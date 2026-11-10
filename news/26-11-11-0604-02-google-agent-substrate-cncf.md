---
date: 2026-11-10
slug: google-agent-substrate-cncf
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  Editorial isometric illustration of a vast server hall with glowing
  containers; a conveyor labeled "AGENT SUBSTRATE" moves stateful blue capsules
  into a warm nursery marked "WARM POOL — WAKE UNDER 1 SEC". Above the pool
  floats a tag "10X DENSITY". A ribbon labeled "DONATED TO CNCF" wraps around
  the whole hall. Dark teal and warm amber palette, clean vector style, crisp
  typography readable at 200px thumbnail. 1:1 aspect, no real human faces.
image: images/26-11-11-0604-02-google-agent-substrate-cncf.png
---

# Google ยก Agent Substrate กับ gVisor ให้ CNCF — เปิดสนาม runtime มาตรฐานของ stateful agent

## TL;DR
- Google donate **Agent Substrate** และ **gVisor** เข้า Cloud Native Computing Foundation (CNCF) — เริ่มจาก sandbox status — สองสัปดาห์ก่อน KubeCon NA 2026
- Agent Substrate บอกว่ารัน **millions of sandboxes ที่ density ~10x ของ standard container runtime** และปลุก stateful actor กลับมาได้ **ภายใน < 1 วินาที**
- เป็น runtime mastership move — Google เลือกเดิน open standard แทนขาย managed-only เพื่อกินตลาด agent runtime ที่กำลังโตก่อน AWS กับ Azure จะล็อค

## เกิดอะไรขึ้น
Google ประกาศเมื่อสัปดาห์แรกของพฤศจิกายน 2026 ว่ายก **Agent Substrate** (runtime สำหรับ stateful AI agent บน Kubernetes) และ **gVisor** (user-space kernel ที่ใช้ sandbox untrusted code) เข้า Cloud Native Computing Foundation. ตอน donate เข้าไปอยู่ที่ sandbox status — stage เริ่มต้นสำหรับ CNCF projects. OpenRL ก็ถูก donate มาด้วยในคราวเดียว

ตัว Agent Substrate เองเป็น open source ภายใต้ Apache 2.0 รันได้บน Kubernetes cluster ไหนก็ได้ (tuned สำหรับ GKE). ตัวเลขที่ Google claim: วิ่งได้หลายล้าน sandbox พร้อมกัน ที่ความหนาแน่น ~10x ของ container runtime มาตรฐาน; stateful actor ถูก pack ใส่ warm worker pool แล้วปลุกกลับมาได้ในเวลา sub-second. GA บน GKE ยังเป็น allowlist-only — จะต้องขอเข้าก่อน managed offering ค่อยเปิดกว้าง

