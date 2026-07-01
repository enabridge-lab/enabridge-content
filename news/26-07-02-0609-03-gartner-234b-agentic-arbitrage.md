---
date: 2026-07-01
slug: gartner-234b-agentic-arbitrage
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration of a huge dollar-sign iceberg floating in dark
  ocean. The visible tip labeled "$234B AT RISK · 20% OF SaaS BY 2030"
  in bold amber text. Below the waterline, glowing agent silhouettes
  swim silently between three glowing SaaS-app icons (a CRM window, an
  ERP grid, a helpdesk chat bubble), extracting outcomes and bypassing
  each app's UI. On the surface, a Gartner-branded pennant floats. In
  the sky, ticker-tape header reads "AGENTIC ARBITRAGE" in big
  serif letters. Deep navy + amber palette, cinematic editorial style,
  ultra-sharp text rendering for 200px thumbnail readability, 1:1
  aspect ratio, no real human faces.
image: images/26-07-02-0609-03-gartner-234b-agentic-arbitrage.png
---

# Gartner: $234B ของ enterprise SaaS spend เสี่ยงถูก agent "arbitrage" ภายใน 2030 — SaaS UX กำลังจะกลายเป็น "invisible layer"

## TL;DR
- 1 ก.ค. — Gartner ปล่อยรายงานว่า **$234 พันล้าน** ของ enterprise application software spending เสี่ยง disruption จาก agentic AI ระหว่างนี้ถึง 2030 = **~20% ของ SaaS spend รวม**
- Concept ใหม่ที่ Gartner บัญญัติ: **"agentic arbitrage"** — agent ทำงานข้าม system หลาย ๆ ตัว ทำให้ user ไม่ต้อง log เข้า UX ของ SaaS แต่ละตัว. George Brocklehurst (MVP Gartner): "agentic systems make the software invisible — breaks the link between user growth and revenue growth"
- แนวทางรอด: (1) embed agentic feature เข้า product, (2) เก็บ customer-specific knowledge ที่ agent อื่นเข้าไม่ถึง, (3) ย้ายไป **outcome-based pricing**. Salesforce Agentforce Help Agent ที่ปล่อยวันเดียวกันคือ playbook ตัวอย่าง

## เกิดอะไรขึ้น

1 กรกฎาคม 2026 — Gartner ปล่อย press release ที่ **"Gartner Says $234 Billion in Enterprise Application Software Spend Is at Risk from Agentic Artificial Intelligence"** และคำที่ Gartner ใช้ทั้งรายงานคือคำใหม่ที่ยังไม่มีใครเคยได้ยิน: **"agentic arbitrage"**. Concept ง่าย ๆ — เมื่อ agent สามารถ complete task ที่ครอบคลุมหลาย SaaS system ในการ orchestrate ครั้งเดียว, user ไม่ต้อง log in เข้า UI ของ SaaS แต่ละตัว. เจ้าของ SaaS เดิมที่ pricing แบบ per-seat/per-active-user ก็จะเห็น seat ลดลงเรื่อย ๆ ทั้งที่ workload ยังอยู่

George Brocklehurst, Managing Vice President ที่ Gartner บอกในรายงานว่า: **"Agentic AI changes the economics of software. Agentic systems deliver outcomes directly, bypassing traditional user experience heavy applications and making the software invisible. This breaks the link between user growth and revenue growth for many enterprise software vendors."** คือ Gartner บอกตรงว่า SaaS unit economics แบบเดิม (revenue = seat × price/seat) พังลงแล้ว

ตัวเลข $234B = ~20% ของ SaaS spend รวมภายใน 2030 มาจากประเมิน 3 กลุ่ม vendor ที่เสี่ยงสุด: (1) **Front-office SaaS** ที่ interaction เยอะแต่ workflow ซ้ำ ๆ (help desk, ticketing, CRM data entry), (2) **Middle-office productivity** (project management, HR admin, form filling), (3) **UX-heavy analytics** ที่ user ต้อง navigate หลาย screen. Gartner ไม่ระบุชื่อ vendor แต่ analyst และ IT Voice ที่ cover report ชี้ชัดไปที่ Zendesk, Freshworks, Asana, monday.com, Tableau — vendor ที่ business model ต้องพึ่ง active user จำนวนมาก

Timing ของ press release น่าสังเกต — **วันเดียวกัน** Salesforce เปิดตัว Agentforce Help Agent + pay-per-resolution ($2 flat per autonomous resolution). ทั้ง Business Standard India + TechEdgeAI ที่ cover เรื่องนี้ต่างสังเกตว่า Gartner + Salesforce release ตกลงพร้อมกันเหมือน **choreograph** — SF น่าจะได้ preview report และตอบด้วย product move ในทันที เพื่อ frame ตัวเองว่าเป็น "winner ของ shift" ไม่ใช่ "victim"

