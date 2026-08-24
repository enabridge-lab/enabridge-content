---
date: 2026-08-25
slug: microsoft-thinkingbox-pass-at-20-agent-reliability
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A wide editorial isometric illustration of a cracked marble podium in a
  neon-lit test arena. Two huge stacked scoreboards float above the podium:
  the top one reads "PASS AT 1 = 65.36%" glowing gold; the one beneath reads
  "PASS AT 20 = 25.25%" in bright red, breaking apart into shards. A stylized
  database cylinder labeled "PROD DB" sits in the foreground with tool-call
  arrows spiraling into it. A small Microsoft logo pin on the corner of the
  arena; sharp navy, teal, and amber palette; chunky sans-serif labels
  readable at 200px thumbnail; 1:1 aspect ratio; no real human faces.
image: images/26-08-25-0615-01-microsoft-thinkingbox-pass-at-20-agent-reliability.png
---

# Microsoft ThinkingBox — pass^20 คือตัวเลขที่กระชากทุก agent demo กลับสู่ความจริง

## TL;DR
- Microsoft ปล่อย ThinkingBox open-source: sandbox + benchmark 507 stateful business tasks รันซ้ำ 20 ครั้งต่อ task บน 12 model ทั้ง proprietary/open-weight — วัดที่ **state ของ database จริง** ไม่ใช่คำอ้างของ agent
- Top model ทำ **pass@1 = 65.36%** แต่พอวัด **pass^20 (ผ่านครบทั้ง 20 รอบ) = 25.25%** — "ผ่านครั้งเดียว fail ทุกครั้งหลังจากนั้น" คือ default
- หลาย fail run จบด้วย tool call ที่ดูสมเหตุสมผล — agent ไม่รู้ตัวว่าทำพัง เพราะไม่มี ground truth ให้ verify กลับ

## เกิดอะไรขึ้น
วันที่ 19 ส.ค. 2026 Microsoft Research ปล่อย ThinkingBox — sandbox กับ benchmark suite ที่วางกติกาใหม่ของการวัด agent reliability ทั้งชุดคือ 507 task ของ business workflow จริง (order fulfillment, invoice reconciliation, HR onboarding, IT ticketing, sales quote generation) กระจายอยู่ใน 5 domain แต่ละ task ถูกรัน 20 ครั้งต่อ model 12 ตัว (proprietary กับ open-weight) แล้วให้คะแนนจาก state ของ database หลังจบ ไม่ใช่จากคำตอบสุดท้ายของ agent

ตัวเลขที่ทีมออกแบบมาให้เห็นเลยคือ **pass^20** — ต้องผ่านครบทั้ง 20 รอบถึงจะนับ ตัว top model ทำ **pass@1 ได้ 65.36%** ซึ่งฟังดูโอเค แต่พอวัดที่ pass^20 เหลือ **25.25%** เท่านั้น หมายความว่า agent ที่ demo ให้ CEO ดูอาจ complete ทุก step ถูกในรอบเดียว แต่ถ้าเอาไปรันทุกวัน 20 วันต่อเดือน โอกาสที่จะเกิด silent failure ที่ทำให้ order status พังหรือ ledger balance เพี้ยนคือ 3 ใน 4 รอบ

รายละเอียดที่หนักกว่านั้นคือ pattern ของ failure หลาย fail run จบด้วย tool call ที่ syntactic ถูก, agent bot ตอบ "task complete" กลับ orchestrator เรียบร้อย แต่พอเปิด database เช็ก field ปลายทางไม่มีการอัพเดต หรือ update ผิด row Microsoft เรียก failure mode นี้ว่า "plausible completion" — agent ไม่ได้ตายกลาง flow, ไม่ได้ throw exception, ไม่มี log อะไรผิด, แค่ state ปลายทางไม่ match กับ intent

## ทำไมสำคัญ
ตัวเลขนี้ทำสิ่งที่ vendor ทั้งอุตสาหกรรมไม่อยากทำมาปีกว่า: ให้ number ที่ CIO เอาไปยัดใส่ RFP ได้ ตลอดปี 2025-2026 vendor pitch ทุกเจ้าถือ leaderboard ของ tau-bench, SWE-bench, GAIA ที่ตัวเลขวิ่ง 70-90% แต่ enterprise pilot ตายที่ 80% ระหว่างทางไป production เพราะ benchmark เหล่านั้นวัดคำตอบเดียว ThinkingBox เป็นตัวแรกที่วัด variance ของ agent เดียวกันบน task เดียวกันซ้ำ ๆ ซึ่งคือ pattern ของ production ที่แท้จริง

