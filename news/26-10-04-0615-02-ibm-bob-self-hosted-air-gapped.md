---
date: 2026-10-04
slug: ibm-bob-self-hosted-air-gapped
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a fortified bank vault labeled "ON-PREM"
  with a glowing IBM robot icon named "BOB" inside, surrounded by a dashed
  perimeter stamped "AIR-GAPPED". A stock ticker overhead flashes "IBM +5%"
  in neon green. Two model badges hang on the vault door — "NVIDIA NEMOTRON"
  and "POOLSIDE LAGUNA". Code streams in through isolated conduits. Cinematic
  cobalt-blue and gold palette, bold text rendering for 200px thumbnails, no
  real human faces, 1:1 aspect. Style of a Bloomberg Businessweek cover.
image: images/26-10-04-0615-02-ibm-bob-self-hosted-air-gapped.png
---

# IBM เปิด Bob แบบ self-hosted — air-gapped coding agent สำหรับ regulated enterprise, หุ้นเด้ง 5%

## TL;DR
- 1 ต.ค. IBM ประกาศ **self-hosted deployment ของ IBM Bob** — agentic software development platform; รันบน on-prem, private cloud, sovereign cloud, air-gapped network โดยไม่ต้องส่งโค้ดออก
- Model ที่ซัพพอร์ตบน customer infra: **NVIDIA Nemotron** และ **Poolside Laguna**; รัน Red Hat OpenShift GA ตั้งแต่ 24 ก.ย.
- **IBM เด้ง 4-5% pre-market** วันประกาศ; target banking, government, healthcare — อุตสาหกรรมที่ไม่ยอมส่ง source code เข้า cloud ของ vendor

## เกิดอะไรขึ้น
วันที่ 1 ตุลาคม IBM ประกาศ **self-hosted deployment สำหรับ IBM Bob** — agentic software development platform ที่ IBM เปิดตัวครั้งแรกเมษายน 2026 แบบ multi-agent system ที่จัดการ full software lifecycle: planning การเปลี่ยนแปลง, เขียนโค้ด, test, deploy, และ modernize legacy Java/COBOL/PL/I/RPG. ตัว self-hosted option รันบน **Red Hat OpenShift** ซึ่ง GA ไปแล้วตั้งแต่ 24 ก.ย., เก็บ core capability ไว้ครบ — BobShell IDE, parallel tool calling, skills, operating modes — แต่ย้ายกล่องมาอยู่ใน data center ของลูกค้า.

Model ที่รองรับบน customer infrastructure ตอนนี้คือ **NVIDIA Nemotron** และ **Poolside Laguna** — สอง model ที่ fine-tune สำหรับ coding โดยเฉพาะ, บวก BYOL (bring-your-own-license) สำหรับ model อื่นใน IBM's supported list. ตัวอย่างที่ IBM ยกใน press release ชัดและคม: ธนาคารแห่งหนึ่งใช้ local model process core banking software แต่ connect ไป approved external service สำหรับงานที่ regulate น้อยกว่า. Flexibility แบบนี้ตรงกับความต้องการของ financial services, government, healthcare, critical infrastructure และ enterprise ที่ปกป้อง IP + proprietary business logic.

ตลาดตอบรับ **ภายในชั่วโมงแรก IBM shares พุ่ง 4-5% pre-market** วันที่ 1 ต.ค. ตามด้วย Salesforce +3% และ Palantir บวกเล็กน้อย — pattern ของ regulated enterprise AI play ที่นักลงทุนเริ่มราคาเข้า. IBM เลือก timing ที่ Oracle, SAP, และ Palantir ก็กำลังขับเคลื่อน "sovereign AI" narrative ของตัวเอง.

## ทำไมสำคัญ
ประเด็นใหญ่ไม่ใช่ coding agent — Claude Code, Cursor, Windsurf ทำได้ดีกว่า Bob ในหลาย benchmark. ประเด็นใหญ่คือ **การยอมรับว่า cloud-only AI model สูญเสียลูกค้า regulated**. ตลอด 18 เดือนที่ผ่านมา GitHub Copilot, Cursor, Claude Code เติบโตเร็วมากกับ startup + mid-market tech แต่ชนกำแพงที่ bank, defense, government — เพราะ compliance team บอกว่า source code ออกจาก network ไม่ได้. IBM เลือกเล่น gap นี้โดยตรง: ไม่สู้ frontier capability แต่สู้ **deployment flexibility**.

