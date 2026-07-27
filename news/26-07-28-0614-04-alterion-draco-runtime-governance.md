---
date: 2026-07-28
slug: alterion-draco-runtime-governance
topic: openbridge-trend
reading_time_min: 5
sources: 5
image_prompt: |
  A translucent glass control tower marked "DRACO" hovering between a fleet
  of autonomous agent drones and a factory of enterprise apps; a bright
  gauge on the tower reads "$234B AT RISK" and a policy panel below reads
  "SOC 2 / ISO 42001 / EU AI ACT". Editorial isometric illustration, cool
  teal and amber accent palette, high contrast so labels and numbers read
  at 200px. 1:1 aspect, no real human faces.
image: images/26-07-28-0614-04-alterion-draco-runtime-governance.png
---

# Alterion Draco: runtime governance layer สำหรับ agent — จับ prompt + block action ก่อนเกิด, ตอบ $234B SaaS risk ที่ Gartner เตือน

## TL;DR
- **Alterion** (ก่อตั้งโดยอดีต McKinsey Partner + Google VP) launch **Draco** — runtime control plane สำหรับ enterprise AI agent — เมื่อ 16 ก.ค. 2026
- Draco สังเกต **ทุก prompt + ทุก action** ที่ agent ทำ, model behavior, apply programmable guardrail **ก่อน** high-risk action เกิดขึ้น — ไม่ใช่ post-hoc logging เหมือน APM
- Compliance framework built-in: **SOC 2, ISO 42001, EU AI Act** — agent ที่ deploy ในธุรกิจ regulated ผ่าน audit ได้โดยไม่ต้อง custom evidence collection
- Timing สำคัญ: มาพร้อม Gartner warning ว่า agentic AI จะ disrupt **$234 พันล้าน** ของ SaaS spend ภายใน 2030 — governance gap คือ blocker ของการ deploy scale
- Positioning: "sit between agent + enterprise infra" — layer ที่ MCP/A2A protocol ไม่ครอบ

## เกิดอะไรขึ้น

**Alterion** — startup ที่ก่อตั้งโดย **Alharith Hussin** (อดีต McKinsey Partner) และ **Asim Husain** (อดีต Google Engineering VP) — ประกาศ availability ของ **Draco** ตอนกลางเดือน ก.ค. Draco ถูก position เป็น "runtime control plane สำหรับ enterprise AI agent" — layer ที่นั่งอยู่ระหว่าง agent (Claude, GPT, Gemini, in-house) กับ enterprise infrastructure (databases, ERP, CRM, comms, ไฟล์)

ที่ทำให้ Draco แยกจาก APM tool (Datadog, New Relic) หรือ security tool (CrowdStrike, Wiz) ทั่วไปคือ **granularity ของ observation**. Draco ไม่ log แค่ metric — สังเกต **ทุก prompt ที่ agent ส่ง, ทุก tool call ที่ agent เรียก, ทุก response ที่ agent ได้กลับ** — แล้ว model behavior pattern ต่อเนื่อง. เมื่อ agent จะทำ high-risk action (transfer เงิน > threshold, delete production data, send email ไป external, invoke tool ที่ไม่อยู่ใน allowlist) — Draco intercept + apply programmable guardrail **ก่อน** action ผ่าน

หัวใจของ pitch enterprise คือ compliance surface. Draco ship พร้อม **SOC 2, ISO 42001, EU AI Act** framework compliance built-in — audit evidence collection auto-generate, per-agent risk score, policy versioning. บริษัทที่ regulated (financial services, healthcare, government) ที่ต้อง prove ต่อ regulator ว่า "agent ที่ deploy ไม่ทำ action ที่ไม่ได้ authorize" — Draco lower barrier ของ deployment ลงจาก 6-12 เดือน compliance sprint → พร้อม ship

