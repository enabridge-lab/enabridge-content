---
date: 2026-07-10
slug: openai-gpt-5-6-sol-terra-luna-live-agentic-tier
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  A wide editorial isometric scene: three glowing model orbs floating above a
  server rack labeled "GPT-5.6" — one large orange "SOL — FRONTIER AGENTIC",
  one medium blue "TERRA — EVERYDAY, 2X CHEAPER", one small green "LUNA —
  FASTEST". Behind them a fourth waveform-shaped orb marked "GPT-LIVE-1 —
  FULL DUPLEX VOICE". Along the bottom a pricing billboard reads
  "$5 / $30", "$2.50 / $15", "$1 / $6" per 1M tokens. Off to the side a
  logo panel: "CODEX + GITHUB COPILOT — DAY 1". Cinematic editorial
  lighting, high contrast, 1:1 aspect, readable at 200px thumbnail, no real
  human faces.
image: images/26-07-10-0608-04-openai-gpt-5-6-sol-terra-luna-live-agentic-tier.png
---

# OpenAI ปล่อย GPT-5.6 Sol/Terra/Luna + GPT-Live วันนี้ (9 ก.ค.) — model tier แยกตาม agentic use case ชัดเจน, GitHub Copilot รับ day-1

## TL;DR
- OpenAI **rollout GPT-5.6 ทั่ว ChatGPT, Codex, และ API** เริ่ม 9 ก.ค. 2026 — 3 tier: **Sol (frontier, long-horizon agentic), Terra (everyday balanced, GPT-5.5-comp performance ที่ราคาถูกครึ่งหนึ่ง), Luna (fastest/cheapest)**
- Pricing per 1M token: **Sol $5/$30, Terra $2.50/$15, Luna $1/$6** — Terra ราคาเดียวกับ Gemini 2.5 Pro, Luna แข่งกับ Sonnet 5 tier กลาง
- **GPT-Live-1 + GPT-Live-1 mini** — full-duplex voice model (listen + speak พร้อมกัน) ปล่อยเป็น default voice สำหรับทุก tier
- **GitHub Copilot support day-1** — Sol/Terra/Luna เข้า Copilot ตั้งแต่ประกาศ + ChatGPT Plus/Pro/Business/Enterprise access ตาม tier

## เกิดอะไรขึ้น
วันพุธ 8 ก.ค. (US time) OpenAI ประกาศ end government-limited preview ของ GPT-5.6 และ **rollout ทั่ว ChatGPT + Codex + API เริ่ม 9 ก.ค. 10:00 PT**. โครงสร้าง model แบ่งเป็น 3 tier — **Sol** สำหรับ frontier reasoning + long-horizon agentic work, **Terra** เป็น everyday balanced ที่ performance เทียบเท่า GPT-5.5 ที่ราคาครึ่งหนึ่ง, **Luna** เป็น fastest + cheapest สำหรับ high-volume workload

Pricing per 1M token ชัดเจน: **Sol $5 input / $30 output, Terra $2.50 / $15, Luna $1 / $6**. Terra ราคาใกล้ Gemini 2.5 Pro ($3.5/$10.5) แต่ประกาศ performance สูงกว่า; Luna ราคาต่ำกว่า Sonnet 5 mid tier ประมาณ 30-40%. ChatGPT Plus, Pro, Business, Enterprise เข้าถึง Sol ผ่าน medium+ effort setting; Pro + Enterprise ได้ **Sol Pro** สำหรับ complex work

พร้อมกันนั้น **GPT-Live-1 + GPT-Live-1 mini** ปล่อยเป็น full-duplex voice model — model listen + speak พร้อมกัน (interrupt-friendly), แทนที่ voice model เดิมของ ChatGPT ทุก tier. OpenAI บอกว่า "conversation feel like real conversation" — ลด latency ให้เหลือ sub-500ms, มี safety guardrail ผ่าน multi-org red team

Distribution partner day-1 ที่โดดเด่นที่สุด: **GitHub Copilot** — Sol/Terra/Luna พร้อมใช้ใน Copilot Chat + Agent Mode ตั้งแต่วันประกาศ (ประกาศบน GitHub blog changelog เวลาเดียวกัน). ChatGPT web + iOS + Android app upgrade default เป็น Sol สำหรับ Plus user, Terra สำหรับ Free user

