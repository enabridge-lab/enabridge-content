---
date: 2026-05-02
slug: 26-05-02-0624-03-salesforce-agentforce-operations-back-office-blueprints
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: Editorial illustration of an automated factory floor where invisible mechanical arms process invoices and documents in mid-air, with one human supervisor watching from a glass walkway above, minimal flat shapes, muted indigo and warm peach palette, dramatic top-down lighting, no text no logos no faces
image:
---

# Salesforce ขึ้น Agentforce Operations — agent ทำงาน back-office ครบ end-to-end ลด cycle time 50-70%, ลด manual task 80%

## TL;DR
- 29 เม.ย. — Salesforce ปล่อย **Agentforce Operations** ขึ้น GA: agent ทำงาน back-office (audit, onboarding, compliance, AP/AR, document extraction) แบบ **complete-not-just-orchestrate** + **30+ pre-built blueprints** สำหรับ vertical task
- ตัวเลขที่ Salesforce อ้าง: ลด **cycle time 50-70%**, ลด **manual task 80%**, อัปโหลด process ผ่าน **Lucidchart/Word/drawing** แล้ว auto-digitize เป็น multi-step workflow
- Customer base ที่เปิดใช้: **18,500 ราย** (vs 12,500 ไตรมาสก่อน), **9,500 ดีลเสียเงิน**; Agentforce + Data 360 ARR แตะ **$1.4B** เติบโต **114% YoY** = product line โตเร็วที่สุดในประวัติ Salesforce

## เกิดอะไรขึ้น

วันที่ 29 เม.ย. Salesforce announce **Agentforce Operations** เปิด GA ทันที — extension ของ Agentforce platform ที่ขยายจาก front-office (sales, service, marketing) ลงสู่ **back-office** (finance, operations, compliance) ฟีเจอร์หลัก: agent ที่ "complete the work" ไม่ใช่แค่ "orchestrate" — สามารถ extract data จาก document complex (invoice หลายภาษา, contract, customs form), run computation (credit model, currency conversion), update record ใน ERP, identify compliance gap แล้ว flag ขึ้น human reviewer เฉพาะตอนต้องการ approval

จุดเด่นทาง engineering: **process digitization ผ่าน upload** — user upload Lucidchart diagram, Word document, หรือแม้กระทั่ง drawing ของ workflow แล้ว Agentforce Operations แปลงเป็น multi-step workflow มี agent มอบหมายให้ทำในแต่ละขั้น และ Salesforce ส่งมา **30+ pre-built blueprints** สำหรับ task ที่พบบ่อย: invoice auditing, customer onboarding, purchase order rescheduling, compliance reporting, AP/AR reconciliation, expense management, data quality checks

ตัวเลข aggregate ของ Agentforce platform (Q3 FY26 = ปี Salesforce, ตรงกับ ม.ค.-มี.ค. 2026 ปฏิทิน): **18,500 ลูกค้า** (เพิ่ม 6,000 ราย QoQ), **9,500 paid deal**, accounts in production เพิ่ม **70% QoQ**, ARR ของ Agentforce + Data 360 รวม **$1.4 พันล้าน** ที่ +114% YoY = product line โตเร็วที่สุดในประวัติ Salesforce — แม้เร็วกว่า Service Cloud ตอน 2017 หรือ Marketing Cloud ตอน 2020 เหตุที่ Salesforce ลง back-office ตอนนี้คือ Marc Benioff ใน earnings call Q3 FY26 บอก "front-office Agentforce ไม่ขยายต่อแบบ exponential ได้แล้ว แต่ back-office เป็น white space ที่ใหญ่กว่า 3-4 เท่า — finance, ops, HR, compliance ครอบ 60-70% ของ enterprise headcount"

ที่ใต้ฉาก: Salesforce ใช้ Anthropic Claude เป็น primary model (เปิดเผยใน AWS re:Invent 2025) + OpenAI GPT-5 รอง ทำให้ Agentforce Operations กลายเป็น **largest commercial deployment ของ Claude ในระดับ end-user-facing app** ที่ไม่ใช่ Anthropic เอง — คาดว่า monthly token volume ของ Salesforce-Anthropic อยู่ระดับ trillion-token เดือนเดียว

