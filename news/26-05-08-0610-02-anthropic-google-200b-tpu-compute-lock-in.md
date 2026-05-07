---
date: 2026-05-06
slug: anthropic-google-200b-tpu-compute-lock-in
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: A bold editorial composition split diagonally across a deep navy frame — left side shows a glowing Anthropic 'A' wordmark in cream, tethered by a heavy chain of golden links arching across the diagonal to a Google 'G' logo on the right side rendered in flat geometric primary shapes. Above the chain a giant cream price tag dangles displaying '$200B' in oversized sans-serif numerals, with '5 YEARS' in coral underneath. Behind the chain, faint silhouettes of stacked TPU chip wafers form a backdrop pattern. A small comparison ribbon at the bottom reads '$40B' in tiny cream type with an arrow pointing the other direction — visually showing the 5x asymmetry. Editorial flat-vector style, navy + cream + coral + soft gold palette, no human figures, designed to read clearly at 200px thumbnail.
image: 
---

# Anthropic ขายอนาคตให้ Google $200B — เงินแลกชิป TPU 5 ปี ขณะที่ Google ลงทุนกลับแค่ 1 ใน 5

## TL;DR
- The Information ตี exclusive วันที่ 5 พ.ค. 2026 — Anthropic ตกลงจ่าย Google Cloud $200B ตลอด 5 ปี เริ่ม 2027 แลก gigawatt+ ของ TPU ที่ออกแบบเฉพาะ training/serving Claude
- Google ลงทุนกลับ "up to $40B" ใน Anthropic เมื่อ 24 เม.ย. — อัตรา reciprocity 5:1; ดีลคิดเป็น 40%+ ของ Google Cloud disclosed backlog แสดงว่า Google ใช้ Anthropic เป็น anchor tenant ของ TPU monetization
- run-rate ของ Anthropic แตะ $30B (ขึ้นจาก $9B end of 2025); วันเดียวกัน OpenAI ย้าย GPT-5.5 ขึ้น Bedrock ฟ้องว่ายุค "1 lab = 1 cloud" จบ; ทุก lab ต้อง multi-cloud + multi-chip

## เกิดอะไรขึ้น

วันที่ 5 พ.ค. 2026 The Information รายงาน exclusive ที่ตลาด financial AI เก็บไม่อยู่ — Anthropic ตกลง commit จ่าย Google Cloud $200B (สองแสนล้าน) ตลอด 5 ปี เริ่มจาก 2027 เป็น compute commitment ที่ใหญ่ที่สุดในประวัติศาสตร์อุตสาหกรรมจาก private company คนเดียว ดีลครอบคลุม "well over 1 GW" ของ TPU capacity ที่ Google จะเปิด online เป็น tranche ตลอด 5 ปีหน้า โดย TPU เหล่านี้ถูกปรับ tune ให้ training และ serve workload ของ LLM ระดับ Claude โดยเฉพาะ ทั้ง Anthropic และ Google ยังไม่ confirm ตัวเลข officially แต่หลาย second source (Yahoo Finance, Engadget, Tech Portal) ยืนยันแหล่งเดียวกัน

ดีลนี้ตามหลังประกาศวันที่ 24 เม.ย. ที่ Google ลงทุน "up to $40B" เพิ่มใน Anthropic — แปลว่า reciprocity ratio อยู่ที่ราว 5:1 ฝั่ง Anthropic จ่ายมากกว่ารับ Anthropic ใช้เงินที่ระดมจาก Google + การ raise อื่นไปซื้อ compute กลับจาก Google เอง pattern ที่ critic เรียกว่า "circular financing" คล้ายกับ Microsoft–OpenAI แต่ scale ใหญ่กว่า ในขณะเดียวกัน Anthropic เปิดเผยวันเดียวกันว่า annualized run-rate revenue แตะ $30B แล้ว — ขึ้นจาก ~$9B ตอน end of 2025 (กว่า 3 เท่าใน 4 เดือน) บริษัทกำลังเผา cash เพื่อโต แต่ก็มี top-line ที่ justify scale compute commitment ขนาดนี้ได้ระดับหนึ่ง

