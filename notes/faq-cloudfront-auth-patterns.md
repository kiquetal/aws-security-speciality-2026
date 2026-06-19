# FAQ: CloudFront Authentication & Security Patterns

> **Blueprint refs:** Task 3.1 (edge security), Task 5.1 (data in transit)
> **Purpose:** CloudFront security mechanisms and when to use which. Dojo tests exact distinctions.

---

## The Four CloudFront Security Mechanisms

```
┌─────────────────────────────────────────────────────────────────┐
│  CLOUDFRONT SECURITY — FOUR DIFFERENT PROBLEMS                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. OAC (Origin Access Control)                                  │
│  ══════════════════════════════                                  │
│  PROBLEM: Prevent direct S3 access (bypass CloudFront)           │
│  HOW:     S3 bucket policy only allows CloudFront service        │
│  RESULT:  Users MUST go through CloudFront, can't hit S3 URL     │
│  DOES NOT: Authenticate users at CloudFront level                │
│                                                                  │
│  2. Lambda@Edge (viewer-request)                                 │
│  ═══════════════════════════════                                 │
│  PROBLEM: Enforce authentication BEFORE serving content          │
│  HOW:     Check JWT/cookie/session on every request              │
│  RESULT:  Unauthenticated users get redirected to login          │
│  USE:     When you need custom auth logic at the edge            │
│                                                                  │
│  3. CloudFront Response Headers Policy                           │
│  ═════════════════════════════════════                            │
│  PROBLEM: Add security headers (HSTS, CSP, X-Content-Type)      │
│  HOW:     Managed policy attached to cache behavior              │
│  RESULT:  Every response includes security headers               │
│  USE:     Static headers, zero code, least overhead              │
│                                                                  │
│  4. Field-Level Encryption (FLE)                                 │
│  ════════════════════════════════                                │
│  PROBLEM: Encrypt specific POST fields at the edge               │
│  HOW:     RSA public key → profile → config → cache behavior    │
│  RESULT:  Intermediate systems can't see raw field values        │
│  USE:     PII/credit cards encrypted before reaching origin      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## OAC vs Lambda@Edge Auth — THE KEY DISTINCTION

```
SCENARIO: SPA on S3 via CloudFront. Unsigned users downloading source code.

  OAC alone:
  ┌────────────────────────────────────────────────┐
  │  Unauthenticated user → CloudFront → S3        │
  │                          ✅ serves content     │
  │                                                 │
  │  Unauthenticated user → S3 direct              │
  │                          ❌ BLOCKED (no OAC)   │
  └────────────────────────────────────────────────┘
  OAC prevents S3 BYPASS, but CloudFront still serves to EVERYONE.

  Lambda@Edge viewer-request:
  ┌────────────────────────────────────────────────┐
  │  Unauthenticated user → CloudFront → Lambda@Edge │
  │                          → no valid token?      │
  │                          → REDIRECT to login ❌ │
  │                                                 │
  │  Authenticated user → CloudFront → Lambda@Edge  │
  │                          → valid token? ✅      │
  │                          → serve SPA            │
  └────────────────────────────────────────────────┘
  Lambda@Edge AUTHENTICATES at CloudFront level.
```

### Decision Table

| Question says... | Answer | Why |
|---|---|---|
| "Prevent direct S3 access" | OAC | Locks origin, not the edge |
| "Prevent unauthenticated access via CloudFront" | Lambda@Edge viewer-request | Auth gate at the edge |
| "Unsigned users can see content" | Lambda@Edge (not OAC!) | OAC doesn't solve this |
| "S3 + CloudFront + Cognito auth" | OAC (lock S3) + Lambda@Edge (check JWT) | Often need BOTH |

> **Exam trap:** OAC is NOT authentication. It's origin protection. "Users can still access content without signing in" = Lambda@Edge viewer-request is missing.

---

## Response Headers Policy vs Lambda@Edge

```
┌─────────────────────────────────────────────────────────────────┐
│  ADDING HEADERS TO RESPONSES                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  STATIC headers (HSTS, CSP, X-Frame-Options):                   │
│  → CloudFront Response Headers Policy (managed, zero code)       │
│  → "SecurityHeadersPolicy" = built-in managed policy             │
│  → LEAST overhead, LEAST effort                                  │
│                                                                  │
│  DYNAMIC/CONDITIONAL headers (vary by request, user, path):      │
│  → Lambda@Edge (viewer-response or origin-response)              │
│  → Custom code required                                          │
│  → More overhead, more flexibility                               │
│                                                                  │
│  CloudFront Functions (viewer-response):                         │
│  → Lightweight (< 10KB, no network, < 1ms)                      │
│  → Simple header manipulation only                               │
│  → Can't validate tokens or make API calls                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Rule

| Need | Answer |
|---|---|
| "Add security headers, least overhead" | Response Headers Policy (managed) |
| "Dynamic logic per request" | Lambda@Edge |
| "Simple header rewrite, lightweight" | CloudFront Functions |

> **Exam trap:** "HSTS + CSP + least overhead" ≠ Lambda@Edge. That's the managed Response Headers Policy.

---

## Field-Level Encryption (FLE) — Setup Chain

```
Step 1: Upload RSA PUBLIC key to CloudFront
Step 2: Create FLE Profile (map field name → public key)
Step 3: Create FLE Configuration (map content-type → profile)
Step 4: Attach FLE Config to cache behavior

  POST request → CloudFront edge
    → FLE encrypts "claim_id" field with RSA public key
    → Encrypted payload forwarded to origin
    → Origin decrypts with RSA PRIVATE key (lives on YOUR server)
    → AWS never sees the private key
```

### Key Facts

| Fact | Detail |
|---|---|
| Key type | RSA (asymmetric) — public at edge, private at origin |
| KMS involved? | NO — FLE uses its own RSA keys, not KMS |
| Who decrypts? | YOUR origin server (private key lives there) |
| What's encrypted? | Specific POST form fields (not entire request) |
| Intermediate visibility? | Cannot see raw values (WAF, logs, caches) |

> **Exam trap:** FLE ≠ KMS. FLE uses RSA keys you upload. KMS encryption context is a SEPARATE concern enforced at the S3/KMS layer by application code.

---

## Signed URLs vs Signed Cookies

```
Signed URL:  One URL = one resource. Embed expiry + signature in URL.
             Use when: single file download, time-limited access.

Signed Cookie: One cookie = access to multiple resources.
               Use when: entire site/SPA access for authenticated users.

Both use CloudFront key pairs (not KMS).
```

---

## 🧠 Cheat-Sheet One-Liners

- **OAC = "prevent S3 bypass." Lambda@Edge viewer-request = "enforce auth at CloudFront level." Different problems.**
- **"Unsigned users see content via CloudFront" = Lambda@Edge missing (OAC alone doesn't solve this).**
- **"Add HSTS/CSP headers, least overhead" = CloudFront Response Headers Policy (managed, zero code). NOT Lambda@Edge.**
- **FLE = RSA public key at edge, private key on YOUR origin. NOT KMS. Intermediate systems can't see raw values.**
- **FLE setup chain: key → profile (field→key) → config (content-type→profile) → cache behavior.**
- **Signed URL = one file. Signed Cookie = multiple files/whole site.**
