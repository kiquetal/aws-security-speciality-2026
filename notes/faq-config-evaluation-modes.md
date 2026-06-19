# FAQ: AWS Config Evaluation Modes (Proactive vs Detective)

> **Blueprint refs:** Task 6.3 (compliance evaluation), Task 1.1 (monitoring)
> **Purpose:** Config has THREE evaluation modes. Dojo tests the distinction. Most people only know detective.

---

## Three Evaluation Modes

```
┌─────────────────────────────────────────────────────────────────┐
│  AWS CONFIG — THREE WAYS TO EVALUATE                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. DETECTIVE (default — what most people know)                  │
│  ═════════════════════════════════════════════                    │
│  WHEN:  AFTER resource exists (periodic or on change)            │
│  WHAT:  Evaluates existing resources against rules               │
│  RESULT: COMPLIANT / NON_COMPLIANT finding                       │
│  ACTION: Can auto-remediate via SSM Automation                   │
│  USE:    "Detect drift and fix"                                  │
│                                                                  │
│  2. PROACTIVE (newer — the one Dojo tests)                       │
│  ══════════════════════════════════════════                       │
│  WHEN:  BEFORE resource is created (during CloudFormation)       │
│  WHAT:  Evaluates resource config in CF template before deploy   │
│  RESULT: COMPLIANT → resource created. NON_COMPLIANT → blocked  │
│  ACTION: Resource NEVER exists if non-compliant                  │
│  USE:    "Prevent bad resources from ever existing"              │
│                                                                  │
│  3. CUSTOM (Lambda-based)                                        │
│  ═════════════════════════                                       │
│  WHEN:  On change or periodic (like detective)                   │
│  WHAT:  YOUR Lambda code evaluates whatever logic you want       │
│  RESULT: COMPLIANT / NON_COMPLIANT                               │
│  ACTION: Can auto-remediate                                      │
│  USE:    "Complex business logic not in managed rules"           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Proactive vs Detective — The Decision

```
QUESTION SAYS:                              ANSWER:
════════════                                ═══════

"Before provisioned"                    →   PROACTIVE
"Before resource is created"            →   PROACTIVE
"Ensure NO public IPs before subnets    →   PROACTIVE
 are provisioned"
"Prevent creation of noncompliant"      →   PROACTIVE (or SCP)

"Detect noncompliant resources"         →   DETECTIVE
"After resource exists"                 →   DETECTIVE
"Remediate drift"                       →   DETECTIVE + SSM
"Track configuration changes"           →   DETECTIVE (config history)
```

---

## All "Before Creation" Mechanisms Compared

| Mechanism | Service | How it works | Scope |
|---|---|---|---|
| Config PROACTIVE rules | AWS Config | Evaluates resource in CF template before creation | Per-account (or org via org rules) |
| CloudFormation Guard (cfn-guard) | CI/CD pipeline | Policy-as-code validates template in pipeline | Pipeline-level (shift-left) |
| CloudFormation Hooks | CloudFormation | Custom logic runs before each resource in stack | Per-account |
| Control Tower proactive guardrail | Control Tower | CF Hook deployed org-wide via CT | Organization-wide |
| SCP | Organizations | Blocks the API call itself | Organization-wide |

### When to pick which:

| Signal in question | Answer |
|---|---|
| "Config" in the options + "before provisioned" | Config proactive |
| "CI/CD pipeline" + "before deploy" | cfn-guard |
| "Control Tower" + "proactive guardrail" | CF Hook via CT |
| "Block API call org-wide" | SCP |
| "Validate template content" (no Config in options) | cfn-guard or CF Hook |

---

## Config Proactive — How It Works

```
Developer writes CloudFormation template:
  Resources:
    MySubnet:
      Type: AWS::EC2::Subnet
      Properties:
        MapPublicIpOnLaunch: true   ← noncompliant!

CloudFormation BEFORE creating the subnet:
  → Sends resource config to Config proactive rule
  → Rule evaluates: "MapPublicIpOnLaunch = true? NON_COMPLIANT"
  → CloudFormation: "Rule says NO. Abort resource creation."
  → Subnet NEVER exists.
```

---

## Detective + Remediation (Standard Pattern)

```
Resource created (already exists)
  → Config recorder captures configuration
  → Config rule evaluates: NON_COMPLIANT
  → Auto-remediation fires (SSM Automation document)
  → SSM fixes the resource (e.g., enables encryption, removes public access)
  
  GAP: Resource exists in non-compliant state briefly (minutes)
  RISK: Acceptable for most cases, not for "must NEVER exist"
```

---

## Exam Gotchas

| Gotcha | Truth |
|---|---|
| "Config can prevent resource creation" | YES — with proactive mode (newer feature) |
| "Config is only detective" | WRONG — also supports proactive (since ~2023) |
| "SCP prevents, Config detects" | MOSTLY true, but Config proactive also prevents |
| "Proactive = SCP" | DIFFERENT — SCP blocks API. Config proactive validates resource CONFIG in template. SCP can't inspect template content. |
| "Config proactive vs cfn-guard" | Config proactive = AWS-managed rules. cfn-guard = custom policy-as-code in YOUR pipeline. |

---

## 🧠 Cheat-Sheet One-Liners

- **Config proactive = evaluates BEFORE CloudFormation creates resources.** "Before provisioned" = proactive. "After exists" = detective.
- **SCP blocks the API call. Config proactive validates the resource configuration in the template.** Different layers.
- **Config detective + SSM = detect and fix (resource exists briefly). Config proactive = resource never exists.**
- **"Prevent noncompliant resources" + Config in options = proactive. Without Config = SCP.**
