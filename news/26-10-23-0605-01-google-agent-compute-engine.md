---
date: 2026-10-22
slug: google-agent-compute-engine
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  An editorial isometric illustration of a vast glass data-center floor, filled with
  thousands of tiny glowing isolation cells — each cell a transparent microVM pod with
  a small agent silhouette inside, sealed off from its neighbors by a vertical light
  wall. In the foreground a single pod opens to reveal a shielded CPU chip labeled
  "TITANIUM IPU". Three stacked numbers float above: "200,000 AGENTS", "<0.5s
  SUSPEND", "ZERO SHARED SECRETS". A ribbon labeled "AGENT COMPUTE ENGINE" curls
  through the scene. Deep blue, Google-red accent, high contrast for 200px thumbnails,
  1:1 aspect, no real human faces.
image: images/26-10-23-0605-01-google-agent-compute-engine.png
---

# Google เปิด Agent Compute Engine — microVM ต่อ 1 agent, Titanium IPU กันขาด, ขายอินฟราที่รัน Gemini ของตัวเองให้คนอื่น

## TL;DR
- **22 ต.ค.** Google ประกาศ **Agent Compute Engine (ACE)** ที่งาน Linux Foundation **AGNTCon + MCPCon** ซานโฮเซ — บริการ compute ที่ให้ **AI agent 1 ตัวได้ microVM 1 ตัว** พร้อม hardware-isolated boundary. ตัวเดียวกับที่ Google ใช้รัน Gemini agent ภายใน ยังไม่ GA — preview บน Google Cloud "ไม่กี่เดือนข้างหน้า"
- **สถาปัตยกรรมความปลอดภัย**: Cloud Hypervisor isolation, guest kernel แยก, **ไม่มี secret อยู่บน disk หรือ memory**, session-scoped identity อายุสั้น, ไม่มี VPC/IP gateway ปกติ — traffic ลอดผ่าน virtio-vsock → local proxy. physical host เป็น **stateless immutable appliance** rootfs read-only. ชิป **Titanium IPU** ของ Google คือ silicon-rooted defense
- **Scale**: Google อ้าง benchmark ของตัวเอง **200,000 agent** พร้อม suspend/resume ต่ำกว่า 0.5 วินาที (vendor-reported, ยังไม่มี third party reproduce) จับคู่กับ **Agent Substrate** — Kubernetes runtime open-source
- **Governance extend**: Agent Gateway + Agent Registry + Agent Identity ขยายไปที่ ACE, Cloud Run, GKE — Google จงใจทำให้ identity + registry layer เป็น horizontal ทั้ง stack
- **คู่แข่งตรง**: **AWS Bedrock AgentCore** ที่ให้ microVM ต่อ session เหมือนกัน, cap 8 ชั่วโมง — hyperscaler ทั้งสองเจ้าตัดสินใจพร้อมกันว่า "agent runtime คือ layer ที่ขาย"

## เกิดอะไรขึ้น

วันพฤหัสที่ **22 ต.ค.** ที่ AGNTCon+MCPCon ของ Linux Foundation ในซานโฮเซ, Google Cloud ประกาศ **Agent Compute Engine** — บริการ compute ที่ออกแบบมาเฉพาะสำหรับรัน AI agent, ไม่ใช่ containerize แอป CRUD ทั่วไป. จุดเริ่มของเรื่องน่าสนใจ: Google **ไม่ได้สร้างของใหม่** — Agent Compute Engine คือ **อินฟราชุดเดียวกับที่ Google ใช้รัน Gemini agent ของตัวเอง** ภายใน, และตอนนี้ Google ตัดสินใจเปิดขายให้ลูกค้าภายนอก. เหมือนตอน AWS ตัดสินใจเปิดขาย EC2 ที่ Amazon ใช้รัน retail ของตัวเอง — การประกาศแบบนี้ส่งสัญญาณชัดว่า Google เชื่อว่า agent runtime คือ **บริการระดับ platform ที่จะมี demand พอให้ขาย** ไม่ใช่แค่ชั้น software ที่ wrap LLM

