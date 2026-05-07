# SCS-C03 Exam-Day Cheat Sheet

> One-liners and gotchas only. No explanations — you either recall it or you don't.

---

## D4: Identity & Access Management (20%)

### Policy Layers
- SCP restricts your principals. RCP restricts your resources — blocks external callers that SCPs can't touch.
- Service-linked roles are EXEMPT from RCPs (but NOT from SCPs). AWS service principals are exempt via `PrincipalIsAWSService`. Don't confuse the two.

### Cross-Account
- RAM opens, RCP closes. RAM shares infrastructure cross-account. RCP denies external access to data org-wide. Opposite problems, zero service overlap.
- RAM doesn't support KMS. Use KMS Grants for per-operation, per-principal, revocable cross-account key access.
- RAM supports: Transit Gateways, Subnets, Route 53 Resolver rules, DNS Firewall rule groups, Aurora DB clusters, License Manager, EC2 Image Builder. NOT S3, NOT KMS.
- RCP DOES support KMS (also S3, STS, SQS, Secrets Manager, DynamoDB, ECR, CloudWatch Logs, Cognito). Don't confuse with RAM's list.

### STS
-

---

## D5: Data Protection (18%)

### KMS
-

### Secrets Manager
-

---

## D3: Infrastructure Security (18%)

### Firewalls
-

### Edge
-

---

## D1: Detection (16%)

### Service Selection
-

### CloudTrail
-

---

## D2: Incident Response (14%)
-

---

## D6: Governance (14%)
-

---

## Quotas That Trick You

| Service | Limit | Value |
|---|---|---|
| KMS key policy | Max size | 32 KB |
| SCP / RCP | Max size | 5,120 chars |
| SCP / RCP | Max per target | 5 |

---

## Condition Keys to Know Cold

| Key | When to Use |
|---|---|
| `aws:PrincipalOrgID` | Restrict to your org |
| `aws:PrincipalIsAWSService` | Exempt AWS services from org-deny rules |
| `aws:SourceArn` | Confused deputy prevention |
| `sts:ExternalId` | Third-party cross-account roles |
| `aws:PrincipalServiceName` | Identify which AWS service is calling |
| `aws:TokenIssueTime` | Revoke STS sessions issued before a timestamp |
