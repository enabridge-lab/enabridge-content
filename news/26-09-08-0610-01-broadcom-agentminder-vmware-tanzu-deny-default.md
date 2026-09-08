---
date: 2026-09-08
slug: broadcom-agentminder-vmware-tanzu-deny-default
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial isometric illustration of a fortified data vault labeled
  "PRIVATE AI CLOUD"; in front of it a traffic-controller silhouette holds
  a glowing red gate stamped "DENY BY DEFAULT" while stacked labels behind
  read "ZERO API", "ZERO NETWORK", "ZERO MCP" — three small robot agents
  wait outside behind a yellow line. Muted navy and amber palette on a
  soft gradient ground, dramatic rim lighting, high contrast large text
  for a 200px thumbnail, 1:1 aspect, no real human faces.
image: images/26-09-08-0610-01-broadcom-agentminder-vmware-tanzu-deny-default.png
---

# Broadcom เปิด "AgentMinder" ที่ VMware Explore — Tanzu Platform วาง deny-by-default runtime สำหรับ agent, ตัด access API/network/MCP/internet ทั้งหมดจนกว่าจะ grant ทีละอัน

## TL;DR
- Broadcom เปิด **AgentMinder** ที่ VMware Explore 2026 (2 ก.ย.) — traffic-controller ระดับ enterprise ที่ควบคุม runtime + policy ของ AI agent ทั้ง portfolio; positioned เป็น **"official agent platform" ของ VMware Private AI Cloud**
- **Tanzu Platform for Agents** ใช้ **deny-by-default** — agent เริ่มด้วย **zero access** ต่อ API, network, MCP servers, internet; ต้อง grant ทีละ policy; credentials เก็บใน isolated store ที่ agent ไม่เห็นเลย → ปิด credential theft + prompt injection ในระดับ architecture
- GA fall 2026; positioning: **"private cloud = operating layer for enterprise AI"** — ตอบตรงข้าม hyperscaler-first playbook ของ Anthropic Claude Enterprise, Bedrock, Azure OpenAI
- Signal ใหญ่: enterprise vendor infrastructure (Broadcom) เข้าเป็นชั้น governance layer ของ agent — ไม่ใช่แค่ security tooling อีกแล้ว, แต่เป็น runtime primitive

## เกิดอะไรขึ้น

วันอังคารที่ Las Vegas, Broadcom เปิด VMware Explore 2026 ด้วยชุด announcement ที่ทะลุกรอบ virtualization vendor แบบเดิม — **VMware Private AI Cloud, VMware AI Factory, Tanzu Platform for Agents, AgentMinder, vDefend, Avi Load Balancer, TrueSource** วางรวมกันเป็น "operating layer for enterprise AI". launchhead ตัวเด่นที่สุดคือ **AgentMinder** — Broadcom ไม่เรียกว่า "AI security tool" หรือ "agent gateway" แต่เรียกว่า **"traffic controller for autonomous agents"** ที่บังคับให้ agent เดินตาม company rules + security standards ทุก call

ส่วนที่ทำให้ engineer หันหัวมองคือ architecture choice ของ **Tanzu Platform for Agents**. Broadcom เลือก **deny-by-default runtime** — agent ที่ deploy บน Tanzu **เริ่มด้วย zero access ต่อทุกอย่าง**: no API, no network egress, no MCP server, no internet — ต้อง grant ทีละ scope ผ่าน policy ก่อน agent ถึงจะเข้าถึง resource ได้. เสริมด้วย **isolated credential store** ที่ agent ไม่มี handle ตรงเลย — token ถูก injected เข้า outbound call แบบ side-channel — closing off both credential theft และ prompt injection ในระดับ architecture ไม่ใช่ pattern-matching detection

นี่คือ inverse ของ pattern ที่เห็นตลอดหนึ่งปีที่ผ่านมา ที่ vendor ปล่อย SDK แล้วบอกให้ developer configure security เอง. Broadcom pitch ตรงข้าม — **"agent เข้าถึงอะไรไม่ได้เลยจนกว่า admin จะสั่ง"**. Positioning นี้เข้ากับ enterprise mental model ของ VMware customers (banks, healthcare, government, defense) ที่โต้กับ zero-trust network ระดับ layer 3-4 อยู่แล้ว — แค่ยกกรอบเดียวกันขึ้นมาบน layer 7 ของ agent

Broadcom ประกาศ **GA ใน fall 2026** สำหรับ AgentMinder + Tanzu agent foundations. Chuck Robbins (CEO Broadcom หลัง VMware merger) ใน keynote pitch ว่านี่คือคำตอบสำหรับลูกค้าที่ **"อยาก deploy agent แต่ไม่ยอมให้ data ออกจาก perimeter"** — ตรงกับสิ่งที่ CISO ของ Fortune 500 พูดกันในปี 2026 ว่าไม่ต่อ SaaS AI agent ตรงกับ core system ของบริษัท

