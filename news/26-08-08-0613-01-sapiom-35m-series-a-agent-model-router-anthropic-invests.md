---
date: 2026-08-08
slug: sapiom-35m-series-a-agent-model-router-anthropic-invests
topic: agentic-ai
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial isometric illustration of a giant traffic control tower labeled
  "SAPIOM ROUTER" sitting between a swarm of small AI agent icons on the
  left and a row of five model boxes on the right — the boxes are stacked
  from cheapest to most expensive, tagged "FLASH", "MID", "PRO", "OPUS",
  "MAX". Glowing routing paths show most agents being sent to FLASH/MID,
  with only a thin premium lane going up to OPUS/MAX. A large ticker on
  the tower reads "POLSIA: 1.2M -> 100K", and beneath it a second ticker
  reads "270M TX / DAY 100K RUNS". Purple + teal palette, grid floor,
  editorial isometric style, 1:1 aspect, no real human faces, text sharp
  at 200px thumbnail.
image: images/26-08-08-0613-01-sapiom-35m-series-a-agent-model-router-anthropic-invests.png
---

# Sapiom $35M Series A: model router สำหรับ agent ที่ตัดบิล Anthropic ของลูกค้าลง 10 เท่า — และ Anthropic คือคนใส่เงิน

## TL;DR
- **5 ส.ค.** — Sapiom ปิด **$35M Series A** นำโดย Dragonfly (Haseeb Qureshi) ตามหลัง $15M seed ของ Accel เมื่อต้นปี — total funding **$50M ใน 11 เดือน** นับจากก่อตั้ง. **Anthropic ร่วมลง**ใน round นี้ด้วย พร้อม Menlo, Coinbase Ventures, Gradient, VanEck
- **ตัวเลขที่ CFO จะสะดุด** — Sapiom Router ตัดบิล agent ของลูกค้า **Polsia จาก $1.2M/เดือน (Anthropic)** เหลือ **~$100K/เดือน** โดย route แต่ละ call ไปที่ model ที่ราคา/ประสิทธิภาพเหมาะสม (Flash / Mid / Pro / Opus / Max) แทนที่จะยิง Opus ทุกครั้ง — ประหยัดประมาณ 10x
- **Scale จริง** — 6 เดือนหลัง launch: **270M+ transactions**, **100K+ agent runs/วัน**, ship product 3 ตัวพร้อมกัน (Router / Agent Studio / Runtime)
- **มุม Agent Platform** — Anthropic ลงเงินใน layer ที่ตัดรายได้ตัวเอง = ยอมรับว่า **model diversity layer** จะเป็นค่า default ในการ deploy agent ระดับ production — และอยากอยู่ในโต๊ะเจรจา ไม่ใช่โดน commoditize จากด้านล่าง

## เกิดอะไรขึ้น

วันอังคารที่ 5 สิงหาคม Sapiom — startup 11 เดือนที่สร้าง infrastructure สำหรับ deploy AI agent — ประกาศ **$35M Series A** นำโดย Dragonfly ผ่าน Haseeb Qureshi ซึ่ง lead deal นี้เอง. Round นี้มาต่อจาก $15M seed ที่ Accel นำเมื่อ 6 เดือนก่อน → **total funding $50M** และ investor list ที่บอกจุดยืน: **Anthropic**, Coinbase Ventures, Menlo, Gradient, Okta Ventures, VanEck Ventures, Operator Collective, Formus Capital, Array Ventures. คู่กับ round Sapiom launch 3 ผลิตภัณฑ์พร้อมกัน — **Sapiom Router** (คัดเลือก model ต่อ call), **Sapiom Agent Studio** (build agent), **Sapiom Runtime** (deploy + observe)

เคสที่ Sapiom โยนใส่ deck คือลูกค้าชื่อ **Polsia** — AI agent company ที่บิล Anthropic เดิม $1.2M/เดือน. หลัง route ผ่าน Sapiom Router — ที่กระจายทุก call ไปยัง Claude Haiku / Claude Sonnet / GPT-5.4 Flash / Gemini 3 Flash / โมเดล open-weight (Llama, Qwen) ตาม profile task — บิลลดเหลือ **~$100K/เดือน**, ประหยัด ~10x โดยที่ output quality ผ่าน SLA เดิม. ในระดับ platform: 6 เดือนหลัง launch Sapiom process **270M+ transactions** และ powers **100K+ agent runs/วัน** — เป็น scale ที่ enterprise team ยากที่จะ replicate เองด้วย eval framework in-house

**Twist ที่น่าสนใจ = Anthropic ลงเงินในบริษัทที่งานประจำวันคือ route call ออกจาก Anthropic**. อ่านตรง ๆ = ขัดกันเอง; อ่านลึก = Anthropic ยอมรับว่า **สงคราม model จะจบที่ multi-model deployment** (แบบ Claude Sonnet สำหรับ reasoning, Haiku สำหรับ tool call, GPT-5.4 สำหรับ code, Gemini Flash สำหรับ classification) และอยากอยู่ในโต๊ะที่กำหนด routing policy — ไม่ใช่โดน orchestrator commoditize จาก outside. คล้ายกับที่ Cloudflare ลงใน AI infra startup แล้วดึงมาอยู่ Workers — เป็น "**own the pipe, don't fight it**"