## ทำไมสำคัญ
Model tier **แยกตาม agentic use case ชัดเจน** เป็น narrative shift ที่ OpenAI ไม่เคยทำ — GPT-4/GPT-5 ก่อนหน้านี้ pitch "หนึ่งโมเดล ทุก use case". **Sol positioning ตรง ๆ ว่า "long-horizon agentic work"** — คือ workload ประเภทที่ agent ทำ tool call 10-50 ครั้ง, plan/reason/critique ในลูป, ไม่ใช่ chat ตอบสั้น ๆ. Terra + Luna ทำ workload ที่ short + high-volume — เหมาะกับ classifier, extractor, router ใน agent pipeline

Pricing signal ที่แข่งขันชัด — **Terra $2.50/$15 คือ challenge ตรง ๆ ต่อ Sonnet 5** ที่ Anthropic ประกาศเป็น "agentic default" ในรอบก่อน. Anthropic เคย pitch Sonnet 5 เป็น model ที่ balance performance + cost สำหรับ agent เข้าถึงกว้าง; OpenAI ปล่อย Terra ที่ราคาใกล้เคียงและ tuning สำหรับ tool call. **สมรภูมิ mid-tier agentic model จะแข่งราคาลงต่ออีก 30-50% ในไตรมาสถัดไป**

Signal ที่ enterprise ต้องอ่าน — **cost per agent-hour กำลัง commoditize เร็วมาก**. เมื่อ 6 เดือนก่อน (มกราคม 2026) cost per 1M output token ของ frontier-tier model อยู่ที่ $60-90 (Claude Opus 4.7, GPT-5 Pro); ตอนนี้ Sol $30, Terra $15, Luna $6 — median cost drop **60% ในครึ่งปี**. Business ที่ pilot agent workload ในไตรมาส Q1 2026 ควรทำ cost model rerun ทันที — ROI จะดีขึ้นทันทีโดยไม่ต้องแก้ code, แค่ swap model endpoint

**GPT-Live ปลดล็อค voice-first agent** — call center, voice assistant, drive-thru ordering, in-store kiosk เป็น use case ที่ตอนนี้ economic viable แล้ว. Full-duplex + sub-500ms latency = ลูกค้ารู้สึกเหมือนคุยกับคนจริง. Retell AI, Vapi, Bland — startup voice agent ทั้งหมดต้องอัพเดต stack และ pricing model ทันที เพราะ underlying model ที่พวกเขา wrap upgrade แล้ว

## มุม AI Agent Platform
**Builders** — framework builder ที่ยัง hard-code model endpoint (GPT-4o, Sonnet 4) ต้อง migrate เข้า tiered routing model ทันที: **classifier/router → Luna, main reasoning → Terra, complex/long-horizon → Sol**. Framework ที่มี **model routing config + cost dashboard** (LangGraph, OpenRouter, LiteLLM) มี tailwind. Voice-first agent builder — Retell, Vapi, Bland, Deepgram — ต้องออก GPT-Live integration ใน 2 สัปดาห์ ไม่งั้นโดน bypass โดย Sol Voice API ที่ integrate ทางตรง

**Users/business ในไทย** — ธุรกิจที่มี call center 100+ seat (True Corp, DTAC, AIS, ธนาคารทุกเจ้า) ควร reopen voice agent RFP รอบใหม่ — GPT-Live + Sonnet Voice + Gemini Live 3 เจ้าแข่งกันอีก 2-3 เดือน. Retailer/CPG ที่มี AI agent workload ต้อง cost re-baseline — Terra จะทำให้ agentic workload ที่ ROI border line เข้าเกณฑ์ทันที. **Cost model ที่ CFO อนุมัติเมื่อ Q1 ควร rerun Q3** เพราะ input assumption เปลี่ยนมาก

