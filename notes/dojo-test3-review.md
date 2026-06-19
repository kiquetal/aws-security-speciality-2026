# Dojo Practice Exam Set 3 — Full Review

> Date: 2026-06-19
> Score: 31/65 (48%)
> Purpose: Capture ALL wrong questions for targeted gap analysis and re-drill.

---

## Questions for Review

### Q55 — S3 Data Exfiltration via Proxy (Select TWO)

**Scenario:** EC2 in private subnet, proxy in public subnet. Rogue employee exfils to external S3 bucket using own AWS creds. Mitigate without affecting other workloads.

**Your Answer:** C + D (NACL on app subnet + proxy block)
**Correct:** D + E (proxy block + VPC Gateway endpoint with restrictive endpoint policy)

**Key concept:** Gateway endpoint policy = allowlist for ALL S3 traffic from VPC. If destination bucket not in policy = denied at your network boundary. Attacker's creds irrelevant.

---

### Q64 — Config Delivery to S3 Failure (Select TWO)

**Scenario:** Config error "unable to write to bucket." Fix?

**Your Answer:** A + C (trust relationship + bucket policy)
**Correct:** C + E (bucket policy for config.amazonaws.com + role needs s3:GetBucketAcl + s3:PutObject*)

**Key concept:** "Unable to write" = role already assumed (trust is fine). Fix = bucket policy + GetBucketAcl + PutObject. Same pattern as S3 server access logging.

---

### Q65 — GuardDuty Email Notifications (medium+high)

**Scenario:** Org-wide GuardDuty, send email for medium+high findings. Most operationally efficient.

**Your Answer:** (TBD — paste your answer)
**Correct:** GuardDuty delegated admin → EventBridge rule (severity filter) → SNS → email

**Key concept:** GuardDuty publishes to EventBridge natively. No Lambda needed. Delegated admin sees all org findings.

---

<!-- TEMPLATE: Add more questions below as you review them -->

