# New in SCS-C03 — Must Know (Guaranteed Questions)

> These 7 topics have NO C02 precedent. Exam writers will test them as differentiators.
> **Status:** Quick reference only. Each needs a deep-dive FAQ.

## 1. RCPs — Resource Control Policies (Task 6.1)

**Status:** ✅ Deep dive exists → [faq-rcp.md](./faq-rcp.md) + [policy-layers-reference.md](./policy-layers-reference.md)

## 2. GenAI OWASP Top 10 (Task 3.2.7)

**Status:** ❌ Needs FAQ

```
What the exam tests:
├── Amazon Bedrock Guardrails — content filtering for LLM apps
├── Prompt injection — attacker manipulates LLM via input
├── Model access controls — who can invoke which model
└── You DON'T need the full OWASP list — just AWS controls

Exam signal: "protect AI application" / "prevent prompt injection"
→ Bedrock Guardrails
```

## 3. OCSF — Open Cybersecurity Schema Framework (Task 3.1.4)

**Status:** ❌ Needs FAQ

```
What it is:
├── Standard schema for security events across tools
├── Amazon Security Lake uses OCSF as its native format
├── Normalizes logs from CloudTrail, VPC Flow Logs, WAF,
│   Route 53, GuardDuty, third-party tools into ONE format
└── Enables cross-service queries without format conversion

Exam signal: "normalize security logs" / "common schema" / "Security Lake"
→ OCSF

You don't need to know schema fields.
Just: OCSF = Security Lake's format = normalizes everything.
```

## 4. Data Masking (Task 5.3.4)

**Status:** ❌ Needs FAQ

```
Two services:

CloudWatch Logs data protection policies:
├── Detect and mask sensitive data in logs automatically
├── PII (SSN, credit cards, email) masked in real-time
├── Policy defines which data identifiers to detect
└── Masked data shows as ******* in log output

SNS message data protection:
├── Same concept but for SNS messages
├── Detect/mask/audit sensitive data before delivery
└── Protects subscribers from receiving raw PII

Exam signal: "mask PII in logs" / "protect sensitive data in log output"
→ CloudWatch Logs data protection policy
NOT Macie (Macie scans S3, not logs)
```

## 5. Nitro Inter-Instance Encryption (Task 5.1.3)

**Status:** ❌ Needs FAQ

```
What it is:
├── Automatic encryption of traffic BETWEEN EC2 instances
├── Nitro-based instances only
├── No application changes needed — hardware level
├── No performance impact (hardware-accelerated)
└── Covers: EC2-to-EC2, EKS inter-node, EMR, SageMaker

Exam signal: "encrypt traffic between instances"
           / "encryption in transit without application changes"
→ Nitro inter-instance encryption

K8s mapping: Istio mTLS but at the hypervisor level —
zero config, infrastructure handles it.
```

## 6. Imported Key Material Differences (Task 5.3.3)

**Status:** ✅ Deep dive exists → [faq-kms.md](./faq-kms.md) (rotation matrix, durability, manual rotation)

## 7. Multi-Region Keys + Private CA (Task 5.3.5)

**Status:** ❌ Needs FAQ

```
Multi-Region Keys (MRKs):
├── Same key material replicated across regions
├── Same key ID prefix (mrk-...)
├── Each replica has INDEPENDENT key policy
├── Use case: encrypt in us-east-1, decrypt in eu-west-1
│             without cross-region KMS calls
├── NOT supported for imported key material
└── Primary key + replica keys

ACM Private CA:
├── Issue private X.509 certificates for internal TLS
├── Cross-region: share CA across regions
├── Use case: mTLS between services, internal HTTPS
└── NOT for public websites (use ACM public certs for that)

Exam signal: "encrypt in one region, decrypt in another" → MRK
           / "internal TLS certificates at scale" → ACM Private CA
```

## Progress Tracker

| # | Topic | Quick Ref | Deep-Dive FAQ |
|---|---|---|---|
| 1 | RCPs | ✅ | ✅ faq-rcp.md |
| 2 | GenAI OWASP Top 10 | ✅ | ❌ TODO |
| 3 | OCSF / Security Lake | ✅ | ❌ TODO |
| 4 | Data Masking | ✅ | ❌ TODO |
| 5 | Nitro Encryption | ✅ | ❌ TODO |
| 6 | Imported Key Material | ✅ | ✅ faq-kms.md |
| 7 | Multi-Region Keys + Private CA | ✅ | ❌ TODO |
