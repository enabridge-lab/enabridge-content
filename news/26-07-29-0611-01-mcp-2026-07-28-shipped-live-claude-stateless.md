---
date: 2026-07-29
slug: mcp-2026-07-28-shipped-live-claude-stateless
topic: openbridge-trend
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial isometric illustration on a deep navy background of a data
  center hallway with a giant blue-glowing gateway labeled "MCP 2026-07-28
  LIVE" and beneath it three stone tablets carved with "NO SESSIONS", "NO
  HANDSHAKE", "STATELESS CORE". To the right a scoreboard shows "400M
  DOWNLOADS/MO — 4x YoY" and "950 CLAUDE CONNECTORS". Cables flow from
  the gateway into serverless boxes labeled "LAMBDA · CLOUDFLARE · EDGE".
  Sharp editorial typography, cinematic depth, 1:1 aspect, no real human
  faces.
image: images/26-07-29-0611-01-mcp-2026-07-28-shipped-live-claude-stateless.png
---

# MCP 2026-07-28 ship จริงแล้ว — stateless core, no handshake, no session — Claude เปิดใช้ทันที กับ 950 connectors ที่ user ล้านคนใช้ทุกวัน

## TL;DR
- 28 ก.ค. spec ที่ Model Context Protocol เรียกว่า **largest update since launch** ship live พร้อมกับ Anthropic เปิดใช้ใน Claude ทันที
- Core change: **ตัด session, ตัด initialize handshake, ตัด Mcp-Session-Id header** — MCP กลายเป็น pure request/response แบบเดียวกับ HTTP → deploy บน **serverless / edge / behind load balancer** ได้แล้ว
- **MCP Apps** และ **Tasks** ship เป็น versioned extensions — interactive UI + long-running work มี formal path โดยไม่กระทบ core protocol
- Authorization align กับ **OAuth 2.0 + OIDC** production — เชื่อม Entra / Okta ตรง ไม่ต้อง workaround
- Scale ที่ Anthropic เปิด: **400M SDK downloads/เดือน (4x YoY)** + **950 MCP servers ใน Claude connectors directory** ที่มี user "millions daily"

## เกิดอะไรขึ้น
วันที่ 28 กรกฎาคม 2026 spec **MCP 2026-07-28** ที่ Anthropic + community pre-announce เป็น release candidate เมื่อ 21 พฤษภาคม — official ship live วันนี้. ทีม maintainer เรียกมันตรง ๆ ว่า *"the largest revision of the protocol since launch"* — และ **Anthropic ประกาศพร้อมกันว่า Claude รองรับ spec ใหม่ทันทีตั้งแต่วันแรก** ใน blog แยกที่ claude.com/blog/bringing-mcp-2026-07-28-to-claude.

Core change สั้น ๆ: **MCP เลิกเป็น stateful protocol**. SEP-2575 ตัด `initialize` handshake ที่ทุก session ต้องทำก่อน (บังคับให้ client + server จับคู่กันตั้งแต่ต้น), SEP-2567 ตัด `Mcp-Session-Id` header ที่ผูก request กับ session state บน server. หลังจากนี้ MCP request ทุกอันเป็น **self-contained, cacheable, routable** — บบเดียวกับ HTTP REST call. Server สามารถ deploy บน **AWS Lambda, Cloudflare Workers, Vercel Edge, หรือ scale horizontally behind load balancer** ได้ทันที โดยไม่ต้องพึ่ง sticky session, ไม่ต้อง shared cache, ไม่ต้อง WebSocket infra.

ส่วน **MCP Apps** (interactive UI ที่ server ส่งกลับมาให้ user render) และ **Tasks** (long-running work ที่ client poll ได้) — ทั้งสอง feature ที่ community ต้องการมาหลายเดือน — ship ภายใต้ **versioned extensions framework**. หมายความว่า core protocol ยัง stable ขณะที่ capability ใหม่ ๆ (agent-to-agent handoff, streaming binary, human-in-loop UI) เพิ่มเข้ามาโดยไม่ต้อง break existing implementation. **Authorization ก็เขียนใหม่หมด** — align กับ OAuth 2.0 + OIDC pattern ที่ enterprise identity provider (Microsoft Entra, Okta, Auth0) ใช้ในระบบ production อยู่แล้ว. Deprecate 3 core features เก่าที่ workaround รู้กันในวงจำกัด — ผู้พัฒนา server เก่าต้อง migrate ก่อน end of year.

