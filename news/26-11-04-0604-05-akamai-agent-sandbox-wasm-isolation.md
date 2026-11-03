---
date: 2026-10-27
slug: akamai-agent-sandbox-wasm-isolation
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a glowing hex-shaped cell labeled
  "WASM SANDBOX" containing a tiny robot-agent typing code. Around the cell,
  thick translucent walls are stamped "DENY-BY-DEFAULT", "NO OUTBOUND",
  "CAPPED MEMORY", "CAPPED COMPUTE". Beneath the cell runs a river of binary
  that stops at the wall with a red X. A ribbon across the top reads "AKAMAI
  AGENT SANDBOX — BETA", with a small "SPIN · OPEN SOURCE" badge pinned
  below. Deep navy and electric cyan palette with safety-amber warning lines,
  1:1 aspect, strong contrast for 200px thumbnails, no real human faces.
image: images/26-11-04-0604-05-akamai-agent-sandbox-wasm-isolation.png
---

# Akamai Agent Sandbox เปิด beta — WebAssembly isolation deny-by-default สำหรับโค้ดที่ agent เขียน

## TL;DR
- 27 ต.ค. 2026 Akamai เปิด beta **Agent Sandbox** + **Akamai Inference** — runtime isolated สำหรับโค้ดที่ AI agent สร้าง
- ใช้ **WebAssembly isolation ใน runtime ตรง ๆ** (ไม่ wrap container) ผ่าน **Spin framework** (open-source)
- **Deny-by-default outbound** — code ที่ agent เขียนจะ run ด้วยไม่มี network access เว้นแต่ explicit grant
- Cap ได้ทั้ง compute, memory, outbound connection, system privilege
- Signal: **runtime isolation กลายเป็น default requirement** ของ enterprise agent, ไม่ใช่ feature premium

## เกิดอะไรขึ้น

27 ต.ค. 2026 Akamai ประกาศเปิด beta ของสอง product พร้อมกัน: **Agent Sandbox** และ **Akamai Inference**. Agent Sandbox คือ runtime ที่ชอบพิเศษ — agent หลักรันบน Akamai Functions, แต่ **โค้ดที่ agent เขียน** รันแยกใน sandbox ที่ใช้ WebAssembly เป็นชั้น isolation

Akamai ยืนยันว่าต่างจาก sandbox ที่ทีม dev ส่วนใหญ่รู้จัก (Firecracker VM, gVisor, Docker-in-Docker) ตรงที่ไม่ wrap container — ใช้ **WebAssembly isolation ตรงใน runtime** ซึ่งเร็วและกินทรัพยากรน้อยกว่า. Base ของ sandbox คือ **Spin framework** — Akamai เปิดเป็น open-source และ ship กับ Spin SDK

Security model: **deny-by-default outbound**. โค้ดที่ agent เขียนจะรันด้วย **no outbound access** ต้อง explicit grant. Cap ได้ครบทั้ง compute, memory, outbound connection, system privilege. Roadmap พูดถึง agent-governance control — ควบคุมว่า agent แตะอะไรได้บ้าง + อะไรแตะ agent ได้บ้าง — มาทีหลัง

Context: ตลาด agent sandbox เริ่มครึกครื้น. LangChain มี LangSmith Sandboxes, E2B มี cloud code interpreter, Together AI มี code execution runtime. Akamai เข้า segment นี้ด้วย edge angle — มี infrastructure พร้อม distribute โค้ดที่ agent สร้างไปรันที่ edge ใกล้ user โดยไม่ต้อง roundtrip กลับ origin

## ทำไมสำคัญ

ปี 2025 agent sandbox เป็น "feature"— ปี 2026 ครึ่งหลังมันกลายเป็น **default requirement**. สาเหตุที่ชัดคือ incident ที่เริ่มสะสม: coding agent รัน destructive command บน repo production (มี case Replit AI delete database, มี case Claude Code rm สำคัญ), LLM agent ที่ exfiltrate credential, agent ที่ invoke endpoint ไม่ควร. CISO ที่ยอมให้ agent รัน shell = เสี่ยง SOC2/ISO audit fail

Akamai เลือก WebAssembly แทน container เพราะ (1) startup time ต่ำกว่า container มาก (ms vs second), (2) attack surface ของ Wasm VM น้อยกว่า OCI runtime, (3) deny-by-default กำหนดง่ายกว่าใน capability model ของ Wasm. Trade-off: โค้ด native (C, Rust compiled, บาง Python lib ที่ต้อง C extension) ต้อง compile เป็น Wasm ก่อน — ซึ่งปัจจุบันยังเจ็บปวดกับ Python ecosystem. ถ้า agent สร้าง Python ที่ใช้ numpy/pandas — ต้อง solve ที่ environment ก่อน

ที่น่าจับตา: Spin เป็น **open-source** — Akamai ไม่ได้ lock architecture ไว้กับตัวเอง. นี่คือ pattern เดียวกับ gVisor (Google open-source), Firecracker (AWS open-source) — คือ hyperscaler เลือกเปิด infrastructure layer เพื่อให้ ecosystem standardize แล้ว monetize ที่ hosted service. Cloudflare Workers ที่ใช้ V8 isolate แข่งกันตรงนี้โดยตรง, AWS จะต้องตอบในระดับเดียว (ปัจจุบัน Bedrock AgentCore code interpreter ยังเป็น container-based)

