---
date: 2026-05-02
slug: 26-05-02-0624-04-sierra-ghostwriter-fragment-agent-builds-agent
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: Editorial illustration of a hand sketching a stick figure on paper, and the stick figure stepping out of the page fully formed and walking into a city of glowing buildings, minimal flat shapes, soft cream and electric purple palette, dramatic side lighting, no text no logos no faces
image:
---

# Sierra ปล่อย Ghostwriter — agent ที่สร้าง agent อื่นด้วยภาษาธรรมชาติ + ซื้อ Fragment เป็นการ acquire ครั้งที่ 3 ในปีนี้: Bret Taylor เดิมพัน "ยุคปุ่มหมดแล้ว"

## TL;DR
- 10 เม.ย. — Sierra เปิด **Ghostwriter** ตัวที่ build + deploy agent อื่นจาก natural language description = **"meta-agent"** ที่ user ไม่ต้องเขียน prompt/flow เอง บอกแค่ "ฉันต้องการ agent ทำ X" → ได้ agent พร้อมใช้
- 23-24 เม.ย. — Sierra ซื้อ **Fragment** (YC-backed, French) ตัวที่ 3 ในปีนี้ ต่อจาก Opera Tech (ญี่ปุ่น) + Receptive AI (voice agent) — pattern: **acquire เร็วเพื่อ stack vertical knowledge**
- ARR แตะ **$150M+**, valuation $10B, voice agent surpass text เป็น primary channel; CEO Bret Taylor: "**era of clicking buttons is over**"

## เกิดอะไรขึ้น

วันที่ 10 เม.ย. Sierra (ก่อตั้งโดย Bret Taylor อดีต CTO Facebook + co-CEO Salesforce + chair OpenAI board) เปิด **Ghostwriter** — feature ที่อยู่บน Sierra agent platform แล้วทำหน้าที่ "agent ที่สร้าง agent" user พูด natural language ว่า "ฉันต้องการ agent ที่จัด refund สำหรับลูกค้าที่ติดต่อมา 2 ครั้งใน 7 วัน" หรือ "agent ที่ติดตาม invoice ค้าง 30+ วันแล้วส่ง follow-up อัตโนมัติ" → Ghostwriter generate spec, deploy agent, ติดตั้ง integration กับ system เดิม (Salesforce, Zendesk, Slack), เริ่ม shadow mode อัตโนมัติให้ human review สัปดาห์แรก แล้วค่อยให้รัน autonomous

จากนั้น 23-24 เม.ย. Sierra ประกาศซื้อ **Fragment** (Y Combinator-backed startup ฝรั่งเศส) ที่ขายเครื่องมือ integrate AI เข้า workflow business — มูลค่าดีลไม่เปิดเผย เป็นการ acquire ครั้งที่ 3 ในปีนี้ของ Sierra (Q1 26: ซื้อ Opera Tech ญี่ปุ่นที่ทำ enterprise AI; Q1 26: ซื้อ Receptive AI ที่ทำ voice agent; Q2 26: Fragment) — pattern ของ Sierra ต่างจากบริษัทใหญ่อื่น: **acquire vertical/regional expertise + integration plumbing แทน build เอง** — ผลลัพธ์คือ Sierra ขยาย footprint ใน Japan + EU + US ใน 6 เดือนโดยไม่ต้อง hire local team จาก scratch

ตัวเลขปัจจุบัน Sierra: ARR **$150M+** (จาก $100M ตอน พ.ย. 2025 = +50% ใน 5 เดือน), valuation **$10B**, ลูกค้าระดับ Fortune 500 ส่วนมากใน customer service/support, voice agent ตอนนี้ surpass text เป็น **primary channel** processed (Sierra อ้างว่า "hundreds of millions of voice calls per year") พร้อมกัน Bret Taylor ไปขึ้นเวทีให้สัมภาษณ์ Stratechery และ The Information ปลาย เม.ย. ประกาศ thesis ใหม่: "**era of clicking buttons is over** — software ที่ดีที่สุดในยุคหน้าไม่มี UI ปกติ มีแต่ agent ที่คุยภาษาธรรมชาติแล้วทำ task ให้" Sierra position ตัวเองเป็น **language-driven software platform** ไม่ใช่แค่ customer service agent vendor

