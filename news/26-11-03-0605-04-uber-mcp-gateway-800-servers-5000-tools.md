---
date: 2026-10-30
slug: uber-mcp-gateway-800-servers-5000-tools
topic: openbridge-trend
reading_time_min: 5
sources: 4
image_prompt: |
  Editorial isometric illustration of a hyperscale control center with three
  layered rings. Outer ring: dozens of small cubes labeled "MCP SERVER" with a
  big header "800+ SERVERS". Middle ring: a dense tool grid stamped
  "5,000+ TOOLS". Inner ring: a glowing gate called "OMNI MCP PROXY" that
  exposes only four meta-tools labeled "discover_server / discover_tools /
  get_tool_schema / invoke_tool". A side panel shows a Cadence workflow
  loop labeled "AUTOCRAWLER", and a small ribbon reads "AIFX CLI +
  MINION CODING AGENT". A header on top: "UBER'S PRODUCTION MCP STACK".
  Deep slate and burnt orange palette with cyan accents, 1:1 aspect,
  strong contrast for 200px thumbnails, no real human faces.
image: images/26-11-03-0605-04-uber-mcp-gateway-800-servers-5000-tools.png
---

# Uber ships MCP Gateway production — 800 server + 5,000 tool หลัง gateway เดียว, และ playbook ที่ Fortune 500 จะ copy

## TL;DR
- Uber ย้าย MCP Gateway เข้า production: **800+ MCP server, 5,000+ tool** ภายใต้ single control plane; blog "Designing MCP Gateway" ลงวันที่ 1 ต.ค. 2026, นำเสนออีกครั้งใน AAIF MCP Dev Summit สัปดาห์ก่อน
- **AutoCrawler** (Cadence-based workflow) scan IDL registry อัตโนมัติ, สร้าง tool spec ใหม่, **แต่ default disabled** จนกว่า owning team จะยืนยัน
- **Omni MCP Proxy** expose แค่ 4 meta-tool (`discover_server`, `discover_tools`, `get_tool_schema`, `invoke_tool`) — agent ไม่ต้องโหลด schema เป็นแสนบรรทัดก่อนทำงาน
- **aifx CLI** ให้ Claude Code / Cursor / Codex เรียก tool ของ Uber โดยไม่ต้องรัน MCP server ใน laptop; **Minion** คือ internal background coding agent บน stack เดียวกัน

## เกิดอะไรขึ้น

Uber engineering blog "Designing MCP Gateway" (เผยแพร่ 1 ต.ค. 2026) + presentation ที่ AAIF MCP Dev Summit ปลายเดือน ต.ค. เปิด architecture ของ MCP Gateway ที่รันใน production — **800+ MCP server, 5,000+ tool** ที่ครอบ microservice ของ Uber ที่พูด HTTP, gRPC, และ TChannel

Problem ที่แก้: Uber มี microservice หลักพันตัว, ถ้าปล่อยให้ทีมแต่ละทีมเขียน MCP server เอง จะ fragment, security policy ไม่ consistent, discovery เป็น hell. Solution: **dual-plane architecture** — control plane (MCP Registry) ที่เก็บ tool metadata + authorization + enablement state; data plane (Proxy Gateway) ที่รับ call จาก agent + enforce policy + redaction + route ไปหา service

**AutoCrawler** คือ Cadence-based workflow (Cadence เป็น workflow engine ของ Uber เอง, open-source) ที่ scan IDL (Interface Definition Language) registry ของ Uber หา service ใหม่ + schema change อัตโนมัติ — translate เป็น MCP tool spec แล้วลงใน Registry. **จุดสำคัญ**: tool ที่ discover ใหม่ **default = disabled** จนกว่า owning team จะ explicit review และ enable. นี่คือ safe-by-default pattern ที่ Fortune 500 ต้องการ

**Omni MCP Proxy** คือตัวที่ fix problem ใหญ่ของ enterprise MCP: ถ้า agent ต้อง `list_tools` แล้วได้ 5,000 tool schema คืนมา จะกิน context window ของ Claude หมดก่อน. Omni เปิดแค่ **4 meta-tool**: `discover_server` (list servers), `discover_tools` (list tools in server), `get_tool_schema` (get schema of one tool), `invoke_tool` (call it). Agent "search" tool ก่อนแล้วค่อย load schema ของ tool ที่จะใช้จริง — Claude Code เองก็มี pattern เดียวกันเรียก "progressive tool discovery"

