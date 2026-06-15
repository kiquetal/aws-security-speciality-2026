# KMS Permissions By Service — Quick Reference

> Exam-critical table. If the answer says `kms:Encrypt` for S3/CRR/Kinesis/Secrets Manager → it's WRONG.

## Complete Matrix

| Service | Write/Upload | Read/Download | Special | CreateGrant? |
|---|---|---|---|---|
| **S3 (single put)** | GenerateDataKey | Decrypt | — | ❌ |
| **S3 (multipart)** | GenerateDataKey | Decrypt | Decrypt at reassembly | ❌ |
| **S3 CRR source** | — | Decrypt | — | ❌ |
| **S3 CRR dest** | GenerateDataKey | — | NOT Encrypt | ❌ |
| **EBS (new volume)** | GenerateDataKeyWithoutPlaintext | — | — | ✅ Always |
| **EBS (start existing)** | — | Decrypt | — | ✅ Always |
| **DynamoDB** | GenerateDataKey (via grant) | Decrypt (via grant) | DescribeKey | ✅ Always |
| **Kinesis producer** | GenerateDataKey | — | — | ❌ |
| **Kinesis consumer** | — | Decrypt | DescribeKey | ❌ |
| **Secrets Manager write** | GenerateDataKey | — | — | ❌ |
| **Secrets Manager read** | — | Decrypt | — | ❌ |
| **Lambda env vars** | Encrypt (only exception!) | Decrypt | <4KB direct | ❌ |

## Rules

1. **S3 NEVER uses kms:Encrypt** — always GenerateDataKey (envelope encryption)
2. **CreateGrant = services with backends** — EBS, DynamoDB, RDS, Redshift (delegate to backend)
3. **DescribeKey = Kinesis consumer + DynamoDB** — verify key access before operations
4. **Multipart adds kms:Decrypt** — reassembly decrypts individual parts
5. **kms:Encrypt = only Lambda env vars** — <4KB direct encryption, the ONLY exception

## Why CreateGrant?

```
Services that DELEGATE to a backend (EC2→EBS, DDB→storage engine):
  Your role → kms:CreateGrant → backend receives a Grant
  Backend uses Grant to Decrypt/GenerateDataKey internally

Services where YOUR CALL is evaluated directly (S3, Kinesis, SM):
  Your role → kms:Decrypt/GenerateDataKey → done
  No delegation, no grant needed
```

## CRR Specifics

- Source: `kms:Decrypt` (read encrypted source)
- Destination: `kms:GenerateDataKey` (create fresh DEK, NOT kms:Encrypt)
- Encryption context at destination = **destination bucket ARN** (rewritten, not preserved)
- Key policy on destination CMK must grant replication role explicitly (cross-account)
