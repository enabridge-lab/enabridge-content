---
date: 2026-07-06
slug: salesforce-agentforce-commerce-chatgpt-native
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  A wide editorial isometric scene: a huge shopping cart at center, split
  into three lanes flowing out labeled "SHOPPER AGENT", "BUYER AGENT",
  "MERCHANT AGENT". At the top of each lane, a channel gate labeled
  "CHATGPT — GA JULY", "GOOGLE AI MODE — SUMMER", "GEMINI APP — SUMMER".
  A giant number in bright orange reads "+59% SALES GROWTH" with subtitle
  "RETAILERS RUNNING SHOPPER AGENTS". At bottom-right, a silhouette of a
  shopper walks toward a phone screen showing an AI chat with a product
  card. Editorial isometric style, high-contrast cinematic lighting,
  1:1 aspect, readable at 200px thumbnail, no real human faces.
image: images/26-07-06-0609-04-salesforce-agentforce-commerce-chatgpt-native.png
---

# Salesforce Agentforce Commerce ปิด GA พร้อม ChatGPT-native (ก.ค.) + Google AI Mode + Gemini — retailer ที่รัน Shopper Agent โต 59% เร็วกว่าคู่แข่ง

## TL;DR
- Salesforce ประกาศ **Agentforce Commerce GA** พร้อม 3 agent — **Shopper (B2C), Buyer (B2B), Merchant (back office)** — ChatGPT native integration **GA กรกฎาคม 2026**; Google Search AI Mode + Gemini app "**arriving this summer**"
- ตัวเลข retail: **retailer ที่รัน shopper agent โต sales 59% เร็วกว่าคู่แข่งที่ยังไม่ deploy** — Salesforce quote จาก data internal
- Buyer Agent เข้าไป live ใน **WhatsApp + SMS** โดยตรง (B2B use case); Merchant Agent จัดการ catalog + trend + product listing ผ่าน natural language

## เกิดอะไรขึ้น
Salesforce เผยรายละเอียดของ **Agentforce Commerce GA** เพิ่มเติมช่วง 30 มิ.ย. – 3 ก.ค. — 3 agent core:

1. **Shopper Agent** (B2C) — carry customer conversation ตั้งแต่ discovery → checkout → service; ใช้ voice + tone ของ brand; แชท conversation-first แทน "click through 4 หน้าจน checkout"
2. **Buyer Agent** (B2B) — เข้าไป live ใน **WhatsApp + SMS** ทางตรง; รับ order + reorder + technical Q&A จาก procurement/distributor ที่ไม่เข้ามาที่ portal
3. **Merchant Agent** (back office) — จัดการ catalog / product sorting / trend response ผ่าน natural language แทน dashboard 15 tab

**Distribution channel ที่ big signal**: agents เหล่านี้จะไป **live native ใน ChatGPT (GA กรกฎาคม 2026)**, **Google Search AI Mode**, และ **Gemini app** ("arriving this summer" ตาม Salesforce). แปลว่า **customer ที่ถาม ChatGPT "หา cushion ที่นุ่มพิเศษสำหรับ back pain" จะได้ product recommend ตรงจาก Shopper Agent ของ retailer เจ้านั้น** (assumption: retailer setup Shopper Agent + ChatGPT connector)

Salesforce บอกตัวเลข retail ตรง ๆ: **retailer ที่รัน shopper agent (early adopter cohort ที่ pilot ตั้งแต่ Q1 2026) โต sales 59% เร็วกว่า retailer ที่ยังไม่ deploy**. ตัวเลขจาก Salesforce internal data, ยังไม่มี third-party audit — แต่ pattern สอดคล้องกับ shopper agent ที่ Levi's / Sephora / Wayfair ประกาศแยกต่างหากช่วง 6 เดือนที่ผ่านมา

Adam Blitzer, EVP GM Salesforce Commerce, quote สั้น: "**AI Assistants grow retail traffic volumes by 119%**" — traffic mix เปลี่ยนจาก search engine + direct → conversational surface (ChatGPT/Gemini/Claude/Perplexity)

