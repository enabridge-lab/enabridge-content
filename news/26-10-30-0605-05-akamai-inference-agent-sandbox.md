---
date: 2026-10-30
slug: akamai-inference-agent-sandbox
topic: openbridge-trend
reading_time_min: 3
sources: 3
image_prompt: |
  An editorial isometric illustration of a glowing world globe wrapped in a
  honeycomb mesh of edge nodes; each node a tiny secure cell labeled "WASM
  SANDBOX". A hovering shelf of chips reads "NVIDIA B300", "NEMOTRON 3 ULTRA",
  "GPT-OSS-120B", "GEMMA 4". Massive display text above: "AGENTS AT THE EDGE".
  On the left a stack of three numbers: "12 OPEN MODELS", "2.8T PARAMS", "WASM
  ISOLATION". Deep indigo and teal palette, Kodak-film grading, high contrast
  for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-30-0605-05-akamai-inference-agent-sandbox.png
---

# Akamai เปิด AI Inference + Agent Sandbox beta — CDN รายใหญ่ขยับเป็น edge agent runtime

## TL;DR
- **27 ต.ค.** Akamai เปิด 2 ผลิตภัณฑ์ beta พร้อมกัน: **Akamai Inference** (managed model serving) + **Akamai Agent Sandbox** (isolated execution สำหรับ code ที่ agent generate)
- Inference catalog เริ่มที่ **12 open-weight models** range **8B → 2.8T parameters** รวม **NVIDIA Nemotron 3 Ultra, OpenAI gpt-oss-120b, Google Gemma 4** + serverless deploy option
- Agent Sandbox รันบน **WebAssembly** ตาม Spin framework (open source), cap **compute + memory + outbound connections + system privileges**
- Hardware: **NVIDIA B300 cluster** พร้อม (ผ่าน sales); **Vera Rubin** support **2027**
- Signal: ชั้น **CDN รายใหญ่ (Akamai, Cloudflare, Fastly)** ขยับเป็น **edge agent runtime** — compete กับ hyperscaler ด้วย latency + distribution

## เกิดอะไรขึ้น

27 ต.ค. Akamai ประกาศเปิด beta 2 ผลิตภัณฑ์ที่ชั้น compute: **Akamai Inference** และ **Akamai Agent Sandbox**. ประเด็น positioning: Akamai มี CDN footprint **4,100+ POP ใน 1,000+ city** ที่ยาวนานเป็น infrastructure delivery layer ของเว็บ — ตอนนี้ขยับไปเป็น infrastructure สำหรับ agent inference + agent execution ที่ **edge** แทน

**Akamai Inference** — managed model serving. Catalog เริ่มที่ 12 open-weight models, range จาก **8B parameter เล็ก** (เหมาะสำหรับ edge inference, low-latency chat) ไป **2.8T parameter** (NVIDIA Nemotron 3 Ultra — frontier-grade open model). รุ่นเด่นอื่น: **OpenAI gpt-oss-120b**, **Google Gemma 4**, Meta Llama 4.5, Mistral Large 2.1. **Serverless deploy option** รวมใน beta — dev deploy model ครั้งเดียว, scale ตาม request. Hardware baseline: **NVIDIA B300 GPU cluster** (ผ่าน sales channel, ยัง gated); **Vera Rubin** (NVIDIA Gen next) ประกาศ support ปี **2027**

**Akamai Agent Sandbox** — isolated execution environment สำหรับ code ที่ agent generate (คล้ายกับ Vercel Sandbox, E2B, Modal Sandbox). ที่ **ต่าง**: Akamai Agent Sandbox รันบน **WebAssembly (WASM)** โดย build on **Spin framework** (open-source project ของ Fermyon). ชั้น WASM บังคับ: cap compute, cap memory, cap outbound network connections, cap system privilege. ต่างจาก container-based sandbox (Docker/Kubernetes-ของ OpenSandbox Alibaba) ที่ประหยัดกว่าในการจัดสรร resource — WASM start ใน **milliseconds**, overhead ต่ำกว่า **100×** ของ Docker ใน spin-up

