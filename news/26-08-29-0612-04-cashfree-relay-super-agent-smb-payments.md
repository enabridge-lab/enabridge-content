---
date: 2026-08-29
slug: cashfree-relay-super-agent-smb-payments
topic: use-case
reading_time_min: 3
sources: 4
image_prompt: |
  Editorial isometric illustration of a small Indian shop counter at dusk
  glowing with warm light — behind the counter, a translucent multi-armed
  robotic silhouette juggles floating task chips: "RETRY PAYMENT",
  "RECOVER CART", "CONFIRM COD", "MANAGE SUB", "FILE DISPUTE". A stack of
  invoices flows into the robot on the left and out as neat completed
  receipts on the right. Three oversized number panels stacked at top:
  "FREE AT LAUNCH", "OUTCOME PRICING NEXT", "MERCHANT-DATA STAYS INTERNAL".
  Cashfree-blue banner across the top reads "RELAY — SUPER AGENT GA". Deep
  navy background with amber-to-cyan rim light. 1:1 aspect. No real human
  faces (silhouette only). Text and numbers sized to read in a 200px
  thumbnail.
image: images/26-08-29-0612-04-cashfree-relay-super-agent-smb-payments.png
---

# Cashfree ปล่อย **Relay Super Agent** GA ทั่วอินเดีย — AI agent รับงาน payment ops ของ SMB ฟรีที่ launch, pricing outcome-based ตามการใช้จริง

## TL;DR
- **27 ส.ค. 2026** Cashfree Payments (fintech อินเดีย, PhonePe subsidiary) เปิด **Relay** — AI **"Super Agent"** สำหรับ SMB — จาก merchant beta (เริ่ม พ.ค. 2026) → **general availability ทั่ว Cashfree merchant network**
- Task ที่ Relay รับ: **failed payment retry, abandoned cart recovery, COD confirmation, subscription management, dispute filing** — งาน payment operations ที่ SMB owner ปกติทำเอง หรือจ้าง junior staff
- **Pricing model แปลก:** ฟรีสำหรับทุก Cashfree merchant ที่ launch — พร้อมจะ move ไป **outcome-based pricing** เมื่อ adoption โตขึ้น. Relay run บน infrastructure ของ Cashfree ทั้งหมด — merchant transaction data **ไม่ส่ง** ให้ external AI provider
- Signal: **agentic AI เข้าถึง SMB layer** — ไม่ใช่แค่ enterprise Fortune 500. Pattern SMB-native agent ที่ bundle เข้า vertical SaaS ที่ merchant ใช้อยู่แล้ว = distribution model ที่ scale เร็วที่สุด, และ **outcome-based pricing** เป็น experiment ที่ทั้ง vertical จะจับตา

## เกิดอะไรขึ้น

**Cashfree Payments** ที่เป็น payment gateway อันดับต้น ๆ ของอินเดีย (เป็น subsidiary ของ PhonePe ตั้งแต่ 2024) — เปิดตัว **Relay** ในเดือน พ.ค. 2026 เป็น merchant beta ให้ D2C brand + SMB ทดลอง. 27 ส.ค. 2026 ประกาศ **general availability** ผ่าน sme streaming media coverage (BFSI Elets, SMEStreet, IBS Intelligence): merchant Cashfree ทุกรายเปิดใช้ Relay ได้ทันที ไม่ต้องรอ waitlist

Relay ถูกแบรนด์ว่า **"Super Agent"** — คือ agent ตัวเดียวที่ทำงาน payment ops หลายอย่างได้แทน SMB owner. Task ที่ Relay รับผิดชอบ (ตาม official spec):
- **Failed payment retry** — เมื่อ transaction fail (card decline, bank timeout, network issue) Relay retry ตาม pattern ที่เรียนรู้จาก merchant catalog + customer behavior
- **Abandoned cart recovery** — customer add to cart แต่ไม่ complete → Relay ส่ง follow-up ที่ personalize (email, SMS, WhatsApp) + generate discount code ตาม willingness-to-pay heuristic
- **COD (cash on delivery) confirmation** — Relay call/message customer ยืนยัน COD order ก่อน dispatch เพื่อลด return-to-origin rate ที่เจ็บมาก D2C brand อินเดีย
- **Subscription management** — เตือน renewal, handle upgrade/downgrade, handle payment method update
- **Dispute filing** — เมื่อ chargeback เกิด Relay รวบรวม evidence + ยื่น dispute ให้ merchant ตาม timeline ของ card network

