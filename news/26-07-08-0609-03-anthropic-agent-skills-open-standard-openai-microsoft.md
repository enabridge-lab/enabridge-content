---
date: 2026-07-08
slug: anthropic-agent-skills-open-standard-openai-microsoft
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  A wide editorial isometric scene: a giant open-source jigsaw board titled
  "AGENT SKILLS — OPEN STANDARD". Puzzle pieces coming from all sides — one
  large piece stamped "ANTHROPIC" placing the center piece, and four pieces
  labeled "OPENAI", "MICROSOFT", "ATLASSIAN", "FIGMA" locking in. A sub-shelf
  underneath shows small skill cards labeled "CANVA", "NOTION", "JIRA",
  "SLACK". A banner on top reads "PORTABLE ACROSS PLATFORMS". Cinematic warm
  lighting, 1:1 aspect, readable at 200px thumbnail, no real human faces.
image: images/26-07-08-0609-03-anthropic-agent-skills-open-standard-openai-microsoft.png
---

# Anthropic Agent Skills กลายเป็น open standard — OpenAI/Microsoft/Atlassian/Figma รับ, ChatGPT + Codex CLI ใช้ spec เดียวกันเงียบ ๆ, org-level Skills management เข้า Team/Enterprise

## TL;DR
- Anthropic ปล่อย **Agent Skills** เป็น open standard — spec ให้ AI assistant เรียนรู้ specialized task (เช่น "fill Excel form", "generate legal contract Thai", "run RCA on SEV1") — พร้อมประกาศให้ **Microsoft, OpenAI, Atlassian, Figma** เป็น first-wave adopter
- Dev **Elias Judin** เจอว่า **OpenAI เอา architecture ที่ structurally identical ไปใส่ ChatGPT + Codex CLI แล้วเงียบ ๆ** — directory ที่เก็บ skill file mirror spec ของ Anthropic ตรง ๆ. คือ **OpenAI adopt spec คู่แข่ง โดยไม่ประกาศ**
- Enterprise feature ใหม่: **org-wide Skills management** สำหรับ Team + Enterprise plan — admin จัดการ Skills กลาง, user access prebuilt Skills จาก **Canva, Notion, Figma, Atlassian**. Signal — Anthropic เดิน play เดียวกับ **MCP** (บริจาคให้ Linux Foundation) — **ecosystem growth > proprietary lock-in**

## เกิดอะไรขึ้น
Anthropic ปล่อยข่าวว่า **Agent Skills** — spec ให้ AI agent load "skill" เป็น modular package (คล้าย plugin แต่เป็น instruction + tool + context package ที่ portable) — จะเปิดเป็น **open standard** อย่างเป็นทางการ. Skill 1 ตัว = folder ที่มี YAML metadata + prompt/instruction + reference file + tool binding — agent ตัวไหนที่ implement spec นี้ก็สามารถ load skill ตัวเดียวกันได้ ไม่ผูกกับ Claude โดยเฉพาะ

Twist ที่ทำให้เรื่องนี้ hot: dev ชื่อ **Elias Judin** ไปเปิดดู source ของ ChatGPT desktop app กับ Codex CLI แล้วเจอว่า **OpenAI ก็เอา architecture ที่ structurally identical ไปใส่แล้ว** — directory layout mirror spec ของ Anthropic ตรง ๆ, format YAML metadata ตรงกัน, มี "skill loader" ที่ resolve tool call แบบเดียวกัน. OpenAI ไม่ได้ประกาศเป็นทางการว่า adopt Skills; VentureBeat ตีข่าวว่านี่คือ **"OpenAI adopt คู่แข่งเงียบ ๆ"** — signal ที่แข็งมากว่า **spec นี้จะเป็น de facto standard** ไม่ว่า OpenAI จะยอมรับ public หรือไม่

Enterprise angle — Anthropic เพิ่ม **org-wide Skills management** เข้า Team + Enterprise plan: admin ของ organization กำหนดได้ว่า user ใช้ Skill ตัวไหนได้บ้าง, deploy Skill แบบ central, และ audit ว่าใครเรียก Skill อะไรตอนไหน. **Prebuilt Skills** ที่มาพร้อม launch จาก partner ecosystem: **Canva** (สร้าง presentation), **Notion** (สร้าง page + link database), **Figma** (สร้าง component + prototype), **Atlassian** (สร้าง Jira issue + Confluence page). — คือ workflow tool ที่ knowledge worker Fortune 500 ใช้ทุกวัน กลายเป็น Skill ที่ AI agent ตัวไหนก็เรียกได้

