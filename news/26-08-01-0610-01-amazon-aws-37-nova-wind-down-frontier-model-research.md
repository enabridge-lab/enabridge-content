---
date: 2026-08-01
slug: amazon-aws-37-nova-wind-down-frontier-model-research
topic: agentic-ai
reading_time_min: 5
sources: 7
image_prompt: |
  Editorial isometric split composition. Left side: a rising AWS-style bar chart
  labeled "AWS +37% YoY" with two neon stack labels — "AI RUN RATE >$25B" and
  "CHIPS RUN RATE >$25B" — flowing into a bold "$220B CAPEX" ribbon. Right side:
  a warehouse floor with four Nova-branded crates being wheeled into a dim room
  labeled "KTLO", while a bright doorway labeled "FRONTIER MODEL RESEARCH" glows
  behind Pieter-shaped silhouette. Between them a large headline "ONE MODEL, ONE
  BET". Deep AWS-orange + Anthropic-copper palette, chiaroscuro editorial style,
  1:1 aspect, no real human faces (silhouettes only), text must render sharply
  at 200px thumbnail.
image: images/26-08-01-0610-01-amazon-aws-37-nova-wind-down-frontier-model-research.png
---

# AWS โต 37% เร็วสุดใน 18 ไตรมาส, Nova เข้าโหมด KTLO — Amazon เลิกทำหลาย model, ทุ่มทุกอย่างเข้า Frontier Model Research

## TL;DR
- **Q2 2026 (30 ก.ค.)** — AWS revenue $42.2B (+37% YoY, เร็วสุดใน 18 ไตรมาส), AI run rate + Chips run rate **แตะ $25B+ ต่อ business** (triple-digit growth); total company revenue >$200B ครั้งแรก; Jassy บอก AWS "line of sight" ถึง trillion-dollar run rate
- **28 ก.ค. (ก่อนเลข earnings 2 วัน)** — Amazon deprecate **Nova Premier / Omni / Reel / Canvas** (KTLO mode); ย้ายวิศวกร + compute เข้า **Frontier Model Research (FMR)** ที่ Pieter Abbeel (UC Berkeley, ex-Covariant CEO) lead; เป้า debut re:Invent ปลายปี
- Capex 2026 ขยับจาก $200B เป็น **$220B**; profit Q2 tripled ส่วนใหญ่จาก **Anthropic equity mark-to-market**
- Signal: **hyperscaler ที่แข่ง foundation model เองไม่ไหว = เลือก "one big bet" + double down infrastructure** — AWS จะเป็น landlord ของ agent economy, ไม่ใช่ผู้เล่นเอง

## เกิดอะไรขึ้น

วันที่ 30 กรกฎาคม Amazon รายงาน Q2 2026 ที่ Wall Street ไม่คาดว่าจะแรงขนาดนี้. AWS revenue $42.2 พันล้าน — **โต 37% YoY เร็วที่สุดในรอบ 18 ไตรมาส** (analysts รอ 31%); annualized run rate ทะลุ $169B. Total revenue Amazon ข้าม $200B ต่อไตรมาสเป็นครั้งแรกในประวัติศาสตร์บริษัท. ที่เด่นกว่านั้น — Andy Jassy บอกในโทรศัพท์ analyst ว่า AWS's **AI business แตะ run rate >$25B** และ **AWS Chips (Trainium + Inferentia + Graviton) แตะ >$25B** เช่นกัน; ทั้งสอง triple-digit growth. Capex ทั้งปี upgrade จาก $200B → **$220B**. Profit Q2 tripled — Wall Street focus ที่ตัวเลขนี้ แต่ประมาณ half มาจาก mark-to-market **Anthropic equity** (Amazon ลง $8B ตั้งแต่ปี 2024, ตอนนี้ valuation Anthropic ใกล้ $1T ตาม IPO filing เดือน มิ.ย.)

แต่สองวันก่อน earnings — 28 ก.ค. — Bloomberg + The Information รายงาน strategy shift ที่ contrast สุดขั้วกับ narrative "AWS AI booming": Amazon เข้าโหมด **wind-down active development** สำหรับ **Nova Premier** (flagship LLM), **Nova Omni** (multimodal), **Nova Reel** (video gen), **Nova Canvas** (image gen). ทั้งสี่ตัวยัง supported สำหรับ existing customer แต่ internally เรียกโหมดนี้ว่า **"KTLO" (Keep The Lights On)** — ไม่มี roadmap ใหม่. Nova 2 Lite / Nova 2 Sonic / Nova Forge (customization service) ยังไปต่อ. วิศวกรและ compute ย้ายเข้า **Frontier Model Research (FMR)** — team ใหม่ที่ Pieter Abbeel เป็นหัวหน้า

