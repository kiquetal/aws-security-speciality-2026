# Dojo Practice Exam Set 4 — Full Review

> Date: 2026-06-22
> Score: 22/33 (64%) — 25/39 points (64.1%)
> Time: 34:32
> Purpose: Capture ALL wrong questions for targeted gap analysis and re-drill.

---

## Score by Category

| Category | Score |
|---|---|
| Data Protection | 66.67% |
| Detection | 60% |
| Identity and Access Management | 33.33% |
| Incident Response | 80% |
| Infrastructure Security | 75% |
| Management and Security Governance | 100% |
| Security Foundations and Governance | 100% |
| Security Logging and Monitoring | 100% |
| Threat Detection and Incident Response | 25% |

---

## Questions for Review

### Q — IAM Credential Report 4-Hour Cache

**Scenario:** Security overhaul, Config rules enabled, GenerateCredentialReport shows noncompliant resources.

**Your Answer:** C (MaximumExecutionFrequency set to 3 hours)
**Correct:** D (Credential report generated less than 4 hours ago — cache is stale)

**Key concept:** `GenerateCredentialReport` is cached for 4 hours minimum. Recent IAM changes won't appear until cache expires. The noncompliant flags are from the OLD cached report showing pre-fix state.

**Rule:** "Just changed IAM + credential report shows old state" = 4-hour cache. Not a Config frequency issue.

---

### Q — Permission Boundary Delegation vs Service Catalog

**Scenario:** 1,200 accounts, backlog of IAM role requests, app teams need to independently provision roles with limited scope.

**Your Answer:** A (Service Catalog with pre-approved IAM role templates)
**Correct:** C (SCP + permissions boundary — teams create their own roles within guardrails)

**Key concept:** "Independently provision" = self-service CREATION, not selection from a menu. Service Catalog requires security team to build every template (backlog persists). SCP + boundary = one-time setup, teams create anything within ceiling.

**Rule:** "Independently provision" + "limited scope" + "least overhead" = boundary delegation. Service Catalog = "self-service DEPLOY pre-built infra."

---

### Q — SCP Attachment: OU vs Individual Accounts

**Scenario:** Restrict to ap-southeast-1 for existing AND future accounts in Development OU.

**Your Answer:** A (SCP attached to individual Development accounts)
**Correct:** C (SCP attached to Development OU)

**Key concept:** "Existing + future accounts" = attach to OU (auto-applies to new accounts). Individual account attachment requires manual action for each new account.

**Rule:** SCP questions — read the ATTACHMENT TARGET first (OU vs account), not the JSON.

---

### Q — EBS Snapshot Sharing (Default Key → CMK)

**Scenario:** Error: "Encrypted snapshots with EBS default key cannot be shared." Share with security account for forensics.

**Your Answer:** A + B + E (included "create volume from snapshot" — unnecessary step)
**Correct:** A + C + E (Create CMK → Copy snapshot with CMK → Share snapshot → Grant key access)

**Key concept:** Copy snapshot with re-encryption (A) already produces a shareable snapshot. No need to create an intermediate volume (B). The flow is: copy snapshot → share it → grant key.

**Rule:** "Default key can't share" → copy snapshot with CMK → share → grant key policy access. No volume creation needed.

---

### Q — SCP Block Root User (Containment vs Hygiene)

**Scenario:** Organizations, minimize risk if root credentials are compromised across member accounts.

**Your Answer:** A (Deactivate access key of root user)
**Correct:** D (SCP to block service access for root user)

**Key concept:** Deactivating access key only blocks programmatic access. Root can still sign in via Console with password. SCP blocks ALL service actions regardless of authentication method.

**Rule:** "If root compromised" + "minimize risk" + "Organizations" = SCP blocks root actions. Deactivate key = hygiene (one path only). SCP = containment (all paths).

---

### Q — Public-Facing EC2 Security Group (Select TWO)

**Scenario:** Public-facing HTTPS transaction system + SSH only via bastion from 192.168.2.0/24.

**Your Answer:** A + D (port 443 from internal subnet 10.0.4.0/24 + port 22 from security team)
**Correct:** B + D (port 443 from 0.0.0.0/0 + port 22 from security team)

