# FAQ: Amazon Security Lake

> **Blueprint refs:** Task 1.2 (log storage and data lakes), Task 3.1.4 (OCSF ingestion)
> **New in C03:** Yes — OCSF format is explicitly testable
> **Diagram:** [security-lake-architecture.mmd](../diagrams/security-lake-architecture.mmd)

## One-Liner

**Centralized security data lake — normalizes ALL log sources into OCSF format in YOUR S3 bucket.**

## The Problem It Solves

```
WITHOUT Security Lake:
  CloudTrail logs → S3 (JSON format A)
  VPC Flow Logs  → S3 (format B) or CloudWatch Logs
  GuardDuty      → Security Hub (ASFF format)
  WAF logs       → S3/CloudWatch/Firehose (format C)
  Route 53 DNS   → CloudWatch Logs (format D)
  Third-party    → their own format

  → 6 different formats, 6 different locations
  → Cross-source queries = painful ETL
  → Each SIEM integration = custom parser

WITH Security Lake:
  ALL sources → Security Lake → ONE S3 bucket → OCSF format
  → Single schema for everything
  → Any OCSF-compatible tool queries all sources
  → Subscriber model for SIEM/analytics access
```

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    SOURCES (auto-collected)                       │
│                                                                  │
│  CloudTrail    VPC Flow    Route 53    Security Hub    GuardDuty │
│  (mgmt+data)   Logs        DNS Logs    findings       findings  │
│                                                                  │
│  S3 data       Lambda       WAF         EKS audit     Firewall  │
│  events        data events  logs        logs          Manager   │
└──────────────────────────────┬──────────────────────────────────┘
                               │ normalized to OCSF
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                    SECURITY LAKE                                  │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  YOUR S3 Bucket (Lake-managed, Apache Iceberg tables)    │    │
│  │  ├── Region: us-east-1/                                  │    │
│  │  │   ├── cloud_trail/                                    │    │
│  │  │   ├── vpc_flow/                                       │    │
│  │  │   ├── route53/                                        │    │
│  │  │   ├── security_hub/                                   │    │
│  │  │   └── custom_source/                                  │    │
│  │  └── Partitioned by: region, account, time              │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  Format: OCSF (Open Cybersecurity Schema Framework)              │
│  Storage: Apache Parquet on Apache Iceberg tables                │
│  Partitioning: Automatic (region, account, time)                 │
└──────────────────────────────────┬──────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────┐
│                    SUBSCRIBERS (consumers)                        │
│                                                                  │
│  Athena         OpenSearch       Splunk        Datadog           │
│  (SQL queries)  (dashboards)     (SIEM)        (monitoring)      │
│                                                                  │
│  Detective      Custom Lambda    QRadar        Any OCSF tool     │
└─────────────────────────────────────────────────────────────────┘
```

## OCSF — The Schema (Exam-Critical)

**Open Cybersecurity Schema Framework** — vendor-neutral schema for security events.

```
You DON'T need to know schema fields for the exam.
You DO need to know:

1. OCSF = Security Lake's native format
2. It normalizes ALL sources into ONE schema
3. Any OCSF-compatible tool can query without custom parsers
4. WAF logs, CloudTrail, VPC Flow Logs, third-party → all become OCSF
5. "Common schema" / "normalize logs" / "unified format" → OCSF / Security Lake
```

## Security Lake vs CloudTrail Lake vs CloudWatch Logs Insights

| Dimension | Security Lake | CloudTrail Lake | CloudWatch Logs Insights |
|---|---|---|---|
| **Data sources** | ALL (CloudTrail + VPC Flow + DNS + WAF + GuardDuty + third-party) | CloudTrail events + Config CIs | CloudWatch Log Groups |
| **Format** | OCSF (normalized) | CloudTrail native | Raw log lines |
| **Storage** | YOUR S3 bucket (Iceberg/Parquet) | Managed (no S3) | CloudWatch store |
| **Query language** | Athena SQL (or subscriber tools) | SQL (built-in) | CloudWatch Insights syntax |
| **Cross-account** | ✅ Org-wide delegated admin | ✅ Single event data store | ❌ Per-account log groups |
| **Latency** | Minutes (batch) | Near real-time | Near real-time |
| **Retention** | You control (S3 lifecycle) | 7yr or 1yr extendable | Configurable per group |
| **Cost model** | S3 storage + Athena queries | Ingestion + storage + query GB | Ingestion + storage + query GB |
| **Exam signal** | "normalize all logs" / "common schema" / "OCSF" | "fast API investigation" / "SQL on CloudTrail" | "query app logs" / "VPC Flow Logs" |

## Supported Sources

### AWS Native (auto-collected, zero config)

| Source | What It Provides |
|---|---|
| **CloudTrail** | Management events + data events |
| **VPC Flow Logs** | Network traffic metadata |
| **Route 53 Resolver** | DNS query logs |
| **Security Hub** | Aggregated findings (ASFF → OCSF) |
| **GuardDuty** | Threat findings |
| **AWS WAF** | Web request logs |
| **EKS Audit Logs** | Kubernetes API activity |
| **Lambda Data Events** | Function invocations |
| **S3 Data Events** | Object-level access |

### Custom Sources

- Any third-party tool that outputs OCSF
- Custom Lambda that transforms your logs to OCSF
- Partner integrations (CrowdStrike, Palo Alto, etc.)

## Subscriber Model

```
SUBSCRIBER = any tool that READS from Security Lake

