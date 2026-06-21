# FAQ: AWS Well-Architected Tool

> **Blueprint ref:** Task 6.3 (evaluate compliance with AWS security best practices)
> **Exam trap frequency:** High — confused with Audit Manager, Security Hub, Config

---

## What It Does (One Sentence)

Manual architecture review against AWS best practices → generates prioritized improvement plan → tracks progress via milestones.

---

## Milestones — The Exam-Critical Feature

### What a Milestone IS
- A **snapshot** of your workload review at a point in time
- Captures: all answers, risk levels (HRI/MRI/NRI), notes, improvement plan status
- Immutable once saved — represents "state at this date"
- Created manually (no auto-creation)

### What Milestone Comparison SHOWS
| Visible in comparison | Example |
|---|---|
| ✅ HRI/MRI/NRI count per milestone | 8 HRI → 3 HRI |
| ✅ Per-question risk level changes | Q7 moved from High Risk to No Risk |
| ✅ Pillar-level risk summary | Security Pillar: 4 HRI → 1 HRI |
| ✅ Date/time of each milestone | Jan 15 vs Apr 15 |
| ✅ Improvement plan items (open/resolved) | 12 items → 5 items |

### What Milestone Comparison DOES NOT SHOW
| NOT available | Why |
|---|---|
| ❌ Automated evidence (Config, CloudTrail) | WAT is self-reported, not verified |
| ❌ Compliance scores | No numerical scoring system |
| ❌ Auto-resolution of items | Manual review only |
| ❌ Integration with Security Hub findings | Separate tools, no link |
| ❌ Root cause of improvement | Just shows state changed, not how |

---

## WAT vs Audit Manager vs Security Hub

| Question | Answer | NOT this |
|---|---|---|
| "Architectural gaps + improvement plan + track progress" | **Well-Architected Tool** | ❌ Audit Manager (evidence collection) |
| "Collect evidence for SOC 2 audit" | **Audit Manager** | ❌ WAT (no evidence) |
| "CIS compliance dashboard + aggregate findings" | **Security Hub** | ❌ WAT (no automation) |
| "Prove to auditor we improved over 3 quarters" | **WAT milestones** | ❌ Audit Manager (framework evidence, not architectural review) |
| "Download AWS's ISO 27001 report" | **Artifact** | ❌ Everything else |

---

## Operational Details (Exam Gotchas)

| Gotcha | Detail |
|---|---|
| **No automation** | WAT doesn't connect to Config, SH, or any service for auto-updates |
| **Self-reported** | Answers are YOUR assessment — no verification |
| **Pillars** | Operational Excellence, Security, Reliability, Performance, Cost, Sustainability |
| **Lenses** | Custom lenses available (SaaS, Serverless, etc.) |
| **Sharing** | Workloads can be shared with other accounts (for consulting) |
| **Free** | No cost for the tool itself |
| **Milestones are immutable** | Can't edit a saved milestone — create a new one |
| **Max milestones** | No practical limit documented |

---

## Stack Policy (Related — Same Session Trap)

Since Stack Policy also came up in the same session:

| Dimension | Stack Policy | Termination Protection |
|---|---|---|
| **Protects against** | Resource modification/replacement/deletion INSIDE stack | Stack deletion |
| **Default** | Implicit deny on all Update actions | Disabled |
| **Override** | Temporary override with `--stack-policy-during-update-body` | Must disable explicitly |
| **Scope** | Per-resource within the stack | Entire stack |

**Stack Policy evaluation:**
- No explicit Allow = implicitly denied (like SCP)
- Pattern: Allow `Update:*` on all → Deny specific dangerous actions on sensitive resources
- `Update:Modify` = in-place change (no new physical ID)
- `Update:Replace` = new physical resource created (new ID)
- `Update:Delete` = resource removed from stack

---

## 🧠 Cheat-Sheet One-Liners

- WAT = manual architecture review + improvement plan + milestones for tracking progress. NO automation.
- WAT milestones = immutable snapshots. Compare = see risk reduction. NO evidence, NO Config, NO auto-fix.
- "Track architectural improvement over time" = WAT milestones. "Collect compliance evidence" = Audit Manager.
- WAT is FREE. Audit Manager costs money (evidence collection).
- Stack Policy default = implicit deny. Start with Allow *, then Deny dangerous actions on sensitive resources.
