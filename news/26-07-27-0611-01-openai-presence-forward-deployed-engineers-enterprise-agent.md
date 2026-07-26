---
date: 2026-07-27
slug: openai-presence-forward-deployed-engineers-enterprise-agent
topic: openbridge-trend
reading_time_min: 5
sources: 5
image_prompt: |
  An editorial isometric illustration on a warm cream background of a
  sleek corporate lobby with a bold gold sign reading "OPENAI PRESENCE"
  over three revolving doors labeled "VOICE", "CHAT", "CODEX". In front,
  a black-suited silhouette carries a briefcase stamped "FORWARD DEPLOYED
  ENGINEER" walking toward a client tower with logos "BBVA · SOFTBANK ·
  IAG". A giant scoreboard on the wall shows "75% CALLS RESOLVED" and
  "-15pts HANDOFFS · 10 DAYS". Sharp editorial typography, high contrast,
  1:1 aspect, no real human faces.
image: images/26-07-27-0611-01-openai-presence-forward-deployed-engineers-enterprise-agent.png
---

# OpenAI ปล่อย Presence — enterprise agent platform ที่ขายแบบ consulting, Forward Deployed Engineer เข้าไปสร้างจริง, resolve 75% call ที่ OpenAI เอง

## TL;DR
- 22 ก.ค. OpenAI เปิดตัว **Presence** — enterprise platform สำหรับ deploy voice + chat agent ที่ **มี OpenAI Forward Deployed Engineer (FDE) เข้าไปทำ deployment จริง ๆ ในบริษัทลูกค้า**
- ไม่ใช่ self-serve — จำกัด **limited GA** ผ่าน OpenAI + selected global SI ตามโมเดล OpenAI Deployment Company ($4B, $10B valuation, พ.ค. 2026)
- Proof point ที่แรง: **resolve 75% ของ English-language phone support call ของ OpenAI เอง** โดยไม่ต้อง human, และ **ลด handoff 15 percentage point ใน 10 วัน**
- Early customer: **BBVA Mexico, SoftBank Corp., Retail Insurance Australia (IAG)** — enterprise ที่ compliance หนัก + high-volume CX
- Stack: policies + SOP + guardrail + approved actions + simulation + eval + **Codex-powered improvement loop** — ทุกอย่าง managed by OpenAI

## เกิดอะไรขึ้น
วันอังคาร 22 กรกฎาคม 2026 OpenAI ประกาศ **Presence** — enterprise agent platform ที่วาง positioning ไม่เหมือน product SaaS เจ้าอื่นเลย. Presence ไม่ได้ขายเป็น license แบบ Agentforce, ไม่ใช่ credit-based แบบ ChatGPT Enterprise, และ**ไม่ใช่ self-serve** — customer เข้าถึงผ่าน **limited general availability programme** ที่ **OpenAI ส่ง Forward Deployed Engineer (FDE) เข้าไปทำ deployment ในบริษัทลูกค้าโดยตรง**, หรือผ่าน selected global systems integrator ที่ OpenAI cert.

Deployment model นี้เชื่อมโดยตรงกับ **OpenAI Deployment Company** — subsidiary ที่ OpenAI ตั้งขึ้นเมื่อ พ.ค. 2026 พร้อม backing $4 พันล้านและ valuation $10 พันล้าน. FDE คือทีมวิศวกรที่ Palantir + Anduril ใช้เป็น weapon — เข้าไปนั่งกับลูกค้า, เขียน integration, ปรับ model, ทำ eval, จน agent ทำงานได้จริงในระบบ. OpenAI copy playbook นั้นตรง ๆ — เพราะเห็นแล้วว่า enterprise agent ที่ทำงานได้จริงในโลก customer support / claims / KYC / workflow ไม่ได้เกิดจาก config ผ่าน UI แต่เกิดจาก integration งานหนักที่ vendor ต้องทำเอง.

Presence stack ครบ: **policies + standard operating procedures** (behavior spec), **guardrails** (safety layer), **approved actions** (whitelist ของสิ่งที่ agent ทำได้), **simulations + evaluation tools** (offline test ก่อน production), และ **Codex-powered improvement process** (loop ที่ auto-tune agent จาก transcript หลัง launch). ทั้งหมด managed by OpenAI — ลูกค้าไม่ต้อง maintain framework เอง.

