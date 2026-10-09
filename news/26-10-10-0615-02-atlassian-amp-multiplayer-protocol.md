---
date: 2026-10-07
slug: 26-10-10-0615-02-atlassian-amp-multiplayer-protocol
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial hero: a glass boardroom table viewed from above with six seats —
  three occupied by human silhouettes, three by glowing geometric agent
  avatars. In the center floats a shared document labeled "TEAMWORK GRAPH"
  with scoped permission rings colored differently for each seat. A big
  overhead sign reads "AMP: AGENTIC MULTIPLAYER PROTOCOL". Thin arrows
  loop between seats carrying tiny tags "@mention", "LOOM BRIEF", "MCP
  CALL". Isometric vector, Atlassian blue + emerald + warm grey, 1:1
  aspect, no real human faces.
image: images/26-10-10-0615-02-atlassian-amp-multiplayer-protocol.png
---

# Atlassian เปิด AMP — เอา AI agent มานั่งโต๊ะเดียวกับทีม แล้ว @mention เรียกใช้งานได้เหมือนคน

## TL;DR
- 7 ต.ค. 2026 ที่ Team '26 Europe, Atlassian ประกาศ **AMP (Agentic Multiplayer Protocol)** — platform layer ที่ให้ agent "ร่วมโต๊ะ" กับ human teammate ใน Jira / Confluence / Loom
- Agent แต่ละตัวได้ **scoped identity + scoped authority + scoped data context** → admin จำกัดได้ว่าใครเห็นอะไร ทำอะไรได้; มนุษย์ @mention เรียกใช้ใน comment thread, Jira ticket, หรือ **Loom video brief** (annotated recording) ก็ได้
- มาพร้อม **Atlassian MCP Server**, Teamwork Graph ที่ขยาย context, และ **Rovo Work mode** ที่ให้ agent รัน multi-step project ภายใต้ human oversight

## เกิดอะไรขึ้น

วันพุธที่ 7 ต.ค. 2026 ที่งาน Team '26 Europe, Atlassian เปิดตัวสิ่งที่พวกเขาเรียกว่า **Agentic Multiplayer Protocol (AMP)** — framework ที่ platform บริษัท (Jira, Confluence, Loom, Trello) ใช้คุมการ "ร่วมงาน" ระหว่าง human กับ AI agent. ทีซิสของ CEO **Mike Cannon-Brookes** ตรงไปตรงมา: "working with AI isn't single player any more — it's multiplayer" — จบยุค chatbot ที่พนักงานคุยคนเดียว เริ่มยุคที่ agent นั่งอยู่ใน channel เดียวกัน และทุกคน (คน + agent) เห็น context เดียวกัน

