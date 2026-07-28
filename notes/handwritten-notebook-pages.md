# Handwritten Notebook Pages — Write by Hand to Retain

> Created: 2026-07-28. Write these by hand in your physical notebook.
> Covers 90%+ of your 49 red-priority error patterns.

---

## PAGE 1: Detection Decisions (D1 — 16%)

```
SPECIFIC API + FAST       → EventBridge
ANOMALOUS BEHAVIOR        → GuardDuty  
WHO COULD ACCESS (static) → Access Analyzer
MISCONFIGURATION          → Config / Security Hub
INVESTIGATE FINDING       → Detective
NO FINDING + OPEN QUERY   → CW Logs Insights

"Detect X, zero code/infra" → ALWAYS GuardDuty
  (C2, crypto, exfil, unusual geo — all built-in)

GuardDuty DOES NOT fire on:
  - Blocked attempts (RCP/SCP denied = no successful access)
  - Unknown IPs not in threat feeds
  - Policy changes (that's EventBridge)
  - Misconfigurations (that's Access Analyzer)

Access Analyzer vs GuardDuty:
  AA = STATIC (reads policy text, fires immediately on config)
  GD = DYNAMIC (needs successful + anomalous access)
  Both can fire on same resource INDEPENDENTLY
  RCP blocks access → AA still fires, GD stays silent

StopLogging scope:
  - Member StopLogging → kills THEIR trail only
  - Org trail → still recording, still delivers to EB
  - CW metric filter → ALWAYS blind to StopLogging

Finding progression:
  DNS query only        → Impact (always, any destination)
  Active TCP to mining  → CryptoCurrency  
  Active TCP to C2      → Trojan

CT Lake:
  No backfill (events before EDS creation = never ingested)
  Data vs mgmt (PutObject = data event, not in mgmt-only EDS)
```

### Log Destinations

```
              S3    CW Logs   Firehose   EventBridge
VPC Flow      ✅     ✅        ✅          ❌
CloudTrail    ✅     ✅        ❌          ✅ (auto)
ELB Access    ✅     ❌        ❌          ❌  ← S3 ONLY
WAF Logs      ✅     ✅        ✅          ❌
DNS Query     ❌     ✅        ❌          ❌  ← CW ONLY (public zone)
Resolver      ✅     ✅        ✅          ❌
S3 Access     ✅     ❌        ❌          ❌  ← S3 ONLY
CF Access     ✅     ❌        ❌          ❌  ← S3 ONLY

TRAPS:
  "CW Insights on ELB logs" → impossible (ELB = S3 only, use Athena)
  "Public DNS logging to S3" → impossible (CW Logs only)

DELIVERY MECHANISM:
  VPC Flow Logs → IAM role (ALL targets — only service that does this)
  CloudTrail → S3 = bucket policy, CW Logs = IAM role
  R53 Resolver → CW Logs = log group resource policy
  WAF → CW Logs = log group resource policy

"OLD FOUR" need s3:GetBucketAcl:
  CloudTrail, Config, ELB, S3 server access logging
  (legacy ACL ownership check)
```

---

## PAGE 2: Containment Decision Tree (D2 — 14%)

