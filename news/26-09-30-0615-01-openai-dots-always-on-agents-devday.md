---
date: 2026-09-29
slug: openai-dots-always-on-agents-devday
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a glowing constellation of five small
  orbs — "dots" — orbiting a laptop screen labeled "ChatGPT SPACE". Each dot
  runs on its own miniature cloud computer with a tiny browser window,
  stitched to Slack and Microsoft Teams icons with light beams. A big price
  tag reads "$200/mo — PRO 200". Cinematic teal-and-amber palette, sharp
  contrast for 200px thumbnails, bold text rendering, no real human faces,
  1:1 aspect. Style of a Wired magazine cover story.
image: images/26-09-30-0615-01-openai-dots-always-on-agents-devday.png
---

# OpenAI เปิดตัว "Dots" always-on agents ที่ DevDay — ChatGPT กลายเป็น shared surface ของคนกับเอเจนต์

## TL;DR
- OpenAI จัด DevDay 2026 วันที่ 29 ก.ย. เปิดตัว **dots** — always-on agents ตัวเล็ก ๆ ที่รันบน GPT-6.1 Sol แต่ละตัวมี cloud computer + browser ของตัวเอง ทำงาน 24/7
- **ChatGPT Space** เป็น shared workspace ให้ทีมคน + ทีม dots ทำงานร่วมกัน — เข้าถึงผ่าน desktop/mobile/web, Slack, Teams, และ voice call
- Dots มีเฉพาะ Pro 200 ($200/เดือน) กับ Business Premium — เป็นสัญญาณว่า OpenAI แยก "agent tier" ออกจาก consumer แล้ว

## เกิดอะไรขึ้น
Sam Altman ขึ้นเวที Bill Graham Auditorium ที่ San Francisco วันที่ 29 กันยายน แล้วประกาศ 20+ ผลิตภัณฑ์ในงาน DevDay 2026 — แต่พาดหัวจริงเหลือแค่คำเดียว: **dots**. แต่ละ dot คือ always-on agent ที่รันบน GPT-6.1 Sol (โมเดลใหม่ที่ประกาศในวันเดียวกัน), ได้ cloud computer และ browser ส่วนตัว, จำ preference ของเจ้าของจาก feedback แล้วทำงานให้ต่อเนื่องไม่หยุด. งานบางอย่างจะโผล่มาก่อนที่เราจะสั่ง — OpenAI บอกว่า "some of the work will show up before anyone asks for it."

Dot ใช้ apps ได้หลายตัวตั้งแต่ Slack, Microsoft Teams, ChatGPT, และจะขยายต่อ. คุยกับมันได้ผ่าน desktop app, mobile, web, ผ่าน Slack/Teams, ผ่าน voice call — SMS มาต่อ. แต่ราคาไม่ใช่ของฟรี: dots มีเฉพาะแพ็คเกจ Pro 200 (200 ดอลลาร์/เดือน) กับ Business Premium — Plus ($20) กับ Pro tier ล่าง ($100) ไม่ได้.

คู่กับ dots คือ **ChatGPT Space** — collaborative workspace ที่ให้คนจริงกับ dots นั่งอยู่ในห้องเดียวกัน แชร์ page, presentation, living document, และงานที่ dots กำลังรันในพื้นหลัง. Altman อธิบายว่า ChatGPT ตอนนี้ไม่ใช่ chatbot แล้ว มันเป็น "shared surface" ที่คน + agent มาทำงานร่วมกัน และเป็น native runtime ให้ developer ปล่อย plugin extensions ที่เป็น "essentially entire applications" ยัดเข้าไปได้เลย.

## ทำไมสำคัญ
Signal ใหญ่ที่สุดคือ **การเปลี่ยน mental model ของ ChatGPT ทั้งตัว**. เดิม OpenAI ขาย ChatGPT เป็น chat interface ผูกกับ subscription รายเดือน. dots ทำให้มันกลายเป็นสิ่งอื่น — เป็น container ที่ agent หลายตัวรันอยู่พร้อมกัน แต่ละตัวมี state, memory, tools ของตัวเอง แล้วผู้ใช้เดินเข้าออก session ได้เหมือน slack channel. เมื่อ ChatGPT รองรับ multi-agent + human collaboration ในระดับ product interface มันก็เริ่มเป็น competitor ตรงของ enterprise workspace ทั้ง Slack, Teams, Notion — ไม่ใช่แค่ Copilot ในหน้าจอ.

ราคาเป็นสัญญาณอีกอย่าง. $200/เดือน สำหรับ dots ไม่ได้ pricing แบบ consumer software — มัน priced แบบ productivity subscription (Sierra, Devin, Harvey) ที่ขายให้คนที่มีเวลาเป็นเงิน. หลายเดือนที่ผ่านมา OpenAI พูดว่า revenue เพิ่ม 70% ตั้งแต่ต้น Q3 ไปแตะ $70B ARR — ตัวเลขระดับนี้จะเกิดขึ้นไม่ได้ถ้าไม่มี tier แบบ dots ที่ margin สูงกว่า chat หลายเท่า. คนที่จ่าย $200/เดือน คือคนที่คำนวณแล้วว่า ROI ของ dot หนึ่งตัวคืนใน 2-3 ชั่วโมงของงาน.

