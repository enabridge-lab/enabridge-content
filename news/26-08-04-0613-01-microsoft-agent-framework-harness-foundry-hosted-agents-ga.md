---
date: 2026-08-04
slug: microsoft-agent-framework-harness-foundry-hosted-agents-ga
topic: agentic-ai
reading_time_min: 5
sources: 7
image_prompt: |
  Editorial isometric illustration of three cloud towers standing side by side
  on a marble podium — each labeled "AWS AGENTCORE", "GOOGLE MANAGED AGENTS",
  and "MSFT FOUNDRY HOSTED AGENTS" — with a fresh green ribbon draped across
  the Microsoft tower reading "GA — AUG 2026". At the base a large glass floor
  shows a cross-section of an "AGENT HARNESS" binary: 98% opaque scaffolding
  labels ("TOOL CALLS / MEMORY / TELEMETRY / APPROVALS / OTEL"), and a tiny
  1.6% glowing core labeled "MODEL DECISION". A stat banner reads
  "3 HYPERSCALER RUNTIMES / ONE HARNESS PATTERN". Deep navy + electric cyan
  palette, chiaroscuro editorial style, 1:1 aspect, no real human faces,
  text sharp at 200px thumbnail.
image: images/26-08-04-0613-01-microsoft-agent-framework-harness-foundry-hosted-agents-ga.png
---

# Microsoft Foundry Hosted Agents + Agent Framework Harness GA — hyperscaler agent runtime กลายเป็น "commodity 3 ค่าย" ในสัปดาห์เดียว

## TL;DR
- **3 ส.ค.** — InfoQ ยืนยัน **Microsoft Agent Framework Harness + Foundry Hosted Agents ขึ้น GA** — Microsoft = hyperscaler ตัวที่ 3 ที่มี production agent runtime หลัง AWS AgentCore (ต.ค. 2025) + Google Managed Agents (28 ก.ค. 2026). Runtime layer ปิด 3 ค่ายภายในสัปดาห์เดียว
- **Harness = single binary** รันเหมือนกันตั้งแต่ laptop → container → Foundry Hosted Agents managed compute (consumption-based billing). Built-in: function invocation, per-call history, context compaction, tool approval, OpenTelemetry, web search, todo list plan/execute mode, file memory, skills. Optional (พร้อม warning): shell tooling, file access, background sub-agents, auto-looping
- **GitHub Copilot SDK + Claude Agent SDK connectors** stable — coding-agent traffic ไหลเข้า OpenTelemetry trace + Foundry dashboard เดียวกันกับ agent อื่น = fleet governance ตัวจริงตัวแรก. Semantic Kernel + AutoGen เข้า maintenance mode
- **Reveal ที่เปลี่ยน framing ทั้งหมด**: MBZUAI analysis ของ **Claude Code v2.1.88** พบ **98.4% ของ codebase = harness infrastructure + permission + context** เหลือ **1.6% เป็น AI decision logic**. คำ Wes Steyn (MSFT principal engineer): "*A model on its own can only generate text*" — **harness คือ product ตัวจริง ไม่ใช่ model**

## เกิดอะไรขึ้น

วันที่ 3 สิงหาคม InfoQ ปล่อยรายงานยืนยันว่า **Microsoft Agent Framework Harness + Foundry Hosted Agents ขึ้น general availability** — ปิดขั้นตอนสุดท้ายของสิ่งที่ Microsoft ประกาศไว้ที่ Build 2026 (มิ.ย.) และเริ่มด้วย v1.0 framework GA เมื่อ 2 เมษายน 2026. Foundry Hosted Agents คือ managed compute ที่รัน harness binary บน consumption-based billing (คิดตาม request + token + tool call แทน always-on VM) — เข้าคู่กับ AWS AgentCore (GA ต.ค. 2025 + Gateway ประกาศ MCP 2026-07-28 native 29 ก.ค.) + Google Gemini Managed Agents (major update 28 ก.ค., มี free tier). **สามค่ายมี production agent runtime พร้อมกันภายในสัปดาห์เดียว** — สิ่งที่ Gartner คาดว่าจะเกิดปลายปี เกิดใน 7 วัน.

