---
date: 2026-10-27
slug: dayforce-agentic-hcm-claude-mcp
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a glass HR tower stamped "DAYFORCE" with
  rows of payroll desks. A glowing MCP pipeline runs from the tower into a
  separate studio marked "CLAUDE", carrying tagged payloads that read
  "APPROVE SHIFT", "TIME OFF", "ENGAGE CANDIDATE". On a side panel, three
  big numbers stack: "60M FORMS / YEAR", "MCP CONNECTOR: BETA",
  "BUILD + MARKETPLACE: 2027". A small lock icon between the two buildings is
  labeled "HUMAN CONFIRM REQUIRED". Deep navy and warm orange palette with
  silver accents, 1:1 aspect, strong contrast for 200px thumbnails,
  no real human faces.
image: images/26-11-03-0605-01-dayforce-agentic-hcm-claude-mcp.png
---

# Dayforce เปิด Agentic HCM Platform + ส่ง MCP connector เข้า Claude — ERP vendor รายต่อไปที่ต้องเลือกข้างใน 2027

## TL;DR
- 27 ต.ค. 2026 ที่ Dayforce Discover, Dayforce เปิด **Agentic HCM Platform** บน data model เดียว + **Ask Dayforce** เป็น conversational entry + **MCP connector เข้า Claude ที่ beta** (GA ปี 2027)
- Connector ให้ Claude อ่าน/เขียน HR + payroll data: approve shift, submit time off, engage candidate — ทุก write ต้อง **human confirm**
- Dayforce ยัง launch **Build** (plain-language app builder) + **Marketplace** (ปี 2027) + Build Academy certification; early partner: Aflac, Checkr, Deloitte, Emburse, Guusto, PwC, WorkBright
- Scale signal: Dayforce ประมวล **60 ล้าน form/ปี** ผ่าน HCM platform — ถ้า MCP ไหลผ่าน Claude ได้แม้แต่ 5% ก็เป็น 3 ล้าน task ที่ย้ายจาก UI → agent

## เกิดอะไรขึ้น

Dayforce (ชื่อใหม่ของ Ceridian หลัง rebrand ปี 2024, มูลค่าตลาด ~$10B) จัดงาน Dayforce Discover วันที่ 27 ตุลาคม 2026 แล้วเปิดสาม layer พร้อมกัน: **Agentic HCM Platform** (ชั้นล่าง — data model เดียว + Ask Dayforce เป็น natural-language interface), **Dayforce Build** (plain-language app builder — เขียน prompt → ได้ app/bot/document), และ **Dayforce Marketplace** (ที่พนักงาน Dayforce + partner + ลูกค้า publish เครื่องมือที่ตัวเองสร้างให้คนอื่นใช้ และ monetize ได้ถ้าผ่าน Build Academy)

Dr. Joe Korngiebel CEO ประกาศว่าสองของสาม layer — Build กับ Marketplace — จะ **GA ปี 2027** ไม่ใช่ตอนนี้. ส่วนที่พร้อมใช้ทันทีคือ Ask Dayforce บน platform ใหม่. **ตัวเด็ด** คือ MCP connector ที่ Dayforce ประกาศคู่กัน: ให้ Claude ของ Anthropic เรียกเข้า HR และ payroll data ผ่าน Model Context Protocol — action set เริ่มต้นที่ "approve shift" "fill open shift" "submit time off" "engage candidate" และ workflow approval. ทุก write operation ต้องผ่าน human confirmation ก่อน execute, การเข้าถึง data ยัง scope ตาม permission ของ user ที่ sign in

Scale signal ที่ Dayforce ใส่ลง deck: **60 ล้าน form จะไหลผ่าน Dayforce HCM ปีนี้**. นี่ไม่ใช่ตัวเลข agent — แต่เป็น TAM ของ task ที่อาจย้ายจาก UI → MCP tool call. บน engineering side, Dayforce วาง Agentic Platform บน single data model เดียว แทนการแยก HR / payroll / scheduling เป็นหลาย silo — ทำให้ MCP tool ไม่ต้อง join หลาย system เพื่อตอบคำถามเดียว. Diginomica ตั้ง skeptical note ว่า Marketplace launch ด้วย thin catalog + Build Academy ที่ยังไม่มีคนเรียน จะชักชวนลูกค้าให้ build on top ยาก

