# Dojo Practice Exam Set 3 — Full Review

> Date: 2026-06-19
> Score: 31/65 (48%)
> Purpose: Capture ALL wrong questions for targeted gap analysis and re-drill.

---

## Questions for Review

### Q55 — S3 Data Exfiltration via Proxy (Select TWO)

**Scenario:** EC2 in private subnet, proxy in public subnet. Rogue employee exfils to external S3 bucket using own AWS creds. Mitigate without affecting other workloads.

**Your Answer:** C + D (NACL on app subnet + proxy block)
**Correct:** D + E (proxy block + VPC Gateway endpoint with restrictive endpoint policy)

**Key concept:** Gateway endpoint policy = allowlist for ALL S3 traffic from VPC. If destination bucket not in policy = denied at your network boundary. Attacker's creds irrelevant.

---

### Q64 — Config Delivery to S3 Failure (Select TWO)

**Scenario:** Config error "unable to write to bucket." Fix?

**Your Answer:** A + C (trust relationship + bucket policy)
**Correct:** C + E (bucket policy for config.amazonaws.com + role needs s3:GetBucketAcl + s3:PutObject*)

**Key concept:** "Unable to write" = role already assumed (trust is fine). Fix = bucket policy + GetBucketAcl + PutObject. Same pattern as S3 server access logging.

---

### Q65 — GuardDuty Email Notifications (medium+high)

**Scenario:** Org-wide GuardDuty, send email for medium+high findings. Most operationally efficient.

**Your Answer:** (TBD — paste your answer)
**Correct:** GuardDuty delegated admin → EventBridge rule (severity filter) → SNS → email

**Key concept:** GuardDuty publishes to EventBridge natively. No Lambda needed. Delegated admin sees all org findings.

---

<!-- TEMPLATE: Add more questions below as you review them -->

### Q2 — CloudFront SPA Auth (Select TWO)

**Scenario:** CloudFront serves SPA from S3. Cognito auth. Unsigned users can download SPA source code. Prevent this.

**Your Answer:** A + D (OAC + Cognito hosted UI)
**Correct:** C + D (Lambda@Edge viewer-request + Cognito hosted UI)

**Key concept:** OAC locks S3 direct access, NOT CloudFront-level auth. Lambda@Edge viewer-request = enforce auth at CloudFront. OAC doesn't prevent unauthenticated CloudFront access.

**Rule:** OAC = "prevent S3 bypass." Lambda@Edge viewer-request = "enforce auth at CloudFront level." Different problems.

---

### Q3 — ECR Centralized Scanning + Cross-Account Access

**Scenario:** Fargate app in multiple accounts (dev/qa/uat/prod). Container images must be scanned for severe vulnerabilities + secure access controls allowing only specific accounts/roles.

**Your Answer:** C (repository policies + ABAC)
**Correct:** A (repository policies + identity-based policies)

**Key concept:** ECR cross-account access = repository policies + identity-based policies. ABAC is not the standard ECR pattern. "Least operational overhead" = simplest policy mechanism.

---


### Q4 — GuardDuty S3 Finding Type (bucket accessible over internet)

**Scenario:** Detect whether a private bucket becomes accessible over the internet using GuardDuty S3 Protection.

**Your Answer:** C (Policy:S3/BucketPublicAccessGranted)
**Correct:** A (Policy:S3/BucketAnonymousAccessGranted)

**Key concept:** "Accessible over the internet" = anonymous (unauthenticated) access = BucketAnonymousAccessGranted. "PublicAccessGranted" = authenticated AWS users outside your account. Anonymous = internet (no creds needed). Public = any AWS account (still needs creds).

**Rule:** Internet = anonymous (no credentials). Public = any authenticated AWS principal.

---

### Q5 — CRR SSE-KMS Replication Failure (Select THREE)

**Scenario:** CRR same account, source SSE-KMS in ap-southeast-1, dest uses new CMK in ap-northeast-2. Unencrypted objects replicate fine, encrypted ones fail.

