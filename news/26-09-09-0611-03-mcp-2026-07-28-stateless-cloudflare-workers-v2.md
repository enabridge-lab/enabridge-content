---
date: 2026-09-09
slug: mcp-2026-07-28-stateless-cloudflare-workers-v2
topic: openbridge-trend
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial isometric illustration of a protocol handshake being cut with
  scissors: on the left a bulky server tower stamped "STATEFUL SESSION"
  crumbles; on the right a lean Cloudflare Worker cube glows labeled
  "STATELESS 2026-07-28". Above them a big header reads "NO SESSION ID —
  EVERY REQUEST SELF-DESCRIBING". Small chips float: "SENTRY LIVE",
  "LINEAR LIVE", "AGENT SDK v0.20". Muted indigo and neon-orange palette,
  dramatic rim lighting, high contrast typography for a 200px thumbnail,
  1:1 aspect, no real human faces.
image: images/26-09-09-0611-03-mcp-2026-07-28-stateless-cloudflare-workers-v2.png
---

# MCP 2026-07-28 spec ทิ้ง session state ทั้งชั้น — Cloudflare Workers รัน MCP server ไม่ต้องใช้ Durable Object, Sentry + Linear เข้า production วันแรก, protocol foundation shift ที่ agent runtime ต้อง port ก่อนสิ้นปี

## TL;DR
- **MCP 2026-07-28 specification** (release candidate) ประกาศเป็น **biggest change since launch** — protocol core กลายเป็น **stateless เต็มระบบ**: ตัด `initialize` / `initialized` handshake + `Mcp-Session-Id` header ออก, request ทุก call self-describing (protocol version + client info + capabilities ใน `_meta`)
- **Cloudflare Agents SDK v0.20** + **Cloudflare product MCP servers** ready day zero — MCP server เดี๋ยวนี้ run ใน **single Worker ไม่ต้องใช้ Durable Object, no sticky session, no open stream**
- **Sentry + Linear** เข้า production ตั้งแต่วันแรก — signals ว่า enterprise adoption ไม่ต้องรอไตรมาสสอง
- **December 2025**: Anthropic donate MCP ให้ **Agentic AI Foundation (Linux Foundation)** — OpenAI + Block เป็น co-founder, AWS + Google + Microsoft + Cloudflare + GitHub + Bloomberg เป็น supporting member
- **Multi Round-Trip Requests** + **header-based routing** + **cacheable list results** + **formal extensions framework** — spec expansion ที่ตั้งใจให้ MCP scale ผ่าน CDN + gateway ได้ตรง

## เกิดอะไรขึ้น

**28 กรกฎาคม 2026** Anthropic (ตอนนี้ Linux Foundation) ปล่อย **MCP specification 2026-07-28 (release candidate)** — spec update ที่ทั้ง protocol council + reference implementer เรียกว่า **biggest change since MCP launched**. Core shift คือ **statelessness เต็มระบบ** — ตัด `initialize` / `initialized` handshake + `Mcp-Session-Id` header ออกทั้งหมด. request ทุก call ตอนนี้เดินคนเดียว, carry ทั้ง protocol version, client identity, capabilities inline ใน `_meta` field. gateway route ได้ด้วย required `method` + `tool-name` header — routing ไม่ต้อง parse JSON body ก่อน (latency ต่ำลง 30-50% ในไตรมาสที่วัด)

**Cloudflare ships day-zero support**. Agents SDK v0.20 ปล่อยพร้อม spec — Cloudflare product-specific MCP server ทุกตัว (Workers, R2, D1, KV, Durable Objects, Queues) รัน spec ใหม่ที่ **fresh stateless server ต่อ request, ไม่มี MCP protocol session, ไม่มี protocol-specific Durable Object**. Cloudflare Dev twitter อธิบาย simply: "MCP server run ใน single Worker, no sticky sessions, no open streams, no Durable Objects needed — production กับ Sentry + Linear แล้ว". เป็น architecture ที่คนที่ build MCP server ระดับ scale (10K+ concurrent agent) รอมานาน — pattern เดิม stateful ทำให้ CDN cache ไม่ได้, load balancer sticky ต้อง maintain, connection pool exhaust ที่ traffic spike

