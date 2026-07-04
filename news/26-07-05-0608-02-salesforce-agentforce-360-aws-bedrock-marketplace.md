---
date: 2026-07-05
slug: salesforce-agentforce-360-aws-bedrock-marketplace
topic: openbridge-trend
reading_time_min: 3
sources: 3
image_prompt: |
  A polished corporate deal scene: two glass towers connected by a glowing bridge, tower left labeled "SALESFORCE TRUST BOUNDARY", tower right labeled "AWS BEDROCK". A huge banner above the bridge reads "AGENTFORCE 360 FOR AWS". A subtitle billboard below reads "AWS MARKETPLACE — ONE INVOICE". Floating icons above the bridge labeled "CLAUDE", "NOVA LITE", "NOVA PRO", all wrapped in a translucent blue security perimeter. Inside the perimeter, a "CROWDSTRIKE" logo card labeled "CUSTOMER". Editorial isometric style, cool corporate palette, high contrast, 1:1 aspect, readable at 200px thumbnail, no real human faces.
image: images/26-07-05-0608-02-salesforce-agentforce-360-aws-bedrock-marketplace.png
---

# Salesforce จับมือ AWS ปล่อย Agentforce 360 for AWS ขึ้น Marketplace — LLM traffic อยู่ใน Trust Boundary, จ่ายเข้า AWS invoice เดียว

## TL;DR
- Salesforce + AWS ประกาศ **Agentforce 360 for AWS** วางขายบน **AWS Marketplace** (ประกาศทางการรอบล่าสุด 2-3 ก.ค.) — offering แรกที่ Salesforce ยอม "หย่อน" AI/procurement เข้าไปในบ้าน hyperscaler ระดับนี้
- **Salesforce Trust Boundary** — LLM traffic ทั้งหมดวิ่งอยู่ใน private AWS cloud ของ Salesforce (Hyperforce), ข้อมูลลูกค้าไม่ leak ออกไป external, ไม่ถูกใช้ train foundation model
- Atlas Reasoning Engine ใช้ **Claude ผ่าน Amazon Bedrock + Amazon Nova Lite/Nova Pro**; **CrowdStrike** เป็นลูกค้าตัวอย่างที่ deploy governed agent ในเพอริมิเตอร์นี้แล้ว
- Procurement angle: consolidated billing ผ่าน AWS EDP + pre-approved budget + private pricing = CFO/CIO ตัด friction ของ RFP ได้เยอะ

## เกิดอะไรขึ้น
Salesforce กับ AWS ประกาศ **Agentforce 360 for AWS** — offering เดียวที่รวม **compute (AWS Hyperforce) + agent runtime (Agentforce Atlas Reasoning Engine) + model access (Claude on Bedrock + Amazon Nova) + procurement (AWS Marketplace)** ให้อยู่ในสัญญาเดียว ปกติ Salesforce ยังพยายาม lock ลูกค้าอยู่ใน Salesforce cloud + Anthropic direct — รอบนี้ยอมเปิดให้ **Bedrock อยู่ตรงกลาง** พร้อมเปิดให้ **CrowdStrike** เป็น showcase customer ที่ deploy secure agent inside Salesforce Trust Boundary + running on Bedrock ในบ้านลูกค้าเอง

โครงสร้าง Trust Boundary คือจุดขายจริง — LLM traffic ทั้งหมดวิ่งอยู่ใน private AWS cloud ของ Salesforce (Hyperforce architecture), ข้อมูลลูกค้าไม่ leak ออกไป external model provider, ไม่ถูกใช้ train foundation model ตอบโจทย์ CISO ที่เจอ objection จาก CFO/CTO เรื่อง "จะเอา CRM data ป้อน LLM ยังไงให้ปลอดภัยพอ SOC 2 / PDPA / GDPR" — คำตอบเดิมของ Salesforce คือ "อยู่ใน Salesforce cloud อย่างเดียว", รอบนี้คำตอบขยายเป็น "อยู่ใน Trust Boundary ของ Salesforce แต่วิ่งบน Bedrock ที่ลูกค้าอาจเคย audit ไว้แล้ว"

