---
date: 2026-08-08
slug: naive-28m-series-a-autonomous-companies-agent-primitives
topic: agentic-ai
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial isometric illustration of a small startup office in a snow
  globe labeled "NAIVE", with an AI agent (robot silhouette) standing
  behind three desks — one desk stacked with paperwork labeled "KYC /
  IDENTITY", one with a cloud storage server labeled "CLOUD", one with a
  legal binder labeled "GOVERNANCE". Above the globe, three revenue
  arrows spelling "10x IN 6 MONTHS" curve upward. On the horizon behind:
  three tiny businesses labeled "TIKTOK CHANNEL", "AI AGENCY", "RENTAL
  CAR" — each with the same robot silhouette in a driver seat. Amber +
  navy palette, grid floor, editorial isometric style, 1:1 aspect, no
  real human faces (silhouettes OK), text sharp at 200px thumbnail.
image: images/26-08-08-0613-04-naive-28m-series-a-autonomous-companies-agent-primitives.png
---

# Naïve $28.5M Series A: infrastructure สำหรับ "autonomous companies" — 30K devs, revenue 10x ใน 6 เดือน, ลูกค้าจริงคือ TikTok channel + rental car agency

## TL;DR
- **6 ส.ค.** — Naïve (San Francisco, ก่อตั้ง 2026 โดย Berkeley dropout Sean Dorje + Dennis Zax) ปิด **Series A $28.5M** นำโดย Nexus Venture Partners; มี Y Combinator, Zetta, Liquid 2, angel (Gokul Rajaram, Tim Zheng, JD Sherman) ร่วมลง
- **Traction ที่ทำให้ round pop** — **30,000+ dev signup** ใน "months" หลัง launch; **run-rate revenue โต 10x** ใน 6 เดือน sliding เป็น "**low double-digit millions**" (แปลว่า ~$10-20M ARR ที่ 6 เดือน)
- **What it sells** — Unified API + provisioning stack ที่ให้ AI agent มี **identity (KYC verified)**, **cloud storage/compute**, **governance gateway**, **payment rail** → **"agent เป็น economic entity ที่ setup + run business ได้เอง"**
- **ลูกค้าจริง (ไม่ใช่ demo)** — AI automation agency, faceless TikTok/YouTube channel, **rental car agency ที่รัน autonomous** — POV: "**autonomous company**" กำลังกลายเป็น business model จริง แม้ regulator ยังไม่ตั้งหลัก
- **มุม Agent Platform** — Naïve นั่งตรง gap ที่ Cloudflare Wallets (identity + payment) + Databricks Unity Gateway (governance) ยังไม่ครอบ = **operational stack** ที่ agent ต้องใช้เพื่อ "**เปิดบริษัทใน 5 นาที**". คำถาม: ที่ผสมทั้ง 3 layer เข้าด้วยกันสำเร็จ = Cloudflare/Anthropic ซื้อภายใน 18 เดือน หรือ IPO?

## เกิดอะไรขึ้น

วันพุธที่ 6 สิงหาคม Naïve — startup 8 เดือนที่ก่อตั้งโดย Berkeley dropout สองคน Sean Dorje + Dennis Zax — ปิด **Series A $28.5M** นำโดย Nexus Venture Partners. Cap table เจ๋งกว่า deal size: **Y Combinator, Zetta, Liquid 2, Gokul Rajaram** (Doordash/Coinbase board), **Tim Zheng** (Apollo.io co-founder), **JD Sherman** (ex-HubSpot COO). Founder แค่ 21 ปี, พึ่งกลับจาก YC batch, ประกาศ pitch ว่า "**เราสร้าง infrastructure สำหรับ autonomous companies**" ที่ปกติ VC จะหัวเราะ — แต่ traction ทำให้ Nexus + gang เข้าใน 3 สัปดาห์