Two access methods:
├── S3 access: subscriber reads Parquet files directly from your bucket
└── SQS notification: Security Lake notifies subscriber when new data arrives

Subscriber types:
├── Query access: Athena, OpenSearch (pull model)
└── Data access: Splunk, Datadog, QRadar (push via SQS notification)
```

## Key Limits/Quotas

| Limit | Value |
|---|---|
| Regions | Available in most commercial regions |
| Sources per region | All supported AWS sources + custom |
| Subscribers per lake | Multiple (no hard limit published) |
| Retention | You control via S3 Lifecycle |
| Rollup regions | Aggregate data from multiple regions into one |
| Delegated admin | ✅ Supported (org-wide) |
| Cost | S3 storage + data transfer + Athena queries (no Security Lake fee) |

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **YOUR S3 bucket** | Security Lake stores data in S3 buckets it creates in YOUR account — you own the data |
| **OCSF format** | Everything normalized — no custom parsers needed for subscribers |
| **Not real-time** | Batch ingestion (minutes), not streaming. For real-time → CloudWatch Logs or CloudTrail Lake |
| **Doesn't replace Security Hub** | Security Hub aggregates findings for dashboards. Security Lake stores raw logs for analysis. Different jobs. |
| **Doesn't replace CloudTrail** | CloudTrail is the SOURCE. Security Lake is the DESTINATION that normalizes it. |
| **Apache Iceberg** | Table format — enables efficient queries on partitioned Parquet files |
| **Cross-region rollup** | Can aggregate data from all regions into one "rollup region" for centralized queries |
| **Delegated admin** | Don't run in management account — delegate to security tooling account |
| **No CloudTrail Lake overlap** | CloudTrail Lake = fast SQL on API calls only. Security Lake = all logs normalized. |
| **Third-party ingestion** | Partners can write OCSF data directly into your lake |

## Integration with Other Services

| Service | Relationship |
|---|---|
| **CloudTrail** | Source → Security Lake ingests CloudTrail events |
| **GuardDuty** | Source → findings normalized to OCSF |
| **Security Hub** | Source → findings normalized to OCSF |
| **VPC Flow Logs** | Source → network data normalized |
| **Athena** | Consumer → SQL queries on Security Lake data |
| **OpenSearch** | Consumer → dashboards and search |
| **Detective** | Can correlate with Security Lake data |
| **Organizations** | Org-wide deployment via delegated admin |

## K8s Mapping

```
Security Lake  ≈  Loki/Elasticsearch with a unified schema
OCSF           ≈  OpenTelemetry semantic conventions for security
Subscribers    ≈  Grafana/Kibana dashboards reading from the store
Custom sources ≈  Fluentd/Vector shipping logs in a standard format
```

## 🧠 Cheat-Sheet One-Liners

- **Security Lake = YOUR S3 bucket + OCSF format + ALL log sources normalized.** Not managed storage — you own the bucket.
- **"Normalize all logs into one schema" = Security Lake / OCSF.** "Fast SQL on API calls" = CloudTrail Lake. Different tools.
- **Security Lake is NOT real-time.** Batch ingestion (minutes). For real-time investigation → CloudTrail Lake or CloudWatch Logs Insights.
- **Three "lakes":** CloudTrail Lake (API calls, SQL, managed store) vs Security Lake (all logs, OCSF, your S3) vs CloudWatch Logs Insights (app logs, custom syntax, CloudWatch store).