Wes Steyn, Microsoft principal software engineer, สรุปกรอบคิดของ product ในประโยคเดียว: "*A model on its own can only generate text.*" Harness = layer ที่แปลง text-generator ให้กลายเป็น agent — wraps model call, provides tool-invocation loop, persists history, compact context, approve/reject action ก่อน execute, emit OpenTelemetry span ทุก step. Built-in features ที่ enable-by-default: function invocation, multi-step task execution, per-call history persistence + context compaction, tool approval, OTel instrumentation, web search, todo list ใน plan/execute mode, file memory, skills. Features ที่ต้อง opt-in และมี explicit warning: shell tooling, file access, background sub-agents, automatic looping — Microsoft ระวังเรื่อง blast radius ของ autonomous agent ตั้งแต่ default

Extension สำคัญที่ ship พร้อม GA คือ **GitHub Copilot SDK connector + Claude Agent SDK connector** — เป็น bridge ที่ทำให้ coding agent (VS Code Copilot, Claude Code, third-party wrapper) inject เข้ามาใน Foundry fleet policy — identity, content safety, observability ทั้งหมด "honor" ตาม fleet policy ที่ platform team set ไว้แล้ว. Coding-agent traffic ไหลเข้า OpenTelemetry trace + Foundry dashboard เดียวกับ agent อื่น ๆ = enterprise ได้ **fleet-wide governance ของ coding agent เป็นครั้งแรก**. Semantic Kernel + AutoGen — เครื่องมือเดิมของ Microsoft — โอนย้ายเข้า maintenance mode. Framework available ใน .NET + Python บน GitHub

Reveal ที่จะเปลี่ยนวิธี framing ตลาดคือ analysis จาก **MBZUAI (Mohamed bin Zayed University of AI)** เรื่อง Claude Code v2.1.88 — vendor ที่ทุกคนอ้างว่าเป็น "AI-first coding tool" — พบว่า **98.4% ของ codebase คือ harness infrastructure + permission + context management** และเหลือเพียง **1.6% ที่เป็น AI decision logic**. เท่ากับพูดว่า **สิ่งที่ทำให้ agent ทำงานได้จริง 98% คือ engineering ธรรมดา ไม่ใช่ frontier model** — model call คือ 1.6% ที่เหลือ

## ทำไมสำคัญ

**Hyperscaler agent runtime กลายเป็น commodity ภายในสัปดาห์เดียว** — AWS + Google + Microsoft มี production runtime พร้อม hosted compute + consumption billing + MCP support + fleet governance ครบทุกค่าย. **Differentiation ไม่ใช่ "มี agent runtime หรือไม่มี" อีกต่อไป** — แต่กลายเป็น: ราคาต่อ agent-second, model catalog, integration กับ existing IAM/observability, และ region availability. Enterprise procurement team ที่เมื่อ 6 เดือนก่อนต้องใช้เวลา 3-6 เดือน pick vendor — วันนี้ทำ RFP 3-column comparison ได้เลย (AWS AgentCore vs Google Managed Agents vs MSFT Foundry Hosted Agents). Pattern ที่เกิดกับ cloud VM ปี 2013-2015, container orchestration ปี 2018-2020, serverless ปี 2020-2022 กำลังเกิดกับ agent runtime ปี 2026 — cycle เร็วขึ้น 3x

**MBZUAI reveal เปลี่ยนวิธี pitch ตลาด** — ถ้า 98.4% ของ "AI product" คือ engineering ธรรมดา framework battle จบไปแล้ว. Model layer = commodity (Claude 4.7, GPT-5.6, Gemini 3.6 Flash ราคาต่างกันหลัก 20-30%), **harness layer = moat จริง**. Microsoft position ตัวเองเข้า core นี้ — Foundry Hosted Agents ไม่ใช่ SDK แต่เป็น "governed platform for running them" (คำใน InfoQ). AWS AgentCore + Google Managed Agents ก็เดินทางเดียวกัน. Startup ที่ pitch "our agent is better because we use Claude 5" กำลังพูดผิด layer — investor ควรถามว่า harness ของคุณให้ observability กี่ level, permission granularity ระดับไหน, context compaction ทำได้กี่ token, tool approval throughput เท่าไร. 6-8 เดือนข้างหน้า vertical agent startup ที่ไม่มี harness moat จะโดน commoditize เพราะ hyperscaler harness ราคาถูกกว่า

