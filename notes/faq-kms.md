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

### Key Material Import
- Can import symmetric, asymmetric, and HMAC keys
- Must be wrapped with KMS-provided public key
- **You maintain durability** - AWS doesn't back up imported keys
- Can set expiration time for imported key material
- Can delete imported material on-demand (key ID remains for re-import)

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
