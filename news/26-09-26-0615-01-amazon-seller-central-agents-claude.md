---
date: 2026-09-25
slug: amazon-seller-central-agents-claude
topic: use-case
reading_time_min: 5
sources: 5
image_prompt: |
  A dramatic editorial isometric warehouse-scale storefront cut open like a
  dollhouse; on one side a huge orange "AMAZON SELLER CENTRAL" vault door
  swings wide, on the other a small purple "CLAUDE" robot silhouette walking
  in with an OAuth key ring stamped "60 SECONDS". Behind them: three glowing
  neon panels labeled "INVENTORY", "PRICING", "LISTINGS" and a red do-not-enter
  banner over a fourth panel labeled "ADS — LOCKED". A big scoreboard reads
  "90% OF SELLERS ALREADY USE OUTSIDE AI" in contrasty numbers sized to
  read at 200px thumbnail. Editorial isometric style, brand-neutral except the
  Amazon-A and Anthropic-A logos, 1:1 aspect, no real human faces.
image: images/26-09-26-0615-01-amazon-seller-central-agents-claude.png
---

# Amazon เปิด Seller Central ให้ third-party AI agents — Claude เป็นตัวแรก, OAuth 60 วิ, ยกเว้น ads

## TL;DR
- **23 ก.ย. ที่ Amazon Accelerate** — Amazon เปิด Seller Central APIs ให้ external AI agent เข้าถึงเป็นครั้งแรก; **US beta plugin** สำหรับ **Anthropic Claude** และ **Amazon Quick**. Connect ผ่าน OAuth ใน ~**60 วินาที ไม่ต้องเขียนโค้ด** — เข้าถึง inventory, pricing, listings, sales analytics ตรงจาก chat interface
- Claude plugin ครอบ **11 skills** ที่ shipped ทันที: sales-drop diagnosis, FBA stockout risk check, suppressed-listing fix, review-response draft, ad-copy generate, etc. Amazon แถม **Quick Plus subscription ฟรี 12 เดือน** (ถึง 31 ธ.ค. 2026) ให้ primary account holder ทุกคน
- Amazon บอกเองว่า **~90% ของ seller ใช้ external AI อยู่แล้ว** ในบางส่วนของ operation — move นี้คือยอมรับความจริงและเข้ามาเป็น platform-of-record แทนที่จะให้ workflow ไหลไป ChatGPT/Claude/Cursor ข้าง ๆ. **ข้อจำกัดสำคัญ:** advertising data ถูก exclude ออกจาก beta — signal ว่า Amazon จะไม่ให้ third-party agent แตะ ad spend attribution ในเร็ว ๆ นี้

## เกิดอะไรขึ้น

**23 กันยา 2026** — Andy Jassy ประกาศบนเวที Amazon Accelerate ที่ Seattle ว่า **Seller Central APIs เปิดให้ external AI agent เข้าถึงเป็น general availability** ผ่าน US beta plugin. Beta launch จบภายในสัปดาห์เดียว, connection setup ใช้ **OAuth 2.1 flow มาตรฐาน ~60 วินาที ไม่ต้องเขียนโค้ด** — seller คลิก Enable plugin ใน Claude Desktop หรือ Amazon Quick, กด Grant access, จบ. ตั้งแต่ commit นั้น agent เห็น inventory levels, pricing, listing contributions, real-time performance metrics และ sales analytics ของ store นั้นแบบเดียวกับที่ seller เห็นใน dashboard

Claude plugin ที่ ship วันแรกครอบ **11 skills**: sales-drop root-cause diagnosis, FBA stockout risk projection, suppressed-listing repair, negative-review response drafting, product-content compliance check, pricing-elasticity what-if, competitor-price monitoring, keyword-gap analysis, listing-quality score, bulk-listing edit, และ inventory reorder planner. Amazon **Quick** (assistant ของ Amazon เอง, รัน Amazon Nova + Claude บน Bedrock) มี skill set คล้ายกัน + **bundle Quick Plus subscription ฟรี 12 เดือน** (มูลค่า ~$120 ต่อปี) ให้ primary account holder ทุกคนถึง 31 ธ.ค. 2026 เพื่อ shift adoption ไปอยู่ใน owned surface

บริบทเบื้องหลัง: Jassy บอกในคำปราศรัยว่า **~90% ของ Amazon seller ใช้ external AI tool** ในบางส่วนของ operation อยู่แล้ว — จาก Helium 10 ถึง ChatGPT ถึง in-house scripts. เดิม workflow นี้ต้องผ่าน screen-scraping หรือ manual copy-paste เพราะ Seller Central ไม่มี stable public API สำหรับ agent — ตอนนี้ Amazon เลือกที่จะเปิดประตูให้ instead of ปล่อยให้ scraper economy โต. **ข้อจำกัดที่ต้อง watch:** advertising campaigns, bids, ACoS optimization ถูก exclude ทั้งหมด. **PPC agency แหล่งเดียวที่ยังปลอดภัย** จาก agent takeover ในช่วงนี้ — Amazon เก็บ ad platform ไว้ในกำมือตัวเอง ยังไม่มี timeline ที่จะเปิด

