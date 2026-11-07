---
date: 2026-11-07
slug: agiloft-execution-agents-mcp-clm
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a sleek contract-ops command room.
  Three robot-agent silhouettes labeled "BULK UPDATE", "CONTRACT REQUEST"
  and "ESIGNATURE" each hold a stack of glowing documents on a conveyor
  belt. A big back wall banner reads "FROM ANALYZE TO EXECUTE". A smaller
  side banner reads "MCP PREVIEW" with the Claude symbol beside it. In
  the foreground an open folder labeled "VALUE LEAKAGE" is being sealed
  with a wax stamp. Clean editorial style, deep green and warm cream
  palette, 1:1 aspect, high contrast for 200px thumbnail, no real human
  faces (silhouettes OK).
image: images/26-11-08-0604-05-agiloft-execution-agents-mcp-clm.png
---

# Agiloft เปิดตัว 3 agent "ทำงานจริง" + MCP สำหรับ Claude — contract AI เปลี่ยนจาก "analyze" เป็น "execute"

## TL;DR
- Agiloft ปล่อย 3 agent — Bulk Update, Contract Request, eSignature Agent for Adobe Acrobat Sign — เน้น execute multi-step task ไม่ใช่แค่ analyze contract
- Preview MCP support — Claude และ external agent อื่นเข้ามา act บน Agiloft data ได้ โดย inherit permission + security control เดิม
- Framing ของ CPO Jason Barnwell: ตัด "value leakage" ซึ่งคือ admin overhead ที่ทำให้ contract term หาย

## เกิดอะไรขึ้น
วันที่ 5 พฤศจิกายน Agiloft — contract lifecycle management (CLM) vendor ระดับ enterprise ที่ customer เป็น Fortune 500 เช่น Chevron, Pfizer, Allianz — เปิดตัว agent 3 ตัวใหม่ใน Ask AI ecosystem ของตัวเอง ทุกตัวถูกออกแบบให้ "execute" ไม่ใช่ "analyze":

1. **Bulk Update Agent** — รับ instruction "ไปอัปเดต status ของ contract 400 ฉบับที่ค้างอยู่ให้ reflect renewal term ใหม่" แล้วทำเองทั้งหมด (reconcile field, trigger approval workflow, log change) แทนที่ user ต้อง bulk edit ทีละ record
2. **Contract Request Agent** — business user พิมพ์ "ต้องการ NDA กับ vendor นี้ มี confidentiality 2 ปี exclusive clause 1 ปี" agent หา request form ที่ถูก, ตรวจ permission ของ user, submit เข้า workflow
3. **eSignature Agent for Adobe Acrobat Sign** — orchestrate flow ของ send-for-signature, follow up กับ counter-party ที่ยังไม่เซ็น, log การเซ็นเข้า contract repository, trigger activation step

ข่าวที่ซ่อนอยู่ใต้ 3 agent คือ **MCP preview** — Agiloft เปิดให้ external agent (Claude โดย explicit mention) เข้ามา invoke action ใน CLM ผ่าน MCP server โดย respect permission scope เดิม (user A เห็นได้แค่ contract ที่ตัวเองมี access, agent ที่ act ใน name ของ user A ก็เห็นแค่นั้น) นี่คือ pattern ที่ enterprise software vendor ชั้นนำเริ่มทำแทบทุกราย — expose agent surface ผ่าน MCP ให้ customer เอา agent ของตัวเอง (หรือ Claude/ChatGPT) มา drive ได้

## ทำไมสำคัญ
**"Execution gap" เป็น narrative หลักของ enterprise agent ปี 2026** — AI ที่ analyze (summary, risk score, clause extraction) ขายได้มา 2 ปีแล้ว แต่ ROI ที่ CFO วัดได้ยากเพราะมันลด read time ไม่ลด work ที่ต้องทำ — การที่ Agiloft ย้ายไป execute (ทำ work จริง: update, request, sign) เป็น direction ที่ทั้งวงการต้องไป เพราะเป็น metric ที่ CFO วัดได้ตรง (count ของ contract ที่ update เอง, ชั่วโมงที่ paralegal ไม่ต้องทำ bulk edit)

MCP preview สำคัญเป็นลำดับ — มันแปลว่า Agiloft เลือก **"not winner-take-all"** architecture การเปิด MCP server ให้ Claude/external agent เข้ามาทำแทนที่จะ lock customer อยู่ใน Ask AI อย่างเดียว เป็น move ที่สะท้อนว่า vendor enterprise ที่ ชนะในปี 2027 คือคนที่ยอม distribute agent surface ให้ customer เลือก runtime เอง — vs vendor ที่พยายาม own agent end-to-end แล้วลูกค้าจะเลือกคน open กว่า

เทียบกับคู่แข่ง — Icertis ออก ExploreAI (analyze-focused), Ironclad ออก Jurist (AI contract lawyer, analyze + draft), DocuSign มี CLM agent — ไม่มีใครในกลุ่มนี้ประกาศ MCP preview อย่างเป็นทางการ Agiloft เป็น vendor แรกใน CLM tier 1 ที่ commit (ใน language ของ press release) — เป็น differentiation ที่สามารถเป็น customer wedge ได้ ถ้า buyer side value interoperability

