---
date: 2026-08-28
slug: mcp-stateless-400m-downloads-agentic-http
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial isometric illustration of a giant blueprint labeled "MCP
  2026-07-28" being unrolled across a datacenter floor; on top of it, dozens
  of MCP server icons stack up cleanly on standard HTTP load-balancer rails.
  Three floating number panels dominate: "400M SDK DOWNLOADS", "4X GROWTH",
  "STATELESS CORE". Around the blueprint, small logo silhouettes of GitHub,
  Cloudflare, Supabase, AWS, PostHog, and Microsoft Foundry glow with green
  checkmarks. A banner across the top reads "SESSION STORES DELETED". Deep
  navy background with cyan rim lighting. 1:1 aspect. No real human faces
  (silhouette only). Numbers oversized so they read in a 200px thumbnail.
image: images/26-08-28-0621-02-mcp-stateless-400m-downloads-agentic-http.png
---

# MCP 2026-07-28 stateless spec + 400M SDK downloads: agentic protocol กลายเป็น "just another HTTP workload" — enterprise scaling ปลด lock

## TL;DR
- **22 ส.ค. 2026** MCP Core Maintainers เผย updated roadmap รอบใหญ่ตาม landmark spec **2026-07-28** (ปลาย ก.ค.) — เปลี่ยน MCP จาก bidirectional stateful → **stateless request/response core**, MCP server เท่ากับ HTTP workload ธรรมดา, run บน serverless/edge/standard load balancer ได้ทันทีโดยไม่ต้อง sticky session
- **Adoption metric สะกดใจ:** MCP SDK ทะลุ **400M monthly downloads** (โต 4x จากต้นปี), กลายเป็น industry standard เชื่อม agent ↔ tool/data. GitHub, Cloudflare, Supabase, AWS, PostHog, Microsoft Foundry ship stateless implementation ภายใน "release week" — pace adoption ที่ open standard ไม่ค่อยได้เห็น
- **Enterprise unlock ที่ใหญ่กว่า scale:** authorization ใหม่ align กับ **OAuth 2.0 + OIDC** production stack, admin provision MCP connectors ทั้ง org ผ่าน identity provider เดียว, user inherit access ตาม IdP group — เลิก build custom auth ต่อ connector
- Signal: MCP กำลังจะกลายเป็น "**HTTPS ของ agent layer**" — invisible plumbing ที่ทุกคนใช้แต่ไม่ต้องรู้ว่าใช้อยู่. ต่อจากนี้การแข่งย้ายจาก "ใครถือ protocol" → "ใครมี skill/tool ที่ดีที่สุดบน protocol กลาง"

## เกิดอะไรขึ้น

28 ก.ค. 2026 MCP Core Maintainers ship spec release ที่ทีมเรียกว่า **"biggest update ever"** — **stateless core** ที่ตัด transport-level session management ออกทั้งหมด. เดิม MCP server ต้องถือ session state (client identity, protocol version, capability negotiation) ตลอด connection — ทำให้ต้อง sticky session, shared session store (Redis, Memcached), และ WebSocket-like transport ที่ scale ยากบน commodity HTTP infrastructure

2026-07-28 spec กลับด้าน: request แต่ละครั้ง carry protocol version + client identity + capabilities ในตัวเอง. server ไม่ต้องจำอะไรระหว่าง request. ผลคือ MCP server ตัวใหม่ deploy บน AWS Lambda, Cloudflare Workers, Vercel Edge, Google Cloud Run โดยไม่ต้อง config อะไรพิเศษ — เหมือน HTTP API ธรรมดา. Multi-Round-Trip Requests (SEP-2322) แทน server-initiated request pattern เดิม — user confirmation flow, elicitation, long-running task ทำงานบน stateless server ได้ครบ. **Tasks** ถูก rework เป็น official extension (SEP-2663), MCP Apps + Tasks ship ผ่าน versioned extensions framework — เพิ่ม capability ใหม่โดยไม่ break core protocol

