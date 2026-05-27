# FAQ: Declarative Policies (New in C03)

> **Blueprint ref:** Task 6.1 (organization policies to manage permissions)
> **Launched:** Late 2024 — new for SCS-C03
> **Exam weight:** Low (0-1 questions likely)

## One-Liner

**Org-wide policies that enforce a desired resource STATE — no API can put the resource into a non-compliant state, regardless of path.**

## How They Differ from SCPs

| Dimension | SCP | Declarative Policy |
|---|---|---|
| **Mechanism** | Deny specific API calls | Enforce resource attribute state |
| **Bypass risk** | Alternative API paths may exist | None — state is enforced at the service level |
| **Scope** | API actions + conditions | Resource attributes |
| **Grants access?** | Never | Never |
| **Example** | Deny `RunInstances` unless `MetadataHttpTokens=required` | IMDSv2 is the ONLY option — `ModifyInstanceMetadataOptions` can't change it |
| **Where it lives** | AWS Organizations | AWS Organizations |
| **Max per target** | 5 | 5 |

## Supported Services (Very Limited)

| Service | What It Enforces |
|---|---|
| **EC2** | Block public AMI sharing, enforce serial console settings, enforce IMDSv2 as default, block public IP auto-assign |
| **VPC** | Block internet access (no IGW creation) |
| **EBS** | Enforce encryption by default |

> ⚠️ That's it. No S3, no KMS, no IAM, no Lambda. Extremely narrow scope.

## When to Use (Exam Signal)

```
"Ensure X can NEVER be non-compliant regardless of which API is used"
  → Declarative policy

"Block a specific API call unless condition met"
  → SCP

"Detect non-compliance and fix after"
  → Config + remediation
```

## Key Difference: SCP Bypass Risk

```
SCP approach to enforce IMDSv2:
  Deny RunInstances unless MetadataHttpTokens=required
  → Works! But what about ModifyInstanceMetadataOptions?
  → Must also deny that. And any future API that touches IMDS.
  → Whack-a-mole with new APIs.

Declarative policy approach:
  "IMDSv2 is the only option in this org"
  → Service-level enforcement. No API can change it.
  → Future APIs automatically respect it.
  → Zero maintenance.
```

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Not a replacement for SCPs** | Different scope — SCPs cover all services, declarative covers EC2/VPC/EBS only |
| **Management account exempt** | Same as SCPs and RCPs |
| **Inheritance** | Root → OU → account (same as SCPs) |
| **No conditions** | Unlike SCPs, you can't add conditions — it's binary (on/off) |
| **Account-level override** | Cannot be overridden by member accounts |
| **Complements SCPs** | Use both: SCP for API-level control, declarative for state-level guarantee |

## 🧠 Cheat-Sheet One-Liners

- **Declarative policy = "this state is impossible to violate."** SCP = "this API call is blocked." Different layers.
- **Only EC2/VPC/EBS.** If the question mentions S3, KMS, IAM → not declarative policies.
- **"Regardless of which API" = declarative. "Block this specific API" = SCP.**
