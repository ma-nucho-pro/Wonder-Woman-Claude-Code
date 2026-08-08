# Platform notes

Wonder Woman skill files intentionally name abstract actions rather than hard-coding one vendor's tool names.

- A host with native skills + subagents can load `skills/wonder-woman/SKILL.md` and dispatch the roles directly.
- A host with skills but no subagents can only run degraded sequential review.
- A host with subagents but no automatic bootstrap must be configured to load `skills/using-wonder-woman/SKILL.md` at session start.
- A plain chat interface with no skill loader and no subagent API cannot execute FULL mode merely by receiving the ZIP.