Design decision ที่สำคัญคือ **microVM per agent, hardware-isolated**. ทุก agent ที่รันบน ACE ได้ Cloud Hypervisor boundary ของตัวเอง, มี guest kernel แยก, root access ของตัวเอง ภายใน sandbox — ไม่ใช่ container ที่แชร์ kernel. ที่สำคัญกว่าคือ **secret handling**: ตามรายงานของ The New Stack กับ the-decoder, sandbox ไม่เก็บ secret บน disk หรือ memory, ใช้ **session-scoped identity ที่อายุสั้น** — จบ session, identity หายไป. traffic ของ agent ไม่มี virtual network interface, ไม่มี default IP gateway, ไม่มี VPC access ปกติ — ต้องลอดผ่าน **virtio-vsock channel** ไปยัง local proxy, แล้วค่อยออก external proxy อีกชั้น. physical host runs as a **stateless, immutable appliance** ที่มี read-only root filesystem. ชิป **Titanium IPU** (Infrastructure Processing Unit) ของ Google เอง เป็น silicon-rooted defense layer

Google เปิดเผย benchmark ภายใน: **200,000 agents พร้อมกัน**, suspend-resume ต่ำกว่า **0.5 วินาที**. ตัวเลขนี้มาจาก Google เอง, ยังไม่มี third party ทำซ้ำ — The New Stack ชี้ประเด็นนี้ตรง ๆ ("vendor-reported figures, not yet independently reproduced"). จับคู่กับ **Agent Substrate** — Kubernetes runtime ที่ Google เปิด open source สำหรับ orchestrate agent workload. ส่วน governance layer เดิมของ Google — **Agent Gateway, Agent Registry, Agent Identity** — จะขยายไปที่ ACE, Cloud Run และ GKE ด้วย, ทำให้ identity + registry layer เป็น horizontal plane เดียวทั้ง compute stack

## ทำไมสำคัญ

สัญญาณจริงของข่าวนี้ไม่ใช่ "ตัวเลข 200K" หรือ "sub-half-second suspend" — มันคือ **การตัดสินใจว่า agent runtime คือ layer ที่ hyperscaler ขายได้โดยตรง**. ก่อนหน้านี้ปีกว่าที่ผ่านมา, agent runtime ส่วนใหญ่ "แฝง" อยู่ใน SaaS layer: Salesforce Agentforce, Microsoft Copilot Studio, Oracle Agent Studio — ทุกเจ้า wrap runtime ใต้ product. แต่ ACE + AWS Bedrock AgentCore ที่ออกมาในกรอบเวลาใกล้กันหมายถึง hyperscaler สองเจ้าใหญ่สุดเลือกเดินสายขนาน: ขาย **"compute สำหรับ agent"** เป็น primitive แยก, คนละ bucket กับ VM/container/serverless เดิม. นี่คือสัญญาณว่า **agent workload แตกต่างพอจาก web/batch workload** จนต้องมี compute category ของตัวเอง — ที่สำคัญคือเพราะมันต้องการ **sandbox strictness ระดับ hardware** (agent ตัวหนึ่งเขียน code ของตัวเอง, call tool, ขอ internet access, สามารถ compromise ได้ง่ายกว่า container ทั่วไป)

Pattern อีกชั้นที่น่าสังเกต: **Google เลือกเปิด Agent Substrate เป็น open source** คู่ไปกับ ACE ที่เป็น commercial service. การเดินแบบนี้คือ playbook ที่ Google ใช้เสมอ — Kubernetes เองก็เริ่มจาก Borg ภายใน, open source แล้วขาย GKE ทับ. การเปิด Substrate ให้ชุมชนหมายความว่า Google กำลังพยายามทำให้ **Kubernetes-sized primitive สำหรับ agent** กลายเป็น de facto standard — ถ้ามันกลายเป็นมาตรฐาน, Google มี head start ของการเป็น "AWS ของ agent compute" บน open layer เดียวกัน. AWS AgentCore ยัง closed, Microsoft Copilot Runtime ยังไม่แยกออกจาก Studio — Google กำลัง bet ว่า openness ที่ runtime layer จะชนะเหมือนที่ชนะใน container

**Isolation guarantee ที่แรง** คือจุดที่ ACE แตกต่างชัด: ไม่มี secret บน disk, ไม่มี VPC default, immutable host, hardware root of trust — มาตรฐานนี้ตรงกับที่ regulated industry (finance, healthcare, defense) ต้องการจะ deploy agent ที่จับข้อมูลสำคัญ. ถ้า compliance team ที่ธนาคารขอ "proof of isolation ของ agent ที่อ่าน PII ของลูกค้า", ACE มีคำตอบใน slide เดียว; container-based agent ทั่วไปตอบไม่ได้

## มุม AI Agent Platform

