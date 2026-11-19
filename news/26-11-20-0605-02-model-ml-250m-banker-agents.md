---
date: 2026-11-18
slug: model-ml-250m-banker-agents
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a sleek London banking floor at
  dusk with rows of trading desks; above each desk floats a glowing holographic
  briefcase labeled "AI BANKER". A giant chart on the far wall rises steeply,
  labeled "12x ARR" with year markers, and a huge price tag hangs beside it
  reading "$1.5B VALUATION". A smaller banner says "$250M SERIES B". Clean
  editorial style, deep blue and warm gold palette, 1:1 aspect, no real
  human faces (silhouettes OK), high contrast so numbers stay readable
  at 200px.
image: images/26-11-20-0605-02-model-ml-250m-banker-agents.png
---

# Model ML ปิด $250M ที่ $1.5B — "ทุก banker มี agent" คือ pitch ที่ตลาดเชื่อแล้ว

## TL;DR
- Model ML ที่ London ปิด Series B $250M ที่ valuation $1.5B — General Atlantic + QED Investors co-lead, YC + FT Partners ร่วม
- CEO อ้าง ARR โต 12x ในหนึ่งปี และบอกว่า agent ของตัวเอง "ช่วย bank หาเงิน" ไม่ใช่แค่ประหยัดเวลา
- สองปีผ่านมามี Rogo ($160M ที่ $2B) และ OpenAI/Anthropic ขาย enterprise license ให้ financial services — vertical banking agent กลายเป็นตลาดที่ VC วางเงินได้แล้ว

## เกิดอะไรขึ้น
Model ML บริษัท 2 ปีจาก London ประกาศ Series B $250M ที่ valuation $1.5B รวม funding ถึงปัจจุบัน $350M ที่น่าสังเกตคือ Series A รอบ $75M ที่ FT Partners lead เพิ่งปิดเมื่อพฤศจิกายน 2025 — ระหว่างสองรอบห่างกัน 12 เดือน valuation ขึ้น 5-6 เท่า General Atlantic และ QED Investors co-lead รอบนี้ โดยมี Evolution Equity, Airtree, Forestay, Y Combinator, FT Partners, Latitude, Inception Fund และ 13Books Capital ตามเข้ามา

ตัวเลขที่ CEO Chaz Englander พูดกับ The Next Web คือ ARR โต 12 เท่าในหนึ่งปี และ positioning ที่ชัดกว่านั้น — Englander บอกว่าช่วงที่ผ่านมา agent ใน financial services ถูก pitch ว่า "ประหยัดเวลา analyst" แต่ Model ML ขายต่างจากนั้น agent ของ Model ML จับงาน client-facing ที่ generate revenue โดยตรง เช่นช่วย relationship manager เตรียม deck สำหรับ client pitch, ร่าง term sheet, วิเคราะห์ portfolio exposure — งานที่ bank จ่ายเงินให้คนทำอยู่แล้วและเกี่ยวกับ revenue line ไม่ใช่ cost center

Model ML ไม่ใช่ตัวเดียวในเลน — Rogo ที่ New York ปิด $160M ที่ $2B valuation เมื่อเมษายน และ Scommerce รายงานว่ามีลูกค้า investment bank กลุ่ม top-tier หลายราย ใน UK ตลาดนี้มี Griffin ที่เพิ่ง announce Series B เพื่อเพิ่ม card และ stablecoin payment บน agentic banking platform ของตัวเอง แปลว่าทั้ง "agent ช่วย banker" และ "banking-as-agent-infrastructure" ได้ VC money ก้อนใหญ่ในเดือนเดียวกัน

## ทำไมสำคัญ
ตัวเลข 12x ARR ของ vertical SaaS ใน financial services ไม่ใช่เรื่องปกติ — benchmark industry สำหรับ vertical SaaS ที่ขาย enterprise license อยู่ที่ 2-3x YoY ในปีที่โตเต็มที่ การที่ Model ML อ้าง 12x แล้ว General Atlantic + QED (ซึ่งเป็น fintech-focused VC ที่รู้จักตลาดดีที่สุด) ยอมจ่าย premium ที่ $1.5B แปลว่าพวกเขาเห็นอะไรบางอย่างใน sales motion ที่ scale ได้ ไม่ใช่ pilot revenue จาก relationship

Caveat ใหญ่สุดคือ 12x ARR จาก base เท่าไหร่ ถ้า base เริ่มที่ $2M ARR แล้วไปที่ $24M ก็ยัง meaningful แต่ไม่ใช่ story ที่ justify $1.5B valuation — multiple 60x revenue ต้องการ ARR อย่างน้อย $25M เพื่อจะไม่ absurd Model ML ไม่เปิดเผยตัวเลขสุทธิ ซึ่งเป็นสัญญาณปกติของ private round แต่ถ้า Rogo ที่โตช้ากว่าได้ valuation สูงกว่า Model ML อาจมี gap ที่ VC เห็นว่า grow into ได้

