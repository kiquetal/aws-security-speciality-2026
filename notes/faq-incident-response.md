# FAQ: Incident Response (Domain 2 — 14%)

> **Blueprint refs:** Task 2.1 (design/test IR plans), Task 2.2 (respond to security events)
> **Weight:** 14% = ~9 questions on a 65-question exam
> **Your stats:** 21/30 = 70% — weakest domain by accuracy AND lowest volume (3% of practice)

---

## IR Decision Framework — The 4 Phases

```
┌──────────────────────────────────────────────────────────────────────┐
│                    AWS IR LIFECYCLE (4 PHASES)                         │
├──────────────┬──────────────┬───────────────────┬────────────────────┤
│ 1. PREPARE   │ 2. DETECT    │ 3. CONTAIN +      │ 4. POST-INCIDENT   │
│              │   & TRIAGE   │    INVESTIGATE     │                    │
├──────────────┼──────────────┼───────────────────┼────────────────────┤
│ Runbooks     │ Validate     │ Isolate (SG)      │ Root cause         │
│ Roles ready  │ findings     │ Preserve (AMI/EBS)│ Lessons learned    │
│ Tools staged │ Scope/impact │ Investigate       │ Update runbooks    │
│ Test plans   │ False pos?   │ (Detective)       │ Resilience assess  │
├──────────────┼──────────────┼───────────────────┼────────────────────┤
│ FIS          │ GuardDuty    │ Deny-all SG       │ Resilience Hub     │
│ Resilience   │ Security Hub │ No-reboot AMI     │ Audit Manager      │
│ Hub          │ EventBridge  │ EBS snapshot      │ Well-Architected   │
│ ARC          │ Detective    │ TokenIssueTime    │                    │
│ Runbooks/SSM │              │ Step Functions    │                    │
└──────────────┴──────────────┴───────────────────┴────────────────────┘
```

---

## Containment Decision Tree (Exam-Critical)

```
GuardDuty Finding on EC2
        │
        ▼
┌─────────────────────────────────┐
│ What type of credential finding? │
└────────────┬────────────────────┘
             │
    ┌────────┴────────────────────────────────────┐
    │                                              │
    ▼                                              ▼
OutsideAWS                                    InsideAWS
(creds used from external IP)                (creds used from DIFFERENT EC2 in same account)
    │                                              │
    ▼                                              ▼
TokenIssueTime inline Deny                    Deny-all SG on ATTACKER's instance
(old creds = dead, IMDS gives fresh)         (can't use TokenIssueTime — would kill BOTH)
    │                                              │
    ▼                                              ▼
Instance stays up with new creds             Legitimate instance keeps working
```

### OutsideAWS — Full Sequence (if API must stay up)

```
1. Inline Deny: aws:TokenIssueTime < NOW     ← kills stolen creds
2. EBS snapshot                                ← disk forensics
3. IMDSv2 hop limit = 1                        ← prevent future SSRF
   (DON'T deny-all SG — kills legitimate API traffic)
```

### InsideAWS — Full Sequence

```
1. Deny-all SG on attacker's instance         ← network isolation
2. EBS snapshot of attacker's instance         ← disk forensics
3. No-reboot AMI of attacker's instance        ← volatile memory
   (DON'T use TokenIssueTime — both instances share same role)
```

### Credential Leak (Keys on GitHub)

```
1. Deactivate exposed access keys             ← stop immediate bleeding
2. Attach inline Deny * to IAM USER           ← covers 2nd key + console + sessions
   (NOT just deactivate keys — attacker may have created new keys/console)
3. CloudTrail investigation                    ← scope blast radius
4. Detective for timeline                      ← what else was accessed
```

> ⚠️ **Contain ALL paths BEFORE investigating.** Detective/CloudTrail comes AFTER containment.

---

## Forensic Evidence Preservation (Exam-Critical)

| Evidence Type | How to Capture | Notes |
|---|---|---|
| **Disk** | EBS snapshot | Non-destructive, instance stays running |
| **Volatile memory** (processes, network conns, kernel modules) | **No-reboot AMI** | Creates AMI without stopping instance = captures RAM state |
| **Network state** | VPC Flow Logs (already flowing) | Check existing logs, no new capture needed |
| **API activity** | CloudTrail (already logged) | Query via Lake or Athena |
| **Blast radius** | Detective | Timeline, related entities, lateral movement |

### No-Reboot AMI — Why It Matters

