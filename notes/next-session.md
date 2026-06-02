# Next Session — FINAL RE-TEST

> Session 68: 7/10 (70%). Three errors need re-test.

---

## Re-Test Targets (3 questions)

### 1. Session policy + server-side KMS (Q679)
- Pattern: Session policy gates caller's DIRECT calls only. S3's internal KMS call is server-side — not gated.
- Trap: "session policy doesn't include kms:Decrypt" sounds right but misses the server-side distinction.
- Count: 3rd miss on this pattern (Q591, Q679)

### 2. RCP scope — your resources only, not outbound (Q683)
- Pattern: RCP protects YOUR resources (inbound). Outbound to external resources = SCP's job.
- Trap: SLR exemption is TRUE but irrelevant when target resource isn't yours.
- Count: New concept — first encounter.

### 3. VPC endpoints — direct KMS + DynamoDB (Q685)
- Pattern: S3 SSE-KMS = server-side (no KMS endpoint). Direct kms:Decrypt in code = needs KMS endpoint. DynamoDB = separate Gateway endpoint.
- Trap: Easy to miss DynamoDB as a separate endpoint requirement.
- Count: First miss with all 4 together.

---

## Status: RE-TEST THEN BOOK EXAM

### Post-Re-Test
If 3/3 pass → exam ready. Book it.
If any miss → one more targeted drill on that specific pattern.
