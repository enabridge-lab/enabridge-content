---
date: 2026-07-13
slug: mcp-2026-07-28-stateless-enterprise-auth-spec
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric hero illustration of a giant server rack labeled
  "MCP 2026-07-28" glowing on a dark technical plane, with three big glowing
  tags in front: "STATELESS CORE", "OAUTH 2.1 + OIDC", and "ENTERPRISE
  AUTH". Behind the rack, a wall of session-state boxes are visibly being
  smashed and disappearing into pixels; a diagonal countdown banner across
  the top reads "SHIPS JULY 28". Silhouettes of tiny developers stand
  looking up at the rack. High-contrast cinematic teal-and-orange palette,
  bold labels readable at 200px thumbnail, 1:1 aspect, no real human faces.
image: images/26-07-13-0608-01-mcp-2026-07-28-stateless-enterprise-auth-spec.png
---

# MCP 2026-07-28 คือ reboot ครั้งใหญ่ที่สุดของ protocol — stateless core, OAuth 2.1, enterprise auth เป็น stable และ ship ใน 16 วัน

## TL;DR
- Model Context Protocol ปล่อย release candidate สำหรับ **spec version 2026-07-28** — Anthropic เรียกว่า "the largest revision since launch" ยิง **stateless core, OAuth 2.1 alignment, และ Enterprise-Managed Authorization** เป็น stable, ship 28 กรกฎาคม พร้อม **12-month deprecation window** สำหรับ legacy
- Server ที่เขียนขึ้นในปี 2025 ทั้งหมดต้อง migrate — session state หายไป, tools/list cacheable ผ่าน `ttlMs`, `Mcp-Method` header route ได้เลย. audience นี้ต้องรู้ว่า **six breaking changes** ทำให้ production server อาจแตกถ้าไม่แตะ code ก่อนสิ้นเดือน
- Auth ทำ enterprise-ready จริง: token replay ข้าม server ทำไม่ได้ (protocol-level enforcement), `iss` validation ตาม RFC 9207, EMA extension ให้ IdP กลาง control access — MCP เพิ่งเปลี่ยนจาก dev toy เป็น protocol ที่ CIO เซ็นได้

## เกิดอะไรขึ้น
Model Context Protocol เกิดเมื่อ Anthropic ประกาศครั้งแรกในปลายปี 2024 — เป็น open standard ให้ agent เชื่อม tool กับ data source ได้แบบ vendor-neutral. หนึ่งปีครึ่งต่อมา MCP กลายเป็นค่าเริ่มต้นของ agent ecosystem: Microsoft ใส่ 60+ ready servers ไว้ใน Copilot Studio + Azure AI Foundry, Cloudflare ทำ MCP reference architecture, OpenAI เพิ่ม MCP connectors ให้ ChatGPT enterprise, Google Cloud ทำ managed MCP servers. ตัวเลขที่ industry อ้างอิงกันคือ **78% ของ enterprise AI team รัน MCP-backed agents ใน production, 28% ของ Fortune 500 รัน MCP server ของตัวเอง, monthly SDK downloads ~97 ล้าน** — ผ่าน critical mass ไปแล้ว

แต่ spec version เก่ายังพก session state, in-memory client state, และ auth pattern ที่ไม่ใช่ enterprise-grade — สาย security team เอาไปเซ็นยาก. release candidate 2026-07-28 (lock ตั้งแต่ 25 พ.ย. 2025) จึงเป็น reboot ที่ทีม MCP รอ: **stateless core** ให้ remote MCP server รันหลัง plain round-robin load balancer ได้เลย, route traffic ผ่าน `Mcp-Method` header, client cache `tools/list` response ตาม `ttlMs` ที่ server กำหนด — model เดียวกับ HTTP ที่ scale ได้ตาม infra เดิม ไม่ต้องพก sticky session

