---
date: 2026-09-03
slug: mckinsey-state-of-ai-2026-scaling-gap
topic: use-case
reading_time_min: 4
sources: 3
image_prompt: |
  A financial-report style split scene: on the left, a giant glowing bar
  chart with the number "80%" labeled "PRODUCTIVITY". On the right, a much
  smaller bar labeled "37% EBIT IMPACT". Between them, a wide chasm labeled
  "SCALING GAP". A silhouetted executive stares across the gap holding a
  briefcase labeled "AI BUDGET". Editorial isometric style, high contrast,
  navy background with warning-yellow accents, 1:1 aspect, no real human
  faces.
image: images/26-09-03-0613-03-mckinsey-state-of-ai-2026-scaling-gap.png
---

# McKinsey State of AI 2026 — 80% เห็น productivity แต่ 37% เห็น EBIT: scaling gap คือปัญหาที่ agent ต้องปิด

## TL;DR
- **McKinsey State of AI (25 ส.ค. 2026, n=1,719)** — 80% ของบริษัทเห็น productivity gain แต่ **แค่ 37% เห็น EBIT impact จริง**
- **40% ของบริษัท $1B+ scale agent แล้ว** ในหนึ่งหรือหลาย function (จาก 27% ปีก่อน) — โต 48% YoY
- **32% ของบริษัทเลือกไม่ซื้อ software feature** เพราะสามารถ build เองด้วย agentic coding tools

## เกิดอะไรขึ้น
McKinsey ปล่อย State of AI survey ปี 2026 เมื่อ 25 ส.ค. โดยสุ่ม 1,719 executive ทั่วโลก — และตัวเลขที่กระแทกที่สุดไม่ใช่การ adoption แต่คือ **scaling gap**: 80% ของบริษัทเห็นว่าพนักงานได้ productivity gain จาก AI แต่มีเพียง 37% ที่รายงานว่า AI ส่งผลถึง EBIT ระดับ enterprise. Register พาดหัวว่า enterprise AI "กำลังอยู่บนถนน" สู่ ROI — คำสำคัญคือ "กำลังอยู่บนถนน" ไม่ใช่ "ถึงแล้ว"

จุดที่น่าสนใจคือ **agent-specific data** — 40% ของบริษัทรายได้ $1 พันล้าน+ ตอนนี้ scale agent ในอย่างน้อยหนึ่ง function ต่อจาก 27% ปีก่อน — โต 48% YoY ในกลุ่ม enterprise ใหญ่. แต่ถ้าดูภาพรวมทั้ง sample เพียง 23% เท่านั้นที่ scale agentic system เข้า production จริง อีก 39% กำลัง experiment — pattern คลาสสิกของ enterprise tech: pilot เยอะ, production น้อย

ตัวเลขที่ builder ต้องอ่านคือ **32% ของบริษัทตัดสินใจไม่ซื้อ software product/feature เพราะสามารถ build เองด้วย agentic coding tools** — เท่ากับ 1 ใน 3 ของ enterprise SaaS deal ที่เคยเซ็นได้ ตอนนี้แข่งกับ Devin, Cursor, Copilot ที่ raise เงินระดับ $1B ล่าสุด (Cognition ที่ $26B valuation, $492M ARR ต้นปี). Cannibalization ที่ SaaS vendor กลัวมาสองปี ตอนนี้ McKinsey วัดออกมาเป็นตัวเลขได้แล้ว

## ทำไมสำคัญ
Scaling gap คือ **the story of 2026** สำหรับ enterprise AI. ปีที่แล้วเรื่องเดียวคือ "adoption" — ปีนี้เรื่องเดียวคือ "แล้วเงินอยู่ไหน?". นักลงทุนเริ่มขอ ROI concrete ก่อนจ่ายเงินรอบต่อไป — CFO ที่เซ็น budget AI $10M–$50M ปีก่อน ปีนี้ต้องขึ้น board ตอบว่าทำไม EBIT ไม่ขยับ. ปัจจัยที่แยก 37% ออกจาก 63% ที่เหลือ ตาม McKinsey คือ **scoped use case + clean data + pre-defined escalation path** — สามอย่างที่ agent platform ต้อง productize ให้กลายเป็น default ไม่ใช่ให้ลูกค้าคิดเอง

