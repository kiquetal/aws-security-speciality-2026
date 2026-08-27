# PAGE 2 — D-DAY (Incident Response D2)

> Write by hand. Read once before entering the exam room.

---

## Containment Decision (ASK BEFORE PICKING)

```
Q1: "Shared role?"      YES → eliminate TokenIssueTime (kills ALL instances)
Q2: "Can't disrupt?"    YES → eliminate deny-all SG (kills the app)

Dedicated + can disrupt    → TokenIssueTime + deny-all SG + AMI + EBS
Dedicated + can't disrupt  → TokenIssueTime + EBS + IMDSv2 hop=1
Shared + can disrupt       → Deny-all SG on compromised ONLY
Shared + can't disrupt     → NF DROP on attacker IP (surgical)
InsideAWS (always)         → Deny-all SG on attacker (never TokenIssueTime)
IAM user leaked            → Deny * on user (covers ALL paths)
```

## Credential Leak — What Survives Deactivating a Key

```
KILLED by deactivating key:
  ✅ Presigned URLs (checked at use time against key status)
  ✅ Direct API calls with that key

SURVIVES deactivating key:
  ❌ Second access key attacker created
  ❌ Console password attacker enabled
  ❌ Already-issued STS tokens in Account B

FIX: Deny * on IAM user (blocks ALL paths with one action)
     + TokenIssueTime on assumed roles in other accounts (separate)
```

## Forensic Evidence Order

```
ASG present?  → Detach/suspend FIRST (protect from auto-termination)
Then ALWAYS:  → No-reboot AMI (memory, most perishable)
              → EBS snapshot (disk)
              → Block C2 (NACL or NF DROP)
              → Deregister from LB (LAST)
              → Copy to forensics account with Object Lock

RULE: ACQUIRE before ISOLATE (deny-all blocks SSM for memory capture)
```

## Evidence by Instance Type

```
EC2 running       → No-reboot AMI (memory) + EBS snapshot (disk)
EC2 won't boot    → EC2Rescue for Windows (detach volume, offline)
Lambda            → NO EBS/AMI. Only CW Logs + X-Ray + CloudTrail.
```

## Kill Active Connections

```
SG removal    = does NOT kill tracked flows (stateful, conntrack)
NACL deny all = kills EVERY packet instantly (stateless)

"Active connections + immediately" = ALWAYS NACL
```

## IR Services (one line each)

```
Test IR pipeline       → CreateSampleFindings (NOT FIS)
Assess RTO/RPO         → Resilience Hub (NOT FIS)
Shift bad AZ           → ARC zonal shift (seconds, LB-level)
Inject infra failure   → FIS (chaos with stop conditions)
Investigate finding    → Detective (needs finding as entry point)
No finding + query     → CW Logs Insights (NOT Detective)
Custom viz + reusable  → SageMaker notebooks (NOT Detective)
Session recording      → Session Manager logging (NOT CW Agent)
```

## EBS Snapshot Cross-Account (for forensics)

```
aws/ebs default key:  Copy with CMK → Share → Grant → They Copy
Customer CMK:         Share → Grant → They Copy

"Share it, grant the key, they copy with their own key"
Always: Share → Grant → They Copy (aws/ebs adds copy-first step)
```

## Ordering Question Pattern (no partial credit)

```
Protect → Acquire volatile → Acquire stable → Isolate → Remove traffic → Archive
ASG     → No-reboot AMI   → EBS snapshot  → NACL/NF → Deregister    → Object Lock
```
