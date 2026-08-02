---
date: 2026-08-03
slug: mcp-2026-07-28-stateless-serverless-agent-protocol
topic: agentic-ai
reading_time_min: 5
sources: 8
image_prompt: |
  Editorial isometric illustration of a network diagram morphing from a
  cluttered stateful mesh into a clean stateless grid. On the left, a
  tangle of server nodes wired with thick "SESSION" cables, one blinking
  red. On the right, identical serverless "MCP" nodes arranged in a clean
  grid behind a plain round-robin load balancer; each node lit green with
  the label "STATELESS". A bold banner across the top reads
  "MCP 2026-07-28" and a stat block underneath shows "400M SDK DOWNLOADS"
  and "4x YoY". A small foundation seal in the corner reads "AAIF /
  LINUX FOUNDATION". Deep navy + electric cyan palette, chiaroscuro
  editorial style, 1:1 aspect, no real human faces, text sharp at 200px
  thumbnail.
image: images/26-08-03-0612-01-mcp-2026-07-28-stateless-serverless-agent-protocol.png
---

# MCP 2026-07-28 = ทิ้ง session, เดิน stateless — protocol ที่กำลังกลายเป็น "HTTP ของ agent" ในสัปดาห์เดียว

## TL;DR
- **28 ก.ค.** — Agentic AI Foundation (AAIF ใต้ Linux Foundation) ปล่อย **MCP spec 2026-07-28** — update ใหญ่สุดตั้งแต่ Anthropic เปิดตัว protocol เมื่อ 20 เดือนก่อน
- **ทิ้ง stateful core ทั้งหมด** — `initialize` handshake หายไป, `Mcp-Session-Id` หายไป, ทุก request เป็น self-describing ผ่าน `_meta` + HTTP header. Server รันบน serverless/edge ได้ทันที, sticky session ไม่จำเป็น, load-balance แบบ plain round-robin
- ปิดด้วย **official extension 3 ตัว**: MCP Apps (server-rendered UI), Tasks (async/long-running), Enterprise Managed Auth (IdP-based org provisioning). Tier-1 SDK (TypeScript, Python, Go, C#) upgrade วันเดียวกัน
- **Ecosystem response ใน 48 ชม.**: AWS Bedrock AgentCore Gateway ประกาศ compat, Cloudflare Workers MCP template, Vercel + Netlify serverless template, Anthropic Claude Desktop client rollout, OpenAI ChatGPT connector migrate. **MCP ผ่านหลัก 400M SDK download/เดือน — โต 4x YoY**

## เกิดอะไรขึ้น

วันที่ 28 กรกฎาคม Agentic AI Foundation (AAIF — directed fund ใต้ Linux Foundation ที่ Anthropic บริจาค MCP ให้เมื่อธันวาคม 2025, มี OpenAI, Google, Microsoft, AWS, Block เป็น platinum member) ปล่อย **Model Context Protocol specification 2026-07-28** — update ใหญ่ที่สุดตั้งแต่ Anthropic ประกาศ MCP เมื่อ พฤศจิกายน 2024. Anthropic เขียน blog ตอบรับในชื่อ "Bringing MCP 2026-07-28 to Claude" ภายในไม่กี่ชั่วโมง; Cloudflare, Vercel, Netlify, Fly.io ประกาศ serverless template ในวันเดียวกัน; AWS ตามด้วย **AgentCore Gateway supports MCP 2026-07-28 spec** บน ML Blog ในวันที่ 29 ก.ค.

Headline change: **stateless core**. Protocol เดิม (ตั้งแต่ 2024) เป็น bidirectional stateful — client ต้องเปิด `initialize` handshake, แลก `Mcp-Session-Id`, server ต้องเก็บ session state, ต้องมี sticky routing หรือ shared session store (Redis, Memcached) เพื่อ scale horizontal. Spec ใหม่ตัดทั้งหมดทิ้ง. **ทุก request เป็น self-describing** — protocol version, client identity, capabilities ทั้งหมด encode ใน `_meta` object + HTTP header. Server รันเหมือน HTTP service ธรรมดา — request landing บน server instance ไหนก็ได้ ผ่าน round-robin load balancer, serverless function (Lambda, Cloudflare Workers, Vercel Functions), edge runtime, ทั้งหมด compatible ทันที. ผู้ maintain รายหนึ่งบอก TechTimes ว่า "ก่อนหน้านี้ MCP รู้สึกเหมือน WebSocket — ตอนนี้เป็น REST"

ปิดด้วย **official extension สามตัว**. **MCP Apps** — server-rendered UI ที่ให้ tool call แสดง widget แบบ progressive disclosure (adopt โดย Claude, ChatGPT, VS Code Copilot, Goose, Postman ก่อนหน้า). **Tasks** — async / long-running operation support (background research, big data pipeline, multi-hour code build) — client polling หรือ webhook callback. **Enterprise Managed Auth** — IdP-based (Okta, Entra, Ping) org-wide provisioning + scope authorization ที่ก่อนหน้า enterprise ต้อง hack เอง. Tier-1 SDK ทั้งสี่ (TypeScript, Python, Go, C#) upgrade complete ในวัน 28 ก.ค. เอง. Adoption metric: MCP ผ่านหลัก **400M SDK download/เดือน — โต 4x YoY**; Gartner คาด 75% ของ API gateway vendor จะ ship MCP feature ก่อนสิ้น 2026

## ทำไมสำคัญ

**MCP กำลังกลายเป็น "HTTP ของ agent" ตัวจริง** — คำที่ Anthropic + AAIF พูดมาหลายไตรมาส เพิ่งจริงจังขึ้นวันนี้. เพราะ stateless คือ criterion เดียวที่ทำให้ **protocol scale ไป production infrastructure grade**. Stateful protocol = ต้องแบก session state, ต้อง sticky routing, ต้อง shared store, ต้อง reconnect logic, ต้อง failure recovery — ทั้งหมดคือ operational tax ที่ enterprise ปฏิเสธมา 20 ปีก่อนตอน SOAP → REST. เมื่อ MCP ทิ้ง state ทิ้ง handshake, มันเข้ากับ platform ที่มีอยู่แล้ว — CloudFront + Lambda, Cloudflare Workers, GCP Cloud Run — โดยไม่ต้อง redesign infra. **หมายความว่า SI ที่ deploy agent ให้ enterprise ไม่ต้อง justify "ทำไมต้องมี MCP session store" ให้ CTO ฟัง** — เพียงแค่บอก "เหมือน API endpoint ปกติ" จบ. Deployment velocity ที่ประหยัด 60-80% (คำ AWS)

**Governance signal สำคัญกว่า technical spec**. Update นี้ปล่อยภายใต้ **AAIF Linux Foundation ไม่ใช่ Anthropic** — เป็นครั้งแรกที่ protocol ตัดสินใจร่วมกันโดยหกบริษัท (Anthropic, OpenAI, Google, Microsoft, AWS, Block) ผ่าน RFC process. หมายความ **ไม่มี vendor ใดจะ fork ทิศทาง MCP ได้อีก** — ลด risk lock-in ที่ CIO กลัวมากที่สุด. ต่างจากเมื่อ 6 เดือนก่อนที่ Google ประกาศ A2A protocol แข่ง (ตอนนี้ A2A v1.0 อยู่ใต้ AAIF เดียวกัน) — layering ชัด: MCP = tool access, A2A = agent-to-agent coordination, Streamable HTTP = transport. **Enterprise procurement team วันนี้เขียน RFP ได้แล้วว่า "must support MCP 2026-07-28 + A2A v1.0"** — vendor ทุกเจ้าต้อง comply

**Ecosystem response ใน 48 ชม. = signal ว่า MCP ได้เข้าสถานะ standard จริง** — ไม่ใช่แค่ Anthropic push. Cloudflare ปล่อย Workers MCP template, Vercel ปรับ ai-sdk MCP adapter, Netlify Functions template, Fly.io Machine template, AWS AgentCore Gateway update — ทั้งหมดใน 24-48 ชม. Compare กับ MCP release ก่อนหน้า (2025-11-25 spec) ที่ใช้เวลา 3-4 สัปดาห์กว่า cloud vendor จะ ship template. **นี่คือ moment ที่ MCP หยุดถูก judge ด้วย "adoption speed" แล้วเริ่มถูก judge ด้วย enterprise-grade criterion** — governance, identity, audit, scalability

## มุม AI Agent Platform

**สำหรับ builders:** ถ้ากำลัง build agent framework, MCP server, หรือ tool integration — **migrate ไป 2026-07-28 spec ภายใน 2 สัปดาห์**. Stateful implementation (session-based) จะกลายเป็น legacy ภายใน Q4. Priority action list: (1) ลบ `initialize` handshake logic, (2) ย้าย server state ไป external store (ถ้าจำเป็นจริง — ส่วนใหญ่ไม่จำเป็น), (3) implement Enterprise Managed Auth extension ก่อนเพราะ IdP-integration เป็น first thing ที่ enterprise buyer ถาม, (4) ถ้ามี MCP server อยู่ — publish deployment template สำหรับ Cloudflare Workers / AWS Lambda / Vercel / GCP Cloud Run (จะได้ organic distribution จาก MCP registry). **ถ้ากำลังสร้าง framework** (LangChain, LlamaIndex, Mastra, Vercel AI SDK) — ต้อง support MCP Apps extension ทันทีเพราะ UI-rich tool = differentiator หลักในไตรมาส 3-4

**สำหรับ users/business:** Enterprise IT team ที่มี MCP server production อยู่แล้ว (คาด 15-20% ของ Fortune 2000 หลังจาก Anthropic + OpenAI + Google ship connector) — **ประเมิน migration cost ก่อนสิ้นสิงหาคม**. เป็น breaking change แต่ backward-compat mode มี 6 เดือน; หลังจากนั้น server เก่าจะ deprecate. Business benefit ที่ควร pitch CFO: **operating cost ของ MCP server ลด 40-70%** เพราะ serverless + edge deploy ทำให้ pay-per-request แทน always-on VM. Thai enterprise ที่ยังอยู่ในเฟส pilot (SCB, K-Bank, PTT, Bangchak, CPALL) — ควรเขียน MCP 2026-07-28 เป็น requirement ใน RFP renewal 2027 ทันที; ถ้า vendor ไหนไม่ commit ให้ตัดออก shortlist

**สำหรับ ecosystem:** Winners ชัด — **Cloudflare Workers + Vercel + Netlify + Fly.io** เพราะ serverless MCP = first-time market ที่ hyperscaler ยังไม่ค่อยครอง. **AWS AgentCore Gateway** ได้ประโยชน์เพราะ position ตัวเองเป็น managed MCP router (bill per request). **Anthropic + OpenAI + Google** ได้ moat เล็กน้อยเพราะ client-side implementation ยัง lock ผ่าน SDK ของตัวเอง. Losers: **API gateway ที่ยังไม่ ship MCP** (Kong, Apigee, Tyk, WSO2) — เสี่ยง lose enterprise seat ใน 12 เดือนถ้าไม่ update roadmap; **MCP session store vendor** (ถ้ามี — Redis-based products) — feature relevance หายไป. Enabridge angle: ทีมที่ deploy agent ให้ Thai enterprise บน Bedrock/Foundry — ประกาศเป็น MCP 2026-07-28 native SI ตัวแรกใน SEA, กลายเป็น reference architect ที่ hyperscaler channel manager แนะนำ

## Sources
- [The 2026-07-28 Specification — Model Context Protocol Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [Bringing MCP 2026-07-28 to Claude — Anthropic](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)
- [MCP just got its biggest update ever — VentureBeat](https://venturebeat.com/infrastructure/mcp-just-got-its-biggest-update-ever-heres-what-changes-for-ai-agents)
- [Anthropic Rebuilds MCP as Stateless — AlphaSignal](https://alphasignal.ai/news/anthropic-rebuilds-mcp-as-stateless-unlocking-serverless-ai-agent-deployments)
- [MCP is now stateless: what the 2026-07-28 update changes — flaviocopes.com](https://flaviocopes.com/mcp-2026-07-28-stateless/)
- [Stateless MCP Ecosystem Adoption — Agentic AI Foundation](https://aaif.io/blog/the-ecosystem-responds-to-stateless-mcp)
- [MCP Just Went Stateless — DigitalApplied](https://www.digitalapplied.com/blog/mcp-2026-07-28-stateless-spec-agent-infrastructure-2026)
- [How AgentCore Gateway supports MCP 2026-07-28 spec — AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/how-agentcore-gateway-supports-the-mcp-2026-07-28-spec/)

---

## Audio script
วันที่ 28 กรกฎาคม Agentic AI Foundation ใต้ Linux Foundation ปล่อย MCP spec เวอร์ชั่นใหม่ ชื่อ 2026-07-28. เป็น update ใหญ่สุดตั้งแต่ Anthropic เปิด protocol เมื่อ 20 เดือนก่อน. หัวใจของ change คือคำเดียว — stateless.

ก่อนหน้า MCP เป็น bidirectional stateful — client ต้องเปิด initialize handshake, แลก session id, server ต้องเก็บ state, ต้องมี sticky routing. Spec ใหม่ตัดทั้งหมดทิ้ง. ทุก request เป็น self-describing ผ่าน HTTP header. Server รันบน serverless หรือ edge ได้ทันที. Cloudflare Workers, Lambda, Vercel Functions ทั้งหมด compatible ในวันเดียว. เพิ่ม official extension 3 ตัว — MCP Apps สำหรับ server-rendered UI, Tasks สำหรับ async operation, Enterprise Managed Auth สำหรับ IdP-based provisioning.

Signal สำคัญ — MCP กำลังกลายเป็น HTTP ของ agent ตัวจริง เพราะ enterprise buyer ปฏิเสธ stateful protocol มา 20 ปีตั้งแต่สมัย SOAP ไป REST. เมื่อทิ้ง state, MCP เข้ากับ platform เดิม โดยไม่ต้อง redesign infra. SI ที่ deploy agent ประหยัด 60-80% operational cost. Ecosystem ตอบใน 48 ชั่วโมง — AWS AgentCore Gateway, Cloudflare, Vercel, Netlify ship template หมด. MCP ผ่าน 400 ล้าน SDK download ต่อเดือน โต 4 เท่า YoY. สำหรับ Enabridge — ถ้ากำลัง pitch Thai bank เรื่อง agent deployment, เขียน MCP 2026-07-28 เป็น mandatory line ใน RFP renewal 2027 ทันที.
