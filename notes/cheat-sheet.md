# SCS-C03 Exam-Day Cheat Sheet

> One-liners and gotchas only. No explanations — you either recall it or you don't.

---

## D4: Identity & Access Management (20%)

---

### Policy Layers
- SCP restricts your principals. RCP restricts your resources — blocks external callers that SCPs can't touch.
- 🧠 **SCP is a CEILING (allowlist).** If an action isn't in the SCP Allow, it's implicitly denied — IAM policy Allow is irrelevant. SCP Allow ec2+lambda only → s3:* in IAM = denied.
- 🧠 **SLRs escape the RESOURCE gate (RCP), not the PRINCIPAL gate (SCP).** SLRs are exempt from RCPs only. SCPs still apply to SLRs because they live in your account. AWS service principals are a different thing — exempt via `PrincipalIsAWSService` condition.
- Boundary = ceiling on ONE role. Identity ∩ boundary = effective. Never grants.
- Delegation pattern: Deny CreateRole without boundary + Deny remove/swap boundary = safe self-service IAM.
- 🧠 **SCP questions: read the ATTACHMENT TARGET first (OU vs account), not the JSON.** "Existing + future accounts" = attach to OU. Attach to individual accounts = new accounts miss it.

---

### Data Perimeter
- 🧠 **RCP blocks outsiders IN. SCP blocks insiders OUT.** Full data perimeter = both together. Bucket policy per-bucket doesn't scale org-wide.
- 🧠 **RCP protects YOUR resources only (inbound). Outbound to external resources = SCP's job.** If your SLR replicates to a partner's bucket, RCP doesn't apply — the partner's bucket isn't your resource.

---

### Cross-Account
- RAM opens, RCP closes. RAM shares infrastructure cross-account. RCP denies external access to data org-wide. Opposite problems, zero service overlap.
- RAM doesn't support KMS. Use KMS Grants for per-operation, per-principal, revocable cross-account key access.
- RAM supports: Transit Gateways, Subnets, Route 53 Resolver rules, DNS Firewall rule groups, Aurora DB clusters, License Manager, EC2 Image Builder. NOT S3, NOT KMS.
- RCP DOES support KMS (also S3, STS, SQS, Secrets Manager, DynamoDB, ECR, CloudWatch Logs, Cognito). Don't confuse with RAM's list.

---

