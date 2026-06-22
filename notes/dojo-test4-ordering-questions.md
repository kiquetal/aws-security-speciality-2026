# Dojo Test 4 — Ordering Questions (Review Later)

## Q: Security Hub CSPM Multi-Account Setup (Order 4 Steps)

**Steps (to arrange):**
- A: Set up the Security Hub administrator the ability to assume AWS IAM roles across member accounts.
- B: Turn on GuardDuty and Security Hub in each member account and configure AWS IAM trust permissions to allow management by the administrator account.
- C: Assign the security account as the central administrator for Security Hub.
- D: Activate AWS Security Hub within the designated security account.

**Correct Order:** D → C → B → A

**Logic:** Enable locally → Designate admin → Enable in members → Cross-account access

| Step | Why This Order |
|------|---------------|
| 1. Activate Security Hub in security account (D) | Service must EXIST in admin account before it can be designated admin |
| 2. Assign security account as central admin (C) | Now it has SH running, can become delegated admin |
| 3. Enable SH+GD in members + trust permissions (B) | Members need the services running + trust the admin |
| 4. Set up cross-account role assumption (A) | Admin assumes roles into members for management |

**Mnemonic:** "Enable → Designate → Members → Access" (E-D-M-A)

**Key insight:** You can't designate a delegated admin for a service unless that service is ALREADY enabled in the admin account.

---

## Notes on Ordering Questions (New in SCS-C03)

- SCS-C03 introduced ordering question types (didn't exist in C02)
- Think in logical dependency chains: what MUST exist before the next step can work?
- Common patterns:
  - Delegated admin → cross-account access → enable services → configure features
  - Create resource → configure resource → attach to target → verify
  - Contain → Acquire → Investigate → Report (IR sequence)
