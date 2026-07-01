---
date: 2026-06-24
slug: taktile-110m-goldman-sachs-financial-agentic-decisions
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: |
  A dramatic editorial illustration of a brushed-steel bank vault door swung
  open to reveal a glowing modular control panel labeled "AGENTIC DECISION
  PLATFORM" with three illuminated workflow blocks: "UNDERWRITING", "CLAIMS",
  "AML". A bold floating headline reads "$110M SERIES C" with secondary stack
  "GOLDMAN SACHS · LED ROUND · $184M TOTAL RAISED". A small Taktile wordmark
  glows on the panel, Goldman Sachs ribbon at the lower edge. Cinematic
  isometric tech-magazine cover style, deep navy and brushed-gold palette,
  ultra-sharp text rendering for 200px thumbnail readability, 1:1 aspect
  ratio, no real human faces.
image: images/26-07-01-0608-03-taktile-110m-goldman-sachs-financial-agentic-decisions.png
---

# Goldman Sachs นำ $110M Series C ใน Taktile — เดิมพันว่า agentic decision คือ "ของจริง" ในธนาคารและประกัน

## TL;DR
- 24 มิ.ย. — **Taktile** (Berlin / NY) ปิด **$110M Series C** นำโดย **Growth Equity at Goldman Sachs Alternatives**, ร่วมกับ Balderton Capital, Index Ventures, Tiger Global, Y Combinator, Dig Ventures — **total raised $184M**
- ตัว product คือ **Agentic Decision Platform** — modular stack ที่ผสม AI agent + business rule + human oversight ให้ bank/insurer automate high-stakes decision: underwriting, claims processing, AML compliance
- เป็น signal ใหญ่ว่า **regulated financial services กำลังกลายเป็นจุดที่ agentic AI mature เร็วสุด** เพราะมี budget + workflow ที่ ROI ของ automation ชัดเจน + Goldman ที่ underwrite รอบนี้เองก็เป็น future customer ของ Taktile

## เกิดอะไรขึ้น

24 มิถุนายน 2026 — Taktile ประกาศปิด Series C $110M นำโดย Growth Equity arm ของ Goldman Sachs Alternatives — รอบใหญ่ที่สุดของบริษัทตั้งแต่ก่อตั้งเมื่อปี 2020. ผู้ร่วมลงทุนรายอื่น includes Balderton Capital, Index Ventures, Tiger Global Management, Y Combinator, และ Dig Ventures. รวมเงินระดมตลอด lifecycle เป็น $184M. Taktile วางแผนใช้เงินขยาย footprint ในสหรัฐ, EMEA, LATAM และพัฒนา AI solution สำหรับ use case ที่ complex ขึ้นใน banking + insurance

ที่ดูเหมือนปกติแต่จริงจังคือ — **Goldman Sachs ลงเป็น lead investor**. Goldman ไม่ใช่ VC ทั่วไป — เป็น investment bank ที่ทำงานกับ bank อื่น ๆ ทั่วโลกเป็น primary business. การที่ Growth Equity arm ของ Goldman ลงเงิน $110M ใน decisioning platform แปลว่า Goldman เห็น signal **(1) ลูกค้าธนาคาร / insurer ของ Goldman เริ่มถาม Goldman ว่าควรซื้อ Taktile หรือคู่แข่ง, (2) Goldman เองอาจเป็น customer ในไม่นาน**. Investment กับ commercial leverage มาคู่กัน

ตัว product ของ Taktile คือ **modular Agentic Decision Platform** — concept ที่แตกต่างจาก agent บริษัทอื่นตรงที่ไม่ใช่ "agent ที่ทำทุกอย่าง" แต่เป็น **agent + rule engine + human oversight ที่ work together ใน specific decision flow**. ใช้ก็คือ: bank loan officer ส่ง application เข้าระบบ → agent extract info จาก document, query data source, ประเมิน risk → rule engine check policy/regulatory constraint → human reviewer approve หรือ override. แต่ละ step มี audit log + explainability layer ที่ regulator ตรวจสอบได้

