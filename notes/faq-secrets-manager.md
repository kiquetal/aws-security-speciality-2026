# FAQ: AWS Secrets Manager

## Security Use Cases

### Secret Storage & Retrieval
- Store database credentials, API keys, OAuth tokens, SSH keys
- Any text blob up to **64 KB** (JSON document format)
- Programmatic retrieval via API (no hardcoded secrets)
- Replaces plaintext secrets in application code

### Encryption
- **Encryption at rest**: AWS KMS (AES-256 envelope encryption)
- **Customer managed KMS keys**: Optional for full control
- **Encryption in transit**: TLS for all API calls
- **No plaintext caching**: Secrets decrypted in memory, not written to disk

### Access Control
- **IAM policies**: Control who can retrieve/manage secrets
- **Resource-based policies**: Attach policies directly to secrets for cross-account access
- **VPC endpoints**: Private access without internet gateway
- **Condition keys**: `secretsmanager:SecretId`, `secretsmanager:VersionStage`

### Rotation
- **Automatic rotation**: Scheduled rotation for supported databases
- **Managed rotation**: No Lambda function required (AWS handles it)
- **Custom rotation**: Lambda function for unsupported secrets (Oracle on EC2, OAuth tokens)
- **Zero-downtime rotation**: Creates clone user with same privileges, different password
- **Rotation doesn't re-authenticate open connections**

### Monitoring & Auditing
- **CloudTrail integration**: All API calls logged
- **CloudWatch Events**: Notifications on rotation, deletion
- **CloudWatch metrics**: Track secret usage
- **AWS Config rules**: Monitor rotation compliance

## Key Limits/Quotas

### Secret Limits
- **64 KB maximum** secret size
- **500,000 secrets per region** (soft limit, can request increase)
- **20 versions per secret** (soft limit)

### Rotation Limits
- **Rotation frequency**: Minimum 1 hour between rotations
- **Rotation window**: 24 hours to complete rotation
- **Supported databases**: RDS (MySQL, PostgreSQL, Aurora), DocumentDB, Redshift

### API Limits
- **GetSecretValue**: 5,000 requests per second (soft limit)
- **Other APIs**: Lower limits, can request increase
- **Batch operations**: Use caching to reduce API calls

### Pricing
- **$0.40 per secret per month**
- **$0.05 per 10,000 API calls**
- **30-day free trial** for new secrets
- **Rotation**: No additional charge (Lambda execution costs apply)

## Exam Gotchas

### Rotation Behavior
- **Open connections NOT re-authenticated** during rotation
- Applications must handle connection refresh
- Use connection pooling with short TTL
- Test rotation in non-production first

### Secrets Manager vs Parameter Store
- **Secrets Manager**: Automatic rotation, cross-region replication, higher cost
- **Parameter Store**: No automatic rotation, cheaper, integrated with Systems Manager
- **Use Secrets Manager for**: Database credentials, API keys requiring rotation
- **Use Parameter Store for**: Configuration data, non-sensitive parameters

### Deletion Protection
- **Minimum 7-day recovery window** (max 30 days)
- Cannot delete immediately
- Secret marked for deletion, can be restored during window
- After window, secret permanently deleted

### Version Staging
- **AWSCURRENT**: Current version in use
- **AWSPENDING**: New version being created during rotation
- **AWSPREVIOUS**: Previous version (for rollback)
- Applications should always retrieve AWSCURRENT

### Cross-Region Replication
- **Primary secret**: Source of truth
- **Replica secrets**: Read-only copies in other regions
- **Automatic sync**: Changes to primary replicated to replicas
- **Rotation**: Only on primary, replicas updated automatically

### VPC Endpoints
- **Interface endpoint**: Uses PrivateLink (charged)
- **Endpoint policy**: Controls access through endpoint
- **Private DNS**: Enabled by default
- **Security group**: Must allow HTTPS (port 443)

### KMS Integration
- **Default KMS key**: `aws/secretsmanager` (AWS managed)
- **Customer managed key**: Full control, rotation, audit
- **Key policy**: Must allow Secrets Manager to use key
- **Cross-account**: Requires key policy + IAM policy

### Managed Rotation
- **Supported services**: RDS, DocumentDB, Redshift, and third-party SaaS partners
- **No Lambda required**: Secrets Manager handles rotation logic
- **Custom rotation**: Requires Lambda function for unsupported secrets

## Best Practices for IAM Policies

1. **Least privilege**: Grant only GetSecretValue for applications
2. **Separate secrets** for different environments (dev, staging, prod)
3. **Use resource-based policies** for cross-account access
4. **Condition keys**: Restrict by VPC, IP, or tag
5. **Enable rotation** for all database credentials
6. **Use VPC endpoints** for private access
7. **Monitor with CloudTrail**: Track who accessed which secrets
8. **Tag secrets**: For cost allocation and access control
9. **Use versioning**: Don't delete old versions immediately
10. **Cache secrets**: Reduce API calls and costs

### Example: Restrict Secret Access by VPC
```json
{
  "Effect": "Allow",
  "Action": "secretsmanager:GetSecretValue",
  "Resource": "arn:aws:secretsmanager:region:account:secret:MySecret-*",
  "Condition": {
    "StringEquals": {
      "aws:SourceVpc": "vpc-12345678"
    }
  }
}
```

### Example: Prevent Secret Deletion
```json
{
  "Effect": "Deny",
  "Action": "secretsmanager:DeleteSecret",
  "Resource": "arn:aws:secretsmanager:region:account:secret:prod/*"
}
```
