---
date: 2026-08-25
slug: salesforce-agentic-enterprise-index-13-agents-1-9-days
topic: use-case
reading_time_min: 4
sources: 3
image_prompt: |
  A wide editorial isometric illustration of a bustling glass office tower.
  Three giant floating stat cards fill the sky: card one reads
  "5 to 13 AGENTS" with an upward arrow, card two reads "1.9 DAYS TO DEPLOY"
  above a shrinking hourglass, card three reads "4X RETAIL GROWTH" with a
  rising bar chart. Tiny agent icons stream out of a big blue cloud labeled
  "Agentforce" and dock into rows of glowing office cubicles. A small
  Salesforce cloud pin at the corner; deep navy, teal, and amber palette;
  chunky sans-serif labels readable at 200px thumbnail; 1:1 aspect ratio;
  no real human faces.
image: images/26-08-25-0615-03-salesforce-agentic-enterprise-index-13-agents-1-9-days.png
---

# Salesforce Agentic Enterprise Index — 5 → 13 agents/ลูกค้าใน 14 เดือน, deploy เฉลี่ย 1.9 วัน

## TL;DR
- Salesforce ปล่อย Agentic Enterprise Index ฉบับ 2 (n=**4,689** respondent + aggregated Agentforce telemetry): ลูกค้าเฉลี่ยมี agent activated **5 ตัวใน ก.พ. 2025 → 13 ตัวใน เม.ย. 2026** (compound monthly growth 7%)
- Median time to deploy 1 agent = **1.9 วัน** — retailer ที่รัน agent ช่วง holiday shopping 2025 โต **4× เทียบ peer** ที่ไม่ใช้
- Slackbot สำหรับ user เฉลี่ย **68 session/สัปดาห์** ตั้งแต่ GA ก.พ. 2026 — สวนตัวเลข "9-14% ship" ที่หลาย analyst report ทั่วไป

## เกิดอะไรขึ้น
วันที่ 10 ส.ค. 2026 Salesforce ปล่อย Agentic Enterprise Index ฉบับที่ 2 — combined survey ของ 4,689 respondent จาก IT/business leader ทั่วโลก ผสมกับ aggregated telemetry จริงของ Agentforce ที่วิ่งอยู่ในลูกค้าจำนวนหลักพัน report เขียนขึ้นเพื่อสวน narrative "AI agent hype แต่ deploy ไม่จริง" ที่ระบาดหนักตั้งแต่ Gartner ออกตัวเลข "40% ของโครงการ agentic AI จะถูกยกเลิกภายในปี 2027" เมื่อเดือน มิ.ย.

ตัวเลขที่ตั้งใจให้เห็นก่อนอื่น: ลูกค้า Salesforce เฉลี่ยมี agent activated **5 ตัวในเดือน ก.พ. 2025 → 13 ตัวในเดือน เม.ย. 2026** — compound monthly growth 7% ต่อเนื่อง 14 เดือน (ตัวเลขนี้คือ agent per average customer ไม่ใช่ total agent ในระบบ) **Median time to deploy 1 agent อยู่ที่ 1.9 วัน** ซึ่งเทียบกับตัวเลขปี 2024 ที่ AI project เฉลี่ย 6-9 เดือนก่อนขึ้น production ถือเป็น deployment velocity ที่ผิดปกติ

ที่แหลมกว่านั้นคือ economic impact ของ retail vertical — retailer ที่ใช้ Agentforce ตลอด holiday shopping season ปี 2025 (Black Friday → New Year) โต **4 เท่าของ peer** ที่ไม่ใช้ Salesforce ไม่เปิด absolute number แต่ context คือ US retail อีคอมเมิร์ซโต ~7-9% ช่วง holiday แปลว่า Agentforce user ทำเกิน 25% growth ในช่วงเดียวกัน สำหรับ Slack Agentforce ที่ GA ในเดือน ก.พ. 2026 usage เฉลี่ย **68 session/สัปดาห์ต่อ user** — ไม่ใช่ user เปิด once-a-month แล้วลืม

## ทำไมสำคัญ
ตัวเลขนี้ทำ 2 อย่างพร้อมกัน: ประกาศ moat ของ platform play, และเปลี่ยน conversation ในตลาด สำหรับ moat — Salesforce มี CRM data, workflow, และ identity ของลูกค้าอยู่แล้ว การเสียบ agent layer ทับลงไปทำให้ time-to-value ลดลงเหลือหลักวัน ไม่ใช่หลักเดือน เทียบกับ startup ที่ต้อง integrate ระบบ 3-5 ตัวก่อน agent ทำงานได้จริง 1.9 วันคือตัวเลขที่ยากมากที่จะแข่ง

สำหรับ conversation — report นี้เป็น counter-weight ที่ CIO เอาไปใช้ป้องกัน budget cut ได้ ตั้งแต่กลางปี 2026 board room ทั่วไปเริ่มถาม "ทำไม AI project เรายังไม่ ROI" report ของ Salesforce ให้ตัวเลขว่ามี pattern ที่ ship แล้วขายได้จริง (retail 4× growth, Slack 68 session/week) ต่างกับ narrative ของ Gartner/McKinsey ที่กลาง ๆ ว่า pilot ตายเยอะ

