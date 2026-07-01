---
date: 2026-07-01
slug: salesforce-agentforce-help-agent-pay-per-resolution
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of a giant coin-operated turnstile at the
  entrance of a customer-service hall. Each turnstile arm has a bold
  "$2" glowing tag. Above, a huge sign reads "PAY ONLY WHEN RESOLVED".
  In the background, a wall of channel icons — voice waveform, chat
  bubble, portal window, SMS — all flowing into a single Agentforce
  console labeled "HELP AGENT". A small counter beside reads
  "4.3M INQUIRIES · 70% AUTONOMOUS" in ticker style. Salesforce cloud
  logo in the corner. Cinematic isometric editorial style, deep navy
  and Salesforce sky-blue palette, ultra-sharp text rendering for
  200px thumbnail readability, 1:1 aspect ratio, no real human faces.
image: images/26-07-02-0609-02-salesforce-agentforce-help-agent-pay-per-resolution.png
---

# Salesforce เปิด Agentforce Help Agent — เก็บเงิน $2 ต่อ "การแก้ปัญหาสำเร็จ" เท่านั้น, ล้ม SaaS seat pricing ทั้งวงการ

## TL;DR
- 1 ก.ค. — Salesforce ประกาศ **Agentforce Help Agent** GA เดือน ก.ค. นี้ (Summer '26 release) — prebuilt customer service agent + **outcome-based pricing $2 ต่อการ resolve autonomous เสร็จ**. ลูกค้าขอคุยกับ human = ไม่คิดเงิน
- Deploy "ในไม่กี่นาที" ครอบทุก channel (voice / web / portal / SMS) — Salesforce เอง dogfood ผ่าน help.salesforce.com: **4.3 ล้าน inquiries, resolve autonomous 70%**
- Model shift ที่ใหญ่กว่า product — Salesforce เป็น **enterprise SaaS incumbent รายแรก** ที่ยอมทิ้ง per-seat / per-conversation ไปเป็น per-outcome. Analyst ชี้ว่านี่คือ "answer" ต่อ Gartner report เมื่อวันเดียวกันที่บอก $234B SaaS spend เสี่ยง disruption จาก agentic AI

## เกิดอะไรขึ้น

Salesforce ประกาศ **Agentforce Help Agent** เป็น GA ในช่วงเดือนกรกฎาคม 2026 พร้อม pricing model ใหม่ที่ชื่อว่า **pay-per-resolution** — คิดเงิน **$2 ต่อการแก้ปัญหาลูกค้าที่ agent ทำจนจบเองแบบ autonomous**. Salesforce Ben พาดหัวตรง ๆ ว่า "Huge Agentforce Pricing Shift" และ CIO Magazine กับ CX Network ต่างจับประเด็นเดียวกัน — นี่คือครั้งแรกที่ SaaS incumbent ยอมเลิก seat pricing มา sell outcome

Help Agent เป็น **prebuilt agent** ที่ Salesforce configure มาให้แล้ว ต่างจาก Agentforce Builder เดิมที่ต้อง configure workflow เอง — คลิกไม่กี่ทีก็ deploy ได้ครอบ voice / web / portal / messaging พร้อมกัน. Salesforce ย้ำว่า **"deploys in minutes"** และ configuration ทำในหน้าจอเดียว. หลักฐานที่บริษัทเอามาโชว์คือ dogfood ตัวเอง: บน help.salesforce.com Agentforce handle inquiries รวม **4.3 ล้าน ticket** ผ่านมาแล้ว, **resolve autonomous ไป 70%** ที่เหลือ escalate ให้ human. Salesforce บอกว่าทั้ง product นี้ "ทุกอย่างที่เราเรียนรู้จาก 4.3 ล้าน ticket นั้น ถูก encode เข้ามาใน Help Agent"

Pricing $2 flat per resolution เป็น **หมุดหมายทาง economic** — เพราะ Salesforce เอง admit ว่าที่ Agentforce เดิม (launched Oct 2024) มี friction สูงในการ sell: ลูกค้าไม่ยอมจ่าย per-conversation เพราะไม่มีทางประเมิน ROI ล่วงหน้า. Pay-per-resolution แก้ปัญหานี้ตรง ๆ — CIO คำนวณได้ทันที: จากเดิม call center คนหนึ่งจัดการ 20 ticket/วัน ที่ต้นทุน $200 (~$10/ticket), Help Agent ที่ resolve 70% ของ inquiries ต้นทุน $2/resolution = **~5x cheaper** และ predictable

รอบนี้ผูกกับสถาปัตยกรรม Agentforce 360 (launched April 15, 2026 ที่ TrailblazerDX) ที่ SF ลงทุน $15B ใน San Francisco initiative. Help Agent เป็น **first outcome-priced product** ในสายนี้ — analyst ที่ CX Network และ CMSWire คาดว่า Salesforce จะ **roll pay-per-outcome ไปที่ Agentforce Operations และ Agentforce Sales** ในไตรมาสถัดไป

## ทำไมสำคัญ

**Pay-per-resolution ไม่ใช่แค่ pricing tactic — เป็น business model bet ที่กัด Salesforce เองก่อน**. Marc Benioff รู้ดีว่าถ้าลูกค้า Fortune 1000 ที่ปกติซื้อ Service Cloud license 10,000 seat ($150-250/seat/เดือน = ~$18-30M ARR ต่อ account) ย้ายมา Help Agent ที่ pay-per-resolution — ARR จะ **ลดลงตอนต้นก่อน**. แต่ Salesforce กำลังเดิมพันว่า **volume จะโต 5-10x** เพราะ CIO ทดลองได้ง่าย. คนที่ต้าน pricing model นี้ในบอร์ด SF น่าจะเยอะ — ที่ยอม launch ได้แปลว่า data ภายในบอก signal ชัด

จับคู่กับ **Gartner report ที่ออกวันเดียวกัน** ที่ประเมิน $234B ของ enterprise application spend เสี่ยง "agentic arbitrage" ระหว่างนี้ถึง 2030 — เท่ากับ 20% ของ SaaS spend รวม. George Brocklehurst ที่ Gartner บอกตรง ๆ ว่า "agentic systems deliver outcomes directly, bypassing UX-heavy applications and making the software invisible. This breaks the link between user growth and revenue growth." คือ analyst report กับ Salesforce announcement วันเดียวกันไม่บังเอิญ — SF น่าจะได้ preview report และตอบด้วย product ในทันที เพื่อ **frame ตัวเองว่าเป็นวินเนอร์ ไม่ใช่ผู้แพ้**ในการ shift นี้

Pattern ที่ต้องดูต่อ — คนอื่นจะตาม. **Intercom** เริ่ม Fin outcome-priced ตั้งแต่ 2024, **Decagon** ปลายปี 2025, **Sierra** (Bret Taylor) มีอยู่แล้ว. แต่ทั้งหมดคือ startup — Salesforce เป็น **incumbent Fortune 500 SaaS วินเนอร์รายแรก** ที่ยอมเปลี่ยน. ServiceNow, Workday, Adobe, Microsoft (Dynamics) จะทำตามในไตรมาสถัดไป โดยเฉพาะ ServiceNow ที่มี Agentic accelerator กับ Cognizant (จาก 30 มิ.ย.) — ราคาที่จ่ายต่อ workflow completion จะกลายเป็นบทสนทนา CIO ปกติภายในสิ้นปี

Signal ที่ต้อง watch — **base rate ของ 70% autonomous resolution ในสภาพจริงหลัง GA**. ตัวเลข 70% ที่ Salesforce โชว์เป็น **inbound question เกี่ยวกับตัว Salesforce เอง** ซึ่ง prompt training data พร้อมมาก (10 ปีของ Trailhead + Documentation). ในลูกค้าจริงที่ deploy Help Agent บน product ตัวเอง — เช่น bank ที่ answer คำถาม mortgage — base rate อาจจะเริ่มที่ 30-40% ในเดือนแรก. ถ้าลูกค้าคาดหวัง 70% แล้วเจอ 30% + จ่าย $2 ต่อ resolve (แทน per-seat cheap เก่า) ก็ **churn ได้เร็ว** และ Salesforce จะเจอ backlash

## มุม AI Agent Platform

**Builders** — คำถามใหญ่ที่ agent platform ทุกเจ้าจะต้องตอบภายในไตรมาสหน้าคือ **"outcome ของคุณคืออะไร?"**. คำ resolve/deflection/completion ต้องมี definition ที่ CIO ยอมรับ + audit ได้. คำแนะนำ: (1) เขียน **resolution schema** ใน agent config (input = customer query type, success criteria = confirmed resolved by customer / no reopen in 7 days), (2) ทำ dashboard ที่ **แสดง unit cost ต่อ resolution** แบบ realtime, (3) มี tier pricing: charge เต็มใน confident resolution, discount ใน grey area, ไม่คิดเงินเมื่อ escalate. ที่ Sierra กับ Decagon ทำแล้วเป็น template เอามา iterate ต่อได้

**Users / business** — ถ้าคุณเป็น CIO ของ enterprise ที่ประเมิน customer service agent อยู่: Help Agent + $2/resolution ทำให้ **pilot risk เกือบเป็นศูนย์** — ทดลองใน channel เดียว 1 เดือน หมดงบ $10-20K ก็รู้ผลชัด. แต่**ก่อน sign contract ต้องเจรจา 2 ประเด็น**: (1) definition ของ "resolution" — ให้ agree ว่า resolution = customer confirm + no reopen 7 วัน, ไม่ใช่แค่ agent บอกว่าเสร็จ, (2) cap รายเดือน — ระวัง edge case ที่ agent resolve เกินความคาดหวัง (เช่น bug ทำให้เดา "resolved" ซ้ำ) แล้ว bill พุ่ง. สำหรับ Thai enterprise (SCB, KTB, True, AIS) ที่กำลัง evaluate — model นี้ตรงกับ business context ไทยกว่าเก่า เพราะ finance team เคยชินกับ **transactional pricing** (per SMS, per QR verification) มากกว่า SaaS subscription

**Ecosystem** — ตลาด **agent observability + outcome verification** จะโตเร็วมาก. LangSmith, Arize AI, WhyLabs, Braintrust — ปัจจุบัน focus ที่ prompt / trace observability ต้องขยายไปที่ **outcome tracking** (แต่ละ conversation resolve จริงมั้ย, ลูกค้ากลับมา reopen ใน 7 วันมั้ย). วงจร dispute resolution — ถ้าลูกค้า contest ว่า "ไม่ได้ resolve" — ต้องมี evidence chain (recording + trace + verifier LLM) ซึ่งจะกลายเป็น sub-industry ตัวเอง. คนที่ shipping outcome-based agent ต้องมี audit layer นี้ก่อน sign enterprise deal

## Sources
- [Salesforce Launches Agentforce Help Agent That Deploys in Minutes and Only Charges for Resolutions — Salesforce Newsroom](https://www.salesforce.com/news/stories/agentforce-help-agent-announcement/)
- [Huge Agentforce Pricing Shift: Salesforce Introduces Pay-Per-Resolution — Salesforce Ben](https://www.salesforceben.com/huge-agentforce-pricing-shift-salesforce-introduces-pay-per-resolution/)
- [Salesforce unveils AI Help Agent with pay-per-resolution pricing — CIO](https://www.cio.com/article/4189183/salesforce-unveils-ai-help-agent-with-pay-per-resolution-pricing.html)
- [Salesforce launches Help Agent, a prebuilt AI customer-service agent on Agentforce, priced at $2 per autonomously resolved issue — Shopifreaks](https://www.shopifreaks.com/salesforce-launches-help-agent-a-prebuilt-ai-customer-service-agent-on-agentforce-priced-at-2-per-autonomously-resolved-issue/)
- [Salesforce Debuts Help Agent With Pay-Per-Resolution AI — CMSWire](https://www.cmswire.com/contact-center/salesforce-debuts-help-agent-with-payperresolution-ai/)

---

## Audio script

หนึ่งกรกฎาคม Salesforce ประกาศ Agentforce Help Agent ที่จะ GA เดือนนี้ พร้อม pricing model ใหม่ชื่อ pay-per-resolution — คิดสองดอลลาร์ต่อการแก้ปัญหาลูกค้าจนจบเองแบบ autonomous. ลูกค้าขอคุยกับคน หรือเดินจากไปโดยไม่พอใจ ไม่คิดเงิน. นี่คือครั้งแรกที่ SaaS incumbent ระดับ Fortune 500 ยอมทิ้ง per-seat pricing มาขาย outcome.

หลักฐานที่ SF โชว์คือ dogfood ตัวเอง — บน help.salesforce.com Agentforce จัดการ inquiry ไปสี่ล้านสามแสน ticket, resolve autonomous เจ็ดสิบเปอร์เซ็นต์. Prebuilt agent deploy ในไม่กี่นาที ครอบทุก channel voice web portal SMS. CIO คำนวณ ROI ได้ทันที — ต้นทุน call center คนสิบดอลลาร์ต่อ ticket, Help Agent สองดอลลาร์ต่อ resolution, ประหยัดห้าเท่าและ predictable.

Timing ที่น่าสนใจ — Gartner ปล่อยรายงานวันเดียวกันบอกว่าสองแสนสามหมื่นสี่พันล้านของ enterprise SaaS spend เสี่ยง disruption จาก agentic arbitrage ภายในสองพันสามสิบ. George Brocklehurst พูดตรง ๆ ว่า agent ทำ user growth หยุด link กับ revenue growth ของ vendor. คือ Gartner บอกว่า SaaS incumbent จะเสีย SF ตอบทันทีว่า จะเป็นวินเนอร์ ไม่ใช่ผู้แพ้ ของ shift นี้.

สำหรับ agent builder — คำถามใหญ่ที่ต้องตอบไตรมาสหน้า outcome ของคุณคืออะไร. Resolution schema ต้องมี definition ที่ CIO audit ได้, dashboard ต้องแสดง unit cost ต่อ resolution แบบ realtime. สำหรับ enterprise ไทยที่กำลัง pilot — model นี้ตรงกับ business context ไทยกว่า SaaS เก่า เพราะ finance team เคยชินกับ transactional pricing แต่ก่อนเซ็นสัญญา เจรจา definition ของ resolution ให้ชัด — customer confirm plus no reopen ในเจ็ดวัน ไม่ใช่แค่ agent บอกว่าเสร็จ. Cap รายเดือนต้องมี กันเคส agent เพี้ยนแล้ว bill พุ่ง.
