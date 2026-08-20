---
date: 2026-08-21
slug: resolve-agentlab-enterprise-orchestration-natural-language
topic: openbridge-trend
reading_time_min: 3
sources: 3
image_prompt: |
  A clean editorial illustration of a workshop bench where a designer sketches
  workflow arrows with a pencil, and the arrows glow into holographic agent
  icons hovering above server racks. A big label reads: "NATURAL LANGUAGE →
  AGENT", with three sub-labels: "REUSABLE SKILLS", "GOVERNANCE-AWARE",
  "PROD-READY". Style: editorial isometric, cream background, teal and
  amber accents, warm rim light. 1:1 aspect, no real human faces.
image: images/26-08-21-0612-04-resolve-agentlab-enterprise-orchestration-natural-language.png
---

# Resolve ปล่อย AgentLab next-gen — IT ops vendor 20 ปีต่อยอด runbook เป็น "natural-language agent factory"

## TL;DR
- Resolve (บริษัท IT process automation ที่เก่าแก่ 20+ ปี) ปล่อย AgentLab next-gen เมื่อ 17 ส.ค. — natural-language agent creation + reusable skills + governance-aware deployment
- Position ตัวเองเป็น "IT automation ที่ evolved เป็น agent platform" — ไม่ใช่ agent startup ที่ต้องเรียนรู้ enterprise ops
- Pattern เดียวกับ ServiceNow, UiPath, Automation Anywhere — RPA/ITSM vendor รุ่นเก่าเบียดขึ้นมาเป็น agent platform โดยใช้ runbook library ที่มีอยู่แล้วเป็น moat

## เกิดอะไรขึ้น

Resolve — vendor IT process automation ที่ทำ runbook + orchestration ให้ enterprise ตั้งแต่ยุค pre-cloud — ประกาศ next generation ของ AgentLab เมื่อ 17 ส.ค. บริษัทระบุว่า release ใหม่รวม natural-language agent creation, reusable skills library, AI-assisted workflow building, และ governance-aware deployment เข้าไว้ที่เดียว — ทีม IT/DevOps/SRE สร้าง agent จาก prompt ภาษาธรรมชาติแล้ว AgentLab แปลงเป็น workflow ที่ทดสอบและ deploy ได้บน production

Key feature ที่แตกต่างจาก agent framework ทั่วไป: "test agent behavior, roles, และ permission confidence ก่อน expand use" — เป็น testing harness สำหรับ agent ที่คล้าย CI/CD pipeline. Agent ตัวหนึ่งอาจถูกทดสอบใน sandbox 100 scenario ก่อนได้ permission เขียนไป production system. Reusable skills library ให้ engineer แชร์ capability ข้ามทีม (คล้ายกับที่ Anthropic เพิ่ง GA Skills ใน Claude Developer Platform — สอง vendor คนละ segment converge บน mental model เดียวกัน)

Resolve position AgentLab เป็น "IT automation ที่ evolved เป็น agent" ไม่ใช่ "agent startup ที่กำลังเรียนรู้ IT ops" — บริษัทเน้นว่า 20+ ปีของ runbook library, permission model, และ enterprise integration (ITSM, ServiceNow, JIRA, PagerDuty, Splunk) ยังคงอยู่, agent แค่เป็นทาง entry ใหม่ที่ non-programmer ใช้ได้

## ทำไมสำคัญ

Pattern ชัดขึ้นเรื่อย ๆ ในปี 2026: **RPA/ITSM vendor รุ่นเก่ากำลังเบียดขึ้นเป็น agent platform** โดยใช้สิ่งที่ agent startup ยังไม่มี — คือ enterprise footprint, compliance certification, และ library ของ workflow ที่ battle-tested. ServiceNow มี AI Agents, UiPath มี Agentic Automation, Automation Anywhere มี Automation Success Platform, Blue Prism มี Agentic Automation Foundation. ทั้งหมด launch/rebrand ในช่วง 12 เดือน — และ Resolve เพิ่งใหม่สุด

