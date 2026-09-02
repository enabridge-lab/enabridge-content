---
date: 2026-09-03
slug: claudeforce-salesforce-anthropic-open-beta
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A cinematic editorial illustration of two massive stone temples labeled
  "SALESFORCE" and "ANTHROPIC" connected by a glowing bridge in the sky. On
  the bridge, giant floating tiles spell "37 SKILLS" and "OPEN BETA". A
  silhouetted sales rep walks across the bridge carrying a briefcase, leaving
  the Salesforce temple behind. Editorial isometric style, high contrast,
  gold-and-navy palette, 1:1 aspect, no real human faces.
image: images/26-09-03-0613-01-claudeforce-salesforce-anthropic-open-beta.png
---

# Claudeforce เปิด Open Beta กันยา 26 — Salesforce ยอมให้ CRM ตัวเองอยู่ใน Claude แทน UI ตัวเอง

## TL;DR
- **Salesforce + Anthropic** ประกาศ Claudeforce เมื่อ 26 ส.ค. 2026 — Salesforce in Claude เปิด **Open Beta ก.ย. 2026** พร้อม **37 pre-built sales skills**
- Anthropic Claude เป็น **default reasoning model** ใน Agentforce, Slack และ Salesforce dev tools ทั้งหมด
- AIforce (harness ฝั่ง Salesforce) ให้ agent เข้าถึง CRM ผ่าน **MCP servers + APIs + CLI** — เขียนบทเรียนใหม่ให้ทั้ง platform vendor ที่กลัว agent จะกินหน้าตัวเอง

## เกิดอะไรขึ้น
เมื่อ 26 ส.ค. Salesforce ประกาศ "Claudeforce" ร่วมกับ Anthropic — และสิ่งที่ทำให้ deal นี้ไม่เหมือน AI partnership ทั่วไปคือ **Salesforce ยอมให้ sales rep ทำงานทั้ง flow ใน Claude โดยไม่ต้องเปิด Salesforce UI อีกเลย** จุดกลางของประกาศคือ Salesforce in Claude — plug-in สำหรับ Claude Cowork ที่มาพร้อม 37 sales skill สำเร็จรูป ครอบตั้งแต่ meeting prep, deal health review, ไปจนถึง pipeline analysis. Pilot เปิดกับลูกค้าที่คัดเลือกแล้ว open beta ตามมาเดือน ก.ย. 2026 และ Salesforce บอกว่าจะทยอย ship skill เพิ่มถึงปลายปี

ฝั่งเทคนิค กลไกที่ทำให้ Claude "เข้า" CRM ได้ชื่อว่า **AIforce** — เป็น enterprise harness ของ Salesforce ที่ expose data + business rules ผ่าน MCP servers, APIs และ CLI tools. พูดง่ายๆ คือ Salesforce ยอม "เปิดกระเป๋า" ของตัวเองให้ agent จากค่ายอื่นเข้ามาใช้แบบ first-class. ในเวลาเดียวกัน Claude ก็กลายเป็น default reasoning model ของ Agentforce, Slack (Salesforce ซื้อมา) และ dev tools ของ Salesforce — คือ Anthropic แทรกลึกในทั้ง 3 surface ใหญ่ของ ecosystem นี้

VentureBeat พาดหัวได้แรงว่า "Salesforce just put its entire CRM inside Claude — and says you'll never need its app again" — และคำพูดนี้ไม่ใช่ hype ทั้งหมด เพราะถ้า agent ทำ meeting prep, update opportunity, log activity, forecast — 80% ของงาน sales rep ได้ใน chat, การ "เปิด" Salesforce web app ก็เหลือแค่ edge case จริงๆ

## ทำไมสำคัญ
Deal นี้เป็น **case study สดๆ ของ platform disintermediation ยุค agent** — ก่อนหน้านี้ทุก SaaS vendor รู้ว่า agent จะมาแทน UI แต่ไม่มีใครกล้ายอมเปิดตัวเองเป็น "backend สำหรับ agent ของคนอื่น" เพราะกลัวเสียหน้าและเสีย pricing power. Salesforce เลือกยอม ก่อนที่จะโดนบังคับ — ซึ่งเป็นการ bet ที่ตรงข้ามกับ Microsoft (บังคับให้ทุกอย่างวิ่งผ่าน Copilot). Marc Benioff ยอมให้ Claude เป็นหน้าบ้าน แลกกับการเป็น "system of record" ที่ agent ทุกตัวต้องมา query — เป็น pattern เดียวกับที่ Stripe เป็น payment infrastructure สำหรับ marketplace อื่น

