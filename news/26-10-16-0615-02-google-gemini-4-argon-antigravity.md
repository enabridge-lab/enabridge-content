---
date: 2026-10-16
slug: google-gemini-4-argon-antigravity
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: |
  A giant price-tag floating over a futuristic Google-colored datacenter;
  the tag reads "$2 / $10" in massive glowing numbers, with a smaller
  shadow tag behind showing "$4 / $20". In the foreground, a cracked
  gravestone labeled "GEMINI CODE ASSIST" leans against a shining
  monolith reading "ANTIGRAVITY". Editorial isometric style, cold blue
  and warm sodium-amber contrast, 1:1 aspect, no real human faces.
image: images/26-10-16-0615-02-google-gemini-4-argon-antigravity.png
---

# Gemini 4 Argon: Google ตั้งราคา agent model ต่ำกว่า Astra ครึ่งหนึ่ง + ฆ่า Code Assist

## TL;DR
- **Gemini 4 Argon** โฟกัส long-running agent — output token limit โตจาก 64K เป็น 1M, promo pricing $2/$10 ต่อ 1M token (standard $4/$20)
- Google หยุดขาย **Gemini Code Assist** subscription ใหม่ ไล่ลูกค้า enterprise ไปใช้ **Antigravity** platform แทน
- สัญญาณราคาที่ดุ: index task บน Argon ทำได้ที่ 61% ของต้นทุน Astra ในช่วง promo — Google กำลังพยายามซื้อ market share ด้วย token economics

## เกิดอะไรขึ้น

สัปดาห์นี้ Google ขยับสองเรื่องพร้อมกัน หนึ่งคือเปิด **Gemini 4 Argon** ซึ่งเป็น model ตัวใหม่ที่ออกแบบมาเฉพาะทางสำหรับ agentic workload ยาว — code migration, enterprise research, long-horizon planning Google ตั้งราคา promo ที่ $2 ต่อ 1M input token และ $10 ต่อ 1M output token แล้วประกาศไว้ล่วงหน้าว่า standard rate หลังจบ promo จะเป็น $4 และ $20 (ยังไม่บอกวันหมดอายุ) จุดขายสำคัญคือ **output token limit โตเป็น 1 ล้าน token** จากเดิม 64K — ทำให้ agent run ยาว ๆ ไม่ต้องกลัวโดนตัดกลางทาง (บาง source อย่าง OpenCode รายงานเลขที่ 66K ซึ่งขัดแย้ง — ต้องเช็ค Google อีกครั้ง)

สองคือ Google หยุดรับ subscription ใหม่สำหรับ **Gemini Code Assist** ลูกค้า enterprise ที่สอบถามถูก redirect ไป **Antigravity** ซึ่งเป็น agentic development platform ที่ Google เพิ่งเปิดเต็มรูปแบบ นี่คือการบีบเลือกครั้งใหญ่: ลูกค้าที่เคยซื้อ Gemini เป็น autocomplete AI assistant ต้องยอมอัปเกรดไปที่ platform ที่คิดเงินแบบ task-based แทน seat-based

การผสมสองเรื่องนี้บอกเล่า bet ของ Google อย่างชัด — จ่าย Astra สูงสำหรับ chat/reasoning และจ่าย Argon ต่ำสำหรับ long-running agent คือยอมรับว่า economics ของ "AI copilot" กับ "AI employee" ไม่เหมือนกัน Antigravity ก็เลยไม่ขายเป็น seat แต่ขายเป็น task

## ทำไมสำคัญ

ปีที่แล้ว pricing war ของ model API อยู่ที่หน่วย per-token เฉย ๆ — ใครต่ำกว่าใครก็ชนะ แต่ Argon กับ Antigravity เปิด pattern ใหม่: **tiered model ตามประเภทงาน** + **task-based platform billing** คือ Google ยอม cannibalize ตัวเอง เพราะเห็นว่า agent workload โตเร็วกว่า chat workload มาก และตั้ง price point ให้ enterprise รู้สึก "ปลอดภัย" ที่จะรัน agent ทิ้งค้างคืน

