# Evidence and Source Policy

## Core rule

A citation is useful only if the source was actually accessed and the cited material entails the claim.

## Evidence tiers

### Tier 1 — direct / primary
- direct execution results;
- original user data;
- user-provided source document for claims about that document;
- official database;
- official specification/documentation;
- original research or primary legal text;
- first-party announcement for first-party facts.

### Tier 2 — strong secondary
- systematic reviews;
- reputable independent reporting;
- established technical/reference publications.

### Tier 3 — supporting
- expert commentary;
- community documentation;
- forums or social posts with corroboration.

### Not sufficient by itself
- another agent's assertion;
- model memory;
- confidence score;
- majority vote;
- search-result snippet when the underlying source can be opened;
- unsourced generated summary.

## Freshness

For current facts—news, politics, prices, product availability, laws, API/software versions, office holders, schedules, statistics—use a source current enough for the claim. Record publication/update date when available.

## Conflicts

Do not hide source disagreement. Preserve:
- evidence for;
- evidence against;
- source quality;
- dates/versions;
- what remains unresolved.

## Tool semantics

- Tool failure → `UNVERIFIED`, never automatically `FALSE`.
- Empty search results → “not found in this search,” not “does not exist.”
- Agent report → lead requiring independent inspection.
- Citation → must be opened/inspected when possible before relying on it.
