---
date: 2026-07-11
slug: xai-grok-4-5-cursor-coding-agent-60-percent-cheaper
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  A dramatic isometric market-floor scene: a giant scoreboard labeled
  "ARTIFICIAL ANALYSIS INTELLIGENCE INDEX" with four ranked entries — "#1 GPT-
  5.6", "#2 CLAUDE OPUS 4.8", "#3 GEMINI 3 ULTRA", "#4 GROK 4.5". Below the
  scoreboard, three neon price tags glow in front of the Grok 4.5 tile:
  "$2 IN", "$6 OUT", "-60% vs OPUS". On the right, a smaller shop titled
  "CURSOR" hands over training data through a glowing tube into the Grok
  tower. Editorial isometric style, high contrast, night lighting, 1:1
  aspect, readable at 200px thumbnail, no real human faces.
image: images/26-07-11-0609-02-xai-grok-4-5-cursor-coding-agent-60-percent-cheaper.png
---

# Grok 4.5 กระโดดขึ้นอันดับ 4 บน Intelligence Index — ราคาถูกกว่า Opus 4.8 / GPT-5.5 กว่า 60% coding agent commodity แล้ว

## TL;DR
- xAI เปิดตัว **Grok 4.5** (8 ก.ค.) — foundation model 1.5 ล้านล้าน parameter (V9), **co-train กับ Cursor** ใน multi-step software engineering task ระดับแสนตัวอย่าง, train บน NVIDIA GB300 หลายหมื่นตัว
- ราคา **$2 / 1M input + $6 / 1M output tokens** — **ถูกกว่า Claude Opus 4.8 และ GPT-5.5 มากกว่า 60%** — พร้อมขึ้นอันดับ 4 บน Artificial Analysis Intelligence Index เหนือทุก Gemini + open-weight model
- **EU ยังไม่มี** (target กลาง ก.ค.). Available ผ่าน xAI API, Grok Build (coding agent harness ของ xAI เอง), และ **Cursor ทุก plan** — coding agent kit commodity price ปีนี้จบเกม

## เกิดอะไรขึ้น
วันพุธ 8 กรกฎาคม 2026 xAI ปล่อย **Grok 4.5** — model foundation ตัวใหม่ที่บริษัทเรียกเองว่า "flagship for coding, agentic, and knowledge work". Foundation คือ V9 architecture ขนาด **1.5 ล้านล้าน parameter**, train บน NVIDIA GB300 GPU หลายหมื่นตัว, พร้อม RL pipeline ที่ครอบคลุมงาน software engineering แบบ multi-step **หลายแสนตัวอย่าง** — grading ทั้งแบบ automated + model-based

จุดที่แตกต่างจาก Grok รุ่นก่อน: **xAI ประกาศชัดว่า co-train กับ Cursor** — code editor ที่มี market share developer AI-native สูงสุดในตลาดปัจจุบัน. RL rollout วิ่งต่อเนื่องหลายชั่วโมงต่อ session, learning วิ่ง parallel ระหว่างที่ agent execute จริง. ผลลัพธ์คือ model ที่ **ขึ้นอันดับ 4 บน Artificial Analysis Intelligence Index** ทันที — เหนือทุก Gemini variant และทุก open-weight model ที่มีในตลาด

ราคาคือช็อกที่สุด: **$2 / 1M input tokens + $6 / 1M output tokens** พร้อม reasoning effort ที่ config ได้ (low / medium / high, default high). เทียบ Claude Opus 4.8 (~$15/$75) และ GPT-5.5 (~$8/$24) — Grok 4.5 **ถูกกว่าอย่างน้อย 60%** ในทุก tier. Availability: xAI API (`grok-4.5`), Grok Build (agent harness ของ xAI เอง), และ **Cursor ทุก plan รวม free tier**

Caveat สำคัญ: **EU ยังไม่ available** ทั้ง xAI product และ API console — target กลางเดือน ก.ค.. ตลาด EU financial services / healthcare ที่มี GDPR + AI Act constraint จะยังไม่ทำ pilot ได้ในช่วงนี้

