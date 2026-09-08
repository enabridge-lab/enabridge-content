---
date: 2026-09-08
slug: enterprise-saas-agent-tollbooth-sap-servicenow
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial isometric illustration of three highway tollbooths side by
  side, each with a large sign: the first labeled "SAP · BLOCKED" with a
  crossed-out gate, the second labeled "SERVICENOW · METER" with a
  running counter reading "ASSISTS: 4,821", the third labeled
  "SALESFORCE · HEADLESS" with an open gate. A line of small robot agents
  queues in front of each booth. Muted navy, amber, red palette on a
  soft gradient ground, dramatic rim lighting, large high-contrast text
  readable at 200px thumbnail, 1:1 aspect, no real human faces.
image: images/26-09-08-0610-04-enterprise-saas-agent-tollbooth-sap-servicenow.png
---

# SAP block, ServiceNow meter, Salesforce headless — enterprise SaaS ทั้งสามเจ้าตั้ง "agent tollbooth" ต่างสาย, กำลังรีดีไซน์ pricing model ของ enterprise software ทั้งอุตสาหกรรม

## TL;DR
- **SAP** — API Policy v4/2026 **prohibit AI systems ที่ schedule/execute call แบบ independent** — external agent ไม่ได้ใช้ SAP API แล้ว, ทุกอย่างต้องผ่าน Joule agent ของ SAP เอง
- **ServiceNow** — เปิด **Action Fabric** ที่ Knowledge 2026 — external agent ต้องผ่าน integration layer นี้; meter การใช้งานเป็น **"assists"**, ลูกค้าจ่าย top-up ถ้าเกิน subscription
- **Salesforce** — **headless** — agent ไหนก็เข้าถึงได้ผ่าน API แต่ทุก transaction ผ่าน Data Cloud + Agentforce runtime; positioning เหมือน Salesforce เป็น execution layer, ลูกค้าเลือก AI เอง
- **Forrester** warning: "SAP approach = pricing cliff" — CIO ระวัง single vendor เป็น gatekeeper enterprise AI
- Signal ใหญ่: **agent-metered pricing** กำลังกลายเป็น business model ใหม่ของ SaaS — เทียบเท่า database ที่เคย meter storage/compute

## เกิดอะไรขึ้น

หลัง Knowledge 2026 (พ.ค.) + SAP API Policy v4 (มิ.ย.) + Dreamforce prep รอบล่าสุด, สัปดาห์นี้ **PYMNTS, Techzine, UC Today** ปล่อยบทวิเคราะห์ concurrent ว่า **enterprise SaaS ทั้งสามเจ้ามี strategy ต่อ agent ต่างกันสิ้นเชิง** — และเป็น pricing revolution ที่ CIO ต้องเลือกฝ่ายภายในปีนี้

**SAP: block**. SAP API Policy v4/2026 explicit prohibit **"AI systems ที่ independently schedule หรือ execute calls"** ต่อ SAP endpoint. แปลว่า Anthropic Claude, ChatGPT, Gemini, Perplexity, custom LangChain agent — ไม่ได้ต่อ SAP โดยตรง. ทุก request จาก AI agent ต้องผ่าน **Joule** ซึ่งเป็น native SAP agent. Positioning: SAP ตั้งเป็น **walled garden ของ enterprise data + workflow** — Forrester เรียก architecture นี้ว่า **"pricing cliff"** เตือน CIO ระวัง

**ServiceNow: meter**. ที่ Knowledge 2026, ServiceNow เปิด **Action Fabric** — integration layer ที่ external agent **ต้องผ่านก่อน** เข้าถึง data + execute workflow ใน ServiceNow. Metered ในหน่วย **"assists"**; subscription base ให้ assist quota, เกินแล้ว pay-per-assist. ServiceNow shift business model จาก "seat license" → "transaction meter" — คล้าย Twilio/Stripe billing style. ลูกค้า Fortune 500 ที่มี 20-30 agent internal ทำงานพร้อมกัน จะเห็น bill โต 3-5x ภายในปี

**Salesforce: headless**. Salesforce ประกาศ agent ไหนก็เข้าถึง Salesforce ได้ผ่าน API — แต่ทุก transaction ผ่าน **Data Cloud + Agentforce runtime** ซึ่งเป็น pricing anchor ของ Salesforce เอง. Positioning ชัด: Salesforce เป็น execution layer, ลูกค้าเลือก AI ที่ต้องการ (Claude/ChatGPT/Gemini/Copilot) แต่ transaction ยังนับเข้า Data Cloud consumption + Agentforce action. Forrester อ่านว่านี่คือ **"pay-to-play headless" — เปิดเข้าง่าย แต่จ่ายทาง economics layer**

