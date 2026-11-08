---
date: 2026-11-05
slug: firmly-15m-ask-agent-commerce
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a bright e-commerce store interior
  with a glowing chatbox hovering above the checkout counter labeled
  "ASK AGENT". Three stacked stat bars read "+18% CONVERSION",
  "+23% AOV", and "1 LINE OF JAVASCRIPT". Outside the window, bank
  logos "JPM" and "MASTERCARD" ride in on a conveyor belt tagged
  "$15M SERIES A". A tiny agent cube is swiping a credit card at the
  counter while a merchant silhouette watches. Deep teal and warm coral
  palette, 1:1 aspect, no real human faces (silhouettes OK), high contrast
  so numbers stay readable at 200px.
image: images/26-11-09-0607-03-firmly-15m-ask-agent-commerce.png
---

# Firmly ปิด $15M + ปล่อย Ask Agent — JPM กับ Mastercard ลงทุนใน rail ที่ agent ซื้อของแทนลูกค้า

## TL;DR
- 5 พ.ย. Firmly ประกาศ Series A $15M + เปิดตัว Ask Agent product; lead โดย Squarepoint Capital; **J.P. Morgan Payments, Mastercard, Samsung NEXT** ร่วม — total funding ~$20M
- Mastercard เป็น commercial partner ด้วย — ใช้ Firmly สำหรับ merchant catalog + cart ใน Agent Connect ของตัวเอง (ไม่ใช่แค่ financial investor)
- Ask Agent = conversational shopping บน merchant site ของตัวเอง, integrate ด้วย JavaScript 1 บรรทัด
- Firmly อ้าง early results: conversion rate +18%, AOV +23% — ตัวเลข company-reported จาก early deployment
- Network claim: ~11M merchants, ครอบคลุม majority of US online GMV

## เกิดอะไรขึ้น
5 พฤศจิกายน Firmly startup ที่ทำ agentic commerce infrastructure ประกาศปิด Series A $15M พร้อมเปิดตัว product ใหม่ชื่อ **Ask Agent** — Axios Pro รายงาน exclusive ก่อน ส่วน GlobeNewswire ปล่อย press release เต็มภายในวันเดียวกัน Lead investor คือ Squarepoint Capital ซึ่ง AlphaMaven confirm ส่วน J.P. Morgan Payments, Mastercard, และ Samsung NEXT ร่วมในฐานะ strategic ข้อสังเกตคือ Mastercard ไม่ได้มาแค่เขียนเช็ค — บริษัทใช้ Firmly เป็น merchant catalog และ cart layer สำหรับ Agent Connect ซึ่งเป็น agent commerce product ของ Mastercard เอง total funding หลังรอบนี้ประมาณ $20M

**Ask Agent** คือ conversational shopping tool ที่ embed บน merchant site เอง — shopper พิมพ์ว่าอยากได้อะไร (เช่น "running shoes สำหรับวิ่ง marathon พื้นเท้า neutral งบไม่เกิน $150") Ask Agent ก็ค้นหาสินค้า, แนะนำ, ตอบคำถาม และ checkout ให้จบใน chat ไม่ต้องเปลี่ยนหน้า การ integrate ใช้ JavaScript 1 บรรทัด — ไม่ต้องสร้าง API integration หรือ ใช้ product feed ใหม่ early deployment ที่ Firmly report มี conversion rate ดีขึ้นสูงสุด 18% และ AOV ดีขึ้นสูงสุด 23% ตัวเลขเหล่านี้ company-reported ยังไม่มี third-party audit

Firmly ยังยืนยัน positioning เดิมคือ **merchant of record** — merchant ยังเป็นคนขาย, เก็บ first-party data, คุม pricing/inventory, Firmly แค่เป็น infrastructure ที่ connect agent ecosystem เข้ากับ catalog network ของ Firmly claim ว่าครอบคลุม merchants ประมาณ 11 ล้านราย — majority ของ US online GMV (gross merchandise value)

## ทำไมสำคัญ
สามเรื่องที่น่าสนใจ หนึ่ง — คนลงทุนบอกเยอะมาก **J.P. Morgan Payments + Mastercard + Samsung NEXT** ใน Series A $15M ของ startup payments/commerce startup เป็น sign ว่า tier 1 ใน payments stack ยอมเลือก startup ที่มี POV แทนที่จะ build in-house ก่อน เพราะ time-to-market สำคัญ รอ in-house ปี 2027 Shopify, Stripe, Amazon จะไปไกลแล้ว

สอง — **Ask Agent บน first-party site** คือ bet ที่น่าสนใจ ตลาด agentic commerce แยกเป็น 2 แนว: (a) agent ของ consumer (ChatGPT shopping, Perplexity Comet, Walmart Sparky) ที่ไป "ชอป" ให้ลูกค้าในหลาย store, (b) agent บน merchant site เองที่ช่วย consumer หา product และ checkout ในหน้าเดียว แนว (b) คือที่ Firmly กับ Envive และ ไปอยู่ — เถียง merchant ว่า "คุณไม่อยากเสียลูกค้าให้ aggregator เช่น ChatGPT ใช่ไหม? งั้นให้เรา embed agent บน site ของคุณเอง" argument นี้ landed เพราะ merchant กลัว disintermediation — Mastercard บอกเองว่า Agent Connect ก็ support ทั้ง 2 แนวควบคู่กัน

