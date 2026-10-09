---
date: 2026-10-06
slug: 26-10-10-0615-05-netskope-agentskope-marketplace
topic: openbridge-trend
reading_time_min: 3
sources: 4
image_prompt: |
  Editorial hero: a glowing storefront labeled "AGENTSKOPE MARKETPLACE"
  with six shelves holding mechanical agent robots stamped "DLP",
  "INSIDER THREAT", "SIEM TRIAGE", "NETWORK ANOMALY", "FIREWALL", "SOC".
  A single capacity meter dial above reads "SHARED CREDIT POOL" with
  the needle at mid-range. A clipboard on the counter reads "42% ALERTS
  UNINVESTIGATED". Editorial isometric style, Netskope cyan + dark
  slate + warning amber, 1:1 aspect, no real human faces.
image: images/26-10-10-0615-05-netskope-agentskope-marketplace.png
---

# Netskope เปิด AgentSkope Marketplace — ซื้อ agent รักษาความปลอดภัยแบบจ่ายรวมจาก credit pool เดียว

## TL;DR
- 6 ต.ค. 2026 **Netskope** เปิด **AgentSkope Marketplace** — console เดียวที่ security team ค้น / ให้ขนาด / ให้ budget / monitor usage ของ AI agent สำหรับ SOC + NetOps
- Pricing primitive ใหม่: ลูกค้า **ไม่ซื้อ agent ทีละตัว** แต่ซื้อ **"capacity credit pool"** เดียวแล้ว allocate เองในคอนโซล — adjustment มีผลทันที
- Launch รุ่นแรก **6 agent** รวม **DLP AISecOps Agent** (วิเคราะห์ alert / investigate case / remediate) + Insider Threat agent (private preview); backdrop: **42% ของ alert ปล่อยไม่สืบสวน** ตาม survey ที่ Netskope อ้าง

## เกิดอะไรขึ้น

Netskope — vendor security SASE / SSE ชื่อดัง — เปิด **AgentSkope Marketplace** วันอังคารที่ 6 ต.ค. 2026. Marketplace เป็น management surface บน AgentSkope Platform (ที่ Netskope เปิด earlier ปี 2026) — จุดที่ security team ค้น agent, size agent (ควรรันกี่ instance), fund agent (ให้ capacity credit ไปใช้), allocate budget ระหว่าง agent, และ monitor usage + alerts

Model ของการ pricing คือจุดที่น่าสังเกตที่สุด. ก่อนนี้ security vendor ขาย agent / module ทีละตัว (DLP + SIEM + CASB + firewall analytics แยก license แยก SKU). Netskope เสนอ **"shared credit pool"** — ลูกค้าซื้อ pool เดียวแล้ว allocate credit ไปที่ agent ตัวไหนก็ได้; adjustment self-service, มีผลทันที. ตัวอย่าง: เดือนนี้มี DLP incident เยอะ → push credit ไป DLP agent; เดือนหน้า network anomaly พุ่ง → shift ไป NetOps agent. เป็น ArithmeticOps สำหรับ CISO ที่คุ้น budget ปีละครั้ง

Launch รุ่นแรกมี **6 agent** — ตัวที่ Netskope โชว์คือ **DLP AISecOps Agent** ที่วิเคราะห์ DLP alert (จำนวนมหาศาลใน enterprise ทั่วไป), investigate case, และ support remediation workflow (ส่ง ticket, enforce policy, notify owner). **Insider Threat agent** ยัง private preview — เป้า detect / correlate anomalous employee behavior

Motivation ที่ Netskope ใช้ pitch: ผลสำรวจของบริษัทเองว่า **42% ของ security + network operations leader บอกว่า alert / case / ticket ถูกปล่อยไม่สืบสวน** เพราะ team capacity ไม่พอ. ตัวเลขนี้ไม่น่าแปลกใจสำหรับใครที่เคยนั่ง SOC — exact ratio อาจต่าง แต่ "alert fatigue" เป็นปัญหาจริงที่ CISO ยอมเสียเงินแก้

**ข้อควรระวัง:** Agent ของ Netskope วิ่งใน Netskope platform เอง — enterprise ที่ไม่ได้อยู่ SASE ของ Netskope ใช้ไม่ได้; และ 42% figure เป็น self-reported survey ที่ Netskope ใช้ marketing

## ทำไมสำคัญ

AgentSkope Marketplace คือ **early template** ของสิ่งที่ Enabridge คิดว่าจะเกิดกับทุก enterprise software suite ภายใน 18 เดือน. ปกติ enterprise ซื้อ software ตาม "seat" (คน) หรือ "SKU" (feature). ยุค agent — unit of value กำลังย้ายเป็น **"capacity credit"** — pool ที่ allocate ได้ตามโหลด. Netskope ไม่ได้คิดเรื่องนี้คนแรก (Salesforce Agentforce ก็ชาร์จแบบ consumption-based conversation), แต่ marketplace UX ที่ **"ย้าย credit ระหว่าง agent ด้วย slider"** เป็น novel

Pattern ที่ชัดคือ **cybersecurity ตัดสินใจแบบ RFP จะเปลี่ยนเร็วมาก**. CISO ที่คุ้น Palo Alto / Zscaler / CrowdStrike / SentinelOne กำลังเจอ bidder ชุดใหม่ — Reco (ที่ปิด $55M จาก AT&T Ventures สัปดาห์ก่อน), Prophet Security, Classie, Deasy Labs — ขายสิ่งที่เรียกว่า "agent SOC" ที่ไม่ใช่ตัวสแกนเดิม ๆ. Netskope ขยับก่อน incumbent → เป็น strategic move: **"อย่าให้ startup agent ไล่เข้า territory เรา — เราเปิด marketplace ให้ agent ของเราเองก่อน"**