```
═══ OUTSIDEAWS (creds used from external IP) ═══

  ASK TWO QUESTIONS BEFORE CHOOSING:

  Q1: "Is the role SHARED with other instances?"
  Q2: "Can traffic be DISRUPTED (SLA allows downtime)?"

  ┌─────────────────────────────────────────────────────┐
  │ Dedicated role + CAN disrupt (no SLA)               │
  │ → TokenIssueTime + deny-all SG + AMI + EBS         │
  │   (simplest, kill everything)                       │
  ├─────────────────────────────────────────────────────┤
  │ Dedicated role + CANNOT disrupt (API must stay up)  │
  │ → TokenIssueTime + EBS snapshot + IMDSv2 hop=1     │
  │   (TokenIssueTime is safe: IMDS refreshes new creds│
  │    app keeps working with fresh tokens)             │
  │   NOT deny-all SG (kills ALB/NLB traffic)          │
  │   NOT deregister (causes downtime)                  │
  ├─────────────────────────────────────────────────────┤
  │ Shared role + CAN disrupt                           │
  │ → Deny-all SG on compromised instance ONLY         │
  │   NOT TokenIssueTime (kills ALL instances on role)  │
  ├─────────────────────────────────────────────────────┤
  │ Shared role + CANNOT disrupt                        │
  │ → NF DROP on attacker's external IP (most surgical)│
  │   NOT TokenIssueTime (kills all)                   │
  │   NOT deny-all SG (kills the app)                  │
  │   NACL also valid if single subnet                 │
  └─────────────────────────────────────────────────────┘

═══ INSIDEAWS (creds used from DIFFERENT EC2 same account) ═══

  ALWAYS → Deny-all SG on attacker instance
  NEVER TokenIssueTime (both share role = kills both)

═══ IAM USER LEAKED (keys on GitHub) ═══

  → Deny * inline on IAM user
    (covers: both keys + console password + future AssumeRole)
  → Already-issued STS sessions in Account B = STILL VALID
    (need TokenIssueTime on assumed role separately)
  → Contain ALL paths BEFORE investigating (Detective comes after)

═══ ORDER ═══

  ACQUIRE first → then ISOLATE
  (deny-all blocks SSM needed for memory capture)

  Evidence:
    Volatile memory → No-reboot AMI
    Disk            → EBS snapshot
    Lambda          → NO EBS/AMI — only CW Logs + X-Ray
    Windows won't boot → EC2Rescue (offline, detached volume)

  NLB/ALB (no ASG):
    AMI + EBS → block C2 (NACL/NF) → deregister LAST

  ASG:
    Detach/suspend FIRST → then acquire → isolate

═══ IR SERVICES ═══

  Test IR pipeline     → CreateSampleFindings (not FIS)
  Assess RTO/RPO       → Resilience Hub
  Shift bad AZ         → ARC zonal shift (seconds, LB-level)
  Inject infra failure → FIS (chaos with stop conditions)
  Investigate finding  → Detective (needs finding as entry)
  Custom viz + reuse   → SageMaker notebooks (not Detective)
  Session recording    → Session Manager logging (not CW Agent)

═══ KILL ACTIVE CONNECTIONS ═══

  SG removal = does NOT kill tracked/established flows (stateful)
  NACL deny  = kills EVERY packet instantly (stateless)

  "Active connections + immediately" = ALWAYS NACL

═══ YOUR ERROR PATTERNS (failed 3+ times) ═══

  ❌ Picked TokenIssueTime on shared role (Q1638, Q1640)
     → RULE: read "shared role" FIRST. If shared = eliminate TIT.

  ❌ Picked deny-all SG when API must stay up (Q1633)
     → RULE: "zero downtime" = eliminate deny-all SG + deregister.

  ❌ Picked deregister from ALB (Q1633)
     → RULE: deregister = downtime. TokenIssueTime = non-disruptive.

  ❌ Picked acquire AFTER isolate (Q1598, Q1643)
     → RULE: deny-all blocks SSM. Memory = most perishable. 
       ALWAYS: AMI first → EBS → then isolate.

  ❌ Confused Deny * (user) vs TokenIssueTime (role) (Q942)
     → RULE: IAM user = Deny * (persistent creds).
             Role = TokenIssueTime (temp creds only).

  ❌ Forgot already-issued STS survives Deny * (Q1645)
     → RULE: Deny * on user blocks FUTURE AssumeRole.
       Already-issued tokens in Account B = separate. 
       Need TokenIssueTime on THAT role too.

  ❌ Picked FIS to test IR pipeline (Q934)
     → RULE: FIS = infra failures (AZ, network).
       CreateSampleFindings = security findings through EventBridge.

  ❌ Picked Detective for custom viz (Q996)
     → RULE: Detective = pre-built investigation from finding.
       SageMaker = custom code + arbitrary queries + reusable.

═══ REGIONAL vs GLOBAL (failed Q3 today + Q1398, Q1579) ═══

  REGIONAL (must enable PER REGION):
    GuardDuty, Security Hub, Inspector, Macie, Detective
    Config, KMS keys, ACM certs, State Manager
    S3 Batch Operations (job + manifest + target = SAME region)

  GLOBAL (one place, works everywhere):
    IAM, Organizations (SCPs/RCPs), Route 53, CloudFront
    S3 bucket names (but bucket lives in one region)

  GLOBAL SERVICE EVENTS → us-east-1 ONLY:
    IAM, STS, CloudFront → EventBridge rules must be in us-east-1

  MULTI-ENDPOINT SERVICES (miss one = broken):
    SSM Session Manager = 3: ssm + ssmmessages + ec2messages
    Bedrock             = 2: bedrock + bedrock-runtime
    ECR                 = 2: ecr.api + ecr.dkr

  STATE MANAGER:
    Regional. 4 regions = 4 associations.
    OnBoot + rate = SAME association (not two).
    No org-wide associations exist.

  ACM CERTS:
    CloudFront custom domain = us-east-1 ALWAYS
    ALB = cert in ALB's region
    Can't share certs cross-region

  SECURITY HUB:
    Regional (not global!)
    Cross-region = designate aggregation region
    "Some accounts zero, others working" = membership issue
    "ALL accounts delayed" = latency (2-24hr at scale)

  MRK (Multi-Region Keys):
    Same key ID + same material + INDEPENDENT policies per region
    Update primary policy ≠ update replica (must do each)
    Required for: DynamoDB Global Tables ONLY
    Not required for: CRR, EBS copy, SM replication (all re-encrypt)

  YOUR ERRORS:
    ❌ Thought State Manager has org-wide associations (today Q3)
    ❌ Thought GD auto-covers all regions via delegated admin (Q1398)
    ❌ Picked 1 association for 3 regions (Q1579)
```

