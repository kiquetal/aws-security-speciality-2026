# FAQ: Amazon GuardDuty

## Security Use Cases

### Intelligent Threat Detection
- **Continuous monitoring** of AWS accounts, workloads, and data
- **ML-based anomaly detection** and threat intelligence
- **No agents required** for foundational monitoring (CloudTrail, VPC Flow Logs, DNS logs)
- **Fully managed** - no infrastructure to deploy or maintain

### Detection Categories
1. **Reconnaissance**: Unusual API activity, port scanning, failed login attempts
2. **Instance compromise**: Crypto mining, malware, C2 communication, data exfiltration
3. **Account compromise**: API calls from unusual geolocation/anonymizing proxy, credential exfiltration
4. **Bucket compromise**: Suspicious S3 access patterns, unauthorized access from malicious IPs
5. **Malware**: Trojans, worms, crypto miners, rootkits, bots
6. **Container compromise**: Malicious behavior in EKS/ECS workloads

### Protection Plans
- **Foundational**: CloudTrail, VPC Flow Logs, DNS logs (always enabled)
- **S3 Protection**: CloudTrail S3 data events (optional)
- **EKS Protection**: EKS audit logs (optional)
- **Runtime Monitoring**: EC2, EKS, ECS runtime activity via security agent (optional)
- **Malware Protection**: EBS volumes, S3 objects, AWS Backup (optional)
- **RDS Protection**: Aurora login events (optional)
- **Lambda Protection**: VPC Flow Logs for Lambda functions (optional)

### Extended Threat Detection (AI/ML)
- **Attack sequence detection**: Correlates multiple findings into single high-priority alert
- **Natural language summaries**: AI-generated threat descriptions
- **Prescriptive remediation**: Step-by-step response recommendations
- **MITRE ATT&CK mapping**: Tactic and technique identification
- **No additional cost** - included with GuardDuty

## Key Limits/Quotas

### Account Limits
- **Regional service** - must enable in each region
- **Multi-account support**: Delegated administrator for organization
- **Member accounts**: Unlimited (via AWS Organizations)

### Finding Retention
- **90 days** in GuardDuty console
- **Export to S3** for longer retention via EventBridge
- **Security Hub integration**: Cross-region aggregation

### Runtime Monitoring
- **Automatic agent deployment**: GuardDuty manages agent lifecycle
- **Manual deployment**: Customer manages agent updates
- **VPC endpoints**: Created automatically in VPCs with monitored workloads
- **Resource overhead**: Minimal CPU/memory impact

### Malware Protection
- **EBS scanning**: Once per 24 hours per instance
- **S3 scanning**: Newly uploaded objects only
- **Snapshot retention**: 24 hours (up to 7 days if scan fails)
- **Supported file systems**: ext2, ext3, ext4, xfs, ntfs

### Pricing
- **Pay-as-you-go**: Based on volume of data analyzed
- **30-day free trial**: All features (except S3 Malware Protection)
- **S3 Malware Protection**: 12-month free tier (1,000 requests, 1GB/month)
- **No charge for VPC Flow Logs** from instances with Runtime Monitoring agent

## Exam Gotchas

### GuardDuty vs Macie vs Inspector
- **GuardDuty**: Threat detection (malicious activity, compromised resources)
- **Macie**: Sensitive data discovery in S3 (PII, credentials)
- **Inspector**: Vulnerability scanning (EC2, Lambda, container images)

### Foundational vs Protection Plans
- **Foundational**: Always enabled, no opt-out (CloudTrail, VPC Flow Logs, DNS)
- **Protection plans**: Optional, can enable/disable individually
- **Extended Threat Detection**: Requires multiple protection plans for comprehensive coverage

### S3 Protection
- **No need to enable S3 data events in CloudTrail** - GuardDuty has direct access
- **Monitors all buckets** by default
- **No additional CloudTrail costs**
- **Separate 30-day free trial**

