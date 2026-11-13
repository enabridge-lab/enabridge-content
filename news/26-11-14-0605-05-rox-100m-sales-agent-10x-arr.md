---
date: 2026-11-14
slug: rox-100m-sales-agent-10x-arr
topic: agentic-ai
reading_time_min: 3
sources: 4
image_prompt: |
  An editorial isometric illustration of a sales floor with empty cubicles
  being replaced by glowing agent silhouettes at every desk. In the middle
  rises a huge revenue chart with a steep "10x ARR" arrow shooting up.
  Three stacked number cards float above: "$100M SERIES B", "$1.3B VALUATION",
  "DATABRICKS VENTURES". Small desk tags read "LEADS", "MEETINGS", "DEALS",
  "EXPANSION". A faded Salesforce cloud icon sits in the far corner with a
  dashed line connecting to the agent swarm, labeled "REPLACED". Editorial
  style, electric blue and soft green palette, high contrast so numbers stay
  readable at 200px, 1:1 aspect, no real human faces (silhouettes OK).
image: images/26-11-14-0605-05-rox-100m-sales-agent-10x-arr.png
---

# Rox ปิด $100M @ $1.3B — sales agent unicorn รุ่นใหม่ ARR โต 10 เท่าในปีเดียว

## TL;DR
- 11 พฤศจิกายน Rox ปิด Series B $100M ที่ valuation $1.3B นำโดย General Catalyst + March Capital
- ลูกค้าใหม่: Databricks Ventures, Prosperity7 Ventures เข้าใหม่; Sequoia, Factory, GV เติมเพิ่ม
- ARR โต 10 เท่าใน year 1 (คาด $8M EOY 2025) — ยัง single-digit millions แต่ growth curve ทำให้ VC ยอม 150x revenue multiple

## เกิดอะไรขึ้น
วันที่ 11 พฤศจิกายน Rox ซึ่งเป็น AI agent สำหรับ sales rep ปิด Series B มูลค่า $100 ล้านที่ valuation $1.3B นำโดย General Catalyst และ March Capital โดยมี Databricks Ventures กับ Prosperity7 Ventures (Saudi Aramco corporate VC) เข้าเป็นนักลงทุนใหม่ Sequoia Capital, Factory HQ, และ GV ที่ลงรอบ seed/Series A ไว้ลงเพิ่ม เทียบรอบก่อน — Series A เมื่อพฤศจิกายน 2024 นำโดย General Catalyst — total funding ก่อนหน้านี้ประมาณ $50M

ตัวเลขที่ Rox เปิดเผยพร้อมรอบนี้ — ARR โตมากกว่า 10 เท่าใน year แรกที่ออก market ตัวเลข Dealroom อ้างอิงข่าวก่อนหน้าบอกว่า Rox คาดจะปิด 2025 ด้วย ARR ประมาณ $8M ถ้าเทียบ valuation $1.3B = ประมาณ 160x ARR multiple ซึ่งแปลว่า investor ลงจาก growth curve + market TAM ไม่ใช่ current revenue — standard สำหรับ agent category ตอนนี้

Product ของ Rox ตั้งเป้าไปที่ sales rep workflow ทั้ง stack — generate leads, book meetings, update deal stage, expand existing account โดยทำงานใน system ที่ลูกค้าใช้อยู่แล้ว (Salesforce, HubSpot, LinkedIn Sales Navigator, Gmail/Outlook) ไม่ใช่ standalone UI ของตัวเอง pitch หลักคือ "replace sales ops overhead แทนที่จะ add workflow" — เป็น framing ที่ CFO ของบริษัท enterprise ซื้อง่าย

การที่ Databricks Ventures ลงรอบนี้มี implication เพิ่มเติม — Databricks กำลัง push Mosaic AI Agent Framework เป็น platform ให้ลูกค้า build agent ของตัวเอง การ invest ใน Rox คือ signal ว่า Databricks เห็นประโยชน์จาก vertical application layer ที่ consume platform ของตัวเอง ไม่ pure horizontal play

## ทำไมสำคัญ
Rox อยู่ในคลื่น "AI รุก seat ของ sales rep" ที่สัปดาห์ก่อนมี Nooks ที่ได้ $500M non-dilutive มา และเดือนก่อน Clay, Regie.ai, 11x.ai ออกตัวเลข traction สัญญาณร่วมของกลุ่มนี้คือ — sales ops function กำลังถูกตีแผ่ และ seat ของ BDR/SDR/junior AE (ที่ค่าใช้จ่ายรวม benefit + tech stack $100K-$150K/คน/ปี) กลายเป็น prime target ของ agent replacement

เทียบ Rox vs Salesforce Agentforce — Agentforce เป็น "in-app assistant" ที่ embed ใน Salesforce UI คนใช้คือ sales rep ที่เปิด Salesforce อยู่แล้ว ส่วน Rox เป็น "autonomous worker" ที่รันเองตลอด quarter ใน background โดยไม่ต้องมี human ที่หน้าจอ ทั้งสองประเภทอาจ coexist ได้ แต่ model business ต่างกัน — Agentforce = feature upsell, Rox = headcount replacement

Caveat ใหญ่ — "ARR โต 10x" จาก base ไม่ชัด (10x จาก $0 ไป $8M ก็เป็น 10x), ตัวเลข ARR ยัง single-digit millions ซึ่งเล็กมากเทียบ valuation และ sales agent category มีคู่แข่งแน่น (Nooks, 11x, Clay, Regie, Outreach) — ไม่มีใครมี moat ชัดเจน การลงรอบนี้จึงเป็น "bet on category size + Rox team execution" ไม่ใช่ "bet on current traction"

