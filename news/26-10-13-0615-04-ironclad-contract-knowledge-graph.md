---
date: 2026-10-12
slug: ironclad-contract-knowledge-graph
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial illustration: a glowing knowledge graph of contract clauses as
  interconnected nodes, with hairline links showing obligations and
  precedents; one node is a redline marked "APPROVED POSITION" and connects
  back to past deals shown as faded cards. Numbers "EVERY AGREEMENT = ASSET",
  "GROUNDED" rendered large for thumbnail legibility. Legal-navy + warm gold
  palette on cream background, flat isometric style, 1:1 aspect, no real
  human faces. Metaphor: contracts become structured memory.
image: images/26-10-13-0615-04-ironclad-contract-knowledge-graph.png
---

# Ironclad เปิด Agent + Contract Knowledge Graph — เอา vertical legal เป็น "ข้อตกลงทุกฉบับคือ asset" และ ground agent ใน precedent ของบริษัทเอง

## TL;DR
- **8 ต.ค.** **Ironclad** ประกาศ **Ironclad Agent** + **Contract Knowledge Graph (CKG)** — vertical legal agent + structured knowledge layer ที่ ground agent ใน contract, approved position, past negotiation decision ของลูกค้าแต่ละราย
- Core concept: **"Every agreement is now an asset"** — contract เลิกเป็น PDF ที่ store ใน shared drive แล้วค้นไม่เจอ; กลายเป็น structured node ใน graph ที่ agent query ได้
- Agent call sub-agent: **Ironclad Agent → Contract Review Agent → redline contract** against approved position + deal history — การ orchestration ที่เลียนแบบ in-house legal workflow
- Audience: Legal, procurement, sales — การขยาย from "ซอฟต์แวร์ของทนาย" สู่ "ซอฟต์แวร์ของทุกคนที่แตะสัญญา"
- Follow-on จาก Ironclad Assistant (มีนาคม 2026) + contract-intelligence agents — ย้ำว่า vertical AI ที่ compound ผลลัพธ์ชนะ horizontal copilot

## เกิดอะไรขึ้น

วันที่ 8 ต.ค. Ironclad ปล่อย press release ที่ปรับ positioning ของตัวเองจาก "Contract Lifecycle Management (CLM) ที่มี AI" สู่ **"Agent-first legal platform ที่ CLM เป็น substrate"**. ประกาศ 2 ชิ้นหลัก: **Ironclad Agent** (natural language interface สำหรับ legal/procurement/sales query + action บน contract) + **Contract Knowledge Graph (CKG)** (structured layer ที่ map clause, obligation, relationship, past decision)

Point ที่ไม่ใช่ marketing fluff คือ **การ shift จาก RAG สู่ graph**. ตั้งแต่ ChatGPT ยุคแรก, legal AI startup ส่วนใหญ่ (Harvey, EvenUp, Spellbook, Robin AI) ใช้ RAG — retrieve chunk จาก contract แล้วให้ LLM สรุป. ปัญหาที่ RAG แก้ไม่ได้: **relationship ระหว่าง clause** ("ข้อ 3 ของ MSA A conflict กับข้อ 7 ของ SOW B ถ้า amendment C มีผล"). Ironclad CKG แก้ด้วย graph structure ที่ node = clause, edge = relationship/obligation/precedent — pattern ที่ fintech knowledge graph ใช้มาก่อน (Palantir Foundry, Enigma) ย้ายมา legal

Agent orchestration ที่ Ironclad โชว์: Ironclad Agent **เป็น top-level** รับ query จาก legal/procurement/sales user; เมื่อต้อง redline contract, Ironclad Agent เรียก **Contract Review Agent** (sub-agent specialized) ที่ run against CKG + approved position + deal history → redline กลับมา. Pattern นี้เป็น **multi-agent orchestration ที่ end user ไม่ต้องรู้ว่ามี sub-agent** — ซึ่งเป็น UX ที่ Google Gemini Agent (Oct 8) และ OpenAI Dots (Sep 29) กำลัง push ให้เป็น default

