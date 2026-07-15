---
date: 2026-07-15
slug: china-anthropomorphic-ai-doubao-qwen-shutdown
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  A vast red concrete plaza at dusk with a single glowing office window
  labeled "AGENT". Above, three stacked block-letter headlines float in
  the sky: "345M USERS", "READ-ONLY MODE", "JULY 15, 2026". A hand-shaped
  silhouette pulls a giant power switch marked "ANTHROPOMORPHIC AI" toward
  OFF. Editorial isometric style, high contrast, 1:1 aspect, no real human
  faces, readable at 200px thumbnail.
image: images/26-07-16-0611-01-china-anthropomorphic-ai-doubao-qwen-shutdown.png
---

# วันที่จีนดึงปลั๊ก AI Agent: Doubao กับ Qwen ต้องปิดฟีเจอร์สร้าง agent ตามกฎหมายใหม่

## TL;DR
- **15 กรกฎาคม 2026** — ByteDance's Doubao (345M MAU) และ Alibaba's Qwen ปิดฟีเจอร์สร้าง AI agent แบบ humanlike ตาม *Interim Measures for the Administration of Anthropomorphic AI Interaction Services* ของ CAC
- Agent ที่ users สร้างไว้ทั้งหมด **หยุดทำงาน**; view ได้ถึง 15 ตุลาคม แล้ว data ถูกลบตาม privacy policy
- นี่คือกฎ agent-specific ตัวแรกของโลกระดับ national — signal ว่าจีนจะเป็น testing ground ของ agent governance ก่อน EU AI Act's agent provisions มีผล

## เกิดอะไรขึ้น

วันนี้ (15 กรกฎาคม 2026) Doubao — แอป AI ที่ใหญ่ที่สุดของจีนด้วย 345 ล้าน monthly active users — และ Qwen ของ Alibaba พร้อมใจกันปิดฟีเจอร์ "AI agent creation" ในฝั่ง consumer. ผู้ใช้ที่เคยสร้าง persona agent ไว้ตอบแชท คุยเป็นเพื่อน หรือเล่นบทบาทสมมติ จะเห็นแค่ **read-only view** ของ agent configuration และ chat history เท่านั้น ตัว agent เองไม่ตอบกลับอีกแล้ว. ตั้งแต่ 15 ตุลาคม 2026 เป็นต้นไป data จะถูกจัดการตาม privacy policy ปกติ — หมายความว่าลบทิ้ง

ตัวขับคือ *Interim Measures for the Administration of Anthropomorphic AI Interaction Services* ที่ Cyberspace Administration of China ร่วมกับอีก 4 หน่วยงาน (NDRC, MIIT, กระทรวงตำรวจ, SAMR) ประกาศตั้งแต่ 10 เมษายน 2026 — คลุมทั้ง AI companion, emotional support agent, และ virtual intimate relationships โดยเฉพาะที่เกี่ยวกับผู้เยาว์. ByteDance กับ Alibaba เลือก "แม่นย" — ปิดทั้ง feature แทนที่จะเสี่ยง compliance กระท่อนกระแท่น เพราะบทลงโทษภายใต้กฎ CAC ไม่เคย proportional กับ mistake

น่าสังเกตคือ enterprise agent ไม่ถูกกระทบ. ทั้ง ByteDance's Volcano Engine และ Alibaba Cloud ยังคง sell agent-building platform ให้ B2B customer ต่อ — ตัดเฉพาะ consumer-facing agent ที่ CAC มองว่าเสี่ยง "emotional manipulation". เท่ากับว่าจีน (โดยพฤตินัย) แยก tier ของ agent regulation แล้ว: **B2B ผ่อน B2C คุม**

## ทำไมสำคัญ

นี่คือครั้งแรกที่รัฐบาลระดับ national ออกกฎเฉพาะสำหรับ AI agent (ไม่ใช่ LLM ทั่วไป) และ enforce ด้วยการบังคับให้ platform ยักษ์ปิด feature จริง ๆ. EU AI Act's high-risk provisions ยังไม่ครอบคลุม agentic autonomy อย่างชัดเจน. California SB 53 ที่พูดเรื่อง frontier model ก็เน้น training compute ไม่ใช่ agent behavior. จีนกระโดดขึ้นนำในการเขียนกฎเฉพาะ agent — และตัวกฎ (companion, emotional manipulation, minors) ก็ตรง failure mode ที่ ChatGPT, Character.AI และเคสฟ้อง OpenAI ในอเมริกากำลังเผชิญ

