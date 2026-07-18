---
date: 2026-07-18
slug: mcp-stateless-enterprise-authorization-release-candidate
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  A vast server room where hundreds of identical MCP nodes sit behind
  a single humming round-robin load balancer labeled "STATELESS". Above
  the racks three glowing signs float in editorial isometric style:
  "1 SESSION STORE → 0", "STICKY SESSIONS → GONE", "OAUTH 2.1 + EMA".
  A tiny Anthropic-style geometric logo watermark in the corner.
  Deep navy and warm amber palette, sharp typography, 1:1 aspect,
  no real human faces, readable at 200px thumbnail.
image: images/26-07-18-0609-01-mcp-stateless-enterprise-authorization-release-candidate.png
---

# MCP 2.0 กำลังจะกลายเป็น "HTTP ของ agent" — 28 กรกฎาคมนี้

## TL;DR
- Anthropic + MCP working group ประกาศ Release Candidate ของ MCP spec 2026-07-28 — revision ใหญ่ที่สุดตั้งแต่ launch พ.ย. 2024
- Core กลายเป็น **stateless** — remote MCP server รันหลัง round-robin LB ธรรมดาได้ ไม่ต้อง sticky session, ไม่ต้อง shared session store
- **Enterprise-Managed Authorization (EMA)** ขึ้น stable แล้ว — Anthropic, Microsoft, Okta adopt, มี 7 MCP server รองรับ single enterprise login ผ่าน OAuth 2.1
- Final spec publish 28 ก.ค. 2026 — SDK maintainer มีเวลา 10 สัปดาห์ validate

## เกิดอะไรขึ้น
MCP working group โพสต์ release candidate ของ spec 2026-07-28 บน blog.modelcontextprotocol.io เมื่อกลางเดือนพฤษภาคม แล้วค่อย ๆ ทยอยดัน component ต่าง ๆ ให้ stable ตลอดสองเดือนหลัง — คลื่นสุดท้ายมาสรุปในเดือนกรกฎาคม ก่อน final spec ประกาศวันที่ 28. เนื้อหาที่เปลี่ยนแบ่งเป็นสามชั้น: (1) core protocol กลายเป็น stateless — request ทุก request แบก context ที่จำเป็นมาเอง, server ไม่ต้องจำอะไร; (2) authorization ปรับให้ align กับ OAuth 2.0 + OpenID Connect เต็มตัว, มี Enterprise-Managed Authorization extension ขึ้น stable แล้วเมื่อ 18 มิ.ย.; (3) สาม extension ใหม่ — MCP Apps (server-rendered UI), Tasks (long-running work), Server Cards (capability discovery ผ่าน .json file)

น้ำหนักของ stateless อยู่ตรงคำเดียว: "ordinary HTTP infrastructure." MCP รุ่นเดิมต้อง sticky session, shared session store, และ deep packet inspection ที่ gateway — เพราะ session state คือส่วนหนึ่งของ protocol. รุ่นใหม่บอกว่า route traffic ตาม `Mcp-Method` header ได้เลย, client cache tools/list ตาม `ttlMs` ที่ server กำหนด, load balancer เป็น commodity round-robin แบบที่ทีม infra ใช้กับ REST API ทั่วไป

Enterprise-Managed Authorization เป็นชิ้นที่ enterprise architect รอมานาน. เดิม MCP server แต่ละตัวมี OAuth flow ของตัวเอง — user ต้อง consent ทีละ server ทีละ tool. EMA รวมทุกอย่างไว้หลัง IdP กลาง (Okta, Entra, Ping) — admin กำหนดสิทธิ์ครั้งเดียว, user ล็อกอินครั้งเดียว, ทุก MCP server ที่รองรับ EMA จะเห็นสิทธิ์ตาม policy นั้นทันที. Anthropic + Microsoft + Okta ประกาศ adopt แล้ว, มี seven MCP server ที่ทำงานกับ EMA ได้ตั้งแต่วัน launch

## ทำไมสำคัญ
Stateless + enterprise auth คือสัญญาณว่า MCP กำลังข้ามเส้นจาก "protocol ของ hobbyist / research" ไปเป็น "middleware ของ enterprise." ในเดือนพฤศจิกายน 2024 ตอนที่ Anthropic เปิดตัว MCP, protocol นี้ถูกออกแบบเพื่อ local dev environment เป็นหลัก — Claude Desktop เชื่อมต่อ tool ผ่าน stdio, session ที่มี state ไม่ใช่ปัญหา. แต่พอปี 2026 MCP server จำนวนมากขึ้น host แบบ remote — Cloudflare, Vercel, AWS, Databricks ต่างเปิด managed MCP hosting — session state กลายเป็นคอขวด operational

