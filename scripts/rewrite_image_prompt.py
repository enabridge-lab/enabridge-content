#!/usr/bin/env python3
"""Rewrite a brief's `image_prompt:` field as a YAML literal-block scalar.

Idempotent: if the field already uses the `|` block form, leave it alone.
Designed to fix briefs where the LLM put the entire prompt on one line and
the prompt contains `word: "..."` substrings that break YAML parsing.

Usage:
    python3 scripts/rewrite_image_prompt.py news/26-05-20-0604-01-foo.md [...]
    python3 scripts/rewrite_image_prompt.py --all-broken
"""

import argparse
import glob
import os
import re
import sys
import textwrap

import yaml

FRONTMATTER_RE = re.compile(r"^(---\n)([\s\S]*?)(\n---\n)")


def fix_one(path: str) -> tuple[bool, str]:
    """Return (changed, reason)."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = FRONTMATTER_RE.match(text)
    if not m:
        return False, "no frontmatter"
    fm = m.group(2)

    # Already parses cleanly? Nothing to do.
    try:
        yaml.safe_load(fm)
        return False, "already valid"
    except yaml.YAMLError:
        pass

    # Find the image_prompt line. We match the line that starts with
    # `image_prompt:` and captures the rest of THAT line as the value.
    ip_match = re.search(r"^image_prompt:[ \t]*(.+)$", fm, re.MULTILINE)
    if not ip_match:
        return False, "no image_prompt field"

    value = ip_match.group(1).strip()
    if not value or value == "|":
        return False, "image_prompt is already a block (or empty)"

    # Wrap to ~80 cols and indent by 2 for the literal-block body.
    wrapped = textwrap.fill(
        value,
        width=80,
        break_long_words=False,
        break_on_hyphens=False,
    )
    indented = "\n".join("  " + line for line in wrapped.splitlines())
    replacement = f"image_prompt: |\n{indented}"

    new_fm = fm[: ip_match.start()] + replacement + fm[ip_match.end():]

    # Verify the rewrite now parses.
    try:
        yaml.safe_load(new_fm)
    except yaml.YAMLError as e:
        return False, f"rewrite still invalid: {e}"

    new_text = m.group(1) + new_fm + m.group(3) + text[m.end():]
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    return True, "fixed"


def find_all_broken() -> list[str]:
    broken = []
    for path in sorted(glob.glob("news/*.md")):
        if path.endswith("-index.md"):
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        m = FRONTMATTER_RE.match(text)
        if not m:
            continue
        try:
            yaml.safe_load(m.group(2))
        except yaml.YAMLError:
            broken.append(path)
    return broken


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--all-broken", action="store_true",
                    help="Find every brief whose frontmatter doesn't parse and fix it")
    args = ap.parse_args()

    if args.all_broken:
        paths = find_all_broken()
        print(f"Found {len(paths)} broken brief(s)")
    else:
        paths = args.files

    if not paths:
        print("Nothing to do", file=sys.stderr)
        return 1

    changed = unchanged = failed = 0
    for path in paths:
        ok, msg = fix_one(path)
        prefix = "fixed " if ok else "skip  "
        print(f"  {prefix} {os.path.basename(path):<70} {msg}")
        if ok:
            changed += 1
        elif msg == "already valid":
            unchanged += 1
        else:
            failed += 1

    print(f"\nDone — changed: {changed}, already-valid: {unchanged}, failed: {failed}")
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
