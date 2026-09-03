---
date: 2026-09-04
slug: kt-woori-bank-agent-connector
topic: use-case
reading_time_min: 4
sources: 3
image_prompt: |
  A cinematic editorial illustration of a Korean bank lobby with three
  service counters merging into one glowing conveyor labeled "AGENT
  CONNECTOR"; above each counter float labels "CHATBOT", "CONSULTATION BOT",
  "AI BANKER", and the numbers "1 CUSTOMER, N CHANNELS" burn on a large
  banner. A silhouetted customer walks the conveyor without stopping.
  Editorial isometric style, indigo-and-warm-gold palette, high contrast,
  1:1 aspect, no real human faces.
image: images/26-09-04-0613-04-kt-woori-bank-agent-connector.png
---

# KT ชนะโปรเจกต์ Woori Bank — deploy "Agent Connector" เชื่อม chatbot, consultation bot, AI Banker เป็น flow เดียว

## TL;DR
- **KT** (Korea Telecom) ประกาศ **31 ส.ค. 2026** — ชนะโปรเจกต์รื้อ chatbot + consultation bot ของ **Woori Bank** (top-4 commercial bank ของเกาหลี)
- Solution ชื่อ **"Agent Connector"** — เชื่อม chatbot, consultation bot, AI Banker, และ AI agent ให้ **customer context ไหลข้าม channel** ได้
- เป้าหมาย: เพิ่ม **resolution rate** ของ inbound + expand ไปทำ **outbound consultation + branch service**
- Context: **Samsung SDS** เพิ่งชนะ **Woori Bank AI Agent** project แยกกัน (เม.ย. 26) — Woori กำลัง multi-vendor ทั้ง stack

## เกิดอะไรขึ้น

Woori Bank — 1 ใน 4 commercial bank ใหญ่ที่สุดของเกาหลี — เดินหน้า agentic transformation รอบใหม่ด้วยการเลือก **KT (Korea Telecom)** เป็น contractor สำหรับรื้อ **chatbot + consultation bot** ทั้ง system. ประกาศเมื่อ 31 ส.ค. และเริ่ม system development แล้ว. Solution กลางที่ KT วางคือ **"Agent Connector"** — layer ที่ทำหน้าที่ **relay customer context ข้าม channel**

จุดที่แยก deal นี้จาก "อีก chatbot upgrade" ทั่วไปคือ **scope ของ context handoff**. Agent Connector ออกแบบให้ (ก) chatbot ที่ลูกค้าคุยผ่าน mobile app, (ข) consultation bot ที่ตอบใน call center, (ค) AI Banker ที่ให้ financial advice, และ (ง) AI agent ที่ทำ task-processing — **share ประวัติสนทนาและ intent state ระหว่างกันได้แบบ real-time**. แปลว่าลูกค้าที่ถามเรื่องสินเชื่อกับ chatbot ตอนเช้า, โทรเข้า call center ตอนบ่าย — consultant (มนุษย์หรือ AI) เห็น context เดิมทันที ไม่ต้องเริ่มใหม่

เป้าหมายชัด 2 อย่าง: **(1) เพิ่ม resolution rate ของ inbound inquiry** — วัดจาก "ลูกค้าจบเรื่องในช่องแรกที่ติดต่อ" — และ **(2) expand ไปทำ outbound consultation + branch service** — เอา AI agent เป็นตัวช่วย advisor ที่ branch จริง

Context สำคัญที่ทำให้ deal นี้อ่านสนุกคือ **Woori กำลัง multi-vendor** — เมื่อ เม.ย. 2026 Samsung SDS ชนะ **Woori Bank AI Agent** project แยกออกมา (Korea Times รายงาน). แปลว่า Woori แยก layer: **Samsung SDS ทำ agent layer, KT ทำ orchestration/connector layer** — pattern ที่แตกต่างจาก big-4 audit firm ในสหรัฐฯ (ที่มักเลือก vendor เดียวครอบทั้ง stack)

## ทำไมสำคัญ

Deal นี้เป็น **case study สดของ agent-to-agent orchestration ในธนาคาร** ที่หายากมากในภูมิภาค. ก่อนหน้านี้ agent deployment ในธนาคารส่วนใหญ่เป็น **single-channel** (chatbot ตัวเดียว, หรือ email agent ตัวเดียว) — pattern ที่ล้มเหลวเพราะลูกค้าไม่อยู่ที่ channel เดียว. Woori bet ว่า **layer ของ orchestration + context sharing** สำคัญกว่า model performance ตัวเอง — และ **โครงสร้าง multi-vendor** บ่งชี้ว่าธนาคารเกาหลีเรียนรู้แล้วว่า agent stack เป็น modular ไม่ควร lock-in vendor เดียว

pattern ที่จะกระเพื่อมออกจากเกาหลีคือ **agent orchestration layer ในฐานะ standalone contract**. ในตลาดสหรัฐฯ orchestration มักถูก bundle เข้ากับ agent framework (LangGraph, CrewAI) หรือ platform (Wonderful, Sierra). ในเกาหลี KT ขาย orchestration แบบ standalone — เพราะ (ก) โครงสร้าง telco ที่มี distribution ในทุก corporate, (ข) ธนาคารเชื่อ telco เรื่อง infrastructure มากกว่า SaaS ใหม่. Model นี้จะขยายเข้า APAC ก่อนอื่น — โดยเฉพาะ **SG (Singtel), TH (AIS/True), MY (Maxis), ID (Telkomsel)**

