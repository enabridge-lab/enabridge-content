---
date: 2026-09-01
slug: 26-09-01-0614-04-woori-bank-kt-agent-connect-korea-financial-vertical
topic: use-case
reading_time_min: 4
sources: 3
image_prompt: |
  A bank counter styled as three glowing kiosks connected by a bright cyan
  ribbon labeled "AGENT CONNECT"; kiosk one tagged "CHATBOT", kiosk two
  "CONSULTATION BOT", kiosk three "AI BANKER". A single silhouette customer
  walks the ribbon carrying an "OPEN TICKET" folder. Above them a headline
  reads "10 TASKS PHASE 1 · DEC 2026". Editorial isometric style, navy blue
  background with cyan and gold accents, crisp legible sans-serif, readable in
  200px thumbnail, 1:1 aspect, no real human faces.
image: images/26-09-01-0614-04-woori-bank-kt-agent-connect-korea-financial-vertical.png
---

# Woori Bank ให้ KT rebuild ระบบ chatbot ทั้งหมด — "Agent Connect" ส่ง context ข้าม chatbot / consultation bot / AI banker / agent, phase 1 ธ.ค. 2026

## TL;DR
- Woori Bank (top-4 ธนาคารเกาหลี) ให้ **KT** rebuild chatbot + consultation bot ทั้งระบบ ผ่าน **Agent Connect** — ตัวกลางที่ส่ง context ข้าม chatbot / consultation bot / AI banker / AI agent (Seoul Economic Daily รายงาน 31 ส.ค.)
- **Phase 1 ธ.ค. 2026**: 10 counseling task ใหม่ที่ใช้ **multimodal counseling** (Woori เพิ่ง launch generative AI counseling bot กับ multimodal ต้นปีนี้)
- **Phase 2 พ.ค. 2027**: integrate AI chatbot + AI banker screen เป็น interface เดียว — เดิม Samsung SDS lead รอบ 04/2026, KT ได้ contract handoff รอบใหม่

## เกิดอะไรขึ้น

31 ส.ค. Seoul Economic Daily รายงานว่า **KT** — teleco รายใหญ่ของเกาหลี — ชนะโปรเจกต์ rebuild ระบบ chatbot ทั้งหมดของ **Woori Bank** ผ่าน solution ใหม่ชื่อ **Agent Connect**. หัวใจของ Agent Connect ไม่ใช่ chatbot ใหม่ แต่คือ **middleware ที่ทำ handoff ระหว่าง 4 layer ของ customer service**: (1) **chatbot** (self-service FAQ), (2) **consultation bot** (structured product inquiry), (3) **AI banker** (financial consultation), (4) **AI agent** (task execution). Value proposition: ลูกค้าเริ่มคุยกับ chatbot ตอนเช้า, ย้ายไป consultation bot ตอนบ่าย, ต่อกับ AI banker ตอนเย็น — **context เดินตามทุก channel** โดยไม่ต้องเล่าเรื่องใหม่.

**Phase 1** launch **ธันวาคม 2026** — 10 counseling task ใหม่ที่ใช้ multimodal (voice + image + text; น่าจะ tie กับ generative AI counseling bot ที่ Woori launch ต้นปีนี้). **Phase 2** launch **พฤษภาคม 2027** — integrate AI chatbot + AI banker screen เป็น interface เดียวสำหรับลูกค้า. บริบทที่ต้องรู้: **เม.ย. 2026 Samsung SDS** ได้ lead โปรเจกต์ AI agent ของ Woori Bank (Korea Times รายงาน) — round นี้ **KT ได้ contract แยก** สำหรับ chatbot/consultation bot rebuild specifically. Woori เลือก **multi-vendor** — Samsung SDS สำหรับ agent layer, KT สำหรับ conversational + orchestration — เป็น pattern ที่แตกจากธนาคารเกาหลีก่อนหน้าที่ปกติผูกกับ vendor เดียว.

## ทำไมสำคัญ

**Handoff architecture** คือ pattern ที่ SEA bank ทุกแห่งจะต้องเจอในอีก 12-18 เดือน. ปัญหาที่ทุก retail bank แชร์: customer แต่ละคนคุยกับหลาย channel (mobile app chat, LINE OA, phone consultation, branch visit) — และแต่ละ channel มี system + vendor ต่างกัน. Handoff ที่ preserve context เป็นปัญหาที่ CRM vendor (Salesforce, Genesys, NICE) แก้แบบ half-baked มานาน 10+ ปี. **Agent Connect ของ KT เป็น first vendor solution ที่ position handoff เป็น first-class primitive** — ไม่ใช่ add-on ของ chatbot หรือ contact center. ที่น่าสนใจกว่าคือ **timeline ที่ realistic** — Phase 1 3 เดือน, Phase 2 อีก 5 เดือน — ไม่ใช่ "AI transformation 2 ปี" แบบ consulting ขาย.

Pattern ที่ 3 signal พร้อมกันสัปดาห์นี้บอกเรา:
- **HappyRobot** ($150M @ $1.2B, 28 ส.ค.) — voice agent ใน logistics
- **DBS Bank** (1,500 banker, 27 ส.ค.) — internal-facing agent สำหรับ credit memo
- **Woori Bank + KT** (31 ส.ค.) — customer-facing multi-channel handoff

