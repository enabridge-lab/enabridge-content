---
date: 2026-07-18
slug: salesforce-agentforce-1-2b-arr-agent-economy
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  A giant billboard in editorial isometric style shining over a busy
  enterprise data center. Big bold numbers stacked on the board:
  "$1.2B ARR", "205% YoY", "28.6T TOKENS", "3.8B WORK UNITS".
  A stylized Salesforce cloud silhouette anchors the composition; below,
  streams of blue light flow into rows of servers labeled "AGENTFORCE".
  Deep navy, warm cyan and gold palette, sharp typography, 1:1 aspect,
  no real human faces, readable at 200px thumbnail.
image: images/26-07-18-0609-02-salesforce-agentforce-1-2b-arr-agent-economy.png
---

# Agentforce แตะ $1.2B ARR — enterprise agent economy จบยุค "pilot" แล้ว

## TL;DR
- Salesforce รายงาน Q1 FY27: Agentforce ARR ทะลุ **$1.2B, โต 205% YoY** — เร็วที่สุดที่ enterprise SaaS เคยมี
- ลูกค้าประมวล **28.6 ล้านล้าน token** สะสมและสร้าง **3.8 พันล้าน "Agentic Work Units"** ในไตรมาสเดียว, AWU โต 111% QoQ
- 60%+ ของ Agentforce booking มาจากลูกค้าเดิม expand — สัญญาณว่าคนย้ายจาก pilot ไป production จริง
- Combined Agentforce + Data 360 ARR อยู่ที่ ~$3.4B, โต >200% YoY

## เกิดอะไรขึ้น
Salesforce ประกาศงบ Q1 FY27 เมื่อ 27 พ.ค. — revenue $11.13B (+13% YoY), non-GAAP operating margin 34.8% record, EPS $3.88 (+50%). แต่ตัวเลขที่ทำให้ Wall Street กับ agent ecosystem หยุดฟังคือ Agentforce line: annual recurring revenue ผ่าน **$1.2 พันล้าน**, โต 205% YoY. เมื่อสองไตรมาสก่อน (Q4 FY26) มันเพิ่งอยู่ที่ $800M. ไตรมาสก่อนหน้านั้น $470M

Benioff ในการประชุมนักวิเคราะห์ใช้ metric ใหม่ที่ชื่อ "Agentic Work Unit" (AWU) — วัดว่า agent ทำงานสำเร็จกี่ครั้งจริง ๆ ไม่ใช่ token consumption. Q1 FY27 มี **3.8 พันล้าน AWU** ทั่ว Agentforce กับ Slack — โต **111% quarter-over-quarter**. token consumption สะสม 28.6 ล้านล้าน — เป็นตัวเลข infra ที่สะท้อนว่า workload จริงเกิดขึ้นในระดับที่คู่แข่งยังตามไม่ทัน. อีกหนึ่งข้อมูล: 60%+ ของ booking มาจาก existing customer expansion — ไม่ใช่ deal ใหม่ — pattern เดียวกับ AWS ตอนเข้าปีที่ 5–6 ที่ enterprise เริ่มย้าย workload production เต็มตัว

Salesforce ยัง raise full-year FY27 guidance เป็น $45.9–46.2B revenue กับ operating margin 34.3% — สัญญาณว่า Agentforce ไม่ใช่ค่าใช้จ่ายที่กิน margin แต่กลับกันคือ operating leverage ที่แรงขึ้นเรื่อย ๆ

## ทำไมสำคัญ
ตลอดปี 2025 มีคำถามใหญ่ในวงการ enterprise AI: agent เก็บเงินได้จริงไหม, หรือเป็นแค่ pilot จบก่อน renewal. คำตอบเชิงตัวเลขที่ชัดที่สุดปีนี้คือ Agentforce — เพราะมันมีทั้งการเปิดเผยรายได้ **แยกออกมาเป็น line item ต่างหาก** (สิ่งที่ Microsoft ยังไม่ทำกับ Copilot Studio, Google ยังไม่ทำกับ Gemini Enterprise), และมี usage metric ที่วัดผลจริง ๆ ไม่ใช่แค่ seat licensed

Gartner projection ที่ว่า 40% ของ enterprise application จะ embed AI agent ภายในสิ้นปี 2026 — ก่อนหน้านี้ฟังดูสูงจัด, พอเห็นตัวเลข Agentforce ก็เริ่มดู realistic. $1.2B ARR + growth 205% หมายความว่าถ้าไม่ deceleration ปีหน้าจะแตะ $3–4B — เข้าใกล้ scale ของ Salesforce Data Cloud ที่ใช้เวลา 4 ปีถึงจุดนั้น

