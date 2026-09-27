---
date: 2026-09-22
slug: salesforce-aiforce-agent-coworker
topic: use-case
reading_time_min: 5
sources: 4
image_prompt: |
  Editorial isometric illustration of a Salesforce cloud dissolving into a glowing
  agent silhouette; three stacked labels on the right read "100+ MCP TOOLS",
  "AGENTFORCE COWORKER GA", "AIFORCE REPLACES UI". A tiny Claude and Gemini icon
  hover beside a bridge labeled "CLAUDEFORCE / SLACKFORCE". Cinematic navy-and-sky
  Salesforce blue with orange highlights, sharp contrast for 200px thumbnails,
  no real human faces, 1:1 aspect. Editorial illustration in the style of an
  Information cover on enterprise software.
image: images/26-09-28-0616-03-salesforce-aiforce-agent-coworker.png
---

# Salesforce เปิดเกม "AI replaces UI" ที่ Dreamforce '26 — Agentforce Coworker GA, Claudeforce เข้าห้อง, MCP tool ทะลุ 100+

## TL;DR
- Dreamforce '26 (15-17 ก.ย.) headline คือ **AIforce** — "live interface layer" ที่ยกทั้ง Salesforce data + business logic + permission ให้เข้าถึงจากทุกที่ที่ agent อยู่ Salesforce บอกตรงว่า UI คือของที่ถูก replace
- Agentforce Coworker GA + Salesforce in Claude beta + Gemini in Reasoning Engine GA + Salesforce เองเปิด reasoning model ชื่อ **Koa** ใน pilot — 3 ทางเลือก brain ในระบบเดียว
- Headless 360 MCP server เปิด beta ตั้งแต่ ก.ค. — Dreamforce ประกาศ 100+ tool skill พร้อม Slackforce Slackbot MCP client — CRM ที่ agent อ่านออกได้ทั้งชุด

## เกิดอะไรขึ้น
Salesforce ปิด Dreamforce '26 (15-17 ก.ย. Moscone Center) ด้วยข้อความชัดที่สุดที่บริษัทเคยพูด — "AIforce is a live interface layer" — พูดตรง ๆ ว่า Salesforce UI แบบเดิม (record page, list view, Lightning App) กำลังจะไม่ใช่ way ที่ business logic ถูก execute อีกต่อไป. Agent จะเป็น interface. AIforce แปลงทั้ง data + business rule + permission + governance ให้ agent เข้าถึงได้ผ่าน composable architecture ที่ Salesforce เรียกว่า Enterprise AI Harness — เอาไปประกอบใน Claude, Slack, Google Workspace, หรือ workflow ของลูกค้าเอง.

Agentforce Coworker เข้า GA — agent ที่ Salesforce ปรุงให้ทำงานคู่กับพนักงานจริงในหน้าตา conversational แบบ persistent. Salesforce in Claude เข้า beta — Anthropic + Salesforce กำหนดร่วมกัน — agent ใน Claude สามารถเข้าถึง Salesforce record + workflow ตรง ๆ ผ่าน Claudeforce bridge. Gemini in Reasoning Engine GA — Salesforce reasoning stack ยอมรับ Gemini เป็น 1 ใน brain choice. Salesforce เองก็โผล่ **Koa** — reasoning model ของตัวเองที่ยัง pilot — เพื่อไม่ให้ตัวเองต้องพึ่ง frontier lab เดียว.

ด้าน MCP protocol — Headless 360 MCP server ที่เปิด beta ตั้งแต่กรกฎาคมด้วย 100 skill ตอนนี้ทะลุ 100+ tool skill + expand ด้วย **Slackforce Slackbot MCP client** ที่ทำให้ agent ใน Slack call Salesforce operation ได้ผ่าน MCP directly. Data 360 MCP server GA + Experience Layer beta. Server เดียวเปิด thousand-plus operation ผ่าน 4 tool ที่ agent เรียกแบบ stable — pattern ที่ต่างจาก "expose ทุก feature เป็น tool" ของ vendor อื่น ที่ agent bloat ไปเยอะ.

## ทำไมสำคัญ
Dreamforce '26 คือครั้งแรกที่ enterprise vendor อันดับ 1 ของ SaaS ยอมรับต่อสาธารณะว่า "UI is not our moat anymore." 2 ปีก่อน Salesforce ต่อต้าน pattern นี้ — CEO บอกว่า UI + user เป็น distribution unit — ปีนี้กลับ pivot มา say "AI is going to replace UI" กลาง keynote. เหตุผลไม่ใช่ vision — เป็นตัวเลข: Copilot, Gemini, Claude, ChatGPT ทำให้ user ทำงาน 60-70% ของ Salesforce ในหน้าต่าง chat ไม่กลับเข้า Salesforce UI. Salesforce เลือกที่จะแปลง distribution จาก "user มา login" เป็น "agent มา call API" — และเป็น first vendor ที่ทำ shift นี้ในเชิงยุทธศาสตร์.

Pattern สำคัญคือ **model portability**. Salesforce ไม่ผูกกับ vendor เดียว — Anthropic (Claude), Google (Gemini), OpenAI (via Copilot integration), และ Koa ของตัวเอง — ทั้งหมดเป็น option ในระบบเดียว. Enterprise buyer ที่กลัว lock-in กับ frontier lab เห็นแล้วรู้สึกอุ่นใจกว่า — และ Anthropic/Google ที่กำลังแย่ง enterprise share ต้อง discount กับ Salesforce เพื่อไม่ให้ Koa ครองที่ต่อไป. Salesforce วิ่งเกม platform-of-brains ที่คล้าย Databricks และ Snowflake ในโลก data — ผูกกับ enterprise data + governance layer ก่อน แล้วให้ model แข่งกันข้างบน.

