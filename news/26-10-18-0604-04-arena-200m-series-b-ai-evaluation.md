---
date: 2026-10-18
slug: arena-200m-series-b-ai-evaluation
topic: use-case
reading_time_min: 4
sources: 3
image_prompt: |
  Editorial isometric illustration of a glowing arena-style stadium made of
  circuitry with model gladiators (abstract geometric shields, no real
  brands) battling on the sand. Above the arena a floating banner reads
  "ARENA" and three stacked numbers tower beside it: "$100M ARR", "$3.1B",
  "8 MONTHS". A ticket booth below spells "LMArena 2023 → Arena 2026".
  Cobalt and amber palette, high contrast for 200px thumbnails, 1:1 aspect,
  no real human faces.
image: images/26-10-18-0604-04-arena-200m-series-b-ai-evaluation.png
---

# Arena ปิด Series B $200M ที่ $3.1B — เรียน $100M "ARR" ภายใน 8 เดือนจาก leaderboard ของ UC Berkeley

## TL;DR
- 8 ต.ค. Arena (เดิม LMArena, UC Berkeley research project) ปิด **Series B $200M** ที่ **$3.1B valuation** — Lightspeed + Khosla co-lead
- 8 เดือนหลังเปิด commercial product, Arena ชน **$100M annualized run-rate** — แต่ CEO Angelopoulos clarify ว่า **ไม่ใช่ ARR แบบ SaaS** เป็น consumption-based คือเก็บต่อ eval call จริง ไม่ใช่ recurring contract
- Series A ม.ค. 2026 คือ $150M ที่ $1.7B valuation ตอน annualized revenue $30M — คือ **8 เดือน จาก $30M → $100M, valuation +84%**
- Pattern ที่ emerg: **evaluation infrastructure** กลายเป็น money-maker จริง — ไม่ใช่ research tool อีกต่อไป เพราะทุกคน (lab + enterprise + regulator) ต้องรู้ว่า agent / model ของตัวเองเทียบคู่แข่งยังไง

## เกิดอะไรขึ้น

วันพุธที่ 8 ต.ค. **Arena** — เดิมชื่อ **LMArena**, เริ่มจาก research project ของ UC Berkeley ในปี 2023 ที่ให้ user โหวตเทียบ model แบบ blind — ประกาศปิด **Series B $200 ล้าน** ที่ valuation **$3.1 พันล้าน**, co-lead โดย Lightspeed Venture Partners กับ Khosla Ventures. ตามข่าว Angel Investors Network รายงานตรงจาก blog post ของ Arena เองวันเดียวกัน. ก่อนหน้านี้ 9 เดือน (ม.ค. 2026) Arena เพิ่งปิด Series A $150M ที่ $1.7B valuation ตอน annualized revenue $30M

ตัวเลขที่ CEO Anastasios Angelopoulos ย้ำคือ Arena ชน **$100M annualized run-rate** ภายใน 8 เดือนหลังเปิด commercial product. แต่เขา hedge ชัดเจน (ซึ่ง rare สำหรับ founder) ว่า: **ไม่ใช่ ARR แบบ SaaS** — Arena ขายแบบ consumption (คิดเงินต่อ eval call) ไม่ใช่ subscription recurring. คือ run-rate แบบ "ถ้าเดือนนี้ยืนราวนี้ตลอดปีจะได้ $100M" ไม่ใช่ "มี contract $100M ล็อคไว้". ความแตกต่างนี้สำคัญเพราะ consumption model volatility สูงกว่า — model ใหม่ hot ขึ้น traffic กระจาย, lab รุ่นหนึ่งลด eval cycle ก็ลงได้

Product ของ Arena ตอนนี้มีสามเลเยอร์: (1) **public leaderboard** (เดิมที่ให้ user vote blind, free), (2) **enterprise eval platform** — API ให้บริษัทรัน custom benchmark ของตัวเอง (regulated industry, domain-specific), (3) **model marketplace routing** — ขาย optimal routing ให้ enterprise user ที่ไม่อยาก lock vendor เดียว. revenue หลักน่าจะ (2) + (3) เพราะ (1) ยังฟรี

และข้อมูลที่ dealroom ยืนยัน: Arena คือ **top-of-funnel** ของ model consumption ของอุตสาหกรรม — เมื่อ model ใหม่ release leaderboard ของ Arena คือจุดที่ enterprise + dev ไปดูก่อน. ทำให้ lab ส่ง model เข้า Arena ก่อน release public เป็น standard — คือ Arena มี **leverage ที่ unique**: lab วาง pre-release ให้, enterprise จ่ายเพื่อ eval ของตัวเอง — ทั้ง supply + demand side

## ทำไมสำคัญ

