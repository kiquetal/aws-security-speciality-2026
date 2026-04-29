# Building a Golden AMI for Incident Recovery

## Why Golden AMIs Matter

When an incident happens and instances are compromised, you need to **replace them fast** with clean, hardened instances. If you don't have a pre-built golden AMI, you waste time building from scratch during the incident.

Golden AMIs are part of the **Recover** phase of incident response.

## What Goes Into a Golden AMI

| Category | What | Why |
|----------|------|-----|
| OS Patches | Latest security updates | Close known vulnerabilities |
| SSH Hardening | No root login, no password auth | Prevent brute force attacks |
| Cleanup | Remove telnet, ftp, unnecessary packages | Reduce attack surface |
| Monitoring | CloudWatch Agent installed and enabled | OS-level metrics and log shipping |
| Auditing | auditd installed and enabled | Track system-level activity |
| Application | Nginx (or your app) installed and configured | Ready to serve traffic |

## How It's Built — No SSH Required

The entire build process uses **Systems Manager (SSM)** — no SSH, no inbound ports needed.

The builder instance only needs:
- An **IAM instance profile** with the `AmazonSSMManagedInstanceCore` managed policy
- A **Security Group** with no inbound rules (SSM uses outbound HTTPS to the SSM endpoint)
- **Outbound access** to SSM, S3, and CloudWatch endpoints (or VPC endpoints in a private subnet)

### Why SSM instead of SSH?

| SSH | SSM |
|-----|-----|
| Requires port 22 open | No inbound ports needed |
| Requires key pair management | Uses IAM for authentication |
| No built-in audit trail | Every command logged in CloudTrail |
| Hard to automate across accounts | Works with Organizations and Automation |

## The Build Process

See the full script: [`labs/build-golden-ami.sh`](../labs/build-golden-ami.sh)

### Step 1 — Get the latest base AMI

AWS publishes the latest AMI IDs in **SSM Parameter Store**. This avoids hardcoding AMI IDs that change per region and update cycle.

```bash
aws ssm get-parameter \
  --name "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64" \
  --query "Parameter.Value" --output text
```

### Step 2 — Launch a builder instance

Launch with an IAM instance profile (for SSM access) and no SSH key. The instance goes in a private subnet with a restrictive SG.

### Step 3 — Patch the OS

Use the SSM document `AWS-RunPatchBaseline` to apply all security patches:

```bash
aws ssm send-command \
  --document-name "AWS-RunPatchBaseline" \
  --targets "Key=instanceids,Values=$INSTANCE_ID" \
  --parameters '{"Operation":["Install"]}'
```

This is the same mechanism **SSM Patch Manager** uses. It applies patches based on the patch baseline for the OS.

### Step 4 — Install the application

Use `AWS-RunShellScript` to run shell commands on the instance via SSM:

```bash
aws ssm send-command \
  --document-name "AWS-RunShellScript" \
  --targets "Key=instanceids,Values=$INSTANCE_ID" \
  --parameters '{"commands":["dnf install -y nginx","systemctl enable nginx"]}'
```

### Step 5 — Harden the instance

Same mechanism — run hardening commands via SSM:
- Disable root SSH login and password authentication
- Remove unnecessary packages (telnet, ftp)
- Install and enable CloudWatch Agent
- Install and enable auditd
- Clean up temp files and shell history

### Step 6 — Create the AMI

```bash
aws ec2 create-image \
  --instance-id $INSTANCE_ID \
  --name "golden-ami-nginx-$(date +%Y-%m-%d)" \
  --no-reboot
```

The `--no-reboot` flag creates the AMI without stopping the instance. For a perfectly consistent snapshot, omit this flag (the instance will stop briefly).

### Step 7 — Store the AMI ID in Parameter Store

```bash
aws ssm put-parameter \
  --name "/golden-ami/nginx/latest" \
  --type "String" \
  --value "$GOLDEN_AMI" \
  --overwrite
```

**This is the key integration point.** Your Auto Scaling launch template references this parameter. When you rebuild the golden AMI, you update the parameter — and the next instance refresh picks up the new AMI automatically.

### Step 8 — Terminate the builder and clean up

The builder instance is disposable. Delete it after the AMI is created.

## Using the Golden AMI in Incident Recovery

When a compromise happens:

1. **Update the launch template** to use the latest golden AMI from Parameter Store
2. **Start an instance refresh** on the Auto Scaling group
3. Auto Scaling **gradually replaces** compromised instances with clean ones
4. **Verify** with Config rules that new instances are compliant

```bash
# Update launch template
GOLDEN_AMI=$(aws ssm get-parameter --name "/golden-ami/nginx/latest" --query "Parameter.Value" --output text)

aws ec2 create-launch-template-version \
  --launch-template-id lt-xxxxx \
  --source-version '$Latest' \
  --launch-template-data "{\"ImageId\":\"$GOLDEN_AMI\"}"

# Trigger instance refresh
aws autoscaling start-instance-refresh \
  --auto-scaling-group-name my-asg
```

## Exam Key Points

- Golden AMIs should be **rebuilt regularly** (automate with SSM Automation)
- Store AMI IDs in **Parameter Store** for dynamic reference
- Use **Config rules** to verify instances match the latest golden AMI
- The entire build uses **SSM only** — no SSH, no inbound ports, full audit trail in CloudTrail
- During recovery: **update template first, then replace instances** — never the other way around
