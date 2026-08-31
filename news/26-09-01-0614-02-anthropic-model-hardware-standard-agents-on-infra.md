---
date: 2026-09-01
slug: 26-09-01-0614-02-anthropic-model-hardware-standard-agents-on-infra
topic: agentic-ai
reading_time_min: 5
sources: 3
image_prompt: |
  A lab bench where a microscope, a robotic arm, and a liquid handler are wired
  to a single glowing central hub labeled "MHS"; a translucent overlay reads
  "3× FASTER" over the beakers. Three floating "READ / WRITE" chips connect the
  devices via bright cyan cables. Editorial isometric style, deep navy
  background with amber highlights, big legible sans-serif numbers, readable in
  200px thumbnail, 1:1 aspect, no real human faces.
image: images/26-09-01-0614-02-anthropic-model-hardware-standard-agents-on-infra.png
---

# Anthropic เปิด "Model Hardware Standard" — MCP สำหรับโลกกายภาพ, Carnegie Mellon รัน dose-response เร็วขึ้น 3 เท่า

## TL;DR
- Anthropic ปล่อย **Model Hardware Standard (MHS)** research preview 28 ส.ค. — driver มาตรฐาน 2 คำสั่ง `read` / `write` ให้ agent สั่ง microscope / liquid handler / robotic arm ได้ภายใน "ชั่วโมงถึงนาที" แทน "สัปดาห์ถึงเดือน"
- **Carnegie Mellon ใช้ MHS รัน serial dilution dose-response experiment เร็วขึ้น ~3×** โดย agent orchestrate liquid handler + plate reader + robotic arm + monitor camera บน 3 เครื่องคนละ interface พร้อมกัน
- Model-agnostic เหมือน MCP — ไม่ผูกกับ Claude, spec เก็บ physical characteristic (น้ำหนัก, safety limit, parameter) ที่เคยอยู่แค่ paper manual + tacit knowledge

## เกิดอะไรขึ้น

28 ส.ค. Anthropic เปิด research preview ของ **Model Hardware Standard (MHS)** — ชื่อที่จงใจ echo Model Context Protocol (MCP) แต่ target คนละชั้น: ไม่ใช่การเชื่อม agent กับ software (database, SaaS, API) แต่คือการเชื่อม agent กับ **physical device**. Standard นี้ define driver ที่ **แปลระหว่าง OS ของคอมพิวเตอร์ กับ hardware device ด้วยคำสั่งง่ายแค่ 2 ตัว** — `read` และ `write` — และเก็บ **physical characteristic ของอุปกรณ์** (น้ำหนัก, safety limit, adjustable parameter) ในรูปแบบ machine-readable ที่ไม่เคยมีมาก่อน — ข้อมูลพวกนี้เดิมอยู่แค่ในคู่มือกระดาษหรือ tacit knowledge ของ specialist.

Proof point ที่ทำให้เรื่องนี้ไม่ใช่ vaporware: **นักวิจัยที่ Carnegie Mellon University รัน serial dilution dose-response experiment เร็วขึ้น ~3 เท่า** โดยใช้ agent เดียว orchestrate **liquid handler + plate reader + robotic arm + monitor camera** ที่กระจายอยู่บน **3 เครื่องคอมพิวเตอร์ที่ interface กันไม่ได้เลย** — งาน integration แบบนี้ในปกติต้องมี lab engineer + PhD student นั่งเขียน glue code เป็นเดือน. MHS ทำให้ agent เห็น pool ของอุปกรณ์เป็น interface เดียว. Anthropic บอกว่า reduce integration work จาก "weeks or months to hours or minutes" — และ **spec ไม่ผูกกับโมเดล Anthropic** (ตรงกับ pattern ของ MCP ที่ open sourced ปลายปี 2024 แล้ว OpenAI/Google/Microsoft adopt ตาม).

MHS ยังอยู่ใน research preview — Anthropic บอกว่า **จะ open publicly หลัง preview จบ** แต่ยังไม่ commit วันที่. Use case กลุ่มแรกที่ยกมาคือ **drug discovery** (routine experiment automation), **laser calibration**, และงาน lab automation ทั่วไป. Roadmap ที่ implicit คือ scope กว้างกว่านั้น — factory floor, warehouse robot, scientific instrument fleet — เพราะ pattern ของ driver + physical property ครอบครอบ hardware ประเภทใดก็ตามที่มี programmable control surface.

## ทำไมสำคัญ

MHS คือ **การขยาย addressable surface ของ agent จาก software → hardware** — เทียบสัดส่วน spend ของโลก การ automate physical asset (โรงงาน, ห้อง lab, warehouse, hospital) เป็นตลาดขนาด **หลาย trillion USD** ต่อปี ที่ automation stack ปัจจุบัน (PLC, SCADA, LIMS) ผูกกับ vendor lock-in และ interface กันไม่ได้. ถ้า MHS จริงจริงกลายเป็น standard (แบบที่ MCP กลายเป็น standard สำหรับ software connection ใน 8 เดือน) — **การ integrate ห้อง lab ใหม่ที่มี 20 อุปกรณ์จาก 15 vendor จะเปลี่ยนจากโปรเจกต์ 6-9 เดือน เป็นโปรเจกต์ 2-4 สัปดาห์**. นี่คือ leverage เดียวกับที่ HTTP เปิดให้ software company build บน internet โดยไม่ต้องเจรจา TCP กับแต่ละ ISP.