Announcement นี้ยัง double หน้าที่ให้ **VMware Cloud Foundation** — Broadcom ต้องการทำ VCF ให้เป็น "on-prem alternative" ต่อ AWS Bedrock, Azure OpenAI, Google Vertex AI สำหรับลูกค้าที่ regulated (financial services, healthcare, defense). ก่อนหน้านี้ VCF ต่อสู้กับ hyperscaler ด้วยเรื่อง cost + control; ตอนนี้ pitch ใหม่คือ **"agentic AI ต้องเดิน private cloud เพราะ hyperscaler ไม่ทำ deny-by-default ระดับ agent"**

## ทำไมสำคัญ

**Pattern ของสัปดาห์**: Broadcom (Tue), Tenable + Proofpoint (Wed) เปิด agent security product พร้อมกัน; CrowdStrike (สัปดาห์ก่อน) เปิด AI Partner Specialization — infrastructure + security vendor **converge บน category เดียวกัน** ในสัปดาห์เดียว. ไม่ใช่ coincidence — enterprise buyer พูดกับพวกเขาคำเดียวกันคือ **"เราจะ deploy agent ตอนไหน ถ้าไม่มี governance stack"**. ก่อน H1 2026 คำตอบคือ AI Gateway (Databricks, Cloudflare); ตอนนี้ layer ที่ขาดคือ **runtime containment + credential isolation** ซึ่ง Broadcom เดินเข้ามาเป็นเจ้าแรกที่ pitch แบบ integrated

Bet ที่น่าจับตาคือ **Cisco reaction ภายใน 30-45 วัน**. Cisco มี Splunk + Duo + AI Defense ในมือ; ถ้า Broadcom lock down Fortune 500 บน on-prem agent runtime ก่อน, Cisco จะต้อง response ที่ Cisco Live EMEA (ต.ค.) หรือ AWS re:Invent (พ.ย.). AWS เองก็ต้องตอบด้วยว่า Bedrock AgentCore runtime containment จะได้ deny-by-default policy layer เมื่อไหร่ — ตอนนี้ AgentCore มี "identity + memory + tools" แต่ยังไม่มี zero-trust runtime แบบ Tanzu

**Deep signal**: Broadcom describing agents as **"data they can trust + boundaries they can't cross"** — Robert Mee ของ InfoWorld อ้าง Broadcom exec — เป็น pitch ที่ compress AI safety discourse ของทั้ง 2025-2026 มาเป็น product statement ที่ CIO ซื้อได้. คำว่า "boundaries" replace "guardrail" ในสัปดาห์นี้ — subtle rebrand แต่สื่อให้เห็นว่า enterprise buyer ไม่ trust prompt-level guardrail อีกแล้ว, ต้อง network-level isolation

## มุม AI Agent Platform

**Builders**: ถ้าคุณสร้าง agent framework หรือ SDK, สัปดาห์นี้เป็นสัญญาณว่า **runtime portability กลายเป็น requirement**. agent ที่ deploy ได้แค่บน hyperscaler cloud จะ lose enterprise deal ให้ agent ที่ deploy บน on-prem Tanzu ได้. หมายความว่า framework ต้อง emit container image ที่ compatible กับ Kubernetes + policy annotation format ที่ AgentMinder อ่านได้ (น่าจะเป็น OPA/Rego หรือ Kyverno spec) — เตรียม support ตอน AgentMinder GA fall

**Users / business**: ลูกค้า enterprise ที่กำลัง evaluate agent platform ในไตรมาสหน้า จะเจอ AgentMinder + Tanzu เป็น "reference architecture" ที่ CISO ยอมให้ผ่าน. ผลกระทบตรง: **timeline agent deployment ใน regulated industry ยาวขึ้น** เพราะต้องรอ policy engine + credential store พร้อม แต่ **budget แต่ละ deal ใหญ่ขึ้น** เพราะรวม infra + runtime + gateway มาด้วย. B2B integration platform (Zapier, Make, workato) ที่ deploy cross-cloud จะ press ให้ต้อง publish deny-by-default profile

**Ecosystem**: MCP registry ต้องมี **"safe-to-deploy" flag** ในระดับ policy — Tenable + CrowdStrike + Broadcom กำลัง converge บน metadata schema เดียวกัน (identity, provenance, network scope, credential requirements). ใครที่เขียน MCP server public ควรเริ่มใส่ manifest field เหล่านี้ก่อน registry บังคับ

