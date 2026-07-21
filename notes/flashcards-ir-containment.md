# Flashcards: Incident Response Containment

> Based on: `diagrams/ir-containment-decision-tree.png`
> Domain: D2 (14%) — 0 flashcards existed before this file
> Weak areas: #36, #37 (credential leak IR, OutsideAWS/InsideAWS)

---

## Containment Method by Finding Type

| Finding | Containment | WHY not the other? |
|---|---|---|
| OutsideAWS (API must stay up) | TokenIssueTime + no-reboot AMI + EBS snapshot + IMDSv2 hop=1 | Deny-all SG kills legitimate traffic |
| OutsideAWS (shared role) | Deny-all SG or NACL on compromised ONLY | TokenIssueTime kills ALL instances sharing that role |
| OutsideAWS (can disrupt) | No-reboot AMI + EBS snapshot + deny-all SG | Memory first (most perishable) |
| InsideAWS | Deny-all SG on ATTACKER's instance | TokenIssueTime kills BOTH (same role) |
| Credential leak (keys on GitHub) | Deactivate keys + Deny * on IAM USER | Covers 2nd key + console + sessions |

## Quick-Fire (cover right column, recall)

| Q | A |
|---|---|
| OutsideAWS + can't stop instance = ? | TokenIssueTime (NOT deny-all SG) |
| InsideAWS = ? | Deny-all SG on attacker (NOT TokenIssueTime) |
| Why not TokenIssueTime for InsideAWS? | Both instances share same role — kills both |
| Why not deny-all SG for OutsideAWS + API up? | Kills legitimate API traffic |
| Credential leak — single broadest action? | Inline Deny * on IAM user |
| Why Deny * and not just deactivate keys? | Attacker may have created 2nd key + console access |
| Compromised ROLE = ? | TokenIssueTime (only temp creds exist) |
| Compromised IAM USER = ? | Deny * on user (keys + console = persistent) |
| Preserve volatile memory without stopping? | No-reboot AMI |
| Preserve disk evidence? | EBS snapshot |
| Prevent future SSRF after OutsideAWS? | IMDSv2 hop limit = 1 |
| Order: acquire or isolate first? | ACQUIRE first (deny-all blocks SSM needed for memory) |
| Forensics Orchestrator: deny-all then SSM fails — why? | Deny-all blocks outbound to SSM endpoints |
| Test IR pipeline without real incident? | CreateSampleFindings API (not FIS) |
| Assess RTO/RPO for auditors? | Resilience Hub (not FIS) |
| Shift traffic from bad AZ in seconds? | ARC zonal shift (not Route 53) |
| FIS does what? | Injects infra failures to TEST your plan |
| Detective entry point? | Needs an existing finding (no finding = CW Logs Insights) |
| Custom viz + reusable notebook for IR? | SageMaker notebooks (not Detective) |

---

## OutsideAWS Containment — The THREE Constraints Check

```
BEFORE picking TokenIssueTime, ask:

  1. "Is the role SHARED?"
     YES → TokenIssueTime kills ALL instances → CAN'T USE IT

  2. "Can traffic be DISRUPTED?"
     NO → Deny-all SG kills the instance → CAN'T USE IT

  3. Both blocked?
     → SURGICAL: NF DROP on attacker's external IP
     → Or NACL deny on attacker's IP (if single subnet)
```

| Constraints | Containment Method |
|---|---|
| Dedicated role + can disrupt | TokenIssueTime ✅ (simplest) |
| Dedicated role + can't disrupt | TokenIssueTime ✅ (IMDS refreshes, app stays up) |
| Shared role + can disrupt | Deny-all SG on compromised ONLY |
| **Shared role + can't disrupt** | **NF DROP on attacker IP (surgical, zero disruption)** |

### Your Error Pattern (4x failed)

```
Q1598: picked deny-all first      → should acquire first
Q1633: picked deregister           → deregister = downtime
Q1638: picked TokenIssueTime       → shared role = kills all
Q23:   picked TokenIssueTime       → shared role + can't disrupt = NF DROP

RULE: Read for "shared role" FIRST. If shared → eliminate TokenIssueTime immediately.
      Then read for "can't disrupt." If can't → eliminate deny-all SG.
      Both eliminated → NF DROP on attacker IP.
```

---

## NACL vs SG for Killing Active Connections (3x Failed)

```
SG = STATEFUL
  → Connection tracking table remembers established sessions
  → Remove ALL rules → tracked connections STILL FLOW
  → New connections blocked, but OLD ones persist
  → SG rule removal ≠ immediate kill

NACL = STATELESS
  → Every single packet evaluated independently
  → No memory of previous packets
  → Deny all → EVERY packet dropped instantly
  → Active TCP sessions die immediately (RST or timeout)

┌──────────────────────────────────────────────────┐
│  "Kill EXISTING active connections immediately"   │
│  = NACL deny all (ALWAYS)                        │
│                                                   │
│  "Block FUTURE connections only"                  │
│  = SG works fine                                  │
│                                                   │
│  "Only resource in subnet" + "active connections" │
│  = NACL (safe, no collateral damage)             │
└──────────────────────────────────────────────────┘
```

### Your Error Pattern (3x)

```
Udemy Q11 (original): picked SG    → should be NACL
Udemy Q12 (retake):   picked SG    → should be NACL
Dojo Q19:             picked SG    → should be NACL

SIGNAL WORDS: "active connections" + "immediately" + "as quickly as possible"
  → ALWAYS NACL. Never SG.
```

---

## Surgical vs Nuclear Containment (3x Failed)

```
NUCLEAR = affects EVERYONE (legitimate + attacker)
  • Bucket policy deny all principals
  • Deny-all SG (kills all traffic including legitimate)
  • DenyAll policy on role (kills all sessions)

SURGICAL = affects ONLY the attacker
  • Revoke role sessions (TokenIssueTime) — kills stolen creds only
  • NF DROP on attacker IP — blocks one IP
  • Suppression of specific IAM user — blocks one identity

RULE: "Minimize disruption" / "without affecting production"
  → SURGICAL (most targeted option)
  → NEVER pick the nuclear option when surgical exists
```

### Your Error Pattern (3x)

```
Q7:  Picked DenyAll policy       → should be Detective (investigate, don't contain!)
Q23: Picked TokenIssueTime       → should be NF DROP (shared role = TIT kills all)
Q33: Picked bucket deny-all      → should be revoke sessions (surgical)

ASK YOURSELF: "Does my answer affect ONLY the attacker?"
  YES → probably correct
  NO  → find the more targeted option
```
