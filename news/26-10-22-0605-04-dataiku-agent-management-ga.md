---
date: 2026-10-20
slug: dataiku-agent-management-ga
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a central glass control room labeled
  "AGENT INVENTORY" surrounded by eight tall platform silos, each with a bold
  label: "AWS BEDROCK", "DATABRICKS", "VERTEX", "COPILOT STUDIO", "AZURE FOUNDRY",
  "AGENTFORCE", "SNOWFLAKE CORTEX", "n8n". Each silo has agents inside shown as
  little glowing orbs that stream into the control room via color-coded pipes.
  Above the control room, three stacked numbers: "8 PLATFORMS", "1 INVENTORY",
  "OPENTELEMETRY". Clean editorial style, deep slate and signal yellow palette,
  strong contrast for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-22-0605-04-dataiku-agent-management-ga.png
---

# Dataiku ปล่อย Agent Management GA — ตัว inventory layer ที่ส่อง agent ทั้ง 8 platform ของ enterprise

## TL;DR
- Dataiku เปิด **Agent Management GA** เดือน ต.ค. 2026 — standalone product ที่ **ไม่ต้องใช้ Dataiku platform**, inventory agent ข้าม **8 vendor stack**: AWS Bedrock, Databricks Agents, Google Vertex, Microsoft Copilot Studio, Azure Foundry, Salesforce Agentforce, Snowflake Cortex, n8n (+ Dataiku เอง)
- รองรับ **OpenTelemetry** สำหรับ custom runtime — คือ agent ไหนยัง emit OTel span ได้, Dataiku จับได้
- สำหรับ "high-risk agent" (agent ที่จับ customer, sensitive data, live transaction), product keeps standing record ของ certification status, named risk, และ scheduled test ที่ re-run เป็นระยะ
- Signal: **agent sprawl + agent governance** กลายเป็น category ใหม่ของ MLOps/LLMOps — คู่แข่ง: Credo AI, Fiddler AI, Humanloop, Arize AI, LangSmith — Dataiku ที่มี foothold enterprise อยู่แล้วลงมา consolidate

## เกิดอะไรขึ้น

Dataiku — vendor data science platform สัญชาติฝรั่งเศส ที่เริ่มชื่อ "Dataiku DSS" ปี 2013 มี valuation ล่าสุด **$3.7B** (Dec 2024) — เปิด **Agent Management GA** ในเดือน **ต.ค. 2026**, ต่อจากการประกาศครั้งแรกที่ **Dataiku Succeed** conference เมื่อ 24 ก.ย. ตัว product คือ **standalone offering** — ลูกค้าไม่จำเป็นต้องมี Dataiku platform ก็ใช้ได้. จุดเด่น: มันเป็น **cross-platform inventory + governance layer** ที่สแกน agent ของลูกค้าในทุก stack แล้ว roll up มาเป็น **single pane**

Connector ที่ Dataiku support ใน GA release: **AWS Bedrock, Databricks Agents, Google Vertex AI Agent Builder, Microsoft Copilot Studio, Azure AI Foundry, Salesforce Agentforce, Snowflake Cortex, n8n** และ Dataiku ของตัวเอง. สำหรับ runtime ที่ไม่ได้อยู่ใน connector list — Dataiku support **OpenTelemetry** standard ให้ agent emit span กลับมา. eWeek note ว่า depth ของ cross-platform visibility ขึ้นกับ **ความลึกของแต่ละ integration** — บาง stack เปิด API full, บางตัวแค่ metadata layer

Feature ที่น่าสังเกตที่สุด: **agent risk classification + scheduled testing**. สำหรับ agent ที่จัด customer-facing, sensitive data, หรือ live transaction, Dataiku บังคับให้มี **certification record** ที่ระบุ: (1) risk categorization (high/medium/low), (2) named risk list (เช่น "prompt injection", "credential leak", "unauthorized action"), (3) **test suite ที่ re-run ตาม schedule** และ roll up certification status กลับมา. คือ pattern ที่ยืมมาจาก **model governance** ของ MLOps เดิม — แต่ปรับ semantic ให้เป็น "agent action" ไม่ใช่ "model prediction"

## ทำไมสำคัญ

Dataiku กำลัง bet ว่า **"agent sprawl"** จะเป็น real pain point ของ 2027 — คือ enterprise จะมี agent 50-500 ตัวใน production แบ่ง stack 5-10 เจ้า, และ CIO/CISO จะต้องการ **single-pane-of-glass** เพื่อตอบ auditor กับ board ว่า "agent ที่เราใช้มีอะไรบ้าง ทำอะไรได้ กินข้อมูลไหน". Pattern ของ **"shadow IT"** ย้ายจาก SaaS tool ยุค 2015 ไปที่ agent ยุค 2026 — เพราะ no-code builder (Copilot Studio, Agentforce, Vertex Agent Builder) ทำให้ business user สร้าง agent เองได้โดยที่ IT ไม่รู้

