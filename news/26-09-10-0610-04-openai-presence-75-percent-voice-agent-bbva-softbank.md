---
date: 2026-09-10
slug: openai-presence-75-percent-voice-agent-bbva-softbank
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial isometric illustration of a giant telephone handset floating
  over a globe; three headline meters glow above the handset showing
  "75% RESOLVED", "-15 PPS HANDOFF", "10 DAYS". Around the base three
  small storefronts labeled "BBVA MX", "SOFTBANK JP", "RETAIL INSURANCE AU"
  each connect a colored wire back to the handset. Muted teal and warm
  amber palette, cinematic rim lighting, oversized high-contrast
  typography for a 200px thumbnail, 1:1 aspect, no real human faces.
image: images/26-09-10-0610-04-openai-presence-75-percent-voice-agent-bbva-softbank.png
---

# OpenAI Presence เก็บตัวเลขจริงจาก 3 ทวีป — 75% autonomous resolution ใน voice/chat support, ลด human handoff 15 percentage point ใน 10 วัน, และ BBVA/SoftBank/Retail Insurance Australia deploy จริง

## TL;DR
- **OpenAI Presence** — enterprise platform สำหรับ realtime voice + chat agent ที่ launch limited GA เดือน ก.ค. 2026 — เก็บตัวเลข production ที่น่าอ้างอิงในเดือนที่ผ่านมา
- **75% ของ inbound issue ปิดโดยไม่ต้องมี human** — วัดที่ OpenAI's own English support channel (**1-888-GPT-0090**) ที่ powered by Presence
- **-15 percentage points ใน human handoff rate ใน 10 วัน** — ผ่าน **Codex-powered improvement loop** ที่ Presence ใช้ auto-tune prompt + tool + guardrail จาก conversation log
- **Early enterprise customer**: **BBVA Mexico** (customer support), **SoftBank Corp** (sales development), **Retail Insurance Australia** (IT service) — 3 ทวีป, 3 use case, deploy โดย OpenAI Forward-Deployed Engineer ทีม
- Signal: **voice agent ก้าวจาก demo → measurable business outcome** — และ Presence positioning ตัวเองไม่ใช่ chatbot vendor แต่คือ **"agent operating platform"** ที่นั่งระหว่าง model กับ enterprise system

## เกิดอะไรขึ้น

OpenAI **Presence** — enterprise agent platform ที่ launch limited GA วันที่ 22 กรกฎาคม 2026 — เก็บตัวเลข production ที่ควรค่าแก่การอ้างอิงในสัปดาห์ที่ผ่านมา. ต่างจาก ChatGPT Enterprise ที่เป็น B2B chatbot, **Presence เป็น deployment + management layer** ที่ handle เรื่องที่ยากที่สุดของการรัน agent ใน production: connect กับ enterprise system, define capability boundary, test edge case ก่อน launch, และ improvement loop หลัง go-live

**Metric ที่ OpenAI เปิด**:
1. **75% resolution rate** — วัดจาก **1-888-GPT-0090**, OpenAI's own English-language phone support channel ที่ powered by Presence ตัวเอง. 3 ใน 4 call จบโดย agent ไม่ต้อง escalate มนุษย์. เป็น ratio ที่ Klarna, Salesforce Help Agent ทำได้ปี 2024-2025 แต่ตอนนั้นเป็น text chat — **voice ใน realtime latency นี่คือ threshold ใหม่**
2. **-15 pp handoff ใน 10 วัน** — Codex-powered improvement loop ใน Presence auto-analyze conversation log, identify prompt/tool gap, generate patch, test บน replay, และ deploy. cycle 10 วัน ทำให้ handoff rate ลด 15 percentage point ที่ OpenAI's own operation. เป็น evidence ว่า **agent improvement ไม่จำเป็นต้องรอ human ML engineer tuning** — model + orchestration loop ทำได้เอง

**Early enterprise customer 3 ราย** ครอบ 3 ทวีป:
- **BBVA Mexico** — bank ขนาดใหญ่ที่ deploy customer support agent สำหรับ millions of retail banking customer
- **SoftBank Corp** — sales development agent ที่ qualify inbound lead + book meeting
- **Retail Insurance Australia** — IT service agent ที่ handle internal help desk ticket

