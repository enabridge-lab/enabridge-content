---
date: 2026-07-10
slug: mcp-2026-07-28-stateless-spec-enterprise-auth-ga
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  A wide editorial isometric scene: a giant server hall labeled "MCP 2026-07-28"
  with three billboard rows on the wall — "STATELESS HTTP", "MCP APPS + TASKS",
  "ENTERPRISE AUTH GA". Old sticky-session boxes labeled "Mcp-Session-Id" and
  "shared store" being carted away by tiny suited silhouettes toward a dumpster;
  a plain round-robin load balancer glowing in the center routing arrows to
  identical worker pods stamped "ANY INSTANCE, ANY REQUEST". Along the top,
  four logos as billboards: "ANTHROPIC", "MICROSOFT", "OKTA", "78% F500".
  High contrast editorial cinematic lighting, 1:1 aspect, readable at 200px
  thumbnail, no real human faces.
image: images/26-07-10-0608-01-mcp-2026-07-28-stateless-spec-enterprise-auth-ga.png
---

# MCP 2026-07-28 กำลังจะออก — Stateless HTTP + Enterprise Auth GA = agent protocol โตขึ้นเป็น enterprise-grade แล้ว

## TL;DR
- Model Context Protocol ประกาศ **release candidate ของ spec 2026-07-28** (lock spec วันที่ 21 พ.ค., publish 28 ก.ค.) — เป็น revision ใหญ่สุดตั้งแต่ launch: **ยกเลิก initialize/initialized handshake + Mcp-Session-Id header ทั้งหมด → protocol กลายเป็น fully stateless บน commodity HTTP**
- **Enterprise-Managed Authorization extension เลื่อนขึ้น stable status** — enterprise ทำ centralized access control ผ่าน IdP ของตัวเองได้ (OAuth + OIDC), Anthropic + Microsoft + Okta adopt แล้ว
- ตัวเลข adoption ล่าสุด — **78% ของ enterprise AI team มี MCP ใน production, 28% ของ Fortune 500 run MCP server, 97M SDK download/เดือน, 10,000+ public MCP server** — signal ว่า MCP กำลังกลายเป็น TCP/IP ของ agent layer

## เกิดอะไรขึ้น
กลางสัปดาห์นี้ (7 ก.ค. 2026) ทีม Model Context Protocol เผยแพร่ **release candidate ของ spec รุ่น 2026-07-28** — spec ถูก lock ตั้งแต่ 21 พ.ค., มาตรฐาน final จะ publish 28 ก.ค. หัวใจของการเปลี่ยนแปลง 3 อย่าง: (1) **stateless HTTP core** — ยกเลิก initialize/initialized handshake + Mcp-Session-Id header, request ไหนก็วิ่งไป server instance ไหนก็ได้โดยไม่ต้องมี sticky session หรือ shared session store; (2) **extensions framework** — capability ใหญ่อย่าง MCP Apps (server ส่ง interactive HTML UI ให้ host render ใน sandboxed iframe) และ Tasks (long-running work ที่ client drive ผ่าน tasks/get, tasks/update, tasks/cancel) ship บน timeline แยกได้; (3) **lifecycle policy** — implementer มั่นใจได้ว่า agent ที่สร้างวันนี้จะ compatible ต่อไป

พร้อมกันนั้น **Enterprise-Managed Authorization extension เลื่อนขึ้น stable status** — เป็น auth model ที่ enterprise คุม access ทั้ง MCP server ผ่าน identity provider ของตัวเอง (Okta, Azure AD, Auth0 ฯลฯ), align กับ OAuth 2.1 + OIDC. **Anthropic, Microsoft, Okta** ประกาศรับ spec ตัวนี้ทันที และ MCP server กระแสหลักจะ migrate ตามใน Q3 2026

ตัวเลข adoption ที่ MCP ประกาศ: **78% ของ enterprise AI team มี MCP ใน production, 28% ของ Fortune 500 run MCP server ในบ้าน, 97 ล้าน SDK download/เดือน, 10,000+ active public MCP server**. เทียบกับสิ้นปี 2025 ที่ Fortune 500 adoption อยู่แค่ ~5% — 6 เดือนโตขึ้น 5 เท่า

