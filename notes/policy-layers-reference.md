# AWS Policy Layers — The 5 Gates

> **Blueprint refs:** Task 4.2 (authorization strategies), Task 6.1 (org policies)
> **Exam weight:** This is the #1 hardest topic on SCS-C03. Master this = master the exam.

## The Mental Model

A request must pass through ALL 5 gates. An explicit Deny in ANY gate = DENIED.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AWS POLICY LAYERS                                 │
│                                                                     │
│  Think of it as 5 security gates. A request must pass ALL of them.  │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ GATE 1: SCP (Organization — PRINCIPAL side)                   │  │
│  │                                                               │  │
│  │  "What can people IN MY ORG do?"                              │  │
│  │                                                               │  │
│  │  • Set by: Org admin                                          │  │
│  │  • Scope: All principals in all member accounts               │  │
│  │  • Grants access? NEVER — only restricts                      │  │
│  │  • Affects external callers? NO ← this is the gap             │  │
│  │  • Affects management account? NO                             │  │
│  │  • K8s equivalent: OPA policy on ServiceAccounts              │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                              ↓ passes                               │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ GATE 2: RCP (Organization — RESOURCE side)                    │  │
│  │                                                               │  │
│  │  "What can ANYONE do to MY RESOURCES?"                        │  │
│  │                                                               │  │
│  │  • Set by: Org admin                                          │  │
│  │  • Scope: All resources in all member accounts                │  │
│  │  • Grants access? NEVER — only restricts                      │  │
│  │  • Affects external callers? YES ← closes the SCP gap         │  │
│  │  • Affects management account resources? NO                   │  │
│  │  • Affects service-linked roles? NO (exempt)                  │  │
│  │  • Affects AWS managed KMS keys? NO (exempt)                  │  │
│  │  • K8s equivalent: OPA policy on Pods/Services (resource)     │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                              ↓ passes                               │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ GATE 3: Permission Boundary (per IAM entity)                  │  │
│  │                                                               │  │
│  │  "What is the MAX this specific role/user can ever do?"       │  │
│  │                                                               │  │
│  │  • Set by: Admin who created the role                         │  │
│  │  • Scope: One IAM user or role                                │  │
│  │  • Grants access? NEVER — only restricts                      │  │
│  │  • K8s equivalent: ResourceQuota on a namespace               │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                              ↓ passes                               │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ GATE 4: Identity-Based Policy (on the caller)                 │  │
│  │                                                               │  │
│  │  "What is this role/user ALLOWED to do?"                      │  │
│  │                                                               │  │
│  │  • Set by: Admin or developer                                 │  │
│  │  • Scope: One IAM user, group, or role                        │  │
│  │  • Grants access? YES                                         │  │
│  │  • Example: AWSLambdaBasicExecutionRole                       │  │
│  │  • K8s equivalent: RBAC RoleBinding                           │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                              ↓ passes                               │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ GATE 5: Resource-Based Policy (on the resource)               │  │
│  │                                                               │  │
│  │  "Who does THIS SPECIFIC RESOURCE allow in?"                  │  │
│  │                                                               │  │
│  │  • Set by: Developer / resource owner                         │  │
│  │  • Scope: One resource (one bucket, one key, one queue)       │  │
│  │  • Grants access? YES — can even grant cross-account          │  │
│  │  • Example: S3 bucket policy, KMS key policy                  │  │
│  │  • K8s equivalent: NetworkPolicy on a specific pod            │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ⚠️  An EXPLICIT DENY in ANY gate = request DENIED. Always.        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## The Formula

```
Effective access = Gate1 ∩ Gate2 ∩ Gate3 ∩ (Gate4 ∪ Gate5)
                   ───────────────────────  ──────────────
                   CEILINGS (never grant)   GRANTS (give access)
                   ALL must allow           EITHER can grant
```

- Gates 1–3 are **ceilings** — they never grant permissions, only restrict
- Gates 4–5 are **grants** — they actually give permissions
- The `∪` (union) between Gates 4 and 5 means: either the identity policy OR the resource policy can grant access
- But all three ceilings must allow it

## What Is an RCP?

> Full deep dive: [faq-rcp.md](./faq-rcp.md)

**Resource Control Policy (RCP)** — an AWS Organizations policy type launched November 2024 (new for SCS-C03).

```
SCP = "What can people IN MY ORG do?"        → controls PRINCIPALS
RCP = "What can ANYONE do to MY RESOURCES?"   → controls RESOURCES
```

