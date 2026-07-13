---
date: 2026-07-14
slug: cisco-90k-personal-agent-model-routing-onprem
topic: use-case
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial isometric hero illustration of a giant glowing corporate tower
  labeled "CISCO" on a dark technical plane, with a bright neon banner
  across the front reading "90,000 EMPLOYEES / 1 AGENT EACH". In front of
  the tower, silhouettes of tiny workers each stand next to a small
  personal robot-agent icon; a giant router-box on the left routes glowing
  wires labeled "cheap model", "mid model", "frontier" into different
  agent icons. In the bottom corner, a red side-panel reads "4,000 LAYOFFS
  SAME MONTH". High-contrast teal-and-amber cinematic palette, bold text
  readable at 200px thumbnail, 1:1 aspect, no real human faces.
image: images/26-07-14-0609-01-cisco-90k-personal-agent-model-routing-onprem.png
---

# Cisco แจก personal AI agent ให้ 90,000 พนักงานสิ้นเดือน ก.ค. — model routing + on-prem เป็น blueprint ของ enterprise agent ที่ scale จริง

## TL;DR
- Cisco เริ่มปีการเงินใหม่ปลาย ก.ค. ด้วยการแจก **personal AI agent ให้พนักงานครบทั้ง 90,000 คน** — largest known internal agent rollout ของบริษัท Fortune 100 ที่มีตัวเลข deployment ชัดเจน
- CFO Mark Patterson วาง architecture ที่ **route แต่ละ task ไปหา model ที่ถูกที่สุดที่ทำงานได้** ไม่ default frontier — model routing กลายเป็น cost lever ที่ CIO ทุกคนต้องมี, ไม่ใช่ optimization ทีหลัง; infra ส่วนใหญ่รันบน **on-premises** เพื่อ control ทั้ง cost + data
- ใน department finance เอง Cisco ใช้ AI เขียน **80–90% ของ first draft MD&A** ใน public filing ไปแล้ว, กำลัง build **"CFO cockpit"** dashboard — deployment นี้ ship ในเดือนเดียวกับที่ Cisco ปลดคน **4,000 ตำแหน่ง** และเป็น trust test ที่ทุก enterprise agent rollout ต่อจากนี้ต้องอธิบาย

## เกิดอะไรขึ้น
1 ก.ค. Fortune ตี exclusive กับ Mark Patterson, CFO Cisco: เมื่อปีการเงินใหม่เริ่ม (สิ้น ก.ค.) พนักงานทุกคนของ Cisco 90,000 คนจะได้รับ **personal AI agent** ประจำตัว. เป็นครั้งแรกที่บริษัทระดับ enterprise IT vendor ประกาศตัวเลข rollout ทั้งองค์กรพร้อม architecture — Amazon, Google, Microsoft ก็แจก AI ให้พนักงาน แต่ไม่มีใครประกาศ agent-per-employee ที่มี model routing + on-prem policy ระดับนี้

จุดที่ทำให้ deployment นี้เป็น blueprint คือ **cost engineering**. Patterson บอก Fortune ตรง ๆ ว่า Cisco จะ **ไม่ default ไป frontier model** สำหรับทุก task. ระบบมี routing layer ที่ตัดสินใจว่า task นี้ควร run บน cheap model (classification, extraction, chat), mid tier (summarization, tool use), หรือ frontier (complex reasoning, code review) — และ route แบบ dynamic. Infrastructure ส่วนใหญ่รันบน on-premises ของ Cisco เอง ทั้งเพื่อ cost economy of scale (Cisco มี compute + network อยู่แล้ว) และเพื่อ data control ที่ finance/legal team อยากได้

โมเดลนี้ Cisco พิสูจน์ใน finance ก่อน. Patterson บอกว่า AI ในทีมของเขาผลิต **first draft ของ Management Discussion & Analysis 80–90%** ใน public filing (10-Q, 10-K) — เอกสารที่มี legal exposure สูงและถือว่า sacred ในบริษัท public. ทีมกำลัง build **"CFO cockpit"** — dashboard ที่ synthesize performance data, forecast, และแนะนำ next action ให้ CFO. ถ้าทำงานใน finance ได้ regular department อื่นก็ควรได้ — logic ของ Cisco คือแบบนั้น

