# Dojo Practice Exam Set 1 — Full 65 Questions Reference

> Score: 38/65 (58.46%) | Time: 53:09 | Date: 2026-06-05

---

## Questions You Got RIGHT (38):

| Q# | Topic | Correct Answer |
|---|---|---|
| 1 | Direct Connect vs VPN | AWS Direct Connect (bypasses Internet, dedicated) |
| 2 | CloudFront + S3 restrict direct access | OAC (Origin Access Control) |
| 3 | IAM policy interpretation (two S3 buckets) | Both buckets accessible (identity + resource policy union) |
| 4 | Medical records encryption in transit + at rest | Kinesis Data Streams + S3 SSE-KMS + Athena |
| 6 | Approved software enforcement | Service Catalog with portfolio |
| 7 | CloudTrail SSE-KMS encryption | SSE-KMS for multi-account, multi-region key control |
| 8 | KMS auto-rotation (correct THREE) | Custom key store + Asymmetric + Imported = no auto rotation |
| 11 | Cross-account billing access | IAM role in TD-Master with ViewBilling + trust to TD-Finance |
| 14 | DynamoDB client-side encryption | DynamoDB Encryption Client |
| 15 | DDoS attack surface reduction | SG+CF+Shield Advanced + NACL+WAF |
| 18 | S3 HIPAA encryption | SSE-S3 AES-256 + client-side encryption |
| 20 | WAF rate-based rule + User-Agent | WAF on ALB + rate-based + User-Agent match |
| 21 | Audit log retention 5 years | S3 Glacier + Vault Lock policy |
| 23 | S3 bucket policy ARN fix | Change Resource to arn:aws:s3:::bucket/* |
| 24 | Envelope encryption description | Encrypt data with data key, encrypt data key with KEK |
| 27 | VPC to KMS private connection | VPC endpoint for KMS + aws:sourceVpce condition |
| 31 | Auto-remediate SG 0.0.0.0/0 | Config rule + SSM Automation + Lambda |
| 33 | Lambda shared connection string to Aurora | Systems Manager Parameter Store SecureString |
| 34 | Perfect Forward Secrecy | CloudFront + ELB |
| 35 | KMS resource-based access controls | Key policies + Grants |
| 36 | RDS authentication token | IAM DB Authentication |
| 37 | S3 access policy types | Bucket policy + IAM User policy |
| 39 | FIPS 140-2 HSM exclusive control | CloudHSM |
| 42 | S3 client-side encryption (keys never in AWS) | Client-side encryption with client-side master key |
| 45 | Route 53 query logs retention | CloudWatch Logs retention policy |
| 46 | IAM security improvements | MFA + strong password policy |
| 51 | Dedicated FIPS 140-2 HSM | CloudHSM |
| 53 | Automated unauthorized API alert | CloudTrail + CloudWatch metric filter + alarm + SNS |
| 54 | On-prem AD integration with AWS | AWS Directory Service |
| 58 | RSA asymmetric keys in dedicated HSM | Import to CloudHSM |
| 59 | HTTPS CF+ALB certificates | us-east-1 for CF + us-west-1 for ALB |
| 60 | HTTP security headers without code changes | Lambda@Edge + CloudFront |
| 62 | KMS key policy root principal | Enables IAM delegation for all principals in account |
| 64 | Temporary cross-account access | AWS STS |
| 32 | Disable Amazon-provided DNS | enableDnsSupport = false |
| 40 | ACM cross-account subdomain validation | NS delegation in parent zone |
| 49 | Investigate access key 3 months free | CloudTrail console Event History |
| 50 | API keys in CloudFormation encrypted | Secrets Manager + {{resolve:secretsmanager:...}} |

---

## Questions You Got WRONG (27):

| Q# | Topic | Your Error | Correct Answer |
|---|---|---|---|
| 5 | AD trust direction | Wrong trust direction | AWS Managed AD + one-way trust (AWS trusts on-prem) |
| 9 | CloudTrail multi-account S3 | Missed log file validation | New account + bucket policy s3:PutObject + log file validation |
| 10 | GuardDuty master/member | Confused permissions | Members can't archive findings, can't manage IP lists |
| 12 | SQS access troubleshooting | Missed resource policy | IAM role + SQS resource policy doesn't deny |
| 13 | CW Logs agent troubleshooting | Picked wrong option | Log rotation + duplicate [logstream] sections |
| 16 | CloudTrail management events | Picked SNS issue | Management events must be Write-only or All |
| 17 | S3 encryption (company keys) | Missed client-side | SSE-C + client-side with own master key |
| 19 | VPC Flow Logs NACL | Picked SG | NACL blocks outbound (stateless) |
| 22 | GuardDuty Trusted IP list | Picked wrong option | EIPs + Trusted IP list |
| 25 | Credential investigation | Missed CW option | CloudTrail console + CloudWatch Log queries |
| 26 | KMS auto-rotation | Missed one type | Custom key store + Asymmetric + Imported |
| 29 | ENI troubleshooting | Missed ALB target | ENI→SG mapping + instance registered in ALB |
| 30 | IoT Core client ID | Picked wrong combo | ThingName policy + Device Defender |
| 38 | IAM policy interpretation | Missed reading all buckets | s3:Get*/List* on Resource:* = ALL buckets |
| 41 | Real-time logs analytics | Missed combo | Kinesis (real-time) + OpenSearch (analytics) |
| 43 | ACM certs for CF+ALB | Wrong regions | us-east-1 for CF + us-west-1 for ALB |
| 44 | Track all regions | Wrong service | CloudTrail trail applied to all regions |
| 47 | KMS Grants | Picked key policy | Grants = programmatic, per-app, revocable |
| 48 | AD federation | Wrong options | ADFS + IAM roles + AssumeRoleWithSAML |
| 50 | Secrets in CF template | Picked Parameter Store | Secrets Manager + {{resolve:secretsmanager:...}} |
| 52 | CloudTrail multi-account troubleshoot | Missed one | Trail active + bucket + bucket policy with account IDs |
| 55 | Disable instance metadata | Picked SSM Agent | HttpEndpoint: disabled |
| 56 | Remote access employees | Wrong VPN type | SSL VPN (client-to-site) |
| 57 | CW metric filter SG | Missed metric value | AuthorizeSecurityGroupIngress + value=1 |
| 61 | NACL ephemeral ports | Picked SG | NACL outbound 1024-65535 |
| 63 | CW Logs agent log file | Picked setup log | /var/log/awslogs.log (runtime) |
| 65 | S3 + SSE-KMS | Picked wrong encryption | S3 + SSE-KMS (envelope + audit + rotation) |

