# Cybr.com Video Watch Plan — Gap-Based Priority

> Based on question tracker analysis (139 questions, 22 sessions)
> Generated: 2025-05-15

---

## 🔴 MUST WATCH (directly addresses weak spots)

| # | Video Title | Gap | Questions | Session Context |
|---|---|---|---|---|
| 1 | About Amazon GuardDuty | GuardDuty vs Inspector vs Access Analyzer confusion | Q116, Q132, Q145 | S20: didn't know Tor finding. S22: picked Inspector for botnet. Drill: picked GuardDuty for "what's exposed" |
| 2 | [LAB] Amazon GuardDuty Demo | Finding types, hands-on reinforcement | Q116, Q132 | See above — need to see real findings in console |
| 3 | Amazon Detective | Swapped with CloudTrail under pressure | Q109, re-test | S20 re-test Q4: said "CloudTrail" for investigation. Signal: "visualize/timeline/scope" = Detective |
| 4 | About IAM Access Analyzer | Confused "find what's exposed" with GuardDuty | Q145 | Drill round: "which buckets accessible externally?" — said GuardDuty. Access Analyzer = permission audit, not active threat |
| 5 | IAM Access Analyzer Unused Access | Different from external access findings | Q145 | Same confusion — Access Analyzer has TWO modes: external access + unused access |
| 6 | Using Step Functions for Security Workflows | Missed IR orchestration completely | Q138 | S22: "multi-step IR orchestration" — said "don't remember". Answer = Step Functions |
| 7 | Automatically remediating incidents | Full IR automation pipeline | Q138, Q147 | S22: missed Step Functions. Drill: missed "validate findings" step. Need full pipeline understanding |
| 8 | About AWS Firewall Manager | RAM vs FM distinction | Q126 | S21: "share DNS Firewall rule groups" — said Control Tower. FM = enforce/deploy. RAM = share. |
| 9 | Using AWS RAM to share resources across accounts | Keep picking Control Tower when it's RAM | Q126 | Same as above. RAM supports: TGW, subnets, DNS Firewall rule groups, Route 53 rules |
| 10 | Incident containment in AWS | IR sequence + validate findings step | Q147 | Drill: left blank for "validate findings before full IR". New in C03 (Task 2.2.3) |

---

## 🟡 SKIM (1.5x speed — fills smaller gaps)

| # | Video Title | Gap |
|---|---|---|
| 11 | AWS hybrid and remote connectivity | MACsec = Layer 2 on dedicated DX (Q149) |
| 12 | Amazon Route 53 Resolver query logs | DNS Firewall rule structure context (Q129, Q134) |
| 13 | [Cheat Sheet] The 6 phases of IR mapped to AWS services | Quick D2 reference |
| 14 | Test and validate your IR plans | Fault Injection Service (new in C03) |
| 15 | About Amazon Macie | Reinforce distinction from GuardDuty |
| 16 | CloudWatch Logs data protection policies | Data masking (new in C03) |

---

## ⏭️ SKIP (mastered — 80%+ accuracy)

- All IAM policy/role videos
- All KMS videos (grants, rotation, key stores)
- All S3 security videos (Object Lock, encryption, cross-account)
- SCPs, RCPs, Control Tower conceptual videos
- CloudTrail, CloudTrail Lake
- VPC endpoints, Session Manager
- Security Hub, Config
- CloudFront OAC, WAF, Shield
- Organizations, Identity Center
- EBS/EFS encryption
- Secrets Manager

---

## Recommended Watch Order

### Session 1 (~90 min) — Detection + Analysis
- [ ] About Amazon GuardDuty
- [ ] [LAB] Amazon GuardDuty Demo
- [ ] Amazon Detective
- [ ] About IAM Access Analyzer
- [ ] IAM Access Analyzer Unused Access

### Session 2 (~60 min) — IR + Governance
- [ ] About AWS Firewall Manager
- [ ] Using AWS RAM to share resources across accounts
- [ ] Incident containment in AWS
- [ ] Using Step Functions for Security Workflows
- [ ] Automatically remediating incidents

### Session 3 (~30 min, 1.5x speed) — Fill Remaining Gaps
- [ ] AWS hybrid and remote connectivity
- [ ] CloudWatch Logs data protection policies
- [ ] Test and validate your IR plans

---

## After Watching: Re-test These

Come back and answer these without notes:

1. EC2 connecting to botnet IP — which service generates the finding?
2. "Which S3 buckets are accessible externally?" — which service?
3. Multi-step IR (isolate → snapshot → tag → notify) — which service orchestrates?
4. Share DNS Firewall rule groups to all accounts — which service?
5. Ensure all ALBs have WAF rules, auto-remediate — which service?
6. Dedicated Direct Connect, Layer 2 encryption — which feature?
7. Before full IR, check if finding is false positive — what's this step called?