**Security + auth**: Gateway enforce charter policy ที่ระดับ tool, apply PII redaction อัตโนมัติ, carry chain of actor (ใครเรียก, agent ตัวไหน, service ไหน) ใน short-lived JWT. ถ้า agent compromised, blast radius จำกัดอยู่ที่ scope ของ JWT นั้น

**Developer tooling**: **aifx** คือ internal CLI ของ Uber ที่ Claude Code, Cursor, Codex, และ Copilot เรียกได้ — agent ไม่ต้องรัน local MCP server, aifx ชี้ตรงไป Omni Proxy. **Minion** คือ Uber's internal background coding agent (คู่กับ Minion ของ Factory และ Devin ของ Cognition) ที่ build on stack เดียวกัน

สิ่งที่ Uber ยังไม่เปิด: **จำนวน agent user**, **ตัวเลข tool call ต่อวัน**, **cost per call**, **time-to-onboard tool ใหม่**. Blog เน้น architecture ไม่ใช่ operation metric. AAIF summit talk ก็ไม่ให้ number เหล่านี้ — น่าจะเก็บไว้ keynote เร็ว ๆ นี้

## ทำไมสำคัญ

MCP เริ่มมี **reference architecture ของ enterprise scale** แล้ว. ตอน Anthropic ปล่อย MCP ธ.ค. 2024 ตัวอย่างคือ Claude Desktop + local Python server — ไม่ใช่ production enterprise. ตอน MCP spec rev 2026-07-28 ทำให้ stateless + serverable-friendly, ยังไม่มี reference ที่ scale ถึง 5,000 tool. ตอนนี้ Uber ตอบคำถามเหล่านั้นหมด: **AutoCrawler สำหรับ discovery, Omni Proxy สำหรับ context budget, JWT-chain สำหรับ auth, Registry สำหรับ governance** — เป็น template ที่ JPMorgan, Walmart, Delta, BP จะ copy แทบจะทันที

**Pattern สำคัญ**: Uber **ไม่** expose tool โดยตรงให้ agent — expose meta-tool แทน. นี่ swings pendulum กลับจาก "เปิดทุกอย่างให้ model ตัดสินใจ" (OpenAI Operator) → "ให้ model ค้น + ขอ schema ของตัวที่จะใช้" (Uber Omni, Claude Code). เป็นสัญญาณว่า **context engineering** กลายเป็นสายงานใหม่ของ enterprise AI team — ไม่ใช่ prompt engineering อีกต่อไป

ที่ sharp อีกจุด: **Minion background coding agent** คือการตอกย้ำว่า **background agent ที่ auto-plan + auto-execute นั้นไม่ใช่ future แต่คือ now สำหรับ Fortune 500 ที่มี infra**. UBS มี 18,000 developer ที่ใช้ AI tooling, Uber มี Minion, Google มี Jules, Factory มี Droids. Enterprise ที่ไม่มี internal coding agent ภายในปี 2027 จะมี 20-30% productivity gap

## มุม AI Agent Platform

สำหรับ **builders** ที่ขาย MCP infrastructure (Cloudflare Workers MCP, FastMCP, LangChain MCP server): **Uber architecture คือ feature list ของคุณ**. ลูกค้า enterprise จะถามถึง AutoCrawler-equivalent, meta-tool proxy, Cadence/Temporal workflow สำหรับ auto-registry, chain-of-actor JWT. ถ้าสินค้าไม่ cover สี่ชั้นนี้, จะหลุดจาก shortlist ของ Fortune 500. Mintive (identity), Cloudflare (gateway), และ Honeycomb (observability) อยู่ในสาม slot นี้แล้ว

สำหรับ **users / business**: ถ้าคุณเป็น enterprise ไทยที่มี microservice 100-500 ตัว (SCB, PTT, CP, True) และกำลังจะเปิด MCP endpoint สำหรับ agent — **copy Uber blueprint ก่อนลองออกเอง**. สี่สิ่งที่ต้องตั้งก่อน rollout: (1) Registry + ownership metadata, (2) auto-discovery pipeline, (3) meta-tool proxy, (4) JWT chain + per-tool policy. Phase 1 เปิดแค่ internal, Phase 2 เปิดให้ Claude/Copilot ของพนักงาน