นักวิเคราะห์ Motley Fool คำนวณว่า $200B คิดเป็นกว่า 40% ของ Google Cloud disclosed revenue backlog ทั้งหมด — กล่าวอีกแบบ Anthropic บริษัทเดียวเป็นลูกค้า cloud ใหญ่กว่าทุก SaaS รายเดียวที่ Google เคยมี ตัวเลขนี้ทำให้นักลงทุนใน Alphabet (GOOG) ตื่นเต้น เพราะ TPU ที่เป็น in-house chip กำลังเป็น hardware monetization track ที่ครั้งหนึ่ง Nvidia ครองคนเดียว Anthropic เป็น anchor tenant ที่ทำให้ Google มี volume justify capex ต่อรอบ TPU generation ใหม่ — Google จึงไม่ต้องพึ่ง Nvidia 100% อีกต่อไป

ที่ทำให้เรื่องเด่นขึ้นคือ ภาพรวมตลาด: วันเดียวกันนั้น OpenAI ประกาศย้าย GPT-5.5 + Codex ขึ้น Amazon Bedrock พร้อมเปิด Bedrock Managed Agents — แปลว่า OpenAI ก็ยอมแยกตัวจาก Azure exclusivity เช่นกัน Anthropic ก่อนหน้านี้รับเงิน $5B จาก Amazon (มี $100B ของ AWS spend พ่วง) และเซ็น chip deal กับ Broadcom อีกหลายแสนล้าน — pattern ชัดว่าทุก foundation model lab กำลัง diversify cloud + diversify chip silicon เพื่อไม่ pin ตัวเองกับ vendor เดียว

## ทำไมสำคัญ

ดีลนี้เปลี่ยนสมการ "AI economics" ตรง ๆ — ตอนนี้ทุกคนรู้ว่า compute เป็น bottleneck แต่ scale ของ commitment $200B ปลอดภัย long-term capacity อ่านได้สามอย่าง: (1) Anthropic เชื่อว่า model usage จะโตอีก 10–20 เท่าจาก $30B run-rate (2) ราคา TPU ต่อ token ต่ำกว่าราคา GPU ของ Nvidia พอที่จะ justify lock-in (3) Google ยินดี discount มหาศาลเพื่อ anchor tenant — หาก Anthropic จ่าย full rack rate, ตัวเลขน่าจะใหญ่กว่านี้ถึง 2–3 เท่า

ที่น่าสนใจยิ่งกว่าคือ implication ต่อ Nvidia — ถ้า Anthropic + Google + ภายในของ Google เอง ทำ workload ใหญ่ ๆ บน TPU แทน Nvidia GPU = ตลาด GPU จะแข็งแรงเฉพาะกลุ่ม training startup + research lab + cloud อื่นที่ไม่มี chip in-house Nvidia ยังคงเป็น default ของ developer แต่ "AI utility computing" ระดับ trillion-token-per-day กำลัง shift ไปสู่ in-house chip ทุกค่าย (Google TPU, Amazon Trainium, Microsoft Maia, Meta MTIA) สถานการณ์ตอน 2024 ที่ Nvidia เป็น monopoly เริ่มมี crack จริงในปี 2026

