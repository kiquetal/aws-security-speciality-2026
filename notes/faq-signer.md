# FAQ: AWS Signer — Code Signing Service

> **Blueprint refs:** Task 3.2 (secure compute deployment), Task 6.2 (secure deployment strategy)
> **Video ref:** "Code Signing with AWS Signer" (course catalog)

## One-Liner

**Cryptographically sign code artifacts (Lambda, containers, IoT firmware) to guarantee integrity and provenance at deployment time.**

## The Problem It Solves

```
WITHOUT code signing:
  Developer → builds Lambda zip → uploads to S3 → deploys
  Attacker  → modifies zip in S3 → Lambda runs tampered code
  → No way to detect the modification

WITH AWS Signer:
  CI pipeline → builds Lambda zip → signs with Signer → uploads to S3
  Lambda deployment → verifies signature → only deploys if valid
  Attacker modifies zip → signature invalid → deployment BLOCKED
```

## What It Signs

| Artifact Type | Integration | Verification Point |
|---|---|---|
| **Lambda deployment packages** | Lambda Code Signing Configuration | At deploy time (CreateFunction / UpdateFunctionCode) |
| **Container images** | ECR + Notation (AWS Signer plugin) | At pull time (EKS admission controller) |
| **IoT OTA updates** | AWS IoT Jobs | At device firmware update |
| **AWS Lambda layers** | Same as Lambda packages | At deploy time |

## How It Works (Lambda — Primary Exam Target)

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  CI Pipeline │────►│  AWS Signer   │────►│  Signed artifact │
│  (build zip) │     │  (signs with  │     │  (S3 bucket)     │
│              │     │   your profile)│     │                  │
└─────────────┘     └──────────────┘     └────────┬────────┘
                                                   │
                                                   ▼
                                          ┌─────────────────┐
                                          │  Lambda Function │
                                          │  (Code Signing   │
                                          │   Configuration) │
                                          │                  │
                                          │  Checks signature│
                                          │  before deploy   │
                                          └─────────────────┘

If signature invalid or missing → deployment REJECTED (or WARN)
```

### Key Components

| Component | What It Is |
|---|---|
| **Signing profile** | Defines the signing configuration (algorithm, validity period) |
| **Signing job** | One-time operation that signs an artifact |
| **Code Signing Configuration (CSC)** | Lambda resource that enforces signature validation |
| **Revocation** | Invalidate a signing profile or specific signature |

### Lambda Code Signing Configuration

```
CSC defines:
├── Allowed signing profiles (who can sign)
├── Untrusted artifact policy:
│   ├── ENFORCE → block deployment if unsigned/invalid
│   └── WARN → allow but log warning in CloudTrail
└── Attached to Lambda function(s)
```

## Container Image Signing (EKS)

```
CI pipeline → build image → push to ECR → sign with Signer (Notation plugin)
                                                    │
EKS cluster → admission controller (Kyverno/OPA) → verify signature → allow/deny pod
```

- Uses **Notation** format (CNCF standard, like cosign)
- AWS Signer acts as the signing authority
- Verification via admission webhooks in EKS (not built into EKS natively)

## Key Limits/Quotas

| Limit | Value |
|---|---|
| Signing profiles per account per region | 100 |
| Signature validity | Configurable (default 135 months for Lambda) |
| Supported platforms | Lambda, Container (Notation), IoT |
| Signing algorithms | ECDSA (P-256, P-384) |
| Cost | Free (no charge for signing operations) |
| Revocation | Per-profile or per-job |

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Doesn't scan code** | Signer signs, doesn't analyze. Inspector scans for CVEs. Different jobs. |
| **Lambda CSC = enforcement point** | Without CSC attached to the function, signing is meaningless |
| **ENFORCE vs WARN** | ENFORCE blocks unsigned deploys. WARN just logs. Exam prefers ENFORCE. |
| **Revocation** | Can revoke a signing profile (all signatures from it become invalid) or revoke specific signatures |
| **CloudTrail logs** | All signing operations and validation failures logged |
| **Free** | No cost for AWS Signer itself |
| **Not ACM** | ACM = TLS certificates. Signer = code artifact signatures. Different things. |
| **Not KMS directly** | Signer manages its own signing keys (backed by KMS internally), you don't manage the key |

## Exam Decision Table

| Signal | Answer | NOT This |
|---|---|---|
| "Ensure Lambda code hasn't been tampered" | **AWS Signer + CSC** | ❌ Inspector (finds CVEs, not tampering) |
| "Only deploy signed container images" | **AWS Signer + admission controller** | ❌ ECR scanning (CVEs, not provenance) |
| "Verify code integrity before deployment" | **AWS Signer** | ❌ CodeGuru (code quality, not integrity) |
| "Scan Lambda for vulnerabilities" | **Inspector** | ❌ Signer (integrity, not vulns) |
| "TLS certificate for HTTPS" | **ACM** | ❌ Signer (code signing, not TLS) |

## Integration with Other Services

| Service | Relationship |
|---|---|
| **Lambda** | CSC enforces signature validation at deploy |
| **ECR** | Stores signed container images (Notation format) |
| **S3** | Stores signed Lambda packages |
| **CloudTrail** | Logs all signing/validation events |
| **IAM** | Controls who can create signing profiles and sign |
| **Inspector** | Complementary — Inspector finds CVEs, Signer ensures integrity |

## K8s Mapping

```
AWS Signer          ≈  cosign / Sigstore / Notary v2
Signing profile     ≈  cosign key pair
CSC on Lambda       ≈  Kyverno ClusterPolicy verifyImages
ENFORCE policy      ≈  Kyverno policy in "enforce" mode
WARN policy         ≈  Kyverno policy in "audit" mode
Revocation          ≈  cosign key rotation + old signatures invalid
```

## Example: Lambda Code Signing Flow

```bash
# 1. Create signing profile
aws signer put-signing-profile \
  --profile-name ProdLambdaSigning \
  --platform-id AWSLambda-SHA384-ECDSA

# 2. Sign the deployment package
aws signer start-signing-job \
  --source 's3={bucketName=my-bucket,key=function.zip,version=abc123}' \
  --destination 's3={bucketName=my-bucket,prefix=signed/}' \
  --profile-name ProdLambdaSigning

# 3. Create Code Signing Configuration
aws lambda create-code-signing-config \
  --allowed-publishers 'SigningProfileVersionArns=arn:aws:signer:us-east-1:123456789012:/signing-profiles/ProdLambdaSigning/abc123' \
  --code-signing-policies 'UntrustedArtifactOnDeployment=Enforce'

# 4. Attach CSC to Lambda function
aws lambda put-function-code-signing-config \
  --function-name my-function \
  --code-signing-config-arn arn:aws:lambda:us-east-1:123456789012:code-signing-config:csc-abc123
```

## 🧠 Cheat-Sheet One-Liners

- **Signer = integrity (hasn't been tampered). Inspector = vulnerabilities (has known CVEs).** Different problems.
- **Lambda Code Signing Configuration = enforcement point.** Without CSC attached, signing is useless.
- **"Ensure only signed code deploys" = AWS Signer + CSC (ENFORCE).** Not Inspector, not CodeGuru, not KMS directly.
