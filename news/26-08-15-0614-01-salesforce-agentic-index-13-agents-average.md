---
date: 2026-08-15
slug: salesforce-agentic-index-13-agents-average
topic: use-case
reading_time_min: 5
sources: 4
image_prompt: |
  Editorial isometric illustration of a modern office floor cut open like a
  dollhouse; on each desk a small glowing robot completes work while three
  giant floating numbers dominate the scene, stacked: "13 AGENTS PER BIZ",
  "734M AWUs", "94% CONSUMERS PREFER AGENTS". Bottom right a Salesforce cloud
  wordmark. Small silhouettes of employees walk past, unfazed. High contrast
  colors, 1:1 aspect, no real human faces, editorial magazine style, thick
  outlines readable at 200px thumbnail.
image: images/26-08-15-0614-01-salesforce-agentic-index-13-agents-average.png
---

# Salesforce เปิด Agentic Enterprise Index รอบ 2 — เฉลี่ย 13 agents ต่อธุรกิจ, agent-driven retail sales โต 4 เท่า, deployment time หายไปครึ่งหนึ่ง

## TL;DR
- Salesforce ปล่อย **Agentic Enterprise Index รอบ 2** เมื่อวันที่ 10 ส.ค. — ธุรกิจบน Agentforce ตอนนี้รัน **เฉลี่ย 13 agents ต่อบริษัท** (จาก 5 ตัวเมื่อ ก.พ. 2025), **deployment time ลด 53%**, agent-driven retail sales โต **4 เท่า**
- **734M Agentic Work Units (AWUs)** ต่อเดือน โต **15% MoM** — และ **94% ของผู้บริโภคเลือก agent** เมื่อได้ตัวเลือก
- Agentforce ARR ตอนนี้อยู่ที่ **~$800M** โต **169% YoY** — เป็น dataset ที่ใหญ่ที่สุดที่ยืนยันว่า agentic layer **ทำเงินได้จริงในสเกล enterprise** ไม่ใช่ demo อีกต่อไป

## เกิดอะไรขึ้น
วันที่ 10 สิงหาคม 2026 Salesforce เผยแพร่ Agentic Enterprise Index edition 2 — index แรกของอุตสาหกรรมที่รวบรวมข้อมูล agent deployment จริงข้ามหลายพันบริษัทบน Agentforce ตั้งแต่ ก.พ. 2025 ถึง เม.ย. 2026 พร้อม survey แยก 4,689 ผู้ตอบใน พ.ค. 2026 ตัวเลขที่โดดเด่นคือ 3 กราฟที่ทุกคนใน enterprise IT จะต้องอ่านซ้ำ

หนึ่ง: **agent per business จาก 5 เป็น 13 ตัวใน 14 เดือน** — compound growth 7% ต่อเดือน ซึ่งเทียบกับ enterprise software rollout ปกติที่ใช้เวลาเป็นปีต่อ module นี่คือ pace ของ SaaS ยุค peak SaaS-per-employee ปี 2018 สอง: **deployment time ลด 53%** จาก edition 1 (ต้น 2025) แสดงว่า tooling รอบ Agent Builder, prompt library, และ integrations พร้อมพอที่ CIO ไม่ต้องรอ 6 เดือนต่อ agent อีกต่อไป สาม: **agent-driven retail sales โต 4 เท่า** — เป็นครั้งแรกที่ agent activity เข้าไปใน P&L line ของ retail brand ไม่ใช่แค่ cost savings

Metric ใหม่ที่ Salesforce บัญญัติเรียกว่า **Agentic Work Unit (AWU)** — งาน 1 ชิ้นที่ agent ทำจบเอง ตอนนี้ Agentforce ทำ **734M AWUs ต่อเดือน** (เม.ย. 2026) เทียบเดือน มี.ค. ที่ 640M นับเป็น **15% MoM growth** — และ average employee interaction กับ agent โต **3 เท่า** ในช่วง 14 เดือน แต่ตัวเลขที่น่าตกใจกว่าคือ **94% ของผู้บริโภคเลือกใช้ agent เมื่อได้ตัวเลือกกับมนุษย์** — พลิกจาก narrative "ลูกค้าไม่ชอบ chatbot" ที่ครอบงำอุตสาหกรรม CX มา 10 ปี

ในไตรมาสเดียวกัน Salesforce แจ้ง investor ว่า **Agentforce ARR แตะ ~$800M โต 169% YoY** — ทำให้ Agentforce กลายเป็น product line ที่โตเร็วที่สุดในประวัติศาสตร์ Salesforce แซง Marketing Cloud, Commerce Cloud, และ Service Cloud AI add-ons

## ทำไมสำคัญ
นี่คือ **dataset industry-wide ตัวแรก** ที่ยืนยันว่า agentic layer ไม่ใช่ hype ปี 2024 อีกต่อไป — เป็น P&L reality Data ทั้งหมดที่ vendor เคยขายมา (Anthropic บอก "Klarna save $60M", Cognition บอก "Devin handle 80% PRs") เป็น cherry-picked case study แต่ 734M AWUs ต่อเดือนข้ามหลายพันบริษัทเป็น scale ที่ statistician ยอมรับได้ CFO ที่เคย push back Agent budget ปีที่แล้วจะเริ่มไม่มีข้ออ้าง

