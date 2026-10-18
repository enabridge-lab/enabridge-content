---
date: 2026-10-18
slug: sakana-agentic-scientist-v3
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  Editorial isometric illustration of a six-chamber Docker container ring —
  each chamber labeled with a research phase: "DRAFT", "INVESTIGATE",
  "ABLATE", "EVALUATE", "ANALYZE", "WRITE". Inside each chamber a tiny
  robot works a different coding tool badge (abstract pencil, scalpel,
  microscope icons — not brand logos). At the center, a glowing scroll
  stamped "ALIFE 2026 ACCEPTED". Three big stacked numbers float beside:
  "6 PHASES", "9 LLMs TESTED", "APACHE 2.0". Cobalt and amber palette,
  high contrast for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-18-0604-02-sakana-agentic-scientist-v3.png
---

# Sakana ปล่อย Agentic Scientist v3 แบบ Apache 2.0 — orchestration ชนะ model capability อีกครั้ง

## TL;DR
- 13 ต.ค. Sakana AI ส่ง paper 88 หน้าขึ้น arXiv แล้วเปิด **Agentic Scientist v3** (เดิมชื่อ AI Scientist) ภายใต้ Apache 2.0 บน 2 repo — pipeline + draw.io auto-illustrator
- รัน 6 phase ใน Docker container คนละตัว: **draft → investigate → ablate → evaluate → analyze → write** — ขับ Claude, Codex, Cursor, OpenCode, Gemini, Pi ผ่าน headless CLI
- Ablation สำคัญสุด: ทีมเทียบ **9 LLM × 4 harness** แล้วสรุปว่า **model เลือกเก่งก็จริง แต่ orchestration layer คือจุดที่ชนะ** — single-shot capability ของ frontier model ไม่พอ
- Development version ของ pipeline ผลิต paper 1 ชิ้นที่ **ALIFE 2026 รับตีพิมพ์จริง** (coverage ขัดแย้งว่า oral หรือ poster) — เป็น end-to-end agent paper ไม่กี่ชิ้นที่ไม่ใช่ demo

## เกิดอะไรขึ้น

วันอังคารที่ 13 ต.ค. ทีม Sakana AI (David Ha + Yujin Tang + พวก) submit paper 88 หน้าชื่อ **"The Agentic Scientist"** ขึ้น arXiv แล้วเปิด code สองก้อนบน GitHub ภายใต้ Apache 2.0: **AI-Scientist-v3** คือ orchestration pipeline, **AutoIllustrate** คือ companion ที่สร้างไฟล์ draw.io แบบ editable ไว้แทรก figure ลง paper. ทั้งคู่คือ generation ที่ 3 ของ AI Scientist ที่ Sakana เริ่มใน 2024 — ว่า: ทำ pipeline ที่ให้ agent ทำวิจัย end-to-end ตั้งแต่ hypothesis ไปจน publishable paper โดยที่มนุษย์ไม่ต้องเข้าแตะ

Architecture ของ v3 ต่างจาก v1/v2 ตรง **แยก 6 phase ไว้ใน Docker container คนละตัว** — Draft (คิด research question), Investigate (รัน exp), Ablate (ตัด variable ทดสอบ), Evaluate (benchmark สุดท้าย), Post-hoc Analyze (วิเคราะห์ผล), Paper (เขียน). ทีมเขียนไว้ว่าการแยก container ลด "cross-stage contamination" — คือ phase หนึ่งจำบริบท phase ก่อนหน้าไม่ได้นอกจากผ่าน artifact ที่ pass ไปจริง. และ pipeline ขับ **coding agent 6 ตัว**: Claude Code, OpenAI Codex, Cursor Agent, OpenCode, Gemini CLI, Pi — คือ wrapper ทาง headless CLI ไม่ใช่ bake model ไว้ตายตัว

Finding ของ paper ที่น่าสนใจกว่า release เอง: ทีม ablate **9 LLM × 4 harness** (คือ 36 combination) แล้วสรุปว่า **cross-agent orchestration layer อยู่ด้านบน model capability** — คือเปลี่ยน harness ให้ผลลัพธ์ต่างกันมากกว่าเปลี่ยน model base เสียอีก. บน benchmark ของ Sakana เอง (ซึ่ง bias แน่นอน) ทีมโชว์ว่า Claude + harness A ทำได้ดีน้อยกว่า GPT + harness A บน task ประเภทหนึ่ง แต่กลับกันบนอีกประเภทหนึ่ง — เลขเลยไปทาง **"model choice matters more than you think, but harness matters even more"** ซึ่งเป็น thesis ที่ตรงกับทั้ง LangGraph และ Microsoft Agent Framework กำลัง push

และ claim ที่ validate เรื่องนี้ที่ที่สุดคือ **ALIFE 2026 รับตีพิมพ์ paper 1 ชิ้น** ที่ development version ของ pipeline เขียน — ไม่ใช่ reviewer accept paper ที่ human คุยกับ agent แล้วแต่ง แต่คือ end-to-end pipeline ที่ agent ขับทั้งหมดจนเป็น publishable work. ทีม disclose ว่า human verify ผล experimental ก่อน submit แต่ไม่ edit paper เอง. coverage แตกกัน: อันหนึ่งเขียน oral presentation อีกอันเขียน poster — จนกว่า ALIFE จะโพส proceeding ชัด เอาเป็น signal ว่า pipeline ผ่าน peer review ไปแล้ว 1 ชิ้น

