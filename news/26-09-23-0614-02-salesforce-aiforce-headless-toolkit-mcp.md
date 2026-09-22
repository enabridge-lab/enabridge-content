---
date: 2026-09-16
slug: salesforce-aiforce-headless-toolkit-mcp
topic: openbridge-trend
reading_time_min: 5
sources: 4
image_prompt: |
  An editorial isometric render of a colossal Salesforce-blue cloud
  building whose classical front façade is being carefully peeled off by
  cranes, revealing an inner architecture of glowing MCP conduits, API
  pipes and skill sockets. Above the exposed core hovers a neon banner:
  "AI REPLACES THE UI — DREAMFORCE '26". Three delivery ports stream data
  to floating third-party surfaces labeled "CLAUDEFORCE", "SLACKFORCE",
  and "AGENTFORCE COWORKER"; smaller partner logos (Anthropic, AWS,
  Google, Microsoft) orbit a marketplace ring stamped "AGENTEXCHANGE".
  Large contrasty text tiles read "168 DAYS", "MCPs + APIs + SKILLS",
  "$540M ARR AGENTFORCE". Salesforce blue + cyan accents, editorial
  isometric style, 1:1 aspect, no real human faces (silhouetted crowd on
  ground floor).
image: images/26-09-23-0614-02-salesforce-aiforce-headless-toolkit-mcp.png
---

# Salesforce ปลด UI ตัวเอง — AIforce + Headless Toolkit เปิดทุก workflow ให้ agent เรียกผ่าน MCP; AgentExchange launch พร้อม Anthropic + Google + Microsoft

## TL;DR
- 16 ก.ย. **Dreamforce 2026** — Salesforce เปิดตัว **AIforce** เป็น "live interface layer" + **Headless Toolkit** ที่ expose ทุก element ของ platform (data, workflow, business logic, governance) ผ่าน **MCP servers, APIs, plug-ins, skills**. Tagline อย่างเป็นทางการ: **"AI Replaces the UI"**
- Launch surface 3 ตัว: **Claudeforce** (Salesforce บน Claude), **Slackforce** (บน Slack), **Agentforce Coworker** (native agent). **AgentExchange marketplace** เปิดพร้อมกัน — partner ecosystem รวม Anthropic, AWS, Google, Microsoft (agentic interfaces); Lovable, Vercel (AI builders); Docusign, Gamma, Jasper, Rippling (apps/agents)
- Timeline สำคัญ: **168 วัน** จาก Marc Benioff ประกาศ "we need to rethink our UI" ที่ TrailblazerDX เดือน มี.ค. → announcement นี้. Agentforce เดิม (product ก่อนหน้า) มี **$540M ARR / 18,500 enterprise customer** ต้น 2026 — AIforce เป็น extension layer ที่ทำให้ Agentforce เข้าไปทำงานใน Claude/Slack/third-party ได้โดยไม่ต้องเปิด Salesforce UI

## เกิดอะไรขึ้น

Dreamforce 2026 (16 ก.ย. SF) Marc Benioff ขึ้นเวที keynote พร้อมประโยคที่ SalesforceBen จับเป็น headline: **"หลัง AI มา, การมี UI ของตัวเอง = คือ liability"**. Salesforce เปิดตัว **AIforce** — เป็น "live interface layer" ที่ทำให้ **ทุก object, workflow, business logic, permission** ใน Salesforce กลายเป็น **callable resource** สำหรับ agent + third-party surface. Framing ทางการ: "Instead of fixed UI, AIforce empowers anyone to build composable, intelligent, live interfaces, wherever work happens"

**Architecture:** AIforce ทำงานบน **Headless Toolkit** — open architecture ที่ expose ทุกส่วนของ Salesforce ออกมาเป็น 4 protocol/artifact:
1. **MCP servers** — ให้ agent (Claude, ChatGPT, Gemini, Copilot) query + mutate data ผ่าน standardized protocol
2. **APIs** — REST + GraphQL layer เดิมที่ modernize
3. **Plug-ins** — custom logic ที่ Salesforce host ให้
4. **Skills** — packaged capability ที่ agent เรียก atomic ได้ (e.g. "close opportunity", "create case", "run apex flow")

**Launch surface 3 ตัว ที่ Salesforce ship พร้อมกัน:**
- **Claudeforce** — Anthropic partnership; Claude Desktop + Claude Code สามารถ query Salesforce data + trigger workflow โดยไม่ต้องออกจาก Claude
- **Slackforce** — native Slack integration ที่ upgrade เดิม; agent conversation ใน Slack ตอบด้วย live Salesforce data
- **Agentforce Coworker** — native agent ที่รันใน Salesforce cloud, autonomous ที่ทำงานบน pipeline / case queue / campaign เอง

