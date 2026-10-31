---
date: 2026-10-30
slug: mintive-agent-identity-mcp-gateway
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a glass control tower stamped
  "MINTIVE AGENT IDENTITY" at the center of a corporate campus. Five labeled
  pipelines flow into the tower from building silhouettes marked "RO",
  "MODERN TREASURY", "U-MICHIGAN", "COURSERA", "APAX". Above the tower a bold
  three-line counter reads "2.5M CALLS / DAY", "200M+ IN 7 MONTHS",
  "50+ ENTERPRISE CUSTOMERS". A side panel shows two gates labeled
  "MCP GATEWAY" and "LLM GATEWAY" plus a shield labeled "MINT GUARD —
  PROMPT INJECTION, SECRETS". Deep navy palette with mint-green and gold
  highlights, 1:1 aspect, strong contrast for 200px thumbnails, no real
  human faces.
image:
---

# Mintive แตะ 2.5M agent call ต่อวัน — agent identity กำลังกลายเป็นชั้น infra ใหม่ของ enterprise

## TL;DR
- **Mintive** (เดิมชื่อ Lantern) ประกาศ 30 ต.ค. 2026 ว่าแพลตฟอร์ม governance สำหรับ agent handle **2.5M calls/day, 200M+ calls ใน 7 เดือน, 50+ paying enterprise customer** — raise **$7M** รอบใหม่นำโดย Cowboy Ventures (รวมสะสม $11M, Coatue + Operator Collective ร่วม)
- Thesis ชัด: **agent ต้องมี identity ของตัวเอง** เหมือน employee — Mintive มี **MCP Gateway** (คุม tool access), **LLM Gateway** (คุม model call), **Mint Guard** (ตรวจ prompt injection + secret leak), audit trail ที่ trace ย้อนได้ถึง person → agent → MCP server → model
- Customer จริง: **Ro** (telehealth), **Modern Treasury** (payments), **U of Michigan**, **Coursera**, **Apax**. Modern Treasury รายงาน agent ที่ build บน Mintive **ลดเวลา case ง่าย 30 นาที, case ซับซ้อน 4 ชั่วโมง**
- Signal: identity + gateway layer เริ่ม **สปริ้นออกจาก** horizontal agent framework (CrewAI, LangGraph) — enterprise CISO ซื้อ gateway ก่อน framework, ไม่ใช่ตรงกันข้าม

## เกิดอะไรขึ้น

29 ต.ค. 2026 Mintive co-founder และ CEO **Jiquan "JQ" Ngiam** (อดีต Head of AI ที่ Coursera, อดีต research scientist ที่ Google Brain) ออกมายืนยันตัวเลขที่น่าตกใจสำหรับ startup ที่ยังไม่มีคนรู้จักกว้าง: platform handle **2.5 ล้าน agent call ต่อวัน, 200 ล้านกว่า call ใน 7 เดือน, 50 กว่า paying enterprise customer**. รอบ $7M นำโดย Cowboy Ventures (Aileen Lee) ปิดพร้อมประกาศ, รวมสะสม $11M จาก Coatue, Operator Collective, Burst, Maven, Hustle Fund และ angel

Mintive วางตัวเองเป็น "**agent identity + governance layer**" ที่นั่งระหว่าง (1) human user, (2) AI agent, (3) tool/MCP server, (4) model. แกน core สามส่วน: **MCP Gateway** คุมว่า agent ไหนเข้า tool ไหนได้ (เทียบง่ายๆ = IAM policy สำหรับ agent); **LLM Gateway** คุม model routing + cost; **Mint Guard** คือ runtime screening ที่ตรวจ prompt injection, exposed secret, PII leak. ทุก call มี audit trail ที่ trace กลับได้ถึง **person → agent → server → model**

Customer เปิดเผย 5 ราย: **Ro** (telehealth, ใช้ agent ใน clinical ops), **Modern Treasury** (payment infra, ใช้ agent ช่วย reconcile), **University of Michigan** (ใช้ Mintive เป็น enterprise MCP gateway), **Coursera** (ex-Ngiam employer, ใช้ agent ช่วย content ops), **Apax Partners** (private equity, ใช้ใน deal workflow). Stability AI Head of Security Christian Burrows ไม่ใช่ customer official แต่ quote สนับสนุนว่า "secure path = easy path" ได้ผลกว่าปิดกั้น

ตัวเลขที่หนัก: **Modern Treasury รายงาน Mintive-built agent ตัดเวลา case ง่าย 30 นาที, case ซับซ้อน 4 ชั่วโมง**. ถ้าทีม support มี 20 คน handle 100 case/วัน และ 20% เป็น case ซับซ้อน → saving ~80 man-hour/วัน = ~$4-6k/วัน ที่ marginal cost. ตัวเลขนี้คือ **business case ชัดที่ทำให้ CISO เซ็น SOW** — ไม่ใช่ demo