ขอบเขต audience สำคัญ: Ironclad ไม่พูดถึง **legal team เท่านั้น** — procurement + sales ขึ้นชัด. การเปลี่ยน positioning นี้ใหญ่กว่าที่เห็นเพราะ sales team ขนาดใหญ่ที่ hate contract bottleneck ตอนปิด deal จะ sign Ironclad license โดยไม่ต้องรอ General Counsel approve. **Sales-led buying ของ legal software** เป็น shift จาก 15 ปีที่แล้วที่ CLM ขาย CFO/GC เท่านั้น

ยังไม่เปิดเผย: pricing, exact GA date, customer logo ที่ production (press release เป็น partial). แต่ pattern ของ Ironclad คือ GA ภายใน 60-90 วันหลังประกาศ

## ทำไมสำคัญ

**Vertical AI ที่มี proprietary data + domain workflow ชนะ horizontal copilot** — argument นี้ Ironclad พิสูจน์ได้ชัด. Horizontal agent (ChatGPT, Claude, Gemini) อ่าน PDF ของสัญญาได้; แต่ไม่ได้ **ประวัติที่ลูกค้า negotiate ไปกับ counterparty นี้แล้ว 3 รอบ** ที่ Ironclad ครอบครอง + ไม่สามารถ ground agent ใน approved position ของบริษัทลูกค้าแต่ละราย. CKG คือ moat ที่ foundation model copy ไม่ได้

Point of view: **Harvey + Robin AI กำลังเจอ existential pressure**. Harvey ที่ raise $300M+ บน horizontal legal reasoning model + Robin AI ที่ specialize contract review แบบ RAG — ทั้งคู่ไม่มี **customer-specific contract repository** ที่ Ironclad มี 10,000+ customer. Ironclad shift ไปที่ graph + agent orchestration = การ turn ลูกค้าเก่าให้เป็น competitive moat ที่คู่แข่งไม่สามารถ bypass. **CLM playbook รอบที่สองคือ "ไม่ขาย software, ขาย institutional memory"**

ที่น่าสนใจกว่าคือ **pattern replication**. ถ้า Ironclad proves ว่า "vertical software + customer data history + agent orchestration" ชนะ, vertical SaaS รายอื่นจะ replicate: **DocuSign** (signature → agreement graph), **Pigment / Anaplan** (plan → scenario graph), **Workday** (HR data → organizational graph), **ServiceNow** (ticket → operations graph). ปี 2027 "Knowledge Graph as a Moat" กลายเป็น standard narrative ของ vertical SaaS

ความเสี่ยง: **customer data silos**. ถ้า Ironclad ทำได้สำเร็จ, Salesforce / HubSpot / NetSuite ไหนที่มี contract touchpoint จะต้อง (ก) acquire CLM หรือ (ข) build graph layer เอง. Salesforce (ซึ่งเคย acquire Vlocity, Slack, Tableau) ยังไม่มี contract-centric graph — bet 50/50 ว่าจะ build หรือ acquire ภายใน 18 เดือน. ลูกค้าที่ลงกับ Ironclad วันนี้ต้องเข้าใจความเสี่ยงของ consolidation M&A

## มุม AI Agent Platform

**Builders:** ถ้าคุณสร้าง vertical AI (legal, finance, HR, procurement) — **lesson ของ Ironclad คือ "shift จาก RAG สู่ graph เร็วที่สุดเท่าที่ทำได้"**. RAG ที่ดีที่สุดยัง miss cross-clause relationship, cross-deal precedent, cross-counterparty pattern. Graph structure ไม่ใช่ magic; แต่ customer-specific graph + agent orchestration = defensibility ที่ foundation model ตามไม่ทัน. Investment ของทีม: 3-6 เดือน data engineering (ไม่ใช่ ML engineer เท่านั้น)

**Users / business:** General Counsel / CFO / CPO ที่ปิดสัญญาเยอะในปีนี้ — ประเมิน Ironclad Agent + CKG ภายใน 90 วัน; benchmark **time-to-redline, exception rate ที่ sub-agent ส่ง escalation, agreement reuse rate** (เท่าไหร่ของสัญญาใหม่สามารถ clone จาก approved position เดิม). ถ้า Ironclad ยังไม่ใช่ CLM ของคุณ — เริ่มคุย counterparty transition. Legal tech ของบริษัทไทย (iTAX Legal, Dharmniti) ควร prototype graph layer เองหรือ partner กับ foundation vendor

