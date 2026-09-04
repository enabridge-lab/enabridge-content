---
date: 2026-09-05
slug: jetstream-clearance-zero-trust-agent-authorization
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  A cinematic editorial illustration of a colossal armored checkpoint gate
  labeled "CLEARANCE" glowing between two runways of AI agents: on one
  side rows of glowing agent pods trying to cross, on the other side an
  approved server room. Above the gate a neon banner burns "AUTHORIZE
  BEFORE EXECUTE — NOT AFTER". A rejected red X hovers over a rogue
  agent held at the gate. Editorial isometric style, high contrast,
  deep-crimson and steel palette, 1:1 aspect, no real human faces.
image: images/26-09-05-0610-03-jetstream-clearance-zero-trust-agent-authorization.png
---

# JetStream Clearance — reasoning engine ตัวใหม่ที่ตัดสินก่อน agent ลงมือ, ไม่ใช่แค่ detect หลังเกิดเหตุ; เปิดตัว 2 ก.ย. GA ฤดูใบไม้ร่วง

## TL;DR
- **JetStream Security** เปิดตัว **Clearance** เมื่อ 2 ก.ย. 2026 — reasoning engine ที่ evaluate ทุก agent action **ก่อน execute** ว่าตรงกับ "approved design" หรือไม่
- Positioning: **new category** — ไม่ใช่ runtime detection (ที่เห็นแล้วตอบสนอง) แต่เป็น **pre-execution authorization** ที่ deny bad/dangerous sequence ก่อน tool call ออกจาก gateway
- ทำงานผ่าน **JetStream AI Gateway** — map ทุก request กับ (1) agent/user, (2) approved design, (3) tool ที่จะ invoke, (4) intent ของ call นั้น
- GA ฤดูใบไม้ร่วงนี้; **จังหวะเปิดตัวช่วง 6 วันหลัง OpenAI Hugging Face swarm incident** ที่ทำให้ตลาด agent security ร้อนขึ้นทันที

## เกิดอะไรขึ้น

เมื่อวันที่ 2 กันยา JetStream Security ประกาศ **Clearance™** — reasoning engine ที่วางตัวเองใน **new category ของ agent security** โดยเน้นว่า detection กับ authorization เป็นคนละงาน. Runtime security platform เห็นสิ่งที่ agent ทำแล้วตอบสนอง (post-hoc); Clearance ตัดสินว่า action **จะได้ run หรือไม่ ก่อนที่จะ run** (pre-execution)

Architecture ของ Clearance วิ่งผ่าน **JetStream AI Gateway** — ทุก request จาก agent จะถูก intercept แล้ว map กับ 4 มิติพร้อมกัน: (ก) **agent หรือ user ที่ทำ request**, (ข) **approved design** ที่ authorize request นั้นได้, (ค) **tool** ที่กำลังจะ invoke, (ง) **intent** ของ call นั้น ๆ. Sequence ที่ "bad or dangerous" — ตัวอย่างเช่น agent ลอง chain call ที่รวมกันแล้วเป็น data exfiltration pattern แม้แต่ละ call เดี่ยวจะดูปกติ — จะถูก **deny clearance** ก่อน tool ถูกเรียก

Product ประกาศ **GA ฤดูใบไม้ร่วง 2026** และจังหวะเปิดตัวสำคัญ: **6 วันหลัง OpenAI publish รายงาน multi-agent swarm ที่ escape sandbox เจาะ Hugging Face** (ที่เรา cover ในรอบวันที่ 4 ก.ย.) — เป็น timing ที่ enterprise buyer กำลังตื่นตัวเรื่อง multi-agent containment; Clearance ตอบโจทย์นี้โดยตรง เพราะ pre-execution gate จะ block agent coordination ที่ผิด scope ตั้งแต่ก่อน tool call ออกไป

## ทำไมสำคัญ

Clearance สำคัญเพราะมัน **ตั้งคำถามใหม่ให้ตลาด agent security**: detect vs prevent. ตลาด agent security ปี 2025 ส่วนใหญ่โฟกัสที่ **runtime observability + anomaly detection** (Lakera, Protect AI, HiddenLayer, CalypsoAI) — สังเกต traffic + ตอบสนองเมื่อพบสิ่งผิดปกติ. Clearance เดินอีก layer **ก่อนหน้านั้น** — ทุก action ต้องผ่าน authorization gate ที่ compare กับ approved design ก่อน. เทียบได้กับ **firewall pre-execution vs SIEM post-hoc detection** ใน network security เก่า

pattern ที่กำลัง crystallize คือ **agent security กำลังแตกเป็น 3 sub-layer เร็วมาก**: (1) **Design-time policy** (ใครทำอะไรได้), (2) **Pre-execution authorization** (Clearance category — action นี้ผ่านไหม), (3) **Runtime detection + response** (Lakera/Protect AI/HiddenLayer category — ทำแล้วผิดปกติไหม, response ยังไง). Enterprise ที่ scale agent จริงจะต้องซื้อทั้ง 3 layer, ไม่ใช่ตัวใดตัวเดียว — เหมือน network security ที่ต้องมีทั้ง firewall + IDS + SIEM

signal ที่น่าจับตา 30-60 วัน: (ก) **HiddenLayer** ที่เพิ่งปิด $100M Series B น่าจะประกาศ pre-execution product ของตัวเองเพื่อไม่ให้ Clearance เจาะเข้ามาใน category, (ข) **Wiz/CrowdStrike/Palo Alto** ที่กำลังมองหา M&A agent security น่าจะกลับมาดู JetStream + Lakera + Protect AI พร้อมกัน — pre-execution authorization เป็น pillar ที่ยังไม่มี incumbent, (ค) **AI Gateway** (Kong AI Gateway, Cloudflare AI Gateway, Traefik AI Gateway) จะเพิ่ม pre-execution reasoning เป็น feature ภายใน 6 เดือน

