# Study Notes: S3 Data Perimeter Configurations

## Key Concepts
Data perimeters are set of controls to ensure only your trusted identities can access your trusted resources from your trusted networks.

1. **Restricting Access to Trusted Orgs**:
   - Use `aws:PrincipalOrgID` in S3 Bucket Policies to deny access to any principal outside your AWS Organization.
   - Use `aws:ResourceOrgID` in IAM Policies / SCPs to prevent your users from writing data to S3 buckets belonging to external organizations.

2. **Network Controls**:
   - Restrict access to S3 endpoints using `aws:SourceVpce` (VPC Endpoint ID) or `aws:SourceVpc` (VPC ID) to ensure data cannot be exfiltrated to the public internet.
   - Combine with VPC Endpoint policies restricting which buckets can be accessed through the endpoint.
