---
date: 2026-06-30
slug: mcp-2026-07-28-stateless-release-candidate
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  An editorial isometric illustration of a vast horizontal MCP server fleet —
  rows of identical glowing cubes labeled "MCP" floating in a clean grid, each
  cube identical with no session-state markers. Above them a clean HTTP request
  arrow with header labels "Mcp-Method" and "Mcp-Name" flying through, landing
  on any cube. An old red "SESSION-ID" tag is dramatically crossed out with a
  large X in the foreground. Floating headline reads "MCP 2026-07-28
  STATELESS" with stacked numbers "97M SDK DOWNLOADS/MO" and "9,400 PUBLIC
  SERVERS" and "JULY 28 GA". Modern editorial palette of dark navy + electric
  cyan + warning red strikethrough, ultra-sharp text rendering for 200px
  thumbnail readability, 1:1 aspect ratio, tech-magazine cover style, no real
  human faces.
image: images/26-06-30-1714-04-mcp-2026-07-28-stateless-release-candidate.png
---

# MCP 2026-07-28 ตัด session ออกทั้งหมด — ปลด constraint ใหญ่สุดของ horizontal scaling, เปิดทาง agent fleet ระดับ enterprise

## TL;DR
- 21 พ.ค. — MCP steering committee lock release candidate **2026-07-28**, finalize 28 ก.ค. — เป็น **largest revision since launch**; โครงสร้างหลักของ MCP **เปลี่ยนเป็น stateless ที่ protocol layer ทั้งหมด**: Mcp-Session-Id header หาย, protocol-level session หายตาม
- เพิ่ม **Tasks extension** สำหรับ long-running work, **MCP Apps** สำหรับ server-rendered UI, และ **OAuth-aligned authorization**; รวมเป็น 4 changes ที่ปลด constraint enterprise scaling ที่ติดมาตั้งแต่ MCP 1.0
- มาในจังหวะที่ MCP ครอง: **97M SDK downloads/เดือน**, **9,400+ public servers**, native support ทุก major lab — และ Anthropic เพิ่งเปิด MCP Tunnels (พ.ค.) ทำให้ MCP เข้า enterprise infra เต็มตัว

## เกิดอะไรขึ้น

21 พฤษภาคม 2026 — MCP steering committee (Anthropic + Microsoft + GitHub maintainer team) lock specification **2026-07-28** เป็น release candidate. เป็นการ commit รายการ change ที่ใหญ่ที่สุดตั้งแต่ MCP เปิดตัวปลาย 2024 — และ ten-week validation window (จนถึง 28 ก.ค. ที่ finalize) คือเวลาให้ SDK maintainer ของ Anthropic Python/TypeScript + Microsoft .NET + third-party (Mintlify, WorkOS, others) สร้าง compliance implementation ก่อน GA

หัวใจของการเปลี่ยน — **stateless ที่ protocol layer**. ใน MCP 1.x (versions 2024-11, 2025-03, 2025-09) มี **Mcp-Session-Id** header + protocol-level session — server ต้องจำ state ของแต่ละ client session, ใช้ session ID เป็น routing key, ต้องมี sticky load balancing + shared session store ใน horizontal deployment. ใน 2026-07-28 — header นี้และ session ทั้งโครงสร้าง **ถูกลบออกทั้งหมด**. Request ทุกประเภท (tools/call, prompts/list, resources/read) สามารถ land ที่ server instance ไหนก็ได้. Protocol version + client info + capabilities ติดมากับ request ผ่าน HTTP header ตามมาตรฐาน (Mcp-Method, Mcp-Name) — เป็น "ordinary HTTP" ที่ load balancer และ infrastructure middleware ของลูกค้า route ได้โดยไม่ต้อง inspect body

ที่เพิ่มเข้ามาคู่กัน — **Tasks extension** ช่วยแก้คำถามใหญ่ที่เกิดจาก stateless: "แล้ว long-running work ทำยังไง?". Tasks extension ให้ server return task ID, client poll หรือ subscribe stream, สามารถ resume + cancel ระหว่าง instance ได้ — pattern เดียวกับ Kubernetes job + AWS Step Function. **MCP Apps** เพิ่ม spec สำหรับ server-rendered UI component ที่ client (เช่น Claude Desktop, Cursor, VS Code MCP client) render ใน chat — เปิด vendor-agnostic UI pattern แทน custom widget ทุกครั้ง. **OAuth-aligned authorization** เปลี่ยน auth flow ให้ align กับ RFC 8693 + RFC 9068 (token exchange + JWT access token) — เปิด federated identity จาก Okta/Auth0/Entra ID มาใช้ตรง

