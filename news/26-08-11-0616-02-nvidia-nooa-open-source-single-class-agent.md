---
date: 2026-08-10
slug: nvidia-nooa-open-source-single-class-agent
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A minimalist code editor showing a single Python class labeled "class Agent:"
  glowing green on dark background; three benchmark cards float above:
  "SWE-BENCH 82.2%", "CYBERGYM 86.8%", "ARC-AGI-3 85.1%". NVIDIA logo bottom right,
  Apache 2.0 badge top left. Editorial isometric style, neon green on charcoal,
  1:1 aspect, no real human faces.
image: images/26-08-11-0616-02-nvidia-nooa-open-source-single-class-agent.png
---

# NVIDIA เปิด NOOA — agent framework Python คลาสเดียว, SWE-bench 82.2%, ครึ่ง token cost

## TL;DR
- NVIDIA ปล่อย NOOA (NVIDIA Object-Oriented Agents) เป็น open-source Apache 2.0 — agent ทั้งตัวคือ Python class เดียว, method = action, field = state, docstring = instruction
- Benchmark: SWE-bench Verified 82.2%, CyberGym L1 86.8%, ARC-AGI-3 85.1% — คู่แข่งใกล้เคียง Claude Code/Devin แต่ประหยัด token ราวครึ่ง
- Version v0.0.8 alpha, `pip install nooa`, Python 3.12-3.13, model-agnostic ผ่าน LiteLLM

## เกิดอะไรขึ้น
วันที่ 7 สิงหาคม NVIDIA Labs ปล่อย NOOA — Object-Oriented Agents framework ที่ตั้งใจแก้ปัญหาที่ทุกคนบ่นเรื่องเดียวกัน: agent code ในปี 2026 กระจายอยู่ทั่วไปหมด prompt template อยู่ไฟล์หนึ่ง, tool schema อยู่อีกไฟล์, workflow graph ใน YAML, callback ใน Python — พอ debug จริงต้องเปิด 5 ไฟล์ NOOA ยุบทั้งหมดเหลือ Python class เดียว: method คือ action, field คือ state, docstring คือ instruction ที่ agent อ่านเอง, type annotation คือ validation ทั้ง input และ output

Benchmark ที่ NVIDIA รายงานไม่ใช่แค่ผ่านมาตรฐาน — SWE-bench Verified 82.2%, CyberGym L1 86.8%, ARC-AGI-3 85.1% ทั้งสามอันดับใกล้เคียง Claude Code, Devin, และ Cognition ที่ใช้ scaffold ซับซ้อนกว่ามาก จุดที่เด็ดกว่าคือ **token cost ลดครึ่ง** — เพราะ NOOA ไม่มี intermediate abstraction layer ที่บีบ context ผ่าน tool describe/return format หลายชั้น agent อ่าน state ตัวเองตรง ๆ ผ่าน Python inspection

ทาง security NVIDIA ประกาศตรงไปว่า AST check และ module deny-list ที่ built-in **ไม่ใช่ containment boundary** — ต้อง run ใน container หรือ VM หรือ NVIDIA OpenShell ที่ปล่อยตอนต้นเดือน คำเตือนนี้สำคัญเพราะ agent ที่ execute Python code ที่ LLM generate คือ RCE-by-design ถ้าไม่มี isolation layer

Repo NVIDIA/NOOA บน GitHub เจอ 8,000+ star ใน 48 ชั่วโมง, HN front page 3 วันติด — เป็นสัญญาณว่าชุมชน dev รับ pattern นี้ทันที เพราะ curve การเรียนรู้แค่รู้จัก Python class ก็เริ่มได้

## ทำไมสำคัญ
NOOA คือ**การ push back ต่อ framework complexity** ที่โตขึ้นเรื่อย ๆ ตลอดปี — LangGraph, CrewAI, AutoGen, Semantic Kernel, Agent Framework ของ Microsoft ทุกเจ้าเพิ่ม abstraction layer เพื่อจัดการ multi-agent, state, tool routing แต่ยิ่งเพิ่ม layer ยิ่งเพิ่ม token cost และ debugging burden NVIDIA มาบอกว่า: object-oriented Python ที่ engineer ทุกคนรู้จักอยู่แล้ว pattern เก่า 30 ปีนี่แหละพอ