3 customer นี้ deploy ผ่าน **OpenAI Forward-Deployed Engineer** — ไม่ใช่ self-service, ไม่ใช่ certified partner. OpenAI engineer ไปนั่งข้าง customer 4-8 สัปดาห์เพื่อ integrate เข้ากับ core system (mainframe, CRM, telephony), design guardrail, และ hand-off operation ให้ customer team ที่ trained แล้ว. **Model deployment ที่ high-touch แบบนี้** copy จาก Palantir Forward-Deployed Engineer และ Databricks Field Engineering — pattern ที่ Anthropic, Microsoft Frontier Company, Accenture-Google Gemini Enterprise ก็รับไปใช้พร้อมกันในไตรมาสที่ผ่านมา

## ทำไมสำคัญ

**75% autonomous resolution ใน voice channel คือ threshold ที่เปลี่ยน BPO industry**. call center BPO ทั่วโลก (Concentrix $10B revenue, TDCX, Teleperformance, TCS BPO) ขายแรงงาน 8-25 USD/hour ให้ enterprise resolve customer inquiry. ถ้า Presence + peer competitor (Sierra AI, Decagon, Ada, Cresta) ปิด 75% ของ call อย่างที่ OpenAI อ้าง, **cost per resolution ลดจาก ~$3-8 (mid-market BPO) ไปเหลือ $0.20-0.80 (agent inference cost)**. ไม่ใช่ 10-20% improvement — คือ order of magnitude. ผลกระทบ: BPO contract ที่ครบสัญญาปี 2026-2027 (ส่วนใหญ่เป็นสัญญา 3-5 ปี) จะ renegotiate ด้วย hybrid model (agent-first + human escalation) เป็นค่ามาตรฐาน, และ BPO ที่ไม่ pivot ทัน จะเสีย 40-60% revenue ในช่วง 24 เดือน

**-15 pp handoff ใน 10 วัน คือ signal ที่สำคัญกว่า 75%**. เพราะ 75% เป็น absolute number ที่ competitor จะเข้าใกล้ในไม่กี่ไตรมาส. แต่ **improvement velocity 15 pp ต่อ 10 วัน** แปลว่า Presence ปรับตัวเร็วกว่า Sierra AI หรือ Decagon ที่พึ่ง human ML engineer tune manual. ถ้า OpenAI ปิด improvement gap นี้ได้ อีก 6-12 เดือน handoff rate อาจตกไปที่ **5-10%** — ระดับที่ competitor และ BPO ตามไม่ทัน. **Codex-powered improvement loop** เป็น moat ที่ยั่งยืนกว่า model quality — เพราะ model quality copy กันได้, operational loop ที่ tuned เข้ากับ enterprise data ไม่

Signal ที่ควรจับตา: **customer selection**. OpenAI ไม่ launch Presence กับ tech company (ที่ integration ง่าย). Launch กับ **bank เม็กซิโก, telecom ญี่ปุ่น, insurance ออสเตรเลีย** — 3 category ที่ IT stack ซับซ้อน, compliance หนัก, และ latency-sensitive. ถ้า Presence work ที่นี่, จะ work ที่ enterprise segment ไหนก็ได้. เป็น sales strategy ที่คล้าย Snowflake เริ่มจาก financial services + insurance เพื่อ prove enterprise-readiness ก่อน expand

## มุม AI Agent Platform

**Builders**: ถ้าคุณสร้าง voice agent framework หรือ orchestration layer, **Codex-style improvement loop** คือ feature ที่ควร ship. Presence's edge ไม่ได้อยู่ที่ voice model (Realtime API) — อยู่ที่ **loop ที่ auto-analyze conversation log, identify gap, generate patch, replay-test, และ deploy**. คุณสมบัตินี้ต้อง require 3 primitive: (1) **structured conversation logging** ที่ capture ทั้ง transcript + tool call + guardrail decision; (2) **replay environment** ที่ simulate conversation อีกครั้งด้วย patch ใหม่; (3) **code-generation agent** ที่ propose prompt/tool change และ evaluate ก่อน commit. LangGraph, CrewAI, และ Vercel AI SDK ยังไม่มี opinion ที่ชัดใน 3 primitive นี้ — window เปิดให้ startup vertical (Retell, Vapi, Poly AI) ship primitive นี้ก่อน framework horizontal จะรับ

