---
date: 2026-10-15
slug: workday-headless-agent-platform
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  A vast corporate glass tower at dusk with an open side wall revealing hundreds
  of glowing data pipes labeled "HR" and "FINANCE" flowing out to a cluster of
  small robot icons on a plaza outside. Above the tower, big block numbers
  read "275 READ TOOLS" and "54 WRITE TOOLS". A banner across the top reads
  "WORKDAY GOES HEADLESS". Editorial isometric illustration, deep navy and
  gold palette, strong contrast, 1:1 aspect, no real human faces.
image: images/26-10-15-0616-01-workday-headless-agent-platform.png
---

# Workday เปิดฝาข้อมูล HR + Finance ให้ AI agent ของลูกค้าเดินเข้ามาเอง

## TL;DR
- Workday ประกาศ Trusted Agent Platform แบบ headless (13 ต.ค. 2026) — ลูกค้าสร้าง agent ของตัวเองด้วย LangChain / Google ADK / Claude Code / Cursor แล้วเข้าถึง HR + Finance ของ Workday ตรง ๆ ผ่าน MCP (275 read + 54 write/delete tools)
- Model-neutral — รัน Anthropic, Google, Meta, Mistral, OpenAI, NVIDIA Nemotron ก็ได้ ขอให้ผ่าน Agent System Users ที่ผูก OAuth เป็น identity ของ agent ตัวนั้น
- Signal สำคัญ: SaaS ยักษ์ที่คุม system of record ของ enterprise กำลังเปลี่ยนตัวเองจาก "app ที่คนล็อกอิน" เป็น "data layer ที่ agent ของใครก็ได้เสียบใช้"

## เกิดอะไรขึ้น
13 ตุลาคม Workday ออก press release ว่า Trusted Agent Platform เข้าสู่ phase ที่ชื่อ "headless access" — แปลไทยคือ ลูกค้าไม่ต้องใช้ UI ของ Workday ไม่ต้องมีคนล็อกอิน แค่สร้าง agent ของตัวเองแล้วเสียบเข้าไปทำงานใน HR + Finance ได้โดยตรง. Agent Harness, Agent-Ready Tools, Developer Agent, Custom Agents และ Workday Data Cloud ทั้งหมดเข้าสถานะ Generally Available พร้อมกัน

Agent-Ready Tools คือ MCP server ที่ Workday publish ให้ลูกค้าใช้ — ตามรายงานของ The New Stack มี 275 read tools และ 54 write/delete tools ครอบ 2 domain หลักคือ HR และ finance. LangChain support เป็น GA แล้ว, Google ADK ยังอยู่ใน design partner, NVIDIA Nemotron ก็ GA แล้วเหมือนกัน. Developer Agent ทำงานร่วมกับ Claude Code, Codex, และ Cursor ได้ตรง ๆ

จุดสำคัญคือ governance model: agent ทุกตัวต้องผูกกับ "Agent System User" ซึ่งเป็น identity แยกจาก human user แล้วใช้ OAuth client ของตัวเอง. ทุก action ที่ agent ทำจะวิ่งผ่าน permission + audit trail ชุดเดียวกับที่ user ปกติเจอ — ไม่มีทางลัดอ้อม. Workday บอกว่าโมเดลนี้ต่างจาก Salesforce ซึ่ง handle agent identity คนละแบบ

Roadmap ที่ยังไม่ออก: Agent Context Service กับ Grounded Reasoning. The New Stack บอกว่าทั้งคู่ early access ต้นปี 2027, แต่ press release ของ Workday เอง (ที่ Stocktitan สรุป) บอกว่า Context Service จะ early access ปลายปี 2026. วันปล่อยจริงให้รอดูอีกที

## ทำไมสำคัญ
มองในฐานะเจ้าของ system of record ใหญ่ที่สุดในองค์กร — Workday ถือข้อมูลพนักงาน เงินเดือน budget expense ของ Fortune 500 กว่าครึ่งโลก. ก่อนหน้านี้ถ้าอยากให้ agent ของบริษัททำงานกับข้อมูลนี้ ต้องผ่าน UI หรือ API แบบ enterprise ที่ pain มาก. การเปิด MCP server + headless + model-neutral เท่ากับ Workday ประกาศว่า "เราจะไม่พยายามเป็นเจ้าของ agent runtime — เราจะเป็น data layer ที่ agent runtime ของใครก็ได้ต้องมาคุยด้วย"

