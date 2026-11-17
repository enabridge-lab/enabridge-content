---
date: 2026-11-18
slug: kindo-30m-agent-control-center
topic: openbridge-trend
reading_time_min: 3
sources: 4
image_prompt: |
  An editorial isometric illustration of a corporate mission-control room
  with a giant wall of glowing dashboards. Each dashboard shows an agent
  running in a different department: SECURITY, IT, FINANCE, COMPLIANCE.
  In the center, a large hex panel labeled "KINDO CONTROL CENTER" tracks
  three stacked numbers: "$30M FUNDING", "800% YoY REVENUE", "ANY AGENT,
  ANYWHERE". Chart lines snake across the wall tracking "TOKEN SPEND" and
  "FAILED ACTIONS". Clean editorial style, graphite and bright coral palette,
  high contrast so numbers stay readable at 200px thumbnail, 1:1 aspect,
  no real human faces (silhouettes OK).
image: images/26-11-18-0605-05-kindo-30m-agent-control-center.png
---

# Kindo ได้ $30M — AI Control Center สำหรับคุม agent "ทุกตัว ทุกทีม" และอ้าง revenue โต 800% ปีเดียว

## TL;DR
- Kindo ปิดรอบ $30M เมื่อ 12 พ.ย. co-led โดย Crosspoint Capital + Forgepoint Capital รวม funding $57.6M
- ชูตัวเองเป็น "AI Control Center" ให้ Security/IT/Compliance/Finance เห็น + คุม agent ทุกตัวในองค์กร ไม่ว่าสร้างใน Kindo หรือ 3rd party
- อ้าง revenue โต 800% YoY ปี 2026 — ถ้าจริง สะท้อนว่า budget สำหรับ agent governance กำลังแยกออกจาก agent build budget

## เกิดอะไรขึ้น
วันที่ 12 พฤศจิกายน Kindo ประกาศปิดรอบ financing $30M co-led โดย Crosspoint Capital กับ Forgepoint Capital รวม funding $57.6M แล้ว ซึ่งต่อยอดจาก Series A $20.6M ที่ปิดโดย Drive Capital เมื่อกรกฎาคม 2024 — บริษัทไม่ยอมให้รอบนี้เป็น Series B อย่างเป็นทางการ เรียกเป็น "financing expansion" เฉย ๆ ซึ่งมักแปลว่า valuation ยังไม่ขยับขึ้นมากพอจะ reset — แต่ระบุว่า revenue โตประมาณ 800% ปีต่อปี (ตัวเลขของบริษัทเอง ยังไม่มี third party verify)

Product ที่ Kindo ขายคือ "AI Control Center" — single pane of glass ให้ CISO, head of IT, compliance officer กับ CFO เห็นว่าในองค์กรตัวเอง มี agent วิ่งอยู่กี่ตัว ใช้ model อะไร เรียก tool ไหนบ้าง คิด token เท่าไหร่ ล้มเหลวที่ step ไหน จุดต่างคือ platform ไม่ได้ขึ้นอยู่กับว่า agent ถูกสร้างใน Kindo หรือเปล่า — agent จาก LangChain, Cursor, AutoGen, in-house script ก็ครอบคลุม ตราบใดที่ instrument ด้วย SDK ของ Kindo นอกจากนั้น Kindo ยังมี model suite ของตัวเองชื่อ Deep Hat ที่ใช้ wrap request ของ agent เพื่อ enforce policy

เงินที่ได้จะไปสองก้อนหลัก — go-to-market กับ platform development ของ Control Center บวก Deep Hat suite บริษัทไม่เปิดเผยจำนวนลูกค้า แต่ถ้า growth 800% จริง และปี 2024 มี customer base ขนาดใดก็ตาม ปีนี้ต้องแตะ 3-digit อย่างต่ำ ถึงจะ justify Crosspoint กับ Forgepoint ที่โดยปกติไม่ลงก่อน pattern ของ ARR scale

## ทำไมสำคัญ
Pattern ที่เห็นในสองเดือนที่ผ่านมา — CrowdStrike ซื้อ Fiddler + Dreadnode, Sentra ได้ $150M, Kindo รอบนี้ — คือ budget สำหรับ "คุม agent" กำลังแยกออกมาจาก budget ที่ใช้ "สร้าง agent" ชัดเจน องค์กรที่ deploy agent ไป 20-50 ตัวแล้ว เริ่มเห็นปัญหาจริง agent วิ่งแล้ว token spend ทะลุงบ โดยไม่มีใครรู้ว่าอะไรวิ่งอยู่, compliance team ไม่สามารถตอบ audit ได้ว่าใครใช้ data อะไร, และ agent fail แล้วไม่มีใครรู้ว่า fail ที่ไหน

