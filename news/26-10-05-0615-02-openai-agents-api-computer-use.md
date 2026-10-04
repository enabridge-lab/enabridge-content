---
date: 2026-10-05
slug: openai-agents-api-computer-use
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of an OpenAI-hosted browser window with
  a glowing padlock labeled "ORIGIN APPROVED". Behind it floats a GPT-6
  Astra crystal and a stack of three approval cards reading "SITE 1",
  "SITE 2", "SITE 3". A warning label at the bottom says
  "NOT PER-ACTION". Deep-emerald and warm-amber palette, bold text
  rendering for 200px thumbnails, no real human faces, 1:1 aspect,
  Wired magazine cover style.
image: images/26-10-05-0615-02-openai-agents-api-computer-use.png
---

# OpenAI เปิด Computer Use ใน Agents API — hosted browser ตัวใหม่ อนุมัติต่อ site ไม่ใช่ต่อ action

## TL;DR
- 29 ก.ย. OpenAI เปิด **Computer Use ใน Agents API** — agent ทำงานผ่าน browser ที่ OpenAI host เอง, รันบน **GPT-6 Astra**; ต้องส่ง header `OpenAI-Beta: agents=v1`
- Approval model เป็น **per-origin ไม่ใช่ per-action** — user approve ครั้งเดียวต่อ site; **"origin approval does not enforce confirmation before individual actions"** — คำพูดตรงของ OpenAI
- รองรับ email/password/verification code; **ไม่รองรับ passkey หรือ QR code**; only main agent request authen ได้ — subagent request ไม่ได้; max 6 credential field (16K char แต่ละ)

## เกิดอะไรขึ้น
วันที่ 29 กันยายน ที่ DevDay 2026 OpenAI ประกาศเพิ่ม **Computer Use** เข้า Agents API — agent สามารถ navigate เว็บ, อ่าน form, คลิก, พิมพ์, ใช้แอปผ่าน UI ของมันเอง — บน browser ที่ OpenAI host ให้. โครงนี้ไม่ใช่ของใหม่ในวงการ (Anthropic เปิด Computer Use ตั้งแต่ปลาย 2024, Operator ของ OpenAI เองก็มาตั้งแต่ ม.ค. 2025) แต่ที่สำคัญคือการ **ยัดลง Agents API สำหรับ developer ทั่วไป** และเปลี่ยน approval model เป็นแบบใหม่. รันบน **GPT-6 Astra** และยังอยู่ใน beta — ต้องส่ง header `OpenAI-Beta: agents=v1`.

Approval model ที่ OpenAI เลือกคือสิ่งที่ควรจดและสงสัยพร้อมกัน — เป็นแบบ **per-origin** ไม่ใช่ per-action. user approve ครั้งเดียวว่า agent เข้า `example.com` ได้ แล้วหลังจากนั้น agent ทำอะไรบน site นั้นก็ได้โดยไม่ต้อง confirm อีก. OpenAI พูดตรงในเอกสาร: *"origin approval does not enforce confirmation before individual actions"*. แปลเป็นปฏิบัติ — ถ้า agent cost คุณซื้อของผิดบน Amazon, delete email ผิดบน Gmail, หรือ send message ผิดบน Slack มันไม่ถือว่าเป็น OpenAI พลาด. OpenAI โยนความรับผิดชอบคืน developer: *"If your application must guarantee confirmation before purchases, destructive changes, or other consequential actions, restrict the hosted browser to resources that cannot perform them."*

ด้าน authentication มีขอบ: รองรับ email + password + verification code เท่านั้น — **ไม่รองรับ passkey หรือ QR authentication** (ซึ่ง site ใหญ่กำลังย้ายไป default). มี constraint ว่า **only the main agent can request browser authentication; subagents cannot** — เพื่อกัน prompt injection จาก tool output ที่ไม่ควร trust. Credential submission จำกัดที่ 6 field, 16,384 character per field, 120 KiB payload. OpenAI เตือนว่าทุก content ที่ browser อ่านมาควร treat เป็น "untrusted" — ซึ่งถูกต้องตาม threat model ของ Simon Willison, Steve Yegge, และ paper CPSC ตลอดครึ่งปีที่ผ่านมา.

**Availability**: ผ่าน API, และใน Codex + ChatGPT Work tier Pro 500 กับ Enterprise. ไม่มี pricing เปิดเผย — ของแบบนี้ปกติคิดเป็น session hour + token premium เพิ่มเติม.

## ทำไมสำคัญ
Pattern ที่ชัดคือ **big lab กำลังเลือก threat model ที่ realistic กว่า "confirm everything"**. ถ้า agent ทำงาน shopping, scheduling, HR task — user ไม่สามารถ confirm 50 action ต่อ session; UX จะพัง. OpenAI เลือก per-origin เพราะ assume developer จะ **sandbox agent ให้เข้า site ที่กู้คืนได้** ไม่ใช่ production system — เป็นท่าที่ realistic แต่โยนความเสี่ยงกลับไปที่ developer ที่ไม่ได้คิดเรื่อง blast radius.

