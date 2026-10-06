---
date: 2026-10-06
slug: 26-10-07-0616-02-meta-hatch-watermelon-consumer
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial hero: a watermelon-shaped vault cracking open on a glossy Meta
  blue stage, releasing a glowing agent avatar labeled "HATCH". Floating
  app icons orbit around it — "DOORDASH", "ETSY", "REDDIT", "YELP",
  "OUTLOOK". A big neon price tag at the lower right reads "$199.99 / MO".
  A smaller caption at the top: "WATERMELON ≈ GPT-5.5 PARITY". Editorial
  isometric style, Meta blue + watermelon pink + warm cream, 1:1 aspect,
  no real human faces.
image: images/26-10-07-0616-02-meta-hatch-watermelon-consumer.png
---

# Meta เตรียมปล่อย Hatch + Watermelon — ยิง AI agent สำหรับผู้บริโภค $199/เดือน ชนตรง ChatGPT Pro

## TL;DR
- Meta เตรียมเปิด **Hatch** ภายในไม่กี่สัปดาห์ — consumer AI agent platform ที่ **customize dashboard** ได้ (fitness tracker, trip planner) และ act แทน user บน DoorDash, Etsy, Reddit, Yelp, Outlook
- **Watermelon** model ใหม่ตามมา ต.ค. — internal benchmark บอก **GPT-5.5 parity** ใช้ compute **~10x** ของ predecessor; Meta ยังไม่ยืนยัน public
- **Pricing tier สูงสุด $199.99/mo** — ชนตรง ChatGPT Pro 500 ของ OpenAI; Zuckerberg เปิดเกม monetize AI spending หลัง capex ปี 2026 ทะลุ $100B

## เกิดอะไรขึ้น

The Information และสำนักข่าว tech หลายเจ้ารายงานต่อเนื่องสัปดาห์นี้ว่า Meta ใกล้เปิด **Hatch** — consumer-facing AI agent platform ที่ internally คือเวอร์ชัน consumer ของ OpenClaw (agent ที่ Meta ใช้ internal). Hatch ออกแบบให้ user สร้าง **customizable dashboard** ใส่ของที่ตัวเองใช้ประจำ เช่น fitness tracker, trip planner, meal planner แล้ว agent ทำงานใน background — คอยอัพเดตข้อมูล, จอง, สั่งของ, ตอบ email ตามที่ตั้งไว้

Integration ที่ Meta pitch แบบตรง ๆ: **DoorDash, Etsy, Reddit, Yelp, Outlook** — basket ของ consumer workflow ปกติที่ user ทำซ้ำทุกสัปดาห์. Hatch ขอ API-level access ให้ agent book / order / search แทนได้. นี่คือจุดต่างจาก ChatGPT ที่ยัง chat-first — Hatch ตั้งใจทำ "ของเล่น" ให้ user feel ว่ามี personal operator

Monetization tier สะดุดตา: **$199.99/mo** สำหรับ premium — ชนกับ ChatGPT Pro ($200/mo) และ Pro 500 ($500/mo) ของ OpenAI ที่เพิ่งเปิดใน DevDay. Zuckerberg บอก investors หลายครั้งปีนี้ว่า Meta ต้อง "grow revenue beyond advertising" — บริษัท burn ~$100B capex ปี 2026 ไปกับ datacenter + GPU, revenue stream ใหม่ที่ไม่ใช่ ads เริ่ม critical สำหรับ story บน Wall Street

และ **Watermelon** — flagship model ใหม่ที่จะเปิด ต.ค. — internal benchmark บอก **GPT-5.5 parity** ใช้ compute ประมาณ 10x ของรุ่นก่อน (Llama 4 family). ตัวเลข 10x compute เพื่อ parity (ไม่ใช่ชนะ) เป็น flag ชัดว่า Meta ยังตามหลัง frontier scaling law แต่พร้อมจ่าย GPU-hour เพื่อปิด gap. The Information ย้ำว่าตัวเลขเหล่านี้มาจาก **internal benchmark ที่ยัง independently unverified** — ของ Meta ต้องรอ public eval

## ทำไมสำคัญ

Hatch คือ **"always-on agent สำหรับ consumer"** — ตรง concept เดียวกับ OpenAI Dots ที่เปิดใน DevDay (ก.ย.) และ Google "Project Jarvis" ที่รอ GA. ตลาด consumer agent กำลังปรับ format จาก chatbot เป็น **personal operator** ที่ user ไม่ต้องเปิด app → agent รัน task ที่ background. Pattern นี้มีความหมายกับ **แพลตฟอร์ม e-commerce / booking / content** ทุกเจ้า — ถ้า agent ของ Meta / OpenAI / Google ไปสั่ง DoorDash แทน user, DoorDash app ที่ user เปิดเองลดลง → revenue จาก upsell ใน app ลดด้วย

