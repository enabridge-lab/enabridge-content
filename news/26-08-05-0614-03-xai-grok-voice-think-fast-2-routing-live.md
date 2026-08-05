---
date: 2026-08-05
slug: xai-grok-voice-think-fast-2-routing-live
topic: agentic-ai
reading_time_min: 4
sources: 6
image_prompt: |
  Editorial isometric illustration of a giant switchboard operator console flipping
  a red lever labeled "grok-voice-latest → 2.0" at exactly 00:00 UTC. Above the
  lever three glowing meters read "$0.08/MIN", "82.9% QUALITY INDEX",
  "-60% REASONING TOKENS". To the left, a tall pillar labeled "SIERRA — $200M ARR"
  and a shorter one "DECAGON — $4.5B VAL" are visibly cracking, dollar bills leaking
  out. To the right, headphones with tiny microphones queue at a booth marked
  "24 LANGUAGES · PHONE-LINE NOISE ROBUST". Background: circuit-trace world map,
  arrows pointing from Vegas to Bangkok. Editorial deep purple + neon cyan palette,
  chiaroscuro style, 1:1 aspect, no real human faces, text sharp at 200px thumbnail.
image: images/26-08-05-0614-03-xai-grok-voice-think-fast-2-routing-live.png
---

# xAI Grok Voice Think Fast 2.0 auto-routes วันนี้ 5 ส.ค. — voice agent pricing shock $0.08/min + 60% token cut, Sierra ($200M ARR) กับ Decagon ($4.5B val) เริ่มถูกบีบ

## TL;DR
- **5 ส.ค.** — xAI ประกาศ **grok-voice-latest ทุก request auto-route ไป Grok Voice Think Fast 2.0 วันนี้** (Speech-to-Speech). Migration ไม่ต้องแตะ code ฝั่ง client — API endpoint เดิม
- **Performance เขย่าตลาด voice agent** — 82.9% Artificial Analysis Speech-to-Speech Quality Index, 56.5% τ-voice, **0.70 วินาที time-to-first-audio**, transcription accuracy ดีกว่า dedicated STT model **1.5-2x** ใน clean audio และสูงถึง **10x ใน noisy phone-line** (24 languages). Reasoning token cut **60%** = tool call latency ลง + cost ลง
- **Pricing** = **$0.08/นาที audio** — OpenAI Realtime API เดิม (GPT-5.6 Sol Voice) อยู่ที่ $0.18/นาที; ElevenLabs Conversational $0.10/นาที; Retell AI/Vapi ($0.05-0.20 ขึ้นกับ model) — xAI เข้ามาตัดกลางตลาดที่ **44% cheaper than OpenAI + intelligence tier ใกล้เคียง GPT-5.6 Sol Voice**
- **สิ่งที่จะเกิดใน 30-90 วัน** — Sierra ($200M ARR, $15.8B val พ.ค. 26), Decagon ($4.5B val ม.ค. 26), Cresta, Retell AI, Vapi จะเผชิญ price compression; voice contact-center vendor (Genesys, NICE, Verint, Concentrix, Teleperformance) จะเร่ง commit Grok Voice หรือ counter-launch; **Yellow.ai + BPO roll-up strategy ที่เพิ่ง SPAC $550M ได้ economic boost ทันที**

## เกิดอะไรขึ้น

วันอังคาร 5 สิงหาคม xAI ยืนยันใน release notes: **API endpoint `grok-voice-latest` ทุก request จะถูก auto-route ไป Grok Voice Think Fast 2.0 (Speech-to-Speech)** เริ่มวันนี้. คือ developer ที่ใช้ endpoint นี้อยู่แล้ว — client code ไม่ต้องเปลี่ยน, request จะเข้า model ใหม่โดยอัตโนมัติ. Grok Voice Think Fast 2.0 เอง launch เข้าสถานะ public API ตั้งแต่ปลาย ก.ค. — แต่ default routing เพิ่งเปิดวันนี้เพื่อให้ผู้ใช้ existing มีเวลา test/rollback ประมาณ 5-7 วัน