จุดขายอีกด้านคือ AWS Marketplace — customer ที่มี AWS EDP (Enterprise Discount Program) อยู่แล้วสามารถ push Agentforce spend เข้า commit เดียวกับ AWS ได้, private pricing + consolidated billing, IT procurement ไม่ต้องเปิด vendor onboarding cycle ใหม่. Salesforce ไม่เปิดตัวเลข gross margin ที่ต้องแบ่งให้ AWS ผ่าน Marketplace, แต่ signal ชัดว่ายอมแลกเพราะ **deal velocity คุ้ม** — ปกติ enterprise procurement cycle ของ Salesforce ใหม่กินเวลา 4-9 เดือน, ผ่าน Marketplace ตัด vendor onboarding ได้ 60-70%

## ทำไมสำคัญ
Pattern ที่ต่างจาก 6 เดือนก่อนคือ Salesforce ยอม "แบ่งของ" กับ AWS ให้มากกว่าเดิม — เพราะ Agentforce Help Agent เพิ่งเข้า GA พร้อม **pay-per-resolution $2** และ ARR $2.9B เมื่อสัปดาห์ที่แล้ว, Salesforce จำเป็นต้อง scale distribution ให้ทัน commitment ที่ประกาศไปแล้ว วิธีที่เร็วที่สุดคือ AWS Marketplace ที่มี Fortune 500 EDP customer อยู่แล้วเป็นแสนราย — โดยไม่ต้องเปิด direct sales pipeline ใหม่

เทียบ Microsoft Frontier Company ที่เพิ่งประกาศ 2 ก.ค. — Microsoft เลือกเดินสูตร **"ส่ง 6,000 engineer เข้าไปฝังตัว"** ส่วน Salesforce+AWS เลือกสูตร **"รวม compute + model + agent + billing ให้ CFO อ่านเข้าใจใน 1 หน้า"**. สองสูตรกำลังชนกันที่ CIO desk เดียวกัน — CIO เลือกจ่ายค่า professional service (Microsoft Frontier) หรือค่า infrastructure margin (Salesforce+AWS). สองแนวทางจะแบ่ง Fortune 500 workload กันไปคนละครึ่ง

Signal ต่อคู่แข่ง Salesforce (Oracle Fusion, ServiceNow AI Agent Fabric, Microsoft Dynamics 365 Copilot) — ถ้ายังไม่มี "on Bedrock" / "on Azure Marketplace" listing ที่ทำ contract velocity ระดับเดียวกัน จะแพ้ที่ **procurement step ไม่ใช่ที่ product feature**. Oracle Fusion SCM ที่เพิ่ง GA agentic supplier module เมื่อสัปดาห์ก่อน ก็ต้องออกโครงสร้าง cloud-neutral ตามภายในไตรมาสนี้ ไม่งั้นเสียลูกค้า EDP 5 พันบัญชีที่ AWS มีอยู่

## มุม AI Agent Platform
- **Builders** — SaaS ที่ยัง lock ลูกค้าอยู่ใน cloud ตัวเอง + billing ตัวเองต้องเริ่มคำนวณ margin trade-off: ยอมแบ่ง 5-10% ให้ marketplace เพื่อได้ deal velocity หรือรักษา margin แต่โดน bypass. **Agent framework**: ที่ hard-code endpoint ของ vendor เดียวจะถูก compress — enterprise ต้องการ agent runtime ที่รู้จัก swap ระหว่าง **Bedrock / Vertex AI / Azure AI Foundry** ตาม procurement scenario (บาง workload กำหนด region + cloud specific)

- **Users/business ในไทย** — บริษัทไทยที่ใช้ Salesforce + AWS อยู่แล้ว (SCB, KTC, AIS, retail chain หลายเจ้า) ควรถามทีม procurement ทันทีว่า EDP ปัจจุบัน apply Agentforce 360 for AWS ได้ไหม — ตัดขั้นตอน vendor onboarding ประจำปีทิ้ง. **CISO ต้อง audit Trust Boundary architecture ก่อน commit** — ประเด็นจริงคือ log/audit trail ของ Bedrock call ไปที่ region ไหน (Singapore / Tokyo?), กี่วัน retention, PDPA compliance ต่อ cross-border transfer เขียนไว้ในสัญญามาตรฐานหรือต้องเจรจา