Use case ที่ Taktile เคลม deploy แล้ว: **underwriting business loan, assessing insurance claims, AML/financial crime detection**. รายชื่อลูกค้าที่บริษัทเคยอ้างถึงในรอบก่อน includes Coinbase, Klarna, Mercury, Zilch, และ insurer ใน EU หลายราย — บริษัทเหล่านี้ run high-volume decision (หลายหมื่นต่อวัน) ที่ก่อนหน้าใช้ human team หลายร้อยคน. Taktile claim ว่าลด decision time จากชั่วโมง → วินาที ในขณะที่ accuracy + auditability ดีขึ้น. CEO Maik Taro Wehmeyer (อดีต McKinsey + QuantumBlack) ระบุว่าตลาด demand accelerate รุนแรงตั้งแต่ปี 2025 หลัง AI model "ทำงาน high-stakes" ได้

## ทำไมสำคัญ

**ดีลนี้บอกตลาดสองเรื่อง**: (1) ตลาด agentic AI ในกลุ่ม **regulated financial services** mature เร็วกว่ากลุ่มอื่น — เพราะ workflow ชัด, ROI วัดได้, ลูกค้ามี budget จ่าย software 6-7 หลักดอลล่าร์, regulator demand audit trail ที่ Taktile-style design ตอบโจทย์ได้พอดี. (2) **Tier-1 financial institution เริ่มลงเงินเป็น investor** ใน agent platform vendor — เป็น pattern ที่จะ scale ในปี 2026-27. JPMorgan, Citi, HSBC ทั้งหมดมี strategic investment arm ที่กำลังประเมิน agentic vendor

อีก signal ที่ลึกกว่าคือ **architectural philosophy ของ Taktile ชนะตอนนี้**. หลาย agent platform เริ่มจาก "ใส่ LLM เข้าทุก step" — ปัญหาคือ regulator + risk officer ของธนาคารไม่ยอม เพราะ explainability ต่ำเกินไป. Taktile เริ่มจาก **decision-tree-first, rule-engine-first** แล้วค่อยใส่ LLM/agent ใน step ที่ unstructured (document parsing, narrative analysis, risk reasoning). ทำให้ค่า model ต่ำ, error mode predictable, audit log ครบ. นี่คือ design pattern ที่ Anthropic, Klarna, สาว ๆ ใน Stripe ตำราเริ่มแนะนำ — และ Taktile ทำมาตั้งแต่ก่อน trend

Pattern ที่เห็นชัด — **vertical agentic + regulated industry = funding magnet**. ในรอบ 2 เดือนที่ผ่านมา: Moment (wealth management) $78M Series C, Sierra (voice agent) $950M valuation, Broadridge (capital markets) ขยาย agentic, Adyen Agentic เปิด commerce. ทั้งหมดอยู่ใน financial services. ตัวที่อยู่นอก financial ที่ดึง funding ใหญ่ ๆ ได้น้อยลงในรอบเดียวกัน. คำอธิบายง่ายสุดคือ — financial services มี (ก) data ที่ digital อยู่แล้ว, (ข) regulatory framework ที่ทำให้ decision audit ได้, (ค) revenue per decision สูงพอที่ software ราคาแพงคุ้ม

## มุม AI Agent Platform

**Builders** ที่ build agent framework (LangGraph, OpenAI Agents SDK, Dust, Cognigy, AutoGen) ต้องสังเกตว่า **architectural composability** ของ Taktile คือ winning pattern สำหรับ regulated vertical — agent + rule engine + human + audit layer ต้อง composable แบบ first-class, ไม่ใช่ทำเป็น afterthought. ใครก็ตามที่ออก feature "policy-as-code + agent + human handoff" เป็น primitive แทนที่จะให้ user combine เอง จะดึง enterprise deal ที่ regulated ได้ก่อน. รวมถึง observability/eval layer ที่ต้อง track regulatory compliance metric ตั้งแต่ design

