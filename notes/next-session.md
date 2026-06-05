# Next Session — DOJO EXAM

> Session 70: 4/5 (80%). One remaining leak.

---

## Remaining Leak (1 pattern)

### 1. RCP scope — your resources only, not outbound (Q683, Q698)
- Pattern: RCP protects YOUR resources (inbound). Outbound to external resources = SCP's job.
- Trap: SLR exemption is TRUE but irrelevant when target resource isn't yours.
- Count: 2nd miss on this pattern.
- Rule: "RCP = shield on YOUR castle walls. Doesn't follow soldiers to other castles."

---

## Status: DOJO EXAM THEN BOOK

### Passed patterns (locked in):
- Session policy + server-side KMS (Q697, Q700) ✅
- VPC endpoints direct KMS + DynamoDB (Q699) ✅
- EventBridge + GuardDuty S3 + SCP mapping (Q701) ✅
- Full 5-layer cross-account evaluation (Q700) ✅

### Next action:
1. Take Dojo practice exam (timed, 65 questions)
2. Bring back wrong answers for targeted drill
3. If Dojo score >= 75% → book exam