สำหรับ **ecosystem**: **AAIF (Agentic AI Foundation)** กำลังกลายเป็น venue มาตรฐานที่ production MCP user มาแชร์ pattern — AWS, Cloudflare, Bloomberg, Google อยู่ platinum tier แล้ว. ภายใน 6 เดือน จะมี **MCP certification / compliance tier** คล้าย SOC 2 สำหรับ gateway implementation. Uber คือ reference ที่คู่กับ Microsoft Agent 365 architecture — pattern สองตัวนี้จะปั้น spec version ถัดไปของ MCP

## Sources
- [Designing MCP Gateway (Uber Engineering blog)](https://www.uber.com/blog/designing-mcp-gateway/)
- [Uber ships MCP gateway at production scale (Forkast)](https://forkast.news/uber-ships-mcp-gateway-at-production-scale-800-servers-and-5000-tools-behind-a-single-control-surface/)
- [AAIF's MCP Dev Summit: Gateways, gRPC, Observability (lavx.hu)](https://news.lavx.hu/article/aaif-s-mcp-dev-summit-gateways-grpc-and-observability-signal-protocol-hardening)
- [Using MCP Gateway with Claude Code (FutureAGI practical guide)](https://futureagi.com/blog/using-mcp-gateway-with-claude-code-practical-guide-2026/)

---

## Audio script
วันนี้มาดูเรื่อง infrastructure ที่สำคัญครับ Uber เปิด blog Designing MCP Gateway ลงวันที่ 1 ตุลาคม แล้วเพิ่งนำเสนออีกครั้งใน AAIF MCP Dev Summit ปลายเดือนตุลาคม ตัวเลขที่โดดคือ 800 กว่า MCP server และ 5,000 กว่า tool ที่รันอยู่หลัง single control surface ของ Uber ที่สำคัญเพราะ Uber ตอบคำถาม architecture ของ enterprise MCP ที่ยังไม่มี reference ชัดก่อนหน้านี้ สี่ชั้นหลัก หนึ่ง AutoCrawler ที่เป็น Cadence based workflow scan IDL registry ของ Uber หา service ใหม่กับ schema change อัตโนมัติ แล้ว register เป็น MCP tool แต่ default ปิดจนกว่า owning team จะ enable เอง สอง Omni MCP Proxy ที่แก้ปัญหาใหญ่ของ enterprise MCP ถ้า agent ต้อง list tool แล้วได้ 5,000 tool schema คืนมาจะกิน context window ของ Claude หมด Omni เปิดแค่ 4 meta tool คือ discover server, discover tools, get tool schema, และ invoke tool agent ค้นก่อนแล้วค่อย load schema ของ tool ที่จะใช้จริง สาม auth ใช้ short lived JWT ที่ carry chain of actor ว่าใครเรียก agent ตัวไหน service ไหน ถ้า agent compromised blast radius จำกัดอยู่ที่ scope ของ JWT สี่ aifx เป็น internal CLI ที่ Claude Code Cursor Codex เรียกได้ agent ไม่ต้องรัน local MCP server และ Uber มี background coding agent ของตัวเองชื่อ Minion บน stack เดียวกัน สิ่งที่ Uber ยังไม่เปิดคือจำนวน agent user จำนวน tool call ต่อวัน และ cost per call Blog เน้น architecture ไม่ใช่ operation metric ที่ takeaway สำคัญ MCP มี reference architecture ของ enterprise scale แล้ว JPMorgan Walmart Delta BP จะ copy template นี้แทบจะทันที สำหรับ enterprise ไทยที่มี microservice 100 ถึง 500 ตัวและกำลังจะเปิด MCP endpoint สำหรับ agent copy Uber blueprint ก่อนลองออกเองดีกว่าครับ สี่สิ่งต้องตั้งก่อน rollout Registry กับ ownership metadata, auto discovery pipeline, meta tool proxy, และ JWT chain plus per tool policy
