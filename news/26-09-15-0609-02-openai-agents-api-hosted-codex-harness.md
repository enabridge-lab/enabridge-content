---
date: 2026-09-14
slug: openai-agents-api-hosted-codex-harness
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A cutaway diagram illustration of a black datacenter rack labeled
  "HOSTED CODEX HARNESS" — inside, a glowing blueprint shows five stacked
  layers: "SESSIONS", "SANDBOXES", "TOOLS", "CONTEXT COMPACTION",
  "MULTI-AGENT". Outside the rack, a small developer silhouette holds a
  single glowing key labeled "1 API CALL" that plugs into the top. Above,
  a countdown card reads "HOURS -> DAYS" and a badge "SEP 10". Editorial
  isometric style, deep charcoal background with mint-green highlights,
  1:1 aspect, no real human faces.
image: images/26-09-15-0609-02-openai-agents-api-hosted-codex-harness.png
---

# OpenAI เปิด Agents API ให้ทุกคน — hosted Codex harness เป็น product แล้ว

## TL;DR
- OpenAI เปิด **Agents API** สาธารณะ 10 ก.ย. — เอา harness ตัวเดียวที่รัน Codex CLI + ChatGPT for Work มาเปิดให้ทุก dev เรียกได้
- Managed service ครบ: **sessions, sandboxes, tool execution, context compaction, multi-agent coordination** — dev ไม่ต้อง build infra เอง
- Pricing: **API เรียกฟรี** — จ่ายเฉพาะ model tokens + tool + sandbox container rates; **Data Agent for ChatGPT Work** ต่อเข้า Snowflake / BigQuery / Redshift / Databricks / ClickHouse / MongoDB / Datadog

## เกิดอะไรขึ้น

10 กันยา OpenAI ทำสิ่งที่ทั้งวงการรอมาสองปี — เปิด **Agents API** เป็น managed service สาธารณะ. Agents API ไม่ใช่ SDK ให้ dev เอาไป wrap เอง เหมือน Assistants API เวอร์ชั่น 2024 อีกต่อไป — เป็น **hosted harness** ที่รัน Codex CLI + ChatGPT for Work อยู่ข้างใน. dev เรียกครั้งเดียว แล้ว OpenAI ดูแล session ที่รันเป็นชั่วโมง เป็นวัน sandbox ที่แยก tool call ไม่ให้ agent เดินผิดที่ context compaction ที่ยัดประวัติเก่าเข้า model ให้ไม่ลืม และ multi-agent coordination ที่ route งานข้าม sub-agent.

Pricing model น่าสนใจไม่แพ้ตัว product — **API เองไม่คิดเงิน**, dev จ่ายเฉพาะ token ของ model ที่เลือก + tool rate ปกติ + container rate ของ sandbox OpenAI-hosted. หมายความว่า OpenAI ยอมให้ orchestration layer เป็น commodity เพื่อรักษา demand ของ model + tool + compute — เกม vertical value capture ที่ AWS ใช้กับ Lambda มาก่อน.

พร้อมกัน **Data Agent for ChatGPT Work** — agent ที่ต่อ Snowflake, BigQuery, Redshift, Databricks, ClickHouse, MongoDB, Datadog และอ่าน Power BI/Tableau/Sigma dashboard ที่มีอยู่แล้ว. business user ถามภาษาธรรมชาติ agent จะตอบ, สืบว่าทำไม metric ขยับ, และ build dashboard interactive พร้อม approval workflow ให้. DEV Community เรียก move นี้ว่า **"OpenAI Just Made the Harness a Product"** — คำอธิบายที่ตรงที่สุด.

## ทำไมสำคัญ

ตลาด agent framework ครึ่งปีที่ผ่านมามีสอง layer ที่ทับกัน — model layer (Claude, GPT, Gemini, Kimi) กับ orchestration layer (LangGraph, LlamaIndex, CrewAI, AutoGen, Mastra, Google ADK). Startup orchestration ทุกเจ้าโฆษณาว่า "เราจัดการ session/memory/durable execution ให้คุณ" — ตอนนี้ OpenAI บอกตลาดว่า **layer นี้ถูก hosted โดยเจ้าของ model ไปฟรี ๆ**. ค่าที่ startup orchestration เคยเก็บได้ต้องเปลี่ยนไปวาง value ที่ไหน?

Signal ตามมา — **framework ที่ตัดสินใจไม่ผูก vendor** (LangGraph, Mastra) ยังมีที่อยู่ในตลาด เพราะ multi-cloud/multi-model deployment; framework ที่ไม่ตัดสินใจ (พยายามเป็น universal wrapper ที่ทำได้ทุกอย่าง) โดน squeeze จาก OpenAI harness บน. Enterprise ที่ยัง POC agent อยู่ต้อง reassess build vs buy ใหม่ — "build ตัว orchestration เอง" ราคาต่ำลงมากหลังจากมี hosted harness. Cellcog เรียก positioning นี้ตรง ๆ ว่า "OpenAI's Agents API Is Really a Hosted Codex Harness" — สังเกตว่า Codex team ที่ build harness ภายในกลายเป็นเจ้าของ SKU ใหม่ของบริษัท ไม่ใช่ product/ChatGPT team.

