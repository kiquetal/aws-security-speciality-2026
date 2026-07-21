# GWLB vs Traffic Mirroring vs Network Firewall — Flashcard

> Three ways to inspect traffic. The difference: INLINE vs PASSIVE vs AWS-NATIVE.
> Failed 3x on Dojo (Q1126). Lock this.

---

## The Three Inspection Patterns

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. TRAFFIC MIRRORING (passive copy)                              │
│                                                                  │
│    Mode: PASSIVE — copies packets, never blocks                  │
│    Encapsulation: VXLAN                                          │
│    Target: NLB or ENI → IDS tool                                 │
│    Production impact: ZERO (copy fails = nothing happens)        │
│    Use: IDS, forensics, content inspection, recording            │
│                                                                  │
│    Analogy: security camera (watches, doesn't stop anyone)       │
│                                                                  │
│    ┌──────┐ normal ──────────────► destination                   │
│    │ ENI  │                                                      │
│    │      │ copy (VXLAN) ────────► NLB → IDS (observes)          │
│    └──────┘                                                      │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 2. GWLB + GENEVE (inline third-party appliance)                  │
│                                                                  │
│    Mode: INLINE — traffic routed THROUGH appliance               │
│    Encapsulation: GENEVE (preserves original headers)            │
│    Target: GWLB endpoint → third-party appliance (Palo Alto etc) │
│    Production impact: HIGH (appliance dies = traffic stops)       │
│    Use: IPS, third-party firewall, deep inspection + blocking    │
│                                                                  │
│    Analogy: security guard at door (inspects AND blocks)         │
│                                                                  │
│    source ──► GWLB endpoint ──► appliance ──► GWLB ──► dest     │
│                                    │                             │
│                                    └── decides: allow or DROP    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 3. AWS NETWORK FIREWALL (inline AWS-native)                      │
│                                                                  │
│    Mode: INLINE — traffic routed through firewall subnet         │
│    Encapsulation: none (AWS manages internally)                   │
│    Rules: Suricata (alert or drop)                               │
│    Production impact: HIGH (firewall down = traffic stops)        │
│    Use: IPS, domain filtering, TLS inspection — ALL AWS-NATIVE   │
│                                                                  │
│    Analogy: built-in building security (no external contractor)  │
│                                                                  │
│    source ──► firewall subnet ──► Network Firewall ──► dest      │
│                                         │                        │
│                                         └── Suricata: alert/drop │
└─────────────────────────────────────────────────────────────────┘
```

---

## Quick Comparison

| Dimension | Traffic Mirroring | GWLB | Network Firewall |
|---|---|---|---|
| **Mode** | Passive (copy) | Inline (route through) | Inline (route through) |
| **Blocks traffic?** | ❌ Never | ✅ Yes | ✅ Yes |
| **Encapsulation** | VXLAN | GENEVE | None (native) |
| **Target** | NLB / ENI | Third-party appliance | AWS-managed |
| **Appliance** | Your IDS tool | Palo Alto, Fortinet, etc | Suricata (built-in) |
| **If it fails** | Nothing (copy stops, traffic fine) | Traffic stops | Traffic stops |
| **Cost** | Low (per session) | High (per AZ + GB) | High (per AZ + GB) |
| **Use case** | IDS / forensics / record | Third-party IPS | AWS-native IPS |

---

## Exam Decision (Memorize This)

| Signal in Question | Answer |
|---|---|
| "Content inspection" / "observe" / "IDS" / "without blocking" | **Traffic Mirroring** |
| "Third-party appliance" / "Palo Alto" / "inline" / "scale + health check" | **GWLB** |
| "Suricata rules" / "IPS" / "TLS inspection" / "AWS-native" | **Network Firewall** |
| "Block + drop malicious traffic" (no third-party mentioned) | **Network Firewall** |
| "Block + drop" + "Palo Alto/Fortinet" | **GWLB** |
| "Full packet payload" + "passive" | **Traffic Mirroring** |
| "GENEVE decapsulation" | **GWLB** |
| "VXLAN" | **Traffic Mirroring** |

---

## Decapsulation Trap

```
GWLB appliance logs show GWLB IP instead of client IP:
  → Appliance must decapsulate GENEVE outer header
  → Original packet (with real client IP) is INSIDE the tunnel
  → Fix: configure appliance to strip GENEVE, read inner packet

Traffic Mirroring IDS shows NLB IP instead of source:
  → IDS must decapsulate VXLAN outer header
  → Original packet is INSIDE the VXLAN tunnel
  → Same concept, different encapsulation
```

---

## Mnemonic

```
MIRROR = CAMERA (watches, VXLAN, NLB, passive)
GWLB   = GUARD (blocks, GENEVE, third-party, inline)
NF     = BOUNCER (blocks, Suricata, AWS-native, inline)
```

---

## Traffic Mirroring vs VPC Flow Logs (4x Failed!)

```
VPC Flow Logs = METADATA ONLY
  → Source IP, dest IP, port, protocol, accept/reject
  → NO packet payload, NO content, NO headers
  → Use: "who talked to whom" / "top talkers" / "was it accepted?"

Traffic Mirroring = FULL PACKET COPY
  → Complete packet including payload
  → Encapsulated in VXLAN → sent to NLB → IDS fleet
  → Use: "inspect content" / "IDS" / "full packet" / "network-layer attacks"

┌──────────────────────────────────────────────────────────┐
│  "Full packet" / "inspect content" / "IDS" / "payload"   │
│  = Traffic Mirroring (ALWAYS)                            │
│                                                           │
│  "Metadata" / "who talked to whom" / "top talkers"       │
│  = VPC Flow Logs                                         │
│                                                           │
│  Flow Logs CANNOT do content inspection. Period.          │
└──────────────────────────────────────────────────────────┘
```

### Your Error Pattern (4x)

```
Dojo Q1126 (original): picked GWLB      → should be Traffic Mirroring (passive)
Dojo Q1126 (re-test):  picked GWLB      → should be Traffic Mirroring (passive)
Udemy Q30 (original):  picked GWLB      → should be Traffic Mirroring (passive)
Udemy Q29 (retake):    picked Flow Logs  → should be Traffic Mirroring (full packet)

SIGNAL: "full packet" + "passive" + "IDS" + "without blocking" = Traffic Mirroring
        NEVER Flow Logs (metadata only)
        NEVER GWLB (inline, not passive)
```
