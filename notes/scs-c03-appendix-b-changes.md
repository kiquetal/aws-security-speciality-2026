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

## Exam Gotchas from Changes

1. **GenAI security is now testable** (Task 3.2.7) — know Amazon Bedrock Guardrails, prompt injection, model access controls
2. **OCSF is testable** (Task 3.1.4) — know it's the schema for Security Lake
3. **Data masking is testable** (Task 5.3.4) — CloudWatch Logs data protection policies are new
4. **Nitro encryption** (Task 5.1.3) — inter-instance encryption without application changes
5. **ASFF removed** — but Security Hub still uses it; just won't ask about format details
6. **No more basic networking questions** — no OSI model, no TCP vs UDP
