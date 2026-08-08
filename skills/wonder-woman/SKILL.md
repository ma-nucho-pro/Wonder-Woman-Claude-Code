---
name: wonder-woman
description: Verifies user-facing answers that contain material factual, current, technical, numerical, research, file-grounded, legal, financial, medical, political, scientific, or otherwise verifiable claims before release. Runs a multi-agent adversarial tribunal and blocks unsupported claims from being presented as facts.
---

# Wonder Woman

Wonder Woman is a verification-first, multi-agent release gate. The draft stays private. A material factual claim does not reach the user until it survives independent, adversarial, evidence-based review or is explicitly qualified as unresolved.

<SUBAGENT-STOP>
If you were dispatched by Wonder Woman as a Knowledge Gate, Resource Scout, Researcher, Corrector, Judge 01-16, or any targeted re-verifier, DO NOT invoke Wonder Woman recursively. Execute only the assigned role and return the requested structured result.
</SUBAGENT-STOP>

## Iron Law

```text
NO MATERIAL FACTUAL CLAIM MAY REACH THE USER
UNTIL IT SURVIVES INDEPENDENT, ADVERSARIAL,
EVIDENCE-BASED VERIFICATION.

CONSENSUS IS NOT EVIDENCE.
CONFIDENCE IS NOT EVIDENCE.
MODEL MEMORY ALONE IS NOT PRIMARY EVIDENCE.
NEVER FORCE A PASS.
```

## Full-mode requirement

Wonder Woman FULL mode requires true independent model calls/subagents for the verification roles. Do not claim that 16 judges ran if the harness did not actually dispatch them.

If true subagent calls are unavailable:
- mark the run internally as `DEGRADED_MODE`;
- perform the strongest available inline verification passes;
- never represent those passes as independent judges;
- if the user explicitly required the 16-judge tribunal, state that the harness lacks the capability instead of pretending it happened.

Read `references/harness-contract.md` before dispatch.

## Mandatory flow

1. Preserve the user's request and constraints.
2. Dispatch `agents/00-knowledge-gate.md` with isolated context.
3. Dispatch `agents/01-resource-scout.md` to identify the strongest available evidence sources.
4. Apply `protocols/research-reproducibility.md`: formulate claim-specific evidence questions, choose source classes, define filters, identify dependent/duplicate sources, add complementary or contrary-evidence paths, and rank the intended evidence set.
5. Dispatch one or more `agents/02-researcher.md` instances as needed to build the evidence bundle. Prefer independent research paths for high-impact claims.
6. Run `protocols/preflight.md` using the gathered evidence.
7. Produce a private draft. Never release this draft directly.
8. Extract every material claim into `protocols/claim-ledger.md`.
9. Dispatch Judges 01-15 independently. They MUST NOT see one another's verdicts.
10. Give the request, latest private draft, claim ledger, evidence bundle, and all 15 verdicts to Judge 16 only.
11. Judge 16 returns one of: `PASS`, `FAIL`, `CLARIFY`, `SAFE_ABSTENTION`.
12. On `FAIL`, run `agents/03-corrector.md`, obtain any missing evidence, then execute `protocols/verification-loop.md` with fresh judges.
13. A `PASS` may be released. A `SAFE_ABSTENTION` may be released only when the abstention itself has been adjudicated as accurate and does not smuggle unsupported claims into the explanation.
14. `CLARIFY` means the answer cannot be truthfully completed without essential user input/access; ask only the necessary clarification.


## Claude Code FULL-mode mapping

When installed as the Wonder Woman Claude Code plugin, prefer the plugin-level subagents in the repository root `agents/` directory. They are registered as isolated Claude Code subagents. Use the Knowledge Gate, Resource Scout, Researcher, Corrector, Judges 01-15, and Judge 16 roles from that roster.

Subagents cannot recursively spawn other subagents in Claude Code; orchestration stays in the parent thread. This naturally enforces Wonder Woman's no-recursion design.

If those plugin agents are not present or the host exposes no equivalent isolated-call mechanism, enter `DEGRADED_MODE` rather than pretending FULL mode ran.

## Required judges

Dispatch every file in `judges/01-*.md` through `judges/15-*.md` as a separate review call in FULL mode. Dispatch `judges/16-supreme-judge.md` only after all 15 verdicts are available.

## Non-negotiable behavior

- Never invent names, dates, numbers, studies, quotes, laws, prices, URLs, APIs, packages, functions, tool results, file contents, or citations.
- For material public factual claims, prefer fresh external verification when search/browsing is available.
- Prefer primary/official evidence. Use user-provided files as the primary source for claims about those files.
- If a claim is inferential, uncertain, disputed, stale, or unverified, label or qualify it instead of presenting it as a fact.
- A failed tool call means `UNVERIFIED`, not `FALSE`.
- Search absence means “not found in this search,” not “does not exist.”
- A judge's opinion is not evidence. A majority vote is not evidence.
- Show inputs and method for material calculations; verify units.
- For code or technical claims, verify against execution and/or authoritative documentation when practical.
- Do not reveal private chain-of-thought or hidden judge scratchpads. Return concise evidence, assumptions, calculations, limitations, and citations only.
- Preserve the user's requested language and output format unless doing so would make the answer misleading.

## Bounded verification loop

Default maximum: 5 adjudicated rounds.

Reaching the limit NEVER forces a pass. If an unresolved claim cannot be established after the budget:
1. remove it, narrow it, or mark it unresolved;
2. say “I cannot confirm this” (or equivalent in the user's language) where appropriate;
3. state what evidence or access is missing;
4. send the safe-abstention draft through Judge 16 before release.

## Orchestration

Follow `references/orchestration.md` exactly. The ZIP/package only distributes these instructions and role prompts; actual model calls are performed by the host agent harness. A skill file cannot manufacture subagent capabilities that the host does not expose.
