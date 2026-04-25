# Examples Index

Practical, production-ready examples organized by SCS-C03 exam domain.

---

## Domain 1: Detection (16%)

> Monitoring, alerting, logging solutions

- _No examples yet_ — GuardDuty EventBridge rules, Config custom rules, Security Hub automations

## Domain 2: Incident Response (14%)

> Response plans, forensics, remediation

- _No examples yet_ — EC2 isolation Lambda, forensic snapshot automation, Step Functions runbooks

## Domain 3: Infrastructure Security (18%)

> Network, compute, and edge security controls

- _No examples yet_ — WAF rules, Network Firewall policies, VPC endpoint policies, Security Group patterns

## Domain 4: Identity and Access Management (20%)

> Authentication and authorization strategies

### IAM Policies
- [Identity-based policies](./iam-policy-examples.md#1-identity-based-policies) — S3 read-only, EC2 management with MFA
- [Resource-based policies](./iam-policy-examples.md#2-resource-based-policies) — S3 bucket policies, KMS key policies, Lambda resource policies
- [Permission boundaries](./iam-policy-examples.md#3-permission-boundaries) — How boundaries work, developer limits, contractor restrictions
- [Service Control Policies (SCPs)](./iam-policy-examples.md#4-service-control-policies-scps) — Root user denial, encryption enforcement, security service protection
- [Trust policies](./iam-policy-examples.md#5-trust-policies-assumerole-policies) — Cross-account access, service roles, OIDC/SAML federation
- [Resource Control Policies (RCPs)](./iam-policy-examples.md#6-resource-control-policies-rcps) — Prevent external resource sharing

### Policy Mechanics
- [Policy evaluation logic](./iam-policy-examples.md#policy-evaluation-logic) — How AWS evaluates multiple policies
- [Testing your policies](./iam-policy-examples.md#testing-your-policies) — IAM Policy Simulator commands
- [Common exam scenarios](./iam-policy-examples.md#common-exam-scenarios) — Frequently tested patterns

## Domain 5: Data Protection (18%)

> Encryption, secrets management, data integrity

- _No examples yet_ — KMS key policies, S3 encryption enforcement, Secrets Manager rotation, CloudHSM patterns

## Domain 6: Security Foundations and Governance (14%)

> Multi-account strategy, compliance, IaC

- _No examples yet_ — CloudFormation StackSets, Firewall Manager policies, Config conformance packs

---

## How to Use

1. **Study the structure**: Each example includes comments explaining the security rationale
2. **Test locally**: Use AWS IAM Policy Simulator or the provided CLI commands
3. **Practice active recall**: Try writing policies from memory, then compare

*All examples align with the [SCS-C03 blueprint](../blueprint.md) and [study plan](../study-plan.md).*