### EKS Protection
- **No need to enable EKS audit logs** - GuardDuty has direct access
- **Monitors control plane activity** (EKS audit logs)
- **Runtime Monitoring**: Monitors pod/container runtime activity (requires agent)
- **Both needed** for comprehensive EKS threat detection

### Runtime Monitoring
- **NOT enabled by default** (unlike other protection plans)
- **Requires agent deployment**: Automatic or manual
- **Supports**: EKS on EC2, ECS on EC2/Fargate, standalone EC2
- **VPC endpoints created**: For agent communication
- **No charge for VPC Flow Logs** from instances with agent

### Malware Protection
- **EBS volumes**: Scans replica, not original volume
- **Once per 24 hours** per instance (even if multiple findings)
- **Snapshot retention**: Optional, disabled by default
- **S3 objects**: Scans on upload, not existing objects
- **Quarantine**: Automatic move to isolated bucket (configurable)
- **AWS Backup**: Incremental scanning (only net-new data)

### RDS Protection
- **Aurora only**: MySQL and PostgreSQL compatible
- **Login activity monitoring**: Detects suspicious login attempts
- **No performance impact** on databases
- **ML-based**: Profiles normal behavior, detects anomalies

### Lambda Protection
- **VPC Flow Logs**: Monitors network activity from Lambda functions
- **No performance impact** on Lambda executions
- **Detects**: Crypto mining, C2 communication

### Extended Threat Detection
- **Automatic**: Enabled for all GuardDuty customers
- **No additional cost**: Included with GuardDuty
- **Requires S3 Protection**: For data exfiltration detection in attack sequences
- **Correlates findings**: Across multiple AWS services and resources

### Threat Intelligence
- **AWS threat intelligence**: Included
- **Third-party feeds**: Proofpoint, CrowdStrike (included)
- **Custom threat lists**: Upload your own IP/domain lists
- **Trusted IP lists**: Whitelist known safe IPs

### Finding Severity
- **Low (0.1-3.9)**: Suspicious activity, may be false positive
- **Medium (4.0-6.9)**: Suspicious activity, investigate
- **High (7.0-8.9)**: Likely malicious, respond immediately
- **Critical (9.0-10.0)**: Confirmed malicious, urgent response required

### Multi-Account Management
- **Delegated administrator**: Centralized management for organization
- **Auto-enable**: New accounts automatically protected
- **Findings aggregation**: All findings visible in administrator account
- **EventBridge**: Events aggregated to administrator account

### Integration with Security Hub
- **Automatic**: GuardDuty findings sent to Security Hub
- **Cross-region aggregation**: Use Security Hub for centralized view
- **ASFF format**: AWS Security Finding Format

## Best Practices for IAM Policies

1. **Enable GuardDuty in all regions** - threats can originate anywhere
2. **Use delegated administrator** for multi-account organizations
3. **Enable all protection plans** for comprehensive coverage
4. **Auto-enable for new accounts** via Organizations
5. **Export findings to S3** for long-term retention (>90 days)
6. **Integrate with EventBridge** for automated response
7. **Use Security Hub** for cross-region aggregation
8. **Enable Runtime Monitoring** for EC2, EKS, ECS
9. **Configure Malware Protection** for S3 buckets with user uploads
10. **Monitor with CloudWatch** - track finding counts and severity

### Example: Automated Response to High-Severity Findings
```json
{
  "source": ["aws.guardduty"],
  "detail-type": ["GuardDuty Finding"],
  "detail": {
    "severity": [7, 8, 9, 10]
  }
}
```
Trigger Lambda to: isolate instance, revoke credentials, notify security team

### Example: Prevent GuardDuty Disablement
```json
{
  "Effect": "Deny",
  "Action": [
    "guardduty:DeleteDetector",
    "guardduty:DisassociateFromMasterAccount",
    "guardduty:StopMonitoringMembers"
  ],
  "Resource": "*"
}
```
