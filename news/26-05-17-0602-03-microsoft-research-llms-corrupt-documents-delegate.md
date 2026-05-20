---
date: 2026-05-11
slug: microsoft-research-llms-corrupt-documents-delegate
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  A single pristine white office document with sharp text floats at the top of the
  image, then a vertical chain of 20 progressively more corrupted, torn,
  ink-smeared versions cascades downward — each more damaged than the last. To the
  right of the chain, three bold red labels float: "Gemini 3.1 Pro — 25% lost",
  "Claude 4.6 Opus — 25% lost", "GPT 5.4 — 25% lost". A green Python logo sits
  alone at the bottom right with the caption "the only survivor". Editorial
  isometric composition, dramatic top-down lighting with red warning glow,
  ultra-sharp text rendering, 1:1 aspect, high contrast for 200px thumbnail
  readability, tech-magazine cover style, no real human faces.
image: images/26-05-17-0602-03-microsoft-research-llms-corrupt-documents-delegate.png
---

# Microsoft Research ตบหน้า agentic hype — Gemini/Claude/GPT เสีย 25% เนื้อหา document หลัง 20 รอบ delegate, มีแค่ Python ที่พร้อมจริง

## TL;DR
- ทีม Microsoft Research (Laban/Schnabel/Neville) ออก preprint "LLMs Corrupt Your Documents When You Delegate" — ทดสอบ DELEGATE-52 benchmark ครอบคลุม 52 vertical domain
- ผลลัพธ์: Gemini 3.1 Pro, Claude 4.6 Opus, GPT 5.4 — ทุกตัวเสีย document content เฉลี่ย **25%** หลัง 20 delegated interaction; โดยรวมเฉลี่ย **50% degradation**; "catastrophic corruption" (คะแนน <80%) เกิดในกว่า **80% ของ model/domain combination**
- จาก 52 domain — มีแค่ **Python programming** ที่ผ่านเกณฑ์ "ready" ที่ 98%; agentic harness (ให้เครื่องมือ file read/write + code execution) ทำให้แย่ลง 6 percentage point เฉลี่ย

## เกิดอะไรขึ้น

ปลายสัปดาห์ที่ผ่านมา (11 พ.ค. coverage) Microsoft Research scientists 3 คน — Philippe Laban, Tobias Schnabel, Jennifer Neville — เผยแพร่ preprint paper ชื่อตรงประเด็นว่า **"LLMs Corrupt Your Documents When You Delegate"**. ทีมสร้าง benchmark ใหม่ชื่อ DELEGATE-52 ที่ทดสอบ frontier model ใน 52 professional domain (เขียน code, crystallography, music notation, regulatory text ฯลฯ) โดยจำลอง workflow ที่ผู้ใช้ delegate งานต่อเนื่อง 20 รอบให้ AI agent

ผลที่ออกมาตบหน้า narrative "agent ready for production" ของอุตสาหกรรมหลายเดือนที่ผ่านมา — ทั้ง Gemini 3.1 Pro (Google), Claude 4.6 Opus (Anthropic), GPT 5.4 (OpenAI) เสียเนื้อหา document เฉลี่ย **25%** หลัง 20 รอบ delegate, ค่าเฉลี่ย model ทั้งหมดที่ทดสอบ degradation **50%**, และ **catastrophic corruption** (คะแนน <80%) เกิดในกว่า **80% ของ model/domain combination**. จาก 52 vertical — มีแค่ **Python programming** ตัวเดียวที่ผ่านเกณฑ์ "ready" ที่ 98%

จุดที่เจ็บที่สุด — เมื่อทีมทดลองเพิ่ม **agentic harness** (ให้ model มี tool ใช้ file read/write, code execution, retrieval) กับ model เดียวกันบน domain เดียวกัน — performance **แย่ลงเฉลี่ย 6 percentage point**. กลายเป็นว่า "ให้เครื่องมือเยอะขึ้น" = "พังเร็วขึ้น" สำหรับ workflow ที่ไม่ใช่ code. นัยตรง ๆ คือ — ทุก agentic framework ที่ขายอยู่ตอนนี้ (LangGraph, AutoGen, CrewAI, OpenAI Swarm) ที่ปั้น agent loop ให้ทำงานต่อเนื่องหลายรอบ อาจะกำลังขยาย error rate มากกว่าลด

## ทำไมสำคัญ

นี่คือ **research signal ที่ทุก CIO ต้องอ่านก่อน sign procurement ใหญ่ ๆ ในไตรมาส 3**. หนึ่งสัปดาห์เดียวกันเรามีดีล PwC-Anthropic 30K certified + OpenAI Deployment Co $4B + ServiceNow Project Arc — ทุก vendor บอกว่า agent พร้อม production. แต่ Microsoft Research (ซึ่งไม่มี dog in this fight เพราะ Azure ขายทุกโมเดล) ออกมาบอกว่า — สำหรับ workflow ที่ไม่ใช่ Python coding "ไม่พร้อม"

Pattern ที่อ่านได้ลึก — **ความสำเร็จของ AI coding agent (Cursor $2B ARR, Devin/Cognition, Factory droids $150M) ไม่ใช่ proof ว่า agent generalize ได้ในทุก vertical** — Python coding เป็น domain ที่ feedback loop ชัด (compile หรือไม่ compile, test pass หรือไม่ pass) ที่ทำให้ self-correction ทำงานได้. domain อื่น (legal drafting, financial modeling, scientific writing) ไม่มี deterministic checker — model จะ accumulate error เงียบ ๆ จนเอกสารพังไปครึ่ง

