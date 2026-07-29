---
date: 2026-07-30
slug: amd-anthropic-nvidia-sk-4gw-agentic-compute-crunch
topic: openbridge-trend
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial isometric illustration on a deep navy background: two colossal
  data center towers rising from opposite corners of a global map — one
  labeled "ANTHROPIC + AMD — 2 GW · $5B" glowing red, one labeled
  "NVIDIA + SK GROUP — 2 GW · $500B" glowing green. A third smaller
  facility in the corner reads "SAMSUNG + BROADCOM — $200B MoU". Between
  them a giant clock reads "8 DAYS" and a scoreboard shows "4 GW+
  AGENTIC COMPUTE ANNOUNCED". At the base of both towers a tag reads
  "H1 2027 LIVE". Sharp editorial typography, cinematic depth, 1:1
  aspect, no real human faces.
image: images/26-07-30-0611-03-amd-anthropic-nvidia-sk-4gw-agentic-compute-crunch.png
---

# 8 วัน 4 กิกะวัตต์ — AMD ทุ่ม 5B ใน Anthropic + Nvidia ล็อก SK 500B พร้อม HBM4 — compute กลายเป็นตัวชี้ว่า agentic AI ใครจะ scale ได้จริง

## TL;DR
- 22 ก.ค. **AMD + Anthropic** ประกาศ strategic partnership ระดับ **multi-billion dollar** — Anthropic จะ deploy **2 GW ของ AMD Instinct MI450 GPUs**, AMD จะ **invest up to $5 billion in Anthropic**, และ optimise software stack ร่วมกัน
- 24-25 ก.ค. **Nvidia + SK Group** ประกาศ LOI มูลค่า **$500 พันล้านบวก** — สร้าง **2 GW AI data center** ในเกาหลี ใช้ **Vera Rubin chips + HBM4 memory** จาก SK Hynix — เปิดใช้งานครึ่งแรกของปี 2027
- 28 ก.ค. **Samsung + Broadcom** เซ็น MoU **$200 พันล้าน** — memory chips + foundry services — เปิด front รอง
- **รวมภายใน 8 วัน**: **4 GW+ ของ agentic AI compute capacity** ถูก commit — ปริมาณเท่ากับ **~4 nuclear power plants**
- Anthropic ได้ **diversification จาก Nvidia** ครั้งแรก; Nvidia ได้ **HBM supply lock** จาก SK Hynix + Samsung ผ่าน US<>Korea axis; ผู้แพ้ = **hyperscaler ที่รอดู** (Meta, Oracle, small clouds)
- Signal: **compute กลายเป็น constraint จริงของ agentic scaling** — vendor ที่ล็อก GW ได้ก่อนจะกำหนด agent economics ของทั้ง ecosystem 2027-2028

## เกิดอะไรขึ้น
ภายในเวลา **8 วัน** ปลายเดือนกรกฎาคม 2026 — โลกได้เห็น deal compute agentic AI ระดับ **gigawatt** สาม deal ติดต่อกัน. Signal จับตรงกันหมด: **compute ไม่ใช่ปัญหา engineering แล้ว — เป็นปัญหา diplomacy + capital allocation ระดับประเทศ**.

**22 กรกฎาคม**: **AMD + Anthropic** ประกาศ deal ที่ Wall Street เรียกว่า *"most significant foothold AMD's had in the market since AI boom began"*. โครงสร้าง 3 ส่วน: (1) AMD ขาย Anthropic ระดับ **tens of billions dollars** ของ AI servers, (2) Anthropic จะ deploy **2 GW** ของ **AMD Instinct MI450 GPUs** ใน **AMD Helios rack-scale solutions** — deployment แรก **1 GW เปิดใช้งานครึ่งแรกของ 2027**, (3) AMD จะ **invest up to $5 billion in Anthropic**. นี่เป็น **ครั้งแรกที่ Anthropic มี compute stack นอก Nvidia อย่างจริงจัง** — ก่อนหน้านี้ Anthropic ใช้ AWS Trainium (partial) + Google TPU (Google $2B investment) + Nvidia GPU. AMD กลายเป็นขาที่สี่ — **diversification move ที่ Anthropic ต้องทำก่อน 2027 model generation** ที่จะกินไฟหนักกว่า Claude Opus 5 ปีที่แล้ว 5-10 เท่า.

