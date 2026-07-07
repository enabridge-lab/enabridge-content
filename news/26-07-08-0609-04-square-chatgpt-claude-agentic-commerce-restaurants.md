---
date: 2026-07-08
slug: square-chatgpt-claude-agentic-commerce-restaurants
topic: use-case
reading_time_min: 3
sources: 4
image_prompt: |
  A cozy street scene at dusk, isometric editorial style. A neon-lit deli
  storefront with a chalkboard menu labeled "REUBEN + CHOPPED LIVER". Above
  the storefront, two giant chat bubbles float — one labeled "CHATGPT" and
  one labeled "CLAUDE" — both funneling glowing orders down into a small
  Square terminal at the counter labeled "SQUARE POS". A banner across the
  top reads "0% MARKETPLACE FEE — 4.5M SELLERS". Warm cinematic amber
  lighting, 1:1 aspect, readable at 200px thumbnail, no real human faces.
image: images/26-07-08-0609-04-square-chatgpt-claude-agentic-commerce-restaurants.png
---

# Square ปล่อย ChatGPT app + Claude plugin — ลูกค้าถาม "หาร้าน deli ที่มี Reuben ใกล้ฉัน" แล้วสั่งจ่ายจบใน chat ผ่าน Order by Cash App, ร้าน F&B opt-in อัตโนมัติ, Square ไม่เก็บ marketplace fee

## TL;DR
- 1 ก.ค. — Square ประกาศ **ChatGPT app + Claude plugin** สำหรับ seller เริ่มที่ **US food & beverage merchant ที่ใช้ Square Online Ordering**. Customer ถาม ChatGPT/Claude "หาร้าน deli ใกล้ฉันที่มี Reuben + chopped liver" → เห็นเมนู, สั่ง, จ่ายด้วย **Order by Cash App** ทั้งหมดใน chat window
- ร้านที่ eligible **opt-in อัตโนมัติ ไม่ต้องเสียเวลา setup, ไม่มีค่า marketplace commission** — ตัดที่ DoorDash/Uber Eats ที่กิน 15-30% ต่อ order
- Square มี seller อยู่ 4.5M ราย; **42% ของ US consumer ใช้ AI ในการช้อป**; Deloitte/Bain ประเมิน **agentic commerce จะขับ US ecom $385B ภายในปี 2030**. Amazon Alexa+ integration ตามมาถัดไป — Square วาง PoS ตัวเองเป็น **default distribution layer ของ agentic commerce ร้านเล็ก**

## เกิดอะไรขึ้น
วันที่ 1 กรกฎาคม Square (แผนก merchant ของ Block) ประกาศ **ChatGPT app + Claude plugin** ที่ deliver capability ใหม่: ลูกค้าที่ใช้ ChatGPT หรือ Claude ถาม assistant ตรง ๆ ว่า "หาร้าน deli ที่มี Reuben sandwich ใกล้ฉัน" — assistant จะไป query ร้านที่มี Square Online Ordering active ใน radius นั้น, ส่ง menu กลับมาใน chat, ให้ลูกค้ากด order, จ่ายด้วย **Order by Cash App** ที่ integrate อยู่แล้วในระบบ Square. **ทุกอย่างเกิดใน chat window เดียว — ลูกค้าไม่ต้องเปิดเว็บร้าน ไม่ต้องดาวน์โหลด DoorDash / Uber Eats app**

Model ธุรกิจของ Square ในเรื่องนี้ตัดขาดจาก aggregator เดิม 2 จุดสำคัญ: (1) **ร้านที่ eligible opt-in อัตโนมัติ** — ไม่ต้องเซ็นสัญญาแยก, ไม่ต้อง onboarding, ไม่ต้อง API integration — เพราะ Square มี catalog เมนูของร้านอยู่แล้วในระบบ; (2) **Square ไม่เก็บค่า marketplace commission เพิ่ม** — order ที่มาจาก ChatGPT/Claude จ่ายค่า processing fee เท่าเดิมกับ order ที่ walk-in — ตัดโมเดล DoorDash/Uber Eats ที่กินร้าน 15-30% ต่อ order

Scale — Square มี **seller 4.5 ล้านราย** ที่ transact ผ่าน search + maps + social + marketplace อยู่แล้ว. Amit Shah, Head of Product Discovery, ให้สัมภาษณ์ว่า Square กำลังทำ integration ต่อกับ **Amazon Alexa+** เพื่อขยายไป voice commerce — signal ว่า **Square เห็นตัวเองเป็น distribution layer ที่ platform AI ตัวไหนก็จะ integrate เข้ามา** ไม่ใช่แค่ PoS provider. บริษัท analytics เอ่ยตัวเลข: **42% ของ US consumer ใช้ AI ในการช้อป**, และ Deloitte/Bain ประเมินว่า **agentic commerce จะขับ US ecom $385B ภายในปี 2030**