สาม — ตัวเลข conversion +18% / AOV +23% เป็น early results ที่ Firmly report เอง ต้อง skeptical: early deployment มักเป็น merchant ที่ pre-qualified และ enthusiastic, ไม่ใช่ random sample ถ้า scale ไปทั้ง 11M merchants จะได้ lift เท่านี้ไหม — unlikely แต่ anchor ตัวเลขที่ merchant ดู คือ "มีคน claim conversion 2 digit" ก็ชนะ

## มุม AI Agent Platform
**Builders** — Agentic commerce rail กำลังเกิด 3 layer ชัด: (1) **Agent surface** (ChatGPT, Comet, Gemini, Sparky), (2) **Agent gateway + merchant adapter** (Walmart Agent Gateway, Firmly Connect, Mastercard Agent Connect, Agentic Commerce Protocol ของ OpenAI), (3) **Merchant storefront + payments** (Shopify, Stripe, แบงก์) Firmly พยายามยืนใน layer 2 โดย abstraction คือ "1 line of JavaScript แทน full integration" คู่แข่ง Envive, Perplexity Native ก็อยู่ layer นี้

**Users / business** — ถ้าคุณเป็น merchant ไทยที่ขายผ่าน Shopify / Shopee / Lazada คำถามจริงที่ต้องตอบไม่ใช่ "AI agent จะมาซื้อของจาก store เราไหม" แต่เป็น "เมื่อ agent มาซื้อ (ปี 2027 แน่) product ของเรา indexable อยู่ใน MCP catalog หรือเปล่า และเรา control price / stock / promotion ที่ agent เห็นได้ไหม" Firmly ขาย infrastructure ที่ตอบคำถามนี้ — นี่คือ wave ต่อจาก e-commerce platform

**Ecosystem** — Google Shopping, Meta Shops, TikTok Shop ต้อง respond — ตอนนี้ control ส่วนที่ agent เข้าถึง product feed ของตัวเอง แต่ถ้า merchant ลงทุนไป Firmly / Mastercard Agent Connect ไปแล้ว อำนาจ gatekeeper ของ platform เหล่านี้ลดลง เพราะ merchant มี direct agent surface บน site ตัวเอง นี่คือ structural shift ที่จะใช้เวลา 2-3 ปี

## Sources
- [Firmly raises $15M Series A and launches Ask Agent (GlobeNewswire)](https://www.globenewswire.com/news-release/2026/11/05/3396499/0/en/firmly-raises-15-million-series-a-and-launches-ask-agent-to-help-merchants-more-easily-adopt-agentic-commerce.html)
- [JPMorgan and Mastercard back AI shopping startup Firmly (Axios Pro)](https://www.axios.com/pro/fintech-deals/2026/11/06/firmly-15-million-series-a-jpmorgan-mastercard)
- [Firmly lands $15M to sell through AI shopping assistants (Dealroom)](https://dealroom.co/news/169997-firmly-lands-15m-to-sell-through-ai-shopping-assistants/)
- [Agent-Shopping Firms Raise $30M as Uber Logs 4 Agent Rides (FourWeekMBA)](https://fourweekmba.com/ai-agent-shopping-firms-raise-30m-as-uber-logs-4-agent-rides/)

---

## Audio script
Firmly startup ที่ทำ infrastructure สำหรับ agentic commerce ปิด Series A 15 ล้านเหรียญเมื่อวันที่ 5 พฤศจิกายน พร้อมเปิดตัว product ใหม่ชื่อ Ask Agent lead investor คือ Squarepoint Capital ส่วน J.P. Morgan Payments, Mastercard, และ Samsung NEXT ร่วมด้วย ที่น่าสนใจคือ Mastercard ไม่ได้เป็นแค่นักลงทุน แต่ใช้ Firmly เป็น merchant catalog และ cart layer สำหรับ product ของตัวเองชื่อ Agent Connect Ask Agent คือ chatbox ที่ merchant embed บน site ของตัวเอง ด้วย JavaScript 1 บรรทัด ลูกค้าพิมพ์ว่าอยากได้อะไร Ask Agent ก็ค้น แนะนำ และ checkout ให้จบใน chat Firmly อ้างว่า early deployment ได้ conversion lift สูงสุด 18% และ AOV สูงสุด 23% ตัวเลขเหล่านี้ยังเป็น company-reported ที่ตลาดต้อง verify สำหรับ merchant ไทยที่ขายผ่าน Shopify, Shopee, Lazada คำถามจริงไม่ใช่ว่า AI agent จะมาซื้อของจาก store เราไหม แต่เป็นว่าเมื่อ agent มาแน่ปี 2027 product ของเรา indexable ใน MCP catalog หรือยัง และเรา control ราคา stock promotion ที่ agent เห็นได้ไหม Agentic commerce กำลังสร้าง stack 3 ชั้นชัดเจน agent surface, agent gateway, และ merchant storefront Firmly ยืนในชั้นกลาง และคู่แข่งอย่าง Envive, Perplexity Native ก็อยู่ชั้นเดียวกัน เงิน tier 1 ไหลเข้าชั้นนี้ก่อน
