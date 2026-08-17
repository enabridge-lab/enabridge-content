---
date: 2026-08-18
slug: nvidia-nemotron-lightning-switchyard
topic: agentic-ai
sources: 5
reading_time_min: 5
image_prompt: |
  Editorial isometric illustration of a giant chrome railway switchyard
  where dozens of glowing model tokens shoot down parallel tracks; a
  central lightning bolt splits into 4 forks labeled with big stacked
  numerals — "4x SPEED", "30% FASTER", "30B PARAMS", "ALWAYS-ON". Small
  worker robot silhouettes ride each token, one arriving at a station
  labeled "AGENT TASK COMPLETE". Deep obsidian and electric emerald
  palette (NVIDIA green accent), dramatic chiaroscuro, editorial
  typography readable at 200px thumbnail; 1:1 aspect; silhouettes only,
  no real human faces, no brand logos.
image: images/26-08-18-0611-03-nvidia-nemotron-lightning-switchyard.png
---

# NVIDIA ปล่อย Nemotron 3.5 Lightning + NeMo Switchyard — 4x เร็วขึ้น, model routing เป็น OSS

## TL;DR
- **NVIDIA** launch **Nemotron 3.5 Lightning** (11 ส.ค.) — 30B MoE open-weight model สำหรับ agent task, **4x output speed** + **30% เร็วขึ้นต่อ task completion** เทียบ comparable
- ปล่อย **NeMo Switchyard** เป็น open-source routing tool คู่กัน — route ทุก request ไป model ที่ handle ได้เร็วสุด/ถูกสุด (small local, medium open, frontier hosted)
- **OCI Enterprise AI** เป็น cloud แรกที่รองรับ Nemotron 3.5 Lightning ตั้งแต่ 11 ส.ค. — Oracle เร่ง sales motion ให้ทัน Q4 fiscal
- Positioning: NVIDIA ตอบ Cisco/enterprise trend ตรง ๆ — "always-on agent workload ที่ทำ action หลายพันครั้ง/วันไม่ควรจ่าย frontier-tier ทุก call"
- Signal: model routing กลายเป็น commodity infrastructure — LiteLLM, Portkey, OpenRouter, ตอนนี้บวก NVIDIA-native = category consolidation ใกล้เกิด

## เกิดอะไรขึ้น

11 ส.ค. NVIDIA launch **Nemotron 3.5 Lightning** — 30 billion parameter Mixture-of-Experts model, open-weight, ปล่อยเป็น "specialized executor" สำหรับ agentic workload. spec ตัวเลขที่ NVIDIA เปิด: **output speed 4x** ของ comparable open model ในขนาด class เดียวกัน, **task completion time 30% ลดลง** เมื่อ measure บน long-running agent benchmark (routing + tool call + verification), และ **train specifically for popular agent harness** (LangGraph, CrewAI, AutoGen, OpenAI Agents SDK, LlamaIndex)

พร้อมกัน NVIDIA ปล่อย **NeMo Switchyard** — open-source routing tool ที่ทำสิ่งที่ LiteLLM, Portkey, OpenRouter ทำอยู่แล้ว แต่ optimize สำหรับ enterprise scale + integrate ตรงกับ NVIDIA inference stack (DGX Cloud, RTX, Jetson). concept คือ request แต่ละครั้งไม่ต้อง hard-code model — Switchyard วิเคราะห์ task ที่ runtime แล้ว route ไป model ที่ handle เร็วสุด/ถูกสุด. Nemotron 3.5 Lightning ออกแบบเป็น "default target" ของ Switchyard สำหรับ routine agent action

Adoption day 1: **Oracle Cloud Infrastructure (OCI) Enterprise AI** เป็น cloud provider แรกที่รองรับ Nemotron 3.5 Lightning ตั้งแต่ 11 ส.ค. Oracle press release เน้นว่า customer สามารถ customize model สำหรับ specialized business workflow + deploy ผ่าน OCI Generative AI service โดยไม่ต้อง manage infra. AWS + GCP + Azure ยังไม่ประกาศ — คาดว่าจะตามภายใน 30 วัน

