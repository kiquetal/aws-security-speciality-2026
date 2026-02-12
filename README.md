# AWS Certified Security - Specialty (SCS-C03) Study Repository

This repository serves as a centralized study environment for the **AWS Certified Security - Specialty (SCS-C03)** exam. It contains structured notes, architectural deep-dives, and hands-on labs designed for senior engineers.

## 🎯 Goal
The primary objective of this repository is to facilitate a deep understanding of AWS security services and architectures. It moves beyond rote memorization towards architectural mastery, focusing on the *why* and *how* of secure cloud design.

## 📚 Repository Structure
- **`notes/`**: Detailed FAQ and overview documents for key AWS services (IAM, KMS, S3, GuardDuty, etc.).
- **`blueprint.md`**: A detailed breakdown of the SCS-C03 exam domains and task statements.
- **`.kiro/`**: Internal steering and configuration for the study environment.

## 🛠️ MCP Tools
This project integrates with Model Context Protocol (MCP) servers to enhance the learning experience:
- **Fetch**: Retrieve documentation and external web content.
- **Excalidraw**: Create and visualize architectural diagrams directly through the CLI.

## 🚀 Getting Started
1. **Explore the Notes**: Start with `notes/iam-overview.md` or dive into specific service FAQs.
2. **Review the Blueprint**: Check `blueprint.md` to align your study path with exam domains.
3. **Run the Excalidraw Canvas**:
   To use the architectural diagramming tools, you need to run the Excalidraw Canvas. You can do this using Docker:
   ```bash
   docker run -d -p 3000:3000 --name mcp-excalidraw-canvas ghcr.io/yctimlin/mcp_excalidraw-canvas:latest
   ```
   Alternatively, use the provided `docker-compose.yml`:
   ```bash
   docker compose up -d
   ```
4. **Configure MCP Tools**:
   The Excalidraw MCP server is configured in `.kiro/settings/mcp.json`. Ensure the `EXPRESS_SERVER_URL` environment variable matches your running canvas instance (defaulting to `http://localhost:3000`).

## 🛡️ Best Practices
When contributing or studying:
- **IAM Policies**: Always adhere to the principle of least privilege. Use `Condition` keys and specific resource ARNs.
- **Active Recall**: Challenge yourself with questions before reading the answers.
- **Hands-on**: Validate architectural patterns in a sandbox AWS environment.
