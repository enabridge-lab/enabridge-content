---
date: 2026-10-20
slug: workday-sana-agent-harness-home
topic: openbridge-trend
reading_time_min: 3
sources: 3
image_prompt: |
  A sleek enterprise office control room, editorial isometric style, with
  a central glowing hub labeled "SANA" surrounded by three satellite panels
  reading "HR", "FINANCE", "IT". A thick cable rail at the base shows
  destination logos: Claude, Gemini Enterprise, Microsoft Copilot, Slack,
  Teams. A standing frame on the side displays bold text "AGENT HARNESS"
  with a padlock icon and a sandbox outline. Deep navy background, warm
  amber accents, high-contrast typography readable at 200px thumbnail.
  1:1 aspect, no real human faces, silhouette-only extras.
image: images/26-10-20-0607-01-workday-sana-agent-harness-home.png
---

# Workday ยก Sana ขึ้นเป็น "หน้าบ้าน" ของทั้งองค์กร — เปิด Agent Harness ให้ลูกค้าสร้าง agent บน data ของตัวเอง

## TL;DR
- ที่งาน Workday Rising เมื่อ 13 ต.ค. 2026 Workday ประกาศให้ **Sana** กลายเป็น Workday Home ตัวใหม่ — เป็น agentic interface ที่ "ปิดงานให้" ไม่ใช่แค่ตอบคำถาม — และเปิด **Agent Harness** ให้ลูกค้าสร้าง agent ของตัวเองบน HR/finance data ใน sandbox แยก
- Sana จะไปอยู่ใน Claude, Gemini Enterprise, Microsoft Copilot, Teams, Slack — Workday เลือกไม่สู้ที่ชั้น chat interface แต่สู้ที่ชั้น "ของจริง" คือ system of record
- Pricing อยู่ใต้ Flex Credits (consumption-based) — ไม่ใช่ per-seat — ซึ่งเป็นสัญญาณ pricing model ใหม่ของ enterprise agent

## เกิดอะไรขึ้น
ที่ Workday Rising เมื่อวันที่ 13 ตุลาคม 2026 Workday ประกาศเลิก "Workday Home" แบบเดิมที่เป็น dashboard ของ widgets แล้วเอา **Sana** — AI startup ที่ Workday ซื้อมาต้นปีนี้ — ขึ้นมาเป็น interface หลักขององค์กรแทน. Sana ไม่ใช่ chatbot ที่ตอบคำถามว่า "ลาป่วยยังเหลือกี่วัน" แล้วให้ user กดต่อเอง — มันเป็น agentic experience ที่รวม task, decision, meeting และ agent activity ไว้หน้าเดียว แล้ว "ปิดงานให้จบ" ตั้งแต่การขออนุมัติ expense ไปจนถึง onboarding พนักงานใหม่. ตามรายงานของ Constellation Research, Sana Home ตอนนี้ GA แล้วสำหรับลูกค้า Workday หลายราย โดยคิดเงินผ่าน Flex Credits consumption model ไม่ใช่ per-seat แบบ SaaS เดิม

ที่สำคัญกว่า Sana Home คือ **Agent Harness** — platform ที่ให้ลูกค้าเอา data ของตัวเองใน Workday มาสร้าง agent ขึ้นมาเอง รันใน isolated environment แบบ sandbox เพื่อให้ agent เข้าถึง HR และ finance data ได้โดยที่ยังอยู่ใน security, permissions และ audit framework เดิมของ Workday. Agent Harness มาพร้อม memory, guardrails, regional data controls, model choice (ไม่ล็อก model เดียว), evaluations และ step-by-step traces — เครื่องมือระดับที่ Builder เจอใน LangSmith หรือ LangGraph ตอนนี้มีให้ customer enterprise ใช้ตรงบนข้อมูลของตัวเอง

Workday เลือกไม่สู้ที่ chat interface. แทนที่จะทำแอป Workday AI ขึ้นมาสู้ Microsoft Copilot หรือ ChatGPT Enterprise, Workday ประกาศว่า Sana จะไปโผล่ "ทุกที่ที่พนักงานทำงาน" — Claude, Gemini Enterprise, Microsoft Copilot, Teams, Slack. ตัวอย่าง: Self-Service Agent ใน Microsoft 365 Copilot จบงานใน Workday โดยใช้ approval workflow และ business rule เดิมของบริษัท แล้วส่งผลลัพธ์กลับมาใน Copilot — user ไม่ต้องรู้ด้วยซ้ำว่าเบื้องหลังเป็น Workday

## ทำไมสำคัญ
นี่คือการประกาศวาง stance ที่ชัดที่สุดของ enterprise SaaS รุ่นเก่าในยุค agent — Workday บอกว่าตัวเองไม่ใช่ "แอป" อีกต่อไป แต่เป็น **data layer + policy layer + agent runtime** ที่ agent จาก Claude หรือ Gemini จะต้องเรียกเพื่อทำงานกับ HR/finance ของบริษัท. Pattern นี้เห็นมาก่อนที่ Salesforce (Agentforce), ServiceNow (AI Agents), SAP (Joule) — แต่ Workday ทำได้ชัดและกล้ากว่า เพราะยอมปล่อย interface ให้ไปอยู่กับ agent ของคนอื่น (Claude, Gemini Copilot) โดยที่ตัวเองรับ monetization ผ่าน consumption credits แทน seat

