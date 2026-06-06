# Next Session — 2026-06-06

## Priority: Re-test Dojo Gaps + AD/VPN Lock-in

### Part 1: AD + VPN recall drill (SHORT DRILL mode)
- AWS Managed AD vs AD Connector vs Simple AD (capabilities, trusts, RDS SQL)
- Trust direction (one-way: who trusts whom)
- Client VPN vs Site-to-Site VPN vs Verified Access
- Why AD Connector can't do RDS SQL auth (no local DC)

### Part 2: Dojo wrong answers re-test (EXAM FORMAT)
Target the 27 wrong questions from Dojo exam. Focus on:
1. AD/Directory Service — trust directions, ADFS federation (Q5, Q48)
2. Operational troubleshooting — agent logs, NACL ephemeral ports, metric filters (Q13, Q19, Q22, Q25, Q57, Q61, Q63)
3. KMS Grants vs key policies (Q47)
4. IoT Core — thing policy variables (Q30)
5. VPN types — SSL VPN vs IPsec (Q56)
6. S3 encryption matrix — SSE-S3 vs SSE-KMS vs SSE-C vs client-side (Q17)
7. GuardDuty master/member permissions (Q10, Q22)
8. CloudTrail config — management events Write-only/All for EventBridge (Q16)
9. Storage tier traps — Glacier Deep Archive vs S3 Standard (Q65)
10. SQS resource policy troubleshooting (Q12)
11. ENI/ALB target registration (Q29)
12. Kinesis + OpenSearch combo (Q41)
13. ACM cert region requirements for CF+ALB (Q43)
14. IAM policy interpretation — Resource:* implications (Q38)
15. Secrets Manager in CloudFormation (Q50)
16. Disable instance metadata (Q55)
17. CloudTrail multi-account troubleshooting (Q9, Q52)

### Question count: 10 exam-format questions covering top gaps
