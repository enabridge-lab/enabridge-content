---
date: 2026-08-20
slug: a2a-protocol-agentic-ai-foundation-multi-agent-standard
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  Editorial isometric illustration of a marble town-square labeled
  "AGENTIC AI FOUNDATION"; five stone pillars in a semicircle stamped
  with logos (Google, Microsoft, AWS, Cisco, Salesforce); a fresh new
  pillar being lowered into place labeled "A2A PROTOCOL"; small robot
  agents crossing between the pillars along glowing lines of dialogue
  arrows; three floating numbers stack above: "150+ ORGS",
  "250+ MEMBERS", "1 YEAR OLD"; magazine editorial style, thick outlines,
  high contrast, readable at 200px thumbnail, 1:1 aspect,
  no real human faces.
image: images/26-08-20-0612-03-a2a-protocol-agentic-ai-foundation-multi-agent-standard.png
---

# A2A ย้ายบ้านเข้า Agentic AI Foundation — Google ปล่อยมือ, มาตรฐาน multi-agent มี governance ใหม่ 150+ องค์กร

## TL;DR
- **17 ส.ค. 2026** — **Agent2Agent (A2A) Protocol** ที่ Google บริจาคให้ **Linux Foundation** เมื่อมิถุนายน 2025 ย้ายเข้าไปเป็น hosted project ของ **Agentic AI Foundation (AAIF)** — sub-foundation เฉพาะทาง agent
- A2A ปีเดียวโต **จาก <40 → 250+ members**, ครอบ **AWS, Cisco, Google, Microsoft, Salesforce, SAP, ServiceNow**, มี **enterprise production use** จริงในหลาย cloud
- นี่คือ **protocol war** ที่ resolve ลง: MCP (Anthropic, ตอนนี้ Linux/AAIF ดูแล) เป็น **agent ↔ tool**, A2A เป็น **agent ↔ agent** — 2 protocol แยกงานกันแล้ว
- Signal ใหญ่: **hyperscaler 3 ราย (AWS/Microsoft/Google) นั่งโต๊ะเดียวกันในเรื่อง multi-agent standard** — เกิดขึ้นครั้งแรกที่ครบทั้ง 3

## เกิดอะไรขึ้น
วันที่ 17 สิงหาคม 2026 **Axios** รายงานว่า **Google's Agent2Agent Protocol (A2A)** ย้ายเข้าไปเป็น **hosted project ของ Agentic AI Foundation** — sub-foundation ภายใต้ Linux Foundation ที่โฟกัส agentic AI โดยเฉพาะ. ตัว AAIF เพิ่งเปิดตัวเมื่อธันวาคม 2025 และในเวลา 8 เดือนโตจาก **<40 → 250+ members**, มี Google, Microsoft, Amazon, Anthropic, OpenAI, Bloomberg, Shopify, Block เป็น key backers

A2A ถือกำเนิดโดย Google เมษายน 2025 ในฐานะ open protocol สำหรับให้ **agent จากหลาย vendor สื่อสารกันได้แบบ secure + discoverable** — เดิมทีอยู่ใต้ Linux Foundation ตั้งแต่มิถุนายน 2025 หลัง Google donate spec + SDK ให้ vendor-neutral governance. ในหนึ่งปีโตจาก **~100 องค์กร → 150+ องค์กร** และมี AWS, Cisco, Google, Microsoft, Salesforce, SAP, ServiceNow เป็นผู้ร่วมก่อตั้งโครงการภายใต้ AAIF, พร้อม **enterprise production use** จริงในหลาย cloud platform (Vertex, Azure AI Foundry, AWS Bedrock)

การย้ายบ้านครั้งนี้สำคัญเชิง governance: **Linux Foundation portfolio ใหญ่มาก** — จาก Kubernetes ถึง PyTorch — และ A2A เป็นแค่ 1 ใน 100+ project. **AAIF เป็นบ้านที่ focused** — มี MCP (2026-07-28 spec ที่เพิ่งอัปเดตใหญ่), มี A2A, และ (คาดว่า) protocol อื่น ๆ ในสาย agent จะตามมา. Anthropic, Microsoft, OpenAI, Google, Amazon อยู่ใน MCP core maintainer group อยู่แล้ว — ตอนนี้ก็อยู่ใน A2A ด้วย

## ทำไมสำคัญ
**"Protocol war"** ที่ปีที่แล้วยังคลุมเครือ ตอนนี้ resolve ลงเป็น **2 layer ที่แยกงานกันชัด**: **MCP = agent ↔ tool/data** (bring context to model), **A2A = agent ↔ agent** (peer coordination). ทั้ง 2 protocol อยู่บ้านเดียว governance เดียว spec compatible กัน — เท่ากับ **stack กลาง** สำหรับ multi-agent system มีคำตอบเชิง architecture ที่ทุก vendor ยอม compromise แล้ว. เทียบกับ 12 เดือนก่อนที่ทุกคนพยายาม push standard ของตัวเอง (Salesforce Agentforce ACP, Microsoft Copilot agent bus, LangChain agent-protocol), ก้าวนี้เห็นชัดว่าตลาด **converge** แล้ว

