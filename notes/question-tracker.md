# SCS-C03 Question Tracker

> Track every question attempted. Review ❌ and ⚠️ items before the exam.

---

## Quick Stats (Cumulative)

| Metric | Value |
|---|---|
| **Total Questions** | 0 |
| **✅ Correct** | 0 (0%) |
| **⚠️ Partial** | 0 (0%) |
| **❌ Wrong** | 0 (0%) |
| **Sessions** | 0 |
| **Re-tests Passed** | 0 of 0 |

## Domain Breakdown

| Domain | Exam Weight | ✅ | ⚠️ | ❌ | Total | Score % | Weak? |
|---|---|---|---|---|---|---|---|
| D1: Detection | 16% | 0 | 0 | 0 | 0 | 0% | 🔴 |
| D2: Incident Response | 14% | 0 | 0 | 0 | 0 | 0% | 🔴 |
| D3: Infrastructure Security | 18% | 0 | 0 | 0 | 0 | 0% | 🔴 |
| D4: Identity & Access Management | 20% | 0 | 0 | 0 | 0 | 0% | 🔴 |
| D5: Data Protection | 18% | 0 | 0 | 0 | 0 | 0% | 🔴 |
| D6: Governance | 14% | 0 | 0 | 0 | 0 | 0% | 🔴 |

Legend: 🔴 < 50% — 🟡 50–79% — 🟢 ≥ 80%

## Weak Areas to Review

| Priority | Topic | Questions | Domain | Count |
|---|---|---|---|---|

---

| 1227 | D4/D6 | RCP on S3, ELB SLR writes access logs — succeeds or fails? | B | ✅ | Succeeds — SLRs exempt from RCPs | — | RCP SLR exemption |
| 1228 | D5 | EC2 encrypted EBS won't start, role has kms:Decrypt — missing? | B | ✅ | kms:CreateGrant | — | EC2 EBS always needs CreateGrant |
| 1229 | D1 | CryptoCurrency:EC2/BitcoinTool.B — detection method? | B | ✅ | Active TCP to mining pool (not DNS) | — | GD finding type = detection method |
| 1230 | D5 | CRR SSE-KMS replication role — three permissions? | B | ✅ | Decrypt source + GenerateDataKey dest + GetObjectVersionForReplication | — | CRR D-G-F |
| 1231 | D2 | IAM user creds on GitHub, 2 keys + console + STS — first containment? | B | ❌ | A: Deactivate key + inline Deny * on user (covers ALL paths) | — | User = Deny *. Role = TokenIssueTime. |