**Users / Business**: enterprise ที่ operate call center / customer support / IT service desk **ตอนนี้ต้องทำ 3 อย่างพร้อมกัน**: (1) **pilot voice agent บน high-volume, low-complexity queue** (password reset, order status, appointment rescheduling) เพื่อ validate 75% threshold ใน context ของตัวเอง; (2) **แก้ contract กับ BPO vendor** ให้ include agent-managed workflow เป็น option ก่อน renewal — ถ้ารอ contract ปกติถึงต่อ อาจ lock ราคาเก่าอีก 3-5 ปี; (3) **retrain frontline supervisor** เป็น **agent operator** — role ที่ monitor agent quality, review handoff, และ tune prompt แทนที่จะ manage human agent

**Ecosystem**: ผู้ชนะ: (1) **hyperscaler ที่ host agent platform** — Azure ที่ pair แน่นกับ OpenAI, AWS ที่ host Presence workload บน compute agreement, Google ที่ push Contact Center AI + Agentspace; (2) **CRM ที่ integrate agent layer เร็ว** — Salesforce Agentforce, HubSpot Breeze, Zendesk Advanced AI; (3) **telephony infra** ที่ ship agent-native primitive — Twilio, Vonage, Sinch. ผู้แพ้: (1) **BPO ระดับกลาง** (staff 5K-20K seat) ที่พึ่งราคา + scale แต่ไม่มี agent capability — จะเสีย mid-market contract เป็นอันดับแรก; (2) **legacy IVR vendor** — Genesys, NICE, Cisco Contact Center ที่ยัง frame product เป็น phone tree; (3) **outsourcing consulting** ที่ขาย "how to run BPO" ไม่ใช่ "how to run agent + BPO hybrid". สำหรับ Thailand: **call center industry ที่ 100,000+ seat** (True, AIS, InfoQuest, MFEC, VSTECS) **ต้องเริ่ม pilot Presence-equivalent ที่ Thai-language voice model** — Thai-language latency + accent handling ยังเป็น edge case ที่ startup Thai (Botnoi, IApp, Amity Voice) มี opportunity ก่อน US vendor localize