**AgentExchange marketplace** เปิดพร้อมกัน — เป็น "App Exchange for the agent era". Launch partner list ยาว: **agentic interfaces**: Anthropic, AWS, Google, Microsoft; **AI builders**: Lovable, Vercel; **AI agents/tools**: Docusign, Gamma, Jasper, Rippling. Partner ecosystem ประเภทนี้ = "everyone shows up" — สัญญาณว่า Salesforce ยึด standard เป็น neutral ground เพื่อไม่ให้ Microsoft (Copilot Studio + Foundry) หรือ Google (Gemini Enterprise Agent) ครอบไปเอง

**Numbers ที่ไปกับ launch:** Agentforce เดิม (product ที่ AIforce เข้าไป amplify) มี **ARR $540M / 18,500 enterprise customers** ต้น 2026, Benioff เรียกเป็น "fastest growing product ever" ของบริษัท. AIforce ไม่ใช่ product ใหม่แยก — เป็น **delivery + extension layer** ที่ทำให้ Agentforce เรียกจากทุก surface ที่ agent อยู่

## ทำไมสำคัญ

Move นี้เป็นครั้งแรกที่ **enterprise SaaS ระดับ top-5 (Salesforce = market cap ~$300B)** ยอมรับต่อสาธารณะว่า **UI ของตัวเอง = ไม่ใช่ competitive moat อีกต่อไป** — data + workflow + governance ต่างหากคือ moat. เป็นการ concede ที่หนักหน่วง เพราะ Salesforce สร้าง brand ตัวเองมาบน "Lightning UI + AppExchange UI paradigm" ตลอด 20 ปี. SalesforceDevops.net จับเวลาไว้: **168 วัน** จาก TrailblazerDX มี.ค. ("Benioff talked himself out of his own UI") ถึง Dreamforce ก.ย. — เป็น product pivot ที่เร็วที่สุดของบริษัท mega-cap SaaS ที่เคยเห็นมา

Pattern ที่กำลัง standardize: **"headless + agentic delivery"** = playbook มาตรฐานของ enterprise SaaS 2026-27. Sapiens (insurance core system, launch SapiensAIP 14 ก.ย.), Workday (rumor ว่ากำลังทำ "Workday Agent Layer" คล้ายกัน), ServiceNow (Now Assist + AgentIQ), SAP (Joule Agent Framework) — ทุกเจ้าเดินทางเดียวกัน. **MCP = de facto delivery protocol** — เพราะ Salesforce เลือก MCP เป็น first-class citizen (ไม่ใช่ REST-only) มันตอกย้ำว่า Anthropic ยึด standard นี้สำเร็จภายใน 12 เดือน

**สิ่งที่หลายคนพลาด:** Salesforce ไม่ได้แค่ expose data — เขา expose **governance + permission model** ด้วย. หมายความว่าเมื่อ Claude เรียก Salesforce object ผ่าน MCP, permission ยัง enforce ตาม Salesforce roles/profiles เดิม; audit log ยังเก็บใน Salesforce; sharing rules ยัง apply. เป็นการตัด objection ที่ใหญ่ที่สุดของ enterprise IT (compliance + audit trail) ทันที — และเป็น pattern ที่ vendor อื่นต้อง copy ไม่งั้น buyer จะไม่ deploy

จุดที่ต้องจับตา: **"AI replaces the UI" หมายถึง UI vendor แบบ Retool / Bubble / Softr / OutSystems ที่ position เป็น "no-code UI on top of your data" จะเจอ pressure หนัก**. ถ้า Salesforce (คนที่มี UI มากที่สุดในโลก B2B) ยอมทิ้ง UI, ตลาด "build UI on top of API" อาจ shrink 30-50% ใน 24 เดือน. Retool ล่าสุด pivot ไป **"AI-first workflow builder"** = signal ว่าเขาเห็นแนวโน้มนี้แล้ว

## มุม AI Agent Platform

สำหรับ **builders** ที่ทำ agent สำหรับ enterprise: **MCP integration = table stake ปีนี้แล้ว**. ถ้า agent ของคุณไม่พูด MCP กับ Salesforce/ServiceNow/Workday/SAP, ลูกค้าจะไม่ deploy — ไม่ใช่เพราะ feature แต่เพราะ compliance team ไม่ approve. Startup ไทยที่ทำ vertical agent (finance ops, HR ops, sales ops) ควร **prioritize MCP client ก่อน UI polish** — 2 สัปดาห์ MCP > 2 เดือน UI