Pattern ใหญ่กว่านั้น — ปีนี้เป็นปีที่ "vertical agent" กลายเป็น thesis หลักของ late-stage VC แทนที่จะเป็น horizontal agent framework ที่ขายให้ทุกคน Pitch ของ vertical agent คือ "เราเข้าใจ workflow ของอุตสาหกรรม X ลึกพอที่ foundation model generalist (Claude, GPT) ทำตามไม่ได้" ซึ่ง defensibility ไม่ได้มาจาก model แต่มาจาก data integration, compliance framework, และ sales relationship กับลูกค้า category ที่จ่ายแพง — bank, law firm, consulting firm, healthcare

## มุม AI Agent Platform
Builders — ถ้าคุณกำลังสร้าง horizontal agent framework ให้ reconsider positioning rounds ปีนี้ของ Harvey (legal), Rogo + Model ML (finance), Hippocratic AI (healthcare) บอกชัดว่า capital flow ไปที่ vertical ที่ลูกค้าจ่ายได้ $50K-$500K ต่อปีต่อ seat Horizontal play ที่ยังเวิร์คคือ infrastructure layer (orchestration, observability, governance) ไม่ใช่ end-user agent ทั่วไป

Users/business — bank และ financial services firm ไทยควรเริ่ม evaluate vertical agent vendor อย่างจริงจัง — ไม่ใช่สร้างเองด้วย Claude หรือ GPT พร้อม RAG ลัวนสังเกตว่า Rogo กับ Model ML ทั้งคู่โฟกัสงาน client-facing ที่ generate revenue ไม่ใช่ internal automation ซึ่งเป็น framing ที่ approval ง่ายกว่าเพราะไม่ต้องสู้กับ cost-center benchmarking

Ecosystem — CFO ของ bank ใหญ่จะเริ่มถาม vendor ทุกคนว่า "คุณขายเป็น seat หรือ action" Model ML + Salesforce Agentforce + Microsoft Copilot ทั้งหมดกำลัง converge ไปที่ per-seat pricing ($30-$100 range) ซึ่งทำให้ budget ง่ายและขาย rollout ได้เร็ว vendor ที่ยังยืนที่ consumption-only pricing จะเจอ friction ที่ CFO เพิ่มขึ้นในรอบ renewal

## Sources
- [Model ML raises $250m at a $1.5bn valuation for bankers' AI agents (TNW)](https://thenextweb.com/news/model-ml-250m-series-b-1-5bn-valuation-ai-agents-bankers)
- [Model ML bags $250m to give every banker an AI agent (FinTech Global)](https://fintech.global/2026/11/18/model-ml-bags-250m-to-give-every-banker-an-ai-agent/)
- [Model ML raises USD 250 mln Series B for finance AI agents (The Paypers)](https://thepaypers.com/fintech/news/model-ml-raises-usd-250-mln-series-b-for-ai-agents-in-finance)
- [Model ML Raises $250M at $1.5B Valuation for Personal AI Agents in Finance (WOWTALE)](https://en.wowtale.net/2026/11/18/236073/)

---

## Audio script
Model ML บริษัท agent สำหรับ banker ที่ London เพิ่งปิด Series B สองร้อยห้าสิบล้านเหรียญ valuation ที่หนึ่งพันห้าร้อยล้านเหรียญ General Atlantic กับ QED Investors ซึ่งเป็น VC fintech ตัวจริง co-lead รอบนี้ ตัวเลขที่น่าสังเกตคือ ARR โต 12 เท่าในหนึ่งปี และ Series A รอบก่อนหน้าเพิ่งปิดเมื่อหนึ่งปีก่อนที่ valuation ต่ำกว่าถึง 5-6 เท่า

ที่ positioning ของ Model ML ต่างจากคู่แข่งคือ CEO พูดชัดว่า agent ของเขาช่วย bank "หาเงิน" ไม่ใช่ประหยัดเวลา analyst — งานที่ agent ทำคือเตรียม pitch deck, ร่าง term sheet, วิเคราะห์ portfolio exposure ให้ relationship manager ซึ่งเป็น revenue-generating ไม่ใช่ cost center

เทรนด์ใหญ่ที่เห็นในรอบนี้คือ VC capital ย้ายจาก horizontal agent framework ไปที่ vertical agent สำหรับอุตสาหกรรมที่ลูกค้าจ่ายได้แพง bank, law firm, consulting ก่อนหน้านี้มี Rogo ปิดร้อยหกสิบล้าน Harvey ปิดใหญ่สำหรับ legal ปีนี้ชัดว่า defensibility ของ agent business ไม่ได้มาจาก model แต่มาจาก industry depth และ data integration สำหรับ bank ไทยนี่คือ signal ว่าเริ่ม evaluate vendor ภายนอกได้แล้วครับ
