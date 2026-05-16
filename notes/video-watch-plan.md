# Cybr.com Video Watch Plan — Gap-Based Priority

> Based on question tracker analysis (149 questions, 23 sessions)
> Updated: 2025-05-15
> **Full catalog:** [video-catalog.md](./course/video-catalog.md)

---

## 🔴 MUST WATCH (directly addresses weak spots)

| # | Video Title | Gap | Status |
|---|---|---|---|
| 1 | About Amazon GuardDuty | GuardDuty vs Inspector confusion | ✅ Done |
| 2 | [LAB] Amazon GuardDuty Demo | Finding types, hands-on | ⏭️ Skipped (requires subscription) |
| 3 | Amazon Detective | Swapped with CloudTrail under pressure | ✅ Done |
| 4 | About IAM Access Analyzer | Confused with GuardDuty | ✅ Done |
| 5 | IAM Access Analyzer Unused Access | Two modes distinction | ✅ Done |
| 6 | Using Step Functions for Security Workflows | Missed IR orchestration (Q138) | ✅ Done |
| 7 | Automatically remediating incidents | Full IR automation pipeline | ✅ Done |
| 8 | About AWS Firewall Manager | RAM vs FM distinction (Q126) | ✅ Done |
| 9 | Using AWS RAM to share resources across accounts | Keep picking Control Tower | ✅ Done |
| 10 | Incident containment in AWS | IR sequence + validate findings | ✅ Done |

---

## 🟡 SHOULD WATCH (from full catalog — fills remaining gaps)

| # | Video Title | Why | Status |
|---|---|---|---|
| 11 | Delegating and Centralizing GuardDuty | You just asked how this works | ✅ Done |
| 12 | Delegating and Centralizing Detective | Same delegated admin pattern | ⬜ |
| 13 | About AWS Security Hub CSPM | Never watched, exam-critical service | ⬜ |
| 14 | Delegating and Centralizing Security Hub CSPM | Org-wide aggregation pattern | ⬜ |
| 15 | [Quiz] Security Monitoring and Threat Detection | Free test of D1 knowledge | ⬜ |
| 16 | CloudWatch Logs data protection policies | Data masking (new in C03) | ✅ Done |
| 17 | [LAB] Protect CloudWatch Logs data with masking policies | Hands-on data masking | ⬜ |
| 18 | AWS hybrid and remote connectivity | MACsec = Layer 2 on dedicated DX | ✅ Done |
| 19 | Amazon Route 53 Resolver query logs | DNS Firewall context (Q129, Q134) | ✅ Done |
| 20 | Test and validate your IR plans | Fault Injection Service (new in C03) | ⬜ |
| 21 | [Scenario] Alert and monitoring for all root activities | Practical exam scenario | ⬜ |
| 22 | Incident management with SSM OpsCenter and Explorer | IR tooling gap | ⬜ |
| 23 | [Quiz] Automatically remediate incidents | Free test of D2 knowledge | ⬜ |

---

## ⏭️ SKIP (mastered — 80%+ accuracy)

- All IAM policy/role videos
- All KMS videos (grants, rotation, key stores)
- All S3 security videos (Object Lock, encryption, cross-account)
- SCPs, RCPs, Control Tower conceptual videos
- CloudTrail, CloudTrail Lake
- VPC endpoints, Session Manager
- Config, EventBridge
- CloudFront OAC, WAF, Shield
- Organizations, Identity Center
- EBS/EFS encryption, Secrets Manager
- CloudFormation, Service Catalog
- Macie (already watched)

---

## Recommended Watch Order

### Session 1 (~90 min) — Detection + Analysis ✅ COMPLETE
- [x] About Amazon GuardDuty
- [-] [LAB] Amazon GuardDuty Demo (requires subscription — skipped)
- [x] Amazon Detective
- [x] About IAM Access Analyzer
- [x] IAM Access Analyzer Unused Access

### Session 2 (~60 min) — IR + Governance
- [x] About AWS Firewall Manager
- [x] Using AWS RAM to share resources across accounts
- [x] Incident containment in AWS
- [x] Using Step Functions for Security Workflows
- [x] Automatically remediating incidents

### Session 3 (~45 min) — Delegated Admin + Security Hub
- [x] Delegating and Centralizing GuardDuty
- [ ] Delegating and Centralizing Detective
- [ ] About AWS Security Hub CSPM
- [ ] Delegating and Centralizing Security Hub CSPM
- [ ] [Quiz] Security Monitoring and Threat Detection

### Session 4 (~30 min, 1.5x speed) — Fill Remaining Gaps
- [ ] AWS hybrid and remote connectivity
- [ ] Amazon Route 53 Resolver query logs
- [ ] CloudWatch Logs data protection policies
- [ ] Test and validate your IR plans

### Session 5 (optional — labs/scenarios)
- [ ] [Scenario] Alert and monitoring for all root activities
- [ ] Incident management with SSM OpsCenter and Explorer
- [ ] [Quiz] Automatically remediate incidents

---

## After All Videos: Final Re-test

1. EC2 connecting to botnet IP — which service generates the finding?
2. "Which S3 buckets are accessible externally?" — which service?
3. Multi-step IR (isolate → snapshot → tag → notify) — which service orchestrates?
4. Share DNS Firewall rule groups to all accounts — which service?
5. Ensure all ALBs have WAF rules, auto-remediate — which service?
6. Dedicated Direct Connect, Layer 2 encryption — which feature?
7. Before full IR, check if finding is false positive — what's this step called?
