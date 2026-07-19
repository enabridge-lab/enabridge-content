---
date: 2026-07-19
slug: fireworks-1-5b-series-d-specialized-intelligence
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  A dark server room split down the middle by a bright vertical divider;
  left side shows a single glowing generic model orb, right side shows dozens
  of small specialized model chips arranged in a grid, each glowing in a
  different warm color. Three bold headlines float above: "$1.5B RAISED",
  "$17.5B VALUATION", "95% SPECIALIZED". Editorial isometric style, deep
  navy background with amber highlights, sharp typography readable at 200px
  thumbnail, 1:1 aspect, no real human faces.
image: images/26-07-19-0609-02-fireworks-1-5b-series-d-specialized-intelligence.png
---

# Fireworks ได้ $1.5B ที่ valuation $17.5B — เดิมพันว่า agent runtime อนาคตคือ "specialized" ไม่ใช่ "frontier"

## TL;DR
- **Fireworks AI** ปิด Series D **$1.505B** ที่ valuation **$17.5B** — นำโดย Atreides Management, Index Ventures และ TCV (16 กรกฎาคม)
- **ARR run rate ทะลุ $1B** — โต 5x YoY, daily token volume เพิ่มจาก 15T เป็น **40T token/วัน**
- **95% ของ token ที่ Fireworks serve เป็นโมเดล specialized** — ไม่ใช่ closed frontier general-purpose อีกต่อไป
- ลูกค้าใหญ่: Uber, Shopify, Doximity, Elastic, GitLab, MongoDB, Harvey AI, Cursor

## เกิดอะไรขึ้น
วันพฤหัสบดี Fireworks ประกาศ Series D $1.505B ที่ valuation $17.5B — round นำโดย Atreides Management, Index Ventures และ TCV โดยมี Evantic, Lightspeed และ NVIDIA ลง reup. ตัวเลขที่มาพร้อมกันคือหัวใจของ deal: ARR run rate ทะลุ 1 พันล้านดอลลาร์ โต 5 เท่าเทียบปีก่อน; token volume ต่อวันขยับจาก 15 ล้านล้านเป็นกว่า 40 ล้านล้าน. ในระดับที่ platform เดียวส่ง 40T token/วัน Fireworks ใหญ่กว่า OpenAI API ในช่วงต้นปี 2024 ทั้งหมด

Thesis ของบริษัทชัดในสองบรรทัด: **customer นำโมเดล open ของตัวเองมา, Fireworks ช่วย fine-tune บน proprietary data ให้กลายเป็น "specialized intelligence"** ที่ทำ specific task ได้ดีกว่าหรือเท่า closed frontier แต่ **ราคาถูกกว่ามากและเร็วกว่ามาก**. 95% ของ token ทั้งหมดที่ platform serve มาจากโมเดลที่ผ่านการ specialize แล้ว — ไม่ใช่ base model, ไม่ใช่ Claude/GPT ที่เรียกผ่านเท่านั้น. เม็ดเงิน round นี้จะไปที่ compute infrastructure, engineering team และ deeper partnership กับ Microsoft และ NVIDIA

รายชื่อลูกค้าเล่า story ของตัวเองได้เกือบครบ: Uber (agent สำหรับ operational routing), Shopify (agent สำหรับ merchant workflow), Doximity (clinical summarization), Elastic (search ranking), GitLab (code review), MongoDB (schema-aware querying), Harvey AI (legal), Cursor (coding). ทุกเจ้า common pattern: มี **proprietary data** ที่ทำให้ closed frontier ไม่ได้เปรียบพอ และ **latency + cost** ที่ต้อง predictable เพราะเป็น production workload

## ทำไมสำคัญ
กราฟที่ Fireworks กำลังพิสูจน์คือ **cost curve ของ inference กำลังบังคับให้ frontier ต้องถูก unbundle**. คลื่นแรกของ agent (2023–2024) รัน GPT-4 หรือ Claude ผ่าน API เพราะเป็น cheapest way to prototype. แต่พอ agent เข้า production 10K+ ครั้ง/วัน per customer ตัวเลข API bill กลายเป็น cost center อันดับหนึ่ง — ทีมที่มี data + engineering ก็ specialize model 7B–70B ของตัวเองแทน. Fireworks ขายเครื่องมือ specialize + ที่รันโมเดลนั้น 24/7 ที่ throughput ระดับ enterprise

Signal ที่ควรอ่านคือ **Lightspeed + NVIDIA reup**. NVIDIA มีข้อมูล inference workload ทั้ง industry ผ่าน CUDA + Nemo + DGX Cloud — การที่ NVIDIA ยังลง Fireworks ต่อ แสดงว่า internal data ของเขาสอดคล้องกับ thesis "specialized wins majority of token volume". Lightspeed ที่นำ Series C มาก่อนได้ upside ระดับ 3–4x ใน 12 เดือน — โดยไม่ต้องเปลี่ยน thesis เลย

