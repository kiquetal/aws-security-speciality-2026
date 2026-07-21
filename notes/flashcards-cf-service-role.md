# CloudFormation Service Role — Deep Dive Flashcard

> Failed: Udemy Q35. Pattern never re-tested in 119 sessions.
> This is a D6 + D4 cross-domain pattern (Task 6.2 + Task 4.2).

---

## The Problem

```
WITHOUT service role:

  Developer A (role: has ec2:*, s3:*, lambda:*)
    → deploys CF stack → ✅ succeeds (has all perms)

  Developer B (role: has ec2:*, s3:* only)
    → deploys SAME CF stack → ❌ fails (stack creates Lambda, B lacks lambda:*)

  Developer C (role: has lambda:*, s3:* only)
    → deploys SAME CF stack → ❌ fails (stack creates EC2, C lacks ec2:*)

ROOT CAUSE: CF uses the CALLER'S permissions by default.
            Different callers = different permissions = inconsistent results.
```

---

## The Solution

```
WITH service role:

  CFDeployRole (has ec2:*, s3:*, lambda:* — everything the stack needs)
    Trust policy: cloudformation.amazonaws.com can assume me

  Developer A → "CF, use CFDeployRole" → CF assumes role → ✅ succeeds
  Developer B → "CF, use CFDeployRole" → CF assumes role → ✅ succeeds
  Developer C → "CF, use CFDeployRole" → CF assumes role → ✅ succeeds

  All developers get SAME result because CF uses SAME permissions every time.
  Developers only need: cloudformation:* + iam:PassRole (on CFDeployRole)
```

---

## The Three Pieces

```
┌─────────────────────────────────────────────────────────────────┐
│ PIECE 1: Trust Policy (on CFDeployRole)                          │
│                                                                  │
│ "Who can BECOME this role?"                                      │
│                                                                  │
│ {                                                                │
│   "Version": "2012-10-17",                                       │
│   "Statement": [{                                                │
│     "Effect": "Allow",                                           │
│     "Principal": {                                               │
│       "Service": "cloudformation.amazonaws.com"                  │
│     },                                                           │
│     "Action": "sts:AssumeRole"                                   │
│   }]                                                             │
│ }                                                                │
│                                                                  │
│ ONLY cloudformation.amazonaws.com. Not every service.            │
│ Not the developer. Not ec2 or lambda service principals.         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PIECE 2: Permission Policy (on CFDeployRole)                     │
│                                                                  │
│ "What can this role DO once assumed?"                            │
│                                                                  │
│ {                                                                │
│   "Version": "2012-10-17",                                       │
│   "Statement": [{                                                │
│     "Sid": "CreateStackResources",                               │
│     "Effect": "Allow",                                           │
│     "Action": [                                                  │
│       "ec2:RunInstances",                                        │
│       "ec2:TerminateInstances",                                  │
│       "lambda:CreateFunction",                                   │
│       "lambda:DeleteFunction",                                   │
│       "s3:CreateBucket",                                         │
│       "s3:DeleteBucket"                                          │
│     ],                                                           │
│     "Resource": [                                                │
│       "arn:aws:ec2:us-east-1:123456789012:instance/*",           │
│       "arn:aws:lambda:us-east-1:123456789012:function:MyApp-*",  │
│       "arn:aws:s3:::myapp-*"                                     │
│     ]                                                            │
│   }]                                                             │
│ }                                                                │
│                                                                  │
│ Resources = what CF CREATES (EC2, Lambda, S3)                    │
│ NOT the stack ARN itself. NOT "arn:aws:cloudformation:..."       │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PIECE 3: Developer's Policy (on their IAM role)                  │
│                                                                  │
│ "Can the developer HAND this role to CF?"                        │
│                                                                  │
│ {                                                                │
│   "Version": "2012-10-17",                                       │
│   "Statement": [                                                 │
│     {                                                            │
│       "Sid": "AllowCFOperations",                                │
│       "Effect": "Allow",                                         │
│       "Action": [                                                │
│         "cloudformation:CreateStack",                            │
│         "cloudformation:UpdateStack",                            │
│         "cloudformation:DeleteStack",                            │
│         "cloudformation:DescribeStacks"                          │
│       ],                                                         │
│       "Resource": "*"                                            │
│     },                                                           │
│     {                                                            │
│       "Sid": "AllowPassRoleToCF",                                │
│       "Effect": "Allow",                                         │
│       "Action": "iam:PassRole",                                  │
│       "Resource": "arn:aws:iam::123456789012:role/CFDeployRole", │
│       "Condition": {                                             │
│         "StringEquals": {                                        │
│           "iam:PassedToService": "cloudformation.amazonaws.com"  │
│         }                                                        │
│       }                                                          │
│     }                                                            │
│   ]                                                              │
│ }                                                                │
│                                                                  │
│ Developer does NOT need ec2:*, lambda:*, s3:* anymore!           │
│ They just need to HAND the role to CF. CF does the heavy lifting.│
└─────────────────────────────────────────────────────────────────┘
```

---

## The Full Flow (Step by Step)

