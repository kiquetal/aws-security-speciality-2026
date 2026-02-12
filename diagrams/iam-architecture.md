# AWS IAM Architecture

## Overview
This diagram illustrates the complete IAM architecture showing identity components, authorization policies, and their relationships with AWS resources.

## Key Components

### Identity Components (Blue Zone)
- **IAM User**: Long-term credentials (access keys). Avoid for production workloads.
- **IAM Group**: Collection of users for easier permission management.
- **IAM Role**: Temporary credentials via STS AssumeRole. Preferred for security.
- **Federated Identity**: External identity providers (SAML/OIDC) for SSO.
- **Service Principal**: AWS services that need to act on your behalf.

### Authorization Policies (Red Zone)
- **Identity-based Policy**: Attached to users, groups, or roles. Defines what the identity can do.
- **Resource-based Policy**: Attached to resources (S3, Lambda, etc.). Defines who can access the resource.
- **Permissions Boundary**: Maximum permissions an identity can have (acts as a filter).
- **SCP (Service Control Policy)**: Organization-level guardrails. Cannot grant permissions, only restrict.
- **Session Policy**: Additional restrictions when assuming a role.

### AWS Resources (Cyan Zone)
Examples: S3 buckets, Lambda functions, EC2 instances that policies grant access to.

## Policy Evaluation Logic
IAM uses a **deny-by-default** model:

1. **Explicit DENY** wins (SCP, Permissions Boundary)
2. **Explicit ALLOW** required (Identity-based + Resource-based)
3. **Implicit DENY** if no allow exists

## Best Practices for SCS-C03 Exam

### Least Privilege
- Start with deny-all, grant minimum required permissions
- Use Permissions Boundaries to delegate safely
- Prefer managed policies for common patterns, inline for exceptions

### Prefer Roles over Users
- Roles provide temporary credentials (auto-rotate)
- No long-term access keys to manage or leak
- Use IAM Identity Center for human access
- Use instance profiles for EC2, execution roles for Lambda

### Policy Structure (JSON Best Practices)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DescriptiveStatementId",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-bucket/*",
      "Condition": {
        "StringEquals": {
          "s3:x-amz-server-side-encryption": "AES256"
        }
      }
    }
  ]
}
```

### Key JSON Elements
- **Version**: Always use "2012-10-17"
- **Sid**: Human-readable statement identifier
- **Effect**: "Allow" or "Deny"
- **Principal**: Who (only in resource-based policies)
- **Action**: What operations (use wildcards carefully)
- **Resource**: Which resources (be specific with ARNs)
- **Condition**: When/how (encryption, IP, MFA, tags)

### Common Exam Scenarios

**Q: User can't access S3 despite having permissions?**
- Check: SCP restrictions, Permissions Boundary, bucket policy, encryption requirements

**Q: Cross-account access not working?**
- Need BOTH: Trust policy in target account + permissions in source account

**Q: How to delegate admin tasks safely?**
- Use Permissions Boundary to limit maximum permissions
- Delegate role creation with boundary enforcement

**Q: Federated access setup?**
- SAML: Enterprise IdP (Active Directory)
- OIDC: Web identity (Google, Facebook) or custom IdP
- Both use AssumeRoleWithSAML or AssumeRoleWithWebIdentity

## Encryption & Logging Considerations

### IAM and Encryption
- IAM doesn't encrypt data directly
- Use IAM policies to enforce encryption requirements via Conditions
- Example: Deny S3 uploads without SSE-S3 or SSE-KMS

### IAM Logging
- **CloudTrail**: Logs all IAM API calls (who did what, when)
- **IAM Access Analyzer**: Identifies resources shared with external entities
- **IAM Credential Reports**: Lists all users and credential status
- **Access Advisor**: Shows service permissions last used

## Quotas (Important for Exam)
- **Users per account**: 5,000 (soft limit)
- **Groups per account**: 300
- **Roles per account**: 1,000
- **Managed policies per user/group/role**: 10
- **Inline policy size**: 2,048 characters (users), 10,240 (roles/groups)
- **Managed policy size**: 6,144 characters
- **Policy versions**: 5 per managed policy

## Related Services
- **IAM Identity Center** (successor to AWS SSO): Centralized access management
- **AWS Organizations**: Multi-account governance with SCPs
- **Cognito**: User pools for application authentication
- **Verified Permissions**: Fine-grained authorization using Cedar policy language
