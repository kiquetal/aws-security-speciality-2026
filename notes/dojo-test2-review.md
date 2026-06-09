# Dojo Practice Exam Set 2 — Review in Progress

> Date: 2026-06-09
> Status: IN PROGRESS

---

## Questions Flagged During Exam

| Q# | Topic | Your Issue | Correct Answer |
|---|---|---|---|
| 4 | KMS AAD / tamper-proof ciphertext | Didn't recognize Encryption Context term | Encryption Context |
| ~5-6 | SSE-C + Elastic Beanstalk considerations | Needed clarification on HMAC / instance profile | HTTPS mandatory + you manage keys |
| ~7 | Lambda + Parameter Store SecureString | Didn't connect to kms:Decrypt pattern | ssm:GetParameter + kms:Decrypt |
| ~8 | IoT credential storage, cost-effective + audit | Confused KMS (encrypt) with storage | Parameter Store SecureString |
| ~9 | IDS/IPS vs WAF (SQLi+XSS+DDoS) | Didn't know IDS/IPS as option vs WAF | WAF (app-layer attacks) |
| ~10 | Exceeded SG/NACL limits, no cost | Didn't think of host-based | iptables (free, unlimited) |
| ~11 | KMS key deleted, recover EBS data | Contact AWS Support | Migrate data from encrypted volume to unencrypted volume |
| ~12 | Inspect IP packet content (select TWO) | Needed clarification | Host-based agent + proxy on EC2 |
| ~13 | SNI - multiple domains SSL on same IP | Confused GWLB with TLS termination | CloudFront + ACM + SNI (GWLB is L3 only, no TLS) |
| ~14 | SES TLS port | Never studied SES ports | Port 587 (STARTTLS) |
| ~15 | S3 large file upload fails with KMS | Didn't know multipart needs kms:Decrypt | Multipart completion requires kms:Decrypt (single upload only needs GenerateDataKey) |

---

## Questions You Got WRONG (18 total)

