---
date: 2026-10-05
slug: 26-10-06-0615-01-cohere-north-2-memory-token-caps
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial hero: a sleek enterprise-grade agent cockpit, titled "NORTH 2".
  Center: a glowing memory ribbon labeled "CROSS-SESSION MEMORY" threading
  through three screens — "ON-PREM", "VPC", "AIR-GAPPED". A fuel-gauge dial
  on the right reads "TOKEN CAP" with numbers "2 GPUs min". Carahsoft shield
  stamp bottom-left for government distribution. Isometric vector style, deep
  Cohere blue + white + warm gold accents, 1:1 aspect, no real human faces.
image: images/26-10-06-0615-01-cohere-north-2-memory-token-caps.png
---

# Cohere ปล่อย North 2 — ให้ enterprise agent "มี memory + ใช้ token ตาม budget", ลงรัฐบาลผ่าน Carahsoft

## TL;DR
- Cohere เปิด **North 2** 5 ต.ค. 2026 — enterprise agentic platform ที่เพิ่ม **cross-session memory**, **token spending cap ระดับองค์กร**, orchestration harness ใหม่, deploy ได้บน cloud / on-prem / **air-gapped** บน GPU แค่ **2 ตัว**
- **Carahsoft** รับหน้าที่กระจายให้ US public sector ทันที — Cohere เปิดเกมเจาะ government ชนกับ Palantir, Microsoft, Oracle Gov
- ปี 2026 ตลาด agent ย้ายจาก "model ไหนเก่ง" ไป "แพลตฟอร์มไหนคุม cost + context + sovereignty ได้" — North 2 ยืนตรง intersect นี้พอดี

## เกิดอะไรขึ้น

เมื่อวาน (5 ต.ค.) Cohere เปิด **North 2** — รุ่นถัดจาก North ที่ปล่อยปีก่อน. ของใหม่สามอย่างหลัก: (1) **persistent memory** ข้าม session, agent จำได้ว่า user คนนี้ทำโปรเจกต์อะไร เลือก supplier เจ้าไหน แก้ bug แบบไหน; (2) **redesigned orchestration harness** ที่ Cohere บอกว่าเขียนใหม่หมดจาก learning ของการ deploy North ปีที่ผ่านมาใน finance, healthcare, telco, manufacturing, energy, public sector; (3) **granular token spending controls** — admin ตั้งเพดาน token spend ต่อ team / agent / workflow ได้ และดู utilization แบบ real-time

Deployment story คือ differentiator จริง: on-prem, virtual private cloud, hybrid, และ **fully air-gapped** — ทุก mode ใช้ hardware **ขั้นต่ำแค่ 2 GPUs**. Cohere ยืนยันกับ TechCrunch ตัวเลขนี้เป็นตัวเลขทางการ. นี่คือ pitch ตรงใจ CIO ของ bank/government/healthcare ที่มี GPU budget จำกัดแต่ compliance บังคับ data residency

Enterprise connector catalog ที่มาพร้อม North 2: Slack, SharePoint, OneDrive, Microsoft Outlook, Microsoft Exchange, Jira, Linear, Notion, GitHub — ครอบ productivity stack ของ enterprise ตะวันตกเกือบครบ. Cohere บอกใน blog launch ว่า "enterprise AI without compromises" — ภาษานี้ชัดว่ายิง head-to-head กับ Microsoft Agent 365 ที่ต้องรัน Azure และ Salesforce Agentforce ที่ต้องผูกกับ Salesforce ecosystem

และก้าวใหญ่สำหรับ GTM: **Carahsoft** — distributor อันดับหนึ่งของ US federal/state/local — ประกาศเป็น public sector distributor ของ Cohere อย่างเป็นทางการพร้อม North 2. agencies จะซื้อ Cohere model + North platform ผ่าน GSA schedule, SEWP, NASPO ValuePoint vehicles ที่ procurement team รัฐบาลใช้อยู่แล้ว

## ทำไมสำคัญ

Cohere เลือก **ไม่สู้ frontier capability แข่ง benchmark** กับ OpenAI/Anthropic/Google — ยืนบน "ของเรา deploy ที่ไหนก็ได้ จำได้ คุม cost ได้". พูดอีกอย่าง: Cohere ยอมปล่อย เส้นแข่ง "ตอบคำถามยาก" ให้ frontier lab, แล้ววิ่งเส้นที่ enterprise จ่ายเงินจริง — **compliance, cost, sovereignty**

Pattern นี้ตรงกับที่เราเห็นเมื่อสัปดาห์ก่อน: IBM Bob self-hosted (air-gapped, Nemotron + Poolside), DigitalOcean Agent Droplets (flat pricing), NinjaTech SuperNinja Enterprise (open-weight, 10x ถูกกว่า frontier). ปี 2026 ตลาด enterprise agent **แยกเป็นสองชั้น**: ชั้นบน (OpenAI, Anthropic, Google) ขาย frontier intelligence; ชั้นล่าง (Cohere, IBM, DO, NinjaTech) ขาย **control + economics**. และตลาดชั้นล่างใหญ่กว่าในแง่จำนวน seats

