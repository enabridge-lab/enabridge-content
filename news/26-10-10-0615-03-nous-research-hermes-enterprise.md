---
date: 2026-10-07
slug: 26-10-10-0615-03-nous-research-hermes-enterprise
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial hero: an open-source "Hermes" statue made of translucent glass
  blocks, each block labeled with a model name. Beside it, a sealed vault
  door marked "HERMES FOR BUSINESS" cracked open to reveal a glowing data
  core. Floating numbers hover around: "22.7M DOWNLOADS", "2.5% GLOBAL AI
  TOKENS", "$100M ARR BY EOY". A ribbon at the base reads "$90M AT $1.5B".
  Editorial isometric style, deep indigo + copper + warm white, 1:1
  aspect, no real human faces.
image: images/26-10-10-0615-03-nous-research-hermes-enterprise.png
---

# Nous Research ปิด $90M ที่ valuation $1.5B — เปิด "Hermes for Businesses" พร้อมเก็บ 2.5% ของ token โลก

## TL;DR
- 7 ต.ค. 2026 **Nous Research** ปิด Series B **$90M ที่ valuation $1.5B** — WSJ รายงาน; **Robot Ventures** นำ, บวก **Nvidia / Microsoft M12 / Samsung / Union Square Ventures / Y Combinator / Menlo Ventures** → funding รวม ~$158M
- Open-source **Hermes** download >22.7M ครั้ง + ประมวล **~2.5% ของ global AI token** ตามประมาณการ startup — เป็น benchmark adoption ที่หายากของ open model
- Launch คู่กันคือ **Hermes for Businesses** — enterprise version ที่ให้บริษัทเลือก model ตาม price/goal, เก็บ data เป็นของตัวเอง, ครอบ multi-step workflow; ARR ~$36M (mid Sep) → คาด >$100M สิ้นปี 2026

## เกิดอะไรขึ้น

วันพุธ Wall Street Journal รายงานว่า **Nous Research** ปิด Series B $90M ที่ valuation $1.5B. **Robot Ventures** นำ round, บวก backer ชั้นแนวหน้า — Nvidia (strategic / GPU access), Microsoft's M12, Samsung, Union Square Ventures, Y Combinator, Menlo Ventures. บริษัทไม่ยืนยัน valuation อย่างเป็นทางการ แต่หลายสำนักยืนยันตัวเลข; funding รวมหลัง round นี้แตะ ~$158M (round แรก $50M นำโดย Paradigm เม.ย. 2025)

Nous เริ่มจากเป็น decentralized AI research collective ที่ปล่อย **Hermes** — open-source LLM / agent runtime ที่ community นำไป fine-tune เอง. Download >22.7M ครั้ง — เลขที่หายากสำหรับ open model นอกค่าย Meta/Mistral — และ Nous ประมาณว่า Hermes ประมวล **~2.5% ของ global AI token** ทั้งหมด ตามการวัด routing / download / API traffic ของตัวเอง

Launch คู่กันกับ round คือ **Hermes for Businesses** — enterprise version ที่แก้ปัญหาสองอย่างที่ enterprise ยอมจ่าย: (1) **model portfolio** — บริษัทเลือก model ตาม price × goal ได้; ไม่ต้องเลือกฝ่ายใดฝ่ายหนึ่ง (Gemini vs Claude vs Llama vs ตัวเอง). (2) **data sovereignty** — บริษัท deploy ใน own cloud / own GPU; **ไม่มี public endpoint** ไหนที่ data รั่วออก; **own the institutional knowledge** ที่สะสม

ตัวเลข business ที่น่าสังเกต — Nous บอก ARR ประมาณ **$36M ณ mid-September 2026** และคาด **ทะลุ $100M ก่อนสิ้นปี 2026**. ถ้าจริง = growth rate ที่น้อยคนเทียบได้ในตลาด infrastructure AI; เป็น "mid-cycle open-source → enterprise commercialization" ที่เกิดช้ากว่า Databricks แต่สะท้อน rhythm เดียวกัน

**ข้อควรระวัง:** valuation ยัง not officially confirmed ตามหลาย source; download number เป็นประมาณการของ startup เอง (clone/download ไม่เท่ากับ MAU); token share ก็เป็น self-reported — รอ third-party verification

## ทำไมสำคัญ

**Pattern ชัดเจน** ของ Q4 2026 — enterprise ไม่ซื้อ model ล้วน ๆ อีกต่อไป, ซื้อ **"model marketplace + runtime + governance"**. Hermes for Businesses position เป็น "open alternative" ต่อ Azure AI Foundry (closed proprietary routing) + Databricks (SQL-centric) + Bedrock (AWS-locked). ประเด็นหลักที่ enterprise ยอมเซ็นคือ **data stays home** — board ของธนาคาร / healthcare / defense / government ลงนามง่ายกว่าตอน vendor สัญญาว่า "ไม่มี public endpoint ไหนที่ข้อมูลรั่ว"

Signal สำคัญคือ **Microsoft M12 ลงเงิน**. Microsoft มี Azure OpenAI, Copilot, Agent 365, และ Fabric Data Agents ของตัวเองแล้ว — การลงใน Nous Research = Microsoft hedge ว่า **"open-source model + bring-your-own-compute" จะเป็นตลาดจริง**. Nvidia ลงด้วย — ชัดเจนว่าใครขาย GPU ก็อยากให้ enterprise รัน open model บน DGX ของตัวเอง ไม่ใช่ API ของ OpenAI/Anthropic