**ตัวเลขบริบท:** Amazon marketplace มี ~**2 ล้าน active seller** ทั่วโลก, GMV **~$400B+ ต่อปี** (Amazon ไม่เปิดเลข exact แต่ analyst estimate). ถ้า plugin จะ hit target 20% adoption ใน 6 เดือน = **~400k seller ที่มี agent-in-the-loop** — จำนวน API call ที่ Bedrock/Anthropic infra จะรับใน US region อาจโตเป็น double-digit millions/day

## ทำไมสำคัญ

**Hyperscaler platform strategy กำลัง flip.** จนถึง Q3 2026 pattern ที่เห็นคือ: platform (Amazon, Salesforce, Shopify, HubSpot) build "in-house AI assistant" ที่กีดกัน third-party — ทำให้ workflow อยู่ใน UI ตัวเอง. Amazon ครั้งนี้เลือกทางตรงข้าม: **ยอมให้ Claude เข้าเป็น first-class access layer** โดยรู้ดีว่า seller จะย้าย attention ออกจาก seller.amazon.com. เหตุผลคือ realism — 90% ใช้ external AI อยู่แล้ว, สู้ไม่ได้ ก็เข้าร่วมและควบคุม API surface แทน. เทียบกับ Salesforce "Claudeforce" (25 ส.ค.) และ Google-Salesforce headless partnership (15 ก.ย.) — **enterprise SaaS ทุกเจ้ากำลัง converge ที่ pattern เดียวกัน**: expose data + workflow ผ่าน MCP/API, ให้ agent layer ที่ customer เลือกเองเข้ามา orchestrate

Pattern ที่จับได้ในเดือน ก.ย.: **Amazon เปิด Seller Central → Salesforce เปิด Data Cloud → Google เปิด Workspace → Anthropic คู่กับทุกคน**. Anthropic กำลังกลายเป็น **default agent runtime layer สำหรับ enterprise commerce** — Claudeforce, Amazon Seller Assistant, และ Salesforce in Claude beta ทั้งหมด ship ในเดือนเดียว. OpenAI ยังไม่มี equivalent partnership กับ e-commerce hyperscaler — GPT-6 Sol ลดราคาแรง (22 ก.ย.) แต่ platform-level integration ที่ enterprise ซื้อได้ยังตามหลัง

จุดที่ต้องจับตา: **การที่ ads ถูก exclude คือ signal นโยบายที่ใหญ่กว่า plugin นี้**. Amazon ad business ทำ revenue **~$50B+ ต่อปี** (2025 run-rate) — margin สูงมาก, เป็น protective moat หลักของ Amazon retail economics. Amazon ไม่ยอมให้ agent optimize ad spend เพราะ agent ที่ฉลาดพอ = auction efficiency สูงขึ้น = Amazon ad revenue ลง. **นี่คือ template ที่ทุก marketplace/platform จะทำตาม** — เปิดสิ่งที่ commoditize ไปแล้ว (listing management), ปิดสิ่งที่เป็น profit engine (ads, matching algorithm, discovery). Builder ต้องอ่าน API scope map ทุก platform อย่างละเอียดก่อน bet product line

## มุม AI Agent Platform

สำหรับ **builders** ที่ทำ agent platform สำหรับ Amazon seller (Helium 10, Jungle Scout, DataDive, Perpetua, Pacvue, และ startup ที่กำลัง raise seed) — **moat ของ third-party seller tool อ่อนลงทันที**. เดิม value prop คือ "เรามี scraping infra + data pipeline + UI" — ตอนนี้ Amazon เปิด API เอง, ChatGPT plugin + Claude plugin ทำงานเดียวกันได้ฟรี. **Builders ต้องย้ายไป layer ที่ Amazon ไม่ครอบ** — ads optimization, cross-marketplace (eBay + Walmart + Amazon), forecasting models ที่ train บน proprietary data, หรือ agent-of-agents ที่ orchestrate ทั้ง supply chain. ตัวไหน stuck ที่ "AI-powered listing optimizer" — 12 เดือนข้างหน้าจะเจอ churn สูง

สำหรับ **enterprise seller และ agency** — **ROI model ของ Amazon operation ควร reopen ทันที**. Cost ของการ hire VA (Virtual Assistant) หรือ agency ทำ inventory management, listing repair, review response = **$2,000–8,000/month ต่อ seller mid-tier**. Plugin ใช้ ~$50–200/month ค่า Claude/Quick + agent time = **cost reduction 90%+ สำหรับงาน operational**. ปัญหาคือ quality — plugin generation แรก skill 11 ตัวยังไม่ทดแทน senior PPC หรือ growth strategist ที่รู้ category context ลึก. **แนะนำ hybrid setup**: agent ทำ operational grunt (stockout, listing fix, review response), human ทำ strategy + ads + brand voice — cost overall ลง 40–60%, quality ไม่ตก. Pare's analysis หลังงาน Accelerate สรุปตรงจุดนี้ว่า "Amazon AI tools require a senior PPC hire" — plugin ทดแทน junior, ไม่ใช่ senior