context ที่ทำให้เรื่องนี้ไม่ใช่แค่ productivity story: Cisco ประกาศ layoff **~4,000 ตำแหน่ง** ในเดือนเดียวกัน. บทวิเคราะห์จาก UC Today, CXM, Memeburn ตี frame ว่าเป็น **"biggest trust test of enterprise AI"** — จะรัน agent เข้ามาแทน function ที่คนเพิ่งถูกปลดหรือเปล่า, พนักงานที่รอดมาจะ trust agent ที่ถูก positioning ว่า "co-pilot" แค่ไหน. Patterson ยังไม่แถลงตัวเลขว่า cost per employee-agent ต่อเดือนอยู่ที่เท่าไร (เขาบอก Fortune ว่า "significant but manageable") ซึ่งเป็นข้อมูลที่ CIO ทุกที่จะขอ

## ทำไมสำคัญ
Enabridge track patternนี้มาหลายเดือน — **enterprise agent deployment ที่ scale ไม่ได้ติดที่ model quality, ติดที่ economics + governance**. ตัวเลขจาก Salesforce เอง Agentforce **<10% ของลูกค้า scale ผ่าน pilot** ทั้ง ๆ ที่ product ดี; median time-to-value ในตลาดคือ **5.1 เดือน**. Cisco เพิ่งเสนอ counter-hypothesis: ถ้า **model routing + on-prem + top-down mandate จาก CFO** พร้อม, deployment ระดับ enterprise-wide ทำได้ในไตรมาสเดียว. เป็น first datapoint ที่มี scale + specificity พอที่ CIO อื่นเอาไป benchmark ได้

signal สำหรับ market: **model routing กลายเป็น first-class infrastructure primitive** ไม่ใช่ optimization layer ทีหลัง. ปีที่แล้วบริษัทซื้อ frontier subscription แล้ว throw ทุก task ใส่ — ตอนนี้ economics บังคับให้ต้องมี **cost-aware execution graph**. Startup อย่าง Portkey, Kong AI Gateway, LiteLLM, Not Diamond, Martian ทั้งหมดขาย routing เป็น product — Cisco เพิ่งให้ demand side signal ระดับ 90K seat. อีกด้าน on-prem: Cisco คือคนขาย compute + networking — deploy บน infra ตัวเองมี strategic angle ต่อ Silverback narrative ที่บอกว่า "enterprise AI ไม่ควรพึ่ง hyperscaler อย่างเดียว"

ที่น่าจับตาระยะกลางคือ **trust dynamic**. รอบ layoff+AI rollout ในเดือนเดียวกันจะกลายเป็น case study ของ HR/legal team ทั่วโลก. ถ้าพนักงาน Cisco แล้ว productivity ขึ้น ~ตัวเลข public + retention ไม่ลด, playbook นี้จะ replicate ไปทั่ว Fortune 500 ใน 12–18 เดือน. ถ้าเกิด employee revolt / union pushback / drop in output quality — enterprise CIO อื่น ๆ จะเบรก rollout ของตัวเอง. เดือนสิงหาคม–ตุลาคม 2026 คือ observation window

## มุม AI Agent Platform
สำหรับ **builders**: routing เป็น table stakes แล้ว. Framework ไหนที่ยัง hardcoded model per agent — Claude Agent SDK, LangGraph, CrewAI, AutoGen — ต้องมี built-in router primitive ในเวอร์ชันถัดไป (หลาย tool เริ่มมีแล้วแต่ยังไม่ default). Builder ที่ทำ agent runtime + on-prem deployment (Anthropic Enterprise, Databricks Mosaic, Snowflake Cortex Agents, Nutanix GPT-in-a-Box) เพิ่งได้ demand pull ที่ชัดที่สุดในปีนี้ — pitch "run agents บน infra ของคุณเอง ประหยัด 40–70%" มี proof point อ้างอิงแล้ว

สำหรับ **users/business** ที่ deploy agent: ก่อน sign multi-year contract กับ vendor ไหน ให้ถามหลายคำถาม — (1) รองรับ multi-model routing หรือ lock ที่ frontier เดียว, (2) มี on-prem/private deploy option หรือเปล่า, (3) audit log + cost attribution granular ระดับ user + task หรือไม่. ถ้า vendor ตอบไม่ได้ทั้งหมด — คือ still 2025 product. สำหรับองค์กร Thai: SET-listed enterprise ที่พึ่งเริ่มพิจารณา agent มี window ~6 เดือนก่อนที่ playbook Cisco จะกลายเป็น expected baseline; ทีม CFO ควรเริ่ม inventory workflow ที่ AI ทำ first draft ได้ (management commentary, board pack, budget variance narrative) เป็น pilot ทำนอง Cisco ก่อน

