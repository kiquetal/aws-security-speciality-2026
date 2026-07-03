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

## Tldraw PNG Diagram Generation

The tldraw MCP (`@talhaorak/tldraw-mcp`) creates `.tldr` files but CANNOT export to PNG.
To generate tldraw-style PNG diagrams, use `@kitschpatrol/tldraw-cli` with this pipeline:

### Pipeline (Node.js script → .tldr → PNG)

1. **Create a Node.js script** that uses Puppeteer + the bundled tldraw editor to create shapes:
   - Server path: `/home/kiquetal/.npm/_npx/88d8eb54362880fe/node_modules/@kitschpatrol/tldraw-cli/dist/tldraw`
   - Import puppeteer from: `/home/kiquetal/.npm/_npx/88d8eb54362880fe/node_modules/puppeteer/lib/esm/puppeteer/puppeteer.js`
   - Import hono server from: `/home/kiquetal/.npm/_npx/88d8eb54362880fe/node_modules/@hono/node-server/dist/index.mjs`
   - Import serveStatic from: `/home/kiquetal/.npm/_npx/88d8eb54362880fe/node_modules/@hono/node-server/dist/serve-static.mjs`
   - Import Hono from: `/home/kiquetal/.npm/_npx/88d8eb54362880fe/node_modules/hono/dist/index.js`

2. **Shape creation rules (tldraw 4.5):**
   - Geo shapes use `richText` (ProseMirror doc), NOT `text` prop
   - Text format: `{ type: 'doc', content: [{ type: 'paragraph', content: [{ type: 'text', text: 'line' }] }] }`
   - Available geo types: rectangle, diamond, ellipse, arrow-right, arrow-left, cloud, star, hexagon, octagon, trapezoid, rhombus, oval
   - Available colors: black, red, orange, yellow, green, blue, violet, light-blue, light-green, light-red, light-violet, grey
   - Fill types: solid, semi, none, pattern
   - Shape types: geo, text, arrow, note, draw, frame

3. **Export the store snapshot** as `.tldr` file from within puppeteer evaluate:
   ```js
   const snapshot = editor.store.getStoreSnapshot();
   const schema = editor.store.schema.serialize();
   return JSON.stringify({ tldrawFileFormatVersion: 1, schema, records: Object.values(snapshot.store) });
   ```

4. **Run tldraw-cli** to render:
   ```bash
   npx @kitschpatrol/tldraw-cli export /tmp/diagram.tldr --format png --output ./diagrams/ --name my-diagram --scale 2
   ```

### Template Script

```js
import puppeteer from '/home/kiquetal/.npm/_npx/88d8eb54362880fe/node_modules/puppeteer/lib/esm/puppeteer/puppeteer.js';
import { serve } from '/home/kiquetal/.npm/_npx/88d8eb54362880fe/node_modules/@hono/node-server/dist/index.mjs';
import { serveStatic } from '/home/kiquetal/.npm/_npx/88d8eb54362880fe/node_modules/@hono/node-server/dist/serve-static.mjs';
import { Hono } from '/home/kiquetal/.npm/_npx/88d8eb54362880fe/node_modules/hono/dist/index.js';
import { writeFileSync } from 'fs';

const app = new Hono();
const tldrawPath = '/home/kiquetal/.npm/_npx/88d8eb54362880fe/node_modules/@kitschpatrol/tldraw-cli/dist/tldraw';
app.get('/tldr-data', (c) => c.text('', 404));
app.use('/*', serveStatic({ root: tldrawPath }));
const server = serve({ fetch: app.fetch, port: 19878 });

const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.goto('http://localhost:19878', { waitUntil: 'networkidle0', timeout: 30000 });

const tldrData = await page.evaluate(() => {
  const editor = window.editor;
  if (!editor) return null;

  function rt(text) {
    const lines = text.split('\n');
    return { type: 'doc', content: lines.map(line => ({
      type: 'paragraph',
      content: line ? [{ type: 'text', text: line }] : undefined
    }))};
  }

  // === CREATE YOUR SHAPES HERE ===
  editor.createShape({ type: 'geo', x: 50, y: 50, props: { w: 200, h: 100, geo: 'rectangle', color: 'blue', fill: 'solid', richText: rt('My Shape') } });

  // Export
  const snapshot = editor.store.getStoreSnapshot();
  const schema = editor.store.schema.serialize();
  return JSON.stringify({ tldrawFileFormatVersion: 1, schema, records: Object.values(snapshot.store) });
});

if (tldrData) { writeFileSync('/tmp/output.tldr', tldrData); console.log("SUCCESS"); }
await browser.close();
server.close();
```

### DO NOT use the tldraw MCP for PNG generation — its schema is incompatible with tldraw-cli.
