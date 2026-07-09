# WAF Bot Control — Flashcard

> Blueprint ref: Task 3.1 (edge security)
> Missed Q3 + Q5 in Session 120. Lock these patterns.

---

## Three Exam Angles (Always One of These)

| Question Pattern | Answer |
|---|---|
| "Legitimate traffic blocked by Bot Control" | **Scope-down statement** (exempt known-good) |
| "Sophisticated bot gets through Common" | **Targeted level** (behavioral, not signature) |
| "Server/mobile can't pass Challenge/CAPTCHA" | **Scope-down statement** (both need browser) |

---

## Common vs Targeted Protection Level

| | Common | Targeted |
|---|---|---|
| **How it detects** | Signatures (User-Agent strings, known bot IPs) | Behavioral (JS tokens, fingerprinting, session tracking) |
| **Defeats** | Simple bots with known patterns | Sophisticated bots rotating IPs + headers |
| **Fails when** | Attacker rotates User-Agent/IP per request | N/A (much harder to evade) |
| **Cost** | Lower | Higher |
| **Exam signal** | "known bot" / "obvious crawler" | "distributed" / "rotating" / "low-volume per IP" |

---

## Challenge vs CAPTCHA vs Scope-Down

| Mechanism | Requires | Use When |
|---|---|---|
| **Challenge** | Browser with JS engine (silent) | Block bots that can't execute JS |
| **CAPTCHA** | Browser + human (visible puzzle) | Block bots AND automated scripts |
| **Scope-down** | Nothing (header/IP match) | Exempt known-good non-browser clients |

```
Browser client (web app)     → Challenge works ✅
Mobile app (no JS engine)    → Challenge fails ❌ → use scope-down
Server-to-server (no browser)→ Challenge fails ❌ → use scope-down
                              → CAPTCHA also fails ❌ → use scope-down

RULE: If client has no browser → ONLY scope-down can exempt it.
      Never switch between Challenge/CAPTCHA — both fail.
```

---

## Verified vs Unverified Bots

| Category | Examples | Default Action |
|---|---|---|
| **Verified** | Googlebot, Bingbot, GPTBot | Labeled but ALLOWED (not blocked) |
| **Unverified** | Scrapers, stuffers, unknown | Challenge/Block |

AWS verifies via reverse DNS + IP. You can override (block verified or allow unverified) but defaults matter for exam.

---

## Scope-Down Statement — How It Works

```
Bot Control rule group applied to: ALL requests
Scope-down: EXCLUDE requests where X-Api-Key header = "known-partner"

Result:
  Browser users     → Bot Control evaluates (Challenge/block bots)
  Known partner API → SKIPPED (scope-down excludes it)
  Mobile app        → SKIPPED (scope-down by custom header)
```

Scope-down = "only apply this rule group to requests matching THIS condition." Excluded traffic bypasses the entire rule group.

---

## 🧠 Exam One-Liners

- **"Legitimate server/mobile blocked by Bot Control" = scope-down statement.** Challenge AND CAPTCHA both need browser.
- **"Sophisticated distributed attack, rotating IPs+headers" = Targeted level.** Common = signatures only (useless if attacker rotates).
- **Common = known patterns. Targeted = behavioral + tokens.** "Rotating/distributed" = always Targeted.
- **Verified bots (Google) = allowed by default.** Unverified = challenged/blocked by default.
- **Scope-down = surgical exemption.** Identify known-good by header, IP, or path → exclude from rule group.
