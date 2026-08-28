# FAQ: Google Workspace → IAM Identity Center Federation (SAML + SCIM)

> **Domain 4 (Identity & Access Management)** — workforce federation, external IdP, SCIM provisioning, delegated administration.
> Pattern: Google Workspace is the IdP (source of truth for *people*); AWS IAM Identity Center trusts it and controls *access*.

---

## 1. The Big Picture (who does what)

```
   START HERE (Google is the front door)
        │
        ▼
┌────────────────────────┐   SAML 2.0 (authn: who you are)    ┌──────────────────────────┐
│   GOOGLE WORKSPACE      │◄──────────────────────────────────►│  IAM IDENTITY CENTER      │
│   (Admin Console)       │                                    │  (delegated to SECURITY   │
│   - the IdP             │   SCIM 2.0 (provisioning: sync)     │   account)                │
│   - MFA enforced HERE   │───────────────────────────────────►│  - permission sets        │
│   - app assignment      │                                    │  - group→account assign   │
└────────────────────────┘                                    └──────────────────────────┘
```

Two channels, two credentials:

| Channel | Protocol | Credential | If it breaks |
|---------|----------|------------|--------------|
| Authentication (login) | SAML 2.0 | SAML certificate | Users **can't log in** (loud, obvious) |
| Provisioning (sync) | SCIM 2.0 | SCIM bearer token | Sync **silently stops** — provisioning AND deprovisioning die (sneaky) |

---

## 2. Account Topology (management + security + 2 workloads)

```
                    AWS Organization
                          │
        ┌─────────────────┼─────────────────────────────┐
        ▼                 ▼                             ▼
┌───────────────┐  ┌───────────────┐          ┌──────────────────┐
│  MANAGEMENT   │  │   SECURITY    │          │  WORKLOAD ACCTS  │
│               │  │ (delegated    │          │  ┌────────────┐  │
│ - owns Org    │─►│  admin for    │          │  │ Account A  │  │
│ - registers   │  │  Id Center)   │──────────┼─►│ (Prod)     │  │
│   delegation  │  │               │  assigns │  └────────────┘  │
│ - then locked │  │ team works    │  access  │  ┌────────────┐  │
│   down        │  │ HERE          │──────────┼─►│ Account B  │  │
└───────────────┘  └───────────────┘          │  │ (Dev)      │  │
        ▲                                      │  └────────────┘  │
        │                                      └──────────────────┘
        └── delegated admin CANNOT assign access into mgmt account ❌
```

**Delegation rules (exam gold):**
- Delegated (security) account manages access for **all member accounts** ✅
- It **cannot** manage access into the **management account** ❌ (blocks privilege escalation to Org root)
- **Enable/disable/delete** the Identity Center instance stays **management-account only**
- "Managing access" ≠ "having access" — you still need a permission set assigned + role assumption to *operate* in an account.

---

## 3. Setup — 100% CLI

> Assumes Organizations is enabled and Identity Center instance exists. Steps that are **inherently console/IdP-side** (SAML metadata exchange, pasting the SCIM token into Google) are marked — those cannot be done via AWS CLI because they live in the Google Admin Console.

### 3.1 Delegate Identity Center admin to the security account
```bash
# Run from the MANAGEMENT account
aws organizations register-delegated-administrator \
  --account-id <SECURITY_ACCOUNT_ID> \
  --service-principal sso.amazonaws.com

# Verify
aws organizations list-delegated-administrators \
  --service-principal sso.amazonaws.com
```
> `sso.amazonaws.com` = Identity Center's service principal (legacy "AWS SSO" name).

### 3.2 Find your instance + identity store IDs (run in security account)
```bash
aws sso-admin list-instances
# → returns InstanceArn (arn:aws:sso:::instance/ssoins-xxxx)
#           IdentityStoreId (d-xxxxxxxxxx)
```

