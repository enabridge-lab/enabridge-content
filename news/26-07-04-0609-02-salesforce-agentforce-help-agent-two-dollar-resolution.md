---
date: 2026-07-04
slug: salesforce-agentforce-help-agent-two-dollar-resolution
topic: openbridge-trend
reading_time_min: 3
sources: 3
image_prompt: |
  A vending machine styled with the Salesforce cloud logo dispensing tickets
  labeled "RESOLVED"; each ticket has a price tag "$2". Above the machine, a
  massive stacked billboard reads "PAY PER RESOLUTION", "NO RESOLUTION →
  NO CHARGE", "$2.9B ARR". A small side panel shows a per-conversation
  meter with a red cross over it. Editorial isometric style, deep blue and
  cloud-white palette, 1:1 aspect, big readable numbers at thumbnail size,
  no real human faces.
image: images/26-07-04-0609-02-salesforce-agentforce-help-agent-two-dollar-resolution.png
---

# Salesforce Agentforce Help Agent GA เดือนนี้ — คิดเงินเมื่อ agent "ปิดจบ" เท่านั้น $2/resolution

## TL;DR
- Salesforce เปิดตัว Agentforce Help Agent เป็น GA ในเดือนกรกฎาคม 2026 พร้อม pricing model ใหม่ — $2 ต่อ resolution เมื่อ agent ปิดเคสจบเอง; ถ้าลูกค้าขอ human หรือเดินออก = ไม่คิดเงิน
- Agentforce ทำ ARR $2.9B, ปิดดีล 29,000+ deals — Salesforce กำลังเปลี่ยนจาก "sell software" เป็น "sell outcome"
- Pricing shift นี้ transfer risk จาก customer (ที่กลัวจ่ายค่า pilot ไม่ได้ผล) กลับไปที่ vendor — Salesforce ต้องมั่นใจว่า agent ทำงานได้จริงก่อนขาย

## เกิดอะไรขึ้น
Salesforce ประกาศว่า Agentforce Help Agent และ Agentforce Customer Service Portal จะเข้า general availability ในเดือนกรกฎาคม 2026 พร้อมกับ pricing model ใหม่: pay-per-resolution ที่ราคา flat $2 ต่อครั้งที่ agent ปิดเคสได้จบด้วยตัวเอง หากลูกค้าขอ escalate ไปหา human agent หรือถ้าลูกค้าเดินออกไปโดยไม่ได้ resolution — Salesforce ไม่คิดเงิน

โมเดลนี้ต่างจาก pricing ยุคก่อนของ Agentforce ที่คิดแบบ per-conversation ($2 per conversation) — ซึ่งลูกค้าหลายรายบ่นว่า "จ่ายให้ agent คุยไปเรื่อย ๆ โดยไม่ได้ผลลัพธ์" pay-per-resolution แก้ปัญหานี้ตรง ๆ: cost tied to outcome, not activity Adam Evans, EVP ฝ่าย Agentforce บอกว่า Salesforce ต้องการให้ลูกค้ารู้สึกว่า "Help Agent works for you — you only pay when it works"

Help Agent เป็น prebuilt agent ที่ setup ได้ในหลักนาที — เชื่อมกับ knowledge base + Salesforce Data Cloud โดยไม่ต้องเขียน code ทำงานได้ทุก channel (web, WhatsApp, in-product) และมี guardrails มาให้พร้อม pricing $2/resolution ทำให้ TCO คำนวณง่ายกว่า agent generic ในตลาด — CIO/COO เห็นเลขได้ทันทีว่าถ้าลด human handled tickets ได้ X% จะประหยัดกี่ล้านต่อปี

## ทำไมสำคัญ
Salesforce กำลังชี้ทิศทาง unit economics ของ agent industry ทั้งวงการ — และมันเปลี่ยน risk allocation ระหว่าง vendor กับ buyer ตลาด agent ปี 2025 เต็มไปด้วย pilot ที่ยกเลิกก่อนเข้า production เพราะลูกค้ากลัว "จ่ายค่าน้ำหมึกไปแล้วไม่ได้ผลลัพธ์" pay-per-resolution ตัด friction นั้นออก — vendor ต้องรับความเสี่ยงเองว่า agent จะทำงานได้ ถ้าไม่ได้ vendor ไม่มีรายได้

