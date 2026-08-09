import json, os, subprocess, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "wonder-woman"

class PackageTests(unittest.TestCase):
    def test_manifest(self):
        m = json.loads((ROOT / "manifest.json").read_text())
        self.assertEqual(m["name"], "wonder-woman")
        self.assertEqual(m["version"], "0.3.0")
        self.assertEqual(m["judge_count"], 16)
        self.assertEqual(m["first_stage_judge_count"], 15)
        self.assertTrue(m["full_mode_requires_independent_model_calls"])

    def test_judges_exactly_16(self):
        judges = sorted((SKILL / "judges").glob("*.md"))
        self.assertEqual(len(judges), 16)
        self.assertEqual(judges[0].name, "01-knowledge-examiner.md")
        self.assertEqual(judges[-1].name, "16-supreme-judge.md")

    def test_required_agents(self):
        names = {p.name for p in (SKILL / "agents").glob("*.md")}
        self.assertEqual(names, {
            "00-knowledge-gate.md", "01-resource-scout.md", "02-researcher.md", "03-corrector.md"
        })

    def test_recursion_guards(self):
        core = (SKILL / "SKILL.md").read_text()
        boot = (ROOT / "skills" / "using-wonder-woman" / "SKILL.md").read_text()
        self.assertIn("SUBAGENT-STOP", core)
        self.assertIn("DO NOT invoke Wonder Woman recursively", core)
        self.assertIn("SUBAGENT-STOP", boot)

    def test_no_false_full_mode_claim(self):
        core = (SKILL / "SKILL.md").read_text()
        self.assertIn("Do not claim that 16 judges ran", core)
        self.assertIn("DEGRADED_MODE", core)

    def test_bounded_loop_and_safe_exit(self):
        core = (SKILL / "SKILL.md").read_text()
        loop = (SKILL / "protocols" / "verification-loop.md").read_text()
        self.assertIn("Default maximum: 5 adjudicated rounds", core)
        self.assertIn("Reaching the limit NEVER forces a pass", core)
        self.assertIn("SAFE_ABSTENTION", loop)

    def test_plugin_jsons(self):
        for p in [ROOT / ".claude-plugin" / "plugin.json", ROOT / ".codex-plugin" / "plugin.json", ROOT / ".cursor-plugin" / "plugin.json"]:
            data = json.loads(p.read_text())
            self.assertEqual(data["name"], "wonder-woman")
            self.assertEqual(data["version"], "0.3.0")

    def test_hook_outputs_valid_json(self):
        hook = ROOT / "hooks" / "session-start"
        cases = [
            ({"CLAUDE_PLUGIN_ROOT": str(ROOT)}, "hookSpecificOutput"),
            ({"CURSOR_PLUGIN_ROOT": str(ROOT)}, "additional_context"),
            ({"COPILOT_CLI": "1"}, "additionalContext"),
        ]
        for extra, key in cases:
            env = os.environ.copy()
            for k in ["CURSOR_PLUGIN_ROOT", "CLAUDE_PLUGIN_ROOT", "COPILOT_CLI"]:
                env.pop(k, None)
            env.update(extra)
            out = subprocess.check_output(["bash", str(hook)], env=env, text=True)
            data = json.loads(out)
            self.assertIn(key, data)

    def test_schema_json_parses(self):
        for p in (SKILL / "schemas").glob("*.json"):
            json.loads(p.read_text())

    def test_all_markdown_fences_balanced(self):
        for p in ROOT.rglob("*.md"):
            self.assertEqual(p.read_text().count("```") % 2, 0, p)

    def test_first_stage_judges_blind(self):
        for p in sorted((SKILL / "judges").glob("*.md"))[:15]:
            t = p.read_text()
            self.assertIn("Do not assume another judge checked anything", t, p.name)

    def test_supreme_is_not_majority_vote(self):
        t = (SKILL / "judges" / "16-supreme-judge.md").read_text()
        self.assertIn("Do not decide by majority vote", t)
        self.assertIn("Never force a PASS", t)

    def test_reproducible_research_protocol(self):
        p = SKILL / "protocols" / "research-reproducibility.md"
        self.assertTrue(p.exists())
        t = p.read_text()
        for phrase in ["Formulate the evidence question", "Select source classes", "Detect duplicates", "Search complementary paths", "Rank and select"]:
            self.assertIn(phrase, t)

    def test_claude_plugin_agents_present(self):
        agents = sorted((ROOT / "agents").glob("*.md"))
        self.assertEqual(len(agents), 20)
        names = []
        for p in agents:
            text = p.read_text()
            self.assertTrue(text.startswith("---\n"), p.name)
            m = __import__('re').search(r"^name:\s*([a-z0-9-]+)$", text, flags=__import__('re').M)
            self.assertIsNotNone(m, p.name)
            names.append(m.group(1))
        self.assertEqual(len(names), len(set(names)))

    def test_logo_and_repository_links(self):
        self.assertTrue((ROOT / "assets" / "wonder-woman-logo.png").exists())
        readme = (ROOT / "README.md").read_text()
        self.assertIn("assets/wonder-woman-logo.png", readme)
        self.assertIn("https://github.com/ma-nucho-pro/Wonder-Woman-Claude-Code", readme)

    def test_license_and_attribution(self):
        self.assertTrue((ROOT / "LICENSE").exists())
        self.assertTrue((ROOT / "NOTICE").exists())
        self.assertTrue((ROOT / "AUTHORS.md").exists())
        license_text = (ROOT / "LICENSE").read_text()
        notice = (ROOT / "NOTICE").read_text()
        plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
        self.assertIn("Apache License", license_text)
        self.assertIn("Version 2.0", license_text)
        self.assertIn("Roberto Manuel Jara Peche / ARKEA AI", notice)
        self.assertEqual(plugin.get("license"), "Apache-2.0")
        self.assertEqual(plugin.get("author", {}).get("name"), "Roberto Manuel Jara Peche / ARKEA AI")


    def test_agent_skill_frontmatter_constraints(self):
        import re
        text = (SKILL / "SKILL.md").read_text()
        fm = re.search(r"^---\n(.*?)\n---", text, flags=re.S)
        self.assertIsNotNone(fm)
        name = re.search(r"^name:\s*(.+)$", fm.group(1), flags=re.M).group(1).strip()
        desc = re.search(r"^description:\s*(.+)$", fm.group(1), flags=re.M).group(1).strip()
        self.assertRegex(name, r"^[a-z0-9-]{1,64}$")
        self.assertGreater(len(desc), 0)
        self.assertLessEqual(len(desc), 1024)
        self.assertNotIn("<", desc)
        self.assertNotIn(">", desc)


if __name__ == "__main__":
    unittest.main()
