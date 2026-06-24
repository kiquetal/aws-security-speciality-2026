# D1 Detection — Exam-Day Rapid Reference Card

> Print this. Read it 10 min before your exam. This is your #1 error pattern.

---

## THE DECISION (read question's LAST SENTENCE first)

| Question says... | Service | Why NOT the other |
|---|---|---|
| "Detect [specific API] within 60s" | **EventBridge** | GD detects behavior, not API calls |
| "Detect anomalous/unusual [anything]" | **GuardDuty** | EB can't detect "unusual" — only exact API matches |
| "Detect external/unusual data access, zero code" | **GuardDuty S3 Protection** | CloudTrail is the log, not the detector |
| "Who CAN access (no access yet)" | **Access Analyzer** | GD needs ACTUAL access to fire |
| "Investigate + timeline + blast radius" | **Detective** | Needs an existing finding as entry point |
| "No finding exists, open-ended query" | **CW Logs Insights** | Detective needs a finding to start |
| "Detect [API call] + auto-remediate" | **Config rule + SSM** | EventBridge detects faster but Config fixes |
| "Prevent [API call] from ever happening" | **SCP** | Not a detection service at all |

---

## THE THREE TRAPS (your error history)

### Trap 1: "Detect external decryption, least overhead"
- ❌ CloudTrail (log, not detector)
- ❌ EventBridge (specific API, not anomaly)
- ✅ **GuardDuty S3 Protection** (anomalous access pattern)

### Trap 2: "Bucket grants external, no access yet — what fires?"
- ❌ GuardDuty (needs SUCCESSFUL access)
- ✅ **Access Analyzer** (reads policy text, fires immediately)

### Trap 3: "RCP blocks, 500 denied attempts — what fires?"
- ❌ GuardDuty (BLOCKED = no successful access = no finding)
- ✅ **Access Analyzer** (still fires — reads policy, doesn't know about RCP runtime)

---

## STOPLOGGING SPECIAL CASE

| Mechanism | Fires? | Why |
|---|---|---|
| CW metric filter | ❌ NO | StopLogging kills its own CW Logs delivery |
| EventBridge | ✅ YES (seconds) | Receives from CT management stream directly |
| Config | ✅ YES (minutes) | Evaluates resource state independently |

---

## GUARDDUTY FINDING CHEAT

| DNS query only (no connection) | → Impact |
|---|---|
| Active TCP to mining pool | → CryptoCurrency |
| Active TCP to C2 server | → Trojan |
| Credentials from Tor/unusual geo | → UnauthorizedAccess |

**Rule:** DNS = always Impact. TCP destination determines the rest.
