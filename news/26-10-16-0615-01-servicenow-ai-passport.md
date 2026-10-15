---
date: 2026-10-16
slug: servicenow-ai-passport
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: |
  A sleek border-control checkpoint inside a glass server hall; a glowing
  passport labeled "AI PASSPORT" sits on a scanner, with three stamps
  beside it: "SCOPE", "OWNER", "KILL". In the background a holographic
  robot agent waits in line while a red "DRIFT DETECTED" badge pulses on
  a wall screen. Editorial isometric illustration, deep teal and amber
  palette, 1:1 aspect, no real human faces.
image: images/26-10-16-0615-01-servicenow-ai-passport.png
---

# ServiceNow AI Passport: agent governance กลายเป็น infrastructure layer

## TL;DR
- ServiceNow เปิดตัว **AI Passport** วันที่ 15 ต.ค. — signed credential ที่ผูกกับ agent หรือ MCP server แต่ละตัว บอก scope + accountable owner + action ที่ทำได้
- Runtime control ยิง kill-switch ตัด agent ที่ **drift ออกนอก scope** แบบ real-time ไม่ต้องรอให้ incident response ไล่หา
- ขยายต่อจาก **AI Control Tower** ที่เปิดใน Knowledge 2026 — ServiceNow เลือก repositioning ตัวเองเป็น "AI governance platform" มากกว่า workflow ITSM

## เกิดอะไรขึ้น

เมื่อเช้าวันพฤหัสที่ 15 ต.ค. ServiceNow ประกาศ AI Passport เป็นส่วนหนึ่งของ "operational harness" รอบใหม่ ซึ่งเป็นระบบ enterprise control plane สำหรับ AI agent ทุกตัวในองค์กร — ไม่ว่าจะเป็น agent ของ ServiceNow เอง, agent ของ third-party vendor, หรือ MCP server ที่ host โดยทีมภายใน ทุกตัวต้องมี passport ที่ลงลายเซ็น ประกอบด้วยรายการ action, scope ของ data, และ owner ที่รับผิดชอบ ถ้า agent เริ่ม call tool ที่ไม่ได้อยู่ใน passport หรือเรียก data นอก scope ระบบ terminate agent instance นั้นทันที

Reuters รายงานว่า ServiceNow positioning ให้ feature นี้เป็น "layer underneath whatever agent framework you already use" — คือไม่ได้ขายให้ทีมเปลี่ยน runtime มาใช้ ServiceNow แต่ให้มาเสียบ instrumentation เพิ่ม นี่คือการต่อยอดโดยตรงจาก AI Control Tower ที่เปิดในงาน Knowledge 2026 เมื่อพฤษภาคม ที่ตอนนั้นทำได้แค่ monitor five dimensions (compliance, cost, performance, security, usage) — AI Passport คือการเติม enforcement เข้าไปในสาย monitor นั้น

ที่น่าสังเกตคือ ServiceNow เขียน MCP server เข้าไปใน spec ของ passport ด้วย — ไม่ใช่แค่ agent runtime หมายความว่าเวลาองค์กร deploy MCP server ไว้ให้ agent เรียก (เช่น Slack MCP, Jira MCP, internal database MCP) MCP server ตัวนั้นก็ต้องมี passport ของตัวเองด้วย เท่ากับ ServiceNow กำลังพยายามเป็น identity provider สำหรับทั้ง agent และ tool layer

## ทำไมสำคัญ

Agent governance เริ่มเป็นปัญหาจริงเมื่อปลายปี 2025 ที่ Salesforce, Microsoft, Google แต่ละราย push agentic AI เข้า production — IT shadow deployment เริ่มเกิดเพราะ developer ไหนก็ spin up agent + MCP server ขึ้นมาได้ Hyland เพิ่ง launch Agent Passport ของตัวเองเมื่อมิถุนายน และ cite สถิติว่า 88% ของ AI agent fail ก่อนเข้า production เพราะ compliance หรือ permission issue แปลว่า market สำหรับ "agent identity layer" กำลังจะกลายเป็นหมวดใหม่