$100M "ARR" ของ Arena คือ **data point ที่ยืนยันว่า evaluation layer เป็น business** ไม่ใช่ research. ปีที่แล้วตอนลัยทาง AI eval ยังมอง HumanEval, MMLU, Chatbot Arena เป็น academic metric ที่ไม่มีใครจ่ายซื้อ — ตอนนี้ Angelopoulos โชว์ว่า enterprise จ่ายจริงเพราะ 2 เหตุผล: (1) **compliance** — ต้องมี benchmark reproducible ที่ auditor ยอมรับ, (2) **procurement** — บริษัท multi-model (ที่ไม่ lock vendor เดียว) ต้องรู้ว่า model ไหนดีกว่าสำหรับ task ของตัวเอง ก่อนจ่าย premium ของ Opus หรือ GPT-6

Pattern ที่น่าสังเกตอีกตัว: Arena คือ **"shovel seller" ของ model gold rush** — เหมือน Snowflake, Databricks ขายทาง data layer โดยไม่ compete กับ cloud provider โดยตรง. การที่ Lightspeed + Khosla เล่น Series B $200M ที่ valuation x3 ใน 9 เดือน บอกว่า VC ชั้นนำ view evaluation infrastructure คือ moat ที่กว้างกว่า coding assistant หรือ agent framework (ที่แข่งขันดุ)

แต่ risk ที่ควร note: Angelopoulos เองยอม hedge "ไม่ใช่ ARR แบบ SaaS" ซึ่ง rare. ถ้า model ตลาด commoditize (routing กันเองได้, agent framework ให้ default eval ใน OSS) revenue model consumption ของ Arena อาจ volatile กว่า SaaS classic. และ competitor open-source อย่าง HELM (Stanford), LMSYS fork, และ internal benchmark ของ enterprise เอง อาจกิน market share

## มุม AI Agent Platform

สำหรับ **Builders** (framework + agent runtime): **integrate Arena eval early** — ถ้า agent product ของคุณไม่มี metric reproducible ที่ปัญหาจริงของลูกค้า enterprise จะไม่กล้า deploy. และ pattern "ขาย eval ให้ enterprise ที่ไม่ lock vendor" คือ opportunity ที่ยังเล็ก — vertical eval (legal, medical, financial) ยังไม่มี Arena ของตัวเอง. สำหรับ **Users / Business**: ถ้าทีม procurement ยัง pick model ด้วย demo ของ vendor คือสัญญาณที่ pause — ควรมี internal benchmark หรือ subscribe eval platform ที่ independent. การ run eval ของตัวเองก่อน sign contract 7-figure เป็น default สมัยใหม่. สำหรับ **Ecosystem**: lab ปิด model (OpenAI, Anthropic, Google) มี incentive ให้ Arena ตีความ metric ของตัวเองในทางบวก — เป็นความสัมพันธ์ที่ยัง healthy แต่ต้องระวังเวลา Arena ขึ้นเป็น gatekeeper จริง จะเริ่มมีคำถามเรื่อง bias เหมือน Gartner Magic Quadrant

## Sources
- [Arena, the AI leaderboard everyone uses, is now a $100M business (TechCrunch)](https://techcrunch.com/2026/06/29/arena-the-ai-leaderboard-everyone-uses-is-now-a-100m-business/)
- [Arena AI evaluations hit $100M ARR eight months after launch (aiweekly)](https://aiweekly.co/alerts/arena-ai-evaluations-hit-100m-arr-eight-months-after-launch)
- [Arena Raises $200M Series B at $3.1B Valuation (Angel Investors Network)](https://angelinvestorsnetwork.com/venture-capital/arena-raises-200m-in-series-b-funding-at-3-1b-valuation)

---

## Audio script
Arena ที่ย่อจาก LMArena ไอ eval leaderboard ที่เริ่มจาก UC Berkeley research ปี 2023 เพิ่งปิด Series B $200 ล้าน ที่ valuation $3.1 พันล้าน Lightspeed กับ Khosla co-lead. ตัวเลขที่สวยคือ 8 เดือนหลังเปิด commercial product Arena ชน $100 ล้าน annualized run-rate. แต่ CEO Angelopoulos hedge ชัดเจนซึ่ง rare สำหรับ founder ว่าไม่ใช่ ARR แบบ SaaS เป็น consumption-based คือเก็บต่อ eval call จริง ไม่ใช่ contract recurring. จาก Series A มกราคม $30M revenue ที่ $1.7B valuation ไปถึง Series B ตุลาคม $100M run-rate ที่ $3.1B — valuation +84% ใน 9 เดือน. ที่น่าสังเกตคือ Arena ขาย evaluation layer ซึ่งปีที่แล้วยังมองเป็น academic metric ที่ไม่มีใครจ่าย ตอนนี้ enterprise จ่ายจริงด้วยสองเหตุผล compliance ต้องมี benchmark auditor ยอมรับ และ procurement บริษัทที่ไม่ lock vendor เดียวต้องรู้ว่า model ไหนดีกว่าก่อนจ่าย premium. Pattern คือ Arena เป็น shovel seller ของ model gold rush เหมือน Snowflake ที่ไม่ compete กับ cloud provider โดยตรง. บทเรียน ถ้าทีม procurement คุณยัง pick model ด้วย demo ของ vendor คือสัญญาณที่ควร pause ควรมี internal benchmark หรือ subscribe eval platform ที่ independent ก่อน sign contract เจ็ดหลัก.