สำหรับ **ecosystem** — Bedrock (Amazon) และ Anthropic ทั้งคู่ = winner ทันที; API traffic ที่ผ่าน Bedrock จาก Seller Assistant คือ **new baseline volume** ที่ยั่งยืน. Shopify, Etsy, Walmart Marketplace, TikTok Shop จะถูกกดดันให้ launch equivalent plugin ภายใน 3–6 เดือน หรือเสี่ยง lose seller mind-share. Shopify มี "Sidekick" agent อยู่แล้วแต่ยังปิด — เดิมพันคือจะเปิด API ตามหรือไม่. สำหรับทีมไทยที่ขายบน Amazon US หรือ EU — plugin เปิด US beta ก่อน, JP/EU rollout คาดว่า Q1–Q2 2027. ทีมที่มี US entity เริ่มทดลองได้ตั้งแต่วันนี้; ทีมที่ขายเฉพาะ Amazon SG/JP ต้องรอ

## Sources
- [Amazon opens its seller tools to outside AI agents, starting with Anthropic's Claude — GeekWire](https://www.geekwire.com/2026/amazon-opens-its-seller-tools-to-outside-ai-agents-starting-with-anthropics-claude/)
- [Amazon gives sellers an even smarter Seller Assistant and a new plugin for Amazon Quick and Anthropic's Claude — About Amazon](https://www.aboutamazon.com/news/innovation-at-amazon/seller-assistant-plugin-amazon-quick-claude)
- [Amazon Brings Seller Assistant to Claude and Amazon Quick — Unite.AI](https://www.unite.ai/amazon-brings-seller-assistant-to-claude-and-amazon-quick/)
- [Amazon Seller Assistant - Plugin for Amazon Quick and Anthropic's Claude — ChannelX](https://channelx.world/2026/09/amazon-seller-assistant-plugin-for-amazon-quick-and-anthropics-claude/)
- [Amazon Accelerate AI Tools Require a Senior PPC Hire — Pare](https://pare.so/blog/amazon-accelerate-2026-ai-tools-human-ppc-hire-signal)

---

## Audio script
วันที่ 23 กันยา 2026 บนเวที Amazon Accelerate ที่ Seattle, Andy Jassy ประกาศเรื่องใหญ่ที่จะเปลี่ยน landscape ของ Amazon seller ทั้งวงการ — Amazon เปิด Seller Central APIs ให้ external AI agent เข้าถึงเป็นครั้งแรก, launch เป็น US beta plugin สำหรับ Anthropic Claude และ Amazon Quick ของตัวเอง. Setup ใช้ OAuth flow มาตรฐาน 60 วินาทีไม่ต้องเขียนโค้ด — seller คลิก enable plugin, กด grant access, จบ. Agent ก็เห็น inventory, pricing, listings, sales analytics ตรงจาก chat ได้ทันที. Claude plugin ครอบ 11 skills ที่ ship วันแรก — sales-drop diagnosis, FBA stockout risk check, suppressed-listing fix, review-response draft และอื่น ๆ. Amazon แถม Quick Plus subscription ฟรี 12 เดือนถึงสิ้นปี 2026 ให้ primary account holder ทุกคน เพื่อ shift adoption ไปอยู่ใน surface ของตัวเอง. บริบทที่สำคัญคือ Amazon ยอมรับเองว่า 90 เปอร์เซ็นต์ของ seller ใช้ external AI tool อยู่แล้ว — สู้ไม่ได้ก็ยอมเปิด API ให้ Claude เข้าเป็น first-class citizen แทนที่จะปล่อยให้ workflow ไหลไป ChatGPT ข้าง ๆ. แต่มีจุดที่ต้อง watch ให้ดี — advertising data ถูก exclude ออกจาก beta ทั้งหมด. PPC agency คือแหล่งเดียวที่ยังปลอดภัยจาก agent takeover ในช่วงนี้ เพราะ Amazon ad business ทำ revenue 50 พันล้านดอลลาร์ต่อปี margin สูง เป็น profit engine หลักที่ Amazon ไม่ยอมเปิด. Pattern ที่จับได้เดือนกันยานี้คือ enterprise SaaS ทุกเจ้ากำลัง converge — Salesforce Claudeforce ปลายเดือน สิงหา, Google-Salesforce headless partnership 15 กันยา, และ Amazon Seller Assistant วันนี้. Anthropic กำลังกลายเป็น default agent runtime layer สำหรับ enterprise commerce. สำหรับ builder ไทย ถ้าทำ third-party tool สำหรับ Amazon seller — ต้องย้ายไป layer ที่ Amazon ไม่ครอบทันที เช่น ads optimization, cross-marketplace หรือ forecasting model. ทีมที่ขายบน Amazon US หรือ EU เริ่มทดลอง plugin ได้เลย; ขายเฉพาะ SG/JP ต้องรอ Q1 ปีหน้า.
