# Next Session — POST-DOJO TARGETED DRILL

> Dojo Score: 38/65 (58%). Need 75%+ to book exam.
> 27 misses clustered into 5 drillable categories.

---

## Drill Plan (Priority Order)

### Priority 1: Operational Troubleshooting (6 misses → 22% of errors)
- NACL stateless = inbound ACCEPT + outbound REJECT (Q19, Q61)
- CloudWatch metric filter: correct event name + metric value = 1 (Q57)
- CW Logs agent: /var/log/awslogs.log (runtime) not setup.log (Q63, Q13)
- ENI → SG mapping + ALB target registration (Q29)
- Ephemeral ports 1024-65535 on NACL outbound (Q61)

### Priority 2: S3 Encryption Selection (3 misses)
- SSE-S3 = AWS manages everything, no audit trail
- SSE-KMS = envelope encryption + audit trail + auto rotation
- SSE-C = you provide key each request, AWS encrypts server-side
- Client-side = you encrypt before upload, keys never in AWS
- Decision: "company manages keys + never in AWS" = client-side. "audit trail + rotation" = SSE-KMS. (Q17, Q42, Q65)

### Priority 3: AD/ADFS/Directory Service (2 misses)
- AWS Managed AD = full MS AD, supports trusts, separate domain
- Simple AD = Samba-based, NO trust capability
- AD Connector = proxy only, no domain in AWS
- One-way trust direction: "AWS trusts on-prem" = on-prem admins access AWS resources
- Federation: ADFS + IAM roles + AssumeRoleWithSAML (never IAM users/groups)
- (Q5, Q48)

### Priority 4: CloudTrail Configuration (3 misses)
- Management events must be Write-only or All for EventBridge rules to fire (Q16)
- Multi-account: bucket policy must list account IDs + s3:PutObject (not UploadPart) (Q9)
- Log file validation = detect tampering (SHA-256 digest). Encryption = prevent reading. (Q9)
- Requester Pays must be OFF for CloudTrail delivery (Q28 — got wrong)
- Log file prefix in bucket policy must match trail config (Q28)

### Priority 5: Service-Specific (4 misses)
- GuardDuty master/member: members can't archive findings, can't manage IP lists (Q10)
- KMS Grants = programmatic, per-app, revocable delegation (Q47)
- IoT Core: ThingName = trusted identity, ClientId = untrusted (Q30)
- Real-time logs: Kinesis (ingestion) + OpenSearch (analytics) (Q41)

---

## Execution Plan

1. Session A: Priority 1 + 2 (9 questions as killer drill)
2. Session B: Priority 3 + 4 + 5 (9 questions as killer drill)
3. Session C: Full 18-question mixed re-test (all 5 categories)
4. Re-take Dojo → target 75%+
5. If >= 75% → book exam

---

## Locked Patterns (do NOT re-test)
- RCP scope (your resources only, not outbound) ✅
- Session policy + server-side KMS ✅
- Full 5-layer cross-account evaluation ✅
- EventBridge + GuardDuty S3 + SCP mapping ✅
- Data perimeter (RCP IN, SCP OUT) ✅
- RCP same-org evaluation ✅
- RAM for sharing vs FM for enforcing ✅
- All D6 Governance patterns ✅ (100% on Dojo)
- All logging/monitoring patterns ✅ (100% on Dojo)
