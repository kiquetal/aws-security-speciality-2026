# GenAI Security — Flashcard (Task 3.2)

> Blueprint: Task 3.2.7 (GenAI OWASP Top 10 protections)
> Expected: 2-4 questions on the exam. NEW in C03.

---

## Bedrock Security — 4 Layers

```
Layer 1: MODEL ACCESS CONTROL (who can invoke which model)
  → IAM: bedrock:InvokeModel + model ARN
  → SCP: Deny InvokeModel on unapproved model ARN = org-wide block
  → Simplified access: models auto-available BUT IAM/SCP still enforced

Layer 2: CONTENT FILTERING (Guardrails)
  → 5 filter types (see next slide)
  → Filters INPUT and OUTPUT (both directions)
  → IAM condition: bedrock:GuardrailIdentifier = mandatory per call

Layer 3: NETWORK ISOLATION
  → VPC endpoint: com.amazonaws.{region}.bedrock (management APIs)
  → VPC endpoint: com.amazonaws.{region}.bedrock-runtime (inference)
  → Both Interface type. Endpoint policy restricts principals/actions.

Layer 4: DATA PRIVACY
  → Your data NOT used to train models (opted out BY DEFAULT)
  → Model customization data stays in YOUR account
  → CloudTrail logs EVERY InvokeModel call
  → KMS at rest + TLS in transit
```

---

## Guardrails — 5 Filter Types

| Filter | What it blocks | Example |
|---|---|---|
| **Content filters** | Hate, violence, sexual, insults | "violence score > medium → block" |
| **Denied topics** | Entire subjects you define | "Never discuss competitors" |
| **Word filters** | Specific words/phrases (exact match) | Block profanity, project codenames |
| **PII filters** | Sensitive data in/out | Mask SSNs, credit cards in responses |
| **Contextual grounding** | Hallucinations | "Is response grounded in source docs?" |

🧠 **Guardrails filter BOTH directions: input AND output. Not just responses.**

---

## Guardrail Enforcement (IAM)

```
PROBLEM: Developer calls InvokeModel WITHOUT a guardrail
SOLUTION: IAM/SCP condition forces guardrail on every call

SCP example:
{
  "Effect": "Deny",
  "Action": "bedrock:InvokeModel",
  "Resource": "*",
  "Condition": {
    "StringNotEquals": {
      "bedrock:GuardrailIdentifier": "arn:aws:bedrock:us-east-1:123:guardrail/abc123"
    }
  }
}

= "Deny InvokeModel unless THIS guardrail is attached"
```

**Three ways to enforce:**
- IAM policy with condition (per-role)
- SCP with condition (org-wide)
- Both together (defense in depth)

---

## ApplyGuardrail — Standalone API

```
bedrock:ApplyGuardrail
  → Filter ANY text through guardrails
  → Does NOT need bedrock:InvokeModel permission
  → Does NOT invoke a model
  → Use for: non-AWS LLMs (self-hosted on EC2, third-party)

Use case:
  App → calls OpenAI API → gets response
  App → calls bedrock:ApplyGuardrail → filters PII from response
  App → returns clean response to user
```

🧠 **"Filter content from non-AWS LLM" = ApplyGuardrail (standalone, no model invocation)**

---

## OWASP LLM Top 10 → AWS Mapping

| OWASP Risk | AWS Answer |
|---|---|
| **Prompt Injection** | Guardrails input filters + denied topics |
| **Insecure Output** | Guardrails output filters + content filters |
| **PII Disclosure** | Guardrails PII filter + CW Logs data protection |
| **Excessive Agency** | IAM least privilege on Bedrock agent actions |
| **Overreliance** | Contextual grounding checks |
| **Model Theft** | IAM + VPC endpoints + model access controls |

🧠 You don't need the full OWASP list. Just the AWS mitigation mapping.

---

## Amazon Q Business

```
WHAT: Enterprise doc Q&A (internal knowledge base)
AUTH: IAM Identity Center REQUIRED (not IAM users)
ACLS: Auto-crawled from source connectors
      → User sees ONLY their permitted docs
      → Once enabled, ACLs CAN'T BE DISABLED (permanent)
CONTROLS: Admin can block specific topics
ENCRYPTION: KMS at rest, TLS in transit
AUDIT: CloudTrail logs all API calls
```

**Exam traps:**
- Q Business requires Identity Center (not Cognito, not IAM users)
- ACLs can't be disabled once enabled
- "User sees HR docs they shouldn't" = ACL identity mapping failed (not ACLs disabled)

---

## CodeGuru Security vs Inspector

```
CodeGuru Security = SAST (SOURCE CODE, pre-deploy)
  → Hardcoded secrets
  → SQL injection patterns
  → Insecure AWS SDK usage
  → OWASP Top 10 / CWE Top 25
  → Findings → Security Hub
  → Languages: Java, Python, JS, TS, C#, Go, Ruby, PHP, Kotlin

Inspector = CVE scanning (RUNNING SYSTEMS, post-deploy)
  → Known CVEs in OS packages
  → Known CVEs in Lambda dependencies
  → Container image vulnerabilities
  → Network exposure findings

"Find issues in CODE" → CodeGuru
"Find issues in RUNNING systems" → Inspector
```

---

## Exam Decision Table

| Signal | Answer | NOT this |
|---|---|---|
| "Prevent prompt injection" | **Bedrock Guardrails** | ❌ WAF (HTTP, not LLM content) |
| "Block PII in LLM responses" | **Bedrock Guardrails** PII filter | ❌ Macie (S3 only) |
| "Block model org-wide" | **SCP** deny InvokeModel on model ARN | ❌ Guardrails (content, not access) |
| "Force guardrail on every call" | **SCP/IAM** + `bedrock:GuardrailIdentifier` | ❌ Console toggle (doesn't exist) |
| "Filter non-AWS LLM output" | **ApplyGuardrail** standalone | ❌ InvokeModel (that's for AWS models) |
| "Audit model usage" | **CloudTrail** | ❌ GuardDuty |
| "Enterprise doc Q&A with ACLs" | **Q Business** + Identity Center | ❌ Cognito |
| "Find hardcoded keys in code" | **CodeGuru Security** | ❌ Inspector (runtime CVEs) |
| "Find CVE in Lambda dependency" | **Inspector** | ❌ CodeGuru (code patterns) |

---

## 🧠 Exam One-Liners

- **Guardrails filter INPUT and OUTPUT.** Not just responses — prompts too.
- **Guardrails ≠ WAF.** WAF = HTTP request filtering. Guardrails = LLM content filtering. Different layers.
- **`bedrock:GuardrailIdentifier`** = IAM/SCP condition making guardrail mandatory per call.
- **`bedrock:ApplyGuardrail`** = standalone. Filter ANY text. No model invocation. Non-AWS LLMs.
- **Two VPC endpoints:** `bedrock` (management) + `bedrock-runtime` (inference). Both Interface.
- **Data not used for training** — opted out by default. No action needed.
- **"Block model org-wide"** = SCP deny InvokeModel on model ARN.
- **Q Business = Identity Center + ACLs (can't disable).** Q Developer = IDE code assistant.
- **CodeGuru = SAST (pre-deploy code). Inspector = CVE (post-deploy runtime).** Different moments.
- **Hardcoded secret found in code → Secrets Manager.** Never env vars (plaintext in console).
