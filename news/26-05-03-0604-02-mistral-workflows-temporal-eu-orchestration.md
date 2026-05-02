---
date: 2026-04-28
slug: mistral-workflows-temporal-eu-orchestration
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: Editorial illustration of branching tree-like pipelines flowing through a transparent factory floor, each branch carrying glowing data tokens, with a clean barrier separating control room from production line, minimal flat shapes, muted forest green and warm cream palette, dramatic side lighting, no text no logos no faces
image:
---

# Mistral เปิด Workflows — EU วาง orchestration plane ของตัวเอง สวน US hyperscaler

## TL;DR
- 28 เม.ย. — Mistral AI เปิด **Workflows** เข้า public preview ใน Mistral Studio: orchestration engine บน **Temporal** (เครื่องเดียวที่ Netflix/Stripe/Salesforce ใช้) สำหรับ AI workflow ที่ต้อง durable, observable, fault-tolerant
- เคลม **"millions of executions/day"** ตั้งแต่วัน preview เปิด — ลูกค้าที่ run อยู่จริงคือ **ASML, CMA-CGM, La Banque Postale, France Travail, ABANCA, Moeve** (เกือบทั้งหมดเป็น European industrial/financial heavyweight)
- Architecture แบบ **control plane / data plane split** — workers รันบน Kubernetes ของลูกค้า, data + business logic อยู่ในเขตของลูกค้า, control plane อยู่ฝั่ง Mistral — เป็นคำตอบ EU sovereign ที่ AWS/Azure ทำได้ลำบากกว่า

## เกิดอะไรขึ้น

วันที่ 28 เม.ย. Mistral AI ปล่อย **Workflows** ขึ้น public preview ใน Mistral Studio — เป็น orchestration layer สำหรับ enterprise AI ที่ออกแบบมาเพื่อ "ย้าย AI process จาก proof of concept ไป production reliability" — Mistral ระบุชัดเจนว่ายืน base infrastructure บน **Temporal** ซึ่งเป็น durable execution engine ที่ Netflix, Stripe, และ Salesforce ใช้ run workflow critical ของตัวเองมาหลายปี — แล้ว extend ขึ้นมาให้รองรับ AI-specific concerns: streaming, payload handling, multi-tenancy, observability

ตัวเลขที่หลายคนพลาดในข่าวนี้: Mistral อ้างว่า Workflows กำลัง run **"millions of executions per day"** ตั้งแต่วันที่เปิด preview — ไม่ใช่ launch เปล่า ๆ แต่เป็น launch with production traffic อยู่แล้ว ลูกค้าที่ Mistral เปิดเผยว่า run อยู่: **ASML** (กำลัง orchestrate semiconductor simulation steps — โหลดงาน R&D ที่ใช้คำนวณหนัก), **CMA-CGM** (logistics ทะเลรายใหญ่ของฝรั่งเศส — chain ระบบ legacy shipping API หลายตัวข้ามทศวรรษ), **France Travail** (หน่วยงานจ้างงานของรัฐฝรั่งเศส), **La Banque Postale** + **ABANCA** (ธนาคารสเปน), **Moeve** (oil & gas)

วิธี deploy ที่ทำให้ ASML/Banque ตอบรับเร็ว: **control plane / data plane split** — Mistral host orchestrator (state machine, scheduler, retry logic) ฝั่งของตัวเอง ส่วน workers ที่ทำงานจริงรันใน **Kubernetes ของลูกค้า** — data ทุกประเภท (PII, IP, financial transactions) ไม่เคยออกจาก security perimeter ของลูกค้า model นี้ไม่ใช่ใหม่ใน software architecture (Snowflake / Databricks เคยใช้แนวคล้ายกัน) แต่ใน AI orchestration นี่คือครั้งแรกที่มี vendor offer แบบ first-class — โดยเฉพาะสำหรับลูกค้า EU ที่ติดเรื่อง GDPR + EU AI Act + sovereign cloud requirements

