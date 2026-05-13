# FAQ: Detect vs Prevent — The Verb Tells You the Service

> **Blueprint refs:** Task 1.1 (monitoring), Task 3.3 (network controls), Task 4.2 (authorization)
> **Purpose:** The exam uses "detect" and "prevent/block/restrict" as signals. Wrong verb = wrong answer.

## The Rule

```
"DETECT" / "identify" / "alert" / "monitor"  → DETECTION service (passive)
"PREVENT" / "block" / "restrict" / "enforce"  → CONTROL/POLICY (active)
```

## Decision Matrix

| Scenario Verb | Answer Category | Specific Service |
|---|---|---|
| "Detect external decryption" | Detection | **GuardDuty** (S3 Protection) |
| "Prevent external decryption" | Control | **KMS key policy** (PrincipalOrgID condition) |
| "Detect C2 communication" | Detection | **GuardDuty** |
| "Block C2 domains" | Control | **DNS Firewall** |
| "Detect public S3 buckets" | Detection | **Security Hub** / Config |
| "Prevent public S3 buckets" | Control | **S3 Block Public Access** / SCP |
| "Detect compromised credentials" | Detection | **GuardDuty** |
| "Revoke compromised credentials" | Control | **Inline Deny + TokenIssueTime** |
| "Detect overly permissive policies" | Detection | **IAM Access Analyzer** |
| "Prevent overly permissive policies" | Control | **Permission boundary** / SCP |
| "Detect malware on EBS" | Detection | **GuardDuty Malware Protection** |
| "Block malware in traffic" | Control | **Network Firewall** (Suricata IPS) |
| "Detect DNS exfiltration" | Detection | **GuardDuty** (DNS logs) |
| "Block DNS exfiltration" | Control | **DNS Firewall** |
| "Detect non-compliant resources" | Detection | **Config** / Security Hub |
| "Enforce compliance" | Control | **SCP** / Config auto-remediation |
| "Detect external S3 access" | Detection | **GuardDuty S3 Protection** |
| "Block external S3 access" | Control | **RCP** (PrincipalOrgID) |

## Exam Traps

1. **"Detect" + "least overhead"** → GuardDuty or Security Hub (managed, no infra)
2. **"Prevent" + "org-wide"** → SCP (principals) or RCP (resources)
3. **"Detect AND respond"** → GuardDuty + EventBridge + Lambda/Step Functions
4. **CloudTrail is neither** — it's the LOG SOURCE. It doesn't detect or prevent. Other services read CloudTrail to detect.

## 🧠 Cheat-Sheet One-Liners

- **The verb tells you the service.** "Detect" = GuardDuty/Security Hub/Config. "Prevent" = policy/firewall.
- **CloudTrail + condition key = prevention.** GuardDuty = detection. Don't mix them.
- **"Detect external decryption" = GuardDuty. "Prevent external decryption" = key policy.**
