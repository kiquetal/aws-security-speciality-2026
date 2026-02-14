# IAM Policy Examples

This document provides real-world examples of every IAM policy type mentioned in the IAM overview, following AWS security best practices.

---

## 1. Identity-Based Policies

Attached to IAM users, groups, or roles. These define what actions the identity can perform.

### Example 1.1: S3 Read-Only Access (Least Privilege)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadOnlyForSpecificBucket",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-secure-bucket",
        "arn:aws:s3:::my-secure-bucket/*"
      ],
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        }
      }
    }
  ]
}
```

**Key Points:**
- Specific actions only (no wildcards)
- Scoped to a single bucket
- IP restriction for additional security

### Example 1.2: EC2 Instance Management with MFA

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowEC2ReadOperations",
      "Effect": "Allow",
      "Action": [
        "ec2:Describe*",
        "ec2:GetConsole*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowEC2WriteOperationsWithMFA",
      "Effect": "Allow",
      "Action": [
        "ec2:StartInstances",
        "ec2:StopInstances",
        "ec2:RebootInstances"
      ],
      "Resource": "arn:aws:ec2:us-east-1:123456789012:instance/*",
      "Condition": {
        "BoolIfExists": {
          "aws:MultiFactorAuthPresent": "true"
        },
        "StringEquals": {
          "aws:RequestedRegion": "us-east-1"
        }
      }
    },
    {
      "Sid": "DenyEC2TerminationAlways",
      "Effect": "Deny",
      "Action": "ec2:TerminateInstances",
      "Resource": "*"
    }
  ]
}
```

**Key Points:**
- Read operations allowed without MFA
- Write operations require MFA
- Explicit deny for termination (cannot be overridden)
- Region restriction

---

## 2. Resource-Based Policies

Attached directly to AWS resources. Define who can access the resource.

