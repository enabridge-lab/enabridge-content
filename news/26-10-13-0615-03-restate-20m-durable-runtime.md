---
date: 2026-10-12
slug: restate-20m-durable-runtime
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration: a translucent pipeline of agent steps carved into a
  concrete foundation, each step a glowing capsule connected by cables that
  survive a bolt of lightning striking the top; one capsule is cracked but
  the data flow continues through a saved checkpoint. Numbers "$20M", "27M
  TOTAL", "DURABLE" stacked large for thumbnail legibility. Deep navy +
  electric amber palette, flat isometric style, 1:1 aspect, no real human
  faces. Metaphor: agents that survive crashes.
image: images/26-10-13-0615-03-restate-20m-durable-runtime.png
---

# Restate ปิด $20M Series A — ท้า Temporal ($550M @ $12.55B) ว่า durable runtime คือ bottleneck ของยุค agent

## TL;DR
- **30 ก.ย.** **Restate** (Berlin) ปิด Series A **$20M** นำโดย **Singular** + Redpoint Ventures + Capital One Ventures — total funding $27M
- Product: **durable workflow runtime** ที่รัน multi-step agent process ผ่าน crash + network interruption โดยไม่สูญ state
- Co-founder: **Stephan Ewen** — Apache Flink creator (stream processing standard ของ Big Data era ที่แล้ว)
- ลูกค้าเปิดเผย: **Replit + Fortune 500 financial services** — ปิด deal 6-7 figure หลายรายในไตรมาสล่าสุด
- Context: Restate ชน Temporal ตรง ๆ (Temporal ปิด $550M Series E @ **$12.55B** วันที่ 14 ก.ย., ARR $250M+, growth 200%+ YoY, 4,300+ paying customer รวม OpenAI, Snap, Nvidia, Netflix, JPMorgan)

## เกิดอะไรขึ้น

วันที่ 30 ก.ย. Restate ประกาศ Series A $20M จาก Berlin — รอบนำโดย Singular กับ Redpoint Ventures + Capital One Ventures ร่วม; รวม total funding $27M. Product core คือ **durable workflow runtime** — ตัว execution layer ที่ save state ของ workflow ทุกขั้น เพื่อว่าเมื่อ server crash, network drop, หรือ external service ไม่ตอบ, agent สามารถ resume จากจุดเดิมได้ไม่ต้อง restart

Pitch ของ Restate เรียบง่ายและเกินจริงไม่ได้: **AI agent ที่รัน multi-step process (เช่น order fulfillment agent ที่คุย 5 service, update 3 database, ส่ง email 2 ครั้ง) ต้อง durable layer** — ไม่งั้น error 10% ที่จุดใดจุดหนึ่ง = restart ทั้ง workflow + ทำซ้ำการ side effect (double charging, duplicate email). ปัญหานี้แก้ด้วย exactly-once semantics + replayable journal — เทคโนโลยีที่ Stephan Ewen เคยสร้างใน Apache Flink สำหรับ stream processing ยุค 2015

ลูกค้าที่เปิดเผยชัด: **Replit** (code agent platform ที่ลูกค้า run millions of agent sessions daily) + Fortune 500 financial-services firm ที่ไม่เปิดเผยชื่อ. Restate อ้างว่าปิด deal 6-7 figure หลายรายในไตรมาสล่าสุด — ตัวเลขที่ VC ยอมใส่ $20M ที่ Series A แม้ Temporal จะเป็น incumbent ขนาดใหญ่

การ raise ครั้งนี้ **มาหลัง Temporal ปิด Series E $550M ที่ valuation $12.55B 2 สัปดาห์ก่อนหน้า** (14 ก.ย., co-led by Lightspeed + Wellington + Goldman Growth Equity + Tiger Global). Temporal รายงาน ARR $250M+ growth 200% YoY และ 4,300+ paying customer รวม OpenAI, Snap, Nvidia, Netflix, JPMorgan Chase. Platform ประมวล 1.9 trillion actions ใน August 2026 — เลขที่ Restate ต้องวิ่งไล่ 1-2 ปี