**Your Answer:** A + C + D (Encrypt dest + GetObjectVersionForReplication + GetObjectVersion)
**Correct:** A + B + C (Encrypt dest key + Decrypt source key + GetObjectVersionForReplication)

**Key concept:** CRR with SSE-KMS needs THREE things on the replication role:
1. `kms:Decrypt` on SOURCE key (read encrypted source objects)
2. `kms:Encrypt` on DEST key (write encrypted to destination) — Dojo uses Encrypt here, real AWS = GenerateDataKey
3. `s3:GetObjectVersionForReplication` (NOT GetObjectVersion — replication-specific permission for encrypted objects)

**Your error:** Missed `kms:Decrypt` on source key (B). Picked both C and D — only C (replication-specific) is needed.

---

### Q6 — Verify SGs and NACLs Work as Expected

**Scenario:** Hundreds of EC2 instances. Verify SGs and NACLs are properly configured and work as expected.

**Your Answer:** C (Config rule for each SG/NACL)
**Correct:** B (VPC Flow Logs → S3 → Athena)

**Key concept:** "Verify they WORK as expected" = observe actual traffic behavior. VPC Flow Logs show ACCEPT/REJECT per flow = proves whether SGs/NACLs are blocking/allowing correctly. Config checks configuration (what IS set), not behavior (what HAPPENS). "Work as expected" = runtime validation = Flow Logs.

**Rule:** "Are rules configured correctly?" = Config. "Are rules working as expected?" = VPC Flow Logs (observe actual traffic).

---

### Q7 — Org CloudTrail for All Accounts ✅

**Scenario:** Member accounts not sending CloudTrail logs to centralized bucket. Guarantee all existing and future accounts have at least one trail.

**Your Answer:** B (Update trail in master to enable logging for all members, apply to org)
**Correct:** B ✅

**Key concept:** Organization trail in management account = auto-applies to all members (existing + future). No per-account setup needed.

---

### Q8 — KMS Key Rotation Notification ✅

**Scenario:** Confirm CMK rotations are happening. Email notification immediately on successful rotation.

**Your Answer:** D (EventBridge rule for KMS CMK Rotation event → SNS)
**Correct:** D ✅

**Key concept:** KMS emits rotation events to EventBridge natively. EventBridge → SNS = most operationally efficient (no Lambda, no polling).

---

### Q9 — Config Proactive vs Detective Evaluation

**Scenario:** Detect and consolidate findings + ensure NO public IPs assigned BEFORE VPC subnets are provisioned.

**Your Answer:** B (Config managed rules with detective evaluation + Security Hub)
**Correct:** D (Config managed rules with proactive evaluation + Security Hub)

**Key concept:** "Before provisioned" = PROACTIVE evaluation (evaluates resources in CloudFormation BEFORE deployment). Detective = evaluates AFTER resource exists. Proactive = shift-left validation at deploy time (like CF Hooks/Guard).

**Rule:** "Before resource is created" = proactive. "After resource exists" = detective. Config supports both modes.

---

### Q10 — Post-Compromise Security Improvement (Select TWO)

**Scenario:** EC2 compromised. Improve security of AWS cloud resources.

**Your Answer:** A + B (State Manager remote access + Security Hub)
**Correct:** B + C (Security Hub for unintended network access + VPC Flow Logs to monitor traffic)

**Key concept:** After compromise, improve visibility: Security Hub (check network accessibility misconfigs) + VPC Flow Logs (monitor actual traffic). State Manager is for remote access (Session Manager does that, not State Manager) — and it's a management tool, not a security improvement response.

**Your error:** Confused State Manager (desired-state enforcement) with Session Manager (remote access). Also VPC Flow Logs = essential post-compromise visibility.

---

### Q11 — KMS Key Material Auto-Expire After 30 Days

**Scenario:** Encrypt EBS data. Key material must expire automatically after 30 days.

**Your Answer:** A (AWS Managed KMS key)
**Correct:** C (Customer-managed KMS key with imported key material)

