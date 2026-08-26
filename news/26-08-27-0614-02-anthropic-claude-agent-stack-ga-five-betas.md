---
date: 2026-08-27
slug: anthropic-claude-agent-stack-ga-five-betas
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial isometric illustration of a Claude-branded factory floor with FIVE
  glowing crates being simultaneously stamped "GA" in bold orange ink. Each
  crate carries a label: "COMPUTER USE", "BROWSER USE", "FILES API", "AGENT
  SKILLS", "ADMIN API". A giant "BETA" stamp lies discarded on the floor.
  Overhead sign reads "AUG 19, 2026" in industrial serif letters. Editorial
  isometric style, warm orange + charcoal palette, dramatic key light. 1:1
  aspect. No real human faces (silhouette only). High contrast so text and
  labels read at 200px thumbnail.
image: images/26-08-27-0614-02-anthropic-claude-agent-stack-ga-five-betas.png
---

# Anthropic ปล่อย 5 beta ขึ้น GA พร้อมกัน 19 ส.ค. — Claude agent stack "production-ready" ครบชุด, Computer Use รอ 1 ปี 10 เดือน

## TL;DR
- **19 ส.ค. 2026** Anthropic push **5 features** จาก beta ขึ้น GA พร้อมกันในวันเดียว: **Computer Use** (computer_toolset_20260801), **Browser Use** (browser_toolset_20260801, tool ใหม่ ไม่ใช่ rename), **Files API**, **Agent Skills API** (/v1/skills), และ **Admin API user management** (Enterprise plan)
- Computer Use รอ **1 ปี 10 เดือน** จาก preview → GA — ตอนนี้รองรับ **batch actions** (agent ยิงหลาย action ในหนึ่ง turn); Browser Use อ่าน accessibility tree, set form values ตรง, จัดการ tabs + downloads
- **Anthropic-beta header เลิกต้องใช้แล้วทั้ง 5 ตัว** — สัญญาณ v1 stability, spec ล็อค + billing tier ผ่าน enterprise procurement, no more experimental disclaimers
- Signal: Claude agent stack เข้าสถานะ **production-grade end-to-end** พร้อมชนกับ OpenAI Assistants v2 + Google Gemini Enterprise Agent Platform — timing เดียวกับ MCP/A2A ย้ายไป AAIF, Anthropic กำลัง lock ecosystem lead

## เกิดอะไรขึ้น

19 ส.ค. 2026 Anthropic ประกาศ **5 major features** ขึ้น General Availability พร้อมกันบน Claude API — ปกติ Anthropic จะปล่อย GA ที่ละตัวห่างกันเป็นเดือน, การ ship 5 ตัวในวันเดียวคือ **coordinated push** ที่ signal ว่า agent stack ทั้งชุดพร้อมแล้ว

หัวใจของรอบนี้คือ **Computer Use** — feature ที่ Anthropic เปิด preview ตั้งแต่ ต.ค. 2024 (Claude 3.5 Sonnet), ใช้เวลา **1 ปี 10 เดือน** ในการ productionize. Toolset ใหม่ชื่อ `computer_toolset_20260801` มาพร้อม **batch actions** — agent execute หลาย action (click, type, scroll) ใน one turn แทนที่ต้อง round-trip ทุก step. Latency ต่อ workflow ลด 3-5 เท่าตาม benchmark ที่ ChannelInsider รายงาน

**Browser Use** เป็น tool ใหม่คนละตัวกับ Computer Use ไม่ใช่ rename — `browser_toolset_20260801` driver browser ที่ app ของคุณ host เอง (ปกติเป็น Playwright/Chromium). อ่าน **accessibility tree** พร้อม element references, set form values ตรงเข้า DOM (แทน screen coordinate), จัดการ tabs + downloads. เร็วกว่า + reliable กว่า Computer Use สำหรับ web-only workflow — แต่ Computer Use ยังจำเป็นสำหรับ desktop app / native tool

**Files API + Skills API + Admin API** เป็น backbone layer: Files API ให้ upload/reference file objects พร้อม expiration + pagination + `ids[]` filter — enterprise data plumbing ที่ built-in retention rules. **Agent Skills** เป็น named + versioned skill packages ที่ agent เรียกเป็น first-class primitive (ไม่ต้อง prompt-engineer ซ้ำทุกครั้ง) — Skills API `/v1/skills` เปิดให้ enterprise สร้าง private skill registry ของบริษัท. **Admin API** จัดการ members/invites/groups/custom roles สำหรับ Claude Enterprise org — เชื่อม SCIM + SSO ได้แล้ว

**Anthropic-beta header ไม่ต้องส่งแล้วสำหรับทั้ง 5 ตัว** — สัญญาณ spec ล็อค, billing tier ผ่าน enterprise procurement review, และ SLA รับประกันแล้ว (Anthropic ยังไม่ประกาศตัวเลข SLA ชัด แต่ enterprise contract standard คือ 99.9%)

