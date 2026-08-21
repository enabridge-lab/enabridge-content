---
date: 2026-08-22
slug: cognition-devin-40b-talks-1b-arr-coding-agent
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  An editorial illustration of a colossal robotic architect standing over a
  city of code, holding a giant blueprint labeled "DEVIN". Three glowing
  headline numbers stacked in the sky: "$40B", "$1B ARR TARGET",
  "10X ENTERPRISE USAGE". A tiny Mercedes star, NASA meatball, and Goldman
  Sachs seal are etched on the base pedestal. Editorial isometric style,
  midnight-blue backdrop, cyan and amber accents, dramatic rim lighting.
  1:1 aspect, no real human faces.
image: images/26-08-22-0609-01-cognition-devin-40b-talks-1b-arr-coding-agent.png
---

# Cognition คุยรอบใหม่ที่ $40B — Devin ตั้ง target $1B ARR หลังพุ่งจาก $492M ใน 3 เดือน, Mercedes/NASA/Goldman deploy จริง

## TL;DR
- Cognition (Devin) คุยรอบใหม่ที่ valuation ≥ $40B — ขึ้นจาก $26B post-money เมื่อพ.ค. 2026 (3 เดือนก่อน), Bloomberg รายงาน 12 ส.ค.
- ARR $492M ตอนปิดรอบ $1B ล่าสุด, ตั้ง target $1B run-rate ก่อนปิดรอบใหม่ — enterprise usage โต 10x ตั้งแต่ต้นปี 2026
- Mercedes-Benz, NASA, Goldman Sachs, Santander deploy Devin ทำ production work จริง (migration, updating legacy code) — ไม่ใช่ side project

## เกิดอะไรขึ้น

Bloomberg รายงานเมื่อ 12 ส.ค. ว่า Cognition — บริษัทเจ้าของ Devin ซึ่งเป็น autonomous coding agent — กำลังคุยรอบ funding ใหม่ที่ valuation อย่างน้อย $40B. รอบก่อนหน้าที่ปิดเมื่อ 27 พ.ค. 2026 อยู่ที่ $1B raise บน $25B pre-money ($26B post-money) โดย Founders Fund นำ. ถ้าปิดที่ $40B จริง valuation จะขึ้น ~54% ใน 3 เดือน — จังหวะที่เร็วผิดปกติแม้กระทั่งในตลาด AI ที่ร้อนแรงตอนนี้

ตัวเลข run-rate เป็นตัวขับ: ตอนปิดรอบพ.ค. ARR อยู่ที่ $492M โดย Scott Wu (CEO) บอก TechCrunch ว่า enterprise customer โตการใช้ Devin 50% MoM ใน 6 เดือนก่อนหน้า. Bloomberg บอกว่ารอบใหม่ต้องการเห็น $1B ARR run-rate ก่อนปิด — ถ้าคิดจากเส้นทางเดิม 50% MoM, ตัวเลขนั้นเป็นจริงในไตรมาสถัดไป

Enterprise footprint เป็นสิ่งที่ทำให้ตัวเลขไม่ใช่ hype: Mercedes-Benz ใช้ Devin migrate legacy codebase, NASA รันในโปรเจกต์ mission-critical, Goldman Sachs และ Santander deploy บน production. Enterprise ARR โต >30% ในแค่ 7 สัปดาห์หลังปิดรอบพ.ค. และ enterprise usage รวมโต 10x นับจากต้นปี 2026. การซื้อ Windsurf ที่ผ่านมาเปลี่ยน customer mix จาก bottom-up developer subscription ไปเป็น multi-seat enterprise contract ที่มี ACV สูงกว่ามาก

## ทำไมสำคัญ

Story นี้ไม่ใช่แค่ "startup อีกเจ้าที่ระดมทุนได้เยอะ" — มันคือ signal ว่า autonomous coding agent เข้าสู่ phase ที่ enterprise ยอมจ่ายเงินให้ทำงานจริงบน production codebase, ไม่ใช่ pilot. เมื่อ Goldman Sachs และ Mercedes ยอมให้ agent แตะ codebase ที่มี regulatory risk สูง แปลว่ามันผ่าน internal audit + risk review — เกณฑ์ที่ tools อย่าง GitHub Copilot ยังไม่ค่อยเจอในระดับนั้นเพราะ Copilot ยังอยู่ในบทบาท assistant, ไม่ใช่ autonomous worker

