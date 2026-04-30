# Scenario 4 — IAM Backdoor Persistence After a Breach

## Situation

Your SOC team closed an incident last week involving a compromised EC2 instance. The instance was isolated and replaced. However, this morning CloudTrail reveals suspicious activity:

- `sts:AssumeRole` calls from an **unknown external AWS account** (`999888777666`) assuming a role called `support-debug-role` in your production account.
- The role was **created 6 days ago** — during the original incident window — via `iam:CreateRole` by the same compromised EC2 instance's role.
- The role's trust policy allows `arn:aws:iam::999888777666:root` as a principal.
- The role has `AdministratorAccess` attached.

The attacker planted a **backdoor role** during the original incident that your team missed during eradication.

## Part A — Understanding the Threat

### Questions

1. What makes this type of persistence particularly dangerous compared to a stolen access key?
2. The trust policy specifies `arn:aws:iam::999888777666:root`. What does `:root` mean here, and is this good practice even for trusted accounts?

### Answers

#### 1 — Why backdoor roles are worse than stolen keys

| Factor | Stolen Access Key | Backdoor Role |
|--------|------------------|---------------|
| Survives credential rotation? | ❌ Revoked when key is deleted | ✅ `AssumeRole` generates fresh credentials every call |
| Requires foothold in your account? | ✅ Key must be used from somewhere | ❌ Attacker calls from their own account |
| Self-renewing? | ❌ Static — once dead, it's dead | ✅ New temporary credentials on every `AssumeRole` call |
| Visible in normal key audits? | ✅ Shows up in IAM credential report | ❌ It's a role, not a user — easy to miss |

The attacker has **unlimited, self-renewing admin access** from outside your perimeter until you find and kill the role.

#### 2 — What `:root` means in a trust policy

`arn:aws:iam::999888777666:root` means **every IAM entity** (every user, every role) in account `999888777666` can assume this role. It does NOT mean only the root user.

Best practice for cross-account trust:

| Trust Principal | Risk |
|----------------|------|
| `arn:aws:iam::999:root` | 🔴 Any identity in that account can assume |
| `arn:aws:iam::999:role/SpecificRole` | 🟢 Only that specific role can assume |
| `arn:aws:iam::999:role/SpecificRole` + `sts:ExternalId` | 🟢 Best — also prevents confused deputy |

---

## Part B — Eradication

### Questions

3. Walk through the **exact order** of operations to kill this backdoor. Why does order matter?
4. Explain how the `aws:TokenIssueTime` deny policy works and why it's the critical first step.

### Answers

#### 3 — Eradication sequence

```
1. Revoke sessions → 2. Edit trust policy → 3. Detach permissions → 4. Investigate → 5. Delete role
```

| Step | Action | Why |
|------|--------|-----|
| 1 | **Revoke active sessions** — attach inline deny-all with `aws:TokenIssueTime` | Kills credentials the attacker already has |
| 2 | **Edit trust policy** — remove external account, trust only your security team | Stops new `AssumeRole` calls |
| 3 | **Detach `AdministratorAccess`** | Defense in depth — even if somehow assumed, role can't do anything |
| 4 | **Investigate** — query CloudTrail for all actions by this role's ARN | Determine blast radius |
| 5 | **Delete the role** — only after investigation is complete | Permanent eradication |

**Why order matters:** If you skip step 1 and go straight to editing the trust policy, the attacker might already have valid temporary credentials (up to **12 hours** max session duration). Those credentials **keep working** even after you change the trust policy — the trust policy only controls who can *get new* credentials, not who can *use existing* ones.

#### 4 — How `aws:TokenIssueTime` deny works

Attach this **inline policy** directly to the backdoor role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "DateLessThan": {
          "aws:TokenIssueTime": "2026-04-30T12:00:00Z"
        }
      }
    }
  ]
}
```

**How it works step by step:**

1. When the attacker called `AssumeRole`, STS issued temporary credentials with a `TokenIssueTime` timestamp (e.g., `2026-04-30T08:00:00Z`).
2. Every API call made with those credentials carries that `TokenIssueTime`.
3. The deny policy says: "If `TokenIssueTime` is before `12:00:00Z`, deny everything."
4. Since `08:00:00Z < 12:00:00Z`, **every action is denied**. The attacker's session is dead.

**Key details:**
- **`Action` is `*`**, not `sts:*` — deny everything, not just STS calls.
- **`DateLessThan`** — tokens issued *before* the cutoff are denied.
- **Only affects temporary credentials** — long-term access keys don't carry `TokenIssueTime` (which is why you must handle backdoor keys separately).
- **The role still exists** — you can still investigate CloudTrail logs that reference its ARN.

**See diagram:** `diagrams/iam-backdoor-eradication-flow.png`

---

## Part C — Prevention

### Questions

5. SCPs restrict what principals in your org can do. Can an SCP block an external account from calling `AssumeRole` on a role in your account?
6. What control at the Organizations level prevents roles in your accounts from trusting external accounts outside your org?

### Answers

#### 5 — SCPs cannot block incoming AssumeRole

No. SCPs apply to **principals within your organization**. The `AssumeRole` call originates from account `999888777666` (outside your org) — your SCPs don't apply to them. The **trust policy on the role** is what grants access.

However, you CAN use an SCP to prevent principals **in your org** from creating roles with external trust policies in the first place:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "iam:CreateRole",
        "iam:UpdateAssumeRolePolicy"
      ],
      "Resource": "*",
      "Condition": {
        "ForAnyValue:StringNotLike": {
          "iam:ResourceTag/AllowExternalTrust": "true"
        },
        "StringNotEquals": {
          "aws:PrincipalOrgID": "${aws:ResourceOrgID}"
        }
      }
    }
  ]
}
```

#### 6 — Preventive controls

| Control | What it does |
|---------|-------------|
| **SCP** denying `iam:CreateRole` / `iam:UpdateAssumeRolePolicy` with external principals | Prevents anyone in your org from creating roles that trust outside accounts |
| **IAM Access Analyzer** | Continuously scans for resources shared with external entities — would have flagged this backdoor role |
| **Config rule** `iam-role-no-external-trust` (custom) | Detects roles with trust policies referencing accounts outside your org |

---

## Common Exam Traps

1. **Trust policy `:root` ≠ root user.** `arn:aws:iam::123:root` means every identity in account `123`, not the root user specifically.
2. **Changing the trust policy doesn't kill existing sessions.** Temporary credentials remain valid until they expire (up to 12h). You MUST revoke sessions with `aws:TokenIssueTime`.
3. **SCPs don't block external callers.** SCPs only apply to principals within your organization. Use trust policies and IAM Access Analyzer for external access.
4. **Don't delete the role before investigating.** CloudTrail logs reference the role ARN — you need it to determine what the attacker did.
5. **`aws:TokenIssueTime` only works on temporary credentials.** Long-term access keys don't carry this field — you must delete those separately.
