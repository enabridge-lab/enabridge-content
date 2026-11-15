---
date: 2026-11-10
slug: mercor-750m-human-intelligence-moat
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a split scene: on the left, a
  silhouetted expert at a workstation with a badge labeled "DOMAIN
  EXPERT" tagging data; on the right, a glowing AI agent cube labeled
  "ENTERPRISE AGENT" wired to a grading dashboard. Above the whole scene
  a banner reads "MERCOR — $750M AT $20B". Small chips below show
  "$3B RUN RATE", "NVIDIA + SALESFORCE", "2x IN 13 MONTHS". Clean
  editorial style, muted teal and warm orange palette, 1:1 aspect, no
  real human faces (silhouettes OK), high contrast so numbers stay
  readable at 200px thumbnail.
image: images/26-11-16-0605-03-mercor-750m-human-intelligence-moat.png
---

# Mercor $20B — thesis ว่า "human expertise" คือ moat ที่ frontier lab ซื้อไม่ได้

## TL;DR
- Mercor ปิด Series D $750M ที่ valuation $20B — 2 เท่าจาก $10B เมื่อ 13 เดือนก่อน — NVIDIA + Salesforce ร่วมลงทุน
- CEO Brendan Foody แจ้งบน LinkedIn ว่า run rate ถึง $3B (อ้างจาก Staffing Industry Analysts) — ไม่มี breakdown ระหว่าง labeling และ enterprise eval
- Mercor pivot จาก labeling vendor → "enterprise evaluations" — service ที่วัดว่า agent ทำงานแทนคนได้ขนาดไหน ก่อน deploy production

## เกิดอะไรขึ้น
วันที่ 10 พฤศจิกายน Mercor ประกาศ Series D $750M ที่ $20B post-money — เม็ดเงินจาก Benchmark (lead), Felicis, General Catalyst, Zoom, NVIDIA, และ Salesforce พร้อม employee tender ให้ early staff cash-out บางส่วน valuation สูงขึ้น 2 เท่าจาก $10B ตอน Series C เดือนตุลาคม 2025 — curve ที่เร็วแม้ตามมาตรฐาน AI ปี 2026

Business เดิมของ Mercor คือ staffing domain expert — แพทย์, นักกฎหมาย, นักฟิสิกส์, SWE ระดับ senior — มา label และ grade output ของ frontier model ให้ OpenAI, Anthropic, Google, Meta ซึ่งเป็น 4 ลูกค้ารายใหญ่สุด — ทั้งหมดเป็น model training lab ที่ scale beyond web data หมดแล้ว ต้องซื้อ domain-specific expertise โดยตรง CEO Brendan Foody บอกบน LinkedIn ว่า run rate ถึง $3B ตามที่ Staffing Industry Analysts รายงาน — ถ้าเป็นจริงจะเท่ากับ labeling company ที่ scale เร็วที่สุดในประวัติศาสตร์ (Scale AI ใช้ 8 ปีถึง $1B run rate)

ส่วนที่น่าสนใจกว่าคือ pivot — Mercor's blog post อธิบายว่าเงินส่วนหนึ่งลงใน "enterprise evaluations" — service ที่ enterprise ซื้อไม่ใช่ลูกค้า labeling frontier lab แต่เป็น Fortune 500 ที่ deploy agent ใน workflow ของตัวเอง Mercor จะส่ง domain expert เข้าไปใช้ agent, grade output, และสร้าง eval harness ที่ specific กับ workflow ลูกค้า — เช่น agent ที่ draft contract กฎหมายต้องผ่าน eval โดยทนายจริงก่อนไป production

## ทำไมสำคัญ
Round นี้ settle thesis ที่ debate กันทั้งปี — AI moat อยู่ที่ model หรือ data? Mercor ตอบว่า data ที่ unique ที่สุดคือ "judgment ของ expert" ไม่ใช่ raw text และ enterprise ที่ deploy agent production จะ pay premium เพื่อ eval harness ที่สะท้อน business logic จริง — ไม่ใช่ benchmark public อย่าง SWE-bench, GAIA, หรือ MMLU

เทียบกับ competitor pattern — Scale AI ถูก Meta ซื้อ 49% เมื่อปี 2024 แล้ว scale back ลูกค้า commercial, Surge AI focus ภาษาน้อย, Turing ไปทาง developer workforce — Mercor เข้าช่องว่างที่ "high-expertise, flexible staffing" ที่ scale ไม่ได้ใน traditional BPO การเพิ่ม enterprise eval ทำให้ customer base diversify จาก frontier lab (4 ลูกค้า เสี่ยง concentration) ไปที่ Fortune 500 หลายร้อยราย — เปลี่ยน risk profile ทั้งหมด

Caveat — $3B run rate เป็น CEO claim ไม่ใช่ audited number และ "expert staffing" มีอัตรากำไรบางกว่า SaaS (expect gross margin 30-40% เทียบ SaaS ที่ 70-80%) ซึ่งหมายความว่า Mercor ต้อง justify $20B valuation ด้วย growth rate มากกว่า margin ตอน Series E หรือ IPO จะเห็นชัดว่า unit economics ทำได้ไหม

