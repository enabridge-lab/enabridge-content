---
date: 2026-07-04
slug: cisco-90k-employees-personal-agent-token-diet
topic: use-case
reading_time_min: 3
sources: 3
image_prompt: |
  A giant Cisco headquarters building at dawn with 90,000 tiny glowing office
  windows, each window shaped like a small AI assistant icon. Foreground: a
  massive stacked billboard reading "90,000 EMPLOYEES", "1 AGENT EACH", and
  below it in smaller bold text "NO FRONTIER TOKENS BURNED". A router-like
  hub in the sky routes light beams to cheaper models, not to a giant
  frontier-model tower off to the side. Editorial isometric style, high
  contrast, 1:1 aspect, readable at 200px thumbnail, no real human faces.
image: images/26-07-04-0609-01-cisco-90k-employees-personal-agent-token-diet.png
---

# Cisco แจก AI Agent ให้พนักงาน 90,000 คน — แต่ CFO บอก "ไม่เผา token ที่ frontier model"

## TL;DR
- Cisco ประกาศ (1–2 ก.ค.) roll out AI agent ส่วนตัวให้พนักงาน 90,000 คนเริ่มปีงบใหม่ปลายกรกฎาคม — Fortune 500 rollout ขนาดใหญ่ที่สุดครั้งหนึ่งของปี
- CFO Mark Patterson วางสถาปัตยกรรมแบบ "efficient routing" — คำถามง่ายส่งโมเดลถูก, คำถามยากค่อยส่ง frontier ("we're not going to burn a whole bunch of tokens with frontier models")
- ตัวเลข: AI ร่าง MD&A 80–90% ของ first draft, FY25 orders $2B, FY26 guidance ขยับเป็น $9B ธุรกิจ hyperscaler; หุ้นขึ้น 53% YTD

## เกิดอะไรขึ้น
Fortune รายงานเมื่อวันที่ 1 กรกฎาคม ว่า Cisco — บริษัทอันดับ 83 ของ Fortune 500 — เตรียม deploy AI agent ส่วนตัวให้พนักงานทุกคน 90,000 คน เริ่มต้นในปีงบประมาณใหม่ที่จะเริ่มปลายเดือนกรกฎาคมนี้ agent แต่ละตัวจะทำหน้าที่เป็น personal assistant คอยตอบคำถาม, จัดการงาน, และที่สำคัญที่สุด — routing คำถามไปให้โมเดลที่เหมาะสมกับความยาก ไม่ใช่ยิง frontier ทุกครั้ง

CFO คนใหม่ Mark Patterson (เข้ารับตำแหน่งกรกฎาคม 2025) ให้สัมภาษณ์ที่กลายเป็น talking point ทั่ววงการ: "We're not going to burn a whole bunch of tokens with frontier models" เขาเล่าว่า Cisco ออกแบบ architecture ให้ agent วิเคราะห์ intent ของคำถามก่อน — คำถาม routine เช่น "ขอ code snippet ของ router config" ส่งเข้าโมเดลเล็ก/cheap, คำถามที่ต้องใช้ reasoning จริง ๆ (เช่น debug regression ที่กระจายอยู่หลาย service) ถึงจะ escalate ไป frontier

Patterson ให้ตัวเลข concrete: ตอนนี้ AI ร่าง 80–90% ของ first draft ของ Management Discussion & Analysis (MD&A) ในเอกสาร filing สาธารณะของบริษัท ทีม finance ใช้เวลาน้อยลงกับการเขียน draft แรก และหันไป focus การ review/edit/audit แทน ในภาพใหญ่ Cisco รายงาน hyperscaler orders $2B ใน FY25 และขยับ guidance FY26 เป็น $9B — หุ้นขึ้นประมาณ 53% ตั้งแต่ต้นปี แตะ $117 ปลายมิถุนายน

## ทำไมสำคัญ
ประเด็นที่ under-reported คือ Cisco ไม่ได้ประกาศ "เราซื้อ ChatGPT Enterprise ให้ทุกคน" — แต่ประกาศ "เราสร้าง agent platform ภายในที่รู้จักเลือกโมเดล" นี่คือ signal ที่ CFO/CIO ทั่วโลกกำลังจะเข้าใจ: การให้พนักงานเข้าถึง frontier ทุกคนไม่ scale ทั้งด้าน cost และ latency; วิธีที่ scale ได้จริงคือมี agent runtime + routing layer อยู่ตรงกลาง

