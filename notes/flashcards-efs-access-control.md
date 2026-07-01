# EFS Access Control — Flashcard

> EFS has 4 layers of access control. Miss one = either too open or broken.

---

## The 4 Layers

```
Layer 1: Security Group (network)
  → EFS mount target SG: inbound port 2049 from allowed EC2 SGs
  → Without: timeout (can't reach EFS)

Layer 2: IAM Policy (identity — on EC2 role)
  → elasticfilesystem:ClientMount / ClientWrite / ClientRootAccess
  → Without: mount denied (if IAM auth enforced)

Layer 3: EFS File System Policy (resource — on EFS itself)
  → Denies anonymous access (forces IAM auth)
  → Without: anyone with network access mounts freely (IAM bypassed!)

Layer 4: POSIX permissions (file-level)
  → uid/gid on files inside the mounted FS
  → Without: all authenticated users read everything
```

---

## Key Flashcards

```
Q: EC2 has IAM role with ClientMount. No File System Policy on EFS. Is EFS secure?
A: NO — attacker can mount WITHOUT -o iam flag, skipping IAM entirely.
   File System Policy must DENY anonymous to enforce IAM.

Q: What does the -o iam flag do?
A: Client presents IAM credentials (SigV4) to EFS. EFS evaluates IAM policy.
   Without flag = anonymous NFS mount (no identity check).

Q: Is -o tls required with -o iam?
A: YES — IAM auth requires TLS (credentials must be encrypted in transit).

Q: What package is needed for -o tls,iam?
A: amazon-efs-utils (handles TLS + SigV4 signing).

Q: SG alone enough for "only permitted EC2 can access"?
A: NO — SG = network gate (which instances CAN reach). 
   IAM = identity gate (which instances are ALLOWED to mount).
   Same subnet EC2 with different role = SG passes, IAM blocks.

Q: EFS mount target SG port?
A: 2049 (NFS).

Q: ClientMount vs ClientWrite vs ClientRootAccess?
A: Mount = read-only. +Write = read+write. +RootAccess = uid 0 operations.
```

---

## Exam Signals

| Signal | Answer |
|---|---|
| "Only permitted EC2 can access EFS" | SG + IAM policy (both needed) |
| "Enforce encryption in transit to EFS" | File System Policy requiring `aws:SecureTransport: true` |
| "Per-instance access control, same subnet" | IAM (SGs can't distinguish instances in same SG) |
| "EFS + cross-account access" | File System Policy + IAM role + VPC peering/Transit Gateway |
