---
date: 2026-05-08
slug: moonshot-ai-2b-kimi-k26-china-open-source
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: A bold editorial illustration in deep navy and warm cream — at center, a stylized crescent-moon-and-rocket logo (Moonshot AI) glows white, surrounded by 384 small circular nodes representing the "384 experts" in the K2.6 MoE architecture, arranged in a constellation pattern. Above, a Chinese-character watermark "月之暗面" subtly textures the background. To the right, a giant "$2B" rendered in coral sans-serif sits next to "$20B VAL" in cream. A bright coral headline "OPEN-SOURCE MOONSHOT" arches over the top, with "1T PARAMS" rendered very large in cream on the lower-right. Editorial flat-vector style, dramatic spotlight, slate navy + cream + coral + jade-green palette, no human figures, logos crisp for 200px thumbnail readability, 1:1 aspect ratio.
image: images/26-05-08-0927-04-moonshot-ai-2b-kimi-k26-china-open-source.png
---

# Moonshot AI ระดมทุน $2B ที่ valuation $20B — Kimi K2.6 (1T params, 384 experts) เป็น LLM อันดับสองบน OpenRouter

## TL;DR
- 7 พ.ค. 2026 Moonshot AI (ผู้สร้าง Kimi) ปิดรอบ $2B ที่ $20B valuation นำโดย Long-Z (VC ของ Meituan), ตามด้วย Tsinghua Capital, China Mobile, CPE Yuanfeng — เป็น China LLM startup ที่ funded เร็วที่สุดในรอบ 12 เดือน
- ARR ทะลุ $200M ใน เม.ย. 2026 จากการ subscribe Kimi chatbot + API; Kimi K2.6 (1T params, 384 experts MoE, KV cache compression, 1M-token context, 13 ชม. coding session) เป็น LLM ที่ used มากสุดอันดับ 2 บน OpenRouter
- กระทบ: open-source frontier model จากจีนตอนนี้ price-to-performance ดีกว่า GPT/Claude สำหรับ agent workload ที่ต้องการ throughput สูง — DeepSeek กำลัง raise ที่ $45B, Zhipu + MiniMax > $30B แล้ว ตลาดยอมรับว่า "AI ไม่ใช่ของอเมริกาอย่างเดียวอีกต่อไป"

## เกิดอะไรขึ้น

วันที่ 7 พ.ค. 2026 Moonshot AI ปิดรอบ funding $2 พันล้าน ที่ valuation $20 พันล้าน นำโดย Long-Z Investment (VC arm ของ Meituan) ที่ลงทุน $200M เป็น anchor investor พ่วงด้วย Tsinghua Capital (กลุ่มทุนเชื่อม Tsinghua University), China Mobile (state telecom), และ CPE Yuanfeng — combination ของ tech corporate + state-affiliated capital ที่บอกว่า Moonshot ตอนนี้ถูก position เป็น "China's strategic AI champion" ในระดับเดียวกับ DeepSeek ARR ของ Moonshot ใน เม.ย. 2026 ทะลุ $200M แล้ว จากการ subscribe Kimi chatbot ฝั่ง consumer + API enterprise ฝั่ง B2B — ซึ่งเป็นตัวเลขที่บางบริษัท US ($1B+ valuation) ยังไม่ถึง

ตัวที่ทำให้ Moonshot น่ากลัวที่สุดคือ Kimi K2.6 — model ที่ release open-source เมื่อ 20 เม.ย. 2026 ออกแบบเป็น Mixture-of-Experts ขนาด 1 trillion parameters ประกอบด้วย 384 experts (miniature neural networks ที่ specialize ต่างกัน) ใช้ KV cache compression ที่ลด memory footprint ลงมาก, รองรับ context 1 million tokens ผ่าน Kimi Delta Attention, และ handle agentic coding session ที่ยาว 13 ชั่วโมง coordinate sub-agent ได้ถึง 300 ตัว generate code 4,000+ lines ใน run เดียว ตอนนี้ K2.6 อยู่อันดับ 2 ของ LLM ที่ used มากสุดบน OpenRouter (รองจาก Claude Sonnet) — แปลว่า dev จริง ๆ เลือกใช้ ไม่ใช่แค่ benchmark ดี

ที่ทำให้ Moonshot positioning ต่างจาก US frontier lab คือ — open-source license + ราคา inference ถูกกว่า Claude/GPT 5–10 เท่า สำหรับ agent workload ที่รัน 24/7 (coding agent, support agent, reconciliation agent) ส่วนต่างของต้นทุนเดือนละหลายแสน USD บริษัทที่ใช้ K2.6 แทน Claude ใน workflow ที่ไม่ critical ประหยัดได้ทันที DeepSeek ที่อยู่ใน strategy เดียวกันกำลัง raise ที่ valuation $45B (สูงกว่า Moonshot 2x), Zhipu + MiniMax แตะ public market valuation > $30B แล้ว — คือ tier ของ China open-source frontier ขยายเร็วและกว้าง

