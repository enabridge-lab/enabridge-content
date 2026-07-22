---
date: 2026-07-23
slug: michaels-ask-mike-gemini-enterprise-75k-conversations-early-results
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: |
  An editorial isometric illustration on a warm cream background: a
  storefront titled "MICHAELS" with a giant chat kiosk labeled "ASK MIKE"
  in the window; three floating stat cards read "75,000 CONVERSATIONS",
  "60% PRODUCT DISCOVERY", "6 WEEKS CONCEPT-TO-PRODUCTION". A shopping
  cart rolls out the door with fabric bolts, paint tubes, and craft
  supplies; above the storefront a small ribbon reads "BUILT WITH GEMINI
  ENTERPRISE". Sharp editorial typography, high contrast, 1:1 aspect, no
  real human faces.
image: images/26-07-23-0610-04-michaels-ask-mike-gemini-enterprise-75k-conversations-early-results.png
---

# Michaels "Ask Mike" ปล่อยตัวเลข early — 75,000 conversation, 60% product discovery, 6 สัปดาห์จาก concept ถึง production บน Google Gemini Enterprise

## TL;DR
- 21-22 ก.ค. Michaels (arts + crafts retailer สหรัฐ, market cap ~$4B) เปิดตัว "Ask Mike" อย่างเป็นทางการ — AI shopping assistant built บน Google Cloud Gemini Enterprise for Customer Experience — พร้อม early result ที่ deploy เงียบ ๆ ตั้งแต่พฤษภาคม
- **75,000 conversation** ใน 2 เดือน, **60% ของ interaction เป็น product discovery** (ที่เหลือ 40% เป็น project planning + inspiration), ตัวอย่าง prompt: "help me plan my child's birthday party", "I need a fabric for DIY curtains"
- Google Cloud อ้าง — Michaels ทำจาก concept ถึง production-grade AI ใน **6 สัปดาห์** — signal ที่ Google บอกว่า retail industry กำลัง move ไปทางที่ agent + retail จะ integrate ระดับ default
- Available บน Michaels.com + iOS app + Android app, ทำงานเป็น conversational commerce interface ที่ทดแทน keyword search + filter tree ปกติ
- Signal: **vertical-specific agent + hyperscaler platform + short deployment cycle** = pattern ที่ retail จะ replicate ใน 12 เดือน; Michaels + Google เป็น case study ที่ Sephora, Home Depot, Lowe's, Best Buy จะเรียนก่อน Q4 shopping season

## เกิดอะไรขึ้น
วันที่ 21 กรกฎาคม Michaels (Fortune 1000 arts + crafts retailer, 1,200+ store, market cap ~$4B) ประกาศ Ask Mike อย่างเป็นทางการผ่าน press release + Google Cloud Press Corner. ตามด้วย Digital Commerce 360 วันที่ 22 ก.ค. ที่รายงาน early result — assistant นี้จริง ๆ ไม่ใช่ new launch, เป็น soft-launch ที่ Michaels เปิดใช้เงียบ ๆ ตั้งแต่พฤษภาคม 2026 บน Michaels.com + iOS app + Android app, สะสม data 2 เดือนก่อนประกาศ.

