# Study Notes: KMS Cross-Account Decryption Patterns

## Key Concepts
When an identity in Account A needs to decrypt a resource (e.g., an S3 object) in Account B encrypted with a Customer Managed Key (CMK) owned by Account B:

1. **Key Policy (Account B)**:
   - Must explicitly grant the external Account A root ARN or specific role/user ARN permissions to use the key: `kms:Decrypt`, `kms:DescribeKey`.
   
2. **IAM Policy (Account A)**:
   - The caller's IAM role/user in Account A must also have IAM permissions to call `kms:Decrypt` targeting the key's ARN in Account B.

3. **Key Types**:
   - AWS Managed Keys (e.g., `aws/s3`) **cannot** be used for cross-account access because their key policies cannot be modified to grant external access. Always use Customer Managed Keys (CMKs) for cross-account workflows.
