# Technology Stack
- **Primary Cloud:** AWS (Focus on Security Services: KMS, GuardDuty, WAF, Security Hub, IAM, Cognito).
- **Infrastructure as Code:** Terraform or AWS CDK (TypeScript).
- **Container Security:** Kubernetes (EKS) + Istio (Service Mesh).
- **Diagramming:** Mermaid.js (for logical flows) and AWS Architecture Icons.


Rule for FAQ Generation: When creating faq-*.md files, prioritize information about encryption, logging, and IAM permissions. Deprioritize pricing and basic "what is this service" definitions. I already know what the service does; I need to know how to secure it and also put information about quotas of the services because that always appears in the exam

## Constraints
- **Security First:** Every piece of code or architecture generated MUST follow the **AWS Well-Architected Framework (Security Pillar)**.
- **Least Privilege:** Always default to "Deny" policies. Never suggest `Action: "*"` or `Principal: "*"`.
