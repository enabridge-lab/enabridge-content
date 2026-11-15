---
date: 2026-11-12
slug: anthropic-self-hosted-managed-agents
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a corporate data center behind a
  tall gate labeled "YOUR PERIMETER". Inside, a glowing cube labeled
  "CLAUDE MANAGED AGENTS" sits on a server rack, wired to three cloud
  logos outside — "BEDROCK", "VERTEX", "FOUNDRY". A sign above reads
  "SELF-HOSTED — PRIVATE BETA" and a small clock below shows "8-HOUR
  SAFETY SLA". Clean editorial style, deep navy and warm orange palette,
  1:1 aspect, no real human faces (silhouettes OK), high contrast so
  labels stay readable at 200px thumbnail.
image: images/26-11-16-0605-02-anthropic-self-hosted-managed-agents.png
---

# Anthropic เปิด Claude Managed Agents ให้ run ใน VPC ลูกค้า — 8 ชม. ต้อง act ถ้าเจอ safety flag

## TL;DR
- 12 พฤศจิกายน Anthropic เปิด private beta ของ self-hosted Claude Managed Agents — ย้ายทั้ง server, DB, worker ไปอยู่ใน data center ลูกค้า
- Model call ยังไปที่ Anthropic / Bedrock / Vertex / Foundry / gateway ของลูกค้าเอง — เลือกได้
- License ข้อเล็กที่สำคัญมาก: ถ้า Anthropic flag safety risk ลูกค้าต้อง act ภายใน 8 ชั่วโมง — ไม่ใช่ typical enterprise SLA

## เกิดอะไรขึ้น
วันที่ 12 พฤศจิกายน Anthropic ประกาศ private beta ของ self-hosted Claude Managed Agents บน blog ของ claude.com — ลูกค้าสามารถเอา Managed Agents service (ที่เดิม Anthropic host เท่านั้น) ไป run ใน cloud account หรือ data center ของตัวเอง เข้าถึงได้ผ่าน account team ยังไม่มี public pricing

ที่ย้ายไปคือ server + database + worker (ที่ agent run shell และ file tools) ส่วนที่ไม่ได้ย้ายคือ model inference เอง — model call ยังออกไปข้างนอก แต่ลูกค้าเลือก endpoint ได้ว่าจะไป Anthropic, AWS Bedrock, Google Cloud, Microsoft Foundry, หรือ gateway ของตัวเอง (สำหรับคนที่มี proxy layer อย่าง LiteLLM หรือ Portkey อยู่แล้ว)

ประเด็น gotcha ที่ The New Stack ชี้คือ licensing clause — Anthropic กำหนดว่าถ้าเจอ safety risk ใน software ของลูกค้า ลูกค้าต้อง act ภายใน 8 ชั่วโมง นี่ไม่ใช่ typical enterprise SLA ที่ให้ 24-72 ชั่วโมง และ Anthropic สงวนสิทธิ์ decide ว่า customer บางรายควร access certain models ผ่าน hosted service เท่านั้น (ไม่ใช่ self-hosted) ด้วยเหตุผล safety ส่วนที่ไม่ได้ migrate คือ webhooks, scheduled runs, และ saved agent — ลูกค้าต้อง rebuild ตั้งแต่ศูนย์

## ทำไมสำคัญ
Move นี้ตอบคำถามที่ CISO ถาม Anthropic มาทั้งปี — "agent ของเรา handle PII และ internal code — ทำไมต้อง run บน server ของคุณ" ก่อนหน้านี้ Anthropic ตอบว่า hosted-only เพราะ safety monitoring ต้องเป็น full-stack ตอนนี้ยอม trade — safety monitoring ลดลงเหลือ model-call level + 8-hour mandatory response window เพื่อให้ enterprise compliance (banks, healthcare, defense) buy ได้

เทียบกับ competitor pattern ที่เห็นกันตอนนี้ — OpenAI ไม่มี self-hosted path ให้ Assistants API หรือ ChatGPT Enterprise agents (ต้องผ่าน Azure); Google เปิด Gemini บน GKE และ Vertex ตั้งแต่ปี 2025 แต่ Agent Development Kit ยัง tightly coupled กับ Google Cloud control plane; Microsoft ให้ Copilot Studio agents run ใน customer tenant แต่ไม่ให้ offline — Anthropic เป็นรายที่ "เปิด box" ที่สุดในกลุ่ม frontier lab ตอนนี้

ข้อสังเกตเชิงธุรกิจ — Anthropic เลือก private beta ไม่ใช่ GA ซึ่งหมายความว่ายังไม่มี pricing (expect premium — self-hosted ของ frontier lab โดยทั่วไปคิด 2-5x ของ hosted) และยังมีคำตามมาว่า "agents and saved data must be rebuilt" — แปลว่าลูกค้าที่ invest เงินกับ hosted Managed Agents ปีนี้ต้อง re-architect ถ้าจะย้าย เป็น signal ว่า Anthropic คาด self-host เป็น enterprise entry — ไม่ใช่ migration path ของลูกค้าเดิม

