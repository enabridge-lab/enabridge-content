---
date: 2026-08-15
slug: mcp-stateless-2026-07-28-enterprise-eu-ai-act
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a switchboard operator room being torn
  down; on the left an old panel labeled "STATEFUL SESSIONS" collapses into
  rubble; on the right a modern Kubernetes cluster with three glowing pods
  labeled "MCP POD 1", "MCP POD 2", "MCP POD 3" and a round-robin load
  balancer routing arrows to each. A red EU flag banner across top reads
  "EU AI ACT AUG 2 ENFORCED". Thick outlines, high contrast, 1:1 aspect,
  no real human faces, editorial magazine style, readable at 200px thumbnail.
image: images/26-08-15-0614-04-mcp-stateless-2026-07-28-enterprise-eu-ai-act.png
---

# MCP 2026-07-28 ปล่อย stateless spec — server รันหลัง load balancer ธรรมดาได้, EU AI Act high-risk บังคับใช้ 2 ส.ค. ครอบ MCP gateway

## TL;DR
- **MCP spec version 2026-07-28** เปิดตัว architecture ใหม่แบบ **stateless** — server รันหลัง **round-robin load balancer + Kubernetes ปกติได้** ไม่ต้องมี sticky session หรือ shared session store
- เพิ่ม **RFC 9207 (Issuer Verification) + RFC 8707 (Resource Indicators)** = ระดับ auth ที่ enterprise identity team ยอมรับได้ พร้อม **Specification Feature Lifecycle + Deprecation Policy**
- **EU AI Act high-risk obligations บังคับใช้ 2 ส.ค. 2026** — MCP gateway ที่ใช้กับ regulated data (finance, healthcare, HR, education) เข้าข่ายทันที = compliance clock เริ่มเดินแล้ว

## เกิดอะไรขึ้น
เมื่อวันที่ 28 กรกฎาคม MCP working group ปล่อย **spec version 2026-07-28** ที่เป็น architectural rewrite ที่ใหญ่ที่สุดตั้งแต่ launch เมื่อพฤศจิกายน 2024 การเปลี่ยนหลักคือ **stateless protocol core** — MCP จากที่เดิมเป็น bidirectional stateful ที่ต้องมี session state ตลอด lifetime ของ connection กลายเป็น **request/response stateless** ปกติ

ผลกระทบทาง infrastructure ชัดมาก: server ที่ก่อนหน้านี้ต้องมี sticky session, shared session store (Redis/DynamoDB), และ deep packet inspection ที่ gateway ตอนนี้รันบน **round-robin load balancer ธรรมดา** ได้ — pod ไหนก็ตอบคำขอไหนก็ได้ Client cache tools/list response ตาม ttlMs ที่ server กำหนด และ route traffic ผ่าน `Mcp-Method` header ธรรมดา = MCP server รันบน **standard Kubernetes cluster** ที่ enterprise มีอยู่แล้ว โดยไม่ต้องมี custom operator หรือ service mesh พิเศษ

Spec นี้เพิ่ม security แบบ enterprise-grade: **RFC 9207 (OAuth 2.0 Authorization Server Issuer Identifier)** = client verify ได้ว่า authorization response มาจาก issuer ที่ถูกต้อง กันการโจมตี mix-up attack และ **RFC 8707 (Resource Indicators for OAuth 2.0)** = restrict token ให้ใช้กับ specific resource เท่านั้น ป้องกัน token exfiltration ที่ MCP ยุคแรกเจอปัญหา (มีเคส CVE ตั้งแต่ต้นปี) พร้อม **Specification Feature Lifecycle + Deprecation Policy** อย่างเป็นทางการ — enterprise CIO ที่กลัวว่า protocol จะเปลี่ยนใต้เท้าตอนนี้มี roadmap ที่ committed

ที่สำคัญไม่แพ้กัน: **EU AI Act high-risk obligations เริ่มบังคับใช้ 2 สิงหาคม 2026** และตัว high-risk category ครอบ **MCP gateway ที่ใช้กับ regulated data** (credit scoring, medical diagnosis, HR screening, education assessment) โดยตรง — บริษัทที่ deploy MCP server บน enterprise use case เหล่านี้ต้องมี conformity assessment, risk management system, human oversight, และ transparency documentation ตาม Article 8-15

## ทำไมสำคัญ
Stateless MCP เป็นช่วง **"HTTP moment"** ของ agent protocol — HTTP กลายเป็น dominant เพราะ stateless (scale ง่าย, cache ง่าย, load balance ง่าย) ต่างจาก stateful protocol อย่าง FTP/SMTP MCP ที่เกิดมา 20 เดือนก่อนเลือก stateful เพราะต้องการ real-time bidirectional (subscription, streaming) แต่ในทางปฏิบัติ **90% ของ MCP use case จริง คือ tool call request/response** — stateful architecture เลย over-engineered

Pattern น่าสนใจ 2 อย่าง: หนึ่ง — **spec เริ่มสะท้อน production reality** ไม่ใช่ theoretical design เดิมอีกต่อไป Anthropic + community เห็นว่า enterprise ที่ deploy MCP เจอ operational bottleneck ตัวจริงคือ session management ไม่ใช่ feature ตัดปัญหานั้นออก = deployment velocity เพิ่มทันที สอง — **timing กับ EU AI Act ที่บังคับใช้ 2 ส.ค.** ไม่ใช่บังเอิญ ถ้า MCP ยังต้อง sticky session = การทำ audit trail และ human-in-the-loop เข้ายาก (session state กระจายทั่ว cluster) stateless = ทุก request auditable ที่ boundary เดียว compliance ทำง่ายกว่ามาก

