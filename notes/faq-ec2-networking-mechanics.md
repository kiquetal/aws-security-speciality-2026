# FAQ: EC2 Networking Mechanics (Operational Details)

> **Blueprint refs:** Task 3.3 (network security controls), Task 3.1 (edge security)
> **Purpose:** Operational networking details that Dojo tests but are easy to miss.

---

## Public IP Communication Between EC2 Instances

```
┌─────────────────────────────────────────────────────────────────┐
│  SAME VPC, DIFFERENT AZs — TWO COMMUNICATION PATHS               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PATH 1: Private IP (stays inside VPC)                           │
│  ══════════════════════════════════════                           │
│  Instance A ──(private IP)──► Instance B                         │
│  • Traffic stays INSIDE VPC fabric                               │
│  • SG can reference: instance ID, SG ID, private IP             │
│  • NACL on both subnets evaluates                                │
│                                                                  │
│  PATH 2: Public IP (exits and re-enters via IGW)                 │
│  ═══════════════════════════════════════════════                  │
│  Instance A ──► IGW ──(internet routing)──► IGW ──► Instance B   │
│  • Traffic LEAVES VPC through Internet Gateway                   │
│  • Source appears as PUBLIC IP (not instance ID)                  │
│  • SG must reference: PUBLIC IP address                          │
│  • Instance ID / SG reference = WON'T WORK                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Rule

| Communication via | SG can reference |
|---|---|
| Private IP | Instance ID, SG ID, private IP, CIDR |
| Public IP | **Public IP only** (traffic traverses IGW, identity is lost) |

> **Exam trap:** "Two instances can communicate via private IPs but NOT public IPs" = SG must allow the OTHER instance's public IP. Instance ID references only work for private-IP traffic.

---

## IPv4 vs IPv6 Outbound-Only

```
┌─────────────────────────────────────────────────────────────────┐
│  OUTBOUND-ONLY INTERNET ACCESS                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  IPv4: NAT Gateway                                               │
│  ═════════════════                                               │
│  Private subnet → NAT GW (public subnet) → IGW → Internet       │
│  • Translates private IPv4 → public IPv4                         │
│  • Outbound yes, inbound no (NAT hides private IP)              │
│  • ONLY for IPv4                                                 │
│                                                                  │
│  IPv6: Egress-Only Internet Gateway                              │
│  ══════════════════════════════════                               │
│  Private subnet → Egress-Only IGW → Internet                     │
│  • NO translation needed (all IPv6 = globally routable)          │
│  • Outbound yes, inbound no (one-way gate)                       │
│  • ONLY for IPv6                                                 │
│  • NAT Gateway does NOT support IPv6                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Rule

| Protocol | Outbound-only mechanism | Why |
|---|---|---|
| IPv4 | NAT Gateway | Private IPs need translation |
| IPv6 | Egress-Only Internet Gateway | All IPv6 is public — just need a one-way gate |

> **Exam trap:** "IPv6 outbound-only" + NAT Gateway as an option = WRONG. NAT = IPv4 only. Always.

---

## VPC Endpoint Security Groups (Dual SG Pattern)

```
┌─────────────────────────────────────────────────────────────────┐
│  INTERFACE VPC ENDPOINT — TWO SGs MUST COOPERATE                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  EC2/Lambda                    VPC Endpoint (ENI)                 │
│  ┌──────────┐                 ┌──────────────────┐              │
│  │ SG-A     │ ──(443)──►     │ SG-B             │              │
│  │          │                 │                  │              │
│  │ OUTBOUND │                 │ INBOUND          │              │
│  │ Allow 443│                 │ Allow 443 from   │              │
│  │ to SG-B  │                 │ SG-A (or CIDR)   │              │
│  └──────────┘                 └──────────────────┘              │
│                                                                  │
│  Miss SG-A outbound → TIMEOUT                                   │
│  Miss SG-B inbound  → TIMEOUT                                   │
│  Both missing       → TIMEOUT                                   │
│  Permission issue   → ACCESS DENIED (different error!)           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Rule

| Symptom | Cause | Check |
|---|---|---|
| Timeout | Network (SG, NACL, routing, missing endpoint) | Both SGs |
| Access Denied | Permissions (IAM, endpoint policy, resource policy) | Policies |

> **Exam trap:** "Lambda timeout calling Secrets Manager, endpoint exists" = check BOTH SGs. Not IAM.

---

## Gateway Endpoint Policy (Hidden Gate)

```
┌─────────────────────────────────────────────────────────────────┐
│  S3 GATEWAY ENDPOINT POLICY = ADDITIONAL ALLOWLIST               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Evaluation chain for Lambda → S3 (via Gateway endpoint):        │
│                                                                  │
│  1. SCP              → allows? ✅                                │
│  2. RCP              → allows? ✅                                │
│  3. IAM policy       → allows? ✅                                │
│  4. Bucket policy    → allows? ✅                                │
│  5. ENDPOINT POLICY  → allows? ❌ (PutObject not listed)        │
│                                                                  │
│  Result: Access Denied                                           │
│                                                                  │
│  Default endpoint policy = Allow * (everything passes)           │
│  Hardened endpoint policy = explicit allowlist of actions/buckets │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Rule

> "All IAM correct + bucket policy correct + same account + Access Denied + private subnet"
> = **Check Gateway endpoint policy** (the invisible 6th gate)

### Data Exfiltration Prevention Pattern

```
Endpoint policy:
{
  "Effect": "Allow",
  "Principal": "*",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": ["arn:aws:s3:::my-company-bucket/*"]
}

→ Attacker's own creds trying to upload to external bucket = DENIED
→ Because external bucket ARN is NOT in the endpoint policy
→ Attacker's credentials are irrelevant — network won't carry the request
```

---

## NACL Stateless Reminder

```
SGs = STATEFUL (accepted inbound = auto-allowed return)
NACLs = STATELESS (must explicitly allow BOTH directions)

Flow Log: inbound ACCEPT + outbound REJECT = ALWAYS NACL
(SG would never cause this — stateful handles return traffic)

Fix: Add outbound rule allowing ephemeral ports (1024-65535)
```

---

## 🧠 Cheat-Sheet One-Liners

- **Public IP traffic between EC2s = traverses IGW = SG must allow public IP (not instance ID).**
- **IPv4 outbound-only = NAT Gateway. IPv6 outbound-only = Egress-Only IGW. NAT doesn't support IPv6.**
- **Interface endpoint = TWO SGs (EC2 outbound 443 + endpoint inbound 443). Miss either = timeout.**
- **Gateway endpoint policy = hidden allowlist. All IAM correct + Access Denied = check endpoint policy.**
- **Timeout = network. Access Denied = permissions. The error type tells you where to look.**
- **Flow Log inbound ACCEPT + outbound REJECT = NACL (stateless). Never SG (stateful).**
