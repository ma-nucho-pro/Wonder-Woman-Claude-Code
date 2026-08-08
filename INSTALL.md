# Install Wonder Woman for Claude Code

Repository: https://github.com/ma-nucho-pro/Wonder-Woman-Claude-Code

This repository is the **Claude Code FULL plugin**. It defines 20 Claude Code custom agents: 4 workflow agents plus 16 judges.

## Recommended installation

```bash
git clone https://github.com/ma-nucho-pro/Wonder-Woman-Claude-Code.git
cd Wonder-Woman-Claude-Code
claude plugin validate .
claude --plugin-dir .
```

## Download instead of cloning

Download:

https://github.com/ma-nucho-pro/Wonder-Woman-Claude-Code/archive/refs/heads/main.zip

Extract the archive, open a terminal in `Wonder-Woman-Claude-Code-main`, then run:

```bash
claude plugin validate .
claude --plugin-dir .
```

## Packaged release ZIP

If you downloaded `wonder-woman-claude-code-plugin-v0.3.0.zip` from GitHub Releases, you do not need to extract it:

```bash
claude --plugin-dir ./wonder-woman-claude-code-plugin-v0.3.0.zip
```

On Windows:

```powershell
claude --plugin-dir ".\wonder-woman-claude-code-plugin-v0.3.0.zip"
```

Claude Code supports `.zip` archives with `--plugin-dir`.

## Verify

Inside Claude Code:

```text
/context
```

Look under **Custom Agents**. The plugin should expose the Wonder Woman workflow agents and judges.

To manually trigger the main skill:

```text
/wonder-woman:wonder-woman
```

After editing plugin files:

```text
/reload-plugins
```

For problems, inspect `/plugin` → **Errors** or launch with:

```bash
claude --debug --plugin-dir .
```

## Important distinction

This archive is a **Claude Code plugin**, not the portable Skill ZIP intended for claude.ai or ChatGPT Skill upload interfaces.

Portable Skill repository:

https://github.com/ma-nucho-pro/Wonder-Woman
