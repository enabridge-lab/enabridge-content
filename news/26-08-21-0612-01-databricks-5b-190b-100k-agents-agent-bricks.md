---
date: 2026-08-21
slug: databricks-5b-190b-100k-agents-agent-bricks
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  A vast editorial illustration of an industrial-scale "agent factory" made of
  data pipes and glowing lakehouse tanks feeding thousands of tiny robotic
  agents on a conveyor. Above the scene three stacked headline numbers glow:
  "$190B", "$7B RUN-RATE", "100K AGENTS". A subtle Databricks-style flame
  emblem sits on the tank. Editorial isometric style, deep navy background,
  amber and cyan accents, dramatic lighting. 1:1 aspect, no real human faces.
image: images/26-08-21-0612-01-databricks-5b-190b-100k-agents-agent-bricks.png
---

# Databricks ปิด $5B @ $190B — "agent demand" ดัน run-rate ทะลุ $7B, 100K agent ถูก build บน Agent Bricks แล้ว

## TL;DR
- Databricks ปิดรอบ $5B ที่ valuation $190B (จาก $134B เมื่อ 6 เดือนก่อน) — Coatue นำ, Blackstone/MGX/T. Rowe Price/Sixth Street ร่วม
- Revenue run-rate ทะลุ $7B, โต >80% YoY. Lakebase (agent database, launch มิ.ย. 2025) ถึง $100M ARR ในปีเดียว
- 100K+ agents สร้างแล้วบน Agent Bricks, ประมวลผลกว่า 1 quadrillion tokens ต่อปี — data platform กำลังกลายเป็น agent platform โดยตรง

## เกิดอะไรขึ้น

Databricks ปิดรอบ funding $5B ที่ valuation $190B เมื่อ 13 ส.ค. — จาก $134B เมื่อ 6 เดือนก่อน, นำโดย Coatue พร้อม Blackstone, MGX, T. Rowe Price, และ new investor Sixth Street Growth. TechCrunch รายงานว่าบริษัทตั้งใจจะระดม $1B, VC เสนอมา $15B, สุดท้าย compromise ที่ $5B — signal ว่าทั้งสองฝั่งเห็นตรงกันว่า Databricks ไม่ได้ขาย equity เพื่อรอด แต่รับ cash เพื่อไม่ต้องรีบ IPO ในตลาดที่ยังผันผวน

ตัวเลข operations น่าสนใจกว่ารอบ: revenue run-rate ทะลุ $7B, โต >80% YoY ใน Q2 — เร็วกว่า Snowflake (~$4B run-rate ตอนไล่กัน) และ overtake ทั้ง market cap ด้วยแล้ว. Lakebase — "database for agents" ที่ launch เมื่อมิ.ย. 2025 — พุ่งขึ้น $100M ARR ในปีเดียว. Lakehouse warehouse ยัง $1.5B+ run-rate ส่วน Genie (natural-language BI) กับ Agent Bricks ก็ทวีจำนวน user

Ali Ghodsi (CEO) ระบุใน press ว่า 100K agents ถูก build แล้วบน Agent Bricks, ประมวลผล over 1 quadrillion tokens ต่อปี — เป็นตัวเลขที่แสดงว่า pattern "build agents where the data lives" ทำงานจริง. Genie Ontology (knowledge graph ที่ต่อ 50+ system: Snowflake/BigQuery/Google Drive/SharePoint/Jira/Slack/Confluence) เป็นรากที่ทำให้ agents มี context เกิน siloed workspace

## ทำไมสำคัญ

Pattern ที่เห็นชัดตอนนี้คือ **data platform ทุกเจ้ากำลังบวก agent layer เข้าไปเป็น first-class primitive** — ไม่ใช่ feature เสริม. Snowflake มี Cortex Agents, MongoDB มี Atlas Vector + agent SDK, และ Databricks ไปไกลสุด — เพราะ Lakebase ถูก design ให้เป็น "agent state store" ตั้งแต่ต้น (low-latency writes, native OLTP บน lakehouse). $100M ARR ใน 12 เดือนคือ signal ว่า enterprise ยอมจ่ายเงินให้ database ที่ agent-native แม้ต้องย้ายจาก Postgres/Mongo เดิม

