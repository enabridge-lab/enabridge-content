---
date: 2026-08-28
slug: claudeforce-salesforce-anthropic-ui-is-the-ai
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial isometric illustration of a Salesforce Lightning cloud dissolving
  into ribbons of blue data pouring into a bright, glowing Claude conversation
  window on the right. On the Claude side, three floating chat bubbles labeled
  "MEETING PREP", "DEAL HEALTH", "PIPELINE REVIEW". Bold number panels above:
  "37 SKILLS", "PILOT NOW", "OPEN BETA SEP 2026". A neon banner across the top
  reads "THE UI IS THE AI". Deep navy background with orange-to-blue gradient
  rim lighting. 1:1 aspect. No real human faces (silhouette only). Text and
  numbers oversized so they read in a 200px thumbnail.
image: images/26-08-28-0621-01-claudeforce-salesforce-anthropic-ui-is-the-ai.png
---

# Claudeforce: Salesforce ยัด CRM ทั้งก้อนเข้า Claude — Benioff บอก "UI is the AI", สั่นสะเทือน SaaS pricing model ทั้งอุตสาหกรรม

## TL;DR
- **26 ส.ค. 2026** Salesforce + Anthropic ประกาศ **Claudeforce** — expanded strategic partnership โดย launch product แรกคือ **Salesforce in Claude**, plugin ที่ปล่อย Claude เข้าถึง data + workflow + governance ของ Salesforce ทั้งหมดผ่าน **37 prebuilt sales skills** (meeting prep, deal health review, pipeline review, ...) — pilot ตอนนี้, open beta ก.ย., Q3 ขยายไป function อื่น
- **Benioff บนเวที:** *"The UI is the AI"* — ลูกค้าจะไม่ต้องเปิด Salesforce UI แบบเดิมอีก, sellers คุยกับ Claude แล้ว agent เข้าถึง live revenue context + take governed action กลับได้เลย
- **Pricing model เปลี่ยน:** ลูกค้าจ่าย 2 invoice — Salesforce เก็บค่า "headless consumption" ตาม API tier + Anthropic เก็บค่า Claude inference แยก. Seat license อาจ cannibalize ตัวเอง — token consumption กลายเป็น revenue lever ใหม่
- Signal: **SaaSpocalypse debate เข้ารอบตัดสิน** — SaaS incumbent ที่ยอมเปิด "data + business logic layer" ให้ AI runtime ของค่ายอื่น อยู่รอด. ที่หวงไว้ในกำแพง UI ตัวเองจะโดน bypass. คู่แข่ง Microsoft (Copilot + Dynamics), Google (Gemini Enterprise + Workspace), OpenAI (Assistants API + ChatGPT Enterprise) ต้องรีบตอบ

## เกิดอะไรขึ้น

26 ส.ค. 2026 บนเวที Salesforce Q2 '27 earnings, Marc Benioff เปิดตัว **Claudeforce** ร่วมกับ Anthropic — เป็น expanded strategic partnership ที่ผูกยาวกว่า integration แบบเดิม. Product แรกออกวันเดียวกัน: **Salesforce in Claude** — Claude plugin ที่ install ครั้งเดียวแล้วปลด Claude ให้เข้าถึง entire revenue cycle ของบริษัท ตั้งแต่ pipeline, opportunity, contact, quote, forecast ไปจนถึง governance rule ที่ Salesforce บังคับใช้ทั้งหมด — ผ่าน MCP-compatible interface

Plugin นี้ **ไม่ใช่** generic CRM prompt wrapper รอบ API. Anthropic + Salesforce co-engineer **37 prebuilt sales skills** ที่ออกแบบเพื่อดึง Claude's reasoning, agentic tool use, และ generative UI มาช่วยงาน sales — เช่น meeting prep (Claude pull account history + last touchpoints + open opps → draft brief), deal health review (Claude cross-reference activity signal + forecast confidence + risk factor), pipeline review (Claude summarize weekly changes + flag stalled deals + suggest next best action). Sellers พิมพ์คำสั่งใน Claude → agent take **governed action** กลับเข้า Salesforce ทันที — update field, log call, move stage, create task — โดยยังผ่าน Salesforce permission + audit trail ตามเดิม