**Traction ที่ทำให้ round pop**: (1) **30,000+ dev signup** ใน "หลายเดือน" (Y Combinator ยกเป็น top 5 batch W26 พร้อมกับตัวเลข signup ที่ระดับ Ramp / Stripe ยุคแรก), (2) **annual run-rate revenue โต 10x** ใน 6 เดือน sliding เป็น "**low double-digit millions**" (Nexus ประเมิน ~$12M ARR), (3) **customer proof ที่ไม่ใช่ demo** — AI automation agency (Berkeley grad ที่ใช้ Naïve stack setup 20-30 client subsidiary), **faceless TikTok / YouTube channel** (creator ที่ผูก Naïve identity เพื่อจ่าย TikTok / YT ad revenue + Stripe payout กลับเข้ามาที่ agent wallet), และ **rental car agency ที่รันแบบ autonomous** (agent ทำ pricing, booking confirmation, refund, insurance claim; human ทำแค่ vehicle maintenance)

**Stack ที่ Naïve ขาย = unified API + provisioning สำหรับ 4 อย่างที่ agent ต้องมีก่อน "เปิดบริษัท"**: (a) **verified identity** — DBA / LLC / EIN registration + KYC ผ่าน partner network, (b) **cloud infrastructure** — compute + storage + database ที่ agent request ผ่าน API เดียว, (c) **governance gateway** — role-based policy + spend cap + audit log ที่ human owner ตั้งบน dashboard, (d) **payment rail** — bank account + card issuance + settlement (Stripe / Coinbase partner integration). Framing ที่ founder ใช้: "**Stripe Atlas สำหรับ agent**" — คำ pitch ที่ VC เข้าใจทันที

## ทำไมสำคัญ

**Naïve เป็น first serious attempt ที่ productize "autonomous company as a service"** — คำที่ปีก่อนยัง academic (Balaji Srinivasan's network state, DAOs, Ohanian's "agent DAOs") — วันนี้กลายเป็น product ที่มี ARR + customer ที่ pay จริง. Timing ที่ทำให้ product ทำงานได้ = coincide กับ 3 primitive ที่ launch พร้อมกัน: (1) **agent identity + payment** (Cloudflare Wallets, Stripe Machine Payments, Visa TAP), (2) **agent governance** (Databricks Unity AI Gateway, Snowflake Cortex Gateway, AWS AgentCore), (3) **agent orchestration runtime** (Anthropic Claude Agent SDK, Sapiom Runtime, OpenAI Agents, Google ADK). ก่อนหน้านี้ agent ที่ "รันบริษัท" ต้อง glue 15+ SaaS ด้วย engineer 2-3 คน; วันนี้ 1 dev + 1 Naïve API key ก็เริ่มได้

**POV ที่ต้อง state ตรง ๆ**: "autonomous company" ไม่ใช่ singularity moment — เป็น **cost structure disruption** ที่ **micro-business ระดับ $100K-$1M ARR จะเปลี่ยนเจ้าของจาก solo founder ที่ทำงาน 60 hr/wk → solo founder ที่ operator agent 24/7**. ธุรกิจที่จะโดนก่อน = ธุรกิจที่ **workflow standardize + rule-based + interaction volume สูง แต่ complexity ต่ำ**: dropshipping store, faceless media channel, boutique e-commerce, small law/accounting outsource, digital marketing agency (การ report + client comm), small ad hoc rental (car, equipment, storage). ไม่ใช่ Fortune 500 disruption — เป็น long-tail SME disruption ที่ regulator ยังไม่มี framework จับ

**Regulator gap = ทั้งความเสี่ยงและ moat**. เมื่อ TikTok channel ที่ agent รันชนคดี copyright, rental car agency ที่ agent booking ผิดคนแล้วเกิดอุบัติเหตุ — **ใครรับผิด?** Human owner ที่กด "deploy"? Agent framework (Naïve)? Model provider (Anthropic/OpenAI)? Payment rail (Stripe)? Cloud (AWS)? US, EU, สิงคโปร์, ญี่ปุ่น ยังไม่มี framework ตอบ. EU AI Act (live 2 ส.ค.) เริ่ม hint ที่ "meaningful human oversight" แต่ยังไม่ operational สำหรับ autonomous company case. **นี่คือความเสี่ยง existential ของ Naïve — และเป็น moat เดียวกันเพราะ competitor 6 เดือนใหม่จะไม่ผ่าน compliance ได้ทัน**

