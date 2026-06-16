# FAQ: API Gateway Security (Task 3.1)

> **Blueprint refs:** Task 3.1 (network edge services), Task 4.1 (authentication)
> **Never-seen topic #1** — zero questions in 968 attempts before Session 96.
> **Exam weight:** D3 Infrastructure = 18%. API Gateway appears in edge security + auth questions.

---

## The 4 Security Layers of API Gateway

```
Request arrives at API Gateway:

  ┌─────────────────────────────────────────────────────────────┐
  │ LAYER 1: RESOURCE POLICY                                     │
  │ ═══════════════════════                                      │
  │ Evaluated FIRST — before authorizers, before WAF             │
  │                                                              │
  │ What it checks:                                              │
  │   • aws:SourceIp (CIDR range)                                │
  │   • aws:SourceVpc (VPC ID)                                   │
  │   • aws:SourceVpce (VPC endpoint ID)                         │
  │   • aws:PrincipalAccount (account ID)                        │
  │                                                              │
  │ What it CANNOT check:                                        │
  │   • Headers, body, JWT claims, cookies                       │
  │                                                              │
  │ Use case: "Block before anything runs" = save cost + reduce  │
  │           attack surface                                     │
  │                                                              │
  │ Scope: Per-resource path (e.g., deny /legacy/* from non-     │
  │         approved IPs, allow /web/* from anywhere)            │
  └──────────────────────────┬──────────────────────────────────┘
                             │ passes
                             ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ LAYER 2: WAF (if attached)                                   │
  │ ════════════════════════                                     │
  │ HTTP-level filtering: SQLi, XSS, rate-limit, bot control    │
  │ Regional APIs: WAF in same region                            │
  │ Edge-optimized: WAF must be in us-east-1                     │
  └──────────────────────────┬──────────────────────────────────┘
                             │ passes
                             ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ LAYER 3: AUTHORIZER                                          │
  │ ═════════════════                                           │
  │                                                              │
  │ Type 1: Cognito Authorizer                                   │
  │   • Validates JWT tokens from Cognito User Pool              │
  │   • Zero code — managed by API Gateway                       │
  │   • Use for: web/mobile apps with Cognito                    │
  │                                                              │
  │ Type 2: Lambda Authorizer (TOKEN)                            │
  │   • Receives ONLY the token string (from specified header)   │
  │   • Use for: custom JWT, API keys in Authorization header    │
  │   • CANNOT access: other headers, query params, IP           │
  │                                                              │
  │ Type 3: Lambda Authorizer (REQUEST)                          │
  │   • Receives: ALL headers, query params, path params,        │
  │     stage variables, context (source IP, etc.)               │
  │   • Use for: HMAC validation, multi-header auth, IP checks  │
  │   • Most flexible — but code required                        │
  │                                                              │
  │ Returns: IAM policy (Allow/Deny) + optional context          │
  └──────────────────────────┬──────────────────────────────────┘
                             │ passes
                             ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ LAYER 4: IAM AUTHORIZATION (if using IAM auth)               │
  │ ═══════════════════════════════════════════                  │
  │ Caller signs request with SigV4                              │
  │ API Gateway checks IAM permissions (execute-api:Invoke)      │
  │ Condition keys: aws:SourceIp, aws:SourceVpc, etc.            │
  └─────────────────────────────────────────────────────────────┘
```

---

## Resource Policy — The Bouncer

```
Mental model:
  Resource Policy = bouncer at the door (checks ID/address)
  Authorizer = receptionist inside (validates appointment)

  If bouncer says no → you never reach the receptionist
  → No Lambda invocation cost
  → No authorizer code executed
```

### Example: Restrict legacy routes to specific IP range

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyLegacyFromUnknownIPs",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "execute-api:Invoke",
      "Resource": "arn:aws:execute-api:us-east-1:123456789012:api-id/*/POST/legacy/*",
      "Condition": {
        "NotIpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        }
      }
    }
  ]
}
```

### Example: Private API — only from specific VPC endpoint

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOnlyFromVpce",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "execute-api:Invoke",
      "Resource": "arn:aws:execute-api:us-east-1:123456789012:api-id/*",
      "Condition": {
        "StringNotEquals": {
          "aws:SourceVpce": "vpce-111111"
        }
      }
    }
  ]
}
```

