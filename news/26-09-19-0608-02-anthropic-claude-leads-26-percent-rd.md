---
date: 2026-09-19
slug: anthropic-claude-leads-26-percent-rd
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  Editorial hero illustration: a stylized laboratory of glowing hexagonal
  research pods arranged in a spiral; the pods are stacked into three tiers
  labeled in bold sans-serif "1% MARCH", "26% AUGUST", "?? DEC". A single
  large origami crane made of blueprint paper hovers at the top writing
  formulas onto a floating whiteboard while smaller cranes work in parallel
  below. Palette: deep indigo background, warm amber highlights, off-white
  paper. Editorial isometric composition, minimal flat vector, high contrast
  for 200px thumbnail. 1:1 aspect, no real human faces, no Anthropic logo.
image: images/26-09-19-0608-02-anthropic-claude-leads-26-percent-rd.png
---

# Claude นำ 26% ของ R&D ที่ Anthropic เอง — จาก 1% ในมีนา, 90% ทำ "ร่วม" — 30,000 agent วิ่งอยู่หลังบ้าน

## TL;DR
- Anthropic ประกาศวันพฤหัส (18 ก.ย.) ว่า **Claude เป็น lead ของ R&D task 26%** ที่บริษัทเดือนสิงหา — **ขึ้นจาก 1% เมื่อมีนาคม** ปีเดียวกัน
- ~**90% ของงาน R&D ทั้งหมด** ทำแบบ "collaboration" — human ควบคุมทิศทาง, Claude ทำ large chunk under close supervision
- Anthropic disclose ว่ามี **~30,000 agents** วิ่ง research workload อยู่ในบริษัท ณ เดือนสิงหา
- **Signal: recursive self-improvement เริ่มมี metric ที่ public แล้ว** — และเลข 1% → 26% ใน 6 เดือน = compound rate ที่จะทะลุ 50%+ ก่อนสิ้นปีถ้า trajectory ไม่หัก

## เกิดอะไรขึ้น

Anthropic ปล่อยรายงาน internal metric เมื่อวานพฤหัสในสิ่งที่ CEO Dario Amodei เคยพูดหลายครั้งใน podcast แต่ไม่เคย quantify: **Claude นำ 26% ของงาน R&D ภายในบริษัทเดือนสิงหาคม**, ขึ้นจาก **1% เมื่อมีนาคม** — 26x compound ใน 6 เดือน. คำว่า *"leading"* ใน definition ของ Anthropic คือ Claude complete task *"end-to-end from a high-level prompt while still being under human supervision"* — คือ human ตั้งโจทย์ระดับ paragraph, Claude ทำ everything else ตั้งแต่ literature review, experiment design, code, evaluation, ไปจนถึง writeup

ตัวเลขที่ใหญ่กว่านั้นคือ **~90% ของ R&D ทั้งหมด** ทำ *"in collaboration with Claude"* — คือ Claude ทำ large chunk under close human direction. แปลว่า Anthropic operate หลัง scene แบบที่มีสอง workforce — human กับ agent — และ agent share workload ระดับที่ human ทำเองไม่ได้อีกต่อไป. Anthropic โชว์ context เพิ่มว่า **~30,000 agent วิ่ง research workload** อยู่ในบริษัท ณ เดือนสิงหา — เทียบกับ headcount human ที่รายงานเกิน 1,500 คน = **agent-to-human ratio 20:1** ในกลุ่ม research

Anthropic ระวังเรื่อง narrative — เน้นว่า *"Claude was not working fully autonomously in any of the areas covered by the measurement"* — คือยัง human-in-the-loop ทั้งหมด, และเลข 26% ไม่ใช่ *"AI ทำแทน 26% ของ scientist"* แต่คือ *"AI ทำ leading role บน 26% ของ task"*. Distinction สำคัญเพราะ regulator + press จะ conflate ทั้งสอง; Anthropic pre-empt narrative นั้นด้วยการ commit **third-party safety evaluator embedded ภายในบริษัท**

