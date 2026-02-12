# Technology Stack
- **Primary Cloud:** AWS
  - **Identity:** IAM, Cognito, IAM Identity Center, Verified Permissions.
  - **Detection:** GuardDuty, Security Hub, Macie, Config, Security Lake (OCSF).
  - **Infrastructure:** WAF, Shield, Network Firewall, VPC Endpoints, PrivateLink.
  - **Data Protection:** KMS (CMK vs AWS Managed, Symmetric vs Asymmetric), CloudHSM, Secrets Manager.
  - **Governance:** AWS Organizations, Control Tower, SCPs, Resource Control Policies (RCPs).
- **Infrastructure as Code:** Terraform or AWS CDK (TypeScript).
- **Container Security:** Kubernetes (EKS) + Istio (Service Mesh).
- **Diagramming:** Mermaid.js (for logical flows) and AWS Architecture Icons.


Rule for FAQ Generation: When creating faq-*.md files, prioritize information about encryption, logging, and IAM permissions. Deprioritize pricing and basic "what is this service" definitions. I already know what the service does; I need to know how to secure it and also put information about quotas of the services because that always appears in the exam

## Constraints
- **Security First:** Every piece of code or architecture generated MUST follow the **AWS Well-Architected Framework (Security Pillar)**.
- **Least Privilege:** Always default to "Deny" policies. Never suggest `Action: "*"` or `Principal: "*"`.
