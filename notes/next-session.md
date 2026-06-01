# Next Session — Final Leaks Drill

> Goal: 100% on the two remaining leaks. Then book the exam.

---

## Priority 1: GuardDuty finding types (C2 = Trojan, NOT CryptoCurrency)

**The rule:**
- DNS query to ANY malicious domain → Impact (always)
- Active TCP to **mining pool** → CryptoCurrency
- Active TCP to **C2 server** → Trojan

**Leak:** Q655 — said CryptoCurrency for C2 domain TCP connection. Must be Trojan.

**Drill:** 3 questions mixing C2 vs mining pool destinations with novel phrasing.

---

## Priority 2: Cross-account KMS key policy must name external account

**The rule:**
- Root in key policy enables IAM delegation **same-account only**
- Cross-account KMS: key policy MUST explicitly grant Account B's root or role
- RCP never grants access — it only restricts. Same-org doesn't change this.

**Leak:** Q669 — said "RCP same-org overrides" key policy requirement. Wrong.

**Drill:** 3 questions on cross-account KMS key policy requirement with novel scenarios.

---

## Format

- 6 questions total
- Killer difficulty
- Pass criteria: 6/6 = dominated. Book the exam.
- If <6/6: drill 3 more on the leaked pattern.
