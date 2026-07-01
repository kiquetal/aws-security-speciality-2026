# CloudFront Security — Flashcard

> Everything CloudFront security in one place. Covers: geo restriction, OAC, headers, FLE, WAF, logging.

---

## 1. Geo Restriction (Block/Allow Countries)

```
CloudFront → Distribution → Geographic restrictions
  → Allowlist: only THESE countries
  → Blocklist: block THESE countries

Cost: FREE (built-in)
Mechanism: CloudFront uses GeoIP database (MaxMind)
```

| Scenario | Answer |
|---|---|
| "Block countries + cost-effective + CloudFront" | CloudFront Geo Restriction (free) |
| "Block countries + rate limit + SQLi together" | WAF Geo-Match (need combined rules) |
| "Block countries on ALB (no CF)" | WAF Geo-Match (only option) |
| "Route countries to different servers" | Route 53 geolocation routing |

---

## 2. Origin Access Control (OAC)

```
Problem: S3 bucket should ONLY be accessible via CloudFront (not direct S3 URL)
Solution: OAC (replaces legacy OAI)

OAC:
  ✅ Supports SSE-KMS (OAI doesn't!)
  ✅ Supports S3 in any region
  ✅ Supports dynamic requests (PUT, DELETE)
  ✅ Uses service principal: cloudfront.amazonaws.com

Required:
  1. S3 bucket policy: Allow s3:GetObject from cloudfront.amazonaws.com
  2. KMS key policy: Allow kms:Decrypt from cloudfront.amazonaws.com (if SSE-KMS)
  3. Block public access on bucket (OAC is the only path in)
```

| Scenario | Answer |
|---|---|
| "S3 + SSE-KMS + only via CloudFront" | OAC + KMS key policy for CF |
| "S3 only via CloudFront (no KMS)" | OAC (or OAI — both work) |
| "OAI + SSE-KMS = Access Denied" | Switch to OAC (OAI can't do KMS) |

---

## 3. Security Headers (HSTS, CSP, X-Content-Type-Options)

```
Problem: Add security response headers to CloudFront responses
Solution: Response Headers Policy (managed, zero code)

NOT Lambda@Edge (unless you need dynamic/conditional logic)
```

| Scenario | Answer |
|---|---|
| "Static HSTS/CSP/X-Frame headers, least overhead" | Response Headers Policy (managed) |
| "Dynamic header based on request path or cookie" | Lambda@Edge (custom logic needed) |
| "Add CORS headers" | Response Headers Policy (CORS preset) |

---

## 4. Field-Level Encryption (FLE)

```
Problem: Encrypt specific POST fields at edge (PII protection)
Solution: CloudFront FLE

Architecture:
  Client → CloudFront (encrypts field with RSA public key)
         → Origin receives encrypted blob
         → Only YOUR backend with private key can decrypt

Setup chain: RSA public key → FLE Profile → FLE Config → Cache Behavior

Key points:
  • Public key: uploaded to CloudFront (encrypts at edge)
  • Private key: on YOUR origin (AWS never has it)
  • Per-field encryption (choose which fields)
  • Encrypted before reaching origin
```

| Scenario | Answer |
|---|---|
| "Encrypt credit card at edge before origin" | FLE |
| "WAF can't see encrypted field" | Expected — FLE encrypts before WAF on origin |
| "Where's the private key?" | YOUR server (never AWS) |

---

## 5. WAF on CloudFront

```
WAF attached to CloudFront:
  • Must be in us-east-1 (global)
  • Evaluates BEFORE cache hit (every request checked)
  • Protects: SQLi, XSS, bots, rate limit, geo, IP
```

| Scenario | Answer |
|---|---|
| "Rate limit per IP on CloudFront" | WAF rate-based rule on CF |
| "Block SQLi at edge" | WAF on CF (us-east-1) |
| "Bot detection + JS challenge" | WAF Bot Control on CF |
| "Block country cheaply (only geo needed)" | CF Geo Restriction (free, no WAF needed) |

---

## 6. Viewer/Origin Protocol Policy

```
Viewer Protocol Policy (Client ↔ CloudFront):
  • HTTP and HTTPS: allow both
  • Redirect HTTP to HTTPS: upgrade clients
  • HTTPS Only: reject HTTP

Origin Protocol Policy (CloudFront ↔ Origin):
  • HTTP Only: CF→origin on port 80
  • HTTPS Only: CF→origin on port 443
  • Match Viewer: mirrors what client used

Neither controls HEADERS — that's Cache Policy / Origin Request Policy.
```

---

## 7. Authorization Header Forwarding

```
Problem: Origin requires Authorization header, CloudFront strips it by default.

Fix: Include Authorization in Cache Policy OR Origin Request Policy

Impact: If in Cache Policy → caches per-user (low hit rate)
        If in Origin Request Policy → forwards without caching on it
```

---

## 8. Logging

```
Standard Logs:
  → S3 only
  → Delayed (minutes-hours)
  → FREE
  → Uses ACLs (BucketOwnerEnforced = breaks it!)

Real-Time Logs:
  → Kinesis Data Streams
  → Seconds latency
  → Costs money (Kinesis pricing)
  → IAM role mechanism

Access Logs not appearing?
  → Check: target bucket ACLs enabled (BucketOwnerPreferred)
```

---

## 9. Signed URLs / Signed Cookies

```
Signed URL: one specific file, time-limited
Signed Cookie: multiple files (whole site), time-limited

Use: Restrict content to paying customers / authenticated users

Created with: CloudFront key pair (legacy) or Key Group (recommended)
```

| Scenario | Answer |
|---|---|
| "One file, expiring link" | Signed URL |
| "Entire site access for subscribers" | Signed Cookies |
| "Restrict by IP + time + path" | Signed URL with custom policy |

---

## 10. Lambda@Edge vs CloudFront Functions

```
Lambda@Edge:
  → Full Lambda runtime
  → All 4 events: viewer-request, viewer-response, origin-request, origin-response
  → Max 30s (origin events), 5s (viewer events)
  → Use: auth, A/B testing, dynamic redirects

CloudFront Functions:
  → Lightweight JavaScript only
  → Only: viewer-request, viewer-response
  → Max 1ms execution
  → Use: header manipulation, URL rewrites, cache key normalization
  → 1/6th the cost of Lambda@Edge
```

| Scenario | Answer |
|---|---|
| "Validate JWT at edge" | Lambda@Edge (viewer-request) |
| "Add simple header to response" | Response Headers Policy (even simpler) |
| "Normalize URL for cache key" | CloudFront Functions |
| "Complex auth with DB lookup" | Lambda@Edge |

---

## Exam Decision Summary

| Question Says | Answer |
|---|---|
| "Block countries, cheapest" | CF Geo Restriction |
| "S3 only via CF + SSE-KMS" | OAC + KMS key policy |
| "Static security headers" | Response Headers Policy |
| "Encrypt field at edge" | FLE |
| "Protect from SQLi/XSS + rate limit" | WAF on CF (us-east-1) |
| "Forward Authorization header" | Cache Policy or Origin Request Policy |
| "Logs not appearing" | Check S3 ACLs (BucketOwnerPreferred) |
| "Restrict content to subscribers" | Signed URLs/Cookies |
| "Auth at edge" | Lambda@Edge viewer-request |
