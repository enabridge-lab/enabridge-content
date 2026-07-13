---
date: 2026-07-14
slug: microsoft-dataverse-coding-agent-plugin-claude-cursor-mcp
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric hero illustration of a giant glowing hub labeled
  "DATAVERSE" at the center of a dark technical plane, with three thick
  neon pipelines flowing out labeled "CLAUDE", "CURSOR", "GITHUB
  COPILOT". A shelf on the right displays stacked boxes labeled "60+
  MCP SERVERS" and a badge that reads "CERTIFIED". A side panel on the
  left shows a lock icon with text "RBAC / LEAST PRIVILEGE / BYO MCP".
  High-contrast cinematic teal-blue-and-orange palette, bold text
  readable at 200px thumbnail, 1:1 aspect, no real human faces.
image: images/26-07-14-0609-03-microsoft-dataverse-coding-agent-plugin-claude-cursor-mcp.png
---

# Microsoft เปิด Dataverse plugin ให้ Claude + Cursor + Copilot ใช้ผ่าน MCP — เดิมพัน "one data platform, any agent"

## TL;DR
- 6 ก.ค. Microsoft ประกาศ **Dataverse coding agent plugin** รองรับ **Claude, Cursor และ GitHub Copilot** พร้อมกัน — ครั้งแรกที่ enterprise data platform ของ Microsoft เปิดให้ agent จากคู่แข่งใช้เป็น first-class citizen ผ่าน MCP standard, ไม่ใช่แค่ Copilot ecosystem ของตัวเอง
- Catalog มี **60+ ready MCP servers** สำหรับ Copilot Studio + Azure AI Foundry + Microsoft 365 Copilot + GitHub Copilot, พร้อมเปิด **MCP certification pathway ผ่าน Partner Center** ให้ ISV publish MCP ของตัวเองแบบมี badge + governance + discoverability ในตัว
- Plugin enforce **least-privilege security + Dataverse RBAC**, มี BYO MCP flow ที่ให้ admin approve/monitor MCP internal — Microsoft ตี positioning ชัดว่า "ที่ agent จะ touch business data อย่างปลอดภัย คือ Dataverse" ไม่ว่าจะเป็น agent ค่ายไหน

## เกิดอะไรขึ้น
วันที่ 6 ก.ค. Charles Lamanna ทีม Power Platform ออก post ยาว: **Dataverse Is Your Agent Data Platform: Here's What's New in July 2026**. สาระสำคัญคือ Microsoft ขยาย Dataverse — ระบบ database + governance layer ที่นั่งใต้ Power Platform, Dynamics 365 และตอนนี้คือ Copilot Studio ทั้งหมด — ให้เป็น **primary data plane สำหรับ agent จากค่ายไหนก็ได้**. ก้าวใหญ่คือ **Dataverse coding agent plugin** ที่เดิมทำงานกับ GitHub Copilot ใน Visual Studio Code เท่านั้น ตอนนี้ **available บน Claude และ Cursor ด้วย** — สอง IDE agent ที่กินตลาด developer จริงในปีนี้ (Claude Code + Anthropic Console + Cursor 2.0)

Plugin ตัวนี้ให้ agent ค่ายไหนก็ได้ทำ 3 อย่าง — (1) discover data model, table schema, business rule ใน Dataverse ผ่าน natural language, (2) query/mutate data ตาม existing RBAC + row-level security, (3) generate code + Power Fx expression + plugin ที่ deploy กลับ Dataverse ได้เลย. Skill routing ทำให้ agent ไม่ต้องรู้ raw Dataverse API — utterance เช่น "add validation on Account table for tax ID" เข้ามา, plugin route ไปหา skill ที่ตรง context. ทั้งหมดเปิดเป็น **open-source skill architecture** — Microsoft commit ว่า community ขยายได้

ในระดับ ecosystem — MCP moves ใหญ่กว่านั้น. Dataverse now ships กับ **60+ ready MCP servers** ที่พร้อมใช้ใน Copilot Studio, Azure AI Foundry, Microsoft 365 Copilot, GitHub Copilot, และ MCP client อื่น ๆ. เพิ่ม **MCP certification pathway ผ่าน Partner Center** — ISV package MCP ของตัวเองเข้า certification process 3 ขั้น (package prep → offer type → publish) แล้วได้ badge + discoverability ใน Microsoft ecosystem. ที่ enterprise ชอบมากที่สุดคือ **"Bring Your Own MCP"** flow — องค์กร connect MCP internal (proprietary API, custom tool) เข้า Dataverse ได้ตรง โดยมี admin approval + visibility management + audit log built-in

