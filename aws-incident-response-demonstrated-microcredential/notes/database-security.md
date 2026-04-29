# Database Security (RDS)

## RDS Security Controls

### Network Level
- Deploy RDS in **private subnets** — never public-facing
- Use **Security Groups** to restrict access to application tier only
- **Config rule**: `rds-instance-public-access-check` to detect public instances
- Disable public accessibility: `PubliclyAccessible: false`

### Encryption
- **At rest**: Enable encryption using KMS (must be set at creation time — cannot encrypt existing unencrypted DB)
- **In transit**: Use SSL/TLS connections (enforce with `rds.force_ssl` parameter)
- **Snapshots**: Encrypted DB → encrypted snapshots automatically
- To encrypt an unencrypted DB: snapshot → copy snapshot with encryption → restore from encrypted snapshot

### Authentication
- **IAM database authentication** — use IAM roles/users instead of DB passwords
  - Generates temporary auth tokens (15-minute lifetime)
  - Works with MySQL and PostgreSQL
  - Network traffic encrypted with SSL
- **Master user credentials** — store in Secrets Manager with automatic rotation

### Monitoring and Audit
- **CloudWatch metrics** — CPU, connections, storage, read/write latency
- **Enhanced Monitoring** — OS-level metrics (requires agent)
- **RDS Event Subscriptions** — SNS notifications for DB events (failover, configuration changes)
- **Database Activity Streams** — near real-time stream of DB activity to Kinesis (for Aurora)
- **Audit logs** — enable DB-engine-specific audit logging, send to CloudWatch Logs

## Incident Response for RDS

### Compromised Database

1. **Identify** — CloudTrail for API calls, CloudWatch for unusual metrics (spike in connections, CPU)
2. **Contain** — Restrict Security Group to block unauthorized access
3. **Preserve** — Create a **manual snapshot** before any changes
4. **Investigate** — Review audit logs, check for unauthorized data access
5. **Eradicate** — Rotate master credentials, revoke IAM auth tokens, review DB users
6. **Recover** — Restore from a known-good snapshot if data integrity is compromised

### Key Exam Patterns

- **Data exfiltration via public RDS**: Config detects → Lambda remediates by disabling public access
- **Credential compromise**: Rotate master password via Secrets Manager, force SSL, review IAM auth policies
- **Unauthorized access**: VPC Flow Logs + RDS audit logs to trace the source