Pricing $199.99 บอกว่า Meta วาง bet ว่า **consumer จะจ่าย premium สำหรับ agent ที่ทำงานแทน** — ไม่ใช่ ad-supported model แบบ Facebook/Instagram ที่สร้าง empire ของ Meta. ถ้าสำเร็จ = Meta มี revenue stream ใหม่ที่ไม่ depend กับ Apple App Store policy หรือ ad market cycle. ถ้าไม่สำเร็จ = capex $100B ปีนี้กลายเป็น write-down ที่ CFO ต้องไปอธิบาย

เรื่องที่น่าสังเกตคือ Meta เลือก **ชื่อ codename Watermelon** ตามธรรมเนียม food fruit series — Llama / Behemoth / Scout → Watermelon สะท้อน strategy "big fat model, high compute". ตรงข้ามกับ efficient-first ที่ Mistral, Anthropic Haiku, และ open-weight Chinese labs เดิน. ปีหน้าตลาด consumer AI จะเห็น split: หนึ่งฝั่งขายปัญญา (frontier intelligence per query) หนึ่งฝั่งขาย personal operator (agent ที่ทำงานต่อเนื่องเป็นเดือน ๆ) — Meta ทางเลือกที่สอง

## มุม AI Agent Platform

**Builders:** คนทำ consumer agent app (Perplexity Spaces, Rabbit, Humane) ต้องรีบคิด dashboard pattern ก่อน Hatch เปิด — ถ้าปล่อยให้ Meta set standard "customizable panel + background execution" จะไล่ยาก. API shape ของ Hatch กับ DoorDash/Etsy/Reddit/Yelp/Outlook จะกลายเป็น **de facto consumer agent integration contract** ที่ ecosystem ต้องรองรับ. **Users / business:** merchant บน Etsy / Yelp ต้องเตรียม structured product feed สำหรับ agent (**agentic SEO / GEO**) ภายใน Q1 2027; ร้านอาหารบน DoorDash ต้อง list menu + modifier แบบ agent-readable ไม่งั้นหายจาก search ของ Hatch. **Ecosystem:** Stripe / Visa / Shopify จะเจรจา commission structure ใหม่กับ Meta — ใครเก็บค่าธรรมเนียมเมื่อ agent สั่งแทน user; Apple จะเริ่ม flag Hatch ใน App Store review (ปีก่อน Apple กัน Rabbit R1 กับ Humane ด้วย reason คล้ายกัน); สำหรับ builder enterprise agent — Hatch pricing $199 ยืนยันว่า **consumer willingness-to-pay สำหรับ AI operator สูงกว่าที่คาด** → ตลาด prosumer / SMB agent น่าจะเปิดกว้างต่อ

## Sources
- [Meta Plans to Launch 'Hatch' AI Agent Platform in Coming Weeks - The Information](https://www.theinformation.com/articles/meta-plans-launch-hatch-ai-agent-platform-coming-weeks)
- [Meta's paid AI agent Hatch launches soon with a new model called Watermelon due in October - The Decoder](https://the-decoder.com/metas-paid-ai-agent-hatch-launches-soon-with-a-new-model-called-watermelon-due-in-october/)
- [Meta plans to launch its OpenClaw rival, Hatch, within weeks - The Next Web](https://thenextweb.com/news/meta-hatch-ai-agent-watermelon-199-subscription)
- [Meta plans Hatch agent launch while considering a $199.99 monthly tier - Runtime Wire](https://runtimewire.com/article/meta-hatch-ai-agent-watermelon-model-launch)

---

## Audio script
Meta เตรียมเปิด Hatch ภายในไม่กี่สัปดาห์ — consumer AI agent platform ที่ customize dashboard ได้ ใส่ fitness tracker trip planner meal planner แล้ว agent ทำงาน background คอย book สั่ง อัพเดตข้อมูลแทน user. Integration เป้าแรกคือ DoorDash Etsy Reddit Yelp Outlook — basket ของ consumer workflow ปกติ. Premium tier $199.99 ต่อเดือน ชนตรง ChatGPT Pro ของ OpenAI. และ Watermelon model ใหม่จะเปิดตุลาฯ internal benchmark บอก GPT-5.5 parity ใช้ compute ประมาณสิบเท่าของรุ่นก่อน — Meta ยอมจ่าย GPU-hour เพื่อปิด gap. ทำไมสำคัญ. ตลาด consumer agent กำลังปรับ format จาก chatbot เป็น personal operator ที่ user ไม่ต้องเปิด app. OpenAI Dots เปิดเดือนก่อน ตอนนี้ Meta ตามด้วย Hatch Google กำลังรอ Project Jarvis GA. แพลตฟอร์ม e-commerce booking content ทุกเจ้าโดนกระทบ. ถ้า agent ไปสั่ง DoorDash แทน user DoorDash app ที่ user เปิดเองลดลง revenue จาก upsell ลดด้วย. Builder consumer agent app Perplexity Rabbit Humane ต้องรีบคิด dashboard pattern ก่อน Hatch set standard. Merchant Etsy Yelp ต้องเตรียม structured product feed สำหรับ agent ภายในไตรมาสแรกปีหน้า ไม่งั้นหายจาก search ของ Hatch

