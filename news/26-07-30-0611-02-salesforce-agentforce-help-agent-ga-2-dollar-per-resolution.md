---
date: 2026-07-30
slug: salesforce-agentforce-help-agent-ga-2-dollar-per-resolution
topic: use-case
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial isometric illustration on a deep navy background: a giant
  vending machine labeled "AGENTFORCE HELP AGENT" dispensing a
  glowing ticket stamped "RESOLVED". A coin slot glows blue with a
  price tag "$2 / RESOLUTION". Beside it, three floating scoreboards
  read "4.3M ENQUIRIES", "70% AUTONOMOUS", "MIN 1,000 PACK". Silhouette
  buyers pass by carrying prepaid packs; a rejected card falls into a
  bin labeled "HUMAN HANDOFF — NO CHARGE". Above the machine, a banner
  reads "OUTCOME > TOKEN". Sharp editorial typography, cinematic depth,
  1:1 aspect, no real human faces.
image: images/26-07-30-0611-02-salesforce-agentforce-help-agent-ga-2-dollar-per-resolution.png
---

# Salesforce Agentforce Help Agent GA — $2/resolution flat, 4.3M enquiries + 70% autonomous ที่ Salesforce ทดลอง — outcome-based กลายเป็น standard pricing ของ enterprise agent

## TL;DR
- **Agentforce Help Agent + Agentforce Customer Service Portal ประกาศ GA กรกฎาคม 2026** — pre-packaged autonomous service agent ที่ deploy ได้ในไม่กี่ขั้นตอน (Salesforce เคลม "under 10 setup steps")
- **Pricing model ใหม่: $2 flat per successful resolution** — ถ้า customer กด "ขอคุยกับคน" หรือทิ้งไปโดยไม่ satisfied — **ไม่คิดเงิน**
- Prepaid packs, minimum purchase **1,000 resolutions** (~$2,000 entry ticket) — คน enterprise สามารถ negotiate rate + pack size ได้
- **Proof of concept ของ Salesforce เอง**: handle **4.3 ล้าน enquiries** ผ่าน help.salesforce.com, resolve **70% autonomously** — ไม่ต้อง escalate ให้คน
- Signal: **ยุค token-based pricing ของ agent จะจบเร็ว** — enterprise buyer อยาก tie cost กับ outcome ไม่ใช่ compute; vendor ที่ยังขาย seat/token จะเจอ pressure จาก competitor ที่ขาย outcome ก่อน

## เกิดอะไรขึ้น
กรกฎาคม 2026 **Salesforce ปล่อย Agentforce Help Agent เข้าสู่ general availability** — คู่กับ **Agentforce Customer Service Portal** ที่ GA ในรอบเดียวกัน. product นี้เปิดตัว preview เมื่อ 25 มิถุนายน แต่ **GA รอบนี้มาพร้อม pricing structure ใหม่ที่ทั้ง industry จับตา** — **flat rate $2 ต่อ successful resolution**. ใช้ pattern เดียวกับ Zendesk / Intercom ที่เพิ่งเริ่มขยับ แต่ **Salesforce เป็นเจ้าแรกที่ enterprise-grade แล้ววาง scale**. Prasad Raje (SVP of Product, Agentforce Service) พูดในรอบประกาศตรง ๆ ว่า *"It's a flat price of $2 when a resolution is achieved"*.

**Definition ของ "resolution" สำคัญมาก**: customer เข้าคุยกับ agent, agent แก้ปัญหาจนจบ end-to-end **autonomously** — จะจ่าย $2. ถ้าลูกค้ากด "ขอคุยกับ human agent" ระหว่างทาง หรือทิ้งการสนทนาไปโดยไม่ satisfied — **ไม่มี charge**. Model นี้ **repricing ทั้ง value chain** — เดิม vendor ขาย token/seat/license แล้ว burden ของ ROI เป็นของลูกค้า (ถ้า agent ทำได้ไม่ดี ลูกค้าก็ยังต้องจ่าย). ตอนนี้ Salesforce **shift risk มาที่ตัวเอง** — จะได้เงินก็ต่อเมื่อ deliver value จริง. เป็นการยอมรับโดยไม่ตรง ๆ ว่า **agent ในหลายบริษัทยังไม่ดีพอที่จะให้ลูกค้าเซ็น seat license ได้อย่างมั่นใจ** — Salesforce เอง burn cost บาง resolution แต่จะได้ pricing power ระยะยาว.

