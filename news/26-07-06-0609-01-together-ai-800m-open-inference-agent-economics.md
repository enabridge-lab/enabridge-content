---
date: 2026-07-06
slug: together-ai-800m-open-inference-agent-economics
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  A wide editorial isometric scene: a sleek server hangar labeled
  "TOGETHER AI — $8.3B" glowing at night, with pipes flowing out labeled
  "OPEN MODELS: DEEPSEEK / NEMOTRON / KIMI / GLM". A giant scoreboard on
  the wall shows three stacked numbers: "$800M SERIES C", "$1.15B BOOKINGS",
  "6x CHEAPER INFERENCE". On the side, small logo billboards read
  "ARAMCO VENTURES", "NVIDIA", "SALESFORCE VENTURES". In the foreground,
  a silhouette of an engineer walks toward a smaller building labeled
  "DECAGON — CUT INFERENCE 6x". High-contrast cinematic lighting,
  editorial isometric style, 1:1 aspect, readable at 200px thumbnail,
  no real human faces.
image: images/26-07-06-0609-01-together-ai-800m-open-inference-agent-economics.png
---

# Together AI ปิด $800M ที่ $8.3B — open-model inference กลายเป็น "picks-and-shovels" ของยุค agent scale

## TL;DR
- Together AI ปิด **Series C $800M ที่ valuation $8.3B** (1 ก.ค.) — นำโดย **Aramco Ventures**; NVIDIA, Salesforce Ventures, Vista Equity, General Catalyst, Emergence, SE Ventures, March Capital, Pegatron, S Ventures ร่วม
- Annual bookings ทะลุ **$1.15B**; open-weight usage ในแพลตฟอร์ม **โต 3 เท่าใน 12 เดือน**; benchmark เอง 31% TPS สูงกว่า open-source engine ตัวถัดไปใน production coding agent workload
- Case แรกที่ชัดเจน: **Decagon** (customer service agent, ARR $400K/customer median) — สลับจาก closed-model API ไป open model บน Together = **inference cost ลด 6 เท่า**

## เกิดอะไรขึ้น
วันพุธ 1 กรกฎาคม 2026 Together AI ประกาศปิด **Series C $800 ล้านดอลลาร์ ที่ valuation $8.3 พันล้านดอลลาร์** — เป็น secondary + primary round ที่ **doubling valuation** จากรอบก่อน. Round lead โดย **Aramco Ventures** — venture arm ของ Saudi Aramco ซึ่งเป็น sovereign fund ที่กระโดดเข้า AI infrastructure ระดับ hyperscaler ในครึ่งหลัง 2026. Follow-on จาก **NVIDIA** (ยืนยัน chip alignment) + **Salesforce Ventures** (สัญญาณว่า Agentforce runtime จะเชื่อม Together) + Vista Equity, General Catalyst, Emergence Capital, Schneider Electric SE Ventures, March Capital, Pegatron, SentinelOne S Ventures

ตัวเลขที่ Together เปิด: **annual bookings ทะลุ $1.15 พันล้านดอลลาร์** ในไตรมาสล่าสุด (ระดับใกล้ ๆ Snowflake/Databricks ในช่วง pre-IPO); **open-weight model usage บน platform โต 3 เท่าในรอบ 12 เดือน**; และเบนช์มาร์กเองอ้าง **31% TPS (transactions per second) สูงกว่า open-source engine ตัวถัดไปในงาน production coding agent workload** — Together ขายว่าเป็น "cloud infra ที่ enterprise รัน open model ของคนอื่น (DeepSeek, Nemotron, MiniMax, Kimi, GLM) บน NVIDIA GPU cluster ผ่าน OpenAI-compatible API"

Case ที่โชว์ตัวเลข apple-to-apple ในประกาศ: **Decagon** — customer service agent ที่มี median contract $400K/ปี — สลับจาก closed-model API มาใช้ open model บน Together = **inference cost ลด 6 เท่า**. Together ประเมินว่าลูกค้าที่ย้ายจาก closed-model API สู่ open model บน platform ประหยัดได้ **6 – 20 เท่า** (โดยเฉพาะที่ workload = high-volume + low-tolerance-for-latency = agent conversation)

