---
date: 2026-07-13
slug: together-ai-800m-series-c-open-inference-thesis
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial hero illustration of a giant stack of open-source model shards
  glowing on a data-center floor, forming a rising staircase labeled
  "OPEN INFERENCE 3X". A silhouette of an exec on the top step holds a
  banner reading "$800M SERIES C" while behind them a wall shows three
  bold price tags: "$8.3B VALUATION", "$1B+ ARR", and "50X CAPACITY BY
  2031". A ribbon in the corner reads "LED BY ARAMCO VENTURES". Cinematic
  neon-blue and gold palette, high contrast, bold typography readable at
  200px thumbnail, 1:1 aspect, no real human faces.
image: images/26-07-13-0608-02-together-ai-800m-series-c-open-inference-thesis.png
---

# Together AI ปิด Series C $800M ที่ valuation $8.3B — open-source inference โต 3x, Aramco นำ, "picks and shovels" ยังชนะ

## TL;DR
- 1 กรกฎาคม 2026 **Together AI** ปิด Series C **800 ล้านดอลลาร์** ที่ post-money valuation **8.3 พันล้านดอลลาร์** — เพิ่มขึ้น **>2x** จากรอบก่อน. Lead โดย **Aramco Ventures** กับ NVIDIA, Vista Equity, General Catalyst, Emergence, March Capital, Pegatron, SentinelOne S Ventures ร่วม
- Together โชว์ตัวเลข **>$1B annual bookings** (Q2 2026) และ **open-source model usage บน platform โต 3x YoY** — ยืนยัน thesis ว่า enterprise เลือก open weights + neocloud inference มากขึ้นเรื่อย ๆ
- แผนเงินคือ **scale capacity 50x ใน 5 ปี** — สัญญาณว่า Together มอง demand growth เป็น step-function ไม่ใช่ linear และเดิมพัน infra layer แทน model layer

## เกิดอะไรขึ้น
Together AI เป็นบริษัท neocloud ที่ specialise ใน open-source model inference — Llama, Mistral, DeepSeek, Qwen, และรุ่นล่าสุดของ open weights ใน 2026 — ให้ enterprise เรียกใช้ผ่าน API ที่ราคาต่ำกว่า proprietary API 60-90% และ fine-tune ได้บน dedicated GPU. หลังจากปี 2025 ที่ closed model เริ่มเห็น price competition ชัด ๆ Together เข้าปี 2026 ด้วย **ARR ทะลุ 1 พันล้านใน Q2** และ **usage ของ open-source model บน platform โต 3 เท่าใน 12 เดือน** — จาก demand ที่ enterprise ไม่อยาก lock-in กับ OpenAI/Anthropic แล้วเจอ pricing surprise ทีหลัง

Series C ครั้งนี้จึงไม่ใช่ growth round ธรรมดา — **Aramco Ventures นำ** พร้อม NVIDIA (ยังเชียร์ neocloud อยู่แม้ตัวเองมี DGX Cloud), Vista Equity, General Catalyst, Emergence, March Capital, Pegatron, และ SentinelOne S Ventures. รายชื่อนี้บอกอะไรสองอย่าง: (1) **Middle East money** เข้ามาที่ inference infra จริงจัง — Aramco ไม่ได้แค่ซื้อ model แต่ back "who ships tokens", (2) NVIDIA ยัง double down กับ neocloud partner แม้ hyperscaler pushback เพราะ Together คือ demand driver ให้ H200/B200 shipment โดยตรง

CEO Vipul Ved Prakash บอกว่าจะใช้เงินก้อนนี้ **scale capacity ประมาณ 50x ใน 5 ปีข้างหน้า** — จาก data center footprint ปัจจุบันที่ใหญ่ขึ้นมาก. คำนวณคร่าว ๆ ถ้า capacity ต้องเพิ่ม 50x, บริษัทกำลังเดิมพันว่า open-source inference demand จะโตแบบ step-function จาก agent workload — ไม่ใช่ chatbot อีกต่อไป

## ทำไมสำคัญ
เรื่องนี้อ่านคู่กับ pattern ที่ Enabridge tracking มาหลายรอบ: **closed-model economics เริ่มแตก, open-source + neocloud เริ่มมี tailwind**. เมื่อ DeepSeek V4 ปล่อย 1M context ที่ 98% ถูกกว่า, เมื่อ Meta ปล่อย Llama รุ่นใหม่ open weights, และเมื่อ Chinese open model เข้าใกล้ frontier ทุกไตรมาส — ต้นทุนของ inference layer commoditize เร็วกว่า model quality gap ตามทัน. Together AI ที่ position ตัวเองเป็น **infrastructure สำหรับใครก็ตามที่ไม่อยากซื้อ API ตรงจาก OpenAI/Anthropic** จึงมี tailwind ธรรมชาติ

