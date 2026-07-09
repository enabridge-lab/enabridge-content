---
date: 2026-07-10
slug: 8090-135m-chamath-enterprise-coding-agent-salesforce-ventures
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  A wide editorial isometric scene: a massive glass-walled software factory
  labeled "8090 SOFTWARE FACTORY" with conveyor belts carrying code blocks
  stamped "PRODUCTION-READY" out of the building into three logo-branded
  loading docks — "REGULATED FINANCE", "HEALTHCARE", "DEFENSE". Above the
  main entrance, a giant banner "$135M SERIES A — LED BY SALESFORCE VENTURES".
  In front, a small executive silhouette stepping through a glass door
  labeled "CEO" while board-member desks are being packed away. Side stat
  panel: "AUDIT TRAIL — ENTERPRISE CONTROLS — BUILT-IN". Cinematic editorial
  lighting, high contrast, 1:1 aspect, readable at 200px thumbnail, no real
  human faces.
image: images/26-07-10-0608-03-8090-135m-chamath-enterprise-coding-agent-salesforce-ventures.png
---

# Chamath ปิด $135M Series A ให้ 8090 + นั่ง CEO เอง — Salesforce Ventures ลากขบวน bet "enterprise coding agent สำหรับตลาด regulated"

## TL;DR
- **8090 Labs** ปิด **$135M Series A** (29 มิ.ย.) นำโดย **Salesforce Ventures** + **WndrCo, Craft Ventures, The Production Board, Launch** + angel รวม Nikesh Arora (CEO Palo Alto Networks) และ Adam D'Angelo (CEO Quora)
- **Chamath Palihapitiya นั่ง CEO เต็มเวลา** — ก่อนหน้าเป็น board member/founder — งาน operator ตัวแรกตั้งแต่ออกจาก Facebook (2011)
- Product คือ **Software Factory** — enterprise coding agent สำหรับ **regulated industry (finance, healthcare, defense)** ที่ต้องมี **audit trail + enterprise control** ในทุก commit — ต่างจาก Cursor/Cognition Devin ที่เน้น developer productivity ทั่วไป

## เกิดอะไรขึ้น
เย็นวันจันทร์ 29 มิ.ย. (ปล่อย press full ทั้ง TechCrunch, Yahoo Finance, Business Wire) — Chamath Palihapitiya ประกาศ **8090 Labs** ปิด Series A **$135M** นำโดย **Salesforce Ventures** พร้อม co-lead จาก **WndrCo (Jeffrey Katzenberg), Craft Ventures, The Production Board, Launch**. Angel investor รวม **Nikesh Arora (CEO Palo Alto Networks) และ Adam D'Angelo (CEO Quora)** — signal ชัดว่า deal นี้ underwriting โดย enterprise security executive + AI operator

ที่โดดกว่าตัวเลข: **Chamath ประกาศนั่ง CEO เต็มเวลา** — job operator ตัวแรกตั้งแต่ออกจาก Facebook ปี 2011 หลังจาก 15 ปีเป็น GP ของ Social Capital + SPAC investor + podcast host. ในสัมภาษณ์กับ TechCrunch เขาบอกว่า "AI can be the grand equalizer" — โจทย์คือ Fortune 500 ที่ยัง ship code แบบเก่าอยู่เพราะ regulated industry รับ Cursor/Copilot ไม่ได้ (source code leak, no audit trail, no data residency)

**Product ตัวหลัก: Software Factory** — Chamath ก่อตั้ง 8090 มาตั้งแต่ ม.ค. 2024 (เกือบ 2 ปีก่อน funding round) เป้าคือให้ enterprise dev team ก้าวข้าม prototype → production **โดยที่ทุก commit มี audit trail** — ใครสั่ง, agent ตัวไหนเขียน, ผ่าน review อะไรบ้าง, ข้อมูล training ไปไหน. Enterprise control includes: on-prem/private cloud deployment, IdP integration, per-repo permission, DLP scanning ที่ layer agent

