# FAQ: ABAC — Attribute-Based Access Control

> **Blueprint refs:** Task 4.2 (authorization strategies)
> **Diagram:** [abac-tag-flow.mmd](../diagrams/abac-tag-flow.mmd)

## The Problem ABAC Solves

RBAC requires listing explicit ARNs in policies. Every new resource = policy edit.
ABAC uses **tags** to match dynamically — no policy edits when resources change.

```
RBAC (explicit ARNs):                  ABAC (tag-based):
├── 50 buckets = 50 ARNs in policy     ├── 1 policy covers ALL buckets
├── New bucket = edit policy            ├── New bucket with tag = auto-access
├── New team = new policy               ├── New team = just tag the role
└── Doesn't scale                       └── Scales infinitely
```

## The Three Tag Condition Keys

```
WHO is calling?          → aws:PrincipalTag/Key    (tag on the role/user)
WHAT are they touching?  → aws:ResourceTag/Key     (tag on the resource)
WHAT are they sending?   → aws:RequestTag/Key      (tag in the API call itself)
```

### When to Use Each

| Condition Key | Answers | Use Case |
|---|---|---|
| `aws:PrincipalTag/Project` | "Who is this caller?" | Only Team=Security roles can access |
| `aws:ResourceTag/Project` | "What resource is being accessed?" | Only access resources matching your project |
| `aws:RequestTag/Project` | "What tags are being applied?" | Enforce tagging at resource creation |

### Concrete Example

```bash
# Role tagged Project=Phoenix calls:
aws ec2 run-instances \
  --tag-specifications "ResourceType=instance,Tags=[{Key=Project,Value=Phoenix}]"
```

| Key | Value | Source |
|---|---|---|
| `aws:PrincipalTag/Project` | `Phoenix` | Tag on the calling role |
| `aws:RequestTag/Project` | `Phoenix` | Tag passed in the API call |
| `aws:ResourceTag/Project` | N/A (instance doesn't exist yet) | Tag on the target resource |

## The ABAC Pattern — Match Principal to Resource

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ABACProjectAccess",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::*/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Project": "${aws:PrincipalTag/Project}"
        }
      }
    }
  ]
}
```

**Translation:** "You can only access S3 objects in buckets tagged with YOUR project."

No ARNs. No policy edits. New bucket tagged `Project=Phoenix` → Phoenix team gets access automatically.

## Enforce Tagging at Creation

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ForceSameProjectTag",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": "arn:aws:ec2:*:*:instance/*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestTag/Project": "${aws:PrincipalTag/Project}"
        }
      }
    }
  ]
}
```

**Translation:** "You can only create instances tagged with YOUR project — can't tag them as someone else's."

## ABAC vs RBAC Decision Table

| Dimension | RBAC | ABAC |
|---|---|---|
| **Scale** | Policy per team/project | One policy for all |
| **New resource** | Edit policy | Just tag it |
| **New team** | New policy + attachments | Tag the role |
| **Granularity** | Explicit ARNs | Tag-based matching |
| **Complexity** | Simple to understand | Requires tagging discipline |
| **Exam signal** | "specific bucket" / "specific role" | "scales" / "without policy changes" / "dynamic" |

## Session Tags (IdP → AWS)

Tags can come from your identity provider via SAML/OIDC assertions:

```
Okta/Entra ID → SAML assertion includes:
  PrincipalTag:Project = Phoenix
  PrincipalTag:Team = Backend

→ IAM Identity Center maps these to session tags
→ Role inherits tags for the session
→ ABAC policies evaluate against them
```

**Exam signal:** "Federated users need project-scoped access without per-user policies" → Session tags + ABAC

## Key Limits/Quotas

| Limit | Value |
|---|---|
| Tags per IAM role/user | 50 |
| Tag key max length | 128 characters |
| Tag value max length | 256 characters |
| Session tags per session | 50 |
| Transitive session tags | 50 |

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Tags are case-sensitive** | `Project` ≠ `project` — mismatch = denied |
| **Not all services support ResourceTag** | Check service docs — most do, some don't |
| **RequestTag only works on create/tag actions** | Can't use it for GetObject (no tags in that call) |
| **PrincipalTag works everywhere** | Always available for the caller |
| **Transitive tags** | Persist through role chaining via `sts:TransitiveTagKeys` |
| **Tag propagation is not instant** | Eventual consistency — new tag may take seconds |
| **ABAC + permission boundary** | Boundary must also allow the actions — ABAC doesn't bypass ceilings |

## K8s Mapping

```
aws:PrincipalTag  ≈  K8s ServiceAccount labels
aws:ResourceTag   ≈  K8s resource labels (on pods, services)
aws:RequestTag    ≈  K8s admission webhook validating labels on create
ABAC policy       ≈  NetworkPolicy with matchLabels selector
Session tags      ≈  OIDC token claims mapped to SA annotations
```

## 🧠 Cheat-Sheet One-Liners

- **PrincipalTag = who. ResourceTag = what. RequestTag = what you're sending.** Three different tags, three different things.
- **ABAC magic:** `"aws:ResourceTag/X": "${aws:PrincipalTag/X}"` — match caller to resource, no ARNs needed.
- **Exam signal:** "scales without policy changes" / "dynamic access" → ABAC with tags.
