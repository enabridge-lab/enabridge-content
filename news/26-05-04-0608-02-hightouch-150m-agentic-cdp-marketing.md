---
date: 2026-05-04
slug: hightouch-150m-agentic-cdp-marketing
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: Editorial illustration of a glowing data lake feeding into a constellation of orchestrated marketing channels, with autonomous robotic conductors directing email pulses, SMS waves, and push-notification ribbons across a city grid at dusk, minimal flat geometric shapes, muted teal and coral palette, dramatic backlight, no text no logos no faces
image: images/26-05-04-0608-02-hightouch-150m-agentic-cdp-marketing.png
---

# Hightouch ระดม $150M ที่ valuation $2.75B — แปลง CDP เดิมเป็น "agentic marketing OS" ให้ Domino's, PetSmart, DraftKings

## TL;DR
- 27 เม.ย. — Hightouch (Composable CDP จาก SF) ปิด Series D $150M led by Goldman Sachs Growth Equity + Bain Capital Ventures ที่ valuation $2.75B พร้อมการสนับสนุนจาก Iconiq, Sapphire, Amplify, Y Combinator และ TD7 (VC arm ของ The Trade Desk)
- ตัวเลขที่หนักจริง: revenue โต **มากกว่า 100% สองปีติด**, customer flagship อย่าง PetSmart ส่ง email personalized **4 พันล้านฉบับ/ปี** ผ่าน platform ขับเคลื่อนยอดขาย double-digit; loyalty conversion เพิ่ม 25%; engagement rate +150%
- core product "AI Decisioning" ใช้ agent autonomous เลือก channel/timing/content ต่อ customer แต่ละคนแบบ real-time — pivot จาก reverse-ETL data tool เดิมเป็น **agentic marketing OS** ที่ stack ทับ data warehouse ของลูกค้า ไม่แทนที่

## เกิดอะไรขึ้น

วันที่ 27 เมษายน Kashish Gupta CEO ของ Hightouch ประกาศปิด Series D ขนาด $150 ล้านที่ post-money valuation $2.75 พันล้าน — เกือบ 3x จาก Series C ที่ $1.2B เมื่อปลายปี 2024 รอบนี้ Goldman Sachs Growth Equity และ Bain Capital Ventures นำร่วม โดยมี Iconiq Capital, Sapphire Ventures, Amplify Partners, Y Combinator และ **TD7** — venture arm ของ The Trade Desk — ตามมา การมี TD7 เข้ามาน่าสนใจเป็นพิเศษเพราะ The Trade Desk เป็นยักษ์ ad-tech ที่กำลังหา positioning ใน era post-cookie ที่ first-party data + agentic targeting จะกลายเป็น moat หลัก

Hightouch เกิดจาก Y Combinator batch S19 ในฐานะ "reverse-ETL" tool — ตัวพิมพ์ data จาก data warehouse (Snowflake, Databricks, BigQuery) ไปยัง downstream system อย่าง Salesforce, HubSpot, Marketo แบบ real-time — concept ที่หลังจากนั้นกลายเป็น standard ของวงการ data engineering แต่ในปี 2024 Gupta pivot สำคัญ: launch **AI Decisioning** ที่ใช้ agent autonomous ตัดสินใจว่า customer แต่ละคนควรได้รับ message อะไร ผ่าน channel ไหน ที่เวลาใด — แทนที่ marketer จะต้องนั่ง config rule ใน journey builder รายตัว

ตัวเลข deployment ของ Hightouch ตอนนี้แสดงให้เห็นว่า pivot เวิร์ก PetSmart ใช้ Hightouch + Databricks ส่ง email personalized **4 พันล้านฉบับต่อปี** ผ่าน Salesforce Marketing Cloud — ตัวเลขที่ทำให้ Hightouch กลายเป็น orchestration layer ที่ใหญ่ที่สุดบน Salesforce ecosystem โดย PetSmart รายงาน **double-digit sales growth, customer engagement +150%, loyalty conversion +25%** Domino's, DraftKings, Ramp, Whoop ก็เป็น customer หลัก — รวมแล้ว annual recurring revenue โตเกิน 100% สองปีติดกัน ตัวเลข Gupta บอก TechCrunch ว่า "ARR run-rate ของเรา approaching $200M" แม้ตัวเลขนี้ยังไม่เปิด confirmed

