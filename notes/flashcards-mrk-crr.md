# Multi-Region Key (MRK) + S3 CRR — Flashcard

> Diagram: [mrk-crr-flow.png](../diagrams/mrk-crr-flow.png)
> Failed: Q84, Q123, Q165, Q322, Q373, Q399, Q493. Lock this.

---

## What Is MRK?

```
One key → replicated across regions → SAME key ID + SAME material

us-east-1: mrk-abc-123 → Material X → Key Policy A
us-west-1: mrk-abc-123 → Material X → Key Policy B (INDEPENDENT!)
            ^^^^^^^^^^^    ^^^^^^^^^
            SAME ID        SAME bits   → encrypt here, decrypt there
```

---

## MRK + S3 CRR — How It Works

```
1. Create MRK primary in us-east-1
2. Replicate MRK to us-west-1 (same material, independent policy)
3. S3 CRR configured: source → dest
4. Replication role needs:
     kms:Decrypt on mrk-abc-123 in us-east-1 (read source)
     kms:GenerateDataKey on mrk-abc-123 in us-west-1 (write dest)

CRR process (S3 handles internally):
  Decrypt source → transfer plaintext → re-encrypt at dest (same key material)

App in us-west-1:
  Calls kms:Decrypt on mrk-abc-123 LOCALLY (no cross-region call)
```

---

## SAME vs INDEPENDENT

| SAME across regions | INDEPENDENT per region |
|---|---|
| Key ID (mrk-...) | Key policy |
| Key material (crypto bits) | Grants |
| Key spec (SYMMETRIC_DEFAULT) | Aliases |
| | Tags |
| | Enable/disable state |

---

## Quick Recall

```
Q: "Same key in both regions" → which key type?
A: MRK (Multi-Region Key)

Q: Updated primary key policy, replica still denies. Why?
A: Policies are INDEPENDENT. Must update replica separately.

Q: MRK required for S3 CRR?
A: NO — separate CMKs also work (S3 re-encrypts). MRK only required
   when question says "SAME key in both regions."

Q: MRK required for Secrets Manager replication?
A: NO — SM re-encrypts with any dest key. MRK is optional optimization.

Q: MRK required for DynamoDB Global Tables?
A: YES — Global Tables need same key material for local reads.

Q: How to identify MRK vs regular key?
A: Key ID prefix "mrk-" = Multi-Region Key.

Q: Can imported key material be MRK?
A: NO — imported keys are single-region only.

Q: Can AWS managed keys (aws/s3) be MRK?
A: NO — AWS managed keys are single-region only.
```

---

## When MRK Is REQUIRED vs OPTIONAL

| Scenario | MRK Required? | Why |
|---|---|---|
| DynamoDB Global Tables + SSE-KMS | ✅ YES | Local reads need local key with same material |
| S3 CRR + "same key both regions" | ✅ YES | Question explicitly demands it |
| S3 CRR (no "same key" requirement) | ❌ NO | Separate CMKs work fine |
| Secrets Manager replication | ❌ NO | SM re-encrypts with any dest key |
| EBS snapshot cross-region copy | ❌ NO | Re-encrypts with dest key |
| RDS cross-region replica | ❌ NO | Re-encrypts with dest key |

**Rule:** "Same key in both regions" or "DynamoDB Global Tables" = MRK. Everything else = optional.

---

## 🧠 Exam One-Liners

- **"Same key in both regions" = MRK. Always.**
- **MRK = same key ID + same material + INDEPENDENT policies per region.**
- **DynamoDB Global Tables = ONLY service that REQUIRES MRK.** Everything else re-encrypts.
- **"mrk-" prefix in key ID = Multi-Region Key.**
- **Imported keys and AWS managed keys CANNOT be MRK.**
- **Updated primary policy ≠ updated replica policy. Each region is independent.**