Chamath พูดใน pitch ทาง Instagram: **"AI ที่คู่แข่ง sell ให้ 500,000 developer ทั่วโลก — ผมสร้างสำหรับ 5,000 CTO ของ Fortune 500 ที่ต้องการ regulated market SLA"** — สรุปตัว positioning ทั้งบริษัทได้ในบรรทัดเดียว

## ทำไมสำคัญ
Deal นี้เป็น **signal ที่ 3 สำหรับ pattern "Salesforce ล่า enterprise coding agent"** — ก่อนหน้านี้ Salesforce Ventures ลง Cognition (Devin), และ Windsurf (recent deal ก่อน acquisition rumor). Salesforce ต้องการ **layer coding agent ที่ integrate กับ Agentforce 360** ก่อนที่ Microsoft (GitHub Copilot Enterprise) + AWS (Q Developer) จะ dominate developer stack. Salesforce Ventures นำ round นี้บ่งบอก **มี strategic option ที่ 8090 จะกลายเป็น layer ใน Agentforce Developer** ในไตรมาสถัดไป

การเลือก Chamath นั่ง CEO เป็น **statement ทางตลาด** — ตำแหน่ง 8090 ไม่ใช่แข่ง Cursor/Cognition ที่ dev-first, แต่แข่ง Palantir/Snowflake/Databricks ที่ enterprise-first. Chamath มี relationship กับ Fortune 500 CFO/CIO ผ่าน 15 ปีของ SPAC + Berkshire-adjacent network — ใช้ pitch enterprise sale ได้ทันที. เทียบกับ founder AI ทั่วไปที่ต้องสร้าง Fortune 500 network 3-5 ปีก่อนขายได้จริง — 8090 skip ขั้นตอนนั้นด้วย Chamath direct

Pattern ที่เห็นในตลาด — **enterprise coding agent กำลังแตกออกเป็น 2 layer**: (1) **developer productivity layer** — Cursor, GitHub Copilot, Windsurf, Cognition — sell ที่ developer, PLG, self-serve; (2) **enterprise governance layer** — 8090 Labs, Distyl, Codeium enterprise — sell ที่ CTO/CIO, top-down, contract 6-9 หลัก. **8090 เดินเข้า layer 2 โดยตรงด้วย $135M** — บ่งบอกว่า VC เห็น TAM ของ layer นี้ใหญ่พอที่จะ underwriting $1B+ outcome

Regulated industry pattern (finance/healthcare/defense) เป็น **market niche ที่ hyperscaler ยังไม่ตอบ** — เพราะ Microsoft/AWS/Google ต้อง commit multi-tenant SaaS ก่อน. 8090 มี window 12-18 เดือนก่อนที่ Microsoft ที่ Frontier Co launch ในไตรมาสก่อน (ที่เราคุยไปแล้วในรอบก่อน) จะเข้ามา — ช่วงเวลานี้ 8090 ต้องปิด showcase customer 5-10 รายใน Fortune 500 เพื่อ lock relationship

## มุม AI Agent Platform
**Builders** — startup ที่ยังคิดว่า "sell agent = sell subscription ให้ developer" ต้อง revisit. Enterprise regulated market ต้องการ **agent-as-controlled-runtime**: (1) on-prem/private cloud deploy option, (2) IdP + fine-grained RBAC, (3) audit trail ทุก tool call ไป SIEM, (4) DLP scanning + PII detection ก่อน commit, (5) data residency control (US vs EU vs APAC). Framework builder ที่มี **enterprise-ready deployment guide + on-prem support** (Anthropic Claude Enterprise, OpenAI Enterprise self-hosted, Cohere North) มี tailwind เดียวกับ 8090

**Users/business ในไทย** — SCB, KBank, KTC, AIS ที่ต้องการ AI coding agent แต่ติดเรื่อง PDPA + BOT/OIC regulation + on-prem requirement — Sofware Factory เป็น reference model ใหม่. Vendor selection ในไตรมาสถัดไปควรถาม: agent มี audit trail per commit ไหม? DLP scanning ก่อน commit ไหม? on-prem/private cloud option ที่ไม่ leak source code ไหม? **ถ้าไม่มี ตัดออก** — เพราะ regulator ไทยจะตาม US SEC/FINRA ที่ตอนนี้เริ่ม audit AI-generated code แล้ว