ชั้น enterprise angle: **Akamai Agent Sandbox เป็น open-source component** ของ Spin framework — คือ customer ที่กลัว vendor lock-in สามารถ **run Spin ที่ cloud ใดก็ได้** พร้อม compatibility layer เดียวกัน. ตรงข้ามกับ OpenAI Sandbox / Anthropic Code Execution ที่เป็น proprietary. Position นี้ให้ Akamai ตีตลาด customer segment ที่ **multi-cloud + regulated** (financial services, healthcare, EU customer under AI Act)

## ทำไมสำคัญ

ประเด็นที่หนึ่ง — **CDN รายใหญ่กำลังเปลี่ยนตัวเองเป็น edge compute platform** อย่างเปิดเผย. **Cloudflare Workers AI** เปิดก่อน 2023; **Fastly Compute@Edge** push model inference 2024-2025; วันนี้ Akamai เข้า full stack. Latency ของ agent interaction (chat, code execution, tool call) เริ่มจะ **bottleneck อยู่ที่ network, ไม่ใช่ model** — เพราะ model inference ต่อ token ใน Blackwell/TPU 8i เร็วถึงระดับ sub-second แล้ว แต่ RTT จาก edge user ไปที่ data center ใน us-east-1 ยัง 50-200ms. Edge inference ที่ POP ใกล้ user = **cut 100ms+ RTT** = agent chat ที่ "responsive feel". นี่คือ moat ที่ CDN เจ้าใหญ่มี, hyperscaler ยังไม่ประชันได้ (เพราะ POP ของ AWS/Azure ที่ edge จริงมีน้อยกว่า CDN)

ประเด็นที่สอง — **WASM-based sandbox คือ frontend war ที่สำคัญ**. ชั้น agent sandbox ตอนนี้มี 3 architecture หลัก: (1) **container (Docker/K8s)** — OpenSandbox Alibaba, Vercel Sandbox, E2B, (2) **MicroVM (Firecracker)** — Modal, Fly Machines, (3) **WASM** — Akamai Spin, Fastly Compute. WASM ชนะที่ **cold start** (ms) + **density** (10,000+ sandbox ต่อ VM) — เหมาะกับ agent fleet ที่ 1 agent เรียก sub-agent 50 ตัวต่อ workflow. ข้อเสีย: **tool compatibility แคบ** (ไม่ run Python arbitrary; รัน language ที่ compile WASM ได้ — Rust, Go, JS, Python ผ่าน Pyodide). ตลาด enterprise จะต้อง pick: **generality (Docker) หรือ speed+density (WASM)** — ต้นปี 2027 นี่เป็น architectural debate ชัดเจน

ประเด็นที่สาม — **Nemotron 3 Ultra 2.8T + gpt-oss-120b บน Akamai edge = open-weight ยังมีชีวิต**. ก่อนหน้านี้ debate ว่า open-weight model จะโดน closed vendor (OpenAI, Anthropic) **outcompete** เพราะ compute scale และ data flywheel. Reality 2026: **NVIDIA Nemotron 3 Ultra 2.8T** เป็น open weight ที่ outperform GPT-4 ที่หลาย benchmark; **gpt-oss-120b** จาก OpenAI เองที่ release เมื่อ ส.ค. ที่ outperform Llama 3 70B. การที่ Akamai เลือก **host open weight เป็น default** = commercial validation ว่า open stack competitive. ชั้น enterprise ที่ไม่อยากพึ่ง closed vendor (regulated industries, sovereign AI) ได้ production-grade option วันนี้

## มุม AI Agent Platform

**Builders**: Akamai Spin + WASM sandbox เป็น **free tool stack** สำหรับ dev ที่สร้าง agent — download Spin ลง laptop, test local, deploy ไป Akamai edge หรือ Fly หรือ Fastly ตาม bidding. Compared กับ Vercel Sandbox / E2B ที่เป็น vendor-lock, Spin ให้ freedom portability. Framework ของ agent (CrewAI, LangGraph) ที่ compile ลง WASM จะมี distribution advantage ภายใน 6 เดือน