signal ต่อจากนี้: บริษัทที่จะย้ายจาก "80% productivity" ไปเป็น "37% EBIT" กลุ่มถัดไป จะเป็นกลุ่มที่ยอมให้ agent ตัดสินใจแทนคนใน bounded task — customer service ที่ resolution time ลด 70-80%, การเงินที่ close book เร็วขึ้น, sales ops ที่ pipeline update ตัวเอง. ทั้ง 3 case มี property เดียวกัน: task ซ้ำ, data structured, escalation ชัดเจน — pattern นี้แหละคือ template ของ agent platform ที่จะโตต่อไปได้

## มุม AI Agent Platform
สำหรับ **builders** ตัวเลข 40% scaling ในบริษัท $1B+ คือ green light — enterprise budget เข้าจริงแล้ว. แต่ 32% "build vs buy" ที่พลิกเป็น "build" ก็เป็นคำเตือน: ถ้า product เป็นแค่ wrapper บน foundation model, ลูกค้าอาจตัดสินใจเขียนเองด้วย Copilot ในไม่กี่สัปดาห์. Moat ต้องมาจาก vertical data, workflow integration ที่ setup เอาเองแล้วเสียเวลาเกิน 3 เดือน, หรือ compliance layer ที่ certified. สำหรับ **businesses ที่กำลัง deploy** — ตัวเลข 4-8 เดือน median time to positive ROI + 171% average return หมายความว่า pilot ที่ยังไม่คืนทุนใน 6 เดือนต้องมา review scoping ใหม่ ไม่ใช่ scale ต่อ

สำหรับ **ecosystem ไทย** โดยเฉพาะ SME — pattern เดียวกันจะมาถึงในหนึ่งถึงสองไตรมาส. Agent platform ที่มี **pre-built skill สำหรับ SEA workflow** (Line-based customer service, PromptPay reconciliation, e-tax integration) จะมี positioning ที่ international vendor ไม่แข่ง เพราะ localization cost ไม่คุ้มกับ market size ในสายตาเขา — เป็นช่องที่ Enabridge และคู่แข่งไทยควรเดินเข้าให้เร็ว ก่อน Google/Microsoft จะ ship connector รอบใหม่

## Sources
- [McKinsey says enterprise AI is finally 'on the road to ROI' — The Register](https://www.theregister.com/ai-and-ml/2026/08/25/mckinsey-says-enterprise-ai-is-finally-on-the-road-to-roi/5292388)
- [Record AI Spending Can't Move Earnings Needle for 94% of Enterprises — Tech Times](https://www.techtimes.com/articles/325590/20260826/record-ai-spending-cant-move-earnings-needle-94-enterprises-mckinsey-finds.htm)
- [McKinsey AI 2026: 80% Productive, 37% EBIT — ExplainX](https://explainx.ai/blog/mckinsey-state-of-ai-2026-roi-agentic-coding-august-2026)

---

## Audio script
McKinsey ปล่อยผลสำรวจ State of AI 2026 เมื่อ 25 สิงหา สุ่ม 1,719 executive ทั่วโลก. ตัวเลขที่ทำให้คนสะดุ้งคือ 80 เปอร์เซ็นต์ของบริษัทเห็นว่าพนักงานได้ productivity เพิ่ม จาก AI แต่มีเพียง 37 เปอร์เซ็นต์เห็นว่า EBIT ระดับบริษัทขยับตาม — เรียกว่า scaling gap. ปีที่แล้วเรื่องเดียวคือ adoption ปีนี้เรื่องเดียวคือแล้วเงินอยู่ไหน. ตัวเลขที่คน build platform ต้องรู้คือ 40 เปอร์เซ็นต์ของบริษัทรายได้พันล้านดอลลาร์ขึ้นไป ตอนนี้ scale agent อย่างน้อยหนึ่ง function แล้ว — โตจาก 27 เปอร์เซ็นต์ปีก่อน. อีกตัวคือ 32 เปอร์เซ็นต์ของบริษัท ตัดสินใจไม่ซื้อ software feature เพราะ build เองด้วย agentic coding tool ได้ — เป็นการ cannibalize SaaS ที่ McKinsey วัดออกมาเป็นตัวเลขได้แล้ว. Insight สำคัญคือกลุ่ม 37 เปอร์เซ็นต์ที่เห็น EBIT impact มีสามอย่างเหมือนกัน — scoped use case, clean data และ escalation path ชัดเจน. ใครสร้าง agent platform ต้อง productize สามอย่างนี้ให้เป็น default. สำหรับตลาดไทย เจาะ SEA workflow ที่ international vendor ยังไม่ทำ Line, PromptPay, e-tax คือช่องที่ควรรีบเข้าครับ
