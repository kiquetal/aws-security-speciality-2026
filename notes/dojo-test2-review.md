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
| ~11 | KMS key deleted, recover EBS data | Picked "disable encryption" | Contact AWS Support (or CancelKeyDeletion) |
| ~12 | Inspect IP packet content (select TWO) | Needed clarification | Host-based agent + proxy on EC2 |

---

## Key Concepts Encountered

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

> TBD — update after exam completion

---
