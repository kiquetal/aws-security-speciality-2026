# FAQ: ALB + HIDS + Perfect Forward Secrecy (PFS)

> **Blueprint ref:** Task 5.1 (data in transit), Task 3.1 (edge security)
> **Exam frequency:** 1-2 questions. Always same pattern.

---

## The Problem

```
You have THREE requirements that seem to conflict:

1. HIDS on EC2 must inspect decrypted traffic (needs to see plaintext)
2. Traffic must be encrypted in transit (can't send plaintext over network)
3. PFS required (past sessions safe even if private key leaks)

How do you satisfy all three simultaneously?
```

---

## The 3 Options

```
OPTION A: Terminate at ALB → HTTP to EC2
┌────────┐   HTTPS    ┌─────┐   HTTP (plaintext!)   ┌──────────┐
│ Client │───────────▶│ ALB │──────────────────────▶│   EC2    │
└────────┘            └─────┘                        │ HIDS ✅  │
                    decrypts here                     └──────────┘

✅ HIDS sees plaintext
❌ ALB→EC2 is UNENCRYPTED (anyone on internal network can sniff)
❌ No PFS on back leg (no encryption at all)
❌ FAILS requirement #2


OPTION B: ECDHE end-to-end (re-encrypt to EC2) ← CORRECT ✅
┌────────┐   HTTPS    ┌─────┐  HTTPS (ECDHE+PFS)   ┌──────────┐
│ Client │───────────▶│ ALB │──────────────────────▶│   EC2    │
└────────┘            └─────┘                        │ decrypts │
                   re-encrypts                       │ HIDS ✅  │
                 (new TLS session                    └──────────┘
                  to backend)
✅ HIDS sees plaintext AFTER EC2 decrypts at the host
✅ Encrypted both legs (Client→ALB and ALB→EC2)
✅ PFS (ECDHE = ephemeral key per session)
✅ ALL THREE REQUIREMENTS MET


OPTION C: NLB TCP passthrough → EC2 terminates with static RSA
┌────────┐    TLS     ┌─────┐  TLS (passthrough)    ┌──────────┐
│ Client │───────────▶│ NLB │──────────────────────▶│   EC2    │
└────────┘            └─────┘                        │ decrypts │
                  doesn't touch TLS                  │ HIDS ✅  │
                  (TCP passthrough)                  └──────────┘

✅ HIDS sees plaintext
✅ Encrypted in transit
❌ Static RSA key = NO PFS (key leaked → all past sessions decryptable)
❌ FAILS requirement #3
```

---

## Why ECDHE = PFS

```
STATIC RSA:
  ┌─────────────────────────────────────────────┐
  │ Same private key for EVERY session           │
  │ Attacker records traffic for 2 years         │
  │ Key leaks → decrypt ALL 2 years of traffic   │
  │ ❌ No Perfect Forward Secrecy                │
  └─────────────────────────────────────────────┘

ECDHE (Elliptic Curve Diffie-Hellman Ephemeral):
  ┌─────────────────────────────────────────────┐
  │ NEW throwaway key generated PER SESSION      │
  │ Key destroyed after session ends             │
  │ Attacker records traffic for 2 years         │
  │ Key leaks → only FUTURE sessions vulnerable  │
  │ Past sessions = still safe (keys are gone)   │
  │ ✅ Perfect Forward Secrecy                   │
  └─────────────────────────────────────────────┘

PFS = "each session gets its own disposable key"
ECDHE = the algorithm that makes this happen
```

---

## ALB Configuration for PFS

```
ALB HTTPS Listener:
  - Security Policy: ELBSecurityPolicy-FS-* (FS = Forward Secrecy)
  - These policies ONLY include ECDHE cipher suites
  - No static RSA key exchange allowed

Backend Target Group:
  - Protocol: HTTPS (port 443 on EC2)
  - EC2 has its own cert (can be self-signed for internal)
  - HIDS inspects traffic AFTER EC2 decrypts
```

---

## Exam Decision Table

| Question says | Answer |
|---|---|
| "HIDS on instance + PFS + encrypted in transit" | ALB HTTPS (ECDHE) → HTTPS to EC2 |
| "HIDS on instance + no PFS requirement" | ALB terminate → HTTP to EC2 (simpler) |
| "No decryption at ALB at all" | NLB TCP passthrough → EC2 terminates |
| "PFS required" | Must use ECDHE cipher suites (FS policy) |
| "Static RSA" | ❌ No PFS — always wrong if PFS required |

---

## 🧠 Cheat-Sheet One-Liners

- **ALB + HIDS + PFS = ECDHE end-to-end (re-encrypt to EC2). HIDS inspects after host decrypts.**
- **PFS = ECDHE (ephemeral keys per session). Static RSA = no PFS.**
- **"Forward Secrecy" in ALB security policy name = ECDHE only.**
- **HIDS runs ON the host — it sees traffic AFTER the instance decrypts.**