**Performance ที่ xAI publish** — 82.9% Artificial Analysis Speech-to-Speech Quality Index (สูงกว่า GPT-5.6 Sol Voice ที่ 78.4% ล่าสุด), 56.5% τ-voice score, **time-to-first-audio 0.70 วินาที** (compare กับ OpenAI Realtime API ~1.2 วินาที median). **Reasoning token คิดลง 60%** = tool call ใน voice conversation เสร็จเร็วขึ้นเท่าตัว + cost ต่อ tool-call ต่ำลง 60%. Transcription accuracy สูงกว่า dedicated STT model (Whisper Large v3, Deepgram Nova-3) **1.5-2x ใน clean audio** และสูงถึง **10x ใน degraded audio + phone-line noise** ครอบคลุม 24 languages รวม ไทย/ญี่ปุ่น/เกาหลี. xAI ระบุว่า train บน "conditions such as background noise + degraded audio over phone lines" — ตรง contact-center use case โดยตรง

**Pricing** = **$0.08 per minute of audio** — ตัวเลขที่จะสั่นตลาด voice agent. เปรียบเทียบ: OpenAI Realtime API (GPT-5.6 Sol Voice) ล่าสุด $0.18/นาที audio (Anthropic ยังไม่มี voice-native offering); Google Gemini Live $0.12/นาที; ElevenLabs Conversational AI $0.10/นาที (Turbo v3 model); Retell AI $0.07-0.15/นาที (ขึ้นกับ voice + LLM); Vapi $0.05-0.20/นาที ขึ้นกับ stack. xAI เข้ามาที่ $0.08 พร้อม intelligence tier ที่ใกล้เคียงหรือดีกว่า GPT-5.6 Sol Voice = **44% cheaper than OpenAI Realtime + comparable/better quality** + ดีที่สุดใน noisy environment (contact-center reality). 

**Story ที่ต่อยอด** — xAI เพิ่ง cut OpenAI Terra 20% + Luna 80% เมื่อ 30 ก.ค. (voice ตัวก่อน + text). Grok Voice Think Fast 2.0 routing วันนี้ = **third pricing cut ใน voice/text agent ภายใน 7 วัน**. OpenAI/Anthropic ยังไม่ counter — signal ว่า xAI พยายาม gain enterprise voice share ก่อน Q4 earnings cycle (Nov). Grok Build ก็เพิ่มฟีเจอร์ (/delete command + startup crash fix) — สื่อสารว่า xAI serious ในการ compete developer stack ไม่ใช่แค่ B2C

## ทำไมสำคัญ

**Voice agent = category ที่ price shock กระทบ CX vendor economics โดยตรง**. Sierra ($200M ARR พ.ค. 26, $15.8B val Series C — 79x revenue multiple ที่ตลาด public equity เริ่ม question) เพิ่งขยับจาก text-only → voice-first ในไตรมาสที่ผ่านมา. Decagon ($35M ARR ต.ค. 25 → คาดการณ์ $60-70M กลาง 26, $4.5B val ม.ค.) run voice บน stack ที่ compose OpenAI + Deepgram. **Cost stack ของทั้งคู่ compose ที่ ~$0.14-0.20/นาที**. Grok Voice ที่ $0.08 = margin structure เปลี่ยน — ทั้งสองต้องเลือก: (1) swap ไป Grok Voice = margin ดีขึ้น 20-30% ทันที แต่ dependency บน xAI, (2) stick กับ OpenAI = ต้อง raise price ต่อ customer หรือ margin หด. Yellow.ai ที่ SPAC $550M ที่เพิ่ง roll-up BPO เมื่อ 3 ส.ค. — **economic case ของ "ซื้อ BPO แล้ว replace agent ด้วย voice bot" ดีขึ้นทันที** เพราะ variable cost ต่อ voice-minute ลง 44%

