# AWS Signer — Slide Deck

---

## The 3 Pieces

```
PIECE 1: Signing Profile
  = "The stamp authority"
  = Created once, used many times
  = Has a name: "ReleaseSigning"
  = Has an algorithm: ECDSA
  
PIECE 2: Signing Job
  = "One use of the stamp"
  = Input: unsigned Lambda zip in S3
  = Output: signed Lambda zip in S3
  = Each job has a unique ID
  = You can have 1000s of jobs per profile

PIECE 3: Code Signing Configuration (CSC)
  = "The bouncer on the Lambda function"
  = Says: "I only accept stamps from these profiles"
  = Says: "If no valid stamp → ENFORCE (block) or WARN (log)"
  = ATTACHED to the Lambda function
```

---

## How They Connect

```
CI Pipeline
    │
    ▼
┌─────────────────┐
│ Signing Profile  │ ← "ReleaseSigning" (the authority)
│ (created once)   │
└────────┬────────┘
         │ used by
         ▼
┌─────────────────┐
│ Signing Job #1   │ → signs lambda-orders.zip
│ Signing Job #2   │ → signs lambda-payments.zip
│ Signing Job #3   │ → signs lambda-backdoor.zip  ← bad one
│ Signing Job #4   │ → signs lambda-auth.zip
└────────┬────────┘
         │ verified by
         ▼
┌─────────────────┐
│ CSC              │ ← attached to Lambda function
│ Allowed: "ReleaseSigning"
│ Policy: ENFORCE
└─────────────────┘
```

---

## Deploy Time Verification

```
Developer deploys Lambda:
  → CSC asks: "Was this zip signed by ReleaseSigning?"
  → Checks the signing job status
  → If ACTIVE     → ✅ deploy allowed
  → If REVOKED    → ❌ deployment blocked
  → If no signature → ❌ blocked (ENFORCE mode)
```

---

## The 4 Actions

```
SCENARIO 1: Developer leaves, no suspicion
  → Remove IAM access to signer:StartSigningJob
  → They can't sign NEW things
  → Everything already signed stays valid

SCENARIO 2: One specific artifact is bad
  → Revoke that SIGNING JOB (job #3)
  → Only lambda-backdoor.zip becomes invalid
  → Jobs #1, #2, #4 still valid
  → Surgical fix

SCENARIO 3: Signing profile compromised
  → Revoke the SIGNING PROFILE
  → ALL jobs (#1, #2, #3, #4) become invalid
  → Must re-sign everything with new profile
  → Nuclear — causes outage until re-signed

SCENARIO 4: Remove CSC from function
  → No more verification at all
  → Anyone deploys anything
  → ❌ NEVER do this
```

---

## Exam Cheat

| Signal | Action |
|---|---|
| "Invalidate ONE artifact" | Revoke signing **JOB** |
| "Invalidate ALL from a signer" | Revoke signing **PROFILE** |
| "Prevent future signing" | Remove **IAM** access |
| "Remove enforcement" | Delete CSC (❌ NEVER the answer) |

---

## What Signer is NOT

```
Signer ≠ Inspector
  Signer = integrity (hasn't been tampered)
  Inspector = vulnerabilities (has known CVEs)

Signer ≠ CodeGuru
  Signer = cryptographic proof of origin
  CodeGuru = code quality analysis

Signer ≠ KMS
  Signer manages its own keys internally
  You don't manage the signing key yourself

Signer ≠ ACM
  ACM = TLS certificates for HTTPS
  Signer = code artifact signatures
```

---

## 🧠 One-Liners

- **Profile = stamp authority. Job = one stamp. CSC = bouncer checking stamps.**
- **"One bad artifact" = revoke JOB. "Authority compromised" = revoke PROFILE.**
- **Remove IAM = prevent future. Revoke job = fix the past.**
- **Delete CSC = NEVER the answer.**