อีกประเด็นเชิง business model: Anthropic + OpenAI ทั้งสองค่ายกำลัง expand "service push" — ตามที่ CIO Magazine รายงาน ทั้งสองเริ่มทำ professional services + forward-deployed engineering ให้ลูกค้าระดับ Fortune 500 (Goldman, Blackstone, Moody's, Oracle, State Farm) เพราะ enterprise ต้องการมากกว่า API ต้องการ "บริษัทที่ออกแบบ agent workflow ให้" pattern คล้าย Palantir + Accenture — กล่าวคือ frontier lab ไม่ใช่ pure software company อีกต่อไป กำลังกลายเป็น hybrid software + services + compute utility

## มุม OpenBridge

ดีลนี้ดูไกล แต่กระทบ OpenBridge สามทาง: (1) **ราคา API ของ Claude จะ stable + ลดลงในระยะยาว** — Anthropic lock TPU ที่ deflationary cost curve เทียบ GPU; แปลว่าถ้า OpenBridge build agentic workflow บน Claude แทน GPT จะมี cost predictability ดีกว่าในระยะ 3–5 ปี ทีม product ควรประเมิน cost-per-1k-token ของ Claude vs GPT บน workflow OpenBridge ที่ใหญ่ที่สุด (data sync, schema mapping, customer context) แล้ววางแผน multi-model routing — ลูกค้าจ่ายน้อยลงโดยที่ outcome เท่าเดิม (2) **Anthropic + Google จะออก "Claude on Vertex AI Agent Builder" stack ต่อจากนี้แน่** — ลูกค้าใหญ่ของไทย (SCB, KBank, ปตท.) ใช้ GCP เยอะ; ถ้า OpenBridge มี "Vertex AI native connector" ที่รัน Claude agent บน TPU ของลูกค้าโดยตรง — ลูกค้าจะไม่มี data egress, latency ต่ำ, compliance ผ่านง่าย — เป็น differentiator ชัดเจน (3) **ระวัง circular financing risk** — ถ้า Anthropic run-rate ไม่โตตามที่ promise ($30B → $100B+ ภายใน 2027), ดีลนี้ unwind ได้; OpenBridge ควรมี multi-model fallback architecture ตั้งแต่วันนี้ ไม่ทำตัวเป็น Anthropic-only หรือ OpenAI-only — ลูกค้า enterprise ของไทยจะ value "vendor-neutral" สูงในยุคนี้

ไม่ direct เกี่ยว แต่ adjacent insight: ตลาดกำลังบอกว่า "compute = currency หลักของ AI era" OpenBridge ขายไม่ใช่ compute แต่ขาย "data flow ที่ทำให้ compute ของลูกค้าผลิต outcome ได้" ให้คิด pricing ในมิติ "value of data delivered to agent" ไม่ใช่ "row processed" — ตรงกันกับวิธี OpenAI/Anthropic เริ่ม charge

## Sources
- [Anthropic Commits to Spending $200 Billion on Google's Cloud and Chips | The Information](https://www.theinformation.com/articles/anthropic-commits-spending-200-billion-googles-cloud-chips)
- [Anthropic Just Promised Google $200 Billion. That's Five Times What Google Is Paying Anthropic | Let's Data Science](https://letsdatascience.com/blog/anthropic-200-billion-google-cloud-five-year-commitment-may-5)
- [Anthropic enters $200Bn agreement with Google for cloud and TPU chips | The Tech Portal](https://thetechportal.com/2026/05/06/anthropic-enters-200-billion-agreement-with-google-for-cloud-and-tpu-chips)
- [Anthropic reportedly agrees to pay Google $200 billion for chips and cloud access | Engadget](https://www.engadget.com/2165585/anthropic-reportedly-agrees-to-pay-google-200-billion-for-chips-and-cloud-access/)

---

## Audio script
สวัสดีครับโย ข่าวใหญ่จาก The Information คือ Anthropic ตกลงจ่าย Google Cloud สองแสนล้านดอลลาร์ตลอด 5 ปี เริ่ม 2027 เป็น compute commitment ที่ใหญ่ที่สุดในประวัติศาสตร์ private company ดีลครอบคลุม TPU capacity เกิน 1 gigawatt ที่ Google ออกแบบเฉพาะสำหรับรัน Claude

ที่น่าสนใจคือเทียบกับที่ Google ลงทุนกลับใน Anthropic up to 40 พันล้านเมื่อ 24 เมษา reciprocity อยู่ที่ 5 ต่อ 1 Anthropic จ่ายมากกว่ารับ pattern circular financing ระดับใหม่ของ AI era นักวิเคราะห์ Motley Fool คำนวณว่า 200 พันล้าน คิดเป็นกว่า 40% ของ Google Cloud backlog ทั้งหมด แปลว่า Anthropic บริษัทเดียวคือลูกค้า cloud ใหญ่กว่า SaaS รายอื่นที่ Google เคยมี

context ของวงการคือวันเดียวกัน OpenAI ก็ย้าย GPT 5.5 ขึ้น Amazon Bedrock ทุก foundation model lab กำลัง diversify cloud diversify chip ยุค 1 lab 1 cloud จบแล้ว และ Nvidia เริ่มเสียส่วนแบ่งใน workload ระดับ trillion token per day ให้ in house chip ทุกค่าย TPU Trainium Maia MTIA

มุม OpenBridge สามเรื่อง หนึ่งราคา Claude API จะ stable ลดลงในระยะยาว เพราะ TPU ถูกกว่า GPU ทีม product ควรประเมิน cost ต่อ 1k token ของ Claude vs GPT แล้ววาง multi model routing สองคือ Anthropic Google จะออก Claude on Vertex AI ต่อจากนี้ ลูกค้าไทยใช้ GCP เยอะ ถ้ามี Vertex native connector ของ OpenBridge รัน Claude agent บน TPU ของลูกค้า ไม่มี egress ไม่มี latency เป็น differentiator ชัด สามคือ multi model fallback architecture ตั้งแต่วันนี้ อย่า lock vendor เดียว ลูกค้า enterprise จะ value vendor neutral สูงครับ
