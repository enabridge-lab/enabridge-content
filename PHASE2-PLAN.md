# Phase 2 Plan — Audio + Podcast + Email/Line Delivery

> ⚠️ **HISTORICAL — kept for context.** Phase 2 ตัดสินใจ + ขึ้นแล้ว, Phase 3 (review-before-publish) ก็ขึ้นแล้ว
> ตั้งแต่ **2026-05-05 stack ถูก migrate**: OpenAI DALL-E 3 → Gemini Nano Banana Pro (image gen),
> OpenAI gpt-4o-mini-tts → Google Cloud TTS Chirp 3 HD (TTS).
> ดู `PHASE3-SETUP.md` สำหรับ setup ปัจจุบัน, `RUNBOOK.md` สำหรับ ops
> ตารางตัวเลือก TTS ด้านล่างไม่ใช่สิ่งที่ใช้จริงแล้ว — เก็บไว้เพื่อแสดง trade-off ตอน planning

> สถานะเดิม (เม.ย. 2026): Phase 1 เสร็จ — มี brief .md รายวัน + scheduled task รัน 07:00 แล้ว
> Phase 2 = เพิ่ม audio + delivery channels

## สิ่งที่ต้องตัดสินใจก่อนเริ่ม

### 1. TTS engine (text-to-speech)

| Option | เสียง | ราคา | เซต up | หมายเหตุ |
|---|---|---|---|---|
| **OpenAI TTS** | ดีมาก ไทยได้ | ~$0.015/1K chars (~$0.05/brief) | ง่ายสุด, 1 API key | แนะนำเริ่มที่นี่ |
| **ElevenLabs** | ดีที่สุด, clone เสียง Yoh ได้ | $22/เดือน starter | กลาง | ถ้าอยากได้ "เสียง Yoh" เล่า |
| **Google Cloud TTS** | โอเค ไทยใช้ได้ | ~$0.016/1K chars | ต้อง GCP project | ถูกพอ ๆ กัน, ยุ่งกว่า |

**แนะนำ:** OpenAI TTS ก่อน → ถ้าชอบเสียงค่อยคิด upgrade เป็น ElevenLabs + voice clone

### 2. Podcast feed hosting

ต้อง host 2 อย่าง: **RSS XML** + **MP3 files**

| Option | ข้อดี | ข้อเสีย |
|---|---|---|
| **ใช้ enabridge-site (แนะนำ)** | มี domain + Vercel อยู่แล้ว, free | ต้องเขียน route /research/feed.xml ใน Next.js |
| **GitHub Pages + repo public** | ฟรี, เร็ว | repo ต้อง public (brief คุณอาจไม่อยาก) |
| **Anchor / Spotify for Podcasters** | interface พร้อม | lock-in, ต้อง manual upload |
| **Cloudflare R2 + worker** | ถูกมาก, private-ish | setup เยอะ |

**แนะนำ:** ทำเป็น route ใน `enabridge-site` — `enabridge-site/src/app/research/feed.xml/route.ts` อ่าน MP3 จาก `enabridge-site/public/research/audio/` แล้ว generate RSS dynamic

### 3. ความลับของ feed

Podcast feed ถ้าใส่ URL สาธารณะ คนอื่นเจอ feed ก็ subscribe ได้
- ถ้าต้องการ private: ใส่ random token ใน URL (e.g. `/research/feed.xml?k=abc123xyz`) + check ใน server
- หรือ password-protect ระดับ route
- Apple Podcasts รองรับ feed URL มี query param ok

### 4. Email digest

มี Gmail MCP connected อยู่แล้ว ทำได้ 2 แบบ:
- **Draft-only** — scheduled task สร้าง draft ใน Gmail ให้ Yoh เช็คแล้วกด send เอง (ปลอดภัยกว่า)
- **Auto-send** — ส่งไปเอง (ต้องตั้ง from → to ตัวเอง)

**แนะนำ:** draft-only ช่วงแรก จน trust output

### 5. Line/Telegram

- **Line OA** — ต้องสมัคร Line Official Account + Messaging API, ตั้ง webhook — setup ประมาณ 30 นาที
- **Telegram bot** — เร็วกว่าเยอะ, แค่ `/newbot` ใน BotFather, ได้ token เลย — setup ~10 นาที

**แนะนำ:** Telegram ก่อนเพราะง่ายกว่า ลองใช้งาน 1–2 สัปดาห์ ค่อยเคลื่อนไป Line ถ้าชอบ

## สิ่งที่ผมต้องการจาก Yoh เพื่อทำ Phase 2

- [ ] **TTS API key** — OpenAI API key (ถ้ามีแล้ว) หรือตัดสินใจว่าใช้เจ้าไหน
- [ ] **Domain สำหรับ podcast feed** — confirm ว่าใช้ enabridge-site (สมมุติ https://enabridge.ai หรือ domain จริง)
- [ ] **Telegram bot** — สร้าง bot ผ่าน @BotFather, copy token มาให้ (หรือผม guide ที่นั่น)
- [ ] **ตัดสินใจ private/public** สำหรับ podcast feed

## ถ้าอยากย้ายไป GitHub Actions ทีหลัง

Option "รัน cloud จริง" ที่คุยไว้ตอนต้น — ย้ายได้ถ้าเปลี่ยนใจ:
1. สร้าง repo `enabridge-research` บน GitHub
2. GitHub Action workflow (`.github/workflows/daily.yml`) ตั้ง cron
3. Action call Claude API ด้วย prompt เดียวกัน
4. Commit briefs กลับ repo + trigger rebuild ของ enabridge-site (ถ้า feed อยู่ที่นั่น)

ข้อดี: ไม่ต้องเปิด Cowork ค้างไว้
ข้อเสีย: ต้องจัดการ API key, secrets, ค่าใช้จ่าย ~$3–15/เดือน
