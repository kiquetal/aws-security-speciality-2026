# FAQ: AWS KMS (Key Management Service)

## Security Use Cases

### Encryption Architecture
- **FIPS 140-3 Security Level 3** validated HSMs in all regions (except China: OSCCA certified)
- Keys **never leave HSMs in plaintext** - only used in volatile memory
- Multi-party access control for HSM firmware updates
- Two-tier architecture: API endpoints (TLS) → HSMs

### Key Types & Operations
- **Symmetric keys**: 256-bit AES-GCM for encryption/decryption
- **Asymmetric keys**: RSA (2048/3072/4096), ECC (NIST P-256/384/521, SECG P-256k1)
- **HMAC keys**: For message authentication codes
- **Signing algorithms**: RSASSA_PSS, RSASSA_PKCS1, ECDSA
- **Encryption algorithms**: RSAES_OAEP_SHA_1/256 (RSA only)
- **Key agreement**: ECDH (elliptic curve keys)

### Key Management Options
1. **AWS KMS HSMs** (default): Highest performance, lowest latency, SLA included
2. **CloudHSM custom key store**: Single-tenant HSM, independent lifecycle management
3. **External key store (XKS)**: Keys stored outside AWS under your control
4. **Imported keys**: Bring your own key material

### Envelope Encryption

> **Diagram:** [envelope-encryption-flow.png](../diagrams/envelope-encryption-flow.png)

- KMS generates data keys encrypted under your KMS key
- Data encrypted locally with plaintext data key
- Only encrypted data key stored with encrypted data
- Reduces network load - only small data key transmitted to KMS

### Access Control
- IAM policies control who can manage/use keys
- Key policies define permissions for specific keys
- Resource-based policies for cross-account access
- CloudTrail logs all key usage for audit

## Key Limits/Quotas

### Key Limits
- **100,000 KMS keys per account per region** (enabled + disabled count toward limit)
- AWS managed keys don't count toward limit
- Request limit increase via AWS Support Center
- No limit on data keys derived from a KMS key

### Operation Limits
- **4 KB maximum** for direct encrypt/decrypt operations
- Different rate limits for different key types and algorithms
- Custom key store (CloudHSM) has lower performance than default KMS
- XKS operations: 500ms timeout (includes one retry at 250ms)

### Rotation & Lifecycle
- **Automatic rotation**: Configurable 90-2560 days (default: 365 days)
- **On-demand rotation**: Lifetime limit of 10 per key
- **NOT supported for**: Asymmetric keys, HMAC keys, CloudHSM custom key store keys
- **Deletion waiting period**: 7-30 days (default: 30 days)

## Exam Gotchas

### Key Type Restrictions
- **Asymmetric keys cannot be used for both signing AND encryption** - must choose at creation
- Elliptic curve keys: **signing only** (no encryption)
- RSA keys: Can be used for signing OR encryption (not both)
- **No automatic rotation** for asymmetric or HMAC keys

#### Key Type → Allowed Operations Matrix

| Key Type | Encrypt/Decrypt | Sign/Verify | HMAC | Notes |
|---|---|---|---|---|
| **Symmetric (AES-256)** | ✅ | ❌ | ❌ | Envelope encryption, S3/EBS/RDS |
| **RSA (SIGN_VERIFY)** | ❌ | ✅ | ❌ | JWTs, code signing |
| **RSA (ENCRYPT_DECRYPT)** | ✅ | ❌ | ❌ | Wrap external keys, encrypt small data |
| **ECC (SIGN_VERIFY)** | ❌ | ✅ | ❌ | Signing ONLY — never encrypts |
| **HMAC** | ❌ | ❌ | ✅ | GenerateMac / VerifyMac only |

> **Rule:** One key = one purpose. You cannot change key usage after creation.
> **RSA trap:** RSA CAN do signing OR encryption — but you must choose ONE at creation. A single RSA key cannot do both. ECC is even more restrictive: signing only, never encryption.

### Custom Key Store (CloudHSM)
- Requires **minimum 2 HSMs** in CloudHSM cluster
- **Cannot import key material** into custom key store
- **No automatic rotation** - must rotate manually
- Lower performance than default KMS key store
- You control availability and durability
- **Symmetric encryption only** when accessed through KMS — no asymmetric, no signing, no HMAC
- CloudHSM **directly** (bypassing KMS) supports everything: symmetric, asymmetric, signing, HMAC via PKCS#11/JCE/CNG

