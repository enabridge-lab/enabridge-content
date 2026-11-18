---
date: 2026-11-17
slug: uber-mcp-gateway-800-servers-5000-tools
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a giant control tower at the center
  of a sprawling server farm. Signs on the tower wall read "MCP GATEWAY",
  with labels hanging around it: "800 SERVERS", "5,000 TOOLS",
  "50–70K TOKENS → NEAR ZERO". Rays of light connect the tower to dozens of
  tiny agent silhouettes at desks below. Soft slate-gray, cyan, and warm
  orange palette, clean editorial style, 1:1 aspect, no real human faces
  (silhouettes OK), high contrast so numbers read at 200px thumbnail.
image: images/26-11-19-0605-04-uber-mcp-gateway-800-servers-5000-tools.png
---

# Uber พิสูจน์ว่า MCP ไม่ใช่ demo — MCP Gateway production 800 servers / 5,000 tools / token overhead เกือบ 0

## TL;DR
- Uber ขึ้น MCP Gateway production — host 800+ MCP servers กับ 5,000+ tools ภายใต้ control surface เดียว
- Architecture: Registry (control plane) + Proxy Gateway (data plane) + AutoCrawler (discovery) + MCPFx + Omni MCP — ลด per-session tool-schema overhead จาก 50K–70K tokens ต่อ session ลงเหลือ "near-zero"
- Governance tool-level ผ่าน Access Control System ของ Uber; distinguish ระหว่าง human/service/agent caller; existing HTTP/gRPC/TChannel service expose เป็น MCP tool โดยไม่ต้องแก้

## เกิดอะไรขึ้น
Uber publish engineering blog "Designing MCP Gateway" สัปดาห์นี้ บอกว่า MCP Gateway เป็น "foundational microservice ที่ powers all MCP interactions at Uber" ตอนนี้ host 800+ MCP servers กับ 5,000+ tools แล้ว ครอบคลุม service ทั่วทั้งบริษัท — จากที่เคยเป็น ad-hoc integration ที่ทีมสร้างกันเองจนกระจัด กระจาย

Problem ที่ Gateway แก้มี 4 อย่าง: (1) duplicate infrastructure ที่ทีมสร้างเองซ้ำ (2) tool discovery ที่ไม่มี control plane กลาง (3) protocol fragmentation ระหว่าง HTTP, gRPC, TChannel (service mesh เดิมของ Uber) (4) security risk จาก permission ที่กระจัดกระจาย Solution แยกเป็น control plane (MCP Registry — catalog, ownership, enablement) กับ data plane (Proxy Gateway — translate MCP → HTTP/gRPC/TChannel และกลับ)

Component ที่น่าสนใจคือ AutoCrawler — Cadence-based discovery engine ที่ scan IDL registry ของ Uber แล้วสร้าง MCP server + tool ให้อัตโนมัติ และ heartbeat ค้นหา native MCP server; MCPFx เป็น framework ที่ developer ใช้สร้าง native MCP server; Muttley เป็น service mesh sidecar ที่ run request ปลายทาง ที่สำคัญคือ Omni MCP + Code Mode (aifx CLI) ที่ขยาย discovery เป็น 4 primitive (discover_server, discover_tools, get_tool_schema, invoke_tool) — ทำให้ agent ไม่ต้องโหลด schema ของ tool ทุกตัวเข้า context รวมกัน

ผลลัพธ์ที่ Uber claim: per-session tool-schema overhead ที่เคยอยู่ที่ 50K–70K tokens ต่อ session ลดลงเหลือ "near-zero" — ประหยัด token cost + latency ของ agent invocation อย่างมีนัย

## ทำไมสำคัญ
ตั้งแต่ Anthropic ประกาศ MCP เมื่อปลายปี 2024 คำถามใหญ่ที่สุดในวงการคือ "MCP จะ scale ที่ production enterprise ได้ไหม" — เพราะ naive implementation ให้ agent โหลด tool schema ทุกตัวเข้า context จะกิน token หายไปก่อนที่ agent จะทำอะไรได้ Uber เป็น hyperscaler แรก ๆ ที่ ship design ที่แก้ปัญหานี้แบบ public — Omni MCP pattern (incremental discovery) จะกลายเป็น reference architecture ที่ enterprise อื่นเอาไปลอก

Implication ของ 800 servers / 5,000 tools คือ MCP กลายเป็น "service mesh for agents" ของ Uber จริง ๆ — ไม่ใช่ experiment เล็ก ๆ ของทีม R&D ซึ่งต่างจาก Netflix, Spotify, หรือ Airbnb ที่ยังไม่เห็น public evidence ว่า MCP ขึ้น production ขนาดนี้ Uber กำลัง set bar ของ "agent platform maturity" ให้ hyperscaler อื่นต้องตาม