22 ส.ค. 2026 Core Maintainers ประกาศ updated roadmap — plan roadmap 6 เดือนข้างหน้าเน้น **stability guarantee + governance maturity**, ตามหลัง spec release ไปหนึ่งเดือน. เป็น signal ว่า core spec เข้าเฟส "boring but reliable" — สิ่งที่ enterprise procurement รอมาสามปี

**Adoption pace น่าตกใจ:** ภายใน release week (28 ก.ค. - 4 ส.ค.) GitHub update MCP Server ก่อน spec release official เลย — ตัด Redis session storage + request payload inspection ทิ้ง. Cloudflare deploy stateless server day one, existing client reconnect ได้โดยไม่ config อะไรใหม่. Manufact (managed MCP hosting) report SDK ใหม่ **ลด package size 83% + เร็วขึ้น 25%**, hosts "thousands of MCP servers" ทั้งหมด migrate ภายใน 10 วัน. Supabase, AWS, PostHog, Microsoft Foundry ประกาศ production implementation ในสัปดาห์เดียวกัน — Foundry scale integration count จาก "dozens → thousands" หลัง migrate. Simon Willison (LLM tools observer) comment ว่า stateless MCP *"recaptured my interest"* — สัญญาณจากนักพัฒนาแนวหน้าที่ห่างจาก MCP มาช่วง early spec

**Metric ที่ปิดคดี:** MCP SDK รวมทุก language ทะลุ **400M monthly downloads** (บนตัวเลขที่ core maintainer เผยใน blog roadmap 22 ส.ค.) — โต **4x จากต้นปี 2026**. เทียบ scale: MCP SDK download volume ใกล้เคียง Kubernetes client library ที่ 5-6 ปี maturity. Anthropic ที่เป็นผู้ริเริ่มบริจาค MCP ให้ AAIF ปลาย 2025, ปัจจุบัน AAIF (Linux Foundation) เป็น neutral steward — MCP + A2A รวมกันเป็นสอง protocol หลักของ agent economy (ดู brief 26-08-27-0614-01)

## ทำไมสำคัญ

Stateless MCP คือ **turning point ที่ทำให้ enterprise scale ไม่ใช่คำถามอีกต่อไป**. เดิมทีปัญหาใหญ่ที่ enterprise IT ปฏิเสธ MCP มีสามข้อ: (1) sticky session ทำ horizontal scaling ยาก, (2) auth stack ไม่ align กับ IdP ที่ใช้อยู่ (Okta, Azure AD, PingIdentity), (3) session store ต้อง provision + monitor แยกจาก main app. Spec 2026-07-28 ปิดทั้งสามข้อในรอบเดียว — MCP server กลายเป็น deployable บน infrastructure ที่ enterprise ใช้กันอยู่แล้ว, auth เข้ากับ OAuth 2.0/OIDC ที่ security team audit ได้, admin provision connector ทั้ง org ผ่าน IdP group เดียว

**Pattern ที่ตกผลึกคือ agent protocol กำลังตาม path เดียวกับ HTTPS ปี 2010-2015** — Let's Encrypt + HTTPS Everywhere เปลี่ยน HTTPS จาก "opt-in for banking site" เป็น "default for everything" ภายใน 5 ปี. MCP ตอนนี้อยู่ในเฟสเดียวกัน — จาก "experimental for early adopter" (2024-2025) เข้า "default for anyone building agent" (2026). เมื่อ default set แล้ว, ตัว protocol invisible — คนไม่คิดถึงตอน build, focus ที่ skill/tool layer แทน

**การแข่งย้าย layer:** ถ้า MCP + A2A เป็น commodity plumbing, moat ใหม่อยู่ที่ (1) **skill catalog depth** (จำนวน + คุณภาพของ prebuilt action — Claudeforce ที่ ship 37 skills วันเดียวกัน คือ template), (2) **tool ecosystem** (ใครมี MCP server ให้ enterprise data source สำคัญ — Salesforce, SAP, ServiceNow, Snowflake), (3) **governance + audit layer** (compliance rail ที่ enterprise IT audit ได้). vendor ที่ยังลงทุน "own our own protocol" ปีนี้ (OpenAI Assistants API, บาง proprietary agent framework) กำลังเสี่ยง strand asset — บริษัทลูกค้าจะขอ MCP compatibility แทน

