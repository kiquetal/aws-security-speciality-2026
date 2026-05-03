# FAQ: AWS CloudTrail

## Security Use Cases

### Audit & Compliance
- **Canonical source** of user activity and API usage logs across AWS
- Records who did what, where, and when
- Enables governance, compliance, operational auditing, risk auditing
- Logs delivered to S3, CloudWatch Logs, EventBridge

### CloudTrail Lake (Task 1.2 — Exam-Critical)

> ⚠️ **Know this cold.** The exam tests Lake vs S3+Athena as a decision point.

**Problem Lake solves:** CloudTrail → S3 → Athena works but at scale you manage
partitioning, schemas, S3 lifecycle, and queries hit raw JSON with ~15 min delay.

**What Lake is:** A fully managed, near real-time query engine for CloudTrail events.
No S3 buckets, no Athena tables, no partitioning — just SQL.

```
CloudTrail → S3 + Athena (DIY)          CloudTrail → Lake (managed)
├── ~15 min delivery delay               ├── Near real-time ingestion
├── You manage S3, partitions, schemas   ├── Fully managed — zero plumbing
├── Athena per-scan cost                 ├── SQL built in + dashboards
├── No dashboards                        ├── Pre-built + custom dashboards
├── Cross-account = complex              ├── Cross-account in one data store
└── Unlimited retention (S3 lifecycle)   └── 7yr or 1yr extendable retention
```

#### Lake vs S3+Athena Decision Table

| Dimension | S3 + Athena | CloudTrail Lake |
|---|---|---|
| **Latency** | ~15 min | Near real-time |
| **Management** | You manage everything | Fully managed |
| **Cost** | Lower | Higher (ingestion + storage + query GB) |
| **Retention** | Unlimited (S3 lifecycle) | 7 years or 1 year extendable |
| **Event selectors** | Basic or advanced | **Advanced only** |
| **Cross-account** | Multiple buckets or replication | Single event data store |
| **Import old logs** | N/A | ✅ Copy S3 logs into Lake |
| **Exam signal** | "cost-effective long-term" | "fast investigation" / "near real-time" / "dashboards" |

#### Lake Data Sources (Not Just CloudTrail)
- CloudTrail events (management + data)
- AWS Config configuration items
- Audit Manager evidence
- **Non-AWS sources** (custom integrations)

#### Lake Pricing
- **Ingestion**: Per GB ingested
- **Storage**: Per GB-month
- **Queries**: Per GB scanned
- **Two options**: 7-year retention (higher ingestion, lower query) or 1-year extendable (lower ingestion, higher query)

#### Lake Exam Gotchas
- **Advanced event selectors REQUIRED** — Lake doesn't support basic selectors
- **Switching basic → advanced is one-way** — can't go back
- **Can import S3 logs** — unify historical + new data in one place
- **Only newly recorded Config CIs** — not historical before enablement
- **SQL + natural language** — Lake supports both (NL generates SQL for you)

### Event Types
- **Management events**: Control plane operations (CreateBucket, TerminateInstance)
- **Data events**: Data plane operations (GetObject, PutObject, Lambda invocations)
- **Insights events**: Unusual API activity detected by ML
- **Network activity events**: VPC Flow Logs integration

### Event Enrichment
- **Resource tags**: Include AWS resource tags in events
- **IAM global condition keys**: Include evaluated condition keys (e.g., aws:SourceAccount)
- **Principal tags**: Include tags from IAM principal making request
- **Best-effort basis**: Tags updated with eventual consistency

### Multi-Account & Multi-Region
- **Organization trails**: Capture events from all accounts in organization
- **Multi-region trails**: Capture events from all regions
- **Single S3 bucket**: Consolidate logs from multiple accounts/regions
- **Cross-region aggregation**: Use EventBridge or Security Hub

## Key Limits/Quotas

### Trail Limits
- **5 trails per region** (can request increase)
- **One free trail** per account (management events only)
- **Organization trail**: Captures all accounts in organization

