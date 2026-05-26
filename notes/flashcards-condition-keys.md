# Condition Keys — Flashcard Reference

> Memorize: key name → when to use (one line each)

---

## Identity Keys (WHO is calling?)

| Key | When to Use |
|---|---|
| `aws:PrincipalOrgID` | Restrict to callers in MY org |
| `aws:PrincipalAccount` | Restrict to callers from a SPECIFIC account |
| `aws:PrincipalIsAWSService` | Exempt AWS services (CloudTrail, Config) from org-deny rules |
| `aws:PrincipalServiceName` | Identify WHICH AWS service is calling |
| `aws:PrincipalTag/Key` | ABAC — match caller's tag (from IdP session or IAM) |

## Source Keys (WHO triggered the service?)

| Key | When to Use |
|---|---|
| `aws:SourceAccount` | Confused deputy — which ACCOUNT triggered this service call |
| `aws:SourceArn` | Confused deputy — which specific RESOURCE triggered it |
| `aws:SourceOrgID` | Restrict service-to-service calls to my org |
| `aws:SourceVpc` | Restrict access to callers from a specific VPC |
| `aws:SourceVpce` | Restrict access to callers from a specific VPC endpoint |
| `aws:SourceIp` | Restrict by IP (use with caution — breaks services) |

## Request Keys (WHAT is being sent?)

| Key | When to Use |
|---|---|
| `aws:RequestTag/Key` | Enforce tag at CREATION time ("must tag when creating") |
| `aws:ResourceTag/Key` | Control access based on EXISTING resource tags |
| `aws:TagKeys` | Restrict which tag keys can be used |
| `aws:RequestedRegion` | Restrict API calls to specific regions |

## STS / Session Keys

| Key | When to Use |
|---|---|
| `sts:ExternalId` | Third-party cross-account roles (confused deputy) |
| `sts:SourceIdentity` | Track original human through role chains |
| `sts:RoleSessionName` | Enforce naming convention for sessions |
| `aws:TokenIssueTime` | Revoke sessions issued before a timestamp |
| `aws:MultiFactorAuthPresent` | Require MFA |
| `aws:MultiFactorAuthAge` | Require RECENT MFA (max seconds since auth) |

## KMS Keys

| Key | When to Use |
|---|---|
| `kms:ViaService` | Only allow KMS calls that come THROUGH a specific service (e.g., s3) |
| `kms:EncryptionContext` | Require specific context for encrypt/decrypt |
| `kms:CallerAccount` | Restrict key usage to specific account |
| `kms:GrantIsForAWSResource` | Only allow grants created by AWS services |

## S3 Keys

| Key | When to Use |
|---|---|
| `s3:x-amz-server-side-encryption` | Enforce encryption type on upload |
| `s3:x-amz-server-side-encryption-aws-kms-key-id` | Enforce SPECIFIC KMS key |
| `s3:prefix` | Restrict ListBucket to specific prefix (bucket-level ONLY) |

## RAM Keys

| Key | When to Use |
|---|---|
| `ram:RequestedAllowsExternalPrincipals` | Block sharing resources outside org |

## EC2 Keys

| Key | When to Use |
|---|---|
| `ec2:MetadataHttpTokens` | Enforce IMDSv2 (require "required") |
| `ec2:ResourceTag/Key` | Control access to EC2 by tag |

---

## Quick Rules

- **"Source"** = indirect (service acting on behalf of someone)
- **"Principal"** = direct (the actual caller)
- **"Request"** = what's being CREATED now
- **"Resource"** = what ALREADY EXISTS
- **`IfExists`** suffix = don't deny if key is absent from request context
