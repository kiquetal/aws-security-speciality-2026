# Diagram Index

> 61 files (30 Mermaid + 31 PNG). Organized by exam domain for quick lookup.

---

## D1: Detection (16%)

| Diagram | Format | Description |
|---|---|---|
| [d1-detection-decision-flowchart](d1-detection-decision-flowchart.png) | mmd+png | Service selection: EventBridge vs GuardDuty vs Config vs AA vs Inspector vs Detective |
| [stoplogging-detection-paths](stoplogging-detection-paths.png) | mmd+png | StopLogging: CW=blind, EventBridge=seconds, Config=minutes (WHY for each) |
| [security-services-comparison](security-services-comparison.png) | mmd+png | Side-by-side: GuardDuty vs Inspector vs Macie vs Config vs Security Hub |
| [security-services-complete-map](security-services-complete-map.png) | mmd+png | Full map of all security services and their relationships |
| [log-source-coverage](log-source-coverage.png) | mmd+png | Which log sees what (VPC Flow, TGW Flow, ELB, Resolver, CloudTrail) |
| [session-manager-logging](session-manager-logging.png) | mmd+png | Session Manager logging flow to CW Logs / S3 |

## D2: Incident Response (14%)

| Diagram | Format | Description |
|---|---|---|
| [ir-containment-decision-tree](ir-containment-decision-tree.png) | mmd+png | OutsideAWS vs InsideAWS vs Credential Leak — containment actions for each |
| [rds-incident-response-flow](../aws-incident-response-demonstrated-microcredential/diagrams/rds-incident-response-flow.png) | png | RDS compromise IR flow |
| [iam-backdoor-eradication-flow](../aws-incident-response-demonstrated-microcredential/diagrams/iam-backdoor-eradication-flow.png) | png | IAM backdoor cleanup steps |
| [scp-external-trust-prevention](../aws-incident-response-demonstrated-microcredential/diagrams/scp-external-trust-prevention.png) | png | SCP to prevent external trust policies |

## D3: Infrastructure Security (18%)

| Diagram | Format | Description |
|---|---|---|
| [aws-firewalls-compared](aws-firewalls-compared.png) | mmd+png | All 5 firewall layers compared (WAF, Shield, SG/NACL, NF, DNS FW) |
| [route53-dns-firewall](route53-dns-firewall.png) | mmd+png | DNS Firewall rule evaluation flow |
| [session-manager-vpc-endpoints](session-manager-vpc-endpoints.png) | mmd+png | SSM via VPC endpoints (3 endpoints needed) |
| [hub-and-spoke-tgw](hub-and-spoke-tgw.png) | mmd+png | Transit Gateway hub-and-spoke with inspection VPC |
| [cloudfront-oac](cloudfront-oac.png) | mmd+png | CloudFront OAC + SSE-KMS pattern |
| [hybrid-connectivity-decision](hybrid-connectivity-decision.png) | mmd+png | Site-to-Site VPN vs Client VPN vs DX decision tree |

## D4: Identity & Access Management (20%)

| Diagram | Format | Description |
|---|---|---|
| [policy-evaluation-with-rcps](policy-evaluation-with-rcps.png) | mmd+png | 5-gate policy evaluation (SCP→RCP→Boundary→Identity→Resource) |
| [iam-policy-evaluation-boundaries](iam-policy-evaluation-boundaries.png) | mmd+png | Permission boundary intersection logic |
| [permission-boundary-delegation](permission-boundary-delegation.png) | mmd+png | Boundary delegation pattern (force boundary on CreateRole) |
| [rcp-exemption-paths](rcp-exemption-paths.mmd) | mmd | Two RCP exemption paths (SLR structural + PrincipalIsAWSService) |
| [abac-tag-flow](abac-tag-flow.png) | mmd+png | ABAC: PrincipalTag vs ResourceTag vs RequestTag flow |
| [cross-account-s3-kms](cross-account-s3-kms.png) | mmd+png | Cross-account S3+KMS 3-policy pattern |
| [iam-roles-sequence](iam-roles-sequence.png) | png | Role assumption sequence diagram |
| [delegated-admin-pattern](delegated-admin-pattern.png) | mmd+png | Delegated admin account pattern |

## D5: Data Protection (18%)

| Diagram | Format | Description |
|---|---|---|
| [envelope-encryption-flow](envelope-encryption-flow.png) | mmd+png | KMS envelope encryption (GenerateDataKey → encrypt locally) |
| [kms-key-lifecycle](kms-key-lifecycle.png) | mmd+png | Key states: Enabled→Disabled→PendingDeletion→Deleted |
| [kms-key-store-backends](kms-key-store-backends.png) | mmd+png | Default vs CloudHSM custom vs XKS comparison |
| [kms-grants-cross-account](kms-grants-cross-account.png) | mmd+png | KMS Grants for dynamic cross-account access |
| [kms-grant-token-flow](kms-grant-token-flow.png) | mmd+png | Grant token for immediate use (eventual consistency workaround) |
| [kms-decrypt-key-routing](kms-decrypt-key-routing.png) | mmd+png | How Decrypt auto-routes to correct key version via ciphertext metadata |
| [imported-key-rotation](imported-key-rotation.png) | mmd+png | Manual rotation procedure: new key + import + alias swap |
| [secret-retrieval-deploy-vs-boot](secret-retrieval-deploy-vs-boot.png) | mmd+png | Deploy-time (CF ValueFrom) vs boot-time (runtime API call) |

## D6: Governance (14%)

| Diagram | Format | Description |
|---|---|---|
| [d6-governance-decision-tree](d6-governance-decision-tree.png) | mmd+png | Verb-to-service: RAM vs FM vs StackSets vs Service Catalog vs SCP vs Config vs cfn-guard |
| [study-progress-gantt](study-progress-gantt.png) | mmd+png | Study timeline and milestones |

## UI Mockups / Screenshots

| Diagram | Format | Description |
|---|---|---|
| [dashboard](dashboard.png) | png | Security Hub dashboard screenshot |
| [sessions_tab](sessions_tab.png) | png | Session Manager sessions tab |
| [start_session_modal](start_session_modal.png) | png | Session Manager start modal |
| [interactive_quiz_dojo_mockup](interactive_quiz_dojo_mockup.png) | png | Dojo quiz interface mockup |

---

## Quick Stats

- **Total diagrams:** 67 files
- **Mermaid sources (.mmd):** 33
- **Rendered PNGs:** 34
- **Domains covered:** All 6
- **Most covered:** D5 Data Protection (8), D4 IAM (8), D3 Infrastructure (6), D1 Detection (6)
- **Least covered:** D6 Governance (2), D2 Incident Response (4)