**Consumption billing เปลี่ยน economics agent deployment** — Foundry Hosted Agents + AWS AgentCore + Google Managed Agents ทั้งหมด bill per request/token/tool-call แทน always-on VM. **หมายความว่า pilot cost ลดถึงจุดที่ enterprise ทดสอบ 10-20 agent พร้อมกันได้ในงบ 1 agent VM-hosted**. Long-tail use case (weekly report agent, cron-triggered reconciliation, one-off research bot) ที่เมื่อก่อนไม่คุ้ม VM cost — วันนี้ deploy ได้ทันที. Effect ต่อตลาด: workflow automation vendor (Zapier, n8n, Make.com) มีแรงกดดันหนักกว่าเดิม เพราะ enterprise ที่ commit hyperscaler cloud มี hosted agent runtime "ฟรี" (comes with subscription) แล้ว

## มุม AI Agent Platform

**สำหรับ builders:** ถ้ากำลัง build agent framework, coding agent, orchestration tool — **การเลือก stack เปลี่ยนไป**. เมื่อ Microsoft Agent Framework Harness ship บน .NET + Python และ third-party connector (Claude Agent SDK, GitHub Copilot SDK) เป็นทางเลือกแรก — startup ควร **ship connector ให้ทั้ง 3 hyperscaler harness** แทนสร้าง harness เอง เพราะ enterprise buyer จะเลือก vendor ที่ integrate เข้า fleet policy ที่พวกเขามีอยู่แล้ว. Priority: (1) audit codebase — 98.4% harness ratio ของ Claude Code = benchmark ที่ต้อง match/beat, (2) วาง OTel span ให้ครอบ tool call ทุก layer, (3) ship blueprint สำหรับ Foundry Hosted Agents + AgentCore + Managed Agents ให้ marketplace ทั้ง 3. **ถ้าสร้าง harness ตัวเอง** (LangGraph, Mastra, CrewAI) — ต้อง differentiate ด้วย feature ที่ hyperscaler ไม่ทำ (multi-tenant orchestration, cross-cloud, deep verticalization)

**สำหรับ users/business:** Enterprise IT team ที่กำลัง evaluate agent platform ในไตรมาส 3-4 — **ทำ 3-column RFP comparison ทันที** (AWS AgentCore vs Google Managed Agents vs Foundry Hosted Agents). Criterion หลัก: (1) consumption pricing per 1K request + per 1M token + per tool call, (2) fleet governance (identity, content safety, OTel integration ที่ existing SOC ยอมรับ), (3) MCP 2026-07-28 compatibility, (4) region availability (ap-southeast-1 มี AgentCore + Foundry แล้ว, Managed Agents ตามในไตรมาส 4). **Thai enterprise ที่ผูก Azure อยู่แล้ว** (K-Bank, SCB Advanced Analytics, PTT Digital, True Digital, Bangchak) — evaluate Foundry Hosted Agents ก่อนเพราะ integrate เข้า M365 + Entra ID + Purview ที่มีอยู่แล้ว = migration friction ต่ำสุด

