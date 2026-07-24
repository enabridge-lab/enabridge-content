---
date: 2026-07-25
slug: mcp-2026-07-28-stateless-release-candidate
topic: agent-platform-trend
reading_time_min: 5
sources: 5
image_prompt: |
  An editorial isometric illustration on a deep-navy background:
  a giant server rack labeled "MCP · STATELESS" glowing cyan, with
  arrows showing HTTP requests bouncing freely between three parallel
  load-balancer nodes with no sticky session. To the left, a smaller
  greyed-out rack marked "STATEFUL · DEPRECATED · JUL 28" being
  wheeled off. Above the main rack: three floating badges labeled
  "TASKS · APPS · OAUTH 2.0". Below: a countdown clock reading
  "3 DAYS · SPEC 2026-07-28". Sharp editorial typography, high
  contrast, 1:1 aspect, no real human faces.
image: images/26-07-25-0610-03-mcp-2026-07-28-stateless-release-candidate.png
---

# MCP 2026-07-28 Release Candidate — ตัด stateful, เพิ่ม OAuth, Tasks graduate, MCP Apps — ready สำหรับ enterprise deploy ทันที Monday นี้

## TL;DR
- **Model Context Protocol spec 2026-07-28** ปล่อย release candidate เมื่อ 23 ก.ค. และจะ **finalize วันจันทร์ที่ 28 ก.ค.** (3 วันจากนี้) — เป็น revision ใหญ่ที่สุดตั้งแต่ launch
- **ตัด stateful หมด** — ไม่มี initialize handshake, Mcp-Session-Id header, หรือ sticky routing; capability + protocol version ย้ายไปอยู่ใน `_meta` object ของทุก request
- **Tasks graduate** จาก experimental เป็น extension official (tasks/get, tasks/update, tasks/cancel) — long-running work แบบ stateless พร้อม production
- **MCP Apps** เพิ่ม — server render interactive HTML ให้ agent host แสดงใน sandboxed iframe
- **OAuth 2.0/OIDC alignment** ผ่าน 6 SEPs — enterprise regulated finally deploy MCP ได้
- Breaking: tasks/list ถูกลบ; roots/sampling/logging deprecated; error code "resource not found" ย้ายจาก -32002 → -32602
- Context: **97M+ SDK download/เดือน, 10,000+ MCP server** deployed แล้วก่อน RC นี้

## เกิดอะไรขึ้น
วันที่ 23 กรกฎาคม 2026 The Register กับ MCP maintainer เผยแพร่ **Model Context Protocol spec 2026-07-28 release candidate** — เป็น revision ใหญ่ที่สุดของโปรโตคอลตั้งแต่ launch ปลายปี 2024 — และประกาศว่าจะ **finalize วันจันทร์ที่ 28 กรกฎาคม 2026** (3 วันจาก brief นี้). Change ที่ใหญ่ที่สุด: **ตัด stateful หมด**. Protocol เดิมใช้ initialize handshake ที่ client + server ต้อง exchange capability + protocol version ก่อน, ใช้ `Mcp-Session-Id` header ผูก session, และต้อง sticky routing เพื่อให้ request ไปที่ backend เดียวกันตลอด conversation. สิ่งเหล่านี้ **หายหมด** ใน 2026-07-28 — capability + protocol version ย้ายไปอยู่ใน `_meta` object ของทุก request, ไม่มี session ที่ต้อง manage.

Feature ที่ graduate: **Tasks** ที่เดิมเป็น experimental extension ตอนนี้เป็น official extension — API ประกอบด้วย `tasks/get`, `tasks/update`, `tasks/cancel` (แต่ `tasks/list` ถูกลบเพราะ conflict กับ stateless design). Tasks แก้ปัญหา long-running work — เดิม client ต้อง keep connection open รอ result, ตอนนี้ server return task_id ทันที, client poll หรือ subscribe ทีหลัง. **MCP Apps** เป็น new feature — server render interactive HTML/CSS/JS ที่ agent host แสดงใน sandboxed iframe (agent สามารถ trigger UI form, wizard, dashboard ให้ user tap โดยตรง). Pattern นี้ตอบโจทย์ agent ที่ต้อง collect complex input จาก user — เดิมต้องคุยกันเป็น text หลาย turn, ตอนนี้ pop up form แล้วจบใน 1 interaction.

**OAuth 2.0/OIDC alignment** เป็น change ที่ enterprise ตั้งใจรอ. ผ่าน 6 SEPs (Spec Enhancement Proposals) MCP ตอนนี้: (a) validate `iss` claim ตาม RFC 9207 (protect against token substitution attack), (b) รองรับ `application_type` ใน Dynamic Client Registration (แยก native vs web vs service client), (c) มี External Managed Auth (EMA) pattern สำหรับ enterprise ที่ใช้ centralized identity provider (Okta, Auth0, Ping, Azure AD), (d) support token exchange (RFC 8693) สำหรับ delegated authorization. ก่อนหน้านี้ MCP ผ่าน security review ในองค์กร regulated (bank, insurance, healthcare) ไม่ได้เพราะ auth model ยัง loose; ตอนนี้ผ่านได้แล้ว.