## ทำไมสำคัญ
Coding agent เพิ่งได้ถูก commoditize อย่างเป็นทางการ. เมื่อ 6 เดือนก่อน, Cursor + Claude Sonnet 4.5 คือ default combo ระดับ premium; developer ทั่วโลกจ่าย $20/เดือน + Anthropic เก็บ margin ทั้ง API. Grok 4.5 เข้ามาโดย (1) มี performance ระดับ frontier (อันดับ 4 บน Intelligence Index), (2) ราคาต่ำกว่า 60%, (3) **integrate เข้า Cursor ตรง ๆ ทุก plan รวม free** — developer จะ default ใช้ Grok 4.5 ก่อน Anthropic ในหลาย workload ทันที

ประเด็นที่ Anthropic + OpenAI ต้องกลัวไม่ใช่ tech, แต่คือ **channel**. Cursor มี user active หลายล้านคน; ก่อนหน้านี้ Anthropic ครอง experience เพราะ Cursor default ใช้ Claude. เมื่อ xAI จับมือ co-train Grok 4.5 กับ Cursor โดยตรง, Cursor CEO Michael Truell ส่ง signal ว่า "**model diversity คือ moat ของ editor**" — ลูกค้า Cursor ไม่ต้อง lock-in vendor เดียว. Anthropic จะเสียส่วนแบ่ง developer segment ที่ price-sensitive ใน 90 วัน

Pattern ระดับใหญ่: OpenAI ตอบด้วย ChatGPT Work (vertical integration — เก็บ workflow ทั้งหมดในหอตัวเอง), Anthropic ตอบด้วย Cowork + Sonnet 5 (agent quality), xAI ตอบด้วย **ราคา + Cursor channel**. สามยุทธศาสตร์ต่างกันคนละแนว, แต่ **Grok เดินเลนที่ปลอดการปะทะกับ product ของ hyperscaler ตรง ๆ** (ต่างจาก Cowork ที่แย่ง Copilot). Position นี้ยั่งยืนแค่ไหน ขึ้นกับว่า Elon จะยอมกิน margin ต่อไปนานแค่ไหน — และประวัติ Tesla + SpaceX บอกว่าเขาไม่กลัว price war

ตัวเลข benchmark ที่ควรระวัง: Artificial Analysis Intelligence Index รวม reasoning + coding + knowledge; **coding-specific benchmark** (SWE-bench Verified, LiveCodeBench) ยังไม่มี independent score. xAI + Cursor co-train ทำให้เป็นไปได้ที่ Grok 4.5 overfit กับ Cursor task distribution — enterprise ที่ใช้ VS Code + Copilot หรือ IDE เก่าอื่นควรทดสอบ workload ตัวเองก่อนเชื่อ marketing

## มุม AI Agent Platform
- **Builders** — startup ที่ทำ coding agent (Cognition Devin, Cursor เอง, Codeium, Sourcegraph Cody, Continue.dev) เข้าสู่ **โซนราคา race-to-bottom** อย่างเป็นทางการ. Differentiator ใหม่ต้องเป็น (1) integration depth กับ codebase เก่า (mainframe, COBOL, ERP customization), (2) governance / audit trail สำหรับ regulated industry — 8090 Labs ที่ปิด $135M นำโดย Salesforce Ventures สัปดาห์ที่แล้ววาง moat ตรงนี้พอดี, หรือ (3) **domain-specific agent** ที่ generalist model ไม่ครอบ (game dev, embedded, hardware verification)

- **Users / business ในไทย** — CTO / VP Engineering ที่ negotiate Anthropic / OpenAI contract Q3 นี้ควร **ใช้ Grok 4.5 pricing เป็น anchor** เจรจา discount 30–50%. Developer team ที่ใช้ Cursor อยู่แล้วเปิด Grok 4.5 ทดสอบทันที — ไม่มี switching cost. **ยกเว้น EU subsidiary** ที่ต้องรอกลาง ก.ค. + AI Act audit ก่อน production. Startup ไทยที่ burn rate สูงและใช้ Claude Opus 4.8 เป็น backend agent ควร A/B test workload ตัวเองบน Grok 4.5 ในสัปดาห์นี้ — 60% cost saving คือ 6 เดือน runway เพิ่ม