Pattern ที่น่าจับตาคือ **Anthropic ยึด "protocol layer" อย่างเป็นระบบ**: MCP (Nov 2024, software), MHS (Aug 2026, hardware), Agent Skills API (มิ.ย. 2026), Claude Tag / Slack activation (ก.ค. 2026). ทั้งหมด model-agnostic โดยจงใจ — Anthropic ไม่ได้พยายามชนะเกม distribution แข่ง Meta / OpenAI แต่กำลังยึดตำแหน่ง **"บริษัทที่กำหนด protocol ให้ agent ecosystem"** — ตำแหน่งที่มี moat แบบ TCP/IP era ของ Cisco. เทียบ Google (A2A protocol, Linux Foundation stewardship), OpenAI (ยังไม่มี protocol contribution ใน scale เดียวกัน), และ Microsoft (ผลัก Copilot ตัวเอง + Windows agent runtime) — Anthropic อยู่ในตำแหน่งที่ต่างที่สุด. HPCwire ในบทความ "When Every Machine Becomes an Agent" (31 ส.ค.) เขียนตรงเป้าว่า **AI is moving out of the cloud and into the real world fast** — MHS คือ enabler ของ transition นั้น.

## มุม AI Agent Platform

**สำหรับ builders:** ถ้าคุณ build agent platform ที่ target enterprise ใน manufacturing / pharma / logistics / energy — MHS คือ protocol ใหม่ที่ต้อง **integrate ตั้งแต่วันแรก**, ไม่ใช่รอ. ที่ควรทำเลย: (1) implement MHS driver adapter ให้ agent runtime ของคุณ, (2) build catalog ของอุปกรณ์ที่ทีมลูกค้าใช้บ่อย (mass spec, HPLC, PCR machine, robotic arm 6-DOF ฯลฯ), (3) join research preview เพื่อเข้าถึง spec ก่อน public release. **สำหรับ users / business:** enterprise ใน sector ที่มี physical asset จำนวนมาก (โรงงาน, ห้อง lab, warehouse, hospital, oil rig) ควร inventory อุปกรณ์ที่มี "programmable control surface" — อย่างน้อยเพื่อรู้ว่าถ้า MHS โต 3-5x ในปีหน้า, asset ไหนของเรา automate ได้ด้วย agent, asset ไหนจะกลายเป็น legacy bottleneck. **สำหรับ ecosystem:** vendor ที่ผลิต scientific instrument / industrial robot ที่ยัง lock interface (Waters, Agilent, Beckman, Fanuc, KUKA) จะโดนบีบให้เปิด API — ไม่งั้น customer ของเขาจะเลือก vendor ที่ MHS-compliant ในการซื้อรอบถัดไป. LIMS / MES vendor (LabVantage, Emerson, Rockwell) จะเจอ overlap โดยตรงเพราะ agent runtime + MHS ทำงานที่ orchestration layer ที่พวกเขายึดอยู่.

Enabridge angle: SEA มี **ห้อง lab ที่มหาวิทยาลัย + pharma company + food-tech + agricultural R&D** ที่ integration bar สูงเพราะไม่มี in-house lab automation engineer เท่า US/EU. Product opportunity คือ **"Lab Agent Bundle"** — MHS-compliant runtime + Thai/Bahasa language interface + connector ยอดฮิต (Waters HPLC, Agilent GC, Tecan liquid handler) + template experiment (serial dilution, HPLC analysis, cell counting). Partner ที่คุยได้เลย: จุฬาฯ Faculty of Pharmaceutical Sciences, Mahidol Bioscience, BIOTEC, KKU Ag-Bio. ราคา per experiment run + monthly platform fee, target early revenue $50-200K/customer/yr.

## Sources
- [Previewing the Model Hardware Standard — Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview)
- [Anthropic Model Hardware Standard connects AI to lab equipment — Quartz](https://qz.com/anthropic-model-hardware-standard-ai-robots-lab-equipment-082826)
- [When Every Machine Becomes an Agent — HPCwire/AIwire](https://www.hpcwire.com/aiwire/2026/08/31/when-every-machine-becomes-an-agent/)

---

## Audio script
Anthropic เพิ่งเปิดของใหม่ที่น่าจะสำคัญมากในระยะยาว ชื่อว่า Model Hardware Standard หรือ MHS เป็น research preview ปล่อยเมื่อ 28 สิงหาคม ให้คิดว่ามันคือ MCP เวอร์ชั่นสำหรับโลกกายภาพ MCP เชื่อม agent กับ software เช่น database SaaS API ส่วน MHS เชื่อม agent กับ hardware physical device แบบ microscope liquid handler robotic arm ผ่าน driver มาตรฐาน 2 คำสั่งง่ายๆ read กับ write บวกกับข้อมูลคุณสมบัติทางกายภาพของอุปกรณ์ที่เคยอยู่แค่ในคู่มือกระดาษ proof point แรกคือทีม Carnegie Mellon University รัน serial dilution dose-response experiment เร็วขึ้น 3 เท่า agent เดียว orchestrate liquid handler plate reader robotic arm monitor camera บน 3 คอมพิวเตอร์ที่ interface กันไม่ได้เลย ปกติ integration แบบนี้ใช้เวลาเดือน MHS ลดเหลือชั่วโมงถึงนาที Anthropic ไม่ได้ล็อกกับ Claude เป็น model-agnostic เหมือน MCP pattern ที่เห็นชัดคือ Anthropic กำลังยึดตำแหน่ง protocol layer อย่างเป็นระบบ MCP สำหรับ software MHS สำหรับ hardware Agent Skills API สำหรับ package งาน Claude Tag สำหรับ Slack ไม่แข่ง distribution กับ Meta OpenAI แต่ตั้งใจเป็นบริษัทที่กำหนด protocol ให้ ecosystem สำหรับ Enabridge SEA มี lab ในมหาวิทยาลัยกับ pharma R&D จำนวนมาก opportunity คือ Lab Agent Bundle MHS runtime บวกภาษาไทย บวก connector ที่ใช้บ่อยและ template experiment