**Pattern ที่จะเกิดต่อ 30-90 วัน**: (1) Sierra/Decagon/Cresta/Retell/Vapi bake-off Grok Voice vs. incumbent; startup ที่ move เร็วจะ margin expansion เร็ว, ที่ช้า = investor ถามคำถาม, (2) OpenAI counter — คาดการณ์ GPT-5.6 Sol Voice pricing cut 30-40% ก่อน Q4 (จะประกาศช่วง OpenAI DevDay ก.ย. หรือ pre-holiday), (3) Anthropic ship voice-native API (rumor Claude Voice) ที่ต้อง price ไม่เกิน $0.10/นาที ถึงจะแข่งได้, (4) Contact-center incumbent (Genesys Cloud CX, NICE CXone, Verint, Concentrix, Teleperformance) เร่ง native Grok Voice integration หรือ pricing renegotiation, (5) **BPO roll-up thesis ของ Yellow.ai ทำงานเร็วขึ้น** — margin จาก "replace agent seat with voice bot" งอกขึ้น 15-20% ทันที

**Enterprise procurement angle**: CFO ที่ evaluate voice AI Q3-Q4 2026 = ตอนนี้มี **3-column pricing comparison ที่ Grok เป็น floor** ($0.08). OpenAI + Google ต้องอธิบายว่าทำไม price สูงกว่า 50-125%. Startup ที่ raise ที่ high multiple (Sierra 79x, Decagon 128x ที่ $35M ARR) ต้อง demonstrate margin resilience ต่อ pricing shock ใน next round pitch — ไม่ใช่แค่ ARR growth. **Voice agent = commodity race แล้ว** — differentiation ไม่ใช่ latency/quality (Grok floor สูงพอ) แต่คือ **workflow integration + industry template + governance/compliance layer**

## มุม AI Agent Platform

**สำหรับ builders:** ถ้ากำลัง build voice agent — **run bake-off Grok Voice Think Fast 2.0 vs. current stack ภายใน 7 วัน**. Metric ที่ต้อง measure: (1) TTFB (time-to-first-audio, target <1s), (2) transcription accuracy บน real customer phone recording (โดยเฉพาะ Thai + English mix + noisy environment), (3) tool call latency + accuracy (Grok claim -60% reasoning tokens = สำคัญมาก), (4) cost per successful task completion (ไม่ใช่แค่ per minute — voice ที่ intelligence สูงกว่า resolve task ในเวลาสั้นกว่า). Migration path: xAI provide OpenAI-compatible endpoint — swap base_url ได้ในบรรทัดเดียว. **Kill switch + fallback** = เก็บ OpenAI Realtime เป็น backup เผื่อ Grok downtime + rate limit; multi-provider routing (ทำ 70/30 หรือ 90/10) จะเป็น standard 6 เดือน

**สำหรับ users/business:** Enterprise contact-center + CX team ที่ evaluate voice bot Q3-Q4 — **เพิ่ม Grok Voice ใน RFP short list ทันที** พร้อม 3-column comparison กับ OpenAI Realtime + Google Gemini Live. Question ที่ต้องถาม vendor: (1) integrate Grok Voice ได้ไหม (Sierra/Decagon/Cresta), (2) pricing model ที่ share margin savings ไหม, (3) SLA + observability + compliance (EU AI Act 2 ส.ค. enforcement — voice ที่ interact กับ EU customer ต้อง audit + human oversight + kill switch), (4) Thai + ASEAN language quality บน real recording. **Thai enterprise ที่ run contact center** (AIS, DTAC/True, KBank Call Center, SCB Call Center, PTT Group, Muang Thai Insurance, Central Group Service Center) — pilot Grok Voice บน low-risk queue (billing inquiry, account balance, hours-of-operation) ก่อน scale

**สำหรับ ecosystem:** Winner — **xAI** (voice pricing leader + intelligence tier top-3), **BPO/contact-center vendor ที่พลิกเร็ว** (Yellow.ai + Concentrix + Teleperformance ที่ integrate ก่อน Q4), **Retell + Vapi + LiveKit** ที่ multi-provider ตั้งแต่ต้น (Grok เป็น 1 ใน 4-5 model). Loser — **standalone voice startup ที่ pitch "cheap voice" without workflow integration** (Grok pricing ต่ำกว่า), **model provider ที่ยังไม่มี voice-native** (Anthropic — ต้อง ship Claude Voice Q4 หรือ lose CX market share ทั้งหมดใน 12 เดือน). **Enabridge angle**: Thai SI + Thai voice agent startup (Amity, Sanuk, ChomChob, Voice-savvy vendor) ที่ integrate Grok Voice ตั้งแต่วันนี้ + build Thai-language voice template + governance package ตาม EU AI Act (สำหรับ EU-linked Thai enterprise) จะ open door Thai SET50 contact-center RFP ที่ปกติ Genesys/NICE ครองมา 15 ปี. **Package**: voice agent workflow ($30-80K setup) + monthly usage-based Grok Voice + governance/compliance retainer = TAM ที่แข่งกับ incumbent contact-center ได้ที่ price 40-60% ต่ำกว่า