Angle ที่คม: OpenAI เรียก dots ว่า "coworkers" — คำเดียวกับที่ Meta Muse ใช้และ Sierra ใช้. ทุกเจ้าที่มี frontier model กำลังกลบเส้นแบ่งระหว่าง "assistant ที่ตอบคำถาม" กับ "employee ที่มีงานประจำ". เมื่อผู้ใช้ 30 ล้านคนเริ่มพูดว่า "ให้ dot ของฉันไปทำ" ในที่ทำงานปกติ agent ก็เข้า mainstream vocabulary — เร็วกว่าที่ analyst คาดไว้ตอนต้นปี.

## มุม AI Agent Platform
**Builders** — ChatGPT Space เปิดเป็น native runtime ให้ plugin extensions ที่เป็น "entire applications" — ถ้าคุณสร้าง agent framework แล้ว distribution ยังเป็น API รอผู้ใช้เรียก คุณกำลังแพ้ระดับ 10 เท่า. คำถามคือคุณจะทำตัวเป็น "OS ของ agents" (LangChain, CrewAI) หรือทำตัวเป็น "app in someone else's OS" (plugin ใน ChatGPT). ทางเลือกทั้งสองอย่างใช้ code base คนละแบบ. **Users/Business** ที่ deploy agent ในองค์กร — dots กำลังจะสอนให้ทีมของคุณคาดหวังว่า agent ต้อง always-on + มี memory ต่อเนื่อง + คุยได้หลาย channel. ระบบ internal ของคุณที่ยังใช้ agent แบบ stateless (คุยจบ session ลืมทุกอย่าง) จะดูแย่มากในเดือน 3 หลังจาก dot เข้าองค์กร. **Ecosystem** — Slack กับ Microsoft Teams เพิ่งเจอคู่แข่งใหม่ที่มี native AI พร้อมใช้ ไม่ต้องซื้อเพิ่ม. ระยะสั้น dots คุยกับ Slack ได้ ระยะกลาง Slack/Teams ต้องตัดสินใจว่าจะ "เปิดกว้าง" ให้ dots เข้ามาเดินเยอะ ๆ หรือปิดประตูแล้วออก own agent เอง. Microsoft ที่ยังถือหุ้น OpenAI จะอยู่ในตำแหน่งประหลาดที่สุด.

## Sources
- [OpenAI launches Dots, always-on AI agent coworkers, and ChatGPT Space — VentureBeat](https://venturebeat.com/technology/openai-launches-dots-always-on-ai-agent-coworkers-and-chatgpt-space-where-they-can-collaborate-with-human-teams)
- [OpenAI launches Dots, always-on AI agents in ChatGPT with their own cloud computers — SiliconANGLE](https://siliconangle.com/2026/09/29/openai-launches-dots-always-on-ai-agents-in-chatgpt-with-their-own-cloud-computers/)
- [OpenAI DevDay recap: Dots agents, Altman on IPO — CNBC](https://www.cnbc.com/2026/09/29/openai-devday-2026-live-updates.html)
- [DevDay 2026 Recap — OpenAI](https://openai.com/index/devday-2026-recap/)

---

## Audio script
ข่าวใหญ่วันนี้ครับ. เมื่อวานที่ San Francisco Sam Altman ขึ้นเวที DevDay 2026 แล้วประกาศของใหม่ 20 กว่าอย่าง แต่พาดหัวจริงเหลือแค่คำเดียว: dots. dots คือ always-on agent ตัวเล็ก ๆ ที่รันบน GPT-6.1 Sol โมเดลใหม่ของ OpenAI แต่ละตัวได้ cloud computer กับ browser ส่วนตัว จำ preference เจ้าของแล้วทำงานให้ 24 ชั่วโมงต่อวัน. คุยกับมันได้ผ่าน ChatGPT, Slack, Teams หรือโทร voice call ได้เลย. ที่น่าสนใจกว่าตัว dots คือ ChatGPT Space workspace ที่คนจริงกับ dots นั่งอยู่ในห้องเดียวกัน แชร์ page, document, งานที่ agent กำลังรันในพื้นหลัง. ChatGPT ไม่ใช่ chatbot อีกต่อไป มันกลายเป็น shared surface ที่คนกับ agent มาทำงานร่วมกัน. ราคาไม่ถูก dots มีเฉพาะแพ็คเกจ Pro 200 กับ Business Premium — เดือนละ 200 ดอลลาร์ขึ้น. OpenAI ตั้งราคาแบบ productivity subscription ไม่ใช่ consumer software เพราะรู้ว่าคนที่จ่ายคือคนที่คำนวณ ROI แล้วคุ้ม. Impact ต่อ AI Agent Platform ชัดมากครับ. ถ้าคุณเป็น builder ทำ framework แต่ distribution ยังต้องรอผู้ใช้เรียก API คุณกำลังแพ้ 10 เท่า. ถ้าคุณเป็น business ที่ deploy agent ในองค์กร ระบบ internal ที่ agent ยังเป็น stateless ลืมทุกอย่างจบ session จะดูโบราณมาก. Slack กับ Teams เจอคู่แข่งใหม่ที่มี native agent พร้อมใช้แล้ว. Microsoft ที่ถือหุ้น OpenAI อยู่จะอยู่ในตำแหน่งประหลาดที่สุดครับ.
