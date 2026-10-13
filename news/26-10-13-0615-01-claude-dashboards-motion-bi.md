---
date: 2026-10-12
slug: claude-dashboards-motion-bi
topic: agentic-ai
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial illustration: a glass dashboard panel floating above a dark data
  warehouse, with a single glowing line of SQL beneath each chart like a
  receipt — numbers "ONE SQL PER CHART" and "LAST REFRESH" rendered large and
  readable at thumbnail size. Anthropic warm-cream and burnt-orange palette on
  deep indigo background, flat isometric style, 1:1 aspect, no real human
  faces. Visual metaphor: BI with its homework shown.
image: images/26-10-13-0615-01-claude-dashboards-motion-bi.png
---

# Claude Dashboards + Motion เข้า beta — Anthropic เปิดแนวรบ BI ด้วย "SQL ใต้ทุก chart" และ dashboard ที่ update ตัวเองจาก warehouse

## TL;DR
- 8-9 ต.ค. **Anthropic** เปิด **Claude Dashboards** และ **Claude Motion** ใน beta — Dashboards ให้ user ถามเป็นภาษาธรรมดา แล้ว Claude เขียน SQL + สร้าง dashboard ที่ **update ตัวเองเมื่อ data เปลี่ยน**
- Data sources ที่ประกาศ: **Amazon Redshift, BigQuery, ClickHouse, Databricks, Snowflake** + apps ที่ connect ไว้ (Salesforce เป็นตัวอย่าง)
- Core differentiator: **หนึ่ง chart = หนึ่ง SQL query ที่ Claude โชว์ให้ดู + timestamp refresh ล่าสุด** — ไม่ใช่ BI แบบ black-box
- Plans: Dashboards อยู่บน **Pro, Max, Team, Enterprise**; Motion เฉพาะ **Team + Enterprise** และ Enterprise ต้องเปิดใน Organization settings ก่อน
- Caveat: **ยังไม่มี row-level security, scheduled refresh + alerts, audit log, version history** — Looker / Tableau / Mode ยังนอนเล่น (ชั่วคราว)

## เกิดอะไรขึ้น

วันที่ 8 ต.ค. Anthropic ประกาศ Claude Dashboards และ Claude Motion ในฐานะ beta features บน paid plans — ส่วนขยาย natural ของ Artifacts ที่ย้าย Claude จาก "ตอบคำถามเกี่ยวกับ data" ไปสู่ **"สร้างและ maintain surface ที่ data อยู่"**. สิ่งที่ต่างจาก BI legacy: ไม่มี schema modeling ขั้นตอน, ไม่มี drag-and-drop designer, ไม่มี semantic layer — user พิมพ์คำถาม, Claude อ่าน warehouse ของตัวเอง, generate SQL, run, แล้วแสดง chart; ทุก chart มี **SQL ที่ run ให้ดู + last refresh time**

ขอบเขต data source กว้างกว่าที่คนคาดการณ์ — Amazon Redshift, BigQuery, ClickHouse, Databricks, Snowflake รวมอยู่ตั้งแต่ day 1 บวกกับ app ที่ connect ไว้แล้ว (Salesforce เป็นตัวอย่างที่ Anthropic เน้นบ่อย; byteiota รายงานเพิ่ม MongoDB + Datadog แต่ outlet อื่นไม่ยืนยัน). นั่นแปลว่า **tech moat ของ Looker (schema modeling + LookML) และ Tableau (semantic layer + published data source) ถูก sidestep ไปตรง ๆ** — ลูกค้า Snowflake ที่ไม่อยากซื้อ BI license เพิ่มสามารถเปิด Claude Dashboards แล้วอาศัย business user คุยกับ data ได้ทันที

Motion เป็นผลิตภัณฑ์คู่ที่ animate dashboard ให้กลายเป็น auditable animation สำหรับการ present — Anthropic positioning ว่าเป็น "data narrative ที่ auditable" ซึ่งจำกัดเฉพาะ Team + Enterprise. ทั้งคู่รัน under Artifacts, ซึ่งใน Enterprise ต้อง admin เปิดเองใน Organization settings — Anthropic ไม่กล้าปล่อย default-on ให้ data governance team ต้องวิ่ง incident response ตอน Monday morning