Bench mark ที่ McKinsey State of AI 2026 ปล่อย: **enterprise ที่ scale agent อย่างน้อยหนึ่ง function โต 27% → 40% ในหกเดือน** — แต่ SME ยังนิ่งที่ 22%. ตัวเลขนี้อธิบายทำไม 3 เจ้าตั้งใจ pivot pricing model ตอนนี้ — **agent adoption ระเบิดใน Fortune 500 ก่อน SME** และ SaaS vendor ไม่อยากพลาด monetization window

## ทำไมสำคัญ

**Pricing revolution ที่ค่อย ๆ เห็น**: enterprise software 20 ปีที่แล้ว = "per-seat license". ปี 2015-2020 = "consumption metered (storage/compute)". ตอนนี้ปี 2026 = **"agent-action metered"** — จำนวน action ที่ agent execute ผ่าน platform. ServiceNow นำก่อน, Salesforce ตาม, Workday จะ mirror เร็ว ๆ นี้ (มี report แล้ว), **Oracle Fusion + Microsoft Dynamics** จะประกาศภายใน Q4

**Bet ที่สำคัญ**: SAP walled garden **ไม่ยั่งยืน**. Enterprise ที่ต่อ Anthropic Claude Enterprise + ChatGPT Enterprise + Gemini พร้อมกันจะเจอ friction ที่ **"agent เข้าถึง Salesforce/ServiceNow ได้ แต่ SAP ไม่ได้"** — และเลือกทาง (1) ย้าย workload ออกจาก SAP (ช้า แพง), (2) push SAP ให้เปิด (มี legal + procurement leverage), (3) **ใช้ RPA/human-in-the-loop เป็น bridge** (ระยะสั้น). Bet ผม: ภายใน 6 เดือน SAP จะ soften — น่าจะเปิด "certified partner agent" scheme (คล้าย ISV OSS certification), หลังเจอ pushback จาก DACH banking ลูกค้าใหญ่

**เปิดช่องให้ layer ใหม่**: **"agent-side observability + cost attribution"** — ลูกค้าต้องรู้ว่า agent A vs B ใช้ ServiceNow assist กี่ครั้ง, ทำ Data Cloud query กี่ dollar, ยิง SAP call ผ่าน RPA กี่ transaction. Databricks Unity AI Gateway เข้ามาช่วยได้ 60% แต่ครอบไม่หมด — startup ใหม่ที่ทำ "FinOps for agents" จะโตเร็วในปีหน้า

## มุม AI Agent Platform

**Builders**: ถ้าคุณสร้าง agent framework หรือ vertical agent, สัปดาห์นี้เป็น signal ให้ **build cost model per platform** เข้า agent SDK — เมื่อ agent จะยิง ServiceNow ให้เตือน user ว่า "จะเสีย 1 assist"; เมื่อจะยิง Salesforce ให้แสดง Data Cloud query estimate; เมื่อจะยิง SAP ให้ fall back ผ่าน Joule หรือ RPA. FinOps observability = feature ที่ enterprise buyer เริ่มถามใน RFP

**Users / business**: enterprise CIO ต้อง review contract renewal ของ SAP/ServiceNow/Salesforce ในมุม agent — negotiate assist cap + Data Cloud consumption tier + SAP alternative access. ที่ปฏิบัติได้ทันที: audit agent traffic ที่ยิงเข้า core system 30 วัน, project cost 12 เดือน; ถ้าเห็น cost spike ให้ deploy caching layer (Databricks Unity หรือ Cloudflare AI Gateway) หน้า core system

**Ecosystem**: **"agent-friendly" กำลังกลายเป็น differentiator ของ SaaS** — startup ที่ launch ปี 2026-2027 จะ pitch "we don't meter agents" เป็น competitive advantage ต่อ ServiceNow/Salesforce. เห็นแล้วใน HR tech (Rippling), spend management (Ramp), sales enablement (Common Room) — ทุกเจ้าประกาศ **"unlimited agent access included"** เป็นจุดขายต่อ Workday/SAP SuccessFactors. B2B integration platform (Enabridge, Zapier, Make) มี opening ใหญ่ในการเป็น **"agent-metering shield"** สำหรับ SME ที่ไม่มี procurement leverage