### STS
- Cross-account KMS always needs BOTH sides: key policy (Account A) + identity policy (Account B). Resource policy alone is never enough for KMS.
- Direct cross-account (no AssumeRole): caller's SCP applies, not resource owner's. SCP governs the principal's account, period.
- 🧠 **"SCP follows the PERSON, not the building."** Your account's SCP applies to you even when you visit another account's resource.
- Revoke active STS sessions: inline Deny with `aws:TokenIssueTime` < timestamp. Only way — can't invalidate individual tokens.
- 🧠 **OutsideAWS = TokenIssueTime (your instances refresh, attacker can't). InsideAWS = deny-all SG on attacker's instance ONLY (surgical isolation).**
- 🧠 **OutsideAWS = credentials used externally → TokenIssueTime OK. InsideAWS = credentials used internally → need surgical SG.**
- 🧠 **IAM user leaked = Deny * on user (keys + password + sessions). Role leaked = TokenIssueTime (only temp sessions exist).**
- Session tags from IdP (SAML/OIDC) land in `aws:PrincipalTag/Key`. Same key used for ABAC matching.
- Session policy = temporary scope-down passed at AssumeRole time. Filters down, never escalates. Effective = role ∩ session policy ∩ boundary ∩ SCP.
- ⚠️ Session policy is a CEILING just like boundary — not "after" it. Both are intersected in parallel. If session allows only Get+Put, Delete is denied even if boundary allows s3:*.
- ⚠️ **Exception:** Resource-based policies that name the session ARN directly BYPASS the session policy ceiling. The filter only restricts identity-based grants.
- ⚠️ **SAME-ACCOUNT ONLY.** The resource-policy bypass of session policies and boundaries ONLY works same-account. Cross-account, session policy ceiling ALWAYS applies — no bypass possible.
- SCPs and RCPs can NEVER be bypassed — not by resource-based policies, not by anything. Only session policies and boundaries have the resource-policy bypass exception (same-account only).

---

### ABAC
- PrincipalTag = who. ResourceTag = what. RequestTag = what you're sending. Three different tags, three different moments.
- RequestTag = creation time ("must tag"). ResourceTag = access time ("can only touch matching"). Don't confuse them.
- 🧠 **"Request = birth certificate (creation). Resource = ID badge (access)."**
- ResourceTag for access control (StartInstances, StopInstances). RequestTag for creation enforcement (RunInstances). They are NOT interchangeable.

---

### Identity Center
- Identity Center = workforce SSO. Cognito = customer apps. Never mix them.
- 🧠 **Cognito Identity Pool = managed STS.** You define the IAM role, Identity Pool calls AssumeRoleWithWebIdentity FOR you. Don't call STS directly when using Identity Pool.
- Only ONE identity source at a time: built-in OR AD OR external IdP (SAML 2.0).
- Permission set = IAM role auto-created in target accounts. No manual role management.
- 🧠 **SCIM = auto-sync users + groups from IdP.** New user added to group in Okta → auto-inherits permission set assignment. No manual action in Identity Center.

---

### Directory Service
- 🧠 **Simple AD = Samba (no trusts, no RDS SQL, no Identity Center). AD Connector = proxy (no data in AWS, no trusts). Managed AD = full MS AD (trusts, RDS SQL, Identity Center).**
- 🧠 **"Need trusts" or "RDS SQL Server" or "Identity Center" = Managed AD. Always.** Simple AD and AD Connector are automatically eliminated.
- 🧠 **One-way trust "AWS trusts on-prem" = on-prem users access AWS. Cloud users CANNOT access on-prem.** Trust direction: users in the TRUSTED domain access resources in the TRUSTING domain.
- 🧠 **AD Connector = pipe. On-prem goes down = all AWS auth fails.** No caching, no data in AWS.
- 🧠 **Federation with on-prem AD = ADFS + IAM ROLES + AssumeRoleWithSAML.** Never IAM users/groups. Cognito = customer apps, not enterprise.
- 🧠 **ADFS federation does NOT need AD Connector.** ADFS uses SAML directly to STS. AD Connector is a separate pattern for Directory Service integration (WorkSpaces, domain-join).
- 🧠 **"No AWS Directory Service infrastructure" = ADFS on-prem + Identity Center external IdP.** AD Connector IS Directory Service infrastructure (you deploy + maintain it in AWS). ADFS lives entirely on-prem.
- 🧠 **AD Connector = connects to on-prem AD (proxy). Simple AD = standalone Samba (own users, NO connection to on-prem).** Never pick Simple AD when question says "on-prem AD."

---

## D5: Data Protection (18%)

---

### S3
- `s3:prefix` condition key ONLY works with `s3:ListBucket` (bucket-level). For object-level path restriction (GetObject, PutObject), use a variable in the Resource ARN instead.
- Default encryption = safety net (applies silently if no header). Bucket policy Deny = enforcement (rejects non-compliant uploads). They solve different problems.
- ⚠️ **Bucket policy Deny evaluates request headers BEFORE default encryption applies.** If Deny checks for a KMS key header and caller sends none → rejected. Default encryption never gets a chance.
- SSE-KMS permissions: **upload** = `s3:PutObject` + `kms:GenerateDataKey`. **Download** = `s3:GetObject` + `kms:Decrypt`. Not Encrypt — it's envelope encryption.
- 🧠 **S3 NEVER calls kms:Encrypt.** Upload = GenerateDataKey. Multipart = GenerateDataKey + Decrypt (reassembly). kms:Encrypt is only for direct <4KB encryption, not S3.
- Object Lock requires versioning. Compliance mode = nobody can delete, not even root. Governance mode = overridable with `s3:BypassGovernanceRetention`.
- Legal Hold = no expiration, independent of retention period. "Lawsuit" / "preserve indefinitely" → Legal Hold.
- 🧠 **"Irreversible once confirmed" = Glacier Vault Lock (24hr confirm window, then permanent).** Object Lock Compliance = per-object retention. Vault Lock = per-vault immutable policy.
- 🧠 **Vault Lock vs Object Lock decision: "24hr confirm + permanently irreversible POLICY" = Vault Lock. "Fixed retention period per OBJECT, auto-expires" = Object Lock Compliance.** Vault Lock = policy-level forever. Object Lock = object-level with expiry.
- 🧠 **Cross-account S3 + SSE-KMS = THREE policies:** bucket policy (Account A) + key policy (Account A) + identity policy (Account B). Forget any one = Access Denied.
- 🧠 **S3 server access logging = ACLs (legacy).** Target logging bucket needs WRITE + READ_ACP ACL for log delivery group. Not bucket policies.
- 🧠 **BucketOwnerEnforced (ACLs disabled) = S3 access logging BREAKS.** Must re-enable ACLs (BucketOwnerPreferred) + grant log-delivery group. Config remediation for logging also needs `s3:GetBucketAcl`.
- 🧠 **Config delivery to S3 = bucket policy needs `s3:PutObject` + `s3:GetBucketAcl` for `config.amazonaws.com`.** Same ACL-check pattern — service verifies bucket ownership before writing.
- 🧠 **Config delivery to S3 = bucket policy needs `s3:PutObject` + `s3:GetBucketAcl` for `config.amazonaws.com`.** Same ACL-check pattern — service verifies bucket ownership before writing.
- 🧠 **S3 Batch Operations cross-account: identity policy alone is insufficient.** Destination bucket policies must also grant the batch job role. Same "both sides" rule as all cross-account S3.
- 🧠 **S3 Batch Operations = regional.** Job + manifest + target bucket must ALL be in the same region. No cross-region support.

---

### KMS
- 🧠 **Sign = private key → verify = public key → integrity + non-repudiation. Encrypt = public key → decrypt = private key → confidentiality.** Direction determines the security property.
- 🧠 **"Sign = YOUR secret hand. Verify = everyone can look."** Private signs, public verifies. Can't sign with public (anyone could forge it).
- Grants are **eventually consistent** (up to 5 min). To use immediately after CreateGrant, pass the **grant token** in the subsequent API call (`--grant-tokens`). No token = AccessDenied until propagation completes.
- 🧠 **EBS encryption by default = opt-in PER REGION.** Must enable in each region's EC2 settings. Not retroactive. S3 encryption is automatic globally (no opt-in since Jan 2023). "Regional opt-in + encryption at rest" = EBS.
- 🧠 **EBS snapshot sharing: "copy then share" vs "share directly."** Default key (`aws/ebs`) = MUST copy with CMK first (can't share managed keys). Cross-account/external = always copy with new CMK + Grant. Direct share only works if recipient already has key access (rare).
- 🧠 **EC2 + encrypted EBS always needs `kms:CreateGrant`.** Start existing = CreateGrant + Decrypt. Create new = CreateGrant + GenerateDataKey(WithoutPlaintext). EC2 delegates key access to EBS backend via grants.
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
- 🧠 **Key policy conditions enforced regardless of caller's identity policy.** Role having kms:Decrypt ≠ key policy conditions are satisfied. KMS evaluates key policy independently.
- 🧠 **KMS keys are REGIONAL.** Cross-account call to wrong region = Access Denied (key not found). Always verify the endpoint region matches the key's region.
- 🧠 **Cross-account KMS: key policy MUST name the external account.** Root in key policy enables IAM delegation same-account only. For Account B to use Account A's key, key policy must grant Account B's root or role explicitly.
- 🧠 **S3 wraps KMS errors as S3 AccessDenied.** Caller called S3, not KMS directly. Error surface = S3, root cause = KMS. Direct `kms:Decrypt` call → KMS.AccessDeniedException.
- 🧠 **SSE-S3 already generates a unique DEK per object.** Envelope encryption = every object gets its own key automatically. "Different key per file" = SSE-S3 (zero config).
- 🧠 **Imported key material = immediate delete (DeleteImportedKeyMaterial).** No 7-day wait. ScheduleKeyDeletion minimum = 7 days. "Within 24 hours" = only imported satisfies.
- 🧠 **KMS: creator ≠ owner, root ≠ full access.** Nobody has automatic access. Must be explicitly granted via key policy/IAM/grant. kms:CreateKey holder CAN set initial key policy.
- 🧠 **Kinesis encrypted stream: Producer = kms:GenerateDataKey. Consumer = kms:Decrypt + kms:DescribeKey.** Same upload/download pattern as S3, plus DescribeKey required for consumer verification.
- 🧠 **CRR + SSE-KMS: source = kms:Decrypt. Destination = kms:GenerateDataKey (not kms:Encrypt).** Same rule as all S3 uploads — S3 never uses kms:Encrypt.
- 🧠 **CRR replication role needs exactly THREE permissions: (1) kms:Decrypt on source key, (2) kms:GenerateDataKey on dest key, (3) s3:GetObjectVersionForReplication on source.** Mnemonic: D-G-F (Decrypt, GenerateDataKey, ForReplication). GetObjectVersion alone is NOT enough — ForReplication is the replication-specific permission.
- 🧠 **CRR rewrites encryption context to destination bucket ARN.** Key policy conditions on dest key must reference dest bucket, not source.
- 🧠 **CRR preserves source custom encryption context alongside S3 system context.** If dest key policy uses strict conditions, custom context from source causes mismatch.
- 🧠 **DynamoDB + customer-managed KMS = needs `kms:CreateGrant` + `kms:DescribeKey`.** DynamoDB delegates via grants internally (like EBS). Never uses kms:Encrypt.

---

### Secrets Manager
- 🧠 **"Retrieve secrets at boot/initialization" = instance role + runtime API call (SSM or SM). CF `ValueFrom` = deploy-time injection (secret visible in stack, wrong timing).** Exam says "during bootstrapping" = boot time, not deploy time.
- Rotation doesn't re-authenticate open connections. Old connections keep working until closed. Compromised? Kill connections directly.
- Secrets Manager = built-in rotation (RDS, Aurora, DocumentDB, Redshift). Parameter Store = no native rotation.
- Deletion has 7–30 day recovery window. Cannot delete immediately.
- 🧠 **"Credentials available in DR region" = Secrets Manager cross-region replication.** MRK replicates key material, not the secret itself. Different layers.
- 🧠 **"Access Denied on DATABASE after rotation" = rotation Lambda failed to update DB password.** Secret changed but DB didn't. "Access Denied on Secrets Manager" = IAM problem. Different layers.

---

### Data Masking (New in C03)
- "Mask PII in logs" → **CloudWatch Logs data protection policy**. Real-time, no app changes, managed data identifiers.
- "Find PII in S3" → **Macie**. Completely different service, S3 only.
- SNS message data protection = same concept for SNS topics.
- 🧠 **CW Logs data protection has TWO outputs:** (1) Masking = `***` in original log group. (2) Audit = record of what was detected sent to separate destination (CW log group / S3 / Firehose).
- 🧠 **"Audit what was masked" = data protection audit destination. "Audit who viewed raw data" = CloudTrail (logs:Unmask calls).** Different questions, different answers.

---

### Encryption in Transit (New in C03)
- "Encrypt between instances, no app changes" → **Nitro inter-instance encryption**. Automatic, hardware-level, zero config.
- Covers EC2-to-EC2, EKS inter-node, SageMaker. Only Nitro-based instance types.
- 🧠 **EMR in-transit ≠ Nitro.** EMR inter-node encryption = EMR security configuration + in-transit enabled + PEM certificates (Private CA). Nitro is NOT the answer for EMR compliance.
- 🧠 **Kinesis encrypted stream: Producer = kms:GenerateDataKey. Consumer = kms:Decrypt + kms:DescribeKey.** Not CreateGrant — Kinesis doesn't delegate via grants.
- 🧠 **Config org custom rule = central Lambda invoked cross-account.** Fix "Unable to invoke": Lambda resource-based policy granting `config.amazonaws.com` + `SourceAccount` condition for member accounts.
- 🧠 **State Manager: ONE association supports BOTH OnBoot trigger + rate schedule.** Don't create two associations — one does both.
- 🧠 **State Manager = "enforce desired state on schedule" (proactive). Session Manager = "connect to instance remotely" (interactive). Config remediation = "detect drift then fix" (reactive, has latency).** "Ensure X applied every 30 min + on launch" = State Manager.
- 🧠 **Inspector SBOM = on-demand API only (no built-in scheduler).** Schedule with EventBridge + Lambda calling `CreateSbomExport`. Export needs bucket policy for `inspector2.amazonaws.com`.

---

### Detect vs Prevent (D5 Trap)
- 🧠 **"Detect external decryption" = GuardDuty S3 Protection. "Prevent external decryption" = KMS key policy condition.** The verb tells you the service.

---

## D3: Infrastructure Security (18%)

---

### Firewalls
- Network Firewall: 1 endpoint per AZ, dedicated firewall subnet, route tables direct traffic through it. ~$288/month per AZ.
- Stateless evaluated FIRST. If stateless says "pass" → skips stateful entirely. "Forward" → sends to stateful engine.
- TLS inspection requires a CA certificate in ACM — firewall decrypts, inspects, re-encrypts (MITM pattern).
- DNS Firewall = domain resolution filtering (VPC-level). Network Firewall = traffic content inspection (subnet-level). Different layers.

---

### Network
- Gateway endpoint (S3, DynamoDB) = free, route table entry. Interface endpoint = ENI + PrivateLink, costs money, needs SG.
- 🧠 **Gateway endpoint = SAME REGION only.** Routes traffic to S3/DynamoDB in the VPC's region. Cross-region S3 access = needs NAT/IGW or Interface endpoint.
- 🧠 **S3 SSE-KMS = server-side (no KMS endpoint needed). Direct kms:Decrypt/GenerateDataKey in YOUR code = needs KMS Interface endpoint.** Count DynamoDB separately (Gateway endpoint).
- Endpoint policy + bucket policy BOTH evaluated. Endpoint policy doesn't replace resource policies.
- NACLs are stateless — need explicit inbound rule for ephemeral ports (1024–65535) on return traffic. SGs are stateful — handle it automatically.
- Verified Access = zero-trust access to internal apps without VPN. Evaluates identity + device posture.
- 🧠 **VPC Lattice = service-to-service (east/west) across accounts.** IAM auth (SigV4), share via RAM, auth policies. No certs, no mesh. "Cross-account service-to-service + least overhead" = Lattice.
- Network Access Analyzer = find unintended network paths (reachable from internet when shouldn't be).
- VPC Reachability Analyzer = "why can't A reach B?" (specific pair, troubleshooting one connection).
- 🧠 **"What's exposed?" = Network Access Analyzer (auditor). "Why can't A reach B?" = Reachability Analyzer (debugger).** Different tools, different questions.
- 🧠 **"Find all exposed paths" = Network Access Analyzer. "Explain WHY this specific path works (hop-by-hop)" = Reachability Analyzer.** NAA finds. RA explains.
- 🧠 **TGW appliance mode = force request + return traffic through SAME AZ.** Without it, TGW splits across AZs = stateful firewall drops return (no conn state). Enable on security VPC attachment.
- 🧠 **WAF scope-down statement = "only apply rule group to matching requests."** Exempt known-good traffic (mobile apps, server-to-server) from Challenge/CAPTCHA. Both require browser/JS.
- MACsec = Layer 2 encryption on **dedicated** Direct Connect only. Hosted connection → use Site-to-Site VPN over DX (IPsec).
- 🧠 **IPv4 outbound-only = NAT Gateway. IPv6 outbound-only = Egress-Only Internet Gateway.** NAT doesn't exist for IPv6 — all IPv6 is globally routable. Egress-only IGW = one-way gate (outbound yes, inbound no).
- 🧠 **"Individual remote users (home)" = Client VPN (SSL). "Two fixed networks (office↔AWS)" = Site-to-Site VPN (IPsec). "Physical dedicated link" = Direct Connect.**

---

### Troubleshooting

---

### Edge
- WAF body inspection: only first **8 KB** by default (up to 64 KB paid). Large payloads can bypass rules.
- WAF attached to CloudFront must be in **us-east-1**. WAF on ALB/API Gateway = regional.
- 🧠 **"Add security headers (HSTS, CSP, X-Content-Type-Options) to CloudFront, least overhead" = CloudFront response headers policy (managed, zero code).** Lambda@Edge = only if you need dynamic/conditional logic.
- 🧠 **CloudFront `Authorization` header = Cache Policy ONLY.** Origin Request Policy → HTTP 400 error. Authorization must be part of cache key to prevent serving authenticated responses to unauthenticated users.
- 🧠 **CW agent ships logs (not SSM agent).** SSM agent = execute commands, sessions, patching. CW agent = ship custom log files + metrics. SSM can INSTALL CW agent but can't replace it.
- 🧠 **"Public-facing + HTTPS to customers" = inbound 0.0.0.0/0 on 443.** "Highest security" doesn't override the requirement of being publicly accessible.
- 🧠 **ALB + HIDS + PFS: send encrypted traffic END-TO-END to EC2 (ECDHE + PFS).** Don't decrypt at ALB if HIDS needs to see traffic on instance. HIDS inspects AFTER decryption at the host. ECDHE = ephemeral keys = PFS (past sessions safe even if key leaks later). Static RSA = no PFS.
- Rate-based rule = "too many requests from one IP." Min threshold: 100 per 5 min. Bot Control = identify/manage bots.
- 🧠 **WAF rate-based types: Blanket (all pages) vs URI-specific (one path) vs IP reputation (blocklist).** "Attack on /login" = URI-specific. Match scope of response to scope of attack.
- Shield Advanced: $3K/month, 1-year commitment. Includes DRT, cost protection, WAF free.

---

### API Gateway Security
- 🧠 **API Gateway mTLS = custom domain name + S3 truststore (PEM file + object version).** Not ACM. Not Lambda authorizer. mTLS only works on custom domains, never on default execute-api endpoint.
- 🧠 **mTLS S3 bucket MUST have versioning enabled.** API Gateway requires an explicit object version reference. No versioning = domain creation fails at setup.
- 🧠 **mTLS troubleshooting: ALL fail = truststore/CA problem. ONE fails (same CA) = that partner's cert expired.** Same CA = truststore already trusts all certs from it. Individual cert issue only.
- 🧠 **mTLS revoke ONE cert = add CRL to S3 truststore.** Remove CA = blocks ALL partners using that CA.
- 🧠 **API Gateway authorizer types:** Cognito Authorizer (JWT tokens) vs Lambda Authorizer TOKEN (header value) vs Lambda Authorizer REQUEST (headers + query + context + IP). Use REQUEST type when you need to validate custom headers or IP addresses.
- 🧠 **TOKEN type receives ONLY the token string.** Cannot access other headers, query params, or source IP. "Validate IP or custom header" = REQUEST type always.
- 🧠 **API Gateway Resource Policy:** JSON policy on the API itself — restrict by IP, VPC, account. Evaluated BEFORE authorizers. "Block at API Gateway boundary" = resource policy.
- 🧠 **Resource Policy can't inspect header VALUES — only IP/VPC/account.** Header value inspection = Lambda authorizer (REQUEST type) or WAF regex.
- 🧠 **Private API = VPC endpoint only.** Resource policy restricts to `vpce-xxx`. Endpoint SG controls which clients can reach the endpoint (inbound 443).
- 🧠 **Private API timeout = Resource Policy rejection (not always network).** If endpoint SG and Lambda SG are fine, check Resource Policy `aws:SourceVpce` condition.
- 🧠 **Interface endpoint + private DNS ON = hijacks ALL DNS for that service in your VPC.** Good: call private APIs via normal URL. Bad: public APIs for that same service become unreachable from your VPC. Need both? Keep private DNS OFF, use vpce-specific URL for private API.

---

### Troubleshooting
- 🧠 **Timeout = network problem (SG, NACL, routing, missing endpoint). Access Denied = permissions problem (IAM, policy, key policy).** The error type tells you where to look.
- 🧠 **"Kill active connections immediately" = NACL (stateless, per-packet). SG rule removal won't kill tracked/established flows.** SG = stateful (conntrack keeps established sessions alive). NACL = stateless (every packet evaluated fresh).
- 🧠 **PASSIVE packet inspection (IDS, "without blocking") = VPC Traffic Mirroring (copy to NLB target). INLINE packet inspection (IPS, "block/drop") = GWLB or Network Firewall.** GWLB = traffic routed THROUGH appliance. Traffic Mirroring = COPY sent to appliance. Three-time exam trap.
- 🧠 **Interface endpoint = TWO SGs must cooperate.** Lambda SG needs outbound 443. Endpoint SG needs inbound 443. Miss either one = timeout.
- 🧠 **C2Activity finding = active IP connection. DNS Firewall useless (IP already known). Use Network Firewall DROP on C2 IP.** DNS FW only helps if attacker needs DNS resolution.
- 🧠 **DGA (Domain Generation Algorithm) = unpredictable domains, can't block-list. Flip to DNS Firewall ALLOW-LIST (block all except known-good).** DNS layer since attacker relies on DNS resolution.
- 🧠 **IoT ThingName = bound to certificate, not physical hardware.** Stolen cert = full impersonation. Mitigation = revoke cert in IoT Core.
- 🧠 **IoT Core cert revocation = instant.** Registry status checked at TLS handshake — no CRL propagation delay.
- 🧠 **Flow Log: inbound ACCEPT + outbound REJECT = always NACL.** SGs are stateful — accepted inbound = auto-allowed return. NACLs are stateless — need explicit outbound ephemeral port rule.
- 🧠 **VPC Flow Logs = intra-VPC (ENI-level, sees same-subnet traffic). TGW Flow Logs = cross-VPC (sees traffic traversing the transit gateway hub).** Each log sees traffic at ITS layer only.

---

## D1: Detection (16%)

---

### Service Selection
- GuardDuty = active threats NOW (C2, crypto mining, exfil). Inspector = known CVEs (software vulns). Macie = sensitive data in S3.
- Security Hub = aggregate findings + compliance dashboards (wraps Config rules). Requires Config enabled.
- Detective = investigate AFTER detection (root cause, blast radius, timeline).
- 🧠 **CloudTrail = raw API log. Detective = the investigator who reads the logs FOR you.** "Who did what" = CloudTrail. "Show me the full picture / timeline / scope" = Detective.
- 🧠 **"Track config changes over time" = AWS Config (configuration history). "Who made the API call" = CloudTrail.** Config shows WHAT changed. CloudTrail shows WHO changed it.
- CloudTrail Lake = fast + dashboards + managed + near real-time. S3+Athena = cheap + DIY + unlimited retention.
- Firewall Manager = DEPLOY rules across org. Security Hub = VIEW findings across org. Different verbs.
- "In progress" / "happening now" = active threat = GuardDuty. "What data exists?" = Macie. "What vulns exist?" = Inspector.
- "Detect C2" = GuardDuty. "Block C2 domains" = DNS Firewall. Detect ≠ prevent.
- 🧠 **"Detect [bad thing] with zero custom code" = always GuardDuty.** It has built-in threat intel for Tor (TorIPCaller), malicious IPs, crypto mining, C2, DNS exfil. No setup needed.
- 🧠 **DNS Firewall ALERT ≠ "generate a finding."** ALERT logs but doesn't produce security findings. GuardDuty reads DNS logs natively and generates findings with threat intel. "Detect + finding" = GuardDuty.
- 🧠 **"Detect external decryption" = GuardDuty. "Prevent external decryption" = key policy condition.** The verb tells you the service.
- "Unused permissions" / "overly permissive" = IAM Access Analyzer. "Credentials being misused" = GuardDuty.
- 🧠 **"Unused PERMISSIONS (per-action)" = Access Analyzer unused access. "Unused ROLE (last assumed)" = Config/credential report.** Different granularity.
- 🧠 **Access Analyzer unused access + policy generation = find bloat + auto-generate replacement.** Two features, one service, designed together.
- 🧠 **Access Analyzer + GuardDuty can BOTH fire on the same resource.** AA = "who CAN access?" (static policy analysis). GD = "who IS accessing abnormally?" (dynamic behavior). Independent services.
- 🧠 **"Detect [bad thing] with zero custom code" = always GuardDuty.** It has built-in threat intel for Tor (TorIPCaller), malicious IPs, crypto mining, C2, DNS exfil. No setup needed.
- 🧠 **"Detect API call fast + least overhead" + org trail exists = EventBridge rule in management account.** Near real-time, one rule. Config is slower + heavier — use for remediation, not pure fast detection.
- 🧠 **"Detect specific API call fast" = EventBridge on CloudTrail. "Detect malicious behavior" = GuardDuty.** GuardDuty doesn't alert on policy changes or blocked attempts.

---

### GuardDuty Operational
- 🧠 **GuardDuty is REGIONAL.** Must enable in every region where workloads run. No findings from a region where it's not enabled.
- 🧠 **Delegated admin ≠ auto-enabled everywhere.** Delegated admin = WHO manages. Regional = WHERE it runs. Independent axes. Must enable per-region THEN auto-enable handles future accounts in THAT region.
- 🧠 **GuardDuty custom threat list → finding type has `.Custom` suffix.** Built-in intel = standard types. Your list = `MaliciousIPCaller.Custom`.
- 🧠 **Global services (IAM, STS, CloudFront) deliver events to us-east-1 ONLY.** EventBridge rules for `CreateUser` etc must be in us-east-1.
- 🧠 **Security Hub = dashboard (view findings). Config = remediation engine (fix resources).** SH wraps Config rules but doesn't own the fix. Auto-remediation = Config rule + SSM.
- 🧠 **GuardDuty reads VPC Flow Logs + DNS logs via internal feed — you DON'T need to enable them yourself.** Your VPC Flow Logs are for YOUR queries (Insights, Athena). GuardDuty has its own tap.
- 🧠 **"Unusual IP" / "never-seen location" = active threat = GuardDuty.** NOT Access Analyzer (that's permission audit, not real-time threats).
- 🧠 **"Zero findings despite active workloads + GuardDuty confirmed enabled" = suppression rule archiving findings.** GuardDuty WILL generate findings on production — if you see none, something is hiding them.
- 🧠 **GuardDuty doesn't fire on BLOCKED/DENIED attempts.** It detects successful anomalous access. If RCP/SCP blocks the request, no successful access occurs = no finding. Access Analyzer fires on policy (static) regardless.
- 🧠 **DNS query = Impact (always). Active TCP: mining pool = CryptoCurrency, C2 server = Trojan.** The destination type determines the second finding's ThreatPurpose.
- 🧠 **DNS query = Impact (always). Active TCP: mining pool = CryptoCurrency, C2 server = Trojan.** The destination type determines the second finding's ThreatPurpose.
- 🧠 **GuardDuty EKS: Audit Log Monitoring = agentless. Runtime Monitoring = needs agent (DaemonSet).** Runtime detects process-level (crypto miners, shells). No agent = no runtime findings.
- 🧠 **GuardDuty finding `!suffix` = data source used for detection.** `!DNS` = DNS logs. `!VPCFlowLogs` = Flow Logs. `!CloudTrail` = CloudTrail. Suffix = HOW it was detected, not WHAT the attack does.
- 🧠 **GuardDuty Extended Threat Detection (Dec 2024, likely not testable yet):** correlates multiple findings into attack sequences in the GD console. If tested, answer = "Extended Threat Detection." Otherwise "correlate/investigate" = Detective.
- 🧠 **GuardDuty Trusted IP list = PUBLIC IPs only.** Private IPs cannot be added. Need EIPs first. `GuardDutyExcluded` tag = Malware Protection scanning ONLY.
- 🧠 **Trusted IP list = nuclear (blinds GD to ALL findings from that IP). Suppression rule = surgical (archives ONE finding type from that IP).** Trusted IP list is NOT a filter field inside suppression rules — it's a separate mechanism.

---

### Log Sources
- 🧠 **ELB access logs → S3 ONLY (never CW Logs directly).** Search = Athena. Metrics = Athena query → PutMetricData to CloudWatch. CW metric filters only work on CW Logs log groups, not S3 files.
- **"Which domain was queried?" = Resolver Query Logs.** VPC Flow Logs only show IP:port — domain name is gone after DNS resolves.
- GuardDuty reads BOTH: DNS logs (domain) + VPC Flow Logs (traffic volume/destination). That's why it catches C2 that other services miss.
- 🧠 **Log source SCOPE (what each sees):**

---

### Log Source Scope Table

| Log Source | Sees What | Key Exam Signal |
|---|---|---|
| **VPC Flow Logs** | IP/port per ENI (intra-subnet, intra-VPC) | "lateral movement", "same subnet" |
| **TGW Flow Logs** | Traffic crossing Transit Gateway (VPC↔VPC) | "hub-and-spoke", "cross-VPC" |
| **ELB Access Logs** | HTTP details (URL, status, latency, cipher) | "request patterns", "HTTP" |
| **R53 DNS Query Logging** | Queries TO your public zone (external) | "public DNS queries" |
| **R53 Resolver Query Logging** | Queries FROM your VPC (internal lookups) | "C2 domains", "VPC DNS" |
| **CloudTrail** | AWS API calls | "who changed", "API call" |

---

### Log Delivery Destinations

| Log Source | S3 | CW Logs | Firehose | EventBridge |
|---|---|---|---|---|
| **VPC Flow Logs** | ✅ | ✅ | ✅ | ❌ |
| **ELB Access Logs** | ✅ | ❌ | ❌ | ❌ |
| **CloudTrail** | ✅ | ✅ | ❌ | ✅ (automatic) |
| **WAF Logs** | ✅ | ✅ | ✅ | ❌ |
| **R53 DNS query logging (public)** | ❌ | ✅ only | ❌ | ❌ |
| **R53 Resolver query logging (VPC)** | ✅ | ✅ | ✅ | ❌ |
| **S3 Server Access Logs** | ✅ | ❌ | ❌ | ❌ |
| **CloudFront Access Logs** | ✅ | ❌ | ❌ | ❌ |

---

### Log Delivery Mechanisms
  - VPC Flow Logs → S3/CW Logs/Firehose = **IAM role** (all three)
  - CloudTrail → S3 = **bucket policy**, CW Logs = **IAM role**, EventBridge = automatic
  - Route 53 Resolver → CW Logs = **log group resource policy**, S3 = bucket policy, Firehose = IAM role
  - WAF Logs → CW Logs = **log group resource policy**, S3 = bucket policy, Firehose = IAM role
- 🧠 **VPC Flow Logs = only service using IAM role for ALL delivery targets.**
- 🧠 **CW Logs as destination = usually log group resource policy (service principal).** Exception: VPC Flow Logs uses IAM role for everything.
- 🧠 **"Old Four" that need `s3:GetBucketAcl` for S3 delivery:** CloudTrail, Config, ELB, S3 server access logging. Legacy ACL ownership check. Modern services (GuardDuty, Inspector, Macie, Security Lake) use bucket policy with service principal instead.

---

### CloudTrail / Logging
- CloudTrail Lake = its own managed data store, SQL, near real-time, dashboards. NOT S3, NOT OCSF.
- 🧠 **CloudTrail Lake no backfill — events before EDS creation are never ingested.** "Zero results" + old data = no backfill, not ingestion delay.
- 🧠 **Org trail = management account only.** Member accounts can see it but cannot modify, stop, or delete it. API call fails.
- 🧠 **State Manager: new target = immediate first run.** `rate(1hr)` = how often to RE-RUN on known targets. New matching instance detected = runs within minutes (doesn't wait for next rate cycle).
- 🧠 **Security Hub = dashboard (view findings). Config = remediation engine (fix resources).** SH wraps Config rules but doesn't own the fix. Auto-remediation = Config rule + SSM.
- 🧠 **Security Hub is REGIONAL (not global).** Cross-region aggregation = designate one region. Does NOT write to S3. Trusted Advisor does NOT integrate with SH.
- 🧠 **Trusted Advisor = periodic checklist (no real-time, no automation, no SH integration).** "Immediately" or "as soon as" = eliminate TA.
- 🧠 **S3 event notifications can't filter by ACL/permission values.** Only prefix, suffix, event type. Need CloudTrail data events + EventBridge for ACL-based detection.
- 🧠 **"Object-level logging" = CloudTrail data events for S3.** Same feature, different name. Must enable explicitly.
- Security Lake = YOUR S3 bucket, OCSF format, normalizes ALL log sources (CloudTrail + VPC Flow + WAF + GuardDuty + third-party).
- CloudWatch Logs Insights = query app logs / VPC Flow Logs / Lambda logs. Custom syntax (not SQL). Already-ingested data.
- "Fast API call investigation" → CloudTrail Lake. "Normalize all logs into one schema" → Security Lake. "Query app/VPC logs" → CloudWatch Logs Insights.
- 🧠 **Three "lakes": CloudTrail Lake (API calls, SQL, managed store) vs Security Lake (all logs, OCSF, your S3) vs CloudWatch Logs Insights (app logs, custom syntax, CloudWatch store). No "CloudWatch Lake" exists.**
- 🧠 **CloudWatch Logs Insights = open-ended queries on data already in CW. Detective = investigate from a specific finding/entity.** "Top talkers" = Insights. "What else did this IP do?" = Detective.
- 🧠 **`/var/log/awslogs.log` = runtime errors (logs stopped flowing). `/var/log/awslogs-agent-setup.log` = installation errors only.** "Was working, now stopped" = check runtime log.
- 🧠 **CloudTrail management events: Write-only trail = ConsoleLogin (Read event) won't trigger EventBridge.** Must be "All" or "Read-only/Read+Write" for login events. Event History always shows all events regardless.
- 🧠 **CW metric filter: metric value must be 1 (not 0).** Value=0 means every match publishes nothing — alarm threshold >= 1 never fires. Common troubleshooting trap.
- 🧠 **StopLogging kills its own CW Logs delivery.** Metric filter on the log group can never detect StopLogging — use EventBridge instead (receives from CloudTrail's management event stream directly).
- 🧠 **CloudTrail data events (GetObject, PutObject, Decrypt, Invoke) are NOT logged by default.** Only management events are. If a question says "CloudTrail recorded X" where X is a data operation — check if data events are explicitly enabled. Not stated = not logged.

---

## D2: Incident Response (14%)
- IR sequence: Acquire (metadata + EBS snapshot + no-reboot AMI for memory) → Isolate (swap SG to deny-all) → Investigate (Detective, forensics account) → Report (SNS, S3). NEVER terminate first.
- 🧠 **ASG = detach/suspend FIRST (protect evidence from auto-termination), THEN acquire → isolate.** No ASG = acquire before isolate directly.
- 🧠 **ACQUIRE before ISOLATE.** Isolation (deny-all SG) can block SSM needed for memory capture. Volatile memory must be captured FIRST. AWS docs: "capture memory before isolation or shutdown."
- 🧠 **"Validate findings" = first step before full IR (Task 2.2.3, new in C03).** Assess scope, check false positives, confirm severity. Exam keyword is "validate" or "triage", not "evaluate".
- Automated Forensics Orchestrator = Step Functions pipeline that auto-isolates + snapshots EC2 on GuardDuty finding.
- Test IR plans with **Fault Injection Service** (simulate failures). Validate resilience with **Resilience Hub**.
- Validate findings BEFORE full IR — assess scope, check false positives, correlate in Security Hub, investigate in Detective.
- 🧠 **"Assess RTO/RPO for auditors" = Resilience Hub (analyze architecture). "Test IR plan by breaking things" = FIS (inject chaos). "Shift traffic from bad AZ" = ARC zonal shift (recover).** Three verbs: assess → test → recover.
- 🧠 **`CreateSampleFindings` = test GuardDuty → EventBridge → Step Functions pipeline end-to-end without a real incident.** FIS injects infra failures (AZ/network), NOT security findings.
- Revoke compromised sessions: inline Deny with `aws:TokenIssueTime` < timestamp on the role.

---

- 🧠 **OutsideAWS = TokenIssueTime (creds used externally, instance gets fresh ones). InsideAWS = deny-all SG on attacker's instance (TokenIssueTime would break both instances sharing same role).**
- 🧠 **OutsideAWS + SHARED ROLE = never TokenIssueTime (kills all instances). Use deny-all SG or NACL on compromised only.**
- 🧠 **OutsideAWS + can't stop instance: TokenIssueTime (stop attacker) + no-reboot AMI (if memory requested) + EBS snapshot (disk) + IMDSv2 hop limit 1 (prevent future SSRF). Deny-all SG kills legitimate traffic — wrong choice if API must stay up.**
- 🧠 **C2Activity + API must stay up: Network Firewall DROP on C2 IP (surgical). Deny-all SG = nuclear (kills all traffic). "Preserve evidence" in same question = MUST include EBS snapshot.**
- 🧠 **Credential leak IR (keys on GitHub): Deactivate exposed keys + attach inline Deny-all to user (covers second key/console/sessions).** Contain ALL access paths BEFORE investigating. Detective comes after containment.
- 🧠 **Compromised ROLE = TokenIssueTime (only temp creds exist). Compromised IAM USER = Deny * on user (keys + console + sessions = persistent creds).** TokenIssueTime only kills STS tokens, not access keys or console passwords.

---

- 🧠 **S3 Access Grants scope access by prefix (location). Overlapping prefixes = unintended cross-department access.** This is the #1 operational misconfiguration — not IAM bypass.
- 🧠 **"Windows boot issue + collect memory dump" = EC2Rescue for Windows.** SSM agent requires running OS — can't help if instance won't boot.
- 🧠 **Session Manager logging = built-in "upload session logs" (records keystrokes/commands).** CloudWatch Agent = OS/app logs. Different things. "Record session activity" = Session Manager preferences.
- 🧠 **Route 53 TWO logging features:** DNS query logging = public hosted zone queries (CW Logs only). Resolver query logging = VPC outbound queries (CW Logs, S3, Firehose). "Public DNS queries" = DNS query logging.
- 🧠 **JWT decode ≠ JWT verify.** Decode = read payload (no tamper detection). Verify = check cryptographic signature (aws-jwt-verify). "Most secure" = always verify.
- 🧠 **"AWS managed key" = NEVER the answer when question mentions control, policy, expiration, rotation config, or grants.** AWS managed = autopilot with no steering wheel.
- 🧠 **Config proactive evaluation = evaluates resources BEFORE CloudFormation creates them.** "Before provisioned" = proactive. "After exists" = detective. Config supports both modes.
- 🧠 **EFS encryption = creation-time ONLY.** Cannot enable on existing file system. Must create new EFS + migrate.
- 🧠 **DNSSEC "broken trust chain" = DS record missing in parent zone.** Always.
- 🧠 **Network Firewall = inline IDS/IPS (inspect + block). Traffic Mirroring = passive copy (doesn't block).** "IDS" in question = Network Firewall.
- 🧠 **ALB + HIDS + PFS: send encrypted traffic END-TO-END to EC2 (ECDHE + PFS).** Don't decrypt at ALB if HIDS needs to see traffic on instance.

---

## D6: Governance (14%)
- Management account exempt from BOTH SCPs and RCPs. Don't put workloads there.
- Control Tower = automated landing zone + guardrails (SCPs/RCPs for preventive, Config for detective).
- 🧠 **Control Tower prerequisites: STS enabled in all regions + IAM Identity Center enabled + DISABLE existing trusted access for Config/CloudTrail (CT manages these itself).** Existing trusted access = conflict.
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
- 🧠 **Config stopped = detection engine dead.** Rules can't fire, remediation can't trigger. Not a circular dependency — the engine itself is off.
- 🧠 **SCP future only + FM auto-remediates existing.** New account joins OU: SCP blocks FUTURE API calls. FM attaches to EXISTING resources immediately.
- 🧠 **Org conformance pack auto-deploys rules + remediation CONFIG, but NOT the execution role.** New account joins → role missing → remediation silently fails. Fix: StackSets deploys the role.
- 🧠 **Terraform = direct API (not CF).** Terraform AWS provider calls APIs directly — Config proactive (CF service-level) is blind to it.
- 🧠 **Control Tower guardrails: Preventive = SCP (block API). Detective = Config (detect after). Proactive = CF Hook (validate template before deploy).**
- 🧠 **"Validate template content" = Proactive guardrail (CF Hook). "Block API call" = SCP.** SCP can't see what's inside a CloudFormation template.
- 🧠 **SCP can't inspect API payload content (e.g., bucket policy JSON).** To prevent the consequence of `Principal:*`, use RCP (blocks external access) + EventBridge (detects the call).
- 🧠 **Every security service supports delegated admin.** GuardDuty, Security Hub, FM, Config, Audit Manager, Macie, Inspector, Detective, Security Lake, Access Analyzer.
- 🧠 **"Detect specific API call fast" = EventBridge on CloudTrail. "Detect malicious behavior" = GuardDuty.** GuardDuty doesn't alert on policy changes.
- 🧠 **If the service has delegated admin + auto-enable → use native, not StackSets.** GuardDuty, Inspector, Security Hub, Macie, Detective, Config, Access Analyzer.
- 🧠 **No single governance service does everything.** CT doesn't share (RAM), deploy WAF (FM), or remediate (Config).
- 🧠 **Well-Architected Tool = architecture review + improvement plan + milestones (snapshot + compare over time).** No Config/SH integration for auto-resolution.
- 🧠 **cfn-guard = validate template content in CI/CD (shift-left, cheapest). Config proactive = validate at CF service level (heavier). CF Hook = same as Config proactive but Control Tower managed.** All three = "before deploy" but different weight.
- 🧠 **cfn-guard = bypassable (CI/CD only, Console deploy skips it). Config proactive = service-level (can't bypass, catches ALL CF deploys including Console).** "Developer bypasses pipeline" = Config proactive catches, cfn-guard misses.
- 🧠 **CF Hook = CF service-level (same layer as Config proactive).** Both intercept ANY CF deploy (CLI, Console, SDK). cfn-guard = pipeline only.
- 🧠 **"ALL CF deploys + BEFORE creation + least code" = Config proactive with managed rules.** SCP can't see template content. cfn-guard is bypassable.
- 🧠 **Declarative policy = "this state is impossible to violate" (EC2/VPC/EBS only).** SCP = "this API call is blocked." Different layers. "Regardless of which API" = declarative.
- 🧠 **Proactive enforcement = don't downgrade for convenience.** If Config proactive blocks it, the answer is "fix the template" — never "switch to detective so dev can fix later."
- 🧠 **Service Catalog = deploy only, no post-provisioning monitoring.** SC provisions resources but never detects drift/changes after. "Post-deploy compliance" = Config + SSM.
- 🧠 **Stack Policy = protect resources inside stack (preventive, blocks CF updates). Termination protection = prevent stack deletion.** Drift detection = detective only (reports manual changes, doesn't prevent). Change sets = preview before deploy.
- 🧠 **Stack Policy = DEFAULT DENY ALL.** Unlike IAM, if no Allow statement exists, NOTHING passes. Must explicitly Allow actions. Explicit Deny always wins (same as IAM).
- 🧠 **Config proactive fires BEFORE SCP in CF deploys.** Proactive rejects template → CF never calls API → SCP never evaluates. Earliest CF-level gate.
- 🧠 **cfn-guard can't resolve intrinsics (!Ref, !Sub, Fn::If).** Sees raw template text only. Parameter overrides at deploy time bypass cfn-guard.
- 🧠 **Proactive rejection = CloudTrail failed API.** Config proactive rejects → CF logs failed CreateStack in CloudTrail.
- 🧠 **StackSets auto-deploy = new accounts.** Service-managed + auto-deploy = auto-deploys to new accounts joining OU. Different from auto-remediation (which StackSets NEVER does).
- 🧠 **CT supports custom controls.** Custom SCP = preventive. Custom Config rule = detective. Custom CF Hook = proactive. NOT limited to AWS-managed.
- 🧠 **RAM attachment = member-owned.** RAM shares parent resource (TGW). Attachments created BY members belong to members. Members can delete their own.
- 🧠 **Standards evaluation latency at scale.** Enabling SH standards across 200 accounts = 2-24 hours for findings (Config evaluation at scale). Not minutes.
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
- 🧠 **IAM Credential Report cached 4 hours.** Recent changes won't appear until cache expires. Not a Config frequency issue.
- 🧠 **SCP block root (containment vs hygiene):** Deactivate key = one path (programmatic). SCP deny root = ALL paths (API + Console). "If compromised" = SCP.

---

## GenAI / ML / New Services (SCS-C03 additions)

- 🧠 **Bedrock Guardrails = LLM content filtering (prompt injection, PII, topics). WAF = HTTP filtering. Different layers.**
- 🧠 **`bedrock:ApplyGuardrail` = standalone API.** Filter ANY text (even non-AWS LLMs) without InvokeModel.
- 🧠 **Bedrock IAM enforcement: condition `bedrock:GuardrailIdentifier` = mandatory guardrail per call.** Missing condition = InvokeModel denied.
- 🧠 **"Block model org-wide" = SCP deny `bedrock:InvokeModel` on model ARN.** Simplified access doesn't override IAM/SCP blocks.
- 🧠 **Two Bedrock VPC endpoints: `bedrock` (management) + `bedrock-runtime` (inference).** Both Interface type.
- 🧠 **Bedrock data privacy: your data NOT used for training (opted out by default).** No action needed.
- 🧠 **Q Business = enterprise docs (requires Identity Center + ACL crawling). Q Developer = code security (IDE + SAST).**
- 🧠 **Q Business ACLs can't be disabled once enabled.** Automatic document-level security from source connectors.
- 🧠 **CodeGuru Security = SAST (code before deploy). Inspector = CVE scanning (running workloads after deploy).**
- 🧠 **CodeGuru detects: OWASP Top 10, CWE Top 25, hardcoded secrets, insecure AWS SDK usage.**
- 🧠 **FSx for Lustre = ALWAYS encrypted (XTS-AES-256), symmetric KMS only, VPC-only.**
- 🧠 **FSx linked to SSE-KMS S3 bucket: key policy must grant `fsx.amazonaws.com`.** Same pattern as CloudFront OAC.
- 🧠 **FSx Scratch = no backups, no replication (temp). Persistent = backups + within-AZ replication.**

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