Timing ของ launch จับ **Gartner report** ที่ปล่อยต้น ก.ค. — analyst warning ว่า agentic AI จะ **redirect $234 พันล้าน** ของ enterprise SaaS spend ระหว่าง 2026-2030 (คิดเป็น ~20% ของ SaaS market). Gartner เรียก phenomenon ว่า **"agentic arbitrage"** — agent ที่ทำ workflow ข้าม system หลาย ๆ ตัวโดยไม่ต้องผ่าน UI ของ SaaS แต่ละเจ้า, ทำให้ software เดิม "invisible". Governance gap = blocker หลักที่ทำให้ enterprise ยังไม่ full-scale deploy — Draco target ตรงจุดนั้น

Alterion ไม่เปิดตัวเลข ARR, deal size, หรือ customer name — แต่ press release ระบุว่ามี "beta customer ใน regulated verticals" หลายราย. Funding round ยังไม่ประกาศ แต่ founder pedigree + timing แนะว่า Series A ระดับ $30-60M น่าจะตามภายใน 90 วัน

## ทำไมสำคัญ

Draco คือ **early move ของ market segment ที่ยังไม่มีชื่อ**: agent runtime governance. คำอธิบายที่ถูกใช้ตอนนี้ — "guardrails", "safety layer", "agent observability" — ยังไม่ settle เพราะยังไม่มี category leader. Segment นี้กำลังจะโตแบบเดียวกับที่ **API management** โตจาก Layer 7 (2007) → Apigee (2010) → Kong (2015) → MuleSoft ($6.5B Salesforce acquisition 2018). ทุก protocol ที่กลายเป็น infrastructure ต้องมี governance product ที่ตามมา

Pattern ที่ชัดคือ **3 category กำลัง form พร้อมกัน**: (1) **runtime control** = Draco, Lasso, Robust Intelligence; (2) **agent gateway** = Kong AI Gateway, Cloudflare AI Gateway, WorkOS AuthKit for MCP; (3) **policy + compliance framework** = Credo AI, Fiddler AI, Arthur. ทั้ง 3 มี overlap แต่ประเด็นหลักต่างกัน. Winner จะเป็นคนที่ integrate ได้ทั้ง 3 layer หรือ define standard ที่คน layer อื่นต้อง comply — Draco เลือก positioning แรก (all-in-one runtime)

จุดที่น่าจับตาคือ **Gartner number vs Draco pitch**. Gartner $234B = 20% ของ SaaS spend. ถ้า governance product ยึด **1% ของ agent traffic** ที่ผ่าน enterprise = market size ~$2.3B/year — พอเลี้ยง 3-5 unicorn. Draco เข้ามาจับ window ที่กว้างมาก + timing ก่อนคู่แข่ง ระบุ SKU. Alterion ที่มี McKinsey + Google pedigree = fund-raising + enterprise sales จะเร็วกว่า challenger technical-founder ทั่วไป

Signal ต่อ Anthropic / OpenAI / Google: 3 เจ้าใหญ่ต้อง decide ว่า **build governance เอง หรือ partner**. Anthropic มี Trust & Safety team + own model + own SDK — natural build เอง. แต่ enterprise CISO ไม่อยาก vendor lock-in ที่ระดับ governance — จะบังคับ multi-vendor. คนที่ launch **"agent governance layer แบบ vendor-neutral"** ก่อน (Draco, Lasso, หรือ Kong / Cloudflare) จะยึด standard

## มุม AI Agent Platform

**Builders:** ถ้า agent framework ของคุณยังไม่มี **runtime policy hook** (before-action interceptor, per-tool guardrail, audit event stream) = pay technical debt Q4 นี้. เพิ่ม API surface ที่ third-party governance product plug-in ได้ — pattern เดียวกับที่ webhook + OAuth มาตรฐาน. คนที่ integration แล้วกับ Draco / Lasso / Cloudflare AI Gateway ภายในไตรมาส = ผ่าน RFP enterprise ในไตรมาสถัดไปโดยไม่ต้อง rewrite

**Users / business:** สำหรับ enterprise ที่ deploy agent เกิน 3 use case ใน production — ถ้ายังไม่มี governance layer, **CISO / Chief Risk / auditor** ของบริษัทจะ block scale ในไตรมาสหน้า. เลือก governance product ก่อน scale ให้ pain — evaluate Draco, Lasso, Robust Intelligence, Kong AI Gateway parallel; ให้ security team lead ไม่ใช่ engineering ให้ criteria SOC 2 + ISO 42001 + EU AI Act support = table stakes

