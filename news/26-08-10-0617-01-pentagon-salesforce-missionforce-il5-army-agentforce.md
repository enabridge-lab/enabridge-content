---
date: 2026-08-05
slug: pentagon-salesforce-missionforce-il5-army-agentforce
topic: use-case
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial illustration of a massive stone Pentagon building with a glowing
  Salesforce cloud symbol lifting off its center like a launched rocket;
  three floating stacked numbers "55M CONVERSATIONS/MONTH", "$6M SAVED",
  "IL5 AUTHORIZED"; muted navy, military green, and gold palette;
  soldiers as silhouettes at the base; flat editorial isometric style;
  dramatic rim lighting; 1:1 aspect; no real human faces.
image: images/26-08-10-0617-01-pentagon-salesforce-missionforce-il5-army-agentforce.png
---

# Pentagon เปิดให้ Salesforce Agentforce เข้า IL5 — Army HRC เป็นหน่วยแรกใช้ AI agent รับ 55M call/เดือน, ประหยัด $6M/ปี, ตามหลังสัญญา $5.6B ต้นปี

## TL;DR
- **5 ส.ค.** Salesforce ประกาศ **Missionforce National Security ได้ Impact Level 5 (IL5) authorization** จาก Department of War — เป็น **AI agent ตัวแรก** ที่ได้ clearance ระดับนี้ในตลาด federal defense
- **U.S. Army Human Resources Command (HRC)** เป็น customer แรก — deploy Agentforce 360 รับ **55 ล้าน conversations ต่อเดือน**, ประหยัด **~$6M/ปี**, บริการ **9.2 ล้าน soldiers/veterans/civilian staff/military families** แบบ 24/7
- ตามหลังสัญญา **$5.6 พันล้าน** ที่ Salesforce ชนะเมื่อ **มกราคม** สร้าง Missionforce platform — วันนี้แสดงว่าสัญญาเปลี่ยนเป็น production ได้จริง
- Signal: **agent ระดับ FedRAMP High + IL5** เปิดตลาด government agentic AI ที่ก่อนหน้านี้ถูก block โดย compliance; ทุก vendor ที่ยังไม่มี IL5 (Anthropic, OpenAI, xAI) ต้องเร่ง — และ Thai government sector มี playbook ให้ copy ได้ทันที

## เกิดอะไรขึ้น

วันอังคารที่ 5 ส.ค. Salesforce ประกาศว่า **Missionforce National Security** — platform เฉพาะสำหรับหน่วยงานความมั่นคง — ได้รับ **Impact Level 5 (IL5) authorization** จาก Department of War (เปลี่ยนชื่อจาก DoD เมื่อเมษาที่ผ่านมา). IL5 คือ classification สำหรับ **Controlled Unclassified Information ที่ mission-critical** — สูงกว่า IL4 หนึ่งขั้น รองรับ workload ที่การรั่วไหลจะกระทบ operational security. นี่คือ **AI agent commercial platform แรก** ที่ได้ clearance นี้ เปิดทางให้ Agentforce 360 ทั้ง portfolio (agent + data cloud + apps) เข้าไปรัน workload ในสภาพแวดล้อมที่ก่อนหน้านี้เข้าไม่ได้

**U.S. Army Human Resources Command (HRC)** — หน่วยที่ดูแล personnel record, benefits, promotion, retirement transition ของกำลังพลทั้งหมด — เป็นลูกค้าแรก และตัวเลขที่ Salesforce disclose คือของจริง ไม่ใช่ pilot: **agent จะรับ 55 ล้าน conversations ต่อเดือน** ผ่าน call center + chat + email + form intake, **ประหยัด ~$6 ล้านต่อปี** จาก human agent workload ที่โยกไป AI, และ **บริการประชากรรวม 9.2 ล้านคน** — soldier active + Reserve + National Guard + veteran + civilian staff + military family — แบบ 24/7 ใน 3-4 ภาษา. Marc Benioff quote ในงาน: "This is the largest deployment of trusted autonomous AI in the history of the U.S. government" — คำที่หนักแต่ตัวเลขรองรับได้

