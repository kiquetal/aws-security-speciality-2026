# Dojo Practice Exam — Questions for Review

> Date: 2026-06-05
> Purpose: Save questions encountered during Dojo exam for post-exam study.

---

## Q1 — Directory Service (Task 4.1)

**Scenario:** 100 accounts in Organizations. Cloud users must be in separate auth domain, prevented from accessing on-prem. On-prem AD admins must access RDS SQL Server + EC2.

**Answer:** AWS Managed Microsoft AD + one-way forest trust.

**Key concepts:**
- Simple AD = no trust capability (Samba-based)
- AD Connector = proxy only, no separate domain
- Managed AD = full MS AD, supports trusts, creates separate domain

**Gap:** We never drilled Directory Service differences.

---

## Q2 — CloudTrail Log Integrity (Task 1.2)

**Scenario:** Enable log integrity validation.

**Key concepts:**
- Integrity = SHA-256 digest files (detect tampering)
- Encryption = SSE-S3/SSE-KMS (prevent reading)
- Different controls, enable both

---

## Q3 — Cross-Account Billing Access (Task 4.2)

**Scenario:** Finance team in TD-Finance needs read billing in TD-Master, nothing else.

**Answer:** Cross-account IAM role in TD-Master with trust to TD-Finance + billing-only permissions.

---

## Q4 — CloudTrail Insights vs Regular Events (Task 1.1)

**Scenario:** EventBridge rule on specific access key usage not sending SNS alerts.

**Answer:** SNS topic misconfiguration (empty ARN or missing publish permissions).

**Key concepts:**
- CloudTrail Insights = anomaly detection (unusual volume), NOT individual event tracking
- Regular management events already log access key usage
- Troubleshoot the plumbing (SNS permissions), not the detection

---

## Q5 — VPC Flow Logs NACL Troubleshooting (Task 3.3)

**Scenario:** Ping inbound ACCEPT, outbound REJECT.

**Answer:** NACL missing outbound rule (stateless). SG is stateful so wouldn't cause this.

**Rule:** Inbound ACCEPT + Outbound REJECT = NACL problem.

---

## Q6 — WAF Rate-Based Rule + User-Agent (Task 3.1)

**Scenario:** DDoS-like flood with specific User-Agent from multiple IPs.

**Answer:** WAF on ALB with rate-based rule matching User-Agent header.

**Key concepts:**
- WAF attaches to ALB/CloudFront, NEVER to EC2
- Multiple IPs = IP set won't scale
- Rate-based + string match = surgical block

---

## Q7 — GuardDuty Trusted IP List (Task 1.1)

**Scenario:** Suppress findings from authorized security testing EC2 instances.

**Answer:** Attach EIPs + add to GuardDuty Trusted IP list.

**Key concepts:**
- Trusted IP list = public IPs only (need EIPs)
- GuardDutyExcluded tag = Malware Protection only, not port scan findings
- Suppression rules = alternative (auto-archive), not offered here

---

## Q8 — KMS Auto Rotation Support (Task 5.2)

**Scenario:** Some keys failed to enable auto-rotation.

**Answer:** Custom key store + Asymmetric + Imported = no auto rotation.

**Rule:** Auto rotation ONLY for symmetric + AWS-generated + default key store.

---

## Q9 — CloudTrail Not Delivering to S3 (Task 1.3)

**Scenario:** Multi-account CloudTrail not delivering to central S3 bucket.

**Answer:** (1) Bucket policy restricting regions (2) Requester Pays disabled (3) Prefix in bucket policy correct.

**Key concepts:**
- CORS irrelevant (not browser)
- VPC endpoint irrelevant (CloudTrail uses AWS backbone)
- Requester Pays must be OFF

---

## Q10 — IoT Core Client ID Injection (Task 3.2)

**Scenario:** Malware injects special chars in MQTT client ID to access unauthorized topics.

**Answer:** Bind client ID to ThingName + IoT policy restricts iot:Connect to `client/${iot:Connection.Thing.ThingName}`.

**Key concepts:**
- ThingName = server-registered (trusted)
- ClientId = client-supplied (untrusted)
- Client-side validation useless against malware

---

## Q11 — VPC DNS Disable (Task 3.3)

**Scenario:** Prevent EC2 from using Amazon-provided DNS (169.254.169.253).

**Answer:** Set enableDnsSupport to false in VPC.

**Key concepts:**
- 169.254.169.253 is link-local, not routable via SG/NACL/route tables
- Only VPC attribute can disable it

---

## Q12 — Perfect Forward Secrecy (Task 5.1)

**Scenario:** Which services offer PFS cipher suites?

**Answer:** CloudFront + Elastic Load Balancers.

**Key concept:** PFS = ECDHE cipher suites. Services that terminate TLS connections.

---

## Q13 — ACM Cross-Account Subdomain Validation (Task 5.1)

**Scenario:** Wildcard cert for dev.tutorialsdojo.com pending validation. CNAME in Account 2 zone.

**Answer:** Add NS delegation records in parent zone (Account 1) pointing to Account 2's nameservers.

**Key concept:** Without NS delegation in parent, child zone is invisible to internet.

---

## Q14 — CloudFront + ALB Certificates (Task 5.1)

**Scenario:** HTTPS client→CF→ALB with custom domain.

**Answer:** One cert in us-east-1 (CloudFront) + one cert in us-west-1 (ALB region).

**Rule:** CloudFront custom domain cert MUST be in us-east-1. ALB cert in ALB's region.

---

## Q15 — CloudTrail All Regions (Task 1.2)

**Scenario:** Track activities across all regions.

**Answer:** Create CloudTrail trail applied to all regions.

---

## Q16 — On-Prem AD Federation (Task 4.1)

**Scenario:** Federate on-prem AD with AWS.

**Answer:** ADFS relying party trust + IAM roles + AssumeRoleWithSAML.

**Key concepts:**
- Federated users = roles, NEVER IAM users/groups
- Cognito = customer apps, not enterprise workforce
- RAM = resource sharing, not identity

---

## Q17 — CloudTrail Event History (Task 1.2)

**Scenario:** Investigate access key usage past 3 months, quickly, no cost.

**Answer:** CloudTrail console Event History (free, 90 days, filter by access key).

**Key concepts:**
- Athena = costs money
- CloudWatch Logs = needs setup
- Event History = free, immediate, 90 days

---

## Q18 — Secrets Manager in CloudFormation (Task 5.3)

**Scenario:** API keys in CF template, encrypted, not plaintext.

**Answer:** Secrets Manager + `{{resolve:secretsmanager:...}}` dynamic reference.

**Key concepts:**
- `{{resolve:ssm:...}}` = standard parameter (plaintext)
- `{{resolve:ssm-secure:...}}` = SecureString
- Secrets Manager = highest security for credentials

---

## Q19 — Cross-Account CloudTrail to Central S3 (Task 1.2)

**Scenario:** 3 accounts not delivering logs to central bucket.

**Answer:** (1) Verify trail active + correct bucket name (2) Bucket policy must include those account IDs.

**Key concepts:**
- Each account's trail must point to correct bucket
- Central bucket policy must list allowed account IDs
- No "global CloudTrail config" in master that controls others
