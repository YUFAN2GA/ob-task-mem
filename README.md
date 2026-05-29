# Codex Obsidian Task Memory Skill

`ob-task-mem` is a Codex skill for recording Codex project work into an Obsidian vault with two complementary views:

- a daily note entry that preserves process material, attempts, commands, files, and verification;
- a task note entry that keeps the concise task story for future reading.

The skill is designed for task-centric Obsidian vaults with daily notes, task notes, project notes, project tags, and optional Dataview/Tasks queries. It first reads the user's vault convention and avoids forcing a structure onto an unrelated vault.

## Install

Install directly from this repository with Codex's skill installer:

```text
$skill-installer install https://github.com/YUFAN2GA/codex-ob-task-mem/tree/main/skills/ob-task-mem
```

After installation, restart Codex so the skill list is refreshed.

## Use

Ask Codex to record the current project work into Obsidian:

```text
Use ob-task-mem to record today's Codex work into my Obsidian daily note and related task note.
```

If your vault does not already have a compatible structure, the skill will offer a simple fallback or point you to the task-centric vault reference.

## Contents

```text
skills/ob-task-mem/
  SKILL.md
  agents/openai.yaml
  scripts/upsert_section.py
  references/
    original-reddit-workflow.md
    task-vault-template.md
```

## Safety

The skill should not reorganize a vault, download a template, clone a repository, or merge template files into an existing vault unless the user explicitly asks for that action and confirms the target location.

## License

MIT
