---
date: 2026-09-11
slug: zscaler-agentic-soc-frontier-model
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial illustration of a glowing fortified control room shaped like a hexagon
  with three towering pillars stamped "TRIAGE", "INVESTIGATE", "CONTAIN"; overhead
  a giant readout displays "750 BILLION TRANSACTIONS / DAY" in bold block letters,
  while thin luminous threads flow from a small Anthropic swirl and OpenAI knot at
  the top down through the pillars. Cool cyan and deep purple palette, isometric
  perspective, sharp rim light, magazine-cover clarity, 1:1 aspect, high contrast
  readable at 200px thumbnail, no real human faces.
image: images/26-09-11-0610-02-zscaler-agentic-soc-frontier-model.png
---

# Zscaler เปิด "Agentic SOC" — AI agent วิ่งบน 750B daily transaction, plug กับ Anthropic + OpenAI frontier model ตรง; SOC operating model ที่ถูก re-write

## TL;DR
- Zscaler ประกาศ **Zscaler Agentic SOC** (9 ก.ย.) — SOC platform ที่ **specialized AI agent** ทำ alert triage / root-cause investigation / verdict assignment / response workflow แทน analyst
- Agent วิ่งบน telemetry base **750 พันล้าน zero-trust transaction/วัน** — network + identity + endpoint + cloud + AI signal ครอบ single trust plane เดียว
- **Partner กับ Anthropic + OpenAI ตรง** — frontier model ของ 2 lab ถูก wire เข้ากับ Zscaler proprietary threat intelligence; ประกาศพร้อมกันในสัปดาห์เดียว
- Available globally now — Zscaler ไม่รอ preview / early access; **ยิงตรงเข้า enterprise procurement cycle ปี 2027**

## เกิดอะไรขึ้น

วันอังคาร 9 ก.ย. — Zscaler ประกาศ **Zscaler Agentic SOC** ที่ Goldman Sachs Communacopia Technology Conference. Jay Chaudhry (CEO) และ Adam Geller (Chief Product Officer) วางกรอบผลิตภัณฑ์ว่าเป็น **"AI-first SOC ที่ purpose-built ตั้งแต่ ground up"** — ไม่ใช่ SIEM/SOAR เดิมที่แปะ Copilot ทับ, แต่คือ operating model ใหม่ที่ **agent ทำ workflow แทน analyst โดย default, human เข้ามาเมื่อ escalate เท่านั้น**

Architectural bet ที่โดดที่สุดคือ **data moat**. Zscaler อ้างว่า agent ตัวเดียวเข้าถึง telemetry ของ **750 พันล้าน zero-trust transaction ต่อวัน** — network + identity + endpoint + cloud + AI insight — บน customer footprint ของ Zscaler เอง (Fortune 500 หลายพันราย). นี่เป็น context window ที่ SIEM incumbent (Splunk, Sentinel, QRadar) ไม่มี เพราะเขาเก็บ log ของแต่ละลูกค้าแยกกัน. Zscaler เก็บ trust decision **cross-tenant** เป็น graph เดียวที่ agent เรียนได้ทั้งกลุ่ม

Agent ที่ Zscaler ประกาศแบ่งเป็น 4 role: (1) **Triage agent** — วิเคราะห์ alert แยก false positive; (2) **Root-cause investigation agent** — pivot จาก signal เดียวไปหาต้นเหตุ; (3) **Verdict assignment agent** — ตัดสินใจว่าเป็น true positive/false positive/benign; (4) **Response workflow agent** — trigger containment (isolate endpoint, revoke session, block IP). Zscaler อ้างว่า agent ทั้ง 4 ถูก **train + tune บน experience 10 ปีของทีม frontline SOC + Managed Detection Response + threat hunting** ของตัวเอง — ไม่ใช่ base LLM ที่พัฒนา prompt engineering ทับ

จุดที่น่าสนใจกว่าคือ **partnership ที่ Zscaler เปิดเผยชัดเจน**: Anthropic + OpenAI. Zscaler ประกาศว่า **frontier model ของทั้ง 2 lab ถูก wire เข้ากับ Zscaler proprietary threat intelligence + zero-trust telemetry** — เพื่อให้ agent "reason ด้วย depth, accuracy, และ explainability สูงกว่าที่ single lab จะทำได้เอง". นี่เป็นครั้งแรกที่ security vendor ระดับ hyperscale ประกาศใช้ **dual frontier model** (ไม่ใช่ single-lab lock-in) — เป็น sign ว่า security workload มี requirement redundancy + benchmarking ที่ single model API ไม่ตอบได้เดี่ยว ๆ

**Available globally now** — ไม่มี preview, ไม่มี early-access, ไม่มี waitlist. Zscaler ยิงตรงเข้า enterprise procurement cycle ที่ CISO กำลังวาง budget ปี 2027 — ซึ่งเป็น **6-8 สัปดาห์ที่เจ้าใหญ่ต้อง commit vendor ก่อน RFP season ปิด**. Timing นี้ไม่ใช่บังเอิญ

