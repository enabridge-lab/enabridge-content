---
date: 2026-08-20
slug: etched-700m-21b-sohu-transformer-asic-jane-street
topic: use-case
reading_time_min: 5
sources: 4
image_prompt: |
  Editorial isometric illustration of a datacenter rack labeled "SOHU"
  glowing in the middle; on top a stacked number readout: "$700M SERIES D",
  "$21B VALUATION", "1 MONTH". Jane Street logo painted on the delivery
  crate at the base of the rack; behind it a cutaway silicon wafer shaped
  like a transformer diagram with attention arrows drawn on it; magazine
  editorial style, thick outlines, high contrast, readable at 200px
  thumbnail, 1:1 aspect, no real human faces.
image: images/26-08-20-0612-02-etched-700m-21b-sohu-transformer-asic-jane-street.png
---

# Etched ปิด $700M @ $21B — valuation เท่าตัวใน 1 เดือน, Jane Street เป็น lead investor และลูกค้าแรกที่รับ rack Sohu ไปใช้จริง

## TL;DR
- **18 ส.ค. 2026** — Etched ระดม Series D **$700M** ที่ valuation **$21B**, lead โดย **Jane Street**
- **Valuation เท่าตัวจาก $10.3B** ที่ set ปลายกรกฎาคม — กระโดดจาก **$5B ในธันวาคม → $21B ในสิงหาคม** ในเวลา 8 เดือน
- Chip ตัวหลักคือ **Sohu** — transformer-specialized ASIC ที่ทำ inference เท่านั้น, Jane Street รับ **first production rack** ไปใช้เทรด quant จริง
- บริษัทมี **~400 คน** (ทีมจาก Nvidia, Broadcom, Google TPU, SK Hynix), มี **signed contracts เกิน $1B**

## เกิดอะไรขึ้น
วันที่ 18 สิงหาคม 2026 **Etched** ประกาศ Series D ที่ **$700M** — round นำโดย **Jane Street** และมี Kleiner Perkins, Sequoia, a16z, Tiger Global, Bain Capital Ventures, Neo, Primary, Stripes, Positive Sum, Blackstone ตาม. Valuation ที่ **$21B** เกือบเท่าตัวจาก **$10.3B** ที่บริษัทระดมได้ปลายกรกฎาคม — และเป็นการเดินทางจาก **$5B ในธันวาคม 2025 มา $21B ใน 8 เดือน** ก้าวเดียว. บริษัทประกาศคู่กับข่าวว่า **ship first production rack ให้ Jane Street** ที่เป็นทั้ง lead investor และลูกค้าแรก

Product ของ Etched คือ **Sohu** — ASIC ที่ออกแบบมาสำหรับ **transformer architecture โดยเฉพาะ** (attention, feedforward, layer norm burned เข้า silicon แทนที่จะ programmable แบบ GPU). Bet ทั้งบริษัทวางบนสมมติฐานว่า transformer จะครอง architecture ไปอีกหลายปี — ถ้าถูกก็จะเร็วกว่า/ถูกกว่า GPU มาก, ถ้าผิด (architecture ใหม่มาแทน) chip นี้จะกลายเป็นขยะ. บริษัทก่อตั้งปี 2022 โดย **Gavin Uberti, Chris Zhu, Robert Wachen** — Harvard dropouts, ตอนนี้มีทีม **~400 คน** ดึงมาจาก Nvidia, Broadcom, Google TPU, SK Hynix

**Jane Street** เป็น proof point ที่หนักที่สุดในดีลนี้: ไม่ใช่แค่ VC ที่ใส่เงิน แต่รับ **production hardware ไป deploy จริง** ใน workload trading — เท่ากับ signal ว่า chip ผ่าน integration test ในระดับ mission-critical แล้ว. บริษัทอ้าง **signed contracts เกิน $1B** สะสม, ซึ่งเทียบกับ Nvidia (quarterly datacenter revenue **>$30B**) ยังเล็ก แต่เทียบกับ Cerebras, SambaNova, Groq (peer inference chip startups) นับว่าโตเร็ว

## ทำไมสำคัญ
Pattern ที่กำลังชัดขึ้นเรื่อย ๆ ในปี 2026 คือ **inference infrastructure กำลังแตกออกจาก training infrastructure** — เพราะ **workload agent-native ต่างจาก workload chat/model-training** อย่างพื้นฐาน. Agent ตัวเดียวอาจ call model 500 ครั้งใน 30 วินาที (planning, tool selection, self-review, verification), และ **latency ต่อ call กระทบ UX โดยตรง**. Chip ที่ specialize inference — Etched, Groq, Cerebras — จึง reposition ตัวเองเป็น "agent compute" ไม่ใช่ "inference chip" อีกต่อไป

Valuation multiple **2x ใน 30 วัน** และ **4.2x ใน 8 เดือน** บอกอย่างอื่น: private market ยัน re-price stack ทั้งชั้น — ที่ Stripe ซื้อ OpenRouter **$7B** เมื่อสัปดาห์ที่แล้ว, Fireworks ระดม **$1.505B**, Together **$800M** ในเดือนเดียวกัน. รวมกับ Etched ก็เกือบ **$3B** ในหนึ่งเดือนแค่สาย inference/routing — สัญญาณว่า tier ระหว่าง agent runtime กับ raw silicon กำลังกลายเป็น battleground ต่อไป

