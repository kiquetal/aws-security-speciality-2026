# Next Session — Dojo Combined Gap Drill

> Source: Dojo Test 1 (27 wrong) + Dojo Test 2 (18 wrong) = 45 total, deduplicated to ~25 unique patterns
> Target: 10 killer questions covering the most frequent/impactful gaps
> Format: Exam-style, novel scenarios, Dojo-style wording

---

## Priority 1: KMS Operational (failed in BOTH tests)

- GenerateDataKey vs GenerateDataKeyWithoutPlaintext
- kms:CreateGrant for EBS start (vs GenerateDataKey)
- Multipart upload needs kms:Decrypt
- KMS key deleted → rsync data before expiry
- KMS Grants vs key policy (when to use which)
- Encryption Context = AAD

**Generate: 3 questions**

---

## Priority 2: IAM Wording Traps (failed in BOTH tests)

- "Least permissive" = single action (not managed policy)
- Permission Boundaries (delegate creation) vs SCP (restrict account)
- SCP is ceiling — if not listed, blocked
- AssumeRoleWithWebIdentity vs GetSessionToken vs AssumeRoleWithSAML
- ExternalID for confused deputy (not GetAccessKeyInfo)
- AWS Config for "track changes over time / point-in-time"

**Generate: 3 questions**

---

## Priority 3: Service/Architecture Selection (failed in BOTH tests)

- NLB (custom protocol) vs ALB (HTTP only) vs GWLB (appliances, L3)
- CloudFront/ALB for SNI (not GWLB)
- CodeDeploy (on-prem) vs Elastic Beanstalk (EC2 only)
- SSM runbook (least config) vs Lambda (custom code)
- Parameter Store SecureString (cost-effective) vs Secrets Manager (rotation)
- Kinesis (real-time ingest) + OpenSearch (analytics)
- GuardDuty direct to EventBridge (no Security Hub middle layer needed)

**Generate: 2 questions**

---

## Priority 4: Operational Troubleshooting (Test 1 heavy)

- NACL stateless: inbound ACCEPT + outbound REJECT = NACL
- CW Logs agent: /var/log/awslogs.log (runtime) not setup.log
- CloudTrail: Write-only trail = ConsoleLogin won't fire EventBridge
- GuardDuty Trusted IP list = PUBLIC IPs only
- AD: Managed AD + one-way trust (need trusts/separate domain)
- VPN: Site-to-Site (offices) vs Client VPN (laptops)

**Generate: 2 questions**

---

## Delivery Rules

- 10 questions total
- Exam format (scenario + 4-5 options)
- Novel wording (don't repeat Dojo verbatim)
- Include at least 2 "Select TWO" questions
- At least 1 cross-domain combo
- Use "LEAST permissive/MOST cost-effective/LEAST overhead" wording traps
