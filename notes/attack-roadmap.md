# SCS-C03 Attack Roadmap — Depth-First, Hardest-First

> Derived from Appendix B recategorization analysis + blueprint task weights.
> Strategy: attack the topics the exam goes **deepest** on first, not just heaviest by weight.

## Difficulty Tiers

### 🔴 Tier 1: Deep & Tricky (exam differentiators — most questions get wrong here)

These are where C03 goes deeper than C02, has new content, or fans out across multiple domains.

| # | Topic | Tasks | Why It's Hard | Depth Signal |
|---|-------|-------|---------------|--------------|
| 1 | **IAM policy evaluation with ALL layers** (SCP + RCP + boundary + session + identity + resource) | 4.2, 6.1 | 6 policy types intersecting. RCPs are brand new. Session policies are subtle. Cross-account evaluation differs from same-account. | RCPs new in C03; SCPs tested in BOTH D4 and D6; troubleshooting added |
| 2 | **Cross-account access patterns** (trust policies, confused deputy, ExternalId, role chaining, source identity) | 4.1, 4.2 | Multiple mechanisms interact. Role chaining resets duration to 1hr. Presigned URLs inherit signer permissions at USE time. | D4 jumped +4%; policy basics removed = exam assumes you know them cold |
| 3 | **KMS key management matrix** (AWS managed vs customer managed vs imported vs CloudHSM vs XKS, grants vs key policies, multi-region keys) | 5.2, 5.3 | 5 key origin types × different rotation/durability/quota rules. Imported keys: YOU own durability. XKS: 500ms timeout, no SLA. MRKs: same key material, independent policies. | 3 new sub-tasks added (5.3.3, 5.3.4, 5.3.5) |
| 4 | **Data perimeter architecture** (RCPs + SCPs + VPC endpoints + S3 bucket policies + KMS key policies working together) | 4.2, 5.2, 6.1 | Must understand which policy type blocks which principal type. RCPs block external callers; SCPs block internal callers. `aws:PrincipalIsAWSService` exception is critical. | Spans 3 domains — exam tests this from IAM, data protection, AND governance angles |
| 5 | **Troubleshooting auth/authz failures** (why is access denied? which policy layer blocked it?) | 4.1, 4.2, 1.3 | Requires mental simulation of the full evaluation chain. CloudTrail shows the deny but not always which policy caused it. IAM Access Analyzer vs Policy Simulator. | Troubleshooting is NEW first-class concern in C03 |

### 🟠 Tier 2: Broad & Interconnected (many services, must know integration patterns)

| # | Topic | Tasks | Why It's Hard | Depth Signal |
|---|-------|-------|---------------|--------------|
| 6 | **Detection pipeline architecture** (GuardDuty → Security Hub → EventBridge → Lambda/Step Functions → remediation) | 1.1, 2.1, 2.2 | Must know: what each service detects, how findings flow, severity levels, automated response patterns. Extended Threat Detection is new. | Old D1+D2 merged; detection + response now tested as connected pipeline |
| 7 | **Logging architecture** (CloudTrail org trails + VPC Flow Logs + Security Lake + Athena + CloudWatch Logs Insights) | 1.2, 1.3 | Which log source for which question? When CloudTrail Lake vs S3+Athena? OCSF format for Security Lake. Troubleshooting missing logs. | Absorbed old D2 entirely; OCSF is new |
| 8 | **Network security across layers** (SGs + NACLs + Network Firewall + VPC endpoints + Verified Access + Direct Connect + MACsec) | 3.3, 5.1 | Old Task 3.2 fanned out to 4 C03 tasks. North/south vs east/west. Endpoint policies don't replace bucket policies. | Broadest fan-out in the recategorization |
| 9 | **Secrets + rotation lifecycle** (Secrets Manager managed rotation vs custom Lambda, Parameter Store comparison, cross-region replication) | 5.3 | Rotation doesn't re-auth open connections. 7-day deletion window. Managed rotation vs custom. When to use which. | Compute hardening + secrets now linked (old 3.3 → new 5.3) |
| 10 | **Incident response automation** (forensic snapshot, EC2 isolation, Step Functions runbooks, Automated Forensics Orchestrator) | 2.1, 2.2 | Must know the sequence: isolate → snapshot → investigate → remediate. New: validate findings to assess scope (2.2.3). | New sub-task 2.2.3; Fault Injection Service for testing IR plans |

