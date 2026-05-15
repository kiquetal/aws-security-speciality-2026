# FAQ: Nitro Inter-Instance Encryption

> **Blueprint refs:** Task 5.1.3 (inter-resource encryption in transit)
> **New in C03:** Yes — brand new, no C02 precedent

## One-Liner

**Automatic, hardware-level encryption of traffic between EC2 instances — zero config, zero app changes.**

## The Problem It Solves

```
WITHOUT Nitro encryption:
  EC2 (AZ-a) ──── plaintext traffic ────► EC2 (AZ-b)
  EKS node   ──── plaintext pod traffic ──► EKS node
  → Traffic visible to anyone on the physical network
  → Requires app-level TLS (mTLS, Istio, etc.) to encrypt

WITH Nitro encryption:
  EC2 (AZ-a) ════ encrypted at hardware ══► EC2 (AZ-b)
  EKS node   ════ encrypted at hardware ══► EKS node
  → Automatic, no app changes, no performance impact
  → Nitro card handles encryption/decryption in hardware
```

## How It Works

```
┌──────────────────┐                    ┌──────────────────┐
│  EC2 Instance A  │                    │  EC2 Instance B  │
│  (Nitro-based)   │                    │  (Nitro-based)   │
│                  │                    │                  │
│  App sends       │                    │  App receives    │
│  plaintext       │                    │  plaintext       │
│       │          │                    │       ▲          │
│       ▼          │                    │       │          │
│  ┌────────────┐  │                    │  ┌────────────┐  │
│  │ Nitro Card │  │                    │  │ Nitro Card │  │
│  │ encrypts   │──┼── encrypted ───────┼──│ decrypts   │  │
│  └────────────┘  │   on the wire      │  └────────────┘  │
└──────────────────┘                    └──────────────────┘

Key points:
├── Encryption happens BELOW the OS — app never sees it
├── No certificates, no key management, no config
├── Only works between Nitro-based instance types
└── Covers ALL traffic between instances (any port, any protocol)
```

## What It Covers

| Traffic Type | Encrypted? | Notes |
|---|---|---|
| EC2 → EC2 (same VPC) | ✅ | Both must be Nitro-based |
| EC2 → EC2 (cross-AZ) | ✅ | Same region |
| EKS node → EKS node | ✅ | Pod-to-pod across nodes |
| EMR node → EMR node | ✅ | Spark shuffle traffic |
| SageMaker training nodes | ✅ | Distributed training |
| EC2 → RDS | ❌ | RDS is managed — use TLS |
| EC2 → S3 | ❌ | Use HTTPS (TLS) |
| EC2 → non-Nitro EC2 | ❌ | Both sides must be Nitro |

## Nitro-Based Instance Types (Know the Pattern)

```
Nitro-based (supports inter-instance encryption):
├── C5, C5n, C6g, C6i, C7g, C7i
├── M5, M5n, M6g, M6i, M7g, M7i
├── R5, R5n, R6g, R6i, R7g, R7i
├── T3, T3a, T4g
├── P4, P5 (GPU)
├── Graviton (all generations)
└── Basically: anything 5th gen or newer

NOT Nitro (no inter-instance encryption):
├── T2, M4, C4, R4
├── Anything 4th gen or older
└── Previous-generation instances
```

> **Exam rule:** You don't need to memorize instance types. Just know: "modern instances (5th gen+) = Nitro = automatic encryption."

## Key Limits/Quotas

| Limit | Value |
|---|---|
| Performance impact | None (hardware-accelerated) |
| Configuration needed | None (automatic) |
| Key management | None (AWS handles internally) |
| Supported protocols | ALL (TCP, UDP, ICMP — everything) |
| Cross-region | ❌ Same region only |
| Cross-VPC (peering/TGW) | ✅ Yes, if both sides are Nitro |
| Cost | Free (included with Nitro instances) |

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Zero config** | No setup, no opt-in, no certificates — just use Nitro instances |
| **Both sides must be Nitro** | If one side is non-Nitro, traffic is NOT encrypted |
| **Doesn't replace TLS** | For traffic to managed services (RDS, S3, ElastiCache), still use TLS |
| **Not visible to the OS** | `tcpdump` on the instance sees plaintext — encryption is below the OS |
| **Complements app-level TLS** | Defense in depth — Nitro encrypts the wire, TLS encrypts the session |
| **EKS inter-node** | Pod traffic between nodes is encrypted if nodes are Nitro |
| **No CloudTrail logging** | Hardware-level — no API calls, no audit trail of encryption itself |

## Nitro vs Other Encryption-in-Transit Options

| Method | Scope | Config | Performance | Use Case |
|---|---|---|---|---|
| **Nitro** | Instance-to-instance | Zero | Zero impact | Default for all inter-instance traffic |
| **TLS (app-level)** | App-to-app | Certificates needed | Small overhead | Managed services, cross-service |
| **IPsec (VPN)** | Network-to-network | Tunnel config | Moderate overhead | Hybrid/on-prem connectivity |
| **MACsec** | DX connection | Dedicated DX only | Zero impact | Layer 2 on Direct Connect |

## K8s Mapping

```
Nitro encryption  ≈  WireGuard/Calico encryption between nodes
                  ≈  Istio mTLS but at the hypervisor level
                  ≈  "Encrypt everything" without sidecar overhead

Key difference: Istio mTLS requires sidecars + cert management.
Nitro encryption requires NOTHING — it's the network fabric itself.
```

## 🧠 Cheat-Sheet One-Liners

- **"Encrypt between instances, no app changes" = Nitro inter-instance encryption.** Automatic, hardware-level, zero config.
- **Both sides must be Nitro-based (5th gen+).** Non-Nitro instance on either end = no encryption.
- **Doesn't replace TLS to managed services.** EC2→RDS still needs TLS. Nitro only covers instance-to-instance.
- **Covers EC2-to-EC2, EKS inter-node, EMR, SageMaker.** Any Nitro-to-Nitro traffic in same region.