Wall Street react ด้วยการ upgrade valuation — CRM share jump 8% หลัง earnings, analyst หลายเจ้าอ้าง Agentforce เป็น "structural inflection." สำหรับ vendor เจ้าอื่น pressure ชัด: ServiceNow, Workday, SAP ต้องเปิดเผยตัวเลข agent revenue ของตัวเองในไตรมาสต่อ ๆ ไป ไม่งั้น analyst จะเดา worst case

## มุม AI Agent Platform
**Builder** ที่สร้าง orchestration / runtime framework ควรมอง "Agentic Work Unit" ให้ดี — เป็น metric แรกที่ enterprise SaaS วัด "work done" แทน "tokens burned." ใครใช้ pricing model ตาม token consumption อย่างเดียวจะเริ่มเจอ pushback จากลูกค้าที่อยาก align ต้นทุนกับ outcome. **Users / business** ที่ยัง deploy agent แบบเป็น pilot ควรตัดสินใจแล้วว่าจะเลือกไปทางไหน — pattern การ expansion จาก existing customer 60%+ ของ Salesforce แปลว่าคนที่ commit เร็วได้ compounding advantage; คนที่รอ "ตลาดชัดกว่านี้" กำลังพลาด window ของการเรียนรู้ deployment. **Ecosystem** — ทุกคนใน ISV / SI ที่ทำ implementation รอบ Salesforce จะเจอ demand สูงมากในอีก 12 เดือน; ในทางกลับกัน vendor คู่แข่ง (Microsoft Copilot Studio, Google Gemini Enterprise, ServiceNow Now Assist) ต้องเร่งพิสูจน์ metric ในระดับเดียวกัน. สำหรับ builder ในไทย — คำถามที่น่าถามคือ integration path ไปยัง Salesforce data model กับ Agentforce runtime ควรอยู่ตรงไหนใน stack ของทีมเรา

## Sources
- [Salesforce Delivers Record First Quarter Fiscal 2027 Results](https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-First-Quarter-Fiscal-2027-Results/default.aspx)
- [Salesforce Q1 FY27 Earnings Conference Call transcript](https://s205.q4cdn.com/626266368/files/doc_financials/2027/q1/Salesforce-Q1-FY27-Earnings-Transcript.pdf)
- [Salesforce: Agentforce Reaches $1.2B ARR, Record Margins Signal Structural Inflection (Longyield)](https://longyield.substack.com/p/salesforce-agentforce-reaches-12b)
- [Agentforce Revenue Surges Past $1B (Salesforce Ben)](https://www.salesforceben.com/salesforce-q1-results-agentforce-hits-1b-arr-as-benioff-takes-aim-at-ai-doubters/)

---

## Audio script
Salesforce ประกาศงบไตรมาส Q1 FY27 แล้ว และตัวเลขที่ทำให้วงการ agent หยุดฟังคือ Agentforce annual recurring revenue ทะลุ 1.2 พันล้านดอลลาร์ โต 205% เทียบกับปีก่อน. แค่สองไตรมาสก่อนหน้านี้มันยังอยู่ที่ 800 ล้าน — แปลว่า scale ขึ้นเร็วที่สุดที่ enterprise SaaS เคยมี. อีกตัวเลขที่น่าสนใจคือ Benioff เอามาใช้ metric ใหม่ชื่อ Agentic Work Unit หรือ AWU — วัดว่า agent ทำงานสำเร็จกี่ครั้งจริง ๆ ไม่ใช่แค่ token consumption. ไตรมาสนี้มี 3.8 พันล้าน AWU โต 111% ในไตรมาสเดียว. 60%+ ของ booking ใหม่มาจากลูกค้าเดิม expand — ไม่ใช่ pilot ใหม่ — สัญญาณว่า enterprise ย้ายจาก pilot ไป production เต็มตัวแล้ว. Wall Street react ทันที CRM share jump 8%, analyst หลายเจ้าใช้คำว่า structural inflection. ในมุม builder — AWU ที่ Salesforce ตั้งขึ้นน่าจะกลายเป็น standard ที่คนอื่นต้องตอบ เพราะ enterprise เริ่มไม่พอใจกับ pricing ตาม token อีกต่อไป อยากจ่ายตาม outcome. สำหรับ vendor คู่แข่งอย่าง Microsoft Copilot Studio, Google Gemini Enterprise, ServiceNow Now Assist ก็ pressure ชัด — ต้องเปิดตัวเลข agent revenue ของตัวเองในไตรมาสหน้า ไม่งั้น analyst จะเดา worst case. สำหรับทีมไทย คำถามคือ integration path ไปยัง Salesforce ควรอยู่ตรงไหนใน stack ของเรา
