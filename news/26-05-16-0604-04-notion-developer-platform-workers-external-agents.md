---
date: 2026-05-16
slug: notion-developer-platform-workers-external-agents
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  A futuristic open warehouse loading dock labeled "NOTION" as the control hub,
  with multiple AI agent characters arriving from different doors labeled
  "CLAUDE", "CODEX", "DECAGON", "GEMINI". In the center, a glowing conveyor belt
  with "Workers" engraved on metal plates carrying database icons (Zendesk,
  Salesforce, Postgres). A large bold floating text reads "External Agents API ·
  Aug 11". Composition: wide hero shot, warm yellow Notion-brand interior light
  against cool blue exterior, cinematic depth. Style: editorial 3D isometric
  illustration, high contrast for thumbnail legibility, no human faces.
image: images/26-05-16-0604-04-notion-developer-platform-workers-external-agents.png
---

# Notion เปิด Developer Platform — Workers + External Agents API กลายเป็น "control room" ให้ agent ทำงานข้ามระบบ

## TL;DR
- **13 พ.ค. 2026** — Notion 3.5 เปิดตัว Developer Platform: Workers (hosted code runtime), External Agents API, database sync ทั้งหมดในก้อนเดียว
- Partner agent วันแรก: **Claude, OpenAI Codex, Decagon** — work out of the box ภายใน workspace
- Workers free ช่วง beta, **เริ่มคิด Notion credits 11 ส.ค. 2026**; deploy/manage จำกัด Business + Enterprise tier

## เกิดอะไรขึ้น

วันที่ 13 พ.ค. Notion ปล่อย release 3.5 พร้อมประกาศใหญ่ที่สุดในรอบหลายปี — **Notion Developer Platform** ที่เปลี่ยน workspace ให้กลายเป็น runtime สำหรับ AI agent. มี 3 ชิ้นหลัก: (1) **Notion Workers** — hosted code runtime, ผู้ใช้ (หรือ coding agent ของผู้ใช้) เขียน code, deploy ผ่าน CLI, รันใน sandbox; Worker รับ webhook ทำ logic แล้ว action กลับเข้า Notion หรือเรียก external API. (2) **External Agents API** — partner agent อย่าง Claude, Codex, Decagon และอื่น ๆ ทำงานใน workspace ของ Notion ได้ทันที. (3) **Database sync** — ดึง data จาก system of record ที่มี API (Zendesk, Salesforce, Postgres, ฯลฯ) เข้า Notion database และอัพเดทอัตโนมัติ.

ตัวอย่างที่ Notion ยกมาบน blog post: Worker รัน webhook ที่ปิด task ใน Notion เมื่อ PR merge บน GitHub, อัพเดท CRM เมื่อ subscription เปลี่ยน, สร้าง onboarding doc เมื่อ offer letter เซ็น. ทั้งหมดนี้คือ workflow ที่ก่อนหน้านี้ต้องใช้ Zapier / Make / n8n เป็นชั้นกลาง — ตอนนี้ Notion เก็บไว้เอง.

โมเดล pricing น่าสนใจ: **CLI ใช้ได้ทุก tier** — ทำให้ developer ลองได้แม้บน free workspace. แต่การ deploy + manage Workers จริง ๆ จำกัดเฉพาะ Business / Enterprise. Workers ฟรีในช่วง beta จนถึง 10 ส.ค. แล้วเริ่มคิด **Notion credits** วันที่ 11 ส.ค. — น่าสนใจที่ Notion เลือก credit-based แบบเดียวกับที่ Anthropic เพิ่งประกาศใช้กับ Claude Agent SDK วันก่อนหน้า. pattern เดียวกันชัด ๆ — token economy.

## ทำไมสำคัญ

Notion กำลังเดิมพันว่ามันจะกลายเป็น **agent control room** — ที่ที่ human review งาน, ที่ที่ agent หลายตัวมาเจอกัน, ที่ที่ data sync กลับมา. คู่แข่งโดยตรงไม่ใช่ Confluence หรือ Coda แต่เป็น **Zapier และ Make.com** — สอง integration platform ที่ครอง workflow automation มาตลอด 10 ปี. ถ้า Notion ทำได้ดี ความได้เปรียบคือ data อยู่ใน workspace อยู่แล้ว — ไม่ต้อง map field, ไม่ต้อง schedule pull, agent อ่าน Notion page ก็จบ.

จุดที่อ่อน: Workers ตอน launch ยัง compute-limited (sandbox เล็ก ๆ ไม่ใช่ Lambda full), Notion ไม่ใช่ developer platform โดยกำเนิด, ecosystem ของ template / library ยังเล็ก. แต่ทาง partner stack เลือกมาดี — Claude, Codex, Decagon คือ 3 agent ที่นัก enterprise ใช้จริง. การที่ "out of the box" หมายความว่าไม่ต้อง config OAuth, ไม่ต้อง expose webhook URL — แค่เลือก agent กดเปิด ก็ทำงาน. compatibility-as-a-feature เป็น move ที่ Zapier ใช้ชนะมาตั้งแต่ปี 2014.