### Example 2.1: S3 Bucket Policy (Cross-Account Access)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCrossAccountReadFromAuditAccount",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::999999999999:role/AuditRole"
      },
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-logs-bucket",
        "arn:aws:s3:::my-logs-bucket/*"
      ],
      "Condition": {
        "StringEquals": {
          "s3:x-amz-server-side-encryption": "aws:kms"
        },
        "Bool": {
          "aws:SecureTransport": "true"
        }
      }
    },
    {
      "Sid": "DenyUnencryptedObjectUploads",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::my-logs-bucket/*",
      "Condition": {
        "StringNotEquals": {
          "s3:x-amz-server-side-encryption": "aws:kms"
        }
      }
    },
    {
      "Sid": "DenyInsecureTransport",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::my-logs-bucket",
        "arn:aws:s3:::my-logs-bucket/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

**Key Points:**
- Specific principal (no wildcards in Allow statements)
- Enforces encryption at rest (KMS)
- Enforces encryption in transit (TLS)
- Deny statements use `"Principal": "*"` for enforcement

### Example 2.2: KMS Key Policy

```json
{
  "Version": "2012-10-17",
  "Id": "key-policy-1",
  "Statement": [
    {
      "Sid": "Enable IAM User Permissions",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:root"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "AllowS3ServiceToUseKey",
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "s3.us-east-1.amazonaws.com",
          "kms:CallerAccount": "123456789012"
        }
      }
    },
    {
      "Sid": "AllowApplicationRoleToEncryptDecrypt",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/ApplicationRole"
      },
      "Action": [
        "kms:Decrypt",
        "kms:DescribeKey"
      ],
      "Resource": "*"
    }
  ]
}
```

**Key Points:**
- Root account statement enables IAM policies to work
- Service principal scoped with `kms:ViaService`
- Separate permissions for different use cases

### Example 2.3: Lambda Function Resource Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3InvocationFromSpecificBucket",
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:ProcessUploads",
      "Condition": {
        "StringEquals": {
          "AWS:SourceAccount": "123456789012"
        },
        "ArnLike": {
          "AWS:SourceArn": "arn:aws:s3:::my-upload-bucket"
        }
      }
    }
  ]
}
```

**Key Points:**
- Service principal with source account validation
- Prevents confused deputy problem with `AWS:SourceArn`

---

## 3. Permission Boundaries

Set the maximum permissions an identity can have, even if their identity-based policy grants more.

### Example 3.1: Developer Permission Boundary

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowedServices",
      "Effect": "Allow",
      "Action": [
        "s3:*",
        "dynamodb:*",
        "lambda:*",
        "logs:*",
        "cloudwatch:*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowIAMReadOnly",
      "Effect": "Allow",
      "Action": [
        "iam:Get*",
        "iam:List*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenyIAMUserManagement",
      "Effect": "Deny",
      "Action": [
        "iam:CreateUser",
        "iam:DeleteUser",
        "iam:CreateAccessKey",
        "iam:DeleteAccessKey"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenyLeavingBoundary",
      "Effect": "Deny",
      "Action": [
        "iam:DeleteUserPermissionsBoundary",
        "iam:DeleteRolePermissionsBoundary"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenyRegionRestriction",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": [
            "us-east-1",
            "us-west-2"
          ]
        }
      }
    }
  ]
}
```

**Key Points:**
- Limits services developers can use
- Prevents privilege escalation by denying boundary removal
- Enforces regional restrictions
- Even if identity policy grants more, boundary limits it

### Example 3.2: Third-Party Contractor Boundary

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowReadOnlyAccess",
      "Effect": "Allow",
      "Action": [
        "s3:Get*",
        "s3:List*",
        "ec2:Describe*",
        "rds:Describe*",
        "cloudwatch:Get*",
        "cloudwatch:List*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenyAllWriteOperations",
      "Effect": "Deny",
      "Action": [
        "s3:Put*",
        "s3:Delete*",
        "ec2:Create*",
        "ec2:Delete*",
        "ec2:Modify*",
        "rds:Create*",
        "rds:Delete*",
        "rds:Modify*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenyIAMAccess",
      "Effect": "Deny",
      "Action": "iam:*",
      "Resource": "*"
    }
  ]
}
```

**Key Points:**
- Read-only boundary for external contractors
- Explicit deny on all write operations
- Complete IAM lockout

---

## 4. Service Control Policies (SCPs)

Organization-level guardrails that apply to all accounts in an OU. SCPs do NOT grant permissions; they set boundaries.

### Example 4.1: Deny Root User Actions

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyRootUserActions",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "aws:PrincipalArn": "arn:aws:iam::*:root"
        }
      }
    }
  ]
}
```

**Key Points:**
- Prevents root user usage across all accounts
- Critical for compliance (CIS AWS Foundations Benchmark)

### Example 4.2: Enforce Encryption and Region Restrictions

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyUnencryptedS3Uploads",
      "Effect": "Deny",
      "Action": "s3:PutObject",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "s3:x-amz-server-side-encryption": [
            "aws:kms",
            "AES256"
          ]
        }
      }
    },
    {
      "Sid": "DenyUnencryptedEBSVolumes",
      "Effect": "Deny",
      "Action": [
        "ec2:RunInstances",
        "ec2:CreateVolume"
      ],
      "Resource": "arn:aws:ec2:*:*:volume/*",
      "Condition": {
        "Bool": {
          "ec2:Encrypted": "false"
        }
      }
    },
    {
      "Sid": "RestrictRegions",
      "Effect": "Deny",
      "NotAction": [
        "iam:*",
        "organizations:*",
        "route53:*",
        "cloudfront:*",
        "support:*",
        "budgets:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": [
            "us-east-1",
            "us-west-2",
            "eu-west-1"
          ]
        }
      }
    }
  ]
}
```

**Key Points:**
- Enforces encryption organization-wide
- Regional restrictions (data residency compliance)
- Uses `NotAction` for global services (IAM, CloudFront, etc.)

### Example 4.3: Prevent Security Service Disablement

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyDisablingSecurityServices",
      "Effect": "Deny",
      "Action": [
        "guardduty:DeleteDetector",
        "guardduty:DisassociateFromMasterAccount",
        "guardduty:StopMonitoringMembers",
        "securityhub:DisableSecurityHub",
        "securityhub:DisassociateFromMasterAccount",
        "config:DeleteConfigurationRecorder",
        "config:DeleteDeliveryChannel",
        "config:StopConfigurationRecorder",
        "cloudtrail:StopLogging",
        "cloudtrail:DeleteTrail"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenyCloudTrailLogDeletion",
      "Effect": "Deny",
      "Action": [
        "s3:DeleteObject",
        "s3:DeleteObjectVersion"
      ],
      "Resource": "arn:aws:s3:::*-cloudtrail-logs/*"
    }
  ]
}
```

**Key Points:**
- Prevents disabling GuardDuty, Security Hub, Config, CloudTrail
- Protects audit logs from deletion
- Critical for compliance and forensics

### Example 4.4: Allow List SCP (Explicit Allow Pattern)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOnlyApprovedServices",
      "Effect": "Allow",
      "Action": [
        "s3:*",
        "ec2:*",
        "rds:*",
        "lambda:*",
        "dynamodb:*",
        "cloudwatch:*",
        "logs:*",
        "kms:*",
        "iam:*",
        "sts:*"
      ],
      "Resource": "*"
    }
  ]
}
```

**Key Points:**
- Whitelist approach (more restrictive)
- Only listed services can be used
- Requires careful maintenance

---

## 5. Trust Policies (AssumeRole Policies)

Define who can assume an IAM role. Attached to roles, not identities.

### Example 5.1: Cross-Account Access Trust Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAssumeRoleFromAuditAccount",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::999999999999:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "unique-external-id-12345"
        },
        "IpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        }
      }
    }
  ]
}
```

**Key Points:**
- External ID prevents confused deputy attacks
- IP restriction for additional security
- Specific account principal (not wildcard)

### Example 5.2: Service Role Trust Policy (EC2)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowEC2ServiceToAssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        }
      }
    }
  ]
}
```

**Key Points:**
- Service principal for EC2 instances
- Source account validation

### Example 5.3: Federated Identity Trust Policy (OIDC)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowGitHubActionsAssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::123456789012:oidc-provider/token.actions.githubusercontent.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
        },
        "StringLike": {
          "token.actions.githubusercontent.com:sub": "repo:my-org/my-repo:*"
        }
      }
    }
  ]
}
```

**Key Points:**
- OIDC federation for GitHub Actions
- Scoped to specific repository
- No long-term credentials needed

### Example 5.4: SAML Federation Trust Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSAMLFederationAssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::123456789012:saml-provider/MyCompanyIdP"
      },
      "Action": "sts:AssumeRoleWithSAML",
      "Condition": {
        "StringEquals": {
          "SAML:aud": "https://signin.aws.amazon.com/saml"
        }
      }
    }
  ]
}
```

**Key Points:**
- SAML 2.0 federation for corporate SSO
- Validates SAML audience

---

## 6. Resource Control Policies (RCPs)

**Note:** RCPs are a newer feature in AWS Organizations that provide resource-level guardrails.

### Example 6.1: Prevent Resource Sharing Outside Organization

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PreventExternalResourceSharing",
      "Effect": "Deny",
      "Principal": "*",
      "Action": [
        "ram:CreateResourceShare",
        "ram:UpdateResourceShare"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEqualsIfExists": {
          "ram:RequestedResourceType": [
            "route53resolver:ResolverRule",
            "ec2:TransitGateway"
          ]
        },
        "Bool": {
          "ram:RequestedAllowsExternalPrincipals": "true"
        }
      }
    }
  ]
}
```

**Key Points:**
- Prevents sharing resources outside the organization
- Allows specific resource types if needed
- Complements SCPs for resource-level control

---

## Policy Evaluation Logic

When multiple policies apply, AWS evaluates them in this order:

1. **Explicit Deny** (in any policy) → Access denied
2. **SCP Deny** → Access denied
3. **Permission Boundary Deny** → Access denied
4. **Explicit Allow** (in identity-based or resource-based policy) → Access allowed
5. **Default** → Access denied (implicit deny)

### Key Principle: "Deny Always Wins"

---

## Best Practices Summary

1. **Use specific ARNs** instead of `"Resource": "*"` whenever possible
2. **Add conditions** to limit scope (IP, MFA, time, encryption)
3. **Explicit denies** for critical protections (cannot be overridden)
4. **Least privilege**: Start with minimal permissions, add as needed
5. **Use IAM Access Analyzer** to validate policies before deployment
6. **Tag resources** and use tag-based conditions for dynamic access control
7. **Separate read and write** permissions with different conditions
8. **Always validate** with `aws iam simulate-principal-policy` or `simulate-custom-policy`

---

## Testing Your Policies

Use AWS IAM Policy Simulator or CLI:

```bash
# Test if a user can perform an action
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:user/testuser \
  --action-names s3:GetObject \
  --resource-arns arn:aws:s3:::my-bucket/file.txt

# Test a custom policy
aws iam simulate-custom-policy \
  --policy-input-list file://policy.json \
  --action-names ec2:RunInstances \
  --resource-arns arn:aws:ec2:us-east-1:123456789012:instance/*
```

---

## Common Exam Scenarios

1. **Cross-account access**: Use trust policy + identity-based policy
2. **Prevent privilege escalation**: Use permission boundaries
3. **Organization-wide enforcement**: Use SCPs with explicit denies
4. **Confused deputy**: Use `aws:SourceAccount` and `aws:SourceArn` conditions
5. **Encryption enforcement**: Deny unencrypted operations in SCPs
6. **Regional restrictions**: Use `aws:RequestedRegion` condition
7. **MFA enforcement**: Use `aws:MultiFactorAuthPresent` condition

