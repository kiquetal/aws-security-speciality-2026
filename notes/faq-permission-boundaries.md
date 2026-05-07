# FAQ: Permission Boundaries

> **Blueprint refs:** Task 4.2 (authorization strategies)
> **Diagram:** [permission-boundary-delegation.mmd](../diagrams/permission-boundary-delegation.mmd)

## The Problem Boundaries Solve

Developers need `iam:CreateRole` to build Lambda functions, ECS tasks, etc.
But `iam:CreateRole` + `iam:AttachRolePolicy` = privilege escalation.
They can create a role with `AdministratorAccess` and assume it.

```
WITHOUT boundaries:
  Developer (has ec2:*, s3:*, iam:CreateRole)
    → Creates role with AdministratorAccess
    → Assumes it
    → Now has full admin ← ESCALATION

WITH boundaries:
  Developer (has ec2:*, s3:*, iam:CreateRole)
    → Must attach DevBoundary to any role they create
    → DevBoundary caps at s3:* + ec2:* only
    → Even if they attach AdministratorAccess, effective = boundary ∩ identity = s3 + ec2
    → No escalation possible
```

## How It Works

```
Effective permissions = Identity Policy ∩ Permission Boundary

Identity policy: Allow s3:*, ec2:*, kms:*
Boundary:        Allow s3:*, ec2:*
─────────────────────────────────────────
Effective:       s3:*, ec2:*  (kms removed by boundary)
```

- Boundary is a **ceiling** (Gate 3) — never grants, only restricts
- It's a regular IAM policy JSON — just used differently
- Attached to ONE user or role

## The Delegation Pattern (Exam-Critical)

Three deny statements that make self-service IAM safe:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ForceBoundaryOnCreateRole",
      "Effect": "Deny",
      "Action": "iam:CreateRole",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "iam:PermissionsBoundary": "arn:aws:iam::123456789012:policy/DevBoundary"
        }
      }
    },
    {
      "Sid": "DenyRemoveBoundary",
      "Effect": "Deny",
      "Action": "iam:DeleteRolePermissionsBoundary",
      "Resource": "*"
    },
    {
      "Sid": "DenySwapBoundary",
      "Effect": "Deny",
      "Action": "iam:PutRolePermissionsBoundary",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "iam:PermissionsBoundary": "arn:aws:iam::123456789012:policy/DevBoundary"
        }
      }
    }
  ]
}
```

**What each statement prevents:**

| Statement | Prevents |
|---|---|
| ForceBoundaryOnCreateRole | Creating roles without the boundary |
| DenyRemoveBoundary | Removing the boundary after creation |
| DenySwapBoundary | Swapping to a more permissive boundary |

## Boundary vs SCP vs RCP

| Dimension | Permission Boundary | SCP | RCP |
|---|---|---|---|
| **Scope** | One user/role | All principals in account/OU | All resources in account/OU |
| **Set by** | Account admin | Org admin | Org admin |
| **Use case** | Delegation without escalation | Org-wide principal guardrails | Org-wide data perimeter |
| **Where created** | IAM (`iam:PutRolePermissionsBoundary`) | Organizations | Organizations |

## CLI

```bash
# Create the boundary policy
aws iam create-policy \
  --policy-name DevBoundary \
  --policy-document file://boundary.json

# Attach to existing role
aws iam put-role-permissions-boundary \
  --role-name DevRole \
  --permissions-boundary "arn:aws:iam::123456789012:policy/DevBoundary"

# Check what boundary is attached
aws iam get-role --role-name DevRole \
  --query 'Role.PermissionsBoundary.PermissionsBoundaryArn'

# Remove boundary (if allowed)
aws iam delete-role-permissions-boundary --role-name DevRole
```

## Key Limits/Quotas

| Limit | Value |
|---|---|
| Boundaries per role/user | 1 (only one boundary at a time) |
| Boundary policy size | Same as IAM policy (6,144 chars inline / 6,144 managed) |
| Can attach to groups? | ❌ No — users and roles only |

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Only 1 boundary per entity** | Can't stack multiple boundaries — use one comprehensive policy |
| **Doesn't apply to resource-based policies** | If S3 bucket policy grants access directly, boundary on the caller doesn't block it (same-account) |
| **Cross-account: boundary IS evaluated** | When assuming a role cross-account, the role's boundary applies |
| **Boundary doesn't grant anything** | Even with `Allow *` in boundary, you still need an identity policy to grant access |
| **SCP + Boundary + Identity = triple intersection** | All three must allow for access to work |
| **Can't attach to groups** | Only IAM users and roles — not groups |
| **`iam:PermissionsBoundary` condition key** | Use in policies to force boundary attachment |

## K8s Mapping

```
Permission Boundary  ≈  ResourceQuota on a namespace
                     ≈  LimitRange for pods
                     ≈  "You can deploy anything, but max 4 CPU, 8GB RAM"

Delegation pattern   ≈  Admission webhook requiring ResourceQuota on namespace creation
                     ≈  "You can create namespaces, but each must have a quota"
```

## 🧠 Cheat-Sheet One-Liners

- **Boundary = ceiling on ONE role.** Identity policy ∩ boundary = effective. Boundary never grants.
- **Delegation pattern:** Deny CreateRole without boundary + Deny remove/swap boundary = safe self-service IAM.
- **Exam signal:** "developers create their own roles" / "prevent privilege escalation" → Permission Boundary.
