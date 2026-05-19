# Cognito — Slide Deck

---

## Two Services, One Name

```
Amazon Cognito
├── User Pool  → WHO ARE YOU? (authentication)
└── Identity Pool → WHAT CAN YOU DO IN AWS? (authorization)
```

They're separate. You can use both together or independently.

---

## User Pool = Directory

```
User Pool = your app's user database

├── Sign-up / sign-in (email, phone, username)
├── MFA (TOTP, SMS, email)
├── Password policies
├── OAuth 2.0 / OIDC tokens (ID token, access token, refresh token)
├── Hosted UI (or custom)
└── Federation: Google, Facebook, Apple, SAML, OIDC

OUTPUT: JWT tokens (ID + Access + Refresh)
```

🧠 User Pool = **authentication**. "Prove who you are."

---

## Identity Pool = Credential Broker

```
Identity Pool = vends temporary AWS credentials

INPUT:  Token from User Pool (or Google, Facebook, SAML, OIDC)
OUTPUT: Temporary AWS credentials (AccessKey + SecretKey + SessionToken)

├── Authenticated role → real user, scoped permissions
├── Unauthenticated role → guest, minimal permissions
└── Role selection: rules-based or token-based
```

🧠 Identity Pool = **authorization**. "Here are your AWS permissions."

---

## How They Work Together

```
Mobile App
    │
    ▼
┌──────────────┐
│  User Pool   │ ← user signs in (email + password + MFA)
│              │ → returns JWT tokens
└──────┬───────┘
       │ ID token
       ▼
┌──────────────┐
│ Identity Pool│ ← exchanges token for AWS creds
│              │ → returns STS temporary credentials
└──────┬───────┘
       │ temp creds
       ▼
┌──────────────┐
│  S3 / DDB    │ ← app accesses AWS resources directly
└──────────────┘
```

---

## Per-User S3 Access (Exam Pattern)

```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::mybucket/${cognito-identity.amazonaws.com:sub}/*"
}
```

Each user can only access their own folder.

`sub` = unique Cognito identity ID per user.

---

## Identity Center vs Cognito

| | Identity Center | Cognito |
|---|---|---|
| **Who** | Employees | App users (customers) |
| **Access to** | AWS Console + CLI | Your app + AWS resources |
| **Credentials** | Permission sets → IAM roles | JWT tokens + optional temp creds |
| **Sign-up** | ❌ Admin provisions | ✅ Self-service |
| **Exam signal** | "workforce" / "SSO" | "mobile app" / "customer" / "sign-up" |

🧠 **Never mix them.** Workforce = Identity Center. Customers = Cognito.

---

## Unauthenticated Access

```
Guest user (no login)
  → Identity Pool assigns "unauth role"
  → Minimal permissions (e.g., read-only public data)
  → No friction (no login screen)
  → Still uses temporary credentials (not public access)
```

Exam signal: "guest access without login" → Cognito Identity Pool unauth role.

---

## Token Types (User Pool Output)

| Token | Contains | Use |
|---|---|---|
| **ID token** | User attributes (email, name, groups) | Pass to Identity Pool or your backend |
| **Access token** | Scopes, authorized actions | Call your API (API Gateway authorizer) |
| **Refresh token** | Long-lived, gets new ID/access tokens | Silent re-auth (no re-login) |

---

## Key Limits

| Limit | Value |
|---|---|
| Users per User Pool | 40 million |
| User Pools per account | 1,000 |
| Identity Pools per account | 1,000 |
| Token validity (ID/Access) | 5 min – 1 day |
| Refresh token validity | 1 hour – 10 years |
| Custom attributes | 50 per User Pool |

---

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **User Pool ≠ Identity Pool** | Authentication vs authorization. Different resources. |
| **Identity Pool doesn't store users** | It only vends credentials. User data lives in User Pool. |
| **Cognito NOT a source for Identity Center** | Can't use Cognito as IdP for workforce SSO. |
| **Per-user S3** | Use `${cognito-identity.amazonaws.com:sub}` in IAM policy Resource. |
| **Unauthenticated = still IAM role** | Guest access uses temp creds with a restricted role, not public access. |
| **API Gateway integration** | Cognito User Pool can be a native authorizer for API Gateway. |
| **Lambda triggers** | Pre/post sign-up, pre/post auth, custom messages, migration. |

---

## Exam Decision Table

| Signal | Answer |
|---|---|
| "Mobile app needs temp AWS creds" | **Cognito Identity Pool** |
| "Customer sign-up/sign-in" | **Cognito User Pool** |
| "Per-user S3 folders" | **Identity Pool + IAM policy with sub** |
| "Employee SSO to AWS Console" | **Identity Center** (NOT Cognito) |
| "Guest access without login" | **Identity Pool unauthenticated role** |
| "Authorize API Gateway with user token" | **User Pool as authorizer** |

---

## K8s Mapping

```
User Pool       ≈  Keycloak / Dex (authentication)
Identity Pool   ≈  IRSA (IAM Roles for Service Accounts)
ID token        ≈  OIDC token from Dex
Temp AWS creds  ≈  Pod's projected service account token → STS
Per-user S3     ≈  RBAC scoped by ServiceAccount annotation
```

---

## 🧠 One-Liners

- **User Pool = authentication (JWT). Identity Pool = authorization (AWS creds).**
- **"Mobile app + AWS resources" = Identity Pool.**
- **"Per-user S3 prefix" = `${cognito-identity.amazonaws.com:sub}` in Resource ARN.**
- **Cognito = customers. Identity Center = employees. Never mix.**
