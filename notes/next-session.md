# Next Session — DOJO EXAM

> Session 71: 4/5 (80%). RCP scope LOCKED IN. One remaining leak.

---

## Remaining Leak (1 pattern)

### 1. Access Analyzer static + GuardDuty ≠ failed attempts (Q518, Q534, Q594, Q652, Q706)
- Pattern: AA = static policy analysis (fires on policy text). GD = dynamic (needs successful anomalous access).
- Trap: Picking contradictory options (A+C) under speed pressure.
- Count: 5th appearance of this pattern across sessions.
- Rule: "AA reads the POLICY. GD reads the TRAFFIC. Blocked traffic = no GD finding."

---

## Status: DOJO EXAM THEN BOOK

### Passed patterns (locked in):
- Session policy + server-side KMS ✅
- VPC endpoints direct KMS + DynamoDB ✅
- EventBridge + GuardDuty S3 + SCP mapping ✅
- Full 5-layer cross-account evaluation ✅
- RCP scope (your resources only, not outbound) ✅ (3/3 in Session 71)
- RCP same-org evaluation ✅
- Data perimeter (RCP IN, SCP OUT) ✅

### Next action:
1. Take Dojo practice exam (timed, 65 questions)
2. Bring back wrong answers for targeted drill
3. If Dojo score >= 75% → book exam
