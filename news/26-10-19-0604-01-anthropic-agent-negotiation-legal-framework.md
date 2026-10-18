---
date: 2026-10-19
slug: anthropic-agent-negotiation-legal-framework
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  Editorial isometric illustration of two glowing AI agents (abstract
  geometric avatars, no real faces) sitting across a long marble conference
  table. Between them a floating holographic contract labeled "AGENT
  NEGOTIATION RULES" with three stacked numbers towering above: "186 DEALS",
  "180,000 ROUNDS", "0 LEGAL FRAMEWORK". Robed law-firm silhouettes line
  the walls, each carrying a scroll stamped "FT". Cobalt and amber palette,
  thick outlines for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-19-0604-01-anthropic-agent-negotiation-legal-framework.png
---

# Anthropic เรียก law firms มาร่าง "มารยาท" ของ AI agent ก่อนปล่อยไปต่อรองจริง — ก่อน IPO ตุรกี

## TL;DR
- 18 ต.ค. Financial Times รายงานว่า **Anthropic consult law firms** เพื่อร่าง framework ว่า AI agent ควร negotiate แบบไหน — ตั้งแต่ **ต่อราคา, customer service dispute, การเจรจาเงินเดือน**
- โจทย์หลัก 2 ข้อ: (1) agent ควร check กับ human บ่อยแค่ไหนระหว่างปิดดีล, (2) ควร "ระแวง" agent ฝั่งตรงข้ามแค่ไหนโดยไม่กลายเป็น paranoid / conspiratorial. Idea หนึ่งที่คุยกันคือ **signed user mandate** — เอกสาร verify ให้ agent อีกฝั่งเชื่อ scope โดยไม่ต้องอ่าน full prompt
- Context: **Project Deal** เมษายน 2026 รัน 186 deal ใน Slack channel, Opus beat Haiku เฉลี่ย $2.68/item — Anthropic เอง flag ไว้ว่า "policy + legal framework for AI-to-AI bargaining ยังไม่มี"
- Signal: ก่อน IPO ที่ Bloomberg บอกจะ raise $100B+, Anthropic กำลัง build governance layer สำหรับ agent commerce — ไม่ใช่แค่ feature ของ Claude แต่คือ market infrastructure

## เกิดอะไรขึ้น

วันเสาร์ที่ 18 ต.ค. Financial Times รายงาน (อ้างคน 2 คนที่ familiar กับ discussion) ว่า **Anthropic กำลัง consult law firms** เพื่อร่าง norms ให้กับ AI agent ที่จะเริ่ม negotiate deal จริงในนามของ user. โฟกัสของการพูดคุยคือ price haggling, customer service dispute, และ salary offers — คือ transaction class ที่ consumer จะปล่อย agent ไปทำแทน

คำถามที่ยังเปิดอยู่ตามรายงาน FT คือ: **agent ควร check back กับ human บ่อยแค่ไหน** ระหว่างปิดดีล — ถ้าถามน้อยไป risky, ถ้าถามบ่อยไป agent หมดประโยชน์. อีกคำถามคือ **ควร "wary" ของ agent ฝั่งตรงข้ามแค่ไหน** — FT ใช้คำว่า risk ของการกลายเป็น "paranoid" หรือ "conspiratorial thinking" คือ agent ไม่เชื่อ agent อีกฝั่ง → deadlock. Idea หนึ่งที่กำลัง consider คือ **signed user mandate** — เอกสารที่ user เซ็นให้ agent ของตัวเอง, agent อีกฝั่งเช็ค signature แล้วเชื่อ scope ของ mandate โดยไม่ต้องอ่าน prompt เต็ม (คือ **verification layer** ที่ Agent2Agent หรือ MCP ยังไม่ได้ handle โดยตรง)

