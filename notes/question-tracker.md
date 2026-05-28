# SCS-C03 Question Tracker

> Track every question attempted. Review ❌ and ⚠️ items before the exam.

---

## Quick Stats (Cumulative)

| Metric | Value |
|---|---|
| **Total Questions** | 557 |
| **✅ Correct** | 432 (78%) |
| **⚠️ Partial** | 23 (4%) |
| **❌ Wrong** | 102 (18%) |
| **Sessions** | 56 |
| **Re-tests Passed** | 204 of 247 |

## Domain Breakdown

| Domain | ✅ | ⚠️ | ❌ | Total | Score % | Weak? |
|---|---|---|---|---|---|---|
| D1: Detection | 81 | 5 | 33 | 119 | 68% | 🟡 |
| D2: Incident Response | 11 | 1 | 1 | 13 | 85% | 🟢 |
| D3: Infrastructure Security | 60 | 4 | 10 | 74 | 81% | 🟢 |
| D4: Identity & Access Management | 137 | 8 | 21 | 166 | 83% | 🟢 |
| D5: Data Protection | 68 | 3 | 14 | 85 | 80% | 🟢 |
| D6: Governance | 75 | 2 | 23 | 100 | 75% | 🟡 |

Legend: 🔴 < 50% — 🟡 50–79% — 🟢 ≥ 80%

## Weak Areas to Review

