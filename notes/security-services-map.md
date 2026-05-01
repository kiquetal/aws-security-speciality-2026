# AWS Security Services — Complete Map

> **Blueprint refs:** Task 1.1, 1.2, 1.3, 2.1, 2.2, 3.2
> **Diagram:** [security-services-complete-map.png](../diagrams/security-services-complete-map.png)

## The Full Picture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         DATA SOURCES                                     │
│                                                                         │
│  CloudTrail    VPC Flow Logs    DNS Logs    S3 Objects    EC2/Lambda    │
│  (API calls)   (network)       (domains)   (stored data)  (software)   │
└──────┬──────────────┬─────────────┬────────────┬──────────────┬────────┘
       │              │             │            │              │
       ▼              ▼             ▼            ▼              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      DETECTION LAYER                                     │
│                                                                         │
│  🔴 GuardDuty          🟡 Macie           🟠 Inspector    🔵 Config   │
│  ═══════════           ════════           ═══════════     ════════     │
│  THREATS               SENSITIVE DATA     VULNERABILITIES COMPLIANCE  │
│  ─────────             ──────────────     ─────────────── ──────────  │
│  • Crypto mining       • PII in S3        • EC2 CVEs      • Config   │
│  • Compromised creds   • PHI in S3        • Lambda CVEs     changes  │
│  • C2 traffic          • Credit cards     • Container CVEs• Managed  │
│  • Data exfiltration   • AWS keys in S3   • Network          rules   │
│  • Malware (EBS/S3)    • Custom regex       exposure      • Drift    │
│  • Container threats                                                  │
│  ─────────             ──────────────     ─────────────── ──────────  │
│  Reads: CloudTrail     Reads: S3 objects  Reads: SSM Agent Reads:    │
│    VPC Flow Logs                            ECR images     Resource   │
│    DNS logs                                 Lambda code    configs    │
│  No agents needed      S3 ONLY            Needs SSM Agent            │
│                                           on EC2                      │
└────────┬───────────────────┬──────────────────┬──────────────┬────────┘
         │                   │                  │              │
         │    findings       │    findings      │   findings   │ compliance
         ▼                   ▼                  ▼              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      AGGREGATION LAYER                                   │
│                                                                         │
│  🟢 Security Hub                                                        │
│  ════════════════════════════════════════════════════════════════        │
│  CENTRAL DASHBOARD — two jobs:                                          │
│                                                                         │
│  Job 1: AGGREGATE findings from GuardDuty, Macie, Inspector,           │
│          Config, IAM Access Analyzer, Firewall Manager, 3rd party      │
│                                                                         │
│  Job 2: COMPLIANCE checks via security standards                        │
│          • AWS Foundational Security Best Practices (FSBP)              │
│          • CIS AWS Foundations Benchmark                                 │
│          • PCI DSS                                                      │
│          • NIST 800-53                                                   │
│                                                                         │
│  ⚠️  REQUIRES AWS Config enabled (compliance checks use Config rules)   │
│  ⚠️  Org-wide via delegated admin + cross-region aggregation            │
│                                                                         │
└──────────┬──────────────────────────────────────┬───────────────────────┘
           │                                      │
           │ investigate                          │ automate
           ▼                                      ▼
┌─────────────────────────┐    ┌──────────────────────────────────────────┐
│ INVESTIGATION LAYER     │    │ RESPONSE LAYER                           │
│                         │    │                                          │
│ 🟣 Detective            │    │ EventBridge ──► Lambda (remediate)       │
│ ═══════════             │    │             ──► Step Functions (runbook)  │
│ ROOT CAUSE ANALYSIS     │    │             ──► SNS (notify team)        │
│ ───────────────         │    │                                          │
│ • Investigate findings  │    │ Example:                                 │
│ • Visualize behavior    │    │   GuardDuty high severity finding        │
│ • Correlate events      │    │   → EventBridge rule                     │
│ • Used AFTER detection  │    │   → Lambda: isolate EC2, revoke creds   │
│ • NOT a monitor         │    │   → SNS: page security team             │
│                         │    │                                          │
└─────────────────────────┘    └──────────────────────────────────────────┘
```

## Dependencies (What Requires What)

```
Security Hub ──requires──► AWS Config (compliance checks use Config rules)
Inspector    ──requires──► SSM Agent on EC2 (for instance scanning)
GuardDuty    ──requires──► nothing (reads CloudTrail/VPC Flow Logs/DNS directly)
Macie        ──requires──► nothing (reads S3 directly)
Detective    ──requires──► GuardDuty enabled (investigates GuardDuty findings)
Config       ──requires──► nothing (records resource configs directly)
```

## One-Line Cheat Sheet

```
GuardDuty   = "Something BAD is happening right now"        → active threats
Macie       = "There's SENSITIVE DATA sitting in S3"        → data discovery
Inspector   = "This software has a KNOWN VULNERABILITY"     → CVE scanning
Config      = "A resource CHANGED — is it still compliant?" → drift detection
Security Hub= "Show me EVERYTHING in one place"             → aggregation
Detective   = "WHY did this happen? Show me the timeline"   → investigation
```

## Exam Decision Table

```
Question contains...              → Answer is...        → NOT this
─────────────────────             ─────────────         ──────────
"public S3 bucket"                → Security Hub/Config → NOT Macie
"PII / sensitive data in S3"      → Macie               → NOT GuardDuty
"crypto mining / C2 traffic"      → GuardDuty           → NOT Inspector
"compromised credentials"         → GuardDuty           → NOT Access Analyzer
"software vulnerabilities / CVEs" → Inspector            → NOT GuardDuty
"Lambda vulnerabilities"          → Inspector            → NOT GuardDuty
"container image vulnerabilities" → Inspector            → NOT GuardDuty
"unusual API activity"            → GuardDuty            → NOT Config
"compliance with standards"       → Security Hub/Config  → NOT GuardDuty
"investigate / root cause"        → Detective            → NOT GuardDuty
"aggregate across accounts"       → Security Hub         → NOT GuardDuty
"malware on EBS/S3"               → GuardDuty            → NOT Inspector
"configuration changes"           → Config               → NOT CloudTrail
"S3 data exfiltration"            → GuardDuty            → NOT Macie
```
