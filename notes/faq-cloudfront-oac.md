# FAQ: CloudFront Origin Access Control (OAC)

> **Blueprint refs:** Task 3.1 (edge security), Task 5.2 (data protection at rest — S3 encryption)

## The Problem OAC Solves

Without OAC, you must make your S3 bucket public for CloudFront to serve content.
A public bucket means users can bypass CloudFront and access S3 directly — skipping
your WAF rules, geo-restrictions, caching, and access logging.

```
WITHOUT OAC (bucket is public):

  User ──► CloudFront ──► S3 Bucket (public)    ✅ works
  User ──────────────────► S3 Bucket (public)    ✅ also works (bypass!)
                           ↑
                           WAF, geo-blocks, logging all skipped


WITH OAC (bucket is private):

  User ──► CloudFront ──(OAC signs request)──► S3 Bucket (private)  ✅ works
  User ──────────────────────────────────────► S3 Bucket (private)  ❌ denied
                                                ↑
                                                Only CloudFront can access it
```

## How OAC Works

1. S3 bucket: **Block Public Access = ON** (fully private)
2. CloudFront distribution: OAC configured as origin access
3. S3 bucket policy: Only allows the CloudFront **service principal**
4. CloudFront signs every request to S3 using **SigV4**
5. S3 verifies the signature → only CloudFront gets in

## The Bucket Policy (Not Public — Scoped to One Distribution)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontOACOnly",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudfront.amazonaws.com"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::mybucket/*",
      "Condition": {
        "StringEquals": {
          "AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE"
        }
      }
    }
  ]
}
```

**Key points:**
- `Principal: {"Service": "cloudfront.amazonaws.com"}` — only CloudFront service
- `AWS:SourceArn` condition — only THIS specific distribution (confused deputy prevention)
- Bucket stays fully private — Block Public Access remains ON

## OAC vs OAI (Exam-Critical)

| Dimension | OAI (legacy) | OAC (current) |
|---|---|---|
| **Status** | ⚠️ Deprecated | ✅ Recommended |
| **Signing** | Custom CloudFront signing | SigV4 (standard AWS) |
| **SSE-KMS support** | ❌ No | ✅ Yes |
| **S3 regions** | All | All (including new opt-in regions) |
| **HTTP methods** | GET only | GET, PUT, POST, DELETE |
| **Confused deputy prevention** | ❌ No SourceArn condition | ✅ SourceArn condition |
| **Principal type** | Special CloudFront identity | CloudFront service principal |
| **Bucket policy** | References OAI ID | References service + SourceArn |

> **Exam rule:** If OAI and OAC are both options → **OAC is always the better answer**.

## OAC + SSE-KMS (Task 5.2)

OAI cannot work with SSE-KMS encrypted S3 objects. OAC can.

For OAC + SSE-KMS, the KMS key policy must allow CloudFront:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontDecrypt",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudfront.amazonaws.com"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE"
        }
      }
    }
  ]
}
```

**Two policies needed for OAC + SSE-KMS:**
1. S3 bucket policy → allows CloudFront `s3:GetObject`
2. KMS key policy → allows CloudFront `kms:Decrypt`

## Exam Gotchas

### OAC vs OAI
- **"S3 origin with KMS encryption"** → OAC (OAI can't do KMS)
- **"Upload to S3 via CloudFront"** → OAC (OAI is GET only)
- **"Restrict S3 to CloudFront only"** → OAC (both work, but OAC is recommended)
- **"Prevent confused deputy"** → OAC (SourceArn condition)

### Bucket Policy Is Still Needed
- OAC doesn't eliminate the bucket policy — it changes what the policy says
- Without OAC: bucket policy grants public access (`Principal: "*"`)
- With OAC: bucket policy grants CloudFront service principal only
- The bucket policy is now a **security control**, not a public access grant

### Block Public Access Stays ON
- OAC works WITH Block Public Access enabled
- The bucket policy allowing CloudFront service principal is NOT considered "public"
- AWS treats service principal access differently from `Principal: "*"`

### CloudFront + S3: Common Misconfigurations
1. **Missing SourceArn condition** → any CloudFront distribution can access your bucket
2. **Using OAI with SSE-KMS** → 403 errors (OAI can't decrypt KMS)
3. **S3 website endpoint as origin** → OAC doesn't work (use REST endpoint)
4. **Missing KMS key policy** → 403 errors even with correct bucket policy

### K8s Mapping
- **OAC ≈ Istio AuthorizationPolicy** — only the ingress gateway (CloudFront) can reach the backend (S3)
- **Bucket policy ≈ NetworkPolicy** — pod only accepts traffic from the gateway
- **Block Public Access ≈ default-deny ingress** — nothing gets in unless explicitly allowed
