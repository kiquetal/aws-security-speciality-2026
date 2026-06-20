# Next Weekly Session

> Say "run the weekly session" and I'll generate questions from the current week below.
> After grading, I mark it ✅ and advance to the next week.

---

## Current Week: 3 (Jun 30 - Jul 6) — D1 Weak Areas + cfn-guard + State Manager

**Focus:** D1 Detection remaining wording traps + CloudFormation Guard (policy-as-code) + SSM State Manager (deeper variants)

**Generate:** 25 questions, killer difficulty

**Structure:**
- Q1-8: D1 Detection (StopLogging detection mechanisms, GuardDuty ≠ failed attempts, Access Analyzer static vs GD dynamic, EventBridge vs Config speed, CW Logs Insights vs Detective)
- Q9-14: CloudFormation Guard (cfn-guard rules, CI/CD integration, vs CF Hooks vs SCP, validate template content)
- Q15-20: State Manager (dual triggers, vs Config remediation, vs Session Manager, desired-state vs reactive, schedule enforcement)
- Q21-25: Cross-domain killers mixing all Week 3 topics with Dojo-style wording traps

---

### Question 1 (mTLS Customs)
A financial client requires mutual TLS (mTLS) authentication for all B2B API integrations connecting to a backend microservice. The microservice is exposed through Amazon API Gateway. The integrations must be validated against a private Root CA certificate managed by the client. 
What is the most secure and operationally efficient way to implement this architecture?
A. Upload the private Root CA certificate to AWS Certificate Manager (ACM) in the same region, and associate this certificate directly as the client certificate in the API Gateway custom domain settings.
B. Create a Custom Lambda Authorizer in API Gateway. In the Lambda code, import the client's Root CA, fetch the incoming client certificate from the `X-Forwarded-Client-Cert` header, and use cryptography libraries to validate the certificate chain.
C. Store the client's Root CA PEM certificate file in an S3 bucket with versioning enabled. Create an API Gateway custom domain name, enable mutual TLS, and provide the S3 URI and S3 Object Version of the PEM file. Configure Route 53 to point to the API Gateway custom domain.
D. Deploy an Application Load Balancer (ALB) in front of API Gateway. Configure the ALB listener with an HTTPS rule, enable Mutual TLS on the ALB listener, and upload the Root CA to the ALB's trust store.

---

### Question 2 (API Gateway Authorizer Route Rules)
An API Gateway API serves a single web application. The security engineer must configure authentication such that standard web clients authenticate using JWT tokens from an Amazon Cognito User Pool. However, a group of legacy API clients must bypass Cognito and authenticate using an HMAC signature provided in a custom request header (`X-Signature`). These legacy clients always make requests from a fixed, known set of public IP addresses, and legacy requests from other IPs must be rejected immediately at the API Gateway boundary.
Which configuration achieves this with the **least operational overhead**?
A. Use a single Cognito Authorizer for the API. In Cognito, create a user group for the legacy clients, and configure a custom authentication flow to validate HMAC signatures and verify source IP addresses.
B. Create a Cognito Authorizer for the web client routes. Create a Custom Lambda Authorizer of type `REQUEST` for the legacy routes that computes the expected HMAC signature and validates the client IP against the allowed list in the Lambda code.
C. Create a Cognito Authorizer for the web client routes. Create a Custom Lambda Authorizer of type `REQUEST` for the legacy routes to validate the `X-Signature` header. Apply an API Gateway Resource Policy that denies invoke access to the legacy routes if the request originates outside the specified legacy public IP addresses.
D. Configure an AWS WAF Web ACL associated with the API Gateway. Write a WAF rule that inspects the `X-Signature` header, validates it using a Custom Lambda helper, and restricts the source IP addresses. Apply a Cognito Authorizer to the remaining routes.

---

### Question 3 (CloudFront FLE Cryptography)
A medical portal processes sensitive Health Insurance Claim Numbers (HICN) submitted via HTTP POST requests inside a nested form field named `claim_id`. Corporate security rules mandate that this field must be encrypted at the AWS network edge (CloudFront) using asymmetric public-key cryptography before the payload is forwarded to the application servers (origins), ensuring intermediate firewalls or logging endpoints cannot access the raw field value.
How should the security engineer implement this requirement with the **least configuration complexity**?
A. Create an AWS KMS customer managed key (CMK). Configure the CloudFront distribution cache behavior to enable KMS encryption, mapping the POST form field `claim_id` directly to the CMK.
B. Upload an RSA public key file to CloudFront. Create a Field-Level Encryption Profile in CloudFront mapping the field `claim_id` to the public key. Create a Field-Level Encryption Configuration associating the profile with the `application/x-www-form-urlencoded` content type, and link this configuration to the origin's cache behavior.
C. Write a CloudFront Functions script to intercept the POST request, extract the `claim_id` query parameter, encrypt it using the WebCrypto API with a public key hardcoded in the function, and forward the request.
D. Associate a Lambda@Edge function with the `viewer-request` event. In the function, call `kms:Encrypt` using an asymmetric KMS key to encrypt the `claim_id` field in the request body before forwarding to the origin.

