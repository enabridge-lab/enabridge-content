---
date: 2026-11-13
slug: mercor-750m-agent-eval-benchmark
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  A cinematic editorial grading hall full of giant wall-mounted monitors — each
  screen shows a different AI agent icon being scored against a unique
  enterprise-specific rubric card. The central panel glows with a huge number
  "$20B VALUATION" and below it "$750M SERIES D". A clean serif mark "MERCOR"
  anchors the top. In one corner, a smaller ticker reads "$2B ARR" with Nvidia
  and Salesforce logo chips floating beside it. Editorial isometric style, deep
  teal + warm amber palette, 1:1 aspect, high contrast so the dollar numbers
  stay readable at 200px, no real human faces.
image: images/26-11-13-0604-01-mercor-750m-agent-eval-benchmark.png
---

# Mercor $750M ที่ $20B valuation — การประเมิน AI Agent กลายเป็นธุรกิจใหญ่สุดก่อนที่ agent เองจะโต

## TL;DR
- Mercor ปิด Series D ที่ $750M valuation $20B (จาก $10B ตุลา 2025) — Nvidia, Salesforce, Benchmark, Felicis, Apollo ร่วมลง
- Annualized revenue แตะ $2B เรียบร้อยแล้วตั้งแต่ก่อน Q3 — ตัวเลขที่ Scale AI และ Surge AI ไม่เคยเปิด
- เงินไปสร้าง custom benchmark เฉพาะบริษัท + "realistic environment" ให้ agent ฝึกงานระดับ professional

## เกิดอะไรขึ้น
วันที่ 10 พฤศจิกายน Mercor ประกาศ Series D $750M ที่ valuation $20B — ตัวเลขที่ทำให้บริษัทเพิ่งอายุไม่ถึงสามปีกลายเป็นหนึ่งใน private company ด้าน AI ที่ valuation สูงที่สุดนอกกลุ่ม foundation model lab เอง รอบนี้ไม่มี lead ประกาศชัด แต่รายชื่อ participant ชี้ชัดว่าใครยังเดิมพันตลาดนี้ — Nvidia และ Salesforce เข้าเป็น corporate investor, Benchmark, Felicis, Fundomo, และ fund ภายใต้ Apollo ร่วมด้วย

ตัวเลขที่สำคัญกว่า valuation คือ revenue — Mercor ยืนยันว่า annualized revenue run rate ทะลุ $2B ไปแล้วตั้งแต่กลางปี เป็นการเปิดเผยที่ทำให้ Scale AI (ที่ Meta จ่ายไป $14B ปีก่อน) และ Surge AI (ที่ยังเงียบเรื่องตัวเลข) ต้องกลายเป็น benchmark ที่หลวมขึ้น business model ของ Mercor สร้างขึ้นจาก 2 ด้าน — ด้านหนึ่งคือ matching บุคคล (expert ที่มีทักษะวิชาชีพ — แพทย์, ทนาย, นักบัญชี, developer senior) เข้ากับ lab ที่ต้องการ expert labor สำหรับ post-training; อีกด้านคือ enterprise evaluation — สร้าง custom benchmark ที่วัดว่า agent ตัวหนึ่งเชื่อถือได้ไหมในการทำงานเฉพาะของบริษัท X

ปีนี้ Mercor ซื้อ Deeptune ซึ่งใช้เวลาสองปีสร้าง "realistic environment" ของ enterprise application กว่าหลายร้อยตัว — Salesforce, Workday, SAP, Epic, Oracle — ให้ agent ฝึกงานในสภาพแวดล้อมใกล้ production สิ่งนี้คือกำแพงที่ยากขึ้นเรื่อย ๆ สำหรับคู่แข่ง เพราะ synthetic environment จะวัด "agent ทำได้ไหม" แม่นกว่า static benchmark แบบ MMLU หรือ SWE-bench มาก

## ทำไมสำคัญ
Pattern สำคัญคือ — ก่อนที่ตลาด agent จะโตเต็ม market cycle ถัดไปกำลังเกิด infrastructure ของ "วัดว่า agent ทำงานได้จริงไหม" เติบโตเร็วกว่า agent เอง ตัวเลข $2B ARR ของ Mercor ที่โตก่อน enterprise agent deployment ระดับล้าน seat แปลว่า lab และ enterprise จ่ายเงินให้ evaluation + training environment มากกว่าที่คนทั่วไปคิด

ทำไมถึงจ่ายเยอะขนาดนี้ — เพราะ CFO และ CIO ต้องการเลขที่ defendable ก่อนจะ sign off budget ให้ agent ไป autonomous ทำงาน คำว่า "เรา A/B test แล้ว agent ชนะ human ใน benchmark X ที่เป็น proxy ของงานจริง" กลายเป็น prerequisite สำหรับ procurement — ไม่ต่างจากที่ security team ต้องการ penetration test report ก่อนจะ deploy โปรดักต์ใหม่