## ทำไมสำคัญ

Pattern ชัด: **frontier lab กำลังเปลี่ยน stance จาก "model provider" → "agent platform provider"**. หนึ่งปีก่อน Anthropic ขาย API + Claude Console; วันนี้ขาย **agent runtime + tool ecosystem + skill registry + enterprise identity** ครบ stack. ราคาที่จะจ่ายคือ **complexity surface กว้างขึ้น** — ก่อนหน้านี้ต้อง maintain แค่ model quality, ตอนนี้ต้อง maintain Files API uptime, Skills registry compatibility, Computer Use security posture. แต่ payoff คือ enterprise ซื้อ platform ทั้งชุดจากเจ้าเดียว — ARR per customer โตกว่า model-only revenue หลายเท่า

**จุดเปรียบ vs OpenAI:** OpenAI Assistants API v2 (เปิดตัว WWDC-style event ก.ค. 2026) มี Function Calling + Code Interpreter + File Search + Retrieval — คล้ายกัน แต่ยังไม่มี native computer-control tool ที่ GA (Operator ยัง preview). Anthropic ที่ push Computer Use ก่อน 1 ปี 10 เดือน, ตอนนี้ productionize สำเร็จก่อน — competitive moat จริง สำหรับ workflow ที่ต้อง interact กับ legacy desktop app หรือ browser-only SaaS ที่ไม่มี API

**Ecosystem signal:** timing ที่ 19 ส.ค. ก่อน A2A ย้ายไป AAIF วันที่ 20 ส.ค. — เดา coordinate ไม่ยาก. Anthropic push agent stack ให้ **production-ready** ก่อน, แล้ววันรุ่งขึ้น protocol layer ย้ายบ้าน. รวมกันคือข้อความชัด: "MCP + A2A จะเป็น standards, Claude เป็น reference implementation ของทั้งคู่ที่ enterprise-grade แล้ว — build บน Claude ไม่มี lock-in เพราะ protocol เป็น open standards, แต่ platform maturity + support ต้องมาจากที่นี่"

**คำถามที่เหลือคือ pricing.** Anthropic ยังไม่ประกาศ Files API + Skills API pricing สุดท้าย (คาดเห็นในไตรมาสหน้า). ถ้าตั้งราคา flat + reasonable — enterprise adoption แรง. ถ้าคิด per-request + per-storage — จะเปิดช่องให้ AWS Bedrock AgentCore, Google Gemini Enterprise ตัดราคาชิง deal

## มุม AI Agent Platform

**Builders:** ถ้าคุณเขียน agent app ที่ใช้ Anthropic-beta headers อยู่ — **ลบทิ้งได้เลยจาก 5 header ต่อไปนี้:** `computer-use-2025-01-24`, `browser-use-2026-04-15`, `files-2025-08-30`, `skills-2025-10-02`, `admin-api-2025-05-01`. ถ้ายังใส่ header, request จะ work ต่อ (backward compat) แต่ response format จะเป็น deprecated format. **ที่สำคัญกว่า:** ถ้ายัง prompt-engineer skill logic ทุก request — เปลี่ยนไปใช้ Skills API เก็บ skill เป็น versioned artifact, agent เรียก by name, ประหยัด token 40-60% ต่อ conversation

**Users / business:** Enterprise ที่ pilot Claude ในไตรมาสที่แล้ว — **rollout production ได้แล้ว**. Compliance officer ที่ block เพราะ "still beta" ต้องยอมแล้ว. Workflow ที่ควร prioritize: (1) Computer Use สำหรับ legacy internal app ที่ไม่มี API (SAP, Oracle, custom .NET), (2) Browser Use สำหรับ SaaS ที่ block API access (LinkedIn Sales Nav, some CRM/ERP tenants), (3) Skills API สำหรับ compliance/regulatory workflow ที่ต้อง audit + versioning. Thai enterprise (ธนาคาร, ประกัน, โรงพยาบาล) ที่รอ SLA-backed Computer Use — จังหวะเริ่มโครงการคือตอนนี้

**Ecosystem:** OpenAI น่าจะเร่ง Operator GA + Assistants v3 ในไตรมาสนี้ เพื่อ close gap. Google Gemini Enterprise Agent Platform มี Vertex AI + Agentspace แต่ยังไม่มี native browser/computer control ที่เทียบชั้น — คาด Google ประกาศตอน Cloud Next Tokyo ต.ค.. Cohere / Mistral / Databricks จะเสียเปรียบต่อ enterprise deal ที่ต้อง computer-control tool. **สำหรับ OpenBridge:** ถ้า orchestrate multi-vendor agents — plan ให้ Computer Use route ไป Claude by default (จนกว่าคู่แข่งจะไล่ทัน), Text-only reasoning ยัง multi-vendor ได้ตามราคา/latency