สัญญาณกว้างกว่า: **"agentic workspace"** กำลังจะเป็น new category. Notion ทำ control plane, Slack ขยับเป็น notification + approval layer, Salesforce / SAP / ServiceNow ขยับเป็น system of record ของ agent. แต่ middle layer — integration + orchestration — ยัง up for grabs.

## มุม OpenBridge

นี่คือข่าวที่ **ใกล้ตัว OpenBridge ที่สุดในรอบนี้**. Notion Workers + External Agents API เป็น direct competitor กับ value prop ของ integration platform — ดึง data จาก Salesforce / Zendesk เข้า Notion อัตโนมัติคือสิ่งที่ลูกค้า OpenBridge หลายเจ้าซื้อมาทำ. คำถามที่ต้องตอบในที่ประชุมสัปดาห์หน้า: (1) ลูกค้าของเราที่ใช้ Notion อยู่ จะอยู่กับเราหรือย้ายไปใช้ Notion Workers? — น่าจะแบ่งเป็น "Notion-heavy" จะย้าย, "multi-tool" จะอยู่. (2) เรามี integration กับ Notion ที่ลูกค้าใหม่จะใช้ได้ทันทีไหม? ถ้ายัง — สร้างก่อน Q3 ก่อน Notion lock developer audience.

มุมที่ปลอดภัยกว่า: OpenBridge ทำ depth ใน B2B connector ที่ Notion จะไม่ทำ (เช่น Thai banking API, regional ERP, SaaS เฉพาะกลุ่ม) — แล้ว expose ผ่าน MCP server / Notion External Agent ให้ Workers เรียกได้. **เป็น "data plane" ให้ Notion เป็น "control plane"** ดีกว่าแข่งกันตรง ๆ.

## Sources
- [Introducing Notion's Developer Platform — Notion Blog](https://www.notion.com/blog/introducing-developer-platform)
- [May 13, 2026 – 3.5: Notion Developer Platform — Notion Releases](https://www.notion.com/releases/2026-05-13)
- [Notion just turned its workspace into a hub for AI agents — TechCrunch](https://techcrunch.com/2026/05/13/notion-just-turned-its-workspace-into-a-hub-for-ai-agents/)
- [Notion Launches Developer Platform For AI Workflows And Agents — Dataconomy](https://dataconomy.com/2026/05/14/notion-launches-developer-platform-for-ai-workflows-and-agents/)

---

## Audio script
ข่าวสุดท้ายของวันนี้ ใกล้ตัวเราที่สุด — Notion ปล่อย 3.5 วันที่ 13 พฤษภาคม พร้อม Developer Platform ใหญ่. มีสามชิ้น Workers ที่เป็น hosted code runtime ผู้ใช้หรือ coding agent ของผู้ใช้เขียน code deploy ผ่าน CLI รันใน sandbox รับ webhook ทำ logic แล้ว action กลับ Notion หรือเรียก external API. ชิ้นที่สอง External Agents API พาร์ทเนอร์วันแรกคือ Claude OpenAI Codex Decagon ทำงานใน workspace ได้ทันที. ชิ้นที่สาม database sync ดึงข้อมูลจาก Zendesk Salesforce Postgres เข้า Notion database อัตโนมัติ. ตัวอย่างที่ Notion โชว์คือ Worker ปิด task เมื่อ PR merge อัพเดท CRM เมื่อ subscription เปลี่ยน สร้าง onboarding doc เมื่อ offer letter เซ็น — ทั้งหมดที่ก่อนต้องผ่าน Zapier Make n8n ตอนนี้ Notion เก็บไว้เอง. Workers ฟรีช่วง beta เริ่มคิด Notion credits วันที่ 11 สิงหาคม. คู่แข่งจริงไม่ใช่ Confluence แต่เป็น Zapier และ Make.com — Notion เดิมพันว่าจะเป็น agent control room ที่ data อยู่แล้วและ agent หลายตัวมาเจอกัน. มุม OpenBridge นี่คือข่าวใกล้ตัวเราที่สุด คำถามที่ต้องตอบสัปดาห์หน้า ลูกค้าเราที่ใช้ Notion จะอยู่หรือย้ายไป Workers, เรามี integration กับ Notion ที่ลูกค้าใหม่ใช้ได้ทันทีไหม. ทางที่ปลอดภัยกว่าคือทำ depth ใน B2B connector ที่ Notion จะไม่ทำ เช่น Thai banking API regional ERP แล้ว expose ผ่าน MCP server หรือ External Agent ให้ Notion Workers เรียก — เป็น data plane ให้ Notion เป็น control plane ดีกว่าแข่งตรง ๆ.
