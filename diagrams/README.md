# Diagrams

## Tldraw Diagrams (visual study aids)

| File | Topic | Key Exam Pattern |
|------|-------|-----------------|
| `aws-policy-5-gates-tldraw.png` | Policy evaluation: SCP → RCP → Boundary → Identity → Resource | All 5 gates must allow. Explicit Deny wins. |
| `s3-object-lock-tldraw.png` | Governance vs Compliance vs Legal Hold vs Glacier Vault Lock | "Fixed period" = Compliance. "24hr confirm permanent" = Vault Lock. |
| `kms-key-types-tldraw.png` | AWS Managed vs Customer Managed vs Imported | Imported = no auto-rotation, YOU own durability. |
| `traffic-inspection-tldraw.png` | Traffic Mirroring (passive) vs GWLB (inline) vs Network Firewall | "IDS/observe" = Mirror. "Palo Alto" = GWLB. "Suricata" = NF. |
| `log-destinations-tldraw.png` | Which log source writes to S3 / CW Logs / Firehose / EventBridge | ELB/CF/S3 = S3 ONLY. DNS public = CW ONLY. |
| `ir-outside-aws-tldraw.png` | OutsideAWS containment: TokenIssueTime vs shared role vs memory | "Shared role" = never TokenIssueTime. "Memory" = AMI first. |
| `ir-inside-asg-alb-tldraw.png` | InsideAWS + ASG detach + ALB deregister ordering | ASG = detach first. ALB only = acquire first, deregister last. |
| `ir-credential-leak-tldraw.png` | IAM user keys on GitHub: 5-step ordering | Inactivate → Create → Update → Revoke STS → Delete console. |

## Mermaid Diagrams

| File | Topic |
|------|-------|
| `policy-evaluation-with-rcps.*` | Policy evaluation flow with RCPs |
| `iam-policy-evaluation-boundaries.*` | IAM boundaries evaluation |
| `security-services-comparison.*` | GuardDuty vs Macie vs Inspector vs Config |
| `security-services-complete-map.*` | Full detection → aggregation → response pipeline |
| `cross-account-s3-kms.*` | Three-policy cross-account pattern |
| `kms-grants-cross-account.*` | KMS Grants for dynamic access |
| `cloudfront-oac.*` | OAC vs OAI for S3 origins |
| `session-manager-logging.*` | Session Manager three logging layers |
| `session-manager-vpc-endpoints.*` | SSM VPC endpoint requirements |
| `route53-dns-firewall.*` | DNS Firewall rule evaluation |
| `guardduty-org-setup.*` | Delegated admin pattern |
| `kms-access-control-myths.*` | Root ≠ full access, creator ≠ owner |

## How tldraw diagrams are generated

See `.kiro/steering/tech.md` for the pipeline:

```
Node.js script (Puppeteer + bundled tldraw editor)
  → creates shapes via editor API
  → exports .tldr file
  → tldraw-cli renders to PNG
```

The tldraw MCP (`@talhaorak/tldraw-mcp`) manages `.tldr` files but CANNOT export to PNG due to schema incompatibility with `@kitschpatrol/tldraw-cli`.
