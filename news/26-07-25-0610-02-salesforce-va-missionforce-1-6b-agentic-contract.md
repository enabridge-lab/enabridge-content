---
date: 2026-07-25
slug: salesforce-va-missionforce-1-6b-agentic-contract
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration on a warm off-white background:
  a massive stone government building labeled "U.S. VETERANS AFFAIRS"
  with 170 tiny hospital icons scattered around it. Floating above,
  a glowing contract scroll stamped in gold "$1.6B · AELA · 3 YEARS".
  A river of 17 million tiny figure silhouettes flowing into the
  building's front door. In the background, four smaller buildings
  labeled "AGENTFORCE", "DATA CLOUD", "SLACK", "MISSIONFORCE" linked
  by glowing pipelines converging on the main building. Sharp editorial
  typography, high contrast, 1:1 aspect, no real human faces.
image: images/26-07-25-0610-02-salesforce-va-missionforce-1-6b-agentic-contract.png
---

# Salesforce คว้าดีล $1.6B กับกระทรวงกิจการทหารผ่านศึกสหรัฐ — เปิดตัว "Agentic Enterprise License" ครั้งแรก แม่แบบใหม่ของการซื้อ agent platform ยุค deployment

## TL;DR
- U.S. Department of Veterans Affairs (VA) มอบสัญญา **$1.6 พันล้านดอลลาร์ 3 ปี** ให้ Salesforce เมื่อ 24 ก.ค. — เรียกว่า **"Agentic Enterprise License Agreement" (AELA)** — เป็น contract vehicle ใหม่ที่ bundle Agentforce + Data Cloud + Slack + Missionforce เข้าเป็น flat-fee package
- Missionforce จะเชื่อม people + data + workflow ข้าม **170 medical center + 1,100+ outpatient clinic** ให้บริการ **veteran + ครอบครัว + caregiver รวม 17 ล้านคน**
- Agent capability ครอบคลุม 24/7 virtual contact center, real-time knowledge surfacing, automated benefits verification, case routing/triage; Slack live แล้วที่ 150+ VA facility กำลังขยาย
- Structure: 1-year base + 2 x 1-year option ceiling $1.6B; Agentforce context: **$800M ARR (+169% YoY), 29,000 Q4 deals, 2.4B agentic work unit delivered**
- Signal: **AELA เป็น template แรกของนิยามใหม่ "flat-fee agent bundle"** — เตรียมพร้อมให้ ServiceNow / Microsoft / Google Cloud copy ไตรมาสหน้า

## เกิดอะไรขึ้น
วันที่ 24 กรกฎาคม 2026 U.S. Department of Veterans Affairs ประกาศมอบสัญญา **$1.6 พันล้านดอลลาร์ ระยะเวลา 3 ปี** ให้ Salesforce — บรรจุใน contract vehicle ใหม่ชื่อ **"Agentic Enterprise License Agreement" (AELA)** — เป็น flat-fee ที่รวม Agentforce (platform สร้าง + run agent), Data Cloud (unified data layer), Slack (collaboration + agent surface), และ **Missionforce** (solution suite ที่ Salesforce build โดยเฉพาะสำหรับ federal + defense + veteran affairs) เข้าเป็น package เดียว. Structure ทางกฎหมาย: 1-year base ($~530M) + 2 x 1-year renewal option, ceiling รวม $1.6B — ให้ VA มี exit ทุกปีถ้า performance ไม่เข้าเป้า.

Missionforce จะเชื่อม workflow ข้าม **170 VA medical center + 1,100+ outpatient clinic** ให้บริการ **veteran + ครอบครัว + caregiver รวมกัน 17 ล้านคน**. Capability agent ที่ VA จะเปิดในไตรมาสหน้า: (1) **24/7 virtual contact center triage** — agent รับสายและ classify urgent vs non-urgent, route ต่อ; (2) **real-time knowledge surfacing** — ระหว่าง human agent คุยกับ veteran, AI ดึง case history + eligibility + benefit rule ที่เกี่ยวข้องขึ้นมาโชว์ทันที; (3) **automated benefits verification** — agent เช็ค eligibility และเตรียม document โดยไม่ต้องรอ manual review; (4) **case routing + triage** — จัด priority queue อัตโนมัติตาม severity + wait time. Slack platform ก็ deploy แล้วที่ **150+ VA facility** และมีแผนขยายทั่วระบบภายในปีนี้.

