# S3 Server Access Logging — Permissions Deep Dive

> Source: AWS official docs (docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html)
> Failed: Q864, Q868, Q903, Q1595. Lock this.

---

## How S3 Access Logging Works

```
Source bucket → "deliver logs to target bucket"
                     │
                     ▼
           logging.s3.amazonaws.com (S3 log delivery service)
                     │
                     ▼
           Target bucket (same region, same account)
```

The S3 logging service (`logging.s3.amazonaws.com`) is the principal that WRITES log files to your target bucket.

---

## Two Ways to Grant Permission (Exam-Critical)

### Option 1: Bucket Policy (RECOMMENDED — modern)

```json
{
  "Sid": "S3ServerAccessLogsPolicy",
  "Effect": "Allow",
  "Principal": {
    "Service": "logging.s3.amazonaws.com"
  },
  "Action": "s3:PutObject",
  "Resource": "arn:aws:s3:::target-bucket/prefix*",
  "Condition": {
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::source-bucket"
    },
    "StringEquals": {
      "aws:SourceAccount": "123456789012"
    }
  }
}
```

- ✅ Works with BucketOwnerEnforced (ACLs disabled)
- ✅ Includes confused deputy prevention (SourceArn + SourceAccount)
- ✅ AWS recommended approach

### Option 2: Bucket ACL (LEGACY — old way)

```
Grant to: http://acs.amazonaws.com/groups/s3/LogDelivery
Permissions: WRITE + READ_ACP
```

- ❌ Does NOT work with BucketOwnerEnforced (ACLs disabled = can't grant)
- ❌ No confused deputy prevention
- ❌ AWS no longer recommends this

---

## The BucketOwnerEnforced Trap

```
S3 Object Ownership settings (3 options):

1. BucketOwnerEnforced (DEFAULT since Apr 2023)
   → ACLs DISABLED. All objects owned by bucket owner.
   → S3 access logging via ACL method = BROKEN
   → Must use bucket policy method for logging

2. BucketOwnerPreferred
   → ACLs ENABLED. Objects uploaded with bucket-owner-full-control ACL = owned by bucket owner.
   → S3 access logging via ACL method = WORKS ✅

3. ObjectWriter
   → ACLs ENABLED. Object owned by uploading account.
   → S3 access logging via ACL method = WORKS ✅

Summary:
  BucketOwnerEnforced = ACLs disabled → bucket policy ONLY for logging
  BucketOwnerPreferred or ObjectWriter = ACLs enabled → both methods work
  New buckets since April 2023 = BucketOwnerEnforced BY DEFAULT
```

---

## Constraints (Exam Scenarios)

| Constraint | Detail |
|---|---|
| **Same region** | Source and target must be in same AWS Region |
| **Same account** | Source and target must be in same AWS account |
| **SSE-KMS on target** | ❌ NOT supported. Target must use SSE-S3 (or no encryption). S3 logging service can't use KMS. |
| **Requester Pays on target** | ❌ NOT supported. Must be disabled. |
| **Object Lock on target** | ❌ NOT supported. Can't use as logging target. |

---

## Config Remediation for Logging

When Config auto-remediates "enable S3 logging":

```
Remediation role needs:
  s3:PutBucketLogging     ← enable logging on source
  s3:GetBucketAcl         ← verify ACL state / ownership on target
  
  WHY GetBucketAcl? → S3 service checks bucket ownership
  before accepting it as a logging target (legacy verification step).
  Even with bucket policy method, this check still occurs.
```

---

## Exam Scenarios

| Scenario | Answer |
|---|---|
| "Logging enabled, zero logs, BucketOwnerEnforced, using ACLs" | Switch to bucket policy for `logging.s3.amazonaws.com` |
| "Logging enabled, zero logs, bucket policy correct" | Check: SSE-KMS on target? (must be SSE-S3) |
| "Config remediation for logging fails AccessDenied" | Missing `s3:GetBucketAcl` on remediation role |
| "S3 access logging target permissions" | Bucket policy (recommended) OR ACL grant (legacy) |
| "New bucket, enable logging" | Bucket policy only (new buckets = BucketOwnerEnforced default) |

---

## vs Other "Old Four" Services

| Service | How it delivers to S3 | GetBucketAcl needed? |
|---|---|---|
| **S3 server access logging** | `logging.s3.amazonaws.com` bucket policy OR ACL | ✅ (ownership check) |
| **CloudTrail** | `cloudtrail.amazonaws.com` bucket policy | ✅ (ownership check) |
| **Config** | `config.amazonaws.com` bucket policy | ✅ (ownership check) |
| **ELB** | ELB account ID in bucket policy | ❌ (uses account ID, not ACL) |

---

## 🧠 Exam One-Liners

- **S3 access logging = `logging.s3.amazonaws.com` service principal.** Recommended: bucket policy. Legacy: ACL.
- **BucketOwnerEnforced breaks ACL method only.** Bucket policy method works fine with ACLs disabled.
- **Target bucket constraints:** same region + same account + NO SSE-KMS + NO Requester Pays + NO Object Lock.
- **Config remediation for logging needs `s3:GetBucketAcl`** — legacy ownership verification step.
- **New buckets (since April 2023) = BucketOwnerEnforced default** → must use bucket policy method.