### 🟡 Tier 3: Know-It-or-Lose-Points (factual recall, service-specific gotchas)

| # | Topic | Tasks | Key Gotchas |
|---|-------|-------|-------------|
| 11 | **Edge security** (WAF rules, Shield Advanced, CloudFront, OCSF, third-party WAF rules) | 3.1 | Shield Advanced: $3K/month, DDoS cost protection, proactive engagement. WAF: rate-based rules, geo-match, IP sets. OCSF is new. |
| 12 | **Compute security** (Inspector, SSM Patch Manager, Session Manager, Image Builder, GenAI OWASP) | 3.2 | Instance profile vs service role vs execution role. Inspector: EC2 + Lambda + container images. GenAI OWASP is new (3.2.7). |
| 13 | **Data masking** (CloudWatch Logs data protection, SNS message data protection) | 5.3.4 | Brand new in C03. Know the policy syntax and supported data identifiers. |
| 14 | **Multi-account governance** (Organizations, Control Tower, SCPs, RCPs, delegated admin, Firewall Manager) | 6.1, 6.2, 6.3 | SCP: management account exempt. RCP: management account resources exempt. Control Tower: uses SCPs+RCPs for preventive controls. |
| 15 | **Inter-resource encryption in transit** (Nitro, EKS inter-node, EMR, SageMaker) | 5.1.3 | New in C03. Nitro: automatic inter-instance encryption, no app changes. EKS: Istio mTLS or EKS pod identity. |

## Attack Order (recommended sequence)

```
Phase 1: IAM Deep Dive (Weeks 1-2) — 20% of exam
  ├─ #1  Policy evaluation (all 6 layers)        ← hardest, do first
  ├─ #2  Cross-account + STS mechanics
  ├─ #4  Data perimeter (RCP + SCP + endpoint)
  └─ #5  Troubleshooting auth failures

Phase 2: Data Protection (Weeks 3-4) — 18% of exam
  ├─ #3  KMS key management matrix               ← 3 new sub-tasks
  ├─ #9  Secrets + rotation lifecycle
  ├─ #13 Data masking (new in C03)
  └─ #15 Inter-resource encryption (new in C03)

Phase 3: Infrastructure (Weeks 5-6) — 18% of exam
  ├─ #8  Network security across layers
  ├─ #11 Edge security + OCSF
  └─ #12 Compute security + GenAI OWASP

Phase 4: Detection + IR (Weeks 7-9) — 30% combined
  ├─ #6  Detection pipeline architecture
  ├─ #7  Logging architecture
  └─ #10 IR automation + forensics

Phase 5: Governance (Week 10) — 14% of exam
  └─ #14 Multi-account governance
         (partially covered by #1 and #4 already)

Phase 6: Cross-domain (Weeks 11-12)
  └─ Full practice exams targeting weak spots
```

## What Your K8s/Istio Background Already Covers

Don't waste time re-learning these — just map to AWS equivalents:

| You Already Know | AWS Equivalent | Exam Task |
|-----------------|----------------|-----------|
| K8s RBAC | IAM RBAC + ABAC | 4.2 |
| Istio mTLS / service mesh | EKS inter-node encryption, Nitro, VPC encryption | 5.1.3 |
| K8s NetworkPolicy | Security Groups + NACLs + Network Firewall | 3.3 |
| K8s Secrets | Secrets Manager + Parameter Store | 5.3 |
| OPA/Gatekeeper policies | SCPs + RCPs + Permission Boundaries | 4.2, 6.1 |
| Container image scanning | Amazon Inspector + ECR scanning | 3.2 |
| K8s audit logs | CloudTrail + GuardDuty EKS Protection | 1.1, 1.2 |

## The 7 "New in C03" Topics to Nail

These have no C02 precedent — exam writers will test them because they're differentiators:

1. **RCPs** (Task 6.1) — resource-side data perimeter
2. **GenAI OWASP Top 10** (Task 3.2.7) — Bedrock Guardrails, prompt injection
3. **OCSF** (Task 3.1.4) — Security Lake schema format
4. **Data masking** (Task 5.3.4) — CloudWatch Logs + SNS data protection
5. **Nitro inter-instance encryption** (Task 5.1.3) — automatic, no app changes
6. **Imported key material differences** (Task 5.3.3) — durability, rotation, expiration
7. **Multi-Region keys + Private CA** (Task 5.3.5) — MRKs share material, independent policies
