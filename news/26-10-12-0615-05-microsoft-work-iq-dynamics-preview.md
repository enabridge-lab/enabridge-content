---
date: 2026-09-30
slug: 26-10-12-0615-05-microsoft-work-iq-dynamics-preview
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial hero: a hospital-ER style control room where a glowing dashboard
  labeled "WORK IQ" shows live heart-rate traces for data streams from
  "DYNAMICS 365", "POWER APPS", "SALES", "SERVICE". A central approval
  modal pops up asking "APPROVE AGENT WRITE?" with YES/NO buttons. A
  ribbon across the top reads "GOVERNED ACTIONS — PREVIEW OCT 2026".
  Isometric vector, Microsoft blue + traffic-light green/red accents on
  slate background, 1:1 aspect, no real human faces, bold text clearly
  readable at 200px thumbnail.
image: images/26-10-12-0615-05-microsoft-work-iq-dynamics-preview.png
---

# Microsoft เปิด Work IQ Preview — ให้ Copilot อ่าน Dynamics / Power Apps และ "เสนอการแก้ไข" ก่อน approve

## TL;DR
- 30 ก.ย. 2026 Microsoft เปิด public preview ของ **Work IQ** สำหรับ **Dynamics 365 Sales / Customer Service + Power Apps + third-party line-of-business apps**; **Finance and Operations (ERP) จะเพิ่มปลาย ต.ค.**
- Core primitive คือ **semantic model + reusable business skills + governed actions** — agent ที่ "เสนอ" การแก้ไข, route ไป approve, แล้วค่อย commit ภายใน scope ของ user; รัน under **Microsoft Agent 365** และ **billed ผ่าน Copilot Credits**
- Positioning ของ Microsoft คือ **"CRM/ERP data finally connected to agents"** — ตอบ Google Gemini Agent (ที่ประกาศวันที่ 8 ต.ค.) และยืนยันว่า **"copilot = app layer, agent = cross-app layer"** ของ enterprise AI สองค่าย

## เกิดอะไรขึ้น

30 ก.ย. 2026 Microsoft เปิด public preview ของ Work IQ สำหรับผลิตภัณฑ์กลุ่ม Dynamics 365 และ Power Platform. การประกาศทำโดย **James Oleinik** ที่เป็น product management lead สำหรับ Dataverse + Work IQ (post 25 ก.ย.). Rollout ค่อย ๆ ปล่อยถึง ต.ค. 2026, **Finance and Operations (ERP core ของ Microsoft) จะเพิ่มปลาย ต.ค.** — ซึ่งคือ chunk ที่ enterprise รอ

Work IQ สร้างบน 3 primitive:

1. **Semantic model** — layer ที่แปล raw data ใน Dynamics / Dataverse / Power Platform เป็น "business concept" ที่ agent เข้าใจ (customer lifetime value, open opportunity, service case severity, invoice status). ย้ายงาน schema-mapping ที่ developer เคยทำมือใส่ platform

2. **Reusable business skills** — "action primitives" ที่ encode business logic (e.g., "create lead", "escalate case", "approve invoice") แต่ละ skill มี permission scope ของตัวเอง, logging ของตัวเอง, และสามารถถูก compose กันเป็น workflow ยาวได้

3. **Governed actions** — จุดแตกต่างสำคัญ. **Agent ไม่ commit write operation โดยตรง** แต่ propose change, route ให้ user หรือ manager approve, จากนั้น platform commit under permission ของ user ที่ approve. Flow นี้แก้ปัญหา **"agent ทำเสียโดยไม่มีคนรู้"** ที่ CISO กลัวที่สุด

**Scope ที่เปิดก่อน**: Dynamics 365 Sales, Customer Service, Power Apps, + third-party line-of-business apps (ผ่าน Dataverse connector). **Scope ที่รอ**: Finance and Operations (ซึ่งคือ Microsoft ERP) จะ GA ปลาย ต.ค.; Supply Chain Management, Project Operations, Commerce ยังไม่มี timeline. **Billing**: ผ่าน Copilot Credits (ไม่ใช่ seat license) — pattern เดียวกับที่ Microsoft เปลี่ยนจาก Copilot per-seat เป็น Copilot Credit ตั้งแต่ Build 2026

