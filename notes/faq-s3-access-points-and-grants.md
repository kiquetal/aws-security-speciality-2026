# FAQ: S3 Access Points & S3 Access Grants

> **Blueprint refs:** Task 5.2 (data at rest controls), Task 6.2 (secure deployment strategy)
> **Video ref:** "S3 Access Points" + "S3 Access Grants" (course catalog)
> **Related:** [faq-s3.md](./faq-s3.md) (bucket policies, encryption, Object Lock)

---

## The Problem Both Solve

A single S3 bucket policy becomes unmanageable when many teams, apps, or users need different access patterns on the same bucket.

```
ONE bucket, TEN teams, each needs different prefix access:
  → Bucket policy grows to 50+ statements
  → Hits 20KB policy size limit
  → One typo = data breach or broken access
  → Auditing "who can access what" = nightmare
```

**Access Points** and **Access Grants** solve this differently:

| | Access Points | Access Grants |
|---|---|---|
| **Approach** | Split one policy into many named endpoints | Map identities to prefixes declaratively |
| **Mental model** | "Multiple front doors to the same house, each with its own lock" | "A guest list that says who can enter which rooms" |
| **Who it's for** | Applications, services, cross-account | Corporate users (Identity Center) or IAM principals |

---

## S3 Access Points

### One-Liner

**Named network endpoints with their own access policy — each scoped to a prefix, VPC, or account.**

### Mental Model

```
Traditional:
  Everyone → one bucket policy → bucket
  (one giant policy, one entry point)

With Access Points:
  Team Analytics → ap-analytics (own policy, prefix=/analytics/) → bucket
  Team ML        → ap-ml-data  (own policy, prefix=/ml/)        → bucket
  Team Logs      → ap-logs     (own policy, VPC-only)           → bucket

Each access point = separate hostname + separate policy
```

### How It Works

```
┌─────────────────────────────────────────────────────────────┐
│  S3 Bucket: "company-data-lake"                              │
│  Bucket policy: delegates to access points                   │
│                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌────────────┐  │
│  │ ap-analytics    │  │ ap-ml-data      │  │ ap-logs    │  │
│  │                 │  │                 │  │            │  │
│  │ Policy:         │  │ Policy:         │  │ Policy:    │  │
│  │ Allow Team A    │  │ Allow Team B    │  │ Allow VPC  │  │
│  │ prefix=/analytics│  │ prefix=/ml/     │  │ only       │  │
│  │                 │  │                 │  │            │  │
│  │ DNS:            │  │ DNS:            │  │ DNS:       │  │
│  │ ap-analytics-   │  │ ap-ml-data-     │  │ ap-logs-   │  │
│  │ 123456789012    │  │ 123456789012    │  │ 123456789  │  │
│  │ .s3-accesspoint │  │ .s3-accesspoint │  │ .s3-access │  │
│  │ .us-east-1...   │  │ .us-east-1...   │  │ point...   │  │
│  └─────────────────┘  └─────────────────┘  └────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Key Properties

| Property | Detail |
|---|---|
| **Unique DNS name** | `https://{name}-{account-id}.s3-accesspoint.{region}.amazonaws.com` |
| **Own access policy** | JSON policy, independent of bucket policy |
| **VPC restriction** | Can lock to a specific VPC (internet access blocked) |
| **Block Public Access** | Each access point has its own BPA settings |
| **Cross-account** | ✅ Can grant access to other accounts |
| **ARN format** | `arn:aws:s3:{region}:{account}:accesspoint/{name}` |

### Policy Evaluation (Exam-Critical)

```
Request arrives at access point:
  1. Access point policy evaluated
  2. Bucket policy evaluated
  3. BOTH must allow (intersection)

Access point policy CANNOT grant more than bucket policy allows.
Think of it as: bucket policy = ceiling, access point policy = room-level control.
```

**Bucket policy that delegates to access points:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DelegateToAccessPoints",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::company-data-lake",
        "arn:aws:s3:::company-data-lake/*"
      ],
      "Condition": {
        "StringEquals": {
          "s3:DataAccessPointAccount": "123456789012"
        }
      }
    }
  ]
}
```

> This says: "I trust any access point in my account to make access decisions."

### VPC-Only Access Points

```
Access point created with:
  NetworkOrigin: VPC
  VpcConfiguration:
    VpcId: vpc-abc123

Result:
  ✅ Requests from vpc-abc123 → allowed (if policy permits)
  ❌ Requests from internet → blocked (regardless of policy)
  ❌ Requests from other VPCs → blocked
```

**Exam signal:** "Restrict S3 access to private network only" → VPC-only access point.

### Limits

| Limit | Value |
|---|---|
| Access points per region per account | 10,000 |
| Access point policy max size | 20 KB |
| Access point name | 3-50 characters, lowercase, no underscores |

---

## S3 Access Grants

### One-Liner

**Declarative mapping of identities (Identity Center users/groups or IAM) to S3 prefixes with a permission level — no JSON policies to write.**

### Mental Model

```
Traditional IAM approach:
  "Write a policy that allows role X to GetObject on prefix /analytics/*"
  → You write JSON, attach to role, manage lifecycle

Access Grants approach:
  "Analytics group gets READ on /analytics/"
  → One grant definition. Done. No JSON policy.
  → User calls GetDataAccess API → gets temporary scoped credentials
