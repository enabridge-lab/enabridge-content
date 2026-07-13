---
date: 2026-07-14
slug: salesforce-help-agent-pay-per-resolution-2-dollar
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial isometric hero illustration of a giant glowing dashboard
  labeled "AGENTFORCE HELP AGENT" over a dark cinematic plane. In the
  center a large price tag reads "$2 / RESOLUTION" with a green check
  next to "AUTONOMOUS RESOLVE" and a red X next to "HUMAN ESCALATE".
  On the left, a small text panel reads "GA JULY 2026". On the right a
  bar chart shows a bar labeled "<10% SCALED PAST PILOT" glowing red.
  Silhouettes of tiny customers connect through voice, web, and chat
  icons into the dashboard. High-contrast cinematic navy-and-orange
  palette, bold text readable at 200px thumbnail, 1:1 aspect, no real
  human faces.
image: images/26-07-14-0609-04-salesforce-help-agent-pay-per-resolution-2-dollar.png
---

# Salesforce ship Agentforce Help Agent GA — $2 ต่อ resolution เท่านั้น, แก้ปัญหาที่ <10% ของลูกค้า scale ผ่าน pilot

## TL;DR
- Salesforce ประกาศ **Agentforce Help Agent** พร้อม **pay-per-resolution pricing $2/resolution** — จ่ายเฉพาะเมื่อ agent ปิด ticket แบบ autonomous ตั้งแต่ต้นจนจบ, ถ้าลูกค้า escalate ไปหาคนหรือเดินออกไม่พอใจ ไม่คิดเงิน; GA เดือน ก.ค. 2026
- Product deploy ได้ในไม่กี่นาทีบน voice/web/portal/messaging พร้อม library of actions (case management, appointment scheduling, order management, account management) — ตอบโจทย์ตัวเลขที่หนักที่สุดของ Agentforce: **<10% ของลูกค้า Salesforce scale ผ่าน pilot**, deployment time เฉลี่ย **5–11 เดือน**
- Pricing model นี้เป็นการยอมรับว่า **seat-based licensing ตายแล้วสำหรับ agent** — ทุก enterprise agent vendor รอบ 18 เดือนหน้าจะถูกกดดันให้ move ไป outcome-based pricing เดียวกัน

## เกิดอะไรขึ้น
Agentforce เป็น product line ที่ Salesforce ปั้นมาตั้งแต่ปลาย 2024 พร้อม Dreamforce ประกาศใหญ่โต — เข้าปี 2026 Marc Benioff บอกใน earning call ว่า ARR ทะลุ **$1.2B** จริงในไตรมาส Q1 FY27 (โต 205% YoY) — แต่ตัวเลขที่ analyst จับจ้องคือ **<10% ของลูกค้า Salesforce ที่ deploy Agentforce สามารถ scale ผ่าน pilot ไปสู่ production**, และ median time-to-value อยู่ที่ **5–11 เดือน** เทียบกับ SaaS traditional ที่ deploy ได้ในหลายสัปดาห์. ลูกค้า enterprise หลายรายเริ่มถามว่า "จ่าย seat license ต่อเดือนตอน pilot ล้มเหลว = จ่ายให้ Salesforce test product"

**Agentforce Help Agent** คือคำตอบ. Product เปิดในเดือน มิ.ย. — GA เดือน **ก.ค. 2026** — พร้อมสองสิ่งใหม่ที่ break pattern เดิม. หนึ่ง **deploy ในไม่กี่นาที** ไม่ใช่หลายเดือน: pre-built service agent ที่มี library of actions พร้อมใช้ (case management, appointment, order, account), connect เข้า company knowledge base + communication channel จากหน้าจอเดียว, ทำงานข้าม voice + web + portal + messaging ในตัว. สอง **pay-per-resolution pricing $2 flat per autonomous resolution** — ถ้า agent ปิด issue ตั้งแต่ต้นจนจบโดยไม่ต้องคน = จ่าย $2; ถ้าลูกค้าขอ human, เดินออกไม่พอใจ, หรือ resolution ไม่ complete = **$0**

Model นี้ break rule ที่ Salesforce ถือมา 25 ปี — seat-based license. Benioff เคยแย้งตัว **outcome pricing** ตั้งแต่ปี 2024 ว่า "จะทำ margin ให้หายหมด" แต่ตัวเลข <10% scaling เห็นได้ชัดว่า seat model กลายเป็น anti-adoption. Salesforce Ben, CXM, CIO magazine, SalesforceDevops ทั้งหมด frame move นี้ว่าเป็น **"huge pricing shift"** — ครั้งแรกที่ vendor SaaS ระดับ Big 5 commit ต่อ outcome-based pricing โดยไม่มี seat floor. เดา: ตัวเลข $2 คือ pricing point ที่ Salesforce คำนวณ break-even บน frontier LLM cost (probably ~$0.50–1.00 per resolution ที่ token cost) + margin สำหรับ human review + platform

