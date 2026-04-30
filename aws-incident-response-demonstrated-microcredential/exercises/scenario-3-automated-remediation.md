# Scenario 3 — Automated Remediation of a Public S3 Bucket + Network Hardening Recovery

## Situation

Your organization runs a multi-account setup with AWS Organizations. At 4 PM, Security Hub surfaces a **CRITICAL** finding: an S3 bucket in a workload account (`arn:aws:s3:::finance-reports-prod`) has been made publicly accessible. CloudTrail shows a `PutBucketPolicy` call 10 minutes ago from an IAM user `dev-contractor` that set `Principal: "*"` on the bucket.

Simultaneously, GuardDuty raises a finding of type `UnauthorizedAccess:EC2/MaliciousIPCaller.Custom` on an EC2 instance in the same account. VPC Flow Logs confirm outbound connections from this instance to a known C2 (command-and-control) IP on port 443.

You need to contain both threats, automate future detection, and harden the environment to prevent recurrence.

## Part A — Immediate Containment (Manual)

### Questions

1. You have two active threats (public S3 bucket + compromised EC2). **Which do you contain first and why?**
2. For the S3 bucket, write the **exact AWS CLI command** to block all public access immediately. What is the difference between this approach and modifying the bucket policy?
3. For the EC2 instance, describe the containment steps. **Why is modifying the existing Security Group a mistake?**

### Answers

#### 1 — Prioritization

**S3 first.** The bucket is actively exposed to the entire internet — data exfiltration is happening *right now* to anyone who discovers the URL. The EC2 instance is communicating with a single C2 IP, which is serious but has a smaller blast radius.

**General rule:** Contain the threat with the widest exposure first.

#### 2 — S3 Public Access Block

```bash
aws s3api put-public-access-block \
  --bucket finance-reports-prod \
  --public-access-block-configuration \
    BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
```

**Difference from modifying the bucket policy:**
- `PutPublicAccessBlock` is an **override** — it blocks public access regardless of what the bucket policy says. Even if the attacker's `Principal: "*"` policy is still there, it's neutralized.
- Modifying the bucket policy is a **correction** — you're fixing the specific misconfiguration, but if the attacker still has access, they can re-apply it.
- **Use both:** Block first (immediate), then fix the policy (eradication).

#### 3 — EC2 Containment

1. Create a **new, empty Security Group** (no inbound, no outbound rules) in the same VPC.
2. **Replace** the instance's SG with the empty one — do NOT modify the existing SG.
3. Create **EBS snapshots** of all attached volumes for forensic preservation.

**Why not modify the existing SG?**
- Other instances may share the same SG — your changes would affect them.
- Removing rules from the existing SG destroys evidence of the original network configuration.
- The empty SG approach is atomic — one API call, instant isolation, no side effects.

---

## Part B — Automated Remediation Architecture

### Questions

4. Design an automated remediation pipeline that detects and fixes public S3 buckets **without human intervention**. Name each AWS service in the chain and what it does.
5. Write the **EventBridge rule pattern** (JSON) that matches when AWS Config evaluates a bucket as `NON_COMPLIANT` for the `s3-bucket-public-read-prohibited` managed rule.
6. The remediation Lambda needs two IAM permissions on the target bucket. What are they, and why do you need **both**?

### Answers

#### 4 — Remediation Pipeline

```
AWS Config → EventBridge → SNS → Lambda (remediate)
                              → Security Team (alert)
```

| Service | Role |
|---------|------|
| **AWS Config** | Continuously evaluates `s3-bucket-public-read-prohibited` managed rule |
| **EventBridge** | Matches `NON_COMPLIANT` evaluation results and routes them |
| **SNS** | Fan-out: triggers Lambda for remediation AND notifies the security team |
| **Lambda** | Executes `PutPublicAccessBlock` + `PutBucketPolicy` on the offending bucket |

**Why EventBridge and not a Config remediation action directly?**
Config has built-in remediation via SSM Automation documents, which works. But the EventBridge pattern gives you:
- Fan-out (remediate + alert simultaneously)
- Custom logic in Lambda (e.g., check if the bucket is in an exception list)
- Consistent architecture across all detection sources (Config, GuardDuty, Security Hub)

#### 5 — EventBridge Rule Pattern

```json
{
  "source": ["aws.config"],
  "detail-type": ["Config Rules Compliance Change"],
  "detail": {
    "messageType": ["ComplianceChangeNotification"],
    "configRuleName": ["s3-bucket-public-read-prohibited"],
    "newEvaluationResult": {
      "complianceType": ["NON_COMPLIANT"]
    }
  }
}
```

**Exam traps:**
- `source` is `aws.config`, not `aws.configrules`
- `detail-type` is `Config Rules Compliance Change`, not `AWS API Call via CloudTrail`
- The compliance result is nested under `newEvaluationResult.complianceType`

#### 6 — Lambda IAM Permissions

The Lambda function needs:

1. **`s3:PutBucketPublicAccessBlock`** — to apply the four public access block settings
2. **`s3:PutBucketPolicy`** — to remove or replace the malicious bucket policy

**Why both?**
- `PutBucketPublicAccessBlock` neutralizes public access immediately but doesn't remove the bad policy — it's still there, just overridden.
- `PutBucketPolicy` removes the attacker's `Principal: "*"` policy so the bucket is clean even if someone later disables the public access block.
- Defense in depth: the block is the safety net, the policy fix is the actual remediation.