Caveat — $20B สำหรับบริษัทที่ภายในยังมี expert-matching marketplace เป็นหลักฐาน revenue (สาย labor arbitrage ที่ scale ได้แต่ margin จำกัด) + eval product ที่เพิ่งแยกเป็นสายเอง ตัวเลข ARR ที่ประกาศเป็น mixed ของสองธุรกิจ ถ้าแบ่งแยกออกและ eval business ยังเล็กกว่าคาด valuation อาจถูก revalue เมื่อ growth slow ลง สิ่งที่ต้องจับตา — Nvidia และ Salesforce ลงเงินด้วยไม่ใช่เพราะหวัง return ทางเงินอย่างเดียว แต่เพราะอยาก lock access ไปที่ eval infrastructure เพื่อป้องกันไม่ให้คู่แข่งใช้วัด agent ของตัวเอง

## มุม AI Agent Platform
Builders — ถ้าคุณกำลังสร้าง agent framework หรือ vertical agent อย่างซีเรียส คำว่า "benchmark ของเราเอง" กลายเป็นอาวุธสำคัญกว่า model accuracy สักครั้ง สิ่งที่น่าสนใจคือ moat ของ evaluation infrastructure สูงกว่าที่คิด — สร้าง synthetic environment ที่ fidelity สูงต้องใช้เวลา 2+ ปี (ดู Deeptune) และต้องเข้าถึง enterprise app ที่ licensing ซับซ้อน ถ้าคุณเป็น startup เล็กคงไม่สู้ Mercor ได้ตรง ๆ แต่ยัง niche vertical (industry-specific eval) ที่ยังว่าง

Users/business — ก่อน sign contract agent platform ตัวต่อไป ถามคำถามเดียว "evaluation methodology เค้าใช้อะไร" ถ้า vendor ตอบว่า "เรา test กับ benchmark public" เลิกเจรจาได้เลย เพราะ benchmark public ไม่สะท้อน workflow เฉพาะของคุณ Enabridge และ system integrator ไทยที่ deploy agent ให้ enterprise ควรเสนอ custom eval environment เป็น deliverable (เก็บเงินแยก) ไม่ใช่ freebie — สิ่งนี้คือ defensible service ที่ราคา commodity ไม่ลงได้ง่าย

Ecosystem — Scale AI (Meta ซื้อ) + Surge AI (private) + Mercor กำลังก่อตัวเป็น "eval cartel" ที่ควบคุม training data + eval environment ของ foundation lab + enterprise พร้อมกัน ถ้า Linux Foundation หรือ open source alternative ไม่เร่งสร้าง public evaluation standard ภายใน 12 เดือน อำนาจกำหนด "agent ตัวไหนเก่ง" จะตกอยู่ใน 3 บริษัทนี้แบบไม่มี checks and balances

## Sources
- [Mercor raises $750M at $20B valuation to take AI agent evaluation to enterprises (SiliconANGLE)](https://siliconangle.com/2026/11/10/mercor-raises-750m-at-20b-valuation-to-take-ai-agent-evaluation-to-enterprises/)
- [Mercor doubles valuation to $20B with $750M Series D to train and test AI agents for enterprises (TechFundingNews)](https://techfundingnews.com/mercor-doubles-valuation-to-20b-with-750m-series-d-to-train-and-test-ai-agents-for-enterprises/)
- [Mercor Hits $20B Valuation After $750M Series D to Train and Test AI Agents (The AI Insider)](https://theaiinsider.tech/2026/11/11/mercor-hits-20b-valuation-after-750m-series-d-to-train-and-test-ai-agents/)
- [Mercor raises $750m to expand AI evaluation tools for enterprises (Tech Monitor)](https://www.techmonitor.ai/news/mercor-raises-750m-to-expand-ai-evaluation-tools-for-enterprises)

---

## Audio script
Mercor ปิด Series D ที่ 750 ล้านเหรียญ valuation 20 พันล้านเหรียญเมื่อวันที่ 10 พฤศจิกายน เพิ่มขึ้นเป็นสองเท่าจากรอบตุลาคมปีที่แล้ว รายชื่อ investor ชี้ชัดว่าใครยังเดิมพันตลาด evaluation ของ AI Agent — Nvidia, Salesforce เข้ามาเป็น corporate investor, Benchmark และ Felicis กลับมาลง, Apollo ร่วมด้วย ตัวเลขที่สำคัญกว่า valuation คือ revenue annualized run rate ทะลุ 2 พันล้านเหรียญไปแล้วตั้งแต่กลางปี ทำให้ Scale AI และ Surge AI ต้องกลายเป็น benchmark ที่หลวมขึ้น ธุรกิจ Mercor มีสองด้าน ด้านแรกคือ matching expert วิชาชีพกับ AI lab สำหรับ post-training ด้านที่สองคือ enterprise evaluation สร้าง custom benchmark เฉพาะบริษัท ปีนี้ Mercor ซื้อ Deeptune ที่สร้าง realistic environment ของ enterprise app กว่าร้อยตัว ให้ agent ฝึกในสภาพแวดล้อมใกล้ production ซึ่งเป็น moat ที่สร้างยาก pattern ที่สำคัญคือก่อนที่ตลาด agent จะโตเต็ม infrastructure ของการวัดว่า agent ทำงานได้จริงไหมโตเร็วกว่า agent เอง CFO และ CIO ต้องการเลขที่ defendable ก่อน sign budget ให้ agent autonomous สำหรับคนที่ขาย agent platform ในไทย คำว่า custom evaluation environment ควรกลายเป็น deliverable ที่เก็บเงินแยก ไม่ใช่ freebie มันคือ defensible service ที่ commodity ยากสำหรับ system integrator
