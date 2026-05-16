# Detect vs Prevent — Flashcard (Your #1 Recurring Error)

> You've missed this 5 times: Q100, Q105, Q153, Q156, Q158
> The verb in the question tells you the service. STOP. READ THE VERB.

## The Rule

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   "DETECT" / "ALERT" / "NOTIFY" / "KNOW WHEN"          │
│   + "least overhead" / "zero code"                      │
│                                                         │
│   = GuardDuty. ALWAYS. NO EXCEPTIONS.                   │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                                                         │
│   "PREVENT" / "BLOCK" / "RESTRICT" / "ENFORCE"          │
│                                                         │
│   = Policy (KMS key policy, SCP, RCP, bucket policy)    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Why You Keep Picking CloudTrail

```
YOUR BRAIN:  "detect decryption" → "I need to see the API call" → CloudTrail
CORRECT:     "detect decryption" → "I need ALERTS with zero effort" → GuardDuty

CloudTrail = the RAW LOG (a filing cabinet)
GuardDuty  = the SECURITY GUARD (watches the cameras FOR you)

CloudTrail doesn't alert. It just records.
GuardDuty reads CloudTrail + VPC Flow + DNS → generates findings → alerts you.
```

## Why You Keep Picking Access Analyzer

```
YOUR BRAIN:  "unusual location" → "something is wrong with access" → Access Analyzer
CORRECT:     "unusual location" → "something BAD is HAPPENING NOW" → GuardDuty

Access Analyzer = AUDIT (finds bad configs that COULD be exploited)
GuardDuty       = ALARM (finds bad things ACTUALLY happening)

"Overly permissive policy"     → Access Analyzer (misconfiguration)
"Credentials used from Tor"    → GuardDuty (active threat)
"Unusual geographic location"  → GuardDuty (active threat)
```

## Self-Test (answer without looking up)

1. "Alert when external account decrypts our KMS keys, least overhead" → ?
2. "Which roles have unused permissions?" → ?
3. "Notify when credentials used from anonymizing proxy" → ?
4. "Which S3 buckets are externally accessible?" → ?
5. "Detect crypto mining on EC2, zero custom code" → ?

## Answers

1. **GuardDuty** (detect + least overhead)
2. **IAM Access Analyzer** (unused = misconfiguration audit)
3. **GuardDuty** (active threat happening now)
4. **IAM Access Analyzer** (external access = misconfiguration audit)
5. **GuardDuty** (active threat + zero code)

## The 3 Services — One Sentence Each

| Service | One sentence |
|---|---|
| **GuardDuty** | "Something bad is happening RIGHT NOW — here's a finding." |
| **IAM Access Analyzer** | "Your permissions are too broad — here's what to tighten." |
| **CloudTrail** | "Here's the raw log of every API call — do what you want with it." |