Contrast กับ **DoorDash / Uber Eats / Grubhub** — aggregator เหล่านี้ยัง lock ลูกค้าใน app ตัวเอง + กินค่า commission 15-30%. Square กำลังใช้ **AI assistant เป็นช่อง distribution ใหม่** ที่ bypass aggregator เดิม — จ่ายค่าอะไรให้ ChatGPT/Claude ไม่ประกาศ แต่ pattern ในอุตสาหกรรมคือ **revenue share ต่ำกว่า aggregator เพราะ AI vendor ยังไม่เอาส่วนต่างการชำระเงินเป็น core business**

## ทำไมสำคัญ
รอบนี้เป็น **first-mover moment ของ agentic commerce ในระดับ retail มวลชน** — ก่อนหน้านี้ agentic commerce จำกัดอยู่ที่ B2B (procure-to-pay, RFQ automation) หรือ eCommerce ใหญ่ (Amazon Rufus, Shopify Sidekick). รอบนี้เป็นครั้งแรกที่ **ร้านอาหารเล็ก ระดับ mom-and-pop deli** ได้เข้าถึง AI-driven demand generation โดยไม่ต้องเซ็นสัญญา, ไม่ต้องจ่ายค่า setup, และไม่ต้องแบ่ง revenue กับ aggregator. Bar to entry = 0 → **น่าจะเห็น GMV ที่ผ่าน channel นี้กระโดดใน 90 วันข้างหน้า**

Signal ต่อ aggregator เดิม: **DoorDash/Uber Eats/Grubhub มี moat อ่อนลงเร็ว** — ลูกค้าที่พึ่ง AI assistant ในการค้นหาร้าน (42% ของ US consumer) จะ bypass app aggregator เพราะ chat UX friction ต่ำกว่า. aggregator ต้องประกาศ integration กับ ChatGPT/Claude ภายในไตรมาสถัดไป ไม่งั้น demand จะ leak หนัก. DoorDash พยายาม launch "DoorDash for AI" ตัวเองเป็นทางเลือก แต่ scale ยังห่างจาก 4.5M sellers ของ Square

Point ที่ underweighted ในข่าว: **Order by Cash App เป็น checkout layer** — คือลูกค้าไม่ต้องกรอกบัตรเครดิตใน ChatGPT/Claude เพราะ Cash App เก็บข้อมูลจ่ายเงินแล้ว. **Block กำลัง arbitrage สินทรัพย์ตัวเอง 3 ตัวรวมกัน — Square (merchant), Cash App (payment), และ AI distribution (ChatGPT/Claude)**. เทียบกับ PayPal ที่มี Braintree แต่ไม่มี merchant catalog + AI channel, และ Stripe ที่มี pipeline แต่ไม่มี consumer payment app — **Block มี position ที่ competitor ไม่มี** ในสงคราม agentic commerce

## มุม AI Agent Platform
- **Builders** — startup ที่ทำ **shopping assistant vertical** (Perplexity Shopping, Klarna AI, Kayak Chat) กำลังจะเจอปัญหา moat ต่ำ — เพราะ Square + Shopify + BigCommerce + Amazon จะทยอยเปิด direct integration กับ ChatGPT/Claude ในไตรมาสถัดไป. ทางรอด: (1) **vertical ที่ Square ไม่แตะ** — luxury goods, medical device, B2B parts, sneakers/collectibles, (2) **AI checkout layer** ที่ handle payment + shipping + return แบบ end-to-end (Stripe / Adyen / Shopify Payments compete จุดนี้ตรง ๆ), (3) **inventory-aware routing** ที่ query multi-merchant real-time — เป็นชั้นที่ ChatGPT/Claude เองไม่ทำ

- **Users / business ไทย** — retailer + F&B chain ที่มี e-commerce channel ควรถามคำถาม 3 ข้อในการประชุม CDO/CMO ถัดไป: (1) **catalog ของเราพร้อมไปอยู่ใน AI assistant discovery ไหม** — schema ครบ, สินค้ามี description, price, inventory sync real-time; (2) **checkout ของเราเชื่อม LINE Pay / TrueMoney / ShopeePay ที่ user ไทยมี default ไหม** — Cash App คือ default ของ US, ไทยต้อง localize; (3) **ถ้า Foodpanda / Grab / LINE MAN ถูก bypass, เราขายตรงลูกค้าใน AI assistant ได้ต้นทุนต่ำแค่ไหน** — ตัวเลข economics ที่ต่างจาก aggregator commission เดิมชัด ๆ ควรวิเคราะห์วันนี้. **SME food ระดับร้านเดี่ยว** — ยังต้องรอ localize (Line MAN / Grab น่าจะทำก่อน) แต่ pattern โผล่ในไทยแน่ ๆ ในครึ่งหลังปี