## มุม AI Agent Platform
Builders — ถ้าตั้งใจ build agent ที่ replace headcount ไม่ใช่ augment ให้ focus ที่ system ของลูกค้า (CRM, email, calendar) ไม่ใช่ UI ของตัวเอง เพราะ user ที่คุณกำลังแทนที่ไม่ได้ open "agent app" ทุกวัน — workflow ของเขาอยู่ใน Salesforce + Outlook การ embed แบบ invisible คือ success criterion สำคัญกว่า chat UX สวย ๆ นอกจากนั้น pricing model ที่ CFO ซื้อง่ายคือ "ต่อ seat ที่ replace" หรือ "ต่อ outcome ที่ create" ไม่ใช่ per-seat ของพนักงานปัจจุบัน

Users/business — enterprise ที่กำลัง scale sales team ปี 2027 ควรเปิด conversation ว่า — ถ้า agent สามารถทำ pipeline generation + meeting booking + deal expansion แทน BDR ได้ 70-80% ของ workload headcount ที่ plan ไว้ปีหน้าควรเป็นเท่าไหร่ ลูกค้าไทยกลุ่ม B2B software, enterprise service, industrial equipment ที่ Enabridge ดูแลควร benchmark cost per meeting booked กับ Rox-style vendor ก่อน hire batch ถัดไป — ถ้า per-meeting cost ของ agent < $50 เทียบ BDR ปัจจุบันที่ประมาณ $150-$300/meeting การ delay hiring แล้ว pilot agent คุ้มกว่า

Ecosystem — Salesforce อยู่ในตำแหน่งที่ยากที่สุด — เป็นทั้ง distribution channel ให้ Rox (Rox รันบน Salesforce data) และเป็นคู่แข่งโดยตรงผ่าน Agentforce ประวัติศาสตร์ทำนายว่า Salesforce จะใช้ API change, pricing change, หรือ platform policy เป็น friction ให้ Rox-like startup ภายใน 12-18 เดือนข้างหน้า — รอดู ว่า Rox จะ hedge ด้วยการ port ไป HubSpot + CRM ทางเลือกอื่นเร็วแค่ไหน

## Sources
- [Rox Raises $100M at $1.3B Valuation to Take On Salesforce (FourWeekMBA)](https://fourweekmba.com/ai-rox-raises-100m-at-1-3b-valuation-to-take-on-salesforce/)
- [Rox Reaches $1.2B Valuation in New General Catalyst Funding Round (Shopifreaks)](https://www.shopifreaks.com/rox-reaches-1-2b-valuation-in-new-general-catalyst-funding-round/)
- [Sales automation startup Rox AI hits $1.2B valuation (Yahoo Finance / Reuters)](https://finance.yahoo.com/news/sales-automation-startup-rox-ai-222550353.html)
- [Rox hits $1.2B valuation and $8M ARR with new round (Dealroom)](https://dealroom.co/news/126775-ai-sales-startup-rox-hits-1-2b-valuation-and-8m-arr-with-new-round/)

---

## Audio script
วันที่ 11 พฤศจิกายน Rox ซึ่งเป็น AI agent สำหรับ sales rep ปิด Series B มูลค่า 100 ล้านเหรียญที่ valuation 1.3 พันล้านเหรียญ นำโดย General Catalyst และ March Capital Databricks Ventures กับ Prosperity7 Ventures เข้าเป็นนักลงทุนใหม่ Sequoia, Factory และ GV ที่ลงรอบ seed กับ Series A ไว้ลงเพิ่ม ตัวเลขที่ Rox เปิดเผยพร้อมรอบนี้คือ ARR โตมากกว่า 10 เท่าใน year แรกที่ออก market ถ้าดูข่าวก่อนหน้า Rox คาดจะปิด 2025 ที่ ARR ประมาณ 8 ล้านเหรียญ แปลว่า valuation 1.3 พันล้านเหรียญเท่ากับ 160 เท่าของ ARR ซึ่ง investor ลงจาก growth curve ไม่ใช่ current revenue Product ของ Rox ทำงานใน Salesforce, HubSpot, LinkedIn Sales Navigator และ Gmail Outlook ที่ลูกค้าใช้อยู่แล้ว ไม่ใช่ standalone UI pitch คือ replace sales ops overhead แทนที่จะ add workflow ซึ่งเป็น framing ที่ CFO ของบริษัท enterprise ซื้อง่าย Rox อยู่ในคลื่น AI รุก seat ของ sales rep ที่สัปดาห์ก่อนมี Nooks ได้ 500 ล้านแบบ non-dilutive และก่อนหน้านี้มี Clay 11x Regie.ai ออกตัวเลข traction สัญญาณร่วมคือ sales ops function กำลังถูกตีแผ่ และ seat ของ BDR SDR junior AE ที่ค่าใช้จ่าย 100,000 ถึง 150,000 เหรียญต่อคนต่อปี กลายเป็น prime target ของ agent replacement สำหรับ enterprise ที่กำลัง scale sales team ปี 2027 ควรถามว่า ถ้า agent ทำ pipeline generation meeting booking และ deal expansion แทน BDR ได้ 70 ถึง 80 เปอร์เซ็นต์ของ workload headcount ที่ plan ไว้ปีหน้าควรเป็นเท่าไหร่
