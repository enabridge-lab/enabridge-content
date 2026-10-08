---
date: 2026-10-08
slug: 26-10-09-0615-01-google-gemini-agent-work
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial hero: a towering glass office tower sliced open to reveal a glowing
  "GEMINI AGENT" nerve center at its core, with four stacked memory shelves
  labeled "SESSION", "SEMANTIC", "PROCEDURAL", "EPISODIC". Mini sub-agent
  silhouettes with tiny envelope badges orbit the tower, each wearing a mail
  tag like "coworker@acme.com". Satellite logo plates reading "SALESFORCE",
  "SERVICENOW", "JIRA", "SNOWFLAKE", "BIGQUERY", "MICROSOFT 365", "SLACK"
  dock into the building. A bold banner at the bottom reads
  "ONE PROMPT. DAYS OF WORK." Isometric vector, Google blue + spectrum
  gradient + warm neutral grey, 1:1 aspect, no real human faces.
image: images/26-10-09-0615-01-google-gemini-agent-work.png
---

# Google เปิด "Gemini agent" — universal agent ที่คุณสั่งเป้าหมาย แล้วมันคิดวางแผน, สร้าง sub-agent, และทำงานต่อแม้ปิดจอ

## TL;DR
- Google Cloud เปิดตัว **Gemini agent** วันที่ 8 ต.ค. 2026 ที่งาน Gemini at Work — "universal agent for work" ที่รับ **objective** ไม่ใช่ step-by-step แล้ววางแผนเอง, เขียน-รันโค้ด, สร้าง "coworker agent" ที่มีอีเมล + storage ของตัวเอง
- Agent รันบน cloud → ไม่ต้องเปิด laptop ก็ทำงานต่อหลายชั่วโมงหรือหลายวัน; job ใหญ่จะ spin up sub-agent (แต่ละตัวมี identity แยก) และต่อ Salesforce / ServiceNow / Jira / Snowflake / BigQuery / Microsoft 365 / Slack
- Memory เป็น 4 ชั้น: **session / semantic / procedural / episodic** — ตัว agent เขียน skill ของตัวเองเก็บเป็น procedural memory เพื่อ reuse ครั้งต่อไป. Gemini แตะ **950M monthly users** และกำลังไล่ ChatGPT

## เกิดอะไรขึ้น

วันที่ 8 ตุลาคมที่งาน **Gemini at Work 2026**, Google Cloud เปิดตัว **Gemini agent** ซึ่ง blog ของ Google เรียกว่า "universal agent for work". ประเด็นหลักคือเลิก paradigm "chatbot ตอบ prompt" ไปสู่ "agent รับ objective" — ผู้ใช้พิมพ์ *เป้าหมาย* ปลายทางเข้าไป (ไม่ใช่ขั้นตอน) แล้ว agent plan steps เอง, เขียน-รันโค้ด, และเรียก tool/app ตามจำเป็น ภายใน prompt box เดียว

ความแตกต่างสำคัญคือ **persistence**. Agent รันบน cloud ไม่ใช่ laptop — ปิดจอ ปิดเครื่อง มันก็ทำงานต่อ. ตามรายงาน VentureBeat งานที่ใช้ **หลายชั่วโมงหรือหลายวัน** จะยังทำงานต่อแม้ไม่มีคนดู; job ใหญ่ Gemini agent จะ **spin up sub-agent ชั่วคราวแยกตัว** ที่มี identity ของตัวเอง เพื่อแบ่งงานออกเป็นชิ้นเล็ก ตามแบบ multi-agent orchestration. Google ยังเปิดเรื่อง **"coworker agent"** — persistent agent ที่ทีมสร้างได้ มี **อีเมล, storage และ role** ของตัวเอง (เช่น "finance-reporter@acme.com" ที่สมาชิกทีมส่งคำสั่ง, cc งานได้)

Memory system เป็นชั้นที่ชัดเจนที่สุดของสถาปัตยกรรมใหม่. 9to5Google อธิบายว่า Gemini agent เก็บ 4 memory types: **session memory** (งานปัจจุบัน), **semantic memory** (จาก document + interactions), **procedural memory** (วิธีทำงาน — รวม skill ที่ agent เขียนให้ตัวเองเพื่อ reuse), และ **episodic memory** (past actions). ทั้งหมด sync ใน single personalization graph บน cloud. Agent ต่อ **Salesforce, ServiceNow, Jira, Snowflake, BigQuery** และฝั่ง productivity **Gmail, Drive, Docs, Sheets, Slides, Chat, Calendar, Slack, Microsoft 365**. บางสำนัก (Xenospectrum) รายงานว่า Gemini agent สลับ model ระหว่าง Gemini กับ **Claude** ตามงาน — แต่สำนักอื่นยังไม่ยืนยัน

Google ยังไม่ลงรายละเอียด pricing / rollout timeline เต็มใน embargoed material, และ VentureBeat สังเกตว่ายังไม่ชัดว่า admin จะ **selectively enable/disable** component ย่อยอย่างไร — เป็นประเด็น governance ที่ CIO ต้องจับตา

## ทำไมสำคัญ

นี่คือ **อนาคตที่ Oracle Fusion Claw พูดถึงเมื่อสัปดาห์ก่อน แต่ Google ปล่อยในรูปแบบ horizontal** — ไม่ใช่ runtime ของ ERP ตัวเดียว แต่เป็น runtime สำหรับทุก knowledge worker ที่ใช้ Gmail/Workspace อยู่แล้ว. Pattern เดียวกัน: **แยก reasoning (model) ออกจาก execution (long-running cloud runtime)** พร้อม memory + identity + tool graph. ความต่างคือ Google มี distribution 950M MAU พร้อม install base ของ Workspace ทั่วองค์กร — Oracle มี 75 Fusion apps, Google มี Gmail

