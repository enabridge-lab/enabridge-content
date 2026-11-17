---
date: 2026-11-18
slug: genpact-onyx-agentic-operations
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a vast operations control tower
  overlooking a city of invoices, workflows and spreadsheets. In the center,
  a glowing hexagonal core labeled "PROCESS INTELLIGENCE" pulses, with
  robotic agents orbiting around it. A large banner reads "GENPACT ONYX" and
  three floating panels show: "AGENTS BUILT", "ACTIONS LOGGED",
  "HUMAN APPROVED". One panel highlights "ACCOUNTS PAYABLE SUITE" as the
  first use case. Clean editorial style, deep teal and warm amber palette,
  high contrast so labels stay readable at 200px thumbnail, 1:1 aspect,
  no real human faces (silhouettes OK).
image: images/26-11-18-0605-02-genpact-onyx-agentic-operations.png
---

# Genpact Onyx — BPO ยักษ์ Ventures 30 ปี เปิด agent platform ที่สร้างจาก process intelligence เป็นแกน

## TL;DR
- Genpact เปิดตัว Onyx เมื่อ 16 พ.ย. — Agentic Operations platform สำหรับสร้าง run และ govern agent ใน enterprise ops บน "Process Intelligence Core" ที่สะสมมา 30 ปี
- First use case คือ Accounts Payable Suite ของตัวเอง — plus รองรับ custom build จาก client และ partner ecosystem หลาย model
- Governance model เป็น "earned autonomy" — ทุก action log + traceable + require human approval จนกว่า agent จะพิสูจน์ตัวเอง ซึ่งเป็น framing ที่ consultant จะเริ่มขายให้ board

## เกิดอะไรขึ้น
วันที่ 12 พฤศจิกายน Genpact จัด Agentic Operations Day ที่นิวยอร์ก unveil ของใหม่ชื่อ Onyx จากนั้นวันที่ 16 ปล่อย GA — Onyx เป็น "Agentic Operations Platform" สำหรับสร้าง run และ govern AI agent ที่ทำ enterprise operations ตั้งแต่ finance, supply chain, HR ไปจนถึง customer service สิ่งที่ Genpact ชูเป็นจุดขายคือ Process Intelligence Core ซึ่งเป็น codified operating knowledge ที่สะสมจากการเป็น BPO ให้ Fortune 500 มาสามทศวรรษ — บริษัทอ้างว่า context layer นี้ทำให้ agent ของ Onyx ไม่ใช่แค่ GPT ที่เรียก API แต่เป็น agent ที่ "รู้" workflow ของ enterprise จริง

use case แรกที่ Genpact เอาขึ้นโต้ตั้งเองคือ Accounts Payable Suite — คิดง่าย ๆ คือ agent ที่รับ invoice, match กับ PO, flag anomaly, แล้วส่งเข้า approval queue โดย human จะเคาะเฉพาะ case ที่ agent uncertain เท่านั้น Onyx ยังเปิดให้ client เลือก model ได้ (Claude, GPT, Gemini หรือ open-source) และผ่าน connector เข้ากับ SAP, Oracle, Workday ที่ลูกค้า Genpact ส่วนใหญ่ใช้อยู่แล้ว ส่วน governance layer นี่คือจุดที่หลาย report เน้น — ทุก action ของ agent ถูก log, traceable กลับไปยัง reasoning chain และ default mode คือ "earned autonomy" ซึ่งแปลว่า agent ต้องผ่าน human approval หลาย ๆ ครั้งก่อนที่จะได้ run อิสระในบาง scope

## ทำไมสำคัญ
นี่คือสัญญาณว่า BPO legacy — Genpact เอง + Accenture + Cognizant — ไม่ยอมให้ pure-play agent startup กินตลาด enterprise automation ของตัวเอง สามสิบปีที่ผ่านมา โมเดลของ Genpact คือรับ process ของลูกค้ามา run ให้ด้วยคนในอินเดีย ตอนนี้ model จะกลายเป็น "run ให้ด้วย agent + supervisor คน" ที่ margin สูงกว่ามาก คำถามคือ Genpact จะกิน margin ตรงกลางนั้น หรือต้องแบ่งให้ model vendor กับ client เอง pattern ของ Onyx ที่ให้ลูกค้าเลือก model ได้ — บวกกับ positioning ว่าตัวเองคือ process layer ไม่ใช่ model layer — เป็นเดิมพันว่า IP ของ Genpact อยู่ที่ workflow knowledge ไม่ใช่ที่ reasoning capability

