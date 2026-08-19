---
date: 2026-08-19
slug: openai-codex-64-percent-enterprise-tokens-agentic-shift
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  Editorial isometric illustration of a corporate token-flow river forking
  in two: the smaller stream labeled "CHAT 36%" pouring into a coffee mug,
  the huge stream labeled "CODEX 64%" pouring into an autonomous robotic
  workshop with saws, welders, and code files being built; a giant OpenAI
  wordmark on the workshop roof; three big floating numbers stacked centre:
  "64% TOKENS", "8.3x FRONTIER GAP", "108x LEGAL GROWTH"; a small "AGENTIC
  EXECUTION" nameplate on the workshop. Editorial magazine style, thick
  outlines, high contrast, readable at 200px thumbnail, 1:1 aspect, no
  real human faces.
image: images/26-08-19-0611-02-openai-codex-64-percent-enterprise-tokens-agentic-shift.png
---

# OpenAI เปิด data ครั้งแรก — Codex กิน 64% ของ enterprise output tokens, frontier firm ใช้ agent มากกว่าค่าเฉลี่ย 8.3 เท่า, การ delegate ชนะ chat แล้ว

## TL;DR
- **13 ส.ค. 2026** — OpenAI ปล่อย **"Enterprise Signal" report** จาก anonymised aggregate data ของลูกค้า enterprise ทั่วโลก
- **ณ เดือน มิ.ย. 2026 Codex สร้าง 64% ของ output tokens รวม Codex + ChatGPT** ในลูกค้า enterprise — ทาง agentic execution กินสัดส่วนใหญ่ที่สุดของ compute จริงแล้ว
- **Frontier firms** (top 10% ของ AI usage) ใช้ output tokens ต่อ active user **8.3x ของ typical firm** ขึ้นจาก 2.6x เมื่อ ม.ค. — ช่องว่างขยาย 3x ในครึ่งปี
- Weekly active Codex users โต **108x ใน legal, 41x ใน sales, 41x ใน recruiting, 26x ใน marketing** เทียบกับ 5x ใน engineering — Codex ไม่ใช่แค่เครื่องมือ dev อีกแล้ว

## เกิดอะไรขึ้น
วันที่ 13 สิงหาคม 2026 OpenAI ปล่อย report ชื่อ *"From assistance to execution: How enterprises put AI to work"* เป็นครั้งแรกที่บริษัทเปิด **anonymised aggregate usage data** ของฐาน enterprise customer พร้อมงานวิจัยชื่อ *"The Shift to Agentic AI: Evidence from Codex"* เขียนโดย Drew Johnston และ David Holtz ที่ผ่าน methodology review ก่อน publish

ตัวเลขเด่นที่วงการ VC และ analyst forward กันทั่วเช้าวันที่ 14 คือ **Codex สร้าง 64% ของ output tokens รวมของ Codex + ChatGPT** ในกลุ่มลูกค้า enterprise เมื่อเดือน มิ.ย. 2026 — และเลข 64% นี้สะท้อน 2 อย่างพร้อมกัน: (1) จำนวนงานที่ delegate ให้ Codex ทำจริงมากขึ้น, และ (2) แต่ละงาน agentic กิน token มากกว่า chat หลายเท่าเพราะเป็น multi-step task ที่ยาวและ recursive. ไม่ใช่แค่ engineer ใช้: **weekly active enterprise Codex users โตตั้งแต่ ก.พ.** — 108x ใน legal, 41x sales, 41x recruiting, 26x marketing เทียบกับ 5x engineering. Codex กลายเป็น general-purpose delegation runtime ไม่ใช่ IDE tool

Report ยังเผย gap ที่น่ากลัวชื่อ **"frontier firm 8.3x"** — บริษัทที่อยู่ top 10% ของ AI usage แต่ละเดือน สร้าง output tokens ต่อ active user มากกว่าค่าเฉลี่ยของ typical firm ถึง 8.3 เท่า, ขึ้นจาก 2.6 เท่าเมื่อ ม.ค. 2026. ช่องว่างขยาย 3 เท่าในครึ่งปี — pattern ที่แปลว่า "AI compound advantage" ไม่ใช่คำโฆษณาอีกแล้ว บริษัทที่เริ่มก่อน + integrate ลึกกำลังเปิด lead อย่างมีนัยสำคัญ

## ทำไมสำคัญ
Report นี้เป็น **first-party evidence** ที่ตอบคำถามที่ทั้งวงการเถียงกันมา 2 ปี — "agentic AI ทำงานจริงในเชิงเศรษฐศาสตร์ไหม?" ที่ผ่านมามีแต่ demo, benchmark, หรือ case study แบบเลือกเชอร์รี. คราวนี้ OpenAI เอาข้อมูล **compute ทั้งฐาน** มาโชว์: token ที่ enterprise จ่ายจริงส่วนใหญ่ **ไม่ใช่ chat แล้ว** — เป็น agentic execution ที่ agent เขียน code, refactor multi-file, รัน test, และ deploy ให้เอง

