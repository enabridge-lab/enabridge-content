---
date: 2026-11-13
slug: adobe-mcp-creative-suite-agent-control
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric scene of an open Photoshop canvas with layers panel
  visible on one side; a glowing conduit labeled "MCP" bridges from a chat
  window labeled "CHATGPT" directly into the canvas, dragging layer edits.
  Behind, a giant headline reads "9 ARTBOARDS IN 9 MINUTES". A small red
  Adobe wordmark sits in the lower corner; a tiny sign reads "PRIVATE BETA
  EARLY 2027". Four tiny app tiles line up at the bottom: Ps, Pr, Ai, Ae.
  Clean editorial isometric style, red + warm cream + ink-blue palette, 1:1
  aspect, high contrast so headline + MCP label stay readable at 200px, no
  real human faces.
image: images/26-11-13-0604-03-adobe-mcp-creative-suite-agent-control.png
---

# Adobe เปิดบ้านให้ MCP — ไม่ใช่ feature แต่เป็น retreat จาก walled garden

## TL;DR
- Adobe ประกาศที่ MAX 2026 เมื่อวันที่ 10 พฤศจิกายน — Photoshop, Illustrator, Premiere Pro, After Effects จะรองรับ MCP ช่วง private beta ต้นปี 2027
- Demo โชว์ ChatGPT สร้าง 9 editable artboard ใน Photoshop ภายใน 9 นาที — เอดิตต่อได้จริงทุก layer
- เป็นครั้งแรกที่ Adobe ยอมให้ external AI agent เข้ามา manipulate native project file — ไม่ผ่าน Firefly, ไม่ผ่าน API wrapper

## เกิดอะไรขึ้น
วันที่ 10 พฤศจิกายน Adobe ประกาศที่งาน MAX 2026 ว่า Creative Suite จะรองรับ Model Context Protocol (MCP) — external AI agent (เช่น ChatGPT, Claude Desktop, Copilot) จะเข้ามาควบคุม Photoshop, Illustrator, Premiere Pro, After Effects ได้ตรง ๆ ผ่าน MCP server ที่ Adobe รัน feature จะเข้า private beta ช่วงต้นปี 2027 Demo ที่ MAX ใช้ ChatGPT เป็น client — คำสั่งเดียว agent สร้าง 9 artboard ของ Photoshop ภายใน 9 นาที ทุก layer ยัง editable (ไม่ใช่ raster flatten)

ประเด็นที่สำคัญคือ scope — ไม่ใช่ wrapper API ที่ส่ง prompt แล้ว render จาก server แต่เป็น agent ควบคุมแอป desktop จริงบน machine ของ user — manipulate layer, vector path, timeline bin, sequence โดยตรงในไฟล์ project ไฟล์ .psd, .ai, .prproj ที่ agent แก้ยังเปิดใน Adobe app แบบ editable 100% ที่ WordPress มี Gutenberg API ให้ตัวแก้ external ทำได้บ้างแต่ขนาด Photoshop + Premiere ซึ่งเป็น walled garden มายาวนาน ไม่เคยเห็น Adobe เปิดระดับนี้

Adobe ปล่อย Creative Agent ของตัวเองด้วย — เป็น AI Assistant ที่อยู่ใน Premiere, Illustrator, InDesign, After Effects, และ Frame.io ตอนนี้ beta แต่ MCP announcement สำคัญกว่า — เพราะเปิดให้ third-party agent เข้ามาแข่งกับ Adobe เอง

## ทำไมสำคัญ
Pattern ที่เห็นคือ — walled garden ยอม open protocol เมื่อรู้ว่า standalone agent + MCP ecosystem กำลังโตจนลูกค้าจะเริ่มถาม "ทำไมผม connect Photoshop กับ Claude ไม่ได้" การ ignore ยิ่งทำให้ workflow ของ user ย้ายออก (ส่งไฟล์ไป Figma + Runway + Topaz ที่ open กว่า) Adobe เลือก acquisition (เปิด MCP) แทน resistance (ปิดต่อ)

เทียบกับคู่แข่ง — Figma มี AI feature ของตัวเอง, Canva ประกาศ agentic orchestration เมื่อ 7 เดือนก่อน, Runway มี API เปิด Adobe ที่ชนะด้วย lock-in file format (.psd, .ai, .indd) ไม่สามารถชนะ AI-era ด้วย lock-in เดิมได้เพราะ agent รุ่นใหม่ transcode format ได้เร็ว + cheap มากขึ้นทุกไตรมาส MCP เป็นทางเลี่ยงเดียวที่ Adobe รักษา relevance ได้ — คือ ให้ agent เชื่อมเข้าแอปของตัวโดย native ไม่ต้อง export/import

Caveat ใหญ่สุดคือ timing — "private beta ต้นปี 2027" ยังไกลพอให้ Figma + Canva เร่งทำ Figma Make หรือ Canva Magic agent-controllable ก่อน Adobe launch จริง + ยัง unclear ว่า licensing จะผูกกับ Creative Cloud subscription tier ไหน ถ้า lock ให้เฉพาะ Enterprise tier ($85/seat ขึ้น) ความแรงจะหายไปเยอะ

