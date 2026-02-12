# AWS Certified Security - Specialty (SCS-C03) Exam Blueprint

## Exam Version
**SCS-C03** - Current version as of December 2025

## Exam Details
- **Duration:** 170 minutes
- **Number of Questions:** 65 (50 scored + 15 unscored)
- **Passing Score:** 750 (on a scale of 100-1,000)
- **Question Types:** Multiple choice, Multiple response, Ordering, Matching
- **Cost:** $300 USD

## Domain Weights

| Domain | Weight | Focus Area |
|--------|--------|------------|
| Domain 1: Detection | 16% | Monitoring, alerting, and logging solutions |
| Domain 2: Incident Response | 14% | Response plans, forensics, and remediation |
| Domain 3: Infrastructure Security | 18% | Network, compute, and edge security controls |
| Domain 4: Identity and Access Management | 20% | Authentication and authorization strategies |
| Domain 5: Data Protection | 18% | Encryption, secrets management, data integrity |
| Domain 6: Security Foundations and Governance | 14% | Multi-account strategy, compliance, IaC |

---

## Domain 1: Detection (16%)

### Task Statement 1.1: Design and implement monitoring and alerting solutions for an AWS account or organization

**Skills:**
- Analyze workloads to determine monitoring requirements.
- Design and implement workload monitoring strategies (for example, by configuring resource health checks).
- Aggregate security and monitoring events.
- Create metrics, alerts, and dashboards to detect anomalous data and events (for example, Amazon GuardDuty, Amazon Security Lake, AWS Security Hub, Amazon Macie).
- Create and manage automations to perform regular assessments and investigations (for example, by deploying AWS Config conformance packs, Security Hub, AWS Systems Manager State Manager).

**Key Services:**
- Amazon GuardDuty
- Amazon Security Lake
- AWS Security Hub
- Amazon Macie
- AWS Config
- AWS Systems Manager State Manager
- Amazon CloudWatch

### Task Statement 1.2: Design and implement logging solutions

**Skills:**
- Identify sources for log ingestion and storage based on requirements.
- Configure logging for AWS services and applications (for example, by configuring an AWS CloudTrail trail for an organization, by creating a dedicated Amazon CloudWatch logging account, by configuring the Amazon CloudWatch Logs agent).
- Implement log storage and log data lakes (for example, Security Lake) and integrate with third-party security tools.
- Use AWS services to analyze logs (for example, CloudWatch Logs Insights, Amazon Athena, Security Hub findings).
- Use AWS services to normalize, parse, and correlate logs (for example, Amazon OpenSearch Service, AWS Lambda, Amazon Managed Grafana).
- Determine and configure appropriate log sources based on network design, threats, and attacks (for example, VPC Flow Logs, transit gateway flow logs, Amazon Route 53 Resolver logs).

**Key Services:**
- AWS CloudTrail
- Amazon CloudWatch Logs
- Amazon Security Lake
- Amazon Athena
- Amazon OpenSearch Service
- AWS Lambda
- Amazon Managed Grafana
- VPC Flow Logs
- Transit Gateway Flow Logs
- Amazon Route 53 Resolver Logs

### Task Statement 1.3: Troubleshoot security monitoring, logging, and alerting solutions

**Skills:**
- Analyze the functionality, permissions, and configuration of resources (for example, Lambda function logging, Amazon API Gateway logging, health checks, Amazon CloudFront logging).
- Remediate misconfiguration of resources (for example, by troubleshooting CloudWatch Agent configurations, troubleshooting missing logs).

**Key Services:**
- AWS Lambda
- Amazon API Gateway
- Amazon CloudFront
- Amazon CloudWatch Agent

---

## Domain 2: Incident Response (14%)

### Task Statement 2.1: Design and test an incident response plan

**Skills:**
- Design and implement response plans and runbooks to respond to security incidents (for example, Systems Manager OpsCenter, Amazon SageMaker AI notebooks).
- Use AWS service features and capabilities to configure services to be prepared for incidents (for example, by provisioning access, deploying security tools, minimizing the blast radius, configuring AWS Shield Advanced protections).
- Recommend procedures to test and validate the effectiveness of an incident response plan (for example, AWS Fault Injection Service, AWS Resilience Hub).
- Use AWS services to automatically remediate incidents (for example, Systems Manager, Automated Forensics Orchestrator for Amazon EC2, AWS Step Functions, Amazon Application Recovery Controller, Lambda functions).

