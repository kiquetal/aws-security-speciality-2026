# Flashcards: Quotas & Condition Keys That Trick You

> These are pure recall items. No understanding needed — just burn them in.

---

## The 5 Numbers (ascending order: 4-5-8-32-5120)

| Number | What | Memory Hook |
|---|---|---|
| **4 KB** | KMS direct Encrypt/Decrypt max | "4 KB = 4 Kilo Bytes = tiny, use envelope for anything real" |
| **5** | Max SCPs/RCPs attached per target | "HIGH 5 = 5 policies slapping one OU" |
| **8 KB** | WAF body inspection default | "8 KB = ate KB = WAF ate only the first bite" |
| **32 KB** | KMS key policy max size | "32 = 2^5 = key policy is a power of 2" |
| **5,120** | SCP/RCP max characters | "5K characters = about 1 page of JSON" |

### Drill Pattern (cover right column, recall)

```
KMS direct encrypt max?     → 4 KB
SCPs per target?            → 5
WAF body default?           → 8 KB
Key policy max?             → 32 KB
SCP character limit?        → 5,120
```

---

## The 3 "Always Works / Can't Be Denied" Items

| Item | Rule | Memory Hook |
|---|---|---|
| **GetCallerIdentity** | Cannot be denied by ANY policy (IAM, SCP, boundary, session) | "WHO AM I? — existential questions can't be silenced" |
| **SLRs vs RCPs** | SLRs are exempt from RCPs | "Service-Linked = Resource-exempt (both start with consonants)" |
| **Management account** | Exempt from BOTH SCPs and RCPs | "The boss doesn't follow their own rules" |

---

## The 5 Condition Keys That Appear on Every Exam

| Key | When You See | Memory Hook |
|---|---|---|
| **aws:TokenIssueTime** | "Revoke sessions" / "compromised credentials" | "TOKEN = birth certificate. ISSUE TIME = birthday. Deny before birthday X" |
| **aws:PrincipalOrgID** | "Restrict to my org" / "block external" | "Principal = person. OrgID = their badge. No badge = no entry" |
| **aws:PrincipalIsAWSService** | "Exempt CloudTrail/Config from deny rules" | "Is this a ROBOT? Robots get a pass" |
| **sts:ExternalId** | "Third-party vendor" / "confused deputy" | "External = outsider. ID = prove you're the right outsider" |
| **aws:RequestTag/Key** | "Enforce tagging at creation" | "Request = what you're ASKING for. Must include the tag" |

### Drill Pattern (cover right column)

```
Revoke active sessions?         → aws:TokenIssueTime
Block external callers?         → aws:PrincipalOrgID
Exempt AWS services from deny?  → aws:PrincipalIsAWSService
Prevent confused deputy?        → sts:ExternalId
Force tag at resource creation? → aws:RequestTag/Key
```

---

## The 3 Time-Based Quotas

| Item | Min | Max/Default |
|---|---|---|
| **KMS key deletion wait** | 7 days | 30 days (default) |
| **Secrets Manager deletion** | 7 days | 30 days |
| **Role chaining session** | — | 1 hour (always, can't increase) |

### Drill Pattern

```
KMS deletion wait range?        → 7-30 days
Secrets Manager deletion range? → 7-30 days (same!)
Role chaining max duration?     → 1 hour (always resets)
```

---

## Speed Recall Test (do this once a day until exam)

Cover answers. Say them out loud. Check.

1. KMS direct encrypt max? ___
2. SCPs per target? ___
3. WAF body default? ___
4. Key policy max? ___
5. SCP char limit? ___
6. Can't-be-denied STS API? ___
7. Revoke sessions condition key? ___
8. KMS deletion min wait? ___
9. Role chaining max? ___
10. Exempt AWS services condition? ___

Answers: 4KB, 5, 8KB, 32KB, 5120, GetCallerIdentity, aws:TokenIssueTime, 7 days, 1 hour, aws:PrincipalIsAWSService