| Dimension | SCP | RCP |
|---|---|---|
| **Controls** | Principals (IAM users/roles) | Resources (S3, KMS, STS, SQS, etc.) |
| **Affects external callers?** | ❌ No — only your org's principals | ✅ Yes — evaluated on resource regardless of caller |
| **Affects management account?** | ❌ No | ❌ No (resources in mgmt account exempt) |
| **Affects service-linked roles?** | ✅ Yes | ❌ No — SLRs are exempt |
| **Affects AWS managed KMS keys?** | ✅ Yes | ❌ No — only customer managed keys |
| **Grants permissions?** | ❌ Never | ❌ Never |
| **Max size** | 5,120 characters | 5,120 characters |
| **Where it lives** | AWS Organizations | AWS Organizations |

**RCPs only support a subset of services (exam-critical):**
- ✅ S3, KMS, STS, SQS, Secrets Manager, DynamoDB, ECR, CloudWatch Logs, Cognito
- ❌ NOT supported: EC2, RDS, Lambda, IAM, SNS, EBS, EFS

> ⚠️ If a question asks about restricting external access to a service NOT on this list, RCPs won't help — you need resource-based policies or SCPs.

## Why RCPs Exist — The Gap SCPs Leave Open

```
SCENARIO: Developer puts Principal:"*" on an S3 bucket policy

                        Your Org                          External
                     ┌──────────────┐                   ┌──────────┐
                     │  Account A   │                   │ Attacker │
                     │              │                   │ Account  │
                     │  S3 Bucket   │                   │          │
                     │  Policy:     │◄──────────────────│ GetObject│
                     │  Allow *     │   cross-account   │          │
                     └──────────────┘   request         └──────────┘

WITHOUT RCP:
  SCP?     → doesn't apply (attacker is NOT in your org)
  RCP?     → doesn't exist
  Boundary → doesn't apply (attacker's role, not yours)
  Identity → doesn't apply (attacker's policy)
  Resource → bucket policy says Allow *
  Result:  ✅ ALLOWED — attacker reads your data

WITH RCP:
  SCP?     → doesn't apply (attacker is NOT in your org)
  RCP?     → Deny if PrincipalOrgID ≠ my-org
  Result:  ❌ DENIED — RCP blocks it, bucket policy doesn't matter
```

## Quick Reference

```
WHO SETS IT?        WHAT DOES IT CONTROL?         GRANTS ACCESS?
─────────────       ──────────────────────        ──────────────
Org admin    ──►    SCP  ── your PRINCIPALS  ──►  No (ceiling)
Org admin    ──►    RCP  ── your RESOURCES   ──►  No (ceiling)
Role admin   ──►    Boundary ── one role     ──►  No (ceiling)
Admin/dev    ──►    Identity policy ── role  ──►  YES
Dev/owner    ──►    Resource policy ── resource►  YES
```

## Same-Account vs Cross-Account (Exam-Critical)

```
SAME-ACCOUNT REQUEST (Role in Account A → Bucket in Account A):
  Either identity policy OR resource policy can grant access.
  Only one needs to say Allow (the other can be silent).

CROSS-ACCOUNT REQUEST (Role in Account B → Bucket in Account A):
  BOTH identity policy AND resource policy must grant access.
  Account B's role needs Allow + Account A's bucket policy needs Allow.
  Exception: If Account B is in the same org, resource-based policy alone
  can grant access (no identity policy needed on the caller side).
```

## Resources That Have Resource-Based Policies

| Resource | Policy Name | Common Use |
|---|---|---|
| S3 Bucket | Bucket policy | Cross-account access, enforce encryption |
| KMS Key | Key policy | Control who can use/manage the key |
| Lambda Function | Function policy | Allow API Gateway/S3/EventBridge to invoke |
| SQS Queue | Queue policy | Allow SNS/S3/Lambda to send messages |
| SNS Topic | Topic policy | Allow cross-account publish |
| Secrets Manager | Resource policy | Cross-account secret access |
| CloudWatch Log Group | Resource policy | Allow services to write logs |
| ECR Repository | Repository policy | Cross-account image pulls |

## Exam Gotchas

1. **Explicit Deny wins everywhere** — doesn't matter which gate, Deny always beats Allow
2. **SCP doesn't affect management account** — only member accounts
3. **RCP doesn't affect management account resources** — only member account resources
4. **RCP doesn't affect service-linked roles** — AWS services need them to function
5. **RCP doesn't affect AWS managed KMS keys** — only customer managed keys
6. **Permission boundary + identity policy = intersection** — both must allow
7. **Cross-account needs both sides** — caller's identity policy + resource's policy
8. **Session policies** (6th gate, not shown) — further scope down AssumeRole sessions
9. **KMS is special** — key policy is REQUIRED, identity policy alone is never enough
10. **S3 bucket policy can grant access to external accounts** — that's why RCPs exist