## ทำไมสำคัญ

ก่อน Zscaler ประกาศ พึ่งพ่วง Broadcom (AgentMinder), CrowdStrike (AI Partner Specialization), Proofpoint (SOC Agent + OpenAI Daybreak), Palo Alto (Console acquisition $500M), Tenable (CyberAgents Exchange Inspector) ในเดือนเดียวกัน — **security incumbent ทั้ง 5 ค่ายเข้าตลาด "agentic SOC" พร้อมกันภายใน 30 วัน**. แต่ Zscaler ต่างที่ 3 จุด: (1) มี **telemetry moat** ที่จริง (750B daily transaction ที่ endpoint EDR/SIEM ไม่มี); (2) กล้าใช้ **dual frontier lab** ไม่ vendor-lock; (3) **GA ทันที** ไม่รอ enterprise preview

signal ที่คม 3 ชั้น:

**ชั้นที่ 1 — SIEM หมดยุค.** Splunk (ตอนนี้อยู่ใต้ Cisco), Microsoft Sentinel, IBM QRadar — ทั้งหมด architecture "log storage + query + rule" — ไม่สามารถ compete กับ **telemetry graph ที่ agent เรียนได้ live**. Cisco พึ่งประกาศจ่าย $28B ซื้อ Splunk เมื่อปี 2024 กำลังโดน bet ผิด direction; Microsoft Security Copilot ที่วางบน Sentinel ต้อง re-architect. **Splunk M&A จะกลายเป็น SolarWinds/Symantec ของ security decade นี้**

**ชั้นที่ 2 — Dual-lab partnership เป็น default ใหม่.** เมื่อ Zscaler บอกว่า "wire ทั้ง Anthropic + OpenAI" แปลว่า enterprise procurement จะ **push single-model vendor ให้ตอบว่า fallback model plan คืออะไร**. Vertical AI startup ที่ pitch "based on GPT-5" หรือ "powered by Claude" ต้องเตรียมเรื่องราว multi-model ก่อน sales call ตกจาก shortlist

**ชั้นที่ 3 — SOC analyst hiring plateau.** ปี 2015-2024 SOC analyst salary + hiring growth ที่ 15-20% ต่อปี. เมื่อ Zscaler ประกาศว่า agent ทำ triage + investigation + verdict + response — role SOC Tier 1 (analyst ระดับต้น) จะ shrink. **Junior cybersecurity headcount ปี 2027-2028 จะไม่โต หรืออาจลดลงจริง**; แต่ demand สำหรับ senior "agent supervisor" + "threat hunter" ที่ handle escalation จะขึ้น

## มุม AI Agent Platform

**สำหรับ Builders** ที่กำลังสร้าง agent framework: สังเกต **specialization strategy** ของ Zscaler — ไม่ใช่ "generic super agent" แต่คือ **4 agent ที่แต่ละตัวมี narrow scope + train บน task data specific**. Anthropic กับ OpenAI ทำ frontier reasoning ให้; Zscaler ทำ training data + domain guardrail + tool binding. Split of labor นี้เป็น blueprint ให้ startup ที่มี domain data moat (medical imaging, legal contract, financial transaction) — pitch ต่อ VC ไม่ใช่ "we're building an agent framework" แต่คือ **"we're the specialization layer on top of frontier reasoning"**. Category นี้ยัง open — คนที่ปิด vertical ก่อนได้ moat ตลอด decade

**สำหรับ Users / Business** ที่กำลัง evaluate SOC/security agent: อย่ารีบ commit vendor. รอ 60-90 วันให้ Palo Alto, CrowdStrike, Microsoft ตอบก่อน — เพราะสัปดาห์นี้ **Zscaler ตั้ง benchmark ที่ทุกคนต้อง match**. Question ที่ต้องถามใน RFP: (1) มี dual-frontier model plan ไหม? (2) telemetry footprint (event/day) มีขนาดเท่าไร cross-tenant? (3) agent ถูก train บน SOC playbook จริงกี่ปี? (4) เมื่อ frontier lab เปลี่ยน pricing / policy จะ migrate ยังไง?

**สำหรับ Ecosystem** (frontier lab / hyperscaler / infra vendor): **Anthropic + OpenAI ที่ยอม co-brand กับ Zscaler เดียวกัน = neutrality signal**. เมื่อก่อน 2 lab นี้ compete ตรง; ตอนนี้ยอมนั่งข้างกันใน announcement เดียว = ตลาด security workload ใหญ่พอที่แบ่งได้; และแปลว่า **enterprise vendor ระดับใหญ่พอมี leverage บอกทั้ง 2 lab ให้ co-integrate**. บริษัทไทยขนาดใหญ่ (Gulf, SCB, PTT, AIS) ที่กำลังคุย Zscaler อยู่แล้ว จะได้ pathway เข้าใช้ dual frontier model โดยไม่ต้องเจรจา contract Anthropic/OpenAI แยก — **procurement leverage ของ security incumbent เพิ่มขึ้นชัดเจนหลัง 9 ก.ย.**

