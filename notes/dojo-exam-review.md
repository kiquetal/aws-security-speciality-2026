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

---

## Q20 — Disable Instance Metadata (Task 3.2)

**Scenario:** Prevent users on shared EC2 from using metadata to attack other resources.

**Answer:** Turn off access to instance metadata (`HttpEndpoint: disabled`).

**Key concepts:**
- Inspector, GuardDuty, SSM Agent cannot disable metadata
- Metadata controlled at EC2 level: `modify-instance-metadata-options --http-endpoint disabled`
- If metadata not needed, disable entirely. If needed, enforce IMDSv2.

---

## Q21 — SSL VPN for Remote Workers (Task 3.3)

**Scenario:** Employees work from home, need access to enterprise apps, not publicly accessible.

**Answer:** SSL VPN in public subnet + apps in private subnet + VPN client on laptops.

**Key concepts:**
- SSL VPN (client-to-site) = individual remote users
- IPsec VPN (site-to-site) = two fixed networks
- Direct Connect = physical link, not Internet-based
- ALB + HTTPS alone doesn't restrict to employees only

---

## Q22 — CloudWatch Metric Filter for SG Changes (Task 1.3)

**Scenario:** CloudWatch alarm for SG changes not firing when inbound rule added.

**Answer:** (1) Filter pattern must include `AuthorizeSecurityGroupIngress` (2) Metric filter must have metric value of 1.

**Key concepts:**
- AuthorizeSecurityGroupIngress = add inbound SG rule
- CreateNetworkAclEntry = NACL, not SG
- Metric value = 1 per event (not 10)
- Inspector doesn't monitor SG changes

---

## Q23 — CloudFront + ALB HTTPS Certificates (Task 5.1)

**Scenario:** HTTPS client→CF→ALB (us-west-1), custom domain on CF.

**Answer:** ACM cert in us-east-1 for CloudFront + ACM cert in us-west-1 for ALB.

**Key concepts:**
- CloudFront custom domain cert = ALWAYS us-east-1
- ALB cert = same region as ALB
- Lambda@Edge ≠ TLS termination

---

## Q24 — KMS Key Policy Root Principal (Task 5.2)

**Scenario:** Key policy grants `arn:aws:iam::111122223333:root` with `kms:*`. What does it do?

**Answer:** Enables IAM delegation — allows any principal in that account to manage key access via IAM policies.

**Key concepts:**
- Root in key policy ≠ "only root user"
- Root in key policy = "enable IAM policies to control this key"
- Each principal still needs explicit KMS permissions in their identity policy

---

## Q25 — CloudWatch Logs Agent Troubleshooting (Task 1.3)

**Scenario:** EC2 instances stopped sending logs to CloudWatch.

**Answer:** Check `/var/log/awslogs.log` for runtime errors.

**Key concepts:**
- `/var/log/awslogs.log` = runtime errors (logs stopped flowing)
- `/var/log/awslogs-agent-setup.log` = installation errors only
- GuardDuty Trusted IP list irrelevant to log delivery

---

## DOJO EXAM RESULTS — 2026-06-05

**Score: 38/65 (58.46%)**
**Time: 53:09**

### Domain Breakdown

| Domain | Score | Status |
|---|---|---|
| Data Protection | 75% | 🟢 |
| Infrastructure Security | 72% | 🟡 |
| Security Foundations and Governance | 100% | 🟢 |
| Security Logging and Monitoring | 100% | 🟢 |
| Detection | 18% | 🔴 CRITICAL |
| Identity and Access Management | 37.5% | 🔴 CRITICAL |
| Threat Detection and Incident Response | 0% | 🔴 CRITICAL |
| Not categorized | 50% | 🟡 |

### Analysis

- D6 Governance + Logging/Monitoring = LOCKED (100%)
- D5 Data Protection + D3 Infrastructure = SOLID (72-75%)
- D1 Detection + D4 IAM + D2 IR = FAILING

### Next Steps
- Bring back all wrong answers for targeted drill
- Focus: Detection, IAM, Incident Response
- These are likely DIFFERENT question styles than our practice (Dojo uses different wording/scenarios)

