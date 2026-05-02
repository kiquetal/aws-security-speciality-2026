# FAQ: AWS Systems Manager Session Manager

> **Blueprint refs:** Task 3.2 (secure administrative access to compute), Task 1.2 (logging solutions)
> **Diagrams:** [session-manager-logging.png](../diagrams/session-manager-logging.png) | [session-manager-vpc-endpoints.png](../diagrams/session-manager-vpc-endpoints.png)

## Security Use Cases

### Secure Administrative Access (No SSH/RDP)
- **No inbound ports required** — agent makes outbound HTTPS (443) to SSM endpoint
- **No bastion hosts** — eliminates jump-box infrastructure and attack surface
- **No SSH keys to manage** — authentication via IAM, not key pairs
- **No public IP required** — works via VPC endpoints (PrivateLink)
- **Centralized access control** — IAM policies govern who can start sessions on which instances

### How It Works
1. SSM Agent (pre-installed on Amazon Linux 2/2023, Windows AMIs) opens **outbound** HTTPS connection to SSM endpoint
2. Admin calls `ssm:StartSession` API (console, CLI, or SDK)
3. SSM service brokers a WebSocket channel between admin and agent
4. All traffic encrypted with TLS 1.2+ in transit, optional KMS encryption for session data

### K8s Equivalent
- **Session Manager ≈ `kubectl exec`** with audit logging
- **IAM policy on `ssm:StartSession`** ≈ K8s RBAC on `pods/exec`
- **Session logging** ≈ K8s audit log + terminal recording

## Three Logging Layers (Exam-Critical)

| Log Destination | What It Captures | Latency | Enabled By Default? |
|---|---|---|---|
| **CloudTrail** | `StartSession`, `TerminateSession`, `ResumeSession` API calls (who, when, which instance) | ~15 min | ✅ Yes (management events) |
| **S3** | Full session transcript (keystrokes, command output) | After session ends | ❌ Must configure |
| **CloudWatch Logs** | Same session transcript | **Near real-time streaming** | ❌ Must configure |

### What Each Layer Answers

- **"Who connected to the instance?"** → CloudTrail
- **"What commands did they run?"** → S3 or CloudWatch Logs
- **"Alert me if someone runs a dangerous command right now"** → CloudWatch Logs (real-time) + metric filter + alarm

### Logging Configuration
- Configured in **Session Manager preferences** (not CloudTrail settings)
- Per-account, per-region setting
- Can enforce via SSM Session Document (`AWS-StartInteractiveCommand`, `AWS-StartNonInteractiveCommand`)

## Encryption

### In Transit
- TLS 1.2+ between agent and SSM endpoint (always)
- Optional **KMS encryption** for the session data channel itself (additional layer)

### Session Logs at Rest
- **S3**: Encrypt with SSE-S3, SSE-KMS, or SSE-C
- **CloudWatch Logs**: Encrypt with KMS customer managed key
- **Exam preference**: Customer managed KMS key for both (audit trail + rotation)

## Key Limits/Quotas

| Limit | Value |
|---|---|
| Concurrent sessions per instance | **2** (default, can increase) |
| Concurrent sessions per account per region | **500** |
| Session idle timeout | **20 minutes** (configurable, max 60 min) |
| Session max duration | **No hard limit** (idle timeout applies) |
| Session log max size (S3) | **No limit** |
| Supported OS | Linux, macOS, Windows |

## IAM Access Control

### Who Can Start Sessions
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSessionManagerForTaggedInstances",
      "Effect": "Allow",
      "Action": "ssm:StartSession",
      "Resource": "arn:aws:ec2:us-east-1:123456789012:instance/*",
      "Condition": {
        "StringEquals": {
          "ssm:resourceTag/Environment": "production"
        }
      }
    },
    {
      "Sid": "AllowSessionManagerPlugin",
      "Effect": "Allow",
      "Action": "ssm:TerminateSession",
      "Resource": "arn:aws:ssm:*:*:session/${aws:username}-*"
    }
  ]
}
```

### Enforce Logging (Block Sessions Without Logging)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenySessionWithoutLogging",
      "Effect": "Deny",
      "Action": "ssm:StartSession",
      "Resource": "arn:aws:ssm:*:*:document/SSM-SessionManagerRunShell",
      "Condition": {
        "BoolIfExists": {
          "ssm:SessionDocumentAccessCheck": "true"
        }
      }
    }
  ]
}
```

> ⚠️ Use a custom Session Document that mandates S3/CloudWatch logging, then restrict users to that document only.