Pricing model เป็นประเด็นใหญ่ที่คนไม่ค่อยพูด — Flex Credits เป็นการเดิมพันว่า agent จะใช้ data ของ Workday ถี่มากพอจนรายได้ consumption สูงกว่า per-seat เดิม. ถ้าเดิมพันถูก มันคือ moat ที่ competitors ยากตาม เพราะ data gravity + policy inheritance อยู่กับ Workday อยู่แล้ว. ถ้าเดิมพันผิด Workday จะกลายเป็น "ท่อน้ำ" ที่ agent คนอื่นใช้ฟรี ๆ

## มุม AI Agent Platform
สำหรับ **Builders** — Agent Harness เป็นสัญญาณชัดว่า enterprise agent runtime ไม่ได้ขายในฐานะ generic framework (LangGraph, CrewAI, AutoGen) อีกต่อไป — แต่ขายในฐานะ "framework ที่ผูกกับ data + policy ของ system of record". ถ้าคุณสร้าง horizontal framework ตอนนี้ ต้องตอบให้ได้ว่าทำไมลูกค้า enterprise ต้องเลือกคุณแทน Agent Harness ของ Workday / Agentforce ของ Salesforce. สำหรับ **Users/business** — ถ้าใช้ Workday อยู่ สิ่งที่ควรทำคือลอง pilot Sana ผ่าน Flex Credits ก่อนที่ CFO จะได้ยินตัวเลข consumption แล้วตกใจ — เลือก use case ที่วัด cost saved ได้ชัด (expense approval, time-off, onboarding ticket) แล้วเทียบกับ cost ปัจจุบัน. สำหรับ **Ecosystem** — Anthropic และ Google ได้ประโยชน์ชัด ๆ เพราะ Workday ยอมเปิด Sana เข้าไปใน Claude และ Gemini Enterprise — เท่ากับว่าสองรายนี้ได้ "ปลั๊ก" ที่ตรงเข้า HR/finance data ของลูกค้า Workday ทั่วโลกฟรี ๆ ซึ่งเป็น strategic win ที่ Microsoft Copilot เคยผูกขาด

## Sources
- [Sana Is the New Workday Home: A Dynamic Agentic Experience Built to Finish the Work, Not Just Answer Questions](https://newsroom.workday.com/2026-10-13-Sana-Is-the-New-Workday-Home-A-Dynamic-Agentic-Experience-Built-to-Finish-the-Work,-Not-Just-Answer-Questions)
- [Workday to Bring Sana Everywhere Employees Work, Including Claude, Gemini Enterprise, Microsoft Copilot, Slack, and Teams](https://newsroom.workday.com/2026-10-13-Workday-to-Bring-Sana-Everywhere-Employees-Work,-Including-Claude,-Gemini-Enterprise,-Microsoft-Copilot,-Microsoft-Teams,-and-Slack)
- [Workday makes Sana its interface, launches Agent Harness, decision and work intelligence](https://www.constellationr.com/insights/news/workday-makes-sana-its-interface-launches-agent-harness-decision-and-work)

---

## Audio script
วันนี้ Workday ประกาศเรื่องที่ใหญ่กว่าที่ข่าวพาดหัว. ที่งาน Workday Rising เมื่อสัปดาห์ที่แล้ว เขาเลิก Workday Home แบบเดิม — ที่เป็น dashboard มี widget เต็มไปหมด — แล้วเอา Sana ซึ่งเป็น AI ที่ซื้อมาต้นปี มาเป็นหน้าบ้านใหม่ของทั้งองค์กร. Sana ไม่ใช่ chatbot ที่ตอบคำถามแล้วให้คุณกดต่อเอง — มันปิดงานให้จบตั้งแต่ขอ expense จนถึง onboarding พนักงาน. ที่น่าสนใจกว่าคือ Workday เปิดของใหม่ชื่อ Agent Harness — ให้ลูกค้าเอา data HR และ finance ของตัวเองในระบบ Workday มาสร้าง agent ขึ้นมาเองได้ รันอยู่ใน sandbox แยก มี guardrail มี audit มี model choice — เหมือนให้ enterprise ทำ LangGraph บนข้อมูลของตัวเอง. และสิ่งที่กล้าที่สุดคือ Workday บอกว่า Sana จะไปอยู่ใน Claude, Gemini Enterprise, Microsoft Copilot, Teams, Slack — ไม่สู้ที่ chat interface แต่สู้ที่ data layer. เขาเปลี่ยน pricing เป็น Flex Credits แบบ consumption ไม่คิดเป็น seat อีกต่อไป. ความหมายคือ enterprise SaaS ยอมรับแล้วว่าในยุค agent มันคือ pipe ที่ agent ของคนอื่นจะเรียกใช้ — รายได้มาจาก data gravity ไม่ใช่ interface