กลไกหลักของ AMP คือการ assign สามอย่างให้ agent แต่ละตัว: (1) **identity** — ตัวตนในระบบที่ตามรอยได้; (2) **authority** — ขอบเขตที่กระทำได้ (เปิด PR? merge? deploy? close ticket? post ใน #general?); (3) **scoped data context** — เห็น Jira project ไหน, Confluence space ไหน, Loom folder ไหน. admin กำหนดจาก console เดียว — ให้ agent ตัวใหม่ "เริ่มงาน" ใช้เวลาเท่าการ onboard พนักงาน

วิธีเรียก agent เข้างานเป็น UX ที่น่าสนใจที่สุด. ใน Confluence comment หรือ Jira thread, user **@mention agent** ได้ตรง ๆ เหมือน @ หา teammate; agent reply ใน thread เดียวกัน; ทุกคนในโปรเจกต์เห็น history ของการตัดสินใจ. และ Atlassian ยังเพิ่ม **Loom integration** ให้ user บันทึก video brief พร้อม annotation — "ดูที่ 1:14 ของคลิปนี้ แล้ว adjust Jira ticket PROJ-421" — เป็น input format ใหม่ที่ reduce context switching

ของเสริมที่ไม่ควรมองข้าม: (1) **Atlassian MCP Server** — expose Jira/Confluence/Loom เป็น MCP endpoint ให้ Claude Desktop, Cursor, และ IDE อื่น ๆ เข้าถึงข้อมูลได้ตรง ๆ; (2) **Teamwork Graph** รุ่นใหม่ที่ขยาย context ไปข้าม tool; (3) **Rovo Work mode** — mode ที่ Rovo agent รัน multi-step project (เขียน epic → แตก ticket → assign → track → report) ภายใต้ human oversight. ทั้งหมด available ใน early access แล้ว

**ข้อสงสัย:** Runtimewire ตั้งข้อสังเกตว่า Atlassian ประกาศ AMP เป็น "protocol" แต่ public material ยังไม่ชัดว่าเป็น **open standard ที่ vendor อื่น implement เองได้** หรือเป็นแค่ internal design pattern ของ Atlassian เอง. ถ้าปิด ประโยคเริ่มดูเหมือน "Atlassian lock-in มี logo ใหม่". TechTarget analyst เสริม — "คำถามสำคัญคือ customer trust Atlassian ให้ store และ curate context data ของ agent หรือเปล่า"

## ทำไมสำคัญ

AMP เป็น answer เชิง product ต่อปัญหาที่ Google ก็เจอ (เห็นจาก Gemini Agent) และ Salesforce ก็เจอ (จาก Agentforce) — **agent หลายตัวใน enterprise เดียวกันต้องมี protocol ร่วมกัน** หรือจะกลายเป็น ad-hoc integration hell ภายใน 18 เดือน. ตัว **scoped identity + authority + data** ของ AMP ตรง gap ที่ Microsoft Agent 365 ก็กำลังแก้ และ ServiceNow Workflow Agents, Salesforce Agentforce เริ่มพูดถึง. ทุกคน converge ไปที่ identity-first agent governance — question เดียวคือใครจะ win mindshare ของ CISO

**Pattern สำคัญ** คือ agent หยุด "เข้าหา user" แล้วเริ่ม "ร่วมโปรเจกต์". ก่อนหน้านี้ copilot cycle = user เปิด chat → ถามคำถาม → ปิด chat; context หายทันที; ไม่มีใครเห็น decision log. AMP เปลี่ยนเป็น agent ใช้ **conversation surface ที่คนใช้งานอยู่แล้ว** (Jira ticket, Confluence comment, Loom brief); decision อยู่ใน thread; audit free ไม่ต้องจ่าย extra. นี่คือ playbook ที่ Slack พยายามทำกับ AgentForce แต่ Atlassian ได้เปรียบตรงที่ platform เขาเป็น **system of record ของงาน** ไม่ใช่แค่ chat

Signal อีกชั้นคือ **Loom เป็น input format ใหม่สำหรับ agent**. ปี 2025-26 ตลาด voice interface พุ่ง (ElevenLabs, Deepgram, Vida); ปี 2026-27 **video brief + screen recording + annotation** จะเป็น input primitive ถัดไป. Loom + agent หมายถึง PM ไม่ต้องเขียน spec 10 หน้า — บันทึก 3 นาที, annotate, ให้ agent แตก epic เอง. ถ้าได้ผล productivity gain ของ product team อาจเป็น step-function

## มุม AI Agent Platform

**Builders:** คนทำ agent framework ควรจับ pattern "@mention invocation + conversation-as-context" เป็น UX primitive หลัก ไม่ใช่ chat window แยกต่างหาก. และ Atlassian MCP Server บอกชัดว่า **ทุก SaaS platform ของยุค 2026 ต้องมี MCP endpoint** — ถ้าไม่มี vendor อื่น integrate ไม่ได้ ตกจาก shortlist RFP. **Users / business ที่ใช้ Jira/Confluence/Loom อยู่แล้ว** ได้ path ง่ายที่สุดที่จะ pilot agent-in-workflow — ไม่ต้องย้าย data, ไม่ต้อง train พนักงานใหม่, ลงทะเบียน agent ใน admin console แล้ว @mention test ได้ภายในสัปดาห์

**Ecosystem:** ถ้า AMP เปิดจริงเป็น standard, มีสิทธิเป็น "Slack-of-agents" era — Atlassian ชนะที่ layer coordination. ถ้าปิด — Microsoft Teams + Google Workspace จะ reply ด้วย protocol ของตัวเอง (Microsoft Agent 365 มี similar concept อยู่แล้ว) และตลาดจะแตกเป็น silo อีก 2-3 ปีก่อน converge. SMB ไทยที่ใช้ Jira / Confluence หรือ Trello (ซื้อ Atlassian) ควร pilot Rovo Work mode เร็ว — มี potential ที่ PM 1 คน + Rovo รับ workload ของ PM 3 คนได้ ถ้าโฟลว์ sprint standard

## Sources
- [Atlassian Introduces AMP, the Agentic Multiplayer Protocol, to Power Human/AI Collaboration - SaaS Rise](https://www.saasrise.com/news/atlassian-launches-agentic-multiplayer-protocol-to-blend-humans-and-ai-agents-1c78ac0f-a690-4ed4-b630-93415c6c49f7)
- [Atlassian adds multi-player agent collaboration, expands context - TechTarget](https://www.techtarget.com/it-infrastructure/news/366651938/Atlassian-adds-multi-player-agent-collaboration-expands-context)
- [Atlassian introduces AMP to make AI agents visible in team workflows - Runtimewire](https://runtimewire.com/article/atlassian-amp-agentic-multiplayer-protocol)
- [AI work is multiplayer: Atlassian CEO on agentic AI - St-hakky](https://book.st-hakky.com/en/news/ai-work-is-multiplayer-atlassian-ceo-on-agentic-ai)

---

## Audio script
วันพุธที่ Team 26 Europe ของ Atlassian, Mike Cannon-Brookes เปิดตัว AMP — Agentic Multiplayer Protocol. ประโยคของเขาตรงไปตรงมา. การทำงานกับ AI ไม่ใช่ single player แล้ว มันคือ multiplayer. จบยุค chatbot ที่พนักงานคุยคนเดียว เริ่มยุคที่ agent นั่ง channel เดียวกับทีม และทุกคนเห็น context เดียวกัน. กลไก AMP คือ assign สามอย่างให้ agent — identity, authority, scoped data context. admin คุมจาก console เดียว onboard agent ใหม่ใช้เวลาเท่า onboard พนักงาน. UX ที่น่าสนใจที่สุดคือการเรียก agent. ใน Jira ticket หรือ Confluence comment user แค่ @mention agent เหมือน @ หา teammate; agent reply ใน thread เดียวกัน. และ Atlassian ให้บันทึก Loom video brief พร้อม annotation เป็น input ของ agent ได้ด้วย — PM ไม่ต้องเขียน spec 10 หน้า บันทึก 3 นาที annotate ให้ agent แตก epic. ของเสริม — Atlassian เปิด MCP Server ให้ Claude Cursor IDE อื่นเข้าถึง Jira Confluence ตรงได้ และ Rovo Work mode รัน multi-step project ภายใต้ human oversight. ข้อสงสัย — ยังไม่ชัดว่า AMP เป็น open standard หรือ internal pattern. Signal สำคัญ. agent หยุด เข้าหา user แล้วเริ่ม ร่วมโปรเจกต์. conversation surface ที่ใช้งานอยู่แล้วกลายเป็น context. audit log ฟรี. Loom จะเป็น input primitive ถัดไปของ agent ปี 2026 ถึง 27. SMB ไทยที่ใช้ Jira หรือ Trello อยู่แล้ว ลอง Rovo Work mode ได้เลย
