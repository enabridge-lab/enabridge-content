---
date: 2026-07-10
slug: anthropic-claude-cowork-mobile-web-cloud-background
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  A wide editorial isometric scene: a laptop labeled "CLAUDE COWORK" glowing on
  an office desk, its screen closed while a giant translucent Claude agent
  keeps working in the cloud above it — a big billboard reads "AGENT STILL
  RUNNING". In the foreground, a silhouette on a train checking a phone
  labeled "CLAUDE COWORK MOBILE" that shows an approval dialog: "APPROVE?".
  Two bold stat panels on the side: "91.3% NON-DEV WORK" and "33.4% BIZ OPS".
  Cinematic warm lighting, high contrast, 1:1 aspect, readable at 200px
  thumbnail, no real human faces.
image: images/26-07-10-0608-02-anthropic-claude-cowork-mobile-web-cloud-background.png
---

# Anthropic ยก Claude Cowork ขึ้น mobile + web พร้อม cloud background — agent เปลี่ยนจาก "app ที่เปิดไว้" เป็น "coworker ที่ทำงานเงียบ ๆ แล้วส่ง notification"

## TL;DR
- Anthropic ปล่อย **Claude Cowork บน mobile (iOS/Android) + web** สำหรับ Max subscriber (7-8 ก.ค.) — เดิม limit อยู่แค่ macOS/Windows desktop app ที่ launch เดือน ม.ค. 2026
- **Task ย้ายไป cloud** — user สั่งงานจาก desktop, ปิด laptop, ดู status จากมือถือ, approve บนรถไฟ, เก็บผลลัพธ์ที่บ้าน. Anthropic เรียก pattern นี้ว่า **"agent as background coworker"** — user ให้ goal, Claude plan, ใช้ tool, ถามคำถามที่เฉพาะคนตอบได้ผ่าน push notification
- ตัวเลขที่ Anthropic ปล่อย: **91.3% ของ session ไม่เกี่ยวกับ software dev เลย**; category ใหญ่สุด **33.4% = Business Process & Operations** (รวม status report, onboarding checklist, spreadsheet reconciliation) — signal ว่า agent-based work ในองค์กรกำลังจะ mainstream แบบไม่ต้อง IT tag along

## เกิดอะไรขึ้น
วันอังคารที่ 7 ก.ค. Anthropic ประกาศ Claude Cowork ขยายจาก desktop app เข้า mobile + web สำหรับ Max subscriber (later paid tier ตามใน "coming weeks"). **การเปลี่ยนแปลงจริงไม่ใช่แค่ platform** — สถาปัตยกรรมของ agent หลังบ้านถูกยกไปรัน **cloud-based background execution** ทั้งหมด. Claude รับ goal, plan งาน, ใช้ tool (browser, terminal, MCP tool, doc/sheet/slide generator), และเวลาถึงจุดที่ต้อง approval จากคน — ยิง push notification ไปมือถือ. **User review + approve แล้ว agent ทำต่อ**

Anthropic ให้ประเด็นใน UX ตัวใหม่ 3 อย่าง: (1) **task persistence** — เริ่มจาก desk, ปิด laptop, agent ยังรันต่อใน cloud, ผลลัพธ์รอที่ mobile หรือ web; (2) **approval gate on mobile** — เวลา agent ต้องการ input (เช่น "จะส่ง email นี้ไหม" หรือ "จะ commit code นี้ไหม") user approve จากที่ไหนก็ได้; (3) **output artifact** — เอกสาร, spreadsheet, presentation, report generate เสร็จเก็บใน Cowork workspace, share ต่อได้เลย

ข้อมูลที่ Anthropic ปล่อยพร้อม launch (ประเมินจาก sample sessions) เปลี่ยน narrative ของ AI agent ทั้ง industry — **91.3% ของ Cowork session ไม่เกี่ยวกับ software dev**. Category ใหญ่สุด **33.4% = Business Process & Operations** — เช่น "รวม update จากทีมทั้ง 5 ทีมมาเขียน report สรุปสัปดาห์" หรือ "สร้าง onboarding checklist สำหรับ role นี้" หรือ "reconcile 3 spreadsheet ที่หน่วยงานต่างส่งมา"

