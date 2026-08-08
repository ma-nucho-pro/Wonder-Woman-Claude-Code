#!/usr/bin/env python3
from __future__ import annotations
import json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "wonder-woman"
BOOT = ROOT / "skills" / "using-wonder-woman" / "SKILL.md"

checks = []

def check(name, condition, detail=""):
    ok = bool(condition)
    checks.append((name, ok, detail))
    if not ok:
        print(f"FAIL  {name}: {detail}")
    else:
        print(f"PASS  {name}")
    return ok

# Required structure
required = [
    ROOT / "README.md", ROOT / "INSTALL.md", ROOT / "manifest.json",
    SKILL / "SKILL.md", BOOT,
    SKILL / "references" / "orchestration.md",
    SKILL / "references" / "harness-contract.md",
    SKILL / "agents" / "00-knowledge-gate.md",
    SKILL / "agents" / "01-resource-scout.md",
    SKILL / "agents" / "02-researcher.md",
    SKILL / "agents" / "03-corrector.md",
    ROOT / "hooks" / "session-start",
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / ".codex-plugin" / "plugin.json",
    ROOT / ".cursor-plugin" / "plugin.json",
    ROOT / "assets" / "wonder-woman-logo.png",
    SKILL / "protocols" / "research-reproducibility.md",
]
for p in required:
    check(f"exists:{p.relative_to(ROOT)}", p.exists(), str(p))

# JSON files parse
for p in ROOT.rglob("*.json"):
    try:
        json.loads(p.read_text(encoding="utf-8"))
        check(f"json:{p.relative_to(ROOT)}", True)
    except Exception as e:
        check(f"json:{p.relative_to(ROOT)}", False, repr(e))

manifest = json.loads((ROOT / "manifest.json").read_text())
check("manifest-version", manifest.get("version") == "0.3.0", manifest.get("version"))
check("manifest-core-skill", (ROOT / manifest["core_skill"]).exists(), manifest["core_skill"])
check("manifest-bootstrap-skill", (ROOT / manifest["bootstrap_skill"]).exists(), manifest["bootstrap_skill"])

# Judge roster
judges = sorted((SKILL / "judges").glob("*.md"))
check("judge-count-16", len(judges) == 16, str([p.name for p in judges]))
expected = [f"{i:02d}-" for i in range(1,17)]
check("judge-numbering-01-16", all(p.name.startswith(prefix) for p, prefix in zip(judges, expected)), str([p.name for p in judges]))
check("supreme-is-16", judges[-1].name == "16-supreme-judge.md" if judges else False)

# Every markdown file has balanced fenced blocks
for p in ROOT.rglob("*.md"):
    count = p.read_text(encoding="utf-8").count("```")
    check(f"fences:{p.relative_to(ROOT)}", count % 2 == 0, f"count={count}")

# Frontmatter names
for p, expected_name in [(SKILL / "SKILL.md", "wonder-woman"), (BOOT, "using-wonder-woman")]:
    text = p.read_text(encoding="utf-8")
    m = re.search(r"^---\n(.*?)\n---", text, flags=re.S)
    check(f"frontmatter:{p.relative_to(ROOT)}", bool(m), "missing frontmatter")
    if m:
        nm = re.search(r"^name:\s*(.+)$", m.group(1), flags=re.M)
        check(f"frontmatter-name:{expected_name}", bool(nm and nm.group(1).strip() == expected_name), nm.group(1).strip() if nm else "missing")

# Agent Skills frontmatter constraints
core_frontmatter = (SKILL / "SKILL.md").read_text(encoding="utf-8")
fm = re.search(r"^---\n(.*?)\n---", core_frontmatter, flags=re.S)
if fm:
    nm = re.search(r"^name:\s*(.+)$", fm.group(1), flags=re.M)
    desc = re.search(r"^description:\s*(.+)$", fm.group(1), flags=re.M)
    skill_name = nm.group(1).strip() if nm else ""
    skill_desc = desc.group(1).strip() if desc else ""
    check("agent-skill-name-format", bool(re.fullmatch(r"[a-z0-9-]{1,64}", skill_name)), skill_name)
    check("agent-skill-description-length", 0 < len(skill_desc) <= 1024, str(len(skill_desc)))
    check("agent-skill-description-no-xml", "<" not in skill_desc and ">" not in skill_desc, skill_desc)