จุด engineering ที่น่าสนใจคือ **Hightouch ไม่ migrate data ของลูกค้าเข้า platform ตัวเอง** — ทุกอย่างยังอยู่ใน data warehouse เดิม Hightouch แค่เป็น compute + decisioning layer ที่ vibe กับ Snowflake/Databricks/BigQuery โดย agent จะ query data ใน warehouse แบบ federated เพื่อตัดสินใจ และ trigger action ผ่าน connector ไปยัง downstream marketing tool — pattern ที่ Goldman Sachs analyst note ระบุว่าเป็น "anti-Salesforce architecture" — แทนที่จะ lock-in customer ใน proprietary CDP, Hightouch แต่งให้ data warehouse ของลูกค้าเป็น CDP

Gupta ให้สัมภาษณ์ Bloomberg ว่า funding รอบนี้จะใช้สามอย่าง: (1) ขยาย AI Decisioning ให้ครอบคลุม push notification, in-app message, voice channel (เพิ่งมี integration กับ Twilio Flex) (2) build "Agent Studio" — interface ให้ marketer ออกแบบ agent custom ของตัวเอง โดยไม่ต้องเขียน code (3) expand ทีม enterprise sales ใน EMEA และ APAC โดย headcount จะ double จาก 380 เป็น ~700 ภายในสิ้นปี

## ทำไมสำคัญ

Hightouch เป็น case study ที่สมบูรณ์แบบของ pattern ที่ Stratechery เรียก **"agentic verticalization"** — บริษัท horizontal SaaS ที่เคยขาย data infra plain ๆ พบว่าจุดที่ value สูงสุดอยู่ที่ **decisioning layer** ที่อยู่บน data infra ไม่ใช่ตัว infra เอง การ pivot จาก reverse-ETL ($) ไป agentic marketing decisioning ($$$$) ทำให้ pricing สามารถเก็บแบบ outcome-based แทน seat-based — Goldman Sachs note ระบุว่า contract Hightouch ใหม่ ๆ มี ACV เฉลี่ย "5–10x" ของ contract เดิม

เทียบกับ player อื่น Hightouch กำลังตีตลาด CDP เดิมจากด้านบน — Salesforce Data Cloud, Adobe Real-Time CDP, Twilio Segment ทั้งหมดยึด architecture แบบ "store data in our cloud" แต่ Hightouch + Databricks-as-CDP คือ pitch ที่ enterprise CDO ฟังแล้วถูกใจ: ไม่ต้อง migrate data, ไม่ต้องทำ ETL job ใหม่, ไม่มี data residency issue — แค่เปิด query access ให้ Hightouch agent ก็ได้ AI Decisioning ทันที pattern นี้คือเหตุผลว่าทำไม **Composable CDP** ขนาดตลาดถูก IDC revise upward จาก $4B เป็น $8B ภายในปี 2027

อีกจุดที่น่าจับตา: TD7 ลงในรอบนี้น่าจะ signal ว่า The Trade Desk วางแผนใช้ Hightouch เป็น ingestion layer ของ first-party signal จากแบรนด์ — เป็นทางที่ ad-tech แท้ ๆ จะรอด post-cookie โดย first-party data orchestration กลายเป็น new oil ของ industry และ Hightouch ก็พร้อมจะ position ตัวเองเป็น default

## มุม OpenBridge

OpenBridge ในฐานะ B2B integration platform ควรอ่าน Hightouch แบบ **mirror** — เราต้องตอบให้ได้ว่าเราเป็น "reverse-ETL ของ workflow" ที่ขายเป็น utility หรือเราเป็น "agentic decisioning OS" ที่ขายเป็น outcome และเราจะ migrate pricing จากแบบ usage-based ไปเป็น outcome-based ได้อย่างไร เพราะ Hightouch ที่ pivot สำเร็จได้ ACV เพิ่ม 5–10 เท่า — ส่วนเราถ้า stuck อยู่ที่ utility pricing จะไม่มีทางได้ valuation $2.75B แม้จะมี customer 10x

