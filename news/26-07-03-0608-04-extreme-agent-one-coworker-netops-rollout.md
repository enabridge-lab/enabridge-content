---
date: 2026-07-01
slug: extreme-agent-one-coworker-netops-rollout
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration: a glowing corporate network operations room seen
  from above. A translucent AI agent silhouette leans over the shoulder of
  a silhouetted NetOps engineer, pointing to floating alerts on a giant
  wallscreen — "WI-FI CONGESTION · AUTO-FIX APPLIED", "POS SLOWDOWN ·
  PRIORITIZED", "TICKET #7412 · RESOLVED". A bold overlay headline reads
  "AGENT ONE COWORKER — SHIPPED TO EVERY CUSTOMER". Extreme Networks
  wordmark at lower-right. Cinematic isometric tech-magazine style,
  deep navy and electric-purple palette, ultra-sharp text for 200px
  thumbnail readability, 1:1 aspect ratio, no real human faces.
image: images/26-07-03-0608-04-extreme-agent-one-coworker-netops-rollout.png
---

# Extreme Networks ปล่อย Agent ONE Coworker ให้ทุกลูกค้า Platform ONE แล้ว — autonomous NetOps เริ่ม 1 ก.ค.

## TL;DR
- 1 ก.ค. — Extreme Networks (NASDAQ: EXTR) rollout **Agent ONE Coworker** ไปยัง *ทุกลูกค้า Extreme Platform ONE* — ไม่ต้อง opt-in, ไม่ต้อง add-on subscription, ปุ่มเปิดใน console เดิม
- Coworker เป็น first tier ของ Agent ONE — conversational + real-time decisioning + "Nudge" (agent เสนอ action ให้ NetOps ก่อนที่ user จะ ถาม); tier ถัดไป **Agent ONE Operator** (autonomous, always-on) จะปล่อย Q4 2026
- POV — นี่คือ **first-at-scale rollout ของ agent สาย infrastructure** (ไม่ใช่ knowledge work): Extreme มีลูกค้าหลัก 60K globally, ปล่อย agent ให้ทั้ง base พร้อมกัน = สาม-สี่แสน NetOps engineer จะมี agent coworker ตั้งแต่วันแรก. Playbook นี้ต่างจาก SaaS ที่ให้ trial ก่อน — Extreme bake เข้า platform เดิมเลย

## เกิดอะไรขึ้น

1 กรกฎาคม 2026 — Extreme Networks เริ่ม rollout Agent ONE Coworker ให้ทุกลูกค้าที่ subscribe Extreme Platform ONE โดยไม่ต้องคุยเพิ่ม ไม่ต้อง license ใหม่. Coworker เป็น first tier ของ Agent ONE product line ที่บริษัทประกาศไปเมื่อ Extreme Connect '26 ต้นเดือน พ.ค. — ตอนนั้น timeline คือ "available Q3 2026" ซึ่งวันนี้คือวันแรกของ Q3

**Coworker ไม่ใช่ chatbot** — pitch ของ Extreme คือ agent ที่ทำงาน "alongside IT teams" ไม่ใช่รอ user prompt. Feature หลัก 4 กลุ่ม: (1) **Conversational access** ไปยัง network data + documentation + security insight (แทน dashboard เก่า), (2) **Automated support workflows** สร้าง case → investigate → resolve เอง, (3) **On-demand real-time dashboard** สร้าง view จาก live data ตามที่ NetOps ถาม, (4) **AI-driven Wi-Fi optimization** ผ่าน conversational control

จุดที่แตกต่างจาก AIOps เดิม (Cisco AI Assistant, Juniper Mist AI, HPE Aruba Central AI) คือ **"Nudge" capability** — agent เสนอ action ก่อนที่ NetOps จะถาม. ตัวอย่างที่ Extreme โชว์ในประกาศ — agent detect Wi-Fi congestion กำลังขึ้น → เสนอ config change ให้ NetOps approve หรือ auto-apply ตาม policy. หรือ detect POS system ในร้าน retail ช้าซ้ำ ๆ ตอน peak hour → เสนอ traffic prioritization rule. คือ pattern → nudge → action ในหลักวินาที