---

## FULL EXAM DUMP — All 65 Questions with Answers

### Questions You Got WRONG (27 questions):

| # | Topic | Your Error | Correct Answer |
|---|---|---|---|
| 5 | AD trust direction | Picked wrong trust direction | AWS Managed AD + one-way trust (AWS trusts on-prem) |
| 9 | CloudTrail multi-account S3 | Missed log file validation | New account + bucket policy s3:PutObject + log file validation |
| 10 | GuardDuty master/member permissions | Confused what members can/can't do | Members can't archive findings, can't manage IP lists |
| 12 | SQS access troubleshooting | Missed resource policy check | IAM role allows SQS + SQS resource policy doesn't deny |
| 13 | CW Logs agent troubleshooting | Picked wrong option | Log rotation + duplicate [logstream] sections |
| 16 | CloudTrail management events config | Picked SNS config issue | Trail management events must be Write-only or All |
| 17 | S3 encryption (company manages keys) | Missed client-side option | SSE-C + client-side encryption with own master key |
| 19 | VPC Flow Logs NACL | Picked SG instead of NACL | NACL blocks outbound (stateless) |
| 22 | GuardDuty Trusted IP list | Picked wrong option | EIPs + Trusted IP list |
| 25 | Compromised credential investigation | Missed CloudWatch option | CloudTrail console + CloudWatch Log queries |
| 26 | KMS auto-rotation | Missed one type | Custom key store + Asymmetric + Imported = no auto rotation |
| 29 | ENI troubleshooting | Missed ALB target registration | Correct ENI→SG mapping + instance registered in ALB |
| 30 | IoT Core client ID injection | Picked wrong combo | ThingName policy + client ID verification + Device Defender |
| 38 | IAM policy interpretation | Missed reading from all buckets | s3:Get*/List* on Resource:* = read ALL buckets |
| 41 | Kinesis + OpenSearch for logs | Missed the combo | Kinesis (real-time) + OpenSearch (analytics) |
| 43 | ACM certificates for CF+ALB | Picked wrong region combo | us-east-1 for CF + us-west-1 for ALB |
| 44 | CloudTrail all regions | Picked wrong service | CloudTrail trail applied to all regions |
| 47 | KMS Grants | Picked key policy or IAM | Grants = programmatic, per-app, revocable |
| 48 | AD federation with AWS | Picked wrong options | ADFS relying party trust + IAM roles + AssumeRoleWithSAML |
| 50 | Secrets Manager in CF | Picked Parameter Store | Secrets Manager + {{resolve:secretsmanager:...}} |
| 52 | CloudTrail multi-account troubleshoot | Missed one answer | Trail active + correct bucket + bucket policy with account IDs |
| 55 | Disable instance metadata | Picked SSM Agent | Turn off metadata (HttpEndpoint: disabled) |
| 56 | Remote access for employees | Picked wrong VPN type | SSL VPN (client-to-site) in public subnet + apps in private |
| 57 | CW metric filter for SG changes | Missed metric value | AuthorizeSecurityGroupIngress filter + metric value = 1 |
| 61 | NACL ephemeral ports | Picked SG ephemeral | NACL outbound rule for ports 1024-65535 |
| 63 | CW Logs agent log file | Picked setup log | /var/log/awslogs.log (runtime) not setup.log |
| 65 | S3 + SSE-KMS | Picked SSE-S3 or Glacier | S3 + SSE-KMS (envelope encryption + audit trail + rotation) |

### Key Gaps Identified:

1. **AD/Directory Service** — trust directions, ADFS federation
2. **Operational troubleshooting** — agent logs, NACL ephemeral ports, metric filters
3. **KMS Grants vs key policies** — programmatic delegation
4. **IoT Core** — thing policy variables, client ID security
5. **VPN types** — SSL VPN vs IPsec vs Direct Connect
6. **S3 encryption matrix** — SSE-S3 vs SSE-KMS vs SSE-C vs client-side
7. **GuardDuty master/member permissions** — who can archive, who manages IP lists
8. **CloudTrail configuration** — management events Write-only/All requirement for EventBridge
