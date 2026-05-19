# Bedrock Guardrails — Slide Deck

---

## What Is It

```
Amazon Bedrock Guardrails = content filtering for LLM apps

User Input → FILTER → Model → FILTER → Response
              ↑                   ↑
         INPUT side          OUTPUT side
```

Filters BOTH directions. Not just output.

---

## The 5 Filter Types

| Filter | Blocks | Example |
|---|---|---|
| **Content filters** | Hate, violence, sexual, insults | "violence score > medium → block" |
| **Denied topics** | Entire subjects | "Never discuss competitors" |
| **Word filters** | Specific words/phrases | Block profanity, project codenames |
| **PII filters** | Sensitive data in/out | Mask SSNs, credit cards |
| **Grounding checks** | Hallucinations | "Is response grounded in source docs?" |

---

## Access Control (Separate from Guardrails)

```
WHO can invoke models = IAM policy
  → bedrock:InvokeModel + resource ARN

WHICH models available = Bedrock console
  → Model access management

HOW to access privately = VPC endpoint
  → No internet needed

AUDIT = CloudTrail
  → Every invocation logged
```

🧠 Guardrails = content. IAM = access. Different layers.

---

## OWASP LLM Top 10 (Only Know These)

| Risk | AWS Answer |
|---|---|
| **Prompt Injection** | Guardrails input filters |
| **Insecure Output** | Guardrails output filters |
| **PII Disclosure** | Guardrails PII filter + CW Logs data protection |
| **Excessive Agency** | IAM least privilege on agent actions |
| **Model Theft** | IAM + VPC endpoints |

You don't need the full list. Just the AWS mapping.

---

## What Guardrails is NOT

```
Guardrails ≠ WAF
  WAF = HTTP request filtering (SQLi, XSS)
  Guardrails = LLM content filtering (prompt injection, PII)

Guardrails ≠ Inspector
  Inspector = code vulnerabilities (CVEs)
  Guardrails = runtime content filtering

Guardrails ≠ Macie
  Macie = find PII in S3
  Guardrails = mask PII in LLM responses
```

---

## Exam Decision Table

| Signal | Answer |
|---|---|
| "Prevent prompt injection" | **Bedrock Guardrails** |
| "Block PII in LLM responses" | **Bedrock Guardrails** |
| "Control who invokes models" | **IAM** (bedrock:InvokeModel) |
| "Audit model usage" | **CloudTrail** |
| "Block SQLi in API" | **WAF** (not Guardrails) |

---

## Key Limits

| Limit | Value |
|---|---|
| Guardrails per account/region | 100 |
| Denied topics per guardrail | 30 |
| Word filters | 10,000 |
| Cost | Per 1,000 text units evaluated |
| Latency | Milliseconds (inline) |

---

## K8s Mapping

```
Bedrock Guardrails  ≈  OPA/Gatekeeper for LLM requests
Content filters     ≈  Envoy ext_authz filter
Model access (IAM)  ≈  RBAC on CRDs
CloudTrail audit    ≈  K8s audit log
```

---

## 🧠 One-Liners

- **"Protect AI app" / "prompt injection" = Bedrock Guardrails.**
- **Guardrails filters input AND output.** Not just responses.
- **IAM controls access. Guardrails controls content.** Different problems.
- **Not WAF, not Inspector, not Macie.** Each solves a different thing.
