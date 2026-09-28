---
date: 2026-09-28
slug: instinct-personal-agent-1b-series-c
topic: use-case
reading_time_min: 3
sources: 5
image_prompt: |
  Editorial isometric illustration of a smartphone standing upright on a
  desk, an SMS bubble floating above it that reads "Text me. I handle it."
  On the desk sit three tasks the phone handles in parallel: a tiny cargo
  truck labeled "GROCERIES", a paper map labeled "ROAD TRIP", and a
  crossed-out subscription card labeled "CANCELLED". A price tag on the
  phone reads "$10B" and a small ribbon "4x IN 3 WEEKS". Cinematic
  navy-and-copper palette, no real human faces (no user hands visible),
  1:1 aspect. High contrast for 200px thumbnails, editorial style like a
  Fortune startup profile.
image: images/26-09-29-0615-03-instinct-personal-agent-1b-series-c.png
---

# Instinct ระดม $1B ที่ valuation $10B — โตขึ้น 4 เท่าใน 3 สัปดาห์ pattern personal agent เริ่มลงตัว

## TL;DR
- 28 ก.ย. **Instinct** startup personal agent ปิดรอบ Series C **$1B ที่ valuation $10B** จาก Sequoia, Benchmark, Coatue
- **4x markup ใน 3 สัปดาห์** — ก่อนหน้า Series B $250M ที่ $2.5B; ทะลุ **100,000 users** ใน early access
- Founder **Noah Shinn อายุ 23** (อดีต Sierra + MIT/Northeastern ML/PL research); product เป็น agent ที่คุยผ่าน SMS + call ทำงานให้เสร็จเอง

## เกิดอะไรขึ้น
Instinct บริษัท personal AI agent จาก San Francisco ประกาศระดม Series C **$1 พันล้าน** ที่ **valuation $10 พันล้าน** จาก Sequoia Capital, Benchmark Capital, และ Coatue — 4 เท่าของ Series B ที่ปิดไปเมื่อ 3 สัปดาห์ก่อนที่ $2.5B. Founder **Noah Shinn** อายุ 23 ปี (research scientist ที่ Sierra ก่อนหน้า + ML และ programming-language research ที่ MIT/Northeastern) บอกว่าเงินก้อนนี้จะเอาไป "bring useful AI to everyone" — statement กว้างมากสำหรับ product ที่ยังอยู่ใน invite-only.

Product design ของ Instinct ตรงข้ามกับ Muse ของ Meta ที่โดน Amazon block คนละทิศ. Instinct **ไม่มี mobile app** — user text หรือ call มาที่เบอร์ ระบบใช้ **phone และ computer ของตัวเอง** (isolated sandbox, short-lived local credential, identity-signed tool execution) ทำงานให้เสร็จตั้งแต่ต้นจนจบ. Use case ที่ product page แสดงคือ: วางแผน road trip ข้ามประเทศ, สั่งของ grocery รายสัปดาห์, ยกเลิก subscription ที่ลืมไว้. The Information รายงานว่า Instinct ทะลุ 100,000 users แล้ว. TechCrunch เรียก product ตัวนี้ว่า "viral AI agent" — SMS-only interface + Twitter demo ทำให้ user growth ขึ้น ตี organic ล้วน.

พร้อมกับ funding, Instinct ประกาศ **active detection system** — hallucination filter ที่ตรวจ error เล็ก ๆ ระหว่างที่ agent form response แล้วลบทิ้งก่อน execute action. เป็น pattern ตอบตรงกับ safety concern ที่ตลาดตั้งคำถามหลัง OpenAI Medicare case — agent ที่จ่ายเงิน + จอง + ยกเลิก contract ให้ user ต้องมี guard rail. Business Insider ทำ profile Noah Shinn ในสัปดาห์เดียวกัน — เน้นว่าเขา research scientist ที่ Sierra (โครงการ virtual agent สาย customer service ของ Bret Taylor + Clay Bavor) ก่อนจะออกมาสร้าง Instinct — background sync กับ product ที่ต้องการ tool use เก่ง.

## ทำไมสำคัญ
$10B valuation ของ Instinct โตขึ้น 4 เท่าใน 3 สัปดาห์ **ก่อนที่ product จะออกจาก early access** — พูดอีกทางคือ Sequoia + Benchmark + Coatue เดิมพันว่า personal agent market ใหญ่กว่าที่ conservative model คำนวณ. ตัวเลข 100K user ไม่ใหญ่โดยตัวมันเอง แต่ signal สำคัญคือ **retention กับ willingness to pay** ที่ VC เห็นภายในเลย — Instinct จำกัด access แสดงว่าใช้แล้วติด, viral demo บน X คนถ่ายวิดีโอ agent จองร้าน / ยกเลิก subscription จริง ๆ แสดงว่ามี trust แบบที่ chatbot ปกติไม่ได้.

Pattern ที่กำลังเกิดขึ้น: **personal agent เอาชนะ personal assistant app** ด้วยเงื่อนไข 3 ข้อ — (1) interface ที่ user familiar อยู่แล้ว (SMS/phone แทน app store install), (2) task ที่ user ยอมจ่ายให้คนอื่นทำ (executive assistant, travel agent, personal shopper — market ที่ Rocketrip, Zeel, TaskRabbit จับได้แต่ไม่ scale เพราะ marginal cost คน), (3) safety layer ที่ user เชื่อได้ที่จะให้ credential (ตรงจุดที่ Instinct เพิ่ง ship). Muse ของ Meta ล้ม 3/3 ข้อ — mobile app ใหม่, ไม่มี trust track record, และ Amazon block ปิดประตูก่อน user รู้จัก. Rabbit R1, Humane AI Pin ล้มทั้งสามข้อยิ่งกว่านั้น.

