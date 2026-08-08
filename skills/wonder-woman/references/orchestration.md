# Orchestration Protocol

Use host-native actions. Do not invent tool names that the harness does not expose.

## Phase A — Pre-draft

1. Dispatch Knowledge Gate.
2. If `CLARIFICATION_REQUIRED`, ask only the necessary question; do not draft.
3. Dispatch Resource Scout.
4. Apply `../protocols/research-reproducibility.md`: formulate evidence questions, define source classes and filters, identify duplicates/dependencies, and plan complementary/contrary-evidence paths.
5. Dispatch Researcher(s) for the source plan. High-impact or contested claims should use more than one independent research path when practical.
6. Assemble the evidence bundle.

## Phase B — Draft and claims

7. Draft privately.
8. Create the claim ledger.
9. Ensure each major/critical factual claim has evidence references or is explicitly marked unresolved before review.

## Phase C — Independent tribunal

10. Create 15 independent judge tasks, one per file `judges/01-*` through `judges/15-*`.
11. Give each judge only:
   - user request;
   - private draft;
   - claim ledger;
   - evidence bundle relevant to its mission;
   - its own judge prompt.
12. Do not give a judge any other judge's verdict.
13. Run in parallel when the harness supports it.
14. Wait for all 15 verdicts.
15. Validate that every expected judge returned a verdict.
16. Dispatch Judge 16 with all artifacts and all 15 verdicts.

## Phase D — Release decision

17. `PASS`: release the adjudicated draft.
18. `SAFE_ABSTENTION`: release only the limitation/partial answer Judge 16 approved.
19. `CLARIFY`: ask the required clarification.
20. `FAIL`: do not release the draft.

## Phase E — Failure loop

21. Identify targeted missing evidence from the Supreme verdict.
22. Dispatch fresh researcher(s) if needed.
23. Dispatch Corrector.
24. Rebuild the claim ledger.
25. Dispatch fresh Judges 01-15. Do not reuse prior verdicts as authority and do not show them to the fresh judges.
26. Dispatch a fresh Supreme Judge adjudication.
27. Repeat up to the configured maximum.

## Integrity checks before claiming FULL-mode completion

- Exactly 15 independent first-stage judge results exist for the final round.
- Exactly one Supreme Judge adjudicated the final round.
- No first-stage judge saw other judge verdicts.
- No judge recursively launched Wonder Woman.
- Every cited source in the final answer was actually accessed by the research process or the orchestrator.
- Any unresolved material claim is qualified, removed, disputed, or abstained from.
