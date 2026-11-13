---
date: 2026-11-14
slug: anthropic-self-hosted-managed-agents
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a sleek enterprise data center with
  thick glass walls. Inside, three server racks are labeled "MANAGED AGENTS
  SERVER", "POSTGRES", and "WORKER SANDBOX". A vault door on the front reads
  "YOUR INFRA". Three stacked numbers float above: "ZERO PUBLIC ENDPOINTS",
  "PRIVATE NETWORK", "BYO COMPUTE". Outside the vault, a thin bridge labeled
  "MODEL INFERENCE" extends toward a distant Anthropic cloud icon, with small
  tags "BEDROCK" and "VERTEX" marking alternate routes. Editorial style, deep
  navy and warm orange palette, high contrast so labels stay readable at
  200px, 1:1 aspect, no real human faces.
image: images/26-11-14-0605-02-anthropic-self-hosted-managed-agents.png
---

# Anthropic เปิดให้ enterprise รัน Claude Managed Agents บน server ตัวเอง — regulated industries unlock

## TL;DR
- Anthropic เปิด private beta ของ Claude Managed Agents แบบ self-hosted (12 พฤศจิกายน) — ลูกค้ารัน server + Postgres + worker sandbox บน infra ตัวเอง
- Model inference ยัง default ไปที่ Anthropic API แต่ redirect ไป Amazon Bedrock, Google Vertex, Microsoft Foundry หรือ custom gateway ได้ — แปลว่า control plane แยกจาก model vendor
- เป้า segment ชัด — banking, insurance, healthcare, public sector ที่ไม่สามารถส่ง agent state + customer PII ออก network ของตัวเองได้

## เกิดอะไรขึ้น
วันที่ 12 พฤศจิกายน Anthropic เปิด private beta ของ Claude Managed Agents แบบ self-hosted หลังจาก public beta ของ self-hosted sandboxes ไปก่อนช่วง Q3 ครั้งนี้ย้าย control plane ทั้งหมดเข้าไปในของลูกค้า — server ของ Managed Agents, PostgreSQL database ที่เก็บ agent state และ workers ที่รัน shell + file tools ทั้งหมดอยู่บน VPC ของลูกค้า Anthropic เป็นคนติดตั้งและดูแล security ของแต่ละ release แต่ไม่เข้าถึง data

ที่น่าสนใจคือ model inference ยังไม่ self-hosted — default inference.provider ยังตั้งเป็น anthropic คือยิงไปที่ API ของ Anthropic แต่ customer สามารถสลับไปใช้ Amazon Bedrock, Google Cloud Vertex, Microsoft Foundry หรือ gateway ของตัวเองได้ แปลว่าในทางปฏิบัติ "self-hosted" ของ Managed Agents = control plane + state + tool execution อยู่ใน VPC ของลูกค้า แต่ model call ยังออก network ไปที่ provider ของ model

Access ยังปิด — ต้องติดต่อ account team ของ Anthropic เพื่อขอ early access และมี feature gap ที่สำคัญ: webhooks และ scheduled runs ยังไม่ port มา และ data จาก hosted service ไม่ migrate ให้ ต้อง rebuild agent + saved data ใหม่ ซึ่ง signal ว่า Anthropic ตั้งใจให้ customer ย้ายอย่างตั้งใจ ไม่ใช่ auto-migration ทั้งหมด

Anthropic ประกาศนี้คู่กับ MCP tunnels ที่อยู่ใน research preview — เป็น way ให้ agent ใน self-hosted environment เรียก MCP server ภายนอกได้โดยไม่ต้องเปิด public endpoint สำหรับ regulated industry ที่ network policy ห้าม inbound traffic จาก internet นี่คือตัวที่รอมาทั้งปี

## ทำไมสำคัญ
ตลาด enterprise agent มี bottleneck ที่พูดกันน้อย — ไม่ใช่ model quality หรือ price ต่อ token แต่เป็น "agent state ควรอยู่ที่ไหน" ธนาคารใหญ่ของสหรัฐบอก consulting partner ว่าอยากใช้ Claude แต่ตอน POC ต้อง route data ทั้งหมดออก network ของตัวเองซึ่งผิด policy — คนที่เคยติด GDPR และ EU AI Act ของยุโรปเข้าใจความเจ็บปวดนี้ดี การที่ Anthropic ยอมเปิด self-hosted control plane คือการยอมรับว่า "Anthropic own model, customer own agent"

เทียบกับคู่แข่ง — OpenAI ยังไม่ให้ self-host Managed Agents (Assistants API ของ OpenAI ก็ cloud-only) Google ให้ build agent บน Vertex AI ซึ่งอยู่ใน Google Cloud แต่ไม่ให้ run ใน on-prem AWS Bedrock ให้ model แต่ไม่มี managed agent service เป็นของตัวเอง นั่นแปลว่าสำหรับ regulated industry ตอนนี้ Anthropic เป็นรายเดียวที่ให้ control plane อยู่ในมือลูกค้าโดยไม่ต้อง build runtime เอง