## ทำไมสำคัญ

**"Agent ที่สร้าง agent" = abstraction ใหม่ที่จะ shift entire build motion** ที่ Cloudflare ทำใน Code Mode คือ "agent กดทำงานในโค้ด" — Sierra ทำตำแหน่งสูงขึ้นไปอีก: "user สั่งสร้าง agent ด้วย natural language" Glean เปิด autonomous agent builder ตอน ธ.ค. 2025; Salesforce Agentforce Builder + Bedrock Agent Studio + Microsoft Copilot Studio ทุกค่ายมี "agent builder" แต่ส่วนใหญ่ยัง require user เลือก trigger, mapping, prompt — Ghostwriter ของ Sierra ไม่มี — แค่ describe ภาษาคน → agent มา (อย่างน้อย Sierra อ้างเช่นนั้น) ถ้า delivery ตรงกับ marketing นี่จะเป็น "Cursor moment" ของ enterprise agent ที่ผู้ไม่เป็น engineer build agent ได้

**Acquisition strategy ของ Sierra = signal ของ vertical knowledge moat** Bret Taylor เป็นคนที่ understand market timing — ที่ Salesforce ปี 2018-2020 acquire Quip, MuleSoft, Tableau ที่จุดที่ "AI/integration/data viz" จะ commodity; ตอนนี้ acquire vertical AI startup (Opera Tech ญี่ปุ่น = enterprise process; Receptive AI = voice; Fragment = workflow integration) signal ที่ส่ง: **moat ของ agent ไม่ใช่ model หรือ infrastructure แต่เป็น vertical workflow knowledge + regional integration depth** — เหมือน Avoca ($1B valuation) ที่เราเขียนใน 04-30 brief ที่ moat คือ vertical knowledge ของช่างประปา/HVAC ไม่ใช่ model

**Voice surpass text** = pattern ที่ทุก agent vendor (Sierra, Decagon, Avoca, Cresta) ยืนยันใน Q1 2026 — สำหรับ customer service voice calls 60-80% ของ volume + ค่าใช้จ่ายต่อ minute ลดจาก $0.50-1.50 (human) เป็น $0.05-0.10 (voice agent) **economic gap คือ 10-30x** ที่จุด ARR $150M Sierra ประมวลการ "hundreds of millions of voice calls per year" หมายความว่า process volume ของ Sierra > big-bank call center bigger than JPMorgan retail support — เป็น scale ที่ enterprise vendor ไม่เคยถึงในเวลาน้อยขนาดนี้ (Sierra ก่อตั้งปี 2023 — < 3 ปี)

## มุม OpenBridge

**Path ที่ OpenBridge ห้ามเดิน: build "agent builder" generic แข่ง Sierra/Glean/Salesforce** ตลาด generic agent builder จะถูกครอง 3 รายในรอบ 12 เดือน (Sierra Ghostwriter + Salesforce Agentforce Builder + Microsoft Copilot Studio) — OpenBridge ที่ build generic agent builder = แข่งกับ vendor ที่มี $1.4B+ ARR + brand established ลูกค้าจะไม่เลือก OpenBridge แม้ feature parity

**Path ที่ OpenBridge ควรเดิน: vertical-specific agent factory ที่ใช้ Ghostwriter pattern แต่จำกัด vertical** เช่น:
- "**Thai AP/AR agent factory**" — user upload chart of accounts + sample invoice → ได้ agent ทำ AP/AR ที่เข้าใจ VAT 7%, withholding tax, e-tax invoice
- "**Customs declaration agent factory**" — user describe shipping pattern + product → ได้ agent ที่ filing customs ผ่าน NSW + DOC system อัตโนมัติ
- "**Thai BoT/SEC compliance agent factory**" — user describe entity type + regulatory class → ได้ agent ที่ generate quarterly filing draft

**ใช้ Sierra acquisition pattern เป็น playbook** ใน 24 เดือน OpenBridge มี option acquire 1-2 เล็ก ๆ ที่มี vertical domain expertise (e.g. ผู้ขาย software AP/AR ขนาด <$2M ARR ที่กำลัง decline เพราะไม่มี AI strategy) — buy team + customer + domain knowledge แทน build organically; Bret Taylor ทำ playbook นี้แล้วใน 4 เดือน scale Sierra ใน 3 ภูมิภาค OpenBridge ใช้ same pattern ได้ใน ASEAN ที่มี startup vertical software เก่าแก่ที่ valuation ตก

