# FAQ: Detection Decision Tree (Domain 1 — 16%)

> **Blueprint refs:** Task 1.1 (monitoring strategies), Task 1.2 (analyze findings), Task 1.3 (troubleshoot)
> **Weight:** 16% = ~10 questions on a 65-question exam
> **Your stats:** 167/228 = 73% — high volume but persistent decision confusion
> **Root cause:** You know ALL the services — you pick the wrong one because of VERB/CONTEXT mismatch

---

## The Master Decision Tree

```
                    ┌──────────────────────────────────┐
                    │  WHAT IS THE QUESTION ASKING?     │
                    └────────────────┬─────────────────┘
                                     │
            ┌────────────────────────┼─────────────────────────────┐
            │                        │                              │
            ▼                        ▼                              ▼
    "DETECT / ALERT /        "PREVENT / BLOCK /              "INVESTIGATE /
     IDENTIFY / MONITOR"      RESTRICT / ENFORCE"             DETERMINE / SCOPE"
            │                        │                              │
            ▼                        ▼                              ▼
    DETECTION SERVICE          CONTROL/POLICY               INVESTIGATION
    (next tree below)         (SCP/RCP/firewall)            = Detective
                                                             (always)
```

---

## Detection Service Selection (The Tree You Keep Getting Wrong)

```
"DETECT [something]..."
        │
        ├─── Is it a SPECIFIC API CALL? (named action like PutBucketPolicy, 
        │    StopLogging, CreateAccessKey, DeleteDetector)
        │         │
        │         ▼
        │    EventBridge rule on CloudTrail
        │    (near real-time, org trail, mgmt account)
        │
        ├─── Is it ANOMALOUS BEHAVIOR? (unusual geo, unusual volume,
        │    never-seen IP, 3AM access, baseline deviation)
        │         │
        │         ▼
        │    GuardDuty (threats) or GuardDuty S3 Protection (data access)
        │    (zero code, zero infra, built-in ML/threat intel)
        │
        ├─── Is it a MISCONFIGURATION? (public bucket, open SG,
        │    unencrypted resource, missing tag)
        │         │
        │         ▼
        │    Config (detect + fix) or Security Hub (detect + dashboard)
        │
        ├─── Is it EXTERNAL ACCESS EXPOSURE? (who COULD access
        │    my resource based on policy analysis)
        │         │
        │         ▼
        │    IAM Access Analyzer (static policy analysis)
        │
        └─── Is it a SOFTWARE VULNERABILITY? (CVE, package version,
             code weakness, container image flaw)
                  │
                  ▼
             Inspector (CVE scanning)
```

---

## The Three Services You Keep Confusing

### GuardDuty vs EventBridge vs Access Analyzer

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                      │
│   GuardDuty                EventBridge              Access Analyzer  │
│   ─────────                ───────────              ───────────────  │
│                                                                      │
│   WHAT:                    WHAT:                    WHAT:            │
│   Active threats           Specific API calls       Policy exposure  │
│   happening NOW            that just occurred        (who CAN)       │
│                                                                      │
│   WHEN IT FIRES:           WHEN IT FIRES:           WHEN IT FIRES:  │
│   Successful anomalous     Any matched API call     Policy grants    │
│   access detected          (regardless of who/why)  external access  │
│                                                                      │
│   EXAMPLES:                EXAMPLES:                EXAMPLES:        │
│   - C2 communication      - StopLogging called     - Bucket policy  │
│   - Credential from Tor   - DeleteDetector called    has Principal:* │
│   - Unusual S3 downloads  - CreateAccessKey (root) - SQS queue open │
│   - Crypto mining DNS      - PutBucketPolicy         to external    │
│   - Exfiltration pattern   - DisableKey called                      │
│                                                                      │
│   DOES NOT FIRE ON:        DOES NOT CARE ABOUT:    DOES NOT FIRE:   │
│   - Blocked attempts       - Whether it's bad      - On actual      │
│   - Policy changes         - Behavioral context      access events  │
│   - Specific API names     - Threat intel          - On blocked     │
│   - Failed requests                                  attempts        │
│                                                                      │
│   KEYWORD SIGNALS:         KEYWORD SIGNALS:         KEYWORD SIGNALS: │
│   "anomalous" "unusual"   "within 60 seconds"     "who can access"  │
│   "least overhead"        "specific API call"      "overly permis-  │
│   "zero code" "zero infra" "detect [API name]"     sive" "exposure" │
│   "behavioral" "pattern"   "near real-time"        "unused perms"   │
│                            "org trail exists"                         │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Your Top 3 Repeated Mistakes + Fix