Pattern ต่อจาก MCP — Anthropic เดิน play เดียวกับที่ทำกับ Model Context Protocol เมื่อปีที่แล้ว: **บริจาค spec ให้ Linux Foundation, open ให้ทั้งอุตสาหกรรมใช้, เก็บ engagement ผ่าน quality ของ Claude implementation แทน lock-in ทาง protocol**. Anthropic + OpenAI + Block เพิ่ง co-found **Agentic AI Foundation** ร่วมกับ Google/Microsoft/AWS เป็น member — organization กลางที่ steward ทั้ง MCP + Agent Skills + spec อื่น ๆ ในอนาคต

## ทำไมสำคัญ
Agent Skills เป็น **spec ที่แก้ปัญหาแรง friction ที่สุดของ agent enterprise deployment** — คือ knowledge transfer ระหว่าง team + agent. เดิม ทีม security เขียน runbook 40 หน้าให้ agent ทำ SEV1 response แต่ทำใน Anthropic Claude ไม่ portable ไป OpenAI/Google; ทีม legal เขียน template contract Thai แต่ใช้ได้เฉพาะบน platform ตัวเอง. Agent Skills spec = **runbook + template + prompt engineering ที่ portable ระหว่าง platform** — reduce lock-in cost ของ enterprise ที่ hate multi-vendor commit

Point ที่ OpenAI adopt spec คู่แข่ง **โดยไม่ประกาศ public** เป็น signal เชิงตลาดที่แข็งมาก — bigger tell กว่า Anthropic ออก press release. แปลว่า OpenAI มองว่า Skills = table stake ที่ต้องมี **ไม่ใช่ differentiator ที่จะไปสร้างเอง** — เพราะ compete กับ Anthropic ที่ **ecosystem MCP + Skills + Sub-agent** อยู่แล้วในขณะที่ตัวเองยังต้องปั้นเอง. เทียบกับตอนที่ MCP launch (Nov 2024): OpenAI ปฏิเสธเป็นปีกว่าจะยอม adopt; รอบ Skills นี้ adopt ในเดือนเดียวหลัง launch — cycle time ในการยอมรับ open standard สั้นลงมาก

Contrast กับ **Google Gemini Agent Space / Microsoft Copilot Studio** ที่ยังพยายามสร้าง skill/agent ecosystem แบบ proprietary — ทั้งคู่จะกลายเป็น island ถ้าไม่ adopt spec นี้ในไตรมาสถัดไป. **Salesforce Agentforce, ServiceNow AI Control Tower** ที่เน้น vertical enterprise ก็ต้องประกาศ Skills support ในเร็ววันเช่นกัน — เพราะลูกค้าจะเริ่มถามว่า "Skill ที่เราสร้างในระบบเธอ portable ไปที่อื่นไหม" — คำตอบ "ไม่" = deal breaker ในไตรมาสถัดไป

## มุม AI Agent Platform
- **Builders** — startup ที่ทำ **agent framework** ต้อง support Skills spec เป็น first-class โดย default — ไม่รอ 6 เดือน. skill catalog / registry / marketplace เป็นช่องเปิดใหม่ให้ **startup** สร้าง — คล้าย npm registry ของยุค Node.js. **Vertical skill vendor** (สายกฎหมายไทย, สายการเงินไทย, สาย SME accounting) มี opportunity ขาย skill เป็น package ที่ price per usage — ไม่ต้อง build agent เต็มตัว. **Framework startup** ที่ทำ orchestration ต้องรีบ integrate Skills loader ก่อนถูก LangGraph/CrewAI OSS แซง