Caveat ที่ ZenML ชี้ใน LLMOps database: Uber blog ไม่ได้ให้ independent evaluation ของ reliability, agent task quality, latency, หรือ cost — ตัวเลข "near-zero token overhead" เป็น self-report ไม่ได้มี external benchmark และยังไม่มีตัวเลข agent count / request-per-day / dollar saved ที่ CFO จะอ้างอิงตรง ๆ ได้

## มุม AI Agent Platform
**Builders** — ถ้าคุณสร้าง agent framework หรือ orchestration tool ตอนนี้ pattern ของ Uber (central registry + incremental discovery + schema-on-demand) เป็น spec implicit ที่ enterprise จะ demand ภายใน 12-18 เดือน framework ที่ยัง assume "agent initialize ด้วย tool list ทั้งหมด" จะดูล้าสมัยทันที LangChain, LlamaIndex, Semantic Kernel ควรเพิ่ม native support ของ MCP Omni pattern

**Users/business** — สำหรับ enterprise ไทยที่มี microservice architecture ซับซ้อน (ธนาคาร, telco, utility) การวาง MCP Gateway layer กลางเป็น investment ที่ payoff ชัดกว่าการให้แต่ละทีมสร้าง agent-to-service integration เอง Enabridge ที่สร้าง agent platform ควรเสนอ "managed MCP Gateway" เป็น service — ลด cost ของ central IT team ที่ต้อง maintain gateway เอง

**Ecosystem** — Cloudflare (ที่ ship MCP server platform เมื่อต้นปี), AWS (Bedrock AgentCore), Google Cloud (Vertex AI Agent Builder) จะต้องมี equivalent ของ MCP Gateway as managed service ภายใน Q1 2027 — Uber reference architecture จะกลายเป็น template; vendor ที่ไม่ถึงภายใน H1 2027 จะเสีย enterprise deal ให้คู่แข่ง

## Sources
- [Designing MCP Gateway (Uber Engineering)](https://www.uber.com/blog/designing-mcp-gateway/)
- [Uber MCP Gateway for AI Agents (InfoQ)](https://infoq.com/news/2026/11/uber-mcp-gateway-ai-agents)
- [Scaling Enterprise Agent Access with a Centralized MCP Gateway (ZenML LLMOps Database)](https://www.zenml.io/llmops-database/scaling-enterprise-agent-access-with-a-centralized-mcp-gateway)

---

## Audio script
ข่าวที่สี่วันนี้เป็น infrastructure story ที่ enterprise architect ไทยต้องฟัง Uber publish engineering blog เรื่อง MCP Gateway บอกว่า MCP Gateway ของ Uber เป็น foundational microservice ที่ powers MCP interaction ทุกตัวในบริษัท ตอนนี้ host 800 MCP servers กับ 5,000 tools ภายใต้ control surface เดียว problem ที่ gateway แก้มี 4 อย่าง duplicate infra ที่ทีมสร้างซ้ำ tool discovery ที่ไม่มี control plane protocol fragmentation ระหว่าง HTTP gRPC TChannel และ security risk จาก permission กระจัดกระจาย Uber แยกเป็น control plane คือ MCP Registry กับ data plane คือ Proxy Gateway ที่ translate MCP เป็น HTTP gRPC TChannel แล้วกลับ มี AutoCrawler ที่ scan IDL registry แล้วสร้าง MCP server tool อัตโนมัติ และที่สำคัญคือ Omni MCP pattern ที่ agent ไม่ต้องโหลด schema ของ tool ทุกตัวเข้า context รวมกัน แต่ discover แบบ incremental ผ่าน 4 primitive ผลลัพธ์คือ per-session tool schema overhead ที่เคยอยู่ 50 ถึง 70 พัน tokens ต่อ session ลดลงเหลือ near-zero ตามที่ Uber claim สิ่งที่สำคัญคือ MCP กลายเป็น service mesh for agents ของ Uber จริง ไม่ใช่ experiment เล็ก ๆ อีกต่อไป เป็น signal ที่ enterprise ไทยที่มี microservice architecture ซับซ้อน ควรวาง MCP Gateway กลางเป็น investment ที่ payoff ชัดกว่าให้แต่ละทีมสร้าง integration เอง Enabridge ควรเสนอ managed MCP Gateway เป็น service เพื่อลด cost ของ central IT ไม่ต้อง maintain gateway เอง
