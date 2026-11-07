---
date: 2026-11-07
slug: ocient-100m-petabyte-agentic-analytics
topic: use-case
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a vast underground data vault
  with giant stacks of glowing database cylinders labeled "PETABYTE".
  A huge sign reads "$100M SERIES C" with a smaller tag "$260M TOTAL".
  Robot agent silhouettes walk directly through the stacks reading them
  in place, with a dotted path labeled "NO COPY MOVE". A back wall banner
  reads "REVENUE 3X IN 2026". Snowflake and Databricks logos fade on a
  distant wall. Clean editorial style, deep navy and warm amber palette,
  1:1 aspect, high contrast so numbers read at 200px, no real human faces
  (silhouettes OK).
image: images/26-11-08-0604-02-ocient-100m-petabyte-agentic-analytics.png
---

# Ocient ปิด $100M Series C — พนัน $260M ว่า agent จะไม่ย้าย data ไป warehouse แต่จะวิ่งเข้า data เอง

## TL;DR
- Ocient ระดม Series C $100M (co-lead โดย BOKA Capital + OCA Ventures) ยอดรวม $260M, revenue คาดว่าจะโต 3 เท่าในปี 2026
- OcientAIQ รวม ingestion, analytics, governance และ agent orchestration ไว้ใน engine เดียวสำหรับ dataset ระดับ petabyte — compete ทาง pattern กับ Snowflake/Databricks
- Dealroom จัดอันดับ round นี้อยู่ใน top 10% ของ Series C enterprise software US (จาก 1,747 deal) — cybersecurity กลายเป็น vertical ที่โตเร็วสุด

## เกิดอะไรขึ้น
วันที่ 5 พฤศจิกายน Ocient — hyperscale data warehouse ที่ก่อตั้งใน Chicago และวางตัวเองเป็น competitor ของ Snowflake/Databricks มานาน — ประกาศปิด Series C ที่ $100M co-lead โดย BOKA Capital และ OCA Ventures พร้อม existing investor เข้าเพิ่มทั้งหมด ทำให้ยอดระดมสะสมแตะ $260M BOKA ยังได้ board seat ไปด้วย CEO Chris Gladwin บอก Unite.AI ว่าปี 2026 revenue จะมากกว่า 3 เท่าของปี 2025

สิ่งที่น่าสนใจคือ pitch ของ Ocient ในรอบนี้ไม่ใช่ "faster SQL" แบบเดิมแต่คือ **OcientAIQ** — platform ที่รวม 4 ชั้นเข้าด้วยกันใน engine เดียว: data ingestion, analytics query, governance, และ **agent orchestration** โดยยืนยันว่าการที่ agent รัน agentic workload "in-place" บน dataset โดยไม่ต้อง copy data ไปที่ feature store หรือ inference pipeline ต่างหาก เป็น edge ที่ engine architecture ของตัวเองรองรับได้จาก first principles (Ocient build engine ตัวเองเพื่อ petabyte-scale, ไม่ใช่ fork Postgres หรือ layer บน object storage)

Dealroom จัดอันดับ round นี้ติด top 10% ของ Series C ทั้งหมดของ US enterprise software ในช่วงเดียวกัน — สะท้อนว่า VC กำลัง re-rate "infrastructure ที่ agent รันได้โดยตรงบน data" สูงกว่า pure warehouse play SiliconAngle รายงานเพิ่มว่า cybersecurity (SIEM, threat hunting agent, insider risk detection) เป็น vertical ที่ demand แตกเร็วที่สุดสำหรับ OcientAIQ — makes sense เพราะ security log cardinality สูงจน copy-move architecture ทำไม่ได้ในทาง economic

## ทำไมสำคัญ
Narrative ของ 2024-25 คือ "copy data ไป warehouse แล้วเทรน model / inference ที่นั่น" — Snowflake/Databricks โตบนสคริปต์นี้ แต่ agent เปลี่ยนสมการ: agent ตัดสินใจเรียล-ไทม์, ขอ query ซ้ำหลายรอบต่อ turn, ต้องการ context จาก data หลาย domain พร้อมกัน — pipeline แบบ "copy then analyze" ไม่ทัน latency และ budget ของ agent workload นี่คือเหตุผลที่ engine architecture ที่รองรับ "agent-in-place" กลายเป็นหมวดที่ VC ให้ premium

เทียบกับคู่แข่ง — Snowflake ออก Cortex Agents และ Databricks ออก Mosaic AI Agent Framework ทั้งคู่ยัง bolt-on บน warehouse engine เดิม Ocient argument คือ engine ที่ออกแบบเพื่อ petabyte ตั้งแต่ต้น ให้ cost per agent query ต่ำกว่า จุดนี้ยังต้อง 3rd party verify แต่ถ้า revenue 3x ของปี 2026 ผ่าน audit ได้ จะเป็น proof point สำหรับ thesis นี้

