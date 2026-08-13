---
date: 2026-08-14
slug: anthropic-first-profit-10-9b-quarter
topic: use-case
reading_time_min: 4
sources: 3
image_prompt: |
  Editorial isometric illustration of a giant open ledger book at center; on the
  left page a plunging bar chart labeled "COMPUTE COST 71¢ → 56¢", on the right
  page a rising bar chart labeled "REVENUE $4.8B → $10.9B". Above the ledger a
  glowing pennant reads "FIRST PROFIT $559M" with an Anthropic wordmark bottom
  right. Small silhouettes of enterprise buyers queue at the ledger. High
  contrast, 1:1 aspect, no real human faces, editorial magazine style.
image: images/26-08-14-0630-01-anthropic-first-profit-10-9b-quarter.png
---

# Anthropic ทำกำไรไตรมาสแรก — Q2 รายได้ $10.9B, กำไรจากปฏิบัติการ $559M, เร็วกว่าแผน 2 ปี

## TL;DR
- Anthropic ปิด Q2 2026 ที่รายได้ **$10.9 พันล้าน** โต 130% จาก $4.8B ใน Q1 พร้อม operating profit **$559 ล้าน** — กำไรไตรมาสแรกในประวัติศาสตร์บริษัท
- ต้นทุน compute ต่อ 1 ดอลลาร์รายได้ลดจาก **71 เซนต์ → 56 เซนต์** ในไตรมาสเดียว ขับเคลื่อนโดย Claude Code ที่ enterprise รับใช้เต็มตัว
- Anthropic เตือน investor เองว่า Q3/Q4 อาจกลับเป็นขาดทุนจาก capex compute — และมี "SpaceX compute discount" ที่ทำให้ตัวเลข Q2 ดูดีเกินจริง

## เกิดอะไรขึ้น
วันที่ 13 สิงหาคม 2026 Anthropic แจ้ง investor ว่า Q2 ที่จบไปทำรายได้ 10.9 พันล้านดอลลาร์ โต 130% จาก 4.8 พันล้านใน Q1 และทำ operating profit ครั้งแรกที่ 559 ล้านดอลลาร์ — เร็วกว่า internal roadmap ที่วางไว้ประมาณสองปี

ตัวเลขที่น่าสนใจกว่ารายได้คือ margin: cost ของ compute ต่อ 1 ดอลลาร์รายได้ลดจาก 71 เซนต์ใน Q1 เหลือ 56 เซนต์ใน Q2 — เป็นการดีดขึ้นของ gross margin ระดับที่บริษัท SaaS ปกติใช้เวลาหลายปีถึงจะทำได้ ตัวขับเคลื่อนหลักคือ Claude Code ที่กลายเป็น product ที่ enterprise ซื้อจริงจัง กับดีล compute ยาว 20 ปี $9.1B กับ Riot Platforms ที่เพิ่งปิดสัปดาห์ก่อน

Anthropic เปิดว่าตอนนี้มี enterprise account มากกว่า 1,000 ราย ที่แต่ละรายจ่ายเกิน $1M/ปี — เป็นสัญญาณว่า Claude ไม่ใช่ dev tool ที่ engineer แอบใช้ต่อไปแล้ว แต่กลายเป็น line item บน enterprise procurement ที่ต้องมี master service agreement, security review, และ business owner

แต่บริษัทเตือน investor ตรง ๆ ว่าเลขนี้อาจไม่ยั่งยืน — Q3 กับ Q4 น่าจะขาดทุนอีกครั้ง เพราะ capex ที่จองไว้กับดีล compute ปลายปี 2026 และตลอด 2027 จะกลับมา hit P&L และ commentator หลายรายชี้ว่า "SpaceX compute discount" (ดีล Anthropic + xAI ที่แชร์ colocation) ช่วยกดต้นทุน Q2 ต่ำเกินความเป็นจริงในระยะยาว

## ทำไมสำคัญ
นี่คือครั้งแรกในประวัติศาสตร์ frontier lab ที่บริษัทใดบริษัทหนึ่งใน Big-4 (OpenAI, Anthropic, Google DeepMind, xAI) แสดงกำไร operating เป็นบวก และมันเกิดขึ้นเร็วกว่าที่แม้แต่ทีมภายในเชื่อ ในตลาดที่ narrative หลัก 3 ปีที่ผ่านมาคือ "AI ยังไม่ทำกำไร" ตัวเลข $559M นี้จะถูกใช้เป็นข้ออ้างใน pitch deck ของ VC ทุกรอบใน 12 เดือนข้างหน้า

Pattern ที่น่าสนใจกว่ากำไร: gross margin จะเดินหน้าได้เพราะ Claude Code เป็น product ที่ tie ตรงกับ workflow ที่ enterprise ยอมจ่าย per-seat + per-token — ต่างจาก consumer chatbot ที่ margin บาง Anthropic เพิ่งประกาศขึ้นราคา Claude Sonnet 5 จาก $2 → $3/M ตั้งแต่ 31 สิงหาคม ซึ่งเป็นการแสดง pricing power ที่ enterprise vendor ปกติจะพยายามไม่ใช้ในปีแรกของ product cycle

