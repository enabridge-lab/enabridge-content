---
date: 2026-09-30
slug: restate-20m-durable-agent-runtime
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: |
  Editorial isometric illustration of a thick glowing pipeline labeled
  "DURABLE RUNTIME" running beneath a floor of brittle glass; above the
  glass, small agent orbs stumble and freeze mid-step as crash cracks spread
  across the glass, but each one is caught by the pipeline below and
  continued. Floating bold cards: "$20M SERIES A", "SURVIVES CRASH",
  "REPLIT AGENT INSIDE". Deep indigo and neon-green cinematic palette, high
  contrast tuned for 200px thumbnails, bold text rendering, no real human
  faces, 1:1 aspect.
image: images/26-10-02-0615-04-restate-20m-durable-agent-runtime.png
---

# Restate ระดม $20M Series A — "agents need an OS layer" กลายเป็น thesis ของ VC จริงจัง, Replit Agent รัน durable orchestration อยู่บนนี้

## TL;DR
- 30 ก.ย. Restate (Berlin, founded 2022) ประกาศ **Series A $20M** นำโดย Singular + Redpoint Ventures + Capital One Ventures
- ขาย **durable workflow runtime** — engine ให้ multistep process ของ agent รอด crash + network interruption ได้ (retry, state, recovery เขียนในระดับ framework ไม่ใช่โค้ด app)
- Prominent deployment: **Replit Agent** ใช้ Restate orchestrate agent calls แทนที่จะเขียน retry logic เอง; ปัจจุบันมี "hundreds of companies" รวม AI startup + Fortune 500 ใช้

## เกิดอะไรขึ้น
วันอังคารที่ 30 กันยายน Restate — startup Berlin ก่อตั้งปี 2022 — ประกาศปิด Series A ที่ **$20 ล้าน** นำโดย Singular และมี Redpoint Ventures + Capital One Ventures ร่วม. Product ของ Restate คือ "durable workflow runtime" — engine ที่ให้ multistep business process (เช่น agent ที่ต้องทำงาน 15 step ติดกัน) **รอด crash และ network interruption** ได้ โดย retry logic, state persistence, exactly-once semantics ถูก handle ที่ชั้น runtime — developer เขียนโค้ด application level ไม่ต้องเขียน try-except ซ้อนไปซ้อนมา.

Pitch ของ Restate ตรง: "AI agents need this infrastructure underneath them". Agent framework ยุคแรก (LangChain, CrewAI, AutoGen) จัดการ retry ที่ชั้น library ด้วย decorator — ซึ่ง fail เมื่อ pod crash, container restart, หรือ provider API timeout. Production agent ที่รัน 24/7 fail ทุก 10 นาที ถ้าไม่มี durable layer. Restate ทำสิ่งนี้ให้ โดย expose API เหมือน Temporal/Inngest แต่ปรับแต่งโฟกัส agent workload — single workflow step อาจเป็น LLM call ที่กินเวลา 60 วินาที, retry policy ต้องเข้าใจ rate limit และ fallback model.

Deployment ที่โชว์: **Replit Agent** — flagship coding agent ของ Replit ที่ใช้ user หลายล้านคน — รัน durable orchestration บน Restate. ก่อนหน้านี้ Replit เขียน retry/state logic เอง, หลัง migrate มา Restate ลด latency ของ recovery เหลือเสี้ยวและ reduce engineering overhead. Restate บอกว่า **"hundreds of companies"** ใช้ product ตอนนี้ รวม AI startup และ Fortune 500 organization.

## ทำไมสำคัญ
"Agents need an OS" เริ่มกลายเป็น **thesis ของ VC** ไม่ใช่ meme ของ Twitter. ภายใน 12 เดือนที่ผ่านมา: Temporal ระดม Series C ขนาด $100M+ (bulk of workload ย้ายมา agent), Inngest ปิด Series B, DBOS (จาก Michael Stonebraker) ปิด seed, Trigger.dev ขยาย enterprise, Hatchet.run ปิด Seed+. Restate เลือกตั้ง positioning เฉพาะ: "durable" ก่อน ไม่ใช่ "serverless-first" (Inngest) หรือ "database-native" (DBOS). ที่ Berlin + ยอมรับ early-stage challenge ของตลาด Europe = **ครอง enterprise GDPR + sovereign cloud** ซึ่งเป็นสนามที่ US-based runtime เข้าได้ยากกว่า.

Pattern ของ "operating layer ของ enterprise agent" ตกผลึกชัดในปลาย ก.ย. — ต้น ต.ค. 2026. ภายใน 72 ชั่วโมง: Nvidia OpenShell (28), Docusign MCP GA (30), Bloomberg Enterprise MCP (29), Restate (30), Classie Supervise (1), IBM Bob self-hosted (1). ชัดเจนว่า **layer เดียวที่ยังเปิดคือ orchestration/durable runtime** — ที่ VC bet $20M+ เพราะเชื่อว่า agent framework (LangGraph/CrewAI/OpenAI Agent SDK) จะไม่ build durable layer เอง ไปซื้อจาก vendor เป็นหลัก. ถ้า bet ถูก Restate อยู่ตำแหน่ง AWS Lambda ของ pre-serverless era.

