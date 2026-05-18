# SCS-C03 Question Tracker

> Track every question attempted. Review ❌ and ⚠️ items before the exam.

---

## Quick Stats (Cumulative)

| Metric | Value |
|---|---|
| **Total Questions** | 276 |
| **✅ Correct** | 201 (73%) |
| **⚠️ Partial** | 20 (7%) |
| **❌ Wrong** | 55 (20%) |
| **Sessions** | 36 |
| **Re-tests Passed** | 92 of 116 |

## Domain Breakdown

| Domain | ✅ | ⚠️ | ❌ | Total | Score % | Weak? |
|---|---|---|---|---|---|---|
| D1: Detection | 41 | 4 | 20 | 65 | 63% | 🟡 |
| D2: Incident Response | 6 | 1 | 1 | 8 | 75% | 🟡 |
| D3: Infrastructure Security | 26 | 4 | 5 | 35 | 74% | 🟡 |
| D4: Identity & Access Management | 81 | 7 | 14 | 102 | 79% | 🟡 |
| D5: Data Protection | 37 | 3 | 7 | 47 | 79% | 🟡 |
| D6: Governance | 10 | 1 | 8 | 19 | 53% | 🟡 |

Legend: 🔴 < 50% — 🟡 50–79% — 🟢 ≥ 80%

## Weak Areas to Review

| Priority | Topic | Questions | Domain | Count |
|---|---|---|---|---|
| 🔴 1 | Detect vs prevent (GuardDuty vs policy) | Q100, Q105, Q153, Q156, Q158 | D1, D5 | 5 |
| 🔴 2 | GuardDuty finding types | Q116, Q142, Q154, Q155 | D1 | 4 |
| 🔴 3 | Network Firewall TLS inspection | Q35, Q87, Q152 | D3 | 3 |
| 🔴 4 | Security services comparison | Q5, Q24 | D1 | 2 |
| 🔴 5 | RAM vs KMS Grants | Q11, Q37 | D4 | 2 |
| 🔴 6 | Cross-account KMS + SCP evaluation | Q70, Q256 | D4 | 2 |
| 🔴 7 | Session policy bypass by resource-based policy | Q96, Q169 | D4 | 2 |
| 🔴 8 | GuardDuty finding types (Impact vs CryptoCurrency) | Q178, Q226 | D1 | 2 |
| 🔴 9 | Detect vs prevent (GuardDuty vs Access Analyzer) | Q187, Q233 | D1 | 2 |
| 🔴 10 | Service Catalog (self-service) | Q274, Q277 | D6 | 2 |
| 🟡 11 | CloudTrail data vs management events | Q1 | D1 | 1 |
| 🟡 12 | Basic vs Advanced event selectors | Q2 | D1 | 1 |
| 🟡 13 | Troubleshooting (Task 1.3) | Q6 | D1 | 1 |
| 🟡 14 | Policy layers reference | Q7 | D4 | 1 |
| 🟡 15 | faq-ram-vs-rcp.md | Q12 | D4 | 1 |
| 🟡 16 | GuardDuty vs CloudTrail | Q13 | D1 | 1 |
| 🟡 17 | DNS Firewall | Q14 | D3 | 1 |
| 🟡 18 | Cross-account patterns | Q15 | D5 | 1 |
| 🟡 19 | CloudTrail Lake vs S3+Athena | Q23 | D1 | 1 |
| 🟡 20 | NACLs stateless | Q34 | D3 | 1 |
| 🟡 21 | RAM vs RCP | Q38 | D4 | 1 |
| 🟡 22 | RCP exemptions (SLR vs service principal) | Q39 | D4 | 1 |
| 🟡 23 | RCP exemptions (PrincipalIsAWSService) | Q42 | D4 | 1 |
| 🟡 24 | Cross-account KMS | Q53 | D4 | 1 |
| 🟡 25 | STS session revocation | Q62 | D4 | 1 |
| 🟡 26 | Session tags + ABAC | Q63 | D4 | 1 |
| 🟡 27 | SCP + RequestTag enforcement | Q68 | D4 | 1 |
| 🟡 28 | Session tags + ABAC (ResourceTag vs RequestTag) | Q72 | D4 | 1 |
| 🟡 29 | Session policy as ceiling | Q78 | D4 | 1 |
| 🟡 30 | SCP cannot be bypassed | Q83 | D4 | 1 |
| 🟡 31 | MRK independent key policies | Q84 | D5 | 1 |
| 🟡 32 | Object Lock Compliance vs Legal Hold | Q85 | D5 | 1 |
| 🟡 33 | Detect C2 = GuardDuty (not DNS Firewall) | Q106 | D1 | 1 |
| 🟡 34 | Imported key rotation procedure | Q114 | D5 | 1 |
| 🟡 35 | SCP for preventive guardrails | Q119 | D6 | 1 |
| 🟡 36 | RAM for resource sharing | Q126 | D6 | 1 |
| 🟡 37 | DNS Firewall rule actions | Q129 | D3 | 1 |
| 🟡 38 | GuardDuty vs Inspector | Q132 | D1 | 1 |
| 🟡 39 | DNS Firewall rule structure | Q134 | D3 | 1 |
| 🟡 40 | Step Functions for IR | Q138 | D2 | 1 |
| 🟡 41 | Access Analyzer modes | Q144 | D1 | 1 |
| 🟡 42 | Validate findings (Task 2.2.3) | Q148 | D2 | 1 |
| 🟡 43 | Data masking (Macie ≠ logs) | Q181 | D5 | 1 |
| 🟡 44 | RCP exemptions (SLR) | Q183 | D4 | 1 |
| 🟡 45 | Access Analyzer policy validation vs Simulator | Q184 | D4 | 1 |
| 🟡 46 | KMS auto-rotation retention | Q192 | D5 | 1 |
| 🟡 47 | KMS key policy delegation + GenerateDataKey | Q206 | D5 | 1 |
| 🟡 48 | Firewall Manager SG audit | Q208 | D3 | 1 |
| 🟡 49 | GuardDuty is regional + agentless | Q232 | D1 | 1 |
| 🟡 50 | CloudWatch Logs Insights vs Detective | Q236 | D1 | 1 |
| 🟡 51 | SCP for preventive guardrails (Control Tower) | Q251 | D6 | 1 |
| 🟡 52 | Secrets Manager cross-region replication | Q258 | D5 | 1 |
| 🟡 53 | SCP for preventive enforcement | Q261 | D3 | 1 |
| 🟡 54 | SCIM provisioning (Identity Center) | Q263 | D4 | 1 |
| 🟡 55 | KMS key policy root = delegation, not grant | Q264 | D5 | 1 |
| 🟡 56 | Audit Manager vs Artifact | Q271 | D6 | 1 |
| 🟡 57 | StackSets vs Firewall Manager | Q273 | D6 | 1 |
| 🟡 58 | Config conformance packs | Q275 | D6 | 1 |
| 🟡 59 | StackSets vs Conformance Pack | Q276 | D6 | 1 |

---

## Session Index