ตัวเลขที่รายงาน: **75,000 conversation** ใน ~2 เดือน (avg ~1,200 conversation/day — สูงพอสำหรับ retailer ระดับ Fortune 1000 แต่ยังห่างจาก mass adoption). **60% ของ interaction เป็น product discovery** — shopper describe project ที่อยาก build (party, DIY curtain, quilting project, kids' craft night) แล้ว agent recommend product + material list. ที่เหลือ 40% แบ่งเป็น inspiration + planning + how-to guidance. Michaels ยกตัวอย่าง prompt ที่ receive จริง — "help me plan my child's birthday party", "I need a fabric for DIY curtains" — สื่อว่า user interact ในภาษาธรรมชาติ ไม่ใช่ keyword mode.

Ask Mike built บน **Google Cloud Gemini Enterprise for Customer Experience** — วง product ที่ Google เพิ่งประกาศ GA เดือนก่อน, targeting retail + hospitality + travel + telco. Under the hood ใช้ Gemini 3.5 Flash เป็น backbone (พร้อม fine-tune บน Michaels product catalog + brand voice + inventory), Vertex AI Search สำหรับ product retrieval, และ Contact Center AI สำหรับ escalation ไป human agent. Google Cloud ในการ press release เน้นว่า **Michaels ทำจาก concept ถึง production-grade ใน 6 สัปดาห์** — ตัวเลขที่ Google ต้องการเป็น flag ใน RFP ต่อไป (เทียบกับ typical enterprise deployment ที่กิน 6-12 เดือน).

Digital Commerce 360 ตั้งข้อสังเกตว่า Michaels ยังไม่เปิดเผย conversion rate (จาก conversation ไป purchase), average order value uplift, หรือ revenue attribution — สาม metric ที่ CFO อยากเห็น. บริษัทบอกว่า "จะ share detailed metric ใน Q3 earning call" (สิงหาคม). ตัวเลข 60% product discovery อ่าน positive แต่ยังไม่ direct revenue signal — คู่เทียบที่ต้อง watch คือ Sephora Beauty Advisor (Salesforce Agentforce, launch พ.ค.) ที่รายงาน 22% conversion lift ใน Q2 earning, และ Best Buy My Best Buy Assistant (Amazon Bedrock, launch เม.ย.) ที่รายงาน $180 AOV lift.

## ทำไมสำคัญ
Michaels case study **ตอบ HCLTech 90-vs-18 gap ตรง ๆ** (ดู brief #2) — 60% product discovery interaction คือ **operational signal ที่มีโอกาสสูงจะแปลงเป็น revenue impact** ถ้า Michaels สามารถ track attribution ได้จริง. Google Cloud รู้ว่า retail vertical เป็นตลาดที่ ROI proof-point ต้องเข้ม, จึง push case study นี้เข้าตลาดในสัปดาห์เดียวกับที่ Gemini 3.6 Flash release (ดู brief #3) และ HCLTech report ปล่อย — orchestrated PR ที่ตั้งใจตอบข้อกังขา revenue impact.

Pattern ที่กำลังก่อตัว: **vertical-specific agent + hyperscaler platform + short deployment cycle**. เมื่อปีที่แล้ว retail agent ยังเป็น bespoke build ที่ต้องใช้ 12-18 เดือน + $5-10M budget (Sephora ยุคแรก, Nike, Levi's). ปีนี้ Google Gemini Enterprise + AWS Bedrock AgentCore + Microsoft Copilot Studio + Salesforce Agentforce ทำให้ deployment timeline หด **6-8 สัปดาห์ ที่ $500K-$1.5M budget**. Q4 shopping season 2026 (Black Friday, Cyber Monday, Christmas) จะเป็นครั้งแรกที่ mid-size retailer (revenue $1-10B) มี AI shopping assistant ใน production พร้อม gan. Sephora, Home Depot, Lowe's, Best Buy, Kohl's, Bed Bath & Beyond, Wayfair, Etsy — ทุกเจ้าจะมี agent ก่อน Thanksgiving หรือเสียเปรียบ shelf discovery.

Second-order signal: **conversational commerce interface กำลังทดแทน keyword search + filter tree** ในบางประเภท shopping. keyword search + facet filter (Amazon-style) ยัง dominant สำหรับ commodity shopping (electronics, groceries) แต่ project-based shopping (crafts, home improvement, party planning, gift discovery, apparel styling) จะเปลี่ยนไปเป็น conversational-first UI ในไตรมาสถัดไป. Retail site ที่ไม่มี "chat with our assistant" button ที่ prominent จะเสีย engagement + bounce rate เพิ่มใน Q4.

Third-order signal — **Google Cloud กำลังชนะ retail vertical เหนือ AWS + Azure**. Michaels + Google, Home Depot + Google (ประกาศ May 2026), Best Buy + AWS, Wayfair + Azure — Google กำลัง focus retail มากที่สุดในสามฝั่ง. ตัวเลข 6-week deployment เป็น marketing weapon ที่ Google จะใช้ต่อสัปดาห์นี้ที่ Google Cloud Retail Summit (5-6 สิงหาคม).

## มุม AI Agent Platform
สำหรับ **builders** ที่ทำ retail-focused agent — ให้อ่าน Michaels playbook เป็น reference: (1) soft-launch 2 เดือน ก่อน announce เพื่อ collect real interaction data + polish behavior; (2) reserved data disclosure สำหรับ Q3 earning เพื่อ tie AI story เข้ากับ CFO narrative; (3) integrate Gemini Enterprise / Bedrock AgentCore / Copilot Studio + Contact Center AI ตั้งแต่ day one เพื่อ escalation path; (4) design conversational-first UI, keep keyword search เป็น fallback. อย่าสร้าง agent เป็น "add-on chatbot" — วาง agent เป็น primary discovery interface.

สำหรับ **users / business** — ถ้าคุณเป็น CDO/CIO ของ retailer ที่มี revenue > $500M, สัปดาห์นี้ทำสามอย่าง: (1) evaluate Google Gemini Enterprise for CX vs Salesforce Agentforce vs AWS Bedrock AgentCore vs Amazon Connect + Bedrock — RFP short list ต้อง short (3-4 vendor); (2) commit deployment timeline **6 สัปดาห์ soft-launch + 4 สัปดาห์ tuning + Nov 1 GA** เพื่อทัน Q4 shopping season; (3) ตกลง KPI ล่วงหน้า — conversation-to-purchase conversion, AOV uplift, revenue attribution, escalation rate. ถ้าไม่ทัน Q4 นี้, missed season = missed year. สำหรับ **ecosystem** — retail-focused agent vendor (Sierra, Fetch.ai, Rebuy, Constructor.io, Bloomreach) จะแข่งหนักกับ hyperscaler vertical playbook. Consulting firm ที่ทำ retail practice (Deloitte Digital, Publicis Sapient, Accenture Song, IBM Consulting) จะเห็น engagement เพิ่ม 40-60% ใน Q3 จาก retailer ที่เร่ง deploy ก่อน Q4.

## Sources
- [Michaels Unveils 'Ask Mike' AI Assistant, Built With Google Cloud's Gemini Enterprise for Customer Experience — Google Cloud Press Corner (20 Jul)](https://www.googlecloudpresscorner.com/2026-07-20-Michaels-Unveils-Ask-Mike-AI-Assistant-Built-With-Google-Clouds-Gemini-Enterprise-for-Customer-Experience)
- [Michaels shares early results from its Gemini-powered AI assistant — Digital Commerce 360 (22 Jul)](https://www.digitalcommerce360.com/2026/07/22/michaels-early-results-google-gemini-powered-ai-assistant/)
- [Michaels Launches 'Ask Mike' AI-Powered Shopping Assistant — Retail TouchPoints (21 Jul)](https://www.retailtouchpoints.com/news/michaels-launches-ask-mike-ai-powered-shopping-assistant/620561/)
- [Michaels Debuts Google-Powered AI Shopping Assistant — PYMNTS (21 Jul)](https://www.pymnts.com/news/artificial-intelligence/2026/michaels-debuts-google-powered-ai-shopping-assistant/)
- [Michaels teams with Google on new 'Ask Mike' AI shopping assistant — Chain Store Age (21 Jul)](https://chainstoreage.com/michaels-teams-google-new-ask-mike-ai-shopping-assistant)

---

## Audio script
วันนี้ 21 ถึง 22 กรกฎาคม Michaels เปิดตัว Ask Mike อย่างเป็นทางการครับ AI shopping assistant ที่ build บน Google Cloud Gemini Enterprise for Customer Experience พร้อม early result ที่ deploy เงียบ ๆ ตั้งแต่พฤษภาคม ตัวเลขที่รายงาน 75,000 conversation ใน 2 เดือน 60 เปอร์เซ็นต์ของ interaction เป็น product discovery ที่เหลือ 40 เปอร์เซ็นต์เป็น inspiration และ planning ตัวอย่าง prompt ที่ Michaels เผย help me plan my child's birthday party หรือ I need a fabric for DIY curtains สื่อว่า user interact ในภาษาธรรมชาติ ไม่ใช่ keyword mode Ask Mike ใช้ Gemini 3.5 Flash เป็น backbone พร้อม fine-tune บน product catalog กับ brand voice ใช้ Vertex AI Search สำหรับ product retrieval และ Contact Center AI สำหรับ escalation Google Cloud เน้นว่า Michaels ทำจาก concept ถึง production-grade AI ใน 6 สัปดาห์ ตัวเลขที่ Google จะใช้เป็น marketing weapon ต่อสัปดาห์นี้ที่ Google Cloud Retail Summit 5 ถึง 6 สิงหาคม ทำไมสำคัญครับ Michaels case study ตอบ HCLTech 90 vs 18 gap ตรง ๆ 60 เปอร์เซ็นต์ product discovery interaction คือ operational signal ที่มีโอกาสสูงจะแปลงเป็น revenue impact ถ้า Michaels สามารถ track attribution ได้จริง จะรายงานตัวเลขเต็มใน Q3 earning call เดือนสิงหาคม Pattern ที่กำลังก่อตัวคือ vertical-specific agent + hyperscaler platform + short deployment cycle เมื่อปีที่แล้วต้องใช้ 12 ถึง 18 เดือน 5 ถึง 10 ล้านดอลลาร์ ปีนี้ Google Gemini Enterprise AWS Bedrock AgentCore Microsoft Copilot Studio Salesforce Agentforce ทำให้ deployment หด 6 ถึง 8 สัปดาห์ 500K ถึง 1.5M ดอลลาร์ Q4 shopping season 2026 จะเป็นครั้งแรกที่ mid-size retailer มี AI shopping assistant พร้อม gan Sephora Home Depot Lowe's Best Buy Kohl's Bed Bath Wayfair Etsy ทุกเจ้าจะมี agent ก่อน Thanksgiving หรือเสียเปรียบ shelf discovery สำหรับ CDO CIO ของ retailer ที่มี revenue เกิน 500 ล้าน สัปดาห์นี้ evaluate Google Gemini Enterprise vs Salesforce Agentforce vs AWS Bedrock AgentCore commit deployment timeline 6 สัปดาห์ soft-launch + 4 สัปดาห์ tuning + Nov 1 GA เพื่อทัน Q4 ถ้าไม่ทัน Q4 นี้ missed season = missed year ครับ