ที่หลายคนยังไม่เห็นคือ Moonshot strategy ที่กว้างกว่า model — Kimi-VL คือ vision-language model ที่ extract information จาก video ดีกว่า peer (สำคัญกับ surveillance + retail analytics ในจีน), Muon optimization tool optimize model ขนาด 10B+ params, และ Kimi Delta Attention เป็น innovation ที่ paper academic ใช้อ้าง — Moonshot ไม่ใช่ "China's ChatGPT clone" แต่เป็น lab ที่ contribute paper จริงในระดับ peer-review

## ทำไมสำคัญ

ที่สำคัญที่สุดคือ ตลาด AI ปี 2026 ไม่ใช่ "US lab ครองโลก" อีกต่อไป — DeepSeek + Moonshot + Zhipu + MiniMax + Alibaba Qwen + ByteDance Doubao รวมกันเป็น 6 จีน lab ที่มี frontier model ซึ่ง 4 ใน 6 (DeepSeek, Moonshot, Zhipu, Alibaba) เปิด open-source บางส่วน — บริษัทใน ASEAN, Middle East, Africa, Latin America ที่ไม่ต้องการ vendor lock-in กับ US frontier (เพราะ data privacy, cost, sovereignty) มี practical alternative ที่ทำงานได้จริงแล้ว ตัวเลข OpenRouter ที่ K2.6 อันดับ 2 = developer ทั่วโลกโหวตด้วย API call

ที่ pattern คือ — agent workload ตอนนี้ split เป็น 2 ระดับ: critical (ต้องการ accuracy สูง, latency ต่ำ) ใช้ Claude/GPT, vs throughput (รัน 24/7, accuracy 95%+ พอใช้, ราคาเป็นทุกอย่าง) ใช้ K2.6/DeepSeek ใน 12 เดือนข้างหน้า บริษัทเอเชียที่ deploy agent fleet ใหญ่ (เช่น แทน customer service หลักหมื่นคน) จะใช้ K2.6/DeepSeek เป็น default — economics ของ inference ถูกกว่า Claude 5–10x ทำให้ business case มีกำไร

อีกประเด็นที่ลึก: Meituan (ผู้นำ delivery + food + travel ในจีน) เป็น lead investor — ไม่ใช่บังเอิญ Meituan มี data ของ user 700M ที่จะใช้ Kimi train + deploy agent ใน food order, restaurant CS, hotel booking ภายในประเทศ จีนกำลังสร้าง "vertically-integrated AI champion" คล้ายที่สหรัฐมี OpenAI–Microsoft, Anthropic–Amazon — Moonshot–Meituan คือคู่ของจีน

## มุม OpenBridge

ไม่ direct เกี่ยว แต่ adjacent insight ที่ OpenBridge ต้อง position เร็ว: (1) **AI router ระหว่าง provider เป็น core feature ที่ OpenBridge ควรขายราคาเต็ม** — ลูกค้า Thai enterprise ที่กลัว vendor lock + ต้องการ optimize cost จะอยาก route workload ระหว่าง Claude (critical), GPT (general), K2.6/DeepSeek (throughput) ตาม policy รายลูกค้า OpenBridge ที่ทำ provider-agnostic abstraction layer = pricing premium ที่ลูกค้ายอมจ่าย เพราะ break-even ใน 1 เดือนจาก inference cost saving (2) **Sovereignty narrative ของ China model = ขายเข้า government + GLC ของไทยได้ตรง** — ลูกค้าราชการ + KTB + GovTech ที่ไม่อยากใช้ US-only model เพราะ data sovereignty มี alternative คือ Moonshot/DeepSeek hosted in Singapore/HK/Bangkok OpenBridge ที่ wrap K2.6 ผ่าน connector และ certify "data residency Thailand" จะได้ deal flow ที่คู่แข่ง US-aligned ทำไม่ได้ (3) **K2.6 1M-token context + 13-hour coding = dev tool ที่ OpenBridge offer ใน developer mode** — สำหรับ dev ที่ใช้ OpenBridge ทำ integration ลึก K2.6 จะ scan codebase ใหญ่ + suggest connector ที่ optimal ได้ในรอบเดียว ราคาถูกกว่า Claude Code ที่จะต้อง split context — feature ที่ OpenBridge dev plan free tier ใช้ดึงดูด indie developer

Adjacent insight: ที่ Moonshot strategy เปิด open-source + ราคาถูก เป็น playbook ที่ Linux ใช้กับ Windows ในยุค 1995–2005 — open + cheap + good-enough ค่อย ๆ กิน server market จาก Microsoft ในที่สุด AWS เกิดเพราะ Linux พร้อม OpenAI/Anthropic ที่ exclusive + premium อาจเจอชะตาเดียวกันใน 5–10 ปี — OpenBridge ต้องเตรียม thesis ที่ "we serve all models, including the open-source ones that will eat the world"