## ทำไมสำคัญ

ประเด็นที่หนึ่ง — **agent identity กำลังเป็น primitive ที่ enterprise ซื้อก่อน framework**. ตั้งแต่กลางปี 2026 pattern ที่ repeat คือ **CISO + IT ซื้อ gateway/identity layer ก่อน dev team เลือก framework**. Mintive, [Rein Security](https://thenextweb.com/news/island-series-f-400m-6-4bn-valuation-ai-agents) (sidecar), Island (browser control) ทั้งหมด sell ไปที่ CISO ไม่ใช่ platform engineer. Thesis เหตุผล: agent framework switch cost ต่ำ (เปลี่ยน CrewAI → LangGraph ภายใน sprint ได้), แต่ **identity + audit trail ย้อนกลับไม่ได้** — ถ้า audit บอกไม่ได้ว่า agent ไหนเรียก tool ไหน, enterprise ไม่ pass compliance (SOC2, ISO 42001). Mintive มี SOC 2 Type II audit แล้ว — ตัว marker ว่า sell เข้า Fortune 1000 ได้

ประเด็นที่สอง — **"agent as employee" คือ framing ที่กำลังชนะ, ไม่ใช่ "agent as tool"**. Mintive ใช้คำว่า **Coworker agent** ที่ "ทำงานใน Slack/Teams, มี long-term memory, มี identity ของตัวเอง". pattern เดียวกับ Microsoft Copilot Cowork (มี.ค. 2026) และ Decagon's AI employee concept — ซึ่ง resembled เหมือน SaaS seat-based pricing ไม่ใช่ API-call pricing. ถ้า pattern นี้ชนะ, pricing model ของ agent category จะ consolidate ไปที่ **$X ต่อ agent/เดือน** คล้าย Salesforce licensing — ซึ่งทำให้ TAM ของ agent คำนวณใหม่ (ไม่ใช่ "replace knowledge worker 100%" แต่ "เพิ่ม seat 20-30% ที่ marginal cost")

ประเด็นที่สาม — **MCP consolidation signal: Mintive ใช้ MCP เป็น protocol หลัก, support Claude + ChatGPT + Copilot + Cursor + internal agent ใน gateway เดียว**. 7 เดือนก่อนตลาดยัง fragment ระหว่าง Anthropic MCP, Google A2A, OpenAI tool-use spec. Mintive bet ว่า **MCP จะชนะ default protocol** ขณะที่ A2A/ACP จะเป็น complementary. การที่ U of Michigan ใช้เป็น "enterprise MCP gateway" ยืนยันว่า **MCP เริ่มมี enterprise reference architecture แยกจาก developer tool** — คือ gateway + policy + audit + routing (ไม่ใช่แค่ "server ที่ Claude Desktop ต่อได้")

## มุม AI Agent Platform

สำหรับ **Builders**: ถ้าสร้าง agent framework หรือ orchestration ตอนนี้, **อย่า build identity layer เอง** — เสียเวลา 6-12 เดือน และ enterprise ไม่ซื้อ identity ที่ไม่มี SOC2/ISO 42001. Integrate กับ Mintive (หรือ Workday, Okta ที่กำลังขยายไปทาง agent identity) ตั้งแต่วันแรก. Pattern design: **agent มี service account ของตัวเอง, ขอ scoped token ผ่าน MCP Gateway, log ทุก tool call พร้อม person+agent+server trace**. ที่สำคัญ: **Mint Guard pattern** (prompt injection + secret screening ที่ runtime) ควรเป็น default ใน dev loop ไม่ใช่ bolt-on หลัง deploy

สำหรับ **Users / Business**: ถ้ากำลัง deploy agent มากกว่า 2-3 ตัวใน enterprise, **ซื้อ gateway ก่อน scale**. Cost ของ identity layer ($0.5-2M ต่อปี enterprise license) ถูกกว่า cost ของ breach ครั้งเดียว (average breach cost $4.9M, agentic breach ที่ exfiltrate ผ่าน tool call จะมากกว่า). Modern Treasury benchmark (30 นาที/4 ชั่วโมง saving) คือ reference ที่ใช้ build business case ได้ — ถ้าทีมมี >50 case/วัน และ >30% ซับซ้อน, ROI คุ้มใน <6 เดือน. โปรด note: **Mintive ยัง $11M total raise** — ถ้า deploy critical ควรเตรียม exit plan (vendor lock-in risk) และ ask Mintive ว่า architecture support self-host หรือไม่

สำหรับ **Ecosystem**: ไทย corporate ที่ deploy agent (ธนาคาร, insurance, hospital) มี 2 ทางเลือก — (ก) รอ global vendor (Mintive, Workday agent, Microsoft Entra agent) เข้ามา, หรือ (ข) build gateway บน open-source stack (Portkey, LiteLLM, Pangea agent guard) + ต่อกับ IAM ที่มีอยู่ (SCB on-prem, True ADFS). ทางเลือก (ข) ถูกกว่า แต่ต้องมี platform team ≥3 คนที่ full-time dedicate — น้อยกว่านี้ไม่คุ้ม. Opportunity สำหรับ Thai SI (G-Able, True Digital Group, Ascend): package agent gateway + IAM integration + Mint Guard-equivalent + compliance mapping (PDPA, BoT RL19) เป็น managed service

## Sources
- [Mintive Tops 2.5 Million Daily Agent Calls (National Law Review press release)](https://natlawreview.com/press-releases/mintive-tops-25-million-daily-agent-calls-enterprises-make-ai-agent-identity)
- [Mintive raises $7M for AI agent identity (TechCrunch coverage via AI Agents Directory)](https://aiagentsdirectory.com/news)
- [Mintive product page — MCP Gateway + LLM Gateway + Mint Guard](https://www.mintive.com/)

---

## Audio script
Mintive สตาร์ตอัพด้าน agent identity ประกาศวันที่ 30 ตุลาคม 2026 ว่าแพลตฟอร์ม handle 2.5 ล้าน agent call ต่อวัน รวม 200 ล้านกว่า call ใน 7 เดือน และมี 50 กว่า paying enterprise customer พร้อมเพิ่งปิด round 7 ล้านดอลลาร์ที่นำโดย Cowboy Ventures รวมสะสม 11 ล้านดอลลาร์. Thesis ของ Mintive คือ agent ต้องมี identity ของตัวเองเหมือน employee มี MCP Gateway คุม tool access มี LLM Gateway คุม model routing และ Mint Guard ตรวจ prompt injection กับ secret leak ทุก call ย้อน trace ได้ถึง person agent server model. Customer เปิดเผย Ro Modern Treasury University of Michigan Coursera และ Apax. Modern Treasury รายงานว่า agent ที่ build บน Mintive ตัดเวลา case ง่าย 30 นาที case ซับซ้อน 4 ชั่วโมง ถ้าทีม support 20 คน handle 100 case ต่อวัน saving ประมาณ 80 man-hour ต่อวัน. ประเด็นต่อจากนี้มีสาม หนึ่ง agent identity กำลังเป็น primitive ที่ enterprise ซื้อก่อน framework pattern ที่ repeat คือ CISO กับ IT ซื้อ gateway ก่อน dev team เลือก framework เพราะ framework switch cost ต่ำ แต่ identity กับ audit trail ย้อนกลับไม่ได้ ถ้า audit บอกไม่ได้ว่า agent ไหนเรียก tool ไหน enterprise ไม่ผ่าน SOC2 กับ ISO 42001. สอง framing agent as employee กำลังชนะ agent as tool pricing จะ consolidate ไปที่ dollar ต่อ agent ต่อเดือนคล้าย Salesforce licensing ซึ่งทำให้ TAM คำนวณใหม่ไม่ใช่ replace worker 100% แต่เพิ่ม seat 20-30% ที่ marginal cost. สาม Mintive bet ว่า MCP จะชนะ default protocol รองรับ Claude ChatGPT Copilot Cursor ใน gateway เดียว U of Michigan ใช้เป็น enterprise MCP gateway ยืนยันว่า MCP เริ่มมี enterprise reference architecture แยกจาก developer tool. สำหรับ builder อย่า build identity layer เอง integrate กับ Mintive หรือ Workday Okta agent identity ตั้งแต่วันแรก Mint Guard pattern ควรเป็น default ใน dev loop. สำหรับ enterprise ที่ deploy agent มากกว่า 2-3 ตัวซื้อ gateway ก่อน scale cost 0.5-2 ล้านดอลลาร์ต่อปี ถูกกว่า breach ครั้งเดียว 4.9 ล้านดอลลาร์. สำหรับ ไทย ธนาคาร insurance hospital มีสองทางเลือก รอ global vendor หรือ build บน Portkey LiteLLM Pangea บวก IAM ที่มีอยู่ ทางหลังถูกกว่าแต่ต้องมี platform team 3 คน full-time opportunity สำหรับ Thai SI คือ package gateway บวก IAM บวก compliance PDPA BoT RL19 เป็น managed service