**China ecosystem ยังไม่ align:** Alibaba, ByteDance, Tencent ไม่ใช่สมาชิก AAIF, ไม่ ship MCP-compatible server. ถ้า geopolitical split เกิดขึ้นในอีก 6-12 เดือน — Chinese cloud อาจสร้าง MPCP (Manufacturing Protocol for Chinese Platform) หรือ join AAIF ก็ยังไม่แน่. คนที่ deploy agent workload ข้าม China + non-China ต้องเตรียม dual-stack

## มุม AI Agent Platform

**Builders:** ถ้าคุณ maintain MCP server หรือ agent framework — **migrate ไป 2026-07-28 spec ทันที** ก่อน enterprise deal ต่อไปมาถาม compliance. Checklist: (1) ตัด session storage layer ทิ้ง, (2) implement OAuth 2.0/OIDC auth path, (3) support Multi-Round-Trip Requests (SEP-2322) แทน server-initiated, (4) publish tool ใน extensions framework แทน core spec extension. ถ้ายังใช้ WebSocket transport เดิม — plan sunset ภายใน Q4 2026. คนที่ยังไม่ ship stateless implementation จะ lose deal ให้คู่แข่งที่ ship ก่อนใน RFP ที่ include "MCP 2026-07-28 baseline" (มาแน่ในอีก 3-6 เดือน)

**Users / business:** สำหรับ enterprise ที่ evaluate agent platform — **require MCP 2026-07-28 baseline ใน RFP วันนี้**, บวก compliance กับ AAIF standards (MCP + A2A) ที่เขียนไว้ใน brief 26-08-27. Benefit ทันที: (1) portable agent workload ข้าม cloud (AWS Lambda ↔ Cloudflare Workers ↔ on-premise Kubernetes), (2) auth stack ใช้ Okta/Azure AD ที่มีอยู่ไม่ต้องซ้ำ, (3) audit trail ผ่าน standard OAuth 2.0 log ที่ SOC 2 auditor รู้จัก. Thai SMB ที่ deploy agent ครั้งแรก — เริ่มจาก MCP server ที่ managed (Cloudflare, Supabase) ไม่ต้อง self-host, cost < $100/เดือน สำหรับ workload เล็ก

**Ecosystem:** Anthropic (MCP originator) ได้ leverage strategic ที่ประเมินยาก — MCP-native จาก Claude Desktop → Claude API → Claude Agent Stack (GA 19 ส.ค.) → Claudeforce (26 ส.ค.). Every product ในสาย Anthropic support MCP native ตั้งแต่ launch. คู่แข่งที่ retrofit MCP support (OpenAI, Google) จะเห็น friction ยาว — architectural debt จาก assistant API design เก่า. Kubernetes analogy: Google ที่บริจาค K8s ให้ CNCF ไม่ได้ "เสีย" — ได้ tail-end lead ยาว 5+ ปีในตลาด managed K8s (GKE โต 40% YoY ยังทุกวันนี้). Anthropic กำลังเดินหมากเดียวกันบน MCP layer

