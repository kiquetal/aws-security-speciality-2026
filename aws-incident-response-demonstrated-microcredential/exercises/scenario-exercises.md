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

## Scenario 2 — Compromised RDS Database

### Situation

CloudWatch alarms detect a sudden spike in `DatabaseConnections` on an RDS MySQL instance at 2 AM. CloudTrail shows a `ModifyDBInstance` call that disabled the `DeletionProtection` flag. RDS audit logs show queries running `SELECT * FROM users` and `SELECT * FROM payment_info` from an unfamiliar IP.

### Questions

1. What are your **immediate containment** steps?
2. The attacker used `ModifyDBInstance` — what does that tell you about **what kind of access** they have?
3. How do you **recover** the database to a known-good state?

### Answers

#### 1 — Containment

Replace the RDS instance's Security Group with an **empty SG** — cuts all network access immediately.

#### 2 — Two levels of access

`ModifyDBInstance` is an **AWS API call**, not a SQL query. The attacker has **two levels of access**:

- **AWS API level** — IAM credentials that allow `rds:ModifyDBInstance`
- **Database level** — MySQL credentials (username/password) to run SQL queries

**Key exam detail:** CloudTrail captures API calls (`ModifyDBInstance`), but **NOT SQL queries**. To see what SQL the attacker ran, you need **RDS audit logging** (engine-specific):

| What you want to see | Where to find it |
|----------------------|-----------------|
| Who called `ModifyDBInstance` | CloudTrail (`userIdentity` field) |
| What SQL queries the attacker ran | RDS audit logs (engine-specific) |
| Connection spikes, CPU anomalies | CloudWatch metrics |
| Real-time activity stream (Aurora only) | Database Activity Streams → Kinesis |

For MySQL: enable `general_log`, `slow_query_log` via DB parameter groups, or use the **MariaDB Audit Plugin**.

Audit logs can be **published to CloudWatch Logs** for analysis and long-term retention.

**Important:** Audit logging must be enabled *before* the incident — without it, you have no record of SQL activity.

#### 3 — Recovery using PITR

The recovery produces **two running instances + one snapshot**:

| # | What | Type | Purpose |
|---|------|------|---------|
| 1 | `compromised-db` | Running instance | Forensic investigation |
| 2 | Manual snapshot | Storage (S3, not a running instance) | Long-term evidence archive |
| 3 | `clean-db-restored` | Running instance | Production recovery |

**Step-by-step:**

1. **Contain** — empty SG on `compromised-db`
2. **Preserve** — create manual snapshot (runs in background, don't wait)
3. **Recover** — immediately run PITR to create a new clean instance:

```bash
aws rds restore-db-instance-to-point-in-time \
  --source-db-instance-identifier compromised-db \
  --target-db-instance-identifier clean-db-restored \
  --restore-time "2025-01-15T02:00:00Z"
```

4. **Harden** the new instance:
   - Restricted SG (least-privilege)
   - DeletionProtection re-enabled
   - Rotate master credentials via Secrets Manager
   - Force SSL connections (`rds.force_ssl` parameter)
   - Review and remove unauthorized DB users
5. **Update** application to point to the new instance endpoint
6. **Eradicate** — revoke the compromised IAM credentials (same pattern as Scenario 1)
7. **Cleanup** — investigate `compromised-db` using audit logs, then delete it. The manual snapshot stays as permanent forensic evidence.

**Snapshot vs PITR — exam distinction:**

| Feature | Manual Snapshot | Point-in-Time Recovery |
|---------|----------------|----------------------|
| What it is | Backup stored in S3 | Restore operation that creates a new instance |
| Granularity | Whenever you trigger it | Any second within retention period (1–35 days) |
| Requires | Nothing | Automated backups enabled (retention > 0) |
| Result | Storage (not a running instance) | New running RDS instance |
| Use in IR | Forensic evidence | Production recovery |

**See diagram:** `diagrams/rds-incident-response-flow.png`
