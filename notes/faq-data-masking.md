# FAQ: Data Masking — CloudWatch Logs & SNS Data Protection

> **Blueprint refs:** Task 5.3.4 (mask sensitive data)
> **New in C03:** Yes — brand new, no C02 precedent
> **Related:** Macie (S3 only, different service)

## One-Liner

**Detect and mask sensitive data in CloudWatch Logs and SNS messages in real-time — no code changes.**

## The Problem It Solves

```
WITHOUT data protection policies:
  App logs: "User john@acme.com paid with card 4111-1111-1111-1111"
  → PII sits in CloudWatch Logs forever
  → Anyone with logs:GetLogEvents sees raw PII
  → Compliance violation (PCI DSS, GDPR, HIPAA)

WITH CloudWatch Logs data protection:
  App logs: "User j***@***.com paid with card ****-****-****-1111"
  → PII masked automatically at ingestion
  → No application code changes
  → Unmasked access requires separate IAM permission
```

## Two Services (Don't Confuse)

| Service | What It Protects | Where |
|---|---|---|
| **CloudWatch Logs data protection** | Log events in log groups | CloudWatch Logs |
| **SNS message data protection** | Messages published to topics | SNS topics |

Both use the same concept: managed data identifiers + policy → detect + mask/audit.

## CloudWatch Logs Data Protection (Primary Exam Target)

### How It Works

```
App → PutLogEvents → CloudWatch Logs
                         │
                         ▼
                    Data Protection Policy
                    ├── Scan log events for sensitive data
                    ├── Match against data identifiers (SSN, credit card, etc.)
                    └── Actions:
                        ├── Audit: send finding to another log group / S3 / Firehose
                        ├── Deidentify (mask): replace with ****
                        └── Both (typical)
                         │
                         ▼
                    Stored log event: masked
                    "Card: ****-****-****-1111"
```

### Policy Structure

```json
{
  "Name": "DataProtectionPolicy",
  "Description": "Mask PII in application logs",
  "Version": "2021-06-01",
  "Statement": [
    {
      "Sid": "AuditStatement",
      "DataIdentifier": [
        "arn:aws:dataprotection::aws:data-identifier/CreditCardNumber",
        "arn:aws:dataprotection::aws:data-identifier/EmailAddress",
        "arn:aws:dataprotection::aws:data-identifier/SocialSecurityNumber-US"
      ],
      "Operation": {
        "Audit": {
          "FindingsDestination": {
            "CloudWatchLogs": {
              "LogGroup": "/aws/data-protection/audit"
            },
            "S3": {
              "Bucket": "my-audit-bucket"
            }
          }
        }
      }
    },
    {
      "Sid": "DeidentifyStatement",
      "DataIdentifier": [
        "arn:aws:dataprotection::aws:data-identifier/CreditCardNumber",
        "arn:aws:dataprotection::aws:data-identifier/EmailAddress",
        "arn:aws:dataprotection::aws:data-identifier/SocialSecurityNumber-US"
      ],
      "Operation": {
        "Deidentify": {
          "MaskConfig": {}
        }
      }
    }
  ]
}
```

### Managed Data Identifiers (Know These Exist, Not the Full List)

| Category | Examples |
|---|---|
| **Financial** | Credit card numbers, bank account numbers |
| **Personal** | SSN, passport numbers, driver's license |
| **Contact** | Email addresses, phone numbers, physical addresses |
| **Health** | Health insurance IDs (US) |
| **Credentials** | AWS secret keys, API keys |

> You don't need to memorize all identifiers. Know that AWS provides **managed identifiers** and you reference them by ARN in the policy.

### Unmasking (Exam-Critical)

```
Default: everyone sees masked data (****)

To see UNMASKED data, caller needs BOTH:
  1. logs:GetLogEvents (normal read permission)
  2. logs:Unmask (special permission — grant sparingly)

Without logs:Unmask → you see: "Card: ****-****-****-1111"
With logs:Unmask    → you see: "Card: 4111-1111-1111-1111"
```

