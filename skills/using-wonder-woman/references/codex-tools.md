# Codex multi-agent note

Wonder Woman FULL mode requires Codex multi-agent support. In environments matching the supplied Superpowers reference, enable:

```toml
[features]
multi_agent = true
```

Then map the abstract actions "dispatch subagent", "wait for subagent", and "close subagent" to the host's native multi-agent actions. If those actions are unavailable in the running Codex environment, use `DEGRADED_MODE` and do not claim that 16 independent judges ran.