เทียบกับ Salesforce ที่เพิ่งเปลี่ยนไปใช้ pay-per-resolution ($2 ต่อ resolution) กับ Agentforce Help Agent — Cisco กำลังเดินคนละสูตร: internal platform + BYO routing + cheap models เป็นหลัก, frontier เป็นข้อยกเว้น ทั้งสองสูตรตอบโจทย์เดียวกัน — "unit economics ของ agent ต้องเปลี่ยน" — แต่คนละมุม Cisco ทำจากด้าน infra, Salesforce ทำจากด้าน pricing model

ที่น่าจับตาอีกเรื่องคือ Cisco ประกาศ rollout ใน month เดียวกับที่ประกาศ layoff — CX Magazine ตั้งคำถามว่าจะสร้าง trust กับพนักงานที่กลัวถูก AI แทนที่ยังไง คำตอบของ Cisco คือ position เป็น "personal assistant" ไม่ใช่ "co-worker" — ให้ agent ทำ prep work (draft, search, summary) ให้พนักงาน focus decision making ที่ agent ยังทำไม่ได้

## มุม AI Agent Platform
- **Builders**: routing layer + model gateway เป็น commodity ที่ต้องมีในทุก enterprise stack — SnapLogic, Portkey, LiteLLM, Datadog LLM Observability กำลังแย่งชิงชั้นนี้; ที่ Cisco น่าจะสร้างเองอยู่ในบ้าน แต่ pattern จะบังคับให้ทุกคนต้องเลือกว่าจะซื้อหรือสร้าง
- **Users/business**: จำนวน head count × cost/query = สมการที่ CFO ต้อง defend; Cisco แสดงให้เห็นว่าสามารถ deploy scale ระดับหมื่นคนได้ถ้าคิด architecture ดี — Fortune 500 ที่ยัง pilot อยู่จะโดนถามว่า "ทำไมยังไม่ scale"
- **Ecosystem**: OpenAI/Anthropic ต้องยอมรับว่า workload ส่วนใหญ่ของ enterprise agent จะไม่ใช่ frontier — cheaper tier (Haiku 4.5, Luna, GPT-5.6 Terra) คือสมรภูมิที่จะโต และ margin จะบางลง

## Sources
- [Cisco is rolling out AI agents to every single one of its 90,000 employees — Fortune](https://fortune.com/2026/07/01/cisco-cfo-ai-agents-finance-employees-mark-patterson/)
- [Cisco to roll out AI agents to all 90000 employees from August — Business Today](https://www.businesstoday.in/technology/artificial-intelligence/story/cisco-to-roll-out-ai-agents-to-all-90000-employees-from-august-540580-2026-07-02)
- [Cisco's AI Agent Rollout Lands the Same Month as Layoffs — CX Magazine](https://cxm.world/employee-experience/cisco-ai-agent-rollout-layoffs-employee-trust/)

---

## Audio script
วันนี้เรามีข่าวใหญ่จาก Cisco — บริษัท networking ที่มีพนักงาน 90,000 คนทั่วโลก ประกาศจะแจก AI agent ส่วนตัวให้พนักงานทุกคน เริ่มปลายเดือนกรกฎาคมนี้ ครอบคลุมทั้งบริษัท ทีเด็ดอยู่ที่คำพูดของ CFO คนใหม่ Mark Patterson เขาบอกว่า "We're not going to burn a whole bunch of tokens with frontier models" แปลว่า Cisco จะไม่ยิงทุกคำถามเข้า frontier model เพราะแพงเกินไป แต่จะสร้าง routing layer เอง คำถามง่ายส่งเข้าโมเดลถูก คำถามยากถึงค่อย escalate นี่คือ signal ใหญ่ต่อทุก enterprise ที่กำลังคิดจะ scale agent — pilot มันง่าย แต่พอ deploy หมื่นคนพร้อมกัน unit economics จะไม่ยอมให้คุณใช้ frontier ทั้งบ้าน คุณต้องมี agent runtime มี model gateway มี observability ตรงกลาง Cisco เลยกลายเป็น case study ที่ CFO ทุกคนจะยกมาอ้าง และตอนนี้ AI ของเขาช่วยร่าง MD&A ในเอกสาร filing สาธารณะได้ถึง 80–90 เปอร์เซ็นต์ของ first draft แล้ว หุ้นขึ้น 53 เปอร์เซ็นต์ตั้งแต่ต้นปี ต่อไปน่าจับตาว่าสัปดาห์นี้จะมี Fortune 500 อีกกี่รายที่ออกมาประกาศตามในสูตรเดียวกัน
