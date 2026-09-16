---
date: 2026-09-17
slug: 26-09-17-0609-01-salesforce-aiforce-interface-layer-claude-slack
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a giant translucent glass window
  labeled "SALESFORCE UI" shattering into shards, and behind it a clean
  network of glowing pipes marked "CLAUDE", "SLACK", "AMAZON Q",
  "GEMINI" all pouring into a central control hub labeled "AIforce".
  Three floating badges: "37 SALES SKILLS", "800K INQUIRIES / YEAR",
  "ZERO DATA RETENTION". Editorial magazine style, deep navy background,
  bright cyan and orange highlights, 1:1 aspect, high contrast for
  200px thumbnail, no real human faces.
image: images/26-09-17-0609-01-salesforce-aiforce-interface-layer-claude-slack.png
---

# Salesforce ประกาศ AIforce — "AI replaces the UI" เปิดข้อมูล CRM ให้ Claude, Slack, Amazon Q ใช้ตรง

## TL;DR
- Dreamforce 2026 Day 1 (15 ก.ย.) — Salesforce เปิดตัว **AIforce** เป็น interface layer ใหม่บน Agentforce/Data 360/Customer 360 ให้ข้อมูล+business logic+security+governance ของ Salesforce ทำงานอยู่ใน Claude, Slack, Amazon Q, Gemini Enterprise แทนที่จะเปิดหน้าจอ Salesforce
- สามผลิตภัณฑ์แรก: **Claudeforce** (37 sales skills พร้อม, 40 skills ผ่าน Claude Code plugin), **Slackforce** (Slackforce Surfaces + Slack CRM), **Agentforce Coworker** (AI teammate ใน Lightning interface)
- Signal ใหญ่ที่สุดของงานปีนี้: Salesforce ยอมรับต่อสาธารณะว่า UI ของตัวเองไม่ใช่ที่ทำงานหลักของ user อีกต่อไป — เดินหน้าเป็น **data + logic + governance layer** ใต้ทุก AI client แทน

## เกิดอะไรขึ้น

Marc Benioff ขึ้นเวที Moscone West วันจันทร์ 15 ก.ย. แล้วพูดประโยคที่ทุกคนจะจำ: **"AI is creating an interface revolution."** สิ่งที่ตามมาคือ AIforce — ชั้นซอฟต์แวร์ใหม่ที่ Salesforce เรียกว่า "AI interface layer" ที่วางอยู่บน Agentforce, Data 360 และ Customer 360 หน้าที่ของมันคือเอาข้อมูล CRM, business logic, permissions และ policy ของ Salesforce **ไปทำงานอยู่ในที่ที่พนักงานเปิดอยู่แล้ว** — ไม่ว่าจะเป็น Claude, Slack, Amazon Q หรือ Gemini Enterprise — ไม่ใช่บังคับให้มาเปิด Lightning

AIforce เปิดตัวพร้อมสามผลิตภัณฑ์: **Claudeforce** เอา Salesforce เข้าไปอยู่ใน Claude ผ่าน prebuilt MCP server พร้อม 37 sales skills (prospecting, pipeline management, ต่อยอดไปยัง Tableau analytics, service, marketing, commerce), บวก 40 skills ผ่าน Claude Code plugin ที่มี GitHub library access. Deloitte, GitLab และ Legora ทดลองใช้แล้ว. **Slackforce** เอา Salesforce context เข้า Slack — Slackforce Surfaces เปิดให้ team ดึง live pipeline stages / account histories / case updates เข้ามาเป็น interactive interface ที่หลายคน act ได้พร้อมกัน โดยไม่ต้องออกจาก Slack; ฟีเจอร์ Slack CRM ใหม่ให้สร้าง account + update record ได้ตรงในนั้น. Hotel Engine CEO ยืนยันว่าใช้ Slackforce จัดการ inquiries **มากกว่า 800,000 รายการต่อปี**. **Agentforce Coworker** คือ AI teammate ใน Lightning interface — เรียก specialized agent ตัวอื่นได้ ทำ multi-step action ตามสิทธิ์ของ user จริง

ที่น่าสังเกตคือ AIforce ไม่ได้เริ่มจากศูนย์ — มันเป็น productization ของ **Headless 360 architecture** ที่ Salesforce เปิดตัวมีนา 2026 คือแยก data + logic + policy ออกจาก UI ให้ทุก endpoint (MCP, REST API, plug-in, skill, developer tools) เรียกใช้ได้เท่าเทียม AgentExchange ตอนนี้มี **Anthropic, AWS, Google, Lovable Labs, Vercel, Docusign, OpenAI** เป็น launch partner — ทั้งหมดออกแบบให้ integrate เป็น first-class citizen ไม่ใช่ third-party plugin. Benioff ย้ำเรื่อง Zero Data Retention เพื่อให้ผู้บริหาร enterprise สบายใจว่า prompt + data ที่ส่งผ่าน AIforce จะไม่ไปโผล่ในการ train model ของ Anthropic / Google / OpenAI

## ทำไมสำคัญ

**นี่คือประกาศยอมแพ้ของ UI-first vendor rat race** — Salesforce ที่มี Lightning ราคาแพงเป็นสัญลักษณ์ของ SaaS ยุค 2010s ยอมรับต่อสาธารณะว่าอนาคตของงาน enterprise ไม่ได้เกิดในหน้าจอของ vendor รายใดรายหนึ่ง แต่เกิดในหน้า AI client ที่ user เลือกเอง. เมื่อ Salesforce ที่ครองตลาด CRM อันดับ 1 ระดับโลกยังยอม "เปิดหลังบ้าน" ให้ Claude/Slack/Amazon Q เข้าถึง ทุก SaaS vendor ที่พึ่งพา UI stickiness ต้องเปลี่ยนแผนเร่งด่วน — ServiceNow, Workday, SAP, HubSpot, Zendesk ทุกเจ้าต้องเลือกเดินตามหรือดูตัวเองเป็น commodity data source

