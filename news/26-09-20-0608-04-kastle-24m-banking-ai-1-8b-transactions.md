---
date: 2026-09-17
slug: kastle-24m-banking-ai-1-8b-transactions
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  A stylized editorial isometric of a US bank branch during working hours.
  Behind the teller counter stand three glowing orange orbs labeled
  "KASTLE AI WORKFORCE"; each holds a stack of mortgage files. On the wall,
  huge neon dashboard numbers read "$1.8B PROCESSED", "6 LENDER LOGOS",
  "$24M SERIES A", "INSIGHT PARTNERS LED". A silhouetted human loan
  officer at a desk reviews a summary the orb prepared. Deep navy and
  banker-green palette with amber highlights on the dashboard.
  Editorial isometric style, 1:1 aspect, no real human faces.
image: images/26-09-20-0608-04-kastle-24m-banking-ai-1-8b-transactions.png
---

# Kastle ปิด Series A $24M — AI agent ประมวลผลไปแล้ว $1.8B ในธุรกิจ consumer lending, ลูกค้าคือ Newrez / Valley Bank / Carrington

## TL;DR
- 17 ก.ย. Kastle (San Francisco, ก่อตั้ง 2024) ปิด **Series A $24M** นำโดย **Insight Partners**; Y Combinator + Commerce Ventures + Fifth Wall ร่วม
- **AI agent ประมวลผลไปแล้ว $1.8B ในธุรกรรม** — ข้ามระบบ core banking เดิม, จัดการ high-volume workflow (originations, document processing, servicing)
- Customer disclosed: **Newrez, Valley Bank, Carrington Mortgage Services, New American Funding, Planet Home, Selene Finance** — 6 ชื่อในสาย mortgage/consumer lending

## เกิดอะไรขึ้น

Kastle ก่อตั้งปี 2024 โดยทีมที่มาจาก banking + AI backend, target ตลาด **consumer lending** ที่ยังใช้ core system อายุ 20-30 ปี (FIS, Jack Henry, Fiserv) — bottleneck คือ workflow ระหว่างระบบ ไม่ใช่ core ตัวเอง. Kastle **ไม่ replace core** แต่ deploy agent ให้ทำงานข้ามระบบ — pull data จาก Encompass, cross-check FICO, sign document ผ่าน DocuSign, update servicing platform โดยไม่ต้อง IT project reintegration

17 ก.ย. Kastle ปิด Series A **$24M** — **Insight Partners นำ**, existing investor **Y Combinator + Commerce Ventures** ร่วม, **Fifth Wall** (proptech-focused VC) + กลุ่ม founder/exec จาก financial services เข้าใหม่. Insight นำ = signal ว่า Kastle อยู่ในเส้นทาง scale-up class ไม่ใช่ pure seed play

Metric ที่ Kastle disclosed **มีน้ำหนักที่สุด**: agent ประมวลผลไปแล้ว **$1.8B ใน transaction** — เทียบสัปดาห์ก่อนที่ Wonderful ($550M Series C) ยัง "not disclose named customer / ARR" = Kastle มี proof of production ที่ enterprise buyer sniff test ผ่าน. **Customer list ที่ระบุ**: Newrez, Valley Bank, Carrington Mortgage Services, New American Funding, Planet Home Lending, Selene Finance — mid-market และ regional mortgage lender ที่มี volume จริงหลัก $10-50B annual origination ต่อราย

Kastle บอกว่าเงินก้อนนี้ใช้ **ขยายจาก mortgage → auto lending → SBA + student loan** — เดินตาม vertical ใน consumer lending ที่มี regulatory-heavy workflow แบบเดียวกัน

## ทำไมสำคัญ

Enterprise agent story ในตลาด 2026 มีสองประเภทที่ contrast กันชัด: (1) **"AI OS" story** — Wonderful ($550M @ $5B, Series C ผ่านมา) ที่ระดม valuation ก่อน named customer; (2) **"vertical workflow" story** — Kastle ($24M Series A) ที่มี $1.8B tx processed + 6 named lender ก่อนไปจับเงินก้อนใหญ่. **VC เริ่มแยกซื้อ**: Insight ทำทั้งสอง deal แต่ pricing ต่างกัน 10-20x ต่อ ARR

**Consumer lending คือ market ที่ agent มี unfair advantage ชัด**: workflow complex, document-heavy, regulator-audited, ROI คำนวณเป็น "hours saved per loan × loan volume" ตรง. Kastle claim การ **ประมวลผล $1.8B** = ~10,000-15,000 loan (ที่ average $150K-180K per US mortgage) = จำนวน pilot ที่ regulator scrutiny ผ่านแล้ว. เทียบ Salesforce Agentforce ที่ตัวเลข "hours saved" มักเป็น aggregate ไม่ได้ผูกกับ dollar volume — Kastle metric แข็งกว่าเพราะ **loan servicing = money movement ที่ audit ได้**

Pattern ที่เห็น: **agent สาย vertical (mortgage, insurance claim, medical claim, tax prep) กำลัง out-execute agent สาย horizontal**. เพราะ vertical มี regulatory moat + workflow specificity + customer paying willingness สูง. Enabridge bet: ปี 2027 startup vertical agent จำนวน 5-10 ราย จะแตะ $100M ARR ก่อน horizontal orchestration ที่ยัง scaling burn

