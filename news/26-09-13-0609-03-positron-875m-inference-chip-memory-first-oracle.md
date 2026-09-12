---
date: 2026-09-13
slug: positron-875m-inference-chip-memory-first-oracle
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: |
  An editorial isometric illustration of a server rack in a data
  center: on the left side a single monstrous glowing chip labeled
  "HBM" being fed by tiny expensive-looking gold coins; on the right
  side a compact clean chip labeled "ASIMOV" fed by a steady stream
  of grey commodity memory bricks stamped "LPDDR5X"; a large bold
  headline banner across the top reads "$875M · $5B · 16T PARAMS".
  Editorial style, deep midnight-blue background with cyan and amber
  accents, strong rim light, high-contrast readable at 200px thumbnail,
  1:1 aspect, no real human faces.
image: images/26-09-13-0609-03-positron-875m-inference-chip-memory-first-oracle.png
---

# Positron ระดม $875M ที่ $5B — เอา commodity memory ไปท้า HBM ในตลาด inference; Jim Clark กลับมา, Oracle เดินขบวนแรก

## TL;DR
- Positron AI ปิด **Series C $875M** ที่ **valuation $5B post-money** (10 ก.ย.) — แบ่งเป็น C-round $375M ($3.5B pre-money) + C-1 tranche สูงสุด $500M
- Lead: **NEA** + **Atreides** + **Valor Equity** + **Andra Capital** + **SemiAnalysis Capital** (Dylan Patel); C-1 นำโดย NEA + **Jim Clark** (Silicon Graphics / Netscape founder)
- **Bet ที่ contrarian:** ใช้ **commodity LPDDR5X memory** แทน **HBM** ที่ Nvidia lock ตลาด — architecture "memory-first" สำหรับ inference โดยเฉพาะ
- Product roadmap: **Atlas** (Gen 1) deployed แล้ว **50+ rack ที่ Oracle Cloud Infrastructure**, ลูกค้ารวม Parasail, Jump Trading, i3d.net; **Asimov** (Gen 2) tape out TSMC N3P ปลายปี, production H2 2027; **Titan** (system) รวม Asimov 4-8 ตัวใน 1 node รองรับ model **16T+ params + 10M+ token context**

## เกิดอะไรขึ้น

**10 กันยายน 2026** — Positron AI ประกาศปิด **Series C $875M** ที่ **$5B post-money valuation**. โครงสร้าง round มีสองชั้น: (1) Series C **$375M** ที่ pre-money $3.5B — co-led NEA, Atreides Management, Valor Equity, Andra Capital, Dylan Patel ที่ **SemiAnalysis Capital**; (2) Series C-1 สูงสุด **$500M** — led NEA + **Jim Clark** (co-founder Silicon Graphics, Netscape). การที่ Jim Clark ที่ 74 ปีกลับมาลง big check ในบริษัท semiconductor รอบใหม่ signal ว่าตลาด inference silicon เป็น structural bet ระดับ decade

**Bet ที่ contrarian ของ Positron:** ใช้ **LPDDR5X memory ที่เป็น commodity** (มือถือ / consumer chip ใช้กัน) แทน **HBM ที่ Nvidia lock supply ผ่าน SK Hynix, Samsung, Micron**. หลักการทาง architecture คือ inference workload memory-bound มากกว่า compute-bound — ถ้า design chip ให้ memory bandwidth + capacity เยอะ ไม่ต้อง compute density สูงเท่า training chip. **Asimov** (Gen 2) จะมี memory **288GB – 2,304GB per chip** — เทียบกับ H100 ที่ 80GB, B200 ที่ 192GB. capacity ที่กว้างขึ้นแปลว่า **model 16T parameter รันได้ใน node เดียว** ไม่ต้อง shard

Product ที่วิ่งอยู่แล้ว: **Atlas** (Gen 1 inference system) deploy **50+ rack ที่ Oracle Cloud Infrastructure** — ตอกย้ำว่า Oracle ไม่ได้แค่ทำ deal Nvidia $300B แต่ diversify supplier เต็มตัว. Customer อื่นที่ยืนยันแล้ว: **Parasail** (inference-as-a-service ที่ resell Atlas capacity), **Jump Trading** (HFT firm ที่ใช้ inference low-latency), **i3d.net** (game hosting infrastructure ที่ทำ AI companion / NPC). Positron ยัง cite **Anthropic** เป็น "evaluation partner" (ไม่ commit deployment)

Use of proceeds: (1) Asimov **tape out ปลาย 2026 บน TSMC N3P** — process 3nm generation หลัง N3E; (2) **2-megawatt engineering data center + emulation platform**; (3) production ramp **Titan** — system รวม Asimov 4–8 ตัวใน node เดียว สำหรับ model **16T+ params + 10M+ token context window**

## ทำไมสำคัญ

