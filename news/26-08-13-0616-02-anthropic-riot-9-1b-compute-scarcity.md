---
date: 2026-08-13
slug: anthropic-riot-9-1b-compute-scarcity
topic: use-case
reading_time_min: 3
sources: 3
image_prompt: |
  Editorial isometric hero image of a Texas oil-rig-style bitcoin mining
  facility with towers being repainted from orange BTC logos to a purple
  "Claude" wordmark. Overlay a giant scoreboard reading "$9.1B / 20 YEARS
  / 191 MW", plus a smaller banner "THROUGH JUNE 2048". Grid power lines
  glow purple leading toward the mine. High contrast, 1:1 aspect, no real
  human faces, text sized to be readable at 200px thumbnail.
image: images/26-08-13-0616-02-anthropic-riot-9-1b-compute-scarcity.png
---

# Anthropic ล็อกดีล $9.1B / 20 ปี กับ Riot Platforms — บิตคอยน์ไมเนอร์กลายเป็นเจ้าของที่ดินให้ Claude

## TL;DR
- Anthropic เซ็นสัญญา 20 ปี มูลค่า **$9.1 พันล้าน** กับ Riot Platforms เช่า 191 MW ที่ Rockdale, Texas ผ่านมิถุนายน 2048 — extension อีก 2 รอบ 5 ปี รวมได้ถึง **$16.1B**
- Riot ขึ้นราคาหุ้น +25% after hours — พลิกจาก bitcoin miner เป็น AI infra landlord
- Anthropic รวมดีลกับ Volta ($10B) และ xAI ($45B compute purchase ในเดือน May) แสดง pattern การ lock power capacity ระยะยาวเพื่อรองรับ Claude scaling

## เกิดอะไรขึ้น
วันที่ 11 สิงหาคม 2026 Riot Platforms เปิดเผยการเซ็นสัญญา 20 ปีมูลค่า 9.1 พันล้านดอลลาร์กับ Anthropic โดย Anthropic จะเช่ากำลัง compute 191 เมกะวัตต์จาก campus ของ Riot ที่ Rockdale รัฐเท็กซัส สัญญาครอบคลุมถึงเดือนมิถุนายน 2048 และมี option ต่ออีก 2 รอบ ๆ ละ 5 ปี ซึ่งจะดันมูลค่ารวมขึ้นเป็นราว 16.1 พันล้านดอลลาร์

Riot จะทยอยส่งมอบ capacity เป็น phase — ถึง 96 เมกะวัตต์ภายในธันวาคม 2027 และเต็ม 191 เมกะวัตต์ภายในมิถุนายน 2028 หุ้น Riot Platforms กระโดดขึ้น 25% ในการซื้อขาย after hours หลังข่าวออก สะท้อนตลาดที่มองว่าธุรกิจ bitcoin mining ที่เจอทั้งราคาเหรียญกด, competition สูง, และผลของ Bitcoin halving รอบล่าสุด — กลายเป็นธุรกิจเช่าที่ดินและไฟฟ้าให้ AI lab ที่มี margin แน่นอนกว่ามาก

ที่น่าสนใจกว่านั้นคือ Anthropic ไม่ใช่ทำดีลเดียว — ก่อนหน้านี้บริษัทเซ็นดีล 10 พันล้านดอลลาร์กับ Volta Infra Holdings และในเดือนพฤษภาคม 2026 ทำดีลซื้อ compute capacity ราว 45 พันล้านดอลลาร์จาก xAI ของ Elon Musk แสดงว่า Anthropic กำลัง lock supply chain ทั้ง grid-connected power และ silicon capacity ให้ครอบคลุม Claude generation ต่อ ๆ ไปทั้งชุด

ERCOT (Electric Reliability Council of Texas) ปีนี้เริ่มเข้มขึ้นกับ interconnection request ใหม่จาก data center — ยิ่งทำให้ capacity ที่มีสายส่งพร้อมอยู่แล้ว (เช่นที่ Riot ครองอยู่) แพงและหายากขึ้น Anthropic รู้ดีจึงยอมล็อก 20 ปี

## ทำไมสำคัญ
ดีลนี้ไม่ใช่แค่ big number — มันบอก 3 อย่างพร้อมกัน หนึ่ง compute เป็น bottleneck ระดับที่ frontier lab ยอมล็อกสัญญา 22 ปีกับ counterparty ที่เพิ่งเปลี่ยนธุรกิจ นั่นแปลว่าคาดการณ์ demand สำหรับ inference ของ Claude ในปี 2030+ สูงมากพอที่จะรอง 191 MW ตลอด

สอง power infrastructure จริง ๆ ในสหรัฐฯ กำลังกลายเป็น moat มากกว่า chip แม้แต่ Nvidia GPU ก็หาซื้อได้ถ้ามีเงิน แต่ substation, transformer, และ interconnection agreement ที่มีอยู่แล้วนั้น regulator ใหม่จะไม่ให้อย่างง่ายอีกต่อไป การที่ bitcoin miner ที่นั่งบน grid access อยู่แล้วเข้ามาเป็น player — เปลี่ยน map ของ AI infrastructure โดยสิ้นเชิง

