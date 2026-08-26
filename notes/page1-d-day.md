# PAGE 1 — D-DAY (Detection D1)

> Write by hand. Read once before entering the exam room.

---

## Service Selection (instant decision)

```
Specific API + fast (60s)     → EventBridge
Anomalous behavior + zero code → GuardDuty
Who COULD access (static)     → Access Analyzer
No finding + open query       → CW Logs Insights
Finding exists + investigate  → Detective
Normalize all logs + OCSF     → Security Lake
SQL on API calls + dashboards → CloudTrail Lake
Query data in S3 (ELB logs)   → Athena
```

## Global Service Events — ISC = us-east-1

```
I = IAM (CreateUser, CreateRole, AttachPolicy, CreateAccessKey)
S = STS (AssumeRole, ConsoleLogin, GetSessionToken)
C = CloudFront (CreateDistribution)

EventBridge rule for these → MUST be in us-east-1
Everything else → region where the resource lives
```

## GuardDuty Rules

```
DNS query only (no TCP)     → Impact (always, any destination)
Active TCP to mining pool   → CryptoCurrency
Active TCP to C2 server     → Trojan
GD ≠ failed attempts        → RCP blocks = no finding (needs successful access)
GD is REGIONAL              → not enabled in region = zero findings
```

## StopLogging Detection

```
CW metric filter  → BLIND (StopLogging kills its own CW delivery)
EventBridge       → SECONDS (fast path from CloudTrail)
Config            → MINUTES (evaluates state periodically)
```

## Log Destinations

```
S3 ONLY club (never CW Logs): ELB, S3 access logs, CloudFront
CW Logs ONLY: Route 53 public DNS query logging
VPC Flow Logs: S3 + CW Logs + Firehose (all 3, IAM role for ALL)
CloudTrail: S3 (slow 15min) + CW Logs (slow) + EventBridge (fast seconds)
```

## Network Analysis Tools — A-D-S

```
NAA (Network Access Analyzer) = AUDITOR  → "find ALL exposed paths"
RA  (Reachability Analyzer)   = DEBUGGER → "explain THIS one path hop-by-hop"
Inspector Network             = SCANNER  → "is THIS port reachable?"

NAA finds. RA explains. Inspector scans.
```

## CloudTrail Delivery Speeds

```
CloudTrail → S3           = ~15 min (batch, archival)
CloudTrail → CW Logs      = ~5-15 min (batch)
CloudTrail → EventBridge  = SECONDS (near real-time, auto for mgmt events)

"Fast detection" = ALWAYS EventBridge (not CW metric filter)
```

## Access Analyzer vs GuardDuty

```
AA = STATIC (reads policy text, fires immediately on config)
GD = DYNAMIC (needs successful + anomalous access to fire)

RCP blocks external → AA still fires (reads policy)
                    → GD stays silent (no successful access)
```

## The Verb Rule

```
"Detect anomalous"  → GuardDuty (behavioral ML, zero code)
"Detect specific API" → EventBridge (pattern match, seconds)
"Prevent / block"   → Policy (SCP, RCP, key policy, bucket policy)

CloudTrail = LOG (never the detection answer)
EventBridge = TRIGGER (reads from CloudTrail fast path)
GuardDuty = BEHAVIORAL DETECTOR (reads CT + Flow + DNS internally)
```
