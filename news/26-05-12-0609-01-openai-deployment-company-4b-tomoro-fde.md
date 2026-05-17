---
date: 2026-05-11
slug: openai-deployment-company-4b-tomoro-fde
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: A hero illustration of a giant glowing OpenAI logo emblem at the center of a wide corporate boardroom, with silhouettes of consultants in suits walking out from the logo like a workforce being deployed into smaller skyscrapers labeled with industry tags (BANK, RETAIL, HEALTH, GOV). In bold massive condensed white sans-serif headline overlaid at top reads "$4B + 150 FDEs". A smaller second-line label beneath reads "OpenAI Deployment Company". Editorial dark teal and electric orange palette, high contrast, magazine-cover composition, 1:1 aspect, no real human faces (only silhouettes allowed). Style The Information / Stratechery cover art with cinematic depth and corporate hard light.
image: images/26-05-12-0609-01-openai-deployment-company-4b-tomoro-fde.png
---

# OpenAI สร้าง "บริษัทขาย deployment" $4B ของตัวเอง — ซื้อ Tomoro 150 FDE, ดึง TPG/Advent/Bain/Brookfield ร่วมเป็น partner, เปิด services era ของ frontier AI

## TL;DR
- 11 พ.ค. 2026 OpenAI ปล่อย **OpenAI Deployment Company** หน่วยใหม่ใต้ majority control — initial fund **$4B จาก 19 partners** lead by **TPG** + co-lead **Advent / Bain Capital / Brookfield** + founding partner BBVA / Goldman Sachs / SoftBank / Warburg Pincus / WCAS / Emergence / B Capital / Goanna
- ซื้อ **Tomoro** บริษัท applied AI consulting จาก London (ตั้งปี 2023) ดึง ~**150 Forward Deployed Engineers** เข้าวันแรก — Tomoro มีลูกค้าเดิม Mattel / Red Bull / Tesco / Virgin Atlantic; valuation รวมของ unit อยู่ที่ **$14B** (รายงาน Axios)
- **Frame ใหม่ของเกม:** frontier model ไม่พอ — ตลาด enterprise ต้องการ "deployment engineering as a service" และ OpenAI accept ว่าจะ compete กับ Accenture/Deloitte/IBM ในชั้น services อย่างเปิดเผย ไม่ใช่ปล่อยให้ partner ตัวเองเก็บ margin ทั้งหมด

## เกิดอะไรขึ้น

OpenAI ประกาศ 11 พ.ค. 2026 ก่อตั้ง **OpenAI Deployment Company** — บริษัท services ใหม่ที่ majority-owned โดย OpenAI แต่เปิด equity ให้ 19 พันธมิตร global investment firms / consultancies / system integrators ใส่เงินรวม **$4B** เพื่อขยาย operations ทันที lead investor คือ **TPG** ตามด้วย co-lead **Advent / Bain Capital / Brookfield** และ founding partner ที่หลายชื่อ surprising ไม่ใช่ consulting house ทั่วไป — **BBVA** ธนาคารใหญ่ของสเปน, **Goldman Sachs**, **SoftBank Corp**, **Warburg Pincus**, **WCAS**, **Emergence Capital**, **B Capital**, **Goanna** การที่ Goldman + BBVA ลงทุนเอง signals ว่า bank ต้องการ deployment capability ฝังตรงข้างใน partnership นี้ — ไม่ใช่ outsource ให้ Accenture/IBM ต่อ

ตัว vehicle ที่ทำให้ unit นี้ "ไม่ใช่ slide deck" คือ acquisition ของ **Tomoro** — applied AI consulting + engineering firm ก่อตั้ง 2023 ที่ London ที่มี partnership ก่อนหน้ากับ OpenAI ตรงอยู่แล้ว ทีม Tomoro ~150 คนส่วนใหญ่เป็น **Forward Deployed Engineer (FDE)** + Deployment Specialist ที่เคย ship production AI ที่ **Mattel / Red Bull / Tesco / Virgin Atlantic** — model เดียวกับ Palantir FDE ที่ฝัง engineer ในลูกค้าเพื่อ co-design + ship workflow Tomoro CEO Charlie Cardin ใน statement บอกว่า "we built Tomoro around the conviction that the next decade of business value comes from teams who actually deploy AI inside real organizations, not from those who advise from the outside" — language ที่จิกตรง McKinsey/BCG

