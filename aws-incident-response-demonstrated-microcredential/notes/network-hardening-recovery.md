# Network Hardening and Recovery

## VPC Security Controls

### Security Groups (Stateful)
- Instance-level firewall
- **Allow rules only** — no explicit deny
- Default: all outbound allowed, all inbound denied
- Changes take effect **immediately**
- Use for: EC2 isolation (empty SG), least-privilege access

### Network ACLs (Stateless)
- Subnet-level firewall
- **Allow and deny rules** — evaluated by rule number (lowest first)
- Default: all traffic allowed
- Use for: blocking specific IPs, subnet-level isolation

### VPC Flow Logs
- Capture IP traffic metadata (not payload)
- Can be sent to CloudWatch Logs or S3
- Enable at VPC, subnet, or ENI level
- **Key for incident response**: identify unusual traffic patterns, data exfiltration attempts

## Recovery Patterns

### EC2 Recovery After Compromise

1. **Do NOT reuse the compromised instance**
2. Launch a **new instance** from a known-good AMI
3. Apply the **hardened Security Group** (least-privilege)
4. Use **Systems Manager** to:
   - Patch the instance (SSM Patch Manager)
   - Run compliance checks (SSM State Manager)
   - Execute commands without SSH (SSM Run Command)
5. Validate with Config rules before returning to production

### Auto Scaling for Recovery

- Auto Scaling can **replace unhealthy instances** automatically
- Use **launch templates** with hardened AMIs
- Health checks detect compromised instances (custom health checks via ELB)
- **Key exam pattern**: terminate compromised instance → Auto Scaling launches clean replacement

### Network Hardening Checklist

| Control | Action |
|---------|--------|
| Security Groups | Remove overly permissive rules (0.0.0.0/0) |
| NACLs | Add deny rules for known malicious IPs |
| VPC Flow Logs | Enable if not already active |
| VPC Endpoints | Use for S3/DynamoDB to keep traffic off public internet |
| Subnet isolation | Move sensitive resources to private subnets |
| NAT Gateway | Control outbound internet access from private subnets |

## Systems Manager for Incident Response

### Key capabilities
- **Run Command** — execute scripts on instances without SSH/RDP
- **Session Manager** — interactive shell without opening inbound ports
- **Patch Manager** — automate OS and application patching
- **State Manager** — enforce desired configuration state
- **Automation** — runbooks for multi-step remediation

### Exam detail
- SSM Agent must be installed and running on the instance
- Instance needs an IAM role with `AmazonSSMManagedInstanceCore` policy
- Works across accounts with AWS Organizations
