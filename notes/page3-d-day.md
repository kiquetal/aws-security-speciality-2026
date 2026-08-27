# PAGE 3 — D-DAY (Policy + KMS + Governance — D4/D5/D6)

> Write by hand. Read once before entering the exam room.

---

## 5 Gates (Policy Evaluation)

```
SCP → RCP → Boundary → Identity → Resource
│         │         │          │         │
CEILING   CEILING   CEILING    GRANT     GRANT

Effective = all ceilings allow + either grant authorizes
Explicit Deny in ANY gate = DENIED. Always.
```

## Cross-Account Rules

```
Same-account:  identity OR resource policy can grant (either one)
Cross-account: BOTH sides must grant (identity + resource)
Exception:     KMS ALWAYS needs both sides (key policy + identity)

Session policy bypass: same-account resource-based naming role → bypasses ceiling
Cross-account: session ceiling ALWAYS applies (no bypass)
```

## SCP Rules

```
SCP = ceiling (Allow list). Action not listed = implicitly denied.
SCP on OU → applies to ALL principals in ALL accounts under it.
Management account = EXEMPT from SCP and RCP.
SCP cannot be bypassed by anything (not bucket policy, not key policy).
```

## RCP Rules

```
RCP protects YOUR resources only (inbound).
Outbound to partner's bucket = RCP irrelevant (SCP's job).
SLRs = exempt from RCP (structural).
AWS service principals = exempt via PrincipalIsAWSService condition.
```

## KMS — The Rules

```
Root in key policy = enables IAM delegation (NOT blanket grant)
Each principal still needs explicit kms:Decrypt in identity policy.

Cross-account KMS: key policy MUST name external account.
Root = same-account delegation only. Never cross-account.

S3 NEVER uses kms:Encrypt (always GenerateDataKey)
Multipart = GenerateDataKey + Decrypt (reassembly)
CRR role = D-G-F (Decrypt source + GenerateDataKey dest + ForReplication)
EBS/DynamoDB = CreateGrant + DescribeKey (delegate via grants)
Kinesis consumer = Decrypt only (no CreateGrant, no DescribeKey)
```

## Default Encryption vs Policy Deny

```
Policy evaluates headers AS-RECEIVED (before default applies)
No header + policy check = DENIED (default never fires)
"Policy first, default last"
```

## ViaService + SCP

```
SCP Deny kms:* unless ViaService = s3
→ S3 read/write: ViaService satisfied ✅ (S3 calls KMS server-side)
→ Direct CLI kms:decrypt: no ViaService = DENIED ❌
```

## Governance (D6)

```
cfn-guard         = pipeline only (bypassable via Console)
Config proactive  = CF service-level (can't bypass, catches all CF)
CF Hook           = same layer as Config proactive (custom Lambda)
SCP               = ALL paths (CLI, Console, CF, Terraform)
Terraform         = direct API → only SCP + Config detective catch it

Deploy via Console CF:  proactive ✅ + Hook ✅ + SCP ✅ (NOT cfn-guard)
Deploy via Terraform:   SCP ✅ + detective ✅ (nothing else fires)
```

## E-D-M-A (Security Hub Setup)

```
Enable → Designate → Members → Access
"Eat Dinner, Meet Amigos"
```

## Object Lock

```
Compliance = nobody can delete (not even root). Fixed period. Auto-expires.
Governance = admin can override with BypassGovernanceRetention.
Legal Hold = indefinite (no expiry). For litigation.
Vault Lock = permanent POLICY (24hr confirm, then irreversible forever).

Can extend Compliance (more restrictive) ✅
Can add Legal Hold on top ✅  
CANNOT shorten/remove/downgrade Compliance to Governance ❌
```
