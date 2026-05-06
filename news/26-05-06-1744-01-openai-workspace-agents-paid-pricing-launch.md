---
date: 2026-05-06
slug: openai-workspace-agents-paid-pricing-launch
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: A giant cream-colored ChatGPT speech bubble cracks open in the center of the frame, releasing a procession of small geometric agent icons that march across the canvas toward connected app silhouettes labeled "SLACK" "SALESFORCE" "NOTION" "DRIVE" in slate blue. A bold coral price tag dangles from the speech bubble showing "$20" in cream block letters, with a smaller "MAY 6" calendar badge in the upper-right corner in white. Editorial illustration, flat geometric shapes with subtle grain, cream + coral + slate blue palette on a deep navy background, dramatic side-lighting suggesting a curtain rising. No real human faces, no logos beyond the abstract app silhouettes. 1:1 aspect.
image:
---

# OpenAI พลิก Workspace Agents จากฟรี → คิดเครดิตวันนี้ — Codex-powered, ทะลุ Slack/Salesforce/Notion ตรง พ่วงเป็น "successor to custom GPTs"

## TL;DR
- **6 พ.ค. 2026** — OpenAI หยุดให้ Workspace Agents ใน ChatGPT Business/Enterprise/Edu/Teachers ใช้ฟรี เปลี่ยนเป็น **credit-based pricing** ตามตารางที่ประกาศไว้กลาง เม.ย. ของรอบ research preview
- **ChatGPT Business ราคา $20/user/month** ยังเดิม แต่ workspace agent กิน credit แยกต่อหน้าที่ — รัน scheduled task, รับงานใน Slack, ขอ approval ตามขั้นตอน, handoff ระหว่างคน
- เครื่องยนต์เป็น **Codex** + connector ฝัง: Slack, Google Drive, Microsoft 365, **Salesforce, Notion, Atlassian Rovo**; admin คุม IAM ต่อ user group/tool — อ่านเป็น "successor to custom GPTs" ที่ทำงานข้ามทีมจริง ๆ ไม่ใช่ wrapper prompt
- Signal: **OpenAI ปั๊ม enterprise revenue ให้ทันสัญญาใจกับนักลงทุน** — enterprise share โต 30% → 40%+ ของ revenue, $2B/เดือน, ต้องชน Microsoft Agent 365 ($15/seat) + Google Gemini Enterprise ที่บีบเข้ามาแล้ว

## เกิดอะไรขึ้น

วันนี้ 6 พฤษภาคม คือวันที่ OpenAI ขีดเส้นไว้ในประกาศ Workspace Agents ตั้งแต่ research preview — preview ใช้ฟรี **จนถึงวันนี้เท่านั้น**, จากนี้เป็น credit-based pricing ลูกค้า ChatGPT Business, Enterprise, Edu, Teachers ที่ต้องการให้ agent ทำงานต่อจะเริ่มถูกหักเครดิตตาม run-time + tool-call จริง. การเปลี่ยน pricing model ไม่ใช่ปรับ list price — เป็น **shift จาก seat economics → consumption economics** สำหรับ agent layer ที่ OpenAI วางบนหัว ChatGPT Enterprise

Workspace Agents ตัวเองออกครั้งแรกกลางเมษา OpenAI พ่วงคำว่า "successor to custom GPTs" — สิ่งที่ custom GPT ทำได้แค่ wrapper prompt + retrieval, workspace agent ทำต่อได้: รัน scheduled (ทุกเช้าวันจันทร์ pull report), รับ task ใน Slack channel ทันทีที่มีใคร @, ทำงาน async ในคลาวด์ตอนคนปิดเครื่อง, ขอ approval หรือ handoff หากเจอ branch ที่ต้องคนตัดสินใจ. หลังบ้าน **Codex** ถือ execution layer ทุก agent — code generation, browser action, tool call ทั้งหมดวิ่งผ่าน sandbox เดียวกันที่ OpenAI เปิดเป็น Standalone product ปลายปีก่อน