- **Ecosystem** — AWS ได้ตัวเลข marketplace ARR + billed compute ที่จับต้องได้; Salesforce ได้ velocity; Anthropic ได้ workload ผ่าน Bedrock ที่ margin ต่ำกว่า direct API แต่ volume สูงและ predictable; **loser = SI ที่ขาย custom integration Salesforce-AWS ที่จะถูก platform ทำแทนหมด** — SI ต้อง reposition เป็น business process consulting + change management

## Sources
- [Salesforce and AWS Deepen Collaboration to Launch Agentforce 360 for AWS — Salesforce](https://www.salesforce.com/news/stories/agentforce-360-for-aws-announcement/)
- [Salesforce Launches Agentforce 360 for AWS on AWS Marketplace — Contact Center Technology Insights](https://contactcentertechnologyinsights.com/news/salesforce-agentforce-360-aws-marketplace-launch)
- [Salesforce brings Agentforce 360 for AWS to AWS Marketplace — Techzine Global](https://www.techzine.eu/news/applications/136984/salesforce-brings-agentforce-360-for-aws-to-aws-marketplace/)

---

## Audio script
วันนี้เรามีข่าวใหญ่จาก Salesforce กับ AWS ที่ประกาศ Agentforce 360 for AWS วางขายบน AWS Marketplace อย่างเป็นทางการ ต่างจาก 6 เดือนก่อนที่ Salesforce ยัง lock ลูกค้าอยู่ใน cloud ตัวเอง รอบนี้ยอมเปิดให้ Bedrock อยู่ตรงกลาง โดยที่ LLM traffic ทั้งหมดวิ่งอยู่ใน Salesforce Trust Boundary ซึ่งเป็น private AWS cloud ของ Salesforce เอง ข้อมูลลูกค้าไม่ leak ออก ไม่ถูกใช้ train foundation model นอกบริษัท จุดขายที่จริงจังคือ Atlas Reasoning Engine เลือกใช้ Claude ผ่าน Bedrock กับ Amazon Nova Lite Nova Pro ได้ CrowdStrike เป็น showcase customer แรกที่ deploy agent inside perimeter นี้แล้ว ที่ CFO ชอบมากคือฝั่ง procurement customer ที่มี AWS EDP อยู่แล้วสามารถ push Agentforce spend เข้า commit เดียวกับ AWS ได้ ประหยัด vendor onboarding cycle ที่ปกติกิน 4 ถึง 9 เดือน ตัดได้เกิน 60 เปอร์เซ็นต์ นี่คือ signal ใหญ่ต่ออุตสาหกรรม Oracle Fusion ServiceNow Microsoft Dynamics ต้องมี listing แบบเดียวกันบน Marketplace ไม่งั้นแพ้ที่ procurement step ไม่ใช่ที่ product เทียบกับ Microsoft Frontier Company ที่ประกาศเมื่อวันพฤหัสฯ Microsoft เลือกเดินสูตรส่ง engineer หกพันคนเข้าไปฝังตัว ส่วน Salesforce กับ AWS เลือกสูตรรวมทุกอย่างในสัญญาเดียวให้ CFO อ่านเข้าใจ สองสูตรจะแบ่ง Fortune 500 workload กันไปคนละครึ่ง สำหรับธุรกิจไทยที่ใช้ Salesforce กับ AWS อยู่แล้ว ควรคุยกับทีม procurement เลยว่า EDP ปัจจุบันครอบตัวนี้ได้ไหม แต่ CISO ต้อง audit ก่อนว่า log กับ audit trail ของ Bedrock call ไปที่ region ไหน retention กี่วัน PDPA cross-border transfer อยู่ในสัญญามาตรฐานหรือต้องเจรจา ถึงจะ deploy production ได้จริง