Timing น่าสนใจ — Anthropic ปล่อย metric นี้สัปดาห์เดียวกันกับที่ Hacktron ใช้ Claude Opus 5 เจาะ OpenAI (ดู brief แรกของรอบนี้). ทั้งสอง event ยืนยันเรื่องเดียวกัน: **frontier model ใน late 2026 ทำ multi-step technical work ที่เมื่อก่อนต้องใช้ senior engineer** — ไม่ว่าจะเป็น model R&D หรือ exploit development. เส้นแบ่งระหว่าง *"tool"* กับ *"colleague"* กำลังหายไปในระดับ definition

## ทำไมสำคัญ

**Recursive self-improvement มี public metric แล้ว.** เมื่อก่อน RSI เป็น thought experiment ของ AI safety community ที่ argue ได้แต่ในทางทฤษฎี; Anthropic เพิ่งเปลี่ยนมันเป็น dashboard number ที่ update รายเดือน. **Trajectory 1% → 26% ใน 6 เดือน = compound monthly rate ~65%**. ถ้า trajectory นี้ hold ต่ออีก 6 เดือน, เลขจะทะลุ 50% ในไตรมาส 1 ปี 2027 — เกินครึ่ง. เกินครึ่งของ R&D ที่ frontier lab นำโดย model ของตัวเอง = territory ที่ไม่เคยมี company ใน history อยู่มาก่อน

**Talent implication เปลี่ยนไปสิ้นเชิง**. ก่อนหน้านี้ frontier lab แข่งกัน hire scientist ที่ premium 3-5x. ตอนนี้ marginal contribution ของ senior scientist เพิ่มเข้าไปใน team ที่มี Claude Opus 5 + 30k agent workforce แล้ว = สูงกว่า *marginal cost ของ agent ทีมใหม่* จริงหรือ? ถ้าไม่ — hiring plan ของ Anthropic ปี 2027 อาจจะ pivot จาก *scale headcount* → *scale agent farm*. OpenAI + Google DeepMind ต้อง publish metric เดียวกันภายใน 30 วันเพื่อรักษา perceived leadership; ถ้าเลขต่ำกว่าจะโดน narrative *"stuck ใน old paradigm"*

Pattern ที่เห็น: **AI lab กำลังกลายเป็น first case study ของ agentic organization ที่ scale จริง**. ไม่ใช่ SaaS startup, ไม่ใช่ hedge fund — คือ AI lab เอง. เพราะ (1) domain expertise สอน model ให้เข้าใจได้เพียง one-hop, (2) task ทั้งหมด computational → verifiable, (3) infrastructure + budget ไม่มี constraint. Enterprise ที่พยายาม deploy agent workforce ควร watch pattern นี้แทน McKinsey slide — เพราะ Anthropic กำลัง run experiment ที่คนอื่นจะ replicate ใน 12-18 เดือน

ที่ต้องระวังคือ **verification gap**. Anthropic ระบุเลขเอง — ไม่มี third party audit. Definition ของ *"leading"* กำหนดโดย Anthropic; ถ้า scope task ที่ AI ทำ *"small enough to complete end-to-end"* จะทำให้ percentage สูงเทียม. AIUC + METR (สอง org ที่ทำ third-party AI audit) น่าจะถูกกดดันให้เข้ามา validate metric แบบนี้ — เพราะ investor + regulator ต้องการเลขที่ apples-to-apples comparable ระหว่าง lab

## มุม AI Agent Platform

**Builders:** ถ้าคุณสร้าง agent framework หรือ orchestration layer, **เรียนจาก stack ของ Anthropic เอง** — ทีมกำลัง publish partial reference architecture ผ่าน Claude Code + Claude Agent SDK + MCP ecosystem. Pattern ที่เห็น: (1) high-level prompt → task decomposition, (2) parallel agent farm (30k concurrent!), (3) human-in-the-loop checkpoint ที่ granularity 1-4 ชั่วโมงต่อ task. Framework ที่ replicate pattern นี้ได้จะ dominant. อย่า overengineer routing — Anthropic เอง run flat topology

