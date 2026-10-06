---
date: 2026-10-06
slug: 26-10-07-0616-04-reco-55m-agent-security-funding
topic: agentic-ai
reading_time_min: 3
sources: 4
image_prompt: |
  Editorial hero: a glowing fortress wall labeled "AGENT PERIMETER" with
  tiny agent avatars funneling through a single checkpoint titled
  "RECO". A large pile of chips in the foreground stacked with "$55M"
  and "$140M TOTAL". Behind the wall a billboard reads
  "150,000 AGENTS PER FORTUNE 500 BY 2028 — GARTNER". AT&T logo tag on
  the corner lantern. Isometric editorial vector, deep indigo + alert
  amber + silver, 1:1 aspect, no real human faces.
image: images/26-10-07-0616-04-reco-55m-agent-security-funding.png
---

# Reco ปิด $55M จาก AT&T Ventures — pump เงินเข้า "ตำรวจของ agent" ขณะ Gartner forecast Fortune 500 จะมี agent 150,000 ตัวต่อ enterprise ภายใน 2028

## TL;DR
- Reco ปิด **strategic round $55M** 29 ก.ย. 2026 นำโดย **AT&T Ventures** + Forestay + Quadrille Capital — รวมเงิน funding แล้ว **$140M**
- Reco ขาย **agent security + governance platform** ที่ secure autonomous AI agent ข้าม application, identity, permission, workflow — ตลาด Fortune 500 กำลัง scramble
- **Gartner คาด** Fortune 500 เฉลี่ยจะมี **>150,000 agent** ต่อ enterprise ภายในปี 2028 (จากน้อยกว่า 15 ในปี 2025) — scale นี้ทำให้ "security for agents" กลายเป็น budget line ใหม่ของ CISO

## เกิดอะไรขึ้น

Reco — บริษัท SaaS/AI security ที่ตั้งอยู่ Tel Aviv + NYC — ประกาศปิด strategic round $55M เมื่อ 29 ก.ย. นำโดย **AT&T Ventures** (เป็น strategic signal: carrier ใหญ่เริ่มมอง agent security เป็น infra); มี new backer **Forestay** และ **Quadrille Capital** ร่วม. บวกกับ $30M Series B เดือน ก.พ. (รวมเป็น $85M) → cumulative funding **$140M**

Platform ของ Reco นั่งเป็น **"security graph"** ที่ map connection ระหว่าง: agent ↔ identity ↔ permission ↔ application ↔ data ↔ workflow. เมื่อ agent สักตัวได้สิทธิ์เข้า Salesforce / Slack / Google Drive / Confluence แล้ว Reco track behavior pattern, detect privilege escalation, revoke access ก่อนที่ data จะรั่ว. เน้นปัญหา **"shadow agent"** — agent ที่พนักงาน spin ขึ้นเองใน Copilot / ChatGPT Enterprise / Zapier แล้วไม่มีใน IT inventory

ตัวเลขที่ Reco ใช้ pitch VC คือ **Gartner forecast ปี 2028**: Fortune 500 เฉลี่ยจะมี **>150,000 agent** ต่อ enterprise (จาก <15 ในปี 2025) — เป็น 10,000x growth ในสาม ปี. ถ้าเลขนี้ใกล้ความจริง, security tooling ที่ visibility ได้แค่ 1,000 agent (ปัจจุบัน) จะใช้ไม่ได้; CISO ต้องซื้อ platform ใหม่ที่ scale ถึงหลักแสน

เงินใหม่จะไปที่ **sales / partner / channel expansion** — บอกว่าตลาด enterprise พร้อมซื้อแล้ว ไม่ใช่ engineering ยังไม่พร้อม

## ทำไมสำคัญ

Pattern สัปดาห์นี้สะท้อนตลาดเดียวกับที่เราเห็นกับ **Classie Supervise** (ปิดเงินปลาย ก.ย.), **Trail ML** (acquired), **Collibra Deasy Labs** (acquired) — **agent governance / observability / security กำลัง consolidate เร็วมาก**. เหตุผลคือ: enterprise ที่ pilot agent 3-5 ตัวในปี 2024 กำลังสเกลไป 50-500 ตัวในปี 2026 แล้วไม่มี tooling ที่ scale ตาม. VC มองออกว่าตลาดนี้จะเป็น **$5-10B category** ภายใน 3 ปี เพราะเลข Gartner 150K agent / enterprise คูณกับ Fortune 500 = 75 ล้าน agent instance ที่ต้อง secure