**Sales Agent** ที่ Microsoft เปิดก่อนหน้านี้ (ปี 2025) ตอนนี้สามารถ invoke ได้จากทั้ง Dynamics 365 Sales และ Microsoft 365 — คือ **unified agent surface** ที่ seller ใช้ที่ไหนก็ได้. บาง embedded capability ยัง preview; admin ต้องเช็กก่อน rollout

## ทำไมสำคัญ

**Work IQ คือคำตอบของ Microsoft ต่อ Google Gemini Agent (ที่ประกาศ 8 ต.ค.)**. ทั้งสองค่ายเดินทางเดียวกัน: ขยับ layer value จาก **copilot (ภายใน app)** ไป **agent (ข้าม app)**. ความต่าง: Google Gemini Agent focus **productivity suite** (Gmail, Drive, Docs); Microsoft Work IQ focus **business application** (CRM, ERP, LOB). ลูกค้า enterprise ที่ใช้ทั้ง Microsoft 365 + Dynamics ได้ coverage กว้างสุด — ซึ่งเป็น default ของ Fortune 500 US อยู่แล้ว

**Governed actions = pattern ที่จะกลายเป็น table stakes ภายใน Q1 2027.** ปัญหา "agent write operation โดยไม่ควบคุม" คือ reason ที่ CFO ของ Fortune 500 บล็อก agent rollout จาก IT ตั้งแต่ปี 2024 — เพราะ "ถ้า agent delete 10,000 record ใครรับผิดชอบ?". Microsoft แก้ด้วย propose-then-approve flow + permission under user scope (ไม่ใช่ agent principal แยก). นี่ **ตรงข้ามกับ Google Gemini Agent** ที่ให้ agent มี Workspace account ของตัวเอง — สองวิธี, สอง philosophy. Microsoft ปลอดภัยกว่าในระยะสั้น; Google scaleable กว่าในระยะยาว

**Semantic model = เรื่องที่น่าสนใจกว่า agent ตัวหน้า.** หลายปีที่ enterprise พยายามสร้าง "data catalog" (Collibra, Alation, Atlan) ที่ให้ business user เข้าใจ data ของตัวเอง, ส่วนใหญ่ล้มเหลวเพราะ ownership + maintenance. Work IQ เสนอว่า **semantic model เป็น primitive ของ platform** — ไม่ต้องซื้อ Collibra เพิ่ม, Microsoft maintain ให้. ถ้า Microsoft สำเร็จ จะเป็น existential threat ต่อ data catalog category ทั้งหมด (ที่มี market size ~$3B/ปี) — ภายใน 2-3 ปี. Snowflake Horizon + Databricks Unity Catalog ก็เล่น play เดียวกัน แต่ scope แคบกว่า

## มุม AI Agent Platform

**Builders:** ถ้าสร้าง vertical agent ที่ลูกค้าเป็น Microsoft shop (Dynamics 365 CRM, Finance & Operations ERP, Business Central SMB), ควรเริ่มสำรวจ Work IQ API ตั้งแต่ตอนนี้ — เพราะมันจะเป็น default integration layer ที่ Microsoft customer คาดหวัง. ส่วน builder ที่ขายข้าม Microsoft + Salesforce + SAP ยังต้องรักษา Ampersand / Merge / Workato pattern เพราะ Work IQ ไม่ cover competing CRM/ERP. ส่วนทีมที่สร้าง **semantic layer tool** ของตัวเอง (Cube, Steampipe, Malloy) ต้องพิจารณาจุดยืน — เป็น alternative ของ Microsoft สำหรับ non-Microsoft stack, หรือเป็น complement ที่เสริม Work IQ