## Sources
- [VentureBeat — OpenAI unveils Presence, a new platform that lets enterprises launch and manage realtime voice agents and chatbots](https://venturebeat.com/orchestration/openai-unveils-presence-a-new-platform-that-lets-enterprises-launch-and-manage-realtime-voice-agents-and-chatbots)
- [Help Net Security — OpenAI Presence connects AI agents to enterprise data with built-in guardrails](https://www.helpnetsecurity.com/2026/07/22/openai-presence-ai-agent-platform/)
- [Renascence — OpenAI Presence: Enterprise Voice & Chat Agents Resolve 75% of Contacts](https://www.renascence.io/news/6736/openai-presence-enterprise-voice-and-chat-agents-resolve-75-of-contacts)
- [Enterprise DNA — OpenAI Launches Presence for Enterprise Voice AI](https://enterprisedna.co/resources/news/openai-presence-enterprise-voice-agent-platform-2026/)
- [OpenAI News — Introducing OpenAI Presence](https://openai.com/index/introducing-openai-presence/)

---

## Audio script
OpenAI Presence enterprise agent platform ที่ launch limited GA 22 กรกฎาคม 2026 เก็บตัวเลข production ที่ควรค่าแก่การอ้างอิงในสัปดาห์ที่ผ่านมา. ต่างจาก ChatGPT Enterprise ที่เป็น B2B chatbot. Presence เป็น deployment management layer ที่ handle เรื่องที่ยากที่สุดของการรัน agent ใน production. connect กับ enterprise system. define capability boundary. test edge case ก่อน launch. improvement loop หลัง go live.

Metric ที่ OpenAI เปิด. 75% resolution rate. วัดจาก 1 888 GPT 0090. OpenAI's own English language phone support channel ที่ powered by Presence เอง. 3 ใน 4 call จบโดย agent ไม่ต้อง escalate มนุษย์. เป็น ratio ที่ Klarna Salesforce Help Agent ทำได้ในปี 2024 ถึง 2025 แต่ตอนนั้นเป็น text chat. voice ใน realtime latency นี่คือ threshold ใหม่.

ตัวเลขที่ 2. ลด 15 percentage point ใน handoff rate ใน 10 วัน. Codex powered improvement loop ใน Presence auto analyze conversation log identify prompt tool gap generate patch test บน replay และ deploy. cycle 10 วัน ทำให้ handoff rate ลด 15 percentage point ที่ OpenAI's own operation. evidence ว่า agent improvement ไม่จำเป็นต้องรอ human ML engineer tuning.

Early enterprise customer 3 ราย ครอบ 3 ทวีป. BBVA Mexico bank ที่ deploy customer support สำหรับ retail banking. SoftBank Corp sales development agent ที่ qualify inbound lead book meeting. Retail Insurance Australia IT service agent ที่ handle internal help desk. 3 customer นี้ deploy ผ่าน OpenAI Forward Deployed Engineer. ไม่ใช่ self service. ไม่ใช่ certified partner. OpenAI engineer ไปนั่งข้าง customer 4 ถึง 8 สัปดาห์.

Signal ใหญ่. 75% autonomous resolution ใน voice channel คือ threshold ที่เปลี่ยน BPO industry. call center BPO ทั่วโลก Concentrix TDCX Teleperformance TCS BPO ขายแรงงาน 8 ถึง 25 เหรียญต่อชั่วโมง. ถ้า Presence ปิด 75% ของ call cost per resolution ลดจาก 3 ถึง 8 เหรียญ ไปเหลือ 20 ถึง 80 เซนต์. ไม่ใช่ 10 ถึง 20 percent improvement. คือ order of magnitude.

ลด 15 pp handoff ใน 10 วัน คือ signal ที่สำคัญกว่า 75%. เพราะ 75% เป็น absolute number ที่ competitor จะเข้าใกล้ในไม่กี่ไตรมาส. แต่ improvement velocity 15 pp ต่อ 10 วัน แปลว่า Presence ปรับตัวเร็วกว่า Sierra AI Decagon ที่พึ่ง human ML engineer tune manual. อีก 6 ถึง 12 เดือน handoff rate อาจตกไปที่ 5 ถึง 10 percent.

Customer selection. OpenAI ไม่ launch Presence กับ tech company ที่ integration ง่าย. Launch กับ bank เม็กซิโก telecom ญี่ปุ่น insurance ออสเตรเลีย. 3 category ที่ IT stack ซับซ้อน compliance หนัก latency sensitive. ถ้า Presence work ที่นี่ จะ work ที่ enterprise segment ไหนก็ได้.

สำหรับ builder ที่สร้าง voice agent framework. Codex style improvement loop คือ feature ที่ควร ship. Presence's edge ไม่ได้อยู่ที่ voice model. อยู่ที่ loop ที่ auto analyze conversation log identify gap generate patch replay test และ deploy. ต้อง require 3 primitive. structured conversation logging. replay environment. code generation agent ที่ propose prompt tool change.

สำหรับ enterprise ที่ operate call center customer support IT service desk. ตอนนี้ต้องทำ 3 อย่างพร้อมกัน. pilot voice agent บน high volume low complexity queue. แก้ contract กับ BPO vendor ให้ include agent managed workflow ก่อน renewal. retrain frontline supervisor เป็น agent operator.

ผู้แพ้. BPO ระดับกลาง staff 5K ถึง 20K seat ที่พึ่งราคา scale แต่ไม่มี agent capability. legacy IVR vendor Genesys NICE Cisco Contact Center. outsourcing consulting ที่ขาย how to run BPO. Thailand call center industry ที่ 100,000 seat ต้องเริ่ม pilot Presence equivalent ที่ Thai language voice model.
