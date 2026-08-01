---
date: 2026-08-02
slug: upwind-ai-context-scanner-ai-dr-agent-runtime-ga
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric composition. Left half: a stylized "AI AGENT" cube being
  inspected by a large magnifying-glass silhouette labeled "CONTEXT SCANNER",
  with three arrows pointing into the cube: "INSTRUCTIONS", "TOOLS",
  "CONNECTIONS". Right half: same agent cube in production runtime with a
  green baseline heartbeat line and a red drift spike labeled "DRIFT DETECTED
  — AI DR". Between the two halves a bold headline "SCAN BEFORE. WATCH
  DURING." plus a banner "AI DR NOW GA". Deep navy + electric-teal palette,
  chiaroscuro editorial style, 1:1 aspect, no real human faces, text must
  render sharply at 200px thumbnail.
image: images/26-08-02-0610-04-upwind-ai-context-scanner-ai-dr-agent-runtime-ga.png
---

# Upwind Context Scanner + AI DR GA — agent security แยกเป็น "before act" กับ "after act" อย่างเป็นทางการ

## TL;DR
- **30 ก.ค.** — Upwind Security ปล่อย **AI Agent Context Scanner** (inspect instructions/tools/connections **ก่อน** agent take action) + moved **AI Detection & Response (AI DR) to general availability**
- Scanner ไล่ทุกที่ที่ instruction/tool อาศัย — endpoint, cloud, managed AI provider — cross-reference กับ Upwind runtime platform ให้ **rank ตาม actual runtime risk** ไม่ใช่ standalone alert queue
- AI DR baseline agent behavior (tool call, API touch, data store access) แล้ว flag drift real-time — โมเดล runtime security แบบ EDR แต่สำหรับ agent
- Signal: **agent security กำลัง codify เป็น 2 stage discipline** (context scan → runtime detect) ไม่ต่างจาก DevSecOps split ที่ shift-left + shift-right เมื่อ 10 ปีก่อน

## เกิดอะไรขึ้น

30 กรกฎาคม Upwind Security ที่ Yotam Segev + Amiram Shachar co-found (ตั้งแต่ 2022, ราคา Series A $50M จาก Craft Ventures + Cyberstarts, valuation ~$900M ในไตรมาสหลัง) ปล่อยของใหม่คู่กัน — **AI Agent Context Scanner** เข้า public availability + **AI Detection & Response (AI DR) เข้า GA**. ก่อนวันนี้ Upwind มีชื่อในกลุ่ม CNAPP (cloud-native application protection) เดียวกับ Wiz, Orca, Sysdig; ตอนนี้เริ่ม pivot เข้าสู่ **agent-specific security** เต็มตัว. SiliconANGLE exclusive อธิบายว่า Scanner "inspects the instructions, tools and connections feeding artificial intelligence agents before those agents act on them"

Scanner เดินไล่ **สาม input layer ของ agent**: (1) **instructions** — system prompt + agent policy + injection surface, (2) **tools** — MCP server, API, function call registry, code execution sandbox, (3) **connections** — data source (RAG index, vector DB, warehouse), identity boundary (service account, OAuth scope), network path. ค้นหา malicious / vulnerable / ambiguous ใน 3 layer พร้อมกัน; findings cross-reference กับ Upwind's existing runtime platform (workload, cloud config, identity) เพื่อ **rank ตาม runtime blast radius จริง** — CVE ใน MCP server ที่ agent ใน production ยิงจริง 10K ครั้ง/วันจะ rank ก่อน CVE ที่อยู่ใน tool ที่ dev สร้างไว้แต่ไม่มีใครใช้

**AI DR** ทำหน้าที่ตรงข้ามในเวลา — **during / after action**. AI DR baseline "how each agent behaves normally" — จับ pattern ว่า agent A ปกติ call tool X, Y, Z ในสัดส่วน 60/30/10, touch data store D1 + D2 ไม่เกิน 300 QPS, session length ~4 turn เฉลี่ย. Drift = flag real-time (agent เริ่ม call tool Z ที่ 90%, หรือ touch data store D5 ที่ไม่เคยแตะ, หรือ session ยาว 40 turn). Model เหมือน EDR (endpoint detection & response) — behavioral baseline + anomaly + auto-quarantine — แต่ scope ที่ agent runtime แทน endpoint OS

