---
date: 2026-10-15
slug: google-gemini-agent-workspace-identity
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  A corporate office directory wall at night with glowing name plates, three
  rows: "ALEX CHEN — PM", "SARAH LIU — DESIGNER", and a third plate glowing
  cyan labeled "GEMINI AGENT — COWORKER" with a tiny Google logo. A speech
  bubble next to it shows a tiny Gmail icon, Calendar icon, and Drive icon.
  Big block text at the top reads "7-DAY RUNS" and bottom reads "OWN IDENTITY".
  Editorial flat illustration, dark navy with cyan accent, high contrast,
  1:1 aspect, no real human faces (silhouettes only).
image: images/26-10-15-0616-02-google-gemini-agent-workspace-identity.png
---

# Google ให้ AI agent มี Gmail กับโต๊ะทำงานของตัวเอง — รันงานยาว 7 วัน

## TL;DR
- Google Cloud เปิดตัว Gemini Agent เป็น universal enterprise agent ที่มี Workspace identity ของตัวเอง (Gmail, Calendar, Drive, ชื่อใน directory) และรันงานต่อเนื่องได้นาน 7 วัน
- Multi-model ตั้งแต่วันแรก — route ไป Anthropic Claude ได้ตรง ๆ นอกจาก Gemini, มี session + semantic + procedural + episodic memory, spin sub-agents ได้
- Signal ชัด: การขายของเปลี่ยนจาก "agent คือ feature ใน app ของเรา" เป็น "agent คือ coworker ที่มีบัญชีของตัวเอง" — vendor lock-in กำลังย้ายจาก model ไปอยู่ที่ identity layer

## เกิดอะไรขึ้น
Google Cloud ประกาศ Gemini Agent ในงาน Gemini at Work (8 ต.ค. 2026) — ต่างจาก agent รุ่นก่อนตรงที่เป็น "coworker" ที่มีบัญชี Workspace ของตัวเอง. เมื่อ admin สร้าง agent หนึ่งตัว ระบบจะออก email address, calendar, Drive folder, และ entry ใน company directory ให้ — เพื่อนร่วมงานสามารถ @mention ชื่อ agent ใน Google Docs ได้ แล้วเห็น edit ของมันใน version history เหมือน collaborator คนอื่น

Runtime ของ job เดียวยาวได้ 7 วัน — ปิด laptop ได้ไม่ขาด. ข้างในมี 4 ชั้นของ memory (session, semantic, procedural, episodic) และ agent สามารถ spin sub-agent ชั่วคราวที่มี identity แยกเป็นของตัวเอง เพื่อแตก task เป็น parallel หรือ sequential steps. Google ย้ำว่า agent "acts under its own identity rather than yours" — แปลคือ ถ้ามันทำพลาด audit trail ชี้มาที่ agent ไม่ชี้มาที่คุณ (ประเด็น compliance ที่ enterprise อยากได้ยินมานาน)

เรื่อง model ที่น่าสนใจคือ Google ไม่พยายามล็อกให้ใช้ Gemini อย่างเดียว — press briefing บอกชัดว่า agent route ไป Anthropic Claude ก็ได้ (รวมถึง model อื่น). Governance ชุดใหญ่: per-agent cryptographically attested identity, sandboxed tasks, audit trail attributed to the agent, และ hard per-project AI spend caps ตั้งใน Cloud Billing ตรง ๆ

สิ่งที่ยังไม่ประกาศ: GA date, pricing แยกจาก Gemini Enterprise subscription, และ benchmark ที่ 3rd party ยืนยัน. ตอนนี้ coworker mode อยู่ใน private preview — ลูกค้าทั่วไปยังเข้าไม่ได้

## ทำไมสำคัญ
ก่อนหน้านี้คำว่า "AI agent in Workspace" คือ sidebar ที่ช่วย summarize หรือ draft — แปลง่าย ๆ คือ feature ของ app. การให้ agent มี Gmail กับ directory entry ของตัวเองเปลี่ยน mental model ของ enterprise IT ไปอย่างสิ้นเชิง — มันกลายเป็น "principal" ที่ provision ด้วย HR process ปกติ, มี compliance owner, มี cost center, มี offboarding playbook. นี่คือ enterprise shape ที่ CIO กับ CISO เข้าใจและซื้อได้ ซึ่ง sidebar agent ไม่เคยทำได้

