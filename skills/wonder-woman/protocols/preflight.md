# Preflight Protocol

Run before drafting.

## 1. Request integrity

Record:
- exact task;
- requested output/language;
- constraints explicitly supplied by the user;
- what must not be changed or reinterpreted.

Do not silently repair the request. If an ambiguity changes the answer materially, mark `CLARIFICATION_REQUIRED`.

## 2. Knowledge exam

Classify the task:
- domains involved;
- facts required;
- time-sensitive facts;
- private/file-grounded facts;
- calculations required;
- technical/runtime claims;
- claims likely to require primary evidence.

Return one of:
- `READY_WITH_EVIDENCE`
- `RESEARCH_REQUIRED`
- `CLARIFICATION_REQUIRED`
- `INSUFFICIENT_ACCESS`

Model recollection is allowed only as a lead for research, not as decisive evidence for a material public fact that can be checked.

## 3. Premise scan

Flag:
- potentially false premises;
- hidden assumptions;
- ambiguous names/terms;
- missing dates/versions/locations;
- claims supplied by the user that are being used as task assumptions rather than independently verified facts.

Never treat “the user said it” as independent proof. You may use user-provided facts as explicit assumptions: “Using the value you provided…”

## 4. Resource Scout

Before the draft, identify the strongest available evidence source for each claim class.

Priority examples:
1. direct execution / original data / primary document / official database;
2. official documentation / original research / authoritative first-party source;
3. high-quality independent secondary source;
4. supporting community material;
5. model memory only — discovery lead, not primary proof.
