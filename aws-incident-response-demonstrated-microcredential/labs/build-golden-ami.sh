#!/bin/bash
# Golden AMI Build Script — Amazon Linux 2023 + Nginx
# This script creates a hardened AMI step by step.
# Run each section manually or automate with SSM Automation.

set -euo pipefail

REGION="us-east-1"
INSTANCE_TYPE="t3.micro"
KEY_NAME="my-key-pair"
SUBNET_ID="subnet-xxxxx"          # Use a private subnet
SG_ID="sg-xxxxx"                  # SG that allows SSM access only (no SSH)
INSTANCE_PROFILE="SSMInstanceProfile"  # IAM role with AmazonSSMManagedInstanceCore

# ============================================================
# STEP 1 — Get the latest Amazon Linux 2023 AMI
# ============================================================
# AWS publishes the latest AMI ID in SSM Parameter Store.
# This avoids hardcoding AMI IDs that change per region/update.

BASE_AMI=$(aws ssm get-parameter \
  --name "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64" \
  --region "$REGION" \
  --query "Parameter.Value" \
  --output text)

echo "Base AMI: $BASE_AMI"

# ============================================================
# STEP 2 — Launch a builder instance
# ============================================================
# No SSH key needed — we use SSM Session Manager for access.
# Instance profile gives it the IAM role for SSM.

INSTANCE_ID=$(aws ec2 run-instances \
  --image-id "$BASE_AMI" \
  --instance-type "$INSTANCE_TYPE" \
  --subnet-id "$SUBNET_ID" \
  --security-group-ids "$SG_ID" \
  --iam-instance-profile "Name=$INSTANCE_PROFILE" \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=golden-ami-builder},{Key=Purpose,Value=ami-build}]' \
  --region "$REGION" \
  --query "Instances[0].InstanceId" \
  --output text)

echo "Builder instance: $INSTANCE_ID"

# Wait for the instance to be running and SSM-ready
aws ec2 wait instance-status-ok \
  --instance-ids "$INSTANCE_ID" \
  --region "$REGION"

echo "Instance is ready."

# ============================================================
# STEP 3 — Patch the OS using SSM Run Command
# ============================================================
# This applies all available security patches.

aws ssm send-command \
  --document-name "AWS-RunPatchBaseline" \
  --targets "Key=instanceids,Values=$INSTANCE_ID" \
  --parameters '{"Operation":["Install"]}' \
  --region "$REGION" \
  --comment "Patch OS for golden AMI"

echo "Patching started. Waiting for completion..."
sleep 120  # In production, poll the command status instead

# ============================================================
# STEP 4 — Install and configure Nginx using SSM Run Command
# ============================================================

aws ssm send-command \
  --document-name "AWS-RunShellScript" \
  --targets "Key=instanceids,Values=$INSTANCE_ID" \
  --parameters '{
    "commands": [
      "dnf install -y nginx",
      "systemctl enable nginx",
      "systemctl start nginx"
    ]
  }' \
  --region "$REGION" \
  --comment "Install Nginx"

echo "Nginx installation started."
sleep 30

# ============================================================
# STEP 5 — Harden the instance using SSM Run Command
# ============================================================

aws ssm send-command \
  --document-name "AWS-RunShellScript" \
  --targets "Key=instanceids,Values=$INSTANCE_ID" \
  --parameters '{
    "commands": [
      "# --- SSH Hardening ---",
      "sed -i 's/^#PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config",
      "sed -i 's/^#PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config",
      "systemctl restart sshd",

      "# --- Remove unnecessary packages ---",
      "dnf remove -y telnet ftp",

      "# --- Install and configure CloudWatch Agent ---",
      "dnf install -y amazon-cloudwatch-agent",
      "systemctl enable amazon-cloudwatch-agent",

      "# --- Enable audit logging ---",
      "dnf install -y audit",
      "systemctl enable auditd",
      "systemctl start auditd",

      "# --- Clean up ---",
      "dnf clean all",
      "rm -rf /tmp/* /var/tmp/*",
      "rm -f /root/.bash_history",
      "history -c"
    ]
  }' \
  --region "$REGION" \
  --comment "Harden instance for golden AMI"

echo "Hardening started."
sleep 30

# ============================================================
# STEP 6 — Create the Golden AMI
# ============================================================
# --no-reboot: creates the AMI without stopping the instance.
# In production, you may want to stop first for a clean snapshot.

GOLDEN_AMI=$(aws ec2 create-image \
  --instance-id "$INSTANCE_ID" \
  --name "golden-ami-nginx-$(date +%Y-%m-%d)" \
  --description "Hardened Amazon Linux 2023 + Nginx - $(date +%Y-%m-%d)" \
  --no-reboot \
  --region "$REGION" \
  --query "ImageId" \
  --output text)

echo "Golden AMI: $GOLDEN_AMI"

# Wait for AMI to be available
aws ec2 wait image-available \
  --image-ids "$GOLDEN_AMI" \
  --region "$REGION"

echo "AMI is ready."

# ============================================================
# STEP 7 — Tag the AMI for tracking
# ============================================================

aws ec2 create-tags \
  --resources "$GOLDEN_AMI" \
  --tags \
    "Key=Name,Value=golden-ami-nginx" \
    "Key=Version,Value=$(date +%Y-%m-%d)" \
    "Key=Hardened,Value=true" \
    "Key=OS,Value=al2023" \
  --region "$REGION"

echo "AMI tagged."

# ============================================================
# STEP 8 — Store AMI ID in SSM Parameter Store
# ============================================================
# Launch templates can reference this parameter dynamically.
# When you rebuild the AMI, just update this parameter.

aws ssm put-parameter \
  --name "/golden-ami/nginx/latest" \
  --type "String" \
  --value "$GOLDEN_AMI" \
  --overwrite \
  --region "$REGION"

echo "AMI ID stored in Parameter Store: /golden-ami/nginx/latest"

# ============================================================
# STEP 9 — Terminate the builder instance
# ============================================================

aws ec2 terminate-instances \
  --instance-ids "$INSTANCE_ID" \
  --region "$REGION"

echo "Builder instance terminated."
echo ""
echo "=== DONE ==="
echo "Golden AMI: $GOLDEN_AMI"
echo "Parameter:  /golden-ami/nginx/latest"
