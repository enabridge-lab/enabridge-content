---
date: 2026-09-17
slug: 26-09-17-0609-02-salesforce-nvidia-koa-crm-reasoning-model
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  Editorial isometric illustration of a large glowing brain-shaped chip
  labeled "KOA" sitting inside a transparent fortress marked "SALESFORCE
  TRUST BOUNDARY". Around it, ribbons of data flowing in labeled
  "27 YEARS CRM DATA" and "NEMOTRON 3 SUPER". Bright badges floating:
  "3X FEWER ERRORS", "14 INDUSTRIES", "WINTER GA". Deep navy background,
  bright green and orange accents, editorial magazine style, 1:1 aspect,
  numbers large and high contrast for 200px thumbnail, no real human faces.
image: images/26-09-17-0609-02-salesforce-nvidia-koa-crm-reasoning-model.png
---

# Salesforce + NVIDIA เปิด Koa — CRM reasoning model ที่ต่อ Nemotron ด้วย 27 ปีของข้อมูล CRM

## TL;DR
- 15 ก.ย. ที่ Dreamforce — Salesforce เปิด **Koa** reasoning model ตัวแรกที่บริษัทสร้างเอง โดย post-train NVIDIA Nemotron 3 Super (120B open-weight) บนข้อมูล synthetic ที่จำลองจาก 27 ปีของ CRM deployment ครอบคลุม 14 อุตสาหกรรม
- **ผลตอบ:** เท่าหรือดีกว่า frontier model ใน CRM action + **3x fewer errors** (Salesforce CRM Benchmark), เข้า pilot กับ Formula 1, Xero, Baxter Credit Union, UChicago Medicine, 1-800Accountant, Engine — GA ฤดูหนาวปีนี้ในสหรัฐฯ
- Salesforce ควบคุม weights + train + inference ในโครงสร้างพื้นฐานตัวเอง — **prompt/data ไม่ไปแตะ Anthropic/OpenAI/Google** — เป็นบทเรียนใหม่ของ "vertical AI moat = proprietary data + own weights + trust boundary"

## เกิดอะไรขึ้น

ในขณะที่ Benioff โฆษณา AIforce เรื่อง interface layer วันเดียวกัน Salesforce ปล่อยเซอร์ไพรส์ตัวที่สอง: **Koa** ซึ่งเป็น reasoning model ตัวแรกที่ Salesforce สร้างเอง — post-train จาก NVIDIA Nemotron 3 Super base (120B parameter open-weight model) บน **corpus สังเคราะห์จากประสบการณ์การ deploy CRM 27 ปี ครอบคลุมกว่า 14 อุตสาหกรรม**. ในเมื่อ Salesforce มีข้อมูล telemetry จาก 150,000+ customer และเคสจริงตั้งแต่ 1999 ถึงวันนี้ Koa คือความพยายามเปลี่ยน dataset ที่ frontier lab ไม่มีให้กลายเป็น model advantage

Jensen Huang ขึ้นเวทีคู่กับ Benioff โพลอยา "Now we can know everything and do anything" — คำพูดที่ฟังเหมือน hype แต่มีสารสำคัญคือ NVIDIA เดินเกม "โมเดล open-weight base + partner ที่มี proprietary data" ต่างจากเกม hyperscaler ปกติ (คือ Azure OpenAI, AWS Anthropic ที่ขาย frontier LLM สำเร็จรูป). Koa รันเต็มตัวใน **Salesforce trust boundary** — SF ควบคุม weight, post-training pipeline, และ inference เอง ไม่ส่ง prompt ออก third-party lab เลย. นี่เป็นครั้งแรกที่ SaaS vendor ขนาด Salesforce แสดงตัวเป็น model developer ไม่ใช่แค่ model consumer

Performance ที่ SF อ้าง: Koa เท่าหรือดีกว่า "leading models" ใน CRM action พร้อม **3x fewer errors** อ้างอิงจาก benchmark ภายในของ Salesforce เอง (CRM Benchmark). Pilot customer ที่เปิดชื่อ: Formula 1, Xero, Baxter Credit Union, UChicago Medicine, 1-800Accountant, Engine — ครอบคลุมทั้ง sports/entertainment, finance, healthcare, accounting SaaS. Salesforce เองใช้ Koa อยู่ภายในแล้วเป็น Slack agent ให้พนักงาน. GA คาดฤดูหนาวปีนี้ในภูมิภาคสหรัฐฯ ก่อน

## ทำไมสำคัญ

Koa คือ proof point ของสมมติฐานที่วงการ enterprise AI พูดกันมา 2 ปี: **"proprietary domain data + own weights"** จะเป็น moat ที่ frontier lab ทั่วไปทำแทนไม่ได้. Salesforce มีข้อมูลจริงจาก CRM deployment ในทุก vertical ที่ OpenAI/Anthropic ไม่มี — pipeline stage transitions, discount approval flows, escalation patterns, quota-attainment shapes ในแต่ละ industry — เอามาสร้าง synthetic training data ที่ frontier lab ไม่มีทางหาได้. ถ้าข้อมูลนี้ทำให้ Koa error rate ต่ำจริง 3x ในงาน CRM action เฉพาะทาง frontier lab จะไม่ปิด gap นี้ได้ด้วย compute เพียงอย่างเดียว