**Key concept:** Only IMPORTED key material supports expiration dates. You set an expiry when importing — after that date, the material is automatically deleted (key becomes unusable until re-import). AWS-generated keys (managed or customer-managed) NEVER expire.

**Rule:** "Key material must expire" = imported key material (only option with expiration). AWS managed keys can't be configured at all.

---

### Q12 — Config + Security Hub CIS Benchmark ✅

**Scenario:** Continuous security checks on resource configs + CIS AWS Foundations Benchmark.

**Your Answer:** B (Config all regions + Security Hub with CIS benchmark)
**Correct:** B ✅

**Key concept:** Security Hub = CIS benchmark standards built-in. Config required underneath (SH wraps Config rules). Inspector = CVE scanning, not CIS benchmarks.

---

### Q13 — FIPS 140-2 Level 3 + S3/EBS Integration ✅

**Scenario:** Encrypt data in S3 and EBS. FIPS 140-2 Level 3 HSM required.

**Your Answer:** A (Customer-managed KMS key backed by CloudHSM custom key store)
**Correct:** A ✅

**Key concept:** CloudHSM = FIPS 140-2 Level 3. Custom key store = integrates with KMS API = native S3/EBS support. CloudHSM directly (B) = no native S3/EBS integration. KMS default = FIPS 140-3 but multi-tenant.

---

### Q14 — On-Prem AD + Organizations + Identity Center ✅

**Scenario:** On-prem AD, Organizations, Direct Connect. Restrict access by group membership. Centralized identity management.

**Your Answer:** A (Identity Center + SAML 2.0 + SCIM + ABAC)
**Correct:** A ✅

**Key concept:** Identity Center = workforce SSO to AWS accounts. SAML 2.0 connects to on-prem AD. SCIM auto-syncs users/groups. ABAC = group-based access. Cognito = customer apps (wrong). Managed AD = overkill when Identity Center suffices.

---

### Q15 — EFS Encryption (Cannot Enable After Creation)

**Scenario:** EFS file system is unencrypted. Must encrypt with regularly rotated key for SOX compliance.

**Your Answer:** D (Create CMK + enable encryption on EXISTING EFS)
**Correct:** A (Create CMK + deploy NEW EFS with encryption enabled)

**Key concept:** EFS encryption can ONLY be enabled at creation time. You cannot enable encryption on an existing unencrypted EFS file system. Must create a NEW encrypted EFS and migrate data.

**Rule:** EFS encryption = creation-time only (like S3 Object Lock — must be set at bucket creation). Cannot be toggled on existing file system.

---

### Q16 — SCP Deny KMS Modification in Production ✅

**Scenario:** Organizations. Prohibit IAM users in production accounts from modifying/updating KMS keys.

**Your Answer:** D (SCP deny KMS actions, attach to production OU)
**Correct:** D ✅

**Key concept:** SCP on production OU = org-wide prevention for all principals in those accounts. IAM policy (A) = per-user, doesn't scale. Control Tower (B) = uses SCPs underneath but answer is the mechanism. Declarative policies (C) = EC2/VPC state enforcement, not KMS actions.

---

### Q17 — Cognito User Pool Groups for Team Permissions ✅

**Scenario:** Web app with Delivery (write), Finance (read), Admin teams. Grant distinct permissions per team.

**Your Answer:** A (Cognito User Pool Groups)
**Correct:** A ✅

**Key concept:** User Pool Groups = assign users to groups, each group maps to an IAM role with different permissions. Identity Pool = vends AWS creds (different purpose). Cognito Sync = deprecated data sync.

---

### Q18 — IPv6 Outbound Only (Egress-Only Internet Gateway)

**Scenario:** EC2 needs IPv6 outbound internet (updates) but must block inbound connections from external apps.

**Your Answer:** A (NAT gateway + private subnet)
**Correct:** B (Egress-only internet gateway + private subnet)

**Key concept:** NAT Gateway = IPv4 ONLY (translates private IPv4 to public IPv4). For IPv6 outbound-only, use EGRESS-ONLY Internet Gateway — allows outbound IPv6 but blocks inbound. IPv6 doesn't need NAT (all addresses are public), so the egress-only IGW provides the one-way gate.