จุดอ่อนที่ชัด: **ยังไม่มี row-level security** (RLS), ไม่มี scheduled refresh พร้อม alert, ไม่มี audit log, ไม่มี version history — คือ feature ที่ enterprise BI สะสมมา 15 ปี. ที่ Claude ชนะ ณ จุดนี้คือ **time-to-first-chart** และ **transparency ของ SQL** — ที่ Looker/Tableau แพ้คือ feature parity ของ governance; game กลายเป็น race ว่า Anthropic หรือ incumbent ใครขยับเร็วกว่า

## ทำไมสำคัญ

นี่คือ **ครั้งแรกที่ foundation model vendor ย้ายจาก assistive layer ไป system-of-record layer** ของ data analytics. Anthropic กำลังทำกับ BI สิ่งที่ **Microsoft Copilot ทำกับ Office**: ไม่พยายาม disrupt tool ที่มีอยู่ตรง ๆ, แต่สร้าง interface ใหม่ที่ bypass tool นั้น + ต่อตรงกับ data layer

Point of view: BI incumbent **ไม่ตายทันที** — row-level security, metric layer, และ change management ของ enterprise data team ยังทำให้ Looker / Tableau / Mode ปลอดภัยอีก 18-24 เดือน. แต่ **บทที่สำคัญคือ pricing power หายไป** — ตอนนี้ Snowflake customer ที่จ่าย Looker $150/user/month คิดใหม่: ถ้า Claude Pro $20/mo สร้าง dashboard พื้นฐานได้ 70%, deal size ของ Looker ต้องชี้แจงมากขึ้น. ครั้งหน้าที่ renew contract = negotiation ปั่นป่วน

ที่น่าสนใจกว่าคือ **"SQL ที่ Claude โชว์ให้ดู"**. นี่คือการ positioning ตรงข้าม ChatGPT Code Interpreter และ Looker AI — Claude ไม่ hide การคิดของ model; โชว์ query ที่ run, data source ที่แตะ, timestamp ที่ refresh. สำหรับ compliance-sensitive vertical (finance, healthcare, pharma) นี่คือ **ตั๋วเข้าห้องประชุมที่ Looker ไม่มี** — auditor ถามว่า "เลขนี้มาจากไหน" = คลิก SQL แล้วอ่านได้. Looker ตอบไม่ได้ง่ายขนาดนั้น (semantic layer อยู่ระหว่าง user กับ warehouse)

Pattern ที่เห็นชัด: **AI vendor ที่คุมทั้ง model + interface + runtime กำลัง collapse BI stack เป็น 1-2 ชั้น**. ปี 2024 BI มี 5 ชั้น (warehouse → semantic → modeling → viz → embedded). ปี 2026 Claude Dashboards กำลัง compress เป็น 2 ชั้น (warehouse → Claude). อีก 18 เดือน Snowflake Cortex, Databricks AI/BI Genie, OpenAI Operator จะไล่ตามด้วย feature เดียวกัน — **tooling layer ตรงกลางหายไป**

## มุม AI Agent Platform

**Builders:** ถ้าคุณสร้าง vertical BI product (healthcare analytics, retail analytics) — moat ที่เหลือคือ **data model + domain logic ที่ encode in semantic layer** ไม่ใช่ UX ของ dashboard builder. Claude กำลังทำ UX ให้เป็น commodity. Startup ที่จะอยู่รอดใน 24 เดือนข้างหน้าต้อง own **data pipeline + metric definition + compliance workflow** ไม่ใช่แค่ "chart ที่สวย"

**Users / business:** CFO/CDO ที่ sign Looker/Tableau renewal ภายใน 6 เดือน — เปิด Claude Dashboards POC กับ 2-3 team ก่อน; benchmark **time-to-first-dashboard, SQL quality, drift rate เมื่อ schema เปลี่ยน**. ถ้า Claude ทำได้ 70%+ ของ use case = เริ่ม pressure incumbent lower pricing หรือ shift seat allocation. ที่ยังต้องระวัง: Claude Dashboards **ไม่มี RLS** = sensitive data (PII, PHI, financial) ยังต้องผ่าน governance layer เดิม

