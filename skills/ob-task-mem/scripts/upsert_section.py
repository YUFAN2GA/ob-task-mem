#!/usr/bin/env python3
"""Idempotently replace or append a Markdown block in a note."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def marker(slug: str, kind: str) -> str:
    return f"<!-- codex:{slug}:{kind} -->"


def upsert(text: str, slug: str, body: str, heading: str | None) -> str:
    start = marker(slug, "start")
    end = marker(slug, "end")
    block = f"{start}\n{body.rstrip()}\n{end}"

    if start in text and end in text:
        before, rest = text.split(start, 1)
        _, after = rest.split(end, 1)
        return before.rstrip() + "\n\n" + block + after

    if heading and heading in text:
        idx = text.find(heading) + len(heading)
        return text[:idx].rstrip() + "\n\n" + block + "\n" + text[idx:].lstrip("\n")

    return text.rstrip() + "\n\n" + block + "\n"


def heading_level(line: str) -> int:
    match = re.match(r"^(#{1,6})\s+\S", line)
    if not match:
        raise ValueError("heading mode requires body to start with a Markdown heading")
    return len(match.group(1))


def heading_block_range(text: str, heading_line: str) -> tuple[int, int] | None:
    pattern = re.compile(rf"^{re.escape(heading_line.rstrip())}\s*$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return None

    level = heading_level(heading_line)
    next_heading = re.compile(rf"^#{{1,{level}}}\s+\S", re.MULTILINE)
    next_match = next_heading.search(text, match.end())
    return match.start(), next_match.start() if next_match else len(text)


def upsert_heading(text: str, body: str, insert_after: str | None) -> str:
    block = body.strip()
    first_line = block.splitlines()[0]
    heading_level(first_line)

    existing = heading_block_range(text, first_line)
    if existing:
        start, end = existing
        before = text[:start].rstrip()
        after = text[end:].lstrip("\n")
        return before + "\n\n" + block + ("\n\n" + after if after else "\n")

    if insert_after and insert_after in text:
        idx = text.find(insert_after) + len(insert_after)
        return text[:idx].rstrip() + "\n\n" + block + "\n" + text[idx:].lstrip("\n")

    return text.rstrip() + "\n\n" + block + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("note", type=Path)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--body-file", required=True, type=Path)
    parser.add_argument("--heading")
    parser.add_argument("--mode", choices=("marked", "heading"), default="marked")
    args = parser.parse_args()

    original = args.note.read_text(encoding="utf-8") if args.note.exists() else ""
    body = args.body_file.read_text(encoding="utf-8")
    if args.mode == "heading":
        updated = upsert_heading(original, body, args.heading)
    else:
        updated = upsert(original, args.slug, body, args.heading)
    args.note.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