Pattern สำคัญ 2 อย่าง: หนึ่ง — **deployment time ลด 53%** แปลว่า bottleneck ในการ scale agent ย้ายจาก "สร้าง agent" ไปเป็น "governance/observability/permissions" ซึ่งอธิบายว่าทำไม LangSmith, Arize, Weights & Biases, และ MCP gateway vendor ทั้งหมดกำลัง reprice ขึ้นในไตรมาสนี้ สอง — **94% consumer preference** เป็นสัญญาณว่ารุ่นก่อนหน้าของ chatbot (บอทกดปุ่ม, IVR, live chat แบบเก่า) จะถูก retire ในอีก 18-24 เดือน แบรนด์ที่ไม่ทำ transition จะเสีย CSAT ให้คู่แข่งที่ทำ

Signal ต่อจากนี้: Q3-Q4 2026 จะเป็นช่วงที่ **vertical SaaS competitor ทุกเจ้า** (HubSpot, ServiceNow, Workday, Zendesk, Freshworks) ต้องโชว์ agent metric ในลักษณะเดียวกัน ถ้าโชว์ไม่ได้ = investor จะตีความเป็น "ไม่มี agent story" และตัด multiple ลง เหมือนที่เคยเกิดกับ "cloud story" ปี 2015

## มุม AI Agent Platform
**Builders** ที่สร้าง framework/orchestration: ตัวเลข deployment time -53% แปลว่าตลาด kicked จาก "make it possible" ไปเป็น "make it operable" — สิ่งที่ต้องขายคือ observability, permission scoping, cost attribution per agent, และ audit trail ไม่ใช่ prompt template อีกต่อไป ถ้า framework ของคุณยังโชว์ demo ที่เขียน prompt ให้สวย = คุณล้าไป 12 เดือน

**Users / business** ที่ deploy agent: 13 agents ต่อบริษัทเป็น benchmark ที่ board จะเริ่มถามใน Q4 planning ถ้าองค์กรคุณมี < 5 agents = ต้อง justify ว่าทำไมช้ากว่าตลาด และ vertical retail brand ต้องอ่าน 4x sales lift ให้จบก่อนตัดสินใจ Q4 promo strategy เพราะช่วงเทศกาลปลายปีจะเป็น first stress test ของ agent-driven commerce จริง ๆ

**Ecosystem**: Salesforce เพิ่ง set standard สำหรับ "Agentic Enterprise Index" — คาดว่า HubSpot, Microsoft (Copilot Studio), Google (Gemini Enterprise), และ ServiceNow จะออก index ของตัวเองใน 90 วัน คนที่ได้ประโยชน์รอบสอง = analyst firm (Forrester, Gartner) ที่จะรวมทุก index เป็น cross-vendor benchmark และ MCP/A2A gateway vendor ที่ทำ agent metering ข้ามระบบ

## Sources
- [Salesforce Agentic Enterprise Index 2025–2026 (Salesforce News)](https://www.salesforce.com/news/stories/agentic-enterprise-index-insights-2026/)
- [AI Agent Workforces More Than Doubled, Salesforce Finds (Enterprise DNA)](https://enterprisedna.co/resources/news/salesforce-agentic-enterprise-index-agent-deployments-double-2026/)
- [Salesforce's Agentic Enterprise Index: A Paradigm Shift in AI Deployment (Futurum Group)](https://futurumgroup.com/insights/salesforces-agentic-enterprise-index-a-paradigm-shift-in-ai-deployment/)
- [Salesforce Says Agentforce Adoption Is Accelerating (CX Today)](https://www.cxtoday.com/crm/salesforce-says-agentforce-adoption-is-accelerating-but-enterprise-cx-readiness-remains-in-question/)

---

## Audio script
เมื่อวันที่ 10 สิงหาคม Salesforce ปล่อย Agentic Enterprise Index รอบสอง เป็น dataset industry-wide ตัวแรกที่รวมข้อมูล agent deployment จริงจากหลายพันบริษัทบน Agentforce ตั้งแต่กุมภาพันธ์ 2025 ถึงเมษายน 2026 ตัวเลขที่โดดเด่นคือ ธุรกิจตอนนี้รันเฉลี่ย 13 agents ต่อบริษัท จาก 5 ตัวเมื่อต้นปี 2025 และ deployment time หายไปครึ่งหนึ่ง

ตัวเลขที่น่าตกใจกว่าคือ agent-driven retail sales โตสี่เท่า และ 94 เปอร์เซ็นต์ของผู้บริโภคเลือกใช้ agent เมื่อได้ตัวเลือก พลิก narrative ที่ว่าลูกค้าไม่ชอบ chatbot ที่ครอบงำวงการมา 10 ปี ในไตรมาสเดียวกัน Agentforce ARR แตะประมาณ 800 ล้านดอลลาร์ โต 169 เปอร์เซ็นต์ YoY กลายเป็น product line ที่โตเร็วที่สุดในประวัติศาสตร์ Salesforce

ทำไมสำคัญ นี่คือครั้งแรกที่ agentic layer มี data ระดับ statistician ยอมรับ ไม่ใช่ cherry-picked case study อีกแล้ว CFO ที่ push back budget ปีก่อนจะเริ่มไม่มีข้ออ้าง และ bottleneck ในการ scale agent ย้ายจาก สร้าง agent ไปเป็น governance, observability, permission scoping ซึ่งอธิบายว่าทำไม LangSmith, Arize, และ MCP gateway vendor กำลัง reprice ขึ้นในไตรมาสนี้

สำหรับ builder ที่สร้าง agent framework สิ่งที่ต้องขายตอนนี้คือ observability กับ cost attribution per agent ไม่ใช่ prompt template สำหรับ business ที่ deploy agent 13 agents ต่อบริษัทเป็น benchmark ที่ board จะเริ่มถามใน Q4 planning และ vertical retail brand ต้องเอา 4x sales lift มาคิด promo strategy ก่อนช่วงเทศกาลปลายปีครับ