## ทำไมสำคัญ

**Front-to-back office = 3-4x TAM expansion** Salesforce ใช้ playbook คลาสสิก: launch product ใน segment เล็กก่อน (front-office sales agent), ได้ data + reference ลูกค้า, ขยายเข้า segment ใหญ่กว่า — ตอนนี้เข้า back-office ที่ TAM 60-70% ของ enterprise headcount = ใหญ่กว่า front-office 3-4x ที่ ARR $1.4B ตอนนี้ ถ้า penetrate back-office ในอัตราเดียวกับ front-office (3 ปีไปสู่ ~$1.4B) ในอีก 24 เดือนจะแตะ $5-7B ARR = ~60% ของ Salesforce total revenue

**"Process digitization จาก document" = killer feature ที่จะ commoditize iPaaS** การ upload Lucidchart/Word/drawing แล้ว auto-generate multi-step agent workflow คือ solution ที่ Workato, Zapier, Make ขายในรูป "low-code integration platform" มา 8 ปี — ตอนนี้ Salesforce ทำให้ "no-code from document" ได้แล้ว iPaaS ที่ขายเฉพาะ trigger-action graph ไม่มี vertical blueprint จะถูกบีบในรอบ 12 เดือน — Workato/Zapier ต้อง pivot ไป "agent orchestration ที่มี blueprint vertical" ใน Q3 หรือเสีย mid-market

**ตำแหน่งของ ServiceNow + Microsoft Power Platform** ทั้งคู่มี back-office ดีกว่า Salesforce อยู่แล้ว แต่ตำแหน่ง agent ของทั้งคู่ไม่เท่ากัน ServiceNow Now Assist agent build เอง stack-locked กับ Now Platform; Microsoft Copilot Studio ใช้ MCP-first และมี Fabric integration; Salesforce Agentforce Operations อยู่ตรงกลาง — ใช้ Claude/GPT (multi-model) แต่ลูกค้าต้องอยู่ใน Salesforce stack ผมเชื่อ ServiceNow มี window 6-9 เดือน respond ก่อน Salesforce กิน mid-large enterprise back-office; ส่วน Microsoft จะ Build 2026 (พ.ค. 19-22) น่าจะตอบด้วย "Power Platform Operations" ที่คล้าย Agentforce Operations แต่ใช้ Fabric เป็น data plane

## มุม OpenBridge

**Window แคบลงในตลาด mid-market ASEAN — ลงตอนนี้หรือเสีย** ที่ 04-30 brief พูดถึง Appian + MCP + Snowflake เป็น blueprint ที่ OpenBridge ต้อง mirror ใน mid-market ASEAN — ตอนนี้เพิ่ม pressure จาก Salesforce ลงมา back-office ASEAN reseller (Aware, AIS Cloud, Krungthai-AXA) จะมี Salesforce Agentforce Operations ใน 3-6 เดือน mid-market Thai ที่ยังไม่ได้ใช้ Salesforce (~70% ของ enterprise mid-market ไทย) คือ window ของ OpenBridge — ต้อง ship MVP ของ "back-office agent ที่ใช้ Document Studio/Word/PDF เป็น input" ภายใน 90 วัน

**Productize 5 vertical blueprints** ที่ OpenBridge ทำได้ใน 60-90 วันบน workflow primitive ที่มีอยู่: (1) **AP/AR reconciliation** สำหรับ SME ที่ใช้ Express/AccCloud/PEAK; (2) **customs declaration auto-fill** สำหรับ logistics + e-commerce; (3) **invoice 3-way match** สำหรับ retail chain; (4) **employee onboarding** ที่เชื่อม HRIS เก่าผ่าน OCR + RPA; (5) **compliance log generation** สำหรับ BoT/SEC submission คิด pricing $200-1,500/mo per blueprint per company — เทียบ Salesforce Agentforce Operations $50-300/agent/mo (ทั้ง stack) — OpenBridge ขายเป็น vertical blueprint ที่ลูกค้าซื้อ 2-3 ตัวพอรอบรู้ใช้ stack ใหญ่