**Key Services:**
- AWS Systems Manager OpsCenter
- Amazon SageMaker AI
- AWS Shield Advanced
- AWS Fault Injection Service
- AWS Resilience Hub
- Automated Forensics Orchestrator for Amazon EC2
- AWS Step Functions
- Amazon Application Recovery Controller
- AWS Lambda

### Task Statement 2.2: Respond to security events

**Skills:**
- Capture and store relevant system and application logs as forensic artifacts.
- Search and correlate logs for security events across applications and AWS services.
- Validate findings from AWS security services to assess the scope and impact of an event.
- Respond to affected resources by containing and eradicating threats, and recover resources (for example, by implementing network containment controls, restoring backups).
- Describe methods to conduct root cause analysis (for example, Amazon Detective).

**Key Services:**
- Amazon Detective
- AWS CloudTrail
- Amazon CloudWatch Logs
- AWS Security Hub
- Amazon GuardDuty
- AWS Backup

---

## Domain 3: Infrastructure Security (18%)

### Task Statement 3.1: Design, implement, and troubleshoot security controls for network edge services

**Skills:**
- Define and select edge security strategies based on anticipated threats and attacks.
- Implement appropriate network edge protection (for example, CloudFront headers, AWS WAF, AWS IoT policies, protecting against OWASP Top 10 threats, Amazon S3 cross-origin resource sharing [CORS], Shield Advanced).
- Design and implement AWS edge controls and rules based on requirements (for example, geography, geolocation, rate limiting, client fingerprinting).
- Configure integrations with AWS edge services and third-party services (for example, by ingesting data in Open Cybersecurity Schema Framework [OCSF] format, by using third-party WAF rules).

**Key Services:**
- Amazon CloudFront
- AWS WAF
- AWS Shield Advanced
- AWS IoT Core
- Amazon S3 (CORS)

**Key Concepts:**
- OWASP Top 10
- Open Cybersecurity Schema Framework (OCSF)
- Rate limiting
- Client fingerprinting

### Task Statement 3.2: Design, implement, and troubleshoot security controls for compute workloads

**Skills:**
- Design and implement hardened Amazon EC2 AMIs and container images to secure compute workloads and embed security controls (for example, Systems Manager, EC2 Image Builder).
- Apply instance profiles, service roles, and execution roles appropriately to authorize compute workloads.
- Scan compute resources for known vulnerabilities (for example, scan container images and Lambda functions by using Amazon Inspector, monitor compute runtimes by using GuardDuty).
- Deploy patches across compute resources to maintain secure and compliant environments by automating update processes and by integrating continuous validation (for example, Systems Manager Patch Manager, Amazon Inspector).
- Configure secure administrative access to compute resources (for example, Systems Manager Session Manager, EC2 Instance Connect).
- Configure security tools to discover and remediate vulnerabilities within a pipeline (for example, Amazon Q Developer, Amazon CodeGuru Security).
- Implement protections and guardrails for generative AI applications (for example, by applying GenAI OWASP Top 10 for LLM Applications protections).

**Key Services:**
- Amazon EC2
- EC2 Image Builder
- AWS Systems Manager (Session Manager, Patch Manager)
- Amazon Inspector
- Amazon GuardDuty
- EC2 Instance Connect
- Amazon Q Developer
- Amazon CodeGuru Security

**Key Concepts:**
- GenAI OWASP Top 10 for LLM Applications
- Container image hardening
- Instance profiles vs. service roles vs. execution roles

### Task Statement 3.3: Design and troubleshoot network security controls

**Skills:**
- Design and troubleshoot appropriate network controls to permit or prevent network traffic as required (for example, security groups, network ACLs, AWS Network Firewall).
- Design secure connectivity between hybrid and multi-cloud networks (for example, AWS Site-to-Site VPN, AWS Direct Connect, MAC Security [MACsec]).
- Determine and configure security workload requirements for communication between hybrid environments and AWS (for example, by using AWS Verified Access).
- Design network segmentation based on security requirements (for example, north/south and east/west traffic protections, isolated subnets).
- Identify unnecessary network access (for example, AWS Verified Access, Network Access Analyzer, Amazon Inspector network reachability findings).

**Key Services:**
- Security Groups
- Network ACLs
- AWS Network Firewall
- AWS Site-to-Site VPN
- AWS Direct Connect
- AWS Verified Access
- Network Access Analyzer
- Amazon Inspector

**Key Concepts:**
- MACsec (MAC Security)
- North/south vs. east/west traffic
- Network segmentation strategies

---