3 partner ใหญ่ที่โผล่ครั้งนี้ — Anthropic, Google, และ Slack (in-house) — บอกว่า Salesforce จะ triangulate distribution ผ่าน 3 พื้นที่ที่ knowledge worker อยู่จริง: browser (Claude), search (Gemini), และ chat (Slack) — ไม่ใช่ Salesforce.com. บริษัทที่กำลังตัดสินใจว่าจะ deploy agentic CX platform ไหน จะเห็น optionality นี้เป็น edge สำคัญเทียบกับ Microsoft Copilot ที่ผูกกับ OpenAI + Microsoft ecosystem ล้วน.

## มุม AI Agent Platform
**Builders** ที่ทำ orchestration หรือ vertical agent — Headless 360 กับ Slackforce เปิดโอกาส integrate CRM ที่ใหญ่ที่สุดในโลกโดยไม่ต้องเขียน connector เอง. ถ้า target ตลาด mid-market ขึ้นบน จับ Salesforce MCP กับ Slack MCP เป็น requirement ไม่ใช่ nice-to-have แล้ว. **Users / business** ที่ใช้ Salesforce อยู่แล้ว — ประเมินตอนนี้ว่า workflow ไหนย้ายไป Claude/Slack ได้ทันที (customer service inbound, sales inbox triage, order status query) — และ workflow ไหนต้องคง UI ไว้ (deal desk approval, compliance review). Salesforce ก็เปิดโอกาสให้ measure ROI ของ Agentforce Coworker กับ ROI ของ human seat — comparison ที่จะขึ้น boardroom deck ภายในไตรมาสหน้า. **Ecosystem** — Microsoft, ServiceNow, HubSpot, Zoho ต้อง response ภายใน 6 เดือนถ้าจะไม่ตกขบวน. Microsoft น่าจะเดินเกม Copilot Studio + Dataverse MCP layer ใน Ignite เดือนพฤศจิกายน — ServiceNow จะยัด Now Assist ที่ค่อย ๆ ทำมาแล้ว, HubSpot กับ Zoho มี option เล็กกว่า อาจต้องรวมกับ frontier lab. คนที่แพ้จริงคือ mid-tier CRM ที่ไม่มี MCP layer และ enterprise SI ที่ขายเวลาเซตอัพ Salesforce แบบดั้งเดิม — model นั้นกำลังหด.

## Sources
- [Salesforce Launches AIforce at Dreamforce '26: 'AI Replaces the UI' — Salesforce Ben](https://www.salesforceben.com/salesforce-launches-aiforce-at-dreamforce-26-ai-replaces-the-ui/)
- [Biggest Dreamforce '26 Announcements — Salesforce Ben](https://www.salesforceben.com/biggest-dreamforce-26-announcements-everything-in-a-nutshell/)
- [Dreamforce 2026 Announcement: AIforce, Claudeforce, Koa & AI Updates — Concret.io](https://www.concret.io/blog/dreamforce-2026-keynote-day-1)
- [Headless 360 (Beta) | Hosted MCP Servers | Salesforce Developers](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/headless-360-mcp.html)

---

## Audio script
สัปดาห์ที่แล้ว Salesforce ปิด Dreamforce '26 ด้วยข้อความที่ชัดที่สุดเท่าที่เคยพูด AI is going to replace UI. Headline คือ AIforce — live interface layer ที่ยก Salesforce data business logic กับ permission ให้ agent เข้าถึงจากทุกที่ที่ user ทำงานจริงไม่ใช่หน้า Salesforce เอง. Agentforce Coworker เข้า GA แล้ว. Salesforce in Claude beta ทำให้ agent ใน Claude เรียก Salesforce record ได้ตรง ๆ. Gemini in Reasoning Engine GA. แล้ว Salesforce ยังเปิด Koa reasoning model ของตัวเอง pilot อีกด้วย. ด้าน MCP protocol Headless 360 MCP server ทะลุ 100+ tool skill พร้อม Slackforce Slackbot MCP client ให้ agent ใน Slack เรียก Salesforce ผ่าน MCP ตรง. Signal ที่สำคัญคือ Salesforce ยอมรับต่อสาธารณะว่า UI ไม่ใช่ moat อีกต่อไป reason ไม่ใช่ vision แต่คือ user 60-70% ทำงาน Salesforce ในหน้าต่าง chat ไม่กลับมา login อีกแล้ว. Salesforce เลือก pivot จาก user มา login เป็น agent มา call API และเป็น vendor แรกที่ทำ shift นี้จริงจัง. Pattern อีกอย่างคือ model portability Anthropic Google และ Koa ของตัวเองเป็น option ในระบบเดียว enterprise buyer ที่กลัว lock-in อุ่นใจกว่า. ถ้าคุณสร้าง vertical agent target enterprise Salesforce MCP กับ Slack MCP คือ integration ที่ต้องเสียบ ไม่ใช่ nice-to-have แล้ว. คู่แข่งใหญ่คือ Microsoft ServiceNow HubSpot ต้อง response ภายใน 6 เดือน ไม่งั้นตกขบวนครับ.