**Spec feature ใหม่** ที่ยัง underappreciated: (1) **Multi Round-Trip Requests** — client ระบุได้ว่า tool call จะมี multi-turn interaction (elicitation) โดย server ไม่ต้อง maintain state ระหว่าง turn; (2) **header-based routing** — gateway อ่าน `mcp-method: tools/call` + `mcp-tool-name: search` แล้ว route ได้เลยโดยไม่ parse body — สำคัญมากสำหรับ shared MCP gateway ที่ serve หลาย tenant; (3) **cacheable list results** — `tools/list` response cache ได้ที่ CDN ระดับวันที่เนื่องจาก idempotent — server load ลดลงหลายเท่า; (4) **authorization hardening** — token binding เข้ม, revocation flow เร็ว, delegation model ชัด; (5) **formal extensions framework** — vendor เพิ่ม feature ได้โดยไม่ break interoperability (แก้ปัญหา MCP + WebMCP + A2A protocol fragmentation)

**Governance shift ที่คู่กัน** — เดือน **ธันวาคม 2025** Anthropic donate MCP ให้ **Agentic AI Foundation ใต้ Linux Foundation**. OpenAI + Block เข้าเป็น **co-founder** (สัญลักษณ์สำคัญ — คู่แข่ง commercial ยอม share governance); AWS, Google, Microsoft, Cloudflare, GitHub, Bloomberg เป็น **supporting member**. ผลกระทบตอนนี้: MCP spec release cycle อยู่ใต้ neutral foundation, contributor เพิ่มเป็น 500+, RFC process open, breaking change ต้องผ่าน multi-vendor review — เป็นสาเหตุที่ 2026-07-28 spec ผ่านออกได้เป็น RC ทันในไตรมาสหนึ่งหลัง draft, ไม่ delay แบบ private-project spec

Reference implementer ที่ signal enterprise readiness: **Sentry + Linear** ประกาศ production adoption วันแรก. **AWS AgentCore Gateway + Bedrock** จะรองรับใน update ถัดไป (docs.aws.amazon.com/bedrock-agentcore roadmap). **Google Cloud Vertex AI Agent Engine** จะ support ใน Q4 (Google Developers Blog "Scaling AI Agent Infrastructure with MCP Stateless"). **GitHub Copilot MCP server catalog** update spec ไปเรียบร้อยแล้ว. **NPM registry MCP** จะเปลี่ยน default ในเดือนหน้า. **The New Stack** อธิบายว่านี่คือ "MCP's biggest growing pains for production use will soon be solved"

## ทำไมสำคัญ

**Pattern signal**: **Statelessness = CDN-first architecture**. ก่อน 2026-07-28, MCP server run ได้แต่ที่ server ที่ hold session state — sticky routing + connection pool + memory. หลัง spec ใหม่, MCP server run ใน serverless function ที่ scale infinitely ที่ edge (Cloudflare Workers, AWS Lambda@Edge, Vercel Edge, Deno Deploy). **นี่คือ pattern REST 2.0 ที่ทำให้ web scale ทั้งใน 2010s** — MCP ถอดบทเรียนเดียวกัน 15 ปีหลัง. คำถามที่ InfoQ ยก "MCP Goes Stateless, and Developers Ask Whether That Just Makes it an API Again" — จริงส่วนหนึ่ง แต่ MCP ยัง carry semantic tool discovery + prompt/resource/elicitation abstraction ที่ REST ไม่มี — ยัง protocol แต่ deploy pattern เหมือน REST

Bet ที่จับตา: **AWS AgentCore Gateway จะ compete กับ Cloudflare Monetization Gateway ในไตรมาสหน้า**. ทั้งสอง gateway ยืน layer เดียวกัน — จับ traffic ระหว่าง agent + MCP tool, apply policy, monetize. Cloudflare ได้เปรียบเรื่อง edge presence + latency; AWS ได้เปรียบเรื่อง integration กับ agent runtime + spending policy + IAM. **Google Vertex + Anthropic Claude API + OpenAI Response API** จะปล่อย gateway ของตัวเองภายในสิ้นปี — เกิดเป็น **4 MCP gateway ที่แข่ง protocol เดียวกัน** = network effect ให้ MCP standard, competition ให้ price / feature