เรื่องที่น่าสังเกตคือ **memory + token cap** กลายเป็น table stakes พร้อมกัน. Memory โดยไม่มี budget control = agent มี context ที่อยากเท่าไหร่ก็ได้ แต่ invoice ของ CFO ระเบิด; budget control โดยไม่มี memory = agent ลืมทุกครั้งจนประหยัดจริงไม่ได้ (user ต้อง re-explain = burn token ซ้ำ). Cohere วาง 2 ตัวนี้คู่กัน — บอกว่าปี 2027 ตลาด enterprise agent จะเริ่ม consolidate รอบ 3 primitive นี้: **memory, budget, deployment surface**

## มุม AI Agent Platform

**Builders:** คนทำ agent framework / orchestration ต้องเพิ่ม **first-class budget controls** ใน SDK ก่อนสิ้นปี — Microsoft Agent 365 มี cost dashboard แล้ว, DigitalOcean มี per-droplet pricing, ตอนนี้ Cohere มี per-agent token cap. LangChain/LlamaIndex/AutoGen/CrewAI ที่ไม่มี budget primitive ใน abstraction layer จะหา enterprise GTM ยากขึ้นภายใน 2 ควอเตอร์. **Users / business** ใน regulated sector (bank, healthcare, gov) ที่กำลัง pilot cloud-only agent มี option ใหม่ที่ deploy air-gapped บน 2 GPUs — RFP ปี 2027 จะเพิ่ม criteria "cross-session memory + per-team token cap + air-gapped mode" เป็น mandatory. **Ecosystem:** Carahsoft channel = Cohere เข้า federal procurement ไม่ต้องสร้าง sales motion เอง; Palantir Foundry (ที่โตมากจาก gov contract) ต้องตอบด้วย "North-equivalent agent surface"; Databricks + Snowflake จะเร่งสร้าง connector เข้า North 2 เพราะ enterprise data นั่งอยู่ตรงนั้น; Nvidia ชนะเพิ่ม — North 2 บน 2 GPUs ยัง Nvidia-first (ยังไม่เห็น AMD MI325X mention)

## Sources
- [Cohere unveils North 2 AI agent platform with rebuilt orchestration and token spending caps - SiliconANGLE](https://siliconangle.com/2026/10/05/cohere-unveils-north-2-ai-agent-platform-with-rebuilt-orchestration-and-token-spending-caps/)
- [Cohere Launches North 2 With Redesigned Agent Harness and Memory - Unite.AI](https://www.unite.ai/cohere-launches-north-2-with-redesigned-agent-harness-and-memory/)
- [North 2: Enterprise AI Without Compromises - Cohere Blog](https://cohere.com/blog/introducing-north-2)
- [Carahsoft to Distribute Cohere AI Models, North Platform to Government - ExecutiveBiz](https://www.executivebiz.com/articles/cohere-carahsoft-public-sector-ai-distribution-partnership)

---

## Audio script
เมื่อวานที่ 5 ตุลา Cohere เปิด North 2 — enterprise agent platform เวอร์ชันใหม่. ของใหม่สามอย่าง หนึ่ง persistent memory ข้าม session, agent จำได้ว่า user ทำโปรเจกต์อะไร เลือก supplier เจ้าไหน. สอง token spending cap ระดับองค์กร admin ตั้งเพดาน token ต่อทีมได้ ต่อ agent ได้ ต่อ workflow ได้. สาม orchestration harness เขียนใหม่หมดจาก learning ของการ deploy North ในปีที่ผ่านมา. ที่น่าสนใจคือ deployment — on-prem, VPC, air-gapped ทุก mode ใช้ GPU ขั้นต่ำแค่ 2 ตัว, Carahsoft เป็น distributor ให้รัฐบาลสหรัฐ. Signal สำคัญคือ Cohere เลือกไม่สู้ frontier capability แข่ง benchmark แล้ว แต่ยืนบน "deploy ที่ไหนก็ได้ จำได้ คุม cost ได้". สอดคล้องกับ IBM Bob, DigitalOcean, NinjaTech ที่ขายเส้นเดียวกัน. ตลาด enterprise agent แยกเป็นสองชั้นชัดเจน ชั้นบนขาย intelligence ชั้นล่างขาย control. ปีหน้า RFP จะมี criteria ใหม่ cross-session memory, per-team token cap, air-gapped mode เป็นมาตรฐาน. Builder ที่ไม่มี budget primitive ใน SDK จะหา enterprise ขายยากขึ้นภายในสองไตรมาส