**24-25 กรกฎาคม**: **Nvidia + SK Group** ประกาศ **LOI มูลค่า $500 พันล้านบวก** — deal ที่ CNBC เรียกว่า *"changes AI race"*. Deal มี 3 axis: (1) **SK Telecom สร้าง 2 GW AI data center** ในเกาหลี ใช้ **Nvidia Vera Rubin chips + HBM4 memory** — เปิดใช้งาน 2027, (2) **Nvidia + SK Hynix ล็อก long-term partnership** สำหรับ **co-develop next-gen AI memory** including HBM (Nvidia lock memory supply — สิ่งที่ analyst หลายคนเรียก "the real bottleneck"), (3) framework สำหรับ scale multiple AI factories ในเกาหลี. Motley Fool + Yahoo Finance คาดว่า deal นี้จะทำให้ทั้ง Nvidia + SK Hynix เป็น *big winners* ระยะยาว — เพราะ HBM supply constraint คือปัญหาหลักที่ทำให้ hyperscaler ที่ไม่ใช่ hyperscaler ระดับ Microsoft/Google ต้องรอเป็นปี ๆ กว่าจะได้ chip.

**28 กรกฎาคม**: **Samsung Electronics เซ็น MoU $200 พันล้าน กับ Broadcom** — memory chips + foundry services. Deal นี้ smaller scale แต่ complete triangle **Nvidia (design) + SK Hynix (HBM) + Samsung (foundry + memory)** ที่ล็อก **US<>Korea agentic AI supply chain** ในช่วง 2027-2030. เทียบกับ Nvidia's Taiwan concentration ที่ TSMC — deal Korea เป็น *geopolitical hedge* ที่ Trump administration ต้องการ (ลด dependency บน Taiwan) และ Nvidia ต้องการเช่นกัน (Trump tariff on Taiwan wafer risk).

**เอา 3 deal มารวมกัน**: 2 GW (AMD-Anthropic) + 2 GW (Nvidia-SK) + capacity ที่จะเกิดจาก Samsung-Broadcom = **4 GW+ ของ agentic AI compute ถูก commit ภายใน 8 วัน**. เพื่อ scale — **1 GW ≈ 500,000-750,000 GPU** (H100/MI300 range) — 4 GW = **2-3 ล้าน GPU new capacity** ที่จะออนไลน์ H1 2027. บริบทเปรียบเทียบ: ทั้งโลกมี AI-dedicated GPU deployment รวม **~5 ล้านตัว ณ ต้น 2026** — ปริมาณที่ deal เดือนนี้ commit **จะเพิ่ม installed base ขึ้น 40-60%** ภายในปีเดียว.

Anthropic ระดับ CEO ให้เหตุผลในโพสต์บริษัท: *"we're focused on serving frontier customers with the most performant, cost-effective infrastructure — this partnership with AMD makes that possible at gigawatt scale"*. Nvidia CEO Jensen Huang ในการแถลงร่วมกับ SK Chairman Chey Tae-won บอก *"South Korea is becoming a strategic AI factory hub"*. ทั้ง 3 deal มี **timeline convergent — H1 2027 first operational** — จับกันด้วย synchronised commitment cycle ที่ค่ายลูกค้าใหญ่ (Anthropic, OpenAI, Google) ต้อง lock supply ก่อน frontier model 2027.

## ทำไมสำคัญ
**Compute เข้าเฟส "sovereign infrastructure" — ไม่ใช่ commodity อีก**. ปีก่อน argument ยอดฮิตของ investor คือ *"agent race จะ commoditize compute เร็ว"* — เพราะทุกคนใช้ chip เดียวกัน. Deal สามอันในสัปดาห์นี้ **ปฏิเสธ thesis ดังกล่าวโดยตรง** — chip กลายเป็น differentiator จริง + memory supply กลายเป็น moat. **Anthropic ที่ diversify ไป AMD** — ป้องกัน Nvidia hold pricing power ระยะยาว + ได้ MI450 ที่ software stack ทีม Anthropic ช่วย optimize ให้ (co-design). **Nvidia ที่ล็อก SK Hynix** — ป้องกัน AMD, Intel, Broadcom แย่ง HBM supply — เพราะ HBM4 คือ constraint จริงของ 2027-2028 (ไม่ใช่ compute die). **ผู้ที่ยังไม่ล็อก supply — Meta, Oracle, small clouds** — จะเจอ delivery lead time 12-18 เดือน + premium pricing.