Promo $2/$10 ไม่ใช่เรื่องเล่น ๆ — Anthropic กำลังขาย Claude Sonnet 5.5 สำหรับ long-context agent ที่ $3/$15 และ Claude Opus 5.5 ที่ $15/$75 ถ้า Argon ไปถึง quality ใกล้เคียง Sonnet ได้ Google จะกวาด price-sensitive agentic customer ที่ build long-horizon workflow (เช่น batch research, migration, data pipeline agent) ก่อนที่ Anthropic จะมีเวลาตอบ

## มุม AI Agent Platform

สำหรับ **builder** นี่คือสัญญาณให้ทบทวน model selection logic ใน orchestrator — ถ้ายังใช้ model เดียวสำหรับทั้ง tool-calling, planning, และ long-running task คุณกำลังจ่ายเกินจริงอยู่ Argon จะทำให้ pattern "cheap model for the long tail, expensive model for critical reasoning" ได้ ROI มากขึ้น สำหรับ **business** ที่ deploy agent — รีบคำนวณใหม่ว่า workflow ไหนที่เคย "แพงเกินไป" (เช่น nightly research agent, document migration) ตอนนี้คุ้มรันหรือยัง

สำหรับ **ecosystem** การตัด Gemini Code Assist คือ signal ที่น่ากลัวสำหรับ pure-copilot vendor (Cursor, Windsurf, Cognition) — Google กำลังบอกว่า autocomplete ไม่ใช่ product แล้ว แต่เป็น feature ของ agent platform Antigravity จะเป็นคู่แข่งโดยตรงกับ Devin และ Claude Code ในระดับ enterprise

## Sources
- [Gemini 4 Argon pricing: the $2/$10 promo, the $4/$20 bill](https://www.eesel.ai/blog/gemini-4-argon-pricing)
- [Google prices Gemini 4 Argon at $2 per million tokens](https://ppc.land/google-prices-gemini-4-argon-at-2-per-million-tokens-paid-users-only/)
- [Gemini 4 Argon's $2/$10 Price Is Half the Later Rate](https://fourweekmba.com/ai-gemini-4-argon-introductory-price-footnote-4-20/)

---

## Audio script
สัปดาห์นี้ Google ขยับสองเรื่องพร้อมกันในเรื่อง agentic AI หนึ่งคือเปิด Gemini 4 Argon model ตัวใหม่ที่ออกแบบมาสำหรับ agent ที่รันงานยาว ๆ เช่น code migration หรือ enterprise research จุดขายคือ output token limit โตจาก 64K เป็น 1 ล้าน token และตั้งราคา promo แค่ 2 ดอลลาร์ต่อ 1 ล้าน input token กับ 10 ดอลลาร์ต่อ output token

สองคือ Google หยุดขาย Gemini Code Assist subscription ใหม่ ลูกค้า enterprise ที่สนใจถูกไล่ไปที่ Antigravity ซึ่งเป็น agentic development platform ที่คิดเงินแบบ task-based แทน seat-based ที่น่าสนใจคือ Google ยอม cannibalize product ของตัวเองเพื่อย้ายลูกค้าไปโมเดลธุรกิจใหม่

ที่น่าจับตาคือ pattern นี้บอกว่า pricing war ของปีที่แล้วที่แข่งกัน per-token อย่างเดียวจบไปแล้ว ตอนนี้เป็น tiered model ตามประเภทงานบวกกับ task-based platform billing สำหรับทีม builder ของเรา นี่คือสัญญาณให้ทบทวน model selection logic ใน orchestrator ถ้ายังใช้ model เดียวสำหรับทุก workload อยู่ก็กำลังจ่ายเกินจริง สำหรับ business ที่ deploy agent รีบคำนวณใหม่ว่า workflow ไหนที่เคยคิดว่าแพงเกินไป ตอนนี้คุ้มรันหรือยัง และสำหรับ pure copilot vendor อย่าง Cursor หรือ Windsurf นี่คือ signal ที่น่ากลัวมาก เพราะ Google กำลังบอกว่า autocomplete ไม่ใช่ product แล้ว แต่เป็นแค่ feature ของ agent platform
