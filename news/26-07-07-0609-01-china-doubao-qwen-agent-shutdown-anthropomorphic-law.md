---
date: 2026-07-07
slug: china-doubao-qwen-agent-shutdown-anthropomorphic-law
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  A wide editorial isometric scene: two massive Chinese neon storefronts side-by-side
  labeled "DOUBAO" and "QWEN" with dimmed lights and steel shutters half-rolled down.
  Above each entrance, huge red bilingual signs read "AGENT FEATURES OFFLINE — JULY 15"
  and "USER DATA UNRECOVERABLE — OCT 15". In the sky, a giant government stamp
  glows over the whole street: "INTERIM MEASURES FOR ANTHROPOMORPHIC AI". Tiny
  silhouettes of confused users walk away from the shutters clutching phones with
  fading conversation bubbles. To the far left, one small sign points toward an
  emergency exit labeled "MAOXIANG". Cinematic dusk lighting, cyberpunk-editorial style,
  high contrast, 1:1 aspect, readable at 200px thumbnail, no real human faces.
image: images/26-07-07-0609-01-china-doubao-qwen-agent-shutdown-anthropomorphic-law.png
---

# จีนสั่งปิด AI Agent ระดับชาติ — Doubao + Qwen dismantle persistent-memory companion วันที่ 15 ก.ค. ก่อนกฎหมาย "Anthropomorphic AI" มีผล

## TL;DR
- ByteDance และ Alibaba ประกาศพร้อมกันเสาร์ 4 ก.ค. — **Doubao ปิด agent feature 15 ก.ค.**, **Qwen ปิด humanlike agent 10 ก.ค. + agent function ทั้งหมด 15 ก.ค.**; หลัง 15 ต.ค. **data ทั้งหมด unrecoverable**
- เหตุ: **Interim Measures for the Administration of AI Anthropomorphic Interaction Services** — CAC + NDRC + MIIT + MPS + SAMR 5 หน่วยงานร่วมออก เม.ย. 2026 บังคับ anti-addiction system + 2-hour break reminder ที่ **clash โดยตรงกับ architecture ของ persistent-memory agent**
- ByteDance ตั้ง fallback ให้ user redirect ไป **Maoxiang** (in-house app คนละ compliance envelope); Alibaba **ไม่มี migration path** ให้ Qwen — ผู้ใช้เสีย agent + memory ทั้งหมด
- **จีนกลายเป็นตลาดใหญ่แห่งแรกที่ regulator สั่ง "tear down persistent agent" ที่ scale ระดับชาติ** — signal ต่อทุก platform builder ว่า agent memory + persona = regulatory surface ที่ต้อง architect เผื่อ toggle ได้

## เกิดอะไรขึ้น

เช้าวันเสาร์ 4 กรกฎาคม 2026 ByteDance กับ Alibaba ปล่อยประกาศพร้อมกันภายในไม่กี่ชั่วโมง — **Doubao** app AI companion ที่มีผู้ใช้ใหญ่ที่สุดของ ByteDance ประกาศว่าฟีเจอร์ AI agent (personalized companion + custom agent creation) จะถูกปิดถาวรวันที่ **15 ก.ค. 2026**. ผู้ใช้ยังเข้าถึง configuration + chat history แบบ read-only ได้ถึง **15 ต.ค. 2026** หลังจากนั้น "ข้อมูลจะถูกประมวลผลตาม privacy policy และไม่สามารถกู้คืนได้อีก". Qwen ของ Alibaba ประกาศตามในเวลาไล่เลี่ยกัน — **humanlike interactive agent + user-created agent function ปิด 10 ก.ค.**, ส่วน **agent function และ service ในภาพรวมทั้งหมดปิด 15 ก.ค.** — และ Alibaba ไม่ประกาศ data retention window ให้เลย

ที่มาของ deadline คือ **Interim Measures for the Administration of AI Anthropomorphic Interaction Services** — กรอบกำกับดูแลตัวแรกของโลกที่มุ่งเฉพาะ AI service ที่ "simulate human personality traits, thinking patterns and communication styles to provide sustained emotional interaction". ออกโดย 5 หน่วยงานพร้อมกันเมื่อเดือน เม.ย. 2026 — **Cyberspace Administration of China (CAC) + National Development and Reform Commission (NDRC) + Ministry of Industry and Information Technology (MIIT) + Ministry of Public Security (MPS) + State Administration for Market Regulation (SAMR)** — ระดับ inter-agency แบบนี้ไม่ใช่ notice ธรรมดา, เป็นสัญญาณว่ารัฐบาลจีนวางกรอบระยะยาว. รายละเอียดที่ทำให้ persistent-memory agent ปฏิบัติตามไม่ได้: บังคับ **anti-addiction system + 2-hour break reminder + instant-exit mechanism + regulatory friction requirement** ที่ขัดแย้งโดยตรงกับ design goal ของ companion agent ที่พยายาม maximize engagement + emotional continuity