Signal ที่ต้องจับตาไม่ใช่ Instinct จะโตต่อไปไหม — คือ **Sequoia, Benchmark, Coatue** สามเจ้านี้ที่เข้าใน round เดียว. สามเจ้านี้ rare ร่วม deal ก่อน Series D (Airbnb, Instagram, Stripe เป็น example ที่ทั้งสามอยู่). ที่ทั้งสามเข้าครั้งเดียวใน round pre-revenue = signal ตลาดที่ personal agent จะเป็น consumer subscription tier ใหญ่กว่า Netflix ในอีก 5 ปี. คำถามที่เปิดคือ **retention curve ที่ 6-12 เดือน** — ถ้า user still use ทุกวันที่ month 12, valuation $10B ต่ำเกินไป; ถ้า drop ที่ month 3, VC อาจได้ paper markdown ใหญ่ที่สุดของปี.

## มุม AI Agent Platform
**Builders** ที่ทำ personal agent — Instinct ทำให้ **SMS / voice interface** ชนะการแข่งขัน UX สำหรับ consumer agent; app native ไม่จำเป็น. ถ้าคุณกำลัง build agent สาย productivity / lifestyle, ลด friction install ให้ต่ำที่สุด, ให้ user text ก็ใช้ได้. **Users / business** ที่ทำ B2C — ถ้า product ของคุณเป็น booking / e-commerce / subscription, เตรียม **agent-friendly rate card**. Amazon เลือก block ได้ = สูญเสีย $68B retail media แต่ Delta / Marriott / Spotify ที่อยากให้ Instinct จอง/สมัครแทน user ตรง ๆ จะเสนอ discount 5-15% ผ่าน agent channel ในไตรมาสหน้า. **Ecosystem** — Stripe Link, Visa Intelligent Commerce, Mastercard Agent Pay จะเห็น transaction volume จาก Instinct-shaped agent เพิ่มขึ้น 5-10x ในปีหน้า. Trust layer + payment rail คือ dual moat ที่ทั้ง incumbent (Visa) และ startup (Stripe) จะแย่งกัน; personal agent เป็น demand source แรกที่หนักพอจะสร้าง unit economics ให้ pattern นี้.

## Sources
- [Instinct Raises $1 Billion in Series C Funding from Sequoia, Benchmark and Coatue at $10 Billion Valuation — Business Wire](https://www.businesswire.com/news/home/20260928153437/en/Instinct-Raises-$1-Billion-in-Series-C-Funding-from-Sequoia-Benchmark-and-Coatue-at-$10-Billion-Valuation)
- [Viral AI agent Instinct raises $1B Series C at a $10B valuation — TechCrunch](https://techcrunch.com/2026/09/28/viral-ai-agent-instinct-raises-1b-series-c-at-a-10b-valuation/)
- [Personal AI Agent Instinct Quadruples Valuation to $10 Billion in 1 Month — PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/personal-ai-agent-instinct-quadruples-valuation-to-10-billion-in-1-month/)
- [Business Insider Profiles Noah Shinn as Instinct AI Talks $10B Valuation — AI Weekly](https://aiweekly.co/alerts/business-insider-profiles-noah-shinn-as-instinct-ai-talks-10b-valuation-invite)
- [Instinct Raises $1B Series C at $10B Valuation to Bring Useful AI to Everyone — Unite.AI](https://www.unite.ai/instinct-raises-1b-series-c-at-10b-valuation-to-bring-useful-ai-to-everyone/)

---

## Audio script
Instinct startup personal agent จาก San Francisco เพิ่งปิด Series C หนึ่งพันล้านดอลลาร์ที่ valuation หมื่นล้าน จาก Sequoia Benchmark Coatue — โตขึ้น 4 เท่าใน 3 สัปดาห์จาก Series B ที่ 2.5 พันล้าน. Founder Noah Shinn อายุ 23 ปี อดีต research scientist ที่ Sierra + ML programming language research ที่ MIT Northeastern. Product design ตรงข้าม Muse ของ Meta ที่โดน Amazon block คนละทิศ — Instinct ไม่มี mobile app user text หรือ call ที่เบอร์ agent ใช้ phone และ computer ของตัวเอง sandbox แยก ทำงานให้เสร็จตั้งแต่ต้นจนจบ. Use case คือวางแผน road trip สั่ง grocery รายสัปดาห์ ยกเลิก subscription. ทะลุ 100000 user แล้ว ใน invite only. พร้อม funding ประกาศ hallucination filter ตรวจ error ก่อน execute — pattern ตอบ safety concern หลัง OpenAI Medicare case. Pattern ที่เกิดคือ personal agent เอาชนะ personal assistant app ด้วย 3 เงื่อนไข — interface ที่ user familiar อยู่แล้ว task ที่ user ยอมจ่ายให้คนอื่นทำ safety layer ที่ user เชื่อได้. Muse ล้ม 3 ใน 3. Rabbit R1 Humane AI Pin ล้มยิ่งกว่า. Signal ที่ต้องจับตาคือ Sequoia Benchmark Coatue รวมกันใน round เดียว rare มาก เคยเจอที่ Airbnb Instagram Stripe เท่านั้น. คำถามเปิดคือ retention 6 ถึง 12 เดือน — ถ้ายังใช้ทุกวันปีหน้า valuation ต่ำเกินไป ถ้าดร็อป month 3 อาจเป็น markdown ใหญ่ที่สุดของปี. ถ้าคุณ build agent สาย consumer ลด friction install ให้ SMS ก็ใช้ได้ ถ้าคุณเป็น B2C service เตรียม agent friendly rate card เพราะ Delta Marriott Spotify จะเริ่มเสนอส่วนลด 5 ถึง 15 percent ผ่าน agent channel ไตรมาสหน้าแน่นอนครับ.
