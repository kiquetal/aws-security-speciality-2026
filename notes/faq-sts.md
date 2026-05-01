# FAQ: AWS Security Token Service (STS)

> **Blueprint refs:** Task 4.1 (temporary credentials, authentication strategies), Task 4.2 (authorization strategies)

## Security Use Cases

### Temporary Credentials
- All STS credentials are **short-lived** — no rotation needed
- Consist of: `AccessKeyId`, `SecretAccessKey`, `SessionToken`, `Expiration`
- Used by IAM roles, federation, cross-account access, and Identity Center
- **Always prefer STS over long-term IAM user credentials**

### AssumeRole Variants

| API | Who Uses It | Identity Source | Token Input |
|-----|------------|----------------|-------------|
| `AssumeRole` | IAM users/roles, cross-account | IAM | None (caller already authenticated) |
| `AssumeRoleWithSAML` | Enterprise federation | SAML 2.0 IdP (Okta, ADFS, Entra ID) | SAML assertion |
| `AssumeRoleWithWebIdentity` | Mobile/web apps | OIDC provider (Google, Facebook, Amazon) | OIDC token |
| `GetFederationToken` | IAM users (legacy) | IAM user | None |
| `GetSessionToken` | IAM users needing MFA | IAM user | MFA token code |

### Session Duration Limits

| API | Default | Min | Max |
|-----|---------|-----|-----|
| `AssumeRole` | 1 hour | 15 min | 12 hours (role setting) |
| `AssumeRoleWithSAML` | 1 hour | 15 min | 12 hours |
| `AssumeRoleWithWebIdentity` | 1 hour | 15 min | 12 hours |
| `GetFederationToken` | 12 hours | 15 min | 36 hours |
| `GetSessionToken` | 12 hours | 15 min | 36 hours |

> ⚠️ **Exam gotcha:** `MaxSessionDuration` is set on the **role** (1–12 hours), but the caller requests `DurationSeconds` in the API call. The actual duration = min(requested, role max).

### Cross-Account Access Pattern
1. Account A creates role with trust policy allowing Account B's principal
2. Account B's principal calls `sts:AssumeRole` with the role ARN
3. STS returns temporary credentials scoped to the role's permissions
4. No credential sharing — each account manages its own policies

### Session Policies
- Optional JSON policy passed as parameter in `AssumeRole` call
- **Filters down** the role's permissions for that session only
- Cannot escalate beyond the role's identity policies
- Use case: vend narrower credentials to downstream services
- Effective permissions = role policy ∩ session policy ∩ boundary ∩ SCP

## Key Limits/Quotas

### API Throttling
- `AssumeRole`: **No published default** — scales with account usage
- `GetCallerIdentity`: Very high limit (useful for debugging, cheap to call)
- `GetSessionToken`: Standard limits apply

### Token Size
- **Packed policy size limit**: 2,048 characters (for session policies)
- **AssumeRole response**: Credentials + `AssumedRoleUser` (ARN + `AssumedRoleId`)

### Regional Endpoints
- STS has a **global endpoint** (`sts.amazonaws.com`) — maps to `us-east-1`
- **Regional endpoints recommended** (`sts.eu-west-1.amazonaws.com`) — lower latency, better availability
- **Activate regional endpoints** in IAM console (some disabled by default)
- CloudTrail logs STS calls in the **region of the endpoint used**

> ⚠️ **Exam gotcha:** If regional STS endpoints are not activated and the global endpoint goes down, AssumeRole fails everywhere. Always activate regional endpoints.

## Exam Gotchas

