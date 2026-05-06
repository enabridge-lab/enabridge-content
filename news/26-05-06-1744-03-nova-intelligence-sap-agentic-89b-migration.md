---
date: 2026-05-06
slug: nova-intelligence-sap-agentic-89b-migration
topic: use-case
reading_time_min: 5
sources: 5
image_prompt: A massive cream-colored monolithic vault labeled "S/4HANA" cracks down the middle in the center of the frame, with abstract geometric agent figures (no faces, slate blue silhouettes) carrying glowing amber code blocks out through the crack toward a sunrise horizon of small Fortune 500 office towers. A bold coral headline "$89B" floats in the upper-right in cream sans-serif, with a smaller "5x FASTER" badge in the lower-left. Editorial illustration, flat geometric shapes with subtle grain, cream + slate blue + amber + coral palette on a deep navy background, dramatic side-lighting from a rising sun. No real human faces. 1:1 aspect.
image:
---

# Nova Intelligence ปิด $31.5M Series A — agentic AI ลงไปจับ SAP $89B migration wave, Festo รัน "เดือน → 1 วัน" เร็วขึ้น 5 เท่า, Kyndryl ลด manual 75%

## TL;DR
- **5 พ.ค.** — Nova Intelligence (San Francisco, **Emma Qian** founder) ประกาศ Series A **$31.5M** นำโดย **Chemistry**, รวม total funding **$40M+**; โฟกัสแคบ: agentic AI สำหรับ SAP custom code modernization บนเส้น migration ไป S/4HANA
- ตลาดเป้าหมาย: **$89B** ตามที่ analyst ประมาณการรวม implementation + upgrade + ongoing support ของ SAP customer 35,000+ รายที่ต้อง migrate ภายใน **deadline 2030 ที่ SAP บังคับ**
- ตัวเลข deployment จริง — **Kyndryl case study เม.ย. 2025: ลด manual effort 75% + ลด cost 50%**; **Festo (SAP customer 30 รายแรกของโลก, รัน SAP ตั้งแต่ 1970s): เร็วขึ้น 5 เท่า, program ที่เคยใช้เวลา "หลายเดือน" → 1 วัน**
- Signal: vertical agent ที่ทุก VC ลังเลในปี 2025 (กลัว frontier lab กลืน) เริ่มแสดง defendable moat — Nova ฝัง **proprietary SAP knowledge graph** + **process intelligence จาก SAP iO Fund relationship** ที่ Claude/GPT raw ทำไม่ได้

## เกิดอะไรขึ้น

Fortune ปล่อย exclusive วันที่ 5 พ.ค. — Nova Intelligence ปิด Series A $31.5M led by Chemistry. ขนาดเงินไม่ใหญ่เมื่อเทียบ Sierra ($950M) หรือ Anthropic ($50B) แต่ thesis แคบ คม ขายง่าย: **บริษัท Fortune 500 ที่รัน SAP มา 30 ปี ต้อง migrate code legacy ไป S/4HANA ภายในปี 2030 — และไม่มี internal team ขนาดที่ทำได้ทัน**

ตัวเลขที่ทำให้ deal สวย: SAP มี customer 35,000+ ราย, ส่วนใหญ่มี **custom ABAP code 5-15 ล้านบรรทัด** ที่เขียนทับกันมาตลอด 2-3 decade — payroll, supply chain, finance core. Migration ไป S/4HANA ไม่ใช่ lift-and-shift ธรรมดา เพราะ S/4HANA ใช้ data model ใหม่ (universal journal, in-memory HANA), เลิก support ABAP feature เก่าหลายตัว, และต้อง **clean core** ก่อน apply patch อนาคตได้. Analyst บางคนมอง $89B รวม implementation + upgrade + support; consultancy big 4 ตีราคา deal Fortune 500 ที่ $30-100M ต่อราย, timeline 18-36 เดือน — Nova เสนอลด timeline ลง 50-75% ด้วย agent

