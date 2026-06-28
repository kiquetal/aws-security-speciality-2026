# Flashcards: D6 Governance — StackSets vs Conformance Packs vs Control Tower

> Created: 2026-06-27. Review before every D6 drill.

---

## Card 1: StackSets

**Q:** StackSets auto-deploy vs auto-remediate — what's the difference?

<details><summary>Answer</summary>

- **Auto-deploy** = new account joins OU → stack deployed ✅
- **Auto-remediate** = someone changes a resource → StackSets fixes it ❌ NEVER

StackSets handles new accounts but IGNORES runtime drift.

</details>

---

## Card 2: Conformance Packs

**Q:** Does a conformance pack auto-remediate?

<details><summary>Answer</summary>

The PACK = just a container (deploys rules). The RULES INSIDE can have SSM remediation attached. So it LOOKS like the pack remediates, but technically Config rule + SSM does the work. The pack is just packaging.

</details>

---

## Card 3: StackSets vs Conformance Pack

**Q:** "Deploy GuardDuty + Config + IAM roles" vs "Bundle 20 encryption checks + auto-fix" — which service?

<details><summary>Answer</summary>

- Deploy services/resources = **StackSets** (any CF resource)
- Bundle compliance checks + remediation = **Conformance pack** (Config rules only)

</details>

---

## Card 4: Control Tower CAN vs CAN'T

**Q:** Can Control Tower: (a) auto-revert drift? (b) support custom SCPs? (c) deploy WAF rules?

<details><summary>Answer</summary>

- (a) ❌ Detects drift, does NOT auto-revert (manual fix)
- (b) ✅ Custom SCPs, Config rules, and CF Hooks all supported
- (c) ❌ WAF = Firewall Manager's job

</details>

---

## Card 5: Control Tower Custom Controls

**Q:** What three types of custom controls does Control Tower support?

<details><summary>Answer</summary>

1. **Preventive** = custom SCP
2. **Detective** = custom Config rule
3. **Proactive** = custom CF Hook

</details>

---

## Card 6: Stack Policy Default

**Q:** Stack Policy has no Allow statements. Developer tries Update:Modify. Result?

<details><summary>Answer</summary>

**FAILS.** Stack Policy = default deny all. No Allow = nothing passes. Must explicitly Allow actions (opposite intuition from "no policy = allow all").

</details>

---

## Card 7: Security Hub Standards

**Q:** Security Hub enabled but 0% compliance everywhere. Config is running. Why?

<details><summary>Answer</summary>

**Standards not enabled.** Enabling Security Hub ≠ enabling standards. Must explicitly enable FSBP/CIS/PCI/NIST after setup. No standards = no checks = 0%.

</details>

---

## Card 8: Service Catalog Post-Deploy

**Q:** Service Catalog provisions VPC. Developer disables flow logs 2 weeks later. Does SC catch it?

<details><summary>Answer</summary>

**No.** Service Catalog = deploy and forget. Zero post-provisioning monitoring. Fix = Config + SSM.

</details>

---

## Card 9: cfn-guard Limitations

**Q:** cfn-guard rule checks `StorageEncrypted: true`. Template has `StorageEncrypted: !Ref Param`. Result?

<details><summary>Answer</summary>

**FAIL.** cfn-guard = static text analysis. Sees `{"Ref": "Param"}`, not the resolved value. Can't resolve parameters, conditions, or intrinsic functions.

</details>

---

## Card 10: RAM Shared Resources — Ownership

**Q:** RAM shares TGW. Member creates attachment. Member deletes attachment. Allowed?

<details><summary>Answer</summary>

**Yes.** RAM shares the parent resource (TGW = owner's). Attachment created BY member = member-owned. Members control their own resources.

</details>
