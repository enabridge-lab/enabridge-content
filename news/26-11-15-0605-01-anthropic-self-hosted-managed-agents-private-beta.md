---
date: 2026-11-12
slug: anthropic-self-hosted-managed-agents-private-beta
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a sleek enterprise datacenter vault
  stamped "YOUR PERIMETER" with glowing racks labeled "AGENT HARNESS",
  "SANDBOX", "CREDENTIALS", "SESSION HISTORY" lined up inside. A single
  fiber-optic cable arcs out of the vault into a distant cloud marked
  "ANTHROPIC / BEDROCK / FOUNDRY" with the tag "MODEL CALL ONLY". A bold
  three-line counter floats above the scene: "ZERO PUBLIC ENDPOINTS",
  "PRIVATE NETWORK", "BYO COMPUTE". Deep navy and warm orange palette with
  subtle grid, 1:1 aspect, strong contrast for 200px thumbnails, no real
  human faces.
image: images/26-11-15-0605-01-anthropic-self-hosted-managed-agents-private-beta.png
---

# Anthropic เปิด self-hosted Claude Managed Agents private beta — ย้าย agent control plane เข้าไปอยู่ใน perimeter ของลูกค้า

## TL;DR
- 12 พ.ย. 2026 Anthropic เปิด **private beta** ของ **self-hosted Claude Managed Agents** — ลูกค้า run **agent harness, sandbox, credentials, session history** บน cloud/on-prem ของตัวเองได้
- **Model call ยังออกไปข้างนอก** (Anthropic, AWS Bedrock, Google Cloud, Microsoft Foundry เลือกได้) — เป็น "change of address ของ agent service ไม่ใช่ของ model"
- ต้อง **PostgreSQL 16+**, มี beta header `managed-agents-2026-04-01`, ราคาอยู่ที่ account team — ไม่เปิด GA date, ไม่เปิดชื่อลูกค้า beta
- Signal: หลัง UBS / Mintive / Databricks ตลอดปีนี้ **"ของเข้าไปใน perimeter" คือ unlock สุดท้ายของ enterprise agent adoption** — บริษัทไหนไม่ยอมให้ agent harness รันบน cloud vendor จะเป็น segment ที่ Anthropic กับ OpenAI ยอมแลก latency

## เกิดอะไรขึ้น

**12 พ.ย. 2026** ClaudeDevs account ของ Anthropic ประกาศ: **Self-hosted Claude Managed Agents เข้า private beta แล้ว**. โพสต์เดียวในวันนั้นผ่าน 717K views — สะท้อน demand ที่สะสมมาตั้งแต่ Claude Agent SDK เปิด GA ต้นปี

ของที่ลูกค้า host เองได้: **agent harness** (orchestration layer ที่เรียก tool + จัดการ control flow), **sandbox** ที่ agent รัน shell/file operation, **credentials** ที่ agent ใช้เข้าถึง internal system, และ **session history** ทั้งหมด. ลูกค้าต้อง operate server ของ Managed Agents + PostgreSQL 16+ database + worker machines ที่รัน sandbox เอง

จุดสำคัญที่ต้องเข้าใจ: **model call ยังไม่ได้ย้ายเข้า perimeter**. Anthropic ให้ลูกค้าเลือกว่าจะส่ง request ไปที่ Anthropic API, AWS Bedrock, Google Cloud Vertex AI หรือ Microsoft Foundry — แต่ Claude โมเดลยัง serve อยู่ที่ provider เจ้านั้น. Help Net Security และ cellcog.ai สรุปตรงกันว่า **"นี่คือ change of address ของ agent service ไม่ใช่ของ model"**

การเข้าถึง: ติดต่อ Anthropic account team เท่านั้น (ไม่มี self-signup). ทุก endpoint ต้องมี beta header `managed-agents-2026-04-01` แม้ว่า Anthropic SDK จะเติมให้อัตโนมัติ. ราคา **ไม่เปิดสาธารณะ** — quote per deal. ไม่มี GA date, ไม่มี customer reference list

Anthropic ยกตัวอย่าง use case: workload ที่แตะ **internal code และ production system** อย่าง fixing broken build, triaging alert, ops automation — งานที่ enterprise ไม่ยอมให้ agent sandbox รันอยู่ข้าง repo + credential ของตัวเองบน shared cloud ของ vendor อื่น. ก่อนหน้านี้ Anthropic เปิด **self-hosted sandbox** มาก่อน (ไม่ใช่ full control plane) — คราวนี้คือยกระดับให้ครบชุด

## ทำไมสำคัญ

ตั้งแต่ Mintive (ที่เรารายงานเมื่อ 31 ต.ค.) เตือนว่า **"personal agent identity + credential sprawl จะเป็น governance crisis อันดับหนึ่งของ 2027"** และ UBS เปิดตัวเลข **12,700 personal agent** ใน Q3 earnings — ภาพรวมของปีคือ: enterprise กำลังย้าย agent จาก pilot เข้า production **แต่ติดที่ control plane**. ทุก harness, ทุก sandbox, ทุก credential store ที่ vendor เก็บไว้บน cloud ของตัวเอง = **แผล audit, แผล data residency, แผล compliance** ที่ bank / insurer / regulated industry รับไม่ได้

Anthropic เป็น vendor ใหญ่รายแรกที่ยอมให้ **control plane ออกจาก cloud ตัวเอง** — OpenAI ยังไม่ปล่อย self-hosted Agents API (AgentKit visual builder sunset ไป 30 พ.ย.), Google ยัง bundle Gemini Agent Engine กับ Vertex AI. Pattern นี้คล้ายกับที่ GitHub Enterprise Server กับ GitLab self-managed ชนะใจ bank / defense contractor ในยุค DevOps: **"ให้ compute อยู่ในบ้านเรา model ขอเช่า"** เป็น compromise ที่ทำให้สายเข้มงวดที่สุดยอมเดิน

