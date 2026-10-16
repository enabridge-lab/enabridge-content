---
date: 2026-10-16
slug: anthropic-dynamic-workflows-beta
topic: agentic-ai
reading_time_min: 3
sources: 2
image_prompt: |
  A floating cloud server labeled "CLAUDE PLATFORM" with a glowing root
  agent spawning a fan-out of child agents like a program tree; three
  stacked spec numbers hover beside it: "64 THREADS/RUN", "1000 AGENTS
  TOTAL", "$0.08 / SESSION-HR". Below, a dim desktop labeled "LOCAL" is
  being eclipsed. Editorial isometric style, Anthropic warm sand and
  deep plum palette, 1:1 aspect, no real human faces.
image: images/26-10-16-0615-05-anthropic-dynamic-workflows-beta.png
---

# Anthropic Dynamic Workflows: Claude Platform ย้าย orchestration ขึ้น server ของตัวเอง

## TL;DR
- **Dynamic workflows for Managed Agents** เข้า **beta บน Claude Platform** วันที่ 9 ต.ค. — agent เขียน code แล้ว server รัน workflow เองใน background
- Spec: **64 threads/run**, **1,000 agents ตลอด run**, **24 ชม. lifetime**, **10 runs open ต่อ session**
- Pricing: tokens ตามปกติ + **$0.08/session-hour** — ไม่มี orchestration fee แยก คือ price point ที่ undercut DIY infra

## เกิดอะไรขึ้น

วันพฤหัสที่ 9 ต.ค. Anthropic ปล่อย dynamic workflows เข้า beta ภายใน Claude Platform สำหรับ Managed Agents ซึ่งเป็น service ที่ host agent runtime ของตัวเอง หลักการคือ Claude Code ใช้ feature นี้มาตั้งแต่ 28 พ.ค. และตอนนี้ GA ไปแล้วใน Claude Code แต่สำหรับ Managed Agents บน platform เพิ่งเริ่ม beta

Pattern ของ dynamic workflow คือ **agent เขียน program (ไม่ใช่ graph) แล้ว server รันให้** — ต่างจาก static workflow (LangGraph, Temporal) ที่ต้อง pre-define node และ edge ล่วงหน้า Dynamic workflow ให้ root agent decide ที่ runtime ว่าจะ spawn sub-agent กี่ตัว, แต่ละตัวทำอะไร, ส่ง result กลับยังไง เหมือน `fork()` ของ Unix process

Hard limits ที่ Anthropic เขียนไว้ชัด: 64 thread ที่ทำงานพร้อมกันใน run เดียว, 1,000 agent ตลอดอายุ run, lifetime default 24 ชั่วโมง, 10 run open ต่อ session Pricing คิดแค่ token ตาม rate ของ model เดิมบวก $0.08 per session-hour — ซึ่งถ้าเทียบกับการรัน K8s pod เพื่อ host orchestrator ของตัวเองที่ 2-3 vCPU + idle time ก็ประมาณราคาเดียวกัน

Caveat ที่ Vanja (เจ้าของ blog ที่เขียน post อธิบาย feature) ชี้: run ที่ status "completed" ยังอาจมี thread ที่ fail อยู่, agent อาจ spawn thread ซ้ำสำหรับ work ชิ้นเดียวกัน (idempotency ไม่การันตี), budget ตั้งได้แค่ตอน create session เท่านั้น แก้ระหว่าง run ไม่ได้

## ทำไมสำคัญ

ปีที่ผ่านมา orchestration layer ของ agent (LangGraph, Temporal, Dagster, Prefect, CrewAI) แข่งกันหนัก — แต่ส่วนใหญ่ยังต้องให้ user host เอง หรือใช้ managed service ที่คิดเงินแบบ seat/user Anthropic ย้าย orchestration ขึ้นมาเป็น platform feature ที่คิดเงินตาม compute hour คือการแข่งกับทั้ง LangGraph Cloud, Temporal Cloud, และ Replit Agent

Price point $0.08/session-hour เป็นตัวเลขที่น่าสังเกต — ถูกพอให้ long-running agent (เช่น research agent ที่รัน 8-12 ชม.) คุ้มกว่าการ pay-per-request อย่างชัดเจน และถูกกว่า Vertex AI Agent Engine ของ Google ที่ยังคิดเงิน seat-based

