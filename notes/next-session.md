# Next Session — Domination Drill

> Goal: 90%+ on every domain. Zero hesitation.

---

## Priority 1: D1 Detection (current ~82%, target 90%)

**Specific leaks:**
- "Detect anomalous data access / least overhead" → **GuardDuty S3 Protection** (NOT CloudTrail, NOT EventBridge)
- "Detect C2 with zero code / zero infra" → **GuardDuty** (NOT Network Firewall, NOT DNS Firewall)
- "Detect specific API call fast" → **EventBridge** (NOT GuardDuty, NOT Config)

**Drill:** 10 questions, cold, 90 seconds each. Mix all three patterns with novel phrasing.

---

## Priority 2: D5 Data Protection (current ~88%, target 90%)

**Specific leak:**
- SCP/bucket policy Deny evaluates request headers BEFORE default encryption applies
- No header sent + Deny checks for header → rejected (default encryption never fires)

**Drill:** 3 questions on evaluation order (SCP Deny + default encryption timing).

---

## Priority 3: D6 Governance (current ~85%, target 90%)

**Specific leak:**
- RAM shares vs FM enforces — under novel phrasing / time pressure
- Verb signals: "share/visible/accessible" = RAM. "enforce/associate/re-apply" = FM.

**Drill:** 5 questions mixing RAM/FM with novel wording (not the same scenarios seen before).

---

## Format

- All killer difficulty
- Zero warm-up (cold start)
- Timed: 90 seconds per question
- Total: ~18 questions
- Pass criteria: 17/18 (94%+) = dominated

---

## After passing this drill

If 17/18+: You dominate all 6 domains. Book the exam.
If <17/18: Identify which pattern leaked, drill 5 more on that pattern only.