การเลือก "ปิด" แทน "rebuild" เป็น business decision ที่บอกอะไรหลายอย่าง — ByteDance กับ Alibaba มีทั้ง engineering muscle และ compliance budget พอที่จะรื้อสถาปัตยกรรมได้ แต่ **ประเมินว่าไม่ทัน timeline + rebuild แล้ว UX เสียจนไม่คุ้ม**. ByteDance ปิดทางแก้แบบครึ่ง ๆ ด้วยการ redirect ผู้ใช้ไปที่ **Maoxiang** — app in-house อีกตัวที่ compliance envelope ต่างออกไป (มี friction mechanism ในตัวแต่ agent ให้ครีเอทน้อยกว่า). Alibaba ไม่ทำ fallback เลย — ผู้ใช้ Qwen ที่ลงทุนสร้าง persona/context/memory ตลอดหลายเดือน = **หายเกลี้ยงในวันที่ 15**

## ทำไมสำคัญ

**จีนกลายเป็นตลาดใหญ่แห่งแรกที่ regulator สั่ง "dismantle persistent-agent architecture" ที่ scale ระดับชาติ.** เทียบกับ EU AI Act ที่เน้น risk category + transparency requirement ค่อยเป็นค่อยไป, หรือ White House framework ที่ยังไม่คลอด, กฎจีนเลือก **behavior-level constraint** (anti-addiction, break reminder) ที่ทำลาย product-market fit ของ persistent agent โดยตรง. Pattern นี้ **ตรงข้ามกับที่ US ไปทาง developer-first + industry-self-regulation** — regulator จีนตัดสินว่า "AI ที่ simulate human relationship = risk category ที่รอตลาด self-correct ไม่ได้"

Signal ที่ชัดกว่าคือ **agent memory + persona = regulatory surface**. ตลอด 18 เดือนที่ผ่านมา, framework builder ทั้งหมด (LangChain, Autogen, CrewAI, Anthropic Skills, OpenAI Workspace Agents) ออกแบบ memory เป็น first-class primitive — user context, preference, long conversation history เก็บใน vector store + retrieved ทุก session. **ถ้าตลาดใหญ่ต่อไป (อินโดนีเซีย, อินเดีย, บราซิล) เลือก pattern จีน**, ทุก builder จะต้องรื้อ architecture ให้ memory toggle-able ต่อ jurisdiction ต่อ user cohort ต่อ session type — คล้ายที่ GDPR บังคับให้ทุกบริษัทมี "right to be forgotten" endpoint แต่ scale ขึ้นทั้ง order of magnitude

จับตา **Baidu, Tencent Yuanbao, Moonshot Kimi** ที่ยังไม่ประกาศ compliance plan — ถ้าเลือก path เดียวกับ ByteDance (ปิด + redirect) จะเห็น consolidation ของ AI companion market จีนกลับไปสู่ walled garden ของ super-app เดิม; ถ้าเลือก rebuild สำเร็จ (มี anti-addiction + break UI แต่รักษา retention) จะกลายเป็น **reference architecture ของ "compliant persistent agent"** ที่ export ออกไปที่ตลาดอื่น. Deadline สั้น (11 วันจากวันประกาศ) แสดงว่าจีนไม่ให้ industry ต่อรอง — และ **incumbent US framework builder ต้องเริ่ม draft equivalent toggle ทันที** ก่อน regulator ประเทศอื่น copy-paste

Angle ที่ underplay ในสื่อ: **Maoxiang กลายเป็น designated safe harbor** สำหรับ ByteDance — ถ้า user migrate สำเร็จ, ByteDance รักษา engagement ได้แม้ต้องเสีย agent creation surface. Alibaba ทิ้ง user คือเจตนา หรือคือ engineering constraint ที่แก้ไม่ทัน — คำตอบจะชัดเจนในไตรมาสหน้า ถ้า Alibaba ประกาศ "Wukong Personal" หรือ product ใหม่ที่มี compliance mechanic ตั้งแต่ต้น

## มุม AI Agent Platform

- **Builders** (framework + memory infra) — agent memory ต้อง **jurisdiction-aware ตั้งแต่ schema level**: session mode, region, user consent status ต้องเป็น 1st-class dimension ใน retrieval + persistence layer ไม่ใช่ afterthought. Framework ที่ hard-code long-term memory (LangChain memory module, Autogen conversation buffer, OpenAI Assistants API `metadata`) ต้องเพิ่ม **regional policy adapter** — สลับ memory scope, session TTL, anti-engagement UI ได้ผ่าน config เดียว. Product ที่ pivot ทันจะได้เรียกตัวเองว่า "regulation-ready agent stack" ตอน RFP ปีหน้า