**Rule:** IPv4 outbound-only = NAT Gateway. IPv6 outbound-only = Egress-Only Internet Gateway.

---

### Q19 — Threat Detection for AWS Accounts ✅

**Scenario:** Continuous monitoring for malicious activity and unauthorized behavior.

**Your Answer:** A (GuardDuty)
**Correct:** A ✅

---

### Q20 (Threat Detection/IR) — Compromised IAM Access Key in Lambda

**Scenario:** Compromised access key in Lambda. Key has overly permissive perms. Attacker exploiting Lambda Function URL for crypto mining. Must: neutralize key, prevent future, follow best practices.

**Your Answer:** A (Deactivate key, generate new key, apply to Lambda, least-privilege)
**Correct:** B (DELETE key, STOP using access keys entirely, create IAM ROLE for Lambda, assign role, respond to abuse report)

**Key concept:** Best practice = Lambda should use IAM ROLES, never embedded access keys. "Prevent future similar incidents" = stop using access keys for Lambda entirely. Deactivate + new key (A) perpetuates the anti-pattern. DELETE + switch to role (B) = proper remediation.

**Rule:** Lambda should NEVER use embedded access keys. Always use execution roles. "Implement best practices" = switch from key to role.

---

### Q21 (Governance) — EC2 Public IP Communication Between Instances

**Scenario:** Two EC2 instances in same VPC, different AZs. Can communicate via private IPs but NOT via public IPs.

