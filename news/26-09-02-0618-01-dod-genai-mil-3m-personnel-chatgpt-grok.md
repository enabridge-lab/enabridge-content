---
date: 2026-09-02
slug: dod-genai-mil-3m-personnel-chatgpt-grok
topic: use-case
reading_time_min: 5
sources: 4
image_prompt: |
  A monumental Pentagon-shaped vault opening its five sides, three glowing
  model badges marching out in formation labeled "CHATGPT MIL",
  "GROK FOR GOV", and "GEMINI". A big banner overhead reads
  "3,000,000 USERS". One empty pedestal in the foreground carries a torn
  ribbon labeled "CLAUDE — BLOCKED". Editorial isometric magazine style,
  muted navy + gold palette, ultra-high contrast so the "3M USERS" number
  and the empty pedestal read at 200px thumbnail size. No real human faces,
  silhouette OK. 1:1 aspect ratio.
image: images/26-09-02-0618-01-dod-genai-mil-3m-personnel-chatgpt-grok.png
---

# Pentagon เปิด GenAI.mil ให้ ChatGPT + Grok ยิงตรงเข้า 3M ทหาร-พลเรือน — Claude ถูก block เพราะดีลเรื่อง lethal weapons ล่ม

## TL;DR
- **DoD** ประกาศ **1 ก.ย. 2026** เปิด GenAI.mil ให้ **3M military + civilian personnel** ใช้ ChatGPT Mil (OpenAI) + Grok for Government (xAI) ร่วมกับ Gemini for Government ที่มีอยู่แล้ว
- **Onboard 1.7M user** จาก 3M ทั้งหมดแล้ว — จาก launch ครั้งแรก **9 ธ.ค. 2025** ใน 9 เดือน
- **Impact Level 5 accreditation** — ยัด controlled unclassified info ได้
- **Anthropic ถูก block** — ปฏิเสธ contract เพราะไม่ยอมให้ DoD ใช้ Claude ทำ **mass surveillance** + **lethal autonomous weapons**

## เกิดอะไรขึ้น

Department of Defense ประกาศ **1 กันยายน 2026** ว่า **GenAI.mil** — portal genAI ของ Pentagon — เพิ่ม **ChatGPT Mil** (OpenAI) และ **Grok for Government** (xAI/Starshield) เข้าไปเสริม Google Gemini for Government ที่เป็นตัวเปิดตัวตั้งแต่ **9 ธันวาคม 2025**. ตอนนี้ Pentagon 3M คน — ทหาร + พลเรือนสังกัด DoD ทั้งหมด — เข้าถึง 3 frontier model ผ่าน portal เดียว. Onboard ไปแล้ว **1.7M unique user** จาก 3M

ทั้ง ChatGPT Mil และ Grok for Government ถือ **Impact Level 5 accreditation** — ระดับที่จัดการ controlled unclassified information (CUI) ได้ตาม DISA standard. หมายถึง soldier ใน field, analyst ที่ Pentagon, contract officer ใช้ AI ยัด logistics data, mission planning, procurement analysis ได้โดยไม่ต้องกลัวว่า model provider จะเห็นข้อมูล — traffic วิ่งอยู่ใน gov cloud, model host แยก isolated

**ที่น่าสังเกต** — และเป็น structural signal ของ agent-AI-in-defense — คือ **Anthropic ไม่อยู่ในรายชื่อ**. DefenseScoop รายงานว่า Anthropic ปฏิเสธข้อเสนอ contract เพราะ leadership ยืนยัน 2 ข้อ: (1) Claude จะไม่ถูกใช้ทำ **mass surveillance ต่อ US citizens** (2) Claude จะไม่ถูก integrate เข้า **lethal autonomous weapons system**. Pentagon ไม่ยอมให้ carve-out นี้ในสัญญา — ดีลจึงล่ม. Anthropic ยอมสูญ contract หลาย 100M เพื่อไม่ให้ safety principle ถูก compromise

Fortune ระบุตัวเลขว่า 3M ผู้ใช้ = ตัวเลข **agent deployment ที่ใหญ่ที่สุดในภาครัฐทั่วโลก**. เทียบ UK Gov AI (~500K user), Singapore Gov (~150K), Australia DTA (~80K) — Pentagon ใหญ่กว่า 6-30 เท่า

## ทำไมสำคัญ

3 signal เด่นที่จะเห็นภายใน 6 เดือน:

**1. Model provider ถูกบังคับให้เลือกฝ่าย.** OpenAI + xAI เลือก accept DoD spec เต็มรูป — ได้ contract 3M user + billion-dollar ARR. Anthropic เลือก stand ที่ safety — เสียตลาดรัฐบาลใหญ่สุดในโลก. ไม่มี middle ground อีกแล้ว. Google อยู่ตรงกลาง (Gemini เข้าตั้งแต่รอบแรก) แต่ยังไม่ commit lethal weapons module. **Google Cloud Next 2027** จะเป็น deadline บังคับให้ Google เลือก

