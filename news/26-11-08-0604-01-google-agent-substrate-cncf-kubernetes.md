---
date: 2026-11-07
slug: google-agent-substrate-cncf-kubernetes
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  An editorial isometric illustration of a giant glass server room where
  hundreds of tiny glowing cubes labeled "AGENT" float in neat rows, each
  cube wrapped in a thin blue security ring marked "microVM". A big banner
  on the back wall reads "10X DENSITY"; another banner nearby reads "500ms
  WAKE". The CNCF cloud logo hovers above the room with a ribbon that says
  "DONATED". The Google G sits small in a corner, handing a scroll to a
  neutral white-robed figure holding a Kubernetes helm. Clean editorial
  style, soft turquoise and warm orange palette, 1:1 aspect, high contrast
  so the numbers stay readable at 200px thumbnail, no real human faces
  (silhouettes OK).
image: images/26-11-08-0604-01-google-agent-substrate-cncf-kubernetes.png
---

# Google ยก Agent Substrate + gVisor ให้ CNCF — เดิมพันว่า agent runtime จะเป็น "Kubernetes ตัวถัดไป"

## TL;DR
- Google บริจาค Agent Substrate, gVisor และ OpenRL เข้า CNCF Sandbox ที่ KubeCon NA — ตั้งใจให้เป็น industry standard แบบที่ Kubernetes เคยเป็นกับ container
- Agent Substrate snapshot agent session ไป storage ได้ แล้ว restore ใน 500ms — ทำให้ density สูงกว่า standard container runtime 10 เท่า
- GKE Agent Sandbox เป็น GA แล้ว, agent compute engine ให้ microVM ต่อ agent ทุกตัว — governance stack (Gateway + Registry + Identity) ครบในวันเดียว

## เกิดอะไรขึ้น
วันที่ 5 พฤศจิกายนที่ KubeCon North America ใน Salt Lake City, Drew Bradstock, VP of Kubernetes and orchestration ของ Google Cloud, ประกาศบริจาคโครงการโครงสร้างพื้นฐาน agent 3 ตัวให้ CNCF: **Agent Substrate**, **gVisor** และ **OpenRL** — ทั้งหมดเข้า sandbox tier ของมูลนิธิ ซึ่งเป็นด่านแรกสู่ "graduated" status แบบที่ Kubernetes, Prometheus, และ Envoy เคยเดินผ่าน

Agent Substrate คือ runtime ที่ snapshot ทั้ง state ของ agent (memory, open file handles, คอนเท็กซ์ tool call ที่ค้างอยู่) ลง storage ได้เลย แล้ว restore กลับใน 500 มิลลิวินาที — ประเด็นคือ agent ส่วนใหญ่ "waiting" มากกว่า "computing" (รอ LLM, รอ tool call, รอ user approve) ดังนั้นถ้า pause ลง disk ได้ระหว่างรอ จะวาง agent ต่อ node ได้เยอะกว่า container ปกติเป็น 10 เท่า ตาม paper internal ของ Google — นี่คือ math ที่เปลี่ยน unit economics ของ agent platform ได้เลย

ควบคู่กันคือ **Agent Compute Engine** (เปิดตัวที่ AGNTCon 22 ตุลาคม แต่ขยาย GA ในสัปดาห์นี้) — ให้แต่ละ agent รันใน hardware-isolated microVM ของตัวเอง, ได้ SPIFFE certificate + short-lived identity token, ไม่มี user credential เข้ามาใน VM เลย Governance stack เต็มสมบูรณ์: **Agent Gateway** (validate delegation + apply DLP policies), **Agent Registry** (catalog ของ plugins/skills/MCP servers/A2A agents ที่ admin อนุมัติ), **Agent Identity** (4 identity ต่อ agent) — ทุกตัว Google บอกว่าจะรองรับ cross-cloud รวม on-prem และ coding agent อย่าง Claude Code บน managed device

Caveat: GitHub README ของ Agent Substrate ยังขึ้น "pre-1.0" ขณะที่ Google ปล่อยข่าวว่า 1.0 แล้ว, และ limitation ที่ document ไว้คือยังไม่มี GPU passthrough, ไม่มี live CUDA snapshot, และ dropped open connections เมื่อ suspend — ดังนั้น workload ที่พึ่ง GPU state เยอะยังทำไม่ได้ในรุ่นแรก

## ทำไมสำคัญ
การยก Agent Substrate เข้า CNCF ไม่ใช่ท่า charity — Google กำลังเล่นสคริปต์เดียวกับที่ตัวเองเคยใช้กับ Kubernetes: ปล่อยของให้เป็น neutral standard เพื่อให้ ecosystem ลงทุนพัฒนา operator / hosting / tooling รอบมัน แล้วตัวเอง (GKE) ขายเป็น "managed version ที่ดีที่สุด" เหนือ layer นั้น Pattern นี้ชนะมาแล้วกับ container — คำถามคือ 2027-28 นี้มันจะ repeat กับ agent runtime ไหม

Density 10x มีผลโดยตรงกับ margin ของทุก agent platform — ถ้าคุณขาย agent seat $50/user/เดือนและ host บน runtime ปกติ COGS ต่อ agent คือ compute idle ที่รอ LLM/tool — การเปลี่ยนไป runtime ที่ pause-to-disk ได้ แปลว่ากำไรต่อ seat เพิ่มทันที หรือราคาลดได้โดยไม่กระทบ margin — นี่คือเหตุผลที่ Agent Substrate จะมีคนลงทุน contribute เร็ว