**Voice channel = ต้องวางใน roadmap ภายใน 60 วัน** ทุก agent vendor ระดับโลก voice surpass text ใน Q1 26 — OpenBridge ที่ยังเน้น chat/text agent อย่างเดียวจะ miss 60-80% ของ enterprise volume ในไทยที่ลูกค้ายังโทรเป็นหลัก partner กับ Vapi/ElevenLabs Thai/Looloo สำหรับ voice infra + ส่วน OpenBridge focus ที่ workflow + integration layer

## Sources
- [Bret Taylor's Sierra buys YC-backed AI startup Fragment | TechCrunch](https://techcrunch.com/2026/04/23/bret-taylors-sierra-buys-yc-backed-ai-startup-fragment/)
- [Sierra Advances AI Agent Model with Ghostwriter as Bret Taylor Signals Shift to Language-Driven Software | The AI Insider](https://theaiinsider.tech/2026/04/10/sierra-advances-ai-agent-model-with-ghostwriter-as-bret-taylor-signals-shift-to-language-driven-software/)
- [Bret Taylor's Sierra Acquires French AI Startup Fragment in Third Deal This Year | The AI Insider](https://theaiinsider.tech/2026/04/24/bret-taylors-sierra-acquires-french-ai-startup-fragment-in-third-deal-this-year/)
- [Sierra AI at $10B Valuation: The Enterprise Voice Agent That's Redefining Customer Service | AgentMarketCap](https://agentmarketcap.ai/blog/2026/04/06/sierra-ai-10b-valuation-enterprise-voice-agent-customer-service)
- [Sierra revenue, valuation & funding | Sacra](https://sacra.com/c/sierra/)

---

## Audio script
Sierra ของ Bret Taylor — อดีต CTO Facebook, co-CEO Salesforce, chair OpenAI board — เคลื่อน 2 step ใหญ่ในเดือน เม.ย. step แรก 10 เม.ย. ปล่อย Ghostwriter ตัวที่เป็น meta-agent — agent ที่ build agent อื่นจาก natural language description แทนที่จะเขียน prompt หรือ flow เอง user แค่บอก "ฉันต้องการ agent จัด refund ลูกค้าติดต่อ 2 ครั้งใน 7 วัน" → Ghostwriter generate spec, deploy agent, ตั้ง integration, เริ่ม shadow mode สัปดาห์แรก step สอง 23 เม.ย. Sierra ซื้อ Fragment สตาร์ทอัพฝรั่งเศสจาก YC เป็นการ acquire ครั้งที่ 3 ในปีนี้ ก่อนหน้านี้ซื้อ Opera Tech ที่ญี่ปุ่น + Receptive AI ที่ทำ voice ตัวเลข Sierra ตอนนี้ ARR 150 ล้านดอลลาร์ +50% ใน 5 เดือน, valuation 10 พันล้าน, voice surpass text เป็น primary channel processed Bret Taylor ขึ้นเวที Stratechery บอก "era of clicking buttons is over" software ในยุคหน้าไม่มี UI ปกติ มีแต่ agent ที่คุยภาษาคนแล้วทำ task ให้ สำหรับ OpenBridge — path ที่ห้ามเดิน คือ build generic agent builder แข่ง Sierra/Salesforce/Microsoft จะแพ้แน่ path ที่ควรเดิน คือ vertical-specific agent factory เช่น Thai AP/AR factory ที่เข้าใจ VAT 7% + withholding tax, customs declaration factory ที่ filing ผ่าน NSW อัตโนมัติ, BoT/SEC compliance agent factory และอย่าลืม voice — ทุก vendor ระดับโลก voice surpass text ใน Q1 ถ้า OpenBridge ยังเน้น text อย่างเดียวจะ miss 60-80% ของ enterprise volume ในไทย partner กับ Vapi, ElevenLabs Thai, Looloo สำหรับ voice infra ภายใน 60 วันครับ
