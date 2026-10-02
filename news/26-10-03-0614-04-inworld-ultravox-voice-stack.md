---
date: 2026-10-02
slug: inworld-ultravox-voice-stack
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: |
  Editorial isometric illustration of two glowing speech bubbles labeled
  "INWORLD" and "ULTRAVOX" fusing into a single waveform ribbon that wraps
  a tiny globe. Three stacked tags float above: "SUB-100ms LATENCY",
  "200+ LANGUAGES", "TTS-2 UPGRADE". A microphone and a tiny speaker sit on
  opposite ends like endpoints of a call. Cinematic violet and amber
  palette, sharp contrast for 200px thumbnails, bold text rendering, no
  real human faces, 1:1 aspect. Style of a Wired magazine cover story.
image: images/26-10-03-0614-04-inworld-ultravox-voice-stack.png
---

# Inworld ซื้อ Ultravox — รวม voice agent + model inference เป็น full stack เดียว ยิง sub-100ms ใน 200+ ภาษา

## TL;DR
- 1 ต.ค. **Inworld ซื้อ Ultravox** — platform สำหรับสร้าง real-time voice agent ที่มี turn-taking + interruption handling ที่ developer ใช้กันอยู่ (deal terms ไม่เปิดเผย)
- รวมเข้า Inworld voice stack = **sub-100ms latency + 200+ languages** + upgrade built-in voice ทั้งหมดเป็น **Realtime TTS-2** ฟรีไม่ต้องแตะ code
- play คือ **consolidate voice agent infra ให้เหลือ single vendor** ก่อน OpenAI/Google ยัดเข้า default stack ของ developer

## เกิดอะไรขึ้น
Inworld — AI research lab ที่เริ่มจาก voice agent สำหรับ gaming + learning app แล้วขยายเป็น general voice infrastructure — ประกาศ 1 ตุลาคมว่าซื้อ **Ultravox**, platform ที่ developer หลายพัน startup ใช้สร้าง real-time voice agent. Ultravox ไม่ใช่ household name แต่ underlying ของมันคือหนึ่งใน open source speech-to-speech model ที่หลายทีมพึ่งพาสำหรับ turn-taking และ interruption handling — สองความสามารถที่ voice interaction ที่ "คุยแล้วไม่เขิน" ต้องมี.

Terms ของ deal ไม่เปิดเผย. ที่เปิดเผยคือ Ultravox จะ fold เข้า Inworld เป็น "full voice stack" — รวม speech-to-speech research, voice agent capability, real-time TTS. Existing Ultravox customer ได้ upgrade voice ทั้งหมดเป็น **Realtime TTS-2** ของ Inworld ฟรี ไม่ต้องแก้ code ไม่ต้องจ่ายเพิ่ม. ตัวเลข spec ที่ Inworld โฆษณา: **sub-100ms latency + 200+ languages**. ทีม Ultravox ย้ายเข้ามาต่อ development.

Context ใหญ่คือ **สนาม voice agent เริ่ม consolidate หนัก**. ปีที่แล้ว ElevenLabs, Cartesia, PlayHT, Deepgram, Rime, Resemble AI ทั้งหลายอยู่คนละมุม — แต่ละตัว strong ด้าน แต่ developer ที่สร้าง voice product ต้องผสมหลายเจ้าเข้าด้วยกัน (TTS จาก A + STT จาก B + turn-taking จาก C). OpenAI กับ Google ยัด voice เป็น native API ตั้งแต่ Realtime API ออก ทำให้ pricing ของ independent voice startup compress ลง 30-50%. Inworld + Ultravox เป็น M&A move แรกใน 2026 ที่พยายามรวม layer เข้ามาก่อนที่ hyperscaler จะกลืน.

## ทำไมสำคัญ
Signal แรก: **voice agent กำลังจะกลายเป็น commoditized infrastructure**. ภายใน 12 เดือนทุก agent framework จะ bundle voice เป็น default feature — เหมือนที่ chat ถูก bundle ตอน 2024. ตัวเลข sub-100ms latency + 200+ languages ที่ Inworld โฆษณาแปลว่า voice interaction ไม่ใช่ "nice to have" อีกต่อไปแต่เป็น table stake. ภาษาไทย คงอยู่ใน 200+ ถ้าใครยังขาย Thai-specific voice startup ด้วย premium pricing ต้องรีบ pivot ภายใน 6 เดือน.

Angle คม: **Inworld play คือ anti-ElevenLabs**. ElevenLabs market cap $11B+ แต่ positioning อยู่ที่ voice cloning + content creation — ไม่ใช่ real-time agent-first. Inworld สร้าง moat ตรง gap นี้ — voice ที่เน้น conversation ไม่ใช่ production. เมื่อ enterprise ส่วนใหญ่ที่ deploy voice agent (contact center, inside sales, outbound call) ต้องการ latency + language scale ไม่ใช่ celebrity voice clone — Inworld + Ultravox positioned ดีกว่า ElevenLabs ในตลาด enterprise voice agent ที่มี TAM ใหญ่กว่า voice cloning หลายเท่า.