ดีลนี้ตามหลังชัยชนะสัญญา **$5.6 พันล้าน** ที่ Salesforce เซ็นกับ Pentagon เมื่อ **มกราคม 2026** สร้าง Missionforce เป็น dedicated tenant ของ Salesforce Government Cloud Plus (FedRAMP High + DoD IL5). ระหว่างเดือน ม.ค. ถึง ส.ค. ทีม Salesforce Federal + Army HRC ทำงาน parallel — **build platform + train agent + get IL5 authorization + integrate legacy system** — 7 เดือน. ในตลาด government IT ที่ปกติ deployment cycle 18-24 เดือน, ตัวเลข 7 เดือนนี้เป็น velocity ที่ทำให้ competitor (Deloitte + Palantir + Booz Allen ที่ทำ agent-adjacent workload) ต้องเร่ง

**เจาะลึก workload**: HRC เผชิญ backlog **1.2 ล้าน case ที่ค้างเกิน 6 เดือน** ก่อน deployment. Agentforce ตอบ 68% ของ inquiry ในระดับที่ user rate satisfaction ≥4/5 โดยไม่ต้อง escalate ไป human agent (benchmark การใช้ Klarna's AI ที่ 65-70%). Case ที่ต้อง escalate ก็ได้ **summary + suggested resolution + relevant policy citation** จาก agent — เหลือแค่ soldier support specialist confirm/edit. Army คาดว่าจะ **reduce backlog เหลือต่ำกว่า 3 เดือนภายใน Q4 FY26** (ก.ย.) — ตัวเลขที่ personnel command ไม่เคยเห็นในทศวรรษที่ผ่านมา

Craig McCauley (SVP, Salesforce Public Sector) confirm ต่อ DefenseScoop ว่า **มีอีก 3 หน่วยของ Army + 2 หน่วยของ Navy ที่ signed** — จะประกาศตัวเลข deployment ใน Q4. Salesforce กำลัง scale **Missionforce field team จาก 40 → 200 คน** ภายใน 90 วัน — สัญญาณว่าบริษัทคาดสัญญาต่อเนื่อง

## ทำไมสำคัญ

**IL5 authorization เปลี่ยน landscape ของ government agentic AI** อย่างมีนัยสำคัญ. ก่อนหน้านี้ agent framework จาก Anthropic, OpenAI, xAI, Google — ทั้งหมดติดที่ FedRAMP High ระดับสูงสุด ทำให้ workload ที่ต้องการ IL5 (personnel + finance + intel-adjacent) ยังต้อง fallback ไป script-based RPA หรือ human. Salesforce วันนี้ jump ไป **IL5** เท่ากับ AWS GovCloud/Azure Government (ที่ authorized มาหลายปี) — แต่ **ในระดับ application/agent layer เป็นครั้งแรก**. Anthropic Claude Gov + OpenAI ChatGPT Gov ที่ launch ต้นปี = ยังอยู่ FedRAMP High moderate, ไม่ IL5. คาดว่าทั้งสองต้องเร่ง — ประกาศ IL5 track ภายใน 60 วัน หรือเสียตลาดที่ Salesforce ล็อคก่อน

Pattern ที่น่าสนใจกว่านั้น: **การ productize จากสัญญา contract แบบ traditional government ($5.6B, 7 ปี) → platform product ที่ replicate ได้ทันที**. Missionforce ไม่ใช่ custom-built สำหรับ Army เท่านั้น — เป็น **tenant model** ที่ Navy, Air Force, DHS, DOJ ทุกคน sign แล้ว spin up instance ใหม่ได้ในเวลา 30-60 วัน (แทน 18-24 เดือนของ old-school gov project). นี่คือ **Salesforce cloning ตัวเองใน gov market** — ใช้ product-led growth ในตลาดที่แต่เดิมเป็น services-led. Federal SI (Accenture Federal, Booz Allen, Leidos) โดน disintermediate ที่ layer ล่างสุด — ยัง win integration work แต่ margin ตก 30-50% เพราะ Salesforce eat platform revenue

**Salesforce winning ที่ Agent layer เร็วกว่าที่ analyst คาด** — $800M ARR (Q4 FY26) → **คาดแตะ $1.5B ARR ในสิ้นปี FY27** ถ้า public sector deals ที่ประกาศทยอย convert ตามที่ McCauley บอก. ตัวเลขนี้ทำให้ Marc Benioff อยู่ในสถานะที่ **สามารถ counter-narrative Anthropic-Blackstone Ode และ Palantir AIP** ได้ — โดยไม่ต้อง disclaim strengths ของแต่ละฝ่าย. Wall Street ปกติ price Salesforce ที่ 6-8x forward ARR; ถ้า Agentforce hit $1.5B, market ควร repricing CRM stock ขึ้น 15-25% ในช่วง earnings รอบหน้า

## มุม AI Agent Platform

**Direct implication ต่อ Enabridge / OpenBridge:** ตัวเลข **55M conversations/month × $6M savings** สำหรับ population 9.2M คน = model ที่ replicate ไปที่ **large-scale Thai institution** ได้ทันที: (1) กระทรวงมหาดไทย (call center + citizen service), (2) กรมสรรพากร (tax inquiry), (3) สปสช. (health benefit inquiry), (4) กสิกร/SCB retail banking (customer support). ตัวเลขต่อ population Thai อาจน้อยกว่า (5-10M conversations/month, savings 30-50M บาท/ปี) แต่ **playbook เดียวกัน**: ประเมิน compliance level (Thailand ไม่มี IL5 แต่มี PDPA sensitive-data classification + BOT/OIC regulation), pick platform ที่ pass compliance, ทำ 6-month pilot กับ 1 workflow แล้ว scale. **Enabridge ควรเตรียม whitepaper "Government-Grade Agentic AI for Thai Public Sector" ภายใน 30 วัน** — ตอนที่ Salesforce ประกาศ Thailand deployment (คาดใน Q4/Q1 next FY) จะได้ position เป็น trusted integrator แทนที่จะแข่ง toe-to-toe

**Product action 60 วัน:** (1) **Build "Compliance-First Agent Template" library** — templates ที่ pre-configured กับ Thai PDPA + BOT sensitive-data handling + audit log requirement; (2) **เริ่ม conversation กับ Salesforce Thailand + KPMG Federal Advisory** — เพื่อวาง multi-vendor partnership; Enabridge นำเสนอ Thai language depth + local system integration (สรรพากร eForm, สปสช. API, ธปท. reporting), Salesforce/Palantir เอา platform + compliance certification; (3) **เปิด "Enterprise Concierge" tier** — mimic HRC deployment แต่ scale เล็กกว่า ให้ Thai bank/insurance (KTC, Bangkok Insurance, ทิพยประกันภัย) รับ customer inquiry 24/7 หลายภาษา; charge based on deflection rate (30-40% deflection ที่ satisfaction ≥4/5 = premium tier)

**Strategic signal:** Missionforce = **จุดเปลี่ยนที่ agentic AI จาก "cool tech in slide deck" เป็น "line item ใน government budget"** — และเมื่อ government adopt, private sector regulated industry (finance, healthcare, utility) จะตามใน 6-12 เดือน. Enabridge ต้องเลือก: (a) **compete บน general-purpose Thai agent platform** (pain point: Salesforce/Palantir จะ enter ในปี 2027) หรือ (b) **specialize บน vertical + language + compliance** (defense น่าเหนื่อยไม่คุ้ม แต่ Thai banking + government service ที่ Salesforce ไม่ vertical-ize = window 18-24 เดือน). แนะนำ (b) — และเริ่มวางกลยุทธ์ regulatory relationship (ธปท., คปภ., ดีอี) ตั้งแต่ Q3 นี้

## Sources
- [Missionforce National Security Unveils IL5-Authorized AI Agents and Apps to Drive Decision Advantage, Readiness, and Enhanced Warfighter Support (Salesforce IR)](https://investor.salesforce.com/news/news-details/2026/Missionforce-National-Security-Unveils-IL5-Authorized-AI-Agents-and-Apps-to-Drive-Decision-Advantage-Readiness-and-Enhanced-Warfighter-Support/default.aspx)
- [Pentagon ready to deploy Salesforce AI agents for admin tasks (Military Times)](https://www.militarytimes.com/news/your-military/2026/08/07/pentagon-ready-to-deploy-ai-agents-for-admin-tasks/)
- [Salesforce previews plans to deliver newly authorized 'AI agents' across DOD (DefenseScoop)](https://defensescoop.com/2026/08/05/salesforce-plans-deliver-newly-authorized-ai-agents-across-dod/)
- [Salesforce (CRM) Gets IL5 Clearance For Army AI Agents Serving Millions (Simply Wall St)](https://simplywall.st/stocks/us/software/nyse-crm/salesforce/news/salesforce-crm-gets-il5-clearance-for-army-ai-agents-serving)
- [Salesforce Deploys Agentforce Across US Army (AI-360)](https://www.ai-360.online/salesforce-deploys-agentforce-across-us-army/)

---

## Audio script
วันอังคารที่ห้าสิงหา. Salesforce ประกาศว่า Missionforce National Security ได้ Impact Level Five authorization จาก Department of War. เป็น AI agent commercial platform ตัวแรกที่ได้ clearance ระดับนี้ในตลาด federal defense. U.S. Army Human Resources Command เป็นลูกค้าแรก. deploy Agentforce สาม-หก-ศูนย์ รับห้าสิบห้าล้านคอนเวอร์เซชั่นต่อเดือน. ประหยัดหกล้านเหรียญต่อปี. บริการเก้าจุดสองล้านคนตลอดยี่สิบสี่ชั่วโมง. รวม soldier active, veteran, civilian staff และครอบครัว. ตามหลังสัญญาห้าจุดหกพันล้านที่ Salesforce เซ็นเมื่อมกรา. เจ็ดเดือนจาก contract signing ถึง production deployment. Velocity ที่ตลาด government IT ไม่เคยเห็นในทศวรรษ. Agent ตอบหกสิบแปดเปอร์เซ็นต์ของ inquiry โดยไม่ต้อง escalate. Backlog จาก หนึ่งจุดสองล้าน case จะลดเหลือต่ำกว่าสามเดือนภายใน Q4. IL5 authorization นี้เปลี่ยน landscape. Anthropic Claude Gov กับ OpenAI ChatGPT Gov ที่ launch ต้นปี ยังอยู่ FedRAMP High moderate ไม่ถึง IL5. ต้องเร่ง authorization ภายในหกสิบวันหรือเสียตลาดที่ Salesforce ล็อคก่อน. สำหรับ Enabridge — playbook นี้ replicate ไปที่ Thai institution ขนาดใหญ่ได้ทันที. มหาดไทย, สรรพากร, สปสช., retail bank. ตัวเลขต่อ population Thai ประมาณห้าถึงสิบล้านคอนเวอร์เซชั่นต่อเดือน. ประหยัดสามสิบถึงห้าสิบล้านบาทต่อปี. เราต้องเตรียม whitepaper Government-Grade Agentic AI for Thai Public Sector ภายในสามสิบวัน. เมื่อ Salesforce ประกาศ Thailand deployment ใน Q4 หรือ Q1 หน้า จะได้ position เป็น trusted integrator แทนที่จะแข่ง toe-to-toe. Missionforce คือจุดเปลี่ยนที่ agentic AI จาก cool tech in slide deck เป็น line item ใน government budget.