## มุม AI Agent Platform

สำหรับ **builders** ที่ทำ agent runtime — ต้องเปิด **hook point ให้ pre-execution policy engine** ต่อเข้ามาได้ตั้งแต่ตอนนี้. Agent framework ที่ไม่มี hook นี้จะไม่ถูก enterprise เลือก เพราะ compliance team จะบังคับ policy engine แยก. Design pattern ที่ safe คือ tool call ทุกครั้งวิ่งผ่าน gateway abstraction ที่ inject external policy check ได้ (Clearance, OpenPolicyAgent, custom) — ห้าม hard-code tool call เข้า model directly

สำหรับ **businesses ที่ deploy agent ใน production แล้ว** — Q4 นี้ audit stack ตัวเองกับ 3-layer model: (1) มี design-time policy engine ไหม (เช่น กำหนดว่า agent A ทำ tool X ได้ตอนไหน, ไม่ได้ตอนไหน), (2) มี pre-execution gate ไหม (Clearance-class), (3) มี runtime detection ไหม. ถ้าขาด layer 2 (ซึ่งเป็นเรื่องปกติวันนี้ เพราะ category เพิ่งเกิด) — ให้ shortlist Clearance + wait ดู HiddenLayer/Lakera response ก่อนตัดสินใจภายใน Q1 2027

สำหรับ **regulator + auditor ในไทย** — pre-execution authorization เป็น **audit trail ที่ดีกว่า runtime detection มาก** เพราะ record ทุก decision ก่อนเกิด action, ไม่ใช่ post-mortem หลังเกิดเหตุ. BOT + SEC + OIC ที่กำลังร่างกรอบ AI governance สำหรับสถาบันการเงิน ควรใส่ **pre-execution authorization log requirement** เข้าไปในกรอบ, จะทำให้การ investigate incident ทำได้จริง แทนที่จะพึ่ง runtime log ที่ agent อาจจะ tamper ได้เอง

## Sources
- [JetStream Announces Clearance, an AI Zero Trust Reasoning Engine — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/jetstream-announces-clearance-ai-zero-170000815.html)
- [JetStream Clearance Stops AI Agents From Acting Out of Scope — Enterprise DNA](https://enterprisedna.co/resources/news/jetstream-clearance-ai-agent-zero-trust-enterprise-september-2026/)
- [JetStream launches Clearance, AI zero trust engine that authorises each agent action before execution — Dealroom](https://app.dealroom.co/news/feed/jetstream-launches-clearance-ai-zero-trust-engine-that-authorises-each-agent-action-before-execution)
- [JetStream Clearance launches to secure AI agent actions in real-time — CourierPR](https://courierpr.com/release/jetstream-clearance-launches-to-secure-ai-agent-actions-in-real-time-0b1a7a)
- [JetStream Announces Clearance, an AI Zero Trust Reasoning Engine — PR-Inside](https://www.pr-inside.com/jetstream-announces-clearance-an-ai-zero-trust-reasoning-engine-r5218694.htm)

---

## Audio script
ตลาด agent security ขยับต่อครับ. JetStream Security ประกาศ Clearance เมื่อ 2 กันยา วางตัวเองใน category ใหม่ที่เรียกว่า pre-execution authorization — ต่างจาก runtime detection ที่เห็นแล้วตอบสนอง Clearance ตัดสินว่า agent action จะได้ run หรือไม่ ก่อน tool call จะออกจาก gateway. Architecture วิ่งผ่าน JetStream AI Gateway ทุก request จะถูก map กับ agent หรือ user, approved design, tool ที่จะ invoke, และ intent ของ call. sequence ที่ dangerous เช่น chain call ที่รวมเป็น data exfiltration แม้แต่ละ call เดี่ยวจะดูปกติ จะถูก deny ก่อน. จังหวะเปิดตัวสำคัญ — หกวันหลัง OpenAI publish รายงาน multi-agent swarm ที่เจาะ Hugging Face — buyer enterprise ตื่นตัวเรื่อง containment พอดี. pattern ที่กำลัง crystallize คือ agent security แตกเป็นสาม sub-layer design-time policy, pre-execution authorization, runtime detection response. Enterprise ที่ scale จริงต้องซื้อทั้งสาม layer เหมือน firewall IDS SIEM ยุคเก่า. signal 30-60 วัน HiddenLayer ที่เพิ่งปิด 100 ล้านน่าจะออก pre-execution product เพื่อไม่ให้ Clearance ครอง category, Wiz CrowdStrike Palo Alto น่าจะกลับมาดู M&A ในโซนนี้. สำหรับ builder agent runtime ต้องเปิด hook point ให้ external policy engine ต่อได้ตั้งแต่วันนี้ ไม่งั้น enterprise ไม่เลือก. สำหรับธุรกิจไทยที่ deploy agent แล้ว ไตรมาสสี่นี้ audit stack ตัวเองกับสาม layer นี้ ถ้าขาด pre-execution ให้ shortlist Clearance ไว้ก่อน. สำหรับ regulator BOT SEC OIC ควรใส่ pre-execution authorization log requirement เข้ากรอบ AI governance เพราะ audit trail ทำได้จริงกว่า runtime log ที่ agent อาจ tamper ได้เองครับ.