วิธีที่ Mistral pitch business value: developers เขียน workflow เป็น Python ใน Mistral Studio — จาก **publish ขึ้น Le Chat** ทันที พนักงานในองค์กรใครก็ trigger workflow ผ่าน chat ได้ — UX แบบ "ไม่ต้องสร้าง app ใหม่" Le Chat กลายเป็น universal frontend สำหรับ workflow ทั้งหมดที่ทีม dev ลง

## ทำไมสำคัญ

ถ้าอ่านระหว่างบรรทัด — Mistral กำลังเล่นเกมที่ AWS/Azure/GCP **เล่นยาก**: **EU enterprise sovereignty** อาวุธของ EU ที่ไม่ใช่แค่กฎหมาย (GDPR, AI Act) แต่เป็นการที่ banking/government/industrial heavyweight ของ EU ไม่อยากผูก orchestration plane กับ US hyperscaler — กลัวเรื่อง CLOUD Act, data residency, vendor concentration risk Mistral ใช้ pain point นี้ตรง ๆ — host orchestrator ในยุโรป + รัน worker ใน customer's K8s + ใช้ Temporal (open standard) — ลูกค้าใหม่ ๆ ที่ลังเลกับ AWS Bedrock + Microsoft Agent 365 ตอนนี้มี **third option ที่เป็น European alternative อย่างจริงจัง**

เปรียบเทียบกับ **Microsoft Agent 365 GA (1 พ.ค.)** — สอง launch นี้ติดกัน 3 วัน ไม่ใช่บังเอิญ Microsoft ลง "control plane + governance" ส่วน Mistral ลง "execution engine + sovereignty" — สองชิ้นนี้คนละ wedge แต่บางส่วน overlap ลูกค้า EU ที่ต้องเลือก: ใช้ Agent 365 เป็น registry ของ agents แต่ใช้ Mistral Workflows เป็น orchestrator — น่าจะเป็น pattern ที่เห็นบ่อยใน 6 เดือนข้างหน้า ส่วน **OpenAI/AWS** ที่เพิ่ง launch GPT-5.5 + Codex + Bedrock Managed Agents เมื่อ 28 เม.ย. (วันเดียวกับ Mistral!) — ลงเฉพาะ "model + agent runtime" ยังไม่มี orchestration layer ระดับ Temporal-grade

Trajectory ระยะ 60-90 วัน: Mistral น่าจะเปิด **Workflows GA + on-prem deployment option** ตามมา + ขยาย customer disclosure จาก 6-7 รายเป็น 20-30 ราย; พร้อมกัน Mistral Workflows น่าจะกลายเป็น default orchestrator ใน EU public sector procurement ที่กำลัง roll out AI agent ภายใน Q3 ของกฎ EU AI Act; **competitive risk ต่อ LangGraph / LangSmith / CrewAI** สูงมาก — สาม framework นี้เป็น Python orchestrator แบบ open-source แต่ไม่มี enterprise SLA / Temporal-grade durability — ใครจ้างทีม dev ภายในให้ self-host LangGraph จะเริ่มถามคำถาม "ทำไมเราไม่ใช้ Mistral Workflows แทน"

## มุม OpenBridge

**Direct relevance สูง** — OpenBridge อยู่ตรง integration / orchestration layer ของ enterprise — Mistral Workflows คือสิ่งที่ดึงลูกค้า EU ไปให้ vendor European ก่อน OpenBridge เคลื่อน คำถามที่ทีมต้องตอบใน 30 วัน: **ถ้าลูกค้าระดับ ASML / Banque Postale มา OpenBridge แทน — เรามีอะไรที่ Mistral ให้ไม่ได้?** สามคำตอบที่มีศักยภาพ: (1) **vendor-neutral orchestration** — Mistral ดี แต่ผูก model ของ Mistral เป็นหลัก, OpenBridge route ระหว่าง Claude / GPT / Gemini / Mistral / open-source ได้; (2) **MCP-native composition** — chain MCP server หลายตัวเป็น flow เดียว ที่ Mistral Workflows ยังไม่ได้โฟกัส; (3) **legacy SaaS + ERP integration depth** — Mistral แข็งใน orchestration logic แต่ connector ecosystem ของ Workato/Zapier-grade ยังไม่มี — OpenBridge อยู่ในตำแหน่งที่จะเป็น "universal connector layer ที่ feed Mistral Workflows" แทนที่จะแข่งตรง

