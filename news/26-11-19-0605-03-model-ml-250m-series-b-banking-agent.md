---
date: 2026-11-17
slug: model-ml-250m-series-b-banking-agent
topic: use-case
reading_time_min: 4
sources: 2
image_prompt: |
  An editorial isometric illustration of a London banking floor at dusk. A
  single trading desk with three monitors glowing teal; beside it a robotic
  agent silhouette holds an open briefcase labeled "MODEL ML — PERSONAL AGENT".
  Behind the desk, a bar chart rises sharply with labels "12x ARR" and
  "26x DAU" at the top. A separate ticker overhead shows "$250M SERIES B"
  and "$1.5B VALUATION". Big Ben silhouette barely visible through the window.
  Soft indigo, warm amber palette, clean editorial style, 1:1 aspect, no
  real human faces (silhouettes OK), high contrast so numbers read at 200px
  thumbnail.
image: images/26-11-19-0605-03-model-ml-250m-series-b-banking-agent.png
---

# Model ML ปิดราคา $1.5B ของ "AI agent ส่วนตัวสำหรับ banker" — ARR โต 12 เท่า, DAU โต 26 เท่า, มี fine-tuned model เองที่ถูกกว่า frontier 50 เท่า

## TL;DR
- Model ML (London) ปิด Series B $250M ที่ valuation $1.5B — co-lead โดย General Atlantic และ QED Investors; total funding แตะ $350M จาก $75M Series A (พ.ย. 2025) และ $12M seed (ก.พ. 2025)
- ARR Q3 2026 โต 12x YoY, DAU โต 26x YoY; "deeply embedded" ใน bank ขนาดใหญ่ (ไม่ disclose ชื่อ) — model-agnostic + fine-tuned own open-source model ที่ cost ~2% ของ frontier และวิ่งเร็วกว่า ~5 เท่า
- Positioning ตรงข้ามคู่แข่ง (Rogo, Hebbia, Unique, Eunice, Gradient Labs) — เป็น "personal agent" สำหรับ individual banker ไม่ใช่ task-specific tool หรือ general chatbot

## เกิดอะไรขึ้น
วันที่ 17 พฤศจิกายน Model ML ของสองพี่น้อง Chaz และ Arnie Englander ประกาศปิด Series B $250M ที่ valuation $1.5B — co-lead โดย General Atlantic และ QED Investors พร้อม Evolution Equity Partners, Airtree, Y Combinator, FT Partners รวม cap table รอบนี้ยาวกว่า Series B ปกติ Total funding ของบริษัทรวม $350M หลังจาก Series A $75M เมื่อพฤศจิกายน 2025 และ seed $12M เมื่อกุมภาพันธ์ 2025 — คือ 1 ปี 9 เดือนจาก seed ถึง $1.5B

Product ของ Model ML คือ personal AI agent ที่ไม่ใช่ "chatbot ที่คุณถามคำถาม" หรือ "task tool ที่ทำงาน 1 อย่าง" แต่เป็น agent ส่วนตัวของ individual banker/consultant/investment professional ที่อยู่ใน infra ของบริษัท run ตลอด 24 ชั่วโมง และ personalize มากขึ้นเมื่อใช้ไปเรื่อย ๆ Use case ยกตัวอย่างใน pitch: research news ของบริษัทลูกค้าแล้วเตรียม output ใน format ที่ firm ใช้ประจำ — คือ workflow ที่ junior analyst ใช้เวลา 3-4 ชั่วโมงต่อวัน

ตัวเลข traction: Q3 2026 ARR โต 12x YoY, DAU โต 26x YoY (ไม่เปิดเผยตัวเลข absolute) Englander บอก Tech Funding News ว่า product "deeply embedded inside some of the world's largest institutions" แต่ไม่ยอมเปิดชื่อ bank — pattern ที่ financial-services vendor เข้าใจกัน (NDA + reputation risk ของ bank ถ้า agent พลาด) Model ML ถือ ISO/IEC 27001:2022 + SOC 2 Type II — เป็น table stakes ของ regulated buyer ที่ต้องเช็ค

Technical angle ที่ underrated: Model ML เริ่มใช้ own fine-tuned open-source model มากขึ้น บริษัทอ้างว่า cost ~2% ของ frontier model และวิ่งเร็วกว่า ~5 เท่า — เป็น hybrid routing ที่ task heavy ไป frontier, task routine ใน own model

## ทำไมสำคัญ
วงการ "AI agent สำหรับ banker" มี vertical player เยอะแล้ว — Rogo กับ Hebbia เน้น research tool, Unique ทำ FinanceGPT, Eunice ทำ due diligence agents, Gradient Labs โฟกัส regulated financial operations การที่ General Atlantic + QED ยอมจ่าย $1.5B valuation กับ Model ML signal ว่า investor เชื่อ "personal agent ของ individual" เป็น category แยกจาก "task tool สำหรับ team" — bet ว่า agent ที่รู้จัก user ลึก, personalize ตาม style, และ run ตลอดเวลา จะกลายเป็น stickier product กว่า point tool