ของจริงที่ Nova ขาย: agent **อ่าน custom ABAP code → ระบุว่า code ตัวไหน redundant / เทียบกับ SAP standard / ต้อง rewrite — แล้ว generate รหัส clean core ใหม่อัตโนมัติ**. ไม่ใช่ transpile, เป็น semantic rewrite ที่เข้าใจ business logic. เคสที่ Nova ยกขึ้นมาในการระดมทุน: **Festo** — เป็น 30 บริษัทแรกของโลกที่ใช้ SAP ตั้งแต่ทศวรรษ 1970, มี ABAP code base ที่ซับซ้อนที่สุดในวงการ, **ระบุว่า "บางโปรแกรมที่ใช้เวลาเป็นเดือน ตอนนี้ทำเสร็จใน 1 วัน — เร็วกว่าเดิม 5 เท่า"** (คำพูดจาก Festo CIO ใน case study). Kyndryl case study เม.ย. 2025 (ก่อน round นี้ 1 ปี): **75% reduction in manual effort, 50% cost reduction** — ตัวเลขที่ทำให้ Chemistry ลงทุน

จุดที่น่าสนใจ: Nova ได้ **strategic investment จาก SAP iO Fund** (SAP venture arm) ในรอบ seed ก่อนหน้า — เปิดประตู process intelligence + knowledge graph ที่ดึงตรงจาก SAP product team. นี่คือ moat ที่ Claude/GPT ที่ raw ทำไม่ได้ — **ใครก็ generate ABAP code ได้ แต่ใครจะรู้ว่าใน Q3 2026 SAP จะเลิก support feature ตัวไหน** (insider knowledge ที่ค่อยปล่อยใน community 6 เดือน). Sequoia/Andreessen ผ่านดีลนี้ไป — Chemistry ที่เป็น emerging fund ของ Naval Ravikant + Mark Pincus เข้ามาแทน. Emma Qian (founder, ex-McKinsey + ex-Google) เน้น GTM ผ่าน Fortune 500 logo: ตอนนี้ Nova มี deal จริงกับลูกค้า "Big Pharma + Big Energy + Big Bank" ที่ยังไม่เปิดเผยชื่อ

ใครคู่แข่ง: **Kyndryl (ที่เป็น Nova customer ด้วย)** มี Agentic AI Custom Code Modernization ของตัวเองด้วย, **WalkMe + Gainsight** มี SAP enablement layer, **Accenture/Deloitte SAP practice** มี internal automation ที่ใช้ Claude/GPT generate ABAP. แต่ Nova เน้น **SAP-native agent** ที่ฝัง knowledge graph เฉพาะ — ของแบบนี้ services firm ใหญ่ทำเองไม่ได้เพราะไม่มี SAP iO relationship + ไม่ scale modular product

## ทำไมสำคัญ

Pattern ที่กลับมาในรอบ 6 เดือน: **vertical agent ที่ลึก > horizontal agent ที่กว้าง** ใน enterprise spend. ปี 2024-2025 VC เทเงินเข้า horizontal platform (LangChain, CrewAI, AutoGen — สวยที่ developer mindshare) แต่ payback ตามไม่ทัน เพราะ enterprise ไม่ซื้อ "framework เพื่อ build เอง" — ซื้อ "agent ที่ทำงาน job เดียวเสร็จ". Nova คือ proof ในด้านที่ลึกที่สุด — SAP custom code — ที่ไม่มีคู่ต่อกร horizontal เพราะ moat = knowledge graph + process intelligence

POV ที่สำคัญ: **frontier lab จะไม่ลง vertical SAP** เพราะ market segment เล็กเกินใน lens ของ OpenAI/Anthropic ($89B / 35,000 customer = avg $2.5M/customer/lifetime หาร 5 ปี = $500k/year — ไม่ใหญ่พอจะดึง compute attention ของ frontier lab). ตรงข้ามกับ financial services ($40B/year + 1B+ end user หากนับ retail banking) ที่ Anthropic ลงเอง. Vertical ที่ไม่ฮอตในข่าวแต่ "เงียบ ๆ ใหญ่และ defendable" จะ shape return ของ portfolio ปี 2026-2027 มากกว่า horizontal play

