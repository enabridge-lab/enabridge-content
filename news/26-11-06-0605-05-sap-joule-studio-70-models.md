---
date: 2026-11-04
slug: sap-joule-studio-70-models
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a wide developer cockpit split
  down the middle. Left side labeled "NO-CODE" shows a floating chat
  bubble turning into a flowchart of agents; right side labeled "PRO-CODE"
  shows an IDE window with code and a terminal. A big banner above reads
  "JOULE STUDIO · 70+ MODELS". Smaller tags float: "n8n WORKFLOWS",
  "LangChain · Pydantic AI · LlamaIndex", "SANDBOXED". A sleek SAP-style
  blue-and-gold frame edges the whole scene. Editorial style, deep SAP
  blue and amber palette, 1:1 aspect, no real human faces (silhouettes OK),
  high contrast for 200px thumbnail.
image: images/26-11-06-0605-05-sap-joule-studio-70-models.png
---

# SAP ยัด 70+ models + n8n + Cursor ลง Joule Studio — เดิมพันว่า enterprise agent สร้างง่ายกว่า code

## TL;DR
- SAP เปิดตัว Joule Studio + Joule Work ที่ TechEd 2026 — no-code + pro-code tooling ใน platform เดียว
- เลือกได้มากกว่า 70 AI models, รองรับ n8n workflow ใน studio, LangChain / Pydantic AI / LlamaIndex, ใช้ Visual Studio Code + Cursor extension
- Governance: agent รันใน sandbox แยกตัว มี observability + spend control — เพื่อต่อสู้กับ ServiceNow, Workday, Salesforce ที่ขาย vertical agent ให้ enterprise เดียวกัน

## เกิดอะไรขึ้น
ที่งาน SAP TechEd 2026 (ปลาย ตค) SAP ประกาศ Joule Studio 2.0 — development environment สำหรับสร้างและ deploy agent ที่มี two-track approach: no-code สำหรับ business user และ pro-code สำหรับ developer โดยใช้ Visual Studio Code หรือ Cursor extension no-code path สามารถสร้าง agent หรือ n8n workflow จาก prompt เดียว — ให้ business user ที่ไม่เขียน code ก็เริ่มต้นได้

Pro-code side มี integration กับ framework ยอดนิยม — LangChain, Pydantic AI, LlamaIndex โดยนั่งข้าง embedded n8n environment สำหรับ visual orchestration ของ multi-agent system developer สามารถเลือก model ได้มากกว่า 70 ตัว รวม Anthropic Claude, OpenAI GPT, Google Gemini, และ open-source model ที่ run ใน SAP AI Core

Governance เป็นจุดที่ SAP เน้น — agent แต่ละตัวรันใน sandbox แยกตัว มี policy + guardrail configurable มี observability ของ model usage, token spend, และ agent behavior admin ควบคุมได้ว่า agent ตัวไหนเข้าถึง ERP data ตัวไหน รวมถึง audit log ทุก action — เหมือน SAP ERP เดิมที่มี row-level security แต่ย้ายมาเป็น agent-level

SAP เน้นว่า Joule Studio เชื่อมกับ SAP Business Data Cloud, SAP Business AI Platform, และ "context layer" ที่ดึง data จาก SAP S/4HANA, Ariba, SuccessFactors, Concur โดยไม่ต้องเขียน integration — เป็น vertical advantage ที่ Microsoft Copilot Studio หรือ ServiceNow Now Assist ตามยาก

## ทำไมสำคัญ
ตลาด enterprise agent builder platform กำลังแบ่งออกเป็น 3 ค่าย — (1) horizontal pure-play เช่น LangGraph, CrewAI, AutoGen ที่ developer-first และ opinionated ด้าน framework (2) hyperscaler platform เช่น Microsoft Copilot Studio, Google Vertex AI Agent Builder, AWS Bedrock Agents ที่ ride cloud infra (3) application vendor เช่น Salesforce Agentforce, ServiceNow Now Assist, Workday Illuminate, และตอนนี้ SAP Joule Studio ที่ embed agent เข้าไปใน application ที่ลูกค้าใช้อยู่แล้ว

SAP's bet คือค่ายที่ 3 ชนะ — เพราะ enterprise ไม่ซื้อ framework พวกเขาซื้อ outcome ใน workflow ที่ตัวเอง run อยู่แล้ว การเลือก 70+ models หมายความว่า SAP ไม่ผูกตัวเองกับ model vendor เดียว — ลูกค้าเลือกได้ว่า Claude หรือ GPT หรือ open-source — แต่ "operating system" ที่ host agent คือ SAP

