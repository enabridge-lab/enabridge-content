---
date: 2026-07-15
slug: grok-4-5-cursor-trained-2-6-coding-agent-commodity
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial isometric hero illustration of a boxing ring at dusk. In one
  corner a giant glowing model card labeled "GROK 4.5" with a sub-label
  "$2 IN / $6 OUT" and a small "CURSOR-TRAINED" badge pinned on it. In
  the opposite corner two stacked frontier boxes labeled "CLAUDE OPUS"
  and "GPT-5.6 SOL" priced "$15+ / $75+". A stadium jumbotron overhead
  reads "OPUS-CLASS. LOWER COST." The referee holds a scoreboard reading
  "COMMODITY ROUND: CODING AGENT". Bold text readable at 200px thumbnail,
  high-contrast teal-and-amber cinematic palette, 1:1 aspect, no real
  human faces.
image: images/26-07-15-0610-03-grok-4-5-cursor-trained-2-6-coding-agent-commodity.png
---

# SpaceXAI ปล่อย Grok 4.5 ที่ Cursor เทรน — ยิง $2/$6 ทุบราคา coding agent, สัญญาณ commodity phase เร่งขึ้น

## TL;DR
- 8 ก.ค. SpaceXAI ปล่อย **Grok 4.5** — coding + agentic model ที่ **Cursor ร่วมเทรน** ด้วย real developer interaction data; ราคา **$2 input / $6 output per M tokens** — undercut Claude Opus + GPT-5.6 Sol ราว 5–15 เท่า
- Elon Musk เรียกว่า **"Opus-class model แต่เร็ว, token-efficient, ต้นทุนต่ำกว่า"**; ใช้เป็น default ใน **Grok Build** (terminal coding agent) และ **Cursor ทุก plan**; ทำได้ทั้ง code + Excel/PowerPoint/Word — knowledge work commoditize เพิ่มด้วย
- Signal: **coding agent เข้าเฟส price war**; Cursor ที่ SpaceXAI acquire ต้นปีนี้ทำ dual-role — เป็น distribution channel + training data source ที่ competitor เข้าถึงไม่ได้; ราคาต่ำนี้บังคับให้ Anthropic + OpenAI ต้อง revise pricing หรือหา differentiation ใหม่ก่อนสิ้น Q3

## เกิดอะไรขึ้น
วันที่ 8 ก.ค. SpaceXAI (บริษัท AI ของ Elon Musk ที่ IPO ต้นปีนี้และ acquire Cursor เดือน เม.ย.) ปล่อย **Grok 4.5** เป็น flagship coding + agentic model. Bloomberg ตี exclusive ก่อน 24 ชั่วโมงว่าเป็น "the first Grok built with Cursor's help" — เป็นครั้งแรกที่ IDE-maker + foundation model lab ผลิต model ร่วมกันตั้งแต่ training phase. Cursor's interaction data (จาก ~5M active developer) "played a central role, feeding the model real-world signals on how engineers write, review, and debug code" — training set ที่ OpenAI/Anthropic ยากที่จะ replicate เพราะไม่มี IDE ตัวเอง

Pricing structure เป็น shock ของ industry: **$2 input / $6 output per M tokens**. เทียบกับ:
- Claude Opus 4.8 ที่ ~$15/$75 (ตัวเลข public จาก Anthropic pricing page)
- GPT-5.6 Sol ที่ $5/$30 (frontier ที่ OpenAI เพิ่งประกาศ 9 ก.ค.)
- Gemini 3 Pro ที่ ~$1.25/$10 (leaked)
- SpaceXAI's Grok 4 (รุ่นก่อน) ที่ ~$5/$15

Grok 4.5 pricing = ต่ำกว่า Opus ~7.5x on input, ~12.5x on output; ต่ำกว่า Sol ~2.5x on input, ~5x on output. Musk ประกาศ positioning ตรง ๆ ว่าเป็น **"Opus-class model, but faster, more token-efficient, and lower cost"** — challenge frontier tier ที่ 20% ของราคา

