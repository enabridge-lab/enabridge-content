---
date: 2026-10-13
slug: nous-research-hermes-enterprise-15b
topic: agentic-ai
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial illustration: a wild forking Git tree labeled "HERMES"
  branches endlessly into enterprise office silhouettes, each branch
  tagged with a company badge. In the center a receipt reads
  "24M CLONES", "2.5% OF GLOBAL AI TOKENS", "$36M ARR", "$1.5B VALUATION",
  "$90M SERIES B" — numbers large, high-contrast, legible at 200px.
  Open-source teal + Robot Ventures neon green on deep slate background,
  flat isometric style, 1:1 aspect, no real human faces. Visual metaphor:
  open-source agent that leaked out of GitHub and bought itself a suit.
image: images/26-10-14-0615-04-nous-research-hermes-enterprise-15b.png
---

# Nous Research ปิด $90M Series B ที่ $1.5B — open-source Hermes agent กำลังเดินทาง enterprise ด้วย ARR $36M + 2.5% ของ global AI token

## TL;DR
- 7 ต.ค. **Nous Research** ปิด **$90M Series B** ที่ reported valuation **$1.5B** (จาก Wall Street Journal); รวม total funding **~$158M**
- Lead ไม่ชัดเจน — บาง source อ้าง **Robot Ventures** (Axios), บางเจ้าบอก "ยังไม่ name lead"
- Traction ที่อ้าง: Hermes agent open-source **ถูก clone 24M+ ครั้ง**, คิดเป็น **~2.5% ของ global AI token usage** ตามการประเมินของบริษัท; **ARR ~$36M** ตาม WSJ
- เงิน round นี้จะไปที่ **"Hermes for Businesses"** — enterprise version ที่ยอมให้บริษัท (1) เลือก model ตาม price, (2) own institutional knowledge, (3) run on-prem. Launch date + pricing ยังไม่เปิด
- Signal ที่ชัด: **open-source agent + ARR เกือบ $40M = ไม่ใช่ experiment อีกต่อไป**. OpenAI + Anthropic ต้องตอบคำถาม "ทำไมองค์กรต้องจ่าย closed-source model เมื่อ open stack ขนาด Hermes ขึ้น enterprise ได้แล้ว?"

## เกิดอะไรขึ้น

7 ต.ค. Nous Research ยืนยัน Series B $90M ที่ Wall Street Journal รายงาน valuation $1.5B — การ step up ครั้งใหญ่จาก $400M valuation ของ Series A ปี 2024. Blog post ของบริษัทไม่เปิด valuation + lead investor; TechFundingNews + Runtimewire อ้าง Robot Ventures ลง lead (sourcing จาก Axios), ขณะที่ CellCog บอกว่า "ยังไม่ name lead." Nous ยืนยันเฉพาะว่าเงินจะไปที่ **"Hermes for Businesses"** — commercial version ที่พัฒนาจาก Hermes open-source agent ที่บริษัทปล่อยในปี 2023

ตัวเลข traction ที่น่าทึ่งที่สุด: **Hermes agent ถูก clone 24M+ ครั้งทาง Hugging Face + GitHub**, คิดเป็น **~2.5% ของ global AI token usage** ตามการประเมินของ Nous เอง (uncorroborated). WSJ รายงาน annualized revenue ~$36M — ถ้าตัวเลขจริง, Nous กลายเป็น open-source AI company ที่โตเร็วที่สุด rivaling Mistral ที่ early stage. 2.5% ของ global token usage = 1 ใน 3 ของ Anthropic's share (ตามประเมิน Artificial Analysis Q3 2026) โดยที่ไม่มี pretrained foundation model เป็นของตัวเอง — Nous ปรับแต่ง LLaMA + Qwen + DeepSeek + Mistral เป็น Hermes variant แล้ว open-source

Hermes for Businesses จะมี 3 commitment: (1) **model-agnostic** — ลูกค้าเลือก backbone ตาม price/latency; (2) **data ownership** — institutional knowledge ที่ fine-tune บน data ของบริษัทจะ remain property ของบริษัท, Nous ไม่ claim; (3) **on-prem deployment** — รัน air-gapped ได้. Pricing + launch date ยังไม่เปิด. Runtimewire รายงานเพิ่มว่าส่วนหนึ่งของเงินจะไปที่ **mobile app ของ Hermes** — target consumer market ด้วย (ซึ่งขัดกับ positioning enterprise)