**Ecosystem** — Chamath positioning "AI = grand equalizer" เป็น narrative ที่ SEA public + regulator กำลัง buy — pattern น่าจะ trigger local VC (Beacon VC, InnoVen, 500 Global SEA) มองหา clone/localization ในไทย/สิงคโปร์/อินโดเสีย. **SI ไทย** (Bluebik, G-Able, MFEC, Bizanywhere) ที่มี relationship กับธนาคาร/insurance/telecom สามารถ pitch เป็น distribution partner ของ 8090 ในไทยได้ — pattern เดียวกับที่ Microsoft Frontier Co ใช้ Big-4 consulting เป็น channel

## Sources
- [Chamath Palihapitiya raises $135M Series A for his AI coding startup, takes CEO role — TechCrunch](https://techcrunch.com/2026/06/29/chamath-palihapitiya-raises-135m-series-a-for-his-ai-coding-startup-takes-ceo-role/)
- [8090 Raises $135M Series A to Accelerate Their Rollout of Software Factory — Business Wire](https://www.businesswire.com/news/home/20260626795833/en/8090-Raises-$135M-Series-A-to-Accelerate-Their-Rollout-of-Software-Factory)
- [Palihapitiya Takes CEO Role at 8090 Labs After $135M Salesforce Ventures-Led Round — TechTimes](https://www.techtimes.com/articles/319378/20260630/palihapitiya-takes-ceo-role-8090-labs-after-135m-salesforce-ventures-led-round.htm)
- [Chamath Palihapitiya Announces $135 Million Funding, Rare CEO Title For 8090 — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/chamath-palihapitiya-announces-135-million-110110136.html)

---

## Audio script
วันจันทร์ที่ 29 มิถุนายน Chamath Palihapitiya ประกาศ 8090 Labs ปิด Series A 135 ล้านดอลลาร์ นำโดย Salesforce Ventures มี WndrCo Craft Ventures The Production Board และ Launch ร่วมกัน angel investor รวม Nikesh Arora CEO Palo Alto Networks และ Adam D'Angelo CEO Quora สิ่งที่โดดกว่าตัวเลขคือ Chamath ประกาศนั่ง CEO เต็มเวลา เป็น job operator ตัวแรกตั้งแต่ออกจาก Facebook ปี 2011 หลังเป็น GP Social Capital และ SPAC investor มา 15 ปี Product ตัวหลักชื่อ Software Factory ก่อตั้งมาตั้งแต่มกราคม 2024 target ที่ regulated industry finance healthcare defense ที่ต้องมี audit trail กับ enterprise control ในทุก commit ต่างจาก Cursor หรือ Cognition Devin ที่เน้น developer productivity ทั่วไป Chamath ประกาศใน pitch ว่า AI ที่คู่แข่ง sell ให้ 500,000 developer ทั่วโลก ผมสร้างสำหรับ 5,000 CTO ของ Fortune 500 ที่ต้องการ regulated market SLA สรุปตัวบริษัททั้งบริษัทได้ในบรรทัดเดียว signal ที่ 3 ของ pattern Salesforce ล่า enterprise coding agent Salesforce Ventures เคยลง Cognition และ Windsurf มาก่อน ต้องการ layer coding agent ที่ integrate กับ Agentforce 360 ก่อน Microsoft GitHub Copilot Enterprise กับ AWS Q Developer จะ dominate stack สำหรับธุรกิจไทย SCB KBank KTC AIS ที่ต้องการ AI coding agent แต่ติดเรื่อง PDPA กับ BOT regulation กับ on-prem requirement Software Factory เป็น reference model ใหม่ vendor selection รอบต่อไปให้ถาม agent มี audit trail per commit ไหม DLP scanning ก่อน commit ไหม on-prem private cloud option ไหม ถ้าไม่มีตัดออก เพราะ regulator ไทยจะตาม US SEC ที่ตอนนี้เริ่ม audit AI-generated code แล้ว