| Q# | Topic | Your Answer | Correct Answer |
|---|---|---|---|
| 3 | CW custom metrics stopped - IAM fix | CloudWatchActionsEC2Access managed policy | `cloudwatch:PutMetricData` (least permissive) |
| 4 | KMS AAD / tamper-proof ciphertext | (flagged) | Encryption Context |
| ~5-6 | SSE-C + Elastic Beanstalk | (flagged) | HTTPS mandatory + you manage keys |
| ~7 | Lambda + SecureString | (flagged) | ssm:GetParameter + kms:Decrypt |
| ~8 | IoT credential storage | KMS | Parameter Store SecureString |
| 11 | App uploads to S3, needs role | GetSessionToken | AssumeRoleWithWebIdentity |
| 12 | Edge security for public app (TWO) | WAF+CF + geo-restriction | WAF on ALB + CloudFront with WAF |
| ~13 | SNI multiple domains | GWLB | CloudFront + ACM + SNI |
| ~14 | SES TLS port | (didn't know) | Port 587 (STARTTLS) |
| ~15 | S3 large file upload fails KMS | Picked inline policy size restriction | Multipart upload + kms:Decrypt missing |
| 22 | KMS key deleted, recover EBS | Contact AWS Support | Migrate data from encrypted volume to unencrypted volume |
| 25 | EKS audit logs + runtime monitoring | GD EKS + Security Hub + EventBridge | GD EKS Protection + Runtime Monitoring + EventBridge + SNS (direct, no SH needed) |
| 33 | Encrypt data later, get encrypted key only | GenerateDataKey | GenerateDataKeyWithoutPlaintext |
| 40 | Cross-account audit access issues (THREE) | GetAccessKeyInfo + AssumeRole + ARN | ExternalID + AssumeRole + ARN |
| 43 | S3 large file upload fails KMS (TWO) | Multipart + inline policy | Multipart + kms:Decrypt missing |
| 44 | Auto-remediate VPC without Flow Logs | Lambda remediation action | SSM runbook remediation action (least config overhead) |
| 47 | EC2 can't start with encrypted EBS (TWO) | GenerateDataKey + Decrypt | kms:CreateGrant + kms:Decrypt |
| 48 | Centrally manage policies across accounts | Organizations + OUs + custom IAM policy | Organizations + SCPs (least complexity) |
| 49 | Custom protocol encryption + load balancer | ALB HTTPS termination | NLB TCP passthrough (custom protocol ≠ HTTP, ALB can't handle) |
| 55 | Deploy app to EC2 + on-prem, secure DB creds | Secrets Manager + Elastic Beanstalk | Parameter Store SecureString + CodeDeploy (EB can't deploy to on-prem) |
| 60 | Track IAM permission changes over time | GenerateCredentialReport + Lambda + S3 | AWS Config (tracks resource config history, point-in-time) |
| 61 | Delegate user creation with restrictions | SCPs | Permission Boundaries (ceiling on created users) |
| 64 | IAM best practices (TWO) | Least privilege + inline policies | Least privilege + delete root access keys |
| 65 | SCP missing S3 allow, can't create bucket | "IAM policy doesn't have S3 permissions" | SCP doesn't allow s3:* — SCP is ceiling, IAM policy DOES have s3:* but SCP blocks it |

---

### KMS Key Deleted + EBS Recovery
- During `PendingDeletion` window: instance can still READ the mounted volume
- Use `rsync` to copy data from encrypted volume to a new unencrypted volume
- You CANNOT: regenerate the same key, disable encryption on existing volume, or get AWS to recover the key
- Once key is fully deleted = data permanently unrecoverable
- Prevention: SCP Deny `kms:ScheduleKeyDeletion`

### Encryption Context (KMS AAD)
- Key-value pairs passed at encrypt/decrypt time
- Must match at decrypt (tamper-proof)
- Logged in CloudTrail (audit)
- Can use in key policy conditions (`kms:EncryptionContext:key`)

### CloudTrail Insights vs GuardDuty
- Insights = unusual API call VOLUME (statistical baseline)
- GuardDuty = malicious BEHAVIOR (threat intel)
- Neither supports custom thresholds like "3 in 5 min"
- Custom thresholds = CloudWatch metric filter + alarm

### SSE-C
- HTTPS mandatory (S3 rejects HTTP)
- You send key with EVERY request (GET and PUT)
- S3 stores HMAC of key (fingerprint for validation), discards actual key
- Lose key = lose data

### Credential Storage Decision Tree
- Store + rotation + RDS = Secrets Manager
- Store + audit + cost-effective + no rotation = Parameter Store SecureString
- Encrypt only (no storage) = KMS
- Custom schema = DynamoDB (overkill for simple credentials)

### Parameter Store SecureString + Lambda
- Lambda needs: ssm:GetParameter + kms:Decrypt
- Same pattern as S3 SSE-KMS: caller needs explicit KMS permission
- AWS-managed key (aws/ssm) may auto-grant in some contexts
- Customer-managed key = always explicit kms:Decrypt required

---

## Final Score

**Score: 47/65 (72.31%)** | Time: 01:12:36

### Domain Breakdown

| Domain | Score | Status | vs Test 1 |
|---|---|---|---|
| Detection | 100% | 🟢 | ↑ from 18% |
| Threat Detection + IR | 100% | 🟢 | ↑ from 0% |
| Infrastructure Security | 81.48% | 🟢 | ↑ from 72% |
| Incident Response | 80% | 🟢 | ↑ from N/A |
| Data Protection | 62.5% | 🟡 | ↓ from 75% |
| Identity and Access Management | 44.44% | 🔴 | ↑ from 37.5% |
| Management and Security Governance | 0% | 🔴 | ↓ from 100% |

### Analysis

**Massive improvement:** 58% → 72% (+14 points!)

**Locked domains (80%+):**
- Detection: 100% (was 18% — complete turnaround)
- Threat Detection + IR: 100%
- Infrastructure Security: 81%
- Incident Response: 80%

**Still failing:**
- IAM: 44% — likely operational IAM (ADFS, federation, policy interpretation) not our policy-layers focus
- Governance: 0% — suspicious (may be 1-2 questions, small sample)
- Data Protection: 62.5% — SSE-C, multipart KMS, credential storage gaps

### Key Gap Categories (Test 2 specific)
1. Operational IAM: ADFS federation, instance profiles, AD integration
2. KMS operational: multipart upload permissions, encryption context
3. Service trivia: SES ports, GWLB vs ALB, SNI
4. Credential storage: Parameter Store vs Secrets Manager vs KMS decision tree

---
