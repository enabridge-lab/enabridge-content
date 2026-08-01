---
date: 2026-08-01
slug: openai-gpt-5-6-luna-80-percent-price-cut-deepseek-pressure
topic: agentic-ai
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial isometric composition. Center: a giant price tag with two prices in
  neon — "$1 / $6" crossed out in red, replaced by bold "$0.20 / $1.20"; label
  above reads "GPT-5.6 LUNA — 80% CUT". Around the tag, three flag-labeled
  robotic arms — one US-flagged (OpenAI logo), one crossed-out China-flagged
  robot labeled "DEEPSEEK V4 PRO — 46% SHARE", and a smaller Terra tag reading
  "-20%". Beneath the composition, a horizontal token bar chart showing
  Chinese-origin models overtaking US-origin. Muted teal + electric-yellow
  palette, dramatic chiaroscuro, flat editorial style, 1:1 aspect, no real
  human faces (silhouettes only), text must render sharply at 200px thumbnail.
image: images/26-08-01-0610-02-openai-gpt-5-6-luna-80-percent-price-cut-deepseek-pressure.png
---

# OpenAI ตัดราคา Luna 80% ใน 3 สัปดาห์หลัง launch — DeepSeek V4 Pro กิน 46% ของ OpenRouter, pricing power ของ frontier lab กำลังละลาย

## TL;DR
- **30 ก.ค. (คำประกาศ OpenAI)** — GPT-5.6 **Luna** ตัดราคา **80%** ($1/$6 → **$0.20/$1.20** per million input/output tokens); **Terra** ตัด 20% ($2.50/$15 → $2/$12); **Sol** (flagship) ราคาเดิม $5/$30
- Launch เมื่อ **9 ก.ค.** — cut นี้เกิด **3 สัปดาห์หลัง GA** — signal เร่งจาก pricing pressure สูงกว่า OpenAI คาดเยอะ
- **CNBC (7 ก.ค.):** DeepSeek V4 Pro + Chinese models กิน **46% ของ US enterprise token usage บน OpenRouter** — peak แซง US-origin models ทั้งหมด; DeepSeek V4 Pro ราคา $0.435/$0.87 (มี standing 75% promo)
- Signal: **frontier model = commoditized ที่ mid-tier** — Luna เข้า price band ของ DeepSeek/Kimi K3; agent economics เปลี่ยน overnight — per-turn cost ลดได้ 60-80% ถ้า swap รุ่น + prompt cache

## เกิดอะไรขึ้น

วันที่ 30 กรกฎาคม OpenAI ปรับราคา API สำหรับสอง tier ของ GPT-5.6. **Luna** — mid-tier ที่ตั้งใจแข่ง cost-sensitive workload — ตัดราคา **80%** จาก $1 (input) / $6 (output) ต่อ million tokens ลงเหลือ **$0.20 / $1.20**. **Terra** — high-quality tier — ตัด 20% จาก $2.50/$15 เหลือ $2/$12. **Sol** — flagship ที่เพิ่งผ่าน US government customer-by-customer review — คงราคา $5/$30. Cut นี้ **effective ทันที** — และเกิดเพียง **3 สัปดาห์หลัง GA 9 กรกฎาคม** ของ GPT-5.6 family. Sam Altman ในทวีต 30 ก.ค. เขียนแค่ประโยคเดียว: "Luna is now $0.20/$1.20. Ship."

Context ที่ทำให้ move นี้ dramatic คือ CNBC investigation ที่ตีพิมพ์ **7 ก.ค.** (2 วันก่อน GPT-5.6 launch). Reporter วิเคราะห์ traffic ของ **OpenRouter** (aggregator ที่ enterprise dev ใช้เป็น router สำหรับ multi-model deployment) พบว่า **Chinese-origin models กิน 46% ของ US enterprise token usage**, และในบางวัน **แซง US-origin models ทั้งหมด**. Star performer คือ **DeepSeek V4 Pro** — ราคา $0.435 (input) / $0.87 (output) ต่อ million tokens, ได้ standing 75% promotional discount. Kimi K3 (Moonshot AI, IPO Hong Kong Q4 ที่ Enabridge cover ไปเมื่อ 25 ก.ค.) — ราคาใกล้ ๆ กัน. **DeepSeek + Moonshot** = tier ที่ OpenAI ยอมรับไม่ได้ว่าจะเสีย US enterprise share แบบนี้

