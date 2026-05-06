#!/usr/bin/env python3
"""
Generate daily podcast audio from brief .md files using Google Cloud
Text-to-Speech (Chirp 3 HD voices).

Usage:
    python scripts/tts.py --slug 26-04-18-0700
    python scripts/tts.py --slug 26-04-18-0700 --voice th-TH-Chirp3-HD-Charon

Reads:  news/YY-MM-DD-HHMM-NNN-*.md (excluding -index.md)
Writes: audio/YY-MM-DD-HHMM.mp3 + audio/YY-MM-DD-HHMM.json (metadata)

Auth: set GOOGLE_APPLICATION_CREDENTIALS to a service-account JSON path.
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    from google.cloud import texttospeech
except ImportError:
    sys.exit("ต้อง: pip install google-cloud-texttospeech --break-system-packages")

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None  # type: ignore[assignment]


ROOT = Path(__file__).resolve().parent.parent
if load_dotenv is not None:
    load_dotenv(ROOT / ".env")


def extract_audio_script(md_text: str) -> str | None:
    """Pull the content under '## Audio script' heading."""
    m = re.search(r"##\s*Audio script\s*\n+(.*?)(?=\n##\s|\Z)", md_text, re.DOTALL)
    if not m:
        return None
    return m.group(1).strip()


def extract_title(md_text: str) -> str:
    """Pull the first H1 as the title."""
    m = re.search(r"^#\s+(.+)$", md_text, re.MULTILINE)
    return m.group(1).strip() if m else "(no title)"


def parse_slug(slug: str) -> tuple[str, str, str]:
    """
    Parse YY-MM-DD-HHMM slug.
    Returns (iso_date, human_intro, human_title_suffix).
    """
    parts = slug.split("-")
    if len(parts) != 4 or len(parts[3]) != 4:
        raise ValueError(f"slug must be YY-MM-DD-HHMM, got: {slug}")
    yy, mm, dd, hhmm = parts
    hh, mi = hhmm[:2], hhmm[2:]
    iso_date = f"20{yy}-{mm}-{dd}T{hh}:{mi}:00+07:00"
    dt = datetime.strptime(f"20{yy}-{mm}-{dd} {hh}:{mi}", "%Y-%m-%d %H:%M")
    human_intro = f"{dt.strftime('%d %B %Y')} เวลา {hh}:{mi}"
    human_title_suffix = f"{yy}-{mm}-{dd} {hh}:{mi}"
    return iso_date, human_intro, human_title_suffix


def build_daily_script(slug: str) -> tuple[str, list[dict], str, str]:
    """Compose the full daily audio script.
    Returns (text, item_meta, iso_date, title_suffix)."""
    news_dir = ROOT / "news"
    briefs = sorted(
        p for p in news_dir.glob(f"{slug}-*.md")
        if not p.name.endswith("-index.md")
    )
    if not briefs:
        sys.exit(f"ไม่เจอ brief สำหรับ {slug} ใน {news_dir}")

    iso_date, intro_label, title_suffix = parse_slug(slug)

    # Thai ordinals — avoid "เรื่องที่ 1." pattern: Google's Thai parser
    # treats digit+period as a decimal number, not a sentence terminator,
    # which fuses the header into the next paragraph and exceeds the
    # Chirp 3 HD per-sentence length limit.
    thai_ordinals = ["แรก", "ที่สอง", "ที่สาม", "ที่สี่", "ที่ห้า",
                     "ที่หก", "ที่เจ็ด", "ที่แปด", "ที่เก้า", "ที่สิบ"]

    parts = [
        f"สวัสดีครับ นี่คือ Enabridge AI Brief รอบ {intro_label} ครับ.",
        f"รอบนี้มี {len(briefs)} เรื่อง เน้น Agentic AI, business use case, และ trend ที่เอามาใช้กับ OpenBridge ได้.",
        "",
    ]
    items = []
    for i, brief_path in enumerate(briefs, 1):
        md = brief_path.read_text(encoding="utf-8")
        script = extract_audio_script(md)
        title = extract_title(md)
        if not script:
            print(f"[warn] {brief_path.name} ไม่มี '## Audio script' — ข้าม")
            continue
        ordinal = thai_ordinals[i - 1] if i <= len(thai_ordinals) else f"ที่ {i}"
        parts.append(f"เรื่อง{ordinal}.")
        # Ensure script terminates with a sentence-ending mark so the next
        # section's header doesn't fuse into the final sentence on TTS.
        if script and script[-1] not in ".!?":
            script = script + "."
        parts.append(script)
        parts.append("")
        items.append({
            "file": brief_path.name,
            "title": title,
            "order": i,
        })

    parts.append("ทั้งหมดนี้คือ brief ของรอบนี้. ขอให้วันนี้เป็นวันที่ดีครับ. แล้วเจอกันรอบหน้า.")
    return "\n".join(parts), items, iso_date, title_suffix


# Google Cloud TTS limit is 5000 bytes per request — stay safely under.
CHUNK_BYTES = 4500


def _split_chunks(text: str, max_bytes: int) -> list[str]:
    """Split UTF-8 text into chunks ≤ max_bytes, preferring newline > space cuts.
    Thai characters are 3 bytes each so character-length is not enough."""
    chunks: list[str] = []
    remaining = text
    while remaining:
        if len(remaining.encode("utf-8")) <= max_bytes:
            chunks.append(remaining)
            break

        # Largest character-prefix whose UTF-8 size fits, via binary search.
        lo, hi = 1, len(remaining)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if len(remaining[:mid].encode("utf-8")) <= max_bytes:
                lo = mid
            else:
                hi = mid - 1
        limit = lo

        cut = remaining.rfind("\n", 0, limit)
        if cut < limit // 2:
            cut = remaining.rfind(" ", 0, limit)
        if cut <= 0:
            cut = limit

        chunks.append(remaining[:cut])
        remaining = remaining[cut:].lstrip()
    return chunks


def generate_audio(text: str, out_path: Path, voice_name: str,
                   speaking_rate: float, sample_rate: int) -> None:
    client = texttospeech.TextToSpeechClient()

    voice = texttospeech.VoiceSelectionParams(
        language_code="th-TH",
        name=voice_name,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=speaking_rate,
        sample_rate_hertz=sample_rate,
    )

    chunks = _split_chunks(text, CHUNK_BYTES)
    print(f"[tts] {len(chunks)} chunk(s), voice={voice_name}, rate={speaking_rate}x, {sample_rate}Hz")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("wb") as f:
        for i, chunk in enumerate(chunks, 1):
            print(f"[tts] chunk {i}/{len(chunks)} ({len(chunk.encode('utf-8'))} bytes)")
            response = client.synthesize_speech(
                input=texttospeech.SynthesisInput(text=chunk),
                voice=voice,
                audio_config=audio_config,
            )
            f.write(response.audio_content)
    print(f"[tts] wrote {out_path} ({out_path.stat().st_size // 1024} KB)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True,
                    help="Timestamp slug YY-MM-DD-HHMM (e.g. 26-04-18-0700)")
    ap.add_argument("--voice", default="th-TH-Chirp3-HD-Achernar",
                    help="Google Cloud TTS voice (default: th-TH-Chirp3-HD-Achernar — female Thai)")
    ap.add_argument("--speaking-rate", type=float, default=1.3,
                    help="Speech rate 0.25–2.0 (default: 1.3 ≈ 30%% faster)")
    ap.add_argument("--sample-rate", type=int, default=24000,
                    help="Output sample rate Hz (default: 24000)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Build + save script only, skip API call")
    args = ap.parse_args()

    script, items, iso_date, title_suffix = build_daily_script(args.slug)
    audio_dir = ROOT / "audio"
    audio_dir.mkdir(exist_ok=True)

    # Always save the script text for debugging
    script_path = audio_dir / f"{args.slug}.txt"
    script_path.write_text(script, encoding="utf-8")
    print(f"[tts] script → {script_path} ({len(script)} chars)")

    out_mp3 = audio_dir / f"{args.slug}.mp3"
    if not args.dry_run:
        generate_audio(script, out_mp3, args.voice, args.speaking_rate, args.sample_rate)

    # Metadata for RSS feed. Field name `speed` retained for backwards compat
    # with audio/index.json entries from the OpenAI era — same semantic.
    meta = {
        "date": args.slug,
        "iso_date": iso_date,
        "title": f"Daily AI Brief — {title_suffix}",
        "items": items,
        "script_char_count": len(script),
        "audio_file": out_mp3.name,
        "voice": args.voice,
        "model": "google-cloud-tts-chirp3-hd",
        "speed": args.speaking_rate,
    }
    meta_path = audio_dir / f"{args.slug}.json"
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[tts] meta → {meta_path}")


if __name__ == "__main__":
    main()
