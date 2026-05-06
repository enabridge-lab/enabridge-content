# Runbook — Phase 2 first-time setup

> ทำตาม 4 ขั้น ~10 นาที จะ end-to-end pipeline ทำงาน: brief → audio → podcast feed → Telegram

## Cloud mode (GitHub Actions) — default

**Image gen** ทำใน Claude Code routine ก่อน push (Higgsfield MCP, ดู `prompts/daily-research.md` step 5)
**TTS / index / PR / Telegram** ทำต่อโดย GHA — `.github/workflows/daily-branch-build.yml` trigger auto เมื่อ push `daily/*` branch

**Setup ครั้งเดียว (ที่ repo settings → Secrets and variables → Actions):**
- `GCP_TTS_SA_JSON` — base64 ของ service-account JSON (role: `Cloud Text-to-Speech User`)
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `GEMINI_API_KEY` — **fallback only** ถ้า Higgsfield ใช้ไม่ได้ + ต้องรัน `scripts/gen_images.py` มือ (CI ไม่ได้ใช้แล้ว)

**Backfill วันที่พลาด:** GitHub → Actions tab → "daily-branch-build" → Run workflow on existing `daily/*` branch

## 0. Prerequisite (local mode เท่านั้น)

Credentials อยู่ใน `.env`:

```
GEMINI_API_KEY=AIza...
GOOGLE_APPLICATION_CREDENTIALS=/absolute/path/to/gcp-tts-sa.json
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
```

ติดตั้ง Python deps:

```bash
cd ~/ws/company/enabridge-research
pip3 install google-genai google-cloud-texttospeech python-dotenv requests 'httpx[socks]' --break-system-packages
```

## 1. เชื่อม Telegram bot

```bash
# 1a. เปิด Telegram, search bot ของคุณ (username ที่ @BotFather ให้), กด Start หรือพิมพ์ /start
# 1b. รัน:
python3 scripts/telegram_setup.py
```

Script จะแสดง chat_id ที่เจอ, ถามว่า update .env ให้เลยไหม → ตอบ `y`

## 2. ทดสอบ TTS + Telegram ด้วย brief ของเมื่อวาน

```bash
bash scripts/run_daily.sh 26-04-18
```

ถ้าทุกอย่างผ่าน:
- `audio/26-04-18.mp3` จะเกิด (~3 MB)
- Copy ไปที่ `enabridge-site/public/research/audio/`
- Telegram message + voice file จะเด้งเข้ามือถือคุณ

ถ้าพังที่ TTS → ดู `audio/26-04-18.txt` ก่อน (script ยังอยู่), ตรวจ `GOOGLE_APPLICATION_CREDENTIALS` ชี้ไปที่ SA JSON ที่ valid + role `Cloud Text-to-Speech User`
ถ้าพังที่ image gen (Higgsfield MCP) → check `mcp__...__balance` ดู credits, หรือ fallback มือ `python3 scripts/gen_images.py --slug ${SLUG}` (ใช้ `GEMINI_API_KEY`)
ถ้าพังที่ Telegram → ตรวจ TELEGRAM_CHAT_ID ใน .env

## 3. Deploy enabridge-site ให้ feed ใช้งานได้

```bash
cd ~/ws/company/enabridge-site
npm run build   # ตรวจว่า route ใหม่ build ผ่าน
# ถ้า build ผ่าน: deploy ตามปกติ (Vercel auto จาก git push, หรือ vercel --prod)
```

เสร็จแล้ว test:
- https://enabridge.ai/research — landing page พร้อม audio player
- https://enabridge.ai/research/feed.xml — RSS XML

## 4. Subscribe podcast

- **Apple Podcasts**: Library → Follow Show by URL → paste `https://enabridge.ai/research/feed.xml`
- **Spotify**: ต้อง submit feed ผ่าน [Spotify for Podcasters](https://podcasters.spotify.com/) (ครั้งเดียว, รอ review ~1-2 วัน)
- **Overcast / Pocket Casts / ฯลฯ**: กด "Add by URL" แล้ววาง feed URL

## 5. Pre-approve tools ใน scheduled task

เปิด Cowork → Sidebar "Scheduled" → task `enabridge-daily-research` → กด "Run now"

ครั้งแรกจะ prompt ขอ permission (Bash, WebSearch, ฯลฯ) — approve ให้หมด เพื่อ run ต่อ ๆ ไปไม่ติดขัด

## Troubleshooting

| ปัญหา | ที่ดู |
|---|---|
| MP3 เป็น 0 ไบต์ | SA JSON ไม่ valid / TTS API ยังไม่ enabled / role ขาด — ดู error ใน terminal |
| Higgsfield MCP fail / out of credits | check `mcp__...__balance`; top up ที่ Higgsfield; หรือ fallback มือ: `python3 scripts/gen_images.py --slug ${SLUG}` (ใช้ Gemini) แล้ว commit รูป + frontmatter |
| Image gen 403 / quota (Gemini fallback) | API key ใช้หมด quota → check Google AI Studio billing; หรือ fallback ไป `gemini-2.5-flash-image` ใน script |
| Telegram ไม่ส่ง | `python3 scripts/telegram_setup.py` อีกครั้ง, ตรวจว่า chat ยังเปิดอยู่ |
| Feed ว่าง | MP3 ยังไม่ถูก copy ไป `enabridge-site/public/research/audio/` — ตรวจ path ใน `run_daily.sh` |
| Feed โหลดไม่ได้ | Deploy enabridge-site ยัง? ตรวจ vercel log |
| Scheduled task ไม่รัน | Cowork ต้องเปิดตอน 07:00 — ถ้าไม่สะดวก ย้ายไป GitHub Actions (ดู PHASE2-PLAN.md) |

## หลัง setup เสร็จ — rotate credentials

⚠️ ถ้า key ถูก paste ใน chat — rotate ทันที:
1. Gemini: [aistudio.google.com/apikey](https://aistudio.google.com/apikey) → delete key เดิม + create ใหม่ → update `.env` + GitHub secret `GEMINI_API_KEY`
2. GCP TTS: [console.cloud.google.com/iam-admin/serviceaccounts](https://console.cloud.google.com/iam-admin/serviceaccounts) → service account → Keys → revoke old + create new JSON → update `.env` (path) + GitHub secret `GCP_TTS_SA_JSON` (base64)
3. Telegram: คุย `@BotFather` → `/mybots` → เลือก bot → "API Token" → "Revoke current token" → update `.env`