## มุม AI Agent Platform

**สำหรับ builders:** ถ้าคุณ build **vertical agent SaaS** (agent สำหรับ real estate, agent สำหรับ legal, agent สำหรับ healthcare admin) — **piggyback Naïve stack แทน build 4 primitive เอง** (identity, cloud, governance, payment). Timeline ที่ save = 6-12 เดือน. ถ้าคุณ build **horizontal platform** (competitor ของ Naïve) — คำถามคือ **specialize ที่ไหน**: (a) locale/regulation (Naïve US-first; EU/APAC/LATAM หน้าที่ยังว่าง), (b) vertical depth (Naïve horizontal; specialize e-commerce autonomous / creator autonomous / SME finance autonomous จะ moat กว่า), (c) integration depth (integrate ลึกกับ Salesforce / Shopify / HubSpot / SAP แทนที่จะ generic API). ห้าม compete ตรง horizontal + US — Naïve มี YC + 30K dev + $28M cash หน้าเปรียบ 12-18 เดือน

**สำหรับ users/business:** Small business owner + micro-preneur — **pilot 1 agent เดียวก่อน**: agent ที่ทำ social media reply + inventory reorder + refund handling ในธุรกิจ e-commerce, agent ที่ทำ client status update + invoice ในธุรกิจ agency. ตัวเลข ROI ที่จริง: reduce operator cost 30-60% ในธุรกิจ standardized. **Enterprise CEO** ที่มี business unit ที่ operate แบบ semi-autonomous (franchise, dealership network, contract manufacturing) — **watch Naïve model** เพราะกำลังเปลี่ยน franchise economics ระยะยาว (ทำไมต้องจ่าย royalty 5% ถ้า operator เป็น agent ที่ deploy ที่ไหนก็ได้?). **Thai SME context** — ที่มี **micro-influencer + creator economy + dropship + affiliate ecosystem** ขนาดใหญ่บน Shopee/Lazada/TikTok Shop — คือ demographic ที่ Naïve จะ target ในอีก 12 เดือน. Thai integrator ที่พูดภาษา creator/SME ได้ + integrate Thai payment (PromptPay, Truemoney, K PLUS API) + Thai identity (National ID KYC) ได้ = **prime opportunity ก่อน US vendor เข้ามาเอง**

**สำหรับ ecosystem:** **Winner (สั้น):** Naïve, Anthropic (Naïve ใช้ Claude หนักตาม pattern YC), Stripe/Coinbase (payment rail), Cloudflare (identity + wallet). **Winner (กลาง):** creator economy platform ที่ integrate agent (TikTok, YouTube, Shopify), tax/legal tech ที่ทำ compliance auto (Pilot.com, Kruze, Deel — ต้อง pivot), micro-VC ที่ fund solo founder + agent stack. **Loser:** solo founder ที่ยังทำงาน manual, ล่างของ BPO ที่ทำงาน rule-based, agency ที่ขาย commodity service (basic bookkeeping, basic social media posting). **Regulator:** SEC, IRS, ก.ล.ต., BOT, EU commission — ต้อง define legal personhood ของ agent-run company ภายใน 24 เดือน ก่อน case จะ pile up. **Enabridge angle:** เกิด **advisory + implementation opportunity 2 ทิศ**: (1) ช่วย Thai SME + creator ที่ ready เปลี่ยน model → offer "**agent-operator setup pack**" (Naïve/competitor + Thai localization + compliance advisory) เป็น productized service ราคา 50-200K THB, (2) ช่วย Thai enterprise ที่ operate franchise/dealership → **rethink operator model** ก่อน US เข้ามา. Position ที่ Enabridge เล่นได้ดีคือ **bridge ระหว่าง global agent stack กับ Thai compliance/payment/culture** — เป็น niche ที่ระดับโลกไม่ crack