Structure การซื้อ: **prepaid packs**, ต้องซื้อขั้นต่ำ **1,000 resolutions** = **$2,000 entry ticket** — เข้าถึง SMB ได้เกือบเต็มตลาด. Enterprise buyer สามารถ negotiate rate ต่ำกว่า $2 + pack size ใหญ่ขึ้น — สอดคล้องกับ note จาก UpperEdge (procurement advisor) ที่บอก enterprise ควร treat $2 เป็น "starting point" ไม่ใช่ list price. Salesforce ปล่อยข้อมูลว่า **Agentforce ทั้งชุด (ไม่ใช่แค่ Help Agent) แตะ $1 พันล้าน ARR** ในไตรมาสก่อน — ถ้า Help Agent ที่ปั่นด้วย outcome model สามารถ scale ได้ตามที่ hyped จะเป็น catalyst ให้ Salesforce ผลักดัน tiers ให้ทั้งหมด ไม่ใช่แค่ service.

**Salesforce ทำ dogfooding เต็มตัว**: help.salesforce.com ใช้ Agentforce Help Agent มาแล้วช่วงหลายเดือน — **handle 4.3 ล้าน customer enquiries, resolve 70% autonomously**. Number 70% เป็น *containment rate* ที่ทั้ง industry จับ่ตา — ตัวเลขที่ทีม customer service ระดับโลก (Amazon, Airbnb, Uber) ตั้งเป้าให้ถึง 70% กันมาสามปีแล้ว. **ถ้า number ของ Salesforce ยืนยันได้จริงกับ Fortune 500 client** (ยังไม่มี third-party validation ณ จุดนี้ — บริษัทอ้าง) จะเปลี่ยน category ทั้งชุด.

รอบเดียวกัน Salesforce ปล่อย **Agentforce Commerce GA** พร้อม **Shopper, Buyer, Merchant agents** — สินค้า Shopper agent สามารถ *"check live inventory, confirm carrier cutoffs, offer store pickup, and close sale within a single conversation"* — commerce-native agent transaction. บวกกับ **Setup with Agentforce GA** (admin ใช้ agent build agent อื่น) — Salesforce กำลัง compress agent lifecycle ทั้ง build → deploy → charge เข้า suite เดียว. Constellation Research อ่านว่านี่คือ Salesforce สร้าง **agent operations business unit ระยะ 5 ปี** ที่จะเป็นทดแทน CRM seat license ที่โต flat.

## ทำไมสำคัญ
**Outcome-based pricing แก้ปัญหาที่ทั้ง industry ติดมาสองปี — "AI agent มี ROI จริงไหม?"**. ตั้งแต่ 2024 CIO ระดับ Fortune 1000 จ่ายเงินซื้อ agent license ที่คิดตาม seat หรือ token — แล้วต้อง prove ROI ให้ CFO ในไตรมาสถัดไป. ตอนนี้ Salesforce เปลี่ยน equation: **จ่ายเฉพาะเมื่อ deliver — CFO อ่านง่ายกว่า** เพราะทุก dollar cost ผูกกับ business outcome (resolution ที่นับได้). Signal ที่ตลาดอ่าน: **vendor ทุกรายที่ขาย autonomous agent จะต้องมี outcome pricing option ใน 12 เดือน** — Zendesk, Intercom, Freshworks, ServiceNow ก็ต้องขยับ; ServiceNow ที่รายงาน Q2 AI ACV $1B (เราคุยเมื่อ 26 ก.ค.) จะเจอ pressure หนักที่สุด. Startup ที่ยังขาย token/seat จะเจอ headwind บาง — Twilio, Vonage, LivePerson ที่ pivot ไป AI ต้องคิดใหม่ก่อนสิ้นปี.

