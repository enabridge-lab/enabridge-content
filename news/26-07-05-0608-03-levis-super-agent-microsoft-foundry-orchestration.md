---
date: 2026-07-05
slug: levis-super-agent-microsoft-foundry-orchestration
topic: use-case
reading_time_min: 3
sources: 3
image_prompt: |
  A denim-toned orchestration control room in editorial isometric style. Center: a large screen labeled "LEVI'S SUPER AGENT" with glowing lines routing to four smaller screens labeled "HR / ESS AGENT", "SAP AGENT", "RETAIL AGENT", "FINANCE AGENT". Below the screens a bold banner reads "ONE ENTRY POINT — MANY BACKENDS". Around the room, faint Microsoft Teams window frames and a small platform badge "MICROSOFT FOUNDRY" in a corner. Warm indigo lighting, brass accents, high contrast, 1:1 aspect, readable text at 200px thumbnail, no real human faces.
image: images/26-07-05-0608-03-levis-super-agent-microsoft-foundry-orchestration.png
---

# Levi's ปล่อย "Super Agent" บน Microsoft Foundry — Fortune 500 retailer รายแรกที่ ship orchestration layer ครอบ HR/SAP/Retail agents ในบ้าน

## TL;DR
- Levi Strauss ประกาศสร้าง **"Super Agent"** บน **Microsoft Foundry + GitHub Copilot** รันใน Microsoft Teams บน Azure — เป็น orchestration layer ครอบ specialized agent ที่ deploy มาก่อน (ESS agent, custom SAP agent, Retail Agent ที่ครอบ inventory/HR/finance/IT)
- Global rollout เริ่มปี 2026 — pattern **"specialized agent ก่อน, super-agent ทีหลัง"** ตรงข้ามกับ vendor ที่พยายาม sell "one agent to rule them all" ตั้งแต่ day 1
- Jason Gowans (CDTO) บอกชัด: **"speed at which we need to operate"** — direct-to-consumer retailer ต้อง turn design → production → shelf ใน 8-12 สัปดาห์เพื่อแข่ง TikTok Shop / Shein / Temu จึงต้องมี ops layer ที่ปรึกษาได้ผ่าน Teams window เดียว

## เกิดอะไรขึ้น
Levi Strauss ประกาศผ่าน Microsoft Customer Story + PYMNTS + Chain Store Age คัฟเวอร์ต่อ (สัปดาห์นี้) ว่าได้สร้าง **"Super Agent"** บน Microsoft Foundry เป็น orchestration layer ครอบ specialized agent ที่ Levi's ทำมาแล้ว 12-18 เดือน:

- **ESS agent** (Employee Self Service) — HR request ทั้งหมด
- **Custom SAP agent** — ERP transaction, procurement, inventory query
- **Retail Agent** — cross-store inventory, basic HR, finance action สำหรับ store manager
- **Design/Finance agents** ที่ deploy ก่อนหน้าใน 6-12 เดือนที่ผ่านมา (ครอบ product design workflow + finance close cycle)

Employee (พนักงาน 15,000+ ทั่วโลก) เข้าผ่าน **Microsoft Teams** อย่างเดียว — พิมพ์คำถามเดียว ("ขอดู inventory 501 size 32 ที่ store สยาม", "ขอ approve OT พรุ่งนี้", "ขอ MD&A ล่าสุด") → Super Agent วิเคราะห์ intent → route ไป underlying agent → กลับมาตอบใน conversation เดียว. ไม่ต้องเปิด SAP GUI, ไม่ต้องเปิด Workday, ไม่ต้อง search intranet, ไม่ต้อง swivel-chair ระหว่างระบบ

Jason Gowans, Chief Digital & Technology Officer, พูดที่สำคัญ: **"the biggest thing that's changed for us is the speed at which we need to operate"** — direct-to-consumer retailer ในยุค TikTok Shop / Shein / Temu ต้องแข่ง turn design → production → shelf ให้อยู่ในกรอบ 8-12 สัปดาห์ ไม่ใช่ 6 เดือนแบบ 5 ปีที่แล้ว ต้องมี ops layer ที่พนักงานถามอะไรก็ได้แล้วได้คำตอบทันที ไม่งั้นแพ้ที่ organizational velocity ไม่ใช่ที่ product idea