Nabil Bukhari, CTO และ President of AI Platforms ที่ Extreme กล่าวไว้ตอน launch ว่า "As networks begin to think, adapt, and act in real-time, the relationship between human users and AI agents will rapidly evolve". สิ่งที่ Extreme ทำต่างจาก Cisco / Juniper คือ **rollout to entire base ในวันเดียว** — ไม่ทำ pilot program, ไม่แบ่ง SKU. คิดว่า scale ของ deployment จะเป็น moat มากกว่า features. Next tier — Agent ONE Operator — จะปล่อย Q4 2026 เป็น always-on autonomous agent ที่ทำ task ตาม schedule + governance boundary โดยไม่ต้อง human ในลูป

## ทำไมสำคัญ

**Infrastructure agent — network, storage, database — คือ category ที่คนคาดว่าจะรอด longest ก่อน agent เข้ามา แต่กลับกลายเป็นที่แรกที่ deploy at scale**. Reason ชัด — (1) telemetry ในโลก network structured อยู่แล้ว (SNMP, syslog, NetFlow, RESTCONF), (2) action ที่ agent ต้องทำ well-defined (change VLAN, adjust QoS, reboot AP), (3) risk ประเมินง่ายเพราะ observable ทันที. เทียบกับ agent ที่ทำ knowledge work ที่ต้อง reason on messy human text — infrastructure agent มี clearer signal + clearer reward function

Pattern ที่เห็นในตลาด — **AIOps 2.0 กำลัง unfold**. Cisco Splunk AI Assistant ปล่อยธันวา, Juniper Mist AI agent (Marvis 2.0) ปล่อยมีนา, HPE Aruba GreenLake AI Assistant ปล่อยเมษา, และตอนนี้ Extreme Agent ONE. ทุกตัวมี pattern ร่วม — pre-installed with existing platform (ไม่ขาย standalone), integrate กับ existing management console, และ target **NetOps engineer shortage** ที่ Fortune 500 แบก. ตลาด global NetOps มี job vacancy 300K+ ที่หาคนไม่ได้ — agent ที่ทำ tier-1/tier-2 task คือทางออกที่ CIO เต็มใจ pay for

Signal ที่ agent platform builder ควรอ่านคือ — **"ship agent to install base" กำลังกลายเป็น distribution strategy default ในหลาย category**. Salesforce Agentforce ทำผ่าน Sales Cloud, ServiceNow Now Assist ทำผ่าน ITSM console, Oracle Fusion Studio ทำผ่าน SCM, Extreme Agent ONE ทำผ่าน Platform ONE. **ไม่มี vendor ไหน pitch agent เป็น standalone product แล้ว** — เพราะ integration friction สูงเกินไป, customer ไม่อยาก manage login/policy/data mapping สำหรับ agent แยกต่างหาก. Standalone agent startup (Sierra, Cognigy, Ada) ต้องเลือก vertical ที่ platform incumbent ยังไม่ครอบ ไม่งั้นถูก bundle out

## มุม AI Agent Platform

**Builders** — ถ้า agent framework ของคุณ target NetOps / DevOps / SRE / SysAdmin ต้องคิดใหม่. Model "developer signs up โดย product" ตายเพราะ Fortune 500 ห้าม developer ติดตั้ง third-party agent ที่มี network access. Path เดียวที่เหลือคือ (1) OEM ผ่าน network vendor (partner กับ Cisco / Juniper / HPE / Extreme), (2) sell ผ่าน hyperscaler (AWS Marketplace, Azure Marketplace), หรือ (3) เจาะ mid-market ที่ไม่มี Fortune 500 procurement barrier. Kentik, ThousandEyes, Datadog Network Monitoring กำลัง reposition รอบ agent — ตัวไหน slow จะโดน bundle