**IAM policy to deny unmasking:**
```json
{
  "Sid": "DenyUnmask",
  "Effect": "Deny",
  "Action": "logs:Unmask",
  "Resource": "*"
}
```

### Audit Destinations

| Destination | Use Case |
|---|---|
| **CloudWatch Logs** (another log group) | Real-time alerting on PII detection |
| **S3** | Long-term audit trail |
| **Kinesis Data Firehose** | Stream to SIEM (Splunk, Datadog) |

## SNS Message Data Protection

Same concept, different service:

```
Publisher → SNS Topic (with data protection policy)
                │
                ├── Inbound policy: mask BEFORE storing/delivering
                └── Outbound policy: mask per-subscriber (different subscribers see different masking)
```

### Key Difference from CloudWatch Logs

| Dimension | CloudWatch Logs | SNS |
|---|---|---|
| **When masking happens** | At ingestion (PutLogEvents) | At publish (inbound) or delivery (outbound) |
| **Per-subscriber control** | ❌ Same masking for all readers | ✅ Different masking per subscription |
| **Unmask permission** | `logs:Unmask` | N/A — use outbound policy per subscriber |

## Key Limits/Quotas

| Limit | Value |
|---|---|
| Data identifiers per policy | 30 |
| Log groups with data protection per account per region | 500 |
| Audit destinations per policy | 3 (one of each type) |
| Latency impact | Minimal (milliseconds) |
| Cost | No additional charge for data protection (normal CloudWatch Logs pricing) |
| SNS data protection | Additional charge per message scanned |

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **No code changes** | Policy applied to log group — app doesn't change |
| **Masking is at ingestion** | Once masked, original data is gone from the log event (unless you have `logs:Unmask`) |
| **`logs:Unmask` is the control** | This is how you restrict who sees raw PII — deny this action |
| **Not Macie** | Macie = S3 data discovery. Data protection = real-time masking in logs/messages |
| **Not GuardDuty** | GuardDuty detects threats. Data protection masks PII. Different problems. |
| **Audit ≠ masking** | Audit sends a finding (what was detected). Deidentify masks the data. Use both. |
| **Custom identifiers** | Can create custom data identifiers with regex (like Macie custom identifiers) |
| **Account-level policy** | Can set a default data protection policy for ALL log groups in the account |
| **Org-wide** | Deploy via CloudFormation StackSets or Organizations for consistency |

## Decision Table

| Exam Question Says | Answer | NOT This |
|---|---|---|
| "Mask PII in application logs" | **CloudWatch Logs data protection** | ❌ Macie (S3 only) |
| "Find PII in S3 buckets" | **Macie** | ❌ CloudWatch data protection (logs only) |
| "Mask credit cards before SNS delivery" | **SNS message data protection** | ❌ Lambda transform |
| "Detect sensitive data in CloudWatch Logs" | **CloudWatch Logs data protection (Audit)** | ❌ Macie |
| "Prevent analysts from seeing raw PII in logs" | **Deny `logs:Unmask`** | ❌ Separate log groups |

## K8s Mapping

```
CloudWatch Logs data protection  ≈  Fluentd/Vector filter that redacts PII before shipping
SNS message data protection      ≈  Envoy filter masking sensitive headers per-route
logs:Unmask permission           ≈  RBAC allowing specific users to see unredacted logs
Managed data identifiers         ≈  Pre-built regex library (like detect-secrets)
```

## 🧠 Cheat-Sheet One-Liners

- **"Mask PII in logs" = CloudWatch Logs data protection policy.** No code changes, real-time, managed identifiers.
- **"Find PII in S3" = Macie. "Mask PII in logs" = CloudWatch Logs data protection.** Different services, different targets.
- **`logs:Unmask` is the IAM permission that controls who sees raw PII.** Deny it broadly, grant it to security team only.
- **SNS message data protection = same concept for messages.** Can mask differently per subscriber (outbound policy).