## ทำไมสำคัญ
Levi's น่าจะเป็น Fortune 500 retailer รายแรกที่ ship pattern นี้ scale ระดับหมื่นคนบน production — และ pattern **"specialized agents first, super agent later"** คือคำตอบต่อ debate ที่ร้อนอยู่ในวงการ 12 เดือนที่ผ่านมา: "จะสร้าง 1 agent ที่ทำได้ทุกอย่าง หรือหลาย agent ที่ specialize แล้ว orchestrate?" — ตลาดรอบก่อนพยายาม sell **"one-agent that does everything"** แต่ pilot เยอะรายก็ตกม้าตายเพราะ context/tool ยาวเกินไป, ownership ไม่ชัด, governance เอาไม่อยู่

Levi's เดินสูตรตรงข้าม — เอา specialized agent ที่ทำงานอยู่แล้ว (proven ROI, proven governance, ownership ชัดเจนที่ business unit เดิม) มาเป็น backend ของ Super Agent layer ที่ทำหน้าที่ intent routing + conversation state + fallback ให้มนุษย์ ผลลัพธ์: **super-agent ไม่ต้องเก่ง, แค่ router ที่ฉลาด** — ลด hallucination surface, ลด context length, ลด cost per query, และที่สำคัญ **debug ได้เพราะ boundary ระหว่าง super-agent กับ backend agent ชัดเจน**

Signal อีกด้าน: **Microsoft Foundry กลายเป็น production platform สำหรับ multi-agent orchestration** — ไม่ใช่แค่ Copilot dev sandbox อีกต่อไป Levi's เลือก Foundry เพราะ Teams + Azure + GitHub Copilot อยู่ที่นั่นทั้งหมด → operational velocity สูงกว่า stitch tool อื่น. Foundry ยัง power Frontier Company deployment กับ LSEG อีก — signal เดียวกัน. AWS Bedrock AgentCore กับ Google Vertex AI Agent Builder ต้องออก reference architecture end-to-end แข่งกันภายในไตรมาสถัดไป

รอบก่อนคือ Cisco 90k rollout ที่แจก personal agent ให้พนักงาน; รอบนี้ Levi's แสดงว่า Fortune 500 อีกกลุ่ม (retail, consumer goods, manufacturing) ก็เริ่ม deploy ได้เหมือนกัน แต่ pattern คนละแบบ — **Cisco เน้น "personal assistant + intent routing ระหว่างโมเดล"; Levi's เน้น "super agent + orchestration ระหว่าง backend system"**. สองสูตรจะกลายเป็นสอง reference architecture ที่ CIO อ่านเทียบกันในปี 2027 — Cisco สายที่ workforce heterogeneous / knowledge-worker heavy, Levi's สายที่ ops workflow ผูกกับ ERP+HRIS+POS

## มุม AI Agent Platform
- **Builders** — Agent framework ที่มี native **"sub-agent as tool"** pattern (Anthropic Claude Sub-Agent, OpenAI Agents SDK sub-agent, LangGraph supervisor) จะได้เปรียบ — เพราะ deployment ระดับ Levi's ต้องการ handoff/state management ที่ debug ได้. Framework ที่ยัง treat agent เป็น flat chain จะโดน bypass. Startup ที่ทำ **orchestration/supervisor layer** โดยตรง (CrewAI enterprise, Emergence, Cognosys, LangChain LangGraph Platform) มี tailwind ชัดเจน