### Mistake 1: "Detect external decryption" → You pick CloudTrail/EventBridge

```
WRONG THINKING: "Detect an API call → EventBridge"
RIGHT THINKING: "Detect ANOMALOUS ACCESS to data → GuardDuty S3 Protection"

The difference:
- EventBridge: "Alert me EVERY TIME kms:Decrypt is called by anyone"
  (too noisy, no intelligence, just raw event matching)

- GuardDuty S3 Protection: "Alert me when access PATTERNS are anomalous"
  (unusual volume, geo, time, caller — ML-based, zero config)

SIGNAL WORDS that mean GuardDuty (not EventBridge):
✓ "anomalous" / "unusual" / "inconsistent with baseline"
✓ "least overhead" / "zero code" / "zero infra" / "no filters"
✓ "external account" + behavior (not just existence)
✓ "alert on [behavioral description]"

SIGNAL WORDS that mean EventBridge:
✓ Named API action (StopLogging, PutBucketPolicy, DeleteDetector)
✓ "within 60 seconds" / "near real-time" / "fast"
✓ "detect [specific action]" (not pattern/behavior)
```

### Mistake 2: "Detect C2 communication" → You pick Network Firewall/DNS Firewall

```
WRONG THINKING: "C2 = network = firewall"
RIGHT THINKING: "DETECT = passive observation. BLOCK = active control."

The rule:
- "DETECT C2 + zero code + zero infra" = GuardDuty (ALWAYS)
  GuardDuty reads VPC Flow Logs + DNS logs natively
  Has built-in threat intel for C2 IPs and domains
  Generates findings automatically

- "BLOCK C2 domain" = DNS Firewall (domain-based, VPC-wide)
- "BLOCK C2 IP (hardcoded)" = Network Firewall (IP-based, stateful DROP)

TRAP: Network Firewall CAN alert (Suricata alert action)
      but requires DEPLOYMENT + RULES = NOT "zero code/infra"
      GuardDuty is ALWAYS the "zero overhead" detection answer
```

### Mistake 3: "GuardDuty fires on blocked attempts"

```
WRONG THINKING: "RCP blocks + GuardDuty detects the attempt"
RIGHT THINKING: "RCP blocks = no successful access = no GD finding"

GuardDuty detects SUCCESSFUL ANOMALOUS ACCESS:
- If RCP/SCP blocks the request → request never succeeds
- No successful access → nothing for GD to flag as anomalous
- GD monitors actual traffic/behavior, not denied API calls

WHO fires on what:
- Access Analyzer: fires on POLICY (static analysis, doesn't need access)
- GuardDuty: fires on BEHAVIOR (needs actual successful activity)
- EventBridge: fires on API CALL (regardless of outcome)

Combined scenario:
  RCP blocks external + bucket policy grants external + AA + GD enabled
  Result: AA flags the policy ✅, GD stays silent ✅ (nothing got through)
```

---

## GuardDuty Finding Type Quick Reference

```
ThreatPurpose : ResourceType / ThreatName ! DataSource

Finding progression for compromised EC2:

1. DNS query to malicious domain (Impact)
   └─ Impact:EC2/BitcoinDomainRequest.Reputation
   └─ Impact:EC2/MaliciousDomainRequest.Reputation

2a. Active TCP to MINING POOL (CryptoCurrency)
    └─ CryptoCurrency:EC2/BitcoinTool.B

2b. Active TCP to C2 SERVER (Trojan)
    └─ Trojan:EC2/C2Activity.B!DNS (if DNS detected it)
    └─ Trojan:EC2/DriveBySourceTraffic!DNS

Key rule:
  DNS query only    → IMPACT (always, regardless of destination type)
  Active TCP mining → CRYPTOCURRENCY
  Active TCP C2     → TROJAN
  The DESTINATION determines the active-connection category
```

---

## "Least Overhead" Decision Shortcuts

| Scenario | Answer | Why NOT the alternative |
|---|---|---|
| "Detect anomalous S3 access, least overhead" | GuardDuty S3 Protection | CloudTrail + metric filter = heavy plumbing |
| "Detect StopLogging within 2 min" | EventBridge in mgmt account | Config = slower (~minutes). CW metric filter = StopLogging kills its own delivery |
| "Detect public S3 buckets org-wide" | Security Hub (FSBP) | Config conformance pack = more setup. Custom Lambda = most overhead |
| "Detect unused permissions" | Access Analyzer unused access | Manual review = highest overhead |
| "Normalize all logs + own S3" | Security Lake | CW Logs Insights = only CW data. Athena = DIY plumbing |
| "Query CloudTrail, SQL, dashboards" | CloudTrail Lake | S3 + Athena = cheap but heavy setup |
| "Detect C2, zero code" | GuardDuty | Network Firewall = requires deployment |
| "Blast radius + timeline" | Detective | CloudTrail Lake = raw query, no graph |
| "Detect API call volume anomaly" | CloudTrail Insights | GuardDuty = behavioral threats, not API stats |
| "What's reachable from internet?" | Network Access Analyzer | Reachability Analyzer = single pair troubleshooting |

