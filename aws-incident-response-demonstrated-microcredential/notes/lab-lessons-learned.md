# Lessons Learned — Incident Response Microcredential Lab

> Completed: 2026-04-30

## The Attack Chain

```
AttackSimulationRole (instance role)
  ├── Created IAM user: compromised-user
  ├── Launched crypto mining EC2s: WebServer-Backup-1, WebServer-Backup-2
  └── DatabaseExploitFunction created bucket: db-archive-643dac10 (database dump)

compromised-user (from 3 Tor exit nodes)
  ├── Created backdoor user: system-backup-643dac10
  ├── Created backdoor user: app-admin-643dac10
  ├── Created exfiltration bucket: data-backup-643dac10
  └── Uploaded stolen files: financial_transactions.csv, customer_data.csv
```

## Mistakes I Made (Won't Repeat)

### 1. Deleted evidence before preserving it
**What happened:** Deleted the attacker's S3 bucket (`data-backup-643dac10`) before copying files to the forensic bucket.

**Correct order:** Copy to forensic bucket FIRST → then delete attacker's bucket.

**Rule:** Contain → **Preserve** → Eradicate. Never skip preserve.

### 2. Filtered Athena queries by single identity
**What happened:** Queried `WHERE useridentity.arn LIKE '%compromised-user%'` and missed the `db-archive-643dac10` bucket created by `DatabaseExploitFunction`.

**Correct approach:** Filter by **attacker IPs**, not identity. Attackers use multiple identities.

```sql
-- GOOD: catches all identities used by the attacker
WHERE r.sourceipaddress IN ('185.220.101.48', '23.129.64.131', '103.253.145.28', '98.83.113.2', '98.89.27.83')

-- BAD: only catches one identity in the attack chain
WHERE r.useridentity.arn LIKE '%compromised-user%'
```

## Key Skills Practiced

### Athena Queries on CloudTrail

Table had nested `records` array — required UNNEST:

```sql
SELECT DISTINCT r.eventtime, r.eventname, r.useridentity.arn, r.sourceipaddress, r.requestparameters
FROM cloudtrail_events
CROSS JOIN UNNEST(records) AS t(r)
WHERE r.eventname = 'CreateBucket'
ORDER BY r.eventtime DESC
```

### S3 Containment
- `PutPublicAccessBlock` — account-level: S3 → left sidebar → Block Public Access settings for this account
- `PutPublicAccessBlock` — bucket-level: S3 → Bucket → Permissions → Block public access
- Delete versioned bucket: use **Empty** button (handles versions) → then **Delete**

### EC2 Forensics & Containment
- Create AMI before terminating: EC2 → Instance → Actions → Image and templates → Create image
- Isolate: Actions → Security → Change security groups → empty SG
- Enforce IMDSv2: Actions → Instance settings → Modify instance metadata options → V2 required, hop limit 1

### Launch Template Hardening
- Modify template creates a **new version** (same template ID)
- Must set new version as **default**
- Instance refresh replaces running instances with new template version
- Auto Scaling groups → Instance management → Start instance refresh

### NACL Rules
- Evaluated by **lowest rule number first**
- To block before an allow at rule 100, use rule 50/51/52
- Always use `/32` for single IP blocks

### RDS Hardening
- Publicly accessible: RDS → Modify → Connectivity → set to **No**
- Backup retention: RDS → Modify → Backup → set retention period

### AWS Config Rules Deployed
- `s3-bucket-public-read-prohibited`
- `s3-bucket-public-write-prohibited`
- `rds-instance-public-access-check`
- `restricted-ssh`
- `vpc-flow-logs-enabled`
- `cloud-trail-enabled`

### CloudTrail Protection
- Log file validation: CloudTrail → Trail → Edit → enable
- S3 bucket encryption: SSE-S3 (was already enabled)
- Lifecycle rule: expire after 90 days

### IAM Eradication
- Identified backdoor users via Athena (`CreateUser` events)
- Delete access keys first, then delete users
- Three users to eradicate: `compromised-user`, `system-backup-643dac10`, `app-admin-643dac10`

### SSM Documents
- Check Systems Manager → Documents → Owned by me
- Delete any unauthorized documents (attacker persistence mechanism)

## Console Navigation Cheat Sheet

| Task | Path |
|------|------|
| S3 account-level block | S3 → left sidebar → Block Public Access settings for this account |
| EC2 create AMI | EC2 → Instance → Actions → Image and templates → Create image |
| EC2 change SG | EC2 → Instance → Actions → Security → Change security groups |
| EC2 IMDSv2 | EC2 → Instance → Actions → Instance settings → Modify instance metadata options |
| Launch template new version | EC2 → Launch templates → Actions → Modify template (Create new version) |
| Set default version | Launch templates → Actions → Set default version |
| Instance refresh | Auto Scaling groups → Instance management → Start instance refresh |
| NACL rules | VPC → Network ACLs → select → Inbound/Outbound rules → Edit |
| RDS public access | RDS → Databases → Modify → Connectivity → Publicly accessible |
| Config rules | Config → Rules → Add rule |
| CloudTrail validation | CloudTrail → Trails → Edit → Log file validation |
| SSM documents | Systems Manager → Documents → Owned by me |
| Athena queries | Athena → Query editor → select workgroup + database |

## Key Takeaway

**Preserve before you eradicate. Always. Every time.**
