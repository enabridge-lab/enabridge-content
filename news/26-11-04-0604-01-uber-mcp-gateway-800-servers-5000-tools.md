---
date: 2026-11-03
slug: uber-mcp-gateway-800-servers-5000-tools
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  An editorial isometric illustration of a massive glass control-tower stamped
  "UBER MCP GATEWAY" at the center of a vast dark-navy data campus. Hundreds of
  tiny glowing server racks fan out below, converging through a single translucent
  pipe into the tower. Above the tower, a bold three-line counter reads
  "800+ MCP SERVERS", "5,000+ TOOLS", "10,000+ IDLs CRAWLED". A side panel
  shows a developer silhouette typing on a CLI labeled "aifx" that lights up
  a routing map. Deep navy and silver palette with Uber-black accents and
  neon-cyan trace lines, 1:1 aspect, strong contrast for 200px thumbnails,
  no real human faces.
image: images/26-11-04-0604-01-uber-mcp-gateway-800-servers-5000-tools.png
---

# Uber เปิด MCP Gateway — 800 server + 5,000 tool หลังประตูเดียว, agentic infrastructure เข้าสู่ยุค platform

## TL;DR
- Uber เปิดสถาปัตยกรรม **MCP Gateway** — ประตูกลางที่รวม **800+ MCP server** และ **5,000+ tool** สำหรับ AI agent ภายในบริษัทให้เรียกใช้ผ่าน control plane เดียว (InfoQ, Nov 2026)
- **AutoCrawler** บน Cadence สแกน IDL registry > **10,000 services** เพื่อ auto-generate tool definition — ทีมเจ้าของ service ไม่ต้องเขียน MCP server เอง
- แยก **MCP Registry** (control plane) ออกจาก **Proxy Gateway** (runtime) + authz 2 ชั้น (server + tool) ผ่านระบบ internal access control
- Coding agent เข้าถึงผ่าน CLI ภายในชื่อ **aifx** — ไม่ต้อง install MCP server บนเครื่อง developer
- Signal: MCP ย้ายจาก "protocol" เป็น "enterprise infra" — Uber คือ reference architecture แรกที่ production-grade เปิดตัวเลขได้ชัด

## เกิดอะไรขึ้น

สัปดาห์นี้ Uber Engineering เปิด deep dive เรื่อง **MCP Gateway** — ระบบ production ที่รวม MCP server ทั่วบริษัทไว้หลังชั้น proxy เดียว. InfoQ ยืนยันตัวเลข **800+ MCP server, 5,000+ tool** กำลังรันบน gateway ตัวนี้. ก่อนหน้านี้ Uber มี pattern เดียวกันกับที่หลายบริษัทเจอ: แต่ละทีมสร้าง MCP integration ของตัวเองทำให้ infra ซ้ำซ้อน, security ไม่สม่ำเสมอ, discoverability แย่, agent ผูกติดกับ service ตัวใดตัวหนึ่ง

Architecture ของ gateway แยกเป็นสองชั้นชัดเจน — **MCP Registry** เป็น control plane (เก็บ metadata, policy, versioning), **Proxy Gateway** เป็น runtime (handle request, enforce authz, log). ที่น่าสนใจคือ **AutoCrawler** — service ที่รันบน Cadence สแกน Uber's IDL (Interface Definition Language) registry ซึ่งมี **10,000+ service definition** แล้ว auto-generate MCP tool ออกมาโดยที่ทีม service ไม่ต้องเขียน MCP server เลย. นี่ตัดงาน onboarding ที่ปกติต้องให้แต่ละทีมเขียน wrapper เอง — พังทลายคอขวดหลักของ enterprise MCP

Authorization วิ่งผ่านระบบ internal access control ของ Uber เอง — เช็คทั้งระดับ server (agent มีสิทธิ์เรียก MCP server นี้ไหม) และระดับ tool (ใน server นี้ agent เรียก tool ตัวไหนได้บ้าง). ด้าน developer experience: coding agent ของวิศวกร Uber ไม่ติดตั้ง MCP server ลงเครื่องแต่คุยผ่าน CLI ภายในชื่อ **aifx** ที่ list, search, และ invoke tool ผ่าน gateway ตรง ๆ

## ทำไมสำคัญ

จุดสำคัญไม่ใช่ตัวเลข 800/5,000 — แต่คือ **การยืนยันว่า pattern "MCP Gateway" คือคำตอบของ enterprise agent governance**. ตลอดปี 2026 ปัญหาใหญ่ของทีมที่ deploy agent บน scale ไม่ใช่ว่าโมเดลเขียน tool call ไหวหรือเปล่า — แต่คือ (1) จะ onboarding service ใหม่เข้าระบบยังไงโดยไม่ bottleneck ที่ central team, (2) จะ audit ว่า agent ไหน เรียก tool ไหน เมื่อไหร่ ได้ไหม, (3) จะจัดการ identity ของ agent vs identity ของ user ยังไง. Uber ตอบครบทั้งสามข้อด้วย design pattern เดียวกันที่ cloud ทุกเจ้ากำลังขาย — แต่พิสูจน์ที่ production ก่อน