ตัวเลขที่ Anthropic เปิดในโพสต์วันนี้บอก scale ของ ecosystem แล้ว: **MCP SDK downloads แตะ 400 ล้าน/เดือน — โต 4 เท่าในปีเดียว**. บน Claude เอง **connectors directory มี MCP server มากกว่า 950 ตัว** ที่ Anthropic บอกว่า *"used by millions of people every day"*. Numbers นี้ทำให้ MCP กลายเป็น **de facto industry standard** สำหรับเชื่อม AI agent กับ tool/data/system — สถานะที่ 6 เดือนก่อนยังไม่ชัด แต่ตอนนี้ค่อนข้าง lock แล้ว.

## ทำไมสำคัญ
**Stateless คือประตูให้ MCP scale ในโลกจริง.** ตลอดปีที่ผ่านมา MCP มีข้อจำกัดที่ enterprise architect รู้กันในวงในว่า *"deploy ยากบน cloud modern"* — session-based protocol ที่ต้อง sticky routing กัดกับ pattern serverless ที่ทุกที่ใช้อยู่. ทีม platform ต้องเลือกระหว่าง (1) รัน MCP server เป็น long-running process บน VM/container (แพง + scaling ยาก), หรือ (2) ทำ session-affinity layer เอง (fragile + operations pain). Spec ใหม่ **ยกข้อจำกัดนั้นออกทั้งชุด** — deploy MCP server บน Lambda/Workers/Edge ราคาเท่า API endpoint ธรรมดา, scale ตาม demand จริง ๆ, ไม่ต้องมี ops team ดูแล session store. นี่คือเหตุผลจริงที่ Anthropic บอกว่า *"reduces the complexity we manage, so we can ship more features to our customers, faster"* — Anthropic เอง burn compute ไปกับการ maintain session state ของทุก Claude user ที่ใช้ connector, และ stateless model ปลดล็อกทั้งชั้นนี้ออก.

Pattern ที่เห็นชัดตอนนี้คือ **MCP โต จนกลายเป็น protocol layer ที่คนต่อสู้กันเรื่อง extension ไม่ใช่ core**. Google A2A ที่ Linux Foundation host, IETF ที่พิจารณา standard track, Crunchbase MCP, Microsoft catalog 60+ ready-to-use MCP server, LangGraph 1.0 ที่ treat MCP tool เป็น first-class node — ทุกคน bet ว่า MCP จะเป็น TCP/IP ของ agentic AI. Spec 2026-07-28 ที่ **align กับ OAuth/OIDC + serverless-native** คือ signal ว่า MCP เริ่มเข้าเฟส *"maturity"* — infrastructure grade, ไม่ใช่ prototype อีกต่อไป. Vendor ที่ยังไม่ implement MCP server ในปี 2026 จะเจอ pressure เท่ากับ SaaS ที่ไม่มี REST API ในปี 2015.

## มุม AI Agent Platform
**Builders:** ถ้า maintain MCP server อยู่ — วางแผน migration ทันที. ตัด session code out ก่อน spec เก่า deprecate. ประโยชน์ที่ได้ทันที: **cost ลง 60-80%** จากการ deploy บน serverless, latency ลงจากการที่ CDN cache request ที่ static ได้ (list_tools, describe_tool). ถ้า build agent framework (LangGraph, CrewAI, Autogen, Mastra) — ต้อง support extensions framework ให้ครบ ไม่งั้นจะโดน framework ที่ support ก่อน (LangGraph 1.0 support แล้ว) กิน market share. คนที่จะ build MCP server ใหม่ปีนี้ — **บอก client ให้ default บน stateless core, ปฏิเสธ requirement ที่ต้องพึ่ง session** เพราะจะเป็น tech debt ทันทีเมื่อ deploy production.

**Users / business:** ถ้าองค์กรใช้ Claude Enterprise / ChatGPT Enterprise / Copilot อยู่ — ผลเห็นในไตรมาสหน้าเป็น **จำนวน connector ที่เพิ่มขึ้นเร็วมาก** เพราะ vendor deploy MCP server ง่ายขึ้นเท่าตัว. ทีม security ต้อง update policy: OAuth/OIDC ที่ MCP ใช้ตอนนี้เท่ากับที่ enterprise SSO ใช้อยู่ — เท่ากับ **MCP server ทุกตัวเข้า pipeline vetting เดียวกับ SaaS ใหม่** (audit scope, data flow, retention). ที่สำคัญ — **ถามให้ vendor confirm ว่า MCP server รองรับ 2026-07-28 spec** ก่อน commit — server เก่าที่ยังเป็น stateful จะขาด support ปลายปี.

