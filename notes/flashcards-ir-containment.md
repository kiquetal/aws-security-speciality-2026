# Flashcards: Incident Response Containment

> Based on: `diagrams/ir-containment-decision-tree.png`
> Domain: D2 (14%) — 0 flashcards existed before this file
> Weak areas: #36, #37 (credential leak IR, OutsideAWS/InsideAWS)

---

## Containment Method by Finding Type

| Finding | Containment | WHY not the other? |
|---|---|---|
| OutsideAWS (API must stay up) | TokenIssueTime + EBS snapshot + IMDSv2 hop=1 | Deny-all SG kills legitimate traffic |
| OutsideAWS (can disrupt) | Deny-all SG + EBS snapshot + no-reboot AMI | Full isolation OK |
| InsideAWS | Deny-all SG on ATTACKER's instance | TokenIssueTime kills BOTH (same role) |
| Credential leak (keys on GitHub) | Deactivate keys + Deny * on IAM USER | Covers 2nd key + console + sessions |

## Quick-Fire (cover right column, recall)

| Q | A |
|---|---|
| OutsideAWS + can't stop instance = ? | TokenIssueTime (NOT deny-all SG) |
| InsideAWS = ? | Deny-all SG on attacker (NOT TokenIssueTime) |
| Why not TokenIssueTime for InsideAWS? | Both instances share same role — kills both |
| Why not deny-all SG for OutsideAWS + API up? | Kills legitimate API traffic |
| Credential leak — single broadest action? | Inline Deny * on IAM user |
| Why Deny * and not just deactivate keys? | Attacker may have created 2nd key + console access |
| Compromised ROLE = ? | TokenIssueTime (only temp creds exist) |
| Compromised IAM USER = ? | Deny * on user (keys + console = persistent) |
| Preserve volatile memory without stopping? | No-reboot AMI |
| Preserve disk evidence? | EBS snapshot |
| Prevent future SSRF after OutsideAWS? | IMDSv2 hop limit = 1 |
| Order: acquire or isolate first? | ACQUIRE first (deny-all blocks SSM needed for memory) |
| Forensics Orchestrator: deny-all then SSM fails — why? | Deny-all blocks outbound to SSM endpoints |
| Test IR pipeline without real incident? | CreateSampleFindings API (not FIS) |
| Assess RTO/RPO for auditors? | Resilience Hub (not FIS) |
| Shift traffic from bad AZ in seconds? | ARC zonal shift (not Route 53) |
| FIS does what? | Injects infra failures to TEST your plan |
| Detective entry point? | Needs an existing finding (no finding = CW Logs Insights) |
| Custom viz + reusable notebook for IR? | SageMaker notebooks (not Detective) |
