---
date: 2026-08-08
slug: mcp-stateless-spec-largest-revision
topic: agentic-ai
reading_time_min: 3
sources: 4
image_prompt: |
  A giant "MCP" glass panel splits open in the center of a data-center hallway;
  from the left side an old cable labeled "SESSION-ID" gets unplugged and falls,
  while on the right dozens of glowing packet arrows fan out to identical HTTP
  load-balancer boxes. Bold headline text overlay reads "STATELESS: 97M
  DOWNLOADS/MO" and "SEP-2575 REMOVED". Editorial isometric style, deep navy
  background with teal + amber accents, 1:1 aspect, no real human faces.
image: images/26-08-09-0613-01-mcp-stateless-spec-largest-revision.png
---

# MCP โยนทิ้ง "session" ทั้งหมด — spec เดือน ก.ค. เปลี่ยน landscape ของ AI Agent Platform

## TL;DR
- Model Context Protocol (MCP) spec version `2026-07-28` ตัด initialize handshake (SEP-2575) และ Mcp-Session-Id header (SEP-2567) ออกทั้งหมด — ทุก request เป็น self-describing และ independent
- MCP ทะลุ 97 ล้าน download ต่อเดือน (Python + TS combined) — ถูกใช้โดย Anthropic, OpenAI, Google, Microsoft, Amazon และตอนนี้ governed โดย Linux Foundation's Agentic AI Foundation
- Impact ทันที: agent server scale แบบ round-robin load balancer ธรรมดาได้เลย, ไม่ต้อง session affinity, cost infra ลด, ทำ multi-region ง่ายขึ้น

## เกิดอะไรขึ้น
เมื่อ 28 กรกฎาคม MCP maintainers ปล่อย spec revision ที่เรียกได้ว่าใหญ่ที่สุดตั้งแต่ protocol เปิดตัว — และเป็น breaking change แบบเปลือย. Session ที่เคยเป็น first-class concept ในระดับ transport ถูกลบทิ้ง. `initialize` / `initialized` handshake หายไป. Logical header `Mcp-Session-Id` หายไป. แทนที่จะเจรจากันครั้งเดียวตอนต่อ connection แล้วจำ context ไว้ใน server, ตอนนี้ทุก request ต้องแบก protocol version, client info, และ capabilities ไว้ใน `_meta` field ของ payload ทุกครั้ง.

ผลข้างเคียงคือ MCP server ตอนนี้เดินตามลุคของ REST API ปกติ — และนั่นคือความตั้งใจ. Google Developers Blog เขียนว่า "the stateless core removes the need for session affinity, which simplifies horizontal scaling and load balancing. Any server instance can serve any request behind a plain round-robin load balancer." Server ที่ยังต้อง keep state (shopping cart, browser session, long-running job) ต้องเปลี่ยน pattern: mint explicit handle เช่น `basket_id` หรือ `browser_id` แล้วให้ model ส่งกลับมาเป็น argument ธรรมดา — ไม่ใช้ protocol-level session อีกต่อไป.

เวลาที่ประกาศออกมาไม่ได้บังเอิญ. MCP ตอนนี้แตะ 97 ล้าน SDK download ต่อเดือน (Python + TypeScript รวมกัน) และถูก adopt โดย Anthropic, OpenAI, Google, Microsoft, Amazon เป็น standard. Governance ก็ย้ายเข้า Linux Foundation's Agentic AI Foundation (AAIF) ที่ co-founded โดย OpenAI, Anthropic, Google, Microsoft, AWS และ Block. Spec ก่อนหน้าที่ built สำหรับ prototype era — long-lived stateful connection กับ dev laptop — เริ่มเป็น bottleneck ตอน enterprise ต้อง scale MCP server หลายพัน replica ในหลาย region.

## ทำไมสำคัญ
Pattern ที่ MCP กำลังตาม คือ pattern เดียวกับที่ HTTP ทำสำเร็จเมื่อ 30 ปีก่อน — และเดียวกับที่ REST เอาชนะ SOAP: "ทำ protocol ให้โง่ที่สุดในระดับ transport, ให้ application เป็นคนถือ state." เมื่อ session หายไปจาก wire ทุก MCP server สามารถ deploy เป็น serverless function, edge worker, หรือ auto-scaled container fleet โดยไม่ต้องแคร์ sticky routing. cost infra ลดทันที เพราะไม่ต้อง maintain in-memory session store หรือ Redis replication ที่แชร์ระหว่าง replica.