**Ecosystem:** ผู้ชนะรอบนี้คือ **serverless / edge platform** (Cloudflare, Vercel, Fly.io, AWS Lambda) ที่กลายเป็น deployment target อันดับ 1 ของ MCP server ทันที. ผู้แพ้: vendor ที่ขาย **agent gateway / session-management layer** เป็น product แยก (บาง startup ปี 2025 build อยู่บนสมมติฐานว่า MCP session ยากจน enterprise ต้อง buy managed layer) — value prop นั้นหายเป็นเปอร์เซ็นต์ใหญ่. **Anthropic ได้เปรียบเชิง strategic** เพราะ 950 connector บน Claude directory มี network effect ที่ competitor ตามยาก — ทุก connector ใหม่ที่ build ให้ Claude ก็ทำงานกับ competitor ได้ทันที (MCP open standard), แต่ user base + discoverability อยู่ที่ Claude ก่อน. **Sovereign / regional builder ในไทย SEA** — window นี้เหมาะที่จะ deploy MCP server สำหรับ local system (Bitkub, K-Bank Open API, GBiz, ThaID) — enterprise ลูกค้าจะเริ่มถามในไตรมาสหน้าแน่นอน.

## Sources
- [MCP 2026-07-28 spec: stateless core, coming to Claude — Anthropic](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)
- [The 2026-07-28 Specification — MCP Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [AI Tool Protocol Drops Sessions Tomorrow: MCP's Largest Spec Change Since Launch — TechTimes](https://www.techtimes.com/articles/321671/20260727/ai-tool-protocol-drops-sessions-tomorrow-mcps-largest-spec-change-since-launch.htm)
- [MCP Goes Stateless: The 2026-07-28 Spec Explained — Nerd Level Tech](https://nerdleveltech.com/mcp-stateless-protocol-enterprise-authorization)
- [The biggest MCP spec update ships July 28 — WorkOS](https://workos.com/blog/mcp-2026-spec-agent-authentication)

---

## Audio script
เช้านี้เรื่องแรกคือ MCP spec 2026-07-28 ship จริงแล้ววันนี้ — ทีม Model Context Protocol เรียกว่าเป็น update ที่ใหญ่ที่สุดตั้งแต่ launch. Change ใหญ่ที่สุดคือ MCP เลิกเป็น stateful protocol — ตัด session, ตัด initialize handshake, ตัด session ID header ออกหมด. หลังจากนี้ MCP request ทุกอันเป็น self-contained แบบเดียวกับ HTTP — deploy บน AWS Lambda, Cloudflare Workers, Vercel Edge ได้ทันที ไม่ต้องพึ่ง sticky session อีก.

พร้อมกันนั้น Anthropic ประกาศว่า Claude รองรับ spec ใหม่ตั้งแต่วันแรก. Numbers ที่ Anthropic เปิดวันนี้บอก scale ของ ecosystem ชัด — MCP SDK downloads แตะ 400 ล้านต่อเดือน โต 4 เท่าในปีเดียว, บน Claude มี MCP server มากกว่า 950 ตัวที่ user ล้านคนใช้ทุกวัน. MCP กลายเป็น de facto industry standard สำหรับเชื่อม agent กับ tool แบบไม่มีคู่แข่งจริงจังแล้ว.

signal ที่สำคัญ: MCP เข้าเฟส maturity — infrastructure grade, ไม่ใช่ prototype. Vendor ที่ยังไม่ implement MCP server ปีนี้จะเจอ pressure เท่ากับ SaaS ที่ไม่มี REST API ในปี 2015. Cost ที่ทีม deploy MCP server จะลด 60-80% จากการย้ายไป serverless, และเพราะ authorization align กับ OAuth OIDC ที่ Entra Okta ใช้อยู่แล้ว — MCP server จะเข้า pipeline vetting เดียวกับ SaaS ตัวอื่น.

สำหรับทีม builder ในไทย — window นี้เหมาะที่จะ deploy MCP server สำหรับ local system อย่าง Bitkub, K-Bank Open API, GBiz หรือ ThaID เพราะ enterprise ลูกค้าจะเริ่มถามในไตรมาสหน้าแน่นอน.
