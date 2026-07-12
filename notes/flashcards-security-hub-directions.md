# Security Hub Integration Directions — Flashcard

> Who sends TO Security Hub? Who reads FROM Security Hub? Who doesn't integrate at all?

---

## Services That SEND Findings TO Security Hub

| Service | What it sends | Automatic? |
|---|---|---|
| **GuardDuty** | Threat findings (C2, crypto, exfil) | ✅ Auto |
| **Inspector** | CVE findings (EC2, Lambda, containers) | ✅ Auto |
| **Macie** | Sensitive data findings (PII in S3) | ✅ Auto |
| **Config** | Compliance findings (rule evaluations) | ✅ Auto |
| **Access Analyzer** | External access + unused access findings | ✅ Auto |
| **Firewall Manager** | Non-compliant resource findings | ✅ Auto |
| **CodeGuru Security** | Code vulnerability findings | ✅ Auto |
| **IoT Device Defender** | IoT audit findings | ✅ Auto |
| **Third-party tools** | Custom findings (ASFF format) | Manual integration |

---

## Services That READ FROM Security Hub

| Service | What it reads | Direction |
|---|---|---|
| **Detective** | Findings as investigation entry points | SH → Detective |
| **EventBridge** | Findings for automated response | SH → EventBridge → Lambda/SF |
| **Custom actions** | User clicks "Remediate" → triggers EventBridge | SH → EventBridge |

---

## Services That DO NOT Integrate with Security Hub

| Service | Why not |
|---|---|
| **CloudTrail** | Raw API logs, not findings |
| **VPC Flow Logs** | Raw network logs, not findings |
| **Trusted Advisor** | No SH integration at all |
| **Security Lake** | Stores logs in OCSF, different purpose |
| **CloudWatch Logs** | Raw app/OS logs, not findings |
| **Detective** | Reads FROM SH, never sends TO SH |

---

## Data Flow Direction (Full Pipeline)

```
┌─────────────────────────────────────────────┐
│ DETECTION (generate findings)                │
│ GuardDuty, Inspector, Macie, Config, AA, FM │
└──────────────────┬──────────────────────────┘
                   │ findings flow DOWN
                   ▼
┌─────────────────────────────────────────────┐
│ AGGREGATION (view + compliance)              │
│ Security Hub                                 │
│ • Dashboard + scores                         │
│ • FSBP / CIS / PCI standards                │
│ • Cross-region aggregation                   │
└──────────────────┬──────────────────────────┘
                   │ two directions OUT
          ┌────────┴────────┐
          ▼                 ▼
┌──────────────────┐ ┌─────────────────────────┐
│ INVESTIGATE      │ │ RESPOND (automate)       │
│ Detective        │ │ EventBridge → Lambda/SF  │
│ • Timeline       │ │ • Isolate EC2            │
│ • Blast radius   │ │ • Revoke creds           │
│ • Correlate      │ │ • Notify team            │
└──────────────────┘ └─────────────────────────┘
```

---

## Exam Traps

| Trap | Truth |
|---|---|
| "Detective sends findings to SH" | ❌ Detective READS from SH (investigation tool) |
| "Security Hub remediates" | ❌ SH = dashboard only. Config+SSM = remediation. |
| "Trusted Advisor integrates with SH" | ❌ No integration at all |
| "CloudTrail sends to SH" | ❌ Raw logs ≠ findings |
| "Security Hub is global" | ❌ Regional. Cross-region = aggregation region designated. |
| "Security Hub writes to S3" | ❌ No. You build EventBridge → Firehose → S3 yourself. |

---

## 🧠 Exam One-Liners

- **"Aggregate findings from all services" = Security Hub.** It RECEIVES, doesn't generate.
- **Detective READS from SH (entry point for investigation). Never sends TO SH.**
- **SH = dashboard. Config = remediation. Don't confuse.**
- **Trusted Advisor ≠ Security Hub. No integration. Ever.**
- **SH is regional. Cross-region = designate aggregation region.**