### Instance Role (Minimum Permissions)
The EC2 instance needs an instance profile with:
- `ssm:UpdateInstanceInformation` — heartbeat to SSM
- `ssmmessages:CreateControlChannel` — session channel
- `ssmmessages:CreateDataChannel` — session data
- `s3:PutObject` — if logging to S3
- `logs:CreateLogStream`, `logs:PutLogEvents` — if logging to CloudWatch
- `kms:GenerateDataKey` — if encrypting session data with KMS

> **Exam gotcha:** If Session Manager connects but logs are missing, check the **instance role** — it needs S3/CloudWatch/KMS permissions, not just SSM permissions.

## VPC Endpoints (Private Access)

For instances in **private subnets** (no internet gateway, no NAT):

| Endpoint | Service | Type |
|---|---|---|
| `com.amazonaws.region.ssm` | SSM API | Interface (PrivateLink) |
| `com.amazonaws.region.ssmmessages` | Session data channel | Interface (PrivateLink) |
| `com.amazonaws.region.ec2messages` | SSM Agent messages | Interface (PrivateLink) |
| `com.amazonaws.region.s3` | Session log delivery | Gateway (free) |
| `com.amazonaws.region.logs` | CloudWatch Logs delivery | Interface (PrivateLink) |
| `com.amazonaws.region.kms` | KMS encryption | Interface (PrivateLink) |

> **Exam gotcha:** You need **three** SSM-related endpoints (`ssm`, `ssmmessages`, `ec2messages`) for Session Manager to work in a private subnet. Missing any one = connection failure.

## Exam Gotchas

### Session Manager vs SSH/RDP
- Session Manager: No inbound ports, IAM auth, full audit trail, no key management
- SSH: Requires port 22, key pairs, bastion hosts, no native session recording
- **Exam always prefers Session Manager** for "most secure administrative access"

### CloudTrail Is Not Enough
- CloudTrail logs **that** a session happened (API call)
- CloudTrail does NOT log **what happened inside** the session
- If question asks "audit commands run during session" → S3 or CloudWatch Logs

### Logging Must Be Explicitly Configured
- S3 and CloudWatch logging are **off by default**
- Configure in Session Manager preferences or via Session Document
- Can enforce with IAM policy (deny sessions without approved Session Document)

### Missing Logs Troubleshooting (Task 1.3)
1. **Instance role missing permissions** — needs `s3:PutObject` or `logs:PutLogEvents`
2. **VPC endpoint missing** — private subnet instance can't reach S3/CloudWatch
3. **KMS key policy** — if encrypting logs, instance role needs `kms:GenerateDataKey`
4. **Session Document not configured** — preferences not set for logging destination
5. **S3 bucket policy** — must allow the instance role to write

### Session Manager vs EC2 Instance Connect
- **Session Manager**: Shell access, full session logging, works on Linux + Windows
- **EC2 Instance Connect**: Pushes temporary SSH key, requires port 22 open, Linux only
- **Exam preference**: Session Manager (no ports, better logging)

### Run Command vs Session Manager
- **Run Command**: Execute commands remotely, output to S3/CloudWatch, no interactive shell
- **Session Manager**: Interactive shell session, real-time terminal
- Both use SSM Agent, both need similar IAM/VPC endpoint setup

## Integration with Other Services

| Service | Integration |
|---|---|
| **CloudTrail** | Logs StartSession/TerminateSession API calls |
| **CloudWatch Logs** | Real-time session transcript streaming |
| **S3** | Session transcript archive |
| **KMS** | Encrypt session data channel + logs at rest |
| **EventBridge** | Trigger on session start/stop events |
| **IAM** | Control who can start sessions on which instances |
| **VPC Endpoints** | Private subnet access without internet |
| **AWS Config** | Rule: `ec2-instance-managed-by-systems-manager` |

## Best Practices

1. **Use Session Manager over SSH/RDP** — always, for all admin access
2. **Enable both S3 and CloudWatch logging** — archive + real-time
3. **Encrypt with KMS** — customer managed key for session data and logs
4. **Enforce logging via IAM** — deny sessions without approved Session Document
5. **Use VPC endpoints** — no internet exposure for management traffic
6. **Tag-based access** — restrict sessions to specific environments via `ssm:resourceTag`
7. **Set idle timeout** — 20 min default, reduce for sensitive environments
8. **Monitor with EventBridge** — alert on session starts to production instances
9. **Audit with Config** — ensure all instances are SSM-managed
10. **Restrict TerminateSession** — users should only terminate their own sessions