Sam Cheung, CEO Together, ให้สัมภาษณ์กับ TechTimes ว่า "closed-model APIs อยู่ในช่วง plateau ทั้ง performance และ pricing; ตลาดกำลังเปลี่ยนไปที่ 'ใครมี stack ให้ enterprise ควบคุม cost + latency ได้ในระดับ token' — Together ตั้งใจเป็นชั้นนั้น"

## ทำไมสำคัญ
รอบก่อนหน้าเราคุยเรื่อง **model layer commoditize** (Microsoft Frontier / AWS FDE / Anthropic JV / OpenAI Deployment Co รวม $15.1B ใน 90 วัน). รอบนี้ **ชั้นล่างของ stack — inference runtime — กำลังปิดการโหวตของตัวเอง**. Sonnet 5 ($2/$10 introductory) กับ GPT-5.6 Sol เป็น closed-model ที่ราคาถูกที่สุดในตลาด แต่ **ยังแพงกว่า open model บน Together 6 เท่า** สำหรับ workload agent ที่เรียก LLM หลายพันครั้งต่อ session

Sonnet 5 น่ารักตรงที่ smart ใน 80% ของ workload — แต่ agent conversation ระดับพัน request ต่อ session (Decagon-style customer service, Cursor coding session, Devin PR loop) ยังเลือด token อยู่ดี. **Enterprise ที่กำลัง scale agent จากพัน → หมื่น session ต่อวัน มีสองทางเลือก**: (1) contract volume commit กับ frontier lab (Anthropic/OpenAI/Google) ที่ยัง lock spec + rate limit + margin ของ vendor, (2) รัน open model บน Together/Fireworks/Baseten ที่จ่ายเป็น GPU-hour + margin ต่ำกว่า

Round นี้ตอบด้วยเงินว่า **VC + strategic เชื่อทาง #2**. NVIDIA join round เพราะทุก customer ของ Together = customer NVIDIA (Blackwell/Hopper deployment). Salesforce Ventures join เพราะ **Agentforce ในอนาคตต้องมี route ไป open model** — Salesforce ประกาศแล้วว่า Atlas Reasoning Engine ใช้ Claude on Bedrock + Nova, แต่ Bedrock เป็น Amazon walled garden; Together เป็นทางเลือกที่ **BYO-cloud + BYO-region** จ่ายผ่าน Salesforce contract ตรง

Pattern เทียบ AWS vs Salesforce Ventures: AWS launch FDE ให้ Bedrock ผูก customer; Salesforce Ventures ซื้อ minority position ใน Together = **hedge ว่า enterprise ไม่ได้อยาก lock-in ที่ Bedrock ยาว**. เดิมพันของ Together คือ **12–24 เดือนข้างหน้า, 50% ของ token consumption ในโลก agent จะย้ายไป open model** — ถ้าจริง Together ได้ margin ของทั้งชั้น infra ที่ Anthropic/OpenAI/Google ไม่ได้กิน

## มุม AI Agent Platform
- **Builders** — ถ้ากำลังสร้าง agent framework/product ที่ scale จาก pilot → production ใน 12 เดือนข้างหน้า, **routing layer ต้อง support open model บน Together/Fireworks/Baseten day-1** ไม่ใช่ closed-only. Framework ที่ hard-code endpoint (LangChain/CrewAI/Autogen) — เพิ่ม provider adapter Together ใน sprint นี้; ถ้าเป็น product ที่ vertical (legal/healthcare/support) — ทำ A/B test cost benchmark กับ Sonnet 5 + open model 2–3 ตัว, แล้ว publish result เป็น marketing signal. **Distyl, Sierra, Decagon, Cresta enterprise, Parloa** — deal ต่อไปกับ Fortune 500 ต้อง show margin structure ที่ open-model แล้วขายเป็น "ประหยัด 6 เท่า" เข้า CFO conversation ตรง ๆ

- **Users/business ในไทย** — บริษัทที่ pilot agent conversation-heavy (call center, healthcare triage, retail chatbot) มา 6 เดือน เห็นบิล Anthropic/OpenAI ทะลุ $100K/เดือน + คำถาม CFO — **RFP รอบต่อไป**: ให้ vendor เสนอ 2 option (closed vs open on Together/Fireworks) ให้ ROI 12 เดือน apple-to-apple + latency benchmark ในช่วง peak. **SCB, KBank, KTC, AIS, True, dtac** ที่ใช้ Salesforce อยู่ — สัญญาณจาก Salesforce Ventures round ว่า **Agentforce จะเชื่อม Together ในเร็ววัน**; ถ้าคุยกับ AE ได้ ให้ถามว่า BYO open model timeline อยู่ตรงไหน

