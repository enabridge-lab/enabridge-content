---
date: 2026-05-05
slug: yutori-agent-reliability-compounding-error
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: Editorial illustration of a long winding bridge of glass blocks across a vast canyon, each block subtly cracked while one hand patiently aligns them, abstract decay particles drifting downward, minimal flat geometric shapes, muted slate and pale-yellow palette, dramatic side lighting, no text no logos no faces
image:
---

# Yutori ออกมาท้า industry — "agent ที่ทำงานได้ 90% ก็ใช้ไม่ได้" reliability เป็น moat ที่แท้จริงของ agentic AI

## TL;DR
- Abhishek Das (co-founder Yutori, อดีต Meta AI lead) ออก essay 4 พ.ค. ในชื่อ "The #1 Rule for Building AI Agents in 2026" — argument ตรง ๆ: industry กำลัง normalize ความ unreliable ของ agent และนี่คือ existential bug
- ตัวเลขที่ Das นำเสนอ: **90% accuracy ต่อ step** ฟังดูดี แต่ใน workflow 10-step → success rate 35%, 20-step → 12%, 50-step → 0.5% — เกือบ guarantee ว่าจะ fail ทั้ง flow ที่มี complex orchestration
- Yutori's Navigator agent (ตัว product Delegate ที่เพิ่งเปิดตัว 23 เม.ย.) ตามแถลงของบริษัท outperform Gemini 2.5, Claude 4.0/4.5, OpenAI Operator ที่ **10–20 percentage point** บน real-world web task — และทำงานเร็ว 2–3 เท่า

## เกิดอะไรขึ้น

วันที่ 4 พฤษภาคม Abhishek Das, co-founder/co-CEO ของ Yutori (startup ที่ Fei-Fei Li + Jeff Dean หนุน, ระดมทุน $15M seed เมื่อมีนาคม 2025) ออก thought piece ที่ถูก circulated หนักใน VC + AI engineering community — argument หลัก: **agent industry ทุกราย รวม OpenAI Operator + Anthropic Claude Computer Use + Google Project Mariner กำลัง normalize unreliability** และเรื่องนี้จะเป็น barrier ที่ยังไม่มีใครยอมรับว่าใหญ่จริง

ตัวเลขที่ Das นำเสนอชัดเจน — และน่ากลัวเมื่อคำนวณตามว่า: ถ้า agent ทำ step ใด ๆ accuracy 90% (ตัวเลขที่ frontier agent ส่วนใหญ่ claim ใน benchmark), workflow 10 ขั้นตอนจะมี end-to-end success rate แค่ 0.9^10 = **35%** — ใน 20 step เหลือ 12% — ใน 50 step เหลือ **0.5%** เกือบ certainty ว่า fail Das บอกว่านี่คือเหตุผลที่ enterprise customer พบ "demo ดูดีในห้องทดลอง พอ deploy production agent fail ตลอด" — ไม่ใช่เพราะ model ไม่ดี แต่เพราะ math ของ compounding error

Das ชี้ pain point เพิ่ม: getting reliability จาก **50% → 80% → 99+%** ใช้ effort ที่ scale ไม่ใช่ linear แต่ใกล้ exponential — เพราะ failure mode ที่เหลือคือ edge case ที่ rare แต่ devastating (auth fail, page layout เปลี่ยน, dropdown ใหม่, captcha) และต้อง handle ผ่าน infrastructure layer ไม่ใช่ prompt engineering ที่ Yutori สร้าง: error detection ที่ agent **รู้ว่าตัวเอง fail** (meta-cognition), backtracking ที่ recover จาก dead-end, durable execution บน DBOS framework (Yutori announce partnership กับ Databricks/DBOS เมื่อมีนาคม 2026)

ผลลัพธ์ที่ Yutori claim ใน announcement ของ Delegate (product launch 23 เม.ย. 2026) — Navigator agent ทำงาน real-world web task ที่ benchmark ภายใน outperform **Gemini 2.5, Claude 4.0, Claude 4.5, OpenAI Operator** ที่ 10–20 percentage point บน accuracy และ 2–3x เร็วกว่า ที่น่าสนใจคือ Das ไม่ argue ว่า base model Yutori ดีกว่า — argue ว่า **infrastructure layer รอบ ๆ model สำคัญกว่า model เอง** เป็นจุดยืนที่ controversial

