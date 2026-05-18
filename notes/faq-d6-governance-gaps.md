# FAQ: D6 Governance Gaps — StackSets, Service Catalog, Audit Manager, Artifact

> **Blueprint refs:** Task 6.2 (secure deployment strategy), Task 6.3 (evaluate compliance)
> **Purpose:** Fill the last untested gaps before exam day.

---

## 1. CloudFormation StackSets (Task 6.2)

### One-Liner

**Deploy the same CloudFormation template across multiple accounts and regions in one operation.**

### How It Works

```
Admin Account (management or delegated admin):
  │
  └── StackSet: "security-baseline"
        ├── Template: GuardDuty enablement + Config rules + CloudTrail
        ├── Target: All accounts in "Production" OU
        ├── Regions: us-east-1, eu-west-1, ap-southeast-1
        │
        ▼ automatically creates stack instances
  ┌──────────┐  ┌──────────┐  ┌──────────┐
  │ Account A│  │ Account B│  │ Account C│
  │ 3 regions│  │ 3 regions│  │ 3 regions│
  └──────────┘  └──────────┘  └──────────┘
```

### Two Permission Models

| Model | How | When |
|---|---|---|
| **Self-managed** | You create IAM roles in each account manually | Legacy, standalone accounts |
| **Service-managed** | StackSets uses Organizations — auto-deploys to new accounts | ✅ Exam preference |

### Exam Signals

| Signal | Answer |
|---|---|
| "Deploy security baseline to all accounts" | StackSets |
| "IaC across multiple accounts and regions" | StackSets |
| "New account joins org → auto-gets Config/GuardDuty" | StackSets (service-managed, auto-deploy enabled) |
| "Deploy ONE template to 200 accounts" | StackSets |

### Key Limits

| Limit | Value |
|---|---|
| Stack instances per StackSet | 2,000 |
| Concurrent operations per region | 1 |
| Max concurrent accounts | Configurable (default 1, increase for speed) |
| Failure tolerance | Configurable (e.g., "stop if 5 accounts fail") |

### Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Service-managed = Organizations integration** | Auto-deploys to new accounts in target OUs |
| **Drift detection** | StackSets can detect if someone modified resources manually |
| **Deletion** | Deleting StackSet deletes all stack instances across all accounts |
| **Region ordering** | Deploys to regions sequentially by default (can parallelize) |
| **Not real-time** | Deployment takes minutes — not instant like SCPs |
| **vs Firewall Manager** | FM deploys security RULES. StackSets deploys any RESOURCE. |
| **vs Control Tower** | Control Tower uses StackSets internally for its baseline |

### StackSets vs Firewall Manager vs Control Tower

| | StackSets | Firewall Manager | Control Tower |
|---|---|---|---|
| **Deploys** | Any CloudFormation resource | WAF/Shield/SG/NF/DNS FW rules only | Landing zone + guardrails |
| **Scope** | Any resource you can template | Security rules only | Account onboarding + governance |
| **Auto-remediate** | ❌ (just deploys) | ✅ (re-applies if removed) | ✅ (drift detection) |
| **Exam signal** | "deploy resources" / "IaC" | "enforce security rules" | "landing zone" / "guardrails" |

---

## 2. AWS Service Catalog (Task 6.2)

### One-Liner

**Pre-approved, self-service product catalog — users launch standardized resources without needing broad IAM permissions.**

### How It Works

```
Admin creates:
  Portfolio: "Approved Security Products"
    ├── Product: "Compliant S3 Bucket" (CF template with encryption + logging)
    ├── Product: "Hardened EC2" (CF template with IMDSv2 + SSM agent)
    └── Product: "Approved VPC" (CF template with flow logs + endpoints)

Developer experience:
  "I need an S3 bucket"
  → Opens Service Catalog → picks "Compliant S3 Bucket" → Launch
  → Gets a bucket with encryption, logging, tags — all pre-configured
  → Developer never needs s3:CreateBucket permission directly
```

### Key Concepts

| Concept | What It Is |
|---|---|
| **Portfolio** | Collection of products, shared with accounts/OUs |
| **Product** | CloudFormation template packaged for self-service |
| **Constraint** | Rules on how products can be launched (e.g., allowed instance types) |
| **Launch role** | IAM role that Service Catalog assumes to create resources — user doesn't need resource permissions |
| **TagOption** | Enforce tags on all provisioned resources |

### Exam Signals

| Signal | Answer |
|---|---|
| "Self-service with guardrails" | Service Catalog |
| "Developers deploy without broad IAM" | Service Catalog (launch role) |
| "Standardized, pre-approved resources" | Service Catalog |
| "Enforce compliance at deployment time" | Service Catalog constraints |

### Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Launch role** | User doesn't need resource permissions — Service Catalog assumes a role with those permissions |
| **Share via Organizations** | Portfolios can be shared across accounts via Organizations |
| **Not a firewall** | Doesn't block non-catalog deployments (use SCPs for that) |
| **vs StackSets** | StackSets = admin pushes. Service Catalog = user pulls (self-service). |

---

## 3. AWS Audit Manager (Task 6.3)

### One-Liner

**Continuously collect evidence for compliance audits — maps AWS activity to compliance frameworks automatically.**

### How It Works

```
1. Choose a framework:
   ├── SOC 2
   ├── PCI DSS
   ├── HIPAA
   ├── GDPR
   ├── CIS Benchmarks
   └── Custom framework

2. Audit Manager automatically collects evidence:
   ├── Config rule evaluations → "Is encryption enabled?"
   ├── CloudTrail logs → "Who accessed what?"
   ├── Security Hub findings → "Are controls passing?"
   └── Manual evidence → upload screenshots, attestations

3. Generate assessment report → hand to auditor
```

