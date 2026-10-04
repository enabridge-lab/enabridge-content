---
date: 2026-10-05
slug: microsoft-agent-framework-codeact
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a glowing Microsoft Agent Framework
  console stacked on top of a Hyperlight micro-VM capsule. Three vertical
  gauges hover beside it labeled "LATENCY -52.4%", "TOKENS -63.9%", and
  "GA 1.0". A folded roadmap behind reads "AutoGen + Semantic Kernel -> MAF".
  Deep-cobalt and electric-cyan palette, bold text rendering for 200px
  thumbnails, no real human faces, 1:1 aspect, Wired magazine cover style.
image: images/26-10-05-0615-01-microsoft-agent-framework-codeact.png
---

# Microsoft เปิดไพ่ MAF ที่ BUILD 2026 — CodeAct ตัด latency 52%, token 64% ผ่าน Hyperlight micro-VM

## TL;DR
- Microsoft Agent Framework (MAF) ขึ้น **1.0 GA ตั้งแต่ 2 เม.ย. 2026** — รวม AutoGen + Semantic Kernel เป็น platform เดียวทั้ง .NET และ Python; ที่ BUILD 2026 เพิ่ม Agent Harness, CodeAct, Foundry Hosted Agents ให้ครบ production stack
- **CodeAct** ยุบ sequential tool call หลายตา เป็น Python block เดียวรันใน **Hyperlight micro-VM** — บน workload ตัวแทน **latency 27.81s → 13.23s (-52.4%)**, **token 6,890 → 2,489 (-63.9%)**
- **Foundry Hosted Agents** GA ตั้งแต่ ก.ค. 2026 — scale-to-zero, per-session VM isolation, รับทั้ง MAF, LangGraph, Claude Agent SDK, OpenAI Agents SDK, GitHub Copilot SDK, custom code; model-agnostic ตามเจตนา

## เกิดอะไรขึ้น
สัปดาห์นี้ที่ BUILD 2026 Microsoft เปิดไพ่ชุดใหญ่สำหรับทีม Agent Framework — ไม่ใช่การประกาศ GA ใหม่ (MAF ขึ้น 1.0 GA ตั้งแต่ 2 เม.ย. 2026 แล้ว, Foundry Hosted Agents GA ก.ค. 2026) แต่เป็นการ **ปิด gap production stack** ให้ไม่ต้องประกอบของเองจาก open-source อีกต่อไป. เรื่องเด่นสามอย่างคือ Agent Harness, CodeAct ผ่าน Hyperlight, และ Handoff orchestration pattern — รวมถึง GitHub Copilot SDK integration ที่ลง MAF programming model.

**Agent Harness** เอา pattern ที่ builder เคยต้องเขียนเอง — context compaction, instruction merging, todo tracking, skill discovery จาก filesystem, plan/execute mode, background agent delegation, sandboxed shell (.NET only), integrated web search พร้อม approval workflow — มาเป็น first-class citizen. นี่คือสัญญาณชัดว่า Microsoft เห็น "agent harness เป็น OS layer ของ agentic era" และตั้งใจไม่ให้ builder ไปเลือก Claude Agent SDK / OpenAI Agents SDK ก่อน MAF.

ที่ควรจดคือ **CodeAct**. แทนที่ model จะ loop tool call ทีละตา (prompt→tool→prompt→tool→…) ให้ model เขียน Python block เดียวที่เรียก tool หลายตัวในโปรแกรม แล้วรันโปรแกรมนั้นใน Hyperlight micro-VM. บน workload ตัวแทนที่ Microsoft เปิดเผย ตัวเลขคือ **latency 27.81s → 13.23s** (ลด 52.4%) และ **token usage 6,890 → 2,489** (ลด 63.9%). Hyperlight — micro-VM ของ Microsoft ที่ออกแบบมาให้ start < 1ms — ทำให้ "strong isolation at the granularity of a single tool call ค่าแทบเป็นศูนย์" ตามคำพูดในประกาศ. ถ้าตัวเลขจริงใน field ใกล้เคียง นี่คือการเปลี่ยน economics ของ agent orchestration รอบใหม่ — token ที่ประหยัดได้ 60%+ ย้าย margin ของทั้ง stack.

**Foundry Hosted Agents** คือ production destination สำหรับทุก harness — ไม่ใช่แค่ MAF. ตั้งใจเป็น model-agnostic และ harness-agnostic: บรรจุ code เป็น container, scale-to-zero, per-session VM isolation พร้อม persistent filesystem, OpenTelemetry → Application Insights ในตัว. Microsoft รับทั้ง LangGraph, Claude Agent SDK, OpenAI Agents SDK, GitHub Copilot SDK, custom code — จงใจเปิดกว้าง เพราะต้องการให้ Foundry เป็น "cloud ของ agent" ไม่ว่าใครเป็น framework.

## ทำไมสำคัญ
Pattern ของ 2026 ชัดขึ้นทุกเดือน: **frontier model แข่งราคาแล้ว, moat ย้ายไป runtime + orchestration + developer surface**. Anthropic เพิ่งปล่อย Claude Code Mods (1 ต.ค.) ให้ developer เขียน middleware เข้า agent internals; DigitalOcean วาง Agent Droplets flat-price (1 ต.ค.); IBM ปล่อย Bob self-hosted air-gapped (1 ต.ค.); OpenAI เพิ่ม Agents API Computer Use (29 ก.ย.). ตอนนี้ Microsoft ขึ้นมาตั้งโต๊ะที่หนักที่สุด — ครอบตั้งแต่ harness → orchestration → hosted runtime → coding agent SDK ของ GitHub Copilot — บน model layer ที่เปิดกว้างกับทุก provider.

