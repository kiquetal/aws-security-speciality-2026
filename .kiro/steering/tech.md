# Technology Stack
- **Primary Cloud:** AWS (Focus on Security Services: KMS, GuardDuty, WAF, Security Hub, IAM, Cognito).
- **Infrastructure as Code:** Terraform or AWS CDK (TypeScript).
- **Container Security:** Kubernetes (EKS) + Istio (Service Mesh).
- **Diagramming:** Mermaid.js (for logical flows) and AWS Architecture Icons.

## Constraints
- **Security First:** Every piece of code or architecture generated MUST follow the **AWS Well-Architected Framework (Security Pillar)**.
- **Least Privilege:** Always default to "Deny" policies. Never suggest `Action: "*"` or `Principal: "*"`.