Signal ต่อจากนี้: **MCP server marketplace boom** — เดิมที่ deploy MCP ต้องมี ops team เต็มตัว ตอนนี้ทีมเล็กก็ deploy บน Kubernetes ที่มีอยู่ได้ = จำนวน public MCP server น่าจะจาก **10K+ (มี.ค. 2026) ทะลุ 50K ภายในปลาย 2026** และ **enterprise MCP gateway vendor** (Cloudflare, Kong, Tyk, Solo.io) จะเปิดตัว native stateless MCP support ในไตรมาสหน้า MCP registry ที่ Anthropic + community พัฒนาอยู่ก็จะกลายเป็น **npm/PyPI ของ agent tool layer** ในปี 2027

## มุม AI Agent Platform
**Builders** ที่รัน MCP server: migration ไปยัง 2026-07-28 spec ควรอยู่ใน Q3 roadmap — โดยเฉพาะถ้า production traffic เข้าจริง sticky session เป็น operational pain ที่หายไปทันที และถ้ายังไม่ implement OAuth ตาม RFC 9207/8707 = จะเจอ security review reject ตอน enterprise procurement

**Users / business** ที่ deploy agent workflow บน MCP: ตรวจสอบว่า vendor stack ของคุณอยู่ในข่าย EU AI Act high-risk หรือไม่ (ถ้าลูกค้า/ข้อมูลอยู่ในยุโรป ตอบว่าใช่แน่นอน) และเริ่ม conformity assessment ทันที deadline for existing systems ให้เวลาถึง ส.ค. 2027 แต่ CIO ที่ฉลาดเริ่มตอนนี้เพราะการทำ risk management system + human oversight ใช้เวลา 6-12 เดือน

**Ecosystem**: คนที่ได้ประโยชน์ = **cloud/K8s vendor** (AWS, GCP, Azure, DigitalOcean, Fly.io) ที่จะ market native MCP hosting, **API gateway** (Cloudflare Workers, Kong, Tyk) ที่ทำ MCP-aware routing, **identity provider** (Okta, Auth0, WorkOS) ที่จะออก MCP-compatible OAuth flows คนที่ต้องปรับตัว = **MCP hosting startup ยุคแรก** (Smithery, mcp.run) ที่ moat จาก session management จะบางลง — ต้อง pivot ไป curation, security scanning, และ enterprise governance features แทน

## Sources
- [The 2026-07-28 Specification (Model Context Protocol Blog)](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [Scaling AI Agent Infrastructure with MCP Stateless updates (Google Developers Blog)](https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/)
- [MCP gets an enterprise makeover (The Register)](https://www.theregister.com/ai-and-ml/2026/07/29/mcp-gets-an-enterprise-makeover/5280027)
- [New Enterprise-Ready MCP Specification Brings New Security Challenges (SecurityWeek)](https://www.securityweek.com/new-enterprise-ready-mcp-specification-brings-new-security-challenges/)

---

## Audio script
เมื่อวันที่ 28 กรกฎาคม MCP working group ปล่อย spec version 2026-07-28 ที่เป็น architectural rewrite ที่ใหญ่ที่สุดตั้งแต่ launch เมื่อพฤศจิกายน 2024 การเปลี่ยนหลักคือ stateless protocol core MCP จากที่เคยเป็น bidirectional stateful ตอนนี้กลายเป็น request response ปกติ

ผลกระทบชัดมาก server ที่ก่อนหน้านี้ต้องมี sticky session shared session store และ deep packet inspection ที่ gateway ตอนนี้รันบน round robin load balancer ธรรมดาได้ pod ไหนก็ตอบคำขอไหนก็ได้ MCP server รันบน Kubernetes cluster ที่ enterprise มีอยู่แล้วโดยไม่ต้องมี custom operator หรือ service mesh พิเศษ

Spec นี้เพิ่ม security แบบ enterprise คือ RFC 9207 ที่ client verify ได้ว่า authorization response มาจาก issuer ที่ถูกต้อง และ RFC 8707 ที่ restrict token ให้ใช้กับ resource เดียว ป้องกัน token exfiltration พร้อม Feature Lifecycle กับ Deprecation Policy อย่างเป็นทางการ enterprise CIO ที่กลัว protocol เปลี่ยนตอนนี้มี roadmap ที่ committed แล้ว

ที่สำคัญไม่แพ้กัน EU AI Act high risk obligations เริ่มบังคับใช้ 2 สิงหาคม 2026 และครอบ MCP gateway ที่ใช้กับ regulated data โดยตรง เช่น credit scoring, medical diagnosis, HR screening บริษัทที่ deploy MCP server บน use case เหล่านี้ต้องมี conformity assessment, risk management, human oversight, และ transparency documentation

Stateless MCP เป็นช่วง HTTP moment ของ agent protocol เพราะ 90 เปอร์เซ็นต์ของ MCP use case จริงคือ tool call request response ไม่ต้อง stateful

สำหรับ builder ที่รัน MCP server migration ไป 2026-07-28 spec ควรอยู่ใน Q3 roadmap โดยเฉพาะถ้ามี production traffic จริง สำหรับ business ที่ deploy agent บน MCP ตรวจสอบว่า vendor stack อยู่ในข่าย EU AI Act high risk หรือไม่ และเริ่ม conformity assessment ทันทีครับ
