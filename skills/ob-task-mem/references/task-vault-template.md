# Task-Centric Obsidian Vault Template Reference

Use this reference only when a user's vault does not already have a compatible daily/task/project workflow.

The template pattern is based on the `meta/About this Vault.md` note from a task-centric Obsidian vault and the Reddit workflow it cites. For the original workflow details and download links, see `original-reddit-workflow.md`.

https://www.reddit.com/r/ObsidianMD/comments/16psegl/how_i_manage_tasks/

Sample template vault:

- Repository: https://github.com/axelson/task-centric-obsidian-vault
- Direct zip: https://github.com/axelson/task-centric-obsidian-vault/archive/refs/tags/v1.0.0.zip

## Core idea

The vault is organized around tasks, daily capture, project overview notes, and later cleanup from raw daily notes into task/project notes.

## Common plugins

- Obsidian Tasks: task collection, open/completed task queries.
- Templater: folder templates and automatic note scaffolding.
- Dataview: project status tables and dynamic lines.
- Auto Note Mover: moves templated People and Meetings notes into folders.
- Obsidian Copilot or another AI helper: optional help with Tasks, Templater, Dataview, and note cleanup.

## Common folders

- Daily Notes or `daily/`: fast capture and raw work logs.
- Project Notes or `proj/`: project overview notes.
- People: person notes.
- Meetings: meeting notes.
- Emails: email notes, when used.
- Attachments or `img/`: attachments and pasted images.

## Project linking pattern

Projects usually have both a tag and a dynamic field:

- Tag example: `#ProjectA`
- Dynamic field example: `ProjectA:: Some content about Project A`

Meeting notes and tasks use project tags so project notes can collect related tasks and meetings. Dataview can collect dynamic field lines into project status tables.

## Task note pattern

Prefer plain Obsidian Tasks syntax over custom Dataview task syntax because it is easier to read and write:

```markdown
- [ ] Example task #ProjectA
- [x] Completed task #ProjectA
```

## Manual setup guidance

If the user's vault does not match this structure, do not mutate it automatically. Suggest that the user manually download, recreate, or adapt a task-centric starter vault based on the linked workflow, then rerun the memory-recording task after they have chosen daily note, task note, and project note locations.

If the user asks Codex to set it up, confirm whether they want to:

- download the sample vault zip into a new folder,
- clone the GitHub repository,
- or create the same structure manually inside an existing vault.

Never merge a template into an existing vault without a clear target folder and explicit confirmation.