ที่น่าคิดคือ **money split**: OpenAI Deployment Co $10B, Anthropic ครั้งที่แล้ว $50B, Microsoft Frontier Company $2.5B — ทั้งหมดเป็น commercial fund ให้ hyperscaler + frontier lab. ส่วน Together $800M, Cerebras, Groq, SambaNova, และ neocloud cluster ที่ Middle East หนุน — คือฝั่ง **picks and shovels**. เมื่อ agent workload เข้ามา multi-step / long-context / high-throughput, cost per output token กลายเป็นตัวคุณค่า มากกว่า benchmark score. Together เดิมพันว่าเมื่อ workload shift ทีมที่ควบคุม **cost per token + latency SLO** จะกินส่วนแบ่งใหญ่ ไม่ใช่ทีมที่มี model ดีที่สุด

## มุม AI Agent Platform
สำหรับ **builders**: ถ้า agent stack ของคุณ round-trip ไป frontier API สำหรับ every tool call — cost model จะพังเมื่อ scale. หันไปดู open-source + neocloud (Together, Fireworks, Groq, Cerebras) สำหรับ high-volume routine call, เก็บ frontier API ให้เฉพาะ complex reasoning step. hybrid routing = savings 5-10x ในหลาย workload. สำหรับ **users/business**: ถ้า vendor agent platform ที่คุณใช้ built บน frontier API เท่านั้น จะกินต้นทุน gross margin ของตัวเอง — ถามได้ว่ามี open-source routing option ไหม เพราะเมื่อไหร่ที่ closed API ขึ้นราคา คุณจะเป็นคนรับ. สำหรับ **ecosystem**: Aramco Ventures นำ Together สื่อว่า Gulf capital pool เข้ามาที่ **AI infra layer** จริงจัง — ต่อจาก G42 กับ MGX ใน UAE, sovereign fund ในภูมิภาคนี้ใช้ AI infra เป็น strategic asset. hyperscaler ที่พึ่ง single source cluster location ต้องคิดใหม่ เพราะ neocloud footprint ที่กระจายไป Gulf, India, Southeast Asia จะกลายเป็น distribution advantage ในหลาย compliance context

## Sources
- [Neocloud Together AI raises $800M, leaps to $8.3B valuation — TechCrunch](https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/)
- [Together AI Raises $800 Million at $8.3 Billion Valuation — BusinessWire](https://www.businesswire.com/news/home/20260701243402/en/Together-AI-Raises-$800-Million-at-$8.3-Billion-Valuation-to-Make-Frontier-AI-Accessible-to-All)
- [Together AI raises $800M: Open-Source Inference Breaks $1B — TechTimes](https://www.techtimes.com/articles/319657/20260703/together-ai-raises-800m-open-source-inference-breaks-1b-closed-models-stall.htm)
- [Together AI raises $800 million Series C at $8.3 billion valuation — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/together-ai-raises-800-million-180132872.html)

---

## Audio script
1 กรกฎาคมที่ผ่านมา Together AI ปิด Series C 800 ล้านดอลลาร์ที่ post-money valuation 8 point 3 พันล้านดอลลาร์ เพิ่มขึ้นมากกว่า 2 เท่าจากรอบก่อน round นี้ Aramco Ventures นำ ตามด้วย NVIDIA Vista Equity General Catalyst Emergence Pegatron และ SentinelOne S Ventures ตัวเลขที่บริษัทเปิดคือ annual bookings ทะลุ 1 พันล้านใน Q2 และ usage ของ open-source model บน platform โต 3 เท่าใน 12 เดือน

Together จะใช้เงินก้อนนี้ scale capacity ประมาณ 50 เท่าใน 5 ปีข้างหน้า สัญญาณว่ามอง demand growth เป็น step function ไม่ใช่ linear — เพราะ agent workload เข้ามาแบบ multi-step long context high throughput cost per output token กลายเป็นตัวชี้ขาดมากกว่า benchmark score

pattern ที่เห็นคือ money แบ่งเป็นสองฝั่ง OpenAI Deployment Co 10 พันล้าน Anthropic 50 พันล้าน Microsoft Frontier Company 2 point 5 พันล้าน คือ commercial fund ให้ hyperscaler กับ frontier lab แต่ Together 800 ล้าน Cerebras Groq SambaNova กับ neocloud ที่ Middle East หนุนคือฝั่ง picks and shovels เมื่อ closed model economics เริ่มแตกจาก DeepSeek Llama open weight เข้าใกล้ frontier — ต้นทุน inference commoditize เร็วกว่า model quality gap ตามทัน

สำหรับ builder ที่ทำ agent อยู่ ถ้า round trip ไป frontier API สำหรับทุก tool call cost model จะพังเมื่อ scale hybrid routing ระหว่าง open-source neocloud กับ frontier API ประหยัดได้ 5 ถึง 10 เท่าในหลาย workload สำหรับ business ที่ใช้ vendor agent platform ถามได้เลยว่ามี open-source routing option ไหม เพราะเมื่อ closed API ขึ้นราคาคุณจะเป็นคนรับ ecosystem ที่ต้องปรับคือ hyperscaler ที่พึ่ง single source cluster เพราะ neocloud footprint ที่กระจายไป Gulf India Southeast Asia จะกลายเป็น distribution advantage ในหลาย compliance context
