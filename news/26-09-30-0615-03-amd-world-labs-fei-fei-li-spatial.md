---
date: 2026-09-28
slug: amd-world-labs-fei-fei-li-spatial
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a giant AMD chip on a pedestal
  connecting to a floating 3D wireframe world globe labeled "SPATIAL
  INTELLIGENCE". A big price tag reads "$8.2B ALL-STOCK". A smaller badge
  says "EVP + CHIEF SCIENTIST" next to a professor's silhouette holding a
  book. NVIDIA logo appears smaller and grayed out in the corner as a
  competitor. Deep red and silver palette, sharp contrast for 200px
  thumbnails, bold text rendering, no real human faces, 1:1 aspect. Style
  of a Wall Street Journal M&A cover.
image: images/26-09-30-0615-03-amd-world-labs-fei-fei-li-spatial.png
---

# AMD ควัก $8.2B ซื้อ World Labs ของ Fei-Fei Li — Lisa Su เปิดฉากไล่ Nvidia ในสนาม spatial AI

## TL;DR
- AMD ประกาศ all-stock deal มูลค่า **$8.2 พันล้านดอลลาร์** ซื้อ World Labs ของ Dr. Fei-Fei Li — ดีลใหญ่อันดับ 2 ของ AMD รองจาก Xilinx ($50B ปี 2022)
- Dr. Fei-Fei Li ("godmother of AI") จะเข้า AMD ในตำแหน่ง **EVP + Chief Scientist** รายงานตรง Lisa Su หลัง deal ปิดปลายปี 2026
- World Labs สร้าง spatial intelligence models ที่ generate/reconstruct/simulate 3D environments — เป็นเครื่องมือสำหรับ robotic learning + physical AI agents

## เกิดอะไรขึ้น
วันที่ 28 กันยายน AMD ประกาศดีล all-stock มูลค่าประมาณ **8.2 พันล้านดอลลาร์** เพื่อซื้อ World Labs — startup ของ Dr. Fei-Fei Li ที่ตั้งใน San Francisco. Deal คาดว่าจะปิดปลายปี 2026 ขึ้นอยู่กับการอนุมัติของ regulator. World Labs โฟกัสเรื่อง **spatial intelligence** — โมเดลที่สร้าง, สร้างใหม่, และจำลอง 3D environments จาก input ที่เป็น text, image, video — บวกเทคโนโลยีสำหรับ robotic learning + simulation.

หลัง deal ปิด Dr. Fei-Fei Li จะเข้ามาเป็น **Executive Vice President และ Chief Scientist** ของ AMD รายงานตรงต่อ Dr. Lisa Su. เธอเป็นผู้ก่อตั้ง ImageNet, อดีต Chief Scientist ของ Google Cloud, และคนที่หลายสำนักเรียกว่า "godmother of AI". SCMP กับ TechCrunch ระบุว่านี่คือการ escalate ความแข่งขันของ AMD กับ Nvidia ในระดับที่ไม่เคยเห็นมาก่อน — AMD เดิมเก่งเรื่อง hardware แต่ขาดชื่อ AI research ระดับ Fei-Fei Li ที่จะดึง talent + ecosystem attention.

ราคา $8.2B ทำให้เป็นดีล M&A ใหญ่อันดับ 2 ในประวัติศาสตร์ AMD — เทียบ Xilinx ที่ AMD ซื้อไปประมาณ $50B ในปี 2022. AMD บอกว่าการซื้อครั้งนี้จะช่วยยัด "model research expertise" เข้ากับ hardware + software roadmap โดยเฉพาะเมื่อ AI ขยายไป reasoning, robotics และ physical applications ที่ compute pattern ต่างจาก LLM inference แบบเดิม.

## ทำไมสำคัญ
Deal นี้เปลี่ยน ambition ของ AMD จาก **GPU vendor เบอร์สอง** เป็น **frontier AI company**. เดิม Lisa Su ทำ AMD ให้กลายเป็น alternative ของ Nvidia ในด้าน hardware — MI300X, MI400 series ได้พาร์ทเนอร์ hyperscaler มาแล้ว. แต่ในเกม AI นักลงทุนไม่ให้ premium ถ้าคุณเป็นแค่ chip vendor — ต้องมี AI IP + top researcher ถึงจะได้ multiple แบบ Nvidia. การได้ Fei-Fei Li มาเป็น Chief Scientist ทำให้ AMD มีคน "หน้าตาเดียวกับ Jensen Huang" ในเวที AI industry — ในเชิง signaling นี่มีค่ามหาศาล.

ทำไมต้อง spatial intelligence? เพราะเป็น **จุดที่ Nvidia ยังไม่ได้ครองแบบเบ็ดเสร็จ**. LLM training + inference ที่ Nvidia ครองคือของยากอยู่แล้ว — แต่ **physical AI**, robotics, autonomous vehicle, spatial simulation เป็น domain ที่ทั้งอุตสาหกรรมยังหาผู้ชนะไม่ได้ชัดเจน. World Labs ให้ AMD (1) research talent, (2) โมเดลที่พร้อม deploy บน hardware AMD, (3) narrative ให้ Lisa Su ไปคุยกับ CEO ของ Ford, GM, Boston Dynamics, Amazon (robots), และ Tesla ว่า "hardware + software stack ที่ทำ physical AI ครบ end-to-end". นี่คือ pattern เดียวกับที่ Nvidia ใช้เข้า enterprise ผ่าน Omniverse — แต่ AMD กำลังจะได้เร็วกว่าด้วย M&A แทน organic build.