### Confused Deputy Prevention
- **Problem:** Service A assumes a role in your account on behalf of any customer, not just you
- **Solution:** Use `aws:SourceArn` and `aws:SourceAccount` conditions in the trust policy
- **Also use:** `aws:PrincipalOrgID` for org-scoped trust

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowServiceWithConfusedDeputyProtection",
      "Effect": "Allow",
      "Principal": {
        "Service": "guardduty.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:guardduty:us-east-1:123456789012:detector/*"
        }
      }
    }
  ]
}
```

### Trust Policy ≠ Permissions
- Trust policy controls **who can assume** the role
- Identity policy controls **what the role can do**
- Both must be correct — trust without permissions = usable but powerless role

### Role Chaining
- Role A assumes Role B, which assumes Role C
- **Session duration resets to 1 hour max** when chaining (cannot use role's `MaxSessionDuration`)
- Session policies and source identity propagate through the chain
- CloudTrail shows each hop separately

### `GetCallerIdentity`
- **Cannot be denied** by any policy (IAM, SCP, boundary, session)
- Always returns: Account, ARN, UserId
- Use for debugging "who am I?" in scripts
- No permissions required to call it

### Source Identity
- Set during initial `AssumeRole` call via `SourceIdentity` parameter
- **Persists through role chaining** — cannot be changed
- Logged in CloudTrail for audit trail back to original human
- Use `sts:SourceIdentity` condition key to enforce

### `ExternalId` for Third-Party Access
- Random string shared between you and the third party
- Prevents confused deputy when granting cross-account access to vendors
- **Not a secret** — it's a transaction identifier, not authentication
- Set in trust policy condition: `sts:ExternalId`

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowThirdPartyWithExternalId",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "unique-id-assigned-by-vendor-12345"
        }
      }
    }
  ]
}
```

### Revoking Sessions
- **Cannot revoke individual STS tokens** — no invalidation API
- **Revoke all sessions:** Add inline deny policy with `aws:TokenIssueTime` condition
- Denies all sessions issued before a specific timestamp
- New sessions (after the timestamp) work normally

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RevokeAllOlderSessions",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "DateLessThan": {
          "aws:TokenIssueTime": "2025-01-15T12:00:00Z"
        }
      }
    }
  ]
}
```

> ⚠️ **Exam gotcha:** This is the ONLY way to revoke active STS sessions. Deleting the role or removing policies doesn't invalidate already-issued tokens until they expire.

### `AssumeRoleWithWebIdentity` vs Cognito Identity Pools
- **Direct `AssumeRoleWithWebIdentity`:** App calls STS directly with OIDC token
- **Cognito Identity Pools:** Cognito brokers the exchange (recommended)
- Cognito adds: unauthenticated access, identity merging, attribute-based role mapping
- **Exam preference:** Use Cognito Identity Pools over direct STS for mobile/web apps

### S3 Presigned URLs
- Generated using STS temporary credentials (or IAM user credentials)
- **Inherit the permissions of the signer** at time of use (not creation)
- If the role's session expires, presigned URL stops working
- Max expiry: 7 days (SigV4), but limited by credential lifetime
- **Cannot be revoked** — rotate the signing credentials to invalidate

## STS Condition Keys (Exam-Critical)

| Condition Key | Use Case |
|--------------|----------|
| `sts:ExternalId` | Third-party confused deputy prevention |
| `sts:SourceIdentity` | Track original human through role chains |
| `sts:RoleSessionName` | Enforce naming convention for sessions |
| `sts:TransitiveTagKeys` | Control which tags persist through chaining |
| `aws:TokenIssueTime` | Revoke sessions issued before a timestamp |
| `aws:MultiFactorAuthPresent` | Require MFA for AssumeRole |
| `aws:MultiFactorAuthAge` | Require recent MFA (max seconds since auth) |
| `aws:PrincipalOrgID` | Restrict trust to your organization |

## Best Practices

1. **Use regional STS endpoints** — activate in all regions you operate in
2. **Set `MaxSessionDuration`** to minimum needed (don't leave at 12 hours)
3. **Always add confused deputy conditions** in trust policies for AWS services
4. **Use `ExternalId`** for all third-party cross-account roles
5. **Enable `SourceIdentity`** for audit trail through role chains
6. **Prefer Cognito Identity Pools** over direct `AssumeRoleWithWebIdentity`
7. **Monitor with CloudTrail** — all STS API calls are logged
8. **Use session policies** to scope down credentials for downstream consumers
9. **Require MFA** for sensitive AssumeRole operations via `aws:MultiFactorAuthPresent`
10. **Know the revocation pattern** — `aws:TokenIssueTime` deny is the only way