Signal ที่ตามมา: ทีมที่ token bill พุ่งจาก multi-agent scaffolding — ยกตัวอย่างบริษัทที่ใช้ CrewAI แล้วเจอ bill $50k+/เดือน จาก orchestration overhead — จะเริ่มพิจารณา flat framework แบบ NOOA เพราะประหยัดชัดเจน NVIDIA ไม่ได้บังคับใช้ NIM หรือ CUDA — model-agnostic ผ่าน LiteLLM แปลว่ารันกับ Claude, GPT, Gemini, DeepSeek ก็ได้ ท่าเปิดกว้างกว่า framework ปกติของ vendor รายอื่น

จุดยาก: v0.0.8 alpha ยัง production-ready ไม่ได้ — ไม่มี async support ที่ mature, retry logic ยัง manual, ยังไม่มี distributed tracing built-in Cognition หรือ Anthropic ยังไม่ควรทิ้ง Claude Code หรือ agent SDK ของตัวเองไปเลย แต่สำหรับ startup ที่ prototype agent ใหม่ NOOA เป็นทางเลือกที่ deployment ง่ายกว่ามาก

## มุม AI Agent Platform
สำหรับ **builders** ที่กำลังทำ framework ของตัวเอง: NOOA reset baseline ว่า agent framework ที่ "ดี" คืออะไร — ตอนนี้ standard คือ SWE-bench 80%+ ที่ประหยัด token ครึ่งของ scaffold ปกติ ถ้าอยู่ในตลาด framework แบบ CrewAI, LangGraph, ต้อง benchmark ตัวเองกับ NOOA แล้วอธิบายว่า overhead ที่เพิ่มมีคุณค่าอะไร สำหรับ **users/business** ที่ใช้ agent อยู่แล้ว: ถ้า vendor ของคุณคิด token markup 3-4x จาก orchestration layer — เช่น bill $30/month per user แต่ effective token ประมาณ $8 — NOOA เป็น leverage negotiation ให้ต่อรอง

สำหรับ **ecosystem/vendor**: NVIDIA ไม่ใช่ agent company มาแต่ไหน แต่การ ship framework นี้ทันทีหลัง Open Secure AI Alliance (37 สมาชิก) เดือน July signal ว่า Jensen เห็นตลาด agent runtime เป็น battlefield ต่อไปหลัง GPU — และไม่อยากปล่อยให้ Anthropic, OpenAI, Google ครอบครองชั้น software คำถามที่ตามมา: ถ้า NVIDIA push NOOA + OpenShell + NIM เข้าเป็น full-stack agent platform ที่รันบน GPU ตัวเอง Nemotron model จะเข้า chart ในปีนี้แบบไหน — เพราะ NVIDIA มี full control ตั้งแต่ chip ยัน runtime framework

## Sources
- [NVIDIA AI Releases NOOA (MarkTechPost)](https://www.marktechpost.com/2026/08/07/nvidia-ai-releases-nooa-an-object-oriented-python-framework/)
- [NVIDIA open-sources NOOA, a single-class Python agent framework (AI Weekly)](https://aiweekly.co/alerts/nvidia-open-sources-nooa-a-single-class-python-agent-framework)
- [NVIDIA NOOA Review 2026: 82.2% SWE-bench, Apache 2.0](https://aitoolsrecap.com/Blog/nvidia-nooa-python-agent-framework-review-2026)

---

## Audio script
NVIDIA เพิ่งปล่อย framework agent ตัวใหม่ชื่อ NOOA ครับ ชื่อย่อจาก NVIDIA Object-Oriented Agents ไอเดียคือยุบ agent ทั้งตัวให้เป็น Python class เดียว method ก็คือ action ของ agent field คือ state docstring คือ instruction ที่ agent อ่านเอง เรียบง่ายมากจนคนเริ่มจาก zero ใน 5 นาทีได้ Benchmark น่าตกใจ SWE-bench 82 กว่า CyberGym 86 ARC-AGI-3 85 — ระดับใกล้ Claude Code Devin แต่ใช้ token ประมาณครึ่ง ทำไมสำคัญ ตลอดปีนี้ framework agent อย่าง LangGraph CrewAI AutoGen เพิ่ม abstraction layer เยอะขึ้น token bill พุ่งขึ้น NVIDIA มาบอกว่า pattern object-oriented Python เก่า 30 ปีนี่แหละพอ ประเด็นที่ต้องระวังคือ NOOA อยู่ v0.0.8 alpha ยัง production-ready ไม่ได้เต็มตัว async retry distributed tracing ยัง manual สำหรับ Enabridge platform สัญญาณคือถ้าคุณกำลังทำ orchestration layer ต้อง benchmark กับ NOOA ให้ได้ว่า overhead ที่เพิ่มมีคุณค่าอะไร ถ้าไม่มีก็จะโดน framework โคตร minimal แบบนี้กินเวลา