ตัวเลข "$7B run-rate โต 80%" เทียบกับ Snowflake ที่โต ~30% YoY บอกอะไรมากกว่าตัวเลขเดี่ยว: enterprise ที่กำลัง deploy agents ยอมจ่าย premium ให้ platform ที่รวม data + compute + agent orchestration ไว้ที่เดียว. ถ้า Databricks push run-rate ต่อไปโต 80% จนถึง Q4, จะแตะ $10B ก่อนคู่แข่งจะเห็นแนวโน้ม — และเป็นตัวปั่นให้ Snowflake ต้องเร่ง agent story ก่อน IPO cycle ถัดไป

## มุม AI Agent Platform

**Builders** ที่กำลังสร้าง agent framework: signal ตรงนี้คือ "context locality" กำลังกลายเป็น differentiator สำคัญกว่า "model quality" — agent ที่รันบน platform ที่เข้าถึง data โดยตรง (ไม่ต้อง ETL ออกไป) จะเร็วกว่าและถูกกว่า. LangChain/CrewAI/AutoGen ที่ยัง agnostic ต่อ storage อาจต้องหา partnership กับ data platform ไม่งั้นจะโดน bypass. **Businesses ที่ deploy agent**: การเลือก data platform ตอนนี้ = การเลือก agent runtime ใน 2–3 ปี — Lakebase, MongoDB Atlas, Snowflake Cortex ไม่ใช่ "แค่ database" แล้ว. **Ecosystem**: Databricks IPO ที่ likely จะเกิดใน 2027 น่าจะเป็น catalyst ให้ Snowflake/MongoDB/Confluent reprice — และเปิดช่อง SMB SaaS อย่าง Neon, PlanetScale, Turso ที่จะเสนอ "agent-native database" ในราคาที่ SMB จ่ายไหว

## Sources
- [Databricks wanted to raise $1B, investors wanted $15B. It settled on $5B at a $190B valuation (TechCrunch)](https://techcrunch.com/2026/08/13/databricks-wanted-to-raise-1b-investors-wanted-15b-it-settled-on-5b-at-a-190b-valuation/)
- [Databricks Grows >80% YoY, Surpasses $7B Revenue Run-Rate (Databricks Press)](https://www.databricks.com/company/newsroom/press-releases/databricks-grows-80-yoy-surpasses-7b-revenue-run-rate-scales)
- [Databricks Raises $5B at $190B Valuation (TechEdgeAI)](https://techedgeai.com/databricks-grows-80-yoy-surpasses-7b-revenue-run-rate-scales-lakebase-genie-and-unity-ai-gateway/)
- [Databricks closes $5B funding round at $190B valuation as revenue run-rate tops $7B (TechNode)](https://technode.global/2026/08/14/databricks-closes-5b-funding-round-190b-valuation-revenue-run-rate-7b/)
- [Databricks Data + AI Summit 2026: Key Announcements Recap (Atlan)](https://atlan.com/know/ai-agent/databricks/databricks-data-ai-summit-2026-announcements/)

---

## Audio script
Databricks ปิดรอบใหม่ $5,000 ล้านเหรียญ ที่ valuation $190,000 ล้านเหรียญ เมื่อ 13 สิงหาคม — ขึ้นจาก $134,000 ล้านแค่ 6 เดือนก่อน. เรื่องจริงที่น่าสนใจกว่ารอบระดมทุนคือตัวเลข operations: revenue run-rate ทะลุ $7,000 ล้าน โต 80 เปอร์เซ็นต์ YoY. แล้ว Lakebase ที่เป็น database สำหรับ agent โดยเฉพาะ เพิ่ง launch เดือนมิถุนายนปีที่แล้ว วันนี้ทะลุ $100 ล้าน ARR ในปีเดียว. Ali Ghodsi ซีอีโอบอกว่าตอนนี้มี agent ถูก build บน Agent Bricks 100,000 ตัว ประมวล tokens เกิน 1 quadrillion ต่อปี. เห็น pattern ชัดว่า data platform ทุกเจ้ากำลังแปลงตัวเองเป็น agent platform — ไม่ใช่ feature เสริม แต่เป็นหัวใจของ product ใหม่. Snowflake, MongoDB, Confluent ต้องรีบเดินเกม agent ก่อน Databricks จะทะลุ $10,000 ล้าน run-rate ปลายปีนี้. สำหรับคนที่กำลังเลือก stack ไป deploy agent — การเลือก data platform วันนี้ เท่ากับเลือก agent runtime ใน 2–3 ปีข้างหน้า.