## ทำไมสำคัญ
Move นี้เป็น pivot ที่ต่อเนื่องกับ pattern ที่ Enabridge tracking — **Microsoft เลิก bet ว่า Copilot ecosystem จะเป็น agent runtime เดียวของ enterprise, แล้วหันไป bet ว่า data + governance layer ของ Microsoft จะเป็น underlying** ที่ทุก agent (Claude, Cursor, ChatGPT, Gemini) วิ่งผ่าน. เป็นเกม infrastructure economics แบบเดียวกับที่ AWS ทำกับ S3+IAM ในยุค 2015 — ไม่ต้อง lock ที่ compute layer, lock ที่ data layer สำเร็จก็พอ. Microsoft มี **300M+ M365 seat, 5.6M+ Dataverse tenant, hundreds of ISV** เป็น distribution moat ที่ competitor แทบเป็นไปไม่ได้ทำในระยะ 5 ปี

ทำไม timing ตอนนี้ — **MCP 2026-07-28 spec ship 28 ก.ค. นี้** (Enabridge เขียนถึงเมื่อวาน). MCP เพิ่ง promote OAuth 2.1 + Enterprise-Managed Authorization + stateless core เข้า stable. Microsoft ที่ ship 60+ certified MCP + Partner Center certification 3 สัปดาห์ก่อน spec ลง GA เท่ากับ **ยึด reference implementation** ให้ enterprise ทั้งวงการ. เมื่อองค์กรมองหา MCP server + agent skill ที่ certified + governed + discoverable — Microsoft catalog จะเป็นตัวเลือกแรกที่ CISO เซ็นให้. หลังจากนี้ Google Cloud + AWS จะประกาศ counter — คาดว่า Google Cloud Next 2026 ครั้งถัดไปมี "MCP Studio" หรือคล้ายกัน, AWS Bedrock Agent Marketplace อาจโผล่ที่ re:Invent

signal ระยะยาว: **agent ไม่ใช่ product, agent เป็น interchangeable layer**. เมื่อ Dataverse plugin ทำงานเท่าเทียมกันบน Claude, Cursor, Copilot — enterprise เริ่ม procurement agent แบบ "ประหยัด/แม่น/บาก" per task ไม่ใช่ per vendor. Coding agent market เข้าสู่ **commodity phase** เร็วกว่าที่คาด, ที่รอด differentiate ต้องอยู่ที่ tool depth + reasoning quality + workflow specialization, ไม่ใช่ integration coverage. ในทางกลับกัน **data + governance layer วัด value ได้จำนวนมากขึ้น** — เพราะ agent ทุกตัวต้อง touch data ผ่านมัน

## มุม AI Agent Platform
สำหรับ **builders**: ถ้าทำ agent framework — ship MCP client + Partner Center package ก่อนสิ้นปี. distribution ผ่าน Microsoft catalog เร็วกว่า organic outreach 10x. ถ้าทำ vertical SaaS ที่มี tool/API — publish MCP server, apply certification, ปล่อยให้ Claude/Cursor/Copilot ทุกตัวเรียก tool ของคุณจาก Dataverse ได้ตรง. ที่ Enabridge ควรทำในไตรมาสนี้: Openbridge MCP server ที่ package Thai-context data (SET data, กรมสรรพากร e-tax invoice format, banking regulatory) แล้ว publish ผ่าน Microsoft Partner Center — เท่ากับได้ **default position** ที่ Thai enterprise ทุกที่ใช้ Copilot Studio อยู่แล้ว. builder หน้าใหม่ที่ทำ point solution + hoard integration จะเสียเปรียบ

สำหรับ **users/business**: (1) ก่อนต่อ contract Copilot Studio ต่อ ปีหน้า ถามให้ inventory ว่า agent ที่ใช้จริง — Claude, Cursor, ChatGPT, Gemini — เชื่อม Dataverse ได้ไหม ผ่านช่องทางไหน; (2) ตั้ง MCP governance policy: MCP internal ที่ BYO เข้ามาต้อง review ที่ admin console ก่อน enable, มี audit log ครบ; (3) ถ้าไม่ใช้ Dataverse — พิจารณาว่า data platform อื่น (Snowflake, Databricks, Salesforce Data Cloud) มี MCP + skill routing + certification เทียบเท่าหรือไม่ ก่อน commit multi-year contract. สำหรับ Thai enterprise ที่พึ่ง migrate Dynamics 365 → Fabric — window นี้ดีสำหรับ standardize MCP layer

