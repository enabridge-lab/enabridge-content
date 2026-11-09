---
date: 2026-11-10
slug: anthropic-dreaming-agent-memory
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a sleeping AI agent inside a glowing
  translucent dome, with cross-sections of its "notebook" being rewritten by
  tiny labeled modules: "NOTES", "FACTS", "WIKI LINKS". Above the dome, a
  large panel shows a graph rising from "73%" to "87%" labeled "COMPLEX
  RESEARCH TASK". Soft purple and warm orange palette, clean editorial
  style, 1:1 aspect, no real human faces (silhouettes OK), high contrast so
  numbers stay readable at 200px thumbnail.
image: images/26-11-10-0605-01-anthropic-dreaming-agent-memory.png
---

# Anthropic เปิดงานวิจัย "Dreaming" — agent นอนหลับแล้วจัด memory เองออฟไลน์, ดันคะแนน complex research จาก 73% ไป 87%

## TL;DR
- Anthropic Engineering ปล่อย "The components of agent memory" โดย Lance Martin (6 พ.ย.) — เสนอ pattern การใช้ offline job ที่ชื่อ "Dreams" ให้ agent review session ย้อนหลังสูงสุด 100 sessions แล้วเขียน memory store ใหม่ให้สะอาด
- รายงานผลใน Claude Managed Agents: dreaming แก้ความจำผิด (เช่น ตำแหน่ง Pokémon Center ใน Pokémon Red) และดัน wiki-only accuracy จาก 13% ไป 48% — xenospectrum รายงาน delta บน complex research task ที่ 73% → 87%
- Dreams เปิดเป็น research preview job ใน Managed Agents — ใช้คู่กับ memory store ที่มีอยู่ ไม่ใช่ product แยก

## เกิดอะไรขึ้น
วันที่ 6 พฤศจิกายน Anthropic Engineering เผยแพร่ research post "The components of agent memory" โดย Lance Martin ที่วาง pattern ใหม่สำหรับหนึ่งใน pain point ใหญ่สุดของ long-running agent — memory ที่สะสมไปเรื่อย ๆ จนเละ ความคิดคือแยก memory ของ agent เป็นชั้น ๆ: notes สด ๆ ที่เขียนระหว่าง session, facts ที่กลั่นออกมา, และ wiki links ที่เชื่อม entities เข้าหากัน แต่ pattern ที่ทุกคนจับจ้องคือ offline job ที่ชื่อ "Dreams"

Dreams ทำงานเหมือนการนอนหลับของมนุษย์ — agent ไม่ได้รับ request ใหม่ มันไปอ่าน session transcripts ย้อนหลังสูงสุด 100 sessions พร้อมกับ memory store ที่มีอยู่ แล้วเขียน memory store ใหม่ที่ consolidated ลบ note ที่ขัดกันทิ้ง, merge ข้อเท็จจริงซ้ำซ้อน, แก้ error ที่ fix ได้ด้วยการ cross-reference ตัวอย่างใน paper คือตอน agent เล่น Pokémon Red แล้วจำตำแหน่ง Pokémon Center ผิด — dreaming แก้โดย review session ที่ agent เคยเดินผ่านจริง

ตัวเลขที่ทำให้ paper นี้ถูก share เยอะคือ wiki-building experiment — ทีมสร้าง 25-question evaluation set บน document corpus หนึ่ง แล้วให้ agent สร้าง wiki ที่ linked โดย dream ขยายจาก 2 sessions ไป 128 sessions scaled accuracy จาก 13% ไป 48% ของ graded criteria และ xenospectrum อ้างอิง complex research task ที่ขยับจาก 73% ไป 87% Dreams เปิดเป็น research preview job ใน Claude Managed Agents — developer เรียกใช้คู่กับ memory store ที่มีอยู่ ไม่ใช่ product แยก

## ทำไมสำคัญ
Agent memory คือปัญหาที่ทุก framework ตั้งแต่ LangChain, AutoGen ไป CrewAI ตอบไม่ตรงจุด — ทุกคนทำ vector store แล้วเรียกว่า long-term memory แต่ไม่มีใครตอบคำถามว่า agent ควรลืมอะไร, ควร reconcile ความขัดแย้งเมื่อไหร่, ควร rewrite notes ตอนไหน การที่ Anthropic วาง pattern ที่มี "offline consolidation" ชัดเจนและมี result เบื้องต้นออกมาเป็น framework ที่คนอื่นจะ copy หรือ improve ได้ ไม่ใช่ demo

Signal ที่สำคัญกว่าตัว paper คือ Managed Agents เป็น runtime ที่ Anthropic กำลัง invest หนัก Dreams ไม่ได้ออกเป็น library หรือ open source — มันเป็น job ใน Managed Agents หมายความ Anthropic กำลัง bet ว่า long-running agent ต้อง host ไว้ที่ใครสักคน ไม่ใช่รันบน laptop ของ dev หรือ VM ของบริษัท การผูก dreaming ไว้กับ platform จึงเป็นทั้ง technical choice และ business choice

