# IAM Backdoor Eradication

## Core Principle: Delete → Audit → Revoke → Reissue

Order matters. Don't issue new credentials until the policy state is verified clean.

## Eradication Sequence

### Step 1 — Delete Backdoor Access Keys

**Delete** (not deactivate) the attacker-created access keys.

**Why delete, not deactivate?**
- Deactivated keys can be reactivated by anyone with `iam:UpdateAccessKey`
- Deletion is permanent and irreversible

### Step 2 — Audit IAM Policies

Check if the attacker modified the user's permissions:
- Review attached managed policies
- Review inline policies
- Check for unauthorized policy attachments (e.g., `iam:*`, `s3:*`)
- Use CloudTrail to trace all `iam:AttachUserPolicy`, `iam:PutUserPolicy` events

### Step 3 — Remove Unauthorized Policies

Remove any policies the attacker attached or modified.

### Step 4 — Revoke Active Sessions

Attach an **inline deny-all policy** with a time-based condition to invalidate all temporary credentials issued before remediation:

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
          "aws:TokenIssueTime": "2025-01-15T12:00:00Z"
        }
      }
    }
  ]
}
```

**Key details:**
- **Action is `*`**, not `sts:*` — deny everything for old sessions, not just STS calls
- **Condition operator is `DateLessThan`** — tokens issued before the timestamp are denied
- **Condition key is `aws:TokenIssueTime`** — carried by temporary credentials from `AssumeRole`, federation, etc.
- **Only affects temporary credentials** — long-term access keys don't have a `TokenIssueTime`, which is why you must delete backdoor keys separately

### Step 5 — Issue New Credentials

Only after verifying the policy state is clean, generate new access keys for the legitimate user.

## Detection with CloudTrail

Key API calls to monitor for backdoor activity:
- `iam:CreateAccessKey` — attacker creating new keys
- `iam:AttachUserPolicy` — attacker escalating privileges
- `iam:PutUserPolicy` — attacker adding inline policies
- `iam:CreateUser` — attacker creating new users
- `iam:CreateLoginProfile` — attacker enabling console access
- `sts:AssumeRole` — attacker assuming roles

## IAM Best Practices for the Exam

- Always use `Condition` keys for fine-grained control
- Use specific resource ARNs — never `Resource: "*"` without conditions
- Prefer `Deny` policies for security controls
- Use permissions boundaries to limit maximum permissions
- Rotate credentials regularly
- Enable MFA for all human users