**Pricing model:** ฟรีสำหรับ Cashfree merchant ทั้งหมดที่ launch. Cashfree ระบุ intent จะ move ไป **outcome-based pricing** เมื่อ adoption โต — คิดค่าตาม dollar-value ของ payment ที่ recover ได้ / cart ที่ save ได้ / dispute ที่ชนะ — แทน seat-based license หรือ token consumption. **Data residency:** Relay run **entirely บน infrastructure ของ Cashfree** ในอินเดีย — merchant transaction data (PII, transaction detail, customer identifier) **ไม่ส่ง** ไปยัง OpenAI/Anthropic/Google. Cashfree ไม่เปิดเผยว่าใช้ model อะไรอยู่หลังบ้าน (น่าจะเป็น mix ระหว่าง open-source model บน dedicated infra + fine-tuned ตาม vertical)

## ทำไมสำคัญ

**สิ่งที่น่าสนใจไม่ใช่ Relay เอง — เป็น distribution model** ที่ Cashfree เลือก. Instead of ให้ merchant SMB ต้อง (1) evaluate agent platform, (2) integrate API, (3) train, (4) จ่ายค่า subscription — Cashfree bundle agent เข้าไปใน gateway ที่ merchant ใช้อยู่แล้วรายวัน. Merchant คนใหม่ไม่ต้องทำอะไรเพิ่ม — feature เปิดใน dashboard ที่รู้จักอยู่แล้ว. Distribution cost per user = **ต่ำมาก** vs. horizontal agent platform ที่ต้อง acquire user เอง

Pattern นี้จะกระจายเร็วทั่วอินเดีย + เอเชียใต้ + ประเทศกำลังพัฒนาที่ SMB > 90% ของ business: **vertical SaaS (payment, POS, e-commerce, accounting) จะแข่งกัน bundle agent เข้ามาเป็น native feature**. คาดการณ์: Razorpay จะประกาศ analog ภายใน 60 วัน, PayU ภายใน 90 วัน, และในไทย SCB Easy/KBank Business/Ascend Money จะเริ่ม pilot ในไตรมาสถัดไป. **Point of view:** Cashfree เดินเกม outcome-based pricing ถูก — เพราะ SMB ไม่ยอมจ่าย fixed subscription ที่ไม่รู้ ROI, แต่ยอมจ่าย % ของเงินที่ agent recover ได้จริง. Pattern นี้จะกลายเป็น **default pricing model ของ agent ในตลาด SMB** ภายในสิ้นปี — และ Cashfree ที่ทดลองก่อนจะ set benchmark

Data residency angle สำคัญ — merchant data อยู่ในอินเดีย, ไม่ส่ง external AI provider — จะเป็น requirement บังคับใน jurisdiction ที่มี data localization law (อินเดีย DPDP Act, ไทย PDPA, EU GDPR + AI Act). Vendor agent horizontal (OpenAI, Anthropic, Google) จะเสียเปรียบใน SMB layer ประเทศเหล่านี้ — เพราะ SMB ไม่มี legal + engineering resource ทำ compliance ให้ passing regulator. Vendor local ที่ own infrastructure + build agent stack ในประเทศจะได้เปรียบ

## มุม AI Agent Platform