**Users / business:** CIO ของบริษัทที่อยู่ Microsoft stack (ซึ่งคือ **80%+ ของ Fortune 500**) ควรเริ่ม pilot Work IQ ก่อน Finance and Operations GA ปลาย ต.ค. — เพราะเมื่อ ERP เพิ่มเข้ามา จะเจอ queue preview + onboarding ยาว. บริษัทไทยที่ใช้ Dynamics 365 (ส่วนใหญ่คือ bank, insurance, retail chain ขนาดกลาง-ใหญ่) ควรเตรียม semantic model mapping + governed action policies ตั้งแต่ตอนนี้. **Ecosystem:** Partner ที่ขาย Dynamics implementation (Avanade, Hitachi Solutions, Columbus) ได้ revenue stream ใหม่จาก Work IQ configuration services. Independent CRM/ERP vendor (NetSuite, Workday, Oracle Fusion, SAP S/4) ต้องเร่งปลา agent-ready layer ของตัวเอง — ไม่งั้นจะเจอ customer migration pressure ภายใน 18-24 เดือน

## Sources
- [Microsoft Opens Work IQ Preview for Dynamics 365 and Power Platform Data — ERP Today](https://erp.today/microsoft-opens-work-iq-preview-for-dynamics-365-and-power-platform-data)
- [Microsoft Sales Agent in Dynamics 365 CE/CRM: What has Changed with Copilot Cowork and Work IQ — MSDynamicsWorld](https://msdynamicsworld.com/blog-post/microsoft-sales-agent-dynamics-365-cecrm-what-has-changed-copilot-cowork-and-work-iq)
- [Work IQ: Business and workplace intelligence in the flow of work — Microsoft Dynamics 365 Blog](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/09/25/work-iq-business-and-workplace-intelligence-in-the-flow-of-work/)
- [Microsoft's Work IQ Gets Down to Business, and That's What Makes Agents Useful — Cloud Wars](https://cloudwars.com/ai/microsofts-work-iq-gets-down-to-business-and-thats-what-makes-agents-useful/)
- [Copilot Work IQ Public Preview Adds Dynamics 365, Power Platform Data — Windows Forum](https://windowsforum.com/news/copilot-work-iq-public-preview-adds-dynamics-365-power-platform-data.446041/)

---

## Audio script
30 กันยายน Microsoft เปิด public preview ของ Work IQ สำหรับ Dynamics 365 Sales และ Customer Service บวก Power Apps บวก third party line of business apps. ประกาศโดย James Oleinik ที่เป็น product lead สำหรับ Dataverse และ Work IQ. Finance and Operations ซึ่งคือ ERP core ของ Microsoft จะเพิ่มปลายตุลาคม. Work IQ สร้างบน 3 primitive. หนึ่ง semantic model ที่แปล raw data ใน Dynamics เป็น business concept ที่ agent เข้าใจ. สอง reusable business skills ที่ encode business logic เช่น create lead escalate case approve invoice. สาม governed actions — จุดแตกต่างสำคัญ. Agent ไม่ commit write operation โดยตรง แต่ propose change route ให้ user หรือ manager approve แล้ว platform commit under permission ของ user ที่ approve. Flow นี้แก้ปัญหา agent ทำเสียโดยไม่มีคนรู้ ที่ CISO กลัวที่สุด. ความสำคัญ: Work IQ คือคำตอบของ Microsoft ต่อ Google Gemini Agent ที่ประกาศ 8 ตุลาคม. ทั้งสองค่ายเดินทางเดียวกัน — ขยับ layer value จาก copilot ภายใน app ไป agent ข้าม app. ความต่าง Google focus productivity suite Gmail Drive Docs. Microsoft focus business application CRM ERP LOB. ลูกค้า enterprise ที่ใช้ทั้งคู่ได้ coverage กว้างสุด ซึ่งเป็น default ของ Fortune 500 US. Governed actions จะกลายเป็น table stakes ภายใน Q1 2027. ปัญหา agent write operation โดยไม่ควบคุม คือเหตุที่ CFO Fortune 500 บล็อก agent rollout ตั้งแต่ปี 2024. Microsoft แก้ด้วย propose then approve flow บวก permission under user scope ไม่ใช่ agent principal แยก. นี่ตรงข้ามกับ Google Gemini Agent ที่ให้ agent มี Workspace account ของตัวเอง. CIO ไทยที่ใช้ Dynamics 365 ควรเตรียม semantic model mapping และ governed action policies ตั้งแต่ตอนนี้ ก่อน ERP เพิ่มเข้ามาปลายตุลาคม
