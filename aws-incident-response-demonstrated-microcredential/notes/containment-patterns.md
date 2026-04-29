# Containment Patterns

## Core Principle: Isolate → Preserve → Investigate

Never stop or terminate a compromised resource before isolating and preserving evidence.

## EC2 Instance Containment

### Step 1 — Network Isolation

Replace the instance's Security Group with a **new, completely empty SG** (no inbound, no outbound rules).

**Why not just remove the existing SG?**
- The instance might fall back to a default SG that still allows traffic
- Removing rules from the existing SG could affect other instances sharing it

**What the empty SG achieves:**
- Cuts all ingress and egress — stops exfiltration, C2 communication, lateral movement
- Instance stays running — volatile data (RAM, processes, connections) is preserved

**Why not stop the instance?**
- Stopping destroys volatile memory evidence
- Doesn't help if attacker already pivoted using stolen credentials

### Step 2 — Preserve Evidence

Create **EBS snapshots** of all attached volumes **immediately after isolation, before any forensic tools touch the disk**.

**Why snapshots matter:**
- Point-in-time forensic copy that can't be tampered with
- Mount to a clean forensic instance in an isolated VPC for safe analysis
- Evidence preservation for legal/compliance investigations

### Step 3 — Investigate

- Mount snapshot on a **clean instance in an isolated VPC**
- Never investigate on the live compromised instance
- Use Systems Manager for remote access if needed (no SSH required)

## S3 Data Exfiltration Containment

### Automated Remediation Flow

```
Config (detect) → EventBridge (route) → SNS (notify) + Lambda (remediate)
```

1. **Config** evaluates managed rule (e.g., `s3-bucket-public-read-prohibited`)
2. **EventBridge** matches the `NON_COMPLIANT` event
3. **SNS** fans out to:
   - Lambda function for automated remediation
   - Security team for alerting
4. **Lambda** executes two actions:
   - `PutBucketPolicy` — remove public access
   - `PutPublicAccessBlock` — prevent future public access

### Key Exam Detail

EventBridge is **always enabled** — AWS services automatically emit events to it. You only need to create rules to match and route events.

## When to Use Step Functions vs Lambda

| Scenario | Use |
|----------|-----|
| Simple, single-action remediation | Lambda |
| Multi-step workflow with dependencies | Step Functions |
| Requires error handling and retries | Step Functions |
| Needs human approval gates | Step Functions (Task token + callback) |
| Requires complete audit trail of execution | Step Functions |