## Sources
- [PYMNTS — ServiceNow, SAP and Workday Make AI Agents Pay to Play](https://www.pymnts.com/news/artificial-intelligence/2026/servicenow-sap-and-workday-make-ai-agents-pay-to-play/)
- [Techzine — SAP blocks external AI agents. Salesforce and ServiceNow don't.](https://www.techzine.eu/blogs/applications/141323/sap-blocks-external-ai-agents-salesforce-and-servicenow-dont/)
- [UC Today — Enterprise Software Giants Are Changing the Rules on AI Agent Access](https://www.uctoday.com/productivity-automation/enterprise-software-giants-are-changing-the-rules-on-ai-agent-access/)
- [GSPANN — Enterprise AI Interoperability: Agentic AI Tollbooth](https://www.gspann.com/insights/blog/a-new-tollbooth-on-enterprise-ai-interoperability)
- [ServiceNow Newsroom — Knowledge 2026 Announcements](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-expands-AI-Control-Tower-to-discover-observe-govern-secure-and-measure-AI-deployed-across-any-system-in-the-enterprise/default.aspx)

---

## Audio script
สัปดาห์นี้ PYMNTS Techzine UC Today ปล่อยบทวิเคราะห์ concurrent. enterprise SaaS สาม เจ้า มี strategy ต่อ agent ต่างกันสิ้นเชิง. เป็น pricing revolution ที่ CIO ต้องเลือกฝ่ายภายในปีนี้.

SAP block. API Policy v4 2026 explicit prohibit AI systems ที่ independently schedule execute call. Claude ChatGPT Gemini custom LangChain agent ไม่ได้ต่อ SAP ตรง. ทุก request ต้องผ่าน Joule ซึ่งเป็น native SAP agent. Forrester เรียกว่า pricing cliff. เตือน CIO ระวัง.

ServiceNow meter. Action Fabric เปิดที่ Knowledge 2026. external agent ต้องผ่าน integration layer นี้ก่อน. metered เป็น assist. subscription base ให้ quota. เกินแล้ว pay per assist. shift จาก seat license ไป transaction meter. คล้าย Twilio Stripe. ลูกค้าที่มี ยี่สิบ ถึง สามสิบ agent internal จะเห็น bill โต สาม ถึง ห้า เท่าภายในปี.

Salesforce headless. agent ไหนก็เข้าถึง Salesforce ได้ผ่าน API. แต่ทุก transaction ผ่าน Data Cloud กับ Agentforce runtime ซึ่งเป็น pricing anchor ของ Salesforce. positioning ชัด. Salesforce เป็น execution layer. ลูกค้าเลือก AI ที่ต้องการ. transaction นับเข้า Data Cloud consumption กับ Agentforce action. pay to play headless.

McKinsey State of AI 2026. enterprise ที่ scale agent อย่างน้อยหนึ่ง function โต 27 เป็น 40 เปอร์เซ็นต์ในหกเดือน. SME ยังนิ่งที่ 22. อธิบายทำไม สาม เจ้าตั้งใจ pivot pricing ตอนนี้. adoption ระเบิดใน Fortune 500 ก่อน SME.

Pricing revolution ที่ค่อย ๆ เห็น. ยุค seat license. ยุค consumption metered. ยุคนี้ agent action metered. ServiceNow นำก่อน. Salesforce ตาม. Workday จะ mirror. Oracle Fusion กับ Microsoft Dynamics จะประกาศภายใน Q4.

Bet ที่สำคัญ. SAP walled garden ไม่ยั่งยืน. enterprise ที่ต่อ Claude Enterprise ChatGPT Enterprise Gemini พร้อมกันจะเจอ friction ว่า agent เข้าถึง Salesforce ServiceNow ได้ แต่ SAP ไม่ได้. ทางเลือกคือ ย้าย workload ออก. push SAP ให้เปิด. หรือใช้ RPA bridge. bet ผม. ภายใน หกเดือน SAP จะ soften. เปิด certified partner agent scheme หลังเจอ pushback DACH banking.

เปิดช่องให้ layer ใหม่. agent side observability กับ cost attribution. ลูกค้าต้องรู้ agent A vs B ใช้ ServiceNow assist กี่ครั้ง. Data Cloud query กี่ dollar. SAP call กี่ transaction. Databricks Unity ช่วยได้ หกสิบ เปอร์เซ็นต์. startup ที่ทำ FinOps for agents จะโตเร็วในปีหน้า.

สำหรับ builder. build cost model per platform เข้า agent SDK. เตือน user ว่าจะเสียเท่าไหร่แต่ละ call. FinOps observability กำลังจะเป็น feature ที่ enterprise ถามใน RFP.

startup ที่ launch ตอนนี้ pitch we don't meter agents เป็น competitive advantage ต่อ ServiceNow Salesforce. เห็นใน Rippling Ramp Common Room. ประกาศ unlimited agent access included ต่อ Workday SAP SuccessFactors. B2B integration platform อย่าง Enabridge Zapier Make มี opening ใหญ่ในการเป็น agent metering shield สำหรับ SME.
