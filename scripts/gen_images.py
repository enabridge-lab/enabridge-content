#!/usr/bin/env python3
"""
Generate hero images for briefs via Gemini "Nano Banana Pro"
(model: gemini-3-pro-image-preview, fallback: gemini-2.5-flash-image).

For each news/YY-MM-DD-HHMM-*.md (excluding -index):
  - Parse frontmatter
  - If `image:` is already filled → skip
  - If `image_prompt:` exists → call Gemini, save PNG to news/images/,
    rewrite frontmatter with `image: images/<filename>.png`

Usage:
    python3 scripts/gen_images.py --slug 26-04-19-0700
    python3 scripts/gen_images.py --slug 26-04-19-0700 --aspect-ratio 1:1 --image-size 1K
"""
import argparse
import os
import re
import sys
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    sys.exit("ต้อง: pip install google-genai --break-system-packages")

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # GHA จะ inject env vars ผ่าน workflow อยู่แล้ว — .env ไม่จำเป็น


ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = ROOT / "news"
IMAGES_DIR = NEWS_DIR / "images"

PRIMARY_MODEL = "gemini-3-pro-image-preview"
FALLBACK_MODEL = "gemini-2.5-flash-image"


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(md: str) -> tuple[dict, str, str]:
    """Return (frontmatter_dict, frontmatter_block_raw, body)."""
    m = FRONTMATTER_RE.match(md)
    if not m:
        return {}, "", md
    fm_text = m.group(1)
    fm = {}
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    return fm, m.group(0), md[m.end():]


def upsert_frontmatter_line(fm_block: str, key: str, value: str) -> str:
    """Set frontmatter key=value, either replacing or appending before the closing ---."""
    # [ \t]* keeps the match on one line. \s* previously swallowed the newline
    # after "image:" so the value landed on the next line (invalid YAML).
    pattern = re.compile(rf"^{re.escape(key)}:[ \t]*.*$", re.MULTILINE)
    if pattern.search(fm_block):
        return pattern.sub(f"{key}: {value}", fm_block)
    # Insert before the closing ---
    return fm_block.replace("\n---\n", f"\n{key}: {value}\n---\n", 1)


def generate_image_bytes(client, model: str, prompt: str,
                         aspect_ratio: str, image_size: str) -> bytes:
    image_config_kwargs = {"aspect_ratio": aspect_ratio}
    # gemini-2.5-flash-image generates at fixed resolution per aspect ratio —
    # only Nano Banana Pro accepts image_size.
    if model == PRIMARY_MODEL:
        image_config_kwargs["image_size"] = image_size

    response = client.models.generate_content(
        model=model,
        contents=prompt.strip(),
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(**image_config_kwargs),
        ),
    )

    for part in response.parts:
        inline = getattr(part, "inline_data", None)
        if inline is not None and inline.data:
            return inline.data

    raise RuntimeError(f"{model} returned no image part")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True,
                    help="Timestamp slug YY-MM-DD-HHMM (e.g. 26-04-19-0700)")
    ap.add_argument("--aspect-ratio", default="1:1",
                    choices=["1:1", "3:4", "4:3", "9:16", "16:9"])
    ap.add_argument("--image-size", default="1K",
                    choices=["1K", "2K", "4K"],
                    help="Only Nano Banana Pro honors this; fallback ignores")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    briefs = sorted(
        p for p in NEWS_DIR.glob(f"{args.slug}-*.md")
        if not p.name.endswith("-index.md")
    )
    if not briefs:
        sys.exit(f"[images] ไม่เจอ brief สำหรับ {args.slug}")

    for brief_path in briefs:
        md = brief_path.read_text(encoding="utf-8")
        fm, fm_block, body = parse_frontmatter(md)

        if fm.get("image"):
            print(f"[images] {brief_path.name}: มี image อยู่แล้ว — ข้าม")
            continue

        prompt = fm.get("image_prompt")
        if not prompt:
            print(f"[images] {brief_path.name}: ไม่มี image_prompt — ข้าม")
            continue

        # slug ของ brief: YY-MM-DD-NNN-slug → ใช้ทั้งชื่อเป็น filename ของรูป
        image_filename = f"{brief_path.stem}.png"
        image_path = IMAGES_DIR / image_filename

        if args.dry_run:
            print(f"[images] DRY RUN: would gen {image_filename} "
                  f"({args.aspect_ratio}, {args.image_size}) — {prompt[:80]}...")
            continue

        # Try Nano Banana Pro first; fall back if it errors out.
        data = None
        last_err: Exception | None = None
        for model in (PRIMARY_MODEL, FALLBACK_MODEL):
            print(f"[images] {brief_path.name}: gen → {image_filename} via {model}")
            try:
                data = generate_image_bytes(
                    client, model, prompt, args.aspect_ratio, args.image_size,
                )
                break
            except Exception as e:
                print(f"[images] {model} failed: {e}")
                last_err = e

        if data is None:
            print(f"[images] FAIL {brief_path.name}: {last_err}")
            continue

        image_path.write_bytes(data)
        print(f"[images] wrote {image_path} ({len(data) // 1024} KB)")

        # Update frontmatter
        rel = f"images/{image_filename}"
        new_fm_block = upsert_frontmatter_line(fm_block, "image", rel)
        brief_path.write_text(new_fm_block + body, encoding="utf-8")
        print(f"[images] updated frontmatter: image: {rel}")

    print(f"[images] done for {args.slug}")


if __name__ == "__main__":
    main()