= **vertical AI agent enters banking / logistics production at scale**. Enterprise ที่ยัง pilot อยู่ปีนี้จะเห็น competitor ที่ deploy production ในไตรมาสถัดไป — window ของ "wait and see" ปิดในระยะ 6-9 เดือน.

## มุม AI Agent Platform

**สำหรับ builders:** Handoff เป็น feature ที่ agent platform ต้องมี — ไม่ใช่ทางเลือก. ที่ต้อง implement: (1) **conversation state persistence** ที่ portable ข้าม channel + vendor, (2) **intent + context transfer format** ที่ standard (candidate: OpenTelemetry-style trace + span for conversation), (3) **role handoff** ระหว่าง bot ↔ human ↔ specialist agent, (4) **audit trail** ที่ complience (บันทึกว่า agent ไหนพูดอะไรกับลูกค้าตอนไหน). ที่หลีกเลี่ยงได้เลย: อย่าคิดว่า chatbot + AI banker เป็น product แยก — customer เห็นเป็น "ธนาคาร" ตัวเดียว. **สำหรับ businesses:** ถ้าคุณเป็น bank/insurance/telco/utility ที่มี multi-channel customer service — ประเมิน **handoff maturity** เป็นวาระ Q4 2026. คำถาม: (a) context ไปกับลูกค้าข้าม channel ได้ป่าว, (b) AI agent execute task (ไม่ใช่แค่ตอบคำถาม) ได้ป่าว, (c) audit log ผ่าน compliance ป่าว. **สำหรับ ecosystem:** teleco ที่มี contact center DNA (KT, SingTel, AIS, Globe, Telkomsel) มี positional advantage — พวกเขาเข้าใจ conversational flow + call routing มานาน. Vendor CRM แบบ traditional (Salesforce Service Cloud, Genesys Cloud) ต้อง repackage เป็น "agent orchestration" ไม่งั้นถูก AI-first platform disrupt.

Enabridge angle: **ทำ "Agent Connect for Thai Banks"** — reference architecture + reusable component สำหรับ handoff ระหว่าง LINE OA chatbot + K PLUS / SCB Easy mobile chat + call center + branch visit + relationship manager. ผูกกับ Thai regulatory (ธปท circular ว่าด้วย customer conversation logging), audit format ที่ SEC ยอมรับ, language nuance (ไทย + ภาษาถิ่น ใต้/อีสาน/เหนือ). Partner candidate: True Corp (Contact Center BU), Advanced Info Service (call center outsourcing), IBM Consulting Thailand. Deal structure: 1 flagship bank customer (BBL/SCB/KBank/KTB) ใน 12-18 เดือนแรก, expansion เป็น industry template ปีที่ 2-3.

## Sources
- [KT to Rebuild Woori Bank's AI Chatbot and Consultation Bot Systems — Seoul Economic Daily](https://en.sedaily.com/technology/2026/08/31/kt-to-rebuild-woori-banks-ai-chatbot-and-consultation-bot)
- [KT begins rebuild of Woori Bank AI chatbot, consultation bot — Digital Today](https://www.digitaltoday.co.kr/en/view/97987/kt-begins-rebuild-of-woori-bank-ai-chatbot-consultation-bot)
- [Samsung SDS to lead Woori Bank AI agent project — Korea Times](https://www.koreatimes.co.kr/business/tech-science/20260407/samsung-sds-to-lead-woori-bank-ai-agent-project-driving-ax-finance-push)

---

## Audio script
ที่ Woori Bank ธนาคาร top 4 ของเกาหลี มีข่าวสำคัญเมื่อวานนี้ 31 สิงหาคม KT teleco รายใหญ่ของเกาหลีชนะโปรเจกต์ rebuild ระบบ chatbot กับ consultation bot ทั้งระบบ ผ่าน solution ใหม่ชื่อ Agent Connect ที่น่าสนใจไม่ใช่ chatbot ใหม่แต่คือ middleware ที่ทำ handoff ระหว่าง 4 layer ของ customer service chatbot self-service consultation bot structured inquiry AI banker financial consultation และ AI agent task execution ลูกค้าเริ่มคุยกับ chatbot ตอนเช้า ย้ายไป consultation bot ตอนบ่าย ต่อกับ AI banker ตอนเย็น context เดินตามทุก channel ไม่ต้องเล่าเรื่องใหม่ phase 1 launch ธันวาคม 2026 10 counseling task ใหม่ multimodal phase 2 พฤษภาคม 2027 integrate AI chatbot กับ AI banker screen เป็น interface เดียว บริบทที่ต้องรู้เมษายน Samsung SDS ได้ lead โปรเจกต์ AI agent ของ Woori แล้ว รอบนี้ KT ได้ contract แยก multi-vendor ธนาคารเดียว รวมกับข่าว HappyRobot 150 ล้านที่ปิดสัปดาห์ที่แล้ว กับ DBS Bank 1,500 banker ที่ใช้ agent เขียน credit memo signal ตรงกันว่า vertical AI agent เข้าสู่ production banking กับ logistics แบบ scale จริง แล้ว window ของ wait and see จะปิดในระยะ 6 ถึง 9 เดือน สำหรับ Enabridge opportunity คือ Agent Connect for Thai Banks reference architecture สำหรับ handoff ระหว่าง LINE OA mobile chat call center branch visit relationship manager