AT&T Ventures นำ round นี้มีความหมายเฉพาะ: AT&T มี **core telecom infrastructure** และดูแล enterprise customer หลายหมื่นราย. ถ้า carrier ใหญ่เริ่ม bundle "agent security" เป็น add-on ของ enterprise connectivity → ตลาดเปิดกว้างกว่า "pure SaaS vendor sell direct". คาดว่า Verizon, Deutsche Telekom, BT, NTT, AIS/True ของไทยจะ follow pattern นี้ภายใน 12-18 เดือน — ขาย agent security ให้ enterprise customer ที่ซื้อ MPLS/5G ของตัวเองอยู่แล้ว

Signal อีกชั้นที่น่าสนใจ: Reco **ไม่ได้ขาย frontier model** และ **ไม่ได้ขาย agent framework** — ขายแค่ **governance layer**. ตลาด agent ปี 2026 เริ่มมี category แยกชัด: (1) model provider, (2) framework / orchestration, (3) vertical agent app, (4) **governance + security + observability**. ชั้นที่ 4 เป็นที่ที่ VC เห็น clear defensible margin เพราะ switching cost สูง (ลูกค้า Fortune 500 จะไม่เปลี่ยน security platform บ่อย)

## มุม AI Agent Platform

**Builders:** คนทำ agent framework (LangChain, CrewAI, AutoGen) ต้องตัดสินใจ — จะสร้าง governance primitive ใน SDK เอง (compete กับ Reco) หรือ expose hook ให้ Reco/Classie/Deasy plug เข้ามา (เป็น partner). Framework ที่ปิด API ไว้จะโดนลูกค้า push ให้ open — เพราะ CISO ต้องการ unified view ข้ามทุก agent runtime. **Users / business:** CTO/CISO ที่ยังเปิด agent pilot แบบ ad-hoc ควรเริ่ม inventory ก่อน Q1 2027 — ถาม 3 คำถามพื้นฐาน: (1) agent มีกี่ตัวในองค์กร? (2) แต่ละตัวได้สิทธิ์อะไรใน SaaS stack? (3) ใครเป็นเจ้าของ agent แต่ละตัว? ถ้าตอบไม่ได้ = ซื้อ governance tool. **Ecosystem:** Palo Alto Networks, CrowdStrike, Wiz, Zscaler — security giant จะต้องตอบ "agent security" ภายใน 12 เดือน ไม่งั้นเสีย enterprise mindshare ให้ pure-play Reco/Classie; audit vendor (Deloitte, PwC) จะเริ่มเพิ่ม "agent inventory + permission audit" เป็น standard scope ของ internal audit

## Sources
- [Reco raises $55 million with participation from AT&T Ventures - The Paypers](https://thepaypers.com/fraud-and-fincrime/news/reco-raises-usd-55-million-with-participation-from-att-ventures)
- [Reco raises $60 million for agentic security - Enterprise Times](https://www.enterprisetimes.co.uk/2026/09/29/reco-raises-60-million-for-agentic-security/)
- [Reco raises $55M for agentic security - SecurityWeek](https://www.securityweek.com/reco-raises-55-million-for-agentic-security/amp/)
- [Reco raises $50M with AT&T backing as enterprises race to secure AI agents - Ynetnews](https://www.ynetnews.com/business/article/h1et60uczg)

---

## Audio script
Reco ปิด strategic round ห้าสิบห้าล้านดอลลาร์ 29 กันยา นำโดย AT&T Ventures บวก Forestay บวก Quadrille Capital รวม funding แล้วหนึ่งร้อยสี่สิบล้าน. Reco ขาย agent security และ governance platform ที่ secure autonomous AI agent ข้าม application identity permission workflow. ตัวเลขที่ Reco ใช้ pitch คือ Gartner forecast ปี 2028 Fortune 500 เฉลี่ยจะมี agent มากกว่าหนึ่งแสนห้าหมื่นตัวต่อ enterprise จากน้อยกว่าสิบห้าในปี 2025 เป็นหมื่นเท่าในสามปี. ถ้าเลขนี้ใกล้ความจริง security tool ที่ visibility ได้แค่พันตัวจะใช้ไม่ได้ CISO ต้องซื้อ platform ใหม่ที่ scale ถึงหลักแสน. ที่ AT&T Ventures นำ round นี้มีความหมายเฉพาะ. AT&T มี core telecom infrastructure และดูแล enterprise customer หลายหมื่นราย. ถ้า carrier ใหญ่เริ่ม bundle agent security เป็น add on ของ enterprise connectivity ตลาดเปิดกว้างกว่า pure SaaS sell direct. คาดว่า Verizon, NTT, AIS, True ของไทยจะ follow pattern ภายในหนึ่งปี. CTO CISO ที่ยังเปิด agent pilot แบบ ad hoc ควรเริ่ม inventory ก่อนไตรมาสแรกปีหน้า agent มีกี่ตัวในองค์กร ใครเป็นเจ้าของ แต่ละตัวได้สิทธิ์อะไร. ตอบไม่ได้ซื้อ governance tool