**สำหรับ ecosystem:** Winners ชัด — **Anthropic + GitHub** เพราะ Claude Agent SDK + Copilot SDK เป็น first-class connector บน 3 hyperscaler harness (moat = SDK adoption ใน enterprise fleet). **OpenTelemetry vendor** (Datadog, New Relic, Honeycomb, Grafana, Splunk) — agent observability = 1M-agent traffic pattern ต้องใช้ dedicated tooling. **MCP gateway vendor** (Snowflake Cortex AI Gateway, Natoma, Kong upcoming, Cloudflare Agents) — เพราะเป็น neutral routing layer ระหว่าง harness ต่าง ๆ. Losers: **Semantic Kernel + AutoGen** — maintenance mode = death sentence 6-12 เดือน; **Standalone agent framework startup** ที่ไม่มี hyperscaler distribution channel — เสี่ยง lose seat ใน enterprise deal เพราะ RFP comparison เริ่มจาก hyperscaler runtime เป็น default. Enabridge angle: Thai SI ที่ position ตัวเองเป็น "harness-native architect" (deploy agent บน Foundry Hosted Agents + AgentCore + Managed Agents แล้วรับผิดชอบ fleet governance ทั้งหมด) จะกินตลาด Fortune 500 SEA + Thai SET50 ก่อน generic "agent builder" ที่ยัง pitch model layer

## Sources
- [Microsoft Agent Framework Harness and Hosted Agents Reach General Availability — InfoQ](https://www.infoq.com/news/2026/08/agent-framework-harness-ga/)
- [Microsoft Agent Framework at BUILD 2026 — Microsoft Agent Framework DevBlog](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/)
- [Build and run agents at scale with Microsoft Foundry at Build 2026 — Microsoft Foundry Blog](https://devblogs.microsoft.com/foundry/agent-service-build2026/)
- [Introducing the new hosted agents in Foundry Agent Service — Microsoft Foundry Blog](https://devblogs.microsoft.com/foundry/introducing-the-new-hosted-agents-in-foundry-agent-service-secure-scalable-compute-built-for-agents/)
- [The Microsoft Agent Framework Harness is now released — Microsoft Agent Framework DevBlog](https://devblogs.microsoft.com/agent-framework/the-microsoft-agent-framework-harness-is-now-released/)
- [Microsoft Foundry Adds Runtime, Tooling, and Governance for Production Agents — InfoQ](https://www.infoq.com/news/2026/06/microsoft-foundry-agents/)
- [Meet your agent harness and claw — Microsoft Agent Framework DevBlog](https://devblogs.microsoft.com/agent-framework/meet-your-agent-harness-and-claw/)

---

## Audio script
วันที่ 3 สิงหาคม InfoQ ยืนยัน Microsoft Agent Framework Harness และ Foundry Hosted Agents ขึ้น general availability. Microsoft กลายเป็น hyperscaler ตัวที่สาม ที่มี production agent runtime หลัง AWS AgentCore เมื่อตุลาคม 2025 และ Google Managed Agents เมื่อ 28 กรกฎาคม. Runtime layer ปิดสามค่ายภายในสัปดาห์เดียว.

Harness คือ single binary รันเหมือนกันตั้งแต่ laptop container ไปถึง Foundry Hosted Agents managed compute แบบ consumption-based billing. Built-in ครบ ตั้งแต่ function invocation, context compaction, tool approval, OpenTelemetry trace, ไปจนถึง todo list plan-execute mode. Ship พร้อม GitHub Copilot SDK connector และ Claude Agent SDK connector — coding agent traffic ไหลเข้า Foundry dashboard เดียวกันกับ agent อื่น. Semantic Kernel และ AutoGen เข้า maintenance mode.

Reveal ที่เปลี่ยน framing ทั้งตลาด — MBZUAI analysis ของ Claude Code เวอร์ชั่น 2.1.88 พบว่า 98.4% ของ codebase คือ harness infrastructure permission และ context management. เหลือแค่ 1.6% เป็น AI decision logic. Wes Steyn จาก Microsoft พูดตรง ๆ ว่า model บนตัวมันเองสร้างได้แค่ text — harness คือ product ตัวจริง. Signal สำคัญ hyperscaler agent runtime กลายเป็น commodity — differentiation เลื่อนไปที่ราคาต่อ agent second, fleet governance และ region availability. Startup ที่ยัง pitch model layer กำลังพูดผิด layer. สำหรับ Enabridge ทีมที่ position ตัวเองเป็น harness-native architect deploy agent บน Foundry Hosted Agents AgentCore Managed Agents แล้วรับผิดชอบ fleet governance ครบ จะกินตลาด Thai SET50 ก่อน generic agent builder ในไตรมาสถัดไป.