Pattern นี้เทียบได้กับ headless CMS เมื่อ 8 ปีก่อน: Contentful/Strapi/Sanity เกิดขึ้นเพราะ WordPress ไม่ยอม decouple frontend กับ backend. ตอนนี้ AIforce ทำแบบเดียวกันในระดับ enterprise stack — แต่ **Salesforce ยอม disrupt ตัวเองก่อน** ไม่ให้ startup กลุ่มใหม่ (Sierra, Decagon, Adept ใน enterprise agent tier) มาเป็น interface layer แข่ง. เกมนี้ Salesforce เดินก่อน 1-2 ปี ในขณะที่ Oracle/SAP ยังคิดในกรอบ vertical suite

ต่างจาก Agentforce 360 ที่ประกาศไปเมื่อวาน (ที่โฟกัสไปที่ **AI Control Plane** เรื่อง agent identity/policy/lifecycle) AIforce โฟกัสไปที่ **AI Interface Layer** — คำตอบของสองคำถามคนละคำถาม แต่ทั้งคู่คือ layer ใหม่ที่ Salesforce อยากยึดก่อน. รวมกันแล้ว Salesforce กำลังบอกว่า "เราไม่ใช่ CRM vendor แล้ว เราคือ OS ของ enterprise agent"

## มุม AI Agent Platform

**Builders** — ถ้ากำลังสร้าง vertical AI agent สำหรับ enterprise workflow ที่ต้องพึ่งข้อมูล CRM: ต่อไปคุณต้องรองรับ AIforce ผ่าน MCP เป็น minimum. Startup ที่คิดจะสร้าง "Slack for AI + CRM" ตัวใหม่ต้องคำนวณใหม่ว่าจะ differentiate ยังไงเมื่อ Slack เองมี Salesforce context in-line. **Users / business** — ทีมที่ใช้ Salesforce Enterprise/Unlimited อยู่แล้วและมี AE บอกให้ upgrade ควรถามเรื่อง Claudeforce/Slackforce roadmap ก่อนต่อสัญญาปีหน้า; ทีมไทย (SCB / KBank / DTAC / AIS / เมเจอร์) ที่พนักงานใช้ Slack + Salesforce วันละ 8 ชม. จะได้ productivity boost ที่ชัดเจนวัดได้ในไตรมาสแรกหลัง deploy. **Ecosystem** — Anthropic ได้ moat เพิ่มจาก Claudeforce (37 skills + 40 Claude Code skills = pre-built enterprise integration ที่ OpenAI ยังไม่มี); Slack เป็น "UI-of-record" ของ Salesforce data โดยไม่ต้องซื้อของ Salesforce; Microsoft Copilot / Google Gemini Enterprise เดินอยู่ในเลนเดียวกันแต่ยังเป็น walled garden ของตัวเอง — AIforce เปิดกว้างกว่า อันนี้เป็นตัวเปลี่ยน narrative ตลาด

## Sources
- [Salesforce announces AIforce, unlocking the power of its platform using composable agents — SiliconANGLE](https://siliconangle.com/2026/09/15/salesforce-announces-aiforce-unlocking-the-power-of-its-platform-using-composable-agents/)
- [Salesforce Launches AIforce at Dreamforce '26: 'AI Replaces the UI' — Salesforce Ben](https://www.salesforceben.com/salesforce-launches-aiforce-at-dreamforce-26-ai-replaces-the-ui/)
- [Salesforce Unveils AIforce, Bringing the Full Power of Its Platform to Any Interface — Salesforce Newsroom](https://www.salesforce.com/uk/news/stories/aiforce-announcement/)
- [Salesforce wants enterprises to 'break free of a shared user interface' with AIforce — IT Pro](https://www.itpro.com/technology/artificial-intelligence/salesforce-wants-enterprises-to-break-free-of-a-shared-user-interface-with-aiforce)

---

## Audio script
เรื่องเช้านี้เป็นข่าวใหญ่ที่สุดของ Dreamforce ปีนี้ครับ. Salesforce เปิดตัว AIforce ที่ Marc Benioff เรียกว่า interface revolution. หัวใจของมันคือ Salesforce ยอมรับว่าพนักงานไม่ได้อยากเปิดหน้าจอ Salesforce ทำงานอีกต่อไป เขาอยากทำงานใน Claude, ใน Slack, ใน Amazon Q, ใน Gemini Enterprise. AIforce เลยเอาข้อมูล CRM, business logic, permissions ของ Salesforce ไปวางไว้ในทุกที่ที่คนเปิดอยู่แล้ว. ตัวแรกที่ launch คือ Claudeforce มาพร้อม 37 sales skills ที่ Deloitte, GitLab, Legora ทดลองใช้แล้ว. ตัวที่สองคือ Slackforce — Hotel Engine บอกว่าใช้จัดการลูกค้าปีละ 800,000 รายการ. ตัวที่สามคือ Agentforce Coworker AI teammate ใน Lightning. ที่น่าสนใจคือ AgentExchange launch partner มี Anthropic, AWS, Google, Docusign, OpenAI ครบเลย. Signal คือ Salesforce ยอม disrupt ตัวเองก่อนที่ startup อย่าง Sierra หรือ Decagon จะขึ้นมาเป็น interface layer แทน. ทีมไทยที่ใช้ Salesforce + Slack ควรถาม AE เรื่อง Claudeforce roadmap ก่อนต่อสัญญาปีหน้าครับ.
