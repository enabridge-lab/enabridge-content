---
date: 2026-10-07
slug: 26-10-10-0615-04-stuut-order-to-cash-agent
topic: use-case
reading_time_min: 3
sources: 4
image_prompt: |
  Editorial hero: a dollar bill traveling along a conveyor belt through
  five labeled stations — "COLLECTIONS", "CASH APPLICATION", "PAYMENTS",
  "DISPUTES", "DEDUCTIONS" — with mechanical agent arms stamping each.
  At the end, a glowing counter reads "$3B PROCESSED, 150 ENTERPRISES".
  A banner overhead reads "DSO DOWN 47%, 81% NO-HUMAN COLLECTIONS".
  Editorial isometric style, Stuut navy + treasury green + warm steel,
  1:1 aspect, no real human faces.
image: images/26-10-10-0615-04-stuut-order-to-cash-agent.png
---

# Stuut ปิด $52.5M จาก Insight + a16z + M12 — agent วิ่ง order-to-cash ครบ 5 สเตจ, DSO ลด 47%

## TL;DR
- 7 ต.ค. 2026 **Stuut** (New York, agent สำหรับ **order-to-cash**) ปิด Series B **$52.5M** — Insight Partners นำ, a16z + Microsoft M12 ร่วม → funding รวม **$93M** หลังปิด Series A 10 เดือนก่อน
- Agent รัน **5 สเตจ** ของ receivables: collections / cash application / payments / disputes / deductions — ไม่ใช่ copilot ที่ช่วยคน แต่เป็น **autonomous operator** ที่รันครบลูป
- ตัวเลข deployment จริง (บริษัทรายงาน): **150+ enterprises**, **$3B+ processed**, จับคู่ payment 95%+ อัตโนมัติ, **collections 81% ไม่ต้องใช้คน**, ลด DSO **47%** — เป็น case study ที่ CFO ขอเห็นก่อนเซ็น

## เกิดอะไรขึ้น

วันพุธ Stuut — startup นิวยอร์กที่สร้าง agent สำหรับ **order-to-cash (O2C)** ครบ pipeline — ปิด Series B **$52.5M**. Insight Partners นำ round, Andreessen Horowitz และ Microsoft M12 ร่วม. Round นี้มา **10 เดือนหลัง Series A** → funding รวม $93M (growth rate แบบที่ CFO ลงนามเช็ค)

สิ่งที่ Stuut ทำแตกต่างจาก copilot ปกติคือ scope. ไม่ใช่ "ช่วย AR team ร่าง email ทวงหนี้" (เป็น output ของยุค 2023); scope ของ Stuut agent ครอบทั้ง **lifecycle receivables**: (1) collections (ติดตามหนี้), (2) cash application (จับคู่เงินโอนเข้ากับ invoice), (3) payments (รับและ confirm), (4) disputes (รับเรื่องและ route), (5) deductions (ยืนยัน credit note / refund). ลูกค้า integrate ERP → agent รันเองในลูป → report ขึ้น dashboard

ตัวเลขที่ Stuut ประกาศ (self-reported, ยังไม่ independent audit): **150+ enterprises** รวม Verifone, Bishop Lifting Products, ZoomInfo; รวม **payment >$3B** ประมวลผ่าน platform; จับคู่ payment ต่อ invoice **>95% อัตโนมัติ** (เลขที่ CFO เรียก "touchless cash app"); **>81% ของ collection cycle รันโดยไม่มีคน**; ลด **DSO (Days Sales Outstanding) ลง 47%** — เลขที่ถ้าจริงมี impact ตรง working capital และ cost of capital ของบริษัท

Insight นำ round นี้สะคัญ. Insight เป็น growth-stage VC ที่ลงใน vertical SaaS มานานกับ margin disciplined; การเลือก Stuut สะท้อนว่า **vertical AI agent** กำลัง emerge เป็น category ที่ Insight เชื่อว่าแยกจาก horizontal copilot market. a16z + M12 (Microsoft) ที่ร่วม — ชัดว่า hyperscaler-adjacent fund เริ่มลง agent product ที่ "ไม่ชน Agent 365 ของ Microsoft" แต่ complement กัน

Market context: Stuut อ้างว่าตลาด unpaid B2B invoices อยู่ที่ **~$16 trillion** ทั่วโลก — ตัวเลขที่ Insight และ a16z คงใช้ pitch LP ว่า TAM ของ receivables agent ใหญ่กว่าที่หลายคนประเมิน

## ทำไมสำคัญ

Stuut เป็น **proof point ของ vertical agent category** ที่ Enabridge ติดตามมาตั้งแต่ Q2 2026 — ทีซิสคือ "generic agent framework" (CrewAI, AutoGen, LangGraph) ไม่ชนะเกม enterprise ตรง ๆ; สิ่งที่ชนะคือ **pre-built workflow agent สำหรับ vertical process** ที่ domain-rich. O2C เป็น **เนื้อหอมที่สุด** ของ CFO suite เพราะ ROI วัดได้ตรง — DSO ลด 10 วัน = cash flow เพิ่ม ล้าน ๆ (คำนวณได้)

Pattern ที่เห็นในหลายดีลตอนนี้: **Sierra** (customer service), **Harvey** (legal), **Hippocratic AI** (healthcare), **Clay** (sales enrichment), และตอนนี้ **Stuut** (O2C) — vertical agent builder ที่ raise rounds ใหญ่ขณะที่ generic framework ลด valuation ลงหลายเจ้า. **Unit economics ของ vertical agent ดีกว่า** เพราะ: (1) ตีราคาตาม outcome ได้ (Vida ก็ pivot ไปทางนี้), (2) ตลาด switch cost สูง (ย้าย AR software ใช้เวลา 6-12 เดือน), (3) data moat สะสม (model fine-tune บน dispute patterns ของ 150 enterprise)

