# Verification Loop

The user must never receive a failed factual draft.

## Round

1. Read the Supreme Judge's failed claims and hard blockers.
2. Research or inspect the missing evidence.
3. Dispatch the Corrector with the failed draft + evidence + adjudication.
4. Correct the draft; do not merely soften wording around a false claim.
5. Rebuild the claim ledger if claims changed.
6. Dispatch fresh Judges 01-15. They must not see prior judge verdicts.
7. Dispatch a fresh Judge 16 with the new evidence and final-round verdict set.

## Hard blockers

Any of these forces `FAIL` regardless of score:
- fabricated source/citation/tool result;
- citation does not support a critical/major claim;
- unresolved critical contradiction;
- unsupported major factual claim presented as fact;
- material number not reproducible from stated inputs;
- current claim based only on stale/model-memory evidence when fresh verification is available;
- user/document content attributed to a source where it does not appear;
- claimed FULL mode without the required independent subagent calls.

## Bounded loop

Default: maximum 5 adjudicated rounds.

The limit is not permission to release a bad answer. If the answer cannot pass by the final round:
1. remove or explicitly qualify the unsupported claims;
2. state “I cannot confirm this” (or equivalent in the user's language) for the unresolved part;
3. state what evidence/access is missing;
4. submit this safe-abstention draft to Judge 16 for final adjudication.

A `SAFE_ABSTENTION` may be released only if Judge 16 confirms that the limitation itself is accurate and contains no unsupported material claims.

## Verification score

This is a process-quality metric, **not a probability that the answer is true**.

- Evidence coverage: 25
- Source quality: 20
- Citation entailment: 15
- Freshness: 10
- Internal consistency: 10
- Adversarial survival: 10
- Numerical/technical checks: 10

Default release threshold: 95/100 plus zero hard blockers.
