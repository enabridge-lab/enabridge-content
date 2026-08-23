---
date: 2026-08-22
slug: mcp-2026-roadmap-agent-identity-dpop
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A wide editorial isometric illustration of a modernist protocol foundation
  labeled "MCP" with five glowing pillars rising above it, each pillar tagged
  with a short label: "AGENT IDENTITY", "DPoP", "WORKLOAD FEDERATION",
  "SERVER-INITIATED EVENTS", "RESULT TYPES". A silhouette of an agent robot
  is walking up to a doorway on the foundation, holding a small badge glyph
  instead of a browser password prompt. Sharp navy and deep-teal palette
  with amber accent lighting. High contrast, chunky sans-serif labels
  readable at 200px thumbnail size, 1:1 aspect ratio, no real human faces.
image: images/26-08-23-0609-01-mcp-2026-roadmap-agent-identity-dpop.png
---

# MCP roadmap 2026 — protocol โตขึ้น, ยก agent identity เป็น first-class

## TL;DR
- Core Maintainers ปล่อย MCP 2026 roadmap วันที่ 22 ส.ค. — จัด 5 priority areas โดย **agent identity** ขึ้นมาเป็นเรื่องหลัก แทนที่จะเป็น "รอไว้ก่อน"
- DPoP (SEP-1932) และ Workload Identity Federation (SEP-1933) กลายเป็น proposal ที่ maintainers กำลังผลักดันให้ไปถึง finalization
- SDK ของ Python + TypeScript รวมกันโหลด ~97M ครั้ง/เดือน — MCP กลายเป็น de facto layer ที่ Claude, ChatGPT, Goose, VS Code รองรับ native หมด

## เกิดอะไรขึ้น
วันที่ 22 ส.ค. 2026 ทีม Core Maintainers ของ Model Context Protocol โพสต์ roadmap ใหม่บน blog.modelcontextprotocol.io พร้อมสรุปทิศทาง 6–12 เดือนข้างหน้าเป็น 5 priority areas ที่ working groups จะโฟกัสในการ shape spec ต่อไป — server-initiated events, result type improvements, agent identity, transport, และ ecosystem tooling

หัวใจของรอบนี้คือคำว่า **agent identity** — เดิม MCP ออกแบบ authorization รอบสมมติฐานว่ามี "คนกดยืนยันในเบราว์เซอร์" ซึ่งใช้ได้ดีกับ interactive client อย่าง Claude Desktop หรือ Cursor แต่พอเข้าปี 2026 caller ส่วนใหญ่กลายเป็น agent ที่รันเป็น cloud workload มี identity ของตัวเอง ทำหน้าที่แทน user ที่ไม่ได้อยู่หน้าจอ และบ่อยครั้งยัง delegate อำนาจต่อไปให้ sub-agent — model ยืนยันด้วย browser ไม่พอแล้ว

Roadmap เลย highlight active proposal สองอันขึ้นมา: **SEP-1932 (DPoP — Demonstrating Proof of Possession)** ที่ผูก token กับ key ที่ agent ถือ ทำให้ token ที่รั่วเอาไปใช้ไม่ได้ และ **SEP-1933 (Workload Identity Federation)** ที่ให้ MCP server เชื่อ identity ที่มาจาก AWS IAM, Google Cloud Service Account, หรือ SPIFFE/SPIRE โดยไม่ต้องออก long-lived secret เพิ่ม — pattern เดียวกับที่ enterprise SRE ใช้ระหว่าง service อยู่แล้ว

## ทำไมสำคัญ
ปี 2025 เราคุยกันว่า "MCP จะเป็น USB-C ของ agent tooling ไหม" — พอเข้าปี 2026 นี่คือคำถามที่ตอบไปแล้ว SDK สอง runtime หลักโหลดรวมกัน 97 ล้านครั้ง/เดือน framework agent เกือบทุกเจ้ารองรับ และ 2026-07-28 spec ที่ตัด session state ทิ้ง (คลุมไปในรอบก่อน) เพิ่งเปิดทางให้ horizontal scale ได้แบบ HTTP ปกติ