### 3.3 Set identity source to external IdP — *console/IdP step*
- IAM Identity Center → Settings → Identity source → **Change to External identity provider**.
- Download **AWS SP metadata**; in Google Admin add the **AWS IAM Identity Center** SAML app; swap metadata both directions.
- **Enable automatic provisioning** → AWS returns the **SCIM endpoint URL + bearer token**.
- Paste SCIM endpoint + token into Google's auto-provisioning config.
- *(No AWS CLI for the metadata/token exchange — it's cross-console by design.)*

### 3.4 Create permission sets (CLI)
```bash
INSTANCE_ARN=arn:aws:sso:::instance/ssoins-xxxx

aws sso-admin create-permission-set \
  --instance-arn "$INSTANCE_ARN" \
  --name "ReadOnly" \
  --session-duration "PT1H"

# Attach an AWS managed policy to the permission set
aws sso-admin attach-managed-policy-to-permission-set \
  --instance-arn "$INSTANCE_ARN" \
  --permission-set-arn arn:aws:sso:::permissionSet/ssoins-xxxx/ps-xxxx \
  --managed-policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess
```

### 3.5 Assign group → permission set → account (CLI)
```bash
# Find the group's principal ID in the identity store
aws identitystore list-groups \
  --identity-store-id d-xxxxxxxxxx \
  --filters AttributePath=DisplayName,AttributeValue=developers

# Create the assignment
aws sso-admin create-account-assignment \
  --instance-arn "$INSTANCE_ARN" \
  --target-id <DEV_ACCOUNT_ID> --target-type AWS_ACCOUNT \
  --permission-set-arn arn:aws:sso:::permissionSet/ssoins-xxxx/ps-xxxx \
  --principal-type GROUP \
  --principal-id <GROUP_PRINCIPAL_ID>
```

---

## 4. `externalId` — the immutable identity anchor

SCIM needs a **stable primary key** to know "this is the same person" across syncs. If it matches on **email/username**, a rename orphans the user:

```
Alice Smith  alice.smith@corp   (has AWS access)
        │  [marriage → email changes]
        ▼
Alice Jones  alice.jones@corp   ← SCIM sees a NEW person if matching on email
        → old record DEPROVISIONED (access lost)
        → new record created with ZERO entitlements ❌
```

**Fix:** map SCIM `externalId` → Google's **immutable directory user ID** (objectId), never email.
```
externalId = 114857293... (permanent)   →  survives name/email changes ✅
```

- With Google Workspace, `externalId` is often **auto-set** to the immutable ID (you don't pick it — you *verify* it).
- If a mapping dropdown exists: choose **User ID / objectId**, never email/username/displayName.
- Same idea as a DB surrogate key vs natural key.

**Verify externalId (CLI):**
```bash
aws identitystore describe-user \
  --identity-store-id d-xxxxxxxxxx \
  --user-id <USER_ID>
# Look at ExternalIds[].Id:
#   long opaque value  → ✅ immutable ID mapped
#   an email address   → ❌ mutable field mapped, FIX the Google attribute mapping
```

---

## 5. "User not showing up in Identity Center" — the app-assignment gotcha

SCIM only syncs users/groups **assigned to the AWS app in Google**. Your whole directory does NOT sync.

```
GOOGLE WORKSPACE (500 users)
   only [alice, bob] assigned to AWS app  ──SCIM──►  Identity Center has alice, bob
   carol, dave, erin NOT assigned         ──────────►  invisible to AWS
```

**Two separate "assignments" — don't confuse them:**

| Layer | Where | Controls |
|-------|-------|----------|
| 1. **App assignment** | **Google** | *Whether the user EXISTS in AWS at all* (SCIM provisioning) |
| 2. **Access assignment** | **AWS** | *What the user can DO* (permission set → account) |

**Fix (in Google Admin):**
1. Apps → Web and mobile apps → **AWS IAM Identity Center** app.
2. User access → turn app **ON** for the OU/group that needs AWS.
3. Ensure the missing user is IN that OU/group.
4. Wait for the next SCIM cycle → verify:
```bash
aws identitystore list-users --identity-store-id d-xxxxxxxxxx
```

**Decision tree:**
```
User missing in Identity Center?
   ├─ Assigned to AWS app in Google? ──No──► assign OU/group ──► wait for SCIM ──► ✅
   └─ Yes ──► check last sync ran + SCIM token not expired ──► ✅
```

---

## 6. The SCIM token — silent-failure landmine

Bearer token Google presents on every SCIM call (`Authorization: Bearer <token>`).

```
Token valid ───────────────────────────► expiry (up to 1 yr)
   syncs ✅                                    │
                                               ▼  EXPIRED
                                         Google keeps trying
                                         AWS → 401, changes dropped
                                         NO new users, NO deprovisioning ⚠️
                                         (logins still work → you don't notice)
```

The dangerous part: **deprovisioning stops too** — fired employees keep AWS access.

**Zero-downtime rotation (2 tokens can be active):**
```
1. Identity Center → generate NEW token   (2 valid now)
2. Google Admin    → replace token with NEW
3. Confirm a sync succeeds
4. Identity Center → delete OLD token
```

---

## 7. Monitoring the SCIM token (layered)

```
┌─ Layer 1: expiry date in console (passive, must look)
├─ Layer 2: AWS Health event → EventBridge → SNS  (proactive expiry alert) ✅ primary
└─ Layer 3: CloudTrail → CloudWatch alarm on provisioning failures (real-time backstop)
```

**AWS Health → EventBridge → SNS (must be in us-east-1 — Health is global there):**
```bash
aws sns create-topic --name scim-token-alerts --region us-east-1
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:<ACCT>:scim-token-alerts \
  --protocol email --notification-endpoint security-team@corp.com \
  --region us-east-1

# EventBridge rule (pattern below), then target the SNS topic
aws events put-rule --name scim-token-expiry \
  --event-pattern file://health-pattern.json --region us-east-1
aws events put-targets --rule scim-token-expiry \
  --targets Id=1,Arn=arn:aws:sns:us-east-1:<ACCT>:scim-token-alerts \
  --region us-east-1
```
`health-pattern.json`:
```json
{
  "source": ["aws.health"],
  "detail-type": ["AWS Health Event"],
  "detail": { "service": ["SSO"], "eventTypeCategory": ["scheduledChange"] }
}
```
> Note: AWS changed Identity Center CloudTrail event data recently — verify current event names in *"Understanding CloudTrail events for IAM Identity Center"* before hardcoding metric filters.

---

## 8. Must-Not-Skip Checklist

| # | Control | Why |
|---|---------|-----|
| 1 | **MFA at Google layer** | Google is the front door to every AWS account |
| 2 | **`externalId` → immutable ID** | Renames/email changes don't orphan access |
| 3 | **SCIM deprovisioning test** | Offboarding in Google must kill AWS access |
| 4 | **Break-glass account** | Non-federated admin path for when Google/SCIM is down |
| 5 | **Rotate SCIM token before expiry** | Silent failure breaks provisioning + deprovisioning |
| 6 | **Group-based, not per-user** | Onboarding = add to Google group; scales, auditable |
| 7 | **Delegate to security account** | Keep management account locked down |

---

## 9. Evaluation (self-test — active recall)

<details>
<summary>Q1. Why map <code>externalId</code> to Google's directory ID instead of email?</summary>

Email is mutable. If SCIM matches on email and a user's email changes, Identity Center treats them as a new person — deprovisions the old record (loses entitlements) and creates a fresh one with none. The immutable directory ID never changes, so identity (and all access) survives renames.
</details>

<details>
<summary>Q2. A new hire's manager says "I assigned them a permission set but they don't appear in Identity Center." Root cause?</summary>

They were never **assigned to the AWS app in Google**, so SCIM never provisioned them. App assignment (Google) controls existence; access assignment (AWS) controls permissions. Fix in Google Admin, not AWS. (Answer-reveals-the-problem pattern.)
</details>

<details>
<summary>Q3. Logins work fine but no new users have synced for 3 weeks and a terminated employee still has access. MOST LIKELY cause?</summary>

The **SCIM bearer token expired**. SAML (login) is a separate credential and still valid, so logins work — but SCIM provisioning/deprovisioning silently stopped. Rotate the token. This is why deprovisioning-stops is the scary symptom.
</details>

<details>
<summary>Q4. Which Identity Center actions can the delegated security account NOT perform?</summary>

Enable/disable/delete the Identity Center instance, and assign/manage access **into the management account**. These stay management-account only to prevent privilege escalation to Org root.
</details>

<details>
<summary>Q5. What's the recommended way to get proactively alerted before the SCIM token expires?</summary>

Create an **AWS Health** event rule in **EventBridge** (in us-east-1) targeting an **SNS** topic. Don't rely on the passive console date or reminder email. Back it with a CloudTrail-based alarm for actual provisioning failures.
</details>

<details>
<summary>Q6. Two credentials in this integration expire — name them and the different failure symptoms.</summary>

**SAML certificate** → expiry blocks login (loud). **SCIM bearer token** → expiry silently stops user/group sync and deprovisioning (sneaky; logins keep working).
</details>

---

## 10. Exam One-Liners

- Google Workspace = **IdP** (SAML authn + SCIM provisioning); AWS trusts it. Standard enterprise pattern (like Okta/Entra), just less mature SCIM group sync.
- **Delegate Identity Center admin to a security account**; management account only registers the delegation, then stays locked down.
- Delegated admin **cannot** touch the management account or enable/disable the instance.
- Map SCIM **`externalId` → immutable directory ID**, never email/username.
- Only users **assigned to the AWS app in Google** get provisioned — whole directory does NOT sync.
- **SCIM token expiry = silent death** of provisioning AND deprovisioning; rotate with 2-token overlap; monitor via AWS Health → EventBridge → SNS.
- Enforce **MFA at the Google layer** (it's the front door) and keep a **break-glass** non-federated path.
- **Group-based assignments** everywhere: Google group → app (existence) and group → permission set → account (access).