Pattern ที่เห็นใน semiconductor stage คือ **inference market แยกออกจาก training market**. Training ยังเป็น Nvidia dominant (H100/B200/Rubin ผูก HBM + NVLink + CUDA) — inference กำลัง fragment ให้ specialist หลายค่าย: Cerebras (wafer-scale), Groq (LPU), SambaNova (RDU), Etched (Sohu ASIC), และตอนนี้ Positron ที่ commodity memory. **Reason** คือ economics ต่างกัน — training runs 10K-100K chip 6-12 เดือน; inference runs 100M query/day ตลอดปี = **energy + memory bandwidth ต่อ query สำคัญกว่า peak FLOPs**

signal ที่คมกว่าคือ **Jim Clark กลับมาลงระดับ big check**. Clark วางมือจาก tech หลัง Netscape IPO 1995 มา 30 ปี — การกลับมาลง $500M anchor round นี้แปลว่า มองเห็น **"Silicon Graphics moment"** ในตลาด inference. SGI ในยุค 90s ชนะ workstation graphics ด้วย custom silicon ที่ commodity chip ตามไม่ทัน; ตอนนี้ Positron ทำในทิศ**ตรงกันข้าม** — ใช้ commodity memory ไปกด HBM ที่กลายเป็น "custom + supply-locked". Playbook ต่างกันแต่ theme เดียวกัน: **memory + interconnect คือ battleground**

จุดคมที่ 3 คือ **Oracle เดินเกม supplier diversification เต็มตัว**. Oracle Cloud Infrastructure เพิ่งประกาศ $300B Nvidia deal เดือนก่อน — deploy Atlas 50+ rack แปลว่า OCI ไม่ต้องพึ่ง Nvidia 100%. AWS (Trainium/Inferentia), Google (TPU), Meta (MTIA) มี in-house silicon อยู่แล้ว; Oracle ที่ไม่มี chip design DNA ต้อง **outsource แต่ diversify** — Positron เป็น bet แรก, คาดว่าจะตามด้วย Groq หรือ SambaNova ภายในไตรมาส

## มุม AI Agent Platform

**สำหรับ Builders** ที่รัน agent workload — agent มี characteristic ที่ต่างจาก chatbot: **long-running session + heavy tool call + repeated context**. Positron memory-first architecture ตรงกับ agent workload มากกว่า training-derived chip — เพราะ agent มี **KV cache ที่ยาว, context ที่ต้อง persist ข้าม turn**. Builder ที่วางแผน 6-12 เดือนควรถาม cloud vendor ว่ามี **Positron / Groq / SambaNova instance offer ไหม** — cost per token ตอน scale อาจถูกกว่า H100/B200 ~40-60% ตาม workload

**สำหรับ Users / Business** ที่ deploy agent: (1) ถ้ายังอยู่ใน pilot stage — ไม่ต้องคิดเรื่อง chip แต่ถ้ากำลังจะ scale ไปหลักล้าน query/day, **inference chip choice จะเข้ามาใน RFP**; (2) Oracle Cloud (มี Atlas เดินอยู่) กำลังเป็นทางเลือกที่ competitive สำหรับ agent workload — ถ้าเดิมใช้ Azure/AWS ให้ evaluate benchmark; (3) enterprise ไทย/APAC ที่มี data residency requirement ควรถามว่า Oracle Bangkok/Singapore region จะได้ Atlas cluster เมื่อไหร่ — น่าจะ H1 2027

**สำหรับ Ecosystem** (cloud / silicon / model vendor): **HBM supply crunch** ที่เป็น chokepoint ของ Nvidia (SK Hynix + Samsung + Micron ผลิตไม่ทันตลอด 2 ปีที่ผ่านมา) — ถ้า Positron scale ได้จริง จะเบี่ยงส่วนของ inference market ไป LPDDR5X ที่ production capacity ใหญ่กว่า 5-10 เท่า. Memory vendor (Micron, Samsung) ที่ diversify LPDDR5X pipeline จะได้ประโยชน์; Nvidia ที่ margin สูงบน inference จะโดนบีบก่อน — CUDA lock ยังมี แต่ **"Nvidia tax" ในตลาด inference จะเริ่มถูก question ในบอร์ด**

