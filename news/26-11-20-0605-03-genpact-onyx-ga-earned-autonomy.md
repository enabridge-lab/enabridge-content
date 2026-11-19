---
date: 2026-11-16
slug: genpact-onyx-ga-earned-autonomy
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a corporate operations floor with
  AI agent avatars working at paired desks alongside empty chairs; above
  them hovers a transparent governance layer labeled "EARNED AUTONOMY" with
  green check icons. A giant metric board on the wall reads "67% TOUCHLESS
  AP" in huge type, with a smaller banner "ACCOUNTS PAYABLE PILOT". Clean
  editorial style, deep teal and warm amber palette, 1:1 aspect, no real
  human faces (silhouettes OK), high contrast so numbers stay readable
  at 200px.
image: images/26-11-20-0605-03-genpact-onyx-ga-earned-autonomy.png
---

# Genpact เปิด Onyx GA — BPO ยักษ์เดิมพันว่า "earned autonomy" คือ moat ของ enterprise agent

## TL;DR
- Genpact ประกาศ GA ของ Onyx แพลตฟอร์ม agentic operations วันที่ 16 พฤศจิกายน (unveil ที่ New York 12 พ.ย.) — Accounts Payable Suite เป็นผลิตภัณฑ์ภายใน Onyx ตัวแรก
- Early customer report ว่า AP process ไปจาก "ไม่มี automation" เป็น 67% touchless หลัง deploy agent (เป็น vendor-presented claim)
- Platform ใช้ "earned autonomy" model — agent ต้อง earn trust ก่อนที่ human จะอนุมัติให้ทำงานแบบ autonomous และ integrate กับ AWS, ServiceNow, Microsoft, Databricks

## เกิดอะไรขึ้น
Genpact บริษัท BPO ที่มีรายได้ $4.5B ต่อปี กำลังเปลี่ยนตัวเองจาก "ขายคน" เป็น "ขาย agent" และ Onyx คือ product ที่แทนสัญลักษณ์ของ shift นี้ ประกาศ unveil ที่งาน Agentic Operations Day ที่ New York วันที่ 12 พฤศจิกายน และ GA announce ตามมาวันที่ 16 Onyx เป็น platform agentic operations ที่สร้างให้ enterprise ใช้ build run และ govern AI agents ใน workflow ที่ Genpact เคยขายเป็น managed service

Product แรกบน Onyx คือ Accounts Payable Suite — Genpact เอางาน AP ของลูกค้าตัวหนึ่งที่เริ่มจาก 0% automation แล้ว deploy agent บน Onyx รายงานว่าไปถึง 67% touchless processing (ไม่ต้องมีคนแตะ invoice เลย) ตัวเลขนี้เป็น vendor claim ที่ยังไม่มี third party verify แต่ถ้าจริงเป็น ratio ที่สูงกว่า automation benchmark ของ RPA generation เก่าซึ่งปกติอยู่ที่ 20-40% touchless

สิ่งที่ Genpact เรียกว่า differentiator คือ "earned autonomy" — agent ไม่ได้รับสิทธิ์ทำงาน autonomous ทันที ต้องผ่าน approval loop ของ human หลายรอบ จนกว่า pattern ของ decision จะ consistent พอที่จะ "earn" สิทธิ์ยัดเงินได้โดยไม่ต้อง approve ทีละ invoice ทุก action ของ agent audit trail-able และ traceable กลับไปที่ reason ที่ decide Onyx รองรับ model หลายตัว (ไม่ผูก Claude หรือ GPT) และ integrate กับ AWS, ServiceNow, Microsoft, Databricks ซึ่ง Genpact บอกว่าเป็น stack ที่ลูกค้า Fortune 500 มีอยู่แล้ว

## ทำไมสำคัญ
Narrative ที่น่าสังเกตคือ BPO company ไม่ได้ compete กับ agent platform — พวกเขา package และ wrap agent ขายเป็น managed service ที่มี SLA ประวัติศาสตร์ยุค RPA (UiPath, Blue Prism) BPO เป็น channel distribution ที่ใหญ่ที่สุด แต่ยุค LLM agent BPO ตัดสินใจ build platform ตัวเอง แทนที่จะเป็น channel ของ Agentforce หรือ Microsoft Copilot

67% touchless ของ AP เป็นตัวเลขที่น่าเชื่อถือกว่าของ RPA รุ่นก่อน เพราะ AP เต็มไปด้วย edge case ที่ rule-based ทำไม่ได้ — supplier ที่เปลี่ยน format invoice, tax จาก multi-jurisdiction, PO ที่ไม่ match line-item ตัวเลขนี้ถ้าจริงแปลว่า agent ทำได้ดีกว่า RPA แบบที่ measurable ซึ่งจะเปลี่ยน sales cycle ของ enterprise automation ครั้งใหญ่