Model นี้ available ที่ 3 surface พร้อมกัน — **Grok Build** (terminal-based AI coding agent ของ SpaceXAI), **Cursor ทุก plan** (รวม free), และ **SpaceXAI console API**. Grok Build เข้ามาตอน Claude Code + Cursor + GitHub Copilot + Windsurf + Codex CLI ครองตลาด — differentiation คือ default model ราคาถูกที่สุดในกลุ่ม frontier-class + Musk network distribution. ประเด็นที่น่าสังเกต: Grok Build ทำได้ทั้ง code, Excel, PowerPoint, Word — SpaceXAI extend claim จาก coding agent ไป knowledge work agent ตรง (Bloomberg รายงานว่า model ถูก "designed for legal and finance tasks" ด้วย)

EU availability ยังไม่มี — คาดว่ามีกลาง ก.ค. ตาม EU AI Act compliance review. US + APAC + EMEA (non-EU) ได้ทันที

## ทำไมสำคัญ
Enabridge track pattern **coding agent commoditization** มาต่อเนื่อง — GitHub Copilot ปล่อย model routing, Cursor เพิ่ม Composer mode, Claude Code auto mode default, Codex CLI GA — สัญญาณ frontier lab แข่งกันที่ inference cost + specialization ไม่ใช่ raw benchmark. Grok 4.5 pricing structure ทำให้ **frontier model ราคา premium (>$10 input, >$50 output) จะรอดยากใน coding use case** เพราะ IDE ที่มี distribution (Cursor, VS Code, JetBrains) ต้อง route ตาม cost-per-outcome ให้ user บ้าง — 5–15x price difference ยังยาก justify

Signal ที่สำคัญคือ **training data moat กลับสำคัญกว่าที่คิด**. SpaceXAI ซื้อ Cursor ไม่ใช่แค่ distribution — คือ real-world developer interaction dataset ที่ scale ~5M dev x หลายล้าน edit ต่อวัน. OpenAI มี ChatGPT + Codex CLI (interaction data), Google มี Gemini in Cloud Code + AI Studio, Anthropic มี Claude Code + Cowork — แต่ non-IDE lab (Meta, Mistral, DeepSeek, Cohere) เพิ่มขาดขอบนี้. Musk เพิ่ง establish ว่า **IDE ownership = defensible training moat**. คาด next 12 เดือน: Anthropic ซื้อ Zed หรือ Continue, OpenAI ผลักดัน Codex CLI + Windsurf integration ให้เป็น first-party IDE, Google เร่ง JetBrains Junie partnership

ที่น่าจับตาระยะกลางคือ **enterprise coding agent procurement**. Q4 2025 – Q2 2026 organizations ซื้อ Copilot Enterprise + Claude Code + Cursor Business ที่ราคา $30–60/seat/month; ถ้า Grok 4.5 (ใน Cursor) รัน equivalent output ที่ 20% ของราคา — CFO เริ่มตั้งคำถาม pricing model. Cursor ต้องเลือก — คงราคาสูงเพื่อ margin หรือลดตาม cost saving; หรือย้ายไป outcome-based pricing (per PR merged, per bug fixed) — pattern เดียวกับ Salesforce Help Agent $2/resolution ที่ยกให้ pricing สัปดาห์ก่อน

## มุม AI Agent Platform
สำหรับ **builders**: ถ้าทำ coding agent (Cline, Aider, Sweep, Devin) — Grok 4.5 default ให้ผู้ใช้ ratio price/performance ที่ 5–15x ดีขึ้น = pressure ให้ผู้ใช้ demand ราคาใกล้เคียง. Route requests ผ่าน multi-model gateway (Portkey, LiteLLM, OpenRouter, Not Diamond) ที่ include Grok 4.5 กลายเป็น table stake. ถ้าทำ non-coding agent (data extraction, workflow automation, customer service) — Grok 4.5's $2/$6 tier เปิด option เข้า margin-sensitive vertical (SMB, education, non-profit) ที่ frontier tier แพงไป

สำหรับ **users/business** ที่ deploy coding agent: (1) update model choice option ใน dev tool config ให้ include Grok 4.5 ก่อนสิ้นเดือน — cost saving 40-80% ที่ workflow ไม่เปลี่ยน; (2) ถ้าอยู่ EU — ต้องรอ compliance review ปลาย ก.ค.; (3) เจรจา Cursor / GitHub Copilot / Windsurf contract ที่กำลังจะ renew ให้มี model routing clause + cost cap ที่ผูก benchmark กับ Grok 4.5 tier pricing. Thai dev team ที่ใช้ Cursor free tier อยู่แล้ว: Grok 4.5 default ใน free plan ทำให้ productivity gap vs paid plan แคบลง — reassess ROI ของ paid seat ก่อน renewal