**Ecosystem:** Snowflake + Databricks ได้ประโยชน์เพราะ query volume เพิ่ม (Claude Dashboards = เครื่อง query generator); Looker + Tableau + Mode เสีย because mid-market mindshare เริ่มไหลไปทาง AI-native UI. Semantic layer vendor (Cube, dbt Semantic Layer, AtScale) อยู่ที่ **inflection point** — ถ้า integrate กับ Claude Dashboards เป็น "RLS + metric definition provider" = ชนะใหญ่; ถ้า ignore = ถูก bypass. Fivetran + Hightouch (data movement) ไม่กระทบ

## Sources
- [Anthropic — Claude Dashboards and Motion in beta](https://www.unite.ai/anthropic-launches-claude-dashboards-and-motion-takes-docs-out-of-beta/)
- [TestingCatalog — Claude launches Dashboards and Motion in beta](https://www.testingcatalog.com/claude-launches-dashboards-and-motion-in-beta/)
- [AlphaSignal — Claude Dashboards and Motion turn data into auditable animations](https://alphasignal.ai/news/anthropic-ships-claude-dashboards-and-motion-to-turn-data-into-auditable)
- [eesel.ai — Claude Dashboards review 2026: how it works, plans, limits](https://www.eesel.ai/blog/claude-dashboards-review)
- [Shashi.co — Claude Builds a Live Dashboard From Your Warehouse and Shows the SQL](https://www.shashi.co/2026/10/claude-builds-live-dashboard-from-your.html)
- [Byteiota — Claude Dashboards and Motion: What They Actually Do](https://byteiota.com/claude-dashboards-motion-beta/)

---

## Audio script
วันพุธที่ผ่านมา Anthropic เปิด Claude Dashboards และ Claude Motion ใน beta — เรื่องนี้ founder ไทยที่ใช้ Looker หรือ Tableau ต้องฟัง. Dashboards ให้ user ถามเป็นภาษาธรรมดา แล้ว Claude เขียน SQL เอง สร้าง dashboard ที่ update ตัวเองเมื่อ data เปลี่ยน. รองรับ Snowflake, BigQuery, Redshift, Databricks, ClickHouse ตั้งแต่ day 1. Salesforce ก็ได้ ผ่าน app integration

จุดที่ต่างจาก BI legacy คือสองอย่าง. หนึ่ง — ไม่ต้อง schema modeling ไม่ต้อง LookML ไม่ต้อง published data source. สอง — ทุก chart โชว์ SQL ที่ run ให้ดู พร้อม timestamp refresh ล่าสุด. ถ้า CFO ถามว่า เลขนี้มาจากไหน. คลิก SQL อ่านได้ทันที. Looker กับ Tableau ตอบไม่ได้ง่ายขนาดนี้

ด้าน plan — Dashboards อยู่บน Pro, Max, Team, Enterprise. Motion เฉพาะ Team กับ Enterprise. Enterprise ต้องให้ admin เปิดใน organization settings ก่อน. Anthropic ระวังพอสมควร เพราะยัง ไม่มี row-level security ไม่มี audit log ไม่มี version history. feature ที่ enterprise BI สะสม 15 ปี Claude ยังไม่มี

แต่ที่สำคัญคือ pricing power ของ BI incumbent หาย. Looker ลูกค้า Snowflake ที่จ่าย $150 ต่อ user ต่อเดือน ตอนนี้ต้องชี้แจงว่า ถ้า Claude Pro $20 ต่อเดือน ทำ dashboard พื้นฐานได้ 70% ของ use case. ทำไมต้องจ่ายเพิ่ม. Deal renewal รอบหน้าจะปั่นป่วนแน่

สำหรับทีม Enabridge. ถ้าคุณสร้าง vertical BI product — moat ที่เหลือคือ data model, metric definition, compliance workflow. ไม่ใช่ dashboard builder UX ที่ Claude กำลังทำให้เป็น commodity. ถ้าคุณเป็นคนซื้อ BI — POC Claude Dashboards กับ 2-3 team ก่อน renewal. Benchmark time-to-first-chart และ SQL quality. แล้วใช้ pressure ลด price กับ incumbent

สัญญาณใหญ่กว่าคือ foundation model vendor กำลัง collapse BI stack เป็น 2 ชั้น — warehouse ตรงไป Claude. tooling layer กลางหายไป. อีก 18 เดือน Snowflake Cortex, Databricks Genie, OpenAI Operator จะมา feature เดียวกัน. ปี 2027 ตลาด BI คือตลาด infrastructure และ compliance ไม่ใช่ตลาด UI
