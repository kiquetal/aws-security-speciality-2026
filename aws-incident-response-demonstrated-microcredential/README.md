# AWS Incident Response - Demonstrated Microcredential

## Exam Objectives

| # | Objective | Key Services |
|---|-----------|-------------|
| 1 | Implement audit and compliance controls | CloudTrail, Config, CloudWatch, Athena |
| 2 | Contain data exfiltration | S3, VPC, CloudWatch, SNS |
| 3 | Establish database security | RDS, IAM, CloudWatch |
| 4 | Identify and remediate compromised resources | EC2, Systems Manager, Lambda, Step Functions, CloudWatch |
| 5 | Eradicate backdoor access | IAM, CloudTrail, Lambda |
| 6 | Recover with network hardening | VPC, EC2 Auto Scaling, EC2, Config |

## Core Incident Response Lifecycle

Every scenario follows this pattern:

```
Detect → Contain → Eradicate → Recover
```

## AWS Services Covered

- Amazon Athena
- Amazon EC2 Auto Scaling
- AWS CloudTrail
- Amazon CloudWatch
- AWS Config
- Amazon EC2
- AWS IAM
- AWS Lambda
- Amazon RDS
- Amazon S3
- Amazon SNS
- AWS Systems Manager
- AWS Step Functions
- Amazon VPC

## Study Materials

- `notes/` — Key concepts and patterns for each objective
- `labs/` — Hands-on challenge scenarios with solutions
- `diagrams/` — Architecture and flow diagrams

## Study Priority (for tomorrow)

1. **HIGH** — Containment patterns (EC2 isolation, S3 public access remediation)
2. **HIGH** — IAM backdoor eradication (session revocation, key management)
3. **HIGH** — Automated remediation (Config + EventBridge + Lambda/Step Functions)
4. **MEDIUM** — CloudTrail log analysis with Athena
5. **MEDIUM** — VPC network hardening and recovery
6. **MEDIUM** — RDS security controls