## ทำไมสำคัญ
Pattern ที่กำลัง crystalize — **enterprise agent economics ไม่ compatible กับ SaaS seat licensing**. เมื่อ agent ทำงาน 24/7, ไม่มี concept ของ "log in", และ output-per-hour swing ตาม task type — การขาย license per seat กลายเป็น **misaligned incentive** ทันที: vendor อยากขายมาก, ลูกค้าต้องการ pay สำหรับผลจริง, agent quality ไม่ถูก measure ตรง. Salesforce เพิ่งยอมรับ (พร้อมกัน) ว่า pricing model เก่าเป็นเหตุผลหลักที่ <10% ของลูกค้าตัวเอง scale ไม่ผ่าน, และ commit ต่อ **outcome-first economics** — เป็น signal ที่ทุก enterprise agent vendor ต้องอ่านและ replan pricing sheet ของตัวเอง

เทียบกับ competition: **OpenAI Workspace Agents** เพิ่งเปลี่ยน pricing ไป credit-based (6 พ.ค.), **Microsoft Copilot** ยังยึด per-seat แต่มี message pack เสริม, **Zendesk AI Agent Copilot** และ **Intercom Fin** ขาย per-resolution มาก่อน Salesforce แต่ target SMB, ไม่ใช่ enterprise. Salesforce เป็นเจ้าแรกใน enterprise CRM tier ที่ commit outcome pricing เต็มตัว. Microsoft จะโดนกดดันหนักที่สุด — ถ้า Dynamics 365 Customer Service ยังคง seat model ในขณะที่ Salesforce ทำ $2/resolution, procurement decision จะเข้าข้าง Salesforce ในทุก RFP ปีนี้

signal ระยะยาว — **agent จะโดน measure ต่างจาก software ทั่วไป**. เดิม vendor SaaS ขาย feature; ต่อไป vendor ขาย outcome + SLA + audit trail. Zapier, Workato, n8n, UiPath, Automation Anywhere ทั้งวงการ automation ต้อง revisit pricing sheet ใน 12 เดือนหน้า. Analyst layer ใหม่จะเกิด — เดิมมี AI/LLM cost dashboard, ต่อไปจะมี **"resolution economics dashboard"** ที่ break-down ต่อ task ต่อ agent ต่อ resolution — เพราะ CFO ต้อง reconcile invoice จาก vendor ที่คิด $2 per resolution กับ internal cost + quality metric

## มุม AI Agent Platform
สำหรับ **builders**: revisit pricing model **ทันที**. ถ้า product คุณขาย seat license สำหรับ agent — เหลืออีก 12–18 เดือนก่อนตลาดบังคับให้ move ไป outcome. ทำ 3 อย่างในไตรมาสนี้: (1) instrument success signal ที่ measurable per task (resolution completeness, customer sat post-agent, no-escalation rate); (2) ออก **hybrid tier** ให้ลูกค้าเลือก seat หรือ outcome ก่อน commit; (3) build cost model ที่ break-even ที่ high-volume outcome flow (Salesforce ที่ $2 น่าจะ break-even ~40–60% autonomous rate). Vertical builder (legal, healthcare, finance) ได้เปรียบเพราะ resolution definition ชัด — automation ตอบ ticket, สรุปเอกสาร, ปิด case — vs horizontal chatbot ที่ยาก measure

สำหรับ **users/business**: (1) ก่อน sign Agentforce contract ใหม่, run pilot กับ Help Agent ที่ $2/resolution ก่อน — economics ชัด, no floor; ถ้า workflow มี escalation rate สูง ค่าใช้จ่ายจริงต่ำกว่า seat มาก; (2) ต่อรอง vendor อื่นด้วย benchmark $2/resolution ในการเจรจา — เมื่อ Salesforce ตั้ง reference price แล้ว ทุก customer service AI vendor ต้องอธิบายทำไมของตัวเองแพงกว่า; (3) build internal **"agent economics dashboard"** ที่ track cost per outcome, autonomous resolution rate, escalation reason — ถ้าไม่มี, CFO approve agent budget รอบต่อไปยาก. สำหรับ Thai enterprise ที่ customer service ราวใหญ่ (บริการโทรคมนาคม, ธนาคาร, สายการบิน) ตัวเลข $2 อาจแพงเกินสำหรับ Thai market — ต่อรองราคาต่ำกว่าที่ list, หรือขอ tier ตาม volume + local ARPU

