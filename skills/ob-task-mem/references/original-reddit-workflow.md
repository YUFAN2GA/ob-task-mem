# Original Reddit Task Workflow Reference

Use this reference when a user's vault is not already organized for daily capture, project notes, task notes, Tasks queries, and Dataview status lines, or when the user asks where the workflow came from.

## Sources

- Original workflow post: https://www.reddit.com/r/ObsidianMD/comments/16psegl/how_i_manage_tasks/
- Template vault announcement: https://www.reddit.com/r/ObsidianMD/comments/16wczsh/a_taskcentric_obsidian_vault_template/
- Sample template vault repository: https://github.com/axelson/task-centric-obsidian-vault
- Direct template zip: https://github.com/axelson/task-centric-obsidian-vault/archive/refs/tags/v1.0.0.zip

## What the workflow contains

The original post describes Obsidian as a task and project visibility system. Its key pieces are:

- Daily Note: high-priority tasks, previous/next day links, new tasks, scratch notes, meetings attended, and completed tasks.
- Meeting Note: attendees, conversation notes, project tags/links, inline project status fields, and action items.
- Task Note: a central clearinghouse that groups pending tasks by project tag and catches unprojected tasks.
- Project Notes: open tasks, documentation links, meeting history, status notes from inline fields, and completed tasks.
- People Notes: useful for recurring one-on-ones and person-specific follow-up tags.

The important implementation pattern is that tasks and notes are linked by intentional project tags, while project status snippets can be surfaced with Dataview-style inline fields such as:

```markdown
ProjectA:: Important content to remember goes here
```

## How to use this reference

If the user's vault already has its own structure, preserve it.

If the user's vault does not match this workflow, offer three options:

- Use a minimal fallback: write one dated note and one task summary note in locations chosen by the user.
- Manually create or adapt the task-centric structure by following the original Reddit post.
- Download or clone the sample template vault, then record Codex memory into that new vault once the user confirms its location.

Do not automatically download, clone, or merge the template into an existing vault. Ask first, because this can create folders, plugin settings, and templates that may conflict with the user's current vault.

