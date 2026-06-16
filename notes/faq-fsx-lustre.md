# FAQ: Amazon FSx for Lustre Security (Task 5.2)

> **Blueprint refs:** Task 5.2 (data at rest controls), Task 5.1 (data in transit)
> **In-scope:** Storage and Data Management section
> **Risk:** 0-1 questions (encryption + KMS key policy pattern).

---

## Key Security Facts

| Dimension | Detail |
|---|---|
| **Encryption at rest** | ALWAYS encrypted (can't opt out). XTS-AES-256 block cipher. |
| **KMS key type** | Symmetric only (no asymmetric) |
| **Key options** | AWS managed key (default) OR customer CMK |
| **Encryption in transit** | Automatic TLS between clients and file system |
| **Network** | VPC-only. Security groups control access. No public internet. |
| **Backup** | Stored in S3 (11 9's durability). Encrypted with same key as FS. |

---

## File System Types

| Type | Durability | Backups | Use Case |
|---|---|---|---|
| **Scratch** | No replication. Data lost if server fails. | ❌ No | Temporary compute (short jobs) |
| **Persistent** | Replicated within AZ. | ✅ Yes | Long-running workloads, ML training |

---

## S3 Integration (Exam Trap)

```
FSx for Lustre can link to an S3 bucket as data repository.

If S3 bucket uses SSE-KMS:
  → FSx needs permissions on that KMS key
  → Key policy must grant fsx.amazonaws.com:
    - kms:Encrypt
    - kms:Decrypt
    - kms:GenerateDataKey
    - kms:DescribeKey

Same pattern as: CloudFront OAC + KMS, DynamoDB + CMK, EBS + CMK
```

---

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Always encrypted** | Unlike EBS, you can't create unencrypted FSx Lustre |
| **Symmetric KMS only** | No asymmetric, no HMAC |
| **Scratch = no backup** | Data NOT durable. Server failure = data gone. |
| **S3 linked + SSE-KMS** | Key policy must grant `fsx.amazonaws.com` |
| **VPC only** | No public access. No VPC endpoint needed (direct ENI in subnet). |

---

## 🧠 Cheat-Sheet One-Liners

- **FSx for Lustre = ALWAYS encrypted (XTS-AES-256), symmetric KMS only, VPC-only.**
- **FSx linked to SSE-KMS S3 bucket: key policy must grant `fsx.amazonaws.com`.**
- **Scratch = no backups/replication (temp). Persistent = backups + within-AZ replication.**