- **Users/business ในไทย** — Retailer/CPG/manufacturer ในไทยที่ pilot AI agent แยกทีม (HR ทีมนึง finance ทีมนึง IT ทีมนึง) **ยังไม่ต้องรีบสร้าง super-agent ตอนนี้**; ให้ specialized agent มี proven ROI ก่อน แล้วค่อยเติม orchestration layer ทีหลัง — Levi's ใช้เวลา 18 เดือนสร้าง specialized ก่อนเริ่ม super. **ระวัง trap**: อย่าให้ vendor sell "super agent day 1 พร้อม LLM connector 200 ตัว" — ค่าล้างจะไม่คุ้ม, governance boundary ไม่ชัด, ownership ไม่มี BU ไหนกล้ารับ

- **Ecosystem** — Microsoft Foundry ได้ story customer ที่ prestige (Levi's + LSEG จาก Frontier Company ในสัปดาห์เดียวกัน); AWS/Google Vertex ต้อง response ด้วย end-to-end reference architecture ก่อน re:Invent ปีนี้. Big-4 SI (Deloitte, Accenture, EY, PwC) ที่มี retail practice จะทำ template "Super Agent for retailer" ให้ Fortune 500 อีกร้อยราย pipeline ปี 2027 ชัดเจน

## Sources
- [Levi Strauss & Co. simplifies work and accelerates decision-making with Microsoft Foundry — Microsoft Customer Stories](https://www.microsoft.com/en/customers/story/26647-levi-strauss-and-co-microsoft-foundry)
- [Super Agents Are Connecting What Enterprise Software Kept Separate — PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/super-agents-are-connecting-what-enterprise-software-kept-separate/)
- [Levi's Unifies AI Agents Into Single Interface — Let's Data Science](https://letsdatascience.com/news/levis-unifies-ai-agents-into-single-interface-af53fa97)

---

## Audio script
วันนี้เรามีข่าวใหญ่จาก Levi Strauss ที่สร้าง Super Agent บน Microsoft Foundry แล้วประกาศ rollout ทั่วโลกปีนี้ ที่น่าสนใจคือ Levi's ไม่ได้พยายามสร้าง agent ตัวเดียวที่ทำได้ทุกอย่าง แต่ deploy specialized agent ทีละตัวก่อน มี ESS agent สำหรับ HR มี custom SAP agent สำหรับ ERP มี Retail Agent สำหรับ store manager ครบทั้ง inventory HR finance IT แล้วค่อยเติม Super Agent มาเป็น orchestration layer อยู่ข้างบน พนักงาน 15,000 คนทั่วโลกเข้าผ่าน Microsoft Teams อย่างเดียว ถามอะไรก็ได้ Super Agent วิเคราะห์ intent แล้ว route ไป backend ที่เหมาะสม กลับมาตอบใน conversation เดียว Jason Gowans ที่เป็น Chief Digital & Technology Officer พูดว่าเหตุผลหลักคือ speed at which we need to operate direct-to-consumer retailer ต้องแข่งกับ TikTok Shop กับ Shein ที่ turn design ให้ทันภายใน 8 ถึง 12 สัปดาห์ ต้องมี ops layer ที่เร็วกว่าคนเก่า pattern นี้เป็นสัญญาณสำคัญต่ออุตสาหกรรม รอบก่อน Cisco แจก personal agent ให้พนักงาน 90,000 คน pattern เน้น routing ระหว่างโมเดล รอบนี้ Levi's แสดงว่า Fortune 500 อีกกลุ่ม retail กับ CPG เริ่มออกกันแล้ว แต่ pattern เน้น orchestration ระหว่าง backend system สอง reference architecture ที่ CIO ทั่วโลกจะอ่านเทียบกันในปีหน้า สำหรับ retailer ไทยที่ pilot AI agent แยกทีมอยู่ ยังไม่ต้องรีบสร้าง super-agent ตอนนี้ สร้าง specialized agent ให้ ROI ชัดก่อน แล้วค่อยเติม orchestration ทีหลัง Levi's ใช้เวลา 18 เดือนสร้าง specialized ก่อนเริ่ม super อย่ารีบ ระวัง vendor ที่ pitch super agent day one พร้อม connector 200 ตัว ค่าล้างจะไม่คุ้ม governance ไม่ชัด ownership ไม่มีใครกล้ารับ