สำหรับ **ecosystem**: **Snowflake, Databricks, Salesforce Data Cloud** ต้องตอบภายในไตรมาส. Databricks น่าจะออก Mosaic MCP Certification (มี foundation จาก Unity Catalog อยู่), Snowflake ต่อยอด Cortex Agents + Native App Framework, Salesforce ใช้ MuleSoft + Data Cloud + Agentforce Actions รวมกัน. Loser คือ standalone agent framework startup ที่ไม่มี data + governance layer ของตัวเอง (LangChain LangGraph Platform, CrewAI Enterprise, Vercel AI Gateway) — ต้อง partner กับ hyperscaler ของ data ไม่งั้น relevance หายในสองรอบสัญญา. **Openbridge angle**: ผลัก "MCP-first data connectivity" เป็น differentiation ต่อ Thai SaaS ที่ Microsoft partner ไม่ครอบคลุม — Local ERP, government API, Thai bank open banking — และ publish ผ่าน Partner Center ให้ discoverable ในไทย

## Sources
- [Dataverse Is Your Agent Data Platform: Here's What's New in July 2026 — Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/2026/07/06/dataverse-july2026/)
- [Dataverse Expands Coding Agent Plugin to Claude, Cursor, and Copilot with MCP Governance — Windows Forum](https://windowsforum.com/threads/dataverse-expands-coding-agent-plugin-to-claude-cursor-and-copilot-with-mcp-governance.435235/)
- [Microsoft's July Dataverse Wave Brings Business Data Directly to Copilot — Windows News](https://windowsnews.ai/article/microsofts-july-dataverse-wave-brings-business-data-directly-to-copilot-adds-semantic-models-and-mor.432378)
- [Dataverse Meets Claude, Cursor and Copilot via MCP — Digital Applied](https://www.digitalapplied.com/blog/microsoft-dataverse-coding-agent-plugins-mcp-governance-2026)

---

## Audio script
วันที่ 6 กรกฎาคม Microsoft ประกาศครั้งใหญ่ Dataverse coding agent plugin ที่เดิมทำงานเฉพาะกับ GitHub Copilot ตอนนี้ available บน Claude และ Cursor ด้วย ครั้งแรกที่ enterprise data platform ของ Microsoft เปิดให้ agent จากคู่แข่งใช้เป็น first class citizen ผ่าน MCP standard ไม่ใช่แค่ Copilot ecosystem ของตัวเอง

Plugin ให้ agent ค่ายไหนก็ได้ทำสามอย่าง discover data model และ business rule ผ่าน natural language query mutate data ตาม existing RBAC generate code Power Fx และ plugin กลับ Dataverse ทั้งหมดเปิดเป็น open source skill architecture ในระดับ ecosystem Microsoft ship 60 กว่า MCP server สำเร็จรูป เปิด certification pathway ผ่าน Partner Center และมี Bring Your Own MCP flow ที่ admin approve และ audit ได้ครบ

Move นี้เป็น pivot สำคัญ Microsoft เลิก bet ว่า Copilot จะเป็น agent runtime เดียว หันไป bet ว่า data กับ governance layer ของ Microsoft จะเป็น underlying ที่ทุก agent วิ่งผ่าน เป็นเกม infrastructure economics แบบเดียวกับที่ AWS ทำกับ S3 ในยุค 2015 timing ตรงกับ MCP 2026 07 28 spec ที่ ship 28 กรกฎาคม เป็น one two punch ที่ยึด reference implementation ให้ enterprise ทั้งวงการ

signal ระยะยาว agent ไม่ใช่ product agent เป็น interchangeable layer coding agent market เข้าสู่ commodity phase เร็วกว่าที่คาด สำหรับ builder Thai ที่ทำ vertical SaaS ให้พิจารณา publish MCP server ผ่าน Partner Center ก่อนสิ้นปีจะได้ default position ที่ enterprise ที่ใช้ Copilot Studio อยู่แล้ว สำหรับ business ก่อนต่อ contract Copilot Studio ปีหน้า ให้ตรวจว่า Claude Cursor ChatGPT ที่ team ใช้จริง เชื่อม Dataverse ได้ผ่านช่องไหน สำหรับ ecosystem Snowflake Databricks Salesforce Data Cloud ต้องตอบภายในไตรมาสไม่งั้นเสีย positioning
