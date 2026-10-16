---
date: 2026-10-16
slug: meta-muse-wonder-enterprise
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: |
  A massive dark Meta-blue monolith with the word "WONDER" etched in
  silver, surrounded by three glowing orbs labeled "ACTIVE MEMORY",
  "ACTIVE FOCUS", and "ENTERPRISE". A hesitant corporate briefcase at the
  foot of the monolith shows a yellow warning symbol labeled "TRUST GAP".
  Across the top, floating price tags read "$4 / $20". Editorial
  isometric style, cold Meta-blue with cautionary amber highlights, 1:1
  aspect, no real human faces.
image: images/26-10-16-0615-04-meta-muse-wonder-enterprise.png
---

# Meta Muse Wonder: Zuckerberg เข้า enterprise agent — แต่มี trust gap ต้องข้าม

## TL;DR
- Meta เปิด **Muse Wonder** และ **Wonder Full** วันที่ 12 ต.ค. — frontier model สำหรับ agentic task, feature เด่น **Active Memory** (ข้าม conversation) + **Active Focus** (recovery จาก multi-step error)
- Independent Artificial Analysis ให้ **Wonder Full ที่ 56** ใกล้ Claude Sonnet 5.5, ต่ำกว่า Claude Opus 5.5 (58)
- Zuckerberg ตั้ง **Meta Enterprise Platform** นำโดย CJ Desai (อดีต CEO MongoDB) — Meta Business Agent, Muse API, Muse Code เข้า B2B

## เกิดอะไรขึ้น

วันจันทร์ที่ 12 ต.ค. Meta ประกาศ Muse Wonder และ Muse Wonder Full ซึ่งเป็น model ที่ Meta describe ว่า "most capable for personal and professional agent work" Wonder เปิดผ่าน Meta Model API และ Muse Code ส่วน Wonder Full จำกัดเฉพาะ Muse Code subscriber Feature หลักสองตัวคือ **Active Memory** ที่ให้ agent เก็บ context ข้าม session ได้ (คล้ายกับที่ Anthropic และ OpenAI พยายามแก้ด้วย memory API ตั้งแต่กลางปี) และ **Active Focus** ที่ให้ agent recovery จาก multi-step error โดยไม่ต้อง rollback ทั้ง task

ที่น่าสนใจกว่า model คือ Zuckerberg เลือกเปิด **Meta Enterprise Platform** พร้อมกัน และดึง CJ Desai อดีต CEO MongoDB มานำ platform ตัวนี้จะรวม Muse Agent (consumer), Meta Business Agent, Muse API, และ Muse Code ไว้ใต้ sales motion เดียว ซึ่งเป็นครั้งแรกที่ Meta ลงมาเล่น B2B seriously หลังจากพยายามหลายรอบใน workplace era ที่ล้มเหลว

ด้าน benchmark: Artificial Analysis (third-party eval) ให้ Wonder Full ที่ score 56 ใกล้ Claude Sonnet 5.5 แต่ต่ำกว่า Claude Opus 5.5 ที่ 58 Meta ปล่อย internal scorecard ของตัวเองที่โชว์ Wonder Full ชนะใน long coding + legal agent task — ซึ่งเป็น framing ที่น่าสังเกต (เลี่ยง general reasoning benchmark) ส่วนราคา Spanish source รายงานที่ **$4/$20 ต่อ 1M token** ซึ่งเท่ากับ Gemini Argon standard rate พอดี

## ทำไมสำคัญ

Meta อยู่ในตำแหน่งลำบาก — Llama ยังเป็น open-weight ที่คนใช้เยอะที่สุด แต่ ARR แบบ enterprise อยู่ที่ประมาณศูนย์ ขณะที่ Anthropic, OpenAI, Google ขาย enterprise API เป็นหลัก การเปิด Muse Wonder คือ Meta พยายามย้ายจาก "model company ที่ไม่เก็บเงินตรง" ไปเป็น "platform company" โดยอาศัย memory + focus feature เป็นจุด differentiation ที่ไม่ overlap กับคู่แข่ง

ปัญหาคือ **trust gap** ที่ AI Business ชี้: enterprise ส่วนใหญ่ไม่เชื่อ Meta ในฐานะ data custodian (จาก Cambridge Analytica, workplace privacy fine, ad targeting) — ซึ่งเป็นเหตุผลที่ Meta ดึง CJ Desai (คนจาก enterprise world จริง ๆ) มาแทนที่จะส่ง insider ของตัวเองไป ความสำเร็จของ platform นี้จึงไม่ได้ขึ้นกับ model benchmark แต่ขึ้นกับว่า Desai จะ clean brand enterprise ของ Meta ได้แค่ไหน