Pattern ที่เห็นชัด: **agentic AI economics ถูก set ที่ layer infrastructure — ไม่ใช่ layer model หรือ layer application**. Startup ที่ compete บน model quality (mistral, cohere, ai21) หรือ compete บน application (glean, harvey, hebbia) — ยังไงก็ต้องผ่าน compute layer ที่มี Anthropic/OpenAI/Google/Meta ล็อก long-term commit. Pricing ของ inference ที่ agent ต้องจ่ายจะ track ตาม access to gigawatt compute — และ deal สัปดาห์นี้ **สร้าง price floor** สำหรับ inference cost ในปี 2027 (คนที่ล็อก supply ตอนนี้ = price setter). **The Register, Wall Street Journal, และ CNBC** อ่านตรงกัน: 2027 จะเป็นปีที่ **inference cost stop declining** เพราะ demand โต faster than supply.

**Anthropic ได้ leverage เชิง strategic ใหญ่ที่สุด**: (1) มี 3 stack — Nvidia (via AWS + Google), Google TPU, AMD MI450 — competition ระหว่าง vendor ทำให้ Anthropic negotiate ราคาได้ดีที่สุด, (2) กระจาย geographic risk — บาง GW จะอยู่ US, บาง GW อยู่ EU (Anthropic UK plans), บางส่วนอาจ Korea/Japan, (3) **funding + compute แบบ vertical integration** — Google $2B + Amazon $8B + AMD $5B — Anthropic กำลังมี **balance sheet ที่ backed by hyperscaler ตรง** ระดับที่แม้แต่ OpenAI ยังไม่มีถึงขนาดนี้ (OpenAI มี Microsoft $10-15B แต่ locked in Azure). สำหรับ **valuation** — เป็นเหตุผลที่ Anthropic secondary rumor $150B ต้น 2026 ดูสมเหตุสมผลกว่าที่ควรจะเป็น.

## มุม AI Agent Platform
**Builders:** ถ้ากำลัง build agent framework / runtime — **assumption ว่า inference จะ cheap มากขึ้นต่อไป จะไม่จริงในปี 2027**. Cost per token ที่ตกลง 10x ตั้งแต่ 2023 จะ *stop declining* — เพราะ demand จาก autonomous agent (ที่ใช้ token 100-1000x เทียบ chat) กินหมด. **Design agent architecture ให้ token-efficient ตั้งแต่วันแรก**: (1) cache aggressive — reuse retrieval + reasoning ที่คุ้มค่า reuse, (2) escalate model tier ก่อน escalate token — ใช้ Haiku/Flash/Nano สำหรับ 80% task, reserve Opus/Ultra สำหรับ 20% ที่ต้องการ, (3) instrument token accounting per action — ให้ FinOps team ของลูกค้า audit ได้. **Framework ที่ build-in cost accounting** (Vercel AI SDK ที่มี cost tracker, LangGraph ที่มี node-level budget) จะ preferred over framework ที่ไม่มี.

**Users / business:** ถ้าจะ scale agent ใน production Q3-Q4 2026 — **lock inference contract ตอนนี้** ก่อน spot price ขึ้น. Anthropic, OpenAI, Google ทั้งหมด offer volume commitment + reserved capacity ที่ discount 20-40% เทียบ on-demand. **RFP ปีนี้ต้องมี clause about compute committed capacity** — vendor ที่ commit dedicated inference (Salesforce Agentforce Ultra tier, Microsoft PTU) จะ deliver latency + cost predictability ที่ competitor on shared capacity ทำไม่ได้. สำหรับ **Thai enterprise (K-Bank, SCB, AIS, PTT, CPALL)** — คุยกับ AWS, Google, Azure ในไทยเรื่อง sovereign inference capacity (Bangkok region) — เพราะ latency + data residency ก็สำคัญเช่นกัน + ราคาจะไปทางเดียวกับ global market ใน 2027.

**Ecosystem:** ผู้ชนะรอบนี้ — **AMD** (ในที่สุดก็ได้ frontier customer จริง — MI450 pipeline ปลอด revenue risk), **SK Hynix** (HBM4 supply lock — stock price น่าจะ re-rate), **Anthropic** (compute + capital + optionality), **Cloudflare/Vercel/Fly.io** (serverless inference ที่ leverage stateless MCP spec, deploy บน multiple compute vendor). ผู้แพ้ — **Meta** (ยังต้อง lock supply ด้วยตัวเอง + $145B capex ที่ Zuck ประกาศจะยังไม่พอ), **Oracle** (OCI ที่ยังไม่มี frontier customer lock), **small model providers** (mistral, ai21 ที่ต้อง compete on API price without supply lock). **Regional angle**: **Thailand + SEA data center player** (True IDC, INET, TCC) — window เปิดให้ partner กับ AMD/Nvidia/SK เรื่อง regional compute hub — ไม่ใช่ frontier training แต่ **inference layer สำหรับ SEA agent deployment** ที่ต้องการ low latency + PDPA compliance.