## มุม AI Agent Platform
Builders — MCP เพิ่ม creative software เป็น surface ใหม่ — image, video, vector, motion graphics manipulation ผ่าน MCP server แปลว่า agent ที่ทำงาน marketing/brand/content workflow จะ orchestrate Adobe app ผ่าน MCP ได้โดยไม่ต้อง API wrapper เอง opportunities สำหรับ specialized agent (เช่น brand compliance checker ที่ scan ทุก .psd ของ organization) ชัดขึ้นมาก — แต่ต้องรอ 2027 beta

Users/business — ทีม creative ขนาดเล็กได้ประโยชน์ก่อนทีมใหญ่ — เพราะ agent เข้ามาเร่ง task ซ้ำ ๆ (resize สำหรับ social, color swap สำหรับ A/B, batch export) ที่ปกติต้อง junior designer 1-2 คน สำหรับ agency ไทยที่ขาย creative service เริ่มคิดตั้งแต่ตอนนี้ว่า pricing model จะเปลี่ยนไหม — ถ้า agent ทำ work ของ junior ได้ 70-80% ทีมของคุณต้อง reprice เป็น outcome ไม่ใช่ hour

Ecosystem — สิ่งที่น่าจับตา — ใครได้ "default AI client" ของ Adobe user เป็น ChatGPT, Claude Desktop, หรือ Microsoft Copilot? ถ้า ChatGPT ได้เพราะ demo ของ Adobe โชว์ด้วย OpenAI ก่อน — คือ win ใหญ่ที่ลด customer-acquisition cost ของ ChatGPT Plus/Pro อย่างเงียบ ๆ ทั่วทุกอุตสาหกรรม creative Microsoft Copilot + Claude Desktop ต้องรีบลงไปเจรจากับ Adobe ตอน beta ไม่งั้นจะเสียเปรียบตั้งแต่ GA

## Sources
- [Adobe MAX: AI agents to control Photoshop, Premiere Pro and more (Heise)](https://www.heise.de/en/news/Adobe-MAX-AI-agents-to-control-Photoshop-Premiere-Pro-and-more-11519781.html)
- [Adobe will let outside AI agents edit Photoshop and Premiere files (The Next Web)](https://thenextweb.com/news/adobe-mcp-integrations-photoshop-premiere-ai-agents)
- [Adobe announces MCP support for 2027 (Gigazine)](https://gigazine.net/gsc_news/en/20261111-adobe-creative-tools-mcp-support/)
- [Photoshop 28 is here: Relight, new AI tools, and MCP for AI agents starting in 2027 (Basic Tutorials)](https://basic-tutorials.com/news/photoshop-28-is-here-relight-new-ai-tools-and-mcp-for-ai-agents-starting-in-2027/)

---

## Audio script
Adobe ประกาศที่งาน MAX 2026 เมื่อวันที่ 10 พฤศจิกายน Creative Suite จะรองรับ Model Context Protocol หรือ MCP external AI agent เช่น ChatGPT, Claude Desktop, หรือ Microsoft Copilot จะเข้ามาควบคุม Photoshop, Illustrator, Premiere Pro, After Effects ได้ตรง ๆ ผ่าน MCP server ที่ Adobe รัน feature จะเข้า private beta ช่วงต้นปี 2027 Demo ที่ MAX ใช้ ChatGPT เป็น client คำสั่งเดียว agent สร้าง 9 artboard ของ Photoshop ภายใน 9 นาที ทุก layer ยัง editable จุดสำคัญคือไม่ใช่ wrapper API ที่ render จาก server แต่เป็น agent ควบคุมแอป desktop จริงบน machine ของ user แก้ไฟล์ native project ไฟล์ psd, ai, prproj โดยตรง pattern ที่เห็นคือ walled garden ยอมเปิด protocol เมื่อรู้ว่า standalone agent กำลังโตจนลูกค้าจะเริ่มถามว่าทำไม connect Photoshop กับ Claude ไม่ได้ Adobe เลือก acquisition แทน resistance Adobe ที่ชนะด้วย lock-in file format ไม่สามารถชนะ AI-era ด้วย lock-in เดิมได้เพราะ agent รุ่นใหม่ transcode format ได้เร็วและ cheap มากขึ้น MCP เป็นทางเลี่ยงเดียวที่ Adobe รักษา relevance ได้ สำหรับทีม creative ขนาดเล็กได้ประโยชน์ก่อน เพราะ agent เข้ามาเร่ง task ซ้ำที่ปกติต้อง junior designer 1-2 คน สำหรับ agency ไทยที่ขาย creative service เริ่มคิดตั้งแต่ตอนนี้ว่าถ้า agent ทำ work ของ junior ได้ 70-80% ทีมต้อง reprice เป็น outcome ไม่ใช่ hour
