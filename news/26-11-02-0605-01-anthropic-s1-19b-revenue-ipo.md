---
date: 2026-10-26
slug: anthropic-s1-19b-revenue-ipo
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  An editorial isometric illustration of a stock-ticker tower stamped "ANT /
  NASDAQ" rising out of a Claude-logo pedestal. On the glass façade three
  stacked bold numbers glow: "$19.7B TTM REVENUE", "11,900 CUSTOMERS >$100K",
  "250 CUSTOMERS >$10M". A ribbon unfurls down the side labeled "COMPUTE
  COMMITMENTS $265B – $637B". A bell-ringing podium in the foreground is
  empty with a sign that reads "IPO · THANKSGIVING". Deep navy, cream and
  Anthropic orange palette, high contrast for 200px thumbnails, 1:1 aspect,
  no real human faces.
image: images/26-11-02-0605-01-anthropic-s1-19b-revenue-ipo.png
---

# Anthropic ยื่น S-1 สาธารณะ — $19.7B TTM revenue, 250 ลูกค้าใช้เกิน $10M, มุ่ง Nasdaq ANT ก่อน Thanksgiving

## TL;DR
- Anthropic ยื่น S-1 สาธารณะเมื่อ **26 ต.ค. 2026** ขึ้น Nasdaq ticker **ANT**, คาด IPO ก่อน Thanksgiving ที่ valuation **$1.5T–$2T**
- Revenue 12 เดือนย้อนหลัง **$19.7B** — H1 2026 แตะ $16.3B (จาก $1.16B ปีก่อน), Q3 รายงานกับ investor ที่ **$16.8B** (adjusted profitable)
- Customer tier: **>11,900 ที่ใช้ ≥$100K TTM** (จาก 950 ปีก่อน), **1,900+ ที่ ≥$1M**, **250 ที่ ≥$10M**
- Compute commitment ค่าตั้งแต่ **$265B** (fixed minimum, AlphaSense) ถึง **$637B** (รวม lease ยาว, Tunguz); Implicator cite $518B. ความต่างคือ definition ของ "commitment"
- Risk flag: top 5 ลูกค้า ~25% ของ revenue, model/rate limit "may change" เขียนตรงใน filing

## เกิดอะไรขึ้น

26 ต.ค. 2026 Anthropic ปลด confidential จาก S-1 ที่ยื่น SEC เมื่อ มิ.ย. 2026 แล้วเปิดให้สาธารณะอ่าน — ticker **ANT** บน Nasdaq นำโดย Goldman Sachs + Morgan Stanley. ตัวเลขที่หลุดออกมาเขย่าทั้งตลาด: Revenue H1 2026 **$16.29B** โตจาก $1.16B ของ H1 2025 ประมาณ **14x**. Tomasz Tunguz วิเคราะห์ว่าทั้งปี 2025 → H1 2026 revenue โต **~11x**. Q3 2026 ที่รายงานกับ investor ตามข่าว FT **$16.8B** — จาก $11.5B ใน Q2 แปลว่าเดือน ก.ค.–ก.ย. โตโดดอีกครั้ง

Customer concentration ที่น่าสนใจที่สุด: **250 ลูกค้า run contract ≥$10M/ปี, 1,900 ที่ ≥$1M, 11,900 ที่ ≥$100K** — ตัวเลขหลัง (11,900) โตจาก **950 ปีก่อน** หรือ **~12.5x YoY**. นี่ไม่ใช่ consumer boom อย่างเดียว — คือ enterprise agent spending ที่ไหลเข้า Claude ผ่าน API, Claude Code, Claude Agent SDK. ด้าน loss: non-cash accounting loss **$80.7B** ใน H1 (ส่วนใหญ่จาก fair-value remeasurement ของ convertible preferred), แต่ AlphaSense ชี้ว่า **Q2 Anthropic กำไร operating** — คนละภาพกับ GAAP

