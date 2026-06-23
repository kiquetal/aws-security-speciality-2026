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
Trap answer: SCP (can't see inside template)
Correct: Config proactive (evaluates resource properties at CF service level)

Question: "Ensure no EC2 without IMDSv2 is EVER launched"  
Correct: SCP (MetadataHttpTokens IS an API request parameter)
Trap: Config proactive (works too, but SCP is simpler and preventive for ALL paths, not just CF)
```