- **Users / business** ในไทยและ APAC — **ทุก enterprise ที่ deploy consumer-facing agent (bank chatbot, insurer companion, retail personal shopper) ต้อง audit วันนี้**: (1) มี memory persistence ข้าม session ไหม, (2) simulate persona ระดับ emotional continuity ไหม, (3) มี break reminder / usage cap ไหม. **สำนักงานคุ้มครองข้อมูลส่วนบุคคล (PDPC)** และ **ธปท./กสทช.** ไม่มีกฎเทียบเท่าจีนวันนี้ — แต่ pattern นี้ export ง่าย + Thailand copy-paste regulator บ่อย. ทีม compliance ควร brief board ภายใน Q3 ว่า architecture ปัจจุบัน **rebuild ทันไหม + budget เท่าไหร่** ถ้า regulator ไทย mandate ในปีถัดไป

- **Ecosystem** — vector DB + memory infra vendor (Pinecone, Weaviate, Zep, Mem0, LangMem) ควรเริ่มเสนอ **compliance-mode SKU** — auto TTL, jurisdiction filter, audit-trail-by-default. **Enterprise integration platform** ที่ propagate identity ระหว่าง agent + backend (SnapLogic Trusted Agent Identity, Databricks Unity, Salesforce Trust Boundary) ได้เปรียบตรงที่ policy layer มีอยู่แล้ว — แค่ push metadata field เพิ่มไม่กี่ตัว. **APAC AI startup** ที่ pitch VC ควรเน้น "compliance-native architecture" เป็น differentiator ตั้งแต่ pitch deck — เพราะ US โมเดล "move fast" กำลังจะเจอกฎเดียวกันในตลาดที่คุณจะขยายไป

## Sources
- [ByteDance's Doubao and Alibaba's Qwen to shut down AI agent features on July 15 — TechNode](https://technode.com/2026/07/06/bytedances-doubao-and-alibabas-qwen-to-shut-down-ai-agent-features-on-july-15/)
- [ByteDance and Alibaba to disable humanlike AI custom agents as new rules loom — South China Morning Post](https://www.scmp.com/tech/big-tech/article/3359482/bytedance-and-alibaba-disable-humanlike-ai-custom-agents-new-rules-loom)
- [ByteDance, Alibaba pull AI companion features as China tightens rules — Business Standard](https://www.business-standard.com/world-news/bytedance-alibaba-pull-ai-companion-features-as-china-tightens-rules-126070600221_1.html)
- [China AI Companion Law Arrives July 15: Doubao and Qwen Agent Data Will Be Deleted — TechTimes](https://www.techtimes.com/articles/319703/20260704/china-ai-companion-law-arrives-july-15-doubao-qwen-agent-data-will-deleted.htm)

---

## Audio script
วันนี้เรามีข่าวใหญ่จากจีนที่จะเปลี่ยนวิธีคิดเรื่อง AI agent architecture ทั้งอุตสาหกรรม เช้าเสาร์ที่ผ่านมา ByteDance กับ Alibaba ประกาศพร้อมกันว่า Doubao กับ Qwen จะปิดฟีเจอร์ AI agent ทั้งหมดในวันที่ 15 กรกฎาคม และหลัง 15 ตุลาคม ข้อมูลผู้ใช้ที่สร้าง persona กับ agent เอาไว้จะถูกลบและกู้คืนไม่ได้ Qwen หนักกว่าเพราะ Alibaba ไม่มี migration path ให้เลย ผู้ใช้จะเสีย memory ที่ลงทุนไปทั้งหมด สาเหตุคือกฎหมายจีนตัวใหม่ชื่อ Interim Measures for Anthropomorphic AI Interaction Services ที่ 5 หน่วยงานร่วมกันออกตั้งแต่เมษายน มีผลบังคับ 15 กรกฎาคมนี้ กฎบังคับให้ทุก AI ที่ simulate persona มนุษย์ต้องมี anti-addiction system มี break reminder ทุก 2 ชั่วโมง และมี exit mechanism ซึ่ง clash โดยตรงกับ architecture ของ persistent-memory agent เกือบทั้งหมด ByteDance เลือก redirect ผู้ใช้ไป Maoxiang app อีกตัวที่ compliance envelope ต่างออกไป Alibaba ทิ้งผู้ใช้เลย ที่น่าสังเกตคือทั้งสองบริษัทมี engineering muscle พอที่จะ rebuild ได้ แต่ประเมินว่าไม่ทัน deadline สั้นแค่ 11 วัน สัญญาณต่ออุตสาหกรรมคืออะไร คือ agent memory และ persona กลายเป็น regulatory surface ที่ทุก platform builder ต้อง architect ให้ toggle ได้ต่อ jurisdiction ต่อ session type ตั้งแต่ schema level ถ้าอินโดนีเซียหรืออินเดียเลือก path เดียวกับจีน framework ที่ hard-code memory จะโดนบังคับให้รื้อทั้ง stack สำหรับธุรกิจไทยที่ deploy consumer-facing agent ในธนาคาร ประกัน retail ควรทำ compliance audit ภายในไตรมาสนี้ว่า memory persistence กับ persona simulation ของเรา ถ้า PDPC หรือธปท. mandate ตามจีน rebuild ทันไหม budget เท่าไหร่ เพราะ pattern แบบนี้ copy-paste ข้าม regulator ได้เร็วมาก