---

## Key Rules Learned from This Exam

### Operational Troubleshooting
- Inbound ACCEPT + Outbound REJECT in Flow Logs = **NACL problem** (stateless)
- NACL needs outbound ephemeral ports 1024-65535 for return traffic
- `/var/log/awslogs.log` = runtime errors. `/var/log/awslogs-agent-setup.log` = install only.
- Duplicate [logstream] sections = agent stops pushing logs
- Timeout = network. Access Denied = permissions.
- ENI troubleshooting: check SG mapping to correct ENI + ALB target registration

### Directory Service
- Simple AD = Samba, NO trusts
- AD Connector = proxy, no domain in AWS
- Managed AD = full MS AD, supports trusts
- One-way trust: "AWS AD trusts on-prem" = on-prem users can access AWS resources
- Federation: ADFS + IAM ROLES (never groups) + AssumeRoleWithSAML

### S3 Encryption
- "Company manages keys + never in AWS" = client-side encryption with client master key
- "Audit trail + rotation + envelope" = SSE-KMS
- "Company provides key each request" = SSE-C
- "Cheapest, no control needed" = SSE-S3

### CloudTrail
- Management events must be Write-only or All for EventBridge to fire on API calls
- Multi-account bucket policy: s3:PutObject (not UploadPart) + list account IDs
- Requester Pays must be OFF
- Log file validation = detect tampering (SHA-256). Encryption = prevent reading.
- Event History = free, 90 days, immediate

### GuardDuty
- Master: can archive findings, manage IP lists, generate sample findings
- Member: can't archive, can't manage IP lists, CAN generate own samples
- Trusted IP list = PUBLIC IPs only (need EIPs)
- GuardDutyExcluded tag = Malware Protection ONLY

### KMS
- Grants = programmatic, dynamic, per-app, revocable, cross-account
- Key policy = static, 32KB limit
- Root in key policy = enables IAM delegation (not blanket grant)

### Networking
- SSL VPN = client-to-site (home workers)
- IPsec VPN = site-to-site (two fixed networks)
- Direct Connect = physical dedicated link (not Internet)
- WAF attaches to ALB/CloudFront, NEVER to EC2
- CloudFront custom domain cert = ALWAYS us-east-1. ALB cert = ALB's region.

### Other
- IoT Core: ThingName (trusted) vs ClientId (untrusted)
- Kinesis = real-time ingestion. OpenSearch = analytics/search.
- Secrets Manager + {{resolve:secretsmanager:...}} = highest security for CF templates
- CloudWatch metric filter: value = 1 per event. AuthorizeSecurityGroupIngress = inbound SG rule.