ขาที่ OpenAI ทุ่มหนักคือ **connector breadth** — Workspace Agents ออกมาพร้อมเสียบ Slack, Google Drive, Microsoft 365, **Salesforce, Notion, Atlassian Rovo** ตรง ๆ ผ่าน MCP-style adapter; admin set IAM ต่อ user group ได้ว่าทีมไหนเรียก tool ไหนได้บ้าง ใครสร้าง/แชร์/รัน agent ได้บ้าง — ตัด pain point ที่ enterprise IT ใช้ custom GPT ไม่ได้เพราะ governance อ่อน. รอบนี้ OpenAI วาง enterprise-grade monitoring + protect-sensitive-data control เป็นจุดขายหลัก ไม่ใช่ feature เสริม

ตัวเลขที่ลอยอยู่ background รอบ pricing transition นี้: **enterprise share ของ OpenAI revenue โตจาก 30% ปลายปีก่อน → 40%+ ตอนนี้** และอยู่บน track จะแตะ parity กับ consumer ภายในสิ้นปี 2026; revenue runrate $2B/เดือน, API ทะลุ 15B token/นาที (CNBC + OpenAI blog). หลัง round funding $122B ที่ valuation $852B ปลายมีนา นักลงทุนหลัก SoftBank/Amazon/NVIDIA/Microsoft + a16z + T. Rowe Price + retail $3B รอบใหม่นี้กดดันเรื่อง **monetize enterprise ให้คุ้ม compute ที่ลงไปแล้ว** — ตัวเลข payback period ของ deal ใหญ่จะเริ่มดูชัดในไตรมาสสามถ้ามาตรการ pricing วันนี้เห็น traction

ฝั่ง competitive — OpenAI โดนบีบจากสองทาง: **Microsoft Agent 365** ที่ GA วันที่ 1 พ.ค. ($15/seat/month, multi-cloud registry sync ดูแล agent ที่อยู่บน AWS Bedrock + Google Gemini Enterprise ด้วย — ดูเรื่องที่ 02), และ **Google Gemini Enterprise Agent Platform** ที่ Cloud Next 2026 ที่ ship A2A v1.0 production ที่ 150 องค์กรพร้อม managed MCP ผ่าน Apigee. OpenAI ไม่มี API gateway ที่ฝัง enterprise อยู่แล้ว 30k บริษัท ต้องหา leverage ที่ไหน — คำตอบคือ **distribution ผ่าน ChatGPT user base 800M+** + connector breadth ที่ดูเหมือน "open" ไม่ผูก cloud ใด

## ทำไมสำคัญ

Pattern ที่ตลาดเริ่มเห็น: **agent layer มี pricing model ใหม่ที่ไม่ใช่ seat license** — Microsoft Agent 365 คิด $15/seat แบบ classic, Google Gemini Enterprise + Agentspace คิดผสม seat + consumption, OpenAI Workspace Agents เลือก **consumption-only ทับ seat** (ChatGPT Business seat $20 + credit สำหรับ agent rep). ของจริงคือ OpenAI ต้องการให้ลูกค้า scale agent count ขึ้นได้เร็วโดยไม่เจอ procurement bottleneck — แต่ enterprise CFO กลัวที่สุดคือ unbounded consumption bill. **ใครออกแบบ guardrails (cap, alert, refund credits) ดีกว่า กิน mid-market ก่อน**

จุดที่ต้อง bet: workspace agent ของ OpenAI **ดู feature แทบเหมือน Microsoft Copilot Studio + Salesforce Agentforce** — sched, Slack handoff, approval gate, multi-tool. แต่ OpenAI ได้เปรียบใน developer mindshare (Codex distribution + ChatGPT app ecosystem) และเสียเปรียบใน enterprise governance depth (SSO, DLP, regional data residency). 12 เดือนหน้า: ถ้า OpenAI ยังไม่เปิด on-prem deploy หรือ regional model ที่จับ EU/Asia compliance ได้จริง, deal Fortune 1000 จะตกไปฝั่ง Microsoft/Google เป็นทอดคล้ายกับที่ AWS แพ้ภาครัฐช่วงปี 2018-2020