ความเสี่ยงอยู่ที่ **OpenAI กับ Google**. Realtime API ของ OpenAI รองรับ speech-to-speech ที่ latency ใกล้เคียง (120-150ms). Google เพิ่ง ship Gemini 3.8 Live Extended Thinking ที่ voice agent performance ดีขึ้นเยอะ. ถ้าสองเจ้าลดราคาลงมาที่ parity กับ Inworld pricing ตอนนี้ voice-first startup ทุกเจ้าต้องเลือกจะ specialize ไปทาง deep vertical (medical dictation, legal transcription) หรือ exit ทาง M&A. Inworld + Ultravox น่าจะต้องเร่ง ship enterprise feature ก่อนที่ Realtime API GA เต็มรูปแบบ.

## มุม AI Agent Platform
**Builders** — ถ้าคุณสร้าง agent framework ที่ยังเรียก voice ผ่าน TTS/STT API แยกกันอยู่ ควร re-architect เป็น speech-to-speech stack ภายในไตรมาสนี้ — latency จาก sub-100ms vs 300-500ms เป็น difference ที่ user รู้สึก. Inworld + Ultravox เพิ่ม pressure ให้ framework (LangGraph, Agno, Mastra, CrewAI) ต้องมี **native voice stage** ใน workflow definition. **Users/Business** — ธุรกิจที่ run contact center หรือ outbound call operation ใหญ่ (เช่น US insurance, Thai banking, Philippine BPO) ควร pilot voice agent ของ Inworld ตั้งแต่ Q4 นี้. ตัวเลขที่น่าจับตา: sub-100ms latency = conversation feel natural เท่ากับ human — เมื่อ agent interrupt และ turn-take ได้ดี customer satisfaction ไม่ลด (ปัจจุบัน IVR score drop 15-25%). **Ecosystem** — ElevenLabs, Cartesia, Rime ต้องตอบด้วย M&A หรือ product pivot ภายใน 6-9 เดือน. Deepgram ที่ specialize STT ต้องขยายเป็น full stack หรือยอมเป็น vendor layer ของ Inworld/OpenAI. VC ที่ fund voice startup ปี 2024-2025 จะเห็น consolidation wave ภายในปีหน้า — likely 2-3 M&A ใหญ่ก่อน Q2 2027.

## Sources
- [AI Research Lab Inworld Acquires Voice Agent Platform Ultravox — Yahoo Finance / Business Wire](https://finance.yahoo.com/technology/ai/articles/ai-research-lab-inworld-acquires-211500825.html)
- [Inworld acquires Ultravox to add a voice-agent platform to its speech stack — RuntimeWire](https://runtimewire.com/article/inworld-acquires-ultravox-voice-agents)
- [Inworld Buys Ultravox and Upgrades Only Its Own Voices — Beri.net](https://www.beri.net/article/inworld-ultravox-acquisition-voice-agent-platform-third-party-tts-continuity-pricing)

---

## Audio script
ข่าว M&A สนาม voice agent วันนี้ครับ. 1 ตุลาคม Inworld ซึ่งเป็น AI research lab ที่เริ่มจาก voice agent สำหรับ gaming กับ learning app ประกาศซื้อ Ultravox — platform ที่ developer หลายพัน startup ใช้สร้าง real-time voice agent ที่มี turn-taking กับ interruption handling. Terms ไม่เปิดเผย. ที่เปิดเผยคือ Ultravox จะรวมเข้า Inworld เป็น full voice stack ที่ชู spec sub-100ms latency และ 200 ภาษา. Existing Ultravox customer upgrade เป็น Realtime TTS-2 ของ Inworld ฟรี. Context ใหญ่คือสนาม voice agent เริ่ม consolidate หนัก. ปีที่แล้ว ElevenLabs Cartesia PlayHT Deepgram Rime Resemble อยู่คนละมุม developer ต้องผสมหลายเจ้าเข้าด้วยกัน. OpenAI กับ Google ยัด voice เป็น native API ตั้งแต่ Realtime API ออก ทำให้ pricing ของ independent voice startup compress ลง 30 ถึง 50 เปอร์เซ็นต์. Inworld plus Ultravox เป็น M&A move แรกใน 2026 ที่พยายามรวม layer เข้ามาก่อน hyperscaler จะกลืน. Signal สำคัญคือ voice agent กำลังจะกลายเป็น commoditized infrastructure ภายใน 12 เดือน ทุก framework จะ bundle voice เป็น default feature. Angle ที่คมคือ Inworld play เป็น anti-ElevenLabs. ElevenLabs market cap 11 พันล้านดอลลาร์ positioning อยู่ที่ voice cloning + content creation. Inworld positioned ดีกว่าในตลาด enterprise voice agent. ความเสี่ยงอยู่ที่ OpenAI กับ Google ที่ Realtime API ของพวกเขาเองรองรับ speech-to-speech ใกล้เคียง. Builder ที่ยังเรียก TTS กับ STT API แยกกันอยู่ควร re-architect เป็น speech-to-speech stack ภายในไตรมาสนี้ครับ.