Gartner แนะนำ SaaS vendor 3 หนทางรอด: (1) **embed agent เข้า product ตัวเอง** — ทำให้ workflow ที่ agent อื่นข้าม product ไม่ได้ (ตัวอย่าง Notion AI, Airtable AI), (2) **hold on to customer-specific knowledge** — data ที่เฉพาะลูกค้ารายนั้น ๆ ที่ agent จากภายนอกเข้ามาใช้ไม่ได้ (Salesforce Data Cloud, ServiceNow Now Assist), (3) **shift ไป outcome-based pricing** ก่อนที่ลูกค้าจะ dictate เอง

## ทำไมสำคัญ

**Gartner ไม่เคยใช้คำแรง ๆ แบบนี้ในรายงานปกติ**. เทียบ report Gartner ปี 2025 ที่บอก 40% ของ agentic AI project จะ cancel ภายในปลาย 2027 — ก็เป็น bearish signal. แต่ report วันนี้เป็นครั้งแรกที่ Gartner **ระบุตัวเลขความเสี่ยงทางการเงินโดยตรง** ต่อ SaaS incumbent — บอกกลาย ๆ ว่า board ของ Salesforce / ServiceNow / Adobe / Workday ควรเริ่ม stress test business model ทันที. Analyst ทั่วไปจะเก็บ report แบบนี้ไว้ใช้ตอนคุยกับ CEO SaaS ในไตรมาสหน้า

Concept **agentic arbitrage** จะ stick เพราะมันครอบทั้ง 2 มุม: (1) มุม user — agent ประหยัดเวลาโดยการ orchestrate ข้าม system, (2) มุม vendor — value ที่ SaaS สร้างถูก "arbitrage" หายไปเพราะ user ไม่จ่ายเงิน. ต่างจาก "AI eating software" ที่ Marc Andreessen เขียนใน 2011 (software eating world) — คำ arbitrage สร้างภาพชัดขึ้น: **agent เป็น middleware ที่กินส่วน margin ของทั้ง producer + consumer relationship**

จับคู่กับ **Bland AI Series C $50M ที่ปิดเมื่อ 16 มิ.ย.** ที่ platform Bland handle 175 ล้าน call/ปี และ **ปฏิเสธจะ integrate OpenAI/Anthropic model** — เพราะ Bland รู้ว่าถ้าใช้ frontier model ก็จะเป็น "middleman ที่ arbitrage ตัวเอง" ทันที. Vertical agent platform ที่ประสบความสำเร็จรอบใหม่จะ own model + own workflow + own customer data — เพื่อไม่ให้เจ้าของอื่นมา arbitrage ตัวเอง. คือคำ arbitrage สรุปยุคใหม่ทั้งหมด

Signal ที่ต้องระวัง — **20% ในอีก 4 ปี = fast ผิดปกติ**. Gartner ปกติ conservative — ประเมินตัวเลขแบบนี้แปลว่า data ที่ได้จาก client interview ในช่วง Q1-Q2 2026 sees pattern ชัดมาก. ที่ต้องดูต่อคือ Q3-Q4 2026 revenue reports ของ **Zendesk (private), Freshworks (FRSH), monday.com (MNDY), HubSpot (HUBS)** — ถ้า NRR (net revenue retention) ลดจากระดับ 110-120% เดิม มาต่ำกว่า 100% ในไตรมาสถัด ๆ คือ signal ว่า arbitrage เริ่มเกิดจริง

## มุม AI Agent Platform

**Builders** — คุณคือคนที่ Gartner บอกว่ากำลัง arbitrage SaaS incumbent. คำถามสำคัญที่ต้องตอบไม่ใช่ "เราจะ integrate SaaS ไหน" แต่ **"เราจะ own layer ไหน"**. LangChain / LangGraph, Cognigy, Dust, Sierra ที่ทำ orchestration ระหว่าง SaaS หลาย ๆ ตัว = ผู้ arbitrage โดยตรง — profit margin ของคุณเท่ากับ **ราคาที่ SaaS incumbent ลดลง minus ค่า agent inference**. เพื่อ moat ในระยะยาว: (1) build customer-specific knowledge layer (RAG + fine-tune) ที่ agent อื่นจำลองไม่ได้, (2) ผูก outcome contract แบบ Bland (per-call) ไม่ใช่ subscription แบบเดิม, (3) เปิด API ให้ agent อื่นเข้ามา call — เพราะ arbitrage จะแบ่งชั้น (คุณจะ arbitrage คนอื่น คนอื่นจะ arbitrage คุณ)