---

## StopLogging Detection — The Trap

```
Three detection mechanisms:
                                                      Works?
1. CW Metric Filter on CloudTrail log group    →     ❌ NO
   (StopLogging kills its own CW delivery —
    the event never reaches CW Logs)

2. EventBridge rule in management account      →     ✅ YES
   (EventBridge receives from CloudTrail's
    management event stream DIRECTLY, not CW)

3. Config rule (cloudtrail-enabled)            →     ✅ YES
   (evaluates state periodically, slower)

FASTEST: EventBridge (seconds)
RELIABLE BUT SLOWER: Config (minutes)
BROKEN: CW metric filter (never sees the event)
```

---

## Access Analyzer — Two Modes (Don't Confuse)

```
1. EXTERNAL ACCESS analyzer (default):
   "Who OUTSIDE my account/org can access this resource?"
   - Fires on policy granting external access
   - Static analysis — doesn't need actual access
   - Resources: S3, SQS, IAM roles, KMS, Lambda, Secrets Manager

2. UNUSED ACCESS analyzer:
   "Which permissions haven't been used in 90 days?"
   - Per-action granularity (not just per-role)
   - Generates replacement policy (policy generation)
   - "Find bloat + generate right-sized replacement" = two features, one service

3. POLICY VALIDATION (pre-deployment):
   "Check this policy for security issues BEFORE attaching"
   - Grammar, security warnings, best practices
   - Different from IAM Policy Simulator (tests existing policies)
```

---

## Config vs Security Hub vs Conformance Pack

```
┌──────────────────────────────────────────────────────────────────────┐
│ Config Rule           → Evaluates ONE resource against ONE rule       │
│                         Can trigger auto-remediation (SSM/Lambda)     │
│                                                                      │
│ Conformance Pack      → BUNDLE of rules + remediation as ONE unit    │
│                         Org-wide from delegated admin                 │
│                         "20 rules + auto-fix + single deploy"        │
│                                                                      │
│ Security Hub Standard → Same rules BUT:                              │
│                         ✅ Dashboard + scoring + aggregation         │
│                         ❌ No built-in remediation                   │
│                         "CIS score across 200 accounts"              │
└──────────────────────────────────────────────────────────────────────┘

Decision:
- "Check + auto-fix" → Config rule / conformance pack
- "Dashboard + compliance score + org-wide" → Security Hub
- "Both" → Security Hub (view) + conformance pack (fix)
```

---

## Log Source Decision Matrix

| "I want to know..." | Source | Query Tool |
|---|---|---|
| Which API calls were made | CloudTrail | Lake (SQL) or Athena |
| Which domains were queried | Route 53 Resolver Query Logs | CW Logs Insights |
| Traffic volumes between IPs | VPC Flow Logs | CW Logs Insights or Athena |
| What GuardDuty found | GuardDuty findings | Security Hub / EventBridge |
| Normalized view of everything | Security Lake (OCSF) | Athena / SageMaker |
| Top talkers / aggregation | VPC Flow Logs in CW | CW Logs Insights |
| Full investigation graph | Detective | Detective console |

---

## 🧠 Cheat-Sheet One-Liners

- **"Anomalous behavior" = GuardDuty. "Specific API call" = EventBridge. "Who could access" = Access Analyzer.** Three different questions, three different services.
- **GuardDuty ≠ failed attempts.** It needs SUCCESSFUL anomalous access. Blocked by RCP/SCP = no finding.
- **EventBridge SIGNAL WORDS: "within 60 seconds" + "specific API" + "org trail exists" + "least overhead for fast detection."**
- **GuardDuty SIGNAL WORDS: "anomalous" + "unusual" + "zero code" + "behavioral" + "pattern" + "least overhead for threat detection."**
- **Access Analyzer SIGNAL WORDS: "who can access" + "overly permissive" + "unused permissions" + "before deploying" (validation).**
- **DNS query = Impact (always). Active TCP to mining = CryptoCurrency. Active TCP to C2 = Trojan.**
- **StopLogging kills CW metric filter delivery. Use EventBridge (direct from CloudTrail stream).**
- **"Detect + find + investigate" chain: GuardDuty (find) → EventBridge (route) → Detective (investigate).**
