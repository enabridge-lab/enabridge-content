---
date: 2026-10-06
slug: 26-10-07-0616-03-vida-outcome-based-billing
topic: agentic-ai
reading_time_min: 3
sources: 4
image_prompt: |
  Editorial hero: a sleek cash register redesigned as an agent dashboard,
  front panel labeled "PAID PER OUTCOME". Three LED counters stacked —
  "LEAD QUALIFIED", "WARM TRANSFER COMPLETED", "WIN-BACK CLOSED". A dim
  grey ribbon in the background crossed out with a red line reads
  "PER TOKEN". A small corner stamp: "VIDA AGENT OS". Isometric vector
  style, muted teal + warm cream + bright coral accents, 1:1 aspect,
  no real human faces.
image: images/26-10-07-0616-03-vida-outcome-based-billing.png
---

# Vida เปิด outcome-based billing — ลูกค้าจ่ายเฉพาะเมื่อ agent "ปิด lead / โอนสาย / ชนะกลับลูกค้า" สำเร็จ

## TL;DR
- Vida ประกาศ 5 ต.ค. 2026 — pricing model ใหม่ของ Vida Agent OS: จ่ายต่อ **outcome** (lead qualified, warm transfer completed, onboarding done, win-back closed) แทนการจ่าย per-token / per-minute / per-seat
- เป็น signal ชัดว่า **ตลาด enterprise agent กำลังย้ายจาก "sell compute" → "sell result"** — Sierra เริ่มก่อน, Vida ตาม, Salesforce Agentforce + ServiceNow เริ่มทดลองแบบนี้แล้ว
- Model นี้ย้าย **financial risk จาก buyer ไป vendor** → vendor ที่ไม่กล้า guarantee outcome จะหลุด; vendor ที่ instrument outcome แม่น ๆ จะชนะ budget RFP

## เกิดอะไรขึ้น

Vida — บริษัทที่ pitch ตัวเองว่าเป็น **"AI Agent Operating System"** สำหรับ voice / messaging / email / web — ประกาศ 5 ต.ค. ว่าจะเริ่ม bill ลูกค้าแบบ outcome-based สำหรับ 4 use case หลัก: **lead qualification, warm transfer, onboarding, และ win-back campaigns**. ภาษาที่ Vida ใช้ตรง ๆ: "charge only when the agent delivers a measurable business result"

Mechanic: agent connect เข้า CRM / dialer / ticketing / billing ของลูกค้าแล้วรับงานเข้ามา. เมื่อ agent ทำสำเร็จ (lead ผ่าน qualification criteria ที่ตั้งไว้, call ถูก transfer ไปที่ sales rep จริง, onboarding ticket ปิดโดย user ไม่ได้ร้อง escalate) → นับเป็น 1 outcome → bill 1 รายการ. ถ้า agent คุย 500 นาทีแล้ว lead ไม่ qualified / transfer ไม่สำเร็จ → **ลูกค้าไม่จ่าย**. Vida แบก compute cost เอง

Vida ไม่ใช่คนแรก — **Sierra** (startup ของ Bret Taylor อดีต co-CEO Salesforce) pioneer การขาย per-resolution ให้ customer-service agent มาตั้งแต่ปี 2024 และปิดดีลใหญ่ ๆ กับ Sonos, SiriusXM. **Salesforce Agentforce** เริ่ม pilot "pay per conversation resolved" กับ customer บางเจ้าใน Q3; **ServiceNow** กำลังทดลองแบบนี้กับ ITSM agent. แต่ Vida เป็นเจ้าแรกที่ **ประกาศเป็น default pricing** สำหรับ voice/messaging agent ทั้ง stack

## ทำไมสำคัญ

Pricing model เป็นหนึ่งใน **primitive สำคัญที่สุดของ AI Agent Platform** ที่ยังไม่ settle. ปี 2025 ทุกคนขาย per-token (API) หรือ per-seat (copilot) — model ที่ยืมมาจาก SaaS era. ปัญหาคือ customer จ่าย input แต่ไม่รู้ว่าได้ output อะไร: ChatGPT Enterprise seat $30/คน/เดือน ถ้าพนักงานใช้แค่สรุปอีเมล 3 ครั้งต่อสัปดาห์ = CFO เห็น ROI เป็น 0

Outcome-based ย้าย **unit of value** จาก compute → business result. ตรงจุดที่ CFO วัดได้: 1 lead qualified = $X, 1 ticket closed = $Y, 1 win-back = $Z. Enterprise procurement team เริ่มเปิด RFP ที่บังคับให้ vendor **guarantee outcome price** — vendor ที่ไม่กล้าจะหลุดจาก shortlist. Pattern เดียวกับที่ cloud infra move จาก server rent → pay-per-request (Lambda) → pay-per-outcome (Vercel Edge pricing); agent ย้ายทางเดียวกันแค่ช้ากว่า 10 ปี

