# SCS-C03 Appendix B: Comparison of SCS-C02 → SCS-C03

> **Source:** https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-appendix-b.html
> **Blueprint ref:** All domains

## Domain Weight Changes (C02 → C03)

| Domain | SCS-C02 | SCS-C03 | Delta |
|--------|---------|---------|-------|
| D1: Detection (was Threat Detection + Logging) | 14% + 18% = 32% | 16% + 14% = 30% | -2% |
| D3: Infrastructure Security | 20% | 18% | -2% |
| D4: IAM | 16% | **20%** | **+4%** |
| D5: Data Protection | 18% | 18% | — |
| D6: Governance | 14% | 14% | — |

**Key takeaway:** IAM jumped from 16% → 20%, making it the heaviest domain. Infrastructure dropped 2%.

## New Content Added in SCS-C03

| Task | What's New | Exam Impact |
|------|-----------|-------------|
| **2.2.3** | Validate findings from AWS security services to assess scope/impact | Security Hub finding triage, GuardDuty severity assessment |
| **3.1.4** | OCSF format ingestion, third-party WAF rules | Know OCSF schema, WAF Marketplace rules |
| **3.2.7** | GenAI OWASP Top 10 for LLM Applications protections | NEW — guardrails for AI workloads |
| **5.1.3** | Inter-resource encryption in-transit (EMR, EKS, SageMaker AI, Nitro) | Know Nitro encryption, EKS inter-node TLS |
| **5.3.3** | Imported key material vs AWS-generated key material differences | KMS import: durability, rotation, expiration |
| **5.3.4** | Data masking (CloudWatch Logs data protection, SNS message data protection) | NEW service feature — know policies |
| **5.3.5** | Multi-Region key/cert management (KMS MRKs, Private CA) | Multi-Region keys, cross-region cert strategy |

## Content Removed from SCS-C03

| Removed Topic | Was In |
|--------------|--------|
| ASFF (AWS Security Finding Format) | Task 1.1 |
| AWS Security Incident Response Guide | Task 1.3 |
| Log format and components | Task 2.5 |
| Host-based security / firewalls / hardening | Task 3.3 |
| VPC Reachability Analyzer details | Task 3.4 |
| TCP/IP fundamentals (OSI model, UDP vs TCP) | Task 3.4 |
| Policy components (Principal, Action, Resource, Condition) | Task 4.2 |
| TLS concepts | Task 5.1 |
| S3 static website hosting | Task 5.2 |
| Security gaps via architectural reviews + cost analysis | Task 6.4 |

**Key takeaway:** Exam assumes you already know networking fundamentals, TLS, and basic policy structure. Focus shifted to higher-level architecture and newer services.

## Major Restructuring

- Old D1 (Threat Detection + Incident Response) + D2 (Logging/Monitoring) → New D1 (Detection) + D2 (Incident Response)
- D6 renamed: "Management and Security Governance" → "Security Foundations and Governance"

## Detailed Recategorization Map (C02 → C03)

This is the key to understanding where the exam shifted depth. Tasks that fan out to many C03 targets are broader; tasks that converge are deeper.

| SCS-C02 Task | Maps To (SCS-C03) | What This Tells Us |
|---|---|---|
| 1.1 (Threat Detection) | 1.1, 1.2, 2.1, 2.2 | Split across Detection + IR — old "detect & respond" is now two separate domains |
| 1.2 (Incident Response) | 1.1, 1.2 | IR monitoring pieces moved into Detection |
| 1.3 (Incident Response) | 2.1, 2.2 | Pure IR stayed in D2 |
| 2.1 (Logging/Monitoring) | 1.1 | Monitoring → Detection |
| 2.2 (Logging/Monitoring) | 1.1, 1.2, 1.3 | Expanded — now includes troubleshooting |
| 2.3 (Logging) | 1.2 | Straight move |
| 2.4 (Logging) | 1.2, 1.3 | Added troubleshooting dimension |
| 2.5 (Log formats) | 1.2 | Log format details removed but log design stays |
| 3.1 (Edge security) | 1.2, 3.1 | Edge logging moved to D1; edge controls stay in D3 |
| 3.2 (Network security) | 1.2, 3.3, 5.1, 6.2 | **Fanned out to 4 tasks** — network security now touches logging, data-in-transit, and IaC |
| 3.3 (Compute security) | 3.2, 5.3 | Compute hardening + secrets protection now linked |
| 3.4 (Network troubleshooting) | 1.2, 3.3 | VPC Reachability Analyzer details dropped; Network Access Analyzer stays |
| 4.1 (Authentication) | 4.1 | 1:1 — but now 20% weight |
| 4.2 (Authorization) | 4.2 | 1:1 — but policy component basics removed; deeper architecture expected |
| 5.1 (Data in transit) | 3.2, 3.3, 5.1 | TLS basics removed; inter-node encryption (Nitro, EKS) added |
| 5.2 (Data at rest) | 4.2, 5.2 | S3 authorization patterns moved to IAM domain |
| 5.3 (Data at rest) | 5.2 | Straight move |
| 5.4 (Secrets/keys) | 5.2, 5.3 | Split: encryption at rest vs key management/masking |
| 6.1 (Org management) | 4.2, 6.1 | SCPs/RCPs now tested in BOTH IAM and Governance |
| 6.2 (IaC deployment) | 6.2 | 1:1 |
| 6.3 (Compliance) | 1.1, 5.2, 6.3 | Compliance now touches monitoring AND data protection |
| 6.4 (Architecture review) | 2.1, 1.1, 6.3 | Cost analysis removed; security architecture review redistributed |

### Key Insights from the Recategorization

1. **Old C02 Task 3.2 (network security) exploded into 4 C03 tasks** — this means network security is now tested from logging, infrastructure, data-in-transit, AND IaC angles. Not harder per topic, but broader.
2. **IAM (D4) absorbed authorization patterns from D5 and D6** — S3 bucket policy authorization, SCPs/RCPs all converge into D4. This explains the 16%→20% weight jump.
3. **Troubleshooting is a new first-class concern** — C02 barely tested it. C03 has explicit troubleshooting in Tasks 1.3, 3.1, 3.2, 3.3, 4.1, 4.2.
4. **Detection (D1) absorbed most of old D2 (Logging)** — if you know logging well, you're covering 16% of the exam.
5. **Compliance is no longer siloed in D6** — it's tested through monitoring (1.1), data protection (5.2), and governance (6.3).

## Exam Gotchas from Changes

1. **GenAI security is now testable** (Task 3.2.7) — know Amazon Bedrock Guardrails, prompt injection, model access controls
2. **OCSF is testable** (Task 3.1.4) — know it's the schema for Security Lake
3. **Data masking is testable** (Task 5.3.4) — CloudWatch Logs data protection policies are new
4. **Nitro encryption** (Task 5.1.3) — inter-instance encryption without application changes
5. **ASFF removed** — but Security Hub still uses it; just won't ask about format details
6. **No more basic networking questions** — no OSI model, no TCP vs UDP
7. **Troubleshooting is everywhere** — expect "why is this failing?" scenarios across D1, D3, D4