## ทำไมสำคัญ
Stateless HTTP ฟังดูเทคนิค แต่ผลกระทบเชิงธุรกิจใหญ่มาก — MCP server ที่เดิมต้องใช้ **sticky session + shared session store + deep packet inspection ที่ gateway** ตอนนี้วางหลัง **plain round-robin load balancer** ได้ทันที, route traffic ตาม Mcp-Method header, client cache tools/list response ตาม ttlMs. ต้นทุน infra ของการ run remote MCP server ในองค์กรใหญ่จะ **drop 40-70%** (ประเมินจาก case จริงของ server ที่ Anthropic reference) — เพราะไม่ต้องซื้อ Redis cluster + sticky-session load balancer + custom session gateway อีกต่อไป

Pattern ที่เห็นสอดคล้องกับ trajectory ของ protocol ทั้งหลายในอุตสาหกรรมนี้ — เริ่มจาก stateful protocol ที่ implementor แต่ละคนคุมเอง, แล้วเมื่อ adoption ถึง critical mass, community push spec ขึ้น stateless เพื่อให้ scale ตาม cloud pattern ปัจจุบัน (HTTP/2, gRPC, Kafka รุ่นใหม่ ๆ ก็เดินสูตรนี้). **MCP ใช้เวลาแค่ 18 เดือน** จาก launch (พ.ย. 2024) ถึง enterprise-grade stateless spec — เร็วกว่า SOAP → REST หรือ REST → GraphQL หลายเท่า signal ว่า ecosystem push หนัก, ไม่ใช่ vendor เดียวลาก

Enterprise Auth GA คือ **piece สุดท้ายที่ CISO รอ** — ก่อนหน้านี้ MCP server ในองค์กรใหญ่ ๆ ต้องเขียน adapter เอง (Okta SCIM + custom claim + policy), CISO block adoption ทั้งเจ้าเพราะไม่มี audit trail. ตอนนี้ centralized IdP-based control เข้ามาแล้ว, admin ปิด/เปิด access ต่อ tool ต่อ role ต่อ user ได้จาก dashboard เดียว, log ทุก tool call ไป SIEM ปกติ. **การ block "adoption ถัดไป" ของ enterprise MCP หายไป**

Compare กับ trajectory ของ Kubernetes — spec ที่ vendor-neutral + open + rapid iteration ทำให้ทุก cloud + on-prem stack ต้อง commit. MCP อยู่ในช่วงเดียวกัน — **Google (A2A protocol), Salesforce (Agentforce API), OpenAI (Agents SDK), Microsoft (Foundry)** ต่างเชื่อม MCP เข้าใน SDK ของตัวเอง. ในไตรมาสถัดไปวัดจะเห็น **แทบทุก enterprise agent framework จะพูดภาษา MCP เป็น first-class** — cross-vendor tool calling จะเป็น table stakes

## มุม AI Agent Platform
**Builders** — framework/tool builder ที่ยัง require sticky session (LangChain built-in memory server, ตัว proprietary agent runtime ที่ผูก session state ใน memory) ต้อง migrate ในไตรมาสนี้ ไม่งั้นโดน bypass. Framework ที่มี **native MCP client + stateless-first design** (Anthropic Claude Agent SDK, OpenAI Agents SDK v2, Google ADK) มี tailwind สูงสุด. Vertical agent startup ที่ build เอง stack ตัวเองต้องเลิกและปรับตัวเข้า MCP — ไม่งั้นจะไม่มีทาง cross-sell ผ่าน Fortune 500 ที่คุ้นชิน MCP ecosystem

