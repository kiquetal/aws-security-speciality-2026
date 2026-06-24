# Maintenance Mode — Until Aug 27, 2026

> You're ready. This is decay prevention, not cramming.
> **NEW:** Never-seen blueprint topics now integrated into weekly drills and mocks.
> **RULE:** After completing ANY weekly drill, mock exam, or never-seen topic test — update this file immediately (mark ✅, add scores, update dates). Don't wait for the user to remind you.

---

## Daily (30 seconds)

```bash
./scripts/daily-drill.sh
```
Read section → close eyes → recall 3 rules.

---

## Weekly (1 session, ~60 min)

25-question killer drill targeting untested or low-attempt topics + Session error re-tests + cross-domain combos.

| Week | Date | Focus | Never-Seen Included | Status |
|------|------|-------|---------------------|--------|
| 1 | Jun 16-22 | Novel topics: ACM cross-region, IoT ThingName, Kinesis+OpenSearch, Config custom rules | — (recent Session 86-90 gaps) | ✅ |
| 2 | Jun 23-29 | **NEVER-SEEN BLITZ 1:** API Gateway security, CF Field-Level Encryption, Inspector SBOM, Macie custom identifiers, S3 Access Grants | 4 new topics | ⬜ |
| 3 | Jun 30 - Jul 6 | D1 weak areas + CloudFormation Guard, SSM State Manager | 2 new topics | ⬜ |
| 4 | Jul 7-13 | **NEVER-SEEN BLITZ 2:** VPC Lattice, WAF Bot Control, CodeGuru Security, Private CA advanced | 3 new topics | ⬜ |
| 5 | Jul 14-20 | Cross-domain killer + Data Lifecycle Manager, DataSync, Well-Architected Tool, EMR inter-node | 4 new topics | ⬜ |
| 6 | Jul 21-27 | Re-test all remaining errors from Sessions 81+ | — (consolidation) | ⬜ |
| 7 | Jul 28 - Aug 3 | **NEVER-SEEN BLITZ 3:** Resilience Hub, FIS, Application Recovery Controller, Automated Forensics Orchestrator, SageMaker IR | 5 new topics | ⬜ |
| 8 | Aug 4-10 | D1 Detection final push (target 80%) | — | ⬜ |
| 9 | Aug 11-17 | Cross-domain full simulation (65 questions, all never-seen revisited) | Validation of all 18 | ⬜ |
| 10 | Aug 18-24 | Cheat sheet review only + 2 short drills | — | ⬜ |
| 11 | Aug 25-26 | REST. Read cheat sheet once. Sleep well. | — | ⬜ |

---

## Mocks (every 10 days — increased frequency for exam technique)

Each mock MUST be timed (170 min), include 5-8 never-seen topics, and followed by error categorization: (a) didn't know, (b) misread, (c) ran out of time.

| # | Target Date | Source | Never-Seen Quota | Score | Error Type | Status |
|---|---|---|---|---|---|---|
| Mock 1 | Jun 23 | Tutorials Dojo Set 3 | 5 Qs: API GW, CF FLE, SBOM, Macie, WAF Bot | 48% | 70% misread | ✅ |
| Mock 2 | Jun 22 | Tutorials Dojo Set 4 | 5 Qs: VPC Lattice, CF Guard, State Manager, DataSync, DLM | 64% | TBD | ✅ |
| Mock 3 | Jul 1 | Tutorials Dojo Set 5 | 5 Qs: Resilience Hub, FIS, ARC, Well-Architected, CodeGuru | — | — | ⬜ |
| Mock 4 | Jul 11 | Tutorials Dojo Set 6 | 8 Qs: all never-seen mixed | — | — | ⬜ |
| Mock 5 | Jul 21 | AWS Official Practice (if available) | Full coverage | — | — | ⬜ |
| Mock 6 | Aug 1 | Udemy Jon Bonso Set 2 (or similar) | 5 Qs: weakest sub-patterns | — | — | ⬜ |
| Mock 7 | Aug 11 | Final validation (any source) | Full coverage | — | — | ⬜ |
| Mock 8 | Aug 20 | Light 30-question confidence check | — | — | — | ⬜ |

---

## Never-Seen Blueprint Topics Master List

> 18 topics from the official SCS-C03 blueprint with 0 questions in 912 attempts.
> All must be tested at least once before exam day.

