---
date: 2026-09-25
slug: google-antigravity-gemini-api-09
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a glowing hexagonal API portal floating
  above a Google-branded sandbox terminal, with three stacked labels on the
  right: "FILES API", "CREDENTIALS API", "MCP TOOL BRIDGE". A tiny satellite
  labeled "antigravity-preview-09-2026" orbits an older greyed-out satellite
  marked "05-2026 — SHUTS DOWN OCT 5". Editorial illustration in the style of a
  Wired developer cover, cinematic teal and neon-lime palette, high contrast for
  200px thumbnails, no real human faces, 1:1 aspect.
image: images/26-09-28-0616-02-google-antigravity-gemini-api-09.png
---

# Google เอา Antigravity coding agent ยัดเป็น managed agent ใน Gemini API — เปิดฟรี tier, ปิด May version วันที่ 5 ต.ค.

## TL;DR
- Google ปล่อย `antigravity-preview-09-2026` เข้า Gemini API + AI Studio — เป็น managed agent ที่รันใน sandbox Linux ของ Google เอง มี plan/reason/tool-call/file-mgmt/web-search ครบชุด
- Version ใหม่มาพร้อม Files API + Credentials API + native code search + line-range editing + prompt caching — deprecate version พฤษภาคม 5 ต.ค. 2026
- Free tier ใช้ได้ทันที ผ่าน Interactions API — agent-as-API primitive ที่พร้อมสำหรับทั้ง prototype และ production

## เกิดอะไรขึ้น
Google เพิ่ง update docs ของ Gemini API ให้ Antigravity เป็น managed agent ตัวแรกที่ callable ผ่าน Interactions API ทั้งใน free tier และ paid tier. Version ล่าสุดชื่อ `antigravity-preview-09-2026` ที่ปล่อยเดือนนี้ replace `antigravity-preview-05-2026` ที่จะปิดตัววันที่ 5 ตุลาคม 2026. Release notes ระบุการ upgrade runtime harness ให้มี prompt caching ที่ดีขึ้น, native code search tools, และ file editing แบบ line-range — 3 อย่างที่ตรงกับ pain point ที่ coding agent generation แรก ๆ (Devin, SWE-agent) เจอบ่อย.

Antigravity เดิมเปิดตัวใน Google I/O 2026 เดือนพฤษภาคม — เป็น "coding agent" ที่ทำได้ทั้ง plan, reason, run code, manage files, และ search web โดยรันใน isolated Linux sandbox ที่ Google host ให้ ตัว developer ไม่ต้องเปิด VM เอง. รอบนี้ Google ทำการเปลี่ยนแปลง 2 อย่างที่สำคัญ: หนึ่ง คือ **แยก Antigravity เป็น managed agent primitive** ที่เข้าถึงผ่าน API — ไม่ใช่แค่ product ที่ใช้ใน AI Studio; สอง คือเปิด **Credentials API** ให้ agent เรียก MCP servers และ third-party APIs ได้ในลักษณะที่ Google ช่วย broker credential — จุดที่ทั้ง OpenAI และ Anthropic ยังบังคับให้ developer จัดการ secret เอง.

Documentation ของ Google ยังเปิด Files API สำหรับดึงข้อมูลเข้าออก sandbox — พร้อม path ที่ predictable สำหรับ CI/CD integration. คู่กับ prompt caching ที่ upgrade ใหม่ Google กำลังจะ position ตัวเองในโพซิชั่นที่ต่างจาก competitor: ไม่ใช่ "model + IDE plugin" แบบ Cursor หรือ Windsurf ไม่ใช่ "agent-as-product" แบบ Devin ของ Cognition — แต่เป็น **agent-as-managed-API primitive** ที่ developer เอาไปประกอบใน pipeline ของตัวเอง.

## ทำไมสำคัญ
Signal ที่สำคัญไม่ใช่ตัว feature — คือ **สถานะทางการตลาด**. Google กำลังเลิกเชื่อว่า coding agent จะขายผ่าน IDE product เดี่ยว ๆ (แบบที่ Cursor + Windsurf ครองอยู่) แต่จะขายเป็น commodity primitive ผ่าน API ที่ตัวเองมี distribution แข็งอยู่แล้ว. เมื่อคำนึงว่า Cognition เพิ่งปิด Series E 2 พันล้านที่ valuation 4.8 หมื่นล้าน (ARR $900M) — และ Cursor ผลักผ่าน $1B ARR ไป — Google ต้องเลือกว่าจะสู้ direct หรือกลับไป layer ล่าง. Antigravity 09-2026 บอกว่า Google เลือก layer ล่าง.