**Pattern ที่น่าจับตา**: ทุกเจ้าใน frontier model ตอนนี้ (Google, Anthropic, Meta) กำลัง pivot จาก model-as-product ไปที่ platform-as-product ภายในไตรมาสเดียวกัน ซึ่งแปลว่า pricing power ของ frontier model เริ่มลดลง — ต้องขาย orchestration/memory/tool layer เพิ่ม

## มุม AI Agent Platform

สำหรับ **builder** feature Active Memory ของ Wonder เป็นสัญญาณว่า memory layer จะกลายเป็น commodity ของ model — ถ้ากำลัง build memory service แยก (Mem0, Zep, Letta) ต้องชัดเจนว่า differentiation อยู่ตรงไหน Active Focus (error recovery) อาจเป็น primitive ที่น่าสนใจกว่าสำหรับ advanced builder เพราะ orchestrator ส่วนใหญ่ยังทำแบบ naive retry อยู่

สำหรับ **business** ที่กำลังเลือก agent platform ให้ชั่งน้ำหนัก trust cost อย่างจริงจัง — Meta ให้ราคาและ feature คุ้ม แต่ data governance team อาจไม่อนุมัติ จุดสังเกตคือ Muse Code สำหรับ enterprise code migration อาจเป็น beachhead ที่ Meta ชนะได้ก่อน (เพราะ code migration ไม่ใช่ sensitive data)

สำหรับ **ecosystem** การที่ Meta ขยับหมายความว่า B2B agent market จะมีคู่แข่ง major 4 ราย (OpenAI, Anthropic, Google, Meta) + หลาย specialist (Nous, Mistral) — pricing จะกดลงอีกใน Q4 นี้

## Sources
- [Meta joins enterprise agent race with Muse Wonder, facing a trust gap](https://aibusiness.com/agentic-ai/meta-joins-enterprise-agent-race-with-muse-wonder)
- [Meta Enters AI Frontier With New "Wonder" Models](https://propakistani.pk/2026/10/13/meta-enters-ai-frontier-with-new-wonder-models/)
- [Meta Launches Muse Wonder and Muse Wonder Full for Agentic Tasks](https://letsdatascience.com/news/meta-launches-muse-wonder-and-muse-wonder-full-for-agentic-t-41113cca)

---

## Audio script
วันจันทร์ที่ 12 ต.ค. Meta ประกาศ Muse Wonder และ Wonder Full ซึ่งเป็น frontier model สำหรับ agentic task Meta บอกว่าเป็น model ที่สามารถที่สุดสำหรับงาน agent ทั้ง consumer และ enterprise feature เด่นคือ Active Memory ที่ให้ agent เก็บ context ข้าม session ได้ และ Active Focus ที่ให้ agent recovery จาก multi-step error โดยไม่ต้อง rollback ทั้ง task

Independent Artificial Analysis ให้ Wonder Full ที่คะแนน 56 ใกล้ Claude Sonnet 5.5 แต่ต่ำกว่า Claude Opus 5.5 ที่ 58 ที่น่าสนใจกว่า model คือ Zuckerberg เปิด Meta Enterprise Platform พร้อมกัน และดึง CJ Desai อดีต CEO MongoDB มานำ นี่เป็นครั้งแรกที่ Meta ลงมาเล่น B2B seriously หลังพยายามหลายรอบใน workplace era ที่ล้มเหลว

ปัญหาที่น่าจับตาคือ trust gap AI Business ชี้ว่า enterprise ส่วนใหญ่ไม่เชื่อ Meta ในฐานะ data custodian จากประวัติ Cambridge Analytica และ ad targeting ความสำเร็จจึงไม่ได้ขึ้นกับ benchmark แต่ขึ้นกับว่า Desai จะ clean brand enterprise ของ Meta ได้แค่ไหน

สำหรับทีมที่ทำ memory service แยกอยู่อย่าง Mem0 หรือ Letta ต้องทบทวนว่า differentiation อยู่ตรงไหน เพราะ memory layer กำลังจะกลายเป็น commodity ของ model สำหรับ business ที่เลือก agent platform ให้ชั่งน้ำหนัก trust cost อย่างจริงจัง Meta ให้ราคาคุ้มกว่า แต่ data governance team อาจไม่อนุมัติ ภาพรวม pricing ของ frontier model จะกดลงอีกใน Q4 นี้
