---
date: 2026-09-17
slug: anthropic-one-claude-docs-slides-productivity
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A minimalist editorial illustration of three separate glass windows labeled
  "CHAT", "COWORK", "DESIGN" merging into a single glowing panel labeled
  "ONE CLAUDE" with two new tabs "DOCS (BETA)" and "SLIDES (BETA)" popping
  out. Behind the panel, two shadowy competitor logos loom on the horizon:
  a "365 COPILOT" box and a "WORKSPACE" box. Neon tagline reads
  "CONTEXT FOLLOWS YOU". Editorial isometric style, deep navy and Anthropic-
  orange palette with amber highlights, 1:1 aspect, no real human faces.
image: images/26-09-18-0609-02-anthropic-one-claude-docs-slides-productivity.png
---

# Anthropic รวม chat + Cowork + Design เป็น "One Claude" — เปิด Docs และ Slides beta ยิงตรง Google Workspace + Microsoft 365 Copilot

## TL;DR
- เมื่อวาน (16 ก.ย.) Anthropic รวม **Claude chat**, **Cowork** และ **Design** เข้าเป็น interface เดียวเรียกว่า **"One Claude"** — user ไม่ต้องเลือกอีกแล้วว่างานนี้ไปทำที่ไหน
- เปิด **Claude Docs** และ **Claude Slides beta** — พิมพ์คำสั่งเดียว Claude drafts doc หรือ deck ให้เลย พร้อม context/skill/connector ต่อเนื่องจาก chat
- Rollout เริ่มจาก Pro/Max plan (web + desktop + mobile), Team/Free ตามมา — เป็นการยิงตรง Google Workspace + Microsoft 365 Copilot ที่คุมตลาด office productivity

## เกิดอะไรขึ้น

Anthropic เก็บ pain point ที่ผู้ใช้บ่นตั้งแต่ Cowork เปิดตัวเมื่อต้นปี: **ต้องเลือกก่อนเริ่มพิมพ์ว่า "งานนี้ไป chat หรือไป Cowork?"** — chat เร็วแต่ทำงานยาว ๆ ไม่ได้, Cowork ทำงานยาวได้แต่ pointless สำหรับคำถามสั้น ๆ, แล้ว **context ไม่ carry ข้ามกัน** — ถ้าอยู่ใน chat แล้วอยากขยายเป็น full document ต้อง copy-paste ย้ายไป Cowork ใหม่. โพสต์ประกาศของ Anthropic บอกตรง ๆ ว่า "the update removes the need for users to decide where a task should go"

"One Claude" เป็นชื่อ marketing ของ interface ที่ **Claude เดาให้เองว่างานที่ user ขอต้องเป็น chat, ต้องเป็น Cowork workflow, หรือ Design artifact** — แล้วสลับ mode ให้อัตโนมัติ. Skills, connectors (Gmail, Slack, Google Drive, GitHub) และ project context ที่ set ใน chat จะติดตามไปตอน escalate เป็น Cowork หรือ Design โดยไม่ต้อง re-establish. ตัวอย่างที่ Anthropic โชว์คือ user คุยกับ Claude เรื่อง Q3 review ใน chat, Claude ตอบสั้น ๆ 2-3 turn, แล้วถามว่า "อยากให้ผมทำเป็น deck ให้ทีมทั้งหมดไหม?" — user ตอบใช่, Claude สลับเข้า **Slides mode** พร้อม content จาก chat ทั้งหมด + skill preset ของ user + Google Drive connector

**Docs และ Slides** เป็น 2 tool ใหม่ที่มาพร้อมกัน. Claude Docs beta ให้ Claude draft document แบบ collaborative — user แก้ inline, Claude เห็น diff, resume การเขียนต่อจากจุดที่ user แก้. Claude Slides beta คล้าย Beautiful.ai + Gamma — Claude gen structure ของ deck + visual + speaker note ทีเดียว. Rollout เริ่มที่ **Pro/Max plan** ใน web/desktop/mobile — **Team และ Free รอตามมา** (ยังไม่บอก timeline)

Claude Design (feature เดิม ที่ให้ generate visual/asset) ก็ถูกดึงเข้าให้เรียกจาก chat ตรง ๆ ได้ — เป็น mode สลับ ไม่ต้องเข้า Design tab แยก. Announcement ยัง note ว่า **projects, skills, memory** ที่ user สร้างไว้ก่อน "One Claude" launch จะ carry มาทั้งหมด — ไม่มี migration ให้ user ทำเอง

## ทำไมสำคัญ

Anthropic กำลังบอก positioning ที่ชัดที่สุดตั้งแต่บริษัทเปิดมา: **"Claude คือ workspace"** ไม่ใช่ AI assistant ที่เสียบใน workspace ของคนอื่น. Google Workspace มี Gemini ในทุก surface (Docs, Slides, Meet, Gmail); Microsoft 365 Copilot มี Word, PowerPoint, Teams, Outlook. Anthropic ไม่มี distribution ระดับ office suite — แต่ move นี้บอกว่า **จะสร้าง office suite ของตัวเองรอบ Claude** ตั้งแต่วันนี้

Pattern สำคัญคือ **"context follows user"** — เป็น thesis ที่ Sam Altman พูดถึงมานาน (single ChatGPT surface) และตอนนี้ Anthropic ทำจริง. Chat ที่ start เรื่อง Q3 review ต่อไป slide deck ได้ทันทีโดยไม่เสีย context; ต่อไป draft email หา CFO ก็ยังรู้เรื่อง Q3 อยู่. เมื่อ context = moat, cross-surface context = deep moat ที่ Google/Microsoft ต้องคิดแรง — เพราะ Docs/Sheets/Slides ของเขาเก็บ context แยกไฟล์ ไม่ต่อกัน