**Ecosystem** — GitHub Copilot day-1 support = Microsoft ยัง**ยึดตำแหน่ง distribution partner ระดับสูงสุด**ของ OpenAI แม้จะแยกทาง Frontier Company ไป. Signal ว่า Copilot Enterprise เป็น channel ที่ OpenAI ไม่ยอมทิ้งง่าย ๆ. VS Code + JetBrains + Cursor + Zed — code editor ทุกเจ้าต้องรีบอัพเดต SDK ให้ทัน tiered routing config, ไม่งั้น developer จะไปใช้ Copilot ตรง ๆ

## Sources
- [OpenAI to publicly release GPT-5.6, rolls out Live voice AI models — CNBC](https://www.cnbc.com/2026/07/08/openai-expanding-gpt-5point6-ai-model-release-ending-government-limits.html)
- [GPT-5.6 Is Live: OpenAI Rolls Out Sol, Terra, and Luna Across ChatGPT, Codex, and the API — Nerova](https://nerova.ai/news/openai-gpt-56-live-chatgpt-codex-api-business-use-july-2026)
- [OpenAI's GPT-5.6 Sol, Terra, and Luna are now available in GitHub Copilot — GitHub Changelog](https://github.blog/changelog/2026-07-09-openais-gpt-5-6-sol-terra-and-luna-are-now-available-in-github-copilot/)
- [Introducing GPT-5.6 series: Sol, Terra and Luna. Coming July 9 10am PT — OpenAI Developer Community](https://community.openai.com/t/introducing-gpt-5-6-series-sol-terra-and-luna/1384931)

---

## Audio script
วันพุธที่ 8 กรกฎาคม OpenAI ประกาศ end government-limited preview ของ GPT-5.6 rollout ทั่ว ChatGPT Codex และ API เริ่มวันที่ 9 กรกฎาคม 10 โมงเช้าเวลา Pacific โครงสร้าง model แบ่งเป็น 3 tier ชัดเจน Sol สำหรับ frontier reasoning และ long-horizon agentic work Terra เป็น everyday balanced ที่ performance เทียบเท่า GPT-5.5 ที่ราคาครึ่งหนึ่ง Luna เป็น fastest cheapest สำหรับ high volume workload Pricing per 1 ล้าน token Sol 5 ดอลลาร์ input 30 output Terra 2.50 กับ 15 Luna 1 กับ 6 Terra ราคาใกล้ Gemini 2.5 Pro Luna ต่ำกว่า Sonnet 5 mid tier ประมาณ 30 ถึง 40 เปอร์เซ็นต์ พร้อมกันนั้น OpenAI ปล่อย GPT-Live-1 กับ GPT-Live-1 mini เป็น full duplex voice model listen speak พร้อมกัน latency sub 500 ms Distribution partner day-1 ที่โดดเด่นสุดคือ GitHub Copilot ใช้ Sol Terra Luna ได้ตั้งแต่วันประกาศ narrative shift ที่ OpenAI ไม่เคยทำคือ model tier แยกตาม agentic use case ชัดเจน Sol positioning ตรง ๆ ว่า long horizon agentic work ไม่ใช่ chat ตอบสั้น ๆ Terra Luna เหมาะกับ classifier extractor router ใน agent pipeline pricing signal สำคัญ Terra 2.50 กับ 15 คือ challenge ตรง ๆ กับ Sonnet 5 สมรภูมิ mid tier agentic model จะแข่งราคาลงต่ออีก 30 ถึง 50 เปอร์เซ็นต์ในไตรมาสถัดไป cost per agent hour กำลัง commoditize เร็ว 6 เดือนก่อน frontier tier อยู่ที่ 60 ถึง 90 ดอลลาร์ ตอนนี้ Sol 30 Terra 15 Luna 6 median drop 60 เปอร์เซ็นต์ในครึ่งปี สำหรับธุรกิจไทย call center 100 seat ขึ้นไป True DTAC AIS ธนาคารทุกเจ้าควร reopen voice agent RFP รอบใหม่ GPT-Live กับ Sonnet Voice กับ Gemini Live 3 เจ้าแข่งกันอีก 2 ถึง 3 เดือน retailer ที่มี AI agent workload ต้อง cost re-baseline Terra จะทำให้ workload ที่ ROI border line เข้าเกณฑ์ทันที