Timeline: pilot customers เริ่มใช้วันประกาศ, open beta กันยา 2026, expansion ไป service, marketing, commerce, industries function ช่วง Q3 2026 (ต.ค.-ธ.ค.). ราคาแบ่งเป็น **สอง invoice**: Salesforce เก็บค่า "headless consumption" (API calls ตาม license tier ของลูกค้า) + Anthropic เก็บค่า Claude inference (token-based) แยก — สองบริษัทเจรจา revenue split กันหลังบ้าน แต่ลูกค้าเห็นบิลตรงจากทั้งคู่. Salesforce Ben รายงานว่า Benioff ระบุใน earnings call ว่าลูกค้าใหญ่หลายรายอยู่ใน pilot แล้ว — ตัวเลข customer list ยังไม่เปิดเผย

Benioff quote สำคัญบนเวที: *"We're bringing together the world's #1 AI and #1 CRM — the best of both worlds. Here, **the UI is the AI**."* — signal ชัดว่า Salesforce ยอมรับว่าลูกค้าจะเลิกเปิด Salesforce Lightning UI เพื่อทำงาน sales รายวัน, sellers จะอยู่ใน Claude interface แล้วให้ agent ทำงานที่เมื่อก่อนต้อง click 15-20 ครั้งใน UI. Patrick Stokes, president of applications and marketing, ใน CNBC สัมภาษณ์: adoption pattern นี้ *"จะดัน token consumption ขึ้นซึ่งชัดเจนว่าเป็นเหตุผลที่ Anthropic ตื่นเต้น"*

## ทำไมสำคัญ

**Claudeforce คือ moment ที่ SaaSpocalypse debate เข้ารอบตัดสิน** — คำถามที่ค้างมาสองปีคือ "AI agent จะ commoditize SaaS UI layer แล้วดูดค่ากำไรไปหมด หรือ SaaS incumbent จะยึด data + business logic layer ไว้เป็น moat?" — Benioff เพิ่งตอบด้วยการเดินหมากที่ Wall Street analyst เรียกว่า *"radical concession or brilliant judo"* แล้วแต่มุมมอง

มุมหนึ่ง: Salesforce **ยอมเปิด data + workflow moat** ให้ AI runtime ของค่ายอื่น (Anthropic ไม่ใช่ subsidiary Salesforce) เข้ามาเป็น primary interface. Per-user seat license — โมเดล pricing ที่หล่อเลี้ยง SaaS มา 25 ปี — เริ่ม lose coherence เมื่อ user จริง ๆ ที่ทำ action ใน Salesforce กลายเป็น agent ไม่ใช่คน. หนึ่งใน analyst ในบทความ VentureBeat ระบุตรง ๆ: *"ถ้า interface layer commoditize, pricing power จะ migrate ไปหาคนที่ own intelligence — และ Anthropic ไม่ใช่ Salesforce ที่ own Claude."* คำถามคือ Salesforce จะเก็บ margin ได้ยาวแค่ไหน เมื่อ data + governance layer เป็นเพียง commodity ที่ AI vendor ใครก็ต่อได้

อีกมุม: การนี้อาจเป็น **brilliant defensive play** — ถ้า Salesforce ไม่เปิดเอง, OpenAI Operator หรือ Google Gemini Enterprise จะสร้าง connector ที่ scrape UI ของ Salesforce แล้ว bypass ต่างหาก. เปิดเองแปลว่าคุมเงื่อนไข — พันธมิตร Anthropic ที่มี MCP + governance stack แข็งกว่า OpenAI, สร้าง technical + commercial standard ก่อน. คนอื่นที่จะ integrate ต้องทำ Salesforce compliance ก่อน. Benioff ที่บริหาร Salesforce มา 27 ปีคง read tea leaves ได้ว่าตลาดจะไปทางไหน