Valuation ที่ขึ้นเร็วขนาดนี้เทียบกับ Anysphere (Cursor) ที่ SpaceX ซื้อไป $60B เมื่อสัปดาห์ก่อน สะท้อนว่านักลงทุนกำลังแยกเซกเมนต์ "coding tool" ออกจาก "coding agent" อย่างชัดเจน: tool ที่มนุษย์ยังอยู่ใน loop (Cursor) กับ agent ที่มนุษย์เพียง review output (Devin) มีเส้นทาง revenue ต่างกัน — agent scale ตาม ticket, tool scale ตาม seat. ตัวเลข 50% MoM ของ Devin สะท้อน enterprise ยอมจ่ายตามปริมาณงานที่ agent ทำ ไม่ใช่ตาม developer ที่ใช้

## มุม AI Agent Platform

**Builders** ที่กำลังสร้าง coding agent framework (OpenHands, SWE-Agent, Cline, Aider): pricing model ของ Cognition กำลังเป็น template — usage-based ที่คิดจาก successful task completion ไม่ใช่ token consumption. ถ้า framework ของคุณยังบังคับ enterprise ให้ต้องซื้อ seat ต่อ developer, จะเสียเปรียบเพราะ enterprise คิด ROI ต่อ ticket ไม่ใช่ต่อ user. **Businesses** ที่ deploy coding agent: signal จาก Mercedes/NASA/Goldman คือมันผ่าน audit ได้ — ต้อง benchmark internal ต่อ Devin ก่อนสิ้นปี, migration project ที่วางแผนจะทำใน 6 เดือนตอนนี้ agent ทำได้ใน 6 สัปดาห์. **Ecosystem**: SpaceX ซื้อ Cursor $60B, Cognition คุย $40B — พฤติกรรม M&A กำลังบอกว่า coding infra กลายเป็น strategic asset ระดับเดียวกับ cloud region. ทุก big tech ต้องมี coding-agent stack ของตัวเอง ไม่งั้นเสีย developer mindshare ให้คู่แข่ง

## Sources
- [AI coding startup Cognition reportedly already in talks to raise at $40B valuation (TechCrunch)](https://techcrunch.com/2026/08/12/ai-coding-startup-cognition-reportedly-already-in-talks-to-raise-at-40b-valuation/)
- [AI Startup Cognition in New Funding Talks at $40 Billion Value (Bloomberg)](https://www.bloomberg.com/news/articles/2026-08-12/ai-startup-cognition-in-new-funding-talks-at-40-billion-value)
- [Cognition Seeks Funding at a Valuation of at Least $40 Billion as Devin Revenue Target Reaches $1 Billion (Mezha)](https://mezha.net/eng/bukvy/a24cb53d_cognition_seeks_funding/)
- [How Does Cognition Make Money: Devin Pricing, Windsurf, and $492M ARR (Value Add VC)](https://valueaddvc.com/blog/how-does-cognition-make-money-devin-pricing-windsurf-enterprise-and-the-492m-arr-breakdown)
- [AI coding startup Cognition raises $1B at $25B pre-money valuation (TechCrunch, May 2026)](https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/)

---

## Audio script
Cognition บริษัทเจ้าของ Devin — coding agent ที่ทำงานเองแบบ autonomous — กำลังคุยรอบใหม่ที่ valuation อย่างน้อย 40,000 ล้านเหรียญ. เพิ่งปิดรอบก่อนที่ 26,000 ล้านเมื่อพฤษภาคมแค่ 3 เดือนก่อน คือขึ้นเกือบเท่าตัวในหนึ่งไตรมาส. ตัวเลข run-rate ตอนปิดรอบก่อนอยู่ 492 ล้านเหรียญ Bloomberg บอกว่าต้องแตะ 1,000 ล้านก่อนรอบใหม่จะปิด. ที่น่าสนใจคือลูกค้า enterprise: Mercedes-Benz, NASA, Goldman Sachs, Santander เอา Devin ไป deploy บน production code จริง ทำ migration, update legacy — ไม่ใช่ pilot. Enterprise usage โตสิบเท่าตั้งแต่ต้นปี. Signal ที่ชัดคือตลาดเริ่มแยก "coding tool" กับ "coding agent" ออกจากกัน — tool อย่าง Cursor คิดเงินต่อ seat มนุษย์, agent อย่าง Devin คิดเงินต่อ ticket ที่มันปิดได้เอง. สำหรับ business ที่มี legacy code รอ migrate signal ตรงนี้คือ project ที่วางไว้ 6 เดือน agent ทำได้ใน 6 สัปดาห์. สำหรับคนสร้าง framework — ถ้ายังบังคับ enterprise ซื้อเป็น seat ต่อ developer จะเสียเปรียบเพราะ ROI enterprise คิดต่อ ticket ไม่ใช่ต่อ user แล้ว.