สิ่งที่ยังไม่พิสูจน์: (1) ราคาจะแพงพอที่ Anthropic ยอมให้ GA scale หรือเปล่า — self-hosted software ปกติ margin ต่ำกว่า SaaS หลายเท่า; (2) เมื่อ customer run harness เอง Anthropic จะ ship update ยากขึ้นเท่าไร — Claude Agent SDK ขยับเร็ว, ถ้า customer ค้างที่ version เก่า 6 เดือน จะเกิด fragmentation; (3) latency ของ model call ออก perimeter จะเป็น bottleneck ของ agent loop ที่ต้อง call model หลายรอบต่อ task หรือเปล่า

## มุม AI Agent Platform

สำหรับ **builders** (LangChain ที่เพิ่งระดม $300M, Cresta, Sema4.ai, ทีม internal platform ของ bank): self-hosted Managed Agents เซ็ต **reference architecture ใหม่** — "run harness locally, call model remotely". LangChain Deployments / LangSmith ที่ขายเป็น SaaS ตอนนี้ pressure ต้องมี on-prem edition (Enterprise Server) เร็ว ๆ นี้. ใครขยับช้าจะเสียดีลกับ regulated vertical

สำหรับ **users / business** ที่ deploy agent ใน workflow (bank, insurer, hospital, telco, utility): นี่คือสัญญาณให้ **เปลี่ยน procurement question** จาก "vendor นี้มี SOC 2 / ISO 27001 มั้ย" เป็น **"vendor นี้ให้ harness รันใน VPC ของเราได้มั้ย"**. ถ้ายังไม่ได้ ให้ add clause ใน RFP รอบถัดไป. CISO ที่ไทย/SEA ที่เจอ regulator (BOT, SEC, OIC) ถามเรื่อง AI governance ใน 2027 จะมี **หลักฐานตอบได้ว่า agent runtime อยู่ใน perimeter**

สำหรับ **ecosystem**: AWS, GCP, Azure ได้ประโยชน์ทันที — self-hosted Managed Agents = compute instance เพิ่มบน IaaS ของเขา ไม่ว่า model call จะไปที่ไหน. Postgres managed service (RDS, AlloyDB, Azure Database) ก็ได้. แต่คน **เสีย** คือ pure-SaaS agent vendor ที่ไม่มี on-prem play — ถ้า customer tier 1 require self-hosted ภายใน 2027 ใครไม่มี roadmap on-prem ภายในไตรมาสหน้า จะถูกตัดจาก shortlist

## Sources
- [Operate Claude Managed Agents inside your security perimeter (Anthropic)](https://claude.com/resources/articles/self-hosted-claude-managed-agents)
- [Self-hosted Claude Managed Agents keeps agent credentials in your environment (Help Net Security)](https://www.helpnetsecurity.com/2026/11/12/anthropic-self-hosted-claude-managed-agents/)
- [Anthropic lets companies run Claude's agent service on their own servers (The Next Web)](https://thenextweb.com/news/anthropic-self-hosted-claude-managed-agents)
- [Self-Hosted Claude Managed Agents: Beta, Limits, License (cellcog.ai)](https://cellcog.ai/blog/claude-managed-agents-self-hosted/)

---

## Audio script
วันนี้มีข่าวใหญ่จาก Anthropic ที่น่าจะเปลี่ยน procurement question ของ enterprise agent ไปเลยครับ 12 พฤศจิกายน 2026 Anthropic เปิด private beta ของ self hosted Claude Managed Agents ลูกค้ารัน agent harness รัน sandbox รัน credentials และ session history บน cloud หรือ on prem ของตัวเองได้ทั้งหมด แต่ model call ยังออกไปข้างนอกเลือกได้ว่าจะไป Anthropic AWS Bedrock Google Cloud หรือ Microsoft Foundry มีคนบอกว่านี่คือการย้าย address ของ agent service ไม่ใช่ย้าย address ของ model จุดสำคัญคือหลัง UBS เปิดตัวเลข 12,700 personal agent ใน earnings call แล้ว Mintive เตือนว่า credential sprawl คือ governance crisis อันดับหนึ่งของปี 2027 Anthropic เป็นเจ้าใหญ่รายแรกที่ยอมให้ control plane ออกจาก cloud ตัวเอง OpenAI ยังไม่ปล่อย self hosted Agents API ครับ pattern นี้คล้ายกับ GitHub Enterprise Server ที่ชนะใจ bank กับ defense contractor ในยุค DevOps ให้ compute อยู่ในบ้าน ให้ model เช่า นี่คือ compromise ที่ regulator ยอม สำหรับ CISO ไทย SEA ที่กำลังโดน BOT โดน SEC โดน OIC ถามเรื่อง AI governance ต้องเปลี่ยน procurement question จาก vendor มี SOC 2 มั้ย เป็น vendor ให้ harness รันใน VPC ของเราได้มั้ย ถ้าไม่ได้ให้ add clause ใน RFP รอบถัดไปเลยครับ สำหรับ LangChain Cresta Sema4.ai ที่ขายเป็น SaaS ตอนนี้โดน pressure ต้องมี on prem edition เร็วๆนี้ ส่วนคนที่ได้ประโยชน์ทันทีคือ AWS GCP Azure เพราะ compute instance เพิ่มขึ้น Postgres managed service ก็ได้ด้วย ส่วนคนที่เสียคือ pure SaaS agent vendor ที่ไม่มี on prem play ครับ