ที่ SecurityWeek รายงาน: การถอด sticky session ออกลด attack surface อย่างมีนัย — attacker ไม่มี long-lived state ให้ hijack — แต่ก็เปิดช่องใหม่: server side ต้อง validate ทุก request เอง, ไม่มี "trust from previous request in same session." implementation quality กลายเป็นเรื่องคอขวด. แปลว่าอีก 12 เดือนข้างหน้าจะเห็น MCP security consultancy กับ auditing เกิดใหม่หลายเจ้า — เหมือนที่เกิดกับ Kubernetes ยุค 2018

เทียบกับ agent protocol อื่น: Google's A2A ยังเน้น orchestration ระหว่าง agent, ไม่ใช่ tool wiring; OpenAI's Agents SDK มี tool spec ของตัวเองที่ยังไม่ interoperable กับ MCP เต็ม 100%. การที่ MCP มี formal deprecation policy กับ 10-week validation window แสดงว่า Anthropic วางแผนให้มันเป็น "stable substrate" ที่ vendor คนอื่นจะพึ่งได้จริง — คล้ายกับ HTTP/1.1 ตอนกลายเป็น IETF standard

## มุม AI Agent Platform
**Builder** ของ MCP server ทุกเจ้าต้องอ่าน migration guide ให้จบ — โค้ดที่พึ่ง session state จะแตกหลัง 28 ก.ค. และ deprecation policy หมายความว่ามี timeline จริงที่ต้องปรับ. **Users / business** ที่ deploy internal MCP catalog จะได้ประโยชน์ทันที: infra bill ลด, ไม่ต้องรัน Redis สำหรับ session, ไม่ต้อง config sticky routing ที่ gateway. **Ecosystem** — cloud vendor ทุกเจ้า (AWS, GCP, Azure, Cloudflare) จะรีบเปิด "managed MCP host" ที่คิดเงินตาม request ไม่ใช่ตาม session — เพราะ economics ของ stateless workload ต่างจาก stateful. ทีมที่ทำ orchestration บน MCP (Enabridge, LangChain, Vercel AI SDK) น่าจะเห็น pattern เดียวกับที่ REST API เห็นเมื่อ 10 ปีก่อน — layer สูงขึ้นเริ่มมี opinion ต่อ retry, backoff, circuit breaker, observability — เพราะ transport กลายเป็น commodity แล้ว

## Sources
- [The 2026-07-28 MCP Specification Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
- [AI Model Context Protocol Adds Centralised Auth for Enterprise (InfoQ)](https://www.infoq.com/news/2026/07/mcp-ema-enterprise-auth/)
- [New Enterprise-Ready MCP Specification Brings New Security Challenges (SecurityWeek)](https://www.securityweek.com/new-enterprise-ready-mcp-specification-brings-new-security-challenges/)
- [MCP Goes Stateless: The 2026-07-28 Spec Explained](https://nerdleveltech.com/mcp-stateless-protocol-enterprise-authorization)
- [Why the Model Context Protocol Won (The New Stack)](https://thenewstack.io/why-the-model-context-protocol-won/)

---

## Audio script
วันที่ 28 กรกฎาคมนี้ MCP หรือ Model Context Protocol จะออก spec ใหม่ที่เป็นการเปลี่ยนโครงสร้างครั้งใหญ่ที่สุดตั้งแต่ตัว protocol เกิดมาเมื่อปลายปี 2024. Release candidate โผล่บน blog ทางการของ MCP working group แล้ว และเนื้อหาสำคัญมีสามชั้น. ชั้นแรกคือ core protocol กลายเป็น stateless เต็มตัว — remote MCP server รันหลัง round-robin load balancer ธรรมดาได้เลย ไม่ต้อง sticky session ไม่ต้องมี shared session store ทำให้ทีม infra scale MCP server เหมือน scale REST API ทั่วไป. ชั้นที่สองคือ Enterprise-Managed Authorization หรือ EMA extension ขึ้น stable แล้ว — Anthropic, Microsoft, Okta ประกาศ adopt, มี MCP server เจ็ดตัวรองรับ single enterprise login ตั้งแต่วัน launch. ชั้นที่สามคือ extension ใหม่สามตัว: MCP Apps สำหรับ server-rendered UI, Tasks สำหรับงาน long-running, และ Server Cards สำหรับ capability discovery. ความหมายกว้าง ๆ คือ MCP กำลังข้ามเส้นจาก protocol ของ hobbyist กับ research ไปเป็น middleware ของ enterprise จริง ๆ. Cloud vendor ทุกเจ้าน่าจะรีบออก managed MCP host, ทีมที่ทำ orchestration ชั้นบนน่าจะขยับไปเน้น retry, observability กับ policy — เพราะชั้น transport กลายเป็น commodity แล้ว. สำหรับทีมที่มี MCP server ของตัวเอง — โค้ดที่พึ่ง session state จะแตกหลัง 28 กรกฎาคม ควรอ่าน migration guide ให้จบก่อน