Caveat — private beta แปลว่ายังไม่ scale, feature incomplete และตอน rebuild agent + data จาก hosted service ต้องใช้ engineering team ของลูกค้า ไม่ใช่ click-to-migrate แต่สำหรับธนาคารใหญ่ที่มีทีม 50-100 คนทำ AI platform อยู่แล้ว ค่าเสียเวลา migration คุ้มกับการ unblock project ที่ค้างมา 6-12 เดือน

## มุม AI Agent Platform
Builders — ถ้ากำลังสร้าง agent framework ที่ขาย enterprise ให้คิดถึง deployment model ตั้งแต่ต้น — managed, self-hosted, hybrid เป็นสามชั้นที่ลูกค้าแต่ละกลุ่มต้องการ Anthropic ใช้เวลา 2 ปีกว่าจะเปิด self-hosted — ถ้าเริ่มต้นวันแรกจะย่น cycle ไป คำแนะนำ: แยก control plane กับ model inference เป็น service ที่ port ได้ ไม่ bundle กับ vendor ใด vendor หนึ่ง

Users/business — enterprise ที่อยู่ในกลุ่ม regulated (banking, insurance, healthcare, government, large utilities) ควร re-evaluate agent roadmap ตอนนี้ — bottleneck "ส่ง data ออกไม่ได้" ที่เคยเป็นเหตุผลให้ไม่ทำ อาจจะไม่ใช่ blocker อีกต่อไป คำถามใหม่คือ internal team พร้อมดูแล Postgres + sandbox cluster ไหม ถ้าไม่ ควรจ้าง managed service provider (เช่น consulting firm หรือ systems integrator) ไม่ใช่ build เอง ลูกค้าไทยกลุ่มธนาคาร, บริษัทประกัน, โรงพยาบาลเอกชน ที่ Enabridge ดูแล — อันนี้คือโอกาสเปิด conversation ใหม่

Ecosystem — Microsoft Foundry และ Google Vertex ถูก list เป็น provider ทาง alternative — Anthropic กำลังเดิมพันว่า "control plane neutral + model agnostic" คือ winning configuration อนาคตเราอาจเห็น Managed Agents server รันบน Azure กับ model มาจาก Bedrock ซึ่งเป็น hybrid ที่คนไม่เคยคิด แต่สำหรับลูกค้าที่มี commitment หลาย cloud (ซึ่งเป็น reality ของ enterprise ส่วนใหญ่) นี่คือ flexibility ที่สำคัญมาก

## Sources
- [Claude Managed Agents overview (Anthropic docs)](https://platform.claude.com/docs/en/managed-agents/overview)
- [New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels (Anthropic blog)](https://claude.com/blog/claude-managed-agents-updates)
- [Anthropic lets companies run Claude's agent service on their own servers (TheNextWeb)](https://thenextweb.com/news/anthropic-self-hosted-claude-managed-agents)
- [Anthropic Lets Enterprises Self-Host the Claude Agent Control Plane (AlphaSignal)](https://alphasignal.ai/news/anthropic-lets-enterprises-self-host-the-claude-agent-control-plane)

---

## Audio script
วันที่ 12 พฤศจิกายน Anthropic เปิด private beta ของ Claude Managed Agents แบบ self-hosted หลังจากที่ก่อนหน้านี้เปิดแค่ self-hosted sandboxes แบบ public beta ครั้งนี้ย้าย control plane ทั้งหมดเข้าไปในของลูกค้า server ของ Managed Agents, PostgreSQL ที่เก็บ agent state และ workers ที่รัน shell กับ file tools ทั้งหมดอยู่บน VPC ของลูกค้าเอง Anthropic เป็นคนติดตั้งและดูแล security ของ release แต่ไม่เข้าถึง data model inference ยัง default ไปที่ Anthropic API แต่ลูกค้าสามารถสลับไปใช้ Amazon Bedrock, Google Vertex, Microsoft Foundry หรือ gateway ของตัวเองได้ สิ่งที่สำคัญคือ ตลาด enterprise agent มี bottleneck ที่พูดกันน้อย ไม่ใช่ model quality หรือราคาต่อ token แต่เป็นคำถามว่า agent state ควรอยู่ที่ไหน ธนาคารใหญ่กับบริษัทประกันที่เจอ GDPR, EU AI Act หรือ regulation ของแต่ละประเทศเข้าใจความเจ็บปวดนี้ดี Anthropic ยอมเปิด self-hosted control plane คือการยอมรับว่า Anthropic เป็นเจ้าของ model แต่ customer เป็นเจ้าของ agent เทียบกับคู่แข่ง OpenAI ยังไม่ให้ self-host Managed Agents, Google ให้ build agent บน Vertex แต่ไม่ให้รัน on-prem, AWS Bedrock ให้ model แต่ไม่มี managed agent service แปลว่าสำหรับ regulated industry ตอนนี้ Anthropic เป็นรายเดียวที่ให้ control plane อยู่ในมือลูกค้า สำหรับทีมที่สร้าง agent platform ควรแยก control plane กับ model inference ตั้งแต่ต้น สำหรับลูกค้าไทยกลุ่มธนาคาร ประกัน โรงพยาบาลเอกชน นี่คือโอกาสเปิด conversation ใหม่
