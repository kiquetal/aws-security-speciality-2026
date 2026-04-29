# Exam Day Quick Reference

## The Golden Rule

```
Detect → Contain → Eradicate → Recover
```

**Never skip steps. Order matters.**

## Containment Cheat Sheet

| Scenario | Action |
|----------|--------|
| Compromised EC2 | Replace SG with empty SG → Snapshot EBS → Investigate on forensic copy |
| Public S3 bucket | Config rule → EventBridge → Lambda (`PutBucketPolicy` + `PutPublicAccessBlock`) |
| Compromised IAM user | Delete backdoor keys → Audit policies → Remove unauthorized policies → Revoke sessions (inline deny-all) → Reissue credentials |
| Compromised RDS | Restrict SG → Manual snapshot → Review audit logs → Rotate credentials → Restore from known-good snapshot |

## Session Revocation Policy (memorize this)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "DateLessThan": {
          "aws:TokenIssueTime": "<REMEDIATION_TIMESTAMP>"
        }
      }
    }
  ]
}
```

- `Action: "*"` — not `sts:*` (deny everything, not just STS)
- Only affects **temporary credentials** — long-term keys must be deleted separately

## Service → Purpose Map

| Service | Incident Response Role |
|---------|----------------------|
| CloudTrail | **Detect** — who did what, when |
| Config | **Detect** — is the resource compliant? |
| CloudWatch | **Detect** — metrics, logs, alarms |
| Athena | **Detect** — SQL queries on CloudTrail logs in S3 |
| EventBridge | **Route** — match events, trigger targets |
| SNS | **Notify** — alert security team |
| Lambda | **Remediate** — single-action fixes |
| Step Functions | **Orchestrate** — multi-step workflows with error handling |
| Systems Manager | **Manage** — remote access, patching, automation |
| VPC (SG/NACL) | **Contain** — network isolation |
| EC2 Auto Scaling | **Recover** — replace compromised instances |
| IAM | **Eradicate** — revoke access, delete keys |
| S3 | **Preserve** — store logs, snapshots |
| RDS | **Protect** — encryption, auth, audit |

## Common Traps

1. **Stopping an EC2 instance is NOT containment** — it destroys volatile evidence
2. **Deactivating access keys is NOT eradication** — they can be reactivated
3. **Denying `sts:*` is NOT enough** — use `Action: "*"` in session revocation
4. **Config is NOT enabled by default** — must be turned on per region
5. **EventBridge IS always enabled** — services emit events automatically
6. **RDS encryption must be set at creation** — cannot encrypt existing unencrypted DB in place