| # | Date | Questions | ✅ | ⚠️ | ❌ | Domains Covered | Link |
|---|---|---|---|---|---|---|---|
| 1 | 2025-05-01 | Q1–Q20 | 10 | 6 | 4 | D1 Detection · D3 Infrastructure · D4 IAM · D5 Data Protection | [Jump](#session-1--2025-05-01) |
| 2 | 2025-05-02 | Q21–Q23 | 2 | 0 | 1 | D1 Detection (re-test) | [Jump](#session-2--2025-05-02) |
| 3 | 2025-05-03 | Q24–Q25 | 1 | 1 | 0 | D1 Detection (re-test) | [Jump](#session-3--2025-05-03) |
| 4 | 2025-05-04 | Q26–Q35 | 8 | 1 | 1 | D3 Infrastructure Security (firewalls comparison) | [Jump](#session-4--2025-05-04) |
| 5 | 2025-05-05 | Q36–Q38 | 1 | 2 | 0 | D4 Identity & Access Management (re-test) | [Jump](#session-5--2025-05-05) |
| 6 | 2025-05-05 | Q39–Q43 | 3 | 0 | 2 | D4 Identity & Access Management (policy layers quiz) | [Jump](#session-6--2025-05-05) |
| 7 | 2025-05-05 | Q44–Q48 | 5 | 0 | 0 | D4 Identity & Access Management (rapid fire — post hyperfocus) | [Jump](#session-7--2025-05-05) |
| 8 | 2025-05-05 | Q49–Q58 | 9 | 1 | 0 | D4 Identity & Access Management (Week 1 final quiz — mixed Task 4.1 + 4.2) | [Jump](#session-8--2025-05-05) |
| 9 | 2025-05-08 | Q59–Q63 | 3 | 0 | 2 | D4 Identity & Access Management (Week 2 — cross-account, VP, STS) | [Jump](#session-9--2025-05-08) |
| 10 | 2025-05-08 | Q64–Q68 | 4 | 1 | 0 | D4 Identity & Access Management (Week 2 — Identity Center, session policies, VP, ABAC) | [Jump](#session-10--2025-05-08) |
| 11 | 2025-05-09 | Q69–Q73 | 3 | 0 | 2 | D4 Identity & Access Management (re-test — cross-account KMS, STS revocation, ABAC, RAM) | [Jump](#session-11--2025-05-09) |
| 12 | 2025-05-09 | Q74–Q78 | 4 | 0 | 1 | D4 Identity & Access Management (Week 2 quiz — data perimeter, VP, boundaries, session policies) | [Jump](#session-12--2025-05-09) |
| 13 | 2025-05-09 | Q79–Q83 | 4 | 0 | 1 | D4 Identity & Access Management (Week 2 final quiz — ABAC, boundaries, cross-account KMS, RCP, SCP bypass) | [Jump](#session-13--2025-05-09) |
| 14 | 2025-05-09 | Q84–Q88 | 2 | 0 | 3 | D5 Data Protection · D3 Infrastructure Security (combined mini-exam) | [Jump](#session-14--2025-05-09) |
| 15 | 2025-05-13 | Q89–Q91 | 3 | 0 | 0 | D5 Data Protection · D3 Infrastructure Security (re-test) | [Jump](#session-15--2025-05-13) |
| 16 | 2025-05-13 | Q92–Q96 | 4 | 0 | 1 | D4 Identity & Access Management (Week 2 final quiz — SCP bypass, session policies, ABAC, cross-account KMS) | [Jump](#session-16--2025-05-13) |
| 17 | 2025-05-13 | Q97–Q99 | 3 | 0 | 0 | D4 Identity & Access Management · D1 Detection (re-test — SLR exemptions, session policy bypass, Security Hub) | [Jump](#session-17--2025-05-13) |
| 18 | 2025-05-13 | Q100–Q104 | 4 | 1 | 0 | D5 Data Protection (Week 3 mini-exam — KMS, S3 encryption, Secrets Manager, Object Lock) | [Jump](#session-18--2025-05-13) |
| 19 | 2025-05-14 | Q105–Q109 | 3 | 0 | 2 | D1 Detection (re-test — detect vs prevent, security services comparison) | [Jump](#session-19--2025-05-14) |
| 20 | 2025-05-15 | Q110–Q119 | 7 | 2 | 1 | Cross-domain practice exam (Week 11 — all domains) | [Jump](#session-20--2025-05-15) |
| 21 | 2025-05-15 | Q120–Q129 | 8 | 1 | 1 | Cross-domain timed practice exam (Week 11 — all domains) | [Jump](#session-21--2025-05-15) |
| 22 | 2025-05-15 | Q130–Q139 | 7 | 1 | 2 | Cross-domain timed practice exam (Week 11 — all domains, RAM/FM focus) | [Jump](#session-22--2025-05-15) |
| 23 | 2025-05-15 | Q140–Q149 | 7 | 2 | 1 | D1 Detection · D2 Incident Response (re-test — post-video drill) | [Jump](#session-23--2025-05-15) |
| 24 | 2025-05-16 | Q150–Q154 | 2 | 1 | 2 | Cross-domain (re-test — red-priority weak areas drill) | [Jump](#session-24--2025-05-16) |
| 25 | 2025-05-16 | Q155–Q159 | 2 | 0 | 3 | D1 Detection (re-test — GuardDuty finding types + detect vs prevent drill) | [Jump](#session-25--2025-05-16) |
| 26 | 2025-05-16 | Q160–Q182 | 20 | 0 | 3 | Cross-domain exam-format practice (Week 11 — all domains) | [Jump](#session-26--2025-05-16) |
| 27 | 2025-05-16 | Q183–Q206 | 19 | 0 | 5 | Cross-domain exam-format practice (Week 11 — hardest topics) | [Jump](#session-27--2025-05-16) |
| 28 | 2025-05-16 | Q207–Q216 | 9 | 0 | 1 | Cross-domain exam-format practice (Week 11 — mixed, targeting remaining gaps) | [Jump](#session-28--2025-05-16) |
| 29 | 2025-05-16 | Q217–Q226 | 9 | 0 | 1 | Cross-domain exam-format practice (Week 11 — final killer set, all weak spots) | [Jump](#session-29--2025-05-16) |
| 30 | 2025-05-17 | Q227–Q231 | 5 | 0 | 0 | Cross-domain (re-test — red-priority gaps: Impact vs CryptoCurrency, session policy bypass) | [Jump](#session-30--2025-05-17) |
| 31 | 2025-05-17 | Q232–Q241 | 7 | 0 | 3 | D1 Detection + Cross-domain (Week 11 — D1 focus, targeting 62% domain) | [Jump](#session-31--2025-05-17) |
| 32 | 2025-05-17 | Q246–Q255 | 9 | 0 | 1 | Cross-domain exam-format practice (Week 11 — mixed, all domains) | [Jump](#session-32--2025-05-17) |
| 33 | 2025-05-17 | Q256–Q265 | 5 | 0 | 5 | Cross-domain exam-format practice (Week 11 — harder scenarios, multi-concept) | [Jump](#session-33--2025-05-17) |
| 34 | 2025-05-18 | Q266–Q270 | 5 | 0 | 0 | Cross-domain (re-test — Session 33 errors) | [Jump](#session-34--2025-05-18) |
| 35 | 2025-05-18 | Q271–Q275 | 1 | 0 | 4 | D6 Governance (untested gaps — StackSets, Audit Manager, Artifact, Service Catalog, Conformance Packs) | [Jump](#session-35--2025-05-18) |
| 36 | 2025-05-18 | Q276–Q280 | 3 | 0 | 2 | D6 Governance (re-test — StackSets, Service Catalog, Audit Manager, Artifact, Conformance Packs) | [Jump](#session-36--2025-05-18) |

---

## Sessions

### Session 1 — 2025-05-01

**Domains:** D1 Detection · D3 Infrastructure · D4 IAM · D5 Data Protection
**Score:** 10 ✅ · 6 ⚠️ · 4 ❌ (50% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Review Topic |
|---|---|---|---|---|---|---|
| 1 | D1 | S3 bucket exfiltrated object-by-object — which CloudTrail event type? Enabled by default? | "Not enabled by default, PutEvent" | ⚠️ | Data events, **GetObject** (not Put). Not enabled by default. | CloudTrail data vs management events |
| 2 | D1 | Lambda `UpdProdCount` — most flexible way to log invocations? | Didn't know | ❌ | Advanced event selectors with `StartsWith` on resource ARN | Basic vs Advanced event selectors |
| 3 | D3 | Session Manager — security advantage from network perspective? | "No open ports" | ✅ | No inbound ports needed — outbound HTTPS only | Session Manager |
| 4 | D3 | NACLs or Security Groups — which is stateless and needs ephemeral ports? | "NACLs, 100% sure" | ✅ | NACLs are stateless | NACLs vs Security Groups |
| 5 | D1 | Detect public S3 buckets org-wide with least overhead? | Didn't know | ❌ | **Security Hub** — built-in S3 controls, org-wide | Security services comparison |
| 6 | D1 | Lambda stopped logging — Config + what? | Confused | ⚠️ | Depends: role changed → Config + IAM Access Analyzer. Role fine → CloudWatch Logs Insights | Troubleshooting (Task 1.3) |
| 7 | D4 | Resource-based policy vs RCP — difference? | Confused them | ⚠️ | RBP = per-resource, grants access. RCP = org-wide ceiling, never grants. | Policy layers reference |
| 8 | D5 | Can you rotate imported KMS key material? | "Yes" | ✅ | Yes, but only manually (alias swap) | KMS rotation matrix |
| 9 | D5 | KMS imported key — who owns durability? | "You" | ✅ | You — AWS doesn't back up imported material | KMS imported keys |
| 10 | D5 | Import NEW material into EXISTING key? | Knew it was wrong | ✅ | ❌ Can't — only re-import SAME material. New material = new key + alias swap. | KMS imported keys |
| 11 | D4 | Why can't you use RAM for KMS cross-account? | "RAM is not for sharing?" | ⚠️ | RAM IS for sharing, but doesn't support KMS. Use KMS Grants. | RAM vs KMS Grants |
| 12 | D4 | RAM vs RCP — difference? | "Didn't remember RCP" | ⚠️ | RAM shares infrastructure. RCP restricts data access. Opposite problems. | faq-ram-vs-rcp.md |
| 13 | D1 | Suspicious root login attempts — GuardDuty vs CloudTrail + CloudWatch? | Chose CloudTrail + CloudWatch | ❌ | **GuardDuty + EventBridge** — "suspicious" = GuardDuty, least overhead | GuardDuty vs CloudTrail |
| 14 | D3 | Lambda in private subnet — restrict domain lookup to one domain? | Didn't know | ❌ | **Route 53 Resolver DNS Firewall** | DNS Firewall |
| 15 | D5 | Cross-account S3 + SSE-KMS — how many policies needed? | Got Account A right, missed B | ⚠️ | THREE: bucket policy + key policy + identity policy on caller | Cross-account patterns |
| 16 | D4 | When to use RCP — identify the use case? | Got it after review | ✅ | "Outsiders + my data + org-wide" → RCP | RCP use cases |
| 17 | D1 | GuardDuty — what is it responsible for? | "GuardDuty" (for crypto mining) | ✅ | Threat detection — active malicious behavior | Security services |
| 18 | D1 | Security Hub setup order — 4 steps? | Followed along | ✅ | Enable SH → make admin → enable members → assume roles | Security Hub |
| 19 | D4 | `aws:PrincipalIsAWSService` — when to use? | Understood after explanation | ✅ | Always add when using PrincipalOrgID deny — exempts CloudTrail, Config, etc. | RCP conditions |
| 20 | D4 | VPC endpoints — why 3 for Session Manager? | Understood | ✅ | `ssm` (API) + `ssmmessages` (session) + `ec2messages` (heartbeat) | Session Manager VPC endpoints |

---

### Session 2 — 2025-05-02

**Domains:** D1 Detection (re-test)
**Score:** 2 ✅ · 0 ⚠️ · 1 ❌ (67% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 21 | D1 | Root user API calls from unexpected country — detect + isolate with least overhead? | B: GuardDuty → EventBridge → Step Functions | ✅ | GuardDuty for behavioral threats, Step Functions for orchestration | Q13 | Security services comparison |
| 22 | D1 | Log only `Prod-*` Lambda invocations, exclude read-only, queryable in Lake? | B: Advanced event selectors with StartsWith + readOnly + eventName | ✅ | Advanced selectors required for prefix, Lake requires advanced | Q2 | CloudTrail advanced selectors |
| 23 | D1 | What is CloudTrail Lake? What problem does it solve? | Didn't know it existed | ❌ | Managed query engine — replaces S3+Athena plumbing, near real-time, dashboards | — | CloudTrail Lake vs S3+Athena |

---

### Session 3 — 2025-05-03

**Domains:** D1 Detection (re-test)
**Score:** 1 ✅ · 1 ⚠️ · 0 ❌ (50% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 24 | D1 | 200 accounts, detect public S3 buckets org-wide, least overhead — Config conformance pack vs Security Hub vs Macie vs Lambda? | B: Config conformance pack | ⚠️ | C: **Security Hub** FSBP standard — wraps Config rules with less overhead, one-click org-wide, dashboards | Q5 | Security services comparison |
| 25 | D1 | Investigate credential compromise across 15 accounts, need SQL + dashboards + fast results — Athena vs Lake vs CloudWatch Logs vs OpenSearch? | B: CloudTrail Lake | ✅ | CloudTrail Lake — near real-time, cross-account, built-in SQL + dashboards | Q23 | CloudTrail Lake vs S3+Athena |

---

<!-- TEMPLATE: Copy this block for new sessions

### Session N — YYYY-MM-DD

**Domains:** Dx · Dy
**Score:** X ✅ · Y ⚠️ · Z ❌ (N% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| | | | | | | — | |

After adding a session:
1. Update the Session Index table above
2. Update Quick Stats totals
3. Update Domain Breakdown counts
4. Move resolved weak areas out, add new ones

-->

### Session 4 — 2025-05-04

**Domains:** D3 Infrastructure Security (firewalls comparison)
**Score:** 8 ✅ · 1 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 26 | D3 | Lambda in private subnet making DNS queries to C2 domains — block immediately? | DNS Firewall | ✅ | DNS Firewall — block at DNS, connection never happens | — | DNS Firewall |
| 27 | D3 | ALB receiving credential-stuffing from single IP — block? | WAF | ✅ | WAF rate-based rules — single IP, not volumetric DDoS | — | WAF vs Shield |
| 28 | D3 | Detect malware signatures in egress traffic, have Suricata rules? | Network Firewall | ✅ | Network Firewall — Suricata = Network Firewall always | — | Network Firewall |
| 29 | D3 | SG opened to 0.0.0.0/0 in 150 accounts — auto-detect and fix org-wide? | Firewall Manager | ✅ | Firewall Manager SG audit policy — org-wide, auto-remediate | — | Firewall Manager |
| 30 | D3 | 40 Gbps UDP DDoS, bill spiking, want AWS to credit scaling costs? | Shield Advanced | ✅ | Shield Advanced — DDoS cost protection | — | Shield Advanced |
| 31 | D3 | EC2 needs to reach only api.stripe.com, cheapest layer to block? | DNS Firewall | ✅ | DNS Firewall — cheapest, block all except allowed domain | — | DNS Firewall |
| 32 | D3 | Ensure all 300 accounts have same WAF rules on ALBs, auto for new accounts? | Firewall Manager | ✅ | Firewall Manager WAF policy — org-wide, auto-applies | — | Firewall Manager |
| 33 | D3 | Data encoded in DNS subdomain queries (exfiltration) — block? | DNS Firewall | ✅ | DNS Firewall — exfil is in the query itself, block the domain | — | DNS Firewall |
| 34 | D3 | NACL allows inbound 443, SG allows 443, web server not responding? | Ephemeral ports | ⚠️ | NACL needs outbound ephemeral ports (1024-65535) — stateless, must allow response | — | NACLs stateless |
| 35 | D3 | Decrypt TLS traffic, inspect plaintext for malware, re-encrypt? | WAF Advanced | ❌ | **Network Firewall** — TLS inspection is Network Firewall only, WAF never decrypts | — | Network Firewall TLS inspection |


### Session 5 — 2025-05-05

**Domains:** D4 Identity & Access Management (re-test)
**Score:** 1 ✅ · 2 ⚠️ · 0 ❌ (33% correct, 100% partial+)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 36 | D4 | Dev puts Principal:* on bucket policy, external attacker reads objects. Block all external S3 access org-wide without modifying bucket policies — which policy type and why not SCP? | "SCP can't stop external accounts, RCP is the answer" + knew PrincipalIsAWSService condition | ✅ | RCP — evaluated on resource side regardless of caller. SCP only governs principals inside your org. Conditions: PrincipalOrgID + PrincipalIsAWSService:false with IfExists. | Q7 | Policy layers — RCP vs SCP |
| 37 | D4 | 300 customers need Decrypt on your KMS key, onboard/offboard weekly. Junior suggests RAM — why won't it work? | "Limitations maybe? KMS Grants is the answer" — didn't know RAM's service list excludes KMS | ⚠️ | RAM doesn't support KMS (infrastructure only: TGW, subnets, Route 53). Even if it did, RAM shares entire resource — Grants give per-operation control (Decrypt only). Key policy 32KB limit ~200 principals; Grants unlimited. | Q11 | RAM vs KMS Grants |
| 38 | D4 | One sentence each: what problem does RAM solve vs RCP? | "RAM shares resources between accounts. RCP manage control?" — RCP answer too vague | ⚠️ | RAM = OPENS access (share infrastructure cross-account). RCP = CLOSES access (deny external principals from data org-wide). Opposite problems, different service lists, zero overlap. | Q12 | RAM vs RCP |

### Session 6 — 2025-05-05

**Domains:** D4 Identity & Access Management (policy layers quiz)
**Score:** 3 ✅ · 0 ⚠️ · 2 ❌ (60% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 39 | D4 | SLR in Account A does PutObject, RCP denies non-org principals — does SLR succeed? | "Fails — RCP needs PrincipalIsAWSService rule" | ❌ | **Succeeds** — SLRs are completely exempt from RCPs (separate mechanism from PrincipalIsAWSService). | — | RCP exemptions (SLR vs service principal) |
| 40 | D4 | Role identity policy allows kms:Decrypt, boundary only allows s3:* and ec2:* — what happens? | "Denied — boundary doesn't include KMS" | ✅ | Denied. Permission boundary is a ceiling; kms:Decrypt outside boundary = blocked at Gate 3. | — | Permission boundary as ceiling |
| 41 | D4 | External Account B assumes role in Account A, role allows s3:GetObject, SCP allows all, no RCP — succeeds? | "Succeeds — evaluated against Account A's role policies" | ✅ | Succeeds. Once role is assumed, evaluation uses Account A's SCP + role's identity policy + boundary. | — | Cross-account evaluation |
| 42 | D4 | RCP denies kms:Decrypt for external principals. CloudTrail needs to decrypt — blocked? | "RCP doesn't support KMS?" | ❌ | **Succeeds** — RCP condition `PrincipalIsAWSService: false` doesn't match CloudTrail (it IS a service), so Deny doesn't fire. RCP does support KMS. | — | RCP exemptions (PrincipalIsAWSService) |
| 43 | D4 | Role: identity=Allow s3:*, boundary=Allow GetObject+ListBucket only. Calls PutObject? | "Denied — boundary limits" | ✅ | Denied. Boundary ceiling doesn't include PutObject. Gate 3 blocks. | — | Permission boundary as ceiling |

### Session 7 — 2025-05-05

**Domains:** D4 Identity & Access Management (rapid fire — post hyperfocus)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 44 | D4 | RCP denies s3:* for non-org. ELB SLR writes access logs to S3 — blocked? | "RCP can't block service-linked role" | ✅ | Allowed — SLRs are structurally exempt from RCPs | Q39 | RCP exemptions (SLR) |
| 45 | D4 | Identity allows s3:*, boundary allows s3:Get* only. Calls s3:DeleteObject? | "Permission boundary blocks it" | ✅ | Denied — Gate 3 (boundary) doesn't include DeleteObject | — | Permission boundary |
| 46 | D4 | 400 external accounts need Decrypt, key policy at 30KB — mechanism? | "KMS Grants" | ✅ | KMS Grants — key policy near 32KB limit, grants scale without policy edits | Q37 | KMS Grants |
| 47 | D4 | Role chaining A→B→C, Role C MaxSessionDuration=12hr — actual max? | "1 hour" | ✅ | 1 hour — role chaining always resets to 1hr max | — | Role chaining |
| 48 | D4 | External account calls s3:GetObject, bucket policy grants access, no RCP — need identity policy? | "No" | ✅ | No — resource-based policy alone grants cross-account (except KMS) | — | Cross-account evaluation |

### Session 8 — 2025-05-05

**Domains:** D4 Identity & Access Management (Week 1 final quiz — mixed Task 4.1 + 4.2)
**Score:** 9 ✅ · 1 ⚠️ · 0 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 49 | D4 | Developer creates role with AdministratorAccess — prevent escalation? | "SCP deny CreateRole without boundary" | ✅ | Permission boundary delegation pattern — iam:PermissionsBoundary condition | — | Permission boundaries |
| 50 | D4 | Block external S3 access org-wide even with Principal:* bucket policy? | "RCP" | ✅ | RCP — blocks external callers regardless of resource policy | — | RCP |
| 51 | D4 | Federated Okta user needs project-scoped S3 access without per-user policies? | "ABAC with ResourceTag = PrincipalTag" | ✅ | Session tags from IdP + ABAC: aws:ResourceTag/Project = ${aws:PrincipalTag/Project} | — | ABAC + session tags |
| 52 | D4 | Role chaining A→B→C, Role C MaxSessionDuration=12hr — actual max? | "1 hour" | ✅ | 1 hour — role chaining always resets | — | Role chaining |
| 53 | D4 | Cross-account KMS decrypt — minimum policies needed? | "Key policy + identity policy in Account B" | ⚠️ | Both sides must agree: key policy names Account B + Account B identity policy allows kms:Decrypt on key ARN. Got the concept, imprecise wording. | — | Cross-account KMS |
| 54 | D4 | Can GetCallerIdentity be denied by SCP? | "No" | ✅ | Cannot be denied by any policy — always works | — | STS |
| 55 | D4 | RCP denies kms:Decrypt with PrincipalIsAWSService:false. AWS Config decrypts? | "Allowed" | ✅ | Allowed — Config is AWS service principal, condition doesn't match, deny doesn't fire | Q42 | RCP exemptions |
| 56 | D4 | Identity allows ec2:*, boundary allows RunInstances+Describe only. TerminateInstances? | "Denied" | ✅ | Denied — Gate 3 boundary doesn't include TerminateInstances | — | Permission boundary |
| 57 | D4 | Share Transit Gateway with 30 dev accounts in org? | "RAM" | ✅ | RAM — infrastructure sharing within org, auto-accept | — | RAM |
| 58 | D4 | SCP denies s3:DeleteBucket. Role identity allows s3:*. DeleteBucket? | "Denied, Gate 1" | ✅ | Denied — SCP explicit deny always wins over identity policy Allow | — | SCP |

### Session 9 — 2025-05-08

**Domains:** D4 Identity & Access Management (Week 2 — cross-account, VP, STS)
**Score:** 3 ✅ · 0 ⚠️ · 2 ❌ (60% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 59 | D4 | Cross-account S3+KMS: bucket policy + identity policy correct, forgot KMS key policy — what error? | "403" | ✅ | Access Denied (403) — KMS decrypt fails as permission error | — | Cross-account KMS |
| 60 | D4 | Vendor needs to assume role in your account, prevent confused deputy — condition key? | "ExternalId" | ✅ | `sts:ExternalId` in trust policy condition | — | Confused deputy |
| 61 | D4 | SaaS app needs "Can user X edit doc Y in tenant Z?" at runtime — IAM or VP? | "Verified Permissions" | ✅ | Verified Permissions — app-level authz, not AWS API | — | Verified Permissions |
| 62 | D4 | Compromised role with active STS sessions — revoke immediately? | "You can't" | ❌ | **You CAN** — inline Deny with `aws:TokenIssueTime` < timestamp. Only way to revoke active tokens. | — | STS session revocation |
| 63 | D4 | Federated user from Okta, SAML assertion includes Project=Phoenix — what condition key evaluates this? | "equals?" (gave operator, not key) | ❌ | `aws:PrincipalTag/Project` — session tags from IdP land in PrincipalTag | — | Session tags + ABAC |

### Session 10 — 2025-05-08

**Domains:** D4 Identity & Access Management (Week 2 — Identity Center, session policies, VP, ABAC)
**Score:** 4 ✅ · 1 ⚠️ · 0 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 64 | D4 | Okta workforce SSO into 50 accounts with temp creds — which service? | "Identity Center" | ✅ | IAM Identity Center with external IdP (Okta via SAML 2.0) | — | Identity Center |
| 65 | D4 | Broad role, need narrow creds for downstream Lambda — mechanism? | "Session role" | ✅ | Session policy passed at AssumeRole time — filters down without new role | Q62 | Session policies |
| 66 | D4 | Multi-tenant SaaS "Can editor Bob update invoice-789 in tenant Acme?" — which service? | "Verified Permissions" | ✅ | Verified Permissions — app-level authz with Cedar policies | — | Verified Permissions |
| 67 | D4 | Employee signs in via Identity Center — what does permission set become? | "IAM role" | ✅ | IAM role auto-created in target account by Identity Center | — | Identity Center |
| 68 | D4 | Enforce CostCenter tag on all EC2 creation org-wide — where + condition key? | "In the caller, aws:RequestTag" | ⚠️ | **SCP** on org root with `Null: aws:RequestTag/CostCenter = true`. Got condition key right, but "in the caller" is vague — SCP is the org-wide enforcement point. | — | SCP + RequestTag enforcement |

### Session 11 — 2025-05-09

**Domains:** D4 Identity & Access Management (re-test — cross-account KMS, STS revocation, ABAC, RAM)
**Score:** 3 ✅ · 0 ⚠️ · 2 ❌ (60% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 69 | D4 | 50 customers/month need kms:Decrypt, grant/revoke without key policy edits? | B: KMS Grant per customer | ✅ | KMS Grants — one API call per onboard, RevokeGrant to offboard, no policy edits | Q37 | RAM vs KMS Grants |
| 70 | D4 | Cross-account KMS: key policy grants Account B root, identity policy correct, still AccessDenied? | C: Missing sts:AssumeRole | ❌ | **B: Account B's SCP denies kms:Decrypt** — Lambda doesn't AssumeRole, it calls directly. Caller's SCP applies. | Q53 | Cross-account KMS + SCP evaluation |
| 71 | D4 | Exfiltrated role credentials, active sessions making calls — revoke immediately? | B: Inline Deny with TokenIssueTime | ✅ | Inline Deny with `aws:TokenIssueTime` < current timestamp — only way to revoke active sessions | Q62 | STS session revocation |
| 72 | D4 | Okta team attribute → EC2 access by team tag, no per-team policies — which two? | D: RequestTag | ❌ | **A + C**: Map Okta attribute to session tag (A) + policy with `ec2:ResourceTag/Team = ${aws:PrincipalTag/Team}` (C). RequestTag is creation-time only. | Q63 | Session tags + ABAC (ResourceTag vs RequestTag) |
| 73 | D4 | Enforce CostCenter tag on all EC2 launches org-wide? | A: SCP Deny RunInstances if RequestTag missing | ✅ | SCP + `aws:RequestTag/CostCenter` with Null condition — org-wide preventive control | Q68 | SCP + RequestTag enforcement |

### Session 12 — 2025-05-09

**Domains:** D4 Identity & Access Management (Week 2 quiz — data perimeter, VP, boundaries, session policies)
**Score:** 4 ✅ · 0 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 74 | D4 | 80 accounts, block external S3 access org-wide, exempt AWS services — which two? | A+C: RCP + PrincipalIsAWSService condition | ✅ | RCP (not SCP) blocks external callers + PrincipalIsAWSService:false exempts AWS services | — | Data perimeter (RCP) |
| 75 | D4 | Multi-tenant SaaS "editors edit own tenant docs" — centralized authz? | B: Verified Permissions with Cedar | ✅ | VP + Cedar policies evaluating tenant claims from Cognito token | — | Verified Permissions |
| 76 | D4 | Boundary delegation + must tag with own team — how many Deny statements? | C: 4 | ✅ | 4: force boundary + force team tag + deny remove + deny swap | — | Permission boundaries + ABAC |
| 77 | D4 | RCP denies non-org KMS access, same-org Account B calls Decrypt — blocked? | B: No, PrincipalOrgID matches | ✅ | Same-org caller matches condition → Deny doesn't fire → allowed | — | RCP cross-account same-org |
| 78 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, session=GetObject+PutObject — DeleteObject? | A: Allowed (identity grants s3:*) | ❌ | **C: Denied — session policy only allows GetObject+PutObject.** Session policy is a ceiling like boundary. Effective = identity ∩ boundary ∩ session ∩ SCP. ALL must allow. | — | Session policy as ceiling |

---

### Session 13 — 2025-05-09

**Domains:** D4 Identity & Access Management (Week 2 final quiz — ABAC, boundaries, cross-account KMS, RCP, SCP bypass)
**Score:** 4 ✅ · 0 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 79 | D4 | Identity Center + Okta, engineers access EC2 by project tag, no per-engineer policies — approach? | B: Session tags + ABAC | ✅ | Session tags from SAML + ABAC matching PrincipalTag/Project to ResourceTag/Project | — | Session tags + ABAC |
| 80 | D4 | Boundary allows s3+ec2+logs, identity policy allows *, attempt kms:Encrypt? | B: Denied — boundary doesn't include kms | ✅ | Boundary is ceiling — effective = identity ∩ boundary. kms not in boundary = denied. | — | Permission boundary ceiling |
| 81 | D4 | Cross-account KMS: key policy grants Account B root, identity policy allows Decrypt, no SCP restriction — result? | B: Allowed — both sides satisfied | ✅ | Key policy (Account A) + identity policy (Account B) = both sides present = allowed | Q70 | Cross-account KMS + SCP evaluation |
| 82 | D4 | Block external principals from S3 org-wide even if bucket policy says Principal:* — solution? | B: RCP with PrincipalOrgID + PrincipalIsAWSService exception | ✅ | RCP blocks external callers that SCPs can't touch. SCP only governs your own principals. | — | RCP vs SCP for external callers |
| 83 | D4 | Lambda in Account B calls S3 in Account A, bucket policy names role ARN directly, Account B SCP denies s3:GetObject — succeeds? | A: Yes — resource-based policy bypasses SCP | ❌ | **B: No — SCP cannot be bypassed by anything.** The bypass rule applies to session policies and boundaries, NEVER SCPs. | — | SCP cannot be bypassed |

---

### Session 14 — 2025-05-09

**Domains:** D5 Data Protection · D3 Infrastructure Security (combined mini-exam)
**Score:** 2 ✅ · 0 ⚠️ · 3 ❌ (40% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 84 | D5 | DynamoDB Global Table + MRK, reads fail in eu-west-1 with AccessDenied on KMS — cause? | D: MRK needs a KMS Grant in eu-west-1 | ❌ | **B: MRK replica key policy doesn't allow DynamoDB.** MRK policies are independent per region — must update each separately. | — | MRK independent key policies |
| 85 | D5 | S3 objects immutable for 5 years, root can't delete — what combination? | C: Compliance mode + Legal Hold | ❌ | **B: Compliance mode + versioning.** Legal Hold = indefinite (no expiry). Compliance mode = fixed retention period. Don't mix them. | — | Object Lock Compliance vs Legal Hold |
| 86 | D5 | App in private subnet (no NAT) needs Secrets Manager — minimum infra? | B: Interface VPC endpoint + SG allowing HTTPS | ✅ | Interface endpoint (Gateway only for S3/DynamoDB). SG must allow 443. | — | VPC endpoints |
| 87 | D3 | Network Firewall TLS inspection — users get cert warnings — what's missing? | C: Network Firewall needs public ACM cert | ❌ | **A: Firewall's CA cert isn't trusted by clients.** TLS inspection = private CA + MITM. Must distribute CA to client trust stores. | Q35 | Network Firewall TLS inspection |
| 88 | D5 | Mask credit cards in CloudWatch Logs without code changes — Macie? | C: CloudWatch Logs data protection policy | ✅ | Macie = S3 only. CloudWatch Logs data protection = real-time masking in logs. | — | Data masking (new in C03) |


---

### Session 15 — 2025-05-13

**Domains:** D5 Data Protection · D3 Infrastructure Security (re-test)
**Score:** 3 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 89 | D3 | Network Firewall TLS inspection — users get cert warnings — root cause? | B: Firewall's CA cert isn't trusted by clients | ✅ | Private CA + MITM pattern — must distribute CA to client trust stores. | Q87 | Network Firewall TLS inspection |
| 90 | D5 | DynamoDB Global Table + MRK, reads fail in eu-west-1 with AccessDenied on KMS — cause? | B: Replica key policy doesn't grant DynamoDB permission | ✅ | MRK policies are independent per region — must update each separately. | Q84 | MRK independent key policies |
| 91 | D5 | S3 objects immutable for 5 years, root can't delete, auto-deletable after — config? | B: Compliance mode + versioning | ✅ | Compliance mode = fixed period, nobody can delete. Legal Hold = indefinite. Don't mix. | Q85 | Object Lock Compliance vs Legal Hold |


---

### Session 16 — 2025-05-13

**Domains:** D4 Identity & Access Management (Week 2 final quiz — SCP bypass, session policies, ABAC, cross-account KMS)
**Score:** 4 ✅ · 0 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 92 | D4 | Lambda in Account B calls S3 in Account A, bucket policy names role ARN, Account B SCP denies s3:GetObject — succeeds? | B: No — SCP cannot be bypassed | ✅ | SCP cannot be bypassed by anything — not resource-based policies, not direct ARN grants. | Q83 | SCP cannot be bypassed |
| 93 | D4 | Role identity=s3:*, no boundary, session policy=GetObject+PutObject only — DeleteObject? | B: Denied — session policy is ceiling | ✅ | Session policy is a ceiling like boundary. Effective = identity ∩ session ∩ boundary ∩ SCP. | Q78 | Session policy as ceiling |
| 94 | D4 | Okta Team=Platform attribute, restrict StartInstances/StopInstances to matching EC2 tag — condition? | B: ec2:ResourceTag/Team = ${aws:PrincipalTag/Team} | ✅ | ResourceTag for access control on existing resources. RequestTag for creation enforcement. | Q72 | Session tags + ABAC (ResourceTag vs RequestTag) |
| 95 | D4 | Cross-account KMS: key policy grants Account B root, identity policy correct, AccessDenied — cause? | B: Account B's SCP denies kms:Decrypt | ✅ | SCP follows the caller. Caller's SCP applies even when accessing another account's resources. | Q70 | Cross-account KMS + SCP evaluation |
| 96 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, session=GetObject+ListBucket, same-account bucket policy grants PutObject — PutObject? | A: Denied — session policy doesn't include PutObject | ❌ | **B: Allowed — resource-based policy naming the role directly bypasses session policy ceiling.** Session policy only filters identity-based grants. | — | Session policy bypass by resource-based policy |


---

### Session 17 — 2025-05-13

**Domains:** D4 Identity & Access Management · D1 Detection (re-test — SLR exemptions, session policy bypass, Security Hub)
**Score:** 3 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 97 | D4 | SCP denies s3:PutObject without Env tag. Config SLR writes snapshot (no tags) — succeeds? | Fails — SCP follows users | ✅ | Fails. SCP applies to SLRs — they're principals in your account. RCP exempts SLRs, SCP does not. | Q39 | RCP exemptions (SLR vs service principal) |
| 98 | D4 | Role identity=s3:*, session policy=GetObject only, same-account bucket policy grants role PutObject — PutObject? | Succeeds — resource-based policy bypasses session ceiling | ✅ | Resource-based policy naming the role directly bypasses session policy ceiling. Session policy only filters identity-based grants. | Q96 | Session policy bypass by resource-based policy |
| 99 | D1 | 200 accounts, detect public S3 buckets org-wide, least overhead — Config conformance pack vs Security Hub vs Macie vs Lambda? | B: Security Hub FSBP | ✅ | Security Hub FSBP — one-click org-wide, built-in S3 controls, dashboards. Less overhead than Config conformance pack. | Q24 | Security services comparison |


---

### Session 18 — 2025-05-13

**Domains:** D5 Data Protection (Week 3 mini-exam — KMS, S3 encryption, Secrets Manager, Object Lock)
**Score:** 4 ✅ · 1 ⚠️ · 0 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 100 | D5 | SSE-KMS buckets, detect external decryption — which service? | B: CloudTrail + key policy condition | ⚠️ | **C: GuardDuty S3 Protection** — "detect" = GuardDuty. Key policy condition prevents, doesn't detect. | — | Detect vs prevent (GuardDuty vs policy) |
| 101 | D5 | CreateGrant → partner gets AccessDenied immediately, works 30s later — fix? | B: Pass grant token | ✅ | Grant token for immediate use before eventual consistency. | — | KMS Grants eventual consistency |
| 102 | D5 | Key material never in AWS + native S3 SSE-KMS integration — which option? | B: XKS | ✅ | External key store — material outside AWS, still integrates via KMS API. | — | XKS |
| 103 | D5 | Global Table + MRK, reads fail in eu-west-1, primary key policy correct — cause? | B: Replica key policy missing DynamoDB access | ✅ | MRK policies are independent per region — must update each separately. | Q84 | MRK independent key policies |
| 104 | D5 | Secret rotated, open DB connection still works — why? | B: AWSPREVIOUS keeps old password valid | ✅ | Old password valid as AWSPREVIOUS until next rotation cycle. | — | Secrets Manager rotation |


---

### Session 19 — 2025-05-14

**Domains:** D1 Detection (re-test — detect vs prevent, security services comparison)
**Score:** 3 ✅ · 0 ⚠️ · 2 ❌ (60% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 105 | D1 | SSE-KMS buckets, CISO wants alerts when external accounts decrypt, least overhead? | A: CloudTrail data events + metric filter | ❌ | **C: GuardDuty S3 Protection** — "alert/detect" + "least overhead" = GuardDuty. CloudTrail filter works but heavy plumbing. | Q100 | Detect vs prevent (GuardDuty vs policy) |
| 106 | D1 | Lambda making DNS queries to known C2 domain — detect and generate finding, don't block yet? | A: DNS Firewall ALERT action | ❌ | **B: GuardDuty** — reads DNS logs as foundational source, has built-in C2 threat intel, generates findings automatically. DNS Firewall ALERT logs but doesn't produce security findings. | — | Detect C2 = GuardDuty (not DNS Firewall) |
| 107 | D1 | Confirmed C2 — block DNS resolution to that domain VPC-wide immediately? | C: DNS Firewall BLOCK | ✅ | DNS Firewall BLOCK — kills query at DNS, connection never happens, VPC-wide. | — | Block C2 = DNS Firewall |
| 108 | D1 | 300 accounts, dashboard for public S3 + unencrypted EBS + CIS compliance score, least overhead? | C: Security Hub with CIS benchmark | ✅ | Security Hub — aggregation + compliance dashboards + CIS benchmark built-in, one-click org-wide. | Q5 | Security services comparison |
| 109 | D1 | EC2 exfiltrating data at 3 AM — determine who launched it, role used, other resources accessed in 48hr? | C: Detective | ✅ | Detective — "investigate" / "determine scope" / "timeline" = always Detective. | — | Detective for investigation |


---

### Session 20 — 2025-05-15

**Domains:** Cross-domain practice exam (Week 11 — all domains)
**Score:** 7 ✅ · 2 ⚠️ · 1 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 110 | D4 | Identity Center permission set=s3:*+ec2:*, boundary=s3:* only — ec2:DescribeInstances? | Blocked | ✅ | Denied — boundary doesn't include ec2:*, effective = identity ∩ boundary. | — | Permission boundary as ceiling |
| 111 | D4 | Cross-account S3, bucket policy grants role ARN, Account B SCP denies s3:GetObject — succeeds? | Blocked | ✅ | Denied — SCP cannot be bypassed by anything. | Q83 | SCP cannot be bypassed |
| 112 | D3 | Inspect egress for malware (Suricata) + block C2 DNS — which TWO services? | Network Firewall + DNS Firewall | ✅ | Network Firewall (Suricata IPS) + DNS Firewall (block C2 domains). | — | Firewalls layered |
| 113 | D3 | Private subnet EC2 needs Secrets Manager, no NAT/IGW — minimum infra? | Interface endpoint + endpoint policy | ✅ | Interface VPC endpoint + SG allowing HTTPS (443). | — | VPC endpoints |
| 114 | D5 | Imported key material — how to rotate? | "Manual rotation" (no steps) | ⚠️ | Create NEW KMS key (origin=EXTERNAL) → import new material → update alias → old key stays for old ciphertext. | — | Imported key rotation procedure |
| 115 | D5 | CreateGrant → partner gets AccessDenied immediately, works 30s later — fix? | Pass grant token | ✅ | Pass grant token in subsequent API call for immediate use before eventual consistency. | Q101 | KMS Grants eventual consistency |
| 116 | D1 | Detect credentials used from Tor exit node — which service, zero custom code? | Didn't know | ❌ | **GuardDuty** — finding type UnauthorizedAccess:IAMUser/TorIPCaller. Built-in threat intel, zero setup. | — | GuardDuty finding types |
| 117 | D1 | Query CloudTrail across 50 accounts, SQL, near real-time, dashboards, no S3/Athena? | CloudTrail Lake | ✅ | CloudTrail Lake — managed, SQL, near real-time, cross-account, dashboards. | Q25 | CloudTrail Lake |
| 118 | D2 | EC2 communicating with C2 — first 3 IR steps? | Isolate (SG) → EBS snapshot + tag → stop | ✅ | Isolate (deny-all SG) → Snapshot (EBS forensic copy) → Tag → Investigate. Never terminate first. | — | IR sequence |
| 119 | D6 | Prevent disabling GuardDuty/CloudTrail/Flow Logs org-wide, auto for new accounts? | Control Tower | ⚠️ | **SCP** (Deny statements). Control Tower uses SCPs but the mechanism itself is SCP. | — | SCP for preventive guardrails |


---

### Session 21 — 2025-05-15

**Domains:** Cross-domain timed practice exam (Week 11 — all domains)
**Score:** 8 ✅ · 1 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 120 | D4 | SCP denies PutObject without Env tag, Config SLR writes snapshot (no tags) — succeeds? | Fail | ✅ | Fails — SCP applies to SLRs. RCP exempts SLRs, SCP does not. | Q97 | SCP applies to SLRs |
| 121 | D1 | Detect root access key creation in any member account, zero code? | GuardDuty | ✅ | GuardDuty — Policy:IAMUser/RootCredentialUsage. | — | GuardDuty finding types |
| 122 | D3 | Network Firewall TLS inspection — users get cert warnings — root cause? | Import private CA in browsers | ✅ | Firewall's CA cert not trusted by clients — distribute to trust stores. | Q87 | Network Firewall TLS inspection |
| 123 | D5 | Global Table + MRK, reads fail in eu-west-1, primary key policy correct — cause? | Key policies are independent | ✅ | MRK replica key policy missing DynamoDB permission. Must update each region. | Q84 | MRK independent key policies |
| 124 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, session=GetObject only — DeleteObject? | Denied | ✅ | Session policy ceiling — DeleteObject not in session = denied. | Q78 | Session policy as ceiling |
| 125 | D2 | After isolating compromised EC2 (deny-all SG), next step? | EBS snapshot + tag | ✅ | Snapshot EBS (forensic copy) + tag. Never terminate before preserving evidence. | — | IR sequence |
| 126 | D6 | Share DNS Firewall rule groups from security account to all members, auto for new accounts? | Control Tower | ❌ | **AWS RAM** — sharing resources cross-account = RAM. Control Tower manages guardrails, not resource sharing. | — | RAM for resource sharing |
| 127 | D5 | S3 immutable 7 years, root can't delete, auto-expire after — config? | Compliance mode Object Lock | ✅ | Compliance mode + versioning. Fixed retention, nobody deletes, auto-expires. | Q85 | Object Lock Compliance mode |
| 128 | D1 | Normalize CloudTrail + VPC Flow + GuardDuty + WAF into common schema, own S3 bucket? | Security Lake | ✅ | Security Lake — OCSF format, normalizes all sources, your S3 bucket. | — | Security Lake / OCSF |
| 129 | D3 | Lambda resolve only 2 domains, block all else — service + rule structure? | DNS Firewall + DENY rule | ⚠️ | DNS Firewall correct. Actions are ALLOW/BLOCK/ALERT (not Deny). Structure: ALLOW specific → BLOCK *. | — | DNS Firewall rule actions |


---

### Session 22 — 2025-05-15

**Domains:** Cross-domain timed practice exam (Week 11 — all domains, RAM/FM focus)
**Score:** 7 ✅ · 1 ⚠️ · 2 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 130 | D6 | 200 accounts, same WAF rules on all ALBs, auto-remediate — which service? | Firewall Manager | ✅ | Firewall Manager — "ensure/enforce" + auto-remediate = FM. | — | Firewall Manager vs RAM |
| 131 | D6 | Share Transit Gateway from networking account to dev OU — which service? | RAM | ✅ | RAM — "share" infrastructure cross-account = RAM. | — | RAM for resource sharing |
| 132 | D1 | Lambda connecting to botnet IP, want security finding auto-generated — which service? | Inspector | ❌ | **GuardDuty** — active threat (C2/botnet connection) = GuardDuty. Inspector = CVEs, not active threats. | — | GuardDuty vs Inspector |
| 133 | D4 | RCP denies s3:* for non-org, ELB SLR writes access logs — blocked? | No (SLR exempt from RCP) | ✅ | SLRs are structurally exempt from RCPs. | Q44 | RCP exemptions (SLR) |
| 134 | D3 | Block all DNS except 3 domains, ALERT on "crypto" queries — rule structure? | ALERT using DNS Firewall | ⚠️ | ALLOW 3 domains → ALERT *crypto* → BLOCK *. Need full structure with priorities. | — | DNS Firewall rule structure |
| 135 | D5 | AWS_KMS key, auto-rotation enabled, can old ciphertext still be decrypted? | Yes | ✅ | Yes — KMS keeps all old key material versions. Rotation doesn't break decryption. | — | KMS auto-rotation |
| 136 | D1 | IAM role used from unexpected country, visualize blast radius — which service? | Detective | ✅ | Detective — "visualize" / "blast radius" / "what else" = investigation. | — | Detective for investigation |
| 137 | D4 | Cross-account KMS: key policy grants B, identity policy allows, no SCP — result? | Succeeds | ✅ | Allowed — both sides satisfied, no SCP restriction. | Q81 | Cross-account KMS |
| 138 | D2 | Multi-step IR: isolate → snapshot → tag → notify — which service orchestrates? | Don't remember | ❌ | **Step Functions** — multi-step workflow orchestration. EventBridge triggers, Step Functions coordinates. | — | Step Functions for IR |
| 139 | D5 | After rotation, old DB connections still work — why? | AWSCURRENT and AWSPREVIOUS | ✅ | Old password valid as AWSPREVIOUS until next rotation cycle. | Q104 | Secrets Manager rotation |


---

### Session 23 — 2025-05-15

**Domains:** D1 Detection · D2 Incident Response (re-test — post-video drill)
**Score:** 8 ✅ · 1 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 140 | D1 | EC2 connecting to botnet IP, want finding auto-generated, zero code — which service? | GuardDuty | ✅ | GuardDuty — active threat = GuardDuty. Inspector = CVEs only. | Q132 | GuardDuty vs Inspector |
| 141 | D1 | "Which S3 buckets accessible by external accounts?" — which service? | IAM Access Analyzer | ✅ | IAM Access Analyzer (external access) — finds overly permissive resource policies. | — | Access Analyzer vs GuardDuty |
| 142 | D1 | GuardDuty finding type for credentials used from Tor exit node? | "TorIP" | ⚠️ | `UnauthorizedAccess:IAMUser/TorIPCaller` — pattern is ThreatPurpose:ResourceType/ThreatName. | Q116 | GuardDuty finding types |
| 143 | D1 | Compromised role, determine other resources accessed in 48hr, visualize blast radius? | Detective | ✅ | Detective — "visualize" / "blast radius" / "timeline" = always Detective. | Q109 | Detective for investigation |
| 144 | D1 | External access vs unused access in IAM Access Analyzer — one sentence each? | Confused the definitions | ❌ | External = "who outside can reach my resources?" Unused = "which permissions haven't been used in 90 days?" | — | Access Analyzer modes |
| 145 | D2 | Multi-step IR: isolate → snapshot → tag → notify — which service orchestrates? | Step Functions | ✅ | Step Functions — multi-step workflow orchestration. | Q138 | Step Functions for IR |
| 146 | D6 | Share DNS Firewall rule groups to all 200 member accounts — which service? | RAM | ✅ | RAM — sharing resources cross-account = RAM. | Q126 | RAM for resource sharing |
| 147 | D6 | Ensure all ALBs across 200 accounts have same WAF rules, auto-remediate — which service? | Firewall Manager | ✅ | Firewall Manager — "ensure/enforce" + auto-remediate = FM. | Q130 | Firewall Manager vs RAM |
| 148 | D2 | Before full IR, what should you do first with the GuardDuty finding? | "Evaluate" | ⚠️ | **Validate findings** — assess scope, check false positives, confirm severity. Exam keyword = "validate" or "triage". | — | Validate findings (Task 2.2.3) |
| 149 | D3 | Dedicated Direct Connect, Layer 2 encryption — which feature? | MACsec | ✅ | MACsec — Layer 2 encryption on dedicated DX only. | — | MACsec |


---

### Session 24 — 2025-05-16

**Domains:** Cross-domain (re-test — red-priority weak areas drill)
**Score:** 2 ✅ · 1 ⚠️ · 2 ❌ (40% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 150 | D1 | 200 accounts, dashboard: unencrypted S3/EBS + CIS score, least overhead? | Security Hub | ✅ | Security Hub — FSBP + CIS benchmark, org-wide, one-click. | Q108 | Security services comparison |
| 151 | D4 | 600 customers need kms:Decrypt, key policy at 28KB, onboard/offboard weekly? | KMS Grants | ✅ | KMS Grants — one API call per customer, no policy edits, scales without limit. | Q69 | RAM vs KMS Grants |
| 152 | D3 | Network Firewall TLS inspection — users get cert warnings — root cause? | "Import public CA in browser" | ⚠️ | Firewall's **private** CA cert not trusted by clients — distribute private CA to trust stores. Not a public cert — it's a MITM pattern with private CA. | Q122 | Network Firewall TLS inspection |
| 153 | D1 | SSE-KMS buckets, alert when external account decrypts, least overhead? | CloudTrail | ❌ | **GuardDuty S3 Protection** — "alert/detect" + "least overhead" = GuardDuty. CloudTrail is the log source, not the detection engine. | Q105 | Detect vs prevent (GuardDuty vs policy) |
| 154 | D1 | GuardDuty finding for credentials used from anonymizing proxy — finding type pattern? | Don't know | ❌ | `UnauthorizedAccess:IAMUser/TorIPCaller` — pattern: ThreatPurpose:ResourceType/ThreatName. | Q142 | GuardDuty finding types |


---

### Session 25 — 2025-05-16

**Domains:** D1 Detection (re-test — GuardDuty finding types + detect vs prevent drill)
**Score:** 2 ✅ · 0 ⚠️ · 3 ❌ (40% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 155 | D1 | GuardDuty finding type for EC2 mining Bitcoin? | "Mining:EC2/" | ❌ | `CryptoCurrency:EC2/BitcoinTool.B` — ThreatPurpose is CryptoCurrency, not Mining. | Q154 | GuardDuty finding types |
| 156 | D1 | SSE-KMS, want to KNOW when external account decrypts, least overhead — GuardDuty or CloudTrail? | CloudTrail | ❌ | **GuardDuty S3 Protection** — "detect/alert" + "least overhead" = GuardDuty. CloudTrail is the log source, not the detection engine. | Q153 | Detect vs prevent (GuardDuty vs policy) |
| 157 | D3 | Network Firewall TLS inspection CA cert — public, private, or self-signed? | Private | ✅ | Private CA cert — MITM pattern, distribute private CA to client trust stores. | Q152 | Network Firewall TLS inspection |
| 158 | D1 | Credentials used from unusual geographic location, notify, least overhead? | IAM Access Analyzer | ❌ | **GuardDuty** — active threat (unusual location) = GuardDuty. Access Analyzer finds misconfigurations, not real-time threats. | Q156 | Detect vs prevent (GuardDuty vs policy) |
| 159 | D1 | EC2 communicating with C2 server, alert with zero custom code? | GuardDuty | ✅ | GuardDuty — active threat + zero code = always GuardDuty. | Q140 | GuardDuty vs Inspector |


---

### Session 26 — 2025-05-16

**Domains:** Cross-domain exam-format practice (Week 11 — all domains)
**Score:** 17 ✅ · 0 ⚠️ · 3 ❌ (85% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 160 | D1 | 100 accounts SSE-KMS, alert external decryption, least overhead? | GuardDuty | ✅ | GuardDuty S3 Protection — detect + least overhead = GuardDuty. | Q156 | Detect vs prevent (GuardDuty vs policy) |
| 161 | D1 | GuardDuty finding type for EC2 mining cryptocurrency? | CryptoCurrency:EC2/something | ✅ | `CryptoCurrency:EC2/BitcoinTool.B` — ThreatPurpose correct. | Q155 | GuardDuty finding types |
| 162 | D1 | Credentials from Tor exit node — GuardDuty or Access Analyzer? | GuardDuty | ✅ | GuardDuty — active threat = always GuardDuty. | Q158 | Detect vs prevent (GuardDuty vs policy) |
| 163 | D4 | Block external S3 access org-wide without modifying bucket policies? | B: RCP | ✅ | RCP with PrincipalOrgID + PrincipalIsAWSService exception. | — | RCP for external access |
| 164 | D5 | Encrypt between EC2 (C6i), no code changes, least overhead? | C: Nitro | ✅ | Nitro inter-instance encryption — automatic, hardware-level. | — | Nitro encryption |
| 165 | D5 | Global Table + MRK, reads fail eu-west-1, primary key policy correct? | B: Replica key policy | ✅ | MRK policies independent per region — must update each. | Q123 | MRK independent key policies |
| 166 | D3 | Lambda private subnet, no NAT, needs Secrets Manager — minimum infra? (TWO) | B+D | ✅ | Interface VPC endpoint + SG allowing HTTPS 443. | — | VPC endpoints |
| 167 | D2 | EC2 communicating with C2, first action? | C: Deny-all SG | ✅ | Isolate first (deny-all SG) → snapshot → investigate. Never terminate. | — | IR sequence |
| 168 | D6 | 300 accounts, same WAF on all ALBs, auto-remediate, new accounts? | C: Firewall Manager | ✅ | Firewall Manager WAF policy — org-wide, auto-applies. | — | Firewall Manager |
| 169 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, session=Get+Put, bucket policy grants Delete — DeleteObject? | A: Denied | ❌ | **C: Allowed** — resource-based policy naming role directly bypasses session policy ceiling. | Q96 | Session policy bypass by resource-based policy |
| 170 | D1 | Normalize CloudTrail + VPC Flow + GuardDuty + third-party into single schema, own S3? | B: Security Lake | ✅ | Security Lake — OCSF format, your S3 bucket. | — | Security Lake / OCSF |
| 171 | D4 | SCP denies PutObject without Env tag, Config SLR writes snapshot (no tags)? | C: Fails | ✅ | SCP applies to SLRs — they're principals in your account. | Q120 | SCP applies to SLRs |
| 172 | D5 | Imported key material — how to rotate? | C: New key + import + alias | ✅ | Create new KMS key (EXTERNAL) → import → update alias. No auto-rotation. | Q114 | Imported key rotation |
| 173 | D4 | Compromised role, active sessions, revoke immediately? | B: Inline Deny TokenIssueTime | ✅ | Inline Deny with aws:TokenIssueTime < timestamp. Only way. | Q71 | STS session revocation |
| 174 | D4 | Okta Team attribute → EC2 access by team tag, no per-team policies? (TWO) | A+C | ✅ | Map attribute to session tag + ResourceTag condition. | Q94 | Session tags + ABAC |
| 175 | D5 | CreateGrant → partner AccessDenied immediately, works 30s later? | B: Grant token | ✅ | Pass grant token for immediate use before eventual consistency. | Q115 | KMS Grants eventual consistency |
| 176 | D4 | Third-party vendor assumes role, prevent confused deputy? | B: sts:ExternalId | ✅ | ExternalId in trust policy condition. | — | Confused deputy |
| 177 | D1 | Query CloudTrail 50 accounts, SQL, near real-time, dashboards, no S3/Athena? | B: CloudTrail Lake | ✅ | CloudTrail Lake — managed, SQL, near real-time, dashboards. | Q117 | CloudTrail Lake |
| 178 | D1 | EC2 querying DNS domains for Bitcoin mining pools — finding type? | D: Trojan | ❌ | **C: `Impact:EC2/BitcoinDomainRequest.Reputation`** — DNS query to crypto domain = Impact. Active mining = CryptoCurrency. | — | GuardDuty finding types (Impact vs CryptoCurrency) |
| 179 | D4 | Role in Account B, SCP denies GetObject, bucket policy in A grants role ARN — result? | B: Denied | ✅ | SCP cannot be bypassed by anything. | Q92 | SCP cannot be bypassed |
| 180 | D1 | Detect external S3 access (misconfig) + detect EC2 malicious IP (threat) — which TWO? | C+D | ✅ | Access Analyzer (misconfig) + GuardDuty (active threat). | — | Access Analyzer vs GuardDuty |
| 181 | D5 | Mask credit cards in CloudWatch Logs, no code changes, restrict who sees raw? | A: Macie | ❌ | **B: CloudWatch Logs data protection policy** + logs:Unmask. Macie = S3 only. | — | Data masking (Macie ≠ logs) |
| 182 | D3 | Dedicated Direct Connect, Layer 2 encryption? | B: MACsec | ✅ | MACsec — Layer 2 on dedicated DX only. | — | MACsec |


---

### Session 27 — 2025-05-16

**Domains:** Cross-domain exam-format practice (Week 11 — hardest topics)
**Score:** 19 ✅ · 0 ⚠️ · 5 ❌ (79% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 183 | D4 | RCP denies s3:* for non-org, ELB SLR writes access logs — blocked? | A: Denied | ❌ | **B: Allowed** — SLRs are structurally exempt from RCPs. | Q133 | RCP exemptions (SLR) |
| 184 | D4 | Validate policy for security issues BEFORE deploying — which service? | A: Policy Simulator | ❌ | **B: Access Analyzer policy validation** — pre-deployment check. Simulator tests existing policies. | — | Access Analyzer policy validation vs Simulator |
| 185 | D3 | EC2 private subnet needs S3 + DynamoDB, no internet — endpoint types? (TWO) | B+D | ✅ | Gateway endpoints for both (S3 + DynamoDB = only two Gateway endpoint services). | — | Gateway vs Interface endpoints |
| 186 | D5 | Secret rotated, open DB connections still work — why? | B: AWSPREVIOUS | ✅ | Old password valid as AWSPREVIOUS until next rotation cycle. | Q104 | Secrets Manager rotation |
| 187 | D1 | Role used from never-seen IP, zero code — which service? | B: Access Analyzer | ❌ | **C: GuardDuty** — unusual behavior happening NOW = active threat = GuardDuty. | Q158 | Detect vs prevent (GuardDuty vs Access Analyzer) |
| 188 | D5 | S3 immutable 3 years, root can't delete, auto-expire after? | B: Compliance mode | ✅ | Compliance mode + fixed retention. Nobody deletes, auto-expires. | Q91 | Object Lock Compliance mode |
| 189 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, attempt kms:Encrypt? | B: Denied — boundary | ✅ | Boundary ceiling doesn't include kms:* = denied at Gate 3. | — | Permission boundary ceiling |
| 190 | D1 | GuardDuty finding Policy:IAMUser/RootCredentialUsage — what happened? | B: Root API call | ✅ | Root account made an API call. Policy = risky config/usage. | — | GuardDuty finding types |
| 191 | D6 | Prevent disabling GuardDuty/CloudTrail/Flow Logs org-wide? | B: SCP Deny | ✅ | SCP with explicit Deny on disable actions. | Q119 | SCP for preventive guardrails |
| 192 | D5 | KMS auto-rotation: how long are old key material versions kept? | C: 90 days | ❌ | **B: Forever** — KMS keeps all versions until key deleted. No expiry. | — | KMS auto-rotation retention |
| 193 | D4 | RCP denies s3:* non-org, ELB SLR writes — blocked? (re-test) | Allowed | ✅ | SLRs structurally exempt from RCPs. | Q183 | RCP exemptions (SLR) |
| 194 | D4 | Validate policy before deploying — which service? (re-test) | Access Analyzer | ✅ | Access Analyzer policy validation = pre-deployment. | Q184 | Access Analyzer validation |
| 195 | D1 | Role from unusual IP, zero code — which service? (re-test) | GuardDuty | ✅ | Active threat = GuardDuty. | Q187 | Detect vs prevent |
| 196 | D5 | KMS auto-rotation: how long kept? (re-test) | Forever | ✅ | No expiration. All versions kept until key deleted. | Q192 | KMS auto-rotation retention |
| 197 | D4 | Cross-account KMS: key policy grants B root, identity allows, no SCP — result? | B: Allowed | ✅ | Both sides satisfied, no SCP restriction. | Q81 | Cross-account KMS |
| 198 | D4 | SCP denies RunInstances without CostCenter tag, dev launches without tag? | B: Denied | ✅ | SCP explicit Deny wins over identity Allow. | Q73 | SCP + RequestTag enforcement |
| 199 | D5 | Mask SSNs in CW Logs, no code changes, restrict raw access? (TWO) | B+C | ✅ | CW Logs data protection + logs:Unmask for authorized users. | — | Data masking |
| 200 | D4 | Session=GetObject only, cross-account bucket policy grants session PutObject — result? | B: Allowed | ✅ | Resource-based policy naming session bypasses session policy ceiling. | Q169 | Session policy bypass |
| 201 | D1 | Exfiltration:S3/AnomalousBehavior — what does it indicate? | B: Unusual data transfer | ✅ | Unusual data transfer pattern suggesting exfiltration. | — | GuardDuty finding types |
| 202 | D3 | Dedicated DX, encryption without latency? | B: MACsec | ✅ | MACsec — Layer 2, line-rate, dedicated only. | — | MACsec |
| 203 | D5 | CMK scheduled for deletion, discovered 3 days later — what to do? | B: CancelKeyDeletion | ✅ | CancelKeyDeletion → key moves to Disabled. Must re-enable. | — | KMS key deletion |
| 204 | D3 | Block C2 domain resolution VPC-wide immediately? | C: DNS Firewall BLOCK | ✅ | DNS Firewall BLOCK — kills query at DNS, VPC-wide. | — | DNS Firewall |
| 205 | D1 | Access Analyzer finds external SQS access + GuardDuty enabled — what does each tell you? | B: AA=misconfig, GD=active threat | ✅ | AA = "exposed". GD = "being exploited". Complementary. | — | Access Analyzer vs GuardDuty |
| 206 | D5 | Lambda has kms:GenerateDataKey in identity policy, key policy grants account root — succeeds? | C: Needs kms:Encrypt | ❌ | **B: Allowed** — root in key policy enables IAM delegation. GenerateDataKey IS correct for S3 envelope encryption. | — | KMS key policy delegation + GenerateDataKey |


---

### Session 28 — 2025-05-16

**Domains:** Cross-domain exam-format practice (Week 11 — mixed, targeting remaining gaps)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 207 | D4 | RCP denies kms:Decrypt non-org + PrincipalIsAWSService:false. CloudTrail decrypts — blocked? | B: Allowed | ✅ | CloudTrail IS an AWS service → condition doesn't match → Deny doesn't fire. | Q42 | RCP exemptions (PrincipalIsAWSService) |
| 208 | D3 | SG opened to 0.0.0.0/0 across 200 accounts, auto-detect + revert — which service? | A: GuardDuty | ❌ | **C: Firewall Manager SG audit policy** — misconfig + org-wide + auto-remediate = FM. GuardDuty detects threats, not misconfigs. | — | Firewall Manager SG audit |
| 209 | D3 | DNS Firewall: allow only 2 domains, block all else — rule structure? | B: ALLOW specific → BLOCK * | ✅ | ALLOW domains first (lowest priority number) → BLOCK * last. First match wins. | Q129 | DNS Firewall rule structure |
| 210 | D4 | Identity Center employee selects permission set — what does it become? | B: IAM role | ✅ | Permission set = IAM role auto-created in target account. | — | Identity Center |
| 211 | D5 | Lambda uploads to S3 with SSE-KMS — which KMS permission needed? | C+A | ✅ | **C only: kms:GenerateDataKey** — S3 uses envelope encryption. kms:Encrypt is for direct <4KB. | Q206 | KMS GenerateDataKey for S3 |
| 212 | D4 | Role chaining A→B→C, Role C MaxSessionDuration=12hr — actual max? | B: 1 hour | ✅ | Role chaining always resets to 1hr max. | — | Role chaining |
| 213 | D1 | GuardDuty Runtime Monitoring for EKS — what extra component needed? | B: Security agent | ✅ | Runtime Monitoring = only GuardDuty feature needing an agent. | — | GuardDuty Runtime Monitoring |
| 214 | D4 | Prevent CreateRole without boundary, org-wide? | B: SCP + iam:PermissionsBoundary | ✅ | SCP delegation pattern — force boundary on all role creation. | — | SCP + boundary delegation |
| 215 | D1 | CloudTrail log file modified — how detected? | C: Digest files + SHA-256 | ✅ | Log file integrity validation — digest files, validate via CLI. | — | CloudTrail integrity |
| 216 | D4 | "Can editor Bob update invoice-789 in tenant Acme?" — which service? | B: Verified Permissions | ✅ | VP + Cedar — app-level authz, not AWS API. | — | Verified Permissions |


---

### Session 29 — 2025-05-16

**Domains:** Cross-domain exam-format practice (Week 11 — final killer set, all weak spots)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 217 | D4 | RCP denies s3:* non-org. Config SLR writes + CloudTrail writes — which succeed? | A: Both | ✅ | Both — SLR exempt (structural) + CloudTrail exempt (PrincipalIsAWSService). Two different mechanisms. | Q183, Q207 | RCP exemptions (both paths) |
| 218 | D1 | EC2 actively sending traffic to Bitcoin mining pool — finding type? | B: CryptoCurrency:EC2/BitcoinTool.B | ✅ | Active mining = CryptoCurrency. DNS query only = Impact. | Q178 | GuardDuty finding types |
| 219 | D4 | Check new policy for security issues BEFORE attaching — which tool? | B: Access Analyzer validation | ✅ | Pre-deployment = Access Analyzer policy validation. Simulator = test existing. | Q184 | Access Analyzer validation |
| 220 | D5 | Mask PHI in CW Logs, only compliance officer sees raw — which TWO? | B+C | ✅ | CW Logs data protection + deny logs:Unmask broadly. | Q181 | Data masking |
| 221 | D4 | Session=GetObject only, bucket policy grants role PutObject — result? | B: Allowed | ✅ | Resource-based policy naming role bypasses session policy ceiling. | Q169, Q200 | Session policy bypass |
| 222 | D4 | SCP denies GetObject, bucket policy in Account A grants role ARN — result? | B: Denied | ✅ | SCP cannot be bypassed by anything. | Q179 | SCP cannot be bypassed |
| 223 | D5 | KMS rotated 3 times, decrypt data from original material 3 years ago? | B: Succeeds forever | ✅ | All versions kept forever, auto-routes via ciphertext metadata. | Q192 | KMS auto-rotation retention |
| 224 | D3/D1 | Detect overly permissive SGs + detect malicious IP comms — which TWO? | C+D | ✅ | FM SG audit (misconfig) + GuardDuty (active threat). | Q208 | FM vs GuardDuty |
| 225 | D5 | Key policy grants root only, Lambda identity has GenerateDataKey — succeeds? | B: Allowed | ✅ | Root = IAM delegation enabled. Identity policy grants the action. | Q206 | KMS key policy delegation |
| 226 | D1 | EC2 queries DNS for crypto domain, no connection yet — finding type? | D: Discovery | ❌ | **B: `Impact:EC2/BitcoinDomainRequest.Reputation`** — DNS query to crypto domain = Impact. Active mining = CryptoCurrency. Discovery = resource enumeration. | Q178 | GuardDuty finding types (Impact vs CryptoCurrency) |


---

### Session 30 — 2025-05-17

**Domains:** Cross-domain (re-test — red-priority gaps: Impact vs CryptoCurrency, session policy bypass)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 227 | D1 | EC2 DNS queries to pool.minergate.com, no TCP connection yet — ThreatPurpose? | Impact | ✅ | Impact — DNS query only = Impact. Active mining = CryptoCurrency. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 228 | D1 | EC2 actively sending traffic TO mining pool (connection established) — ThreatPurpose? | CryptoCurrency | ✅ | CryptoCurrency:EC2/BitcoinTool.B — active mining traffic. | Q218 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 229 | D4 | Identity=s3:*, session=GetObject only, same-account bucket policy grants role DeleteObject — succeeds? | Yes | ✅ | Resource-based policy naming role bypasses session policy ceiling. | Q169, Q221 | Session policy bypass by resource-based policy |
| 230 | D4 | Same as Q229 but caller's SCP denies DeleteObject — succeeds? | No | ✅ | SCP cannot be bypassed by anything. | Q222 | SCP cannot be bypassed |
| 231 | D1 | EC2 queries DNS for known botnet C2 domain, no connection — ThreatPurpose? | Impact | ✅ | DNS query only = Impact. Active C2 communication = Trojan. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |


---

### Session 31 — 2025-05-17

**Domains:** D1 Detection + Cross-domain (Week 11 — D1 focus, targeting 62% domain)
**Score:** 7 ✅ · 0 ⚠️ · 3 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 232 | D1 | GuardDuty enabled via delegated admin, one account has no findings despite production workloads — cause? | C: VPC Flow Logs not enabled | ❌ | **D: Workloads in a region where GuardDuty not enabled.** GuardDuty is regional. It reads VPC Flow Logs via internal feed — no need to enable them yourself. | — | GuardDuty is regional + agentless |
| 233 | D1 | Detect credentials used from never-seen IP, zero custom code — which service? | A: Access Analyzer | ❌ | **C: GuardDuty** — unusual IP = active threat happening NOW = GuardDuty. Access Analyzer = permission audit, not real-time threats. | Q187 | Detect vs prevent (GuardDuty vs Access Analyzer) |
| 234 | D1 | CloudTrail Lake vs Security Lake — how do they store data? | B: CT Lake managed, Security Lake your S3 | ✅ | CloudTrail Lake = managed data store. Security Lake = your S3 bucket (Iceberg/Parquet/OCSF). | — | CloudTrail Lake vs Security Lake |
| 235 | D2 | GuardDuty severity 8.5, EC2 communicating with C2 — first action? | C: Deny-all SG | ✅ | Isolate first (deny-all SG) → snapshot → investigate. Never terminate. | — | IR sequence |
| 236 | D1 | Query VPC Flow Logs in CloudWatch for top data sender — most efficient? | D: Detective | ❌ | **B: CloudWatch Logs Insights** — data already in CW, arbitrary aggregation query, no extra setup. Detective = investigate from a finding/entity, not open-ended queries. | — | CloudWatch Logs Insights vs Detective |
| 237 | D1/D6 | S3 logging enforcement across 300 accounts, auto-remediate within 1hr — which TWO? | A+D | ✅ | Config managed rule + auto-remediation (A) + organizational rule from delegated admin (D). | — | Config org rules + auto-remediation |
| 238 | D1 | EC2 private subnet, VPC Flow Logs not appearing in CloudWatch, CW agent installed — cause? | A: Flow log pointing to S3 | ✅ | VPC Flow Logs are VPC-level, don't use CW agent. Configuration determines destination. | — | VPC Flow Logs ≠ CW agent |
| 239 | D1/D2 | GuardDuty Recon finding, want to know what else attacker IP touched in 48hr — which service? | B: Detective | ✅ | Detective = "what else" / "blast radius" / "timeline". | — | Detective for investigation |
| 240 | D1/D4 | GuardDuty S3 Protection + RCP denying non-org, external attacker tries to read — what happens? | A: Both act | ✅ | RCP blocks access + GuardDuty detects the attempt. Independent services. | — | RCP + GuardDuty complementary |
| 241 | D1 | Detect CloudTrail StopLogging org-wide within 5 min, minimal setup — approach? | C: Org trail + EventBridge in mgmt account | ✅ | Organization trail + one EventBridge rule in management account. Detect ≠ prevent. | — | Org trail + EventBridge detection |


---

### Session 32 — 2025-05-17

**Domains:** Cross-domain exam-format practice (Week 11 — mixed, all domains)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 246 | D5 | Lambda uploads to S3 with SSE-KMS — which KMS permission? | C: kms:GenerateDataKey | ✅ | S3 envelope encryption = GenerateDataKey for uploads. kms:Encrypt is for direct <4KB. | — | KMS GenerateDataKey for S3 |
| 247 | D5 | KMS key scheduled for deletion 5 days ago, 30-day wait — recover? | B: CancelKeyDeletion → Disabled | ✅ | CancelKeyDeletion → key moves to Disabled. Must re-enable manually. | — | KMS key deletion recovery |
| 248 | D5/D6 | Prevent S3 buckets without encryption org-wide — approach? | D: Config rule + auto-remediation | ✅ | CreateBucket API doesn't have encryption settings — must detect and fix after. | — | Config auto-remediation |
| 249 | D3 | EC2 private subnet needs S3 + DynamoDB, minimize cost — endpoint types? | B+D: Gateway for both | ✅ | S3 and DynamoDB = only two Gateway endpoint services (free). | — | Gateway vs Interface endpoints |
| 250 | D2 | Access keys leaked to GitHub — correct response sequence? | B: Deactivate → CloudTrail → new key → delete old | ✅ | Stop bleeding first, then investigate, then replace. | — | Credential leak IR |
| 251 | D6 | Control Tower prevent disabling GuardDuty — which mechanism? | A: Config rule | ❌ | **B: SCP** — "prevent" = preventive control = SCP. Config = detective (detect after). Control Tower uses SCPs for preventive guardrails. | — | SCP for preventive guardrails (Control Tower) |
| 252 | D4 | RCP denies s3:* non-org, Config SLR writes snapshot — succeeds? | A: Yes — SLR exempt | ✅ | SLRs structurally exempt from RCPs. | Q183 | RCP exemptions (SLR) |
| 253 | D4 | Validate policy for security issues BEFORE deploying — which tool? | B: Access Analyzer validation | ✅ | Pre-deployment = Access Analyzer policy validation. Simulator = test existing. | Q184 | Access Analyzer policy validation |
| 254 | D5 | Secret rotated, old DB connection still works — why? | B: AWSPREVIOUS | ✅ | Old password valid as AWSPREVIOUS until next rotation cycle. | — | Secrets Manager rotation |
| 255 | D5 | Encrypt between C6i instances, zero config — mechanism? | C: Nitro | ✅ | C6i = Nitro-based. Automatic hardware-level encryption. | — | Nitro inter-instance encryption |


---

### Session 33 — 2025-05-17

**Domains:** Cross-domain exam-format practice (Week 11 — harder scenarios, multi-concept)
**Score:** 5 ✅ · 0 ⚠️ · 5 ❌ (50% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 256 | D4/D5 | Cross-account Lambda → S3+KMS, all policies correct, still AccessDenied — cause? | A: Missing sts:AssumeRole | ❌ | **C: Caller's SCP denies kms:Decrypt.** SCP follows the caller even when accessing another account's resources. AssumeRole already succeeded (error is on S3/KMS call). | Q70 | Cross-account KMS + SCP evaluation |
| 257 | D4 | Developers need CreateRole but can't escalate beyond s3+ec2 — mechanism? | B: SCP requiring PermissionsBoundary | ✅ | SCP forces boundary on all CreateRole calls. Boundary caps effective permissions. | — | Permission boundary delegation |
| 258 | D5 | DB credentials available in DR region if primary fails — which feature? | A: KMS MRK | ❌ | **B: Secrets Manager cross-region replication.** MRK replicates key material, not the secret itself. | — | Secrets Manager cross-region replication |
| 259 | D1 | Suspect CloudTrail log file modified — how to verify integrity? | B: Digest files + AWS CLI | ✅ | CloudTrail digest files with SHA-256 hashes, validate via CLI. | — | CloudTrail integrity validation |
| 260 | D5 | S3 immutable 7 years, root can't delete, auto-expire — config? | B: Compliance mode | ✅ | Compliance mode = fixed period, nobody deletes, auto-expires. | — | Object Lock Compliance mode |
| 261 | D3/D4 | Enforce IMDSv2 org-wide, prevent non-compliant launches — approach? | B: Config + auto-remediation | ❌ | **A: SCP denying RunInstances unless MetadataHttpTokens=required.** "Prevent" + "org-wide" = SCP. Config = detect and fix after. | Q251 | SCP for preventive enforcement |
| 262 | D3 | Lambda private subnet, no NAT, needs Secrets Manager — which TWO? | B+C | ✅ | Interface endpoint + SG allowing outbound HTTPS 443. | — | VPC endpoints + security groups |
| 263 | D4 | Identity Center + Okta + SCIM, new engineer joins Platform group — what happens? | C: Manual assignment needed | ❌ | **B: SCIM auto-syncs user + group membership.** Group already assigned to permission set → new user inherits access automatically. | — | SCIM provisioning (Identity Center) |
| 264 | D5 | Key policy grants root only, engineer has s3:GetObject but no KMS perms — can they read? | C: Yes, root delegates to all | ❌ | **B: No — root enables IAM delegation but doesn't grant access.** Each principal still needs explicit kms:Decrypt in their identity policy. | Q206 | KMS key policy root = delegation, not grant |
| 265 | D4 | Multi-tenant DynamoDB, restrict users to own tenant rows, no per-tenant policies? | C: dynamodb:LeadingKeys + PrincipalTag | ✅ | ABAC with LeadingKeys condition matching caller's TenantId tag. | — | ABAC for DynamoDB multi-tenant |


---

### Session 34 — 2025-05-18

**Domains:** Cross-domain (re-test — Session 33 errors)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 266 | D4/D5 | Cross-account Lambda → S3+KMS, all correct, AccessDenied — cause? | B: Account B's SCP denies kms:Decrypt | ✅ | SCP follows the caller even when accessing another account's resources. | Q256 | Cross-account KMS + SCP evaluation |
| 267 | D5 | DB credentials available in DR region if primary fails — which feature? | B: Secrets Manager cross-region replication | ✅ | MRK replicates key material, not the secret itself. Secrets Manager replication replicates the secret. | Q258 | Secrets Manager cross-region replication |
| 268 | D3/D4 | Enforce IMDSv2 org-wide, prevent non-compliant launches — approach? | B: SCP denying RunInstances unless MetadataHttpTokens=required | ✅ | "Prevent" + "org-wide" = SCP. Config = detect and fix after. | Q261 | SCP for preventive enforcement |
| 269 | D4 | Identity Center + Okta + SCIM, new engineer joins Platform group — what happens? | B: SCIM auto-syncs user + group membership | ✅ | Group already assigned to permission set → new user inherits access automatically. | Q263 | SCIM provisioning (Identity Center) |
| 270 | D5 | Key policy grants root only, engineer has s3:GetObject but no KMS perms — can they read? | B: Fails — root enables delegation but doesn't grant | ✅ | Root in key policy enables IAM delegation. Each principal still needs explicit kms:Decrypt. | Q264 | KMS key policy root = delegation, not grant |


---

### Session 35 — 2025-05-18

**Domains:** D6 Governance (untested gaps — StackSets, Audit Manager, Artifact, Service Catalog, Conformance Packs)
**Score:** 2 ✅ · 0 ⚠️ · 3 ❌ (40% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 271 | D6 | HIPAA compliance, auto-collect evidence, generate report for auditor? | D: Artifact | ❌ | **B: Audit Manager** — collects YOUR evidence (Config, CloudTrail, Security Hub) and generates YOUR audit report. Artifact = AWS's compliance paperwork. | — | Audit Manager vs Artifact |
| 272 | D6 | Auditor needs AWS's PCI DSS Attestation of Compliance — where? | B: Artifact | ✅ | Artifact = download AWS's compliance reports/certificates. | — | AWS Artifact |
| 273 | D6 | Deploy GuardDuty + Config + CloudTrail across 150 accounts, auto for new accounts? | A: Firewall Manager | ❌ | **B: StackSets (service-managed, auto-deploy)** — FM only deploys firewall rules. StackSets deploys any resource. | — | StackSets vs Firewall Manager |
| 274 | D6 | Self-service S3/EC2 with encryption+logging baked in, devs don't need broad IAM? | C: StackSets | ❌ | **B: Service Catalog with launch role** — self-service = users pull. StackSets = admin pushes. Launch role means dev doesn't need resource permissions. | — | Service Catalog (self-service) |
| 275 | D6 | 30 Config rules as single unit + auto-remediation + org-wide from delegated admin? | D: Firewall Manager | ❌ | **B: Config conformance pack (organizational)** — bundle of rules + remediation as one unit. FM doesn't deploy Config rules. | — | Config conformance packs |


---

### Session 36 — 2025-05-18

**Domains:** D6 Governance (re-test — StackSets, Service Catalog, Audit Manager, Artifact, Conformance Packs)
**Score:** 3 ✅ · 0 ⚠️ · 2 ❌ (60% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 276 | D6 | Deploy GuardDuty + Config + CloudTrail across 200 accounts, auto for new accounts? | D: Conformance pack | ❌ | **B: StackSets (service-managed, auto-deploy)** — conformance packs deploy Config RULES, not enable services. StackSets deploys any resource. | Q273 | StackSets vs Conformance Pack |
| 277 | D6 | Self-service hardened EC2/S3, devs don't need broad IAM (ec2:RunInstances, s3:CreateBucket)? | D: SCP | ❌ | **B: Service Catalog with launch constraint** — SCP restricts, doesn't enable. Launch constraint lets Service Catalog assume a role with the permissions. | Q274 | Service Catalog (self-service) |
| 278 | D6 | Evidence that S3 encrypted + CloudTrail enabled, mapped to SOC 2 framework, generate report? | C: Audit Manager | ✅ | Audit Manager — collects YOUR evidence, maps to frameworks, generates YOUR report. | Q271 | Audit Manager vs Artifact |
| 279 | D6 | Proof that AWS infrastructure meets PCI DSS — where to get? | B: Artifact | ✅ | Artifact = download AWS's compliance reports/certificates. | Q272 | AWS Artifact |
| 280 | D6 | 25 Config rules + auto-remediation + single package + org-wide from delegated admin? | C: Organizational conformance pack | ✅ | Conformance pack = bundle of rules + remediation as one unit, org-wide. | Q275 | Config conformance packs |
