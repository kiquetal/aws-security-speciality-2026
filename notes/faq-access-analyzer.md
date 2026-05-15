# FAQ: IAM Access Analyzer

> **Blueprint refs:** Task 4.2 (authorization strategies), Task 1.1 (monitoring)
> **Exam weight:** High — "unused permissions" / "externally accessible" questions

## One-Liner

**Finds overly permissive access (external exposure) and over-provisioned permissions (unused access).**

## Two Analyzer Types — Different Questions

```
EXTERNAL ACCESS:                          UNUSED ACCESS:
"Who OUTSIDE can get IN?"                 "What INSIDE is never USED?"

┌─────────────────────┐                   ┌─────────────────────┐
│  Your Account/Org   │                   │  Your Account/Org   │
│                     │                   │                     │
│  S3 bucket policy:  │                   │  Role: DataTeamRole │
│  Principal: "*"  ◄──┼── Attacker?       │  ├── s3:*        ← used
│                     │                   │  ├── ec2:*       ← used
│  KMS key policy:    │                   │  ├── kms:*       ← NEVER USED
│  Account 999... ◄───┼── Partner?        │  └── rds:*       ← NEVER USED
│                     │                   │                     │
└─────────────────────┘                   └─────────────────────┘

Finding: "This bucket is                  Finding: "This role has kms:*
accessible by anyone                      and rds:* but hasn't used
on the internet"                          them in 90 days — remove them"

SCANS: resource policies                  SCANS: CloudTrail activity logs
(bucket, key, queue, role trust)          (what was actually called)

ANSWERS: "Am I exposed?"                  ANSWERS: "Am I over-provisioned?"
```

## Side-by-Side

| Dimension | External Access | Unused Access |
|---|---|---|
| **Question** | Who outside can reach my resources? | Which permissions are never used? |
| **Scans** | Resource-based policies | CloudTrail activity (90–180 days) |
| **Zone of trust** | Account or Organization boundary | N/A |
| **Resources checked** | S3, KMS, SQS, IAM roles, Lambda, Secrets Manager, SNS, EFS, ECR | IAM roles, users, access keys |
| **Finding examples** | "Bucket accessible by external account" | "Role has unused s3:DeleteBucket permission" |
| **Cost** | Free | Paid (per role/user analyzed per month) |
| **Scope** | ACCOUNT or ORGANIZATION | ACCOUNT_UNUSED_ACCESS or ORGANIZATION_UNUSED_ACCESS |
| **Delegated admin** | ✅ Org-wide | ✅ Org-wide |

## Additional Features

| Feature | What It Does |
|---|---|
| **Policy validation** | Checks policy grammar + security warnings before deployment |
| **Policy generation** | Generates least-privilege policy from CloudTrail activity |
| **Custom policy checks** | Validate policies against your security standards (paid) |

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Not GuardDuty** | Access Analyzer = permission audit. GuardDuty = active threats. |
| **Not a monitor** | Doesn't detect attacks — finds misconfigurations and bloat |
| **Unused access is paid** | External access is free, unused access costs per entity |
| **Org-level analyzer** | One analyzer covers all member accounts (delegated admin pattern) |
| **Automated reasoning** | Uses mathematical proofs, not sampling — findings are provably correct |
| **Integrates with Security Hub** | Findings appear in Security Hub dashboard |

## Exam Decision Table

| Signal | Answer |
|---|---|
| "Which resources are externally accessible?" | **Access Analyzer** (external access) |
| "Right-size permissions" / "least privilege" | **Access Analyzer** (unused access) + policy generation |
| "Credentials being misused RIGHT NOW" | **GuardDuty** (not Access Analyzer) |
| "Validate policy before deploying" | **Access Analyzer** (policy validation) |
| "Generate policy from actual usage" | **Access Analyzer** (policy generation) |

## 🧠 Cheat-Sheet One-Liners

- **External access = "Am I exposed?" Unused access = "Am I over-provisioned?"** Two different analyzers, two different problems.
- **Access Analyzer finds misconfigurations. GuardDuty finds active threats.** Don't confuse them.
- **"Unused permissions" / "overly permissive" = IAM Access Analyzer. "Credentials being misused" = GuardDuty.**
