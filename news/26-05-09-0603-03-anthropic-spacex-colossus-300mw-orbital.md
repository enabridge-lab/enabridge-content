---
date: 2026-05-08
slug: anthropic-spacex-colossus-300mw-orbital
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: A bold editorial illustration in deep navy and warm cream — at center, a stylized SpaceX-style rocket silhouette in coral lifts off from a slate data center cluster glowing with teal GPU chip patterns; trailing the rocket, a cream banner reads 'COLOSSUS 1' in big sans-serif letters with the number '300 MW' rendered very large in coral on the lower-right corner. Above the rocket, a small orbital ring icon hints at space, and a tiny cream Anthropic-style starburst Claude mark sits on the rocket nose. Editorial flat-vector style, dramatic spotlight, slate navy + cream + coral + teal palette, no human figures, logos crisp for 200px thumbnail readability.
image: images/26-05-09-0603-03-anthropic-spacex-colossus-300mw-orbital.png
---

# Anthropic เซ็น SpaceX Colossus 1 — 300MW + 220K GPUs ใหม่ + คุย "orbital compute" — Claude Code limits 2x ทันที

## TL;DR
- 6 พ.ค. 2026 Anthropic ประกาศข้อตกลง compute กับ **SpaceX (xAI compute side)** — Anthropic จะใช้ "**all of the compute capacity at Colossus 1**" ของ SpaceX = **300+ MW** + **220,000+ NVIDIA GPUs** ใหม่ภายในเดือนนี้
- ผลลัพธ์ทันทีต่อ product: **Claude Code 5-hour rate limits = 2x** สำหรับ Pro / Max / Team / Enterprise; ปลด peak-hour throttle สำหรับ Pro/Max; **API rate limit Tier-1 จาก 30K → 500K tokens/min** input, 8K → 80K output (ขึ้น **16x** สำหรับ Opus models)
- รวม compute portfolio ของ Anthropic ตอนนี้: AWS **5 GW** + Google/Broadcom **5 GW** (เริ่ม 2027) + Microsoft Azure **$30B** + Fluidstack **$50B US infrastructure** + SpaceX **300MW + orbital interest** — ภาพคือ **multi-cloud hedge** ที่ extreme + เริ่มคุย compute ใน space จริงจัง

## เกิดอะไรขึ้น

วันที่ 6 พ.ค. 2026 Anthropic ปล่อย post "Higher usage limits for Claude and a compute deal with SpaceX" — เซ็น agreement กับ SpaceX ใช้ compute ทั้งหมดที่ **Colossus 1** data center ของ SpaceX ตัวเลขที่ออกมาคือ "**more than 300 megawatts of new capacity**" และ "**over 220,000 NVIDIA GPUs**" ภายในเดือนนี้ — ซึ่งเป็น scale ใหญ่กว่า data center ของ Anthropic อันใดอันหนึ่งที่มีอยู่ก่อนหน้า สิ่งที่น่าสังเกตคือ "Colossus 1" เป็นชื่อเดิมของคลัสเตอร์ที่ xAI (Elon บริษัทเดียวกับ SpaceX) ใช้ฝึก Grok — มี report ว่า SpaceX และ xAI re-organize compute asset และ Colossus 1 เก่าถูกย้าย ownership/lease ออกมาเป็น standalone data center business

ผลกระทบต่อ product **เกิดทันที** Anthropic ใช้โอกาสนี้ปรับ rate limit ทุกตัวพร้อมกัน: **Claude Code** 5-hour usage limit สำหรับ Pro, Max, Team, และ seat-based Enterprise plans ถูก **double** ทุก tier; peak-hour throttle ที่ Pro/Max เคยโดนช่วงเวลาคนใช้เยอะ ถูกปลดทั้งหมด; **API rate limit Tier-1** สำหรับ Opus models เพิ่มจาก 30,000 → **500,000 input tokens/min** (16x) และ 8,000 → **80,000 output tokens/min** (10x) ตัวเลขนี้สำหรับ enterprise dev ที่รัน agent บน Claude Opus หมายความว่า workload ที่เคยต้อง throttle หรือ batch overnight สามารถรัน real-time ใน production ได้ — agent ที่ต้อง reason ผ่าน 1M context window จะไม่ติด rate limit ตอน peak อีก

