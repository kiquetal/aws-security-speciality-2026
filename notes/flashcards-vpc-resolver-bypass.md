# VPC Resolver Bypass — Flashcard

> GuardDuty + DNS Firewall + Resolver Query Logging ALL depend on VPC Resolver.
> Bypass it = all three go blind. Exam tests this with on-prem AD scenarios.

---

## The Single Point of Dependency

```
VPC Resolver (169.254.169.253) = feeds ALL THREE:
  ├── GuardDuty DNS monitoring (C2 detection, crypto domains)
  ├── Resolver Query Logging (your visibility into DNS queries)
  └── DNS Firewall (block bad domains)

Bypass the Resolver = ALL THREE go dark simultaneously.
```

---

## What Causes Bypass?

| Scenario | Bypasses VPC Resolver? | Why |
|---|---|---|
| Default VPC (no custom DHCP) | ❌ No | Instances use 169.254.169.253 by default |
| Custom DHCP options → on-prem DNS | ✅ YES | Instances query on-prem directly |
| Windows EC2 joined to on-prem AD | ✅ YES | DNS hardcoded to AD domain controllers |
| `enableDnsSupport = false` | ✅ YES | VPC Resolver disabled entirely |
| Route 53 Resolver outbound endpoint | ❌ No | Queries STILL go through VPC Resolver first, then forwarded |

---

## The Fix: Resolver Outbound Endpoint

```
BROKEN (bypass):
  EC2 → on-prem AD DNS directly → GuardDuty blind ❌

FIXED (keep Resolver in the path):
  EC2 → VPC Resolver (GD sees ✅) → Outbound Endpoint → on-prem AD DNS
         169.254.169.253              forwards AD queries only
```

### How to Configure:

1. Create Resolver **outbound endpoint** (ENIs in your VPC)
2. Create **forwarding rules**: `corp.internal` → forward to on-prem AD IPs
3. Remove custom DHCP options (use VPC default DNS)
4. Result: ALL DNS goes through VPC Resolver. AD queries forwarded. GuardDuty sees everything.

---

## Exam Scenarios

| Question Pattern | Answer |
|---|---|
| "GuardDuty not seeing DNS logs, Windows EC2, on-prem AD" | Custom DNS bypasses VPC Resolver. Fix: Resolver outbound endpoint. |
| "DNS Firewall rules not blocking anything, on-prem DNS" | Same cause. Instances bypass DNS Firewall. |
| "Resolver Query Logs empty despite active instances" | Instances using custom DNS, not VPC Resolver. |
| "GuardDuty DNS findings work for Linux but not Windows" | Windows joined to AD = DNS points to AD servers. |

---

## The Mental Model

```
169.254.169.253 = the security camera on your DNS

If traffic goes through it → you see everything (GD, logging, firewall)
If traffic bypasses it → you're blind

On-prem AD DNS = a back door that bypasses the camera
Fix = Route 53 Resolver outbound endpoint (keeps camera in the path)
```

---

## Quick Recall

```
Q: GuardDuty DNS monitoring not working. Windows EC2 + on-prem AD. Fix?
A: Instances bypass VPC Resolver (use AD DNS directly).
   Fix: Remove custom DHCP options + Resolver outbound endpoint for AD domains.

Q: What THREE services go blind when VPC Resolver is bypassed?
A: GuardDuty DNS + Resolver Query Logging + DNS Firewall

Q: Does Resolver outbound endpoint fix the bypass?
A: YES — queries still go through VPC Resolver FIRST, then get forwarded.

Q: enableDnsSupport = false. What breaks?
A: Everything DNS — VPC Resolver off = no resolution + GD/Firewall/Logging all dead.
```

---

## GuardDuty Data Sources — Complete List

```
FOUNDATIONAL (always on, can't disable):
  ├── CloudTrail management events (API calls)
  ├── VPC Flow Logs (network traffic metadata)
  └── DNS logs (domain queries via VPC Resolver) ← YES, DNS IS INCLUDED

OPTIONAL PROTECTION PLANS (enable per feature):
  ├── S3 Protection (CloudTrail S3 data events)
  ├── EKS Audit Log Monitoring (K8s API server logs)
  ├── EKS/EC2/ECS Runtime Monitoring (needs agent)
  ├── RDS Protection (Aurora login events)
  ├── Lambda Protection (Lambda network activity)
  └── Malware Protection (EBS/S3 scanning)
```

### Exam Trap: "GuardDuty doesn't analyze DNS logs"

```
❌ WRONG. DNS logs are a FOUNDATIONAL source (always on).
✅ GuardDuty reads DNS from VPC Resolver (169.254.169.253).
✅ This is how it detects: C2 domains, crypto mining domains, DNS exfil.

The ONLY reason GuardDuty wouldn't see DNS:
  → Instances BYPASS VPC Resolver (custom DHCP / on-prem AD DNS)
  → NOT because GuardDuty doesn't support DNS
```

---

## 🧠 Cheat-Sheet One-Liners

- **VPC Resolver (169.254.169.253) = single feed for GuardDuty DNS + DNS Firewall + Resolver Logging. Bypass it = all three blind.**
- **On-prem AD DNS / custom DHCP = bypass. Fix = Resolver outbound endpoint (keeps Resolver in the path).**
- **"GuardDuty DNS not working + Windows + AD" = instances using AD DNS directly, bypassing VPC Resolver.**
- **GuardDuty foundational = CloudTrail + VPC Flow Logs + DNS. All three ALWAYS ON. "GD doesn't analyze DNS" = WRONG distractor.**