OpenAI Deployment Company จะ scale FDE pool จาก 150 ไปเป็นพันคน (รายงาน Axios) โดย valuation รวมของ unit แตะ **$14B** จาก partner equity ลำดับงานคือ partner กับ enterprise / government / regulated industry แต่ละราย แล้ว embed engineer ตรงข้างใน redesign workflow ใหม่รอบ "AI ที่ reason + act + measure result" — pricing คาดว่าจะเป็น hybrid services fee + revenue share จาก AI consumption ของลูกค้า (รายละเอียดยังไม่เปิดเผย)

## ทำไมสำคัญ

หกเดือนที่ผ่านมา pattern ของ FDE-as-a-service เป็น signal ที่ดังที่สุดในตลาด enterprise AI — Anthropic ฝัง Applied AI team กับ FIS เพื่อ build Financial Crimes Agent (4 พ.ค.), ServiceNow จับ Accenture เปิด FDE program (6 พ.ค.), Sierra ส่ง engineer เข้าลูกค้า Fortune 50 (round $950M เพิ่ง close 4 พ.ค.) ความจริงที่ทุก vendor ยอมรับร่วมกันคือ **frontier model ไม่ขายตัวเอง** — buyer ใหญ่ทุกรายต้องการ engineer ที่นั่งข้างใน redesign critical workflow ของตัวเอง ไม่ใช่ API documentation + Slack support ตัว OpenAI โดดเข้าเล่น service layer ของตัวเอง mean ว่าจะไม่ยอมให้ Accenture/IBM/Deloitte เก็บ services margin (โดยทั่วไป **3-7x ของ software ARR**) ในขณะที่ OpenAI ขาย token ราคาแข่ง

จุดที่ขัดหู contrarian: นี่คือ admission ว่า model API alone **commoditize ลงเร็วกว่าคาด** ก่อนหน้า OpenAI position เป็น "infrastructure ระดับ AWS for AI" — vendor neutral, ขายผ่าน partner; แต่ใน reality สี่ปี deploy enterprise AI พบว่า workflow integration เป็น value 70-80% — ไม่ใช่ model accuracy งานต้องอาศัย FDE ที่เข้าใจ data pipeline + IT policy + change management — capability ที่ OpenAI เคย refuse ที่จะ scale (เพราะเป็น "ไม่ scalable") ตอนนี้ OpenAI เปลี่ยนใจ: scale ผ่าน Tomoro + partner equity เพื่อ split risk การที่ Goldman + BBVA ลงทุน founding mean ว่า bank ต้องการ deployment muscle ที่ไม่ pass through consulting firm — เป็น proof point ว่า financial services market พร้อมจ่าย premium สำหรับ direct access ไม่ใช่ระดับ Magic Quadrant

อีก angle ที่จะเล่นออกในไตรมาสนี้: Microsoft + Anthropic + Google จะตอบยังไง Microsoft มี Consulting + Industry Solutions แต่ structure ของ Microsoft เปิด margin ให้ partner ecosystem (เช่น Avanade) Anthropic มี Applied AI team + FDE แต่ขนาดเล็กกว่า OpenAI ตอนนี้แล้ว Google มี Vertex Industry Cloud + Google Cloud Consulting แต่ไม่มี standalone services entity ระดับ $4B 90 วันข้างหน้าน่าจะมี Anthropic / Google ออก services arm ของตัวเองตอบในระดับ scale คล้ายกัน เพราะ buyer cycle ของ enterprise AI กำลัง consolidate เร็ว และคนที่ขาย AI โดยไม่มี FDE attached จะแพ้ deal

## มุม OpenBridge

