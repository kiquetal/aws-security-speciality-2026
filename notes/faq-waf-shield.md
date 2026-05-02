# FAQ: AWS WAF + Shield

> **Blueprint refs:** Task 3.1 (edge security), Task 3.3 (network security)

## AWS WAF — Web Application Firewall

### What It Does (One-Liner)

**Filters HTTP/HTTPS requests at Layer 7 — blocks SQLi, XSS, rate limiting, geo-blocking.**

### K8s Mapping

```
WAF ≈ ModSecurity on NGINX Ingress Controller
    ≈ Istio AuthorizationPolicy with custom rules
    ≈ OWASP CRS (Core Rule Set) for your ingress
```

### Where WAF Attaches (Exam-Critical)

| Resource | Use Case |
|---|---|
| **CloudFront** | Protect static sites, APIs behind CDN |
| **ALB** | Protect web apps behind load balancer |
| **API Gateway** | Protect REST/HTTP APIs |
| **AppSync** | Protect GraphQL APIs |
| **Cognito User Pool** | Protect authentication endpoints |

> ⚠️ WAF does NOT attach to NLB, EC2 directly, or S3 directly.

### Rule Types

| Rule Type | What It Does | Example |
|---|---|---|
| **Rate-based** | Block IPs exceeding request threshold | Block IP after 2,000 requests in 5 min |
| **Regular** | Match request attributes | Block if User-Agent contains "BadBot" |
| **Managed rule groups** | Pre-built by AWS or Marketplace | AWS managed: SQLi, XSS, known bad inputs, IP reputation |

### Managed Rule Groups (Know These)

| Group | What It Blocks |
|---|---|
| **AWSManagedRulesCommonRuleSet** | OWASP Top 10 (SQLi, XSS, LFI, RFI) |
| **AWSManagedRulesSQLiRuleSet** | SQL injection patterns |
| **AWSManagedRulesKnownBadInputsRuleSet** | Log4j, known exploits |
| **AWSManagedRulesAmazonIpReputationList** | Known malicious IPs |
| **AWSManagedRulesBotControlRuleSet** | Bot detection and management |
| **Third-party (Marketplace)** | F5, Fortinet, Imperva rules |

### Rule Actions

| Action | What Happens |
|---|---|
| **Allow** | Request passes through |
| **Block** | Request rejected (403) |
| **Count** | Request passes but counted (monitoring mode) |
| **CAPTCHA** | Challenge the client |
| **Challenge** | Silent browser challenge (JS) |

### Key Limits/Quotas

| Limit | Value |
|---|---|
| Web ACLs per region | 100 |
| Rules per Web ACL | 1,500 WCU (Web ACL Capacity Units) |
| Rate-based rule threshold | 100–20,000,000 requests per 5 min |
| IP sets | 10,000 IPs per set |
| Regex patterns | 10 per regex set |
| Request body inspection | First 8 KB (default), up to 64 KB (paid) |

### Exam Gotchas

| Gotcha | Detail |
|---|---|
| **WAF is regional** | Except when attached to CloudFront (global) |
| **Rate-based rules** | Minimum threshold is 100 requests per 5 min |
| **Body inspection limit** | Only first 8 KB by default — large payloads can bypass |
| **Count mode first** | Always deploy in Count mode, then switch to Block |
| **Logging** | CloudWatch Logs, S3, or Kinesis Firehose |
| **WAF + CloudFront** | WAF must be in us-east-1 when attached to CloudFront |
| **OCSF format** | WAF logs can be ingested into Security Lake (new in C03) |
| **Third-party rules** | Can import Marketplace rules (Task 3.1.4 — new in C03) |

---

## AWS Shield — DDoS Protection

### Two Tiers

```
Shield Standard (free, automatic):
  ├── Enabled on ALL AWS accounts by default
  ├── Protects against Layer 3/4 DDoS (SYN floods, UDP reflection)
  ├── No configuration needed
  └── No visibility into attacks

Shield Advanced ($3,000/month + data transfer):
  ├── Layer 3/4/7 DDoS protection
  ├── DDoS cost protection (credits for scaling costs during attack)
  ├── 24/7 DDoS Response Team (DRT) access
  ├── WAF included at no extra cost
  ├── Real-time attack visibility and metrics
  ├── Health-based detection (Route 53 health checks)
  ├── Automatic application-layer mitigation
  └── 1-year commitment required
```

### Shield Advanced — What It Protects

| Resource | Layer |
|---|---|
| CloudFront | 3/4/7 |
| ALB | 3/4/7 |
| NLB | 3/4 |
| Elastic IP | 3/4 |
| Global Accelerator | 3/4 |
| Route 53 Hosted Zone | 3/4 |

### Key Limits/Quotas

| Limit | Value |
|---|---|
| Cost | $3,000/month + data transfer fees |
| Commitment | 1-year subscription |
| DDoS cost protection | Credits for CloudFront, ALB, Route 53, EIP scaling |
| DRT response time | Minutes (proactive engagement) |
| Resources per account | 1,000 protected resources |

### Exam Gotchas

| Gotcha | Detail |
|---|---|
| **$3,000/month** | If question mentions cost-sensitive → Shield Standard (free) |
| **DDoS cost protection** | Shield Advanced credits you for auto-scaling costs during attack |
| **DRT access** | Only with Advanced — they can manage your WAF rules during attack |
| **Proactive engagement** | Shield Advanced contacts YOU when it detects an attack |
| **Health-based detection** | Uses Route 53 health checks to detect application-layer attacks faster |
| **WAF included** | Shield Advanced includes WAF at no extra cost |
| **1-year commitment** | Cannot cancel early |
| **Shield Standard is always on** | You already have it — no setup needed |
| **Firewall Manager integration** | Deploy Shield Advanced across org via Firewall Manager |

---

## Decision Tree: Which Edge/Network Service?

```
What are you protecting against?
│
├── DDoS attack?
│   ├── Basic protection (free) → Shield Standard (already on)
│   └── Advanced + cost protection + DRT → Shield Advanced ($3K/month)
│
├── SQL injection / XSS / OWASP Top 10?
│   └── WAF (attached to CloudFront, ALB, or API Gateway)
│
├── Rate limiting / bot control?
│   └── WAF rate-based rules
│
├── Geo-blocking (block specific countries)?
│   └── WAF geo-match rules OR CloudFront geo-restriction
│
├── Deep packet inspection / IDS/IPS?
│   └── Network Firewall
│
├── Restrict DNS resolution?
│   └── DNS Firewall
│
└── Allow/deny by IP and port?
    └── Security Groups (stateful) / NACLs (stateless)
```

## WAF + Shield + CloudFront Together (Common Exam Pattern)

```
Internet → CloudFront → WAF → ALB → EC2
           │              │
           │              ├── SQLi/XSS blocked
           │              ├── Rate limiting
           │              └── Geo-blocking
           │
           └── Shield Advanced
               ├── DDoS protection (L3/4/7)
               ├── Cost protection
               └── DRT on standby
```