ตัวอย่าง use case ที่ Yutori นำเสนอ: order food, book flight, monitor competitor pricing, fill insurance form — task ที่มี 30–50 sub-step และต้อง authenticate, parallelize, handle retry ปริมาณการใช้งานของ Delegate (ที่เปิดตัว 2 สัปดาห์ก่อน) ยังไม่เปิดเผย แต่ Encord (vendor ที่ Yutori ใช้ build training data) อ้างว่า Yutori ใช้ "high-quality human annotation ปริมาณ industry-leading" เป็นปัจจัยสำคัญที่ทำให้ accuracy ที่ 99%+ เป็นไปได้

## ทำไมสำคัญ

Das ชี้ปัญหาที่ everyone-knows-but-no-one-talks-about: **Stanford AI Index 2026 รายงานว่า 89% ของ enterprise agent project fail ใน production** (จากที่เราพูดในรอบเก่า) — และ Das บอกว่า root cause ส่วนใหญ่ไม่ใช่ model capability แต่เป็น compounding error ใน multi-step workflow ที่ engineering team ไม่ได้ build infrastructure รอบ ๆ ให้ดี OpenAI/Anthropic ถนัดเทรน base model ให้ smart — แต่ไม่ถนัด build agentic infrastructure ที่ resilient — และนี่เปิดช่องให้ startup อย่าง Yutori, Adept (อยู่ในระยะที่จะถูก acquire), Imbue, Cresta สร้าง moat ที่ frontier lab copy ยาก

ชั้นที่สอง — **reliability เป็น first-class metric ที่จะเข้ามาแทน benchmark performance** SWE-bench, MMLU, HumanEval บอกว่า model ตอบ single question ได้ดีแค่ไหน — แต่ enterprise CIO ที่จะ deploy agent ไม่สนใจตัวเลขนั้น สนใจว่า **agent นี้ run 1,000 workflow แล้ว fail กี่ตัว** Das กำลังเรียกร้อง benchmark ใหม่ที่วัด end-to-end reliability บน 30+ step workflow — และ Yutori พร้อมที่จะ publish ของตัวเอง การที่ Das ยอม pre-announce ว่า Yutori outperform frontier โดย 10–20pp ใน reliability เป็น signal ว่าตลาดน่าจะเข้าสู่ phase ที่ infrastructure dominance สำคัญกว่า model dominance

ชั้นที่สาม — **Pattern ที่กำลังโตเงียบ ๆ คือ "durable execution" สำหรับ agent** — DBOS (ที่ Yutori partner), Temporal, Inngest, Trigger.dev กำลังกลายเป็น critical layer ที่ enterprise เริ่ม spec ใน RFP เพราะ agent ที่ run นาน + ผ่าน multiple tool call + เก็บ state ระหว่าง user session ต้องการ infrastructure แบบ workflow engine ที่ traditional codebase ใช้ ไม่ใช่ stateless API call แบบ ChatGPT — และ tooling นี้กำลังกลายเป็น differentiator

## มุม OpenBridge

Yutori's argument คือ **บทเรียนตรงสำหรับ OpenBridge** — เพราะ OpenBridge ในฐานะ B2B integration platform คือ "infrastructure layer for agent reliability" โดยธรรมชาติ — ทุกครั้งที่เราเพิ่ม monitoring, retry, circuit breaker, rollback ก็คือสิ่งที่ Das บอกว่า frontier lab ละเลย OpenBridge มี opportunity ที่จะ position ตัวเองว่า "**infrastructure layer ที่ทำให้ Claude/GPT/Gemini agent ของลูกค้า run reliable ใน production**" — ไม่ใช่แค่ workflow tool ทั่วไป

จุดที่ act ทันที: (1) **Audit ของ workflow ที่ลูกค้า OpenBridge ใช้ AI step** — มีกี่ workflow ที่ chain step มากกว่า 5? มีกี่ workflow ที่ใช้ AI ใน step สำคัญและไม่มี fallback? ตัวเลขนี้คือ market sizing สำหรับ "reliability product" ที่อาจขายเพิ่มได้, (2) **Build observability + retry primitive ที่ agent-friendly** ไม่ใช่ HTTP retry แบบเดิม — ต้องมี LLM-aware retry ที่ understand intent ของ failed step, semantic backtracking, error classification ที่แบ่งเป็น "transient vs structural" และ (3) **publish reliability benchmark ของ workflow บน OpenBridge** — เป็น marketing tool + technical credibility ที่ลูกค้าใหญ่ต้องการเห็น — Sierra/Decagon จะตามมาในไม่ช้า

