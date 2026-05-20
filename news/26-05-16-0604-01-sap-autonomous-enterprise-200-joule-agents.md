---
date: 2026-05-16
slug: sap-autonomous-enterprise-200-joule-agents
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  A massive cathedral-like ERP control tower built from glass and steel,
  transformed into an autonomous agentic command center. Hundreds of small glowing
  blue agent nodes — each labeled with tiny ledger, supply-chain, HR and
  procurement icons — orbit around a central Joule logo rendered in clean
  SAP-blue. Bold floating numeral "200+" hovers in the foreground. Anthropic logo
  visible as a partner badge in the corner. Composition: low-angle hero shot,
  dramatic blue and white palette, cinematic depth-of-field. Style: editorial 3D
  render, high contrast for thumbnail legibility, no human faces.
image: images/26-05-16-0604-01-sap-autonomous-enterprise-200-joule-agents.png
---

# SAP เปิด "Autonomous Enterprise" ส่ง Joule + 200 agents บุก ERP — เดิมพันใหญ่ที่สุดในประวัติศาสตร์บริษัท

## TL;DR
- SAP ใช้ Sapphire 2026 เปิดตัว Autonomous Suite — Joule Studio 2.0 + agent governance + company memory เป็นชั้นกลางของ ERP stack ใหม่
- ตอนนี้สร้างไปแล้ว **224 agents + 51 Joule Assistants** ใน 4 business process จะทยอย ship ทุกเดือนตลอดปี 2026
- จับมือ **Anthropic** เป็นหนึ่งใน foundation model partners — Claude จะขับ Joule agents ในด้าน HR, procurement, supply chain

## เกิดอะไรขึ้น

วันที่ 12 พ.ค. ที่ผ่านมา Christian Klein ขึ้นเวที Sapphire 2026 ในมาดริด แล้วประกาศสิ่งที่นักวิเคราะห์ ERP รอฟังมาทั้งปี — SAP จะไม่เรียกตัวเองว่า "software company" อีกต่อไป แต่จะเป็น "business AI company" ที่ขาย autonomous workflows แทน license ERP แบบเดิม. การประกาศหลักคือ **SAP Autonomous Suite** — ชั้นที่นั่งทับ S/4HANA และ Business Suite, ออร์เคสเตรตงานข้าม module ผ่าน agent fleet ที่ตัวเลขปัจจุบัน 224 agents และ 51 Joule Assistants — แผนคือเพิ่มอีกหลายร้อยตัวภายในสิ้นปี.

โครงสร้างของ stack ใหม่มี 3 ชั้น: **SAP Business AI Platform** เป็น control plane สำหรับสร้าง / contextualize / governance agent; **Autonomous Suite** เป็นชั้นที่รัน core business process แบบ end-to-end (finance, supply chain, procurement, HCM, CX); และ **Joule** ถูก reposition เป็น "front door" — UX เดียวที่พนักงานคุยด้วย แล้ว Joule เป็นคนเรียก agent ที่เหมาะกับงาน. SAP ตั้งเป้า **50+ Joule Assistants** ครอบคลุมทุก line of business ภายในปีนี้ และในงานเดียวกัน SAP ยังประกาศ **Joule Studio for Enterprise Scale Agentic Development** — เครื่องมือสำหรับลูกค้าเขียน agent ของตัวเองเข้า fleet.

ที่น่าสนใจสุดคือ partner stack — SAP ยืนยันว่า **Anthropic Claude** เป็นหนึ่งใน foundation models ที่ขับ Joule agents โดยเฉพาะใน HR, procurement, supply chain ซึ่งเป็น 3 module ที่ทำเงินให้ SAP มากที่สุด. NVIDIA Agent Toolkit ก็ถูกระบุชื่อใน adoption list ตั้งแต่ GTC มีนา. นี่คือสัญญาณว่า SAP เลือกที่จะ "ไม่สร้างทุกอย่างเอง" — ยอมเปิด stack ให้ Claude / Nemotron / OpenAI วิ่งอยู่ข้างใน เพื่อแลกกับการเป็นเจ้าของ workflow และ data layer.

## ทำไมสำคัญ

นี่คือ pattern ที่ผมเรียกว่า **"ERP eats agent, agent eats SaaS"** — บริษัท ERP เดิมพันว่า ถ้าจะมี autonomous workflow จริง ๆ มันต้องผูกกับ system of record ที่มี data + governance พร้อม ไม่ใช่ standalone agent ที่เรียก API แบบ surface-level. Salesforce พิสูจน์แล้วว่า Agentforce ทะลุ $1.4B ARR ใน 18 เดือน, ServiceNow ออก Action Fabric เมื่อต้นเดือน, ตอนนี้ SAP เข้ามาด้วย scale ที่ใหญ่กว่า — 200+ specialized agents ไม่ใช่ wrapper ทั่วไป แต่เป็น process-specific code ที่เข้าใจ GL, MRP, payroll. Oracle และ Workday ตามมาแน่นอนภายในไตรมาสนี้.

