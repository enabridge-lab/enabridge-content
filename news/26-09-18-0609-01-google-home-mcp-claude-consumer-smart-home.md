---
date: 2026-09-17
slug: google-home-mcp-claude-consumer-smart-home
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  A cutaway isometric editorial illustration of a modern smart home. Inside,
  a glowing purple orb marked "CLAUDE" and a green orb marked "HERMES" reach
  through the roof like agents entering through a portal labeled
  "GOOGLE HOME MCP". On living-room walls, big neon signs read
  "MCP = SMART HOME PROTOCOL", "US ONLY / $20/MO", and "DOORS = LOCKED".
  A silhouette on the sofa watches a floating dashboard showing camera feeds
  and laundry status. Editorial isometric style, deep navy and google-red
  palette with amber highlights, 1:1 aspect, no real human faces.
image: images/26-09-18-0609-01-google-home-mcp-claude-consumer-smart-home.png
---

# Google เปิด Home API ให้ Claude / Hermes / OpenClaw คุมบ้าน — MCP กลายเป็น consumer protocol ตัวแรกที่มี hyperscaler backing

## TL;DR
- วันนี้ (17 ก.ย.) Google เปิด **Google Home MCP** ให้ third-party AI agent (Claude, Google Antigravity, Hermes, OpenClaw) เข้าถึงและควบคุมอุปกรณ์ smart home ผ่านมาตรฐาน Model Context Protocol
- Early access เฉพาะ **Google Home Premium Advanced** ($20/เดือน หรือ $200/ปี) ใน US เท่านั้น — ยังบล็อก sensitive action (ปลดล็อกประตู) และให้ผู้ใช้ revoke ได้
- Setup ต้อง Google Cloud project + Home API + OAuth — ไม่ใช่ one-click แต่เปิดทาง developer สร้าง cross-camera dashboard, device history analytics, voice reply ผ่านลำโพง Google Home

## เกิดอะไรขึ้น

Google เดิน move ที่ 2 ปีก่อนคงทำไม่ได้ — **เปิดบ้านของลูกค้า Nest ให้ Anthropic เข้ามาคุม**. วันนี้ที่ blog post ของ Google Home team ประกาศ **Google Home MCP early access** — third-party AI agent อย่าง Claude, Google Antigravity, Hermes และ OpenClaw จะเชื่อม Nest camera, Google Home speaker, สมาร์ทหลอดไฟ, thermostat ผ่าน MCP server ที่ Google host ให้ ไม่ต้องเขียน integration แยกต่อยี่ห้อ

Feature ที่ pitched ตอนเปิดตัว: **cross-camera analysis** ("มีแมวเข้าสวนตอนไหน?"), **device state history** ("เครื่องซักผ้าเสร็จเมื่อไหร่?"), **voice output** — เมื่อ agent จบงาน มันสั่ง Google Home ลำโพงพูดกลับใน household ได้ด้วย. ตัวอย่างที่ Anthropic demo ในคลิปคือ: user พิมพ์ใน Claude Desktop "ช่วยดูว่าลูกกลับบ้านหรือยัง แล้วเปิดไฟทางเดินให้ด้วย" — Claude ดึงเช็ค activity feed ของ Nest Doorbell, เห็นว่ามีคนเข้าประตูตอน 3:47 PM, แล้วเรียก `set_light` MCP tool ให้เปิดไฟ

จุด friction ที่ Google ยัง gate อยู่ก็มี. Rollout **US only** ที่ **Home Premium Advanced tier** ($20/เดือน หรือ $200/ปี — ก่อนหน้านี้เป็น Gemini-only tier); setup ยังต้อง Google Cloud project + Home API key + OAuth flow. Sensitive action (ปลดล็อกประตู, disarm alarm) ถูก hard-block ที่ protocol layer แม้ agent จะขอ tool นั้น. ผู้ใช้ revoke access agent ตัวไหนก็ได้จาก Google Home app — audit log ครบ

Timing ก็สำคัญ. AGNTCon + MCPCon Europe จัดพรุ่งนี้ที่ Amsterdam (17-18 ก.ย.) โดย David Soria Parra (co-creator MCP จาก Anthropic) เป็น keynote — Google ประกาศ **สองวันก่อนงาน** เป็น signal ชัด ๆ ว่า MCP ไม่ใช่ open standard ของ Anthropic คนเดียวอีกแล้ว. เมื่อเดือนที่แล้ว Anthropic donate MCP ให้ Linux Foundation ผ่าน Agentic AI Foundation (AAIF) — Anthropic, Block, OpenAI ร่วมก่อตั้ง; Google adopt เข้ามาในสัปดาห์นี้ = tipping point ของ protocol governance

## ทำไมสำคัญ

MCP จนถึงเมื่อเดือนที่แล้วเป็น **developer protocol** — 17,000+ MCP server ใน registry, 70% ของ MCP consumer มี 2-7 server ต่อ environment. แต่ทุกคนที่ใช้เป็น **B2B**: dev tools, enterprise data pipeline, internal automation. Google move นี้เป็นครั้งแรกที่ **consumer surface ของ hyperscaler เปิดให้ MCP** — Nest + Google Home มี install base ~150M อุปกรณ์ทั่วโลก แม้ US-only ใน early access, บ้านที่ agent เข้าไปคุมได้ก็เป็นหลัก 10-ล้าน overnight