อีกชั้นที่ underrated: **Codex เป็นเครื่องยนต์ workspace agent** = OpenAI กลายเป็น **execution layer** ของ agent ที่สร้างใน LangChain/LlamaIndex/Crewหรือ CopilotKit — ลูกค้าจะ build agent ใน framework ใดก็ได้ แต่ payload สุดท้ายวิ่งใต้ Codex/o-series sandbox. ถ้า view นี้ถูก, **OpenAI เลิกแข่ง agent platform ที่ orchestration layer** — แข่งที่ runtime layer ใต้ทุก platform แทน. คล้าย Stripe ที่ไม่แข่งกับ Shopify แต่ขับ payment ใต้ Shopify

## มุม OpenBridge

**Direct relevance:** Workspace Agents = pitch ใกล้ OpenBridge มาก (cross-app workflow + Slack/Salesforce connector + scheduled run + approval gate) แต่ราคา consumption เปิดให้ OpenBridge **เสนอ flat-rate alternative** สำหรับ Thai SMB ที่กลัว variable bill — เป็นมุมที่ขายตรงกับ CFO ได้ว่า "OpenBridge รันงานเหมือน OpenAI Workspace Agents แต่ predictable cost ตามแพ็กเกจ ไม่หักเครดิตต่อ tool call". 30 วันต้อง: (1) เขียน pricing comparison sheet (OpenBridge plan vs OpenAI Workspace Agents credit estimate ที่ 100/500/2000 task ต่อเดือน), (2) ทำ landing page "predictable cost" สำหรับ workflow ที่ลูกค้าใช้ ChatGPT Business อยู่แล้ว แต่ขยับไม่ไหวเพราะ pricing เปลี่ยน

**Signal สำหรับ product roadmap:** OpenAI ผูก Codex เป็น execution layer = **workspace agent ทุกตัวจะกลาย "code-first"** ใน 6-12 เดือน. OpenBridge ที่อยู่ฝั่ง no-code/low-code workflow ต้อง decide ระหว่าง (a) ship "code mode" สำหรับ power user (เปิด Python/TypeScript inline ใน flow), (b) ทำ MCP adapter ตรงเข้า Codex ให้ workflow ของ OpenBridge ยิงงาน computational เข้า Codex sandbox แล้วรับผลลัพธ์มา compose ต่อ. ทางที่สองเร็วกว่าและไม่ต้อง hire เพิ่ม — เป็น hedge ที่ผมแนะนำ

**Strategic note:** ถ้า OpenAI ปั่น enterprise revenue ให้ถึง parity ปลายปี (โต 40% → 50% ของ revenue), การที่ OpenBridge ขาย direct ให้ Thai enterprise โดยไม่ทำ Microsoft/OpenAI co-sell program จะเป็น single biggest competitive risk ในไตรมาส 3-4. ควรเปิด **OpenAI Solutions partner application** ภายใน 30 วัน — ถึงไม่ผ่านรอบแรก, การมี relationship เปิดประตู ChatGPT Enterprise referral ที่กำลังขยายในไทยตอนนี้