---

## PAGE 3: Policy Evaluation + KMS + Governance (D4/D5/D6)

```
FIVE GATES: SCP → RCP → Boundary → Identity → Resource
  All ceilings must allow. Either grant can authorize.
  Explicit Deny in ANY gate = DENIED. Always.

Cross-account KMS:
  Key policy MUST name external account
  Root = same-account delegation ONLY
  ViaService satisfied = S3/SM call KMS server-side
  Session policy does NOT gate server-side KMS

RCP scope:
  Protects YOUR resources only (inbound)
  Outbound to partner bucket = RCP irrelevant (SCP's job)
  Supported: S3, KMS, STS, SQS, SM, DDB, ECR, CW Logs, Cognito,
             CloudFront, WAFv2, + 30 more (45+ total)
  NOT supported: EC2, RDS, Lambda, IAM, SNS, EBS, EFS

Session policy bypass:
  Same-account resource-based naming role → bypasses session ceiling
  Cross-account → ceiling ALWAYS applies (no bypass)

OAC + SSE-KMS = TWO policies:
  1. Bucket policy → CF s3:GetObject
  2. KMS key policy → CF kms:Decrypt
  Miss KMS policy = 403

Default encryption vs policy Deny:
  Policy evaluates headers AS-RECEIVED
  No header + policy check = DENIED (default never fires)

SCP vs Config proactive vs cfn-guard:
  SCP       → blocks API call (ALL paths)
  Proactive → validates CF template (CF-level only)
  cfn-guard → validates in pipeline (bypassable)
  Terraform → direct API (only SCP + detective catch it)

cfn-guard limitations:
  Sees raw template text only
  !Ref, !If, !Sub = JSON objects (can't resolve)
  "true" (string) ≠ true (boolean) = type-strict

State Manager = REGIONAL
  4 regions = 4 associations
  OnBoot + rate = same association
  New target = immediate first run
```

---

## PAGE 4: Infrastructure Troubleshooting (D3 — 18%)

