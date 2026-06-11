# Pearson SCS-C02 Practice Exam — Review

> Date: 2026-06-11
> Source: O'Reilly / Pearson (SCS-C02 format)
> Score: **48/65 (~74%)**

---

## Domain Breakdown

| Domain | Score | Correct | Total | Status |
|---|---|---|---|---|
| Data Protection | 77.78% | 7 | 9 | 🟡 |
| Authentication for AWS resources | 100% | 3 | 3 | 🟢 |
| Exam Overview and Preparation | 66.67% | 6 | 9 | 🟡 |
| Identity and Access Management | 77.78% | 7 | 9 | 🟡 |
| Infrastructure Security | 77.78% | 7 | 9 | 🟡 |
| Management and Security Governance | 55.56% | 5 | 9 | 🔴 |
| Monitoring and Reporting | 0% | 0 | 1 | 🔴 |
| Security Logging and Monitoring | 87.5% | 7 | 8 | 🟢 |
| Threat Detection and Incident Response | 75% | 6 | 8 | 🟡 |

---

## Questions Got WRONG

### Cryptography / Data Protection
| Topic | Your Answer | Correct Answer | Lesson |
|---|---|---|---|
| Private key encrypts, public key decrypts — what does it guarantee? | Data confidentiality | **Data integrity and non-repudiation** | Private→Public = signing (verify sender). Public→Private = encryption (confidentiality). |

### CloudTrail / Logging Delivery
| Topic | Your Answer | Correct Answer | Lesson |
|---|---|---|---|
| Why is IAM role not required for CloudTrail cross-account delivery? | Bucket policies are used | **CloudTrail doesn't support IAM roles for cross-account delivery** | Root cause (doesn't support) vs consequence (uses bucket policy instead). |
| Which log source uses IAM role for ALL delivery targets? | CloudTrail | **VPC Flow Logs** | VPC Flow Logs = IAM role for S3, CW Logs, Kinesis. CloudTrail uses bucket policy for S3. |
| Route 53 Resolver → CW Logs delivery permission? | IAM role | **Log group resource policy** | R53 Resolver uses resource policy on CW Log Group (grants route53resolver.amazonaws.com). |

### Exam Domain Weights (C02-specific)
| Topic | Your Answer | Correct Answer | Lesson |
|---|---|---|---|
| Largest domain in C02? | IAM (C03 answer) | **Infrastructure Security (26%)** | C02 weights differ from C03. Infra = 26% in C02, IAM = 20%. |
| Threat Detection + IR percentage? | (wrong) | **14%** | C02/C03 mixed question. As standalone domain = 14%. |

### IAM / Policy Evaluation
| Topic | Your Answer | Correct Answer | Lesson |
|---|---|---|---|
| Two types of managed identity policies? | AWS-managed + resource-based | **AWS-managed + customer-managed** | Resource-based = NOT identity policy. Inline = identity but NOT managed. |
| Resource policy names session ARN as principal — which policy to check? | Both identity + resource | **Resource policy only** | Resource policy naming principal directly = grants access alone (bypass rule). |

### Incident Response
| Topic | Your Answer | Correct Answer | Lesson |
|---|---|---|---|
| Establish normal behavior baselines — which IR phase? | Preparation | **Detection and Analysis** | Baselines = how you detect anomalies. "Set up tools" = Preparation. "Know what's normal" = Detection. |

### Infrastructure / Networking
| Topic | Your Answer | Correct Answer | Lesson |
|---|---|---|---|
| EC2 can't access S3 via interface endpoint — root cause? | NACLs and route tables | **Security group rules + host-based firewall** | Interface endpoint = ENI = SGs matter. Gateway endpoint = route table. Question said "interface." |

### Service Selection
| Topic | Your Answer | Correct Answer | Lesson |
|---|---|---|---|
| Data classification + identifying improper permissions? | GuardDuty | **Macie** | Speed error. "Data classification" = always Macie. |
| Free tier always available at low usage rate? | IAM | **S3** | IAM = completely free (no "tier"). S3 = free tier (5GB limit, then pay). |

### Governance / Control Tower
| Topic | Your Answer | Correct Answer | Lesson |
|---|---|---|---|
| Control Tower prerequisite? | Trusted access enabled for Config/CloudTrail | **STS enabled in all regions** | CT sets up Config/CloudTrail itself — existing trusted access must be DISABLED first. |

---

## Key Rules Learned

### Delivery Mechanisms by Service
```
VPC Flow Logs → ALL targets = IAM role (only service that does this)
CloudTrail → S3 = bucket policy (service principal)
CloudTrail → CW Logs = IAM role
Route 53 Resolver → CW Logs = log group resource policy
Route 53 Resolver → S3 = bucket policy
Route 53 Resolver → Kinesis = IAM role
```

### Asymmetric Key Direction
```
Private key encrypts → Public decrypts = SIGNING (integrity + non-repudiation)
Public key encrypts → Private decrypts = ENCRYPTION (confidentiality)
```

### Control Tower Prerequisites
```
✅ STS enabled in all regions
✅ IAM Identity Center enabled (same region)
❌ DISABLE existing trusted access for Config/CloudTrail (CT manages these)
❌ No existing Config recorder in management account
```

### Interface vs Gateway Endpoint Troubleshooting
```
Gateway (S3/DynamoDB) → check: route table + NACL + endpoint policy
Interface (everything else) → check: SG + host firewall + DNS + endpoint policy
```

### IR Phase Keywords
```
Preparation = tools, runbooks, access, training
Detection and Analysis = baselines, thresholds, anomalies, correlation
Containment = isolate (SG), preserve (snapshot), eradicate
Post-Incident = lessons learned, update runbooks
```
