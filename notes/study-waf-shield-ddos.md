# Study Notes: WAF Bot Control & Shield Advanced DDoS

## Key Concepts

1. **WAF Bot Control**:
   - Analyzes client behavior and signatures to detect scraper bots, search engines, and malicious automated scripts.
   - Use WAF Scope-down policies to run Bot Control rules only on specific endpoints (e.g., `/login`, `/checkout`) to optimize cost.

2. **AWS Shield Advanced**:
   - Provides near real-time visibility into DDoS attacks.
   - Offers automatic layer 7 DDoS mitigation (creates custom WAF rules dynamically).
   - Protects against cost spikes from web-tier resources during massive scaling attacks.
   - Integrates directly with Route 53, CloudFront, ALB, and Global Accelerator.