นี่คือ pattern ที่เริ่มเห็นชัดเจนในปี 2026: SaaS ยักษ์ที่ควบคุม data หยุดสู้สงคราม UI กับ agent builder แล้วย้ายไปอยู่ชั้นล่าง — เป็น trusted data provider ที่คิดเงินตาม query. Databricks ทำ Unity AI Gateway, Atlassian ทำ Agentic Multiplayer Protocol, Google ทำ Gemini Agent ที่ route ไป Claude ได้. ทุกเจ้าตระหนักว่า agent orchestration ยังเป็น commodity war ที่ไม่แน่ว่าจะได้กินยาว แต่ data access control + governance นั้นมี moat ชัด

## มุม AI Agent Platform
- **Builders**: ถ้าคุณสร้าง vertical agent (เช่น compliance agent, hiring agent, finance close agent) คุณจะมี surface area กว้างขึ้นมากในการต่อ enterprise ของจริง — ไม่ต้องรอ Workday เขียน agent ให้ แค่เรียก MCP tool แล้ว deploy. ข้อแลกคือต้องยอม Workday เป็น gatekeeper และราคาต่อ query จะเริ่มเห็น
- **Users / Business**: บริษัทที่ลงทุนใน Workday ไปแล้วหลายสิบล้าน จะได้ ROI รอบใหม่ — agent ของทีมจะเข้าถึงข้อมูล HR/Finance ได้โดยที่ security team ไม่ต้องตื่น เพราะ Agent System User + audit trail วิ่งตามอยู่
- **Ecosystem**: นี่คือ bellwether ของ SaaS wave ต่อไป — ThinkAbout Salesforce, SAP, Oracle NetSuite ซึ่งยังขายวิสัยทัศน์ "agent ของเราเท่านั้น" — ภายในสองไตรมาสน่าจะมี headless เหมือนกัน ไม่งั้นลูกค้าจะหา workaround

## Sources
- [Workday's Trusted Agent Platform Now Delivers Headless Access to HR and Finance](https://newsroom.workday.com/2026-10-13-Workdays-Trusted-Agent-Platform-Now-Delivers-Headless-Access-to-HR-and-Finance,-Letting-Customers-Build-and-Run-Lawful-AI-Agents)
- [Workday goes headless, opening its HR and finance data to outside AI agents — The New Stack](https://thenewstack.io/workday-headless-mcp-agents/)
- [Workday launches headless AI agent platform for HR and finance — Investing.com](https://uk.investing.com/news/stock-market-news/workday-launches-headless-ai-agent-platform-for-hr-and-finance-93CH-4907839)
- [AI agents can now do real work in HR and finance — Stocktitan](https://www.stocktitan.net/news/WDAY/workday-s-trusted-agent-platform-now-delivers-headless-access-to-hr-4bts3bnztze2.html)

---

## Audio script
สวัสดีครับทุกคน วันนี้ Workday ประกาศเรื่องที่น่าจะเปลี่ยน landscape ของ enterprise AI agent ไปอีกรอบ. Workday เปิด Trusted Agent Platform ให้เป็น headless แล้ว แปลง่าย ๆ คือ ลูกค้าสร้าง AI agent ของตัวเอง ด้วย LangChain, Google ADK หรือ Claude Code แล้วเสียบเข้าไปทำงานกับข้อมูล HR และ Finance ของ Workday ได้เลย ไม่ต้องผ่าน UI ไม่ต้องมีคนล็อกอิน. เขาเปิด MCP server มี 275 read tools กับ 54 write tools ครอบทุก workflow ใหญ่. ที่สำคัญคือ model-neutral — รัน Anthropic, Google, OpenAI, Mistral, Nemotron ก็ได้. แต่ที่น่าสนใจกว่าคือ governance — agent ทุกตัวต้องผูกกับ Agent System User แยกจากคน แล้ววิ่งผ่าน OAuth กับ audit trail ชุดเดียวกับ user ปกติ. นี่คือ signal สำคัญ — SaaS ยักษ์ที่คุม data ของ enterprise กำลังเลิกสู้สงคราม UI agent แล้วย้ายตัวเองลงไปเป็น data layer ชั้นล่างที่ agent runtime ของใครก็ได้ต้องมาคุยด้วย. ถ้าคุณสร้าง vertical agent อยู่ นี่คือ surface area ใหม่ที่กว้างมหาศาล — แต่คุณจะต้องยอม Workday เป็น gatekeeper และจ่ายต่อ query. จับตา Salesforce, SAP, Oracle ให้ดี ภายในสองไตรมาสน่าจะมี headless เหมือนกัน
