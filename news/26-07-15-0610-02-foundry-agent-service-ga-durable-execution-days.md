---
date: 2026-07-15
slug: foundry-agent-service-ga-durable-execution-days
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial isometric hero illustration of a giant server-hall labeled
  "FOUNDRY AGENT SERVICE" with a huge glowing "GA" seal on the front wall.
  Inside, three assembly-line conveyor belts move labeled boxes marked
  "LANGCHAIN", "CREWAI", "CUSTOM" toward a single hosted-runtime engine
  in the center. In the foreground, a giant hourglass turned on its side,
  labeled "SUSPEND 6h → RESUME", with digital numbers "99.9% SLA" glowing
  above. Below the engine, a thin ribbon reads "VOICE LIVE · PRIVATE NET
  · EVALUATIONS". Bold text readable at 200px thumbnail, high-contrast
  teal-and-amber cinematic palette, 1:1 aspect, no real human faces.
image: images/26-07-15-0610-02-foundry-agent-service-ga-durable-execution-days.png
---

# Microsoft Foundry Agent Service ขึ้น GA — hosted agent ที่รันหลายวัน + framework-agnostic runtime กลายเป็น enterprise default

## TL;DR
- **Foundry Agent Service (hosted agents) ขึ้น GA เดือน ก.ค. 2026** — จบ preview, ได้ **99.9% uptime SLA** + Azure enterprise support; ทีมสามารถ deploy agent เป็น managed compute endpoint ที่ Foundry ดูแล message routing / checkpointing / scaling ให้เอง
- **"Long-running workflow mode"** เป็น differentiator — durable execution layer built-in ที่ ถ้า agent เรียก external API ที่ใช้เวลา **6 ชั่วโมง** ตอบ runtime **suspend + resume ให้อัตโนมัติ** ไม่ต้องเขียน checkpoint / state persistence เอง — solve pain ที่ทำให้ agent production deployment ล้มมากที่สุด
- **Framework-agnostic**: รองรับ **Microsoft Agent Framework, LangChain, CrewAI, custom Python orchestrator** พร้อม **Magentic-One multi-agent orchestration stable**, Voice Live GA สำหรับ real-time voice agents, private networking, enterprise-grade evaluations — ทำให้ Foundry เป็น first cloud runtime ที่ pitch "bring your framework, we run it in production"

## เกิดอะไรขึ้น
Microsoft ประกาศ **Foundry Agent Service hosted agents ขึ้น GA** ต้นเดือน ก.ค. 2026 — 8 เดือนหลังเปิด public preview ที่ Build 2026 (พ.ค.). การขึ้น GA ไม่ใช่เรื่อง feature parity แต่คือ commitment structure: Azure ผูก **99.9% uptime SLA** + standard enterprise support plans, มี compliance certification (SOC 2, HIPAA, ISO 27001, FedRAMP moderate) — enterprise procurement team ที่รอ signal นี้ตัดสินใจซื้อได้แล้ว. Foundry เป็น successor ของ Azure AI Studio + Prompt Flow + AI Foundry (rebrand พ.ย. 2025) ที่ตอนนี้ position เป็น "one-stop agent platform" ของ Microsoft

Feature ที่ทำให้ Foundry differentiate จาก competitor คือ **long-running workflow mode**. Developer deploy agent เป็น managed compute endpoint, Foundry จัดการ message routing, checkpointing, scaling. Durable execution layer built-in — ถ้า agent เรียก external API (ระบบ ERP, third-party approval, batch job) ที่ใช้เวลา 6 ชั่วโมงตอบ runtime จะ **suspend agent state + resume** เมื่อ response กลับมา ไม่ต้อง developer เขียน checkpoint / retry / state persistence เอง. นี่คือ pain ที่ทำให้ agent 90% ตายใน production — เพราะ real workflow ในองค์กร (approval chain, compliance review, ETL, human-in-loop) ไม่จบใน 30 วิ แต่ tool ปัจจุบันไม่มี durable primitive ใน platform layer (LangGraph checkpoint ต้อง code เอง, Temporal ต้อง set up broker แยก)