ตัวเลข ARR 12x + DAU 26x ที่โตไม่พร้อมกันคือ signal ที่สำคัญ — DAU โตเร็วกว่า ARR แปลว่า land phase (ให้ user ลองใช้) กำลังเร็วกว่า expand phase (ขาย seat เพิ่ม) ซึ่ง pattern นี้ถ้า play ถูกจะทำให้ ARR ไล่ตามใน 2-3 ไตรมาสข้างหน้า (land-and-expand classic) แต่ถ้าไม่ตามจะกลายเป็น churn risk ที่ CFO ตั้งข้อสังเกต

Fine-tuned own model ที่ "2% ของ cost + 5x เร็วกว่า" ไม่ใช่เรื่องเล็ก — มันบอกว่า Model ML กำลัง decouple จาก frontier lab pricing ซึ่งเป็น risk ที่ founder vertical agent หลายคนกังวล (ถ้า OpenAI/Anthropic ขึ้นราคา margin หาย) การสร้าง own model ที่ specialize task ของ banker (คำศัพท์การเงิน, format document, compliance tone) คือ moat ที่ยั่งยืนกว่า wrapper รอบ GPT

## มุม AI Agent Platform
**Builders** — Pattern ของ Model ML (personal agent + own fine-tuned model + run ใน infra ลูกค้า) เป็น template ที่ vertical agent platform ควรทำตาม ไม่ใช่สร้าง chatbot ที่คนเปิด browser เข้ามา framework ที่ support "agent-as-persistent-session-per-user + model routing + on-prem option" จะมี market ใน regulated vertical (law firm, accounting firm, healthcare)

**Users/business** — สำหรับธนาคารไทยที่มี banker 500-5,000 คน Model ML เป็น proof of concept ว่า "personal agent per professional" ทำได้จริง Enabridge ที่ลูกค้าในกลุ่ม financial services ไทย (ธนาคาร, บลจ., Wealth Management) ควร pitch ว่า agent platform ของ Enabridge ให้อะไรที่ Model ML ไม่มี — ภาษาไทย + กฎ regulator ไทย (ธปท., ก.ล.ต.) + integration กับ core banking Thai (Infosys Finacle, Temenos T24) คือ 3 moat ที่ global vendor สร้างยาก

**Ecosystem** — ถ้า Model ML scale ได้ใน 2-3 ปีข้างหน้า จะกดดัน Bloomberg Terminal (ราคา $25k/user/ปี) — Bloomberg Terminal คือ default ของ banker มา 40 ปี แต่ UX เป็น keyboard shortcut ยุค 80s ถ้า personal agent ที่รู้ context ของ deal + draft output ได้ ทำงานแทน terminal ลูกค้ายอมจ่าย $25k อยู่ไหม — เป็นคำถามเดียวกับที่ Bloomberg ควรกังวลตั้งแต่ 2 ปีที่แล้ว

## Sources
- [London's Model ML raises $250M from General Atlantic and QED to put AI agents inside banks (Tech Funding News)](https://techfundingnews.com/londons-model-ml-raises-250m-from-general-atlantic-and-qed-to-put-ai-agents-inside-banks)
- [AI Agents News Brief: November 17, 2026 (AI Agents Directory)](https://aiagentsdirectory.com/news/ai-agents-news-brief-november-17-2026)

---

## Audio script
ข่าวที่สามวันนี้ Model ML ที่ลอนดอน ปิด Series B 250 ล้านเหรียญที่ valuation 1.5 พันล้าน co-lead โดย General Atlantic และ QED Investors รวม total funding 350 ล้าน บริษัทผ่านจาก seed ถึงยูนิคอร์นใน 1 ปี 9 เดือน Model ML เป็น personal AI agent สำหรับ banker consultant และ investment professional ไม่ใช่ chatbot หรือ task tool แต่เป็น agent ส่วนตัวที่อยู่ใน infra ของบริษัท รันตลอด 24 ชั่วโมง และ personalize มากขึ้นเมื่อใช้ไปเรื่อย ตัวอย่าง use case คือ research ข่าวบริษัทลูกค้าแล้วเตรียม output ใน format ที่ firm ใช้ประจำ ซึ่งเป็น workflow ของ junior analyst ตัวเลข Q3 น่าสนใจ ARR โต 12 เท่า DAU โต 26 เท่า แต่ไม่เปิดเผยตัวเลข absolute บริษัทบอกว่า product อยู่ใน bank ขนาดใหญ่ของโลก แต่ไม่ยอมบอกชื่อ และถือ certification ISO 27001 และ SOC 2 Type II ซึ่งเป็น table stakes ของ buyer regulated จุดที่น่าทึ่งที่สุดคือ Model ML สร้าง own fine-tuned open-source model ที่ cost ประมาณ 2 เปอร์เซ็นต์ของ frontier model และวิ่งเร็วกว่า 5 เท่า แปลว่าบริษัทกำลัง decouple จาก price ของ OpenAI หรือ Anthropic ซึ่งเป็น risk ที่ founder vertical agent หลายคนกังวล สำหรับธนาคารไทยที่มี banker 500 ถึง 5,000 คน Model ML เป็น proof ว่า personal agent per professional ทำได้จริง Enabridge ที่ลูกค้าในกลุ่มการเงินไทยควร pitch ว่าจุดต่างคือ ภาษาไทย กฎ regulator ไทย และ integration กับ core banking ไทย ซึ่งเป็น 3 moat ที่ global vendor สร้างยาก