### Key Concepts

| Concept | What It Is |
|---|---|
| **Framework** | Compliance standard (SOC 2, PCI, HIPAA, custom) |
| **Control** | Specific requirement within a framework |
| **Assessment** | Active evaluation against a framework |
| **Evidence** | Proof that a control is met (auto-collected or manual) |
| **Delegation** | Assign control owners to collect manual evidence |

### Evidence Types (Auto-Collected)

| Source | What It Proves |
|---|---|
| **AWS Config** | Resource compliance (encryption on, logging on) |
| **CloudTrail** | Activity audit (who did what) |
| **Security Hub** | Security posture (controls passing/failing) |
| **Manual upload** | Screenshots, policy documents, attestations |

### Exam Signals

| Signal | Answer |
|---|---|
| "Prepare for SOC 2 / PCI audit" | Audit Manager |
| "Collect compliance evidence automatically" | Audit Manager |
| "Map AWS controls to compliance frameworks" | Audit Manager |
| "Generate audit-ready reports" | Audit Manager |

### Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Not a scanner** | Doesn't find vulnerabilities (that's Inspector) or threats (that's GuardDuty) |
| **Not Security Hub** | Security Hub = real-time compliance dashboard. Audit Manager = evidence collection for auditors. |
| **Delegated admin** | ✅ Supported — run from security account |
| **Custom frameworks** | Can create your own if standard ones don't fit |
| **Evidence retention** | Stored in your S3 bucket |

---

## 4. AWS Artifact (Task 6.3)

### One-Liner

**Download AWS compliance reports and agreements (SOC, PCI, ISO, BAA) — proves AWS's side of shared responsibility.**

### What It Provides

```
Artifact = "AWS's compliance paperwork"

├── Reports (read-only):
│   ├── SOC 1, SOC 2, SOC 3 reports
│   ├── PCI DSS Attestation of Compliance
│   ├── ISO 27001, 27017, 27018 certificates
│   ├── FedRAMP authorization
│   └── Penetration test reports
│
└── Agreements (accept/manage):
    ├── BAA (Business Associate Agreement) for HIPAA
    ├── GDPR DPA (Data Processing Agreement)
    └── Other regulatory agreements
```

### Exam Signals

| Signal | Answer |
|---|---|
| "Download AWS SOC 2 report" | Artifact |
| "Prove AWS is PCI compliant" | Artifact |
| "Sign BAA for HIPAA" | Artifact (agreements) |
| "AWS's compliance certifications" | Artifact |

### Artifact vs Audit Manager

| | Artifact | Audit Manager |
|---|---|---|
| **Whose compliance?** | AWS's (their infrastructure) | Yours (your workloads) |
| **What it provides** | AWS certifications/reports | Evidence from your account |
| **Who uses it** | You show auditor "AWS is compliant" | You show auditor "WE are compliant" |
| **Exam signal** | "AWS's SOC report" | "Collect evidence for our audit" |

---

## 5. Config Conformance Packs (Task 6.3)

### One-Liner

**Bundle of Config rules + remediation actions deployed as a single unit — org-wide via delegated admin.**

> ⚠️ This is a feature of **AWS Config** — not a separate service. Think of it as "Config rules in bulk."

### Hierarchy

```
AWS Config
├── Individual Config rules (one rule at a time, one account)
├── Conformance packs (bundle of rules + remediation as ONE unit)
│   ├── Account-level conformance pack (one account)
│   └── Organizational conformance pack (all accounts from delegated admin)
└── Aggregators (view compliance across accounts — read-only)
```

### AWS Pre-Built Packs (just pick and deploy)

- `Operational-Best-Practices-for-PCI-DSS`
- `Operational-Best-Practices-for-HIPAA`
- `Operational-Best-Practices-for-CIS`
- `Operational-Best-Practices-for-NIST-800-53`
- Or build your own custom pack with Lambda-backed rules

### How It Works

```
Conformance Pack: "PCI-DSS-Operational-Best-Practices"
  ├── Rule: s3-bucket-server-side-encryption-enabled
  ├── Rule: restricted-ssh
  ├── Rule: cloud-trail-enabled
  ├── Rule: rds-storage-encrypted
  └── ... 30+ rules in one pack

Deploy org-wide:
  Delegated admin → deploy conformance pack → all 200 accounts get all rules
```

### Exam Signals

| Signal | Answer |
|---|---|
| "Deploy bundle of compliance rules org-wide" | Conformance pack |
| "PCI/HIPAA compliance rules as a package" | Conformance pack |
| "Config rules + remediation in one deployment" | Conformance pack |

### vs Security Hub Standards

| | Conformance Packs | Security Hub Standards |
|---|---|---|
| **Engine** | Config rules directly | Config rules (wrapped by Security Hub) |
| **Dashboard** | Config console | Security Hub console (better UX) |
| **Custom rules** | ✅ Include custom Lambda rules | ❌ Only AWS-managed controls |
| **Remediation** | ✅ Built into the pack | ❌ Separate (EventBridge + Lambda) |
| **Exam preference** | "Custom compliance" / "remediation included" | "Least overhead" / "dashboard" / "aggregate" |

---

## 🧠 Cheat-Sheet One-Liners

- **StackSets = push IaC to many accounts.** Service Catalog = users pull pre-approved resources.
- **Audit Manager = YOUR compliance evidence.** Artifact = AWS's compliance reports.
- **Conformance pack = bundle of Config rules deployed as one unit.** Security Hub standard = same rules but with dashboard + aggregation.
- **"Self-service with guardrails" = Service Catalog.** Launch role means user doesn't need broad IAM.
