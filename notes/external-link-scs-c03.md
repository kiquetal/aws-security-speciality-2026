# External Study Guide Reference — SCS-C03

> Source: Paul Mangham's documentation-first study guide (https://paulmangham.dev)
> Saved: 2026-08-23
> Purpose: Cross-reference for question generation and coverage validation

---

## Priority Tiers

- ★★★ Core — multiple questions, must know cold
- ★★ Important — 1-2 questions reliably
- ★ Light — one distinguishing question or distractor

---

## Domain 1: Detection (16%)

### Chapter 1 — Monitoring and alerting (Task 1.1)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 1.1 | Security Hub (aggregation, standards, cross-Region, automation) | ★★★ | 3-5 |
| 1.2 | GuardDuty (data sources, finding types, protection plans, multi-account) | ★★★ | 3-5 |
| 1.3 | CloudWatch (metric filters, alarms, Logs encryption) | ★★★ | 3-4 |
| 1.4 | Macie (custom identifiers, jobs vs automated, S3 posture) | ★★ | 1-2 |
| 1.5 | Automated assessments (Config conformance packs, State Manager, EventBridge) | ★★ | 1-2 |
| 1.6 | EventBridge (patterns, targets, cross-account buses, DLQ) | ★★★ | 2-3 |

### Chapter 2 — Logging solutions (Task 1.2)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 2.1 | CloudTrail (mgmt/data/Insights, org trails, integrity, Lake) | ★★★ | 3-5 |
| 2.2 | Network logs (VPC Flow, TGW Flow, Resolver, WAF, ALB, CloudFront) | ★★★ | 2-3 |
| 2.3 | Security Lake / OCSF (normalize, Parquet, subscribers) | ★★ | 1-2 |
| 2.4 | Log storage + analysis (Athena, Insights, lifecycle, Object Lock) | ★★ | 2-3 |
| 2.5 | Normalizing logs (OpenSearch, Grafana, Firehose) | ★ | 0-1 |
| 2.6 | Application log sources (CT data events vs S3 access logs, API GW, CF) | ★★ | 1-2 |

### Chapter 3 — Troubleshooting (Task 1.3)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 3.1 | Missing logs (bucket policy, KMS key policy, IAM role, CW agent) | ★★ | 2-3 |
| 3.2 | Alerting failures (metric filter, alarm state, SNS policy, EB pattern) | ★★ | 1-2 |

---

## Domain 2: Incident Response (14%)

### Chapter 4 — Planning and testing (Task 2.1)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 4.1 | IR planning (credential runbook, SSM Automation, OpsCenter) | ★★★ | 2-4 |
| 4.2 | Testing (FIS, Resilience Hub, ARC) | ★ | 1 |
| 4.3 | Automated remediation (EventBridge → Lambda/SF/SSM, Forensics Orchestrator) | ★★ | 2-3 |

### Chapter 5 — Responding (Task 2.2)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 5.1 | Containment + recovery (EC2 isolation sequence, SG connection tracking) | ★★★ | 2-3 |
| 5.2 | Forensic capture (Object Lock, EBS snapshots, forensics account) | ★★ | 1-2 |
| 5.3 | Investigation (Detective, Athena, Lake, Security Hub workflow) | ★★ | 2-3 |
| 5.4 | Triage (severity, workflow status, suppression, validation) | ★★ | 1-2 |

---

## Domain 3: Infrastructure Security (18%)

### Chapter 6 — Edge security (Task 3.1)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 6.1 | WAF (attaches to, managed rules, Bot Control, rate-based, geo) | ★★★ | 2-4 |
| 6.2 | Shield (Standard vs Advanced, SRT, cost protection) | ★★ | 1-2 |
| 6.3 | CloudFront + S3 (OAC, signed URLs, headers, FLE, CORS) | ★★ | 2-3 |
| 6.4 | Route 53 (DNS Firewall, DNSSEC) + IoT policies | ★ | 1 |

### Chapter 7 — Compute security (Task 3.2)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 7.1 | AMI hardening + IMDSv2 + role taxonomy | ★★ | 2-3 |
| 7.2 | Inspector + Patch Manager + Runtime Monitoring | ★★★ | 2-4 |
| 7.3 | Session Manager (portless, logging, port forwarding) | ★★ | 1-2 |
| 7.4 | Pipeline security (CodeGuru, Q Developer) | ★ | 1 |
| 7.5 | GenAI (Bedrock Guardrails, OWASP LLM Top 10) | ★★ | 1-2 |

### Chapter 8 — Network controls (Task 3.3)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 8.1 | SGs + NACLs (stateful/stateless, connection tracking) | ★★★ | 2-4 |
| 8.2 | Network Firewall + segmentation (Suricata, TGW, inspection VPC) | ★★ | 2-3 |
| 8.3 | Hybrid (VPN, DX, MACsec, TGW, peering) | ★★ | 1-2 |
| 8.4 | Verified Access + NAA + Inspector network reachability | ★★ | 1-2 |

---

## Domain 4: Identity and Access Management (20%)

