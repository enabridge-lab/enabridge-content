---
date: 2026-08-13
slug: ltts-agenticiq-engineering-manufacturing
topic: openbridge-trend
reading_time_min: 3
sources: 3
image_prompt: |
  Editorial isometric hero showing a modular factory floor with three
  reusable AI agent modules labeled "CAD AGENT", "PLM AGENT", "QA AGENT"
  clicking into slots on a big planning board titled "PLANNING-FIRST".
  A stock ticker glowing in the corner reads "LTTS +2.42%". Under the
  factory a small tag says "PILOT → PRODUCTION". Deep navy background,
  Enabridge-neutral palette, 1:1 aspect, high contrast, no real human
  faces (silhouettes of engineers welcome).
image: images/26-08-13-0616-03-ltts-agenticiq-engineering-manufacturing.png
---

# LTTS เปิด AgenticIQ — vertical agent platform สำหรับ engineering + manufacturing ที่ดัน pilot ขึ้น production

## TL;DR
- L&T Technology Services (LTTS) เปิดตัว **AgenticIQ** วันที่ 11 สิงหาคม 2026 — vertical agent platform ที่แปลง engineering capability ของ LTTS ให้กลายเป็น reusable AI agent
- **Planning-first architecture** ทำงานภายใน governance boundary ขององค์กร — เจาะกลุ่มลูกค้า automotive, industrial manufacturing, medical device, semiconductor, plant engineering
- หุ้น LTTS ขึ้น 2.42% (₹3,670) ใน trading session เดียวกัน — sentiment ตลาดยืนยันว่าเรื่อง "pilot ไป production" คือ narrative ที่ analyst ซื้อ

## เกิดอะไรขึ้น
วันที่ 11 สิงหาคม 2026 L&T Technology Services (LTTS) บริษัท engineering services ในเครือ Larsen & Toubro จากอินเดีย เปิดตัว AgenticIQ™ — platform agentic AI ที่ออกแบบมาเฉพาะสำหรับ engineering, product development, manufacturing และ industrial operations

แนวคิดหลักคือ "planning-first architecture" — แทนที่จะให้ agent เรียก tool แบบ reactive AgenticIQ ให้ agent วางแผนงานทั้ง sequence ก่อน แล้ว execute ผ่าน specialized agent ที่ pre-built มาจาก portfolio Engineering Intelligence ของ LTTS เอง แต่ละ agent ถูก package ให้ reusable ในหลาย workflow — CAD review agent, PLM sync agent, QA validation agent, testing pipeline agent ฯลฯ

Platform เป็น cloud-agnostic — deploy บน cloud หรือ on-premise ก็ได้ ทำให้ลูกค้าที่มี IP proprietary (เช่น semiconductor design, medical device firmware, automotive control logic) เก็บ knowledge / workflow / IP ไว้ในสภาพแวดล้อมของตัวเองได้ ไม่ต้องส่งไป cloud หรือลง third-party model

Target industry คือ automotive, industrial manufacturing, medical device, healthcare, semiconductor, plant engineering, hi-tech — กลุ่มลูกค้าที่ LTTS มี track record ทำ engineering services มายาวและมี regulatory constraint สูงจน frontier lab เจาะเข้ายาก ตลาดตอบรับด้วยการดันหุ้น LTTS ขึ้น 2.42% แตะ ₹3,670 ในช่วงเช้าของวันเดียวกันตามเวลาอินเดีย

## ทำไมสำคัญ
Pattern ที่ AgenticIQ ตอกย้ำคือ "vertical-first, framework-second" — ปี 2025 ทุกคนพูดถึง horizontal framework (LangChain, LlamaIndex, AutoGen) แต่ปี 2026 ตัวที่จริงในตลาดคือ platform ที่มาพร้อม vertical knowledge + workflow ที่ pre-baked มาจากบริษัทที่ทำอุตสาหกรรมนั้นจริง ๆ LTTS ไม่ได้แข่งกับ OpenAI หรือ Anthropic — LTTS แข่งกับ Accenture, TCS, Wipro, Cognizant ในการเป็น "AI-native systems integrator"

ที่น่าจับตาคือ "planning-first" positioning — เป็น response ต่อปัญหา reactive agent (LLM เรียก tool ตอบสนอง prompt แล้วหลง context) ที่ปีนี้เริ่มเป็น pain point ที่ enterprise พูดถึงมากขึ้น การ pre-plan sequence ก่อน execute เป็นวิธีที่ปลอดภัยขึ้นสำหรับ production workflow ที่มี stakes สูง (เช่น validate CAD design ก่อนส่งเข้าโรงงาน)

