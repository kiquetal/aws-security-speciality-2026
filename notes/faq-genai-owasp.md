# FAQ: GenAI Security — Bedrock Guardrails & OWASP LLM Top 10

> **Blueprint refs:** Task 3.2.7 (implement protections and guardrails for generative AI applications)
> **New in C03:** Yes — brand new, no C02 precedent

## One-Liner

**Amazon Bedrock Guardrails = content filtering + access controls for LLM applications. Prevents prompt injection, data leakage, and harmful outputs.**

## What the Exam Tests

```
You DON'T need to memorize the full OWASP LLM Top 10 list.
You DO need to know:

1. Amazon Bedrock Guardrails is the AWS answer for GenAI security
2. Prompt injection = attacker manipulates LLM via crafted input
3. Model access controls = who can invoke which foundation model
4. Content filters = block harmful/sensitive content in inputs AND outputs
5. "Protect AI application" / "prevent prompt injection" → Bedrock Guardrails
```

## Amazon Bedrock Guardrails

### What It Does

```
User Input → Guardrails (INPUT filter) → Foundation Model → Guardrails (OUTPUT filter) → Response
                  │                                                │
                  ├── Block prompt injection                       ├── Block harmful content
                  ├── Block denied topics                          ├── Block PII in responses
                  ├── Block PII in prompts                         ├── Enforce word filters
                  └── Apply content filters                        └── Apply grounding checks
```

### Guardrail Components

| Component | What It Does | Example |
|---|---|---|
| **Content filters** | Block harmful categories (hate, violence, sexual, insults) | Block responses with violence score > medium |
| **Denied topics** | Block specific subjects entirely | "Never discuss competitor products" |
| **Word filters** | Block specific words/phrases | Block profanity, internal project names |
| **Sensitive information filters** | Detect/mask PII in input/output | Mask SSNs, credit cards in responses |
| **Contextual grounding** | Check if response is grounded in source | Reduce hallucinations |

### Access Controls for Models

| Control | Mechanism |
|---|---|
| **Who can invoke models** | IAM policies on `bedrock:InvokeModel` |
| **Which models are available** | Model access management in Bedrock console |
| **Cross-account model sharing** | Resource-based policies on custom models |
| **VPC access** | VPC endpoints for Bedrock (no internet needed) |
| **Logging** | CloudTrail logs all Bedrock API calls |

## OWASP LLM Top 10 — AWS Mapping (Exam-Relevant Subset)

| OWASP Risk | AWS Mitigation |
|---|---|
| **LLM01: Prompt Injection** | Bedrock Guardrails input filters + denied topics |
| **LLM02: Insecure Output Handling** | Bedrock Guardrails output filters + content filters |
| **LLM06: Sensitive Information Disclosure** | Bedrock Guardrails PII filters + CloudWatch Logs data protection |
| **LLM08: Excessive Agency** | IAM least privilege on Bedrock agent actions |
| **LLM09: Overreliance** | Contextual grounding checks |
| **LLM10: Model Theft** | IAM policies, VPC endpoints, model access controls |

> The exam won't ask "what is LLM03?" — it asks "how do you protect against X in AWS?"

## Key Limits/Quotas

| Limit | Value |
|---|---|
| Guardrails per account per region | 100 |
| Denied topics per guardrail | 30 |
| Word filters per guardrail | 10,000 words |
| Content filter categories | 4 (hate, insults, sexual, violence) + custom |
| Latency impact | Milliseconds (evaluated inline) |
| Cost | Per-policy evaluation (charged per 1,000 text units) |

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Guardrails work on input AND output** | Filters apply in both directions |
| **Not just Bedrock models** | Can apply guardrails to self-hosted models via Bedrock API |
| **IAM controls model access** | `bedrock:InvokeModel` + resource ARN for specific models |
| **CloudTrail logs everything** | Model invocations, guardrail evaluations, all auditable |
| **VPC endpoints available** | Private access to Bedrock without internet |
| **Not WAF** | WAF protects HTTP APIs. Guardrails protect LLM content. Different layers. |
| **Not Inspector** | Inspector scans code for CVEs. Guardrails filter LLM I/O. Different problems. |

## Decision Table

| Exam Question Says | Answer | NOT This |
|---|---|---|
| "Prevent prompt injection in AI app" | **Bedrock Guardrails** | ❌ WAF (HTTP layer, not content-aware) |
| "Block PII in LLM responses" | **Bedrock Guardrails** (sensitive info filter) | ❌ Macie (S3 only) |
| "Control who can invoke foundation models" | **IAM policy** on `bedrock:InvokeModel` | ❌ Guardrails (content, not access) |
| "Audit LLM usage" | **CloudTrail** | ❌ GuardDuty |
| "Scan Lambda code for vulnerabilities" | **Inspector** | ❌ Bedrock Guardrails |

## K8s Mapping

```
Bedrock Guardrails  ≈  OPA/Gatekeeper admission webhook for LLM requests
Content filters     ≈  Envoy external authorization filter
Denied topics       ≈  NetworkPolicy blocking specific egress
Model access        ≈  RBAC on custom resources (who can use which model)
```

## 🧠 Cheat-Sheet One-Liners

- **"Protect AI application" / "prevent prompt injection" = Bedrock Guardrails.** Filters input AND output.
- **Guardrails ≠ WAF.** WAF = HTTP request filtering. Guardrails = LLM content filtering. Different layers.
- **Model access = IAM.** `bedrock:InvokeModel` with resource ARN controls who invokes which model.
- **All Bedrock activity logged in CloudTrail.** Model invocations, guardrail triggers, everything auditable.
