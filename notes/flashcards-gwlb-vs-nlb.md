# GWLB vs NLB vs ALB

> "NLB = load balance your APP. GWLB = load balance your FIREWALL."

---

## Side-by-Side

| | ALB | NLB | GWLB |
|---|---|---|---|
| **Layer** | 7 (HTTP/HTTPS) | 4 (TCP/UDP/TLS) | 3 (IP packets) |
| **Purpose** | Route HTTP requests to app targets | Route TCP connections to app targets | Route ALL traffic THROUGH security appliances |
| **Sees** | HTTP headers, paths, methods | TCP/UDP flows | Raw IP packets (GENEVE encapsulated) |
| **Use case** | Web apps, microservices | Databases, gaming, non-HTTP | **Firewalls, IDS/IPS, DLP** |
| **Transparent?** | ❌ (terminates connection) | ❌ (terminates connection) | ✅ (transparent bump-in-the-wire) |
| **Protocol** | HTTP/HTTPS/gRPC | TCP/UDP/TLS | GENEVE (port 6081) |

---

## The Core Distinction

```
NLB = traffic goes TO your targets (targets are the DESTINATION)
      Client → NLB → Your App
      "Load balance my application"

GWLB = traffic goes THROUGH your targets (targets INSPECT then forward)
       Client → GWLB → Firewall appliance → GWLB → Destination
       "Inspect my traffic with a security appliance"
```

---

## Exam Signals

| Question says | Answer |
|---|---|
| "Non-HTTP protocol, load balance" | **NLB** |
| "TLS termination on port 6379/9100/any" | **NLB** |
| "Third-party firewall/IDS, inline, transparent" | **GWLB** |
| "Palo Alto / Fortinet / Check Point appliances" | **GWLB** |
| "Inspect traffic without changing source IP" | **GWLB** (transparent) |
| "Scale security appliances + health check" | **GWLB** |
| "Traffic Mirroring destination" | **NLB** (passive IDS target) |

---

## Traffic Mirroring + NLB — How They Work Together

```
Traffic Mirroring ≠ NLB. They're different things that COLLABORATE:

Normal traffic (unaffected):
  Client ──► EC2 instance (production, keeps working)

Mirrored copy (passive observation):
  EC2 ENI ──(VXLAN copy)──► NLB ──► IDS EC2 fleet (observes only)
                             ^^^
                        NLB = cable delivering footage
                        to the monitoring room

Traffic Mirroring = the CAMERA (copies packets)
NLB               = the CABLE (distributes copies to IDS fleet)
IDS tool          = the MONITOR (analyzes the footage)
```

| | Traffic Mirroring | NLB (as mirror target) |
|---|---|---|
| **What it is** | Feature that COPIES packets from an ENI | Load balancer receiving the copies |
| **Does it block?** | ❌ Never | N/A (just distributes) |
| **If it fails** | Production unaffected (copy stops) | IDS stops receiving (production fine) |
| **Encapsulation** | VXLAN (IDS must decapsulate) | Passes VXLAN to targets |

**Key exam trap:** "Traffic Mirroring destination" = NLB (or ENI). NOT GWLB. NOT Network Firewall. Mirroring is passive — it sends COPIES to an NLB target group of IDS instances.

---

## GWLB GENEVE Trap

Appliance logs show GWLB endpoint IP instead of client → appliance must **decapsulate GENEVE outer header** to see original packet inside. NOT X-Forwarded-For (that's ALB/HTTP only).

---

## Three Inspection Patterns

```
PASSIVE (copy, no block):     Traffic Mirroring → NLB → IDS
INLINE (inspect + block):     GWLB → third-party appliance (Palo Alto)
INLINE (AWS-native IPS):      Network Firewall (Suricata rules)
```

| Pattern | Blocks? | Production risk if fails? | Tool |
|---|---|---|---|
| Traffic Mirroring | ❌ Never | Zero | Copy to NLB |
| GWLB | ✅ Yes | Traffic stops | Third-party |
| Network Firewall | ✅ Yes | Traffic stops | AWS native |