Use of funds ของ Restate: product development + U.S. expansion + commercial hub ที่ SF — การ move จาก Berlin สู่ Bay Area signal ชัดว่า target market คือ US enterprise ไม่ใช่ EU first

## ทำไมสำคัญ

**Durable execution เป็น infrastructure primitive ที่หายไปจากคำสนทนา AI agent ปี 2024-2025** — ทุกคนพูดเรื่อง model, framework, protocol (MCP, A2A, PAP, PACT); น้อยคนพูดเรื่อง runtime ที่ยอมให้ agent รันหลายชั่วโมง-หลายวันโดยไม่เสียงาน. ปี 2026 Temporal + Restate กำลังเปลี่ยน narrative — **ไม่มี durable layer = ไม่มี production agent**

Point of view: **Temporal ชนะ enterprise ขนาดใหญ่, Restate มีโอกาสชนะ mid-market + developer-first**. Temporal ประวัติศาสตร์มาจาก Uber (Cadence project) + Google SRE pattern — pricing + onboarding complex, deploy เหมาะกับทีมที่มี 20+ engineer dedicated to infra. Restate ขายตัวเองเป็น **"Temporal ที่ developer คนเดียวต่อใช้ได้"** — SDK ที่ embed ใน TypeScript / Python / Rust โดยตรง, deployment profile เล็กกว่า. Pattern เหมือน Supabase vs AWS RDS ยุค 2020

ที่น่าสังเกตคือ **Capital One Ventures** เข้าร่วม — ธนาคาร Fortune 500 ที่ regulate หนัก; การใส่เงินผ่าน strategic arm = signal ว่า financial services vertical ตัดสินใจแล้วว่า durable workflow เป็น critical infrastructure. Pattern คล้าย AWS Lambda ยุค 2016 ที่ bank เริ่ม adopt เมื่อ exactly-once semantics ชัด — ปี 2026-2027 agent production deployment ของ bank จะ force vendor consolidation ที่ประเด็นเดียวกัน

Signal ที่ยังไม่สรุป: ตลาด durable execution มีขนาดเท่าไรจริง. Temporal + Restate + AWS Step Functions + Cloudflare Durable Objects + Inngest + Hatchet + Trigger.dev + Mastra + Convex — ทุกเจ้าแย่ง developer attention. ภายใน 24 เดือน ตลาดจะ consolidate เป็น 3 ค่าย: **(1) hyperscaler primitive** (AWS Step Functions, Google Workflows), **(2) specialized enterprise** (Temporal), **(3) developer-first SDK** (Restate / Inngest / Trigger.dev). Startup ที่ไม่ชัด position ใน 1 ใน 3 บัตร = เสี่ยง

## มุม AI Agent Platform

**Builders:** ถ้าคุณสร้าง agent framework (LangGraph, Mastra, CrewAI, AutoGen) — **ควร integrate กับ durable runtime vendor อย่างน้อย 2 เจ้า** (Temporal + Restate เป็น minimum) ภายใน 6 เดือน; มิฉะนั้นลูกค้า enterprise จะต้องเขียน glue code เอง + production migration ยากขึ้น. Pattern ที่เห็นจาก Replit (ใช้ Restate) และ OpenAI (ใช้ Temporal) คือ **framework ที่ bundled durable execution ชนะ enterprise RFP** รอบ 2027

**Users / business:** CTO/VP Eng ที่ scale AI agent สู่ production — ถ้าใช้ async workflow ที่รัน > 5 นาที, มี > 3 external service call, หรือ handle financial transaction = **durable execution ไม่ optional**. POC ทั้ง Temporal (ถ้าทีม > 20 engineer) + Restate (ถ้าทีม 5-20 engineer) ภายใน Q4 2026 เลือกตาม **cost per workflow + onboarding complexity + SDK language fit**. บริษัทไทยที่พึ่ง fintech / insurance workflow — Capital One Ventures ลงใน Restate เป็น signal ชัดสำหรับ compliance-sensitive context

