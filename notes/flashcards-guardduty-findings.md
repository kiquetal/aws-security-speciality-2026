# GuardDuty Finding Types — Flashcard

> Pattern: `ThreatPurpose:ResourceType/ThreatName`

## ThreatPurpose (memorize these 8)

| ThreatPurpose | Meaning | Example Finding |
|---|---|---|
| **UnauthorizedAccess** | Creds used from bad place (Tor, malicious IP) | `UnauthorizedAccess:IAMUser/TorIPCaller` |
| **CryptoCurrency** | Mining crypto | `CryptoCurrency:EC2/BitcoinTool.B` |
| **Trojan** | Malware communicating out | `Trojan:EC2/BlackholeTraffic` |
| **Recon** | Scanning, probing | `Recon:EC2/PortProbeUnprotectedPort` |
| **Exfiltration** | Data leaving your environment | `Exfiltration:S3/AnomalousBehavior` |
| **Impact** | Resource abuse (not crypto) | `Impact:EC2/WinRMBruteForce` |
| **Policy** | Risky config or root usage | `Policy:IAMUser/RootCredentialUsage` |
| **Discovery** | Enumeration of resources | `Discovery:S3/MaliciousIPCaller` |

## ResourceType (the middle part)

| ResourceType | What's affected |
|---|---|
| `IAMUser` | IAM credentials (user or role) |
| `EC2` | EC2 instance |
| `S3` | S3 bucket |
| `EKS` | EKS cluster |
| `RDS` | RDS database |
| `Lambda` | Lambda function |
| `Runtime` | Container/EC2 runtime |

## High-Priority Findings to Know Cold

| Finding | What Happened |
|---|---|
| `UnauthorizedAccess:IAMUser/TorIPCaller` | Creds used from Tor exit node |
| `UnauthorizedAccess:IAMUser/MaliciousIPCaller` | Creds used from known-bad IP |
| `CryptoCurrency:EC2/BitcoinTool.B` | EC2 mining Bitcoin |
| `Recon:EC2/PortProbeUnprotectedPort` | Open port being scanned |
| `Trojan:EC2/BlackholeTraffic` | EC2 sending traffic to black hole |
| `Policy:IAMUser/RootCredentialUsage` | Root account API call |
| `Exfiltration:S3/AnomalousBehavior` | Unusual S3 data transfer |
| `Impact:EC2/BitcoinDomainRequest.Reputation` | EC2 querying crypto domain |

## Memory Trick

```
U-C-T-R-E-I-P-D (say: "U See TRIP-D")

U = UnauthorizedAccess (bad location)
C = CryptoCurrency     (mining)
T = Trojan             (malware)
R = Recon              (scanning)
E = Exfiltration       (data out)
I = Impact             (abuse)
P = Policy             (risky config)
D = Discovery          (enumeration)
```