**Users / business**: Enterprise ที่ build chatbot หรือ internal agent — edge inference จาก Akamai แปลว่า **respond time < 500ms end-to-end** ที่ Southeast Asia (เพราะ Akamai มี POP ใน Bangkok, Singapore, Jakarta). เทียบ: AWS inference จาก Virginia มี 250ms RTT ก่อน model แม้ Blackwell จะเร็วแค่ไหน. Thai enterprise ที่ build customer-facing agent (banks, telco, retail) จะเลือก edge inference เป็น default — latency + data residency อยู่ที่ POP ไทยเอง

**Ecosystem**: Market split ชัดระหว่าง "AI compute layer" กับ "agent runtime layer": AWS/GCP/Azure/Oracle = heavy training + large-scale inference; Akamai/Cloudflare/Fastly = light-inference + agent sandbox edge; Snowflake/Databricks = in-data agent primitive. VC ที่ allocate ที่ชั้น infra ควรเห็น gap: **"orchestration ที่ route งานข้าม layer เหล่านี้"** ยังเปิด — ไม่มี vendor เดียวครอบทั้ง stack. Thai VC ที่ bet agent orchestration layer local = window ยังเปิด ภายใน H1 2027

## Sources
- [Akamai launches AI inference service and agent sandbox (Techzine Global)](https://www.techzine.eu/news/infrastructure/145346/akamai-launches-ai-inference-service-and-agent-sandbox/)
- [Akamai Launches AI Inference and Agent Sandbox in Beta (StockTitan — Akamai press)](https://www.stocktitan.net/news/AKAM/akamai-launches-ai-inference-service-and-agent-execution-0uym3tqcwiyc.html)
- [Akamai opens inference and agent-code sandbox betas on its cloud (OpenTools)](https://opentools.ai/news/akamai-inference-agent-sandbox-beta-spin-sdk-serverless-october-2026)

---

## Audio script
Akamai ประกาศวันอังคารที่ 27 ตุลาคม เปิด 2 ผลิตภัณฑ์ beta พร้อมกัน หนึ่งคือ Akamai Inference managed model serving ที่มี catalog เริ่มที่ 12 open-weight models ตั้งแต่ 8 พันล้าน parameter ถึง 2.8 ล้านล้าน parameter รวม NVIDIA Nemotron 3 Ultra, OpenAI gpt-oss-120b, Google Gemma 4 แล้วก็มี serverless deploy option ให้ dev deploy ครั้งเดียว scale ตาม request ฮาร์ดแวร์เริ่มที่ NVIDIA B300 cluster และ Vera Rubin support ปี 2027 สองคือ Akamai Agent Sandbox ที่เป็น isolated execution environment สำหรับ code ที่ agent generate รันบน WebAssembly ตาม Spin framework ซึ่งเป็น open source cap resource ทั้ง compute memory outbound connection system privilege ความต่างจาก sandbox แบบ Docker คือ WASM start ใน milliseconds overhead ต่ำกว่า 100 เท่า เหมาะกับ agent fleet ที่ 1 agent เรียก sub agent 50 ตัวต่อ workflow ประเด็นสำคัญคือ CDN รายใหญ่กำลังเปลี่ยนตัวเองเป็น edge agent runtime อย่างเปิดเผย ทั้ง Akamai, Cloudflare, Fastly การที่ latency ของ agent interaction เริ่ม bottleneck ที่ network ไม่ใช่ model แล้ว ทำให้ edge inference เป็น moat ที่ hyperscaler สู้ไม่ได้ สำหรับ Thai enterprise ที่สร้าง customer-facing agent — ธนาคาร telco retail — Akamai มี POP ใน Bangkok Singapore Jakarta แปลว่า respond time ต่ำกว่า 500 ms end to end data residency อยู่ที่ POP ไทยเอง เป็น default choice ปีหน้าแน่นอน