**2. Pentagon กลายเป็น biggest agent-infra reference customer.** ถ้า 3M user ใช้จริงระดับ 40-50% ประจำ (= 1.2-1.5M DAU) — GenAI.mil จะเป็น deployment ที่ใหญ่กว่า enterprise ทุกเจ้ารวมกัน. Federal agency, NATO ally, พันธมิตร Five Eyes จะ **copy spec ทันที** — เกิด "GovAI stack" มาตรฐานใหม่ (IL5 + BYO cloud + sovereign identity) ที่ทั้ง OpenAI, xAI, Google จะขายต่อยอดไปทั่วโลก. ประเทศไทย (กลาโหม, DES) จะโดน pitch แน่นอนภายในไตรมาส

**3. "Agentic warfare" เข้าสู่ mainstream discussion.** ChatGPT Mil + Grok ที่ Pentagon deploy ตอนนี้เป็น chat-first — soldier ถามคำถาม, model ตอบ. แต่ Grok Government roadmap 2027 มี **autonomous agent tier** — model วิเคราะห์ satellite feed + คำสั่ง + ยิง alert ให้ commander โดยไม่ต้องรอ human loop. ที่ Anthropic ปฏิเสธคือ "ยิง trigger" ให้ weapon; ที่ OpenAI/xAI ยอมคือทุกอย่างจนถึงก่อน trigger. เส้นแบ่งบางลง

## มุม AI Agent Platform

**Builders**: ถ้าคุณสร้าง agent framework / orchestration ที่ target enterprise + gov, ต้องเตรียม **compliance stack ระดับ IL5** เป็น table stake ไม่ใช่ premium feature: FedRAMP High, DISA IL5, ITAR-controlled deploy region, air-gapped mode, audit trail ที่ tamper-evident. AccuKnox AgentZ, Broadcom AgentMinder (ที่เพิ่ง launch 31 ส.ค.), Palantir AIP กำลังไล่ตลาดนี้ — window ปิดเร็ว

**Users / businesses**: บริษัทที่ทำงาน supply chain / cloud service ให้ US gov (Amazon, MSFT, Google, Oracle) จะเจอ pressure ต้องรับ agent workflow ของ contractor Pentagon เข้ามาใน integration point ของตัวเอง — ต้องมี MCP endpoint / A2A gateway ที่ compliance-certified. ธุรกิจไทยที่ export ไป US defense supply chain (electronics, textile ที่ label MIL-SPEC) จะได้ RFP ที่ระบุ "agent-readable BOM/certification" ใน 12 เดือน

**Ecosystem**: Anthropic ทำ risk asymmetric bet — สูญ short-term revenue เพื่อ brand equity ระยะยาวใน enterprise + regulated market (healthcare, finance, EU public sector) ที่ safety story = win. ต้องดูว่าตลาดพวกนั้นจะโตพอ compensate defense revenue ที่หายไปหรือเปล่า — เกม 3-5 ปี

## Sources
- [Grok and ChatGPT join Gemini in Pentagon's enterprise genAI portal (DefenseScoop)](https://defensescoop.com/2026/08/31/grok-chatgpt-added-to-genai-mil/)
- [The Pentagon now has its own version of ChatGPT and Grok (TechCrunch)](https://techcrunch.com/2026/08/31/the-pentagon-now-has-its-own-version-of-chatgpt-and-grok/)
- [The Pentagon is giving 3 million military and civilian workers access to ChatGPT and Grok (Fortune)](https://fortune.com/2026/09/01/pentagon-chatgpt-grok-government-military-ai-members-pete-hegseth-defense-department/)
- [OpenAI's ChatGPT Mil is now available to over 3 million US military personnel (Neowin)](https://www.neowin.net/news/openais-chatgpt-mil-is-now-available-to-over-3-million-us-military-personnel/)

---

## Audio script
สวัสดีครับทุกคน ข่าวใหญ่ที่สุดของวันนี้มาจาก Pentagon. Department of Defense ประกาศเมื่อวันที่ 1 กันยายน ว่าเปิด portal GenAI dot mil ให้ทหารและพลเรือนสังกัด DoD 3 ล้านคนใช้ ChatGPT Mil ของ OpenAI และ Grok for Government ของ xAI ร่วมกับ Gemini ของ Google ที่มีอยู่แล้ว. Onboard ไปแล้ว 1.7 ล้าน user จาก 9 เดือนที่ launch — เป็น deployment agent ภาครัฐที่ใหญ่ที่สุดในโลก. ทั้ง ChatGPT Mil และ Grok ถือ Impact Level 5 — ใช้กับ controlled data ได้. ที่น่าจับตาคือ Anthropic ไม่อยู่ในรายชื่อ — เขาปฏิเสธ contract เพราะไม่ยอมให้ Claude ถูกใช้ทำ mass surveillance กับพลเมือง US หรือ integrate เข้า lethal autonomous weapon. Pentagon ไม่ยอมเซ็น carve out นี้ ดีลจึงล่ม — Anthropic ยอมสูญ revenue หลาย 100 ล้านเพื่อยืน principle เรื่อง safety. Signal ที่จะตามมา — model provider ทุกเจ้าถูกบังคับให้เลือก stance ต่อ defense use แล้ว ไม่มี middle ground; Federal agency กับพันธมิตร Five Eyes จะ copy spec ของ Pentagon ทันที เกิด GovAI stack มาตรฐานใหม่ที่ประเทศไทยจะโดน pitch ในไตรมาสหน้าแน่นอน. สำหรับ builder ที่ทำ agent platform — compliance ระดับ IL5, FedRAMP High, air-gap deployment ต้องเป็น table stake ตั้งแต่วันนี้ครับ