**คู่แข่งต้องตอบใน 60-90 วัน** — Microsoft ที่มี Dynamics 365 + Copilot น่าจะประกาศ Dynamics in Copilot + skill catalog แข่งภายในไตรมาส 4 (มี Ignite ต.ค. เป็น target date). Google Gemini Enterprise Financial Services (25 ส.ค.) เป็น vertical bet — ถ้าไม่ตอบ horizontal จะโดนแซง. OpenAI ที่ยัง proprietary ทั้ง Assistants API + ChatKit จะเจอ pressure หนักสุด — enterprise deal ที่กำลังเจรจาอยู่จะเริ่มถาม "why not Claudeforce?"

## มุม AI Agent Platform

**Builders:** ถ้าคุณสร้าง vertical agent app หรือ agent framework — model นี้เป็น template ของ "next-gen SaaS distribution": ไม่ใช่ own the UI แต่ **own the skills catalog + governance layer + billing rail** ที่ agent runtime ใครก็ตามต่อได้. เริ่มออกแบบ SDK ให้ (1) publish MCP-compatible skill spec, (2) enforce per-tenant permission + audit trail ผ่าน protocol layer, (3) meter action ตาม consumption ไม่ใช่ seat. ถ้าคู่แข่งของคุณ ship Claude/ChatGPT/Gemini plugin ที่ทำงานได้ใน 5 นาที คุณจะไม่มีเวลา build proprietary UX แข่ง — ที่ต้อง ship คือ **skill catalog + governance moat**

**Users / business:** สำหรับ Salesforce customer — เริ่ม pilot Salesforce in Claude กับ sales team เล็ก 5-10 คน ทันที ก่อน open beta ก.ย. เพื่อวัด (1) time saved per rep per week (Claudeforce hyphe ว่าน่าจะ 5-10 ชม.), (2) forecast accuracy ที่เปลี่ยน, (3) net new pipeline ที่ agent surface ได้จาก signal ที่ manual review หลุด. สำหรับ non-Salesforce enterprise — เริ่ม audit ว่า SaaS ที่ใช้อยู่มี "in-Claude/Copilot/Gemini plugin" หรือยัง — vendor ที่ยังไม่มี in 6 เดือนน่าจะเป็น legacy risk. Thai SMB ที่ใช้ HubSpot/Zoho/Freshworks ควรเช็คว่า vendor มี MCP roadmap ไหม — ถ้าไม่ Claude/ChatGPT enterprise plan จะไม่คุ้มค่าใช้จ่าย

**Ecosystem:** สอง moat ใหม่ที่จะ define agent economy ปี 2027 คือ **skill catalog depth** (จำนวน + คุณภาพของ prebuilt action ที่ agent ใช้ได้) และ **governance protocol compliance** (ปฏิบัติตาม MCP + A2A + agent audit standard). Winner take most — SaaS incumbent ที่ ship plugin ก่อน + skill เยอะกว่า จะ lock enterprise buyer ตลอด renewal cycle ยาว 3-5 ปี. คนที่ปฏิเสธ pattern นี้เพราะกลัว cannibalization จะเจอสภาพเดียวกับ Kodak ต่อ Fujifilm หรือ Blockbuster ต่อ Netflix — ตายเพราะกลัว disrupt ตัวเองก่อน

