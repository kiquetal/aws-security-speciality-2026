# FAQ: Glacier Vault Lock vs S3 Object Lock

> **Blueprint ref:** Task 5.2 (data integrity, lifecycle)
> **Exam trap frequency:** HIGH — failed 2 times (Q800, Q822)

---

## One-Sentence Definitions

- **S3 Object Lock** = Per-OBJECT retention period. Auto-expires. Applied per object or as bucket default.
- **Glacier Vault Lock** = Per-VAULT immutable POLICY. Permanent once confirmed. Applied to entire vault.

---

## Decision Matrix

| Exam Signal | Answer |
|---|---|
| "Fixed retention period (3yr/5yr/7yr), auto-expires after" | **S3 Object Lock Compliance** |
| "Root can't delete during retention" | **S3 Object Lock Compliance** |
| "24-hour confirm window, then permanently irreversible" | **Glacier Vault Lock** |
| "Even AWS Support can't modify after confirmation" | **Glacier Vault Lock** |
| "Policy-level WORM (applies to entire vault)" | **Glacier Vault Lock** |
| "Per-object, different retention per object" | **S3 Object Lock** |
| "Indefinite hold for litigation, no expiry" | **S3 Object Lock Legal Hold** |

---

## Side-by-Side Comparison

| Dimension | S3 Object Lock (Compliance) | S3 Object Lock (Governance) | Glacier Vault Lock |
|---|---|---|---|
| **Scope** | Per-object | Per-object | Per-vault (policy) |
| **Retention** | Fixed period, auto-expires | Fixed period, overridable | N/A — policy is permanent |
| **Root can delete?** | ❌ No | ✅ With permission | ❌ No (after confirm) |
| **AWS Support can override?** | ❌ No | ✅ Yes | ❌ No |
| **Reversible?** | After expiry | Anytime with permission | ❌ NEVER (once confirmed) |
| **Confirm window?** | No | No | ✅ 24 hours to test |
| **Use case** | Compliance retention (SEC 17a-4) | Soft protection (dev teams) | Audit vault policies forever |
| **Requires versioning?** | ✅ Yes | ✅ Yes | N/A (Glacier) |

---

## Vault Lock Lifecycle

```
1. Initiate Lock → Policy enters "InProgress" state
2. 24-hour window → TEST the policy (validate it works)
3. Complete Lock → Policy is PERMANENT. Cannot be:
   - Modified
   - Deleted
   - Overridden by root
   - Changed by AWS Support
   Forever. No undo. Period.
```

If you DON'T complete within 24 hours → lock expires, start over.

---

## Legal Hold (Third Option)

| Dimension | Legal Hold | Compliance Mode |
|---|---|---|
| **Expiry** | NONE — indefinite until manually removed | Fixed period |
| **Who removes?** | User with `s3:PutObjectLegalHold` permission | Nobody (waits for expiry) |
| **Use case** | Litigation preservation | Regulatory retention |
| **Combines with retention?** | ✅ Yes (both can be active) | N/A |

---

## Exam Traps

| Trap | Truth |
|---|---|
| "WORM for 7 years" → Vault Lock | ❌ Probably Object Lock Compliance (has expiry). Vault Lock = permanent POLICY, no retention period. |
| "Permanently irreversible after confirm" | ✅ Vault Lock (the 24hr confirm is the giveaway) |
| "Root can't delete" | Could be EITHER — Compliance mode OR Vault Lock. Read for "confirm window" or "policy-level" to differentiate. |
| "Auto-delete after retention" | ✅ Object Lock (has lifecycle). Vault Lock policies don't auto-delete. |

---

## 🧠 Cheat-Sheet One-Liners

- "24hr confirm + permanently irreversible POLICY" = Glacier Vault Lock. "Fixed retention per OBJECT, auto-expires" = Object Lock Compliance.
- Vault Lock = policy forever. Object Lock = object with expiry. Legal Hold = object without expiry.
- "Root can't delete" alone isn't enough — both Compliance mode AND Vault Lock satisfy this. Look for "confirm window" (Vault Lock) or "auto-expire after X years" (Object Lock).