```

### How It Works

```
┌──────────────────────────────────────────────────────────────────┐
│  S3 Access Grants Instance (one per account per region)           │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │  Location 1: s3://company-bucket/analytics/*                 │ │
│  │  Location 2: s3://company-bucket/ml-data/*                   │ │
│  │  Location 3: s3://company-bucket/finance/*                   │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │  Grant 1: Identity Center group "Analytics" → Location 1    │ │
│  │           Permission: READ                                   │ │
│  │                                                              │ │
│  │  Grant 2: Identity Center group "ML Team" → Location 2      │ │
│  │           Permission: READWRITE                              │ │
│  │                                                              │ │
│  │  Grant 3: IAM role "FinanceApp" → Location 3                │ │
│  │           Permission: READ                                   │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  User flow:                                                       │
│  1. User authenticates (Identity Center or IAM)                   │
│  2. App calls s3:GetDataAccess API                                │
│  3. Access Grants returns temporary S3 credentials                │
│  4. Credentials scoped to ONLY the granted prefix + permission    │
│  5. User accesses S3 with those credentials                       │
└──────────────────────────────────────────────────────────────────┘
```

### Permission Levels (Only Three)

| Level | S3 Actions Granted |
|---|---|
| **READ** | `GetObject`, `GetObjectAttributes`, `ListBucket` (scoped to prefix) |
| **WRITE** | `PutObject`, `DeleteObject`, `AbortMultipartUpload` |
| **READWRITE** | All of the above |

> No custom actions — just pick one of three levels. Simplicity is the point.

### Identity Sources

| Source | How It Works |
|---|---|
| **IAM Identity Center** | Map groups/users from corporate directory (Okta, Entra ID, etc.) |
| **IAM principals** | Map IAM roles or users directly |
| **Directory (via Identity Center)** | Corporate AD groups synced via SCIM |

### Key Properties

| Property | Detail |
|---|---|
| **Credential mechanism** | `s3:GetDataAccess` API returns temporary credentials |
| **Credential duration** | 15 min to 12 hours (configurable) |
| **Prefix scoping** | Built into the grant (no policy conditions needed) |
| **Audit** | CloudTrail logs every `GetDataAccess` call |
| **Cross-account** | ✅ Can grant to principals in other accounts |
| **VPC restriction** | ❌ Not VPC-scoped (use Access Points for that) |

### Limits

| Limit | Value |
|---|---|
| Access Grants instances per account per region | 1 |
| Grants per instance | 100,000 |
| Locations per instance | 1,000 |
| Credential duration | 15 min – 12 hours |

---

## Access Points vs Access Grants — Decision Table

| Exam Question Says | Answer | Why |
|---|---|---|
| "Simplify bucket policy for multiple teams" | **Access Points** | Split one policy into many |
| "Restrict S3 access to specific VPC" | **Access Points** (VPC-only) | Network-level restriction |
| "Map corporate directory groups to S3 prefixes" | **Access Grants** | Identity Center integration |
| "Grant S3 access based on Identity Center groups without writing policies" | **Access Grants** | Declarative, no JSON |
| "Cross-account S3 access with dedicated endpoint" | **Access Points** | Named endpoint per consumer |
| "Temporary scoped credentials for S3 prefix" | **Access Grants** | `GetDataAccess` vends creds |
| "Application needs its own S3 endpoint with own policy" | **Access Points** | Per-app entry point |

---

## How They Relate to Other S3 Access Mechanisms

```
┌─────────────────────────────────────────────────────────────────┐
│  S3 ACCESS CONTROL — ALL MECHANISMS                              │
│                                                                  │
│  POLICY-BASED (you write JSON):                                  │
│  ├── Bucket policy (one per bucket, 20KB limit)                  │
│  ├── IAM policy (on the caller's role/user)                      │
│  └── Access Point policy (one per access point)                  │
│                                                                  │
│  DECLARATIVE (no JSON):                                          │
│  └── Access Grants (identity → prefix → permission level)        │
│                                                                  │
│  TEMPORARY ACCESS (time-limited):                                │
│  ├── Presigned URLs (one object, one operation, expiry)          │
│  └── Access Grants credentials (prefix-scoped, via API)          │
│                                                                  │
│  NETWORK-LEVEL:                                                  │
│  ├── VPC-only Access Points (restrict to one VPC)                │
│  ├── VPC Gateway Endpoint + endpoint policy                      │
│  └── S3 Block Public Access (account/bucket level)               │
│                                                                  │
│  LEGACY (don't use):                                             │
│  └── ACLs (disabled by default since April 2023)                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Access Point policy + bucket policy = intersection** | AP policy can't exceed what bucket policy allows |
| **VPC-only AP = no internet** | Once set to VPC, can't access from outside that VPC |
| **Access Grants ≠ KMS Grants** | Completely different services. S3 Access Grants = S3 prefix access. KMS Grants = KMS key operations. |
| **Access Grants needs Identity Center OR IAM** | Must have one identity source configured |
| **`GetDataAccess` is the API** | This is how apps request temporary credentials from Access Grants |
| **One Access Grants instance per account per region** | Unlike access points (10,000 per region) |
| **Access Grants don't replace bucket policies** | Bucket policy still evaluated — grants work alongside |
| **Access Points support S3 Object Lambda** | Can transform data on read (e.g., redact PII) |

---

## 🧠 Cheat-Sheet One-Liners

- **Access Points = multiple front doors with separate locks.** Each has own policy, own hostname, optional VPC restriction.
- **Access Grants = guest list mapping identities to rooms.** No JSON policies — just identity + prefix + permission level.
- **"VPC-only S3 access" = Access Point with NetworkOrigin:VPC.** Not Access Grants (no VPC scoping).
- **"Map Identity Center groups to S3 prefixes" = Access Grants.** Vends temporary credentials via `GetDataAccess`.
- **Access Grants ≠ KMS Grants.** Different services, different problems. Don't confuse them.
