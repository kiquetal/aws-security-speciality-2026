# Dojo Practice Exam Set 2 — Full Review

> Date: 2026-06-09
> Score: **47/65 (72.31%)** | Time: 01:12:36
> Previous: Test 1 = 38/65 (58%) → **+14 points improvement**

---

## Domain Breakdown

| Domain | Score | Status | vs Test 1 |
|---|---|---|---|
| Detection | 100% | 🟢 | ↑ from 18% |
| Threat Detection + IR | 100% | 🟢 | ↑ from 0% |
| Infrastructure Security | 81.48% | 🟢 | ↑ from 72% |
| Incident Response | 80% | 🟢 | ↑ from N/A |
| Data Protection | 62.5% | 🟡 | ↓ from 75% |
| Identity and Access Management | 44.44% | 🔴 | ↑ from 37.5% |
| Management and Security Governance | 0% | 🔴 | ↓ from 100% |

---

## Questions You Got WRONG (18 total)

### 🔴 KMS Operational (should drill — testable patterns)

| Q# | Topic | Your Answer | Correct Answer | Difficulty |
|---|---|---|---|---|
| 22 | KMS key deleted, recover EBS | Contact AWS Support | Migrate data (rsync) to unencrypted volume | Medium |
| 33 | Encrypt data later, only need encrypted key | GenerateDataKey | **GenerateDataKeyWithoutPlaintext** | Medium |
| 43 | S3 >10GB upload fails with KMS (TWO) | Multipart + inline policy | Multipart + **kms:Decrypt** missing | Medium |
| 47 | EC2 can't start with encrypted EBS (TWO) | GenerateDataKey + Decrypt | **kms:CreateGrant** + kms:Decrypt | Hard |

### 🔴 IAM / Policy (should-have-known — concepts we drilled)

| Q# | Topic | Your Answer | Correct Answer | Difficulty |
|---|---|---|---|---|
| 3 | CW custom metrics stopped, least permissive | CloudWatchActionsEC2Access | `cloudwatch:PutMetricData` single action | Easy |
| 48 | Centrally allow/deny services per account | Organizations + OUs + custom IAM | Organizations + **SCPs** (least complexity) | Easy |
| 61 | Delegate user creation with restrictions | SCPs | **Permission Boundaries** | Easy |
| 64 | IAM best practices (TWO) | Least privilege + inline policies | Least privilege + **delete root access keys** | Easy |
| 65 | SCP missing S3 allow | "IAM policy missing perms" | **SCP is ceiling** — IAM has s3:* but SCP blocks | Medium |

### 🟡 Service Selection (tricky wording)

| Q# | Topic | Your Answer | Correct Answer | Difficulty |
|---|---|---|---|---|
| 11 | App users upload to S3, need role | GetSessionToken | **AssumeRoleWithWebIdentity** | Medium |
| 12 | Edge security for public app (TWO) | WAF+CF + geo-restriction | **WAF on ALB** + CloudFront with WAF | Medium |
| 25 | EKS audit + runtime + alert | GD + Security Hub + EB | GD EKS + Runtime Monitoring + **EventBridge→SNS direct** | Hard |
| 40 | Cross-account audit fails (THREE) | GetAccessKeyInfo + AssumeRole + ARN | **ExternalID** + AssumeRole + ARN | Medium |
| 44 | Auto-remediate VPC Flow Logs | Lambda remediation | **SSM runbook** (least config) | Medium |
| 55 | Deploy to EC2 + on-prem | Secrets Manager + Elastic Beanstalk | Parameter Store + **CodeDeploy** (EB can't do on-prem) | Medium |
| 60 | Track IAM permission changes over time | GenerateCredentialReport + Lambda | **AWS Config** (configuration history) | Medium |

### ⚪ Trivia (memorization — one read fixes)

| Q# | Topic | Your Answer | Correct Answer | Difficulty |
|---|---|---|---|---|
| ~13 | SNI multiple domains on same IP | GWLB | **CloudFront/ALB** (GWLB is L3, no TLS) | Easy |
| ~14 | SES TLS port | (didn't know) | **Port 587** (STARTTLS) | Trivia |
| 49 | Custom protocol + load balancer | ALB HTTPS | **NLB TCP passthrough** (ALB = HTTP only) | Medium |

---

## Decision Trees to Memorize

### KMS Permissions for EBS
```
Start existing encrypted volume  = kms:CreateGrant + kms:Decrypt
Create new encrypted volume      = kms:CreateGrant + kms:GenerateDataKey(WithoutPlaintext)
```

### GenerateDataKey Variants
```
Need plaintext NOW to encrypt     = GenerateDataKey (returns both)
Encrypt LATER (store key for now) = GenerateDataKeyWithoutPlaintext (encrypted copy only)
```

### S3 Upload with KMS
```
Single upload (< 5GB)   = kms:GenerateDataKey only
Multipart upload (> 5GB) = kms:GenerateDataKey + kms:Decrypt (reassembly)
```

### "Least Complexity/Config" Signals
```
Remediation     = SSM runbook (pre-built) > Lambda (custom code)
Org-wide policy = SCPs (one policy) > custom IAM per account
```

### Deploy To On-Prem
```
CodeDeploy        = ✅ EC2 + on-prem
Elastic Beanstalk = ❌ EC2 only (never on-prem)
```

### AssumeRole Variants
```
Web/mobile app users  = AssumeRoleWithWebIdentity
Enterprise SAML (AD)  = AssumeRoleWithSAML
EC2/Lambda/existing   = AssumeRole
MFA enforcement       = GetSessionToken
```

### Load Balancer Protocol Support
```
ALB  = HTTP/HTTPS/gRPC only (terminates TLS)
NLB  = TCP/UDP/TLS (any protocol, passthrough)
GWLB = L3 IP packets (security appliances, never terminates TLS)
```

---

## Key Concepts Learned

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