Deep signal ที่ subtle: **statelessness ปิด attack surface ใหญ่ที่ MCP security research ปีนี้เจอ**. session state ที่ hold ระหว่าง call เป็นที่เก็บ token, credential, cached tool response — attacker ที่ hijack session เข้าถึงทุกอย่างที่ agent สะสม. spec ใหม่ที่ทุก request self-describing + token bound ต่อ call, credential ไม่ persist ใน server memory ระหว่าง call — **attack window ลดจากเซสชั่นเป็น request เดียว**. ตรงกับ pattern Broadcom AgentMinder deny-by-default ที่ report สัปดาห์ที่แล้ว — enterprise security narrative รอบใหม่คือ **"agent runtime ต้อง minimize persistent state"**

**Timing implication**: ทีมที่ build MCP server ก่อน 2026-07-28 ต้อง **plan migration ภายใน Q4** — server ที่ยัง require session handshake จะไม่ compatible กับ gateway ใหม่ + Cloudflare Workers execution. ทีมที่ start build ตอนนี้ควร **skip stateful pattern เลย** — เหมือน team ที่เพิ่ง build web app ปี 2015 skip Flash + jQuery ไปเขียน React ตรง

## มุม AI Agent Platform

**Builders**: ถ้าคุณ maintain MCP server, **checklist migration**: (1) remove `initialize` / `initialized` handshake, ทำ request self-describing; (2) migrate session-scoped state ไป external store (Redis, D1, DynamoDB) หรือ encode ใน request context; (3) implement `mcp-method` + `mcp-tool-name` header emission; (4) mark idempotent list results ให้ `Cache-Control: max-age=86400`; (5) test authorization hardening flow + token binding. Cloudflare Agents SDK v0.20 มี migration guide + `mcp-server-cloudflare` เป็น reference implementation. **ถ้าคุณ build agent client**, LangChain / LangGraph / OpenAI Agents SDK / Google ADK / AWS Strands ต้อง upgrade MCP client library ก่อน connect ไปที่ server รุ่นใหม่ — old client + new server = handshake error

**Users / Business**: enterprise ที่ deploy MCP server (SAP MCP, ServiceNow MCP, DocuSign MCP, Salesforce MCP, custom internal MCP) ต้อง audit **inventory MCP server ทั้งหมด** และ **spec version ที่รัน** — server ที่ยัง run pre-2026-07-28 อาจ compatible กับ agent runtime ปัจจุบันแต่ break พอ AgentCore + Vertex + Copilot upgrade spec version ในไตรมาสหน้า. **budget allocation** สำหรับ Q4: MCP server upgrade + gateway migration + observability re-configuration. **Vendor conversation ที่ควรเปิดตอนนี้**: "MCP server ของท่านรองรับ 2026-07-28 หรือไม่, roadmap upgrade เมื่อไหร่, breaking change ที่ต้องเตรียม?"

**Ecosystem**: (1) **Winner (short-term)**: Cloudflare — ready day zero + product MCP server เต็ม stack + agent SDK ที่ทำ pattern สำเร็จรูป; (2) **Winner (protocol governance)**: Linux Foundation + Agentic AI Foundation — neutral standard body ที่ทำให้ enterprise + regulator ยอมรับ MCP เป็น de-facto layer; (3) **Ambiguous**: A2A (Google) — protocol คู่ขนานที่ target inter-agent communication แต่ยังไม่รวมกับ MCP; ถ้า A2A + MCP รวมได้ในสเปคเดียวใน 2027, agent interop จะเข้าสู่ยุคใหม่; (4) **Loser (transitional)**: proprietary tool integration vendor ที่ยังไม่ปล่อย MCP endpoint — customer จะ default ไปหา MCP-native alternative ก่อน. **สำหรับ Enabridge**: opportunity ตรงในการเป็น **MCP migration + observability layer สำหรับ Thai enterprise** — พอ SAP MCP, Salesforce MCP, ServiceNow MCP ต้อง version-migrate พร้อมกัน, มี partner ที่ handle multi-vendor migration + testing + rollback จะเป็น service ที่ enterprise ยอมจ่ายพรีเมี่ยม

