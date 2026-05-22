# KMS Key Anatomy — Visual Reference

> **Blueprint refs:** Task 5.2, 5.3
> **Purpose:** Clarify the relationship between alias, key, and key material.

---

## The Three Layers

```
┌─────────────────────────────────────────────────────────────────┐
│  KEY ALIAS (friendly name — a pointer, nothing more)            │
│  alias/my-app-key                                               │
│       │                                                         │
│       │  points to                                              │
│       ▼                                                         │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  KMS KEY (the container — has an ID, ARN, policies)       │  │
│  │  key-id: abc-123-def-456                                  │  │
│  │  ARN: arn:aws:kms:us-east-1:123456:key/abc-123-def-456    │  │
│  │                                                           │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │  KEY MATERIAL (the actual cryptographic bits)        │  │  │
│  │  │  = the secret sauce that encrypts/decrypts          │  │  │
│  │  │                                                     │  │  │
│  │  │  Origin:                                            │  │  │
│  │  │  ├── AWS_KMS    → AWS generated it (default)        │  │  │
│  │  │  ├── EXTERNAL   → YOU imported it                   │  │  │
│  │  │  └── AWS_CLOUDHSM → your CloudHSM generated it     │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  │                                                           │  │
│  │  + Key policy (who can use/manage)                        │  │
│  │  + Metadata (creation date, state, rotation config)       │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Alias = Pointer (Can Be Moved)

```
  alias/my-app-key ──────► key-id-1 (old key material)
                    │
        (rotation)  │  just move the pointer
                    ▼
  alias/my-app-key ──────► key-id-2 (new key material)

  App always calls: "encrypt with alias/my-app-key"
  App never changes. Only the alias target changes.
```

---

## Imported Key Rotation (Manual — The Alias Swap)

```
  BEFORE:
    alias/prod-key ──► Key A (key-id-1, origin=EXTERNAL, old material)

  STEP 1: Create NEW key (origin=EXTERNAL)
  STEP 2: Import new material into Key B
  STEP 3: Move alias

  AFTER:
    alias/prod-key ──► Key B (key-id-2, origin=EXTERNAL, new material)
    Key A still exists → decrypts old ciphertext (key-id baked into ciphertext)
```

---

## AWS-Generated Auto-Rotation (Same Key ID)

```
  Key abc-123 (origin=AWS_KMS):
    ├── Material v1 (2023) ← old ciphertext uses this
    ├── Material v2 (2024) ← mid ciphertext uses this
    └── Material v3 (2025) ← new encryptions use this

  Same key ID, same alias, same ARN.
  KMS auto-routes decrypt to correct version via ciphertext metadata.
  All versions kept FOREVER (until key deleted).
```

---

## MRK (Multi-Region Key)

```
  us-east-1:  mrk-abc-123  ──► key material X  + key policy A
  eu-west-1:  mrk-abc-123  ──► key material X  + key policy B (INDEPENDENT!)

  Same key ID. Same material. Different policies per region.
  Encrypt in us-east-1, decrypt in eu-west-1 locally.
```

---

## Why "Key Material" Matters on the Exam

The exam uses "key material" to distinguish WHAT gets replicated or rotated:

| Scenario | What moves | What stays |
|---|---|---|
| **Auto-rotation** | New material added inside same key | Key ID, alias, ARN unchanged |
| **Imported key rotation** | New material in a NEW key, alias moves | Old key + old material stay for old ciphertext |
| **MRK replication** | Key material copied to new region | Key policies are INDEPENDENT per region |
| **Secrets Manager replication** | The SECRET VALUE (password, not key material) | Completely different layer |

### The Exam Trap

> "DB credentials available in DR region" — what replicates?

- ❌ MRK (replicates key material — the encryption key)
- ✅ Secrets Manager replication (replicates the secret value — the password)

**MRK replicates the lock. Secrets Manager replicates what's inside the safe.**

---

## Key Takeaways

- **Alias** = just a pointer you can move (enables rotation without app changes)
- **Key material** = the actual crypto bits inside the key
- **Imported** = you brought the material, you own durability, no auto-rotation
- **Auto-rotation** = AWS swaps material inside the SAME key ID (transparent)
- **MRK** = same material replicated, but policies are independent per region
- **Secrets Manager** = replicates the secret value, not key material (different layer)