สำหรับ **ecosystem**: hyperscaler ที่ขาย managed agent runtime (Azure AI Foundry, Vertex AI Agent Builder, Bedrock Agents) เจอ counter-narrative — Cisco เลือก run เอง. คาดว่า hyperscaler ทั้งสามจะเร่ง product ที่รองรับ hybrid/on-prem deployment ใน Q3–Q4. Vendor ขาย observability + cost governance (Datadog LLM Observability, Arize, Airia, Braintrust) เพิ่งเข้า critical infrastructure category — CFO ที่จะ approve budget ระดับ 90K seat ต้องเห็น dashboard สรุปว่า agent ใครใช้เท่าไร routing แม่นแค่ไหน. อีกกลุ่มคือ change management + workforce comms consulting — deployment 90K seat ที่มาพร้อม layoff ต้องการ playbook ที่ยังไม่มีใครเขียน; Accenture/BCG/McKinsey เตรียมออก practice ใหม่ก่อนสิ้นปี

## Sources
- [Cisco is rolling out AI agents to every single one of its 90,000 employees — Fortune](https://fortune.com/2026/07/01/cisco-cfo-ai-agents-finance-employees-mark-patterson/)
- [Cisco's 90,000 Employees Will Soon Have Personalized AI Agents — Entrepreneur](https://www.entrepreneur.com/business-news/cisco-has-90000-employees-each-of-them-will-soon-have-their-own-ai-agent)
- [Cisco's 90,000-Employee AI Agent Rollout Could Become Enterprise AI's Biggest Trust Test — UC Today](https://www.uctoday.com/employee-engagement-recognition/ciscos-90000-employee-ai-agent-rollout-could-become-enterprise-ais-biggest-trust-test/)
- [Cisco's AI Agent Rollout Lands the Same Month as Layoffs — CXM](https://cxm.world/employee-experience/cisco-ai-agent-rollout-layoffs-employee-trust/)
- [Cisco Hands AI Agents to 90,000 Workers After 4,000 Layoffs — Memeburn](https://memeburn.com/cisco-ai-agents-employees/)

---

## Audio script
วันที่ 1 กรกฎาคมที่ผ่านมา Fortune ตี exclusive กับ Mark Patterson CFO ของ Cisco เขาบอกว่าเมื่อปีการเงินใหม่ของ Cisco เริ่มปลายเดือนกรกฎาคม พนักงานทุกคนของ Cisco เก้าหมื่นคนจะได้รับ AI agent ประจำตัว นี่เป็น largest known internal agent rollout ของ Fortune 100 ที่มีตัวเลข deployment ชัดเจน

จุดที่ทำให้ deployment นี้เป็น blueprint คือเรื่อง cost engineering Patterson บอกตรง ๆ ว่า Cisco จะไม่ default ไป frontier model สำหรับทุก task ระบบมี routing layer ที่ตัดสินใจว่า task นี้ควรวิ่งบน cheap model mid tier หรือ frontier — route แบบ dynamic infrastructure ส่วนใหญ่รันบน on premises ของ Cisco เอง ทั้งเพื่อ cost economy of scale และเพื่อ data control ที่ finance กับ legal team อยากได้ ในทีม finance ของ Patterson เอง AI ผลิต first draft ของ MD&A section แปดสิบถึงเก้าสิบเปอร์เซ็นต์ในเอกสาร public filing ไปแล้ว ทีมกำลัง build CFO cockpit เป็น dashboard ที่ synthesize performance data กับ forecast

context ที่ทำให้เรื่องนี้ไม่ใช่แค่ productivity story คือ Cisco ประกาศ layoff สี่พันตำแหน่งในเดือนเดียวกัน UC Today กับ CXM ตี frame ว่าเป็น biggest trust test ของ enterprise AI จะรัน agent เข้ามาแทน function ที่คนเพิ่งถูกปลดหรือเปล่า พนักงานที่รอดมาจะ trust agent แค่ไหน

signal สำหรับ market model routing กลายเป็น first class infrastructure primitive แล้ว ไม่ใช่ optimization ทีหลัง สำหรับ builder ที่ทำ framework agent runtime ต้องมี built in router สำหรับ business ที่จะ deploy ให้ถาม vendor สามข้อ multi model routing on prem option cost attribution granular ระดับ user ถ้าไม่ครบ product นั้นยังเป็น 2025 product สำหรับ enterprise ไทยที่กำลังพิจารณา agent มี window ราวหกเดือนก่อนที่ playbook Cisco จะกลายเป็น expected baseline ทีม CFO ควรเริ่ม inventory task ที่ AI ทำ first draft ได้เป็น pilot ก่อน
