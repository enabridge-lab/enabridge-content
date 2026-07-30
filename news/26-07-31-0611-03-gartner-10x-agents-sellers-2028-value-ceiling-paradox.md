---
date: 2026-07-31
slug: gartner-10x-agents-sellers-2028-value-ceiling-paradox
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial illustration of a vast auditorium filled with rows of small identical agent silhouettes
  (ten to one ratio) sitting in shadow, and one lone human sales rep silhouette standing at a podium
  in a spotlight. Above the crowd floats a translucent glowing ceiling labeled "VALUE CEILING",
  with a bold percent tag "<40% PRODUCTIVITY GAIN" and a small "10:1 by 2028" tag. Muted teal and
  ember palette, flat editorial style, dramatic contrast. 1:1 aspect. No real human faces
  (silhouettes only). Text must render sharply at 200px thumbnail.
image: images/26-07-31-0611-03-gartner-10x-agents-sellers-2028-value-ceiling-paradox.png
---

# Gartner: agent จะ outnumber sales rep 10:1 ปี 2028 — แต่ <40% ของ seller บอกว่า agent เพิ่ม productivity

## TL;DR
- **28 ก.ค.** — Gartner press: **AI agent จะ outnumber seller 10 ต่อ 1 ภายในปี 2028**; แต่ paradox — **<40% ของ seller จะรายงานว่า agent ช่วยเพิ่ม productivity**
- Dan Gottlieb (VP Analyst, Gartner Sales practice) เรียกว่า **"value ceiling"** — เกิดจาก data foundation อ่อน, workflow integration ไม่ครบ, seller experience แย่
- Melissa Hilbert (VP Analyst) เสริม: *"AI agents are everywhere, but there's a value ceiling. Beyond a certain point, more AI does not mean more productivity"*
- Context: pair กับ Gartner's forecast ก่อนหน้า (Q2) — Fortune 500 average จะ operate **150,000+ agent** ภายในปี 2028 (จาก <15 ในปี 2025); แต่ **only 13% ขององค์กรมี governance ที่พอ** — agent sprawl gap ที่ Hush + Encore + Netzilo กำลัง sell into

## เกิดอะไรขึ้น

Gartner press release วันที่ 28 ก.ค. ที่ถูก re-issue จาก Q4 2025 pattern (Gartner ทำ 2 รอบต่อปี) — คราวนี้ปรับตัวเลขให้ update. Core prediction: **ภายในปี 2028, AI agent จะ outnumber human seller ในสัดส่วน 10 ต่อ 1** ในองค์กร B2B sales. Baseline ปัจจุบัน = **<1 agent per seller** (H1 2026 survey). Pattern แบบเดียวกับที่ Fortune 500 forecast ก่อนหน้า — จาก <15 agent per company ในปี 2025 ไป 150,000+ ในปี 2028 — เกิดจาก **each seller จะ orchestrate agent team ของตัวเอง** (research, prospecting, follow-up, forecast, deal desk)

แต่ paradox ที่ press release highlight ตัวหนา: **<40% ของ seller จะรายงานว่า AI agent ช่วยเพิ่ม productivity ของตัวเอง**. Dan Gottlieb (VP Analyst ใน Gartner Sales practice) ให้ interpretation ว่า **"value ceiling"** — เกิดจาก 3 สาเหตุที่ compound กัน:
- **Data foundation อ่อน** — agent ไม่มี access CRM ที่ clean, contact record ที่ enriched, pipeline history ที่ structured; ผลคือ agent ใช้ prompt engineering compensate = ผลผลิต generic
- **Workflow integration ไม่ครบ** — agent standalone ที่ไม่ hook เข้า Salesforce/HubSpot/Outlook/Teams = seller ต้อง copy-paste context เข้า/ออก; productivity loss ใน context switching หักลบ output gain
- **Seller experience แย่** — agent ที่ interrupt, over-notify, บังคับ workflow ที่ seller ไม่ชอบ — เจอ resistance + shelfware effect ภายใน 6-9 เดือน