**Reframe sales pitch จาก "integration" เป็น "process digitization"** ลูกค้า Thai mid-market พูดภาษา "ลด manual work" ไม่ใช่ "iPaaS connector" — ถ้า OpenBridge เปลี่ยน sales deck ให้ pitch "อัปโหลด process flowchart → ได้ agent ทำงานแทน" ภายใน 30 วัน + เก็บ case study 2-3 ลูกค้าใน Q2 จะได้ wedge ที่ Salesforce reseller เข้าไม่ทัน

## Sources
- [Salesforce Launches Agentforce Operations to End Back-Office Bottlenecks | Salesforce Newsroom](https://www.salesforce.com/news/stories/agentforce-operations-announcement/)
- [Salesforce introduces Agentforce Operations to automate outdated back-office tasks | SiliconANGLE](https://siliconangle.com/2026/04/29/salesforce-introduces-agentforce-operations-automate-outdated-back-office-tasks/)
- [Salesforce expands beyond the front office with Agentforce Operations | CIO](https://www.cio.com/article/4164708/salesforce-expands-beyond-the-front-office-with-agentforce-operations.html)
- [Agentforce Operations tackles workflow orchestration | TechTarget](https://www.techtarget.com/searchcustomerexperience/news/366642340/Agentforce-Operations-tackles-workflow-orchestration)
- [While everyone talks about an AI bubble, Salesforce quietly added 6,000 enterprise customers in 3 months | VentureBeat](https://venturebeat.com/technology/while-everyone-talks-about-an-ai-bubble-salesforce-quietly-added-6-000)

---

## Audio script
วันที่ 29 เมษา Salesforce ปล่อย Agentforce Operations ขึ้น GA ทันที เป็น extension ของ Agentforce ที่ขยายจาก front-office ลงสู่ back-office — finance, operations, compliance, HR ฟีเจอร์ที่ผมว่าน่าสนใจสุดคือ agent "complete the work" ไม่ใช่แค่ orchestrate — สามารถ extract data จาก document, run computation, update ERP, flag compliance gap ขึ้น human reviewer เฉพาะตอน need approval อีกอันคือ process digitization ผ่าน upload — user upload Lucidchart, Word doc, หรือแม้กระทั่ง drawing ของ workflow แล้วระบบแปลงเป็น multi-step agent workflow + มี 30 pre-built blueprints สำเร็จ ตัวเลขที่ Salesforce อ้าง — ลด cycle time 50 ถึง 70%, ลด manual task 80% สเกล Agentforce ตอนนี้ — 18,500 ลูกค้า, 9,500 paid deal, ARR รวม Data 360 แตะ 1.4 พันล้านดอลลาร์ +114% YoY = product line โตเร็วที่สุดในประวัติ Salesforce นี่คือ playbook คลาสสิก — front-office ก่อน, ได้ data + reference, ขยายเข้า back-office ที่ TAM ใหญ่กว่า 3-4 เท่า ในอีก 24 เดือนน่าจะแตะ 5 ถึง 7 พันล้าน ARR สำหรับ OpenBridge — Salesforce reseller ASEAN (Aware, AIS Cloud) จะมี Agentforce Operations ใน 3 ถึง 6 เดือน mid-market Thai ที่ยังไม่ได้ใช้ Salesforce ราว 70% คือ window ของ OpenBridge ต้อง ship MVP ของ back-office agent ที่ใช้ document เป็น input ภายใน 90 วัน + productize 5 vertical blueprints — AP/AR reconciliation, customs declaration, invoice 3-way match, employee onboarding, compliance log สำหรับ BoT submission ราคา 200 ถึง 1,500 ดอลลาร์ต่อเดือนต่อ blueprint และเปลี่ยน sales pitch จาก integration เป็น process digitization — ลูกค้าไทย mid-market พูดภาษา "ลด manual work" ไม่ใช่ "iPaaS connector" ครับ