สำหรับ **users / business** ที่ deploy agent — **ประเมิน Agentforce Coworker vs custom-built** ใหม่. Agentforce Coworker ตอนนี้เข้าไปทำงานใน Slack + Claude ได้แล้ว = สาเหตุที่ต้องสร้าง custom agent stack แคบลงมาก. เว้นแต่ business logic ของคุณเฉพาะเจาะจงมาก (industry-specific compliance, regional regulation, proprietary workflow), 60-70% ของ use case ที่ทีมกำลัง build เองอาจใช้ Agentforce Coworker + MCP ได้ทันที. **Procurement checklist ใหม่:** ก่อน sign contract SaaS vendor ปีหน้า ให้ถาม "Do you ship MCP server?" — เพราะถ้าไม่มี = ทีมคุณต้อง build integration เอง = $500K–2M engineering cost

สำหรับ **ecosystem** — **Anthropic = biggest indirect winner** เพราะ Salesforce ตั้ง Claudeforce เป็น flagship surface, ส่งไปรวมกับ dueling launch วันเดียวกันของ Opus 5.5 = Claude กำลังเป็น "enterprise default LLM" อย่างชัดเจน. **Microsoft (Copilot Studio + Foundry)** = ยังคง lead ที่ Office 365 side แต่พร้อมที่จะเจอ AgentExchange partner แข่งตรงใน Copilot; **Google (Gemini Enterprise Agent + Agent Data Cloud)** = ต้อง ship equivalent AgentExchange partnership ใน 60-90 วัน ไม่งั้น narrative "Salesforce ยึด agentic distribution" ก็จบเกม. Sovereign SaaS ประเทศไทย/อาเซียน (ThaiLLM, Sea-Lion, local ERP) ควร copy pattern Headless Toolkit เร็ว — timing สำคัญเพราะ enterprise buyer เริ่ม lock rundown MCP standard 6-12 เดือนข้างหน้า

## Sources
- [Salesforce Launches AIforce at Dreamforce '26: 'AI Replaces the UI' — Salesforce Ben](https://www.salesforceben.com/salesforce-launches-aiforce-at-dreamforce-26-ai-replaces-the-ui/)
- [Salesforce announces AIforce, unlocking the power of its platform using composable agents — SiliconANGLE](https://siliconangle.com/2026/09/15/salesforce-announces-aiforce-unlocking-the-power-of-its-platform-using-composable-agents/)
- [Salesforce Unveils AIforce, Bringing the Full Power of Its Platform to Any Interface — Salesforce.com](https://www.salesforce.com/news/stories/aiforce-announcement/)
- [168 Days: How Salesforce Talked Itself Out of Its Own User Interface — SalesforceDevops.net](https://salesforcedevops.net/index.php/2026/09/15/salesforce-aiforce-168-days-dreamforce-2026/)

---

## Audio script
Dreamforce 2026 ที่ San Francisco เมื่อ 16 กันยา Salesforce เปิดตัว AIforce กับ Headless Toolkit — tagline ทางการคือ AI Replaces the UI. AIforce เป็น live interface layer ที่เปิด data, workflow, business logic, governance ของ Salesforce ให้ agent จากที่ไหนก็ได้เรียกใช้ผ่าน MCP, API, plug-in และ skill. Launch surface 3 ตัวคือ Claudeforce บน Claude Desktop + Claude Code, Slackforce ใน Slack, และ Agentforce Coworker เป็น native agent ที่รันเองใน Salesforce cloud. AgentExchange marketplace เปิดพร้อมกัน — partner ecosystem ประกอบด้วย Anthropic, AWS, Google, Microsoft, Lovable, Vercel, Docusign, Gamma, Jasper, Rippling. Timeline สำคัญคือ 168 วัน จาก Marc Benioff ประกาศต้อง rethink UI ตอน TrailblazerDX มีนา ถึง announcement นี้ — เป็น product pivot ที่เร็วที่สุดของ mega-cap SaaS ที่เคยเห็น. Signal ที่สำคัญคือ enterprise SaaS ระดับ top-5 ยอมรับต่อสาธารณะว่า UI ของตัวเอง = ไม่ใช่ moat อีกต่อไป, data + workflow + governance ต่างหากคือ moat. Pattern นี้จะขยายไป Workday, ServiceNow, SAP ทันที ใน 6-12 เดือนข้างหน้า. MCP กลายเป็น de facto delivery protocol เพราะ Salesforce เลือกเป็น first-class citizen. สำหรับ builder ไทยที่ทำ agent เข้า enterprise — MCP integration = table stake, ไม่มี = compliance ไม่ approve. สำหรับ enterprise buyer — procurement checklist ใหม่ต้องถาม vendor ทุกเจ้าว่า ship MCP server หรือไม่ ก่อน sign contract SaaS ปีหน้า.
