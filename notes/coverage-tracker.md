# SCS-C03 Blueprint Coverage Tracker

> Last updated: 2025-05-17 (Session 33, 261 questions)
> Purpose: Ensure every blueprint task has been tested before exam day.

## Legend
- ✅ Tested in questions + FAQ exists
- ⚠️ FAQ exists but not directly tested in exam-format questions
- ❌ Not covered yet

---

## D4: Identity & Access Management (20%) — ✅ HEAVILY COVERED

| Task | Topic | Status | Questions |
|---|---|---|---|
| 4.1 | Identity Center (SSO, permission sets) | ✅ | Q64, Q67, Q210 |
| 4.1 | SCIM provisioning | ✅ | Q263 |
| 4.1 | Cognito (user pools, identity pools) | ⚠️ | FAQ only |
| 4.1 | STS (AssumeRole, session duration, revocation) | ✅ | Q62, Q71, Q173 |
| 4.1 | Confused deputy (ExternalId) | ✅ | Q60, Q176 |
| 4.2 | Policy evaluation (SCP+RCP+boundary+session+identity+resource) | ✅ | 50+ questions |
| 4.2 | Permission boundaries (delegation pattern) | ✅ | Q49, Q76, Q257 |
| 4.2 | Session policies (ceiling + resource-policy bypass) | ✅ | Q78, Q96, Q169, Q229 |
| 4.2 | ABAC (PrincipalTag, ResourceTag, RequestTag) | ✅ | Q51, Q72, Q94, Q265 |
| 4.2 | Cross-account patterns (KMS, S3, SCP follows caller) | ✅ | Q70, Q95, Q256 |
| 4.2 | RCP (data perimeter, SLR exemption, PrincipalIsAWSService) | ✅ | Q36, Q44, Q74, Q217 |
| 4.2 | Verified Permissions (Cedar, app-level authz) | ✅ | Q61, Q66, Q75, Q216 |
| 4.2 | IAM Access Analyzer (external + unused + validation) | ✅ | Q141, Q144, Q184, Q253 |
| 4.2 | KMS Grants (cross-account, eventual consistency, grant token) | ✅ | Q46, Q69, Q101, Q175 |

---

## D5: Data Protection (18%) — ✅ WELL COVERED

| Task | Topic | Status | Questions |
|---|---|---|---|
| 5.1 | Nitro inter-instance encryption | ✅ | Q164, Q255 |
| 5.1 | MACsec (dedicated DX, Layer 2) | ✅ | Q149, Q182, Q202 |
| 5.1 | VPC endpoints (Gateway vs Interface) | ✅ | Q86, Q166, Q249, Q262 |
| 5.2 | KMS key types (symmetric, asymmetric, HMAC) | ✅ | FAQ |
| 5.2 | KMS rotation (auto, on-demand, manual/imported) | ✅ | Q114, Q172 |
| 5.2 | KMS auto-rotation retention (forever) | ✅ | Q192, Q223 |
| 5.2 | KMS key deletion (CancelKeyDeletion → Disabled) | ✅ | Q203, Q247 |
| 5.2 | KMS key policy (root = delegation, not grant) | ✅ | Q206, Q225, Q264 |
| 5.2 | KMS GenerateDataKey for S3 uploads | ✅ | Q211, Q246 |
| 5.2 | MRK (independent policies per region) | ✅ | Q84, Q103, Q165 |
| 5.2 | XKS (keys never in AWS) | ✅ | Q102 |
| 5.2 | CloudHSM (direct vs custom key store) | ✅ | FAQ |
| 5.2 | S3 Object Lock (Compliance vs Governance vs Legal Hold) | ✅ | Q85, Q127, Q260 |
| 5.2 | S3 encryption (SSE-S3/KMS/C decision) | ✅ | FAQ |
| 5.3 | Secrets Manager (rotation, AWSPREVIOUS) | ✅ | Q104, Q186, Q254 |
| 5.3 | Secrets Manager cross-region replication | ✅ | Q258 |
| 5.3 | Data masking (CW Logs data protection + logs:Unmask) | ✅ | Q88, Q181, Q199, Q220 |
| 5.3 | ACM Private CA (internal TLS, Network Firewall CA) | ⚠️ | FAQ only, tested indirectly via Q87/Q152 |

---

## D3: Infrastructure Security (18%) — ✅ WELL COVERED

| Task | Topic | Status | Questions |
|---|---|---|---|
| 3.1 | WAF (rules, rate-based, managed rule groups, 8KB limit) | ✅ | Q27, FAQ |
| 3.1 | Shield (Standard vs Advanced, DDoS cost protection) | ✅ | Q30, FAQ |
| 3.1 | CloudFront OAC (vs OAI, SSE-KMS support) | ✅ | FAQ |
| 3.1 | OCSF format / third-party WAF rules | ⚠️ | FAQ only |
| 3.2 | Inspector (EC2 CVEs, Lambda, container images) | ✅ | Q132, Q140 |
| 3.2 | SSM Session Manager (no inbound ports, logging) | ✅ | Q3, FAQ |
| 3.2 | GenAI OWASP / Bedrock Guardrails | ⚠️ | FAQ only — not tested in questions |
| 3.3 | Security Groups vs NACLs (stateful vs stateless) | ✅ | Q4, Q34 |
| 3.3 | Network Firewall (Suricata, TLS inspection, private CA) | ✅ | Q28, Q35, Q87, Q157 |
| 3.3 | DNS Firewall (ALLOW/BLOCK/ALERT, rule structure) | ✅ | Q26, Q31, Q107, Q209 |
| 3.3 | Firewall Manager (org-wide deploy, SG audit, auto-remediate) | ✅ | Q29, Q130, Q208, Q224 |
| 3.3 | Direct Connect + MACsec | ✅ | Q149, Q182 |
| 3.3 | Verified Access (zero-trust, per-app, no VPN) | ✅ | FAQ |
| 3.3 | Network Access Analyzer | ⚠️ | FAQ only |