เรื่อง auth เปลี่ยนใหญ่กว่านั้นอีก: spec ใหม่ align กับ **OAuth 2.1 + OpenID Connect** โดย token ที่ client ขอสำหรับ MCP server หนึ่ง **ไม่สามารถ replay ไปยัง server อื่นได้** — enforce ที่ protocol level ไม่ใช่ที่ implementer เลือกทำหรือไม่ทำ. Client ต้อง validate `iss` parameter ตาม RFC 9207 เพื่อกัน mix-up attack, และ Dynamic Client Registration ต้องประกาศ `application_type` แบบ OIDC. **Enterprise-Managed Authorization (EMA) extension** ที่เคย experimental ตอนนี้ promote เป็น stable — ให้ CIO route ทุก MCP access ผ่าน identity provider กลาง (Okta, Entra ID, Ping) พร้อม RBAC + audit log ในตัว. ที่ปวดหัวคือ MCP ก็เปิด **extensions framework** ใหม่ใช้ reverse-DNS identifier — extension แต่ละตัวมี repo, maintainer, versioning ของตัวเอง independent จาก core spec เลย

## ทำไมสำคัญ
เรื่องนี้เป็น pattern ที่ Enabridge tracking มาหลายเดือน — **protocol layer commoditize เร็วกว่าที่คิด แต่ enterprise adoption ยัง gate ที่ security stack**. spec เก่าทำ POC พอไหว แต่พอ CISO เข้าห้องประชุมแล้วถาม "token replay ป้องกันยังไง, session state ไป audit ที่ไหน, ถ้า MCP server compromise จะ blast radius แค่ไหน" — คำตอบเมื่อปีที่แล้วคือ "ต้องทำ layer เพิ่มเอง". พอ 2026-07-28 ผลัก 6 breaking change ทั้งหมดเข้า core spec แล้ว MCP เพิ่งข้าม threshold ที่จะเข้าไปใน **security review + procurement pipeline** ของ enterprise แบบไม่ต้อง carve-out. นี่คือช่วงเวลาเดียวกับที่ HTTPS ceased-being-optional สำหรับ web ในราวปี 2016

ประเด็นเชิงตลาดคือ **12-month deprecation window** เป็น gift ให้ vendor ที่พร้อม migrate — และเป็น pressure ต่อทุกคนที่ยังไม่เริ่ม. Cloudflare, Microsoft, และ Anthropic น่าจะรีบ ship SDK beta ให้ตรง 28 ก.ค. เพื่อโชว์ leadership. ส่วน team ที่รัน MCP server ใน production วันนี้แล้ว next 16 วันจะเป็นเดือนที่ต้องเลือกอย่างจริงจังว่าจะ migrate ทันหรือ freeze roadmap ไว้รอ. ถ้ามอง 5 ปีข้างหน้า — protocol ที่มี **stateless HTTP + OAuth 2.1 + IdP-centralized auth** คือ protocol ที่ CIO ยอมเปิด outbound traffic ให้ ซึ่งแปลว่า agent-to-tool integration cost จะลดลงเป็นระดับ magnitude

## มุม AI Agent Platform
สำหรับ **builders**: ถ้ารัน MCP server อยู่แล้ว — จัดสรร sprint หน้าให้ migration เลย. session state ต้อง externalize (Redis, DynamoDB) ไม่งั้น scale ไม่ได้ตาม spec ใหม่. tools/list ต้อง idempotent + return `ttlMs`. auth flow ต้องรองรับ EMA + IdP integration ตั้งแต่แรก ไม่ใช่ retrofit. builder ที่ทำ MCP-first framework (Anthropic Claude Agent SDK, LangChain, LlamaIndex) มี edge ตรงที่ SDK จะออก beta พร้อม spec ให้เลย — คนที่ hand-roll server จะ lag. สำหรับ **users/business**: ถามทีม security ก่อนอนุมัติ MCP-based integration ใหม่ว่า vendor migrate ไป 2026-07-28 spec หรือยัง — ถ้ายัง อย่าเซ็น procurement 2 ปี. Enterprise ที่ standardize MCP + EMA แล้ว จะเห็น agent-to-tool integration cost ลดลงจริง เพราะ IdP กลางเอาไปดูแลได้ทีเดียว. สำหรับ **ecosystem**: gateway vendor (Citrix, Nutanix, Kong, Salt Security) และ IdP (Okta, Entra, Ping) เพิ่ง get **protocol-level moat** ให้ปกป้อง — ต่อจากนี้ enterprise MCP traffic ที่ไม่ผ่าน gateway + IdP อย่างเป็นทางการจะดูเป็น anomaly. อีกฝั่งคือ MCP registry / marketplace (Anthropic MCP registry, Smithery, Mintlify) จะกลายเป็น critical infrastructure เพราะ extension framework จะ produce library ที่แยกจาก core spec เร็วมาก

