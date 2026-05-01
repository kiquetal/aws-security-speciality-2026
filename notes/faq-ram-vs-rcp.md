# FAQ: RAM vs RCP — Sharing vs Restricting

> **Blueprint refs:** Task 6.2 (cross-account resource sharing), Task 6.1 (org policy management)
> **Purpose:** These solve opposite problems on different services. Don't confuse them.

## One-Liner

```
RAM = "Let Account B use my Transit Gateway"     → SHARES access
RCP = "Block everyone outside my org from my S3"  → RESTRICTS access
```

## Side-by-Side

| Dimension | RAM | RCP |
|---|---|---|
| **Purpose** | Share resources across accounts | Restrict access to resources |
| **Grants access?** | ✅ Yes | ❌ Never — only restricts |
| **Service types** | Infrastructure (networking, compute) | Data (storage, encryption, secrets) |
| **Where it lives** | Per-account resource shares | AWS Organizations policy |
| **Who sets it** | Resource owner | Org admin |
| **Scope** | Specific resources → specific accounts | Org-wide ceiling on all callers |
| **How it works** | API/CLI creates a resource share | JSON Deny policy attached to root/OU/account |

## Services They Support (Almost Zero Overlap)

```
RAM (infrastructure sharing):          RCP (data protection):
├── Transit Gateways                   ├── S3
├── Subnets                            ├── KMS
├── Route 53 Resolver rules            ├── STS
├── DNS Firewall rule groups           ├── SQS
├── License Manager                    ├── Secrets Manager
├── Aurora DB clusters                 ├── DynamoDB
├── CodeBuild projects                 ├── ECR
├── EC2 Image Builder                  ├── CloudWatch Logs
└── etc.                               └── Cognito

OVERLAP: none
```

## RAM Examples (CLI — RAM uses API calls, not JSON policies)

### Example 1: Share a Transit Gateway with Another Account

```bash
# Account A (owner) shares Transit Gateway with Account B
aws ram create-resource-share \
  --name "shared-transit-gateway" \
  --resource-arns "arn:aws:ec2:us-east-1:111111111111:transit-gateway/tgw-abc123" \
  --principals "222222222222"
```

Account B then accepts the share:
```bash
# Account B accepts the invitation
aws ram accept-resource-share-invitation \
  --resource-share-invitation-arn "arn:aws:ram:us-east-1:111111111111:resource-share-invitation/12345"
```

### Example 2: Share DNS Firewall Rule Group Across Org

```bash
# Security account shares DNS Firewall rules with entire org
aws ram create-resource-share \
  --name "org-dns-firewall-rules" \
  --resource-arns "arn:aws:route53resolver:us-east-1:111111111111:firewall-rule-group/rslvr-frg-abc123" \
  --principals "arn:aws:organizations::111111111111:organization/o-abc123" \
  --permission-arns "arn:aws:ram::aws:permission/AmazonRoute53ResolverFirewallRuleGroupAssociation"
```

### Example 3: Share Subnet (Shared VPC Pattern)

```bash
# Networking account shares subnets with workload accounts
aws ram create-resource-share \
  --name "shared-vpc-subnets" \
  --resource-arns \
    "arn:aws:ec2:us-east-1:111111111111:subnet/subnet-aaa" \
    "arn:aws:ec2:us-east-1:111111111111:subnet/subnet-bbb" \
  --principals "arn:aws:organizations::111111111111:ou/o-abc123/ou-xyz789"
```

## RCP Examples (JSON — attached in AWS Organizations)

### Example 1: Block External S3 Access

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyExternalS3Access",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "*",
      "Condition": {
        "StringNotEqualsIfExists": {
          "aws:PrincipalOrgID": "o-abc123"
        },
        "BoolIfExists": {
          "aws:PrincipalIsAWSService": "false"
        }
      }
    }
  ]
}
```

### Example 2: Block External KMS Usage

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyExternalKMSUsage",
      "Effect": "Deny",
      "Principal": "*",
      "Action": [
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:GenerateDataKey",
        "kms:ReEncryptFrom",
        "kms:ReEncryptTo"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEqualsIfExists": {
          "aws:PrincipalOrgID": "o-abc123"
        },
        "BoolIfExists": {
          "aws:PrincipalIsAWSService": "false"
        }
      }
    }
  ]
}
```

## How They Work Together (Exam Scenario)

```
"Share a Transit Gateway with dev accounts AND
 ensure no S3 bucket can be accessed outside the org"

  Step 1: RAM — share Transit Gateway with dev OU
    aws ram create-resource-share \
      --name "dev-tgw" \
      --resource-arns "arn:aws:ec2:...:transit-gateway/tgw-abc" \
      --principals "arn:aws:organizations::...:ou/.../ou-dev"

  Step 2: RCP — block external S3 access org-wide
    Attach Deny policy to org root:
    "Deny s3:* if PrincipalOrgID ≠ my-org AND PrincipalIsAWSService = false"

  RAM opens access to infrastructure.
  RCP closes access to data.
  They complement each other.
```

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **RAM doesn't support KMS** | Use KMS Grants for cross-account key access |
| **RAM doesn't support S3** | Use bucket policies for cross-account S3 access |
| **RCP doesn't support EC2, Lambda, RDS** | Use SCPs or resource policies instead |
| **RAM can be restricted by SCPs** | SCP can deny `ram:CreateResourceShare` with external principals |
| **RAM within org = auto-accept** | No invitation needed if sharing within same org |
| **RAM outside org = invitation** | Recipient must accept the resource share invitation |
| **RCP affects external callers** | RAM shares don't bypass RCPs — if RCP denies, access is denied |