- **Users / business ไทย** — corporate ที่ pilot agent อยู่ (SCB, KBank, AIS, True, CP, PTT) ให้ทีม knowledge management เริ่มถอด **procedure/SOP/runbook ภายในเป็น Skill format** โดยไม่ต้องคิดเรื่อง vendor ก่อน — ถ้า Skills เป็น open standard จริง Skill ที่เขียนวันนี้จะ portable ไป vendor ไหนก็ได้ปีหน้า. **ทีมกฎหมาย/compliance** — Skill "review contract คู่กับ PDPA" ที่ทำได้จริง คือ moat ที่ทีมภายในสร้างได้เอง โดยไม่ต้องรอ vendor. **CISO** — Skill = attack surface ใหม่, ต้องมี policy audit ก่อน enable prebuilt skill จาก external partner (Canva/Notion อาจ leak sensitive doc ได้ถ้า skill ไม่ถูก governance)

- **Ecosystem** — Agentic AI Foundation ที่ Anthropic + OpenAI + Block co-founded (+ Google/Microsoft/AWS member) จะกลายเป็น governance body ระดับอุตสาหกรรม — คล้าย W3C ของยุค web แต่สำหรับ agent. **Model vendor รอง** (Kimi, DeepSeek, Qwen, Mistral) ต้อง support Skills spec เพื่อเข้า Fortune 500 procurement. **SaaS incumbent** (Notion, Figma, Atlassian, Canva) ที่ปล่อย prebuilt Skills ได้ distribution ผ่าน Claude/ChatGPT ที่มี user 500M+ ทันที — ทำ Skill 1 ตัวได้ engagement มากกว่า plugin marketplace ปกติ 10x

## Sources
- [Anthropic launches enterprise 'Agent Skills' and opens the standard — VentureBeat](https://venturebeat.com/ai/anthropic-launches-enterprise-agent-skills-and-opens-the-standard)
- [Anthropic Launches Skills Open Standard for Claude — AI Business](https://aibusiness.com/foundation-models/anthropic-launches-skills-open-standard-claude)
- [Agent Skills: Anthropic's Next Bid to Define AI Standards — The New Stack](https://thenewstack.io/agent-skills-anthropics-next-bid-to-define-ai-standards/)
- [Equipping agents for the real world with Agent Skills — Anthropic](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

---

## Audio script
วันนี้ Anthropic ปล่อย Agent Skills เป็น open standard spec ให้ AI agent โหลด skill เป็น modular package คล้าย plugin แต่เป็น instruction บวก tool บวก context ที่ portable First wave adopter ที่ประกาศคือ Microsoft OpenAI Atlassian Figma ที่ interesting คือ dev ชื่อ Elias Judin ไปเปิดดู source ของ ChatGPT desktop app กับ Codex CLI แล้วเจอว่า OpenAI ก็เอา architecture ที่ structurally identical ไปใส่แล้วโดยไม่ประกาศ Directory layout mirror spec ของ Anthropic ตรง ๆ VentureBeat ตีข่าวว่านี่คือ OpenAI adopt คู่แข่งเงียบ ๆ signal ที่แข็งมากว่า spec นี้จะเป็น de facto standard ไม่ว่า OpenAI จะยอมรับหรือไม่ Enterprise feature ใหม่คือ org wide Skills management เข้า Team กับ Enterprise plan admin จัดการ Skills กลาง user access prebuilt Skills จาก Canva Notion Figma Atlassian pattern ต่อจาก MCP ที่ Anthropic บริจาคให้ Linux Foundation เดิน play เดียวกัน ecosystem growth มากกว่า proprietary lock in ที่สำคัญคือ Skill spec แก้ปัญหา friction ที่สุดของ agent enterprise deployment คือ knowledge transfer ระหว่าง team กับ agent เดิมทีม security เขียน runbook 40 หน้าให้ agent ทำ SEV1 response แต่ portable ไม่ได้ระหว่าง platform ทีมกฎหมายเขียน template contract Thai ใช้ได้เฉพาะ platform ตัวเอง Skills spec ทำให้ runbook กับ template portable ระหว่าง vendor สำหรับธุรกิจไทย corporate ที่ pilot agent อยู่ SCB KBank AIS True CP PTT ให้ทีม knowledge management เริ่มถอด SOP internal เป็น Skill format โดยไม่ต้องคิดเรื่อง vendor ก่อน ถ้า Skills เป็น open standard จริง Skill ที่เขียนวันนี้จะ portable ปีหน้า