## Domain 4: Identity and Access Management (20%)

### Task Statement 4.1: Design, implement, and troubleshoot authentication strategies

**Skills:**
- Design and establish identity solutions for human, application, and system authentication (for example, AWS IAM Identity Center, Amazon Cognito, multi-factor authentication [MFA], identity provider [IdP] integration).
- Configure mechanisms to issue temporary credentials (for example, AWS Security Token Service [AWS STS], Amazon S3 presigned URLs).
- Troubleshooting authentication issues (for example, CloudTrail, Amazon Cognito, IAM Identity Center permission sets, AWS Directory Service).

**Key Services:**
- AWS IAM Identity Center
- Amazon Cognito
- AWS Security Token Service (STS)
- Amazon S3 (presigned URLs)
- AWS CloudTrail
- AWS Directory Service

**Key Concepts:**
- Multi-factor authentication (MFA)
- Identity Provider (IdP) integration
- Temporary credentials

### Task Statement 4.2: Design, implement, and troubleshoot authorization strategies

**Skills:**
- Design and evaluate authorization controls for human, application, and system access (for example, Amazon Verified Permissions, IAM paths, IAM Roles Anywhere, resource policies for cross-account access, IAM role trust policies).
- Design attribute-based access control (ABAC) and role-based access control (RBAC) strategies (for example, by configuring resource access based on tags or attributes).
- Design, interpret, and implement IAM policies by following the principle of least privilege (for example, permission boundaries, session policies).
- Analyze authorization failures to determine causes or effects (for example, IAM Policy Simulator, IAM Access Analyzer).
- Investigate and correct unintended permissions, authorizations, or privileges granted to a resource, service, or entity (for example, IAM Access Analyzer).

**Key Services:**
- Amazon Verified Permissions
- AWS IAM (policies, roles, permission boundaries, session policies)
- IAM Roles Anywhere
- IAM Policy Simulator
- IAM Access Analyzer

**Key Concepts:**
- Attribute-Based Access Control (ABAC)
- Role-Based Access Control (RBAC)
- Principle of least privilege
- Permission boundaries
- Session policies
- Cross-account access patterns

---

## Domain 5: Data Protection (18%)

### Task Statement 5.1: Design and implement controls for data in transit

**Skills:**
- Design and configure mechanisms to require encryption when connecting to connect to resources (for example, by configuring Elastic Load Balancing [ELB] security policies, by enforcing TLS configurations).
- Design and configure mechanisms for secure and private access to resources (for example, AWS PrivateLink, VPC endpoints, AWS Client VPN, AWS Verified Access).
- Design and configure inter-resource encryption in transit (for example, inter-node encryption configurations for Amazon EMR, Amazon Elastic Kubernetes Service [Amazon EKS], SageMaker AI, Nitro encryption).

**Key Services:**
- Elastic Load Balancing (ELB)
- AWS PrivateLink
- VPC Endpoints
- AWS Client VPN
- AWS Verified Access
- Amazon EMR
- Amazon EKS
- Amazon SageMaker AI
- AWS Nitro System

**Key Concepts:**
- TLS/SSL configurations
- Inter-node encryption
- Nitro encryption

### Task Statement 5.2: Design and implement controls for data at rest

**Skills:**
- Design, implement, and configure data encryption at rest based on specific requirements (for example, by selecting the appropriate encryption key service such as AWS CloudHSM or AWS Key Management Service [AWS KMS] or by selecting the appropriate encryption type such as client-side encryption or server-side encryption).
- Design and configure mechanisms to protect data integrity (for example, S3 Object Lock, S3 Glacier Vault Lock, versioning, digital code signing, file validation).
- Design automatic lifecycle management and retention solutions for data (for example, S3 Lifecycle policies, S3 Object Lock, Amazon Elastic File System [Amazon EFS] Lifecycle policies, Amazon FSx for Lustre backup policies).
- Design and configure secure data replication and backup solutions (for example, Amazon Data Lifecycle Manager, AWS Backup, ransomware protection, AWS DataSync).

**Key Services:**
- AWS Key Management Service (KMS)
- AWS CloudHSM
- Amazon S3 (Object Lock, Glacier Vault Lock, Lifecycle policies)
- Amazon EFS
- Amazon FSx for Lustre
- Amazon Data Lifecycle Manager
- AWS Backup
- AWS DataSync

**Key Concepts:**
- Client-side vs. server-side encryption
- Data integrity mechanisms
- Versioning strategies
- Ransomware protection
- Lifecycle management