signal ต่อไป: ถ้า Salesforce ทำได้ในระดับ pilot ให้เห็นตัวเลข retention/expansion จริง คู่แข่ง (HubSpot, ServiceNow, Workday) จะโดนกดดันให้เปิดของตัวเองในทำนองเดียวกันภายใน 6-12 เดือน. Anthropic ก็ได้ **enterprise distribution channel** ที่ไม่ต้องขายเอง — Salesforce มี Fortune 500 บนสัญญาอยู่แล้ว ทันทีที่ Claude กลายเป็น default model ในนั้น จำนวน seat ของ Claude ก็โตแบบ compounded

## มุม AI Agent Platform
สำหรับ **builders** — Claudeforce เป็น proof point ว่า pattern "SaaS as MCP server" มาแน่ ไม่ใช่แค่เล่นๆ. ถ้ากำลังสร้าง agent platform, การรอให้ vendor ปล่อย official MCP server จะกลายเป็น critical path — และคนที่ ship connector library ครบก่อน (Zapier-style สำหรับยุค agent) จะได้ทัน window นี้. สำหรับ **businesses ที่กำลัง deploy agent**, sales use case ของ Salesforce customer เพิ่งเปลี่ยนจาก "build เอง" เป็น "รอ open beta แล้ว configure" — cost ลด แต่ differentiation จาก vertical skill custom ก็เหลือน้อยลง ต้องคิดใหม่ว่า "moat" จะสร้างที่ layer ไหน

สำหรับ **ecosystem** — นี่คือ moment ที่ Anthropic ได้เดินหน้าไปหนึ่ง step สำคัญในการเป็น "OS-level agent" ของ enterprise (OpenAI ได้ Microsoft, Google ได้ Google Workspace, Anthropic ได้ Salesforce). สามยักษ์ AI ตอนนี้แต่ละคนจับ enterprise surface ต่างกันชัดเจน — เป็นการวาง chessboard ที่บริษัทไทยและ SME ควรเลือกฝั่งให้ตรงกับ stack ที่ใช้อยู่ แทนที่จะเลือกจาก benchmark

## Sources
- [Salesforce and Anthropic Announce Claudeforce](https://www.salesforce.com/news/press-releases/2026/08/26/salesforce-and-anthropic-announce-claudeforce/)
- [Salesforce just put its entire CRM inside Claude — VentureBeat](https://venturebeat.com/orchestration/salesforce-just-put-its-entire-crm-inside-claude-and-says-youll-never-need-its-app-again)
- [Claudeforce: 37 Sales Skills, Availability & How It Works — Project Monet](https://www.projectmonet.space/blog/claudeforce-salesforce-in-claude)

---

## Audio script
วันที่ 26 สิงหาที่ผ่านมา Salesforce กับ Anthropic ประกาศดีลที่ชื่อว่า Claudeforce ครับ เดือนกันยานี้เปิด open beta แล้ว. หัวใจของดีลคือ Salesforce ยอมให้ sales rep ทำงาน CRM ทั้ง flow อยู่ใน Claude โดยไม่ต้องเปิดหน้า Salesforce เลย มี 37 sales skill สำเร็จรูป ตั้งแต่ meeting prep ยันไล่ pipeline. ที่สำคัญคือ Claude เป็น default reasoning model ใน Agentforce, Slack และ dev tools ของ Salesforce ทั้งหมด. เทคนิคเบื้องหลังชื่อ AIforce — Salesforce เปิด data กับ business rules ผ่าน MCP server ให้ agent ค่ายอื่นมาใช้ได้แบบ first-class. เรื่องนี้สำคัญเพราะ Salesforce คือ SaaS vendor ใหญ่รายแรกที่ยอมเป็น backend ให้ agent คนอื่น — เดิมพันว่าเป็น system of record ยังจำเป็นอยู่ ถึงหน้า UI จะหายไป. คู่แข่งอย่าง HubSpot, ServiceNow น่าจะโดนกดดันตามภายใน 6 ถึง 12 เดือน. สำหรับคนที่สร้าง agent — pattern SaaS-as-MCP-server มาแน่แล้ว. สำหรับ business ที่ใช้ Salesforce อยู่ — เตรียมทดลอง open beta เดือนนี้ได้เลยครับ