signal ต่อไป 60-90 วัน: (1) ธนาคารเกาหลีอันดับรองอย่าง **KB Kookmin, Shinhan, Hana** จะประกาศโครงการที่คล้ายกันภายใน Q4, (2) **AIS Business หรือ True Corp** ในไทยจะ pitch "Agent Connector-equivalent" ให้ธนาคารไทย, (3) **Samsung SDS + KT** อาจร่วมทำ reference architecture ที่ export ไปทั่วภูมิภาค

## มุม AI Agent Platform

สำหรับ **builders** — ถ้าคุณสร้าง agent framework ในไทย/APAC, สิ่งที่ deal นี้บอกคือ **orchestration layer ขายได้ในฐานะ product แยก** ไม่ต้อง bundle เข้ากับ agent runtime. Focus feature ที่สำคัญคือ (ก) cross-channel session state, (ข) intent handoff protocol ระหว่าง agent, (ค) fallback logic ที่โยนไปหา human agent ได้ smooth. อย่า assume ว่าลูกค้าจะซื้อ full-stack — bank/telco/insurer ที่มี legacy อยู่แล้วมักซื้อ layer-by-layer

สำหรับ **businesses ในไทย** (โดยเฉพาะ finance + telco + retail multi-channel) — deal Woori-KT เป็น **reference architecture ที่ควร study**. Structure การ contract ที่แยก **agent layer** ออกจาก **orchestration layer** ช่วยหลีกเลี่ยง vendor lock-in และเปิดโอกาสให้ swap agent ตัวใดตัวหนึ่งได้ในอนาคต. ธนาคารไทยที่กำลังจะสรุป Q4 procurement (SCB, KBank, Bangkok Bank) ควรถามคำถามนี้กับ vendor ก่อนเซ็น

สำหรับ **ecosystem ไทย** — window เปิดสำหรับ **local system integrator** ที่สามารถทำ agent orchestration layer โดยไม่ต้อง reinvent ทั้ง stack. ใช้ open-source component (LangGraph, Temporal, Kafka สำหรับ event streaming) + wrap ด้วย domain knowledge ของ regulated industry ไทย (BOT compliance, PDPA). Enabridge สามารถ position **"Agent Connector สำหรับ Thai enterprise"** — เป็น bridging layer ระหว่าง agent runtime ของ vendor ต่างๆ กับ core banking / core insurance ของ enterprise ไทย. ไม่ต้องแข่ง agent runtime; แข่ง orchestration + local context depth

## Sources
- [KT Wins Woori Bank AI Chatbot Upgrade Project — The Elec](https://www.thelec.net/news/articleView.html?idxno=13469)
- [KT begins rebuild of Woori Bank AI chatbot, consultation bot — Digital Today](https://www.digitaltoday.co.kr/en/view/97987/kt-begins-rebuild-of-woori-bank-ai-chatbot-consultation-bot)
- [Samsung SDS to lead Woori Bank AI agent project, driving finance AX push — Korea Times](https://www.koreatimes.co.kr/business/tech-science/20260407/samsung-sds-to-lead-woori-bank-ai-agent-project-driving-finance-ax-push)

---

## Audio script
ปิดท้ายด้วยข่าวจากเกาหลีที่ builder ไทยควรจดครับ. Woori Bank หนึ่งใน สี่ ธนาคารพาณิชย์ใหญ่ที่สุดของเกาหลี ประกาศ สามสิบเอ็ด สิงหา เลือก KT เป็น contractor รื้อ chatbot กับ consultation bot ทั้ง system. Solution กลางชื่อ Agent Connector — layer ที่ relay customer context ข้าม channel. ให้ chatbot ใน mobile app, consultation bot ใน call center, AI Banker ที่ให้คำแนะนำการเงิน, และ AI agent ที่ทำ task-processing แชร์ประวัติสนทนากันได้ real-time. ลูกค้าถามสินเชื่อกับ chatbot เช้า โทรเข้า call center บ่าย consultant เห็น context เดิมทันที. เป้าหมายชัดสองอย่าง — เพิ่ม resolution rate ของ inbound และ expand ไป outbound consultation กับ branch service. Context สำคัญคือ Woori multi-vendor — เมษา ที่ผ่านมา Samsung SDS ชนะโปรเจกต์ AI Agent แยก. แปลว่าธนาคารเกาหลีเรียนรู้แล้วว่า agent stack ควร modular ไม่ควร lock-in vendor เดียว. Pattern ที่จะกระเพื่อม — orchestration layer ขายได้เป็น standalone. Telco ในเอเชียมี distribution ในทุก corporate อยู่แล้ว AIS True Singtel Maxis Telkomsel น่าจะออก Agent Connector-equivalent ตามใน หกสิบ ถึง เก้าสิบ วัน. สำหรับ builder ไทย — orchestration layer ขายได้แยก focus cross-channel session state, intent handoff, fallback logic. สำหรับธนาคารไทย ที่จะสรุป Q4 procurement — SCB KBank Bangkok Bank ควรถาม vendor เรื่อง contract แยก agent กับ orchestration ก่อนเซ็น. สำหรับ Enabridge — position เป็น Agent Connector สำหรับ Thai enterprise เชื่อม agent runtime หลาย vendor เข้ากับ core banking core insurance ไทย ไม่ต้องแข่ง runtime แข่ง orchestration กับ local context depth ครับ