## Sources
- [AMD and Anthropic Announce Strategic Partnership to Deploy Up to 2 Gigawatts of AMD Instinct MI450 Series GPUs — AMD Newsroom](https://newsroom.amd.com/news/amd-anthropic-strategic-partnership/)
- [AMD to invest up to $5 billion in Anthropic as part of computing power deal — CNBC](https://www.cnbc.com/2026/07/22/amd-anthropic-ai-chip-investment.html)
- [SK Group and NVIDIA Expand Strategic Partnership Across AI Factories and Next-Generation Memory — SK hynix Newsroom](https://news.skhynix.com/en/skhynix-nvidia-partnership-2026/)
- [Nvidia and SK Group announce $500bn AI agreement, includes 2GW of data center capacity — DataCenterDynamics](https://www.datacenterdynamics.com/en/news/nvidia-and-sk-group-announce-500bn-ai-agreement-includes-2gw-of-data-center-capacity/)
- [Nvidia locks down memory supply from SK Hynix as part of $500 billion AI deal — CNBC](https://www.cnbc.com/2026/07/25/nvidia-locks-down-memory-from-sk-hynix-as-part-of-500-billion-ai-deal.html)

---

## Audio script
เรื่องสุดท้ายวันนี้คือ compute race ที่ปลายเดือนกรกฎาคมจบด้วย 3 deal ระดับ gigawatt ภายในเวลา 8 วัน. 22 กรกฎาคม AMD กับ Anthropic ประกาศ partnership — Anthropic จะ deploy 2 กิกะวัตต์ของ AMD Instinct MI450, AMD จะ invest up to 5 พันล้านดอลลาร์ใน Anthropic — เป็นครั้งแรกที่ Anthropic มี compute stack นอก Nvidia อย่างจริงจัง. 24-25 กรกฎาคม Nvidia กับ SK Group ประกาศ LOI 500 พันล้านดอลลาร์บวก — 2 กิกะวัตต์ AI data center ในเกาหลี ใช้ Vera Rubin chip กับ HBM4 จาก SK Hynix. 28 กรกฎาคม Samsung เซ็น MoU 200 พันล้านดอลลาร์กับ Broadcom.

รวม 3 deal — 4 กิกะวัตต์ compute capacity ถูก commit ภายใน 8 วัน — ประมาณ 2-3 ล้าน GPU ที่จะออนไลน์ครึ่งแรกของ 2027 — เพิ่ม installed base โลกขึ้น 40-60 เปอร์เซ็นต์ภายในปีเดียว.

signal ที่ต้องอ่าน — compute เข้าเฟส sovereign infrastructure ไม่ใช่ commodity. Argument ปีก่อนที่ว่า agent race จะ commoditize compute — ปฏิเสธโดยตรง. Chip กับ HBM supply กลายเป็น moat จริง. Anthropic diversify ไป AMD ป้องกัน Nvidia hold pricing power. Nvidia ล็อก SK Hynix ป้องกัน AMD Intel Broadcom แย่ง HBM. Meta, Oracle, small clouds ที่ยังไม่ล็อก supply จะเจอ lead time 12-18 เดือน + premium pricing.

pattern สำคัญที่สุด — cost per token จะ stop declining ในปี 2027 เพราะ demand จาก autonomous agent ที่ใช้ token 100-1000 เท่า chat กินหมด supply ที่เพิ่ม. Builder ต้อง design agent architecture ให้ token efficient ตั้งแต่วันแรก — cache aggressive, escalate model tier ก่อน escalate token, instrument accounting per action. Enterprise ที่จะ scale agent Q3-Q4 นี้ — lock inference contract ตอนนี้ก่อน spot price ขึ้น. สำหรับ Thai enterprise คุยกับ AWS Google Azure เรื่อง Bangkok region sovereign inference — เพราะ latency กับ data residency ก็สำคัญ + ราคาจะไปทางเดียวกับ global market ใน 2027.
