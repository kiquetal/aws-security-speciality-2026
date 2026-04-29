# Scenario-Based Exercises

## Scenario 1 — Data Exfiltration via Compromised EC2

### Situation

CloudWatch alarms fire showing an unusual spike in S3 `GetObject` requests on a sensitive bucket at 3 AM. VPC Flow Logs show large outbound data transfers from an EC2 instance to an unknown external IP.

You suspect an attacker compromised an EC2 instance and is using it to exfiltrate data from S3.

### Questions

1. What's the **first thing** you do to stop the bleeding?
2. How do you **identify** what the attacker accessed in S3?
3. How do you determine **how** the attacker got access to the EC2 instance in the first place?

### Answers

#### 1 — Containment (two actions)

**EC2 isolation:** Replace the instance's Security Group with an empty SG (no inbound, no outbound). This cuts the exfiltration immediately and preserves volatile evidence.

**S3 bucket lockdown:** Apply a temporary deny-all bucket policy that preserves access only for the security team:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::sensitive-bucket",
        "arn:aws:s3:::sensitive-bucket/*"
      ],
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalArn": "arn:aws:iam::123456789012:role/SecurityTeamRole"
        }
      }
    }
  ]
}
```

**Why lock down S3 too?** Even if the EC2 instance is isolated, the attacker might have the credentials and could access S3 from another location.

**IAM best practice:** Never use a naked `Deny` on `Principal: "*"` without a condition to preserve your own access.

#### 2 — Identify what was accessed (Athena + CloudTrail)

**Prerequisite:** S3 data event logging must be enabled in CloudTrail (not on by default — common exam trap).

When enabled, CloudTrail captures `GetObject`, `PutObject` with the bucket name, full object key, IAM identity, and source IP.

Use **Athena** to query CloudTrail logs in S3:

```sql
SELECT
    eventtime,
    useridentity.arn,
    requestparameters.bucketName,
    requestparameters.key,
    sourceipaddress
FROM cloudtrail_logs
WHERE eventsource = 's3.amazonaws.com'
  AND eventname = 'GetObject'
  AND sourceipaddress = '<suspicious_IP>'
  AND eventtime > '2025-01-15T00:00:00Z'
```

This gives you exactly what objects the attacker downloaded, when, and from which IP.

#### 3 — Determine how the attacker got in (CloudTrail `userIdentity.type`)

The CloudTrail field `userIdentity.type` tells you the attack vector:

| `userIdentity.type` | Meaning | Eradication Steps |
|----------------------|---------|-------------------|
| `AssumedRole` | Attacker used the EC2 instance's IAM role (temporary credentials from instance metadata) | 1. Isolate instance (done) 2. Revoke role's active sessions (inline deny-all with `aws:TokenIssueTime`) 3. Review and tighten role permissions |
| `IAMUser` | Attacker used hardcoded long-term access keys | 1. Delete compromised access keys 2. Audit user policies 3. Revoke sessions 4. Issue new keys 5. Fix the application — stop hardcoding credentials, use instance roles instead |

**Key difference:** With `AssumedRole`, temporary credentials expire automatically once the instance is isolated. With `IAMUser`, credentials **never expire** until you delete them.