**Key concept:** "Public-facing to customers over internet" = customers ARE the internet = 0.0.0.0/0 on 443. Internal subnet restriction would block all customer traffic.

**Rule:** "Public-facing + HTTPS" = 0.0.0.0/0 on 443. "Highest security" doesn't override the functional requirement of being publicly accessible.

---

### Q — CW Agent vs SSM Agent (Log Shipping)

**Scenario:** Custom log files on EC2, available to ops within 30 minutes, no interactive sessions.

**Your Answer:** D + E (SSM agent sends logs to CW Logs + EventBridge schedule)
**Correct:** A + E (CloudWatch agent sends logs to CW Logs + EventBridge schedule)

**Key concept:** CloudWatch agent = ships custom log files. SSM agent = executes commands, sessions, patching. SSM agent CANNOT ship logs to CloudWatch Logs — that's CW agent's job.

**Rule:** "Ship custom logs to CW Logs" = always CW agent. SSM agent manages instances, doesn't ship logs.

---

### Q — Secrets Retrieval: Deploy Time vs Boot Time

**Scenario:** EC2 needs sensitive config during bootstrapping. Must not be hardcoded. Strict permissions.

**Your Answer:** B (Secrets Manager + CF `ValueFrom` template injection)
**Correct:** D (Parameter Store + IAM role + ssm:GetParameters at runtime)

**Key concept:** CF `ValueFrom` resolves at DEPLOY time (secret visible in stack). Instance role + API call retrieves at BOOT time (secret only in memory). "During initialization/bootstrapping" = boot time = runtime retrieval.

**Rule:** "During bootstrapping" = runtime API call via instance role. CF ValueFrom = deploy-time injection (wrong timing, less secure).

---

### Q — Rotation Lambda "Unable to log into database"

**Scenario:** Lambda rotates Secrets Manager credentials. VPC endpoint for SM works. Error: can't log into database.

**Your Answer:** C (Force rotation via CLI)
**Correct:** D (Update SG rules: Lambda egress to EC2 + EC2 ingress from Lambda)

**Key concept:** The Lambda successfully retrieved the secret (SM endpoint works) but can't CONNECT to the database = network issue between Lambda and DB. SG must allow Lambda → EC2 traffic.

**Rule:** Rotation error "Unable to log into database" = network issue (Lambda can't reach DB). Not a Secrets Manager or permissions issue.

---

### Q — Log Source Matching (VPC Flow Logs vs TGW Flow Logs)

**Scenario:** Match log sources to monitoring requirements: intra-subnet, DNS, hub-and-spoke, HTTP patterns.

**Your Error:** Swapped VPC Flow Logs and TGW Flow Logs.

**Correct mapping:**
- Same subnet / lateral movement → **VPC Flow Logs** (ENI-level, sees intra-VPC)
- DNS lookups / C2 detection → **Resolver Query Logs**
- Hub-and-spoke / cross-VPC → **TGW Flow Logs** (sees what crosses the gateway)
- HTTP request patterns → **ELB Access Logs**

**Rule:** VPC Flow Logs = intra-VPC (traffic that never leaves). TGW Flow Logs = cross-VPC (traffic that traverses the hub). Each log source sees traffic at ITS layer only.

---

### Q — Security Hub Setup Ordering

**Correct Order:** Enable SH in admin account → Designate as admin → Enable in members → Cross-account access

**Rule:** Service must EXIST in admin account before it can be designated admin. "Enable → Designate → Members → Access" (E-D-M-A).

---

## Error Pattern Analysis

| Type | Count | Pattern |
|---|---|---|
| **Reading/wording traps** | 6 | Missed key phrases: "independently", "existing+future", "public-facing", "bootstrapping" |
| **Scope confusion** | 2 | VPC Flow vs TGW Flow, snapshot vs volume |
| **New facts** | 2 | Credential report 4hr cache, SSM vs CW agent distinction |
| **Containment vs hygiene** | 1 | SCP root block vs deactivate key |

**Primary improvement area:** Read the KEY PHRASE in question stem before evaluating options.