**Ecosystem:** Harvey / Robin AI / Spellbook / EvenUp เจอ pressure สูง — ต้อง (ก) acquire CLM เพื่อได้ customer data, (ข) partner กับ CLM ที่ไม่มี agent capability, หรือ (ค) pivot ไป niche ที่ Ironclad ยังไม่แตะ (litigation, patent). Palantir Foundry + Snowflake Horizon Catalog + Databricks Unity Catalog ควร note — vertical knowledge graph คือ pattern ที่ขยายได้; **"graph as a service"** จะเป็น primitive ใหม่ที่ hyperscaler จะเข้าแข่งใน 18 เดือน

## Sources
- [Ironclad Press Release — Introducing Ironclad's Next Wave of AI Agents: Every Agreement is Now an Asset](https://ironcladapp.com/news/press-releases/ironclad-launches-new-ai-agents-grounded-in-commercial-context)
- [MarTech Series — Introducing Ironclad's Next Wave of AI Agents](https://martechseries.com/predictive-ai/ai-platforms-machine-learning/introducing-ironclads-next-wave-of-ai-agents-every-agreement-is-now-an-asset/)
- [AI Agent News Today — October 9 roundup (Ironclad coverage)](https://aiagentstore.ai/ai-agent-news/daily/2026-10-09)
- [Ironclad 2026 Release Log — Contract Knowledge Graph entry](https://support.ironcladapp.com/hc/en-us/articles/40760031220887-2026-Release-Log)

---

## Audio script
วันพุธ Ironclad ประกาศ Ironclad Agent กับ Contract Knowledge Graph. เรื่องที่ General Counsel กับ Chief Procurement Officer ของบริษัทไทยต้องรู้. เพราะ positioning ของ Ironclad เปลี่ยนจาก Contract Lifecycle Management software กลายเป็น agent-first legal platform ที่ CLM เป็น substrate

จุดที่สำคัญกว่า marketing คือการ shift จาก RAG สู่ graph. ตั้งแต่ ChatGPT ยุคแรก legal AI ส่วนใหญ่ใช้ RAG. ดึง chunk จาก contract แล้วให้ LLM สรุป. ปัญหาคือ RAG แก้ relationship ระหว่าง clause ไม่ได้. ข้อ 3 ของ MSA A ชน ข้อ 7 ของ SOW B ถ้า amendment C มีผล. Ironclad แก้ด้วย graph. node = clause. edge = relationship, obligation, precedent

การ orchestration ที่ Ironclad โชว์. Ironclad Agent เป็น top level รับ query จาก legal procurement sales. เมื่อต้อง redline สัญญา Ironclad Agent เรียก Contract Review Agent sub-agent specialized. redline กลับมา. multi-agent flow ที่ user ไม่ต้องรู้ว่ามี sub-agent. UX ที่ Google Gemini Agent กับ OpenAI Dots กำลัง push ให้เป็น default

Point of view ของผม. Harvey ที่ raise สามร้อยล้านดอลลาร์ บน horizontal legal reasoning. กับ Robin AI ที่ทำ contract review แบบ RAG. ทั้งคู่กำลังเจอ existential pressure. เพราะ Ironclad มี customer-specific contract repository ของหมื่นลูกค้า. CKG คือ moat ที่ foundation model copy ไม่ได้. CLM playbook รอบที่สองคือ ไม่ขาย software ขาย institutional memory

สำหรับทีม Enabridge. ถ้าคุณสร้าง vertical AI legal finance HR procurement — lesson คือ shift จาก RAG สู่ graph เร็วที่สุด. ลงทุน 3-6 เดือน data engineering ไม่ใช่ ML engineer เท่านั้น. ลูกค้าที่ปิดสัญญาเยอะ — ประเมิน Ironclad ภายใน 90 วัน. ถ้า CLM ของคุณไม่ใช่ Ironclad เริ่มคุย transition. legal tech ไทยควร prototype graph layer เอง หรือ partner foundation vendor

สัญญาณใหญ่กว่า. vertical AI ที่มี proprietary customer data + domain workflow ชนะ horizontal copilot. argument นี้ Ironclad พิสูจน์ได้ชัด. ปี 2027 Knowledge Graph as a Moat จะกลายเป็น standard narrative ของ vertical SaaS ทั้งวงการ. DocuSign Workday ServiceNow Pigment ทุกเจ้าที่มี customer data ประวัติจะ replicate pattern นี้