Pattern ที่เห็นชัด: **ยุค agent pricing กำลังเข้าเฟส "insurance"** — vendor รับ risk ของ delivery. คล้ายกับ shift ที่ SaaS ทำจาก perpetual license → subscription ในปี 2010-2015 — model transition ที่ **บริษัทเจ้าตลาดที่มี scale เท่านั้นที่ทน initial margin compression ได้**. Salesforce มี scale — startup ไม่มี. นี่คือ subtle moat play — Salesforce ใช้ balance sheet ของตัวเอง absorb loss ในช่วง early adopter, บังคับ competitor ต้อง match — จบด้วย consolidation ที่ Salesforce ได้เปรียบ. **The Information และ Constellation Research** สังเกตว่าถ้า Help Agent hit target volume — Salesforce จะ crush เจ้าเล็กในตลาด ITSM/CX ทั้งชั้น. **แต่ที่น่าสงสัย** — Prasad Raje บอก $2 flat แต่ Salesforce ยังไม่เปิด **cost of goods (COGS)** ต่อ resolution — ถ้า inference cost + retrieval cost + human oversight cost รวมกันเกิน $2 — Salesforce จะกำลัง subsidize เพื่อ lock market share (playbook เดียวกับ AWS S3 ในยุคแรก).

## มุม AI Agent Platform
**Builders:** ถ้ากำลัง build customer service agent, sales agent, IT agent — **เพิ่ม outcome-tracking layer เป็น first-class citizen** ก่อน launch. หมายถึง: (1) **definition of resolution ต้อง clear + measurable** — ปิด ticket ใน CRM, satisfaction score, no-callback ใน N days; (2) **pricing engine** ที่คิดเงินเฉพาะ successful outcome — ต้อง track dispute, refund, edge case; (3) **cost model transparent** — CFO ของลูกค้าจะถาม unit economics — เตรียม breakdown ให้ครบ (inference, retrieval, human handoff cost). Framework ที่ support outcome tracking ตั้งแต่ต้น (Mastra, Vercel AI SDK, LangGraph Platform) จะได้ advantage. **สำหรับ MCP server builders** — ต้อง support metrics endpoint ที่ agent runtime ใช้ track resolution + attribution — spec MCP 2026-07-28 ที่ stateless + cacheable ทำให้ metrics collection ง่ายขึ้น มาก.

**Users / business:** ถ้าจะ deploy service agent Q3-Q4 — **RFP ต้องมี 3 clause ใหม่**: (1) *outcome pricing option* — ให้ vendor commit rate + volume tier + no-charge on human handoff; (2) *containment rate SLA* — vendor commit % ของ enquiries ที่ resolve autonomously (Salesforce claim 70% — ใช้เป็น baseline); (3) *escalation cost cap* — ถ้า resolution rate ต่ำกว่า SLA vendor รับผิดชอบ. อย่าเซ็นสัญญาที่ price ตาม token / seat / เดือน ถ้ามี outcome option. สำหรับ CFO — ยืมกรอบของ Prasad Raje: **"pay for outcomes, not effort"** — ใช้เป็น criteria vendor selection ตลอด procurement cycle ของ AI.

