---
date: 2026-07-23
slug: openai-presence-enterprise-voice-agent-platform-fde-codex
topic: agent-platform-trend
reading_time_min: 4
sources: 5
image_prompt: |
  An editorial isometric illustration on a warm off-white background: a
  glass-walled enterprise command center titled "PRESENCE" with three
  concentric rings labeled "POLICY", "GUARDRAILS", "ESCALATION"; inside the
  center ring a chat bubble and a voice waveform sit side by side. Two
  hard-hat "OpenAI FDE" toolboxes flank the doors; above hovers a Codex
  loop icon with the counter "-15 pts HANDOFFS · 10 DAYS". Sharp editorial
  typography, high contrast, 1:1 aspect, no real human faces.
image: images/26-07-23-0610-01-openai-presence-enterprise-voice-agent-platform-fde-codex.png
---

# OpenAI เปิดตัว "Presence" — เอา Forward Deployed Engineers + Codex feedback loop ยัดเป็น first-class enterprise agent platform

## TL;DR
- 22 ก.ค. OpenAI เปิดตัว Presence — enterprise platform สำหรับ deploy realtime voice + chat agent, bundling policy, permission, escalation, simulation, guardrail, และ Codex-powered continuous improvement เข้าเป็นชิ้นเดียว
- **ไม่ใช่ self-service** — ขายผ่าน limited GA ที่มี OpenAI Forward Deployed Engineers (FDEs) + global systems integrators เข้าไป deploy ให้ (มาจาก OpenAI Deployment Company subsidiary ที่ตั้งพฤษภาคม 2026 ด้วย $4B backing, $10B valuation)
- Codex plugin ที่รีวิว production interaction, propose behavior update — early data: **ลด human handoff 15 percentage point ใน 10 วัน** หลัง deploy. Simulation batch ทดสอบ policy change (เช่น "revised annual refund policy") ก่อน push จริง
- Signal: OpenAI ประกาศชนกับ Sierra, Cognigy, Parloa, Salesforce Agentforce, Google Presence-of-Gemini-Enterprise แบบตรง — วิธีชนะคือ "deploy สำเร็จ" ไม่ใช่ "SDK ดีที่สุด"

## เกิดอะไรขึ้น
วันที่ 22 กรกฎาคม OpenAI เปิดตัว Presence ผ่าน limited general availability program — enterprise product ตัวแรกที่ตรงหน้าตรงตัวว่าเป็น "platform for deploying and managing AI agents across customer-facing and internal business workflows". VentureBeat, MLQ News, และ DataWorldBank รายงานตรงกันว่า Presence bundle 6 ชั้นเข้าเป็น deployment framework เดียว — company policies + standard operating procedures, permission controls ที่จำกัด data/system access, escalation rules ที่ route conversation ไปหา human เมื่อ trigger, pre-deployment simulation batches ที่ทดสอบ agent กับ common request + edge case + high-risk scenario, guardrails, และ Codex-powered feedback loop.

โครงสร้าง distribution ต่างจาก OpenAI product เดิมชัด — Presence **ไม่ available บน self-service**, ขายผ่าน OpenAI Forward Deployed Engineers (FDEs) + select global systems integrators (Accenture, Deloitte, McKinsey QuantumBlack, TCS, Cognizant ที่มี early access). Model นี้ต่อยอดจาก OpenAI Deployment Company subsidiary ที่ตั้งพฤษภาคม 2026 ด้วย backing $4B ที่ valuation $10B — dedicated subsidiary ที่ทำหน้าที่ "Palantir-style FDE-led deployment" สำหรับ enterprise account อย่างเดียว. Sam Altman เคยพูดกลาง Dreamforce 2025 ว่า "SDK ที่ดีไม่พอ — ต้องมีคนที่ไปนั่งใน conference room ของ Fortune 500 แล้วเปลี่ยน SOP ให้"; Presence คือ product ที่ผูก philosophy นี้เข้าเป็น SKU.

Codex feedback loop เป็นชิ้นที่น่าสังเกตที่สุด — ใช้ Codex agent (OpenAI coding agent ตัวเดียวกับที่ deploy ใน Cursor + Windsurf + GitHub Copilot) มาเป็น operational analyst: อ่าน production interaction ทุกวัน, identify weakness (agent ตอบพลาด, escalate ช้า, guardrail block false positive), propose behavioral improvement เป็น policy diff, ให้ staff review + test + approve ก่อน push. OpenAI เผยตัวเลข early: **customer หนึ่งราย ลด human handoff ลง 15 percentage point ภายใน 10 วัน** หลัง Presence go-live — เพราะ Codex identify ว่า agent ไม่รู้จัก 12 refund reason ใหม่ที่เพิ่งเปลี่ยน policy สัปดาห์ก่อน, generate policy diff, staff approve, agent handle ได้ใน 24 ชม. ตัวเลขนี้ยังไม่ third-party verify แต่ pattern ถูก — feedback loop ที่ automate การ maintain agent behavior เป็น pain point อันดับหนึ่งของ enterprise ที่ deploy agent เกิน 3 เดือน.

