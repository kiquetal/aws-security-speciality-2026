# SCS-C03 Exam-Day Cheat Sheet

> One-liners and gotchas only. No explanations — you either recall it or you don't.

---

## D4: Identity & Access Management (20%)

### Policy Layers
- SCP restricts your principals. RCP restricts your resources — blocks external callers that SCPs can't touch.
- 🧠 **SLRs escape the RESOURCE gate (RCP), not the PRINCIPAL gate (SCP).** SLRs are exempt from RCPs only. SCPs still apply to SLRs because they live in your account. AWS service principals are a different thing — exempt via `PrincipalIsAWSService` condition.
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
- SCPs and RCPs can NEVER be bypassed — not by resource-based policies, not by anything. Only session policies and boundaries have the resource-policy bypass exception.

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
- Default encryption = safety net (applies silently if no header). Bucket policy Deny = enforcement (rejects non-compliant uploads). They solve different problems.
- SSE-KMS permissions: **upload** = `s3:PutObject` + `kms:GenerateDataKey`. **Download** = `s3:GetObject` + `kms:Decrypt`. Not Encrypt — it's envelope encryption.
- Object Lock requires versioning. Compliance mode = nobody can delete, not even root. Governance mode = overridable with `s3:BypassGovernanceRetention`.
- Legal Hold = no expiration, independent of retention period. "Lawsuit" / "preserve indefinitely" → Legal Hold.
- 🧠 **Cross-account S3 + SSE-KMS = THREE policies:** bucket policy (Account A) + key policy (Account A) + identity policy (Account B). Forget any one = Access Denied.

### KMS
- Grants are **eventually consistent** (up to 5 min). To use immediately after CreateGrant, pass the **grant token** in the subsequent API call (`--grant-tokens`). No token = AccessDenied until propagation completes.
- Grants have **no expiration** — they last forever until explicitly revoked (`RevokeGrant`) or retired (`RetireGrant`). No auto-cleanup.
- 🧠 **Admin revokes (takes away). Grantee retires (gives back).** `RevokeGrant` = key admin. `RetireGrant` = the grantee themselves.
- Multi-region keys share the **same key ID** (`mrk-` prefix) and **same key material** across regions. Encrypt in one region, decrypt in another locally. Imported keys CANNOT be multi-region.
- MRK key policies are **independent per region** — updating policy on primary does NOT propagate to replicas. Must update each separately.
- "Global Table + SSE-KMS + multi-region" → answer is always MRK. AWS managed keys (`aws/dynamodb`) are single-region only.
- Key deletion waiting period: **7–30 days** (default 30). Can cancel with `CancelKeyDeletion` anytime during wait.
- Prevent accidental deletion: **SCP Deny `kms:ScheduleKeyDeletion`**. Detect: **CloudTrail + EventBridge + Lambda** (auto-cancel + alert).
- **Key store backends:** Default (multi-tenant, all ops) vs Custom Key Store (single-tenant CloudHSM, symmetric only via KMS) vs XKS (keys outside AWS, symmetric only via KMS). The symmetric-only limit is KMS, not the HSM.
- CloudHSM **directly** = all operations (symmetric, asymmetric, sign, HMAC). CloudHSM **through KMS** (custom key store) = symmetric only.
- `CancelKeyDeletion` → key moves to **Disabled** (not Enabled). Must manually re-enable.

### Secrets Manager
- Rotation doesn't re-authenticate open connections. Old connections keep working until closed. Compromised? Kill connections directly.
- Secrets Manager = built-in rotation (RDS, Aurora, DocumentDB, Redshift). Parameter Store = no native rotation.
- Deletion has 7–30 day recovery window. Cannot delete immediately.

### Data Masking (New in C03)
- "Mask PII in logs" → **CloudWatch Logs data protection policy**. Real-time, no app changes, managed data identifiers.
- "Find PII in S3" → **Macie**. Completely different service, S3 only.
- SNS message data protection = same concept for SNS topics.

### Encryption in Transit (New in C03)
- "Encrypt between instances, no app changes" → **Nitro inter-instance encryption**. Automatic, hardware-level, zero config.
- Covers EC2-to-EC2, EKS inter-node, EMR, SageMaker. Only Nitro-based instance types.