CodeAct เป็นจุดที่น่าจับตา. ตัวเลข 52% / 64% ไม่ใช่ academic benchmark — มันคือ "ให้ model เขียน code แทน loop tool call" ซึ่ง pattern นี้ CrewAI, LangGraph, Microsoft เอง, และ Anthropic ก็เริ่มสนใจตั้งแต่ paper CodeAct ปี 2024. ที่ Microsoft เพิ่มคือ **Hyperlight** — ทำให้การ sandbox ไม่ใช่ bottleneck. ถ้าคุณเป็น Builder ที่ยังอยู่ใน loop pattern (ReAct, function calling) การ migrate ไป CodeAct = cost structure ใหม่ที่ competitor ที่ยังอยู่ old pattern จะไล่ไม่ทัน.

Angle อีกข้างคือ **Foundry Hosted Agents กำลังจะเป็นสิ่งที่ Vercel/Cloudflare/Fly.io ต้องตอบ**. การที่ Microsoft เปิดรับ Claude Agent SDK + OpenAI Agents SDK ลงรันบน Foundry — นี่ไม่ใช่ท่าทีของ frenemy แต่คือการตั้ง "Agent Cloud" ที่ compiler-agnostic. ก่อน Foundry Agents ขึ้นมา Vercel มีเวลาเตรียมตัวจาก Agent Platform ที่ประกาศไว้ครึ่งปีก่อน — แต่หลังจากนี้ compete กับ Azure footprint + enterprise sales ของ Microsoft คือเกมคนละระดับ.

## มุม AI Agent Platform
**Builders** ควร prototype CodeAct บน workload ของตัวเองในสองสัปดาห์หน้า — ถ้า latency/token saving ใกล้ 50/60% ของ Microsoft ภาระ migration คุ้มชัด. harness-first pattern (plan→execute→verify loop แทน single-shot) ที่ MAF 1.0 รองรับคือ pattern ที่ LlamaIndex Extract v2.5 (ปล่อย 1 ต.ค.) ก็ใช้ — grounding score กระโดด 46.8 → 80.6 ชี้ตรงกันว่า harness ชนะ loop. **Users/businesses** ที่กำลังเลือก agent runtime: Foundry Hosted Agents + MAF 1.0 คือ "safe default" สำหรับ enterprise ที่ Microsoft stack อยู่แล้ว; แต่ถ้าทีม dev อยู่ Python + ต้องการ model เปิด ยังมีช่องให้ DigitalOcean Agent Droplets, Vercel, หรือ self-host. **Ecosystem**: Vercel Agent Platform, Cloudflare Agents, Fly.io, Modal, Render ต้องมี equivalent ของ CodeAct + Hyperlight ภายใน Q1 2027 ไม่งั้นจะเสีย developer tier; AWS Bedrock AgentCore ต้องประกาศ CodeAct equivalent ที่ reinvent 2026 ปลายปี; ส่วน vendor security (Snyk, Semgrep) จะมี product scan "AI-generated Python ที่รันใน micro-VM" ภายในสิ้นปี.

## Sources
- [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/)
- [Microsoft Build 2026 recap: vision, launches, and top sessions](https://developer.microsoft.com/blog/build-recap/)
- [Microsoft Agent Framework Harness and Hosted Agents Reach General Availability — InfoQ](https://www.infoq.com/news/2026/08/agent-framework-harness-ga/)
- [Microsoft Build 2026: Top Announcements for Agent Developers](https://newsletter.victordibia.com/p/microsoft-build-2026-top-announcements)

---

## Audio script
สวัสดีครับ ข่าวแรกของเช้าวันจันทร์. ที่ Microsoft BUILD 2026 สัปดาห์นี้ Microsoft เปิดไพ่ชุดใหญ่สำหรับ Agent Framework — รวมของ AutoGen และ Semantic Kernel ไว้ใน MAF ซึ่งขึ้น 1.0 GA ตั้งแต่เมษายน. ที่น่าสนใจที่สุดคือ CodeAct — แทนที่ model จะ loop เรียก tool ทีละตา ให้ model เขียน Python block เดียวที่เรียก tool หลายตัวในโปรแกรม แล้วรันในของที่เรียก Hyperlight ซึ่งเป็น micro-VM เบามาก. ตัวเลขที่ Microsoft เปิดเผยคือ latency ลด 52.4 เปอร์เซ็นต์, token usage ลด 63.9 เปอร์เซ็นต์ บน workload ตัวแทน. นี่คือการเปลี่ยน economics ของ agent orchestration เลย. อีกเรื่องคือ Foundry Hosted Agents ซึ่ง GA ไปตั้งแต่กรกฎาคม — scale-to-zero, VM isolation, รับทั้ง MAF, LangGraph, Claude Agent SDK, OpenAI Agents SDK, GitHub Copilot SDK. Microsoft ตั้งใจให้ Foundry เป็น Agent Cloud ที่ model-agnostic และ harness-agnostic. Pattern ของ 2026 ชัดขึ้น — moat ของ vendor ย้ายจาก model layer ไปอยู่ที่ runtime กับ orchestration ครับ. ถ้าคุณเป็น Builder ที่ยังอยู่ใน loop pattern แบบ ReAct, แนะนำให้ลอง prototype CodeAct ภายในสองสัปดาห์หน้าดู — ถ้าตัวเลขใกล้เคียงที่ Microsoft เปิด cost structure ใหม่คุ้มชัดครับ.
