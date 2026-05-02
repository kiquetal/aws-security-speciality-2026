# FAQ: Security Services — When to Use Which

> **Blueprint refs:** Task 1.1 (monitoring/alerting), Task 2.2 (respond to events), Task 3.2 (compute scanning)
> **Diagram:** [security-services-comparison.png](../diagrams/security-services-comparison.png)

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Security Hub (AGGREGATOR)                     │
│         Collects findings from all services below                │
│         Runs compliance checks (standards/controls)              │
│         Org-wide via delegated admin                             │
├──────────────┬──────────────┬──────────────┬────────────────────┤
│  GuardDuty   │    Macie     │  Inspector   │   Config           │
│  (threats)   │  (sensitive  │  (vulns)     │   (compliance)     │
│              │   data)      │              │                    │
└──────────────┴──────────────┴──────────────┴────────────────────┘
         │              │             │               │
    Threat intel   S3 scanning   CVE scanning    Resource config
    ML anomalies   PII/PHI       EC2/Lambda/     Rule evaluation
    Runtime        Credit cards  containers      Drift detection
```

## Service Comparison Matrix

| Question the Exam Asks | Answer | NOT This |
|---|---|---|
| "Detect **public S3 buckets**" | **Security Hub** (S3 controls) or **Config** (managed rule) | ❌ Macie (finds data, not access), ❌ GuardDuty (finds threats, not misconfig) |
| "Find **sensitive data** (PII, credentials) in S3" | **Macie** | ❌ GuardDuty, ❌ Inspector, ❌ Security Hub |
| "Detect **compromised EC2** (crypto mining, C2 traffic)" | **GuardDuty** | ❌ Inspector (finds vulns, not active threats), ❌ Config |
| "Detect **compromised IAM credentials**" | **GuardDuty** | ❌ IAM Access Analyzer (finds overly permissive, not compromised) |
| "Scan EC2 for **software vulnerabilities** (CVEs)" | **Inspector** | ❌ GuardDuty (threats, not vulns), ❌ Macie |
| "Scan **Lambda functions** for vulnerabilities" | **Inspector** | ❌ GuardDuty Lambda Protection (network threats only) |
| "Scan **container images** for vulnerabilities" | **Inspector** (or ECR native scanning) | ❌ GuardDuty |
| "Detect **unusual API activity** (anomalies)" | **GuardDuty** (or CloudTrail Insights) | ❌ Config, ❌ Inspector |
| "Check if resources are **compliant** with standards" | **Security Hub** (standards) or **Config** (rules) | ❌ GuardDuty, ❌ Inspector |
| "**Investigate** a finding (root cause analysis)" | **Detective** | ❌ GuardDuty (detects, doesn't investigate) |
| "**Aggregate findings** across accounts/regions" | **Security Hub** | ❌ GuardDuty (regional, feeds into Security Hub) |
| "Detect **malware** on EBS/S3" | **GuardDuty** Malware Protection | ❌ Inspector, ❌ Macie |
| "Monitor **resource configuration changes**" | **Config** | ❌ CloudTrail (logs API calls, not config state) |
| "Detect **S3 data exfiltration** in progress" | **GuardDuty** S3 Protection | ❌ Macie (discovery, not real-time threat) |

## Deep Dive: Each Service

### GuardDuty — Threat Detection (Task 1.1)

**What it does:** Continuously monitors for malicious activity and unauthorized behavior.

**Data sources (no agents for foundational):**
- CloudTrail management events (always)
- VPC Flow Logs (always)
- DNS logs (always)
- S3 data events (optional protection plan)
- EKS audit logs (optional)
- Runtime activity — EC2, EKS, ECS (optional, needs agent)
- RDS login events — Aurora only (optional)
- Lambda network activity (optional)

**Detects:**
- ✅ Compromised instances (crypto mining, C2, data exfil)
- ✅ Compromised credentials (unusual geo, anonymizing proxy)
- ✅ Compromised S3 buckets (access from malicious IPs)
- ✅ Malware (EBS, S3, AWS Backup scanning)
- ✅ Container threats (EKS/ECS runtime)
- ❌ Does NOT detect misconfigurations
- ❌ Does NOT detect vulnerabilities
- ❌ Does NOT find sensitive data

**Org-wide:** Delegated admin, auto-enable new accounts

**Exam gotchas:**
- Foundational sources (CloudTrail, VPC Flow Logs, DNS) are always enabled — no opt-out
- S3 Protection doesn't require enabling CloudTrail data events — direct feed
- Runtime Monitoring requires agent deployment (not automatic)
- EBS Malware scan: once per 24 hours per instance
- Finding severity: Low (0.1-3.9), Medium (4.0-6.9), High (7.0-8.9), Critical (9.0-10.0)
- Extended Threat Detection: correlates findings into attack sequences (no extra cost)

---

### Macie — Sensitive Data Discovery (Task 1.1)

**What it does:** Discovers and protects sensitive data stored in S3.

**Detects:**
- ✅ PII (names, addresses, SSNs, passport numbers)
- ✅ PHI (health records, insurance IDs)
- ✅ Financial data (credit card numbers, bank accounts)
- ✅ Credentials (AWS keys, private keys in S3)
- ✅ Custom data identifiers (regex patterns you define)
- ❌ Does NOT detect threats or attacks
- ❌ Does NOT scan EC2, Lambda, or databases
- ❌ Does NOT detect public access (that's Security Hub/Config)

**How it works:**
- Scans S3 objects using ML + pattern matching
- Scheduled or one-time discovery jobs
- Automated sensitive data discovery (samples all buckets)

**Org-wide:** Delegated admin, manage member accounts centrally

**Exam gotchas:**
- **S3 only** — doesn't scan EBS, EFS, RDS, DynamoDB
- Automated discovery samples objects (not full scan) — use jobs for comprehensive
- Findings go to Security Hub automatically
- Can create custom data identifiers with regex + keywords
- Suppression rules to reduce noise (not delete findings)

---

### Inspector — Vulnerability Scanning (Task 3.2)

**What it does:** Scans compute workloads for software vulnerabilities and unintended network exposure.

**Scans:**
- ✅ EC2 instances (OS + application CVEs via SSM agent)
- ✅ Lambda functions (code + dependency vulnerabilities)
- ✅ Container images in ECR (OS + language package CVEs)
- ❌ Does NOT scan S3
- ❌ Does NOT detect active threats (that's GuardDuty)
- ❌ Does NOT find sensitive data (that's Macie)

**How it works:**
- **Agentless for ECR** — scans on push
- **SSM Agent for EC2** — continuous scanning
- **Automatic for Lambda** — scans on deploy
- Findings include CVE ID, severity (CVSS), affected package, fix version

**Org-wide:** Delegated admin, auto-enable

**Exam gotchas:**
- Requires SSM Agent on EC2 (same agent as Session Manager)
- Network reachability findings: detects open ports accessible from internet
- Inspector ≠ Inspector Classic (v1 is deprecated, exam uses v2)
- Lambda scanning: code vulnerabilities + dependency vulnerabilities
- Findings go to Security Hub automatically

---

### Security Hub — Aggregation + Compliance (Task 1.1)

**What it does:** Central dashboard for security findings + automated compliance checks.

**Two functions:**
1. **Aggregates findings** from GuardDuty, Macie, Inspector, Config, Firewall Manager, IAM Access Analyzer, third-party tools
2. **Runs compliance checks** via security standards (uses Config rules under the hood)

**Built-in standards:**
- AWS Foundational Security Best Practices (FSBP)
- CIS AWS Foundations Benchmark
- PCI DSS
- NIST 800-53

**S3-specific controls (why it answers the "public bucket" question):**
- `[S3.1]` S3 Block Public Access should be enabled
- `[S3.2]` S3 buckets should prohibit public read access
- `[S3.3]` S3 buckets should prohibit public write access
- `[S3.8]` S3 Block Public Access should be enabled at bucket level

**Org-wide:** Delegated admin, cross-region aggregation, auto-enable

**Exam gotchas:**
- **Requires AWS Config** to be enabled (compliance checks use Config rules)
- Findings in ASFF format (AWS Security Finding Format)
- Can send findings to EventBridge for automated response
- Cross-region aggregation: designate one region as aggregation region
- Custom actions: trigger EventBridge from specific findings

---

### Detective — Investigation (Task 2.2)

**What it does:** Analyzes and visualizes data to investigate security findings. Used AFTER detection.

- ✅ Root cause analysis of GuardDuty findings
- ✅ Visualize resource behavior over time
- ✅ Correlate across CloudTrail, VPC Flow Logs, GuardDuty, EKS
- ❌ Does NOT detect anything — only investigates
- ❌ Not a monitoring tool

**Exam signal:** "investigate," "root cause," "determine scope" → Detective

---

### Config — Configuration Compliance (Task 1.1, 6.1)

**What it does:** Records resource configuration changes and evaluates compliance against rules.

- ✅ Tracks configuration history (who changed what, when)
- ✅ Managed rules (e.g., `s3-bucket-public-read-prohibited`)
- ✅ Custom rules (Lambda-backed)
- ✅ Conformance packs (bundle of rules)
- ✅ Organization-wide rules
- ❌ Does NOT detect threats
- ❌ Does NOT scan for vulnerabilities

**Exam signal:** "compliance," "configuration drift," "detect non-compliant resources" → Config

## Decision Flowchart

```
Is something ACTIVELY MALICIOUS happening?
├─ Yes → GuardDuty
└─ No
   ├─ Is there SENSITIVE DATA in S3?
   │  └─ Yes → Macie
   ├─ Are there SOFTWARE VULNERABILITIES?
   │  └─ Yes → Inspector
   ├─ Is a RESOURCE MISCONFIGURED?
   │  └─ Yes → Config or Security Hub
   ├─ Need to INVESTIGATE a finding?
   │  └─ Yes → Detective
   └─ Need to AGGREGATE across accounts?
      └─ Yes → Security Hub
```

## Common Exam Traps

1. **"Detect public S3 bucket"** — Security Hub or Config, NOT Macie (Macie finds data, not access)
2. **"Find PII in S3"** — Macie, NOT GuardDuty (GuardDuty detects threats to S3, not data content)
3. **"EC2 running crypto miner"** — GuardDuty, NOT Inspector (Inspector finds vulns, not active threats)
4. **"Scan Lambda for vulnerabilities"** — Inspector, NOT GuardDuty Lambda Protection (GuardDuty monitors Lambda network traffic)
5. **"Investigate a GuardDuty finding"** — Detective, NOT GuardDuty itself
6. **"Aggregate findings org-wide"** — Security Hub, NOT GuardDuty (GuardDuty is regional, feeds into Security Hub)
7. **"Detect S3 exfiltration in progress"** — GuardDuty S3 Protection, NOT Macie (Macie is discovery, not real-time)
