# SCS-C03 Exam-Day Cheat Sheet

> One-liners and gotchas only. No explanations — you either recall it or you don't.

---

## D4: Identity & Access Management (20%)

### Policy Layers
- SCP restricts your principals. RCP restricts your resources — blocks external callers that SCPs can't touch.
- 🧠 **SLRs escape the RESOURCE gate (RCP), not the PRINCIPAL gate (SCP).** SLRs are exempt from RCPs only. SCPs still apply to SLRs because they live in your account. AWS service principals are a different thing — exempt via `PrincipalIsAWSService` condition.
- Boundary = ceiling on ONE role. Identity ∩ boundary = effective. Never grants.
- Delegation pattern: Deny CreateRole without boundary + Deny remove/swap boundary = safe self-service IAM.

### Data Perimeter
- 🧠 **RCP blocks outsiders IN. SCP blocks insiders OUT.** Full data perimeter = both together. Bucket policy per-bucket doesn't scale org-wide.

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
- ⚠️ **SAME-ACCOUNT ONLY.** The resource-policy bypass of session policies and boundaries ONLY works same-account. Cross-account, session policy ceiling ALWAYS applies — no bypass possible.
- SCPs and RCPs can NEVER be bypassed — not by resource-based policies, not by anything. Only session policies and boundaries have the resource-policy bypass exception (same-account only).

### ABAC
- PrincipalTag = who. ResourceTag = what. RequestTag = what you're sending. Three different tags, three different moments.
- RequestTag = creation time ("must tag"). ResourceTag = access time ("can only touch matching"). Don't confuse them.
- 🧠 **"Request = birth certificate (creation). Resource = ID badge (access)."**
- ResourceTag for access control (StartInstances, StopInstances). RequestTag for creation enforcement (RunInstances). They are NOT interchangeable.

### Identity Center
- Identity Center = workforce SSO. Cognito = customer apps. Never mix them.
- Only ONE identity source at a time: built-in OR AD OR external IdP (SAML 2.0).
- Permission set = IAM role auto-created in target accounts. No manual role management.
- 🧠 **SCIM = auto-sync users + groups from IdP.** New user added to group in Okta → auto-inherits permission set assignment. No manual action in Identity Center.

---

## D5: Data Protection (18%)

### S3
- `s3:prefix` condition key ONLY works with `s3:ListBucket` (bucket-level). For object-level path restriction (GetObject, PutObject), use a variable in the Resource ARN instead.
- Default encryption = safety net (applies silently if no header). Bucket policy Deny = enforcement (rejects non-compliant uploads). They solve different problems.
- ⚠️ **Bucket policy Deny evaluates request headers BEFORE default encryption applies.** If Deny checks for a KMS key header and caller sends none → rejected. Default encryption never gets a chance.
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
- 🧠 **"Keys never IN AWS" = XKS. "Single-tenant HSM inside AWS" = CloudHSM custom key store.** Both integrate with KMS API, but only XKS satisfies "never in AWS infrastructure."
- CloudHSM **directly** = all operations (symmetric, asymmetric, sign, HMAC). CloudHSM **through KMS** (custom key store) = symmetric only.
- `CancelKeyDeletion` → key moves to **Disabled** (not Enabled). Must manually re-enable.
- **4 KB max** for direct KMS Encrypt/Decrypt. Anything larger → envelope encryption (GenerateDataKey → encrypt locally).
- 🧠 **"Root in key policy" = enables IAM delegation, NOT a blanket grant.** Each principal still needs explicit kms:Decrypt in their identity policy. Root opens the door for IAM — it doesn't let everyone through.
- 🧠 **KMS keys are REGIONAL.** Cross-account call to wrong region = Access Denied (key not found). Always verify the endpoint region matches the key's region.