เรื่องที่ยากคือ **vendor ต้อง instrument outcome ได้แม่น**. Vida ต้องรู้จริง ๆ ว่า lead qualified นี้เป็นเพราะ agent (จ่าย) หรือเป็นเพราะ marketing campaign (ไม่จ่าย); ต้องรู้ว่า warm transfer เกิดเพราะ agent clean prospect ให้ sales rep (จ่าย) หรือลูกค้าโทรกลับเอง (ไม่จ่าย). นี่คือเหตุผลที่ outcome-based model จะไม่ scale ให้ทุก vendor — มีแค่ **vertical-focused agent** (customer service, sales dev, collection) ที่ attribution clear พอ

## มุม AI Agent Platform

**Builders:** คนทำ horizontal agent framework (LangChain, CrewAI, AutoGen) ไม่ได้ประโยชน์โดยตรง — pricing yังเป็น per-token ของ underlying model. แต่ **vertical agent builder** ที่ pitch SMB/mid-market ต้องเริ่มคิด outcome pricing ตั้งแต่ MVP — เพราะพวกเขาแข่งกับ Sierra, Vida, Decagon, Lindy ที่ขายแบบนี้แล้ว. **Users / business:** CFO ที่ยัง approve agent pilot แบบ per-seat ควรขอ vendor เสนอ outcome-based option; ถ้า vendor ปฏิเสธ = vendor ไม่เชื่อว่า agent ของตัวเองทำงานได้จริง. BPO / contact center ของไทยที่กำลัง pilot AI voice bot ของผู้ให้บริการ local มีไพ่ใหม่ — ขอ vendor แสดง outcome metric ก่อนเซ็น. **Ecosystem:** cloud vendor (AWS Bedrock, Azure OpenAI, GCP Vertex) จะต้องสร้าง **attribution layer** ให้ customer วัด outcome ได้ — ไม่ใช่แค่ monitor token spent; รอบของ ARR metric ปี 2027 ใน SaaS vendor จะเริ่มเห็น split "outcome ARR" vs "subscription ARR"

## Sources
- [AI Agents News Brief: Security, Governance, and Development Updates - AI Agents Directory](https://aiagentsdirectory.com/news/ai-agents-daily-brief-security-concerns-new-tools-and-market-moves)
- [Vida AI agents for performance marketing - Vida.io](https://vida.io/solutions/performance-marketing)
- [From Tokens to Outcomes: The Shift to Value-Based AI Agent Billing Models - IT Convergence](https://www.itconvergence.com/blog/from-tokens-to-outcomes-the-shift-to-value-based-ai-agent-billing-models/)
- [Outcome-Based Billing for AI Agents and GenAI Platforms - OneBill](https://www.onebillsoftware.com/outcome-based-consumption-pricing-ai-agents/)

---

## Audio script
Vida ประกาศ 5 ตุลาคม pricing model ใหม่ของ Vida Agent OS. จ่ายต่อ outcome ไม่ใช่ per token ไม่ใช่ per seat. 4 use case หลัก lead qualification, warm transfer, onboarding, win-back campaign. mechanic คือ agent connect เข้า CRM dialer ticketing ของลูกค้า เมื่อ agent ทำสำเร็จนับเป็นหนึ่ง outcome bill หนึ่งรายการ. ถ้า agent คุยห้าร้อยนาทีแล้ว lead ไม่ qualified ลูกค้าไม่จ่าย Vida แบก compute cost เอง. Vida ไม่ใช่คนแรก Sierra ของ Bret Taylor pioneer การขาย per resolution มาตั้งแต่ปี 2024 ปิดดีลใหญ่กับ Sonos SiriusXM. Salesforce Agentforce เริ่ม pilot แบบนี้ ServiceNow กำลังทดลอง. แต่ Vida เป็นเจ้าแรกที่ประกาศ outcome based เป็น default pricing สำหรับ voice และ messaging agent ทั้ง stack. ทำไมสำคัญ. pricing model เป็น primitive สำคัญที่สุดของ AI Agent Platform ที่ยังไม่ settle. ปี 2025 ทุกคนขาย per token หรือ per seat ย้ายมาจาก SaaS era. ปัญหาคือ customer จ่าย input แต่ไม่รู้ว่าได้ output อะไร. outcome based ย้าย unit of value จาก compute เป็น business result ตรงจุดที่ CFO วัดได้. enterprise procurement จะเปิด RFP ที่บังคับให้ vendor guarantee outcome price vendor ที่ไม่กล้าจะหลุดจาก shortlist. BPO contact center ไทยที่กำลัง pilot AI voice bot มีไพ่ใหม่ ขอ vendor แสดง outcome metric ก่อนเซ็น