**Users / business** ที่รัน Extreme network infrastructure (retail chain, hotel chain, K-12 school, hospital system) — Coworker เข้ามาผ่าน console เดิมโดยไม่ต้อง change vendor contract, แต่ CISO ต้องเช็ค 2 เรื่อง: (1) telemetry ที่ agent อ่านมี PII ไหม (Wi-Fi client MAC address, session data), (2) auto-apply action ต้อง configure boundary ให้ชัด (VLAN change ok, ACL rule change ต้อง approve). Retail Thai (CPN, Central Retail) และ hotel Thai (Minor, Centara) ที่ใช้ Extreme Wi-Fi 6E — เปิด Coworker ทดสอบใน 1-2 store ก่อน expand, ROI ที่ track ได้ทันทีคือ mean-time-to-resolution ของ NetOps ticket

## Sources
- [Introducing Extreme Agent ONE — Extreme Networks Investor Relations](https://investor.extremenetworks.com/news/news-details/2026/Introducing-Extreme-Agent-ONE-A-Smarter-Faster-Autonomous-Approach-to-Enterprise-Networking/default.aspx)
- [Extreme Connect 26: Agent ONE takes forward network AI — Computer Weekly](https://www.computerweekly.com/news/366642566/Extreme-Connect-26-Agent-ONE-takes-forward-network-AI)
- [Introducing Extreme Agent ONE™ — Built Different — Extreme Networks Blog](https://www.extremenetworks.com/resources/blogs/introducing-extreme-agent-one-built-different)
- [Extreme Networks moves beyond AI chatbots for network operations — Fierce Network](https://www.fierce-network.com/broadband/extreme-networks-moves-beyond-ai-chatbots-network-operations)
- [Extreme Connect 2026: Agentic AI, Platform ONE and the next phase of enterprise networking — SiliconANGLE](https://siliconangle.com/2026/05/06/extreme-connect-2026-agentic-ai-platform-one-next-phase-enterprise-networking/)

---

## Audio script

วันที่หนึ่งกรกฎาคม Extreme Networks เริ่ม rollout Agent ONE Coworker ไปยังทุกลูกค้า Platform ONE โดยไม่ต้อง opt-in ไม่ต้องซื้อ subscription เพิ่ม แค่เปิดปุ่มใน console เดิม. Coworker คือ tier แรกของ Agent ONE ที่บริษัทประกาศตอน Extreme Connect ต้นพฤษภาคม timeline คือ Q3 2026 วันนี้คือวันแรกของ Q3 พอดี.

Coworker ไม่ใช่ chatbot — pitch คือ agent ที่ทำงาน alongside IT team ไม่รอ prompt. Feature หลักสี่กลุ่ม conversational access ไป network data, automated support workflow สร้าง case ตัด case จบเอง, real-time dashboard สร้าง view จาก live data, และ AI Wi-Fi optimization ผ่าน conversational control. จุดต่างจาก AIOps เดิมคือ Nudge — agent เสนอ action ก่อน user ถาม detect Wi-Fi congestion แล้ว nudge config change หรือเห็น POS ช้าซ้ำ ๆ ตอน peak แล้ว nudge traffic priority rule.

Insight คือ infrastructure agent กลับกลายเป็น category ที่ deploy at scale ก่อน knowledge agent ทั้งที่คนคิดว่าจะรอดนาน — เพราะ telemetry structured อยู่แล้ว action well-defined risk observable. AIOps 2.0 กำลัง unfold Cisco Juniper HPE Extreme ทุกเจ้าปล่อย agent ผ่าน platform เดิม ไม่ขาย standalone.

Pattern ที่ builder ต้องอ่าน — ship agent ไป install base กลายเป็น distribution default ในหลาย category. Salesforce ผ่าน Sales Cloud ServiceNow ผ่าน ITSM Oracle ผ่าน SCM Extreme ผ่าน Platform ONE. ไม่มี vendor ไหน pitch agent เป็น standalone แล้วเพราะ integration friction สูง customer ไม่อยาก manage login policy data mapping สำหรับ agent แยก. ฝั่งไทย retail chain hotel chain ที่ใช้ Extreme Wi-Fi 6E ทดสอบ Coworker ใน 1-2 สาขาก่อน expand ROI ที่ track ได้ทันทีคือ mean time to resolution ของ NetOps ticket.