ที่ควรระวังคือ **transformer bet** — ถ้า architecture ใหม่ (state-space, diffusion, MoE hybrid ที่ break assumption ของ attention) มาแทน, chip ที่ hardwire transformer จะกลายเป็นภาระ. Etched pitching ว่า transformer จะครอง 5-10 ปี — market ที่ให้ **$21B** valuation ก็ pricing สมมติฐานนี้เข้าไปแล้ว. Bet ใหญ่, upside ก็ใหญ่, downside ก็เจ็บ

## มุม AI Agent Platform
สำหรับ **Builders** ที่กำลังสร้าง agent framework/orchestration: ถึงจุดที่ต้องเริ่ม **abstract inference backend** ให้เปลี่ยน chip ได้โดยไม่ต้องแตะ agent logic — เพราะ Sohu, Groq LPU, Cerebras WSE-4, Nvidia B200 มี latency/cost profile ต่างกันมาก, และ agent framework ที่ optimize สำหรับ chip เดียวจะแพ้ agent ที่ route by capability. LangGraph, Vercel AI SDK ที่มี provider abstraction อยู่แล้วมี leverage — ใครที่ hardcode Nvidia CUDA ระดับลึกจะทน pain ตอน migrate

สำหรับ **Users / business** ที่ deploy agent ใน workflow: ราคาต่อ **token กำลังจะลงอีก 5-10x** ในสาย transformer inference ใน 12-18 เดือนถ้า Sohu deliver ตามที่ claim — คำถามคือ agent workload ของธุรกิจตัวเองจะ latency-bound หรือ cost-bound มากกว่ากัน (chip specialty แต่ละยี่ห้อชนะคนละสถานการณ์). สำหรับ **ecosystem** — Nvidia ที่ครอง training market แน่นอนต้องเริ่มถามว่า **inference จะแยกออกไปกี่ %** เพราะทุกครั้งที่ startup อย่าง Etched คว้าดีล enterprise ได้ ก็คือ share ที่ Nvidia เสียในสาย agent-native. AWS Trainium/Inferentia และ Google TPU ที่ vertically integrated จะได้เปรียบตรงที่ **bundle ทั้ง chip + runtime + agent framework** ได้ในสัญญาเดียว — คำถามใหญ่คือ Etched จะทำ vertical stack ของตัวเองไหมหรือขาย chip เดี่ยว

## Sources
- [Etched Raises $700M at a $21B Valuation and Completes First Customer Delivery to Jane Street — GlobeNewswire](https://www.globenewswire.com/news-release/2026/08/18/3347095/0/en/etched-raises-700m-at-a-21b-valuation-and-completes-first-customer-delivery-to-jane-street.html)
- [Etched Raises $700M Series D at $21B Valuation to Ramp Inference Hardware Production — Unite.AI](https://www.unite.ai/etched-raises-700m-series-d-at-21b-valuation-to-ramp-inference-hardware-production/)
- [Inference chip startup Etched raises $700m, doubles valuation to $21bn — Data Center Dynamics](https://www.datacenterdynamics.com/en/news/inference-chip-startup-etched-raises-700m-doubles-valuation-to-21bn/)
- [Inference chip startup Etched raises another $700M at $21B valuation — SiliconANGLE](https://siliconangle.com/2026/08/18/inference-chip-startup-etched-raises-another-700m-at-21b-valuation/)

---

## Audio script
วันที่ 18 สิงหาคมที่ผ่านมา Etched ระดมทุน Series D 700 ล้านดอลลาร์ที่ valuation 21 พันล้าน lead โดย Jane Street. Valuation เท่าตัวจาก 10.3 พันล้านที่ set ปลายกรกฎาคม และเป็นการเดินทางจาก 5 พันล้านในธันวาคมมา 21 พันล้านใน 8 เดือน. จุดที่หนักคือ Jane Street เป็นทั้ง lead investor และรับ first production rack ไป deploy จริงใน trading workload — เท่ากับ chip ผ่าน integration test ในระดับ mission-critical แล้ว. Product คือ Sohu — ASIC ที่ออกแบบมาสำหรับ transformer architecture โดยเฉพาะ ถ้า transformer ครอง 5-10 ปีตามที่ Etched pitch ก็จะเร็วกว่า GPU มาก ถ้าผิดคือ architecture ใหม่มาแทน chip นี้จะกลายเป็นขยะ. Pattern ที่ชัดคือ inference infrastructure กำลังแตกออกจาก training เพราะ workload agent-native ต่างกันโดยพื้นฐาน. Agent ตัวเดียวอาจ call model 500 ครั้งใน 30 วินาที latency ต่อ call กระทบ UX โดยตรง. รวมกับที่ Fireworks ระดม 1.5 พันล้าน Together 800 ล้าน Stripe ซื้อ OpenRouter 7 พันล้านในเดือนเดียวกัน tier ระหว่าง agent runtime กับ raw silicon กำลังกลายเป็น battleground ต่อไป. สำหรับ builder ควรเริ่ม abstract inference backend ให้เปลี่ยน chip ได้โดยไม่ต้องแตะ agent logic. สำหรับธุรกิจราคาต่อ token กำลังจะลงอีก 5-10 เท่าใน 12-18 เดือนถ้า Sohu deliver ตามที่ claim.