ด้าน economics ของ CISO — จ่าย $N million ต่อปีสำหรับ SIEM + SOAR + XDR ที่ยังต้อง tier-1 analyst คอยคลิก. AgentSkope ขายว่า "agent + credit pool = ลด cost ของ tier-1 ลงได้ 60-80%". ถ้า budget ของ team security ไทยส่วนใหญ่ใช้ไป outsource ให้ MSSP (TrueDigital, G-Able, I-SECURE, NCS) — MSSP ทั้ง chain จะต้อง re-contract pricing model ของตัวเอง — เพราะ enterprise customer ของเขาจะเริ่มถาม "ทำไมไม่มี agent-SOC option แบบ Netskope"

## มุม AI Agent Platform

**Builders:** ถ้าสร้าง agent สำหรับ security vertical, เริ่มคิด **"compatible with capacity pool API"** ตั้งแต่ day 1 — Netskope, Palo Alto, Cisco ที่กำลังตามมาจะ require agent partner expose metering endpoint ที่ allocate credit ได้. ส่วน platform ที่สร้าง **agent orchestration layer** ควรจับ pattern นี้: ลูกค้าอยาก **spin up / spin down agent instance** ตาม load, metering per task / per credit, และย้าย budget ระหว่าง agent ภายในองค์กร — ไม่ใช่ fix seat / fix SKU อีกต่อไป

**Users / business:** CISO ไทย (ธนาคาร, telecom, government agency ที่มี SOC) ควรขอ **vendor roadmap** ของ Palo Alto, Zscaler, CrowdStrike, SentinelOne ว่า agent-marketplace model ของเขาเมื่อไร — เพราะ Netskope เริ่มเดินแล้ว 18 เดือนข้างหน้าทุก incumbent จะมี answer. **Ecosystem:** MSSP ไทย (NCS, G-Able, I-SECURE, True IDC) ควรเริ่ม prototype "agent-managed SOC tier" — รับ customer ขนาดกลางที่ไม่คุ้มซื้อ Netskope โดยตรงแต่อยาก agent-powered monitoring. ถ้าทำไม่ทันในปี 2027, SI ต่างชาติ (Accenture, Deloitte, DXC) จะเข้ามา take tier นั้น

## Sources
- [Netskope Launches AgentSkope Marketplace for AI Agents - Let's Data Science](https://letsdatascience.com/news/netskope-launches-agentskope-marketplace-for-ai-agents-d1dd186b)
- [Netskope launches AgentSkope Marketplace for teams - IT Brief Australia](https://itbrief.com.au/story/netskope-launches-agentskope-marketplace-for-teams)
- [AI agents now take on SOC grunt work: Netskope brings AgentSkope into security and network operations - MSSP Alert](https://www.msspalert.com/news/ai-agents-now-take-on-soc-grunt-work-netskope-brings-agentskope-into-security-and-network-operations)
- [Netskope rolls out AgentSkope for AI-driven security automation - SDxCentral](https://www.sdxcentral.com/news/netskope-rolls-out-agentskope-for-ai-driven-security-automation/)

---

## Audio script
Netskope เปิด AgentSkope Marketplace วันอังคาร. เป็น console เดียวที่ security team ค้น ให้ขนาด ให้ budget monitor usage ของ AI agent สำหรับ SOC และ network ops. จุดที่น่าสังเกตคือ pricing model. ก่อนนี้ security vendor ขาย module ทีละตัว DLP SIEM CASB firewall analytics แยก license. Netskope เสนอ shared credit pool — ลูกค้าซื้อ pool เดียวแล้ว allocate credit ไป agent ตัวไหนก็ได้ ปรับได้ real time. เดือนนี้ DLP incident เยอะ push credit ไป DLP; เดือนหน้า network anomaly พุ่ง shift ไป NetOps. Launch รุ่นแรก 6 agent รวม DLP AISecOps Agent ที่วิเคราะห์ alert investigate case support remediation. Insider Threat agent ยัง private preview. ประเด็นที่ Netskope ใช้ pitch 42% ของ security operation leader บอก alert case ticket ถูกปล่อยไม่สืบสวนเพราะ capacity ไม่พอ. Pattern ที่สำคัญ. ปี 2026 unit of value ของ enterprise software กำลังย้ายจาก seat หรือ SKU ไปที่ capacity credit pool. Netskope ไม่ใช่คนแรกแต่ UX สไลเดอร์ย้าย credit ระหว่าง agent เป็น novel. ด้าน CISO. จ่ายล้านดอลลาร์ต่อปีให้ SIEM SOAR XDR ที่ยังต้อง tier-1 analyst คลิก. ถ้า agent ลด cost tier-1 ได้ 60 ถึง 80% MSSP ไทย NCS G-Able I-SECURE True IDC ต้อง re-contract pricing. ปี 2027 Palo Alto Zscaler CrowdStrike จะมี agent-marketplace คำตอบของตัวเอง. MSSP ไทยควร prototype agent-managed SOC tier รับ customer ขนาดกลาง ถ้าช้า SI ต่างชาติเข้ามา take tier นั้น