Context ที่สำคัญ: ปีนี้ Mistral AI ก็ announce enterprise AI stack (Mistral Business); DeepSeek ก็ตามมาด้วย enterprise license; Meta ยัง double-down บน Llama 4 Argon สำหรับ enterprise. **ตลาด open-source enterprise AI กำลัง consolidate แล้วเริ่มมี pricing power**. Nous ชนะใน niche ของ "agent-first open-source" — ไม่ใช่ foundation model, ไม่ใช่ RAG — แต่คือ **agent orchestration stack ที่ run open backbone**

## ทำไมสำคัญ

**ครั้งแรกที่ open-source agent มี ARR เกินแปด digit แล้ว valuation ขึ้น Billion+**. Hugging Face Transformer library มี contributor + download มากกว่า แต่ ARR ของ enterprise business เล็กกว่า. Mistral แม้ valuation สูงกว่าแต่คู่แข่งเป็น foundation model vendor (ไม่ใช่ agent). Nous คือ **first proof** ว่า open-source agent business = **viable ที่ scale enterprise** ไม่ใช่ research toy

Point of view: การที่ open-source agent มี ARR $36M ตีกรอบ **แบบจำกัดใหม่** ของ pricing power ของ closed-source model vendor. OpenAI Enterprise ที่คิด $60/user/mo + metered API ต้องตอบคำถามของ CFO: "ถ้า Hermes open-source ทำ 70% ของ workflow ของเราได้ แล้วเราจ่าย compute เองที่ $0.001/token เทียบกับ GPT-5 ที่ $0.015/token = $5M/year savings — ทำไมเรายังจ่าย ChatGPT Enterprise?" คำตอบของ Sam Altman ปัจจุบันคือ "quality + safety + enterprise support" — ซึ่งใน 24 เดือนข้างหน้า Nous + Mistral + DeepSeek จะ eroded กันหมด

Pattern ที่เห็นชัด: **AI investment กำลัง bifurcate**. ค่ายหนึ่งลงเงิน foundation model + flagship closed-source (Anthropic, OpenAI, Google, xAI); อีกค่ายลงเงิน **open-source agent stack ที่ run on ใครก็ได้** (Nous, Together AI, Lightning AI). ทั้งสองค่าย win แต่ margin ต่างกัน — closed vendor win on margin + brand, open vendor win on volume + developer trust. ตลาดจะมี 2-3 brand ต่อ segment ภายใน 24 เดือน

Caveat: ตัวเลข 2.5% ของ global AI token usage **เป็นประเมินของ Nous เอง** ไม่มี third-party verify. ถ้าตัวเลขจริง = Nous ใหญ่กว่า Groq + Together AI รวมกันบน inference. ถ้าไม่จริง = ปรกติของ open-source company ที่ overstate reach — ควร skeptical จนกว่า OpenRouter / Artificial Analysis จะยืนยัน

## มุม AI Agent Platform

**Builders:** ถ้าคุณสร้าง **agent framework ที่ assume closed-source backbone** (ตัวอย่าง: LangChain default OpenAI, CrewAI default Anthropic) — ลูกค้า enterprise จะเริ่มถาม "support Hermes ได้ไหม" ภายใน 6 เดือน. Framework ที่ **model-agnostic ที่ day-1** (LlamaIndex, Vercel AI SDK, Semantic Kernel) ได้ advantage. Rebuild framework ให้ support **swap backbone แบบ 1-click** จะเป็น table stakes

**Users / business:** CTO/CFO ที่ sign ChatGPT Enterprise + Claude for Enterprise ภายใน 6 เดือน — ขอ POC Hermes for Businesses คู่กัน. ตัวชี้ขาด: **(1) workflow coverage** (Hermes ทำ workflow ของเราได้กี่ %?), **(2) total cost of ownership** (compute + ops เทียบกับ API bill ของ closed vendor), **(3) data residency** (on-prem = ชนะ compliance game ใน finance/healthcare/government). ถ้า Hermes ทำได้ 70%+ ของ workflow = เริ่ม negotiate lower pricing กับ incumbent

