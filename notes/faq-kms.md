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

### Custom Key Store (CloudHSM)
- Requires **minimum 2 HSMs** in CloudHSM cluster
- **Cannot import key material** into custom key store
- **No automatic rotation** - must rotate manually
- Lower performance than default KMS key store
- You control availability and durability

### External Key Store (XKS)
- **Double encryption**: First by KMS internal key, then by your external key
- **You are responsible** for availability, durability, and performance
- **No SLA** for XKS operations (excluded from KMS SLA)
- 500ms timeout per request (including retry)
- Supports only symmetric encryption operations: Encrypt, Decrypt, ReEncrypt, GenerateDataKey

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

### Encryption Context
- Additional authenticated data (AAD) for AES-GCM
- Not secret, but must match for decryption
- Logged in CloudTrail for audit
- Use for access control in key policies

### KMS vs CloudHSM vs Private CA
- **KMS**: Managed service, encryption/signing, no certificates
- **CloudHSM**: Single-tenant HSM, full control, PKCS#11/JCE/CNG
- **Private CA**: PKI infrastructure, X.509 certificates, TLS termination

## Best Practices for IAM Policies

1. **Use separate keys** for different data classifications
2. **Enable automatic rotation** for symmetric encryption keys
3. **Use grants** for temporary, programmatic access
4. **Condition keys**: `kms:EncryptionContext`, `kms:ViaService`
5. **Deny direct key access** - require service integration via `kms:ViaService`
6. **Monitor with CloudTrail** - all key usage is logged
7. **Use key policies + IAM policies** together for defense in depth