```
┌────────────────────────────────────────────────────────┐
│ Regular AMI:  Stop → Snapshot → Start                   │
│               ❌ Memory LOST on stop                    │
│                                                         │
│ No-reboot AMI: Snapshot while RUNNING                   │
│               ✅ Memory state preserved in the image    │
│               ✅ Instance never stops                   │
│               ⚠️ Filesystem consistency not guaranteed  │
└────────────────────────────────────────────────────────┘

Use case: "Capture volatile memory + disk WITHOUT stopping instance"
Answer: No-reboot AMI (memory) + EBS snapshot (disk)

WRONG answers:
- dd /dev/mem → restricted on modern kernels (Amazon Linux 2+)
- Terminate then snapshot → memory gone forever
- Deny-all SG → isolates but doesn't dump memory
```

---

## IR Automation Services (Task 2.1)

### Automated Forensics Orchestrator for EC2

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────────────┐
│ GuardDuty/  │────▶│ EventBridge  │────▶│ Step Functions           │
│ Config/     │     │ (trigger)    │     │ (orchestrator)           │
│ Security Hub│     └──────────────┘     │                         │
└─────────────┘                          │  1. Triage (validate)   │
                                          │  2. Isolate (swap SG)   │
                                          │  3. Acquire (snapshot   │
                                          │     + memory dump via   │
                                          │     SSM RunCommand)     │
                                          │  4. Investigate (launch │
                                          │     forensic EC2 with   │
                                          │     attached evidence)  │
                                          │  5. Report (SNS/S3)    │
                                          └─────────────────────────┘
```

**Exam keywords:** "Automate forensics" / "auto-isolate on finding" / "orchestrate IR steps" → Step Functions + Lambda + SSM

| Component | Role |
|---|---|
| Step Functions | Workflow orchestration (state machine) |
| Lambda | Individual actions (swap SG, create snapshot, notify) |
| SSM RunCommand | Execute commands on instance (memory dump, log collection) |
| SSM Automation | Pre-built runbooks (less code than Lambda) |
| EventBridge | Trigger from GuardDuty/Config/Security Hub |
| SNS | Notifications |
| S3 | Evidence storage (forensic bucket) |

### AWS Fault Injection Service (FIS) — Task 2.1

```
Purpose: CHAOS ENGINEERING to TEST your IR plan

What it does:
- Inject failures into AWS resources (stop EC2, throttle API, AZ impairment)
- Validates your monitoring/alerting fires correctly
- Validates your runbooks actually work

Exam keywords:
- "Test incident response plan effectiveness"
- "Validate monitoring detects failures"
- "Simulate AZ outage"
- "Chaos engineering"

Key facts:
- Experiments define targets + actions + stop conditions
- Safety: stop conditions auto-halt if metrics breach thresholds
- Integrates with CloudWatch alarms as guardrails
- Supports: EC2, ECS, EKS, RDS, network (packet loss, latency)
```

### AWS Resilience Hub — Task 2.1

```
Purpose: ASSESS your application's RESILIENCE POSTURE

What it does:
- Define RTO/RPO targets per application
- Discovers infrastructure (CloudFormation, Terraform, manual)
- Assesses resilience against AZ failure, region failure, app failure
- Generates recommendations to meet targets
- Tracks compliance over time

Exam keywords:
- "Assess RTO/RPO compliance"
- "Resilience posture"
- "Application recovery readiness"
- "Recommendations to improve resilience"

Key facts:
- Input: your apps (CF stacks, resource groups, Terraform state)
- Output: resilience score + gap analysis + recommendations
- NOT a runtime tool — it's an assessment/planning tool
- Integrates with FIS to validate recommendations
```

### Amazon Application Recovery Controller (ARC) — Task 2.1

```
Purpose: RECOVER from failures by shifting traffic away from impaired AZ/region

Two capabilities:
1. ZONAL SHIFT: Move traffic away from one AZ (minutes to recover)
   - Works with: ALB, NLB, ASG, EKS
   - "Start zonal shift" = stop sending traffic to bad AZ
   - Zonal autoshift = AWS automatically shifts for you

2. READINESS CHECKS: Verify DR readiness BEFORE failure (deprecated for new customers Apr 2026)
   - Audits: replicas in sync, DNS configured, capacity provisioned

Exam keywords:
- "Rapidly recover from AZ impairment"
- "Shift traffic away from impaired AZ"
- "Zonal recovery"
- "Minimize blast radius of AZ failure"