### Event Data Store (CloudTrail Lake)
- **Retention**: 7 years (default) or 1 year extendable
- **Query concurrency**: Multiple concurrent queries supported
- **Data sources**: CloudTrail events, AWS Config CIs, Audit Manager evidence, non-AWS sources

### Log Delivery
- **15 minutes typical latency** for log delivery to S3
- **Near real-time** for CloudTrail Lake
- **90-day retention** in CloudTrail console (free)
- **Longer retention**: Store in S3 or CloudTrail Lake

### API Limits
- **LookupEvents**: 50 requests per second
- **Other APIs**: Standard AWS API limits apply

## Exam Gotchas

### CloudTrail vs CloudWatch vs VPC Flow Logs
- **CloudTrail**: API activity (who did what)
- **CloudWatch**: Metrics, logs, alarms (performance, application logs)
- **VPC Flow Logs**: Network traffic (IP, port, protocol)

### Event History vs Trails
- **Event History**: 90 days, free, management events only, per-region
- **Trails**: Configurable retention, S3 storage, all event types, multi-region

### Data Events
- **Not enabled by default** (high volume, additional cost)
- **S3 data events**: GetObject, PutObject, DeleteObject
- **Lambda data events**: Invoke
- **DynamoDB data events**: GetItem, PutItem, DeleteItem
- **Can filter by resource** (specific buckets, functions, tables)

### Log File Integrity Validation
- **SHA-256 hashing** for log files
- **Digital signing** with SHA-256 with RSA
- **Digest files**: Hourly, contain hashes of log files
- **Validate with AWS CLI**: `aws cloudtrail validate-logs`
- **Computationally infeasible** to modify without detection

### Organization Trails
- **Created in management account**
- **Applies to all accounts** in organization (existing and new)
- **Member accounts cannot modify** organization trail
- **Logs delivered to single S3 bucket** in management account

### CloudTrail Lake vs S3 Logs
- **CloudTrail Lake**: SQL queries, dashboards, near real-time, higher cost
- **S3 logs**: Long-term storage, lower cost, requires Athena for queries
- **Import capability**: Copy S3 logs to CloudTrail Lake for unified querying

### Insights Events
- **ML-based anomaly detection**: Unusual API call rate or error rate
- **Baseline period**: 7 days to establish normal behavior
- **Additional cost**: Charged per 100,000 events analyzed
- **Use cases**: Detect compromised credentials, resource provisioning spikes

### Event Selectors — Basic vs Advanced (Task 1.2)

> ⚠️ **Exam signal:** Any question mentioning "prefix," "subset of functions," or "most flexibly" with data events → **advanced event selectors**.

#### Comparison

| Capability | Basic | Advanced |
|---|---|---|
| Toggle management events on/off | ✅ | ✅ |
| Toggle data events on/off per service | ✅ | ✅ |
| Filter by **exact** resource ARN | ✅ | ✅ |
| Filter by ARN **prefix** (`StartsWith`) | ❌ | ✅ |
| Exclude by ARN prefix (`NotStartsWith`) | ❌ | ✅ |
| Filter by `eventName` (e.g., Invoke only) | ❌ | ✅ |
| Filter by `readOnly` (true/false) | ✅ (read/write toggle) | ✅ (field selector) |
| Combine multiple field conditions | ❌ | ✅ |
| Max selectors per trail | 5 | 500 conditions |
| Required for CloudTrail Lake | — | ✅ (Lake only supports advanced) |

#### When to Use Which

- **Basic:** Simple "log all S3 data events" or "log one specific bucket"
- **Advanced:** Prefix-based filtering, event name filtering, cost optimization on high-volume workloads, CloudTrail Lake

#### Advanced Event Selector Fields