---

## Mutual TLS (mTLS) — Client Certificate Authentication

```
┌───────────────────────────────────────────────────────────────┐
│ mTLS REQUIREMENTS (exam-critical):                             │
│                                                                │
│ 1. Custom domain name (REQUIRED — default endpoint can't mTLS)│
│ 2. CA truststore PEM file in S3 (versioning REQUIRED)         │
│ 3. Enable mTLS on the custom domain, provide S3 URI + version │
│ 4. Route 53 alias to custom domain                            │
│                                                                │
│ NOT these:                                                     │
│ ❌ Upload CA to ACM (ACM = server certs, not truststores)     │
│ ❌ Lambda authorizer to validate certs (works but not native)  │
│ ❌ ALB mTLS in front of API GW (unnecessary extra layer)      │
└───────────────────────────────────────────────────────────────┘

How mTLS works:
  Client → presents client certificate
  API Gateway → validates cert chain against S3 truststore
  If valid → request proceeds to authorizer/backend
  If invalid → 403 Forbidden (before authorizer)
```

---

## Private APIs — VPC Endpoint Pattern

```
┌────────────────────────────────────────────────────────────────┐
│ Private API = NO public DNS, NO internet access                 │
│ ONLY reachable via Interface VPC Endpoint (execute-api)         │
│                                                                 │
│ You create:                                                     │
│   aws ec2 create-vpc-endpoint                                   │
│     --service-name com.amazonaws.{region}.execute-api            │
│     --vpc-endpoint-type Interface                               │
│     --security-group-ids sg-endpoint-sg                         │
│                                                                 │
│ Two enforcement layers:                                         │
│   1. Resource Policy: aws:SourceVpce = vpce-xxx                 │
│   2. Endpoint SG: inbound 443 from client sg-yyy only           │
│                                                                 │
│ Result: only apps in sg-yyy via vpce-xxx can call the API       │
└────────────────────────────────────────────────────────────────┘
```

---

## Authorizer Type Decision Table

| Exam Signal | Authorizer Type |
|---|---|
| "Cognito JWT" / "User Pool tokens" | Cognito Authorizer (managed, zero code) |
| "Custom header" / "HMAC" / "API key in non-standard header" | Lambda REQUEST |
| "OAuth token in Authorization header" | Lambda TOKEN |
| "Validate source IP in authorizer" | Lambda REQUEST (TOKEN can't see IP) |
| "Multiple validation factors (header + IP + query)" | Lambda REQUEST |
| "Block IP BEFORE authorizer runs" | Resource Policy (not authorizer) |

---

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Resource Policy evaluated FIRST** | Before WAF, before authorizer — cheapest rejection point |
| **mTLS = custom domain + S3 truststore** | Not ACM, not Lambda, not ALB |
| **Private API = no public DNS** | Must use VPC endpoint — can't access from internet at all |
| **TOKEN type = one string only** | Can't inspect IP, other headers, or query params |
| **REQUEST type = everything** | Headers, query, path, stage vars, source IP |
| **WAF on private API** | ❌ NOT supported — use Resource Policy instead |
| **Resource Policy can't inspect body/headers** | Only network-level attributes (IP, VPC, account) |

---

## 🧠 Cheat-Sheet One-Liners

- **API Gateway mTLS = custom domain + S3 truststore (PEM + version).** Not ACM. Not Lambda.
- **Resource Policy = bouncer. Authorizer = receptionist.** Bouncer rejects before receptionist even sees you.
- **TOKEN type = single token string. REQUEST type = everything (headers, IP, query).** "Need IP validation" = REQUEST.
- **Private API = VPC endpoint only.** Resource Policy restricts vpce-id. Endpoint SG restricts client SG.
- **WAF doesn't work on private APIs.** Resource Policy is the only boundary control.