ต้องเตือนสักครั้ง: number ทุกตัวมาจาก Salesforce เอง เป็น "vendor-reported" ไม่ใช่ third-party audit — sample bias มีแน่ (ลูกค้า Salesforce ที่ล้มเหลวจะไม่ตอบ survey) และ compound monthly growth 7% ต่อเนื่อง 14 เดือนคือ pattern ของ early adopter ที่ยัง scale ไม่ hit ceiling ยัง สิ่งที่ต้องดูต่อคือ retention curve ปีที่ 2 — agent 13 ตัวที่ activated จริง ๆ ยังใช้อยู่กี่ตัว

Signal ต่อจากนี้: Microsoft Copilot Studio, Google Workspace, HubSpot, ServiceNow จะต้อง release equivalent report ในไม่กี่เดือน ไม่งั้นเสียงจะเงียบเทียบ Salesforce — และ analyst จะเริ่มถามเลย platform บ้านไหน show number ระดับนี้ได้บ้าง

## มุม AI Agent Platform
สำหรับ **builders** ที่ทำ agent framework standalone: 1.9 วัน deploy คือกำแพงใหม่ที่ต้องไล่ตาม ถ้า framework ยังต้อง config credential 5 ที่, wire workflow ใน orchestrator แยก, แล้วเทรน user อีก 2 สัปดาห์ก่อนได้ผลลัพธ์แรก — โอกาสชนะ Salesforce ใน enterprise account ที่ commit ecosystem อยู่แล้วน้อยลงมาก path ที่ยังเปิดคือ vertical ที่ Salesforce ไม่ครอบ (manufacturing shop floor, healthcare clinical workflow, government casework) หรือ SMB ที่จ่าย Salesforce ไม่ไหว

สำหรับ **users/business** ที่ deploy agent ใน workflow: ตัวเลข 68 session/สัปดาห์ต่อ user คือ signal ว่า agent ต้องอยู่ในที่ที่ user "อยู่แล้ว" — Slack, Teams, email — ไม่ใช่ portal แยกที่บังคับให้ user เปิดเข้าไปใช้ สำหรับลูกค้า Thai SME ที่ Enabridge เข้าไปคุย argument จะเป็น "อย่าเริ่มด้วยการสร้าง agent app แยก — เสียบเข้า tool ที่ทีมใช้ทุกวันก่อน" LINE OA, Google Workspace, Notion ของ user คือ deployment surface

สำหรับ **ecosystem** (system integrator, boutique AI shop): pattern การชนะจะเปลี่ยน — 12 เดือนถัดไป enterprise deal ที่ใหญ่ที่สุดจะเป็น "expansion" ไม่ใช่ "new deploy" คือช่วยลูกค้าที่ใช้ Agentforce/Copilot Studio/Gemini Enterprise อยู่แล้วขยายจาก 5 agent เป็น 30-50 agent ที่ครอบ workflow เชิงลึกกว่านั้น boutique ที่รู้ workflow ของ vertical (freight, wealth management, hospital operation) จะเป็น layer ที่ hyperscaler suite ยังเข้าไม่ถึง — value ของ Ode + Casper Studios deal เมื่อสัปดาห์ก่อนคือ pattern นี้เป๊ะ

## Sources
- [Agentic Enterprise Index — Salesforce](https://www.salesforce.com/agentforce/agentic-enterprise-index/)
- [Second Agentic Enterprise Index Insights 2026 — Salesforce Newsroom](https://www.salesforce.com/news/stories/agentic-enterprise-index-insights-2026/)
- [Salesforce Agentic Enterprise Index shows agent deployments double in 2026 — Enterprise DNA](https://enterprisedna.co/resources/news/salesforce-agentic-enterprise-index-agent-deployments-double-2026/)

---

## Audio script
วันนี้ Salesforce ปล่อย Agentic Enterprise Index ฉบับที่ 2 ครับ เป็น combined report ของ survey 4,689 respondent กับ telemetry จริงจาก Agentforce

ตัวเลขที่แรงที่สุด ลูกค้า Salesforce เฉลี่ยมี agent activated 5 ตัวในเดือนกุมภาพันธ์ปีที่แล้ว โตเป็น 13 ตัวในเดือนเมษายนปีนี้ compound monthly growth 7% ต่อเนื่อง 14 เดือน median time to deploy 1 agent อยู่ที่ 1.9 วัน ซึ่งเทียบกับ AI project ยุคก่อนที่ใช้ 6-9 เดือนถือเป็นการเปลี่ยนกฎ

ที่หนักกว่านั้นคือ retailer ที่ใช้ Agentforce ช่วง holiday shopping ปีที่แล้วโต 4 เท่าของ peer ที่ไม่ใช้ และ Slack Agentforce ที่ GA เดือนกุมภาพันธ์ user เปิดเฉลี่ย 68 session ต่อสัปดาห์ ไม่ใช่ใช้ครั้งเดียวแล้วลืม

ต้องระวังไว้ว่าตัวเลขทั้งหมดเป็น vendor-reported ของ Salesforce เองไม่ใช่ third-party audit แต่ signal คือ platform ที่มี data workflow กับ identity อยู่แล้วมี moat ที่ standalone framework ตามยาก 12 เดือนถัดไปเราจะเห็น Microsoft Copilot Studio กับ Google Workspace ปล่อย equivalent report มาแข่งครับ
