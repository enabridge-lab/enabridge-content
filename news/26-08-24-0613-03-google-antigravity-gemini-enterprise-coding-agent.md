---
date: 2026-08-23
slug: google-antigravity-gemini-enterprise-coding-agent
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  A wide editorial isometric illustration of the Google Antigravity spaceship
  labeled "ANTIGRAVITY" landing on a corporate rooftop platform stamped
  "GEMINI ENTERPRISE". Four docking arms extend out with tagged badges:
  "VS CODE", "VS", "JETBRAINS", "ZED". A big admin console dashboard on the
  side glows with rows labeled "BUDGET", "AUDIT LOG", "WORKFORCE ID FED",
  "SANDBOX". A small robot agent silhouette walks up a boarding ramp holding
  a spec doc. Sharp navy and deep-teal palette with amber accent lighting;
  chunky sans-serif labels readable at 200px thumbnail; 1:1 aspect ratio; no
  real human faces.
image: images/26-08-24-0613-03-google-antigravity-gemini-enterprise-coding-agent.png
---

# Google Antigravity เข้า Gemini Enterprise — coding agent เดินไปหา admin console

## TL;DR
- 20 ส.ค. Google ประกาศ bundle **Antigravity** เข้า Gemini Enterprise Standard / Plus / Standard Emerging Market โดย admin เปิด/ปิดจาก Enterprise admin console ได้ตรง
- IDE extension ใหม่: VS Code (GA), Visual Studio / JetBrains / Zed (preview), พร้อม Antigravity 2.0 desktop + CLI — "coding agent หลุดออกจาก IDE ของตัวเอง" ไปอยู่ที่ dev ทำงานอยู่จริง
- รองรับ Workforce Identity Federation + Application Default Credentials, admin ตั้ง budget threshold, จำกัด browser permission, sandbox workspace, audit log — enterprise-first ตั้งแต่ day 1

## เกิดอะไรขึ้น
วันที่ 20 ส.ค. Google Cloud ประกาศว่า Antigravity — coding agent platform ที่ Google เปิดตัวช่วง I/O 2026 (พฤษภาคม) — พร้อมใช้เป็นส่วนหนึ่งของ Gemini Enterprise subscription ทุก tier ที่รองรับ (Standard, Plus, Standard Emerging Market) โดย IT admin สามารถ enable ให้ user, monitor spend, ตั้ง policy จาก Gemini Enterprise admin console เดียวกัน

Feature ที่มากับ launch นี้: Antigravity หลุดจาก IDE ของตัวเอง ไปอยู่บน **VS Code (GA), Visual Studio (preview), JetBrains (preview), Zed (preview)** พร้อม Antigravity 2.0 desktop app + Antigravity CLI. Google ยอมรับตรง ๆ ว่าคนไม่ย้าย IDE ไปหา coding agent — coding agent ต้องย้ายไปหาคน

Enterprise control ที่ Google ใส่มาแบบ default: (1) Workforce Identity Federation + Application Default Credentials — agent ยืม identity ของ workforce IdP ที่ enterprise ใช้อยู่ ไม่ต้องออก secret แยก (2) admin ตั้ง monthly budget threshold ต่อ user / team (3) จำกัด browser permission และ workspace sandbox ที่ agent เข้าถึงได้ (4) audit log ครบทุก tool call, ทุก file edit, ทุก network request

## ทำไมสำคัญ
เกม coding agent ปีนี้ชัดว่าไม่ได้แข่งที่ "code เก่งกว่า" อย่างเดียว — Cursor, Windsurf, Devin, Copilot, Claude Code, Codex, Antigravity ทุกเจ้าออกโมเดล + tool call ที่ใกล้เคียงกัน เกมจริงคือ **ใครกลายเป็น default ของ enterprise IT** ที่มี procurement, compliance, budget, audit ครบมือ — และ Google เดินเกม vertical integration ที่ Microsoft ทำมาก่อนกับ Copilot / Azure AD / Purview

จุดที่ Google ได้เปรียบเฉพาะคือ **Workforce Identity Federation** — enterprise ที่มี Okta, Ping, Entra, Google Workspace อยู่แล้ว เปิด agent ได้โดยไม่ต้องออก long-lived API key ใหม่ pattern เดียวกับที่ MCP roadmap 2026 push ให้เป็น standard สำหรับ agent identity Google เอา pattern นี้มาใช้ก่อนที่ spec จะ finalize ในระดับ ecosystem

