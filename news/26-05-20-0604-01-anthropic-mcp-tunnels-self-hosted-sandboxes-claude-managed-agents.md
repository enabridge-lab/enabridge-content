---
date: 2026-05-20
slug: anthropic-mcp-tunnels-self-hosted-sandboxes-claude-managed-agents
topic: agentic-ai
reading_time_min: 4
sources: 6
image_prompt: A sleek enterprise data center cross-section in editorial isometric style — left half a dark glass corporate vault holding glowing internal databases, knowledge bases, and ticketing systems labeled "INTERNAL"; right half Anthropic's signature warm cream studio with a luminous Claude orchestration core. Between them, a single bright encrypted tunnel labeled "MCP TUNNEL" arcs from the vault outward, with a smaller floating sandbox box labeled "SELF-HOSTED SANDBOX" hosting tool icons for Cloudflare, Daytona, Modal, Vercel. A bold headline billboard floats above reading "Claude Managed Agents" with three stacked numbers: "ZERO PUBLIC ENDPOINTS", "PRIVATE NETWORK", "BYO COMPUTE". Dramatic rim lighting in coral and deep teal, ultra-sharp text rendering, high contrast for 200px thumbnail readability, 1:1 aspect, tech-magazine cover style, no real human faces.
image: images/26-05-20-0604-01-anthropic-mcp-tunnels-self-hosted-sandboxes-claude-managed-agents.png
---

# Anthropic เปิด MCP Tunnels + Self-Hosted Sandboxes — ดัน Claude Managed Agents เข้า private network ของ enterprise โดยไม่ต้องเปิด firewall

## TL;DR
- 19 พ.ค. ที่ "Code with Claude" London — Anthropic เปิด 2 ฟีเจอร์ปิด gap ใหญ่ของ Claude Managed Agents: **MCP Tunnels** (research preview) ให้ agent ต่อ MCP server หลัง firewall ได้โดยไม่ต้องเปิด public endpoint และ **Self-Hosted Sandboxes** (public beta) ย้าย tool execution ไปอยู่บน infra ลูกค้าหรือ Cloudflare/Daytona/Modal/Vercel
- Architecture แยกหน้าที่ชัด: orchestration loop + context management อยู่บน Anthropic; tool execution + data access อยู่ฝั่งลูกค้า — แก้โจทย์ใหญ่ที่สุดของ enterprise procurement (data residency + network isolation)
- Move นี้บอกชัดว่า Anthropic ไม่แข่ง OpenAI ที่ consumer แต่ tap ตลาด enterprise governance — ตามหลัง PwC alliance (30K certified Claude users) + Anthropic Wall Street agents + Microsoft 365 integration

## เกิดอะไรขึ้น

19 พฤษภาคม 2026 ที่งาน Code with Claude — developer conference ครั้งแรกของ Anthropic ที่ London — บริษัทประกาศ 2 ฟีเจอร์ที่กว่าจะเข้าใจความหมายต้องอ่าน architecture diagram. **MCP Tunnels** เปิดให้ Claude Managed Agents (และ Messages API) ต่อกับ MCP server ที่อยู่หลัง corporate firewall โดยไม่ต้องเปิด public endpoint. กลไกคือ lightweight gateway วิ่ง outbound connection เดียวจาก private network ไปยัง Anthropic, end-to-end encrypted, ไม่ต้อง configure inbound firewall rule. แปลว่า agent ที่ทำงานบน Anthropic infrastructure สามารถ "เข้าถึง" internal database, ticketing, knowledge base ของลูกค้าได้ราวกับอยู่ใน VPN เดียวกัน — โดย IT ไม่ต้องเปิดรู

**Self-Hosted Sandboxes** ทำงานคู่กัน แต่แก้คนละโจทย์. เดิม Claude Managed Agents รัน tool execution บน Anthropic sandbox (เช่น code execution, browser automation, file ops). ฟีเจอร์ใหม่ย้าย execution layer ทั้งหมดไปฝั่งลูกค้า — รันบน VM ของตัวเอง, หรือผ่าน managed provider อย่าง Cloudflare, Daytona, Modal, Vercel. ลูกค้าควบคุม resource sizing + runtime image + capacity ของ workload. เปิด public beta แล้ว — ส่วน MCP Tunnels ยัง research preview

จุด design ที่สำคัญที่สุดคือ **การแยก orchestration จาก execution**. Agent loop, context management, error recovery ยังคงอยู่บน Anthropic — เพราะนั่นคือส่วน "smart" ที่ Claude ทำได้ดี และ Anthropic ต้องเก็บข้อมูลใช้ปรับ model. ส่วน tool execution + data access ที่ติดปัญหา compliance, data residency, security review — ปล่อยให้ลูกค้าจัดการเอง. นี่คือ architectural pattern ที่ทำให้ enterprise สูง regulation (bank, hospital, telco) ยอม sign deal — เพราะ data ไม่เคยออกจาก premises แต่ยังได้ intelligence ของ frontier model

