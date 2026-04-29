# Audit and Compliance Controls

## CloudTrail

### What it captures
- **Management events** — API calls that modify resources (enabled by default)
- **Data events** — S3 object-level operations, Lambda invocations (must be explicitly enabled)
- **Insights events** — unusual API activity patterns

### Key exam points
- CloudTrail delivers logs to S3 with ~15 minute delay
- Enable **log file validation** to detect tampering (SHA-256 digest files)
- Use **Organization trails** to capture events across all accounts
- CloudTrail logs are **encrypted by default** with SSE-S3; use SSE-KMS for additional control
- **Quotas**: 5 trails per region, but Organization trails count as 1 in each member account

## Athena for Log Analysis

### Why Athena?
- Query CloudTrail logs directly in S3 using SQL
- No infrastructure to manage — serverless
- Pay per query (data scanned)

### Common incident response queries
- Find all API calls by a specific IAM user/role
- Identify `PutBucketPolicy` calls that made buckets public
- Trace `CreateAccessKey` events for backdoor detection
- Find unauthorized `AssumeRole` calls

### Key exam detail
- Create a **CloudTrail table** in Athena pointing to the S3 bucket
- Partition by date for cost-effective queries
- Use `WHERE` clauses on `eventtime`, `eventsource`, `eventname` for targeted analysis

## AWS Config

### What it does
- Continuously evaluates resource configurations against **rules**
- Records configuration changes over time (configuration timeline)
- Triggers remediation actions for non-compliant resources

### Managed rules relevant to incident response
- `s3-bucket-public-read-prohibited`
- `s3-bucket-public-write-prohibited`
- `iam-user-mfa-enabled`
- `iam-root-account-mfa-enabled`
- `restricted-ssh` (no 0.0.0.0/0 on port 22)
- `vpc-flow-logs-enabled`
- `cloud-trail-enabled`
- `rds-instance-public-access-check`

### Remediation
- **Automatic remediation** — Config triggers SSM Automation or Lambda
- **Manual remediation** — Config flags non-compliant, human reviews

### Key exam detail
- Config rules evaluate on **configuration change** or **periodic schedule**
- Config **must be enabled** per region — it's not on by default
- Config records are stored in S3

## CloudWatch

### Alarms
- Monitor metrics and trigger actions (SNS, Auto Scaling, EC2 actions)
- Use **composite alarms** to combine multiple conditions

### Logs
- Centralize logs from EC2, Lambda, CloudTrail, VPC Flow Logs
- Use **metric filters** to create alarms from log patterns
- **Log Insights** for interactive querying

### Events (EventBridge)
- Always enabled — services emit events automatically
- Create rules to match event patterns and route to targets
- Supports Lambda, Step Functions, SNS, SQS, and more as targets

### Key exam detail
- CloudWatch Logs supports **data masking** for sensitive data (new for SCS-C03)
- VPC Flow Logs can be sent to CloudWatch Logs or S3
- CloudWatch agent required for OS-level metrics and custom logs from EC2
