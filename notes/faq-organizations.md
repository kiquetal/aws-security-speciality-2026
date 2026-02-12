# FAQ: AWS Organizations

## Security Use Cases

### Centralized Governance
- Programmatically create and manage AWS accounts
- Organize accounts into hierarchical Organizational Units (OUs)
- Apply policies centrally across multiple accounts
- Consolidated billing with single payer account (management account)

### Policy Types
1. **Service Control Policies (SCPs)**: Control maximum IAM permissions
   - Affect IAM users, roles, AND root user
   - Don't grant permissions - only restrict
   - Empty SCP = explicit DENY all
2. **Resource Control Policies (RCPs)**: Control maximum resource permissions
3. **Declarative policies**: Enforce baseline configurations, prevent non-compliant actions
4. **Backup policies**: Centrally manage backup plans
5. **Tag policies**: Standardize resource tags
6. **Chatbot policies**: Control chat app access
7. **AI services opt-out policies**: Control AI service data collection

### Account Structure
- **Management account**: Creates organization, ultimate control, payer account
  - Cannot change which account is management account
- **Member accounts**: Can belong to only ONE organization at a time
- **Administrative root**: Top-most container, starting point for hierarchy
- **OUs**: Logical grouping of accounts, can nest up to **5 levels deep**

### Cross-Account Access
- IAM roles with trust policies enable secure cross-account access
- No credential sharing required
- Centralized identity management via IAM Identity Center

## Key Limits/Quotas

### Organizational Structure
- **5 levels deep** for OU nesting (including root and accounts)
- Account can be member of **only ONE OU** at a time
- OU can be member of **only ONE parent OU** at a time
- Number of accounts varies - request increase via AWS Support

### Policy Evaluation
- SCPs evaluated with IAM policies: Effective permission = IAM ∩ SCP
- Policies attached at root apply to ALL accounts
- Policies attached to OU apply to OU and nested OUs
- Policies attached to account apply only to that account

### Account Management
- Accounts created via Organizations can be transferred to new organization
- To make account standalone: must provide contact info, payment method, support plan
- Cannot change management account after creation

## Exam Gotchas

### SCP Behavior
- **Explicit Deny always wins** - cannot be overridden
- SCPs affect **root user** of member accounts (unlike IAM policies)
- Empty SCP = DENY all (not allow all)
- Management account is **NOT affected** by SCPs
- Principals in member account cannot remove/change SCPs

### Policy Inheritance
- Policies inherit down the hierarchy (root → OU → nested OU → account)
- Effective permissions = intersection of all applicable policies
- More restrictive as you go down the hierarchy

### IAM Policy Simulator
- Can test SCP effects on IAM principals
- Available in member accounts with proper Organizations permissions
- Shows if SCP is affecting access

### Organizations vs Control Tower
- **Organizations**: Foundation for multi-account management
- **Control Tower**: Built on Organizations, adds automated setup and guardrails
- Control Tower uses SCPs and RCPs for preventive controls
- Control Tower provides prescriptive guidance and flexible controls

### Declarative Policies vs SCPs
- **Declarative policies**: Simpler, maintain configuration automatically
- **SCPs**: More complex, require manual updates for new APIs
- Declarative policies provide customizable error messages
- Both can be used together for defense in depth

### Account Creation
- New accounts automatically get IAM role with full admin permissions
- Management account can assume this role for access
- Accounts inherit policies from parent OU immediately
- Cannot create account in multiple OUs simultaneously

### Service Integration
- Many AWS services integrate with Organizations
- Enables centralized management across accounts
- Examples: GuardDuty, Security Hub, CloudTrail, Config

### Global vs Regional
- Organizations entities are **globally accessible** (except China)
- No need to specify region for organization management
- Separate organization required for China regions

## Best Practices for SCPs

1. **Start with FullAWSAccess** SCP, then add Deny statements
2. **Test in non-production** OU first
3. **Use Deny statements** for critical security controls:
   - Prevent disabling CloudTrail
   - Prevent leaving organization
   - Prevent deleting VPC Flow Logs
   - Require MFA for sensitive operations
4. **Condition keys**: `aws:RequestedRegion`, `aws:PrincipalOrgID`, `aws:PrincipalOrgPaths`
5. **Document SCP purpose** in description field
6. **Version control** SCPs in git
7. **Monitor with CloudTrail** - track SCP changes