---

### Question 4 (Inspector SBOM Compliance) — **Select TWO**
A company's compliance framework requires a centralized, automated Software Bill of Materials (SBOM) to be maintained for all software components and packages installed across the organization's Amazon EC2 instances and Amazon Elastic Container Registry (ECR) repositories. This SBOM must be exported regularly in CycloneDX format to a central S3 bucket in a compliance account for auditing.
Which combination of steps will achieve this with the **least operational overhead**? (Select TWO)
A. Configure an S3 Bucket Policy on the central compliance bucket that allows `s3:PutObject` and `s3:PutObjectAcl` permissions for the Amazon Inspector service principal `inspector2.amazonaws.com`.
B. Use AWS Systems Manager Inventory to collect installed package lists from all EC2 instances, and configure a central Lambda function to parse the lists and compile them into CycloneDX format before writing to S3.
C. Set up Amazon Inspector in the organization's delegated administrator account. Use Inspector's native SBOM export feature, specify CycloneDX format, and set the destination S3 URI to the central compliance S3 bucket.
D. Create an AWS Config custom rule that runs an AWS Systems Manager Run Command script across all instances to collect package SBOMs, exporting them via an AWS Config delivery channel to the central bucket.
E. Enable Amazon Macie to scan all EC2 EBS volumes and ECR container layers, and configure Macie to generate and write the CycloneDX compliance report to S3.

---

### Question 5 (Macie Custom Identifiers Regex)
A defense contractor processes documents in S3 containing proprietary project tracking IDs. The tracking IDs follow a strict format: `PROJ-[4 letters]-[4 digits]` (e.g., `PROJ-ABCD-1234`). To protect intellectual property, the contractor wants to scan S3 buckets using Amazon Macie to identify these IDs, but must prevent false positive matches on generic text. The detection should only trigger if the keyword "ProjectSecret" or "Classified" appears within 40 characters of the matched pattern.
How should this be configured in Macie?
A. Create a custom Amazon Macie data identifier. Define the Regular Expression (regex) as `(?i)\bPROJ-[A-Z]{4}-\d{4}\b`. Add the keywords "ProjectSecret" and "Classified", and configure the maximum proximity distance to 40 characters.
B. Configure an EventBridge rule that triggers on S3 object uploads, invoking a Lambda function that downloads the object, runs the regex `(?i)\bPROJ-[A-Z]{4}-\d{4}\b` on the content, and checks for keywords within 40 characters.
C. Create an AWS Glue classifier to parse all files in S3. Configure Amazon Athena to query the metadata tables and identify occurrences of the pattern and keywords.
D. Use a Macie managed data identifier for custom patterns, and write an AWS WAF rule to block S3 access to any client requesting objects that contain matches.

---

### Question 6 (S3 Access Grants AD Groups)
A business intelligence platform stores analytics datasets in a single Amazon S3 bucket. The data is organized into prefixes by department, such as `s3://corp-analytics/finance/` and `s3://corp-analytics/marketing/`. The security team manages corporate identities in a third-party directory linked with AWS IAM Identity Center. They need a solution to map Active Directory (AD) groups directly to their corresponding S3 prefixes, avoiding the complexity of writing large S3 bucket policies or managing separate IAM roles for every group.
Which solution meets these requirements with the **least administrative complexity**?
A. Write a single S3 bucket policy with hundreds of conditional statements checking the user's `aws:PrincipalTag` or active directory groups, and deny-all access unless the tags match the target prefix.
B. Enable S3 Access Grants on the S3 bucket. Register the bucket with S3 Access Grants, and associate S3 Access Grants with the active AWS IAM Identity Center instance. Create access grants that map each corporate AD group directly to its corresponding S3 prefix with the appropriate permission level (e.g., READ or READWRITE).
C. Create an IAM role for each department. Write a central broker Lambda function that issues short-lived credentials via `AssumeRole` after querying the user's AD group membership via LDAP.
D. Implement an S3 Access Point for each department, and attach an access point policy that restricts access to specific IAM roles mapped to individual AD users.

---