เทียบกับ Anthropic Mods ที่ปล่อย 1 ต.ค. — Anthropic เลือก "no sandbox, คุณ audit code เอาเอง" สำหรับ Claude Code; OpenAI เลือก "sandbox browser แต่ไม่ sandbox action" สำหรับ Agents API. ทั้งสองเจ้ากำลัง delegate security กลับไปให้ builder — ซึ่งหมายความว่า **category ของ "AI agent runtime security"** กำลังเปิด: Snyk, Semgrep, Socket, Noma, Prompt Security, Lasso จะมี product สำหรับ "scan agent action log, flag anomalous origin, trigger human approval" ภายใน Q1 2027.

จุดที่ interesting ต่อ Enterprise ไทย — การที่ OpenAI ไม่รองรับ passkey และ QR auth = **ส่วนใหญ่ของ e-banking, PromptPay-linked service, government portal ไทย ใช้ไม่ได้**. ถ้าจะ deploy agent ที่ handle real workflow ยัง bottleneck ที่ authen layer. การย้ายเกินกว่า POC ต้องรอ passkey support อีก 1-2 iteration.

## มุม AI Agent Platform
**Builders** ที่กำลังสร้าง agent app: ก่อน ship ใด ๆ ที่ใช้ Computer Use ให้ **จำกัด origin whitelist** และ **อย่าทำ background agent** ที่ไม่มี human-in-the-loop ตั้งแต่วันแรก — threat ของ prompt injection ผ่าน tool output คือจริง. **Users/businesses** ที่มอง deploy agent สำหรับ customer-facing workflow: ตอนนี้ยังเหมาะ internal task (ขุด report ภายใน, draft document, QA บน staging site) มากกว่า production purchase หรือ transaction; รอ passkey + per-action approval policy สักครึ่งปีถึงจะ safe for retail. **Ecosystem**: Anthropic ต้องตอบด้วย Agents API แบบเดียว ไม่ใช่แค่ Claude Code; Google จะ ship Gemini Live Agent SDK เร็วขึ้น; Operator standalone ของ OpenAI เองก็เริ่มดูเหมือน product line ที่ cannibalize ตัวเอง — คาดว่าจะยุบรวมกับ Agents API ภายในสิ้นปี; และ identity vendor (Okta, Auth0, Clerk) จะมี "agent identity" product ที่แยกจาก human identity ภายใน Q4.

## Sources
- [OpenAI's Agents API gets a hosted browser, and one approval covers a whole site](https://mixed-news.com/en/openai-agents-api-computer-use-origin-approval/)
- [Computer use — OpenAI developer docs](https://developers.openai.com/api/docs/guides/agents-api/tools/computer-use)
- [OpenAI Gave AI Agents Their Own Computers at DevDay 2026](https://decrypt.co/379584/openai-ai-agents-computers-devday-2026-everything-announced)
- [OpenAI Expands Agents API with Computer Use and AWS Support at DevDay 2026](https://windowsreport.com/openai-expands-agents-api-with-computer-use-and-aws-support-at-devday-2026/)

---

## Audio script
ข่าวที่สอง. ที่ DevDay 2026 เมื่อ 29 กันยายน OpenAI เปิด Computer Use ใน Agents API — agent สามารถใช้ browser ที่ OpenAI host เอง เพื่อ navigate เว็บ กด form เข้าแอปผ่าน UI. รันบน GPT-6 Astra ยังอยู่ใน beta. ที่น่าจดและสงสัยพร้อมกันคือ approval model — เป็นแบบ per-origin ไม่ใช่ per-action. แปลว่า user approve ครั้งเดียวต่อ site แล้วหลังจากนั้น agent ทำอะไรก็ได้โดยไม่ต้อง confirm อีก. OpenAI พูดตรงในเอกสารว่า origin approval ไม่ enforce confirmation ก่อน individual action. ความเสี่ยงถูกโยนคืน developer. ด้าน authentication มีข้อจำกัดใหญ่ — รองรับ email, password, verification code เท่านั้น ไม่รองรับ passkey หรือ QR code. ซึ่ง site ใหญ่ ๆ กำลังย้ายไป passkey เป็น default. สำหรับ enterprise ไทยที่ส่วนใหญ่ของ e-banking กับ government portal ใช้ passkey และ QR — ยัง deploy agent ที่ handle real workflow ยาก. Pattern ที่ชัดคือ big lab กำลังเลือก threat model realistic กว่าแบบ confirm everything และโยน security กลับไปให้ builder. category ของ AI agent runtime security กำลังเปิด — vendor อย่าง Snyk, Socket, Prompt Security น่าจะมี product scan agent action log ภายใน Q1 2027 ครับ.