เทียบกับ Agentforce ของ Salesforce หรือ Joule Studio ของ SAP ที่เราคุยกันเมื่อสองสัปดาห์ก่อน Onyx ต่างตรงที่ไม่ได้ขึ้นกับ CRM หรือ ERP stack ของตัวเอง — Genpact ไม่มี core system ที่ล็อค customer ไว้ จุดที่ยึดคือ consultant kinship กับ CFO กับ COO ของ Fortune 500 สิ่งที่ "earned autonomy" ทำได้คือทำให้ CFO กล้าเซ็น PO ให้ agent ทำงานที่มี compliance audit ต้องผ่าน — ซึ่งเป็น framing ที่ Agentforce ยังไม่เน้นหนัก

## มุม AI Agent Platform
สำหรับ **Builders** — Onyx เป็น signal ว่า vertical agent platform ที่มาจาก BPO ไม่ใช่ software house จะเล่นเกม context กับ governance ไม่ใช่เกม model ใครที่สร้าง platform แล้ว positioning เป็น "better Claude" จะเจอคู่แข่งใหม่ที่ไม่สนใจ benchmark แต่มี enterprise relationship ลึก 30 ปี และ catalog ของ process ที่ transcribe ไว้แล้ว การแข่งใน enterprise จะวัดกันที่ "integration + audit trail" มากขึ้นเรื่อย ๆ ไม่ใช่แค่ capability

สำหรับ **Users / business** — ถ้าองค์กรกำลังชั่งใจระหว่างซื้อ platform จาก frontier lab, จาก SaaS vendor เดิม (Salesforce/SAP) หรือจาก consulting partner (Genpact/Accenture) — Onyx คือ data point ใหม่ ข้อดีของ option BPO คือ onboarding เร็วกว่าเพราะ consultant รู้ process ของคุณอยู่แล้ว ข้อเสียคือ platform lock-in อาจย้ายยากกว่าถ้า BPO เป็นเจ้าของ Process Intelligence layer — ควรถามว่า process knowledge ที่ codify ขึ้นมานั้น portable กลับไปที่ลูกค้าไหม หรือเป็นของ Genpact ตลอดไป

## Sources
- [Genpact launches Onyx platform: Process intelligence is last mile for AI agents — Constellation Research](https://www.constellationr.com/insights/news/genpact-launches-onyx-platform-process-intelligence-last-mile-ai-agents)
- [Genpact Makes Onyx Available to Build and Govern Enterprise AI Agents — Unite.AI](https://www.unite.ai/genpact-makes-onyx-available-to-build-and-govern-enterprise-ai-agents/)
- [Genpact Onyx Helps Run AI Agents for Enterprise Operations — Procurement Magazine](https://procurementmag.com/news/genpact-onyx-helps-run-ai-agents-for-enterprise-operations)
- [Genpact Launches Genpact Onyx (Press Release) — PR Newswire](https://www.prnewswire.com/news-releases/genpact-launches-genpact-onyx-the-agentic-operations-platform-for-building-running-and-governing-ai-agents-in-enterprise-operations-302940973.html)

---

## Audio script
Genpact BPO ยักษ์ใหญ่สามสิบปี เปิดตัว platform ใหม่ชื่อ Onyx เมื่อสองวันก่อน เป็น agentic operations platform สำหรับสร้างและคุม AI agent ที่ทำงาน enterprise operations ตั้งแต่ finance, supply chain, HR ไปจนถึง customer service จุดขายคือ Process Intelligence Core ซึ่งเป็น knowledge เกี่ยวกับ workflow ของ Fortune 500 ที่ Genpact สะสมมาเป็นสามทศวรรษ ทำให้ agent ของ Onyx ไม่ใช่แค่ chatbot เรียก API แต่เป็น agent ที่เข้าใจ process จริง use case แรกที่ Genpact โชว์คือ Accounts Payable Suite — agent รับ invoice, match PO, flag anomaly แล้วส่งให้คน approve เฉพาะ case ที่ไม่แน่ใจ

สิ่งที่น่าจับตาคือ governance model ที่เรียกว่า earned autonomy — agent ต้องผ่าน human approval หลายรอบก่อนจะได้ทำงานอิสระ ซึ่งเป็น framing ที่ CFO กับ compliance team ยอมรับได้ง่ายกว่า pattern ของ agent รุ่นเก่า นี่คือเดิมพันว่า IP ของ Genpact อยู่ที่ process knowledge ไม่ใช่ model และเป็นสัญญาณให้ builders เห็นว่า การแข่งใน enterprise จะวัดกันที่ integration กับ audit trail มากกว่า benchmark สำหรับ organization ที่กำลังเลือก agent platform ข้อดีของ option BPO คือ consultant รู้ process คุณอยู่แล้ว ข้อเสียคือต้องถามให้ชัดว่า process IP ที่ codify ไปเป็นของใคร
