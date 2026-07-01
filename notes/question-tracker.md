# SCS-C03 Question Tracker

> Track every question attempted. Review ❌ and ⚠️ items before the exam.

---

## Quick Stats (Cumulative)

| Metric | Value |
|---|---|
| **Total Questions** | 1606 |
| **✅ Correct** | 1275 (79%) |
| **⚠️ Partial** | 38 (2%) |
| **❌ Wrong** | 290 (18%) |
| **Sessions** | 116 |
| **Re-tests Passed** | 753 of 901 |

## Domain Breakdown

| Domain | Exam Weight | ✅ | ⚠️ | ❌ | Total | Score % | Weak? |
|---|---|---|---|---|---|---|---|
| D1: Detection | 16% | 344 | 12 | 82 | 438 | 79% | 🟡 |
| D2: Incident Response | 14% | 81 | 2 | 20 | 103 | 79% | 🟡 |
| D3: Infrastructure Security | 18% | 261 | 10 | 59 | 330 | 79% | 🟡 |
| D4: Identity & Access Management | 20% | 302 | 11 | 66 | 379 | 80% | 🟢 |
| D5: Data Protection | 18% | 302 | 9 | 68 | 379 | 80% | 🟢 |
| D6: Governance | 14% | 322 | 3 | 82 | 407 | 79% | 🟡 |

Legend: 🔴 < 50% — 🟡 50–79% — 🟢 ≥ 80%

## Weak Areas to Review

| Priority | Topic | Questions | Domain | Count |
|---|---|---|---|---|
| 🔴 1 | Detect vs prevent (GuardDuty vs policy) | Q1578, Q100, Q105, Q153, Q156, Q158, Q546, Q568, Q581 | D1, D3, D5 | 9 |
| 🔴 2 | No-reboot AMI for volatile memory | Q1598, Q810, Q825, Q830, Q933 | D1, D2 | 5 |
| 🔴 3 | EventBridge for API call detection | Q474, Q549, Q570, Q574, Q688 | D1, D6 | 5 |
| 🔴 4 | Cross-account KMS key policy must name external account | Q541, Q669, Q850, Q870, Q974 | D4, D5 | 5 |
| 🔴 5 | State Manager OnBoot + schedule (dual triggers) | Q1403, Q1579, Q1048, Q1071 | D1, D3, D6 | 4 |
| 🔴 6 | cfn-guard bypassable vs Config proactive service-level | Q1387, Q1588, Q1220, Q1271 | D3, D6 | 4 |
| 🔴 7 | S3 server access logging = ACLs | Q1595, Q864, Q868, Q903 | D5, D6 | 4 |
| 🔴 8 | GuardDuty finding types | Q116, Q142, Q154, Q155 | D1 | 4 |
| 🔴 9 | RAM for sharing vs FM for enforcing | Q313, Q441, Q562, Q1329 | D6 | 4 |
| 🔴 10 | StopLogging kills own CW Logs delivery | Q860, Q866, Q1092, Q1256 | D1 | 4 |
| 🔴 11 | RCP scope (your resources only, not outbound) | Q1581, Q683, Q698 | D4, D6 | 3 |
| 🔴 12 | GuardDuty ≠ failed attempts | Q1582, Q534, Q594 | D1, D4, D5, D6 | 3 |
| 🔴 13 | Credential leak IR (Deny-all before investigate) | Q1587, Q862, Q867 | D2, D4 | 3 |
| 🔴 14 | Sign=private, verify=public | Q1596, Q812, Q824 | D4, D5 | 3 |
| 🔴 15 | Network Firewall TLS inspection | Q35, Q87, Q152 | D3 | 3 |
| 🔴 16 | GuardDuty finding types (Impact vs CryptoCurrency) | Q178, Q226, Q489 | D1 | 3 |
| 🔴 17 | KMS key policy root = delegation, not grant | Q264, Q503, Q687 | D4, D5 | 3 |
| 🔴 18 | Default encryption vs bucket policy Deny | Q426, Q626, Q643 | D5 | 3 |
| 🔴 19 | kms:ViaService + SCP | Q488, Q495, Q495 | D4, D5 | 3 |
| 🔴 20 | Detect C2 = GuardDuty (zero code) | Q571, Q584, Q633 | D1 | 3 |
| 🔴 21 | Security services comparison | Q5, Q24 | D1 | 2 |
| 🔴 22 | RAM vs KMS Grants | Q11, Q37 | D4 | 2 |
| 🔴 23 | CloudTrail Lake (data vs mgmt + no backfill) | Q1440, Q951 | D1 | 2 |
| 🔴 24 | Cross-account KMS + SCP evaluation | Q70, Q256 | D4, D5 | 2 |
| 🔴 25 | Session policy bypass by resource-based policy | Q96, Q169 | D4 | 2 |
| 🔴 26 | Detect vs prevent (GuardDuty vs Access Analyzer) | Q187, Q233 | D1 | 2 |
| 🔴 27 | SCP for preventive enforcement | Q261, Q413 | D3, D4 | 2 |
| 🔴 28 | Service Catalog (self-service) | Q274, Q277 | D6 | 2 |
| 🔴 29 | StackSets no auto-remediation | Q283, Q439 | D6 | 2 |
| 🔴 30 | Firewall Manager auto-remediation | Q284, Q435 | D6 | 2 |
| 🔴 31 | Access Analyzer unused + policy generation | Q374, Q1003 | D1, D4 | 2 |
| 🔴 32 | Data perimeter (RCP blocks IN, SCP blocks OUT) | Q398, Q1095 | D4, D6 | 2 |
| 🔴 33 | Native org-wide deployment | Q483, Q492 | D6 | 2 |
| 🔴 34 | Access Analyzer + GuardDuty both fire | Q518, Q652 | D1, D4 | 2 |
| 🔴 35 | Gateway endpoint policy as additional gate | Q535, Q1080 | D3, D4, D5 | 2 |
| 🔴 36 | Session policy + server-side KMS | Q591, Q679 | D4, D5, D6 | 2 |
| 🔴 37 | Access Analyzer static + GuardDuty ≠ failed attempts | Q706, Q1260 | D1, D4 | 2 |
| 🔴 38 | Glacier Vault Lock vs Object Lock | Q800, Q822 | D5 | 2 |
| 🔴 39 | S3 Access Grants prefix overlap | Q819, Q826 | D1, D5 | 2 |
| 🔴 40 | Kinesis consumer = Decrypt + DescribeKey | Q879, Q1100 | D3, D5 | 2 |
| 🔴 41 | Kinesis + KMS VPC endpoints (timeout = network) | Q918, Q950 | D3, D5 | 2 |
| 🔴 42 | API Gateway mTLS = custom domain + S3 truststore | Q967, Q1012 | D3 | 2 |
| 🔴 43 | EMR in-transit = security config + PEM certs | Q1030, Q1073 | D5 | 2 |
| 🔴 44 | IoT revocation = registry. API GW mTLS revocation = CRL in truststore | Q1032, Q1070 | D3, D5 | 2 |
| 🔴 45 | Inspector SBOM = native export + bucket policy | Q1059, Q1119 | D3 | 2 |
| 🔴 46 | Public-facing = 0.0.0.0/0 on 443 | Q1239, Q1250 | D3 | 2 |
| 🔴 47 | Rotation Lambda can't reach DB = SG issue | Q1242, Q1254 | D3, D5 | 2 |
| 🔴 48 | Security Hub setup ordering (E-D-M-A) | Q1244, Q1273 | D6 | 2 |
| 🔴 49 | Detective needs finding. No finding = CW Logs Insights | Q1277, Q1314 | D1 | 2 |
| 🟡 50 | CloudTrail data vs management events | Q1 | D1 | 1 |
| 🟡 51 | Basic vs Advanced event selectors | Q2 | D1 | 1 |
| 🟡 52 | Troubleshooting (Task 1.3) | Q6 | D1 | 1 |
| 🟡 53 | Policy layers reference | Q7 | D4 | 1 |
| 🟡 54 | faq-ram-vs-rcp.md | Q12 | D4 | 1 |
| 🟡 55 | GuardDuty vs CloudTrail | Q13 | D1 | 1 |
| 🟡 56 | DNS Firewall | Q14 | D3 | 1 |
| 🟡 57 | Cross-account patterns | Q15 | D5 | 1 |
| 🟡 58 | CloudTrail Lake vs S3+Athena | Q23 | D1 | 1 |
| 🟡 59 | GuardDuty is regional (console shows current region only) | Q1398 | D1 | 1 |
| 🟡 60 | Config proactive = CF service-level, least code | Q1401 | D6 | 1 |
| 🟡 61 | Config proactive + SCP covers all paths | Q1404 | D6 | 1 |
| 🟡 62 | SCP for IMDSv2 (established exam pattern) | Q1410 | D6 | 1 |
| 🟡 63 | CF Hook = CF service-level (same as Config proactive) | Q1411 | D6 | 1 |
| 🟡 64 | Proactive enforcement = don't downgrade for convenience | Q1424 | D6 | 1 |
| 🟡 65 | Security Hub = dashboard. Config = remediation. | Q1442 | D1 | 1 |
| 🟡 66 | Console direct bypasses Config proactive | Q1389 | D6 | 1 |
| 🟡 67 | Service Catalog = no post-deploy monitoring | Q1464 | D6 | 1 |
| 🟡 68 | Config proactive fires BEFORE SCP in CF deploys | Q1486 | D6 | 1 |
| 🟡 69 | Proactive rejection = CloudTrail failed API | Q1499 | D6 | 1 |
| 🟡 70 | StackSets auto-deploy = new accounts | Q1505 | D6 | 1 |
| 🟡 71 | CT supports custom controls | Q1509 | D6 | 1 |
| 🟡 72 | cfn-guard can't resolve intrinsics | Q1510 | D6 | 1 |
| 🟡 73 | RAM attachment = member-owned | Q1512 | D6 | 1 |
| 🟡 74 | Standards evaluation latency at scale | Q1514 | D6 | 1 |
| 🟡 75 | Config can't detect own death = use SCP | Q1535 | D6 | 1 |
| 🟡 76 | SCP future only + FM auto-remediates existing | Q1540 | D6 | 1 |
| 🟡 77 | Terraform = direct API (not CF) | Q1541 | D6 | 1 |
| 🟡 78 | NACLs stateless | Q34 | D3 | 1 |
| 🟡 79 | RAM vs RCP | Q38 | D4 | 1 |
| 🟡 80 | RCP exemptions (SLR vs service principal) | Q39 | D4 | 1 |
| 🟡 81 | RCP exemptions (PrincipalIsAWSService) | Q42 | D4 | 1 |
| 🟡 82 | Cross-account KMS | Q53 | D4 | 1 |
| 🟡 83 | STS session revocation | Q62 | D4 | 1 |
| 🟡 84 | Session tags + ABAC | Q63 | D4 | 1 |
| 🟡 85 | SCP + RequestTag enforcement | Q68 | D4 | 1 |
| 🟡 86 | Session tags + ABAC (ResourceTag vs RequestTag) | Q72 | D4 | 1 |
| 🟡 87 | Session policy as ceiling | Q78 | D4 | 1 |
| 🟡 88 | SCP cannot be bypassed | Q83 | D4 | 1 |
| 🟡 89 | MRK independent key policies | Q84 | D5 | 1 |
| 🟡 90 | Object Lock Compliance vs Legal Hold | Q85 | D5 | 1 |
| 🟡 91 | Detect C2 = GuardDuty (not DNS Firewall) | Q106 | D1 | 1 |
| 🟡 92 | Imported key rotation procedure | Q114 | D5 | 1 |
| 🟡 93 | SCP for preventive guardrails | Q119 | D6 | 1 |
| 🟡 94 | RAM for resource sharing | Q126 | D6 | 1 |
| 🟡 95 | DNS Firewall rule actions | Q129 | D3 | 1 |
| 🟡 96 | GuardDuty vs Inspector | Q132 | D1 | 1 |
| 🟡 97 | DNS Firewall rule structure | Q134 | D3 | 1 |
| 🟡 98 | Step Functions for IR | Q138 | D2 | 1 |
| 🟡 99 | Access Analyzer modes | Q144 | D1 | 1 |
| 🟡 100 | Validate findings (Task 2.2.3) | Q148 | D2 | 1 |
| 🟡 101 | Data masking (Macie ≠ logs) | Q181 | D5 | 1 |
| 🟡 102 | RCP exemptions (SLR) | Q183 | D4 | 1 |
| 🟡 103 | Access Analyzer policy validation vs Simulator | Q184 | D4 | 1 |
| 🟡 104 | KMS auto-rotation retention | Q192 | D5 | 1 |
| 🟡 105 | KMS key policy delegation + GenerateDataKey | Q206 | D5 | 1 |
| 🟡 106 | Firewall Manager SG audit | Q208 | D3 | 1 |
| 🟡 107 | GuardDuty is regional + agentless | Q232 | D1 | 1 |
| 🟡 108 | CloudWatch Logs Insights vs Detective | Q236 | D1 | 1 |
| 🟡 109 | SCP for preventive guardrails (Control Tower) | Q251 | D6 | 1 |
| 🟡 110 | Secrets Manager cross-region replication | Q258 | D5 | 1 |
| 🟡 111 | SCIM provisioning (Identity Center) | Q263 | D4 | 1 |
| 🟡 112 | Audit Manager vs Artifact | Q271 | D6 | 1 |
| 🟡 113 | StackSets vs Firewall Manager | Q273 | D6 | 1 |
| 🟡 114 | Config conformance packs | Q275 | D6 | 1 |
| 🟡 115 | StackSets vs Conformance Pack | Q276 | D6 | 1 |
| 🟡 116 | DNS Firewall ALERT ≠ finding | Q295 | D1 | 1 |
| 🟡 117 | Security Lake vs CW Logs Insights | Q303 | D1 | 1 |
| 🟡 118 | Verified Access trust providers | Q336 | D3, D4 | 1 |
| 🟡 119 | Signer revocation (job vs profile vs IAM) | Q339 | D4, D6 | 1 |
| 🟡 120 | Cognito Identity Pool + KMS permissions | Q341 | D3, D4 | 1 |
| 🟡 121 | GuardDuty suppression rules | Q372 | D1 | 1 |
| 🟡 122 | Secrets Manager rotation failure | Q376 | D5 | 1 |
| 🟡 123 | Cognito + DynamoDB ABAC (sub vs TenantId) | Q395 | D3, D4 | 1 |
| 🟡 124 | EventBridge for fast detection | Q401 | D1 | 1 |
| 🟡 125 | Timeout vs Access Denied (SG troubleshooting) | Q418 | D3 | 1 |
| 🟡 126 | KMS is regional | Q423 | D4, D5 | 1 |
| 🟡 127 | RCP same-org evaluation | Q427 | D4 | 1 |
| 🟡 128 | Secrets Manager replication ≠ MRK | Q428 | D5 | 1 |
| 🟡 129 | SCP prevents disabling services | Q440 | D6 | 1 |
| 🟡 130 | RAM + FM complementary | Q442 | D6 | 1 |
| 🟡 131 | Full governance stack | Q445 | D6 | 1 |
| 🟡 132 | StackSets limitations | Q450 | D6 | 1 |
| 🟡 133 | FM SG common policy | Q454 | D6 | 1 |
| 🟡 134 | Delegated admin (all services) | Q462 | D6 | 1 |
| 🟡 135 | Proactive guardrail (CF Hook) | Q464 | D6 | 1 |
| 🟡 136 | No single governance service | Q486 | D6 | 1 |
| 🟡 137 | SCP can't inspect payload + RCP prevents consequence | Q515 | D1, D6 | 1 |
| 🟡 138 | EventBridge for fast detection + auto-revert | Q523 | D1, D6 | 1 |
| 🟡 139 | Network FW for IP-level C2 block | Q526 | D1, D3 | 1 |
| 🟡 140 | Detection + response architecture | Q532 | D1, D3, D6 | 1 |
| 🟡 141 | GuardDuty ≠ failed attempts + Access Analyzer static analysis | Q545 | D1, D4, D5 | 1 |
| 🟡 142 | Detect vs prevent (GuardDuty vs EventBridge for behavioral) | Q640 | D1 | 1 |
| 🟡 143 | GuardDuty finding types (C2 = Trojan, not CryptoCurrency) | Q655 | D1 | 1 |
| 🟡 144 | VPC endpoints (direct KMS + DynamoDB) | Q685 | D3, D5 | 1 |
| 🟡 145 | DGA = allow-list DNS Firewall | Q690 | D1, D3 | 1 |
| 🟡 146 | NACLs stateless (Dojo Q19, Q61) | Q707 | D3 | 1 |
| 🟡 147 | Directory Service + trust direction (Dojo Q5) | Q709 | D4 | 1 |
| 🟡 148 | CloudTrail management events Read/Write (Dojo Q16) | Q710 | D1 | 1 |
| 🟡 149 | GuardDuty Trusted IP list (Dojo Q22) | Q711 | D1 | 1 |
| 🟡 150 | VPN types (Dojo Q56) | Q719 | D3 | 1 |
| 🟡 151 | CW metric filter value (Dojo Q57) | Q724 | D1 | 1 |
| 🟡 152 | ADFS vs AD Connector (Dojo Q48) | Q731 | D4 | 1 |
| 🟡 153 | AD Connector vs Simple AD | Q739 | D4 | 1 |
| 🟡 154 | EC2 EBS + kms:CreateGrant (Dojo T2 Q47) | Q745 | D5 | 1 |
| 🟡 155 | SCP ceiling implicit deny (Dojo T2 Q65) | Q747 | D4 | 1 |
| 🟡 156 | InsideAWS = SG isolation | Q761 | D2, D4 | 1 |
| 🟡 157 | S3 envelope encryption never uses kms:Encrypt | Q765 | D5 | 1 |
| 🟡 158 | Cognito Identity Pool + role (not direct STS) | Q778 | D4 | 1 |
| 🟡 159 | NACLs stateless (inbound ACCEPT + outbound REJECT) | Q781 | D3 | 1 |
| 🟡 160 | EKS Runtime Monitoring (agent required) | Q797 | D1, D3 | 1 |
| 🟡 161 | CloudFront response headers policy | Q801 | D3 | 1 |
| 🟡 162 | GuardDuty Extended Threat Detection (too new) | Q806 | D1 | 1 |
| 🟡 163 | OutsideAWS IR + IMDSv2 hardening | Q820 | D1, D2, D4 | 1 |
| 🟡 164 | GuardDuty ≠ failed attempts + AA static | Q839 | D1 | 1 |
| 🟡 165 | S3 Batch Operations cross-account + manifest region | Q855 | D4, D5 | 1 |
| 🟡 166 | S3 Batch cross-account needs bucket policy | Q857 | D4, D6 | 1 |
| 🟡 167 | SCP prevention > detect+remediate | Q858 | D4, D6 | 1 |
| 🟡 168 | S3 Batch Operations regional | Q872 | D5 | 1 |
| 🟡 169 | IoT ThingName = cert-bound, not hardware | Q880 | D3 | 1 |
| 🟡 170 | Config custom rule = Lambda (max 15min timeout) | Q881 | D1, D6 | 1 |
| 🟡 171 | CRR dest = kms:GenerateDataKey (not Encrypt) | Q883 | D5 | 1 |
| 🟡 172 | CRR rewrites encryption context to dest | Q888 | D5 | 1 |
| 🟡 173 | IoT cert revocation = instant (no CRL delay) | Q892 | D3 | 1 |
| 🟡 174 | DynamoDB + CMK = CreateGrant + DescribeKey | Q899 | D4, D5 | 1 |
| 🟡 175 | Reading comprehension (perms already present) | Q901 | D5 | 1 |
| 🟡 176 | EBS encryption by default + SCP = full prevention | Q902 | D5, D6 | 1 |
| 🟡 177 | GWLB GENEVE decapsulation | Q905 | D3 | 1 |
| 🟡 178 | Config org custom rule cross-account invoke | Q908 | D1, D6 | 1 |
| 🟡 179 | Reading comprehension (multiple missing perms) | Q911 | D3, D5 | 1 |
| 🟡 180 | CRR custom encryption context preserved | Q923 | D5 | 1 |
| 🟡 181 | CreateSampleFindings vs FIS | Q934 | D2 | 1 |
| 🟡 182 | Resilience Hub = assess, FIS = test, ARC = recover | Q935 | D2 | 1 |
| 🟡 183 | ARC zonal shift | Q936 | D2 | 1 |
| 🟡 184 | Deny * on user vs TokenIssueTime (user vs role) | Q942 | D2 | 1 |
| 🟡 185 | KMS endpoint + SG (direct calls only) | Q965 | D3, D5 | 1 |
| 🟡 186 | API Gateway TOKEN vs REQUEST authorizer | Q988 | D3 | 1 |
| 🟡 187 | S3 wraps KMS errors (error surface vs root cause) | Q989 | D4, D5 | 1 |
| 🟡 188 | SageMaker notebooks vs Detective (custom vs built-in) | Q996 | D2 | 1 |
| 🟡 189 | CloudTrail Insights vs GuardDuty (complementary) | Q1004 | D1 | 1 |
| 🟡 190 | Bedrock IAM guardrail enforcement (condition key) | Q1007 | D3 | 1 |
| 🟡 191 | Q Business ACL identity mapping failure | Q1010 | D3 | 1 |
| 🟡 192 | Resource Policy = boundary rejection (before authorizer) | Q1013 | D3 | 1 |
| 🟡 193 | Private API timeout = Resource Policy rejection (not always network) | Q1025 | D3, D5 | 1 |
| 🟡 194 | Access Grants + SSE-KMS needs explicit kms:Decrypt on role | Q1026 | D4, D5 | 1 |
| 🟡 195 | Well-Architected Tool = architecture review + improvement plan | Q1031 | D6 | 1 |
| 🟡 196 | IoT Core = registry-based revocation (instant) | Q1035 | D3 | 1 |
| 🟡 197 | Key policy conditions enforced regardless of caller's identity policy | Q1040 | D4, D5 | 1 |
| 🟡 198 | Inspector SBOM = on-demand API (EventBridge + Lambda to schedule) | Q1051 | D3 | 1 |
| 🟡 199 | Hardcoded credential → always Secrets Manager | Q1054 | D3 | 1 |
| 🟡 200 | mTLS 403 = cert expired (if same CA works for others) | Q1055 | D3 | 1 |
| 🟡 201 | RCP evaluates S3 CALLER (Lambda), not original HTTP client | Q1074 | D4, D6 | 1 |
| 🟡 202 | CRR preserves source custom encryption context | Q1075 | D5 | 1 |
| 🟡 203 | Lambda = no EBS/AMI forensics (ephemeral) | Q1079 | D2, D3 | 1 |
| 🟡 204 | OutsideAWS + can't disrupt = TokenIssueTime + snapshot | Q1108 | D2 | 1 |
| 🟡 205 | Cron vs Rate vs PITR | Q1124 | D5 | 1 |
| 🟡 206 | Traffic Mirroring = passive. GWLB = inline. 3x failed. | Q1126 | D3 | 1 |
| 🟡 207 | State Manager = schedule enforcement (proactive) | Q1127 | D1, D3 | 1 |
| 🟡 208 | Session Manager logging = session activity (not CW Agent) | Q1132 | D2 | 1 |
| 🟡 209 | DNSSEC broken chain = DS in parent | Q1135 | D3 | 1 |
| 🟡 210 | Stack Policy = protect resources inside stack | Q1138 | D6 | 1 |
| 🟡 211 | Federated user ARN = sts:: not iam:: | Q1139 | D4 | 1 |
| 🟡 212 | SCP = what key, Key policy = who uses it | Q1140 | D4, D5 | 1 |
| 🟡 213 | mTLS = custom domain + S3 | Q1172 | D3 | 1 |
| 🟡 214 | Bedrock guardrail condition key | Q1187 | D3 | 1 |
| 🟡 215 | Config also detects StopLogging | Q1201 | D1 | 1 |
| 🟡 216 | mTLS S3 versioning required | Q1207 | D3 | 1 |
| 🟡 217 | Well-Architected Tool milestones | Q1211 | D6 | 1 |
| 🟡 218 | cfn-guard vs Config proactive (template validation) | Q1213 | D6 | 1 |
| 🟡 219 | WAT milestones = no automation | Q1221 | D6 | 1 |
| 🟡 220 | Stack Policy default deny + selective Deny | Q1225 | D6 | 1 |
| 🟡 221 | WAT milestones = no automated evidence | Q1226 | D6 | 1 |
| 🟡 222 | User = Deny *. Role = TokenIssueTime. | Q1231 | D2 | 1 |
| 🟡 223 | WAT = self-reported, no automation | Q1233 | D6 | 1 |
| 🟡 224 | IAM Credential Report 4-hour cache | Q1234 | D1 | 1 |
| 🟡 225 | Permission boundary delegation vs Service Catalog | Q1235 | D4 | 1 |
| 🟡 226 | SCP attachment OU vs accounts | Q1236 | D4, D6 | 1 |
| 🟡 227 | EBS snapshot sharing (copy with CMK, no volume needed) | Q1237 | D5 | 1 |
| 🟡 228 | SCP block root (containment vs hygiene) | Q1238 | D4, D6 | 1 |
| 🟡 229 | CW agent ships logs (not SSM agent) | Q1240 | D1 | 1 |
| 🟡 230 | Boot-time retrieval vs deploy-time injection | Q1241 | D5 | 1 |
| 🟡 231 | VPC Flow vs TGW Flow Logs scope | Q1243 | D1, D3 | 1 |
| 🟡 232 | Resolver vs DNS query logging direction | Q1276 | D1 | 1 |
| 🟡 233 | Remediation succeeds but returns = re-creation | Q1287 | D1 | 1 |
| 🟡 234 | Macie enabled ≠ Macie scanning | Q1293 | D1 | 1 |
| 🟡 235 | Preserve evidence = EBS snapshot | Q1295 | D2, D3 | 1 |
| 🟡 236 | NAA finds, RA explains | Q1296 | D3 | 1 |
| 🟡 237 | Trojan = outbound. Recon = inbound. | Q1302 | D1 | 1 |
| 🟡 238 | EventBridge=seconds, Config=minutes | Q1309 | D1 | 1 |
| 🟡 239 | SCP + conformance pack = OU-level auto-apply | Q1313 | D6 | 1 |
| 🟡 240 | cfn-guard bypassable vs Config proactive | Q1354 | D6 | 1 |
| 🟡 241 | EBS encryption by default + SCP | Q1371 | D5 | 1 |

---

## Session Index

| # | Date | Questions | ✅ | ⚠️ | ❌ | Domains Covered | Link |
|---|---|---|---|---|---|---|---|
| 1 | 2025-05-01 | Q1–Q20 | 10 | 6 | 4 | D1 Detection · D3 Infrastructure · D4 IAM · D5 Data Protection | [Jump](#session-1--2025-05-01) |
| 2 | 2025-05-02 | Q21–Q23 | 2 | 0 | 1 | D1 Detection (re-test) | [Jump](#session-2--2025-05-02) |
| 3 | 2025-05-03 | Q24–Q25 | 1 | 1 | 0 | D1 Detection (re-test) | [Jump](#session-3--2025-05-03) |
| 110 | 2026-06-24 | Q1390–Q1394 | 5 | 0 | 0 | D2 Incident Response (D2 uplift drill — novel operational patterns) | [Jump](#session-110--2026-06-24) |
| 111 | 2026-06-25 | Q1395–Q1419 | 19 | 1 | 5 | D1 Detection · D6 Governance · D3 Infrastructure (Week 3 drill — StopLogging, cfn-guard vs Config proactive vs CF Hook, State Manager dual triggers, GuardDuty regional) | [Jump](#session-111--2026-06-25) |
| 112 | 2026-06-27 | Q1420–Q1429 | 9 | 0 | 1 | D6 Governance (hyperfocus uplift — cfn-guard vs Config proactive, WAT milestones, Stack Policy, SCP all-paths, auto-apply on OU join) | [Jump](#session-112--2026-06-27) |
| 113 | 2026-06-27 | Q1430–Q1454 | 23 | 0 | 2 | D1 Detection (hyperfocus uplift — remediation loops, Detective vs CW Insights, StopLogging detection, Macie sampling, log source direction) | [Jump](#session-113--2026-06-27) |
| 109 | 2026-06-24 | Q1380–Q1389 | 8 | 0 | 2 | D1 Detection · D3 Infrastructure · D6 Governance (Week 2 never-seen drill — Bedrock, NACLs, StopLogging, cfn-guard vs Config proactive) | [Jump](#session-109--2026-06-24) |
| 114 | 2026-06-27 | Q1455–Q1514 | 52 | 0 | 8 | D6 Governance (hyperfocus uplift — Config proactive scope, Security Hub setup, WAT vs Audit Manager, Stack Policy, Service Catalog) | [Jump](#session-114--2026-06-27) |
| 115 | 2026-06-28 | Q1515–Q1577 | 60 | 0 | 3 | D6 Governance (re-test — Session 114 errors) | [Jump](#session-115--2026-06-28) |
| 116 | 2026-06-30 | Q1578–Q1606 | 20 | 2 | 7 | Cross-domain (Red-priority kill drill — novel angles, killer difficulty) | [Jump](#session-116--2026-06-30) |
| 4 | 2025-05-04 | Q26–Q35 | 8 | 1 | 1 | D3 Infrastructure Security (firewalls comparison) | [Jump](#session-4--2025-05-04) |
| 5 | 2025-05-05 | Q36–Q38 | 1 | 2 | 0 | D4 Identity & Access Management (re-test) | [Jump](#session-5--2025-05-05) |
| 6 | 2025-05-05 | Q39–Q43 | 3 | 0 | 2 | D4 Identity & Access Management (policy layers quiz) | [Jump](#session-6--2025-05-05) |
| 7 | 2025-05-05 | Q44–Q48 | 5 | 0 | 0 | D4 Identity & Access Management (rapid fire — post hyperfocus) | [Jump](#session-7--2025-05-05) |
| 8 | 2025-05-05 | Q49–Q58 | 9 | 1 | 0 | D4 Identity & Access Management (Week 1 final quiz — mixed Task 4.1 + 4.2) | [Jump](#session-8--2025-05-05) |
| 9 | 2025-05-08 | Q59–Q63 | 3 | 0 | 2 | D4 Identity & Access Management (Week 2 — cross-account, VP, STS) | [Jump](#session-9--2025-05-08) |
| 10 | 2025-05-08 | Q64–Q68 | 4 | 1 | 0 | D4 Identity & Access Management (Week 2 — Identity Center, session policies, VP, ABAC) | [Jump](#session-10--2025-05-08) |
| 11 | 2025-05-09 | Q69–Q73 | 3 | 0 | 2 | D4 Identity & Access Management (re-test — cross-account KMS, STS revocation, ABAC, RAM) | [Jump](#session-11--2025-05-09) |
| 12 | 2025-05-09 | Q74–Q78 | 4 | 0 | 1 | D4 Identity & Access Management (Week 2 quiz — data perimeter, VP, boundaries, session policies) | [Jump](#session-12--2025-05-09) |
| 13 | 2025-05-09 | Q79–Q83 | 4 | 0 | 1 | D4 Identity & Access Management (Week 2 final quiz — ABAC, boundaries, cross-account KMS, RCP, SCP bypass) | [Jump](#session-13--2025-05-09) |
| 14 | 2025-05-09 | Q84–Q88 | 2 | 0 | 3 | D5 Data Protection · D3 Infrastructure Security (combined mini-exam) | [Jump](#session-14--2025-05-09) |
| 15 | 2025-05-13 | Q89–Q91 | 3 | 0 | 0 | D5 Data Protection · D3 Infrastructure Security (re-test) | [Jump](#session-15--2025-05-13) |
| 16 | 2025-05-13 | Q92–Q96 | 4 | 0 | 1 | D4 Identity & Access Management (Week 2 final quiz — SCP bypass, session policies, ABAC, cross-account KMS) | [Jump](#session-16--2025-05-13) |
| 17 | 2025-05-13 | Q97–Q99 | 3 | 0 | 0 | D4 Identity & Access Management · D1 Detection (re-test — SLR exemptions, session policy bypass, Security Hub) | [Jump](#session-17--2025-05-13) |
| 18 | 2025-05-13 | Q100–Q104 | 4 | 1 | 0 | D5 Data Protection (Week 3 mini-exam — KMS, S3 encryption, Secrets Manager, Object Lock) | [Jump](#session-18--2025-05-13) |
| 19 | 2025-05-14 | Q105–Q109 | 3 | 0 | 2 | D1 Detection (re-test — detect vs prevent, security services comparison) | [Jump](#session-19--2025-05-14) |
| 20 | 2025-05-15 | Q110–Q119 | 7 | 2 | 1 | Cross-domain practice exam (Week 11 — all domains) | [Jump](#session-20--2025-05-15) |
| 21 | 2025-05-15 | Q120–Q129 | 8 | 1 | 1 | Cross-domain timed practice exam (Week 11 — all domains) | [Jump](#session-21--2025-05-15) |
| 22 | 2025-05-15 | Q130–Q139 | 7 | 1 | 2 | Cross-domain timed practice exam (Week 11 — all domains, RAM/FM focus) | [Jump](#session-22--2025-05-15) |
| 23 | 2025-05-15 | Q140–Q149 | 7 | 2 | 1 | D1 Detection · D2 Incident Response (re-test — post-video drill) | [Jump](#session-23--2025-05-15) |
| 24 | 2025-05-16 | Q150–Q154 | 2 | 1 | 2 | Cross-domain (re-test — red-priority weak areas drill) | [Jump](#session-24--2025-05-16) |
| 25 | 2025-05-16 | Q155–Q159 | 2 | 0 | 3 | D1 Detection (re-test — GuardDuty finding types + detect vs prevent drill) | [Jump](#session-25--2025-05-16) |
| 26 | 2025-05-16 | Q160–Q182 | 20 | 0 | 3 | Cross-domain exam-format practice (Week 11 — all domains) | [Jump](#session-26--2025-05-16) |
| 27 | 2025-05-16 | Q183–Q206 | 19 | 0 | 5 | Cross-domain exam-format practice (Week 11 — hardest topics) | [Jump](#session-27--2025-05-16) |
| 28 | 2025-05-16 | Q207–Q216 | 9 | 0 | 1 | Cross-domain exam-format practice (Week 11 — mixed, targeting remaining gaps) | [Jump](#session-28--2025-05-16) |
| 29 | 2025-05-16 | Q217–Q226 | 9 | 0 | 1 | Cross-domain exam-format practice (Week 11 — final killer set, all weak spots) | [Jump](#session-29--2025-05-16) |
| 30 | 2025-05-17 | Q227–Q231 | 5 | 0 | 0 | Cross-domain (re-test — red-priority gaps: Impact vs CryptoCurrency, session policy bypass) | [Jump](#session-30--2025-05-17) |
| 31 | 2025-05-17 | Q232–Q241 | 7 | 0 | 3 | D1 Detection + Cross-domain (Week 11 — D1 focus, targeting 62% domain) | [Jump](#session-31--2025-05-17) |
| 32 | 2025-05-17 | Q246–Q255 | 9 | 0 | 1 | Cross-domain exam-format practice (Week 11 — mixed, all domains) | [Jump](#session-32--2025-05-17) |
| 33 | 2025-05-17 | Q256–Q265 | 5 | 0 | 5 | Cross-domain exam-format practice (Week 11 — harder scenarios, multi-concept) | [Jump](#session-33--2025-05-17) |
| 34 | 2025-05-18 | Q266–Q270 | 5 | 0 | 0 | Cross-domain (re-test — Session 33 errors) | [Jump](#session-34--2025-05-18) |
| 35 | 2025-05-18 | Q271–Q275 | 1 | 0 | 4 | D6 Governance (untested gaps — StackSets, Audit Manager, Artifact, Service Catalog, Conformance Packs) | [Jump](#session-35--2025-05-18) |
| 36 | 2025-05-18 | Q276–Q280 | 3 | 0 | 2 | D6 Governance (re-test — StackSets, Service Catalog, Audit Manager, Artifact, Conformance Packs) | [Jump](#session-36--2025-05-18) |
| 37 | 2025-05-18 | Q281–Q295 | 12 | 0 | 3 | D6 Governance + D3/D4 (untested topics) + D1 Detection (retention check) | [Jump](#session-37--2025-05-18) |
| 38 | 2025-05-18 | Q296–Q305 | 9 | 0 | 1 | Cross-domain exam simulation (all domains) | [Jump](#session-38--2025-05-18) |
| 39 | 2025-05-18 | Q306–Q325 | 19 | 0 | 1 | Cross-domain exam simulation (all domains, hardest scenarios) | [Jump](#session-39--2025-05-18) |
| 40 | 2025-05-18 | Q326–Q330 | 5 | 0 | 0 | Cross-domain exam simulation (all domains, final validation) | [Jump](#session-40--2025-05-18) |
| 41 | 2025-05-19 | Q331–Q335 | 5 | 0 | 0 | Cross-domain (untested gaps — Bedrock, Cognito, OAC+KMS, Security Lake, VPC endpoints) | [Jump](#session-41--2025-05-19) |
| 43 | 2025-05-20 | Q360–Q369 | 10 | 0 | 0 | Cross-domain (killer set — remaining 🟡 weak areas) | [Jump](#session-43--2025-05-20) |
| 42 | 2025-05-19 | Q336–Q359 | 21 | 0 | 3 | Cross-domain (Signer, Verified Access, Cognito, hybrid, detection gaps) | [Jump](#session-42--2025-05-19) |
| 44 | 2025-05-20 | Q370–Q379 | 7 | 0 | 3 | Cross-domain killer exam simulation (all domains, novel scenarios) | [Jump](#session-44--2025-05-20) |
| 45 | 2025-05-22 | Q380–Q384 | 5 | 0 | 0 | Cross-domain (re-test — Session 44 errors + validation) | [Jump](#session-45--2025-05-22) |
| 46 | 2026-05-24 | Q385–Q394 | 10 | 0 | 0 | Cross-domain exam simulation (all domains, certification-level) | [Jump](#session-46--2026-05-24) |
| 47 | 2026-05-24 | Q395–Q404 | 7 | 1 | 2 | Cross-domain killer exam simulation (all domains, novel scenarios) | [Jump](#session-47--2026-05-24) |
| 48 | 2026-05-24 | Q405–Q414 | 9 | 0 | 1 | Cross-domain killer exam simulation (all domains, novel scenarios) | [Jump](#session-48--2026-05-24) |
| 49 | 2026-05-24 | Q415–Q429 | 10 | 0 | 5 | Cross-domain lightning rounds (all domains, novel scenarios) | [Jump](#session-49--2026-05-24) |
| 50 | 2026-05-25 | Q430–Q434 | 5 | 0 | 0 | Cross-domain (re-test — Session 49 errors + new killer) | [Jump](#session-50--2026-05-25) |
| 51 | 2026-05-25 | Q435–Q486 | 39 | 1 | 12 | D6 Governance (targeted drill — RAM vs FM, StackSets, Service Catalog, Audit Manager) | [Jump](#session-51--2026-05-25) |
| 52 | 2026-05-26 | Q487–Q505 | 19 | 0 | 6 | Cross-domain (hard drill — D1/D4/D5/D6 weak spots) | [Jump](#session-52--2026-05-26) |
| 53 | 2026-05-26 | Q506–Q515 | 9 | 0 | 1 | Cross-domain (re-test + killer uplift — all domains) | [Jump](#session-53--2026-05-26) |
| 54 | 2026-05-26 | Q516–Q530 | 12 | 0 | 3 | Cross-domain (killer uplift — hard novel scenarios) | [Jump](#session-54--2026-05-26) |
| 55 | 2026-05-26 | Q531–Q540 | 7 | 0 | 3 | Cross-domain (killer difficulty — multi-concept combos) | [Jump](#session-55--2026-05-26) |
| 56 | 2026-05-28 | Q541–Q555 | 11 | 1 | 3 |  | [Jump](#session-56--2026-05-28) |
| 57 | 2026-05-28 | Q556–Q565 | 9 | 0 | 1 | Cross-domain (killer exam set — all red-priority weak areas) | [Jump](#session-57--2026-05-28) |
| 58 | 2026-05-28 | Q566–Q575 | 6 | 0 | 4 | D1 Detection + D6 Governance (targeted drill — detect vs prevent + RAM/FM) | [Jump](#session-58--2026-05-28) |
| 59 | 2026-05-28 | Q576–Q580 | 5 | 0 | 0 | D1 Detection (targeted drill — GuardDuty S3 Protection vs EventBridge vs Access Analyzer) | [Jump](#session-59--2026-05-28) |
| 60 | 2026-05-30 | Q581–Q590 | 8 | 0 | 2 | D1 Detection + D6 Governance (re-test blitz — top 3 red-priority gaps) | [Jump](#session-60--2026-05-30) |
| 61 | 2026-05-30 | Q591–Q600 | 8 | 0 | 2 | Cross-domain killer exam simulation (all domains, hardest scenarios) | [Jump](#session-61--2026-05-30) |
| 62 | 2026-05-30 | Q601–Q610 | 10 | 0 | 0 | D1 Detection + D6 Governance (killer targeted drill — all red-priority gaps) | [Jump](#session-62--2026-05-30) |
| 63 | 2026-05-30 | Q611–Q620 | 10 | 0 | 0 | Cross-domain killer (session policy + server-side KMS + cross-account + RCP + ViaService) | [Jump](#session-63--2026-05-30) |
| 64 | 2026-05-30 | Q621–Q630 | 9 | 0 | 1 | Cross-domain (AWS-style wording traps — all domains, novel phrasing) | [Jump](#session-64--2026-05-30) |
| 65 | 2026-05-31 | Q631–Q648 | 15 | 0 | 3 | Cross-domain domination drill (D1 Detection + D5 Data Protection + D6 Governance) | [Jump](#session-65--2026-05-31) |
| 66 | 2026-06-01 | Q649–Q670 | 11 | 1 | 2 | Cross-domain domination drill (D1 Detection + D5 Data Protection + D6 Governance + D4 IAM) | [Jump](#session-66--2026-06-01) |
| 67 | 2026-06-01 | Q671–Q676 | 6 | 0 | 0 | D1 Detection + D4/D5 IAM/Data Protection (final leaks drill — C2=Trojan + cross-account KMS key policy) | [Jump](#session-67--2026-06-01) |
| 68 | 2026-06-02 | Q677–Q686 | 7 | 0 | 3 | Cross-domain final validation killer set (all domains, maximum difficulty) | [Jump](#session-68--2026-06-02) |
| 69 | 2026-06-02 | Q687–Q696 | 7 | 0 | 3 | Cross-domain killer exam simulation (all domains, maximum difficulty + novel patterns) | [Jump](#session-69--2026-06-02) |
| 70 | 2026-06-05 | Q697–Q701 | 4 | 0 | 1 | Cross-domain (pre-Dojo killer drill — session policy + RCP scope + VPC endpoints + ViaService) | [Jump](#session-70--2026-06-05) |
| 71 | 2026-06-05 | Q702–Q706 | 4 | 0 | 1 | Cross-domain (pre-Dojo RCP scope drill + AA vs GD static/dynamic) | [Jump](#session-71--2026-06-05) |
| 72 | 2026-06-09 | Q707–Q712 | 2 | 1 | 3 | Cross-domain (Dojo Test 1 gap drill — operational troubleshooting, Directory Service, GuardDuty, CloudTrail, S3 encryption) | [Jump](#session-72--2026-06-09) |
| 73 | 2026-06-09 | Q713–Q722 | 9 | 0 | 1 | Cross-domain (Dojo Test 1 gap drill #2 — CloudTrail, IoT, ENI, SQS, VPN, GuardDuty, IAM, S3 encryption) | [Jump](#session-73--2026-06-09) |
| 74 | 2026-06-10 | Q723–Q732 | 8 | 0 | 2 | Cross-domain (Dojo Test 1 gap drill #3 — GuardDuty admin, CW metric filters, IAM boundaries, KMS Grants, OpenSearch, ACM, CloudTrail Read/Write, metadata, AD/ADFS, S3 encryption) | [Jump](#session-74--2026-06-10) |
| 75 | 2026-06-10 | Q733–Q742 | 9 | 0 | 1 | Cross-domain (Dojo Test 1 gap drill #4 — AD/Directory Service focus + operational troubleshooting) | [Jump](#session-75--2026-06-10) |
| 76 | 2026-06-10 | Q743–Q752 | 8 | 0 | 2 | Cross-domain (Dojo Test 2 gap drill — KMS operational, IAM/SCP, STS variants, SSM remediation, load balancers) | [Jump](#session-76--2026-06-10) |
| 77 | 2026-06-10 | Q753–Q762 | 9 | 0 | 1 | Cross-domain killer exam simulation (all domains, maximum difficulty) | [Jump](#session-77--2026-06-10) |
| 78 | 2026-06-10 | Q763–Q772 | 9 | 0 | 1 | Cross-domain (Dojo Test 2 gap drill #2 — KMS operational, SCP, permission boundaries, SSE-C, Secrets Manager, CloudTrail Insights) | [Jump](#session-78--2026-06-10) |
| 79 | 2026-06-11 | Q773–Q782 | 8 | 0 | 2 | Cross-domain (Dojo combined gap reinforcement drill — KMS operational, IAM wording traps, service selection, troubleshooting) | [Jump](#session-79--2026-06-11) |
| 80 | 2026-06-11 | Q783–Q795 | 13 | 0 | 0 | Cross-domain (Dojo combined gap drill — KMS operational, IAM wording traps, service selection, troubleshooting) | [Jump](#session-80--2026-06-11) |
| 81 | 2026-06-11 | Q796–Q813 | 12 | 2 | 4 | Cross-domain (novel topics drill — encryption context, EKS runtime, presigned URLs, Glacier Vault Lock, CloudFront headers, IAM Roles Anywhere, S3 Object Lambda, declarative policies) | [Jump](#session-81--2026-06-11) |
| 82 | 2026-06-11 | Q814–Q820 | 5 | 0 | 2 | Cross-domain (novel topics killer drill — ACM regions, Config remediation, encryption context ABAC, GWLB, declarative policies, S3 Access Grants, IR forensics) | [Jump](#session-82--2026-06-11) |
| 83 | 2026-06-12 | Q821–Q827 | 3 | 0 | 4 | Cross-domain (priority re-test — Sessions 81-82 errors) | [Jump](#session-83--2026-06-12) |
| 84 | 2026-06-12 | Q828–Q834 | 6 | 0 | 1 | Cross-domain (priority re-test #2 — Sessions 81-83 errors, reinforcement) | [Jump](#session-84--2026-06-12) |
| 85 | 2026-06-12 | Q835–Q848 | 13 | 0 | 1 | D1 Detection + D2 Incident Response (killer targeted drill — weakest domains) | [Jump](#session-85--2026-06-12) |
| 86 | 2026-06-12 | Q849–Q865 | 10 | 0 | 7 | Cross-domain (killer difficulty — novel operational scenarios, cross-account patterns, ACM, Config, Kinesis) | [Jump](#session-86--2026-06-12) |
| 87 | 2026-06-15 | Q866–Q882 | 9 | 0 | 8 | Cross-domain (Session 86 re-test + Week 1 novel topics — ACM, IoT, Kinesis, Config custom rules, CloudTrail Lake, S3 Batch) | [Jump](#session-87--2026-06-15) |
| 88 | 2026-06-15 | Q883–Q892 | 7 | 0 | 3 | Cross-domain (score uplift drill — CRR+KMS, StopLogging, IR containment, multipart, EBS, IoT, Config custom rules) | [Jump](#session-88--2026-06-15) |
| 89 | 2026-06-15 | Q893–Q902 | 7 | 0 | 3 | Cross-domain (score uplift drill #2 — CRR, IoT, S3 Batch, DynamoDB KMS, ViaService, EBS encryption) | [Jump](#session-89--2026-06-15) |
| 90 | 2026-06-15 | Q903–Q912 | 6 | 0 | 4 | Cross-domain (surprise drill — S3 ACLs, GWLB, Roles Anywhere, Private CA, declarative policies, Kinesis, VPC endpoints) | [Jump](#session-90--2026-06-15) |
| 91 | 2026-06-15 | Q913–Q922 | 9 | 0 | 1 | Cross-domain (Week 1 killer drill — CRR encryption context, StopLogging, credential leak IR, S3 logging, IoT revocation, Kinesis endpoints, S3 Batch, GWLB, Config custom rules, DynamoDB KMS) | [Jump](#session-91--2026-06-15) |
| 92 | 2026-06-15 | Q923–Q932 | 9 | 0 | 1 | Cross-domain (Week 1 weekly drill — CRR custom context, IoT ThingName, Kinesis SGs, Config Lambda timeout, CloudTrail Lake, S3 Batch regional, GWLB GENEVE, DynamoDB CreateGrant, ACM regional, Config org rule) | [Jump](#session-92--2026-06-15) |
| 93 | 2026-06-16 | Q933–Q942 | 5 | 1 | 4 | D2 Incident Response + D1 Detection (D2 never-seen services blitz + D1 decision validation) | [Jump](#session-93--2026-06-16) |
| 94 | 2026-06-16 | Q943–Q956 | 12 | 2 | 0 | D2 Incident Response + D1 Detection + D5 Data Protection + D3 Infrastructure + D6 Governance (Week 1 weekly drill + Session 93 re-test) | [Jump](#session-94--2026-06-16) |
| 95 | 2026-06-16 | Q957–Q961 | 5 | 0 | 0 | D2 Incident Response (D2 novel patterns blitz — automated forensics, chain of custody, Step Functions orchestration) | [Jump](#session-95--2026-06-16) |
| 96 | 2026-06-16 | Q962–Q1010 | 39 | 3 | 7 | D1 Detection + D5 Data Protection + D3 Infrastructure + D2 Incident Response (cross-domain uplift — never-seen topics + verb traps) | [Jump](#session-96--2026-06-16) |
| 97 | 2026-06-17 | Q1012–Q1011 | 35 | 0 | 13 | D3 Infrastructure + D5 Data Protection + D1 Detection + D6 Governance (Week 2-5 never-seen blitz — API GW mTLS, authorizers, FLE, Inspector SBOM, Macie, S3 Access Grants, VPC Lattice, State Manager, cfn-guard, DLM, DataSync, EMR, WAF Bot Control, CodeGuru) | [Jump](#session-97--2026-06-17) |
| 98 | 2026-06-18 | Q1056–Q1115 | 48 | 0 | 12 | D3 Infrastructure + D5 Data Protection + D1 Detection + D4 IAM + D6 Governance (Week 2 NEVER-SEEN validation — mTLS, FLE, SBOM, Macie, Access Grants, Session 97 re-tests, cross-domain killers) | [Jump](#session-98--2026-06-18) |
| 99 | 2026-06-20 | Q1116–Q1140 | 16 | 0 | 9 | D3 Infrastructure + D5 Data Protection + D1 Detection + D4 IAM + D2 Incident Response + D6 Governance (Week 2 DOJO GAP DRILL - Udemy + Dojo 3 operational gaps) | [Jump](#session-99--2026-06-20) |
| 100 | 2026-06-20 | Q1141–Q1191 | 49 | 1 | 1 | D3 Infrastructure · D5 Data Protection · D4 IAM · D1 Detection · D6 Governance · D2 Incident Response | [Jump](#session-100--2026-06-20) |
| 101 | 2026-06-20 | Q1192–Q1206 | 14 | 1 | 0 | D6 Governance · D5 Data Protection · D1 Detection · D3 Infrastructure · D4 IAM | [Jump](#session-101--2026-06-20) |
| 102 | 2026-06-21 | Q1207–Q1233 | 18 | 0 | 9 | D3 Infrastructure · D1 Detection · D5 Data Protection · D6 Governance · D2 Incident Response | [Jump](#session-102--2026-06-21) |
| 103 | 2026-06-22 | Q1234–Q1244 | 0 | 0 | 11 | D1 Detection · D3 Infrastructure · D4 IAM · D5 Data Protection · D6 Governance (Dojo Practice Exam Set 4) | [Jump](#session-103--2026-06-22) |
| 104 | 2026-06-22 | Q1245–Q1254 | 8 | 0 | 2 | D1 Detection · D3 Infrastructure · D4 IAM · D5 Data Protection · D6 Governance (Dojo 4 re-test drill) | [Jump](#session-104--2026-06-22) |
| 105 | 2026-06-22 | Q1255–Q1264 | 8 | 0 | 2 | D1 Detection · D3 Infrastructure · D4 IAM · D5 Data Protection · D6 Governance (Killer difficulty cross-domain drill) | [Jump](#session-105--2026-06-22) |
| 106 | 2026-06-22 | Q1265–Q1274 | 8 | 0 | 2 | D1 Detection · D2 Incident Response · D6 Governance (D1+D6 targeted push — killer difficulty) | [Jump](#session-106--2026-06-22) |
| 107 | 2026-06-22 | Q1275–Q1319 | 35 | 0 | 10 | D1 Detection · D3 Infrastructure · D5 Data Protection · D6 Governance (D1+D6 uplift drill + D2/D3 cross-domain) | [Jump](#session-107--2026-06-22) |
| 108 | 2026-06-23 | Q1320–Q1379 | 57 | 0 | 3 | D1 Detection · D2 Incident Response · D3 Infrastructure · D4 IAM · D5 Data Protection · D6 Governance (Red-priority kill drill — all 48 red areas) | [Jump](#session-108--2026-06-23) |

---

## Sessions

### Session 1 — 2025-05-01

**Domains:** D1 Detection · D3 Infrastructure · D4 IAM · D5 Data Protection
**Score:** 10 ✅ · 6 ⚠️ · 4 ❌ (50% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Review Topic |
|---|---|---|---|---|---|---|
| 1 | D1 | S3 bucket exfiltrated object-by-object — which CloudTrail event type? Enabled by default? | "Not enabled by default, PutEvent" | ⚠️ | Data events, **GetObject** (not Put). Not enabled by default. | CloudTrail data vs management events |
| 2 | D1 | Lambda `UpdProdCount` — most flexible way to log invocations? | Didn't know | ❌ | Advanced event selectors with `StartsWith` on resource ARN | Basic vs Advanced event selectors |
| 3 | D3 | Session Manager — security advantage from network perspective? | "No open ports" | ✅ | No inbound ports needed — outbound HTTPS only | Session Manager |
| 4 | D3 | NACLs or Security Groups — which is stateless and needs ephemeral ports? | "NACLs, 100% sure" | ✅ | NACLs are stateless | NACLs vs Security Groups |
| 5 | D1 | Detect public S3 buckets org-wide with least overhead? | Didn't know | ❌ | **Security Hub** — built-in S3 controls, org-wide | Security services comparison |
| 6 | D1 | Lambda stopped logging — Config + what? | Confused | ⚠️ | Depends: role changed → Config + IAM Access Analyzer. Role fine → CloudWatch Logs Insights | Troubleshooting (Task 1.3) |
| 7 | D4 | Resource-based policy vs RCP — difference? | Confused them | ⚠️ | RBP = per-resource, grants access. RCP = org-wide ceiling, never grants. | Policy layers reference |
| 8 | D5 | Can you rotate imported KMS key material? | "Yes" | ✅ | Yes, but only manually (alias swap) | KMS rotation matrix |
| 9 | D5 | KMS imported key — who owns durability? | "You" | ✅ | You — AWS doesn't back up imported material | KMS imported keys |
| 10 | D5 | Import NEW material into EXISTING key? | Knew it was wrong | ✅ | ❌ Can't — only re-import SAME material. New material = new key + alias swap. | KMS imported keys |
| 11 | D4 | Why can't you use RAM for KMS cross-account? | "RAM is not for sharing?" | ⚠️ | RAM IS for sharing, but doesn't support KMS. Use KMS Grants. | RAM vs KMS Grants |
| 12 | D4 | RAM vs RCP — difference? | "Didn't remember RCP" | ⚠️ | RAM shares infrastructure. RCP restricts data access. Opposite problems. | faq-ram-vs-rcp.md |
| 13 | D1 | Suspicious root login attempts — GuardDuty vs CloudTrail + CloudWatch? | Chose CloudTrail + CloudWatch | ❌ | **GuardDuty + EventBridge** — "suspicious" = GuardDuty, least overhead | GuardDuty vs CloudTrail |
| 14 | D3 | Lambda in private subnet — restrict domain lookup to one domain? | Didn't know | ❌ | **Route 53 Resolver DNS Firewall** | DNS Firewall |
| 15 | D5 | Cross-account S3 + SSE-KMS — how many policies needed? | Got Account A right, missed B | ⚠️ | THREE: bucket policy + key policy + identity policy on caller | Cross-account patterns |
| 16 | D4 | When to use RCP — identify the use case? | Got it after review | ✅ | "Outsiders + my data + org-wide" → RCP | RCP use cases |
| 17 | D1 | GuardDuty — what is it responsible for? | "GuardDuty" (for crypto mining) | ✅ | Threat detection — active malicious behavior | Security services |
| 18 | D1 | Security Hub setup order — 4 steps? | Followed along | ✅ | Enable SH → make admin → enable members → assume roles | Security Hub |
| 19 | D4 | `aws:PrincipalIsAWSService` — when to use? | Understood after explanation | ✅ | Always add when using PrincipalOrgID deny — exempts CloudTrail, Config, etc. | RCP conditions |
| 20 | D4 | VPC endpoints — why 3 for Session Manager? | Understood | ✅ | `ssm` (API) + `ssmmessages` (session) + `ec2messages` (heartbeat) | Session Manager VPC endpoints |

---

### Session 2 — 2025-05-02

**Domains:** D1 Detection (re-test)
**Score:** 2 ✅ · 0 ⚠️ · 1 ❌ (67% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 21 | D1 | Root user API calls from unexpected country — detect + isolate with least overhead? | B: GuardDuty → EventBridge → Step Functions | ✅ | GuardDuty for behavioral threats, Step Functions for orchestration | Q13 | Security services comparison |
| 22 | D1 | Log only `Prod-*` Lambda invocations, exclude read-only, queryable in Lake? | B: Advanced event selectors with StartsWith + readOnly + eventName | ✅ | Advanced selectors required for prefix, Lake requires advanced | Q2 | CloudTrail advanced selectors |
| 23 | D1 | What is CloudTrail Lake? What problem does it solve? | Didn't know it existed | ❌ | Managed query engine — replaces S3+Athena plumbing, near real-time, dashboards | — | CloudTrail Lake vs S3+Athena |

---

### Session 3 — 2025-05-03

**Domains:** D1 Detection (re-test)
**Score:** 1 ✅ · 1 ⚠️ · 0 ❌ (50% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 24 | D1 | 200 accounts, detect public S3 buckets org-wide, least overhead — Config conformance pack vs Security Hub vs Macie vs Lambda? | B: Config conformance pack | ⚠️ | C: **Security Hub** FSBP standard — wraps Config rules with less overhead, one-click org-wide, dashboards | Q5 | Security services comparison |
| 25 | D1 | Investigate credential compromise across 15 accounts, need SQL + dashboards + fast results — Athena vs Lake vs CloudWatch Logs vs OpenSearch? | B: CloudTrail Lake | ✅ | CloudTrail Lake — near real-time, cross-account, built-in SQL + dashboards | Q23 | CloudTrail Lake vs S3+Athena |

---

### Session 110 — 2026-06-24

**Domains:** D2 Incident Response (D2 uplift drill — novel operational patterns)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1390 | D2/D5 | Cross-account forensic snapshot, encrypted EBS, share with external firm — sequence? | B: Copy with new CMK + Grant Decrypt + share snapshot | ✅ | Copy re-encrypts, Grant gives access, RAM doesn't support KMS | — | Forensic snapshot sharing cross-account |
| 1391 | D2 | 12-account role investigation, custom Python, reusable template — tool? | C: SageMaker notebooks | ✅ | Custom code + reusable + interactive = SageMaker | — | SageMaker notebooks vs Detective (custom vs built-in) |
| 1392 | D2/D3 | C2 active, block surgically + preserve memory + keep production — THREE? | B+C+D: NF DROP + no-reboot AMI + EBS snapshot | ✅ | NF=surgical, AMI=memory, snapshot=disk | — | Surgical containment (NF + forensics) |
| 1393 | D2 | Test full IR pipeline (GD→EB→SF) with realistic findings — approach? | B: CreateSampleFindings | ✅ | Generates real findings through EventBridge flow | — | CreateSampleFindings = test IR pipeline |
| 1394 | D2 | Forensics account: isolation + immutability 1yr + audit access — THREE? | A+B+C: Cross-account copy + Object Lock Compliance + CloudTrail data events | ✅ | Separate account + WORM + audit trail | — | Forensics chain of custody architecture |

---

### Session 111 — 2026-06-25

**Domains:** D1 Detection · D6 Governance · D3 Infrastructure (Week 3 drill — StopLogging, cfn-guard vs Config proactive vs CF Hook, State Manager dual triggers, GuardDuty regional)
**Score:** 20 ✅ · 0 ⚠️ · 5 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1395 | D1 | StopLogging then DeleteTrail 3min later — which detects DeleteTrail? | B: Only EventBridge | ✅ | StopLogging killed CW delivery, EB receives directly | Q860, Q1092 | StopLogging kills own CW Logs delivery |
| 1396 | D1/D4 | RCP blocks external, 200 denied GetObjects, AA + GD enabled — which TWO true? | B+C: AA fires + GD doesn't | ✅ | AA=static policy, GD=needs successful access | Q534, Q706 | Access Analyzer static + GuardDuty ≠ failed attempts |
| 1397 | D1 | Detect root CreateAccessKey within 30s, Write-only trail — approach? | B: EventBridge in mgmt account | ✅ | Specific API + fast = EventBridge | Q474 | EventBridge for API call detection |
| 1398 | D1 | GD enabled, 60d zero findings, 50 EC2s active, no suppression — cause? | D: Export filter | ❌ | B: GuardDuty not enabled in workload region | — | GuardDuty is regional (console shows current region only) |
| 1399 | D1 | Port 445 same subnet, no GD finding, all IPs over 7d — tool? | B: CW Logs Insights | ✅ | No finding = no Detective entry point | Q1277, Q1314 | Detective needs finding. No finding = CW Logs Insights |
| 1400 | D6 | cfn-guard in pipeline, dev deploys via Console — which TWO catch? | B+D: SCP + Config detective | ✅ | SCP=preventive all paths, Config detective=after creation | Q1220, Q1271 | cfn-guard bypassable vs SCP + Config detective |
| 1401 | D6 | ALL CF deploys validated before creation, least custom code — mechanism? | D: SCP | ❌ | B: Config proactive (CF service-level, managed rules) | Q1220 | Config proactive = CF service-level, least code |
| 1402 | D1/D6 | Config remediation succeeds but bucket re-flagged 5min later — cause? | C: Another process re-disabling | ✅ | Remediation returns = something re-creating bad state | Q1287 | Remediation succeeds but returns = re-creation |
| 1403 | D1/D3 | CW agent on boot + every 2hr + single config — approach? | C: Two associations | ❌ | B: ONE State Manager association (OnBoot + rate) | Q1048, Q1071 | State Manager OnBoot + schedule (dual triggers) |
| 1404 | D6 | cfn-guard pipeline + Console bypass, address BOTH paths — which TWO? | B+C: SCP + CF Hook | ⚠️ | A+B: Config proactive + SCP | Q1220 | Config proactive + SCP covers all paths |
| 1405 | D1/D3 | State Manager OnBoot runs at 14:30, next rate at 17:00 — what happens? | B: Runs again (independent triggers) | ✅ | OnBoot and rate are independent | Q1048 | State Manager OnBoot + schedule (dual triggers) |
| 1406 | D6 | cfn-guard rule passes but unencrypted RDS deploys — how? | B: Parameter override at deploy time | ✅ | cfn-guard can't see runtime parameter values | — | cfn-guard = static template text only |
| 1407 | D1 | CW metric filter correct pattern, alarm never fires — cause? | A: Metric value set to 0 | ✅ | Value=0 publishes nothing useful | Q724 | CW metric filter value |
| 1408 | D1 | DNS queries FROM VPC + TO public zone — which TWO logging? | A+B: DNS query logging + Resolver logging | ✅ | DNS query=inbound to zone, Resolver=outbound from VPC | Q1276 | Resolver vs DNS query logging direction |
| 1409 | D1/D3 | Admin stops CW agent manually, next State Manager run — what happens? | C: Re-runs document (re-installs+starts) | ✅ | State Manager re-applies blindly on schedule | Q1048 | State Manager = desired-state enforcement |
| 1410 | D6 | No EC2 without IMDSv2 EVER, preventive, any path — mechanism? | D: Declarative policy | ❌ | B: SCP with ec2:MetadataHttpTokens condition | Q261 | SCP for IMDSv2 (established exam pattern) |
| 1411 | D6 | cfn-guard + Config proactive + CF Hook, dev runs create-stack from CLI — which evaluate? | B+E: Config proactive + Config detective | ❌ | B+C: Config proactive + CF Hook (both CF service-level) | Q1220, Q1271 | CF Hook = CF service-level (same as Config proactive) |
| 1412 | D1 | CT Lake mgmt-only EDS, GetObject query returns zero — TWO causes? | A+C: Data event + no backfill | ✅ | GetObject=data event, Lake no backfill | Q882, Q927 | CloudTrail Lake (data vs mgmt + no backfill) |
| 1413 | D1/D6 | Config org custom rule "Unable to evaluate" in members — fix? | B: Lambda resource-based policy for config.amazonaws.com | ✅ | Org rule = cross-account invoke, resource policy needed | Q908, Q921 | Config org custom rule cross-account invoke |
| 1414 | D1 | Query Security Lake — correct statement? | B: Athena on OCSF Parquet in S3 | ✅ | No built-in engine, use Athena | — | Security Lake = Athena on your S3 |
| 1415 | D1/D3/D6 | Match 4 requirements to services — correct combo? | A: Config proactive + SM + EB + GD S3 | ✅ | Full architecture match | — | Cross-domain architecture matching |
| 1416 | D6 | cfn-guard + Config proactive, dev uses aws s3api create-bucket — which fire? | C: Neither (direct API = SCP + Config detective only) | ✅ | Direct API bypasses all CF-level validation | Q1318 | CLI/Console direct = only SCP + Config detective |
| 1417 | D1 | StopLogging detection speed: CW filter vs EventBridge vs Config — rank? | A: EB(sec) → Config(min) → CW(never) | ✅ | StopLogging kills CW delivery | Q860, Q1309 | EventBridge=seconds, Config=minutes, CW=never |
| 1418 | D1/D3 | Tag removed at 14:00, next rate run at 21:00 — what happens? | B: Does NOT run (instance left target) | ✅ | Tag removed = no longer in target set | — | State Manager target evaluation is dynamic |
| 1419 | D1/D6/D3 | SCP+cfn-guard+SM+EB architecture weakness? | A: cfn-guard misses Console CF deploys | ✅ | cfn-guard = pipeline only, add Config proactive/Hook | Q1220, Q1271 | cfn-guard bypassable vs Config proactive |

---

### Session 112 — 2026-06-27

**Domains:** D6 Governance (hyperfocus uplift — cfn-guard vs Config proactive, WAT milestones, Stack Policy, SCP all-paths, auto-apply on OU join)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1420 | D6 | cfn-guard in CI/CD, dev uses Console to launch CF stack without DeletionProtection — which statement true? | B: Config proactive would have caught this | ✅ | Config proactive = CF service-level, catches Console CF deploys. cfn-guard = pipeline only. | Q1220, Q1271 | cfn-guard bypassable vs Config proactive service-level |
| 1421 | D6 | WAT quarterly report + evidence from Config/CloudTrail automatically — service? | B: Audit Manager | ✅ | WAT milestones = self-reported. Audit Manager = auto-collects evidence. | Q1221, Q1226 | WAT milestones = no automation |
| 1422 | D6 | Stack Policy Allow Update:Modify only, dev tries Update:Replace — result? | B: Fails — Replace not allowed | ✅ | Modify/Replace/Delete are independent actions. Only explicitly allowed actions work. | Q1225 | Stack Policy Modify vs Replace vs Delete independent |
| 1423 | D6 | Match 4 requirements: prevent EBS + detect+fix S3 + self-service VPC + PCI evidence — services? | A: SCP + Config conformance pack + Service Catalog + Audit Manager | ✅ | Full D6 governance decision tree | — | Full governance stack |
| 1424 | D6 | Config proactive rejects template, dev says "I'll fix manually after" — response? | D: Switch to detective | ❌ | **B: Reject — proactive exists to prevent non-compliant resources from ever existing.** Prevention > detect+remediate. | Q858 | Proactive enforcement = don't downgrade for convenience |
| 1425 | D6 | New account joins OU with SCP + conformance pack + FM WAF — which auto-apply? | A: All three | ✅ | SCP (immediate) + org conformance pack (auto-deploy) + FM (auto-scope). All org-level services auto-apply. | Q1313 | SCP + conformance pack + FM = OU-level auto-apply |
| 1426 | D6 | Ensure DeletionProtection on ALL RDS regardless of deployment method — single mechanism? | D: SCP | ✅ | SCP evaluates actual API regardless of source (Console, CLI, CF, Terraform, SDK). | Q1272 | SCP = catches ALL deployment paths |
| 1427 | D6 | Config proactive for RDS DeletionProtection, dev runs direct CLI create-db-instance — blocked? | B: No — proactive only evaluates CF deploys | ✅ | Config proactive = CF service-level only. Direct API = SCP's job. | Q1389 | Console/CLI direct bypasses Config proactive |
| 1428 | D6 | WAT Jan milestone, Jun 3/4 HRIs resolved, CISO wants resource-level CloudTrail evidence — can WAT? | C: No — milestones only show per-question risk changes (self-reported) | ✅ | No automation, no resource links, no CloudTrail integration. | Q1221, Q1233 | WAT = self-reported, no automation |
| 1429 | D6 | cfn-guard + Config proactive + CF Hook + SCP + Config detective, dev creates S3 via Console (no CF) — which TWO fire? | D+E: SCP + Config detective | ✅ | Console direct = no CF = cfn-guard/proactive/Hook all blind. Only SCP + detective fire. | Q1318, Q1385 | CLI/Console direct = only SCP + Config detective |

---

### Session 113 — 2026-06-27

**Domains:** D1 Detection (hyperfocus uplift — remediation loops, Detective vs CW Insights, StopLogging detection, Macie sampling, log source direction)
**Score:** 23 ✅ · 0 ⚠️ · 2 ❌ (92% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1430 | D1 | Config remediation removes SG rule, GD fires same finding 10min later — cause? | B: Another process re-adding the rule | ✅ | Remediation loop = something re-creating bad state. Check CloudTrail for WHO. | Q1287 | Remediation succeeds but returns = re-creation |
| 1431 | D1 | No GD finding, investigate which IPs communicated with suspicious external IP, Flow Logs in CW — tool? | B: CW Logs Insights | ✅ | No finding = no Detective entry point. Data in CW = Insights. | Q1277, Q1314 | Detective needs finding. No finding = CW Logs Insights |
| 1432 | D1 | StopLogging: CW metric filter + EventBridge + Config — which fire and in what order? | B: EventBridge (sec) + Config (min). CW filter never fires. | ✅ | StopLogging kills CW delivery. EB + Config detect. | Q860, Q866 | StopLogging kills own CW Logs delivery |
| 1433 | D1 | GD Recon:EC2/Portscan finding, "what else did source IP talk to 24hr" — tool? | B: Detective | ✅ | Finding EXISTS = Detective entry point. | Q1277, Q1314 | Finding exists = Detective |
| 1434 | D1 | Config remediation removes public access, CF stack update re-adds it — first action? | C: Investigate the CF stack | ✅ | Same re-creation pattern. Investigate root cause before SCP. | Q1287 | Remediation loop = fix root cause |
| 1435 | D1 | Detect iam:CreateAccessKey for root 60s + anomalous S3 volumes — which TWO? | B: EventBridge + GuardDuty S3 Protection | ✅ | Specific API fast = EB. Behavioral = GD S3 Protection. | Q474, Q568 | EventBridge + GuardDuty S3 Protection |
| 1436 | D1 | Macie automated discovery 30d, only 5/200 buckets have findings, PII known in 50 — cause? | B: Automated = sampling, create job for full | ✅ | Enabled ≠ exhaustive scanning. Job = full. | Q1293 | Macie enabled ≠ Macie scanning |
| 1437 | D1 | Flow Logs show IPs but need domain names — which log source? | B: Resolver query logging | ✅ | Resolver = FROM VPC (outbound). DNS query = TO public zone (inbound). | Q1276 | Resolver vs DNS query logging direction |
| 1438 | D1 | Config remediation fixes public S3, CF stack reverts — first action? | C: Investigate CF stack | ✅ | Root cause investigation before prevention. | Q1287 | Remediation loop = fix root cause |
| 1439 | D1 | GD S3 Protection: same-org account downloads 500 objects 3AM unusual country — fires? | B: Yes — behavioral regardless of org | ✅ | GD S3 Protection = anomaly detection, org irrelevant. | Q1268 | GuardDuty S3 Protection behavioral |
| 1440 | D1 | CT Lake mgmt-only EDS, PutObject query returns zero — TWO causes? | A+B: Data event + ingestion delay | ❌ | A+D: Data event (correct) + Lake doesn't backfill (not ingestion delay). | Q882, Q927 | CloudTrail Lake (data vs mgmt + no backfill) |
| 1441 | D1 | Macie SSE-KMS "Unable to analyze" on 30/200 buckets — cause? | B: Key policies don't grant Macie SLR kms:Decrypt | ✅ | Key policy must grant service SLR access. | Q1305 | Macie + SSE-KMS key policy |
| 1442 | D1 | Security Hub non-compliant, want auto-fix — where configure? | C: Security Hub custom actions + EB + Lambda | ❌ | B: Config rule auto-remediation (SSM). SH = dashboard only. | Q1307 | Security Hub = dashboard. Config = remediation. |
| 1443 | D1 | Resolver query logging enabled, public zone external queries missing — why? | A: Resolver = VPC outbound only, not inbound to public zones | ✅ | Two different features, different directions. | Q1276 | Resolver vs DNS query logging direction |
| 1444 | D1 | CW metric filter correct pattern, alarm never fires, trail delivers to log group — cause? | A: Metric value set to 0 instead of 1 | ✅ | Value=0 publishes nothing useful. | Q724 | CW metric filter value |
| 1445 | D1 | GD S3 Protection: same-account Lambda 10x volume + 3AM + new region — fires? | B: Yes — behavioral anomaly detection | ✅ | Anomaly = baseline deviation regardless of caller identity. | Q1268 | GuardDuty S3 Protection behavioral |
| 1446 | D1 | StopLogging then DeleteTrail 3min later — which detects DeleteTrail? | B: Only EventBridge | ✅ | StopLogging killed CW delivery, EB receives directly | Q860, Q1092 | StopLogging kills own CW Logs delivery |
| 1447 | D1 | Top 10 source IPs by bytes, Flow Logs in S3 (not CW) — tool? | B: Athena | ✅ | CW Logs Insights can't query S3. Athena queries S3 directly. | Q236 | CW Logs Insights scope (CW only) |
| 1448 | D1 | CT Insights 10x RunInstances, GD silent — which true? | B: Complementary (Insights=volume, GD=behavior) | ✅ | Legit spike triggers Insights not GD. Different detection lenses. | Q1004 | CloudTrail Insights vs GuardDuty (complementary) |
| 1449 | D1 | Macie SSE-KMS "Unable to analyze" one bucket, others work — check first? | B: Key policy missing Macie SLR kms:Decrypt | ✅ | Per-key grant needed. Other keys work = those grant access. | Q1305 | Macie + SSE-KMS key policy |
| 1450 | D1 | SH 47 non-compliant, engineer proposes fix inside SH — why wrong? | B: SH = dashboard, Config = remediation | ✅ | SH views. Config + SSM fixes. | Q1307, Q1442 | Security Hub = dashboard. Config = remediation. |
| 1451 | D1 | DNS query logging on public zone, can't see Lambda queries from VPC — why? | B: DNS query logging = TO zone from internet, not FROM VPC | ✅ | Two features, two directions. VPC queries = Resolver logging. | Q1276 | Resolver vs DNS query logging direction |
| 1452 | D1 | Config remediation enables S3 logging, succeeds but no logs appear — missing? | B: s3:GetBucketAcl — logging uses ACLs | ✅ | Legacy ACL mechanism for S3 access logging. | Q864, Q868, Q903 | S3 server access logging = ACLs |
| 1453 | D1 | OutsideAWS finding, "what else accessed 72hr" — tool? | C: Detective | ✅ | Finding exists + blast radius + timeline = Detective. | Q1277 | Finding exists = Detective |
| 1454 | D1 | Detect CreateUser without MFA, 300 accounts, sub-60s, org trail — approach? | B: EventBridge in management account | ✅ | Specific API + fast + org trail = EventBridge. | Q474 | EventBridge for API call detection |

---

### Session 109 — 2026-06-24

**Domains:** D1 Detection · D3 Infrastructure · D6 Governance (Week 2 never-seen drill — Bedrock, NACLs, StopLogging, cfn-guard vs Config proactive)
**Score:** 8 ✅ · 0 ⚠️ · 2 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1380 | D3 | Bedrock mandatory guardrail org-wide, dev deploys without it — enforcement? | C: SCP + bedrock:GuardrailIdentifier | ✅ | SCP condition key = org-wide, no exceptions | — | Bedrock IAM guardrail enforcement (condition key) |
| 1381 | D3 | Flow Log inbound ACCEPT + outbound REJECT, SG allows 443 — cause? | B: NACL missing outbound ephemeral | ✅ | NACLs stateless, need explicit outbound | — | NACLs stateless |
| 1382 | D1 | CW metric filter on StopLogging fails, EventBridge succeeds — why? | C: StopLogging kills own CW delivery | ✅ | EB receives from CT management stream directly | — | StopLogging kills own CW Logs delivery |
| 1383 | D1/D4 | RCP blocks external, 500 denied GetObjects, AA + GD enabled — which TWO true? | B+C: AA fires + GD doesn't fire | ✅ | AA=static policy, GD=needs successful access | — | Access Analyzer static + GuardDuty ≠ failed attempts |
| 1384 | D1/D3 | CW agent on boot + every 2hr + single config — approach? | B: ONE State Manager association (OnBoot + rate) | ✅ | Dual triggers on single association | — | State Manager OnBoot + schedule (dual triggers) |
| 1385 | D6 | Console deploy S3 without encryption, cfn-guard + proactive + SCP + detective — which fire? (TWO) | C+D: SCP + Config detective | ✅ | Console = no CF = cfn-guard/proactive blind | — | Console direct = SCP + Config detective only |
| 1386 | D1 | No GD finding, internal IP port 445 spike, query all destinations 7d — tool? | B: CW Logs Insights | ✅ | No finding = no Detective entry point | — | Detective needs finding. No finding = CW Logs Insights |
| 1387 | D6 | CF template must have DeletionProtection, all CF paths, can't bypass — mechanism? | B: SCP | ❌ | **C: Config proactive** — SCP can't inspect template content, only API params | — | cfn-guard bypassable vs Config proactive service-level |
| 1388 | D3/D5 | Lambda private subnet, SM works, direct kms:GenerateDataKeyWithoutPlaintext times out — fix? | A: KMS Interface endpoint | ✅ | Direct KMS call = needs own endpoint. Timeout = network. | — | KMS endpoint for direct calls only |
| 1389 | D6 | cfn-guard bypassed via Console direct, detect + prevent — which TWO? | A+B: SCP + Config proactive | ❌ | **A+C: SCP (prevent all paths) + Config detective+SSM (detect+fix existing)**. Console direct = no CF = proactive blind. | — | Console direct bypasses Config proactive |

---

### Session 114 — 2026-06-27

**Domains:** D6 Governance (hyperfocus uplift — Config proactive scope, Security Hub setup, WAT vs Audit Manager, Stack Policy, Service Catalog)
**Score:** 49 ✅ · 0 ⚠️ · 11 ❌ (82% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1455 | D6 | Config proactive + RDS DeletionProtection, dev runs CLI rds:CreateDBInstance directly — why not blocked? | B: Config proactive = CF only | ✅ | Config proactive only evaluates CloudFormation deployments, not direct API calls | Q1389 | Config proactive = CF only, not direct API |
| 1456 | D6 | WAT: CISO wants Config rule changes + CloudTrail events + resource evidence mapped to controls — which? | B: WAT = risk snapshots, Audit Manager = evidence | ✅ | WAT = self-reported. Audit Manager = automated evidence + control mapping | Q1221, Q1226 | WAT = self-reported, Audit Manager = evidence |
| 1457 | D6 | Security Hub setup 200 accounts from delegated admin — correct sequence? | B: Enable in mgmt → Designate → Members → Standards | ✅ | E-D-M-A: Enable first, Designate second | Q1244, Q1273 | Security Hub setup ordering (E-D-M-A) |
| 1458 | D6 | cfn-guard in pipeline, dev creates S3 via Console (no CF), detect+prevent — which TWO? | B+D: SCP + Config detective+SSM | ✅ | Console direct = no CF = proactive/Hook blind. SCP prevents, Config+SSM detects+fixes | Q1389 | Console direct = SCP + Config detective |
| 1459 | D6 | Account joins OU with SCP+conformance pack+FM WAF, existing EBS+ALB — which TWO true? | C+E: SCP future only + FM auto-attaches WAF | ✅ | SCP = bouncer (future). FM = auto-remediates existing. | Q1425 | SCP future only + FM auto-remediates existing |
| 1460 | D6 | Stack Policy Allow Update:* + Deny Replace/Delete on ProductionDB, engine change requires replacement — result? | B: Fails — explicit Deny wins | ✅ | Explicit Deny always wins (same as IAM) | Q1225 | Stack Policy explicit Deny wins |
| 1461 | D6 | S3 encryption posture improved Jan→Jun, before/after evidence, least overhead — approach? | B: Audit Manager assessments Jan+Jun compare | ✅ | Audit Manager = evidence collection for compliance | Q1221, Q1233 | Audit Manager for compliance evidence |
| 1462 | D6 | Config proactive AND CF Hook registered, dev runs create-stack from CLI — how many pre-creation? | C: Two — both evaluate before creation | ✅ | Both are CF service-level, both intercept any CF deploy | Q1411 | Config proactive + CF Hook = both pre-creation |
| 1463 | D6 | Account joins OU, SCP blocks DeleteDetector, existing suppression rule — effect? | B: SCP blocks deletion only, suppression continues | ✅ | SCP blocks specific API actions, doesn't affect existing config | — | SCP = action-level block, not config override |
| 1464 | D6 | Service Catalog VPCs, 30% flow logs disabled after provisioning — what's true + fix? | C: Launch constraint prevents changes | ❌ | **B: SC doesn't monitor post-provisioning. Fix = Config + SSM.** | — | Service Catalog = no post-deploy monitoring |
| 1465 | D6 | Console direct S3 no encryption, cfn-guard+proactive+SCP+detective — which catch? (TWO) | C+D: SCP + Config detective | ✅ | Console = no CF = proactive/Hook blind | Q1389 | Console direct = SCP + Config detective |
| 1466 | D6 | Security Hub = dashboard, junior proposes auto-fix inside SH — why wrong? | B: SH = dashboard, Config+SSM = remediation | ✅ | SH views, Config fixes | Q1307, Q1442 | Security Hub = dashboard. Config = remediation. |
| 1467 | D6 | Org conformance pack 15 rules, new account joins OU — what happens? | B: Auto-deploys all rules immediately | ✅ | Organizational conformance pack = auto-deploy | Q1313 | Conformance pack auto-deploys |
| 1468 | D6 | WAT: can it pull Config/CloudTrail evidence automatically? | B: No, milestones = self-reported only | ✅ | WAT = no automation, no resource links | Q1221 | WAT = self-reported, no automation |
| 1469 | D6 | Stack Policy no Allow, only Deny on one resource — Update:Modify? | B: Fails — default deny all, must explicitly Allow | ✅ | Stack Policy = default deny all | Q1225 | Stack Policy default deny |
| 1470 | D6 | FM needs RAM for DNS FW but not for WAF — why? | A: RAM shares existing rule group cross-account | ✅ | FM creates WAF directly, DNS FW rule group lives elsewhere | Q441 | FM creates WAF directly, needs RAM for DNS FW |
| 1471 | D6 | SC product EKS, logging disabled after 3 months — which TWO true? | B+C: SC no monitoring + fix = Config+SSM | ✅ | SC = deploy and forget | — | Service Catalog = no post-deploy monitoring |
| 1472 | D6 | Config proactive blocks template, dev says "I'll fix manually after" — response? | B: Reject — proactive exists to prevent non-compliant | ✅ | Don't downgrade for convenience | Q858 | Proactive enforcement = don't downgrade |
| 1473 | D6 | IMDSv2 enforcement: cfn-guard+proactive+SCP, dev runs CLI run-instances — which fires? | B: Only SCP | ✅ | CLI direct = no CF = only SCP | Q1389 | CLI direct = only SCP fires |
| 1474 | D6 | Full governance match: prevent+detect/fix+self-service+evidence — services? | A: SCP → Config+SSM → Service Catalog → Audit Manager | ✅ | Full D6 decision tree | — | Full governance stack |
| 1475 | D6 | FM WAF policy, new account joins with 3 ALBs — when protected? | A: Immediately — FM auto-scopes | ✅ | FM auto-scopes existing resources | Q284 | FM auto-remediates immediately |
| 1476 | D6 | SCP denies RunInstances without tag, SC launch role launches without tag — result? | B: Fails — SCP applies to all principals including SC role | ✅ | SCP = all principals in member accounts | — | SCP applies to SC launch roles |
| 1477 | D6 | Dev says "SCP allows this!" after Config proactive rejects — why wrong? | B: Proactive fires before API call, SCP never consulted | ✅ | Config proactive → before API → SCP never sees it | Q1220 | Config proactive fires before SCP in CF |
| 1478 | D6 | SCP deny ScheduleKeyDeletion + break-glass role exception — approach? | A: StringNotLike PrincipalARN condition | ✅ | SCPs support conditions for exceptions | — | SCP condition exemption pattern |
| 1479 | D6 | Terraform uses CF, Config proactive enabled — does proactive evaluate? | B: Yes — any CF deploy evaluated regardless of trigger | ✅ | Config proactive = CF service-level, any source | Q1220 | Config proactive = any CF deploy |
| 1480 | D6 | CIS score + SOC 2 evidence + design gaps — match 3 services? | A: Security Hub → Audit Manager → WAT | ✅ | Three distinct purposes | — | SH vs AM vs WAT |
| 1481 | D6 | Config remediation loop — bucket re-flagged 10min after fix — cause? | B: Something re-disabling (check CloudTrail) | ✅ | Remediation loop = re-creation | Q1287 | Remediation succeeds but returns |
| 1482 | D6 | SH enabled, 0% compliance, Config running — what's missing? | B: Standards must be explicitly enabled | ✅ | Enable SH ≠ enable standards | Q1244 | SH standards must be enabled separately |
| 1483 | D6 | StackSets deploys Config, dev runs StopConfigurationRecorder — what happens? | B: Nothing — StackSets no auto-remediation | ✅ | StackSets = deploy and forget | Q283 | StackSets no auto-remediation |
| 1484 | D6 | No public IPv4 regardless of current/future API — mechanism? | C: Declarative policy | ✅ | State enforcement vs API enumeration | — | Declarative = future-proof |
| 1485 | D6 | CT detects manual SCP modification — what happens? | B: Reports drift, no auto-fix | ✅ | CT drift = alert only | — | Control Tower drift |
| 1486 | D6 | CF deploy: Config proactive + SCP both present — which STOPS resource first? | B: Config proactive (fires before API call) | ❌ | Proactive rejects template → CF never calls API → SCP never fires | Q1220 | Config proactive fires BEFORE SCP in CF deploys |
| 1487 | D6 | Inspector via StackSets, operational problem? | B: Inspector has native delegated admin + auto-enable | ✅ | Native org = use native | Q483 | Native org-wide deployment |
| 1488 | D6 | Stack Policy empty Statement array, dev tries update — result? | B: Fails — default deny all | ✅ | No Allow = nothing passes | Q1225 | Stack Policy default deny |
| 1489 | D6 | Audit Manager 95% vs Security Hub 60% — why discrepancy? | B: AM includes manual evidence (attestations) | ✅ | AM = manual + automated, SH = automated only | — | Audit Manager includes manual evidence |
| 1490 | D6 | RAM shares NF policy, FM enforces, admin deletes endpoint — what happens? | B: FM re-creates endpoint | ✅ | FM auto-remediates lifecycle | Q441 | RAM + FM complementary |
| 1491 | D6 | Verb match: visible + ensure + deploy + pull — services? | A: RAM → FM → StackSets → Service Catalog | ✅ | Verb-to-service mapping | — | RAM vs FM vs StackSets vs SC |
| 1492 | D6 | SCP denies StopConfigurationRecorder + conformance pack + new account — which TWO auto-apply? | A+B: SCP + conformance pack | ✅ | Both auto-apply on OU join | Q1313 | SCP + conformance pack = OU-level auto |
| 1493 | D6 | SH custom action "Remediate" button — what triggers? | B: Custom action → EventBridge → Lambda (you built) | ✅ | SH = dashboard, you build the automation | Q1307 | SH custom action = you build it |
| 1494 | D6 | StackSets deployed Config+CloudTrail, need new rule + remediation org-wide — approach? | B: Organizational conformance pack | ✅ | New rules = conformance pack layer | — | StackSets foundation + conformance pack rules |
| 1495 | D6 | Declarative no-public-IPv4, AWS releases new API — needs update? | B: No — state enforcement, future-proof | ✅ | Declarative = regardless of API | — | Declarative policy future-proof |
| 1496 | D6 | FM WAF policy, new ALB, developer has no WAF perms — what happens? | B: FM attaches using own service role | ✅ | FM's role, dev perms irrelevant | Q284 | FM uses own role |
| 1497 | D6 | Config proactive = ALL RDS DeletionProtection regardless of deploy method — flaw? | B: Only covers CF, CLI/Console bypass | ✅ | "Regardless of method" = need SCP | Q1389 | Config proactive = CF only |
| 1498 | D6 | RAM shares subnet, dev launches EC2 — who owns instance? | B: Workload account (launcher) | ✅ | Launcher owns resources in shared infra | — | RAM shared subnet ownership |
| 1499 | D6 | Config proactive rejects template — where in CloudTrail? | B: Config evaluation result | ❌ | **A: CloudTrail failed CreateStack API call** | — | Proactive rejection = CloudTrail failed API |
| 1500 | D6 | WAT review for ISO 27001 audit evidence — correct response? | B: WAT = self-reported, use Audit Manager for ISO evidence | ✅ | WAT ≠ audit evidence | Q1221 | WAT vs Audit Manager |
| 1501 | D6 | Enforcement timing: cfn-guard → proactive → SCP → detective — order? | A: Pipeline → CF eval → API call → after exists | ✅ | Full enforcement timeline | — | Enforcement timeline |
| 1502 | D6 | SCP on member root user StopLogging — result? | B: Fails — SCP applies to member root | ✅ | Member root subject to SCP | — | SCP applies to member root |
| 1503 | D6 | CI/CD: cfn-guard first to reject unencrypted EBS — why? | B: Pipeline runs before CF deploy | ✅ | cfn-guard = shift-left, earliest gate | — | cfn-guard = earliest in pipeline |
| 1504 | D6 | Audit Manager "insufficient evidence" for MFA control — why? | B: Needs manual evidence alongside automated | ✅ | Some controls need both types | — | AM manual + automated evidence |
| 1505 | D6 | StackSets auto-deploy + SH auto-enable, new account joins — both deploy? | A: Both auto-deploy | ❌ | StackSets auto-deploy = handles new accounts. SH auto-enable = handles new accounts. | — | StackSets auto-deploy = new accounts |
| 1506 | D6 | Different Config rules per OU (Prod strict, Dev relaxed) — approach? | B: Separate conformance packs per OU | ✅ | Org conformance packs target OUs | — | Conformance packs per OU |
| 1507 | D6 | SC product, dev removes tag after provisioning — what happens? | B: Nothing — SC no post-deploy monitoring | ✅ | SC = deploy and forget | — | Service Catalog no monitoring |
| 1508 | D6 | SH enabled, standards enabled, Config stopped in one member — findings? | B: That account shows no data | ✅ | SH depends on Config | — | SH requires Config running |
| 1509 | D6 | CT custom preventive guardrail for RDS final snapshot — how? | A: Custom SCP registered as CT preventive control | ❌ | Control Tower supports custom SCPs as preventive controls | — | CT supports custom controls |
| 1510 | D6 | cfn-guard sees !Ref EncryptionParam — result? | B: FAIL — static text, can't resolve Refs | ❌ | cfn-guard = static analysis only | — | cfn-guard can't resolve intrinsics |
| 1511 | D6 | Console CF deploy: cfn-guard + proactive + Hook + SCP + detective — which fire? (THREE) | B+C+D: Proactive + Hook + SCP | ✅ | Console CF = all except cfn-guard (pipeline only) | Q1318 | Console CF = all layers except cfn-guard |
| 1512 | D6 | RAM TGW shared, member deletes own attachment — allowed? | B: Yes — member owns their attachment | ❌ | RAM shares parent, member resources = member-owned | — | RAM attachment = member-owned |
| 1513 | D6 | SCP alone minimum for "all paths" EBS encryption — correct? | A: Yes — evaluates actual API regardless of source | ✅ | SCP = minimum for all-path prevention | — | SCP = all deployment paths |
| 1514 | D6 | SH 0% after enabling standards — when do findings appear at 200-account scale? | A: Within minutes | ❌ | **B: 2-24 hours (Config evaluation latency at scale)** | — | Standards evaluation latency at scale |

---

<!-- TEMPLATE: Copy this block for new sessions
### Session 115 — 2026-06-28

**Domains:** D6 Governance (re-test — Session 114 errors)
**Score:** 60 ✅ · 0 ⚠️ · 3 ❌ (95% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1515 | D6 | Service Catalog EKS clusters, logging disabled 3mo later — correct statement + fix? | B: SC no post-deploy monitoring + Config+SSM | ✅ | SC doesn't monitor after provisioning. Config+SSM detects+fixes. | Q1464 | Service Catalog = no post-deploy monitoring |
| 1516 | D6 | Config proactive + SCP both present, CF deploy without DeletionProtection — order? | B: Proactive fires first, CF never calls API, SCP never evaluates | ✅ | Config proactive fires BEFORE SCP in CF deploys | Q1486 | Config proactive fires BEFORE SCP in CF deploys |
| 1517 | D6 | Config proactive rejects template — where in CloudTrail? | A: Failed CreateStack API call | ✅ | Proactive rejection = CloudTrail failed API | Q1499 | Proactive rejection = CloudTrail failed API |
| 1518 | D6 | StackSets service-managed + auto-deploy, new account joins OU — what happens? | B: Auto-deploys without manual action | ✅ | StackSets auto-deploy = new accounts get stack automatically | Q1505 | StackSets auto-deploy = new accounts |
| 1519 | D6 | CT custom preventive guardrail for RDS FinalDBSnapshot — how? | B: Register custom SCP as CT preventive control | ✅ | CT supports custom controls (SCP=preventive, Config=detective, Hook=proactive) | Q1509 | CT supports custom controls |
| 1520 | D6 | cfn-guard rule, template uses !Ref EncryptionEnabled — result? | B: FAIL — sees literal text, can't resolve Ref | ✅ | cfn-guard can't resolve intrinsics (!Ref, !Sub, Fn::If) | Q1510 | cfn-guard can't resolve intrinsics |
| 1521 | D6 | RAM shared TGW, member creates+deletes own attachment — allowed? | B: Yes — member owns resources they create | ✅ | RAM attachment = member-owned | Q1512 | RAM attachment = member-owned |
| 1522 | D6 | SH 200 accounts, standards enabled, 0% after 15min — cause? | B: 2-24 hours (Config evaluation latency at scale) | ✅ | Standards evaluation latency at scale | Q1514 | Standards evaluation latency at scale |
| 1523 | D6 | Config proactive + direct CLI rds:CreateDBInstance — blocked? | B: No — proactive = CF only, not direct API | ✅ | Config proactive = CF only, not direct API | — | Config proactive = CF only |
| 1524 | D6 | 12 new Config rules + remediation + org-wide + auto new accounts — approach? | B: Organizational conformance pack | ✅ | Conformance pack = bundle + remediation + auto-deploy | — | Conformance pack vs StackSets |
| 1525 | D6 | Stack Policy empty Statement array, dev tries update — result? | B: Fails — default deny all | ✅ | No Allow = nothing passes | — | Stack Policy default deny |
| 1526 | D6 | FM WAF + FM DNS FW — which needs RAM? | C: Only DNS Firewall requires RAM | ✅ | FM creates WAF directly, DNS FW rule group needs RAM sharing | — | FM WAF vs FM DNS FW RAM dependency |
| 1527 | D6 | SCP denies ec2:AssignIpv6Address, new API ec2:AssignIpv6PublicPool — protected? | B: No — SCPs must enumerate specific actions | ✅ | Declarative = state enforcement vs SCP = action-specific | — | Declarative policy vs SCP (future API) |
| 1528 | D6 | SH enabled 48hr, findings aggregated, compliance tab empty — missing? | B: Standards must be explicitly enabled | ✅ | Enable SH ≠ enable standards | — | SH standards must be explicitly enabled |
| 1529 | D6 | SCP modified outside CT, CT detects — what happens? | B: Reports drift, no auto-fix | ✅ | CT drift = alert only, manual resolution | — | Control Tower drift |
| 1530 | D6 | SCP denies DeleteDetector, management account calls it — result? | B: Allowed — management account exempt | ✅ | Management account exempt from SCPs | — | Management account exempt from SCP |
| 1531 | D6 | Prod OU strict rules, Dev OU relaxed — approach? | B: Two separate conformance packs per OU | ✅ | Org conformance packs target specific OUs | — | Conformance packs per OU |
| 1532 | D6 | Find+revoke 0.0.0.0/0 + apply baseline SG — FM policy types? | C: SG audit + SG common | ✅ | Audit=remove bad, Common=add good | — | FM SG audit vs FM SG common |
| 1533 | D6 | SC launch role + SCP denies without tag, template lacks tag — result? | B: Fails — SCP applies to launch role | ✅ | SCP applies to SC launch roles | — | SCP applies to all principals |
| 1534 | D6 | Console S3 creation, cfn-guard+proactive+SCP+detective — which fire? (TWO) | C: SCP + Config detective | ✅ | Console direct = no CF = only SCP + detective | — | Console direct = SCP + Config detective |
| 1535 | D6 | Config rule to re-enable own recorder — why flawed? | A: Circular dependency | ❌ | B: Recorder stopped = rules can't fire. Detection engine is dead. Use SCP to prevent. | — | Config can't detect own death = use SCP |
| 1536 | D6 | StackSets deployed GD, admin manually deletes detector — what happens? | B: Nothing — StackSets no auto-remediation | ✅ | StackSets = deploy and forget | Q283, Q439 | StackSets no auto-remediation |
| 1537 | D6 | Delegated admin — which services support it? | B: All major security services | ✅ | Every security service supports delegated admin | — | Delegated admin (all services) |
| 1538 | D6 | SH 92% FSBP, why also need WAT? | B: SH=resource compliance, WAT=architecture review+improvement plans | ✅ | Different levels: resource vs workload design | — | Security Hub vs WAT |
| 1539 | D6 | RAM shares subnet, dev launches EC2 — who owns instance? | B: Account B (launcher) | ✅ | RAM shares infra, launched resources belong to launcher | — | RAM shared subnet ownership |
| 1540 | D6 | New account joins OU: SCP+FM WAF+conformance pack, existing ALBs — which TWO true? | B+E: FM existing + SCP future | ❌ | A+B: SCP future only + FM auto-attaches to existing ALBs | — | SCP future only + FM auto-remediates existing |
| 1541 | D6 | Terraform AWS provider deploys RDS, Config proactive enabled — caught? | A: Yes Terraform uses CF | ❌ | B: No — Terraform calls APIs directly, bypasses CF. Proactive = CF only. | — | Terraform = direct API (not CF) |
| 1542 | D6 | WAT milestones: show Config/CloudTrail evidence to auditors? | B: No — self-reported only, use Audit Manager | ✅ | WAT = no automation, no resource links | — | WAT milestones = no automated evidence |
| 1543 | D6 | Stack Policy Allow Modify + Deny Replace/Delete, engine change requires replacement — result? | B: Fails — Replace explicitly denied | ✅ | Modify/Replace/Delete independent. Explicit Deny wins. | — | Stack Policy Modify vs Replace independent |
| 1544 | D6 | SH custom action "Quarantine Instance" button clicked — what triggers? | B: EventBridge event — you build automation | ✅ | SH = dashboard. Custom action → EB → Lambda (you build). | — | SH custom action = EventBridge (you build it) |
| 1545 | D6 | Prevent disabling GD in member accounts — which actions to deny? | B: DeleteDetector + StopMonitoringMembers | ✅ | No DisableGuardDuty API exists. Block both paths. | — | SCP prevents disabling GD |
| 1546 | D6 | SCP deny ScheduleKeyDeletion + break-glass exception — approach? | B: StringNotLike PrincipalARN condition | ✅ | SCPs support conditions for exceptions | — | SCP condition exemption pattern |
| 1547 | D6 | Declarative no-public-IPv4, AWS releases new API — needs update? | B: No — state enforcement, future-proof | ✅ | Declarative = regardless of API | — | Declarative policy future-proof |
| 1548 | D6 | SC launch role + SCP requires versioning, template lacks it — result? | B: Fails — SCP evaluates launch role | ✅ | SCP applies to ALL principals | — | SCP applies to SC launch roles |
| 1549 | D6 | Config proactive rejects, dev asks to switch to detective — response? | B: Reject — proactive exists to prevent non-compliant | ✅ | Don't downgrade for convenience | — | Proactive enforcement philosophy |
| 1550 | D6 | Config rule flags S3 no logging, auto-remediate — where configured? | B: Config rule → SSM Automation | ✅ | Config detects, SSM remediates | — | Config + SSM remediation |
| 1551 | D6 | Deploy GD (native) + custom IAM role (no native) — approach? | B: GD delegated admin + StackSets for IAM role | ✅ | Native = use native. Custom = StackSets. | — | Native vs StackSets hybrid |
| 1552 | D6 | Audit Manager 95% vs Security Hub 60% — why? | B: AM includes manual attestation + automated | ✅ | AM = manual + automated. SH = automated only. | — | Audit Manager includes manual evidence |
| 1553 | D6 | RAM NF policy + FM enforces, admin deletes endpoint — what happens? | B: FM re-creates endpoint | ✅ | FM auto-remediates lifecycle | — | FM auto-remediates deletions |
| 1554 | D6 | SCP on OU, member root user StopLogging — result? | B: Denied — SCP applies to member root | ✅ | Member root subject to SCP. Management root exempt. | — | SCP applies to member root |
| 1555 | D6 | Prevent member accounts sharing externally via RAM — how? | B: SCP condition + Organizations sharing setting | ✅ | Two mechanisms: SCP + org-level setting | — | RAM external sharing controls |
| 1556 | D6 | Org conformance pack 15 rules, new account joins OU — what happens? | B: Auto-deploys all rules immediately | ✅ | Organizational conformance pack = auto-deploy | — | Conformance pack auto-deploys |
| 1557 | D6 | SH standards enabled 200 accounts, 0 findings after 10min — when? | B: 2-24 hours (Config evaluation latency at scale) | ✅ | Config at scale = hours, not minutes | — | Standards evaluation latency |
| 1558 | D6 | SCP denies StopConfigurationRecorder, member admin tries — result? | B: Denied — SCP blocks regardless | ✅ | SCP blocks API regardless of caller | — | SCP protects Config recorder |
| 1559 | D6 | Conformance pack vs StackSets for 20 Config rules — TWO advantages? | A+C: Bundle + auto-deploy to new OU members | ✅ | Purpose-built for Config rules, lighter weight | — | Conformance pack advantages over StackSets |
| 1560 | D2 | Forensics: isolation + immutability 1yr + audit — THREE? | A+B+C: Cross-account + Object Lock + CT data events | ✅ | Separate account + WORM + audit trail | — | Forensics chain of custody architecture |
| 1561 | D2 | Step Functions severity routing (≥8 quarantine, 4-7 notify, <4 suppress) — state type? | B: Choice state evaluates severity | ✅ | Native branching, no Lambda needed | — | Step Functions Choice state for IR |
| 1562 | D2 | Assess RTO + inject AZ failure + shift traffic — match 3 services? | A: Resilience Hub + FIS + ARC zonal shift | ✅ | Assess, test, recover — three verbs | — | Resilience Hub vs FIS vs ARC |
| 1563 | D2 | IAM user leaked vs role exfiltrated — containment? | B: User=Deny *, Role=TokenIssueTime | ✅ | Persistent creds vs temp tokens | — | User = Deny *. Role = TokenIssueTime. |
| 1564 | D2 | Deny-all SG then SSM fails — cause + fix? | B: Acquire BEFORE isolate | ✅ | Deny-all blocks SSM outbound | — | Acquire before isolate |
| 1565 | D3 | Third-party Palo Alto, inline, scale, health-check — component? | C: GWLB with Palo Alto targets | ✅ | GWLB = third-party inline appliances | — | GWLB = third-party inline |
| 1566 | D3 | Private API: Lambda A works, Lambda B timeout, same endpoint — cause? | B: Lambda B SG missing outbound 443 | ✅ | Timeout = network. Same RP = permissions fine. | — | Interface endpoint dual SGs |
| 1567 | D3 | Laptops + office router + dedicated 10G L2 — match? | A: Client VPN + S2S VPN + DX MACsec | ✅ | Three connectivity types | — | VPN types + DX MACsec |
| 1568 | D3 | IPv6 outbound only, no inbound — component? | B: Egress-Only Internet Gateway | ✅ | NAT = IPv4 only. Egress-only IGW = IPv6 one-way | — | Egress-Only IGW (IPv6) |
| 1569 | D3 | New Lambda SG, endpoint times out, first Lambda works — fix? | A: Add sg-new to endpoint inbound rules | ✅ | Endpoint SG must allow each caller's SG | — | Interface endpoint SG per-caller |
| 1570 | D3 | NF stateless vs stateful — evaluation order? | B: Stateless first, "forward" sends to stateful | ✅ | Stateless → forward → stateful. Pass = skip stateful. | — | NF stateless/stateful ordering |
| 1571 | D3 | Active C2 TCP connection, kill immediately — action? | B: NACL deny (stateless, kills tracked flows) | ✅ | SG removal won't kill established connections | — | NACL kills active connections |
| 1572 | D3 | Same-subnet lateral movement SMB — which log source? | B: VPC Flow Logs (ENI-level) | ✅ | TGW = cross-VPC only. VPC Flow = intra-VPC. | — | VPC Flow Logs scope |
| 1573 | D3 | Okta + CrowdStrike + no VPN + internal web app — service? | B: Verified Access (identity + device trust) | ✅ | Zero-trust per-app, no VPN client | — | Verified Access use case |
| 1574 | D3 | Same VPC, SG ref sg-B, communicate via public IP — result? | B: Fails — public IP via IGW, SG ref doesn't match | ✅ | Public IP = IGW = source is public IP, not SG | — | Public IP via IGW breaks SG refs |
| 1575 | D3 | Okta + CrowdStrike + no VPN + Finance group + internal app — service? | B: Verified Access | ✅ | Identity + device + group + no VPN = VA | — | Verified Access full stack |
| 1576 | D3 | Flow Logs inbound ACCEPT 443 + outbound REJECT ephemeral — cause? | B: NACL missing outbound ephemeral | ✅ | NACLs stateless, SGs never cause this | — | NACLs stateless |
| 1577 | D3 | DNS Firewall: ALLOW 2 + ALERT crypto + BLOCK * — priority order? | B: ALLOW(1,2) → ALERT(3) → BLOCK(4) | ✅ | First match wins, ALLOW specific first | — | DNS Firewall rule priority |

---


### Session N — YYYY-MM-DD

**Domains:** Dx · Dy
**Score:** X ✅ · Y ⚠️ · Z ❌ (N% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| | | | | | | — | |

After adding a session:
1. Update the Session Index table above
2. Update Quick Stats totals
3. Update Domain Breakdown counts
4. Move resolved weak areas out, add new ones

-->

### Session 116 — 2026-06-30

**Domains:** Cross-domain (Red-priority kill drill — novel angles, killer difficulty)
**Score:** 21 ✅ · 2 ⚠️ · 7 ❌ (62.5% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1578 | D1/D3 | DynamoDB anomalous access alert + prevent subsidiary KMS re-encrypt — which TWO? | B+D | ⚠️ | B: GuardDuty (alert) + SCP ViaService (prevent). D wrong: RCP wrong target (subsidiary is in-org + their key is their resource) | Q100, Q546 | Detect vs prevent (GuardDuty vs policy) |
| 1579 | D1/D3/D6 | State Manager 500 instances, 3 regions, OnBoot + 6hr, minimum associations — config? | C: ONE org-wide | ❌ | B: ONE per region (3 total). State Manager is regional, not org-wide. OnBoot + rate on single association. | Q1403, Q1048 | State Manager OnBoot + schedule (dual triggers) |
| 1580 | D1 | CT Lake EDS June 1 mgmt-only, query May AssumeRole + add data events June 15 query GetObject — THREE explanations? | A+C+D | ✅ | A: AssumeRole=mgmt event (only from June 1). C: No backfill. D: Data event ingestion starts from modification moment. | Q1440, Q951 | CloudTrail Lake (data vs mgmt + no backfill) |
| 1581 | D4/D6 | RCP denies non-org s3:*, Lambda writes own bucket + partner bucket + regulator bucket — which fail? | D: RCP blocks partner not govt | ❌ | C: RCP doesn't apply to external buckets (not your resource). Failures = missing cross-account perms or SCP. | Q683, Q698 | RCP scope (your resources only, not outbound) |
| 1582 | D1/D4/D5 | SCP blocks external, 10K denied attempts Day 1-2, SCP removed Day 3, 500 downloads — which THREE true? | A+D+B | ❌ | B+C+D: AA flags policy (static), GD no finding on denied (Day 1-2), GD fires on successful access (Day 3). | Q534, Q594 | GuardDuty ≠ failed attempts |
| 1583 | D3/D4/D5 | Gateway endpoint policy allows Get+Put+Query on Orders table, Scan + GSI Query fail — which TWO? | B+C | ✅ | B: Endpoint policy=allowlist (Scan not listed). C: GSI ARN doesn't match table ARN in endpoint policy. | Q535, Q1080 | Gateway endpoint policy as additional gate |
| 1584 | D4/D5/D6 | Cross-account role in Account A, session policy=GetObject only, SSE-KMS — succeeds? | B | ✅ | B: Server-side KMS not gated by session policy. S3 calls KMS internally. | Q591, Q679 | Session policy + server-side KMS |
| 1585 | D1/D2 | VPC Flow spike port 8443 beacon, GD zero findings, identify IPs 14d + correlate roles — tool? | B | ✅ | B: CW Logs Insights (no finding = no Detective). Separate CT Lake query for roles. | Q1277, Q1314 | Detective needs finding. No finding = CW Logs Insights |
| 1586 | D2/D1 | Trojan C2Activity, capture memory + disk + block C2 + remove from NLB — correct order? | C | ✅ | C: No-reboot AMI FIRST (memory), EBS snapshot (disk), deregister, deny-all SG. Standard AMI reboots = memory lost. | Q810, Q825, Q830 | No-reboot AMI for volatile memory |
| 1587 | D2/D4 | Identity Center federated session stolen, attacker created IAM user + keys + EC2 — FIRST action? | B: Delete IAM user | ❌ | D: Inline Deny-all on permission set role (blocks root attack vector first, then mop up IAM user). | Q862, Q867 | Credential leak IR (Deny-all before investigate) |
| 1588 | D6/D3 | Five enforcement layers, three developer actions (CLI CF, direct CLI, pipeline) — which layers fire? | A: cfn-guard fires on CLI CF | ❌ | E: cfn-guard=pipeline only, proactive+Hook=CF service-level, SCP=API level. CLI CF bypasses pipeline. | Q1387, Q1220, Q1271 | cfn-guard bypassable vs Config proactive service-level |
| 1589 | D3/D5 | Lambda GetRecords succeeds, kms:Decrypt times out, endpoint SG modified — cause? | B | ✅ | B: KMS endpoint SG inbound modified to restrict source. Lambda's ENI doesn't match. Timeout=network. | Q918, Q950 | Kinesis + KMS VPC endpoints (timeout = network) |
| 1590 | D5/D3 | EMR in-transit TLS handshake errors, Nitro C6i works fine, Private CA — TWO correct? | A+B | ✅ | A: Nitro unrelated (hardware-level). B: EMR expects PEM zip in S3, not ACM-managed cert directly. | Q1030, Q1073 | EMR in-transit = security config + PEM certs |
| 1591 | D6 | Security Hub setup: designate admin first, then enable SH — 0 members 0 findings — what's wrong? | A | ✅ | A: Must enable SH in management account FIRST (E-D-M-A). | Q1244, Q1273 | Security Hub setup ordering (E-D-M-A) |
| 1592 | D5/D4 | Three uploads: no flags + correct key + wrong key, default encryption + bucket policy + SCP — which succeed? | C | ✅ | A/C: Only Upload 2. Policies evaluate headers as-received before default encryption. | Q426, Q626, Q643 | Default encryption vs bucket policy Deny |
| 1593 | D5/D6 | Type 1: 7yr auto-delete. Type 2: permanent irreversible. Engineer swaps them — what's wrong? | D | ✅ | D: Both swapped. Object Lock Compliance = fixed period. Glacier Vault Lock = permanent policy. | Q800, Q822 | Glacier Vault Lock vs Object Lock |
| 1594 | D1/D4 | CISO asks 3 questions: who IS accessing + who COULD access + unused roles — match services? | B | ✅ | B: GuardDuty S3 (behavioral) + AA external (policy) + AA unused+policy gen. | Q187, Q233 | Detect vs prevent (GuardDuty vs Access Analyzer) |
| 1595 | D5/D6 | S3 access logging enabled, zero logs appear, ACLs disabled (BucketOwnerEnforced) — cause? | D: Missing GetBucketAcl | ❌ | B: S3 logging uses ACLs. ACLs disabled = logging can't work. Re-enable ACLs + grant log-delivery group. | Q864, Q868, Q903 | S3 server access logging = ACLs |
| 1596 | D5/D4 | IoT firmware signing offline verification + key rotation + non-repudiation — THREE correct? | A+C+F | ⚠️ | A+B+C: Symmetric=needs API (wrong for air-gapped) + shared secret=no non-repudiation + asymmetric sign/verify. | Q812, Q824 | Sign=private, verify=public |
| 1597 | D6/D3 | NF policy + DNS FW rules + WAF, "RAM for all three" — what's wrong? | B | ✅ | B: RAM shares NF+DNS FW but NOT WAF. FM creates WAF directly. DNS/NF = RAM+FM. WAF = FM only. | Q313, Q441, Q562 | RAM for sharing vs FM for enforcing |
| 1598 | D2 | Trojan C2Activity, capture memory+disk, instance removable — order? | A: Deny-all first | ❌ | B: No-reboot AMI FIRST (memory) → EBS → deregister → deny-all. Acquire before isolate. | Q810, Q825, Q830 | No-reboot AMI for volatile memory |
| 1599 | D3 | Flow Logs inbound ACCEPT + outbound REJECT ephemeral — cause? | B: NACL | ✅ | NACL stateless, needs explicit outbound ephemeral rule. SG stateful = never causes this. | Q707 | NACLs stateless |
| 1600 | D6 | SH enabled 200 accounts, 0 findings after 10min — cause? | B: 2-24hr latency | ✅ | Config evaluation at scale = hours not minutes. | Q1514 | Standards evaluation latency at scale |
| 1601 | D6 | WAF vs DNS FW — which needs RAM? | B: WAF=FM only, DNS FW=RAM+FM | ✅ | FM creates WAF directly. DNS FW rule groups shared via RAM. | Q313, Q441 | RAM for sharing vs FM for enforcing |
| 1602 | D6 | StackSets deployed Config, admin disables — what happens? | B: Nothing, no auto-remediation | ✅ | StackSets = deploy and forget. SCP prevents. | Q283, Q439 | StackSets no auto-remediation |
| 1603 | D1 | SOC searches Flow Logs for domain name, zero results — why? | B: Flow Logs = IP only, domains = Resolver | ✅ | VPC Flow Logs never contain domain names. | Q1276 | VPC Flow Logs = IPs only |
| 1604 | D1 | RCP blocks external, 5K denied, GD+AA enabled — which fires? | B: Only AA (static). GD silent. | ✅ | GD needs successful access. AA reads policy. | Q534, Q594 | GuardDuty ≠ failed attempts |
| 1605 | D1 | Detect kms:DisableKey 30s, org trail — approach? | B: EventBridge in mgmt account | ✅ | Specific API + fast = EventBridge. | Q474 | EventBridge for API call detection |
| 1606 | D2 | IAM user keys on GitHub, attacker created 2nd key + admin — FIRST action? | B: Inline Deny-all on user | ✅ | Blocks all paths (keys+console+sessions). | Q862, Q867 | Credential leak IR (Deny-all before investigate) |

---

### Session 4 — 2025-05-04

**Domains:** D3 Infrastructure Security (firewalls comparison)
**Score:** 8 ✅ · 1 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 26 | D3 | Lambda in private subnet making DNS queries to C2 domains — block immediately? | DNS Firewall | ✅ | DNS Firewall — block at DNS, connection never happens | — | DNS Firewall |
| 27 | D3 | ALB receiving credential-stuffing from single IP — block? | WAF | ✅ | WAF rate-based rules — single IP, not volumetric DDoS | — | WAF vs Shield |
| 28 | D3 | Detect malware signatures in egress traffic, have Suricata rules? | Network Firewall | ✅ | Network Firewall — Suricata = Network Firewall always | — | Network Firewall |
| 29 | D3 | SG opened to 0.0.0.0/0 in 150 accounts — auto-detect and fix org-wide? | Firewall Manager | ✅ | Firewall Manager SG audit policy — org-wide, auto-remediate | — | Firewall Manager |
| 30 | D3 | 40 Gbps UDP DDoS, bill spiking, want AWS to credit scaling costs? | Shield Advanced | ✅ | Shield Advanced — DDoS cost protection | — | Shield Advanced |
| 31 | D3 | EC2 needs to reach only api.stripe.com, cheapest layer to block? | DNS Firewall | ✅ | DNS Firewall — cheapest, block all except allowed domain | — | DNS Firewall |
| 32 | D3 | Ensure all 300 accounts have same WAF rules on ALBs, auto for new accounts? | Firewall Manager | ✅ | Firewall Manager WAF policy — org-wide, auto-applies | — | Firewall Manager |
| 33 | D3 | Data encoded in DNS subdomain queries (exfiltration) — block? | DNS Firewall | ✅ | DNS Firewall — exfil is in the query itself, block the domain | — | DNS Firewall |
| 34 | D3 | NACL allows inbound 443, SG allows 443, web server not responding? | Ephemeral ports | ⚠️ | NACL needs outbound ephemeral ports (1024-65535) — stateless, must allow response | — | NACLs stateless |
| 35 | D3 | Decrypt TLS traffic, inspect plaintext for malware, re-encrypt? | WAF Advanced | ❌ | **Network Firewall** — TLS inspection is Network Firewall only, WAF never decrypts | — | Network Firewall TLS inspection |


### Session 5 — 2025-05-05

**Domains:** D4 Identity & Access Management (re-test)
**Score:** 1 ✅ · 2 ⚠️ · 0 ❌ (33% correct, 100% partial+)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 36 | D4 | Dev puts Principal:* on bucket policy, external attacker reads objects. Block all external S3 access org-wide without modifying bucket policies — which policy type and why not SCP? | "SCP can't stop external accounts, RCP is the answer" + knew PrincipalIsAWSService condition | ✅ | RCP — evaluated on resource side regardless of caller. SCP only governs principals inside your org. Conditions: PrincipalOrgID + PrincipalIsAWSService:false with IfExists. | Q7 | Policy layers — RCP vs SCP |
| 37 | D4 | 300 customers need Decrypt on your KMS key, onboard/offboard weekly. Junior suggests RAM — why won't it work? | "Limitations maybe? KMS Grants is the answer" — didn't know RAM's service list excludes KMS | ⚠️ | RAM doesn't support KMS (infrastructure only: TGW, subnets, Route 53). Even if it did, RAM shares entire resource — Grants give per-operation control (Decrypt only). Key policy 32KB limit ~200 principals; Grants unlimited. | Q11 | RAM vs KMS Grants |
| 38 | D4 | One sentence each: what problem does RAM solve vs RCP? | "RAM shares resources between accounts. RCP manage control?" — RCP answer too vague | ⚠️ | RAM = OPENS access (share infrastructure cross-account). RCP = CLOSES access (deny external principals from data org-wide). Opposite problems, different service lists, zero overlap. | Q12 | RAM vs RCP |

### Session 6 — 2025-05-05

**Domains:** D4 Identity & Access Management (policy layers quiz)
**Score:** 3 ✅ · 0 ⚠️ · 2 ❌ (60% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 39 | D4 | SLR in Account A does PutObject, RCP denies non-org principals — does SLR succeed? | "Fails — RCP needs PrincipalIsAWSService rule" | ❌ | **Succeeds** — SLRs are completely exempt from RCPs (separate mechanism from PrincipalIsAWSService). | — | RCP exemptions (SLR vs service principal) |
| 40 | D4 | Role identity policy allows kms:Decrypt, boundary only allows s3:* and ec2:* — what happens? | "Denied — boundary doesn't include KMS" | ✅ | Denied. Permission boundary is a ceiling; kms:Decrypt outside boundary = blocked at Gate 3. | — | Permission boundary as ceiling |
| 41 | D4 | External Account B assumes role in Account A, role allows s3:GetObject, SCP allows all, no RCP — succeeds? | "Succeeds — evaluated against Account A's role policies" | ✅ | Succeeds. Once role is assumed, evaluation uses Account A's SCP + role's identity policy + boundary. | — | Cross-account evaluation |
| 42 | D4 | RCP denies kms:Decrypt for external principals. CloudTrail needs to decrypt — blocked? | "RCP doesn't support KMS?" | ❌ | **Succeeds** — RCP condition `PrincipalIsAWSService: false` doesn't match CloudTrail (it IS a service), so Deny doesn't fire. RCP does support KMS. | — | RCP exemptions (PrincipalIsAWSService) |
| 43 | D4 | Role: identity=Allow s3:*, boundary=Allow GetObject+ListBucket only. Calls PutObject? | "Denied — boundary limits" | ✅ | Denied. Boundary ceiling doesn't include PutObject. Gate 3 blocks. | — | Permission boundary as ceiling |

### Session 7 — 2025-05-05

**Domains:** D4 Identity & Access Management (rapid fire — post hyperfocus)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 44 | D4 | RCP denies s3:* for non-org. ELB SLR writes access logs to S3 — blocked? | "RCP can't block service-linked role" | ✅ | Allowed — SLRs are structurally exempt from RCPs | Q39 | RCP exemptions (SLR) |
| 45 | D4 | Identity allows s3:*, boundary allows s3:Get* only. Calls s3:DeleteObject? | "Permission boundary blocks it" | ✅ | Denied — Gate 3 (boundary) doesn't include DeleteObject | — | Permission boundary |
| 46 | D4 | 400 external accounts need Decrypt, key policy at 30KB — mechanism? | "KMS Grants" | ✅ | KMS Grants — key policy near 32KB limit, grants scale without policy edits | Q37 | KMS Grants |
| 47 | D4 | Role chaining A→B→C, Role C MaxSessionDuration=12hr — actual max? | "1 hour" | ✅ | 1 hour — role chaining always resets to 1hr max | — | Role chaining |
| 48 | D4 | External account calls s3:GetObject, bucket policy grants access, no RCP — need identity policy? | "No" | ✅ | No — resource-based policy alone grants cross-account (except KMS) | — | Cross-account evaluation |

### Session 8 — 2025-05-05

**Domains:** D4 Identity & Access Management (Week 1 final quiz — mixed Task 4.1 + 4.2)
**Score:** 9 ✅ · 1 ⚠️ · 0 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 49 | D4 | Developer creates role with AdministratorAccess — prevent escalation? | "SCP deny CreateRole without boundary" | ✅ | Permission boundary delegation pattern — iam:PermissionsBoundary condition | — | Permission boundaries |
| 50 | D4 | Block external S3 access org-wide even with Principal:* bucket policy? | "RCP" | ✅ | RCP — blocks external callers regardless of resource policy | — | RCP |
| 51 | D4 | Federated Okta user needs project-scoped S3 access without per-user policies? | "ABAC with ResourceTag = PrincipalTag" | ✅ | Session tags from IdP + ABAC: aws:ResourceTag/Project = ${aws:PrincipalTag/Project} | — | ABAC + session tags |
| 52 | D4 | Role chaining A→B→C, Role C MaxSessionDuration=12hr — actual max? | "1 hour" | ✅ | 1 hour — role chaining always resets | — | Role chaining |
| 53 | D4 | Cross-account KMS decrypt — minimum policies needed? | "Key policy + identity policy in Account B" | ⚠️ | Both sides must agree: key policy names Account B + Account B identity policy allows kms:Decrypt on key ARN. Got the concept, imprecise wording. | — | Cross-account KMS |
| 54 | D4 | Can GetCallerIdentity be denied by SCP? | "No" | ✅ | Cannot be denied by any policy — always works | — | STS |
| 55 | D4 | RCP denies kms:Decrypt with PrincipalIsAWSService:false. AWS Config decrypts? | "Allowed" | ✅ | Allowed — Config is AWS service principal, condition doesn't match, deny doesn't fire | Q42 | RCP exemptions |
| 56 | D4 | Identity allows ec2:*, boundary allows RunInstances+Describe only. TerminateInstances? | "Denied" | ✅ | Denied — Gate 3 boundary doesn't include TerminateInstances | — | Permission boundary |
| 57 | D4 | Share Transit Gateway with 30 dev accounts in org? | "RAM" | ✅ | RAM — infrastructure sharing within org, auto-accept | — | RAM |
| 58 | D4 | SCP denies s3:DeleteBucket. Role identity allows s3:*. DeleteBucket? | "Denied, Gate 1" | ✅ | Denied — SCP explicit deny always wins over identity policy Allow | — | SCP |

### Session 9 — 2025-05-08

**Domains:** D4 Identity & Access Management (Week 2 — cross-account, VP, STS)
**Score:** 3 ✅ · 0 ⚠️ · 2 ❌ (60% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 59 | D4 | Cross-account S3+KMS: bucket policy + identity policy correct, forgot KMS key policy — what error? | "403" | ✅ | Access Denied (403) — KMS decrypt fails as permission error | — | Cross-account KMS |
| 60 | D4 | Vendor needs to assume role in your account, prevent confused deputy — condition key? | "ExternalId" | ✅ | `sts:ExternalId` in trust policy condition | — | Confused deputy |
| 61 | D4 | SaaS app needs "Can user X edit doc Y in tenant Z?" at runtime — IAM or VP? | "Verified Permissions" | ✅ | Verified Permissions — app-level authz, not AWS API | — | Verified Permissions |
| 62 | D4 | Compromised role with active STS sessions — revoke immediately? | "You can't" | ❌ | **You CAN** — inline Deny with `aws:TokenIssueTime` < timestamp. Only way to revoke active tokens. | — | STS session revocation |
| 63 | D4 | Federated user from Okta, SAML assertion includes Project=Phoenix — what condition key evaluates this? | "equals?" (gave operator, not key) | ❌ | `aws:PrincipalTag/Project` — session tags from IdP land in PrincipalTag | — | Session tags + ABAC |

### Session 10 — 2025-05-08

**Domains:** D4 Identity & Access Management (Week 2 — Identity Center, session policies, VP, ABAC)
**Score:** 4 ✅ · 1 ⚠️ · 0 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 64 | D4 | Okta workforce SSO into 50 accounts with temp creds — which service? | "Identity Center" | ✅ | IAM Identity Center with external IdP (Okta via SAML 2.0) | — | Identity Center |
| 65 | D4 | Broad role, need narrow creds for downstream Lambda — mechanism? | "Session role" | ✅ | Session policy passed at AssumeRole time — filters down without new role | Q62 | Session policies |
| 66 | D4 | Multi-tenant SaaS "Can editor Bob update invoice-789 in tenant Acme?" — which service? | "Verified Permissions" | ✅ | Verified Permissions — app-level authz with Cedar policies | — | Verified Permissions |
| 67 | D4 | Employee signs in via Identity Center — what does permission set become? | "IAM role" | ✅ | IAM role auto-created in target account by Identity Center | — | Identity Center |
| 68 | D4 | Enforce CostCenter tag on all EC2 creation org-wide — where + condition key? | "In the caller, aws:RequestTag" | ⚠️ | **SCP** on org root with `Null: aws:RequestTag/CostCenter = true`. Got condition key right, but "in the caller" is vague — SCP is the org-wide enforcement point. | — | SCP + RequestTag enforcement |

### Session 11 — 2025-05-09

**Domains:** D4 Identity & Access Management (re-test — cross-account KMS, STS revocation, ABAC, RAM)
**Score:** 3 ✅ · 0 ⚠️ · 2 ❌ (60% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 69 | D4 | 50 customers/month need kms:Decrypt, grant/revoke without key policy edits? | B: KMS Grant per customer | ✅ | KMS Grants — one API call per onboard, RevokeGrant to offboard, no policy edits | Q37 | RAM vs KMS Grants |
| 70 | D4 | Cross-account KMS: key policy grants Account B root, identity policy correct, still AccessDenied? | C: Missing sts:AssumeRole | ❌ | **B: Account B's SCP denies kms:Decrypt** — Lambda doesn't AssumeRole, it calls directly. Caller's SCP applies. | Q53 | Cross-account KMS + SCP evaluation |
| 71 | D4 | Exfiltrated role credentials, active sessions making calls — revoke immediately? | B: Inline Deny with TokenIssueTime | ✅ | Inline Deny with `aws:TokenIssueTime` < current timestamp — only way to revoke active sessions | Q62 | STS session revocation |
| 72 | D4 | Okta team attribute → EC2 access by team tag, no per-team policies — which two? | D: RequestTag | ❌ | **A + C**: Map Okta attribute to session tag (A) + policy with `ec2:ResourceTag/Team = ${aws:PrincipalTag/Team}` (C). RequestTag is creation-time only. | Q63 | Session tags + ABAC (ResourceTag vs RequestTag) |
| 73 | D4 | Enforce CostCenter tag on all EC2 launches org-wide? | A: SCP Deny RunInstances if RequestTag missing | ✅ | SCP + `aws:RequestTag/CostCenter` with Null condition — org-wide preventive control | Q68 | SCP + RequestTag enforcement |

### Session 12 — 2025-05-09

**Domains:** D4 Identity & Access Management (Week 2 quiz — data perimeter, VP, boundaries, session policies)
**Score:** 4 ✅ · 0 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 74 | D4 | 80 accounts, block external S3 access org-wide, exempt AWS services — which two? | A+C: RCP + PrincipalIsAWSService condition | ✅ | RCP (not SCP) blocks external callers + PrincipalIsAWSService:false exempts AWS services | — | Data perimeter (RCP) |
| 75 | D4 | Multi-tenant SaaS "editors edit own tenant docs" — centralized authz? | B: Verified Permissions with Cedar | ✅ | VP + Cedar policies evaluating tenant claims from Cognito token | — | Verified Permissions |
| 76 | D4 | Boundary delegation + must tag with own team — how many Deny statements? | C: 4 | ✅ | 4: force boundary + force team tag + deny remove + deny swap | — | Permission boundaries + ABAC |
| 77 | D4 | RCP denies non-org KMS access, same-org Account B calls Decrypt — blocked? | B: No, PrincipalOrgID matches | ✅ | Same-org caller matches condition → Deny doesn't fire → allowed | — | RCP cross-account same-org |
| 78 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, session=GetObject+PutObject — DeleteObject? | A: Allowed (identity grants s3:*) | ❌ | **C: Denied — session policy only allows GetObject+PutObject.** Session policy is a ceiling like boundary. Effective = identity ∩ boundary ∩ session ∩ SCP. ALL must allow. | — | Session policy as ceiling |

---

### Session 13 — 2025-05-09

**Domains:** D4 Identity & Access Management (Week 2 final quiz — ABAC, boundaries, cross-account KMS, RCP, SCP bypass)
**Score:** 4 ✅ · 0 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 79 | D4 | Identity Center + Okta, engineers access EC2 by project tag, no per-engineer policies — approach? | B: Session tags + ABAC | ✅ | Session tags from SAML + ABAC matching PrincipalTag/Project to ResourceTag/Project | — | Session tags + ABAC |
| 80 | D4 | Boundary allows s3+ec2+logs, identity policy allows *, attempt kms:Encrypt? | B: Denied — boundary doesn't include kms | ✅ | Boundary is ceiling — effective = identity ∩ boundary. kms not in boundary = denied. | — | Permission boundary ceiling |
| 81 | D4 | Cross-account KMS: key policy grants Account B root, identity policy allows Decrypt, no SCP restriction — result? | B: Allowed — both sides satisfied | ✅ | Key policy (Account A) + identity policy (Account B) = both sides present = allowed | Q70 | Cross-account KMS + SCP evaluation |
| 82 | D4 | Block external principals from S3 org-wide even if bucket policy says Principal:* — solution? | B: RCP with PrincipalOrgID + PrincipalIsAWSService exception | ✅ | RCP blocks external callers that SCPs can't touch. SCP only governs your own principals. | — | RCP vs SCP for external callers |
| 83 | D4 | Lambda in Account B calls S3 in Account A, bucket policy names role ARN directly, Account B SCP denies s3:GetObject — succeeds? | A: Yes — resource-based policy bypasses SCP | ❌ | **B: No — SCP cannot be bypassed by anything.** The bypass rule applies to session policies and boundaries, NEVER SCPs. | — | SCP cannot be bypassed |

---

### Session 14 — 2025-05-09

**Domains:** D5 Data Protection · D3 Infrastructure Security (combined mini-exam)
**Score:** 2 ✅ · 0 ⚠️ · 3 ❌ (40% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 84 | D5 | DynamoDB Global Table + MRK, reads fail in eu-west-1 with AccessDenied on KMS — cause? | D: MRK needs a KMS Grant in eu-west-1 | ❌ | **B: MRK replica key policy doesn't allow DynamoDB.** MRK policies are independent per region — must update each separately. | — | MRK independent key policies |
| 85 | D5 | S3 objects immutable for 5 years, root can't delete — what combination? | C: Compliance mode + Legal Hold | ❌ | **B: Compliance mode + versioning.** Legal Hold = indefinite (no expiry). Compliance mode = fixed retention period. Don't mix them. | — | Object Lock Compliance vs Legal Hold |
| 86 | D5 | App in private subnet (no NAT) needs Secrets Manager — minimum infra? | B: Interface VPC endpoint + SG allowing HTTPS | ✅ | Interface endpoint (Gateway only for S3/DynamoDB). SG must allow 443. | — | VPC endpoints |
| 87 | D3 | Network Firewall TLS inspection — users get cert warnings — what's missing? | C: Network Firewall needs public ACM cert | ❌ | **A: Firewall's CA cert isn't trusted by clients.** TLS inspection = private CA + MITM. Must distribute CA to client trust stores. | Q35 | Network Firewall TLS inspection |
| 88 | D5 | Mask credit cards in CloudWatch Logs without code changes — Macie? | C: CloudWatch Logs data protection policy | ✅ | Macie = S3 only. CloudWatch Logs data protection = real-time masking in logs. | — | Data masking (new in C03) |


---

### Session 15 — 2025-05-13

**Domains:** D5 Data Protection · D3 Infrastructure Security (re-test)
**Score:** 3 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 89 | D3 | Network Firewall TLS inspection — users get cert warnings — root cause? | B: Firewall's CA cert isn't trusted by clients | ✅ | Private CA + MITM pattern — must distribute CA to client trust stores. | Q87 | Network Firewall TLS inspection |
| 90 | D5 | DynamoDB Global Table + MRK, reads fail in eu-west-1 with AccessDenied on KMS — cause? | B: Replica key policy doesn't grant DynamoDB permission | ✅ | MRK policies are independent per region — must update each separately. | Q84 | MRK independent key policies |
| 91 | D5 | S3 objects immutable for 5 years, root can't delete, auto-deletable after — config? | B: Compliance mode + versioning | ✅ | Compliance mode = fixed period, nobody can delete. Legal Hold = indefinite. Don't mix. | Q85 | Object Lock Compliance vs Legal Hold |


---

### Session 16 — 2025-05-13

**Domains:** D4 Identity & Access Management (Week 2 final quiz — SCP bypass, session policies, ABAC, cross-account KMS)
**Score:** 4 ✅ · 0 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 92 | D4 | Lambda in Account B calls S3 in Account A, bucket policy names role ARN, Account B SCP denies s3:GetObject — succeeds? | B: No — SCP cannot be bypassed | ✅ | SCP cannot be bypassed by anything — not resource-based policies, not direct ARN grants. | Q83 | SCP cannot be bypassed |
| 93 | D4 | Role identity=s3:*, no boundary, session policy=GetObject+PutObject only — DeleteObject? | B: Denied — session policy is ceiling | ✅ | Session policy is a ceiling like boundary. Effective = identity ∩ session ∩ boundary ∩ SCP. | Q78 | Session policy as ceiling |
| 94 | D4 | Okta Team=Platform attribute, restrict StartInstances/StopInstances to matching EC2 tag — condition? | B: ec2:ResourceTag/Team = ${aws:PrincipalTag/Team} | ✅ | ResourceTag for access control on existing resources. RequestTag for creation enforcement. | Q72 | Session tags + ABAC (ResourceTag vs RequestTag) |
| 95 | D4 | Cross-account KMS: key policy grants Account B root, identity policy correct, AccessDenied — cause? | B: Account B's SCP denies kms:Decrypt | ✅ | SCP follows the caller. Caller's SCP applies even when accessing another account's resources. | Q70 | Cross-account KMS + SCP evaluation |
| 96 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, session=GetObject+ListBucket, same-account bucket policy grants PutObject — PutObject? | A: Denied — session policy doesn't include PutObject | ❌ | **B: Allowed — resource-based policy naming the role directly bypasses session policy ceiling.** Session policy only filters identity-based grants. | — | Session policy bypass by resource-based policy |


---

### Session 17 — 2025-05-13

**Domains:** D4 Identity & Access Management · D1 Detection (re-test — SLR exemptions, session policy bypass, Security Hub)
**Score:** 3 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 97 | D4 | SCP denies s3:PutObject without Env tag. Config SLR writes snapshot (no tags) — succeeds? | Fails — SCP follows users | ✅ | Fails. SCP applies to SLRs — they're principals in your account. RCP exempts SLRs, SCP does not. | Q39 | RCP exemptions (SLR vs service principal) |
| 98 | D4 | Role identity=s3:*, session policy=GetObject only, same-account bucket policy grants role PutObject — PutObject? | Succeeds — resource-based policy bypasses session ceiling | ✅ | Resource-based policy naming the role directly bypasses session policy ceiling. Session policy only filters identity-based grants. | Q96 | Session policy bypass by resource-based policy |
| 99 | D1 | 200 accounts, detect public S3 buckets org-wide, least overhead — Config conformance pack vs Security Hub vs Macie vs Lambda? | B: Security Hub FSBP | ✅ | Security Hub FSBP — one-click org-wide, built-in S3 controls, dashboards. Less overhead than Config conformance pack. | Q24 | Security services comparison |


---

### Session 18 — 2025-05-13

**Domains:** D5 Data Protection (Week 3 mini-exam — KMS, S3 encryption, Secrets Manager, Object Lock)
**Score:** 4 ✅ · 1 ⚠️ · 0 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 100 | D5 | SSE-KMS buckets, detect external decryption — which service? | B: CloudTrail + key policy condition | ⚠️ | **C: GuardDuty S3 Protection** — "detect" = GuardDuty. Key policy condition prevents, doesn't detect. | — | Detect vs prevent (GuardDuty vs policy) |
| 101 | D5 | CreateGrant → partner gets AccessDenied immediately, works 30s later — fix? | B: Pass grant token | ✅ | Grant token for immediate use before eventual consistency. | — | KMS Grants eventual consistency |
| 102 | D5 | Key material never in AWS + native S3 SSE-KMS integration — which option? | B: XKS | ✅ | External key store — material outside AWS, still integrates via KMS API. | — | XKS |
| 103 | D5 | Global Table + MRK, reads fail in eu-west-1, primary key policy correct — cause? | B: Replica key policy missing DynamoDB access | ✅ | MRK policies are independent per region — must update each separately. | Q84 | MRK independent key policies |
| 104 | D5 | Secret rotated, open DB connection still works — why? | B: AWSPREVIOUS keeps old password valid | ✅ | Old password valid as AWSPREVIOUS until next rotation cycle. | — | Secrets Manager rotation |


---

### Session 19 — 2025-05-14

**Domains:** D1 Detection (re-test — detect vs prevent, security services comparison)
**Score:** 3 ✅ · 0 ⚠️ · 2 ❌ (60% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 105 | D1 | SSE-KMS buckets, CISO wants alerts when external accounts decrypt, least overhead? | A: CloudTrail data events + metric filter | ❌ | **C: GuardDuty S3 Protection** — "alert/detect" + "least overhead" = GuardDuty. CloudTrail filter works but heavy plumbing. | Q100 | Detect vs prevent (GuardDuty vs policy) |
| 106 | D1 | Lambda making DNS queries to known C2 domain — detect and generate finding, don't block yet? | A: DNS Firewall ALERT action | ❌ | **B: GuardDuty** — reads DNS logs as foundational source, has built-in C2 threat intel, generates findings automatically. DNS Firewall ALERT logs but doesn't produce security findings. | — | Detect C2 = GuardDuty (not DNS Firewall) |
| 107 | D1 | Confirmed C2 — block DNS resolution to that domain VPC-wide immediately? | C: DNS Firewall BLOCK | ✅ | DNS Firewall BLOCK — kills query at DNS, connection never happens, VPC-wide. | — | Block C2 = DNS Firewall |
| 108 | D1 | 300 accounts, dashboard for public S3 + unencrypted EBS + CIS compliance score, least overhead? | C: Security Hub with CIS benchmark | ✅ | Security Hub — aggregation + compliance dashboards + CIS benchmark built-in, one-click org-wide. | Q5 | Security services comparison |
| 109 | D1 | EC2 exfiltrating data at 3 AM — determine who launched it, role used, other resources accessed in 48hr? | C: Detective | ✅ | Detective — "investigate" / "determine scope" / "timeline" = always Detective. | — | Detective for investigation |


---

### Session 20 — 2025-05-15

**Domains:** Cross-domain practice exam (Week 11 — all domains)
**Score:** 7 ✅ · 2 ⚠️ · 1 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 110 | D4 | Identity Center permission set=s3:*+ec2:*, boundary=s3:* only — ec2:DescribeInstances? | Blocked | ✅ | Denied — boundary doesn't include ec2:*, effective = identity ∩ boundary. | — | Permission boundary as ceiling |
| 111 | D4 | Cross-account S3, bucket policy grants role ARN, Account B SCP denies s3:GetObject — succeeds? | Blocked | ✅ | Denied — SCP cannot be bypassed by anything. | Q83 | SCP cannot be bypassed |
| 112 | D3 | Inspect egress for malware (Suricata) + block C2 DNS — which TWO services? | Network Firewall + DNS Firewall | ✅ | Network Firewall (Suricata IPS) + DNS Firewall (block C2 domains). | — | Firewalls layered |
| 113 | D3 | Private subnet EC2 needs Secrets Manager, no NAT/IGW — minimum infra? | Interface endpoint + endpoint policy | ✅ | Interface VPC endpoint + SG allowing HTTPS (443). | — | VPC endpoints |
| 114 | D5 | Imported key material — how to rotate? | "Manual rotation" (no steps) | ⚠️ | Create NEW KMS key (origin=EXTERNAL) → import new material → update alias → old key stays for old ciphertext. | — | Imported key rotation procedure |
| 115 | D5 | CreateGrant → partner gets AccessDenied immediately, works 30s later — fix? | Pass grant token | ✅ | Pass grant token in subsequent API call for immediate use before eventual consistency. | Q101 | KMS Grants eventual consistency |
| 116 | D1 | Detect credentials used from Tor exit node — which service, zero custom code? | Didn't know | ❌ | **GuardDuty** — finding type UnauthorizedAccess:IAMUser/TorIPCaller. Built-in threat intel, zero setup. | — | GuardDuty finding types |
| 117 | D1 | Query CloudTrail across 50 accounts, SQL, near real-time, dashboards, no S3/Athena? | CloudTrail Lake | ✅ | CloudTrail Lake — managed, SQL, near real-time, cross-account, dashboards. | Q25 | CloudTrail Lake |
| 118 | D2 | EC2 communicating with C2 — first 3 IR steps? | Isolate (SG) → EBS snapshot + tag → stop | ✅ | Isolate (deny-all SG) → Snapshot (EBS forensic copy) → Tag → Investigate. Never terminate first. | — | IR sequence |
| 119 | D6 | Prevent disabling GuardDuty/CloudTrail/Flow Logs org-wide, auto for new accounts? | Control Tower | ⚠️ | **SCP** (Deny statements). Control Tower uses SCPs but the mechanism itself is SCP. | — | SCP for preventive guardrails |


---

### Session 21 — 2025-05-15

**Domains:** Cross-domain timed practice exam (Week 11 — all domains)
**Score:** 8 ✅ · 1 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 120 | D4 | SCP denies PutObject without Env tag, Config SLR writes snapshot (no tags) — succeeds? | Fail | ✅ | Fails — SCP applies to SLRs. RCP exempts SLRs, SCP does not. | Q97 | SCP applies to SLRs |
| 121 | D1 | Detect root access key creation in any member account, zero code? | GuardDuty | ✅ | GuardDuty — Policy:IAMUser/RootCredentialUsage. | — | GuardDuty finding types |
| 122 | D3 | Network Firewall TLS inspection — users get cert warnings — root cause? | Import private CA in browsers | ✅ | Firewall's CA cert not trusted by clients — distribute to trust stores. | Q87 | Network Firewall TLS inspection |
| 123 | D5 | Global Table + MRK, reads fail in eu-west-1, primary key policy correct — cause? | Key policies are independent | ✅ | MRK replica key policy missing DynamoDB permission. Must update each region. | Q84 | MRK independent key policies |
| 124 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, session=GetObject only — DeleteObject? | Denied | ✅ | Session policy ceiling — DeleteObject not in session = denied. | Q78 | Session policy as ceiling |
| 125 | D2 | After isolating compromised EC2 (deny-all SG), next step? | EBS snapshot + tag | ✅ | Snapshot EBS (forensic copy) + tag. Never terminate before preserving evidence. | — | IR sequence |
| 126 | D6 | Share DNS Firewall rule groups from security account to all members, auto for new accounts? | Control Tower | ❌ | **AWS RAM** — sharing resources cross-account = RAM. Control Tower manages guardrails, not resource sharing. | — | RAM for resource sharing |
| 127 | D5 | S3 immutable 7 years, root can't delete, auto-expire after — config? | Compliance mode Object Lock | ✅ | Compliance mode + versioning. Fixed retention, nobody deletes, auto-expires. | Q85 | Object Lock Compliance mode |
| 128 | D1 | Normalize CloudTrail + VPC Flow + GuardDuty + WAF into common schema, own S3 bucket? | Security Lake | ✅ | Security Lake — OCSF format, normalizes all sources, your S3 bucket. | — | Security Lake / OCSF |
| 129 | D3 | Lambda resolve only 2 domains, block all else — service + rule structure? | DNS Firewall + DENY rule | ⚠️ | DNS Firewall correct. Actions are ALLOW/BLOCK/ALERT (not Deny). Structure: ALLOW specific → BLOCK *. | — | DNS Firewall rule actions |


---

### Session 22 — 2025-05-15

**Domains:** Cross-domain timed practice exam (Week 11 — all domains, RAM/FM focus)
**Score:** 7 ✅ · 1 ⚠️ · 2 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 130 | D6 | 200 accounts, same WAF rules on all ALBs, auto-remediate — which service? | Firewall Manager | ✅ | Firewall Manager — "ensure/enforce" + auto-remediate = FM. | — | Firewall Manager vs RAM |
| 131 | D6 | Share Transit Gateway from networking account to dev OU — which service? | RAM | ✅ | RAM — "share" infrastructure cross-account = RAM. | — | RAM for resource sharing |
| 132 | D1 | Lambda connecting to botnet IP, want security finding auto-generated — which service? | Inspector | ❌ | **GuardDuty** — active threat (C2/botnet connection) = GuardDuty. Inspector = CVEs, not active threats. | — | GuardDuty vs Inspector |
| 133 | D4 | RCP denies s3:* for non-org, ELB SLR writes access logs — blocked? | No (SLR exempt from RCP) | ✅ | SLRs are structurally exempt from RCPs. | Q44 | RCP exemptions (SLR) |
| 134 | D3 | Block all DNS except 3 domains, ALERT on "crypto" queries — rule structure? | ALERT using DNS Firewall | ⚠️ | ALLOW 3 domains → ALERT *crypto* → BLOCK *. Need full structure with priorities. | — | DNS Firewall rule structure |
| 135 | D5 | AWS_KMS key, auto-rotation enabled, can old ciphertext still be decrypted? | Yes | ✅ | Yes — KMS keeps all old key material versions. Rotation doesn't break decryption. | — | KMS auto-rotation |
| 136 | D1 | IAM role used from unexpected country, visualize blast radius — which service? | Detective | ✅ | Detective — "visualize" / "blast radius" / "what else" = investigation. | — | Detective for investigation |
| 137 | D4 | Cross-account KMS: key policy grants B, identity policy allows, no SCP — result? | Succeeds | ✅ | Allowed — both sides satisfied, no SCP restriction. | Q81 | Cross-account KMS |
| 138 | D2 | Multi-step IR: isolate → snapshot → tag → notify — which service orchestrates? | Don't remember | ❌ | **Step Functions** — multi-step workflow orchestration. EventBridge triggers, Step Functions coordinates. | — | Step Functions for IR |
| 139 | D5 | After rotation, old DB connections still work — why? | AWSCURRENT and AWSPREVIOUS | ✅ | Old password valid as AWSPREVIOUS until next rotation cycle. | Q104 | Secrets Manager rotation |


---

### Session 23 — 2025-05-15

**Domains:** D1 Detection · D2 Incident Response (re-test — post-video drill)
**Score:** 8 ✅ · 1 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 140 | D1 | EC2 connecting to botnet IP, want finding auto-generated, zero code — which service? | GuardDuty | ✅ | GuardDuty — active threat = GuardDuty. Inspector = CVEs only. | Q132 | GuardDuty vs Inspector |
| 141 | D1 | "Which S3 buckets accessible by external accounts?" — which service? | IAM Access Analyzer | ✅ | IAM Access Analyzer (external access) — finds overly permissive resource policies. | — | Access Analyzer vs GuardDuty |
| 142 | D1 | GuardDuty finding type for credentials used from Tor exit node? | "TorIP" | ⚠️ | `UnauthorizedAccess:IAMUser/TorIPCaller` — pattern is ThreatPurpose:ResourceType/ThreatName. | Q116 | GuardDuty finding types |
| 143 | D1 | Compromised role, determine other resources accessed in 48hr, visualize blast radius? | Detective | ✅ | Detective — "visualize" / "blast radius" / "timeline" = always Detective. | Q109 | Detective for investigation |
| 144 | D1 | External access vs unused access in IAM Access Analyzer — one sentence each? | Confused the definitions | ❌ | External = "who outside can reach my resources?" Unused = "which permissions haven't been used in 90 days?" | — | Access Analyzer modes |
| 145 | D2 | Multi-step IR: isolate → snapshot → tag → notify — which service orchestrates? | Step Functions | ✅ | Step Functions — multi-step workflow orchestration. | Q138 | Step Functions for IR |
| 146 | D6 | Share DNS Firewall rule groups to all 200 member accounts — which service? | RAM | ✅ | RAM — sharing resources cross-account = RAM. | Q126 | RAM for resource sharing |
| 147 | D6 | Ensure all ALBs across 200 accounts have same WAF rules, auto-remediate — which service? | Firewall Manager | ✅ | Firewall Manager — "ensure/enforce" + auto-remediate = FM. | Q130 | Firewall Manager vs RAM |
| 148 | D2 | Before full IR, what should you do first with the GuardDuty finding? | "Evaluate" | ⚠️ | **Validate findings** — assess scope, check false positives, confirm severity. Exam keyword = "validate" or "triage". | — | Validate findings (Task 2.2.3) |
| 149 | D3 | Dedicated Direct Connect, Layer 2 encryption — which feature? | MACsec | ✅ | MACsec — Layer 2 encryption on dedicated DX only. | — | MACsec |


---

### Session 24 — 2025-05-16

**Domains:** Cross-domain (re-test — red-priority weak areas drill)
**Score:** 2 ✅ · 1 ⚠️ · 2 ❌ (40% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 150 | D1 | 200 accounts, dashboard: unencrypted S3/EBS + CIS score, least overhead? | Security Hub | ✅ | Security Hub — FSBP + CIS benchmark, org-wide, one-click. | Q108 | Security services comparison |
| 151 | D4 | 600 customers need kms:Decrypt, key policy at 28KB, onboard/offboard weekly? | KMS Grants | ✅ | KMS Grants — one API call per customer, no policy edits, scales without limit. | Q69 | RAM vs KMS Grants |
| 152 | D3 | Network Firewall TLS inspection — users get cert warnings — root cause? | "Import public CA in browser" | ⚠️ | Firewall's **private** CA cert not trusted by clients — distribute private CA to trust stores. Not a public cert — it's a MITM pattern with private CA. | Q122 | Network Firewall TLS inspection |
| 153 | D1 | SSE-KMS buckets, alert when external account decrypts, least overhead? | CloudTrail | ❌ | **GuardDuty S3 Protection** — "alert/detect" + "least overhead" = GuardDuty. CloudTrail is the log source, not the detection engine. | Q105 | Detect vs prevent (GuardDuty vs policy) |
| 154 | D1 | GuardDuty finding for credentials used from anonymizing proxy — finding type pattern? | Don't know | ❌ | `UnauthorizedAccess:IAMUser/TorIPCaller` — pattern: ThreatPurpose:ResourceType/ThreatName. | Q142 | GuardDuty finding types |


---

### Session 25 — 2025-05-16

**Domains:** D1 Detection (re-test — GuardDuty finding types + detect vs prevent drill)
**Score:** 2 ✅ · 0 ⚠️ · 3 ❌ (40% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 155 | D1 | GuardDuty finding type for EC2 mining Bitcoin? | "Mining:EC2/" | ❌ | `CryptoCurrency:EC2/BitcoinTool.B` — ThreatPurpose is CryptoCurrency, not Mining. | Q154 | GuardDuty finding types |
| 156 | D1 | SSE-KMS, want to KNOW when external account decrypts, least overhead — GuardDuty or CloudTrail? | CloudTrail | ❌ | **GuardDuty S3 Protection** — "detect/alert" + "least overhead" = GuardDuty. CloudTrail is the log source, not the detection engine. | Q153 | Detect vs prevent (GuardDuty vs policy) |
| 157 | D3 | Network Firewall TLS inspection CA cert — public, private, or self-signed? | Private | ✅ | Private CA cert — MITM pattern, distribute private CA to client trust stores. | Q152 | Network Firewall TLS inspection |
| 158 | D1 | Credentials used from unusual geographic location, notify, least overhead? | IAM Access Analyzer | ❌ | **GuardDuty** — active threat (unusual location) = GuardDuty. Access Analyzer finds misconfigurations, not real-time threats. | Q156 | Detect vs prevent (GuardDuty vs policy) |
| 159 | D1 | EC2 communicating with C2 server, alert with zero custom code? | GuardDuty | ✅ | GuardDuty — active threat + zero code = always GuardDuty. | Q140 | GuardDuty vs Inspector |


---

### Session 26 — 2025-05-16

**Domains:** Cross-domain exam-format practice (Week 11 — all domains)
**Score:** 17 ✅ · 0 ⚠️ · 3 ❌ (85% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 160 | D1 | 100 accounts SSE-KMS, alert external decryption, least overhead? | GuardDuty | ✅ | GuardDuty S3 Protection — detect + least overhead = GuardDuty. | Q156 | Detect vs prevent (GuardDuty vs policy) |
| 161 | D1 | GuardDuty finding type for EC2 mining cryptocurrency? | CryptoCurrency:EC2/something | ✅ | `CryptoCurrency:EC2/BitcoinTool.B` — ThreatPurpose correct. | Q155 | GuardDuty finding types |
| 162 | D1 | Credentials from Tor exit node — GuardDuty or Access Analyzer? | GuardDuty | ✅ | GuardDuty — active threat = always GuardDuty. | Q158 | Detect vs prevent (GuardDuty vs policy) |
| 163 | D4 | Block external S3 access org-wide without modifying bucket policies? | B: RCP | ✅ | RCP with PrincipalOrgID + PrincipalIsAWSService exception. | — | RCP for external access |
| 164 | D5 | Encrypt between EC2 (C6i), no code changes, least overhead? | C: Nitro | ✅ | Nitro inter-instance encryption — automatic, hardware-level. | — | Nitro encryption |
| 165 | D5 | Global Table + MRK, reads fail eu-west-1, primary key policy correct? | B: Replica key policy | ✅ | MRK policies independent per region — must update each. | Q123 | MRK independent key policies |
| 166 | D3 | Lambda private subnet, no NAT, needs Secrets Manager — minimum infra? (TWO) | B+D | ✅ | Interface VPC endpoint + SG allowing HTTPS 443. | — | VPC endpoints |
| 167 | D2 | EC2 communicating with C2, first action? | C: Deny-all SG | ✅ | Isolate first (deny-all SG) → snapshot → investigate. Never terminate. | — | IR sequence |
| 168 | D6 | 300 accounts, same WAF on all ALBs, auto-remediate, new accounts? | C: Firewall Manager | ✅ | Firewall Manager WAF policy — org-wide, auto-applies. | — | Firewall Manager |
| 169 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, session=Get+Put, bucket policy grants Delete — DeleteObject? | A: Denied | ❌ | **C: Allowed** — resource-based policy naming role directly bypasses session policy ceiling. | Q96 | Session policy bypass by resource-based policy |
| 170 | D1 | Normalize CloudTrail + VPC Flow + GuardDuty + third-party into single schema, own S3? | B: Security Lake | ✅ | Security Lake — OCSF format, your S3 bucket. | — | Security Lake / OCSF |
| 171 | D4 | SCP denies PutObject without Env tag, Config SLR writes snapshot (no tags)? | C: Fails | ✅ | SCP applies to SLRs — they're principals in your account. | Q120 | SCP applies to SLRs |
| 172 | D5 | Imported key material — how to rotate? | C: New key + import + alias | ✅ | Create new KMS key (EXTERNAL) → import → update alias. No auto-rotation. | Q114 | Imported key rotation |
| 173 | D4 | Compromised role, active sessions, revoke immediately? | B: Inline Deny TokenIssueTime | ✅ | Inline Deny with aws:TokenIssueTime < timestamp. Only way. | Q71 | STS session revocation |
| 174 | D4 | Okta Team attribute → EC2 access by team tag, no per-team policies? (TWO) | A+C | ✅ | Map attribute to session tag + ResourceTag condition. | Q94 | Session tags + ABAC |
| 175 | D5 | CreateGrant → partner AccessDenied immediately, works 30s later? | B: Grant token | ✅ | Pass grant token for immediate use before eventual consistency. | Q115 | KMS Grants eventual consistency |
| 176 | D4 | Third-party vendor assumes role, prevent confused deputy? | B: sts:ExternalId | ✅ | ExternalId in trust policy condition. | — | Confused deputy |
| 177 | D1 | Query CloudTrail 50 accounts, SQL, near real-time, dashboards, no S3/Athena? | B: CloudTrail Lake | ✅ | CloudTrail Lake — managed, SQL, near real-time, dashboards. | Q117 | CloudTrail Lake |
| 178 | D1 | EC2 querying DNS domains for Bitcoin mining pools — finding type? | D: Trojan | ❌ | **C: `Impact:EC2/BitcoinDomainRequest.Reputation`** — DNS query to crypto domain = Impact. Active mining = CryptoCurrency. | — | GuardDuty finding types (Impact vs CryptoCurrency) |
| 179 | D4 | Role in Account B, SCP denies GetObject, bucket policy in A grants role ARN — result? | B: Denied | ✅ | SCP cannot be bypassed by anything. | Q92 | SCP cannot be bypassed |
| 180 | D1 | Detect external S3 access (misconfig) + detect EC2 malicious IP (threat) — which TWO? | C+D | ✅ | Access Analyzer (misconfig) + GuardDuty (active threat). | — | Access Analyzer vs GuardDuty |
| 181 | D5 | Mask credit cards in CloudWatch Logs, no code changes, restrict who sees raw? | A: Macie | ❌ | **B: CloudWatch Logs data protection policy** + logs:Unmask. Macie = S3 only. | — | Data masking (Macie ≠ logs) |
| 182 | D3 | Dedicated Direct Connect, Layer 2 encryption? | B: MACsec | ✅ | MACsec — Layer 2 on dedicated DX only. | — | MACsec |


---

### Session 27 — 2025-05-16

**Domains:** Cross-domain exam-format practice (Week 11 — hardest topics)
**Score:** 19 ✅ · 0 ⚠️ · 5 ❌ (79% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 183 | D4 | RCP denies s3:* for non-org, ELB SLR writes access logs — blocked? | A: Denied | ❌ | **B: Allowed** — SLRs are structurally exempt from RCPs. | Q133 | RCP exemptions (SLR) |
| 184 | D4 | Validate policy for security issues BEFORE deploying — which service? | A: Policy Simulator | ❌ | **B: Access Analyzer policy validation** — pre-deployment check. Simulator tests existing policies. | — | Access Analyzer policy validation vs Simulator |
| 185 | D3 | EC2 private subnet needs S3 + DynamoDB, no internet — endpoint types? (TWO) | B+D | ✅ | Gateway endpoints for both (S3 + DynamoDB = only two Gateway endpoint services). | — | Gateway vs Interface endpoints |
| 186 | D5 | Secret rotated, open DB connections still work — why? | B: AWSPREVIOUS | ✅ | Old password valid as AWSPREVIOUS until next rotation cycle. | Q104 | Secrets Manager rotation |
| 187 | D1 | Role used from never-seen IP, zero code — which service? | B: Access Analyzer | ❌ | **C: GuardDuty** — unusual behavior happening NOW = active threat = GuardDuty. | Q158 | Detect vs prevent (GuardDuty vs Access Analyzer) |
| 188 | D5 | S3 immutable 3 years, root can't delete, auto-expire after? | B: Compliance mode | ✅ | Compliance mode + fixed retention. Nobody deletes, auto-expires. | Q91 | Object Lock Compliance mode |
| 189 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, attempt kms:Encrypt? | B: Denied — boundary | ✅ | Boundary ceiling doesn't include kms:* = denied at Gate 3. | — | Permission boundary ceiling |
| 190 | D1 | GuardDuty finding Policy:IAMUser/RootCredentialUsage — what happened? | B: Root API call | ✅ | Root account made an API call. Policy = risky config/usage. | — | GuardDuty finding types |
| 191 | D6 | Prevent disabling GuardDuty/CloudTrail/Flow Logs org-wide? | B: SCP Deny | ✅ | SCP with explicit Deny on disable actions. | Q119 | SCP for preventive guardrails |
| 192 | D5 | KMS auto-rotation: how long are old key material versions kept? | C: 90 days | ❌ | **B: Forever** — KMS keeps all versions until key deleted. No expiry. | — | KMS auto-rotation retention |
| 193 | D4 | RCP denies s3:* non-org, ELB SLR writes — blocked? (re-test) | Allowed | ✅ | SLRs structurally exempt from RCPs. | Q183 | RCP exemptions (SLR) |
| 194 | D4 | Validate policy before deploying — which service? (re-test) | Access Analyzer | ✅ | Access Analyzer policy validation = pre-deployment. | Q184 | Access Analyzer validation |
| 195 | D1 | Role from unusual IP, zero code — which service? (re-test) | GuardDuty | ✅ | Active threat = GuardDuty. | Q187 | Detect vs prevent |
| 196 | D5 | KMS auto-rotation: how long kept? (re-test) | Forever | ✅ | No expiration. All versions kept until key deleted. | Q192 | KMS auto-rotation retention |
| 197 | D4 | Cross-account KMS: key policy grants B root, identity allows, no SCP — result? | B: Allowed | ✅ | Both sides satisfied, no SCP restriction. | Q81 | Cross-account KMS |
| 198 | D4 | SCP denies RunInstances without CostCenter tag, dev launches without tag? | B: Denied | ✅ | SCP explicit Deny wins over identity Allow. | Q73 | SCP + RequestTag enforcement |
| 199 | D5 | Mask SSNs in CW Logs, no code changes, restrict raw access? (TWO) | B+C | ✅ | CW Logs data protection + logs:Unmask for authorized users. | — | Data masking |
| 200 | D4 | Session=GetObject only, cross-account bucket policy grants session PutObject — result? | B: Allowed | ✅ | Resource-based policy naming session bypasses session policy ceiling. | Q169 | Session policy bypass |
| 201 | D1 | Exfiltration:S3/AnomalousBehavior — what does it indicate? | B: Unusual data transfer | ✅ | Unusual data transfer pattern suggesting exfiltration. | — | GuardDuty finding types |
| 202 | D3 | Dedicated DX, encryption without latency? | B: MACsec | ✅ | MACsec — Layer 2, line-rate, dedicated only. | — | MACsec |
| 203 | D5 | CMK scheduled for deletion, discovered 3 days later — what to do? | B: CancelKeyDeletion | ✅ | CancelKeyDeletion → key moves to Disabled. Must re-enable. | — | KMS key deletion |
| 204 | D3 | Block C2 domain resolution VPC-wide immediately? | C: DNS Firewall BLOCK | ✅ | DNS Firewall BLOCK — kills query at DNS, VPC-wide. | — | DNS Firewall |
| 205 | D1 | Access Analyzer finds external SQS access + GuardDuty enabled — what does each tell you? | B: AA=misconfig, GD=active threat | ✅ | AA = "exposed". GD = "being exploited". Complementary. | — | Access Analyzer vs GuardDuty |
| 206 | D5 | Lambda has kms:GenerateDataKey in identity policy, key policy grants account root — succeeds? | C: Needs kms:Encrypt | ❌ | **B: Allowed** — root in key policy enables IAM delegation. GenerateDataKey IS correct for S3 envelope encryption. | — | KMS key policy delegation + GenerateDataKey |


---

### Session 28 — 2025-05-16

**Domains:** Cross-domain exam-format practice (Week 11 — mixed, targeting remaining gaps)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 207 | D4 | RCP denies kms:Decrypt non-org + PrincipalIsAWSService:false. CloudTrail decrypts — blocked? | B: Allowed | ✅ | CloudTrail IS an AWS service → condition doesn't match → Deny doesn't fire. | Q42 | RCP exemptions (PrincipalIsAWSService) |
| 208 | D3 | SG opened to 0.0.0.0/0 across 200 accounts, auto-detect + revert — which service? | A: GuardDuty | ❌ | **C: Firewall Manager SG audit policy** — misconfig + org-wide + auto-remediate = FM. GuardDuty detects threats, not misconfigs. | — | Firewall Manager SG audit |
| 209 | D3 | DNS Firewall: allow only 2 domains, block all else — rule structure? | B: ALLOW specific → BLOCK * | ✅ | ALLOW domains first (lowest priority number) → BLOCK * last. First match wins. | Q129 | DNS Firewall rule structure |
| 210 | D4 | Identity Center employee selects permission set — what does it become? | B: IAM role | ✅ | Permission set = IAM role auto-created in target account. | — | Identity Center |
| 211 | D5 | Lambda uploads to S3 with SSE-KMS — which KMS permission needed? | C+A | ✅ | **C only: kms:GenerateDataKey** — S3 uses envelope encryption. kms:Encrypt is for direct <4KB. | Q206 | KMS GenerateDataKey for S3 |
| 212 | D4 | Role chaining A→B→C, Role C MaxSessionDuration=12hr — actual max? | B: 1 hour | ✅ | Role chaining always resets to 1hr max. | — | Role chaining |
| 213 | D1 | GuardDuty Runtime Monitoring for EKS — what extra component needed? | B: Security agent | ✅ | Runtime Monitoring = only GuardDuty feature needing an agent. | — | GuardDuty Runtime Monitoring |
| 214 | D4 | Prevent CreateRole without boundary, org-wide? | B: SCP + iam:PermissionsBoundary | ✅ | SCP delegation pattern — force boundary on all role creation. | — | SCP + boundary delegation |
| 215 | D1 | CloudTrail log file modified — how detected? | C: Digest files + SHA-256 | ✅ | Log file integrity validation — digest files, validate via CLI. | — | CloudTrail integrity |
| 216 | D4 | "Can editor Bob update invoice-789 in tenant Acme?" — which service? | B: Verified Permissions | ✅ | VP + Cedar — app-level authz, not AWS API. | — | Verified Permissions |


---

### Session 29 — 2025-05-16

**Domains:** Cross-domain exam-format practice (Week 11 — final killer set, all weak spots)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 217 | D4 | RCP denies s3:* non-org. Config SLR writes + CloudTrail writes — which succeed? | A: Both | ✅ | Both — SLR exempt (structural) + CloudTrail exempt (PrincipalIsAWSService). Two different mechanisms. | Q183, Q207 | RCP exemptions (both paths) |
| 218 | D1 | EC2 actively sending traffic to Bitcoin mining pool — finding type? | B: CryptoCurrency:EC2/BitcoinTool.B | ✅ | Active mining = CryptoCurrency. DNS query only = Impact. | Q178 | GuardDuty finding types |
| 219 | D4 | Check new policy for security issues BEFORE attaching — which tool? | B: Access Analyzer validation | ✅ | Pre-deployment = Access Analyzer policy validation. Simulator = test existing. | Q184 | Access Analyzer validation |
| 220 | D5 | Mask PHI in CW Logs, only compliance officer sees raw — which TWO? | B+C | ✅ | CW Logs data protection + deny logs:Unmask broadly. | Q181 | Data masking |
| 221 | D4 | Session=GetObject only, bucket policy grants role PutObject — result? | B: Allowed | ✅ | Resource-based policy naming role bypasses session policy ceiling. | Q169, Q200 | Session policy bypass |
| 222 | D4 | SCP denies GetObject, bucket policy in Account A grants role ARN — result? | B: Denied | ✅ | SCP cannot be bypassed by anything. | Q179 | SCP cannot be bypassed |
| 223 | D5 | KMS rotated 3 times, decrypt data from original material 3 years ago? | B: Succeeds forever | ✅ | All versions kept forever, auto-routes via ciphertext metadata. | Q192 | KMS auto-rotation retention |
| 224 | D3/D1 | Detect overly permissive SGs + detect malicious IP comms — which TWO? | C+D | ✅ | FM SG audit (misconfig) + GuardDuty (active threat). | Q208 | FM vs GuardDuty |
| 225 | D5 | Key policy grants root only, Lambda identity has GenerateDataKey — succeeds? | B: Allowed | ✅ | Root = IAM delegation enabled. Identity policy grants the action. | Q206 | KMS key policy delegation |
| 226 | D1 | EC2 queries DNS for crypto domain, no connection yet — finding type? | D: Discovery | ❌ | **B: `Impact:EC2/BitcoinDomainRequest.Reputation`** — DNS query to crypto domain = Impact. Active mining = CryptoCurrency. Discovery = resource enumeration. | Q178 | GuardDuty finding types (Impact vs CryptoCurrency) |


---

### Session 30 — 2025-05-17

**Domains:** Cross-domain (re-test — red-priority gaps: Impact vs CryptoCurrency, session policy bypass)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 227 | D1 | EC2 DNS queries to pool.minergate.com, no TCP connection yet — ThreatPurpose? | Impact | ✅ | Impact — DNS query only = Impact. Active mining = CryptoCurrency. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 228 | D1 | EC2 actively sending traffic TO mining pool (connection established) — ThreatPurpose? | CryptoCurrency | ✅ | CryptoCurrency:EC2/BitcoinTool.B — active mining traffic. | Q218 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 229 | D4 | Identity=s3:*, session=GetObject only, same-account bucket policy grants role DeleteObject — succeeds? | Yes | ✅ | Resource-based policy naming role bypasses session policy ceiling. | Q169, Q221 | Session policy bypass by resource-based policy |
| 230 | D4 | Same as Q229 but caller's SCP denies DeleteObject — succeeds? | No | ✅ | SCP cannot be bypassed by anything. | Q222 | SCP cannot be bypassed |
| 231 | D1 | EC2 queries DNS for known botnet C2 domain, no connection — ThreatPurpose? | Impact | ✅ | DNS query only = Impact. Active C2 communication = Trojan. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |


---

### Session 31 — 2025-05-17

**Domains:** D1 Detection + Cross-domain (Week 11 — D1 focus, targeting 62% domain)
**Score:** 7 ✅ · 0 ⚠️ · 3 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 232 | D1 | GuardDuty enabled via delegated admin, one account has no findings despite production workloads — cause? | C: VPC Flow Logs not enabled | ❌ | **D: Workloads in a region where GuardDuty not enabled.** GuardDuty is regional. It reads VPC Flow Logs via internal feed — no need to enable them yourself. | — | GuardDuty is regional + agentless |
| 233 | D1 | Detect credentials used from never-seen IP, zero custom code — which service? | A: Access Analyzer | ❌ | **C: GuardDuty** — unusual IP = active threat happening NOW = GuardDuty. Access Analyzer = permission audit, not real-time threats. | Q187 | Detect vs prevent (GuardDuty vs Access Analyzer) |
| 234 | D1 | CloudTrail Lake vs Security Lake — how do they store data? | B: CT Lake managed, Security Lake your S3 | ✅ | CloudTrail Lake = managed data store. Security Lake = your S3 bucket (Iceberg/Parquet/OCSF). | — | CloudTrail Lake vs Security Lake |
| 235 | D2 | GuardDuty severity 8.5, EC2 communicating with C2 — first action? | C: Deny-all SG | ✅ | Isolate first (deny-all SG) → snapshot → investigate. Never terminate. | — | IR sequence |
| 236 | D1 | Query VPC Flow Logs in CloudWatch for top data sender — most efficient? | D: Detective | ❌ | **B: CloudWatch Logs Insights** — data already in CW, arbitrary aggregation query, no extra setup. Detective = investigate from a finding/entity, not open-ended queries. | — | CloudWatch Logs Insights vs Detective |
| 237 | D1/D6 | S3 logging enforcement across 300 accounts, auto-remediate within 1hr — which TWO? | A+D | ✅ | Config managed rule + auto-remediation (A) + organizational rule from delegated admin (D). | — | Config org rules + auto-remediation |
| 238 | D1 | EC2 private subnet, VPC Flow Logs not appearing in CloudWatch, CW agent installed — cause? | A: Flow log pointing to S3 | ✅ | VPC Flow Logs are VPC-level, don't use CW agent. Configuration determines destination. | — | VPC Flow Logs ≠ CW agent |
| 239 | D1/D2 | GuardDuty Recon finding, want to know what else attacker IP touched in 48hr — which service? | B: Detective | ✅ | Detective = "what else" / "blast radius" / "timeline". | — | Detective for investigation |
| 240 | D1/D4 | GuardDuty S3 Protection + RCP denying non-org, external attacker tries to read — what happens? | A: Both act | ✅ | RCP blocks access + GuardDuty detects the attempt. Independent services. | — | RCP + GuardDuty complementary |
| 241 | D1 | Detect CloudTrail StopLogging org-wide within 5 min, minimal setup — approach? | C: Org trail + EventBridge in mgmt account | ✅ | Organization trail + one EventBridge rule in management account. Detect ≠ prevent. | — | Org trail + EventBridge detection |


---

### Session 32 — 2025-05-17

**Domains:** Cross-domain exam-format practice (Week 11 — mixed, all domains)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 246 | D5 | Lambda uploads to S3 with SSE-KMS — which KMS permission? | C: kms:GenerateDataKey | ✅ | S3 envelope encryption = GenerateDataKey for uploads. kms:Encrypt is for direct <4KB. | — | KMS GenerateDataKey for S3 |
| 247 | D5 | KMS key scheduled for deletion 5 days ago, 30-day wait — recover? | B: CancelKeyDeletion → Disabled | ✅ | CancelKeyDeletion → key moves to Disabled. Must re-enable manually. | — | KMS key deletion recovery |
| 248 | D5/D6 | Prevent S3 buckets without encryption org-wide — approach? | D: Config rule + auto-remediation | ✅ | CreateBucket API doesn't have encryption settings — must detect and fix after. | — | Config auto-remediation |
| 249 | D3 | EC2 private subnet needs S3 + DynamoDB, minimize cost — endpoint types? | B+D: Gateway for both | ✅ | S3 and DynamoDB = only two Gateway endpoint services (free). | — | Gateway vs Interface endpoints |
| 250 | D2 | Access keys leaked to GitHub — correct response sequence? | B: Deactivate → CloudTrail → new key → delete old | ✅ | Stop bleeding first, then investigate, then replace. | — | Credential leak IR |
| 251 | D6 | Control Tower prevent disabling GuardDuty — which mechanism? | A: Config rule | ❌ | **B: SCP** — "prevent" = preventive control = SCP. Config = detective (detect after). Control Tower uses SCPs for preventive guardrails. | — | SCP for preventive guardrails (Control Tower) |
| 252 | D4 | RCP denies s3:* non-org, Config SLR writes snapshot — succeeds? | A: Yes — SLR exempt | ✅ | SLRs structurally exempt from RCPs. | Q183 | RCP exemptions (SLR) |
| 253 | D4 | Validate policy for security issues BEFORE deploying — which tool? | B: Access Analyzer validation | ✅ | Pre-deployment = Access Analyzer policy validation. Simulator = test existing. | Q184 | Access Analyzer policy validation |
| 254 | D5 | Secret rotated, old DB connection still works — why? | B: AWSPREVIOUS | ✅ | Old password valid as AWSPREVIOUS until next rotation cycle. | — | Secrets Manager rotation |
| 255 | D5 | Encrypt between C6i instances, zero config — mechanism? | C: Nitro | ✅ | C6i = Nitro-based. Automatic hardware-level encryption. | — | Nitro inter-instance encryption |


---

### Session 33 — 2025-05-17

**Domains:** Cross-domain exam-format practice (Week 11 — harder scenarios, multi-concept)
**Score:** 5 ✅ · 0 ⚠️ · 5 ❌ (50% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 256 | D4/D5 | Cross-account Lambda → S3+KMS, all policies correct, still AccessDenied — cause? | A: Missing sts:AssumeRole | ❌ | **C: Caller's SCP denies kms:Decrypt.** SCP follows the caller even when accessing another account's resources. AssumeRole already succeeded (error is on S3/KMS call). | Q70 | Cross-account KMS + SCP evaluation |
| 257 | D4 | Developers need CreateRole but can't escalate beyond s3+ec2 — mechanism? | B: SCP requiring PermissionsBoundary | ✅ | SCP forces boundary on all CreateRole calls. Boundary caps effective permissions. | — | Permission boundary delegation |
| 258 | D5 | DB credentials available in DR region if primary fails — which feature? | A: KMS MRK | ❌ | **B: Secrets Manager cross-region replication.** MRK replicates key material, not the secret itself. | — | Secrets Manager cross-region replication |
| 259 | D1 | Suspect CloudTrail log file modified — how to verify integrity? | B: Digest files + AWS CLI | ✅ | CloudTrail digest files with SHA-256 hashes, validate via CLI. | — | CloudTrail integrity validation |
| 260 | D5 | S3 immutable 7 years, root can't delete, auto-expire — config? | B: Compliance mode | ✅ | Compliance mode = fixed period, nobody deletes, auto-expires. | — | Object Lock Compliance mode |
| 261 | D3/D4 | Enforce IMDSv2 org-wide, prevent non-compliant launches — approach? | B: Config + auto-remediation | ❌ | **A: SCP denying RunInstances unless MetadataHttpTokens=required.** "Prevent" + "org-wide" = SCP. Config = detect and fix after. | Q251 | SCP for preventive enforcement |
| 262 | D3 | Lambda private subnet, no NAT, needs Secrets Manager — which TWO? | B+C | ✅ | Interface endpoint + SG allowing outbound HTTPS 443. | — | VPC endpoints + security groups |
| 263 | D4 | Identity Center + Okta + SCIM, new engineer joins Platform group — what happens? | C: Manual assignment needed | ❌ | **B: SCIM auto-syncs user + group membership.** Group already assigned to permission set → new user inherits access automatically. | — | SCIM provisioning (Identity Center) |
| 264 | D5 | Key policy grants root only, engineer has s3:GetObject but no KMS perms — can they read? | C: Yes, root delegates to all | ❌ | **B: No — root enables IAM delegation but doesn't grant access.** Each principal still needs explicit kms:Decrypt in their identity policy. | Q206 | KMS key policy root = delegation, not grant |
| 265 | D4 | Multi-tenant DynamoDB, restrict users to own tenant rows, no per-tenant policies? | C: dynamodb:LeadingKeys + PrincipalTag | ✅ | ABAC with LeadingKeys condition matching caller's TenantId tag. | — | ABAC for DynamoDB multi-tenant |


---

### Session 34 — 2025-05-18

**Domains:** Cross-domain (re-test — Session 33 errors)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 266 | D4/D5 | Cross-account Lambda → S3+KMS, all correct, AccessDenied — cause? | B: Account B's SCP denies kms:Decrypt | ✅ | SCP follows the caller even when accessing another account's resources. | Q256 | Cross-account KMS + SCP evaluation |
| 267 | D5 | DB credentials available in DR region if primary fails — which feature? | B: Secrets Manager cross-region replication | ✅ | MRK replicates key material, not the secret itself. Secrets Manager replication replicates the secret. | Q258 | Secrets Manager cross-region replication |
| 268 | D3/D4 | Enforce IMDSv2 org-wide, prevent non-compliant launches — approach? | B: SCP denying RunInstances unless MetadataHttpTokens=required | ✅ | "Prevent" + "org-wide" = SCP. Config = detect and fix after. | Q261 | SCP for preventive enforcement |
| 269 | D4 | Identity Center + Okta + SCIM, new engineer joins Platform group — what happens? | B: SCIM auto-syncs user + group membership | ✅ | Group already assigned to permission set → new user inherits access automatically. | Q263 | SCIM provisioning (Identity Center) |
| 270 | D5 | Key policy grants root only, engineer has s3:GetObject but no KMS perms — can they read? | B: Fails — root enables delegation but doesn't grant | ✅ | Root in key policy enables IAM delegation. Each principal still needs explicit kms:Decrypt. | Q264 | KMS key policy root = delegation, not grant |


---

### Session 35 — 2025-05-18

**Domains:** D6 Governance (untested gaps — StackSets, Audit Manager, Artifact, Service Catalog, Conformance Packs)
**Score:** 2 ✅ · 0 ⚠️ · 3 ❌ (40% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 271 | D6 | HIPAA compliance, auto-collect evidence, generate report for auditor? | D: Artifact | ❌ | **B: Audit Manager** — collects YOUR evidence (Config, CloudTrail, Security Hub) and generates YOUR audit report. Artifact = AWS's compliance paperwork. | — | Audit Manager vs Artifact |
| 272 | D6 | Auditor needs AWS's PCI DSS Attestation of Compliance — where? | B: Artifact | ✅ | Artifact = download AWS's compliance reports/certificates. | — | AWS Artifact |
| 273 | D6 | Deploy GuardDuty + Config + CloudTrail across 150 accounts, auto for new accounts? | A: Firewall Manager | ❌ | **B: StackSets (service-managed, auto-deploy)** — FM only deploys firewall rules. StackSets deploys any resource. | — | StackSets vs Firewall Manager |
| 274 | D6 | Self-service S3/EC2 with encryption+logging baked in, devs don't need broad IAM? | C: StackSets | ❌ | **B: Service Catalog with launch role** — self-service = users pull. StackSets = admin pushes. Launch role means dev doesn't need resource permissions. | — | Service Catalog (self-service) |
| 275 | D6 | 30 Config rules as single unit + auto-remediation + org-wide from delegated admin? | D: Firewall Manager | ❌ | **B: Config conformance pack (organizational)** — bundle of rules + remediation as one unit. FM doesn't deploy Config rules. | — | Config conformance packs |


---

### Session 36 — 2025-05-18

**Domains:** D6 Governance (re-test — StackSets, Service Catalog, Audit Manager, Artifact, Conformance Packs)
**Score:** 3 ✅ · 0 ⚠️ · 2 ❌ (60% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 276 | D6 | Deploy GuardDuty + Config + CloudTrail across 200 accounts, auto for new accounts? | D: Conformance pack | ❌ | **B: StackSets (service-managed, auto-deploy)** — conformance packs deploy Config RULES, not enable services. StackSets deploys any resource. | Q273 | StackSets vs Conformance Pack |
| 277 | D6 | Self-service hardened EC2/S3, devs don't need broad IAM (ec2:RunInstances, s3:CreateBucket)? | D: SCP | ❌ | **B: Service Catalog with launch constraint** — SCP restricts, doesn't enable. Launch constraint lets Service Catalog assume a role with the permissions. | Q274 | Service Catalog (self-service) |
| 278 | D6 | Evidence that S3 encrypted + CloudTrail enabled, mapped to SOC 2 framework, generate report? | C: Audit Manager | ✅ | Audit Manager — collects YOUR evidence, maps to frameworks, generates YOUR report. | Q271 | Audit Manager vs Artifact |
| 279 | D6 | Proof that AWS infrastructure meets PCI DSS — where to get? | B: Artifact | ✅ | Artifact = download AWS's compliance reports/certificates. | Q272 | AWS Artifact |
| 280 | D6 | 25 Config rules + auto-remediation + single package + org-wide from delegated admin? | C: Organizational conformance pack | ✅ | Conformance pack = bundle of rules + remediation as one unit, org-wide. | Q275 | Config conformance packs |


---

### Session 37 — 2025-05-18

**Domains:** D6 Governance + D3/D4 (untested topics) + D1 Detection (retention check)
**Score:** 10 ✅ · 0 ⚠️ · 3 ❌ (77% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 281 | D6 | Deploy GuardDuty + Config + CloudTrail across 200 accounts, auto for new accounts? | C: StackSets | ✅ | StackSets (service-managed, auto-deploy) — deploys any resource. | Q276 | StackSets vs Conformance Pack |
| 282 | D6 | Junior dev needs VPC but only has servicecatalog:ProvisionProduct — how? | C: Service Catalog assumes launch role | ✅ | Launch constraint lets Service Catalog assume a role with the permissions. | Q277 | Service Catalog (self-service) |
| 283 | D6 | StackSet deployed Config, developer disables recorder manually — what happens? | D: Conformance pack re-enables | ❌ | **B: Nothing — StackSets doesn't auto-remediate.** Conformance pack remediates rule violations, not service disablement. | — | StackSets no auto-remediation |
| 284 | D6 | 200 accounts, same WAF on ALBs, auto for new accounts, re-apply if removed? | D: Conformance pack | ❌ | **C: Firewall Manager** — WAF rules + auto-remediate = FM. Conformance packs deploy Config rules, not WAF. | — | Firewall Manager auto-remediation |
| 285 | D3 | SG opened to 0.0.0.0/0 port 22, auto-revert across 300 accounts? | C: Firewall Manager SG audit | ✅ | FM SG audit policy — org-wide, auto-remediate overly permissive SGs. | Q208 | Firewall Manager SG audit |
| 286 | D6 | 15 new accounts join OU, need CloudTrail+Config+GuardDuty immediately, zero manual? | C: StackSets with auto-deploy | ✅ | StackSets targeting OU with auto-deploy = new accounts get stack automatically. | Q276 | StackSets auto-deploy |
| 287 | D6 | Platform team "Golden VPC", app teams self-provision without ec2:CreateVpc? | C: Service Catalog with launch constraint | ✅ | Self-service + no broad IAM = Service Catalog + launch constraint. | Q277 | Service Catalog (self-service) |
| 288 | D3 | Bedrock chatbot, prevent prompt injection + block PII in responses? | B: Bedrock Guardrails | ✅ | Guardrails filter input (prompt injection) and output (PII). | — | GenAI / Bedrock Guardrails |
| 289 | D4 | Mobile app, Cognito sign-in, needs temp AWS creds for S3 upload? | B: Cognito Identity Pool | ✅ | User Pool authenticates. Identity Pool vends temporary AWS credentials. | — | Cognito Identity Pool |
| 290 | D3 | Verify EC2 reachable from internet without sending traffic? | C: Network Access Analyzer | ✅ | Analyzes configs to find unintended network paths — no traffic needed. | — | Network Access Analyzer |
| 291 | D1 | SSE-KMS, alert external decryption, least overhead? | C: GuardDuty S3 Protection | ✅ | "Detect" + "least overhead" = GuardDuty. | Q156 | Detect vs prevent |
| 292 | D1 | EC2 active traffic to mining pool — ThreatPurpose? | B: CryptoCurrency | ✅ | Active mining = CryptoCurrency. | Q218 | GuardDuty finding types |
| 293 | D1 | EC2 DNS query to mining pool, no connection — ThreatPurpose? | C: Impact | ✅ | DNS query only = Impact. Active mining = CryptoCurrency. | Q226 | Impact vs CryptoCurrency |
| 294 | D1 | Credentials from never-seen location, zero code? | C: GuardDuty | ✅ | Active threat + zero code = GuardDuty. | Q233 | Detect vs prevent |
| 295 | D1 | Lambda DNS to C2 domain, want finding generated, no blocking? | A: DNS Firewall ALERT | ❌ | **B: GuardDuty** — DNS Firewall ALERT logs but doesn't produce findings. GuardDuty reads DNS logs + generates findings. | Q106 | DNS Firewall ALERT ≠ finding |


---

### Session 38 — 2025-05-18

**Domains:** Cross-domain exam simulation (all domains)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 296 | D4 | Block external S3 access org-wide without modifying bucket policies? | B: RCP + PrincipalOrgID | ✅ | RCP blocks external callers on resource side. SCP can't stop outsiders. | — | RCP for external access |
| 297 | D3 | EC2 private subnet, no NAT, needs Secrets Manager — which TWO? | B+C: Interface endpoint + SG HTTPS | ✅ | Interface endpoint (Gateway = S3/DynamoDB only) + SG allowing 443. | — | VPC endpoints |
| 298 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, session=Get+Put — DeleteObject? | C: Denied — session policy | ✅ | Session policy ceiling — DeleteObject not in session = denied. | — | Session policy as ceiling |
| 299 | D5 | KMS key scheduled for deletion 5 days ago, 30-day wait — recover? | B: CancelKeyDeletion → Disabled | ✅ | CancelKeyDeletion during wait → Disabled → must re-enable. | — | KMS key deletion recovery |
| 300 | D4 | Identity Center + Okta + SCIM, new engineer joins Platform group? | B: SCIM auto-syncs | ✅ | Group already assigned → new user inherits access automatically. | — | SCIM provisioning |
| 301 | D2 | GuardDuty severity 8.5, EC2 communicating with C2 — first action? | C: Deny-all SG | ✅ | Isolate first → snapshot → investigate. Never terminate. | — | IR sequence |
| 302 | D1 | Investigate finding, blast radius, what else in 48hr? | C: Detective | ✅ | "Investigate" + "blast radius" + "timeline" = Detective. | — | Detective for investigation |
| 303 | D1 | Normalize CloudTrail + VPC Flow + GuardDuty + third-party, own S3? | C: CloudWatch Logs Insights | ❌ | **B: Security Lake** — "normalize" + "single schema" + "your S3" = Security Lake (OCSF). CW Insights queries existing CW data. | — | Security Lake vs CW Logs Insights |
| 304 | D4 | SCP denies PutObject without Env tag, Config SLR writes (no tags)? | C: Fails — SCP applies to SLRs | ✅ | SCP applies to SLRs — they're principals in your account. RCP exempts SLRs. | — | SCP applies to SLRs |
| 305 | D4 | Validate policy for security issues BEFORE deploying? | B: Access Analyzer validation | ✅ | Pre-deployment = Access Analyzer policy validation. Simulator = test existing. | — | Access Analyzer policy validation |


---

### Session 39 — 2025-05-18

**Domains:** Cross-domain exam simulation (all domains, hardest scenarios)
**Score:** 19 ✅ · 0 ⚠️ · 1 ❌ (95% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 306 | D1 | Query VPC Flow Logs in CW for top 10 source IPs — most efficient? | B: CloudWatch Logs Insights | ✅ | Data already in CW + aggregation query = CW Logs Insights. | Q236 | CW Logs Insights vs Detective |
| 307 | D3 | Lambda DNS to C2 domain, BLOCK resolution VPC-wide? | C: DNS Firewall BLOCK | ✅ | DNS Firewall BLOCK kills query at DNS, VPC-wide. | — | DNS Firewall BLOCK |
| 308 | D1 | Lambda DNS to C2 domain, want FINDING generated, no blocking? | B: GuardDuty | ✅ | GuardDuty generates findings. DNS Firewall ALERT just logs. | Q295 | DNS Firewall ALERT ≠ finding |
| 309 | D1 | Normalize CloudTrail + VPC Flow + WAF into OCSF, third-party SIEM reads from S3? | C: Security Lake | ✅ | "Normalize" + "OCSF" + "your S3" = Security Lake. | Q303 | Security Lake / OCSF |
| 310 | D4 | Identity=s3:*, session=GetObject only, bucket policy grants role DeleteObject — result? | B: Allowed — resource-based bypasses session | ✅ | Resource-based policy naming role bypasses session policy ceiling. | Q169 | Session policy bypass |
| 311 | D4 | Same as Q310 but SCP denies DeleteObject — result? | B: Denied — SCP cannot be bypassed | ✅ | SCP cannot be bypassed by anything. | — | SCP cannot be bypassed |
| 312 | D6 | Prove AWS data centers meet ISO 27001 — where? | B: Artifact | ✅ | AWS's compliance = Artifact. | — | AWS Artifact |
| 313 | D6 | Share DNS Firewall rule groups from security account to 15 new accounts? | A: Firewall Manager | ❌ | **B: RAM** — "share resources cross-account" = RAM. FM enforces rules, RAM shares them. | Q126 | RAM for sharing vs FM for enforcing |
| 314 | D6 | 20 Config rules + remediation + single unit + org-wide from delegated admin? | C: Organizational conformance pack | ✅ | Conformance pack = bundle + remediation as one unit. | — | Config conformance packs |
| 315 | D1 | Impact:EC2/BitcoinDomainRequest.Reputation — what happened? | B: DNS query to crypto domain, no connection | ✅ | Impact = DNS query only. CryptoCurrency = active mining. | Q226 | Impact vs CryptoCurrency |
| 316 | D4 | RCP denies s3:* non-org, ELB SLR writes access logs — blocked? | B: Allowed — SLR exempt from RCP | ✅ | SLRs structurally exempt from RCPs. | — | RCP exemptions (SLR) |
| 317 | D4 | Validate new policy + test existing role access — which TWO tools? | A+B: Access Analyzer + Simulator | ✅ | Validation = pre-deploy. Simulator = test existing. | — | Access Analyzer vs Simulator |
| 318 | D5 | Secret rotated, open DB connection still works — why? | B: AWSPREVIOUS | ✅ | Old password valid as AWSPREVIOUS until next rotation. | — | Secrets Manager rotation |
| 319 | D5 | KMS rotated 3 times, decrypt 3-year-old data? | B: Succeeds forever | ✅ | All versions kept forever, auto-routes via ciphertext metadata. | — | KMS auto-rotation retention |
| 320 | D3/D1 | Detect overly permissive SGs + detect malicious IP comms — which TWO? | C+B: FM SG audit + GuardDuty | ✅ | FM = misconfig remediation. GuardDuty = active threats. | — | FM + GuardDuty complementary |
| 321 | D5 | Imported key rotation procedure, keep old key for historical data? | C: New key + import + alias | ✅ | Create new key (EXTERNAL) → import → update alias → old stays. | — | Imported key rotation |
| 322 | D5 | Global Table + MRK, reads fail eu-west-1, primary key policy correct? | B: Replica key policy missing DynamoDB | ✅ | MRK policies independent per region. | — | MRK independent key policies |
| 323 | D4 | Cross-account same-org, RCP denies non-org — result? | B: Allowed — PrincipalOrgID matches | ✅ | Same-org = condition doesn't match = Deny doesn't fire. | — | RCP same-org evaluation |
| 324 | D3/D4 | Enforce IMDSv2 org-wide, block non-compliant launches? | B: SCP | ✅ | "Prevent" + "org-wide" = SCP. | — | SCP for preventive enforcement |
| 325 | D4 | Mobile app, Cognito sign-in, per-user S3 prefix — which TWO? | A+C: Identity Pool + IAM policy with sub | ✅ | Identity Pool vends creds + policy scoped to Cognito sub. | — | Cognito Identity Pool + per-user access |


---

### Session 40 — 2025-05-18

**Domains:** Cross-domain exam simulation (all domains, final validation)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 326 | D1/D2 | GuardDuty Trojan finding severity 8.9, contain + preserve + investigate 72hr — correct sequence? (THREE) | B+C+D | ✅ | Isolate (deny-all SG) → EBS snapshot → Detective for 72hr blast radius. Never terminate first. | — | IR sequence + Detective |
| 327 | D4 | Identity=s3:*+ec2:*+lambda:*, boundary=s3:*+ec2:*, session=Get+Put, same-account bucket policy grants role DeleteObject — result? | C: Allowed — resource-based bypasses session | ✅ | Resource-based policy naming role bypasses session policy ceiling. Boundary allows s3:* so no block there. | Q169 | Session policy bypass by resource-based policy |
| 328 | D5 | PHI in S3 with CMK, need: DR credentials, key in both regions, mask PHI in CW Logs — which THREE? | A+C+E | ✅ | MRK for cross-region key + Secrets Manager replication for credentials + CW Logs data protection for masking. | — | MRK + Secrets Manager replication + data masking |
| 329 | D3/D6 | 400 accounts, block malicious DNS org-wide, auto-apply new accounts, auto-remediate disassociation — which TWO? | A+B: RAM + Firewall Manager | ✅ | RAM shares rule group. FM enforces association + auto-remediates. They complement each other. | Q313 | RAM for sharing + FM for enforcing |
| 330 | D1/D6 | CIS compliance dashboard across 200 accounts + collect SOC 2 evidence for audit — which TWO services? | B+C: Security Hub + Audit Manager | ✅ | Security Hub = CIS dashboard. Audit Manager = YOUR evidence mapped to SOC 2. Artifact = AWS's reports. | — | Security Hub vs Audit Manager vs Artifact |


---

### Session 41 — 2025-05-19

**Domains:** Cross-domain (untested gaps — Bedrock, Cognito, OAC+KMS, Security Lake, VPC endpoints)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 331 | D3 | Bedrock chatbot: prevent prompt injection + block PII in responses + restrict model access — which TWO? | B+C | ✅ | Bedrock Guardrails (content) + IAM bedrock:InvokeModel (access). WAF ≠ LLM content. | — | Bedrock Guardrails + IAM |
| 332 | D4 | Mobile app, Cognito sign-in, per-user S3 folders + guest read-only — which TWO? | A+D | ✅ | User Pool authenticates + Identity Pool vends creds (auth role per-user, unauth role guest). | — | Cognito Identity Pool + per-user access |
| 333 | D5 | CloudFront + S3 origin + SSE-KMS, only CF can access — which TWO? | B+C | ✅ | OAC (not OAI) for SSE-KMS + KMS key policy granting CF service principal. OAI can't do KMS. | — | OAC + KMS key policy |
| 334 | D1 | Security Lake + Splunk — which THREE true statements? | A+B+F | ✅ | Your S3 (Parquet) + OCSF normalized + third-party OCSF ingestion. Not real-time (batch). | — | Security Lake / OCSF |
| 335 | D3/D5 | Private subnet (no NAT), needs Secrets Manager + S3 SSE-KMS upload — minimum infra? (THREE) | A+B+D | ✅ | Interface endpoint (Secrets Mgr) + Gateway endpoint (S3) + SG HTTPS. KMS endpoint not needed — S3 calls KMS server-side. | — | VPC endpoints + SSE-KMS server-side |


---

### Session 43 — 2025-05-20

**Domains:** Cross-domain (killer set — remaining 🟡 weak areas)
**Score:** 10 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 360 | D3/D4 | Verified Access: stolen laptop, block specific device without affecting others? | B: Update device trust provider | ✅ | Mark device non-compliant in device trust provider | Q336 | Verified Access trust providers |
| 361 | D6 | StackSets deployed Config, developer disables recorder — what happens? | B: Nothing — StackSets no auto-remediation | ✅ | StackSets does not auto-remediate drift | Q283 | StackSets no auto-remediation |
| 362 | D1 | GuardDuty finding `Trojan:EC2/DriveBySourceTraffic!DNS` — what does !DNS mean? | B: Finding from DNS log analysis | ✅ | !suffix = data source used for detection | — | GuardDuty finding structure |
| 363 | D4/D5 | Cross-account S3+KMS, all policies correct, still fails — cause? | B: Account B's SCP denies kms:Decrypt | ✅ | SCP follows the caller | Q256 | Cross-account KMS + SCP evaluation |
| 364 | D6 | Self-provision hardened RDS, devs don't need rds:CreateDBInstance? | B: Service Catalog with launch constraint | ✅ | Launch constraint = Service Catalog assumes role | Q274 | Service Catalog (self-service) |
| 365 | D1/D2 | After containment, determine other resources accessed, visualize timeline? | C: Detective | ✅ | "What else" + "visualize" + "timeline" = Detective | Q109 | Detective for investigation |
| 366 | D5 | KMS rotated 3 times, decrypt original data from year 1? | B: Succeeds — auto-routes to correct version | ✅ | All versions kept forever, ciphertext metadata routes | Q192 | KMS auto-rotation retention |
| 367 | D3 | DNS Firewall: ALLOW 2 domains + ALERT crypto + BLOCK all — priority order? | B: ALLOW → ALLOW → ALERT → BLOCK | ✅ | First match wins, ALLOW specific first, BLOCK * last | Q134 | DNS Firewall rule structure |
| 368 | D4 | SCP denies RunInstances without tag, Config SLR launches (no tags) — result? | B: Fails — SCP applies to SLRs | ✅ | SLRs escape RCPs, NOT SCPs | Q97 | SCP applies to SLRs |
| 369 | D1/D5 | Prevent external decrypt + alert on attempts — which TWO? | D+B: RCP + GuardDuty | ✅ | RCP prevents, GuardDuty detects | Q100 | Detect vs prevent (RCP + GuardDuty) |

---

### Session 42 — 2025-05-19

**Domains:** Cross-domain (Signer, Verified Access, Cognito, hybrid, detection gaps)
**Score:** 18 ✅ · 0 ⚠️ · 3 ❌ (86% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 336 | D3/D4 | Verified Access: Okta group + device posture — which TWO enforce? | A+C | ❌ | **A+B**: Trust provider for Okta (identity) + trust provider for device management (posture). IAM doesn't control VA decisions. | — | Verified Access trust providers |
| 337 | D5 | Lambda uploads SSE-KMS, key policy grants root, role has GenerateDataKey — fails? | B: Should succeed | ✅ | Root enables delegation + identity has GenerateDataKey = both sides satisfied. Trick question. | Q206 | KMS key policy delegation |
| 338 | D1 | CryptoCurrency vs Impact finding — DNS query + active mining from same instance? | D: Different stages | ✅ | CryptoCurrency = active mining traffic. Impact = DNS query only. Different stages of same attack. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 339 | D4/D6 | Signer: developer left, backdoored Lambda found — most targeted remediation? | D: Remove IAM | ❌ | **B: Revoke specific signing job.** Remove IAM prevents future but doesn't invalidate existing artifact. | — | Signer revocation (job vs profile vs IAM) |
| 340 | D3 | Verify EC2 reachable from internet without sending traffic? | C: Network Access Analyzer | ✅ | "Any instance unintentionally reachable" = broad discovery = Network Access Analyzer. | — | Network Access Analyzer vs Reachability |
| 341 | D3/D4 | Cognito + S3 per-user + SSE-KMS — what additional config? (TWO) | B+C | ❌ | **A+B**: Identity Pool auth role needs kms:GenerateDataKey (mobile app calls S3 directly, not Lambda). | — | Cognito Identity Pool + KMS permissions |
| 342 | D1/D3 | EC2 DNS to C2 domain — finding generated + block DNS? | B | ✅ | GuardDuty for finding + DNS Firewall BLOCK for prevention. DNS Firewall ALERT ≠ finding. | Q295 | GuardDuty + DNS Firewall complementary |
| 343 | D4/D5 | Signer: ENFORCE + allowed profile + invalidate one artifact — THREE? | A+E+F | ✅ | CSC ENFORCE (A) + attach to function (F) + revoke job for compromised artifact (E). | Q339 | Signer CSC + revocation |
| 344 | D5/D6 | S3 immutable 7yr + HIPAA evidence — THREE? | B+D | ✅ | Compliance mode (B) + Audit Manager HIPAA (D). Question design asked THREE but only two needed. | — | Object Lock + Audit Manager |
| 345 | D4/D3 | Prevent IMDSv1 launches org-wide — approach? | B: SCP | ✅ | "Prevent" + "org-wide" = SCP denying RunInstances unless MetadataHttpTokens=required. | Q261 | SCP for preventive enforcement |
| 346 | D1/D5 | Alert external KMS decryption, least overhead? | C: GuardDuty | ✅ | "Alert" + "least overhead" = GuardDuty S3 Protection. | Q156 | Detect vs prevent |
| 347 | D2/D4 | Exfiltrated role creds, stop attacker + keep app working? | B: Inline Deny TokenIssueTime | ✅ | Deny sessions before timestamp, app gets new creds after. | Q71 | STS session revocation |
| 348 | D6/D3 | 25 Config rules + remediation + single package + org-wide? | C: Conformance pack | ✅ | Organizational conformance pack from delegated admin. | Q275 | Config conformance packs |
| 349 | D3/D5 | Dedicated DX, Layer 2 encryption, zero overhead? | B: MACsec | ✅ | MACsec = Layer 2, dedicated only, line-rate. | — | MACsec |
| 350 | D4/D5 | Cross-account Lambda → S3+KMS, all correct, AccessDenied — cause? | B: Account B's SCP | ✅ | SCP follows the caller even when accessing another account's resources. | Q256 | Cross-account KMS + SCP |
| 351 | D1/D2 | Impact finding then CryptoCurrency finding 30min later — what happened? | B: DNS query → active mining | ✅ | Instance progressed from DNS resolution to active mining traffic. | Q226 | GuardDuty finding stages |
| 352 | D3/D6 | RAM shares rule group + FM policy, developer disassociates — what happens? | B: FM re-associates automatically | ✅ | FM auto-remediates. Developer can disassociate but FM re-applies. | Q329 | FM auto-remediation |
| 353 | D4 | RCP denies non-org s3:*. ELB SLR + CloudTrail + external attacker — which succeed? | B: SLR + CloudTrail only | ✅ | SLR exempt (structural) + CloudTrail exempt (PrincipalIsAWSService). Attacker blocked. | Q217 | RCP exemptions (both paths) |
| 354 | D5/D3 | Key material NEVER in AWS + native S3 SSE-KMS integration? | B: XKS | ✅ | External key store — material outside AWS, integrates via KMS API. | Q102 | XKS |
| 355 | D1/D4 | Access Analyzer finds external access + GuardDuty finds malicious IP — what does each tell you? | B: AA=exposed, GD=being exploited | ✅ | AA = misconfiguration. GD = active threat. Complementary. | Q205 | Access Analyzer vs GuardDuty |
| 356 | D2/D1 | After containment, determine roles used + buckets accessed + 72hr timeline? | C: Detective | ✅ | "What else" + "timeline" + "blast radius" = Detective. | Q109 | Detective for investigation |
| 357 | D6/D4 | Identity Center + Okta + SCIM, new engineer joins Platform group? | B: SCIM auto-syncs | ✅ | Group already assigned → new user inherits access automatically. | Q263 | SCIM provisioning |
| 358 | D5 | CreateGrant → partner AccessDenied immediately, works 30s later? | B: Grant token | ✅ | Pass grant token for immediate use before eventual consistency. | Q101 | KMS Grants eventual consistency |
| 359 | D3/D5 | Private subnet needs DynamoDB + S3, minimize cost — endpoint types? | B: Gateway for both | ✅ | S3 + DynamoDB = only two Gateway endpoint services (free). | Q249 | Gateway vs Interface endpoints |


### Session 44 — 2025-05-20

**Domains:** Cross-domain killer exam simulation (all domains, novel scenarios)
**Score:** 7 ✅ · 0 ⚠️ · 3 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 370 | D4/D6 | RCP block external S3 + exempt Config — which TWO? | B+C | ✅ | RCP with PrincipalOrgID + PrincipalIsAWSService exception | — | RCP + PrincipalIsAWSService |
| 371 | D4/D5 | SCP denies kms:Decrypt unless ViaService=s3, Lambda still works — why? | B: ViaService satisfied | ✅ | S3 calls KMS on behalf of caller, condition satisfied | — | kms:ViaService condition |
| 372 | D1 | GuardDuty enabled all regions, zero findings 90 days, active workloads — cause? | A: VPC Flow Logs not enabled | ❌ | **D: Suppression rule archiving findings.** GuardDuty reads Flow Logs via internal feed. Zero findings on active workloads = suppression rule. | — | GuardDuty suppression rules |
| 373 | D6 | Self-service VPC, no broad IAM, NOT auto for new accounts — which service? | B: Service Catalog | ✅ | Self-service + no broad IAM + not automatic = Service Catalog with launch constraint | — | Service Catalog (self-service) |
| 374 | D4 | Find unused permissions 90d + generate replacement policies, least overhead — which TWO? | C+A | ❌ | **A+B: Access Analyzer unused access + policy generation.** Config rule = role-level, not permission-level. | — | Access Analyzer unused + policy generation |
| 375 | D5 | CW Logs mask credit cards + only compliance sees raw + audit trail — which THREE? | A+B+E | ✅ | Data protection policy + logs:Unmask + audit destination | — | CW Logs data masking |
| 376 | D5 | Secrets Manager rotation, batch works, new Lambda fails on RDS — cause? | C: Missing GetSecretValue | ❌ | **D: Rotation Lambda failed to update DB password.** Error on DATABASE = credential problem, not IAM. | — | Secrets Manager rotation failure |
| 377 | D4/D6 | Data perimeter: block external IN + block exfil OUT + exempt services — which TWO? | A+B | ✅ | RCP (block outsiders) + SCP with ResourceAccount (block exfil) | — | Data perimeter (RCP+SCP) |
| 378 | D3/D5 | Private subnet, Secrets Manager + S3 SSE-KMS + CW Logs — minimum endpoints? | 3 | ✅ | Gateway (S3) + Interface (Secrets Mgr) + Interface (CW Logs). KMS not needed — S3 calls server-side. | — | VPC endpoints minimum |
| 379 | D1/D2 | Trojan finding severity 8.2, contain + preserve + investigate 72hr — sequence? | B,C,D | ✅ | Isolate (deny-all SG) → Snapshot (EBS) → Detective (72hr timeline) | — | IR sequence + Detective |


### Session 45 — 2025-05-22

**Domains:** Cross-domain (re-test — Session 44 errors + validation)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 380 | D1 | GuardDuty zero findings 6 months, junior created filter — investigate first? | C: Suppression rules with overly broad filter | ✅ | Suppression rules auto-archive findings. "Created filter to reduce noise" = suppression rule. | Q372 | GuardDuty suppression rules |
| 381 | D4 | Find unused permissions 90d + generate replacement policy, least overhead? | B: Access Analyzer unused + policy generation | ✅ | Two features, one service, least overhead. | Q374 | Access Analyzer unused + policy generation |
| 382 | D5 | Rotation completes, new Lambda "password auth failed" on RDS, ECS works — cause? | C: Rotation Lambda failed ALTER USER on RDS | ✅ | Error on DATABASE = rotation Lambda didn't update DB. ECS uses old connection (AWSPREVIOUS). | Q376 | Secrets Manager rotation failure |
| 383 | D5 | S3 CRR + MRK, decrypt fails in destination, replica exists — cause? | B: MRK replica key policy missing kms:Decrypt | ✅ | MRK policies independent per region — must update each separately. | Q84 | MRK independent key policies |
| 384 | D4/D1 | Block external S3 access org-wide + detect attempts — which TWO? | B+C: RCP + GuardDuty S3 Protection | ✅ | RCP prevents, GuardDuty detects. SCP can't stop external callers. | Q369 | Detect vs prevent (RCP + GuardDuty) |


### Session 46 — 2026-05-24

**Domains:** Cross-domain exam simulation (all domains, certification-level)
**Score:** 10 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 385 | D4/D6 | Block external S3 org-wide, exempt AWS services — which TWO? | B+D: RCP + PrincipalIsAWSService | ✅ | RCP with PrincipalOrgID + PrincipalIsAWSService exception | — | RCP + PrincipalIsAWSService |
| 386 | D1/D2 | EC2 C2 communication, determine other resources + roles + 72hr timeline? | B: Detective | ✅ | "Investigate" + "what else" + "timeline" = Detective | — | Detective for investigation |
| 387 | D5 | Key policy grants root only, Lambda has GenerateDataKey — upload result? | B: Succeeds — root enables delegation | ✅ | Root = IAM delegation. GenerateDataKey correct for S3 envelope encryption. | — | KMS key policy delegation |
| 388 | D3/D6 | WAF on all ALBs, auto-remediate if removed, new accounts — which service? | C: Firewall Manager | ✅ | FM = WAF rules + auto-remediate + org-wide | — | Firewall Manager auto-remediation |
| 389 | D1 | GuardDuty enabled, zero findings 90d, active workloads, Flow Logs not enabled — cause? | D: Suppression rule | ✅ | GuardDuty reads Flow Logs internally. Zero findings = suppression rule. | Q372 | GuardDuty suppression rules |
| 390 | D4/D5 | Cross-account S3+KMS, SCP denies kms:* unless ViaService=s3 — result? | B: Succeeds — ViaService satisfied | ✅ | S3 calls KMS on behalf of caller, condition satisfied | — | kms:ViaService + SCP |
| 391 | D6 | SOC 2: own evidence mapped to controls + AWS certification — which TWO? | B+C: Audit Manager + Artifact | ✅ | Audit Manager = YOUR evidence. Artifact = AWS's reports. | — | Audit Manager vs Artifact |
| 392 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, session=Get+Put, bucket policy grants Delete — result? | C: Allowed — resource-based bypasses session | ✅ | Same-account resource-based policy bypasses session policy ceiling | — | Session policy bypass |
| 393 | D3 | DNS Firewall: ALLOW 2 domains + ALERT crypto + BLOCK all — rule order? | B: ALLOW → ALLOW → ALERT → BLOCK | ✅ | First match wins, ALLOW specific first, BLOCK * last | — | DNS Firewall rule structure |
| 394 | D6 | Service Catalog, dev only has ProvisionProduct, VPC created — how? | B: Launch constraint role | ✅ | Launch constraint = Service Catalog assumes role with permissions | — | Service Catalog launch constraint |


### Session 47 — 2026-05-24

**Domains:** Cross-domain killer exam simulation (all domains, novel scenarios)
**Score:** 7 ✅ · 1 ⚠️ · 2 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 395 | D4/D3 | Multi-tenant DynamoDB, Cognito Identity Pool, Tenant A reads Tenant B — fix? (TWO) | A+C | ⚠️ | **C+D**: Map TenantId as session tag (C) + Verified Permissions for app-level authz (D). `sub` ≠ TenantId. | — | Cognito + DynamoDB ABAC (sub vs TenantId) |
| 396 | D2/D4 | Exfiltrated role creds, stop attacker + keep ECS running? | B: Inline Deny TokenIssueTime | ✅ | Deny sessions before timestamp, ECS gets new creds after. | Q71 | STS session revocation |
| 397 | D3 | Network Firewall TLS inspection — cert warnings — fix? | B: Distribute private CA to trust stores | ✅ | Private CA + MITM pattern — distribute to client trust stores. | Q87 | Network Firewall TLS inspection |
| 398 | D4/D6 | Data perimeter: block external IN + block exfil OUT — which TWO? | A+C | ❌ | **A+B**: RCP (block outsiders IN) + SCP with ResourceAccount (block insiders OUT). Bucket policy per-bucket doesn't scale. | — | Data perimeter (RCP blocks IN, SCP blocks OUT) |
| 399 | D5 | S3 CRR + MRK, decrypt fails in eu-west-1 — cause? | B: MRK replica key policy missing permissions | ✅ | MRK policies independent per region — must update each separately. | Q84 | MRK independent key policies |
| 400 | D4 | Identity Center + Okta + SCIM, new engineer joins Platform group — how? (TWO) | A+B: SCIM syncs + group already assigned | ✅ | SCIM auto-syncs. Group assigned to permission set → inherits access. | Q263 | SCIM provisioning |
| 401 | D1 | Detect StopLogging within 5 min, org trail exists, least overhead? | C: Config rule | ❌ | **B: EventBridge rule in management account.** Near real-time, one rule. Config is slower + heavier. | — | EventBridge for fast detection |
| 402 | D3/D5 | Private subnet, Secrets Manager + S3 SSE-KMS + CW Logs — minimum endpoints? | B: 3 | ✅ | Gateway (S3) + Interface (Secrets Mgr) + Interface (CW Logs). KMS not needed — S3 calls server-side. | — | VPC endpoints minimum |
| 403 | D5 | Rotation completes, new Lambda "password auth failed" on RDS, ECS works — cause? | B: Rotation Lambda failed ALTER USER on RDS | ✅ | Error on DATABASE = rotation Lambda didn't update DB. ECS uses old connection (AWSPREVIOUS). | Q376 | Secrets Manager rotation failure |
| 404 | D4 | Find unused permissions 90d + generate replacement policies, least overhead? | B: Access Analyzer unused + policy generation | ✅ | Two features, one service, least overhead. | Q374 | Access Analyzer unused + policy generation |


### Session 48 — 2026-05-24

**Domains:** Cross-domain killer exam simulation (all domains, novel scenarios)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 405 | D5 | CW Logs mask credit cards + only compliance sees raw — which TWO? | B+C: Data protection + deny Unmask | ✅ | Data protection policy + logs:Unmask for authorized users. | — | CW Logs data masking |
| 406 | D4 | External account, trust policy allows, RCP denies non-org STS — result? | C: Denied by RCP | ✅ | RCP evaluated on resource side, external caller blocked. | — | RCP blocks external AssumeRole |
| 407 | D3/D6 | Share DNS FW rule groups + auto-remediate disassociation — which TWO? | A+B: RAM + Firewall Manager | ✅ | RAM shares, FM enforces + auto-remediates. | Q313 | RAM for sharing + FM for enforcing |
| 408 | D3 | Lambda private subnet, restrict DNS to one domain, cheapest? | B: DNS Firewall | ✅ | DNS Firewall = cheapest domain filtering. Network Firewall overkill. | — | DNS Firewall cost-effective |
| 409 | D5 | KMS rotated 3 times, decrypt original data from 3 years ago? | C: Succeeds — auto-routes via ciphertext metadata | ✅ | All versions kept forever, auto-routes. | — | KMS auto-rotation retention |
| 410 | D1 | Detect public S3 org-wide, dashboard + least overhead — Config vs Security Hub? | B: Security Hub | ✅ | Security Hub wraps Config + dashboards + one-click org-wide. | Q5 | Security services comparison |
| 411 | D4 | SCP denies PutObject without tag, Config SLR writes (no tags) — result? | B: Fails — SCP applies to SLRs | ✅ | SLRs escape RCPs, NOT SCPs. | Q97 | SCP applies to SLRs |
| 412 | D4/D3 | Cognito per-user S3, pen tester crafts request to other user's prefix? | B: Fails — IAM policy restricts to caller's sub | ✅ | Policy Resource uses sub variable, mismatch = denied. | — | Cognito per-user isolation |
| 413 | D3/D4 | Enforce IMDSv2 org-wide, block non-compliant launches immediately? | A: Config + auto-remediation | ❌ | **B: SCP** denying RunInstances unless MetadataHttpTokens=required. "Prevent" = SCP. | Q261 | SCP for preventive enforcement |
| 414 | D5 | CloudFront + S3 SSE-KMS, only CF can access — which TWO? | B+C: OAC + KMS key policy for CF service principal | ✅ | OAC (not OAI) for SSE-KMS + KMS key policy granting CF. | — | OAC + KMS key policy |


### Session 49 — 2026-05-24

**Domains:** Cross-domain lightning rounds (all domains, novel scenarios)
**Score:** 10 ✅ · 0 ⚠️ · 5 ❌ (67% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 415 | D6/D1 | Prevent StopLogging from ever happening again, org-wide? | B: SCP Deny StopLogging | ✅ | "Prevent" = SCP. EventBridge = detect. Config = remediate. | Q401 | SCP for preventive enforcement |
| 416 | D1 | Query VPC Flow Logs in CW for top 10 source IPs — most efficient? | B: CloudWatch Logs Insights | ✅ | Data already in CW + aggregation = CW Logs Insights. | Q236 | CW Logs Insights vs Detective |
| 417 | D4/D6 | Enforce CostCenter tag on all EC2 launches org-wide, never create without? | B: SCP + RequestTag Null condition | ✅ | "Must have tag" + "never created without" + org-wide = SCP. | Q73 | SCP + RequestTag enforcement |
| 418 | D3 | Lambda timeout calling Secrets Manager, endpoint exists, endpoint SG correct — cause? | B: Endpoint policy denies | ❌ | **A: Lambda SG missing outbound HTTPS.** Timeout = network problem, not permissions. | — | Timeout vs Access Denied (SG troubleshooting) |
| 419 | D1 | Normalize CloudTrail + VPC Flow + GuardDuty + third-party, own S3, SIEM reads? | B: Security Lake | ✅ | "Normalize" + "single schema" + "your S3" = Security Lake (OCSF). | Q303 | Security Lake / OCSF |
| 420 | D3 | Bedrock: prevent prompt injection + block PII in responses + restrict model access — which TWO? | B+C: Guardrails + IAM | ✅ | Guardrails (content) + IAM bedrock:InvokeModel (access). | — | Bedrock Guardrails + IAM |
| 421 | D2 | EC2 C2 communication: contain + preserve + investigate 72hr — sequence? | B: Deny-all SG → EBS snapshot → Detective | ✅ | Isolate → snapshot → Detective for timeline. | — | IR sequence + Detective |
| 422 | D5 | KMS auto-rotation enabled, rotated once in 2 years — how many material versions? | B: 2 | ✅ | Original + one rotation = 2. All kept forever. | — | KMS rotation versions |
| 423 | D5/D4 | Cross-account KMS, key policy + identity policy correct, still Access Denied — cause? | Confused | ❌ | **C: Wrong regional endpoint.** KMS keys are regional — calling wrong region = key not found. | — | KMS is regional |
| 424 | D3/D6 | RAM shares DNS FW rule group, FM enforces, developer disassociates — what happens? | B: FM re-associates automatically | ✅ | FM auto-remediates. Developer can disassociate but FM re-applies. | Q329 | FM auto-remediation |
| 425 | D4/D5 | SCP denies kms:Decrypt unless ViaService=s3, developer calls KMS directly from CLI? | B: Fails — ViaService not satisfied | ✅ | Direct call has no ViaService context → SCP Deny fires. | — | kms:ViaService + SCP |
| 426 | D5 | Default encryption SSE-KMS + bucket policy Deny if wrong key header — upload without header? | A: Succeeds (default encryption) | ❌ | **B: Fails — bucket policy evaluates headers BEFORE default encryption applies.** | — | Default encryption vs bucket policy Deny |
| 427 | D4 | RCP denies non-org s3:*, same-account Lambda writes to own bucket — result? | D: Succeeds — RCPs don't apply same-account | ❌ | **B: Succeeds — RCPs DO apply, but Lambda's PrincipalOrgID matches → Deny doesn't fire.** | — | RCP same-org evaluation |
| 428 | D5 | Secrets Manager cross-region replication, source key is single-region (not MRK) — works? | A: Replication fails, needs MRK | ❌ | **C: Works — you specify a separate key in destination region. SM re-encrypts.** MRK not required. | — | Secrets Manager replication ≠ MRK |
| 429 | D4 | Employee terminated in Okta, revoke AWS access within minutes — mechanism? | A: SCIM deprovisioning | ✅ | SCIM auto-syncs lifecycle. Deactivate in Okta → removed from Identity Center within minutes. | — | SCIM deprovisioning |


### Session 50 — 2026-05-25

**Domains:** Cross-domain (re-test — Session 49 errors + new killer)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 430 | D3 | Lambda timeout calling Secrets Manager, endpoint exists, endpoint SG correct — cause? | B: Lambda SG missing outbound HTTPS | ✅ | Timeout = network problem. Lambda SG needs outbound 443. | Q418 | Timeout vs Access Denied (SG troubleshooting) |
| 431 | D5 | Default encryption SSE-KMS + bucket policy Deny if wrong key header — upload without header? | B: Fails — bucket policy evaluates before default encryption | ✅ | Bucket policy checks headers BEFORE default encryption applies. | Q426 | Default encryption vs bucket policy Deny |
| 432 | D4 | RCP denies non-org s3:*, same-account Lambda writes to own bucket — result? | B: Succeeds — PrincipalOrgID matches, Deny doesn't fire | ✅ | RCPs DO apply same-account, but condition logic determines outcome. | Q427 | RCP same-org evaluation |
| 433 | D5 | Secrets Manager cross-region replication, source key is single-region (not MRK) — works? | B: Works — specify different key in destination, SM re-encrypts | ✅ | MRK not required. SM re-encrypts with whatever key you specify. | Q428 | Secrets Manager replication ≠ MRK |
| 434 | D3/D6 | Prevent EC2 launch without IMDSv2 + detect existing IMDSv1 and fix — which TWO? | A+B: SCP + Config rule with SSM remediation | ✅ | SCP prevents. Config + SSM detects and fixes existing. | Q261, Q413 | SCP prevent + Config detect/fix |


### Session 51 — 2026-05-25

**Domains:** D6 Governance (targeted drill — RAM vs FM, StackSets, Service Catalog, Audit Manager)
**Score:** 11 ✅ · 0 ⚠️ · 5 ❌ (69% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 435 | D6 | WAF on all ALBs, auto-apply new accounts, re-attach if removed — which service? | C: Config conformance pack | ❌ | **B: Firewall Manager WAF policy.** FM manages WAF/SG/DNS FW/NF. Config can't deploy WAF. | Q284 | Firewall Manager auto-remediation |
| 436 | D6 | Self-provision Golden VPC, dev only has ProvisionProduct — how? | B: Service Catalog launch constraint role | ✅ | Launch constraint role has ec2:CreateVpc. | Q277 | Service Catalog (self-service) |
| 437 | D6 | 15 new accounts need GuardDuty + Config + CloudTrail, zero manual — which service? | C: StackSets with service-managed + auto-deploy | ✅ | StackSets deploys any resource, auto for new accounts. | Q276 | StackSets auto-deploy |
| 438 | D6 | Proof AWS meets ISO 27001 + YOUR evidence mapped to SOC 2 — which TWO? | B+C: Artifact + Audit Manager | ✅ | Artifact = AWS's reports. Audit Manager = YOUR evidence. | Q271 | Audit Manager vs Artifact |
| 439 | D6 | StackSets deployed Config, developer stops recorder — what happens? | C: Conformance pack re-enables | ❌ | **B: Nothing — StackSets doesn't auto-remediate.** | Q283 | StackSets no auto-remediation |
| 440 | D6 | Want Config to stay enabled, auto re-enable if stopped — approach? | B: Config rule + SSM remediation | ❌ | **C: SCP denying StopConfigurationRecorder.** Config can't remediate its own disablement. | — | SCP prevents disabling services |
| 441 | D6 | Share DNS FW rule groups from security account to 200 members — which service? | A: Firewall Manager | ❌ | **B: RAM.** "Share" = RAM. "Enforce" = FM. | Q313 | RAM for sharing vs FM for enforcing |
| 442 | D6 | DNS FW rule groups: share + enforce on all VPCs + re-associate if removed — which TWO? | B+D: FM + conformance pack | ❌ | **A+B: RAM + FM.** RAM shares, FM enforces. Config can't associate firewall resources. | Q329 | RAM + FM complementary |
| 443 | D6 | WAF on all ALBs, auto-remediate — need RAM? | B: No — FM creates WAF directly | ✅ | FM creates + deploys WAF Web ACLs directly. No RAM needed. | — | FM creates WAF directly |
| 444 | D6 | Control Tower prevent disabling GuardDuty/CloudTrail/Config — which mechanism? | B: Preventive guardrail (SCP) | ✅ | "Prevent" = SCP. Detective = Config rule. Proactive = CF Hook. | Q251 | SCP for preventive guardrails |
| 445 | D6 | GuardDuty + S3 encryption check + WAF + DNS FW + prevent CloudTrail disable — which FOUR? | A+C+D+E (missed B) | ❌ | **A+B+C+D+E** (all five needed). Missed conformance pack for "check + fix." | — | Full governance stack |
| 446 | D6 | Network FW policy: share to 200 accounts + enforce + recreate if deleted — which TWO? | A+B: RAM + FM | ✅ | RAM shares, FM enforces lifecycle. | — | RAM + FM for Network FW |
| 447 | D6 | Self-provision hardened RDS, dev only has ProvisionProduct — how? | B: Service Catalog launch constraint role | ✅ | Launch constraint role has rds:CreateDBInstance. | Q274 | Service Catalog (self-service) |
| 448 | D6 | Match verbs to RAM vs FM (4 items) | All correct (A, FM, FM, FM) | ✅ | "Make visible" = RAM. Ensure/enforce/re-apply/create = FM. | — | RAM vs FM verb test |
| 449 | D6 | Prevent unencrypted uploads + collect PCI evidence for auditor — which TWO? | A+D: SCP + Audit Manager | ✅ | SCP prevents. Audit Manager collects evidence for frameworks. | — | SCP + Audit Manager |
| 450 | D6 | Why can't StackSets do everything? Two limitations? | B+E: no remediation + no auto-deploy | ❌ | **B+C: no auto-remediation + can't share resources.** StackSets CAN auto-deploy to new accounts. | — | StackSets limitations |
| 451 | D6 | Shield Advanced on all CloudFront + ALBs across 150 accounts — which service? | B: Firewall Manager only | ✅ | FM creates Shield protections directly. No RAM needed. | — | FM creates directly (Shield) |
| 452 | D6 | TGW in shared-services account, 40 accounts need to attach — which service? | B: RAM | ✅ | TGW = infrastructure sharing = RAM. | — | RAM for TGW sharing |
| 453 | D6 | Detect overly permissive SGs (0.0.0.0/0 port 22) + auto-revoke across 300 accounts? | B: Firewall Manager SG audit | ✅ | FM SG audit = find + auto-remediate overly permissive SGs org-wide. | Q208 | Firewall Manager SG audit |
| 454 | D6 | Ensure baseline SG (deny all inbound) applied to all EC2 across 300 accounts? | B: RAM | ❌ | **A: Firewall Manager SG common policy.** FM creates the SG in each account. Nothing being shared. | — | FM SG common policy |
| 455 | D6 | "DNS FW rule group needs to be accessible to member accounts" — which service? | A: RAM | ✅ | "Accessible/visible/share" = RAM. | — | RAM verb signal |
| 456 | D6 | "DNS FW rule group must be associated with every VPC + re-associated if removed" — which? | B: Firewall Manager | ✅ | "Associated/enforce/re-apply" = FM. | — | FM verb signal |
| 457 | D6 | Network FW policy: Step 1 share, Step 2 enforce — correct sequence? | A: RAM shares, FM enforces | ✅ | RAM first (available), FM second (mandatory). | — | RAM + FM sequence |
| 458 | D6 | Prevent IGW creation + detect/fix flow logs + self-provision VPC + SOC 2 evidence — which FOUR? | A+B+C+D: SCP + conformance pack + Service Catalog + Audit Manager | ✅ | Four governance patterns in one question. | — | Full governance stack |
| 459 | D6 | Control Tower: someone modifies SCP outside CT — what happens? | B: Drift alert, no auto-fix | ✅ | CT detects drift but doesn't auto-revert. | — | Control Tower drift |
| 460 | D6 | Deny LeaveOrganization + CreateUser + StopLogging org-wide — where? | B: SCP on org root | ✅ | Restrict principals = SCP. | — | SCP for preventive guardrails |
| 461 | D6 | Block external S3 reads even with Principal:* bucket policy — where? | B: RCP on org root | ✅ | Block external callers on resources = RCP. | — | RCP for external access |
| 462 | D6 | Which services support delegated admin? (GuardDuty, SH, FM, Config, Audit Manager) | A+B+C+D (missed E) | ⚠️ | **F: All of them.** Every security service supports delegated admin. | — | Delegated admin (all services) |
| 463 | D6 | SCP denies DeleteBucket, user in management account calls it — result? | B: Allowed — mgmt account exempt | ✅ | Management account exempt from SCPs and RCPs. | — | Management account exempt |
| 464 | D6 | Block CF template deploying S3 without encryption — which guardrail type? | A: Preventive (SCP) | ❌ | **C: Proactive (CloudFormation Hook).** SCP blocks API calls. Hook validates template content. | — | Proactive guardrail (CF Hook) |
| 465 | D6 | Proactive guardrails — which statement true? | B: Validate CF templates before resources created | ✅ | Proactive = inspect IaC before deployment. | — | Proactive guardrail definition |
| 466 | D6 | Signed Lambda: validate template + detect unsigned + prevent disabling CSC — which THREE? | A+B+C: Proactive + Detective + SCP | ✅ | Three layers: proactive + detective + preventive. | — | Layered guardrails |
| 467 | D6 | Prevent GuardDuty disablement, never even briefly — approach? | B: SCP denying DeleteDetector + StopMonitoringMembers | ✅ | "Never even briefly" = preventive = SCP. Config has a gap. | Q440 | SCP prevents disabling services |
| 468 | D6 | CF template must include StorageEncrypted + DeletionProtection, fail before creation? | C: Proactive guardrail (CF Hook) | ✅ | "Template must include X" + "before creation" = CF Hook. | Q464 | Proactive guardrail (CF Hook) |
| 469 | D6 | Prevent unsigned Lambda deploy + detect missing CSC + prevent deleting CSC — THREE? | A+C+D: Proactive + Config + SCP | ✅ | Three layers: proactive (template) + detective (after) + preventive (API block). | — | Layered guardrails |
| 470 | D6 | RAM shared subnet, developer launches EC2 — who owns the instance? | B: Workload account (launcher) | ✅ | RAM shares infra, resources launched belong to launcher. | — | RAM shared VPC ownership |
| 471 | D6 | Match 5 scenarios to 5 services (SCP/Config/FM/SC/Hook) | All correct (A,B,C,D,E in order) | ✅ | Full D6 decision tree mapped correctly. | — | D6 governance decision tree |
| 472 | D6 | One sentence each: what makes SCP/conformance/FM/StackSets/SC unique? | All correct | ✅ | Block API / check+fix / firewall lifecycle / push infra / self-service+launch role. | — | D6 service differentiation |
| 473 | D6/D4 | RCP denies non-org s3:*, developer saves Principal:* bucket policy — what happens? | B: Policy saves, RCP blocks subsequent access | ✅ | RCP doesn't block PutBucketPolicy — blocks access at evaluation time. | — | RCP evaluation timing |
| 474 | D1/D6 | Detect PutBucketPolicy with Principal:* within 5 min + prevent external access — TWO? | D+A: GuardDuty + RCP | ❌ | **C+A: EventBridge on CloudTrail + RCP.** GuardDuty detects threats, not API calls. | — | EventBridge for API call detection |
| 475 | D6 | Service Catalog provisions VPC, developer removes flow logs 2 weeks later — what happens? | B: Nothing — SC doesn't monitor after provisioning | ✅ | Service Catalog = deploy only, no monitoring. | — | Service Catalog no post-deploy monitoring |
| 476 | D6 | Self-provision EC2 + auto-fix IMDSv2 + block ModifyInstanceMetadata — THREE? | A+B+C: Service Catalog + Config + SCP | ✅ | Three layers: self-service + detect/fix + prevent. | — | Layered governance |
| 477 | D6/D4 | SCP denies DeleteDetector, rogue admin in management account calls it — result? | B: Allowed — mgmt account exempt | ✅ | Management account always exempt from SCPs. | — | Management account exempt |
| 478 | D6 | Prevent member accounts from sharing resources externally via RAM — how? | D: Both SCP condition + Organizations setting work | ✅ | Two mechanisms: SCP with ram:RequestedAllowsExternalPrincipals, or org-level setting. | — | RAM external sharing controls |
| 479 | D6 | Audit Manager auto-collected evidence sources — which THREE? | A+B+C: Config + CloudTrail + Security Hub | ✅ | Auto-collected. Manual = screenshots, pen test reports. | — | Audit Manager evidence sources |
| 480 | D6 | StackSets service-managed, new account joins OU — what happens? | B: Stack instance auto-deploys (if auto-deploy enabled) | ✅ | Service-managed + auto-deploy = zero manual work. | — | StackSets auto-deploy |
| 481 | D6 | Control Tower detective guardrail "Detect S3 encryption" — what's underneath? | B: Config rule | ✅ | Detective guardrail = Config rule. Preventive = SCP. Proactive = CF Hook. | — | Control Tower guardrail internals |
| 482 | D6 | Conformance pack + Security Hub both flag unencrypted bucket — difference? | B: Conformance pack auto-fixes, Security Hub only reports | ✅ | Conformance pack has remediation. Security Hub = dashboard only. | — | Conformance pack vs Security Hub |
| 483 | D6 | Deploy Inspector across 200 accounts, auto for new — approach? | A: StackSets | ❌ | **B: Inspector delegated admin with auto-enable.** Native org support = use native, not StackSets. | — | Native org-wide deployment |
| 484 | D6 | Deploy GuardDuty across 300 accounts, auto for new — approach? | B: GuardDuty delegated admin with auto-enable | ✅ | Native org support → use native. | Q483 | Native org-wide deployment |
| 485 | D6 | Deploy GuardDuty + Config + CloudTrail + custom IAM roles, auto for new — approach? | C: StackSets + native delegated admin for each | ✅ | Mix: native for services that support it, StackSets for custom resources. | — | Hybrid deployment strategy |
| 486 | D6 | "ONE service that does everything" — which? | A: Control Tower | ❌ | **B: No single service does all.** CT doesn't share (RAM), deploy WAF (FM), or remediate (Config). | — | No single governance service |


### Session 52 — 2026-05-26

**Domains:** Cross-domain (hard drill — D1/D4/D5/D6 weak spots)
**Score:** 5 ✅ · 0 ⚠️ · 2 ❌ (71% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 487 | D1/D6 | Detect PutBucketPolicy within 5 min + prevent external access — TWO? | B+C: EventBridge + RCP | ✅ | EventBridge on CloudTrail for fast API detection + RCP for prevention. | Q474 | EventBridge for API call detection |
| 488 | D5/D4 | SCP denies kms:* unless ViaService=s3, developer calls KMS directly from CLI — result? | D: Account A's RCP blocks it | ❌ | **B: Fails — ViaService not satisfied, SCP Deny fires.** SCP follows the caller. | Q425 | kms:ViaService + SCP |
| 489 | D1 | EC2 DNS query to pool.supportxmr.com, no TCP connection — ThreatPurpose? | C: Trojan | ❌ | **B: Impact.** DNS query only = Impact. Active mining = CryptoCurrency. Active C2 = Trojan. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 490 | D3/D5 | Private subnet Lambda needs Secrets Manager + S3 SSE-KMS + CW Logs — minimum endpoints? | B: 3 | ✅ | Gateway (S3) + Interface (Secrets Mgr) + Interface (CW Logs). KMS not needed. | Q378 | VPC endpoints minimum |
| 491 | D4 | Identity=s3:*, session=GetObject only, same-account bucket policy grants role DeleteObject — result? | B: Allowed — resource-based bypasses session | ✅ | Same-account resource-based policy naming role bypasses session ceiling. | Q169 | Session policy bypass |
| 492 | D6 | Deploy Macie across 150 accounts, auto for new — approach? | D: Security Hub auto-enable | ❌ | **B: Macie delegated admin with auto-enable.** Each service manages its own org-wide deployment independently. | Q483 | Native org-wide deployment |
| 493 | D4/D5 | Global Table + MRK, reads fail eu-west-1, primary key policy correct — cause? | B: MRK replica key policy missing DynamoDB access | ✅ | MRK policies independent per region — must update each separately. | Q84 | MRK independent key policies |
| 494 | D1 | Impact finding then CryptoCurrency 30min later — what happened? | B: DNS lookup → active mining (connection established) | ✅ | Impact = DNS query. CryptoCurrency = active traffic. Two stages. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 495 | D4/D5 | SCP denies kms:Decrypt unless ViaService=s3, Lambda reads S3 object — result? | A: Fails — SCP blocks cross-account | ❌ | **B: Succeeds — ViaService = s3.us-east-1, condition FALSE, Deny doesn't fire.** | Q488 | kms:ViaService + SCP |
| 496 | D3/D1 | EC2 DNS to C2 domain — finding generated + block DNS — which TWO? | A+C: GuardDuty + DNS Firewall BLOCK | ✅ | GuardDuty for finding, DNS Firewall BLOCK for prevention. | Q295 | GuardDuty + DNS Firewall complementary |
| 497 | D6/D4 | SCP denies ScheduleKeyDeletion, member vs management account — results? | C: Member denied, management allowed | ✅ | Management account exempt from SCPs. | — | Management account exempt |
| 498 | D5 | Rotation completes, new Lambda auth fails on RDS, ECS works — cause? | B: Rotation Lambda failed to update DB password | ✅ | Secret changed but DB didn't. ECS uses old connection (AWSPREVIOUS). | Q376 | Secrets Manager rotation failure |
| 499 | D4 | RCP denies non-org s3:*, ELB SLR + CloudTrail + external attacker — which succeed? | B: SLR + CloudTrail only | ✅ | SLR exempt (structural) + CloudTrail exempt (PrincipalIsAWSService). Attacker blocked. | Q217 | RCP exemptions (both paths) |
| 494 | D1 | Impact finding then CryptoCurrency 30min later — what happened? | B: DNS lookup → active mining (connection established) | ✅ | Impact = DNS query. CryptoCurrency = active traffic. Two stages. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 495 | D4/D5 | SCP denies kms:Decrypt unless ViaService=s3, Lambda reads S3 object — result? | A: Fails — SCP blocks cross-account | ❌ | **B: Succeeds — ViaService = s3.us-east-1, condition FALSE, Deny doesn't fire.** | Q488 | kms:ViaService + SCP |
| 496 | D3/D1 | EC2 DNS to C2 domain — finding generated + block DNS — which TWO? | A+C: GuardDuty + DNS Firewall BLOCK | ✅ | GuardDuty for finding, DNS Firewall BLOCK for prevention. | Q295 | GuardDuty + DNS Firewall complementary |
| 497 | D6/D4 | SCP denies ScheduleKeyDeletion, member vs management account — results? | C: Member denied, management allowed | ✅ | Management account exempt from SCPs. | — | Management account exempt |
| 498 | D5 | Rotation completes, new Lambda auth fails on RDS, ECS works — cause? | B: Rotation Lambda failed to update DB password | ✅ | Secret changed but DB didn't. ECS uses old connection (AWSPREVIOUS). | Q376 | Secrets Manager rotation failure |
| 499 | D4 | RCP denies non-org s3:*, ELB SLR + CloudTrail + external attacker — which succeed? | B: SLR + CloudTrail only | ✅ | SLR exempt (structural) + CloudTrail exempt (PrincipalIsAWSService). Attacker blocked. | Q217 | RCP exemptions (both paths) |
| 500 | D4/D5 | Cross-account KMS + ViaService SCP + session policy only s3:GetObject — Lambda reads encrypted S3? | B: Succeeds — S3 calls KMS server-side, session policy doesn't block | ✅ | Role has kms:Decrypt + ViaService satisfied + session ceiling doesn't apply to server-side KMS. | — | Session policy + ViaService + server-side KMS |
| 501 | D3/D4 | Verified Access: stolen laptop, block only that device — action? | B: Mark device non-compliant in CrowdStrike | ✅ | Device trust provider = surgical device block. | Q336 | Verified Access trust providers |
| 502 | D1/D2 | Trojan finding severity 8.7 — stop + preserve + investigate 72hr — sequence? | B: Deny-all SG → EBS snapshot → Detective | ✅ | Isolate → preserve → investigate. Never terminate. | — | IR sequence + Detective |
| 503 | D5/D4 | Key policy grants root only, Lambda only has s3:GetObject (no kms:Decrypt) — reads encrypted object? | C: Succeeds — S3 handles server-side | ❌ | **B: Fails — Lambda needs explicit kms:Decrypt.** Root = delegation, not grant. | Q264 | KMS key policy root = delegation, not grant |
| 504 | D6 | Security Hub + GuardDuty + custom IAM role across 300 accounts — how many mechanisms? | C: 3 (SH native + GD native + StackSets for IAM role) | ✅ | Native for services that support it, StackSets for custom resources. | Q485 | Hybrid deployment strategy |
| 505 | D4/D5 | SCP denies kms:* unless ViaService=s3 — which TWO calls succeed? | A+C: Lambda via S3 read + Lambda via S3 upload | ✅ | ViaService set when S3 calls KMS on behalf of caller. Direct CLI = no ViaService = denied. | Q488 | kms:ViaService + SCP |


### Session 53 — 2026-05-26

**Domains:** Cross-domain (re-test + killer uplift — all domains)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 506 | D4/D5 | SCP denies kms:Decrypt unless ViaService=s3, developer calls KMS directly from CLI — result? | B: Denied — ViaService not satisfied | ✅ | Direct call has no ViaService context → SCP Deny fires. | Q488, Q495 | kms:ViaService + SCP |
| 507 | D1 | EC2 DNS query to xmr.pool.minergate.com, no TCP connection — ThreatPurpose? | B: Impact | ✅ | DNS query only = Impact. Active mining = CryptoCurrency. | Q489 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 508 | D5/D4 | Key policy grants root only, Lambda has s3:GetObject but no kms:Decrypt — reads SSE-KMS object? | B: Fails — needs explicit kms:Decrypt | ✅ | Root = delegation, not grant. Each principal needs explicit KMS perms. | Q503 | KMS key policy root = delegation, not grant |
| 509 | D4/D6 | RCP denies non-org sts:AssumeRole, external partner has trust policy — result? | B: Denied by RCP | ✅ | RCP blocks external AssumeRole regardless of trust policy. | — | RCP blocks external AssumeRole |
| 510 | D3/D5 | Lambda private subnet, monitoring endpoint exists, PutMetricData times out — cause? | A: Endpoint SG missing inbound HTTPS from Lambda SG | ✅ | Timeout = network. Interface endpoint SG must allow inbound 443. | Q418 | Timeout vs Access Denied (SG troubleshooting) |
| 511 | D1/D2 | Trojan:EC2/DropPoint!DNS severity 8.4, contain + preserve + keep API available — sequence? | B: Deny-all SG → EBS snapshot → deregister from ALB | ✅ | Isolate first → preserve evidence → remove from traffic. | — | IR sequence + ALB |
| 512 | D6 | DNS FW rule groups: share from security account + enforce on all VPCs + auto-remediate — which TWO? | A+B: RAM + Firewall Manager | ✅ | RAM shares, FM enforces + auto-remediates. | Q441, Q442 | RAM for sharing + FM for enforcing |
| 513 | D4 | Identity=s3:*+kms:*, boundary=s3:*+ec2:*, session=Get+Put, same-account bucket policy grants role DeleteObject — result? | C: Allowed — resource-based bypasses session | ✅ | Same-account resource-based policy naming role bypasses session + boundary ceiling. | Q169 | Session policy bypass by resource-based policy |
| 514 | D5/D3 | CloudFront + S3 + OAC + SSE-KMS, Access Denied — what's missing? | B: KMS key policy must grant kms:Decrypt to cloudfront.amazonaws.com | ✅ | OAC needs explicit KMS permission for CF service principal. | — | OAC + KMS key policy |
| 515 | D1/D6 | Prevent PutBucketPolicy with Principal:* + detect within 5 min — which TWO? | A+C: SCP + EventBridge | ❌ | **C+D: EventBridge + RCP.** SCP can't inspect API payload content. RCP prevents the consequence (external access). | Q474 | SCP can't inspect payload + RCP prevents consequence |


### Session 54 — 2026-05-26

**Domains:** Cross-domain (killer uplift — hard novel scenarios)
**Score:** 12 ✅ · 0 ⚠️ · 3 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 516 | D4/D5 | SCP denies kms:Decrypt+GenerateDataKey unless ViaService=s3 or secretsmanager, Lambda does 3 ops — which succeed? | B: Only S3 read + GetSecretValue | ✅ | ViaService set by S3 and SM. Direct kms:Decrypt has no ViaService → denied. | Q506 | kms:ViaService + SCP (multiple services) |
| 517 | D6/D4 | SCP denies ScheduleKeyDeletion, member admin + member root + management admin — which denied? | B: Only member admin + member root | ✅ | Management account exempt from SCPs. SCPs apply to member root. | — | Management account exempt |
| 518 | D1/D4 | Bucket policy grants external account, external downloads nightly — which services generate findings? | A: Only GuardDuty | ❌ | **C: Both Access Analyzer + GuardDuty.** AA flags external access (static). GD flags anomalous pattern (dynamic). | — | Access Analyzer + GuardDuty both fire |
| 519 | D5 | Rotation successful, new Lambda Access Denied on RDS, ECS works — cause? | B: Rotation Lambda failed ALTER USER on DB | ✅ | Secret changed but DB didn't. ECS uses AWSPREVIOUS. | Q376 | Secrets Manager rotation failure |
| 520 | D3/D6 | WAF on ALBs + DNS FW on VPCs, both via FM — which needs RAM? | B: Only DNS Firewall | ✅ | FM creates WAF directly. DNS FW rule group exists in another account → RAM shares first. | — | FM creates WAF directly, needs RAM for DNS FW |
| 521 | D4 | RCP denies non-org s3:*, same-org Account B Lambda PutObject to Account A bucket — result? | B: Allowed — PrincipalOrgID matches | ✅ | Same-org caller → condition FALSE → Deny doesn't fire. | Q427 | RCP same-org evaluation |
| 522 | D3/D5 | Lambda private subnet, direct kms:Decrypt from code, no KMS endpoint — result? | B: Add Interface endpoint for KMS + SG inbound 443 | ✅ | Direct KMS call needs network path. S3 SSE-KMS is server-side (no endpoint needed). | — | KMS endpoint needed for direct calls only |
| 523 | D1/D6 | Detect DeleteTrail/StopLogging within 2 min + auto-revert — architecture? | A: Config rule with auto-remediation | ❌ | **B: EventBridge in management account → Lambda.** Near real-time. Config is slower. | Q401 | EventBridge for fast detection + auto-revert |
| 524 | D4/D3 | Cognito per-user S3, pen tester crafts request to other user's prefix — result? | B: Fails — IAM policy restricts to caller's sub | ✅ | Policy variable resolves to caller's identity, not requested path. | — | Cognito per-user isolation |
| 525 | D5 | 7yr immutable + root can't delete + auto-expire + lawsuit preservation beyond 7yr — config? | A: Compliance mode + Legal Hold on lawsuit records | ✅ | Compliance = fixed period. Legal Hold = indefinite for litigation. | — | Object Lock Compliance + Legal Hold |
| 526 | D3/D1 | Trojan:EC2/C2Activity.B — block C2 VPC-wide + continue monitoring other instances — approach? | A: DNS Firewall BLOCK | ❌ | **B: Network Firewall DROP on C2 IP + GuardDuty continues.** C2Activity = active IP connection. DNS FW useless if IP hardcoded. | — | Network FW for IP-level C2 block |
| 527 | D4/D6 | SCP forces boundary, dev attaches AdministratorAccess, calls ec2:RunInstances — result? | B: Denied — boundary doesn't include ec2 | ✅ | Boundary = ceiling. ec2 not in boundary = denied regardless of identity policy. | — | Permission boundary delegation |
| 528 | D1 | Correlate GD + VPC Flow + WAF, SQL, own S3, single schema, SIEM reads — service? | B: Security Lake | ✅ | Multiple sources + OCSF + your S3 + subscriber model = Security Lake. | — | Security Lake |
| 529 | D4/D5 | Identity has kms:Decrypt, session policy only s3:GetObject, reads SSE-KMS object — result? | B: Succeeds — server-side KMS not gated by session policy | ✅ | Session policy gates caller's direct calls, not S3's internal KMS call. | — | Session policy + server-side KMS |
| 530 | D6 | CF template must include StorageEncrypted + DeletionProtection, fail before creation — guardrail type? | C: Proactive (CF Hook) | ✅ | "Validate template content before deploy" = CF Hook. SCP can't see template. | Q464 | Proactive guardrail (CF Hook) |


### Session 55 — 2026-05-26

**Domains:** Cross-domain (killer difficulty — multi-concept combos)
**Score:** 7 ✅ · 0 ⚠️ · 3 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 531 | D4/D5/D6 | SCP ViaService + RCP + key policy root + session policy — Lambda reads SSE-KMS object? | C: Succeeds — server-side KMS, ViaService satisfied | ✅ | Session policy doesn't gate server-side KMS. ViaService satisfied. Root enables delegation. | — | Full stack evaluation |
| 532 | D1/D3/D6 | Block DNS + detect C2 TCP + auto-block IP + org-wide — which FOUR? | C: DNS FW + Inspector + NF + StackSets | ❌ | **A: DNS FW + GuardDuty + Network FW + EventBridge→Lambda.** Inspector detects CVEs not C2. WAF can't block raw TCP. | — | Detection + response architecture |
| 533 | D4/D5 | Cross-account S3+KMS, SCP ViaService, Lambda reads via S3 — result? | A: Succeeds — ViaService satisfied cross-account | ✅ | ViaService set by S3 regardless of account boundary. | — | kms:ViaService cross-account |
| 534 | D1/D4/D6 | External trust policy + RCP + GuardDuty + Access Analyzer + EventBridge — which THREE true? | A+B+C | ❌ | **A+B+D.** GuardDuty doesn't fire on blocked AssumeRole attempts. EventBridge fires on CreateRole API call. | — | GuardDuty ≠ failed attempts |
| 535 | D5/D4/D3 | Secret works, S3 upload Access Denied, all IAM correct — cause? | D: KMS endpoint SG blocks | ❌ | **C: S3 Gateway endpoint policy denies PutObject.** Access Denied = permissions (endpoint policy), not network (timeout). | — | Gateway endpoint policy as additional gate |
| 536 | D1/D2/D4 | InstanceCredentialExfiltration.OutsideAWS — stop attacker + keep instance + new creds work? | B: Inline Deny TokenIssueTime | ✅ | Exfiltrated creds denied. IMDS refreshes new creds after timestamp. Instance stays up. | — | Credential exfiltration response |
| 537 | D6/D3/D4 | Prevent IMDSv1 + detect/fix existing + baseline SG + share NF policy — which FOUR? | A: SCP + Config/SSM + FM SG common + RAM | ✅ | SCP prevents. Config fixes. FM common creates SG. RAM shares NF policy. | — | Full governance stack |
| 538 | D5/D4 | Cross-account KMS, key policy grants Account B root, identity policy has Decrypt — result? | A: Succeeds — both sides grant | ✅ | Root in key policy enables IAM delegation in Account B. Both sides satisfied. | — | Cross-account KMS standard pattern |
| 539 | D1/D6 | CIS score + GD findings + Inspector CVEs + custom metric, least overhead — service? | B: Security Hub | ✅ | Aggregates all + CIS standard + cross-region + one-click org-wide. | — | Security Hub aggregation |
| 540 | D4/D3/D5 | Cross-account S3+KMS + SCP ViaService + RCP + session policy — Lambda reads? | B: Succeeds — all gates pass | ✅ | ViaService satisfied, RCP same-org passes, session doesn't gate server-side KMS. | — | 5-layer cross-account evaluation |


### Session 56 — 2026-05-28
**Score:** 11 ✅ · 1 ⚠️ · 3 ❌ (73% correct)
**Score:** 3 ✅ · 1 ⚠️ · 1 ❌ (60% correct)
**Score:** 2 ✅ · 0 ⚠️ · 1 ❌ (67% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 541 | D4/D5 | RCP + SCP ViaService + key policy grants only Account A root + Lambda in Account B reads SSE-KMS object cross-account — result? | A: Succeeds — all gates pass | ❌ | **C: Fails — key policy grants only Account A root, doesn't name Account B. Cross-account KMS requires key policy to explicitly name external account.** Root enables IAM delegation same-account only. | Q264, Q503 | Cross-account KMS key policy must name external account |
| 542 | D4/D5 | SCP ViaService + session policy (s3:Get+sm:Get only) + same-account SSE-KMS — 3 ops: S3 read, SM GetSecret, direct kms:Decrypt — which succeed? | B: Only #1 and #2 — ViaService satisfied, direct Decrypt has no ViaService | ✅ | Direct kms:Decrypt has no ViaService context → SCP Deny fires. Server-side KMS calls by S3/SM satisfy ViaService and aren't gated by session policy. | Q488, Q495 | kms:ViaService + SCP |
| 543 | D1/D3/D6 | 3 GD findings (Impact→CryptoCurrency→Trojan), block DNS org-wide + block C2 IP + detect mining — which THREE? | A+B+C: GuardDuty + RAM+FM DNS FW + Network FW via FM | ✅ | GD detects (zero code). RAM+FM shares+enforces DNS rules org-wide. Network FW drops hardcoded C2 IPs (DNS FW useless if no DNS query). | — | Detection + response architecture + RAM/FM complementary |
| 544 | D4/D5 | Session policy=GetObject only, same-account bucket policy grants role DeleteObject, SSE-KMS object — DeleteObject result? | B: Succeeds — resource-based bypasses session, DeleteObject doesn't need KMS | ✅ | Same-account resource policy naming role bypasses session ceiling. DeleteObject doesn't call KMS (no decrypt needed for deletion). | Q96, Q169 | Session policy bypass + DeleteObject no KMS |
| 545 | D1/D4/D5 | RCP blocks external + Access Analyzer + GuardDuty + KMS key policy — which THREE true? | A+B+F | ⚠️ | **A+B+E.** RCP blocks (A). AA fires on policy (B). GuardDuty doesn't fire on blocked attempts — no successful access = no finding (E). F is factually true but E is the exam-critical insight. | Q518, Q534 | GuardDuty ≠ failed attempts + Access Analyzer static analysis |
| 546 | D1 | SSE-KMS bucket, CISO wants to KNOW when external decrypts, least overhead? | A: CloudTrail data events + metric filter | ❌ | **C: GuardDuty S3 Protection.** "Detect/alert" + "least overhead" = GuardDuty. CloudTrail is the log source, not the detection engine. | Q100, Q105, Q153 | Detect vs prevent (GuardDuty vs policy) |
| 547 | D1 | EC2 resolves pool.minexmr.com via DNS, no TCP connection — ThreatPurpose? | B: Impact | ✅ | DNS query only = Impact. Active mining = CryptoCurrency. | Q226, Q489 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 548 | D1 | RCP blocks non-org s3:*, external tries GetObject, GuardDuty enabled — what's true? | B: GuardDuty does NOT generate finding — blocked = no successful access | ✅ | GuardDuty fires on successful anomalous access only. Blocked attempts = no finding. | Q534 | GuardDuty ≠ failed attempts |
| 549 | D1 | Detect PutBucketPolicy with Principal:* within 5 min, org trail exists, least overhead? | A: GuardDuty | ❌ | **C: EventBridge rule in management account.** "Detect specific API call" = EventBridge. GuardDuty detects behavior, not API calls. | Q474, Q523 | EventBridge for API call detection |
| 550 | D1 | EC2 actively sending mining traffic (TCP established, data flowing) — ThreatPurpose? | B: CryptoCurrency | ✅ | Active mining traffic = CryptoCurrency. DNS query only = Impact. | Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 551 | D6 | DNS FW rule group needs to be VISIBLE to 200 members — which service? | B: RAM | ✅ | "Visible/accessible/share" = RAM. | Q441 | RAM for sharing vs FM for enforcing |
| 552 | D6 | DNS FW rule group must be ASSOCIATED with every VPC, re-associated if removed — which? | B: Firewall Manager | ✅ | "Enforce/associate/re-apply" = FM. | Q442 | RAM + FM complementary |
| 553 | D6 | StackSets deployed Config, developer stops recorder — what happens? | B: Nothing — StackSets doesn't auto-remediate | ✅ | StackSets deploys but never auto-remediates. Use SCP to prevent. | Q283, Q439 | StackSets no auto-remediation |
| 554 | D6 | Deploy Macie across 150 accounts, auto for new — approach? | B: Macie delegated admin with auto-enable | ✅ | Native org support = use native, not StackSets. | Q483, Q492 | Native org-wide deployment |
| 555 | D6 | WAF on all ALBs, auto-apply new accounts, re-attach if removed — which service? | B: Firewall Manager | ✅ | FM creates WAF directly (no RAM) + auto-remediates. | Q284, Q435 | Firewall Manager auto-remediation |


### Session 57 — 2026-05-28

**Domains:** Cross-domain (killer exam set — all red-priority weak areas)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 556 | D1 | GuardDuty zero findings 6 months, active workloads, VPC Flow Logs enabled — cause? | D: Suppression rule | ✅ | Suppression rule archiving findings. GD reads Flow Logs internally. | Q372, Q389 | GuardDuty suppression rules |
| 557 | D1/D6 | Detect PutBucketPolicy Principal:* within 2 min + prevent external access — which TWO? | C+D: EventBridge + RCP | ✅ | EventBridge for fast API detection + RCP prevents consequence. | Q474, Q549 | EventBridge for API call detection + RCP |
| 558 | D1 | EC2 resolves pool.supportxmr.com via DNS, no TCP connection — ThreatPurpose? | B: Impact | ✅ | DNS query only = Impact. Active mining = CryptoCurrency. | Q226, Q489 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 559 | D4/D5 | Cross-account S3+KMS, key policy grants only Account A root, Account B has kms:Decrypt — result? | B: Fails — key policy must name external account | ✅ | Root enables IAM delegation same-account only. Cross-account needs explicit grant. | Q541 | Cross-account KMS key policy must name external account |
| 560 | D4 | Identity=s3:*, boundary=s3:*+ec2:*, session=Get+Put, same-account bucket policy grants Delete — result? | C: Allowed — resource-based bypasses session | ✅ | Same-account resource policy naming role bypasses session + boundary ceiling. | Q96, Q169 | Session policy bypass by resource-based policy |
| 561 | D6 | Deploy Macie across 200 accounts, auto for new — approach? | B: Macie delegated admin with auto-enable | ✅ | Native org support = use native, not StackSets. | Q483, Q492 | Native org-wide deployment |
| 562 | D6 | RAM shares DNS FW rule group, developer disassociates from VPC — what happens? | A: Nothing — RAM doesn't enforce | ❌ | **C: Firewall Manager re-associates automatically.** RAM shares, FM enforces. Full pattern assumed. | Q313, Q441 | RAM for sharing vs FM for enforcing |
| 563 | D6 | Prevent disabling Config, junior suggests Config rule — why won't it work? | A: Config can't evaluate its own service — use SCP | ✅ | Config can't remediate its own disablement. SCP prevents the API call. | Q440 | SCP prevents disabling services |
| 564 | D4/D5 | SCP denies kms:Decrypt unless ViaService=s3, Lambda reads S3 + dev calls KMS directly — which succeed? | B: Only S3 read — ViaService satisfied | ✅ | Direct CLI has no ViaService context → SCP Deny fires. S3 sets ViaService. | Q488, Q495 | kms:ViaService + SCP |
| 565 | D3/D6 | Share NF policy + enforce on VPCs + auto-recreate if deleted — which TWO? | A+B: RAM + Firewall Manager | ✅ | RAM shares, FM enforces lifecycle + auto-remediates. | Q442, Q446 | RAM + FM complementary |


### Session 58 — 2026-05-28

**Domains:** D1 Detection + D6 Governance (targeted drill — detect vs prevent + RAM/FM)
**Score:** 6 ✅ · 0 ⚠️ · 4 ❌ (60% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 566 | D6 | RAM shares DNS FW rule group, FM enforces, developer disassociates — what happens? | B: FM re-associates automatically | ✅ | FM auto-remediates. RAM shares, FM enforces. | Q562 | RAM for sharing vs FM for enforcing |
| 567 | D6 | RAM share deleted, FM policy still exists — what happens? | B: FM policy non-compliant, rule group inaccessible | ✅ | RAM is the foundation. Remove share → FM can't enforce what doesn't exist. | Q562 | RAM + FM dependency |
| 568 | D1 | SSE-KMS, detect when external account successfully decrypts, least overhead? | A: CloudTrail + metric filter | ❌ | **C: GuardDuty S3 Protection.** "Detect" + "least overhead" = GuardDuty. CloudTrail is the log source, not the detection engine. | Q100, Q546 | Detect vs prevent (GuardDuty vs policy) |
| 569 | D5/D4 | Block external decryption org-wide? | B: RCP denying non-org kms:Decrypt | ✅ | "Block" + "org-wide" = RCP. | Q369 | RCP for prevention |
| 570 | D1 | Detect DeleteTrail within 2 min, org trail exists, least overhead? | A: GuardDuty | ❌ | **C: EventBridge rule in management account.** "Detect specific API call" + "fast" = EventBridge. | Q474, Q549 | EventBridge for API call detection |
| 571 | D1 | EC2 communicating with known C2 IP, alert with zero custom code? | D: Network Firewall alert | ❌ | **C: GuardDuty.** "Detect" + "zero custom code" = always GuardDuty. NF requires deployment + rules. | Q159 | Detect C2 = GuardDuty (zero code) |
| 572 | D3 | Block C2 IP VPC-wide, attacker hardcoded IP (no DNS)? | C: Network Firewall DROP | ✅ | DNS FW useless if no DNS query. Network FW drops by IP. | Q526 | Network FW for IP-level C2 block |
| 573 | D1 | Bucket policy grants external account, no access yet — which service fires? | B: Only Access Analyzer | ✅ | AA = static policy analysis (fires on policy). GD = needs actual access. | Q518 | Access Analyzer + GuardDuty both fire |
| 574 | D1 | Detect DeleteDetector within 1 min, org trail exists? | B: Config rule | ❌ | **C: EventBridge.** "Detect specific API" + "within 1 min" = EventBridge. Config is slower. | Q474, Q549 | EventBridge for API call detection |
| 575 | D1 | Detect PutBucketPolicy within 2 min, org trail exists, least overhead? | C: EventBridge | ✅ | "Specific API call" + "fast" + "least overhead" = EventBridge. | Q474 | EventBridge for API call detection |


### Session 59 — 2026-05-28

**Domains:** D1 Detection (targeted drill — GuardDuty S3 Protection vs EventBridge vs Access Analyzer)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 576 | D1 | Unusual download patterns from unknown country, alert, least overhead? | B: GuardDuty S3 Protection | ✅ | Anomalous access pattern = GuardDuty S3 Protection. | Q568 | Detect vs prevent (GuardDuty vs policy) |
| 577 | D1 | PutBucketPolicy with Principal:*, alert within 2 min? | B: EventBridge | ✅ | Specific API call + fast = EventBridge. | Q574 | EventBridge for API call detection |
| 578 | D1 | External account downloading hundreds of objects at 3 AM, zero setup? | C: GuardDuty S3 Protection | ✅ | Exfiltration + anomalous + zero setup = GuardDuty. | Q568 | Detect vs prevent (GuardDuty vs policy) |
| 579 | D1 | Bucket policy grants external access, no access yet — which service? | B: Access Analyzer | ✅ | Static policy analysis, no access needed = Access Analyzer. | Q573 | Access Analyzer + GuardDuty both fire |
| 580 | D1 | External account downloads from unusual geo + unusual time, least overhead? | C: GuardDuty S3 Protection | ✅ | Anomalous behavior on data access = GuardDuty S3 Protection. | Q568 | Detect vs prevent (GuardDuty vs policy) |


### Session 60 — 2026-05-30

**Domains:** D1 Detection + D6 Governance (re-test blitz — top 3 red-priority gaps)
**Score:** 8 ✅ · 0 ⚠️ · 2 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 581 | D1 | SSE-KMS, alert when external decrypts, least overhead? | D: EventBridge rule on kms:Decrypt | ❌ | **C: GuardDuty S3 Protection.** "Detect anomalous data access" + "least overhead" = GuardDuty. EventBridge is for specific API calls, not behavioral analysis. | Q568, Q546 | Detect vs prevent (GuardDuty vs policy) |
| 582 | D1 | Detect DeleteTrail/StopLogging within 2 min, org trail exists, least overhead? | C: EventBridge rule in management account | ✅ | "Detect specific API call" + "fast" + "org trail" = EventBridge. | Q570, Q574 | EventBridge for API call detection |
| 583 | D6 | DNS FW rule group: share to 200 accounts + re-associate if removed — which TWO? | A+B: RAM + Firewall Manager | ✅ | RAM shares, FM enforces + auto-remediates. | Q562, Q441 | RAM for sharing vs FM for enforcing |
| 584 | D1 | EC2 communicating with known C2 IP, alert, zero custom code, zero infra? | B: Network Firewall alert rule | ❌ | **C: GuardDuty.** "Zero custom code" + "zero infrastructure" = always GuardDuty. NF requires deployment. | Q571 | Detect C2 = GuardDuty (zero code) |
| 585 | D6 | WAF on all ALBs, auto-apply new accounts, re-attach if removed — which service? | B: Firewall Manager only | ✅ | FM creates WAF directly (no RAM needed) + auto-remediates. | Q435, Q284 | Firewall Manager auto-remediation |
| 586 | D1 | PutBucketPolicy with Principal:*, detect within 2 min, org trail exists? | C: EventBridge rule in management account | ✅ | "Specific API call" + "fast" = EventBridge. | Q549, Q574 | EventBridge for API call detection |
| 587 | D1/D5 | Prevent external S3 access org-wide + detect anomalous attempts — which TWO? | B+C: RCP + GuardDuty S3 Protection | ✅ | RCP prevents, GuardDuty detects. | Q369, Q568 | Detect vs prevent (RCP + GuardDuty) |
| 588 | D1 | EC2 DNS query to pool.minexmr.com, no TCP connection — ThreatPurpose? | B: Impact | ✅ | DNS query only = Impact. Active mining = CryptoCurrency. | Q489, Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 589 | D6 | Deploy Macie across 150 accounts, auto for new — approach? | B: Macie delegated admin with auto-enable | ✅ | Native org support = use native, not StackSets. | Q492, Q483 | Native org-wide deployment |
| 590 | D1 | External account downloads objects, unusual geo + time, least overhead? | C: GuardDuty S3 Protection | ✅ | "Anomalous behavior" + "least overhead" = GuardDuty S3 Protection. | Q568, Q546 | Detect vs prevent (GuardDuty vs policy) |


### Session 61 — 2026-05-30

**Domains:** Cross-domain killer exam simulation (all domains, hardest scenarios)
**Score:** 7 ✅ · 0 ⚠️ · 3 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 591 | D4/D5/D6 | SCP ViaService + RCP same-org + session policy + key policy grants B root + server-side KMS — Lambda reads cross-account SSE-KMS? | A: Fails — session policy doesn't include kms:Decrypt | ❌ | **C: Succeeds — ViaService satisfied, RCP same-org passes, session policy doesn't gate server-side KMS.** Session policy only restricts caller's direct calls. | Q529, Q531 | Session policy + server-side KMS |
| 592 | D1/D3/D6 | 3 GD findings (Impact→CryptoCurrency→Trojan), block DNS + block C2 IP + detect — which THREE? | A+B+C: DNS FW (RAM+FM) + Network FW (RAM+FM) + GuardDuty | ✅ | GD detects. RAM+FM shares+enforces DNS rules. Network FW drops C2 IPs. | Q532, Q543 | Detection + response architecture |
| 593 | D4/D5 | Cross-account PutObject SSE-KMS, session policy=Get+Put only, boundary=s3:*+kms:* — succeeds? | D: Succeeds — session policy doesn't gate server-side KMS | ✅ | S3 calls GenerateDataKey server-side. Session policy gates caller's direct calls only. | Q529, Q531 | Session policy + server-side KMS |
| 594 | D1/D4/D5 | RCP blocks external + AA + GD enabled + attacker attempts GetObject for 3 days — which TWO true? | A+C: RCP blocks + GuardDuty fires | ❌ | **A+B: RCP blocks + Access Analyzer fires (on policy).** GuardDuty doesn't fire on blocked attempts — no successful access = no finding. | Q534, Q545 | GuardDuty ≠ failed attempts |
| 595 | D5/D3 | Lambda private subnet, Secrets Manager works, S3 PutObject Access Denied, Gateway endpoint exists — cause? | A: Gateway endpoint policy doesn't allow PutObject | ✅ | Access Denied = permissions. Endpoint policy is additional gate. Secrets Manager working = network fine. | Q535 | Gateway endpoint policy as additional gate |
| 596 | D6/D3/D4 | Prevent IMDSv1 + detect/fix existing + baseline SG + share NF policy — which FOUR? | A+B+C+D: SCP + Config/SSM + FM SG common + RAM | ✅ | SCP prevents. Config fixes. FM common creates SG. RAM shares NF policy. | Q537 | Full governance stack |
| 597 | D5/D4 | Key policy grants only Account A root, Lambda in Account A has s3:GetObject but no kms:Decrypt — reads SSE-KMS object? | B: Fails — needs explicit kms:Decrypt | ✅ | Root = delegation, not grant. Each principal needs explicit KMS perms. | Q503, Q508 | KMS key policy root = delegation, not grant |
| 598 | D2/D4 | InstanceCredentialExfiltration.OutsideAWS, stop attacker + instance stays up + fresh creds work — single action? | B: Inline Deny TokenIssueTime | ✅ | Deny old creds, IMDS refreshes new ones after timestamp. | Q536 | Credential exfiltration response |
| 599 | D4/D5 | Cross-account KMS, key policy grants B root, Account B SCP denies kms:* unless ViaService=s3, Lambda calls Decrypt directly — result? | B: Fails — ViaService not satisfied, SCP Deny fires | ✅ | Direct call has no ViaService context. SCP follows the caller. | Q488, Q506 | kms:ViaService + SCP |
| 600 | D1/D6 | Prevent DeleteTrail/StopLogging + detect PutBucketPolicy 2min + prevent external S3 + alert anomalous downloads — match FOUR services | A+B+C+D: SCP + EventBridge + RCP + GuardDuty | ✅ | SCP prevents API. EventBridge detects API. RCP prevents consequence. GuardDuty detects behavior. | Q557, Q587 | Full detect/prevent architecture |


### Session 62 — 2026-05-30

**Domains:** D1 Detection + D6 Governance (killer targeted drill — all red-priority gaps)
**Score:** 10 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 601 | D1 | RCP blocks external + GuardDuty S3 Protection enabled + attacker attempts 50 GetObjects (all denied) — did GuardDuty alert? | B: No — GD only fires on successful anomalous access | ✅ | GuardDuty doesn't fire on blocked attempts — no successful access = no finding. | Q534, Q594 | GuardDuty ≠ failed attempts |
| 602 | D1/D6 | Detect PutBucketPolicy Principal:* within 2 min + prevent external access — which TWO? | B: EventBridge + RCP | ✅ | EventBridge for fast API detection + RCP prevents consequence. | Q474, Q549 | EventBridge for API call detection + RCP |
| 603 | D1 | EC2 actively sending TCP traffic to mining pool (connection established, data flowing) — ThreatPurpose? | B: CryptoCurrency | ✅ | Active mining traffic = CryptoCurrency. DNS query only = Impact. | Q226, Q489 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 604 | D1 | Same instance 10min earlier, resolved pool.minexmr.com via DNS, no TCP connection — ThreatPurpose? | B: Impact | ✅ | DNS query only = Impact. Active mining = CryptoCurrency. | Q226, Q489 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 605 | D3/D1 | Trojan:EC2/C2Activity.B!DNS, attacker hardcoded C2 IP, no DNS queries — block VPC-wide? | B: Network Firewall DROP on C2 IP | ✅ | IP hardcoded = DNS FW useless. Network FW drops by IP. | Q526, Q571 | Network FW for IP-level C2 block |
| 606 | D1 | Detect DeleteDetector/StopLogging within 1 min, org trail exists, least overhead? | C: EventBridge rule in management account | ✅ | "Detect specific API call" + "fast" = EventBridge. | Q474, Q570 | EventBridge for API call detection |
| 607 | D6 | Prevent DeleteDetector/StopLogging from ever happening — mechanism? | B: SCP denying those actions | ✅ | "Prevent" = SCP. EventBridge detects. Config remediates. | Q440, Q467 | SCP prevents disabling services |
| 608 | D6 | DNS FW rule groups: share + associate all VPCs + auto-re-associate — which TWO? | A: RAM + Firewall Manager | ✅ | RAM shares, FM enforces + auto-remediates. | Q441, Q562 | RAM for sharing + FM for enforcing |
| 609 | D1/D5 | Prevent external decryption + alert anomalous downloads — which TWO? | B+C: RCP + GuardDuty S3 Protection | ✅ | RCP prevents, GuardDuty detects anomalous behavior. | Q568, Q581 | Detect vs prevent (RCP + GuardDuty) |
| 610 | D6 | Developer deploys Inspector via StackSets — why is this wrong? | B: Inspector has native delegated admin with auto-enable | ✅ | Native org support = use native, not StackSets. | Q483, Q492 | Native org-wide deployment |


### Session 63 — 2026-05-30

**Domains:** Cross-domain killer (session policy + server-side KMS + cross-account + RCP + ViaService)
**Score:** 10 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 611 | D4/D5 | Cross-account SSE-KMS, key policy grants only Account A root, Lambda in B has kms:Decrypt, SCP ViaService, RCP same-org, session=GetObject — result? | B: Fails — key policy doesn't name Account B | ✅ | Cross-account KMS requires key policy to explicitly name external account. Root enables delegation same-account only. | Q541, Q559 | Cross-account KMS key policy must name external account |
| 612 | D4/D5 | Same as Q611 but key policy now grants Account B root — result? | C: Succeeds — server-side KMS, ViaService satisfied, session doesn't gate | ✅ | All 5 layers pass. S3 calls KMS server-side, ViaService satisfied, session policy doesn't gate server-side KMS. | Q591, Q531 | Session policy + server-side KMS + ViaService |
| 613 | D4 | Cross-account bucket policy grants role DeleteObject, session=Get+Put only — DeleteObject? | A: Denied — session policy ceiling applies cross-account | ✅ | Resource-policy bypass of session policy ONLY works same-account. Cross-account = ceiling always applies. | Q96, Q169 | Session policy bypass same-account ONLY |
| 614 | D4 | Same-account bucket policy grants role DeleteObject, session=Get+Put only — DeleteObject? | B: Allowed — same-account resource-based bypasses session | ✅ | Same-account resource-based policy naming role bypasses session policy ceiling. | Q96, Q169 | Session policy bypass by resource-based policy |
| 615 | D4/D5 | SCP denies kms:Decrypt+GenerateDataKey unless ViaService=s3 or secretsmanager — S3 read + SM GetSecret + direct Decrypt — which succeed? | B: Only #1 and #2 | ✅ | S3 and SM set ViaService server-side. Direct kms:Decrypt has no ViaService → SCP Deny fires. | Q488, Q506 | kms:ViaService + SCP (multiple services) |
| 616 | D4/D5 | Cross-account SSE-KMS, all correct, key policy grants B root, still Access Denied — cause? | A: RCP denies non-org kms:Decrypt | ✅ | RCP is the hidden gate. Key policy granting root IS sufficient for cross-account (enables delegation). | Q541, Q568 | RCP as hidden gate for cross-account KMS |
| 617 | D1/D4 | Bucket policy grants external account, no access yet — which services fire? (TWO) | A+C: Access Analyzer fires (static) + GuardDuty does NOT (no access) | ✅ | AA = static policy analysis. GD = needs actual anomalous access. No access = no GD finding. | Q518, Q534 | Access Analyzer + GuardDuty both fire |
| 618 | D4/D5 | Identity=GetObject+Decrypt, session=GetObject only, boundary=s3:*+kms:*, same-account, no bucket policy naming role — SSE-KMS read? | A: Succeeds — server-side KMS not gated by session policy | ✅ | Session policy doesn't gate S3's internal KMS call. Identity has kms:Decrypt. Root enables delegation. | Q529, Q591 | Session policy + server-side KMS |
| 619 | D4/D6 | RCP denies non-org s3:* with PrincipalIsAWSService:false — ELB SLR + CloudTrail + external attacker — which succeed? (TWO) | A+B: SLR + CloudTrail | ✅ | SLR exempt (structural) + CloudTrail exempt (PrincipalIsAWSService). Attacker blocked. | Q217, Q499 | RCP exemptions (both paths) |
| 620 | D4/D5/D6 | Full 5-layer: key policy grants B root + SCP ViaService + RCP same-org + session=GetObject + cross-account SSE-KMS read — result? | C: Succeeds — all gates pass | ✅ | ViaService satisfied (server-side), RCP same-org passes, session doesn't gate server-side KMS, key policy enables delegation. | Q591, Q531 | Full 5-layer cross-account evaluation |


### Session 64 — 2026-05-30

**Domains:** Cross-domain (AWS-style wording traps — all domains, novel phrasing)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 621 | D1 | SSE-KMS, CISO wants visibility into access from inconsistent geographies, NO code/infra/maintenance — approach? | C: GuardDuty S3 Protection | ✅ | "Visibility" + "anomalous geo" + "no code/infra" = GuardDuty S3 Protection. | Q568, Q581 | Detect vs prevent (GuardDuty vs policy) |
| 622 | D4/D6 | Data perimeter: no external reads IN + no insider exfil OUT, org-level — which TWO? | A+B: RCP + SCP with ResourceAccount | ✅ | RCP blocks outsiders IN. SCP blocks insiders OUT. Full data perimeter = both. | Q398 | Data perimeter (RCP blocks IN, SCP blocks OUT) |
| 623 | D5/D3 | Lambda private subnet, SM works, S3 PutObject Access Denied, Gateway endpoint exists — cause? | B: Gateway endpoint policy doesn't allow PutObject | ✅ | Access Denied = permissions. Endpoint policy is additional gate. SM working = network fine. | Q535 | Gateway endpoint policy as additional gate |
| 624 | D1 | Detect iam:CreateAccessKey for root within 60 seconds, org trail exists — Config vs EventBridge? | B: EventBridge — near real-time, Config has inherent latency | ✅ | "Within 60 seconds" + "specific API call" = EventBridge. Config is slower. | Q474, Q570 | EventBridge for API call detection |
| 625 | D6 | Inspector deployed via StackSets, 8 new accounts missing — why? | B: Inspector has native delegated admin with auto-enable | ✅ | Native org support = use native, not StackSets. | Q483, Q492 | Native org-wide deployment |
| 626 | D5 | SCP Deny PutObject if encryption header ≠ aws:kms, developer uploads without header, bucket has default SSE-KMS — result? | A: Succeeds (default encryption) | ❌ | **B: Denied — SCP evaluates request headers BEFORE default encryption applies.** No header sent → StringNotEquals fires → Deny. | Q426, Q431 | Default encryption vs bucket policy Deny |
| 627 | D6/D3 | Baseline SG on all EC2 across 300 accounts, auto-re-apply if removed — service? | B: Firewall Manager SG common policy | ✅ | FM common policy creates + applies + auto-remediates. | Q454 | FM SG common policy |
| 628 | D4/D5 | Lambda calls kms:Decrypt directly (not via S3), SCP ViaService=s3 only — result? | B: Fails — no ViaService context, SCP Deny fires | ✅ | Direct call has no ViaService. SCP follows the caller. | Q488, Q506 | kms:ViaService + SCP |
| 629 | D1 | GuardDuty zero findings 90d, active workloads, junior created suppression filter 80d ago — investigate first? | B: Suppression filter overly broad | ✅ | Zero findings + active workloads + suppression filter = filter archiving everything. | Q372, Q389 | GuardDuty suppression rules |
| 630 | D4/D5 | Cross-account SSE-KMS, RCP denies non-org s3:*, Lambda kms:Decrypt — at which layer does RCP evaluate KMS? | C: RCP only covers s3:* actions, not kms:* | ✅ | RCP statement scope is action-level. s3:* doesn't include kms:*. | — | RCP scope (action-level) |


### Session 65 — 2026-05-31

**Domains:** Cross-domain domination drill (D1 Detection + D5 Data Protection + D6 Governance)
**Score:** 15 ✅ · 0 ⚠️ · 3 ❌ (83% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 631 | D1 | SSE-KMS, alert on downloads inconsistent with business hours/geo, zero Lambda/filters/infra — service? | B: GuardDuty S3 Protection | ✅ | "Anomalous pattern" + "zero code/infra" = GuardDuty S3 Protection. | Q568, Q581 | Detect vs prevent (GuardDuty vs policy) |
| 632 | D1 | Detect iam:DeactivateMFADevice within 90s, org trail exists, least overhead? | C: EventBridge rule in management account | ✅ | "Detect specific API call" + "fast" + "least overhead" = EventBridge. | Q474, Q570 | EventBridge for API call detection |
| 633 | D1 | EC2 communicating with C2 IP (hardcoded, no DNS), alert, zero custom code, zero infra deployment? | B: Network Firewall alert | ❌ | **C: GuardDuty.** "Detect + zero code + zero infra" = always GuardDuty. NF requires deployment. | Q571, Q584 | Detect C2 = GuardDuty (zero code) |
| 634 | D1 | Bucket policy grants external account, no access yet, GD + AA enabled — which fires? | C: Only Access Analyzer | ✅ | AA = static policy analysis (fires on policy). GD = needs actual anomalous access. | Q518, Q573 | Access Analyzer + GuardDuty both fire |
| 635 | D1 | RCP blocks external, attacker attempts 200 GetObjects (all denied), GD enabled — finding? | B: No — GD only fires on successful anomalous access | ✅ | GuardDuty doesn't fire on blocked attempts — no successful access = no finding. | Q534, Q594 | GuardDuty ≠ failed attempts |
| 636 | D1 | Detect kms:DisableKey across 300 accounts within 2 min, org trail exists, least overhead? | C: EventBridge rule in management account | ✅ | "Detect specific API call" + "fast" = EventBridge. | Q474, Q570 | EventBridge for API call detection |
| 637 | D1 | Lambda active TCP to mining pool IP (confirmed by Flow Logs) — ThreatPurpose? | B: CryptoCurrency | ✅ | Active mining traffic = CryptoCurrency. | Q226, Q489 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 638 | D1 | Same Lambda 10min earlier, only DNS resolution of pool.minexmr.com, no TCP — ThreatPurpose? | B: Impact | ✅ | DNS query only = Impact. Active mining = CryptoCurrency. | Q226, Q489 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 639 | D1 | Visibility into anomalous download patterns (unusual volumes/times/countries), no code/filters/maintenance — service? | C: GuardDuty S3 Protection | ✅ | "Anomalous behavior" + "zero maintenance" = GuardDuty S3 Protection. | Q568, Q581 | Detect vs prevent (GuardDuty vs policy) |
| 640 | D1 | Prevent external S3 reads org-wide + detect internal 3AM unusual-country downloads — which TWO? | B+E: RCP + EventBridge | ❌ | **B+C: RCP + GuardDuty S3 Protection.** EventBridge detects API calls, not behavioral anomalies. | Q568, Q581 | Detect vs prevent (GuardDuty vs EventBridge for behavioral) |
| 641 | D5 | SCP Deny PutObject if KMS key header ≠ specific key, upload without header, default encryption set — result? | B: Denied — SCP evaluates before default encryption | ✅ | SCP evaluates request headers BEFORE default encryption applies. | Q426, Q626 | Default encryption vs bucket policy Deny |
| 642 | D5 | Same SCP, upload WITH correct KMS key header — result? | A: Succeeds — header matches condition | ✅ | Header present and matches → StringNotEquals is FALSE → Deny doesn't fire. | Q426, Q626 | Default encryption vs bucket policy Deny |
| 643 | D5 | Bucket policy Deny if encryption header ≠ aws:kms, default encryption SSE-KMS, upload without header — result? | A: Succeeds (default encryption) | ❌ | **B: Denied — bucket policy evaluates request headers before default encryption applies.** Same rule as SCP. | Q426, Q626 | Default encryption vs bucket policy Deny |
| 644 | D6 | NF policies in central account, 200 members need them applied + auto-re-apply if deleted — which TWO? | A+B: RAM + Firewall Manager | ✅ | RAM shares, FM enforces + auto-remediates. | Q441, Q562 | RAM for sharing + FM for enforcing |
| 645 | D6 | FM deploys WAF to ALBs, developer disassociates Web ACL — what happens? | B: FM re-associates automatically | ✅ | FM auto-remediates. | Q284, Q435 | Firewall Manager auto-remediation |
| 646 | D6 | Share TGW with 50 accounts + ensure route table entries in all VPCs — which TWO? | A+C: RAM + StackSets | ✅ | RAM shares TGW. StackSets deploys route table entries (FM can't do routes). | — | RAM + StackSets complementary |
| 647 | D6 | DNS FW rule groups visible to 300 members, NO auto-association needed — service? | B: RAM | ✅ | "Visible/accessible" without enforcement = RAM only. | Q441, Q562 | RAM for sharing vs FM for enforcing |
| 648 | D6 | Match verbs: visible=?, associate=?, re-create=?, deploy IAM role=? | A: RAM, FM, FM, StackSets | ✅ | "Visible" = RAM. "Associate/re-create" = FM. "Deploy custom resource" = StackSets. | — | RAM vs FM vs StackSets verb signals |



### Session 66 — 2026-06-01

**Domains:** Cross-domain domination drill (D1 Detection + D5 Data Protection + D6 Governance + D4 IAM)
**Score:** 11 ✅ · 1 ⚠️ · 2 ❌ (79% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 649 | D1 | S3 download volumes inconsistent with baselines, zero Lambda/filters/infra — service? | (not answered) | — | C: GuardDuty S3 Protection | Q568, Q581 | Detect vs prevent (GuardDuty vs policy) |
| 650 | D1 | Detect iam:DeleteRolePolicy within 60s, org trail exists — approach? | (not answered) | — | C: EventBridge rule in management account | Q474, Q570 | EventBridge for API call detection |
| 651 | D1 | EC2 communicating with threat intel IPs, finding generated, zero code/infra — service? | (not answered) | — | C: GuardDuty | Q571, Q584 | Detect C2 = GuardDuty (zero code) |
| 655 | D1 | Lambda resolves C2 domain via DNS then establishes TCP — how many findings + ThreatPurpose? | C: Impact then CryptoCurrency | ❌ | **B: Two findings — Impact (DNS) then Trojan (TCP to C2).** CryptoCurrency only for mining pools. C2 = Trojan. | Q226, Q489 | GuardDuty finding types (C2 = Trojan, not CryptoCurrency) |
| 659 | D5 | SCP Deny PutObject if KMS key header ≠ specific key, upload without header, default encryption set — result? | B: Denied — SCP evaluates before default encryption | ✅ | SCP evaluates request headers BEFORE default encryption applies. | Q426, Q626 | Default encryption vs bucket policy Deny |
| 661 | D5 | Bucket policy Deny if encryption header ≠ aws:kms, upload without header, default encryption SSE-KMS — result? | B: Denied — bucket policy evaluates before default encryption | ✅ | Same rule as SCP — policy evaluates request as-received. | Q426, Q626, Q643 | Default encryption vs bucket policy Deny |
| 663 | D6 | DNS FW rule group in security account, enforce on all VPCs, re-associate if removed — need RAM first? | B: Yes — RAM shares, FM enforces | ✅ | RAM shares rule group cross-account, then FM enforces association. | Q441, Q562 | RAM for sharing + FM for enforcing |
| 652 | D1 | Bucket policy grants external account, no access yet, GD + AA enabled — which fire? | B+C: AA + Security Hub | ⚠️ | **B only: Access Analyzer (static policy analysis).** Security Hub S3 controls check public access, not specific cross-account grants. GD needs actual access. | Q518, Q573 | Access Analyzer + GuardDuty both fire |
| 653 | D1 | RCP blocks external, 500 denied GetObjects, GD enabled — finding? | B: No — GD only fires on successful anomalous access | ✅ | GuardDuty doesn't fire on blocked attempts. | Q534, Q594 | GuardDuty ≠ failed attempts |
| 662 | D6 | NF policies in central account, 300 members, auto-recreate if deleted — which TWO? | A+B: RAM + Firewall Manager | ✅ | RAM shares, FM enforces + auto-remediates. | Q441, Q562 | RAM for sharing + FM for enforcing |
| 665 | D6 | Deploy Detective across 150 accounts, auto for new — StackSets? | B: Detective has native delegated admin with auto-enable | ✅ | Native org support = use native, not StackSets. | Q483, Q492 | Native org-wide deployment |
| 666 | D6 | Match verbs: accessible=?, attached/re-attached=?, deployed=?, self-service=? | A: RAM, FM, StackSets, Service Catalog | ✅ | Correct verb-to-service mapping. | — | RAM vs FM vs StackSets vs Service Catalog |
| 664 | D6 | FM deploys WAF, developer disassociates Web ACL — what happens? | B: FM re-associates automatically | ✅ | FM auto-remediates. | Q284, Q435 | Firewall Manager auto-remediation |
| 667 | D1 | EC2 resolves pool.minexmr.com (DNS), then TCP mining traffic — ThreatPurpose values? | C: Impact then CryptoCurrency | ✅ | Mining pool DNS = Impact. Active mining traffic = CryptoCurrency. | Q226, Q489 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 668 | D4/D5 | 5-layer cross-account SSE-KMS: key policy grants B root + SCP ViaService + RCP same-org + session=GetObject — result? | C: Succeeds — all gates pass | ✅ | Server-side KMS, ViaService satisfied, session doesn't gate, RCP same-org passes. | Q591, Q531 | Full 5-layer cross-account evaluation |
| 669 | D4/D5 | Same as Q668 but key policy grants only Account A root (not B) — result? | C: Succeeds — RCP same-org overrides | ❌ | **B: Fails — key policy must explicitly name external account.** Root enables delegation same-account only. RCP never grants access. | Q541, Q559 | Cross-account KMS key policy must name external account |
| 670 | D4 | Cross-account bucket policy grants DeleteObject, session policy=Get+Put only — result? | B: Denied — session policy ceiling applies cross-account | ✅ | Resource-policy bypass of session policy ONLY works same-account. | Q96, Q169, Q613 | Session policy bypass same-account ONLY |


### Session 67 — 2026-06-01

**Domains:** D1 Detection + D4/D5 IAM/Data Protection (final leaks drill — C2=Trojan + cross-account KMS key policy)
**Score:** 6 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 671 | D1 | Two GD findings: Impact DNS then active TCP to C2 IP (not mining) — ThreatPurpose of #2? | C: Trojan | ✅ | Trojan — active TCP to C2 server = Trojan | Q655 | GuardDuty finding types (C2 = Trojan, not CryptoCurrency) |
| 672 | D1 | EC2 resolves pool.hashvault.pro DNS then TCP port 3333 — ThreatPurpose values in order? | B: Impact then CryptoCurrency | ✅ | DNS query = Impact. Active TCP to mining pool = CryptoCurrency. | Q655, Q226 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 673 | D1 | EKS pod resolves C2 beacon domain then TLS TCP to that IP — ThreatPurpose of #2? | C: Trojan | ✅ | C2 beacon = C2 server = Trojan regardless of port/protocol | Q655 | GuardDuty finding types (C2 = Trojan, not CryptoCurrency) |
| 674 | D4/D5 | Key policy grants only Account A root, Account B (same org) calls Decrypt, RCP denies non-org — result? | C: Fails — key policy doesn't name Account B | ✅ | Root enables delegation same-account only. Cross-account needs explicit grant. RCP never grants. | Q541, Q669 | Cross-account KMS key policy must name external account |
| 675 | D4/D5 | Key policy grants Account B root, SCP ViaService=s3, Lambda reads SSE-KMS cross-account — result? | C: Succeeds — ViaService satisfied by S3 server-side | ✅ | Key policy names B (cross-account satisfied). S3 calls KMS server-side → ViaService satisfied. | Q541, Q488 | Cross-account KMS + ViaService + SCP |
| 676 | D4/D5 | Key policy grants only Account A root, Account B same org, uploads SSE-KMS — result? | C: Fails — key policy must name Account B | ✅ | Same-org doesn't override KMS key policy requirement. Root = same-account delegation only. | Q541, Q669 | Cross-account KMS key policy must name external account |



### Session 68 — 2026-06-02

**Domains:** Cross-domain final validation killer set (all domains, maximum difficulty)
**Score:** 7 ✅ · 0 ⚠️ · 3 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 677 | D4/D5/D6 | SCP denies GenerateDataKey unless ViaService=s3, developer calls GenerateDataKey directly from CLI — result? | C: Denied — no ViaService context | ✅ | Denied — direct CLI call has no ViaService → SCP Deny fires. Key policy never overrides SCP. | Q488, Q506 | kms:ViaService + SCP |
| 678 | D1/D3 | EC2 C2 at hardcoded IP 203.0.113.50:8443, no DNS — block VPC-wide? | B: Network Firewall DROP | ✅ | Network Firewall stateful DROP on destination IP. DNS FW useless (no DNS query). SGs have no deny rules. | Q526, Q571 | Network FW for IP-level C2 block |
| 679 | D4/D5 | Cross-account SSE-KMS, key policy grants B root, session policy=GetObject only — Lambda reads encrypted object? | B: Fails — cross-account bypass doesn't apply | ❌ | **C: Succeeds — S3 calls KMS server-side, session policy doesn't gate server-side KMS calls.** Session policy only restricts caller's direct API calls. | Q591, Q531 | Session policy + server-side KMS |
| 680 | D6/D3 | NF policies in central account, 250 members, auto-recreate if deleted — which TWO? | A+B: RAM + FM | ✅ | RAM shares policy cross-account. FM enforces + auto-recreates if deleted. | Q441, Q446 | RAM + FM complementary |
| 681 | D1 | Alert within 60s on iam:DeleteRolePolicy + alert on unusual S3 download volumes/geo — which TWO services? | E: EventBridge + GuardDuty S3 Protection | ✅ | EventBridge for specific API call fast. GuardDuty S3 Protection for behavioral anomalies. | Q474, Q568 | EventBridge + GuardDuty S3 Protection |
| 682 | D5/D4 | Bucket policy Deny if KMS key header ≠ specific key, default encryption set, upload without header — result? | B: Denied — policy evaluates before default encryption | ✅ | Bucket policy evaluates request headers BEFORE default encryption applies. No header → Deny fires. | Q426, Q626 | Default encryption vs bucket policy Deny |
| 683 | D4/D6 | RCP denies non-org s3:*, S3 replication SLR replicates to EXTERNAL partner bucket — succeeds? | A: Yes — SLR exempt from RCP | ❌ | **D: RCP doesn't apply — external bucket is not your resource.** RCP protects YOUR resources (inbound). Outbound to external resources = SCP's job. | — | RCP scope (your resources only, not outbound) |
| 684 | D2/D1/D4 | InstanceCredentialExfiltration.OutsideAWS, stop attacker + keep instance + fresh creds — single action? | B: Inline Deny TokenIssueTime | ✅ | Inline Deny with TokenIssueTime < now. IMDS refreshes new creds after timestamp. | Q536, Q598 | Credential exfiltration response |
| 685 | D5/D3 | Lambda private subnet: Secrets Manager + S3 SSE-KMS + direct kms:Decrypt + DynamoDB — minimum endpoints? | A: 3 | ❌ | **B: 4 — Interface (SM) + Gateway (S3) + Interface (KMS for direct call) + Gateway (DynamoDB).** S3 SSE-KMS = server-side (no KMS endpoint). Direct kms:Decrypt = needs KMS endpoint. DynamoDB fetch = needs DDB endpoint. | Q378, Q522 | VPC endpoints (direct KMS + DynamoDB) |
| 686 | D4/D5/D6 | Key policy grants only Account A root, Account B (same org) reads SSE-KMS, RCP denies non-org s3:* — result? | B: Fails — key policy must name Account B | ✅ | Key policy must explicitly name external account. Root = same-account delegation only. Same-org doesn't override. RCP never grants. | Q541, Q669 | Cross-account KMS key policy must name external account |


### Session 69 — 2026-06-02

**Domains:** Cross-domain killer exam simulation (all domains, maximum difficulty + novel patterns)
**Score:** 7 ✅ · 0 ⚠️ · 3 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 687 | D4/D5 | Key policy grants root only, Lambda has s3:GetObject but no kms:Decrypt — reads SSE-KMS object? | C: Fails — root doesn't grant | ❌ | **D: Fails for TWO reasons — root = delegation not grant AND Lambda needs explicit kms:Decrypt.** Both B and C are correct. | Q264, Q503 | KMS key policy root = delegation, not grant |
| 688 | D1/D6 | Prevent StopLogging + detect PutBucketPolicy within 2 min + auto-revert — which THREE services? | B: SCP + GuardDuty + Step Functions | ❌ | **A: SCP + EventBridge + Lambda.** GuardDuty detects behavior, not API calls. EventBridge for specific API detection. Lambda for simple revert. | Q474, Q549 | EventBridge for API call detection |
| 689 | D4/D5/D6 | RCP same-org + SCP ViaService + cross-account SSE-KMS read — result? | B: Succeeds — ViaService satisfied | ✅ | S3 calls KMS server-side → ViaService satisfied. RCP same-org passes. All gates clear. | Q591, Q531 | Full 5-layer cross-account evaluation |
| 690 | D3/D1 | Trojan:EC2/DGADomainRequest — DGA domains, all via DNS, block VPC-wide? | A: Network Firewall DROP | ❌ | **D: DNS Firewall allow-list (block all except known-good).** DGA = unpredictable domains, can't enumerate. Allow-list approach. DNS layer since no hardcoded IPs. | — | DGA = allow-list DNS Firewall |
| 691 | D5/D4 | Bucket policy Deny unless KMS key header matches, developer uploads WITH correct header — result? | B: Succeeds — header matches, Deny doesn't fire | ✅ | Header present and matches → StringNotEquals FALSE → Deny doesn't fire. | Q426, Q626 | Default encryption vs bucket policy Deny |
| 692 | D6 | Custom SCP added outside Control Tower, drift detected — what happens? | B: Alert but no auto-fix | ✅ | Control Tower detects drift but does NOT auto-revert. Manual resolution required. | — | Control Tower drift |
| 693 | D2/D4/D1 | InstanceCredentialExfiltration.InsideAWS — attacker on different EC2 same account, contain without breaking legitimate instance? | A: Deny-all SG on compromised instance | ✅ | InsideAWS = TokenIssueTime would block both. Isolate compromised instance with deny-all SG instead. | Q536 | InsideAWS credential exfiltration containment |
| 694 | D5/D3/D4 | Lambda private subnet: Secrets Manager + SQS + S3 SSE-KMS + SNS — minimum endpoints? | B: 4 | ✅ | Interface (SM) + Interface (SQS) + Gateway (S3, KMS server-side) + Interface (SNS) = 4. | Q685 | VPC endpoints counting |
| 695 | D1/D4/D5 | RCP deployed, external reads blocked, AA + GD enabled — which TWO true after RCP? | A+D: AA still flags + GD doesn't fire on blocked | ✅ | AA = static policy analysis (policy unchanged). GD = no successful access = no finding. | Q534, Q518 | AA static + GD ≠ failed attempts |
| 696 | D6/D3/D4 | Baseline SG all EC2 + DNS FW on all VPCs + auto-remediate removal — which THREE? | A+B+D: FM SG common + RAM + FM DNS FW | ✅ | FM SG common creates SG. RAM shares DNS FW rules. FM DNS FW enforces association. All auto-remediate. | Q454, Q441 | FM SG common + RAM + FM DNS FW |


### Session 70 — 2026-06-05

**Domains:** Cross-domain (pre-Dojo killer drill — session policy + RCP scope + VPC endpoints + ViaService)
**Score:** 4 ✅ · 0 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 697 | D4/D5 | Cross-account SSE-KMS, session policy=GetObject only, key policy grants B root — Lambda reads encrypted object? | C: Succeeds — server-side KMS not gated by session | ✅ | S3 calls KMS server-side. Session policy only gates caller's direct calls. | Q679, Q591 | Session policy + server-side KMS |
| 698 | D4/D6 | RCP denies non-org s3:*, SLR replicates to EXTERNAL partner bucket — blocked? | B: No — SLR exempt from RCP | ❌ | **C: RCP doesn't apply — partner's bucket is not your resource.** RCP protects YOUR resources (inbound). Outbound = SCP's job. | Q683 | RCP scope (your resources only, not outbound) |
| 699 | D5/D3 | Lambda private subnet: Secrets Manager + S3 SSE-KMS + direct kms:GenerateDataKey + DynamoDB — minimum endpoints? | B: 4 | ✅ | Interface (SM) + Gateway (S3) + Interface (KMS for direct call) + Gateway (DynamoDB) = 4. | Q685 | VPC endpoints (direct KMS + DynamoDB) |
| 700 | D4/D5/D6 | SCP ViaService + session policy=GetObject only + key policy grants B root + RCP same-org — cross-account SSE-KMS read? | C: Succeeds — ViaService satisfied, session doesn't gate server-side KMS | ✅ | All gates pass: ViaService satisfied (server-side), session doesn't gate, key policy enables delegation, RCP same-org passes. | Q591, Q679 | Full 5-layer cross-account evaluation |
| 701 | D1/D6 | Detect iam:DeleteRolePolicy 60s + detect anomalous S3 downloads + prevent StopLogging — which THREE? | B: EventBridge + GuardDuty S3 Protection + SCP | ✅ | EventBridge for fast API detection. GuardDuty S3 Protection for behavioral anomalies. SCP for prevention. | Q688, Q681 | EventBridge + GuardDuty S3 + SCP |


### Session 71 — 2026-06-05

**Domains:** Cross-domain (pre-Dojo RCP scope drill + AA vs GD static/dynamic)
**Score:** 4 ✅ · 0 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 702 | D4/D6 | RCP denies non-org s3:*, SLR replicates to EXTERNAL partner bucket, replication failing — cause? | C: RCP doesn't apply — partner's bucket is not your resource | ✅ | RCP protects YOUR resources only. Partner's bucket isn't yours. Access Denied from something else (partner bucket policy, destination permissions). | Q683, Q698 | RCP scope (your resources only, not outbound) |
| 703 | D4/D6 | RCP denies non-org s3:*, Lambda writes to own bucket + partner bucket — which succeed? (TWO) | A+C | ✅ | A: Own bucket succeeds (PrincipalOrgID matches). C: Partner bucket succeeds (RCP doesn't apply to external resources). | Q683, Q698 | RCP scope (your resources only, not outbound) |
| 704 | D4/D6 | Data perimeter: block external reads IN + block insider writes OUT — which TWO? | A: RCP + SCP with ResourceAccount | ✅ | RCP blocks outsiders IN. SCP blocks insiders OUT. Full data perimeter = both. | Q398, Q622 | Data perimeter (RCP blocks IN, SCP blocks OUT) |
| 705 | D4/D5 | RCP denies non-org kms:Decrypt, Account B (same org) calls Decrypt on Account A key — result? | C: Allowed — PrincipalOrgID matches | ✅ | Same-org caller → condition FALSE → Deny doesn't fire. | Q427, Q521 | RCP same-org evaluation |
| 706 | D1/D4 | RCP blocks external + AA + GD enabled + 100 denied GetObjects by attacker — which TWO true? | A+C (contradictory) | ❌ | **B+C: Access Analyzer flags policy (static) + GuardDuty doesn't fire (no successful access).** AA is static policy analysis — doesn't know about RCP runtime enforcement. | Q518, Q534, Q594 | Access Analyzer static + GuardDuty ≠ failed attempts |


### Session 72 — 2026-06-09

**Domains:** Cross-domain (Dojo Test 1 gap drill — operational troubleshooting, Directory Service, GuardDuty, CloudTrail, S3 encryption)
**Score:** 4 ✅ · 1 ⚠️ · 3 ❌ (50% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 707 | D3 | VPC Flow Logs: inbound ACCEPT, outbound REJECT — SG or NACL problem? | NACL (wrong reason: said SG is stateless) | ⚠️ | NACL — because NACLs are stateLESS (need explicit outbound). SGs are stateFUL (auto-allow return). | — | NACLs stateless (Dojo Q19, Q61) |
| 708 | D1 | CW Logs agent was working, logs stopped — which log file? | B: /var/log/awslogs.log | ✅ | /var/log/awslogs.log = runtime errors. setup.log = install only. | — | CW Logs agent troubleshooting (Dojo Q63) |
| 709 | D4 | On-prem admins need AWS, cloud users must NOT access on-prem — which Directory + trust? | B: AD Connector | ❌ | C: Managed Microsoft AD + one-way trust (AWS trusts on-prem). AD Connector = no cloud users, no trusts. | — | Directory Service + trust direction (Dojo Q5) |
| 710 | D1 | EventBridge rule on ConsoleLogin never fires, events visible in console — cause? | A: us-east-1 for global events | ❌ | B: Management events set to Write-only. ConsoleLogin = Read event. EventBridge only fires on configured trail events. | — | CloudTrail management events Read/Write (Dojo Q16) |
| 711 | D1 | Suppress GD findings from pen-test EC2 (private IPs only) — approach? | A: Add private IPs to Trusted IP list | ❌ | B: Attach EIPs + add to Trusted IP list. Trusted IP list = PUBLIC IPs only. | — | GuardDuty Trusted IP list (Dojo Q22) |
| 712 | D5 | Company generates own keys, keys must NEVER be in AWS — which S3 encryption? | D: Client-side encryption with client master key | ✅ | Client-side = keys never leave your environment. SSE-C = key touches AWS briefly. | — | S3 encryption matrix (Dojo Q17) |

### Session 73 — 2026-06-09

**Domains:** Cross-domain (Dojo Test 1 gap drill #2 — CloudTrail, IoT, ENI, SQS, VPN, GuardDuty, IAM, S3 encryption)
**Score:** 8 ✅ · 0 ⚠️ · 2 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 713 | D1 | CloudTrail log file integrity validation — what does it do? | B: SHA-256 digest (detect tampering) | ✅ | Integrity = detect tampering. Encryption = prevent reading. Different controls. | — | CloudTrail log integrity (Dojo Q9) |
| 714 | D3 | IoT Core client ID injection — prevent unauthorized topic access? | C: Bind iot:Connect to ThingName | ✅ | ThingName = server-registered (trusted). ClientId = client-supplied (untrusted). | — | IoT Core ThingName vs ClientId (Dojo Q30) |
| 715 | D3 | ALB health checks failing — which TWO to check? | A+B: NACL ephemeral + target registration | ✅ | Dojo answer was B+D (target registration + ENI SG mapping). Both valid. | — | ENI/ALB troubleshooting (Dojo Q29) |
| 716 | D4 | Lambda Access Denied on SQS, IAM role has ReceiveMessage — cause? | B: SQS resource policy explicitly denies | ✅ | Explicit Deny in resource policy always wins over identity Allow. | — | SQS resource policy (Dojo Q12) |
| 717 | D5 | API keys in CloudFormation securely — approach? | B: Secrets Manager + resolve dynamic reference | ✅ | Secrets Manager = encrypted + rotatable + never plaintext in template. | — | Secrets Manager in CF (Dojo Q50) |
| 718 | D1 | CloudTrail org trail, new account logs not appearing — TWO causes? | A+C: Bucket policy + Requester Pays | ✅ | Org trail = auto for members. Delivery = bucket policy + Requester Pays OFF. | — | CloudTrail multi-account (Dojo Q9, Q52) |
| 719 | D3 | 3 branch offices with firewalls need encrypted connectivity to AWS — solution? | D: Transit Gateway + Client VPN | ❌ | B: Site-to-Site VPN. Office with router = Site-to-Site (IPsec). Client VPN = laptops. | — | VPN types (Dojo Q56) |
| 720 | D1 | GuardDuty enabled, zero findings 90d, active workloads — cause? | C: Suppression rule | ✅ | Zero findings + active workloads + confirmed enabled = suppression rule. | — | GuardDuty suppression rules (Dojo Q10) |
| 721 | D4 | s3:PutObject with Resource arn:aws:s3:::bucket (no /*) — result? | B: Access Denied — wrong ARN | ✅ | Bucket ARN = bucket-level actions. Object ARN (/*) = object-level actions. | — | S3 ARN bucket vs object (Dojo Q23) |
| 722 | D5 | Key provided per request, AWS encrypts then discards key — which encryption? | C: SSE-C | ✅ | SSE-C = customer key per request, AWS discards immediately. | — | S3 encryption matrix (Dojo Q17) |

### Session 74 — 2026-06-10

**Domains:** Cross-domain (Dojo Test 1 gap drill #3 — GuardDuty admin, CW metric filters, IAM boundaries, KMS Grants, OpenSearch, ACM, CloudTrail Read/Write, metadata, AD/ADFS, S3 encryption)
**Score:** 8 ✅ · 0 ⚠️ · 2 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 723 | D1 | GuardDuty member account tries CreateIPSet — result? | B: Fails — only delegated admin manages IP lists | ✅ | Only administrator can manage Trusted/Threat IP lists. Members cannot regardless of IAM. | — | GuardDuty master/member permissions (Dojo Q10) |
| 724 | D1 | CW alarm for CreateAccessKey never fires, trail Write-only, events in Event History — cause? | C: Region mismatch | ❌ | D: Metric filter metric value set to 0 instead of 1. Event History shows all events regardless of trail config. | — | CW metric filter value (Dojo Q57) |
| 725 | D4 | Restrict dev to one bucket without modifying existing Allow s3:Get*/List* on * — approach? | B: Permission boundary scoped to dev-data | ✅ | Boundary = ceiling. Effective = identity ∩ boundary. No policy modification needed. | — | Permission boundary as ceiling (Dojo Q38) |
| 726 | D5 | Key policy at 28KB, onboard/offboard monthly, need Decrypt only — mechanism? | B: KMS Grants | ✅ | Grants = programmatic, per-operation, no policy edits, no size limit, revocable. | — | KMS Grants (Dojo Q47) |
| 727 | D1 | Real-time full-text search + dashboards + sub-minute + 30-day hot — architecture? | B: Kinesis Firehose + OpenSearch | ✅ | Real-time + full-text search + dashboards = OpenSearch. Kinesis handles ingestion. | — | Kinesis + OpenSearch (Dojo Q41) |
| 728 | D5 | CloudFront custom domain + ALB in eu-west-1, HTTPS — cert config? | B: us-east-1 for CF + eu-west-1 for ALB | ✅ | CF custom domain cert always us-east-1. ALB cert in ALB's region. | — | ACM region requirements (Dojo Q43) |
| 729 | D1 | EventBridge rule on ConsoleLogin never fires, Event History shows events — cause? | B: Trail Write-only, ConsoleLogin is Read | ✅ | EventBridge only receives events the trail is configured to deliver. Event History shows all. | Q710 | CloudTrail management events Read/Write (Dojo Q16) |
| 730 | D3 | Legacy app doesn't need metadata, SSRF to 169.254.169.253 — eliminate? | C: HttpEndpoint disabled | ✅ | HttpEndpoint=disabled = metadata service completely off. NACLs can't block link-local. | — | Disable instance metadata (Dojo Q55) |
| 731 | D4 | On-prem AD, SSO to AWS Console, NO AWS Directory Service infra, AD groups → permissions? | B: AD Connector + Identity Center | ❌ | C: ADFS on-prem as SAML IdP + Identity Center external IdP. AD Connector IS AWS Directory Service infrastructure. | Q709 | ADFS vs AD Connector (Dojo Q48) |
| 732 | D5 | Upload without encryption headers, bucket has default SSE-KMS + Deny policy checking headers — result? | B: Access Denied — policy evaluates before default encryption | ✅ | Bucket policy evaluates request headers BEFORE default encryption applies. | Q626, Q643 | Default encryption vs bucket policy Deny (Dojo Q65) |

### Session 75 — 2026-06-10

**Domains:** Cross-domain (Dojo Test 1 gap drill #4 — AD/Directory Service focus + operational troubleshooting)
**Score:** 8 ✅ · 0 ⚠️ · 2 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 733 | D4 | 3000 employees, SSO, ZERO AWS infra, AD groups → permissions — approach? | C: ADFS on-prem + Identity Center external IdP | ✅ | "Zero AWS infra" = ADFS on-prem + Identity Center. AD Connector IS AWS infra. | Q709, Q731 | ADFS vs AD Connector (no infra) |
| 734 | D4 | On-prem users need AWS + cloud users need on-prem (bidirectional) — config? | C: Managed AD + two-way trust | ✅ | Bidirectional = two-way trust. One-way = one direction only. | — | Directory Service + trust direction |
| 735 | D4 | WorkSpaces domain-join + RDS SQL Server Windows Auth — minimum Directory Service? | C: Managed AD + one-way trust | ✅ | "RDS SQL Server" = Managed AD always. Simple AD and AD Connector can't. | — | Managed AD requirements |
| 736 | D1 | CW alarm fired (threshold >=5), only 2 events in Event History — why? | B: Data events not in Event History | ✅ | Event History = management events only. Data event AccessDenied matches filter but invisible there. | — | Event History vs data events |
| 737 | D1 | Suppress GD findings from pen-test EC2 with private IPs only — approach? | B: Attach EIPs + add to Trusted IP list | ✅ | Trusted IP list = public IPs only. Private IPs cannot be added. | Q711 | GuardDuty Trusted IP list |
| 738 | D3 | 3 offices with routers + static IPs, encrypted to AWS, centralized routing — solution? | B: Site-to-Site VPN + Transit Gateway | ✅ | Office + router = Site-to-Site. Client VPN = laptops. TGW = centralized. | Q719 | VPN types |
| 739 | D4 | On-prem AD, SSO only, no trusts, no cloud users, some AWS infra OK — simplest? | D: Simple AD | ❌ | B: AD Connector. Simple AD = standalone (own users), doesn't connect to on-prem AD. | — | AD Connector vs Simple AD |
| 740 | D3 | IMDSv2 hop limit 1, container PUT to metadata — no response. Cause? | B: Container network adds extra hop, TTL expires | ✅ | Docker bridge = extra hop. Hop limit 1 = TTL expires. Fix: increase to 2. | — | IMDSv2 hop limit + containers |
| 741 | D4 | Already have ADFS, want AWS SSO, no new Directory Service resources — which TWO? | B+C: ADFS as SAML IdP + permission sets | ✅ | ADFS external IdP in Identity Center + permission sets for group mapping. | Q731 | ADFS + Identity Center |
| 742 | D4 | Match 4 AD scenarios to correct service (Connector, Managed, ADFS, two-way) | All correct: A, B, C, D | ✅ | Full AD decision tree applied correctly. | Q709, Q731 | AD decision tree |

### Session 76 — 2026-06-10

**Domains:** Cross-domain (Dojo Test 2 gap drill — KMS operational, IAM/SCP, STS variants, SSM remediation, load balancers)
**Score:** 8 ✅ · 0 ⚠️ · 2 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 743 | D5 | Encrypt later, only need encrypted key now — which KMS API? | B: GenerateDataKeyWithoutPlaintext | ✅ | No plaintext exposed until actually needed. | — | GenerateDataKey variants (Dojo T2 Q33) |
| 744 | D5 | S3 multipart >10GB + SSE-KMS fails on reassembly — missing permission? | B: kms:Decrypt | ✅ | Multipart = GenerateDataKey + Decrypt (reassembly). Single = GenerateDataKey only. | — | S3 multipart + KMS (Dojo T2 Q43) |
| 745 | D5 | EC2 can't start with encrypted EBS, has kms:Decrypt — what's missing? | B: kms:Encrypt | ❌ | C: kms:CreateGrant. EC2 delegates key access to EBS backend via grants. Always needed. | — | EC2 EBS + kms:CreateGrant (Dojo T2 Q47) |
| 746 | D4 | Delegate user creation but cap permissions of created users — mechanism? | B: Permission boundary | ✅ | Boundary on created users limits effective permissions regardless of attached policies. | — | Permission boundary delegation (Dojo T2 Q61) |
| 747 | D4 | SCP allows ec2+lambda only, IAM has s3:*, calls s3:PutObject — result? | A: IAM missing Resource ARN | ❌ | B: SCP ceiling — s3 not in SCP Allow = implicitly denied regardless of IAM. | — | SCP ceiling implicit deny (Dojo T2 Q65) |
| 748 | D4 | Mobile app, Cognito, needs temp creds for S3 — which STS API? | C: AssumeRoleWithWebIdentity | ✅ | Web/mobile = WebIdentity. Enterprise SAML = SAML. EC2/Lambda = AssumeRole. | — | AssumeRole variants (Dojo T2 Q11) |
| 749 | D4 | Cross-account role, Access Denied ExternalId required — cause? | A: Trust policy requires ExternalId, caller didn't pass it | ✅ | Confused deputy prevention. Must pass matching ExternalId in AssumeRole call. | — | ExternalId (Dojo T2 Q40) |
| 750 | D6 | VPC Flow Logs not enabled, auto-remediate, least config — approach? | B: SSM runbook triggered by Config rule | ✅ | SSM runbook = pre-built, least config. Lambda = custom code, more overhead. | — | SSM runbook remediation (Dojo T2 Q44) |
| 751 | D5 | KMS key PendingDeletion, EC2 still running — recover data? | B: CancelKeyDeletion | ✅ | CancelKeyDeletion saves key. Rsync also valid for data migration. Both work. | — | KMS PendingDeletion recovery (Dojo T2 Q22) |
| 752 | D3 | Custom TCP protocol, NOT HTTP, need load balancer — which type? | B: NLB TCP listener | ✅ | NLB = any TCP/UDP. ALB = HTTP only. GWLB = L3 security appliances. | — | NLB vs ALB vs GWLB (Dojo T2 Q49) |

### Session 77 — 2026-06-10

**Domains:** Cross-domain killer exam simulation (all domains, maximum difficulty)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 753 | D4/D5 | Cross-account KMS, key policy grants only Account A root, Account B same org — result? | B: Fails — key policy must name Account B | ✅ | Root enables delegation same-account only. Cross-account needs explicit grant. | Q541, Q669 | Cross-account KMS key policy must name external account |
| 754 | D4 | Session=GetObject only, same-account bucket policy grants role DeleteObject — result? | B: Allowed — same-account bypass | ✅ | Same-account resource-based policy naming role bypasses session ceiling. | Q96, Q169 | Session policy bypass by resource-based policy |
| 755 | D1/D4 | RCP blocks external, AA + GD enabled, 100 denied GetObjects — which TWO true? | B+C: AA flags + GD doesn't fire | ✅ | AA = static policy analysis. GD = needs successful access. | Q534, Q594 | AA static + GD ≠ failed attempts |
| 756 | D3/D1 | DGA domains, block VPC-wide — approach? | C: DNS Firewall allow-list | ✅ | DGA = unpredictable, can't enumerate. Allow-list = block all except known-good. | Q690 | DGA = allow-list DNS Firewall |
| 757 | D4/D6 | RCP denies non-org s3:*, Lambda writes to own bucket + partner bucket — which succeed? | C: Both | ✅ | Own bucket: PrincipalOrgID matches. Partner bucket: RCP doesn't apply (not your resource). | Q683, Q698 | RCP scope (your resources only) |
| 758 | D5 | S3 multipart 15GB + SSE-KMS fails on reassembly — missing permission? | B: kms:Decrypt | ✅ | Multipart = GenerateDataKey + Decrypt (reassembly). | Q744 | S3 multipart + KMS |
| 759 | D4/D5 | SCP ViaService=s3, Lambda S3 read + direct Decrypt + CLI Decrypt — which succeed? | B: Only #1 (S3 read) | ✅ | Only S3 sets ViaService. Direct calls have no context → SCP Deny fires. | Q488, Q506 | kms:ViaService + SCP |
| 760 | D1/D6 | Prevent ScheduleKeyDeletion + detect PutBucketPolicy 2min + block external S3 — THREE services? | B: SCP + EventBridge + RCP | ✅ | SCP prevents. EventBridge detects API. RCP blocks consequence. | Q688 | Full detect/prevent architecture |
| 761 | D2/D4 | InstanceCredentialExfiltration.InsideAWS, contain without breaking legitimate instance? | A: TokenIssueTime | ❌ | B: Deny-all SG on attacker's instance. InsideAWS = both share role, TokenIssueTime breaks both. | Q693 | InsideAWS = SG isolation |
| 762 | D4 | Cross-account bucket policy grants DeleteObject, session=Get+Put only — result? | B: Denied — session ceiling applies cross-account | ✅ | Resource-policy bypass ONLY works same-account. Cross-account = ceiling always applies. | Q613, Q670 | Session policy bypass same-account ONLY |

### Session 78 — 2026-06-10

**Domains:** Cross-domain (Dojo Test 2 gap drill #2 — KMS operational, SCP, permission boundaries, SSE-C, Secrets Manager, CloudTrail Insights)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 763 | D4 | Centrally allow/deny services per account, least complexity — approach? | B: Organizations + OUs + SCPs | ✅ | SCPs = one policy at OU level, least complexity. | — | SCPs for org-wide control (Dojo T2 Q48) |
| 764 | D5 | KMS PendingDeletion, EC2 running, unauthorized deletion — TWO recovery approaches? | B+C: CancelKeyDeletion + rsync | ✅ | Cancel saves key. Rsync copies decrypted data while instance runs. | — | KMS PendingDeletion recovery (Dojo T2 Q22) |
| 765 | D5 | Store encrypted key for later + upload 20GB multipart SSE-KMS — which THREE KMS perms? | B+D+C (wrong: picked Encrypt) | ❌ | A+B+C: GenerateDataKey (S3 upload) + GenerateDataKeyWithoutPlaintext (store for later) + Decrypt (multipart reassembly). S3 never uses kms:Encrypt. | — | S3 envelope encryption never uses kms:Encrypt |
| 766 | D3 | Public app, CloudFront→ALB, protect SQLi + geo-restrict — approach? | A+D: WAF on CF + geo-restriction | ✅ | Block at the edge (CloudFront), not deeper (ALB). | — | WAF on CloudFront + geo-restriction (Dojo T2 Q12) |
| 767 | D5 | EC2 start with existing encrypted EBS, has kms:Decrypt — what's missing? | B: kms:CreateGrant | ✅ | Start existing = CreateGrant + Decrypt. Always needs CreateGrant. | Q745 | EC2 EBS + kms:CreateGrant (Dojo T2 Q47) |
| 768 | D4 | Developers create roles but roles can't exceed s3+ec2 — mechanism? | B: Permission boundary | ✅ | Boundary caps created roles regardless of attached policies. | — | Permission boundary delegation (Dojo T2 Q61) |
| 769 | D5 | SSE-C upload via HTTP (not HTTPS) — result? | B: S3 rejects — HTTPS required | ✅ | SSE-C mandates HTTPS. Key would be exposed in plaintext over HTTP. | — | SSE-C requires HTTPS (Dojo T2) |
| 770 | D5 | Lambda needs DB creds, rotate every 30d, RDS PostgreSQL — service? | B: Secrets Manager native rotation | ✅ | Rotation + RDS = Secrets Manager. Zero custom code. | — | Secrets Manager native rotation (Dojo T2) |
| 771 | D1 | CloudTrail Insights detects what kind of anomaly? | C: Unusual API call volume | ✅ | Insights = volume (statistical). GuardDuty = behavior (threat intel). | — | CloudTrail Insights vs GuardDuty (Dojo T2) |
| 772 | D5 | Lambda reads Parameter Store SecureString (CMK), has ssm:GetParameter — fails. Missing? | B: kms:Decrypt on customer-managed key | ✅ | Customer-managed key = always explicit kms:Decrypt. AWS-managed may auto-grant. | — | Parameter Store + kms:Decrypt (Dojo T2) |

### Session 79 — 2026-06-11

**Domains:** Cross-domain (Dojo combined gap reinforcement drill — KMS operational, IAM wording traps, service selection, troubleshooting)
**Score:** 8 ✅ · 0 ⚠️ · 2 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 773 | D5 | S3 multipart 50GB + SSE-KMS, Access Denied on complete step — missing permission? | B: kms:Decrypt | ✅ | Multipart reassembly needs kms:Decrypt. Single-part only needs GenerateDataKey. | Q744, Q765 | S3 multipart + KMS (Dojo T2 Q43) |
| 774 | D5 | EC2 encrypted EBS won't start, key policy only has Decrypt + GenerateDataKeyWithoutPlaintext — cause? | B: kms:CreateGrant missing | ✅ | EC2 always delegates to EBS backend via CreateGrant. Always needed. | Q745, Q767 | EC2 EBS + kms:CreateGrant (Dojo T2 Q47) |
| 775 | D5 | Need encrypted data key NOW but plaintext LATER — which API? | B: GenerateDataKeyWithoutPlaintext | ✅ | Returns only encrypted key. Call Decrypt later when ready. | Q743 | GenerateDataKey variants (Dojo T2 Q33) |
| 776 | D4 | SCP allows ec2+s3+lambda only, IAM grants kms:CreateKey — result? | C: Denied — implicit deny (not in SCP Allow) | ✅ | SCP is ceiling. Action not listed = implicitly denied. | Q747 | SCP ceiling implicit deny (Dojo T2 Q65) |
| 777 | D4 | Created roles must never exceed s3:GetObject+logs:*, least admin effort — approach? | B: Permission boundary via SCP condition | ✅ | Boundary delegation pattern. SCP forces boundary on CreateRole. | Q746, Q768 | Permission boundary delegation (Dojo T2 Q61) |
| 778 | D4 | Cognito User Pool + need temp AWS creds for S3 upload — which TWO? | B+A (wrong: picked AssumeRoleWithWebIdentity) | ❌ | B+D: Identity Pool + define authenticated IAM role. Identity Pool handles STS internally. | — | Cognito Identity Pool + role (not direct STS) |
| 779 | D3 | Non-HTTP binary protocol, TLS on port 9100, health checks — which LB? | B: NLB with TLS listener | ✅ | NLB = any TCP/UDP + TLS termination on any port. ALB = HTTP only. | Q752 | NLB vs ALB vs GWLB (Dojo T2 Q49) |
| 780 | D1 | GuardDuty findings severity >= 7, trigger Lambda, least services — architecture? | B: GuardDuty → EventBridge → Lambda | ✅ | GuardDuty publishes directly to EventBridge. No Security Hub needed. | — | GuardDuty direct to EventBridge |
| 781 | D3 | Flow Log: inbound ACCEPT + outbound REJECT — which TWO true? | A+E (wrong: picked SG outbound) | ❌ | B+C: NACL blocking return + issue on response path. SG is stateful — never causes this pattern. | Q707 | NACLs stateless (inbound ACCEPT + outbound REJECT) |
| 782 | D4 | On-prem AD + SSO + WorkSpaces + RDS SQL + cloud-only accounts — which Directory? | B: Managed AD + two-way trust | ✅ | RDS SQL + cloud users = Managed AD always. Two-way = bidirectional access. | Q709, Q734 | Managed AD + two-way trust |

### Session 80 — 2026-06-11

**Domains:** Cross-domain (Dojo combined gap drill — KMS operational, IAM wording traps, service selection, troubleshooting)
**Score:** 13 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 783 | D4 | Cognito User Pool + need temp AWS creds for S3 upload — which TWO? | B+D: Identity Pool + authenticated role mapping | ✅ | Identity Pool + define authenticated IAM role. Identity Pool handles STS internally. | Q778 | Cognito Identity Pool + role (not direct STS) |
| 784 | D3 | Flow Log: inbound ACCEPT port 443 + outbound REJECT ephemeral — cause? | B: NACL missing outbound ephemeral | ✅ | NACLs stateless — need explicit outbound rule. SGs are stateful. | Q781 | NACLs stateless (inbound ACCEPT + outbound REJECT) |
| 785 | D2 | InstanceCredentialExfiltration.InsideAWS, contain without breaking legitimate? | B: Deny-all SG on attacker's instance | ✅ | InsideAWS = both share role, TokenIssueTime breaks both. Isolate attacker. | Q761 | InsideAWS = SG isolation |
| 786 | D5 | S3 multipart 15-50GB + SSE-KMS, fails at complete step — missing permission? | B: kms:Decrypt | ✅ | Multipart = GenerateDataKey + Decrypt (reassembly). S3 never uses kms:Encrypt. | Q744, Q765 | S3 multipart + KMS |
| 787 | D5 | EC2 encrypted EBS won't start, has kms:Decrypt + GenerateDataKeyWithoutPlaintext — missing? | B: kms:CreateGrant | ✅ | EC2 always delegates to EBS backend via grants. Always needed. | Q745, Q767 | EC2 EBS + kms:CreateGrant |
| 788 | D5 | Need encrypted data key now, plaintext later — which API? | B: GenerateDataKeyWithoutPlaintext | ✅ | Returns only encrypted key. Call Decrypt later when ready. | Q743 | GenerateDataKey variants |
| 789 | D4 | SCP Allow ec2+s3+lambda only, IAM grants kms:CreateKey — result? | C: Denied — implicit deny | ✅ | SCP is ceiling. Action not listed = implicitly denied. | Q747 | SCP ceiling implicit deny |
| 790 | D4 | Devs create roles but can't exceed s3:GetObject+logs:*, least effort? | B: SCP requiring PermissionsBoundary | ✅ | Boundary delegation pattern. SCP forces boundary on CreateRole. | Q746, Q768 | Permission boundary delegation |
| 791 | D4 | Cognito User Pool token + direct AssumeRoleWithWebIdentity — what's wrong? | A: User Pool tokens can't be used with STS directly — use Identity Pool | ✅ | Identity Pool is the managed STS layer. Don't call STS directly. | Q778 | Cognito Identity Pool + role (not direct STS) |
| 792 | D3 | Non-HTTP binary protocol, TLS on port 6379, health checks — which LB? | B: NLB with TLS listener | ✅ | NLB = any TCP/UDP + TLS on any port. ALB = HTTP only. | Q752 | NLB vs ALB vs GWLB |
| 793 | D1 | Detect unusual API call volume vs 30-day baseline, least overhead? | B: CloudTrail Insights | ✅ | Insights = volume (statistical baseline). GuardDuty = behavior (threat intel). | — | CloudTrail Insights vs GuardDuty |
| 794 | D1 | EventBridge rule on ConsoleLogin never fires, Event History shows logins, Write-only trail — cause? | B: Trail Write-only, ConsoleLogin is Read | ✅ | EventBridge only receives events the trail delivers. Event History shows all. | Q710 | CloudTrail management events Read/Write |
| 795 | D1 | Suppress GD findings from pen-test EC2 with private IPs only — approach? (TWO) | B+A: EIPs + Trusted IP list, or suppression rule on instance IDs | ✅ | Trusted IP list = public IPs only. Suppression rule = alternative. | Q711 | GuardDuty Trusted IP list + suppression rules |

### Session 81 — 2026-06-11

**Domains:** Cross-domain (novel topics drill — encryption context, EKS runtime, presigned URLs, Glacier Vault Lock, CloudFront headers, IAM Roles Anywhere, S3 Object Lambda, declarative policies)
**Score:** 12 ✅ · 2 ⚠️ · 4 ❌ (67% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 796 | D5/D4 | Encryption context in key policy + PrincipalTag ABAC, engineering Lambda reads finance object — result? | B: Fails — context mismatch blocks Decrypt | ✅ | Key policy evaluates encryption context against caller's PrincipalTag at decrypt time. | — | Encryption context + key policy ABAC |
| 797 | D1/D3 | EKS Runtime Monitoring enabled, crypto miner in pod, no findings, audit log works — cause? | B: Runtime only detects network threats | ❌ | A: Runtime Monitoring needs agent (DaemonSet). Audit Log = agentless. No agent = no runtime findings. | — | EKS Runtime Monitoring (agent required) |
| 798 | D5/D3 | Lambda generates presigned URL, partners upload from internet fails, VPC Gateway endpoint exists — cause? | B: Bucket policy sourceVpce condition | ✅ | Bucket policy restricts to VPC endpoint. Partner's internet request doesn't traverse endpoint. | — | Presigned URL + sourceVpce |
| 799 | D6/D5 | Deploy to EC2 + on-prem + rotate creds, proposes Elastic Beanstalk — TWO issues? | A+E: EB can't do on-prem + CodeDeploy is correct | ✅ | Elastic Beanstalk = EC2 only. CodeDeploy + Secrets Manager is correct. | — | CodeDeploy on-prem + Secrets Manager |
| 800 | D5 | WORM 7yr, root can't delete, irreversible once confirmed — approach? | A: Object Lock Compliance | ⚠️ | B: Glacier Vault Lock. "Irreversible once confirmed" = Vault Lock (24hr confirm, then permanent). Object Lock = per-object retention. | — | Glacier Vault Lock vs Object Lock |
| 801 | D3 | CloudFront missing HSTS/CSP/X-Content-Type headers, least overhead — approach? | B: Lambda@Edge | ❌ | A: CloudFront response headers policy (managed, zero code). Lambda@Edge = only for dynamic/conditional logic. | — | CloudFront response headers policy |
| 802 | D5/D4 | S3 Access Point VPC-only, partner needs internet access — solution? | A: Create second Access Point with NetworkOrigin Internet | ✅ | VPC-only AP is permanent. Create separate AP for internet access. | — | S3 Access Points VPC restriction |
| 803 | D1/D3 | Container CVE in Inspector + active reverse shell — which statement true? | B: GD Runtime detects exploitation, Inspector detects CVE — both needed | ✅ | Inspector = static CVE. GuardDuty Runtime = active exploitation. Complementary. | — | Inspector + GuardDuty Runtime complementary |
| 804 | D5 | S3 CRR + encryption context + destination key policy condition — staging object replication? | B: Fails — destination key rejects staging context | ✅ | CRR preserves encryption context. Destination key policy evaluates it. Per-object failure. | — | Encryption context + CRR |
| 805 | D4 | On-prem server, X.509 cert, short-lived creds, least overhead — approach? | B: IAM Roles Anywhere + trust anchor + profile | ✅ | Roles Anywhere = exchange X.509 for temp STS creds. Designed for on-prem. | — | IAM Roles Anywhere |
| 806 | D1 | Two GD findings correlated into attack sequence in console — which feature? | B: Security Hub insight | ⚠️ | C: GuardDuty Extended Threat Detection (Dec 2024, likely not testable yet). Too new for exam. | — | GuardDuty Extended Threat Detection (too new) |
| 807 | D5/D4 | Same bucket, analytics needs PII redacted, compliance needs full — least duplication? | B: S3 Object Lambda AP for analytics + standard AP for compliance | ✅ | Object Lambda transforms on read. Zero duplication, per-team view. | — | S3 Object Lambda Access Point |
| 808 | D6/D3 | Guarantee no public IPs regardless of ANY API (current or future) — approach? | B: Declarative policy | ✅ | Declarative policy enforces STATE. SCP blocks specific APIs (must enumerate). | — | Declarative policies vs SCP |
| 809 | D1 | Route 53 Resolver logs not appearing in CW Logs, VPC Flow Logs work fine — cause? | B: Log group resource policy missing | ✅ | Route 53 Resolver → CW Logs uses log group resource policy, not IAM role. | — | Log delivery mechanisms (R53 Resolver) |
| 810 | D2 | Trojan finding, preserve volatile memory + disk evidence — sequence? | C: Deny-all SG → EBS snapshot → terminate | ❌ | B: Deny-all SG → no-reboot AMI (memory) → EBS snapshot (disk). Terminate = memory lost. | — | No-reboot AMI for volatile memory |
| 811 | D5/D3 | S3 SSE-KMS uploads work, direct kms:Decrypt times out — fix? | B: Add Interface endpoint for KMS + SG 443 | ✅ | S3 SSE-KMS = server-side (no endpoint needed). Direct KMS call = needs KMS Interface endpoint. | Q685 | KMS endpoint for direct calls only |
| 812 | D5 | Asymmetric KMS keys, sign artifacts, customers verify — which flow? | A: Sign with public key | ❌ | B: Sign with private → verify with public → integrity + non-repudiation. Can't sign with public. | — | Sign=private, verify=public |
| 813 | D3 | Credential stuffing from 3 countries + rate limit 200/5min — where + rules? (TWO) | B+C: WAF on CloudFront + geo-match + rate-based | ✅ | WAF on CF blocks at edge. Geo-match + rate-based in same Web ACL. | — | WAF geo + rate on CloudFront |


### Session 82 — 2026-06-11

**Domains:** Cross-domain (novel topics killer drill — ACM regions, Config remediation, encryption context ABAC, GWLB, declarative policies, S3 Access Grants, IR forensics)
**Score:** 5 ✅ · 0 ⚠️ · 2 ❌ (71% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 814 | D5/D3 | CloudFront + 2 ALBs (us-west-2 + eu-west-1), eu-west-1 ALB cert errors — cause? | C: Cert provisioned in us-west-2 instead of eu-west-1 | ✅ | ALB cert must be in ALB's region. CF cert = us-east-1. ALB cert = ALB's region. | — | ACM region requirements |
| 815 | D1/D6 | RDS DeletionProtection enforcement, 200 accounts, remediate 15min, least overhead? | B: Org Config managed rule + SSM Automation | ✅ | Org Config rule + SSM = detect + auto-remediate, least overhead, delegated admin. | — | Config org rule + SSM remediation |
| 816 | D5/D4 | Encryption context TenantId + PrincipalTag ABAC, alpha Lambda decrypts beta object — which TWO true? | B+C | ✅ | Context mismatch blocks Decrypt (B). Encryption context evaluated at KMS layer (C). | — | Encryption context + key policy ABAC |
| 817 | D3/D1 | Third-party IDS/IPS appliances, centralized inspection, scale + health check + transparent — component? | B: GWLB with GENEVE encapsulation | ✅ | GWLB = transparent inline inspection, GENEVE preserves headers, scales, health checks. | — | GWLB + third-party appliances |
| 818 | D4/D6 | Declarative policy vs SCP, new API assigns public IP — which protects without changes? | B: Declarative policy enforces state regardless of API | ✅ | Declarative = state enforcement. SCP = API-specific (must enumerate). | — | Declarative policies vs SCP |
| 819 | D1/D5 | S3 Access Grants, Finance analyst accesses Marketing prefix — cause? | C: Session policy bypass by bucket policy | ❌ | D: Access Grant location prefix overlaps with Marketing's prefix. Prefix misconfiguration = #1 operational issue. | — | S3 Access Grants prefix overlap |
| 820 | D2/D1/D4 | OutsideAWS credential exfil, can't stop instance, preserve + prevent IMDS — FOUR actions? | A+B+C+G | ❌ | A+C+D (+ question design error for 4th). TokenIssueTime (A) + EBS snapshot (C) + IMDSv2 hop limit 1 (D). B kills API traffic. G irrelevant. | — | OutsideAWS IR + IMDSv2 hardening |


### Session 83 — 2026-06-12

**Domains:** Cross-domain (priority re-test — Sessions 81-82 errors)
**Score:** 3 ✅ · 0 ⚠️ · 4 ❌ (43% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 821 | D1/D3 | EKS Runtime Monitoring, crypto miner in pod, zero findings, audit log works, no DaemonSet — cause? | B: GuardDuty security agent not deployed | ✅ | Runtime Monitoring needs agent (DaemonSet). Audit Log = agentless. No agent = no runtime findings. | Q797 | EKS Runtime Monitoring (agent required) |
| 822 | D5 | WORM 10yr, policy permanently irreversible after 24hr confirm, even AWS Support can't modify — approach? | A: Object Lock Compliance | ❌ | B: Glacier Vault Lock. "24hr confirm + permanently irreversible" = Vault Lock. Object Lock = per-object retention with expiry. | Q800 | Glacier Vault Lock vs Object Lock |
| 823 | D3 | Static HSTS/CSP/X-Content-Type headers on CloudFront, least overhead? | B: CloudFront response headers policy | ✅ | Managed, zero code. Lambda@Edge = only for dynamic/conditional logic. | Q801 | CloudFront response headers policy |
| 824 | D5 | Asymmetric KMS, devs sign artifacts, customers verify offline with public key — correct flow? | A: Sign with public key | ❌ | B: Sign with private → verify with public. Private signs, public verifies. Always. | Q812 | Sign=private, verify=public |
| 825 | D2 | Trojan C2Activity, preserve volatile memory + disk, can't stop instance — TWO actions? | B+E | ❌ | A+B: EBS snapshot (disk) + no-reboot AMI (memory). Deny-all SG doesn't dump memory. | Q810 | No-reboot AMI for volatile memory |
| 826 | D1/D5 | S3 Access Grants, Finance grant for /finance/, analyst lists marketing-budgets/ — cause? | B: Prefix /finance matches finance-adjacent | ❌ | D: Grant location set to root (s3://data-lake/) instead of s3://data-lake/finance/. marketing-budgets starts with 'm', never matches 'finance' prefix. | Q819 | S3 Access Grants prefix overlap |
| 827 | D2/D4 | OutsideAWS, API must stay up, stop attacker + preserve disk + prevent IMDS SSRF — THREE? | A+C+D | ✅ | TokenIssueTime (A) + EBS snapshot (C) + IMDSv2 hop limit 1 (D). Deny-all SG kills API. | Q820 | OutsideAWS IR + IMDSv2 hardening |


### Session 84 — 2026-06-12

**Domains:** Cross-domain (priority re-test #2 — Sessions 81-83 errors, reinforcement)
**Score:** 6 ✅ · 0 ⚠️ · 1 ❌ (86% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 828 | D5 | Audit records in Glacier, policy cannot be altered after validation, brief testing before permanent? | C: Glacier Vault Lock | ✅ | Vault Lock — initiate, 24hr test, complete = permanent. | Q800, Q822 | Glacier Vault Lock vs Object Lock |
| 829 | D5 | Asymmetric KMS, signed binaries, customers verify offline, junior says verification needs KMS — correct? | B: No — public key verifies offline | ✅ | Private signs (KMS). Public verifies (offline). | Q812, Q824 | Sign=private, verify=public |
| 830 | D2 | Trojan C2Activity, capture volatile memory + disk, instance must not stop — TWO actions? | B+C (dd /dev/mem) | ❌ | A+B: EBS snapshot (disk) + no-reboot AMI (memory). dd /dev/mem restricted on modern kernels. | Q810, Q825 | No-reboot AMI for volatile memory |
| 831 | D1/D5 | Access Grants, Engineering grant for /engineering/, engineer reads /hr/salaries/ — check FIRST? | B: Grant location set to root | ✅ | Prefix too broad (root instead of department). | Q819, Q826 | S3 Access Grants prefix overlap |
| 832 | D2/D4 | InsideAWS, stolen creds on different EC2 same role, stop attacker without breaking production? | B: Deny-all SG on attacker's instance | ✅ | InsideAWS = SG isolation. TokenIssueTime breaks both. | Q761, Q825 | InsideAWS = SG isolation |
| 833 | D5 | S3 objects undeletable 5 years exactly, auto-deletable after, root can't override — config? | B: Object Lock Compliance 5yr | ✅ | Fixed per-object retention with expiry = Object Lock Compliance. | Q800, Q822 | Glacier Vault Lock vs Object Lock |
| 834 | D5 | Asymmetric KMS sign, on-prem Jenkins no AWS creds, verify signature — how? | B: Download public key, verify locally OpenSSL | ✅ | Public key offline verification. No AWS needed. | Q812, Q824 | Sign=private, verify=public |


### Session 85 — 2026-06-12

**Domains:** D1 Detection + D2 Incident Response (killer targeted drill — weakest domains)
**Score:** 13 ✅ · 0 ⚠️ · 1 ❌ (93% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 835 | D1 | SSE-KMS, alert on 10x volume + never-seen IP, no Lambda/filters/infra — service? | B: GuardDuty S3 Protection | ✅ | Anomalous volume + novel IP + zero infra = GuardDuty S3 Protection. | Q568, Q581 | Detect vs prevent (GuardDuty vs policy) |
| 836 | D1/D6 | Alert 90s on iam:DeleteRolePolicy + alert on S3 baseline deviation — which TWO? | B: EventBridge + GuardDuty S3 Protection | ✅ | Specific API fast = EventBridge. Behavioral = GuardDuty. | Q474, Q681 | EventBridge + GuardDuty S3 Protection |
| 837 | D1/D3 | C2Activity finding, attacker hardcoded IP (no DNS), block VPC-wide — action? | B: Network Firewall DROP on C2 IP | ✅ | Hardcoded IP = DNS FW useless. NF drops by IP. SGs can't deny. | Q526, Q571 | Network FW for IP-level C2 block |
| 838 | D2 | Trojan 8.9, capture running processes + network conns + kernel modules, no reboot — action? | B: No-reboot AMI | ✅ | No-reboot AMI = volatile memory capture. EBS = disk only. | Q810, Q825, Q830 | No-reboot AMI for volatile memory |
| 839 | D1 | RCP blocks external, 500 denied GetObjects, GD + AA enabled — which true? | C: Only AA fires | ❌ | D: Both B+C true. GD no finding (blocked). AA flags policy (static). Both independent. | Q534, Q594 | GuardDuty ≠ failed attempts + AA static |
| 840 | D1 | EC2 DNS to C2 beacon, then TLS TCP to resolved IP — ThreatPurpose order? | B: Impact then Trojan | ✅ | DNS = Impact. Active TCP to C2 = Trojan. CryptoCurrency = mining only. | Q655, Q671 | GuardDuty finding types (C2 = Trojan) |
| 841 | D1 | GD enabled 6 months all regions, 50 EC2s, zero findings, VPC Flow Logs not enabled — cause? | C: Suppression rule | ✅ | GD reads Flow Logs internally. Zero findings + active workloads = suppression rule. | Q372, Q389 | GuardDuty suppression rules |
| 842 | D1/D4 | Bucket policy grants external, no access yet, GD + AA enabled — which TWO true? | B+D: AA fires (static) + GD fires after actual access | ✅ | AA = static policy. GD = needs actual anomalous access. Independent. | Q518, Q534 | Access Analyzer + GuardDuty both fire |
| 843 | D1 | Detect kms:DisableKey 400 accounts within 60s, org trail exists — approach? | C: EventBridge in management account | ✅ | Specific API + fast + org trail = EventBridge. | Q474, Q570 | EventBridge for API call detection |
| 844 | D1 | EC2 active TCP to mining pool IP port 3333, sustained — ThreatPurpose? | C: CryptoCurrency | ✅ | Active TCP to mining pool = CryptoCurrency. | Q226, Q489 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 845 | D1/D3 | DGADomainRequest finding, all via DNS, block VPC-wide — approach? | C: DNS Firewall allow-list | ✅ | DGA = unpredictable. Can't enumerate. Allow-list = block all except known-good. | Q690 | DGA = allow-list DNS Firewall |
| 846 | D1/D6 | Prevent StopLogging + detect PutBucketPolicy 2min + block external S3 — THREE services? | B: SCP + EventBridge + RCP | ✅ | SCP prevents. EventBridge detects API. RCP blocks consequence. | Q688 | Full detect/prevent architecture |
| 847 | D2/D1 | OutsideAWS, API must stay up, stop attacker + preserve + prevent SSRF — combo? | B: TokenIssueTime + EBS snapshot + IMDSv2 hop 1 | ✅ | Deny-all SG kills API. TokenIssueTime + snapshot + IMDSv2. | Q820, Q827 | OutsideAWS IR + IMDSv2 hardening |
| 848 | D1 | GD org-wide, admin suppression <4, member suppression all pen-test — both valid? | B: Both valid, operate independently | ✅ | Admin + member can both create suppression rules independently. | Q372 | GuardDuty suppression rules |


### Session 86 — 2026-06-12

**Domains:** Cross-domain (killer difficulty — novel operational scenarios, cross-account patterns, ACM, Config, Kinesis)
**Score:** 9 ✅ · 0 ⚠️ · 8 ❌ (53% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 849 | D1/D4 | RCP blocks external, 200 denied GetObjects, AA + GD enabled — which TWO true? | B+C: AA fires + GD doesn't fire | ✅ | AA = static policy. GD = no successful access = no finding. | Q534, Q839 | GuardDuty ≠ failed attempts + AA static |
| 850 | D4/D5 | ECS task retrieves secret, KMS key policy updated to remove task's account, retry Decrypt — result? | D: Fails on secretsmanager:GetSecretValue | ❌ | B: Fails on kms:Decrypt — key policy no longer names external account, cross-account KMS broken. | Q541, Q669 | Cross-account KMS key policy must name external account |
| 851 | D3 | IoT device publishes to other device's topic by spoofing MQTT client ID — fix? | B: Replace ${iot:ClientId} with ${iot:Connection.Thing.ThingName} | ✅ | ThingName = server-registered (trusted). ClientId = client-supplied (untrusted). | — | IoT ThingName vs ClientId |
| 852 | D1 | CloudTrail Lake org-level, architect expects 30s latency — limitation? | C: Lake latency is 5-15 min, not sub-minute | ✅ | Near real-time ≠ sub-minute. EventBridge for seconds. | — | CloudTrail Lake latency |
| 853 | D6/D1 | Org Config custom rule fails in member accounts "Lambda function not found" — fix? | C: Lambda resource-based policy allowing config.amazonaws.com from members | ✅ | Org custom rule invokes Lambda in delegated admin account. Resource policy needed. | — | Config org custom rule cross-account invoke |
| 854 | D1/D3 | 50GB/hr WAF logs, real-time full-text search + 90d retention + User-Agent alerts — architecture? | A: Firehose + OpenSearch + UltraWarm + alerting | ✅ | Full-text + sub-second + dashboards = OpenSearch. | — | Kinesis + OpenSearch architecture |
| 855 | D5/D4 | S3 Batch Operations cross-account re-encrypt 12M objects — which TWO required? | A+E: Decrypt/GenerateDataKey + service principal key policy | ❌ | A+D: KMS perms correct + manifest must be in same region as job. Batch uses YOUR role, not service principal. | — | S3 Batch Operations cross-account + manifest region |
| 856 | D3/D5 | Lambda private subnet, direct kms:Decrypt times out, SM + DDB work — cause? | A: KMS Interface endpoint deleted | ✅ | Direct KMS call = needs endpoint. Timeout = network. SM has its own endpoint. | Q685 | KMS endpoint for direct calls only |
| 857 | D4/D6 | S3 Batch Operations 100% failure PutObjectTagging cross-account, role has s3:* Resource:* — cause? | A: Batch Operations can't operate cross-account | ❌ | B: Member bucket policies don't grant the batch job role access. Cross-account S3 = both sides. | — | S3 Batch cross-account needs bucket policy |
| 858 | D4/D6 | Detect CreateRole without boundary within 2 min + delete within 5 min — which TWO? | A (only one selected) | ❌ | C: SCP preventing creation entirely = least overhead (prevention > detection). A valid for detect+fix. | — | SCP prevention > detect+remediate |
| 859 | D5/D3 | ACM cert "not found" on ap-southeast-1 ALB, cert issued and valid — cause? | A: Cert in wrong region (must be in ALB's region) | ✅ | ACM certs are regional. ALB cert must be in ALB's region. | — | ACM region requirements |
| 860 | D1 | CW metric filter on StopLogging, alarm worked in test, real attack undetected — cause? | D: Trail already stopped by prior StopLogging | ❌ | A: StopLogging stops delivery of its own event to CW Logs — metric filter never sees it. | — | StopLogging kills own CW Logs delivery |
| 861 | D5 | Private CA cert renewed, existing 24hr microservice certs have 20hr remaining — what happens? | B: Existing certs continue working until natural expiry | ✅ | CA renewal doesn't invalidate previously-issued certs. | — | Private CA renewal ≠ revocation |
| 862 | D2 | Developer keys on GitHub 6hrs, attacker used from foreign IP — which TWO FIRST? | B+D: Deactivate keys + Detective | ❌ | B+C: Deactivate keys + inline Deny-all (covers second key/console/sessions). Contain before investigate. | — | Credential leak IR (Deny-all before investigate) |
| 863 | D4/D5 | SCP Deny kms:* unless ViaService=s3, Lambda reads+writes S3 SSE-KMS — result? | A: Both succeed — S3 calls KMS server-side | ✅ | ViaService satisfied for both Decrypt and GenerateDataKey when S3 initiates. | Q488 | kms:ViaService + SCP |
| 864 | D5/D6 | Config auto-remediation S3 logging fails "role does not have permission" — missing? | D: s3:PutBucketPolicy on target | ❌ | A: s3:GetBucketAcl — S3 access logging uses ACLs (legacy), not bucket policies. | — | S3 server access logging = ACLs |
| 865 | D5/D3 | Kinesis encrypted stream, new consumer Lambda Access Denied — missing permission? | A: kms:Decrypt on stream's KMS key | ✅ | Consumer decrypts. Producer generates data key. Same pattern as S3. | — | Kinesis consumer = kms:Decrypt |


### Session 87 — 2026-06-15

**Domains:** Cross-domain (Session 86 re-test + Week 1 novel topics — ACM, IoT, Kinesis, Config custom rules, CloudTrail Lake, S3 Batch)
**Score:** 9 ✅ · 0 ⚠️ · 8 ❌ (53% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 866 | D1 | CW metric filter on StopLogging, alarm worked in test, real attack undetected — cause? | D: Metric filter value changed to 0 | ❌ | C: StopLogging stops its own event delivery to CW Logs — metric filter never sees it. | Q860 | StopLogging kills own CW Logs delivery |
| 867 | D2 | Keys on GitHub 4hrs, attacker created new keys + console access — which TWO FIRST? | C+B: Deny-all + Detective | ❌ | A+C: Deactivate exposed keys + attach inline Deny-all to user. Contain ALL paths before investigating. | Q862 | Credential leak IR (Deny-all before investigate) |
| 868 | D5/D6 | Config auto-remediation S3 logging fails "role does not have permission" — missing? | C: logs:CreateLogGroup | ❌ | A: s3:GetBucketAcl — S3 server access logging uses ACLs (legacy), not bucket policies. | Q864 | S3 server access logging = ACLs |
| 869 | D5/D4 | S3 Batch Operations cross-account re-encrypt 15M objects, 100% failure — cause? | B: Member bucket policies don't grant batch role | ✅ | Cross-account S3 = both sides must agree. | Q857 | S3 Batch cross-account needs bucket policy |
| 870 | D4/D5 | Cross-account ECS task, KMS key policy removes task's account — at which layer fails? | A: secretsmanager:GetSecretValue | ❌ | B: kms:Decrypt — key policy no longer enables cross-account delegation at KMS layer. | Q850 | Cross-account KMS key policy must name external account |
| 871 | D4/D6 | SCP denies CreateRole without boundary, engineer proposes EventBridge+Lambda detect+delete — why rejected? | C: SCP already prevents — detection redundant | ✅ | Prevention > detect+remediate when bad state can never exist. | Q858 | SCP prevention > detect+remediate |
| 872 | D5 | S3 Batch Operations same-account, manifest us-east-1, target eu-west-1, job us-east-1 — result? | A: Succeeds cross-region | ❌ | C: Fails — job must be created in target bucket's region. Batch is regional. | Q855 | S3 Batch Operations regional |
| 873 | D5/D3 | CloudFront + 3 ALBs (3 regions), custom domain HTTPS — minimum ACM certs? | B: 4 (1 CF + 3 ALBs) | ✅ | ACM is regional. CF cert in us-east-1 + 1 per ALB region. | — | ACM regional requirements |
| 874 | D3 | IoT fleet, Device A publishes to Device B's topic via clientId spoofing — fix? | B: Replace ${iot:ClientId} with ${iot:Connection.Thing.ThingName} | ✅ | ThingName = server-registered (trusted). ClientId = client-supplied (untrusted). | — | IoT ThingName vs ClientId |
| 875 | D1/D3 | 200GB/hr WAF logs, full-text search, sub-second, 90d, alerts, dashboards — architecture? | B: Firehose + OpenSearch (UltraWarm) + alerting | ✅ | Full-text + sub-second + dashboards = OpenSearch. Firehose = managed ingestion. | — | Kinesis + OpenSearch architecture |
| 876 | D6/D1 | Config org custom rule, Lambda in delegated admin, member accounts "Unable to invoke" — fix? | B: Lambda resource-based policy allow config.amazonaws.com from members | ✅ | Org custom rule invokes central Lambda cross-account. Resource policy needed. | — | Config org custom rule cross-account invoke |
| 877 | D1 | CloudTrail Lake SQL: AssumeRole outside corporate CIDR — correct syntax? | A: SELECT * FROM event_data_store WHERE eventName='AssumeRole' AND sourceIPAddress NOT LIKE '10.%' | ✅ | Lake SQL uses top-level fields + LIKE for pattern matching. | — | CloudTrail Lake SQL syntax |
| 878 | D5/D3 | ACM cert in us-east-1 attached to ap-southeast-1 ALB — result? | B: Fails — ACM regional, must provision in ALB's region | ✅ | ACM certs are strictly regional. | — | ACM regional (cross-region attach fails) |
| 879 | D5/D3 | Kinesis encrypted stream, consumer Lambda Access Denied, has GetRecords — missing? (TWO) | A only (missed D) | ❌ | A+D: kms:Decrypt + kms:DescribeKey. Consumer needs both for encrypted streams. | — | Kinesis consumer = Decrypt + DescribeKey |
| 880 | D3 | IoT policy uses ThingName, attacker steals cert, uses from different device — can publish? | B: No — hardware attestation | ❌ | A: Yes — ThingName bound to certificate, not physical device. Stolen cert = full impersonation. | — | IoT ThingName = cert-bound, not hardware |
| 881 | D6/D1 | Config org custom rule, Lambda needs 5min, evaluations timeout — fix? | B: Switch to SSM Automation | ❌ | A: Increase Lambda timeout to 15 minutes. Config evaluates with Lambda (max 15min). | — | Config custom rule = Lambda (max 15min timeout) |
| 882 | D1 | CloudTrail Lake org EDS, query returns zero results despite activity — TWO causes? | A+D: Management events only + no backfill | ✅ | EDS config (mgmt vs data) + Lake doesn't backfill historical events. | — | CloudTrail Lake no backfill + event type config |


### Session 88 — 2026-06-15

**Domains:** Cross-domain (score uplift drill — CRR+KMS, StopLogging, IR containment, multipart, EBS, IoT, Config custom rules)
**Score:** 7 ✅ · 0 ⚠️ · 3 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 883 | D5 | S3 CRR cross-account, replication role has kms:Encrypt on dest key, fails — missing? | B: Source key policy missing Decrypt | ❌ | C: Dest key needs kms:GenerateDataKey, not kms:Encrypt. S3 never uses kms:Encrypt. | — | CRR dest = kms:GenerateDataKey (not Encrypt) |
| 884 | D1 | Org trail + EventBridge rule in mgmt account, attacker calls StopLogging in member — fires? | A: Yes — org trail delivers to mgmt EventBridge | ✅ | Org trail delivers all member management events to management account EventBridge. | Q860, Q866 | Org trail + EventBridge detection |
| 885 | D1 | Three detection mechanisms for StopLogging (CW filter, EventBridge, Config) — which work? | B: Only EventBridge + Config | ✅ | CW metric filter blind (StopLogging kills own delivery). EB + Config both detect. | Q860, Q866 | StopLogging kills own CW Logs delivery |
| 886 | D2 | Attacker created 2nd key + console + EC2, broadest single containment action? | C: Inline Deny-all on IAM user | ✅ | Blocks all paths (both keys, console, sessions) with one action. | Q862, Q867 | Credential leak IR (Deny-all before investigate) |
| 887 | D5 | 20GB multipart SSE-KMS fails at CompleteMultipartUpload, has GenerateDataKey — missing? | B: kms:Decrypt | ✅ | Multipart reassembly needs Decrypt. Single-part only needs GenerateDataKey. | Q744, Q765 | S3 multipart + KMS |
| 888 | D5 | S3 CRR SSE-KMS, encryption context on dest object shows source or dest bucket ARN? | A: Source (preserves) | ❌ | B: Dest — S3 rewrites context to dest bucket ARN. Key policy conditions must reference dest. | — | CRR rewrites encryption context to dest |
| 889 | D5 | EC2 encrypted EBS fails to start, key policy has Decrypt + GenerateDataKeyWithoutPlaintext only — missing? | B: kms:CreateGrant | ✅ | EC2 always delegates to EBS backend via grants. | Q745, Q767 | EC2 EBS + kms:CreateGrant |
| 890 | D3/D1 | C2Activity finding, C2 IP hardcoded (no DNS), block VPC-wide — action? | B: Network Firewall DROP on C2 IP | ✅ | Hardcoded IP = DNS FW useless. NF drops by IP. | Q526, Q571 | Network FW for IP-level C2 block |
| 891 | D6/D1 | Config org custom rule Lambda 8min, timing out at 3min — fix? | A: Increase Lambda timeout to 15 minutes | ✅ | Config evaluates with Lambda (sync, max 15min). | Q881 | Config custom rule = Lambda (max 15min timeout) |
| 892 | D3 | IoT cert revoked in IoT Core, attacker still has private key, attempts connect — result? | D: Succeeds until CRL propagates | ❌ | B: Connection fails immediately — IoT Core checks registry status at TLS handshake (instant). | — | IoT cert revocation = instant (no CRL delay) |


### Session 89 — 2026-06-15

**Domains:** Cross-domain (score uplift drill #2 — CRR, IoT, S3 Batch, DynamoDB KMS, ViaService, EBS encryption)
**Score:** 7 ✅ · 0 ⚠️ · 3 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 893 | D5 | S3 CRR cross-account, replication role has Decrypt+GenerateDataKey, dest key policy only grants dest root — cause? | A: CMK-B key policy must grant replication role | ✅ | Cross-account KMS: key policy must name external principal. | Q883 | CRR dest key policy must name replication role |
| 894 | D3 | IoT cert revoked 30 seconds ago, attacker attempts new MQTT connection — result? | B: Fails immediately — registry check at TLS handshake | ✅ | IoT Core = instant revocation, no CRL delay. | Q892 | IoT cert revocation = instant |
| 895 | D5/D3 | Lambda private subnet, direct GenerateDataKeyWithoutPlaintext times out, S3 reads work — fix? | A: Add KMS Interface endpoint | ✅ | S3 SSE-KMS = server-side. Direct KMS call = needs endpoint. | Q685 | KMS endpoint for direct calls only |
| 896 | D5 | CRR dest key policy condition checks source bucket ARN in encryption context — why fails? | B: CRR rewrites context to dest bucket ARN | ✅ | Dest key policy must reference dest bucket ARN. | Q888 | CRR rewrites encryption context to dest |
| 897 | D5 | S3 Batch Operations, manifest in us-east-1, job in ap-southeast-1 — result? | B: Job creation fails — manifest must be same region | ✅ | Batch = regional (job + manifest + target). | Q872 | S3 Batch Operations regional |
| 898 | D5 | Secrets Manager cross-region replication, source uses single-region CMK — works? | B: Yes — specify different key in dest, SM re-encrypts | ✅ | MRK not required for SM replication. | Q428 | Secrets Manager replication ≠ MRK |
| 899 | D5/D4 | DynamoDB CMK, Lambda has Decrypt+GenerateDataKey, Access Denied on PutItem — missing? | A: kms:Encrypt | ❌ | B: kms:CreateGrant + kms:DescribeKey — DynamoDB delegates via grants (like EBS). | — | DynamoDB + CMK = CreateGrant + DescribeKey |
| 900 | D4/D5 | SCP denies kms:* unless ViaService=s3, Lambda reads S3 + writes DynamoDB — which succeed? | D: Only S3 — ViaService value doesn't match for DDB | ✅ | DDB sets ViaService but value ≠ s3, so SCP Deny fires. | Q488 | kms:ViaService + SCP (service-specific match) |
| 901 | D5 | Lambda has s3:GetObject + kms:Decrypt + kms:GenerateDataKey, GetObject Access Denied — cause? | C: Needs kms:Decrypt explicitly | ❌ | B: Perms already correct — issue is another layer (endpoint policy, bucket policy). Reading trap. | — | Reading comprehension (perms already present) |
| 902 | D5/D6 | Ensure every new EC2 has encrypted EBS, preventive only — approach? | A: SCP denying RunInstances unless Encrypted=true | ❌ | D: EBS encryption by default + SCP together = full prevention. Either alone has gaps. | — | EBS encryption by default + SCP = full prevention |


### Session 90 — 2026-06-15

**Domains:** Cross-domain (surprise drill — S3 ACLs, GWLB, Roles Anywhere, Private CA, declarative policies, Kinesis, VPC endpoints)
**Score:** 6 ✅ · 0 ⚠️ · 4 ❌ (60% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 903 | D5 | S3 server access logging, target bucket policy uses service principal — why logs stopped? | C: Needs s3:PutObjectAcl | ❌ | A: S3 access logging uses ACLs, not service principals/bucket policies. | Q864, Q868 | S3 server access logging = ACLs |
| 904 | D5 | Private CA renewed (new key pair), existing 24hr certs have 20hr remaining — what happens? | B: Existing certs continue until expiry | ✅ | CA renewal ≠ revocation. Previously-issued certs unaffected. | — | Private CA renewal ≠ revocation |
| 905 | D3 | GWLB + IDS, source IP shows GWLB IP instead of original client — cause? | D: Enable X-Forwarded-For | ❌ | C: Appliance not decapsulating GENEVE outer header. GWLB preserves original via GENEVE. | — | GWLB GENEVE decapsulation |
| 906 | D4 | Roles Anywhere, cert expires, server has cached STS creds — when does access stop? | B: When current session expires | ✅ | Certificate validated at issuance only. Existing sessions continue. | — | Roles Anywhere session validity |
| 907 | D3 | Static HSTS/CSP headers on CloudFront, least overhead? | B: CF response headers policy | ✅ | Managed, zero code. Lambda@Edge = dynamic only. | Q801, Q823 | CloudFront response headers policy |
| 908 | D6/D1 | Config org custom rule works in admin, times out in members — cause? | D: Lambda VPC blocks outbound | ❌ | B: Lambda resource-based policy missing config.amazonaws.com from members. | Q876 | Config org custom rule cross-account invoke |
| 909 | D5/D3 | S3 Gateway endpoint policy allows Get+Put on data-bucket/*, Lambda calls ListBucket — result? | B: Fails — ListBucket not in endpoint policy | ✅ | Endpoint policy = explicit allow-list. | Q535 | Gateway endpoint policy as additional gate |
| 910 | D6/D3 | Guarantee no public IPs regardless of ANY API (current or future) — mechanism? | B: Declarative policy | ✅ | State enforcement vs API enumeration. | — | Declarative policies vs SCP |
| 911 | D5/D3 | Producer Lambda has PutRecord + GenerateDataKey, tries to read own records — why fails? | A: Only missing KMS perms | ❌ | C: Missing BOTH Kinesis read perms (GetRecords) AND KMS read perms (Decrypt+DescribeKey). | — | Reading comprehension (multiple missing perms) |
| 912 | D5/D4 | SCP denies PutObject if KMS key header ≠ specific key, upload without flags, default encryption set — result? | B: Denied — SCP before default encryption | ✅ | SCP evaluates request as-received. | Q426, Q626 | Default encryption vs SCP Deny |


### Session 91 — 2026-06-15

**Domains:** Cross-domain (Week 1 killer drill — CRR encryption context, StopLogging, credential leak IR, S3 logging, IoT revocation, Kinesis endpoints, S3 Batch, GWLB, Config custom rules, DynamoDB KMS)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 913 | D5/D3 | CRR cross-account, dest key policy checks encryption context against source bucket ARN — why fails? (TWO) | B+E | ✅ | B+E: CRR rewrites context to dest bucket ARN + ViaService sidesteps the problem. | Q888 | CRR rewrites encryption context to dest |
| 914 | D1/D6 | Org trail + CW metric filter on StopLogging doesn't fire, EventBridge does — why? | B | ✅ | B: StopLogging kills own CW Logs delivery — EventBridge receives directly from CloudTrail. | Q860, Q866 | StopLogging kills own CW Logs delivery |
| 915 | D2/D4 | Keys on GitHub 8hrs, attacker created 2nd keys + console + EC2 — broadest single containment? | B | ✅ | B: Inline Deny * on IAM user — blocks all paths simultaneously. | Q862, Q867 | Credential leak IR (Deny-all before investigate) |
| 916 | D5/D6 | Config auto-remediation S3 logging fails AccessDenied, has PutBucketLogging + PutObject — missing? | A | ✅ | A: s3:GetBucketAcl — S3 server access logging uses ACL mechanism for validation. | Q864, Q868, Q903 | S3 server access logging = ACLs |
| 917 | D3/D1 | IoT cert revoked 3 seconds ago, device attempts new MQTT connection — result? | B | ✅ | B: Fails immediately — IoT Core checks registry status at TLS handshake, no CRL delay. | Q892, Q894 | IoT cert revocation = instant (no CRL delay) |
| 918 | D5/D3 | Lambda private subnet, encrypted Kinesis, times out on GetRecords, SM works — fix? (TWO) | B+A | ❌ | A+D: Interface endpoint for Kinesis + Interface endpoint for KMS. Timeout = network, not permissions. | Q685, Q895 | Kinesis + KMS VPC endpoints (timeout = network) |
| 919 | D5 | S3 Batch Operations job in us-east-1 targeting ap-southeast-1 bucket — error cause? | B | ✅ | B: Batch Operations is regional — job must be in same region as target bucket. | Q872, Q897 | S3 Batch Operations regional |
| 920 | D3/D1 | GWLB + IDS, all logs show GWLB IP instead of client IPs — fix? | B | ✅ | B: Appliances must decapsulate GENEVE outer header — original IP in inner packet. | Q905 | GWLB GENEVE decapsulation |
| 921 | D6/D1 | Org Config custom rule, Lambda works locally, "Unable to invoke" in 150 members — fix? | B | ✅ | B: Lambda resource-based policy granting config.amazonaws.com with SourceAccount condition. | Q876, Q908 | Config org custom rule cross-account invoke |
| 922 | D5/D4 | DynamoDB CMK, Lambda has Decrypt+GenerateDataKey, PutItem Access Denied on KMS — missing? | B | ✅ | B: kms:CreateGrant + kms:DescribeKey — DynamoDB delegates via grants like EBS. | Q899 | DynamoDB + CMK = CreateGrant + DescribeKey |


### Session 92 — 2026-06-15

**Domains:** Cross-domain (Week 1 weekly drill — CRR custom context, IoT ThingName, Kinesis SGs, Config Lambda timeout, CloudTrail Lake, S3 Batch regional, GWLB GENEVE, DynamoDB CreateGrant, ACM regional, Config org rule)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 923 | D5 | CRR SSE-KMS, dest key policy checks aws:s3:arn, objects with custom encryption context fail — cause? | A | ❌ | B: CRR preserves source's custom encryption context, which causes mismatch at dest key policy expecting only S3 system context. | Q888, Q913 | CRR custom encryption context preserved |
| 924 | D3 | IoT ThingName policy, attacker steals cert, installs on different device — which statement true? | A | ✅ | A: Expected behavior — ThingName bound to cert, not hardware. Revoke cert to stop attacker. | Q880 | IoT ThingName = cert-bound, not hardware |
| 925 | D5/D3 | Lambda private subnet, Kinesis+KMS endpoints exist, GetRecords times out — fix? (TWO) | A+D | ✅ | A+D: Kinesis endpoint SG inbound 443 + Lambda SG outbound 443. Timeout = network (SGs). | Q918 | Kinesis + KMS VPC endpoints (timeout = SGs) |
| 926 | D6/D1 | Config org custom rule Lambda timeout 3min, check takes 4-7min — least disruptive fix? | A | ✅ | A: Increase Lambda timeout to 15 minutes — Config supports up to 15min. | Q881, Q891 | Config custom rule = Lambda (max 15min timeout) |
| 927 | D1 | CloudTrail Lake org EDS management-only, PutObject query returns zero — TWO causes? | A+C | ✅ | A+C: PutObject is data event (EDS mgmt only) + Lake doesn't backfill historical events. | Q882 | CloudTrail Lake (data vs mgmt + no backfill) |
| 928 | D5 | S3 Batch single job us-east-1, manifest lists objects in 4 regions — cause of failure? | A | ✅ | A: S3 Batch is regional — job must be same region as target. | Q872, Q897, Q919 | S3 Batch Operations regional |
| 929 | D3 | GWLB + IDS, logs show GWLB endpoint IP instead of client — fix? | C | ✅ | C: Appliances must decapsulate GENEVE outer header to access original packet. | Q905, Q920 | GWLB GENEVE decapsulation |
| 930 | D5/D4 | DynamoDB CMK, Lambda has Decrypt+GenerateDataKey+Encrypt, PutItem Access Denied — minimum additional? | B | ✅ | B: kms:CreateGrant — DynamoDB delegates via grants like EBS. | Q899, Q922 | DynamoDB + CMK = CreateGrant |
| 931 | D5/D3 | CloudFront + 2 regional ALBs, eu-west-1 ALB cert error — correct architecture? | A | ✅ | A: CF cert in us-east-1 + each ALB needs own regional ACM cert. | — | ACM regional requirements |
| 932 | D6/D1 | Config org custom rule "Lambda not found" in 180 members, works in admin — cause? | B | ✅ | B: Lambda resource-based policy missing config.amazonaws.com invoke with SourceAccount condition. | Q876, Q908, Q921 | Config org custom rule cross-account invoke |


### Session 93 — 2026-06-16

**Domains:** D2 Incident Response + D1 Detection (D2 never-seen services blitz + D1 decision validation)
**Score:** 6 ✅ · 1 ⚠️ · 4 ❌ (55% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 933 | D2/D1 | Trojan C2Activity, API must stay up, stop exfil + capture memory + preserve disk — THREE? | A+F+B | ⚠️ | A+B+C: TokenIssueTime + EBS snapshot + no-reboot AMI. F has broken dd /dev/mem. | Q810, Q825, Q830 | No-reboot AMI for volatile memory |
| 934 | D2 | Test GuardDuty→EventBridge→Step Functions pipeline without real incident — approach? | B: FIS | ❌ | A: CreateSampleFindings API. FIS injects infra failures, not security findings. | — | CreateSampleFindings vs FIS |
| 935 | D2 | Demonstrate RTO/RPO compliance to auditors, least overhead — service? | A: FIS | ❌ | B: Resilience Hub (assess architecture vs targets, generate report). FIS = test by breaking. | — | Resilience Hub = assess, FIS = test, ARC = recover |
| 936 | D2 | AZ degraded but health checks pass, stop traffic to AZ, no DNS/ASG changes — fastest? | C: Route 53 | ❌ | B: ARC zonal shift (LB-level, seconds, no DNS). Route 53 = DNS = excluded by question. | — | ARC zonal shift |
| 937 | D2 | Forensics Orchestrator: isolation succeeds but SSM memory acquisition fails — cause? | A: deny-all SG blocks SSM | ✅ | A: Deny-all SG blocks SSM agent outbound HTTPS. Need VPC endpoints or reorder workflow. | — | Forensics Orchestrator (deny-all blocks SSM) |
| 938 | D1 | Alert 90s on DeleteRolePolicy + alert on S3 baseline deviation — which TWO? | B+C | ✅ | B: EventBridge (specific API fast) + C: GuardDuty S3 Protection (behavioral anomaly). | Q474, Q568 | EventBridge + GuardDuty S3 Protection |
| 939 | D1 | RCP blocks external, 500 denied GetObjects, AA + GD enabled — which true? | C: Only AA fires | ✅ | C: AA flags policy (static). GD doesn't fire on blocked attempts. | Q534, Q594 | GuardDuty ≠ failed attempts + AA static |
| 940 | D2 | Forensic analysis: query CT Lake + Security Lake, custom viz, reusable template — approach? | B: SageMaker notebook | ✅ | B: Interactive analysis, custom viz, save as reusable runbook template. | — | SageMaker notebooks for IR |
| 941 | D1/D2 | Impact then Trojan findings, block hardcoded C2 IP + preserve + investigate 48hr — THREE? | B+C+D | ✅ | B: NF DROP on IP + C: EBS snapshot + D: Detective timeline. | Q526, Q571 | Network FW + EBS + Detective |
| 942 | D2 | Keys on GitHub, attacker created 2nd keys + console + EC2, SSO active — single containment? | D: TokenIssueTime | ❌ | C: Inline Deny * on IAM user. TokenIssueTime = temp sessions only. Deny * blocks ALL credential types. | Q862, Q867 | Deny * on user vs TokenIssueTime (user vs role) |


### Session 94 — 2026-06-16

**Domains:** D2 Incident Response + D1 Detection + D5 Data Protection + D3 Infrastructure + D6 Governance (Week 1 weekly drill + Session 93 re-test)
**Score:** 12 ✅ · 2 ⚠️ · 0 ❌ (86% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 943 | D2 | Test GD→EB→Step Functions pipeline without real incidents — approach? | B: CreateSampleFindings | ✅ | CreateSampleFindings API generates realistic findings through EventBridge. FIS = infra failures. | Q934 | CreateSampleFindings vs FIS |
| 944 | D2 | Prove RTO/RPO compliance to auditors, least overhead, no breakage — service? | B: Resilience Hub | ✅ | Resilience Hub assesses architecture vs targets, generates reports. FIS = test by breaking. | Q935 | Resilience Hub = assess, FIS = test, ARC = recover |
| 945 | D2 | AZ degraded, gray failure, shift traffic in seconds, no DNS/ASG changes — fastest? | B: ARC zonal shift | ✅ | ARC zonal shift operates at LB level, seconds, no DNS. | Q936 | ARC zonal shift |
| 946 | D2 | Keys on GitHub, attacker created 2nd keys + console + EC2, single broadest containment? | C: Inline Deny * on IAM user | ✅ | Deny * blocks all credential types. TokenIssueTime = temp sessions only. | Q942 | Deny * on user vs TokenIssueTime (user vs role) |
| 947 | D6 | Config org custom rule "Lambda not found" in 200 members, works in admin — fix? | B: Lambda resource-based policy config.amazonaws.com + SourceAccount | ✅ | Org custom rule invokes central Lambda cross-account. Resource policy needed. | Q908, Q921 | Config org custom rule cross-account invoke |
| 948 | D5 | CRR cross-account, replication role has kms:Encrypt on dest key, fails — missing? | C: Dest needs GenerateDataKey not Encrypt | ✅ | S3 never uses kms:Encrypt. Envelope encryption = GenerateDataKey. | Q883 | CRR dest = kms:GenerateDataKey (not Encrypt) |
| 949 | D1/D3 | EKS Runtime Monitoring enabled, crypto miner in pod, zero findings, audit log works — cause? | B: GuardDuty security agent not deployed | ✅ | Runtime Monitoring = only GD feature needing agent (DaemonSet). | Q797, Q821 | EKS Runtime Monitoring (agent required) |
| 950 | D5/D3 | Lambda private subnet, Kinesis+KMS endpoints exist, GetRecords times out, SM works — fix? (TWO) | A+B (missed D) | ⚠️ | A+D: Kinesis endpoint SG inbound 443 + Lambda SG outbound 443. Timeout = both sides of SG path. | Q918, Q925 | Kinesis + KMS VPC endpoints (timeout = network) |
| 951 | D1 | CT Lake org EDS mgmt-only, PutObject query returns zero, EDS created 2 weeks ago — TWO causes? | A only (missed D) | ⚠️ | A+D: PutObject is data event (EDS mgmt only) + Lake doesn't backfill historical events. | Q882, Q927 | CloudTrail Lake (data vs mgmt + no backfill) |
| 952 | D3 | IoT ThingName policy, attacker steals cert, installs on different device — result? | A: Succeeds — cert-bound not hardware | ✅ | ThingName bound to certificate, not physical device. Revoke cert to stop. | Q880, Q924 | IoT ThingName = cert-bound, not hardware |
| 953 | D5/D3 | CF + 3 ALBs, eu-west-1 ALB cert error, other ALBs work — cause? | B: ACM cert provisioned in wrong region | ✅ | ACM regional. ALB cert must be in ALB's region. CF cert = us-east-1. | Q931 | ACM regional requirements |
| 954 | D5/D4 | DynamoDB CMK, Lambda has Decrypt+GenerateDataKey, PutItem Access Denied on KMS — missing? | B: kms:CreateGrant | ✅ | DynamoDB delegates via grants (like EBS). Needs CreateGrant + DescribeKey. | Q899, Q922, Q930 | DynamoDB + CMK = CreateGrant |
| 955 | D5 | S3 Batch job us-east-1, manifest lists objects in 3 regions — result? | A: Fails — Batch is regional | ✅ | Job + manifest + target must be same region. | Q872, Q919, Q928 | S3 Batch Operations regional |
| 956 | D1/D3 | 200GB/hr WAF logs, full-text, sub-second, 90d, alerts, dashboards — architecture? | B: Firehose + OpenSearch + UltraWarm | ✅ | Full-text + sub-second + dashboards = OpenSearch. Firehose = managed ingestion. | Q854, Q875 | Kinesis + OpenSearch architecture |



### Session 95 — 2026-06-16

**Domains:** D2 Incident Response (D2 novel patterns blitz — automated forensics, chain of custody, Step Functions orchestration)
**Score:** 5 ✅ · 0 ⚠️ · 0 ❌ (100% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 957 | D2 | Forensics Orchestrator: isolate→SSM memory capture→snapshot, step 2 fails, SSM agent running — cause? | B: deny-all SG blocks SSM outbound | ✅ | Deny-all SG blocks SSM agent outbound HTTPS. Need VPC endpoints or reorder workflow. | Q937 | Forensics Orchestrator (deny-all blocks SSM) |
| 958 | D2 | Forensics: no cross-contamination + audit trail of evidence access + evidence immutability — architecture? | B: Dedicated forensics account + Object Lock + CloudTrail | ✅ | Separate account = isolation. Object Lock = immutability. CloudTrail = audit trail. | — | Forensics chain of custody architecture |
| 959 | D2 | Step Functions IR workflow, 4 severity branches — how does it decide which branch? | B: Choice state evaluates severity from EventBridge input | ✅ | EventBridge passes full finding JSON. Choice state branches on $.detail.severity. | — | Step Functions Choice state for IR routing |
| 960 | D2 | Credential compromise, determine other resources + roles + 72hr timeline + visualizations across 15 accounts? | C: Detective | ✅ | Detective = investigate + visualize + timeline + blast radius. | — | Detective for IR investigation |
| 961 | D2 | Automated containment <5min, zero human, private subnet, multi-step — architecture? | B: EventBridge → Step Functions (Choice + parallel + VPC endpoints for SSM) | ✅ | Step Functions orchestrates parallel containment. VPC endpoints for private subnet SSM. | — | Automated IR architecture (Step Functions) |



### Session 96 — 2026-06-16

**Domains:** D1 Detection + D5 Data Protection + D3 Infrastructure + D2 Incident Response (cross-domain uplift — never-seen topics + verb traps)
**Score:** 8 ✅ · 1 ⚠️ · 1 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 962 | D1 | Detect PutBucketPolicy with Principal:* within 2 min, org trail exists — approach? | C: EventBridge in management account | ✅ | Specific API call + fast + org trail = EventBridge. | Q474, Q570 | EventBridge for API call detection |
| 963 | D1 | Unusual country + large volumes + 3AM + no code/infra — service? | C: GuardDuty S3 Protection | ✅ | Behavioral anomaly + zero code = GuardDuty S3 Protection. | Q568, Q581 | Detect vs prevent (GuardDuty vs policy) |
| 964 | D1 | Bucket policy grants external, no access yet, AA + GD enabled — which fires? | C: Only Access Analyzer | ✅ | AA = static policy analysis. GD = needs actual access. | Q518, Q573 | Access Analyzer static + GuardDuty ≠ failed attempts |
| 965 | D5/D3 | Lambda private subnet, S3 SSE-KMS works, direct GenerateDataKeyWithoutPlaintext times out — fix? (TWO) | A only (missed C) | ⚠️ | A+C: Add KMS Interface endpoint + configure endpoint SG inbound 443. Timeout = both sides of SG. | Q918, Q950 | KMS endpoint + SG (direct calls only) |
| 966 | D5 | CRR custom encryption context "Engineering", dest key policy requires "Finance" — result? | B: Fails — context preserved, mismatch | ✅ | CRR preserves source encryption context. Dest key policy evaluates it → mismatch → fail. | Q923, Q913 | CRR custom encryption context preserved |
| 967 | D3 | B2B API, partners authenticate with client certs, private CA PEM in S3 — mTLS config? | B: Upload CA to ACM | ❌ | C: Custom domain + enable mTLS + S3 URI + object version of PEM truststore. mTLS = custom domain + S3 truststore. | — | API Gateway mTLS = custom domain + S3 truststore |
| 968 | D1 | Macie flag PROJ-[A-Z]{4}-\d{4} only when "Classified" within 50 chars — how? | A: Custom data identifier + regex + keyword + max distance | ✅ | Macie custom data identifier: regex + keywords + maximum match distance. | — | Macie custom data identifiers (regex + keywords + proximity) |
| 969 | D3 | Patient SSN encrypted at CF edge before origin, WAF can't see raw — approach? | B: RSA public key + FLE profile + FLE config + cache behavior | ✅ | CloudFront FLE: upload RSA public key, map field in profile, attach to behavior. | — | CloudFront Field-Level Encryption |
| 970 | D2 | Trojan C2Activity, API must stay up + block C2 + preserve evidence — which TWO? | B+C: NF DROP on C2 IP + no-reboot AMI + EBS snapshot | ✅ | NF = surgical block. No-reboot AMI + snapshot = complete forensics. | Q526, Q933 | Surgical containment (NF + forensics) |
| 971 | D1/D5 | Prevent ScheduleKeyDeletion + detect PutBucketPolicy 90s + alert anomalous downloads — THREE services? | A: SCP + EventBridge + GuardDuty S3 Protection | ✅ | Prevent = SCP. Detect API = EventBridge. Detect behavior = GuardDuty. | Q688, Q701 | Full prevent/detect/alert architecture |
| 972 | D5 | Glacier Vault Lock: permanently irreversible after 24hr confirm, even AWS can't modify — mechanism? | B: Glacier Vault Lock | ✅ | "24hr confirm + permanently irreversible" = Vault Lock. Object Lock = per-object retention with expiry. | Q800, Q822, Q828 | Glacier Vault Lock vs Object Lock |
| 973 | D5/D3 | Lambda private subnet: DynamoDB + direct kms:Decrypt + S3 SSE-KMS — minimum endpoints? | B: 3 (Gateway S3 + Gateway DDB + Interface KMS) | ✅ | S3 SSE-KMS = server-side (no KMS endpoint). Direct kms:Decrypt = needs KMS Interface endpoint. | Q685, Q699 | VPC endpoints (direct KMS + DynamoDB) |
| 974 | D4/D5 | Cross-account S3+KMS works, then key admin removes Account B from key policy — what fails? | B: Fails at s3:GetObject | ❌ | C: Fails at kms:Decrypt — key policy must name external account. Error surfaces on GetObject but root cause is KMS. | Q541, Q669, Q850 | Cross-account KMS key policy must name external account |
| 975 | D3 | Private API: only from vpce-111111 + only sg-222222 — which TWO? | A+B: Resource Policy + endpoint SG inbound | ✅ | Resource Policy = API-level gate. Endpoint SG = network-level gate. Both needed. | — | Private API Resource Policy + endpoint SG |
| 976 | D1 | CT Lake query GetObject returns zero, DeleteBucket works — cause? | B: GetObject is data event, EDS mgmt-only | ✅ | Data events need explicit EDS configuration. Management events work by default. | Q882, Q927, Q951 | CloudTrail Lake (data vs mgmt + no backfill) |
| 977 | D2 | Forensics Orchestrator: VPC endpoints deployed, deny-all SG, SSM still fails — cause? | A: Deny-all SG blocks outbound to endpoint ENIs | ✅ | Deny-all = no outbound at all. Instance can't reach VPC endpoint ENIs. | Q937, Q957 | Deny-all SG blocks ALL outbound (including to endpoints) |
| 978 | D3 | API GW: web=Cognito JWT, legacy=HMAC header + IP restrict BEFORE authorizer — config? | B: Cognito + Lambda REQUEST + Resource Policy | ✅ | Resource Policy first (saves Lambda cost). REQUEST type for headers+IP. | Q967 | API Gateway Resource Policy + REQUEST authorizer |
| 979 | D5 | RSA KMS key for encryption AND signing — why not? | B: One key = one purpose at creation (sign OR encrypt) | ✅ | KMS locks key usage at creation. RSA can do either but must choose one. | Q812, Q824 | KMS one key = one purpose |
| 980 | D5 | Asymmetric sign, partners verify offline air-gapped — how? | B: Export public key, verify locally OpenSSL | ✅ | Sign=private (KMS). Verify=public (exportable, offline). | Q812, Q824, Q834 | Sign=private, verify=public (offline) |
| 981 | D1/D3 | DGA domains (unpredictable), block VPC-wide — approach? | C: DNS Firewall allow-list (block all except known-good) | ✅ | DGA = can't enumerate. Flip to allow-list. DNS layer since attacker needs DNS. | Q690, Q756 | DGA = allow-list DNS Firewall |
| 982 | D4/D5 | 5-layer: key policy grants B + SCP ViaService + session=GetObject + RCP same-org — SSE-KMS cross-account read? | C: Succeeds — all gates pass | ✅ | Server-side KMS, ViaService satisfied, session doesn't gate, RCP same-org passes. | Q591, Q531 | Full 5-layer cross-account evaluation |
| 983 | D1/D4 | RCP blocks external, 500 denied GetObjects 3 days, AA + GD enabled — which fires? | B: Only Access Analyzer | ✅ | AA = static (fires on policy). GD = needs successful access. Blocked = no GD finding. | Q534, Q594 | Access Analyzer static + GuardDuty ≠ failed attempts |
| 984 | D5/D6 | Config auto-remediation S3 logging AccessDenied, has PutBucketLogging+PutObject — missing? | A: s3:GetBucketAcl | ✅ | S3 server access logging uses ACLs (legacy). Needs GetBucketAcl for validation. | Q864, Q868, Q903 | S3 server access logging = ACLs |
| 985 | D3/D1 | Detect threat IP + block org-wide + auto-update — which THREE? | B: GuardDuty + NF via RAM+FM + EventBridge→Lambda | ✅ | GD detects. NF blocks IPs. EventBridge+Lambda auto-updates NF rules from findings. | Q532, Q543 | Detection + response architecture |
| 986 | D2 | InsideAWS credential exfil, both instances production — containment? | B: Deny-all SG on attacker's instance | ✅ | InsideAWS = SG isolation. TokenIssueTime would break both. | Q761, Q785 | InsideAWS = SG isolation |
| 987 | D5 | 50GB multipart SSE-KMS fails at CompleteMultipartUpload, has GenerateDataKey — missing? | B: kms:Decrypt | ✅ | Multipart reassembly decrypts each part's data key. Single-part only needs GenerateDataKey. | Q744, Q765 | S3 multipart + KMS (reassembly = Decrypt) |
| 988 | D3 | TOKEN authorizer modified to check X-Signature + IP — why fails? | C: Timeout | ❌ | B: TOKEN receives ONLY the token string. Can't access other headers or IP. Need REQUEST type. | Q967 | API Gateway TOKEN vs REQUEST authorizer |
| 989 | D4/D5 | Cross-account KMS, B removed from key policy, Lambda calls GetObject — error type? | A: KMS.AccessDeniedException | ⚠️ | B: S3 wraps KMS failure as S3 AccessDenied — caller called S3, not KMS directly. | Q541, Q974 | S3 wraps KMS errors (error surface vs root cause) |
| 990 | D5/D6 | EBS encryption by default alone — why insufficient for org-wide prevention? | B: Per-account+region, new accounts miss it, users can override | ✅ | Full prevention = EBS default + SCP together. | Q902 | EBS encryption by default + SCP = full prevention |
| 991 | D1 | CW metric filter on StopLogging doesn't fire, EventBridge does — why? | B: StopLogging kills own CW Logs delivery | ✅ | EventBridge receives from CT management stream directly, bypasses CW Logs. | Q860, Q866 | StopLogging kills own CW Logs delivery |
| 992 | D2 | Prove RTO/RPO to auditors without breaking anything — service? | B: Resilience Hub | ✅ | Assess architecture vs targets, generate report. No disruption. | Q935, Q944 | Resilience Hub = assess, FIS = test, ARC = recover |
| 993 | D2 | Validate failover works in production with safety guardrails (auto-stop at 1% error) — service? | B: FIS with stop conditions | ✅ | FIS = chaos with CloudWatch alarm guardrails. | Q934, Q943 | FIS = test by breaking safely |
| 994 | D2 | Gray failure, shift traffic from AZ in seconds, LB-level, temporary, no DNS — action? | C: ARC zonal shift | ✅ | Seconds, LB-level, set duration, auto-reverts. | Q936, Q945 | ARC zonal shift |
| 995 | D2 | Test full IR pipeline (GD→EB→SF) with realistic findings through EventBridge — approach? | C: CreateSampleFindings | ✅ | Generates real-structure findings through normal EventBridge flow. | Q934, Q943 | CreateSampleFindings = test IR pipeline |
| 996 | D2 | Investigate across 15 accounts + custom viz + reusable templates for junior analysts — tool? | A: Detective | ❌ | C: SageMaker notebooks. Detective = pre-built investigation. SageMaker = custom code + reusable templates + arbitrary queries. | — | SageMaker notebooks vs Detective (custom vs built-in) |
| 997 | D1 | GuardDuty member tries CreateIPSet — result? | B: Only admin can manage IP lists | ✅ | Members can't archive findings or manage Trusted/Threat IP lists. | Q711, Q723 | GuardDuty master/member permissions |
| 998 | D1 | EventBridge ConsoleLogin rule never fires, Event History shows logins, Write-only trail — cause? | B: ConsoleLogin is Read event, Write-only doesn't deliver | ✅ | EventBridge only receives events the trail delivers. Event History shows all. | Q710, Q729 | CloudTrail management events Read/Write |
| 999 | D1 | CW metric filter AuthorizeSecurityGroupIngress never fires, alarm >= 1, pattern correct — cause? | A: Metric value set to 0 instead of 1 | ✅ | Value=0 means sum never reaches threshold. Must be 1. | Q724 | CW metric filter value |
| 1000 | D1 | CW Logs agent was working, stops, process running, IAM unchanged — check first? | B: /var/log/awslogs.log (runtime) | ✅ | "Was working, stopped" = runtime. Setup log = install only. | Q708 | CW Logs agent troubleshooting |
| 1001 | D1 | 100GB/hr real-time full-text search + sub-second + dashboards + 30d — architecture? | C: Firehose + OpenSearch | ✅ | Full-text + sub-second + volume = OpenSearch. Firehose = ingestion. | Q854, Q875, Q956 | Kinesis + OpenSearch architecture |
| 1002 | D1 | "Which S3 buckets accessible by externals based on policy?" no access yet — service? | B: Access Analyzer external | ✅ | Static policy analysis. Doesn't need actual access. | Q518, Q573, Q964 | Access Analyzer static (external mode) |
| 1003 | D1 | Unused roles 90d + generate replacement policy scoped to actual usage — service? | B: Credential report | ❌ | A: Access Analyzer unused access + policy generation. Credential report = role-level only, no per-action, no policy gen. | Q374, Q404 | Access Analyzer unused + policy generation |
| 1004 | D1 | Insights fires 10x RunInstances spike — what does Insights detect vs GuardDuty? | A: Volume anomaly (Insights) vs C2/unusual creds (GD) | ⚠️ | D: Both A and C true. Insights = volume. GD = behavior + threat intel. Complementary. | — | CloudTrail Insights vs GuardDuty (complementary) |
| 1005 | D1 | Top 10 source IPs to private subnet last hour, Flow Logs in CW — tool? | B: CW Logs Insights | ✅ | Data already in CW + aggregation = Logs Insights. No extra setup. | Q236, Q306, Q416 | CW Logs Insights for aggregation |
| 1006 | D1 | Security Lake: CloudTrail+Flow+GD+WAF+Splunk — which THREE true? | A+B+C | ✅ | Your S3 Parquet + OCSF + subscriber model. Not real-time. Doesn't replace GD. | Q334, Q528 | Security Lake (OCSF + your S3 + subscriber) |
| 1007 | D3 | Bedrock: force guardrail on every InvokeModel, no exceptions — how? | A: Console toggle | ❌ | B: IAM condition `bedrock:GuardrailIdentifier` on InvokeModel permission. No console toggle exists. | — | Bedrock IAM guardrail enforcement (condition key) |
| 1008 | D3 | Filter PII from self-hosted LLM on EC2, not Bedrock — approach? | B: bedrock:ApplyGuardrail | ✅ | ApplyGuardrail = standalone API. Filter any text without InvokeModel. | — | ApplyGuardrail standalone (non-AWS LLMs) |
| 1009 | D5 | FSx Lustre linked to SSE-KMS S3, creation fails Access Denied — missing? | A: Key policy must grant fsx.amazonaws.com | ✅ | Same pattern: service principal needs Encrypt+Decrypt+GenerateDataKey+DescribeKey. | — | FSx Lustre + SSE-KMS S3 key policy |
| 1010 | D3 | Q Business user sees HR doc they shouldn't — cause? | B: ACLs disabled | ❌ | C: ACL identity mapping failed (sync between connector and Identity Center broke). ACLs can't be disabled once enabled. | — | Q Business ACL identity mapping failure |


### Session 97 — 2026-06-17

**Domains:** D3 Infrastructure + D5 Data Protection + D1 Detection + D6 Governance (Week 2-5 never-seen blitz — API GW mTLS, authorizers, FLE, Inspector SBOM, Macie, S3 Access Grants, VPC Lattice, State Manager, cfn-guard, DLM, DataSync, EMR, WAF Bot Control, CodeGuru)
**Score:** 28 ✅ · 0 ⚠️ · 9 ❌ (76% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1012 | D3 | API Gateway mTLS, private Root CA, most secure + operationally efficient? | A: Upload to ACM | ❌ | C: S3 truststore (PEM + version) + custom domain + enable mTLS + Route 53. mTLS = custom domain + S3 truststore, not ACM. | — | API Gateway mTLS = custom domain + S3 truststore |
| 1013 | D3 | Web=Cognito, Legacy=HMAC+IP, reject unknown IPs at boundary before authorizer — least overhead? | D: WAF | ❌ | C: Cognito + Lambda REQUEST + Resource Policy (IP deny). Resource Policy = boundary (evaluated first). WAF can't validate HMAC. | — | Resource Policy = boundary rejection (before authorizer) |
| 1014 | D3/D5 | Encrypt claim_id POST field at CloudFront edge with asymmetric crypto — least config? | B: RSA key + FLE Profile + FLE Config + cache behavior | ✅ | Native FLE: upload RSA public key → profile (field→key) → config (content-type→profile) → behavior. | — | CloudFront FLE setup chain |
| 1015 | D3 | Inspector SBOM CycloneDX to central S3, least overhead — Select TWO? | A+C | ✅ | Inspector native SBOM export (CycloneDX) + S3 bucket policy for inspector2.amazonaws.com. | — | Inspector SBOM = native export + bucket policy |
| 1016 | D1 | Macie detect PROJ-[4 letters]-[4 digits] only when keyword within 40 chars? | A: Custom data identifier + regex + keywords + proximity | ✅ | Macie custom data identifier = regex + keywords + max proximity distance. | — | Macie custom data identifiers (regex + keywords + proximity) |
| 1017 | D5/D4 | Map AD groups to S3 prefixes via Identity Center, least admin complexity? | B: S3 Access Grants + Identity Center + grants per group | ✅ | Access Grants = declarative identity-to-prefix mapping. No JSON policies. | — | S3 Access Grants (identity + prefix + permission level) |
| 1018 | D3/D1 | Block X-Product-Key regex at API GW edge + Macie scan S3 with keyword proximity — least overhead? | B: Lambda REQUEST authorizer + Macie custom identifier | ✅ | Resource Policy can't inspect header values. Lambda REQUEST can. Macie handles S3 scanning natively. | — | Resource Policy = network only, Lambda = header inspection |
| 1019 | D3 | Private API only from vpce-444444, only sg-555555 clients — Select TWO? | A+B: Resource Policy + Endpoint SG | ✅ | Resource Policy (vpce restriction) + Endpoint SG (client SG inbound 443). Two layers. | — | Private API = Resource Policy + Endpoint SG |
| 1020 | D5/D3 | FLE encrypts at edge, ECS stores in S3 SSE-KMS, CMK requires encryption context — how? | B: Key policy condition + app passes context | ✅ | kms:EncryptionContext:key condition in key policy. App code passes context on PutObject. FLE ≠ KMS. | — | Encryption context = key policy condition + app passes it |
| 1021 | D5 | Inspector SBOM WORM 3yr, root can't delete — least overhead? | A: Object Lock Compliance 3yr | ✅ | Compliance mode = nobody deletes (including root). Fixed retention. | — | Object Lock Compliance (root can't override) |
| 1022 | D3 | VPC Lattice: 15 microservices across 5 accounts, service-to-service auth without certs — least overhead? | B: Lattice service network + RAM + IAM auth (SigV4) | ✅ | VPC Lattice = service-to-service, IAM auth, share via RAM. No certs. | — | VPC Lattice (cross-account service-to-service + IAM) |
| 1023 | D1/D3 | Ensure CW agent always installed, auto-fix drift every 30 min — least admin effort? | B: SSM State Manager association + 30min schedule | ✅ | State Manager = desired-state engine, auto-re-applies on schedule. | — | SSM State Manager (desired-state + schedule) |
| 1024 | D6 | Validate CF template has encryption + IMDSv2 before any resource created — least custom code? | B: cfn-guard rules in CI/CD pipeline | ✅ | cfn-guard = policy-as-code for templates, shift-left validation. | — | CloudFormation Guard (template validation in pipeline) |
| 1025 | D3/D5 | Private API timeout, endpoint SG allows all inbound 443, KMS works fine — cause? | A: Lambda SG missing outbound | ❌ | B: Resource Policy doesn't allow Lambda's VPC endpoint. Private API timeout can mean Resource Policy rejection. | — | Private API timeout = Resource Policy rejection (not always network) |
| 1026 | D5/D4 | Access Grants + SSE-KMS with encryption context, users get Access Denied — missing? | D: Key policy grant s3:GetObject | ❌ | B: Access Grants IAM role needs kms:Decrypt with encryption context condition. Access Grants handles S3 perms, not KMS. | — | Access Grants + SSE-KMS needs explicit kms:Decrypt on role |
| 1027 | D3/D6 | Three IMDSv2 layers: template validation + drift fix + API block — match services? | A: cfn-guard + State Manager + SCP | ✅ | Template=cfn-guard, drift=State Manager, API=SCP. Three moments. | — | Layered enforcement (cfn-guard + State Manager + SCP) |
| 1028 | D5 | Automated daily EBS snapshots, 30d retention, cross-region copy, auto-delete — least overhead? | C: DLM policy + tag + schedule + cross-region | ✅ | DLM = EBS snapshot automation (schedule + retain + cross-region + auto-delete). | — | Data Lifecycle Manager (EBS snapshots) |
| 1029 | D5 | 50TB weekly NFS→S3, encrypted in transit, filter *.parquet, throttle bandwidth — approach? | B: DataSync agent + TLS + include filter + bandwidth limit | ✅ | DataSync = recurring on-prem→AWS. TLS + filtering + throttling built in. | — | DataSync (encrypted transfer + filtering + throttling) |
| 1030 | D5 | EMR inter-node encryption, no code changes — config? | B: EMR security config → in-transit + PEM certs | ❌ | A: EMR security configuration → enable in-transit encryption + PEM certificates (Private CA). | — | EMR in-transit = security config + PEM certs |
| 1031 | D6 | Identify architectural gaps vs AWS best practices + improvement plan + track progress — service? | B: Audit Manager | ❌ | C: Well-Architected Tool (Security Pillar). Architectural review + improvement plan + milestones. | — | Well-Architected Tool = architecture review + improvement plan |
| 1032 | D3/D5 | Compromised IoT device cert, block on IoT Core + API Gateway mTLS — Select TWO? | C+B | ❌ | B+E: IoT Core = mark INACTIVE in registry. API GW mTLS = add CRL to S3 truststore. | — | IoT revocation = registry. API GW mTLS revocation = CRL in truststore |
| 1033 | D3 | Re-test: EMR inter-node encryption — what to configure? | B: Security config + in-transit + PEM | ✅ | Locked. | Q1030 | EMR in-transit = security config + PEM certs |
| 1034 | D6 | Re-test: Architectural gaps + improvement plan + track progress — service? | C: Well-Architected Tool | ✅ | Locked. | Q1031 | Well-Architected Tool |
| 1035 | D3 | Re-test: Block compromised cert on IoT Core specifically? | A: Revoke in Private CA | ❌ | B: Mark INACTIVE in IoT Core registry. IoT Core doesn't use CRL. | Q1032 | IoT Core = registry-based revocation (instant) |
| 1036 | D3 | Re-test: Block compromised cert on API Gateway mTLS? | B: Add CRL to S3 truststore | ✅ | Locked. | Q1032 | API GW mTLS = CRL in S3 truststore |
| 1037 | D3 | Re-test: Private API timeout, KMS works, endpoint SG open — cause? | B: Resource Policy doesn't allow vpce | ✅ | Locked. | Q1025 | Private API timeout = Resource Policy rejection |
| 1038 | D3 | WAF Bot Control: bots rotate IPs, don't execute JS — feature? | B: Bot Control + challenge action (JS challenge) | ✅ | Bots can't execute JS → fail challenge → blocked. IP-independent. | — | WAF Bot Control (challenge action for JS-less bots) |
| 1039 | D3 | Detect hardcoded keys + SQLi + insecure SDK in source code pre-deploy — service? | B: CodeGuru Security (SAST) | ✅ | SAST = source code scanning. Inspector = CVEs in dependencies. | — | CodeGuru Security = SAST (pre-deploy code scanning) |
| 1040 | D5/D4 | Access Grants + SSE-KMS with encryption context required in key policy, role has Decrypt without condition — GetObject fails. Cause? | A: mTLS truststore issue | ❌ | D: Key policy condition enforces context at KMS layer regardless of role's identity policy. | Q1026 | Key policy conditions enforced regardless of caller's identity policy |
| 1041 | D3 | mTLS working, one partner cert compromised, block only that cert — how? | B: Add CRL to S3 truststore | ✅ | CRL in truststore = per-cert revocation. Remove CA = blocks ALL partners. | Q1012 | API GW mTLS CRL revocation |
| 1042 | D2 | Custom Python + viz + reusable template for junior analysts — tool? | C: SageMaker notebooks | ✅ | Custom code + arbitrary queries + reusable = SageMaker. Detective = pre-built. | Q996 | SageMaker notebooks vs Detective |
| 1043 | D3 | 200 IoT certs compromised, block on IoT Core within seconds — approach? | B: Batch UpdateCertificate to INACTIVE | ✅ | IoT Core = registry check at TLS handshake. Instant. No CRL. | Q1035 | IoT Core = registry-based revocation (instant) |
| 1044 | D6 | CISO needs architectural gaps + improvement plan + milestones. SH and AM don't satisfy — why? | B: Neither reviews architecture or generates improvement plans | ✅ | Well-Architected Tool = design-level review + plan + milestones. | Q1031 | Well-Architected Tool = architecture review + improvement plan |
| 1045 | D3 | Private API: Lambda A works, Lambda B timeout, same VPC/subnet — cause? | B: Endpoint SG only allows sg-aaa inbound, not sg-bbb | ✅ | Timeout = network. Same Resource Policy = permissions fine. Difference = SG. | Q1025 | Private API timeout = SG on endpoint |
| 1046 | D5/D4 | Access Grants + SSE-KMS, role has Decrypt, ViaService=s3.us-east-1, bucket in eu-west-1 — fails. Cause? | B: ViaService region mismatch (eu-west-1 vs us-east-1) | ✅ | ViaService is region-specific. Must match bucket's region. | Q1026 | kms:ViaService is region-specific |
| 1047 | D3 | VPC Lattice auth policy: Service A can call B, deny all others — where enforce? | B: Auth policy on Service B (resource-based, allow only A's role) | ✅ | Lattice auth policies = resource-based (like bucket policies). Attached to service. | — | VPC Lattice auth policy (resource-based on service) |
| 1048 | D1/D3 | State Manager: CIS hardening on every boot + drift fix between boots — config? | D: rate(7 days) | ❌ | B: OnBoot trigger + rate(1 hour) schedule. State Manager supports both event + time triggers on one association. | — | State Manager OnBoot + schedule (dual triggers) |
| 1049 | D5 | DLM: developer manually deletes 3-day-old snapshot — what happens? | B: Gone permanently, DLM doesn't monitor for deletions | ✅ | DLM = scheduler only. Creates + deletes on schedule. No replacement of manually deleted. | — | DLM = scheduler only (no monitoring) |
| 1050 | D5 | DataSync: 50 new files + 150 unchanged — behavior? | B: Incremental, only transfers new/modified | ✅ | DataSync compares metadata (size, mtime). Same as rsync. | — | DataSync incremental by default |
| 1051 | D3 | Inspector SBOM export scheduling — how? | A: Built-in scheduling | ❌ | B: EventBridge scheduled rule → Lambda → CreateSbomExport API. No built-in scheduler. | — | Inspector SBOM = on-demand API (EventBridge + Lambda to schedule) |
| 1052 | D3/D5 | FLE: where does private key live for origin decryption? | C: On origin server (app decrypts locally with RSA private key) | ✅ | FLE = public key at edge, private key on YOUR origin. AWS never sees private key. | — | FLE private key = origin server (not AWS) |
| 1053 | D3 | WAF Bot Control: mobile app (no JS) fails challenge — fix? | B: Scope-down statement excluding app's custom header | ✅ | Scope-down = "only apply rule group to matching requests." Exempt known-good. | — | WAF scope-down statement (exempt known traffic) |
| 1054 | D3 | CodeGuru flags hardcoded key, dev says "test only" — remediation? | C: Environment variable | ❌ | B: Secrets Manager. Env vars = plaintext in console, no rotation. SM = encrypted + rotatable + auditable. | — | Hardcoded credential → always Secrets Manager |
| 1055 | D3 | mTLS 403 on new partner, same CA, other partners work — cause? | D: Wrong endpoint | ❌ (then A) | A: Certificate expired. Same CA works for others = truststore fine. 403 at handshake = cert itself invalid. | Q1012 | mTLS 403 = cert expired (if same CA works for others) |
| 1056 | D3 | Lattice: Service C added to network, AccessDeniedException calling B — missing? | B: Auth policy on B must allow C's role | ✅ | Network membership = reachability. Auth policy = authorization. Separate. | Q1022 | VPC Lattice auth policy per-service |
| 1057 | D5 | DLM 7-day + Object Lock 3yr + 8-day-old objects missing — cause? | B: DLM retention correct + S3 lifecycle policy (separate issue) | ✅ | DLM auto-deletes by design. Object Lock prevents delete but check lifecycle. | — | DLM retention vs S3 lifecycle (separate) |
| 1058 | D3/D6 | Console deploy EC2 IMDSv1, five enforcement layers — which catches? | D: Only SCP (blocks RunInstances) | ✅ | SCP blocks API regardless of deployment method. Instance never created = other layers never fire. | — | SCP = catches ALL deployment paths |
| 1011 | D6/D3 | Block specific Bedrock model org-wide, allow others — enforcement? | B: SCP deny InvokeModel on model ARN | ✅ | SCP + model ARN = org-wide block. Simplified access doesn't override IAM/SCP. | — | SCP to block Bedrock model org-wide |
### Session 98 — 2026-06-18

**Domains:** D3 Infrastructure + D5 Data Protection + D1 Detection + D4 IAM + D6 Governance (Week 2 NEVER-SEEN validation — mTLS, FLE, SBOM, Macie, Access Grants, Session 97 re-tests, cross-domain killers)
**Score:** 17 ✅ · 0 ⚠️ · 8 ❌ (68% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1056 | D3 | API GW mTLS: B2B private Root CA — config? | C: S3 truststore + custom domain + mTLS | ✅ | S3 PEM + versioning + custom domain + Route 53 | Q1012 | API Gateway mTLS = custom domain + S3 truststore |
| 1057 | D3 | API GW: Cognito web + HMAC legacy + IP block at boundary — config? | C: Cognito + REQUEST authorizer + Resource Policy IP deny | ✅ | Resource Policy = boundary (before authorizer). REQUEST = headers+IP. | Q1013 | Resource Policy = boundary rejection (before authorizer) |
| 1058 | D3/D5 | CloudFront FLE: encrypt claim_id at edge with asymmetric crypto — config? | B: RSA key + Profile + Config + cache behavior | ✅ | Native FLE chain: key→profile→config→behavior | — | CloudFront FLE setup chain |
| 1059 | D3 | Inspector SBOM: centralized CycloneDX to S3 — which TWO? | B (SSM+Lambda) | ❌ | A+C: Inspector native SBOM export + bucket policy for inspector2.amazonaws.com | Q1051 | Inspector SBOM = native export + bucket policy |
| 1060 | D1 | Macie: custom regex + keywords + proximity — config? | A: Custom data identifier + regex + keywords + proximity | ✅ | Macie custom data identifier = regex + keywords + max proximity distance | — | Macie custom data identifiers |
| 1061 | D5/D4 | S3 Access Grants: map AD groups to prefixes, least complexity? | B: Access Grants + Identity Center + grants per group | ✅ | Declarative identity-to-prefix mapping, no JSON policies | — | S3 Access Grants (identity + prefix + permission level) |
| 1062 | D3/D1 | API GW + Macie: block header regex + scan S3 with keyword proximity — arch? | B: REQUEST authorizer + Macie custom identifier | ✅ | Resource Policy can't inspect header values. Lambda REQUEST can. | Q1018 | Resource Policy = network only, Lambda = header inspection |
| 1063 | D3 | Private API: vpce + client SG restriction — which TWO? | A+B: Resource Policy + endpoint SG inbound | ✅ | Resource Policy (vpce gate) + endpoint SG (client gate) | Q1019 | Private API = Resource Policy + Endpoint SG |
| 1064 | D5/D3 | FLE + KMS encryption context: how to enforce context on S3 CMK? | B: Key policy condition + app passes context | ✅ | FLE ≠ KMS. Context enforced at KMS layer, passed by app code. | Q1020 | Encryption context = key policy condition + app passes it |
| 1065 | D5 | Inspector SBOM + Object Lock: WORM 3yr, root can't delete? | A: Object Lock Compliance 3yr | ✅ | Compliance mode = nobody deletes (including root). | — | Object Lock Compliance (root can't override) |
| 1066 | D3 | mTLS: 15 partners work, 1 new gets 403, same CA — cause? | C: Partner cert expired | ✅ | Same CA works for others = truststore fine. 403 at handshake = cert invalid. | Q1055 | mTLS 403 = cert expired (if same CA works for others) |
| 1067 | D3 | TOKEN authorizer + need custom header + IP — why fails? | A: TOKEN only gets token string, switch to REQUEST | ✅ | TOKEN = only token value. REQUEST = headers + query + IP. | Q988 | API Gateway TOKEN vs REQUEST authorizer |
| 1068 | D3 | Private API timeout, all SGs open, IAM correct — cause? | B: Resource Policy missing vpce Allow | ✅ | Private API timeout = Resource Policy rejection | Q1025 | Private API timeout = Resource Policy rejection |
| 1069 | D5/D4 | Access Grants + SSE-KMS + encryption context condition — Access Denied cause? | A: Access Grants IAM role missing kms:Decrypt with context | ✅ | Access Grants handles S3 perms, not KMS. Role needs explicit kms:Decrypt. | Q1026, Q1040 | Access Grants + SSE-KMS needs explicit kms:Decrypt on role |
| 1070 | D3 | IoT revocation + API GW mTLS revocation — which TWO? | B+C (IoT CRL + API GW CRL) | ❌ | A+C: IoT = registry INACTIVE (instant). API GW = CRL in S3 truststore. | Q1032, Q1035 | IoT revocation = registry. API GW mTLS revocation = CRL in truststore |
| 1071 | D1/D3 | State Manager: CIS on boot + every 4hr drift fix — config? | A: Two separate associations | ❌ | B: ONE association with BOTH OnBoot trigger + rate(4 hours) schedule | Q1048 | State Manager OnBoot + schedule (dual triggers) |
| 1072 | D3 | Inspector SBOM scheduling: weekly auto-export — approach? | B: EventBridge + Lambda + CreateSbomExport | ✅ | Inspector SBOM = on-demand API (no built-in scheduler) | Q1051 | Inspector SBOM = on-demand API (EventBridge + Lambda to schedule) |
| 1073 | D5 | EMR inter-node encryption — config? | C: Nitro on C6i | ❌ | A: EMR security config + in-transit + PEM certs (Private CA) | Q1030 | EMR in-transit = security config + PEM certs |
| 1074 | D4/D6 | RCP + Lambda caller: partner calls API GW, Lambda writes S3 — why succeeds? | B: API GW is AWS service principal | ❌ | A: Lambda is the S3 caller, it's in-org, PrincipalOrgID matches | — | RCP evaluates S3 CALLER (Lambda), not original HTTP client |
| 1075 | D5 | CRR + custom encryption context: partner objects fail replication — cause? | B: mTLS cert expired in DR | ❌ | A: CRR preserves source context, dest key policy condition mismatch | Q923 | CRR preserves source custom encryption context |
| 1076 | D4/D5 | ViaService + session policy + private API — which ops succeed? | C: Both succeed | ✅ | ViaService satisfied (server-side), session doesn't gate server-side KMS | Q591 | Session policy + server-side KMS |
| 1077 | D3 | Bedrock: WAF + guardrail enforcement + PII filter — which THREE? | A+B+C | ✅ | WAF (HTTP), IAM condition (guardrail), Bedrock Guardrails (PII output) | Q1007 | Bedrock IAM guardrail enforcement (condition key) |
| 1078 | D4/D5 | Access Grants + cross-account KMS + RCP — Access Denied fix? | B: CMK key policy must name Account B | ✅ | Cross-account KMS: key policy must name external account | Q541 | Cross-account KMS key policy must name external account |
| 1079 | D3/D2 | Lambda C2 + private API timeout + forensics — which THREE? | A+C+E (picked EBS snapshot) | ❌ | A+C+F: NF DROP + Resource Policy check + endpoint SG inbound 443. Lambda has no EBS. | — | Lambda = no EBS/AMI forensics (ephemeral) |
| 1080 | D3/D5 | Data perimeter + mTLS + Lambda Access Denied — check FIRST? | B: SCP ResourceAccount | ❌ | C: S3 Gateway endpoint policy (hidden allowlist gate) | Q535 | Gateway endpoint policy as additional gate |

---
**Extended Rounds (Q26-Q60):**

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1081 | D3/D5 | Gateway endpoint policy + ViaService: PutObject not in endpoint policy — result? | C: Access Denied | ✅ | Endpoint policy is allowlist — PutObject not listed = denied | Q535 | Gateway endpoint policy as additional gate |
| 1082 | D4/D6 | RCP scope: SLR replicates to external partner bucket — RCP blocks? | C: RCP doesn't apply — partner's bucket not your resource | ✅ | RCP protects YOUR resources only. Outbound = SCP's job. | Q683, Q698 | RCP scope (your resources only, not outbound) |
| 1083 | D4/D6 | Declarative policy vs SCP: new API assigns public IPv6 — what prevents? | B: Declarative policy enforces state regardless of API | ✅ | Declarative = state enforcement. SCP = must enumerate APIs. | — | Declarative policies vs SCP |
| 1084 | D1 | CloudTrail Lake vs Security Lake — match requirements to services? | B: CT Lake for SQL/API queries, Security Lake for OCSF/your S3 | ✅ | CT Lake = API calls, SQL, managed. Security Lake = all logs, OCSF, your S3. | — | CloudTrail Lake vs Security Lake |
| 1085 | D4 | Cognito User Pool token + direct AssumeRoleWithWebIdentity — why fails? | A: Use Identity Pool instead (managed STS) | ✅ | Identity Pool handles STS internally. Don't call STS directly. | Q778 | Cognito Identity Pool + role (not direct STS) |
| 1086 | D2/D4 | InsideAWS: attacker on Instance B, same role — containment? | B: Deny-all SG on Instance B | ✅ | InsideAWS = SG isolation. TokenIssueTime kills both. | Q761 | InsideAWS = SG isolation |
| 1087 | D1/D5 | S3 Access Grants prefix overlap: Finance user reads HR data — cause? | A: User in All-Staff group with root prefix grant | ✅ | Broadest grant wins. Prefix overlap = #1 Access Grants misconfiguration. | Q819, Q826 | S3 Access Grants prefix overlap |
| 1088 | D5 | Private CA renewed (new key pair): existing certs affected? | B: Continue working until natural expiry | ✅ | CA renewal ≠ revocation. Previously-issued certs unaffected. | — | Private CA renewal ≠ revocation |
| 1089 | D1 | CloudTrail Insights 10x spike, GuardDuty silent — which true? | B: Complementary — Insights=volume, GD=behavior | ✅ | Spike may be authorized. Different detection lenses. | Q1004 | CloudTrail Insights vs GuardDuty (complementary) |
| 1090 | D5 | Secrets Manager rotation success but new ECS task auth fails on RDS — cause? | A: Rotation Lambda failed ALTER USER on DB | ✅ | Secret changed, DB didn't. Error on DATABASE = rotation Lambda problem. | Q376 | Secrets Manager rotation failure |
| 1091 | D5/D4 | KMS key policy root only + Lambda has s3:GetObject (no kms:Decrypt) — SSE-KMS read? | B: Fails — needs explicit kms:Decrypt | ✅ | Root = delegation not grant. Each principal needs explicit KMS perms. | Q264, Q503 | KMS key policy root = delegation, not grant |
| 1092 | D1 | StopLogging detection: CW metric filter + EventBridge + Config — which fire? | B (wrong: said C) | ❌ | B: EventBridge + Config both fire. CW metric filter blind (StopLogging kills own delivery). | Q860, Q866 | StopLogging kills own CW Logs delivery |
| 1093 | D3 | WAF Bot Control: mobile app fails JS challenge — fix? | A: Scope-down statement excluding mobile app header | ✅ | Scope-down = exempt known-good traffic from rule group. | — | WAF scope-down statement (exempt known traffic) |
| 1094 | D3 | VPC Lattice: cross-account service-to-service, IAM auth, no certs — config? | B: Lattice service network + RAM + IAM auth + auth policy | ✅ | Lattice = east/west, SigV4, share via RAM, auth policies. | — | VPC Lattice (cross-account service-to-service + IAM) |
| 1095 | D4/D6 | Data perimeter 3 layers: block IN + block OUT + AWS services — which THREE? | A+B+E (wrong: picked C) | ❌ | A+B+E: RCP S3 + SCP ResourceAccount + RCP KMS. Bucket policy doesn't scale. | Q398 | Data perimeter (RCP blocks IN, SCP blocks OUT) |
| 1096 | D6 | cfn-guard: block RDS without encryption before deploy — approach? | B: cfn-guard rules in CI/CD pipeline | ✅ | cfn-guard = policy-as-code for templates, shift-left. | — | CloudFormation Guard (template validation in pipeline) |
| 1097 | D5 | DLM: daily EBS snapshots + 30d retention + cross-region + auto-delete — service? | B: DLM policy with tag, schedule, retention, cross-region | ✅ | DLM = EBS snapshot automation, all native. | — | Data Lifecycle Manager (EBS snapshots) |
| 1098 | D5 | DataSync: 50TB weekly NFS→S3, TLS, filter *.parquet, throttle — approach? | B: DataSync agent + TLS + include filter + bandwidth limit | ✅ | DataSync = recurring on-prem→AWS with built-in features. | — | DataSync (encrypted transfer + filtering + throttling) |
| 1099 | D6 | Well-Architected Tool: CISO wants architectural gaps + improvement plan — service? | B: Well-Architected Tool Security Pillar | ✅ | Architecture review + improvement plan + milestones. | Q1031 | Well-Architected Tool = architecture review + improvement plan |
| 1100 | D5/D3 | Kinesis encrypted consumer: has GetRecords, Access Denied — missing? (TWO) | C+D (wrong) | ❌ | A+C: kms:Decrypt + kms:DescribeKey. Not CreateGrant. | Q879 | Kinesis consumer = Decrypt + DescribeKey |
| 1101 | D6/D1 | Config org custom rule: "Unable to invoke" in members — fix? | B: Lambda resource-based policy for config.amazonaws.com | ✅ | Org custom rule = cross-account invoke. Resource policy needed. | Q908 | Config org custom rule cross-account invoke |
| 1102 | D5 | S3 Batch Operations: one job us-east-1, targets 4 regions — result? | C: Fails — Batch is regional | ✅ | Job + manifest + target = same region. Need 4 jobs. | Q872 | S3 Batch Operations regional |
| 1103 | D3/D4 | Verified Access: stolen laptop, block only that device — action? | B: Mark non-compliant in CrowdStrike | ✅ | Device trust provider = surgical device-level control. | Q336 | Verified Access trust providers |
| 1104 | D3 | GWLB: source IP shows GWLB IP, not client — fix? | B: Appliance decapsulate GENEVE outer header | ✅ | Original packet inside GENEVE tunnel. Decapsulate to see real IP. | Q905 | GWLB GENEVE decapsulation |
| 1105 | D4/D5 | 5-layer cross-account SSE-KMS: SCP ViaService + RCP + session + key policy B root — succeeds? | C: Succeeds — all gates pass | ✅ | Server-side KMS, ViaService satisfied, session doesn't gate, RCP same-org, key policy enables. | Q591 | Full 5-layer cross-account evaluation |
| 1106 | D1 | GuardDuty S3 Protection: anomalous download patterns, zero code — service? | B: GuardDuty S3 Protection | ✅ | Anomalous + zero code = GuardDuty S3 Protection. | Q568 | Detect vs prevent (GuardDuty vs policy) |
| 1107 | D1 | EventBridge: alert 90s on iam:CreateAccessKey for root — approach? | C: EventBridge rule in management account | ✅ | Specific API + fast + org trail = EventBridge. | Q474 | EventBridge for API call detection |
| 1108 | D2 | OutsideAWS + ALB production: stop attacker, keep app up — which TWO? | B+A (wrong: picked A deny-all SG) | ❌ | B+C: TokenIssueTime + EBS snapshot. Deny-all SG kills ALB traffic. | Q820 | OutsideAWS + can't disrupt = TokenIssueTime + snapshot |
| 1109 | D1 | Bucket policy grants external, no access yet, AA+GD enabled — which fires? | B: Only Access Analyzer | ✅ | AA = static policy. GD = needs actual access. | Q518 | Access Analyzer static + GuardDuty ≠ failed attempts |
| 1110 | D2 | Forensics Orchestrator: deny-all SG then SSM fails — why? | B: Deny-all blocks outbound to SSM | ✅ | Deny-all = no outbound. SSM needs HTTPS out. Acquire BEFORE isolate. | Q937 | Forensics Orchestrator (deny-all blocks SSM) |
| 1111 | D1 | Security Lake: OCSF + all sources + your S3 + Splunk subscriber — service? | B: Security Lake | ✅ | OCSF + your S3 + subscriber model = Security Lake. | — | Security Lake (OCSF + your S3 + subscriber) |
| 1112 | D2 | CreateSampleFindings: test full IR pipeline without real incident — approach? | B: CreateSampleFindings API | ✅ | Generates realistic findings through EventBridge. FIS = infra failures. | Q934 | CreateSampleFindings = test IR pipeline |
| 1113 | D1 | EC2 DNS to C2 domain then TLS TCP — findings + ThreatPurpose? | B: Impact then Trojan | ✅ | DNS = Impact. Active TCP to C2 = Trojan. Mining = CryptoCurrency. | Q655 | GuardDuty finding types (C2 = Trojan) |
| 1114 | D1 | Top 10 source IPs by bytes, Flow Logs in CW — tool? | B: CW Logs Insights | ✅ | Data in CW + aggregation = Insights. Detective = investigate from finding. | Q236 | CW Logs Insights for aggregation |
| 1115 | D2 | ARC zonal shift: gray failure, AZ-B errors, health checks pass — action? | B: ARC zonal shift | ✅ | LB-level, seconds, no DNS, temporary. Gray failures = ARC. | Q936 | ARC zonal shift |

### Session 99 — 2026-06-20

**Domains:** D3 Infrastructure + D5 Data Protection + D1 Detection + D4 IAM + D2 Incident Response + D6 Governance (Week 2 DOJO GAP DRILL - Udemy + Dojo 3 operational gaps)
**Score:** 16 ✅ · 0 ⚠️ · 9 ❌ (64% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1116 | D3 | API GW mTLS: private Root CA, B2B integrations — config? | C | ✅ | S3 truststore PEM + custom domain + enable mTLS + Route 53 | Q967, Q1012 | API Gateway mTLS = custom domain + S3 truststore |
| 1117 | D3 | API GW: Cognito web + HMAC legacy + IP block at boundary — config? | C | ✅ | Cognito + REQUEST authorizer + Resource Policy IP deny | Q1013 | Resource Policy = boundary rejection (before authorizer) |
| 1118 | D3/D5 | CloudFront FLE: encrypt claim_id at edge with asymmetric crypto — config? | B | ✅ | RSA key + Profile + Config + cache behavior | — | CloudFront FLE setup chain |
| 1119 | D3 | Inspector SBOM: CycloneDX to central S3 — which TWO? | C+D | ❌ | A+C: Inspector native export + bucket policy for inspector2.amazonaws.com | Q1051, Q1059 | Inspector SBOM = native export + bucket policy |
| 1120 | D1 | Macie: custom regex + keywords + proximity — config? | A | ✅ | Custom data identifier + regex + keywords + proximity | — | Macie custom data identifiers |
| 1121 | D1 | ELB access logs: centralize + searchable + TLS cipher metrics — arch? | B | ✅ | S3 + Athena + PutMetricData to CloudWatch | — | ELB access logs = S3 only |
| 1122 | D4 | MFA condition keys: require MFA + 3hr session max — which TWO? | B+E | ✅ | MultiFactorAuthPresent:true + MultiFactorAuthAge NumericLessThan 10800 | — | MFA condition keys |
| 1123 | D2/D3 | NACL vs SG: isolate instance with active connections immediately — action? | D | ✅ | NACL deny all (stateless, kills tracked connections) | — | NACL kills active connections (SG won't) |
| 1124 | D5 | AWS Backup: DynamoDB 10th+20th monthly, retain 4mo — which TWO? | B+D | ❌ | A+B: AWS Backup + cron expression (specific dates = cron, not PITR) | — | Cron vs Rate vs PITR |
| 1125 | D5 | KMS key type: auto-rotate + control + old data readable — type? | D | ✅ | Customer managed with AWS KMS-generated material | — | KMS key type selection |
| 1126 | D3 | IDS on EC2, inspect full packets passively — action? | A (GWLB) | ❌ | C: VPC Traffic Mirroring (passive copy to NLB target) | Q30 (Dojo 3) | Traffic Mirroring = passive. GWLB = inline. 3x failed. |
| 1127 | D1/D3 | Ensure CW agent installed + re-applied every 30min + on launch — service? | D (Config) | ❌ | B: SSM State Manager association (desired-state + schedule) | Q1048, Q1071 | State Manager = schedule enforcement (proactive) |
| 1128 | D1 | Public hosted zone DNS misconfiguration logging — solution? | B | ✅ | DNS query logging for public hosted zone (CW Logs only) | — | DNS query logging vs Resolver logging |
| 1129 | D6 | No public IPs BEFORE provisioned via CF + Security Hub — mode? | B | ✅ | Config proactive evaluation | — | Config proactive vs detective |
| 1130 | D3/D4 | CF serves SPA, prevent unauthenticated CF access — which TWO? | C+B | ✅ | Lambda@Edge viewer-request JWT validation + Cognito hosted UI | — | OAC vs Lambda@Edge auth |
| 1131 | D2 | Windows EC2 won't boot, need memory dump — approach? | C | ✅ | EC2Rescue for Windows Server | — | EC2Rescue Windows |
| 1132 | D2 | Secure access no SSH + record session keystrokes — solution? | A (CW Agent) | ❌ | B: Session Manager with built-in session logging | — | Session Manager logging = session activity (not CW Agent) |
| 1133 | D4 | JWT compromise, verify tokens most securely — method? | B | ✅ | aws-jwt-verify library (RSA signature verification) | — | JWT decode vs verify |
| 1134 | D4 | Lambda Access Denied writing S3, analyst works in console — cause? | A | ✅ | Lambda execution role lacks s3:PutObject | — | Lambda execution role vs caller |
| 1135 | D3 | DNSSEC enabled on subdomain, broken trust chain — cause? | B (DNSKEY) | ❌ | C: DS record missing in parent zone | — | DNSSEC broken chain = DS in parent |
| 1136 | D3 | ALB + HIDS + PFS, don't interfere with HIDS — solution? | A | ✅ | HTTPS with ECDHE end-to-end to EC2, PFS | — | ALB+HIDS+PFS (ECDHE) |
| 1137 | D1 | GuardDuty CryptoCurrency suppression, ASG replaces instances — approach? | C | ✅ | Tag instances + suppression rule by finding type + tag | — | Suppression by tag (not instance ID) |
| 1138 | D6 | Protect CF stack resources from modification + prevent deletion — which TWO? | D+E | ❌ | A+B: Stack Policy Update:* + termination protection | — | Stack Policy = protect resources inside stack |
| 1139 | D4 | Deny federated user Bill in bucket policy — ARN format? | D (iam::) | ❌ | C: arn:aws:sts::account:federated-user/Bill | — | Federated user ARN = sts:: not iam:: |
| 1140 | D4/D5 | Org-wide enforce specific KMS key + least privilege on key — which TWO? | B+E | ❌ | B+C: SCP (enforce key) + Key policy (who uses it) | — | SCP = what key, Key policy = who uses it |

---

### Session 100 — 2026-06-20

**Domains:** D3 Infrastructure · D5 Data Protection · D4 IAM · D1 Detection · D6 Governance · D2 Incident Response
**Score:** 42.5 ✅ · 0 ⚠️ · 4.5 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1141 | D6 | CF service role, dev has cloudformation:* only, create-stack fails — cause? | B | ✅ | iam:PassRole missing on CFDeployRole | — | CF service role + PassRole |
| 1142 | D6 | Stack Policy Deny Update:* + termination protection, dev deletes RDS via console — result? | C | ✅ | RDS deleted — neither protects manual actions | Q1138 | Stack Policy ≠ manual actions |
| 1143 | D4/D6 | SCP restrict PassRole to platform team for Lambda+ECS — which statement? | B | ✅ | Deny iam:PassRole + StringNotLike PrincipalARN + PassedToService | — | SCP + PassRole restriction |
| 1144 | D3 | IDS full packets, passive, no production impact — architecture? | C | ✅ | Traffic Mirroring → NLB → IDS EC2 | Q1126 | Traffic Mirroring = passive |
| 1145 | D3 | Suricata rules, drop malicious egress — architecture? | B | ✅ | Network Firewall stateful DROP rules | Q1126 | Network Firewall = inline IPS |
| 1146 | D3 | Third-party Palo Alto, inline, transparent, scale, health-check — architecture? | C | ✅ | GWLB with Palo Alto targets | Q1126 | GWLB = third-party inline |
| 1147 | D3 | EC2 public IP to another EC2 public IP, SG ref sg-aaa, times out — cause? | C | ✅ | Public IP traffic via IGW = source is public IP, not SG ref | — | Public IP via IGW |
| 1148 | D3 | IPv6 outbound only, block inbound — component? | B | ✅ | Egress-Only Internet Gateway | — | Egress-Only IGW (IPv6) |
| 1149 | D3 | Lambda private subnet, SQS Interface endpoint exists, timeout — missing? | A | ✅ | Lambda SG missing outbound 443 | — | Interface endpoint dual SGs |
| 1150 | D5/D3 | Gateway endpoint allows Get+List, Lambda calls PutObject — error? | B | ✅ | Access Denied (endpoint policy allowlist) | Q535 | Gateway endpoint policy |
| 1151 | D3 | Network Firewall proposed for passive IDS — why incorrect? | B | ✅ | NF is inline — failure stops traffic | Q1126 | NF inline vs Traffic Mirroring passive |
| 1152 | D5 | CRR SSE-KMS, has Encrypt dest + GetObjectVersionForReplication, fails — missing? | B | ✅ | kms:Decrypt on source key (CMK-A) | Q883 | CRR D-G-F permissions |
| 1153 | D5 | Key material must auto-expire after 30 days — config? | B | ✅ | Imported key material with 30-day expiration | — | Imported key expiration |
| 1154 | D5 | CancelKeyDeletion called, key shows Disabled — why? | B | ✅ | CancelKeyDeletion → Disabled (must re-enable) | — | KMS key lifecycle |
| 1155 | D4/D5 | SCP Deny kms:Decrypt unless ViaService, dev calls from CLI — result? | B | ✅ | Denied — no ViaService context on direct call | Q488 | kms:ViaService + SCP |
| 1156 | D5 | Auto-rotation + full control + old data decryptable — key type? | C | ✅ | Customer-managed + AWS-generated material | — | KMS key type selection |
| 1157 | D1/D3 | State Manager CW agent on boot + every 30min — config? | B | ✅ | ONE association with OnBoot + rate(30min) | Q1048 | State Manager dual triggers |
| 1158 | D3 | DNSSEC subdomain, SERVFAIL for validating resolvers — cause? | C | ✅ | DS record missing in parent zone | Q1135 | DNSSEC broken chain |
| 1159 | D1 | Public DNS queries to hosted zone — which logging? | B | ✅ | Route 53 DNS query logging (not Resolver) | — | DNS query vs Resolver logging |
| 1160 | D1/D6 | Detect unversioned buckets + prevent via CF — which combo? | B | ✅ | Config detective + Config proactive evaluation | — | Config proactive vs detective |
| 1161 | D3 | Inspector via StackSets, 8 new accounts missing — cause? | B | ✅ | Inspector has native delegated admin + auto-enable | Q483 | Native org-wide deployment |
| 1162 | D2 | Windows EC2 won't boot, collect memory dump — tool? | C | ✅ | EC2Rescue for Windows Server | — | EC2Rescue Windows |
| 1163 | D2 | Session Manager record all keystrokes encrypted — config? | B | ✅ | Session Manager logging → encrypted CW Logs | Q1132 | Session Manager logging |
| 1164 | D4 | JWT tampered, most secure verification — method? | B | ✅ | aws-jwt-verify (RSA signature verification) | — | JWT verify vs decode |
| 1165 | D4 | Lambda Access Denied PutObject, analyst works in console — cause? | B | ✅ | Lambda execution role missing permission | — | Lambda execution role |
| 1166 | D2 | Capture volatile memory, instance stays running — action? | C | ✅ | No-reboot AMI | Q810 | No-reboot AMI |
| 1167 | D3 | ALB + HIDS + PFS — config? | B | ✅ | ECDHE end-to-end to EC2, HIDS inspects after decrypt | — | ALB+HIDS+PFS |
| 1168 | D1 | GuardDuty CryptoCurrency, ASG replaces instances — suppression approach? | B | ✅ | Tag + finding type filter (not instance ID) | — | Suppression by tag |
| 1169 | D4 | Deny federated user Bill in bucket policy — ARN format? | C | ✅ | arn:aws:sts::account:federated-user/Bill | Q1139 | Federated user ARN |
| 1170 | D4/D5 | Enforce specific KMS key org-wide + least privilege on key — which TWO? | B+C | ✅ | SCP (enforce key) + Key policy (who uses it) | Q1140 | SCP + key policy |
| 1171 | D3 | mTLS 403, same CA, new 16th partner — check first? | B | ✅ | Partner's cert expired | Q967 | mTLS cert expiry |
| 1172 | D3 | mTLS uploaded PEM to ACM, enabled on default endpoint — TWO problems? | B (partial) | ⚠️ | A+B: custom domain required + S3 not ACM. Missed A. | Q967 | mTLS = custom domain + S3 |
| 1173 | D3 | mTLS revoke ONE compromised cert — action? | B | ✅ | Add CRL to S3 truststore | Q1032 | mTLS CRL revocation |
| 1174 | D5 | CRR custom encryption context fails, no-context objects work — cause? | B | ✅ | CRR preserves context, dest key policy rejects it | Q923 | CRR custom context |
| 1175 | D5/D4 | DynamoDB CMK, has Decrypt+GenerateDataKey, PutItem fails — missing? | B | ✅ | kms:CreateGrant + kms:DescribeKey | Q899 | DynamoDB + CMK |
| 1176 | D5/D3 | Kinesis consumer, has GetRecords + kms:Decrypt, fails — missing? | B | ✅ | kms:DescribeKey | Q879 | Kinesis consumer perms |
| 1177 | D3 | IoT cert revoked, attacker connects 5s later — result? | B | ✅ | Fails immediately (registry check at TLS) | Q892 | IoT instant revocation |
| 1178 | D3 | mTLS remove CA from truststore — what happens? | B | ✅ | ALL partners using that CA blocked | — | mTLS remove CA |
| 1179 | D5 | Backup on 10th+20th monthly — schedule type? | B | ✅ | cron expression | Q1124 | Cron vs Rate |
| 1180 | D3 | Flow Logs inbound ACCEPT, outbound REJECT — cause? | B | ✅ | NACL missing outbound ephemeral rule | Q707 | NACLs stateless |
| 1181 | D6 | Stack Policy: Aurora locked, Lambda modify-only, SQS full — which? | A | ✅ | Deny Update:* on *, Allow Modify Lambda, Allow * SQS | Q1138 | Stack Policy default deny |
| 1182 | D3 | Inspector SBOM via SSM+Lambda — what's wrong? | B | ✅ | Inspector has native SBOM export (unnecessary custom) | Q1059 | Inspector SBOM native |
| 1183 | D5 | EMR inter-node encryption, engineer picks Nitro — why wrong? | B | ✅ | EMR = security config + PEM certs (not Nitro) | Q1030 | EMR in-transit |
| 1184 | D5/D3 | Gateway endpoint allows Get+Put, Lambda calls ListBucket — result? | B | ✅ | Access Denied (not in endpoint policy) | Q535 | Gateway endpoint allowlist |
| 1185 | D4 | MFA session max 3 hours — condition key? | B | ✅ | aws:MultiFactorAuthAge NumericLessThan 10800 | — | MFA condition keys |
| 1186 | D2 | SageMaker: custom viz + reusable template + query Lake — tool? | B | ✅ | SageMaker notebooks | Q996 | SageMaker vs Detective |
| 1187 | D3 | Bedrock mandatory guardrail enforcement — how? | D | ❌ | B: IAM condition bedrock:GuardrailIdentifier | — | Bedrock guardrail condition key |
| 1188 | D3 | Q Business user sees HR docs, ACLs enabled — cause? | B | ✅ | ACL identity mapping failed | Q1010 | Q Business ACL |
| 1189 | D3 | VPC Lattice: only Service A can call B, deny C — where enforce? | B | ✅ | Auth policy on Service B (resource-based) | — | VPC Lattice auth policy |
| 1190 | D3 | WAF Bot Control blocks mobile app (no JS) — fix? | B | ✅ | Scope-down statement excluding mobile header | — | WAF scope-down |
| 1191 | D3 | Bedrock SCP enforce guardrail — which statement? | A | ✅ | Deny InvokeModel + StringNotEquals GuardrailIdentifier | Q1187 | Bedrock guardrail condition key |


### Session 101 — 2026-06-20

**Domains:** D6 Governance · D5 Data Protection · D1 Detection · D3 Infrastructure · D4 IAM
**Score:** 13.5 ✅ · 1 ⚠️ · 0.5 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1192 | D6 | cfn-guard rule SSEAlgorithm=aws:kms, dev sends AES256 — result? | B | ✅ | Pipeline FAIL, blocks before reaching CF | — | cfn-guard shift-left |
| 1193 | D5 | 10TB nightly NFS→S3, TLS + throttle + modified-only — service? | B | ✅ | DataSync (built-in TLS + bandwidth + filter) | — | DataSync features |
| 1194 | D5 | EBS snapshots 12hr + 7d retain + cross-region + DR KMS — service? | B | ✅ | Data Lifecycle Manager policy | — | DLM automation |
| 1195 | D6 | Assess workloads vs WA Security Pillar, track improvements — service? | C | ✅ | Well-Architected Tool | — | WAT vs Audit Manager |
| 1196 | D1 | StopLogging called, CW metric filter on log group — alerted? | B | ✅ | No — StopLogging kills CW delivery | Q860 | StopLogging blinds CW |
| 1197 | D3 | Lattice: add C to network, B auth policy allows only A — fixed? | B | ✅ | No — network = reachability, auth policy = authorization | — | Lattice auth vs network |
| 1198 | D3 | SAST pre-deploy: hardcoded keys + SQLi + insecure SDK — service? | B | ✅ | CodeGuru Security | — | CodeGuru = SAST |
| 1199 | D3 | Bot Control Challenge blocks server-to-server API clients — fix? | B | ✅ | Scope-down excluding X-Client-Type: api | — | WAF scope-down |
| 1200 | D4/D6 | RCP deny s3:* non-org, Lambda writes own bucket + partner bucket — result? | C | ✅ | Both succeed: own (org match) + partner (not your resource) | — | RCP scope = your resources only |
| 1201 | D1 | StopLogging: which of CW filter / EventBridge / Config fire? | B only | ⚠️ | B+C: EventBridge (seconds) + Config (minutes). CW = never | Q860 | Config also detects StopLogging |
| 1202 | D3 | Private API: Lambda A works, Lambda B timeout, same VPC/endpoint — cause? | B | ✅ | Lambda B SG missing outbound 443 | Q1025 | Interface endpoint dual SGs |
| 1203 | D4/D5 | KMS key policy grants only Account A root, Account B (same org) calls Decrypt directly — result? | B | ✅ | Fails — key policy must name external account | Q541 | Cross-account KMS key policy must name external account |
| 1204 | D5 | Bucket policy Deny if KMS key header missing, upload without flags, default encryption set — result? | B | ✅ | Denied — policy evaluates before default encryption | Q426 | Default encryption vs bucket policy Deny |
| 1205 | D2/D4 | InsideAWS, attacker on Instance B, shared role, both production — containment? | B | ✅ | Deny-all SG on Instance B only | Q761 | InsideAWS = SG isolation |
| 1206 | D1/D4/D5/D6 | Static analysis + 60s API alert + block external + anomalous downloads — match 4 services? | A | ✅ | Access Analyzer + EventBridge + RCP + GuardDuty S3 Protection | — | Full detect/prevent architecture |


### Session 102 — 2026-06-21

**Domains:** D3 Infrastructure · D1 Detection · D5 Data Protection · D6 Governance · D2 Incident Response
**Score:** 7 ✅ · 0 ⚠️ · 3 ❌ (70% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1207 | D3 | mTLS setup, S3 bucket NO versioning enabled — what happens? | A | ❌ | B: Custom domain creation fails — versioning required for object version reference | Q967 | mTLS S3 versioning required |
| 1208 | D3 | Inspector SBOM export fails cross-account AccessDenied on PutObject — fix? | B | ✅ | Bucket policy for inspector2.amazonaws.com service principal | Q1059 | Inspector SBOM = native export + bucket policy |
| 1209 | D1/D3 | State Manager CIS on boot + every 2hr — minimum associations? | B | ✅ | ONE association with OnBoot + rate(2 hours) | Q1048 | State Manager OnBoot + schedule (dual triggers) |
| 1210 | D1/D3 | Config 8-12min gap on new instances, eliminate gap — approach? | B | ✅ | State Manager OnBoot + rate (proactive, zero gap) | Q1127 | State Manager = proactive vs Config = reactive |
| 1211 | D6 | WAT 4 HRIs + 7 MRIs, track improvement over 3 quarters — feature? | C | ❌ | A: Milestones — snapshot current state, compare across quarters | Q1031 | Well-Architected Tool milestones |
| 1212 | D2 | Multi-account breach, custom Python + interactive graph + reusable notebook — tool? | B | ✅ | SageMaker AI notebooks (custom code + reusable + arbitrary queries) | Q996 | SageMaker notebooks vs Detective (custom vs built-in) |
| 1213 | D6 | Reject CF template without mTLS before any resource exists — mechanism? | B | ❌ | C: cfn-guard in CI/CD (validates template content, shift-left) | — | cfn-guard vs Config proactive (template validation) |
| 1214 | D5 | EMR inter-node encryption, engineer proposes Nitro on C5 — why wrong? | B | ✅ | EMR = security config + PEM certs (not Nitro) | Q1030 | EMR in-transit = security config + PEM certs |
| 1215 | D6 | cfn-guard passes, dev disables DeletionProtection via Console — limitation + fix? | A | ✅ | cfn-guard = template only. SCP blocks runtime API call. | — | cfn-guard limitation (shift-left only) |
| 1216 | D6/D3/D1 | Match: template validation + boot enforcement + API block — three mechanisms? | B | ✅ | cfn-guard + State Manager (OnBoot+rate) + SCP | — | Three enforcement moments |
| 1217 | D3 | Inspector SBOM — no scheduling option in console — explanation? | B | ✅ | On-demand API only. EventBridge + Lambda for scheduling. | Q1051 | Inspector SBOM = on-demand API (no built-in scheduler) |
| 1218 | D1/D3 | State Manager OnBoot + rate(4hr), instance reboots at 14:30 — what happens? | A | ✅ | OnBoot fires immediately, next rate run still at 17:00 (independent triggers) | Q1048 | State Manager dual triggers independent |
| 1219 | D5 | EMR cluster TLS fails between nodes, security config enabled — missing? | B | ✅ | PEM certificates (Private CA or custom) | Q1030 | EMR in-transit = security config + PEM certs |
| 1220 | D6 | cfn-guard in CI/CD, dev deploys non-compliant via Console — what catches it? | C | ❌ | B: Config proactive evaluation (service-level, can't bypass) | — | cfn-guard bypassable vs Config proactive service-level |
| 1221 | D6 | WAT milestones NOT show — which is correct? | B | ❌ | C: Automated evidence (Config/CloudTrail). Milestones DO show per-question changes. | Q1031 | WAT milestones = no automation |
| 1222 | D6 | Both CI/CD and Console CF deploys must be validated — architecture? | B | ✅ | Config proactive evaluation (service-level, catches all paths) | Q1220 | Config proactive = service-level, can't bypass |
| 1223 | D3 | mTLS S3 URI without specifying object version — result? | B | ✅ | Domain creation fails — explicit truststoreVersion required | Q1207 | mTLS S3 versioning + object version required |
| 1224 | D4 | Bucket policy Deny with StringNotEquals federated-user ARN — what happens? | B | ✅ | Allowed — federated user ARN matches, condition FALSE, Deny doesn't fire | Q1139 | Federated user ARN = sts:: not iam:: |
| 1225 | D6 | Stack Policy: Aurora no replace/delete, Lambda no delete, SQS unrestricted — config? | A | ❌ | B: Allow Update:* all, then Deny Replace+Delete on Aurora, Deny Delete on Lambda | Q1138 | Stack Policy default deny + selective Deny |
| 1226 | D6 | WAT milestone comparison — what does it NOT show? | B | ❌ | C: Automated evidence. Milestones DO show per-question risk changes. | Q1206 | WAT milestones = no automated evidence |
| 1227 | D4/D6 | RCP on S3, ELB SLR writes access logs — succeeds or fails? | B | ✅ | Succeeds — SLRs exempt from RCPs | — | RCP SLR exemption |
| 1228 | D5 | EC2 encrypted EBS won't start, role has kms:Decrypt — missing? | B | ✅ | kms:CreateGrant | — | EC2 EBS always needs CreateGrant |
| 1229 | D1 | CryptoCurrency:EC2/BitcoinTool.B — detection method? | B | ✅ | Active TCP to mining pool (not DNS) | — | GD finding type = detection method |
| 1230 | D5 | CRR SSE-KMS replication role — three permissions? | B | ✅ | Decrypt source + GenerateDataKey dest + GetObjectVersionForReplication | — | CRR D-G-F |
| 1231 | D2 | IAM user creds on GitHub, 2 keys + console + STS — first containment? | B | ❌ | A: Deactivate key + inline Deny * on user (covers ALL paths) | — | User = Deny *. Role = TokenIssueTime. |
| 1232 | D6 | Stack Policy Allow * + Deny Replace/Delete on Aurora, dev changes engine (requires replacement) — result? | B | ✅ | Fails — explicit Deny Update:Replace blocks | Q1225 | Stack Policy explicit Deny wins |
| 1233 | D6 | WAT Jan milestone 4 HRIs, June milestone 1 HRI — what does CISO see? | A | ❌ | B: Per-question risk changes (self-reported). NO automated evidence. | Q1221 | WAT = self-reported, no automation |


### Session 103 — 2026-06-22

**Domains:** D1 Detection · D3 Infrastructure · D4 IAM · D5 Data Protection · D6 Governance (Dojo Practice Exam Set 4)
**Score:** 22 ✅ · 0 ⚠️ · 11 ❌ (67% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1234 | D1 | Config rules enabled, GenerateCredentialReport shows noncompliant — cause? | C: MaximumExecutionFrequency 3hr | ❌ | D: Credential report cached 4hrs, recent changes not reflected yet | — | IAM Credential Report 4-hour cache |
| 1235 | D4 | 1200 accounts, backlog, teams independently provision roles with limited scope — approach? | A: Service Catalog templates | ❌ | C: SCP + permissions boundary delegation (teams create within guardrails) | — | Permission boundary delegation vs Service Catalog |
| 1236 | D4/D6 | Restrict to ap-southeast-1, existing + future accounts in Development OU — SCP attachment? | A: Attach to individual accounts | ❌ | C: Attach to Development OU (auto-applies to future accounts) | — | SCP attachment OU vs accounts |
| 1237 | D5 | EBS snapshot default key can't share, need to share with security account — steps? (THREE) | A+B+E (create volume) | ❌ | A+C+E: Create CMK + copy snapshot with CMK + share snapshot + grant key access | — | EBS snapshot sharing (copy with CMK, no volume needed) |
| 1238 | D4/D6 | Minimize risk if root compromised across member accounts — approach? | A: Deactivate root access key | ❌ | D: SCP to block service access for root user (blocks ALL paths) | — | SCP block root (containment vs hygiene) |
| 1239 | D3 | Public-facing HTTPS + SSH via bastion only — EC2 SG rules? (TWO) | A+D (443 from internal subnet) | ❌ | B+D: 443 from 0.0.0.0/0 (public-facing) + 22 from security team | — | Public-facing = 0.0.0.0/0 on 443 |
| 1240 | D1 | Custom logs on EC2, available within 30min, no interactive sessions — approach? (TWO) | D+E (SSM agent ships logs) | ❌ | A+E: CloudWatch agent ships logs + EventBridge schedule with SendCommand | — | CW agent ships logs (not SSM agent) |
| 1241 | D5 | EC2 needs secrets during bootstrapping, strict permissions — approach? | B: Secrets Manager + CF ValueFrom | ❌ | D: Parameter Store + IAM role + ssm:GetParameters at runtime (boot time) | — | Boot-time retrieval vs deploy-time injection |
| 1242 | D5/D3 | Rotation Lambda "Unable to log into database", SM VPC endpoint works — cause? | C: Force rotation via CLI | ❌ | D: Lambda SG egress + EC2 SG ingress rules missing (network issue) | — | Rotation Lambda can't reach DB = SG issue |
| 1243 | D1/D3 | Match log sources: intra-subnet, DNS, hub-and-spoke, HTTP patterns — ordering? | Swapped VPC Flow and TGW Flow | ❌ | VPC Flow=intra-subnet, Resolver=DNS, TGW Flow=hub-and-spoke, ELB=HTTP | — | VPC Flow vs TGW Flow Logs scope |
| 1244 | D6 | Security Hub setup ordering (4 steps) | Wrong order | ❌ | Enable SH in admin → Designate admin → Enable in members → Cross-account access | — | Security Hub setup ordering (E-D-M-A) |


### Session 104 — 2026-06-22

**Domains:** D1 Detection · D3 Infrastructure · D4 IAM · D5 Data Protection · D6 Governance (Dojo 4 re-test drill)
**Score:** 8 ✅ · 0 ⚠️ · 2 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1245 | D1 | GenerateCredentialReport shows old MFA state after 2hrs — cause? | B: 4hr cache | ✅ | Credential report cached 4 hours | Q1234 | IAM Credential Report 4-hour cache |
| 1246 | D4 | 500 accounts, teams create own roles, limit to s3:GetObject+logs:* — approach? | B: SCP + boundary | ✅ | SCP requiring boundary on CreateRole | Q1235 | Permission boundary delegation vs Service Catalog |
| 1247 | D4/D6 | SCP restricts eu-west-1, new account in OU uses us-east-1 — why? | A: Attached to accounts not OU | ✅ | Attach to OU for auto-apply | Q1236 | SCP attachment OU vs accounts |
| 1248 | D5 | EBS snapshot aws/ebs key, can't share — fastest fix? | B: Copy with CMK then share | ✅ | Copy snapshot with CMK | Q1237 | EBS snapshot sharing (copy with CMK, no volume needed) |
| 1249 | D4/D6 | Root creds leaked 50 member accounts, broadest single containment? | C: SCP deny root | ✅ | SCP blocks all paths | Q1238 | SCP block root (containment vs hygiene) |
| 1250 | D3 | Public HTTPS API + SSH from bastion 10.0.1.0/24 — SG rules? | D: port 80 from 0.0.0.0/0 | ❌ | B: 443 from 0.0.0.0/0 + 22 from 10.0.1.0/24. HTTPS=443 not 80. | Q1239 | Public-facing = 0.0.0.0/0 on 443 |
| 1251 | D1 | Custom logs on 200 EC2, queryable in CW Logs Insights — what ships? | B: CloudWatch agent | ✅ | CW agent ships logs | Q1240 | CW agent ships logs (not SSM agent) |
| 1252 | D5 | EC2 UserData needs DB password at boot, keep out of CF — approach? | B: Instance role + SM API call | ✅ | Runtime retrieval, not CF injection | Q1241 | Boot-time retrieval vs deploy-time injection |
| 1253 | D1/D3 | Lateral movement same subnet — which log source? | C: VPC Flow Logs | ✅ | VPC Flow = intra-VPC, TGW = cross-VPC | Q1243 | VPC Flow vs TGW Flow Logs scope |
| 1254 | D5/D3 | Rotation Lambda "Unable to log into database", SM endpoint works — cause? | C: Password policy | ❌ | B: Lambda SG no outbound to DB SG. "Unable to log in" = network issue. | Q1242 | Rotation Lambda can't reach DB = SG issue |


### Session 105 — 2026-06-22

**Domains:** D1 Detection · D3 Infrastructure · D4 IAM · D5 Data Protection · D6 Governance (Killer difficulty cross-domain drill)
**Score:** 9 ✅ · 0 ⚠️ · 1 ❌ (90% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1255 | D4/D5 | Direct kms:Decrypt from Lambda, SCP ViaService=s3 only, all network correct — cause of AccessDenied? | C: SCP denies (no ViaService context) | ✅ | Direct call = no ViaService → SCP Deny fires | Q488 | kms:ViaService + SCP |
| 1256 | D1 | StopLogging called: CW metric filter + EventBridge + Config — which TWO fire? | B+E (EventBridge + Security Hub) | ❌ | B+C: EventBridge + Config. CW metric filter blind. Security Hub = same as Config underneath. | Q860, Q1092 | StopLogging kills own CW Logs delivery |
| 1257 | D3 | Traffic Mirroring IDS alerts but doesn't block — switch to inline blocking? | A: Network Firewall Suricata DROP | ✅ | Traffic Mirroring = passive. NF = inline IPS. | Q1126 | Traffic Mirroring = passive. NF = inline. |
| 1258 | D6 | Block ANY future API assigning public IPv4, no policy updates needed — mechanism? | C: Declarative policy | ✅ | State enforcement regardless of API | — | Declarative policies vs SCP |
| 1259 | D4/D5 | ECS task AccessDenied on GetSecretValue after KMS key policy removed Account B — which layer fails? | B: kms:Decrypt (surfaces as SM error) | ✅ | Service wraps underlying KMS failure | Q541, Q974 | Cross-account KMS key policy must name external account |
| 1260 | D1/D4 | RCP blocks external, 500 denied GetObjects, AA + GD enabled — which TWO true? | C+E (GD no finding + Security Hub) | ❌ | B+C: AA flags policy (static) + GD no finding. AA doesn't factor RCP runtime. | Q534, Q706 | Access Analyzer static + GuardDuty ≠ failed attempts |
| 1261 | D3/D5 | S3 Gateway endpoint policy allows Get+Put only, Lambda calls ListBucket — result? | B: Access Denied (not in endpoint policy) | ✅ | Endpoint policy = allowlist | Q535 | Gateway endpoint policy as additional gate |
| 1262 | D2 | Forensics: deny-all SG → SSM memory capture times out, VPC endpoints exist — cause? | B: Deny-all blocks outbound to endpoint ENIs | ✅ | Acquire BEFORE isolate | Q937 | Deny-all SG blocks ALL outbound |
| 1263 | D3 | mTLS custom domain creation fails, PEM valid, IAM correct — cause? | B: S3 bucket no versioning | ✅ | mTLS requires S3 versioning for object version reference | Q1207 | mTLS S3 versioning required |
| 1264 | D1 | StopLogging: CW filter + EventBridge + Config — which detect? | B: EventBridge + Config (2+3) | ✅ | CW filter blind (StopLogging kills delivery) | Q860, Q1092 | StopLogging detection mechanisms |


### Session 106 — 2026-06-22

**Domains:** D1 Detection · D2 Incident Response · D6 Governance (D1+D6 targeted push — killer difficulty)
**Score:** 8 ✅ · 0 ⚠️ · 2 ❌ (80% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1265 | D1 | Bucket policy grants external, no access, AA+GD+RCP — which fires NOW? | B: Only AA | ✅ | AA static, GD needs access, RCP irrelevant to AA | Q534, Q706 | Access Analyzer static + GuardDuty ≠ failed attempts |
| 1266 | D1 | StopLogging then DeleteTrail 5min later — which detects DeleteTrail? | B: Only EventBridge | ✅ | StopLogging killed CW Logs delivery, EB still receives | Q860, Q1092 | StopLogging kills own CW Logs delivery |
| 1267 | D1 | CW Logs Insights vs Detective — which statement true? | B: Insights=open-ended, Detective=entity-based | ✅ | Different tools, different entry points | — | CW Logs Insights vs Detective |
| 1268 | D1 | Same-org account downloads 500 objects 3AM unusual country, no RCP — GD fires? | B: Yes, anomalous behavior | ✅ | GD S3 Protection = behavioral, org membership irrelevant | Q568 | GuardDuty S3 Protection behavioral |
| 1269 | D1 | Detect root CreateAccessKey 300 accounts within 60s — approach? | C: EventBridge in management account | ✅ | Specific API + fast = EventBridge | Q474 | EventBridge for API call detection |
| 1270 | D6 | SCP on OU, new account joins OU, launches without tag — result? | C: Denied, SCP auto-applies | ✅ | SCP on OU = auto for all accounts | Q1236 | SCP attachment OU vs accounts |
| 1271 | D6 | cfn-guard + Config proactive, developer deploys via CF Console — which catches? | A: cfn-guard | ❌ | B: Config proactive (CF service-level). cfn-guard = CI/CD only. | Q1220 | cfn-guard bypassable vs Config proactive service-level |
| 1272 | D6 | All paths must have DeletionProtection — which catches Console+CLI+CF+Terraform? | C: SCP | ✅ | SCP blocks API regardless of deployment method | — | SCP = catches ALL deployment paths |
| 1273 | D6 | Security Hub setup order? | A: Designate → Enable → Members → Access | ❌ | B: Enable SH in admin → Designate → Members → Access (E-D-M-A) | Q1244 | Security Hub setup ordering (E-D-M-A) |
| 1274 | D1 | RCP blocks external, 100 denied, then RCP removed, 50 successful downloads — when GD fires? | B: Week 2 (successful access) | ✅ | GD fires on successful anomalous access only | Q534 | GuardDuty ≠ failed attempts |


### Session 107 — 2026-06-22

**Domains:** D1 Detection · D3 Infrastructure · D5 Data Protection · D6 Governance (D1+D6 uplift drill + D2/D3 cross-domain)
**Score:** 19 ✅ · 0 ⚠️ · 6 ❌ (76% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1275 | D1 | CloudTrail Insights 10x RunInstances, GD silent — which true? | B: Complementary (Insights=volume, GD=behavior) | ✅ | Legit spike triggers Insights not GD | — | CloudTrail Insights vs GuardDuty (complementary) |
| 1276 | D1 | Resolver query logging vs DNS query logging — which captures what? | C: Swapped them | ❌ | B: Resolver=FROM VPC (outbound), DNS query=TO your zone (inbound) | — | Resolver vs DNS query logging direction |
| 1277 | D1 | VPC Flow spike same subnet port 445, "what else did IP talk to 24hr" — tool? | B: Detective | ❌ | A: CW Logs Insights (no finding = no Detective entry point, raw log query) | — | Detective needs finding. No finding = CW Logs Insights |
| 1278 | D1 | Write-only trail, ConsoleLogin EventBridge rule doesn't fire — why? | B: ConsoleLogin is Read event | ✅ | Write-only doesn't deliver Read events to EB | Q710 | CloudTrail management events Read/Write |
| 1279 | D1 | Security Lake: which THREE true? | A+B+E: Your S3 + subscriber + OCSF | ✅ | Correct | — | Security Lake (OCSF + your S3 + subscriber) |
| 1280 | D1 | 200GB/hr WAF logs, full-text, sub-second, dashboards, 90d — arch? | C: Firehose + OpenSearch + UltraWarm | ✅ | Full-text + sub-second = OpenSearch | — | Kinesis + OpenSearch architecture |
| 1281 | D1 | Suppressed findings after removing suppression rule — visible? | B: Yes, archived not deleted | ✅ | Suppression = archive, remove filter = reappear | — | GuardDuty suppression = archive |
| 1282 | D1 | Metric filter value=1, alarm never fires despite ERRORs — cause? | A: Metric value set to 0 | ✅ | Value=0 publishes nothing useful | Q724 | CW metric filter value |
| 1283 | D1 | ELB access logs spike 403s, query for patterns — where + how? | B: S3 + Athena | ✅ | ELB logs = S3 only, query with Athena | — | ELB access logs = S3 only |
| 1284 | D1 | EC2 DNS to C2 beacon then TLS TCP — findings + ThreatPurpose? | B: Impact then Trojan | ✅ | DNS=Impact, TCP to C2=Trojan | Q655 | GuardDuty finding types (C2 = Trojan) |
| 1285 | D2 | OutsideAWS, investigate HOW creds exfiltrated — tool? | A: Detective | ✅ | Finding exists, investigate = Detective | — | Detective for investigation |
| 1286 | D1 | CW Logs agent stopped, instances healthy — first file? | B: /var/log/awslogs.log | ✅ | Runtime log for "was working, stopped" | Q708 | CW Logs agent troubleshooting |
| 1287 | D1 | Config remediation succeeds but SG re-opens 5min later — why? | A: Config frequency | ❌ | B: Something re-added the rule (check CloudTrail for WHO) | — | Remediation succeeds but returns = re-creation |
| 1288 | D1 | Security Lake query — built-in SQL engine? | B: No, use Athena | ✅ | Security Lake = your S3, no built-in engine | — | Security Lake vs CloudTrail Lake |
| 1289 | D1 | StopLogging metric filter works in test, fails in prod attack — why? | A: StartLogging re-enables delivery in test | ✅ | Test = quick restart. Prod = no restart = blind | Q860 | StopLogging kills own CW Logs delivery |
| 1290 | D1 | AA flags SQS queue, RCP deployed, AA still shows finding — why? | B: AA reads policy text, not runtime | ✅ | AA static, doesn't know about RCP | Q534 | Access Analyzer static |
| 1291 | D1 | Recon finding, every IP that probed port 22 in 7 days — tool? | A: Detective | ✅ | Finding exists + entity investigation | — | Detective for investigation |
| 1292 | D1 | VPC Flow Logs sent to S3, CW Logs Insights returns zero — why? | B: Logs in S3 not in CW Logs | ✅ | Insights only queries CW Logs, not S3 | — | CW Logs Insights scope |
| 1293 | D1 | Macie enabled 48hrs, 0 findings despite known PII — cause? | D: CMK blocks Macie | ❌ | B: No discovery job created (Macie enabled ≠ scanning) | — | Macie enabled ≠ Macie scanning |
| 1294 | D1 | Correlate GD+Flow+CT across 20 accounts, OCSF, own S3, Splunk — service? | B: Security Lake | ✅ | Multiple sources + OCSF + your S3 + subscriber | — | Security Lake |
| 1295 | D2/D3 | C2Activity, API behind NLB, block C2 + preserve evidence — TWO? | B+E (NF DROP + DNS FW) | ❌ | B+C: NF DROP + EBS snapshot. "Preserve evidence" = must pick snapshot. | — | Preserve evidence = EBS snapshot |
| 1296 | D3 | NAA found path, need hop-by-hop SG+NACL+route explanation — tool? | A: NAA | ❌ | B: Reachability Analyzer (explains specific path) | — | NAA finds, RA explains |
| 1297 | D2 | OutsideAWS, TokenIssueTime applied, fires again next day — why? | A: SSRF still exists, attacker got fresh creds | ✅ | Token deny kills old, vulnerability still present | — | TokenIssueTime doesn't fix root cause |
| 1298 | D3 | Suricata IPS + block DNS bad domains — minimum services? | A: NF + DNS FW | ✅ | Different layers, complement each other | — | NF + DNS FW complementary |
| 1299 | D2 | IAM user leaked, 2 keys + console + STS — single containment? | C: Deny * on user | ✅ | Blocks all paths | Q942 | User = Deny * |

---

**Session 107 continued — D1 Pure Blitz (10 more questions)**

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1300 | D1 | Lambda resolves malware-c2.evil.com — which log source? | B: Resolver query logging | ✅ | VPC resource outbound lookup = Resolver | — | Resolver vs DNS query logging direction |
| 1301 | D1 | CW Logs Insights query on ELB logs returns zero — why? | B: ELB logs in S3 not CW Logs | ✅ | ELB = S3 only | — | ELB access logs = S3 only |
| 1302 | D1 | EC2 TCP to 5 threat intel IPs port 443 — ThreatPurpose? | D: Recon | ❌ | C: Trojan (outbound to bad IPs = C2) | — | Trojan = outbound. Recon = inbound. |
| 1303 | D1 | CT Lake mgmt-only EDS, query PutObject returns zero — why? | A: PutObject is data event | ✅ | Data event not in mgmt-only EDS | Q882 | CloudTrail Lake (data vs mgmt) |
| 1304 | D1 | GD finding exists, what else instance communicated 48hr, visualize — tool? | C: Detective | ✅ | Finding + visualize + timeline = Detective | — | Detective for investigation |
| 1305 | D1 | Macie SSE-KMS buckets "Unable to analyze" — cause? | B: SLR needs kms:Decrypt on CMK | ✅ | Key policy must grant Macie SLR | — | Macie + SSE-KMS key policy |
| 1306 | D1 | Flow Logs show IP but unknown domain — which log reveals domain? | C: Resolver query logging | ✅ | Flow Logs lose domain after DNS resolves | — | Resolver query logging for domain visibility |
| 1307 | D1 | Security Hub non-compliant, want auto-remediate — where configure? | B: Config rule auto-remediation | ✅ | SH = dashboard only, Config = remediation | — | Security Hub vs Config remediation |
| 1308 | D1 | CW Logs data protection masks PII, compliance officer needs raw — permission? | B: logs:Unmask | ✅ | Specific permission for unmasked access | — | CW Logs data protection + Unmask |
| 1309 | D1 | StopLogging: EventBridge fires 2s, Config detects when? | A: Immediately | ❌ | B: 1-10 minutes (Config has inherent latency) | — | EventBridge=seconds, Config=minutes |
| 1310 | D1 | GD S3 Protection flags same-org account anomaly — fires? | B: Yes, behavioral regardless of org | ✅ | Org membership irrelevant for behavioral detection | Q568 | GuardDuty S3 Protection behavioral |
| 1311 | D6 | Config proactive, dev runs `aws cf create-stack` from CLI — catches? | B: Yes, CF service level | ✅ | Any CF deploy (CLI/Console/SDK) gets evaluated | Q1220 | Config proactive = CF service level |
| 1312 | D1 | Detect DeleteDetector 30s, org trail exists — approach? | C: EventBridge in management account | ✅ | Seconds = EventBridge. Config = minutes. | Q474 | EventBridge for API call detection |
| 1313 | D6 | CT Account Factory new account in Prod OU — which TWO auto-apply? | D+A (SH standards + SCP) | ❌ | A+B: SCP + org conformance pack. SH standards = per-account config, not OU-level. | — | SCP + conformance pack = OU-level auto-apply |
| 1314 | D1 | No GD finding, suspect C2, "what else IP talked to 7 days" — tool? | D: Security Hub | ❌ | B: CW Logs Insights (no finding = no Detective, open-ended query) | Q1277 | Detective needs finding. No finding = CW Logs Insights |
| 1315 | D1 | After custom threat list added, GD finding exists — deep investigation? | B: Detective | ✅ | Finding exists = Detective entry point | — | Detective for investigation |
| 1316 | D6 | SCP denies CreateDBInstance without DeletionProtection, Terraform (CF) deploys without it — result? | B: CF stack fails (SCP denies API) | ✅ | SCP evaluates actual API call regardless of trigger | — | SCP = catches ALL deployment paths |
| 1317 | D1 | Macie automated discovery 30d, only 5/200 buckets have findings — why? | A: Automated = sampling, create job for full | ✅ | Automated ≠ exhaustive. Job = full coverage. | Q1293 | Macie enabled ≠ Macie scanning |
| 1318 | D6 | Developer creates S3 via CLI (no CF). cfn-guard + Config proactive + SCP + Config detective — which fire? | B: SCP + Config detective | ✅ | CLI direct = no CF = cfn-guard and proactive irrelevant | — | CLI/Console direct = only SCP + Config detective |
| 1319 | D1 | Trojan:EC2/DNSDataExfiltration — block at DNS layer? | B: DNS Firewall | ✅ | Exfil in DNS query itself. Block resolution = channel dead. | — | DNS exfil = DNS Firewall blocks |


### Session 108 — 2026-06-23

**Domains:** D1 Detection · D2 Incident Response · D3 Infrastructure · D4 IAM · D5 Data Protection · D6 Governance (Red-priority kill drill — all 48 red areas)
**Score:** 24 ✅ · 0 ⚠️ · 1 ❌ (96% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1320 | D1/D5 | SSE-KMS, CISO wants to know if external downloads, no custom infra, least overhead? | B: GuardDuty S3 Protection | ✅ | "Anomalous" + "zero infra" = GuardDuty S3 Protection | Q100, Q546, Q568, Q581 | Detect vs prevent (GuardDuty vs policy) |
| 1321 | D1 | Alert 60s on iam:DeactivateMFADevice, org trail exists, least overhead? | C: EventBridge in management account | ✅ | "Specific API" + "60 seconds" + "org trail" = EventBridge | Q474, Q549, Q570 | EventBridge for API call detection |
| 1322 | D4/D5 | Cross-account KMS, key policy only grants Account A root, Account B Lambda AccessDenied — fix? | B: Key policy must grant Account B | ✅ | Root enables delegation same-account only | Q541, Q669, Q850 | Cross-account KMS key policy must name external account |
| 1323 | D1 | EC2 DNS query to mining pool, no TCP connection — ThreatPurpose? | B: Impact | ✅ | DNS query only = always Impact | Q116, Q142, Q154, Q155 | GuardDuty finding types |
| 1324 | D2 | Trojan C2Activity, capture processes+network+kernel, no interruption — action? | C: No-reboot AMI | ✅ | Volatile memory capture without stopping instance | Q810, Q825, Q830, Q933 | No-reboot AMI for volatile memory |
| 1325 | D1 | StopLogging called, CW metric filter didn't fire — why? | C: StopLogging kills own CW Logs delivery | ✅ | EventBridge receives directly, CW Logs doesn't | Q860, Q866, Q1092, Q1256 | StopLogging kills own CW Logs delivery |
| 1326 | D3 | Network Firewall TLS inspection, cert warnings — fix? | B: Distribute private CA to client trust stores | ✅ | MITM pattern = private CA, not public | Q35, Q87, Q152 | Network Firewall TLS inspection |
| 1327 | D1 | Two findings 15min apart: DNS to mining pool then TCP port 3333 — ThreatPurpose? | B: Impact then CryptoCurrency | ✅ | DNS=Impact, active TCP to mining=CryptoCurrency | Q178, Q226, Q489 | GuardDuty finding types (Impact vs CryptoCurrency) |
| 1328 | D4/D5 | Key policy grants root only, Lambda has s3:GetObject (no kms:Decrypt) — SSE-KMS read? | B: Fails — needs explicit kms:Decrypt | ✅ | Root = delegation not grant | Q264, Q503, Q687 | KMS key policy root = delegation, not grant |
| 1329 | D6 | DNS FW rule groups: available to 200 accounts + auto-associate all VPCs — which TWO? | A+D (RAM + Config) | ❌ | A+B: RAM shares + FM enforces association | Q313, Q441, Q562 | RAM for sharing vs FM for enforcing |
| 1330 | D5 | Default encryption CMK + bucket policy Deny if wrong key header, upload without flags — result? | B: Denied — policy evaluates before default encryption | ✅ | Policy checks headers as-received | Q426, Q626, Q643 | Default encryption vs bucket policy Deny |
| 1331 | D4/D5 | SCP denies kms:Decrypt unless ViaService=s3, direct CLI kms:decrypt — result? | B: Fails — no ViaService context, Deny fires | ✅ | Direct call = no ViaService | Q488, Q495 | kms:ViaService + SCP |
| 1332 | D1 | EC2 communicating with C2 IP, finding generated, zero code/infra/rules — service? | C: GuardDuty | ✅ | "Zero code + zero infra" = always GuardDuty | Q571, Q584, Q633 | Detect C2 = GuardDuty (zero code) |
| 1333 | D5/D6 | Config remediation enables S3 logging, PutBucketLogging succeeds, no logs appear — missing? | B: s3:GetBucketAcl (ACL validation) | ✅ | S3 access logging = ACLs (legacy) | Q864, Q868, Q903 | S3 server access logging = ACLs |
| 1334 | D4 | 50 customers/month need kms:Decrypt, key policy at 28KB — mechanism? | B: KMS Grants | ✅ | Grants scale without policy edits, RAM doesn't support KMS | Q11, Q37 | RAM vs KMS Grants |
| 1335 | D4/D5 | Cross-account S3+KMS, key policy grants B root, B SCP denies kms:* — result? | B: Fails — SCP follows caller | ✅ | SCP can't be bypassed by key policy | Q70, Q256 | Cross-account KMS + SCP evaluation |
| 1336 | D4 | Identity s3:*, session Get+Put only, same-account bucket policy grants Delete to session — result? | B: Allowed — same-account bypass | ✅ | Resource-based naming session bypasses ceiling (same-account only) | Q96, Q169 | Session policy bypass by resource-based policy |
| 1337 | D3/D4 | Guarantee NO EC2 without IMDSv2, preventive not detective, org-wide — approach? | B: SCP denying RunInstances unless MetadataHttpTokens=required | ✅ | "Preventive" + "never exist" = SCP | Q261, Q413 | SCP for preventive enforcement |
| 1338 | D4/D6 | Block external IN + block insider OUT — which TWO? | A+B: RCP + SCP with ResourceAccount | ✅ | RCP=inbound, SCP=outbound, full perimeter | Q398, Q1095 | Data perimeter (RCP blocks IN, SCP blocks OUT) |
| 1339 | D6 | Deploy Inspector 250 accounts, auto for new — approach? | B: Delegated admin + auto-enable | ✅ | Native org support = use native | Q483, Q492 | Native org-wide deployment |
| 1340 | D1/D4 | RCP blocks external, 500 denied GetObjects, AA + GD enabled — which true? | B: Only Access Analyzer fires | ✅ | AA=static policy, GD=needs successful access | Q534, Q594 | GuardDuty ≠ failed attempts |
| 1341 | D3/D5 | Gateway endpoint allows Get+Put only, Lambda calls ListBucket — result? | B: Access Denied (not in endpoint policy) | ✅ | Endpoint policy = explicit allowlist | Q535, Q1080 | Gateway endpoint policy as additional gate |
| 1342 | D4/D6 | RCP denies non-org s3:*, Lambda writes to PARTNER bucket — blocked? | B: No — partner's bucket not your resource | ✅ | RCP protects YOUR resources only | Q683, Q698 | RCP scope (your resources only, not outbound) |
| 1343 | D2 | Keys on GitHub, attacker created 2nd keys + console + EC2 — single containment? | C: Deny * on IAM user | ✅ | Blocks all paths (both keys, console, sessions) | Q862, Q867 | Credential leak IR (Deny-all before investigate) |
| 1344 | D5/D3 | Kinesis consumer Access Denied, has GetRecords — missing TWO? | A+C: kms:Decrypt + kms:DescribeKey | ✅ | Consumer = Decrypt + DescribeKey | Q879, Q1100 | Kinesis consumer = Decrypt + DescribeKey |

---
**Session 108 continued — Red priorities #19-48 + D5 uplift (24 more questions)**

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
|---|---|---|---|---|---|---|---|
| 1345 | D5 | Glacier Vault Lock: 10yr, permanently irreversible after 24hr confirm — approach? | B: Glacier Vault Lock | ✅ | "24hr confirm + permanently irreversible" = Vault Lock | Q800, Q822 | Glacier Vault Lock vs Object Lock |
| 1346 | D5 | Asymmetric KMS sign, air-gapped partners verify — how? | B: Download public key, verify locally OpenSSL | ✅ | Sign=private, verify=public, offline OK | Q812, Q824 | Sign=private, verify=public |
| 1347 | D1/D5 | S3 Access Grants: All-Employees root prefix READ, engineer reads /hr/ — cause? | B: Root prefix includes everything | ✅ | Prefix overlap = #1 misconfiguration | Q819, Q826 | S3 Access Grants prefix overlap |
| 1348 | D5/D3 | Lambda private subnet, Kinesis+KMS endpoints exist, GetRecords timeout, SM works — fix TWO? | A+D: Kinesis endpoint SG inbound + Lambda SG outbound | ✅ (partial round 2, full here) | Interface endpoint = TWO SGs cooperate | Q918, Q950 | Kinesis + KMS VPC endpoints (timeout = network) |
| 1349 | D3 | API GW mTLS on default execute-api endpoint — result? | C: Can't enable, needs custom domain | ✅ | mTLS = custom domain + S3 truststore only | Q967, Q1012 | API Gateway mTLS = custom domain + S3 truststore |
| 1350 | D5 | EMR inter-node, engineer proposes Nitro C6i — why insufficient? | B: EMR needs explicit security config + PEM certs | ✅ | Nitro is implicit, compliance needs auditable config | Q1030, Q1073 | EMR in-transit = security config + PEM certs |
| 1351 | D3/D5 | IoT revocation + API GW mTLS revocation — mechanisms? | B: IoT=INACTIVE in registry, API GW=CRL in S3 truststore | ✅ | Two different mechanisms | Q1032, Q1070 | IoT revocation = registry. API GW mTLS = CRL |
| 1352 | D1/D3 | State Manager CIS on boot + every 2hr — minimum config? | B: ONE association with OnBoot + rate(2hr) | ✅ | Dual triggers on single association | Q1048, Q1071 | State Manager OnBoot + schedule (dual triggers) |
| 1353 | D3 | Inspector SBOM weekly to S3 — which TWO? | B+C: EventBridge+Lambda + bucket policy for inspector2 | ✅ | No built-in scheduler, on-demand API | Q1059, Q1119 | Inspector SBOM = native export + bucket policy |
| 1354 | D6 | cfn-guard bypassed via Console, catch ALL CF deploys — mechanism? | A: SCP | ❌ | D: Both Config proactive and CF Hook work (CF service-level) | Q1220, Q1271 | cfn-guard bypassable vs Config proactive |
| 1355 | D3 | Public HTTPS + SSH from bastion — SG rules TWO? | B+D: 443 from 0.0.0.0/0 + 22 from bastion CIDR | ✅ | Public-facing = 0.0.0.0/0 on 443 | Q1239, Q1250 | Public-facing = 0.0.0.0/0 on 443 |
| 1356 | D5/D3 | Rotation Lambda succeeds in SM but new app gets auth failed on RDS — cause? | B: Lambda SG can't reach RDS SG | ✅ | Rotation Lambda network → DB = SG issue | Q1242, Q1254 | Rotation Lambda can't reach DB = SG issue |
| 1357 | D6 | Security Hub setup order? | B: Enable → Designate → Members → Access | ✅ | E-D-M-A | Q1244, Q1273 | Security Hub setup ordering (E-D-M-A) |
| 1358 | D1 | No GD finding, suspect lateral movement, query all IPs over 7d — tool? | B: CW Logs Insights | ✅ | No finding = no Detective entry point | Q1277, Q1314 | Detective needs finding. No finding = CW Logs Insights |
| 1359 | D1 | Active threat from unusual IP, zero code — service? | C: GuardDuty | ✅ | "Happening now" + "zero code" = GuardDuty | Q187, Q233 | Detect vs prevent (GuardDuty vs Access Analyzer) |
| 1360 | D6 | Self-service RDS, dev has no rds:CreateDBInstance — how? | B: Service Catalog launch constraint role | ✅ | Launch constraint = SC assumes role | Q274, Q277 | Service Catalog (self-service) |
| 1361 | D6 | StackSets deployed Config, admin stops recorder — what happens? | B: Nothing — StackSets no auto-remediation | ✅ | StackSets = deploy and forget | Q283, Q439 | StackSets no auto-remediation |
| 1362 | D6 | FM WAF policy, developer disassociates Web ACL — what happens? | B: FM re-associates automatically | ✅ | FM auto-remediates | Q284, Q435 | Firewall Manager auto-remediation |
| 1363 | D4 | Unused permissions 90d + generate replacement — service? | B: Access Analyzer unused + policy generation | ✅ | Two features, one service | Q374, Q1003 | Access Analyzer unused + policy generation |
| 1364 | D1/D4 | Bucket policy grants external, no access yet, AA+GD — both fire? | C: Both fire (AA=policy, GD=after actual access) | ✅ | AA=static, GD=needs successful access | Q518, Q652 | Access Analyzer + GuardDuty both fire |
| 1365 | D4/D5 | Session policy=GetObject only, same-account SSE-KMS read — succeeds? | B: Succeeds — server-side KMS not gated by session policy | ✅ | Session policy gates direct calls only | Q591, Q679 | Session policy + server-side KMS |
| 1366 | D1/D4 | RCP blocks external, AA+GD enabled, no access, bucket policy unchanged — which TWO true? | A+D: AA fires (static) + GD doesn't fire (no access) | ✅ | AA reads policy, GD needs behavior | Q706, Q1260 | Access Analyzer static + GuardDuty ≠ failed attempts |
| 1367 | D6 | RAM shares NF policy, FM enforces, admin deletes endpoint — what happens? | A+B: RAM + FM auto-recreates | ✅ | RAM shares, FM enforces lifecycle | Q313, Q441 | RAM for sharing vs FM for enforcing |
| 1368 | D5 | CRR custom context "Engineering", dest key expects "Finance" — result? | B: Fails — context preserved, mismatch | ✅ | CRR preserves source custom context | Q923 | CRR custom encryption context preserved |
| 1369 | D5 | S3 Batch job us-east-1, target bucket us-west-2 — result? | B: Fails — Batch is regional | ✅ | Job + manifest + target = same region | Q872 | S3 Batch Operations regional |
| 1370 | D5 | Object Lock: most users can't delete 5yr, CLO can release early — config? | B: Governance mode + BypassGovernanceRetention for CLO | ✅ | "Someone CAN override" = Governance | Q800, Q822 | Object Lock Governance vs Compliance |
| 1371 | D5 | EBS encryption by default — TWO gaps? | A+D: Per-region + new accounts don't inherit | ❌ | A+D correct. Picked A+C (C wrong: can't override) | Q902 | EBS encryption by default + SCP |
| 1372 | D5 | Imported key rotation — procedure? | B: New key EXTERNAL + import + alias swap | ✅ | No auto/on-demand rotation for imported | — | Imported key rotation procedure |
| 1373 | D5 | Global Table MRK, eu-west-1 reads fail, us-east-1 key policy correct — cause? | B: Replica key policy independent, missing DynamoDB grant | ✅ | MRK policies independent per region | Q84 | MRK independent key policies |
| 1374 | D5 | CW Logs PHI masking + compliance officer raw access + audit trail — THREE? | A+B+C: Data protection + logs:Unmask + CloudTrail | ✅ | Three layers for three requirements | — | CW Logs data masking + Unmask |
| 1375 | D5 | Parameter Store SecureString CMK, has ssm:GetParameter, Access Denied — missing? | B: kms:Decrypt on CMK | ✅ | Customer-managed = explicit Decrypt | — | Parameter Store + kms:Decrypt |
| 1376 | D5 | Daily EBS snapshots + 30d retention + cross-region + auto-delete DR — service? | B: DLM | ✅ | All native in one policy | — | DLM cross-region |
| 1377 | D5 | SM replication, source uses single-region CMK — works? | B: Yes — SM re-encrypts with dest key | ✅ | MRK not required for SM replication | Q428 | Secrets Manager replication ≠ MRK |
| 1378 | D6 | Deploy Inspector 250 accounts, auto new — approach? | B: Delegated admin + auto-enable | ✅ | Native org support | Q483, Q492 | Native org-wide deployment |
| 1379 | D1 | 200 accounts, CIS + FSBP + aggregate GD+Inspector — least overhead? | B: Security Hub org-wide | ✅ | Dashboard + standards + aggregation | Q5, Q24 | Security services comparison |
