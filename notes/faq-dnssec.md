# FAQ: DNSSEC in Route 53

> **Blueprint ref:** Task 3.3 (network security controls)
> **Exam frequency:** Low (1-2 questions) but always the same trap.

---

## Trust Chain

```
        Root (.)
          │
          │  DS record → points to .com's KSK
          ▼
        .com (TLD)
          │
          │  DS record → points to example.com's KSK
          ▼
      example.com (your parent zone)
          │
          │  DS record → points to api.example.com's KSK
          ▼
    api.example.com (your subdomain)
          │
          ├── KSK (Key Signing Key) → signs the DNSKEY RRset
          │     └── Public half goes into parent as DS record
          │
          └── ZSK (Zone Signing Key) → signs actual records (A, AAAA, MX, etc.)
                └── Signed by KSK (chain of trust)
```

---

## How Validation Works

```
Resolver asks: "What's the IP for api.example.com?"

1. Get api.example.com's DNSKEY (contains KSK + ZSK public keys)
2. Verify KSK matches DS record in parent zone (example.com)
3. Verify ZSK is signed by KSK
4. Verify A record is signed by ZSK
5. Chain intact → ANSWER TRUSTED ✅

If DS record MISSING in parent:
  Step 2 fails → chain broken → SERVFAIL (validating resolver)
  Non-validating resolver: works fine (doesn't check chain)
```

---

## Route 53 DNSSEC Setup

```
Step 1: Enable DNSSEC signing on hosted zone (Route 53 creates KSK + ZSK)
Step 2: Route 53 gives you the DS record value
Step 3: YOU manually add DS record to PARENT zone
        ↑ THIS IS THE STEP PEOPLE FORGET = broken chain
```

---

## Exam Patterns

| Symptom | Cause | Fix |
|---|---|---|
| SERVFAIL for DNSSEC-validating resolvers, works for non-validating | DS record missing in parent zone | Add DS record to parent |
| ALL resolvers fail | Zone signing misconfigured or KSK expired | Check DNSSEC status in Route 53 console |
| Subdomain SERVFAIL, parent works | DS record for subdomain missing in parent | Add DS to parent zone for that subdomain |

---

## Key Facts

- Route 53 supports DNSSEC for **public hosted zones only** (not private)
- KSK is created in Route 53 (backed by KMS in us-east-1)
- ZSK is fully managed by Route 53 (auto-rotated)
- KSK rotation = manual (you must update DS in parent)
- Enabling DNSSEC does NOT automatically add DS to parent — always manual

---

## 🧠 Cheat-Sheet One-Liners

- **"Broken trust chain" = DS record missing in parent zone. Always.**
- **DNSSEC trust chain:** Root → .com (DS) → example.com (DS) → api.example.com (KSK→ZSK→records)
- **Validating resolver SERVFAIL + non-validating works = DS missing**
- **Route 53 DNSSEC = public zones only. KSK backed by KMS (us-east-1).**
