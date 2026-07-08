# cfn-guard — How It Actually Works

> Source: AWS official docs (docs.aws.amazon.com/cfn-guard/latest/ug/)
> Failed 3x in Session 119 (Q4, Q17, Q5 re-test). Lock this.

---

## What cfn-guard IS

```
cfn-guard = a STATIC TEXT ANALYSIS tool.

It reads a JSON or YAML FILE and checks values against rules you write.
It does NOT execute CloudFormation. It does NOT resolve anything.
It's like running a regex/grep against your template file.
```

From AWS docs:
> "Guard doesn't validate CloudFormation templates for valid syntax or 
>  allowed property values."
> "Guard doesn't provide server-side enforcement."

---

## What cfn-guard Sees

cfn-guard reads the template file AS-IS. It sees exactly what's in the file text.

```yaml
# EXAMPLE TEMPLATE:
Parameters:
  EncryptParam:
    Type: String
    Default: true
    AllowedValues: [true, false]

Resources:
  MyRDS:
    Type: AWS::RDS::DBInstance
    Properties:
      StorageEncrypted: !Ref EncryptParam    # ← what does cfn-guard see?
```

**What cfn-guard sees for `StorageEncrypted`:**

```json
{"Ref": "EncryptParam"}
```

It does NOT see `true`. It sees a JSON object with a key "Ref".

---

## The Rule: Intrinsic Functions = Opaque Objects

cfn-guard treats ALL CloudFormation intrinsic functions as opaque data structures:

| Template text | What cfn-guard sees | Can it evaluate? |
|---|---|---|
| `StorageEncrypted: true` | `true` (boolean) | ✅ YES |
| `StorageEncrypted: "true"` | `"true"` (string) | ✅ YES |
| `StorageEncrypted: !Ref Param` | `{"Ref": "Param"}` (object) | ❌ NO |
| `StorageEncrypted: !If [Cond, true, false]` | `{"Fn::If": ["Cond", true, false]}` (object) | ❌ NO |
| `Engine: !Sub "${Var}-mysql"` | `{"Fn::Sub": "${Var}-mysql"}` (object) | ❌ NO |
| `Arn: !GetAtt Res.Arn` | `{"Fn::GetAtt": ["Res", "Arn"]}` (object) | ❌ NO |

**cfn-guard does NOT:**
- Resolve `!Ref` to parameter values or resource IDs
- Evaluate `!If` conditions
- Substitute `!Sub` variables
- Look at the Parameters section's `AllowedValues`
- Know about the `Default` value of parameters

---

## What Happens When cfn-guard Encounters an Intrinsic

Given this rule:
```
AWS::RDS::DBInstance {
    Properties.StorageEncrypted == true
}
```

| Template value | Comparison | Result |
|---|---|---|
| `StorageEncrypted: true` | `true == true` | ✅ PASS |
| `StorageEncrypted: false` | `false == true` | ❌ FAIL |
| `StorageEncrypted: !Ref X` | `{"Ref":"X"} == true` | ❌ FAIL (object ≠ boolean) |
| `StorageEncrypted: !If [C, true, false]` | `{"Fn::If":[...]} == true` | ❌ FAIL (object ≠ boolean) |

The comparison fails because you're comparing a JSON object against a boolean literal. They're different types.

---

## But Wait — Does This Mean cfn-guard Is Useless for Parameterized Templates?

**Not entirely.** You can write rules that CHECK the intrinsic structure:

```
# Rule: If StorageEncrypted uses !Ref, check it refs an approved parameter
AWS::RDS::DBInstance when Properties.StorageEncrypted is_struct {
    Properties.StorageEncrypted.Ref == "ApprovedEncryptionParam"
}

# Rule: If StorageEncrypted is a literal, it must be true
AWS::RDS::DBInstance when Properties.StorageEncrypted is_bool {
    Properties.StorageEncrypted == true
}
```

But this is advanced usage that most teams don't implement. For the exam, the simple rule applies.

---

## The Exam-Day Rule (Simple Version)

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│  cfn-guard rule checks: Property == <literal value>              │
│                                                                  │
│  Template has LITERAL value  → cfn-guard CAN compare → PASS/FAIL│
│  Template has ANY intrinsic  → comparison fails      → FAIL     │
│                                                                  │
│  This includes: !Ref, !If, !Sub, !Select, !GetAtt,             │
│                 !Join, Fn::ImportValue, !Split                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## cfn-guard vs CloudFormation's Own Validation

These are DIFFERENT validation layers:

| Validation | When | What it checks | Can resolve intrinsics? |
|---|---|---|---|
| **cfn-guard** | In your CI/CD pipeline | Your custom rules against template text | ❌ NO |
| **CF AllowedValues** | At deploy time (CF service) | Parameter value against the AllowedValues list | ✅ YES (CF resolves everything) |
| **Config proactive** | At deploy time (CF service) | Resource properties after resolution | ✅ YES (sees resolved values) |
| **CF Hook** | At deploy time (CF service) | Resource properties after resolution | ✅ YES (sees resolved values) |