Proof point ที่ OpenAI นำมาโชว์เป็น hero metric คือ **OpenAI ใช้ Presence กับ phone support ของตัวเอง — resolve 75% ของ English-language call โดยไม่ต้องส่งต่อ human, และลด agent-to-human handoff 15 percentage point ภายใน 10 วัน**. Early customer roster ก็หนัก: **BBVA Mexico** (retail banking, KYC + card dispute), **SoftBank Corp.** (Japanese telco, tier-1 support), **Retail Insurance Australia (IAG)** (claims triage) — สาม vertical ที่ compliance regulator ไม่ให้ผิดพลาดและ volume สูงพอที่ ROI จะเห็นเร็ว.

## ทำไมสำคัญ
**OpenAI เพิ่งเปิดหน้าใหม่ของสงคราม enterprise agent — จาก platform war มาเป็น deployment war.** สาม tier ที่ตลาดเห็นตอนนี้: (1) Salesforce/ServiceNow/Microsoft ขาย platform + credit ให้ builder ทำเอง, (2) Anthropic ขาย model + Claude Cowork ให้ knowledge worker ใช้ตรง, (3) OpenAI Presence — **ขาย outcome พร้อมทีมวิศวกรที่มาทำให้ agent ทำงานจริง**. Positioning นี้ตรงข้ามกับ narrative "self-serve, democratize AI" ที่ Sam Altman พูดมาสามปี — แต่ตรงกับความจริงที่ enterprise CIO ทุกคนเจอ: **agent ไม่ได้ deploy ยากเพราะ model โง่ แต่เพราะ integration + eval + change management ยาก**. คนที่แก้ปัญหานี้ได้คนแรกจะ lock ตลาด enterprise ที่ Gartner คาดว่า $234 พันล้านของ enterprise app spending จะย้ายมาที่ agent ภายในปี 2030.

Pattern ที่น่าจับตาต่อไปคือ **Palantir-ification ของ AI vendor**. Palantir สร้าง $87B market cap ไม่ใช่ด้วย product — ด้วย FDE team ที่เข้าไปนั่งกับลูกค้า Fortune 500 + agency 3-6 เดือน. OpenAI เห็นตัวเลข ($1B AI ACV ของ ServiceNow, $1.2B Agentforce ARR ของ Salesforce, $1.6B Missionforce VA deal) แล้ว realize ว่า self-serve ChatGPT Enterprise ที่ $60/user/month ไม่ scale เท่า $millions ต่อ deployment แบบ Palantir. **การที่ Anthropic เปิด Claude Cowork enterprise ที่ $100/user/month กับ SOC 2 + custom VM (เมื่อ ก.ค. 7)** ก็อยู่ใน family เดียวกัน — vendor ที่ทำ model จะไม่ยอมให้ SI (Accenture, Deloitte, Capgemini) กิน margin ทั้งหมดของ AI transformation อีกต่อไป.

## มุม AI Agent Platform
**Builders:** ถ้ากำลังสร้าง agent framework / orchestration / eval tool — Presence stack คือ blueprint ที่ต้อง benchmark กับตัวเอง. หลาย component (SOP repo, approved-actions gate, simulation harness, Codex-improvement loop) เป็นสิ่งที่ open framework (LangGraph, CrewAI, Autogen) ยังไม่มี native. คำถามที่ต้องตอบ: "customer ที่ deploy บน framework เราต้อง build 6 อย่างนี้เองใช่ไหม? ถ้าใช่ Presence จะกิน share market segment ที่ CIO ไม่มีทีม engineering หนักพอ." สอง — ถ้ากำลังสร้าง vertical agent (legal, healthcare, insurance) ที่ compete กับ Presence จะโดน OpenAI FDE เข้าไปทับ vertical — ต้อง moat ที่ domain data + regulatory approval + relationship, ไม่ใช่ agent quality.

**Users / business:** ถ้าเป็น enterprise ที่กำลัง evaluate agent platform Q3-Q4 นี้ — Presence เป็น option ใหม่ที่ **ต้องขอ OpenAI มา pitch** พร้อม FDE. Compare กับ Salesforce Agentforce (pay-per-resolution $2 ต่อ ticket resolved, GA ก.ค. 2), ServiceNow Otto (subscription + AI ACV disclosure), Microsoft Agent 365 (bundled ใน E5). สาม price mechanic ที่ต่างกันสิ้นเชิง — ต้องเลือกตาม volume + integration complexity + team skill. Enterprise ที่ไม่มี in-house AI engineering team จะเลือก Presence, ที่มีจะเลือก Agentforce / Otto ที่ตัวเองคุมได้. **สำคัญที่สุด**: Presence เป็น managed service — ต้องอ่าน SLA / data residency / model version control ให้ละเอียด เพราะ FDE จะเข้าถึง customer data ระดับ core system.

