# Claim Ledger

Before dispatching judges, decompose the private draft into material claims.

Use one row per claim:

```yaml
claim_id: C-001
claim: "Exact normalized claim"
importance: critical | major | minor
type: factual | numerical | technical | causal | quote | current | file-grounded | inference
status: proposed
evidence_refs: []
requires_freshness_check: true|false
user_supplied_assumption: true|false
```

## Claim status vocabulary

- `VERIFIED` — direct/strong evidence entails the claim.
- `SUPPORTED` — adequate evidence supports it, with non-critical limitations.
- `INFERENCE` — conclusion reasonably follows from verified premises but is not directly established.
- `DISPUTED` — credible evidence conflicts.
- `UNVERIFIED` — insufficient evidence.
- `FALSE` — evidence contradicts the claim.
- `UNKNOWN` — available access cannot establish it.

Only `VERIFIED` or `SUPPORTED` may appear as ordinary factual prose. Others must be qualified, corrected, removed, or surfaced explicitly.