จังหวะที่ Antigravity เข้า Gemini Enterprise พร้อม Deloitte report บอกว่ามีแค่ 20% ขององค์กรที่พร้อมรับ agent — บอกว่าเรากำลังเข้า phase 3 ของ coding agent: "framework wars จบ, distribution war เริ่ม" ใครมีช่องทางกระจายที่ครอบ Fortune 2000 ครบทั้ง license + admin + support ในสัญญาเดียว จะกินตลาด mass market

## มุม AI Agent Platform
สำหรับ **builders** ที่ทำ coding agent / dev tool: ถ้ายังไม่ใช่ enterprise-first — เวลาไม่เยอะแล้ว feature ที่จำเป็น: admin console, SSO/Workforce IdP, spend control, audit log, sandbox — ทุกอย่างนี้เป็น minimum bar ในการเข้าถึง buyer เหนือระดับ SMB สัญญาณตลาดชัดว่า "IDE plugin" อย่างเดียวไม่พอ ต้อง speak enterprise IT language

สำหรับ **users/business** (CIO, IT platform lead): ประเมิน coding agent stack ใหม่ — ถ้ามี Gemini Enterprise subscription อยู่แล้ว การ enable Antigravity ตอนนี้ = zero incremental license cost (bundle in) + control ผ่าน console เดียวกันกับ Workspace เทียบกับการต่อสัญญาแยกกับ Cursor / Devin / GitHub Copilot ที่ต้องมี admin plane ของแต่ละเจ้า — วางแผน RFP รอบใหม่ให้ include bundle economics ด้วย

สำหรับ **ecosystem** (IDE vendor, dev tool, IdP): เป็นเวลาของ compression margin — coding agent จะกลายเป็น feature ของ productivity suite (Microsoft 365, Google Workspace, Workday, ServiceNow) ผู้เล่น standalone จะต้องพิสูจน์ ROI ที่วัดได้เหนือกว่า bundle 2-3 เท่า. สำหรับ Enabridge — pattern ที่ Google + Microsoft + Anthropic เดินให้เห็น: enterprise agent platform ต้องมาพร้อม admin plane ที่ IT ใช้จริง (budget, audit, identity federation, policy) เป็น first-class feature — ไม่ใช่ทำเป็น "add-on module" ที่ปล่อยหลัง product

## Sources
- [Expanding Google Antigravity for enterprise customers — Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/expanding-google-antigravity-for-enterprise-customers)
- [Google's AI coding agent just escaped its own IDE — The New Stack](https://thenewstack.io/google-antigravity-ide-extensions/)
- [Google tethers Antigravity to enterprise controls amid AI shakeup — The Register (Aug 21, 2026)](https://www.theregister.com/ai-and-ml/2026/08/21/google-tethers-antigravity-to-enterprise-controls-amid-ai-shakeup/5290730)
- [Google bundles Antigravity coding agents into Gemini Enterprise — Investing.com](https://www.investing.com/news/stock-market-news/google-bundles-antigravity-coding-agents-into-gemini-enterprise-93CH-4870301)

---

## Audio script
วันที่ 20 สิงหาคม Google ประกาศ bundle Antigravity ซึ่งเป็น coding agent ของตัวเองเข้ากับ Gemini Enterprise subscription ทุก tier ที่รองรับ ครับ

IT admin สามารถ enable Antigravity ให้ user, monitor spend, ตั้ง policy จาก admin console เดียวกับ Gemini Enterprise ได้เลย และ Antigravity หลุดออกจาก IDE ของตัวเอง ไปอยู่บน VS Code, Visual Studio, JetBrains, Zed พร้อม desktop app และ CLI — Google ยอมรับตรง ๆ ว่าคนไม่ย้าย IDE ไปหา coding agent

Feature enterprise ที่ใส่มาแบบ default คือ Workforce Identity Federation ให้ agent ยืม identity จาก Okta หรือ Entra ที่มีอยู่ ไม่ต้องออก secret แยก, admin ตั้ง budget threshold ต่อ user, จำกัด browser permission และ workspace sandbox พร้อม audit log ครบ

Signal คือ framework wars จบไปแล้ว distribution war เริ่มขึ้น ใครมีช่องทางกระจายที่ครอบ Fortune 2000 ครบทั้ง license, admin, support ในสัญญาเดียว จะกินตลาด mass

ถ้าองค์กรมี Gemini Enterprise อยู่แล้ว เปิด Antigravity ตอนนี้ = zero incremental cost วางแผน RFP รอบใหม่ให้ include bundle economics ด้วยครับ