จุดที่ต้องจับตา 30 วันข้างหน้า: **Salesforce** ที่ผ่าน Dreamforce เมื่อวาน (15-17 ก.ย.) ประกาศ Agentforce 360 + AI Control Plane + Claudeforce (Claude ใน Salesforce Trust Boundary). ถ้า Anthropic push One Claude ให้เป็น workspace-level portal ในขณะที่ Salesforce push Agentforce ให้เป็น enterprise portal, **สอง portal นี้จะ collide ไหม?** — bet ผม: ไม่ collide เพราะ Claudeforce = Claude เข้าไปใน Salesforce; One Claude = Salesforce data เข้ามาใน Claude ผ่าน connector. เป็น complementary distribution แต่ **compete กันแย่ง developer/skill ที่คน build บน platform ไหน**

## มุม AI Agent Platform

สำหรับ **builders** — คนที่สร้าง skills, connectors, MCP server สำหรับ Claude — วันนี้ surface ที่จะรัน skill ของคุณเพิ่มขึ้น 3 เท่า (chat, Cowork, Design, Docs, Slides ทุกอันเรียก skill ได้). skill ที่ build ตอน chat-only จะ auto-elevate เข้า workflow ใหญ่กว่า. ผู้ build MCP server ที่ต่อ CRM/spreadsheet/email — pattern usage เดิมคือ "chat → tool call → chat" กลายเป็น "chat → tool call → doc → deck" ที่ยาวขึ้นและ retention สูงขึ้น

สำหรับ **users/business** ที่ deploy Claude ในองค์กร — ROI story ชัดขึ้น เพราะทีมเดียวใช้ Claude ทำได้ทั้ง knowledge Q&A + document drafting + presentation. ไม่ต้องซื้อ Beautiful.ai, Gamma, Notion AI, Copy.ai แยก. **Enterprise ที่มี license Anthropic Claude Enterprise ต่อ head จะ replace 2-3 SaaS tool ขนาดกลางได้**

สำหรับ **ecosystem**: SaaS วง productivity/design/document ต้องปรับ positioning. Beautiful.ai + Gamma โดน pressure โดยตรง; Notion + Coda ต้องตัดสินใจว่า **integrate Claude เป็น backend หรือชู "AI ของเราเอง"**. Bet: Notion เปิด MCP + Anthropic integration ก่อน (มี partnership อยู่แล้ว); Coda ตามช้ากว่า. Google Workspace + Microsoft 365 = ปลอดภัยระยะสั้นเพราะ distribution มหาศาล แต่ **cross-surface context ของ Claude คือ threat ระยะยาว** ที่ทั้งคู่ต้องตอบ

## Sources
- [Anthropic merges Claude chat and Cowork in one interface — TechCrunch](https://techcrunch.com/2026/09/16/anthropic-merges-claude-chat-and-cowork-in-one-interface/)
- [Anthropic Merges Claude Cowork and Chat into One Unified Experience — Inside AI News](https://insideai.news/news/ai-tools/claude-cowork-chat-merge/12097/)
- [Anthropic Launches One Claude, Merging Chat and Cowork With New Doc Tools — Time News](https://time.news/anthropic-launches-one-claude-merging-chat-and-cowork-with-new-doc-tools/)

---

## Audio script
Anthropic ปิดคำถามที่ผู้ใช้ Claude บ่นมาตั้งแต่ต้นปี. เมื่อวาน 16 กันยา เขา merge chat, Cowork และ Design เข้าเป็น interface เดียวเรียกว่า One Claude. ตอนนี้ผู้ใช้ไม่ต้องเลือกก่อนพิมพ์ว่างานนี้ไป chat หรือ Cowork — Claude เดาให้เองแล้วสลับ mode อัตโนมัติ พร้อม context, skill, connector ที่ carry ตามไปทุกที่. ที่ตามมาพร้อมกันคือของใหม่สองตัว: Claude Docs beta และ Claude Slides beta. พิมพ์คำสั่งเดียว Claude draft document หรือ deck ให้เลย ต่อจาก context ใน chat ก่อนหน้า. rollout เริ่มจาก Pro และ Max ก่อน แล้ว Team กับ Free ตามมา. positioning ชัดที่สุดตั้งแต่ Anthropic เปิดบริษัท: Claude ไม่ใช่ assistant ที่เสียบใน Workspace หรือ 365 อีกต่อไป — Claude คือ workspace. Google Docs, Sheets, Slides เก็บ context แยกไฟล์ ไม่ต่อกัน; Microsoft 365 Copilot ก็เช่นกัน. แต่ One Claude ให้ context เดิมตามไปทุก surface — chat → deck → email หาซีเอฟโอ ยังรู้เรื่องเดิม. moat นี้เป็น threat ระยะยาวที่ทั้ง Google และ Microsoft ต้องตอบ. สำหรับผู้สร้าง skill กับ MCP server รอบ Claude — surface ที่ skill รันได้เพิ่มขึ้นสามเท่าในวันเดียว. สำหรับองค์กรที่ซื้อ Claude Enterprise ต่อ head — ตอนนี้ replace Beautiful, Gamma, Notion AI, Copy AI ได้ในหนึ่งเดียว. เกม productivity SaaS เข้าคลื่นใหญ่แล้ว.
