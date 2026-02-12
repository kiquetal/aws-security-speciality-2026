# FAQ: IAM Identity Center (formerly AWS SSO)

## Security Use Cases

### Centralized Workforce Access
- **Recommended front door** into AWS for workforce users
- Single sign-on to multiple AWS accounts and applications
- Centralized identity management across AWS organization
- Eliminates need for separate credentials per account

### Identity Source Options
- **IAM Identity Center identity store**: Built-in user directory
- **Microsoft Active Directory**: Via AWS Directory Service (AD Connector or Managed AD)
- **External IdP**: Okta, Microsoft Entra ID (Azure AD), OneLogin, PingFederate
- **SAML 2.0 providers**: Any SAML 2.0 compliant IdP
- **Only ONE identity source** can be connected at a time

### Authentication Methods
- **MFA support**: FIDO2 security keys (YubiKey), biometric (Touch ID, facial recognition), TOTP apps
- **RADIUS MFA**: For Active Directory users
- **WebAuthn specification**: For passwordless authentication
- **Social/federated login**: Not supported (use Cognito for customer-facing apps)

### Permission Management
- **Permission sets**: Collections of permissions based on AWS managed policies or custom
- **AWS managed policies for job functions**: Pre-built for common roles
- **ABAC support**: Use attributes from identity store or SAML assertions as tags
- **Automatic IAM role creation**: Identity Center creates roles in accounts automatically
- **No modification of existing IAM**: Doesn't touch existing IAM users/roles/policies

### Access Control
- **Account-level**: Assign users/groups to AWS accounts with permission sets
- **Application-level**: SSO to SAML 2.0 applications
- **OU-based filtering**: Select accounts by organizational unit
- **Trusted identity propagation**: Maintain user identity across AWS analytics services

## Key Limits/Quotas

### Identity Source
- **One instance per account per region** (hard limit)
- Only **one identity source** active at a time (can change, but not multiple simultaneously)
- SCIM synchronization supported: Okta, Entra ID, OneLogin, PingFederate

### Session & Credentials
- **CLI credentials valid for 60 minutes** (can refresh as needed)
- Temporary credentials for all access (no long-term credentials)
- Session tags can be passed from IdP via SAML assertions

### Integration
- **IAM Identity Center-integrated applications**: No additional federation setup needed
- **Pre-integrated SAML apps**: Common business applications pre-configured
- **Custom SAML 2.0 apps**: Use custom application wizard
- **No support for non-SAML apps** (OIDC for applications not supported via SSO)

## Exam Gotchas

### Identity Center vs IAM Users
- **Identity Center**: Workforce identities, temporary credentials, centralized management
- **IAM Users**: Long-term credentials, not recommended for workforce
- Identity Center **doesn't create IAM users/groups** - uses its own identity store
- Existing IAM users/roles continue to work after enabling Identity Center

### Identity Center vs Cognito
- **Identity Center**: Workforce identities (employees, contractors)
- **Cognito**: Customer-facing application identities (app users)
- Cognito is **NOT a supported identity source** for Identity Center

### Active Directory Integration
- **AD Connector**: Proxy to on-premises AD (no caching)
- **AWS Managed Microsoft AD**: Can establish trust with on-premises AD
- **Trust relationship**: Enables hybrid identity scenarios
- AD users authenticate against on-premises AD, not AWS

### Permission Sets
- Applied as IAM roles in target accounts
- Can attach multiple permission sets to same user
- User chooses which permission set to assume in access portal
- Changes to permission sets propagate automatically to all assigned accounts

### SCIM Provisioning
- **Automatic sync**: Okta, Entra ID, OneLogin, PingFederate
- **Manual provisioning**: For other IdPs via console
- Users must be provisioned before assigning permissions
- Group membership synced automatically with SCIM

### Encryption & Data Protection
- **AWS KMS integration**: Encrypt data at rest
- **Customer-managed KMS keys**: Optional for full control
- **TLS 1.2/1.3**: Data encrypted in transit
- **Data signing**: Protects against tampering

### Multi-Account Management
- **AWS Organizations integration**: Required for multi-account access
- **All features must be enabled** in Organizations
- **Delegated administrator**: Can be configured for centralized management
- Findings aggregated to administrator account

### Trusted Identity Propagation
- **Use case**: BI applications querying AWS analytics services (Redshift, QuickSight)
- **Mechanism**: OAuth 2.0 Authorization Framework
- **Benefit**: Single sign-on across multiple analytics applications
- **Granular access**: User and group-level permissions in data sources

## Best Practices for IAM Policies

1. **Use Identity Center for workforce access** - not IAM users
2. **Leverage AWS managed policies** for job functions initially
3. **Refine with custom permission sets** for least privilege
4. **Use ABAC** for scalable, tag-based access control
5. **Enable MFA** for all users (FIDO2 preferred)
6. **Monitor with CloudTrail** - all SSO activity logged
7. **Session tags** for fine-grained, context-aware access
8. **Condition keys**: `identitystore:UserId`, `identitystore:GroupId`
9. **Require Identity Center** for AWS CLI/SDK access (disable long-term credentials)
10. **Automate with APIs** - use CloudFormation for permission set management