Pattern ที่ชัดคือ "agent as coworker" กำลังชนะ "agent as feature" ในวงการ enterprise. OpenAI ปล่อย Dots ที่เป็น always-on agent ก่อนหน้านี้ไม่กี่สัปดาห์, Workday เพิ่งเปิด headless Agent System User, Google ตอนนี้ให้ agent มี Workspace identity เต็มรูปแบบ. ทุกเจ้าตีไปที่โจทย์เดียวกัน — agent ที่คน audit ได้, assign budget ได้, @mention ได้, และยัง route ไปใช้ model หลายเจ้าได้

ความ sophisticated ของ Google อยู่ที่การยอม route ไป Claude ตั้งแต่วันแรก — เป็นการบอก enterprise ว่า "เราไม่บังคับให้คุณใช้ Gemini อย่างเดียว ตราบใดที่ยังเป็น coworker ใน Workspace ของเรา". vendor lock-in กำลังย้ายจาก model layer ไปอยู่ที่ identity + governance layer — ที่ซึ่ง switching cost สูงกว่ามาก

## มุม AI Agent Platform
- **Builders**: ถ้าคุณกำลังสร้าง agent framework หรือ orchestration layer ของตัวเอง — Google เพิ่งตั้ง bar ของ enterprise expectation ไว้สูงมาก (own identity, 7-day runs, cross-model routing, cryptographic attestation, spend caps). ขายต่อ CIO ที่คุ้นกับ Workspace จะยากขึ้นถ้าของคุณยังเป็น stateless agent รัน sandbox
- **Users / Business**: บริษัทที่อยู่บน Workspace อยู่แล้ว ภายใน 2-3 ไตรมาสจะมีคนในทีมเริ่ม request ให้ provision "Gemini coworker" — HR + IT ต้องเตรียม policy ล่วงหน้า โดยเฉพาะ offboarding (agent ยัง active กี่ตัว, ใครเป็น owner)
- **Ecosystem**: Microsoft Copilot ต้องตอบเร็ว — เค้ามี Entra ID + M365 Admin + Teams อยู่แล้ว ยังขาด "coworker agent with email address". ส่วน Slack/Notion ที่ไม่มี identity backbone จะต้องตัดสินใจระหว่างสร้างเองหรือ outsource ให้ Okta/Auth0

## Sources
- [Google Cloud unveils persistent Gemini Agents for long-running tasks — VentureBeat (via OODA loop)](https://oodaloop.com/briefs/technology/google-cloud-unveils-persistent-gemini-agents-for-long-running-tasks/)
- [Google Cloud Launches Gemini Agent, One Universal Agent for Enterprise Work — MarkTechPost](https://www.marktechpost.com/2026/10/08/google-cloud-launches-gemini-agent-one-universal-agent-for-enterprise-work/)
- [Google Introduces a Gemini Agent Designed to Work Across Apps for Days — Superpower Daily](https://superpowerdaily.com/posts/google-introduces-a-gemini-agent-designed-to-work-across-apps-for-days)
- [Google Cloud's Gemini Agent Gets a Mailbox and Directory Seat — AIWeekly](https://aiweekly.co/alerts/google-clouds-gemini-agent-gets-a-mailbox-and-directory-seat)

---

## Audio script
วันนี้มาคุยเรื่อง Google Cloud ที่เพิ่งปล่อย Gemini Agent — เป็น enterprise agent ที่เปลี่ยนเกมเลย. จุดที่ต่างจากเดิมคือ agent แต่ละตัวจะมี Workspace identity ของตัวเอง — คือ มี Gmail address, มี Calendar, มี Drive folder, มีชื่อใน company directory เหมือนพนักงานปกติ. เพื่อนร่วมงานสามารถ at-mention ชื่อ agent ใน Google Docs ได้แล้วเห็น edit ของมันใน version history. งานยาวได้ 7 วัน — ปิด laptop แล้วมันก็รันต่อ. ข้างในมี 4 ชั้น memory และ agent spin sub-agent ได้ด้วย identity แยกกัน. ที่น่าสนใจกว่าคือ Google ไม่ล็อกให้ใช้ Gemini อย่างเดียว — route ไป Anthropic Claude ได้ตั้งแต่วันแรก. Signal ที่ชัดคือ enterprise กำลังเปลี่ยน mental model จาก agent as feature ไปเป็น agent as coworker — คือเป็น principal ที่ IT ต้อง provision, มี compliance owner, มี offboarding playbook. และ vendor lock-in กำลังย้ายจาก model layer ไปอยู่ที่ identity กับ governance layer ที่ switching cost สูงกว่ามาก. ถ้าคุณเป็น CIO ที่อยู่บน Workspace สองสามไตรมาสข้างหน้าทีมคุณจะเริ่มขอ provision Gemini coworker แน่นอน — HR กับ IT เตรียม policy ล่วงหน้าดีกว่าตามไล่
