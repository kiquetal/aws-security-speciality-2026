# SCS-C03 Exam-Day Cheat Sheet

> One-liners and gotchas only. No explanations — you either recall it or you don't.

---

## D4: Identity & Access Management (20%)

### Policy Layers
- SCP restricts your principals. RCP restricts your resources — blocks external callers that SCPs can't touch.
- Service-linked roles are EXEMPT from RCPs (but NOT from SCPs). AWS service principals are exempt via `PrincipalIsAWSService`. Don't confuse the two.
- Boundary = ceiling on ONE role. Identity ∩ boundary = effective. Never grants.
- Delegation pattern: Deny CreateRole without boundary + Deny remove/swap boundary = safe self-service IAM.

### Cross-Account
- RAM opens, RCP closes. RAM shares infrastructure cross-account. RCP denies external access to data org-wide. Opposite problems, zero service overlap.
- RAM doesn't support KMS. Use KMS Grants for per-operation, per-principal, revocable cross-account key access.
- RAM supports: Transit Gateways, Subnets, Route 53 Resolver rules, DNS Firewall rule groups, Aurora DB clusters, License Manager, EC2 Image Builder. NOT S3, NOT KMS.
- RCP DOES support KMS (also S3, STS, SQS, Secrets Manager, DynamoDB, ECR, CloudWatch Logs, Cognito). Don't confuse with RAM's list.

### STS
- Cross-account KMS always needs BOTH sides: key policy (Account A) + identity policy (Account B). Resource policy alone is never enough for KMS.
- Direct cross-account (no AssumeRole): caller's SCP applies, not resource owner's. SCP governs the principal's account, period.
- 🧠 **"SCP follows the PERSON, not the building."** Your account's SCP applies to you even when you visit another account's resource.
- Revoke active STS sessions: inline Deny with `aws:TokenIssueTime` < timestamp. Only way — can't invalidate individual tokens.
- Session tags from IdP (SAML/OIDC) land in `aws:PrincipalTag/Key`. Same key used for ABAC matching.
- Session policy = temporary scope-down passed at AssumeRole time. Filters down, never escalates. Effective = role ∩ session policy ∩ boundary ∩ SCP.
- ⚠️ Session policy is a CEILING just like boundary — not "after" it. Both are intersected in parallel. If session allows only Get+Put, Delete is denied even if boundary allows s3:*.
- ⚠️ **Exception:** Resource-based policies that name the session ARN directly BYPASS the session policy ceiling. The filter only restricts identity-based grants.

### ABAC
- PrincipalTag = who. ResourceTag = what. RequestTag = what you're sending. Three different tags, three different moments.
- RequestTag = creation time ("must tag"). ResourceTag = access time ("can only touch matching"). Don't confuse them.
- 🧠 **"Request = birth certificate (creation). Resource = ID badge (access)."**
- ResourceTag for access control (StartInstances, StopInstances). RequestTag for creation enforcement (RunInstances). They are NOT interchangeable.

### Identity Center
- Identity Center = workforce SSO. Cognito = customer apps. Never mix them.
- Only ONE identity source at a time: built-in OR AD OR external IdP (SAML 2.0).
- Permission set = IAM role auto-created in target accounts. No manual role management.

---

## D5: Data Protection (18%)

### S3
- `s3:prefix` condition key ONLY works with `s3:ListBucket` (bucket-level). For object-level path restriction (GetObject, PutObject), use a variable in the Resource ARN instead.

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
