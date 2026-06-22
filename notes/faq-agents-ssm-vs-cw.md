# FAQ: SSM Agent vs CloudWatch Agent — What Each Does

> **Exam trap:** They're TWO different agents. SSM agent CAN install CW agent (via Run Command), but SSM agent itself CANNOT ship logs.

---

## Side-by-Side

| Dimension | SSM Agent | CloudWatch Agent |
|---|---|---|
| **Primary job** | Execute commands, sessions, patching | Ship logs + custom metrics |
| **Ships custom log files?** | ❌ NO | ✅ YES |
| **Ships OS/app metrics?** | ❌ NO | ✅ YES (memory, disk, etc.) |
| **Remote shell access?** | ✅ Session Manager | ❌ NO |
| **Run scripts remotely?** | ✅ Run Command | ❌ NO |
| **Patch instances?** | ✅ Patch Manager | ❌ NO |
| **Desired-state enforcement?** | ✅ State Manager | ❌ NO |
| **Pre-installed on Amazon Linux 2+?** | ✅ YES | ❌ NO (must install) |
| **Can install the other agent?** | ✅ SSM can install CW agent | ❌ CW agent can't install SSM |

---

## The Relationship

```
SSM Agent (pre-installed)
  │
  ├── Run Command: "install CW agent" (AmazonCloudWatch-ManageAgent document)
  │         │
  │         ▼
  │    CloudWatch Agent (now installed)
  │         │
  │         └── Ships /var/log/app.log → CloudWatch Logs
  │         └── Ships custom metrics → CloudWatch Metrics
  │
  ├── Session Manager: interactive shell (no SSH needed)
  ├── Patch Manager: apply OS patches
  └── State Manager: enforce desired config on schedule
```

**SSM agent can INSTALL the CW agent, but cannot REPLACE it for log shipping.**

---

## Exam Decision Table

| Question says... | Answer |
|---|---|
| "Ship custom log files to CloudWatch Logs" | **CloudWatch agent** |
| "Send OS metrics (memory, disk) to CloudWatch" | **CloudWatch agent** |
| "Access instance without SSH/RDP" | **SSM agent** (Session Manager) |
| "Run script across 500 instances" | **SSM agent** (Run Command) |
| "Install software on all instances" | **SSM agent** (Run Command or State Manager) |
| "Ensure CW agent always installed + configured" | **SSM State Manager** (installs/configures CW agent) |
| "Troubleshoot: logs stopped flowing" | Check **CW agent** config (`/var/log/amazon/amazon-cloudwatch-agent/`) |
| "Troubleshoot: can't connect via Session Manager" | Check **SSM agent** + VPC endpoints + SG outbound 443 |

---

## Common Exam Traps

1. **"SSM agent sends logs to CloudWatch"** — WRONG. SSM agent manages the instance; CW agent ships logs.
2. **"Install CW agent via SSM"** — CORRECT. SSM Run Command or State Manager can deploy and configure the CW agent.
3. **"Athena queries CloudWatch Logs"** — WRONG. Athena queries S3. Use CloudWatch Logs Insights for CW Logs.
4. **"Session Manager logging = CW agent"** — WRONG. Session Manager has its own built-in session logging feature (uploads to CW Logs or S3 directly). CW agent is for app/OS logs.

---

## 🧠 Cheat-Sheet One-Liners

- SSM agent = execute commands, sessions, patches. CW agent = ship logs + metrics. Different agents, different jobs.
- "Ship custom logs to CW Logs" = always CW agent. SSM agent cannot do this.
- SSM can INSTALL CW agent (Run Command / State Manager), but can't REPLACE it.
- Athena queries S3, not CW Logs. CW Logs Insights queries CW Logs.