Signal ที่น่าจับตาคือ AAIF ที่ตั้งขึ้นเมื่อครึ่งปีที่แล้วเริ่มมี teeth. Spec release นี้ผ่าน RFC public 30 วัน มี working group vote, deprecation policy formal — ไม่ใช่ Anthropic ตัดสินใจเอง. MCP กำลังเดิน path เดียวกับ Kubernetes หลังย้ายไป CNCF: จาก single-vendor project กลายเป็น industry standard ที่ทุกคน trust พอจะ build บนได้. คนที่ยังเขียน agent framework ของตัวเองแบบ proprietary tool protocol เริ่มมี switching cost สูงขึ้นเรื่อย ๆ.

## มุม AI Agent Platform
สำหรับ **builders** ที่กำลังทำ MCP server: ต้อง audit code ทุกจุดที่พึ่ง session — replace ด้วย explicit handle pattern. Server ที่ compliant กับ spec ใหม่จะ deploy ถูกกว่ามาก และรัน managed service (Cloudflare, Google Cloud Run, Vercel) ได้แบบ pay-per-request จริง ๆ. สำหรับ **enterprise ที่ deploy agent**: MCP server ที่ compliant กับ spec ใหม่แปลว่า vendor lock-in ลด — สามารถย้ายจาก single VM ไป autoscale fleet ได้โดยไม่แตะ code. Governance layer เช่น Hush Security (ดูข่าวอื่นในรอบนี้), Auth0 for AI Agents, MCP Gateway ต่าง ๆ ก็จะเสียบเข้ากับ standard header pattern ได้ตรง ๆ. สำหรับ **ecosystem**: นี่คือ moment ที่ MCP เลิกเป็น "Anthropic's protocol" แล้วกลายเป็น "the protocol" — competitor protocol อย่าง ACP หรือ vendor-specific tool interface มี window เหลือน้อยลงเรื่อย ๆ.

## Sources
- [The 2026-07-28 Specification | Model Context Protocol Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [Scaling AI Agent Infrastructure with the MCP Stateless updates | Google Developers Blog](https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/)
- [2026-07-28 MCP: stateless, multi-round-trip, routable headers, authorization hardening | 4sysops](https://4sysops.com/archives/2026-07-28-model-context-protocol-mcp-stateless-multi-round-trip-routable-headers-authorization-hardening/)
- [MCP Grows Up: What the July 28 Spec Means for Every Enterprise Agent Deployment | Trilogy AI](https://trilogyai.substack.com/p/mcp-grows-up-what-the-july-28-spec)

---

## Audio script
สวัสดีครับ วันนี้เรื่องแรกเป็นข่าวใหญ่ของฝั่ง protocol. Model Context Protocol หรือ MCP ที่เป็น standard เชื่อม LLM กับ tool ปล่อย spec ใหม่วันที่ยี่สิบแปดกรกฎา — และเป็นการเปลี่ยนที่ใหญ่ที่สุดตั้งแต่เปิดตัว. เขาตัด session ทิ้งทั้งหมด. เมื่อก่อนต่อ MCP server ต้อง handshake หนึ่งครั้ง แล้ว server จำ session ID ไว้. ตอนนี้ไม่มีแล้ว. ทุก request แบก context ไปเองในทุกครั้ง เหมือน REST API ธรรมดา. ทำไมสำคัญ? เพราะตอนนี้ MCP มีคน download เก้าสิบเจ็ดล้านครั้งต่อเดือน ใช้กันตั้งแต่ Anthropic OpenAI Google ยัน Microsoft — spec เก่าที่ออกแบบสำหรับ dev laptop มัน scale ไม่ไหว. Spec ใหม่ทำให้ MCP server รันเป็น serverless function ได้ทันที ไม่ต้อง sticky session ไม่ต้อง Redis กลาง cost infra ลดฮวบ. Signal ที่สำคัญคือ MCP ตอนนี้ไม่ใช่ของ Anthropic คนเดียวแล้ว — governance ย้ายไปอยู่ Linux Foundation ที่ OpenAI Google Anthropic AWS ร่วมกันตั้ง. เหมือน Kubernetes ที่เคยเป็นของ Google แล้วกลายเป็น standard ของโลก. ใครที่ทำ agent framework proprietary เอง — window ในการเป็น standard เริ่มหมดแล้วครับ. เจอกันเรื่องต่อไป.
