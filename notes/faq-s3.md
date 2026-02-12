# FAQ: Amazon S3 (Simple Storage Service)

## Security Use Cases

### Access Control
- **Bucket policies**: Resource-based policies for cross-account access
- **IAM policies**: Identity-based access control
- **Access Control Lists (ACLs)**: Legacy, use bucket policies instead
- **S3 Block Public Access**: Account and bucket-level protection against public exposure
- **Pre-signed URLs**: Temporary access to objects without AWS credentials

### Encryption
- **Server-Side Encryption (SSE)**:
  - **SSE-S3**: AWS managed keys (AES-256)
  - **SSE-KMS**: Customer managed keys in KMS (audit trail, rotation)
  - **SSE-C**: Customer-provided keys (you manage keys)
- **Client-Side Encryption**: Encrypt before upload using AWS Encryption SDK
- **Encryption in transit**: TLS/HTTPS for all API calls
- **Default encryption**: Can be enforced at bucket level

### Logging & Monitoring
- **S3 Server Access Logs**: Detailed records of requests
- **CloudTrail S3 data events**: API-level logging (GetObject, PutObject, DeleteObject)
- **S3 Object Lock**: WORM (Write Once Read Many) for compliance
- **S3 Versioning**: Protect against accidental deletion
- **S3 Inventory**: Audit and report on replication and encryption status

### GuardDuty S3 Protection
- Monitors CloudTrail S3 data events for threats
- Detects: credential misuse, unusual API activity, access from malicious IPs
- No need to enable S3 data event logging in CloudTrail
- Automatically monitors all buckets

## Key Limits/Quotas

### Bucket Limits
- **100 buckets per account** (soft limit, can request increase)
- Bucket names must be globally unique
- Bucket names must be DNS-compliant

### Object Limits
- **5 TB maximum object size**
- **5 GB maximum** for single PUT operation
- Use multipart upload for objects > 100 MB
- **10,000 parts maximum** per multipart upload

### Request Limits
- **3,500 PUT/COPY/POST/DELETE requests per second per prefix**
- **5,500 GET/HEAD requests per second per prefix**
- No limit on number of prefixes

### Storage Classes
- S3 Standard, S3 Intelligent-Tiering, S3 Standard-IA, S3 One Zone-IA
- S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive
- Minimum storage duration charges apply to IA and Glacier classes

## Exam Gotchas

### Bucket Policy vs IAM Policy
- **Bucket policy**: Attached to bucket, can grant cross-account access
- **IAM policy**: Attached to principal, cannot grant cross-account access alone
- **Effective permissions**: Intersection of bucket policy + IAM policy + SCPs
- **Explicit Deny always wins**

### S3 Block Public Access
- **Four settings**: Block public ACLs, Ignore public ACLs, Block public bucket policies, Restrict public buckets
- **Account-level**: Applies to all buckets in account
- **Bucket-level**: Applies to specific bucket
- **Overrides bucket policies and ACLs** - cannot be bypassed

### Encryption Enforcement
- **Bucket policy condition**: `s3:x-amz-server-side-encryption`
- **Deny unencrypted uploads**: Use condition to require SSE
- **KMS key requirement**: `s3:x-amz-server-side-encryption-aws-kms-key-id`
- **Default encryption**: Doesn't prevent unencrypted uploads (use bucket policy)

### S3 Object Lock
- **Governance mode**: Can be overridden with special permissions
- **Compliance mode**: Cannot be overridden, even by root
- **Legal hold**: Independent of retention period
- **Requires versioning** to be enabled

### VPC Endpoints
- **Gateway endpoint**: Free, for S3 and DynamoDB
- **Interface endpoint**: Charged, uses PrivateLink
- **Endpoint policy**: Controls access through endpoint
- **Doesn't replace bucket policy** - both are evaluated

### Cross-Region Replication (CRR)
- **Requires versioning** on source and destination
- **IAM role** for S3 to assume
- **Doesn't replicate**: Existing objects (unless S3 Batch Replication), delete markers (optional), objects encrypted with SSE-C
- **Replication Time Control (RTC)**: 15-minute SLA

### S3 Access Points
- **Unique hostname** per access point
- **Dedicated access policy** per access point
- **VPC-restricted**: Can restrict to specific VPC
- **Simplifies bucket policy management** for shared buckets

### Presigned URLs
- **Inherit permissions** of IAM principal that created them
- **Expiration time**: Set by creator (max 7 days for SigV4)
- **Cannot be revoked** - rotate IAM credentials to invalidate
- **Use SigV4**: SigV2 is deprecated

## Best Practices for Bucket Policies

1. **Enable S3 Block Public Access** by default
2. **Use bucket policies for cross-account access**, not ACLs
3. **Require encryption in transit**: `aws:SecureTransport` condition
4. **Require encryption at rest**: `s3:x-amz-server-side-encryption` condition
5. **Restrict by VPC/VPC endpoint**: `aws:SourceVpc`, `aws:SourceVpce`
6. **Restrict by IP**: `aws:SourceIp` condition (use with caution)
7. **Use MFA Delete** for versioned buckets with sensitive data
8. **Least privilege**: Grant minimum permissions needed
9. **Condition keys**: `s3:prefix`, `s3:delimiter`, `s3:max-keys` for ListBucket
10. **Prevent confused deputy**: `aws:SourceAccount`, `aws:SourceArn`

### Example: Enforce SSE-KMS with Specific Key
```json
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:PutObject",
  "Resource": "arn:aws:s3:::mybucket/*",
  "Condition": {
    "StringNotEquals": {
      "s3:x-amz-server-side-encryption": "aws:kms",
      "s3:x-amz-server-side-encryption-aws-kms-key-id": "arn:aws:kms:region:account:key/key-id"
    }
  }
}
```