Breaking change ที่ dev ต้องรู้: (1) **tasks/list ถูกลบ** — ถ้ามี code เดิมใช้ต้อง refactor ไป external task registry, (2) **roots, sampling, logging deprecated** — ยัง work ในช่วง transition แต่จะหายใน spec ถัดไป, (3) **error code migration** — "resource not found" ย้ายจาก `-32002` → `-32602` (align กับ JSON-RPC standard "invalid params"). MCP maintainer **David Soria Parra** เตือนสาธารณะ: "A lot of things that made MCP are gone" และบอกว่า custom implementation "will be a lot of uplift" — ตรงไปตรงมาว่าใครที่ build MCP server เองต้องเตรียม refactor cycle. Tier-1 SDK (Python, TypeScript, Go, C#) มี beta แล้ว, ให้ 10-week validation window ก่อน finalize.

Scale ของ ecosystem ตอนนี้: **97 ล้าน SDK download/เดือน** และ **10,000+ MCP server** deployed สาธารณะ + private (Anthropic, OpenAI, Google, Microsoft, AWS ทั้งหมด official adopt แล้ว). MCP กลายเป็น de facto agent-to-tool protocol ในไตรมาสที่ผ่านมา — 2026-07-28 RC คือ **การ mature จาก "Anthropic local protocol" เป็น "internet-scale infrastructure"**.

## ทำไมสำคัญ
**Stateless design แก้ปัญหาที่ block enterprise adoption มานานหลายเดือน**. เดิม remote MCP server ต้องมี session store (Redis, Memcached, DynamoDB) + sticky load balancer + connection tracking — architecture ที่ engineer platform ทุกทีมต้องแก้เอง. ตอนนี้ MCP server เป็น plain stateless HTTP microservice — deploy บน Cloudflare Workers, Vercel Edge, AWS Lambda, Google Cloud Run ได้ทันที ผ่าน round-robin load balancer ธรรมดา. Operational cost ลดลงหลายเท่า, และ integration timeline สั้นลงจาก 6 สัปดาห์เป็น 3 วัน (ประมาณจาก dev feedback ใน MCP GitHub discussion).

Pattern ใหญ่ที่ crystallize: **MCP เป็น "USB-C ของ AI"** — protocol ที่ standardize agent-to-tool connection ข้าม vendor. Zapier มี 5,000+ MCP server พร้อม deploy, Workato + MuleSoft + Boomi + n8n มี migration plan ประกาศแล้ว, HubSpot + Salesforce + ServiceNow + Notion + Linear + GitHub — ทุกเจ้ามี native MCP endpoint. Combined กับ Anthropic Claude Code + OpenAI Assistants API + Google Vertex Agent Builder + AWS Bedrock AgentCore ทั้งหมด **support 2026-07-28 spec ตั้งแต่วัน 1** — enterprise ที่ deploy agent ในไตรมาสหน้าไม่ต้องเลือก vendor stack แล้ว, เลือก tool ที่มี MCP endpoint ก็เชื่อมได้หมด.

Sub-signal สำหรับ security/compliance: **OAuth alignment ทำให้ MCP ผ่าน SOC 2, ISO 27001, FedRAMP, HIPAA audit** ได้เป็นครั้งแรก. ก่อนหน้านี้ team compliance ในบริษัท regulated block deployment เพราะ auth model ไม่ทำตาม RFC — วันนี้ argument นี้ตายลง. คาดว่า Q3-Q4 2026 จะเห็น regulated industry (bank, insurance, healthcare, government) roll out MCP-based agent เยอะขึ้นอย่างชัดเจน. Booz Allen federal survey (18% เห็น revenue impact จาก agent เดิม, ดู brief 22 ก.ค.) น่าจะกระโดดในไตรมาสหน้า.

## มุม AI Agent Platform
สำหรับ **builders** — audit custom MCP implementation ของตัวเองก่อน 28 ก.ค. checklist: (1) มี `Mcp-Session-Id` header ที่ต้อง refactor ไหม, (2) ใช้ tasks/list ที่ไหน — ต้องย้ายไป external task registry, (3) auth flow ต้อง align กับ OAuth 2.0/OIDC ที่ RFC 9207 spec ระบุ, (4) error code -32002 ต้อง remap เป็น -32602 ทุกที่, (5) roots/sampling/logging deprecation — plan migration ใน 6 เดือน. SDK Tier-1 (Python, TS, Go, C#) มี beta พร้อมใช้; MCP server ที่เขียนด้วย SDK ต้อง upgrade version แต่ต้องระวังภาษาอื่น (Rust, Java, PHP) ที่ community SDK อาจยังไม่ ready — เก็บ compatibility shim ไว้ 3 เดือน.

สำหรับ **enterprise integration platform** (Zapier, Workato, MuleSoft, Boomi, n8n, Tray, Prismatic) — 2026-07-28 เป็น **หลุมทองใหญ่**. Platform เหล่านี้มี tool integration + auth + connector อยู่แล้ว, expose เป็น stateless MCP endpoint ใช้เวลาเป็นสัปดาห์ ไม่ใช่เดือน. Product roadmap Q3 2026 ควรมี "MCP-native release" เป็น flagship — เพราะ agent developer จะ default MCP endpoint แทน custom connector อยู่แล้ว. ถ้ายังไม่มี MCP endpoint ในไตรมาสหน้า จะเสีย market share ให้ competitor ที่เร็วกว่า.

สำหรับ **enterprise buyers ที่กำลัง evaluate agent platform** — ใส่ "MCP 2026-07-28 compliance" เป็น **mandatory requirement** ใน RFP ทันที. Vendor ที่ support ไม่ได้ = vendor ที่ล้าหลัง 1 ไตรมาส; vendor ที่ support ได้ = future-proof integration ที่ swap tool ได้ตลอด. Talking point ใน contract negotiation: "vendor commit ว่าทุก tool integration จะ expose เป็น MCP endpoint ตาม spec 2026-07-28 ภายใน 90 วัน — ถ้าไม่ทำ contract SLA credit ให้ 5% ต่อไตรมาสที่ delay". นี่จะบังคับให้ vendor ต้อง prioritize protocol standard แทนการสร้าง proprietary API lock-in.

## Sources
- [MCP prepares to break with its stateful past (The Register, 23 ก.ค.)](https://www.theregister.com/devops/2026/07/23/model-context-protocol-prepares-to-break-with-its-stateful-past/5276722)
- [MCP 2026-07-28 Release Candidate (Official blog)](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
- [AI's most important protocol is getting easier to use (TechCrunch)](https://techcrunch.com/2026/07/20/ais-most-important-protocol-is-getting-a-little-bit-easier-to-use/)
- [Centralised OAuth/EMA for enterprise MCP (InfoQ)](https://www.infoq.com/news/2026/07/mcp-ema-enterprise-auth/)
- [MCP just went stateless — scaling on App Service (Microsoft Tech Community)](https://techcommunity.microsoft.com/blog/appsonazureblog/mcp-just-went-stateless-%E2%80%94-what-the-2026-spec-changes-about-scaling-on-app-servic/4530222)

---

## Audio script
สวัสดีครับ วันจันทร์ที่ยี่สิบแปดกรกฎาคมนี้ — สามวันจากนี้ — Model Context Protocol หรือ MCP จะปล่อย spec เวอร์ชันใหม่ 2026-07-28 เป็น revision ที่ใหญ่ที่สุดตั้งแต่ protocol เปิดตัว. Change สำคัญที่สุดคือตัด stateful ออกหมด — ไม่มี initialize handshake, ไม่มี session ID header, ไม่มี sticky routing. Capability + protocol version ย้ายไปอยู่ใน meta object ของทุก request. ผลกระทบเชิง practical — MCP server กลายเป็น plain stateless HTTP microservice ที่ deploy บน Cloudflare Workers, Vercel Edge, AWS Lambda ผ่าน load balancer ธรรมดาได้ทันที. เพิ่ม feature ใหม่: Tasks graduate จาก experimental เป็น official extension สำหรับ long-running work, MCP Apps ให้ server render interactive HTML ใน sandboxed iframe, และ OAuth 2.0 alignment ผ่าน 6 SEPs ที่ทำให้ enterprise regulated deploy ได้จริง. Ecosystem ตอนนี้มี SDK download เก้าสิบเจ็ดล้านต่อเดือน, MCP server หนึ่งหมื่นตัว. Breaking change ที่ต้องรู้: tasks/list ถูกลบ, roots/sampling/logging deprecated, error code resource not found ย้ายจาก minus สามสองศูนย์ศูนย์สองเป็น minus สามสองหกศูนย์สอง. Maintainer David Soria Parra เตือนตรงว่าใครที่ build MCP server เองต้องเตรียม refactor cycle. สำหรับ builder — audit custom implementation ก่อนวันจันทร์. สำหรับ enterprise integration platform อย่าง Zapier, Workato, MuleSoft — 2026-07-28 เป็นหลุมทองใหญ่ เพราะ expose tool ที่มีอยู่แล้วเป็น MCP endpoint ใช้เวลาแค่สัปดาห์เดียว. สำหรับ enterprise buyer ที่ evaluate agent platform ใส่ MCP 2026-07-28 compliance เป็น mandatory requirement ใน RFP ทันทีครับ.