ก่อนหน้านี้ — Claude Managed Agents เปิดตัวเมื่อ Anthropic ประกาศ "deployment company" model ในช่วงต้นปี + เร่งสกัด enterprise revenue. ตัวเลขรอบล่าสุดที่เห็น: PwC alliance certify Claude สำหรับ 30,000 consultants, Anthropic หัวหอกเข้า Wall Street ด้วย 10 pre-built agent (5 พ.ค.), integration เต็มกับ Microsoft 365 (Excel/Word/PowerPoint/Outlook beta) + partnership ข้อมูลกับ Moody's, S&P, FactSet. การเพิ่ม MCP Tunnels + Self-Hosted Sandboxes คือชิ้นต่อเนื่อง — Anthropic กำลัง assemble enterprise stack ที่ครบกว่า OpenAI

## ทำไมสำคัญ

นี่คือ **inflection point ของ MCP จาก spec สู่ enterprise infrastructure layer**. ปีที่แล้ว MCP โต public registry แตะ 9,400 server + adoption ใน production team แตะ 78% (Cdata, การประมาณ 2026). แต่ทุกคนเจอกำแพงเดียวกัน — internal MCP server ที่เก็บข้อมูลจริง (CRM, ERP, ticketing) เปิดออก public ไม่ได้, ใช้ VPN ก็ปวดหัว, ใส่ DMZ ก็ต้องไป security review. Anthropic ปลดล็อกด้วย tunnel pattern ที่ลูกค้าไม่ต้องเปิด port. นี่คือ pattern ที่ Cloudflare Tunnel เคยทำให้ web — เพียงแต่ตอนนี้ Anthropic ทำให้ agent

มอง 6-12 เดือนข้างหน้า — เราจะเห็น **architectural divergence ของ enterprise AI 2 ค่าย**. ค่าย OpenAI/Dell ที่ประกาศ partnership เมื่อ 18 พ.ค. — ย้าย model + agent ไปอยู่บน on-prem hardware (Codex on Dell AI Factory). ค่าย Anthropic — เก็บ model + orchestration ไว้ที่ตัวเอง แต่ extend tentacle ไป private network ของลูกค้าผ่าน tunnel + sandbox. ทั้ง 2 ค่ายแก้โจทย์เดียวกัน (data ไม่ออก premises) ด้วย philosophy ตรงข้าม — OpenAI bring model to data, Anthropic bring data path to model. ใครชนะขึ้นกับว่า enterprise CIO เชื่อ provider แค่ไหน + workload latency-sensitive ขนาดไหน

อีก signal สำคัญ — **MCP กำลังเป็น control point ที่ทุก vendor ต้อง claim**. Cloudflare เพิ่งเปิด enterprise MCP reference architecture, Microsoft Copilot Studio เปลี่ยนตัวเองเป็น "AI agent control center" (14 พ.ค.), Devenex เปิดที่ Google Cloud Next 2026 เป็น execution control plane. การที่ Anthropic เข้ามาเล่นใน infra layer (ไม่ใช่แค่ application) เป็นการประกาศว่า model vendor ไม่พอใจที่จะอยู่หลัง API — ต้องครอบ orchestration + connectivity ด้วย. ระยะยาว — model + protocol + execution layer จะ converge ไปอยู่ใต้ vendor เดียวกัน (vertical integration คือ winning play)

## มุม OpenBridge

ตรงเข้า kill zone. OpenBridge ขาย integration backbone ที่ enterprise ใช้ต่อระบบ — ตอนนี้ Anthropic เพิ่งเปิด primitive ที่ครอบ use case นั้นได้แล้ว. ถ้า MCP Tunnel + Self-Hosted Sandbox ออก GA ภายใน Q3 — ลูกค้า Thai bank ที่กำลัง pilot Claude อาจไม่ต้อง buy connector layer แยกแล้ว เพราะ Anthropic แถมให้ฟรีใน contract. นี่คือ commoditization risk ระดับสูงสุดที่ OpenBridge ต้องอ่านตา

มอง defensive — sweet spot ที่ Anthropic ครอบไม่ถึงคือ **certified vertical connector + compliance audit pattern ที่ map กับ regulator ไทย/SEA**. Anthropic เปิด tunnel แต่ลูกค้า bank/insurance ต้องการ connector ที่ผ่าน BOT IT Security Framework, MAS Technology Risk Management, BNM RMiT — ไม่ใช่แค่ generic SOC 2. OpenBridge มี window 6-9 เดือนสร้าง **"BOT-certified MCP server library"** ที่ wrap CIMB/KBank/SCB API + Telco BSS/OSS + hospital HIS + government API (กรมที่ดิน, สรรพากร, ป.ป.ง.) แล้ว package เป็น "drop-in" สำหรับ Claude/ChatGPT/Gemini agent. นี่คือ niche ที่ frontier lab ไม่มี local team + ไม่มี time-to-market มาแข่ง

