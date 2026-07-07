---
date: 2026-07-08
slug: databricks-openai-agent-bricks-hertz-lead-conversion
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  A wide editorial isometric factory floor labeled "AGENT BRICKS". Along the
  conveyor: golden brick blocks stamped "OPENAI", "ANTHROPIC", "GEMINI",
  "QWEN", "KIMI" flowing into a giant sorting gate labeled "UNITY AI GATEWAY".
  On the wall three giant scoreboards: "100K+ AGENTS BUILT", "1 QUADRILLION
  TOKENS/YR", "HERTZ 60–65% LEAD CONVERSION IN 11 DAYS". Below, tiny suited
  silhouettes labeled "ASTRAZENECA", "7-ELEVEN", "FOX", "BLOCK" carry finished
  bricks toward customer buildings. High contrast cinematic lighting, 1:1
  aspect, readable at 200px thumbnail, no real human faces.
image: images/26-07-08-0609-01-databricks-openai-agent-bricks-hertz-lead-conversion.png
---

# Databricks + OpenAI ปิด DAIS 2026 — Agent Bricks 100k agents, 1 quadrillion token/ปี, Hertz แปลง lead 60-65% ใน 11 วัน = data platform กลายเป็น agent runtime

## TL;DR
- Databricks ประกาศที่ Data + AI Summit 2026 (จบ 6 ก.ค.): **Agent Bricks มี agent ถูก build ไปแล้ว 100,000+ ตัว, ประมวลผลเกิน 1 quadrillion token ต่อปี**. Customer ที่ ship production: **AstraZeneca, 7-Eleven, Fox Corporation, Block**
- Case ตัวเปิดของงาน: **Hertz** พา insurance replacement business ขึ้นเวที — สร้าง agent ด้วย GPT-5.5 + Databricks ใน **11 business days** แล้วได้ **lead conversion rate 60-65%** จากลูกค้าที่โทรเข้ามาหลังเกิดอุบัติเหตุ
- Stack ใหม่: **Agent Bricks** (dev platform) + **Databricks Agent Tools** (governed data access ผ่าน MCP) + **Unity AI Gateway** (runtime governance) — รองรับ OpenAI, Anthropic, Gemini, Qwen, และเพิ่ม **Kimi** ในรอบนี้. Signal: **data warehouse platform โดยตรง กลายเป็น agent runtime + governance layer แทน stack ที่ต้องประกอบเอง**

## เกิดอะไรขึ้น
Data + AI Summit ของ Databricks จบลงเมื่อวันที่ 6 กรกฎาคม 2026 — และ blog สรุปคู่กับ OpenAI ที่ปล่อยตามหลังทันทีทำให้ทั้งอุตสาหกรรมเห็นภาพชัดว่า **Databricks ไม่ได้พยายามขาย "โมเดล" อีกต่อไป, แต่ขาย "โครงสร้างที่ agent จะ ship ไปสู่ production ได้"**. ตัวเลขที่ Ali Ghodsi (CEO) โยนขึ้นเวที: agent 100,000+ ตัวที่ถูก build ผ่าน Agent Bricks ตั้งแต่ launch, ประมวลผลรวมกันเกิน **1 quadrillion token ต่อปี** (10^15) — ตัวเลขนี้ใหญ่กว่า workload ของหลาย hyperscaler รวมกัน และ Databricks ยัน context เดียวคือ **enterprise data ที่อยู่ใน Unity Catalog อยู่แล้ว**

Case study ที่ประทับใจสุดคือ **Hertz** — บริษัทรถเช่าที่มีธุรกิจย่อยเรียกว่า "insurance replacement" (บริษัทประกันส่งลูกค้าที่รถชนไปเช่ารถทดแทนช่วง claim) เดิม lead conversion rate ต่ำเพราะ agent ในคอลเซ็นเตอร์ต้องประกอบข้อมูลจาก 3-4 ระบบ (insurance eligibility + rental inventory + pricing + fleet dispatch) ใน 30 วินาที ก่อนลูกค้าวางสาย. Hertz build agent บน Databricks + GPT-5.5 ใน **11 business days** (ประมาณ 2 สัปดาห์ทำงาน) แล้วยกระดับ conversion rate เป็น **60-65%** — ไม่ใช่ marginal improvement, เป็น step change ที่ Cliff Notley (Hertz Head of Digital Product) โชว์บนเวทีเป็น anchor case ของ Agent Bricks