| # | Topic | Blueprint Task | Week | Mock | Tested? |
|---|---|---|---|---|---|
| 1 | API Gateway security (authorizers, resource policies, mutual TLS) | Task 3.1 | W2 | M1 | ✅ |
| 2 | VPC Lattice (service-to-service auth, auth policies) | Task 3.3 | W4 | M2 | ✅ |
| 3 | CloudFront Field-Level Encryption | Task 3.1 | W2 | M1 | ✅ |
| 4 | Inspector SBOM export | Task 3.2 | W2 | M1 | ✅ |
| 5 | WAF Bot Control (token challenges, CAPTCHA) | Task 3.1 | W4 | M1 | ✅ |
| 6 | CloudFormation Guard (policy-as-code) | Task 6.2 | W3 | M2 | ✅ |
| 7 | Systems Manager State Manager (desired-state) | Task 1.1 | W3 | M2 | ✅ |
| 8 | Amazon Data Lifecycle Manager (EBS snapshots) | Task 5.2 | W5 | M2 | ✅ |
| 9 | AWS DataSync (secure data transfer) | Task 5.2 | W5 | M2 | ✅ |
| 10 | Macie custom data identifiers (regex, keywords) | Task 1.1 | W2 | M1 | ✅ |
| 11 | Resilience Hub (RTO/RPO assessment) | Task 2.1 | W7 | M3 | ✅ |
| 12 | FIS (chaos engineering for IR testing) | Task 2.1 | W7 | M3 | ✅ |
| 13 | Application Recovery Controller (zonal shift) | Task 2.1 | W7 | M3 | ✅ |
| 14 | Amazon Q Developer / CodeGuru Security | Task 3.2 | W4 | M3 | ⬜ |
| 15 | Well-Architected Tool (security pillar) | Task 6.3 | W5 | M3 | ⬜ |
| 16 | Automated Forensics Orchestrator for EC2 | Task 2.1 | W7 | M4 | ⬜ |
| 17 | SageMaker AI notebooks for IR | Task 2.1 | W7 | M4 | ⬜ |
| 18 | EMR / EKS inter-node encryption | Task 5.1 | W5 | M4 | ⬜ |

---

## Pass Criteria

You're ready when:
- Mock scores consistently >= 75% (two in a row)
- No domain below 72%
- D1 Detection >= 78%
- All 18 never-seen topics tested at least once (check column above)
- Can recall 3 rules per cheat sheet section without looking
- Error categorization shows < 30% "misread" on last mock

---

## Mastered Patterns — DO NOT RE-TEST

> These have >= 3 consecutive correct answers. Skip them in all drills.
> Last updated: 2026-06-24

| Pattern | Correct Streak | Last Tested |
|---|---|---|
| mTLS CRL revocation (add CRL to S3 truststore) | 4x | Session 108 |
| mTLS cert expired (same CA, one fails) | 3x | Session 100 |
| GuardDuty Impact vs CryptoCurrency (DNS=Impact, TCP mining=Crypto) | 6x | Session 108 |
| EC2 EBS kms:CreateGrant | 5x | Session 100 |
| S3 multipart kms:Decrypt (reassembly) | 4x | Session 96 |
| GenerateDataKeyWithoutPlaintext (encrypted key for later) | 3x | Session 80 |
| DynamoDB CMK CreateGrant+DescribeKey | 4x | Session 94 |
| IoT cert revocation = instant (registry check) | 4x | Session 94 |
| DNS Firewall allow-list for DGA | 3x | Session 85 |
| Session policy same-account bypass (resource-based) | 6x | Session 108 |
| RCP SLR exempt | 5x | Session 108 |
| Cross-account KMS key policy must name external account | 6x | Session 108 |
| Session policy cross-account NO bypass | 4x | Session 77 |
| SCP cannot be bypassed | 5x | Session 108 |
| RCP scope = your resources only (outbound = SCP) | 3x | Session 100 |
| KMS key policy root = delegation not grant | 4x | Session 100 |
| Secrets Manager rotation failure = Lambda didn't ALTER USER on DB | 4x | Session 94 |
| Object Lock Compliance vs Governance | 4x | Session 84 |
| StackSets no auto-remediation | 3x | Session 108 |
| FM auto-remediates WAF/SG | 4x | Session 108 |
| Native org-wide deployment (delegated admin + auto-enable) | 4x | Session 108 |
| CRR rewrites encryption context to dest bucket | 3x | Session 92 |
| ViaService + SCP (direct call = denied) | 5x | Session 108 |
| Server-side KMS not gated by session policy | 4x | Session 108 |
| Deny-all SG for InsideAWS (not TokenIssueTime) | 4x | Session 86 |
| TokenIssueTime for OutsideAWS | 4x | Session 108 |
| Credential leak = Deny * on user (not just deactivate key) | 3x | Session 108 |
| EventBridge for fast specific API detection | 5x | Session 108 |
| GuardDuty S3 Protection for anomalous behavior | 5x | Session 108 |
| Access Analyzer = static policy (fires regardless of RCP/runtime) | 4x | Session 108 |
| GuardDuty does NOT fire on blocked attempts | 4x | Session 108 |
| S3 Batch Operations = regional | 4x | Session 94 |
| CW metric filter StopLogging = blind | 4x | Session 108 |
| Config org custom rule = Lambda resource-based policy | 4x | Session 94 |
| ACM regional (ALB=ALB region, CF=us-east-1) | 3x | Session 94 |
| No-reboot AMI for volatile memory | 3x | Session 93 |

---

## If Motivation Drops

- You have 1,055 questions banked across 97 sessions. That's more than most people who pass.
- Dojo Test 2 was 72% — already above passing threshold.
- Session 97 tested 14/18 never-seen topics in ONE session. You're ahead of schedule.
- 72 hours of focused study. The exam is 2.8 hours. You've done 25x the exam time.
- August is insurance, not necessity.