**Coworker agent ที่มีอีเมลของตัวเอง** คือ UX win ขนาดใหญ่. Agent ไม่ใช่ "ปุ่มใน sidebar" อีกต่อไป — มันเป็น teammate ที่มีกล่อง inbox, มี role, มีประวัติ. ทีม HR ตั้ง "candidate-screener@" ให้ส่ง resume ไปได้; sales ตั้ง "deal-updater@" ที่คอยอัพเดต CRM ตามอีเมลที่ลูกค้า cc มา. UX pattern นี้แก้ปัญหาใหญ่ที่ copilot กำลังเจอ: **คนลืมใช้มันเพราะต้องเปิด app แยก**. ถ้า agent เป็นที่อยู่ email ปกติ มันเข้า workflow เดิมของทุกคนโดยอัตโนมัติ

Signal ที่ตามมาคือ Google เลือก **multi-vendor model routing** (ถ้ารายงาน Xenospectrum จริง — Gemini + Claude). นี่ขัดกับ walled garden ของ Microsoft/OpenAI ที่พยายามล็อก model stack ของตัวเอง. ถ้า agent runtime กลายเป็น commodity layer ที่สลับ model ได้ตามงาน, มูลค่าจะไปอยู่ที่ **memory graph + tool connectors + distribution** — ไม่ใช่ที่ model เอง. CIO ที่เห็นค่า token ของ Copilot โตเดือนละ 20% จะชอบ story นี้มาก

## มุม AI Agent Platform

**Builders** ที่สร้าง agent framework (LangGraph, Mastra, CrewAI, Pydantic AI) ต้องตอบสองคำถามเร็ว ๆ นี้: (1) framework ของคุณ **persist state ได้ข้ามวัน** หรือยัง? (2) support **sub-agent identity + email/webhook addressing** หรือยัง? ถ้ายัง — ทีม enterprise จะใช้ Gemini agent runtime ไม่ใช่ของคุณ. **Users/business** ที่ใช้ Google Workspace อยู่แล้วมี default option ใหม่ — ไม่ต้อง build "AI copilot" เอง, prompt box ใน Gmail/Drive/Docs จะ auto-upgrade เป็น Gemini agent. CIO ควรเริ่ม policy ตั้งแต่ตอนนี้: อะไรที่ coworker agent ทำได้ ไม่ได้ (ส่งเงิน? approve PR? merge pull request?) และใครเป็น "manager" ของ agent (owner, team, department). **Ecosystem:** Slack / Jira / ServiceNow ได้ประโยชน์เพราะกลายเป็น "ที่ทำงาน" ของ agent; MCP standard ยิ่งสำคัญกว่าเดิมเพราะ Gemini agent รองรับ MCP server เต็มรูปแบบ. Microsoft Agent 365 ต้องตอบด้วย "coworker email" ของตัวเอง — ไม่งั้น narrative ว่า Copilot = agent จะเริ่มสั่นคลอน

## Sources
- [Google Cloud introduces the Gemini agent — Google blog](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gemini-at-work/)
- [Google Cloud announces 'Gemini agent' as 'universal agent for work' — 9to5Google](https://9to5google.com/2026/10/08/gemini-agent-google-cloud/)
- [Google launches Gemini AI workplace agent that can write code and run tasks — CBS News](https://www.cbsnews.com/news/google-gemini-ai-workplace-agent/)
- [Google Cloud unveils persistent Gemini Agents for long-running tasks — VentureBeat](https://venturebeat.com/orchestration/google-cloud-unveils-persistent-gemini-agents-for-long-running-tasks-and-they-get-their-own-gmail-calendar-and-drive-storage)
- [Google Cloud Unveils Gemini Agent — Xenospectrum](https://xenospectrum.com/en/gemini-agent-enterprise-coworker-memory/)

---

## Audio script
วันที่ 8 ตุลาคม Google Cloud เปิดตัว Gemini agent ที่งาน Gemini at Work. ตัวนี้คือ universal agent สำหรับคนทำงาน. ประเด็นคือเลิกเขียน prompt แบบขั้นตอน แล้วเขียน objective เป้าหมายไปแทน. Agent จะวางแผน รันโค้ด เรียก tool เอง ภายใน prompt box เดียว. ที่พิเศษคือมัน persist. Agent รันบน cloud ไม่ใช่ laptop. ปิดเครื่องปิดจอก็ทำงานต่อหลายชั่วโมงหรือหลายวัน. งานใหญ่มัน spin up sub-agent มี identity ของตัวเองแยก. Google เปิด concept coworker agent persistent agent ที่ทีมสร้างได้ มีอีเมล storage role ของตัวเอง. เช่น ตั้ง finance reporter at acme.com แล้วสมาชิกทีมส่งคำสั่งทาง email ได้เลย. Memory มี 4 ชั้น session semantic procedural episodic. Procedural คือ skill ที่ agent เขียนให้ตัวเองเก็บไว้ reuse ครั้งต่อไป. ต่อ Salesforce ServiceNow Jira Snowflake BigQuery Gmail Microsoft 365 Slack. UX pattern coworker email ใหญ่มาก เพราะ agent ไม่ใช่ปุ่มใน sidebar อีกต่อไป เป็น teammate ที่มี inbox มี role. แก้ปัญหาคนลืมใช้ copilot. Pattern เดียวกับ Oracle Fusion Claw แยก reasoning ออกจาก execution. แต่ Google ทำแบบ horizontal สำหรับทุก knowledge worker บน distribution 950 ล้าน user ต่อเดือน