**Ecosystem:** OpenAI + Anthropic ไม่ตายทันที — enterprise support, SLA, model quality + safety ยังเป็น moat. แต่ pricing power ของ closed-source vendor กำลัง compress อย่างชัด. Mistral + Nous + Together AI + Groq + Lightning AI กำลังเดินทาง consolidation — ภายใน 18 เดือนจะเหลือ 3 brand ใหญ่ของ "open-source enterprise AI stack". Nous เป็น **leading candidate** เพราะ ARR traction + brand ที่ developer love — แต่ต้อง execute enterprise sales ที่ culture startup ยัง sketchy

## Sources
- [Nous Research confirms it hit $1.5B valuation, launches AI agents for business users (TechCrunch)](https://techcrunch.com/2026/10/07/nous-research-confirms-it-hit-1-5b-valuation-launches-ai-agents-for-business-users/)
- [Nous Research raises $90M at a reported $1.5B valuation (TechFundingNews)](https://techfundingnews.com/nous-research-raises-90m-at-a-reported-1-5b-valuation-to-take-its-open-source-agent-to-business/)
- [Nous Research raises $90M to take its open-source Hermes agent into business (Runtimewire)](https://runtimewire.com/article/nous-research-90m-series-b-hermes-agent)
- [Nous Research Hits $1.5B Valuation, Launches Hermes Agent (Emergent)](https://emergent.sh/news/nous-research-hits-15b-valuation-launches)
- [Nous Research Raises $90M at $1.5B for AI Agents (Tech Insider)](https://tech-insider.org/nous-research-90-million-series-b-ai-agents-2026/)
- [Nous Research Raises $90M for Hermes Agent at $1.5B (CellCog)](https://cellcog.ai/blog/nous-research-90m-hermes-agent/)

---

## Audio script
วันที่ 7 ตุลาคม Nous Research ปิด Series B 90 ล้านเหรียญที่ valuation ที่ Wall Street Journal รายงาน 1.5 พันล้านเหรียญ รวม total funding 158 ล้านเหรียญ Lead investor ยังไม่ชัด บาง source อ้าง Robot Ventures บางเจ้าบอกยังไม่ name เงินรอบนี้จะไปที่ Hermes for Businesses enterprise version ของ open source agent ที่ Nous ปล่อย open ปี 2023 ตัวเลข traction ที่น่าทึ่งที่สุดคือ Hermes agent ถูก clone 24 ล้านครั้ง คิดเป็นประมาณ 2.5 เปอร์เซ็นต์ของ global AI token usage ตามการประเมินของบริษัทเอง และ WSJ รายงาน annualized revenue 36 ล้านเหรียญ ซึ่งถ้าตัวเลขจริง Nous กลายเป็น open source agent company ที่โตเร็วที่สุด Hermes for Businesses จะ model agnostic ลูกค้าเลือก backbone เอง data ownership stay with customer run on prem ได้ pricing กับ launch date ยังไม่เปิด pattern ที่สำคัญคือครั้งแรกที่ open source agent มี ARR เกินแปด digit แล้ว valuation ขึ้น billion plus Hugging Face มี developer มากกว่าแต่ enterprise ARR เล็กกว่า Mistral valuation สูงกว่าแต่คู่แข่งคือ foundation model vendor Nous คือ first proof ว่า open source agent business viable ที่ scale enterprise สำหรับ CTO ไทยที่ sign ChatGPT Enterprise กับ Claude Enterprise ภายใน 6 เดือน ขอ POC Hermes for Businesses คู่กัน check workflow coverage total cost of ownership กับ data residency ถ้าทำได้ 70 เปอร์เซ็นต์ขึ้นไปของ workflow เริ่ม negotiate lower pricing กับ incumbent ได้ สำหรับ builder ของ agent framework ที่ assume closed source backbone รีบ rebuild ให้ model agnostic ด้วย 1 click swap backbone ภายใน 6 เดือน หรือเสีย enterprise customer ที่กำลังหา hedge
