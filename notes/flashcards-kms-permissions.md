# KMS Permissions Per Service

> Which KMS actions does each service need? The exam tests EXACT permission names.

---

## The Pattern

| Operation | KMS Action | Who Calls It |
|---|---|---|
| **Upload/Write/Encrypt** | `kms:GenerateDataKey` | Producer (S3 PutObject, Kinesis PutRecord, CRR dest) |
| **Download/Read/Decrypt** | `kms:Decrypt` | Consumer (S3 GetObject, Kinesis GetRecords, CRR source) |
| **Delegate to backend** | `kms:CreateGrant` | Services that delegate internally (EBS, DynamoDB, RDS) |
| **Verify key metadata** | `kms:DescribeKey` | Kinesis consumer, DynamoDB, some cross-account patterns |
| **Multipart reassembly** | `kms:Decrypt` | S3 CompleteMultipartUpload (reassembles encrypted parts) |

---

## Per-Service Matrix

| Service + Operation | Permissions Needed | Trap |
|---|---|---|
| **S3 PutObject (single)** | `kms:GenerateDataKey` | NOT kms:Encrypt — S3 never uses Encrypt |
| **S3 GetObject** | `kms:Decrypt` | Server-side, but caller still needs it |
| **S3 Multipart Upload** | `kms:GenerateDataKey` + `kms:Decrypt` | Decrypt needed for reassembly at Complete step |
| **EC2 Start (existing EBS)** | `kms:CreateGrant` + `kms:Decrypt` | Always needs CreateGrant |
| **EC2 Create (new EBS)** | `kms:CreateGrant` + `kms:GenerateDataKeyWithoutPlaintext` | Always needs CreateGrant |
| **DynamoDB PutItem (CMK)** | `kms:CreateGrant` + `kms:DescribeKey` | Delegates via grants like EBS |
| **DynamoDB GetItem (CMK)** | `kms:CreateGrant` + `kms:DescribeKey` | Same — both read and write need grants |
| **Kinesis Producer** | `kms:GenerateDataKey` | Same as S3 upload |
| **Kinesis Consumer** | `kms:Decrypt` + `kms:DescribeKey` | NOT CreateGrant — Kinesis doesn't delegate |
| **CRR Source** | `kms:Decrypt` | Decrypt source key to read |
| **CRR Destination** | `kms:GenerateDataKey` | NOT kms:Encrypt — same as any S3 upload |
| **CRR Replication Role** | Decrypt(src) + GenerateDataKey(dest) + GetObjectVersionForReplication | Mnemonic: D-G-F |
| **CloudFront OAC + SSE-KMS** | `kms:Decrypt` on CF service principal | Key policy must grant `cloudfront.amazonaws.com` |
| **FSx Lustre + SSE-KMS S3** | Encrypt + Decrypt + GenerateDataKey + DescribeKey | Key policy must grant `fsx.amazonaws.com` |

---

## Rules to Memorize

1. **S3 NEVER uses `kms:Encrypt`** — always GenerateDataKey (envelope encryption)
2. **`kms:CreateGrant` = services that delegate to backends** — EBS, DynamoDB, RDS, Redshift
3. **Kinesis does NOT use CreateGrant** — it uses Decrypt + DescribeKey directly
4. **CRR dest = GenerateDataKey (not Encrypt)** — same envelope rule as any S3 write
5. **Multipart = GenerateDataKey + Decrypt** — the Decrypt is for reassembly at CompleteMultipartUpload
6. **DescribeKey appears with**: Kinesis consumer, DynamoDB, cross-account verification

---

## Quick Decision

```
"Upload/write/produce" → GenerateDataKey
"Download/read/consume" → Decrypt
"EBS or DynamoDB" → add CreateGrant + DescribeKey
"Kinesis consume" → Decrypt + DescribeKey (no CreateGrant)
"CRR" → Decrypt source + GenerateDataKey dest
"S3 anything" → NEVER kms:Encrypt
```
