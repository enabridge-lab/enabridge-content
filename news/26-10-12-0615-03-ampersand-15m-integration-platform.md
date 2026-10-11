---
date: 2026-10-06
slug: 26-10-12-0615-03-ampersand-15m-integration-platform
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial hero: an industrial power-strip labeled "AMPERSAND" with six
  thick cables plugging into glowing boxes stamped "SALESFORCE", "NETSUITE",
  "SAP", "WORKDAY", "CRM", "ERP". From the top of the strip a single
  socket is pulsing with light and a tiny robot avatar labeled "AGENT"
  reaches down to plug in. A dollar sign ribbon reads "$15M SERIES A —
  BESSEMER". Isometric vector, electric indigo + warm gold accents on
  deep navy background, 1:1 aspect, no real human faces, bold text
  readable at 200px thumbnail.
image: images/26-10-12-0615-03-ampersand-15m-integration-platform.png
---

# Ampersand ระดม $15M — เดิมพันว่า integration สู่ CRM / ERP คือ moat จริงของยุค agent (ไม่ใช่ model)

## TL;DR
- 6 ต.ค. 2026 **Ampersand** ปิด Series A **$15M** นำโดย **Bessemer Venture Partners** (รวม total funding $20M), ประกาศ GA ของ integration platform ที่ให้ AI-native app อ่าน/เขียน Salesforce, NetSuite, SAP, Workday ได้แบบ per-customer custom fields
- Lauri Moore (Bessemer) เข้า board, ลูกค้าแรกคือ **Square, 11x, Orb**, และบริษัทเปิด **Andi** — AI integration agent ตัวใหม่ ที่ช่วย dev deploy app ของตัวเองในสภาพแวดล้อมของลูกค้า
- Thesis ที่ Bessemer เชื่อ: **"ต่อ system of record ของ enterprise ได้คือ moat จริงของยุคนี้"** — ไม่ใช่ model ไม่ใช่ UI, แต่คือใครเชื่อมเข้า Salesforce / Workday / NetSuite ให้ agent วิ่งได้ไม่พัง schema

## เกิดอะไรขึ้น

6 ต.ค. 2026 Ampersand — startup ที่ก่อตั้งโดย **Ayan Barua** และ **Lauren Long** จากเมืองซานฟรานซิสโก — ประกาศ Series A $15M นำโดย Bessemer Venture Partners. Matrix (ที่นำ seed round $4.7M ปี 2023) ร่วมกับ Flex Capital, Yelp, Tenacity Capital, CTO Fund, Mana Ventures, และ angel อีกกลุ่ม. **Lauri Moore partner ของ Bessemer เข้า Board of Directors** — คนเดียวกันที่ลง Snowflake, DocuSign, และหลาย enterprise SaaS category leader. Total funding ของ Ampersand หลังรอบนี้คือ ~$20M

Product ที่ Ampersand สร้างคือ **integration infrastructure สำหรับ AI-native app** — เลเยอร์กลางที่ให้แอป / agent ของ builder อ่านและเขียน record ใน **Salesforce, NetSuite, SAP, Workday** (และ ERP/CRM อื่น ๆ) โดยจัดการ **custom fields, per-customer schema variations, และ permission scope** ให้. ตัวอย่าง pain ที่ Ampersand ขายทางออก: ถ้าสร้าง AI SDR agent (เช่น 11x) แล้วจะยิง lead เข้า Salesforce ของลูกค้า 100 รายแรก — แต่ละราย Salesforce schema ต่างกัน (custom object, custom field, workflow rules, record-type restriction) — ต้อง spend 2 สัปดาห์ต่อลูกค้าเพื่อ onboard. Ampersand แก้โดย abstract ชั้นนี้ออก ให้ dev เขียน code เดียวต่อครั้ง, platform แปลงให้ตรง schema ของแต่ละลูกค้า