**Framework-agnostic** เป็น bet เชิงกลยุทธ์. GA announcement ยืนยันว่ารองรับทุก toolchain ที่ containerize ได้ — LangChain, CrewAI, custom Python orchestrator, และ multiple LLM จาก OpenAI, Mistral, Meta. **Magentic-One multi-agent orchestration** ขึ้น stable ใน Microsoft Agent Framework — pattern สำหรับ complex multi-agent system ที่ Microsoft Research พัฒนามา 2 ปี. **Voice Live GA** เปิด real-time voice agent (คู่ตรงข้าม Salesforce Agentforce Voice, OpenAI Realtime API, Google Gemini Live) — เจ้าแรกที่มี durable execution + voice ในตัว. **Toolboxes** (managed tools/skills) + **memory types** (short-term, long-term, semantic) built-in ลด boilerplate

Enterprise features ที่ต้องสังเกต: **private networking** — deploy agent ใน customer VNET ไม่ผ่าน public internet, สำหรับ regulated industry (bank, healthcare, gov). **Enterprise-grade evaluations** — built-in test harness ที่รัน agent กับ dataset ตัวอย่าง + metric (accuracy, latency, cost, hallucination rate). **Governed teams pilot** สำหรับปลายปี — policy layer สำหรับ team-scale agent deployment (permission, budget, audit). ทั้งหมด positioning ว่า Foundry ไม่ใช่ agent framework, เป็น **agent runtime + governance stack**

## ทำไมสำคัญ
Enterprise agent economics เข้าเฟส post-hype ที่ Enabridge track ต่อเนื่อง — Cisco 90K deployment (14 ก.ค.), Salesforce Agentforce ARR $1.2B แต่ <10% scale ผ่าน pilot, Microsoft Dataverse plugin สำหรับ Claude/Cursor/Copilot — **บริษัทที่ deploy จริงเจอ pain เดียวกัน 3 อย่าง**: (1) agent workflow ต้องรันนาน ไม่ใช่ single call, (2) framework selection lock choice ไปทั้ง org, (3) governance ไม่ตามทัน scale. Foundry GA จับ pain #1 กับ #2 พร้อมกัน — durable execution ระบุ pain 1 ตรง, framework-agnostic แก้ pain 2. Pain 3 (governance) Microsoft ยกให้ partner ecosystem (Devenex, Datadog, Portkey)

Signal สำหรับ market: **cloud vendor เข้าเฟส agent runtime commoditization**. AWS Bedrock Agents ตอนนี้มี memory, multi-agent collaboration, code interpretation, guardrails — Google Vertex AI Agent Engine + ADK v1.0 stable + Managed MCP; Microsoft Foundry Agent Service GA + hosted + durable + voice. **Big three offering เท่ากันภายใน 90 วัน** — differentiation shift ไปที่ (1) framework portability (Foundry แข็งที่สุด), (2) durable execution primitive (Foundry ประกาศ 6h suspend, Bedrock ยังไม่มี, Vertex มี background task ใน Managed Agents), (3) ecosystem partner (Google A2A 150+ orgs, Microsoft Partner Center MCP certification 60+ servers, AWS Marketplace)

ที่น่าจับตาระยะกลาง: **agent framework consolidation จะเร่ง**. Standalone framework ที่ไม่ผูก cloud (LangGraph, CrewAI, AutoGen open-source) ยังคงมี market สำหรับ hybrid/on-prem/regulated แต่ managed runtime bet จะไป Foundry / Bedrock / Vertex. Framework vendor ที่รอดต้อง (1) partner กับ hyperscaler runtime, (2) มี unique primitive (LangSmith trace, CrewAI role-based, DSPy declarative), (3) มี open-source community เข้มแข็ง. LangChain Inc. เพิ่ง sign partnership กับ Microsoft ต้นปี — signal ว่ารู้ทิศทาง

## มุม AI Agent Platform
สำหรับ **builders**: ถ้าสร้าง agent framework — จำเป็นต้องมี **Foundry deployment guide + LangChain compat layer** ในเอกสาร มิฉะนั้น enterprise buyer จะ default ไป Microsoft Agent Framework. ถ้าสร้าง durable execution primitive (Temporal, Restate, Inngest) — Foundry announcement ทำให้ pattern เป็น mainstream, สร้าง developer education tailwind แต่ก็ commoditize primitive ของตัวเอง; ต้อง double-down ที่ visibility + debugging + workflow authoring UX ที่ Foundry ยังไม่แข็ง