Kindo เล่นเกม control-plane ซึ่งเป็น position ที่น่าสนใจ — เพราะไม่ได้แข่งกับ Agentforce หรือ Joule โดยตรง แต่ complement งาน ของมันคือ "ไม่ว่าคุณจะใช้ platform อะไร ผม observe ได้" ซึ่งคล้ายตำแหน่งที่ Datadog ยึดในยุค microservices คำถามใหญ่คือ incumbent อย่าง Datadog, New Relic, Splunk จะ build ของตัวเองมาแข่งทัน หรือจะยอมให้ Kindo กับเพื่อน ๆ (Sentra, Fiddler) เป็นเจ้าของ category นี้

สำหรับธุรกิจ นี่คือสัญญาณว่าถ้าตอนนี้องค์กรยังตามจำนวน agent ไม่ไหว อย่ารอเร็ว ๆ นี้ — pattern ของ "agent sprawl" จะชัดกว่า cloud sprawl ยุค 2015 เพราะ agent คิด cost แบบ per-token ไม่ใช่ per-instance การไม่มี control plane แปลว่า CFO จะเจอ bill ที่อธิบายไม่ได้ใน 2-3 ไตรมาสข้างหน้า

## มุม AI Agent Platform
สำหรับ **Builders** — ถ้าคุณสร้าง agent platform ของตัวเอง ควรออกแบบ observability hook ให้ Kindo (หรือเพื่อน ๆ ใน category นี้) ดึง telemetry ได้ตั้งแต่วันแรก การ lock-in ลูกค้าด้วยการปิด observability จะกลายเป็น anti-pattern เร็วกว่าที่คิด เพราะ CISO กับ CFO จะไม่ approve platform ที่เขาเห็นไม่ครบ ส่วน vertical agent ที่ runtime อยู่ที่ตัวเอง — ประเมินว่า telemetry layer จะสร้างเองหรือ outsource ให้ Kindo-class vendor

สำหรับ **Users / business** ที่กำลัง deploy agent — ให้ประเมินว่าใน 6-12 เดือนข้างหน้าองค์กรคุณจะมี agent กี่ตัว ถ้าคำตอบคือเกิน 10 ตัว และคุณยังไม่มีคำตอบว่าใครจะ monitor cost + policy — Kindo กับเพื่อน ๆ ควรอยู่ใน shortlist ของ POC ควบคู่กับการประเมินว่า Datadog หรือ incumbent ของคุณจะปล่อย module แข่งทันเมื่อไหร่ ส่วนราคา per-seat ของ control plane ควรคิดเป็น 5-10% ของ total agent spend เป็น baseline

## Sources
- [Kindo Raises $30 Million to Expand Enterprise AI Agent Control and Reduce Costs — Unite.AI](https://www.unite.ai/kindo-30-million-enterprise-ai-agent-control/)
- [Kindo raises $30M to give enterprises control over AI agents — Dealroom](https://dealroom.co/news/172293-kindo-raises-30m-to-give-enterprises-control-over-ai-agents/)
- [Kindo Raises $30 Million In Funding — Tech Company News](https://www.techcompanynews.com/kindo-raises-30-million-in-funding/)
- [Kindo raises $30M after 800% revenue growth — News.DropsTab](https://news.dropstab.com/aggregator/ngnc0sjy-kindo-raises-usd30m-after-800-revenue-growth-can-one-control-center-tame-enterprise-ai-agents)

---

## Audio script
Kindo สตาร์ตอัปที่ขายตัวเองเป็น AI Control Center เพิ่งได้เงินเพิ่มสามสิบล้านดอลลาร์ co-led โดย Crosspoint Capital กับ Forgepoint Capital รวม funding ห้าสิบเจ็ดล้าน บริษัทอ้างว่า revenue โตแปดร้อยเปอร์เซ็นต์ปีต่อปี ซึ่งถ้าจริงสะท้อนว่า budget สำหรับคุม agent กำลังแยกจาก budget ที่ใช้สร้าง agent ชัดขึ้นเรื่อยๆ

ตัว product คือ dashboard สำหรับ CISO, head of IT, compliance กับ CFO ให้เห็นในองค์กรตัวเองว่า agent วิ่งอยู่กี่ตัว ใช้ model อะไร เรียก tool ไหน คิด token เท่าไหร่ ล้มเหลวที่ไหน จุดต่างคือ agent ไม่ต้องถูกสร้างใน Kindo ก็ cover ได้ ตราบใดที่ instrument ด้วย SDK Pattern ที่เห็นในสองเดือนนี้ชัดว่า agent sprawl กำลังจะเป็น cloud sprawl เวอร์ชันใหม่ และเร็วกว่าเดิม เพราะ agent คิดค่าแบบ per-token ไม่ใช่ per-instance สัญญาณสำหรับ builders คือออกแบบ observability hook ให้ Kindo-class vendor ดึง telemetry ได้ตั้งแต่วันแรก สำหรับ enterprise ถ้าคุณจะมี agent เกินสิบตัวในหกถึงสิบสองเดือนข้างหน้า ต้องมี control plane ใน shortlist ของการประเมิน budget 5-10% ของ total agent spend ถือเป็น baseline ของ category นี้