Melissa Hilbert (VP Analyst เดียวกัน) เสริม quote ที่จะกลาย mantra ของปี 2027: **"AI agents are everywhere, but there's a value ceiling. Beyond a certain point, more AI does not mean more productivity."** ในภาษา CFO = **agent ROI curve จะแบนก่อนที่ agent volume จะ peak** — ที่ทำให้ vendor ที่ขาย volume-based (seat + token) ตกในกับดัก over-provisioning; vendor ที่ขาย outcome-based (Salesforce Agentforce Help Agent $2/resolution, Encore's revenue-share) จะ align incentive กับ buyer ดีกว่า

Zoom out: Gartner press ตัวเดียวกัน (28 ก.ค.) ต่อยอด forecast ที่ปล่อยเดือน เม.ย. — **average Fortune 500 company จะ operate 150,000+ agent ภายในปี 2028** (จาก <15 ในปี 2025) — ที่ Max Goss (senior director analyst) เตือน "agent sprawl" ที่ **only 13% ขององค์กรมี governance ที่พอ**. ทั้งสอง number pair กันชัด — **agent จำนวนเยอะขึ้น 10,000x แต่ organizational readiness เพิ่มแค่ marginal** = ช่องว่างที่ SaaS category ใหม่ (Hush's identity registry, Alterion's observability, Netzilo's runtime governance) กำลัง sell into

## ทำไมสำคัญ

**"Value ceiling" คือคำที่ CFO Q3-Q4 2026 จะเริ่มใช้เยอะ** — เพราะ agent budget ปี 2026 พุ่งจาก 1-2% ของ IT budget เป็น 5-8% (Gartner CIO survey Q2 2026), แต่ productivity gain ที่พิสูจน์ได้ยังไม่ commensurate. CFO ที่เคย sign off "agent trial" ปี 2025 จะเริ่มถาม hard question ปี 2026 Q4 — *"where's the productivity number?"*. ถ้า vendor ตอบไม่ได้ = **agent budget freeze** หรือ **shift ไป outcome-based contract only** (คู่กับ Salesforce Agentforce Help Agent $2/resolution ที่ Enabridge cover เมื่อวาน)

**Root cause = 3 ปัญหาที่ 3 SaaS category ใหม่กำลังแก้**:
- *Data foundation* → **agent-native data platform** (Snowflake Cortex, Databricks Agent Bricks, Palantir Foundry AIP; และ startup เช่น Instabase, Rox AI)
- *Workflow integration* → **agent identity + orchestration** (Hush registry + Cognizant EMEA + Anthropic Premier services layer + Netzilo runtime governance)
- *Seller experience* → **outcome-based UX + revenue attribution** (Encore's Interaction Mining, Regal.io voice, Vivun sales agent, Salesforce Agentforce Help Agent)

Vendor ที่ solve ปัญหาใดปัญหาหนึ่ง = grow moderate. Vendor ที่ **bundle 2-3 layer** = premium multiple ที่ Sequoia/Khosla/Index กำลัง bet. Enabridge เห็น pattern นี้ชัดในรอบสัปดาห์ที่ผ่านมา — Cognizant EMEA (workflow+services), Hush (identity), Encore (outcome), Salesforce Agentforce (outcome+platform), Anthropic Premier services layer (data+workflow) — ทุกเจ้ากำลัง converge บน "value ceiling" กันหมด

**Signal ที่ต้องตาม Q3-Q4 2026:** (1) *Vendor ไหนจะ publish "productivity ROI benchmark"?* — Salesforce มี 70% autonomous rate; Microsoft ยังไม่ publish agent-specific ROI; Google Vertex AI Agent Builder silent; Anthropic ยังไม่มี. Vendor แรกที่ publish credible ROI = grab attention CIO/CFO; (2) *Analyst ที่กลายเสียง trusted?* — Gartner Dan Gottlieb + Melissa Hilbert + Max Goss กำลัง set narrative "agent = value ceiling"; Forrester ตามหลัง; IDC ยังไม่มี agent-specific practice ที่แข็ง; (3) *ตัวเลข "10:1 by 2028" จะ trigger CIO ยังไง?* — ถ้า 10 agent per seller = ต้อง orchestration layer, ต้อง identity per agent, ต้อง cost tracking per agent — **RFP Q4 2026 ต้องมี clause เหล่านี้เป็น mandatory**

## มุม AI Agent Platform

**สำหรับ builders (agent app ในไทย/SEA):** ถ้า target sales/service vertical, **อย่าขาย agent stand-alone** — ขาย **agent + data foundation + workflow integration** เป็น bundle. Case ที่ prove value ceiling ผิด = agent ที่ (1) sit inside CRM (ไม่ standalone), (2) ingest structured pipeline data (ไม่ prompt-only), (3) instrument outcome tracking (revenue attribution ต่อ agent action). ตัวอย่าง Thai vertical ที่ window เปิด: **Thai insurance agent (AIA, Muang Thai, FWD), Thai bank RM (SCB, K-Bank, KBank private banking), Thai property agent (SC Asset, AP, Sansiri, Origin)** — customer base ที่ CRM ยัง fragmented, workflow integration ยังไม่ solved, seller experience ยัง painful

**สำหรับ users/business (Fortune 500 + Thai SET50):** ถ้า evaluating agent vendor ปี 2026 Q4, ต้อง **แยก 3 metric ที่ vendor ต้อง commit**:
1. **Productivity metric ที่ measurable** — hours saved per week per seller, deals moved to close per month, revenue per contact enriched (ไม่ใช่ "hours interacted with AI")
2. **Value ceiling proof point** — vendor ต้อง show real customer ที่ productivity plateau ที่ระดับไหน (Salesforce dogfooding 70% autonomous rate = benchmark ที่ transparent)
3. **Failure mode explanation** — vendor ต้อง explain ว่า agent ไม่ทำอะไรได้บ้าง (ไม่ hallucinate confident); เอา limitation ขึ้นหน้าคือ trust signal

**สำหรับ ecosystem (Thai SI + ISV):** window เปิด 12-18 เดือนสำหรับ **"agent value engineering" service** — คล้าย Six Sigma consultant ปี 1990s แต่ focus ที่ agent workflow ROI. Bluebik/G-Able/Accenture SEA/Deloitte Thailand ที่ position "agent value optimization" — audit deployment, ระบุ value ceiling, prescribe integration + data foundation fix — จะ premium price สูงกว่า generic AI advisory. Framework ที่ Gartner + McKinsey จะ publish ปี Q1 2027 = template ที่ SI ต้อง productize ก่อน

## Sources
- [Gartner Predicts AI Agents Will Outnumber Sellers 10 to 1 by 2028, Yet Fewer Than 40% of Sellers Will Say Agents Improved Productivity — Gartner Newsroom (July 28, 2026)](https://www.gartner.com/en/newsroom/press-releases/2026-07-28-gartner-predicts-ai-agents-will-outnumber-sellers-10-to-1-by-2028-yet-fewer-than-40-percent-of-sellers-will-say-agents-improved-productivity)
- [Gartner Identifies Six Steps to Manage AI Agent Sprawl — Gartner Newsroom (April 28, 2026)](https://www.gartner.com/en/newsroom/press-releases/2026-04-28-gartner-identifies-six-steps-to-manage-artificial-intelligence-agent-sprawl)
- [Gartner sees untamed growth in agentic AI — Computerworld](https://www.computerworld.com/article/4165686/gartner-sees-untamed-growth-in-agentic-ai.html)
- [By 2028 AI agents will outnumber sellers tenfold — International Journal Of Sales Transformation](https://www.journalofsalestransformation.com/by-2028-ai-agents-will-outnumber-sellers-tenfold-gartner/)

---

## Audio script
เช้านี้อีกเรื่องที่ทุก sales leader ต้องได้ยิน. Gartner ปล่อย press release วันที่ 28. AI agent จะ outnumber sales rep 10 ต่อ 1 ภายในปี 2028. แต่ paradox ที่หัวข้อเน้น. น้อยกว่า 40% ของ seller จะรายงานว่า agent ช่วยเพิ่ม productivity.

Dan Gottlieb VP Analyst ใน Gartner Sales practice เรียก paradox นี้ว่า value ceiling. 3 สาเหตุ. Data foundation อ่อน. Workflow integration ไม่ครบ. Seller experience แย่. Melissa Hilbert เสริม quote ที่จะกลาย mantra. AI agents are everywhere but there is a value ceiling. Beyond a certain point more AI does not mean more productivity.

Zoom out. Gartner ยังยืน forecast Fortune 500 average จะ operate 150,000 agent ภายในปี 2028 จาก 15 ในปี 2025. แต่ only 13% ขององค์กรมี governance ที่พอ. ตัวเลข 2 ตัวนี้ pair กัน. Agent เพิ่ม 10,000 เท่า แต่ organizational readiness เพิ่ม marginal.

Implication. CFO Q4 2026 จะเริ่มถาม hard question. Where is the productivity number. Vendor ที่ตอบไม่ได้ agent budget freeze หรือ shift ไป outcome-based contract only. Pair กับ Salesforce Agentforce $2 per resolution ที่ Enabridge cover เมื่อวาน. Pattern ชัด.

Root cause 3 ปัญหาที่ 3 SaaS category ใหม่กำลังแก้. Data foundation snowflake cortex Databricks agent bricks Palantir Foundry. Workflow integration Hush registry Cognizant EMEA Anthropic Premier layer. Seller experience Encore Interaction Mining Salesforce Agentforce.

สำหรับ builders ไทย SEA. ถ้า target sales หรือ service vertical อย่าขาย agent stand alone. ขาย agent plus data foundation plus workflow integration เป็น bundle. Vertical ที่ window เปิด. Thai insurance AIA Muang Thai FWD. Thai bank RM SCB K-Bank KBank private. Thai property AP SC Asset Sansiri Origin.

สำหรับ enterprise. Vendor evaluation Q4 นี้ต้องแยก 3 metric. Productivity ที่ measurable. Value ceiling proof point. Failure mode explanation ที่ vendor commit เขียนหน้า contract.

สำหรับ Thai SI. Bluebik G-Able Accenture SEA Deloitte Thailand ที่ position agent value optimization ที่ audit deployment ระบุ value ceiling prescribe fix. Framework ที่ Gartner McKinsey จะ publish Q1 2027 คือ template ที่ SI ต้อง productize ก่อน. คุยกันวันหน้าครับ.
