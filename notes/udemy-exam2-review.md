# Udemy Practice Exam 2 — Wrong Questions Review

> Date: 2026-07-03
> Score: 44/65 (68%)
> Target: 53/65 (81.5%) = comfortable pass
> Purpose: Classify errors and fix knowledge gaps

---

## Error Classification

| Type | Count | Fixable? |
|---|---|---|
| Reading errors | 3 | ✅ Free points on exam day |
| Vocabulary traps | 2 | ✅ Now fixed |
| Knowledge gaps | 6 | ✅ Drilled below |
| TBD (remaining) | 10 | Pending review |

---

## Questions Reviewed

### Q3 — SSE-S3 Already Generates Unique Key Per Object (Knowledge Gap)

**Your answer:** SSE-KMS + encryption context = different key per file
**Correct:** SSE-S3

**Rule:** S3 envelope encryption = EVERY object gets its own unique DEK automatically. Both SSE-S3 and SSE-KMS do this. "Different key per file without overhead" = SSE-S3 (zero config, free).

---

### Q — URI-Specific WAF Rate-Based Rule (Knowledge Gap)

**Your answer:** IP reputation rate-based rule (block all from threat intel lists)
**Correct:** URI-specific rate-based rule on login page

**Rule:** "Attack on /login" → scope the rule to /login. Most surgical response matching scope of attack. WAF rate-based types: Blanket (all pages) vs URI-specific (one path) vs IP reputation (pre-built blocklist).

---

### Q12 — Security Hub Integrations (Knowledge Gap)

**Your wrong picks:** Trusted Advisor → SH + SH consolidates to S3
**Correct:** Firewall Manager → SH + SH sends GD findings to Detective

**Rules:**
- Trusted Advisor does NOT integrate with Security Hub
- Detective RECEIVES from SH (never sends TO)
- Security Hub is REGIONAL (not global), doesn't write to S3
- SH findings to S3 = you build it (EventBridge → Firehose → S3)

---

### Q — S3 Cross-Account Bucket Policy (Reading Error)

**Your answer:** Bucket policy in Finance account
**Correct:** Bucket policy in Audit account (where the bucket lives)

**Rule:** Bucket policies attach to THE BUCKET. Bucket lives in Audit account. Can't create bucket policy in Finance for a bucket that's elsewhere.

---

### Q15 — VPC Endpoint Private DNS Tradeoff (Knowledge Gap)

**Your wrong pick:** "Mandatory multiple subnets" + "private DNS to connect to public APIs"
**Correct:** SG inbound 443 + private DNS ON breaks public API access

**Rules:**
- Private DNS ON = hijacks ALL DNS for that service in your VPC
- Private APIs work via normal URL (good)
- Public APIs for same service become unreachable (bad)
- Multiple subnets = recommended, NOT mandatory
- Interface endpoint = needs SG allowing inbound HTTPS 443

---

### Q — Traffic Mirroring Filter Wording (Vocabulary Trap)

**Your answer:** VPC Flow Logs (confused by "reject/accept" wording)
**Correct:** Traffic Mirroring with filter rules

**Rules:**
- Traffic Mirroring filter "reject" = don't copy (skip). "accept" = copy (mirror).
- NOT firewall block/allow. Just what to send to your appliance.
- "Content inspection" = ALWAYS Traffic Mirroring or Network Firewall. NEVER Flow Logs.
- Flow Logs = metadata only (IP/port/accept/reject, no payload).

---

### Q — GuardDuty Suppression Rule Filter Criteria (Vocabulary Trap)

**Your answer:** Trusted IP list as second filter criterion
**Correct:** API caller IPv4 address as second filter criterion

**Rules:**
- Trusted IP list = standalone feature (prevents ALL findings from that IP)
- Suppression rule filter fields: finding type, severity, API caller IPv4, resource, etc.
- "Trusted IP list" is NOT a filter field inside suppression rules
- Trusted IP list = nuclear (blinds GD to ALL threats from IP)
- Suppression rule = surgical (only suppresses ONE finding type from IP)

---

### Q — CloudTrail → CloudWatch Logs (Reading Error)

**Your answer:** CloudTrail → CloudWatch Alarm + ConsoleSignin
**Correct:** CloudTrail → CloudWatch Logs + ConsoleLogin

**Rules:**
- CloudTrail sends to CloudWatch LOGS (not Alarm directly)
- Alarm is created ON TOP of metric filter
- Correct API name = ConsoleLogin (not ConsoleSignin)

---

### Q — Gateway Endpoint Policy for Exfil Prevention (Knowledge Gap)

**Your answer:** Inline policy on instance role (restrict aws:ResourceOrgID)
**Correct:** Modify S3 Gateway VPC endpoint policy (aws:ResourceOrgID + aws:PrincipalOrgID)

