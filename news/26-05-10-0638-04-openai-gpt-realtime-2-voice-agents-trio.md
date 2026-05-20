---
date: 2026-05-10
slug: openai-gpt-realtime-2-voice-agents-trio
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  A hero illustration of three glowing audio waveform orbs floating side by side
  over a stylized OpenAI globe at night, each labeled in massive bold condensed
  sans-serif white text overlaid: "REALTIME-2", "TRANSLATE", "WHISPER". Each orb
  pulses a different neon color (electric blue, magenta, green) representing
  reasoning, translation, and transcription respectively. Below the orbs in giant
  numbers: "70 LANGS · $32/1M". Cover-art editorial composition with dramatic
  depth, dark space-black and neon palette with high contrast, magazine cover
  style, 1:1 aspect, no real human faces.
image: images/26-05-10-0638-04-openai-gpt-realtime-2-voice-agents-trio.png
---

# OpenAI ปล่อย GPT-Realtime-2 + Translate + Whisper — voice agent ก้าวจาก demo เป็น production layer ราคา audio token เข้าใกล้ text

## TL;DR
- 7 พ.ค. 2026 OpenAI เปิด **3 audio model ใหม่** ใน Realtime API: **GPT-Realtime-2** (voice + GPT-5 reasoning), **GPT-Realtime-Translate** (live translate 70+ ภาษา input → 13 output), **GPT-Realtime-Whisper** (streaming STT)
- Pricing: GPT-Realtime-2 = **$32/M audio input + $64/M audio output + $0.40/M cached input** (cached เกือบฟรี); Translate = $0.034/นาที; Whisper = $0.017/นาที — ลด floor ของ voice agent ลง 5-10x จาก gpt-4o-realtime
- Sierra report ว่า **voice traffic แซง text** ตั้งแต่ ต.ค. 2025 — และ AWS เพิ่งเปิด AgentCore Payments ให้ agent จ่ายเงินเอง 200ms; ทุก primitive ของ "voice agent ที่ทำธุรกรรมจริง" พร้อมใช้พร้อมกัน Q2 2026
- Pattern: voice ไม่ใช่ "feature เสริม" ของ agent อีกต่อไป — กลายเป็น **default channel** ของ customer-facing agent, B2C support, internal tooling

## เกิดอะไรขึ้น

วันที่ 7 พ.ค. 2026 OpenAI ปล่อย 3 model ใหม่ใน Realtime API ที่เน้น production voice agent — ทุก model เน้น "voice ที่ flow เร็วเหมือนคนคุย ไม่ใช่ voice ที่รอ TTS ตามหลัง LLM"

**GPT-Realtime-2** เป็น voice model ตัวแรกของ OpenAI ที่มี **GPT-5-class reasoning** ใน-stream — agent ฟังคำถามยากตอบ + reasoning เกิดใน real-time ไม่ต้อง pre-compute Pricing: **$32 ต่อ 1M audio input token + $64 ต่อ 1M audio output token + $0.40 ต่อ 1M cached input** ตัวเลข cached input ต่ำมาก (50x ถูกกว่า uncached) บอกว่า OpenAI เชื่อว่า voice agent จะมี system prompt + instruction ซ้ำที่ cache ได้เกือบทั้งหมด

**GPT-Realtime-Translate** ทำ live translation 70+ ภาษา input → 13 ภาษา output ระหว่างที่คนพูด — ค่าตัว $0.034/นาที (~$2/ชั่วโมง); ครั้งแรกที่ translation จาก OpenAI ไม่ต้องผ่าน batch step + จ่ายตามนาทีพูดจริง ไม่ใช่ token

**GPT-Realtime-Whisper** เป็น streaming STT รุ่นใหม่ — $0.017/นาที (~$1/ชั่วโมง); หลายเท่าถูกกว่า Whisper batch ที่อยู่ในตลาด

ของที่สำคัญในการทำ pricing structure แบบนี้: ลดกำแพงให้ voice agent run แบบ always-on / per-call แล้วยังคุ้ม จาก gpt-4o-realtime ($100+/M token ปลายปี 2024) ถึง $32/$64 = ลด ~3x ในปีครึ่ง ขณะที่ reasoning ฉลาดขึ้น

## ทำไมสำคัญ

ปกติ voice agent ที่ deploy production มี 3 อุปสรรค: (1) latency รวมระหว่าง STT → LLM → TTS อยู่ที่ 1-2 วินาที (uncanny valley pause), (2) cost ต่อนาที 10-20¢ (จ่ายไม่ไหวถ้า scale call center จริง), (3) reasoning ที่ในขณะ stream ทำได้ตื้น (LLM รอ STT จบ → reasoning → TTS) GPT-Realtime-2 แก้ทั้ง 3 ในเดียว — full duplex + reasoning ใน-stream + cost ลง 3x

ผลในตลาด: ตัวเลข Sierra ที่ "voice แซง text" ตั้งแต่ ต.ค. 2025 ไม่ใช่ outlier — เป็น signal ของ phase shift Decagon, Cresta, Parloa, Sierra, Hume, Vapi, Bland — ทุก voice agent startup จะ benchmark cost-per-minute ใหม่ภายในสิ้นเดือน บางบริษัทที่ build STT + TTS + LLM stack เอง (เพื่อหนีค่า API) จะถามตัวเองว่า defensibility อยู่ตรงไหนต่อ — เพราะ OpenAI managed stack ถูกกว่าและฉลาดกว่า