Pattern นี้สะท้อนสิ่งที่ **Anthropic ทำกับ Claude Enterprise** (private deployment via Bedrock/Vertex) และ **OpenAI กับ Azure Government** — แต่ IBM ไปไกลที่สุดด้วย air-gapped mode ที่ไม่ต้อง network connection เลย. Nvidia Nemotron + Poolside Laguna ที่เป็น partner model ด้วย signal ว่า **frontier coding model จะ commoditize เร็ว** — ไม่ใช่ Anthropic/OpenAI เท่านั้นที่ทำได้ และ enterprise จะเริ่มเลือก model จาก deployment constraint ก่อน capability.

## มุม AI Agent Platform
สำหรับ **Builders** agent platform/framework: self-hosted mode จาก backbone infrastructure ตอนนี้คือ table stakes สำหรับ enterprise GTM — ถ้า framework ของคุณบังคับ cloud SaaS หรือต้องเรียก upstream API ตลอดเวลา บัญชี Fortune 500 ครึ่งหนึ่งจะตัดจาก shortlist. ให้วางแผน air-gapped mode ใน Q1 2027 roadmap. สำหรับ **Users / business** ใน regulated industry: Bob เปิดทางเลือกใหม่ที่ไม่ต้องรอ Microsoft/Google ทำ sovereign tier — pilot ภายใน 90 วันเพื่อลด dependency บน vendor เดียว. สำหรับ **Ecosystem**: NVIDIA ชนะเพิ่มเพราะ Nemotron ขึ้นเป็น default model ของ Bob self-hosted = GPU demand ขยาย; Poolside ได้ enterprise distribution channel ที่ตัวเองสร้างเองไม่ได้; Snyk/Checkmarx/Veracode จะเจอ wave ของ "AI-generated code security scan" workload เพิ่มขึ้นมากจากลูกค้า bank/government ที่เริ่มใช้.

## Sources
- [IBM Introduces Self-Hosted Deployment for IBM Bob (IBM Newsroom)](https://newsroom.ibm.com/2026-10-01-ibm-introduces-self-hosted-deployment-for-ibm-bob-to-help-enterprises-advance-ai-sovereignty-and-governance)
- [IBM allows on-prem deployment of its Bob agentic development platform (SiliconANGLE)](https://siliconangle.com/2026/10/01/ibm-allows-on-prem-deployment-of-its-bob-agentic-development-platform/)
- [IBM Brings Bob to Self-Hosted and Air-Gapped Environments (MarkTechPost)](https://www.marktechpost.com/2026/10/02/ibm-brings-bob-to-self-hosted-and-air-gapped-environments/)
- [IBM Jumps 5% as Bob Coding Agent Gains Self-Hosted Deployment (24/7 Wall St.)](https://247wallst.com/investing/2026/10/01/ibm-jumps-5-as-bob-coding-agent-gains-self-hosted-deployment-salesforce-rises-3-palantir-inches-higher/)

---

## Audio script
วันที่ 1 ตุลาคม IBM ประกาศ self-hosted deployment สำหรับ IBM Bob — agentic software development platform ที่เปิดตัวครั้งแรกเมษายน 2026 สำหรับ full software lifecycle ตั้งแต่ planning เขียนโค้ด test deploy ไปจนถึง modernize legacy Java COBOL PL/I RPG. ตัว self-hosted option รันบน Red Hat OpenShift ซึ่ง GA ไปแล้ว 24 กันยายน และ model ที่ซัพพอร์ตบน customer infrastructure คือ NVIDIA Nemotron และ Poolside Laguna บวก BYOL สำหรับ model อื่น. ตัวอย่างที่ IBM ยกชัดมาก คือธนาคารใช้ local model process core banking แต่ connect ไป approved external service สำหรับงานที่ regulate น้อยกว่า. ตลาดตอบรับทันที หุ้น IBM บวก 4-5% ใน pre-market. ประเด็นสำคัญคือ IBM ไม่ได้สู้ frontier capability กับ Claude Code หรือ Cursor แต่สู้ที่ deployment flexibility เพื่อเจาะลูกค้า bank government healthcare ที่ไม่ยอมส่งโค้ดเข้า cloud ของ vendor. สำหรับทีมที่ทำ agent framework self-hosted mode ตอนนี้คือ table stakes ของ enterprise GTM ถ้าบังคับ cloud SaaS อย่างเดียวบัญชี Fortune 500 ครึ่งหนึ่งจะตัดคุณจาก shortlist ทันที.