ผลกระทบ enterprise — ทุก agent deployment ที่ run loop เกิน 10 รอบโดยไม่มี human-in-the-loop checkpoint มีโอกาสสูงที่จะ silently corrupt output. นี่อธิบายตรง ๆ ว่าทำไม Sierra/Cognition/Hightouch ที่ scale ได้ ทุกตัวมี **constrained domain + outcome validator** (customer service มี CSAT ที่ลูกค้าให้คะแนน, sales agent มี deal close หรือไม่). agent platform ที่ขาย "general purpose" ในงาน knowledge worker ต้องคิดใหม่ — task ขนาดเท่าไร, loop ลึกเท่าไรที่ตัวเองรับประกันได้

อีกประเด็น — Microsoft Research อยู่ใต้ Satya Nadella ที่กำลัง deploy Microsoft 365 Copilot + Agent 365 + Project Arc พร้อม ๆ กัน. การปล่อย paper แบบนี้ออกมา = ส่งสัญญาณ "responsibility deflection" ล่วงหน้าก่อน enterprise deployment failure ที่จะมาในครึ่งปีหลัง — "เราเตือนแล้วนะ"

## มุม OpenBridge

ตรงประเด็นมาก. ถ้า OpenBridge ทำ workflow orchestration ที่มี AI agent เป็น node — **ต้องไม่ออกแบบให้ agent loop เกิน 10 step โดยไม่มี human checkpoint หรือ deterministic validator**. design pattern ที่ปลอดภัย: agent ทำงานเป็น batch สั้น ๆ (3–5 step) แล้วเก็บ state ส่งให้ workflow rule-based engine ตรวจก่อนค่อย hand off กลับให้ agent ต่อ — เหมือน "circuit breaker" สำหรับ agent loop

อีก opportunity — feature "diff viewer + checkpoint replay" สำหรับ agent run. ถ้า agent run 20 step แล้วเอกสารเสีย user ต้องดูได้ว่า step ไหนที่เริ่มพัง + rollback กลับไปได้. นี่จะเป็นความต่างของ "production agent platform" กับ "demo agent platform" — และ Microsoft paper เป็นเอกสารขายในมือ sales OpenBridge ทันทีเมื่อคุยกับ CIO ที่ skeptical กับ agentic hype

## Sources
- [Microsoft researchers find AI models and agents can't handle long-running tasks (The Register)](https://www.theregister.com/ai-ml/2026/05/11/microsoft-researchers-find-ai-models-and-agents-cant-handle-long-running-tasks/5238263)
- [Microsoft Research: frontier AI fails 25% on long workflows (ResultSense)](https://www.resultsense.com/news/2026-05-12-microsoft-research-ai-agents-task-failures/)
- [AI is ready to take over Python programming, but not much else (CIO)](https://www.cio.com/article/4170475/ai-is-ready-to-take-over-python-programming-but-not-much-else.html)
- [AI is ready to take over Python programming, but not much else (InfoWorld)](https://www.infoworld.com/article/4170501/ai-is-ready-to-take-over-python-programming-but-not-much-else-3.html)

---

## Audio script
สวัสดีครับโย้ มาเล่าเรื่อง research paper ที่ตบหน้าวงการ agentic AI นักวิจัย Microsoft Research สามคน Philippe Laban Tobias Schnabel และ Jennifer Neville ออก preprint ชื่อตรงเลยว่า LLMs Corrupt Your Documents When You Delegate ทำ benchmark ใหม่ชื่อ DELEGATE 52 ทดสอบ frontier model ใน 52 vertical domain โดยจำลองการ delegate งานต่อเนื่อง 20 รอบ

ผลที่ออกมาช็อกวงการ Gemini 3.1 Pro Claude 4.6 Opus และ GPT 5.4 ทุกตัวเสียเนื้อหา document เฉลี่ย 25 เปอร์เซ็นต์ หลัง 20 รอบ ค่าเฉลี่ย model ทั้งหมด degradation 50 เปอร์เซ็นต์ และ catastrophic corruption เกิดในกว่า 80 เปอร์เซ็นต์ของ model domain combination จาก 52 vertical มีแค่ Python programming ตัวเดียวที่ผ่านเกณฑ์ ready ที่ 98 เปอร์เซ็นต์

จุดที่เจ็บที่สุดคือ เมื่อเพิ่ม agentic harness ให้ model มี tool ใช้ file read write กับ code execution performance แย่ลงเฉลี่ย 6 เปอร์เซ็นต์ จุด ให้เครื่องมือเยอะขึ้น เท่ากับ พังเร็วขึ้น สำหรับ workflow ที่ไม่ใช่ code นัยตรงๆคือทุก agentic framework ที่ขายอยู่ตอนนี้ ที่ปั้น agent loop ให้ทำงานต่อเนื่อง อาจกำลังขยาย error rate มากกว่าลด

ทำไมสำคัญ Microsoft Research ไม่มี dog in this fight เพราะ Azure ขายทุกโมเดล การออกมาเตือนแบบนี้คือสัญญาณ responsibility deflection ก่อน enterprise deployment failure ที่จะมาครึ่งปีหลัง มุม OpenBridge ถ้าทำ workflow orchestration ต้องไม่ออกแบบให้ agent loop เกินสิบ step โดยไม่มี human checkpoint หรือ deterministic validator design pattern ที่ปลอดภัยคือ agent ทำงานเป็น batch สั้นๆ แล้วเก็บ state ส่งให้ rule-based engine ตรวจ ก่อน hand off กลับให้ agent ต่อ เป็น circuit breaker สำหรับ agent loop ครับ
