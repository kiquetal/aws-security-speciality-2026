# FAQ: Amazon Verified Permissions

> **Blueprint refs:** Task 4.2 (authorization strategies)
> **Launched:** June 2023 — testable on SCS-C03

## One-Liner

**Application-level authorization engine — "Can user X do action Y on resource Z?" at runtime.**

Not for AWS API access (that's IAM). For YOUR app's permission logic.

## IAM vs Verified Permissions

```
IAM:                                    Verified Permissions:
├── "Can this role call s3:GetObject?"  ├── "Can user Alice edit document-123?"
├── AWS API level                       ├── Application level
├── JSON policies                       ├── Cedar policies
├── Evaluated by AWS                    ├── Evaluated by your app calling the API
└── Controls infrastructure access      └── Controls business logic access
```

| Dimension | IAM | Verified Permissions |
|---|---|---|
| **Scope** | AWS API actions | Your app's actions |
| **Language** | IAM JSON | Cedar |
| **Principals** | IAM users/roles | Your app's users (from Cognito, etc.) |
| **Resources** | AWS resources (buckets, keys) | Your app's resources (documents, orders) |
| **Evaluation** | Automatic on every AWS API call | Your app calls `IsAuthorized` API |

## How It Works

```
1. Define a SCHEMA (your app's entity types)
   → Users, Documents, Folders, Teams

2. Write CEDAR POLICIES
   → "Admins can do anything in their tenant"
   → "Viewers can only read documents in their team"

3. Create a POLICY STORE (container for policies)

4. App calls IsAuthorized at runtime:
   → Principal: "User::alice"
   → Action: "Action::editDocument"
   → Resource: "Document::doc-123"
   → Context: { tenant: "acme", ip: "10.0.1.5" }

5. Verified Permissions returns: ALLOW or DENY
```

## Cedar Policy Examples

### Allow admins full access in their tenant

```cedar
permit (
  principal in Role::"admin",
  action,
  resource
) when {
  principal.tenant == resource.tenant
};
```

### Allow viewers to read only

```cedar
permit (
  principal in Role::"viewer",
  action == Action::"viewDocument",
  resource
) when {
  principal.tenant == resource.tenant
};
```

### Deny access from outside allowed IPs

```cedar
forbid (
  principal,
  action,
  resource
) unless {
  context.ip.inRange(ip("10.0.0.0/16"))
};
```

## Integration with Cognito

```
Cognito User Pool (authentication)
  → User signs in → gets ID token with claims (groups, tenant, email)
  → App extracts claims
  → App calls Verified Permissions with claims as principal/context
  → Verified Permissions evaluates Cedar policies
  → Returns Allow/Deny
  → App enforces the decision
```

**Cognito authenticates (who are you?). Verified Permissions authorizes (what can you do?).**

## Key Limits/Quotas

| Limit | Value |
|---|---|
| Policy stores per region | 10 |
| Policies per store | 10,000 |
| Schema size | 160 KB |
| IsAuthorized requests | 1,000 TPS per store |
| BatchIsAuthorized | 30 requests per batch |
| Cedar policy size | 10 KB per policy |

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Not a replacement for IAM** | Complements IAM — IAM for AWS, VP for your app |
| **Cedar ≠ IAM JSON** | Different language, different evaluation engine |
| **Cognito integration** | Primary identity source — maps user pool groups to Cedar principals |
| **No agents/sidecars** | Pure API call — your app calls `IsAuthorized` |
| **Audit via CloudTrail** | All authorization decisions logged |
| **Schema is optional but recommended** | Validates policies against your entity model |
| **Default deny** | Like IAM — no matching permit = denied |

## When to Use (Exam Decision)

| Scenario | Answer |
|---|---|
| "Control who can call AWS APIs" | **IAM** |
| "Fine-grained app permissions per user per document" | **Verified Permissions** |
| "Multi-tenant SaaS authorization" | **Verified Permissions** |
| "Role-based access within your application" | **Verified Permissions** |
| "Restrict which AWS services an account can use" | **SCP** |
| "Dynamic access based on resource tags" | **ABAC (IAM)** |

## K8s Mapping

```
Verified Permissions  ≈  OPA (Open Policy Agent) for app-level decisions
Cedar policies        ≈  Rego rules
Policy store          ≈  OPA bundle / policy repository
IsAuthorized API      ≈  OPA REST API query (/v1/data)
Schema                ≈  OPA input schema validation
Cognito + VP          ≈  Dex/OIDC + OPA sidecar
```

## 🧠 Cheat-Sheet One-Liners

- **IAM = AWS API access. Verified Permissions = your app's access.** Different layers, complement each other.
- **Cedar = policy language. IsAuthorized = runtime API call.** Your app asks, VP answers.
- **Exam signal:** "fine-grained application permissions" / "multi-tenant" / "per-document access" → Verified Permissions.
