# SCS-C03 Blueprint Coverage Tracker

> Last updated: 2026-06-15 (Session 90, 912 questions)
> Purpose: Ensure every blueprint task has been tested before exam day.

## Legend
- ✅ Tested in questions (3+ correct)
- ⚠️ Tested but fewer than 3 correct attempts
- ❌ NEVER TESTED (0 questions in 912 attempts)

---

## CRITICAL: Never-Tested Blueprint Topics (18 items)

These are explicitly listed in the SCS-C03 exam guide but have ZERO coverage in your practice.

| # | Topic | Task | Domain | Scheduled |
|---|---|---|---|---|
| 1 | API Gateway security (authorizers, resource policies, mutual TLS, WAF) | 3.1 | D3 | Week 2 |
| 2 | VPC Lattice (service-to-service auth, auth policies, cross-account) | 3.3 | D3 | Week 4 |
| 3 | CloudFront Field-Level Encryption (encrypt specific POST fields) | 3.1 | D3 | Week 2 |
| 4 | Inspector SBOM export (software bill of materials) | 3.2 | D3 | Week 2 |
| 5 | WAF Bot Control (managed rule group, token challenges, CAPTCHA) | 3.1 | D3 | Week 4 |
| 6 | CloudFormation Guard (cfn-guard, policy-as-code for templates) | 6.2 | D6 | Week 3 |
| 7 | Systems Manager State Manager (desired-state associations) | 1.1 | D1 | Week 3 |
| 8 | Amazon Data Lifecycle Manager (automated EBS snapshot policies) | 5.2 | D5 | Week 5 |
| 9 | AWS DataSync (encrypted data transfer, scheduling, filtering) | 5.2 | D5 | Week 5 |
| 10 | Macie custom data identifiers (regex patterns, keyword lists) | 1.1 | D1 | Week 2 |
| 11 | AWS Resilience Hub (RTO/RPO assessment, compliance) | 2.1 | D2 | Week 7 |
| 12 | AWS Fault Injection Service (chaos engineering for IR) | 2.1 | D2 | Week 7 |
| 13 | Amazon Application Recovery Controller (zonal shift, readiness checks) | 2.1 | D2 | Week 7 |
| 14 | Amazon Q Developer / CodeGuru Security (pipeline scanning) | 3.2 | D3 | Week 4 |
| 15 | Well-Architected Tool (security pillar reviews) | 6.3 | D6 | Week 5 |
| 16 | Automated Forensics Orchestrator for EC2 (Step Functions + SSM) | 2.1 | D2 | Week 7 |
| 17 | SageMaker AI notebooks for IR (forensic analysis) | 2.1 | D2 | Week 7 |
| 18 | EMR / EKS inter-node encryption (in-transit between nodes) | 5.1 | D5 | Week 5 |

---

## D4: Identity & Access Management (20%) — ✅ MASTERED (82%)

All task statements fully covered. 243 questions, 199 correct.

---

## D5: Data Protection (18%) — ✅ WELL COVERED (77%)

167 questions, 129 correct. Gaps: CRR encryption context, DynamoDB+CMK=CreateGrant, S3 Batch regional.
**Never-seen:** Data Lifecycle Manager (#8), DataSync (#9), EMR inter-node (#18).

---

## D3: Infrastructure Security (18%) — ✅ WELL COVERED (79%)

105 questions, 83 correct. Recent gaps: GWLB GENEVE, IoT cert-bound.
**Never-seen:** API Gateway (#1), VPC Lattice (#2), CF Field-Level (#3), Inspector SBOM (#4), WAF Bot Control (#5), CodeGuru (#14).

---

## D1: Detection (16%) — ⚠️ WEAKEST DOMAIN (73%)

226 questions, 165 correct. Persistent gaps: detect vs prevent wording, EventBridge vs GuardDuty.
**Never-seen:** SSM State Manager (#7), Macie custom identifiers (#10).

---

## D2: Incident Response (14%) — ⚠️ LOW VOLUME (69%)

29 questions, 20 correct. Recent gaps: no-reboot AMI, credential leak sequence.
**Never-seen:** Resilience Hub (#11), FIS (#12), ARC (#13), Forensics Orchestrator (#16), SageMaker IR (#17).

---

## D6: Governance (14%) — ✅ COVERED (79%)

136 questions, 108 correct. Core patterns solid.
**Never-seen:** CloudFormation Guard (#6), Well-Architected Tool (#15).
