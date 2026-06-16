# FAQ: New & Undertested SCS-C03 Services (GenAI, ML, Storage)

> **Blueprint refs:** Task 3.2 (compute security), Task 5.2 (data at rest), ML section
> **Exam update:** SCS-C03 (March 2026) "expands coverage of emerging technologies, with dedicated focus on generative AI and machine learning security"
> **Risk:** Expect 2-4 questions from these services. Zero coverage = free misses.

---

## 1. Amazon Bedrock Security (Task 3.2 — GenAI)

### One-Liner
**Managed foundation model service. Security = control WHO calls WHICH models, WHAT content is filtered, and WHERE data flows.**

### Security Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  BEDROCK SECURITY LAYERS                                         │
│                                                                  │
│  Layer 1: MODEL ACCESS CONTROL                                   │
│  ├── IAM: bedrock:InvokeModel (per-model ARN)                   │
│  ├── SCP: Deny bedrock:InvokeModel on unapproved models         │
│  ├── Model access: enable/disable per model in console           │
│  └── IAM policies blocked models REMAIN blocked even if          │
│      "simplified model access" is enabled                        │
│                                                                  │
│  Layer 2: CONTENT FILTERING (Guardrails)                         │
│  ├── Deny topics (custom blocklist)                              │
│  ├── Content filters (hate, insults, sexual, violence, misconduct)│
│  ├── Sensitive info filters (PII, regex patterns)                │
│  ├── Word/phrase filters (exact match blocklist)                  │
│  ├── Contextual grounding (hallucination detection)              │
│  └── IAM policy-based enforcement (mandatory guardrail per call) │
│                                                                  │
│  Layer 3: NETWORK ISOLATION                                      │
│  ├── VPC Interface endpoint (com.amazonaws.{region}.bedrock)     │
│  ├── VPC endpoint for bedrock-runtime (InvokeModel)              │
│  ├── No public internet needed for private workloads             │
│  └── Endpoint policy restricts which principals/actions          │
│                                                                  │
│  Layer 4: DATA PRIVACY                                           │
│  ├── Your data is NOT used to train models (opted out by default)│
│  ├── Model customization data stays in your account              │
│  ├── CloudTrail logs every InvokeModel call                      │
│  └── Encryption: data encrypted at rest (KMS) and in transit     │
└─────────────────────────────────────────────────────────────────┘
```

### Guardrails — Exam-Critical Detail

```
Guardrails can be applied:
  1. Per invocation (developer passes guardrailId in API call)
  2. IAM policy-based enforcement (MANDATORY — can't bypass)
     → IAM condition: bedrock:GuardrailIdentifier
     → If condition not met → InvokeModel denied

ApplyGuardrail API:
  - Can be used INDEPENDENTLY of Bedrock models
  - Filter content from third-party LLMs (OpenAI, Anthropic direct)
  - Only needs bedrock:ApplyGuardrail permission (no InvokeModel)
```

### Key IAM Actions

| Action | Purpose |
|---|---|
| `bedrock:InvokeModel` | Call a foundation model |
| `bedrock:InvokeModelWithResponseStream` | Streaming inference |
| `bedrock:ApplyGuardrail` | Apply content filtering independently |
| `bedrock:CreateGuardrail` | Create guardrail configuration |
| `bedrock:GetFoundationModel` | View model details |
| `bedrock:ListFoundationModels` | List available models |
| `bedrock:CreateModelCustomizationJob` | Fine-tune a model |

### Exam Signals

| Signal | Answer |
|---|---|
| "Prevent prompt injection + block PII in responses" | Bedrock Guardrails |
| "Restrict which models developers can use" | IAM policy on `bedrock:InvokeModel` with model ARN |
| "Block specific model org-wide" | SCP denying `bedrock:InvokeModel` on model ARN |
| "Private access to Bedrock, no internet" | VPC Interface endpoint (bedrock-runtime) |
| "Ensure guardrail always applied" | IAM condition `bedrock:GuardrailIdentifier` |
| "Filter content from non-AWS LLM" | `bedrock:ApplyGuardrail` API (independent mode) |

### Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Guardrails ≠ WAF** | WAF = HTTP filtering. Guardrails = LLM content filtering. Different layers. |
| **ApplyGuardrail = standalone** | Works without InvokeModel. Filter ANY text, not just Bedrock models. |
| **Data not used for training** | Customer data opted out by default. No action needed. |
| **Model access simplified** | Models auto-available BUT IAM/SCP restrictions still enforced. |
| **Two VPC endpoints** | `bedrock` (management) + `bedrock-runtime` (inference). Both Interface type. |

---

## 2. Amazon Q Business Security (Task 3.2 — GenAI)

### One-Liner
**Enterprise AI assistant that answers questions from your company data. Security = who can query, what data they can see (ACL-based), and encryption.**

### Security Model

```
┌─────────────────────────────────────────────────────────────────┐
│  Amazon Q Business Security                                      │
│                                                                  │
│  IDENTITY: Must integrate with IAM Identity Center               │
│  ├── Users authenticate via Identity Center (SSO)                │
│  ├── No IAM users/roles for end-user access                     │
│  └── Corporate directory groups control who can use Q            │
│                                                                  │
│  DATA ACCESS (ACL crawling):                                     │
│  ├── Q Business crawls document ACLs from source connectors      │
│  ├── User only sees answers from docs they have access to        │
│  ├── ACL enforcement is AUTOMATIC (not manual per-doc)           │
│  └── Once ACLs enabled, can't be turned off                     │
│                                                                  │
│  ENCRYPTION:                                                     │
│  ├── Data encrypted at rest with AWS-owned or customer CMK       │
│  ├── In transit: TLS 1.2+                                        │
│  └── Index data encrypted with KMS                              │
│                                                                  │
│  ADMIN CONTROLS:                                                 │
│  ├── Admin controls: who can create apps, which connectors       │
│  ├── Topic blocks: prevent Q from answering about specific topics│
│  └── Guardrails integration for content safety                  │
└─────────────────────────────────────────────────────────────────┘
```

### Exam Signals

| Signal | Answer |
|---|---|
| "Enterprise Q&A over company docs, respect existing permissions" | Q Business + ACL crawling |
| "Identity for Q Business" | IAM Identity Center (required, not IAM users) |
| "User can only see answers from docs they have access to" | ACL-based document security (automatic) |
| "Block Q from answering about topic X" | Q Business topic controls (admin guardrails) |

### Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Requires Identity Center** | Cannot use IAM users for end-user access |
| **ACL = automatic** | Crawls permissions from source (SharePoint, S3, etc.) |
| **ACLs can't be disabled** | Once enabled, permanently on for that application |
| **Not same as Q Developer** | Q Business = enterprise docs. Q Developer = code. |

---

## 3. Amazon Q Developer / CodeGuru Security (Task 3.2)

### One-Liner
**SAST (Static Application Security Testing) in your IDE and CI/CD pipeline. Detects OWASP Top 10, CWE Top 25, secrets in code, and insecure AWS API usage.**

### What It Detects

```
CodeGuru Security scans for:
├── OWASP Top 10 (SQLi, XSS, SSRF, broken auth, etc.)
├── CWE Top 25 (buffer overflow, path traversal, etc.)
├── Hardcoded secrets (API keys, passwords, tokens)
├── Insecure AWS SDK usage (unencrypted S3, open SGs)
├── Log injection vulnerabilities
└── Languages: Java, Python, JavaScript, TypeScript, C#, Go, Ruby, PHP, Kotlin, Scala, Swift

Amazon Q Developer (in IDE):
├── Real-time code suggestions with security awareness
├── Inline vulnerability detection as you type
├── Remediation suggestions with code patches
└── Integrated in VS Code, JetBrains, CLI
```

### Pipeline Integration

```
CI/CD Pipeline:
  Code commit
    │
    ▼
  CodeGuru Security scan (SAST)
    ├── Critical findings → FAIL build
    ├── High findings → WARN
    └── Results → Security Hub (optional)
    │
    ▼
  Deploy (if passed)
```

### Exam Signals

| Signal | Answer |
|---|---|
| "Find vulnerabilities in code before deployment" | CodeGuru Security (SAST) |
| "Detect hardcoded secrets in source code" | CodeGuru Security |
| "Shift-left security in CI/CD" | CodeGuru Security |
| "Real-time security suggestions in IDE" | Amazon Q Developer |
| "Scan for OWASP Top 10 in code" | CodeGuru Security |

### Key Distinction

| | Inspector | CodeGuru Security |
|---|---|---|
| **What it scans** | Running resources (EC2, Lambda, ECR images) | Source code (before deployment) |
| **Finding type** | CVEs in packages/dependencies | Code-level vulnerabilities |
| **When** | Post-deployment (runtime) | Pre-deployment (CI/CD) |
| **Exam signal** | "Vulnerabilities in running workloads" | "Vulnerabilities in code" |

---

## 4. Amazon Managed Grafana Security

### One-Liner
**Managed Grafana for operational dashboards. Security = workspace access via Identity Center or SAML, data source permissions, VPC connectivity.**

### Key Security Facts

| Dimension | Detail |
|---|---|
| **Authentication** | IAM Identity Center OR SAML 2.0 (external IdP) |
| **Authorization** | Workspace-level roles: Admin, Editor, Viewer |
| **Data sources** | CloudWatch, Prometheus, OpenSearch, X-Ray, etc. |
| **Network** | Can connect to VPC data sources via VPC configuration |
| **Encryption** | AWS-managed key or customer CMK (at rest), TLS (in transit) |
| **Audit** | CloudTrail logs API calls to Grafana workspace |

### Exam Signal
- "Security dashboards with SAML/IdP authentication" → Managed Grafana
- "Visualize CloudWatch + Security Hub data with SSO" → Managed Grafana
- Low exam probability — likely 0-1 questions

---

## 5. AWS User Notifications

### One-Liner
**Centralized notification hub — aggregates notifications from multiple AWS services and delivers via email, Chatbot (Slack/Teams), or mobile push.**

### Key Facts

| Dimension | Detail |
|---|---|
| **Sources** | Security Hub, GuardDuty, Config, Health, Budgets, etc. |
| **Delivery** | Email, AWS Chatbot (Slack/Teams), Console mobile app |
| **Filtering** | By service, region, severity, specific resources |
| **Encryption** | Notifications encrypted in transit (TLS) |

### Exam Signal
- "Centralized notification management across AWS services" → User Notifications
- Very low exam probability — likely 0 questions

---

## 6. Amazon FSx for Lustre Security (Task 5.2)

### One-Liner
**High-performance parallel file system for compute workloads (ML training, HPC). Security = encryption + VPC + backup policies.**

### Security Features

```
┌──────────────────────────────────────────────────────────────┐
│ FSx for Lustre Security                                       │
│                                                               │
│ ENCRYPTION AT REST:                                           │
│ ├── Automatic (always encrypted)                              │
│ ├── XTS-AES-256 block cipher                                  │
│ ├── AWS managed key (default) or customer CMK                 │
│ ├── Only SYMMETRIC KMS keys supported                         │
│ └── Encrypted before written to disk                          │
│                                                               │
│ ENCRYPTION IN TRANSIT:                                        │
│ ├── Automatic between Lustre clients and file system          │
│ └── TLS 1.2+                                                  │
│                                                               │
│ NETWORK:                                                      │
│ ├── Deployed in VPC subnet                                    │
│ ├── Security groups control access                            │
│ ├── Only accessible from within VPC (or peered/transit)       │
│ └── No public internet access                                 │
│                                                               │
│ BACKUPS:                                                      │
│ ├── Automatic daily backups (configurable retention)          │
│ ├── Manual on-demand backups                                  │
│ ├── Stored in S3 (11 9's durability)                          │
│ └── Encrypted with same key as file system                   │
│                                                               │
│ S3 INTEGRATION:                                               │
│ ├── Can link to S3 bucket (data repository)                   │
│ ├── S3 bucket can use SSE-S3 or SSE-KMS                       │
│ ├── SSE-KMS linked bucket: FSx needs KMS permissions          │
│ └── Key policy must grant fsx.amazonaws.com                   │
│                                                               │
│ FILE SYSTEM TYPES:                                            │
│ ├── Scratch = temporary, no replication (performance only)    │
│ └── Persistent = replicated within AZ, supports backups       │
└──────────────────────────────────────────────────────────────┘
```

### Exam Signals

| Signal | Answer |
|---|---|
| "High-performance file system encryption" | FSx for Lustre (XTS-AES-256, symmetric KMS only) |
| "ML training data + encryption at rest" | FSx for Lustre + CMK |
| "FSx linked to SSE-KMS bucket" | Key policy must grant `fsx.amazonaws.com` |
| "Scratch vs Persistent" | Scratch = no backups, no replication. Persistent = backups + durability. |

### Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Always encrypted** | Can't create unencrypted FSx for Lustre (unlike EBS) |
| **Symmetric KMS only** | No asymmetric keys |
| **Scratch = no backup** | Data lost if server fails |
| **S3 linked + SSE-KMS** | Must add `fsx.amazonaws.com` to KMS key policy |
| **VPC only** | No public access, no VPC endpoint needed (direct ENI) |

---

## 🧠 Cheat-Sheet One-Liners

- **Bedrock Guardrails = LLM content filtering (prompt injection, PII). WAF = HTTP filtering. Different layers, complementary.**
- **Bedrock ApplyGuardrail = standalone API. Filter ANY text (even from non-AWS LLMs) without InvokeModel.**
- **Bedrock IAM enforcement: `bedrock:GuardrailIdentifier` condition = mandatory guardrail per call.**
- **Q Business = enterprise docs (Identity Center + ACL crawling). Q Developer = code (IDE + SAST).**
- **CodeGuru Security = SAST (code scanning pre-deploy). Inspector = CVE scanning (post-deploy runtime).**
- **FSx for Lustre = always encrypted (XTS-AES-256), symmetric KMS only, VPC-only, S3 linked needs key policy for fsx.amazonaws.com.**
- **"Find vulns in code" = CodeGuru. "Find vulns in running workloads" = Inspector.**