## Sources
- [Semiconductor Digest — Positron AI Raises $875 Million at a $5 Billion Valuation](https://www.semiconductor-digest.com/positron-ai-raises-875-million-at-a-5-billion-valuation-to-bring-its-next-generation-inference-silicon-to-market/)
- [Yahoo Finance — Positron AI raises $875 million Series C at $5 billion valuation](https://finance.yahoo.com/technology/ai/articles/positron-ai-raises-875-million-140907288.html)
- [Implicator — Positron Raises $875M at $5B Before Its Asimov Chip Tapes Out](https://www.implicator.ai/positron-raises-875-million-at-5-billion-before-its-asimov-chip-tapes-out/)
- [PRNewswire — Positron AI Raises $875 Million at a $5 Billion Valuation](https://www.prnewswire.com/news-releases/positron-ai-raises-875-million-at-a-5-billion-valuation-to-bring-its-next-generation-inference-silicon-to-market-302874601.html)
- [BigGo Finance — Positron AI Lands $875 Million to Challenge Nvidia With Commodity Memory Chips](https://finance.biggo.com/news/e38d0a30-aec1-419a-b671-2d221cbbe94f)

---

## Audio script
วันสิบกันยายน Positron AI ประกาศ Series C 875 ล้านเหรียญ ที่ valuation 5 พันล้าน post money. โครงสร้าง round มีสองชั้น. C 375 ล้าน pre money 3.5 พันล้าน co led โดย NEA Atreides Valor Andra กับ Dylan Patel ที่ SemiAnalysis Capital. C หนึ่ง สูงสุด 500 ล้าน led โดย NEA กับ Jim Clark. Jim Clark ที่เป็น co founder Silicon Graphics และ Netscape.

Bet ที่ contrarian ของ Positron. ใช้ LPDDR5X memory ที่เป็น commodity แทน HBM ที่ Nvidia lock supply ผ่าน SK Hynix Samsung Micron. หลัก architecture คือ inference workload memory bound มากกว่า compute bound. ถ้า design chip ให้ memory bandwidth กับ capacity เยอะ ไม่ต้อง compute density สูงเท่า training chip. Asimov Gen 2 จะมี memory 288 GB ถึง 2,304 GB per chip. เทียบกับ H100 ที่ 80 GB. B200 ที่ 192 GB. capacity ที่กว้างขึ้น แปลว่า model 16 ล้านล้าน parameter รันได้ใน node เดียว ไม่ต้อง shard.

Product ที่วิ่งอยู่แล้ว. Atlas Gen 1 deploy 50 กว่า rack ที่ Oracle Cloud Infrastructure. Customer ยืนยันแล้ว. Parasail. Jump Trading. i3d.net. Positron ยัง cite Anthropic เป็น evaluation partner.

pattern ที่เห็นใน semiconductor stage คือ inference market แยกออกจาก training market. Training ยัง Nvidia dominant. Inference กำลัง fragment ให้ specialist หลายค่าย. Cerebras wafer scale. Groq LPU. SambaNova RDU. Etched Sohu ASIC. และตอนนี้ Positron commodity memory. Reason คือ economics ต่างกัน. Training runs 10K ถึง 100K chip 6 ถึง 12 เดือน. Inference runs 100 ล้าน query ต่อวันตลอดปี. energy กับ memory bandwidth ต่อ query สำคัญกว่า peak FLOPs.

signal ที่คมกว่าคือ Jim Clark กลับมาลงระดับ big check. Clark วางมือจาก tech หลัง Netscape IPO 1995 มา 30 ปี. การกลับมาลง 500 ล้าน anchor round นี้แปลว่า มองเห็น Silicon Graphics moment ในตลาด inference. SGI ยุค 90 ชนะ workstation graphics ด้วย custom silicon ที่ commodity chip ตามไม่ทัน. Positron ทำในทิศตรงกันข้าม. ใช้ commodity memory ไปกด HBM ที่กลายเป็น custom กับ supply locked. playbook ต่างกันแต่ theme เดียวกัน. memory กับ interconnect คือ battleground.

จุดคมที่สาม Oracle เดินเกม supplier diversification เต็มตัว. Oracle Cloud Infrastructure เพิ่งประกาศ 300 พันล้าน deal กับ Nvidia เดือนก่อน. deploy Atlas 50 กว่า rack แปลว่า OCI ไม่ต้องพึ่ง Nvidia ร้อยเปอร์เซ็นต์. AWS Trainium Inferentia. Google TPU. Meta MTIA มี in house silicon อยู่แล้ว. Oracle ที่ไม่มี chip design DNA ต้อง outsource แต่ diversify. Positron เป็น bet แรก. คาดว่าจะตามด้วย Groq หรือ SambaNova ภายในไตรมาส.

สำหรับ builder ที่รัน agent workload. Agent มี characteristic ที่ต่างจาก chatbot. long running session. heavy tool call. repeated context. Positron memory first architecture ตรงกับ agent workload มากกว่า training derived chip. เพราะ agent มี KV cache ที่ยาว มี context ที่ต้อง persist ข้าม turn. Builder ที่วางแผน 6 ถึง 12 เดือนควรถาม cloud vendor ว่ามี Positron Groq SambaNova instance offer ไหม. cost per token ตอน scale อาจถูกกว่า H100 B200 สี่สิบถึงหกสิบเปอร์เซ็นต์ตาม workload.

สำหรับ enterprise ไทย APAC ที่มี data residency requirement ควรถามว่า Oracle Bangkok หรือ Singapore region จะได้ Atlas cluster เมื่อไหร่. น่าจะครึ่งแรกปี 2027. HBM supply crunch ที่เป็น chokepoint ของ Nvidia จะเริ่มถูก question ในบอร์ด Nvidia tax ในตลาด inference กำลังโดนบีบ.