Signal ที่ควรอ่านให้ออกคือ **hyperscaler 3 ราย + big enterprise vendor นั่งโต๊ะเดียวกัน** — เกิดขึ้นน้อยมากในประวัติศาสตร์ standard body. เทียบเคียงได้กับตอน CNCF ทำให้ Kubernetes ชนะ Docker Swarm/Mesos ในปี 2017-2018, protocol layer สำหรับ agent-to-agent ที่ vendor-neutral เป็น **prerequisite** สำหรับ multi-agent world ที่ tick-agent จาก Google คุยกับ order-agent จาก Salesforce ที่คุยกับ payment-agent จาก Stripe ได้โดยไม่มี custom integration

ที่น่าจับตาคือ **enterprise production use** — เพราะ standard ที่ไม่มีคนใช้จริงคือกระดาษ. Rest of A2A story ปีหน้าคือ **who ships first inter-vendor agent workflow ที่ทำงานได้ใน prod scale** — คาดว่า Salesforce ↔ ServiceNow ↔ Microsoft Copilot จะเป็น showcase แรก เพราะทั้ง 3 มี installed base ที่แค่เชื่อม A2A ตรงกันก็ปลด value ทันที

## มุม AI Agent Platform
สำหรับ **Builders** ที่กำลังสร้าง agent framework/orchestration: ต้อง **implement ทั้ง MCP + A2A** เป็น first-class citizen — ไม่ใช่ optional adapter. Framework ที่พยายาม push protocol ของตัวเอง (custom RPC, proprietary agent bus) กำลังจะกลายเป็นข้อเสียหลังปีนี้. LangGraph, CrewAI, AutoGen, Microsoft AutoGen — ทั้งหมดต้อง ship A2A spec compliance ในอีก 1-2 quarters ไม่งั้นเสีย strategic position

สำหรับ **Users / business** ที่ deploy agent ใน workflow: ข่าวดีคือ **vendor lock-in ที่กลัวปีที่แล้วเริ่มคลายลง** — ถ้าเลือกใช้ Agentforce วันนี้และเปลี่ยนใจอยากใช้ ServiceNow AI Agent ปีหน้า, A2A ทำให้ agent เก่ายัง interoperate ได้. คำถามที่ CIO ควรถาม vendor คือ "**คุณ certify A2A + MCP compliance หรือยัง?**" — ตอบว่า "กำลังทำ" ปีนี้ยัง OK, ปีหน้าถือว่า red flag. สำหรับ **ecosystem** — startup ที่ทำ **agent gateway/broker/router** (คล้าย OpenRouter ที่ Stripe เพิ่งซื้อ $7B แต่สำหรับ agent traffic) มี window ทองในการ position ตัวเองเป็น "**middleware ของ multi-agent economy**" ก่อนที่ hyperscaler จะบุกเข้ามาเก็บ layer นี้เอง

## Sources
- [Google's A2A protocol gets a new home — Axios](https://www.axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards)
- [A2A Protocol Surpasses 150 Organizations, Lands in Major Cloud Platforms, and Sees Enterprise Production Use in First Year — Linux Foundation](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)
- [Google's Agent2Agent project moves to Linux Foundation — InfoWorld](https://www.infoworld.com/article/4011301/googles-agent2agent-project-moves-to-linux-foundation.html)
- [Linux Foundation Launches the Agent2Agent Protocol Project — Linux Foundation Press](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents)

---

## Audio script
วันที่ 17 สิงหาคมที่ผ่านมา Agent2Agent Protocol หรือ A2A ที่ Google บริจาคให้ Linux Foundation เมื่อมิถุนายนปีที่แล้ว ย้ายเข้าไปเป็น hosted project ของ Agentic AI Foundation ที่เป็น sub-foundation เฉพาะทาง agent. A2A ปีเดียวโตจากน้อยกว่า 40 members มาเป็น 250+ ครอบ AWS Cisco Google Microsoft Salesforce SAP ServiceNow มี enterprise production use จริงแล้วในหลาย cloud. ที่น่าสนใจคือ protocol war ที่ปีที่แล้วคลุมเครือ ตอนนี้ resolve ลงเป็น 2 layer แยกงานกันชัด MCP เป็น agent ↔ tool A2A เป็น agent ↔ agent อยู่บ้านเดียว governance เดียว spec compatible กัน. เทียบกับปีก่อนที่ทุกคน push standard ของตัวเอง ตอนนี้ตลาด converge แล้ว. Signal ใหญ่คือ hyperscaler 3 รายบวก big enterprise vendor นั่งโต๊ะเดียวกันในเรื่อง multi-agent standard เกิดขึ้นน้อยมากในประวัติศาสตร์. เทียบเคียงได้กับตอน CNCF ทำให้ Kubernetes ชนะ Docker Swarm ในปี 2017-2018. สำหรับ builder ต้อง implement ทั้ง MCP และ A2A เป็น first-class citizen framework ที่ push custom protocol ของตัวเองกำลังจะเสีย strategic position. สำหรับธุรกิจ vendor lock-in ที่กลัวเริ่มคลาย คำถามที่ CIO ควรถาม vendor คือคุณ certify A2A และ MCP หรือยัง.