## Sources
- [The New MCP Roadmap (MCP Blog, 22 ส.ค. 2026)](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/)
- [The 2026-07-28 Specification (MCP Blog)](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [Stateless MCP Ecosystem Adoption: Fast Industry Response (Agentic AI Foundation)](https://aaif.io/blog/the-ecosystem-responds-to-stateless-mcp)
- [MCP 2026-07-28 spec: stateless core, coming to Claude (Anthropic)](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)
- [The MCP 2026-07-28 Release, Explained for Enterprise Teams (CData)](https://www.cdata.com/blog/mcp-2026-07-28-release)

---

## Audio script
วันพฤหัสยี่สิบแปดสิงหา. Model Context Protocol เข้ารอบใหญ่. spec สอง พัน ยี่สิบ หก ศูนย์เจ็ด ยี่สิบแปด. เปลี่ยน MCP จาก bidirectional stateful เป็น stateless request response core. MCP server กลายเป็น HTTP workload ธรรมดา. run บน serverless หรือ edge หรือ standard load balancer ได้ทันที.

Metric ที่ปิดคดี. MCP SDK ทะลุ สี่ ร้อย ล้าน monthly downloads. โต สี่ เท่า จากต้นปี. ใกล้เคียง Kubernetes client library ที่มี maturity ห้าถึงหกปี.

Adoption pace น่าตกใจ. GitHub update MCP server ก่อน spec release. Cloudflare deploy stateless day one. Manufact ลด package size แปดสิบสามเปอร์เซ็นต์. เร็วขึ้นยี่สิบห้าเปอร์เซ็นต์. hosts thousands of MCP servers migrate ภายในสิบวัน. Supabase AWS PostHog Microsoft Foundry ship production implementation ในสัปดาห์เดียวกัน. Foundry scale integration count จาก dozens เป็น thousands.

ที่สำคัญกว่า scale คือ enterprise unlock. authorization ใหม่ align กับ OAuth 2.0 กับ OIDC. admin provision MCP connectors ทั้ง org ผ่าน identity provider เดียว. user inherit access ตาม IdP group. เลิก build custom auth ต่อ connector.

Pattern ที่ตกผลึกคือ agent protocol กำลังตาม path เดียวกับ HTTPS ปี สอง พัน สิบ ถึง สอง พัน สิบ ห้า. HTTPS Everywhere เปลี่ยน HTTPS จาก opt in for banking เป็น default for everything ภายในห้าปี. MCP ตอนนี้อยู่ในเฟสเดียวกัน. จาก experimental for early adopter เข้า default for anyone building agent.

การแข่งย้ายลาย. ถ้า MCP กับ A2A เป็น commodity plumbing. moat ใหม่อยู่ที่ skill catalog depth. Claudeforce ที่ ship สาม สิบ เจ็ด skills วันเดียวกันเป็น template. อยู่ที่ tool ecosystem. ใครมี MCP server ให้ enterprise data source สำคัญ. อยู่ที่ governance กับ audit layer. compliance rail ที่ enterprise IT audit ได้.

สำหรับ builders. migrate ไป สอง พัน ยี่สิบ หก ศูนย์ เจ็ด ยี่สิบ แปด spec ทันที. ก่อน enterprise deal มาถาม compliance. ตัด session storage. implement OAuth 2.0. support Multi Round Trip Requests. คนที่ยังไม่ ship stateless implementation จะ lose deal ให้คู่แข่งใน RFP ที่ include MCP baseline.

สำหรับ enterprise. require MCP สอง พัน ยี่สิบ หก ศูนย์ เจ็ด ยี่สิบ แปด ใน RFP. บวก AAIF compliance. Benefit ทันที คือ portable agent workload ข้าม cloud. auth stack ใช้ Okta หรือ Azure AD ที่มีอยู่. audit trail ผ่าน standard OAuth log.

Thai SMB ที่ deploy agent ครั้งแรก. เริ่มจาก MCP server managed จาก Cloudflare หรือ Supabase. cost น้อยกว่าหนึ่งร้อยดอลลาร์ต่อเดือน สำหรับ workload เล็ก. ไม่ต้อง self host

Anthropic ได้ leverage ยาว. MCP native ตั้งแต่ Claude Desktop จนถึง Claudeforce. คู่แข่งที่ retrofit MCP support จะเห็น friction ยาว. architectural debt จาก assistant API design เก่า. คล้าย Google ที่บริจาค Kubernetes ให้ CNCF แล้วยังได้ lead ห้าปีในตลาด managed K8s