ที่เป็น signal ใหญ่กว่า rate limit คือประโยคปิด post: Anthropic บอกว่า "**expressed interest in partnering with SpaceX to develop multiple gigawatts of orbital AI compute capacity**" — orbital data center จริง ๆ ที่อยู่ในอวกาศ ใช้ solar 24/7 + ระบายความร้อนผ่าน radiative cooling ลงฝั่งเย็นของยาน นี่ไม่ใช่ blue-sky พูด — SpaceX มี Starlink Gen3 satellite ที่มี compute payload ที่ใหญ่ขึ้นมากแล้ว และมี cost-to-orbit ($1,500/kg ผ่าน Starship V3) ที่ทำให้ data center ขนาด GW-class ใน LEO เริ่มมี TCO ที่แข่งกับ data center บนโลกในแถบที่ไฟ + cooling แพงได้ Bezos Project Prometheus ของ Amazon ก็ pitch concept คล้าย ๆ กันเดือนก่อน

## ทำไมสำคัญ

ภาพรวมของ Anthropic compute portfolio ตอนนี้คือ AWS 5 GW + Google/Broadcom 5 GW + Microsoft Azure $30B + Fluidstack $50B + SpaceX 300MW = **multi-cloud hedge ระดับ extreme** OpenAI กับ Microsoft ผูกกันแน่นปี 2023 แต่พอ 2025-2026 ก็ต้อง diversify ไป Bedrock (ดู brief #01) Anthropic กลับเดินคนละทาง — diversify ตั้งแต่วันแรก, แต่ละ cloud คือ insurance policy ต่อ **single point of failure ของ supply chain compute** ปี 2026 ทุกคนยอมรับว่า frontier lab ไม่ใช่ "ใครเทรนเก่งกว่า" แต่เป็น "ใครหา energy + chip ได้ก่อน" — และ SpaceX/xAI compute ที่เคยเป็น zero-sum (ฝึก Grok แข่งกับ Claude) กลายเป็น marketplace asset ที่ขายได้

อีกประเด็นคือ orbital compute ที่ Anthropic + SpaceX พูดถึงเปิดเผย เป็น signal ว่า trajectory ของ AI infrastructure อีก 18-24 เดือนจะมี frontier ใหม่ — ตอนนี้ทุก state, county ในอเมริกา block data center เพราะ grid + water + community pushback Texas, Virginia, Iowa เริ่มถึง limit ของ permit ที่ออกได้ orbital compute ลบ constraint นั้น + เป็น narrative ที่ขาย politicly ง่าย ("ไม่กิน grid อเมริกา, ไม่ใช้น้ำเมือง") ภายใน 2027 อาจมี frontier model ที่อย่างน้อยส่วน inference run บน orbital cluster จริง — ไม่ใช่ marketing เกินไป

ที่ controversial: deal กับ SpaceX มาในช่วงที่ Anthropic positioning ตัวเป็น "safety-first AI" และ Elon ตัวเอง split จาก OpenAI เพราะเรื่อง safety; การที่ Anthropic เลือก compute จาก Elon-affiliated entity โดยเปิดเผย เป็น signal ว่า **scarcity ของ compute ชนะ political alignment** ใน 2026 ตลาด compute จะ commoditize ใน behavior คล้าย oil ใน 1973 — บริษัทใหญ่ซื้อจาก source ที่หาได้ ไม่ดู supplier alignment

## มุม OpenBridge

ไม่ direct เกี่ยวกับ OpenBridge แต่มี adjacent insight สามเรื่อง **(1) Claude Code rate limit 2x + Tier-1 API 16x = lower-friction integration testing** — dev ของ OpenBridge ที่ใช้ Claude Code ทดสอบ MCP connector หรือ build connector ใหม่ จะรัน iteration ได้เยอะขึ้นใน window เดียว สำหรับ team เล็กที่ Claude Code เป็น primary tool การ unblock peak-hour throttle = engineering velocity เพิ่ม 20-30% ในเดือนถัด — Yoh ควรพิจารณา upgrade plan ถ้ายังเป็น Pro

**(2) ลูกค้า Fortune 500 จะเริ่ม commit volume กับ Claude มากขึ้นเพราะ API rate ปลดล็อก** — workload agent ที่ pause เพราะรอ rate limit window จะ unlock; OpenBridge connector ที่อยู่ใต้ agent เหล่านี้จะถูกเรียกถี่ขึ้น 10-20x ในบางเคส; capacity planning ของ OpenBridge MCP server ต้องเตรียมรับ — connector ที่ออกแบบไว้สำหรับ "agent เรียกชั่วโมงละ 10 ครั้ง" จะกลายเป็น "agent เรียกนาทีละ 10 ครั้ง" — load testing ใหม่จำเป็น

**(3) compute geopolitics จะ shape product roadmap ของลูกค้า** — บริษัท Thai/SEA ที่ใช้ Claude ผ่าน API จะเริ่มเห็น regional latency ปรับ (Anthropic อาจ deploy capacity ใน region ใหม่หลังได้ Colossus 1) OpenBridge ควรเตรียม region-aware routing ใน MCP layer — ลูกค้าอาจอยากให้ MCP call ที่ไป Anthropic region ใกล้สุด, fallback ไปอีก region ถ้ามี throttle; เป็น value-add ที่ raw Anthropic SDK ไม่มี

## Sources
- [Higher usage limits for Claude and a compute deal with SpaceX | Anthropic](https://www.anthropic.com/news/higher-limits-spacex)
- [Anthropic, SpaceX announce compute deal that includes space development | CNBC](https://www.cnbc.com/2026/05/06/anthropic-spacex-data-center-capacity.html)
- [Anthropic, SpaceX Sign Deal to Boost AI Computing Power for Claude Software | Bloomberg](https://www.bloomberg.com/news/articles/2026-05-06/anthropic-inks-computing-deal-with-spacex-to-meet-ai-demand)
- [Anthropic taps SpaceX Colossus 1 to raise Claude limits | Let's Data Science](https://letsdatascience.com/news/anthropic-taps-spacex-colossus-1-to-raise-claude-limits-d4ddcbe0)
- [Anthropic hikes Claude usage limits for paid users post SpaceX compute deal | Business Standard](https://www.business-standard.com/technology/tech-news/anthropic-claude-usage-rate-limit-increased-paid-users-spacex-compute-deal-new-limits-126050700994_1.html)

---

## Audio script
สวัสดีครับโย Anthropic ปล่อยข่าว 6 พ.ค. ที่เปลี่ยนทั้ง compute landscape และ Claude Code product เซ็นข้อตกลงกับ SpaceX ใช้ compute ทั้งหมดที่ Colossus 1 ของ SpaceX มากกว่า 300 เมกะวัตต์ มากกว่า 220000 GPU ของ NVIDIA ใหม่ภายในเดือนนี้ ที่น่าสนใจคือ Colossus 1 เป็นชื่อ cluster เดิมที่ xAI ใช้ฝึก Grok ตอนนี้ถูกย้าย ownership ออกมาขายเป็น compute asset

ผลทันทีต่อ product Claude Code 5 hour limit ของทุก tier double ปลด peak hour throttle Pro Max API Tier 1 Opus เพิ่ม input จาก 30000 เป็น 500000 tokens per minute output จาก 8000 เป็น 80000 ขึ้น 16 เท่ากับ 10 เท่า workload agent ที่ต้องรอ rate limit ตอน peak รัน real time ได้

signal ใหญ่กว่า rate limit คือ Anthropic บอกว่าสนใจร่วมพัฒนา orbital AI compute หลาย gigawatt กับ SpaceX จริง ไม่ใช่ blue sky talk เพราะ Starlink Gen 3 มี compute payload Starship V3 cost to orbit 1500 ดอลลาร์ต่อ kg ทำให้ TCO data center ใน LEO แข่งกับโลกได้ในที่ที่ไฟแพง

ภาพ portfolio Anthropic ตอนนี้ AWS 5 กิกะวัตต์ Google 5 กิกะวัตต์ Microsoft 30 พันล้าน Fluidstack 50 พันล้าน SpaceX 300 เมกะวัตต์ multi cloud hedge extreme ระดับที่ scarcity compute ชนะ political alignment การที่ Anthropic safety first เลือก compute จาก Elon entity เปิดเผยเป็น signal ว่า compute จะ commoditize เหมือน oil 1973

มุม OpenBridge adjacent หนึ่ง Claude Code limits 2x dev velocity เพิ่ม 20 ถึง 30 เปอร์เซ็นต์ Yoh ควรพิจารณา upgrade plan สอง ลูกค้า Fortune 500 commit volume Claude มากขึ้น MCP connector จะถูกเรียกถี่ขึ้น 10 ถึง 20 เท่าในบางเคส load testing ใหม่จำเป็น สาม region aware routing ใน MCP layer เป็น value add ที่ raw SDK ไม่มี ลูกค้าอยากให้เลือก region ใกล้ fallback ถ้า throttle ครับ