## Sources
- [MCP Blog — The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [Cloudflare Blog — The next generation of MCP](https://blog.cloudflare.com/mcp-v2/)
- [Cloudflare Changelog — Cloudflare MCP servers support the new MCP 2026-07-28 Specification](https://developers.cloudflare.com/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/)
- [InfoQ — MCP Goes Stateless, and Developers Ask Whether That Just Makes it an API Again](https://www.infoq.com/news/2026/08/mcp-stateless-gateway/)
- [Google Developers Blog — Scaling AI Agent Infrastructure with the MCP Stateless updates](https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/)
- [The New Stack — MCP's biggest growing pains for production use will soon be solved](https://thenewstack.io/model-context-protocol-roadmap-2026/)

---

## Audio script
MCP protocol spec ปล่อย version สอง พัน ยี่สิบหก ศูนย์เจ็ด ยี่สิบแปด. เป็น biggest change since launch. Protocol core กลายเป็น stateless ทั้งระบบ. ตัด initialize handshake. ตัด session ID header. request ทุก call self describing. carry protocol version client identity capabilities inline ใน meta field. gateway route ได้ด้วย header ไม่ต้อง parse JSON.

Cloudflare ship day zero. Agents SDK v ศูนย์ จุด สอง ศูนย์. product MCP server ทั้งหมดรัน spec ใหม่. fresh stateless server ต่อ request. ไม่ต้องใช้ Durable Object. ไม่ต้องมี sticky session. Sentry Linear เข้า production วันแรก.

Feature ใหม่ที่ underappreciated. multi round trip requests. header based routing. cacheable list results. authorization hardening. formal extensions framework. gateway ที่ serve หลาย tenant ทำได้ง่ายมาก. list result cache ที่ CDN ระดับวัน. server load ลดลงหลายเท่า.

Governance shift ที่คู่กัน. ธันวาคม สอง พัน ยี่สิบห้า Anthropic donate MCP ให้ Agentic AI Foundation ใต้ Linux Foundation. OpenAI Block เป็น co founder. AWS Google Microsoft Cloudflare GitHub Bloomberg เป็น supporting member. release cycle อยู่ใต้ neutral foundation. contributor เพิ่มเป็นห้าร้อยกว่า. RFC process open.

Pattern signal. Statelessness เท่ากับ CDN first architecture. ก่อนหน้านี้ MCP server ต้อง hold session. sticky routing connection pool memory. หลัง spec ใหม่ MCP server run ใน serverless function ที่ edge. Cloudflare Workers Lambda Edge Vercel Edge Deno Deploy. เหมือน REST สอง จุด ศูนย์ ที่ทำให้ web scale ปี สอง พัน สิบ. MCP ถอดบทเรียนเดียวกัน สิบห้า ปีหลัง.

Bet ที่จับตา. AWS AgentCore Gateway compete กับ Cloudflare Monetization Gateway ในไตรมาสหน้า. Google Vertex Anthropic OpenAI จะปล่อย gateway ของตัวเองภายในสิ้นปี. เกิดเป็น สี่ MCP gateway ที่แข่ง protocol เดียวกัน. network effect ให้ standard. competition ให้ price feature.

Deep signal. statelessness ปิด attack surface ใหญ่ที่ MCP security research ปีนี้เจอ. session state ที่ hold ระหว่าง call เป็นที่เก็บ token credential cached response. attacker ที่ hijack session เข้าถึงทุกอย่าง. spec ใหม่ credential ไม่ persist ใน server memory. attack window ลดจาก session เป็น request เดียว.

สำหรับ builder. migration checklist. remove initialize handshake. migrate session scope state ไป external store. implement method tool name header. mark idempotent list result ให้ cacheable. test authorization hardening flow.

สำหรับ Thailand enterprise. audit inventory MCP server ทั้งหมด. version ที่รัน. server pre spec ใหม่จะ break ในไตรมาสหน้า. เตรียม budget Q สี่ สำหรับ MCP server upgrade gateway migration.