Signal อีกอันคือ narrative "pilot → production" — LTTS pitch AgenticIQ ตรง ๆ ว่าเป้าหมายคือดัน enterprise AI จาก POC ขึ้น production ตัวเลขจาก report ปี 2026 บอกว่า 31% ของ enterprise มี agent อย่างน้อยหนึ่งตัวใน production แต่มีแค่ 25% ที่ดัน pilot ได้มากกว่า 40% เข้าจริง — LTTS มองเห็นช่องว่างนี้และตั้ง GTM ตรงจุด

## มุม AI Agent Platform
**Builders**: ถ้าคุณสร้าง horizontal agent framework อยู่ AgenticIQ เตือนคุณว่า SI ที่มี vertical knowledge จะบุกลงมาแข่งกับ framework layer โดยตรง เพราะลูกค้า enterprise ไม่ต้องการ toolkit — ต้องการ agent ที่รู้ว่า CAD file ของ SolidWorks คืออะไร, ISO 26262 มี requirement อะไร — คนที่ own domain knowledge จะ own agent stack

**Users / business** ในหมวด manufacturing / engineering: นี่คือ vendor ที่ speak ภาษาคุณ ให้ RFI ที่ compare AgenticIQ กับ Palantir Foundry, Siemens Industrial Copilot, และ AWS Industrial Data Fabric — 4 vendor นี้กำลังไล่กันในตลาด vertical agent สำหรับ heavy industry

**Ecosystem**: SI Indian อย่าง LTTS, TCS, Infosys, Wipro กำลัง pivot จาก body-shop model เป็น product + platform model — ใครทำได้จริงจะกลายเป็น "AI-native SI" ที่มี recurring revenue ต่างจาก project-based revenue เดิม สำหรับ Thai enterprise ที่ต้องเลือก partner: ถามให้ชัดว่า SI ที่เสนอมา มี agent platform ของตัวเองหรือแค่ resell ของคนอื่น

## Sources
- [LTTS launches AgenticIQ to move enterprise AI from pilots to production (Business Standard)](https://www.business-standard.com/companies/news/ltts-launches-agenticiq-to-move-enterprise-ai-from-pilots-to-production-126081100561_1.html)
- [L&T Technology Services Launches AgenticIQ™, an End-to-End Agentic AI Platform (AIThority)](https://aithority.com/news/lt-technology-services-launches-agenticiq-an-end-to-end-agentic-ai-platform-for-engineering-manufacturing-and-customer-experience/)
- [L&T Technology Services Launches AgenticIQ AI Platform; Shares Rise 2.42% (HDFC Sky)](https://hdfcsky.com/news/technology-services-launches-agenticiq-ai-platform)

---

## Audio script
เมื่อวานนี้ L&T Technology Services หรือ LTTS จากอินเดีย เปิดตัวแพลตฟอร์มชื่อ AgenticIQ ที่ออกแบบมาสำหรับสาย engineering กับ manufacturing โดยเฉพาะ ต่างจาก horizontal framework ที่เราคุ้นเคย ตรงที่ AgenticIQ เอา engineering capability ที่ LTTS ทำมาสิบกว่าปีมาแปลงเป็น AI agent สำเร็จรูปที่ reusable

แนวคิดหลักคือ planning-first architecture agent จะวางแผนทั้ง sequence ก่อน แล้วค่อย execute ผ่าน specialized agent เช่น CAD review agent หรือ QA validation agent เป้าหมายคือแก้ปัญหา reactive agent ที่เรียก tool มั่วในงาน stake สูง เช่น validate CAD design ก่อนส่งเข้าโรงงาน platform เป็น cloud agnostic รันบน cloud หรือ on-premise ก็ได้ กลุ่มลูกค้าเป้าหมายคือ automotive, medical device, semiconductor, plant engineering ตลาดตอบรับดี หุ้น LTTS ขึ้น 2.42% ในวันเดียวกัน

pattern ที่น่าสนใจคือ vertical first framework second SI ที่มี domain knowledge ลึกกำลังลงมาแข่งกับ framework layer โดยตรง เพราะลูกค้า enterprise ไม่ต้องการ toolkit ต้องการ agent ที่เข้าใจว่า ISO 26262 คืออะไร คนที่ own domain knowledge จะ own agent stack

สำหรับ Thai enterprise ที่กำลังเลือก partner คำถามที่ควรถามคือ SI ที่เสนอมา มี agent platform ของตัวเองไหม หรือแค่ resell ของคนอื่น เพราะปีนี้ LTTS, TCS, Infosys, Wipro กำลัง pivot จาก body shop model เป็น platform model กันทั้งหมดครับ