**Users / business** ใน Thai banking + insurance + securities (KBank, SCB, Bualuang Securities, AIA, Bangkok Insurance) — Taktile + คู่แข่ง (Decipad, Akkio, FeatureBase) เปิด option ใหม่ที่ก่อนหน้านี้ต้อง custom-build เอง 6-12 เดือน. Build vs buy decision เปลี่ยน — buy เร็วกว่า, มี certified architecture, regulator เคยเห็นแล้วในยุโรป. แต่ระวัง localization gap — Thai regulator (BoT, SEC, OIC) ยังไม่มี framework เฉพาะสำหรับ agentic decision; ใครที่จะ deploy แรก ๆ ต้องทำ governance paper เองและ engage regulator แต่ต้น ใช่เวลาเพิ่ม 6-9 เดือน. แต่ปูทาง first-mover ในตลาดที่ทุกธนาคารจะตามมาในปี 2027-28

## Sources
- [Taktile Secures $110M in Goldman Sachs-led Series C — Taktile blog](https://taktile.com/articles/taktile-secures-110m-in-goldman-sachs-led-series-c-to-power-ai-transformation-in-financial-institutions)
- [Goldman Sachs (GS) Led Taktile's $110 Million Series C — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/goldman-sachs-gs-led-taktile-070747817.html)
- [Taktile Raises $110M Series C — The SaaS News](https://www.thesaasnews.com/news/taktile-raises-110m-series-c/)
- [Taktile bags $110m Series C led by Goldman Sachs — FinTech Futures](https://www.fintechfutures.com/venture-capital-funding/taktile-110m-series-c-goldman-sachs)
- [Taktile's $110M Haul Signals a New Era for AI in High-Stakes Finance — BriefGlance](https://briefglance.com/articles/taktiles-110m-haul-signals-a-new-era-for-ai-in-high-stakes-finance)

---

## Audio script

วันที่ยี่สิบสี่มิถุนายน Taktile ปิด Series C ที่หนึ่งร้อยสิบล้านดอลล่าร์ นำโดย Growth Equity arm ของ Goldman Sachs. รวมเงินระดมทุนตลอดของบริษัทเป็นหนึ่งร้อยแปดสิบสี่ล้าน. ที่น่าจับคือ Goldman ไม่ใช่ VC ปกติ เป็น investment bank ที่ทำงานกับธนาคารทั่วโลก — แปลว่ามองเห็น signal สองอย่าง หนึ่ง ลูกค้าธนาคารเริ่มถามว่าควรซื้อ Taktile ไหม สอง Goldman เองก็อาจเป็น customer ในไม่นาน.

ตัว product ของ Taktile คือ Agentic Decision Platform แบบ modular ที่ผสม AI agent กับ rule engine กับ human oversight ใน specific decision flow. Use case ที่ deploy แล้ว — underwriting business loan, assessing insurance claim, AML detection. ลูกค้า includes Coinbase, Klarna, Mercury, Zilch. ลด decision time จากชั่วโมงเป็นวินาที โดย accuracy กับ auditability ดีขึ้น.

จุดที่ design ชนะคือ Taktile เริ่มจาก decision-tree-first แล้วค่อยใส่ LLM ใน step ที่ unstructured เท่านั้น. ทำให้ error mode predictable, audit log ครบ, regulator ตรวจสอบได้ — ตรงข้ามกับ approach "ใส่ LLM เข้าทุก step" ที่ธนาคารไม่ยอม. Pattern ที่เห็นชัดคือ vertical agentic ใน financial services กลายเป็น funding magnet. สองเดือนที่ผ่านมา Moment, Sierra, Broadridge, Adyen ดึง funding ใหญ่ทั้งหมดอยู่ในกลุ่มนี้.

สำหรับทีมในธนาคารและประกันไทย ที่ประเมิน build vs buy สำหรับ underwriting หรือ claim — Taktile กับคู่แข่งเปิด option ใหม่ที่ก่อนหน้าต้อง custom-build เองหกถึงสิบสองเดือน. แต่ระวัง localization gap — แบงค์ชาติ กลต. คปภ. ยังไม่มี framework เฉพาะสำหรับ agentic decision ใครที่จะ deploy ก่อน ต้องทำ governance paper เอง engage regulator แต่ต้น ใช้เวลาเพิ่มหกถึงเก้าเดือน แต่ปูทาง first-mover ในตลาดที่ทุกธนาคารจะตามมาในปี 2027 ถึง 2028.