Move นี้กัดตลาดคู่ไปสองทาง. ทาง (1) startup agent orchestration (Warp Factories, Cognition, Adept ในอดีต) โดนแข่งจาก vendor ที่ enterprise เชื่อใจอยู่แล้ว. ทาง (2) generic agent framework (LangChain, CrewAI) ต้องอธิบายว่าทำไม enterprise ต้อง glue infrastructure เอง ในเมื่อ Resolve/ServiceNow ให้มาครบ. เมื่อ CTO ระดับ Fortune 500 ต้อง approve $2–5M agent transformation budget, การเลือก vendor ที่มี governance track record 20 ปีย่อมง่ายกว่าเลือก YC batch S26

คำถามที่ยังไม่ชัด: agent ที่ Resolve/ServiceNow/UiPath สร้างจะ "smart enough" เท่ากับ agent ที่ build ด้วย Claude/GPT + custom framework หรือเปล่า? Enterprise ตัดสินใจซื้อบน (a) certainty + governance, หรือ (b) capability + speed of iteration? รอบ 12 เดือนข้างหน้าจะเป็น test ว่าตลาดเลือกทางไหน

## มุม AI Agent Platform

**Builders** ที่กำลังสร้าง agent framework — pattern นี้บังคับให้ startup ต้อง either (1) partner กับ ITSM/RPA vendor เพื่อเข้าถึง enterprise footprint, (2) build vertical agent app ที่ deep ในหนึ่ง domain ที่ RPA vendor ไม่ครอบคลุม, หรือ (3) target SMB/mid-market ที่ยังไม่มี ServiceNow/UiPath อยู่. Generic agent orchestration horizon กำลังปิด. **Businesses** ที่ deploy agent ใน IT ops: ก่อนซื้อ agent startup ให้ดูก่อนว่า ITSM/RPA vendor ที่ใช้อยู่มี agent module ถึงไหน — อาจจะได้ agent capability พร้อมกับ contract ที่ต่ออยู่แล้ว โดยไม่ต้องเพิ่ม vendor list. **Ecosystem**: reusable skills library กำลังเป็น battleground — Anthropic Skills, Resolve Skills, UiPath Skills, ServiceNow Skills. ในอีก 12 เดือน คำถามอาจไม่ใช่ "จะใช้ agent เจ้าไหน" แต่เป็น "Skill portable ไหมข้าม vendor" — pattern เดียวกับ Docker container ตอน 2015

## Sources
- [Resolve Unveils the Next Generation of AgentLab (PRWeb)](https://www.prweb.com/releases/resolve-unveils-the-next-generation-of-agentlab-accelerating-the-enterprise-shift-to-autonomous-operations-302852643.html)
- [AI Agents News Brief: August 18, 2026 (AI Agents Directory)](https://aiagentsdirectory.com/news/ai-agents-news-brief-august-18-2026)
- [IT Automation and Orchestration Platform (Resolve.io)](https://resolve.io/)

---

## Audio script
Resolve บริษัท IT process automation ที่ทำ runbook orchestration ให้ enterprise มา 20 กว่าปี ปล่อย AgentLab next-generation เมื่อ 17 สิงหาคม. Feature หลักคือให้ทีม IT DevOps SRE สร้าง agent จากภาษาธรรมชาติ, มี reusable skills library ให้แชร์ข้ามทีม, และ governance-aware deployment ที่ทดสอบ agent 100 scenario ก่อนได้ permission เขียนไป production. Pattern ที่ชัดขึ้นเรื่อย ๆ ในปีนี้คือ ITSM RPA vendor รุ่นเก่ากำลังเบียดขึ้นมาเป็น agent platform — ServiceNow, UiPath, Automation Anywhere, Blue Prism และตอนนี้ Resolve. ทั้งหมดใช้ moat ที่ agent startup ยังไม่มี คือ enterprise footprint, compliance certification, และ library ของ workflow ที่ battle-test มาแล้ว. สำหรับ startup agent orchestration ที่แข่งกันอยู่ — Warp Factories, Cognition — pattern นี้บังคับให้ต้องหาทาง either partner กับ vendor ใหญ่, หรือ deep ในหนึ่ง vertical, หรือไปตลาด SMB. Horizon ของ generic agent framework กำลังปิด. สำหรับองค์กรที่ deploy agent — ก่อนจะซื้อ startup ให้ดูก่อนว่า vendor ITSM ปัจจุบันมี agent module ถึงไหน อาจได้มาฟรีกับ contract ที่ต่ออยู่แล้ว.
