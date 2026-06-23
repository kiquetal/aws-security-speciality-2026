# Config Proactive vs SCP vs cfn-guard — Template Validation

> "SCP sees the ENVELOPE (API call). Config proactive sees the CONTENTS (resource properties)."

---

## What Each Layer Can See

| Layer | Sees API Call? | Sees Template Text? | Sees Resource Properties? | Can Block? | Bypassable? |
|---|---|---|---|---|---|
| **SCP** | ✅ | ❌ | ❌ | ✅ (blocks API) | ❌ Never |
| **cfn-guard** | ❌ | ✅ | ✅ | ✅ (CI/CD only) | ✅ Console/CLI bypass |
| **Config proactive** | ❌ | ❌ | ✅ | ✅ (CF service level) | ❌ Never (catches all CF) |
| **CF Hook** | ❌ | ❌ | ✅ | ✅ (CF service level) | ❌ Never (same as proactive) |
| **Config detective** | ❌ | ❌ | ✅ | ❌ (detect after) | N/A |

---

## SCP Can Check vs Cannot Check

### ✅ SCP CAN (these are API request parameters)

- `ec2:MetadataHttpTokens` = required (IMDSv2)
- `aws:RequestTag/CostCenter` exists (tagging)
- `s3:x-amz-server-side-encryption` = aws:kms (encryption header)
- `kms:ViaService` = s3.us-east-1 (restrict direct KMS)
- `ec2:Encrypted` = true (EBS encryption)

### ❌ SCP CANNOT (these are inside CF template, not API params)

- RDS `StorageEncrypted: true`
- RDS `DeletionProtection: true`
- S3 `VersioningConfiguration`
- Lambda `ReservedConcurrentExecutions`
- Any resource property only visible inside CloudFormation template

---

## Decision Table

| Question Asks | Answer | Why |
|---|---|---|
| "Block RunInstances without IMDSv2" | **SCP** | MetadataHttpTokens = API request param |
| "Block EBS without encryption" | **SCP** | ec2:Encrypted = API request param |
| "Block PutObject without KMS header" | **SCP / Bucket Policy** | Encryption header = request param |
| "Block CF template without DeletionProtection" | **Config proactive** | Resource property inside template |
| "Block CF template without StorageEncrypted" | **Config proactive** | Resource property inside template |
| "Validate template in CI/CD pipeline" | **cfn-guard** | Shift-left, cheapest |
| "Catch ALL CF deployments (Console+CLI+SDK)" | **Config proactive** | CF service-level, can't bypass |
| "Developer bypasses pipeline via Console" | **Config proactive catches it** | cfn-guard missed it |

---

## How Config Proactive Works

```
ANY CloudFormation deployment (Console/CLI/SDK/Terraform-via-CF)
        │
        ▼
CloudFormation Service
        │
        ▼ BEFORE creating resource
Config Proactive Rule evaluates RESOURCE PROPERTIES
        │
    ┌───┴───┐
    │       │
    ✅       ❌
 Create    Stack FAILS
 resource  (resource never exists)
```

Enable: Config → Rules → Add Rule → Choose "Proactive" evaluation mode → Select managed rule.

---

## The Trap Pattern

```
Question: "Ensure no RDS without encryption is EVER deployed via CloudFormation"
Trap answer: SCP (can't see inside template... BUT check if it's also an API param!)
If StorageEncrypted is an API param → SCP works for ALL paths (not just CF)
If it's ONLY in CF template → Config proactive is the only option for CF path

Question: "Ensure no EC2 without IMDSv2 is EVER launched"  
Correct: SCP (MetadataHttpTokens IS an API request parameter → covers ALL paths)
Config proactive also works for CF, but SCP is broader

Question: "Catch ALL CF deployments (Console+CLI+SDK CF deploys)"
Correct: Config proactive (CF service-level)
Wrong: cfn-guard (CI/CD only, bypassable)
```

## CRITICAL SCOPE REMINDER

```
Config proactive = ONLY evaluates CloudFormation deployments
                   Does NOT catch: direct CLI/SDK API calls outside CF
                   
SCP = evaluates ALL API calls regardless of trigger
      (CF, CLI, SDK, Console, Terraform, everything)

IF the property is an API request parameter:
  → SCP alone covers ALL paths (including CF)
  → Config proactive is redundant (but adds defense-in-depth)

IF the property is ONLY visible inside CF template (not an API param):
  → SCP can't help
  → Config proactive is the ONLY preventive option for CF path
  → Direct API path needs Config detective + remediation (after-the-fact)
```