## Sources
- [Introducing workspace agents in ChatGPT (OpenAI)](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)
- [OpenAI Workspace Agents: ChatGPT Business plug into Slack, Salesforce and more (VentureBeat)](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more)
- [Workspace Agents Launch in ChatGPT (UC Today)](https://www.uctoday.com/productivity-automation/openai-workspace-agents-chatgpt-enterprise-workflows/)
- [The next phase of enterprise AI (OpenAI)](https://openai.com/index/next-phase-of-enterprise-ai/)
- [OpenAI raises $122 billion at $852B valuation (CNBC)](https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html)

---

## Audio script
วันนี้หกพฤษภา OpenAI พลิก Workspace Agents จากฟรีเป็น credit based pricing เต็มตัว. ข่าวจริงไม่ใช่แค่ pricing เปลี่ยน. เป็น shift จาก seat economics ไป consumption economics สำหรับ agent layer ทั้งชั้นบน ChatGPT Enterprise.

Workspace Agents ออกกลางเมษา OpenAI พ่วงคำว่า successor to custom GPTs. custom GPT เก่าเป็นแค่ wrapper prompt บวก retrieval. workspace agent ทำได้เยอะกว่า. รัน scheduled. รับ task ใน Slack ทันทีที่ใคร mention. ทำงาน async ในคลาวด์ตอนคนปิดเครื่อง. ขอ approval หรือ handoff เมื่อเจอ branch ที่คนต้องตัดสินใจ. หลังบ้านทุกตัวเป็น Codex. code generation browser action tool call วิ่งผ่าน sandbox เดียวกัน.

ขาที่ OpenAI ทุ่มหนักคือ connector breadth. ออกมาพร้อม Slack Google Drive Microsoft 365 Salesforce Notion Atlassian Rovo เสียบตรง. admin set IAM ต่อ user group ได้ละเอียด. ตัด pain point ที่ enterprise IT ใช้ custom GPT ไม่ได้เพราะ governance อ่อน.

ตัวเลข background. enterprise share ของ OpenAI revenue โตจากสามสิบเปอร์เซ็นต์ปลายปีก่อนเป็นสี่สิบเปอร์เซ็นต์ตอนนี้. revenue runrate สองพันล้านดอลลาร์ต่อเดือน. API ทะลุสิบห้าพันล้าน token ต่อนาที. หลัง round หนึ่งร้อยยี่สิบสองพันล้านดอลลาร์ที่ valuation แปดร้อยห้าสิบสองพันล้าน นักลงทุนกดดันให้ monetize enterprise ให้คุ้ม compute.

OpenAI โดนบีบสองทาง. Microsoft Agent 365 GA วันที่หนึ่งพฤษภา สิบห้าดอลลาร์ต่อ seat ต่อเดือน multi cloud registry sync ดูแล agent บน AWS Bedrock บวก Google Gemini Enterprise ด้วย. และ Google Gemini Enterprise Agent Platform ที่ ship A2A version หนึ่งจุดศูนย์ production ที่หนึ่งร้อยห้าสิบองค์กร.

bet ของผม. ถ้า OpenAI ยังไม่เปิด on prem หรือ regional model ที่จับ EU Asia compliance ได้จริง deal Fortune 1000 จะตกไปฝั่ง Microsoft Google ในสิบสองเดือนหน้า. เหมือน AWS ที่แพ้ภาครัฐช่วงสองพันสิบแปดถึงสองพันยี่สิบ.

อีกชั้น underrated. Codex เป็นเครื่องยนต์ workspace agent. OpenAI กลายเป็น execution layer ของ agent ที่สร้างใน LangChain LlamaIndex Crew CopilotKit. ลูกค้า build ใน framework ใดก็ได้ แต่ payload วิ่งใต้ Codex sandbox. คล้าย Stripe ที่ไม่แข่ง Shopify แต่ขับ payment ใต้ Shopify.

สำหรับ OpenBridge. workspace agent pitch ใกล้เรามาก. ทางรุกคือเสนอ flat rate alternative สำหรับ Thai SMB ที่กลัว variable bill. สามสิบวันต้อง pricing comparison sheet OpenBridge vs OpenAI ที่หนึ่งร้อย ห้าร้อย สองพัน task ต่อเดือน. และ landing page predictable cost. ส่วน hedge ระยะกลาง ทำ MCP adapter ตรงเข้า Codex ให้ workflow OpenBridge ยิงงานเข้า Codex sandbox แล้วรับผลลัพธ์มา compose. เร็วกว่าการ ship code mode เอง. และต้องเปิด OpenAI Solutions partner application ภายในสามสิบวัน. ไม่ผ่านรอบแรกก็ได้ ความสัมพันธ์เปิดประตู referral.