จุดที่ต่าง: Agent Management ของ Dataiku ไม่ใช่ **observability tool** แบบ LangSmith หรือ Arize ที่ focus trace/span. มันเป็น **governance tool** ที่ focus "ทะเบียน agent + risk status + certification lifecycle". คู่แข่งตรงกว่าคือ **Credo AI** (AI governance platform ที่เพิ่งปิด Series B $45M เดือน พ.ค. 2026) และ **Humanloop** (prompt + agent governance). Credo AI focus compliance หนัก (EU AI Act, NIST AI RMF), Dataiku positioning เป็น **ops-first แบบ enterprise ที่ production-centric** — ไม่ใช่ compliance-first

เลเยอร์ที่สำคัญกว่าคือ **Dataiku ขายตัวนี้ให้ลูกค้าที่ไม่ใช่ Dataiku customer ได้** — คือ market expand ของ company. ก่อนหน้าจะขายได้แค่คนที่ลง Dataiku DSS; ตอนนี้ pitching ตัว governance layer ให้ Fortune 500 ที่ลง stack Microsoft + Salesforce + AWS โดยไม่มี Dataiku ก็ยังได้. ถ้า pitch work ตัวเลข ARR ของ Dataiku จะเพิ่มจาก base ที่ไม่เคย lock เข้า

## มุม AI Agent Platform

สำหรับ **Builders** ของ agent framework: **ถ้า framework คุณไม่ emit OpenTelemetry trace, คุณจะหายจาก inventory ของ enterprise ที่ลง governance layer** — Dataiku, Credo AI, Humanloop ทั้งหมดใช้ OTel. ควร prioritize OTel compat ขั้นต่ำ + agent card metadata แบบ A2A. สำหรับ **Users / Business**: ถ้า organization มี agent ใน production > 20 ตัวจาก stack ที่หลายกว่า 2, pattern ที่ควรลงทุนคือ **governance platform + agent registry** ก่อน scale ไปเพิ่ม. ไม่งั้นจะไปตัน incident แล้วไม่รู้ว่า agent ตัวไหนเป็นสาเหตุ. สำหรับ **Ecosystem**: category "agent governance" เพิ่งเกิดเป็น formal segment ปี 2026 นี้ — Dataiku, Credo AI, Fiddler AI, Humanloop, Arize AI ชนกัน. ภายใน 18 เดือน จะมี **1-2 เจ้า consolidation** — คน buyer จะไม่อยากจ่าย 5 vendor คน governance + observability + evaluation + security + registry. ใครที่ bundle ครบ win ขั้วใน Fortune 1000

## Sources
- [Dataiku Launches Agent Management for enterprise AI agents (Dataiku)](https://www.dataiku.com/company/news/dataiku-agent-management-general-availability)
- [Dataiku Says It Can Track AI Agents Across Platforms: What Can It See? (eWeek)](https://www.eweek.com/news/dataiku-ai-agent-tracking-platform-visibility/)
- [How Dataiku Solves Enterprise AI Agent Sprawl and Risk (Technology Magazine)](https://technologymagazine.com/news/how-dataiku-solves-enterprise-ai-agent-sprawl-and-risk)

---

## Audio script
Dataiku เปิดตัว Agent Management GA ในเดือนตุลาคม 2026 เป็น standalone product ที่ไม่ต้องใช้ Dataiku platform ก็ใช้งานได้. ตัว product ทำหน้าที่เป็น inventory layer + governance layer ที่สแกน agent ของบริษัทข้าม 8 vendor stack ได้แก่ AWS Bedrock, Databricks Agents, Google Vertex, Microsoft Copilot Studio, Azure Foundry, Salesforce Agentforce, Snowflake Cortex, n8n รวม Dataiku ของตัวเอง. สำหรับ runtime ที่ไม่ได้อยู่ใน connector list, Dataiku รองรับ OpenTelemetry standard ให้ agent emit span กลับมา. Feature ที่น่าสังเกตที่สุดคือ risk classification กับ scheduled testing — สำหรับ agent ที่จัด customer-facing หรือ sensitive data, product บังคับให้มี certification record ที่ระบุ risk level, named risk list, และ test suite ที่ re-run เป็นระยะ. Pattern ที่ Dataiku bet คือ agent sprawl จะเป็น real pain ของปี 2027 — คือ enterprise จะมี agent 50 ถึง 500 ตัวใน production แบ่ง stack 5 ถึง 10 เจ้า และ CIO ต้องการ single pane of glass เพื่อตอบ auditor. Signal สำหรับ builder คือ ถ้า framework คุณไม่ emit OpenTelemetry trace คุณจะหายจาก inventory ของ enterprise ที่ลง governance layer. และคู่แข่งโดยตรงคือ Credo AI, Humanloop, Arize AI, LangSmith — ภายใน 18 เดือนจะมี consolidation 1-2 เจ้าแน่
