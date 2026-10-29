---
date: 2026-10-30
slug: snowflake-cortex-agents-thinking-stage-mounts
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: |
  An editorial isometric illustration of a glass "data vault" cube labeled
  "SNOWFLAKE STAGE", with three glowing dials on its control panel reading
  "THINKING: MINIMAL -> MAX", "SYSTEM INSTRUCTIONS", and "STAGE MOUNTS".
  A small sandbox terminal hovers beside the cube, mounting the stage via a
  luminous blue cable. Massive display text above: "AGENTS GET KNOBS".
  Deep teal and navy palette, Kodak-film grading, high contrast for 200px
  thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-30-0605-04-snowflake-cortex-agents-thinking-stage-mounts.png
---

# Snowflake Cortex Agents เพิ่ม thinking_effort + stage_mounts — agent primitive บน data warehouse เริ่ม "มี knob จริง"

## TL;DR
- **28 ต.ค.** Snowflake เพิ่ม 3 ตัวควบคุมใหม่ให้ **Cortex Agents Coding Agent** ผ่าน `agent:run` API
- **`thinking_effort`** — 6 ระดับ: `minimal | low | medium | high | xhigh | max` (model ที่ไม่ support ระดับ max จะถูก clamp ลงที่ระดับที่ model รับได้)
- **`instructions.system`** — field ใหม่ที่ append system-level directive เข้า agent request (เหมาะกับ guardrails / persona / context policy)
- **`stage_mounts`** — mount Snowflake stage (รวม versioned stage: notebook, Streamlit app, workspace, agent) เข้า agent sandbox; **ต่างจาก `workspace_mounts`** ที่มีอยู่, stage_mounts รองรับ artifact storage layer ที่กว้างกว่า
- Signal: ชั้น **"agent in data warehouse"** กำลัง mature จาก wrapper → runtime ที่มี **primitive น่าใช้งาน** — Snowflake push ตามรอย Databricks Agent Framework

## เกิดอะไรขึ้น

Snowflake release note วันที่ **28 ต.ค. 2026** ประกาศเพิ่ม 3 field ใหม่ให้ `agent:run` API ของ **Cortex Agents Coding Agent** (component ที่ Snowflake ใช้ขับ agent ภายใน workloads data analysis + ML + ETL ของลูกค้า):

**(1) `thinking_effort`** ตั้งค่า reasoning budget ให้ orchestration model ของ agent run. Enum: `minimal, low, medium, high, xhigh, max`. ความสำคัญคือ consistent naming ข้าม model backend — ถ้า user set `max` แต่ underlying model เป็น Snowflake Arctic Instruct Pro ที่ cap ที่ `high`, request จะถูก **downgrade** อัตโนมัติไปที่ `high` แทนที่ error. ชั้นนี้ปลด dev จากต้องรู้ว่า backend model คือตัวไหน — set effort = "max" แล้วให้ API resolve

**(2) `instructions.system`** append system-level instruction เข้า request. Position ชัดเจน: system > tool defaults > user prompt. Use case: enterprise ที่อยากฝัง policy (เช่น "ห้าม PII leave warehouse", "ตอบเป็นภาษาไทย", "ให้ ask-for-approval ก่อน DROP TABLE") โดยไม่ต้องแก้ user prompt หลายที่. ทำให้ compliance team control agent behavior ที่ **config level** แทนที่ UI level

**(3) `stage_mounts`** mount Snowflake stage เข้า sandbox ของ agent — ก่อนหน้านี้ sandbox เข้าถึงได้แค่ **workspace stage** ของตัวเอง (per `workspace_mounts`). stage_mounts รองรับ **versioned stage** ที่ Snowflake เพิ่งเพิ่มในชั้น platform: Snowflake Notebooks, Streamlit apps, Workspaces, Agents definitions. ชั้นนี้สำคัญเพราะ agent สามารถเรียก notebook/Streamlit app ที่ team สร้างไว้แล้วมาเป็น tool — reuse โดยไม่ต้อง re-implement. **stage mounts เป็น read-only ตาม default** (per code execution docs — "stages mounted for skills are read-only")

Context: นี่ไม่ใช่ feature launch ที่มี keynote — เป็น **doc update ที่ release-notes อย่างเงียบ**. แต่สะท้อน shift ของ Snowflake ที่ขยับจาก "เรา host SQL + ETL + ML" ไป "เรา host **agent runtime** ที่ data อยู่ที่เดียวกับ compute". Databricks ประกาศ Agent Framework ลักษณะคล้ายกันในฤดูร้อน; Snowflake ตามมาด้วย primitive layer ที่ **ไม่หนักทางการตลาด** แต่สะอาดใน API design

## ทำไมสำคัญ

ประเด็นที่หนึ่ง — **agent primitive บน data warehouse เริ่ม standardize**. ตั้งแต่กลางปี 2026 ผู้เล่น data platform (Snowflake, Databricks, BigQuery, Microsoft Fabric) แข่งเพิ่ม "agent capability" เพื่อป้องกัน churn ไปทาง Vercel/Modal + external agent framework. Snowflake update นี้สะท้อน pattern ที่เริ่มเหมือนกันข้าม vendor: (1) reasoning budget control (thinking_effort), (2) system instruction layer, (3) sandbox + stage integration สำหรับ artifact. ลำดับ API นี้คล้าย OpenAI Responses API + Anthropic Claude API + Databricks Agent Bricks — บ่งว่า **AAIF Open Responses standardization กำลัง influence API design จริง**

