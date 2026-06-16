# FAQ: GenAI & ML Security (Task 3.2)

> **Blueprint refs:** Task 3.2 (compute security — GenAI OWASP Top 10), ML in-scope section
> **Exam update:** SCS-C03 (March 2026) adds "dedicated focus on generative AI and machine learning security"
> **Risk:** 2-4 questions expected.

---

## 1. Amazon Bedrock Security

### Security Layers

```
Layer 1: MODEL ACCESS CONTROL
├── IAM: bedrock:InvokeModel (per-model ARN)
├── SCP: Deny bedrock:InvokeModel on unapproved models org-wide
├── Simplified access: models auto-available BUT IAM/SCP still enforced
└── "Block model org-wide" = SCP on model ARN

Layer 2: CONTENT FILTERING (Guardrails)
├── Deny topics (custom blocklist)
├── Content filters (hate, insults, sexual, violence)
├── PII filters (SSN, credit cards, regex patterns)
├── Word/phrase blocklist (exact match)
├── Contextual grounding (hallucination detection)
└── IAM condition: bedrock:GuardrailIdentifier = mandatory per call

Layer 3: NETWORK ISOLATION
├── VPC endpoint: com.amazonaws.{region}.bedrock (management)
├── VPC endpoint: com.amazonaws.{region}.bedrock-runtime (inference)
└── Endpoint policy restricts principals/actions

Layer 4: DATA PRIVACY
├── Your data NOT used to train models (opted out by default)
├── Model customization data stays in your account
├── CloudTrail logs every InvokeModel call
└── Encryption at rest (KMS) + in transit (TLS)
```

### Guardrails (Exam-Critical)

| Feature | Detail |
|---|---|
| **Apply per call** | Pass `guardrailId` in InvokeModel request |
| **IAM enforcement** | Condition `bedrock:GuardrailIdentifier` makes guardrail mandatory |
| **Standalone API** | `bedrock:ApplyGuardrail` — filter ANY text, even non-AWS LLMs |
| **No InvokeModel needed** | ApplyGuardrail works independently |

### Exam Gotchas

| Gotcha | Detail |
|---|---|
| Guardrails ≠ WAF | WAF = HTTP. Guardrails = LLM content. Different layers. |
| ApplyGuardrail = standalone | Filter non-AWS LLMs without InvokeModel permission |
| Data not used for training | Opted out by default. No action needed. |
| Two VPC endpoints | `bedrock` (management) + `bedrock-runtime` (inference) |
| SCP still blocks | Simplified model access doesn't override IAM/SCP |

---

## 2. Amazon Q Business

### Security Model

| Dimension | Detail |
|---|---|
| **Identity** | IAM Identity Center required (not IAM users) |
| **Document ACLs** | Auto-crawled from source connectors. User sees only their docs. |
| **ACLs once enabled** | Can't be disabled. Permanent. |
| **Topic controls** | Admin blocks Q from answering specific topics |
| **Encryption** | KMS at rest, TLS in transit |
| **Audit** | CloudTrail logs all API calls |

### Key Rule
**Q Business = enterprise doc Q&A with automatic ACL enforcement. Requires Identity Center.**

---

## 3. Amazon Q Developer / CodeGuru Security

### What They Do

| | CodeGuru Security | Amazon Q Developer |
|---|---|---|
| **Type** | SAST (static code scan) | AI code assistant |
| **When** | CI/CD pipeline, pre-deploy | IDE, real-time as you type |
| **Finds** | OWASP Top 10, CWE Top 25, secrets, insecure AWS SDK | Same + suggests fixes inline |
| **Languages** | Java, Python, JS, TS, C#, Go, Ruby, PHP, Kotlin | Same |
| **Output** | Findings → Security Hub (optional) | Inline suggestions |

### Key Distinction (Exam-Critical)

```
"Find vulnerabilities in SOURCE CODE"     → CodeGuru Security (SAST, pre-deploy)
"Find vulnerabilities in RUNNING systems" → Inspector (CVE scanning, post-deploy)
```

---

## 🧠 Cheat-Sheet One-Liners

- **Bedrock Guardrails = LLM content filtering. WAF = HTTP filtering. Different layers.**
- **`bedrock:ApplyGuardrail` = standalone.** Filter ANY text without InvokeModel.
- **`bedrock:GuardrailIdentifier` condition = mandatory guardrail per call.**
- **"Block model org-wide" = SCP deny `bedrock:InvokeModel` on model ARN.**
- **Two Bedrock VPC endpoints: `bedrock` + `bedrock-runtime`.** Both Interface.
- **Q Business = enterprise docs (Identity Center + ACL). Q Developer = code (IDE + SAST).**
- **Q Business ACLs can't be disabled once enabled.**
- **CodeGuru = SAST (pre-deploy). Inspector = CVE (post-deploy).**