ตลาด context — MCP โต explosive ในรอบ 18 เดือน. ตัวเลขที่ MCP Steering พูดถึงรอบ Code with Claude เมื่อ พ.ค.: **SDK downloads ~97 ล้านครั้ง/เดือน**, **public MCP server > 9,400** (ที่ register กับ MCP directory + GitHub topic), **native client support: Anthropic Claude, OpenAI ChatGPT, Google Gemini, Microsoft Copilot, GitHub Copilot, Cursor, Windsurf**. คือ MCP เข้าสถานะ de facto standard แล้ว — เพิ่มจังหวะการเข้า enterprise infra layer ผ่าน MCP Tunnels (Anthropic), MCP Gateway (Microsoft), MCP-as-a-Service offering ของ Cloudflare/Cloudflare Workers ที่ scale ขึ้น

## ทำไมสำคัญ

**Stateless transition ปลด moat ของ horizontal-scaling vendor**. ก่อนหน้านี้ enterprise ที่ deploy MCP server fleet (เช่น KBank ที่ wrap internal API เป็น MCP server, hospital ที่ wrap HIS) ต้อง build sticky load balancing + Redis session store + custom routing logic. นั่นเป็น barrier ที่ทำให้ตลาด "managed MCP hosting" (Cloudflare MCP Workers, Vercel MCP runtime, Modal MCP function) ขายได้. ตอนนี้ — MCP request เป็น **plain HTTP** ที่ทุก load balancer + service mesh (NGINX, Envoy, Istio) route ได้. Stateless = vanilla autoscaling = ต้นทุน operate ลด 60-80% สำหรับ deployment ใหญ่ ๆ

POV ที่อาจ contrarian — **MCP Apps คือชิ้นที่จะเปลี่ยน UX paradigm มากที่สุด แต่คนพูดถึงน้อยกว่า**. ใน MCP 1.x ลูกค้าที่อยาก embed UI component (chart, form, interactive widget) ใน Claude Desktop / ChatGPT ต้อง custom integration ของแต่ละ client. MCP Apps spec บอก server return **declarative UI tree** ที่ MCP client render เหมือนกันได้ทุก vendor — pattern คล้าย Apple App Clips + Slack Block Kit + Microsoft Adaptive Cards รวมกัน. ใน 6-12 เดือน — MCP server ที่ build "interactive view" ของตัวเอง (เช่น KBank แสดง balance + transactions + buttons "เพิ่ม recurring payment") จะ embed ใน Claude, ChatGPT, Cursor, VS Code ได้พร้อมกัน — โดย vendor ไม่ต้อง custom UI ใหม่ทุกครั้ง

Implication ของ OAuth alignment — **enterprise procurement จะรับ MCP ได้กว้างกว่าเดิม 3-5 เท่า**. ใน MCP 1.x security model เน้น API key + bearer token ที่ enterprise IT ไม่ไว้ใจ. ตอนนี้ federation ผ่าน Entra ID / Okta / Auth0 ทำให้ IAM policy ที่ enterprise มีอยู่ apply กับ MCP ได้ตรง — admin granular control "user A เข้า MCP server X ได้ แต่ tool Y ใน server X เข้าไม่ได้". นี่คือ piece สุดท้ายของ "enterprise-grade MCP" ที่ Tier-1 ลูกค้าต้องการ. คาดว่าจะเห็น MCP server adoption ใน Fortune 500 เพิ่มเร็วกว่าครึ่งหลัง 2026 มาก

Pattern ที่ใหญ่กว่า — **ระบบ AI agent เริ่มมี maturity ของ web stack ปี 2007-2010**. HTTP 1.1 + RESTful + OAuth 2.0 + JSON Schema + horizontal scaling เป็นชั้นที่ web stack ใช้เวลา 10 ปีกว่าจะตกผลึก. MCP กำลังตกผลึกชั้นเดียวกันใน 18 เดือน. คนที่อยู่ early มี window สั้น — และคนที่อยู่ Tier 1 SDK maintainer (Anthropic, Microsoft) มี structural advantage เพราะ shape spec ก่อน