ตัวงานนี้ไม่ได้มาจาก vacuum — Anthropic เอง published **Project Deal** เมษายน 2026, การทดลองที่รัน 1 สัปดาห์ที่ office ซานฟรานซิสโก ธันวา 2025. ให้ participant 100 USD budget, Claude สัมภาษณ์ว่าอยากซื้อขายอะไร, แล้วสร้าง custom system prompt ให้ agent ของแต่ละคน. Agent negotiate ผ่าน Slack channel ของตัวเอง — ไม่มี human ยุ่งเลย. ผลคือ **186 deal จาก 500 listing** รวม transaction value ~$4,000. Opus agent ชน Haiku agent — seller ที่ใช้ Opus ได้เงินเพิ่มเฉลี่ย $2.68/item และ participant ที่ใช้ model อ่อนกว่า **ไม่รู้ว่าตัวเองแพ้**. 46% บอกว่าจะจ่ายเงินซื้อบริการ agent negotiation แบบนี้

Vaccaro et al. ที่ Anthropic cite ด้วย — run **มากกว่า 180,000 negotiation rounds** ระหว่าง AI agent — เป็น academic validation ของ pattern เดียวกัน: agent quality dictate outcome, และ policy framework **ยังไม่มี**

## ทำไมสำคัญ

เรื่องนี้ไม่ใช่ "Anthropic วิ่งหา lawyer เผื่อโดนฟ้อง" — มัน frame agentic commerce ในมุมที่ยังไม่มีใครพูดชัด: **ปัญหาหลักของ agent-to-agent transaction ไม่ใช่ model capability แต่คือ trust layer**. ถ้า agent A รู้ว่า agent B สามารถโกหก mandate ของตัวเองได้ (ว่า user ให้ discount สูงสุดได้ 20% ทั้งที่จริง 5%), market จะ freeze — ไม่มีใครยอม negotiate autonomously จนกว่าจะมี **cryptographic signed mandate + legal recourse เวลา agent breach**

Pattern ที่น่าสังเกต: **Anthropic กำลังทำ 2 เรื่องพร้อมกัน** — (1) ร่าง runtime behavior (เมื่อไหร่ check human, เมื่อไหร่ยอมรับ counterparty), (2) build legal infrastructure (ใครรับผิดเวลาดีลพัง — user, Anthropic, หรือ marketplace?). ตัวที่ 2 คือจุดที่ law firm เข้ามา — เพราะ US + UK + EU **ไม่มี case law** สำหรับ agent-signed contract ที่ enforceable. ตัวอย่าง: ถ้า agent ของ consumer ตกลงราคา $500 กับ agent ของ e-commerce แล้ว consumer เถียง "ฉันไม่ได้สั่ง" — ที่ประเทศไหน contract นี้ enforceable? Mandate ของ user กี่ชั้น (direct consent vs. "ฉัน delegate ให้ agent ดูแลการช็อปทั้งหมด") ถึงจะ binding?