pattern ที่เห็นคือ **regulatory speed asymmetry** — จีนออกกฎ 3 เดือนแล้วบังคับใช้ทันที (10 April → 15 July) ในขณะที่ US ยังอยู่ในขั้น executive order / state bill. สำหรับ agent builder ที่ ambition คือ global scale นี่แปลว่าต้องออกแบบ compliance layer แบบ region-first ตั้งแต่วันแรก เหมือน data residency ใน SaaS ยุค 2015 — แต่บนเลเยอร์ที่ยากกว่ามาก เพราะ agent behavior แปรผันตาม prompt กับ tool

signal ที่ตามมาน่าจะเป็น: (1) EU ตามด้วย agent-specific delegated act ภายในสิ้นปี, (2) US state (California, Colorado) ออก companion AI bill ตาม, (3) enterprise agent platform เริ่มมี "regulatory mode" toggle ที่บังคับ persona neutrality + audit log อัตโนมัติ

## มุม AI Agent Platform

**Builders**: ถ้าคุณสร้าง agent framework หรือ runtime สาย consumer/companion — ต้องเพิ่ม "compliance primitives" เป็น first-class: persona locking, disclosure banner ("You are talking to AI"), age gating, emotional pattern detection. คนที่ launch ในจีน / EU ต้องเลือกระหว่าง SKU แยกกับ policy engine ที่ปรับได้แบบ per-region. **Users / business**: ธุรกิจไทยที่ deploy chatbot บน LINE / Facebook ที่มี "personality" ต้องเริ่มคิดว่าถ้ากฎ ETDA / กสทช. ตามจีนมา (ซึ่งไทยชอบตาม) จะเสียแค่ persona layer หรือทั้ง flow. **Ecosystem**: Volcano Engine กับ Alibaba Cloud น่าจะได้ประโยชน์ในระยะยาว — B2B agent tooling อยู่รอด, ส่วน consumer competitor (Kimi, Zhipu) ต้อง reshape product ทั้งหมด. นี่คือครั้งแรกที่ **agent governance** กลายเป็น market-shaping force จริง ไม่ใช่แค่ conference panel

## Sources
- [ByteDance's Doubao and Alibaba's Qwen to shut down AI agent features on July 15 — TechNode](https://technode.com/2026/07/06/bytedances-doubao-and-alibabas-qwen-to-shut-down-ai-agent-features-on-july-15/)
- [China AI Companion Law Takes Effect: Doubao and Qwen Shut Down — TechTimes](https://www.techtimes.com/articles/320525/20260715/china-ai-companion-law-takes-effect-doubao-qwen-shut-down-millions-lose-chat-data.htm)
- [ByteDance and Alibaba to disable humanlike AI custom agents as new rules loom — SCMP](https://www.scmp.com/tech/big-tech/article/3359482/bytedance-and-alibaba-disable-humanlike-ai-custom-agents-new-rules-loom)
- [China's AI companion rules force Doubao, Qwen shutdowns — The Next Web](https://thenextweb.com/news/china-humanlike-ai-agent-rules)

---

## Audio script
สวัสดีครับ วันนี้ 15 กรกฎาคม 2026 มีข่าวใหญ่จากฝั่งจีนที่ทุกคนที่ทำ AI Agent ควรฟัง. ByteDance กับ Alibaba สั่งปิดฟีเจอร์สร้าง AI agent ในแอป Doubao กับ Qwen พร้อมกันวันนี้ ตามกฎหมายใหม่ที่ชื่อ Interim Measures for Anthropomorphic AI Interaction Services ของ Cyberspace Administration of China. Doubao มีคนใช้ 345 ล้านคนต่อเดือน คุณลองนึกภาพ user ที่สร้าง agent เป็นเพื่อน เป็นคู่คุย เป็น role-play persona ไว้ทั้งหมด วันนี้เปิดขึ้นมาเจอแค่หน้า read-only ตัว agent ตอบไม่ได้อีกแล้ว. ตั้งแต่ 15 ตุลาคม data จะถูกลบทั้งหมด. ที่น่าสนใจคือ enterprise agent ไม่โดน — Volcano Engine กับ Alibaba Cloud ยังขาย B2B agent tooling ต่อได้ปกติ จีนเลยเป็นชาติแรกที่แยก tier ของ agent regulation อย่างชัดเจนว่า B2B ผ่อน B2C คุมเข้ม. สำหรับคนที่สร้าง agent platform ในไทย นี่คือ signal สำคัญ ว่ากฎเฉพาะ agent (ไม่ใช่ LLM ทั่วไป) กำลังมา และมันจะเน้น consumer-facing เป็นหลัก — เตรียม compliance primitive แบบ persona locking, disclosure banner, age gate ไว้ตั้งแต่วันนี้ดีกว่าไปเจอตอนตลาดปิดครับ
