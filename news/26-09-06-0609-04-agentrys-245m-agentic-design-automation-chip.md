---
date: 2026-09-06
slug: agentrys-245m-agentic-design-automation-chip
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  A dramatic factory floor for silicon: rows of glowing chip wafers on conveyor
  belts, each carrying a small robotic AI agent-figure hovering over it with tools
  — magnifier, wrench, schematic pen. A big overhead banner reads "AGENTIC DESIGN
  AUTOMATION" with a subhead "$24.5M". On the wall a scoreboard shows "EDA →
  ADA" with arrow. Ex-NVIDIA silhouette in the foreground. Editorial isometric
  style, cyan and orange chip-fab palette, high thumbnail contrast, 1:1 aspect,
  no real human faces.
image: images/26-09-06-0609-04-agentrys-245m-agentic-design-automation-chip.png
---

# Agentrys ระดม $24.5M สร้าง "Agentic Design Automation" — vertical agent สำหรับ chip design จาก ex-NVIDIA lead, MediaTek เป็น strategic backer

## TL;DR
- **Agentrys** ระดม **$24.5M** รวม — seed $19.1M oversubscribed นำโดย **Etna Labs** + pre-seed $5.4M นำโดย **MediaTek** (strategic backer แรก) ประกาศเมื่อ 26 ส.ค. 2026
- Founder **Mark Ren** เคย pioneer AI for chip design ที่ NVIDIA; product เป็น platform ให้ engineering team **build + own self-improving agentic workforce** สำหรับ chip verification + physical design
- Company กำหนดตัวเองเป็น category ใหม่ **"Agentic Design Automation" (ADA)** — evolution จาก EDA (Electronic Design Automation) ที่ focus per-task tool → intelligent system ที่ automate + learn + continuously improve ทั้ง workflow
- Signal: **vertical agent for critical infrastructure engineering** เป็น sub-thesis ที่ VC เริ่มลงทุนหนัก — ADA / EDA-successor เป็น pattern เดียวกับ **ClinicalOps agent สำหรับ pharma, LegalOps agent สำหรับกฎหมาย, PolicyOps agent สำหรับ compliance**

## เกิดอะไรขึ้น

Agentrys ประกาศระดม $24.5M เมื่อ 26 ส.ค. 2026 — combination ของ seed round oversubscribed $19.1M ที่ Etna Labs นำ + pre-seed $5.4M ที่ MediaTek นำเมื่อต้นปี. การที่ **MediaTek เป็น strategic backer แรก** สำคัญ — MediaTek เป็นหนึ่งใน chip designer ที่ใหญ่ที่สุดในโลก (มือถือ, IoT, ดาต้าเซ็นเตอร์) มี pipeline design ตันตลอด, เท่ากับ Agentrys มี design partner customer ตั้งแต่ pre-launch. Funding จะใช้ recruiting, agent-native tooling, และขยาย customer engagement ในสอง sub-area: **verification** (ตรวจสอบ correctness ของ RTL) และ **physical design** (place-and-route, timing closure).