Signal ที่ใหญ่กว่า: **agent จะออกจากหน้าจอไปสู่ physical world**. ปีนี้ทุกเจ้าเปิดตัว browser agent, coding agent, customer service agent — ทั้งหมดยัง action อยู่ใน UI layer. อีก 12-18 เดือน agent ที่ต้องทำงานใน warehouse, factory, home ที่มีหุ่นยนต์จริง จะกลายเป็นสนามใหม่. ใครมี foundation model สำหรับ 3D scene + physics simulation + robotic policy จะขาย compute ปริมาณมหาศาลได้. Fei-Fei Li ที่ AMD คือชิ้นแรกที่ Lisa Su ล็อคไว้.

## มุม AI Agent Platform
**Builders** ที่ทำ agent framework — ถ้า roadmap ของคุณยังจำกัดที่ text + web browsing เตรียม expand ไป physical action space (robot arm control, drone flight, warehouse picking) ในปี 2027. Framework ที่ abstract ระหว่าง digital + physical action ได้ดีจะโดดเด่น (LangGraph, CrewAI ยังไม่มี native support จริงจัง — โอกาสของ startup ใหม่). **Users/Business** โดยเฉพาะ manufacturing, logistics, retail (Walmart, Amazon warehouse), automotive — spatial AI จาก AMD จะเปิด option ที่ 2 นอกจาก Nvidia stack. ในอีก 6-12 เดือนที่ deal ปิดยัง cost ของ physical AI compute จะลดลง เพราะการแข่งขัน — และวันหนึ่ง ROI ของ warehouse automation หรือ predictive maintenance ก็จะข้ามเส้น. **Ecosystem** — Nvidia ต้องตอบสนอง. คาดเดา 3 ทาง: (1) เร่ง Omniverse + Isaac ให้เข้า enterprise เร็วขึ้น, (2) ซื้อ competitor ของ World Labs (Skild AI, Physical Intelligence) ก่อนที่ AMD จะได้เพิ่ม, (3) จับมือ hyperscaler ให้เปิด spatial AI service เป็น managed service. เกม physical AI จะร้อนแรงกว่า LLM ในอีก 24 เดือน.

## Sources
- [AMD will acquire Fei-Fei Li's World Labs for $8.2B — TechCrunch](https://techcrunch.com/2026/09/28/amd-will-acquire-fei-fei-lis-world-labs-for-8-2-billion/)
- [AMD acquires Fei-Fei Li's World Labs for $8.2 billion — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/amd-acquires-fei-fei-lis-121544620.html)
- [AMD To Acquire World Labs For $8.2 Billion To Advance AI Compute And Spatial Intelligence — Pulse 2](https://pulse2.com/amd-to-acquire-world-labs-for-8-2-billion-to-advance-ai-compute-and-spatial-intelligence/)
- [AMD buys Fei-Fei Li's World Labs for US$8.2b, escalating rivalry with Nvidia — SCMP](https://www.scmp.com/tech/big-tech/article/3369141/amd-acquires-godmother-ai-li-fei-feis-start-battle-nvidia-intensifies)

---

## Audio script
มาต่อกันครับ. AMD ประกาศ all-stock deal 8.2 พันล้านดอลลาร์ซื้อ World Labs startup ของ Dr. Fei-Fei Li คนที่หลายสำนักเรียก godmother of AI. Deal นี้ใหญ่เป็นอันดับ 2 ในประวัติศาสตร์ AMD รองจากดีล Xilinx เมื่อปี 2022. Dr. Fei-Fei Li จะเข้า AMD ในตำแหน่ง Executive Vice President และ Chief Scientist รายงานตรงต่อ Lisa Su. World Labs โฟกัสเรื่อง spatial intelligence โมเดลที่สร้างและจำลอง 3D environment สำหรับ robot กับ physical AI. คำถามคือทำไม spatial intelligence คำตอบคือมันคือจุดที่ Nvidia ยังไม่ได้ครองเบ็ดเสร็จ. LLM training อยู่ในมือ Nvidia อยู่แล้ว แต่ physical AI robotics autonomous vehicle ยังเป็นสนามเปิดที่ใครก็ชนะได้. AMD ได้ Fei-Fei Li คือได้ทั้ง research talent โมเดลพร้อม deploy บน hardware ของตัวเอง และ narrative ให้ Lisa Su ไปคุยกับ CEO ของ Ford Amazon Tesla ว่ามี stack ครบ end-to-end. Signal ที่ใหญ่กว่านั้นคือ agent จะออกจากหน้าจอไปสู่ physical world. ปีนี้ทุกเจ้าเปิดตัว browser agent coding agent อีก 12-18 เดือน agent ที่ต้องทำงานใน warehouse factory ที่มีหุ่นยนต์จริงจะกลายเป็นสนามใหม่. Builder ที่ทำ framework แล้วยังจำกัดที่ text กับ browser เตรียม expand ไป physical action space. Business ที่ทำ manufacturing logistics retail มี option ที่สองนอกจาก Nvidia stack. Nvidia เองก็ต้องตอบสนองครับ อาจจะซื้อ Skild AI หรือ Physical Intelligence คู่แข่งของ World Labs ก่อนที่ AMD จะได้เพิ่ม. เกม physical AI จะร้อนแรงกว่า LLM ในอีก 24 เดือนครับ.
