---
name: ob-task-mem
description: Use when recording AI agent project work into an Obsidian vault, daily note, task note, project note, convention README, vault template, task memory, work log, branches tried, raw thread notes, or concise completed-task narrative.
---

# Obsidian Task Memory

## Purpose

Record AI agent work in two complementary Obsidian views:

- **Daily thread view:** a faithful work log with raw material, attempts, decisions, branches, commands, files, blockers, and links.
- **Task thread view:** a concise, complete story of the task outcome with noise removed, useful for future readers.

Always preserve the vault's local convention. Read the convention source first when it exists, for example `README.md`, `meta/About this Vault.md`, or a user-named convention document.

## Note Style

Make the note look like the user's existing daily notes:

- Use the related task note title as the largest heading for the daily entry, such as `# howto-agent-task-memory`.
- Put the process material directly under that title as normal content with natural subheadings only when they help.
- Do not add visible headings named `raw`, `raw material`, `daily thread view`, or similar mechanical labels.
- Do not add visible agent marker comments or bracket-like sentinels to human-facing notes.
- Use wikilinks where the vault convention expects them, but prefer readable headings over a heading that is only a bracketed link.

## First Moves

1. Find the vault:
   - Prefer an explicit path from the user.
   - Then check `OBSIDIAN_VAULT`, `OBSIDIAN_VAULT_PATH`, repo docs, shell history hints, and common locations under `~/Documents`, `~/Library/Mobile Documents`, and `~/Obsidian`.
   - Confirm candidates by finding `.obsidian/`.
2. Discover the vault convention before editing:
   - Prefer a convention source such as `README.md`, `Readme.md`, `meta/About this Vault.md`, `About this Vault`, `Wiki`, or another user-named convention document.
   - Search daily-note templates, task-note templates, project indexes, and recent completed task notes.
   - Read only enough examples to copy naming, headings, task syntax, frontmatter, tags, links, dataview fields, and status conventions.
   - If no convention is discoverable, ask the user for the vault path or one example daily note and one task note.
3. Find related Obsidian projects:
   - Search project notes by agent workspace directory name, repo name, branch names, task keywords, user-provided title, and linked issue/PR URLs.
   - Prefer exact wikilinks/backlinks over fuzzy matches.
   - If multiple plausible projects exist, update the daily note with all candidates but only attach a task note to the best match when evidence is strong.

## Evidence To Gather From The Agent Session

Before writing, summarize from the current agent session or project:

- User goal and final outcome.
- Files created/edited, important commands, test/build results, running servers, generated artifacts.
- Branches, worktrees, commits, PRs, issue links, and external URLs.
- Things tried and rejected, including errors and why the final approach changed.
- Remaining follow-ups, blockers, or verification gaps.

Use `git status`, `git branch --show-current`, `git log -n 5 --oneline`, targeted `rg`, and relevant shell output. Do not include secrets, tokens, private keys, or large pasted logs.

## Writing Model

### Daily Capture + Howto Task Pattern

When the convention source says daily notes are raw logs and task/practice notes are organized summaries, use these rules unless local examples disagree:

- `daily/` is the fast daily log. It keeps raw records and should not be deleted after task notes are cleaned up.
- For active work, create or reuse a `howto...` task/practice note and use its readable title as a level-1 heading in the daily note, then put session details under it.
- The task/practice note is where the daily material is later organized into a cleaner summary.
- `proj/` contains project overview notes. Related notes can be connected by tags and dynamic lines beginning with fields like `proj_xx::`.
- `md/` is for copied/reference material about "what is"; task work and personal practice should not be hidden there by default.
- `people/`, `meeting/`, and `daily/` keep their existing directory roles.
- Large binary files over about 30 MB belong in `nimg/`; notes should record paths or links rather than embedding bulky files.

### If the vault is not organized this way

Do not reorganize an existing vault or invent the daily/howto/proj structure without user consent.

If the vault has no task-centric structure, no daily notes, no project notes, or no Tasks/Dataview conventions:

- Tell the user the vault does not appear to match the workflow this skill expects.
- Offer to record into a simple dated note as a minimal fallback, or ask where daily and task notes should go.
- Offer the optional task-vault starter reference in `references/task-vault-template.md` so the user can manually download or recreate the template before using this workflow.
- If the user wants the original workflow, point them to `references/original-reddit-workflow.md`; it includes the Reddit post, sample vault repository, and direct zip download link.
- Do not download, clone, or create a template vault unless the user explicitly asks for that action and confirms the target location.
- Only proceed with the full daily capture + task concise workflow after the user identifies the target note locations or confirms the template-style structure.

### Daily note entry

The daily note is allowed to be messy but should be navigable.

Include, following the local convention:

- Timestamp or session marker when it fits the surrounding daily note.
- A level-1 heading using the related `howto...` task/practice note title when the convention uses the daily-capture/howto-task pattern.
- Agent workspace/project path and related project/task links.
- Process record: commands, branches, files touched, attempts, errors, decisions.
- Final result and verification evidence.
- Links to any task note created or updated.

Keep process details here rather than in the task note. Do not remove the daily record after summarizing it elsewhere.

### Task note entry

The task note should read as a concise project memory.

Include, following the local convention:

- Problem or request.
- Relevant context and related project.
- Links back to the daily note entry that contains raw material.
- What changed.
- Why this approach was chosen.
- Verification performed.
- Current state: completed, partial, blocked, or follow-up needed.

Omit noisy dead ends unless they explain the final design.

## Task Up-Insert Rules

Use "up-insert" to mean idempotent update-or-insert:

- If the daily note section or task note already has this agent session, update that block instead of duplicating it.
- If the task exists in the vault's task syntax, mark it complete only when the actual agent task is complete and verification is recorded.
- Preserve existing frontmatter, backlinks, block IDs, dataview fields, heading levels, and checkbox syntax.
- Insert under the convention's preferred heading. If unclear, create the smallest compatible section with a clear timestamp.
- Never delete prior notes. Move or compact only the block this run owns.

For mechanical section replacement in human-facing notes, use `scripts/upsert_section.py --mode heading` with a natural Markdown heading. Use visible marker mode only for scratch files or when the user explicitly accepts source-level markers.

## Completion Checklist

Before reporting done:

- Daily note updated with process memory and links.
- Related project/task note found or a clear reason recorded if not found.
- Task note updated with concise narrative if the work relates to a task note.
- Obsidian task checkbox/status completed only when warranted.
- Changes reviewed with `git diff --no-index` or equivalent file diff when possible.