## ทำไมสำคัญ
Pattern shift ที่ Anthropic capture ได้แม่นสุดคือ **"agent = คนทำงานที่ไม่ต้องอยู่หน้าจอ"**. เดิมทีสิ่งที่ user คาดจาก AI คือ chat interface — พิมพ์คำถาม, รอตอบ, พิมพ์ต่อ. Claude Cowork mobile เปลี่ยน pattern เป็น **task-based interaction** — สั่ง goal แล้วเดินไปประชุมได้เลย, กลับมาดูผลตอน 15:00. ตัว UX pattern นี้เดินตาม Devin (Cognition), OpenAI Codex Cloud, Google Jules ที่ทดลองมาก่อน — **แต่ Anthropic ทำให้เข้าถึงง่ายที่สุด**: ไม่ต้องเป็น developer, ไม่ต้อง setup, ใช้ mobile app ที่ปุ่ม approve ปุ่มเดียว

91.3% non-dev + 33.4% BizOps เป็น **signal ที่ Salesforce/Microsoft ต้อง reconsider positioning ทันที** — เพราะพวกเขา sell "AI สำหรับ knowledge worker" ผ่าน SaaS suite (Agentforce, Copilot in Word/Excel) แต่ user จริง ๆ ใช้ Claude Cowork ทำ **workflow ที่ SaaS suite แตะไม่ถึง** — งาน ad-hoc, งาน cross-application, งาน reconciliation ระหว่างเอกสารกับ Slack กับ email. Cowork ไม่ต้อง integrate อะไร, Claude ทำผ่าน browser/desktop/mobile ของ user เอง

การขึ้น mobile ยัง unlock **use case ใหม่ทั้งชั้น** ที่ desktop app ไม่มีทางทำ — CEO/CFO/manager ที่ 60-70% ของเวลาไม่อยู่หน้า laptop (ประชุม, ลงพื้นที่, edinburgh trip) สามารถ delegate งานให้ Claude ระหว่างเดินทางแล้ว review กลับมา. **B2B SaaS ที่วางตัวเองว่าเป็น "app ที่ CEO เปิด" (Notion, Airtable, Monday, Asana) จะโดน bypass** — งาน CEO ที่ต้องดึงข้อมูลจากพวกนั้นให้ Claude ทำได้เลย

Compare กับ ChatGPT Workspace Agents ที่ launch เมื่อ 24 เม.ย. — OpenAI เดินสูตร **"workspace as app store"** (Slack agent, Salesforce agent, Google Drive agent เชื่อมเข้ามาใน ChatGPT); Anthropic เดินสูตร **"agent as OS-level coworker"** ทำงานผ่าน mobile + web + desktop ในตัวเดียว. สองสูตรจะแบ่ง user attention กัน — knowledge worker ที่มี integration หนักไป OpenAI; user ทั่วไปที่แค่อยาก "ให้ agent ทำแทน" ไป Anthropic

## มุม AI Agent Platform
**Builders** — agent framework builder ที่ยังคิดว่า agent runtime = long-running server process บน user's machine ต้อง revisit สถาปัตยกรรม; user จริง ๆ ต้องการ **cloud-hosted agent runtime + mobile approval UI**. LangGraph Cloud, Vercel AI SDK Cloud, Modal-based agent hosting มี tailwind. UI kit builder ที่ทำ mobile approval flow (push notification + swipe approve + inline edit) จะเป็น layer ใหม่ที่ Google/OpenAI/Anthropic ทุกเจ้าต้องมี

