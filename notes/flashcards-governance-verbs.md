# RAM vs FM vs StackSets vs Service Catalog — Verb Map

> The exam tests verbs. Match the verb to the service INSTANTLY.

---

## The Verb Rule

| Verb in Question | Service | Never This |
|---|---|---|
| **Share / available / visible / accessible** | **RAM** | ❌ FM (FM enforces, doesn't share) |
| **Enforce / associate / re-associate / re-apply / auto-remediate** | **Firewall Manager** | ❌ RAM (RAM makes visible, doesn't enforce) |
| **Deploy resources / enable services / push infra** | **StackSets** | ❌ FM (FM only does firewall rules) |
| **Self-service / pull / provision / no broad IAM** | **Service Catalog** | ❌ StackSets (that's admin push) |
| **Prevent API call / block action / never happen** | **SCP** | ❌ Config (that's detect+fix) |
| **Detect + fix / remediate drift / check compliance** | **Config + SSM** | ❌ SCP (that's preventive) |
| **Validate template content before deploy** | **cfn-guard / Config proactive** | ❌ SCP (can't see template) |

---

## RAM + FM Work Together (DNS FW / Network FW)

```
Step 1: RAM shares rule group from security account → members can SEE it
Step 2: FM policy enforces association with VPCs → members MUST use it

RAM alone = visible but optional
FM alone = can't enforce what isn't visible
RAM + FM = visible AND mandatory
```

**Exception:** FM creates WAF and Shield directly (no RAM needed). FM only needs RAM for DNS Firewall and Network Firewall rule groups that exist in another account.

---

## What FM Can Manage (creates directly, no RAM)

| Policy Type | Needs RAM? |
|---|---|
| **WAF Web ACLs** | ❌ No — FM creates directly |
| **Shield Advanced** | ❌ No — FM creates directly |
| **Security Group (common)** | ❌ No — FM creates directly |
| **Security Group (audit)** | ❌ No — FM audits directly |
| **DNS Firewall** | ✅ Yes — RAM shares rule group first |
| **Network Firewall** | ✅ Yes — RAM shares policy first |

**The rule:** "Does the resource already exist in another account?" YES = RAM first. NO (FM creates it) = no RAM needed.

---

## StackSets vs Native Delegated Admin

| Service | Use StackSets? | Why |
|---|---|---|
| GuardDuty | ❌ No | Native delegated admin + auto-enable |
| Inspector | ❌ No | Native delegated admin + auto-enable |
| Security Hub | ❌ No | Native delegated admin + auto-enable |
| Macie | ❌ No | Native delegated admin + auto-enable |
| Detective | ❌ No | Native delegated admin + auto-enable |
| Config | ❌ No | Native delegated admin + auto-enable |
| **Custom IAM roles** | ✅ Yes | No native mechanism |
| **Custom Lambda functions** | ✅ Yes | No native mechanism |
| **Custom CloudWatch alarms** | ✅ Yes | No native mechanism |
| **Multiple services together** | ✅ Mix | Native for each + StackSets for custom resources |

**Rule:** If the service has native org-wide deployment → use native. StackSets = custom resources only.

---

## StackSets Limitations

| Can Do | Cannot Do |
|---|---|
| Deploy any CF resource | ❌ Auto-remediate drift |
| Auto-deploy to new accounts (service-managed) | ❌ Share existing resources (that's RAM) |
| Target OUs | ❌ Enforce lifecycle (that's FM) |

---

## Quick Fire Decision

```
"Share TGW/subnet/DNS FW rule group" → RAM
"Enforce WAF on all ALBs + re-apply" → FM (no RAM needed)
"Enforce DNS FW on all VPCs + re-associate" → RAM + FM
"Deploy GuardDuty 200 accounts" → Native delegated admin
"Deploy custom IAM role 200 accounts" → StackSets
"Self-service VPC, dev has no ec2:CreateVpc" → Service Catalog
"Block RunInstances without tag" → SCP
"Detect unencrypted EBS + fix" → Config + SSM remediation
```
