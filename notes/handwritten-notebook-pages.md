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
═══ FIVE GATES (policy evaluation) ═══

  SCP → RCP → Boundary → Identity → Resource
  
  Gates 1-3 = CEILINGS (never grant, only restrict)
  Gates 4-5 = GRANTS (actually give access)
  Effective = all ceilings allow + either grant authorizes
  Explicit Deny in ANY gate = DENIED. Always.

  Same-account: identity OR resource policy can grant
  Cross-account: BOTH sides must grant (except KMS = always both)

═══ CROSS-ACCOUNT KMS (failed 5x: Q541, Q669, Q850, Q870, Q974) ═══

  Key policy MUST name external account explicitly
  Root in key policy = same-account delegation ONLY
  "Root enables IAM delegation" ≠ "root grants everyone access"
  Each principal still needs explicit kms:Decrypt

  Full cross-account SSE-KMS read needs:
    1. Key policy names Account B (or B's role)
    2. Account B identity policy has kms:Decrypt
    3. Account B SCP allows kms:Decrypt
    4. RCP on Account A allows (PrincipalOrgID matches)
    5. Bucket policy grants Account B s3:GetObject

  ViaService satisfied = S3/SM call KMS server-side
  Session policy does NOT gate server-side KMS calls
    (session only restricts caller's DIRECT API calls)

═══ RCP SCOPE (failed 3x: Q1581, Q683, Q698) ═══

  Protects YOUR resources only (inbound)
  Outbound to partner bucket = RCP irrelevant (SCP's job)

  Lambda writes to own bucket + partner bucket:
    Own = PrincipalOrgID matches → allowed
    Partner = not your resource → RCP doesn't apply → allowed

  Supported: S3, KMS, STS, SQS, SM, DDB, ECR, CW Logs, Cognito,
             CloudFront, WAFv2, + 30 more (45+ total)
  NOT supported: EC2, RDS, Lambda, IAM, SNS, EBS, EFS

  Exemptions:
    Management account resources = exempt
    Service-linked roles = exempt (structural)
    AWS managed KMS keys = exempt
    kms:RetireGrant = exempt
    AWS service principals = exempt via PrincipalIsAWSService

═══ SESSION POLICY (failed 2x: Q96, Q169) ═══

  Session policy = ceiling on AssumeRole session
  Effective = role ∩ session ∩ boundary ∩ SCP

  Bypass rule:
    Same-account resource-based naming role → bypasses session ceiling
    Cross-account → ceiling ALWAYS applies (no bypass)

  Server-side KMS:
    S3 calls KMS internally → session policy doesn't gate it
    Direct kms:Decrypt from YOUR code → session policy DOES gate it

═══ DATA PERIMETER (failed 2x: Q398, Q1095) ═══

  Block outsiders IN  → RCP (PrincipalOrgID on resources)
  Block insiders OUT  → SCP (ResourceAccount condition on principals)
  Full perimeter = BOTH together

═══ OAC + SSE-KMS ═══

  TWO policies needed:
    1. Bucket policy → CF s3:GetObject (cloudfront.amazonaws.com)
    2. KMS key policy → CF kms:Decrypt (cloudfront.amazonaws.com)
  Miss KMS policy = 403

═══ DEFAULT ENCRYPTION vs POLICY DENY (failed 3x: Q426, Q626, Q643) ═══

  Policy evaluates headers AS-RECEIVED (before default applies)
  No header + policy check = DENIED (default never fires)

  "Upload without flags + bucket has default + policy checks header"
    → ALWAYS DENIED

═══ SCP vs CONFIG PROACTIVE vs CFN-GUARD (failed 4x) ═══

  SCP       → blocks API call (ALL paths: CLI, Console, CF, Terraform)
  Proactive → validates CF template (CF-level only, catches Console CF)
  cfn-guard → validates in pipeline (bypassable via Console/CLI)
  CF Hook   → same level as Config proactive (CF service-level)
  Terraform → direct API (only SCP + Config detective catch it)

  Console direct (no CF):     only SCP + Config detective fire
  Console CF deploy:          proactive + Hook + SCP fire (not cfn-guard)
  Pipeline CF deploy:         cfn-guard + proactive + Hook + SCP all fire

  cfn-guard limitations:
    Sees raw template text only
    !Ref, !If, !Sub = JSON objects (can't resolve)
    "true" (string) ≠ true (boolean) = type-strict
    Parameter overrides at deploy time bypass validation

═══ ViaService + SCP (failed 3x: Q488, Q495) ═══

  SCP Deny kms:* unless ViaService = s3
  → S3 read/write: S3 calls KMS server-side → ViaService satisfied ✅
  → Direct kms:Decrypt from CLI/code: no ViaService context → DENIED ❌
  → DynamoDB: sets ViaService but value ≠ s3 → DENIED ❌

  RULE: ViaService = which SERVICE made the KMS call on your behalf
        Direct call = no service involved = no ViaService = SCP fires

═══ SIGN vs ENCRYPT (failed 3x: Q1596, Q812, Q824) ═══

  Sign = private key → verify = public key (integrity + non-repudiation)
  Encrypt = public key → decrypt = private key (confidentiality)

  "Customers verify offline air-gapped" = download public key, OpenSSL
  Can't sign with public (anyone could forge)
  KMS: one key = one purpose at creation (sign OR encrypt, not both)

═══ RAM vs KMS GRANTS (failed 2x: Q11, Q37) ═══

  RAM doesn't support KMS (RAM = infrastructure: TGW, subnets, DNS FW)
  KMS cross-account = KMS Grants (per-operation, per-principal, revocable)
  Key policy 32KB limit → ~200 principals max
  Grants = unlimited, one API call per onboard, RevokeGrant to offboard

═══ KMS KEY POLICY ROOT TRAP (failed 3x: Q264, Q503, Q687) ═══

  Root in key policy = "enable IAM policies to control this key"
  Root ≠ "everyone in the account automatically has access"
  Each principal STILL needs explicit kms:Decrypt in identity policy

═══ YOUR ERROR PATTERNS ═══

  ❌ Thought root in key policy = blanket grant (Q264, Q503)
     → RULE: root = delegation. Each principal needs explicit perms.

  ❌ Thought RCP blocks outbound to partner (Q683, Q698)
     → RULE: RCP = YOUR resources. Partner's bucket = not yours.

  ❌ Thought session policy blocks server-side KMS (Q591, Q679)
     → RULE: S3 calls KMS internally. Session gates YOUR calls only.

  ❌ Thought default encryption overrides policy Deny (Q426, Q626)
     → RULE: policy checks FIRST. No header = denied. Default = after.

  ❌ Thought cross-account KMS works with root only (Q541, Q669)
     → RULE: key policy MUST name external account. Root = same-account.

  ❌ Thought ViaService applies to direct CLI calls (Q488, Q495)
     → RULE: direct call = no service = no ViaService = SCP fires.

  ❌ Thought you can sign with public key (Q812, Q824)
     → RULE: sign = private. verify = public. Always.

═══ KMS KEY ORIGINS + CAPABILITIES ═══

                    │ Symmetric │ Asymmetric │ HMAC │ AWS Service │
  ──────────────────┼───────────┼────────────┼──────┼─────────────┤
  AWS_KMS (default) │    ✅      │     ✅      │  ✅   │     ✅       │
  EXTERNAL (import) │    ✅      │     ✅      │  ✅   │     ✅       │
  Custom Key Store  │    ✅      │     ❌      │  ❌   │     ✅       │
  XKS (external)    │    ✅      │     ❌      │  ❌   │     ✅       │
  CloudHSM DIRECT   │    ✅      │     ✅      │  ✅   │     ❌       │

  Custom Key Store + XKS = SYMMETRIC ONLY through KMS
  CloudHSM DIRECT = everything BUT no S3/EBS/RDS integration
  Imported = all types BUT can't import into custom key store

  "Single-tenant + S3/EBS/RDS"        → Custom key store
  "Asymmetric signing on dedicated HSM" → CloudHSM direct
  "Keys NEVER in AWS"                  → XKS
  "Full control + native integration"  → Customer managed (AWS_KMS)

  WHERE KEYS PHYSICALLY LIVE:
    AWS KMS default   → AWS multi-tenant HSMs (shared infra)
    CloudHSM direct   → YOUR dedicated HSMs, YOUR VPC (still in AWS)
    Custom Key Store   → SAME CloudHSM cluster, accessed via KMS API
    XKS               → Your on-prem HSM / data center (OUTSIDE AWS)

  "Keys never in AWS" = ONLY XKS satisfies this
  CloudHSM = in AWS (your account, your VPC, but AWS infrastructure)
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

Network analysis tools:
  "Find ALL exposed resources"          → Network Access Analyzer
  "Why can't A reach B? Hop-by-hop?"    → Reachability Analyzer
  "Is THIS port actually reachable?"    → Inspector Network
  "Find bad SGs org-wide + auto-fix"    → FM SG audit
  NAA FINDS. RA EXPLAINS. Different tools.

Service role pattern (same concept, different services):
  CF service role      → cloudformation.amazonaws.com assumes role
  VPC Flow Logs role   → vpc-flow-logs.amazonaws.com assumes role
  EC2 instance profile → ec2.amazonaws.com assumes role
  All three = "a service assumes a role YOU created"
  Developer needs iam:PassRole (hand keys to service)
  Developer does NOT need the role's actual permissions

  PassRole vs AssumeRole:
    PassRole = "give car keys to valet" (hand role to service)
    AssumeRole = "drive the car yourself" (become the role)
    PassRole can't escalate. AssumeRole can.

Public IP between EC2s:
  Private IP traffic → stays in VPC → SG can ref instance ID/SG
  Public IP traffic → exits via IGW → source = public IP
  SG ref sg-aaa won't match public IP traffic = TIMEOUT
  Fix: allow the other instance's PUBLIC IP explicitly

IPv4 outbound-only = NAT Gateway
IPv6 outbound-only = Egress-Only Internet Gateway
  NAT doesn't support IPv6. Egress-Only IGW = one-way gate.

Kinesis encrypted stream (failed 2x: Q918, Q950):
  Consumer needs: kms:Decrypt ONLY (DescribeKey = admin, not consumer)
  Producer needs: kms:GenerateDataKey
  Timeout = BOTH endpoints needed (Kinesis + KMS Interface)
  + BOTH SGs cooperate (Lambda outbound + endpoint inbound)
  S3 SSE-KMS = server-side (no KMS endpoint needed)
  Direct kms:Decrypt from YOUR code = needs KMS endpoint

Secrets Manager rotation failure (failed 2x: Q1242, Q1254):
  "Unable to log into database" = Lambda SG can't reach DB SG
  "Auth failed for new app" = rotation Lambda didn't ALTER USER
  SM endpoint works ≠ DB is reachable (different network path)
  Fix: Lambda SG egress to DB port + DB SG ingress from Lambda SG

Inspector SBOM (failed 2x: Q1059, Q1119):
  No built-in scheduler (no Console option)
  Schedule with: EventBridge rule + Lambda + CreateSbomExport API
  Export needs: bucket policy for inspector2.amazonaws.com
  NOT SSM, NOT custom scripts — native API only

C2Activity + hardcoded IP (no DNS):
  DNS Firewall useless (attacker doesn't need DNS)
  → Network Firewall DROP on C2 IP
  DGA (unpredictable domains) = flip to DNS Firewall ALLOW-LIST
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

kms:DescribeKey — WHEN is it needed?
  YOU calling S3 directly        → NOT needed (GenerateDataKey + Decrypt)
  AWS SERVICE writing to your bucket → NEEDED in key policy
    (Bedrock, Macie, Config, CloudTrail = validate key first)
  Cross-account KEY POLICY (on key OWNER side, granted TO external caller)
    → NEEDED (AWS validates key metadata for external principals)
    → Account A key policy grants Account B: Decrypt + GenerateDataKey + DescribeKey
  CreateGrant services (EBS, DDB) → NEEDED (validate before grant)
  Kinesis consumer/producer      → NOT needed (direct call, no grant)
  CRR replication role           → NOT needed (D-G-F only, no DescribeKey)
  
  RULE: "Service delegates via grant" OR "service principal in key policy"
        OR "cross-account key policy"
        → DescribeKey needed
        "You call directly (same-account)" → not needed

═══ SIGN vs ENCRYPT (asymmetric KMS) ═══

  Sign = PRIVATE key → verify = PUBLIC key
    → Integrity + non-repudiation
    → "Customers verify offline air-gapped" = download public key, OpenSSL
    → Can't sign with public (anyone could forge — no non-repudiation)

  Encrypt = PUBLIC key → decrypt = PRIVATE key
    → Confidentiality
    → Anyone can encrypt TO you. Only you can decrypt.

  KMS: one key = one purpose at creation (sign OR encrypt, NOT both)
  ECC keys = SIGNING ONLY (never encryption)
  RSA keys = choose one at creation (SIGN_VERIFY or ENCRYPT_DECRYPT)

  Mnemonic: "Sign = YOUR secret hand. Verify = everyone can look."

═══ S3 VERSIONING REQUIREMENTS (what NEEDS versioning?) ═══

  THESE REQUIRE S3 VERSIONING:
    S3 Object Lock (Compliance/Governance/Legal Hold) → versioning mandatory
    S3 CRR (Cross-Region Replication)                 → versioning on BOTH buckets
    S3 SRR (Same-Region Replication)                  → versioning on BOTH buckets
    API Gateway mTLS truststore                       → versioning + explicit object version
    MFA Delete                                        → versioning must be enabled first

  THESE DO NOT REQUIRE VERSIONING:
    S3 server access logging target bucket            → no versioning needed
    S3 default encryption                             → no versioning needed
    S3 lifecycle policies                             → works with or without

  API GW mTLS VERSIONING TRAP:
    mTLS = custom domain + S3 truststore (PEM file)
    S3 bucket MUST have versioning enabled
    You MUST specify the exact object version (truststoreVersion)
    No versioning = domain creation FAILS at setup
    Update truststore = upload new PEM → reference new version

═══ Kinesis + KMS VPC endpoints (timeout = network) ═══

  Lambda private subnet + encrypted Kinesis stream:
    NEEDS TWO Interface endpoints: Kinesis + KMS
    NEEDS TWO SGs to cooperate per endpoint:
      Lambda SG → outbound 443
      Endpoint SG → inbound 443 from Lambda SG

  Timeout = NETWORK (not permissions)
    "GetRecords times out" = missing endpoint OR SG misconfigured
    "Access Denied" = IAM/key policy (different error!)

  S3 SSE-KMS = server-side (NO KMS endpoint needed)
  Direct kms:Decrypt from YOUR code = NEEDS KMS endpoint
  Kinesis GetRecords = YOUR code calling Kinesis = NEEDS Kinesis endpoint
  Kinesis decrypts internally = NEEDS KMS endpoint too

  RULE: count endpoints by counting DIRECT calls your code makes
        + any service that calls KMS on the data path

═══ EMR in-transit = security config + PEM certs ═══

  EMR inter-node encryption:
    ❌ NOT Nitro (Nitro = EC2-to-EC2 only, automatic, no config)
    ✅ EMR security configuration → enable in-transit → PEM certificates

  PEM certificates from:
    → Private CA (ACM Private CA) — recommended
    → Self-signed (custom, more operational burden)
    → Uploaded to S3 as zip file

  "EMR TLS handshake fails between nodes" = 
    → Missing PEM certs in S3 path
    → OR wrong security configuration reference

  WHY NOT NITRO?
    Nitro = implicit hardware encryption (no compliance proof)
    EMR security config = explicit, auditable, configurable
    Compliance/auditors need PROOF = must use security config

═══ CRR encryption context ═══

  HOW CRR ACTUALLY WORKS (S3 assumes your replication role):

  Source bucket (us-east-1)              Dest bucket (eu-west-1)
  ┌─────────────────────┐               ┌─────────────────────┐
  │ object.txt          │               │ object.txt          │
  │ encrypted with      │               │ encrypted with      │
  │ SOURCE CMK DEK      │               │ DEST CMK DEK (NEW!) │
  └──────────┬──────────┘               └──────────▲──────────┘
             │                                      │
             │  Replication Role does:              │
             │                                      │
             ├── 1. kms:Decrypt (source CMK)        │
             │      → gets plaintext                │
             │                                      │
             └── 2. kms:GenerateDataKey (dest CMK) ─┘
                    → new DEK → re-encrypts → writes

  = Decrypt + Re-encrypt (NOT key copy, NOT key share)
  = Source and dest can use COMPLETELY DIFFERENT CMKs
  = MRK NOT required (only DynamoDB Global Tables needs MRK)

  ENCRYPTION CONTEXT at destination:
    S3 REWRITES aws:s3:arn → DEST bucket ARN (not source)
    Custom context from source → PRESERVED as-is
    Dest key policy condition must reference DEST bucket ARN

  WHERE TO PUT CONDITION:
    Source CMK key policy → kms:Decrypt → NO condition needed
    Dest CMK key policy   → kms:GenerateDataKey → ✅ HERE
      Condition: "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::DEST-BUCKET/*"

═══ S3 server access logging ═══

  Bucket policy method → works with BucketOwnerEnforced ✅
  ACL method → BREAKS with BucketOwnerEnforced ❌
  Target bucket: NO SSE-KMS, NO Object Lock, NO Requester Pays

═══ Secrets Manager rotation fails ═══

  "Unable to log into database" = Lambda SG can't reach DB SG
  "Auth failed for new app" = rotation Lambda didn't ALTER USER

═══ Object Lock vs Vault Lock ═══

  "Fixed retention, auto-expires" → Object Lock Compliance
  "24hr confirm, permanent forever" → Glacier Vault Lock
  "Indefinite, for litigation" → Legal Hold

═══ S3 Access Grants ═══

  Broadest prefix wins.
  Root prefix grant (s3://bucket/) = access to everything.
  Overlap = #1 operational misconfiguration.

═══ Imported key ═══

  Immediate delete (DeleteImportedKeyMaterial) — no 7-day wait
  ScheduleKeyDeletion min = 7 days (different mechanism)

═══ EC2 + encrypted EBS ═══

  Start existing = CreateGrant + Decrypt
  Create new     = CreateGrant + GenerateDataKeyWithoutPlaintext
  BOTH always need CreateGrant (delegates to EBS backend)

═══ EBS cross-account snapshot sharing ═══

  Default key (aws/ebs) can't share → copy with CMK first
  copy-snapshot = decrypt + re-encrypt in ONE API call (no volume needed)
  Target account needs on source CMK:
    Decrypt, ReEncrypt*, GenerateDataKey*, DescribeKey, CreateGrant
  Flow: copy-snapshot with CMK → share snapshot → grant key to target
  ❌ "Create volume" = unnecessary trap (copy-snapshot handles it directly)

═══ EBS vs RDS vs Aurora — encrypt unencrypted snapshot ═══

  EBS:    copy-snapshot + encrypt = ✅ direct (one step)
  RDS:    copy-db-snapshot + encrypt = ✅ direct (one step)
  Aurora: copy CANNOT encrypt ❌ → must restore → enable encryption → new snapshot

═══ CRR replication role (D-G-F mnemonic) ═══

  Decrypt on source key
  GenerateDataKey on dest key (NOT Encrypt)
  GetObjectVersionForReplication on source bucket
  (NO DescribeKey in replication role itself)

═══ Cron vs Rate vs PITR ═══

  Specific calendar dates (10th, 20th) = cron
  Fixed interval (every 6hr)           = rate
  Continuous recovery window           = PITR (not scheduled backups)

═══ Services writing to YOUR S3 — two patterns ═══

  Pattern 1: Service uses ITS OWN principal (you grant in bucket/key policy)
    CloudTrail    → cloudtrail.amazonaws.com
    Config        → config.amazonaws.com
    S3 logging    → logging.s3.amazonaws.com
    Inspector     → inspector2.amazonaws.com
    ELB           → (ELB account ID)
    → Bucket policy: Allow s3:PutObject for service
    → Key policy: Allow GenerateDataKey + DescribeKey for service

  Pattern 2: Service assumes A ROLE YOU CREATE (you specify --role-arn)
    VPC Flow Logs → vpc-flow-logs.amazonaws.com assumes YOUR role
    CRR           → s3.amazonaws.com assumes YOUR replication role
    Firehose      → firehose.amazonaws.com assumes YOUR delivery role
    → IAM role: trust + permissions (s3:PutObject, kms:GenerateDataKey)
    → No service principal in bucket/key policy needed

  RULE: "Just enable it" = Pattern 1 (service principal)
        "Specify a role ARN" = Pattern 2 (your role)
```

---

## PAGE 6: Governance Verbs + RAM/FM (D6 — 14%)

```
═══ VERB → SERVICE (instant decision) ═══

  Share / visible / accessible     → RAM
  Enforce / associate / re-apply   → Firewall Manager
  Deploy resources / push infra    → StackSets
  Self-service / pull / no IAM     → Service Catalog
  Prevent API call / block         → SCP
  Detect + fix / remediate         → Config + SSM
  Validate template before deploy  → cfn-guard / Config proactive

═══ RAM + FM (failed 4x: Q313, Q441, Q562, Q1329) ═══

  RAM + FM together:
    DNS FW + Network FW = RAM shares first, FM enforces
    WAF + Shield + SG   = FM creates directly (no RAM)

  RULE: "Does resource exist in ANOTHER account?" 
    YES = RAM shares first, then FM enforces
    NO (FM creates fresh) = no RAM needed

  Mnemonic: "WSS = no RAM" (WAF, Shield, SG — FM creates these)
            "DNS + NF = RAM" (authored centrally, shared cross-account)

  FM auto-remediates:
    Developer disassociates WAF → FM re-attaches ✅
    Developer deletes NF endpoint → FM re-creates ✅
    StackSets NEVER auto-remediates ❌

═══ cfn-guard vs Config proactive vs SCP (failed 4x: Q1387, Q1588, Q1220, Q1271) ═══

  WHAT EACH LAYER SEES:

  | Layer          | Sees API? | Sees template? | Sees properties? | Bypassable? |
  |----------------|-----------|----------------|------------------|-------------|
  | SCP            | ✅         | ❌              | ❌                | ❌ Never     |
  | cfn-guard      | ❌         | ✅              | ✅ (raw text)     | ✅ Console   |
  | Config proact  | ❌         | ❌              | ✅ (resolved)     | ❌ Never(CF) |
  | CF Hook        | ❌         | ❌              | ✅ (resolved)     | ❌ Never(CF) |

  WHICH FIRES FOR EACH DEPLOY PATH:
    Console direct (no CF):  only SCP + Config detective
    Console CF deploy:       proactive + Hook + SCP (NOT cfn-guard)
    Pipeline CF deploy:      cfn-guard + proactive + Hook + SCP (ALL)
    Terraform (direct API):  only SCP + Config detective

  cfn-guard LIMITATIONS:
    Can't resolve: !Ref, !If, !Sub, !Select, !GetAtt
    Sees JSON objects, not resolved values → comparison FAILS
    "true" (string) ≠ true (boolean) → type-strict FAIL
    Parameter overrides at deploy time bypass validation

  FIRING ORDER (CF deploys):
    Config proactive → BEFORE resource creation → SCP never fires if rejected
    SCP → at API call time (if proactive passes)

  KEY TRAP: "SCP can't inspect CF template CONTENT"
    → SCP sees API params (ec2:MetadataHttpTokens, ec2:Encrypted)
    → SCP CANNOT see RDS DeletionProtection inside template
    → For template content = Config proactive or cfn-guard

═══ State Manager (failed 4x: Q1403, Q1579, Q1048, Q1071) ═══

  ONE association supports BOTH:
    OnBoot trigger + rate(Xhr) schedule = SAME association
    ❌ DON'T create two associations

  REGIONAL:
    500 instances, 3 regions = 3 associations (one per region)
    No org-wide associations exist

  OnBoot + rate = INDEPENDENT triggers:
    Reboot at 14:30, next rate at 17:00 → BOTH fire independently
    OnBoot doesn't reset the rate timer

  New target detected = immediate first run (within minutes)
    rate(1hr) = re-run frequency, NOT "wait 1hr before first"

  Blind between runs:
    Admin stops CW agent manually → stays broken until next scheduled run
    State Manager = scheduler, not real-time monitor

  Tag removed = target leaves:
    Instance loses matching tag → skipped on next run (dynamic targeting)

═══ StackSets vs FM vs Native ═══

  StackSets:
    Auto-deploy to new accounts ✅ (service-managed + auto-deploy)
    Auto-remediate drift ❌ NEVER
    "Deploy resources" = StackSets. "Enforce rules" = FM.

  Native org-wide (DON'T use StackSets for these):
    GD, Inspector, SH, Macie, Detective, Config, AA, FM
    → All have delegated admin + auto-enable
    → StackSets only for CUSTOM resources (IAM roles, Lambda, etc.)

═══ Conformance Pack ═══

  Deploys rules + remediation CONFIG
  Does NOT deploy execution ROLE
  New account joins → rules deploy ✅ → role missing → remediation silently fails
  Fix: StackSets deploys the execution role separately

═══ Security Hub setup: E-D-M-A (failed 2x: Q1244, Q1273) ═══

  Enable SH in admin → Designate admin → Enable Members → Access (cross-account)
  
  "Some accounts zero, others working" = membership issue (not enrolled)
  "ALL accounts delayed 0 findings" = latency 2-24hr (Config at scale)
  "Standards enabled but 0%" = standards must be EXPLICITLY enabled after SH

  SH = REGIONAL (not global!)
  Cross-region = designate aggregation region
  SH = dashboard ONLY. Config = remediation engine.

═══ WAT vs Audit Manager vs Artifact ═══

  WAT = self-reported architecture review + improvement plan + milestones
    → NO automation, NO Config/CloudTrail evidence, NO compliance scores
    → Milestones = immutable snapshots (compare risk over time)

  Audit Manager = YOUR evidence (auto-collected from Config + CT + SH + manual)
    → Maps to frameworks (SOC 2, PCI, HIPAA)
    → Generates audit-ready reports

  Artifact = AWS's compliance reports (SOC, PCI, ISO, BAA)
    → Not YOUR evidence — AWS's proof THEY are compliant

═══ Service Catalog (failed 2x: Q274, Q277) ═══

  Self-service + no broad IAM = Service Catalog + launch constraint
  Launch role = SC assumes role with permissions (dev only needs ProvisionProduct)
  SC = deploy only, NO post-provisioning monitoring
  "Post-deploy compliance" = Config + SSM (not SC)

═══ RCP exemptions ═══

  Management account resources = exempt
  Service-linked roles = exempt (structural)
  AWS managed KMS keys = exempt
  kms:RetireGrant = exempt
  AWS service principals = exempt via PrincipalIsAWSService condition

═══ YOUR ERROR PATTERNS ═══

  ❌ RAM vs FM: picked FM alone for DNS FW sharing (Q313, Q441)
     → RULE: DNS FW rule group lives in another account. RAM shares. FM enforces.

  ❌ cfn-guard catches Console CF deploy (Q1220, Q1271, Q1588)
     → RULE: cfn-guard = pipeline ONLY. Console CF = Config proactive catches.

  ❌ State Manager: picked two associations for OnBoot+rate (Q1403, Q1071)
     → RULE: ONE association supports BOTH triggers.

  ❌ State Manager: picked one association for 3 regions (Q1579)
     → RULE: State Manager = REGIONAL. One per region.

  ❌ SCP inspects CF template properties (Q1651)
     → RULE: SCP sees API params. Can't see inside template.
       Template content = Config proactive or cfn-guard.

  ❌ Security Hub: wrong setup order (Q1244, Q1273)
     → RULE: E-D-M-A. Must enable FIRST, then designate.

  ❌ Conformance pack deploys execution role (Q1639)
     → RULE: Pack deploys rules. NOT the role. StackSets deploys role.
```

---

## PAGE 7: Connectivity + D3 Remaining Gaps

```
═══ CONNECTIVITY DECISION (5 options) ═══

  ON-PREM → AWS (fixed networks):
    Site-to-Site VPN   = IPsec over internet (quick, cheap, minutes)
    Direct Connect     = dedicated fiber (fast, private, NOT encrypted!)
    Transit Gateway    = hub connecting VPCs + VPN + DX (share via RAM)

  REMOTE USERS → AWS:
    Client VPN         = full network tunnel (all ports, VPN client needed)
    Verified Access    = per-app, zero-trust, NO client, browser only

  ENCRYPT DX:
    Dedicated DX → MACsec (Layer 2, zero overhead, line-rate)
    Hosted DX    → Site-to-Site VPN over DX (IPsec, Layer 3)
    ❌ MACsec on hosted = IMPOSSIBLE

  KEY TRAPS:
    "DX alone" ≠ encrypted (private ≠ encrypted!)
    "Layer 2 encryption" = MACsec = dedicated ONLY
    "Full network access from laptop" = Client VPN
    "Per-app, no client, identity+device" = Verified Access
    "3 offices with routers" = Site-to-Site VPN (not Client VPN)
    "Individual home workers" = Client VPN (not Site-to-Site)

  DECISION TABLE:
    | Signal                              | Answer            |
    |-------------------------------------|-------------------|
    | "Quick, over internet, on-prem"     | Site-to-Site VPN  |
    | "Dedicated, high-throughput"         | Direct Connect    |
    | "Layer 2 encrypt dedicated DX"      | MACsec            |
    | "Encrypt hosted DX"                 | VPN over DX       |
    | "Many VPCs + on-prem connected"     | Transit Gateway   |
    | "Employees full VPC access"         | Client VPN        |
    | "Specific apps, zero-trust, no VPN" | Verified Access   |

═══ CLIENT VPN AUTHENTICATION (3 options) ═══

  1. Mutual TLS (certificate-based):
     → ACM Private CA issues client certs
     → No user/password — cert = identity
     → "Strongest, no credentials to steal"

  2. Active Directory (user/password):
     → AWS Managed AD or AD Connector
     → Users authenticate with AD credentials
     → "Existing corporate directory"

  3. SAML-based SSO (federated):
     → Okta, Entra ID, any SAML 2.0 IdP
     → Users authenticate via IdP portal
     → "SSO experience for VPN"

  CAN COMBINE: mTLS + AD = cert + password (strongest)
  
  EXAM SIGNALS:
    "Certificate-based VPN auth" = mutual TLS (ACM Private CA)
    "Corporate AD credentials for VPN" = AD auth (Managed AD or Connector)
    "SSO for VPN access" = SAML federation
    "Strongest authentication" = mTLS + AD combined

═══ SITE-TO-SITE VPN vs CLIENT VPN ═══

  Site-to-Site VPN:
    → TWO fixed endpoints (your router ↔ AWS VGW/TGW)
    → IPsec tunnels (2 per connection for HA)
    → Auth: pre-shared key OR certificate
    → "Office to AWS" / "branch to AWS"

  Client VPN:
    → Individual users (laptop/phone → AWS)
    → OpenVPN-based (needs client software)
    → Auth: mTLS / AD / SAML (see above)
    → "Remote workers to AWS"

  TRAP: "3 offices with routers" = Site-to-Site (NOT Client VPN)
        "500 employees from home" = Client VPN (NOT Site-to-Site)

═══ RAM FULL LIST (shares cross-account) ═══

  RAM = "make resource VISIBLE to other accounts" (optional use)

  NETWORKING:
    Transit Gateways, Subnets, Prefix lists

  SECURITY RULES:
    DNS Firewall rule groups, Network Firewall policies
    WAF Web ACLs, Route 53 Resolver rules

  COMPUTE / DATA:
    Aurora DB clusters, EC2 Image Builder, License Manager
    CodeBuild projects, Outposts

  NOT supported (use other mechanisms):
    KMS keys → Grants or key policy
    S3 buckets → bucket policy
    Secrets Manager → resource policy
    IAM roles → trust policy

═══ FM CREATES DIRECTLY (no RAM needed for enforcement) ═══

  FM creates these FRESH in member accounts:
    ✅ WAF Web ACLs (creates new, attaches to ALBs/CF)
    ✅ Shield Advanced protections (creates directly)
    ✅ Security Groups (common policy = creates SG in each account)
    ✅ Security Groups (audit policy = finds + removes bad rules)

  FM CANNOT create these (needs RAM to share first):
    ❌ DNS Firewall rule groups (authored centrally → RAM shares → FM associates)
    ❌ Network Firewall policies (authored centrally → RAM shares → FM deploys)

  RULE:
    "FM enforces WAF/Shield/SG" = FM creates directly (no RAM step)
    "FM enforces DNS FW/NF" = RAM shares first, THEN FM enforces association

  SEPARATELY:
    RAM CAN share WAF Web ACLs too (optional sharing pattern)
    But when FM enforces WAF → FM creates its own, doesn't use RAM

═══ Inspector SBOM (failed 2x: Q1059, Q1119) ═══

  Inspector SBOM export:
    ❌ NO built-in scheduler (no Console option)
    ✅ On-demand API only: CreateSbomExport

  Schedule with: EventBridge rule → Lambda → CreateSbomExport API
  Export format: CycloneDX or SPDX
  Export dest: S3 bucket

  Bucket policy needed:
    Allow s3:PutObject for inspector2.amazonaws.com
    (same Pattern 1 from Page 5 — service principal in bucket policy)

  ❌ NOT SSM + custom scripts
  ❌ NOT "enable scanning" (that's vulnerability scanning, different)

═══ Verified Access (zero-trust per-app) ═══

  WHAT: Access internal apps WITHOUT VPN. Browser-based.
  HOW:  Evaluates identity (IdP) + device posture (MDM) PER REQUEST
  
  Components:
    Trust providers = who checks identity + device
      → Identity: Okta, Entra ID, Identity Center
      → Device: CrowdStrike, Jamf, Intune
    
    Access groups = policies (which users/devices get in)
    Endpoints = the apps being protected

  vs Client VPN:
    Client VPN = full tunnel, all ports, VPN client on device
    Verified Access = per-app HTTPS, no client, zero-trust

  EXAM SIGNALS:
    "Stolen laptop, block ONE device" = mark non-compliant in device trust provider
    "No VPN client" = Verified Access
    "Zero-trust + device posture" = Verified Access
    "Full network access needed" = Client VPN (not VA)

═══ Network Firewall TLS inspection (failed 3x: Q35, Q87, Q152) ═══

  HOW: Network Firewall decrypts → inspects → re-encrypts (MITM pattern)
  NEEDS: Private CA certificate in ACM
  
  Users get cert warnings = Private CA NOT in client trust stores
  Fix: distribute Private CA cert to ALL clients (GPO, MDM, manual)

  This is NOT:
    ❌ Public ACM cert (public CAs don't do MITM)
    ❌ Self-signed on the firewall (clients won't trust it)
    ✅ Private CA → distribute to clients → trusted MITM

═══ Traffic Inspection — 3 patterns (failed 3x) ═══

  PASSIVE (copy, no block):     Traffic Mirroring → NLB → IDS
    Encapsulation: VXLAN
    If it fails: production unaffected (copy stops, traffic fine)
    "IDS" / "observe" / "full packet" / "without blocking"

  INLINE third-party:           GWLB → Palo Alto / Fortinet
    Encapsulation: GENEVE
    If it fails: traffic STOPS
    "Third-party appliance" / "Palo Alto" / "scale + health check"
    TRAP: logs show GWLB IP → decapsulate GENEVE outer header

  INLINE AWS-native:            Network Firewall (Suricata)
    If it fails: traffic STOPS
    "Suricata rules" / "IPS" / "TLS inspection"

  NEVER CONFUSE:
    "Full packet + passive" = Traffic Mirroring (NEVER Flow Logs)
    "IDS/IPS + block" = Network Firewall or GWLB
    VPC Flow Logs = METADATA ONLY (IP/port, no payload)

═══ S3 Batch Operations (encrypt existing objects) ═══

  "20TB unencrypted, encrypt with SSE-S3" = S3 Batch Operations COPY
    → Copy object to itself with encryption specified
    → Parallel processing, millions of objects
    → No code, no Lambda

  Default encryption only covers FUTURE objects
  EXISTING unencrypted = Batch Operations COPY (to self + encrypt)

  S3 Batch = REGIONAL (job + manifest + target = same region)

═══ YOUR ERROR PATTERNS ═══

  ❌ Picked GWLB for passive IDS (Q1126, 3x)
     → RULE: passive = Traffic Mirroring. GWLB = inline (blocks).

  ❌ Picked NF for "full packet + observe only" 
     → RULE: NF = inline IPS. Mirroring = passive copy.

  ❌ Inspector SBOM has built-in scheduler (Q1059, Q1119)
     → RULE: On-demand API only. Schedule = EventBridge + Lambda.

  ❌ MACsec on hosted DX (impossible)
     → RULE: MACsec = dedicated ONLY. Hosted = VPN over DX.
```

---

## PAGE 8: IAM Fundamentals — D4 Gaps (D4 — 20%)

```
═══ PERMISSION BOUNDARIES (delegation pattern) ═══

  Boundary = ceiling on ONE role. NEVER grants, only restricts.
  Effective = Identity policy ∩ Boundary ∩ SCP

  THE PROBLEM:
    Dev has iam:CreateRole → creates role with AdministratorAccess
    → Assumes it → full admin = ESCALATION

  THE FIX (3 Deny statements):
    1. Deny CreateRole WITHOUT boundary attached
    2. Deny DeleteRolePermissionsBoundary (can't remove)
    3. Deny PutRolePermissionsBoundary to different boundary (can't swap)

  RESULT: Dev creates roles, but ALL capped by the boundary.
    Even AdministratorAccess attached → effective = boundary ceiling only.

  EXAM SIGNALS:
    "Devs create own roles, prevent escalation" = boundary delegation
    "Limit what created roles can do" = boundary
    "Self-service IAM without risk" = SCP forces boundary on CreateRole

═══ ABAC — 3 TAG CONDITION KEYS ═══

  aws:PrincipalTag/Key  = WHO is calling (tag on the role/user)
  aws:ResourceTag/Key   = WHAT are they touching (tag on the resource)
  aws:RequestTag/Key    = WHAT are they sending (tag in the API call)

  THREE DIFFERENT MOMENTS:
    RequestTag  = CREATION time ("must tag when creating")
    ResourceTag = ACCESS time ("can only touch matching resources")
    PrincipalTag = ALWAYS (who the caller is)

  THE MAGIC PATTERN (ABAC matching):
    "aws:ResourceTag/Project": "${aws:PrincipalTag/Project}"
    = "You can only access resources tagged with YOUR project"
    = No ARNs. New resource with tag = auto-access.

  ENFORCE TAGGING (Null condition):
    "Null": {"aws:RequestTag/CostCenter": "true"} → Deny
    = "Deny if CostCenter tag is MISSING" = must tag or denied

  EXAM SIGNALS:
    "Scales without policy changes" = ABAC
    "Dynamic access based on tags" = ABAC
    "Per-team access without per-team policies" = ABAC + session tags

═══ COGNITO (User Pool vs Identity Pool) ═══

  User Pool = WHO ARE YOU? (authentication)
    → Sign-up, sign-in, MFA, tokens (JWT)
    → Output: ID token + Access token + Refresh token
    → Use: authenticate your app users

  Identity Pool = WHAT CAN YOU DO IN AWS? (authorization)
    → Exchanges token for temporary AWS credentials
    → Output: AccessKey + SecretKey + SessionToken
    → Use: app accesses S3, DynamoDB directly

  TOGETHER:
    App → User Pool (sign in) → JWT token
    App → Identity Pool (exchange JWT) → temp AWS creds
    App → S3/DynamoDB (with creds)

  PER-USER S3 ACCESS:
    Resource: "arn:aws:s3:::bucket/${cognito-identity.amazonaws.com:sub}/*"
    = Each user only accesses their own folder

  EXAM SIGNALS:
    "Mobile app needs temp AWS creds" = Identity Pool
    "Customer sign-up/sign-in" = User Pool
    "Per-user S3 folders" = Identity Pool + sub in Resource ARN
    "Employee SSO to Console" = Identity Center (NOT Cognito)

  TRAPS:
    ❌ Don't call AssumeRoleWithWebIdentity directly — use Identity Pool
    ❌ Cognito ≠ Identity Center (customers vs employees)
    ❌ User Pool tokens can't go directly to STS — use Identity Pool

═══ IDENTITY CENTER (workforce SSO) ═══

  WHAT: Centralized SSO for employees across multiple AWS accounts
  WHERE: AWS Organizations (required)

  Identity sources (ONLY ONE at a time):
    Built-in directory OR Active Directory OR External IdP (SAML 2.0)

  Permission set = IAM role auto-created in target accounts
    → User picks account + permission set → assumes the role
    → Temporary credentials (no long-term keys)

  SCIM = auto-sync users + groups from IdP (Okta, Entra ID)
    → New user joins group in Okta → auto-inherits permission set
    → No manual action in Identity Center

  EXAM SIGNALS:
    "Workforce SSO" = Identity Center
    "Employees access multiple accounts" = Identity Center
    "Auto-sync from Okta/Entra" = SCIM
    "Permission sets" = Identity Center (auto-creates IAM roles)

  TRAPS:
    ❌ Cognito NOT a source for Identity Center
    ❌ Only ONE identity source at a time
    ❌ Identity Center = employees. Cognito = customers. Never mix.

═══ DIRECTORY SERVICE (AD decision tree) ═══

  Simple AD     = Samba (no trusts, no RDS SQL, standalone)
  AD Connector  = proxy to on-prem AD (no data in AWS, no trusts)
  Managed AD    = full MS AD (trusts, RDS SQL, Identity Center)

  DECISION:
    "Need trusts" OR "RDS SQL Server" OR "Identity Center" = Managed AD
    "Proxy to on-prem, no AWS infra needed" = AD Connector
    "Small standalone directory" = Simple AD

  TRUST DIRECTION:
    "AWS trusts on-prem" = one-way (on-prem users → AWS resources)
    "Both directions" = two-way trust

  FEDERATION WITHOUT DIRECTORY SERVICE:
    ADFS on-prem + Identity Center = NO AWS Directory Service infra needed
    "No AWS Directory Service infrastructure" = ADFS + Identity Center

═══ CONDITION KEYS QUICK REFERENCE ═══

  aws:TokenIssueTime      = revoke sessions (DateLessThan = deny old)
  aws:PrincipalOrgID      = restrict to my org
  aws:PrincipalIsAWSService = exempt AWS services from deny rules
  sts:ExternalId          = confused deputy (third-party roles)
  aws:MultiFactorAuthPresent = require MFA (BoolIfExists!)
  aws:MultiFactorAuthAge  = MFA max session (NumericLessThan, seconds)
  aws:SecureTransport     = require HTTPS (Bool: false → Deny)
  ec2:MetadataHttpTokens  = enforce IMDSv2 (SCP)
  kms:ViaService          = only allow KMS through specific service

  BoolIfExists vs Bool (MFA TRAP):
    Bool alone: CLI/SDK calls (no MFA key) = condition SKIPPED = ALLOWED ❌
    BoolIfExists: key absent = treated as match = Deny fires ✅
    RULE: MFA in Deny statements = ALWAYS BoolIfExists
```

---

## PAGE 9: New C03 Features + Remaining Gaps

```
═══ SECURITY LAKE / OCSF ═══

  Security Lake = YOUR S3 bucket + OCSF format + ALL log sources normalized
  OCSF = Open Cybersecurity Schema Framework (vendor-neutral)

  Sources: CloudTrail + VPC Flow + DNS + WAF + GuardDuty + third-party
  Storage: Apache Parquet on Iceberg tables (your S3)
  Query: Athena (no built-in engine)
  Consumers: subscriber model (Splunk, Datadog, OpenSearch)

  NOT real-time (batch, minutes). For real-time → CloudTrail Lake or CW Logs.
  NOT a replacement for Security Hub (SH = dashboard, SL = data lake).

  "Normalize all logs + common schema + your S3" = Security Lake / OCSF

═══ CW LOGS DATA PROTECTION (masking) ═══

  WHAT: Detect + mask PII in logs automatically. No code changes.
  HOW: Data protection policy on log group

  Two actions:
    Audit = send finding to separate destination (what was detected)
    Deidentify = mask with **** (what users see)

  UNMASKING:
    Default: everyone sees ****
    To see raw: needs logs:Unmask permission (grant sparingly)
    "Who can see raw PII?" = who has logs:Unmask

  NOT Macie (Macie = S3 only). NOT GuardDuty (threats, not PII).
  "Mask PII in logs" = CW Logs data protection. Always.

═══ DNS FIREWALL (DGA + allow-list) ═══

  Rule actions: ALLOW, BLOCK, ALERT
  Priority: lowest number = first evaluated (first match wins)
  Scope: VPC-level (all resources in VPC)

  NORMAL pattern: ALLOW specific → BLOCK *
  DGA pattern: ALLOW known-good → BLOCK * (can't enumerate DGA domains)

  "DGA (Domain Generation Algorithm)" = unpredictable domains
    → Can't block-list (infinite domains)
    → FLIP to allow-list (block all except known-good)

  DNS Firewall ALERT ≠ finding (just logs, no security finding)
  "Detect C2 via DNS" = GuardDuty (reads DNS natively)
  "Block C2 domains" = DNS Firewall

═══ WAF BOT CONTROL ═══

  Common level = signatures (User-Agent strings, known bot IPs)
    → Catches: obvious crawlers, curl, scrapy
    → Misses: rotating User-Agent, distributed attacks

  Targeted level = behavioral (JS tokens, fingerprinting, sessions)
    → Catches: sophisticated bots rotating IPs + headers
    → "Distributed + rotating" = always Targeted

  Challenge = silent JS check (needs browser)
  CAPTCHA = visible puzzle (needs browser + human)
  Scope-down = exempt known-good traffic from rule group

  TRAP: mobile apps + server-to-server can't do Challenge/CAPTCHA
    → Fix: scope-down statement excluding by header/IP

  "Legitimate traffic blocked by Bot Control" = scope-down
  "Sophisticated distributed attack" = Targeted level

═══ CLOUDFRONT OAC + SSE-KMS ═══

  TWO policies needed (miss either = 403):
    1. S3 bucket policy: Allow s3:GetObject for cloudfront.amazonaws.com
       + Condition: aws:SourceArn = distribution ARN
    2. KMS key policy: Allow kms:Decrypt for cloudfront.amazonaws.com
       + Condition: aws:SourceArn = distribution ARN

  OAC vs OAI:
    OAI = legacy (can't do SSE-KMS, GET only)
    OAC = current (SSE-KMS ✅, PUT/DELETE ✅, SigV4)
    "S3 + SSE-KMS + only via CloudFront" = OAC + KMS key policy

═══ VPC LATTICE (service-to-service) ═══

  WHAT: East/west connectivity across accounts without peering/TGW
  HOW: Service network + services + auth policies

  Auth: IAM (SigV4) — no certs, no mesh
  Share: RAM (share service network cross-account)
  Enforce: Auth policy per service (resource-based, like bucket policy)

  "Service A can call B, deny C" = auth policy on B allows A's role
  Network membership = reachability. Auth policy = authorization. SEPARATE.

  "Cross-account service-to-service + no VPN/peering + IAM" = Lattice

═══ NITRO INTER-INSTANCE ENCRYPTION ═══

  Automatic hardware-level encryption between EC2 instances
  Zero config, zero app changes, zero performance impact
  Both sides MUST be Nitro-based (5th gen+: C5, M5, T3, etc.)

  Covers: EC2↔EC2, EKS inter-node, EMR, SageMaker
  Does NOT cover: EC2→RDS, EC2→S3 (use TLS for managed services)
  Non-Nitro on either side = NOT encrypted

  "Encrypt between instances, no app changes" = Nitro
  EMR inter-node = NOT Nitro (needs explicit security config + PEM)

═══ CLOUDSHM vs CUSTOM KEY STORE vs XKS ═══

  | | CloudHSM Direct | Custom Key Store | XKS |
  |---|---|---|---|
  | Symmetric | ✅ | ✅ | ✅ |
  | Asymmetric | ✅ | ❌ | ❌ |
  | Signing | ✅ | ❌ | ❌ |
  | Interface | PKCS#11/JCE | KMS API | KMS API |
  | S3/EBS/RDS integration | ❌ | ✅ | ✅ |
  | Key lives | Your HSM (in AWS) | Your HSM (in AWS) | Your HSM (OUTSIDE AWS) |

  "Single-tenant + S3/EBS integration" = Custom Key Store
  "Asymmetric on dedicated HSM" = CloudHSM direct
  "Keys NEVER in AWS" = XKS
  Custom Key Store + XKS = SYMMETRIC ONLY through KMS

═══ CONTROL TOWER ═══

  Guardrail types:
    Preventive = SCP (blocks API)
    Detective = Config rule (detects after)
    Proactive = CF Hook (validates template before deploy)

  Drift: DETECTS but does NOT auto-fix (manual resolution)
  Custom controls: ✅ supports custom SCPs, Config rules, CF Hooks

  Prerequisites:
    ✅ STS enabled in all regions
    ✅ Identity Center enabled
    ❌ DISABLE existing trusted access for Config/CloudTrail (CT manages these)

═══ DECLARATIVE POLICIES ═══

  "This STATE is impossible to violate, regardless of which API"
  Scope: EC2, VPC, EBS ONLY (very narrow)

  vs SCP:
    SCP = "this API call is blocked" (must enumerate each API)
    Declarative = "this state is enforced" (future APIs auto-covered)

  "No public IPs regardless of any current or future API" = declarative
  "Block RunInstances without IMDSv2" = SCP (specific API)

═══ MACIE CUSTOM DATA IDENTIFIERS ═══

  regex + keywords + max proximity distance
  "Detect PROJ-[A-Z]{4}-\d{4} only when 'Classified' within 50 chars"
    = Custom data identifier with regex + keyword + proximity

  Macie enabled ≠ scanning (automated discovery = sampling only)
  Full coverage = create discovery JOB
  SSE-KMS bucket "Unable to analyze" = key policy missing Macie SLR kms:Decrypt
```

---

> Total: 9 pages covering 95%+ of SCS-C03 exam content intersected with your error patterns.
> Write by hand. Read before every drill. Cycle through daily (3 pages/day).
> Exam day: skim all 9 pages in the 30 min before your appointment.