**Rules:**
- Compromised instance = attacker may have OWN credentials (bypass role)
- Gateway endpoint policy = network-level gate (credential-agnostic)
- Private subnet + no internet = endpoint is ONLY path to S3
- Restrict endpoint policy to company buckets = attacker can't reach external buckets
- IAM role restriction = identity gate (bypassed with attacker's own creds)

---

### Q — KMS Imported Key Immediate Delete (Knowledge Gap)

**Your answer:** ScheduleKeyDeletion with minimum wait time
**Correct:** Import key function (DeleteImportedKeyMaterial = instant)

**Rules:**
- ScheduleKeyDeletion minimum = 7 days (can't go lower)
- Imported key material can be deleted IMMEDIATELY (no wait)
- DisableKey = instant but reversible
- "Within 24 hours" = only imported material deletion satisfies

---

### Q — KMS Key Creator ≠ Owner + Root ≠ Full Access (Knowledge Gap)

**Your picks:** Root has full permission + Resource-based policies description
**Correct:** Creator ≠ owner (needs explicit permission) + kms:CreateKey can set initial policy

**Rules:**
- Key creator does NOT automatically own or have permission on the key
- Identity with kms:CreateKey CAN set initial key policy (bootstrap themselves)
- Root does NOT automatically have full permission on KMS keys
- Nobody has automatic access — must be explicitly granted via key policy/IAM/grant
- KMS authorization: key policy + IAM policy + grants (NO ACLs)

---

## Patterns to Add to Cheat Sheet

1. SSE-S3 = unique DEK per object automatically (no config needed)
2. WAF rate-based: Blanket vs URI-specific vs IP reputation
3. Trusted Advisor ≠ Security Hub integration
4. Security Hub = regional (not global, not S3)
5. VPC endpoint private DNS ON = hijacks all DNS for that service
6. Traffic Mirroring reject/accept = skip/copy (not block/allow)
7. Gateway endpoint policy = network gate (credential-agnostic exfil prevention)
8. Imported key material = immediate delete (no 7-day wait)
9. KMS: creator ≠ owner, root ≠ full access

---

### Q — CloudFront Authorization Header Forwarding (Knowledge Gap)

**Your answer:** Configure the CloudFront origin request policy to forward the Authorization header to the origin
**Correct:** Create a cache policy, associate it with the cache behavior that must forward the Authorization header

**Rules:**
- `Authorization` header MUST be in Cache Policy (part of cache key)
- Origin Request Policy with Authorization → HTTP 400 error (CloudFront rejects at creation)
- Why: prevents serving cached authenticated responses to unauthenticated users
- Viewer Request Policy = doesn't exist for header forwarding (distractor)

---

### Q — Credential Leak IR Ordering (Ordering Question)

**Scenario:** Service account access key published on GitHub. No compromise yet. Critical production app with hard-coded credentials. Minimize downtime.

**Your answer:** Revoke STS first → Inactivate key → Create new → Update app → Delete console
**Correct order:**
1. Inactivate the publicly exposed IAM access key
2. Create a new access key and secret access key pair
3. Update the application to use the new credentials
4. Revoke any temporary STS credentials
5. Delete AWS Management Console credentials

**Why Revoke STS first is wrong:** The exposed key is still active while you revoke sessions. Attacker can call AssumeRole again or make direct API calls. "Mopping the floor while faucet is running."

**Why Delete console credentials (step 5) even though question says "service account":** Attacker may have ENABLED console access via CreateLoginProfile using the leaked key. IR best practice = close ALL doors.

**Principle:** Contain (inactivate) → Replace (new key) → Restore (update app) → Clean up (revoke STS + delete console)

**Rule:** Every long-term credential belongs to an IAM user. One user can have: 2 access keys + 1 password + MFA. Roles have NO long-term credentials.

---

### Q — SSM VPC Endpoints (THREE required, not one) (Reading Error)

**Scenario:** Private EC2, no internet, need Systems Manager. Select THREE.

**Your picks:** SSM Agent ✅ + IAM instance profile on EC2 ✅ + ONE endpoint (ssm only) ❌
**Correct:** SSM Agent + IAM instance profile on EC2 + THREE endpoints (ssm + ssmmessages + ec2messages)

**Rules:**
- Three VPC endpoints required: `com.amazonaws.[region].ssm` + `.ssmmessages` + `.ec2messages`
- Miss any one = connection fails
- IAM instance profile goes on EC2 (not on VPC endpoint policy)
- "Allow outbound internet" contradicts "without internet access" requirement

**Reading trap:** One option says "a VPC endpoint" (singular, ssm only). Another says "three VPC endpoints" (all three listed). Must read carefully.

---

### Q56 — Lambda Permissions = Execution Role (Reading Error)

**Scenario:** Lambda needs access to CMK-encrypted S3 data. Each function needs its own access control.

**Your answer:** Lambda assumes IAM role for AWS-managed key
**Correct:** Establish a Lambda execution role with KMS access for each function

**Why wrong:** (1) Question says customer managed key, you picked AWS-managed. (2) Lambda doesn't "assume" a separate role — it already HAS an execution role.

**Rule:** Lambda permissions = execution role. Always. Can't attach IAM policies directly to functions. Lambda runs AS its execution role.

---

## Remaining Questions (TBD)

6 more wrong questions to review.