Early design partner ที่ Dayforce เปิดชื่อ: **Aflac, Checkr (background check), Deloitte, Emburse (expense), Guusto (recognition), PwC, WorkBright** — mix ระหว่าง insurance, consulting, และ HR tech. ไม่มีตัวเลข deployment หรือ seat จริงใน PR ยังเป็น reference design partner ปกติ

## ทำไมสำคัญ

**Pattern เดียวกับที่ Dayforce ทำวันนี้ กำลังเกิดกับ ERP/HCM vendor ทุกราย** — Workday (ยังไม่เปิด MCP endpoint), SAP (ประกาศ Joule Studio + Business AI Platform เมื่อ 30 ต.ค. — เราจะเขียนในรอบถัดไปถ้ามี update), Oracle (ประกาศ AI Agents แล้วแต่ยังไม่มี MCP), ServiceNow (เปิดกับ OpenAI). เมื่อ enterprise HR แพลตฟอร์มใหญ่เริ่มตั้งราคา action ตามการเรียก MCP ไม่ใช่ seat-based login อีกต่อไป, แต่ละบริษัทจะต้องเลือกข้าง — ให้ Claude หรือ ChatGPT เป็น default agent runtime ของพนักงาน HR

ตัวเลือกของ Dayforce ที่ **ปล่อย MCP ไป Claude ก่อน Copilot** น่าสังเกต (Microsoft เป็น partner อยู่แล้ว แต่ MCP connector ตัวนี้เปิดกับ Anthropic ก่อน). นี่คือสัญญาณที่สองในสัปดาห์ (ต่อจาก Cresta ที่ build บน Claude Agent SDK, และ UBS ที่ไม่เปิด vendor stack แต่มีรายงานใช้ Azure OpenAI + Claude mix) ว่า **Anthropic กำลังชนะศึก enterprise agent runtime มาตรฐาน** ผ่าน MCP เป็น gateway. Microsoft ยังมี distribution และ Copilot แต่ platform-level agent integration — ERP ทั้งหลายกำลัง bet บน MCP ของ Anthropic

ที่ยังไม่โดนพิสูจน์: adoption ของ Build + Marketplace. Low-code builder ที่ขายให้ "ใครก็สร้าง app ได้" มีหลุมเดิมของ Lightning (Salesforce), Power Platform (Microsoft) — คนสร้างน้อย, ของที่สร้างคุณภาพไม่ถึง, admin ตามไม่ทัน. ถ้า Dayforce ไม่มี Build Academy ที่ scale ได้จริงก่อน Marketplace launch ปี 2027, Marketplace จะกลายเป็น empty storefront. OpenAI ยอมปิด AgentKit (sunset 30 พ.ย. — เรารายงานใน round ที่แล้ว) เพราะเหตุผลเดียวกัน

## มุม AI Agent Platform

สำหรับ **builders** ที่สร้าง MCP connector หรือ agent runtime: Dayforce คือ reference ของ "วิธี publish MCP endpoint ให้ enterprise SaaS vendor". action pattern (read-only query + explicit write-with-human-confirm), scope (permission inherit จาก sign-in user), governance (admin review + Build Academy cert สำหรับ publisher) — คือ playbook ที่ Workday, Salesforce, Oracle จะ copy ภายใน 6-12 เดือน. ถ้าคุณขาย connector third-party, แข่งกับ official connector ที่ไม่มี human confirm + ไม่ scope permission ไม่ได้