**ลูกค้าที่เปิดเผย**: Square (ส่วนที่ใช้ Ampersand ไม่ชัด แต่น่าจะเป็น Square's merchant-side AI product), **11x** (เป็น AI SDR / BDR agent — ส่งอีเมล, จอง meeting, ยิง lead เข้า CRM) และ **Orb** (usage-based billing platform). ทั้งสามเป็น case ที่ "AI product ต้องเขียนกลับ system of record ของลูกค้า" — ทำให้ Ampersand positioning ชัดในฐานะ **integration layer สำหรับ agentic era**

พร้อมประกาศ funding, Ampersand launch **Andi** — AI integration agent (บริษัทเรียกตัวเองเพิ่งเริ่มได้ไม่ครึ่งปี) ที่ช่วย developer deploy app ของตัวเองในสภาพแวดล้อมของลูกค้าใหม่. Beta อยู่, free tier ยังไม่ประกาศ. จุดที่สะดุดใจคือ **Ampersand ขาย integration platform แต่ก็เพิ่ม agent ของตัวเอง** — ซึ่งอาจจะเป็น "forward-deployed engineer in a box" ที่ปัจจุบัน Ampersand ขายเป็น service ให้ลูกค้าใหญ่ (บริษัทบอกเงินใหม่จะใช้ "expand forward-deployed experts")

ที่น่าสังเกตอีกจุด: Bessemer ลงใน Ampersand ขณะที่คู่แข่งเดิมคือ **Merge** (ที่ระดมมากกว่ามาก, series B $55M ปี 2023), **Finch** (API สำหรับ HRIS/payroll), **Nango** (open-source alternative), และ **Paragon** (Series B $35M). Thesis ของ Bessemer น่าจะเป็น: ยุค agent ทำให้ **write operations สำคัญกว่า read** — เดิม Merge แข็งที่ data sync (read-mostly) แต่ agent ต้องการ **write + custom field support + per-customer schema** ซึ่งเป็น gap ที่ Ampersand focus

## ทำไมสำคัญ

**"Integration คือ moat" คือ thesis ที่เราได้ยินมาตั้งแต่ Zapier ปี 2015 — แต่ยุค agent มันกลับมาแรงอีกครั้ง.** ประเด็นคือ: builder ที่สร้าง agent ขายเข้า enterprise เจอ "last-mile problem" ซ้ำ ๆ — เอเจนต์เก่งแค่ไหนก็ไม่มีประโยชน์ถ้าเขียนกลับ CRM ของลูกค้าแต่ละรายไม่ได้. OpenAI, Anthropic, Google แก้ด้วย MCP; แต่ MCP เป็น protocol layer, ยังต้องมี **implementation สำหรับทุก Salesforce/NetSuite/SAP schema** ซึ่งเป็น N-by-M problem. Ampersand กินตรงจุดนี้ — ขาย infrastructure ที่ compress N-by-M ให้เป็น 1-to-N

**Thesis ของ Bessemer สะท้อน shift ของ unit of value: จาก model ไป distribution + integration.** ปี 2024 VC ลง foundation model lab ($10M-$1B+). ปี 2025 ลง horizontal agent framework (LangChain, CrewAI). ปี 2026 ลง **integration layer + vertical runtime** — Ampersand, Stuut (O2C agent), Harvey (legal), Hippocratic (healthcare). รูปแบบชัด: **vertical knowledge + integration depth > horizontal reasoning engine**. $15M Series A ที่ Bessemer นำ ไม่ใหญ่ตาม hype cycle แต่ใหญ่พอสำหรับ 2 ปี runway + 20-30 hires + GA launch — สูตร "capital-efficient enterprise SaaS" ที่ Bessemer ชำนาญ

**11x เป็นลูกค้าของ Ampersand คือ validation ที่น่าสนใจ.** 11x เป็น AI SDR agent ที่เคย hype แรงปี 2024, แต่ถูกวิจารณ์หนักเรื่อง quality กลางปี 2025 (lead fake, email spam-like, deliverability แย่). ที่ 11x ยังอยู่และยัง scale ได้ส่วนหนึ่งเพราะต่อ Salesforce / HubSpot ของลูกค้าได้ลึก — ซึ่งถ้าใช้ Ampersand แสดงว่า 11x เลือก buy-vs-build ให้ Ampersand ดูแล layer นี้. สำหรับ builder ไทยที่สร้าง AI SDR / sales agent — บทเรียนคือ **อย่าสร้าง integration เอง, ซื้อ**

## มุม AI Agent Platform

**Builders:** ถ้าสร้าง AI app ที่ต้องเขียน data กลับ CRM / ERP / HRIS / payroll ของลูกค้า, Ampersand (หรือ Merge, Nango, Paragon) ควรอยู่ใน buy-vs-build decision แต่แรก. การสร้าง integration เองคือ **3-6 เดือนของ dev + 20-30% ของ roadmap ไหลไปที่ non-core work**. ส่วน builder ที่เลือก open-source route (Nango) ได้ control + no vendor lock-in แต่ต้องแลกกับ ops burden; Ampersand ขายโมเดล managed + forward-deployed support ซึ่งคุ้มเมื่อลูกค้าแรก ๆ ยังเล็กและต้องการ speed

**Users / business:** CIO ของ enterprise ที่ซื้อ AI product (เช่น AI SDR, AI customer support, AI finance ops) ควรถาม vendor ว่าใช้ integration platform อะไร — ถ้าตอบไม่ได้หรือตอบว่า "เราสร้างเอง" ให้ระวัง onboarding time 2-4 สัปดาห์ต่อ workflow. ขอดู reference customer ที่ onboard สำเร็จในเวลา 1-2 สัปดาห์. **Ecosystem:** Merge ยังเป็น market leader ด้วย $150M+ total funding; Finch focus HRIS/payroll; Nango ลงลง open-source bet; Paragon focus mid-market SaaS; Ampersand ตั้งเป้า **enterprise + agentic workload** — segment ที่โตเร็วสุด. ถ้า Ampersand เติบโตได้ 3-5x ARR ภายใน 18 เดือน จะกลายเป็น **next-gen Merge** และสะเทือน incumbent integration platform ทั้งหมด (รวม Zapier ที่ยัง pivot จาก consumer อยู่)

## Sources
- [Ampersand Raises $15 Million Series A To Expand Integration Enterprise Infrastructure Connecting AI Agents — Pulse 2.0](https://pulse2.com/ampersand-raises-15-million-series-a-to-expand-integration-enterprise-infrastructure-connecting-ai-agents/)
- [Ampersand raises $15M to connect AI agents with legacy enterprise software — CryptoBriefing](https://cryptobriefing.com/ampersand-raises-15m-ai-integration/)
- [Ampersand raises $15M to connect AI agents with legacy enterprise systems — Dealroom](https://dealroom.co/news/160432-ampersand-raises-15m-to-connect-ai-agents-with-legacy-enterprise-systems/)
- [Ampersand's $15 million Series A — Ampersand Blog](https://www.ampersand.ai/blog/series-a-integration-infrastructure-for-enterprise-agents)
- [Ampersand Raises $15M in Series A Funding — FinSMEs](https://www.finsmes.com/2026/10/ampersand-raises-15m-in-series-a-funding.html)

---

## Audio script
วันจันทร์ที่ 6 ตุลาคม Ampersand ปิด Series A 15 ล้านดอลลาร์ นำโดย Bessemer Venture Partners. ก่อตั้งโดย Ayan Barua และ Lauren Long จาก San Francisco. Total funding หลังรอบนี้ 20 ล้าน. Lauri Moore partner ของ Bessemer เข้า board. ลูกค้าที่เปิดเผยคือ Square, 11x, และ Orb. ผลิตภัณฑ์คือ integration platform ให้ AI app อ่านและเขียน Salesforce, NetSuite, SAP, Workday ของลูกค้าได้โดยจัดการ custom fields และ permission ให้. ความสำคัญคือ: builder ที่สร้าง agent ขายเข้า enterprise เจอ last mile problem ซ้ำ ๆ — เอเจนต์เก่งแค่ไหนก็ไม่มีประโยชน์ถ้าเขียนกลับ CRM ของลูกค้าแต่ละรายไม่ได้. OpenAI Anthropic Google แก้ด้วย MCP แต่ MCP เป็น protocol layer ยังต้องมี implementation สำหรับทุก schema ของ Salesforce หรือ SAP. Ampersand กินตรงจุดนี้ — ขาย infrastructure ที่ compress N-by-M ให้เป็น 1-to-N. Thesis ของ Bessemer สะท้อน shift ของ unit of value: จาก model ไป distribution บวก integration. ปี 2024 VC ลง foundation model lab. ปี 2025 ลง horizontal agent framework. ปี 2026 ลง integration layer บวก vertical runtime. 11x เป็นลูกค้าของ Ampersand คือ validation ที่น่าสนใจ. 11x เป็น AI SDR agent ที่ยังอยู่และยัง scale ได้ส่วนหนึ่งเพราะต่อ Salesforce ของลูกค้าได้ลึก. บทเรียนสำหรับ builder ไทย — อย่าสร้าง integration เอง ซื้อ. CIO ไทยที่ซื้อ AI product ควรถาม vendor ว่าใช้ integration platform อะไร ถ้าตอบไม่ได้หรือตอบว่าสร้างเอง ให้ระวัง onboarding time 2 ถึง 4 สัปดาห์ต่อ workflow. ขอดู reference customer ที่ onboard สำเร็จในเวลา 1 ถึง 2 สัปดาห์