AWS กับ Azure ต้องเลือก: (1) adopt Agent Substrate เหมือนเคย adopt Kubernetes ซึ่งทำให้ Google ยืนที่ชั้นประโยชน์ที่สุดในการ monetize มัน (2) ทำของตัวเองคู่ขนาน ซึ่งแบ่ง ecosystem เหมือน Nomad vs Kubernetes เมื่อ 10 ปีก่อน (จบลงที่ Kubernetes ชนะ) ประวัติศาสตร์บอกว่าการ fork ล่าช้ากว่า standard แรงดึงดูด economic ของ 10x density จะดึงทุก hyperscaler ให้ compat ในที่สุด

## มุม AI Agent Platform
**Builders** — ถ้าคุณกำลังสร้าง agent framework (LangGraph, CrewAI, Mastra, Vercel AI SDK) คุณต้องตอบคำถามว่า runtime layer ของคุณจะ compat กับ Agent Substrate ไหม — ถ้าไม่ เท่ากับส่ง customer ให้คู่แข่งที่ host บน GKE/EKS/AKS ได้ cheaper เพราะ density สูงกว่า อีกมุมคือ pause-to-disk model เปลี่ยน design ของ long-running agent — คุณไม่ต้อง optimize memory footprint เพื่อให้ agent "nice to node" อีกต่อไป เพราะ runtime จัดการเองได้

**Users / business** — องค์กรที่ deploy agent ควรกดดัน vendor ว่าจะ support Agent Compute Engine (หรือ equivalent) เมื่อไหร่ — governance stack ที่มาพร้อม (Gateway + Registry + Identity) คือสิ่งที่ 99% ของ enterprise ยังไม่มี ตามรายงาน SailPoint ล่าสุด แปลว่า buying lever ตอนนี้ไม่ใช่ model quality แต่คือ "ลูกค้าคุมได้ไหมว่า agent ตัวไหนเข้าได้ถึง data อะไร" Enabridge ที่สร้าง platform ให้ลูกค้าไทย ควร bake Agent Substrate / gVisor compat ลง roadmap 2027 ไม่ใช่ feature ต่างหาก — มันคือ cost of goods

**Ecosystem** — CNCF ได้ของใหญ่ ตัว protocol layer (MCP, A2A, ACP) ยังไม่มี neutral home แบบนี้ Anthropic ที่ steward MCP อยู่ อาจต้องคิดเรื่อง foundation donation เร็วกว่าเดิมเพื่อไม่ให้ Google control ทั้ง stack

## Sources
- [Open infrastructure for autonomous agents comes to CNCF (Google Cloud Blog)](https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf)
- [Sandboxing Untrusted AI Agents at Scale: Google Donates Agent Substrate and gVisor to the CNCF (Google Open Source Blog)](https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html)
- [Kubernetes, mark II? Why Google's giving away gVisor (The New Stack)](https://thenewstack.io/gvisor-cncf-kubernetes-open-source/)
- [Agent Compute Engine deep dive (Google Cloud Blog)](https://cloud.google.com/blog/topics/ai-infrastructure/agent-compute-engine-deep-dive)
- [Google Donates AI Agent Sandbox to Linux Foundation's CNCF; Agent Substrate Lacks GPU Passthrough (TechTimes)](https://www.techtimes.com/articles/330163/20261106/google-donates-ai-agent-sandbox-linux-foundations-cncf-agent-substrate-lacks-gpu-passthrough.htm)

---

## Audio script
Google ประกาศที่ KubeCon North America วันที่ 5 พฤศจิกายน บริจาคโครงการโครงสร้างพื้นฐาน agent สามตัวให้ CNCF ซึ่งเป็นมูลนิธิเดียวกับที่ดูแล Kubernetes สามตัวนี้คือ Agent Substrate, gVisor และ OpenRL ทั้งหมดเข้า sandbox tier ของ CNCF Agent Substrate คือ runtime ที่ snapshot state ของ agent ลง storage ได้ แล้ว restore กลับใน 500 มิลลิวินาที จุดสำคัญคือ agent ส่วนใหญ่รอ ไม่ได้ compute ดังนั้นถ้า pause ลง disk ได้ระหว่างรอ จะวาง agent ต่อ node ได้เยอะกว่า container ปกติเป็น 10 เท่า ซึ่งเปลี่ยน unit economics ของ agent platform ได้เลย ข่าวควบคู่คือ Agent Compute Engine ให้แต่ละ agent รันใน microVM ของตัวเอง มี governance stack ครบ ประกอบด้วย Agent Gateway Agent Registry และ Agent Identity ทำไมมันสำคัญ Google กำลังเล่นสคริปต์เดิมกับที่ชนะ Kubernetes ปล่อยของให้เป็น neutral standard ให้ ecosystem ลงทุนรอบมัน แล้วตัวเองขาย GKE เป็น managed version ที่ดีที่สุด AWS กับ Azure ต้องเลือกว่าจะ adopt หรือ fork แรงดึงดูด economic ของ 10x density จะดึงทุก hyperscaler ให้ compat ในที่สุด สำหรับคนที่สร้าง agent platform ต้อง bake Agent Substrate compat ลง roadmap เพราะมันจะเป็น cost of goods ไม่ใช่ feature ต่างหาก สำหรับ Anthropic ที่ดูแล MCP อาจต้องคิดเรื่อง foundation donation เร็วกว่าเดิมเพื่อไม่ให้ Google control ทั้ง stack
