---
date: 2026-05-06
slug: nova-intelligence-315m-sap-migration-agentic
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: A massive abstract glass tower labeled with the bold cream sans-serif text 'SAP' rises from the lower-right of a deep navy editorial frame, weathered with cracked legacy code lines snaking across its surface. A swarm of small geometric robotic agent silhouettes in teal flow upward along scaffolding around the tower, replacing each cracked code segment with clean glowing blue glyphs as they ascend. A bold cream sans-serif headline 'S/4HANA' floats top-left, with '$89B' rendered very large in coral on the lower-left edge. Editorial illustration, flat geometric shapes with subtle gradients, slate blue + teal + coral + cream palette on deep navy background, dramatic uplighting from the base of the tower.
image: images/26-05-07-0612-03-nova-intelligence-315m-sap-migration-agentic.png
---

# Nova Intelligence ระดม $31.5M — เคลม 75% manual reduction บน SAP migration $89B wave

## TL;DR
- Nova Intelligence ปิด Series A $31.5M นำโดย Chemistry total funding รวม $40M+ — agentic AI สำหรับ migrate ABAP legacy code ของ SAP ไป S/4HANA
- ตลาดล็อกตายตัวด้วย deadline บังคับของ SAP ปี 2030 — analyst ประเมินขนาด $89B รวม implementation, upgrade, และ ongoing support
- Case study ของ Kyndryl เม.ย. 25 อ้างลด manual effort 75% และ cost 50% ในการ modernize SAP platform ของลูกค้าหนึ่งราย — ตัวเลขจากบริษัท ยังไม่มี independent benchmark

## เกิดอะไรขึ้น

5 พ.ค. 2026 Fortune ปล่อย exclusive — Nova Intelligence จาก San Francisco ปิด Series A $31.5M นำโดย Chemistry venture firm รวม total funding ขึ้นเป็น $40M+ บริษัทก่อตั้งโดย Emma Qian (CEO เดิมจาก SAP labs) ทำ agentic AI ที่ parse, ทำความเข้าใจ และ rewrite custom ABAP code ที่รันอยู่ใน SAP environment ของ Fortune 500 ลูกค้า ABAP เป็นภาษา proprietary ของ SAP ที่เก่า 40 ปี ยังขับเคลื่อน payroll, supply chain, finance ของบริษัทใหญ่ทั่วโลก

ที่ทำให้ timing ของรอบนี้สำคัญคือ deadline — SAP กำหนดให้ลูกค้า migrate จาก ECC (legacy) มา S/4HANA ภายในปี 2030 ไม่งั้น mainstream support จะดับ ตลาดที่ถูกบังคับให้ขยับนี้ analyst ประเมินมูลค่า $89B รวม implementation cost, upgrade fees และ ongoing managed service Nova Intelligence จึงอยู่ในตำแหน่งของ "vertical AI agent" ที่ตลาดถูก mandate ให้เกิด ไม่ใช่ตลาดที่ต้อง educate

ฝั่ง technical Nova claim ว่า agent ของบริษัท parse ABAP legacy → translate เป็น cloud-compliant S/4HANA code → run automated test → iterate refine จนกว่าจะ pass — เป็น end-to-end coding agent ไม่ใช่แค่ copilot ที่แนะนำ snippet Case study ที่บริษัทนำเสนอคือ collaboration กับ Kyndryl เม.ย. 2025 ซึ่งอ้างว่าลด manual effort 75% และ cost 50% ในการ modernize SAP platform ของลูกค้ารายหนึ่ง — ตัวเลขทั้งสอง "บริษัทอ้าง" ยังไม่มี independent third-party verification แต่ Kyndryl ลงนาม strategic partnership อย่างเป็นทางการ ส่งสัญญาณว่าพอ replicate ได้ใน pipeline service จริง

ในงาน announcement Qian บอกว่า Nova มี F500 ลูกค้า "early double-digit" และ pipeline จะปิดดีลใหม่ทุกอาทิตย์ — ไม่เปิดเผยตัวเลข revenue แต่บอก Chemistry investor lead เห็น contract value pipeline เกินค่า ARR ปัจจุบันหลายเท่า

## ทำไมสำคัญ

Nova เป็น case study ตำราเลยว่า "vertical agentic AI ที่จะชนะ คือตัวที่เกาะ regulation/deadline ที่ขยับไม่ได้" — ต่างจาก horizontal coding agent (Cursor, Cognition Devin) ที่ต้องสู้ใน TAM ที่ทุกบริษัทเลือกใช้ Cursor หรือไม่ก็ได้ Nova เลือกตลาด ABAP migration ที่ลูกค้าไม่มี option จะไม่ migrate — และ ABAP เป็นภาษาที่ engineer สมัยใหม่ไม่เขียน บริษัทใหญ่ส่วนมากจ้าง consultant 100 คน $300/hr ทำ 18 เดือน Nova เสนอ agent ทำใน fraction of time + cost — ROI ชัดถึงขนาดที่ procurement กล้าเซ็น MSA ใน 2 quarter

ที่น่าสนใจคือ Kyndryl partnership — Kyndryl เป็น IBM service spin-off ที่มี SAP practice ใหญ่อยู่แล้ว แทนที่ Kyndryl จะกลัว disintermediation จาก agent เขาเลือกมา revsharing กับ Nova เพราะรู้ว่า labor arb ของตัวเองกำลังถูกเครื่องตัด — สู้ไม่ได้ก็ join ราคา hourly billable ต่อหัวจะต้องลด แต่ deal size รวมจะเพิ่มเพราะลูกค้าเลือกทำ migration ที่ก่อนหน้านี้ไม่กล้าเริ่ม นี่คือ pattern ที่จะเห็นใน Accenture, Deloitte, EY ในอีก 12-18 เดือน — service firm ที่ adapt เร็วจะกลายเป็น GTM partner ของ vertical agent startup ส่วนที่ไม่ adapt จะโดน margin บีบ