ตัวเลข compute commitment ที่สื่อขุดต่างกัน: AlphaSense **$265.6B fixed minimum** (as of 30 มิ.ย.), Daloopa **~$590B** (รวม signed lease), Tunguz **$637B**, Implicator **$518B**. ความต่างคือ: fixed-minimum ที่ต้องจ่ายไม่ว่าใช้ไม่ใช้ vs รวมค่าเช่า data center ที่ลงนามแต่ยังไม่เริ่ม build. ยังไงก็เป็นตัวเลขที่หนักที่สุดในประวัติศาสตร์ private tech IPO. Risk section เขียน flag ชัด: top 5 customer ประมาณ **25% ของ revenue** ในช่วง 9 เดือนถึง ก.ย., และ "no single customer >10%" — แปลว่าดีกว่าร่าง draft S-1 ที่หลุดก่อนหน้า (ซึ่งเขียนว่า 2 customer ~12% คนละ)

## ทำไมสำคัญ

ก่อนหน้านี้ทุกคนเดา Anthropic revenue จาก leak — AlphaSense primer, The Information rumors, podcast transcript. ตอนนี้เรามี **ground truth จาก SEC filing**: Claude ไม่ใช่แค่ consumer chatbot ตีคู่ ChatGPT — แต่คือ **enterprise agent runtime** ที่มีลูกค้า tier 1 จำนวนร้อยที่จ่าย 8-digit USD/year. 250 ลูกค้าระดับ $10M แปลว่า Claude Agent SDK + Claude Code + API มีลูกค้า "enterprise ของ enterprise" ที่น่าจะเป็น investment bank, consultancy, big tech, และ hyperscaler ที่ใช้ Claude เป็น primitive ใน workflow เขาเอง (เรื่อง UBS เมื่อวาน + Cresta ที่เราคุยเช่นกัน คือหลักฐานภาคสนาม)

Compute commitment **$265B–$637B** คือ signal ที่หนักกว่า revenue — Anthropic ล็อค capacity ล่วงหน้ากับ Amazon, Google Cloud, Nvidia มูลค่าเท่ากับ GDP ของ มาเลเซีย 2 เท่า. ถ้าตีความ bear case: นี่คือ bet ที่ต้องการ **revenue 10x จากนี้ใน 5 ปี** ถึงจะคุ้ม. Bull case: supply bottleneck ของ GPU จะทำให้ bank นี้คือ moat — ใครไม่ล็อค capacity ตอนนี้จะไม่มี GPU เพียงพอรัน model generation ถัดไป. OpenAI (ที่คาด IPO 2027) และ xAI ต้องแข่งในสนามเดียวกัน

จุดที่ต้องระวังที่สุด — **"usage limits, rate limits, model and product capabilities may change"** เขียนตรงใน risk factor. ตีความได้ว่า Anthropic กำลังเตรียมใจ public shareholder ว่า Claude อาจเปลี่ยนลักษณะการใช้งานได้ทุกเมื่อ (เช่น ที่เพิ่งเปลี่ยน Max → Ultra, remove 5-hour limit สัปดาห์นี้) และนี่คือการเตือนให้ investor ไม่หวังว่า "unlimited Claude" จะอยู่ตลอด — เป็น setup ให้มีความยืดหยุ่นเชิง policy ในอนาคต

## มุม AI Agent Platform

สำหรับ **builders** ที่สร้างบน Claude Agent SDK, Claude Code, Anthropic MCP: ตัวเลข 250 ลูกค้าเกิน $10M แปลว่า distribution channel มี มีน้ำหนัก มาก — ลูกค้าเขาคือ decision maker ที่ซื้อ platform. ถ้า Honeycomb, Replit, Vercel, Cresta build บน Claude เพราะ reach channel นี้ — ตัวเลขยืนยันเหตุผล. บวกกับ compute commitment แปลว่า capacity planning ของ builder ไม่ต้องห่วง rate-limit ระดับโครงสร้างใน 3 ปีข้างหน้า

สำหรับ **business users / enterprise**: เพิ่งได้ reference point ชัดเจน — คุณไม่ใช่คนแรกที่จ่าย $100K+/ปีกับ Claude. 11,900 บริษัทจ่ายอยู่. CFO ที่ยังถามว่า "เงินนี้ worth มั้ย" ตอบได้ง่ายขึ้นว่า: ถ้า 250 บริษัทจ่าย $10M+ และ Anthropic กำไร operating profit — spending pattern นี้มี market validation. แต่ต้องระวัง concentration risk ย้อนกลับ — ถ้าคุณ bet workflow ทั้งหมดกับ Anthropic และ Anthropic เปลี่ยน model/pricing (ที่ risk factor เขียน) workflow จะเสีย