## ทำไมสำคัญ

ปีที่แล้ว AI Scientist v1 คือ demo — v2 คือ reproducibility pass — v3 คือ **production pattern สำหรับ multi-agent research**. ที่ทำให้ v3 ต่างจริงคือสองอย่าง: (1) Apache 2.0 ไม่ใช่ research license — ทีม commercial lift ไปใช้งานใน business workflow ได้เลย, (2) architecture แยก phase ลง container คือ pattern ที่ **transfer ได้นอก research** — ลองจินตนาการ legal pipeline (draft case → investigate case law → ablate argument → final brief), หรือ consulting pipeline (brief → research → scenario test → final deck). container-per-phase + headless CLI คือ reusable blueprint

และ finding "orchestration > capability" คือ thesis ที่ **ขัดกับ marketing ของ frontier lab** ที่ขายว่า GPT-6 Astra หรือ Claude Opus 4.7 คือทางออก — ความจริงคือ harness คือจุดที่ engineering effort ไหลเข้าไป. ตรงกับที่ Microsoft merged AutoGen + Semantic Kernel เป็น Agent Framework และ LangChain center บน LangGraph — ทั้งหมดคือ bet ว่า layer orchestration คือ moat ไม่ใช่ model

## มุม AI Agent Platform

สำหรับ **Builders**: pipeline v3 คือ reference implementation ที่ควรอ่าน code — pattern "Docker ต่อ phase + CLI wrapper ต่อ agent" คือ decoupling ที่ทำให้ swap model ง่าย, test ง่าย, debug ง่าย. และถ้า business ของคุณคือ vertical AI (legal, consulting, healthcare), v3 คือ blueprint ที่ apply ตรงไม่ต้องเริ่มจากศูนย์. สำหรับ **Users / Business** ที่คิด deploy AI research agent: paper ที่ pipeline เขียนแล้วผ่าน ALIFE คือ data point ที่ convince management ว่าเป็นไปได้ — แต่ scope ที่ Sakana demo คือ ALIFE (artificial life, niche conference) ไม่ใช่ Nature. apply ตรงกับ business คือต้องชัดเรื่อง quality gate ไม่ใช่ throughput. สำหรับ **Ecosystem**: lab ปิด model ที่ขาย "research agent" เป็น service (เช่น Elicit, Consensus, SciSpace) ตอนนี้มี open-source reference ที่ feature parity ที่ sophisticated — differentiation ต้องไปที่ data, verification, และ domain ไม่ใช่ orchestration อีกต่อไป

## Sources
- [Sakana AI open-sources Agentic Scientist v3, with ALIFE 2026 paper (aiweekly)](https://aiweekly.co/alerts/sakana-ai-open-sources-agentic-scientist-v3-with-alife-2026-paper)
- [Sakana AI's Agentic Scientist Turns Coding Agents Into Open-Source Researchers (alphasignal)](https://alphasignal.ai/news/sakana-ai-s-agentic-scientist-turns-coding-agents-into-open-source-researchers)
- [Sakana AI builds evidence checks into its open-source AI scientist (runtimewire)](https://runtimewire.com/article/sakana-ai-agentic-scientist-v3)

---

## Audio script
Sakana AI เพิ่งปล่อย Agentic Scientist v3 แบบ Apache 2.0 — pipeline ที่ให้ agent ทำวิจัยตั้งแต่ hypothesis ไปจน publishable paper โดยที่มนุษย์ไม่แตะ. จุดที่ v3 ต่างจากรุ่นก่อนคือ architecture แยก 6 phase ไว้ใน Docker container คนละตัว — draft, investigate, ablate, evaluate, analyze, write — แล้วขับ coding agent 6 ตัวผ่าน headless CLI ตั้งแต่ Claude, Codex, Cursor, OpenCode, Gemini, Pi. finding ที่สะเทือนที่สุดคือ ทีม ablate 9 LLM กับ 4 harness แล้วสรุปว่า harness สำคัญกว่า model base — คือ orchestration layer อยู่ด้านบน model capability. และ development version ของ pipeline เขียน paper ที่ ALIFE 2026 รับตีพิมพ์จริง 1 ชิ้น ไม่ใช่ demo. ที่สะเทือนตลาด: pattern Docker ต่อ phase กับ CLI wrapper ต่อ agent คือ blueprint ที่ transfer ได้นอก research — legal pipeline, consulting pipeline, healthcare pipeline ก็ใช้ pattern เดียวกัน. และคำถาม "model หรือ harness สำคัญกว่า" ตอนนี้มีคำตอบ data-backed แล้ว ว่า harness ชนะ — ที่ engineering effort ของ builder ควรลงไปคือ orchestration ไม่ใช่รอ frontier model รุ่นต่อไป.
