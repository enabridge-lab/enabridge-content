---
date: 2026-11-03
slug: snowflake-always-on-coco-cowork
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a large glass office at night with
  two glowing cubes labeled "COCO" (coder) and "COWORK" (knowledge
  worker) running on their own, lights still on while desks sit empty.
  Memory bubbles stack behind each cube: "MEMORY", "PROFILES",
  "ASYNC AGENT API". A giant banner reads "ALWAYS-ON" with a smaller
  stat tile: "60+ INDUSTRY DATASETS". A tiny admin silhouette holds a
  clipboard labeled "ROUTING RULES". Deep navy and electric teal palette,
  1:1 aspect, no real human faces (silhouettes OK), high contrast so text
  stays readable at 200px.
image: images/26-11-09-0607-04-snowflake-always-on-coco-cowork.png
---

# Snowflake เปลี่ยน CoCo + CoWork เป็น always-on agent — persistent memory, async API, 60+ industry datasets

## TL;DR
- 3 พ.ย. ที่ Snowflake Expedition 2026: ประกาศ "always-on bots" สำหรับ **CoCo** (agent สำหรับ data team) และ **CoWork** (agent สำหรับ knowledge worker)
- **Async Agent API** — CoWork รัน long-running multi-step work ใน background ต่อเนื่อง, resume ได้ถ้า interrupted
- **Persistent memory** — เก็บ context + decision ข้ามรอบ; user ดู/แก้/ลบได้
- **CoWork Profiles** — admin ตั้ง agent access + routing rules ที่ end user ลบไม่ได้ → governance ที่ compliance รักออก
- **AI data package** — 60+ curated industry datasets + semantic views + ready-to-use CoWork agent; CoWork rebrand จาก "Snowflake Intelligence" ที่เริ่มต้นปี 2026

## เกิดอะไรขึ้น
วันที่ 3 พฤศจิกายน ที่ Snowflake Expedition 2026 Snowflake ประกาศ "always-on" upgrade สำหรับ agent ทั้งสองตัวของตัวเอง — **CoCo** ซึ่งเป็น coding agent สำหรับ data team (ชื่อเต็ม "Cloud Agents and Automations" ที่เริ่มต้นเดือน มิถุนายน 2026) และ **CoWork** ซึ่งเป็น personal AI work agent สำหรับ knowledge worker (rebrand จาก Snowflake Intelligence) การ upgrade รอบนี้แกนกลางอยู่ที่ 3 ชิ้น: async, memory, profiles

**Async Agent API** คือ shift ที่สำคัญที่สุด — เดิม agent รันเป็น request-response ภายใน session เดียว หนักก็ 10 นาที rotation ใหม่ CoWork สามารถรัน multi-step work ที่ยาวเป็นชั่วโมง ใน background — user ปิด laptop ไปได้ กลับมา agent ยังทำงานอยู่ และถ้า agent โดน interrupt (เช่น model restart, network blip) มันจะ resume จากจุดที่หยุด pattern เดียวกันกับ Traversal Workers (ที่รัน incident investigation ยาว) หรือ Claude Computer Use ที่รันเป็น background job

**Persistent memory** ให้ CoCo กับ CoWork เก็บ context และ decision ที่เคยทำข้ามรอบ — เช่น "user ชอบ output แบบ bullet list", "team นี้ใช้ convention นี้สำหรับ SQL alias" ฯลฯ จุดที่ enterprise กังวลคือ privacy — Snowflake ตอบด้วยการให้ user view/update/delete memory ที่ store ไว้ และ **CoWork Profiles** ให้ admin ตั้ง access policy + routing rules (เช่น "agent ของ finance team ห้ามอ่าน HR schema") ที่ end user ไม่สามารถ override ได้

สุดท้าย Snowflake ปล่อย **AI data package** — ชุดมากกว่า 60 curated industry datasets พร้อม semantic views และ ready-to-use CoWork agent — เช่น retail traffic data, healthcare claims data, financial market data — target ลูกค้า vertical ที่อยาก deploy agent เร็วโดยไม่ต้องสร้าง data pipeline จาก scratch

## ทำไมสำคัญ
สอง pattern ที่สำคัญ หนึ่ง — **async + persistent = agent จริง** ไม่ใช่ chatbot ที่ dress up ตลอด 2025-26 agent ส่วนใหญ่ ที่ enterprise deploy ยังเป็น short-session: assistant ที่ตอบคำถาม, generate code snippet, สรุป meeting แต่เมื่อ async + memory ครบ + governance แน่น → agent เริ่มทำ long-running work (reconcile trade, generate quarterly report, rewrite data pipeline) ใน background พนักงานไม่ต้อง watch over shoulder Pattern นี้เริ่มเห็นใน Anthropic Claude Code (long task), Cognition Devin, OpenAI Operator, Snowflake CoWork ตอนนี้ — ปี 2027 จะเป็น norm ของ enterprise agent