| Priority | Topic | Questions | Domain | Count |
|---|---|---|---|---|
| 🔴 1 | Detect vs prevent (GuardDuty vs policy) | Q100, Q105, Q153, Q156, Q158, Q546 | D1, D5 | 6 |
| 🔴 2 | GuardDuty finding types | Q116, Q142, Q154, Q155 | D1 | 4 |
| 🔴 3 | Network Firewall TLS inspection | Q35, Q87, Q152 | D3 | 3 |
| 🔴 4 | GuardDuty finding types (Impact vs CryptoCurrency) | Q178, Q226, Q489 | D1 | 3 |
| 🔴 5 | kms:ViaService + SCP | Q488, Q495, Q495 | D4, D5 | 3 |
| 🔴 6 | Security services comparison | Q5, Q24 | D1 | 2 |
| 🔴 7 | RAM vs KMS Grants | Q11, Q37 | D4 | 2 |
| 🔴 8 | Cross-account KMS + SCP evaluation | Q70, Q256 | D4 | 2 |
| 🔴 9 | Session policy bypass by resource-based policy | Q96, Q169 | D4 | 2 |
| 🔴 10 | Detect vs prevent (GuardDuty vs Access Analyzer) | Q187, Q233 | D1 | 2 |
| 🔴 11 | SCP for preventive enforcement | Q261, Q413 | D3 | 2 |
| 🔴 12 | KMS key policy root = delegation, not grant | Q264, Q503 | D5 | 2 |
| 🔴 13 | Service Catalog (self-service) | Q274, Q277 | D6 | 2 |
| 🔴 14 | StackSets no auto-remediation | Q283, Q439 | D6 | 2 |
| 🔴 15 | Firewall Manager auto-remediation | Q284, Q435 | D6 | 2 |
| 🔴 16 | RAM for sharing vs FM for enforcing | Q313, Q441 | D6 | 2 |
| 🔴 17 | EventBridge for API call detection | Q474, Q549 | D1 | 2 |
| 🔴 18 | Native org-wide deployment | Q483, Q492 | D6 | 2 |
| 🟡 19 | CloudTrail data vs management events | Q1 | D1 | 1 |
| 🟡 20 | Basic vs Advanced event selectors | Q2 | D1 | 1 |
| 🟡 21 | Troubleshooting (Task 1.3) | Q6 | D1 | 1 |
| 🟡 22 | Policy layers reference | Q7 | D4 | 1 |
| 🟡 23 | faq-ram-vs-rcp.md | Q12 | D4 | 1 |
| 🟡 24 | GuardDuty vs CloudTrail | Q13 | D1 | 1 |
| 🟡 25 | DNS Firewall | Q14 | D3 | 1 |
| 🟡 26 | Cross-account patterns | Q15 | D5 | 1 |
| 🟡 27 | CloudTrail Lake vs S3+Athena | Q23 | D1 | 1 |
| 🟡 28 | NACLs stateless | Q34 | D3 | 1 |
| 🟡 29 | RAM vs RCP | Q38 | D4 | 1 |
| 🟡 30 | RCP exemptions (SLR vs service principal) | Q39 | D4 | 1 |
| 🟡 31 | RCP exemptions (PrincipalIsAWSService) | Q42 | D4 | 1 |
| 🟡 32 | Cross-account KMS | Q53 | D4 | 1 |
| 🟡 33 | STS session revocation | Q62 | D4 | 1 |
| 🟡 34 | Session tags + ABAC | Q63 | D4 | 1 |
| 🟡 35 | SCP + RequestTag enforcement | Q68 | D4 | 1 |
| 🟡 36 | Session tags + ABAC (ResourceTag vs RequestTag) | Q72 | D4 | 1 |
| 🟡 37 | Session policy as ceiling | Q78 | D4 | 1 |
| 🟡 38 | SCP cannot be bypassed | Q83 | D4 | 1 |
| 🟡 39 | MRK independent key policies | Q84 | D5 | 1 |
| 🟡 40 | Object Lock Compliance vs Legal Hold | Q85 | D5 | 1 |
| 🟡 41 | Detect C2 = GuardDuty (not DNS Firewall) | Q106 | D1 | 1 |
| 🟡 42 | Imported key rotation procedure | Q114 | D5 | 1 |
| 🟡 43 | SCP for preventive guardrails | Q119 | D6 | 1 |
| 🟡 44 | RAM for resource sharing | Q126 | D6 | 1 |
| 🟡 45 | DNS Firewall rule actions | Q129 | D3 | 1 |
| 🟡 46 | GuardDuty vs Inspector | Q132 | D1 | 1 |
| 🟡 47 | DNS Firewall rule structure | Q134 | D3 | 1 |
| 🟡 48 | Step Functions for IR | Q138 | D2 | 1 |
| 🟡 49 | Access Analyzer modes | Q144 | D1 | 1 |
| 🟡 50 | Validate findings (Task 2.2.3) | Q148 | D2 | 1 |
| 🟡 51 | Data masking (Macie ≠ logs) | Q181 | D5 | 1 |
| 🟡 52 | RCP exemptions (SLR) | Q183 | D4 | 1 |
| 🟡 53 | Access Analyzer policy validation vs Simulator | Q184 | D4 | 1 |
| 🟡 54 | KMS auto-rotation retention | Q192 | D5 | 1 |
| 🟡 55 | KMS key policy delegation + GenerateDataKey | Q206 | D5 | 1 |
| 🟡 56 | Firewall Manager SG audit | Q208 | D3 | 1 |
| 🟡 57 | GuardDuty is regional + agentless | Q232 | D1 | 1 |
| 🟡 58 | CloudWatch Logs Insights vs Detective | Q236 | D1 | 1 |
| 🟡 59 | SCP for preventive guardrails (Control Tower) | Q251 | D6 | 1 |
| 🟡 60 | Secrets Manager cross-region replication | Q258 | D5 | 1 |
| 🟡 61 | SCIM provisioning (Identity Center) | Q263 | D4 | 1 |
| 🟡 62 | Audit Manager vs Artifact | Q271 | D6 | 1 |
| 🟡 63 | StackSets vs Firewall Manager | Q273 | D6 | 1 |
| 🟡 64 | Config conformance packs | Q275 | D6 | 1 |
| 🟡 65 | StackSets vs Conformance Pack | Q276 | D6 | 1 |
| 🟡 66 | DNS Firewall ALERT ≠ finding | Q295 | D1 | 1 |
| 🟡 67 | Security Lake vs CW Logs Insights | Q303 | D1 | 1 |
| 🟡 68 | Verified Access trust providers | Q336 | D3 | 1 |
| 🟡 69 | Signer revocation (job vs profile vs IAM) | Q339 | D4 | 1 |
| 🟡 70 | Cognito Identity Pool + KMS permissions | Q341 | D3 | 1 |
| 🟡 71 | GuardDuty suppression rules | Q372 | D1 | 1 |
| 🟡 72 | Access Analyzer unused + policy generation | Q374 | D4 | 1 |
| 🟡 73 | Secrets Manager rotation failure | Q376 | D5 | 1 |
| 🟡 74 | Cognito + DynamoDB ABAC (sub vs TenantId) | Q395 | D4 | 1 |
| 🟡 75 | Data perimeter (RCP blocks IN, SCP blocks OUT) | Q398 | D4 | 1 |
| 🟡 76 | EventBridge for fast detection | Q401 | D1 | 1 |
| 🟡 77 | Timeout vs Access Denied (SG troubleshooting) | Q418 | D3 | 1 |
| 🟡 78 | KMS is regional | Q423 | D5 | 1 |
| 🟡 79 | Default encryption vs bucket policy Deny | Q426 | D5 | 1 |
| 🟡 80 | RCP same-org evaluation | Q427 | D4 | 1 |
| 🟡 81 | Secrets Manager replication ≠ MRK | Q428 | D5 | 1 |
| 🟡 82 | SCP prevents disabling services | Q440 | D6 | 1 |
| 🟡 83 | RAM + FM complementary | Q442 | D6 | 1 |
| 🟡 84 | Full governance stack | Q445 | D6 | 1 |
| 🟡 85 | StackSets limitations | Q450 | D6 | 1 |
| 🟡 86 | FM SG common policy | Q454 | D6 | 1 |
| 🟡 87 | Delegated admin (all services) | Q462 | D6 | 1 |
| 🟡 88 | Proactive guardrail (CF Hook) | Q464 | D6 | 1 |
| 🟡 89 | No single governance service | Q486 | D6 | 1 |
| 🟡 90 | SCP can't inspect payload + RCP prevents consequence | Q515 | D1 | 1 |
| 🟡 91 | Access Analyzer + GuardDuty both fire | Q518 | D1 | 1 |
| 🟡 92 | EventBridge for fast detection + auto-revert | Q523 | D1 | 1 |
| 🟡 93 | Network FW for IP-level C2 block | Q526 | D3 | 1 |
| 🟡 94 | Detection + response architecture | Q532 | D1 | 1 |
| 🟡 95 | GuardDuty ≠ failed attempts | Q534 | D1 | 1 |
| 🟡 96 | Gateway endpoint policy as additional gate | Q535 | D5 | 1 |
| 🟡 97 | Cross-account KMS key policy must name external account | Q541 | D4 | 1 |
| 🟡 98 | GuardDuty ≠ failed attempts + Access Analyzer static analysis | Q545 | D1 | 1 |

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
| 37 | 2025-05-18 | Q281–Q295 | 12 | 0 | 3 | D6 Governance + D3/D4 (untested topics) + D1 Detection (retention check) | [Jump](#session-37--2025-05-18) |
| 38 | 2025-05-18 | Q296–Q305 | 9 | 0 | 1 | Cross-domain exam simulation (all domains) | [Jump](#session-38--2025-05-18) |
| 39 | 2025-05-18 | Q306–Q325 | 19 | 0 | 1 | Cross-domain exam simulation (all domains, hardest scenarios) | [Jump](#session-39--2025-05-18) |
| 40 | 2025-05-18 | Q326–Q330 | 5 | 0 | 0 | Cross-domain exam simulation (all domains, final validation) | [Jump](#session-40--2025-05-18) |
| 41 | 2025-05-19 | Q331–Q335 | 5 | 0 | 0 | Cross-domain (untested gaps — Bedrock, Cognito, OAC+KMS, Security Lake, VPC endpoints) | [Jump](#session-41--2025-05-19) |
| 43 | 2025-05-20 | Q360–Q369 | 10 | 0 | 0 | Cross-domain (killer set — remaining 🟡 weak areas) | [Jump](#session-43--2025-05-20) |
| 42 | 2025-05-19 | Q336–Q359 | 21 | 0 | 3 | Cross-domain (Signer, Verified Access, Cognito, hybrid, detection gaps) | [Jump](#session-42--2025-05-19) |
| 44 | 2025-05-20 | Q370–Q379 | 7 | 0 | 3 | Cross-domain killer exam simulation (all domains, novel scenarios) | [Jump](#session-44--2025-05-20) |
| 45 | 2025-05-22 | Q380–Q384 | 5 | 0 | 0 | Cross-domain (re-test — Session 44 errors + validation) | [Jump](#session-45--2025-05-22) |
| 46 | 2026-05-24 | Q385–Q394 | 10 | 0 | 0 | Cross-domain exam simulation (all domains, certification-level) | [Jump](#session-46--2026-05-24) |
| 47 | 2026-05-24 | Q395–Q404 | 7 | 1 | 2 | Cross-domain killer exam simulation (all domains, novel scenarios) | [Jump](#session-47--2026-05-24) |
| 48 | 2026-05-24 | Q405–Q414 | 9 | 0 | 1 | Cross-domain killer exam simulation (all domains, novel scenarios) | [Jump](#session-48--2026-05-24) |
| 49 | 2026-05-24 | Q415–Q429 | 10 | 0 | 5 | Cross-domain lightning rounds (all domains, novel scenarios) | [Jump](#session-49--2026-05-24) |
| 50 | 2026-05-25 | Q430–Q434 | 5 | 0 | 0 | Cross-domain (re-test — Session 49 errors + new killer) | [Jump](#session-50--2026-05-25) |
| 51 | 2026-05-25 | Q435–Q486 | 39 | 1 | 12 | D6 Governance (targeted drill — RAM vs FM, StackSets, Service Catalog, Audit Manager) | [Jump](#session-51--2026-05-25) |
| 52 | 2026-05-26 | Q487–Q505 | 19 | 0 | 6 | Cross-domain (hard drill — D1/D4/D5/D6 weak spots) | [Jump](#session-52--2026-05-26) |
| 53 | 2026-05-26 | Q506–Q515 | 9 | 0 | 1 | Cross-domain (re-test + killer uplift — all domains) | [Jump](#session-53--2026-05-26) |
| 54 | 2026-05-26 | Q516–Q530 | 12 | 0 | 3 | Cross-domain (killer uplift — hard novel scenarios) | [Jump](#session-54--2026-05-26) |
| 55 | 2026-05-26 | Q531–Q540 | 7 | 0 | 3 | Cross-domain (killer difficulty — multi-concept combos) | [Jump](#session-55--2026-05-26) |
| 56 | 2026-05-28 | Q541–Q555 | 11 | 1 | 3 |  | [Jump](#session-56--2026-05-28) |

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


---

### Session 37 — 2025-05-18

**Domains:** D6 Governance + D3/D4 (untested topics) + D1 Detection (retention check)
**Score:** 10 ✅ · 0 ⚠️ · 3 ❌ (77% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 281 | D6 | Deploy GuardDuty + Config + CloudTrail across 200 accounts, auto for new accounts? | C: StackSets | ✅ | StackSets (service-managed, auto-deploy) — deploys any resource. | Q276 | StackSets vs Conformance Pack |
| 282 | D6 | Junior dev needs VPC but only has servicecatalog:ProvisionProduct — how? | C: Service Catalog assumes launch role | ✅ | Launch constraint lets Service Catalog assume a role with the permissions. | Q277 | Service Catalog (self-service) |
| 283 | D6 | StackSet deployed Config, developer disables recorder manually — what happens? | D: Conformance pack re-enables | ❌ | **B: Nothing — StackSets doesn't auto-remediate.** Conformance pack remediates rule violations, not service disablement. | — | StackSets no auto-remediation |
| 284 | D6 | 200 accounts, same WAF on ALBs, auto for new accounts, re-apply if removed? | D: Conformance pack | ❌ | **C: Firewall Manager** — WAF rules + auto-remediate = FM. Conformance packs deploy Config rules, not WAF. | — | Firewall Manager auto-remediation |
| 285 | D3 | SG opened to 0.0.0.0/0 port 22, auto-revert across 300 accounts? | C: Firewall Manager SG audit | ✅ | FM SG audit policy — org-wide, auto-remediate overly permissive SGs. | Q208 | Firewall Manager SG audit |
| 286 | D6 | 15 new accounts join OU, need CloudTrail+Config+GuardDuty immediately, zero manual? | C: StackSets with auto-deploy | ✅ | StackSets targeting OU with auto-deploy = new accounts get stack automatically. | Q276 | StackSets auto-deploy |
| 287 | D6 | Platform team "Golden VPC", app teams self-provision without ec2:CreateVpc? | C: Service Catalog with launch constraint | ✅ | Self-service + no broad IAM = Service Catalog + launch constraint. | Q277 | Service Catalog (self-service) |
| 288 | D3 | Bedrock chatbot, prevent prompt injection + block PII in responses? | B: Bedrock Guardrails | ✅ | Guardrails filter input (prompt injection) and output (PII). | — | GenAI / Bedrock Guardrails |
| 289 | D4 | Mobile app, Cognito sign-in, needs temp AWS creds for S3 upload? | B: Cognito Identity Pool | ✅ | User Pool authenticates. Identity Pool vends temporary AWS credentials. | — | Cognito Identity Pool |
| 290 | D3 | Verify EC2 reachable from internet without sending traffic? | C: Network Access Analyzer | ✅ | Analyzes configs to find unintended network paths — no traffic needed. | — | Network Access Analyzer |
| 291 | D1 | SSE-KMS, alert external decryption, least overhead? | C: GuardDuty S3 Protection | ✅ | "Detect" + "least overhead" = GuardDuty. | Q156 | Detect vs prevent |
| 292 | D1 | EC2 active traffic to mining pool — ThreatPurpose? | B: CryptoCurrency | ✅ | Active mining = CryptoCurrency. | Q218 | GuardDuty finding types |
| 293 | D1 | EC2 DNS query to mining pool, no connection — ThreatPurpose? | C: Impact | ✅ | DNS query only = Impact. Active mining = CryptoCurrency. | Q226 | Impact vs CryptoCurrency |
| 294 | D1 | Credentials from never-seen location, zero code? | C: GuardDuty | ✅ | Active threat + zero code = GuardDuty. | Q233 | Detect vs prevent |
| 295 | D1 | Lambda DNS to C2 domain, want finding generated, no blocking? | A: DNS Firewall ALERT | ❌ | **B: GuardDuty** — DNS Firewall ALERT logs but doesn't produce findings. GuardDuty reads DNS logs + generates findings. | Q106 | DNS Firewall ALERT ≠ finding |


---

### Session 38 — 2025-05-18

**Domains:** Cross-domain exam simulation (all domains)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 296 | D4 | Block external S3 access org-wide without modifying bucket policies? | B: RCP + PrincipalOrgID | ✅ | RCP blocks external callers on resource side. SCP can't stop outsiders. | — | RCP for external access |
| 297 | D3 | EC2 private subnet, no NAT, needs Secrets Manager — which TWO? | B+C: Interface endpoint + SG HTTPS | ✅ | Interface endpoint (Gateway = S3/DynamoDB only) + SG allowing 443. | — | VPC endpoints |
| 298 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, session=Get+Put — DeleteObject? | C: Denied — session policy | ✅ | Session policy ceiling — DeleteObject not in session = denied. | — | Session policy as ceiling |
| 299 | D5 | KMS key scheduled for deletion 5 days ago, 30-day wait — recover? | B: CancelKeyDeletion → Disabled | ✅ | CancelKeyDeletion during wait → Disabled → must re-enable. | — | KMS key deletion recovery |
| 300 | D4 | Identity Center + Okta + SCIM, new engineer joins Platform group? | B: SCIM auto-syncs | ✅ | Group already assigned → new user inherits access automatically. | — | SCIM provisioning |
| 301 | D2 | GuardDuty severity 8.5, EC2 communicating with C2 — first action? | C: Deny-all SG | ✅ | Isolate first → snapshot → investigate. Never terminate. | — | IR sequence |
| 302 | D1 | Investigate finding, blast radius, what else in 48hr? | C: Detective | ✅ | "Investigate" + "blast radius" + "timeline" = Detective. | — | Detective for investigation |
| 303 | D1 | Normalize CloudTrail + VPC Flow + GuardDuty + third-party, own S3? | C: CloudWatch Logs Insights | ❌ | **B: Security Lake** — "normalize" + "single schema" + "your S3" = Security Lake (OCSF). CW Insights queries existing CW data. | — | Security Lake vs CW Logs Insights |
| 304 | D4 | SCP denies PutObject without Env tag, Config SLR writes (no tags)? | C: Fails — SCP applies to SLRs | ✅ | SCP applies to SLRs — they're principals in your account. RCP exempts SLRs. | — | SCP applies to SLRs |
| 305 | D4 | Validate policy for security issues BEFORE deploying? | B: Access Analyzer validation | ✅ | Pre-deployment = Access Analyzer policy validation. Simulator = test existing. | — | Access Analyzer policy validation |


---

### Session 39 — 2025-05-18

**Domains:** Cross-domain exam simulation (all domains, hardest scenarios)
**Score:** 19 ✅ · 0 ⚠️ · 1 ❌ (95% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 306 | D1 | Query VPC Flow Logs in CW for top 10 source IPs — most efficient? | B: CloudWatch Logs Insights | ✅ | Data already in CW + aggregation query = CW Logs Insights. | Q236 | CW Logs Insights vs Detective |
| 307 | D3 | Lambda DNS to C2 domain, BLOCK resolution VPC-wide? | C: DNS Firewall BLOCK | ✅ | DNS Firewall BLOCK kills query at DNS, VPC-wide. | — | DNS Firewall BLOCK |
| 308 | D1 | Lambda DNS to C2 domain, want FINDING generated, no blocking? | B: GuardDuty | ✅ | GuardDuty generates findings. DNS Firewall ALERT just logs. | Q295 | DNS Firewall ALERT ≠ finding |
| 309 | D1 | Normalize CloudTrail + VPC Flow + WAF into OCSF, third-party SIEM reads from S3? | C: Security Lake | ✅ | "Normalize" + "OCSF" + "your S3" = Security Lake. | Q303 | Security Lake / OCSF |
| 310 | D4 | Identity=s3:*, session=GetObject only, bucket policy grants role DeleteObject — result? | B: Allowed — resource-based bypasses session | ✅ | Resource-based policy naming role bypasses session policy ceiling. | Q169 | Session policy bypass |
| 311 | D4 | Same as Q310 but SCP denies DeleteObject — result? | B: Denied — SCP cannot be bypassed | ✅ | SCP cannot be bypassed by anything. | — | SCP cannot be bypassed |
| 312 | D6 | Prove AWS data centers meet ISO 27001 — where? | B: Artifact | ✅ | AWS's compliance = Artifact. | — | AWS Artifact |
| 313 | D6 | Share DNS Firewall rule groups from security account to 15 new accounts? | A: Firewall Manager | ❌ | **B: RAM** — "share resources cross-account" = RAM. FM enforces rules, RAM shares them. | Q126 | RAM for sharing vs FM for enforcing |
| 314 | D6 | 20 Config rules + remediation + single unit + org-wide from delegated admin? | C: Organizational conformance pack | ✅ | Conformance pack = bundle + remediation as one unit. | — | Config conformance packs |
| 315 | D1 | Impact:EC2/BitcoinDomainRequest.Reputation — what happened? | B: DNS query to crypto domain, no connection | ✅ | Impact = DNS query only. CryptoCurrency = active mining. | Q226 | Impact vs CryptoCurrency |
| 316 | D4 | RCP denies s3:* non-org, ELB SLR writes access logs — blocked? | B: Allowed — SLR exempt from RCP | ✅ | SLRs structurally exempt from RCPs. | — | RCP exemptions (SLR) |
| 317 | D4 | Validate new policy + test existing role access — which TWO tools? | A+B: Access Analyzer + Simulator | ✅ | Validation = pre-deploy. Simulator = test existing. | — | Access Analyzer vs Simulator |
| 318 | D5 | Secret rotated, open DB connection still works — why? | B: AWSPREVIOUS | ✅ | Old password valid as AWSPREVIOUS until next rotation. | — | Secrets Manager rotation |
| 319 | D5 | KMS rotated 3 times, decrypt 3-year-old data? | B: Succeeds forever | ✅ | All versions kept forever, auto-routes via ciphertext metadata. | — | KMS auto-rotation retention |
| 320 | D3/D1 | Detect overly permissive SGs + detect malicious IP comms — which TWO? | C+B: FM SG audit + GuardDuty | ✅ | FM = misconfig remediation. GuardDuty = active threats. | — | FM + GuardDuty complementary |
| 321 | D5 | Imported key rotation procedure, keep old key for historical data? | C: New key + import + alias | ✅ | Create new key (EXTERNAL) → import → update alias → old stays. | — | Imported key rotation |
| 322 | D5 | Global Table + MRK, reads fail eu-west-1, primary key policy correct? | B: Replica key policy missing DynamoDB | ✅ | MRK policies independent per region. | — | MRK independent key policies |
| 323 | D4 | Cross-account same-org, RCP denies non-org — result? | B: Allowed — PrincipalOrgID matches | ✅ | Same-org = condition doesn't match = Deny doesn't fire. | — | RCP same-org evaluation |
| 324 | D3/D4 | Enforce IMDSv2 org-wide, block non-compliant launches? | B: SCP | ✅ | "Prevent" + "org-wide" = SCP. | — | SCP for preventive enforcement |
| 325 | D4 | Mobile app, Cognito sign-in, per-user S3 prefix — which TWO? | A+C: Identity Pool + IAM policy with sub | ✅ | Identity Pool vends creds + policy scoped to Cognito sub. | — | Cognito Identity Pool + per-user access |


---

### Session 40 — 2025-05-18

**Domains:** Cross-domain exam simulation (all domains, final validation)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 326 | D1/D2 | GuardDuty Trojan finding severity 8.9, contain + preserve + investigate 72hr — correct sequence? (THREE) | B+C+D | ✅ | Isolate (deny-all SG) → EBS snapshot → Detective for 72hr blast radius. Never terminate first. | — | IR sequence + Detective |
| 327 | D4 | Identity=s3:*+ec2:*+lambda:*, boundary=s3:*+ec2:*, session=Get+Put, same-account bucket policy grants role DeleteObject — result? | C: Allowed — resource-based bypasses session | ✅ | Resource-based policy naming role bypasses session policy ceiling. Boundary allows s3:* so no block there. | Q169 | Session policy bypass by resource-based policy |
| 328 | D5 | PHI in S3 with CMK, need: DR credentials, key in both regions, mask PHI in CW Logs — which THREE? | A+C+E | ✅ | MRK for cross-region key + Secrets Manager replication for credentials + CW Logs data protection for masking. | — | MRK + Secrets Manager replication + data masking |
| 329 | D3/D6 | 400 accounts, block malicious DNS org-wide, auto-apply new accounts, auto-remediate disassociation — which TWO? | A+B: RAM + Firewall Manager | ✅ | RAM shares rule group. FM enforces association + auto-remediates. They complement each other. | Q313 | RAM for sharing + FM for enforcing |
| 330 | D1/D6 | CIS compliance dashboard across 200 accounts + collect SOC 2 evidence for audit — which TWO services? | B+C: Security Hub + Audit Manager | ✅ | Security Hub = CIS dashboard. Audit Manager = YOUR evidence mapped to SOC 2. Artifact = AWS's reports. | — | Security Hub vs Audit Manager vs Artifact |


---

### Session 41 — 2025-05-19

**Domains:** Cross-domain (untested gaps — Bedrock, Cognito, OAC+KMS, Security Lake, VPC endpoints)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 331 | D3 | Bedrock chatbot: prevent prompt injection + block PII in responses + restrict model access — which TWO? | B+C | ✅ | Bedrock Guardrails (content) + IAM bedrock:InvokeModel (access). WAF ≠ LLM content. | — | Bedrock Guardrails + IAM |
| 332 | D4 | Mobile app, Cognito sign-in, per-user S3 folders + guest read-only — which TWO? | A+D | ✅ | User Pool authenticates + Identity Pool vends creds (auth role per-user, unauth role guest). | — | Cognito Identity Pool + per-user access |
| 333 | D5 | CloudFront + S3 origin + SSE-KMS, only CF can access — which TWO? | B+C | ✅ | OAC (not OAI) for SSE-KMS + KMS key policy granting CF service principal. OAI can't do KMS. | — | OAC + KMS key policy |
| 334 | D1 | Security Lake + Splunk — which THREE true statements? | A+B+F | ✅ | Your S3 (Parquet) + OCSF normalized + third-party OCSF ingestion. Not real-time (batch). | — | Security Lake / OCSF |
| 335 | D3/D5 | Private subnet (no NAT), needs Secrets Manager + S3 SSE-KMS upload — minimum infra? (THREE) | A+B+D | ✅ | Interface endpoint (Secrets Mgr) + Gateway endpoint (S3) + SG HTTPS. KMS endpoint not needed — S3 calls KMS server-side. | — | VPC endpoints + SSE-KMS server-side |


---

### Session 43 — 2025-05-20

**Domains:** Cross-domain (killer set — remaining 🟡 weak areas)
**Score:** 10 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 360 | D3/D4 | Verified Access: stolen laptop, block specific device without affecting others? | B: Update device trust provider | ✅ | Mark device non-compliant in device trust provider | Q336 | Verified Access trust providers |
| 361 | D6 | StackSets deployed Config, developer disables recorder — what happens? | B: Nothing — StackSets no auto-remediation | ✅ | StackSets does not auto-remediate drift | Q283 | StackSets no auto-remediation |
| 362 | D1 | GuardDuty finding `Trojan:EC2/DriveBySourceTraffic!DNS` — what does !DNS mean? | B: Finding from DNS log analysis | ✅ | !suffix = data source used for detection | — | GuardDuty finding structure |
| 363 | D4/D5 | Cross-account S3+KMS, all policies correct, still fails — cause? | B: Account B's SCP denies kms:Decrypt | ✅ | SCP follows the caller | Q256 | Cross-account KMS + SCP evaluation |
| 364 | D6 | Self-provision hardened RDS, devs don't need rds:CreateDBInstance? | B: Service Catalog with launch constraint | ✅ | Launch constraint = Service Catalog assumes role | Q274 | Service Catalog (self-service) |
| 365 | D1/D2 | After containment, determine other resources accessed, visualize timeline? | C: Detective | ✅ | "What else" + "visualize" + "timeline" = Detective | Q109 | Detective for investigation |
| 366 | D5 | KMS rotated 3 times, decrypt original data from year 1? | B: Succeeds — auto-routes to correct version | ✅ | All versions kept forever, ciphertext metadata routes | Q192 | KMS auto-rotation retention |
| 367 | D3 | DNS Firewall: ALLOW 2 domains + ALERT crypto + BLOCK all — priority order? | B: ALLOW → ALLOW → ALERT → BLOCK | ✅ | First match wins, ALLOW specific first, BLOCK * last | Q134 | DNS Firewall rule structure |
| 368 | D4 | SCP denies RunInstances without tag, Config SLR launches (no tags) — result? | B: Fails — SCP applies to SLRs | ✅ | SLRs escape RCPs, NOT SCPs | Q97 | SCP applies to SLRs |
| 369 | D1/D5 | Prevent external decrypt + alert on attempts — which TWO? | D+B: RCP + GuardDuty | ✅ | RCP prevents, GuardDuty detects | Q100 | Detect vs prevent (RCP + GuardDuty) |

---

### Session 42 — 2025-05-19

**Domains:** Cross-domain (Signer, Verified Access, Cognito, hybrid, detection gaps)
**Score:** 18 ✅ · 0 ⚠️ · 3 ❌ (86% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 336 | D3/D4 | Verified Access: Okta group + device posture — which TWO enforce? | A+C | ❌ | **A+B**: Trust provider for Okta (identity) + trust provider for device management (posture). IAM doesn't control VA decisions. | — | Verified Access trust providers |
| 337 | D5 | Lambda uploads SSE-KMS, key policy grants root, role has GenerateDataKey — fails? | B: Should succeed | ✅ | Root enables delegation + identity has GenerateDataKey = both sides satisfied. Trick question. | Q206 | KMS key policy delegation |
| 338 | D1 | CryptoCurrency vs Impact finding — DNS query + active mining from same instance? | D: Different stages | ✅ | CryptoCurrency = active mining traffic. Impact = DNS query only. Different stages of same attack. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 339 | D4/D6 | Signer: developer left, backdoored Lambda found — most targeted remediation? | D: Remove IAM | ❌ | **B: Revoke specific signing job.** Remove IAM prevents future but doesn't invalidate existing artifact. | — | Signer revocation (job vs profile vs IAM) |
| 340 | D3 | Verify EC2 reachable from internet without sending traffic? | C: Network Access Analyzer | ✅ | "Any instance unintentionally reachable" = broad discovery = Network Access Analyzer. | — | Network Access Analyzer vs Reachability |
| 341 | D3/D4 | Cognito + S3 per-user + SSE-KMS — what additional config? (TWO) | B+C | ❌ | **A+B**: Identity Pool auth role needs kms:GenerateDataKey (mobile app calls S3 directly, not Lambda). | — | Cognito Identity Pool + KMS permissions |
| 342 | D1/D3 | EC2 DNS to C2 domain — finding generated + block DNS? | B | ✅ | GuardDuty for finding + DNS Firewall BLOCK for prevention. DNS Firewall ALERT ≠ finding. | Q295 | GuardDuty + DNS Firewall complementary |
| 343 | D4/D5 | Signer: ENFORCE + allowed profile + invalidate one artifact — THREE? | A+E+F | ✅ | CSC ENFORCE (A) + attach to function (F) + revoke job for compromised artifact (E). | Q339 | Signer CSC + revocation |
| 344 | D5/D6 | S3 immutable 7yr + HIPAA evidence — THREE? | B+D | ✅ | Compliance mode (B) + Audit Manager HIPAA (D). Question design asked THREE but only two needed. | — | Object Lock + Audit Manager |
| 345 | D4/D3 | Prevent IMDSv1 launches org-wide — approach? | B: SCP | ✅ | "Prevent" + "org-wide" = SCP denying RunInstances unless MetadataHttpTokens=required. | Q261 | SCP for preventive enforcement |
| 346 | D1/D5 | Alert external KMS decryption, least overhead? | C: GuardDuty | ✅ | "Alert" + "least overhead" = GuardDuty S3 Protection. | Q156 | Detect vs prevent |
| 347 | D2/D4 | Exfiltrated role creds, stop attacker + keep app working? | B: Inline Deny TokenIssueTime | ✅ | Deny sessions before timestamp, app gets new creds after. | Q71 | STS session revocation |
| 348 | D6/D3 | 25 Config rules + remediation + single package + org-wide? | C: Conformance pack | ✅ | Organizational conformance pack from delegated admin. | Q275 | Config conformance packs |
| 349 | D3/D5 | Dedicated DX, Layer 2 encryption, zero overhead? | B: MACsec | ✅ | MACsec = Layer 2, dedicated only, line-rate. | — | MACsec |
| 350 | D4/D5 | Cross-account Lambda → S3+KMS, all correct, AccessDenied — cause? | B: Account B's SCP | ✅ | SCP follows the caller even when accessing another account's resources. | Q256 | Cross-account KMS + SCP |
| 351 | D1/D2 | Impact finding then CryptoCurrency finding 30min later — what happened? | B: DNS query → active mining | ✅ | Instance progressed from DNS resolution to active mining traffic. | Q226 | GuardDuty finding stages |
| 352 | D3/D6 | RAM shares rule group + FM policy, developer disassociates — what happens? | B: FM re-associates automatically | ✅ | FM auto-remediates. Developer can disassociate but FM re-applies. | Q329 | FM auto-remediation |
| 353 | D4 | RCP denies non-org s3:*. ELB SLR + CloudTrail + external attacker — which succeed? | B: SLR + CloudTrail only | ✅ | SLR exempt (structural) + CloudTrail exempt (PrincipalIsAWSService). Attacker blocked. | Q217 | RCP exemptions (both paths) |
| 354 | D5/D3 | Key material NEVER in AWS + native S3 SSE-KMS integration? | B: XKS | ✅ | External key store — material outside AWS, integrates via KMS API. | Q102 | XKS |
| 355 | D1/D4 | Access Analyzer finds external access + GuardDuty finds malicious IP — what does each tell you? | B: AA=exposed, GD=being exploited | ✅ | AA = misconfiguration. GD = active threat. Complementary. | Q205 | Access Analyzer vs GuardDuty |
| 356 | D2/D1 | After containment, determine roles used + buckets accessed + 72hr timeline? | C: Detective | ✅ | "What else" + "timeline" + "blast radius" = Detective. | Q109 | Detective for investigation |
| 357 | D6/D4 | Identity Center + Okta + SCIM, new engineer joins Platform group? | B: SCIM auto-syncs | ✅ | Group already assigned → new user inherits access automatically. | Q263 | SCIM provisioning |
| 358 | D5 | CreateGrant → partner AccessDenied immediately, works 30s later? | B: Grant token | ✅ | Pass grant token for immediate use before eventual consistency. | Q101 | KMS Grants eventual consistency |
| 359 | D3/D5 | Private subnet needs DynamoDB + S3, minimize cost — endpoint types? | B: Gateway for both | ✅ | S3 + DynamoDB = only two Gateway endpoint services (free). | Q249 | Gateway vs Interface endpoints |


### Session 44 — 2025-05-20

**Domains:** Cross-domain killer exam simulation (all domains, novel scenarios)
**Score:** 7 ✅ · 0 ⚠️ · 3 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 370 | D4/D6 | RCP block external S3 + exempt Config — which TWO? | B+C | ✅ | RCP with PrincipalOrgID + PrincipalIsAWSService exception | — | RCP + PrincipalIsAWSService |
| 371 | D4/D5 | SCP denies kms:Decrypt unless ViaService=s3, Lambda still works — why? | B: ViaService satisfied | ✅ | S3 calls KMS on behalf of caller, condition satisfied | — | kms:ViaService condition |
| 372 | D1 | GuardDuty enabled all regions, zero findings 90 days, active workloads — cause? | A: VPC Flow Logs not enabled | ❌ | **D: Suppression rule archiving findings.** GuardDuty reads Flow Logs via internal feed. Zero findings on active workloads = suppression rule. | — | GuardDuty suppression rules |
| 373 | D6 | Self-service VPC, no broad IAM, NOT auto for new accounts — which service? | B: Service Catalog | ✅ | Self-service + no broad IAM + not automatic = Service Catalog with launch constraint | — | Service Catalog (self-service) |
| 374 | D4 | Find unused permissions 90d + generate replacement policies, least overhead — which TWO? | C+A | ❌ | **A+B: Access Analyzer unused access + policy generation.** Config rule = role-level, not permission-level. | — | Access Analyzer unused + policy generation |
| 375 | D5 | CW Logs mask credit cards + only compliance sees raw + audit trail — which THREE? | A+B+E | ✅ | Data protection policy + logs:Unmask + audit destination | — | CW Logs data masking |
| 376 | D5 | Secrets Manager rotation, batch works, new Lambda fails on RDS — cause? | C: Missing GetSecretValue | ❌ | **D: Rotation Lambda failed to update DB password.** Error on DATABASE = credential problem, not IAM. | — | Secrets Manager rotation failure |
| 377 | D4/D6 | Data perimeter: block external IN + block exfil OUT + exempt services — which TWO? | A+B | ✅ | RCP (block outsiders) + SCP with ResourceAccount (block exfil) | — | Data perimeter (RCP+SCP) |
| 378 | D3/D5 | Private subnet, Secrets Manager + S3 SSE-KMS + CW Logs — minimum endpoints? | 3 | ✅ | Gateway (S3) + Interface (Secrets Mgr) + Interface (CW Logs). KMS not needed — S3 calls server-side. | — | VPC endpoints minimum |
| 379 | D1/D2 | Trojan finding severity 8.2, contain + preserve + investigate 72hr — sequence? | B,C,D | ✅ | Isolate (deny-all SG) → Snapshot (EBS) → Detective (72hr timeline) | — | IR sequence + Detective |


### Session 45 — 2025-05-22

**Domains:** Cross-domain (re-test — Session 44 errors + validation)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 380 | D1 | GuardDuty zero findings 6 months, junior created filter — investigate first? | C: Suppression rules with overly broad filter | ✅ | Suppression rules auto-archive findings. "Created filter to reduce noise" = suppression rule. | Q372 | GuardDuty suppression rules |
| 381 | D4 | Find unused permissions 90d + generate replacement policy, least overhead? | B: Access Analyzer unused + policy generation | ✅ | Two features, one service, least overhead. | Q374 | Access Analyzer unused + policy generation |
| 382 | D5 | Rotation completes, new Lambda "password auth failed" on RDS, ECS works — cause? | C: Rotation Lambda failed ALTER USER on RDS | ✅ | Error on DATABASE = rotation Lambda didn't update DB. ECS uses old connection (AWSPREVIOUS). | Q376 | Secrets Manager rotation failure |
| 383 | D5 | S3 CRR + MRK, decrypt fails in destination, replica exists — cause? | B: MRK replica key policy missing kms:Decrypt | ✅ | MRK policies independent per region — must update each separately. | Q84 | MRK independent key policies |
| 384 | D4/D1 | Block external S3 access org-wide + detect attempts — which TWO? | B+C: RCP + GuardDuty S3 Protection | ✅ | RCP prevents, GuardDuty detects. SCP can't stop external callers. | Q369 | Detect vs prevent (RCP + GuardDuty) |


### Session 46 — 2026-05-24

**Domains:** Cross-domain exam simulation (all domains, certification-level)
**Score:** 10 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 385 | D4/D6 | Block external S3 org-wide, exempt AWS services — which TWO? | B+D: RCP + PrincipalIsAWSService | ✅ | RCP with PrincipalOrgID + PrincipalIsAWSService exception | — | RCP + PrincipalIsAWSService |
| 386 | D1/D2 | EC2 C2 communication, determine other resources + roles + 72hr timeline? | B: Detective | ✅ | "Investigate" + "what else" + "timeline" = Detective | — | Detective for investigation |
| 387 | D5 | Key policy grants root only, Lambda has GenerateDataKey — upload result? | B: Succeeds — root enables delegation | ✅ | Root = IAM delegation. GenerateDataKey correct for S3 envelope encryption. | — | KMS key policy delegation |
| 388 | D3/D6 | WAF on all ALBs, auto-remediate if removed, new accounts — which service? | C: Firewall Manager | ✅ | FM = WAF rules + auto-remediate + org-wide | — | Firewall Manager auto-remediation |
| 389 | D1 | GuardDuty enabled, zero findings 90d, active workloads, Flow Logs not enabled — cause? | D: Suppression rule | ✅ | GuardDuty reads Flow Logs internally. Zero findings = suppression rule. | Q372 | GuardDuty suppression rules |
| 390 | D4/D5 | Cross-account S3+KMS, SCP denies kms:* unless ViaService=s3 — result? | B: Succeeds — ViaService satisfied | ✅ | S3 calls KMS on behalf of caller, condition satisfied | — | kms:ViaService + SCP |
| 391 | D6 | SOC 2: own evidence mapped to controls + AWS certification — which TWO? | B+C: Audit Manager + Artifact | ✅ | Audit Manager = YOUR evidence. Artifact = AWS's reports. | — | Audit Manager vs Artifact |
| 392 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, session=Get+Put, bucket policy grants Delete — result? | C: Allowed — resource-based bypasses session | ✅ | Same-account resource-based policy bypasses session policy ceiling | — | Session policy bypass |
| 393 | D3 | DNS Firewall: ALLOW 2 domains + ALERT crypto + BLOCK all — rule order? | B: ALLOW → ALLOW → ALERT → BLOCK | ✅ | First match wins, ALLOW specific first, BLOCK * last | — | DNS Firewall rule structure |
| 394 | D6 | Service Catalog, dev only has ProvisionProduct, VPC created — how? | B: Launch constraint role | ✅ | Launch constraint = Service Catalog assumes role with permissions | — | Service Catalog launch constraint |


### Session 47 — 2026-05-24

**Domains:** Cross-domain killer exam simulation (all domains, novel scenarios)
**Score:** 7 ✅ · 1 ⚠️ · 2 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 395 | D4/D3 | Multi-tenant DynamoDB, Cognito Identity Pool, Tenant A reads Tenant B — fix? (TWO) | A+C | ⚠️ | **C+D**: Map TenantId as session tag (C) + Verified Permissions for app-level authz (D). `sub` ≠ TenantId. | — | Cognito + DynamoDB ABAC (sub vs TenantId) |
| 396 | D2/D4 | Exfiltrated role creds, stop attacker + keep ECS running? | B: Inline Deny TokenIssueTime | ✅ | Deny sessions before timestamp, ECS gets new creds after. | Q71 | STS session revocation |
| 397 | D3 | Network Firewall TLS inspection — cert warnings — fix? | B: Distribute private CA to trust stores | ✅ | Private CA + MITM pattern — distribute to client trust stores. | Q87 | Network Firewall TLS inspection |
| 398 | D4/D6 | Data perimeter: block external IN + block exfil OUT — which TWO? | A+C | ❌ | **A+B**: RCP (block outsiders IN) + SCP with ResourceAccount (block insiders OUT). Bucket policy per-bucket doesn't scale. | — | Data perimeter (RCP blocks IN, SCP blocks OUT) |
| 399 | D5 | S3 CRR + MRK, decrypt fails in eu-west-1 — cause? | B: MRK replica key policy missing permissions | ✅ | MRK policies independent per region — must update each separately. | Q84 | MRK independent key policies |
| 400 | D4 | Identity Center + Okta + SCIM, new engineer joins Platform group — how? (TWO) | A+B: SCIM syncs + group already assigned | ✅ | SCIM auto-syncs. Group assigned to permission set → inherits access. | Q263 | SCIM provisioning |
| 401 | D1 | Detect StopLogging within 5 min, org trail exists, least overhead? | C: Config rule | ❌ | **B: EventBridge rule in management account.** Near real-time, one rule. Config is slower + heavier. | — | EventBridge for fast detection |
| 402 | D3/D5 | Private subnet, Secrets Manager + S3 SSE-KMS + CW Logs — minimum endpoints? | B: 3 | ✅ | Gateway (S3) + Interface (Secrets Mgr) + Interface (CW Logs). KMS not needed — S3 calls server-side. | — | VPC endpoints minimum |
| 403 | D5 | Rotation completes, new Lambda "password auth failed" on RDS, ECS works — cause? | B: Rotation Lambda failed ALTER USER on RDS | ✅ | Error on DATABASE = rotation Lambda didn't update DB. ECS uses old connection (AWSPREVIOUS). | Q376 | Secrets Manager rotation failure |
| 404 | D4 | Find unused permissions 90d + generate replacement policies, least overhead? | B: Access Analyzer unused + policy generation | ✅ | Two features, one service, least overhead. | Q374 | Access Analyzer unused + policy generation |


### Session 48 — 2026-05-24

**Domains:** Cross-domain killer exam simulation (all domains, novel scenarios)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 405 | D5 | CW Logs mask credit cards + only compliance sees raw — which TWO? | B+C: Data protection + deny Unmask | ✅ | Data protection policy + logs:Unmask for authorized users. | — | CW Logs data masking |
| 406 | D4 | External account, trust policy allows, RCP denies non-org STS — result? | C: Denied by RCP | ✅ | RCP evaluated on resource side, external caller blocked. | — | RCP blocks external AssumeRole |
| 407 | D3/D6 | Share DNS FW rule groups + auto-remediate disassociation — which TWO? | A+B: RAM + Firewall Manager | ✅ | RAM shares, FM enforces + auto-remediates. | Q313 | RAM for sharing + FM for enforcing |
| 408 | D3 | Lambda private subnet, restrict DNS to one domain, cheapest? | B: DNS Firewall | ✅ | DNS Firewall = cheapest domain filtering. Network Firewall overkill. | — | DNS Firewall cost-effective |
| 409 | D5 | KMS rotated 3 times, decrypt original data from 3 years ago? | C: Succeeds — auto-routes via ciphertext metadata | ✅ | All versions kept forever, auto-routes. | — | KMS auto-rotation retention |
| 410 | D1 | Detect public S3 org-wide, dashboard + least overhead — Config vs Security Hub? | B: Security Hub | ✅ | Security Hub wraps Config + dashboards + one-click org-wide. | Q5 | Security services comparison |
| 411 | D4 | SCP denies PutObject without tag, Config SLR writes (no tags) — result? | B: Fails — SCP applies to SLRs | ✅ | SLRs escape RCPs, NOT SCPs. | Q97 | SCP applies to SLRs |
| 412 | D4/D3 | Cognito per-user S3, pen tester crafts request to other user's prefix? | B: Fails — IAM policy restricts to caller's sub | ✅ | Policy Resource uses sub variable, mismatch = denied. | — | Cognito per-user isolation |
| 413 | D3/D4 | Enforce IMDSv2 org-wide, block non-compliant launches immediately? | A: Config + auto-remediation | ❌ | **B: SCP** denying RunInstances unless MetadataHttpTokens=required. "Prevent" = SCP. | Q261 | SCP for preventive enforcement |
| 414 | D5 | CloudFront + S3 SSE-KMS, only CF can access — which TWO? | B+C: OAC + KMS key policy for CF service principal | ✅ | OAC (not OAI) for SSE-KMS + KMS key policy granting CF. | — | OAC + KMS key policy |


### Session 49 — 2026-05-24

**Domains:** Cross-domain lightning rounds (all domains, novel scenarios)
**Score:** 10 ✅ · 0 ⚠️ · 5 ❌ (67% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 415 | D6/D1 | Prevent StopLogging from ever happening again, org-wide? | B: SCP Deny StopLogging | ✅ | "Prevent" = SCP. EventBridge = detect. Config = remediate. | Q401 | SCP for preventive enforcement |
| 416 | D1 | Query VPC Flow Logs in CW for top 10 source IPs — most efficient? | B: CloudWatch Logs Insights | ✅ | Data already in CW + aggregation = CW Logs Insights. | Q236 | CW Logs Insights vs Detective |
| 417 | D4/D6 | Enforce CostCenter tag on all EC2 launches org-wide, never create without? | B: SCP + RequestTag Null condition | ✅ | "Must have tag" + "never created without" + org-wide = SCP. | Q73 | SCP + RequestTag enforcement |
| 418 | D3 | Lambda timeout calling Secrets Manager, endpoint exists, endpoint SG correct — cause? | B: Endpoint policy denies | ❌ | **A: Lambda SG missing outbound HTTPS.** Timeout = network problem, not permissions. | — | Timeout vs Access Denied (SG troubleshooting) |
| 419 | D1 | Normalize CloudTrail + VPC Flow + GuardDuty + third-party, own S3, SIEM reads? | B: Security Lake | ✅ | "Normalize" + "single schema" + "your S3" = Security Lake (OCSF). | Q303 | Security Lake / OCSF |
| 420 | D3 | Bedrock: prevent prompt injection + block PII in responses + restrict model access — which TWO? | B+C: Guardrails + IAM | ✅ | Guardrails (content) + IAM bedrock:InvokeModel (access). | — | Bedrock Guardrails + IAM |
| 421 | D2 | EC2 C2 communication: contain + preserve + investigate 72hr — sequence? | B: Deny-all SG → EBS snapshot → Detective | ✅ | Isolate → snapshot → Detective for timeline. | — | IR sequence + Detective |
| 422 | D5 | KMS auto-rotation enabled, rotated once in 2 years — how many material versions? | B: 2 | ✅ | Original + one rotation = 2. All kept forever. | — | KMS rotation versions |
| 423 | D5/D4 | Cross-account KMS, key policy + identity policy correct, still Access Denied — cause? | Confused | ❌ | **C: Wrong regional endpoint.** KMS keys are regional — calling wrong region = key not found. | — | KMS is regional |
| 424 | D3/D6 | RAM shares DNS FW rule group, FM enforces, developer disassociates — what happens? | B: FM re-associates automatically | ✅ | FM auto-remediates. Developer can disassociate but FM re-applies. | Q329 | FM auto-remediation |
| 425 | D4/D5 | SCP denies kms:Decrypt unless ViaService=s3, developer calls KMS directly from CLI? | B: Fails — ViaService not satisfied | ✅ | Direct call has no ViaService context → SCP Deny fires. | — | kms:ViaService + SCP |
| 426 | D5 | Default encryption SSE-KMS + bucket policy Deny if wrong key header — upload without header? | A: Succeeds (default encryption) | ❌ | **B: Fails — bucket policy evaluates headers BEFORE default encryption applies.** | — | Default encryption vs bucket policy Deny |
| 427 | D4 | RCP denies non-org s3:*, same-account Lambda writes to own bucket — result? | D: Succeeds — RCPs don't apply same-account | ❌ | **B: Succeeds — RCPs DO apply, but Lambda's PrincipalOrgID matches → Deny doesn't fire.** | — | RCP same-org evaluation |
| 428 | D5 | Secrets Manager cross-region replication, source key is single-region (not MRK) — works? | A: Replication fails, needs MRK | ❌ | **C: Works — you specify a separate key in destination region. SM re-encrypts.** MRK not required. | — | Secrets Manager replication ≠ MRK |
| 429 | D4 | Employee terminated in Okta, revoke AWS access within minutes — mechanism? | A: SCIM deprovisioning | ✅ | SCIM auto-syncs lifecycle. Deactivate in Okta → removed from Identity Center within minutes. | — | SCIM deprovisioning |


### Session 50 — 2026-05-25

**Domains:** Cross-domain (re-test — Session 49 errors + new killer)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 430 | D3 | Lambda timeout calling Secrets Manager, endpoint exists, endpoint SG correct — cause? | B: Lambda SG missing outbound HTTPS | ✅ | Timeout = network problem. Lambda SG needs outbound 443. | Q418 | Timeout vs Access Denied (SG troubleshooting) |
| 431 | D5 | Default encryption SSE-KMS + bucket policy Deny if wrong key header — upload without header? | B: Fails — bucket policy evaluates before default encryption | ✅ | Bucket policy checks headers BEFORE default encryption applies. | Q426 | Default encryption vs bucket policy Deny |
| 432 | D4 | RCP denies non-org s3:*, same-account Lambda writes to own bucket — result? | B: Succeeds — PrincipalOrgID matches, Deny doesn't fire | ✅ | RCPs DO apply same-account, but condition logic determines outcome. | Q427 | RCP same-org evaluation |
| 433 | D5 | Secrets Manager cross-region replication, source key is single-region (not MRK) — works? | B: Works — specify different key in destination, SM re-encrypts | ✅ | MRK not required. SM re-encrypts with whatever key you specify. | Q428 | Secrets Manager replication ≠ MRK |
| 434 | D3/D6 | Prevent EC2 launch without IMDSv2 + detect existing IMDSv1 and fix — which TWO? | A+B: SCP + Config rule with SSM remediation | ✅ | SCP prevents. Config + SSM detects and fixes existing. | Q261, Q413 | SCP prevent + Config detect/fix |


### Session 51 — 2026-05-25

**Domains:** D6 Governance (targeted drill — RAM vs FM, StackSets, Service Catalog, Audit Manager)
**Score:** 11 ✅ · 0 ⚠️ · 5 ❌ (69% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 435 | D6 | WAF on all ALBs, auto-apply new accounts, re-attach if removed — which service? | C: Config conformance pack | ❌ | **B: Firewall Manager WAF policy.** FM manages WAF/SG/DNS FW/NF. Config can't deploy WAF. | Q284 | Firewall Manager auto-remediation |
| 436 | D6 | Self-provision Golden VPC, dev only has ProvisionProduct — how? | B: Service Catalog launch constraint role | ✅ | Launch constraint role has ec2:CreateVpc. | Q277 | Service Catalog (self-service) |
| 437 | D6 | 15 new accounts need GuardDuty + Config + CloudTrail, zero manual — which service? | C: StackSets with service-managed + auto-deploy | ✅ | StackSets deploys any resource, auto for new accounts. | Q276 | StackSets auto-deploy |
| 438 | D6 | Proof AWS meets ISO 27001 + YOUR evidence mapped to SOC 2 — which TWO? | B+C: Artifact + Audit Manager | ✅ | Artifact = AWS's reports. Audit Manager = YOUR evidence. | Q271 | Audit Manager vs Artifact |
| 439 | D6 | StackSets deployed Config, developer stops recorder — what happens? | C: Conformance pack re-enables | ❌ | **B: Nothing — StackSets doesn't auto-remediate.** | Q283 | StackSets no auto-remediation |
| 440 | D6 | Want Config to stay enabled, auto re-enable if stopped — approach? | B: Config rule + SSM remediation | ❌ | **C: SCP denying StopConfigurationRecorder.** Config can't remediate its own disablement. | — | SCP prevents disabling services |
| 441 | D6 | Share DNS FW rule groups from security account to 200 members — which service? | A: Firewall Manager | ❌ | **B: RAM.** "Share" = RAM. "Enforce" = FM. | Q313 | RAM for sharing vs FM for enforcing |
| 442 | D6 | DNS FW rule groups: share + enforce on all VPCs + re-associate if removed — which TWO? | B+D: FM + conformance pack | ❌ | **A+B: RAM + FM.** RAM shares, FM enforces. Config can't associate firewall resources. | Q329 | RAM + FM complementary |
| 443 | D6 | WAF on all ALBs, auto-remediate — need RAM? | B: No — FM creates WAF directly | ✅ | FM creates + deploys WAF Web ACLs directly. No RAM needed. | — | FM creates WAF directly |
| 444 | D6 | Control Tower prevent disabling GuardDuty/CloudTrail/Config — which mechanism? | B: Preventive guardrail (SCP) | ✅ | "Prevent" = SCP. Detective = Config rule. Proactive = CF Hook. | Q251 | SCP for preventive guardrails |
| 445 | D6 | GuardDuty + S3 encryption check + WAF + DNS FW + prevent CloudTrail disable — which FOUR? | A+C+D+E (missed B) | ❌ | **A+B+C+D+E** (all five needed). Missed conformance pack for "check + fix." | — | Full governance stack |
| 446 | D6 | Network FW policy: share to 200 accounts + enforce + recreate if deleted — which TWO? | A+B: RAM + FM | ✅ | RAM shares, FM enforces lifecycle. | — | RAM + FM for Network FW |
| 447 | D6 | Self-provision hardened RDS, dev only has ProvisionProduct — how? | B: Service Catalog launch constraint role | ✅ | Launch constraint role has rds:CreateDBInstance. | Q274 | Service Catalog (self-service) |
| 448 | D6 | Match verbs to RAM vs FM (4 items) | All correct (A, FM, FM, FM) | ✅ | "Make visible" = RAM. Ensure/enforce/re-apply/create = FM. | — | RAM vs FM verb test |
| 449 | D6 | Prevent unencrypted uploads + collect PCI evidence for auditor — which TWO? | A+D: SCP + Audit Manager | ✅ | SCP prevents. Audit Manager collects evidence for frameworks. | — | SCP + Audit Manager |
| 450 | D6 | Why can't StackSets do everything? Two limitations? | B+E: no remediation + no auto-deploy | ❌ | **B+C: no auto-remediation + can't share resources.** StackSets CAN auto-deploy to new accounts. | — | StackSets limitations |
| 451 | D6 | Shield Advanced on all CloudFront + ALBs across 150 accounts — which service? | B: Firewall Manager only | ✅ | FM creates Shield protections directly. No RAM needed. | — | FM creates directly (Shield) |
| 452 | D6 | TGW in shared-services account, 40 accounts need to attach — which service? | B: RAM | ✅ | TGW = infrastructure sharing = RAM. | — | RAM for TGW sharing |
| 453 | D6 | Detect overly permissive SGs (0.0.0.0/0 port 22) + auto-revoke across 300 accounts? | B: Firewall Manager SG audit | ✅ | FM SG audit = find + auto-remediate overly permissive SGs org-wide. | Q208 | Firewall Manager SG audit |
| 454 | D6 | Ensure baseline SG (deny all inbound) applied to all EC2 across 300 accounts? | B: RAM | ❌ | **A: Firewall Manager SG common policy.** FM creates the SG in each account. Nothing being shared. | — | FM SG common policy |
| 455 | D6 | "DNS FW rule group needs to be accessible to member accounts" — which service? | A: RAM | ✅ | "Accessible/visible/share" = RAM. | — | RAM verb signal |
| 456 | D6 | "DNS FW rule group must be associated with every VPC + re-associated if removed" — which? | B: Firewall Manager | ✅ | "Associated/enforce/re-apply" = FM. | — | FM verb signal |
| 457 | D6 | Network FW policy: Step 1 share, Step 2 enforce — correct sequence? | A: RAM shares, FM enforces | ✅ | RAM first (available), FM second (mandatory). | — | RAM + FM sequence |
| 458 | D6 | Prevent IGW creation + detect/fix flow logs + self-provision VPC + SOC 2 evidence — which FOUR? | A+B+C+D: SCP + conformance pack + Service Catalog + Audit Manager | ✅ | Four governance patterns in one question. | — | Full governance stack |
| 459 | D6 | Control Tower: someone modifies SCP outside CT — what happens? | B: Drift alert, no auto-fix | ✅ | CT detects drift but doesn't auto-revert. | — | Control Tower drift |
| 460 | D6 | Deny LeaveOrganization + CreateUser + StopLogging org-wide — where? | B: SCP on org root | ✅ | Restrict principals = SCP. | — | SCP for preventive guardrails |
| 461 | D6 | Block external S3 reads even with Principal:* bucket policy — where? | B: RCP on org root | ✅ | Block external callers on resources = RCP. | — | RCP for external access |
| 462 | D6 | Which services support delegated admin? (GuardDuty, SH, FM, Config, Audit Manager) | A+B+C+D (missed E) | ⚠️ | **F: All of them.** Every security service supports delegated admin. | — | Delegated admin (all services) |
| 463 | D6 | SCP denies DeleteBucket, user in management account calls it — result? | B: Allowed — mgmt account exempt | ✅ | Management account exempt from SCPs and RCPs. | — | Management account exempt |
| 464 | D6 | Block CF template deploying S3 without encryption — which guardrail type? | A: Preventive (SCP) | ❌ | **C: Proactive (CloudFormation Hook).** SCP blocks API calls. Hook validates template content. | — | Proactive guardrail (CF Hook) |
| 465 | D6 | Proactive guardrails — which statement true? | B: Validate CF templates before resources created | ✅ | Proactive = inspect IaC before deployment. | — | Proactive guardrail definition |
| 466 | D6 | Signed Lambda: validate template + detect unsigned + prevent disabling CSC — which THREE? | A+B+C: Proactive + Detective + SCP | ✅ | Three layers: proactive + detective + preventive. | — | Layered guardrails |
| 467 | D6 | Prevent GuardDuty disablement, never even briefly — approach? | B: SCP denying DeleteDetector + StopMonitoringMembers | ✅ | "Never even briefly" = preventive = SCP. Config has a gap. | Q440 | SCP prevents disabling services |
| 468 | D6 | CF template must include StorageEncrypted + DeletionProtection, fail before creation? | C: Proactive guardrail (CF Hook) | ✅ | "Template must include X" + "before creation" = CF Hook. | Q464 | Proactive guardrail (CF Hook) |
| 469 | D6 | Prevent unsigned Lambda deploy + detect missing CSC + prevent deleting CSC — THREE? | A+C+D: Proactive + Config + SCP | ✅ | Three layers: proactive (template) + detective (after) + preventive (API block). | — | Layered guardrails |
| 470 | D6 | RAM shared subnet, developer launches EC2 — who owns the instance? | B: Workload account (launcher) | ✅ | RAM shares infra, resources launched belong to launcher. | — | RAM shared VPC ownership |
| 471 | D6 | Match 5 scenarios to 5 services (SCP/Config/FM/SC/Hook) | All correct (A,B,C,D,E in order) | ✅ | Full D6 decision tree mapped correctly. | — | D6 governance decision tree |
| 472 | D6 | One sentence each: what makes SCP/conformance/FM/StackSets/SC unique? | All correct | ✅ | Block API / check+fix / firewall lifecycle / push infra / self-service+launch role. | — | D6 service differentiation |
| 473 | D6/D4 | RCP denies non-org s3:*, developer saves Principal:* bucket policy — what happens? | B: Policy saves, RCP blocks subsequent access | ✅ | RCP doesn't block PutBucketPolicy — blocks access at evaluation time. | — | RCP evaluation timing |
| 474 | D1/D6 | Detect PutBucketPolicy with Principal:* within 5 min + prevent external access — TWO? | D+A: GuardDuty + RCP | ❌ | **C+A: EventBridge on CloudTrail + RCP.** GuardDuty detects threats, not API calls. | — | EventBridge for API call detection |
| 475 | D6 | Service Catalog provisions VPC, developer removes flow logs 2 weeks later — what happens? | B: Nothing — SC doesn't monitor after provisioning | ✅ | Service Catalog = deploy only, no monitoring. | — | Service Catalog no post-deploy monitoring |
| 476 | D6 | Self-provision EC2 + auto-fix IMDSv2 + block ModifyInstanceMetadata — THREE? | A+B+C: Service Catalog + Config + SCP | ✅ | Three layers: self-service + detect/fix + prevent. | — | Layered governance |
| 477 | D6/D4 | SCP denies DeleteDetector, rogue admin in management account calls it — result? | B: Allowed — mgmt account exempt | ✅ | Management account always exempt from SCPs. | — | Management account exempt |
| 478 | D6 | Prevent member accounts from sharing resources externally via RAM — how? | D: Both SCP condition + Organizations setting work | ✅ | Two mechanisms: SCP with ram:RequestedAllowsExternalPrincipals, or org-level setting. | — | RAM external sharing controls |
| 479 | D6 | Audit Manager auto-collected evidence sources — which THREE? | A+B+C: Config + CloudTrail + Security Hub | ✅ | Auto-collected. Manual = screenshots, pen test reports. | — | Audit Manager evidence sources |
| 480 | D6 | StackSets service-managed, new account joins OU — what happens? | B: Stack instance auto-deploys (if auto-deploy enabled) | ✅ | Service-managed + auto-deploy = zero manual work. | — | StackSets auto-deploy |
| 481 | D6 | Control Tower detective guardrail "Detect S3 encryption" — what's underneath? | B: Config rule | ✅ | Detective guardrail = Config rule. Preventive = SCP. Proactive = CF Hook. | — | Control Tower guardrail internals |
| 482 | D6 | Conformance pack + Security Hub both flag unencrypted bucket — difference? | B: Conformance pack auto-fixes, Security Hub only reports | ✅ | Conformance pack has remediation. Security Hub = dashboard only. | — | Conformance pack vs Security Hub |
| 483 | D6 | Deploy Inspector across 200 accounts, auto for new — approach? | A: StackSets | ❌ | **B: Inspector delegated admin with auto-enable.** Native org support = use native, not StackSets. | — | Native org-wide deployment |
| 484 | D6 | Deploy GuardDuty across 300 accounts, auto for new — approach? | B: GuardDuty delegated admin with auto-enable | ✅ | Native org support → use native. | Q483 | Native org-wide deployment |
| 485 | D6 | Deploy GuardDuty + Config + CloudTrail + custom IAM roles, auto for new — approach? | C: StackSets + native delegated admin for each | ✅ | Mix: native for services that support it, StackSets for custom resources. | — | Hybrid deployment strategy |
| 486 | D6 | "ONE service that does everything" — which? | A: Control Tower | ❌ | **B: No single service does all.** CT doesn't share (RAM), deploy WAF (FM), or remediate (Config). | — | No single governance service |


### Session 52 — 2026-05-26

**Domains:** Cross-domain (hard drill — D1/D4/D5/D6 weak spots)
**Score:** 5 ✅ · 0 ⚠️ · 2 ❌ (71% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 487 | D1/D6 | Detect PutBucketPolicy within 5 min + prevent external access — TWO? | B+C: EventBridge + RCP | ✅ | EventBridge on CloudTrail for fast API detection + RCP for prevention. | Q474 | EventBridge for API call detection |
| 488 | D5/D4 | SCP denies kms:* unless ViaService=s3, developer calls KMS directly from CLI — result? | D: Account A's RCP blocks it | ❌ | **B: Fails — ViaService not satisfied, SCP Deny fires.** SCP follows the caller. | Q425 | kms:ViaService + SCP |
| 489 | D1 | EC2 DNS query to pool.supportxmr.com, no TCP connection — ThreatPurpose? | C: Trojan | ❌ | **B: Impact.** DNS query only = Impact. Active mining = CryptoCurrency. Active C2 = Trojan. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 490 | D3/D5 | Private subnet Lambda needs Secrets Manager + S3 SSE-KMS + CW Logs — minimum endpoints? | B: 3 | ✅ | Gateway (S3) + Interface (Secrets Mgr) + Interface (CW Logs). KMS not needed. | Q378 | VPC endpoints minimum |
| 491 | D4 | Identity=s3:*, session=GetObject only, same-account bucket policy grants role DeleteObject — result? | B: Allowed — resource-based bypasses session | ✅ | Same-account resource-based policy naming role bypasses session ceiling. | Q169 | Session policy bypass |
| 492 | D6 | Deploy Macie across 150 accounts, auto for new — approach? | D: Security Hub auto-enable | ❌ | **B: Macie delegated admin with auto-enable.** Each service manages its own org-wide deployment independently. | Q483 | Native org-wide deployment |
| 493 | D4/D5 | Global Table + MRK, reads fail eu-west-1, primary key policy correct — cause? | B: MRK replica key policy missing DynamoDB access | ✅ | MRK policies independent per region — must update each separately. | Q84 | MRK independent key policies |
| 494 | D1 | Impact finding then CryptoCurrency 30min later — what happened? | B: DNS lookup → active mining (connection established) | ✅ | Impact = DNS query. CryptoCurrency = active traffic. Two stages. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 495 | D4/D5 | SCP denies kms:Decrypt unless ViaService=s3, Lambda reads S3 object — result? | A: Fails — SCP blocks cross-account | ❌ | **B: Succeeds — ViaService = s3.us-east-1, condition FALSE, Deny doesn't fire.** | Q488 | kms:ViaService + SCP |
| 496 | D3/D1 | EC2 DNS to C2 domain — finding generated + block DNS — which TWO? | A+C: GuardDuty + DNS Firewall BLOCK | ✅ | GuardDuty for finding, DNS Firewall BLOCK for prevention. | Q295 | GuardDuty + DNS Firewall complementary |
| 497 | D6/D4 | SCP denies ScheduleKeyDeletion, member vs management account — results? | C: Member denied, management allowed | ✅ | Management account exempt from SCPs. | — | Management account exempt |
| 498 | D5 | Rotation completes, new Lambda auth fails on RDS, ECS works — cause? | B: Rotation Lambda failed to update DB password | ✅ | Secret changed but DB didn't. ECS uses old connection (AWSPREVIOUS). | Q376 | Secrets Manager rotation failure |
| 499 | D4 | RCP denies non-org s3:*, ELB SLR + CloudTrail + external attacker — which succeed? | B: SLR + CloudTrail only | ✅ | SLR exempt (structural) + CloudTrail exempt (PrincipalIsAWSService). Attacker blocked. | Q217 | RCP exemptions (both paths) |
| 494 | D1 | Impact finding then CryptoCurrency 30min later — what happened? | B: DNS lookup → active mining (connection established) | ✅ | Impact = DNS query. CryptoCurrency = active traffic. Two stages. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 495 | D4/D5 | SCP denies kms:Decrypt unless ViaService=s3, Lambda reads S3 object — result? | A: Fails — SCP blocks cross-account | ❌ | **B: Succeeds — ViaService = s3.us-east-1, condition FALSE, Deny doesn't fire.** | Q488 | kms:ViaService + SCP |
| 496 | D3/D1 | EC2 DNS to C2 domain — finding generated + block DNS — which TWO? | A+C: GuardDuty + DNS Firewall BLOCK | ✅ | GuardDuty for finding, DNS Firewall BLOCK for prevention. | Q295 | GuardDuty + DNS Firewall complementary |
| 497 | D6/D4 | SCP denies ScheduleKeyDeletion, member vs management account — results? | C: Member denied, management allowed | ✅ | Management account exempt from SCPs. | — | Management account exempt |
| 498 | D5 | Rotation completes, new Lambda auth fails on RDS, ECS works — cause? | B: Rotation Lambda failed to update DB password | ✅ | Secret changed but DB didn't. ECS uses old connection (AWSPREVIOUS). | Q376 | Secrets Manager rotation failure |
| 499 | D4 | RCP denies non-org s3:*, ELB SLR + CloudTrail + external attacker — which succeed? | B: SLR + CloudTrail only | ✅ | SLR exempt (structural) + CloudTrail exempt (PrincipalIsAWSService). Attacker blocked. | Q217 | RCP exemptions (both paths) |
| 500 | D4/D5 | Cross-account KMS + ViaService SCP + session policy only s3:GetObject — Lambda reads encrypted S3? | B: Succeeds — S3 calls KMS server-side, session policy doesn't block | ✅ | Role has kms:Decrypt + ViaService satisfied + session ceiling doesn't apply to server-side KMS. | — | Session policy + ViaService + server-side KMS |
| 501 | D3/D4 | Verified Access: stolen laptop, block only that device — action? | B: Mark device non-compliant in CrowdStrike | ✅ | Device trust provider = surgical device block. | Q336 | Verified Access trust providers |
| 502 | D1/D2 | Trojan finding severity 8.7 — stop + preserve + investigate 72hr — sequence? | B: Deny-all SG → EBS snapshot → Detective | ✅ | Isolate → preserve → investigate. Never terminate. | — | IR sequence + Detective |
| 503 | D5/D4 | Key policy grants root only, Lambda only has s3:GetObject (no kms:Decrypt) — reads encrypted object? | C: Succeeds — S3 handles server-side | ❌ | **B: Fails — Lambda needs explicit kms:Decrypt.** Root = delegation, not grant. | Q264 | KMS key policy root = delegation, not grant |
| 504 | D6 | Security Hub + GuardDuty + custom IAM role across 300 accounts — how many mechanisms? | C: 3 (SH native + GD native + StackSets for IAM role) | ✅ | Native for services that support it, StackSets for custom resources. | Q485 | Hybrid deployment strategy |
| 505 | D4/D5 | SCP denies kms:* unless ViaService=s3 — which TWO calls succeed? | A+C: Lambda via S3 read + Lambda via S3 upload | ✅ | ViaService set when S3 calls KMS on behalf of caller. Direct CLI = no ViaService = denied. | Q488 | kms:ViaService + SCP |


### Session 53 — 2026-05-26

**Domains:** Cross-domain (re-test + killer uplift — all domains)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 506 | D4/D5 | SCP denies kms:Decrypt unless ViaService=s3, developer calls KMS directly from CLI — result? | B: Denied — ViaService not satisfied | ✅ | Direct call has no ViaService context → SCP Deny fires. | Q488, Q495 | kms:ViaService + SCP |
| 507 | D1 | EC2 DNS query to xmr.pool.minergate.com, no TCP connection — ThreatPurpose? | B: Impact | ✅ | DNS query only = Impact. Active mining = CryptoCurrency. | Q489 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 508 | D5/D4 | Key policy grants root only, Lambda has s3:GetObject but no kms:Decrypt — reads SSE-KMS object? | B: Fails — needs explicit kms:Decrypt | ✅ | Root = delegation, not grant. Each principal needs explicit KMS perms. | Q503 | KMS key policy root = delegation, not grant |
| 509 | D4/D6 | RCP denies non-org sts:AssumeRole, external partner has trust policy — result? | B: Denied by RCP | ✅ | RCP blocks external AssumeRole regardless of trust policy. | — | RCP blocks external AssumeRole |
| 510 | D3/D5 | Lambda private subnet, monitoring endpoint exists, PutMetricData times out — cause? | A: Endpoint SG missing inbound HTTPS from Lambda SG | ✅ | Timeout = network. Interface endpoint SG must allow inbound 443. | Q418 | Timeout vs Access Denied (SG troubleshooting) |
| 511 | D1/D2 | Trojan:EC2/DropPoint!DNS severity 8.4, contain + preserve + keep API available — sequence? | B: Deny-all SG → EBS snapshot → deregister from ALB | ✅ | Isolate first → preserve evidence → remove from traffic. | — | IR sequence + ALB |
| 512 | D6 | DNS FW rule groups: share from security account + enforce on all VPCs + auto-remediate — which TWO? | A+B: RAM + Firewall Manager | ✅ | RAM shares, FM enforces + auto-remediates. | Q441, Q442 | RAM for sharing + FM for enforcing |
| 513 | D4 | Identity=s3:*+kms:*, boundary=s3:*+ec2:*, session=Get+Put, same-account bucket policy grants role DeleteObject — result? | C: Allowed — resource-based bypasses session | ✅ | Same-account resource-based policy naming role bypasses session + boundary ceiling. | Q169 | Session policy bypass by resource-based policy |
| 514 | D5/D3 | CloudFront + S3 + OAC + SSE-KMS, Access Denied — what's missing? | B: KMS key policy must grant kms:Decrypt to cloudfront.amazonaws.com | ✅ | OAC needs explicit KMS permission for CF service principal. | — | OAC + KMS key policy |
| 515 | D1/D6 | Prevent PutBucketPolicy with Principal:* + detect within 5 min — which TWO? | A+C: SCP + EventBridge | ❌ | **C+D: EventBridge + RCP.** SCP can't inspect API payload content. RCP prevents the consequence (external access). | Q474 | SCP can't inspect payload + RCP prevents consequence |


### Session 54 — 2026-05-26

**Domains:** Cross-domain (killer uplift — hard novel scenarios)
**Score:** 12 ✅ · 0 ⚠️ · 3 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 516 | D4/D5 | SCP denies kms:Decrypt+GenerateDataKey unless ViaService=s3 or secretsmanager, Lambda does 3 ops — which succeed? | B: Only S3 read + GetSecretValue | ✅ | ViaService set by S3 and SM. Direct kms:Decrypt has no ViaService → denied. | Q506 | kms:ViaService + SCP (multiple services) |
| 517 | D6/D4 | SCP denies ScheduleKeyDeletion, member admin + member root + management admin — which denied? | B: Only member admin + member root | ✅ | Management account exempt from SCPs. SCPs apply to member root. | — | Management account exempt |
| 518 | D1/D4 | Bucket policy grants external account, external downloads nightly — which services generate findings? | A: Only GuardDuty | ❌ | **C: Both Access Analyzer + GuardDuty.** AA flags external access (static). GD flags anomalous pattern (dynamic). | — | Access Analyzer + GuardDuty both fire |
| 519 | D5 | Rotation successful, new Lambda Access Denied on RDS, ECS works — cause? | B: Rotation Lambda failed ALTER USER on DB | ✅ | Secret changed but DB didn't. ECS uses AWSPREVIOUS. | Q376 | Secrets Manager rotation failure |
| 520 | D3/D6 | WAF on ALBs + DNS FW on VPCs, both via FM — which needs RAM? | B: Only DNS Firewall | ✅ | FM creates WAF directly. DNS FW rule group exists in another account → RAM shares first. | — | FM creates WAF directly, needs RAM for DNS FW |
| 521 | D4 | RCP denies non-org s3:*, same-org Account B Lambda PutObject to Account A bucket — result? | B: Allowed — PrincipalOrgID matches | ✅ | Same-org caller → condition FALSE → Deny doesn't fire. | Q427 | RCP same-org evaluation |
| 522 | D3/D5 | Lambda private subnet, direct kms:Decrypt from code, no KMS endpoint — result? | B: Add Interface endpoint for KMS + SG inbound 443 | ✅ | Direct KMS call needs network path. S3 SSE-KMS is server-side (no endpoint needed). | — | KMS endpoint needed for direct calls only |
| 523 | D1/D6 | Detect DeleteTrail/StopLogging within 2 min + auto-revert — architecture? | A: Config rule with auto-remediation | ❌ | **B: EventBridge in management account → Lambda.** Near real-time. Config is slower. | Q401 | EventBridge for fast detection + auto-revert |
| 524 | D4/D3 | Cognito per-user S3, pen tester crafts request to other user's prefix — result? | B: Fails — IAM policy restricts to caller's sub | ✅ | Policy variable resolves to caller's identity, not requested path. | — | Cognito per-user isolation |
| 525 | D5 | 7yr immutable + root can't delete + auto-expire + lawsuit preservation beyond 7yr — config? | A: Compliance mode + Legal Hold on lawsuit records | ✅ | Compliance = fixed period. Legal Hold = indefinite for litigation. | — | Object Lock Compliance + Legal Hold |
| 526 | D3/D1 | Trojan:EC2/C2Activity.B — block C2 VPC-wide + continue monitoring other instances — approach? | A: DNS Firewall BLOCK | ❌ | **B: Network Firewall DROP on C2 IP + GuardDuty continues.** C2Activity = active IP connection. DNS FW useless if IP hardcoded. | — | Network FW for IP-level C2 block |
| 527 | D4/D6 | SCP forces boundary, dev attaches AdministratorAccess, calls ec2:RunInstances — result? | B: Denied — boundary doesn't include ec2 | ✅ | Boundary = ceiling. ec2 not in boundary = denied regardless of identity policy. | — | Permission boundary delegation |
| 528 | D1 | Correlate GD + VPC Flow + WAF, SQL, own S3, single schema, SIEM reads — service? | B: Security Lake | ✅ | Multiple sources + OCSF + your S3 + subscriber model = Security Lake. | — | Security Lake |
| 529 | D4/D5 | Identity has kms:Decrypt, session policy only s3:GetObject, reads SSE-KMS object — result? | B: Succeeds — server-side KMS not gated by session policy | ✅ | Session policy gates caller's direct calls, not S3's internal KMS call. | — | Session policy + server-side KMS |
| 530 | D6 | CF template must include StorageEncrypted + DeletionProtection, fail before creation — guardrail type? | C: Proactive (CF Hook) | ✅ | "Validate template content before deploy" = CF Hook. SCP can't see template. | Q464 | Proactive guardrail (CF Hook) |


### Session 55 — 2026-05-26

**Domains:** Cross-domain (killer difficulty — multi-concept combos)
**Score:** 7 ✅ · 0 ⚠️ · 3 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 531 | D4/D5/D6 | SCP ViaService + RCP + key policy root + session policy — Lambda reads SSE-KMS object? | C: Succeeds — server-side KMS, ViaService satisfied | ✅ | Session policy doesn't gate server-side KMS. ViaService satisfied. Root enables delegation. | — | Full stack evaluation |
| 532 | D1/D3/D6 | Block DNS + detect C2 TCP + auto-block IP + org-wide — which FOUR? | C: DNS FW + Inspector + NF + StackSets | ❌ | **A: DNS FW + GuardDuty + Network FW + EventBridge→Lambda.** Inspector detects CVEs not C2. WAF can't block raw TCP. | — | Detection + response architecture |
| 533 | D4/D5 | Cross-account S3+KMS, SCP ViaService, Lambda reads via S3 — result? | A: Succeeds — ViaService satisfied cross-account | ✅ | ViaService set by S3 regardless of account boundary. | — | kms:ViaService cross-account |
| 534 | D1/D4/D6 | External trust policy + RCP + GuardDuty + Access Analyzer + EventBridge — which THREE true? | A+B+C | ❌ | **A+B+D.** GuardDuty doesn't fire on blocked AssumeRole attempts. EventBridge fires on CreateRole API call. | — | GuardDuty ≠ failed attempts |
| 535 | D5/D4/D3 | Secret works, S3 upload Access Denied, all IAM correct — cause? | D: KMS endpoint SG blocks | ❌ | **C: S3 Gateway endpoint policy denies PutObject.** Access Denied = permissions (endpoint policy), not network (timeout). | — | Gateway endpoint policy as additional gate |
| 536 | D1/D2/D4 | InstanceCredentialExfiltration.OutsideAWS — stop attacker + keep instance + new creds work? | B: Inline Deny TokenIssueTime | ✅ | Exfiltrated creds denied. IMDS refreshes new creds after timestamp. Instance stays up. | — | Credential exfiltration response |
| 537 | D6/D3/D4 | Prevent IMDSv1 + detect/fix existing + baseline SG + share NF policy — which FOUR? | A: SCP + Config/SSM + FM SG common + RAM | ✅ | SCP prevents. Config fixes. FM common creates SG. RAM shares NF policy. | — | Full governance stack |
| 538 | D5/D4 | Cross-account KMS, key policy grants Account B root, identity policy has Decrypt — result? | A: Succeeds — both sides grant | ✅ | Root in key policy enables IAM delegation in Account B. Both sides satisfied. | — | Cross-account KMS standard pattern |
| 539 | D1/D6 | CIS score + GD findings + Inspector CVEs + custom metric, least overhead — service? | B: Security Hub | ✅ | Aggregates all + CIS standard + cross-region + one-click org-wide. | — | Security Hub aggregation |
| 540 | D4/D3/D5 | Cross-account S3+KMS + SCP ViaService + RCP + session policy — Lambda reads? | B: Succeeds — all gates pass | ✅ | ViaService satisfied, RCP same-org passes, session doesn't gate server-side KMS. | — | 5-layer cross-account evaluation |


### Session 56 — 2026-05-28
**Score:** 11 ✅ · 1 ⚠️ · 3 ❌ (73% correct)
**Score:** 3 ✅ · 1 ⚠️ · 1 ❌ (60% correct)
**Score:** 2 ✅ · 0 ⚠️ · 1 ❌ (67% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 541 | D4/D5 | RCP + SCP ViaService + key policy grants only Account A root + Lambda in Account B reads SSE-KMS object cross-account — result? | A: Succeeds — all gates pass | ❌ | **C: Fails — key policy grants only Account A root, doesn't name Account B. Cross-account KMS requires key policy to explicitly name external account.** Root enables IAM delegation same-account only. | Q264, Q503 | Cross-account KMS key policy must name external account |
| 542 | D4/D5 | SCP ViaService + session policy (s3:Get+sm:Get only) + same-account SSE-KMS — 3 ops: S3 read, SM GetSecret, direct kms:Decrypt — which succeed? | B: Only #1 and #2 — ViaService satisfied, direct Decrypt has no ViaService | ✅ | Direct kms:Decrypt has no ViaService context → SCP Deny fires. Server-side KMS calls by S3/SM satisfy ViaService and aren't gated by session policy. | Q488, Q495 | kms:ViaService + SCP |
| 543 | D1/D3/D6 | 3 GD findings (Impact→CryptoCurrency→Trojan), block DNS org-wide + block C2 IP + detect mining — which THREE? | A+B+C: GuardDuty + RAM+FM DNS FW + Network FW via FM | ✅ | GD detects (zero code). RAM+FM shares+enforces DNS rules org-wide. Network FW drops hardcoded C2 IPs (DNS FW useless if no DNS query). | — | Detection + response architecture + RAM/FM complementary |
| 544 | D4/D5 | Session policy=GetObject only, same-account bucket policy grants role DeleteObject, SSE-KMS object — DeleteObject result? | B: Succeeds — resource-based bypasses session, DeleteObject doesn't need KMS | ✅ | Same-account resource policy naming role bypasses session ceiling. DeleteObject doesn't call KMS (no decrypt needed for deletion). | Q96, Q169 | Session policy bypass + DeleteObject no KMS |
| 545 | D1/D4/D5 | RCP blocks external + Access Analyzer + GuardDuty + KMS key policy — which THREE true? | A+B+F | ⚠️ | **A+B+E.** RCP blocks (A). AA fires on policy (B). GuardDuty doesn't fire on blocked attempts — no successful access = no finding (E). F is factually true but E is the exam-critical insight. | Q518, Q534 | GuardDuty ≠ failed attempts + Access Analyzer static analysis |
| 546 | D1 | SSE-KMS bucket, CISO wants to KNOW when external decrypts, least overhead? | A: CloudTrail data events + metric filter | ❌ | **C: GuardDuty S3 Protection.** "Detect/alert" + "least overhead" = GuardDuty. CloudTrail is the log source, not the detection engine. | Q100, Q105, Q153 | Detect vs prevent (GuardDuty vs policy) |
| 547 | D1 | EC2 resolves pool.minexmr.com via DNS, no TCP connection — ThreatPurpose? | B: Impact | ✅ | DNS query only = Impact. Active mining = CryptoCurrency. | Q226, Q489 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 548 | D1 | RCP blocks non-org s3:*, external tries GetObject, GuardDuty enabled — what's true? | B: GuardDuty does NOT generate finding — blocked = no successful access | ✅ | GuardDuty fires on successful anomalous access only. Blocked attempts = no finding. | Q534 | GuardDuty ≠ failed attempts |
| 549 | D1 | Detect PutBucketPolicy with Principal:* within 5 min, org trail exists, least overhead? | A: GuardDuty | ❌ | **C: EventBridge rule in management account.** "Detect specific API call" = EventBridge. GuardDuty detects behavior, not API calls. | Q474, Q523 | EventBridge for API call detection |
| 550 | D1 | EC2 actively sending mining traffic (TCP established, data flowing) — ThreatPurpose? | B: CryptoCurrency | ✅ | Active mining traffic = CryptoCurrency. DNS query only = Impact. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 551 | D6 | DNS FW rule group needs to be VISIBLE to 200 members — which service? | B: RAM | ✅ | "Visible/accessible/share" = RAM. | Q441 | RAM for sharing vs FM for enforcing |
| 552 | D6 | DNS FW rule group must be ASSOCIATED with every VPC, re-associated if removed — which? | B: Firewall Manager | ✅ | "Enforce/associate/re-apply" = FM. | Q442 | RAM + FM complementary |
| 553 | D6 | StackSets deployed Config, developer stops recorder — what happens? | B: Nothing — StackSets doesn't auto-remediate | ✅ | StackSets deploys but never auto-remediates. Use SCP to prevent. | Q283, Q439 | StackSets no auto-remediation |
| 554 | D6 | Deploy Macie across 150 accounts, auto for new — approach? | B: Macie delegated admin with auto-enable | ✅ | Native org support = use native, not StackSets. | Q483, Q492 | Native org-wide deployment |
| 555 | D6 | WAF on all ALBs, auto-apply new accounts, re-attach if removed — which service? | B: Firewall Manager | ✅ | FM creates WAF directly (no RAM) + auto-remediates. | Q284, Q435 | Firewall Manager auto-remediation |
