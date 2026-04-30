---
date: 2026-04-30
slug: cloudflare-code-mode-agents-customers
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: Editorial illustration of a glowing API portal compressing thousands of pipes into a single thin beam of light, with autonomous agent silhouettes stepping through as paying customers, minimal flat shapes, muted teal and amber palette, dramatic side lighting, no text no logos no faces
image:
---

# Cloudflare เปิดทาง agents เป็นลูกค้าตัวเอง — พร้อมบีบ API 1.17M tokens เหลือ 1,000

## TL;DR
- Cloudflare ประกาศวันที่ 30 เม.ย. 2026 ว่า AI agents สามารถสมัคร Cloudflare account, ซื้อ subscription, จด domain, รับ API token แล้ว deploy code ได้เอง — ไม่ต้องผ่านมนุษย์ (ยกเว้นช่วง accept ToS)
- "Code Mode" pattern ใหม่บีบ MCP exposure จาก 2,500+ endpoints (~1.17M tokens) เหลือ ~1,000 tokens — ลด context cost ~99.9% โดยให้ model เขียน JS รัน V8 isolate แทนเรียก tool ทีละตัว
- เปิดเป็นส่วนหนึ่งของ Agents Week 2026 — agentic infrastructure layer กำลัง consolidate รอบ Cloudflare เร็วกว่า hyperscaler

## เกิดอะไรขึ้น

วันที่ 30 เม.ย. Cloudflare ปิด Agents Week 2026 ด้วย announcement สองตัวที่ติดกันเหมือนเฟืองล็อกกัน เฟืองแรก: agents กลายเป็นลูกค้า Cloudflare ได้แล้วโดยตรง — สร้าง account, จ่าย subscription, จด domain, รับ API token, push code ขึ้น Workers — ทั้งหมดผ่าน programmatic onboarding ที่ออกแบบให้ agent ทำเองได้ ไม่มีมนุษย์คั่นกลาง (มี human-in-the-loop เฉพาะตอน accept Terms of Service ครั้งแรก) เฟืองที่สอง: "Code Mode" — pattern ใหม่ที่เปลี่ยนวิธีที่ agent คุยกับ MCP server จาก "list ทุก tool ในระบบใส่ context" เป็น "ให้ model เขียน JavaScript เรียก SDK รันใน V8 isolate"

ตัวเลขที่ Cloudflare กางออกมาน่าตกใจ: API ของ Cloudflare เองมี endpoints มากกว่า 2,500 ตัว ถ้าโหลดเข้า MCP context ทั้งหมดจะกิน ~1.17 ล้าน tokens ก่อนเริ่มงานจริง — ในทางปฏิบัติคือใช้ไม่ได้ Code Mode ลดเหลือสองเครื่องมือเท่านั้น: `search()` กับ `execute()` plus type-aware SDK ที่ model generate code เรียกได้ตรง ๆ — รวมแล้ว ~1,000 tokens หรือลดลง ~99.9% และยังต่อ MCP Server Portals ที่รวบ MCP servers หลายตัวไว้หลัง gateway เดียว มี audit, access control, progressive tool disclosure — เปลี่ยน MCP จาก "เปิดทุก tool ตลอดเวลา" เป็น "เรียกเมื่อ agent ต้องใช้จริง"

ภาพรวมที่ Cloudflare วางคือ **agent cloud แบบ end-to-end** — Workers runtime, Durable Objects state, Vectorize memory, AI Gateway routing, Workers AI inference, Hyperdrive DB, R2 storage, Email service สำหรับ agents (เพิ่งเปิด public beta) แล้วจบที่ payment + onboarding ที่ agents จัดการเอง — **agents-as-tenants** เต็มรูปแบบ Matthew Prince ขายเรื่องนี้เป็น "agentic cloud" ที่ออกแบบมาตั้งแต่ layer 0 ไม่ใช่ retrofit hyperscaler เก่า

## ทำไมสำคัญ

นี่คือสัญญาณว่า **agentic infrastructure** กลายเป็น category แยกจาก "AI infra" ทั่วไปแล้ว — และ Cloudflare กำลัง position ตัวเองเป็น default layer ก่อน AWS/GCP/Azure ขยับทัน ถ้าเทียบกับ Microsoft Agentic Fabric (MCP บน data platform) หรือ Adobe CX Enterprise (MCP บน CX stack) — Cloudflare ลงลึกที่ "compute + identity + payment" ซึ่งคือ primitive ที่แต่ละชั้นต้องพึ่ง pattern ที่เห็นชัด: ใครเปิด agent identity + agent billing ก่อน คนนั้นได้ default placement ในการ onboard agents ใหม่ — เหมือน AWS ได้ default ตอน cloud-native era