#### CloudHSM Direct vs Custom Key Store vs XKS

| | CloudHSM Direct | Custom Key Store (CloudHSM via KMS) | XKS (External via KMS) |
|---|---|---|---|
| **Symmetric** | ✅ | ✅ | ✅ |
| **Asymmetric** | ✅ | ❌ | ❌ |
| **Signing** | ✅ | ❌ | ❌ |
| **HMAC** | ✅ | ❌ | ❌ |
| **Interface** | PKCS#11, JCE, CNG | KMS API | KMS API |
| **Key material lives** | Your CloudHSM (in AWS) | Your CloudHSM (in AWS) | Your HSM (outside AWS) |
| **AWS service integration** | ❌ Manual | ✅ Native (S3, EBS, RDS) | ✅ Native (S3, EBS, RDS) |
| **KMS features (policies, grants, CloudTrail)** | ❌ | ✅ | ✅ |
| **Performance** | High | Lower than default KMS | Worst (500ms timeout) |
| **Availability SLA** | You manage | You manage | You manage, no AWS SLA |
| **Use case** | Full control, PKCS#11, signing | Single-tenant + KMS integration | "Keys never in AWS" regulation |

> **Exam gotcha:** "Need asymmetric keys on single-tenant HSM" → CloudHSM **directly**, not through KMS custom key store.
> **Exam gotcha:** Custom key store and XKS both = symmetric only through KMS. The limitation is KMS, not the HSM.

#### Quick Visual — Three CloudHSM-Related Options

```
┌─────────────────────────────────────────────────────────────────────┐
│                  THREE CloudHSM-RELATED OPTIONS                      │
├─────────────────────┬──────────────────────┬────────────────────────┤
│ CloudHSM DIRECT     │ Custom Key Store      │ XKS (External)         │
│                     │ (CloudHSM via KMS)    │ (Your HSM via KMS)     │
├─────────────────────┼──────────────────────┼────────────────────────┤
│ Key lives: YOUR     │ Key lives: YOUR       │ Key lives: YOUR HSM    │
│ CloudHSM (in AWS)   │ CloudHSM (in AWS)     │ OUTSIDE AWS            │
├─────────────────────┼──────────────────────┼────────────────────────┤
│ Interface: PKCS#11  │ Interface: KMS API    │ Interface: KMS API     │
│ JCE, CNG           │                      │                        │
├─────────────────────┼──────────────────────┼────────────────────────┤
│ Ops: ALL            │ Ops: SYMMETRIC ONLY   │ Ops: SYMMETRIC ONLY    │
│ (sym, asym, sign,  │ (encrypt/decrypt/     │ (encrypt/decrypt/      │
│  HMAC, wrap)        │  GenerateDataKey)     │  GenerateDataKey)      │
├─────────────────────┼──────────────────────┼────────────────────────┤
│ KMS features?  ❌   │ KMS features?  ✅     │ KMS features?  ✅      │
│ (no policies,       │ (key policies, grants,│ (key policies, grants, │
│  no grants,         │  CloudTrail, native   │  CloudTrail, native    │
│  no CloudTrail)     │  S3/EBS/RDS integr.)  │  S3/EBS/RDS integr.)   │
├─────────────────────┼──────────────────────┼────────────────────────┤
│ Tenant: SINGLE      │ Tenant: SINGLE        │ Tenant: SINGLE         │
├─────────────────────┼──────────────────────┼────────────────────────┤
│ Min HSMs: 1 (prod=2)│ Min HSMs: 2 (required)│ N/A (your infra)       │
└─────────────────────┴──────────────────────┴────────────────────────┘
```

### External Key Store (XKS)
- **Double encryption**: First by KMS internal key, then by your external key
- **You are responsible** for availability, durability, and performance
- **No SLA** for XKS operations (excluded from KMS SLA)
- 500ms timeout per request (including retry)
- **Symmetric encryption only**: Encrypt, Decrypt, ReEncrypt, GenerateDataKey — no asymmetric, no signing, no HMAC

### Key Material Import (Task 5.3.3 — New in C03)
- Can import symmetric, asymmetric, and HMAC keys
- Must be wrapped with KMS-provided public key
- **You maintain durability** - AWS doesn't back up imported keys
- Can set expiration time for imported key material
- Can delete imported material on-demand (key ID remains for re-import)