## มุม AI Agent Platform
Builders — ถ้า agent ของคุณ deploy ให้ enterprise ใน vertical ที่ต้อง expert judgment (legal, medical, financial compliance) การมี eval harness ที่ validated โดย domain expert กลายเป็น table stake ไม่ใช่ premium Mercor จะเป็น vendor option — หรือสร้าง eval loop เองโดยจ้าง part-time expert ผ่าน platform อย่าง Toptal, Braintrust, หรือ vendor ไทยที่มี domain community พิจารณา build vs buy — ถ้าทำ vertical เดียวควร build, ถ้า horizontal ควร buy

Users/business — สำหรับ CTO/CDO ที่กำลัง deploy agent production ตอนนี้มี market signal แล้วว่า pre-deployment eval คือ step ที่ Fortune 500 willing to pay ก่อน vendor ของคุณจะได้ production budget expect ว่า customer จะเริ่มถาม "eval harness ของเราอยู่ไหน" ภายใน 6-12 เดือน ถ้า agent ของคุณไม่มี กลายเป็น differentiator เชิง negative — vendor ที่มี eval harness ที่ sign-off โดย domain expert จะ win deal

Ecosystem — NVIDIA ลงทุนใน Mercor มีนัยยะเชิง strategy — NVIDIA กำลัง build full-stack จาก GPU → model → agent platform → eval การถือหุ้นใน Mercor ทำให้มี distribution ให้ Agent Knowledge Foundation ที่ประกาศตุลาคม 2026 Salesforce เข้าเพราะ Agentforce Coworker ที่ 185K users ต้องการ eval infrastructure ของตัวเอง — pattern ที่ repeat คือ enterprise AI company ซื้อ labeling+eval company เพื่อ build moat ที่ model อย่างเดียวให้ไม่ได้

## Sources
- [Organizing human intelligence for the entire economy (Mercor blog)](https://www.mercor.com/blog/series-d/)
- [Mercor raises $750M at $20B valuation, doubling its worth with backing from Nvidia, Salesforce (Tech Startups)](https://techstartups.com/2026/11/11/mercor-raises-750m-at-20b-valuation-doubling-its-worth-in-just-over-a-year-with-backing-from-nvidia-salesforce/)
- [Mercor Raises $750M Series D at $20B Valuation to Expand AI Training (Unite.AI)](https://www.unite.ai/mercor-raises-750m-series-d-at-20b-valuation-to-expand-ai-training/)
- [Mercor's $20B Bet: Human Intelligence Is the Enterprise AI Moat (Futurum Group)](https://futurumgroup.com/insights/mercors-20b-bet-human-intelligence-is-the-enterprise-ai-moat/)

---

## Audio script
วันที่ 10 พฤศจิกายน Mercor ประกาศ Series D เจ็ดร้อยห้าสิบล้านเหรียญ ที่ valuation สองหมื่นล้านเหรียญ มี NVIDIA และ Salesforce ร่วมลงทุน valuation สูงขึ้น 2 เท่าจากตุลาคมปีก่อนใน 13 เดือน business เดิมของ Mercor คือ staffing domain expert แพทย์ นักกฎหมาย นักฟิสิกส์ SWE senior มา label และ grade output ของ frontier model ให้ OpenAI, Anthropic, Google, Meta ที่เป็น 4 ลูกค้ารายใหญ่สุด CEO บอกว่า run rate ถึง 3 พันล้านเหรียญ ถ้าเป็นจริงจะเป็น labeling company ที่ scale เร็วที่สุดในประวัติศาสตร์ ส่วนที่น่าสนใจกว่าคือ pivot ไปที่ enterprise evaluations — service ที่ Fortune 500 ซื้อเพื่อ eval agent ของตัวเองก่อน deploy production Mercor จะส่ง domain expert เข้าไปใช้ agent grade output และสร้าง eval harness เฉพาะ workflow ลูกค้า round นี้ settle thesis ที่ debate กันทั้งปีว่า AI moat อยู่ที่ model หรือ data Mercor ตอบว่า judgment ของ expert คือ data ที่ unique ที่สุด และ enterprise จะจ่าย premium เพื่อ eval harness ที่สะท้อน business logic จริง ไม่ใช่ benchmark public สำหรับ builder ถ้า agent คุณ deploy ให้ enterprise ใน vertical ที่ต้อง expert judgment การมี eval harness ที่ validated โดย domain expert กลายเป็น table stake ไม่ใช่ premium NVIDIA ลงทุนเพราะกำลัง build full stack จาก GPU ไป agent platform Salesforce เข้าเพราะ Agentforce Coworker ที่ 185,000 users ต้อง eval infrastructure ของตัวเอง caveat คือ 3 พันล้าน run rate เป็น CEO claim ไม่ใช่ audited และ expert staffing margin บางกว่า SaaS