จุด tactical ที่ apply ได้ทันที: (1) ดู AI Decisioning ของ Hightouch แล้วถามตัวเองว่า OpenBridge มี "decisioning layer" บน workflow definition หรือยัง — agent ที่ตัดสินใจว่าลูกค้าใหม่นี้ควร trigger workflow แบบไหน, channel ไหน, timing ไหน (2) **"data ลูกค้าอยู่ที่ไหน เราไปหา ไม่ migrate มา"** เป็น pattern architecture ที่ Hightouch สำเร็จด้วย — ถ้า OpenBridge ยัง require migrate data เข้า platform ก่อนถึงทำงานได้ pivot ตอนนี้ก่อนที่ enterprise procurement จะ block (3) คิดถึง **"Agent Studio" สำหรับ business user** — interface ให้ ops/marketing สร้าง agent ของตัวเองได้โดยไม่ต้องผ่าน engineering — เพราะนี่คือจุดที่ Hightouch จะปิดดีล expansion ได้เร็วและจะกลายเป็นมาตรฐานของวงการเร็ว ๆ นี้

## Sources
- [Hightouch Raises $150 Million to Reinvent How Marketing Works Using AI](https://www.businesswire.com/news/home/20260427054567/en/Hightouch-Raises-$150-Million-to-Reinvent-How-Marketing-Works-Using-AI)
- [Hightouch Valued at $2.75 Billion as AI Agents Transform Enterprise Marketing](https://www.pymnts.com/news/investment-tracker/2026/hightouch-valued-at-2-75-billion-as-ai-agents-transform-enterprise-marketing/)
- [Raising $150M to build the AI platform for marketers](https://hightouch.com/blog/hightouch-funding-series-d)
- [Hightouch Raises $150M Series D for Agentic CDP](https://www.tamradar.com/funding-rounds/hightouch-series-d-150m)

---

## Audio script
ข่าวที่สอง — Hightouch บริษัท CDP จาก San Francisco ปิด Series D ที่ร้อยห้าสิบล้านดอลลาร์ ที่ valuation สองพันเจ็ดร้อยห้าสิบล้าน นำโดย Goldman Sachs Growth Equity และ Bain Capital Ventures มี TD7 ซึ่งเป็น VC arm ของ The Trade Desk ตามเข้ามาด้วย — สัญญาณว่า ad-tech กำลังหา positioning ใน era post-cookie

Hightouch เริ่มจาก Y Combinator ในฐานะ reverse-ETL tool — เครื่องมือที่ส่งข้อมูลจาก data warehouse ออกไป Salesforce, HubSpot — แต่ในปี 2024 pivot สำคัญด้วยการ launch AI Decisioning agent ที่ตัดสินใจอัตโนมัติว่า customer แต่ละคนควรได้รับ message อะไร ผ่าน channel ไหน ที่เวลาใด — แทนที่ marketer จะนั่ง config rule รายตัว

ตัวเลขโตจริงนะ — PetSmart ใช้ Hightouch ส่ง email personalized สี่พันล้านฉบับต่อปี ดันยอดขาย double-digit, engagement เพิ่มร้อยห้าสิบเปอร์เซ็นต์ Domino's, DraftKings, Ramp, Whoop ก็เป็นลูกค้าหลัก revenue โตมากกว่าร้อยเปอร์เซ็นต์สองปีติด ARR ใกล้สองร้อยล้าน

Pattern สำคัญที่ apply กับ OpenBridge ได้: data ของลูกค้าอยู่ที่ไหน เราไปหา ไม่ migrate มา — Hightouch ไม่เคย store data ของลูกค้าเลย ทุกอย่างยัง federated อยู่บน Snowflake, Databricks ของเขา Hightouch แค่เป็น compute + decisioning layer ทับลงไป pattern นี้ enterprise CDO ชอบมาก เพราะไม่มี data residency issue ไม่ต้องทำ ETL ใหม่

OpenBridge ควรคิดเรื่องเดียวกัน — เรามี decisioning layer บน workflow ของเราหรือยัง agent ที่บอกได้ว่าลูกค้าใหม่นี้ควร trigger workflow แบบไหน — เพราะถ้ายัง stuck อยู่ที่ utility pricing แบบ reverse-ETL valuation 2.75 พันล้านแบบ Hightouch จะไม่มีทางได้