Key facts:
- Zonal shift is TEMPORARY (you set expiration)
- ARC ≠ Route 53 failover (that's region-level, DNS-based)
- ARC = AZ-level, load-balancer-based (faster, no DNS TTL)
```

### SageMaker AI Notebooks for IR — Task 2.1

```
Purpose: INTERACTIVE FORENSIC ANALYSIS with code notebooks

What it does:
- Jupyter notebooks for security analysts
- Query CloudTrail Lake, Security Lake, Athena
- Visualize attack patterns, timelines, correlations
- Reusable: same notebook template for same incident type

Exam keywords:
- "Standardize IR analysis processes"
- "Repeatable forensic investigation"
- "Interactive security analysis with code"
- "Query Security Lake data with ML"

Key facts:
- NOT automated (unlike Step Functions) — it's INTERACTIVE
- Used by analysts AFTER containment, during investigation
- Can integrate with Bedrock for AI-powered log analysis
- Think of it as "forensic lab workbench" — analyst tools
```

### Systems Manager OpsCenter — Task 2.1

```
Purpose: CENTRALIZED operational issue tracking

What it does:
- OpsItems = tickets for operational issues
- Auto-created from GuardDuty, Config, Security Hub findings
- Links to runbooks (SSM Automation) for resolution
- Aggregates across accounts (Organizations integration)

Exam keywords:
- "Centralized view of operational issues"
- "Track security findings to resolution"
- "Operational management of incidents"
```

---

## IR Service Selection Matrix

| "I need to..." | Service |
|---|---|
| **Test** my IR plan works | FIS (inject failures) |
| **Assess** if my app meets RTO/RPO | Resilience Hub |
| **Shift** traffic from bad AZ | ARC (zonal shift) |
| **Automate** isolate→snapshot→investigate | Step Functions + Lambda + SSM |
| **Orchestrate** full forensic pipeline | Automated Forensics Orchestrator |
| **Investigate** interactively with code | SageMaker notebooks |
| **Track** incidents to resolution | OpsCenter |
| **Determine** blast radius + timeline | Detective |
| **Contain** credential exfiltration | Inline Deny + TokenIssueTime |
| **Preserve** volatile memory | No-reboot AMI |
| **Preserve** disk evidence | EBS snapshot |

---

## Exam Gotchas

| Trap | Truth |
|---|---|
| "Terminate instance to stop attack" | NEVER terminate first — evidence lost. Isolate with deny-all SG. |
| "dd /dev/mem for memory dump" | Restricted on modern Amazon Linux. No-reboot AMI is the AWS answer. |
| "Deny-all SG captures memory" | SG only isolates network. Memory capture = no-reboot AMI. |
| "Detective is first step" | Detective comes AFTER containment. Validate findings → contain → THEN investigate. |
| "GuardDuty remediates" | GuardDuty only DETECTS. Remediation = EventBridge → Lambda/Step Functions. |
| "FIS causes real incidents" | FIS is for TESTING — controlled experiments with safety stop conditions. |
| "Resilience Hub shifts traffic" | Resilience Hub ASSESSES. ARC SHIFTS. Different tools. |
| "ARC = Route 53 failover" | ARC = AZ-level (LB-based, seconds). R53 = region-level (DNS, TTL delay). |
| "SageMaker automates IR" | SageMaker = interactive analysis. Step Functions = automation. |
| "Config auto-remediates in real-time" | Config latency = minutes. EventBridge = seconds. For sub-minute IR, use EventBridge. |

---

## Quotas & Timing

| Item | Value |
|---|---|
| GuardDuty finding delivery to EventBridge | ~5 minutes |
| FIS experiment max duration | 12 hours |
| ARC zonal shift max duration | User-specified (must set expiration) |
| EBS snapshot start time | Immediate (point-in-time capture) |
| No-reboot AMI creation time | Minutes (depends on volume size) |
| STS token max validity (role) | 1-12 hours (1 hour for role chaining) |
| TokenIssueTime inline Deny effect | Immediate (next API call) |

---

## 🧠 Cheat-Sheet One-Liners

- **FIS = test IR plan (chaos). Resilience Hub = assess RTO/RPO. ARC = shift traffic from bad AZ.** Three different phases: test → assess → recover.
- **Automated Forensics Orchestrator = Step Functions pipeline: triage → isolate (SG) → acquire (snapshot + memory via SSM) → investigate → report.**
- **SageMaker notebooks = interactive forensic workbench for analysts. NOT automation — that's Step Functions.**
- **OpsCenter = centralized ticket tracker for security findings. Auto-creates OpsItems from GuardDuty/Config/SH.**
- **"Test effectiveness of IR plan" = FIS. "Assess resilience posture" = Resilience Hub. "Recover from AZ" = ARC.** Never confuse test vs assess vs recover.
- **No-reboot AMI = volatile memory. EBS snapshot = disk. Both needed for complete forensics.**
- **OutsideAWS = TokenIssueTime. InsideAWS = SG isolation.** The finding type tells you the containment method.
- **Credential leak = Deactivate keys + Deny-all on user BEFORE investigating.** Contain all paths first.