# Recursion guards
core_text = (SKILL / "SKILL.md").read_text()
boot_text = BOOT.read_text()
check("core-recursion-guard", "SUBAGENT-STOP" in core_text and "DO NOT invoke Wonder Woman recursively" in core_text)
check("bootstrap-recursion-guard", "SUBAGENT-STOP" in boot_text and "Never spawn another Wonder Woman tribunal" in boot_text)
check("full-mode-honesty", "Do not claim that 16 judges ran" in core_text)
check("bounded-loop", "Default maximum: 5 adjudicated rounds" in core_text)

# Internal README/INSTALL links
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for p in [ROOT / "README.md", ROOT / "README.es.md", ROOT / "INSTALL.md"]:
    for target in link_re.findall(p.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target_path = (p.parent / target.split("#",1)[0]).resolve()
        check(f"link:{p.name}->{target}", target_path.exists(), str(target_path))

# Hook emits valid JSON in three shapes
hook = ROOT / "hooks" / "session-start"
def run_hook(env_extra):
    env = os.environ.copy()
    env.update(env_extra)
    for k in ["CURSOR_PLUGIN_ROOT", "CLAUDE_PLUGIN_ROOT", "COPILOT_CLI"]:
        if k not in env_extra:
            env.pop(k, None)
    out = subprocess.check_output(["bash", str(hook)], text=True, env=env)
    return json.loads(out)
try:
    claude = run_hook({"CLAUDE_PLUGIN_ROOT": str(ROOT)})
    check("hook-claude-shape", "hookSpecificOutput" in claude and claude["hookSpecificOutput"].get("hookEventName") == "SessionStart")
except Exception as e:
    check("hook-claude-shape", False, repr(e))
try:
    cursor = run_hook({"CURSOR_PLUGIN_ROOT": str(ROOT)})
    check("hook-cursor-shape", "additional_context" in cursor)
except Exception as e:
    check("hook-cursor-shape", False, repr(e))
try:
    generic = run_hook({"COPILOT_CLI": "1"})
    check("hook-generic-shape", "additionalContext" in generic)
except Exception as e:
    check("hook-generic-shape", False, repr(e))

# Judge prompts are independent and structured
for p in judges[:15]:
    t = p.read_text(encoding="utf-8")
    check(f"judge-contract:{p.name}", "verdict: PASS | FAIL | NOT_APPLICABLE" in t and "critical_findings:" in t)
    check(f"judge-blindness:{p.name}", "Do not assume another judge checked anything" in t)

supreme = (SKILL / "judges" / "16-supreme-judge.md").read_text(encoding="utf-8")
for state in ["PASS", "FAIL", "CLARIFY", "SAFE_ABSTENTION"]:
    check(f"supreme-state:{state}", state in supreme)
check("supreme-no-majority", "Do not decide by majority vote" in supreme)
check("supreme-never-force-pass", "Never force a PASS" in supreme)


# Claude Code plugin-level subagents
plugin_agents = sorted((ROOT / "agents").glob("*.md"))
check("claude-plugin-agent-count-20", len(plugin_agents) == 20, str([p.name for p in plugin_agents]))
seen_agent_names = set()
for p in plugin_agents:
    text = p.read_text(encoding="utf-8")
    m = re.search(r"^---\n(.*?)\n---", text, flags=re.S)
    check(f"plugin-agent-frontmatter:{p.name}", bool(m), "missing frontmatter")
    if m:
        nm = re.search(r"^name:\s*([a-z0-9-]+)$", m.group(1), flags=re.M)
        check(f"plugin-agent-name:{p.name}", bool(nm), "missing/invalid name")
        if nm:
            check(f"plugin-agent-unique:{nm.group(1)}", nm.group(1) not in seen_agent_names, nm.group(1))
            seen_agent_names.add(nm.group(1))

check("logo-present", (ROOT / "assets" / "wonder-woman-logo.png").exists())
check("repository-in-readme", "https://github.com/ma-nucho-pro/Wonder-Woman-Claude-Code" in (ROOT / "README.md").read_text())
check("reproducible-research", "research-reproducibility.md" in (SKILL / "SKILL.md").read_text())

failed = [x for x in checks if not x[1]]
print(f"\n{len(checks)-len(failed)}/{len(checks)} checks passed")
if failed:
    sys.exit(1)