Use case target ที่ OpenAI ระบุ: customer support, outbound sales development, procurement, IT services, HR functions. Agent สามารถ verify identity, access account data, apply company policy, execute approved action รวมถึง billing resolution + refund — เห็นได้ว่าเลียนแบบ Sierra playbook ที่ Bret Taylor build มา 2 ปี (Sierra ARR $200M ณ ก.ค. 2026). แต่ OpenAI มี edge สองอย่าง: (1) frontier model tier ที่ควบคุมเอง — Realtime API + GPT-5.6 Terra + Sol พร้อม voice model ล่าสุด, (2) simulation batch ที่ต่อกับ policy diff โดยตรง — Sierra + Cognigy + Parloa ยังใช้ manual test script.

## ทำไมสำคัญ
Pattern ที่กำลังจะ dominant ในไตรมาสหน้า — **enterprise agent platform ไม่ใช่ product play, มันคือ deployment services play**. AWS Bedrock AgentCore, Google Gemini Enterprise Agent Platform, Microsoft Copilot Studio ทุกตัวมี SDK + guardrail + evaluator เหมือน Presence — สิ่งที่ต่างคือใครไปนั่งกับ CIO ธนาคาร Fortune 100 แล้วเปลี่ยน SOP ให้ได้จริง. Sierra ชนะเพราะ Bret Taylor นำทีม deploy ระดับ VP; Cognigy ชนะยุโรปเพราะ SE team ใหญ่และเข้าใจ compliance ยุโรป; ตอนนี้ OpenAI ตั้ง Deployment Company + FDE program เพื่อไม่ให้ enterprise account ตกไป Sierra/Cognigy/Salesforce Agentforce. HCLTech report เมื่อ 21 ก.ค. (ดู brief #2) รายงานว่า 90% enterprise deploy agent แต่เพียง 18% เห็น revenue impact — ช่องว่างนี้คือ TAM ของ Presence + Sierra + Cognigy + Palantir AIP.

Timing ตรงกับ MCP 2026-07-28 GA (ชิป 28 ก.ค. — จันทร์หน้า) — stateless MCP + Extensions framework + MCP Apps จะทำให้ enterprise สามารถ integrate agent เข้ากับ internal system ผ่าน HTTP load balancer ปกติได้; Presence กับ Sierra จะ leverage สิ่งนี้เป็น connector layer แทน bespoke integration ที่ทำมือ. Presence จะ ship MCP Apps support "ในไตรมาสหน้า" ตามข่าวลือใน MLQ News. คู่กันสองเรื่องนี้ทำให้ AWS Bedrock AgentCore + Microsoft Copilot Studio ต้องเร่ง roadmap MCP integration + FDE program คู่กัน — ไตรมาส 3 คือ deployment services war ไม่ใช่ SDK war.

น่าสังเกตอีกอย่าง — Codex ในบทบาท "operational analyst ของ production agent" เป็น loop ที่ recursive ใน spirit: **agent monitor agent, agent improve agent**. Anthropic Claude Code Agent SDK มี capability คล้ายกัน (Claude review Claude output ใน production), Google Vertex Agent Builder มี Gemini reviewer. แต่ OpenAI packaging ที่ SKU level ก่อน — และ 15-point handoff reduction ใน 10 วันเป็นตัวเลขที่ CFO อ่านได้.

## มุม AI Agent Platform
สำหรับ **builders** ที่กำลังสร้าง framework / agent platform — Presence ยืนยันสิ่งที่ Yoh พูดในบทวิเคราะห์เดือนพฤษภาคม: SDK อย่างเดียวไม่ชนะ, deployment services + operational tooling + FDE program คือ moat. ถ้าทีมของคุณสร้าง agent framework แต่ไม่มี "deploy สำเร็จ" story + "6-week concept-to-production" playbook แบบ Michaels + Gemini Enterprise (ดู brief #4), จะเสียเปรียบใน RFP ไตรมาสหน้า. Codex-in-the-loop pattern คือสิ่งที่ open-source framework (LangGraph, CrewAI, Autogen, LlamaIndex Agents) ควร copy ทันที — feedback loop ที่ auto-generate policy diff + require human approval คือ table stakes.

สำหรับ **users / business** — ถ้าคุณเป็น CTO/CIO ที่ประเมิน voice agent + chat agent platform อยู่, Presence เพิ่มตัวเลือกที่มี OpenAI FDE + Codex loop มาให้ (แม้จะ limited GA ตอนนี้). เทียบกับ Sierra ($200M ARR, focus voice), Cognigy (Europe, compliance), Parloa (contact center specialist), Amazon Connect + Bedrock AgentCore (AWS-native), Google Gemini Enterprise for Customer Experience (Michaels playbook). ประเด็นคือ: **อย่าซื้อ SDK, ซื้อ deployment**. request FDE hour commitment, request Codex-loop analog, request simulation batch feature ก่อน commit. สำหรับ **ecosystem** — Sierra + Cognigy + Parloa จะต้องเพิ่ม FDE headcount หรือ partner กับ SI (Accenture/Deloitte/Capgemini) เพื่อไม่ให้ OpenAI Presence กินตลาด mid-market. Independent contact center platform (Genesys, Five9, NICE) จะโดนกดดันมากที่สุด — OpenAI Presence + Amazon Connect + Google Contact Center AI จะ vertical integrate stack เต็ม.

## Sources
- [OpenAI unveils Presence, a new platform that lets enterprises launch and manage realtime voice agents and chatbots — VentureBeat (22 Jul)](https://venturebeat.com/orchestration/openai-unveils-presence-a-new-platform-that-lets-enterprises-launch-and-manage-realtime-voice-agents-and-chatbots)
- [OpenAI Launches Presence, an Enterprise AI Agent Platform for Voice and Chat Workflows — MLQ News (22 Jul)](https://mlq.ai/news/openai-launches-presence-an-enterprise-ai-agent-platform-for-voice-and-chat-workflows/)
- [OpenAI unveils Presence — DataWorldBank mirror (22 Jul)](https://www.dataworldbank.net/2026/07/22/openai-unveils-presence-a-new-platform-that-lets-enterprises-launch-and-manage-realtime-voice-agents-and-chatbots/)
- [OpenAI Release Notes — July 2026 — Releasebot](https://releasebot.io/updates/openai)
- [OpenAI Introduces Realtime Voice AI for Translation, Transcription, and Task Handling — eWeek](https://www.eweek.com/news/openai-gpt-realtime-2-voice-agents/)

---

## Audio script
วันนี้ 22 กรกฎาคม OpenAI เปิดตัว Presence ครับ enterprise platform สำหรับ deploy realtime voice agent กับ chat agent ที่ bundle policy permission escalation simulation guardrail และ Codex feedback loop เข้ามาเป็นชิ้นเดียว จุดที่น่าสนใจที่สุดคือมันไม่ใช่ self-service — OpenAI ขายผ่าน Forward Deployed Engineers กับ global systems integrator ที่ Accenture Deloitte McKinsey QuantumBlack เข้ามา deploy ให้ pattern เดียวกับ Palantir Model นี้ต่อยอดจาก OpenAI Deployment Company ที่ตั้งเดือนพฤษภาคมด้วย backing 4 พันล้านดอลลาร์ Presence มี Codex plugin ที่รีวิว production interaction ทุกวัน identify weakness propose policy diff แล้วให้ staff test approve ก่อน push OpenAI เผยตัวเลข early ว่า customer หนึ่งราย ลด human handoff ได้ 15 percentage point ภายใน 10 วันหลัง go-live เพราะ Codex ค้นเจอว่า agent ไม่รู้จัก refund reason 12 อันใหม่ที่เพิ่งเปลี่ยน policy สัปดาห์ก่อน ทำไมสำคัญครับ เพราะข่าวนี้ยืนยันว่า enterprise agent platform ยุค 2026 ไม่ใช่ product play มันคือ deployment services play AWS Bedrock AgentCore Google Gemini Enterprise Microsoft Copilot Studio ทุกตัวมี SDK guardrail evaluator เหมือนกัน สิ่งที่ต่างคือใครไปนั่งกับ CIO ธนาคาร Fortune 100 แล้วเปลี่ยน SOP ได้จริง Sierra ชนะเพราะ Bret Taylor นำทีม deploy ระดับ VP Cognigy ชนะยุโรปเพราะ SE team ใหญ่ ตอนนี้ OpenAI สร้าง Deployment Company + FDE program เพื่อไม่ให้ enterprise account ตกไปที่คู่แข่ง Timing ตรงกับ MCP 2026-07-28 GA ที่จะ ship จันทร์หน้า stateless MCP + Extensions framework จะทำให้ Presence กับ Sierra ใช้ MCP เป็น connector layer แทน bespoke integration สำหรับ builder ที่ทำ framework — SDK อย่างเดียวไม่ชนะ deployment + FDE program + operational tooling คือ moat Codex-in-the-loop pattern ที่ auto propose policy diff + require human approval ควร copy ทันที LangGraph CrewAI Autogen ควร ship feature นี้ในเดือนนี้ สำหรับ CTO CIO ที่ evaluate voice agent platform อยู่ อย่าซื้อ SDK ซื้อ deployment ขอ FDE hour commitment ขอ Codex-loop analog ขอ simulation batch feature ก่อน commit ครับ