Caveat สำคัญ — n8n ที่ SAP embed ไว้เป็น open-source workflow tool ที่ popular ในหมู่ developer — แต่ enterprise buyer ยังระวังเรื่อง license (Sustainable Use License ของ n8n มีข้อจำกัดเรื่อง SaaS commercial use) — SAP ต้องเจรจา commercial agreement ให้ชัด Framework list ที่ third-party blog ยก (LangChain, Pydantic AI, LlamaIndex) ยังไม่เจอใน official SAP doc เสมอ — คนที่ pilot ควร verify กับ SAP เรื่อง supported framework version

## มุม AI Agent Platform
Builders — ถ้าคุณขาย framework แยก หรือ agent IDE แยก SAP + Salesforce + ServiceNow + Microsoft กำลัง bundle developer experience เข้าใน application suite ของตัวเอง ตลาด horizontal developer tool จะบีบ — ต้อง compete ที่ depth (feature ที่ enterprise platform ไม่มี เช่น multi-agent coordination, eval framework, observability depth) หรือ open-source route ที่ enterprise ซื้อ for compliance reason

Users/business — ถ้าคุณใช้ SAP ERP อยู่ Joule Studio ทำให้ build agent ได้โดยไม่ต้อง pipe data ออกไปที่ platform อื่น — ลด security + compliance risk แต่ต้องแลกกับ vendor lock-in ที่ลึกขึ้น — ถ้าตัดสินใจย้าย ERP ภายหลัง agent ที่ build ใน Joule Studio ไม่ได้ย้ายตาม Enabridge ที่สร้าง agent ให้ลูกค้าใช้ SAP ควรพิจารณาว่าจะ build agent ใน Joule Studio (เพื่อ time-to-value) หรือ build ใน platform เป็นกลางที่เชื่อมผ่าน SAP RFC/OData API (เพื่อ portability)

Ecosystem — n8n ที่ SAP embed เป็น case study ที่น่าสนใจ — enterprise จะเริ่ม bundle open-source tool เข้า product ของตัวเองมากขึ้น เพราะ workflow automation กำลังกลายเป็น commodity layer — Microsoft เพิ่งซื้อ Logic Apps เข้า Copilot, ServiceNow ซื้อ Workflow Data Fabric — คาดว่า Oracle จะตอบกลับด้วย acquisition workflow vendor ภายใน 6 เดือน

## Sources
- [SAP Empowers AI Developers to Build What Matters (SAP News)](https://news.sap.com/2026/10/sap-teched-ai-developers-build-what-matters-autonomous-execution/)
- [Joule Studio for Enterprise Agentic AI Solutions (SAP Learning)](https://architecture.learning.sap.com/docs/ref-arch/f5a3ef)
- [SAP Bets on 'AI That Executes' (BigGo Finance)](https://finance.biggo.com/news/7edef02a-5f99-4a21-a57a-8f2ddc143c08)

---

## Audio script
SAP เปิดตัว Joule Studio 2.0 ที่งาน TechEd 2026 เป็น development environment สำหรับสร้างและ deploy AI agent ที่มีสองเส้นทางคือ no-code สำหรับ business user และ pro-code สำหรับ developer ที่ใช้ Visual Studio Code หรือ Cursor extension no-code path สามารถสร้าง agent หรือ workflow n8n จาก prompt เดียว ส่วน pro-code มี integration กับ framework ยอดนิยมอย่าง LangChain, Pydantic AI, LlamaIndex และ developer เลือก model ได้มากกว่า 70 ตัวรวม Claude, GPT, Gemini จุดที่ SAP เน้นคือ governance — agent แต่ละตัวรันใน sandbox แยกมี policy configurable, observability ของ token spend, และ audit log ทุก action ลักษณะเหมือน SAP ERP เดิมที่มี row-level security แต่ย้ายมาเป็น agent level ตลาด enterprise agent builder กำลังแบ่งออกเป็นสามค่ายคือ horizontal framework, hyperscaler platform, และ application vendor ที่ embed เข้าไปใน app ที่ลูกค้าใช้อยู่แล้ว SAP เดิมพันว่าค่ายที่สามจะชนะเพราะ enterprise ไม่ซื้อ framework แต่ซื้อ outcome ใน workflow ที่ตัวเอง run อยู่ สำหรับคนที่ใช้ SAP ERP Joule Studio ลด time to value แต่แลกกับ vendor lock-in ที่ลึกขึ้น ถ้าคิดจะย้าย ERP ภายหลัง agent ที่ build ใน Joule Studio ไม่ได้ย้ายตาม Enabridge ควรพิจารณาว่าจะ build ใน Joule เพื่อความเร็ว หรือ build ใน platform กลางที่เชื่อมผ่าน API เพื่อ portability