## Sources
- [Zscaler — Zscaler launches Agentic SOC to contain AI-driven threats](https://www.globenewswire.com/news-release/2026/09/09/3358327/0/en/zscaler-launches-agentic-soc-to-contain-ai-driven-threats.html)
- [Manila Times — Zscaler launches Agentic SOC to contain AI-Driven Threats](https://www.manilatimes.net/2026/09/09/tmt-newswire/globenewswire/zscaler-launches-agentic-soc-to-contain-ai-driven-threats/2421218)
- [SecurityBrief — Zscaler launches Agentic SOC to fight AI-driven attacks](https://securitybrief.news/story/zscaler-launches-agentic-soc-to-fight-ai-driven-attacks-975dfba6-dd15-41f8-aab3-4a3d7207a6d8)
- [StockTitan — Zscaler launches Agentic SOC to contain AI threats](https://www.stocktitan.net/news/ZS/zscaler-launches-agentic-soc-to-contain-ai-driven-z6saj7xobwqj.html)
- [ByteIota — Zscaler Agentic SOC: AI Agents Now Run Your Security Operations Center](https://byteiota.com/zscaler-agentic-soc-ai-agents-security-operations/)

---

## Audio script
วันอังคารที่ 9 กันยายน Zscaler ประกาศ Zscaler Agentic SOC ที่ Goldman Sachs conference. Jay Chaudhry ซีอีโอ และ Adam Geller Chief Product Officer วางกรอบเป็น AI-first SOC ที่ purpose-built ตั้งแต่ ground up. ไม่ใช่ SIEM SOAR เดิมที่แปะ Copilot ทับ. แต่คือ operating model ใหม่ที่ agent ทำ workflow แทน analyst โดย default. human เข้ามาเมื่อ escalate เท่านั้น.

bet ที่โดดที่สุดคือ data moat. Zscaler อ้างว่า agent เข้าถึง telemetry 750 พันล้าน zero-trust transaction ต่อวัน. network identity endpoint cloud AI insight. บน customer footprint ของ Zscaler เอง. Fortune 500 หลายพันราย. นี่เป็น context window ที่ Splunk Sentinel QRadar ไม่มี. เพราะเขาเก็บ log ของแต่ละลูกค้าแยกกัน. Zscaler เก็บ trust decision cross-tenant เป็น graph เดียว ที่ agent เรียนได้ทั้งกลุ่ม.

Agent แบ่งเป็น 4 ตัว. Triage agent วิเคราะห์ alert. Root-cause investigation agent pivot signal ไปหาต้นเหตุ. Verdict assignment agent ตัดสิน true false positive. Response workflow agent trigger containment. ทั้ง 4 ถูก train บน experience 10 ปี ของทีม frontline SOC MDR threat hunting ของ Zscaler เอง.

จุดที่น่าสนใจกว่าคือ partnership. Zscaler ประกาศชัดว่า wire frontier model ของทั้ง Anthropic และ OpenAI เข้ากับ proprietary threat intelligence. ครั้งแรกที่ security vendor ระดับ hyperscale ประกาศใช้ dual frontier model. ไม่ใช่ single-lab lock-in. security workload มี requirement redundancy กับ benchmarking ที่ single model API ไม่ตอบได้เดี่ยวๆ.

Zscaler บอก available globally now. ไม่มี preview ไม่มี early-access ไม่มี waitlist. ยิงตรงเข้า enterprise procurement cycle ที่ CISO กำลังวาง budget ปี 2027. Timing 6 ถึง 8 สัปดาห์ก่อน RFP ปิด. ไม่ใช่บังเอิญ.

signal ที่คมสามชั้น. ชั้นแรก SIEM หมดยุค. Splunk ที่ Cisco จ่าย 28 พันล้านซื้อไปกำลังโดน bet ผิด direction. Microsoft Security Copilot ที่วางบน Sentinel ต้อง re-architect. Splunk M&A จะกลายเป็น SolarWinds Symantec ของ security decade นี้.

ชั้นที่สอง dual-lab partnership เป็น default ใหม่. Vertical AI startup ที่ pitch based on GPT-5 หรือ powered by Claude ต้องเตรียม multi-model story ก่อน sales call.

ชั้นที่สาม SOC analyst hiring plateau. Tier 1 role จะ shrink. junior headcount ปี 2027 2028 อาจไม่โตหรือลดจริง. demand สำหรับ senior agent supervisor และ threat hunter ที่ handle escalation จะขึ้น.

สำหรับผู้ที่ evaluate security agent อยู่. อย่ารีบ commit vendor. รอ 60 ถึง 90 วันให้ Palo Alto CrowdStrike Microsoft ตอบก่อน. เพราะสัปดาห์นี้ Zscaler ตั้ง benchmark ที่ทุกคนต้อง match. RFP ควรถามเรื่อง dual-frontier model plan telemetry footprint agent training data years. และ migration path เมื่อ frontier lab เปลี่ยน pricing policy.