เทียบ landscape: Together AI, Baseten, Replicate, Anyscale ต่างขายชิ้นส่วนใกล้กัน; แต่ Fireworks เป็นเจ้าเดียวที่ประกาศ $1B ARR + 40T token/วัน. Together เพิ่งระดม $305M ปีก่อนที่ valuation $3.3B — gap ระหว่างสองบริษัทถ่างขึ้นเร็วมาก. คำถามคือใครเป็น Cloudflare กับใครเป็น Fastly ของ agent runtime era — Fireworks ตอนนี้อยู่ตำแหน่งของ Cloudflare อย่างชัดเจน

## มุม AI Agent Platform
**Builders** ที่ build agent บน closed frontier API ควรเริ่ม architect ให้ swap runtime ได้ — เพราะ 6–12 เดือนข้างหน้า cost pressure จะบีบให้ต้อง fine-tune model 7B–70B แทน call to GPT-5 หรือ Claude Opus. **Users / business** ที่มี proprietary data (medical, legal, financial, industrial) จะได้เปรียบ: Fireworks ทำให้ specialize model ราคาถูกลงเรื่อย ๆ, competitive edge ของ data owner ขึ้นชัด. **Ecosystem** — ผู้เล่นที่ทับซ้อน (Modal, Baseten, Together) จะต้องเลือก vertical หรือ merge; hyperscaler (AWS Bedrock, Azure AI Foundry) จะเห็น customer นำ specialized model บน Fireworks มาชนกับ managed frontier ของตัวเอง — และเสียง revenue mix จะบีบให้ต้องออก specialization tooling ของตัวเอง

## Sources
- [Fireworks Secures $1.5 Billion in Series D Funding (Company Blog)](https://fireworks.ai/blog/series-d-announcement)
- [Fireworks Raises a $1.5 Billion Series D to Lead the Specialized Intelligence Revolution (BusinessWire)](https://www.businesswire.com/news/home/20260716264405/en/Fireworks-Raises-a-$1.5-Billion-Series-D-to-Lead-the-Specialized-Intelligence-Revolution)
- [AI infrastructure startup Fireworks closes $1.5B round at $17.5B valuation (SiliconANGLE)](https://siliconangle.com/2026/07/16/ai-infrastructure-startup-fireworks-closes-1-5b-round-17-5b-valuation/)
- [Fireworks AI raises $1.5 billion Series D at $17.5B valuation (Quartz)](https://qz.com/fireworks-ai-series-d-fundraise-valuation-open-source-071626)
- [Fireworks AI Series D · $1.5B raised (StartupHub)](https://www.startuphub.ai/investment_rounds/fireworks-ai-series-d-2026)

---

## Audio script
เมื่อวันพฤหัสบดี Fireworks AI ปิด Series D 1,505 ล้านดอลลาร์ ที่ valuation 17,500 ล้านดอลลาร์ นำโดย Atreides, Index Ventures และ TCV โดย Lightspeed กับ NVIDIA ที่เคยลงมาก่อนก็ลงเพิ่ม. ตัวเลขที่ตามมาสำคัญมาก — ARR run rate ของบริษัททะลุ 1 พันล้านดอลลาร์แล้ว โตห้าเท่าเทียบปีก่อน daily token volume ขยับจาก 15 ล้านล้านเป็นกว่า 40 ล้านล้านต่อวัน. Fireworks ไม่ใช่ผู้ให้บริการโมเดล closed frontier — thesis ของเขาคือ 95% ของ token ที่ platform serve มาจากโมเดลที่ลูกค้าเอา open weight มา fine-tune บนข้อมูลของตัวเอง กลายเป็นสิ่งที่บริษัทเรียกว่า specialized intelligence — ทำงาน specific ได้ดีกว่าหรือเท่ากับ GPT กับ Claude ในราคาถูกกว่ามากและ latency ต่ำกว่ามาก. รายชื่อลูกค้ามี Uber, Shopify, Doximity, Elastic, GitLab, MongoDB, Harvey AI และ Cursor — ทุกเจ้าใช้ Fireworks รัน agent workload ที่ต้อง predictable ในระดับ production. Story ใหญ่กว่าคือ cost curve ของ inference กำลังบีบให้ทุกทีมที่ scale agent ต้องยอม unbundle จาก closed frontier — เพราะ API bill ระดับหมื่นเรียกต่อวันต่อลูกค้าเดียว กลายเป็น cost center อันดับหนึ่งของทีม. ทีมไหนที่ยังพึ่ง frontier API ล้วน ๆ ควรเริ่ม architect ให้ swap runtime ได้ — เพราะปี 2027 ราคาที่ต้องจ่ายจะเลือกให้แทนแล้ว