**Founder Mark Ren** มา background ที่แข็งมาก — เคย lead group ที่ NVIDIA ที่ pioneer การใช้ AI สำหรับ chip design (ตีพิมพ์ paper เรื่อง PrefixRL, DeepPCB, และ NVIDIA's Nemotron for EDA workflow). เขาเห็นด้วยตัวเองว่า **EDA tools ปัจจุบัน (Cadence, Synopsys, Siemens EDA) ยัง focus per-task automation** — engineer ยังต้อง orchestrate workflow ด้วยมือระหว่าง tool, sync ผลลัพธ์, iterate design cycle ที่ยาวเป็นสัปดาห์. Agentrys เสนอ **agent-native platform** ที่ engineering team define goal (functional spec + PPA target) แล้ว agent workforce ประกอบด้วย verification agent, floorplan agent, timing agent, DFT agent — ทำงานร่วมกัน, learn จาก previous project, ปรับ strategy อัตโนมัติ.

Vision ระยะยาวคือ **self-improving AI สำหรับ chip design** — engineering system ที่ learn จาก experience, evolve capability, และ tackle design challenge ซับซ้อนขึ้นเรื่อย ๆ. ในภาษา product คือ Agentrys ต้องการเป็น "Cursor ของ chip design" — แต่ระดับ workflow ไม่ใช่ระดับ file. Category name ที่บริษัทเลือกใช้คือ **Agentic Design Automation (ADA)** ที่ตั้งใจ position ว่าเป็น successor ของ EDA — Semiconductor Digest + SemiWiki เขียนถึงกันว่านี่คือ "next-generation EDA" ที่เป็น thesis ใหม่ที่นักลงทุน semi VC ต้องเข้าใจ.

## ทำไมสำคัญ

Signal ที่สำคัญกว่าตัวเงินคือ **pattern "vertical agent for critical infrastructure engineering"** ที่ VC เริ่มมั่นใจ. เมื่อดูข้าง ๆ:
- **Rebar** (HVAC vertical AI, $14M ที่รายงานในรอบ 26-04-19) — engineering agent สำหรับ mechanical
- **Faro** (pharma agent workflow, Series B ล่าสุด) — engineering agent สำหรับ chemistry/biology
- **Agentrys** — engineering agent สำหรับ silicon

pattern สามตัวนี้บ่งชี้ว่า **vertical agent สำหรับ engineering discipline** (ไม่ใช่ generic office work) เป็น thesis ที่ VC yield กลับ 3-5× ในไตรมาสหน้า. หลักการที่นักลงทุนซื้อ: **(1) domain มี complex sequential workflow ที่ current SaaS แยกกันเป็น tool, (2) engineer มี high hourly cost + shortage, (3) mistake มี cost สูงมาก (respin chip = $10-50M) — agent ที่ทำถูก 90% + surface uncertainty ให้ human ตัดสิน 10% = ROI ที่ CEO อนุมัติได้ทันที**.

ผลกระทบต่อ EDA incumbent (Cadence, Synopsys, Siemens EDA — รวม TAM ~$16B) — คำถามยุทธศาสตร์คือ **buy vs build**. Cadence เพิ่ง acquisitions หลายรอบ (Beta CAE, Rambus SerDes IP) ต้องการ AI-native workflow layer; Synopsys มี Synopsys.ai แต่ยังเป็น per-tool assistant ไม่ใช่ orchestration. หาก Agentrys โต pilot กับ MediaTek + ต่อยอดไป Qualcomm/AMD/MTK-tier customer ภายใน 12 เดือน — **acquisition candidate ที่ $200-500M ในปี 2027**. หาก scale เร็วกว่านั้น (ไปถึง TSMC/Samsung foundry design service unit) — potential IPO trajectory ที่คล้าย Ambiq หรือ Astera Labs.

ที่ใหญ่กว่านั้น: **naming pattern "ADA = Agentic X Automation"** จะซ้ำในทุก vertical ที่มี EDA-analog. LegalOps agent (Harvey, EvenUp, Ironclad) กำลังกลายเป็น "Agentic Legal Automation"; ClinicalOps agent (Nabla, Abridge) → Agentic Clinical Automation; PolicyOps agent (Norm AI, Themis, OneTrust AI) → Agentic Compliance Automation. Enterprise buyer ควร map budget ปี 2027 ตาม vertical-suffix นี้ — งบ per-tool SaaS จะ shift ไป agent-native platform ที่ครอบ workflow ทั้งหมด, มาก่อนขี้เกียจ evaluate ตอนบัดเจ็ตแล้ว lock in vendor ผิด.

## มุม AI Agent Platform

**Builders** — ถ้าคุณสร้าง vertical agent, positioning **"Agentic X Automation"** เป็น narrative ที่ VC + enterprise buyer เข้าใจง่ายกว่า generic "AI agent platform". เลือก vertical ที่มี 3 checklist: (1) มี legacy per-tool SaaS ที่ engineer ต้อง orchestrate ด้วยมือ, (2) hourly cost ของ practitioner สูง (>$100/hr), (3) มี domain-specific eval สำหรับ correctness ที่ทำเป็น automated feedback loop ได้. ADA-analog มีในเกือบทุก B2B vertical.

**Users / Business** — CIO ของ enterprise regulated (semiconductor, pharma, financial services, oil&gas) — ทบทวน tool budget ปี 2027; แยกงบ **agent-native workflow platform** ออกจากงบ per-tool SaaS. อย่ารอให้ workflow orchestration layer สุก 100% — start proof-of-concept ในไตรมาสนี้กับ vertical agent 1-2 ตัว, ทดลอง eval, learn integration pattern ก่อนที่จะ commit multi-year contract กับ incumbent SaaS ที่จะ obsolete ใน 24-36 เดือน.

**Ecosystem** — สำหรับ chip design ecosystem ใน region เอเชีย (TSMC, Samsung, MTK, GUC, Silicon Optix): **ผู้ชนะจะเป็นบริษัทที่ integrate ADA-tier platform เร็วสุด** — cycle time reduction 30-50% = advantage ที่ compound เพราะ Moore's Law slow-down ทำให้ speed-to-tape-out สำคัญกว่า transistor count. สำหรับ Enabridge + platform vendor ในไทย/ภูมิภาค: opportunity สร้าง localized vertical agent สำหรับ industry ที่ US-VC ยังไม่มอง — สุขภาพระดับ region-specific (ASEAN clinical workflow), agriculture, government policy — ที่ moat = local domain expertise ที่ Silicon Valley agent scale ไม่ทัน.

## Sources
- [Agentrys Raises $24.5 Million to Build Agentic Design Automation for Chipmakers (BusinessWire, 26 ส.ค. 2026)](https://www.businesswire.com/news/home/20260826681966/en/Agentrys-Raises-$24.5-Million-to-Build-Agentic-Design-Automation-for-Chipmakers)
- [Follow the Money – Agentrys Raises $24.5 Million to Build Agentic Design Automation (SemiWiki)](https://semiwiki.com/eda/agentrys/372749-follow-the-money-agentrys-raises-24-5-million-to-build-agentic-design-automation/)
- [Agentrys Raises $24.5 Million to Build Agentic Design Automation for Chipmakers (Semiconductor Digest)](https://www.semiconductor-digest.com/agentrys-raises-24-5-million-to-build-agentic-design-automation-for-chipmakers/)

---

## Audio script
Agentrys บริษัท startup ทำ AI agent สำหรับ chip design ระดมทุน 24.5 ล้านดอลลาร์ประกอบด้วย seed 19.1 ล้าน Etna Labs นำ กับ pre seed 5.4 ล้าน MediaTek นำเป็น strategic backer แรก founder Mark Ren เคย lead กลุ่ม AI for chip design ที่ NVIDIA ตีพิมพ์ paper เรื่อง PrefixRL DeepPCB และ Nemotron for EDA workflow

ที่น่าสนใจไม่ใช่ตัวเงิน แต่เป็น category ที่บริษัท position ตัวเอง Agentic Design Automation หรือ ADA เป็น successor ของ EDA เดิม Cadence Synopsys Siemens EDA ทั้งหมดยัง focus per task automation engineer ต้อง orchestrate ระหว่าง tool ด้วยมือ Agentrys เสนอ platform ที่ engineer define goal แล้ว agent workforce verification agent floorplan agent timing agent DFT agent ทำงานร่วมกัน learn จาก project ก่อน pattern สำคัญที่ต้องอ่านออก vertical agent for engineering discipline กำลังกลายเป็น thesis ที่ VC ลงทุนหนัก Rebar สำหรับ HVAC Faro สำหรับ pharma Agentrys สำหรับ silicon สาม pattern เดียวกัน naming Agentic X Automation จะซ้ำในทุก vertical Legal Clinical Compliance HR IT enterprise buyer ในไทยควร map budget ปี 2027 ตาม vertical suffix นี้ อย่ารอให้ incumbent SaaS obsolete แล้วค่อยตัดสินใจ ครับ