### Chapter 9 — Authentication (Task 4.1)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 9.1 | IAM identities + MFA + credential reports + root | ★★★ | 2-3 |
| 9.2 | STS (AssumeRole variants, ExternalId, TokenIssueTime, presigned) | ★★★ | 2-4 |
| 9.3 | Federation + Identity Center (SCIM, permission sets) | ★★ | 2-3 |
| 9.4 | Cognito (User Pools vs Identity Pools, tokens) | ★★ | 1-2 |
| 9.5 | Troubleshooting authentication (CloudTrail, IC propagation) | ★★ | 1-2 |

### Chapter 10 — Authorization (Task 4.2)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 10.1 | Policy evaluation logic (all gates, explicit deny, conditions) | ★★★ | 4-6 |
| 10.2 | Cross-account (resource policies, trust policies, PrincipalOrgID) | ★★★ | 3-4 |
| 10.3 | ABAC + boundaries + session policies | ★★★ | 2-3 |
| 10.4 | Roles Anywhere + Verified Permissions | ★ | 1 each |
| 10.5 | Troubleshooting authorization (simulator, Access Analyzer) | ★★ | 2-3 |

---

## Domain 5: Data Protection (18%)

### Chapter 11 — Data in transit (Task 5.1)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 11.1 | TLS enforcement + ACM (per-service mechanisms) | ★★★ | 2-4 |
| 11.2 | VPC endpoints + PrivateLink + Client VPN + Verified Access | ★★★ | 2-3 |
| 11.3 | Inter-resource encryption (EMR, EKS, SageMaker, Nitro) | ★ | 1 |

### Chapter 12 — Data at rest (Task 5.2)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 12.1 | KMS fundamentals (envelope, key types, 4KB, GenerateDataKey) | ★★★ | 4-6 |
| 12.2 | KMS key policies + grants + CloudHSM + custom key stores | ★★★ | 3-4 |
| 12.3 | S3 encryption + Block Public Access + Object Lock | ★★★ | 3-5 |
| 12.4 | Data integrity (Object Lock, Vault Lock, Signer, lifecycle) | ★★ | 2-3 |
| 12.5 | Backup + Backup Vault Lock + DLM + replication + DataSync | ★★ | 1-2 |
| 12.6 | EBS/RDS/DynamoDB/SQS/EFS encryption specifics | ★★ | 2-3 |

### Chapter 13 — Credentials and key material (Task 5.3)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 13.1 | Secrets Manager (rotation, cross-account, replication vs Param Store) | ★★★ | 2-3 |
| 13.2 | Imported keys + XKS (custody, rotation, expiry differences) | ★★ | 1-2 |
| 13.3 | MRK + Private CA (cross-Region crypto + internal TLS) | ★★ | 1-2 |
| 13.4 | Data masking (CW Logs data protection + SNS message protection) | ★★ | 1-2 |

---

## Domain 6: Security Foundations and Governance (14%)

### Chapter 14 — Multi-account strategy (Task 6.1)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 14.1 | Organizations + SCPs + RCPs + declarative policies | ★★★ | 3-4 |
| 14.2 | Control Tower (landing zone, guardrail types, drift, Account Factory) | ★★ | 1-2 |
| 14.3 | Delegated admin + centralized security (SRA pattern) | ★★ | 1-2 |
| 14.4 | Root user management (centralized root, break-glass) | ★★ | 1-2 |

### Chapter 15 — Secure deployment (Task 6.2)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 15.1 | CloudFormation (StackSets, Guard, service roles, stack policies, drift) | ★★ | 1-2 |
| 15.2 | Firewall Manager (WAF/SG/NF/DNS FW policies, prerequisites) | ★★ | 1-2 |
| 15.3 | Service Catalog + RAM + tagging | ★ | 1-2 |

### Chapter 16 — Compliance (Task 6.3)

| # | Topic | Tier | Expected Qs |
|---|---|---|---|
| 16.1 | AWS Config (rules, remediation, conformance packs, aggregators) | ★★★ | 3-4 |
| 16.2 | Audit Manager + Artifact | ★ | 1 |
| 16.3 | Well-Architected Tool + Trusted Advisor | ★★ | 1-2 |

---

## Final Checklist (from the guide)

1. Walk IAM policy evaluation flow (all gates, cross-account differences)
2. KMS key policy uniqueness + custody differences (AWS-generated vs imported vs XKS)
3. EC2 containment + credential compromise sequence (ordering questions)
4. Data source → analysis tool mapping for any question
5. SSE-S3 vs SSE-KMS vs SSE-C vs client-side from one-line requirement
6. Multi-account reference architecture (mgmt, security tooling, log archive, SCPs/RCPs)
7. Bedrock Guardrails + CW Logs data protection + Verified Access one-liners

---

## Question Estimate by Tier

| Tier | Topics | Expected Questions | % of Exam |
|---|---|---|---|
| ★★★ Core | 24 | ~35-45 | ~70% |
| ★★ Important | 35 | ~15-20 | ~25% |
| ★ Light | 7 | ~5-7 | ~5% |