อีกข้อสำคัญ: Temporal เป็น **proven, well-understood foundation** — OpenBridge ควร evaluate ว่า engine ภายในของตัวเองสมควรย้ายไป Temporal-grade durability ด้วยหรือไม่ ลูกค้า enterprise จะเริ่มถามเรื่อง durability + observability ที่ Mistral Workflows / Temporal ตั้ง bar ใหม่ — ถ้า OpenBridge ใช้ orchestration engine ระดับต่ำกว่า จะมีคำถามใน RFP ทุกครั้ง

ระยะ 14 วัน ทีมควร: (1) ทดลอง Mistral Workflows preview ด้วย workflow จริง 1-2 ตัวที่ OpenBridge ใช้อยู่ — เปรียบเทียบ DX + observability + cost; (2) survey ลูกค้า EU ของ OpenBridge (ถ้ามี) ว่าเขา evaluate Mistral Workflows อยู่หรือไม่; (3) ตัดสินใจว่า OpenBridge จะ position เป็น "OpenBridge + Mistral co-deployment" หรือ "OpenBridge replace Mistral Workflows" — ถ้าเลือก co-deployment ต้องวาง integration ตอนนี้

## Sources
- [Workflows for work that runs the business — Mistral AI](https://mistral.ai/news/workflows)
- [Mistral AI launches Workflows, a Temporal-powered orchestration engine already running millions of daily executions — VentureBeat](https://venturebeat.com/technology/mistral-ai-launches-workflows-a-temporal-powered-orchestration-engine-already-running-millions-of-daily-executions)
- [Mistral AI Introduces Workflows for Orchestrating Enterprise AI Processes — InfoQ](https://www.infoq.com/news/2026/04/mistral-ai-workflows/)
- [Mistral AI takes on enterprise AI orchestration with Workflows — The Decoder](https://the-decoder.com/mistral-ai-takes-on-enterprise-ai-orchestration-with-workflows/)

---

## Audio script
อีกข่าวใหญ่จากฝั่งยุโรปวันที่ 28 เมษายน Mistral AI เปิด Workflows ขึ้น public preview ใน Mistral Studio เป็น orchestration engine ที่สร้างบน Temporal — engine ที่ Netflix, Stripe, Salesforce ใช้ run workflow critical อยู่แล้ว Mistral อ้างว่า Workflows รันอยู่ที่ "ล้าน execution ต่อวัน" ตั้งแต่วันแรกที่เปิด preview — ลูกค้าที่ใช้จริงคือ ASML สำหรับ semiconductor simulation, CMA-CGM ของฝรั่งเศสที่ chain shipping API legacy, La Banque Postale, France Travail, ABANCA, Moeve เกือบทั้งหมดเป็น EU industrial หรือ financial heavyweight วิธี deploy ที่ทำให้ลูกค้า EU ตัดสินใจง่ายคือ control plane รันฝั่ง Mistral ส่วน worker รันใน Kubernetes ของลูกค้า — data ไม่เคยออกจาก perimeter เลย ตอบโจทย์ EU AI Act กับ data sovereignty ตรง ๆ ที่ AWS หรือ Azure ทำได้ยากกว่า สำหรับ OpenBridge ตรงเป้ามาก — Mistral กำลังจะเป็น European default orchestrator ก่อนเราจะขยับ คำถามคือเรามีอะไรให้ลูกค้า ASML หรือ Banque Postale ที่ Mistral ให้ไม่ได้ คำตอบที่มีน้ำหนักคือ vendor-neutral routing ระหว่าง Claude GPT Gemini Mistral, MCP-native composition, กับ legacy connector depth ระดับ Workato — เรา position เป็น layer ที่ feed Mistral Workflows ได้ แทนที่จะแข่งตรง น่าจะเหมาะกว่า
