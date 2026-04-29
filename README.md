# AWS Certified Security - Specialty (SCS-C03) Study Repository

This repository serves as a centralized study environment for the **AWS Certified Security - Specialty (SCS-C03)** exam. It contains structured notes, architectural deep-dives, and hands-on labs designed for senior engineers.

## 🎯 Goal
The primary objective of this repository is to facilitate a deep understanding of AWS security services and architectures. It moves beyond rote memorization towards architectural mastery, focusing on the *why* and *how* of secure cloud design.

## 🔄 SCS-C02 vs. SCS-C03 Key Differences
The SCS-C03 (current version) includes several updates over the previous C02 version:
- **Domain Weight Changes**: Increased focus on IAM (up to 20%) and Detection (16%), with a slight decrease in Incident Response (14%) and Infrastructure Security (18%).
- **New Services**: Inclusion of **Amazon Security Lake**, **Amazon Verified Permissions**, **AWS Verified Access**, and **IAM Roles Anywhere**.
- **Generative AI Security**: New requirements for securing GenAI workloads and using **Amazon Q Developer** and **Amazon CodeGuru Security** for vulnerability discovery.
- **Resource Control Policies (RCPs)**: Advanced governance alongside SCPs for centralized management.
- **Data Masking**: Focus on automated data protection in CloudWatch Logs and SNS.

## 📚 Repository Structure
- **`notes/`**: Detailed FAQ and overview documents for key AWS services (IAM, KMS, S3, GuardDuty, etc.).
- **`blueprint.md`**: A detailed breakdown of the SCS-C03 exam domains and task statements.
- **`.kiro/`**: Internal steering and configuration for the study environment.

## 🛠️ MCP Tools
This project integrates with Model Context Protocol (MCP) servers to enhance the learning experience:
- **Fetch**: Retrieve documentation and external web content.
- **Mermaid**: Create and visualize architectural diagrams using Mermaid syntax directly through the CLI.

## 🚀 Getting Started
1. **Explore the Notes**: Start with `notes/iam-overview.md` or dive into specific service FAQs.
2. **Review the Blueprint**: Check `blueprint.md` to align your study path with exam domains.
3. **Create Diagrams**: Use the Mermaid MCP tool to generate security architecture diagrams, data flow visualizations, and logical flows directly from the CLI.

## 🛡️ Best Practices
When contributing or studying:
- **IAM Policies**: Always adhere to the principle of least privilege. Use `Condition` keys and specific resource ARNs.
- **Active Recall**: Challenge yourself with questions before reading the answers.
- **Hands-on**: Validate architectural patterns in a sandbox AWS environment.