วางคู่กับ **Agent Executor** (Google's distributed agent runtime, open source มาตั้งแต่ May 2026) และ **Agent Sandbox** (Kubernetes SIG Apps subproject ที่ใช้ gVisor isolate) — สามชิ้นนี้คือสูตร runtime stack ของ Google สำหรับ agent production workload: executor handle long-running loop, substrate pack state, sandbox isolate untrusted action

## ทำไมสำคัญ
สำหรับ Google นี่คือ textbook Kubernetes playbook ใช้ซ้ำ — ตอน Kubernetes Google ยกให้ CNCF แล้วกลายเป็นเจ้าของ container orchestration de facto. ตอนนี้กำลังทำแบบเดียวกันกับ agent runtime ก่อนที่ AWS (Bedrock AgentCore) และ Azure (ซึ่งเพิ่งประกาศ Imagine Enterprise กับ IBM วันเดียวกัน) จะสร้าง stack ของตัวเองที่ปิด

Agent runtime เป็นที่ที่ยังว่างจริง ๆ — ตลาด framework (LangGraph, CrewAI, AutoGen) โตเร็ว แต่ runtime layer ที่จัดการ state, scale, isolation ยังเป็น point solution รายคน. ถ้า Agent Substrate กลายเป็น "Kubernetes สำหรับ agent" ได้จริง framework ทุกตัวจะต้อง target compatibility กับมัน และ cloud รายอื่นจะเสียเปรียบที่ไม่ได้อยู่บน OSS stack เดียวกัน

จุดที่ต้องระวังคือ CNCF sandbox ≠ production-ready — ยังอีกไกลกว่าจะ graduate ถึง incubating แล้ว graduated. นอกจากนี้ความแตกต่างระหว่าง OSS Agent Substrate กับ managed version บน GKE ยัง fuzzy อยู่ — pattern "open core, managed moat" แบบเดียวกับที่ HashiCorp และ Elastic เคยเจอปัญหา

## มุม AI Agent Platform
- **Builders**: ถ้ากำลังทำ agent framework ตอนนี้ควรเริ่มทดสอบ deploy บน Agent Substrate — ถ้า standard นี้ชนะ framework ที่ทำ state management เองจะเสียเปรียบ. ส่วน builder ที่ทำ runtime tool (เช่น Temporal สำหรับ long-running workflow) จะต้องตัดสินใจว่าจะ integrate หรือ compete
- **Users / business** ที่ deploy agent: ก่อน commit กับ cloud runtime ใด cloud หนึ่ง (Bedrock AgentCore, Azure AI Foundry runtime) ลองพิจารณา portability — stack ที่อยู่บน Kubernetes + CNCF จะ portable กว่าในยาวนี้ โดยเฉพาะถ้าต้อง deploy on-prem หรือ hybrid
- **Ecosystem**: การ donate เข้า CNCF กดดัน AWS และ Azure ต้องเลือก — adopt Agent Substrate หรือสร้าง runtime มาตรฐานตัวเอง. ฝั่ง vendor สาย container (Red Hat, Rancher, Platform9) น่าจะได้แรงหนุนใหม่เพราะ agent runtime กลายเป็น Kubernetes workload ตามปกติ

## Sources
- [Sandboxing untrusted AI agents at scale (Google Open Source Blog, พ.ย. 2026)](https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html)
- [Agent Substrate now available on GKE (Google Cloud Blog)](https://cloud.google.com/blog/products/containers-kubernetes/agent-substrate-available-on-gke)
- [Google Donates Agent Substrate and gVisor to the CNCF (Let's Data Science)](https://letsdatascience.com/news/google-donates-agent-substrate-and-gvisor-to-the-cncf-254c44cc)

---

## Audio script
Google ส่งตัวจริงลงสนาม agent runtime. สัปดาห์นี้ Google donate โปรเจกต์ชื่อ Agent Substrate กับ gVisor เข้า Cloud Native Computing Foundation หรือ CNCF ก่อน KubeCon ที่กำลังจะมีถึง. Agent Substrate เป็น runtime สำหรับรัน agent แบบ stateful บน Kubernetes. Google บอกว่ารันได้ล้าน sandbox พร้อมกัน ที่ความหนาแน่นประมาณสิบเท่าของ container runtime มาตรฐาน. ปลุก actor ที่หลับอยู่ให้กลับมาทำงานได้ในเวลาไม่ถึงหนึ่งวินาที. เปิดเป็น Apache 2.0 รันบน Kubernetes cluster ไหนก็ได้ แต่ GA บน GKE ยังเป็น allowlist. ส่วน gVisor เป็น user space kernel ที่ Google ใช้ sandbox code ที่ไม่ไว้ใจ. ถ้าดูภาพใหญ่นี่คือ playbook เดียวกับที่ Google เคยทำกับ Kubernetes — ยกให้ CNCF แล้วกลายเป็นมาตรฐาน de facto. ตอนนี้กำลังพยายามทำกับ agent runtime ก่อน AWS Bedrock AgentCore กับ Azure stack จะปิดตลาด. มุมกับ builder — ถ้าทำ agent framework อยู่ควรเริ่มทดสอบบน Substrate แล้ว. มุมกับธุรกิจที่ deploy — ก่อน lock กับ cloud runtime ใดคลาวด์หนึ่ง ลอง evaluate stack ที่อยู่บน Kubernetes + CNCF ก่อน เพราะ portable กว่า. AWS กับ Azure ต้องตัดสินใจเร็ว ๆ ว่าจะ adopt หรือสร้างเอง