### Secrets Manager
- Rotation doesn't re-authenticate open connections. Old connections keep working until closed. Compromised? Kill connections directly.
- Secrets Manager = built-in rotation (RDS, Aurora, DocumentDB, Redshift). Parameter Store = no native rotation.
- Deletion has 7–30 day recovery window. Cannot delete immediately.
- 🧠 **"Credentials available in DR region" = Secrets Manager cross-region replication.** MRK replicates key material, not the secret itself. Different layers.
- 🧠 **"Access Denied on DATABASE after rotation" = rotation Lambda failed to update DB password.** Secret changed but DB didn't. "Access Denied on Secrets Manager" = IAM problem. Different layers.

### Data Masking (New in C03)
- "Mask PII in logs" → **CloudWatch Logs data protection policy**. Real-time, no app changes, managed data identifiers.
- "Find PII in S3" → **Macie**. Completely different service, S3 only.
- SNS message data protection = same concept for SNS topics.

### Encryption in Transit (New in C03)
- "Encrypt between instances, no app changes" → **Nitro inter-instance encryption**. Automatic, hardware-level, zero config.
- Covers EC2-to-EC2, EKS inter-node, EMR, SageMaker. Only Nitro-based instance types.

### Detect vs Prevent (D5 Trap)
- 🧠 **"Detect external decryption" = GuardDuty S3 Protection. "Prevent external decryption" = KMS key policy condition.** The verb tells you the service.

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
- VPC Reachability Analyzer = "why can't A reach B?" (specific pair, troubleshooting one connection).
- 🧠 **"What's exposed?" = Network Access Analyzer (auditor). "Why can't A reach B?" = Reachability Analyzer (debugger).** Different tools, different questions.
- MACsec = Layer 2 encryption on **dedicated** Direct Connect only. Hosted connection → use Site-to-Site VPN over DX (IPsec).
- MACsec = Layer 2 encryption on **dedicated** Direct Connect only. Hosted connection → use Site-to-Site VPN over DX (IPsec).

### Edge
- WAF body inspection: only first **8 KB** by default (up to 64 KB paid). Large payloads can bypass rules.
- WAF attached to CloudFront must be in **us-east-1**. WAF on ALB/API Gateway = regional.
- Rate-based rule = "too many requests from one IP." Min threshold: 100 per 5 min. Bot Control = identify/manage bots.
- Shield Advanced: $3K/month, 1-year commitment. Includes DRT, cost protection, WAF free.

### Troubleshooting
- 🧠 **Timeout = network problem (SG, NACL, routing, missing endpoint). Access Denied = permissions problem (IAM, policy, key policy).** The error type tells you where to look.

---

## D1: Detection (16%)

### Service Selection
- GuardDuty = active threats NOW (C2, crypto mining, exfil). Inspector = known CVEs (software vulns). Macie = sensitive data in S3.
- Security Hub = aggregate findings + compliance dashboards (wraps Config rules). Requires Config enabled.
- Detective = investigate AFTER detection (root cause, blast radius, timeline).
- 🧠 **CloudTrail = raw API log. Detective = the investigator who reads the logs FOR you.** "Who did what" = CloudTrail. "Show me the full picture / timeline / scope" = Detective.
- CloudTrail Lake = fast + dashboards + managed + near real-time. S3+Athena = cheap + DIY + unlimited retention.
- Firewall Manager = DEPLOY rules across org. Security Hub = VIEW findings across org. Different verbs.
- "In progress" / "happening now" = active threat = GuardDuty. "What data exists?" = Macie. "What vulns exist?" = Inspector.
- "Detect C2" = GuardDuty. "Block C2 domains" = DNS Firewall. Detect ≠ prevent.
- 🧠 **DNS Firewall ALERT ≠ "generate a finding."** ALERT logs but doesn't produce security findings. GuardDuty reads DNS logs natively and generates findings with threat intel. "Detect + finding" = GuardDuty.
- 🧠 **"Detect external decryption" = GuardDuty. "Prevent external decryption" = key policy condition.** The verb tells you the service.
- "Unused permissions" / "overly permissive" = IAM Access Analyzer. "Credentials being misused" = GuardDuty.
- 🧠 **"Unused PERMISSIONS (per-action)" = Access Analyzer unused access. "Unused ROLE (last assumed)" = Config/credential report.** Different granularity.
- 🧠 **Access Analyzer unused access + policy generation = find bloat + auto-generate replacement.** Two features, one service, designed together.
- 🧠 **"Detect [bad thing] with zero custom code" = always GuardDuty.** It has built-in threat intel for Tor (TorIPCaller), malicious IPs, crypto mining, C2, DNS exfil. No setup needed.
- 🧠 **"Detect API call fast + least overhead" + org trail exists = EventBridge rule in management account.** Near real-time, one rule. Config is slower + heavier — use for remediation, not pure fast detection.