Open question ที่ยังไม่มีคำตอบ: **"controlled handoff ใน contract ที่มี consequence สูงจะ scale ได้ไหม"** — การอนุมัติ change order $50K ด้วย agent อย่างเดียวโดยไม่มี human ใน loop ยัง risky; Agiloft bet ว่า permission control ที่ layer อยู่ตรง MCP จะคุมได้ แต่ real-world failure mode อาจมาจาก edge case ที่ agent ไม่รู้ว่าตัวเองไม่รู้

## มุม AI Agent Platform
**Builders** — ถ้าคุณกำลัง build vertical agent surface บน enterprise SaaS การ bet ตอนนี้คือ **expose MCP server เป็น default** ไม่ใช่ feature premium การไม่มี MCP แปลว่า customer ที่มี Claude/ChatGPT อยู่แล้วจะ bypass คุณไป drive ด้วย generic agent ซึ่งลด stickiness lesson จาก Agiloft: expose "action" ไม่ใช่แค่ "data" — agent ที่อ่าน data ของคุณได้แต่ action ไม่ได้ สุดท้ายจะถูก replace ด้วย agent ที่ action ได้

**Users / business** — องค์กรที่ใช้ CLM หรือ enterprise app ที่มี workflow repetitive สูง ตอนนี้ควร audit ว่า vendor expose MCP หรือ equivalent agent surface ไหม การตั้งคำถามใน vendor review ปี 2027 ควรรวม "MCP roadmap" และ "ยอมให้ external agent รันบน data ไหม" — ถ้า vendor ตอบ "ไม่" คุณกำลังอยู่ใน walled garden ที่ constrain agent strategy ของตัวเอง

**Ecosystem** — ถ้า Agiloft สำเร็จกับ MCP play, คู่แข่ง CLM ทั้งหมดต้อง follow ภายใน 6 เดือน pattern นี้จะ spill ไป vertical อื่น (ITSM, HRIS, ERP) ภายใน 2027 — ส่งผลให้ Anthropic ที่ steward MCP ได้ positioning ที่แข็งแรงขึ้น เพราะ protocol ของตัวเองกลายเป็น default สำหรับ enterprise agent integration

## Sources
- [Agiloft Targets Enterprise Value Leakage with New Suite of Execution-Focused AI Agents (PR Newswire)](https://www.prnewswire.com/news-releases/agiloft-targets-enterprise-value-leakage-with-new-suite-of-execution-focused-ai-agents-302929642.html)
- [Agiloft Adds Three AI Agents for Multi-Step Contract Tasks (Unite.AI)](https://www.unite.ai/agiloft-adds-three-ai-agents-for-multi-step-contract-tasks/)
- [Agiloft Deploys Execution-Focused AI Agents to Plug Procurement Value Leaks (BriefGlance)](https://briefglance.com/articles/agiloft-deploys-execution-focused-ai-agents-to-plug-procurement-value-leaks)

---

## Audio script
Agiloft ซึ่งเป็น contract lifecycle management vendor ระดับ enterprise ประกาศวันที่ 5 พฤศจิกายน เปิดตัว agent 3 ตัวใหม่ ทุกตัวถูกออกแบบให้ execute ไม่ใช่แค่ analyze ตัวแรก Bulk Update Agent รับคำสั่งแล้วไปอัปเดต contract หลายฉบับพร้อมกัน ตัวที่สอง Contract Request Agent ให้ business user พิมพ์ความต้องการแบบธรรมชาติ แล้ว agent หา request form ที่ถูกให้ ตัวที่สาม eSignature Agent for Adobe Acrobat Sign จัดการ flow ของการ sign ตั้งแต่ส่ง follow up log ไปจนถึง activate contract ข่าวที่ซ่อนใต้ 3 agent คือ MCP preview Agiloft เปิดให้ Claude และ external agent อื่นเข้ามา invoke action ใน CLM ผ่าน MCP server โดย respect permission เดิม นี่คือ pattern ที่ enterprise software vendor เริ่มทำแทบทุกราย เปิด agent surface ให้ customer เอา agent ของตัวเองมา drive ทำไมสำคัญ execution gap เป็น narrative หลักของ enterprise agent ปี 2026 AI ที่แค่ analyze ขายได้มา 2 ปีแล้วแต่ ROI วัดยาก การย้ายไป execute เป็น direction ที่ทั้งวงการต้องไปเพราะ CFO วัดได้ตรง MCP preview เป็น move ที่สะท้อนว่า vendor ที่ชนะปี 2027 คือคนที่ยอม distribute agent surface ให้ customer เลือก runtime เอง สำหรับคนที่สร้าง vertical agent บน enterprise SaaS ควร expose MCP เป็น default ไม่ใช่ feature premium สำหรับองค์กรที่ใช้ enterprise app ตอนนี้ต้อง audit ว่า vendor expose MCP ไหม การตั้งคำถามใน vendor review ปี 2027 ควรรวม MCP roadmap ถ้าไม่มี คุณกำลังอยู่ใน walled garden ที่ constrain agent strategy ของตัวเอง
