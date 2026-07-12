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

---

## Tag Enforcement Patterns (Exam-Critical)

```
THREE tag condition keys — THREE different moments:

aws:RequestTag/Key  = what tag is being SENT in this API call (creation time)
aws:ResourceTag/Key = what tag does the TARGET resource already HAVE (access time)
aws:PrincipalTag/Key = what tag does the CALLER have (ABAC matching)
```

**Force tagging at creation (Null condition):**
```json
{
  "Effect": "Deny",
  "Action": "ec2:RunInstances",
  "Resource": "*",
  "Condition": {
    "Null": {
      "aws:RequestTag/CostCenter": "true"
    }
  }
}
```
= "Deny if CostCenter tag is MISSING from request" = must tag or denied.

**ABAC matching (caller tag = resource tag):**
```json
{
  "Condition": {
    "StringEquals": {
      "aws:ResourceTag/Project": "${aws:PrincipalTag/Project}"
    }
  }
}
```
= "You can only access resources tagged with YOUR project."

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

---

## Condition OPERATORS (HOW to compare)

> Keys = WHAT to check. Operators = HOW to compare.

### String Operators

| Operator | Meaning | Example |
|---|---|---|
| `StringEquals` | Exact match | `"aws:PrincipalOrgID": "o-12345"` |
| `StringNotEquals` | NOT this value | `"s3:x-amz-server-side-encryption": "aws:kms"` (deny if ≠ aws:kms) |
| `StringLike` | Wildcard match (* ?) | `"aws:PrincipalArn": "arn:aws:iam::*:role/Admin*"` |
| `StringNotLike` | Doesn't match wildcard | Exclude specific patterns |

### Numeric Operators

| Operator | Meaning | Example |
|---|---|---|
| `NumericEquals` | = | — |
| `NumericLessThan` | < | `"aws:MultiFactorAuthAge": "10800"` (MFA < 3hrs old) |
| `NumericGreaterThan` | > | — |

### Date Operators (🔴 YOUR WEAK SPOT)

| Operator | Meaning | Example |
|---|---|---|
| `DateGreaterThan` | After this timestamp | — |
| `DateLessThan` | Before this timestamp | `"aws:TokenIssueTime": "2026-07-01T12:00:00Z"` |

**The TokenIssueTime pattern:**
```json
{
  "Effect": "Deny",
  "Action": "*",
  "Resource": "*",
  "Condition": {
    "DateLessThan": {
      "aws:TokenIssueTime": "2026-07-01T12:00:00Z"
    }
  }
}
```
= "Deny any session issued BEFORE this time" = revoke old tokens.

**Memory trick:**
```
DateLessThan = "issued BEFORE" = old tokens = REVOKE
DateGreaterThan = "issued AFTER" = new tokens = (rarely used)
```

### Boolean Operators

| Operator | Meaning | Example |
|---|---|---|
| `Bool` | True/false | `"aws:SecureTransport": "false"` (deny if NOT HTTPS) |
| `Bool` | | `"aws:MultiFactorAuthPresent": "true"` (require MFA) |

### Existence Operators

| Operator | Meaning | Example |
|---|---|---|
| `Null` | Key is absent (true) or present (false) | `"aws:RequestTag/Env": "true"` → deny if tag NOT sent |

**The Tag Enforcement pattern:**
```json
{
  "Effect": "Deny",
  "Action": "ec2:RunInstances",
  "Resource": "*",
  "Condition": {
    "Null": {
      "aws:RequestTag/CostCenter": "true"
    }
  }
}
```
= "Deny if CostCenter tag is MISSING from request" = force tagging.

### IfExists Suffix

```
"StringEqualsIfExists" = 
  → If the key IS present in request: evaluate normally
  → If the key is NOT present: skip this condition (don't deny)
  
Use: "enforce X when applicable, but don't break calls that don't have the key"
Example: PrincipalIsAWSService:false with IfExists
  → Human callers: check org membership
  → AWS services: key absent → condition skipped → allowed
```

---

## Exam Patterns (Operator + Key Combos)

| Scenario | Operator + Key |
|---|---|
| Revoke old sessions | `DateLessThan` + `aws:TokenIssueTime` |
| Require MFA | `Bool` + `aws:MultiFactorAuthPresent: true` |
| MFA max 3 hours | `NumericLessThan` + `aws:MultiFactorAuthAge: 10800` |
| Force HTTPS | `Bool` + `aws:SecureTransport: false` (Deny) |
| Force tag at creation | `Null` + `aws:RequestTag/Key: true` (Deny if absent) |
| Enforce KMS key | `StringNotEquals` + `s3:x-amz-server-side-encryption-aws-kms-key-id` |
| Restrict region | `StringNotEquals` + `aws:RequestedRegion` |
| Exempt AWS services | `BoolIfExists` + `aws:PrincipalIsAWSService: false` |
| Block external sharing (RAM) | `Bool` + `ram:RequestedAllowsExternalPrincipals: true` (Deny) |
