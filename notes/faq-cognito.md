# FAQ: Amazon Cognito

## Security Use Cases

### User Authentication
- **First-factor authenticators**: Username/password, email OTP, SMS OTP, WebAuthn passkeys
- **MFA options**: Email OTP, SMS OTP, TOTP authenticators
- **Custom authentication flows**: Use Lambda for third-party or bespoke authenticators
- **Compromised credentials checking**: Automatic detection on sign-up, sign-in, password change

### User Pools (User Management)
- Tenant-based user directory for web/mobile apps
- Secure storage of user profile attributes
- Custom schema support for app-specific attributes
- Email and phone number verification before access
- Password policies: length, complexity, history requirements

### Identity Pools (Federated Access)
- Authenticate via external IdP, get temporary AWS credentials
- Access AWS resources (S3, DynamoDB) with role-based permissions
- Supports: Amazon, Facebook, Twitter, Apple, Google, OIDC, SAML, Cognito user pools
- Unauthenticated (guest) access with limited IAM role

### Access Control
- **IAM roles**: Define permissions for authenticated and unauthenticated users
- **Group-based IAM roles**: Assign roles based on Cognito user pool groups
- **Fine-grained access**: Use Cognito ID in IAM policies (e.g., S3 bucket per-user folders)
- **Token-based**: OAuth 2.0 and OIDC tokens for API authorization

### Data Synchronization
- Cognito Sync: Key/value store linked to Cognito identity
- Data synced across user's devices
- No limit on number of identities
- Each identity has separate data store

## Key Limits/Quotas

### User Pools
- No explicit user limit mentioned - scales to millions
- Custom attributes: Use OpenID Connect standard attributes or customize
- Aliasing: Users can sign in with email OR phone number

### Identity Pools
- No limit on identities in identity pool
- No limit on sync store size
- Each identity has separate data store
- Unauthenticated identities: Each GetId call creates new identity (cache response!)

### Pricing Model
- **Monthly Active Users (MAUs)**: Charged per MAU, not per operation
- MAU = user with identity operation in calendar month
- Subsequent sessions in same month: no additional charge
- **Free tier**: First 10,000 MAUs (new SKU) or 50,000 MAUs (legacy accounts)
- **SMS charges**: Separate pricing for phone verification and MFA

## Exam Gotchas

### User Pools vs Identity Pools
- **User Pools**: User directory, authentication, sign-up/sign-in
- **Identity Pools**: Credential broker, temporary AWS credentials, federated access
- **Identity Pools don't store user profiles** - only vend credentials
- Can use both together: User pool authenticates, identity pool provides AWS access

### Authentication Flow
1. App authenticates with IdP using provider's SDK
2. IdP returns OIDC token or SAML assertion
3. App passes token to Cognito identity pool
4. Identity pool returns Cognito ID + temporary AWS credentials

### Unauthenticated Access
- Separate IAM role for guest users
- Limited permissions for unauthenticated access
- Removes friction of login screen
- Still uses temporary, limited-privilege credentials

### Device Management
- Remember devices for users
- Suppress MFA for remembered devices (adaptive authentication)
- Separate identities on shared devices (e.g., family iPad)

### User Migration
- **Just-in-time (JIT)**: Lambda trigger migrates users on first sign-in (no password reset)
- **Bulk migration**: Upload CSV file, users verify on first sign-in
- Retain existing passwords with JIT migration

### Custom Workflows (Lambda Triggers)
- **Pre-registration**: Fraud detection, custom validation
- **Post-confirmation**: Welcome email, analytics
- **Pre-authentication**: Additional checks before auth
- **During authentication**: Custom challenge/response
- **Post-authentication**: Logging, analytics
- **Custom messages**: Email/SMS verification, MFA messages

### Cognito vs IAM Identity Center
- **Cognito**: Customer-facing apps (B2C, B2B)
- **IAM Identity Center**: Workforce identities (employees)
- Cognito **NOT supported** as identity source for IAM Identity Center

### Token Handling
- Cognito doesn't receive/store IdP credentials
- Cognito doesn't receive confidential info (email, friends list) from IdP
- Uses one-way hash of IdP token for user identification

### Identity Counting
- **Authenticated identities**: One identity per user (GetId called once)
- **Unauthenticated identities**: New identity per GetId call (cache response!)
- Mobile SDK caches automatically

## Best Practices for IAM Policies

1. **Use separate IAM roles** for authenticated vs unauthenticated users
2. **Least privilege for guest access** - minimal permissions
3. **Condition keys**: `cognito-identity.amazonaws.com:sub` (Cognito ID)
4. **Per-user resource access**: Use `${cognito-identity.amazonaws.com:sub}` in policies
5. **Group-based roles**: Assign IAM roles based on Cognito user pool groups
6. **Token validation**: Always validate JWT tokens in backend
7. **Secure token storage**: Never store tokens in localStorage (use httpOnly cookies)
8. **Refresh tokens**: Implement proper token refresh logic
9. **Monitor with CloudTrail**: Track Cognito API calls
10. **Enable advanced security**: Compromised credentials detection, adaptive authentication

### Example: S3 Per-User Folder Access
```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::mybucket/${cognito-identity.amazonaws.com:sub}/*"
}
```