สำหรับ **ecosystem**: Anthropic เจอ pressure โดยตรงที่ Opus positioning — คาด Q3 นี้จะออก **Opus tier ที่ราคาต่ำลง** หรือ **Sonnet tier ที่ powerful ขึ้น** (Sonnet 5 เพิ่งออก 30 มิ.ย. — ตัวเลข Sonnet 5.1 ต่อไป). OpenAI Sol tier ก็ต้อง defend — Terra tier ($2.50/$15) ถูก pitch เป็น "half cost of Sol" แต่ยังแพงกว่า Grok 4.5. Google Gemini 3.5 Pro (คาด GA 17 ก.ค. ตาม leak) มี pricing ~$1.25/$10 อาจจะเป็น response ที่ตรงที่สุด. **IDE / dev tool market entry** โดน SpaceXAI redefine — dev tool ที่ไม่ผูก foundation model จะยาก scale เพราะ margin ถูกกดจากทั้งสองด้าน (foundation model แข่งราคา, user demand agent quality สูงขึ้น)

## Sources
- [SpaceXAI, Cursor Launch Grok 4.5 AI Model for Finance, Legal Applications — Bloomberg](https://www.bloomberg.com/news/articles/2026-07-08/spacexai-cursor-unveil-grok-ai-model-for-legal-finance-tasks)
- [SpaceXAI launches Grok 4.5, its first built with Cursor's help — Engadget](https://www.engadget.com/2211260/spacex-ai-grok-4-5-cursor/)
- [SpaceXAI Releases Grok 4.5, a Cursor-Trained Model for Coding, Agentic Tasks, and Knowledge Work at $2/M Input — MarkTechPost](https://www.marktechpost.com/2026/07/08/spacexai-releases-grok-4-5/)
- [SpaceXAI's Grok 4.5 Undercuts Anthropic and OpenAI on Coding Agent Pricing — DevOps.com](https://devops.com/spacexais-grok-4-5-undercuts-anthropic-and-openai-on-coding-agent-pricing/)
- [Introducing Grok 4.5 — SpaceXAI](https://x.ai/news/grok-4-5)

---

## Audio script
วันที่ 8 กรกฎาคม SpaceXAI บริษัท AI ของ Elon Musk ที่เพิ่ง IPO ต้นปีและ acquire Cursor เมื่อเมษายน ปล่อย Grok 4.5 เป็น flagship coding และ agentic model. Bloomberg ตี exclusive ก่อน 24 ชั่วโมงว่านี่คือ Grok ตัวแรกที่สร้างขึ้นด้วยความช่วยเหลือของ Cursor — เป็นครั้งแรกที่ IDE maker และ foundation model lab ผลิต model ร่วมกันตั้งแต่ training phase. Cursor's interaction data จาก 5 ล้าน active developer feeding real world signal ว่า engineer เขียน review debug code ยังไง — training set ที่ OpenAI Anthropic ยาก replicate. pricing shock ของ industry คือ 2 ดอลลาร์ input 6 ดอลลาร์ output ต่อล้าน token — ต่ำกว่า Claude Opus 7 ถึง 15 เท่า ต่ำกว่า GPT 5.6 Sol 2 ครึ่งถึง 5 เท่า. Musk ประกาศตรงๆ ว่าเป็น Opus class model แต่เร็วกว่า token efficient กว่า ต้นทุนต่ำกว่า. model available ที่ Grok Build terminal coding agent, Cursor ทุก plan รวม free, และ SpaceXAI console API — ทำได้ทั้ง code Excel PowerPoint Word extend claim จาก coding agent ไป knowledge work agent ด้วย. signal ที่สำคัญคือ IDE ownership = defensible training moat SpaceXAI ซื้อ Cursor ไม่ใช่แค่ distribution แต่คือ dataset ที่ scale ไม่ได้ผ่าน API — คาด Anthropic ซื้อ Zed หรือ Continue OpenAI ผลักดัน Codex CLI Windsurf integration Google เร่ง JetBrains Junie partnership ในหกเดือน. สำหรับ Thai dev team ที่ใช้ Cursor free tier อยู่แล้ว Grok 4.5 default ทำให้ productivity gap เทียบ paid plan แคบลง reassess ROI ของ paid seat ก่อน renewal