จุด trade-off: Nova ต้อง **race ต่อ deadline 2030 ของ SAP** — ถ้า SAP ยอมยืดเวลา migration หรือเปลี่ยน roadmap (ที่ Larry Ellison ของ Oracle เคยใช้ FUD โจมตีว่าทำไม่ทันแน่), Nova เสีย urgency. แต่จากที่ SAP ตอกย้ำ deadline ใน earnings call สามไตรมาสติด, urgency ยังจริง. Risk รอง: ถ้า Microsoft ออก Copilot Studio extension สำหรับ SAP integration (rumor มี deal ทั้งสอง), Nova ต้อง pivot ไปจับ migration เฉพาะ ABAP semantic — ไม่ใช่ generic SAP integration

## มุม OpenBridge

**ไม่ direct เกี่ยว** — OpenBridge ไม่อยู่ในตลาด SAP migration. แต่ **adjacent insight ที่ใช้ได้:**

(1) **Vertical depth = pricing power ที่ horizontal play ไม่มี** — Nova ขายลูกค้าได้ด้วย "5x faster, 75% manual reduction" ตัวเลขที่ตรงกับ business outcome ที่ CFO เซ็นได้. OpenBridge ที่ตอนนี้ pitch generic "build agentic workflow" แข่งกับ Workato/Zapier/n8n ที่ราคาต่ำลง — ต้อง pick **1 vertical ที่ Thai SMB เจ็บ** แล้วดำลึก. Candidates: **SME accounting close (FlowAccount/PEAK migration → AI bookkeeping)**, **e-commerce returns/refund flow (Shopee/Lazada vendor automation)**, **HR onboarding for restaurant/retail**. เลือก 1 — ในรอบ 6 เดือน จับ benchmark "X% time saved, Y% cost reduction" จาก customer 3-5 ราย แล้ว publish

(2) **Knowledge graph + process intelligence เป็น moat ที่ build ได้ถ้าฝังลึก** — Nova ใช้ SAP iO relationship แลกความรู้ insider. OpenBridge ทำได้กับ **FlowAccount, PEAK, K-Cloud** ในไทย — ของพวกนี้ team เล็ก, OpenBridge ใหญ่กว่า, มีโอกาสเซ็น strategic partnership ที่ดึง schema updates 6 เดือนก่อน community ทั่วไป. Moat ที่ Microsoft/OpenAI ทำไม่ได้

(3) **Nova case study เป็น playbook ที่ copy ได้สำหรับ Yoh** — Festo case (30 บริษัทแรกของโลกที่ใช้ SAP ตั้งแต่ 1970s, "เดือน → 1 วัน, 5x faster") เป็น marketing material level สูงสุดที่ enterprise CFO อ่านจบจะอยากซื้อทันที. OpenBridge ต้องมี **1 case study ระดับนี้** ใน Thai enterprise (โรงงาน Siam Cement, CP, Charoen Pokphand, ฯลฯ) ก่อนสิ้นปี — ลงไปช่วย customer ฟรีถ้าจำเป็นเพื่อให้ได้ logo + numbers ที่กลายเป็น sales asset ตลอด 2027