ตัวเลข 75% manual reduction ต้องมอง skeptical หน่อย — เป็นตัวเลขจาก case study เดียว ของ partner ที่อยากให้ดีลสำเร็จ ตอน scale ขึ้น 100 ลูกค้า ABAP ของแต่ละ Fortune 500 มี customization ที่ unique มาก ไม่ใช่ pattern matching ง่าย ๆ แต่แม้ลด reduction ไป 50% ก็ยังเป็น value proposition ที่ขายได้

## มุม OpenBridge

ไม่ direct เกี่ยว แต่มี adjacent insight สามจุด: หนึ่ง — pattern "vertical agent + regulatory mandate" ใช้ได้กับหลายตลาด เช่น TFRS 18 ในไทยกำลังบังคับ implementation, ภาษี e-Tax invoice ของ RD, e-Withholding tax — ใครสร้าง agent ที่ automate compliance migration เหล่านี้ มี TAM ที่ procurement จ่ายแน่ สอง — Nova ใช้ agent ที่ "iterate test until pass" ซึ่งต้องการ test infrastructure แข็งแรง OpenBridge connector ที่ทดสอบจริงต่อ external API ได้แบบ replayable เป็น primitive ที่ vertical agent หลายตัวจะอยากใช้

สาม — ที่สำคัญที่สุดคือ lesson ฝั่ง GTM: Nova ไม่ขายตัวเองเป็น "AI for SAP" แต่ขายเป็น "75% เร็วกว่า ที่ครึ่งหนึ่งของ cost" — ภาษา outcome-based ไม่ใช่ technology-based ถ้า OpenBridge อยากสื่อสารกับ enterprise buyer ที่ไม่ใช่ technical — แทนที่จะพูดว่า "integration platform with N connectors" ต้องเปลี่ยนเป็น "ลด time-to-integrate จาก 6 สัปดาห์เหลือ 2 วัน" หรือ "ROI within Q1" ทำให้ procurement หยิบเอกสารส่งบอร์ดได้

## Sources
- [Exclusive: Nova Intelligence raises $31.5 million to bring agentic AI to SAP's $89 billion migration wave | Fortune](https://fortune.com/2026/05/05/exclusive-nova-intelligence-ai-sap-chemistry-emma-qian/)
- [Nova Intelligence — Agentic AI for SAP Modernization](https://www.novaintelligence.com/)
- [Kyndryl and Nova Intelligence Announce Strategic Collaboration to Accelerate SAP Transformation](https://www.prnewswire.com/news-releases/kyndryl-and-nova-intelligence-announce-strategic-collaboration-to-accelerate-sap-transformation-for-customers-302522156.html)
- [Nova Intelligence raises $31.5M Series A led by Chemistry | Shopifreaks](https://www.shopifreaks.com/nova-intelligence-raises-31-5m-series-a-led-by-chemistry-to-bring-agentic-ai-to-saps-89b-migration-wave/)

---

## Audio script
เรื่องที่สาม Nova Intelligence จาก San Francisco ปิด Series A $31.5 ล้าน นำโดย Chemistry รวม total $40 ล้านขึ้น CEO Emma Qian มาจาก SAP labs เดิม สร้าง agentic AI ที่ parse code ABAP เก่า ๆ ของ SAP แล้วแปลเป็น code ใหม่ที่รันบน S/4HANA ได้

ที่ timing นี้สำคัญคือ SAP บังคับให้ลูกค้าต้อง migrate จาก ECC ไป S/4HANA ภายในปี 2030 ไม่งั้น support ดับ analyst ประเมินตลาดนี้ที่ $89 พันล้านเหรียญ รวมค่า implementation upgrade managed service Nova เลยอยู่ในตำแหน่ง vertical agent ที่ตลาดถูก mandate ไม่ต้อง educate ลูกค้าก่อน

case study กับ Kyndryl เม.ย.ที่ผ่านมาบอกว่าลด manual effort 75% ลด cost 50% ตัวเลข บริษัทอ้าง ยังไม่มี third-party verify แต่ Kyndryl เซ็น strategic partnership แล้ว ส่งสัญญาณว่าทำซ้ำได้

pattern ที่น่าจับคือ vertical agent ที่ชนะคือตัวที่เกาะ regulation หรือ deadline ที่ขยับไม่ได้ Cursor Devin ต้องสู้ตลาดเปิด แต่ Nova ลูกค้าไม่มี option ไม่ migrate อันนี้ใช้ได้กับไทยด้วย เช่น TFRS 18 หรือ e-Tax e-Withholding tax — ใครทำ agent automate compliance ของพวกนี้ procurement จ่ายแน่

มุม OpenBridge ไม่ direct แต่ lesson ฝั่ง GTM สำคัญ Nova ไม่ขายตัวเองว่า AI for SAP แต่ขายเป็น 75 percent เร็วกว่า half cost ภาษา outcome-based เราควรเปลี่ยนจาก integration platform with N connectors เป็น ลด time-to-integrate จาก 6 สัปดาห์เหลือ 2 วัน เพื่อให้ procurement หยิบเอกสารเข้าบอร์ดได้ครับ
