---
date: 2026-08-10
slug: aws-agentcore-runtime-14-days-ga
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  A sleek datacenter server rack labeled "AGENTCORE RUNTIME INSTANCES" with a
  glowing hourglass on top; two stacked numeric badges read
  "SESSION LIMIT: 14 DAYS" and "OLD: 8 HOURS" struck-through in red.
  AWS logo on the rack door, GPU cards visible through side panel.
  Editorial isometric style, orange and slate-blue palette, 1:1 aspect, no real
  human faces.
image: images/26-08-11-0616-03-aws-agentcore-runtime-14-days-ga.png
---

# AWS Bedrock AgentCore ยิง Runtime Instances GA — session ยืดจาก 8 ชม. เป็น 14 วัน

## TL;DR
- AWS ประกาศ AgentCore Runtime Instances GA เมื่อ 6 สิงหาคม — persistent EC2-backed runtime สำหรับ agent ที่รันนาน
- Session limit 14 วัน (จาก 8 ชั่วโมง ของ serverless microVM), รองรับ GPU, memory-optimized, compute-optimized instance types
- Deploy 9 region (US, EU, APAC 5 เมือง), pricing = EC2 standard + management fee ของ AgentCore

## เกิดอะไรขึ้น
AWS ปิด gap สำคัญที่ agent-first startup บ่นมาตลอดปี — เมื่อ 6 สิงหาคม Bedrock AgentCore ประกาศ Runtime Instances เข้าสถานะ GA ของเดิม AgentCore Runtime รันบน microVM serverless ซึ่ง session cap ที่ 8 ชั่วโมง เหมาะกับ agent สั้น ๆ ที่จบใน one shot แต่ agent ที่ต้องทำงานหลายวัน — อย่าง cybersecurity monitoring ที่คอย watch traffic, data analytics ที่ scan warehouse ทั้งคืน, หรือ SDR agent ที่ orchestrate outreach ต่อเนื่อง — เดิมทำไม่ได้บน AgentCore

Runtime Instances ย้าย workload ไปรันบน EC2 จริง (AWS manage patching และ lifecycle เอง) — session ยืดเป็น **14 วัน**, รองรับ GPU accelerated instance type สำหรับ workload ที่ต้อง embedding/inference ใน loop, session stop/restart ประหยัด cost ตอน idle, และหลาย agent อยู่ใน host เดียวกัน share session ได้ (multi-agent collaboration แบบ synchronous)

Pricing model น่าสังเกต: AWS ไม่ได้คิด markup ก้อนใหญ่ — เก็บ EC2 standard rate + management fee (ยังไม่ประกาศตัวเลข) จุดนี้ต่างจากคู่แข่งอย่าง LangSmith หรือ Braintrust ที่ค่าตัวคนละคิดผ่าน per-trace pricing ที่บวมเมื่อ agent รันหลายวัน — ลูกค้าที่ทำ math เจอว่า AWS ถูกกว่า 2-3x เมื่อ session ยาว

## ทำไมสำคัญ
Signal ใหญ่ที่สุด: ตลาด agent runtime **แยกออกเป็นสองประเภทชัดเจน** — short-horizon (chatbot, form filling, tool call chain) ที่ยัง serverless พอ vs long-horizon (monitoring, orchestration, autonomous SDR) ที่ต้อง persistent compute — และ AWS เป็นเจ้าแรกใน 3 hyperscaler ที่ ship product แยกให้ทั้งสองแบบ Google Cloud มี Vertex AI Agent Builder แต่ยังไม่มี long-session equivalent, Azure ยังโฟกัสที่ Foundry Agent Service ที่คล้าย serverless microVM

Signal ที่สอง: 14 วันเป็นเลขที่ **ตั้งใจ** — cover use case ที่ตลาด agent-first infrastructure company (Sail Research, LangSmith, Braintrust) เน้นขาย AWS เลือกจะ commoditize layer นี้ ไม่ปล่อยให้ third-party เก็บ margin แบบ pure infra AWS ที่มีทุกอย่างในมือ (EC2, S3, IAM, VPC) push agent runtime เข้าเป็น "just another EC2 workload" ที่ security/IAM/billing เหมือน service อื่น ๆ ที่ enterprise ใช้อยู่แล้ว