## Sources
- [Salesforce and Anthropic Announce Claudeforce (Salesforce press release)](https://www.salesforce.com/news/press-releases/2026/08/26/salesforce-and-anthropic-announce-claudeforce/)
- [Salesforce, Anthropic expand partnership as Benioff responds to 'SaaSpocalypse' concerns (CNBC)](https://www.cnbc.com/2026/08/26/salesforce-anthropic-partnership-claudeforce.html)
- [Salesforce just put its entire CRM inside Claude — and says you'll never need its app again (VentureBeat)](https://venturebeat.com/orchestration/salesforce-just-put-its-entire-crm-inside-claude-and-says-youll-never-need-its-app-again)
- [Salesforce, Anthropic partner to deliver Claudeforce (CIO)](https://www.cio.com/article/4214458/salesforce-anthropic-partner-to-deliver-claudeforce.html)
- [Salesforce and Anthropic Launch Claudeforce Enterprise AI Partnership (HPCWire / AIWire)](https://www.hpcwire.com/aiwire/2026/08/27/salesforce-and-anthropic-launch-claudeforce-enterprise-ai-partnership/)

---

## Audio script
วันพฤหัสยี่สิบแปดสิงหา. Salesforce กับ Anthropic ประกาศ Claudeforce. expanded strategic partnership ที่ยัด CRM ทั้งก้อนของ Salesforce เข้าไปใน Claude.

Product แรกชื่อ Salesforce in Claude. เป็น plugin ที่ปล่อย Claude ให้เข้าถึง revenue cycle ทั้งหมด. pipeline. opportunity. forecast. governance rule. ผ่าน MCP interface. มา พร้อม สาม สิบ เจ็ด prebuilt sales skills. meeting prep. deal health review. pipeline review. built โดยสองบริษัท ไม่ใช่ generic prompt wrapper.

Timeline. pilot ลูกค้าเริ่มใช้วันประกาศ. open beta กันยา. ขยายไป service marketing commerce function ไตรมาสสี่. ราคาแบ่งสอง invoice. Salesforce เก็บค่า headless consumption. Anthropic เก็บค่า Claude inference แยก.

Benioff quote สำคัญ. We're bringing together the world's number one AI and number one CRM. Here the UI is the AI. signal ชัดว่า Salesforce ยอมรับว่าลูกค้าจะเลิกเปิด Salesforce Lightning UI เพื่อทำงาน sales รายวัน.

นี่คือ moment ที่ SaaSpocalypse debate เข้ารอบตัดสิน. คำถามที่ค้างมาสองปีคือ AI agent จะ commoditize SaaS UI layer หรือ SaaS incumbent จะยึด data layer ไว้เป็น moat. Benioff เพิ่งตอบด้วยการเดินหมากที่ analyst เรียกว่า radical concession หรือ brilliant judo.

Per user seat license โมเดล pricing ที่หล่อเลี้ยง SaaS มายี่สิบห้าปี เริ่ม lose coherence. เมื่อ user จริง ๆ ที่ทำ action ใน Salesforce กลายเป็น agent ไม่ใช่คน. pricing จะย้ายไปที่ consumption ที่ token.

คู่แข่งต้องตอบใน หกสิบ ถึง เก้าสิบ วัน. Microsoft Dynamics with Copilot น่าจะประกาศที่ Ignite ตุลา. Google Gemini Enterprise Financial Services เพิ่งประกาศ vertical bet ต้องตามด้วย horizontal. OpenAI ที่ยัง proprietary ทั้ง stack จะเจอ pressure หนักสุด.

สำหรับ builders. model นี้เป็น template ของ next gen SaaS distribution. ไม่ใช่ own the UI แต่ own the skills catalog กับ governance layer กับ billing rail. ที่ agent runtime ใครก็ตามต่อได้. skill catalog moat กับ governance protocol compliance คือ moat ใหม่.

สำหรับ Salesforce customer. เริ่ม pilot Salesforce in Claude กับ sales team เล็ก ห้า ถึง สิบ คน ทันที. ก่อน open beta กันยา. วัด time saved. forecast accuracy. net new pipeline ที่ agent surface ได้.

สำหรับ Thai SMB. ที่ใช้ HubSpot Zoho Freshworks. เช็คว่า vendor มี MCP roadmap หรือยัง. ถ้าไม่. Claude หรือ ChatGPT enterprise plan จะไม่คุ้มค่าใช้จ่าย ในหกเดือนข้างหน้า
