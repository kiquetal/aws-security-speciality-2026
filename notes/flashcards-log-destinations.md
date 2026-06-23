# Log Delivery Destinations & S3 Delivery Mechanisms

> Print this. Memorize the exceptions (S3 ONLY, CW ONLY). The exam tests the gaps.

---

## Where Each Service Can Deliver Logs

| Service | S3 | CW Logs | Firehose | EventBridge | Trap |
|---|---|---|---|---|---|
| **VPC Flow Logs** | ✅ | ✅ | ✅ | ❌ | All 3 data destinations |
| **CloudTrail** | ✅ | ✅ | ❌ | ✅ (auto) | EB = mgmt events automatic |
| **ELB Access Logs** | ✅ | ❌ | ❌ | ❌ | **S3 ONLY** — use Athena to query |
| **WAF Logs** | ✅ | ✅ | ✅ | ❌ | All 3 except EB |
| **R53 DNS Query Logging (public zone)** | ❌ | ✅ | ❌ | ❌ | **CW Logs ONLY** |
| **R53 Resolver Query Logging (VPC)** | ✅ | ✅ | ✅ | ❌ | All 3 |
| **S3 Server Access Logs** | ✅ | ❌ | ❌ | ❌ | **S3 ONLY** |
| **CloudFront Access Logs** | ✅ | ❌ | ❌ | ❌ | **S3 ONLY** |
| **GuardDuty findings** | ✅ | ❌ | ❌ | ✅ (auto) | S3 export + EB native |
| **Config snapshots/history** | ✅ | ❌ | ❌ | ❌ | **S3 ONLY** |
| **Inspector findings** | ❌ | ❌ | ❌ | ✅ | EB → Security Hub |
| **Macie findings** | ❌ | ❌ | ❌ | ✅ | EB → Security Hub |

---

## Exam Traps (Memorize These)

- **"CW Logs Insights query on ELB logs returns zero"** → ELB logs are in S3, not CW Logs. Use Athena.
- **"Public DNS query logging to S3"** → IMPOSSIBLE. CW Logs only.
- **"GuardDuty → Lambda automatically"** → EventBridge (automatic, zero config).
- **"VPC Flow Logs already in CW, query top talkers"** → CW Logs Insights (not Athena).

---

## Which Services Need `s3:GetBucketAcl`?

### YES — Legacy "Old Four" (pre-2018, use ACL ownership check)

| Service | Why |
|---|---|
| **S3 Server Access Logging** | Validates target bucket ownership via log delivery group ACL |
| **CloudTrail delivery** | Verifies bucket ownership before writing trail logs |
| **AWS Config delivery** | Verifies bucket ownership before writing snapshots |
| **ELB access log delivery** | Verifies bucket ownership before writing access logs |

### NO — Modern services (use bucket policy with service principal)

| Service | Mechanism Instead |
|---|---|
| VPC Flow Logs | Bucket policy for `delivery.logs.amazonaws.com` |
| GuardDuty export | Bucket policy for `guardduty.amazonaws.com` |
| Inspector SBOM | Bucket policy for `inspector2.amazonaws.com` |
| Macie results | Bucket policy for `macie.amazonaws.com` |
| CRR/SRR | Replication role permissions (no ACL check) |
| Security Lake | Bucket policy for `securitylake.amazonaws.com` |

### The Rule

```
Pre-2018 service delivering to S3 → GetBucketAcl (legacy ACL pattern)
Post-2018 service delivering to S3 → Bucket policy with service principal
```

**Mnemonic: "CCES" = CloudTrail, Config, ELB, S3-logging = the old four that need GetBucketAcl.**

---

## Log Delivery Auth Mechanisms

| Log Source | To S3 via | To CW Logs via |
|---|---|---|
| **VPC Flow Logs** | IAM role | IAM role |
| **CloudTrail** | Bucket policy | IAM role |
| **R53 Resolver** | Bucket policy | Log group resource policy |
| **WAF Logs** | Bucket policy | Log group resource policy |
| **ELB** | Bucket policy (ELB account ID) | N/A |
| **S3 Server Access Logs** | ACL (log delivery group) | N/A |

**VPC Flow Logs is the only service using IAM role for ALL delivery targets.**
