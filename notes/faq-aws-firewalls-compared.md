# FAQ: AWS "Firewalls" — All 5 Compared

> **Blueprint refs:** Task 3.1 (edge security), Task 3.2 (compute), Task 3.3 (network security), Task 6.1 (governance)
> **Diagram:** [aws-firewalls-compared.png](../diagrams/aws-firewalls-compared.png)
> **Purpose:** AWS has 5 things called "firewall." This file clarifies all of them in one place.

## The Problem: 5 "Firewalls" at 5 Different Layers

```
THE INTERNET
     │
     ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1: AWS WAF                                               │
│  ═══════════════                                                │
│  WHERE: CloudFront, ALB, API Gateway, AppSync, Cognito         │
│  WHAT:  HTTP/HTTPS request filtering (Layer 7)                 │
│  BLOCKS: SQLi, XSS, bad bots, geo, rate limits                │
│  ANALOGY: ModSecurity / OWASP CRS on NGINX Ingress            │
│  COST: ~$5/month per Web ACL + $1/rule + $0.60/M requests     │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 2: AWS Shield                                            │
│  ═══════════════════                                            │
│  WHERE: CloudFront, ALB, NLB, EIP, Global Accelerator, R53    │
│  WHAT:  DDoS protection (Layer 3/4, and 7 with Advanced)      │
│  BLOCKS: SYN floods, UDP reflection, volumetric attacks        │
│  ANALOGY: Cloudflare DDoS protection                           │
│  COST: Standard = FREE (always on). Advanced = $3,000/month   │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 3: Security Groups + NACLs                               │
│  ════════════════════════════════                                │
│  WHERE: SG = ENI (instance). NACL = Subnet.                   │
│  WHAT:  IP/port/protocol filtering (Layer 3-4)                 │
│  SG:    Stateful, allow-only, no deny rules, per-instance      │
│  NACL:  Stateless, allow+deny, needs ephemeral ports, per-subnet│
│  ANALOGY: SG = K8s NetworkPolicy. NACL = iptables on the node.│
│  COST: FREE                                                     │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 4: AWS Network Firewall                                  │
│  ═════════════════════════════                                  │
│  WHERE: Dedicated firewall subnet (inline, per AZ)             │
│  WHAT:  Deep packet inspection, IDS/IPS (Layer 3-7)           │
│  BLOCKS: Suricata signatures, domain filtering, TLS inspection │
│  ANALOGY: Calico Enterprise DPI / Palo Alto in a pod           │
│  COST: ~$288/month per AZ + $0.065/GB processed (EXPENSIVE)   │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 5: Route 53 Resolver DNS Firewall                        │
│  ═══════════════════════════════════════                         │
│  WHERE: VPC-level (all resources in the VPC)                   │
│  WHAT:  DNS query filtering — allow/block domain resolution    │
│  BLOCKS: DNS exfiltration, C2 domains, unapproved domains     │
│  ANALOGY: CoreDNS policy plugin / Istio ServiceEntry           │
│  COST: Low (~$0.0005/query after free tier)                    │
└─────────────────────────────────────────────────────────────────┘

PLUS: AWS Firewall Manager (not a firewall — it's a MANAGER)
  ═══════════════════════════════════════════════════════════
  WHERE: AWS Organizations (org-wide)
  WHAT:  Centrally deploy and manage ALL of the above across accounts
  MANAGES: WAF, Shield Advanced, SGs, Network Firewall, DNS Firewall
  ANALOGY: ArgoCD deploying all your security policies across clusters
  COST: ~$100/month per policy per region
```

## Decision Matrix (Exam-Critical)