Pieter Abbeel ไม่ใช่ชื่อสุ่ม — UC Berkeley professor ที่ Amazon acquire ผ่าน Covariant (robotics + foundation model startup) ปี 2024. ที่ FMR **จะสร้าง one flagship foundation model** เพื่อ debut ที่ re:Invent ปลายปี (อาจใช้ brand Nova ต่อ). Move นี้ตามหลัง layoff ที่ Amazon AGI group เมื่อไม่กี่เดือน. Framework ที่ Jassy สื่อสารกับ analyst ค่อนข้าง blunt — "customer AI demand striking, AWS could be a trillion-dollar business, we have clear line of sight to strong financial returns on our AI bet". Bet นั้นชัดเจนขึ้น: **Anthropic (foundation model) + own chips (Trainium/Inferentia) + one focused frontier project (FMR) = AWS's stack**, ไม่ใช่ Nova family ที่กระจายไปหลายทาง

## ทำไมสำคัญ

**Hyperscaler foundation model race กำลัง converge เป็น "one bet, one model" architecture**. Amazon เพิ่งประกาศ; Google เจอ delay กับ Gemini 3.5 Pro (Bloomberg รายงาน 16 ก.ค. ว่าล่ากว่า plan หลายเดือน, coding อ่อน); Meta ยังไม่เปิดหน้าตา Llama 5 หลังคำสัญญาของ Zuckerberg. Pattern เดียวกัน — 2025-2026 พิสูจน์ว่า foundation model เป็น winner-take-most (OpenAI + Anthropic + DeepSeek/Kimi), ต่อให้เป็น hyperscaler ก็ต้องเลือก **ลงทุนกับ frontier lab (Anthropic, xAI post-SpaceX merge) + ทำ 1 own model** หรือ **infrastructure play เท่านั้น**. Amazon ตัดสินใจแบบแรก — bet on Anthropic + FMR (Abbeel's one-model project) + own chips + agent runtime services (Amazon Quick, AWS Continuum). ทิ้ง 4 Nova models = ตัด opex ที่ไม่ scale, focus wattage

**Anthropic equity trade = quiet biggest ROI of the year**. $8B stake จาก 2024, ตอนนี้ Anthropic ยิ่งถ้าเข้า SEC IPO ที่ $1T target — Amazon's paper gain ประมาณ $60-70B (assume ~7% stake). Q2 profit ที่ triple = ส่วนใหญ่ mark-to-market จากตรงนี้. Bezos-era Amazon Prime moment ครั้งใหม่ — แต่คราวนี้เป็น **strategic minority investment ใน frontier lab** แทนที่จะเป็น consumer subscription. คำถามที่ Wall Street ยังไม่ถามดัง ๆ: ถ้า Amazon own Anthropic equity, ทำไมต้องแข่ง? Answer implicit ของ FMR = **diversify + hedge** ถ้า Anthropic hit ceiling ก่อน AWS ต้องการ

**Capex $220B = infrastructure land grab ที่ crowd out ทุกคน**. เทียบง่าย ๆ: Meta capex 2026 ประมาณ $145B, Microsoft $110B, Google $95B — Amazon อยู่ที่ระดับ **combined ของ Google + Microsoft**. ไม่ใช่แค่ data center — chip (Trainium 3 production ramp), power (deal นิวเคลียร์ Talen Energy), fiber, edge. Position: AWS จะเป็น **landlord ของ AI + agent economy** — vendor ทุกตัวใน stack (ตั้งแต่ Anthropic ถึง Groundcover ถึง Salesforce Agentforce) รัน production traffic บน AWS. Nova wind-down = ยอมรับว่า model layer แข่งไม่ทัน, แต่ **layer ต่ำกว่านั้น (compute, storage, agent runtime, networking) เก็บกำไรจากทุกคน**

## มุม AI Agent Platform

**สำหรับ builders:** ถ้ากำลังสร้าง agent framework / runtime, ต้อง **treat AWS Bedrock + Anthropic API + AWS Continuum (agent orchestration service, GA คาด re:Invent) เป็น first-class deployment target**. Amazon Quick (agent-facing IDE) เพิ่งเปิด beta — คู่แข่งของ Claude Code SDK + Copilot Workspace. Framework ที่ optimize สำหรับ Trainium 3 inference cost (~50% ถูกกว่า H100) จะได้ price advantage 6-12 เดือน. อย่าเสียเวลาสร้างต่อกับ Nova Premier — ไป Claude Opus 5 หรือ Sonnet 5.5 ผ่าน Bedrock

**สำหรับ users/business (Fortune 500 + Thai SET50):** review vendor commitment ต่อ Nova — ถ้ามี **RFP ที่ระบุ Nova Premier / Omni / Reel / Canvas เป็น required capability**, ต้อง ask vendor migration path ทันที (KTLO = ไม่มี new feature ออกอีก). ในเวลาเดียวกัน — **AWS AI + chips $25B run rate + Bedrock coverage ของ Claude + DeepSeek V4 + Llama 5 preview** ทำให้ AWS = safest default agent runtime สำหรับ enterprise regulated workload. Cost optimization: switch agent inference จาก Sol/Opus → Luna (หลัง OpenAI 80% cut) หรือ DeepSeek V4 Pro (46% share ของ OpenRouter traffic แล้ว) จะกด per-turn cost 60-80%

**สำหรับ ecosystem:** hyperscaler foundation model = losing game (Amazon ตัวที่ 3 ที่ยอมรับ implicit, ตาม Meta + Google's Gemini delay). ผู้ชนะรอบต่อไป = (1) frontier lab ที่มี IPO exit chart (Anthropic Q4, OpenAI 2027E, xAI post-SpaceX merge), (2) **agent-native infrastructure vendor** (Groundcover สำหรับ observability, Hush สำหรับ identity, Encore สำหรับ outcome — สาม category ที่ Enabridge cover ไปเมื่อวาน), (3) chip alternative (Groq, Cerebras, Trainium 3 partner). Amazon FMR = ลูกโป่งลาสต์ hyperscaler ก่อนตลาด model layer เข้าสู่ **duopoly + China** ตอนสิ้นปี 2026

## Sources
- [Amazon Q2 2026 earnings: AWS grows 37%, revenue tops $200B — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/amazon-q2-2026-earnings-aws-204411872.html)
- [Amazon (AMZN) Q2 earnings report 2026 — CNBC](https://www.cnbc.com/2026/07/30/amazon-amzn-q2-earnings-report-2026.html)
- [Q2 earnings: CEO Andy Jassy on why AWS is booming — About Amazon](https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-aws-revenue-growth-q2-2026-earnings)
- [Amazon Q2 Profit More Than Triples As Anthropic AI Bet Pays Off Big Time — The Wrap](https://www.thewrap.com/industry-news/business/amazon-earnings-q2-2026/)
- [Amazon winds down most of its Nova AI models — TNW](https://thenextweb.com/news/amazon-winds-down-nova-ai-models-frontier-model-research)
- [Amazon reportedly scales back its Nova AI models and bets on a new Frontier research team — The Decoder](https://the-decoder.com/amazon-reportedly-scales-back-its-nova-ai-models-and-bets-on-a-new-frontier-research-team/)
- [Amazon Overhauls AI Strategy as Flagship Nova Models Wind Down — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/amazon-overhauls-ai-strategy-flagship-174413868.html)

---

## Audio script
วันนี้เช้าที่ Enabridge อยากให้ทุกคนเห็น pattern ที่เกิดใน 48 ชั่วโมงที่ Amazon. Q2 earnings ประกาศ 30 กรกฎาคม. AWS revenue สี่หมื่นสองพันล้าน โต 37% YoY เร็วสุดในรอบ 18 ไตรมาส. AI run rate กับ Chips run rate ทะลุ 25 พันล้านต่อ business. Triple digit growth ทั้งสองส่วน. Total revenue ข้ามสองแสนล้านต่อไตรมาสครั้งแรกในประวัติศาสตร์. Capex ทั้งปี upgrade เป็น 220 พันล้าน.

แต่สองวันก่อน earnings Amazon ประกาศเงียบ ๆ ว่าจะ wind down Nova Premier Omni Reel Canvas. ทั้งสี่โมเดล flagship. Internally เรียก KTLO mode คือ keep the lights on ไม่มี roadmap ใหม่. วิศวกรกับ compute ย้ายเข้า Frontier Model Research นำโดย Pieter Abbeel จาก UC Berkeley ที่ Amazon acquire ผ่าน Covariant ปี 2024. เป้าออก one flagship model ที่ re:Invent ปลายปี อาจใช้ brand Nova ต่อ.

Signal ที่อยากให้เห็น. Hyperscaler foundation model race กำลัง converge เป็น one bet architecture. Google delay Gemini 3.5 Pro. Meta ยังไม่เปิดหน้า Llama 5. Amazon ตัด 4 Nova models. Pattern เดียวกัน foundation model เป็น winner take most. ต่อให้เป็น hyperscaler ก็ต้องเลือกลงกับ frontier lab แล้วทำ own model แค่ตัวเดียว. Amazon bet on Anthropic กับ FMR กับ own chips.

Anthropic equity trade คือ quiet biggest ROI. 8 พันล้านลงตั้งแต่ปี 2024 ตอนนี้ Anthropic ใกล้ trillion dollar IPO. Amazon paper gain ประมาณ 60-70 พันล้าน. Q2 profit ที่ tripled ส่วนใหญ่มาจากตรงนี้.

สำหรับ enterprise ไทย SET50. ถ้ามี RFP ที่ระบุ Nova Premier Omni Reel Canvas ต้องถาม vendor migration path ทันที เพราะไม่มี new feature ออกอีก. ในเวลาเดียวกัน AWS Bedrock กับ Claude Opus 5 กับ Sonnet 5.5 กับ DeepSeek V4 Pro coverage ทำให้ AWS เป็น safest default agent runtime. Cost switch จาก Sol หรือ Opus ไป Luna หลัง OpenAI ตัดราคา 80% หรือ DeepSeek V4 Pro จะกด per-turn cost 60-80%.

สำหรับ builders ที่ทำ agent framework. Focus optimize สำหรับ Trainium 3 inference cost. ถูกกว่า H100 ประมาณครึ่ง. อย่าเสียเวลาสร้างต่อกับ Nova Premier. ไป Claude Opus 5 หรือ Sonnet 5.5 ผ่าน Bedrock. คุยกันวันหน้าครับ.