**Users/business ในไทย** — ธนาคาร/insurer/telecom ที่ CIO stuck กับคำถาม "MCP ปลอดภัยไหม" — Q3 นี้จะมีคำตอบชัดจาก Enterprise Auth extension + OIDC + centralized policy. SCB, KTC, KBank, AIS, DTAC ที่มี Okta/Azure AD deploy อยู่แล้ว activate integration ได้ทันทีในไตรมาสสิงหาคม-กันยายน (ตาม Anthropic/Microsoft roadmap). **RFP รอบต่อไป**: ถาม vendor ว่า MCP server ของพวกเขาผ่าน 2026-07-28 spec ไหม + support Enterprise Auth extension ไหม + audit log ส่งไป SIEM รูปแบบไหน ถ้าตอบไม่ได้ vendor นั้น 6 เดือนล้าสมัย

**Ecosystem** — MCP registry, MCP directory, MCP marketplace (a16z-backed) กำลังจะเป็น **layer ใหม่ที่มูลค่าสูงสุด** — เหมือน npm ของ agent tools. Startup ที่ยึด "tool distribution + governance + observability ของ MCP server" (Cloudflare enterprise MCP, Composio, Arcade) มี window 6-12 เดือนก่อนที่ hyperscaler จะ commoditize layer นี้

## Sources
- [The 2026-07-28 MCP Specification Release Candidate — Model Context Protocol Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
- [AI Model Context Protocol Adds Centralised Auth for Enterprise — InfoQ](https://www.infoq.com/news/2026/07/mcp-ema-enterprise-auth/)
- [MCP Goes Stateless: What the 2026-07-28 Spec Release Candidate Means for Your Servers — jsmanifest](https://jsmanifest.com/mcp-stateless-spec-2026-07-28)
- [MCP Adoption Statistics 2026: Model Context Protocol — Digital Applied](https://www.digitalapplied.com/blog/mcp-adoption-statistics-2026-model-context-protocol)

---

## Audio script
สัปดาห์นี้มีข่าวใหญ่ที่คนสร้าง AI agent ทุกคนควรรู้ Model Context Protocol หรือ MCP ปล่อย release candidate ของ spec รุ่น 2026-07-28 lock spec วันที่ 21 พฤษภาคม publish final วันที่ 28 กรกฎาคม เป็น revision ใหญ่สุดตั้งแต่ launch หัวใจคือ MCP กลายเป็น fully stateless บน HTTP ธรรมดา ยกเลิก initialize handshake และ session ID header request ไหนก็วิ่งไป server ตัวไหนก็ได้ ไม่ต้องมี sticky session หรือ shared store อีกแล้ว ต้นทุน infra ของ MCP server ในองค์กรใหญ่จะลดลง 40 ถึง 70 เปอร์เซ็นต์ พร้อมกันนั้น Enterprise Managed Authorization extension เลื่อนขึ้น stable status enterprise คุม access ผ่าน IdP ของตัวเองได้ ผ่าน OAuth และ OIDC Anthropic Microsoft Okta ประกาศรับ spec นี้ทันที ตัวเลข adoption ที่ MCP ประกาศ 78 เปอร์เซ็นต์ของ enterprise AI team มี MCP ใน production 28 เปอร์เซ็นต์ของ Fortune 500 run MCP server ในบ้าน SDK download 97 ล้านต่อเดือน public MCP server มากกว่า 10,000 ตัว 6 เดือนที่ผ่านมา Fortune 500 adoption โตจาก 5 เปอร์เซ็นต์เป็น 28 เปอร์เซ็นต์ 5 เท่า สำหรับธุรกิจไทยที่ CIO ยัง stuck กับคำถาม MCP ปลอดภัยไหม ไตรมาสสามนี้จะมีคำตอบชัดแล้ว ธนาคารและ telecom ที่มี Okta หรือ Azure AD อยู่แล้วเปิด integration ได้ทันที RFP รอบต่อไปให้ถาม vendor ตรง ๆ ว่า MCP server ของคุณผ่าน spec 2026-07-28 ไหม support Enterprise Auth extension ไหม audit log ส่งไป SIEM รูปแบบไหน ถ้าตอบไม่ได้ vendor นั้นตกยุคไปแล้ว 6 เดือน