อีก signal ที่ underrated: **Translate model ที่จ่ายตามนาที ไม่ใช่ token** เปลี่ยน economics ของ multi-language agent ทั้งหมด สำหรับตลาด SEA (Thai, Bahasa, Tagalog, Vietnamese, Mandarin) ที่ดีลใหม่กับ enterprise BPO/call center — voice agent translation เป็น use case ที่ใหญ่ที่สุดของ region $0.034/นาที = ~$2/ชั่วโมง = ถูกกว่า BPO operator เกือบทุก market ใน SEA โดยไม่ต้อง quality compromise

ส่วน Whisper $0.017/นาที = ~$1/ชั่วโมง — ทำให้ "เก็บ transcript ทุกการประชุม Zoom/Teams" + "ทุกสาย call center" + "ทุก voicemail" เป็น default ไม่ใช่ luxury ตลาด **Granola, Read.ai, Otter.ai, Fireflies.ai** ที่ขาย transcription + summary บน margin ของ Whisper batch ต้อง defend cost pass-through; ทุกบริษัทที่ build pre-Whisper-streaming infrastructure ต้อง re-evaluate

## มุม OpenBridge

Voice เป็น primitive ที่ OpenBridge ยังไม่ได้ position direct — แต่ตอนนี้คือ window ที่ต้องตัดสินใจ ถ้า voice agent กลายเป็น default channel ของ enterprise customer-facing workflow (call center, internal helpdesk, sales call coaching, supply chain check-in) **MCP server ของ OpenBridge ต้อง support "voice-aware payload"** — เช่น context ของ caller history + recent ticket + sentiment หลัง STT สำหรับ agent ใช้ตัดสินใจ; webhook back ที่ trigger TTS prompt + carry context ระหว่าง turn

Insight ตรงสุด: **OpenBridge เก็บ context ที่ frontier voice model ไม่มี** — ลูกค้า, ticket, contract, KYC, billing, inventory ที่ flow ใน enterprise SaaS ของลูกค้า OpenBridge build "voice context layer" ที่ GPT-Realtime-2 (หรือ Claude voice ตัวต่อไป) เรียกผ่าน MCP เพื่อ ground voice agent ใน real customer state จะเป็น differentiator ใหญ่ — voice model ไม่มี business state; ต้องผ่าน connector เสมอ

อีกประเด็น tactical สำหรับ SEA: ราคา $0.034/นาที สำหรับ translate Thai → English (หรือกลับกัน) เปิดตลาด **call center BPO multi-lingual** + **internal cross-border meeting** ที่ enterprise ไทย/SG/VN ลงทุนไม่คุ้มมาก่อน ลูกค้า Thai BPO (Truevue, Sykes, Genesys partners) จะเริ่มเปลี่ยน operator workflow ภายใน Q3 OpenBridge ควรเข้าไป conversation ก่อนคู่แข่งโดย bundle "voice agent integration" + "multi-lingual translate" เป็น offer สำเร็จรูปแทนที่จะรอลูกค้า build เอง

## Sources
- [Advancing voice intelligence with new models in the API — OpenAI](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)
- [OpenAI launches new voice intelligence features in its API — TechCrunch](https://techcrunch.com/2026/05/07/openai-launches-new-voice-intelligence-features-in-its-api/)
- [OpenAI unveils trio of realtime audio models to power next-gen voice agents — Neowin](https://www.neowin.net/news/openai-unveils-trio-of-realtime-audio-models-to-power-next-gen-voice-agents/)
- [OpenAI launches three new GPT-Realtime audio models for speech, translation, and transcription — The Tech Portal](https://thetechportal.com/2026/05/08/openai-launches-three-new-gpt-realtime-audio-models-for-speech-translation-and-transcription/)
- [OpenAI GPT-Realtime-2 Brings GPT-5 Reasoning to Voice Agents — Analytics Drift](https://analyticsdrift.com/openai-gpt-realtime-2-voice-api/)

---

## Audio script
สวัสดีครับ Yoh วันที่ 7 พฤษภา OpenAI ปล่อย 3 model ใหม่ใน Realtime API ที่เปลี่ยนเกม voice agent ทั้งวงการ ตัวแรก GPT-Realtime-2 เป็น voice model ตัวแรกของ OpenAI ที่มี GPT-5 reasoning ใน stream — agent ฟัง + คิด + ตอบ real-time ไม่ต้องรอ ราคา 32 ดอลลาร์ ต่อ 1 ล้าน audio input และ 64 ดอลลาร์ ต่อ output ลดจาก gpt-4o-realtime 3 เท่า ตัวที่สอง GPT-Realtime-Translate ทำ live translate 70 ภาษา input เป็น 13 output ที่ 0.034 ดอลลาร์ ต่อนาที ตัวที่สาม Whisper streaming ที่ 0.017 ดอลลาร์ ต่อนาที — ครึ่งเดียวของ batch ตัวเลข Sierra ที่ voice แซง text ตั้งแต่เดือนตุลา ไม่ใช่ outlier — มันคือ phase shift จริง สำหรับตลาด SEA insight ใหญ่คือ translate ราคา 2 ดอลลาร์ ต่อชั่วโมง ถูกกว่า BPO operator แทบทุก market โดยไม่ compromise quality call center BPO ไทย สิงคโปร์ เวียดนาม จะเริ่มเปลี่ยน operator workflow ใน Q3 สำหรับ OpenBridge insight ตรงสุดคือ voice model ไม่มี business state ของลูกค้า — ต้องผ่าน connector เสมอ ดังนั้น MCP server ของ OpenBridge ที่ "voice-aware" + carry context ระหว่าง turn จะเป็น differentiator ใหญ่ที่ frontier voice model ไม่มีทาง substitute ได้ครับ