Angle ที่คม: round นี้ขนาด $20M ไม่ใหญ่ (compared to Temporal $200M+ ที่ระดมไปแล้ว) — แต่ **composition ของ investor** พูด: Capital One Ventures เข้า = agent deployment ใน regulated financial services ต้องการ durable layer ที่ compliant. ขนาดเล็กไม่ใช่สัญญาณปัญหา — เป็น signal ว่าทีมเลือกเก็บ dilution ไว้ให้ milestone ต่อไป (ปี 2027 น่าจะเห็น Series B $80M+ ถ้า Replit Agent + Fortune 500 scale)

## มุม AI Agent Platform
**Builders** ที่สร้าง agent framework ต้องเลือก — build durable execution layer เองหรือ depend บน Temporal / Restate / DBOS. Decision นี้มี implication ยาว: ถ้า framework ของคุณ bundle durable runtime เอง = engineering overhead +50% แต่ลด dependency; ถ้า depend outside = ship เร็ว แต่ขาย enterprise ต้องผ่าน procurement 2 vendor. Framework ที่น่าจะ bundle: OpenAI Agent SDK, Anthropic Managed Agents (เพราะมี compute อยู่แล้ว). Framework ที่น่าจะ depend: LangGraph, CrewAI (เพราะเน้น developer experience > runtime control). **Users / Business** ก่อน deploy agent ลง production ต้องถาม vendor "มี durable execution ไหม? state checkpoint ตรงไหน? recovery policy เป็นยังไง?" — ถ้าตอบไม่ได้ อย่า deploy. และหลายกรณีคุณเจอว่า vendor ยืม Restate/Temporal อยู่หลังบ้าน ซึ่งหมายความว่าคุณจ่าย premium ให้ layer เดียว 2 รอบ. **Ecosystem** — Temporal, Inngest, DBOS, Trigger.dev ต้อง positioning ให้ชัดว่าเป็น "agent-first" ไม่ใช่ "general workflow". Market จะ bifurcate — AI-native durable runtime vs. workflow general-purpose. ภายใน 18 เดือนน่าจะเห็น consolidation หรือ hyperscaler acquire 1 ตัว

## Sources
- [Restate Raises $20M Series A to Build Durable Infrastructure for AI Agents — Unite.ai](https://www.unite.ai/restate-raises-20m-series-a-to-build-durable-infrastructure-for-ai-agents/)
- [Restate Raises $20M Series A for Durable AI Agent Runtime — AI Weekly](https://aiweekly.co/alerts/restate-raises-20m-series-a-for-durable-ai-agent-runtime)
- [Durable Execution: Restate's Proven, Smart $20M AI Agent Bet — Progressive Robot](https://www.progressiverobot.com/2026/09/30/durable-execution-restate-20m-ai-agents/)

---

## Audio script
ข่าว infrastructure สำหรับ builder วันนี้ครับ. Restate — startup Berlin ก่อตั้งปี 2022 — ประกาศ Series A 20 ล้านดอลลาร์เมื่อวันอังคารที่ 30 กันยายน. Lead investor คือ Singular มี Redpoint Ventures และ Capital One Ventures ร่วม. Product คือ durable workflow runtime — engine ที่ให้ multistep process ของ agent รอด crash และ network interruption ได้. Pitch ตรงมากครับ AI agent ที่รัน production 24 ชั่วโมง fail ทุก 10 นาที ถ้าไม่มี durable layer. Agent framework ยุคแรก LangChain CrewAI AutoGen handle retry ที่ชั้น library ด้วย decorator ซึ่งไม่รอด pod crash หรือ container restart. Restate ทำ handle ที่ชั้น runtime ให้. Deployment ที่โชว์คือ Replit Agent — flagship coding agent ของ Replit ที่มี user หลายล้าน — รัน durable orchestration บน Restate อยู่. Restate บอกตอนนี้มีลูกค้า hundreds of companies รวม AI startup และ Fortune 500. ความสำคัญคือ agents need an OS กำลังกลายเป็น thesis ของ VC จริง ๆ ไม่ใช่ meme Twitter. Temporal ระดม Series C 100 ล้าน Inngest ปิด Series B DBOS จาก Michael Stonebraker ปิด seed. Restate เลือก positioning durable-first ไม่ใช่ serverless. ที่สำคัญคือ Capital One Ventures เข้าร่วม round signal ว่า regulated financial services ต้องการ durable layer ที่ compliant. ถ้าคุณเป็น builder framework ต้องเลือก build durable layer เองหรือ depend บน Temporal Restate. ถ้าคุณเป็น business ก่อน deploy agent ถาม vendor ว่ามี durable execution ไหม recovery policy เป็นยังไง — ถ้าตอบไม่ได้ อย่า deploy. ภายใน 18 เดือนตลาด durable runtime น่าจะ consolidate หรือ hyperscaler acquire ครับ.