| Field | Operators | Example |
|---|---|---|
| `eventCategory` | `Equals` | `Data`, `Management` |
| `resources.type` | `Equals` | `AWS::S3::Object`, `AWS::Lambda::Function`, `AWS::DynamoDB::Table` |
| `resources.ARN` | `Equals`, `StartsWith`, `NotEquals`, `NotStartsWith` | `arn:aws:lambda:...:function:UpdProdCount` |
| `eventName` | `Equals`, `StartsWith` | `GetObject`, `Invoke` |
| `readOnly` | `Equals` | `true`, `false` |

#### Example: Log Only Invoke Events for Lambda Functions with a Name Prefix

```json
{
  "Name": "LambdaPrefixFilter",
  "FieldSelectors": [
    { "Field": "eventCategory", "Equals": ["Data"] },
    { "Field": "resources.type", "Equals": ["AWS::Lambda::Function"] },
    { "Field": "resources.ARN", "StartsWith": ["arn:aws:lambda:us-east-1:123456789012:function:UpdProdCount"] },
    { "Field": "eventName", "Equals": ["Invoke"] }
  ]
}
```

#### Example: Log S3 Data Events for All Buckets Except a High-Volume One

```json
{
  "Name": "S3ExcludeHighVolume",
  "FieldSelectors": [
    { "Field": "eventCategory", "Equals": ["Data"] },
    { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
    { "Field": "resources.ARN", "NotStartsWith": ["arn:aws:s3:::high-volume-logs-bucket/"] }
  ]
}
```

#### Exam Gotchas — Event Selectors
- **Basic selectors force all-or-nothing** per resource type — you can't say "only Invoke, not GetFunction"
- **Advanced selectors are required for CloudTrail Lake** event data stores
- **You cannot mix basic and advanced** on the same trail — it's one or the other
- **Switching from basic to advanced is one-way** — you can't go back to basic
- **Read/write filtering**: Basic uses a toggle; advanced uses `readOnly` field selector (same result, different syntax)

### CloudTrail Lake Pricing
- **Ingestion**: Per GB ingested
- **Storage**: Per GB-month stored
- **Queries**: Per GB scanned
- **Two pricing options**: 7-year retention or 1-year extendable

### Config Integration
- **CloudTrail Lake can ingest Config CIs**: Historical configuration items
- **Use case**: Correlate who changed what with resource configuration changes
- **Limitation**: Only newly recorded CIs (not historical before enablement)

## Best Practices for IAM Policies

1. **Enable CloudTrail in all regions** - use multi-region trail
2. **Enable log file validation** - detect tampering
3. **Encrypt logs with KMS** - use customer managed key
4. **Restrict S3 bucket access** - only CloudTrail and authorized users
5. **Enable MFA Delete** on S3 bucket for log files
6. **Use S3 Object Lock** for compliance (WORM)
7. **Monitor with CloudWatch alarms** - alert on critical API calls
8. **Aggregate logs** from all accounts to central security account
9. **Enable Insights events** for anomaly detection
10. **Use EventBridge** for real-time response to security events

### Example: Prevent CloudTrail Disablement
```json
{
  "Effect": "Deny",
  "Action": [
    "cloudtrail:StopLogging",
    "cloudtrail:DeleteTrail",
    "cloudtrail:UpdateTrail"
  ],
  "Resource": "*"
}
```

### Example: Restrict CloudTrail S3 Bucket Access
```json
{
  "Effect": "Allow",
  "Principal": {
    "Service": "cloudtrail.amazonaws.com"
  },
  "Action": "s3:PutObject",
  "Resource": "arn:aws:s3:::my-cloudtrail-bucket/*",
  "Condition": {
    "StringEquals": {
      "s3:x-amz-acl": "bucket-owner-full-control",
      "aws:SourceArn": "arn:aws:cloudtrail:region:account:trail/trail-name"
    }
  }
}
```

### Example: Alert on Root Account Usage
```
CloudWatch Logs filter: { $.userIdentity.type = "Root" && $.userIdentity.invokedBy NOT EXISTS }
```