- **Ecosystem** — Anthropic + OpenAI จะต้อง **ลด API price ในสัปดาห์ 2–3 ข้างหน้า** (โมเดล Sonnet 5 tier ล่างจะเป็นกระสุนแรก) หรือไม่ก็ต้องกลับไปเน้น distribution deal ระดับ hyperscaler (Bedrock, Vertex, Azure). Cursor + Editor category จะกลายเป็น **battlefield** ที่ frontier lab แข่งชนะ mind share developer — model ที่ไม่ได้อยู่ใน Cursor default = model ที่หายจาก consciousness developer ใน 6 เดือน. NVIDIA รับประโยชน์เต็ม ๆ — GB300 fleet ของ xAI + margin ยังไม่ compete กับตัวเอง

## Sources
- [xAI Launches Grok 4.5 With Deep Agentic and Code Execution Capabilities, Raising Enterprise Governance Stakes — AI Governance Institute](https://aigovernance.com/news/xai-grok-4-5-agentic-coding-governance-compliance)
- [SpaceXAI Launches Grok 4.5 Model for Coding, Agentic Tasks — U.S. News](https://money.usnews.com/investing/news/articles/2026-07-08/spacexai-launches-grok-4-5-model-for-coding-agentic-tasks)
- [Scoop: SpaceXAI launches new model, Grok 4.5 — Axios](https://www.axios.com/2026/07/08/spacexai-grok-new-model)
- [Grok 4.5 Released — Coding, Agents, and What Engineers Should Know — Slipmp](https://www.slipmp.com/blog/grok-4-5-released-coding-agents-and-what-engineers-should-know/)

---

## Audio script
วันพุธที่ผ่านมา xAI ปล่อย Grok 4.5 ออกมา นี่คือ foundation model ขนาด 1.5 ล้านล้าน parameter train บน NVIDIA GB300 หลายหมื่นตัว ที่น่าสนใจกว่าตัวเลขคือ xAI co-train กับ Cursor code editor ที่ developer ใช้เยอะที่สุดในตลาด AI-native ตอนนี้ ผลคือ Grok 4.5 ขึ้นไปอันดับ 4 บน Artificial Analysis Intelligence Index ทันที เหนือทุก Gemini variant และทุก open-weight model ราคาคือช็อคที่สุด สองดอลลาร์ต่อล้าน input token หกดอลลาร์ต่อล้าน output token ถูกกว่า Claude Opus 4.8 และ GPT-5.5 กว่า 60 เปอร์เซ็นต์ทุก tier ใช้ผ่าน xAI API, Grok Build, และ Cursor ทุก plan รวม free tier ด้วย มี caveat ว่า EU ยัง unavailable รอกลางเดือนนี้ signal ใหญ่คือ coding agent ถูก commoditize อย่างเป็นทางการ Cursor เคยเป็น default combo กับ Claude Sonnet 4.5 พอ Cursor เปิดให้ Grok เข้ามาแข่งใน default plan เดียวกัน developer ที่ price-sensitive จะย้ายทันทีในหลาย workload สำหรับธุรกิจไทย CTO ที่ negotiate contract Anthropic OpenAI ช่วง Q3 นี้ควรใช้ราคา Grok 4.5 เป็น anchor ขอลด 30 ถึง 50 เปอร์เซ็นต์ developer team ที่ใช้ Cursor อยู่แล้ว เปิด Grok 4.5 ทดสอบได้ทันทีไม่มี switching cost startup ที่ burn rate สูงและใช้ Opus 4.8 เป็น backend agent ควรลอง A/B test workload ตัวเอง 60 เปอร์เซ็นต์ cost saving คือ runway หกเดือนเพิ่มขึ้นทันที ยกเว้น EU subsidiary รอ AI Act audit ก่อน production