อีก opportunity — **MCP gateway + observability sidecar**. Anthropic เปิด tunnel เพื่อให้ agent ต่อ MCP server แต่ไม่ได้ให้ tooling จัดการ tunnel เอง (rate limit, policy enforcement, audit trail per agent, redaction, fine-grained ACL). OpenBridge สามารถสร้าง gateway ที่ sit อยู่ระหว่าง Anthropic tunnel endpoint กับ internal MCP server — เก็บ log + enforce policy + redact PII ก่อน data ไหลออก. position ตัวเองเป็น "MCP firewall" ที่ทุก Tier-1 enterprise ต้องการ — และเป็น control point ที่ทำให้ contract OpenBridge ไม่ถูก Anthropic ครอบในรอบหน้า

## Sources
- [New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels (Anthropic)](https://claude.com/blog/claude-managed-agents-updates)
- [Anthropic debuts MCP tunnels and self-hosted sandboxes to lock down AI agent infrastructure (The New Stack)](https://thenewstack.io/anthropic-mcp-tunnels-sandboxes/)
- [Anthropic adds self-hosted sandboxes and MCP tunnels to Claude Managed Agents (The Decoder)](https://the-decoder.com/anthropic-adds-self-hosted-sandboxes-and-mcp-tunnels-to-claude-managed-agents/)
- [Anthropic Introduces MCP Tunnels for Private Agent Access to Internal Systems (InfoQ)](https://www.infoq.com/news/2026/05/claude-mcp-tunnels/)
- [Anthropic enhances Claude Managed Agents with two new privacy and security features (9to5Mac)](https://9to5mac.com/2026/05/19/anthropic-enhances-claude-managed-agents-with-two-new-privacy-and-security-features/)
- [Anthropic Expands Enterprise AI Strategy With Self-Hosted Sandboxes And MCP Tunnels (Metaverse Post)](https://mpost.io/anthropic-introduces-self-hosted-ai-agent-infrastructure-for-enterprise-customers/)

---

## Audio script
สวัสดีครับโย้ มาเล่าข่าวใหญ่ของวานนี้ Anthropic เปิด 2 ฟีเจอร์สำคัญใน Claude Managed Agents ที่งาน Code with Claude ครั้งแรกที่ลอนดอน ตัวแรกชื่อ MCP Tunnels เปิดให้ agent ต่อกับ MCP server ที่อยู่หลัง firewall ของลูกค้าได้ โดยลูกค้าไม่ต้องเปิด public endpoint ใด ๆ ใช้ outbound connection เดียวที่ encrypted end-to-end ตัวที่สองชื่อ Self-Hosted Sandboxes ย้าย tool execution ทั้งหมดไปอยู่ฝั่งลูกค้า รันบน VM ของตัวเองหรือผ่าน Cloudflare Daytona Modal Vercel ก็ได้

จุดที่สำคัญที่สุดคือ architecture แยกหน้าที่ orchestration loop กับ context management ยังอยู่บน Anthropic ส่วน data access กับ tool execution อยู่ฝั่งลูกค้าทั้งหมด แก้โจทย์ใหญ่ที่สุดของ enterprise procurement คือ data residency กับ network isolation ตอนนี้ banker insurance hospital regulator ของลูกค้า Anthropic ยอมเซ็นได้แล้วเพราะข้อมูลไม่ออกจาก premises

ทำไมสำคัญ ตอนนี้ MCP กำลังเปลี่ยนจาก spec เป็น enterprise infrastructure layer Anthropic ไม่ใช่เจ้าเดียวที่เคลื่อน Cloudflare เปิด enterprise MCP reference architecture Microsoft Copilot Studio เปลี่ยนตัวเองเป็น AI agent control center Devenex เปิดที่ Google Cloud Next OpenAI ไป Dell on-prem ทุก vendor พยายามครอบ orchestration กับ connectivity ไม่ใช่แค่อยู่หลัง API

มุม OpenBridge ตรงเข้า kill zone ถ้า MCP Tunnel ออก GA ใน Q3 ลูกค้า Thai bank ไม่ต้อง buy connector layer แยกแล้ว defensive play คือสร้าง BOT-certified MCP server library ที่ wrap KBank SCB CIMB กับ Telco BSS OSS hospital HIS แล้ว package ขายเป็น drop-in อีก angle คือสร้าง MCP gateway เป็น firewall อยู่ระหว่าง Anthropic tunnel กับ internal server เก็บ log enforce policy redact PII นี่คือ control point ที่ Tier-1 enterprise ต้องการครับ