Positioning ที่ Jensen Huang จะพูดใน GTC keynote เดือน ต.ค. (leak แล้วผ่าน NVIDIA blog): **"always-on agent workload ที่ทำ thousands of small actions ต่อวันไม่ควรใช้ frontier-tier compute ทุก call"** — direct response ต่อ Cisco 90K rollout ที่ประกาศ model routing เป็น core architectural choice ต้นเดือนเดียวกัน

Nemotron 3.5 Lightning ต่างจาก Meta Llama 4.5 / DeepSeek V4 / Qwen 3 ตรงที่ **train บน trace data ของ agent harness จริง** — NVIDIA เก็บ trace จาก partnership กับ 40+ enterprise ที่ run agent ใน production ตลอดปี. ผลคือ model ทำ tool call format, JSON schema, error recovery ได้ reliable กว่า general-purpose model ในขนาด class เดียวกัน — benchmark ที่ NVIDIA เปิดโชว์ tool call success rate 96% vs Llama 4.5 ที่ 84%

## ทำไมสำคัญ

Launch นี้คือ **admission ครั้งแรกจาก NVIDIA ว่า frontier model ไม่ใช่ answer สำหรับ agent scale**. ตลอด 2 ปีที่ผ่านมา NVIDIA sell narrative "buy more GPU สำหรับ frontier model bigger" — ตอนนี้เริ่ม pivot ไป "buy same GPU สำหรับ routing many small model efficiently". market นี้ใหญ่กว่ามาก: enterprise ที่ run agent ตลอดวัน (24/7 monitoring, automated support, always-on scheduling) มี call volume 100-1000x ของ interactive workload — margin per call เล็กแต่ volume ใหญ่

Pattern ที่เห็น: **specialization ของ model เป็นทิศทางที่ inevitable**. ปี 2023-2024 = frontier ทุก call; ปี 2025 = mixture (frontier + cheap); ปี 2026 = routing tiered (small local, medium open, frontier hosted). ทั้ง NVIDIA (Nemotron + Switchyard), Cisco (internal router), Anthropic (Haiku + Opus tiering), OpenAI (nano + mini + flagship) ตกลงบน design pattern เดียวกัน. คนที่ยังใช้ single-model architecture ใน 2027 = สู้ cost ไม่ไหว

จุดที่ NVIDIA gain leverage คือ **integration ระดับ vertical**: model + routing + inference stack + GPU + cloud partner + support tool. LiteLLM + Portkey + OpenRouter มี moat แค่ orchestration; NVIDIA มี moat จาก physical infra ลงไป — extend เข้า on-prem (DGX), edge (Jetson), workstation (RTX). ถ้า Switchyard adoption ทะลุ 10K deployment ใน 6 เดือน = LiteLLM/Portkey ต้อง pivot ไปเป็น management layer บน Switchyard ไม่ใช่ compete

Weak point: **OSS ที่ NVIDIA controlled ยัง suspect ใน buyer sentiment** — CIO Fortune 500 หลายคนเรียก NVIDIA "de facto Oracle ของ AI" แล้ว. ถ้า Nemotron หรือ Switchyard start ผูก dependency กับ NVIDIA-only feature (CUDA extension, TensorRT-LLM only) = trigger anti-lock-in backlash

Cross-reference: cover ข่าว **Cisco 90K rollout** (brief 02 ของรอบนี้) — ทั้งสอง data point ยืนยัน **model routing เป็น default architecture ของ agent ในปี 2026-2027**. Product manager ของ startup ที่ยัง sell "we use GPT-5" เป็น differentiator = ต้องเปลี่ยน pitch ทันที

## มุม AI Agent Platform