**Ecosystem:** สำหรับ Enabridge — **นี่คือ moat opportunity ระดับ decade**. Draco ทำ generic enterprise; Thai regulator (BOT, SEC, PDPA, กสทช) ยังไม่มี playbook. Enabridge สามารถ position **"agent governance ที่ compliant Thai regulator, ครอบ PDPA + Bank of Thailand IT circular + audit report ที่ SEC accept"** = product ที่ Draco compete ไม่ได้เพราะไม่มี local knowledge. Bundle กับ MCP-native gateway (brief #01) + Thai vertical agent (brief #02, #03) = full stack ที่ Thai enterprise ซื้อ 3-in-1

## Sources
- [Alterion Launches Draco, a Runtime Control Plane for Enterprise AI Agents — PRNewswire](https://www.prnewswire.com/news-releases/alterion-launches-draco-a-runtime-control-plane-for-enterprise-ai-agents-302827818.html)
- [Introducing DRACO — Alterion Blog](https://www.alterion.ai/blog/introducing-draco)
- [Draco: AI Agent Runtime Control Plane — Alterion](https://www.alterion.ai/platform/draco)
- [Gartner Says $234 Billion in Enterprise Application Software Spend Is at Risk from Agentic AI](https://www.gartner.com/en/newsroom/press-releases/2026-07-01-gartner-says-us-dollars-234-billion-in-enterprise-application-software-spend-is-at-risk-from-agentic-artificial-intelligence)
- [Agentic AI puts $234B in enterprise SaaS spending at risk, Gartner says — CIO](https://www.cio.com/article/4192242/agentic-ai-puts-234b-in-enterprise-saas-spending-at-risk-gartner-says.html)

---

## Audio script
Alterion startup ที่ก่อตั้งโดยอดีต McKinsey Partner กับอดีต Google Engineering VP launch product ชื่อ Draco เมื่อวันที่ 16 กรกฎาคม. Draco คือ runtime control plane สำหรับ enterprise AI agent. เป็น layer ที่นั่งระหว่าง agent กับ enterprise infrastructure.

ที่ทำให้ Draco แยกจาก APM ทั่วไปคือ granularity ของ observation. ไม่ log แค่ metric. สังเกตทุก prompt ที่ agent ส่ง ทุก tool call ที่เรียก ทุก response ที่ได้กลับ. เมื่อ agent จะทำ high-risk action เช่น transfer เงินเกิน threshold delete production data send email ไป external. Draco intercept ก่อน action ผ่าน.

หัวใจของ pitch enterprise คือ compliance. Draco ship พร้อม SOC 2 ISO 42001 EU AI Act framework built-in. Audit evidence auto-generate. บริษัท regulated ที่ต้อง prove ต่อ regulator ว่า agent ไม่ทำ action ที่ไม่ได้ authorize. Draco ลด barrier deployment จาก 6 ถึง 12 เดือน compliance sprint เหลือ ship เลย.

Timing ของ launch จับ Gartner report ที่ปล่อยต้นเดือน. analyst warning ว่า agentic AI จะ redirect 234 พันล้านดอลลาร์ของ enterprise SaaS spend ระหว่าง 2026 ถึง 2030 คิดเป็นราว 20 เปอร์เซ็นต์ของ SaaS market ทั้งหมด. Gartner เรียก phenomenon นี้ว่า agentic arbitrage. Governance gap คือ blocker หลัก. Draco target ตรงจุดนั้น.

Pattern ที่ชัดคือ 3 category กำลัง form พร้อมกัน. runtime control agent gateway และ policy compliance framework. Winner จะเป็นคน integrate ได้ทั้ง 3 layer.

สำหรับ Enabridge. นี่คือ moat opportunity ระดับ decade. Draco ทำ generic enterprise. Thai regulator ยังไม่มี playbook. Enabridge position agent governance ที่ compliant Thai PDPA Bank of Thailand IT circular audit report ที่ SEC accept. bundle กับ MCP-native gateway และ Thai vertical agent = full stack ที่ Thai enterprise ซื้อ 3-in-1.