สำหรับ **users/business** ที่ deploy agent ระดับ enterprise: ถ้าใช้ Azure อยู่แล้ว — Foundry GA คือ signal ให้ move production workload จาก dev/pilot cluster ไป hosted, ลด operational burden. Thai enterprise ที่มี Azure landing zone ควร (1) inventory agent workflow ที่ต้องรันนาน > 5 นาที (approval chain, batch process, ETL pipeline, compliance review), (2) POC Foundry hosted agent กับ workflow เดียวก่อน scale, (3) เจรจา private networking + spend cap ก่อน commit contract. หน่วยงานที่ยังไม่ตัดสินใจ cloud — Foundry GA ทำให้ Microsoft Azure น่าสนใจกว่า pure-play GPU cloud สำหรับ agent workload

สำหรับ **ecosystem**: **Governance layer ได้ tailwind ที่สุด** — Devenex, Datadog LLM Observability, Portkey, Kong AI Gateway, LangSmith, Arize เพิ่งมี GA runtime ที่ต้อง observe. Voice agent vendor (Vapi, Retell, Bland) เจอ competition ตรง Voice Live GA — ต้อง pivot ไป specific use case (outbound sales, medical triage) หรือ multi-language niche. **Framework portability standard** ที่มีอยู่ (MCP tool integration, A2A agent communication) จะกลายเป็น procurement checklist item ในทุก RFP ครึ่งหลังปีนี้ — vendor ที่ไม่ support ทั้งคู่ = ตกรอบ

## Sources
- [Foundry Agent Service is GA: private networking, Voice Live, and enterprise-grade evaluations — Microsoft Foundry Blog](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/)
- [AI Agents That Run for Days: Microsoft Foundry's Managed Hosting Goes Live — Windows News](https://windowsnews.ai/article/ai-agents-that-run-for-days-microsoft-foundrys-managed-hosting-goes-live.436672)
- [Microsoft Foundry Agent Service Is GA: What Developers Need to Know — byteiota](https://byteiota.com/foundry-agent-service-ga/)
- [Hosted agents in Foundry Agent Service — Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents)
- [What's New in Microsoft Foundry | June 2026 — Microsoft Foundry Blog](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/)

---

## Audio script
Microsoft ประกาศ Foundry Agent Service hosted agents ขึ้น GA เดือนกรกฎาคม 2026 นี้ 8 เดือนหลังเปิด public preview ที่ Build. GA มาพร้อม 99 จุด 9 SLA compliance certification เต็มชุด — signal สำหรับ enterprise procurement ที่รอตัดสินใจซื้อ. feature ที่ทำให้ Foundry แตกต่างจาก competitor คือ long running workflow mode ถ้า agent เรียก external API ที่ใช้เวลา 6 ชั่วโมงตอบ runtime จะ suspend agent state แล้ว resume เมื่อ response กลับมา ไม่ต้องเขียน checkpoint หรือ state persistence เอง — solve pain ที่ทำให้ agent 90 เปอร์เซ็นต์ตายใน production เพราะ workflow จริงในองค์กรไม่จบใน 30 วินาที. ที่สำคัญคือ framework agnostic รองรับ LangChain CrewAI custom Python orchestrator และ Microsoft Agent Framework Magentic One multi agent orchestration stable. Voice Live ก็ GA ด้วย เป็นเจ้าแรกที่มี durable execution บวก voice ในตัว. เทียบกับ AWS Bedrock Agents และ Google Vertex AI Agent Engine — big three offering เท่ากันภายใน 90 วัน. Standalone framework LangGraph CrewAI AutoGen ยังมี market สำหรับ hybrid on prem regulated แต่ managed runtime bet จะไป Foundry Bedrock Vertex. สำหรับ Thai enterprise ที่มี Azure landing zone อยู่แล้วควร inventory workflow ที่ต้องรันนานเกิน 5 นาที เช่น approval chain batch process compliance review แล้ว POC Foundry hosted agent ก่อน scale. governance vendor Devenex Datadog Portkey Kong AI Gateway ได้ tailwind ที่สุด เพราะเพิ่งมี GA runtime ที่ต้อง observe
