# Regional vs Global Services — Centralization Traps

> The exam tests: "You set up X but it's not working in Region Y" = regional service not enabled there.
> Also: "Centralize across regions" = need aggregation/delegation pattern, not just "enable once."

---

## Regional Services (Must Enable Per-Region)

| Service | Trap |
|---|---|
| **GuardDuty** | Enabled in us-east-1, workloads in eu-west-1 → zero findings in eu-west-1 |
| **Security Hub** | Regional. Cross-region = designate aggregation region. NOT global. |
| **Inspector** | Regional. Must enable in each region. |
| **Macie** | Regional. Must enable in each region. |
| **Detective** | Regional. Must enable in each region. |
| **Config** | Regional. Use aggregator for cross-region VIEW (read-only). |
| **KMS keys** | Regional. Call wrong region = Access Denied (key not found). |
| **ACM certs** | Regional. CloudFront = us-east-1 ONLY. ALB = ALB's region. |
| **S3 Batch Operations** | Regional. Job + manifest + target = SAME region. |
| **State Manager** | Regional. One association per region. "500 instances 3 regions" = 3 associations. |
| **CloudTrail Lake** | Regional EDS. Can aggregate org-wide but each EDS is regional. |

---

## Global Services (One Place, Works Everywhere)

| Service | Note |
|---|---|
| **IAM** | Users, roles, policies = global. No region. |
| **Organizations (SCPs, RCPs)** | Global. Apply to all regions automatically. |
| **Route 53** | Global DNS. |
| **CloudFront** | Global CDN. But WAF on CF = must be in us-east-1. |
| **S3 bucket names** | Globally unique (but bucket LIVES in one region). |
| **WAF on CloudFront** | Web ACL MUST be in us-east-1 (global). WAF on ALB = ALB's region. |

---

## Cross-Region Data Patterns (MRK vs Re-Encrypt)

| Service | Cross-Region Method | Needs MRK? | Why |
|---|---|---|---|
| **DynamoDB Global Tables** | Reads locally in each region | ✅ YES | Same key material needed for local decrypt |
| **S3 CRR** | Re-encrypts at destination | ❌ NO | Specify any dest key (GenerateDataKey) |
| **EBS snapshot copy** | Re-encrypts at destination | ❌ NO | Specify any dest key |
| **Secrets Manager replication** | Re-encrypts at destination | ❌ NO | Specify any dest key |
| **RDS cross-region replica** | Re-encrypts at destination | ❌ NO | Specify any dest key |

```
MRK REQUIRED = "reads locally without re-encryption" (DynamoDB Global Tables only)
MRK NOT REQUIRED = "re-encrypts at destination" (everything else)
```

---

## Global Service Events → us-east-1 ONLY

```
These services deliver CloudTrail events to us-east-1 ONLY:
  • IAM (CreateUser, CreateRole, AttachPolicy)
  • STS (AssumeRole, GetSessionToken)
  • CloudFront (CreateDistribution)

TRAP: EventBridge rule for "detect CreateAccessKey" 
      → must be in us-east-1 (not your workload region!)
```

---

## Centralization Patterns (How to See Everything in One Place)

| Goal | Pattern | Trap |
|---|---|---|
| GuardDuty all regions | Delegated admin + auto-enable PER REGION | Must enable in EACH region separately |
| Security Hub cross-region | Designate aggregation region | SH doesn't auto-aggregate — you configure it |
| Config cross-region view | Config aggregator (read-only view) | Aggregator = VIEW only, can't remediate cross-region |
| CloudTrail all regions | Organization trail (one trail, all regions) | Org trail = auto all regions ✅ (exception to the rule) |
| KMS cross-region | Multi-Region Key (MRK) | Key policies are INDEPENDENT per region |
| ACM cross-region | Provision cert in EACH region needed | CF = us-east-1. ALB = ALB region. Can't share certs cross-region. |

---

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| "GuardDuty zero findings" + workloads in other region | GD not enabled in that region |
| "Security Hub is global" | ❌ WRONG. It's regional. |
| "EventBridge rule for IAM events in eu-west-1" | Won't fire — IAM events go to us-east-1 only |
| "KMS Access Denied despite correct key policy" | Calling wrong region endpoint |
| "Config aggregator auto-remediates cross-region" | ❌ Aggregator is READ-ONLY view |
| "One State Manager association for 3 regions" | ❌ Need one per region (regional service) |
| "ACM cert in us-east-1 for ALB in eu-west-1" | ❌ ALB cert must be in ALB's region |
| "Org trail = per region setup" | ❌ Org trail = auto all regions (the exception) |

---

## 🧠 Exam One-Liners

- **"Zero findings in Region X" = service not enabled in that region.** GuardDuty, Inspector, Macie = all regional.
- **Security Hub = REGIONAL.** Cross-region = aggregation region. Not global.
- **IAM/STS/CloudFront events → us-east-1 ONLY.** EventBridge rules for these must be in us-east-1.
- **KMS keys are REGIONAL.** Wrong region = Access Denied. MRK = same material across regions but independent policies.
- **Config aggregator = VIEW only.** Can't remediate cross-region from aggregator.
- **Org trail = the ONE exception.** One trail, auto-covers all regions. No per-region setup.
- **ACM: CF = us-east-1. ALB = ALB's region.** Can't share certs cross-region.