ประเด็นที่ builder ต้องระวังคือ **"token share metric"** ที่ Nous ชู 2.5% ของ global AI tokens. ถ้าตัวเลขจริง (รอ Semianalysis / Artificial Analysis verify) หมายความว่า open-model ecosystem ไม่ใช่ "long tail" อีกต่อไปแล้ว — มันคือ 1/40 ของ total compute อยู่ใน open stack. Head of AI ของ Fortune 500 ที่ยัง stuck อยู่ "OpenAI หรือ Anthropic เท่านั้น" กำลังมองข้าม pool ที่ scale ใกล้ competitive แล้ว

## มุม AI Agent Platform

**Builders:** คนทำ agent framework ที่อยากขาย enterprise ต้อง **open-model-first** ตั้งแต่ day 1 — rough support Hermes, Llama, Qwen, DeepSeek, Mistral ไว้ใน SDK พร้อมกับ Claude/GPT. "I only support Anthropic" กลาย red flag ใน procurement checklist ของธนาคารไทยที่กลัว data residency มานาน. **Users / business:** CTO ที่พิจารณา "สร้าง agent บน Azure OpenAI vs. bring-your-own-model Hermes" ตอนนี้มี option ที่ 3 ชัดเจน — ซื้อ Hermes for Businesses ที่ Nous ดูแลให้ ไม่ต้อง fine-tune / host เอง. ประหยัดเวลา 6-12 เดือนของ ML engineering budget

**Ecosystem:** ตลาด **"agent runtime for your own data"** กำลัง 2 ขั้วชัด — ขั้ว hyperscaler (Microsoft Fabric, Google Vertex, AWS Bedrock) และขั้ว sovereign stack (Nous, Databricks, Cohere, Together AI, Fireworks, และ national model ของประเทศต่าง ๆ). ไทย — ThaiLLM, Pathumma, และ sovereign AI stack ที่พูดกันตั้งแต่ ม.ค. — ควรจับ playbook ของ Nous เป็นต้นแบบ: open model + enterprise commercial tier + data sovereignty positioning. ไม่ต้องชน OpenAI ตรง benchmark — ชนที่ board conversation ของ regulated industry

## Sources
- [Nous Research raises $90M at $1.5B valuation for open-source AI - Dealroom](https://dealroom.co/news/160592-nous-research-raises-90m-at-1-5b-valuation-for-open-source-ai/)
- [Nous Research confirms it hit $1.5B valuation, launches AI agents for business users - TechCrunch (via WinZheng)](https://www.winzheng.com/en/article/nous-research-1-5b-ai-agents)
- [AI developer Nous Research raises $90 million at $1.5 billion valuation: WSJ - Cryptorank](https://cryptorank.io/insights/deals/nous-research-series-b-2026-10-07)
- [Nous Research Raises $90 Million to Build Enterprise Hermes - St-hakky](https://book.st-hakky.com/en/news/nous-research-raises-90m-for-hermes-ai-agents)

---

## Audio script
Wall Street Journal รายงานวันพุธว่า Nous Research ปิด Series B 90 ล้านดอลลาร์ ที่ valuation 1.5 พันล้าน. Robot Ventures นำ บวก Nvidia Microsoft M12 Samsung Union Square Ventures Y Combinator Menlo Ventures. funding รวมแตะ 158 ล้าน. ตัวเลขที่น่าทึ่งคือ Hermes open-source download 22.7 ล้านครั้ง และประมาณ 2.5% ของ global AI token โลกรันผ่านมัน. Launch คู่กันคือ Hermes for Businesses enterprise version ที่แก้สองปัญหา. หนึ่ง เลือก model ตาม price และ goal ไม่ต้องล็อก Anthropic หรือ OpenAI. สอง data stays home ไม่มี public endpoint ที่ข้อมูลรั่ว deploy ใน own cloud ของบริษัท. ตัวเลข ARR 36 ล้านช่วงกลางกันยา คาดทะลุ 100 ล้านก่อนสิ้นปี. ที่น่าสังเกตคือ Microsoft M12 ลงเงิน. Microsoft มี Azure OpenAI Copilot Agent 365 อยู่แล้ว การลงใน Nous สะท้อนว่า Microsoft เอง hedge ว่า open-model bring-your-own-compute จะเป็นตลาดจริง. Nvidia ลงด้วย ชัดว่าใครขาย GPU ก็อยากให้ enterprise รัน open model บน DGX ของตัวเอง. Signal สำคัญ. ปี 2026 enterprise ไม่ซื้อ model ล้วน ซื้อ model marketplace บวก runtime บวก governance. CTO ไทยที่กลัว data residency มีทางเลือกชัดขึ้น. ThaiLLM Pathumma ควรจับ playbook ของ Nous เป็นต้นแบบ. open model บวก enterprise commercial tier บวก data sovereignty positioning. ไม่ต้องชน OpenAI ตรง benchmark ชนที่ board conversation ของธนาคารและ healthcare