## มุม AI Agent Platform
Builders — ถ้า product ของคุณขายเข้า regulated industry (finance, healthcare, government) การที่ Anthropic open self-host ทำให้ Claude กลายเป็น viable option สำหรับ customer ที่ก่อนหน้านี้ reject "SaaS only AI" แต่ต้อง weigh — SLA 8 ชั่วโมงหมายความว่า incident response team ต้อง 24/7 coverage ซึ่ง most mid-market company ไม่มี พิจารณา hybrid — ส่วนที่ sensitive run self-hosted, ส่วน dev/test ใช้ hosted ด้วย same codebase

Users/business — สำหรับ CIO ของ bank ไทย ตอนนี้มี path ที่ชัด — Enabridge platform หรือ system integrator สามารถ offer managed deployment ของ Claude Managed Agents บน private cloud ลูกค้า ไม่ต้องรอ Anthropic มีออฟฟิศ APAC คำถามที่ควรถามตอน procurement — ใครรับผิดชอบ safety monitoring (vendor หรือ internal), 8-hour window จะวัดจากเวลาไหน (ส่ง alert หรือ detect), และ fallback plan ถ้า Anthropic ตัดสินใจ pull access

Ecosystem — Bedrock, Vertex, Foundry ได้ประโยชน์เพราะเป็น default model call endpoint — expect ทั้งสาม cloud จะ promote self-hosted Claude เป็น "hybrid AI" offering ร่วมกับ sales team ของตัวเอง AWS re:Invent ปลายเดือนนี้น่าจะมี joint announcement กับ Anthropic — pattern เดียวกับที่ปีก่อน AWS ประกาศ Bedrock Agents + Anthropic ตอน re:Invent 2024 — timing เลยไม่น่าจะบังเอิญ

## Sources
- [Operate Claude Managed Agents inside your security perimeter (Anthropic)](https://claude.com/resources/articles/self-hosted-claude-managed-agents)
- [Anthropic now lets you self-host Claude Managed Agents. The catch? 8 hours to act (The New Stack)](https://thenewstack.io/self-hosted-claude-managed-agents/)
- [Anthropic Lets Customers Self-Host Claude Managed Agents (Unite.AI)](https://www.unite.ai/anthropic-lets-customers-self-host-claude-managed-agents/)
- [Self-hosted Claude Managed Agents keeps agent credentials in your environment (Help Net Security)](https://www.helpnetsecurity.com/2026/11/12/anthropic-self-hosted-claude-managed-agents/)

---

## Audio script
วันที่ 12 พฤศจิกายน Anthropic ประกาศ private beta ของ self-hosted Claude Managed Agents ให้ลูกค้าเอา managed agents service ไป run ใน data center หรือ cloud ของตัวเอง ส่วนที่ย้ายคือ server, database, และ worker ที่ agent run shell กับ file tools ส่วนที่ไม่ได้ย้ายคือ model inference เอง — model call ยังออกไปข้างนอก แต่ลูกค้าเลือก endpoint ได้ว่าจะไป Anthropic, AWS Bedrock, Google Cloud, Microsoft Foundry, หรือ gateway ของตัวเอง ประเด็น gotcha ที่สำคัญคือ license clause — ถ้า Anthropic ตรวจพบ safety risk ใน software ของลูกค้า ลูกค้าต้อง act ภายใน 8 ชั่วโมง ซึ่งไม่ใช่ typical SLA ของ enterprise ที่ปกติให้ 24 ถึง 72 ชั่วโมง move นี้ตอบคำถามที่ CISO ถามมาทั้งปี — agent ของเรา handle PII และ internal code ทำไมต้อง run บน server ของคุณ เทียบกับ competitor OpenAI ยังไม่มี self-hosted path, Google มีแต่ tightly coupled กับ Google Cloud, Microsoft Copilot Studio ให้ run ใน tenant แต่ไม่ให้ offline — Anthropic เปิด box ที่สุดในกลุ่ม frontier lab ตอนนี้ สำหรับ builder ที่ขายเข้า regulated industry อย่างธนาคารหรือ healthcare การที่ Claude run self-hosted ได้ ทำให้มันเป็น option ที่ customer ที่ก่อนหน้านี้ reject SaaS only AI พิจารณาใหม่ได้ สำหรับ CIO ธนาคารไทยตอนนี้มี path ที่ชัด system integrator หรือ platform อย่าง Enabridge offer managed deployment ของ Claude Managed Agents บน private cloud ลูกค้า ไม่ต้องรอ Anthropic มีออฟฟิศ APAC สิ่งที่ต้องถามคือใครรับผิดชอบ safety monitoring และ 8 ชั่วโมงเริ่มนับจากตอนไหน
