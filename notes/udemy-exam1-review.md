# Udemy Practice Exam 1 — Full Review

> Date: 2026-06-19
> Score: TBD (partial paste — at least 11 wrong so far)
> Provider: TBD
> Purpose: Gap analysis and targeted re-drill

---

## Questions for Review

### Q7 — ELB Access Logs Destination (S3, not CW Logs)

**Scenario:** Replace on-prem LB with ELB. Centralize logs for audit + create TLS cipher metrics.

**Your Answer:** CW Logs log group + metric filters
**Correct:** S3 bucket + Athena queries + publish custom metrics to CloudWatch

**Key concept:** ELB access logs are delivered to S3 ONLY — never directly to CloudWatch Logs. Athena queries S3 directly. Metric filters only work on CW Logs log groups (not S3 files).

**Rule:** ELB access logs → S3 (only destination). Search = Athena. Metrics = Athena query → PutMetricData to CloudWatch.

---

### Q9 — MFA Condition Keys (MultiFactorAuthPresent + MultiFactorAuthAge)

**Scenario:** Require MFA for EC2 actions + session valid max 3 hours.

**Your Answer:** MaxSessionDuration + TokenIssueTime
**Correct:** `aws:MultiFactorAuthPresent: true` + `aws:MultiFactorAuthAge` NumericLessThan 10800