Luna ใหม่ที่ $0.20/$1.20 = **แพงกว่า DeepSeek V4 Pro แค่ 45% input / 38% output** — เทียบกับก่อน cut ที่แพง 130%/590%. เข้า price band ของ Chinese tier ทันที. Sol ยังคงราคาไว้เพราะ position เป็น "highest capability, US-cleared, security-critical" — enterprise workload ที่ระบุใน RFP ว่าต้อง US-origin (defense, healthcare, regulated finance) จ่ายไม่คุ้มจะ switch. **Luna ที่กลาง = commoditized; Sol ที่บน = premium**; Terra ที่ 20% cut = ท่าที defensive แต่ยังพยายาม hold margin. Timing สำคัญ: cut นี้เกิด **1 วันก่อน Amazon Q2 earnings** (30 ก.ค.) และ **2 วันหลัง Anthropic disclose Claude Mythos breach** (ที่ Enabridge cover ในเรื่อง #3 วันนี้) — OpenAI แย่ง airtime + narrative

## ทำไมสำคัญ

**Mid-tier model = officially commoditized**. ปี 2024-2025 pricing wars อยู่ที่ small model (gpt-4o-mini vs Claude Haiku vs DeepSeek Coder) — ระดับ centi-cents ต่อ million tokens ที่ enterprise ไม่ค่อยรู้สึก. ปี 2026 — pricing pressure เลื่อนขึ้น **mid-tier ที่รับ agent turn ส่วนใหญ่** (RAG, tool use, workflow orchestration, agent-to-agent coordination). Anthropic Claude Sonnet 5.5 อยู่ที่ $3/$15 (Terra tier); Google Gemini 3.6 Flash ~$0.30/$1.20. **Luna ตัดมาที่ $0.20/$1.20 = จุด Chomsky ของ mid-tier** — ทุก vendor ที่อยู่บนราคานี้ ต้อง match ภายใน Q3 หรือเสีย OpenRouter/AWS Bedrock share. คาดว่า Anthropic Sonnet 5.5 → cut 30-40% ภายในเดือน ส.ค. (มี Q4 IPO pressure); Gemini 3.6 Flash → cut อีก 30% ตาม

**Agent economics เปลี่ยน overnight**. Agent ที่รัน 10-turn conversation กับ ~500 output tokens/turn = ~5,000 output tokens/session; ที่ราคา $6 → $1.20 = ค่า inference ต่อ session **ลดจาก 3 cent เหลือ 0.6 cent** (80% saving). Enterprise ที่รัน 1M agent session/day (ระดับ Fortune 500 customer service, coding assistant) = **saving ~$24,000/day = $8.8M/year**. Payback period ของการ **rewrite prompt + swap model** ในระบบ production เดิม สั้นลงจาก ~6 เดือน เหลือ ~3-4 สัปดาห์ = FinOps team + AI platform team จะเริ่ม re-audit ทุก agent pipeline ทันที Q3

**Chinese model share = geopolitical + technical shock พร้อมกัน**. 46% ของ OpenRouter traffic = fact ที่ไม่มี AI vendor US ยอมออกเสียงมาก่อน. Anthropic Claude Sonnet 5.5 มีคำวิพากษ์บ่อยว่า "over-refuses" — DeepSeek V4 Pro / Kimi K3 ผ่อนกว่า, tool-use accuracy ใกล้เคียง Claude 4.7 บน SWE-Bench. Enterprise dev ที่ต้องการ **model ที่ agree to task without extensive negotiation** สำหรับ workflow automation → Chinese tier ชนะ **usability + cost**. คำถาม US regulator ที่จะดังขึ้น Q4: มี export control หรือ approved-vendor list สำหรับ agent workload ที่ท้าทาย DeepSeek/Moonshot ไหม? — probably ไม่มี, เพราะ open-weight release ทำให้ enforce ยาก

## มุม AI Agent Platform

**สำหรับ builders:** ถ้ากำลังสร้าง agent framework — **model tier selection ต้องเป็น first-class config ไม่ใช่ hardcoded**. Framework ที่ default hardcode Claude Sonnet หรือ GPT-5.6 Terra จะ **overprice user** ทันที; ควร expose **model-tier abstraction** (low / mid / high; hi-quality / high-cost / low-latency / low-cost) และให้ orchestrator route ตาม task complexity. Semantic routing (คำถามง่าย → Luna/DeepSeek; คำถามยาก → Sol/Opus 5) จะ **cut inference bill 60-80%** สำหรับ user ทั่วไป. LangGraph, CrewAI, และ AutoGen ที่ยัง single-model = obsolete ภายใน Q4

**สำหรับ users/business (Fortune 500 + Thai SET50):** ประชุม FinOps + AI platform team ในสัปดาห์นี้. คำถามที่ต้องตอบ: (1) *"agent workflow ไหนที่รัน Sol/Opus โดยไม่จำเป็น?"* — โดย default ควรใช้ Luna/Sonnet ก่อน, upgrade tier เฉพาะเมื่อ eval fail. (2) *"prompt caching enable ครบหรือยัง?"* — Luna + prompt cache 90% hit rate = per-turn cost ลดอีก ~50%. (3) *"vendor lock-in คือ risk หรือประหยัด?"* — enterprise ที่รัน multi-model ผ่าน OpenRouter/Bedrock ปรับ tier ได้ ~2-3 วัน; ที่ lock กับ vendor เดียวปรับได้ ~2-3 เดือน (ต้องรอ vendor cut ให้)

**สำหรับ ecosystem:** **สอง sub-category ที่ Q3 จะระเบิด**: (1) **semantic model router** (Portkey, Kong AI Gateway, AWS Bedrock router — ต้องมี real-time model economics engine, budget cap, fallback), (2) **prompt cache optimizer** (rewrite prompt เพื่อ maximize cache hit — เป็น service ที่ vendor ยังไม่ standardize). Loser: legacy AI observability ที่ track แค่ token count ไม่ track cost-per-outcome — Groundcover (ที่ Enabridge cover ในเรื่อง #4 วันนี้) เข้ามาตรงจุดนี้พอดี. VC signal: กองทุนที่เพิ่ง deploy ใน "premium closed-weight AI vendor" ปี 2025 (Sequoia, a16z ใน OpenAI/Anthropic secondary) จะเจอ **compression valuation** ถ้า pricing power ต่อไปอีก 2-3 ไตรมาส

## Sources
- [OpenAI Cuts GPT-5.6 Pricing Up To 80%, As AI Costs Come Under Scrutiny — Forbes](https://www.forbes.com/sites/rachelwells/2026/07/31/openai-cuts-gpt-56-pricing-up-to-80-as-ai-costs-come-under-scrutiny/)
- [OpenAI cuts prices for two of its GPT-5.6 AI models as companies grow sensitive to costs — CNBC](https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html)
- [OpenAI Just Cut GPT-5.6 Luna's Price by 80 Percent – and That Tells You Where the Pressure Is Coming From — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/openai-just-cut-gpt-5-013753910.html)
- [OpenAI cuts GPT-5.6 Luna and Terra prices by up to 80% — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/openai-cuts-gpt-5-6-173045044.html)
- [GPT-5.6 Price Cut: Luna 80% Cheaper, What It Means — Build Fast With AI](https://www.buildfastwithai.com/blogs/gpt-5-6-price-cut)
- [AI just got cheaper: OpenAI slashes prices by up to 80% — American Bazaar](https://americanbazaaronline.com/2026/07/31/ai-just-got-cheaper-openai-slashes-prices-by-up-to-80-485573/)

---

## Audio script
วันนี้เช้าที่ Enabridge เรื่องราคา OpenAI ที่จะเปลี่ยน agent economics ของทุกคน. วันที่ 30 กรกฎาคม OpenAI ตัดราคา GPT-5.6 Luna 80% จาก 1 ดอลลาร์ต่อ input tokens ล้าน กับ 6 ดอลลาร์ต่อ output tokens ล้าน เหลือ 0.20 กับ 1.20. Terra ตัด 20% เหลือ 2 กับ 12. Sol flagship คงเดิม 5 กับ 30. Cut นี้เกิด 3 สัปดาห์หลัง GA ของ GPT-5.6 family เมื่อ 9 กรกฎาคม.

Context ที่ทำให้เข้าใจ. CNBC ตีพิมพ์ investigation 7 กรกฎาคม. DeepSeek V4 Pro กับ Chinese models กิน 46% ของ US enterprise token usage บน OpenRouter. บางวันแซง US origin models ทั้งหมด. DeepSeek V4 Pro ราคา 0.435 กับ 0.87 มี standing 75% promotional. Kimi K3 ราคาใกล้กัน. Luna ที่ตัดใหม่ = แพงกว่า DeepSeek แค่ 45% กับ 38% เทียบก่อน cut ที่แพง 130% กับ 590%.

Signal ที่อยากให้เห็น. Mid tier model = officially commoditized. ปี 2024-2025 pricing wars อยู่ที่ small model. ปี 2026 pressure เลื่อนขึ้น mid tier ที่รับ agent turn ส่วนใหญ่. Claude Sonnet 5.5 อยู่ที่ 3 กับ 15. Gemini 3.6 Flash 0.30 กับ 1.20. Luna ตัดมาที่ 0.20 กับ 1.20 = จุด Chomsky ของ mid tier. Anthropic น่าจะ cut 30-40% ในเดือนสิงหาคม.

Agent economics เปลี่ยน overnight. Agent ที่รัน 10 turn conversation ค่า inference ต่อ session ลดจาก 3 cent เหลือ 0.6 cent. Enterprise ที่รัน 1 ล้าน session ต่อวัน saving 24,000 ดอลลาร์ต่อวัน. Payback period ของ rewrite prompt กับ swap model ลดจาก 6 เดือน เหลือ 3-4 สัปดาห์.

สำหรับ enterprise ไทย SET50. ประชุม FinOps กับ AI platform team สัปดาห์นี้. คำถาม 3 ข้อ. Agent workflow ไหนรัน Sol หรือ Opus โดยไม่จำเป็น. Prompt caching enable ครบหรือยัง. Vendor lock in คือ risk หรือประหยัด. Multi model ผ่าน OpenRouter หรือ Bedrock ปรับได้ 2-3 วัน. Lock vendor เดียวปรับได้ 2-3 เดือน.

สำหรับ builders ที่ทำ agent framework. Model tier selection ต้องเป็น first class config. Framework ที่ hardcode Claude Sonnet หรือ GPT-5.6 Terra จะ overprice user. Semantic routing คำถามง่ายไป Luna หรือ DeepSeek คำถามยากไป Sol หรือ Opus 5 จะ cut bill 60-80%. LangGraph CrewAI AutoGen ที่ยัง single model = obsolete ภายใน Q4. คุยกันวันหน้าครับ.
