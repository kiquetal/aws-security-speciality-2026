# Maintenance Mode — Until Aug 27, 2026

> You're ready. This is decay prevention, not cramming.
> **NEW:** Never-seen blueprint topics now integrated into weekly drills and mocks.

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
| 1 | Jun 16-22 | Novel topics: ACM cross-region, IoT ThingName, Kinesis+OpenSearch, Config custom rules | — (recent Session 86-90 gaps) | ✅ 86% (S94) |
| 2 | Jun 23-29 | **NEVER-SEEN BLITZ 1:** API Gateway security, CF Field-Level Encryption, Inspector SBOM, Macie custom identifiers, S3 Access Grants | 4 new topics | ✅ 90% (Session 100) |
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

## Bi-Weekly (timed 65-question mock)

Each mock MUST include 5-8 questions from never-seen topics to guarantee coverage.

| # | Target Date | Source | Never-Seen Quota | Score | Status |
|---|---|---|---|---|---|
| Mock 1 | Jun 23 | Tutorials Dojo Set 3 (or similar) | Include 5 Qs: API GW, CF Field-Level, Inspector SBOM, Macie custom, WAF Bot | — | ⬜ |
| Mock 2 | Jul 7 | Tutorials Dojo Set 4 (or similar) | Include 5 Qs: VPC Lattice, CF Guard, State Manager, DataSync, DLM | — | ⬜ |
| Mock 3 | Jul 21 | Tutorials Dojo Set 5 (or similar) | Include 5 Qs: Resilience Hub, FIS, ARC, Well-Architected, CodeGuru | — | ⬜ |
| Mock 4 | Aug 4 | Tutorials Dojo Set 6 (or AWS official) | Include 8 Qs: all never-seen topics mixed | — | ⬜ |
| Mock 5 | Aug 18 | Final validation (any source) | Full coverage validation | — | ⬜ |

---

## Never-Seen Blueprint Topics Master List

> 18 topics from the official SCS-C03 blueprint with 0 questions in 912 attempts.
> All must be tested at least once before exam day.

| # | Topic | Blueprint Task | Week | Mock | Tested? |
|---|---|---|---|---|---|
| 1 | API Gateway security (authorizers, resource policies, mutual TLS) | Task 3.1 | W2 | M1 | ⚠️ S97 (5 Qs, 2 wrong) |
| 2 | VPC Lattice (service-to-service auth, auth policies) | Task 3.3 | W4 | M2 | ✅ S97 (2 Qs, 100%) |
| 3 | CloudFront Field-Level Encryption | Task 3.1 | W2 | M1 | ✅ S97 (2 Qs, 100%) |
| 4 | Inspector SBOM export | Task 3.2 | W2 | M1 | ⚠️ S97 (2 Qs, 1 wrong) |
| 5 | WAF Bot Control (token challenges, CAPTCHA) | Task 3.1 | W4 | M1 | ✅ S97 (2 Qs, 100%) |
| 6 | CloudFormation Guard (policy-as-code) | Task 6.2 | W3 | M2 | ✅ S97 (1 Q, 100%) |
| 7 | Systems Manager State Manager (desired-state) | Task 1.1 | W3 | M2 | ⚠️ S97 (1 Q, wrong) |
| 8 | Amazon Data Lifecycle Manager (EBS snapshots) | Task 5.2 | W5 | M2 | ✅ S97 (2 Qs, 100%) |
| 9 | AWS DataSync (secure data transfer) | Task 5.2 | W5 | M2 | ✅ S97 (1 Q, 100%) |
| 10 | Macie custom data identifiers (regex, keywords) | Task 1.1 | W2 | M1 | ✅ S97 (1 Q, 100%) |
| 11 | Resilience Hub (RTO/RPO assessment) | Task 2.1 | W7 | M3 | ✅ S94 (100%) |
| 12 | FIS (chaos engineering for IR testing) | Task 2.1 | W7 | M3 | ✅ S94 (100%) |
| 13 | Application Recovery Controller (zonal shift) | Task 2.1 | W7 | M3 | ✅ S94 (100%) |
| 14 | Amazon Q Developer / CodeGuru Security | Task 3.2 | W4 | M3 | ✅ S97 (1 Q, 100%) |
| 15 | Well-Architected Tool (security pillar) | Task 6.3 | W5 | M3 | ✅ S97 (2 Qs, 1 wrong then fixed) |
| 16 | Automated Forensics Orchestrator for EC2 | Task 2.1 | W7 | M4 | ✅ S95 (100%) |
| 17 | SageMaker AI notebooks for IR | Task 2.1 | W7 | M4 | ✅ S96 (1 wrong, then fixed S97) |
| 18 | EMR / EKS inter-node encryption | Task 5.1 | W5 | M4 | ⚠️ S97 (1 Q, wrong then fixed) |

---

## Pass Criteria

You're ready when:
- Mock scores consistently >= 80%
- No domain below 72%
- D1 Detection >= 78%
- All 18 never-seen topics tested at least once (check column above)
- Can recall 3 rules per cheat sheet section without looking

---

## If Motivation Drops

- You have 1,055 questions banked across 97 sessions. That's more than most people who pass.
- Dojo Test 2 was 72% — already above passing threshold.
- Session 97 tested 14/18 never-seen topics in ONE session. You're ahead of schedule.
- 72 hours of focused study. The exam is 2.8 hours. You've done 25x the exam time.
- August is insurance, not necessity.