Signal ต่อจากนี้: ถ้า OpenAI ที่กำลังจะยื่น S-1 (ตามข่าว) โชว์ margin ที่แย่กว่านี้ นักลงทุนสาธารณะจะเริ่มถามคำถามยาก ๆ ว่าใครใน Big-4 เป็น "structural winner" ตัวจริง และดีลใหญ่ ๆ อย่าง Anthropic acquires Decart AI ($6B ตามข่าว) จะถูกอ่านเป็นการใช้ margin ที่ทำได้ไปซื้อ inference edge เพื่อ lock lead

## มุม AI Agent Platform
**Builders** ที่สร้าง agent framework บน Claude: การขึ้นราคา + margin ที่ Anthropic โชว์ = signal ว่า vendor ไม่ต้องแข่งราคาลงต่ำอีกต่อไป ถ้า agent ของคุณ tie กับ Claude Sonnet 5 ให้ recompute unit economics ใหม่ตอนนี้ก่อน 31 สิงหาคมเข้ามา — และคิดเผื่อว่าราคาจะขึ้นอีกในรอบต่อไป

**Users / business** ที่ deploy Claude ใน workflow: 1,000+ accounts ที่จ่ายเกิน $1M/ปี เป็น proof ที่ procurement ต้องเชื่อได้แล้ว — แต่การพึ่งพา Anthropic ในทุก tier (API + Claude Code + agent SDK) เพิ่ม concentration risk ให้ CFO ตั้งคำถาม ควรมีแผน multi-model routing (คู่กับ Grok 4.6 หรือ GPT-5.6) เอาไว้ในสถาปัตยกรรม

**Ecosystem**: คนที่ได้ประโยชน์รอบสอง = Cursor, Windsurf, และทุก IDE ที่ integrate Claude Code — เพราะจำนวน seat ที่ enterprise ยอมซื้อมันขยับเป็นล้าน คนที่เสีย = model vendor ระดับกลาง (Mistral, Cohere, open-source hosted) ที่ต้องแข่งกับ Claude ที่ตอนนี้มีทั้ง scale, margin, และ enterprise footprint

## Sources
- [Anthropic Projects 559 Million Q2 Operating Profit on 10.9B Revenue (Let's Data Science)](https://letsdatascience.com/blog/anthropic-first-operating-profit-q2-2026-559-million)
- [Anthropic First Profit 2026 — $10.9B Q2 Revenue, $559M Operating Income (AIToolsRecap)](https://aitoolsrecap.com/Blog/anthropic-first-profit-2026-revenue-breakdown)
- [Anthropic Statistics 2026: Revenue, Valuation, Funding & Growth Data (Axis Intelligence)](https://axis-intelligence.com/anthropic-statistics/)

---

## Audio script
เมื่อวานนี้วันที่ 13 สิงหาคม Anthropic แจ้งนักลงทุนว่า Q2 2026 ทำรายได้ 10.9 พันล้านดอลลาร์ โต 130 เปอร์เซ็นต์จากไตรมาสก่อน และมี operating profit ครั้งแรก 559 ล้านดอลลาร์ เร็วกว่าแผนภายในของบริษัทถึงสองปี

ตัวเลขที่น่าสนใจกว่ารายได้คือ margin ต้นทุน compute ต่อรายได้ 1 ดอลลาร์ลดจาก 71 เซนต์ใน Q1 เหลือ 56 เซนต์ใน Q2 ตัวขับเคลื่อนหลักคือ Claude Code ที่ enterprise ซื้อจริงจัง ตอนนี้ Anthropic มีลูกค้า enterprise มากกว่า 1,000 บริษัทที่จ่ายเกิน 1 ล้านดอลลาร์ต่อปี แปลว่า Claude ไม่ใช่ dev tool ที่ engineer แอบใช้อีกต่อไป แต่กลายเป็น line item บน enterprise procurement ที่มี business owner จริง

แต่บริษัทเตือน investor ตรง ๆ ว่า Q3 และ Q4 น่าจะกลับเป็นขาดทุน เพราะ capex compute ที่จองไว้ปลายปี และมี SpaceX compute discount ที่ช่วยกดต้นทุน Q2 ต่ำเกินจริง

สำหรับคนสร้าง agent บน Claude เรื่องนี้แปลว่า Anthropic ไม่ต้องแข่งราคาลงต่ำอีกแล้ว เขากล้าขึ้นราคา Sonnet 5 จาก 2 เป็น 3 ดอลลาร์ต่อล้าน token สิ้นเดือนนี้ ถ้า agent ของคุณ tie กับ Claude ให้คำนวณ unit economics ใหม่ก่อนวันที่ 31 สิงหาคม และคิดเผื่อว่าราคาจะขึ้นอีกในรอบต่อไปครับ
