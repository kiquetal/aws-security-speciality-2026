# FAQ: Hybrid & Remote Connectivity

> **Blueprint refs:** Task 3.3 (secure connectivity between hybrid/multi-cloud), Task 5.1 (data in transit)
> **Diagram:** [hybrid-connectivity-decision.png](../diagrams/hybrid-connectivity-decision.png)

## Decision Table (Exam-Critical)

| Exam Signal | Answer | Why |
|---|---|---|
| "on-prem to AWS, quick/backup/encrypted over internet" | **Site-to-Site VPN** | IPsec tunnel over public internet, minutes to set up |
| "dedicated, high-throughput, private, consistent latency" | **Direct Connect** | Physical fiber, no internet involved, 1/10/100 Gbps |
| "many VPCs + on-prem all interconnected" | **Transit Gateway** | Hub-and-spoke, avoids N×N peering mesh |
| "employees access entire VPC from laptops" | **Client VPN** | OpenVPN-based, full network access, per-user |
| "access specific internal apps, no full network access, zero-trust" | **Verified Access** | Per-app access, evaluates identity + device posture, no VPN client needed |

## Key Distinction: Client VPN vs Verified Access

```
Client VPN:
  Employee laptop ──IPsec tunnel──► entire VPC network
  ├── Full network-level access (like being on the LAN)
  ├── Needs VPN client installed
  ├── Traditional approach
  └── Exam signal: "full network access" / "remote workforce VPN"

Verified Access:
  Employee browser ──HTTPS──► specific internal app only
  ├── Per-application access (not network-level)
  ├── No VPN client needed (browser-based)
  ├── Evaluates: identity (IdP) + device posture (MDM)
  ├── Zero-trust model
  └── Exam signal: "zero-trust" / "specific apps" / "without VPN"
```

## Encryption on Direct Connect (Exam Trap)

```
Direct Connect ALONE = NOT encrypted (private, but plaintext on the fiber)

To encrypt Direct Connect traffic:

Option 1: MACsec (Layer 2)
  ├── Dedicated connections ONLY (not hosted)
  ├── Line-rate encryption, zero overhead
  ├── Point-to-point (DX location ↔ AWS)
  └── Exam signal: "Layer 2 encryption" / "dedicated DX"

Option 2: Site-to-Site VPN over DX (Layer 3)
  ├── Works on dedicated OR hosted connections
  ├── IPsec tunnel rides over the DX link
  ├── Some overhead (encryption/decryption)
  └── Exam signal: "encrypt DX" + "hosted connection"
```

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **DX alone ≠ encrypted** | Private ≠ encrypted. Must add MACsec or VPN. |
| **MACsec = dedicated only** | Hosted connections can't use MACsec — use VPN over DX instead |
| **Transit Gateway = hub** | Connects VPCs + VPNs + DX in one place. Shared via RAM. |
| **Client VPN ≠ Verified Access** | VPN = full network tunnel. VA = per-app, zero-trust, no client. |
| **Verified Access = no VPN client** | Browser-based, evaluates identity + device posture per request |
| **Site-to-Site VPN = backup for DX** | Common pattern: DX primary + VPN failover |

## 🧠 Cheat-Sheet One-Liners

- **MACsec = Layer 2 encryption on dedicated Direct Connect only.** Hosted connection → Site-to-Site VPN over DX (IPsec).
- **Client VPN = full network tunnel. Verified Access = per-app zero-trust, no client.**
- **Direct Connect alone is NOT encrypted.** Private ≠ encrypted.