**Users / Business:** ถ้าคุณ deploy agent ใน workflow ของบริษัท, **ตั้ง metric แบบเดียวกันวันนี้** — track % ของ task ที่ AI ทำ leading role vs collaboration vs assist. บริษัทที่ไม่ measure จะไม่รู้ว่ากำลัง scale หรือ stagnate. Rate 65% compound monthly ของ Anthropic คือ upper bound; enterprise average น่าจะอยู่ที่ 15-25% compound — แต่ถ้าไม่วัดก็ optimize ไม่ได้

**Ecosystem:** สำหรับ SMB ไทยและ vertical SaaS builder — pattern *"agent leads narrow task, human supervise"* คือ template ที่จะขาย enterprise ได้ในปี 2027. อย่ารอ market ready; deploy narrow agent ใน customer workflow วันนี้ (invoice reconciliation, order intake, customer email triage) แล้ว publish % ของ task ที่ agent lead. ตัวเลขนี้จะกลายเป็น *"trust metric"* ที่ B2B buyer ถามก่อน sign contract — เหมือน uptime ในยุค SaaS

## Sources
- [NBC News — Anthropic says its model Claude is helping to build the next version of itself](https://www.nbcnews.com/tech/tech-news/anthropic-says-model-claude-helping-build-next-version-rcna598494)
- [Benzinga — Anthropic Says Claude Now Leads 26% of Its AI R&D, Up From Just 1% in March](https://www.benzinga.com/markets/tech/26/09/61861775/anthropic-says-claude-now-leads-26-of-its-ai-rd-up-from-just-1-in-march)
- [Washington Times — Anthropic says Claude is helping to build next version](https://www.washingtontimes.com/news/2026/sep/17/anthropic-says-claude-helping-build-next-version/)
- [US News — Anthropic Says Its Model Claude Is Helping to Build the Next Version of Itself](https://www.usnews.com/news/business/articles/2026-09-17/anthropic-says-its-model-claude-is-helping-to-build-the-next-version-of-itself)

---

## Audio script
Anthropic ปล่อย metric เมื่อวานที่จะเปลี่ยนวิธีคิดของทั้งวงการเรื่อง agentic AI. Claude เป็น lead ของ R&D task 26% ที่บริษัทเดือนสิงหาคม. ขึ้นจาก 1% เมื่อมีนา. คือ 26 เท่าใน 6 เดือน. ถ้า trajectory นี้ hold. เกินครึ่งของ R&D จะนำโดย model ของตัวเอง ก่อนสิ้นไตรมาส 1 ปีหน้า.

คำว่า lead ใน definition ของ Anthropic คือ. human ตั้งโจทย์ระดับ paragraph. Claude ทำ everything else. ตั้งแต่ literature review. experiment design. code. evaluation. ไปจนถึง writeup. ถ้ารวม collaboration ที่กว้างกว่าคือ. 90% ของ R&D ทั้งหมด ทำร่วมกับ Claude ในระดับใดระดับหนึ่ง.

ตัวเลขที่น่ากลัวกว่านั้นคือ. Anthropic บอกว่ามี 30,000 agent วิ่ง research workload อยู่หลังบ้าน. เทียบกับ headcount human ที่ 1,500 กว่าคน. คือ agent ต่อ human = 20 ต่อ 1 ในกลุ่ม research.

จุดที่สำคัญคือ. เรื่องนี้ไม่ใช่ marketing. เป็น recursive self-improvement ที่เริ่มมี dashboard number update รายเดือน. ก่อนหน้านี้เป็น thought experiment ของ AI safety community. ตอนนี้เป็น metric สาธารณะ.

สำหรับ founder ไทย. ถ้าจะ deploy agent ใน workflow บริษัท. หนึ่ง. ตั้ง metric แบบเดียวกันวันนี้. track % ของ task ที่ AI ทำ leading role vs collaboration vs assist. บริษัทที่ไม่วัด. จะไม่รู้ว่ากำลัง scale หรือ stagnate. สอง. อย่ารอ market ready. deploy narrow agent ใน customer workflow เช่น invoice reconciliation หรือ order intake. แล้ว publish % ของ task ที่ agent lead. metric นี้จะกลายเป็น trust metric ที่ B2B buyer ถามก่อน sign contract. เหมือน uptime ในยุค SaaS.