การเปิด Credentials API เป็นก้าวใหญ่ที่ underrated ตอนนี้. Anthropic เพิ่งประกาศ Enterprise-Managed Authorization extension ให้ MCP ช่วง มิ.ย. โดยผ่าน Okta เป็น IdP แรก. Google เดินคนละทาง: broker credential ให้ agent ที่ตัวเอง host — enterprise ไม่ต้องเลือก IdP, ไม่ต้อง config OAuth flow, ยก responsibility ให้ Google. Trade-off คือ lock-in ใหม่ — agent ต้องรันใน Google sandbox — แต่สำหรับ enterprise ที่อยู่บน Google Cloud อยู่แล้ว มันคือ path of least resistance.

Free tier ก็เป็น pressure point ที่ทำให้ developer indie + startup มีทางเลือกใหม่. ก่อนหน้านี้ agent-as-API ราคาแพงมาก (Cognition ไม่มี free tier, Anthropic ต้อง pay ทันที) — ตอนนี้คุณเปิด account Gemini API ฟรี ๆ ก็ได้ agent ตัวหนึ่งที่ทำงานเทียบชั้นได้แล้ว. บริษัทที่ทำ vertical AI agent (legal, finance, healthcare) ที่ต้องการ underlying general-purpose runtime มี option ใหม่ที่ประหยัดค่า infra ลงเยอะ.

## มุม AI Agent Platform
**Builders** — Antigravity เป็น reference implementation ที่ควร map กับ system ของตัวเอง. ถ้าคุณสร้าง orchestration framework (LangGraph, CrewAI, Vercel AI SDK, Agno) — 3 สิ่งที่ Google ทำ (managed sandbox + Files API + Credentials API) คือสิ่งที่ user ต้องประกอบเองใน platform อื่น. ถ้าจะ compete ที่ layer นั้น ต้องมี paved path ให้ครบ. **Users / business** — ถ้าคุณ deploy agent ที่ต้อง call multiple third-party API (Salesforce, Notion, GitHub, custom API) — Credentials API ของ Google จะ save ทีม infra 3-6 เดือนของงาน. ราคา trade-off คือ code + data ต้องเข้าไปใน Google sandbox — ประเมิน compliance ก่อน adopt. **Ecosystem** — pattern ที่ชัดหลัง Antigravity 09-2026 คือ **coding agent จะ commoditize เร็วขึ้น**. Value จะเลื่อนไปที่ (1) IDE/UX ที่คนใช้จริง (Cursor position), (2) domain expertise agent (Harvey สำหรับ law, Sierra สำหรับ CS), และ (3) governance stack (Alation, Cohesity, Dataiku). Vendor ที่ยังคิดว่า "we build agents" คือ moat จะต้องเลื่อน positioning ภายใน 6 เดือน.

## Sources
- [Antigravity preview | Gemini API — Google AI for Developers](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-09-2026)
- [Antigravity agent | Gemini API — Google AI for Developers](https://ai.google.dev/gemini-api/docs/antigravity-agent)
- [Gemini API Managed Agents Update — AI Studio Learn](https://aistudio.google.com/learn/managed-agents-updated-harness-files-credentials)
- [Google turns its Antigravity coding agent into a free Gemini API tool — Startup Fortune](https://startupfortune.com/google-turns-its-antigravity-coding-agent-into-a-free-gemini-api-tool/)

---

## Audio script
Google เพิ่งย้าย coding agent ของตัวเองชื่อ Antigravity มาเป็น managed agent ใน Gemini API ครับ. Version ใหม่ชื่อ antigravity-preview-09-2026 เข้าถึงได้ทั้ง free tier และ paid tier ผ่าน Interactions API. Antigravity เป็น agent ที่ทำได้ทั้ง plan, reason, run code, manage files, และ search web โดยรันใน isolated Linux sandbox ของ Google เอง developer ไม่ต้องเปิด VM. รอบนี้ Google upgrade harness ให้มี prompt caching ที่ดีขึ้น, native code search และ line-range editing แล้วเพิ่ม Files API กับ Credentials API — ตัวหลังนี่คือของสำคัญ agent สามารถเรียก MCP servers และ third-party API ผ่าน credential broker ของ Google เอง developer ไม่ต้อง manage secret. Signal จริงไม่ใช่ feature แต่คือ Google ยอมรับว่าจะสู้ Cursor Windsurf Cognition ที่ product layer ตรง ๆ ไม่ไหว เลยกลับไป layer ล่าง แล้วขาย coding agent เป็น commodity API primitive ผ่าน distribution ของตัวเอง. Version พฤษภาคมของ Antigravity จะปิดวันที่ 5 ตุลาคม — ถ้าคุณใช้อยู่ต้องอัปเดต. สำหรับคนสร้าง orchestration framework Antigravity คือ reference implementation ที่ควรเทียบ ถ้ายังต้องให้ user ประกอบ sandbox + Files API + Credentials API เอง moat กำลังหายไป. สำหรับ business ที่ deploy agent เรียก third-party API เยอะ Google ช่วย save ทีม infra 3-6 เดือน แต่ trade-off คือ code กับ data ต้องอยู่ใน sandbox ของ Google ประเมิน compliance ก่อน adopt.