```
TIMEOUT = network problem (SG, NACL, routing, missing endpoint)
ACCESS DENIED = permissions (IAM, policy, key policy)

Interface endpoint = TWO SGs cooperate:
  Lambda SG → outbound 443
  Endpoint SG → inbound 443 from Lambda SG
  Miss either = TIMEOUT

Gateway endpoint policy = hidden allowlist:
  All IAM correct + Access Denied + private subnet
  → check endpoint policy (the invisible 6th gate)

Kill active connections = NACL (stateless, per-packet)
  SG removal won't kill tracked/established flows

Passive inspection (IDS) = Traffic Mirroring → NLB
Inline inspection (IPS)  = Network Firewall or GWLB
GWLB logs show wrong IP  = decapsulate GENEVE outer header

NF TLS inspection = Private CA + distribute to clients
  Users get cert warnings = CA not in trust stores

API Gateway:
  mTLS = custom domain + S3 truststore (PEM + versioning)
  Resource Policy = boundary (before authorizer)
  TOKEN type = only token string (can't see IP/headers)
  REQUEST type = headers + IP + query + context
  Private API timeout = check Resource Policy (not always network)

IoT cert revocation = instant (registry check at TLS handshake)
API GW mTLS revocation = add CRL to S3 truststore

"Public-facing HTTPS" = inbound 0.0.0.0/0 on port 443
  "Highest security" doesn't override being publicly accessible

VPC Flow Logs DO NOT capture:
  169.254.x.x (IMDS, time sync, DNS resolver)
  DHCP, ARP, mirrored traffic, Windows licensing
  Everything else = captured (including EC2↔EC2 same subnet)
```

---

## PAGE 5: Data Protection Operational Details (D5 — 18%)

```
KMS permissions per service:
  S3 upload         → GenerateDataKey (NEVER kms:Encrypt)
  S3 download       → Decrypt
  S3 multipart      → GenerateDataKey + Decrypt (reassembly)
  EBS/DynamoDB      → CreateGrant + DescribeKey (delegates)
  Kinesis consumer  → Decrypt only (no CreateGrant)
  CRR source        → Decrypt
  CRR dest          → GenerateDataKey (NOT Encrypt)

CRR encryption context:
  Rewrites to DEST bucket ARN (not source)
  Custom context from source = preserved → can cause mismatch

S3 server access logging:
  Bucket policy method → works with BucketOwnerEnforced ✅
  ACL method → BREAKS with BucketOwnerEnforced ❌
  Target bucket: NO SSE-KMS, NO Object Lock, NO Requester Pays

Secrets Manager rotation fails:
  "Unable to log into database" = Lambda SG can't reach DB SG
  "Auth failed for new app" = rotation Lambda didn't ALTER USER

Object Lock vs Vault Lock:
  "Fixed retention, auto-expires" → Object Lock Compliance
  "24hr confirm, permanent forever" → Glacier Vault Lock
  "Indefinite, for litigation" → Legal Hold

Sign = private key. Verify = public key (offline OK).
  Can't sign with public (anyone could forge).

S3 Access Grants: broadest prefix wins.
  Root prefix grant (s3://bucket/) = access to everything.
  Overlap = #1 operational misconfiguration.

Imported key = immediate delete (DeleteImportedKeyMaterial)
  No 7-day wait. ScheduleKeyDeletion min = 7 days.
```

---

## PAGE 6: Governance Verbs + RAM/FM (D6 — 14%)

```
VERB → SERVICE:
  Share / visible / accessible     → RAM
  Enforce / associate / re-apply   → Firewall Manager
  Deploy resources / push infra    → StackSets
  Self-service / pull / no IAM     → Service Catalog
  Prevent API call / block         → SCP
  Detect + fix / remediate         → Config + SSM
  Validate template before deploy  → cfn-guard / Config proactive

RAM + FM together:
  DNS FW + Network FW = RAM shares first, FM enforces
  WAF + Shield + SG   = FM creates directly (no RAM)

StackSets:
  Auto-deploy to new accounts ✅
  Auto-remediate drift ❌ NEVER

Native org-wide (don't use StackSets):
  GD, Inspector, SH, Macie, Detective, Config, AA, FM

Conformance pack:
  Deploys rules + remediation config
  Does NOT deploy execution role
  New account = role missing = remediation silently fails

Security Hub setup: E-D-M-A
  Enable → Designate → Members → Access
  "Some zero, others working" = membership issue
  "All delayed" = latency (2-24hr)

WAT = self-reported, no automation, milestones = snapshots
Audit Manager = YOUR evidence (Config + CloudTrail + manual)
Artifact = AWS's reports (SOC, PCI, ISO)

RCP exemptions:
  Management account = exempt
  Service-linked roles = exempt (structural)
  AWS managed KMS keys = exempt
  kms:RetireGrant = exempt
  AWS service principals = exempt via PrincipalIsAWSService condition
```

---

> Total: 6 pages covering 90%+ of 49 red-priority error patterns.
> Write by hand. Read before every drill. Cycle through daily (2 pages/day).
