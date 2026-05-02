# FAQ: Route 53 Resolver — DNS Firewall & Resolver Logs

> **Blueprint refs:** Task 3.3 (network security controls), Task 1.2 (logging solutions)
> **Diagram:** [route53-dns-firewall.png](../diagrams/route53-dns-firewall.png)

## Where DNS Firewall Lives (Don't Confuse the Names)

```
Route 53 (the overall service)
├── Route 53 Hosted Zones     ← DNS records (A, CNAME, etc.)
├── Route 53 Health Checks    ← endpoint monitoring
└── Route 53 Resolver         ← VPC DNS resolution
    ├── Resolver Endpoints    ← inbound/outbound DNS forwarding
    ├── Resolver Query Logs   ← log every DNS query
    └── Resolver DNS Firewall ← filter/block DNS queries
```

Full name: **Amazon Route 53 Resolver DNS Firewall**. Exam and docs shorten it to "DNS Firewall."

### Three AWS "Firewalls" — Don't Confuse Them

| Name | What It Filters | Layer | Scope | Exam Signal |
|---|---|---|---|---|
| **Route 53 Resolver DNS Firewall** | DNS queries (domain names) | DNS only | VPC-level | "restrict domain resolution" |
| **AWS Network Firewall** | Network traffic (IP, port, protocol, DPI) | Layer 3-7 | Subnet-level | "inspect traffic / IDS/IPS" |
| **AWS WAF** | HTTP/HTTPS requests (headers, body, SQLi, XSS) | Layer 7 (HTTP) | CloudFront, ALB, API GW | "block SQL injection / rate limit" |

> These are three completely different services at different layers. The exam uses them as distractors.

---

## Route 53 Resolver DNS Firewall (Task 3.3)

### What Problem It Solves

Resources in your VPC can resolve ANY domain by default. DNS Firewall lets you
control which domains can be resolved — blocking data exfiltration via DNS,
restricting outbound access, and enforcing allow-lists.

```
WITHOUT DNS Firewall:

  Lambda ──DNS──► Route 53 Resolver ──► api.partner.com     ✅ resolves
  Lambda ──DNS──► Route 53 Resolver ──► evil.com             ✅ also resolves
  Lambda ──DNS──► Route 53 Resolver ──► data-exfil.attacker.com  ✅ resolves too

WITH DNS Firewall:

  Rule Group:
    Rule 1: ALLOW  api.partner.com
    Rule 2: BLOCK  * (everything else)

  Lambda ──DNS──► DNS Firewall ──► api.partner.com           ✅ ALLOWED
  Lambda ──DNS──► DNS Firewall ──► evil.com                  ❌ BLOCKED
  Lambda ──DNS──► DNS Firewall ──► data-exfil.attacker.com   ❌ BLOCKED
```

### How It Works

1. Create a **rule group** with domain lists + actions (ALLOW, BLOCK, ALERT)
2. **Associate** the rule group with your VPC
3. All DNS queries from the VPC pass through the firewall rules
4. Rules evaluated in priority order (lowest number = highest priority)

### Rule Actions

| Action | What Happens | Use Case |
|---|---|---|
| **ALLOW** | DNS query resolves normally | Approved domains |
| **BLOCK** | DNS query blocked, returns NXDOMAIN or custom response | Everything else |
| **ALERT** | DNS query resolves BUT logs a finding | Monitor before blocking |

### Domain Lists

- **AWS Managed Domain Lists** (free, updated by AWS):
  - Malware domains
  - Botnet C2 domains
  - Newly observed domains (suspicious)
- **Custom Domain Lists**: Your own allow/deny lists

### Example: Restrict Lambda to One Partner Domain

```
Rule Group (priority order):
  Priority 1: ALLOW  api.partner.com        ← only this
  Priority 2: ALLOW  secretsmanager.us-east-1.amazonaws.com  ← AWS services
  Priority 3: ALLOW  kms.us-east-1.amazonaws.com             ← AWS services
  Priority 4: BLOCK  *                      ← deny everything else
```

> ⚠️ Don't forget to allow AWS service domains if your Lambda uses
> Secrets Manager, KMS, S3, etc. via VPC endpoints — those need DNS too.

### DNS Firewall vs Network Firewall vs Security Groups

| Dimension | DNS Firewall | Network Firewall | Security Groups |
|---|---|---|---|
| **Filters by** | Domain name | IP, port, protocol, domain (stateful rules) | IP, port, protocol |
| **Layer** | DNS (Layer 7 — domain only) | Network (Layer 3-7) | Network (Layer 3-4) |
| **Scope** | VPC-level | Subnet-level (inline) | ENI-level |
| **Cost** | Low | High (per GB processed) | Free |
| **Use case** | "Block DNS lookups to bad domains" | "Deep packet inspection, IDS/IPS" | "Allow port 443 from this CIDR" |
| **Overhead** | Minimal — managed rules | Medium — deploy endpoints per AZ | Minimal |

> **Exam signal:** "limit domain lookup" or "restrict DNS resolution" → **DNS Firewall**.
> "Inspect traffic content" or "IDS/IPS" → **Network Firewall**.
> "Allow/deny by IP and port" → **Security Groups / NACLs**.