**Key concept:** 
- `aws:MultiFactorAuthPresent` = Bool, require MFA on request
- `aws:MultiFactorAuthAge` = seconds since MFA auth (NumericLessThan for max session)
- `MaxSessionDuration` = NOT a condition key (it's a role setting)
- `aws:TokenIssueTime` = date of token issuance (different purpose: revoking sessions)

**Rule:** MFA enforcement = MultiFactorAuthPresent (Bool). MFA session timeout = MultiFactorAuthAge (NumericLessThan, seconds). These are the ONLY two MFA condition keys.

---

### Q11 — EC2 IR Containment: NACL vs Security Group (Stateful Problem)

**Scenario:** Isolate EC2 immediately, keep running, instance is ONLY resource in subnet.

**Your Answer:** Modify current SG, remove all rules
**Correct:** New NACL with explicit deny all, associate with subnet

**Key concept:** Security groups are STATEFUL — removing rules does NOT kill EXISTING connections (tracked connections continue). NACLs are STATELESS — evaluate every packet independently, immediately cut existing flows. "Blocks traffic as quickly as possible" for EXISTING active connections = NACL.

**Rule:** "Immediately cut existing connections" = NACL (stateless, kills active flows). "Prevent new connections" = SG works fine. The verb matters: "as quickly as possible" with active connections = NACL wins.

**⚠️ IMPORTANT:** This contradicts standard IR practice (deny-all SG). The difference is the question says "blocks traffic as quickly as possible" with "currently has active network connections." SG change won't kill tracked connections. NACL will.

---

### Q14 — AWS Backup: Cron vs Rate for Specific Dates

**Scenario:** DynamoDB backup on 10th and 20th of month at 1:00 AM, retain 4 months.

**Your Answer:** Rate expression (wrong) + PITR (wrong)
**Correct:** AWS Backup + cron expression + 4-month retention

**Key concept:**
- `rate()` = fixed interval (every X hours/days) — can't target specific calendar dates
- `cron()` = specific dates/times (10th and 20th at 1:00 AM)
- PITR = continuous recovery window, NOT discrete scheduled backups
- AWS DataSync = data transfer, NOT backup

**Rule:** "Specific calendar dates" = cron. "Every X hours/days" = rate. PITR ≠ scheduled backups.

---

### Q16 — KMS Key Type: Customer Managed + Auto-Rotation + Control

**Scenario:** EBS encrypted, yearly snapshots 7yr, auto-rotation yearly, control key policies, old snapshots still decryptable.

**Your Answer:** Imported key material
**Correct:** Symmetric customer managed KMS key (AWS-generated material)

**Key concept:**
- Imported key material = NO auto-rotation (manual only)
- AWS managed key = NO control over key policies
- Customer managed + AWS-generated = auto-rotation ✅ + full control ✅ + old versions kept forever ✅
- Asymmetric = not supported for EBS

**Decision Grid:**

| Need | Customer Managed (AWS-generated) | Customer Managed (Imported) | AWS Managed |
|------|---|---|---|
| Auto-rotation | ✅ | ❌ | ✅ (but you can't configure it) |
| Control key policy | ✅ | ✅ | ❌ |
| Cross-account sharing | ✅ | ✅ | ❌ |
| Old data still decryptable after rotation | ✅ (all versions kept) | N/A (no auto-rotation) | ✅ |
| Set expiration on key material | ❌ | ✅ (only option!) | ❌ |

**Rule:** "Full control + auto-rotation + no overhead" = customer managed with AWS-generated material. Imported = no auto-rotation. AWS managed = no control.

---

### Q17 — GuardDuty Trusted IP List: Plaintext + S3

**Scenario:** Internal IPs generating findings, confirmed trusted, suppress in GuardDuty.

**Your Answer:** JSON file (wrong format)
**Correct:** Plaintext file (required format) + upload to S3 + configure trusted IP list pointing to S3

**Key concept:**
- GuardDuty trusted IP list = PLAINTEXT file format (not JSON)
- File must be stored in S3
- GuardDuty references the S3 location
- Once active, GD stops generating findings for those IPs
- Trusted IP list = PUBLIC IPs only (reminder from previous learning)

**Rule:** GuardDuty IP lists = plaintext file in S3. Not JSON. Not DynamoDB. Not DNS Firewall.

---

### Q20 — IR Forensics: State Manager for Automated Snapshots

**Scenario:** Preserve volatile + non-volatile, tag with ticket, keep online, isolate, capture investigative activity. Least overhead.

**Your Answer:** Manual EBS snapshot + tag (partially right but missed automation)
**Correct:** (1) SG isolation + termination protection + detach ASG/LB, (2) SSM Run Command for volatile memory, (3) State Manager association for automated EBS snapshots + tagging

**Key concept:**
- State Manager association = AUTOMATES snapshot + tagging (less overhead than manual)
- SSM Run Command = execute memory collection scripts on live instance
- Manual EBS snapshot = works but not "least overhead" (no automation)
- Moving to isolation VPC/subnet = more complex than SG change

**Rule:** "Least operational overhead" for repeated forensic tasks = State Manager (automates). Manual snapshot = correct action but higher overhead.

---

### Q21 — Investigate GuardDuty Finding: Detective (not CloudTrail Insights)

**Scenario:** Impact:IAMUser/AnomalousBehavior finding. Investigate in context. Don't affect production.

**Your Answer:** CloudTrail Insights + CloudTrail Lake
**Correct:** Amazon Detective

**Key concept:**
- Detective = purpose-built for investigating GuardDuty findings in context (entities, timelines, relationships)
- CloudTrail Insights = detects unusual API volume PATTERNS (not for investigating a specific finding)
- CloudTrail Lake = SQL queries on API calls (useful but not the contextual investigation tool)
- "Investigate finding in context" = always Detective

**Rule:** "Investigate GuardDuty finding in context" = Detective. Insights = volume anomaly detection. Lake = SQL queries. Different tools, different jobs.

---

### Q22 — S3 Encryption Header: x-amz-server-side-encryption (not x-amz-meta-side-encryption)

**Scenario:** Encrypt at rest + in transit + monitor endpoints. Select THREE.

**Your Answer:** x-amz-meta-side-encryption (wrong header name)
**Correct:** x-amz-server-side-encryption (correct header)

**Key concept:** The correct S3 server-side encryption header is `x-amz-server-side-encryption`. The `x-amz-meta-*` prefix is for custom metadata headers. Confusing these = wrong bucket policy condition.

**Rule:** SSE enforcement header = `x-amz-server-side-encryption`. `x-amz-meta-*` = custom metadata (user-defined, not encryption).

---

### Q23 — End-to-End Encryption: Import Third-Party Cert (Private Key Available)

**Scenario:** ALB public-facing, need TLS client→ALB AND ALB→EC2. End-to-end.

**Your Answer:** ACM Amazon-issued cert on ALB + separate cert for EC2 + mTLS
**Correct:** Import third-party cert to ACM (for ALB) + install same cert on EC2 instances

**Key concept:**
- ACM Amazon-issued certs: private key NOT exportable → can't install on EC2
- Imported third-party certs: private key IS available → can install on both ALB and EC2
- Self-signed: works technically but browsers won't trust it (public-facing = bad UX)
- "End-to-end" = both legs need TLS = need cert material on EC2

**Rule:** "End-to-end encryption ALB→EC2" = need private key on EC2. ACM-issued = not exportable. Imported third-party = exportable. That's the only option that works both sides.

---

### Q28 — IAM Paths + SCP Deny iam:PassRole (not AssumeRole)

**Scenario:** Group IAM roles by team + only platform team can delegate roles to AWS services.

**Your Answer:** Tags + SCP deny iam:PassRole for non-platform policies (wrong target)
**Correct:** IAM paths (group roles) + SCP deny iam:PassRole except platform team PATH

**Key concept:**
- `iam:PassRole` = delegate a role TO an AWS service (Lambda, EC2, ECS assume it)
- `sts:AssumeRole` = one principal assumes another role (different action entirely)
- IAM paths = logical grouping of roles (/product/, /security/, /platform/)
- SCP exception by path = `arn:aws:iam::*:role/platform/*`

**Rule:** "Delegate roles to AWS services" = iam:PassRole. "Assume a role" = sts:AssumeRole. Different actions for different scenarios. PassRole = give service permission to use a role.

---

### Q30 — Traffic Mirroring for Passive Full-Packet IDS (not GWLB, not Flow Logs)

**Scenario:** IDS on dedicated EC2, inspect FULL packets (not just metadata), passive monitoring.

**Your Answer:** GWLB endpoint (inline, not passive)
**Correct:** VPC Traffic Mirroring → NLB target → monitoring EC2

**Key concept:**
- Traffic Mirroring = passive COPY of packets (out-of-band, IDS)
- GWLB = INLINE inspection (IPS, changes traffic path)
- VPC Flow Logs = metadata only (IP, port, accept/reject — NO payload)
- Promiscuous mode = doesn't work in VPC (AWS doesn't forward other ENI's traffic)

**Rule:** "Passive full-packet inspection (IDS)" = Traffic Mirroring. "Inline inspection/blocking (IPS)" = Network Firewall or GWLB. "Metadata only" = Flow Logs.

---

### Q33 — CloudWatch Agent + CW Logs Retention (not S3 Lifecycle for ASG logs)

**Scenario:** Auto Scaling EC2, logs lost on scale-in, retain 6 years.

**Your Answer:** EBS snapshots daily (wrong approach)
**Correct:** CW agent continuously streams → CW Logs + 6yr retention + IAM role on launch template

**Key concept:**
- CW agent = continuous streaming (logs leave instance as generated)
- Scale-in = instance gone, but logs already in CW Logs
- S3 batch upload (every 24hr) = gap window for data loss
- EBS snapshots = block storage backup, not searchable log solution
- CW Logs retention = native setting per log group (up to 10 years)

**Rule:** "No log loss during scaling" = continuous stream off-instance (CW agent). Batch/scheduled = always has a loss window.

---

### Q35 — CloudFormation Service Role (cloudformation.amazonaws.com trust)

**Scenario:** CF stack deployments fail for some team members. Use service role for consistent perms.

**Your Answer:** Service Catalog portfolio (changes deployment model, doesn't fix root cause)
**Correct:** (1) Create CF service role trusting cloudformation.amazonaws.com, (2) attach policies targeting actual AWS resources (not stack ARNs), (3) update stacks to use the role

**Key concept:**
- CF service role = CF assumes this role during deployment (consistent perms for everyone)
- Trust policy must specify `cloudformation.amazonaws.com`
- Policies on the role target the RESOURCES CF creates (Lambda, IAM, EC2 etc.) not the CF stack ARN itself
- Every stack must be updated to USE the role

**Rule:** "CF deployments inconsistent across team members" = create CF service role + update stacks to use it. Policies target actual AWS resources, not stack ARNs.

---

## Gap Analysis Summary

| Gap Pattern | Questions | Already Known? | Priority |
|---|---|---|---|
| **Service-specific log destinations** (ELB→S3 only) | Q7 | Partially (knew CW Logs agent) | 🔴 New |
| **IAM condition keys** (MFA pair, not MaxSessionDuration) | Q9 | ❌ Never drilled | 🔴 New |
| **NACL vs SG for active connections** (stateless kills tracked) | Q11 | ⚠️ Knew stateless but missed IR implication | 🟡 Reinforce |
| **Cron vs Rate expressions** (calendar dates = cron) | Q14 | ❌ Never drilled | 🟡 New |
| **KMS key type selection** (imported = no auto-rotation) | Q16 | ✅ Known (missed under pressure) | 🟢 Recall |
| **GuardDuty IP list format** (plaintext + S3) | Q17 | ⚠️ Knew S3, missed format | 🟡 Detail |
| **State Manager for IR automation** | Q20 | ⚠️ Knew concept, missed exam application | 🟡 Reinforce |
| **Detective vs Insights vs Lake** (investigate finding = Detective) | Q21 | ✅ Known (missed under pressure) | 🟢 Recall |
| **S3 encryption header exact name** | Q22 | ❌ Detail never drilled | 🔴 New |
| **ACM cert exportability** (imported = exportable, Amazon-issued = not) | Q23 | ❌ Never drilled | 🔴 New |
| **iam:PassRole vs sts:AssumeRole** | Q28 | ⚠️ Knew PassRole exists, confused application | 🟡 Reinforce |
| **Traffic Mirroring vs GWLB** (passive vs inline) | Q30 | ⚠️ Knew from Dojo 3 Q26 (same gap!) | 🔴 Repeat error |
| **CW agent continuous vs batch** (no loss during scaling) | Q33 | ✅ Known (missed under pressure) | 🟢 Recall |
| **CF service role pattern** | Q35 | ❌ Never drilled | 🔴 New |

### New Gaps (Not in Previous Drills)
1. ELB logs → S3 only (never CW Logs directly)
2. `aws:MultiFactorAuthPresent` + `aws:MultiFactorAuthAge` condition keys
3. `x-amz-server-side-encryption` exact header name
4. ACM Amazon-issued = private key not exportable
5. CF service role = trusts cloudformation.amazonaws.com
6. Cron vs Rate expressions for scheduling
7. NACL for killing active tracked connections (SG won't)

### Repeat Errors (Same Gap as Dojo 3!)
1. Traffic Mirroring vs GWLB vs Network Firewall (passive vs inline) — **failed TWICE now**
