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