**Builders / framework maker:** ถ้าไม่ integrate model routing ใน SDK ระดับ first-class = OSS project ตายภายใน 12 เดือน. LangChain, LlamaIndex, DSPy ต้อง ship Switchyard adapter + LiteLLM adapter + Portkey adapter ให้ครบใน next release. คนที่ launch framework ใหม่ในปี 2027 โดยไม่มี routing = ไม่มี VC backing

**Users / business deployer:** **audit agent traffic** ตอนนี้ — 80% ของ call ที่ agent ทำเป็น task ระดับ "route email" "summarize slack thread" "extract JSON field" — ทั้งหมด over-serve ด้วย frontier model. shift ไป Nemotron 3.5 Lightning หรือ Haiku หรือ GPT-mini แล้ววัด quality drop. ประหยัด 60-80% cost ทันที ถ้า tolerance ยอมได้

**Ecosystem:** Oracle bet Nemotron 3.5 Lightning เข้า OCI ก่อน hyperscaler อื่น = **repositioning ใหญ่ของ Oracle Enterprise AI**. ถ้า customer conversion rate ดี Q3-Q4 = Oracle Cloud growth story ที่ investor รอ 5 ปี. สำหรับ Thai enterprise ที่ evaluate multi-cloud — OCI ตอนนี้มี legit AI story ครั้งแรกใน 3 ปี, ควร shortlist กลับเข้า evaluation

## Sources
- [NVIDIA Nemotron 3.5 Lightning Delivers Fast, Accurate Specialized Task Execution (NVIDIA Blog)](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/)
- [NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard Deliver Faster Agentic AI (NVIDIA Blogs)](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/)
- [NVIDIA launches Nemotron 3.5 Lightning to make repetitive agent tasks up to 4x faster (Interesting Engineering)](https://interestingengineering.com/ai-robotics/nvidia-nemotron-35-lightning-autonomous-agents)
- [Nvidia launches Nemotron 3.5 Lightning as US open model momentum picks up (Constellation Research)](https://www.constellationr.com/insights/news/nvidia-launches-nemotron-35-lightning-us-open-model-momentum-picks)
- [What's New in Oracle AI? August 2026 Edition (Oracle Blog)](https://blogs.oracle.com/ai-and-datascience/whats-new-in-ai-august-2026)

---

## Audio script
เรื่องที่สาม NVIDIA เพิ่ง launch โมเดลชื่อ Nemotron 3.5 Lightning วันที่ 11 สิงหาคม เป็นโมเดล open-weight ขนาด 30 พันล้าน parameter แบบ Mixture-of-Experts ที่ออกแบบมาเฉพาะ agent workload. spec ที่ NVIDIA เปิด — 4 เท่าของ output speed และ 30% เร็วขึ้นต่อ task completion เทียบโมเดล open size เดียวกัน. train บน trace data ของ agent จริง 40 กว่า enterprise ทำให้ tool call success rate อยู่ที่ 96 เปอร์เซ็นต์ vs Llama 4.5 ที่ 84%. ปล่อยพร้อมกันคือ NeMo Switchyard เป็น open-source routing tool ที่ทำสิ่งที่ LiteLLM กับ Portkey ทำอยู่ แต่ integrate ตรงกับ NVIDIA inference stack. OCI Enterprise AI เป็น cloud แรกที่ support ตั้งแต่ day 1 — Oracle เร่ง sales motion ให้ทัน Q4 fiscal. signal ที่ใหญ่คือ NVIDIA เริ่ม admit ว่า frontier model ไม่ใช่ answer สำหรับ agent scale — market ของ small tiered model จะใหญ่กว่า market ของ frontier ในปี 2027 เพราะ agent always-on ทำ call วันละพันครั้ง. สำหรับทีมที่ deploy agent ทุกวันนี้ audit traffic ทันที 80% ของ call เป็น task ที่ over-serve ด้วย frontier — shift ไป Nemotron หรือ Haiku ประหยัด 60-80% cost ทันที.