## ทำไมสำคัญ

**Cost = แผลใหญ่ที่สุดของ agent ใน production ปี 2026.** เมื่อ agentic workflow ทำงานหลาย turn (retrieve → reason → tool call → verify → act) ต่อ 1 user task, cost/task ต่าง 5-20x จาก chat interaction เดิม — ทีม finance ที่เพิ่งอนุมัติ pilot Q1 กำลังเห็น bill Q3 เริ่มไม่ปกติ. Polsia ที่บิล $14.4M/ปี → $1.2M/ปี ไม่ใช่ตัวเลขที่ CFO ขอ optimize ธรรมดา — เป็น **survival math**. Sapiom pitch = แก้ที่ layer routing ไม่ใช่ที่ prompt / eval / caching — vertical ที่ Portkey (2024), Requesty, Not Diamond, และ LangChain (LangSmith router) แข่งอยู่ แต่ยังไม่มีใครมี scale + investor set แบบนี้

**Investor mix บ่งชี้ 2 pattern**: (1) **Model lab (Anthropic) + payment infra (Coinbase Ventures) + identity (Okta) + crypto liquidity (VanEck) + operator VC (Menlo, Gradient)** — คือชุด backer สำหรับ "**agent economy backbone**" ไม่ใช่ SaaS ธรรมดา. (2) Dragonfly ที่เป็น crypto-native VC lead deal = signal ว่า Sapiom กำลังจะ integrate กับ agent-native payment (x402, USDC settlement) ที่ Cloudflare + Stripe ปล่อยเมื่อสัปดาห์ที่แล้ว — Router อาจ evolve เป็น "routing + settlement" layer ที่จ่ายให้ผู้ให้บริการ model ตาม usage โดยไม่ผ่าน invoice

**Loser ที่ต้องระวัง**: (a) **standalone LLM gateway** ที่ขายเป็น dev tool (Portkey class) — เพราะ Sapiom เข้าถึงระดับ agent runtime + eval + routing ครบวงจร, (b) **model lab ที่ไม่มี tier ครบ** — ถ้าคุณเป็น Cohere / Mistral / xAI ที่มีแค่ 1-2 tier, Router จะเลือก competitor เร็วกว่าที่ user รู้ตัว, (c) **enterprise SI ที่ขาย FinOps ทั่วไป** — Sapiom Router คือ FinOps ที่ specialize สำหรับ AI ที่ SI ไม่มี IP มาสู้

## มุม AI Agent Platform

**สำหรับ builders:** ถ้าคุณกำลัง build agent framework (LangGraph, Mastra, CrewAI, custom orchestrator) — **model routing ต้องเป็น first-class primitive ภายในสิ้นปี**, ไม่ใช่ config file. Interface ที่ Sapiom เดินคือ agent เรียก `sapiom.complete(task, profile="reasoning")` แล้ว Router เลือก model ที่ meet SLA — เปลี่ยนสัญญาจาก "**เลือก model แล้วเสีย SLA เอง**" → "**เลือก SLA + policy แล้ว Router รับผิดชอบ model choice**". Framework ที่ยัง lock-in ที่ model เดียว จะสูญเสีย user ที่ hit bill ครั้งแรก. Startup ที่ pitch "agent memory / agent observability / agent evals" ต้องเช็คว่า data model ของตัวเองรองรับ routing metadata (which model → which turn → which cost bucket) หรือยัง

**สำหรับ users/business:** Enterprise ที่ deploy agent — **CFO + head of AI ต้องคุยกันเรื่อง routing policy Q3-Q4 2026** ก่อน bill Anthropic/OpenAI ทะลุ budget. Checklist: (1) มี **tier map** ของ task ที่ agent ทำ (classification/routing = Flash; reasoning/planning = Pro/Opus; code = Codex/Claude Code) หรือยัง? (2) มี **eval baseline** ที่ยืนยันว่า downgrade model แล้วผลไม่แย่ลงหรือไม่? (3) มี **fallback policy** ตอน cheaper model fail — retry ด้วย premium หรือ escalate ไป human? (4) นำ **cost/task metric** เข้าไปใน agent SLA เดียวกับ latency + accuracy หรือยัง? สำหรับ **Thai enterprise (K-Bank, SCB, PTT, True, AIS)** ที่ pilot agent อยู่ — พิจารณา Sapiom / Portkey / Not Diamond เป็น procurement item ก่อน production. Cost per query ที่แตกต่าง 10x คือความต่างระหว่าง pilot ที่ scale ได้ vs. pilot ที่โดน finance kill ที่ Q1 next year