## มุม AI Agent Platform

Direct สำหรับ **agent platform builders**: ต้อง upgrade MCP runtime เป็น 2026-07-28-compatible ภายใน Q3 — ก่อน Tier-1 enterprise ถาม "support spec ใหม่แล้วยัง?". Roadmap ที่ทุก platform ควรทำ:

- (1) Upgrade SDK ทั้งหมด (Python + TypeScript + Go + Rust) เป็น 2026-07-28-compatible ภายในสัปดาห์ที่ spec finalize
- (2) Implement **Tasks extension** เป็น first-class — เป็น differentiator สำหรับ long-running agent workload (เช่น "agent ใช้เวลา 15 นาที reconcile statement, user disconnect แล้ว resume ได้")
- (3) Build **MCP Apps** preview แบบ vendor-agnostic ภายใน Q4 — ก่อน Cloudflare/Vercel/Mintlify ยึดตลาด UI sandbox layer
- (4) Federated auth ผ่าน Entra ID / Okta / Auth0 — ปลด enterprise procurement gate

ฝั่ง **business** ที่กำลังจะ wrap internal API (core banking, EHR/HIS, claims processing, government API) เป็น MCP server — window เปิดกว้างแล้ว. Stateless transition ลด deployment complexity ของ MCP server fleet ลง 5-10 เท่า. ระดับ regional — platform ที่ build local MCP runtime + library wrap local API (Thai national ID, PromptPay, bank Open API, government API) + Thai-language metadata จะอยู่ตำแหน่งดีก่อน global vendor (Cloudflare, Vercel) ลงมาแข่ง. นี่คือ playbook ที่ทำซ้ำได้ใน Indonesia, Vietnam, Philippines, ทั่ว ASEAN

## Sources
- [The 2026-07-28 MCP Specification Release Candidate — MCP Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
- [Why MCP 2026-07-28 Spec Drops Sessions and Goes Stateless — DEV](https://dev.to/rabinarayanpatra/why-mcp-2026-07-28-spec-drops-sessions-and-goes-stateless-1gd)
- [New Enterprise-Ready MCP Specification Brings New Security Challenges — SecurityWeek](https://www.securityweek.com/new-enterprise-ready-mcp-specification-brings-new-security-challenges/)
- [The biggest MCP spec update ships July 28 — WorkOS](https://workos.com/blog/mcp-2026-spec-agent-authentication)
- [MCP Goes Stateless: What the 2026 Release Candidate Means — MCP Playground](https://mcpplaygroundonline.com/blog/mcp-stateless-2026-release-candidate)

---

## Audio script

เมื่อยี่สิบเอ็ดพฤษภาคม MCP steering committee lock release candidate ของ specification ใหม่ 2026-07-28 — ใหญ่ที่สุดตั้งแต่ MCP เปิดตัวปลายปี 2024. Change หลักคือ MCP กลายเป็น stateless ที่ protocol layer ทั้งหมด. Mcp-Session-Id header หาย, protocol session หายตาม. Request ทุกประเภทสามารถ land ที่ server instance ไหนก็ได้.

ที่เพิ่มมาคู่กัน — Tasks extension สำหรับ long-running work, MCP Apps สำหรับ server-rendered UI ที่ client ทุกตัว render ได้, และ OAuth-aligned authorization ผ่าน token exchange มาตรฐาน. ทั้งสี่ change ปลด constraint ที่ enterprise ต้องการมาตั้งแต่ MCP 1.0.

ตลาด context — MCP ครองแล้ว. SDK downloads ประมาณเก้าสิบเจ็ดล้านครั้งต่อเดือน, public MCP server เก้าพันสี่ร้อย, native support ในทุก major client. การเปลี่ยน spec ครั้งนี้คือ moment ที่ MCP เข้าสู่ enterprise maturity เต็มตัว — เหมือน HTTP/1.1 ที่ใช้เวลาสิบปีตกผลึก แต่ MCP ทำได้ในสิบแปดเดือน.

มุม AI Agent platform — ทุก platform ต้อง upgrade runtime เป็น 2026-07-28-compatible ภายใน Q3, build Tasks extension เป็น differentiator สำหรับ long-running workflow, และคิดเรื่อง MCP Apps แบบ vendor-agnostic. ก่อน Cloudflare และ Vercel ยึดตลาดนี้.
