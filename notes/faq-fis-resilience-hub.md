# FAQ: AWS Fault Injection Service & Resilience Hub

> **Blueprint refs:** Task 2.1 (test and validate IR plans)
> **New in C03:** Yes — FIS and Resilience Hub explicitly added

## AWS Fault Injection Service (FIS)

### One-Liner

**Controlled chaos engineering — inject failures into AWS resources to test your IR plans and resilience.**

### What It Does

```
FIS = "Break things on purpose to see if your response works"

Examples:
├── Stop EC2 instances → does your auto-scaling recover?
├── Throttle API calls → does your app degrade gracefully?
├── Disrupt network → does failover trigger?
├── Inject CPU stress → does your alarm fire?
└── Terminate EKS pods → does your IR runbook kick in?
```

### Experiment Components

| Component | What It Is |
|---|---|
| **Experiment template** | Blueprint defining what to break and how |
| **Actions** | The faults to inject (stop instance, throttle API, network disruption) |
| **Targets** | Which resources to affect (by tag, ARN, or filter) |
| **Stop conditions** | CloudWatch alarms that auto-stop the experiment if things go too wrong |
| **IAM role** | FIS assumes a role with permissions to break your stuff |

### Supported Targets

- EC2 instances (stop, terminate, reboot)
- ECS tasks (stop)
- EKS pods (terminate, network disruption)
- RDS (failover, reboot)
- Network (disrupt connectivity, packet loss, latency)
- Systems Manager (CPU stress, memory stress, disk stress)
- API throttling (simulate service limits)

### Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Not a security scanner** | FIS tests resilience, not vulnerabilities |
| **Stop conditions are critical** | Always set CloudWatch alarm as safety net |
| **IAM scoped** | FIS can only break what its role allows — least privilege applies |
| **Tags for targeting** | Use tags to limit blast radius (e.g., only "env=staging") |
| **Integrates with EventBridge** | Experiment state changes trigger events |
| **Exam signal** | "test IR plan" / "simulate failure" / "chaos engineering" → FIS |

---

## AWS Resilience Hub

### One-Liner

**Assess and validate your application's resilience posture against defined RTO/RPO targets.**

### What It Does

```
Resilience Hub = "Are you READY for failures before they happen?"

├── Define your app (import from CloudFormation, Terraform, or manual)
├── Set resilience targets (RTO: 4hr, RPO: 1hr)
├── Run assessment → Hub checks if architecture meets targets
├── Get recommendations → "Add Multi-AZ to this RDS" / "Add cross-region backup"
└── Track compliance over time
```

### Key Concepts

| Concept | What It Means |
|---|---|
| **RTO** | Recovery Time Objective — how fast you must recover |
| **RPO** | Recovery Point Objective — how much data loss is acceptable |
| **Resilience policy** | Your defined RTO/RPO targets per disruption type |
| **Assessment** | Automated check of architecture vs. targets |
| **Recommendations** | Specific actions to close resilience gaps |
| **Resilience score** | 0-100 score per application |

### Disruption Types Assessed

- AZ disruption (single AZ failure)
- Region disruption (entire region failure)
- Infrastructure disruption (hardware failure)
- Application disruption (software failure)

### Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Not a testing tool** | Resilience Hub *assesses* — FIS *tests*. Different verbs. |
| **Imports architecture** | Reads CloudFormation/Terraform to understand your app |
| **Continuous** | Can run assessments on schedule, track drift |
| **Integrates with FIS** | Can generate FIS experiment templates from its findings |
| **Exam signal** | "validate resilience" / "assess RTO/RPO" / "resilience posture" → Resilience Hub |

---

## FIS vs Resilience Hub — Don't Confuse

| Dimension | FIS | Resilience Hub |
|---|---|---|
| **Verb** | Test / inject / simulate | Assess / validate / recommend |
| **What it does** | Breaks things in controlled way | Checks if architecture is resilient |
| **When** | During testing (active) | Before/after (passive analysis) |
| **Output** | "Did your system survive?" | "Would your system survive?" |
| **Exam signal** | "test IR plan" / "chaos engineering" | "validate resilience" / "assess RTO" |

## 🧠 Cheat-Sheet One-Liners

- **FIS = break things on purpose to test response.** "Test IR plan" / "simulate failure" → FIS.
- **Resilience Hub = assess architecture against RTO/RPO targets.** "Validate resilience posture" → Resilience Hub.
- **FIS tests. Resilience Hub assesses.** Different verbs, different services.