OpenAI Deployment Company คือ signal ที่ดังที่สุดว่า **OpenBridge ต้อง position ที่ "infrastructure ที่ FDE ของ frontier vendor ใช้"** ไม่ใช่ alternative ของ FDE ภายใน 12 เดือนทุก enterprise deal ใน Thai/SEA จะมี OpenAI/Anthropic/Google FDE หรือ Tomoro / Accenture / Deloitte FDE เป็น decision maker คนหนึ่ง — OpenBridge ต้อง make sure ว่า MCP connector + audit trail ของเราเป็น default tooling ในกระเป๋า FDE ทุกคน ไม่ใช่ third-party option ที่ต้อง propose แล้ว เพราะถ้า FDE คนหนึ่งใช้ OpenBridge ใน deal แรก จะใช้ใน 10 deal ถัดไป

Action ตรง: เปิด **OpenBridge for Forward Deployed Engineers** program — free tier สำหรับ FDE individual (Anthropic Applied AI / OpenAI Deployment / Sierra / Tomoro / ServiceNow FDE) ที่ใช้ในลูกค้าตัวเอง + sales motion ตรงกับ practice lead ของ Tomoro และ Accenture/Deloitte AI Practice ใน SEA — pitch ว่า "Workday/SAP/Encompass/Guidewire/SET connector ที่ FDE ไม่ต้อง rebuild ทุก deployment + audit trail ที่ผ่าน Bank of Thailand inspection ได้" สิ่งที่ FDE ขาดที่สุดในงาน implementation คือ **boring connector ที่ enterprise IT accept** — และ OpenBridge ขาย commodity ที่ดูเหมือนน่าเบื่อแต่เป็น critical path

## Sources
- [OpenAI launches the OpenAI Deployment Company to help businesses build around intelligence — OpenAI](https://openai.com/index/openai-launches-the-deployment-company/)
- [OpenAI launches AI consulting arm valued at $14 billion — Axios](https://www.axios.com/2026/05/11/openai-deployco-private-equity)
- [OpenAI launches $4B enterprise AI unit to accelerate corporate adoption, acquires Tomoro to scale deployments — Tech Startups](https://techstartups.com/2026/05/11/openai-launches-4b-enterprise-ai-unit-to-accelerate-corporate-adoption-acquires-tomoro-to-scale-deployments/)
- [OpenAI Acquires Tomoro, Gets Access 150 Forward Deployed Engineers — OfficeChai](https://officechai.com/ai/openai-deployment-company-acquires-tomoro/)
- [OpenAI Launches $4 Billion Company to Accelerate Enterprise AI Adoption — PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/openai-launches-4-billion-dollar-company-accelerate-enterprise-ai-adoption/)

---

## Audio script
สวัสดีครับ Yoh วันนี้ 11 พฤษภาคม OpenAI ปล่อยข่าวใหญ่ ก่อตั้ง OpenAI Deployment Company บริษัท services ของตัวเองด้วยเงินตั้งต้น 4 พันล้านดอลลาร์ TPG เป็น lead investor มี Advent Bain Capital Brookfield ร่วมเป็น co-lead และมี Goldman Sachs BBVA SoftBank Warburg Pincus ลงทุนเป็น founding partner รวม 19 ราย วันเดียวกันซื้อ Tomoro บริษัท AI consulting จาก London ดึง 150 Forward Deployed Engineer เข้าวันแรก ลูกค้าเดิมของ Tomoro คือ Mattel Red Bull Tesco Virgin Atlantic ราคา valuation รวมของ unit แตะ 14 พันล้านดอลลาร์ Frame ใหม่ของเกมคือ frontier model อย่างเดียวขายไม่ออก ตลาด enterprise ต้องการ engineer ที่ฝังเข้าไปข้างใน redesign workflow ของลูกค้า ก่อนหน้านี้ทุกอย่างที่เป็น services layer Accenture Deloitte IBM เป็นคนเก็บ margin 3 ถึง 7 เท่าของ software ARR ตอนนี้ OpenAI ไม่ยอมแล้ว ลงมาแข่งเอง ภายใน 90 วันข้างหน้า Anthropic กับ Google น่าจะตอบด้วย services arm ของตัวเองเหมือนกัน สำหรับ OpenBridge signal คือเราต้อง position เป็น infrastructure ที่ FDE ของทุก frontier vendor ใช้ ไม่ใช่ alternative ของ FDE เพราะภายใน 12 เดือน FDE จะเป็น decision maker คนหนึ่งในทุก enterprise deal ครับ