Upwind claim จาก 6-week early access ที่ 12 F500 (unnamed, แต่ Craft Ventures portfolio ปล่อย hint = Salesforce internal agent, Notion internal ops, Wayfair supply chain agent) — **detect prompt-injection attempt ที่หลุด scanner ไป 3.7% ของ attack surface**, mean-time-to-quarantine 47 วินาที (เทียบ manual SOC review 4-7 hour). Pricing แจ้งวันประกาศ — **$8 per agent per month for Context Scanner, $12 per agent per month for AI DR** (bundle $18); minimum 100 agent — Upwind target enterprise ที่ deploy agent จำนวนมาก, ไม่ใช่ startup

## ทำไมสำคัญ

**Agent security เริ่ม codify เป็น 2 stage discipline — สคาน context ก่อน act, detect drift ระหว่าง act**. เทียบกับ DevSecOps 10 ปีก่อน — เดิม security = periodic pen test; แล้ว shift-left (SAST/DAST/SCA ก่อน deploy) + shift-right (runtime EDR/CDR/CWPP) กลายเป็น 2 pillar. Agent security กำลังตาม pattern เดียวกัน — **shift-left = context scanning (Upwind Scanner, Prompt Security, Zenity Analyze), shift-right = runtime detection (Upwind AI DR, CalypsoAI, Lakera Runtime)**. Category เข้ารูปเข้ารอย = enterprise buyer มี framework ตัดสินใจ, RFP มี template. เดือน ก.ย.-พ.ย. คาดว่า Gartner จะ codify ใน "AI TRiSM" (AI Trust, Risk & Security Management) Magic Quadrant ฉบับใหม่

**Upwind + agent security = ตัวอย่าง CNAPP-to-agent migration pattern**. Wiz ($32B Google acquisition ตกลงกันตุลาคม 2025), Orca ($1.8B Series E เมษายน 2026), Sysdig, และ Upwind ทั้งหมดเริ่ม career จาก cloud posture / workload protection — วันนี้ทุกคนกำลัง **repackage core scan engine + runtime baseline เป็น agent security product** เพราะ agent = workload ประเภทใหม่ที่ CISO ต้อง audit. Wiz Runtime AI (พ.ค.), Orca AI Security (มิ.ย.), Sysdig Sysdig Agent Sentinel (ก.ค.), Upwind AI DR (วันนี้). Enterprise ที่มี CNAPP vendor อยู่แล้ว → default choice = ต่อยอด agent product ของ vendor นั้น. Startup pure-play agent security (Prompt Security, Zenity, Lakera, Robust Intelligence) ต้อง **ดัน differentiator ที่ CNAPP incumbent ไม่มี** — ส่วนใหญ่คือ prompt-injection depth + red-team playbook library

**pricing per-agent = enterprise เริ่มต้อง count agent เหมือน count endpoint**. เดิม CISO นับ endpoint (per-seat), server (per-CPU), user (per-identity) — ตอนนี้เพิ่ม **agent = new asset class** ที่ต้อง inventory + license security. Upwind $18/agent/month = ใน scale 10K agent = $2.16M/year — เข้า enterprise budget line ใหม่. F500 average คาด deploy 5K-50K agent ใน 2027 (Gartner forecast); category size = **$5-10B ARR ใน 3 ปี** — ใหญ่กว่า email security เดิม

## มุม AI Agent Platform

**สำหรับ builders:** ถ้ากำลังสร้าง agent framework — **expose agent runtime metadata standard** (tool call ledger, session graph, data store touch record) ที่ security vendor อย่าง Upwind consume ได้. โอกาส: contribute เข้า **OpenTelemetry SIG-Agent** ที่กำลัง draft schema สำหรับ agent trace + audit — vendor ทุกเจ้าจะ align ที่ standard นี้. ถ้ากำลังสร้าง MCP server — เพิ่ม **capability manifest** ที่ scanner อ่านได้ (declare tool intent, data sensitivity level, permission boundary) เพื่อลด false-positive จาก scanner