**Ecosystem:** AWS + Google Cloud + Azure กำลังจะเจอ pressure สูงสุด — Step Functions, Workflows, Durable Functions ยังไม่ competitive สำหรับ agent-specific use case. hyperscaler จะต้องตัดสินใจระหว่าง (ก) acquire specialized vendor (เป็น rumor ว่า AWS จะ acquire Temporal, Google เล็ง Mastra) หรือ (ข) rewrite primitive ของตัวเอง. Inngest + Trigger.dev + Hatchet + Mastra ที่ไม่ตัดสินใจชัดเจน position ภายใน 12 เดือน = เสี่ยง squeeze

## Sources
- [TechCrunch — Restate lands $20M as the need for durable infrastructure increases with AI agents](https://techcrunch.com/2026/09/30/restate-lands-20m-as-the-need-for-durable-infrastructure-increases-with-ai-agents/)
- [AI Weekly — Restate Raises $20M Series A for Durable AI Agent Runtime](https://aiweekly.co/alerts/restate-raises-20m-series-a-for-durable-ai-agent-runtime)
- [Dealroom — Restate raises $20M to build durability into AI agent infrastructure](https://dealroom.co/news/157982-restate-raises-20m-to-build-durability-into-ai-agent-infrastructure/)
- [n8nlab — Why AI Agents Need Durable Execution: Restate Raises $20M](https://n8nlab.io/news/restate-durable-execution-ai-agents)
- [Pulse2 — Temporal Raises $550 Million Series E At $12.55 Billion Valuation](https://pulse2.com/temporal-raises-550-million-series-e-at-12-55-billion-valuation/)

---

## Audio script
สัปดาห์ที่แล้ว Restate บริษัทจาก Berlin ปิด Series A สองล้านดอลลาร์. นำโดย Singular กับ Redpoint. Capital One Ventures เข้าร่วม. ตัวเลขไม่ใหญ่เท่า deal อื่นในสัปดาห์. แต่ story สำคัญกว่าตัวเลข

Restate ขาย durable workflow runtime. คือ layer ที่ save state ของ agent process ทุกขั้น. เมื่อ server crash หรือ network drop. agent resume จากจุดเดิมได้ไม่ต้อง restart. co-founder Stephan Ewen คือคนสร้าง Apache Flink. stream processing standard ยุค Big Data

ที่น่าสนใจคือ Restate ชน Temporal ตรง ๆ. Temporal เพิ่งปิด Series E ห้าร้อยห้าสิบล้านดอลลาร์ สองสัปดาห์ก่อน valuation สิบสองพันห้าร้อยห้าสิบล้าน. ARR สองร้อยห้าสิบล้าน. 4,300 paying customer รวม OpenAI, Snap, Nvidia, Netflix, JPMorgan. Restate มีลูกค้า Replit กับ Fortune 500 financial services ที่ไม่เปิดเผย. ขนาดเล็กกว่าชัด

แต่สำคัญคือ Restate กำลัง position ว่าเป็น Temporal ที่ developer คนเดียวต่อใช้ได้. SDK embed ใน TypeScript, Python, Rust โดยตรง. ต่างจาก Temporal ที่ต้องการทีม infra 20+ engineer

สิ่งที่ founder ไทยต้องเข้าใจคือ. ถ้าคุณสร้าง agent ที่รันหลายนาที หลายชั่วโมง หลาย external service call หรือ handle เงิน. durable execution ไม่ optional. ไม่งั้น error 10% ที่จุดใดจุดหนึ่งเท่ากับ restart ทั้ง workflow + ทำซ้ำ side effect. ลูกค้าโกรธ compliance หัก

Point of view ของผม. ตลาด durable execution จะ consolidate เป็นสามค่ายใน 24 เดือน. hyperscaler primitive, specialized enterprise, developer-first SDK. Temporal อยู่ค่ายสอง. Restate อยู่ค่ายสาม. บริษัท infrastructure ที่ไม่ชัดเจน position = เสี่ยง squeeze

สำหรับ Enabridge. ถ้าสร้าง agent framework หรือ platform — ควร integrate durable runtime อย่างน้อย 2 เจ้าภายใน 6 เดือน. ลูกค้า enterprise จะไม่ยอมเขียน glue code เอง. ลูกค้า fintech ไทยควรดูที่ Restate ก่อน. เพราะ Capital One Ventures ลงเงิน = signal ของ compliance-sensitive context