**Ecosystem:** ผู้ชนะ — Salesforce, ServiceNow, HubSpot ที่มี scale จน absorb loss ช่วง early adopter. ผู้แพ้ — **startup ที่ขาย autonomous agent under $10M ARR without pricing flexibility** — จะเจอ pressure จาก enterprise buyer ที่ upgrade กรอบใหม่. **Consulting / SI ในไทย** (Cognizant Thailand, Accenture SEA, Bluebik, G-Able, K-Consulting) — window เปิดที่จะ deliver *outcome-based agent implementation service* ให้ Thai enterprise (K-Bank, SCB, AIS, PTT, CP) — model ที่ SI รับ risk ร่วมกับ vendor + client จะเป็น differentiator. Startup ไทยที่ build service agent (Amity Solutions, Skooldio's tool arm, Botnoi) — เริ่ม structure outcome pricing tier ก่อนสิ้นปี — ก่อนที่ Salesforce Agentforce จะเริ่มขายจริงในไทย Q1 2027.

## Sources
- [Salesforce Launches Agentforce Help Agent That Deploys in Minutes and Only Charges for Resolutions — Salesforce](https://www.salesforce.com/news/stories/agentforce-help-agent-announcement/)
- [Salesforce takes a run at outcome-based Help Agent pricing — Constellation Research](https://www.constellationr.com/insights/news/salesforce-takes-run-outcome-based-help-agent-pricing)
- [Salesforce Debuts Help Agent With Pay-Per-Resolution AI — CMSWire](https://www.cmswire.com/contact-center/salesforce-debuts-help-agent-with-payperresolution-ai/)
- [Salesforce's New Agentforce Help Agent: AI Customer Service Help — CXM.world](https://cxm.world/customer-experience/salesforce-agentforce-help-agent-pay-per-resolution/)
- [Salesforce Agentforce Pricing: How to Negotiate Outcome-Based Licensing — UpperEdge](https://upperedge.com/salesforce/salesforces-outcome-based-pricing-for-agentforce-help-agent-what-enterprise-buyers-need-to-negotiate-now/)

---

## Audio script
เรื่องที่สองคือ Salesforce ปล่อย Agentforce Help Agent เข้า general availability กรกฎาคมนี้ — และที่สำคัญคือ pricing แบบใหม่ — flat rate 2 ดอลลาร์ต่อ successful resolution. ถ้าลูกค้ากด ขอคุยกับคน หรือทิ้งไปโดยไม่ satisfied — ไม่คิดเงิน. Salesforce shift ความเสี่ยงมาที่ตัวเอง — จะได้เงินก็ต่อเมื่อ deliver value จริง. Prepaid packs ขั้นต่ำ 1,000 resolution = 2,000 ดอลลาร์ entry ticket, enterprise buyer สามารถ negotiate ได้.

proof point ที่ Salesforce เอา dogfooding ของตัวเองมา claim — help.salesforce.com ใช้ Agentforce Help Agent มาระยะหนึ่ง, handle 4.3 ล้าน enquiries, resolve 70 เปอร์เซ็นต์ autonomously — เป็น containment rate ที่ทีม customer service ระดับโลกตั้งเป้ามาสามปี. ยังไม่มี third party ยืนยัน — บริษัทอ้าง — แต่ถ้าจริงจะเปลี่ยน category ทั้งชุด.

signal ที่ต้องอ่าน — ยุค token-based pricing ของ agent จะจบเร็ว. CFO อ่าน outcome pricing ง่ายกว่า เพราะ dollar cost ผูกกับ business outcome ที่นับได้. Zendesk, Intercom, Freshworks, ServiceNow จะต้องขยับ outcome pricing option ภายใน 12 เดือน. Startup ที่ยังขาย token seat โดยไม่มี flexibility จะเจอ headwind.

สำหรับ builder ในไทย — ถ้ากำลัง build customer service agent ต้องเพิ่ม outcome tracking layer เป็น first class — definition of resolution, pricing engine, cost model. RFP ปีนี้จะเริ่มมี clause ใหม่ — outcome pricing option, containment rate SLA, escalation cost cap. Amity Solutions, Botnoi, Skooldio ทีม tool ต้อง structure tier ก่อน Salesforce เข้าไทยเต็มตัว Q1 2027. SI ไทย — Bluebik, G-Able, Cognizant Thailand — window เปิดที่จะขาย outcome-based implementation service ให้ K-Bank, SCB, AIS, PTT.