สอง — **data platform กลายเป็น agent platform** Snowflake กับ Databricks แข่งกันครอง stack นี้ ตั้งแต่ปี 2024 ที่ค่อย ๆ embed AI feature ใน warehouse ตอนนี้ไปไกลกว่านั้น — agent ที่ run on top of governed data, with lineage, with role-based access, ด้วย semantic layer ที่บริษัททุกคนใช้งานอยู่แล้ว argument sales คือ "ข้อมูลของคุณอยู่ที่นี่แล้ว agent ที่ดีที่สุดคือ agent ที่อยู่ next to data" คู่แข่ง — Google BigQuery, Microsoft Fabric, AWS SageMaker — ต้องเล่นเกมเดียวกัน Snowflake มี first-mover ด้วย CoCo + CoWork ที่ branded ชัด

## มุม AI Agent Platform
**Builders** — Async agent + persistent memory เริ่มเป็น table stakes ของ agent framework ยุคใหม่ ใครยังสร้าง agent framework แบบ request-response + stateless จะเริ่มลำบากในปี 2027 LangGraph, LlamaIndex Workflow, CrewAI Flows, และ Semantic Kernel ล้วน shift ไปทาง durable execution + checkpointing ส่วน MCP — Snowflake CoWork implement MCP ได้ตั้งแต่ Summit 2026 ตอนนี้ MCP เป็น standard ที่แทบทุก agent platform ต้อง support ไม่ว่า vendor จะชอบหรือไม่

**Users / business** — ถ้าองค์กรคุณใช้ Snowflake เป็น data warehouse หลัก อยู่แล้ว CoWork + CoCo เข้าถึงง่าย และ governance ก็ reuse role + masking ที่มีอยู่ ปัญหาคือ pricing — Snowflake ยังคิดเป็น credit บน compute agent ทำงาน background 8 ชั่วโมง = เท่ากับ query heavy ที่ CFO จะถาม ทุก brief ที่ deploy CoWork ต้องมี FinOps budget ชัดเจน ไม่ใช่ปล่อย agent รันไปไม่มี cap

**Ecosystem** — Databricks จะ counter เร็วที่ Data + AI Summit มิ.ย. 2027 ด้วย Mosaic AI Agents + async + memory เช่นกัน การแข่งขันนี้ดีสำหรับทุกคน — pricing จะลง, feature จะมาตรฐาน, governance จะดีขึ้น ส่วน vertical SaaS (Workday, ServiceNow, SAP) ที่สร้าง agent ของตัวเอง ต้องตัดสินใจว่าจะ bypass data warehouse ไปทำ agent ของตัวเอง หรือ wrap Snowflake/Databricks agent เข้า product

## Sources
- [Snowflake adds always-on AI bots for CoCo CoWork (IT Brief)](https://itbrief.com.au/story/snowflake-adds-always-on-ai-bots-for-coco-cowork)
- [Snowflake CoWork gets AI upgrades for knowledge workers (Techzine)](https://www.techzine.eu/news/analytics/141751/snowflake-cowork-gets-ai-upgrades-for-knowledge-workers/)
- [Snowflake CoCo and CoWork power the agentic enterprise (ITWire)](https://itwire.com/business-it-news/business-intelligence/snowflake-coco-and-cowork-power-the-agentic-enterprise-grounded-in-governed-data-and-built-for-autonomous-action)
- [Snowflake Pushes AI Agents Beyond Prompts and Into Persistent Work (Artiverse)](https://www.artiverse.ca/snowflake-pushes-ai-agents-beyond-prompts-and-into-persistent-work/)

---

## Audio script
Snowflake ประกาศ always-on upgrade สำหรับ agent สองตัวของตัวเองที่ Expedition 2026 เมื่อวันที่ 3 พฤศจิกายน CoCo เป็น coding agent สำหรับ data team ส่วน CoWork เป็น personal AI work agent สำหรับ knowledge worker การ upgrade แกนกลางมี 3 ชิ้น หนึ่งคือ Async Agent API ที่ทำให้ CoWork รัน multi-step work ยาวเป็นชั่วโมงใน background user ปิด laptop ได้ และถ้า agent โดน interrupt มัน resume จากจุดที่หยุด สองคือ persistent memory ที่เก็บ context และ decision ข้ามรอบ และสามคือ CoWork Profiles ที่ให้ admin ตั้ง access และ routing rule ที่ end user ลบไม่ได้ ซึ่งเป็น governance ที่ compliance team ชอบ Snowflake ยังปล่อย AI data package 60 industry datasets พร้อม ready-to-use agent สำหรับ vertical ที่อยาก deploy เร็ว pattern ที่สำคัญคือ async บวก persistent memory บวก governance เท่ากับ agent จริง ไม่ใช่ chatbot ที่ dress up pattern นี้เริ่มเห็นใน Claude Code, Cognition Devin, OpenAI Operator และ Snowflake CoWork ปี 2027 จะเป็น norm ของ enterprise agent สำหรับคนที่สร้าง agent framework ยุคใหม่ async execution และ durable checkpointing กำลังเป็น table stake ถ้ายังสร้างแบบ request-response stateless จะเริ่มลำบาก ส่วนองค์กรที่ใช้ Snowflake อยู่แล้ว CoWork เข้าถึงง่าย แต่ต้องมี FinOps budget ชัดเจน เพราะ agent รันยาวในชั่วโมงเท่ากับ query หนักที่ CFO จะถาม