Pattern นี้จะทำซ้ำได้ที่อื่น ถ้ามีสององค์ประกอบ: **registry ที่สะอาด** (Uber มี IDL registry มาก่อน MCP จะเกิด) และ **auth infra ที่ express policy แบบ fine-grain ได้** (เช่น Uber's internal AC, Google Zanzibar, AWS IAM). บริษัทที่ไม่มีสองอย่างนี้จะพยายามซื้อ MCP gateway สำเร็จรูป (Zuplo, Maxim, awesome-mcp-gateways) แต่สุดท้ายจะเจอข้อจำกัดเดียวกัน — gateway ทำได้แค่กันของเข้าออก, แต่ถ้าไม่มี canonical list ของ service ภายในที่ครบ, AutoCrawler-style automation ก็ไม่เกิด

Signal ข้อสาม: InfoQ, ZenML, Forkast รายงานตัวเลขนี้พร้อมกันในสัปดาห์เดียว หมายความว่าตลาด enterprise agent platform กำลังเปลี่ยนภาษาจาก "framework" (LangChain, CrewAI) มาเป็น "gateway + registry" (Uber, Apigee-MCP, Kong-AI). ชั้นที่ชี้ชะตา vendor จะไม่ใช่ว่า framework ไหน DSL สวยที่สุด — แต่คือใครคุม distribution + policy + identity ของ tool call ใน enterprise ได้

## มุม AI Agent Platform

สำหรับ **builders** (ทีม Enabridge Research กับทีม agent framework ไทย): ถ้ากำลังขาย enterprise agent, ขายตัว orchestrator เฉย ๆ ไม่พอ — ต้องตอบได้ว่า "tool discovery, auth, และ audit อยู่ที่ไหน". Uber สอนว่า gateway + registry pattern เป็นคำตอบที่ลูกค้าจะคาดหวัง ไม่ใช่ feature เสริม. ทีมที่ build agent platform บน MCP ควรออกแบบให้ snap เข้ากับ registry/gateway ที่อาจมีอยู่แล้ว ไม่ใช่สร้าง MCP server รายตัว

สำหรับ **users / business** ที่ deploy: อย่าเริ่มจาก agent แต่เริ่มจาก **service catalog**. ถ้าในองค์กรไม่มี registry ของ API/service ที่ยังใช้งานอยู่, การสร้าง MCP server แปดร้อยตัวจะกลายเป็นหนี้ทางเทคนิคในหนึ่งปี. CTO ไทยควรลงทุนใน IDL หรือ service catalog ตัวแรก — แล้วค่อยวาง MCP gateway ทับทีหลัง. Pattern การเดินของ Uber (IDL มาก่อน 10 ปี → Cadence มาก่อน 8 ปี → MCP มาปี 2025 → Gateway มาปี 2026) คือ roadmap ย้อนรอยได้

สำหรับ **ecosystem**: Cloudflare, AWS, Google, Microsoft กำลังเร่งขาย MCP gateway managed (Apigee, API Gateway, Azure API Management, Cloudflare AI Gateway). Uber's post เป็น reference ที่ทุกเจ้าจะอ้างเพื่อขายให้ enterprise. ที่น่าจับตา: Anthropic/OpenAI จะเลือก push MCP registry standard เองไหม — ถ้าไม่, hyperscaler จะกิน layer นี้ไปเหมือนที่กิน API management layer ในยุค REST

## Sources
- [Uber Builds MCP Gateway to Govern Access to 800+ Servers and 5,000+ AI Agent Tools (InfoQ)](https://www.infoq.com/news/2026/11/uber-mcp-gateway-ai-agents/)
- [Uber Ships MCP Gateway at Production Scale (Forkast)](https://forkast.news/uber-ships-mcp-gateway-at-production-scale-800-servers-and-5000-tools-behind-a-single-control-surface/)
- [Scaling Enterprise Agent Access with a Centralized MCP Gateway (ZenML LLMOps DB)](https://www.zenml.io/llmops-database/scaling-enterprise-agent-access-with-a-centralized-mcp-gateway)
- [Designing MCP Gateway — Uber's MCP Management Platform (Uber Engineering)](https://x.com/UberEng/status/2106071967619322330)

---

## Audio script
วันนี้มีข่าวใหญ่จาก Uber ครับ Uber เปิด deep dive เรื่อง MCP Gateway ที่รัน production อยู่จริง มี MCP server แปดร้อยตัวและ tool ห้าพันตัวอยู่หลังประตูเดียว นี่ไม่ใช่ pilot หรือ demo แต่คือ infrastructure ที่ coding agent ของวิศวกร Uber ใช้ทุกวัน จุดที่น่าทึ่งคือ AutoCrawler สแกน service registry ภายในที่มี service definition หนึ่งหมื่นตัว แล้ว auto generate MCP tool ออกมาโดยที่ทีม service ไม่ต้องเขียน MCP server เอง ตัดคอขวด onboarding ที่หลายบริษัทเจอตอนนี้ Architecture แยกเป็น control plane คือ MCP Registry ที่เก็บ metadata กับ policy ออกจาก Proxy Gateway ที่ handle runtime กับ authz authz เช็คสองชั้น ทั้งระดับ server และระดับ tool ผ่านระบบ internal access control ของ Uber เอง สิ่งที่ Uber สอนตลาด AI agent คือ gateway + registry pattern ไม่ใช่แค่ feature แต่เป็นคำตอบของ enterprise agent governance บริษัทที่คิดว่าจะ deploy agent หนึ่งร้อยตัวในองค์กรโดยไม่มี registry กลางควรหยุดและกลับไปทำ service catalog ก่อน Signal อีกข้อ InfoQ ZenML Forkast รายงานพร้อมกันในสัปดาห์เดียว หมายความว่าตลาด enterprise agent กำลังเปลี่ยนภาษาจาก framework เป็น gateway กับ registry ชั้นที่ชี้ชะตา vendor จะไม่ใช่ว่าใคร DSL สวยที่สุด แต่คือใครคุม distribution policy และ identity ของ tool call ใน enterprise ได้ครับ
