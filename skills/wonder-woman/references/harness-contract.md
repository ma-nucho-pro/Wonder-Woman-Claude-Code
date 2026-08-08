# Harness Contract

Wonder Woman separates **skill content** from **execution capability**.

## FULL mode

FULL mode is valid only when the host can create real, separate model/subagent calls and return their outputs to the orchestrating agent.

Required capabilities:
- read the skill and role files;
- dispatch at least 16 independent model calls per adjudication round (15 judges + Supreme Judge);
- keep Judges 01-15 blind to each other's verdicts;
- wait for all judge results before adjudication;
- perform web/file/tool verification required by the question;
- dispatch fresh judges on a failed round.

Optional but strongly preferred:
- parallel dispatch for Judges 01-15;
- model selection per role;
- structured output validation;
- source opening/fetching rather than snippets only.

## DEGRADED mode

If the host cannot create independent subagents/model calls, Wonder Woman may still apply its verification rules as sequential self-review, but MUST NOT describe this as a 16-judge tribunal.

If the user explicitly requests FULL mode and the capability is missing, stop and report the missing harness capability.

## Recursion guard

Every dispatched role must receive the role prompt and the instruction that it is a Wonder Woman subagent. A dispatched role MUST NOT invoke Wonder Woman again. Otherwise the tribunal can recursively spawn tribunals.

## Cost and latency

FULL mode is intentionally expensive. One clean round requires at least:
- 1 Knowledge Gate call;
- 1 Resource Scout call;
- 1+ Researcher calls when verification is needed;
- 15 independent judge calls;
- 1 Supreme Judge call.

A failed round repeats research/correction/review with fresh judges. Do not hide this tradeoff from users who ask about runtime/cost.


## Claude Code plugin agents

The FULL distribution registers role definitions under the plugin root `agents/` directory. Claude Code discovers these as isolated subagents. The parent Wonder Woman skill remains the coordinator; subagents return findings only and cannot spawn nested subagents.

When the plugin agents are available, use them instead of simulating their roles inline. When they are not available, mark the run `DEGRADED_MODE`.
