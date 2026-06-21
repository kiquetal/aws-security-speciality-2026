# FAQ: CloudFormation Stack Policy

> **Blueprint ref:** Task 6.2 (secure deployment strategy)
> **Exam trap frequency:** HIGH — failed 3 times (Q1138, Q1225, Q1232)

---

## What Stack Policy Does (One Sentence)

Prevents CloudFormation from modifying, replacing, or deleting specific resources INSIDE a stack during updates.

---

## Evaluation Logic (Exam-Critical)

```
DEFAULT = IMPLICIT DENY ON ALL UPDATE ACTIONS

If no Allow statement for a resource → that resource CANNOT be updated.
Explicit Deny always wins over Allow (same as IAM).
```

### The Correct Pattern

```json
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "Update:*",
      "Principal": "*",
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": ["Update:Replace", "Update:Delete"],
      "Principal": "*",
      "Resource": "LogicalResourceId/AuroraCluster"
    },
    {
      "Effect": "Deny",
      "Action": "Update:Delete",
      "Principal": "*",
      "Resource": "LogicalResourceId/MyLambda"
    }
  ]
}
```

**Translation:**
- Everything can be updated (Allow * baseline)
- Aurora: can be modified in-place, but NEVER replaced or deleted
- Lambda: can be modified or replaced, but NEVER deleted
- SQS (no Deny): unrestricted

### Update Action Types

| Action | What It Means | Physical ID Changes? |
|---|---|---|
| `Update:Modify` | In-place property change | No |
| `Update:Replace` | New resource created, old deleted | YES — new physical ID |
| `Update:Delete` | Resource removed from template | N/A — gone |
| `Update:*` | All of the above | — |

---

## Stack Policy vs Other Protections

| Mechanism | Protects Against | Scope |
|---|---|---|
| **Stack Policy** | CF updating/replacing/deleting resources INSIDE stack | Per-resource within stack |
| **Termination Protection** | Deleting the ENTIRE stack | Whole stack |
| **DeletionPolicy: Retain** | Resource NOT deleted when removed from template | Per-resource (CF attribute) |
| **SCP** | ANY API call org-wide | Org/OU/Account |
| **cfn-guard** | Non-compliant template content at deploy | Template validation |

---

## Exam Traps

| Trap | Truth |
|---|---|
| "Stack Policy prevents Console changes" | ❌ NO — only CF updates. Console/CLI direct changes bypass it. |
| "Default is Allow all" | ❌ NO — default is implicit DENY all. Must start with Allow. |
| "Deny only Replace+Delete is enough" | ❌ Depends — if no Allow exists, Modify is also blocked by default. |
| "Stack Policy can be updated" | ✅ Yes — but requires temporary override for the update. |
| "Termination protection prevents resource deletion" | ❌ NO — only prevents `DeleteStack`. Resources inside can still be removed via template update. |

---

## Decision Pattern for Exam

```
"Protect resources inside stack from CF updates" → Stack Policy
"Prevent stack deletion" → Termination Protection
"Prevent API calls org-wide" → SCP
"Validate template before deploy" → cfn-guard / Config proactive
"Keep resource even if removed from template" → DeletionPolicy: Retain
```

---

## 🧠 Cheat-Sheet One-Liners

- Stack Policy default = implicit deny. Start with Allow Update:* on all, then Deny dangerous actions on sensitive resources.
- Stack Policy only protects against CF updates — NOT Console/CLI direct changes.
- Termination protection = prevent stack deletion. Stack Policy = prevent resource modification inside stack. Different layers.
- Update:Replace = new physical ID (dangerous). Update:Modify = in-place (usually safe).