- **Ecosystem** — **AI vendor (Anthropic, OpenAI)** ได้ signal ว่า commerce เป็น revenue stream ใหม่ที่ต่างจาก subscription — จะเห็น API surface สำหรับ commerce transaction (product query, cart operation, checkout intent) เป็น first-class ในไตรมาสถัดไป. **Payment processor** (Adyen, Stripe, PayPal) ต้องมี "AI-friendly" API ที่ ChatGPT/Claude เรียก checkout ตรงได้; ที่ไม่ทำจะโดน bypass. **Aggregator delivery** (DoorDash, Uber Eats, Instacart) กำลังเผชิญ existential threat จาก AI channel ที่ไม่กิน commission

## Sources
- [Square Introduces New ChatGPT and Claude Integrations — Square Press Release](https://squareup.com/us/en/press/claude-chatgpt-integrations)
- [Square launches agentic commerce integrations with ChatGPT, Claude — Digital Commerce 360](https://www.digitalcommerce360.com/2026/07/01/square-agentic-commerce-integrations-chatgpt-claude/)
- [Square Intros ChatGPT and Claude Integrations for Sellers — PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/square-intros-chatgpt-and-claude-integrations-for-sellers/)
- [Square launches a ChatGPT app and Claude plugin that take AI-agent orders from restaurants — Shopifreaks](https://www.shopifreaks.com/square-launches-a-chatgpt-app-and-claude-plugin-that-take-ai-agent-orders-from-restaurants/)

---

## Audio script
วันที่ 1 กรกฎาคม Square ประกาศ ChatGPT app กับ Claude plugin สำหรับ seller ของตัวเอง เริ่มที่ร้าน food and beverage ในสหรัฐที่ใช้ Square Online Ordering ลูกค้าเปิด ChatGPT หรือ Claude ถามตรง ๆ ว่า หาร้าน deli ใกล้ฉันที่มี Reuben sandwich กับ chopped liver assistant ไป query ร้านที่มี Square Online Ordering active ในรัศมี ส่งเมนูกลับมาใน chat ให้ลูกค้ากด order จ่ายด้วย Order by Cash App ทั้งหมดจบใน chat window เดียว ลูกค้าไม่ต้องเปิดเว็บร้าน ไม่ต้องดาวน์โหลด DoorDash หรือ Uber Eats app Model ที่ตัดขาดจาก aggregator เดิม 2 จุด ร้านที่ eligible opt in อัตโนมัติ ไม่ต้องเซ็นสัญญาแยก และ Square ไม่เก็บค่า marketplace commission เพิ่มเลย order ที่มาจาก ChatGPT Claude จ่าย processing fee เท่าเดิมกับ order walk in ตัดโมเดล DoorDash Uber Eats ที่กินร้าน 15 ถึง 30 เปอร์เซ็นต์ต่อ order Square มี seller 4.5 ล้านราย 42 เปอร์เซ็นต์ของ US consumer ใช้ AI ในการช้อป Deloitte Bain ประเมิน agentic commerce จะขับ US ecom ถึง 385 พันล้านดอลลาร์ภายในปี 2030 Amazon Alexa plus integration ตามมาถัดไป Square วาง PoS ตัวเองเป็น default distribution layer ของ agentic commerce ร้านเล็ก signal ต่อ aggregator เดิม DoorDash Uber Eats Grubhub moat อ่อนลงเร็ว ลูกค้าที่พึ่ง AI assistant จะ bypass app aggregator เพราะ chat UX friction ต่ำกว่า สำหรับธุรกิจไทย retailer F and B chain ควรถาม 3 ข้อในประชุม CDO CMO ถัดไป catalog พร้อมไปอยู่ใน AI discovery ไหม checkout เชื่อม LINE Pay TrueMoney ShopeePay ที่ user ไทย default หรือยัง ถ้า Grab LINE MAN ถูก bypass ต้นทุนขายตรงลูกค้าใน AI assistant ต่างจาก commission เดิมเท่าไร ตัวเลขนี้ควรวิเคราะห์วันนี้ pattern จะโผล่ในไทยครึ่งหลังปีแน่นอน