Roadmap รอบนี้จึงเป็นสัญญาณของ **phase 2** — จาก "connect ทุกอย่างเข้ากัน" ไปสู่ "run ในระดับ enterprise แบบ audit ได้" การที่ agent identity ขึ้นเป็น priority พร้อม DPoP + Workload Federation แปลว่า maintainers ยอมรับว่ายุคของ "agent ยืม token ของ user" กำลังจบ — ต่อไปนี้ agent จะต้องมี identity ของตัวเอง มี proof-of-possession และถูก federate เข้าระบบ IAM ขององค์กร

เทียบกับ OAuth 2.0 rollout ในทศวรรษที่แล้ว เราอยู่ราวปี 2015 ของ MCP — spec โครงหลักเสถียร แต่ enterprise-hardening (rotation, delegation, revocation, audit) เพิ่งเริ่มถูกเขียนเป็น standard

## มุม AI Agent Platform
สำหรับ **builders** ที่ทำ framework/runtime/orchestration: อ่าน SEP-1932 กับ SEP-1933 ให้เข้าใจ scope แล้วเริ่มออกแบบ layer ที่รองรับ workload identity แทนที่จะ hard-code interactive OAuth flow — เพราะภายในปีนี้ enterprise buyer จะเริ่มถามหา และ vendor ที่ต่อกับ SPIFFE/Workload Federation ได้ก่อนจะได้เปรียบตอน RFP

สำหรับ **users/business** ที่ deploy agent ใน workflow: bar ของ security posture จะขยับขึ้น — ถ้ายังใช้ pattern "agent ถือ API key ของ user" อยู่ให้เตรียม migration plan ไปหา per-agent identity ก่อนที่ audit จะถามหา นี่เป็นเรื่องเดียวกับตอน service-to-service auth ย้ายจาก shared secret ไป mTLS เมื่อ 5–7 ปีก่อน

สำหรับ **ecosystem** (cloud, IAM vendor, security platform): จังหวะทองสำหรับ Okta, Auth0, HashiCorp Vault, AWS IAM, Google Workload Identity ที่จะเข้ามาเสียบเป็น broker — ใครออก MCP-native adapter ก่อนคือคนที่จะกิน layer นี้ไป และเป็นสัญญาณสำคัญให้ Enabridge ในฐานะ AI Agent Platform ต้องมี agent identity story ที่ชัดเจนตั้งแต่ day 1

## Sources
- [The New MCP Roadmap — Model Context Protocol Blog (Aug 22, 2026)](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/)
- [The 2026 MCP Roadmap — Model Context Protocol Blog](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/)
- [The Future of MCP: 2026 Roadmap, Enterprise Adoption, and What Comes Next — Toloka](https://toloka.ai/blog/the-future-of-mcp-enterprise-adoption/)

---

## Audio script
วันนี้ทีม Core Maintainers ของ MCP หรือ Model Context Protocol เพิ่งปล่อย roadmap ปี 2026 ออกมา และประเด็นที่น่าจับตาที่สุดคือเรื่อง agent identity ครับ

เดิมที MCP ออกแบบบนสมมติฐานว่ามีคนกดยืนยันในเบราว์เซอร์ ซึ่งใช้ได้ดีกับ Claude Desktop หรือ Cursor แต่ตอนนี้ caller ส่วนใหญ่กลายเป็น agent ที่รันบน cloud มี identity ของตัวเอง และหลายครั้งยังส่งต่ออำนาจไปให้ sub-agent อีกที ดังนั้นการยืนยันด้วยเบราว์เซอร์อย่างเดียวมันไม่พอแล้ว

Roadmap ยกสอง proposal ขึ้นมา — DPoP หรือ Demonstrating Proof of Possession ที่ผูก token กับ key ของ agent ทำให้ token รั่วก็ใช้ไม่ได้ และ Workload Identity Federation ที่ให้ MCP server เชื่อ identity จาก AWS IAM, Google Cloud Service Account หรือ SPIFFE โดยไม่ต้องออก secret เพิ่ม

สัญญาณคือ MCP กำลังเข้าสู่ phase 2 — จาก "เชื่อมทุกอย่างเข้ากัน" ไปสู่ "รันในระดับ enterprise แบบ audit ได้" ถ้าคุณเป็นทีมสร้าง agent platform วันนี้เริ่มออกแบบให้รองรับ workload identity ตั้งแต่ตอนนี้จะได้เปรียบตอน enterprise เขาเริ่ม RFP ครับ
