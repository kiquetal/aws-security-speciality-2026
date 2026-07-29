# Study Notes: Cognito Advanced Auth Patterns

## Key Concepts

1. **User Pools vs. Identity Pools**:
   - **User Pools**: Directory of users providing Sign-up, Sign-in, and Token issuance (JWTs).
   - **Identity Pools (Federated Identities)**: Exchange federation tokens or Cognito User Pool tokens for temporary, limited-privilege AWS credentials (IAM credentials).

2. **Developer-Authenticated Identities**:
   - Allows registers / sign-ins using custom server auth flows without relying directly on client-side federation.

3. **Cognito Security**:
   - **Advanced Security Features (ASF)**: Provides adaptive authentication (MFA challenge on unusual sign-in) and compromised credentials checks.
   - Use **Cognito User Pool Lambda Triggers** (e.g., Pre-sign-up, Custom Message, Pre-token-generation) to inject security validation logic into the auth pipeline.
