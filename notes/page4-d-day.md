# PAGE 4 — D-DAY (Infrastructure D3)

> Write by hand. Read once before entering the exam room.

---

## Error Type = Layer

```
TIMEOUT       = NETWORK (SG, NACL, routing, missing endpoint)
ACCESS DENIED = PERMISSIONS (IAM, policy, key policy, endpoint policy)

Private API timeout from ONE caller (others work) = Resource Policy
Private API timeout from ALL callers = actual network (SG/endpoint missing)
Private API 403 = execution role missing execute-api:Invoke
```

## Interface Endpoint = TWO SGs

```
Lambda SG → outbound 443 (to endpoint)
Endpoint SG → inbound 443 (from Lambda SG)

Miss EITHER = timeout. Not permissions — NETWORK.
```

## Gateway Endpoint = Hidden Allowlist

```
All IAM correct + Access Denied + private subnet
→ check Gateway endpoint policy (the invisible 6th gate)
Only listed actions pass. ListBucket not listed = denied.
```

## NACL vs SG

```
Flow Log: inbound ACCEPT + outbound REJECT = ALWAYS NACL
(SG is stateful — accepted inbound = auto-allowed return)
NACLs = stateless (need explicit outbound ephemeral 1024-65535)
```

## Traffic Inspection — 3 Patterns

```
PASSIVE (copy, no block)     → Traffic Mirroring → NLB → IDS (VXLAN)
INLINE third-party           → GWLB → Palo Alto/Fortinet (GENEVE)
INLINE AWS-native            → Network Firewall (Suricata)

"Full packet + passive + IDS" = Traffic Mirroring (NEVER Flow Logs)
"Block + third-party"         = GWLB
"Block + Suricata/IPS"        = Network Firewall
```

## Firewalls — Which Does What

```
WAF        = HTTP layer (SQLi, XSS, bots, rate-limit) → ALB/CF/APIGW
Shield     = DDoS (L3/4/7) → $3K/month for Advanced
NF         = IPS/IDS (Suricata, TLS inspect) → subnet-level inline
DNS FW     = block DNS resolution → VPC-level
FM         = deploy rules org-wide (WAF/SG/NF/DNS FW)
```

## NF TLS Inspection

```
Users get cert warnings = Private CA not in client trust stores
Fix: distribute Private CA cert to all clients
NOT public ACM cert. NOT self-signed. = Private CA + distribute.
```

## Connectivity

```
Site-to-Site VPN = office router to AWS (IPsec, over internet)
Client VPN       = laptops to AWS (full tunnel, needs client)
Direct Connect   = dedicated fiber (private, NOT encrypted!)
MACsec           = Layer 2 encryption on DEDICATED DX only
Verified Access  = per-app, zero-trust, no VPN client, browser only

"Layer 2 + dedicated" = MACsec
"Encrypt hosted DX"   = VPN over DX (not MACsec)
IPv4 outbound-only    = NAT Gateway
IPv6 outbound-only    = Egress-Only IGW (NAT doesn't support IPv6)
```

## API Gateway Security

```
mTLS = custom domain + S3 truststore (PEM + versioning required)
Resource Policy = boundary (evaluates BEFORE authorizer)
TOKEN authorizer = only gets token string (can't see IP/headers)
REQUEST authorizer = headers + IP + query + context (use for HMAC/IP)
```

## DNS Logging (TWO features, don't confuse)

```
DNS query logging    = queries TO your public zone (inbound) → CW Logs ONLY
Resolver query logging = queries FROM your VPC (outbound) → S3 + CW + Firehose
```