ลูกค้า enterprise ที่จะ deploy agent ใน production จะถามคำถามใหม่ในรอบ procurement ปลายปี: **"คุณ guarantee uptime/success rate ของ workflow ของฉันได้ระดับไหน"** — ถ้า OpenBridge ตอบไม่ได้ด้วยตัวเลข SLO concrete จะเสีย deal ให้ vendor ที่ตอบได้

## Sources
- [The #1 Rule for Building AI Agents in 2026 | Yutori, Abhishek Das](https://startup.whatfinger.com/2026/05/04/the-1-rule-for-building-ai-agents-in-2026-yutori-abhishek-das/)
- [Yutori launches Delegate to turn AI agents into proactive web workers](https://siliconangle.com/2026/04/23/yutori-launches-delegate-turn-ai-agents-proactive-web-workers/)
- [How Yutori Built the Best Web Agent in the World with High-Quality Human Data](https://encord.com/customers/yutori/)
- [Yutori: Large-scale, Durable Agentic AI on DBOS](https://www.dbos.dev/case-studies/yutori-large-scale-durable-agentic-ai)

---

## Audio script
ข่าวสุดท้ายของรอบนี้น่าสนใจในมุม engineering — Abhishek Das, co-founder ของ Yutori ที่ Fei-Fei Li กับ Jeff Dean หนุน ออก essay เมื่อสี่พฤษภาในชื่อ The Number One Rule for Building AI Agents in 2026 argument ของเขาตรง — industry กำลัง normalize agent ที่ unreliable และนี่คือ existential bug

Das คำนวณให้เห็น — ถ้า agent ทำ step ใด ๆ ที่ accuracy เก้าสิบเปอร์เซ็นต์ ใน workflow สิบ step success rate ปลายทางเหลือสามสิบห้าเปอร์เซ็นต์ ใน twenty step เหลือสิบสองเปอร์เซ็นต์ ใน fifty step เหลือศูนย์จุดห้าเปอร์เซ็นต์ — เกือบ guarantee fail นี่คือเหตุผลที่ enterprise พบว่า demo ดูดีในห้องทดลอง พอ deploy production agent fail ตลอด — ไม่ใช่เพราะ model แย่ แต่เพราะ math ของ compounding error ที่ frontier lab ไม่ได้แก้ที่ infrastructure layer

Yutori claim ว่า Navigator agent ของตัวเอง outperform Gemini 2.5, Claude 4.0, 4.5, OpenAI Operator ที่ ten ถึง twenty percentage point ใน accuracy ที่ real-world task และ work เร็ว two ถึง three เท่า ไม่ใช่เพราะ base model ดีกว่า แต่เพราะ infrastructure layer รอบ ๆ — error detection ที่ agent รู้ว่าตัวเอง fail, backtracking, durable execution บน DBOS framework

ภาพใหญ่คือ — reliability จะเข้ามาแทน benchmark performance เป็น metric หลัก enterprise CIO ไม่สนใจ MMLU score แล้ว สนใจว่า agent นี้ run 1,000 workflow fail กี่ตัว — และ pattern durable execution อย่าง Temporal, Inngest, DBOS กำลังกลายเป็น critical layer

สำหรับ OpenBridge — Yutori's argument คือ playbook ตรงสำหรับเรา เราอยู่ใน infrastructure layer for agent reliability โดยธรรมชาติ ทุกครั้งที่เราเพิ่ม monitoring, retry, rollback คือสิ่งที่ Das บอกว่า frontier lab ละเลย opportunity คือ position ตัวเองว่า — infrastructure ที่ทำให้ Claude หรือ GPT agent ของลูกค้า run reliable ใน production ไม่ใช่แค่ workflow tool ลูกค้าจะถามคำถามใหม่รอบหน้า — คุณ guarantee uptime ระดับไหน — ถ้าเราตอบไม่ได้ด้วยตัวเลข SLO เราจะเสีย deal