สำหรับ **users / business**: ไทย/SEA ที่ใช้ Dayforce หรือ Workday มี procurement cycle ประมาณ 12-18 เดือน. ตอนนี้คือจังหวะที่ CIO ต้อง **ล็อค budget line ของ "MCP integration" แยกจาก seat license** — ไม่งั้นปี 2027 โดนเก็บ metered action charge โดยไม่มีงบ. **Per-action pricing** จะเป็นสงครามหลักของ enterprise SaaS ภายใน 18 เดือน (เรารายงานไป pattern นี้ตอน Sema4.ai Verified Queries ลด token 80% — ซึ่งแปลว่า vendor จะมี pricing lever ใหม่ที่ไม่ได้คิดจาก compute)

สำหรับ **ecosystem**: ชัดแล้วว่า **Anthropic กำลังผูกตัวเองกับ MCP เป็น protocol-level moat** (donation ให้ Linux Foundation ธ.ค. 2025, บวก connector partnership กับ Dayforce / Workato / Cresta / ServiceNow). OpenAI มี ChatGPT Apps + Agents API + Decisions API — แต่ Dayforce เลือก MCP ก่อน. ภายใน 6 เดือน ความเป็น "MCP support status" จะเป็น line item ใน RFP ของ enterprise HCM และ ERP ทั่วโลก

## Sources
- [Dayforce puts its HR and payroll data inside Anthropic's Claude (TNW)](https://thenextweb.com/news/dayforce-claude-connector-agentic-hcm-build)
- [Dayforce Build Lets Customers Extend Its HCM Platform (Futurum Group)](https://futurumgroup.com/?p=97235)
- [Dayforce Launches Build Marketplace for HCM Apps (ITBrief UK)](https://itbrief.co.uk/story/dayforce-launches-build-marketplace-for-hcm-apps)
- [Dayforce HCM to Claude via MCP (Diginomica)](https://diginomica.com/node/31400)

---

## Audio script
วันนี้มีข่าวจาก Dayforce ที่น่าจับตานะครับ Dayforce คือเจ้าของ HCM platform ที่คนไทยอาจไม่คุ้น แต่ประมวล form กว่า 60 ล้าน form ต่อปี บริษัทจัดงาน Dayforce Discover วันที่ 27 ตุลาคม แล้วเปิดสามของใหม่พร้อมกัน หนึ่ง Agentic HCM Platform บน data model เดียว มี Ask Dayforce เป็น natural language interface สอง Dayforce Build ที่ให้ user เขียน prompt แล้วได้ app หรือ bot ออกมา สาม Dayforce Marketplace ที่คนสามารถ publish ของที่สร้างให้คนอื่นใช้ และ monetize ได้ถ้าผ่าน Build Academy certification แต่ส่วนที่ชอบที่สุดคือ MCP connector เข้า Claude ของ Anthropic ตัว beta ให้ Claude อ่านและเขียน HR กับ payroll data ได้ ทุก write operation ต้อง human confirm ก่อน execute เริ่มจาก action set พื้นฐานเช่น approve shift submit time off engage candidate แม้ Build กับ Marketplace จะยังไม่ GA จนถึงปี 2027 แต่ตัว MCP connector นี่คือสัญญาณชัดครับว่า ERP กับ HCM vendor ทุกราย ภายใน 6 ถึง 12 เดือนต่อจากนี้ จะต้องเลือกข้างว่า default agent runtime ของพนักงาน HR คือ Claude หรือ ChatGPT ที่น่าสังเกตคือ Dayforce เลือก Claude ก่อน Copilot ทั้งที่ Microsoft เป็น partner มานานแล้ว นี่คือสัญญาณที่สามในสัปดาห์เดียวหลังจาก Cresta Conductor และ UBS ว่า Anthropic กำลังชนะศึก enterprise agent runtime มาตรฐาน ผ่าน MCP เป็น protocol-level moat สำหรับ CIO ที่ไทย คำแนะนำสั้น ๆ ครับ ตอนนี้คือจังหวะที่ต้องแยก MCP integration budget ออกจาก seat license ก่อนปี 2027 ไม่งั้นโดนเก็บ metered action charge โดยไม่มีงบ