### Example showing both layers:

```yaml
Parameters:
  DBEngine:
    Type: String
    Default: aurora-mysql
    AllowedValues:          # ← CloudFormation enforces this AT DEPLOY TIME
      - aurora-mysql
      - aurora-postgresql

Resources:
  MyDB:
    Type: AWS::RDS::DBInstance
    Properties:
      Engine: !Ref DBEngine   # ← cfn-guard sees {"Ref":"DBEngine"}, can't validate
```

**cfn-guard:** Sees `{"Ref": "DBEngine"}` for Engine property. If rule checks `Engine == "aurora-mysql"` → FAIL (object ≠ string). cfn-guard CANNOT validate this template.

**CloudFormation (at deploy time):** If someone passes `--parameter-overrides DBEngine=mysql` → CF rejects it because `mysql` is NOT in AllowedValues. CF's own validation works independently of cfn-guard.

**Key insight:** The template has TWO safety nets even though cfn-guard can't help:
1. `AllowedValues` in the Parameters section (CF enforces at deploy)
2. Config proactive (evaluates resolved properties at deploy)

---

## Short-Form vs Long-Form (AWS Docs Gotcha)

From AWS troubleshooting docs:
> "Guard doesn't support the short forms of intrinsic functions. For example, 
>  using !Join, !Sub in a YAML-formatted CloudFormation template isn't supported.
>  Instead, use the expanded forms (Fn::Join, Fn::Sub)."

This means cfn-guard has trouble even PARSING short-form YAML intrinsics in some versions. The expanded form works for STRUCTURAL analysis (checking which intrinsic is used), but still can't RESOLVE the value.

---

## WHERE cfn-guard Runs (Client-Side, Not Server-Side)

```
cfn-guard = a CLI binary. It runs wherever YOU put it:
  - In a CI/CD pipeline (typical)
  - On a developer's laptop (also valid)
  - In a pre-commit hook
  - Anywhere you can run a command

It is NOT a server-side gate. CloudFormation does not run cfn-guard.
```

### What This Means for Security

| Scenario | cfn-guard validates? | CF deploys correctly? | GAP? |
|---|---|---|---|
| Pipeline validates → pipeline deploys (same artifact) | ✅ | ✅ | ❌ No gap |
| Developer runs cfn-guard locally → deploys same file | ✅ | ✅ | ❌ No gap |
| Pipeline validates → developer deploys DIFFERENT file via CLI | ✅ (old file) | ✅ (new file) | ✅ GAP! |
| Developer deploys via Console CF (no pipeline) | ❌ Never ran | ✅ | ✅ BYPASSED |
| Developer deploys via Terraform (direct API) | ❌ Irrelevant | N/A (no CF) | ✅ BYPASSED |

### The Key Distinction (Exam-Critical)

```
cfn-guard = CLIENT-SIDE validation (your pipeline/laptop)
  → Bypassable: deploy from Console, CLI without pipeline, or Terraform
  → No enforcement if developer doesn't go through the pipeline

Config proactive = SERVER-SIDE validation (inside CloudFormation service)
  → NOT bypassable for CF deploys: Console, CLI, SDK — all caught
  → Still blind to non-CF deployments (Terraform, direct API)

SCP = SERVER-SIDE validation (inside IAM/Organizations)
  → NOT bypassable for ANY deployment path
  → But can only see API request parameters, not template content
```

**For the exam:**
- "Developer bypasses pipeline" → cfn-guard misses it, Config proactive catches it
- "Hardcoded value + same file deployed" → cfn-guard validation is trustworthy
- "Developer could edit file after cfn-guard ran" → gap exists (no server-side enforcement without Config proactive)

---

## 🧠 Exam One-Liners

- **cfn-guard = static text analysis. Sees the file, not resolved values.**
- **cfn-guard = CLIENT-SIDE (pipeline/laptop). Config proactive = SERVER-SIDE (CF service). Different enforcement points.**
- **ANY intrinsic (!Ref, !If, !Sub, etc.) = cfn-guard sees a JSON object, not the resolved value.**
- **Rule `Property == true` + template has `!Ref X` → FAIL (object ≠ boolean).**
- **cfn-guard can't read Parameters/AllowedValues to validate Refs. It's not that smart.**
- **CloudFormation's OWN AllowedValues still enforces at deploy time — separate from cfn-guard.**
- **Config proactive + CF Hooks see RESOLVED values (they run inside CF service). cfn-guard does not.**
- **"Developer bypasses pipeline" = cfn-guard blind. Config proactive catches. SCP catches API params.**