สำหรับ **ecosystem**: **contact center as a service (CCaaS)** vendor (Genesys, Five9, NICE, Talkdesk) เจอ threat ตรง — Salesforce Help Agent ทำงาน voice/web/portal/messaging ในตัว, ไม่ต้องซื้อ layer เสริม. CCaaS ต้องเร่งจับ AI agent เข้า core product หรือ risk เป็น dumb pipe. ในทางกลับกัน **outcome measurement + evaluation infra** (Braintrust, Arize, Freeplay, LangSmith, Anthropic Console) ได้ tailwind ใหญ่ — ทุก vendor ที่จะเก็บ outcome pricing ต้อง prove outcome; ต้องการ instrumentation ที่ CFO/audit ตรวจสอบได้. คาด Anthropic + OpenAI จะออก first-party evaluation tier ในไตรมาสหน้า

## Sources
- [Huge Agentforce Pricing Shift: Salesforce Introduces Pay-Per-Resolution — Salesforce Ben](https://www.salesforceben.com/huge-agentforce-pricing-shift-salesforce-introduces-pay-per-resolution/)
- [Salesforce Launches Agentforce Help Agent That Deploys in Minutes and Only Charges for Resolutions — Salesforce Newsroom](https://www.salesforce.com/news/stories/agentforce-help-agent-announcement/)
- [Salesforce unveils AI Help Agent with pay-per-resolution pricing — CIO](https://www.cio.com/article/4189183/salesforce-unveils-ai-help-agent-with-pay-per-resolution-pricing.html)
- [Salesforce launches Help Agent to simplify AI customer service deployment — SiliconANGLE](https://siliconangle.com/2026/06/25/salesforce-launches-help-agent-simplify-ai-customer-service-deployment/)
- [Agentforce Help Agent: Strong on Setup, Better on Pricing — SalesforceDevops.net](https://salesforcedevops.net/index.php/2026/06/25/agentforce-help-agent-pay-per-resolution/)

---

## Audio script
Salesforce ประกาศ Agentforce Help Agent เข้า GA เดือนกรกฎาคม 2026 พร้อม pricing model ใหม่ที่เรียกว่า pay per resolution สองดอลลาร์ต่อการปิด case แบบ autonomous ตั้งแต่ต้นจนจบ ถ้าลูกค้าขอคุยกับคนหรือเดินออกไม่พอใจ ไม่คิดเงิน ศูนย์ดอลลาร์ Product deploy ได้ในไม่กี่นาที ทำงานข้าม voice web portal messaging ในตัว มี library of actions พร้อมใช้ case management appointment order management account management

ตัวเลขที่ต้องรู้ Agentforce ARR ทะลุ 1.2 พันล้านดอลลาร์ในไตรมาส Q1 FY27 โต 205 เปอร์เซ็นต์ปีต่อปี แต่ analyst จับจ้องว่า น้อยกว่า 10 เปอร์เซ็นต์ของลูกค้า Salesforce สามารถ scale Agentforce ผ่าน pilot ไปสู่ production ได้ deployment time เฉลี่ยห้าถึงสิบเอ็ดเดือน ลูกค้า enterprise เริ่มถามว่าจ่าย seat license ต่อเดือนตอน pilot ล้มเหลว เท่ากับจ่ายให้ Salesforce test product move ครั้งนี้ break rule ที่ Salesforce ถือมา 25 ปีคือ seat based license

Pattern ที่ crystalize คือ enterprise agent economics ไม่ compatible กับ SaaS seat licensing เมื่อ agent ทำงาน 24 ชั่วโมง ไม่มี concept ของ log in output per hour swing ตาม task type การขาย license per seat กลายเป็น misaligned incentive ทันที Salesforce เพิ่งยอมรับว่า pricing model เก่าเป็นเหตุผลหลักที่ scale ไม่ผ่านและ commit ต่อ outcome first economics

สำหรับ builder ที่ทำ agent product ต้อง revisit pricing ทันที ทำสามอย่าง instrument success signal per task ออก hybrid tier ให้ลูกค้าเลือก build cost model break even ที่ high volume outcome flow สำหรับ business ที่จะซื้อ agent ก่อน sign contract ใหม่ run pilot Help Agent ก่อนเพราะ economics ชัดไม่มี floor ต่อรอง vendor อื่นด้วย benchmark สองดอลลาร์ต่อ resolution สำหรับ CCaaS vendor เจอ threat ตรง ต้องเร่งจับ AI agent เข้า core product หรือกลายเป็น dumb pipe