Pattern ที่จะตามมา: ทุก SaaS vendor ขนาดใหญ่ที่มี proprietary corpus จะต้องเลือกว่าจะเป็น **model developer** (Salesforce, ServiceNow, Workday, Adobe — น่าจะทำเอง) หรือ **model consumer** (HubSpot, Zendesk, Freshworks — น่าจะเช่าใช้). Nemotron 3 Super เป็น base ที่ NVIDIA ตั้งใจให้คนเอาไป post-train เอง จะกลายเป็น **"Linux ของ vertical AI"** — โมเดล open-weight ที่ทุก SaaS vendor เอาไปสร้าง reasoning model เฉพาะ vertical. ในเมืองไทย SCB TechX / KBTG / SET ที่มี transaction data 15+ ปีก็เข้าเกมนี้ได้ถ้าเลือก base ที่ถูกและมีทีม post-training ที่พร้อม

จุดที่ frontier lab (Anthropic, OpenAI) ต้องระวังคือ: enterprise customer จะเริ่มเห็นว่า **"frontier + vertical fine-tune ของ vendor เดียวกับ workflow เดิม"** อาจแซง "frontier ล้วน" ในงานเฉพาะทาง. ถ้า Koa proof out ที่ 3x error reduction จริง GTM ของ Claude/GPT ใน enterprise CRM จะยากขึ้น เพราะ customer จะถามว่า "ทำไมฉันต้องซื้อ frontier ของคุณ ทั้งๆ ที่ Salesforce มีของที่แม่นกว่าใน domain นี้?"

## มุม AI Agent Platform

**Builders** — startup ที่สร้าง vertical AI agent (sales, service, CRM automation) ต้องคิดใหม่ว่า own model / เช่าใช้ frontier — Koa เปิด playbook ที่ทำได้จริงถ้ามี domain data ที่คู่แข่งเข้าไม่ถึง; ถ้าไม่มี ก็ต้องคิดว่าจะ integrate เข้ากับ Koa ยังไง (เช่นเป็น skill/plugin ใน AgentExchange). **Users / business** — enterprise ที่ deploy Agentforce อยู่แล้วในสหรัฐฯ ควรลงทะเบียน pilot Koa เพื่อวัด error rate จริงในงานของตัวเอง; enterprise ไทยที่ยังไม่มี Agentforce ควรให้ทีม data ไปคิด playbook ว่าถ้ามี proprietary corpus (transaction, ticket, contract) จะใช้ Nemotron 3 Super base post-train เองได้ไหม — cost เข้าถึงได้ระดับ mid-market แล้ว. **Ecosystem** — NVIDIA ได้ enterprise SaaS ที่ผลักดัน Nemotron adoption; Anthropic/OpenAI ยังคุม frontier reasoning แต่ต้อง reposition ว่าจุดขายคือ general reasoning ไม่ใช่ vertical accuracy; startup post-training services (Together, Fireworks, Baseten) ได้ tailwind จากทุก SaaS vendor ที่จะเดินตาม Salesforce ในอีก 12 เดือน

## Sources
- [Salesforce's First CRM Reasoning Model 'Koa' Is Revealed at Dreamforce '26 — Salesforce Ben](https://www.salesforceben.com/salesforces-first-crm-reasoning-model-koa-is-revealed-at-dreamforce-26/)
- [Salesforce teams up with Nvidia to launch Koa, a dedicated CRM reasoning model — IT Pro](https://www.itpro.com/technology/artificial-intelligence/salesforce-teams-up-with-nvidia-to-launch-koa-a-dedicated-crm-reasoning-model)
- ['Now We Can Know Everything and Do Anything,' Jensen Huang Says at Dreamforce — NVIDIA Blog](https://blogs.nvidia.com/blog/jensen-huang-dreamforce/)

---

## Audio script
วันเดียวกันกับที่ Salesforce เปิด AIforce เขายังปล่อย Koa ด้วยครับ. Koa คือ reasoning model ตัวแรกที่ Salesforce สร้างเอง ต่อยอดจาก NVIDIA Nemotron 3 Super ขนาด 120 พันล้านพารามิเตอร์. จุดขายคือมัน post-train บนข้อมูลสังเคราะห์ที่จำลองมาจาก 27 ปีของการ deploy CRM ครอบคลุม 14 อุตสาหกรรม — pipeline การ approve ส่วนลด, ขั้นตอน escalation, pattern การปิดดีล — ข้อมูลพวกนี้ frontier lab อย่าง OpenAI หรือ Anthropic ไม่มี. Salesforce บอกว่า Koa error rate ต่ำกว่า leading model 3 เท่าในงาน CRM. Jensen Huang ขึ้นเวทีคู่กับ Benioff. Pilot มี Formula 1, Xero, Baxter Credit Union, UChicago Medicine. GA ฤดูหนาวปีนี้ในสหรัฐฯ. ประเด็นใหญ่คือ Salesforce ควบคุม weight ทั้งหมดใน trust boundary ของตัวเอง — prompt ไม่วิ่งออกไป third-party lab. Pattern ที่จะเกิดตามคือ SaaS vendor ที่มีข้อมูล proprietary ทุกเจ้าจะต้องเลือกว่าจะสร้างโมเดล vertical เองหรือเช่าใช้. Nemotron 3 Super เตรียมกลายเป็น Linux ของ vertical AI. ทีมไทยที่มี transaction data สิบห้าปีขึ้นไปควรลอง playbook นี้ครับ.
