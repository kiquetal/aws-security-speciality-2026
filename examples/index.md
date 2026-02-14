# Examples Index

This directory contains practical, production-ready examples for AWS Security Specialty exam preparation.

## Available Examples

### IAM Policies
  - [IAM Policy Examples](./iam-policy-examples.md) - Comprehensive examples of all IAM policy types
  - [Identity-based policies](./iam-policy-examples.md#1-identity-based-policies) - S3 read-only, EC2 management with MFA
  - [Resource-based policies](./iam-policy-examples.md#2-resource-based-policies) - S3 bucket policies, KMS key policies, Lambda resource policies
  - [Permission boundaries](./iam-policy-examples.md#3-permission-boundaries) - Developer limits, third-party contractor restrictions
  - [Service Control Policies (SCPs)](./iam-policy-examples.md#4-service-control-policies-scps) - Root user denial, encryption enforcement, security service protection
  - [Trust policies](./iam-policy-examples.md#5-trust-policies-assumerole-policies) - Cross-account access, service roles, OIDC/SAML federation
  - [Resource Control Policies (RCPs)](./iam-policy-examples.md#6-resource-control-policies-rcps) - Prevent external resource sharing
  - [Policy evaluation logic](./iam-policy-examples.md#policy-evaluation-logic) - How AWS evaluates multiple policies
  - [Best practices summary](./iam-policy-examples.md#best-practices-summary) - Key principles for secure policies
  - [Testing your policies](./iam-policy-examples.md#testing-your-policies) - IAM Policy Simulator commands
  - [Common exam scenarios](./iam-policy-examples.md#common-exam-scenarios) - Frequently tested patterns

## How to Use These Examples

1. **Study the structure**: Each example includes comments explaining the security rationale
2. **Test locally**: Use AWS IAM Policy Simulator or the provided CLI commands
3. **Modify for your needs**: All examples follow least privilege and can be adapted
4. **Practice active recall**: Try writing policies from memory, then compare

## Best Practices Reminder

- Always use specific ARNs instead of wildcards
- Add conditions to limit scope (IP, MFA, encryption)
- Use explicit denies for critical protections
- Test with IAM Access Analyzer before deployment
- Remember: "Deny always wins" in policy evaluation

---

*All examples align with AWS Well-Architected Framework Security Pillar and SCS-C03 exam domains.*