Pattern ที่สอดคล้องกับเรื่อง 01 (Uber MCP Gateway) และ 02 (GitHub Copilot connectors): **ชั้น infrastructure สำหรับ agent กำลังเป็น commodity ที่ hyperscaler แข่งกันเปิด** — identity (Descope), gateway (Uber-style), distribution (GitHub), sandbox (Akamai). ชั้นที่จะยัง monetize ได้คือ hosted service ที่รวม layer เหล่านี้ให้ enterprise ใช้ได้โดยไม่ต้อง self-host

## มุม AI Agent Platform

สำหรับ **builders** ที่สร้าง agent framework: ถ้า framework ยัง default ให้ agent รัน shell/exec บน host — refactor เร็ว. Baseline ของ enterprise ตอนนี้คือ sandbox + deny-by-default. ลองประเมิน Spin, E2B, LangSmith Sandbox, Akamai Agent Sandbox เป็น option; ไม่มีใครควร roll-your-own sandbox ในปี 2026

สำหรับ **users / business** ที่ deploy agent: ก่อนให้ agent รัน code — list สามคำถาม (1) sandbox อยู่ที่ไหน?, (2) outbound network policy คืออะไร?, (3) ใครเห็น log? ถ้าตอบไม่ได้ครบสามข้อ = ไม่ควร deploy production. ไทยมีบริษัทที่ deploy coding agent ใน CI/CD pipeline อยู่แล้ว — ควร audit outbound connection ของ agent ใน pipeline ภายในเดือนนี้

สำหรับ **ecosystem**: ปี 2027 น่าจะเห็น convergence — ทุก enterprise agent platform ต้อง ship built-in sandbox, ไม่ bundle แยก. Anthropic Claude Code เริ่มมี built-in sandbox mode แล้ว, OpenAI Codex มี container isolation, Google Antigravity ยังไม่ชัด. ที่น่าสังเกต: standard สำหรับ sandbox policy (เช่น "agent allowed to call these domains, use max X cpu-sec") ยังไม่มี — Akamai + Spin น่าจะ push spec นี้เพื่อ lock-in มาตรฐาน. OCI-style spec สำหรับ agent sandbox คือ layer ที่จะเกิดในปีหน้า

## Sources
- [Akamai launches AI inference service and agent sandbox (Techzine Global)](https://www.techzine.eu/news/infrastructure/145346/akamai-launches-ai-inference-service-and-agent-sandbox/)
- [Akamai Launches Agent Sandbox to contain code written by AI agents (Crypto Briefing)](https://cryptobriefing.com/akamai-launches-agent-sandbox-ai-security/)
- [Akamai Agent Sandbox product page](https://www.akamai.com/products/akamai-agent-sandbox)
- [Akamai Adds AI Inference and Agent Sandbox (650 Group)](https://650group.com/blog/akamai-inference-agent-sandbox/)

---

## Audio script
ข่าวสุดท้ายวันนี้ครับ 27 ต.ค. Akamai เปิด beta Agent Sandbox และ Akamai Inference พร้อมกัน Agent Sandbox เป็น runtime isolated สำหรับโค้ดที่ AI agent สร้าง agent หลักรันบน Akamai Functions แต่โค้ดที่ agent เขียนรันแยกใน sandbox ที่ใช้ WebAssembly เป็นชั้น isolation ต่างจาก sandbox ที่ทีม dev ส่วนใหญ่รู้จักเช่น Firecracker หรือ gVisor ตรงที่ไม่ wrap container ใช้ WebAssembly isolation ตรงใน runtime ซึ่งเร็วและกินทรัพยากรน้อยกว่า Base คือ Spin framework ที่ Akamai เปิดเป็น open source Security model สำคัญ deny by default outbound โค้ดที่ agent เขียนจะรันด้วยไม่มี network access ต้อง explicit grant Cap ได้ครบทั้ง compute, memory, outbound connection, system privilege ปี 2025 agent sandbox เป็น feature ปี 2026 ครึ่งหลังมันกลายเป็น default requirement สาเหตุคือ incident สะสม coding agent รัน destructive command บน repo production LLM agent ที่ exfiltrate credential agent ที่ invoke endpoint ที่ไม่ควร CISO ที่ยอมให้ agent รัน shell เสี่ยง SOC2 fail Akamai เลือก Wasm แทน container เพราะ startup time ต่ำกว่ามาก attack surface น้อยกว่า และ deny by default กำหนดง่ายกว่าใน capability model ของ Wasm Trade off คือ โค้ด native ต้อง compile เป็น Wasm ก่อน Python ที่ใช้ numpy pandas ต้อง solve ที่ environment ก่อน ที่สำคัญคือ Spin open source Akamai ไม่ lock architecture — pattern เดียวกับ Firecracker ของ AWS หรือ gVisor ของ Google สำหรับทีมที่ deploy coding agent ใน CI CD pipeline ไทยควร audit outbound connection ของ agent ภายในเดือนนี้ครับ