**Builders:** ถ้าคุณกำลังสร้าง horizontal agent platform ที่คาดว่า SMB จะ direct-signup — reset expectation. Distribution ผ่าน vertical SaaS ที่ SMB ใช้อยู่แล้ว (POS, accounting, payment, e-commerce, booking) เป็น 10x เร็วกว่า. Partner strategy คือ: (1) provide white-label agent SDK ให้ vertical SaaS integrate ได้ใน 2-4 สัปดาห์, (2) share revenue ตาม outcome ไม่ใช่ per-seat, (3) run บน infra ของ partner ถ้า data residency ต้องการ. **Users / business:** ถ้าคุณเป็น SMB — เช็ค vertical SaaS ที่คุณใช้อยู่ (Cashfree/Razorpay/Stripe/BillPlz/PayHere/2C2P): ถามว่ามี agent feature อะไรบ้าง, ราคาเท่าไหร่, outcome เท่าไหร่. ราคา *"ฟรีตอนนี้ + outcome later"* เป็น pattern ปกติ — เริ่มใช้เลย. **Ecosystem:** vertical SaaS ในไทย (Ecomm.co, Bento, Peak Engine, Manatal, Wongnai POS) จะมี pressure ที่ต้อง ship agent feature ใน 90-180 วัน ก่อน customer switch ไป Cashfree/Razorpay analog

## Sources
- [Cashfree Payments Launches 'Relay', AI Super Agents to Automate End-to-End Payment Operations for SMBs — Elets BFSI](https://bfsi.eletsonline.com/cashfree-payments-launches-relay-ai-super-agents-to-automate-end-to-end-payment-operations-for-smbs/)
- [Cashfree Relay Automates Payment Workflows for SMBs — SMEStreet](https://smestreet.in/technology/cashfree-relay-automates-payment-workflows-for-smbs-12442302)
- [Cashfree's Relay brings AI agents to SMB payment operations — IBS Intelligence](https://ibsintelligence.com/ibsi-news/cashfrees-relay-brings-ai-agents-to-smb-payment-operations/)
- [AI Agents News — Week of August 28, 2026 — AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)

---

## Audio script
สวัสดีครับ วันที่ 27 สิงหาคม Cashfree Payments ที่เป็น payment gateway อันดับต้นของอินเดีย เปิด Relay super agent ที่รับงาน payment ops ให้ SMB จาก merchant beta ตั้งแต่พฤษภาคม ไป general availability ทั่ว network task ที่ Relay ทำ failed payment retry abandoned cart recovery COD confirmation subscription management dispute filing งานที่เมื่อก่อน owner ต้องทำเอง หรือจ้าง junior staff pricing model ฟรีที่ launch พร้อมจะ move ไป outcome-based pricing เมื่อ adoption โต คิดค่าตามเงินที่ agent recover ได้ ไม่ใช่ seat license ที่น่าสนใจไม่ใช่ตัว Relay เอง เป็น distribution model ที่ Cashfree เลือก แทนที่จะให้ merchant ต้อง evaluate integrate train Cashfree bundle agent เข้าไปใน gateway ที่ merchant ใช้อยู่แล้วรายวัน distribution cost per user ต่ำมาก pattern นี้จะกระจายเร็วทั่วอินเดียเอเชียใต้ และประเทศที่ SMB เป็นส่วนใหญ่ของธุรกิจ vertical SaaS payment POS e-commerce accounting จะแข่งกัน bundle agent เป็น native feature Razorpay จะประกาศ analog ภายใน 60 วัน PayU 90 วัน ในไทย SCB Easy KBank Business Ascend Money จะเริ่ม pilot ไตรมาสถัดไป outcome-based pricing จะกลายเป็น default ของ agent ตลาด SMB ภายในสิ้นปี ถ้าคุณเป็น SMB เช็ค vertical SaaS ที่คุณใช้อยู่ว่ามี agent feature อะไร ราคาฟรีตอนนี้ outcome later เป็น pattern ปกติ เริ่มใช้เลย ถ้าคุณสร้าง horizontal agent platform ที่คาดว่า SMB direct signup reset expectation distribution ผ่าน vertical SaaS เป็น 10x เร็วกว่า