## ทำไมสำคัญ
คำถามที่ retailer ถามตลอด 12 เดือน = **"ChatGPT/Gemini/AI Overview กำลังกิน SEO traffic ของฉันหรือเปล่า"** คำตอบเดิมที่มีคือ "**ตั้งรับ**: optimize schema.org, feed product catalog เข้า ChatGPT connector, จ่าย affiliate revenue share เมื่อ customer click มาจาก AI channel". Agentforce Commerce เสนอ **ตั้งรุก**: **agent ของ retailer เอง live อยู่ใน ChatGPT/Gemini/Search AI Mode** — customer conversation อยู่ที่ retailer, ไม่ใช่ที่ platform

Pattern เทียบ: **App Store 2008 vs SEO 2005 vs AI Agent 2026**
- App Store 2008 — retailer ที่ ship native app early ได้ direct customer relationship
- SEO 2005 — retailer ที่ own long-tail organic search ได้ margin ต่อ traffic
- AI Agent 2026 — retailer ที่ **ship Shopper Agent เข้า ChatGPT/Gemini early** ได้ conversation ownership ที่ platform ยังยอมให้อยู่

**Distribution moat** ของ Salesforce ที่ retailer อื่นยัง match ยาก:
- Salesforce Commerce Cloud ครอง Fortune 500 retail (Ralph Lauren, PVH, L'Oréal, Adidas ที่ประกาศ, Lululemon ที่ pilot) — install base ที่พร้อม
- Native integration กับ ChatGPT/Gemini = **deal ที่ OpenAI + Google เซ็นกับ Salesforce ตรง** (ไม่ใช่ทุก retailer สร้างเอง)
- Merchant Agent + Shopper Agent + Buyer Agent = pattern **supervisor + specialized worker** ที่ Aim/Levi's ก็ใช้ — Salesforce ship ในระดับ **product ที่ CPG/retail sign contract ผ่าน AWS Marketplace EDP** (deal Salesforce+AWS 2 ก.ค.)

Signal ระยะกลาง: **แต่ละ retailer / brand จะมี "digital storefront on ChatGPT/Gemini" เป็น line item ในงบ 2027**. Shopify ตอบ ChatGPT connector มาก่อน (มี.ค. 2026) แต่เป็น catalog-level connector, ไม่ใช่ **agent ที่ตัดสินใจให้ customer**. Amazon (Anthropic partner) + Walmart (Sparky AI) เดิน sub-strategy — retail giants มี ecosystem ของตัวเอง; Salesforce + retail brand ที่ไม่ใช่ Amazon/Walmart = coalition ธรรมชาติ

Business angle: ตัวเลข **59% growth premium** เป็นตัวเลขที่ CFO retail อ่านแล้ว **หยุดถามว่า ROI** — เปลี่ยน conversation ไปที่ "budget setup" ทันที. Agentforce ARR ล่าสุด $800M (fiscal Q4 2025, +169% YoY) — Commerce เป็น engine ต่อไปที่ Salesforce ต้องการ push ให้ทะลุ $1B ARR ในไตรมาสหน้า

## มุม AI Agent Platform
- **Builders** — startup ที่สร้าง **agentic commerce infra** (Product agent, Cart agent, Return agent, Loyalty agent) — window ปิดเร็ว. Salesforce+ChatGPT+Gemini ผูก 80% ของ Fortune 500 retail; ที่เหลือคือ **long-tail SMB retail** ที่ Shopify ครองอยู่ + emerging market. **Shopify apps ecosystem** = window ดี — ship agent-based app ที่ integrate ChatGPT connector + Instagram/TikTok shop. Framework builders — **A2A / MCP interoperability** ระหว่าง Shopper Agent (Salesforce) กับ Buyer Agent ของ manufacturer เป็น pain point ยังไม่มี standard ที่ scale

- **Users/business ในไทย** — **retailer + brand ในไทย ที่มี Salesforce Commerce Cloud** (Central, King Power, PTG, PC, HomePro, Emporium/EmQuartier online, ThaiBev retail) — พร้อม trial Agentforce Commerce; window ที่ควร activate = Q3 2026. **retailer/brand ที่ยังใช้ Shopify + Magento** — คุยกับ Shopify APAC สำหรับ ChatGPT connector + Shop Assistant. **CPG brand ที่ไม่มี D2C store** (Osotspa, ThaiBev consumer, DTAC brand, AIS brand) — เริ่มมี rationale ที่จะ **build agent-native storefront เพื่อ own AI conversation** แทนที่จะรอ retailer ทำแทน. **Regulated retail (pharmacy, banking product, insurance)** — Buyer Agent บน WhatsApp/SMS เป็น channel ที่มี regulatory boundary ที่ต้อง review PDPA + BOT + OIC ก่อน rollout

- **Ecosystem** — **Amazon+Anthropic** (Rufus + Alexa+ agent) + **Walmart Sparky** = closed ecosystem; **Salesforce+OpenAI+Google** = coalition; **Shopify+ChatGPT** = SMB tier. **Meta AI agent for WhatsApp Business** (Global rollout มิ.ย. 2026) — คู่แข่ง Buyer Agent ของ Salesforce ตรง ๆ. คาดว่า H2 2026 – Q1 2027 จะเห็น **agentic commerce protocol** (แบบ MCP for commerce) ที่ standardize product catalog + payment + return signal — Salesforce กับ Shopify + Stripe น่าจะ push standard ตัวนี้

## Sources
- [As AI Agents Transform Commerce, Salesforce Unleashes Its Biggest Agentforce Commerce Release Yet — Salesforce News](https://www.salesforce.com/news/stories/agentforce-commerce-announcement/)
- [Salesforce Makes Agentforce Commerce Generally Available Ahead of Peak Season — CX Today](https://www.cxtoday.com/crm/salesforce-agentforce-commerce-generally-available/)
- [Salesforce's Agentforce Commerce GA lands ahead of peak season with Shopper, Buyer and Merchant agents — Martech Notes](https://www.martechnotes.com/salesforces-agentforce-commerce-ga-lands-ahead-of-peak-season-with-shopper-buyer-and-merchant-agents/)
- [Salesforce Unveils Agentforce Commerce Capabilities as AI Assistants Grow Retail Traffic Volumes by 119% — Salesforce News](https://www.salesforce.com/news/stories/agentforce-commerce-capabilities-announcement/)

---

## Audio script
Salesforce ประกาศรายละเอียดของ Agentforce Commerce GA เพิ่มเติมช่วงปลายมิถุนายนต่อต้นกรกฎาคม มี 3 agent หลัก Shopper Agent สำหรับ B2C ที่ carry conversation จาก discovery ถึง checkout ถึง service Buyer Agent สำหรับ B2B ที่ live ใน WhatsApp กับ SMS สำหรับ procurement กับ distributor และ Merchant Agent สำหรับหลังบ้านที่จัดการ catalog กับ trend ด้วย natural language ที่น่าสนใจสุดคือ distribution channel agents เหล่านี้จะไป live native ใน ChatGPT ประกาศ GA กรกฎาคม 2026 พร้อม Google Search AI Mode กับ Gemini app ในหน้าร้อนนี้ แปลว่า customer ที่ถาม ChatGPT ว่าหา cushion ที่นุ่มพิเศษสำหรับ back pain จะได้ product recommend ตรงจาก Shopper Agent ของ retailer เจ้านั้น ตัวเลขที่ Salesforce เปิดคือ retailer ที่รัน shopper agent โต sales 59% เร็วกว่าคู่แข่งที่ยังไม่ deploy พร้อมกับตัวเลข AI Assistants grow retail traffic volumes 119% pattern คือ retailer ที่ ship Shopper Agent เข้า ChatGPT Gemini early จะได้ conversation ownership ที่ platform ยังยอมให้อยู่ เทียบได้กับ App Store 2008 หรือ SEO 2005 สำหรับ retail ในไทยที่มี Salesforce Commerce Cloud อยู่แล้ว อย่าง Central King Power PTG HomePro พร้อม trial Agentforce Commerce ใน Q3 นี้เลย retailer ที่ยังใช้ Shopify Magento ก็คุยกับ Shopify APAC สำหรับ ChatGPT connector กับ Shop Assistant CPG brand ที่ไม่มี D2C store อย่าง Osotspa ThaiBev DTAC AIS มี rationale ที่จะสร้าง agent-native storefront เพื่อ own AI conversation แทนที่จะรอ retailer ทำแทน สำหรับ regulated retail อย่าง pharmacy banking product insurance ให้ review PDPA BOT OIC ก่อน rollout Buyer Agent บน WhatsApp SMS ระยะสั้น pattern นี้จะเปลี่ยนงบ marketing ของ retail ทุกเจ้าใน 2027 ให้บวก digital storefront on ChatGPT and Gemini เป็น line item ใหม่