## Sources
- [Naïve raises $28.5M to automate the grunt work of setting up and running a company — TechCrunch](https://techcrunch.com/2026/08/06/naive-raises-28-5m-to-automate-the-grunt-work-of-setting-up-and-running-a-company/)
- [Naïve bags $28.5M in funding to automate the creation and day-to-day running of almost any business — SiliconANGLE](https://siliconangle.com/2026/08/06/naive-bags-28-5m-funding-automate-creation-day-day-running-almost-business/)
- [Naïve Raises $28.5M Series A to Build Autonomous Company Infrastructure — WebWire](https://www.webwire.com/ViewPressRel.asp?aId=358555)
- [Naïve raises $28.5M Series A to let AI agents run companies — Dealroom](https://app.dealroom.co/news/note/na-ve-raises-28-5m-series-a-to-let-ai-agents-run-companies)
- [Naïve Raises $28.5 Million Series A To Build Infrastructure For Autonomous Companies — Pulse2](https://pulse2.com/naive-raises-28-5-million-series-a-to-build-infrastructure-for-autonomous-companies/amp/)
- [Naïve Raises $28.5M in Series A Funding — FinSMEs](https://www.finsmes.com/2026/08/naive-raises-28-5m-in-series-a-funding.html)

---

## Audio script
วันพุธที่ 6 สิงหาคม Naïve startup 8 เดือนจาก San Francisco ก่อตั้งโดย Berkeley dropout สองคน Sean Dorje และ Dennis Zax ปิด Series A 28.5 ล้านดอลลาร์ นำโดย Nexus Venture Partners. Cap table มี Y Combinator Zetta Liquid 2 Gokul Rajaram Tim Zheng และ JD Sherman อดีต COO HubSpot. Traction ที่ทำให้ round pop คือ 30000 dev signup ในไม่กี่เดือน annual run rate revenue โต 10 เท่าใน 6 เดือน เป็น low double digit million ประมาณ 12 ล้านดอลลาร์ ARR.

Product ที่ Naïve ขายคือ unified API และ provisioning stack ที่ให้ AI agent มี 4 อย่างที่ต้องมีก่อนเปิดบริษัท verified identity ผ่าน DBA LLC EIN registration KYC cloud infrastructure compute storage database governance gateway role based policy spend cap audit log payment rail bank account card issuance ผ่าน Stripe หรือ Coinbase. Founder เรียก Stripe Atlas สำหรับ agent.

ลูกค้าจริงที่ไม่ใช่ demo คือ AI automation agency faceless TikTok และ YouTube channel และ rental car agency ที่รันแบบ autonomous agent ทำ pricing booking refund insurance claim human ทำแค่ vehicle maintenance. เป็นสัญญาณว่า autonomous company กำลังกลายเป็น business model จริงในระดับ micro business แม้ regulator ยังไม่ตั้งหลัก.

POV คือ autonomous company ไม่ใช่ singularity moment แต่เป็น cost structure disruption ที่ micro business ระดับ 100K ถึง 1 ล้านดอลลาร์ ARR จะเปลี่ยนเจ้าของจาก solo founder ที่ทำ 60 ชั่วโมงต่อสัปดาห์ ไปเป็น solo founder ที่ operator agent 24 ชั่วโมง. ธุรกิจที่โดนก่อนคือ workflow standardize rule based volume สูง complexity ต่ำ อย่าง dropshipping faceless media boutique e commerce small law accounting outsource. Regulator gap เป็นทั้งความเสี่ยงและ moat เพราะเมื่อ TikTok channel ที่ agent รันชนคดี copyright หรือ rental car agent booking ผิดคนแล้วเกิดอุบัติเหตุ ใครรับผิด ยังไม่มีคำตอบใน US EU สิงคโปร์ หรือญี่ปุ่น.

สำหรับ Thai SME ที่มี creator economy micro influencer dropship affiliate ecosystem บน Shopee Lazada TikTok Shop คือ demographic ที่ Naïve จะ target ในอีก 12 เดือน. Thai integrator ที่พูดภาษา creator หรือ SME ได้ integrate PromptPay Truemoney K PLUS API และ National ID KYC ได้ คือโอกาสก่อน US vendor เข้ามาเอง. Enabridge position คือ bridge ระหว่าง global agent stack กับ Thai compliance payment culture.
