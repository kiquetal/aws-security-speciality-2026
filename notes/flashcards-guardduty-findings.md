# GuardDuty Finding ThreatPurpose Decision Tree

> Finding format: `ThreatPurpose:ResourceType/ThreatName!DataSource`
> Example: `CryptoCurrency:EC2/BitcoinTool.B!DNS`

---

## ThreatPurpose Decision Tree

```
What is the instance DOING?
│
├─ DNS query only (no TCP connection)?
│  └─ IMPACT (always, regardless of destination)
│     Examples: BitcoinDomainRequest.Reputation, MaliciousDomainRequest
│
├─ Active TCP to mining pool (port 3333, pool.*, xmr.*)?
│  └─ CRYPTOCURRENCY
│     Examples: BitcoinTool.B, CryptoMinerTool
│
├─ Active TCP to C2 server (beacon, command channel)?
│  └─ TROJAN
│     Examples: C2Activity.B, DriveBySourceTraffic, DGADomainRequest
│
├─ Port scanning / probing (outbound OR inbound)?
│  └─ RECON
│     Examples: PortProbeUnprotectedPort, Portscan
│
├─ Credentials from unusual location / Tor / anonymous proxy?
│  └─ UNAUTHORIZED ACCESS
│     Examples: TorIPCaller, AnomalousBehavior, ConsoleLogin
│
├─ Data transfer anomaly (S3 large download, unusual geo)?
│  └─ EXFILTRATION
│     Examples: AnomalousBehavior (S3), ObjectRead.Unusual
│
├─ Bucket/resource misconfiguration detected?
│  └─ POLICY
│     Examples: RootCredentialUsage, BucketAnonymousAccessGranted
│
└─ Malware/backdoor on instance?
   └─ BACKDOOR or TROJAN
      Examples: Backdoor:EC2/DenialOfService, Trojan:EC2/DropPoint
```

---

## Quick Lookup Table

| Scenario | ThreatPurpose | Key Signal |
|---|---|---|
| DNS query to mining pool | **Impact** | DNS only = always Impact |
| DNS query to C2 domain | **Impact** | DNS only = always Impact |
| DNS query to ANY bad domain | **Impact** | DNS only = always Impact |
| Active TCP to mining pool | **CryptoCurrency** | Connection established + mining |
| Active TCP to C2 IP | **Trojan** | Connection established + C2 |
| EC2 scanning ports outbound | **Recon** | Probing |
| External IP scanning your EC2 | **Recon** | Probing |
| Creds used from Tor exit node | **UnauthorizedAccess** | Unusual identity behavior |
| Creds used from new country | **UnauthorizedAccess** | Unusual identity behavior |
| S3 downloads unusual volume/geo | **Exfiltration** | Data leaving |
| Root account API call | **Policy** | Risky configuration/usage |
| Bucket made public | **Policy** | Risky configuration |

---

## The Two-Finding Attack Progression

```
Time 14:30 — DNS query to bad domain
             Finding: Impact:EC2/MaliciousDomainRequest

Time 14:45 — TCP connection established to resolved IP
             ├─ If mining pool → CryptoCurrency:EC2/BitcoinTool.B
             └─ If C2 server  → Trojan:EC2/C2Activity.B
```

**Rule:** DNS = always Impact (stage 1). TCP determines stage 2 based on DESTINATION TYPE.

---

## DataSource Suffix (!DNS, !VPCFlowLogs, !CloudTrail)

| Suffix | Meaning |
|---|---|
| `!DNS` | Detected from DNS log analysis |
| `!VPCFlowLogs` | Detected from VPC Flow Log analysis |
| `!CloudTrail` | Detected from CloudTrail analysis |
| (no suffix) | Multiple sources or runtime agent |

Suffix = HOW it was detected, not WHAT the attack does.

---

## Common Traps

| Trap | Truth |
|---|---|
| "DNS to mining pool = CryptoCurrency" | ❌ DNS only = Impact. Active TCP = CryptoCurrency |
| "Outbound to bad IP = Recon" | ❌ Outbound to bad IP = Trojan (C2). Recon = port scanning |
| "GuardDuty fires on blocked attempts" | ❌ GD needs SUCCESSFUL access. RCP blocks = no finding |
| "Discovery = DNS query" | ❌ Discovery = resource enumeration. DNS query = Impact |

---

## Custom Threat List → `.Custom` Suffix

```
Built-in AWS threat intel:
  EC2 connects to known C2 IP → UnauthorizedAccess:EC2/MaliciousIPCaller

YOUR custom threat list (uploaded IPs):
  EC2 connects to YOUR listed IP → UnauthorizedAccess:EC2/MaliciousIPCaller.Custom
                                                                          ^^^^^^^
                                                                     YOUR list = .Custom
```

| Source | Finding Name | Example |
|---|---|---|
| AWS built-in threat intel | Standard type (no suffix) | `Trojan:EC2/C2Activity.B` |
| Your custom threat IP list | `.Custom` suffix appended | `UnauthorizedAccess:EC2/MaliciousIPCaller.Custom` |

**Rule:** See `.Custom` in a finding → traffic matched YOUR uploaded threat list, not AWS's built-in intel.