Deal นี้เป็น context ที่มาต่อจาก Salesforce Q4 FY26 earnings ที่ปิดในเดือน พ.ค. — Agentforce ทะลุ **$800M ARR โต 169% YoY**, ปิด **29,000 deal** ในไตรมาสเดียว, delivered **2.4 พันล้าน agentic work unit** (Salesforce metric ที่นับ discrete task ที่ agent ทำจบ). VA $1.6B ไม่ใช่ deal ใหญ่ที่สุดของ Salesforce ในปี (US Bank ปีที่แล้วเป็น $2.3B, Walmart ปีก่อนหน้านั้น $2.8B) แต่เป็น **deal แรกที่ใช้ AELA structure สาธารณะ**. Marc Benioff บอกใน press release ว่า Missionforce เป็น "first purpose-built agent solution suite for federal mission-critical operation" — signal ว่า Salesforce จะขายเป็น vertical bundle มากขึ้น แทน horizontal Agentforce license ธรรมดา.

Deal นี้เกิดขึ้นในช่วง federal AI spending scrutiny — GAO และ Congressional Budget Office กำลัง audit AI contract ที่ agency ต่าง ๆ (OPM ยกเลิก $500M contract ของ Palantir เมื่อเดือน มิ.ย., DHS pause $1B contract ของ Anduril). แต่ VA-Salesforce ผ่านฉลุยเพราะ (1) Salesforce มี FedRAMP High + IL5 authorization แล้ว, (2) Missionforce architect ให้ data ไม่ออก VA boundary — LLM inference on-premise + government cloud, (3) มี clause ให้ VA ยกเลิกได้ทุกปี ถ้า agent performance ไม่ถึง SLA. structure นี้เป็น model ที่ agency อื่น (DoD, HHS, IRS) น่าจะเอาไปเลียนแบบ.

## ทำไมสำคัญ
**AELA เป็น pricing innovation ที่ตอบโจทย์ enterprise buyer ในยุค agent deployment**. ที่ผ่านมา agent platform pricing เป็น chaos — บาง vendor คิด per-conversation (Sierra), บาง vendor คิด per-agent (Agentforce เดิม), บาง vendor คิด per-token (Bedrock AgentCore), บาง vendor คิด per-successful-outcome (Cognigy). CFO ที่ต้องอนุมัติ multi-million contract ไม่มีวิธี budget เพราะ workload variance สูง. AELA ตัดปัญหานี้ทิ้ง — จ่าย flat fee ต่อปี, ใช้ agent capacity ไม่จำกัดใน scope ที่กำหนด, capacity limit อยู่ที่ Data Cloud storage + Slack seat + workflow definition ไม่ใช่ conversation count.

Pattern ที่กำลัง crystallize คือ **"flat-fee agent bundle" จะแทน per-transaction pricing ในตลาด enterprise ภายใน 12 เดือน**. เทียบกับยุค SaaS ที่ Salesforce เริ่ม "unlimited edition" ใน 2015 แล้ว Oracle/Microsoft/SAP copy ตามในปีถัดไป — AELA ก็น่าจะเป็นจุดเริ่มต้นแบบเดียวกัน. ServiceNow (มี Now Assist + Now Agent Studio + Impact) มี architecture ที่พร้อม package เป็น bundle; Microsoft (Copilot Studio + M365 Copilot + Azure AI Foundry) กำลังทดลอง "Copilot for Enterprise" tier ที่ราคา flat; Google Cloud (Gemini Enterprise + Vertex Agent Builder + Workspace) มี Fortune 100 penetration 90% แล้ว (ดู brief 24 ก.ค.) — flat-fee bundle เป็น next step ธรรมชาติ.

Sub-signal สำหรับ vendor competition: **Palantir กำลังเสีย federal ground แม้จะมี AIP + Foundry** เพราะ pricing model ยัง project-based มากเกินไป (statement of work + T&M) — ในขณะที่ Salesforce ขาย license-based flat fee ที่ agency ประเมิน total cost of ownership ได้ล่วงหน้า. Anduril, Scale AI, Vannevar Labs — vendor ใหม่ที่พยายามแย่ง federal AI market — ต้องคิด structure สัญญาใหม่ ถ้ายังขายเป็น hourly SOW จะแพ้ให้ vendor ที่ขายเป็น subscription.

## มุม AI Agent Platform
สำหรับ **builders** ที่กำลัง price agent product ของตัวเอง — พิจารณา flat-fee tier ที่ scope ตาม (a) domain scope (billing agent เท่านั้น หรือครอบทั้ง customer service), (b) data volume (จำกัด GB ต่อเดือน), (c) integration count (จำกัด SaaS connector) แทนการคิด per-transaction. Enterprise buyer จะเลือก vendor ที่ให้ budget predictability — ถึงแม้ราคาสูงกว่า per-transaction 20-30% ก็ตาม. Startup ที่ทำ agent framework (LangGraph Cloud, Vercel AI SDK, Mastra) ควรออกแบบ pricing tier ที่ mimic AELA — "flat monthly, unlimited invocation within X domain".