```
1. Developer calls: aws cloudformation create-stack \
     --stack-name my-app \
     --template-body file://template.yaml \
     --role-arn arn:aws:iam::123456789012:role/CFDeployRole
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                This is the key parameter!

2. AWS checks: "Does this developer have iam:PassRole on CFDeployRole?"
   → YES (their policy allows it) → proceed

3. CloudFormation says: "I'll assume CFDeployRole now"
   → Checks trust policy: "Am I (cloudformation.amazonaws.com) allowed?"
   → YES → CF gets temporary credentials as CFDeployRole

4. CloudFormation reads the template:
   → "Create an EC2 instance, a Lambda function, an S3 bucket"

5. For each resource, CF calls the AWS API AS CFDeployRole:
   → ec2:RunInstances (CFDeployRole has this) → ✅
   → lambda:CreateFunction (CFDeployRole has this) → ✅
   → s3:CreateBucket (CFDeployRole has this) → ✅

6. Stack created successfully. Developer's own permissions were IRRELEVANT.
```

---

## PassRole vs AssumeRole — The Mental Model

```
Think of it like a rental car:

  iam:PassRole = "Give the car keys to the valet"
    → YOU (developer) hand the role to a SERVICE (CF)
    → You're saying: "Here, use this identity"
    → You need PassRole permission

  sts:AssumeRole = "Drive the car yourself"
    → YOU become the role (get its credentials)
    → You're saying: "I want to BE this identity"
    → You need AssumeRole permission

  Trust policy = "Who is allowed to drive this car?"
    → The role itself says who can assume it
    → For CF: "cloudformation.amazonaws.com can drive"

┌──────────────────────────────────────────────┐
│ Developer:                                    │
│   "I can't drive the CFDeployRole car myself  │
│    (no sts:AssumeRole on it)                  │
│    BUT I can give the keys to CF              │
│    (iam:PassRole to CF)"                      │
│                                               │
│ CloudFormation:                               │
│   "Developer gave me the keys.               │
│    Trust policy says I can drive.             │
│    Let me deploy these resources."            │
└──────────────────────────────────────────────┘
```

---

## Why NOT AssumeRole in the Developer's Policy?

```
Q: Why does the developer need iam:PassRole and NOT sts:AssumeRole?

A: Because the developer is NOT becoming CFDeployRole themselves.
   They're telling CF to use it.

   If developer had sts:AssumeRole on CFDeployRole:
     → Developer becomes CFDeployRole
     → Developer now has ec2:*, lambda:*, s3:*
     → Developer can do ANYTHING CFDeployRole can
     → PRIVILEGE ESCALATION! ❌

   With iam:PassRole only:
     → Developer can't use those permissions themselves
     → Only CF (the service) gets them
     → Developer still restricted to cloudformation:* actions
     → No escalation ✅
```

---

## Why NOT Stack ARNs in Resource?

```
WRONG (targets stack):
  "Resource": "arn:aws:cloudformation:us-east-1:123:stack/my-app/*"
  
  This means: "CFDeployRole can modify the STACK OBJECT"
  But CF needs to create EC2, Lambda, S3 — not the stack metadata!

RIGHT (targets what CF creates):
  "Resource": [
    "arn:aws:ec2:us-east-1:123:instance/*",
    "arn:aws:lambda:us-east-1:123:function:MyApp-*",
    "arn:aws:s3:::myapp-*"
  ]
  
  This means: "CFDeployRole can create/modify THESE actual resources"
```

---

## Exam Scenarios

| Question Pattern | Answer |
|---|---|
| "CF deployments inconsistent across team" | Service role (consistent permissions) |
| "Least privilege for CF deployments" | Service role + scoped permissions on actual resources |
| "Developer shouldn't have broad permissions but needs to deploy" | Service role + iam:PassRole only |
| "CF trust policy — what service principal?" | `cloudformation.amazonaws.com` (only this one) |
| "Composite principal with ec2+lambda+s3 services" | ❌ WRONG — only CF in trust policy |
| "Resource ARN = stack ARN" | ❌ WRONG — target actual resources CF creates |

---

## Quick-Fire Recall

| Q | A |
|---|---|
| CF uses whose permissions by default? | The CALLER's (whoever ran create-stack) |
| How to make CF use consistent permissions? | Specify `--role-arn` (service role) |
| What goes in service role trust policy? | `cloudformation.amazonaws.com` ONLY |
| What goes in service role permission policy? | Actions on resources CF CREATES (EC2, Lambda, S3) |
| What does developer need? | `cloudformation:*` + `iam:PassRole` on the service role |
| Does developer need ec2:*/lambda:*/s3:*? | NO — CF does that via the service role |
| PassRole vs AssumeRole for developer? | PassRole = hand to service. AssumeRole = become the role yourself. |
| Why not AssumeRole for developer? | Would be privilege escalation (developer gets all role's permissions) |
| Why not stack ARN in Resource? | CF needs to create EC2/Lambda/S3, not modify stack metadata |

---

## 🧠 Cheat-Sheet One-Liners

- **"CF deployments inconsistent" = create service role + update stacks to use it.** Developers only need `iam:PassRole`.
- **CF service role trust = `cloudformation.amazonaws.com` ONLY.** Not composite. Not every service.
- **Permission policy targets ACTUAL RESOURCES (EC2, Lambda, S3).** NOT stack ARNs.
- **`iam:PassRole` = hand keys to service. `sts:AssumeRole` = drive the car yourself.** PassRole can't escalate. AssumeRole can.
