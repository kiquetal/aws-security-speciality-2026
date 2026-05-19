# Hybrid Connectivity — Slide Deck

---

## The 5 Options

```
On-prem → AWS:
├── Site-to-Site VPN     → IPsec over internet (quick, cheap)
├── Direct Connect (DX)  → dedicated fiber (fast, private, expensive)
└── Transit Gateway      → hub connecting VPCs + VPN + DX

Remote users → AWS:
├── Client VPN           → full network tunnel (like OpenVPN)
└── Verified Access      → per-app, zero-trust, no VPN client
```

---

## Site-to-Site VPN

```
On-prem ──── IPsec tunnel ────► AWS VPC
             (over internet)

├── Minutes to set up
├── Encrypted (IPsec)
├── Backup for Direct Connect
└── ~1.25 Gbps max per tunnel (2 tunnels = HA)
```

Exam signal: "quick" / "backup" / "encrypted over internet"

---

## Direct Connect (DX)

```
On-prem ──── physical fiber ────► AWS
             (private, no internet)

├── 1 / 10 / 100 Gbps
├── Consistent latency
├── NOT encrypted by default!
└── Weeks to provision
```

🧠 **Private ≠ encrypted.** DX alone is plaintext on the fiber.

---

## Encrypting Direct Connect

```
Option 1: MACsec (Layer 2)
  ├── Dedicated connections ONLY
  ├── Line-rate, zero overhead
  └── Point-to-point encryption

Option 2: Site-to-Site VPN over DX (Layer 3)
  ├── Works on dedicated OR hosted
  ├── IPsec tunnel rides over DX
  └── Some overhead
```

| | MACsec | VPN over DX |
|---|---|---|
| **Connection type** | Dedicated only | Any |
| **Layer** | 2 | 3 |
| **Overhead** | Zero | Some |
| **Exam signal** | "Layer 2" + "dedicated" | "encrypt DX" + "hosted" |

---

## Transit Gateway

```
         ┌── VPC A
         ├── VPC B
TGW ─────├── VPC C
         ├── Site-to-Site VPN
         └── Direct Connect

= Hub-and-spoke (no N×N peering mesh)
```

- Shared via **RAM** across accounts
- Exam signal: "many VPCs + on-prem interconnected"

---

## Client VPN vs Verified Access

```
Client VPN:
  Laptop ──IPsec tunnel──► ENTIRE VPC network
  ├── Full network access (like being on the LAN)
  ├── Needs VPN client installed
  └── Traditional approach

Verified Access:
  Browser ──HTTPS──► SPECIFIC internal app only
  ├── Per-application (not network-level)
  ├── No VPN client needed
  ├── Evaluates: identity (IdP) + device posture (MDM)
  └── Zero-trust model
```

---

## Client VPN vs Verified Access — Decision

| Signal | Answer |
|---|---|
| "Full network access" / "remote workforce VPN" | **Client VPN** |
| "Zero-trust" / "specific apps" / "without VPN" | **Verified Access** |
| "Evaluate device posture" | **Verified Access** |
| "No client software" / "browser-based" | **Verified Access** |

🧠 VPN = network tunnel. Verified Access = per-app, no client.

---

## Exam Decision Table

| Signal | Answer |
|---|---|
| "On-prem to AWS, quick, over internet" | **Site-to-Site VPN** |
| "Dedicated, high-throughput, private" | **Direct Connect** |
| "Layer 2 encryption on dedicated DX" | **MACsec** |
| "Encrypt hosted DX connection" | **VPN over DX** |
| "Many VPCs + on-prem all connected" | **Transit Gateway** |
| "Employees access entire VPC" | **Client VPN** |
| "Access specific internal apps, zero-trust" | **Verified Access** |

---

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **DX alone ≠ encrypted** | Must add MACsec or VPN |
| **MACsec = dedicated only** | Hosted connections can't use MACsec |
| **TGW shared via RAM** | Cross-account hub connectivity |
| **Client VPN ≠ Verified Access** | Network tunnel vs per-app zero-trust |
| **Verified Access = no client** | Browser-based, evaluates identity + device |
| **VPN = backup for DX** | Common pattern: DX primary + VPN failover |

---

## K8s Mapping

```
Client VPN       ≈  kubectl via VPN tunnel to cluster
Verified Access  ≈  Teleport / Boundary (per-app access, identity-aware)
Transit Gateway  ≈  Service mesh gateway connecting multiple clusters
MACsec           ≈  WireGuard on the physical link
```

---

## 🧠 One-Liners

- **MACsec = Layer 2 on dedicated DX only.** Hosted → VPN over DX.
- **Client VPN = full tunnel. Verified Access = per-app, no client, zero-trust.**
- **DX alone is NOT encrypted.** Private ≠ encrypted.
- **Transit Gateway shared via RAM.** Hub-and-spoke for multi-VPC + on-prem.
