# D6 Governance Gaps

---

## Admin PUSHES to accounts

```
StackSets        → any resource (GuardDuty, Config, CloudTrail)
Firewall Manager → security rules only (WAF, SG, NF, DNS FW)
```

---

## Users PULL from catalog

```
Service Catalog → pre-approved products (self-service)
```

---

## Compliance

```
Audit Manager    → collect YOUR evidence, generate YOUR report
Artifact         → download AWS's compliance reports
Conformance Pack → bundle Config rules + remediation as one unit
```

---

## 1. CloudFormation StackSets

**Deploy the same CF template across multiple accounts and regions.**

```
Admin Account
  └── StackSet: "security-baseline"
        ├── Template: GuardDuty + Config + CloudTrail
        ├── Target: "Production" OU
        └── Auto-deploy: ON (new accounts get it)
```

---

## StackSets — Permission Models

| Model | How | When |
|---|---|---|
| Self-managed | Manual IAM roles | Legacy |
| **Service-managed** | Organizations | ✅ Exam answer |

Service-managed + auto-deploy = new accounts get the stack.

---

## StackSets vs Firewall Manager

| | StackSets | Firewall Manager |
|---|---|---|
| **Deploys** | ANY resource | WAF/SG/NF/DNS FW ONLY |
| **Auto-remediate** | ❌ | ✅ |
| **Exam signal** | "deploy resources" | "enforce security rules" |

---

## 2. AWS Service Catalog

**Pre-approved, self-service product catalog.**

```
Admin creates products (CF templates):
  ├── "Compliant S3 Bucket"
  ├── "Hardened EC2"
  └── "Approved VPC"

Dev picks from catalog → Launch → gets compliant resource
```

---

## Service Catalog — Launch Role

```
Without launch role:
  Dev needs s3:CreateBucket → broad IAM = risk

With launch role:
  Dev needs servicecatalog:ProvisionProduct ONLY
  Service Catalog assumes the launch role
  → Dev gets resource without broad permissions
```

---

## Service Catalog vs StackSets

- StackSets = admin **PUSHES** (top-down)
- Service Catalog = user **PULLS** (self-service)

🧠 "Self-service without broad IAM" = Service Catalog

---

## 3. AWS Audit Manager

**Collect YOUR compliance evidence. Generate YOUR report.**

```
1. Pick framework: SOC 2 / PCI / HIPAA
2. Auto-collects evidence:
   ├── Config → "Is encryption on?"
   ├── CloudTrail → "Who accessed what?"
   └── Security Hub → "Controls passing?"
3. Generate report → hand to auditor
```

---

## 4. AWS Artifact

**Download AWS's compliance paperwork.**

```
Reports: SOC 1/2/3, PCI AoC, ISO 27001
Agreements: BAA (HIPAA), GDPR DPA
```

🧠 "Download AWS's SOC 2" = Artifact
🧠 "Sign BAA for HIPAA" = Artifact

---

## Artifact vs Audit Manager

| | Artifact | Audit Manager |
|---|---|---|
| **Whose?** | AWS's | YOURS |
| **Provides** | AWS certs | Your evidence |
| **Signal** | "AWS's SOC" | "Our audit" |

Artifact = AWS's receipts. Audit Manager = YOUR receipts.

---

## 5. Config Conformance Packs

⚠️ Feature of **AWS Config** — not a separate service.

```
Pack: "PCI-DSS-Best-Practices"
  ├── 30+ Config rules
  ├── Auto-remediation actions
  └── Deploy as ONE unit

Organizational pack from delegated admin
  → all 200 accounts get everything
```

---

## Conformance Packs vs Security Hub

| | Conformance Packs | Security Hub |
|---|---|---|
| Custom rules | ✅ Lambda | ❌ AWS only |
| Remediation | ✅ Built-in | ❌ Separate |
| Dashboard | Basic | ✅ Better |
| Signal | "bundle + remediation" | "least overhead" |

---

## Exam Decision Tree

```
"Deploy resources across accounts"     → StackSets
"Enforce WAF/SG rules across accounts" → Firewall Manager
"Self-service without broad IAM"       → Service Catalog
"Collect evidence for our audit"       → Audit Manager
"Download AWS's SOC/PCI report"        → Artifact
"Bundle Config rules + remediation"    → Conformance Pack
"Compliance dashboard, least overhead" → Security Hub
```