## Sources
- [StorageNewsletter — VMware Explore 2026: Broadcom Unveils AgentMinder, An Enterprise Solution for AI Agent Governance and Runtime Control](https://www.storagenewsletter.com/2026/09/02/vmware-explore-2026-broadcom-unveils-agentminder-an-enterprise-solution-for-ai-agent-governance-and-runtime-control/)
- [StorageNewsletter — VMware Explore 2026: Broadcom Introduces VMware Private AI Cloud](https://www.storagenewsletter.com/2026/09/02/vmware-explore-2026-broadcom-introduces-vmware-private-ai-cloud-enabling-enterprises-to-scale-ai-cost-effectively-operate-more-securely-and-innovate-rapidly/)
- [Broadcom Newsroom — Broadcom Unveils AI-Ready Data Foundations in VMware Tanzu Platform to Power Secure Enterprise AI Cloud](https://investors.broadcom.com/news-releases/news-release-details/broadcom-unveils-ai-ready-data-foundations-vmware-tanzu-platform)
- [InfoWorld — Broadcom says enterprise AI agents need two things: Data they can trust and boundaries they can't cross](https://www.infoworld.com/article/4216658/broadcom-says-that-enterprise-ai-agents-need-two-things-data-they-can-trust-and-boundaries-they-cant-cross.html)
- [theCUBE Research — VMware Explore 2026 Wrap-Up: Private Cloud Becomes the Operating Layer for Enterprise AI](https://thecuberesearch.com/vmware-explore-2026-wrap-up-private-cloud-becomes-the-operating-layer-for-enterprise-ai/)

---

## Audio script
วันอังคารที่ลาสเวกัส Broadcom เปิด VMware Explore 2026 ด้วยชุด announcement ที่ทะลุกรอบ virtualization vendor. launchhead ตัวเด่นชื่อ AgentMinder. Broadcom ไม่เรียกว่า security tool เรียกว่า traffic controller สำหรับ autonomous agent. บังคับ agent ให้เดินตาม company rule ทุก call.

ส่วนที่ทำให้ engineer หันหัวมองคือ Tanzu Platform for Agents. Broadcom เลือก deny by default runtime. agent เริ่มด้วย zero access ทุกอย่าง. ไม่มี API. ไม่มี network. ไม่มี MCP server. ไม่มี internet. ต้อง grant ทีละ policy. credential เก็บใน isolated store ที่ agent ไม่เห็น. token ถูก inject side channel. ปิด credential theft และ prompt injection ในระดับ architecture ไม่ใช่ pattern matching.

นี่คือ inverse ของ pattern ที่ vendor ปล่อย SDK แล้วบอกให้ developer configure security เอง. Broadcom pitch ตรงข้าม. agent เข้าถึงอะไรไม่ได้เลยจนกว่า admin จะสั่ง. ตรงกับ zero trust network ระดับ layer 3-4 ที่ enterprise บ่นมาแล้ว. แค่ยกกรอบเดียวกันขึ้นมาบน layer 7.

Broadcom ประกาศ GA fall 2026. Chuck Robbins pitch ว่าเป็นคำตอบสำหรับลูกค้าที่อยาก deploy agent แต่ไม่ยอมให้ data ออกจาก perimeter. VMware Cloud Foundation กำลังจะกลายเป็น on prem alternative ต่อ Bedrock Azure OpenAI Vertex สำหรับ regulated industry.

Pattern ของสัปดาห์นี้. Broadcom วันอังคาร. Tenable กับ Proofpoint วันพุธ. CrowdStrike สัปดาห์ก่อน. Infrastructure vendor และ security vendor converge บน category เดียวกัน. คำตอบร่วมกันคือ enterprise buyer พูดคำเดียวกันว่าจะ deploy agent ตอนไหนถ้าไม่มี governance stack. layer ที่ขาดหลัง AI Gateway คือ runtime containment กับ credential isolation. Broadcom เป็นเจ้าแรกที่ pitch integrated.

Cisco น่าจะ response ภายใน สามสิบถึงสี่สิบห้าวัน. Cisco Live EMEA เดือนตุลาคม. AWS ต้องตอบว่า Bedrock AgentCore runtime containment จะได้ policy layer แบบ Tanzu เมื่อไหร่. ตอนนี้ AgentCore มี identity memory tool. ยังขาด zero trust runtime.

Signal ที่ compress ทั้ง discourse. คำว่า boundaries กำลังจะแทน คำว่า guardrail ในสัปดาห์นี้. subtle. แต่แสดงว่า enterprise buyer ไม่ trust prompt level guardrail อีกแล้ว. ต้อง network level isolation.

สำหรับ AI Agent Platform builder. runtime portability กลายเป็น requirement. agent ที่ deploy ได้แค่บน hyperscaler จะ lose enterprise deal. framework ต้อง emit container image กับ policy annotation ที่ AgentMinder อ่านได้. เตรียม support ก่อน GA fall.
