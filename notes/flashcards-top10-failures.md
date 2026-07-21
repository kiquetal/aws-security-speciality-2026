# Top 10 Repeat Failures — DO NOT DO THIS

> Print this. Read before EVERY drill and exam day.
> These are patterns you've failed 3+ times. Your brain defaults to the wrong answer.

---

## 🔴 1. Traffic Mirroring vs Flow Logs (4x failed)

```
"Full packet / inspect content / IDS / payload" = TRAFFIC MIRRORING
"Metadata / who talked to whom / top talkers" = FLOW LOGS

Flow Logs CANNOT inspect content. Period.
Traffic Mirroring = PASSIVE (copy). GWLB = INLINE (block).
```

❌ You pick: Flow Logs or GWLB
✅ Correct: Traffic Mirroring → NLB → IDS

---

## 🔴 2. NACL vs SG for Active Connections (3x failed)

```
"Kill EXISTING active connections immediately" = NACL (stateless)
"Block FUTURE connections" = SG works fine

SG = stateful = conntrack table = existing flows SURVIVE rule removal
NACL = stateless = every packet evaluated fresh = instant kill
```

❌ You pick: Remove SG rules
✅ Correct: NACL deny all

---

## 🔴 3. Surgical vs Nuclear Containment (3x failed)

```
"Minimize disruption" = most TARGETED option wins

NUCLEAR (affects everyone): bucket deny-all, DenyAll policy, deny-all SG
SURGICAL (affects attacker only): revoke sessions, NF DROP on IP, SG on one instance

ASK: "Does my answer affect ONLY the attacker?" No → wrong answer.
```

❌ You pick: Bucket deny-all / DenyAll policy
✅ Correct: Revoke sessions / NF DROP on attacker IP

---

## 🔴 4. OutsideAWS + Shared Role (4x failed)

```
BEFORE picking TokenIssueTime, ask TWO questions:
  1. "Is the role SHARED?" → Yes = TokenIssueTime kills ALL instances
  2. "Can traffic be disrupted?" → No = Deny-all SG kills the app

Both blocked → NF DROP on attacker IP (surgical, zero disruption)
```

❌ You pick: TokenIssueTime (kills all sharing the role)
✅ Correct: NF DROP on attacker IP

---

## 🔴 5. Detect vs Prevent — Verb Selection (9x failed historically)

```
"DETECT / alert / notify" + "least overhead" = GuardDuty (ALWAYS)
"PREVENT / block / restrict" = Policy (SCP, RCP, key policy, bucket policy)

GuardDuty = the ALARM. CloudTrail = the LOG. Access Analyzer = the AUDIT.
```

❌ You pick: CloudTrail / EventBridge for behavioral detection
✅ Correct: GuardDuty (zero code, zero infra)

---

## 🔴 6. "Investigate without affecting production" (3x failed)

```
"Without making changes" / "don't affect production" / "collect evidence"
= READ-ONLY actions ONLY

→ Eliminate ALL containment options (DenyAll, quarantine, SG change)
→ Answer = Detective / CloudTrail / read-only access
```

❌ You pick: DenyAll / quarantine / containment action
✅ Correct: Detective (read-only investigation)

---

## 🔴 7. cfn-guard Intrinsics (3x failed)

```
cfn-guard sees: {"Ref": "X"} → an OBJECT, not a resolved value
cfn-guard sees: {"Fn::If": [...]} → an OBJECT
cfn-guard sees: "true" (string) → NOT same as true (boolean)

ANY intrinsic = FAIL (object ≠ expected type)
"true" string ≠ true boolean = FAIL (type-strict)
```

❌ You pick: PASS (thinking it resolves)
✅ Correct: FAIL (static text, can't resolve, type mismatch)

---

## 🔴 8. S3 Logging ACLs (4x failed)

```
S3 server access logging = logging.s3.amazonaws.com service principal
BucketOwnerEnforced (ACLs disabled) = ACL method BREAKS
Fix: bucket policy for logging.s3.amazonaws.com OR switch to BucketOwnerPreferred + ACL

Config remediation for logging needs: s3:GetBucketAcl (legacy ownership check)
```

❌ You pick: Only one method works
✅ Correct: BOTH bucket policy and ACL methods are valid fixes

---

## 🔴 9. Default Encryption vs Policy Deny (3x failed)

```
Policy (SCP / bucket policy) evaluates request AS-RECEIVED
Default encryption applies AFTER policy passes

Missing header + policy check = DENIED (default encryption never fires)
```

❌ You pick: "Default handles it, upload succeeds"
✅ Correct: DENIED — policy sees no header, rejects before default applies

---

## 🔴 10. CW Agent vs SSM Agent (3x failed)

```
"Ship custom logs to CW Logs" = CloudWatch agent (ALWAYS)
"Execute commands / sessions / patches" = SSM agent

SSM agent CAN install CW agent but CANNOT replace it for log shipping.
"No log loss during scaling" = CW agent (continuous stream)
EBS snapshots = batch (has loss window)
```

❌ You pick: SSM agent / EBS snapshots
✅ Correct: CW agent (continuous, no gap)

---

## Exam-Day Protocol

Before answering ANY question:
1. Read the LAST sentence first (constraint/requirement)
2. Check: does this match any of the 10 patterns above?
3. If yes → pick the OPPOSITE of your gut instinct
4. If "minimize disruption" → eliminate all nuclear/broad options
5. If "active connections" → NACL
6. If "full packet" → Traffic Mirroring
7. If "without affecting" → read-only only (Detective)