**Builder**: ถ้าคุณสร้าง agent framework (LangGraph, CrewAI, AutoGen, Semantic Kernel) หรือ orchestration layer, ACE/AgentCore เปลี่ยนสมการ build vs buy ของ runtime infrastructure. ก่อนหน้านี้ framework ส่วนใหญ่ต้องมี "execution environment" ของตัวเอง (บ่อยครั้ง Docker container ธรรมดา) — ตอนนี้มี managed primitive ที่ hardware-isolated พร้อมใช้. framework ที่ **compile ลง microVM primitive ได้โดยตรง** จะมี distribution advantage. ที่ไม่พูด Agent Substrate / AgentCore protocol จะต้องมี wrapper layer เพิ่ม

**User / business**: ถ้าคุณ deploy agent ที่ production ที่จับข้อมูล sensitive — session-scoped identity, hardware isolation, no-secret-on-disk ของ ACE เป็นการเปลี่ยนภาษาที่ security team คุยกับ app team ได้. ก่อนหน้านี้ security team บล็อก agent บ่อยเพราะอธิบาย threat model ไม่ได้ ("agent รัน code อะไร? อ่าน memory ของ agent อื่นได้ไหม?"); ACE มี default answer. **ค่าใช้จ่ายและ lock-in** คือ trade-off — microVM ต่อ agent **แพงกว่า container หลายเท่า**, และ Agent Gateway/Registry/Identity ของ Google จะ bind workload เข้า Google Cloud แน่น

**Ecosystem**: AWS vs GCP vs Azure ตอนนี้ไม่ใช่เรื่อง LLM endpoint อีกต่อไป — ปี 2027 จะเป็นเรื่อง **agent runtime + identity + governance stack**. ใครมี isolation + identity + registry ที่ complete ที่สุด จะ win regulated workload. protocol ชั้นระหว่าง (MCP + A2A) ยังคง neutral, แต่ compute ข้างล่างกลายเป็นสนามแข่ง 3 เจ้าใหญ่. ที่ควรจับตา: **Oracle จะต้องเปิด vertical compute offering** คู่กับ Agent Studio for Industry (ข่าววันพุธ) หรือจะ cede runtime layer ให้ hyperscaler

## Sources
- [Google Cloud Blog: Introducing Agent Compute Engine and expanding agent governance](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance)
- [The New Stack: Google turns the infrastructure behind Gemini's agents into a cloud service](https://thenewstack.io/google-agent-compute-engine/)
- [The Decoder: Google's Agent Compute Engine gives every Gemini agent its own hardware-isolated micro virtual machine](https://the-decoder.com/googles-agent-compute-engine-gives-every-gemini-agent-its-own-hardware-isolated-micro-virtual-machine/)
- [Google Cloud Blog: Agent Compute Engine deep dive](https://cloud.google.com/blog/topics/ai-infrastructure/agent-compute-engine-deep-dive)

---

## Audio script
สวัสดีครับ วันนี้ Google เพิ่งเปิด Agent Compute Engine ที่งาน AGNTCon กับ MCPCon ซานโฮเซ — บริการ compute ที่ให้ AI agent 1 ตัวได้ microVM 1 ตัว แยก hardware ของตัวเอง ตัวเดียวกับที่ Google ใช้รัน Gemini agent ภายใน ตอนนี้ตัดสินใจเปิดขายให้คนภายนอก ยังไม่ GA preview ใน Google Cloud อีกไม่กี่เดือน จุดที่น่าสนใจคือ security architecture ของมัน — ไม่มี secret อยู่บน disk หรือ memory ใช้ session-scoped identity อายุสั้น traffic ไม่มี VPC ปกติ ลอดผ่าน virtio-vsock แล้วค่อยออก proxy อีกชั้น physical host เป็น stateless immutable appliance read-only filesystem Google อ้างว่ารันได้ 200,000 agent พร้อมกัน suspend-resume ต่ำกว่าครึ่งวินาที ตัวเลขจาก Google เอง ยังไม่มี third party ทดสอบซ้ำ จับคู่กับ Agent Substrate ที่เปิด open source ทำไมเรื่องนี้สำคัญ เพราะมันหมายความว่า Google ตัดสินใจว่า agent runtime คือ layer ที่ hyperscaler ขายได้โดยตรง ตามหลัง AWS Bedrock AgentCore ที่ทำแบบเดียวกัน ก่อนหน้านี้ agent runtime แฝงอยู่ใน SaaS ของ Salesforce Oracle Microsoft — ตอนนี้ Google กับ AWS บอกชัดว่า agent compute เป็น primitive ของตัวเอง คนละ bucket กับ container กับ VM ปี 2027 สนามแข่ง cloud ไม่ใช่ LLM endpoint แล้ว เป็น runtime กับ identity กับ governance stack ครับ