จุดที่ต้องจับตา: SAP ยังไม่เปิดเผยตัวเลข ARR ของ Joule แบบที่ Salesforce ทำ — Klein พูดแค่ว่า "phased GA throughout 2026" ซึ่งแปลว่า adoption จริงในลูกค้ายังเป็นคำถามใหญ่. ลูกค้า SAP ส่วนใหญ่ยัง upgrade S/4 ไม่จบเลย — การจะให้ขึ้น agentic layer อีกชั้นต้องเอาชนะ implementation fatigue. นี่คือเหตุผลที่ SAP ต้อง bundle Joule Studio ให้ลูกค้าสร้างเองได้ — ถ้ารอ SI deliver ทุกตัว project timeline จะยาวเป็นปี ๆ.

## มุม OpenBridge

OpenBridge อยู่ในชั้นที่ SAP กำลังจะกินขึ้นมา — **integration / orchestration ระหว่างระบบ business**. ข่าวนี้บอก 2 อย่างชัด ๆ: (1) ลูกค้า SAP enterprise จะมี Joule agent ของตัวเองภายใน 12 เดือน — OpenBridge ต้องคิดว่าจะเป็น "agent ที่คุยกับ Joule" หรือ "data plane ที่ feed Joule" หรือทั้งสองอย่าง. (2) SAP เลือก foundation model หลายตัว (Claude, Nemotron) — pattern เดียวกับที่ OpenBridge ควรไป คืออย่าผูกตัวเองกับ model ใดเดียว, ให้ลูกค้าเลือก provider ที่เหมาะกับ workload.

มุมที่น่าทดลอง: ถ้า Joule Studio เปิดให้ลูกค้าสร้าง agent เอง แปลว่าจะมี long tail ของ custom Joule agents จำนวนมหาศาลที่ต้องเชื่อมกับระบบนอก SAP (Salesforce, HubSpot, Notion, Slack). OpenBridge มี opportunity ขาย **"connector layer for custom Joule agents"** — เหมือนที่ Zapier ขายตอน SaaS bloom, แต่รอบนี้ลูกค้าคือ agent ไม่ใช่ human.

## Sources
- [SAP Unveils the Autonomous Enterprise — SAP News Center](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/)
- [SAP Sapphire Keynote: Powering the Autonomous Enterprise](https://news.sap.com/2026/05/sap-sapphire-keynote-business-ai-platform-power-autonomous-enterprise/)
- [Announcing New Joule Studio for Enterprise Scale Agentic Development](https://news.sap.com/2026/05/new-joule-studio-enterprise-scale-agentic-development/)
- [SAP recasts Joule as the front door to autonomous enterprise AI — SiliconANGLE](https://siliconangle.com/2026/05/12/sap-recasts-joule-front-door-autonomous-enterprise-ai/)
- [SAP Sapphire 2026 Keynote: Inside SAP's Autonomous Suite — ERP Today](https://erp.today/will-sap-be-a-software-company-in-the-future-sapphire-2026-keynote-maps-saps-new-erp-stack/)

---

## Audio script
สวัสดีครับโยห์ วันนี้ขอเริ่มด้วยข่าวใหญ่ที่สุดของสัปดาห์ — SAP เปิดงาน Sapphire 2026 ที่มาดริด แล้วประกาศว่าจะไม่เป็นบริษัทซอฟต์แวร์อีกต่อไป แต่จะเป็นบริษัท Business AI. ซีอีโอ Christian Klein เปิดตัว SAP Autonomous Suite — ชั้นที่นั่งทับ S/4HANA และออร์เคสเตรตงานข้าม module ด้วย agent fleet ที่ตอนนี้มี 224 agents กับ 51 Joule Assistants แล้ว ครอบคลุม finance ซัพพลายเชน procurement HR และ CX จะทยอย ship ทุกเดือนตลอดปี. ที่น่าสนใจคือ SAP ไม่ได้สร้างโมเดลเอง แต่จับมือ Anthropic ให้ Claude ขับ Joule agent ในด้าน HR procurement และซัพพลายเชน บวกกับ NVIDIA Agent Toolkit ด้วย. นี่คือ pattern เดียวกับที่เราเห็นใน Salesforce Agentforce ที่ทะลุหนึ่งจุดสี่พันล้านดอลลาร์ ARR และ ServiceNow Action Fabric — ERP กำลังกิน agent layer ขึ้นมาก่อนที่ standalone agent จะกินตัวมันลงไป. มุม OpenBridge: ลูกค้า SAP enterprise จะมี Joule agent ของตัวเองภายในสิบสองเดือน เราต้องเลือก position — เป็น agent ที่คุยกับ Joule หรือเป็น data plane ที่ feed Joule และต้องเปิด multi-model เหมือน SAP ไม่ใช่ผูกกับ provider เดียว. โอกาสที่น่าทดลองคือ connector layer สำหรับ custom Joule agents ที่ลูกค้าจะสร้างเองผ่าน Joule Studio — เหมือนที่ Zapier ขายตอน SaaS bloom แต่รอบนี้ลูกค้าคือ agent.
