# FAQ: ACM Private CA

> **Blueprint refs:** Task 5.1 (data in transit), Task 5.3.5 (multi-region key/cert management)
> **New in C03:** Yes — Task 5.3.5 explicitly added

## ACM Public vs ACM Private CA

| | ACM Public | ACM Private CA |
|---|---|---|
| **Domain validation** | Must own public domain | Any name (internal hostnames, IPs) |
| **Export private key** | ❌ Never | ✅ Yes |
| **Install on your app** | ❌ Only AWS services (ALB, CloudFront, API GW) | ✅ EC2, containers, on-prem |
| **Use case** | Public websites HTTPS | Internal mTLS, service mesh, IoT, Network Firewall TLS inspection |
| **Cost** | Free | ~$400/month per CA + $0.75/cert |
| **Cross-region** | Per-region (re-issue in each region) | Share CA hierarchy across regions |
| **Rotation** | Auto-renew (if attached to AWS service) | You manage renewal (or automate via Lambda) |

## When to Use (Exam Signals)

| Signal | Answer |
|---|---|
| "Internal TLS" / "mTLS between services" | **ACM Private CA** |
| "Private certificates for internal hostnames" | **ACM Private CA** |
| "Network Firewall TLS inspection CA" | **ACM Private CA** |
| "IoT device certificates" | **ACM Private CA** |
| "Public website HTTPS on ALB/CloudFront" | **ACM public** (free) |

## CA Hierarchy

```
Root CA (offline, long-lived, ~10yr validity)
  └── Subordinate CA (online, shorter-lived, issues end-entity certs)
        ├── orders.prod.internal
        ├── payments.prod.internal
        └── *.staging.internal
```

- Root CA can be external (on-prem HSM) with subordinate in ACM Private CA
- Or both root + subordinate in ACM Private CA

## Cross-Region (Task 5.3.5)

- CA itself lives in ONE region
- Certs issued by that CA can be used ANYWHERE (export private key → deploy globally)
- For HA: create subordinate CAs in multiple regions under same root
- Combine with **Multi-Region KMS keys** for cross-region encryption + cross-region certs

## Key Limits/Quotas

| Limit | Value |
|---|---|
| CAs per account per region | 200 |
| Certificates per CA (lifetime) | Unlimited |
| Certificate validity | Up to 10 years (end-entity), 10+ years (CA) |
| Cost per CA | ~$400/month |
| Cost per certificate | $0.75 (first 1000), lower at scale |

## Exam Gotchas

| Gotcha | Detail |
|---|---|
| **Can't export ACM public cert private key** | Only Private CA certs are exportable |
| **$400/month per CA** | Expensive — exam may test cost awareness |
| **Short-lived certs** | Can issue certs valid for hours/days (IoT, ephemeral workloads) |
| **CRL + OCSP** | Private CA supports both for revocation checking |
| **CloudHSM is NOT for issuing certs** | CloudHSM stores keys; Private CA issues certs. Different jobs. |
| **Network Firewall TLS inspection** | Requires Private CA cert — firewall acts as MITM, must distribute CA to client trust stores |

## K8s Mapping

```
ACM Private CA  ≈  cert-manager with a private ClusterIssuer
CA hierarchy    ≈  Root CA → Intermediate → cert-manager issues leaf certs
Cross-region    ≈  Sharing CA bundle across multiple clusters
```

## 🧠 Cheat-Sheet One-Liners

- **ACM public = free, public domains, can't export key. ACM Private CA = $400/mo, any name, exportable, mTLS.**
- **"Internal TLS" / "mTLS" / "private hostnames" → ACM Private CA. "Public HTTPS" → ACM public.**
- **Network Firewall TLS inspection needs Private CA — distribute CA cert to client trust stores or users get warnings.**