## มุม AI Agent Platform

**Builders** ที่กำลังสร้าง orchestration framework — จังหวะเปลี่ยน positioning: ถ้าคุณเป็น LangChain/CrewAI-style wrapper คุณโดน commoditize; ถ้าคุณเป็น deterministic graph runtime (LangGraph, Mastra, Google ADK) ที่ deploy อยู่บน infra ลูกค้าเอง คุณยังมีที่อยู่. **Users / business** — Agents API + Data Agent เป็นเครื่องมือที่ทำให้ทีมภายในลด "vibe-code POC" 2 เดือนเหลือหนึ่งสัปดาห์; แต่ระวังหนึ่ง — lock-in ระดับ orchestration + observability + tool sandbox ที่ OpenAI hosted ไว้; migration cost ในสองปีจะสูงมาก. **Ecosystem** — observability vendor (Arize, LangSmith, Braintrust, Fiddler) ต้องรีบ integrate กับ Agents API telemetry ไม่งั้นเสี่ยงโดน replace ด้วย OpenAI-native tracing; database ที่ยังไม่มี connector สำหรับ Data Agent (Snowflake/BigQuery/Redshift/Databricks/ClickHouse/MongoDB/Datadog อยู่ list, ที่เหลือ Elastic/Presto/Trino/Redis/Neo4j ยัง — เป็น queue ต่อไป).

สำหรับทีมไทย — Data Agent เปิดโอกาสให้ analyst ใน enterprise (banking, telco, retail) ทำ ad-hoc analysis ผ่านภาษาธรรมชาติกับ Snowflake/BigQuery ที่บริษัทมีอยู่ — POC ที่ทำได้ใน 2 สัปดาห์ ไม่ใช่ 2 quarter. แต่ prerequisite คือต้อง cleanup schema + governance ให้ query-ready ก่อน — งานที่ Data team ต้องทำก่อน AI team จะได้ประโยชน์.

## Sources
- [OpenAI Just Opened Its Agents API to Everyone: What It Actually Changes for Developers](https://dev.to/thefluxread/openai-just-opened-its-agents-api-to-everyone-what-it-actually-changes-for-developers-3j1j)
- [The Agents API: OpenAI Just Made the Harness a Product](https://cellcog.ai/blog/openai-agents-api/)
- [OpenAI's Agents API Is Really a Hosted Codex Harness](https://agentconn.com/blog/openai-agents-api-hosted-codex-harness/)

---

## Audio script
OpenAI เปิด Agents API ให้ทุก dev ใช้เมื่อ 10 กันยา และเป็น move ที่คนในวงการรอมาสองปีเลยครับ. Agents API ไม่ใช่ SDK ธรรมดา แต่เป็น managed service ที่ host harness ตัวเดียวที่รัน Codex CLI และ ChatGPT for Work อยู่ภายใน. dev เรียกครั้งเดียว OpenAI จัดการให้หมด — session ที่รันเป็นชั่วโมง เป็นวัน sandbox แยก tool call context compaction ที่ยัดประวัติเข้า model ไม่ให้ลืม และ multi-agent coordination ที่ route งานข้าม sub-agent. ที่น่าสนใจคือ API เองไม่คิดเงินครับ — จ่ายแค่ token ของ model tool rate ปกติ กับ container rate ของ sandbox. OpenAI ยอมให้ orchestration layer เป็น commodity เพื่อรักษา demand ของ model tool กับ compute — เกม value capture ที่ AWS ใช้กับ Lambda มาก่อน. พร้อมกัน Data Agent for ChatGPT Work ต่อกับ Snowflake BigQuery Redshift Databricks ClickHouse MongoDB Datadog และอ่าน dashboard Power BI Tableau Sigma ที่มีอยู่แล้ว business user ถามภาษาธรรมชาติ agent ทำ analysis ให้เสร็จพร้อม approval workflow. ผลต่อตลาด — orchestration framework แบบ wrapper ทั่วไปโดน squeeze; framework ที่ deploy บน infra ลูกค้าอย่าง LangGraph Mastra Google ADK ยังมีที่อยู่. Enterprise ต้อง reassess build vs buy ใหม่ — build ตัว orchestration เองราคาต่ำลงมากแล้ว แต่ระวัง lock-in ระดับ orchestration observability tool sandbox ที่ OpenAI hosted. สำหรับทีมไทย โอกาสคือ Data Agent ทำให้ analyst ใน bank telco retail ทำ ad-hoc analysis ผ่านภาษาธรรมชาติกับ Snowflake BigQuery ที่บริษัทมีอยู่ POC ที่เดิมใช้ 2 quarter ตอนนี้เหลือ 2 สัปดาห์ ถ้า data team cleanup schema กับ governance พร้อม