แต่ implication ที่ deeper กว่านั้นคือ Salesforce ต้อง confident ในระดับ engineering ว่า agent จะ "resolve" ได้จริงในสัดส่วนสูง — ไม่งั้น business model จะพัง unfortunately คำจำกัดความของ "resolution" ยังกำกวมอยู่ (Salesforce ปล่อยให้ลูกค้าและ agent เจรจากันเอง) — คู่แข่ง (Ada, Fin AI, Decagon, Sierra ที่เพิ่งระดมทุน $950M) คงต้องออก pricing แบบเดียวกันภายใน 2 quarter หรือถูกลูกค้าถามว่า "ทำไมพวกคุณยังคิดแบบ per-message อยู่?"

Context ของ ARR ก็สำคัญ: Agentforce ทำ ARR $2.9B และปิดดีล 29,000 deals ตัวเลขนี้กระโดดจาก $800M ARR ที่จบ Q4 FY26 (ม.ค. 2026) แปลว่า Agentforce triple ในหกเดือน หากไม่มี pricing shift แบบนี้ Salesforce อาจ hit ceiling — ลูกค้าที่ pilot แล้วไม่ได้ผลจะไม่ renew pay-per-resolution เปิดทางให้ Salesforce ขายไปได้เยอะขึ้น เพราะ downside risk ลดลง

## มุม AI Agent Platform
- **Builders**: pricing engine ของ agent platform ต้องรองรับ outcome-based billing — attribution, resolution definition, dispute handling; framework ที่ยังคิดแบบ per-token/per-call จะโดน commoditized
- **Users/business**: CFO อ่านเลข TCO ง่ายขึ้น = budget approval เร็วขึ้น; แต่ต้องระวัง edge case ที่ agent "แกล้ง resolve" (ปิดเคสโดยที่ปัญหายังอยู่) เพื่อ trigger billing — audit + escalation SLA ต้อง strict
- **Ecosystem**: BPO/contact center outsourcer (Concentrix, TTEC) จะ position อย่างไรเมื่อ vendor เริ่มขายผลลัพธ์แทน seat license? เรื่องเดียวกันจะกระจายไปสู่ vertical อื่น — legal (Harvey), healthcare, sales agent — และ Salesforce เพิ่งจุดไฟ

## Sources
- [Salesforce Launches Agentforce Help Agent That Deploys in Minutes and Only Charges for Resolutions — Salesforce](https://www.salesforce.com/news/stories/agentforce-help-agent-announcement/)
- [Huge Agentforce Pricing Shift: Salesforce Introduces Pay-Per-Resolution — Salesforce Ben](https://www.salesforceben.com/huge-agentforce-pricing-shift-salesforce-introduces-pay-per-resolution/)
- [Salesforce unveils AI Help Agent with pay-per-resolution pricing — CIO](https://www.cio.com/article/4189183/salesforce-unveils-ai-help-agent-with-pay-per-resolution-pricing.html)

---

## Audio script
เรื่องที่สอง Salesforce เพิ่งประกาศว่า Agentforce Help Agent จะเข้า general availability เดือนนี้ พร้อม pricing model ใหม่ที่จะเขย่าทั้งวงการ — pay per resolution สองดอลลาร์ต่อครั้ง แปลว่าอย่างนี้ ลูกค้าจะจ่ายเงินก็ต่อเมื่อ agent สามารถปิดเคสให้ลูกค้าได้จบด้วยตัวเอง ถ้าลูกค้าขอคุยกับคน หรือเดินออกไปโดยไม่ได้คำตอบ Salesforce ไม่คิดเงินเลย นี่คือการ shift risk จาก buyer กลับไปที่ vendor — เมื่อก่อนลูกค้าซื้อ pilot มาแล้วต้องลุ้นเองว่าจะได้ผลไหม ตอนนี้ Salesforce เป็นคนรับความเสี่ยงว่า agent ต้อง work จริง Adam Evans EVP ของ Agentforce บอกว่าคุณจ่ายเมื่อมัน work เท่านั้น ต่อไปคู่แข่งอย่าง Ada, Fin AI, Decagon, Sierra ที่เพิ่งระดมทุนไปเยอะจะต้องออก pricing แบบเดียวกันภายในครึ่งปี Context ที่สำคัญ Agentforce ทำ ARR แตะสองพันเก้าร้อยล้านดอลลาร์ ปิดดีลไปสองหมื่นเก้าพันดีลแล้ว pricing shift นี้จะเป็นตัวปลดล็อกให้ Salesforce ขายได้เร็วขึ้น เพราะ CFO ลูกค้าเห็นเลข TCO ชัดขึ้น เจอสัญญาแบบนี้ปฏิเสธยากมาก