### Question 7 (Cross-Domain: API Gateway Custom Authorizer & Macie S3)
An application collects feedback files from customers via an Amazon API Gateway endpoint, which writes the files to an S3 bucket. The security policy demands that:
1. Any incoming HTTP POST request containing a proprietary product key matching the regex `PROD-[A-Z]{3}-\d{5}` in the request header `X-Product-Key` must be blocked at the API Gateway edge.
2. The destination S3 bucket must be scanned continuously to identify any uploaded objects containing this pattern with the keyword "InternalOnly" within 30 characters.
Which architecture implements this with the **least operational overhead**?
A. Apply an API Gateway Resource Policy that denies access if the request headers contain a match for `PROD-[A-Z]{3}-\d{5}`. Set up Amazon Macie with a custom data identifier using the regex and the keyword, targeted at the S3 bucket.
B. Create an API Gateway Custom Lambda Authorizer of type `REQUEST` that inspects the incoming headers, returning a DENY policy if the `X-Product-Key` matches the `PROD-[A-Z]{3}-\d{5}` regex. Configure Amazon Macie with a custom data identifier specifying the same regex, keyword "InternalOnly", and a maximum proximity distance of 30 characters, targeted at the S3 bucket.
C. Configure an AWS WAF Web ACL associated with API Gateway using a regex pattern match rule to block the headers. Create an AWS Config custom rule that invokes a Lambda function to download and scan every new S3 object for the pattern and keywords.
D. Use a Cognito User Pool with a custom trigger Lambda to validate the product key in the headers. Set up Amazon GuardDuty Malware Protection on the S3 bucket to scan for the pattern.

---

### Question 8 (Private API Resource Policy & mTLS) — **Select TWO**
A company has configured an Amazon API Gateway private API that must only be accessible from resources inside a specific corporate VPC (`vpc-333333`) via an interface VPC endpoint (`vpce-444444`). Additionally, the security team requires that only client applications running with a specific security group (`sg-555555`) are allowed to call the private API.
Which combination of configurations is required to enforce this security model? (Select TWO)
A. Attach an API Gateway Resource Policy to the private API that denies invoke access to any requests unless the VPC endpoint matches `vpce-444444`.
B. Configure the security group associated with the Interface VPC Endpoint to allow inbound HTTPS (port 443) traffic only from the client security group `sg-555555`.
C. Configure an IAM Role for the client applications that allows `execute-api:Invoke` on the private API, and restrict the role's trust policy to the security group `sg-555555`.
D. Create an API Gateway custom domain name, enable mutual TLS (mTLS), and upload a trust store file listing the security group ID as a trusted client certificate.
E. Enable AWS WAF on the private API, and configure an IP set rule allowing only the CIDR range of the subnet containing the clients.

---

### Question 9 (CloudFront FLE & KMS S3 Context)
A company uses CloudFront Field-Level Encryption (FLE) to encrypt customer identification numbers (tax IDs) at the edge before sending them to an ECS-based payment microservice. The application origin server running in ECS decrypts the tax IDs using an RSA private key and then stores the decrypted transactions in an Amazon S3 bucket. The compliance team mandates that:
1. The S3 bucket must use server-side encryption with AWS KMS (SSE-KMS) with a customer managed key (CMK).
2. The CMK key policy must strictly deny any decryption or generation of keys unless the KMS operation includes an encryption context containing `"System": "Billing"`.
How should the security engineer implement this key policy restriction?
A. Configure the CloudFront Field-Level Encryption profile to pass the encryption context `{"System": "Billing"}` during the edge encryption handshake.
B. In the KMS CMK key policy, add a condition block for `StringEquals` checking `kms:EncryptionContext:System` is `"Billing"`. In the application code running on ECS, pass the encryption context `{"System": "Billing"}` when performing KMS operations to store or retrieve the payload from S3.
C. Set up an S3 Bucket Policy that denies `s3:PutObject` if the request header `x-amz-server-side-encryption-context` is missing the billing system value. CloudFront will automatically carry this context to S3.
D. Attach an IAM Role policy to the ECS tasks that allows `kms:Decrypt` and configure S3 default bucket encryption with the context parameters enabled in the KMS configuration console.

---

### Question 10 (Inspector SBOM S3 & Object Lock Compliance)
An enterprise requires that all Software Bill of Materials (SBOM) reports generated and exported by Amazon Inspector must be stored in a WORM (Write Once Read Many) compliant manner to satisfy external security audit demands. Once written, the SBOM reports must be mathematically protected from deletion, modification, or overwriting by any user, including the AWS account administrator and the Root account, for a minimum period of 3 years.
Which solution meets this compliance requirement with the **least administrative overhead**?
A. Create an S3 bucket with S3 Object Lock enabled. Configure a default bucket retention mode of **Compliance** with a retention period of 3 years. Direct Amazon Inspector to export all SBOM reports to this bucket.
B. Create an S3 bucket with S3 Object Lock enabled. Configure a default bucket retention mode of **Governance** with a retention period of 3 years, and assign the `s3:BypassGovernanceRetention` permission only to the root user.
C. Write an S3 Bucket Policy on the destination bucket that explicitly denies `s3:DeleteObject`, `s3:DeleteObjectVersion`, and `s3:PutObject` if the object already exists, for all principals (`*`).
D. Set up an AWS Config custom rule that monitors the destination S3 bucket. If any object is deleted or modified, invoke an SSM Automation document to redeploy the deleted SBOM file from the Amazon Inspector console cache.

