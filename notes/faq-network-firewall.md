# FAQ: AWS Network Firewall

> **Blueprint refs:** Task 3.3 (network security controls)
> **Diagram:** [network-firewall-architecture.png](../diagrams/network-firewall-architecture.png)

## What It Does (One-Liner)

**Deep packet inspection for VPC traffic — IDS/IPS, stateful rules, domain filtering.**

Think of it as a managed firewall appliance sitting inline in your subnet.

## K8s Mapping

```
Network Firewall ≈ Calico Enterprise with deep packet inspection
                 ≈ Istio + Envoy with L7 filtering
                 ≈ A dedicated firewall pod inspecting all egress traffic
```

## When to Use (vs Other Services)

| Exam Question Says | Answer | NOT This |
|---|---|---|
| "Inspect traffic content" / "IDS/IPS" | **Network Firewall** | ❌ DNS Firewall (DNS only) |
| "Block traffic matching Suricata signatures" | **Network Firewall** | ❌ WAF (HTTP only) |
| "Filter by domain name in network traffic" | **Network Firewall** (stateful domain rules) | ❌ DNS Firewall (DNS resolution only) |
| "Restrict DNS resolution to specific domains" | ❌ DNS Firewall | NOT Network Firewall |
| "Block SQL injection in HTTP requests" | ❌ WAF | NOT Network Firewall |
| "Allow/deny by IP and port only" | ❌ Security Groups / NACLs | NOT Network Firewall (overkill) |

## How It Works

```
WITHOUT Network Firewall:

  Private Subnet → NAT Gateway → Internet
  (no inspection — anything can leave)

WITH Network Firewall:

  Private Subnet → Firewall Subnet → NAT Gateway → Internet
                   ↑
                   Network Firewall endpoint
                   inspects ALL traffic inline
                   before it leaves your VPC
```

### Architecture (Exam-Critical)

```
┌─────────────────────────────────────────────────┐
│  VPC                                             │
│                                                  │
│  ┌──────────────┐   ┌──────────────────────┐    │
│  │ Private      │   │ Firewall Subnet      │    │
│  │ Subnet       │──►│ (Network Firewall    │    │
│  │ (workloads)  │   │  endpoint per AZ)    │    │
│  └──────────────┘   └──────────┬───────────┘    │
│                                │                 │
│                     ┌──────────▼───────────┐    │
│                     │ Public Subnet        │    │
│                     │ (NAT Gateway / IGW)  │────►  Internet
│                     └──────────────────────┘    │
│                                                  │
└─────────────────────────────────────────────────┘

Traffic flow: Workload → Firewall → NAT → Internet
Route tables direct traffic through the firewall subnet
```

### Rule Types

| Rule Type | What It Does | Example |
|---|---|---|
| **Stateless** | Fast, no connection tracking, evaluated first | Allow/deny by IP, port, protocol (like NACLs) |
| **Stateful** | Connection tracking, deep inspection | Domain filtering, Suricata IDS/IPS rules, TLS inspection |

**Stateful rule groups:**

| Group Type | Use Case |
|---|---|
| **Domain list** | Allow/deny traffic to specific domains (e.g., block `*.evil.com`) |
| **Suricata-compatible IPS** | Import Suricata rules for threat detection signatures |
| **5-tuple** | Source/dest IP, source/dest port, protocol — with connection tracking |

### Processing Order

```
Traffic arrives
  ↓
1. Stateless rules (evaluated first, fast)
   ├── Pass → skip stateful, go to destination
   ├── Drop → blocked
   └── Forward → send to stateful engine
  ↓
2. Stateful rules (deep inspection)
   ├── Alert → log but allow
   ├── Drop → blocked
   └── Pass → allowed
```

## Key Limits/Quotas

| Limit | Value |
|---|---|
| Firewall endpoints per AZ | 1 per firewall per AZ |
| Rule groups per firewall policy | 20 stateless + 20 stateful |
| Rules per stateless group | 100 (capacity units) |
| Rules per stateful group | 30,000 Suricata rules |
| Throughput | Scales automatically (no fixed limit) |
| TLS inspection | ✅ Supported (decrypt, inspect, re-encrypt) |

### Pricing (Exam Gotcha)

- **Endpoint charge**: ~$0.395/hour per AZ (~$288/month per AZ)
- **Data processing**: ~$0.065/GB
- **Expensive compared to DNS Firewall** — only use when you need deep inspection
- Deploy in **each AZ** where you have workloads (one endpoint per AZ)

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Deploy per AZ** | One firewall endpoint per AZ — if you have 3 AZs, you need 3 endpoints |
| **Needs its own subnet** | Firewall endpoints go in a dedicated "firewall subnet" — not the workload subnet |
| **Route tables are critical** | Traffic must be routed THROUGH the firewall subnet — misconfigured routes = bypassed firewall |
| **Stateless evaluated first** | If stateless says "pass," traffic skips stateful entirely |
| **Domain filtering works differently than DNS Firewall** | Network Firewall inspects the actual traffic (SNI in TLS). DNS Firewall filters DNS queries. Both can filter by domain, but at different layers. |
| **TLS inspection** | Can decrypt TLS traffic for deep inspection — requires certificate in ACM |
| **Suricata rules** | Import community or commercial Suricata rule sets for IDS/IPS |
| **Logging** | Sends to CloudWatch Logs, S3, or Kinesis Firehose — same as DNS Firewall |
| **Managed rule groups** | AWS provides managed threat intelligence rules (like WAF managed rules) |

## Network Firewall vs DNS Firewall vs WAF vs Security Groups vs NACLs

| Dimension | Network Firewall | DNS Firewall | WAF | Security Groups | NACLs |
|---|---|---|---|---|---|
| **Layer** | 3-7 | DNS only | 7 (HTTP) | 3-4 | 3-4 |
| **Filters by** | IP, port, domain, content, signatures | Domain name | HTTP headers, body, SQLi, XSS | IP, port | IP, port |
| **Stateful?** | Both stateless + stateful | N/A | N/A | ✅ Stateful | ❌ Stateless |
| **Scope** | Subnet (inline) | VPC | CloudFront/ALB/APIGW | ENI | Subnet |
| **IDS/IPS?** | ✅ Yes (Suricata) | ❌ | ❌ | ❌ | ❌ |
| **Cost** | 💰💰💰 High | 💰 Low | 💰💰 Medium | 🆓 Free | 🆓 Free |
| **Exam signal** | "inspect traffic" | "restrict DNS" | "block SQLi/XSS" | "allow port 443" | "ephemeral ports" |

## Best Practices

1. **Use dedicated firewall subnets** — never mix with workloads
2. **Deploy in all AZs** where you have workloads
3. **Start with alert mode** — monitor before blocking
4. **Use managed rule groups** for threat intelligence
5. **Combine with DNS Firewall** — DNS Firewall for domain resolution, Network Firewall for traffic inspection
6. **Log everything** — CloudWatch Logs for real-time, S3 for archive