"Earned autonomy" คือคำที่จะเริ่มเห็นเยอะในอีกหกเดือนข้างหน้า — เป็นคำตอบของ enterprise ต่อคำถาม "เรา trust agent ได้ขนาดไหน" ปีที่ผ่านมามี vendor หลายรายขายแบบ full autonomous (เช่น Sierra ขาย voice agent ที่ handle call จบ end-to-end) แต่ enterprise buyer ไม่ comfortable Genpact pitch ว่า progressive autonomy ที่ human-in-the-loop เริ่มต้น แล้วค่อย lift governance เมื่อ confidence พอ คือ sell ที่ CFO ยอมเซ็น ปีหน้าเราน่าจะเห็น Salesforce, SAP, ServiceNow ทุกคนใช้ framing คล้ายกันนี้

## มุม AI Agent Platform
Builders — ถ้าคุณกำลัง build agent ให้ enterprise ลองออกแบบ autonomy ladder ชัดเจน — agent เริ่มที่ "suggest" ไปที่ "execute with approval" ไปที่ "execute within policy" ไปที่ "full autonomous" แต่ละ level มี metric ว่า earn อย่างไร การวางแบบนี้ลด friction ของ procurement และทำให้ CFO มี sign-off path ที่ CFO ของ Enabridge หรือลูกค้าไทยเข้าใจได้

Users/business — bank, insurance, retailer ไทยที่ outsource AP, order processing, claims ให้ BPO ต่างชาติอยู่แล้ว Onyx อาจเข้ามาถึงคุณผ่าน account manager ของ Genpact ภายในสองไตรมาส พร้อม pitch "touchless ratio" ที่สูงกว่า RPA ให้ถาม 3 คำถาม — (1) 67% touchless base เท่าไหร่ volume invoice และกี่ supplier (2) agent เรียน pattern ของ invoice ที่เป็น proprietary ของคุณที่ถูก shared กับ Genpact customer อื่นไหม (3) ถ้าเปลี่ยน BPO vendor data ของ agent portable หรือไม่

Ecosystem — ยุคของ RPA vendor (UiPath, Automation Anywhere) ที่ขาย platform แยกจาก BPO service กำลังโดนบีบ — Genpact ไม่ใช่รายแรก ก่อนหน้านี้ Accenture, Cognizant, TCS, Infosys ต่างมี agent platform ของตัวเองแล้ว BPO คือ channel สำคัญของ AI agent ปีนี้ ไม่ใช่ SaaS self-serve หรือ developer DIY เหมือนที่ framework vendor pitch

## Sources
- [Genpact launches Onyx platform: Process intelligence is last mile for AI agents (Constellation Research)](https://www.constellationr.com/insights/news/genpact-launches-onyx-platform-process-intelligence-last-mile-ai-agents)
- [Genpact Makes Onyx Available to Build and Govern Enterprise AI Agents (Unite.AI)](https://www.unite.ai/genpact-makes-onyx-available-to-build-and-govern-enterprise-ai-agents/)
- [Genpact Onyx Helps Run AI Agents for Enterprise Operations (Procurement Magazine)](https://procurementmag.com/news/genpact-onyx-helps-run-ai-agents-for-enterprise-operations)
- [Genpact launches Genpact Onyx the agentic operations platform (StockTitan)](https://www.stocktitan.net/news/G/genpact-launches-genpact-onyx-the-agentic-operations-platform-for-9499a0uamlif.html)

---

## Audio script
Genpact บริษัท BPO ขนาดใหญ่ที่มีรายได้สี่พันห้าร้อยล้านเหรียญต่อปี ประกาศ GA แพลตฟอร์ม Onyx เมื่อวันที่ 16 พฤศจิกายน Onyx เป็น platform agentic operations สำหรับ enterprise ใช้สร้างและ govern AI agent สินค้าตัวแรกคือ Accounts Payable Suite ที่ Genpact อ้างว่าช่วยลูกค้ารายหนึ่งไปจากไม่มี automation เลยเป็น 67% touchless

สิ่งที่ Genpact pitch ว่าเป็น differentiator คือ "earned autonomy" — agent ต้อง earn trust ของ human ผ่าน approval loop หลายรอบก่อนที่จะได้สิทธิ์ทำงาน autonomous เอง ทุก action audit ได้และ trace กลับไปที่ reason ของ decision ได้ Platform รองรับ model หลายตัวและ integrate กับ AWS ServiceNow Microsoft Databricks

narrative ที่น่าสังเกต BPO ยักษ์ไม่ได้เป็น channel ของ Agentforce หรือ Copilot แต่เลือก build platform ของตัวเอง — เพราะพวกเขาคุม workflow และ data ของลูกค้า Fortune 500 อยู่แล้ว สำหรับ bank insurance retailer ไทยที่ outsource งานหลังบ้านให้ BPO ต่างชาติอยู่ภายในสองไตรมาส account manager ของ Genpact น่าจะ pitch Onyx ให้ ควรถามก่อนว่า data portable ไหม ถ้าเปลี่ยน vendor ครับ