### Task Statement 5.3: Design and implement controls to protect confidential data, credentials, secrets, and cryptographic key materials

**Skills:**
- Design management and rotation of credentials and secrets (for example, AWS Secrets Manager).
- Manage and use imported key material (for example, by managing and rotating imported key material, by managing and configuring external key stores).
- Describe the differences between imported key material and AWS generated key material.
- Mask sensitive data (for example, CloudWatch Logs data protection policies, Amazon Simple Notification Service [Amazon SNS] message data protection).
- Create and manage encryption keys and certificates across a single AWS Region or multiple Regions (for example, AWS KMS customer managed AWS KMS keys, AWS Private Certificate Authority).

**Key Services:**
- AWS Secrets Manager
- AWS KMS (customer managed keys, imported key material, external key stores)
- AWS Private Certificate Authority
- Amazon CloudWatch Logs (data protection policies)
- Amazon SNS (message data protection)

**Key Concepts:**
- Secret rotation strategies
- Imported vs. AWS-generated key material
- External key stores
- Multi-region key management
- Data masking

---

## Domain 6: Security Foundations and Governance (14%)

### Task Statement 6.1: Develop a strategy to centrally deploy and manage AWS accounts

**Skills:**
- Deploy and configure organizations by using AWS Organizations.
- Implement and manage AWS Control Tower in new and existing environments, and deploy optional and custom controls.
- Implement organization policies to manage permissions (for example, SCPs, RCPs, AI service opt-out policies, declarative policies).
- Centrally manage security services (for example, delegated administrator accounts).
- Manage AWS account root user credentials (for example, by centralizing root access for member accounts, managing MFA, designing break-glass procedures).

**Key Services:**
- AWS Organizations
- AWS Control Tower
- Service Control Policies (SCPs)
- Resource Control Policies (RCPs)

**Key Concepts:**
- Delegated administrator accounts
- Root user management
- Break-glass procedures
- AI service opt-out policies
- Declarative policies

### Task Statement 6.2: Implement a secure and consistent deployment strategy for cloud resources

**Skills:**
- Use infrastructure as code (IaC) to deploy cloud resources consistently and securely across accounts (for example, CloudFormation stack sets, third-party IaC tools, CloudFormation Guard, cfn-lint).
- Use tags to organize AWS resources into groups for management (for example, by grouping by department, cost center, environment).
- Deploy and enforce policies and configurations from a central source (for example, AWS Firewall Manager).
- Securely share resources across AWS accounts (for example, AWS Service Catalog, AWS Resource Access Manager [AWS RAM]).

**Key Services:**
- AWS CloudFormation (stack sets, CloudFormation Guard, cfn-lint)
- AWS Firewall Manager
- AWS Service Catalog
- AWS Resource Access Manager (RAM)

**Key Concepts:**
- Infrastructure as Code (IaC)
- Tagging strategies
- Centralized policy enforcement
- Cross-account resource sharing

### Task Statement 6.3: Evaluate the compliance of AWS resources

**Skills:**
- Create or enable rules to detect and remediate noncompliant AWS resources and to send notifications (for example, by using AWS Config to aggregate alerts and remediate non-compliant resources, Security Hub).
- Use AWS audit services to collect and organize evidence (for example, AWS Audit Manager, AWS Artifact).
- Use AWS services to evaluate architecture for compliance with AWS security best practices (for example, AWS Well-Architected Framework tool).

**Key Services:**
- AWS Config
- AWS Security Hub
- AWS Audit Manager
- AWS Artifact
- AWS Well-Architected Tool

**Key Concepts:**
- Compliance automation
- Evidence collection
- AWS Well-Architected Framework (Security Pillar)

---

## Study Recommendations

### Target Candidate Profile
- 3-5 years of experience securing cloud solutions
- Deep understanding of AWS shared responsibility model
- Experience with multi-account governance
- Knowledge of incident response and forensics
- Understanding of encryption methodologies (at-rest and in-transit)

### Out of Scope
- Designing cryptographic algorithms
- Analyzing traffic on the packet level
- Architecting overall cloud deployments
- Managing end-user compute resources
- Training machine learning models

---

## Sources
Content rephrased for compliance with licensing restrictions from:
- [AWS Official Exam Guide](https://docs.aws.amazon.com/aws-certification/latest/examguides/security-specialty-03.html)
- [VMExam SCS-C03 Syllabus](https://www.vmexam.com/aws/aws-security-specialty-certification-exam-syllabus)
