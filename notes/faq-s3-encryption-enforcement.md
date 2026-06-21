# FAQ: S3 Encryption Enforcement Patterns

> **Blueprint ref:** Task 5.2 (data at rest controls)
> **Exam trap frequency:** HIGH — failed 3 times (Q426, Q626, Q643)

---

## Three Mechanisms, Three Purposes

| Mechanism | What It Does | When It Evaluates |
|---|---|---|
| **Default Encryption** | Silently encrypts if caller sends NO encryption header | AFTER policy evaluation passes |
| **Bucket Policy Deny** | Rejects upload if header missing/wrong | BEFORE default encryption applies |
| **SCP Deny** | Rejects API call if header missing/wrong | BEFORE default encryption applies |

---

## The Critical Rule

```
┌─────────────────────────────────────────────────────────┐
│  POLICY EVALUATES THE REQUEST AS-RECEIVED               │
│  (headers the caller actually sent)                     │
│                                                         │
│  Default encryption applies AFTER policy passes         │
│  (fills in missing headers silently)                    │
│                                                         │
│  If policy checks for a header and caller didn't        │
│  send it → DENIED. Default encryption never fires.      │
└─────────────────────────────────────────────────────────┘
```

---

## Scenario Matrix (Exam-Critical)

| Scenario | Result | Why |
|---|---|---|
| Default encryption SSE-KMS + NO bucket policy + upload without header | ✅ Succeeds (encrypted by default) | No policy to check, default applies |
| Default encryption SSE-KMS + bucket policy Deny if header ≠ aws:kms + upload WITHOUT header | ❌ DENIED | Policy sees no header → Deny fires → default never runs |
| Default encryption SSE-KMS + bucket policy Deny if header ≠ aws:kms + upload WITH `x-amz-server-side-encryption: aws:kms` | ✅ Succeeds | Header present and matches → Deny condition FALSE |
| SCP Deny PutObject if KMS key header ≠ specific ARN + upload without header + default set | ❌ DENIED | SCP evaluates before default encryption |
| SCP Deny if header ≠ specific ARN + upload WITH correct ARN header | ✅ Succeeds | Header matches → StringNotEquals FALSE → Deny doesn't fire |

---

## Common Bucket Policy Pattern

```json
{
  "Sid": "DenyUnencryptedUploads",
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:PutObject",
  "Resource": "arn:aws:s3:::my-bucket/*",
  "Condition": {
    "StringNotEquals": {
      "s3:x-amz-server-side-encryption": "aws:kms"
    }
  }
}
```

⚠️ **This WILL reject uploads that rely on default encryption** (no header sent). Callers must explicitly include the header.

---

## When to Use Which

| Goal | Solution |
|---|---|
| "Safety net — encrypt everything even if caller forgets" | Default encryption alone (no policy) |
| "ENFORCE — reject non-compliant uploads" | Bucket policy Deny + default encryption together |
| "ORG-WIDE enforcement" | SCP Deny + account-level default encryption |
| "Specific CMK only, no other key allowed" | SCP/bucket policy with `StringNotEquals` on key ARN |

---

## Header Names (Exact)

| Header | Purpose |
|---|---|
| `x-amz-server-side-encryption` | Algorithm: `aws:kms` or `AES256` |
| `x-amz-server-side-encryption-aws-kms-key-id` | Specific KMS key ARN |
| `x-amz-server-side-encryption-context` | Base64 encryption context |

⚠️ NOT `x-amz-meta-*` (that's custom metadata, not encryption).

---

## 🧠 Cheat-Sheet One-Liners

- Default encryption = safety net (silent). Bucket policy Deny = enforcement (rejects). SCP = org-wide enforcement.
- Policy evaluates request AS-RECEIVED. Default encryption applies AFTER. Missing header + policy check = DENIED always.
- "Must use specific key" = StringNotEquals on key ARN in SCP or bucket policy. Caller MUST send the header explicitly.