Timing สอดคล้องกับ Sail Research ที่เพิ่งระดม $80M เดือน June สำหรับ "long-horizon agent infrastructure" — ตอนนั้น pitch คือ "AWS ไม่มี" ตอนนี้ pitch นั้นตายแล้ว Sail ต้อง defend ที่ efficiency (บอกว่าถูกกว่า proprietary 12x) เท่านั้น ซึ่งทำได้ยากเพราะ AWS มี volume discount ที่ผู้เริ่มใหม่แข่งไม่ได้

## มุม AI Agent Platform
สำหรับ **builders**: ถ้าทำ agent framework ที่ควบคุม session lifecycle เอง (Temporal-style, durable execution) การ ship บน AgentCore Runtime Instances จะเป็น distribution channel ที่เข้า enterprise ง่ายกว่าตั้ง SaaS ของตัวเอง — เพราะ enterprise ที่ใช้ AWS อยู่ compliance/IAM ผ่านแล้ว สำหรับ **users/business** ที่ deploy agent: workload ที่เดิมต้อง hack ด้วย cron + external state store ตอนนี้ทำใน AgentCore ตรง ๆ ได้ — เช่น weekly reconciliation, month-end close, always-on fraud watch ทีมที่ทำ agent PoC ที่ crash ทุก 8 ชั่วโมงเพราะ session limit จะไม่ต้องออกแบบ workaround แล้ว

สำหรับ **ecosystem/vendor**: LangSmith, LangGraph Cloud, Braintrust, Arize, Weights & Biases — ทุก observability/orchestration vendor ต้อง reprice per-trace model ถ้า AWS charge เพียง EC2 fee flat ที่ predictable margin เดิม 40-50% จะบีบลงเยอะ Anthropic กับ OpenAI ที่ยังไม่มี agent hosting ของตัวเอง จะยอมให้ AWS commoditize layer นี้ต่อ หรือ ship product แข่ง — คำถามนี้จะเห็นคำตอบใน Q4

## Sources
- [Runtime instances: persistent compute for production AI agents (AWS Blog)](https://aws.amazon.com/blogs/aws/runtime-instances-persistent-compute-for-production-ai-agents-on-amazon-bedrock-agentcore/)
- [AgentCore runtime instances are now generally available (AWS What's New)](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/)
- [Amazon launches runtime instances for Bedrock agents (SecurityBrief)](https://securitybrief.com.au/story/amazon-launches-runtime-instances-for-bedrock-agents)

---

## Audio script
AWS เพิ่งประกาศ AgentCore Runtime Instances เข้าสถานะ GA ครับ ประเด็นสำคัญคือ session ของ agent ยืดจาก 8 ชั่วโมงเดิมเป็น 14 วัน ทำไมสำคัญ agent สั้น ๆ อย่าง chatbot รันบน serverless microVM ก็พอ แต่ agent ที่ทำงานหลายวัน อย่าง monitoring cybersecurity SDR ที่ orchestrate outreach warehouse scan รอบ overnight เดิมทำไม่ได้ AWS ย้ายไปรันบน EC2 จริง manage patching ให้เอง รองรับ GPU stop/restart ประหยัดตอน idle Pricing ก็คือ EC2 rate ปกติบวก management fee — ไม่มี markup ก้อนใหญ่ ประเด็นที่จะกระทบตลาดคือ AWS commoditize layer นี้ไปเลย บริษัทที่ pitch long-horizon agent infrastructure อย่าง Sail Research ที่เพิ่งระดม 80 ล้านเดือน June จะต้อง defend ที่ efficiency มากขึ้น สำหรับคนที่ deploy agent อยู่ workload ที่เคย crash ทุก 8 ชั่วโมง ไม่ต้องออกแบบ workaround แล้ว สำหรับ observability vendor ทุกเจ้า LangSmith Braintrust Arize ต้อง reprice per-trace model ถ้า AWS charge เพียง flat EC2 fee