## Sources
- [The 2026-07-28 MCP Specification Release Candidate — Model Context Protocol Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
- [The biggest MCP spec update ships July 28: What changes for AI agent authentication — WorkOS](https://workos.com/blog/mcp-2026-spec-agent-authentication)
- [MCP 2026-07-28: Stateless core, enterprise authorization, and SDK betas — Médéric Hurier, Medium](https://fmind.medium.com/mcp-2026-07-28-stateless-core-enterprise-authorization-and-sdk-betas-2646a980d594)
- [AI Model Context Protocol Adds Centralised Auth for Enterprise — InfoQ](https://www.infoq.com/news/2026/07/mcp-ema-enterprise-auth/)

---

## Audio script
Model Context Protocol กำลังจะ ship spec version ใหม่ วันที่ 28 กรกฎาคมนี้ ทีม Anthropic บอกเองว่านี่คือ revision ที่ใหญ่ที่สุดตั้งแต่เปิดตัว protocol มา สาระหลักมีสามเรื่อง หนึ่ง protocol เปลี่ยนเป็น stateless — server ไม่ต้องเก็บ session state อีกต่อไป client cache tools list ได้ตาม TTL ที่ server กำหนด รัน remote MCP server หลัง round-robin load balancer ธรรมดาได้เลย สอง auth เปลี่ยนใหญ่ — align กับ OAuth 2.1 กับ OpenID Connect โดย token ที่ขอสำหรับ server หนึ่ง เอาไป replay กับ server อื่นไม่ได้ enforce ที่ protocol level และ Enterprise Managed Authorization extension เพิ่งขึ้น stable ให้ CIO route MCP access ผ่าน identity provider กลางได้ สาม เปิด extensions framework แบบ reverse DNS identifier แยก repo แยก maintainer จาก core spec

เหตุผลที่เรื่องนี้สำคัญคือ MCP ผ่าน critical mass ไปแล้ว 78 percent ของ enterprise AI team รัน MCP agent ใน production 28 percent ของ Fortune 500 รัน server เอง SDK download 97 ล้านต่อเดือน แต่ spec เก่ายังไม่ผ่าน security review ของ CISO เพราะ session state กับ auth ไม่ครบ 2026 dash 07 dash 28 คือ threshold ที่ MCP ข้ามจาก dev toy เป็น protocol ที่ CIO เซ็นได้

สำหรับ builder ที่รัน MCP อยู่ ต้องจัดสรร sprint หน้าให้ migration session state ต้อง externalize tools list ต้อง idempotent auth flow ต้องรองรับ Enterprise Managed Authorization ถ้าเป็น enterprise ที่ใช้ agent อยู่ ให้ถาม vendor ว่า migrate ไป spec ใหม่หรือยังก่อนเซ็น procurement รอบต่อไป และสำหรับ ecosystem gateway vendor กับ identity provider เพิ่ง get moat จาก protocol โดยตรง — ต่อจากนี้ enterprise MCP traffic ที่ไม่ผ่านสองชั้นนี้จะดูเป็น anomaly ทันที