**Users/business** — pattern "agent as background coworker" เปลี่ยนวิธีวัด productivity — เดิมวัดที่ "user active time on app"; ตอนนี้วัดที่ **"agent-hours delegated + approval rate"**. หัวหน้าธุรกิจในไทยที่มีทีม operations 20-50 คน (finance ops, marketing ops, HR ops) ควร pilot Cowork 1-2 role ในเดือนสิงหาคม-กันยายน — คนที่ทำ report สรุปสัปดาห์, reconcile spreadsheet, onboarding checklist. ROI วัดเร็วที่สุดใน 30 วัน

**Ecosystem** — mobile push notification provider (Firebase, OneSignal, Twilio) เข้าเป็น dependency ใหม่ของ agent runtime; ผู้ให้บริการ authentication (Auth0, Clerk, WorkOS) ที่รองรับ mobile approval + biometric confirm มี window. **CIO/CISO ในไทย** ต้องเริ่มคิดเรื่อง **approval policy บน mobile** — ไม่ใช่แค่ "ใครเปิด app ได้" แต่ "agent สั่งอะไรได้บ้างเมื่อ user approve จาก mobile" — จะเป็น line item ใหม่ใน AI governance framework ที่ CISO ต้องเขียนภายในไตรมาสถัดไป

## Sources
- [Claude Cowork expands to mobile and web — TechCrunch](https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/)
- [Anthropic's Claude Cowork now keeps working when you close your laptop — The New Stack](https://thenewstack.io/claude-cowork-cloud-mobile/)
- [Claude Cowork turns your phone into a remote control for AI work — Help Net Security](https://www.helpnetsecurity.com/2026/07/08/claude-cowork-phone-mobile-web/)
- [Anthropic Launches Mobile Access for Claude Cowork — PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/anthropic-launches-mobile-access-for-claude-cowork/)

---

## Audio script
Anthropic ประกาศเมื่อวันอังคารที่ 7 กรกฎาคม ปล่อย Claude Cowork ขึ้น mobile และ web สำหรับ Max subscriber เดิมทีอยู่แค่ desktop app บน Mac กับ Windows ตั้งแต่เดือนมกราคม สิ่งที่เปลี่ยนจริง ๆ ไม่ใช่แค่ platform แต่คือสถาปัตยกรรม agent ย้ายไปรันใน cloud หลังบ้านทั้งหมด user สั่งงานจาก desk ปิด laptop เดินไปประชุม agent ยังทำงานต่อใน cloud เวลาถึงจุดที่ต้อง approval agent ยิง push notification ไปมือถือ user กด approve แล้วมันทำต่อ พอเสร็จก็มี report สปreadsheet หรือ presentation รอที่ workspace ตัวเลขที่ Anthropic ปล่อยพร้อม launch สั่นสะเทือน 91.3 เปอร์เซ็นต์ของ session ไม่เกี่ยวกับ coding เลย category ใหญ่สุด 33.4 เปอร์เซ็นต์คืองาน Business Process และ Operations เช่นรวม update จากทีมทั้ง 5 ทีมมาเขียน report สร้าง onboarding checklist reconcile spreadsheet ที่หลายหน่วยส่งมา นี่คือ pattern shift สำคัญ agent ไม่ใช่ chat interface อีกแล้ว agent คือ coworker ที่ทำงานเงียบ ๆ ระหว่างที่คุณประชุมหรือเดินทาง สำหรับหัวหน้าธุรกิจในไทยที่มีทีม operations 20 ถึง 50 คน ลอง pilot Cowork กับ 1 หรือ 2 role ในเดือนสิงหาคมกันยายน คนที่ทำ report สปุปดาห์ reconcile spreadsheet onboarding checklist ROI วัดได้เร็วที่สุดใน 30 วัน สำหรับ CISO นี่คือ line item ใหม่ที่ต้องเขียน approval policy บน mobile ไม่ใช่แค่ใครเปิด app ได้ แต่ agent สั่งอะไรได้บ้างเมื่อ user approve จากมือถือ