**Your Answer:** C (SG inbound rule referencing instance ID)
**Correct:** D (SG inbound rule allowing the other instance's PUBLIC IP)

**Key concept:** When traffic goes via public IPs, it exits and re-enters the VPC through the Internet Gateway. At that point, the source is the PUBLIC IP, not the instance ID or private IP. Security groups must reference the PUBLIC IP. Instance ID references only work for private IP traffic within the VPC.

**Rule:** Public IP traffic between EC2 instances = traverses IGW = source appears as public IP. SG must allow the public IP explicitly.

---

### Q22 (Governance) — Post-Compromise Security Improvement (same as Q10)

**Scenario:** EC2 compromised. Improve security. (Select TWO)

**Your Answer:** B + C (Security Hub + State Manager remote access)
**Correct:** A + B (VPC Flow Logs + Security Hub)

**Key concept:** Same as Q10. "State Manager" ≠ "Session Manager." State Manager = desired-state config enforcement. Session Manager = remote access. The option says "State Manager to access remotely" — that's wrong terminology/capability. VPC Flow Logs = essential post-compromise visibility (see what traffic hit the instance).

---

### Q23 (Governance) — DNSSEC Broken Trust Chain

**Scenario:** DNSSEC signing enabled on subdomain, KSK generated. Error: "broken trust chain" resolving DS record.

**Your Answer:** D (Verify DNSSEC propagation to authoritative servers)
**Correct:** C (Add a Delegation Signer (DS) record for the subdomain in the parent domain's DNS zone)

**Key concept:** DNSSEC trust chain: parent zone must have a DS record pointing to the child zone's KSK. Without DS record in parent = chain of trust is broken. Enabling DNSSEC signing alone isn't enough — you must link child to parent via DS record.

**Rule:** "Broken trust chain" in DNSSEC = DS record missing in parent zone. Always.

---

### Q24 (Infrastructure) — Windows EC2 Boot Issue + Memory Dump Collection

**Scenario:** Windows EC2 can't boot (no RDP access). Need to collect memory dump files from the instance.

**Your Answer:** B (SSM agent + CloudWatch runbook)
**Correct:** C (EC2Rescue tool for Windows Server — manually run to collect memory dumps)

**Key concept:** EC2Rescue for Windows = AWS tool to diagnose OS-level issues and collect memory dumps. SSM agent can't help if the OS won't boot (agent requires running OS). Inspector = CVE scanning, not memory dumps. Console screenshot = visual only, not actual dump.

**Rule:** "Windows boot issue + collect memory dump" = EC2Rescue for Windows. SSM requires running OS.

---

### Q25 (Infrastructure) — SSM Session Manager + VPC Endpoints + SGs (Select THREE)

**Scenario:** EC2 in private subnet, no IGW, SG has NO inbound/outbound rules. Need to connect via Session Manager. SSM agent installed.

**Your Answer:** A + D (VPC endpoint + EC2 outbound to endpoint SG on 443) — missing third
**Correct:** A + C + D (VPC endpoint + endpoint SG allows inbound from VPC CIDR on 443 + EC2 SG outbound to endpoint SG on 443)

**Key concept:** THREE things needed for SSM via VPC endpoint in private subnet:
1. Create VPC interface endpoint for SSM (A)
2. Endpoint SG: allow INBOUND 443 from VPC CIDR (C) — so EC2 can reach the endpoint
3. EC2 SG: allow OUTBOUND 443 to the endpoint SG (D) — so EC2 can send HTTPS to endpoint

**Rule:** Interface endpoint = TWO SGs must cooperate. EC2 SG outbound 443 + Endpoint SG inbound 443. Miss either = timeout.

---

### Q26 (Infrastructure) — NLB + IDS Inspection

**Scenario:** NLB distributes traffic. Security team must inspect ingress/egress traffic using IDS.

**Your Answer:** D (Traffic Mirroring on NLB)
**Correct:** A (AWS Network Firewall at VPC level with custom rule groups + route tables)

**Key concept:** "IDS/IPS" + "inspect traffic" = AWS Network Firewall (Suricata-based). Traffic Mirroring = copy traffic for passive analysis (not inline inspection/blocking). Network Firewall = inline (can block). NLB doesn't support Traffic Mirroring anyway.

**Rule:** "Inspect + block/IDS/IPS" = Network Firewall (inline). "Copy for analysis" = Traffic Mirroring (passive, doesn't block).

---

### Q27 (Infrastructure) — ALB + HIDS + Perfect Forward Secrecy

**Scenario:** HIDS running on EC2 instances behind ALB. Must add security features for user privacy WITHOUT interfering with HIDS.

**Your Answer:** C (HTTPS listener, decrypt at ALB, PFS on EC2)
**Correct:** A (HTTPS listener with ECDHE, send encrypted traffic to EC2, enable PFS)

**Key concept:** HIDS needs to inspect traffic ON the instance. If you decrypt at ALB (C), traffic between ALB→EC2 is unencrypted = HIDS can inspect but privacy is weaker. Answer A sends encrypted traffic END-TO-END (ALB re-encrypts to EC2), and HIDS runs on the instance where decryption happens. ECDHE = PFS = each session has unique keys (past sessions can't be decrypted if key is compromised later).

**Rule:** "Without interfering with HIDS" + "improve privacy" = end-to-end encryption (encrypt to EC2). HIDS sees decrypted traffic at the instance level.

---

### Q28 (IR) — Session Manager Encrypted Session Logs

**Scenario:** Secure access to EC2 without SSH/bastion/keys. Must monitor and record encrypted session activity logs.

**Your Answer:** D (CloudWatch Agent + KMS log group)
**Correct:** C (Session Manager + CloudWatch logging with "upload session logs" option + encrypted CW Logs group)

**Key concept:** Session Manager has BUILT-IN session logging (records every keystroke/command). You enable "upload session logs" in Session Manager preferences → CW Logs. CloudWatch Agent (D) collects OS-level logs, NOT session activity. "Session activity logs" = Session Manager's native feature.

**Rule:** "Record session activity" = Session Manager logging (built-in). NOT CloudWatch Agent (that's for app/OS logs).

---

### Q29 (IR) — GuardDuty Finding Investigation with Detective

**Scenario:** GuardDuty UnauthorizedAccess:EC2/TorClient finding. Determine if instance is compromised. VPC Flow Logs, Config, Detective, Inspector all enabled.

**Your Answer:** D (Inspector risk score)
**Correct:** A (Investigate VPC Flow logs using Detective — analyze network activity patterns, scope, impact)

**Key concept:** "Determine whether compromised" = INVESTIGATE = Detective. Detective ingests VPC Flow Logs + CloudTrail + GuardDuty and provides visualizations of network patterns. Inspector = CVE scanning (software vulnerabilities), not behavioral investigation. Config = configuration state, not network behavior.

**Rule:** "Investigate" / "determine scope" / "analyze patterns" = Detective. Inspector = vulnerabilities. Config = configuration drift.

---

### Q30 (IR) — Route 53 Public DNS Query Logging

**Scenario:** Misconfigured DNS in Route 53 caused outage. Need to log PUBLIC DNS queries for future debugging.

**Your Answer:** C (Route 53 Resolver query logging → CW Logs)
**Correct:** A (Route 53 DNS query logging → CW Logs)

**Key concept:** TWO different logging features in Route 53:
- **DNS query logging** = logs queries to YOUR public hosted zones (external users resolving your domains). Destination = CloudWatch Logs ONLY.
- **Resolver query logging** = logs queries FROM your VPC (internal resources resolving any domain). Destination = CW Logs, S3, or Kinesis Firehose.

"Public DNS queries" = DNS query logging (A). "VPC DNS queries" = Resolver query logging (C).

**Rule:** Public hosted zone queries = DNS query logging. VPC outbound queries = Resolver query logging.

---

### Q31 (IR) — Lambda + Athena Query Results Not Delivered to S3

**Scenario:** Lambda analyzes CloudTrail logs via Athena. Works in Console but no query results delivered to S3 bucket when Lambda runs.

**Your Answer:** B (Security analyst lacks s3:PutObject)
**Correct:** A (Lambda execution role has insufficient S3 permissions)

**Key concept:** Lambda runs as its EXECUTION ROLE, not as the analyst. "Works in Console" (analyst's permissions) but "Lambda fails" = Lambda's role is missing permissions. The analyst's permissions are irrelevant at runtime — Lambda uses its own role.

**Rule:** "Works in Console but not in Lambda" = Lambda execution role missing permissions. Lambda doesn't inherit the caller's permissions.

---

### Q32 (IAM) — S3 Bucket Policy for Federated User

**Scenario:** Restrict S3 access for a specific federated user "Bill." Maintain Bill's other permissions unchanged.

**Your Answer:** C (Deny with `arn:aws:sts::123456789012:assumed-role/*/Bill`)
**Correct:** A (Deny with `arn:aws:sts::123456789012:federated-user/Bill`)

**Key concept:** Federated users have a specific ARN format: `arn:aws:sts::ACCOUNT:federated-user/USERNAME`. `assumed-role` is for IAM roles assumed via STS. `iam::ACCOUNT:user/` is for IAM users. Different identity types = different ARN formats.

**Rule:** Federated user = `sts::account:federated-user/name`. Assumed role = `sts::account:assumed-role/role-name/session`. IAM user = `iam::account:user/name`.

---

### Q33 (IAM) — CloudFormation Stack Policy + Termination Protection

**Scenario:** Prevent users from modifying physical IDs or removing resources from CF stack. Only admins can modify.

**Your Answer:** B + C (Termination protection + Stack Policy deny Update:Replace and Update:Delete)
**Correct:** A + B (Stack Policy deny Update:* + Termination protection)

**Key concept:** "Unable to modify physical IDs OR remove resources" = deny ALL updates (Update:*). Update:Replace changes physical ID. Update:Delete removes resources. Update:Modify changes in-place. Denying only Replace+Delete still allows Modify — which could change physical IDs in some cases. Deny Update:* = blanket protection.

**Rule:** "Cannot modify or remove" = Stack Policy `Update:*` (deny everything). Termination protection = prevent stack deletion. Both together = full lockdown.

---

### Q34 (IAM) — Cognito JWT Token Verification (Most Secure)

**Scenario:** Compromised user accounts. Security engineer must manually verify ID/access tokens for signs of unauthorized access or tampering.

**Your Answer:** C (Decode JWT, extract claims, compare to expected values)
**Correct:** B (Use aws-jwt-verify library — verifies signature + sub + aud + iss + exp)

**Key concept:** Decoding a JWT (C) only reads the payload — it does NOT verify the cryptographic signature. An attacker can forge a JWT payload. The `aws-jwt-verify` library (B) verifies the RSA SIGNATURE against Cognito's public key, then validates claims. "Most secure" = signature verification, not just payload decoding.

**Rule:** "Verify JWT securely" = verify SIGNATURE (aws-jwt-verify). "Decode JWT" = just read payload (no tamper detection). Decode ≠ verify.

---

### Q35 (Detection) — Inspector Org-Wide Deployment with Auto-Enable

**Scenario:** Assess EC2 + ECR for vulnerabilities. Auto-deploy to all members including new accounts. Forward to Security Hub.

**Your Answer:** A (Delegated admin + EventBridge rule for SH findings + SNS)
**Correct:** D (Delegated admin + auto-enable for new member accounts)

**Key concept:** The question asks HOW TO DEPLOY Inspector org-wide, not how to route findings. Inspector natively integrates with Security Hub (no EventBridge rule needed for forwarding). "Auto-enable for new member accounts" = the deployment mechanism. A adds unnecessary notification plumbing that wasn't asked for.

**Rule:** "Deploy across all members + new accounts" = delegated admin + auto-enable. Don't add notification layers when the question only asks about deployment.

---

### Q36 (Detection) — CloudTrail KMS Event Filtering (Write-Only)

**Scenario:** Overwhelmed by KMS audit logs (99% are Encrypt/Decrypt/GenerateDataKey). Only need to track Disable, Delete, ScheduleKey. Most efficient solution.

**Your Answer:** B (Macie to classify CloudTrail logs)
**Correct:** A (Trail configured to record WRITE-ONLY management events)

**Key concept:** Encrypt/Decrypt/GenerateDataKey = READ operations (using the key). Disable/Delete/ScheduleKey = WRITE operations (modifying the key). Setting trail to "write-only management events" filters out 99% of the noise at source. Macie = S3 PII scanning, not log filtering.

**Rule:** KMS usage (Encrypt/Decrypt) = Read events. KMS management (Disable/Delete/Schedule) = Write events. Filter at CloudTrail trail level, not after.

---

### Q37 (Detection) — GuardDuty Suppression for Known Mining Instances

**Scenario:** Company does Bitcoin mining on AWS. GuardDuty generates too many CryptoCurrency findings. Reduce false positives + reduce management overhead.

**Your Answer:** D (Suppression rule filtered by instance ID)
**Correct:** C (Tag instances with "Mining" + suppression rule filtered by finding type + tag value)

**Key concept:** Instance IDs change (scaling, replacement). Tags persist across instance lifecycle. "Reduce management overhead" = use tags (no need to update suppression rule when instances change). Filter by tag = scalable. Filter by instance ID = brittle (must update rule every time instances change).

**Rule:** Suppression rules: filter by TAG (scalable) not instance ID (brittle). Tags survive scaling/replacement.

---

### Q38 (Data Protection) — Enforce Specific KMS Key Org-Wide (SCP + Key Policy)

**Scenario:** Centrally enforce encryption with specific CMK across all accounts. Prevent noncompliant resources. Principle of least privilege for key access.

**Your Answer:** A (S3 Bucket policy + SCP)
**Correct:** C (Key policy with kms:Decrypt for S3/DynamoDB/Lambda + SCP denying creation without the key)

**Key concept:** The question requires TWO things: (1) prevent noncompliant resources = SCP, (2) least privilege KEY ACCESS = key policy. Option A uses bucket policy (per-bucket, doesn't scale org-wide) and misses the key policy requirement. C uses SCP (org-wide prevention) + key policy (least privilege on who can use the key).

**Rule:** "Centrally enforce" = SCP. "Least privilege for key access" = key policy. Both needed together.

---