## มุม AI Agent Platform

สำหรับ **builders**: ถ้า target enterprise B2B — **เลือก vertical ก่อน horizontal**. Kastle เป็น proof ว่า Insight + YC ยอมจ่ายเมื่อเห็น named customer + dollar volume; startup ไทยที่ทำ agent-based invoice processing, KYC, SME lending, claim adjudication ควรวางแผน pilot กับ 2-3 named customer + track hard $ metric (ไม่ใช่แค่ "hours saved") ก่อนไปจับ Series A. Playbook: **land 1 mid-market player → wedge ที่ workflow เดียว → expand adjacent workflow ในลูกค้าเดิม → ค่อยหา second logo**

สำหรับ **users / business**: bank / insurer / lender ไทย (SCB / KBank / KTB / ttb / ไทยพาณิชย์ประกันชีวิต / เมืองไทย / กสิกรไทยประกัน) ที่ evaluate agent platform อยู่ — Kastle case ให้ pattern ที่ replicate ได้: **จับ workflow ระหว่าง core system ที่ IT ยังไม่แตะ** เป็น first deploy; วัดผลด้วย dollar volume + cycle-time reduction ที่ regulator ยอมรับ (ไม่ใช่แค่ user CSAT). US lender ยอมเปิด API + document access ให้ agent เพราะแรงกดดัน operational cost ต่อ loan ($8K-11K per US mortgage origination) — ไทยยัง cost ต่ำกว่า, แต่ผ่าน 5 ปีจะขึ้นเรื่อยเมื่อ compliance เพิ่ม

สำหรับ **ecosystem**: **มีตลาด vertical banking agent ที่ยังโล่ง** ในภูมิภาค — Kastle จับ US mortgage, ยังไม่มีเจ้า SEA equivalent. Startup ไทย + สิงคโปร์ + อินโดฯ ที่ตั้งใจทำ vertical agent สำหรับ SEA lender = window เปิด 12-18 เดือน (ก่อน Kastle ขยาย international หรือมี regional competitor). Salesforce, ServiceNow, UiPath ที่ push agent horizontal = โดน bypass ในสายนี้เพราะ vertical player รู้ workflow ลึกกว่า

## Sources
- [Kastle Raises $24M Series A Led by Insight Partners to Build the AI Workforce for Banking Operations — PR Newswire](https://www.prnewswire.com/news-releases/kastle-raises-24m-series-a-led-by-insight-partners-to-build-the-ai-workforce-for-banking-operations-302881290.html)
- [Kastle raises $24M to build an AI workforce for consumer lending — Dealroom](https://dealroom.co/news/151625-kastle-raises-24m-to-build-an-ai-workforce-for-consumer-lending/)
- [Kastle raises $24 million Series A for banking AI — American Bazaar](https://americanbazaaronline.com/2026/09/17/kastle-24-million-series-a-ai-banking-workforce-488358/)
- [Kastle Raises $24.0M Series A for AI Lending Platform — SignalBase](https://www.trysignalbase.com/news/funding/kastle-raises-24m-series-a-for-ai-lending-platform)

---

## Audio script
Kastle ตั้งอยู่ที่ San Francisco ก่อตั้งปี 2024 ปิด Series A ยี่สิบสี่ล้านดอลลาร์เมื่อ 17 กันยา นำโดย Insight Partners. Y Combinator กับ Commerce Ventures ที่เป็น existing investor ร่วม; Fifth Wall ซึ่งเป็น proptech VC กับกลุ่ม founder และ exec ในสาย financial services เข้าใหม่. Kastle target ตลาด consumer lending ที่ core system เก่ายี่สิบสามสิบปีอย่าง FIS, Jack Henry, Fiserv — bottleneck คือ workflow ระหว่างระบบ ไม่ใช่ core ตัวเอง. Kastle ไม่ replace core แต่ deploy AI agent ให้ pull data จาก Encompass, cross-check FICO, sign document ผ่าน DocuSign, update servicing platform ข้ามระบบเดิม. Metric ที่ตกใจคือ agent ประมวลผลไปแล้ว 1.8 พันล้านดอลลาร์ในธุรกรรม — เทียบสัปดาห์ก่อนที่ Wonderful ปิด 550 ล้านที่ 5 พันล้าน valuation แต่ไม่มี named customer disclosed = Kastle มี proof of production ที่ enterprise buyer sniff test ผ่าน. Customer list เปิดชื่อ Newrez, Valley Bank, Carrington Mortgage Services, New American Funding, Planet Home Lending, Selene Finance — mid-market และ regional mortgage lender ที่ volume $10-50 พันล้านต่อปีต่อราย. เงินก้อนใหม่ใช้ขยายจาก mortgage ไป auto lending, SBA, student loan. Enabridge bet คือปีหน้า startup vertical agent 5-10 ราย จะแตะ 100 ล้าน ARR ก่อน horizontal orchestration. Bank ไทยที่ evaluate agent platform ควรจับ workflow ระหว่าง core ที่ IT ยังไม่แตะเป็น first deploy วัดด้วย dollar volume + cycle time — window sea market ยังเปิด 12-18 เดือนก่อน Kastle ขยายมาเอง.
