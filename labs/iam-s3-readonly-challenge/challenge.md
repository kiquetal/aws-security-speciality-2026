# Lab Challenge: S3 Read-Only Access with IP Restrictions

## Scenario

You are a Security Engineer at a healthcare company. The compliance team requires that data analysts can only read patient data from a specific S3 bucket, and access must be restricted to the corporate network IP range.

## Business Requirements

1. Data analysts need read-only access to the `patient-data-analytics` S3 bucket
2. Access must be restricted to the corporate office IP range: `198.51.100.0/24`
3. Analysts should be able to:
   - List objects in the bucket
   - Download objects
   - View object versions (versioning is enabled for compliance)
4. Analysts must NOT be able to:
   - Upload new objects
   - Delete objects
   - Modify bucket configuration
   - Access any other S3 buckets

## Technical Requirements

Using Terraform, implement the following:

1. Create an IAM role named `DataAnalystRole`
2. Create an identity-based policy that:
   - Grants read-only access to the `patient-data-analytics` bucket
   - Uses specific actions (no wildcards)
   - Includes an IP-based condition to restrict access to `198.51.100.0/24`
   - Follows the principle of least privilege
3. Attach the policy to the role
4. Create a trust policy that allows EC2 instances to assume this role (analysts will use EC2 workstations)

## Security Constraints

- Do NOT use `s3:*` or `Action: "*"` wildcards
- Do NOT use `"Resource": "*"` for S3 operations
- The policy must explicitly deny access from IPs outside the corporate range
- Follow AWS Well-Architected Framework Security Pillar best practices

## Deliverables

Your Terraform code should create:
- `main.tf` - IAM role and policy resources
- `variables.tf` - Input variables (bucket name, IP range)
- `outputs.tf` - Output the role ARN
- `terraform.tfvars.example` - Example variable values

## Testing Criteria

After deployment, verify:
1. The role can be assumed by an EC2 instance
2. From an IP in `198.51.100.0/24`, the role can list and download objects
3. From an IP outside the range, access is denied
4. The role cannot perform write operations (PutObject, DeleteObject)

## Bonus Challenge (Optional)

Add a second statement to the policy that:
- Allows access to CloudWatch Logs for audit purposes
- Restricts log access to read-only operations
- Does NOT require IP restrictions for CloudWatch (analysts may need to check logs remotely)

---

**Do NOT implement the solution yet.** Review the requirements and ask clarifying questions if needed. When ready, request a review of your approach before coding.