| Exam Question Says | Answer | Layer | NOT This |
|---|---|---|---|
| "Block SQL injection" | **WAF** | HTTP (L7) | ❌ Network Firewall |
| "Rate limit API requests" | **WAF** rate-based rules | HTTP (L7) | ❌ Shield |
| "DDoS protection" | **Shield** (Standard=free, Advanced=$3K) | L3/4/7 | ❌ WAF alone |
| "Allow port 443 from this CIDR" | **Security Group** | L3-4 | ❌ Network Firewall (overkill) |
| "Need ephemeral port rules" | **NACL** (stateless) | L3-4 | ❌ Security Group (stateful, handles it) |
| "Inspect traffic content / IDS/IPS" | **Network Firewall** | L3-7 | ❌ WAF (HTTP only) |
| "Suricata signatures" | **Network Firewall** | L3-7 | ❌ WAF |
| "Block DNS lookup to bad domains" | **DNS Firewall** | DNS | ❌ Network Firewall |
| "Prevent DNS exfiltration" | **DNS Firewall** | DNS | ❌ GuardDuty (detects, doesn't block) |
| "Deploy WAF rules across 200 accounts" | **Firewall Manager** | Org | ❌ Manual per-account WAF |
| "Ensure all VPCs have DNS Firewall" | **Firewall Manager** | Org | ❌ Manual per-VPC |

## Side-by-Side Comparison

| Dimension | WAF | Shield | Security Groups | NACLs | Network Firewall | DNS Firewall | Firewall Manager |
|---|---|---|---|---|---|---|---|
| **Layer** | 7 (HTTP) | 3/4/7 | 3-4 | 3-4 | 3-7 | DNS | N/A (manager) |
| **Scope** | CloudFront/ALB/APIGW | CloudFront/ALB/NLB/EIP | ENI | Subnet | Subnet (inline) | VPC | Organization |
| **Stateful?** | N/A | N/A | ✅ Yes | ❌ No | Both | N/A | N/A |
| **IDS/IPS?** | ❌ | ❌ | ❌ | ❌ | ✅ Yes | ❌ | ❌ |
| **Domain filtering?** | ❌ | ❌ | ❌ | ❌ | ✅ (SNI) | ✅ (DNS) | ❌ |
| **DDoS?** | Partial | ✅ Primary | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Cost** | 💰 Low | 🆓/💰💰💰 | 🆓 Free | 🆓 Free | 💰💰💰 High | 💰 Low | 💰💰 Medium |
| **Blueprint task** | 3.1 | 3.1 | 3.3 | 3.3 | 3.3 | 3.3 | 6.1 |

## AWS Firewall Manager — The Orchestrator (Task 6.1)

Firewall Manager is NOT a firewall. It's a **central management service** that deploys
and enforces firewall rules across your entire AWS Organization.

```
WITHOUT Firewall Manager:
  Account 1: manually configure WAF ──┐
  Account 2: manually configure WAF ──┤  200 accounts × 5 regions
  Account 3: manually configure WAF ──┤  = 1,000 manual configs
  ...                                  │  Someone forgets one = breach
  Account 200: manually configure WAF ─┘

WITH Firewall Manager:
  Security Account: ONE Firewall Manager policy
    → auto-deploys to all 200 accounts
    → auto-applies to new accounts
    → detects and remediates non-compliant resources
    → single pane of glass
```

### What Firewall Manager Can Manage

| Policy Type | What It Deploys | Use Case |
|---|---|---|
| **WAF** | Web ACLs + rule groups | Org-wide SQLi/XSS protection |
| **Shield Advanced** | Shield protections | Org-wide DDoS protection |
| **Security Groups** | Common SG rules + audit | Enforce baseline SG rules, find overly permissive SGs |
| **Network Firewall** | Firewall policies | Org-wide IDS/IPS |
| **DNS Firewall** | Rule group associations | Org-wide DNS filtering |
| **Third-party firewalls** | Palo Alto, Fortinet via Marketplace | Hybrid environments |

### Firewall Manager Prerequisites

1. **AWS Organizations** with all features enabled
2. **AWS Config** enabled in all accounts/regions (Firewall Manager reads Config)
3. **Delegated administrator** account (don't run in management account)
4. **Resource sets** define which resources the policy applies to

### Firewall Manager Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Requires AWS Config** | Won't work without Config enabled everywhere |
| **Requires Organizations** | Cannot use with standalone accounts |
| **Delegated admin** | Best practice: Security Tooling account, not management account |
| **Auto-remediation** | Can automatically apply rules to non-compliant resources |
| **New accounts** | Policies auto-apply to new accounts joining the org |
| **SG audit** | Can find overly permissive SGs (0.0.0.0/0) and remediate |
| **Cost** | ~$100/month per policy per region — adds up fast |
| **Regional** | Must create policies in each region (except WAF on CloudFront = us-east-1) |

### SRA Placement

```
┌─────────────────────────────────────────────────┐
│  Security Tooling Account (delegated admin)      │
│                                                  │
│  Firewall Manager ─── creates policies ──────►  │
│       │                                          │
│       ├── WAF policy ──► all ALBs in all accounts│
│       ├── Shield policy ──► all CloudFront dists │
│       ├── SG audit policy ──► find 0.0.0.0/0    │
│       ├── Network Firewall ──► all egress VPCs   │
│       └── DNS Firewall ──► all VPCs              │
│                                                  │
└─────────────────────────────────────────────────┘
```

## Traffic Flow: How They Layer Together

```
Internet
  │
  ▼
CloudFront ◄── Shield Standard (always on, free)
  │             Shield Advanced (optional, $3K/month)
  │
  ▼
WAF (Web ACL) ◄── blocks SQLi, XSS, bots, geo, rate limits
  │
  ▼
ALB ◄── Security Group (allow 443 from CloudFront prefix list)
  │
  ▼
┌─────────────────────────────────────────┐
│  VPC                                     │
│                                          │
│  DNS Firewall ◄── blocks bad DNS lookups │
│       │                                  │
│  Firewall Subnet                         │
│  └── Network Firewall ◄── IDS/IPS,      │
│       │                   Suricata rules │
│       │                                  │
│  Private Subnet                          │
│  └── EC2/EKS ◄── Security Group         │
│       │           (allow from ALB only)  │
│       │                                  │
│  NACL on each subnet ◄── stateless      │
│       (backup layer, usually wide open)  │
│                                          │
└─────────────────────────────────────────┘

Firewall Manager: deploys ALL of the above
                   across ALL accounts from ONE place
```

## K8s/Istio Mapping (Your Mental Model)

| AWS Firewall | K8s/Istio Equivalent | Why |
|---|---|---|
| **WAF** | ModSecurity on Ingress / Istio EnvoyFilter | L7 HTTP filtering at the edge |
| **Shield** | Cloudflare / external DDoS proxy | Volumetric attack absorption |
| **Security Groups** | K8s NetworkPolicy | Per-pod (per-ENI) allow rules |
| **NACLs** | Node-level iptables | Subnet-wide, stateless, backup layer |
| **Network Firewall** | Calico Enterprise DPI / dedicated firewall pod | Inline deep inspection |
| **DNS Firewall** | CoreDNS policy / Istio ServiceEntry | Control which domains can resolve |
| **Firewall Manager** | ArgoCD + OPA/Gatekeeper deploying policies across clusters | Central policy enforcement |

## Exam Traps — Common Distractors

1. **"Filter by domain name"** — TWO services can do this:
   - **DNS Firewall**: blocks the DNS lookup (domain never resolves)
   - **Network Firewall**: blocks the traffic (inspects SNI in TLS handshake)
   - Exam differentiator: "restrict DNS resolution" → DNS Firewall. "Inspect traffic to domain" → Network Firewall.

2. **"Protect against DDoS"** — Shield, not WAF
   - WAF rate-based rules help, but Shield is the DDoS answer
   - Shield Advanced includes WAF at no extra cost

3. **"Deploy security rules across all accounts"** — Firewall Manager
   - Not "create WAF rules in each account" — that's manual
   - Firewall Manager = org-wide automation

4. **"Find overly permissive security groups"** — TWO answers:
   - **Firewall Manager** SG audit policy (org-wide, auto-remediate)
   - **Config** managed rule `restricted-ssh` (per-account, detect only)
   - Exam preference: Firewall Manager for org-wide + remediation

5. **"Stateless firewall"** — TWO things:
   - **NACLs** (subnet-level, free)
   - **Network Firewall stateless rules** (evaluated first, before stateful)
   - Don't confuse: Network Firewall has BOTH stateless and stateful engines

## Key Quotas

| Service | Limit | Value |
|---|---|---|
| WAF | Web ACLs per region | 100 |
| WAF | WCU per Web ACL | 1,500 |
| Shield Advanced | Cost | $3,000/month + 1yr commitment |
| Security Groups | Rules per SG | 60 inbound + 60 outbound |
| Security Groups | SGs per ENI | 5 |
| NACLs | Rules per NACL | 20 (can increase to 40) |
| Network Firewall | Endpoints per AZ | 1 per firewall |
| Network Firewall | Cost per AZ | ~$288/month + $0.065/GB |
| DNS Firewall | Rule groups per VPC | 1 (but group can have many rules) |
| Firewall Manager | Cost per policy per region | ~$100/month |