**Users / business** — ถ้าเป็น CIO / CFO ของ enterprise ที่ subscribe SaaS หลายเจ้า: **เริ่ม audit ทันที** ว่า SaaS ไหนใช้ actively vs SaaS ไหนถือไว้ "just in case" (Zendesk, monday.com, Asana ปกติมี % ใช้จริงต่ำกว่าที่ซื้อ). ก่อนต่อ contract ต้อง negotiate 2 ประเด็นใหม่: (1) **agent access clause** — SaaS ต้องมี API/MCP endpoint ที่ agent ตัวอื่นเข้าถึงได้ ไม่ปิด lock-in, (2) **outcome-based tier** — ถ้า usage seat ลดลง ยินยอมให้ downgrade pricing tier ตาม active usage จริง. ที่หลายทีมยังไม่คิดคือ **agentic arbitrage เกิดในทีมเอง** — ทีม product กำลัง build internal agent ที่แทน SaaS 2-3 ตัว, ควร inventory ให้ครบก่อนต่อ license รอบใหม่

**Ecosystem** — ผู้ที่ได้ประโยชน์แน่ ๆ คือ **iPaaS + integration platform** ที่ pivot เร็ว: MuleSoft (SF), Boomi, Workato, Zapier, OpenBridge, n8n. Layer นี้จะกลายเป็น "runtime ของ agent arbitrage" — คนที่ own API catalog + auth layer + observability จะเก็บค่าผ่าน per-execution ที่ agent เดินผ่าน. คำถามที่ vendor ในกลุ่มนี้ต้องคิด: model ตัวไหน default? MCP server registry ของตัวเองเปิดกี่ตัว? Pricing เป็น per-execution vs per-connection? — คำตอบจะ define ว่าใครกินส่วน $234B ที่หายไปจาก SaaS incumbent

## Sources
- [Gartner Says $234 Billion in Enterprise Application Software Spend Is at Risk from Agentic Artificial Intelligence — Gartner Newsroom](https://www.gartner.com/en/newsroom/press-releases/2026-07-01-gartner-says-us-dollars-234-billion-in-enterprise-application-software-spend-is-at-risk-from-agentic-artificial-intelligence)
- [Agentic AI to Reshape Enterprise SaaS: Gartner — TechEdgeAI](https://techedgeai.com/gartner-says-234-billion-in-enterprise-application-software-spend-is-at-risk-from-agentic-ai/)
- [Agentic AI may put $234 bn of SaaS spending at risk by 2030: Gartner — Business Standard](https://www.business-standard.com/technology/artificial-intelligence/gartner-agentic-ai-forecast-agentic-ai-enterprise-saas-spending-gartner-software-risk-126070100820_1.html)
- [Gartner Says $234 Billion in Enterprise Application Software Spend Is at Risk from Agentic AI — IT Voice](https://www.itvoice.in/gartner-says-234-billion-in-enterprise-application-software-spend-is-at-risk-from-agentic-ai)
- [Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027 — Gartner Newsroom](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)

---

## Audio script

หนึ่งกรกฎาคม Gartner ปล่อยรายงานที่ชี้ตรง ๆ ว่าสองแสนสามหมื่นสี่พันล้านดอลลาร์ของ enterprise SaaS spend เสี่ยง disruption จาก agentic AI ภายในสองพันสามสิบ. เท่ากับยี่สิบเปอร์เซ็นต์ของ SaaS spend รวมทั้งโลก. คำใหม่ที่ Gartner บัญญัติในรายงานนี้คือ agentic arbitrage — agent ทำงานข้าม SaaS หลายตัว user ไม่ต้อง log in UI แต่ละตัว seat ลดลง แต่ workload ยังอยู่.

George Brocklehurst จาก Gartner บอกตรง ๆ ว่า agentic system make software invisible แล้ว break link ระหว่าง user growth กับ revenue growth. คือ SaaS unit economics แบบเดิมพังลงแล้ว. Gartner ไม่ระบุชื่อ vendor แต่ analyst ชี้ไป Zendesk, Freshworks, Asana, monday.com — vendor ที่ต้องพึ่ง active user จำนวนมาก.

Timing ที่น่าสังเกต — Salesforce ประกาศ Agentforce Help Agent pay-per-resolution วันเดียวกัน. เป็น choreograph ที่ SF ตอบด้วย product move เพื่อ frame ตัวเองเป็นวินเนอร์ของ shift. Gartner แนะนำ SaaS vendor สามหนทางรอด embed agent เข้า product, hold customer-specific knowledge, shift ไป outcome-based pricing.

สำหรับ agent builder — คุณคือคนที่ Gartner บอกว่ากำลัง arbitrage SaaS incumbent. คำถามสำคัญไม่ใช่จะ integrate SaaS ไหน แต่จะ own layer ไหน. Moat ระยะยาวมาจาก customer-specific knowledge, outcome contract, และ open API ให้ agent อื่นเข้ามาใช้. สำหรับ CIO ในไทย เริ่ม audit ทันทีว่า SaaS ไหนใช้จริง vs ถือ just in case. ก่อนต่อ contract negotiate agent access clause และ outcome-based tier. ที่หลายทีมยังไม่คิด — arbitrage เกิดใน internal team เอง ทีม product กำลัง build agent ที่แทน SaaS สองสามตัวอยู่แล้ว inventory ให้ครบก่อนต่อ license.