## Sources
- [Introducing Grok Voice Think Fast 2.0 — SpaceXAI](https://x.ai/news/grok-voice-think-fast-2)
- [xAI Release Notes — Releasebot](https://releasebot.io/updates/xai)
- [xAI Unveils Voice AI 'Grok Voice Think Fast 2.0' with Dramatically Improved Transcription Accuracy — BigGo Finance](https://finance.biggo.com/news/4bf16f12-1046-46f1-8d01-aa9649230336)
- [Grok Voice Think Fast 2.0 API — July 2026 — explainx.ai Blog](https://www.explainx.ai/blog/grok-voice-think-fast-2-speech-to-speech-july-2026)
- [xAI upgrades Grok Voice with faster Think Fast 2 mode — YourStory](https://yourstory.com/ai-story/xai-grok-voice-think-fast-2)
- [SpaceXAI Docs — Release Notes](https://docs.x.ai/developers/release-notes)

---

## Audio script
วันอังคาร 5 สิงหาคม xAI ยืนยันว่า API endpoint grok-voice-latest ทุก request จะถูก auto-route ไป Grok Voice Think Fast 2.0 speech-to-speech เริ่มวันนี้. Developer ไม่ต้องเปลี่ยน code — request เข้า model ใหม่โดยอัตโนมัติ. Performance ที่ xAI publish — 82.9% Artificial Analysis Speech-to-Speech Quality Index สูงกว่า OpenAI GPT-5.6 Sol Voice ที่ 78.4%. Time-to-first-audio 0.70 วินาที เทียบกับ OpenAI Realtime ที่ 1.2 วินาที. Reasoning token คิดลง 60%. Transcription accuracy ดีกว่า Whisper และ Deepgram 1.5 ถึง 2 เท่าใน clean audio และสูงถึง 10 เท่าใน noisy phone-line.

Pricing ที่จะสั่นตลาด — 0.08 ดอลลาร์ต่อนาที audio. OpenAI Realtime อยู่ที่ 0.18 ดอลลาร์, Google Gemini Live 0.12, ElevenLabs Conversational 0.10. xAI เข้ามาถูกกว่า OpenAI 44% พร้อม intelligence tier ใกล้เคียงหรือดีกว่า. เป็น price cut ตัวที่ 3 ของ xAI ภายใน 7 วัน หลัง OpenAI Terra กับ Luna cut ปลาย ก.ค.

Signal ที่กระทบ CX vendor — Sierra 200 ล้านดอลลาร์ ARR, Decagon 4.5 พันล้านดอลลาร์ valuation, Cresta, Retell, Vapi ทั้งหมดต้องเลือก swap ไป Grok Voice เพื่อรักษา margin หรือ raise price. Yellow.ai ที่เพิ่ง SPAC 550 ล้านดอลลาร์กับ Bluerock — economic case ของ ซื้อ BPO แล้ว replace agent ด้วย voice bot ดีขึ้นทันทีเพราะ variable cost ต่อ voice minute ลง 44%. สำหรับ Thai enterprise ที่ run contact center อย่าง AIS, KBank, SCB, PTT — pilot Grok Voice บน low-risk queue ก่อน scale. Enabridge angle — Thai SI ที่ integrate Grok Voice ตั้งแต่วันนี้ + build Thai-language voice template + governance package ตาม EU AI Act จะเปิดประตู SET50 contact-center RFP ที่ Genesys กับ NICE ครองมา 15 ปี ที่ราคา 40 ถึง 60% ต่ำกว่า.