- **Ecosystem** — จับตา **Fireworks AI** (คู่แข่งหลัก, ROund $1B ที่ $5B ต้นปี), **Baseten** (Kore.ai adjacent), **Modal** (Python-first). NVIDIA GPU allocation เป็น bottleneck จริงในช่วงนี้ — Together ได้ advantage เพราะ NVIDIA join round; **APAC**: AWS Bedrock/Vertex AI ยัง lead ในช่วง 2026 แต่ปี 2027 open-model on-prem หรือ private-region จะเป็นสัญญาที่ CIO ธนาคาร/telecom เอามาเทียบเสมอ

## Sources
- [Together AI Raises $800M: Open-Source Inference Breaks $1B as Closed Models Stall — TechTimes](https://www.techtimes.com/articles/319657/20260703/together-ai-raises-800m-open-source-inference-breaks-1b-closed-models-stall.htm)
- [Together AI Raises $800M Series C — The SaaS News](https://www.thesaasnews.com/news/together-ai-raises-800m-series-c/)
- [Together AI Raises $800M Series C at $8.3B Valuation Led by Aramco Ventures — MLQ AI](https://mlq.ai/news/together-ai-raises-800m-series-c-at-83b-valuation-led-by-aramco-ventures/)
- [Together AI raises $800M at $8.3B valuation as open-source model demand surges — MasterNodeAI](https://www.masternodeai.com/en/news/together-ai-800m-series-c-8-3b-valuation)

---

## Audio script
วันนี้ Together AI ปิดรอบ Series C มูลค่า 800 ล้านดอลลาร์ ที่ valuation 8.3 พันล้าน นำโดย Aramco Ventures ของซาอุดีอาระเบีย มี NVIDIA และ Salesforce Ventures ร่วมด้วย ตัวเลขที่น่าตกใจคือ annual bookings ทะลุ 1.15 พันล้านดอลลาร์แล้ว และ open-weight model usage บน platform โตสามเท่าในหนึ่งปี Together ทำอะไร ก็คือรับเป็น cloud ที่ enterprise เอา open model ของคนอื่น เช่น DeepSeek Nemotron Kimi GLM มารันบน GPU cluster ผ่าน API ที่เหมือน OpenAI ทุกอย่าง case ที่ชัดคือ Decagon customer service agent สลับจาก closed-model API มา open model บน Together แล้ว inference cost ลดหกเท่า ทำไมเรื่องนี้สำคัญ เพราะรอบก่อนเราคุยเรื่อง model layer commoditize ไปแล้ว รอบนี้ inference runtime กำลังปิดโหวตของตัวเอง Sonnet 5 กับ GPT 5.6 Sol เป็น closed model ที่ถูกที่สุดในตลาด แต่ยังแพงกว่า open model บน Together ประมาณหกเท่า สำหรับ agent ที่เรียก LLM หลายพันครั้งต่อ session enterprise ที่กำลัง scale จากพันเป็นหมื่น session ต่อวัน มีสองทางเลือก คือ commit volume กับ Anthropic OpenAI Google แล้วยอม lock in หรือย้ายไป open model บน Together Fireworks Baseten แล้วได้ margin คืนมา NVIDIA join round เพราะทุก customer ของ Together คือ customer ของ NVIDIA Salesforce Ventures join เพราะ Agentforce ในอนาคตต้องมี route ไป open model นอกจาก Bedrock ที่เป็น Amazon walled garden สำหรับธุรกิจไทยที่ pilot agent conversation heavy อย่าง call center healthcare retail chatbot เห็นบิลทะลุ 100,000 ดอลลาร์ต่อเดือน RFP รอบต่อไปควรให้ vendor เสนอสองทาง apple to apple ตัวเลข ROI 12 เดือน ถ้ายัง sell แค่ closed model อย่างเดียว vendor นั้นตกยุคภายในปีนี้แน่นอน
