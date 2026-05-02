# Cross-Account S3 + SSE-KMS Access Pattern

> **Blueprint refs:** Task 4.2 (authorization strategies), Task 5.2 (data protection at rest)
> **Diagram:** [../diagrams/cross-account-s3-kms.png](../diagrams/cross-account-s3-kms.png)

## Scenario

Account A (111111111111) owns an S3 bucket encrypted with a customer managed KMS key.
Account B (222222222222) has an IAM role that needs to read objects from that bucket.

**Three policies are required — missing any one = Access Denied.**

## The Three Policies

```
Account A (resource owner)                Account B (caller)
┌─────────────────────────┐              ┌─────────────────────────┐
│                         │              │                         │
│  1. S3 Bucket Policy    │              │  3. IAM Identity Policy │
│     Allow RoleB to      │              │     on RoleB:           │
│     s3:GetObject        │              │     Allow s3:GetObject  │
│                         │◄─────────────│     Allow kms:Decrypt   │
│  2. KMS Key Policy      │  cross-acct  │     (on Account A's     │
│     Allow RoleB to      │   request    │      bucket and key)    │
│     kms:Decrypt         │              │                         │
│                         │              │                         │
└─────────────────────────┘              └─────────────────────────┘
```

## Policy 1 — S3 Bucket Policy (Account A)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAccountBRead",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::222222222222:role/RoleB"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::account-a-bucket/*"
    }
  ]
}
```

## Policy 2 — KMS Key Policy (Account A)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAccountBDecrypt",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::222222222222:role/RoleB"
      },
      "Action": "kms:Decrypt",
      "Resource": "*"
    }
  ]
}
```

> `Resource: "*"` is correct here — in a KMS key policy, `*` means "this key"
> (the policy is already attached to the key, so it's self-referencing).

## Policy 3 — IAM Identity Policy on RoleB (Account B)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCrossAccountS3Read",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::account-a-bucket/*"
    },
    {
      "Sid": "AllowCrossAccountKMSDecrypt",
      "Effect": "Allow",
      "Action": "kms:Decrypt",
      "Resource": "arn:aws:kms:us-east-1:111111111111:key/key-id-abc123"
    }
  ]
}
```

## Why All Three Are Needed

```
SAME-ACCOUNT rule:
  Either identity policy OR resource policy can grant access.
  One Allow is enough.

CROSS-ACCOUNT rule:
  BOTH sides must Allow.
  Account A's resource policies (bucket + key) must Allow Account B.
  Account B's identity policy must Allow the actions on Account A's resources.
```

## Common Mistakes (Exam Gotchas)

| Mistake | Result | Fix |
|---|---|---|
| Missing Policy 3 (identity policy on RoleB) | Access Denied | Add s3:GetObject + kms:Decrypt to RoleB |
| Missing Policy 2 (KMS key policy) | Access Denied (403) | Add kms:Decrypt for RoleB in key policy |
| Using SSE-S3 instead of SSE-KMS | Only policies 1 + 3 needed | No KMS key policy required for SSE-S3 |
| Using AWS managed key (`aws/s3`) | Can't grant cross-account | Must use customer managed key for cross-account |
| RoleB has kms:Decrypt but wrong key ARN | Access Denied | Use Account A's key ARN, not Account B's |

## Exam Scenario Variations

| Variation | What Changes |
|---|---|
| "Account B needs to WRITE objects" | Change `s3:GetObject` → `s3:PutObject` in all 3 policies. Add `kms:GenerateDataKey` to policies 2 + 3 (encryption on write). |
| "Use KMS Grants instead of key policy" | Remove Policy 2. Account A creates a Grant for RoleB with `Decrypt` operation. Policy 3 still needed. |
| "Both accounts in same org" | Resource-based policy alone can grant access (Policy 3 optional). But best practice: keep all three. |
| "Add RCP blocking external access" | RCP must have `aws:PrincipalOrgID` condition. If Account B is in the same org, access works. If not, RCP blocks it. |