---

## D1: Detection (16%) — ✅ COVERED (weakest by score: 63%)

| Task | Topic | Status | Questions |
|---|---|---|---|
| 1.1 | GuardDuty (threats, finding types, S3 Protection) | ✅ | Q13, Q116, Q155, Q161, Q218, Q227 |
| 1.1 | GuardDuty (regional, agentless, Runtime Monitoring) | ✅ | Q213, Q232 |
| 1.1 | Security Hub (FSBP, CIS, org-wide, requires Config) | ✅ | Q5, Q24, Q99, Q150 |
| 1.1 | Macie (PII in S3 only) | ✅ | FAQ |
| 1.1 | Config (managed rules, org rules, auto-remediation) | ✅ | Q237, Q248 |
| 1.1 | Detect vs prevent (GuardDuty vs policy) | ✅ | Q100, Q105, Q156, Q160 |
| 1.2 | CloudTrail (org trail, data events, advanced selectors) | ✅ | Q1, Q2, Q22 |
| 1.2 | CloudTrail Lake (managed store, SQL, near real-time) | ✅ | Q23, Q25, Q117, Q177 |
| 1.2 | CloudTrail integrity (digest files, SHA-256) | ✅ | Q215, Q259 |
| 1.2 | Security Lake (OCSF, your S3, normalizes all sources) | ✅ | Q128, Q170, Q234 |
| 1.2 | CloudWatch Logs Insights (query CW data, custom syntax) | ✅ | Q236 |
| 1.2 | VPC Flow Logs (VPC-level, not CW agent) | ✅ | Q238 |
| 1.2 | Resolver Query Logs (domain names, not in Flow Logs) | ✅ | FAQ |
| 1.3 | Troubleshooting missing logs | ✅ | Q6, Q238 |

---

## D2: Incident Response (14%) — ✅ COVERED

| Task | Topic | Status | Questions |
|---|---|---|---|
| 2.1 | IR sequence (isolate → snapshot → tag → investigate) | ✅ | Q118, Q167, Q235 |
| 2.1 | Step Functions for IR orchestration | ✅ | Q138, Q145 |
| 2.1 | FIS (chaos engineering, test IR plans) | ✅ | FAQ |
| 2.1 | Resilience Hub (assess RTO/RPO) | ✅ | FAQ |
| 2.2 | Detective (root cause, blast radius, timeline) | ✅ | Q109, Q136, Q143, Q239 |
| 2.2 | Validate findings (triage before full IR) | ✅ | Q148 |
| 2.2 | Credential leak response (deactivate → investigate → replace) | ✅ | Q250 |
| 2.2 | STS session revocation (TokenIssueTime) | ✅ | Q62, Q71, Q173 |

---

## D6: Governance (14%) — ⚠️ GAPS REMAIN

| Task | Topic | Status | Questions |
|---|---|---|---|
| 6.1 | Organizations (OUs, account structure) | ✅ | FAQ |
| 6.1 | Control Tower (landing zone, guardrails) | ✅ | Q119, Q251 |
| 6.1 | SCPs (preventive, management account exempt) | ✅ | Q58, Q73, Q191, Q261 |
| 6.1 | RCPs (resource-side, SLR exempt) | ✅ | Q36, Q74, Q217, Q252 |
| 6.1 | Delegated admin pattern | ✅ | Q242–Q245 drills |
| 6.2 | Firewall Manager (org-wide deploy) | ✅ | Q29, Q130, Q168 |
| 6.2 | RAM (share resources cross-account) | ✅ | Q57, Q126, Q131, Q244 |
| 6.2 | CloudFormation StackSets (multi-account IaC) | ❌ | Not tested |
| 6.2 | Service Catalog (standardized deployments) | ❌ | Not tested |
| 6.3 | AWS Audit Manager (compliance evidence) | ❌ | Not tested |
| 6.3 | AWS Artifact (compliance reports) | ❌ | Not tested |
| 6.3 | Config conformance packs (org-wide compliance) | ⚠️ | Mentioned in Q24, not directly tested |

---

## Action Items (Remaining Gaps)

| Priority | Topic | Action Needed |
|---|---|---|
| 🔴 | CloudFormation StackSets | 2-3 exam questions to test |
| 🔴 | Audit Manager / AWS Artifact | 1-2 exam questions to test |
| 🟡 | Service Catalog | 1 exam question |
| 🟡 | GenAI / Bedrock Guardrails | 1 exam question |
| 🟡 | Config conformance packs | 1 exam question |
| 🟡 | Cognito (direct scenario) | 1 exam question |
| 🟡 | Network Access Analyzer | 1 exam question |
