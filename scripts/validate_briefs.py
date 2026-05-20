#!/usr/bin/env python3
"""Validate that every brief in a daily slug has parseable YAML frontmatter.

The site (enabridge-site) renders briefs by parsing YAML frontmatter with
gray-matter. If the YAML is malformed — typically when image_prompt contains
patterns like `numbers: "ZERO"` on a single unquoted line — gray-matter
throws, the frontmatter dict ends up empty, no image renders, and the raw
YAML leaks into the rendered body as a Setext heading.

This validator catches that before push so it never reaches production.
Run from `write_briefs.sh` or any other entry point.
"""

import argparse
import glob
import os
import sys

import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
NEWS_DIR = os.path.join(REPO_ROOT, "news")


def extract_frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return text[4:end]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True, help="YY-MM-DD-HHMM slug")
    args = ap.parse_args()

    paths = sorted(
        p for p in glob.glob(os.path.join(NEWS_DIR, f"{args.slug}-*.md"))
        if not p.endswith("-index.md")
    )
    if not paths:
        print(f"[validate] no briefs found for {args.slug}", file=sys.stderr)
        return 1

    failures = []
    for path in paths:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        fm = extract_frontmatter(text)
        if fm is None:
            failures.append((path, "no frontmatter delimiters"))
            continue
        try:
            data = yaml.safe_load(fm)
        except yaml.YAMLError as e:
            failures.append((path, f"YAML parse error: {e}"))
            continue
        if not isinstance(data, dict):
            failures.append((path, f"frontmatter is not a mapping (got {type(data).__name__})"))
            continue
        for required in ("date", "slug", "topic", "image_prompt"):
            if required not in data:
                failures.append((path, f"missing required key: {required}"))

    if failures:
        print(f"[validate] {len(failures)} problem(s) in {args.slug}:", file=sys.stderr)
        for path, msg in failures:
            print(f"  - {os.path.basename(path)}: {msg}", file=sys.stderr)
        print(
            "\n[validate] fix: rewrite the offending field as a YAML literal-block scalar:\n"
            "    image_prompt: |\n"
            "      <prompt text on indented lines>\n",
            file=sys.stderr,
        )
        return 1

    print(f"[validate] ok — {len(paths)} brief(s) for {args.slug} parse cleanly")
    return 0


if __name__ == "__main__":
    sys.exit(main())