**สำหรับ ecosystem:** **Winner:** multi-model orchestrator (Sapiom, Portkey, Not Diamond), model lab ที่มี Flash tier ราคาถูก + quality สูง (Google Gemini Flash 3, Anthropic Haiku 4.5, DeepSeek), open-weight ecosystem (Llama, Qwen ที่ deploy บน dedicated inference). **Loser:** ผู้ให้บริการ single-model API premium-only (บาง niche startup ที่ขาย 1 vertical LLM ไม่มี tier ราคา), FinOps SaaS ทั่วไปที่ไม่ specialize AI. **Enabridge angle:** ตำแหน่งที่ Thai integrator ควรเล่นคือ **"Model FinOps advisor"** — ช่วย Thai enterprise สร้าง tier map + eval baseline + routing policy สำหรับ agent deployment ในภาษาไทย/ภูมิภาค. เป็น niche ที่ SI ระดับโลกยังไม่ vertical เพราะ Thai token cost profile (Thai NLP ความยาวสูงกว่า English 1.5-2x, ทำให้ cost/task พองยิ่งขึ้น) ต่างจาก benchmark ของ Sapiom ที่วัดบน English workflow

## Sources
- [Sapiom Raises $35 Million Series A to Power the Next Trillion AI Agents — Business Wire](https://www.streetinsider.com/Business+Wire/Sapiom+Raises+$35+Million+Series+A+to+Power+the+Next+Trillion+AI+Agents/26872698.html)
- [Sapiom raises $35M Series A to route AI agents to cheaper models — AI Weekly](https://aiweekly.co/alerts/sapiom-raises-35m-series-a-to-route-ai-agents-to-cheaper-models)
- [Sapiom raises $35M to cut AI agent running costs — TNW](https://thenextweb.com/news/sapiom-35m-series-a-ai-agent-cost-routing)
- [Sapiom Secures $35M to Help Companies Control AI Agent Costs — PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/sapiom-secures-35-million-to-help-companies-control-ai-agent-costs/)
- [Sapiom Raises $35M in Series A Funding — FinSMEs](https://www.finsmes.com/2026/08/sapiom-raises-35m-in-series-a-funding.html)
- [Sapiom Series A blog post — Sapiom](https://www.sapiom.ai/resources/blog/series-a/)

---

## Audio script
วันอังคารที่ 5 สิงหาคม Sapiom startup 11 เดือน สร้าง infrastructure สำหรับ deploy AI agent ปิด Series A 35 ล้านดอลลาร์ นำโดย Dragonfly ตามหลัง 15 ล้านของ Accel เมื่อต้นปี รวม total funding 50 ล้าน. investor list น่าสนใจมาก มี Anthropic ร่วมลง คู่กับ Coinbase Ventures Menlo Gradient Okta Ventures VanEck Ventures.

Sapiom เปิดตัว 3 product พร้อมกัน Router Agent Studio Runtime. เคสที่ pitch คือลูกค้าชื่อ Polsia ที่บิล Anthropic เดิม 1.2 ล้านดอลลาร์ต่อเดือน หลัง route ผ่าน Sapiom Router ที่กระจายทุก call ไปยัง Claude Haiku Sonnet GPT 5.4 Flash Gemini 3 Flash หรือ Llama ตาม profile task บิลลดเหลือประมาณ 1 แสนดอลลาร์ต่อเดือน ประหยัด 10 เท่า. 6 เดือนหลัง launch Sapiom process 270 ล้าน transaction และ powers 100000 agent run ต่อวัน.

Twist ที่น่าสนใจคือ Anthropic ลงเงินในบริษัทที่งานคือ route call ออกจาก Anthropic เอง. อ่านลึกคือ Anthropic ยอมรับว่าสงคราม model จะจบที่ multi model deployment ที่แต่ละ task ใช้ tier ต่างกัน และอยากอยู่ในโต๊ะที่กำหนด routing policy ไม่ใช่โดน orchestrator commoditize จาก outside. คล้ายกับ Cloudflare ลงใน AI infra แล้วดึงมาอยู่ Workers.

Signal สำหรับ enterprise ที่ deploy agent ปี 2026 คือ cost per task ต่าง 5 ถึง 20 เท่าจาก chat interaction เดิม CFO ที่อนุมัติ pilot Q1 กำลังเห็น bill Q3 เริ่มไม่ปกติ. checklist ที่ head of AI ต้องคุยกับ CFO คือมี tier map ของ task ที่ agent ทำหรือยัง มี eval baseline ที่ยืนยันว่า downgrade model แล้วผลไม่แย่ลง มี fallback policy ตอน cheaper model fail. สำหรับ K Bank SCB PTT True AIS ที่ pilot agent อยู่ พิจารณา Sapiom Portkey Not Diamond เป็น procurement item ก่อน production. Thai token ยาวกว่า English 1.5 ถึง 2 เท่า cost per task พองยิ่งกว่า benchmark ของ Sapiom. ตำแหน่งที่ Thai SI ควรเล่นคือ Model FinOps advisor ช่วย enterprise สร้าง tier map และ routing policy ในภาษาไทย.