สาม ต้นทุน compute ต่อ token ของ Anthropic ยังคงถูกลอง — ถ้า Claude Sonnet 5 หรือ Opus 5 ที่ดันตลาด agent workload ยังต้อง scale ด้วย hardware ที่ใช้ไฟ 191 MW เดียว บริษัทที่แข่งกับ Anthropic ในตลาด agent platform ต้องมี answer ว่าจะ compete กับ margin structure นี้ยังไง

## มุม AI Agent Platform
**Builders** ที่ build บน Claude API: ข่าวดีคือ Anthropic กำลัง lock capacity ระยะยาว = supply-side risk ต่ำลง ข่าวไม่ดีคือ pricing power ของ Anthropic จะยิ่งแข็ง เพราะไม่ต้องแข่งกับ hyperscaler เพื่อแย่ง GPU ในตลาด spot อีกต่อไป และการ commit 20 ปีสะท้อนว่า Anthropic คาดการณ์ demand ของ agent workload จะแตะ ceiling ปัจจุบันภายในเวลาไม่นาน

**Users / business** ที่ deploy Claude ใน production: ให้ประเมิน multi-cloud / multi-model routing ให้จริงจัง — ไม่ใช่เพราะ Claude จะไม่มีของขาย แต่เพราะ tier ราคาอาจถูก re-price เมื่อ Anthropic ครองประชากร inference มากพอ ตอนนี้เป็นช่วงเจรจา rate card ที่ดีก่อน demand curve ชนกำแพง

**Ecosystem**: bitcoin miner ที่ยัง scale ไม่ทัน AI shift — Marathon, Cipher, Core Scientific — น่าจับตาว่าใครจะเป็นเจ้าถัดไปที่ frontier lab เข้าไปเซ็น long-term lease นักลงทุน infra จะเริ่มมองที่ดินและสายส่งเป็น asset class มากกว่า ASIC farm

## Sources
- [Anthropic Strikes $9 Billion Computing Deal With Riot Platforms (Bloomberg)](https://www.bloomberg.com/news/articles/2026-08-11/anthropic-strikes-9-billion-deal-with-cloud-computing-firm-riot)
- [Riot Platforms strikes deal with Anthropic as bitcoin miners shift focus to AI infrastructure (CNBC)](https://www.cnbc.com/2026/08/11/riot-platforms-signs-anthropic-deal-as-miners-shift-to-ai-infrastructure-.html)
- [Anthropic signs $9.1 billion data center deal with Riot Platforms (Quartz)](https://qz.com/anthropic-riot-platforms-data-center-deal-9-billion-081126)

---

## Audio script
เมื่อวานนี้ Riot Platforms ประกาศเซ็นสัญญา 20 ปี มูลค่า 9.1 พันล้านดอลลาร์กับ Anthropic โดย Anthropic จะเช่ากำลังไฟ 191 เมกะวัตต์จาก campus ของ Riot ที่ Rockdale เท็กซัส สัญญาครอบคลุมถึงมิถุนายน 2048 และถ้ารวม extension อีกสองรอบ รอบละ 5 ปี มูลค่ารวมจะขึ้นเป็นราว 16.1 พันล้านดอลลาร์ หุ้น Riot กระโดดขึ้น 25% ใน after hours ทันที

ที่น่าสนใจคือ Anthropic ไม่ได้ทำดีลเดียว ก่อนหน้านี้เพิ่งเซ็นกับ Volta อีก 10 พันล้านดอลลาร์ และในเดือนพฤษภาคมทำดีลซื้อ compute ราว 45 พันล้านดอลลาร์จาก xAI ของ Elon Musk แสดงว่าบริษัทกำลัง lock ทั้ง supply chain ของไฟฟ้าและ silicon ยาวไปถึงยุค Claude Opus 6 หรือ 7 เลย

จุดที่คนสร้าง agent platform ต้องคิดต่อคือ compute กำลังกลายเป็น moat มากกว่า chip เพราะ ERCOT ในเท็กซัสเริ่มเข้มขึ้นกับ data center ใหม่ ที่ดินที่มีสายส่งพร้อมอยู่แล้วอย่างของ bitcoin miner กลายเป็น asset ที่ frontier lab ยอมจ่ายแพงเพื่อยึด

สำหรับคนที่ deploy Claude ใน production คำถามที่ต้องถามตอนนี้คือ pricing tier ระยะยาวจะเป็นยังไง เพราะเมื่อ Anthropic ครอง supply มากพอ ราคาต่อ token อาจถูก re-price ตอนนี้เป็นช่วงเจรจา rate card ที่ดีก่อน demand curve ชนกำแพงครับ