### GuardDuty Operational
- 🧠 **GuardDuty is REGIONAL.** Must enable in every region where workloads run. No findings from a region where it's not enabled.
- 🧠 **GuardDuty reads VPC Flow Logs + DNS logs via internal feed — you DON'T need to enable them yourself.** Your VPC Flow Logs are for YOUR queries (Insights, Athena). GuardDuty has its own tap.
- 🧠 **"Unusual IP" / "never-seen location" = active threat = GuardDuty.** NOT Access Analyzer (that's permission audit, not real-time threats).
- 🧠 **"Zero findings despite active workloads + GuardDuty confirmed enabled" = suppression rule archiving findings.** GuardDuty WILL generate findings on production — if you see none, something is hiding them.

### Log Sources
- **"Which domain was queried?" = Resolver Query Logs.** VPC Flow Logs only show IP:port — domain name is gone after DNS resolves.
- GuardDuty reads BOTH: DNS logs (domain) + VPC Flow Logs (traffic volume/destination). That's why it catches C2 that other services miss.

### CloudTrail / Logging
- CloudTrail Lake = its own managed data store, SQL, near real-time, dashboards. NOT S3, NOT OCSF.
- Security Lake = YOUR S3 bucket, OCSF format, normalizes ALL log sources (CloudTrail + VPC Flow + WAF + GuardDuty + third-party).
- CloudWatch Logs Insights = query app logs / VPC Flow Logs / Lambda logs. Custom syntax (not SQL). Already-ingested data.
- "Fast API call investigation" → CloudTrail Lake. "Normalize all logs into one schema" → Security Lake. "Query app/VPC logs" → CloudWatch Logs Insights.
- 🧠 **Three "lakes": CloudTrail Lake (API calls, SQL, managed store) vs Security Lake (all logs, OCSF, your S3) vs CloudWatch Logs Insights (app logs, custom syntax, CloudWatch store). No "CloudWatch Lake" exists.**
- 🧠 **CloudWatch Logs Insights = open-ended queries on data already in CW. Detective = investigate from a specific finding/entity.** "Top talkers" = Insights. "What else did this IP do?" = Detective.

---

## D2: Incident Response (14%)
- IR sequence: Isolate (swap SG to deny-all) → Snapshot (EBS forensic copy) → Tag → Investigate → Remediate. NEVER terminate first.
- 🧠 **"Validate findings" = first step before full IR (Task 2.2.3, new in C03).** Assess scope, check false positives, confirm severity. Exam keyword is "validate" or "triage", not "evaluate".
- Automated Forensics Orchestrator = Step Functions pipeline that auto-isolates + snapshots EC2 on GuardDuty finding.
- Test IR plans with **Fault Injection Service** (simulate failures). Validate resilience with **Resilience Hub**.
- Validate findings BEFORE full IR — assess scope, check false positives, correlate in Security Hub, investigate in Detective.
- Revoke compromised sessions: inline Deny with `aws:TokenIssueTime` < timestamp on the role.

---

## D6: Governance (14%)
- Management account exempt from BOTH SCPs and RCPs. Don't put workloads there.
- Control Tower = automated landing zone + guardrails (SCPs/RCPs for preventive, Config for detective).
- Firewall Manager = DEPLOY rules across org. Security Hub = VIEW findings across org. Control Tower = ONBOARD accounts.
- 🧠 **"Which mechanism prevents X?" = SCP. "Which service automates guardrails?" = Control Tower.** Control Tower uses SCPs — the mechanism is SCP, the automation is Control Tower.
- 🧠 **"PREVENT/BLOCK launches" = SCP (preventive). "DETECT + FIX after" = Config (detective).** If the instance should NEVER exist, SCP. If it can exist briefly then get fixed, Config.
- 🧠 **"Share resources cross-account" = RAM. "Enforce guardrails cross-account" = SCP/Control Tower.** DNS Firewall rule groups, TGWs, subnets = RAM. Deny actions org-wide = SCP.
- 🧠 **Audit Manager = YOUR compliance evidence. Artifact = AWS's compliance reports.** "Collect evidence for our audit" = Audit Manager. "Download AWS's SOC 2" = Artifact.
- 🧠 **StackSets = push IaC to many accounts (any resource). Firewall Manager = push security RULES only (WAF/SG/NF/DNS FW).** "Deploy GuardDuty + Config" = StackSets. "Deploy WAF rules" = FM.
- 🧠 **FM auto-remediates. StackSets does NOT.** Someone removes WAF from ALB → FM re-applies. Someone disables Config → StackSets does nothing.
- 🧠 **StackSets = deploy resources/services. Conformance pack = deploy compliance rules + remediation.** "Enable GuardDuty org-wide" = StackSets. "Check encryption + fix" = conformance pack.
- 🧠 **Service Catalog = users PULL pre-approved resources (self-service). StackSets = admin PUSHES.** Launch role means dev doesn't need broad IAM.
- 🧠 **Config conformance pack = bundle of rules + remediation as ONE unit, org-wide from delegated admin.** Security Hub standard = same rules but dashboard + no built-in remediation.
- 🧠 **FM creates WAF/Shield/SG directly (no RAM). FM only enforces DNS FW + Network FW (needs RAM to share first).** Ask: "Does the resource already exist in another account?" Yes = RAM.
- 🧠 **Config can't remediate its own disablement.** If someone stops Config, the rule can't fire. Use SCP to prevent `StopConfigurationRecorder`.
- 🧠 **Control Tower guardrails: Preventive = SCP (block API). Detective = Config (detect after). Proactive = CF Hook (validate template before deploy).**
- 🧠 **"Validate template content" = Proactive guardrail (CF Hook). "Block API call" = SCP.** SCP can't see what's inside a CloudFormation template.
- 🧠 **Every security service supports delegated admin.** GuardDuty, Security Hub, FM, Config, Audit Manager, Macie, Inspector, Detective, Security Lake, Access Analyzer.
---

## Quotas That Trick You (4-5-8-32-5120)

| Service | Limit | Value |
|---|---|---|
| KMS direct Encrypt/Decrypt | Max data size | 4 KB |
| SCP / RCP | Max per target | 5 |
| WAF | Body inspection default | 8 KB (up to 64 KB paid) |
| KMS key policy | Max size | 32 KB |
| SCP / RCP | Max characters | 5,120 |
| KMS key deletion | Wait period | 7–30 days (default 30) |
| Role chaining | Max session | 1 hour (always resets) |

- 🧠 **`GetCallerIdentity` cannot be denied by anything.** Not IAM, not SCP, not boundary, not session policy.
- 🧠 **`aws:TokenIssueTime` = revoke sessions.** Inline Deny with DateLessThan. Only way to kill active STS tokens.

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
| `aws:SourceVpce` | Restrict access to specific VPC endpoint |
| `aws:SourceVpc` | Restrict access to any endpoint in a VPC |
| `aws:MultiFactorAuthPresent` | Require MFA for sensitive operations |
| `aws:RequestTag/Key` | Enforce tag at creation time |
| `aws:ResourceTag/Key` | Control access based on existing resource tags |