Pattern ที่เห็น 30 วันหลัง: Adobe (CX Enterprise Coworker บน MCP), Databricks (Unity AI Gateway บน MCP), Microsoft (Agent Framework 1.18 + MCP history), Docusign (MCP Server GA ครบ agreement layer), และตอนนี้ Google Home. **MCP ถูก build เข้า distribution layer ของ vendor ที่มี user base ใหญ่ที่สุด**. คำถาม 6 เดือนก่อนคือ "MCP จะชนะ A2A ไหม?" — คำถามวันนี้คือ "อะไรที่ **ไม่พูด MCP** ในปี 2027 จะรอดไหม?"

จุดที่ต้องจับตาถัดไปคือ **Apple**. HomeKit + Siri เป็น walled garden ที่สุดใน category smart home; Apple ยังไม่ประกาศ MCP support ใด ๆ. หลังจาก WWDC เดือนมิถุนายนที่โชว์ Apple Intelligence agent แต่ปิดไม่ให้ third-party — ถ้า Apple ยังยืน single-vendor stack ต่อ ในขณะที่ Google เปิด, พฤติกรรมผู้ใช้ smart home ระดับ prosumer อาจไหลไป Google. **Prosumer smart home = high-margin customer** ที่ Apple ไม่อยากเสีย

## มุม AI Agent Platform

สำหรับ **builders**: consumer MCP surface ใหม่ทั้ง category. ใครที่สร้าง home routine agent, family scheduler, ambient security monitor — ตอนนี้เขียน MCP client ต่อกับ Google Home ได้แล้วโดยไม่ต้อง reverse-engineer Nest cloud API. **User acquisition path ใหม่**: agent ที่มี "install ผ่าน Google Home app" จะ discovery ง่ายกว่า launch เป็น mobile app ใหม่.

สำหรับ **users / business**: business ที่ขาย smart-home service (property management, senior care, insurance monitoring) — เดิมต้อง integrate Nest + Ring + SmartThings แต่ละอันเอง; ตอนนี้เขียน agent ทีเดียวใช้กับบ้านลูกค้าทุกหลังที่มี Google Home Premium. Insurance underwriter สามารถขอ agent วิเคราะห์ door lock activity เพื่อ discount premium — พร้อม audit trail จาก MCP log

สำหรับ **ecosystem**: Alexa/Ring (Amazon) และ HomeKit (Apple) โดนบีบให้ตัดสินใจในเดือนหน้า — เปิด MCP หรือรักษา walled garden. Bet: Amazon เปิดก่อน (มี AWS MCP infrastructure พร้อม), Apple ตามช้าอีก 12 เดือน. สำหรับผู้ผลิต hardware smart home ทั่วไป (Yale, Philips Hue, Ecobee) — เขียน MCP tool เป็นทางลัดที่จะเสียบเข้า agent ecosystem ทั้งหมดพร้อมกัน โดยไม่ต้องรอ Alexa/HomeKit certification รอบใหม่

## Sources
- [Your Google Home can now take orders from Claude and other AI agents — Digital Trends](https://www.digitaltrends.com/home/google-home-mcp-ai-agents-smart-home/)
- [Google opens Home ecosystem to third party AI agents through MCP — Crypto Briefing](https://cryptobriefing.com/google-home-mcp-ai-agents/)
- [Google Home MCP lets AI agents control smart homes — TBreak](https://tbreak.com/google-home-mcp-ai-agents-smart-home/)
- [Google just made a huge smart home move — Tom's Guide](https://www.tomsguide.com/ai/google-just-made-a-huge-smart-home-move-and-its-good-news-for-claude-ai-fans)

---

## Audio script
วันนี้ Google เปิดบ้านของลูกค้า Nest ให้ AI agent อื่นเข้ามาคุม ผ่านมาตรฐานที่เรียกว่า Google Home MCP. Claude ของ Anthropic, Antigravity ของ Google เอง, Hermes, OpenClaw — สี่ agent นี้เป็นล็อตแรกที่ต่อเข้ากับ Nest camera, ลำโพง Google Home, ไฟ, thermostat ได้เลย โดยไม่ต้องเขียน integration แยกยี่ห้อ. Early access เฉพาะสหรัฐ ต้องจ่าย Google Home Premium Advanced ยี่สิบเหรียญต่อเดือน — ยัง gate อยู่ แต่ signal ชัด. ที่น่าสนใจคือ Google ประกาศสองวันก่อนงาน AGNTCon plus MCPCon Europe ที่ Amsterdam ซึ่ง David Soria Parra ผู้ co-create MCP จาก Anthropic เป็น keynote. เมื่อเดือนที่แล้ว Anthropic เพิ่ง donate MCP ให้ Linux Foundation ผ่าน Agentic AI Foundation ที่ Anthropic, Block, OpenAI ร่วมก่อตั้ง — วันนี้ Google เข้าร่วม adopt ที่ consumer layer. หกเดือนก่อนเราถามว่า MCP จะชนะ A2A ไหม — ตอนนี้คำถามเปลี่ยนเป็น อะไรที่ไม่พูด MCP ในปี 2027 จะรอดไหม. ต่อไปจับตา Apple. HomeKit เป็น walled garden ที่สุดใน smart home; ถ้ายังไม่เปิดเดือนหน้า prosumer จะไหลไป Google เยอะ. สำหรับ builder ที่สร้าง home routine agent, family scheduler, senior care monitor — เขียน MCP client ทีเดียวใช้กับบ้านลูกค้าทุกหลังได้แล้ว. User acquisition path ใหม่เกิดขึ้นวันนี้.
