# IAM Overview

## Core Concepts

**IAM (Identity and Access Management)** is the foundation of AWS security. It controls who can access what resources.

## Key Components

### Users, Groups, and Roles
- **IAM Users**: Long-term credentials for individuals
- **IAM Groups**: Collections of users with shared permissions
- **IAM Roles**: Temporary credentials assumed by entities (users, services, federated identities)

### Policies
- **Identity-based policies**: Attached to users, groups, or roles
- **Resource-based policies**: Attached to resources (S3 buckets, KMS keys, Lambda functions)
- **Permission boundaries**: Set maximum permissions for an entity
- **Service Control Policies (SCPs)**: Organization-level guardrails

## Integration with Other Services

IAM integrates deeply with:
- **AWS Organizations**: Centralized management across accounts
- **IAM Identity Center** (formerly SSO): Federated access for workforce identities
- **Amazon Cognito**: User authentication for applications
- **AWS KMS**: Key policies work alongside IAM policies
- **Amazon S3**: Bucket policies combined with IAM policies
- **AWS Secrets Manager**: Access control for secrets
- **Amazon GuardDuty**: Detects compromised IAM credentials

## Security Best Practices

1. **Enable MFA** for all human users
2. **Use roles** instead of long-term credentials
3. **Apply least privilege** with permission boundaries
4. **Rotate credentials** regularly
5. **Use IAM Access Analyzer** to identify overly permissive policies
6. **Monitor with CloudTrail** for all IAM API calls

## Cross-Account Access

Use IAM roles with trust policies to enable secure cross-account access without sharing credentials.