สิ่งที่น่าจับตาคือ pattern "control plane as a product" กำลังเลียนแบบวิวัฒนาการของ cloud platform เมื่อ 10 ปีก่อน — ตอนแรกทุกคนขาย compute (model, framework) แล้วค่อย ๆ ลงมาที่ orchestration (Kubernetes) ตอนนี้ที่ ServiceNow, Hyland, และ platform อย่าง Okta ลงมาเล่น "agent IAM" คือสัญญาณว่าการแข่งขันเริ่มย้ายจาก "ใครมี agent เก่งสุด" ไปที่ "ใคร verify agent ได้"

## มุม AI Agent Platform

สำหรับ **builder** ที่ขาย agent runtime หรือ MCP server นี่คือสัญญาณที่ชัดว่าต้อง expose metadata schema ให้ passport provider อ่านเข้ามา — ไม่งั้นลูกค้า enterprise จะเลือก vendor ที่ interop ได้ก่อน สำหรับ **business ที่ deploy agent** ปัญหาเดิมที่คุมไม่ได้ว่าใครในทีมสร้าง agent อะไรไว้บ้างกำลังจะมี enterprise answer — แต่ก็หมายความว่า cost ของ compliance จะเพิ่มเข้าไปใน TCO ด้วย

สำหรับ **ecosystem** โดยรวม ServiceNow คือ incumbent รายใหญ่ที่สุดที่กำลัง claim ตำแหน่ง governance layer ถ้า format passport ของ ServiceNow กลายเป็น de-facto standard เหมือน OIDC/SAML ของ identity ยุคก่อน vendor อื่น (รวมทั้ง Hyland และ Okta) จะต้องเลือกว่าจะ compat หรือจะ fork

## Sources
- [ServiceNow adds AI agent controls and employee automation tools](https://siliconangle.com/2026/10/15/servicenow-adds-ai-agent-controls-and-employee-automation-tools)
- [ServiceNow launches AI Passport for agent governance](https://investing.com/news/company-news/servicenow-launches-ai-passport-for-agent-governance-93CH-4951803)
- [Agent Passport: Why 88% of AI Agents Fail Before Production](https://www.beri.net/article/hyland-agent-passport-88-percent-ai-agents-fail-production-2026)

---

## Audio script
วันนี้ ServiceNow เปิดตัวสิ่งที่เรียกว่า AI Passport ตัวช่วย governance ของ AI agent ในองค์กร คอนเซ็ปต์ง่าย ๆ คือ agent ทุกตัว ไม่ว่าจะเป็นของ ServiceNow เองหรือของ vendor อื่น หรือแม้แต่ MCP server ที่ทีมภายในสร้างขึ้นมา ทุกตัวต้องมี passport ที่ลงลายเซ็น บอกว่าทำอะไรได้บ้าง เข้าถึง data ไหน และใครเป็นเจ้าของ ถ้า agent ตัวไหนเริ่ม drift ออกนอก scope ระบบ kill agent ตัวนั้นทันทีแบบ real-time

ที่สำคัญคือ ServiceNow เขียน MCP เข้าไปใน spec ด้วย ไม่ใช่แค่ agent runtime หมายความว่า tool layer ก็ต้องมี identity ของมันเองเหมือนกัน นี่คือการ reposition ตัวเองของ ServiceNow จาก workflow platform มาเป็น AI governance platform

ภาพรวมที่น่าสนใจคือ pattern นี้กำลังเลียนแบบ cloud platform สมัย 10 ปีก่อน ตอนแรกทุกคนขาย compute แล้วค่อย ๆ ลงมาที่ orchestration ตอนนี้ที่ ServiceNow Hyland และ Okta ลงมาเล่น agent IAM กันแล้ว แปลว่าการแข่งขัน agentic AI กำลังย้ายจากคำถามว่าใคร agent เก่งสุด ไปที่คำถามว่าใคร verify agent ได้ดีกว่า สำหรับทีม builder ของเรา ถ้ากำลังจะขาย agent หรือ MCP server เข้า enterprise รีบคิดเรื่อง metadata schema ที่ให้ passport provider อ่านได้ก่อน ไม่งั้นลูกค้าจะเลือก vendor ที่ interop ได้ก่อนเสมอ