## Sources
- [Anthropic Makes AI Agent Tools Production-Ready (Enterprise DNA)](https://enterprisedna.co/resources/news/anthropic-browser-use-computer-use-skills-api-enterprise-ga-august-2026/)
- [Anthropic Expands Claude Computer Use With Browser Access, Skills and File Storage (Channel Insider)](https://www.channelinsider.com/ai/news-anthropic-claude-computer-use-skills-files-api/)
- [Browser Use Is a New Claude Tool, Not a Renamed One (Digital Applied)](https://www.digitalapplied.com/blog/anthropic-browser-use-tool-ga-new-agent-toolset)
- [Five Betas Went GA. Which Headers Can You Delete Now (Digital Applied)](https://www.digitalapplied.com/blog/claude-platform-betas-ga-computer-use-files-skills)
- [Claude Developer Platform Updates by Anthropic (Releasebot)](https://releasebot.io/updates/anthropic/claude-developer-platform)

---

## Audio script
วันอังคารสิบเก้าสิงหา. Anthropic ปล่อยห้าฟีเจอร์ขึ้น GA พร้อมกันบน Claude API. Computer Use. Browser Use. Files API. Agent Skills API. Admin API. ปกติ Anthropic ปล่อย GA ทีละตัวห่างกันเป็นเดือน. การ ship ห้าตัวในวันเดียวคือ coordinated push. signal ว่า agent stack ทั้งชุดพร้อมแล้ว.

หัวใจของรอบนี้คือ Computer Use. feature ที่ Anthropic เปิด preview ตั้งแต่ตุลา สองพันยี่สิบสี่. ใช้เวลาหนึ่งปีสิบเดือนในการ productionize. toolset ใหม่มาพร้อม batch actions. agent execute หลาย action ใน one turn แทน round trip ทุก step. latency ต่อ workflow ลดสามถึงห้าเท่า.

Browser Use เป็น tool ใหม่คนละตัวกับ Computer Use ไม่ใช่ rename. driver browser ที่ app ของคุณ host เอง. อ่าน accessibility tree. set form values ตรงเข้า DOM. เร็วและ reliable กว่าสำหรับ web only workflow. Computer Use ยังจำเป็นสำหรับ desktop app.

Files API ให้ upload file objects พร้อม expiration pagination filter. Agent Skills เป็น named versioned skill packages. agent เรียกเป็น first class primitive. ไม่ต้อง prompt engineer ซ้ำทุกครั้ง. Skills API เปิดให้ enterprise สร้าง private skill registry ของบริษัท. Admin API จัดการ members invites groups custom roles.

Anthropic beta header ไม่ต้องส่งแล้วสำหรับทั้งห้าตัว. spec ล็อค. billing tier ผ่าน enterprise procurement review.

Pattern ชัด. frontier lab เปลี่ยน stance จาก model provider เป็น agent platform provider. หนึ่งปีก่อน Anthropic ขาย API. วันนี้ขาย agent runtime tool ecosystem skill registry enterprise identity ครบ stack.

จุดเปรียบ vs OpenAI. Assistants API v2 มี Function Calling Code Interpreter File Search Retrieval คล้ายกัน. แต่ยังไม่มี native computer control tool ที่ GA. Operator ยัง preview. Anthropic productionize สำเร็จก่อน. competitive moat จริงสำหรับ workflow ที่ต้อง interact กับ legacy desktop app.

ecosystem signal. timing สิบเก้าสิงหา ก่อน A2A ย้ายไป AAIF ยี่สิบสิงหา. ไม่ใช่บังเอิญ. Anthropic push agent stack ให้ production ready ก่อน. วันรุ่งขึ้น protocol layer ย้ายบ้าน. ข้อความชัด. MCP กับ A2A เป็น standards. Claude เป็น reference implementation ที่ enterprise grade แล้ว.

สำหรับ builders. ลบ Anthropic beta header ห้าตัวได้เลย. เปลี่ยนไปใช้ Skills API เก็บ skill เป็น versioned artifact. ประหยัด token สี่สิบถึงหกสิบ percent ต่อ conversation.

สำหรับ enterprise. Compliance officer ที่ block เพราะ still beta ต้องยอมแล้ว. Thai enterprise ธนาคาร ประกัน โรงพยาบาล ที่รอ SLA backed Computer Use. จังหวะเริ่มโครงการคือตอนนี้.

สำหรับ OpenBridge. ถ้า orchestrate multi vendor agents. plan ให้ Computer Use route ไป Claude by default. Text only reasoning ยัง multi vendor ได้ตามราคา latency