**สำหรับ users/business:** CISO + Head of AI ต้อง **audit ตอนนี้: มี agent inventory ไหม? ถ้าไม่มี → เริ่ม**. Question ที่ต้องตอบใน 30 วัน — (1) กี่ agent ที่ deploy in production? (ส่วนใหญ่ตอบไม่ได้), (2) แต่ละ agent access data store อะไร, tool อะไร? (ต้องมี asset registry), (3) ใครเป็น owner? (compliance requirement). Upwind + คู่แข่ง = tool ทำ inventory + posture ให้ทันที. Thai bank / SET50 ที่ deploy agent workload บน AWS Bedrock + Azure AI Foundry แล้ว = **BOT + BOI จะเริ่มถาม audit trail ปีหน้า**; agent security tooling = table stakes ก่อน examiner มา

**สำหรับ ecosystem:** losers = CNAPP vendor ที่ยังไม่ launch agent product (Aqua Security, Palo Alto Prisma Cloud lite — เป็น full stack แต่ agent story ยัง marketing) → เสี่ยง lose seat ใน renewal 2027. Winners: (1) Upwind + Wiz + Orca ที่ integrate ทั้ง cloud + agent, (2) **pure-play agent security ที่หา niche vertical** (Robust Intelligence สำหรับ regulated FinServ, Lakera สำหรับ EU AI Act compliance), (3) **MCP registry + tool marketplace** (Anthropic MCP Directory, Cloudflare Workers AI Registry) ที่ inject scanner metadata ให้ผู้ใช้เห็น posture score ก่อน install. Enabridge angle: ถ้าคุยลูกค้าไทยเรื่อง production agent — เพิ่ม "agent security posture" เข้า architecture recommendation, ไม่ใช่ afterthought

## Sources
- [Exclusive: Upwind adds context scanning for AI agents as AI DR hits general availability — SiliconANGLE](https://siliconangle.com/2026/07/30/exclusive-upwind-adds-context-scanning-ai-agents-ai-dr-hits-general-availability/)
- [Upwind Expands AI Agent Protection With Context Scanning and Runtime Detection — HackerNoon](https://hackernoon.com/upwind-expands-ai-agent-protection-with-context-scanning-and-runtime-detection)
- [Amplify your security team with AI agents — Upwind product page](https://www.upwind.io/agentic-security)
- [Announcing Upwind AI Sensor for Endpoints — Upwind blog](https://www.upwind.io/feed/upwind-ai-sensor-for-endpoint)

---

## Audio script
30 กรกฎาคม Upwind Security ปล่อยของใหม่คู่กัน. AI Agent Context Scanner ที่ inspect instructions, tools, connections ของ agent ก่อน take action. บวก AI Detection & Response หรือ AI DR ที่ moved เข้า general availability. โมเดลเหมือน EDR สำหรับ endpoint — baseline agent behavior แล้ว flag drift real-time.

ที่สำคัญกว่า product — pattern industry กำลัง codify. Agent security แยกเป็น 2 stage. Stage 1 shift-left — สคาน context ก่อน agent act. Stage 2 shift-right — detect drift ระหว่าง act. เทียบ DevSecOps เมื่อ 10 ปีก่อนที่แยก SAST + DAST + runtime EDR. Gartner คาดจะ codify ใน AI TRiSM Magic Quadrant ปีนี้.

Pricing per-agent $18 ต่อเดือน = enterprise ต้องเริ่ม count agent เหมือน count endpoint. F500 average คาด deploy 5,000 ถึง 50,000 agent ใน 2027. Category size 5 ถึง 10 พันล้าน ARR ใน 3 ปี — ใหญ่กว่า email security เดิม. สำหรับ Thai bank ที่ deploy agent workload บน Bedrock กับ Azure AI Foundry แล้ว — BOT กับ BOI จะเริ่มถาม audit trail ปีหน้า. Agent security tooling คือ table stakes ก่อน examiner มา. Enabridge angle — เพิ่ม agent security posture เข้า architecture recommendation, ไม่ใช่ afterthought.