สำหรับ **ecosystem**: $519B+ compute commitment คือดีลที่หนักพอจะเขย่า hyperscaler economics ของ Amazon (Trainium) และ Google (TPU) — ทั้งคู่คือ landlord ของ Anthropic และ shareholder ขนาดใหญ่. ปี 2027 เราน่าจะเห็น (a) Nvidia launch GPU gen ใหม่ที่ price point ถูกลงเพราะ demand นี้, (b) OpenAI ต้องขุด compute commitment ของตัวเองมาเทียบ ก่อน IPO ปีหน้า, (c) startup agent-infrastructure (vLLM, Modal, Baseten, Fireworks) ต้อง re-pitch ว่าทำไมไม่ล็อคกับ Anthropic อย่างเดียว

## Sources
- [Anthropic S-1: Reconstructed From the Record (Augment Market)](https://augment.market/pulse/anthropics-s-1-reconstructed-from-the-record)
- [Anthropic's S-1 grew eleven-fold (Tom Tunguz)](https://tomtunguz.com/anthropics-s1-grew-eleven-fold/)
- [Anthropic IPO prospectus — $518B compute commitments (Implicator)](https://www.implicator.ai/anthropic-ipo-prospectus-518-billion-compute-commitments/)
- [Anthropic (ANT) company primer on public S-1 (AlphaSense)](https://www.alpha-sense.com/api/html-embed/file-4c88b5685d7120f5cdcdc99545773cca679d25fd-html/)

---

## Audio script
วันจันทร์นี้มีข่าวใหญ่สุดสำหรับคน build บน AI ครับ Anthropic ยื่น S-1 สาธารณะกับ SEC เมื่อ 26 ตุลาคม เตรียมเข้า Nasdaq ด้วย ticker ANT คาดว่า IPO ก่อน Thanksgiving ที่ valuation หนึ่งจุดห้าถึงสองล้านล้านดอลลาร์ Revenue 12 เดือนย้อนหลังอยู่ที่สิบเก้าจุดเจ็ดพันล้านดอลลาร์ ครึ่งปีแรก 2026 แตะสิบหกจุดสามพันล้านโตจากพันล้านของปีก่อนประมาณสิบสี่เท่า ที่สำคัญกว่าตัวเลขรายได้คือ customer breakdown Anthropic มีลูกค้าสองร้อยห้าสิบรายที่ใช้ Claude เกินสิบล้านดอลลาร์ต่อปี มีพันเก้าร้อยรายที่ใช้เกินหนึ่งล้าน และหนึ่งหมื่นหนึ่งพันเก้าร้อยรายที่ใช้เกินแสนดอลลาร์ ตัวเลขหลังโตจากเก้าร้อยห้าสิบของปีก่อนราวสิบสองเท่าครึ่ง นี่คือหลักฐานว่า Claude ไม่ใช่ consumer chatbot แต่คือ enterprise agent runtime ที่มีลูกค้า tier 1 จ่าย eight digit จำนวนร้อยราย ตัวเลข compute commitment สำนักข่าวต่างคิดต่างกันตั้งแต่สองร้อยหกสิบห้าพันล้านถึงหกร้อยสามสิบเจ็ดพันล้านดอลลาร์ ความต่างคือ definition ของ commitment ยังไงก็เป็นดีลที่หนักที่สุดในประวัติศาสตร์ private tech IPO ที่น่าสังเกตคือ risk factor เขียนตรงว่า usage limit และ model capability อาจเปลี่ยนได้ทุกเมื่อ ซึ่งสอดคล้องกับการที่ Anthropic เปลี่ยน Max เป็น Ultra ปลด 5-hour limit สัปดาห์นี้ สำหรับทีมที่ build บน Claude SDK ตัวเลขนี้ตอบคำถาม CFO ว่าทำไมควรลงทุนต่อ แต่ควรระวัง concentration risk ย้อนกลับ ถ้าคุณ bet ทั้ง workflow กับ Anthropic และบริษัทเปลี่ยน policy เร็วเกินไป workflow จะกระทบครับ