---

## Part C — Network Hardening and Recovery

### Questions

7. After containing the EC2 instance, your team decides to **not reuse it**. Describe the recovery process using Auto Scaling and a hardened AMI.
8. What **three VPC-level controls** would you add to prevent the compromised instance's C2 communication pattern from succeeding in the future?
9. You want to ensure all EC2 instances in this account have the SSM Agent running and are patched. Which **two Systems Manager features** do you use, and what IAM policy must the instance role have?

### Answers

#### 7 — Recovery with Auto Scaling

1. **Terminate** the compromised instance (Auto Scaling detects it as unhealthy).
2. Auto Scaling launches a **new instance from the launch template**, which references a **hardened Golden AMI**.
3. The Golden AMI includes:
   - Latest OS patches
   - SSM Agent pre-installed
   - CIS benchmark hardening
   - No hardcoded credentials
4. The new instance gets the **hardened Security Group** from the launch template (least-privilege, not the old permissive one).
5. **Validate** with Config rules (`ec2-instance-managed-by-systems-manager`, `ec2-security-group-attached-to-eni-periodic`) before routing production traffic.

**Key exam point:** Auto Scaling + Golden AMI = immutable infrastructure. You never patch a compromised instance — you replace it.

#### 8 — Three VPC-Level Controls

| Control | What it does | How it stops C2 |
|---------|-------------|-----------------|
| **NACL deny rule** | Add an explicit deny for the known C2 IP range at the subnet level | Blocks traffic before it reaches any instance in the subnet |
| **VPC Endpoints (Gateway)** | Route S3/DynamoDB traffic through AWS private network | Prevents data exfiltration via public S3 endpoints — traffic never leaves the VPC |
| **DNS Firewall (Route 53 Resolver)** | Block DNS resolution of known malicious domains | C2 often uses DNS for beaconing — if the domain doesn't resolve, the callback fails |

**Bonus:** Enable VPC Flow Logs (if not already) to detect future anomalous outbound patterns.

#### 9 — Systems Manager for Compliance

| Feature | Purpose |
|---------|---------|
| **SSM Patch Manager** | Automates OS and application patching on a schedule (patch baselines + maintenance windows) |
| **SSM State Manager** | Enforces desired state — ensures SSM Agent is running, specific configurations are applied, and drift is corrected automatically |

**Required IAM policy on the instance role:** `AmazonSSMManagedInstanceCore`

This managed policy grants the minimum permissions for:
- SSM Agent to communicate with the Systems Manager service
- Session Manager access
- Run Command execution
- Patch Manager operations

**Without this policy**, the instance won't appear in the Systems Manager console — it's the #1 troubleshooting step when SSM "can't find" an instance.

---

## Common Exam Traps

### EventBridge Rule Patterns

1. **`source` is the detecting service, not the affected service.** When Config finds a public S3 bucket, the source is `aws.config`, NOT `aws.s3`. The `source` field answers: "which service is talking to EventBridge?"
2. **`detail-type` for Config is `Config Rules Compliance Change`**, not `AWS API Call via CloudTrail`. The CloudTrail detail-type is for matching raw API calls — Config compliance events have their own detail-type.
3. **Compliance result is nested.** It's `detail.newEvaluationResult.complianceType`, not `detail.complianceType`. If you put it at the wrong level, the rule silently matches nothing.
4. **`source` is `aws.config`**, not `aws.configrules` — there is no `aws.configrules` source.

### EventBridge General

5. **"Enable EventBridge" is a distractor.** Every account has a default event bus that's always active. You only create rules — you never enable the bus itself.
6. **EventBridge vs CloudWatch Events** — they are the same service. CloudWatch Events was renamed to EventBridge. If the exam mentions either, treat them as identical.

### S3 Containment

7. **`PutPublicAccessBlock` is under `s3api`**, not `s3`. The command is `aws s3api put-public-access-block`, not `aws s3 block-public-access`.
8. **Block first, fix policy second.** `PutPublicAccessBlock` is an override layer — it neutralizes public access even if the bad policy is still there. Deleting the policy alone leaves a window where the attacker can re-apply it.

### IAM Eradication

9. **Don't delete the compromised IAM user immediately.** Deactivate access keys and revoke sessions first. Deleting the user destroys CloudTrail audit evidence tied to that identity.

### Containment Prioritization

10. **Contain the widest exposure first.** A public S3 bucket (exposed to the entire internet) takes priority over an EC2 instance talking to a single C2 IP. Blast radius determines order.

---

## Key Takeaways for the Exam

| Pattern | Remember |
|---------|----------|
| Containment priority | Widest exposure first |
| S3 remediation | `PutPublicAccessBlock` (override) + `PutBucketPolicy` (fix) |
| EC2 isolation | New empty SG, never modify existing |
| Automated pipeline | Config → EventBridge → SNS → Lambda |
| EventBridge | Always enabled, you only create rules |
| Recovery | Replace, don't repair (Golden AMI + Auto Scaling) |
| Network hardening | NACLs + VPC Endpoints + DNS Firewall |
| SSM prerequisite | `AmazonSSMManagedInstanceCore` on instance role |