## Sources
- [China's Moonshot AI raises $2B at $20B valuation as demand for open source AI skyrockets | TechCrunch](https://techcrunch.com/2026/05/07/chinas-moonshot-ai-raises-2b-at-20b-valuation-as-demand-for-open-source-ai-skyrockets/)
- [Open-source AI developer Moonshot AI raises $2B at $20B+ valuation | SiliconANGLE](https://siliconangle.com/2026/05/07/open-source-ai-developer-moonshot-ai-raises-2b-20b-valuation/)
- [Kimi chatbot maker Moonshot AI Valued at $20 Billion in Meituan-Led Round | Bloomberg](https://www.bloomberg.com/news/articles/2026-05-07/kimi-chatbot-maker-moonshot-ai-valued-at-20-billion-in-meituan-led-round)
- [Moonshot AI's $20bn valuation seals one of China's fastest AI funding trajectories | TNW](https://thenextweb.com/news/moonshot-ai-20bn-valuation-kimi-meituan-china-mobile)

---

## Audio script
สวัสดีครับโย วันนี้เรื่องจีน Moonshot AI ผู้สร้าง Kimi ปิดรอบ funding 2 พันล้านดอลลาร์ ที่ valuation 20 พันล้านดอลลาร์ เมื่อ 7 พ.ค. นำโดย Long Z VC ของ Meituan ลงทุน 200 ล้าน เป็น anchor พ่วง Tsinghua Capital China Mobile CPE Yuanfeng combination ของ tech corporate กับ state affiliated capital บอกว่า Moonshot ตอนนี้ถูก position เป็น China strategic AI champion ในระดับเดียวกับ DeepSeek ARR เดือน เม.ย. ทะลุ 200 ล้านแล้ว ตัวเลขที่บางบริษัท US 1 พันล้านดอลลาร์ valuation ยังไม่ถึง

ตัวที่ทำให้น่ากลัวที่สุดคือ Kimi K2.6 model open source release 20 เม.ย. ออกแบบเป็น Mixture of Experts 1 trillion parameter ประกอบ 384 experts ใช้ KV cache compression รองรับ context 1 ล้าน token handle agentic coding 13 ชั่วโมง coordinate sub agent ได้ 300 ตัว generate code 4 พันบรรทัดใน run เดียว ตอนนี้อยู่อันดับ 2 ของ LLM ที่ used มากสุดบน OpenRouter รองจาก Claude Sonnet แปลว่า dev จริงเลือกใช้ ไม่ใช่แค่ benchmark ดี

positioning ต่างจาก US frontier คือ open source license บวกราคา inference ถูกกว่า Claude GPT 5 ถึง 10 เท่า สำหรับ agent workload ที่รัน 24 7 บริษัทใช้ K2.6 แทน Claude ใน workflow ไม่ critical ประหยัดเดือนละหลายแสน DeepSeek กำลัง raise valuation 45 พันล้าน Zhipu MiniMax แตะ 30 พันล้านแล้ว tier ของ China open source frontier ขยายเร็วและกว้าง

ที่สำคัญตลาด AI ปี 2026 ไม่ใช่ US lab ครองโลกอีกต่อไป 6 จีน lab DeepSeek Moonshot Zhipu MiniMax Alibaba Qwen ByteDance Doubao 4 ใน 6 เปิด open source บางส่วน บริษัท ASEAN Middle East Africa Latin America ที่ไม่ต้องการ vendor lock มี practical alternative แล้ว ที่ลึกคือ Meituan เป็น lead investor มี data user 700 ล้าน train Kimi deploy agent ใน food order CS hotel booking จีนกำลังสร้าง vertically integrated AI champion คล้าย OpenAI Microsoft Anthropic Amazon Moonshot Meituan คือคู่ของจีน

มุม OpenBridge สาม insight หนึ่ง AI router ระหว่าง provider เป็น core feature ลูกค้า Thai ที่กลัว vendor lock route workload ระหว่าง Claude critical GPT general K2.6 throughput ตาม policy ราคา premium ที่ลูกค้ายอมจ่ายเพราะ break even 1 เดือนจาก inference saving สอง sovereignty narrative ของ China model ขายเข้า government GLC ไทยได้ตรง KTB GovTech ราชการที่ไม่อยากใช้ US only model OpenBridge ที่ wrap K2.6 certify data residency Thailand ได้ deal flow ที่คู่แข่ง US aligned ทำไม่ได้ สาม K2.6 1 ล้าน token context กับ 13 ชั่วโมง coding เป็น dev tool ใน developer mode dev ที่ใช้ OpenBridge scan codebase ใหญ่ suggest connector ใน รอบเดียว ราคาถูกกว่า Claude Code feature dev plan free tier ดึงดูด indie developer adjacent insight ที่ Moonshot ใช้ playbook Linux กับ Windows ในยุค 1995 ถึง 2005 open cheap good enough ค่อย ๆ กิน OpenBridge ต้องเตรียม thesis ว่า we serve all models รวม open source ที่จะเป็นใหญ่ใน 5 ถึง 10 ปีครับ
