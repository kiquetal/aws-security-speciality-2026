# FAQ: IAM Identity Center (formerly AWS SSO)

> **Blueprint refs:** Task 4.1 (authentication strategies)
> **Exam weight:** High — "recommended front door" into AWS for workforce

## One-Liner

**Centralized SSO for employees across multiple AWS accounts. Temporary credentials, no IAM users needed.**

## Identity Center vs Cognito vs IAM Users

| Dimension | IAM Identity Center | Cognito | IAM Users |
|---|---|---|---|
| **Who** | Employees (workforce) | App users (customers) | Legacy — avoid |
| **Credentials** | Temporary (permission sets → roles) | JWT tokens + optional temp creds | Long-term access keys |
| **Multi-account** | ✅ Built-in | ❌ Not designed for this | ❌ Per-account |
| **SSO** | ✅ Console + CLI + apps | ❌ Not for AWS console | ❌ No |
| **Exam signal** | "workforce" / "employees" / "SSO" | "customer-facing" / "mobile" / "sign-up" | "migrate away from" |

## Identity Sources (Only ONE at a time)

| Source | When to Use |
|---|---|
| **Built-in directory** | Small orgs, no existing IdP |
| **Microsoft Active Directory** | On-prem AD via Managed AD or AD Connector |
| **External IdP (SAML 2.0)** | Okta, Entra ID, OneLogin, PingFederate |

> ⚠️ **Only ONE identity source active at a time.** Can switch, but not multiple simultaneously.
> ⚠️ **Cognito is NOT a supported identity source** for Identity Center.

## How Permission Sets Work

```
Admin creates Permission Set (e.g., "ReadOnlyAccess")
  → Assigns it to User/Group + Account(s)
  → Identity Center auto-creates an IAM role in each target account
  → User signs in → picks account + permission set → assumes the role
  → Gets temporary credentials (no long-term keys)
```

**Permission sets can contain:**
- AWS managed policies (e.g., `ViewOnlyAccess`)
- Customer managed policies
- Inline policy
- Permission boundary

## Key Limits/Quotas

| Limit | Value |
|---|---|
| Identity Center instances per org | 1 |
| Permission sets per account | 50 |
| Permission sets total | 2,000 |
| Session duration | 1–12 hours (default 1hr) |
| Identity source | Only 1 at a time |

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **One instance per org** | Can't have multiple Identity Center instances |
| **Cognito NOT supported as source** | Different service, different audience |
| **Permission sets = IAM roles** | Identity Center creates/manages the roles for you |
| **Requires Organizations** | Must have AWS Organizations with all features enabled |
| **Delegated admin supported** | Don't run in management account — delegate to security account |
| **SCIM provisioning** | Auto-sync users/groups from Okta, Entra ID, OneLogin |
| **MFA support** | FIDO2, TOTP, built-in — enforce for all users |
| **No IAM users created** | Identity Center has its own identity store — separate from IAM |
| **CLI access** | `aws configure sso` — temporary credentials, no access keys stored |

## Integration with ABAC

Identity Center supports **session tags** from your IdP:
- IdP sends attributes in SAML assertion
- Identity Center maps them to session tags
- ABAC policies evaluate against `aws:PrincipalTag/Key`

**Exam signal:** "Federated workforce users need tag-based access" → Identity Center + ABAC

## K8s Mapping

```
IAM Identity Center  ≈  Dex/OIDC federation for kubectl access
Permission sets      ≈  ClusterRoles bound per namespace/cluster
SSO portal           ≈  Kubernetes dashboard with OIDC login
SCIM provisioning    ≈  Syncing LDAP groups to K8s RBAC bindings
```

## 🧠 Cheat-Sheet One-Liners

- **Identity Center = workforce SSO. Cognito = customer apps.** Never mix them.
- **Permission set = IAM role auto-created in target accounts.** No manual role management.
- **Only ONE identity source at a time.** Built-in OR AD OR external IdP — pick one.