Caveat ที่ควรระวัง — ตัวเลข 73% → 87% มาจาก secondary source ที่ไม่มี methodology ชัด ส่วน 13% → 48% มีใน paper จริงแต่เป็น specific task (wiki-building) ไม่ใช่ general-purpose benchmark ที่ compare กับ framework อื่นได้ ยังต้องรอคนอื่น replicate หรือ Anthropic ปล่อย full technical report

## มุม AI Agent Platform
Builders — ถ้าคุณกำลังสร้าง agent framework ที่ตั้งเป้ารัน task ยาว ๆ (research, coding, multi-step workflow) Dreams เป็น pattern ที่ควร study ก่อน implement vector memory แบบเดิม การแยก memory เป็น notes/facts/wiki + offline consolidation job เป็น architecture ที่ reduce context pollution และ enable self-correction — ซึ่ง feedback loop ที่ most agent ไม่มีอยู่ตอนนี้ คนที่ทำ open-source framework ควร port pattern นี้ก่อน Anthropic ผูก platform lock-in หนักกว่านี้

Users/business — business ที่กำลัง deploy agent ใน workflow ควรถามตัวเองว่า agent ที่ใช้อยู่ "ลืมเรื่องผิด" บ่อยไหม — ถ้าใช่ นี่คือ signal ว่า vendor ของคุณยังอยู่ชั้น prototype ไม่ใช่ production ถ้า Enabridge หรือคนที่ build agent platform ให้ลูกค้าไทย ต้องตอบคำถามนี้ก่อน demo — เพราะ enterprise buyer ปี 2027 จะถาม

Ecosystem — Dreams reinforce thesis ว่า agent runtime เป็น battleground ใหม่ ไม่ใช่ model alone AWS AgentCore, Microsoft Agent 365, Google Agent Builder, และ Anthropic Managed Agents กำลัง race เพื่อเป็น default home ของ long-running agent ใครที่มี memory, observability, และ consolidation pattern ที่ work จริง จะเป็น platform ที่ dev เลือก ไม่ใช่ agent ที่ smart ที่สุด

## Sources
- [Can Claude dream now? Anthropic explores human-like machine memory (Interesting Engineering)](https://interestingengineering.com/ai-robotics/anthropic-claude-dreaming-memory-research)
- [Anthropic's "Dreaming" Lets AI Agents Reorganize Memory Offline (Xenospectrum)](https://xenospectrum.com/en/anthropic-agent-memory-dreaming-analysis/)
- [Claude Dreaming: How Anthropic's Dreams Fixes Agent Memory (AgentsPulse)](https://agentspulse.github.io/tutorials/claude-dreaming/)
- [Anthropic agent memory: what dreaming and wikis fixed (braindetox.kr)](https://braindetox.kr/en/posts/anthropic_agent_memory_components.html)

---

## Audio script
Anthropic Engineering เผยแพร่ research post ที่ชื่อว่า The components of agent memory เมื่อวันที่ 6 พฤศจิกายน โดย Lance Martin เป็นผู้เขียน เสนอ pattern ใหม่สำหรับ agent memory ที่แยกเป็นชั้น notes, facts, และ wiki links แต่สิ่งที่คนพูดถึงกันมากคือ offline job ที่ชื่อ Dreams Dreams ทำงานเหมือนการนอนหลับของมนุษย์ agent ไม่ได้รับ request ใหม่ มันไปอ่าน session transcripts ย้อนหลังสูงสุด 100 sessions แล้วเขียน memory store ใหม่ที่สะอาดกว่า ลบ notes ที่ขัดกันทิ้ง merge ข้อเท็จจริงที่ซ้ำ แก้ error ที่หาเจอจากการ cross-reference ตัวอย่างใน paper คือตอน agent เล่น Pokémon Red แล้วจำตำแหน่ง Pokémon Center ผิด dreaming แก้ให้ ตัวเลขที่น่าสนใจคือ wiki-building experiment ที่ dream scaled จาก 2 sessions ไป 128 sessions ดัน accuracy จาก 13 เปอร์เซ็นต์ ไป 48 เปอร์เซ็นต์ Dreams เปิดเป็น research preview job ใน Claude Managed Agents ไม่ได้ open source สำหรับคนสร้าง agent framework นี่คือ pattern ที่ควร study ก่อน implement vector memory แบบเดิม เพราะการแยก memory เป็น layer และมี consolidation job offline เป็น architecture ที่ reduce context pollution และ enable self-correction สำหรับ business ที่ deploy agent อยู่ ถามตัวเองว่า agent ลืมเรื่องผิดบ่อยไหม ถ้าใช่ แปลว่า vendor ของคุณยังอยู่ชั้น prototype ไม่ใช่ production