**Pattern ที่น่าจับตา**: Anthropic กำลังเดินทางเดียวกับที่ Google เดินด้วย Antigravity (ข่าวเดียวกันสัปดาห์นี้) — คือ model company เริ่มสร้าง opinionated runtime ของตัวเอง แทนที่จะปล่อยให้ user เลือก framework เอง นี่คือการเปลี่ยนจาก "แข่งที่ model quality" ไปที่ "แข่งที่ developer experience + runtime economics"

## มุม AI Agent Platform

สำหรับ **builder** ที่กำลังสร้าง orchestrator ของตัวเอง — ต้องตัดสินใจ **right now** ว่าจะวาง position ตัวเองยังไง: เป็น (1) open-source alternative ที่ user host เอง, (2) multi-model orchestrator ที่ run ได้บน model หลายเจ้า, หรือ (3) vertical-specific orchestrator (เช่น เฉพาะ security agent, data agent) การเล่น "general managed orchestrator" ไปแข่งตรง ๆ กับ Anthropic + Google กำลังเสียเปรียบมากขึ้น

สำหรับ **business ที่ deploy agent** — ถ้า workflow ส่วนใหญ่คือ Claude-based อยู่แล้ว การย้ายไป Dynamic Workflows จะลด infra cost ชัด ถ้าใช้ multi-model (เช่น Claude + GPT + Gemini) ต้องประเมินว่า vendor lock-in คุ้มกับ cost saving ไหม

สำหรับ **ecosystem** การย้าย orchestration ขึ้น platform ของ model vendor คือสัญญาณระยะยาวว่า "unbundled agent stack" (model + framework + orchestrator + memory + tool แยก vendor) อาจไม่ sustain — margin จะไหลไปที่ player ที่ bundle ได้

## Sources
- [Dynamic Workflows Move to the Server](https://vanja.io/managed-agents-dynamic-workflows/)
- [Anthropic Just Launched Managed Agents. Let's Talk About How We're Going to Pay for This](https://www.finout.io/blog/anthropic-just-launched-managed-agents.-lets-talk-about-how-were-going-to-pay-for-this)

---

## Audio script
วันพฤหัสที่ 9 ต.ค. Anthropic ปล่อย dynamic workflows เข้า beta ภายใน Claude Platform สำหรับ Managed Agents หลักการคือ agent เขียน program ไม่ใช่ graph แล้ว server รันให้ ต่างจาก static workflow อย่าง LangGraph หรือ Temporal ที่ต้อง pre-define ล่วงหน้า dynamic workflow ให้ root agent decide ที่ runtime ว่าจะ spawn sub-agent กี่ตัว แต่ละตัวทำอะไร เหมือน fork ของ Unix process

Spec ที่น่าสนใจคือ 64 thread พร้อมกันใน run เดียว 1000 agent ตลอดอายุ run 24 ชั่วโมง lifetime default ราคาคิดแค่ token ตาม rate ของ model เดิม บวก 0.08 ดอลลาร์ต่อ session-hour ไม่มี orchestration fee แยก ซึ่งถ้าเทียบกับการ host K8s pod ของตัวเองก็ประมาณราคาเดียวกัน

ที่สำคัญคือ pattern นี้บอกว่า Anthropic กำลังเดินทางเดียวกับ Google ที่เพิ่งเปิด Antigravity สัปดาห์เดียวกัน คือ model company เริ่มสร้าง opinionated runtime ของตัวเอง แทนที่จะปล่อยให้ user เลือก framework เอง นี่คือการเปลี่ยนจากแข่งที่ model quality ไปที่ developer experience และ runtime economics

สำหรับ builder ที่กำลังสร้าง orchestrator ของตัวเองต้องตัดสินใจตอนนี้ว่าจะวาง position ยังไง เป็น open-source alternative เป็น multi-model orchestrator หรือเป็น vertical specialist เพราะการเล่น general managed orchestrator ไปแข่งตรง ๆ กับ Anthropic กับ Google กำลังเสียเปรียบมากขึ้น สำหรับ business ที่ deploy agent ถ้า workflow ส่วนใหญ่คือ Claude อยู่แล้ว การย้ายไป Dynamic Workflows จะลด infra cost ชัด แต่ถ้าใช้ multi-model ต้องประเมิน vendor lock-in ให้ดี