Signal อีกชั้นคือ **a16z + M12 + Insight ลง deal เดียวกัน**. ปกติ Insight (growth) และ a16z (early) จะไม่ตก deal เดียว — แต่ตลาด vertical agent ตอนนี้ hot จน early-stage shop ที่ลงใน Series A ยอมอยู่ต่อถึง Series B. การลงร่วมกันของ Microsoft M12 ก็สะท้อนว่า Microsoft เลือก **"ซื้อ equity ใน vertical agent"** แทนที่จะสร้าง Dynamics 365 Receivables Agent เอง — เป็น strategic signal ว่า Microsoft ยอมให้ ecosystem fill vertical gap

## มุม AI Agent Platform

**Builders:** ถ้ากำลังสร้าง agent framework ให้ builder อื่น, Stuut round บอกชัดว่า **ตลาด end-customer ของ framework ของคุณคือ vertical agent startup** — ไม่ใช่ enterprise CIO ตรง ๆ. ขายให้ Harvey/Stuut/Sierra ง่ายกว่าขายให้ Fortune 500. และ framework ที่ **expose tool interface สำหรับ ERP integration** (NetSuite, SAP, Oracle Fusion, Microsoft Dynamics) จะได้ premium — เพราะทุก vertical agent ขายเข้าตลาด enterprise ก็ต้อง integrate ERP เดิมทั้งนั้น

**Users / business:** CFO ไทยในกลุ่มขนาดกลาง-ใหญ่ (บริษัทจดทะเบียน, enterprise B2B) ที่ยัง process AR แบบ manual หรือ semi-automated ด้วย RPA เดิม มี **benchmark จริง** ว่า agent รัน O2C แล้วลด DSO 47% ได้ (ถ้าตัวเลข Stuut จริง). ไม่ต้อง pilot generic Microsoft 365 Copilot และหวังผลลัพธ์ — สามารถ RFP vertical O2C agent (Stuut, Tabs, Serrala) ตรง และ measure ROI ภายใน 6 เดือน. **Ecosystem:** NetSuite, SAP, Microsoft Dynamics, Oracle Fusion ควรเปิด API พิเศษสำหรับ **"agentic O2C partner"** — เพราะ vertical agent จะ aggregate volume ของการเข้าถึง ERP เข้มกว่า human user; ถ้าไม่ ERP vendor จะกลายเป็น commoditize layer ที่ margin หด ขณะที่ Stuut ครอง decision layer

## Sources
- [Stuut Lands $52.5M Series B From Insight, a16z and M12 to Scale AI Order-to-Cash Agents - AI Weekly](https://aiweekly.co/alerts/stuut-lands-525m-series-b-from-insight-a16z-and-m12-to-scale-ai-order-to-cash)
- [Stuut raises $52.5M Series B to run order-to-cash with AI - The Next Web](https://thenextweb.com/news/stuut-52-5m-series-b-ai-order-to-cash)
- [Stuut Raises $52.5M to Automate Enterprise Order-to-Cash - Efficiently Connected](https://www.efficientlyconnected.com/?p=9585)
- [Stuut raises $52.5M from Insight Partners and a16z to unlock $16 trillion in unpaid invoices - HackerNoon](https://hackernoon.com/stuut-raises-$525m-from-insight-partners-and-a16z-to-unlock-$16-trillion-in-unpaid-invoices)

---

## Audio script
Stuut startup นิวยอร์กปิด Series B 52 ล้านครึ่ง วันพุธ Insight Partners นำ Andreessen Horowitz กับ Microsoft M12 ร่วม. funding รวม 93 ล้านหลังปิด Series A แค่ 10 เดือนก่อน. ที่ Stuut ทำแตกต่างคือ scope. ไม่ใช่ copilot ช่วย AR team ร่าง email แต่เป็น autonomous agent รันลูป order-to-cash ครบ 5 สเตจ — collections cash application payments disputes deductions. ตัวเลขที่บริษัทรายงาน 150 enterprise รวม Verifone ZoomInfo Bishop Lifting ประมวลเงิน 3 พันล้าน จับคู่ payment 95% อัตโนมัติ collection 81% ไม่ใช้คน ลด DSO 47%. ถ้าจริงมี impact ตรง working capital ของบริษัท. ที่สำคัญคือ Insight Partners เป็น growth VC ที่เลือก deal ยาก การลง Stuut สะท้อนว่า vertical AI agent เป็น category ใหม่แยกจาก horizontal copilot. a16z กับ M12 ร่วมใน deal เดียวกันปกติไม่เกิด แสดงว่าตลาดนี้ hot. Microsoft M12 เลือกซื้อ equity ใน vertical agent แทนสร้าง Dynamics Receivables Agent เอง เป็น strategic signal. Pattern ชัด. Sierra Harvey Hippocratic Clay Stuut — vertical agent ที่ raise ใหญ่ขณะ generic framework ลด valuation. Unit economics ชนะเพราะ outcome pricing ได้ switch cost สูง data moat สะสม. CFO ไทยที่ยัง process AR แบบ semi-manual มี benchmark ชัดแล้ว ไม่ต้องรอ pilot generic copilot. ERP vendor ไทยควรเปิด API พิเศษสำหรับ agentic O2C partner หรือจะโดน commoditize
