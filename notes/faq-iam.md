# FAQ: AWS IAM (Identity and Access Management)

## Security Use Cases

### Authentication & Authorization
- IAM provides authentication and authorization for AWS services
- Access is **denied by default** - only explicitly granted permissions are allowed
- Use IAM roles for temporary credentials (security best practice)
- Avoid IAM users with long-term credentials; prefer federated access via identity providers

### Least Privilege Implementation
- Grant only permissions required to perform a task
- Start with AWS managed policies, then refine with customer managed policies
- Use IAM Access Analyzer to identify overly permissive policies
- Apply permission boundaries to set maximum permissions for entities

### Policy Types
- **Identity-based policies**: Attached to users, groups, or roles
- **Resource-based policies**: Attached to resources (S3, KMS, Lambda) for cross-account access
- **Service Control Policies (SCPs)**: Organization-level guardrails (don't grant permissions, only restrict)
- **Permission boundaries**: Define maximum permissions an entity can have

### Access Control Models
- **RBAC (Role-Based)**: Assign permissions based on job functions
- **ABAC (Attribute-Based)**: Use tags on resources, roles, and sessions for fine-grained control
  - Scales better in growing environments
  - Automatically grants access to new resources with matching tags

### Credential Management
- Rotate credentials regularly using IAM access last used information
- Use temporary delegation for AWS Partners to request limited-time access
- Review password and access key last used information to identify unused credentials

## Key Limits/Quotas

- **No explicit limits mentioned in FAQ** - IAM is designed to scale
- Use IAM Access Analyzer to continuously monitor and audit access
- All IAM activity logged in CloudTrail for compliance

## Exam Gotchas

### Policy Evaluation Logic
- **Explicit Deny always wins** over Allow statements
- SCPs affect all IAM users, roles, AND the root user of member accounts
- SCPs don't grant permissions - they set boundaries on what can be allowed

### IAM vs Organizations
- IAM policies grant access to specific principals
- SCPs restrict maximum available permissions across accounts
- Both are evaluated together: Effective permission = IAM policy ∩ SCP

### Common Mistakes
- **Don't use long-term IAM user credentials** - use roles with temporary credentials
- IAM Access Analyzer findings show: external access, internal access, and unused access
- Custom policy checks (paid feature) validate policies against security standards before deployment

### Testing & Validation
- Use IAM policy simulator to test policies (includes SCP effects)
- IAM Access Analyzer uses automated reasoning (provable security) for policy validation
- 100+ policy checks available to guide secure policy authoring

### Monitoring & Auditing
- CloudTrail logs all IAM API calls
- IAM Access Analyzer provides centralized dashboard for access findings
- Last accessed information helps identify unused permissions for refinement

## Best Practices for JSON Policies

1. **Always start with explicit Deny for sensitive actions**
2. **Use Condition blocks** for context-based access (IP, MFA, time, tags)
3. **Leverage `aws:PrincipalOrgID`** for cross-account access within your organization
4. **Use `aws:SourceAccount` and `aws:SourceArn`** to prevent confused deputy
5. **Tag-based conditions** (`aws:RequestTag`, `aws:ResourceTag`) for ABAC
6. **Never use** `"Principal": "*"` or `"Action": "*"` in production