---

## Never-Seen Blueprint Topics (MUST TEST before exam)

> These topics are explicitly in the SCS-C03 blueprint but have ZERO questions in 912 attempts.
> Distributed across weekly sessions and bi-weekly mocks below.

| # | Topic | Blueprint Task | Scheduled |
|---|---|---|---|
| 1 | API Gateway security (authorizers, resource policies, mutual TLS) | Task 3.1 | Week 2 |
| 2 | VPC Lattice (service-to-service auth, auth policies) | Task 3.3 | Week 4 |
| 3 | CloudFront Field-Level Encryption | Task 3.1 | Week 2 |
| 4 | Inspector SBOM export | Task 3.2 | Week 2 |
| 5 | WAF Bot Control (token challenges, CAPTCHA, scope-down) | Task 3.1 | Week 4 |
| 6 | CloudFormation Guard (policy-as-code) | Task 6.2 | Week 3 |
| 7 | Systems Manager State Manager (desired-state) | Task 1.1 | Week 3 |
| 8 | Amazon Data Lifecycle Manager (EBS snapshot automation) | Task 5.2 | Week 5 |
| 9 | AWS DataSync (secure data transfer) | Task 5.2 | Week 5 |
| 10 | Macie custom data identifiers (regex, keywords) | Task 1.1 | Week 2 |
| 11 | Resilience Hub (assess RTO/RPO) | Task 2.1 | Week 7 |
| 12 | FIS (chaos engineering, test IR plans) | Task 2.1 | Week 7 |
| 13 | Application Recovery Controller (zonal shift) | Task 2.1 | Week 7 |
| 14 | Amazon Q Developer / CodeGuru Security | Task 3.2 | Week 4 |
| 15 | Well-Architected Tool (security pillar) | Task 6.3 | Week 5 |
| 16 | Automated Forensics Orchestrator for EC2 | Task 2.1 | Week 7 |
| 17 | SageMaker AI notebooks for IR | Task 2.1 | Week 7 |
| 18 | EMR / EKS inter-node encryption | Task 5.1 | Week 5 |

---

## Upcoming Weeks

| Week | Dates | Focus | Never-Seen Topics Included | Status |
|------|-------|-------|----------------------------|--------|
| 1 | Jun 16-22 | ACM cross-region, IoT ThingName, Kinesis+OpenSearch, Config custom rules, S3 Batch Operations | — (recent gaps from Sessions 86-90) | ✅ 90% (Session 92) |
| 2 | Jun 23-29 | **NEVER-SEEN BLITZ 1:** API Gateway security, CloudFront Field-Level Encryption, Inspector SBOM, Macie custom identifiers, S3 Access Grants | #1, #3, #4, #10 | ⬜ Current |
| 3 | Jun 30 - Jul 6 | D1 weak areas + **NEVER-SEEN:** CloudFormation Guard, SSM State Manager | #6, #7 | ⬜ |
| 4 | Jul 7-13 | **NEVER-SEEN BLITZ 2:** VPC Lattice, WAF Bot Control, CodeGuru Security, Private CA advanced | #2, #5, #14 | ⬜ |
| 5 | Jul 14-20 | Cross-domain killer + **NEVER-SEEN:** Data Lifecycle Manager, DataSync, Well-Architected Tool, EMR inter-node | #8, #9, #15, #18 | ⬜ |
| 6 | Jul 21-27 | Re-test all ⚠️/❌ from Sessions 81+ | — (consolidation) | ⬜ |
| 7 | Jul 28 - Aug 3 | **NEVER-SEEN BLITZ 3:** Resilience Hub, FIS, Application Recovery Controller, Automated Forensics Orchestrator, SageMaker IR notebooks | #11, #12, #13, #16, #17 | ⬜ |

**Note:** Session 97 (Jun 17) already tested 14 of 18 never-seen topics. Only 4 remain with errors needing re-test: API GW mTLS (#1), Inspector SBOM scheduling (#4), State Manager dual triggers (#7), EMR in-transit (#18). All others passed.
| 8 | Aug 4-10 | D1 Detection final push (target 80%) | — | ⬜ |
| 9 | Aug 11-17 | Cross-domain 65-question untimed simulation (includes all never-seen) | ALL remaining | ⬜ |
| 10 | Aug 18-24 | Cheat sheet review + 2 short drills only | — | ⬜ |