**Ecosystem:** สงคราม SI ระเบิดใหม่. Accenture, Deloitte, Capgemini, TCS, Infosys ที่ position ตัวเองเป็น "agent implementation partner" อยู่ตอนนี้ — **OpenAI ประกาศจะเลือกแค่ selected global SI เข้าเป็น partner Presence** — คนที่ไม่ได้เลือกจะเสีย pipeline. Sovereign / regional SI (Enabridge, Bluebik, Datamesh ใน SEA) มี window 6-12 เดือนก่อน OpenAI จะขยาย network — window นี้คือช่วง proof-point ที่ต้องปิด case ให้ได้เร็วที่สุด. Vendor ที่ขาย eval / observability / policy engine (Weights & Biases, LangSmith, Arize, Braintrust, HumanLoop) จะเจอ Presence ที่ bundle ทุกอย่างไว้ในกล่องเดียว — ต้อง reposition เป็น "cross-model / cross-vendor" ไม่ใช่ "best-in-class per tool".

## Sources
- [Introducing OpenAI Presence](https://openai.com/index/introducing-openai-presence/)
- [OpenAI unveils Presence, a new platform that lets enterprises launch and manage realtime voice agents and chatbots — VentureBeat](https://venturebeat.com/orchestration/openai-unveils-presence-a-new-platform-that-lets-enterprises-launch-and-manage-realtime-voice-agents-and-chatbots)
- [OpenAI Presence sells enterprise AI agents with engineers attached — AI News](https://www.artificialintelligence-news.com/news/openai-presence-enterprise-ai-agents/)
- [OpenAI Presence connects AI agents to enterprise data with built-in guardrails — Help Net Security](https://www.helpnetsecurity.com/2026/07/22/openai-presence-ai-agent-platform/)
- [OpenAI Tries the Consulting Path with 'Presence' — Ground News](https://ground.news/article/openai-launches-presence-for-enterprise-voice-agents)

---

## Audio script
โอเคเช้านี้เรื่องใหญ่ที่สุดชื่อ OpenAI Presence. OpenAI เปิดตัววันที่ 22 กรกฎาคม — enterprise agent platform สำหรับ voice และ chat agent, แต่ขายไม่เหมือน SaaS อื่นเลย. Presence ไม่ใช่ self-serve — customer ต้องเข้าถึงผ่าน limited GA ที่ OpenAI ส่ง Forward Deployed Engineer หรือ FDE เข้าไปนั่งกับลูกค้าและทำ deployment ให้จริง ๆ. โมเดลนี้ copy มาจาก Palantir กับ Anduril — เข้าไปสร้างงานให้ลูกค้าเสร็จ ไม่ใช่ปล่อยให้ config เอง.

Proof point ที่ทำให้ตลาดสะดุ้งคือ OpenAI ใช้ Presence กับ phone support ของตัวเอง — resolve 75% ของ English-language call โดยไม่ต้องส่งต่อคน, ลด handoff 15 percentage point ใน 10 วัน. Early customer ก็หนัก — BBVA Mexico, SoftBank Corp, IAG Australia — สาม vertical ที่ compliance หนักและ volume สูง.

Signal ที่สำคัญ: OpenAI เปิดหน้าใหม่ของสงคราม enterprise agent — จาก platform war ไปเป็น deployment war. Salesforce ขาย pay-per-resolution สอง dollar ต่อ ticket, ServiceNow ขาย AI ACV, Microsoft bundle Agent 365 ใน E5, OpenAI Presence ขาย outcome พร้อม engineer. สี่ mechanic ที่ต่างกันสิ้นเชิง — CIO ทุกคนต้องกลับไปคิดใหม่ว่าจะเลือกอันไหน.

สำหรับทีม SI ในไทย ทั้ง Enabridge เอง Bluebik Datamesh — window 6-12 เดือนที่ OpenAI ยังไม่ขยาย partner network คือช่วงต้องปิด proof-point ให้เร็วที่สุด ก่อนที่ FDE ของ OpenAI จะเข้ามา cover ตลาด SEA ได้เต็มที่.