## Sources
- [Exclusive: Nova Intelligence raises $31.5 million to bring agentic AI to SAP's $89 billion migration wave (Fortune)](https://fortune.com/2026/05/05/exclusive-nova-intelligence-ai-sap-chemistry-emma-qian/)
- [Nova Intelligence — Agentic AI for SAP Modernization (company)](https://www.novaintelligence.com/)
- [Nova Intelligence Announces Strategic Investment from SAP iO Fund (Nova blog)](https://www.novaintelligence.com/post/saps-strategic-investment-in-nova-intelligence)
- [Agentic AI for accelerated SAP Custom Code Modernization (Kyndryl)](https://www.kyndryl.com/us/en/services/applications/sap/agentic-ai)
- [Nova Intelligence raises $31.5M Series A led by Chemistry (Shopifreaks)](https://www.shopifreaks.com/nova-intelligence-raises-31-5m-series-a-led-by-chemistry-to-bring-agentic-ai-to-saps-89b-migration-wave/)

---

## Audio script
ห้าพฤษภา Fortune ปล่อย exclusive. Nova Intelligence ปิด Series A สามสิบเอ็ดจุดห้าล้านดอลลาร์. นำโดย Chemistry. รวม total funding สี่สิบล้าน. โฟกัสแคบมาก. agentic AI สำหรับ SAP custom code modernization บนเส้น migration ไป S 4 HANA.

ตลาดที่ Nova เล็ง. SAP มี customer สามหมื่นห้าพันราย. ส่วนใหญ่มี custom ABAP code ห้าถึงสิบห้าล้านบรรทัด เขียนทับกันมายี่สิบสามสิบปี. payroll supply chain finance core. SAP บังคับทุกรายต้อง migrate ไป S 4 HANA ภายในสองพันสามสิบ. analyst ตีราคารวมตลาดที่แปดสิบเก้าพันล้านดอลลาร์. consultancy big 4 ตีราคา deal Fortune 500 ที่สามสิบถึงร้อยล้านต่อราย. timeline สิบแปดถึงสามสิบหกเดือน. Nova เสนอลด timeline ห้าสิบถึงเจ็ดสิบห้าเปอร์เซ็นต์ด้วย agent.

ของจริงที่ Nova ขาย. agent อ่าน custom ABAP code. ระบุว่าตัวไหน redundant. เทียบกับ SAP standard. ต้อง rewrite. generate รหัส clean core ใหม่อัตโนมัติ. ไม่ใช่ transpile. เป็น semantic rewrite ที่เข้าใจ business logic.

เคสที่ Nova ยก. Festo. หนึ่งในสามสิบบริษัทแรกของโลกที่ใช้ SAP ตั้งแต่ทศวรรษเจ็ดสิบ. มี ABAP code base ซับซ้อนที่สุดในวงการ. CIO ระบุ บางโปรแกรมเคยใช้เวลาเป็นเดือน ตอนนี้ทำเสร็จในวันเดียว เร็วกว่าเดิมห้าเท่า. Kyndryl case study เมษายนปีก่อน. ลด manual effort เจ็ดสิบห้าเปอร์เซ็นต์ ลด cost ห้าสิบเปอร์เซ็นต์.

moat ที่ Claude GPT raw ทำไม่ได้. Nova ได้ strategic investment จาก SAP iO Fund. เข้าถึง process intelligence knowledge graph จาก SAP product team. ใครก็ generate ABAP ได้. แต่ใครจะรู้ว่า Q3 2026 SAP จะเลิก support feature ตัวไหน. insider knowledge ที่ปล่อยใน community ช้ากว่าหกเดือน.

pattern ที่กลับมาในหกเดือน. vertical agent ที่ลึก กินเงินมากกว่า horizontal agent ที่กว้าง. VC เทเงินเข้า horizontal LangChain CrewAI AutoGen ปี 2024 2025. payback ตามไม่ทัน. enterprise ไม่ซื้อ framework เพื่อ build เอง. ซื้อ agent ที่ทำงาน job เดียวเสร็จ.

POV ของผม. frontier lab จะไม่ลง vertical SAP. market segment เล็กเกินใน lens ของ OpenAI Anthropic. แปดสิบเก้าพันล้านหาร สามหมื่นห้าพัน customer หาร ห้าปี ได้ห้าแสนต่อปี. ไม่ใหญ่พอดึง compute attention. vertical ที่ไม่ฮอตในข่าวแต่เงียบใหญ่ defendable จะ shape return portfolio สองพันยี่สิบหก ยี่สิบเจ็ดมากกว่า horizontal play.

สำหรับ OpenBridge. ไม่ direct เกี่ยวกับ SAP. แต่ adjacent insight สามข้อ. หนึ่ง vertical depth equal pricing power ที่ horizontal play ไม่มี. ต้อง pick หนึ่ง vertical ที่ Thai SMB เจ็บ. SME accounting close. e commerce returns. HR onboarding restaurant retail. เลือกหนึ่ง. หกเดือนจับ benchmark X เปอร์เซ็นต์ time saved Y เปอร์เซ็นต์ cost reduction จาก customer สามถึงห้าราย. publish. สอง knowledge graph เป็น moat ที่ build ได้. partner กับ FlowAccount PEAK K Cloud ดึง schema updates หกเดือนก่อน community. moat ที่ Microsoft OpenAI ทำไม่ได้. สาม Festo case คือ playbook copy ได้. OpenBridge ต้องมีเคสระดับ Siam Cement CP Charoen Pokphand ก่อนสิ้นปี. ลงไปช่วยฟรีถ้าจำเป็น. ได้ logo บวก numbers ที่กลายเป็น sales asset ตลอด สองพันยี่สิบเจ็ด.
