# Network Analysis Tools — Flashcard

> 4 tools that answer different questions about network exposure/connectivity.
> Exam loves to mix these up.

---

## The 4 Tools

```
┌─────────────────────────────────────────────────────────────────┐
│ NETWORK ACCESS ANALYZER (NAA)                                    │
│                                                                  │
│ Question: "What's exposed? Find ALL unintended paths."           │
│ Scope: Broad discovery (entire VPC/account)                      │
│ Output: List of resources reachable from internet/cross-VPC      │
│ Sends traffic? NO (config analysis only)                         │
│ Use: Auditor asks "show me everything exposed"                   │
│ Persona: AUDITOR                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ VPC REACHABILITY ANALYZER (RA)                                   │
│                                                                  │
│ Question: "Why can't A reach B?" or "Explain this specific path" │
│ Scope: ONE specific source → destination pair                    │
│ Output: Hop-by-hop analysis (SG, NACL, route, ENI per hop)       │
│ Sends traffic? NO (config analysis only)                         │
│ Use: Engineer debugging one broken connection                    │
│ Persona: DEBUGGER                                                │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ INSPECTOR NETWORK REACHABILITY                                   │
│                                                                  │
│ Question: "Is this EC2 port ACTUALLY reachable from internet?"   │
│ Scope: Per-instance, per-port                                    │
│ Output: Finding with port + full path evaluated                  │
│ Sends traffic? NO (config analysis only)                         │
│ Extra: Smarter than SG check alone (evaluates full path)         │
│ Use: Vulnerability assessment (exposed port = risk)              │
│ Persona: VULNERABILITY SCANNER                                   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ FIREWALL MANAGER SG AUDIT                                        │
│                                                                  │
│ Question: "Which SGs violate our policy (e.g., 0.0.0.0/0)?"     │
│ Scope: Org-wide (all accounts)                                   │
│ Output: Non-compliant SGs + auto-remediation                     │
│ Sends traffic? NO (SG rule analysis only)                        │
│ Extra: ONLY checks SG rules (not full path like Inspector)       │
│ Use: Compliance enforcement at scale                             │
│ Persona: COMPLIANCE ENFORCER                                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## Decision Table

| Exam Signal | Tool |
|---|---|
| "Find ALL exposed resources" / "audit exposure" | **Network Access Analyzer** |
| "Why can't A reach B?" / "hop-by-hop" / "explain path" | **Reachability Analyzer** |
| "Is this port actually reachable from internet?" | **Inspector Network Reachability** |
| "Find overly permissive SGs org-wide + auto-fix" | **Firewall Manager SG audit** |
| "NAA found a path — now explain WHY it exists" | **Reachability Analyzer** (RA explains what NAA finds) |

---

## Key Distinctions

```
Q: NAA found path. Need hop-by-hop breakdown. Which tool?
A: Reachability Analyzer. NAA FINDS. RA EXPLAINS.

Q: SG open 0.0.0.0/0 but instance in private subnet (no IGW). Actually exposed?
A: Config rule = flags it (false positive). Inspector = no finding (not actually reachable).

Q: 200 accounts, find all 0.0.0.0/0 SGs + auto-remove?
A: Firewall Manager SG audit (org-wide + remediation). Not NAA (no remediation).

Q: "Without sending traffic" — which tools?
A: ALL FOUR are config-analysis only. None send traffic.

Q: Difference between NAA and Inspector Network Reachability?
A: NAA = broad (find all paths to all resources). Inspector = per-instance (is THIS instance exposed?).
```

---

## Mnemonic

```
NAA = "Show me everything exposed" (broad audit)
RA  = "Explain this ONE path" (specific debug)
Inspector = "Is THIS port vulnerable?" (per-instance risk)
FM SG = "Fix bad SGs everywhere" (org-wide compliance)
```
