# FAQ: IR Forensics Tools (Operational Details)

> **Blueprint refs:** Task 2.1 (IR plans), Task 2.2 (respond to events)
> **Purpose:** Exact tool selection for forensics scenarios. Dojo tests specific tools, not just concepts.

---

## Evidence Collection Decision Tree

```
┌─────────────────────────────────────────────────────────────────┐
│  WHAT EVIDENCE DO YOU NEED?                                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  DISK (files, logs, malware):                                    │
│  → EBS Snapshot (point-in-time, instance keeps running)          │
│                                                                  │
│  VOLATILE MEMORY (processes, network conns, kernel modules):     │
│  → No-reboot AMI (captures RAM state without stopping)           │
│                                                                  │
│  NETWORK TRAFFIC (what came in/out):                             │
│  → VPC Flow Logs (already flowing, check existing)               │
│                                                                  │
│  API ACTIVITY (who did what):                                    │
│  → CloudTrail (already logged, query via Lake/Athena)            │
│                                                                  │
│  BLAST RADIUS (what else was touched):                           │
│  → Detective (timeline, related entities, visualizations)        │
│                                                                  │
│  WINDOWS BOOT ISSUE + MEMORY DUMPS:                              │
│  → EC2Rescue for Windows (standalone diagnostic tool)            │
│                                                                  │
│  LAMBDA FORENSICS:                                               │
│  → CloudWatch Logs + X-Ray traces + GuardDuty findings           │
│  → NO EBS, NO AMI (Lambda is ephemeral)                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## EC2Rescue — When and Why

```
┌─────────────────────────────────────────────────────────────────┐
│  EC2Rescue for Windows Server                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  USE WHEN: OS won't boot / can't RDP / need memory dumps         │
│                                                                  │
│  HOW IT WORKS:                                                   │
│  1. Detach EBS volume from broken instance                       │
│  2. Attach to a healthy "rescue" instance                        │
│  3. Run EC2Rescue against the attached volume                    │
│  4. Collects: memory dumps, event logs, crash data               │
│  5. Can also attempt OS repair                                   │
│                                                                  │
│  KEY POINT: Works OFFLINE (doesn't need running OS)              │
│                                                                  │
│  WHY NOT SSM?                                                    │
│  → SSM agent requires a RUNNING OS                               │
│  → If instance won't boot, SSM is useless                        │
│  → EC2Rescue works on the volume directly                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

EC2Rescue for Linux:
  → Same concept: diagnose boot issues, collect logs
  → Works on detached volumes
```

### Decision

| Scenario | Tool |
|---|---|
| Instance running, need memory | No-reboot AMI |
| Instance running, need disk | EBS Snapshot |
| Instance WON'T BOOT, need diagnostics | EC2Rescue (detach volume, analyze offline) |
| Instance won't boot, need SSM | IMPOSSIBLE (SSM needs running OS) |

---

## Session Manager Logging vs CloudWatch Agent

```
┌─────────────────────────────────────────────────────────────────┐
│  TWO DIFFERENT THINGS — DON'T CONFUSE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  SESSION MANAGER LOGGING:                                        │
│  ═════════════════════════                                       │
│  WHAT: Records the SESSION itself (keystrokes, commands, output) │
│  HOW:  Enable "upload session logs" in Session Manager prefs     │
│  DEST: CloudWatch Logs OR S3 (you choose)                        │
│  USE:  "Record/monitor admin session activity"                   │
│  ENCRYPTION: Optional KMS encryption on the log group/bucket     │
│                                                                  │
│  CLOUDWATCH AGENT:                                               │
│  ════════════════                                                │
│  WHAT: Collects OS-level logs (syslog, app logs, custom logs)    │
│  HOW:  Install agent + configure which log files to ship         │
│  DEST: CloudWatch Logs                                           │
│  USE:  "Collect application/OS logs from instances"              │
│  NOTE: Knows NOTHING about Session Manager sessions              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Decision

| Question says... | Answer |
|---|---|
| "Record session activity / keystrokes" | Session Manager logging (built-in) |
| "Monitor encrypted session logs" | Session Manager logging + encrypted destination |
| "Collect application logs" | CloudWatch Agent |
| "Collect OS syslog" | CloudWatch Agent |
| "Session Manager + logging, LEAST effort" | Session Manager preferences → enable upload |

> **Exam trap:** "Record all encrypted session activity logs" ≠ CloudWatch Agent. It's Session Manager's native "upload session logs" feature with encrypted CW Logs group.

---

## No-Reboot AMI — Why It Matters

```
Regular AMI:     Stop → Snapshot → Start
                 ❌ Memory LOST on stop (volatile = gone)

No-reboot AMI:   Snapshot while RUNNING
                 ✅ Memory state preserved in the image
                 ✅ Instance never stops
                 ⚠️ Filesystem may not be perfectly consistent

dd /dev/mem:     ❌ Restricted on modern Amazon Linux 2+ kernels
                 Not the AWS-recommended approach
```

### Rule

| Need | Method |
|---|---|
| Volatile memory (RAM) | No-reboot AMI |
| Disk evidence | EBS Snapshot |
| Both memory + disk | No-reboot AMI + EBS Snapshot (two actions) |
| Windows memory dump + boot issue | EC2Rescue for Windows |

---

## Lambda Forensics — What You CAN'T Do

```
Lambda = EPHEMERAL. No persistent storage.

  ❌ EBS Snapshot (Lambda has no EBS)
  ❌ No-reboot AMI (Lambda has no AMI)
  ❌ Attach volume to rescue instance (no volume)
  ❌ SSM RunCommand (no persistent OS)

  ✅ CloudWatch Logs (function output, errors)
  ✅ X-Ray traces (invocation chain)
  ✅ GuardDuty findings (behavioral detection)
  ✅ CloudTrail (API calls the function made)
```

> **Exam trap:** "Preserve forensic evidence from Lambda" — if EBS snapshot is an option, it's WRONG.

---

## 🧠 Cheat-Sheet One-Liners

- **"Windows boot issue + memory dump" = EC2Rescue (works offline). SSM needs running OS.**
- **"Record session activity" = Session Manager logging (built-in). NOT CloudWatch Agent.**
- **CloudWatch Agent = OS/app logs. Session Manager logging = session keystrokes/commands. Different.**
- **Lambda = no EBS, no AMI, no disk forensics. Evidence = CW Logs + X-Ray + CloudTrail + GD findings.**
- **No-reboot AMI = volatile memory. EBS Snapshot = disk. Need both = two separate actions.**