### Exam Gotchas

- **VPC-level** — associate rule group with VPC, applies to all resources
- **Works with Resolver outbound endpoints** — filters queries before forwarding
- **Priority matters** — rules evaluated lowest number first, first match wins
- **Fail-open vs fail-closed** — configurable: if DNS Firewall fails, allow or block all queries?
- **Cannot filter by source IP within VPC** — all resources in the VPC get the same rules
- **Cross-account via RAM** — share rule groups across accounts using AWS RAM

### K8s Mapping
- **DNS Firewall ≈ CoreDNS policy plugin** or **Istio ServiceEntry** — restrict which external domains pods can resolve
- **BLOCK action ≈ Kubernetes NetworkPolicy egress DNS restriction**
- **ALERT action ≈ Falco DNS monitoring** — observe before enforcing

---

## Route 53 Resolver Query Logs (Task 1.2)

### What They Capture

Every DNS query made by resources in your VPC — what domain was looked up,
by which resource, and what was the response.

```
Resolver Query Log entry:
  ├── Timestamp
  ├── Source IP (which resource made the query)
  ├── Query name (e.g., api.partner.com)
  ├── Query type (A, AAAA, CNAME, MX, etc.)
  ├── Response code (NOERROR, NXDOMAIN, SERVFAIL)
  ├── VPC ID
  ├── Resolver endpoint ID (if using outbound/inbound endpoints)
  └── DNS Firewall rule action (ALLOW, BLOCK, ALERT — if firewall enabled)
```

### Log Destinations

| Destination | Use Case | Latency |
|---|---|---|
| **CloudWatch Logs** | Real-time monitoring, metric filters, alarms | Near real-time |
| **S3** | Long-term archive, Athena queries | Minutes |
| **Kinesis Data Firehose** | Stream to third-party SIEM (Splunk, Datadog) | Near real-time |

### Security Use Cases

1. **Detect DNS exfiltration** — unusually long subdomain queries (e.g., `encoded-data.evil.com`)
2. **Detect C2 communication** — queries to known malicious domains
3. **Audit outbound access** — which resources are resolving which domains
4. **Troubleshoot DNS Firewall** — see which queries were blocked/allowed
5. **Feed into GuardDuty** — GuardDuty uses DNS logs as a foundational data source
6. **Compliance** — prove that only approved domains are being resolved

### Resolver Logs vs VPC Flow Logs vs CloudTrail

| Log Type | What It Captures | DNS Info? |
|---|---|---|
| **Resolver Query Logs** | DNS queries (domain, response, source) | ✅ Full domain name |
| **VPC Flow Logs** | Network traffic (IP, port, bytes, accept/reject) | ❌ No domain — only IP:port |
| **CloudTrail** | AWS API calls (who did what) | ❌ No DNS queries |

> **Exam signal:** "Which resource is querying which domain?" → **Resolver Query Logs**.
> "What IP traffic was accepted/rejected?" → **VPC Flow Logs**.
> "Who called which AWS API?" → **CloudTrail**.

### Key Limits/Quotas

| Limit | Value |
|---|---|
| Log configs per region | 10 |
| VPCs per log config | Unlimited |
| Log destinations | CloudWatch Logs, S3, Kinesis Data Firehose |
| Cross-account sharing | ✅ Via RAM (share log config with other accounts) |

### Exam Gotchas

- **Not enabled by default** — must create a query log config and associate with VPC
- **Per-VPC association** — each VPC must be explicitly associated
- **GuardDuty reads DNS logs independently** — you don't need to enable Resolver logs for GuardDuty to work
- **DNS Firewall actions appear in logs** — if DNS Firewall is enabled, logs show ALLOW/BLOCK/ALERT per query
- **Cross-account via RAM** — share log configs across accounts in your org
- **OCSF format** — Resolver logs can be ingested into Security Lake in OCSF format (new in C03, Task 3.1.4)

### Integration with Other Services

| Service | How It Uses Resolver Logs |
|---|---|
| **GuardDuty** | Reads DNS logs directly (foundational source) — detects C2, crypto mining domains |
| **Security Lake** | Ingests in OCSF format for centralized analysis |
| **CloudWatch Logs** | Real-time metric filters + alarms on suspicious domains |
| **Athena** | SQL queries on S3-stored logs for investigation |
| **Detective** | Correlates DNS activity during incident investigation |

### Example: Alert on Queries to Non-Approved Domains

```
CloudWatch Logs Metric Filter:
  Filter pattern: { $.queryName != "api.partner.com" && $.queryName != "*.amazonaws.com" }
  → CloudWatch Alarm → SNS → Security Team
```

### Best Practices

1. **Enable Resolver Query Logs** in all VPCs — DNS is a blind spot without them
2. **Send to CloudWatch Logs** for real-time alerting + S3 for long-term archive
3. **Combine with DNS Firewall** — firewall blocks, logs prove it
4. **Feed into Security Lake** for OCSF-normalized cross-service analysis
5. **Monitor for DNS tunneling** — unusually long subdomain queries or high query volume to single domain