---

## D3: Infrastructure Security (18%)

### Firewalls
- Network Firewall: 1 endpoint per AZ, dedicated firewall subnet, route tables direct traffic through it. ~$288/month per AZ.
- Stateless evaluated FIRST. If stateless says "pass" → skips stateful entirely. "Forward" → sends to stateful engine.
- TLS inspection requires a CA certificate in ACM — firewall decrypts, inspects, re-encrypts (MITM pattern).
- DNS Firewall = domain resolution filtering (VPC-level). Network Firewall = traffic content inspection (subnet-level). Different layers.

### Network
- Gateway endpoint (S3, DynamoDB) = free, route table entry. Interface endpoint = ENI + PrivateLink, costs money, needs SG.
- Endpoint policy + bucket policy BOTH evaluated. Endpoint policy doesn't replace resource policies.
- NACLs are stateless — need explicit inbound rule for ephemeral ports (1024–65535) on return traffic. SGs are stateful — handle it automatically.
- Verified Access = zero-trust access to internal apps without VPN. Evaluates identity + device posture.
- Network Access Analyzer = find unintended network paths (reachable from internet when shouldn't be).

### Edge
- WAF body inspection: only first **8 KB** by default (up to 64 KB paid). Large payloads can bypass rules.
- WAF attached to CloudFront must be in **us-east-1**. WAF on ALB/API Gateway = regional.
- Rate-based rule = "too many requests from one IP." Min threshold: 100 per 5 min. Bot Control = identify/manage bots.
- Shield Advanced: $3K/month, 1-year commitment. Includes DRT, cost protection, WAF free.

---

## D1: Detection (16%)

### Service Selection
- GuardDuty = active threats NOW (C2, crypto mining, exfil). Inspector = known CVEs (software vulns). Macie = sensitive data in S3.
- Security Hub = aggregate findings + compliance dashboards (wraps Config rules). Requires Config enabled.
- Detective = investigate AFTER detection (root cause, blast radius, timeline).
- CloudTrail Lake = fast + dashboards + managed + near real-time. S3+Athena = cheap + DIY + unlimited retention.
- Firewall Manager = DEPLOY rules across org. Security Hub = VIEW findings across org. Different verbs.
- "In progress" / "happening now" = active threat = GuardDuty. "What data exists?" = Macie. "What vulns exist?" = Inspector.
- "Detect C2" = GuardDuty. "Block C2 domains" = DNS Firewall. Detect ≠ prevent.
- 🧠 **"Detect external decryption" = GuardDuty. "Prevent external decryption" = key policy condition.** The verb tells you the service.
- "Unused permissions" / "overly permissive" = IAM Access Analyzer. "Credentials being misused" = GuardDuty.
- "Normalize logs into common schema" = Security Lake (OCSF format).

### CloudTrail
- CloudTrail Lake = its own managed data store, SQL, near real-time, dashboards. NOT S3, NOT OCSF.
- Security Lake = YOUR S3 bucket, OCSF format, normalizes ALL log sources (CloudTrail + VPC Flow + WAF + GuardDuty + third-party).
- "Fast API call investigation" → CloudTrail Lake. "Normalize all logs into one schema" → Security Lake.

---

## D2: Incident Response (14%)
- IR sequence: Isolate (swap SG to deny-all) → Snapshot (EBS forensic copy) → Tag → Investigate → Remediate. NEVER terminate first.
- Automated Forensics Orchestrator = Step Functions pipeline that auto-isolates + snapshots EC2 on GuardDuty finding.
- Test IR plans with **Fault Injection Service** (simulate failures). Validate resilience with **Resilience Hub**.
- Validate findings BEFORE full IR — assess scope, check false positives, correlate in Security Hub, investigate in Detective.
- Revoke compromised sessions: inline Deny with `aws:TokenIssueTime` < timestamp on the role.

---

## D6: Governance (14%)
- Management account exempt from BOTH SCPs and RCPs. Don't put workloads there.
- Control Tower = automated landing zone + guardrails (SCPs/RCPs for preventive, Config for detective).
- Firewall Manager = DEPLOY rules across org. Security Hub = VIEW findings across org. Control Tower = ONBOARD accounts.

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