Caveat สำคัญ — Ocient ยังไม่ถึง scale ของ Snowflake (ที่ public แล้ว) หรือ Databricks (IPO imminent), $260M total funding ยังเล็กเทียบกับคู่แข่งที่มี war chest เกิน $10B รวมกัน "being complementary rather than replacing" ที่ CEO ย้ำใน SiliconAngle แปลว่า go-to-market จริงคือ niche petabyte workload — ไม่ใช่ head-on fight

## มุม AI Agent Platform
**Builders** — ถ้าคุณกำลังสร้าง agent ที่ต้อง query data หลาย domain บ่อย ๆ (financial compliance agent, security SOC agent, operations analytics agent) architecture pattern ที่ควรพิจารณาคือ "agent orchestrator ภายใน data engine" แทนที่จะเป็น "agent service ข้างนอก + warehouse connector" latency, cost per turn, และ governance จะดีกว่าแบบมี meaningful margin — มากพอที่จะเปลี่ยน competitive positioning

**Users / business** — องค์กรไทยที่ cardinality log/transaction/customer data สูง (bank, telco, retail chain, insurance) ควร evaluate whether agent workload ของตัวเองจะวิ่งบน warehouse เดิมได้ หรือจะต้อง re-architect ไปที่ engine ที่ดีไซน์เพื่อ agent — การ migrate petabyte data cost เยอะ แต่ถ้าโตเกิน 10TB และต้องการ sub-second agent response ตัว architecture decision นี้ต้องขึ้นโต๊ะ CTO ภายในปี 2027

**Ecosystem** — Snowflake และ Databricks จะตอบด้วย engine-level rewrite หรือ acquisition ของ specialist อย่าง Ocient? ประวัติบอกว่า incumbent มัก acquire มากกว่า rewrite (Databricks ซื้อ MosaicML, Snowflake ซื้อ Neeva) — ราคา Ocient จึงน่าจะขึ้นเร็วในปี 2027 ถ้า revenue 3x ผ่านจริง

## Sources
- [Ocient Raises $100M in Series C Funding (FinSMEs)](https://www.finsmes.com/2026/11/ocient-raises-100m-in-series-c-funding.html)
- [Ocient raises $100M Series C to run AI on petabyte-scale data (Dealroom)](https://dealroom.co/news/169967-ocient-raises-100m-series-c-to-run-ai-on-petabyte-scale-data/)
- [Ocient raises $100M Series C to run AI on petabyte-scale data (SiliconANGLE)](https://siliconangle.com/2026/11/05/ocient-raises-100m-series-c-funding-run-ai-petabyte-scale-data/)

---

## Audio script
Ocient ซึ่งเป็น data warehouse ที่ก่อตั้งใน Chicago ประกาศปิด Series C ที่ 100 ล้านเหรียญเมื่อวันที่ 5 พฤศจิกายน co-lead โดย BOKA Capital และ OCA Ventures ทำให้ยอดระดมสะสมแตะ 260 ล้านเหรียญ CEO บอกว่าปี 2026 revenue จะมากกว่า 3 เท่าของปีก่อน Dealroom จัดอันดับว่า round นี้ติด top 10 เปอร์เซ็นต์ของ Series C enterprise software ใน US pitch ของ Ocient รอบนี้ไม่ใช่ faster SQL แบบเดิม แต่คือ OcientAIQ ที่รวม ingestion analytics governance และ agent orchestration ไว้ในเอนจินเดียวสำหรับ dataset ระดับ petabyte argument หลักคือการที่ agent รัน workload in-place บน data โดยไม่ต้อง copy ไปที่ feature store เป็น edge เชิง architecture ที่คู่แข่งทำไม่ได้ เพราะ Ocient build engine ของตัวเองตั้งแต่ต้นไม่ได้ fork postgres หรือ layer บน object storage ตลาดที่แตกเร็วคือ cybersecurity เพราะ log cardinality สูงจน copy แบบเดิมไม่ work สำหรับคนที่สร้าง agent ที่ต้อง query data หลาย domain บ่อยๆ pattern ที่ควรพิจารณาคือ agent orchestrator ภายใน data engine ไม่ใช่ agent service ข้างนอก สำหรับองค์กรไทยที่มี cardinality สูง เช่น ธนาคาร telco retail chain ประกัน การ evaluate architecture ใหม่ควรขึ้นโต๊ะ CTO ภายในปี 2027 ประวัติบอกว่า Snowflake กับ Databricks มักจะ acquire มากกว่า rewrite ราคา Ocient จึงน่าจะขึ้นเร็วในปี 2027 ถ้า revenue 3x ผ่าน audit ได้