Pattern ที่เด่นสุดคือ **การ diverge ของ frontier firm** — ถ้า 8.3x gap นี้ยังโตต่อในอัตราครึ่งปีก่อน ปลายปี 2026 อาจแตะ 15-20x. นั่นแปลว่า enterprise "typical" กำลังจะโดน out-execute โดย competitor ที่ประชาสัมพันธ์น้อยแต่ใช้ agent หนักกว่ามาก. เทียบกับ Cognition ที่รายงานว่า **enterprise Devin usage โต 50% ต่อเดือน** ต่อเนื่อง 6 เดือน (ดูใน brief #3 ของรอบนี้) จะเห็นว่า pattern เดียวกันเกิดขึ้นข้าม vendor — agent adoption กำลัง compounding ไม่ใช่ linear

Data ตัว 108x growth ใน legal ก็แปลว่า **coding agent สามารถ generalise ออกจาก code** ได้เร็วกว่าที่คาด — legal work ที่เดิมคิดว่าเป็น chat use case จริง ๆ แล้วเป็น multi-step delegation work (review contract, extract clause, cross-reference precedent, draft revision) ที่ Codex agent runtime ทำได้ดีกว่า pure conversational interface. นี่คือสัญญาณว่า **"coding agent" กำลังกลายเป็น "task agent"** — และผู้ชนะไม่จำเป็นต้องเป็น vertical agent app แต่เป็น horizontal runtime ที่ดีพอ

## มุม AI Agent Platform
สำหรับ **Builders** ที่กำลังสร้าง agent framework: ข้อมูลชุดนี้บอกว่า **UX ของ "delegated task"** (ส่งงานให้ agent ทำ, ไปทำอย่างอื่น, กลับมาดู PR ทีหลัง) มี traction จริงมากกว่า chat UX. Framework ที่มี checkpoint, resumability, human-in-the-loop review at commit เป็น first-class primitive จะมี edge — framework ที่ยัง model เป็น "chat with tools" อยู่ต้อง rethink

สำหรับ **Users / business** ที่ deploy agent: หา metric **"tokens delegated per employee per week"** ของบริษัทตัวเอง แล้วเทียบกับ frontier firm benchmark. ถ้าต่ำกว่า 8x average — คุณอยู่ในกลุ่ม typical firm ที่กำลังจะโดน out-executed. ทางออกไม่ใช่ซื้อ license เพิ่ม แต่ต้อง **redesign workflow** ให้ agent-first: (1) identify งานที่ multi-step + repeatable, (2) หา tool integration ที่ agent ต้องเข้าถึง, (3) วาง review gate ที่ human check เฉพาะ output ไม่ใช่ทุก step. สำหรับ **ecosystem** — vertical agent app (legal, sales) ต้องพิสูจน์ว่าตัวเองดีกว่า Codex + prompt ที่ generalist runtime ให้ได้เยอะพอที่ enterprise จะจ่ายแยก. ช่วง 6-12 เดือนหน้าจะเห็น consolidation รอบใหม่

## Sources
- [From assistance to execution: How enterprises put AI to work — OpenAI](https://openai.com/index/how-enterprises-put-ai-to-work/)
- [OpenAI says 64% of enterprise output tokens come from Codex — DigitalToday](https://www.digitaltoday.co.kr/en/view/92763/openai-says-64-percent-of-enterprise-output-tokens-come-from-codex-frontier-firms-use-8-3-times-more)
- [Enterprise AI Token Spend Shifts From Chat to Agents — BankInfoSecurity](https://www.bankinfosecurity.com/enterprise-ai-token-spend-shifts-from-chat-to-agents-a-32539)
- [The Shift to Agentic AI: Evidence from Codex — OpenAI (PDF)](https://cdn.openai.com/pdf/5d1e1489-21c0-43e4-9d42-f87efdbf0082/the-shift-to-agentic-ai-evidence-from-codex.pdf)

---

## Audio script
วันที่ 13 สิงหาคม OpenAI ปล่อย report ครั้งแรกที่เปิดข้อมูล aggregate ของลูกค้า enterprise ทั่วโลก ชื่อว่า Enterprise Signal และงานวิจัย The Shift to Agentic AI. เลขเด็ดคือ ณ เดือนมิถุนายน Codex สร้าง 64% ของ output tokens รวมของ Codex บวก ChatGPT ในลูกค้า enterprise. แปลว่างานที่ enterprise ให้ AI ทำจริง ๆ ตอนนี้ไม่ใช่ chat แล้ว เป็น agentic execution ที่ agent เขียน code, รัน test, deploy ให้เอง. อีกเลขที่น่าตกใจคือ frontier firm ท็อป 10% ของการใช้ AI ใช้ token ต่อคนมากกว่าค่าเฉลี่ย 8.3 เท่า ขึ้นจาก 2.6 เท่าเมื่อต้นปี ช่องว่างขยาย 3 เท่าในครึ่งปี. Codex ไม่ใช่แค่ tool ของ dev อีกแล้ว weekly active user โตในสายกฎหมาย 108 เท่า sales 41 เท่า recruiting 41 เท่า marketing 26 เท่า เทียบกับ engineering แค่ 5 เท่า. Coding agent กลายเป็น task agent เต็มตัว. คำถามที่ธุรกิจต้องถามคือ token ที่ delegate ให้ agent ต่อพนักงานหนึ่งคนต่อสัปดาห์ของคุณเท่าไหร่ ถ้าต่ำกว่าค่าเฉลี่ยกำลังโดนคู่แข่งเปิด lead ทิ้งไปเรื่อย ๆ.