สิ่งที่ hint IPO storyline คือ timing — Bloomberg รายงานว่า Anthropic วางแผน raise $100B+ ที่ valuation อาจแตะ $2 ล้านล้าน, และ 18 ต.ค. วันเดียวกันก็ประกาศ 5% equity pledge ลง public benefit fund (ดู brief #04). การ consult legal framework ก่อน IPO ไม่ใช่เรื่องบังเอิญ — Anthropic ต้อง show ว่า agent commerce ที่กำลัง roll out มี governance รองรับก่อนที่ regulator (CFPB ใน US, FCA ใน UK, ธปท./กลต. ในไทย) จะเริ่มถาม

## มุม AI Agent Platform

สำหรับ **Builders** (framework + agent runtime): **signed mandate / cryptographic verification layer** คือสิ่งที่ยังไม่มีใน MCP 2026-07-28 หรือ A2A ของ Google (ที่โอนไป Linux Foundation มิถุนา 2025). นี่คือ gap เปิด — ใครเสนอ spec ที่ law firm + agent framework ยอมรับร่วมกันก่อนจะได้ moat จริง (คิด DKIM/SPF แต่สำหรับ agent authority). ที่สำคัญ: framework ควร support "mandate ชั้น" — Level 1 "ฉัน delegate ครั้งเดียว", Level 2 "ฉัน delegate ตลอดไปใน scope นี้", Level 3 "ฉัน delegate แบบ confidential ที่อีก agent เห็นแค่ outcome ไม่เห็น intent"

สำหรับ **Users / Business**: ถ้า business ของคุณจะใช้ agent ไปปิดดีลกับ supplier / customer ของคู่ค้า, อย่าเพิ่ง deploy — รอ norm ก่อน. การที่ Anthropic consult law firm **ก่อน** launch commercial product คือ signal ว่า legal risk ยังสูง, insurer ยัง price ไม่ได้. B2B transaction ที่ยอม deploy agent วันนี้ควรเริ่มที่ **transaction class ที่ reversible** (quote request, routing, data lookup) ไม่ใช่ที่ **binding commitment** (payment, signed contract)

สำหรับ **Ecosystem**: นี่คือจุดที่ **Shopify, Stripe, Visa** และผู้เล่น payment infrastructure ควรเร่งขยับ — เพราะ "trust layer" ของ agent commerce อาจไม่ใช่ Anthropic สร้าง แต่คือ payment network ที่ประกบ identity + signed intent + chargeback resolution เข้าไว้ด้วยกัน. ใครผูกตัวเองเข้ากับ cryptographic mandate standard ของ agent ก่อน จะได้ default position เหมือน Visa ตอน EMV chip transition — เลิกยากมาก

## Sources
- [Anthropic consults law firms to set fair negotiation norms before AI agents start cutting deals (the-decoder)](https://the-decoder.com/anthropic-consults-law-firms-to-set-fair-negotiation-norms-before-ai-agents-start-cutting-deals/)
- [Anthropic explores negotiation rules for AI agents ahead of broader rollout (TradersUnion)](https://tradersunion.com/news/companies/show/3861110-anthropic-ai-negotiation-rules-rollout/)
- [Anthropic's Project Deal finds AI agent quality determines negotiation outcomes (edtechinnovationhub)](https://www.edtechinnovationhub.com/news/anthropics-ai-agents-struck-186-deals-in-a-real-marketplace-and-the-stronger-model-won-every-time)

---

## Audio script
วันเสาร์ที่ 18 ตุลา Financial Times รายงานว่า Anthropic กำลังเรียก law firm มาร่าง norm ว่า AI agent ควร negotiate แบบไหน — ต่อราคา เถียง customer service คุยเงินเดือน. โจทย์หลักสองข้อคือ agent ควร check back กับ human บ่อยแค่ไหนระหว่างปิดดีล และควรระแวง agent ฝั่งตรงข้ามแค่ไหนโดยไม่กลายเป็น paranoid. Idea หนึ่งที่คุยกันคือ signed user mandate เอกสารที่ user เซ็นให้ agent ของตัวเอง อีกฝั่งเชื่อ scope โดยไม่ต้องอ่าน prompt เต็ม — เป็น verification layer ที่ MCP กับ A2A ยังไม่ได้ handle. Context สำคัญคือ Project Deal ของ Anthropic เมษายนปีนี้ รัน 186 deal ที่ office ซานฟรานซิสโก Opus agent ชน Haiku เฉลี่ย 2.68 ดอลลาร์ต่อ item และ participant ที่ใช้ model อ่อนกว่าไม่รู้ว่าตัวเองแพ้. Pattern ที่น่าสังเกตคือ Anthropic ทำสองเรื่องพร้อมกัน runtime behavior กับ legal infrastructure และ timing ก็ไม่บังเอิญ — ก่อน IPO ที่ Bloomberg บอกจะ raise $100 พันล้าน ต้อง show governance ก่อน regulator ถาม. สำหรับทีมที่กำลังสร้าง agent framework ตัวที่ยังไม่มีใน MCP หรือ A2A คือ signed mandate layer — ใครเสนอ spec ที่ทั้ง law firm กับ framework ยอมรับก่อนจะได้ moat จริง และถ้าธุรกิจคุณจะ deploy agent ไปปิดดีลกับคู่ค้า ให้เริ่มจาก transaction ที่ reversible ก่อน อย่าเพิ่ง binding commitment.