#### Imported vs AWS-Generated — Side by Side

| Dimension | AWS-Generated (default) | Imported |
|---|---|---|
| **Durability** | AWS manages (highly durable) | **YOU manage** — keep a copy or it's gone |
| **Automatic rotation** | ✅ Yes (90–2560 days) | ❌ No |
| **On-demand rotation** | ✅ Yes (max 10/key) | ❌ No |
| **Manual rotation** | Not needed | ✅ Only option (see below) |
| **Expiration** | Never expires | Optional — you set expiry date |
| **Delete material only** | ❌ Must delete whole key (7-30 day wait) | ✅ Can delete material, keep key ID for re-import |
| **Re-import** | N/A | ✅ Same material into same key ID |
| **Multi-region** | ✅ Supported | ❌ Single region only |
| **Key origin** | `AWS_KMS` | `EXTERNAL` |

#### How to Manually Rotate Imported Key Material

```
Step 1: Create a NEW KMS key (origin = EXTERNAL)
Step 2: Import your new key material into it
Step 3: Update your key ALIAS to point to the new key
Step 4: Old key still exists — decrypts old ciphertext

        ┌──────────────┐
        │  Key Alias    │
        │  alias/mykey  │──── points to ────► NEW key (key-id-2)
        └──────────────┘                      + new imported material

        Old key (key-id-1) still exists
        + old imported material
        + decrypts old ciphertext
        (don't delete until all data re-encrypted or expired)
```

> ⚠️ **Exam scenario:** "Company must generate key material on-premises for compliance.
> How do they rotate?" → Create new KMS key, import new material, update alias.
> There is NO automatic option for imported keys.

### Rotation Support Matrix (Exam-Critical)

| Key Type | Auto Rotation | On-Demand | Manual (alias swap) |
|---|---|---|---|
| **Symmetric (AWS-generated)** | ✅ 90–2560 days | ✅ Max 10 | ✅ |
| **Symmetric (imported)** | ❌ | ❌ | ✅ Only option |
| **Symmetric (CloudHSM store)** | ❌ | ❌ | ✅ Only option |
| **Symmetric (XKS)** | ❌ | ❌ | ✅ Only option |
| **Asymmetric (any origin)** | ❌ | ❌ | ✅ Only option |
| **HMAC (any origin)** | ❌ | ❌ | ✅ Only option |

> **Rule:** Automatic rotation ONLY works for symmetric keys with AWS-generated material.
> Everything else = manual rotation via alias swap.

### Multi-Region Keys
- Single-region keys stay in creation region
- Multi-region keys can be replicated within same AWS partition
- Each replica is independent but shares key material
- **Same key ID** across regions (prefix `mrk-`) — only the ARN differs (region part)
- Encrypt in one region, decrypt in another **locally** — no cross-region KMS call needed
- **Imported key material cannot be multi-region** — single region only
- Use case: DynamoDB Global Tables, S3 cross-region replication with SSE-KMS
- AWS managed keys (`aws/dynamodb`, `aws/s3`) are single-region — cannot replicate

### Key Deletion Protection (Exam-Critical)

> **Diagram:** [kms-key-lifecycle.mmd](../diagrams/kms-key-lifecycle.mmd)

| Layer | Mechanism | How |
|---|---|---|
| **Preventive** | SCP/IAM Deny `kms:ScheduleKeyDeletion` | Only break-glass admin can delete |
| **Detective** | CloudTrail + EventBridge + Lambda | Auto-cancel + alert in near real-time |
| **Reactive** | `CancelKeyDeletion` during waiting period | Key returns to Disabled state |

- Waiting period: **7 days (min) — 30 days (max, default)**
- During `PendingDeletion`: key cannot encrypt/decrypt (helps find dependencies)
- `CancelKeyDeletion` → key moves to `Disabled` (must re-enable manually)
- Once waiting period expires: key material destroyed **permanently**, data unrecoverable

### Encryption Context
- Additional authenticated data (AAD) for AES-GCM
- Not secret, but must match for decryption
- Logged in CloudTrail for audit
- Use for access control in key policies

### KMS vs CloudHSM vs Private CA
- **KMS**: Managed service, encryption/signing, no certificates
- **CloudHSM**: Single-tenant HSM, full control, PKCS#11/JCE/CNG
- **Private CA**: PKI infrastructure, X.509 certificates, TLS termination