Announcement คู่ขนาน — วันที่ 6 ก.ค. Databricks ปล่อย blog แยกอีกฉบับกับ OpenAI ว่า partnership ปีนี้ **"centered on production agents"**: Databricks Agent Tools ใน Agent Bricks ให้ OpenAI Codex + GPT-family เข้าถึง enterprise data ผ่าน **MCP** (Model Context Protocol) โดยมี **Unity AI Gateway** เป็น governance layer control ทั้ง cost + permission + audit. Customer เดียวกันเลือกได้ระหว่าง OpenAI, Anthropic, Gemini, Qwen — และรอบนี้เพิ่ม **Kimi** (Moonshot จีน) เข้ามา — routing ตัดตาม latency/price/compliance

## ทำไมสำคัญ
Pattern ที่โผล่ชัดในรอบนี้คือ **"data platform กินขึ้นมาเป็น agent runtime"** — เดิมทีมองว่า agent stack = model + framework (LangChain/CrewAI/Autogen) + tool integration + observability + vector DB, แล้ว data warehouse (Databricks/Snowflake) เป็นแค่ source ของ context. รอบนี้ Databricks บอกว่า "ใช่ทั้งหมดที่กล่าวมา แต่เราจะรวมมาให้อยู่ในบ้านเดียว" — Agent Bricks (build) + Unity Catalog (data + policy) + Unity AI Gateway (runtime + audit) + Agent Tools (MCP-based tooling). **"Composable agent stack" ที่ startup พยายามขาย 18 เดือน เพิ่งถูก assemble เป็น product เดียวโดย platform ที่ Fortune 500 มี license อยู่แล้ว**

Hertz case น่าสนใจกว่า number อีก — 11 business days คือ signal ว่า **cycle time จากไอเดีย → production agent** กำลังลดลงเร็วมาก. เทียบกับปีที่แล้วที่ Fortune 500 project เดียว = 6-12 เดือน (ต้อง evaluate framework, integrate vector DB, ตั้ง observability, ทำ eval harness, ผ่าน security review). Databricks + OpenAI ไม่ได้ทำให้ AI ฉลาดขึ้น — ทำให้ **cost ของการทดลอง agent ตัวใหม่ ตกลงถึงจุดที่ทีม product ตัดสินใจ launch ได้เอง**. เมื่อ marginal cost ของ agent ใหม่ = 2 สัปดาห์ + งบ marketing pilot, business unit จะ launch เยอะกว่าที่ IT รับได้ — บริษัทที่มี governance layer พร้อม (Unity AI Gateway) จะ scale ตัวนี้ได้, ที่ไม่มี = agent shadow IT ระเบิด

Contrast กับ Microsoft Frontier + AWS FDE ที่ประกาศสัปดาห์ก่อน — hyperscaler นั้นแก้ปัญหาด้วย **"ส่ง engineer มาฝังตัวกับลูกค้า"**; Databricks แก้ปัญหาด้วย **"ใส่ทุกอย่างที่จำเป็นในแพลตฟอร์มลูกค้าอยู่แล้ว"**. สองสูตรจะแบ่ง Fortune 500 workload กันคนละครึ่ง — Fortune 500 ที่มี Databricks license (โดยเฉพาะสายการเงิน/pharma/retail ที่ใช้ lakehouse หนัก) จะเลือกสูตรของ Databricks; ที่ไม่มี lakehouse อยู่แล้ว จะเลือก Microsoft/AWS FDE

## มุม AI Agent Platform
- **Builders** — framework แยก (LangChain, CrewAI, Autogen, LlamaIndex) โดน squeeze สองด้าน: Agent Bricks จาก data platform side, และ OpenAI/Anthropic agent SDK จาก model side. ทางรอดคือ (1) **specialization ใน niche vertical** (finance/pharma/legal/manufacturing agents ที่รู้ domain deep พอ), (2) **openness + observability + BYO-runtime** เป็น differentiator (deploy on Kubernetes/on-prem ที่ Databricks ทำไม่ได้), (3) partner กับ **data platform ระดับรอง** (Cloudera, MotherDuck, ClickHouse) ที่ไม่มี agent story ของตัวเอง. **Startup vertical agent (Sierra, Cresta, Decagon, Distyl)** ต้องเทียบ ROI ตรง ๆ กับ "Hertz-style" case ของ Agent Bricks — ถ้า marginal advantage ต่ำกว่า 2-3x จะขาย hard