สำหรับ **enterprise users** ที่กำลัง negotiate contract Q3-Q4 2026 — ขอ AELA-style term กับ vendor ปัจจุบัน. Talking point: "VA เพิ่ง sign $1.6B AELA กับ Salesforce, ผม/ดิฉันขอ pricing structure เดียวกัน — flat annual + unlimited agent invocation ใน scope ที่ตกลง". ถ้า vendor ปฏิเสธ = signal ว่า vendor กำลัง extract rent จาก transaction pricing arbitrage. เตรียม fallback: Salesforce Missionforce (vertical-specific), Google Vertex Agent Builder (Fortune 100 default), Microsoft Copilot Studio Enterprise, AWS Bedrock AgentCore. Multi-vendor negotiation ผ่าน AELA framework จะทำให้ leverage เพิ่ม.

สำหรับ **ecosystem** — SI (System Integrator) ที่เคยขาย hourly deployment service (Accenture, Deloitte, TCS, Infosys, Wipro) ต้อง revamp business model. AELA แปลว่า client จ่าย Salesforce ก้อนเดียว, SI ได้ margin จากการ integrate + customize + operate — ไม่ใช่จากการ resell license. Regional SI ใน APAC (Aegis Softtech, Tech Mahindra, HCL) มี opportunity ใหม่ ถ้าพัฒนา Missionforce-equivalent solution suite สำหรับ vertical ในภูมิภาค (Southeast Asia healthcare, Australian government, Japan manufacturing).

## Sources
- [Missionforce transforms veteran care with $1.6B AELA (Salesforce Press Release)](https://www.salesforce.com/news/press-releases/2026/07/24/missionforce-transforms-veteran-care/)
- [Salesforce Agentforce enterprise ARR and deal metrics (TechHQ)](https://techhq.com/news/salesforce-agentforce-enterprise-agentic-ai/)
- [Salesforce Agentforce 360 announcements hub](https://www.salesforce.com/agentforce/what-is-new/)
- [Salesforce Agentforce complete guide 2026 (MyAskAI)](https://myaskai.com/blog/salesforce-agentforce-complete-guide-2026)

---

## Audio script
สวัสดีครับ วันศุกร์ที่แล้ว Salesforce ปิดดีลใหญ่ — กระทรวงกิจการทหารผ่านศึกสหรัฐฯ หรือ VA มอบสัญญามูลค่าหนึ่งจุดหกพันล้านดอลลาร์ระยะเวลาสามปี. แต่ที่น่าสนใจกว่ามูลค่าคือรูปแบบสัญญา — เรียกว่า Agentic Enterprise License Agreement หรือ AELA — เป็นครั้งแรกที่ vendor รายใหญ่ขาย agent platform เป็น flat fee ระดับพันล้าน. Package รวม Agentforce, Data Cloud, Slack, และ Missionforce ซึ่งเป็น solution suite เฉพาะสำหรับ federal mission-critical operation. Scope ครอบคลุมโรงพยาบาลหนึ่งร้อยเจ็ดสิบแห่งและคลินิกอีกกว่าหนึ่งพันแห่ง ให้บริการ veteran ครอบครัว และ caregiver รวมสิบเจ็ดล้านคน. Capability agent ที่ VA จะเปิดในไตรมาสหน้า — virtual contact center รับสายยี่สิบสี่ชั่วโมง, real-time knowledge surfacing ระหว่าง human agent คุยกับ veteran, automated benefits verification, และ case triage. Slack เอง live อยู่ที่หนึ่งร้อยห้าสิบ facility แล้ว. ที่ผ่านมา agent platform pricing เป็น chaos — per conversation บ้าง per agent บ้าง per token บ้าง per outcome บ้าง — CFO ไม่มีวิธี budget. AELA ตัดปัญหาทิ้ง — flat fee, ใช้ agent capacity ไม่จำกัดใน scope. Pattern ที่กำลัง crystallize คือ ServiceNow, Microsoft, Google Cloud น่าจะ copy AELA ภายในหนึ่งถึงสองไตรมาส. สำหรับ builder ที่กำลัง price agent product แนะนำให้พิจารณา flat fee tier ที่ scope ตาม domain, data volume, integration count แทน per transaction. สำหรับ enterprise buyer กำลังจะ sign contract ไตรมาสนี้ ขอ AELA-style term กับ vendor ปัจจุบันได้เลย — VA เพิ่ง set precedent ให้แล้วครับ.