ที่น่าสังเกตคือ Microsoft ปล่อยตัวนี้เป็น open-source ผ่าน Agent Governance Toolkit — เท่ากับเปิดทางให้ทุกคนเอา framework ไป benchmark คู่แข่ง (รวม Copilot Studio ของ Microsoft เอง) นี่ไม่ใช่ท่าของ vendor ที่กลัวเลข แต่เป็นท่าของคนที่รู้ว่า ecosystem ที่มี consistent metric จะเร่ง sales cycle เพราะ buyer ตัดสินใจได้จริง เทียบง่าย ๆ กับตอน MLPerf ออกในปี 2018 — ก่อนหน้านั้น GPU vendor ทุกเจ้าโชว์ number ที่ไม่ compare กันได้ พอมี MLPerf ตลาดถึงแยก signal จาก noise ได้

Signal ต่อจากนี้: RFP ของ enterprise ที่จริงจังจะเริ่มถามหา pass^N (N = 10, 20, 100) แทน pass@1 และ vendor ที่ยังโชว์แต่ pass@1 จะเริ่มถูกกดดันให้เปิด variance number ตามมา ตลาด agent evals และ agent observability (Braintrust, LangSmith, Arize, Galileo) จะได้ boost เพราะ enterprise ต้องมีเครื่องมือวัดของตัวเอง

## มุม AI Agent Platform
สำหรับ **builders** ที่ทำ agent framework/runtime: อย่า optimize เฉพาะ pass@1 เพราะ enterprise buyer ที่โต 6-12 เดือนถัดไปจะถามหา repeatability agent architecture ต้องออกแบบให้มี verifier / checker step หลัง action ทุก mutation — ไม่ใช่ trust "task complete" ที่ agent เขียนกลับมา แน่นอนว่า overhead จะขึ้น แต่ pass^20 ที่ 25% แปลว่ามี room เหลืออีก 3-4x ก่อนจะไปแตะ ceiling ของ tool

สำหรับ **users/business** ที่ deploy agent ใน workflow: อย่าเซ็น contract ที่ SLA อยู่บน "accuracy" ตัวเดียว บังคับให้ vendor รายงาน pass^20 หรือ variance ต่อ transaction type ก่อน scale ยิ่งเป็น workflow ที่แตะ ledger, order state, หรือ external API ที่ side-effect กลับไม่ได้ — invariant check หลัง run ต้องถูก build เข้า pipeline สำหรับ Enabridge ในฐานะ AI Agent Platform นี่คือ argument ที่จะพูดกับลูกค้า Thai SME ว่า pilot ที่ demo ผ่าน 3 รอบไม่พอ — ต้องเห็น run 20 รอบต่อ transaction type ที่สำคัญที่สุดก่อนเปิด production

สำหรับ **ecosystem** (evals, observability, orchestration): ThinkingBox เพิ่งเปิดช่องว่างที่ใหญ่มาก — startup ที่ทำ "agent QA as a service" ที่รัน replay 20-100 รอบต่อวันบน workflow production ของลูกค้า มี window ประมาณ 6-12 เดือนก่อนที่ Datadog / New Relic / AWS CloudWatch จะ ship native feature ต่อ Databricks / Snowflake / Salesforce ที่ห้ามให้ agent เขียน state โดยไม่มี verifier — pattern "write → verify → commit" คือสิ่งที่จะกลายเป็น default ของ agent platform maturity รอบใหม่

## Sources
- [Microsoft ThinkingBox and the reliability gap in AI agents — CryptoBriefing (Aug 22, 2026)](https://cryptobriefing.com/microsoft-thinkingbox-ai-agent-reliability/)
- [ThinkingBox: Benchmarking Stateful Business Workflow Agents at Scale — arXiv preprint](https://arxiv.org/abs/2608.19741)
- [Microsoft Agent Governance Toolkit — GitHub](https://github.com/microsoft/agent-governance-toolkit)

---

## Audio script
วันนี้ Microsoft Research ปล่อย ThinkingBox ครับ เป็น sandbox กับ benchmark ที่วัด agent ที่ state ของ database จริง ไม่ใช่คำอ้างของ agent เอง

ชุด benchmark มี 507 task ของ business workflow ทั้งหมด รันซ้ำ 20 รอบต่อ task ต่อ model ทั้ง proprietary กับ open-weight 12 ตัว ตัวเลขที่ออกมาแรงมาก top model ทำ pass at one ได้ 65% ซึ่งฟังดูโอเค แต่พอวัด pass at twenty คือต้องผ่านครบทั้ง 20 รอบเหลือแค่ 25% เท่านั้น

ที่หนักกว่านั้นคือ pattern ของ fail หลาย run agent จบ tool call ที่ดูถูกต้อง บอก task complete กลับ orchestrator แต่พอเปิดฐานข้อมูลไม่มีการ update จริง Microsoft เรียก failure mode นี้ว่า plausible completion agent ไม่รู้ตัวว่าทำพัง

signal สำหรับคนทำ agent platform คือ อย่า optimize เฉพาะ pass at one ต่อจากนี้ enterprise จะเริ่มถามหา pass at twenty ใน RFP และ agent architecture ต้องมี verifier step หลัง mutation ทุก action ครับ