ประเด็นที่สอง — **"agent ที่ data อยู่ที่เดียวกับ compute"** คือยุทธศาสตร์ป้องกัน data exfiltration + latency. ก่อนหน้านี้ dev สร้าง agent framework (LangChain, CrewAI) ที่ pull data จาก Snowflake ไป compute นอก (OpenAI API, local script). ปัญหา: (1) data leave perimeter → compliance ร้อง, (2) 10× latency per tool call, (3) auditing กระจาย. Cortex Agents = agent **inside the warehouse** — data ไม่ขยับ, compute อยู่ติด Snowflake Virtual Warehouse เดิม, log อยู่ที่ Snowflake audit layer. ชั้น Fortune 500 ที่ก่อนลังเลจะ run agent บน sensitive data (healthcare, finance, defence) จะ migrate ไปใช้ in-warehouse agent runtime เพราะ **compliance envelope เท่าเดิม**

ประเด็นที่สาม — **stage_mounts = "notebook เป็น tool"** คือ pattern ที่ unlocked reuse ของ asset ที่ data team ลงทุนมา 5 ปี. ก่อนหน้านี้ Snowflake Notebook เป็นที่ data scientist expore; agent ไม่รู้จัก. ตอนนี้ agent mount notebook ที่ sanctioned ของ team เป็น tool — agent เรียก "run_demand_forecast_notebook(region=TH, horizon=90d)" ได้โดย data team ไม่ต้องเขียน MCP server แยก. ชั้นนี้ **short-circuit** ตลาด MCP server builder สำหรับ internal tooling: องค์กรที่มี Snowflake notebook ลึก + Streamlit app ลึก = agent toolkit พร้อม day one

## มุม AI Agent Platform

**Builders**: ถ้าคุณสร้าง agent framework ที่ pull Snowflake data external, update นี้บอกคุณว่า **long-term game อยู่ด้าน Vertical / specialized agent** ไม่ใช่ generic framework — เพราะ in-warehouse agent runtime ของ Snowflake/Databricks จะ "ดี enough" สำหรับ 70% use case ของ data team. ชั้นที่ยังเปิด: cross-warehouse agent (ที่ customer ใช้ Snowflake + Databricks + BigQuery ปนกัน), + domain agent (treasury agent, GTM agent, legal review agent) ที่ขายเป็น SaaS seat

**Users / business**: Snowflake customer (**10,000+ account, ~$3.5B ARR**) ตอนนี้มี agent primitive ที่ไม่ต้องรอ vendor ชิ้นที่ 11 — เขียน SQL + agent ใน UI เดียว, security policy เดียว, user access เดียว. Data team ที่เคย prototype agent บน OpenAI API แล้วติด security review สามารถ **re-platform บน Cortex Agents** ภายใน sprint เดียว. ธุรกิจไทยที่ run Snowflake (SCB, True, PTT bulk analytics) ได้ feature นี้พร้อม global release — ไม่มี regional gate

**Ecosystem**: ชั้น "MCP server for Snowflake data" ที่หลาย startup build (Nango, Fivetran MCP, Portkey) จะ demand ลดลง — เพราะ Snowflake customer เลือกใช้ in-house primitive ก่อน. White space ที่ยังเปิด: **cross-platform agent orchestration** (ที่ agent ทำงานข้าม Snowflake + Salesforce + S3 + Oracle Fusion) และ **vertical agent** ที่ domain knowledge หนา

## Sources
- [October 28, 2026: Cortex Agents Coding Agent thinking effort, system instructions, and stage mounts (Snowflake docs)](https://docs.snowflake.com/en/release-notes/2026/other/2026-10-28-cortex-agents-coding-agent-thinking-effort-stage-mounts)
- [Cortex Agent code execution tool (Snowflake docs)](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-code-execution-tool)
- [Inside Snowflake Intelligence: Five Pillars of Enterprise-Grade Agentic AI (Snowflake engineering blog)](https://www.snowflake.com/en/engineering-blog/inside-snowflake-intelligence-enterprise-agentic-ai/)

---

## Audio script
Snowflake ประกาศวันพุธ 28 ตุลาคม เพิ่ม 3 ตัวควบคุมใหม่ให้ Cortex Agents Coding Agent ผ่าน API ของตัวเอง หนึ่งคือ thinking_effort ที่ตั้ง reasoning budget ได้ 6 ระดับ ตั้งแต่ minimal ถึง max ถ้า model backend ไม่ support ระดับ max จะถูก downgrade อัตโนมัติแทนที่จะ error สองคือ instructions.system ที่ให้ enterprise ฝัง policy ระดับ system เช่น ห้าม PII leave warehouse หรือ ask for approval ก่อน DROP TABLE โดยไม่ต้องแก้ user prompt หลายที่ สามคือ stage_mounts ที่ mount Snowflake stage รวม versioned stage ของ notebook, Streamlit app, workspace, agent definition เข้า sandbox ของ agent ความสำคัญคือ ตอนนี้ agent สามารถเรียก notebook ที่ data team เขียนไว้แล้วเป็น tool ได้เลย ไม่ต้องเขียน MCP server แยก สิ่งที่ release note นี้สะท้อนคือ ชั้น agent primitive บน data warehouse กำลัง standardize ข้าม vendor ทั้ง Snowflake, Databricks, BigQuery, Microsoft Fabric วิ่งไปแนว API design เหมือนกัน คือ reasoning budget + system instruction + sandbox integration สำหรับ Thai enterprise ที่ใช้ Snowflake อยู่ ไม่ว่าจะเป็น SCB True PTT นี่คือ feature ที่ไม่ต้องรอ vendor ชิ้นที่ 11 เขียน SQL กับ agent ใน UI เดียว security policy เดียว audit layer เดียว compliance envelope เท่าเดิม