Code Mode ตัวเลข 99.9% ก็เป็น signal สำคัญ: industry กำลังตระหนักว่า MCP เวอร์ชันแรก ๆ "tool dump ใส่ context" คือ anti-pattern ที่ทั้งแพง ทั้งช้า ทั้งทำให้ model สับสน Anthropic เองก็เพิ่งออก guideline ทำนองเดียวกันใน Q1 — Cloudflare แค่ implement reference architecture ออกมาก่อน คาดว่าภายใน 90 วัน คนจะเห็น MCP server pattern เปลี่ยน: search/execute สองตัว + code-generated tool calls กลายเป็น default ส่วน "list 50 tools" จะถูก deprecate ไปเงียบ ๆ

## มุม OpenBridge

ตรงเป้า OpenBridge มาก — สอง angle: **(1) Integration platform ต้อง audit ของตัวเอง** ถ้า OpenBridge expose tool ผ่าน MCP สมมติมี 200+ endpoints ก็ต้องเริ่ม design search()/execute() pattern เหมือนกัน ไม่อย่างนั้น token cost จะทำให้ลูกค้าวิ่งหนีไปคู่แข่ง — ลองคิด tier: tools list สั้น ๆ สำหรับ discovery, code-mode SDK สำหรับ execution (2) **Agent-as-customer billing model** เป็นโจทย์ใหม่ — ถ้า agent สมัคร OpenBridge เองได้ผ่าน programmatic API, มี usage-based pricing, มี per-agent identity แยกจาก human user, มี audit trail ที่บอกว่า agent ไหนเรียกอะไรเมื่อไหร่ — นั่นคือ moat ระดับ infrastructure ที่ SaaS บริษัทอื่นใช้เวลานานกว่าจะตามทัน

ระยะ 30 วัน ทีมควรลองออกแบบ MCP entry สอง flavor: classic tool list (สำหรับ Claude/ChatGPT consumer agent ที่ยังไม่ใช่ Code Mode) และ Code Mode SDK (สำหรับ enterprise agent ที่เริ่ม optimize cost) — ดู conversion rate ระหว่างสอง flavor ว่าฝั่งไหน sticky กว่า

## Sources
- [Code Mode: give agents an entire API in 1,000 tokens — Cloudflare Blog](https://blog.cloudflare.com/code-mode-mcp/)
- [Agents can now create Cloudflare accounts, buy domains, and deploy — Cloudflare Blog](https://blog.cloudflare.com/agents-stripe-projects/)
- [Cloudflare Launches Code Mode MCP Server to Optimize Token Usage for AI Agents — InfoQ](https://www.infoq.com/news/2026/04/cloudflare-code-mode-mcp-server/)
- [Building the agentic cloud: everything we launched during Agents Week 2026 — Cloudflare Blog](https://blog.cloudflare.com/agents-week-in-review/)

---

## Audio script
ข่าวใหญ่จาก Cloudflare เมื่อวันที่ 30 เม.ย. ปิด Agents Week ด้วยสองเรื่องที่เปลี่ยน landscape เลยนะ เรื่องแรกคือ AI agents สมัคร Cloudflare account เองได้แล้ว จ่ายเงินเอง จด domain เอง ได้ API token แล้ว deploy code ได้ทันที โดยไม่ต้องมีมนุษย์ทำให้ — เป็นครั้งแรกที่ hyperscaler tier เปิดให้ agent เป็น tenant เต็มตัว เรื่องที่สองคือ Code Mode — pattern ใหม่ที่เปลี่ยนวิธี agent คุยกับ MCP จาก "list ทุก tool ใส่ context" มาเป็นให้ model เขียน JavaScript รันใน V8 isolate ลด token จาก 1.17 ล้านเหลือพันเดียว 99.9% เลย สำหรับ OpenBridge ตรงเป้ามาก เพราะถ้าเรา expose integration tools ผ่าน MCP ต้องเริ่มคิดเรื่อง search execute pattern แล้ว ไม่งั้นลูกค้าจะวิ่งหนีไปหาคู่แข่งที่ optimize cost ดีกว่า อีกเรื่องคือ agent-as-customer billing — ถ้าเราออกแบบให้ agent สมัครเอง จ่ายเอง มี audit trail per-agent เร็วกว่าคู่แข่ง นั่นคือ moat infrastructure ระดับใหญ่