## KMS Grants — Dynamic Cross-Account Access (Task 5.2)

> **Diagram:** [kms-grants-cross-account.png](../diagrams/kms-grants-cross-account.png)

KMS has THREE access control mechanisms. Grants are unique to KMS — no other AWS service has them.

```
1. KEY POLICY    — resource-based policy on the key (required, static, 32KB limit)
2. IAM POLICY    — identity-based on the caller (same-account only, if key policy allows)
3. KMS GRANT     — programmatic, dynamic, cross-account, no size limit
```

### When to Use Grants

```
SCENARIO: SaaS platform, 500 customers, each in their own AWS account

  With Key Policy only:
    "Principal": {"AWS": [
      "arn:aws:iam::111111111111:role/CustomerA",
      "arn:aws:iam::222222222222:role/CustomerB",
      ... 498 more ...
    ]}
    → Hit 32KB limit around customer ~200
    → Every onboard/offboard = manual policy edit

  With Grants:
    Key policy (set ONCE, never changes):
      Allow OnboardingService to kms:CreateGrant

    Onboarding automation:
      aws kms create-grant \
        --key-id arn:aws:kms:us-east-1:999999999999:key/abc-123 \
        --grantee-principal arn:aws:iam::111111111111:role/CustomerA \
        --operations Decrypt

    New customer = one API call. No policy edit.
    Customer leaves = kms:RevokeGrant. Done.
```

### Grant vs Key Policy vs IAM Policy

| Question | Answer |
|---|---|
| "Permanent access for your own team" | Key policy or IAM policy |
| "Cross-account, dynamic, scales to many customers" | **KMS Grant** |
| "Without modifying the key policy" | **KMS Grant** |
| "Temporary access for an AWS service" (EBS, RDS) | **KMS Grant** (services use grants internally) |
| "Revoke one customer without affecting others" | **KMS Grant** |

### Grant Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Eventually consistent** | May take up to 5 min. Use **grant token** for immediate use. |
| **AWS services use grants internally** | EBS, RDS, Lambda create grants on your key. Visible in CloudTrail. |
| **RetireGrant vs RevokeGrant** | Grantee can retire own grant. Only key admin can revoke. |
| **RCPs exempt `kms:RetireGrant`** | Even if RCP restricts KMS, RetireGrant still works. |
| **Grants don't appear in key policy** | Use `aws kms list-grants` to see them. |
| **Grant token** | Returned by CreateGrant. Pass to subsequent API calls for immediate use before eventual consistency kicks in. |

### Why NOT AWS RAM for KMS Cross-Account Access?

```
AWS RAM (Resource Access Manager):
  ├── Purpose: SHARE resources across accounts
  ├── Supported: Transit Gateways, Subnets, Route 53 Rules,
  │              License Manager, Aurora DB clusters, etc.
  ├── NOT supported: KMS keys ← RAM doesn't support KMS
  └── Even if it did: RAM shares the resource itself,
      not fine-grained operations (Decrypt only, not Encrypt)

KMS Grants:
  ├── Purpose: Grant specific KMS OPERATIONS to specific principals
  ├── Fine-grained: Decrypt only, Encrypt only, GenerateDataKey only
  ├── Per-principal: Each customer gets exactly the operations they need
  └── Revocable: Remove one customer without touching others
```

| Dimension | RAM | KMS Grants |
|---|---|---|
| **Supports KMS?** | ❌ No | ✅ Yes |
| **Granularity** | Share entire resource | Specific operations (Decrypt, Encrypt, etc.) |
| **Revoke one customer** | Remove from share | RevokeGrant for that principal |
| **Scale** | Good for infra sharing | Good for data access |
| **Use case** | "Share my Transit Gateway" | "Let Customer A decrypt with my key" |

> **Exam trap:** If a question says "share KMS key access across accounts" and RAM is an option → **RAM is wrong**. KMS Grants or key policy are the only ways.

## Best Practices for IAM Policies

1. **Use separate keys** for different data classifications
2. **Enable automatic rotation** for symmetric encryption keys
3. **Use grants** for temporary, programmatic access
4. **Condition keys**: `kms:EncryptionContext`, `kms:ViaService`
5. **Deny direct key access** - require service integration via `kms:ViaService`
6. **Monitor with CloudTrail** - all key usage is logged
7. **Use key policies + IAM policies** together for defense in depth
