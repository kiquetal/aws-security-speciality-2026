# SCS-C03 Question Tracker

> Track every question attempted. Review ❌ and ⚠️ items before the exam.

## Session: 2025-05-01

| # | Question / Scenario | Your Answer | Correct? | Correct Answer | Review Topic |
|---|---|---|---|---|---|
| 1 | S3 bucket exfiltrated object-by-object — which CloudTrail event type captures it? Is it enabled by default? | "Not enabled by default, PutEvent" | ⚠️ Half right | Data events, **GetObject** (not Put). Not enabled by default. | CloudTrail data vs management events |
| 2 | Lambda functions with prefix `UpdProdCount` — most flexible way to log invocations? | Didn't know | ❌ | Advanced event selectors with `StartsWith` on resource ARN | Basic vs Advanced event selectors |
| 3 | Session Manager — what security advantage from a network perspective? | "No open ports" | ✅ | No inbound ports needed — outbound HTTPS only | Session Manager |
| 4 | NACLs or Security Groups — which is stateless and needs ephemeral ports? | "NACLs, 100% sure" | ✅ | NACLs are stateless | NACLs vs Security Groups |
| 5 | Detect public S3 buckets org-wide with least overhead (options: Security Hub, Inspector, Detective, CloudWatch) | Didn't know | ❌ | **Security Hub** — built-in S3 controls, org-wide | Security services comparison |
| 6 | Lambda stopped logging — Config + what? (IAM Access Analyzer vs Security Hub vs CloudWatch Logs Insights) | Confused | ⚠️ | Depends on scenario — if role changed: Config + IAM Access Analyzer. If role is fine: CloudWatch Logs Insights | Troubleshooting (Task 1.3) |
| 7 | Resource-based policy vs RCP — what's the difference? | Confused them | ⚠️ | RBP = per-resource, grants access. RCP = org-wide ceiling, never grants. | Policy layers reference |
| 8 | Can you rotate imported KMS key material? | "Yes" | ✅ | Yes, but only manually (alias swap) | KMS rotation matrix |
| 9 | KMS imported key — who owns durability? | "You" | ✅ | You — AWS doesn't back up imported material | KMS imported keys |
| 10 | Import NEW material into EXISTING key? | Knew it was wrong | ✅ | ❌ Can't — only re-import SAME material. New material = new key + alias swap. | KMS imported keys |
| 11 | Why can't you use RAM for KMS cross-account? | "RAM is not for sharing?" | ⚠️ | RAM IS for sharing, but doesn't support KMS. Use KMS Grants. | RAM vs KMS Grants |
| 12 | RAM vs RCP — what's the difference? | "Didn't remember RCP" | ⚠️ | RAM shares infrastructure. RCP restricts data access. Opposite problems, different services. | faq-ram-vs-rcp.md |
| 13 | Suspicious root login attempts — GuardDuty vs CloudTrail + CloudWatch? | Chose CloudTrail + CloudWatch | ❌ | **GuardDuty + EventBridge** — "suspicious" = GuardDuty, least overhead | GuardDuty vs CloudTrail |
| 14 | Lambda in private subnet — restrict domain lookup to one domain? | Didn't know | ❌ | **Route 53 Resolver DNS Firewall** | DNS Firewall |
| 15 | Cross-account S3 + SSE-KMS — how many policies needed? | Got Account A right, missed Account B | ⚠️ | THREE: bucket policy + key policy + identity policy on caller | Cross-account patterns |
| 16 | When to use RCP — identify the use case? | Got it after review | ✅ | "Outsiders + my data + org-wide" → RCP | RCP use cases |
| 17 | GuardDuty — what is it responsible for? | "GuardDuty" (for crypto mining) | ✅ | Threat detection — active malicious behavior | Security services |
| 18 | Security Hub setup order — 4 steps? | Followed along | ✅ | Enable SH → make admin → enable members → assume roles | Security Hub |
| 19 | `aws:PrincipalIsAWSService` — when to use? | Understood after explanation | ✅ | Always add when using PrincipalOrgID deny — exempts CloudTrail, Config, etc. | RCP conditions |
| 20 | VPC endpoints — why 3 for Session Manager? | Understood | ✅ | `ssm` (API) + `ssmmessages` (session) + `ec2messages` (heartbeat) | Session Manager VPC endpoints |

## Session: 2026-05-02

| # | Question / Scenario | Your Answer | Correct? | Correct Answer | Review Topic |
|---|---|---|---|---|---|
| 21 | Root user API calls from unexpected country — detect + isolate with least overhead? | B: GuardDuty → EventBridge → Step Functions | ✅ | GuardDuty for behavioral threats, Step Functions for orchestration | Security services comparison (re-test Q13) |
| 22 | Log only `Prod-*` Lambda invocations, exclude read-only, queryable in Lake? | B: Advanced event selectors with StartsWith + readOnly + eventName | ✅ | Advanced selectors required for prefix, Lake requires advanced | CloudTrail advanced selectors (re-test Q2) |
| 23 | What is CloudTrail Lake? What problem does it solve? | Didn't know it existed | ❌ | Managed query engine — replaces S3+Athena plumbing, near real-time, dashboards | CloudTrail Lake vs S3+Athena |

## Score Summary (Cumulative)

| Result | Session 1 | Session 2 (re-test) | Total |
|---|---|---|---|
| ✅ Correct | 10 | 2 | 12 |
| ⚠️ Partial | 6 | 0 | 6 |
| ❌ Wrong | 4 | 1 | 5 |

## Score Summary

| Result | Count | Percentage |
|---|---|---|
| ✅ Correct | 10 | 50% |
| ⚠️ Partial / needed help | 6 | 30% |
| ❌ Wrong / didn't know | 4 | 20% |

## Weak Areas to Review

1. **Security services comparison** — which service for which question (Q5, Q13)
2. **CloudTrail event types** — data vs management, advanced selectors (Q1, Q2)
3. **Cross-account access** — all three policies needed (Q15)
4. **DNS Firewall** — new service, need practice (Q14)
5. **Policy layers** — RBP vs RCP distinction (Q7, Q12)

## Files to Re-Read

- `notes/faq-security-services-comparison.md` — Q5, Q13
- `notes/faq-cloudtrail.md` — Q1, Q2
- `notes/policy-layers-reference.md` — Q7, Q12, Q19
- `notes/faq-route53-resolver.md` — Q14
- `examples/cross-account-s3-kms.md` — Q15