- **Users / business** — บริษัทที่ใช้ Databricks อยู่แล้ว (SCB, KBank, Krungthai, บางส่วนของ CP/ThaiBev/PTT) ต้องเรียก account exec Databricks เข้ามาคุย Agent Bricks + Unity AI Gateway ในรอบ FY27 budget planning — สาม pain point ที่ platform นี้แก้: (1) governance กระจัดกระจาย (audit ยาก) รวมเป็นอันเดียวได้, (2) cost ของ token consumption ที่ไม่คุมกระจายทั่วองค์กร routing ผ่าน gateway ได้, (3) skill gap ของทีม data engineer ที่ต้องเรียน framework ใหม่ — Agent Bricks ใช้ pattern SQL/Python/notebook ที่ทีมเป็นอยู่แล้ว. **บริษัทที่ยังไม่มี lakehouse** — อย่ารีบ migrate เพราะ agent, ทำ Snowflake+Cortex หรือ Fabric แทน โมเดล economics ต่างกัน

- **Ecosystem** — MCP กลายเป็น "USB-C ของ agent tool" อย่างเป็นทางการหลังรอบนี้ (Databricks, Salesforce, ServiceNow, Anthropic, OpenAI ล้วนพูดถึง MCP เป็นภาษากลาง). ecosystem effect: **tool vendor** (Notion, Figma, JIRA, Slack) มี distribution ผ่าน MCP registry ของ platform ใหญ่ ไม่ต้อง integrate ทีละราย; **model vendor** ต้อง support MCP client อย่างเป็นทางการ — Kimi ที่เพิ่งเข้าคือ signal ว่า **model จีน (Qwen, Kimi, DeepSeek) กำลัง onboard เป็น first-class ใน platform Western** ผ่าน MCP layer

## Sources
- [OpenAI and Databricks at DAIS 2026: Making enterprise AI real — Databricks Blog](https://www.databricks.com/blog/openai-and-databricks-dais-2026-making-enterprise-ai-real)
- [Agent Bricks: Data + AI Summit 2026 — Databricks Blog](https://www.databricks.com/blog/agent-bricks-dais-2026)
- [Databricks Adds OpenAI Agent Tools for Enterprise AI — Let's Data Science](https://letsdatascience.com/news/databricks-adds-openai-agent-tools-for-enterprise-ai-6abd2c1b)
- [What is Databricks Agent Bricks? Platform and Context Layer — Atlan](https://atlan.com/know/ai-agent/databricks/agent-bricks/)

---

## Audio script
วันนี้ Databricks ปิด DAIS 2026 พร้อมกับ OpenAI ปล่อยข่าวคู่ขนาน สรุปว่าตอนนี้ Agent Bricks ของ Databricks มี agent ถูก build ไปแล้วเกินหนึ่งแสนตัว ประมวลผลรวมกันเกินหนึ่ง quadrillion token ต่อปี ลูกค้าที่ ship production มี AstraZeneca, 7-Eleven, Fox Corporation, และ Block เคสตัวเปิดของงานคือ Hertz ธุรกิจย่อย insurance replacement ที่บริษัทประกันส่งลูกค้ารถชนไปเช่ารถทดแทน Hertz build agent ตัวนี้บน Databricks กับ GPT 5.5 ใน 11 business days แล้วยกระดับ lead conversion rate จากลูกค้าที่โทรเข้ามา ให้ขึ้นไปที่ 60 ถึง 65 เปอร์เซ็นต์ ไม่ใช่ marginal improvement เป็น step change เลย stack ใหม่ที่ Databricks เสนอคือ Agent Bricks สำหรับ build บวก Databricks Agent Tools ให้เข้าถึงข้อมูลผ่าน MCP บวก Unity AI Gateway เป็น governance layer รองรับทั้ง OpenAI, Anthropic, Gemini, Qwen และเพิ่ม Kimi ในรอบนี้ pattern ที่โผล่ชัดคือ data platform กลายเป็น agent runtime โดยตรง ไม่ใช่แค่ source ของ context อีกต่อไป composable agent stack ที่ startup พยายามขาย 18 เดือนที่ผ่านมา เพิ่งถูก assemble เป็น product เดียวโดย platform ที่ Fortune 500 มี license อยู่แล้ว contrast กับ Microsoft Frontier กับ AWS FDE สัปดาห์ก่อนที่แก้ปัญหาด้วยการส่ง engineer ไปฝังตัว Databricks แก้ด้วยการใส่ทุกอย่างในแพลตฟอร์มลูกค้าอยู่แล้ว สองสูตรจะแบ่ง Fortune 500 workload กันคนละครึ่ง สำหรับธุรกิจไทย บริษัทที่ใช้ Databricks อยู่แล้ว SCB, KBank, Krungthai, บางส่วนของ CP กับ PTT ควรเรียก account exec เข้ามาคุย Agent Bricks กับ Unity AI Gateway ในรอบ budget planning ปีหน้าได้เลย
