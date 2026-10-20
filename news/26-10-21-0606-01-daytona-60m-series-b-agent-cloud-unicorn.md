---
date: 2026-10-21
slug: daytona-60m-series-b-agent-cloud-unicorn
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a cloud-shaped data center split into
  thousands of tiny glass cubicles, each one labeled "DIGITAL EMPLOYEE" and lit
  from within. A central spire rises above the cubicles with three stacked
  neon numbers: "$60M SERIES B", "$1B VALUATION", "25x REVENUE JAN→SEP".
  Nine floating logo-badges in a halo around the spire read "ANTHROPIC",
  "OPENAI", "NVIDIA", "CURSOR", "COGNITION", "META", "COHERE", "POSTMAN",
  "FIRSTMARK". Cobalt and amber palette, strong contrast for 200px thumbnails,
  1:1 aspect, no real human faces.
image: images/26-10-21-0606-01-daytona-60m-series-b-agent-cloud-unicorn.png
---

# Daytona ปิด $60M Series B ที่ $1B — "ที่ให้ digital employee ล้มเหลวได้อย่างปลอดภัย" กลายเป็น unicorn ภายใน 8 เดือน

## TL;DR
- 20 ต.ค. Daytona ปิด Series B **$60M ที่ valuation $1B** โดย FirstMark เป็น lead — รวมเงินทั้งหมดที่ระดมได้ **$91M**
- Angel/investor list อ่านเหมือน who's who ของ agent builder: **Patrick Collison, Tobi Lütke, Aravind Srinivas, Olivier Pomel, Eric Yuan, Brendan Foody, Adam D'Angelo** + Pace, Upfront, E2VC, Samsung Next, Qualcomm Ventures
- Revenue run rate **โตขึ้น 25 เท่า ระหว่างมกราคม→กันยายน** — customer list: Anthropic, OpenAI, NVIDIA, Cursor, Cognition, Meta, Cohere, Postman
- CEO Ivan Burazin บอก Fortune: "Companies are going to manage thousands of digital employees, and each one needs a safe place to fail" — Daytona ขยาย product จาก sandbox เดี่ยว ๆ ไปเป็น "agent cloud" ครบ stack: Linux/Windows/macOS, pause/resume, dynamic scaling

## เกิดอะไรขึ้น

วันอังคาร 20 ต.ค. Daytona ประกาศ Series B $60M ที่ unicorn valuation $1B โดย FirstMark เป็น lead — เป็น firm เดียวกับที่นำ Series A $24M เมื่อกุมภาพันธ์ แปลว่าภายในแปดเดือน valuation ขยับจาก unknown (Series A ไม่เปิดตัวเลข) ไปแตะ $1B. ที่เด่นกว่า valuation คือ **list ของคนที่เข้ามาเขียนเช็ค**: Patrick Collison (Stripe CEO), Tobi Lütke (Shopify CEO), Aravind Srinivas (Perplexity CEO), Olivier Pomel (Datadog CEO), Eric Yuan (Zoom founder), Brendan Foody (Mercor CEO), Adam D'Angelo (Quora + OpenAI board). ไม่ใช่ founder angel เบา ๆ — คือคนที่ sell "agent-powered product" ให้ลูกค้าเอง และกำลัง bet ว่าตัว runtime ที่ agent รันอยู่ จะเป็น infrastructure layer ถัดไปของ cloud

Daytona ไม่ใช่ sandbox เจ้าใหม่ — product เริ่มจาก isolated environment ที่ให้ coding agent รัน shell command, build, test, revert — เหมือน SPACE ของ Perplexity หรือ E2B แต่ cross-OS (Linux/Windows/macOS) และมี **pause/resume** ของ VM state เพื่อให้ agent ลอง approach หลายตัวได้โดยไม่สูญ context. ตัวเลขที่สำคัญกว่า funding คือ **revenue run rate โตขึ้น 25 เท่าใน 8 เดือน** — จาก internal number ที่ไม่เปิด แต่ growth curve ขนาดนั้น ใน SaaS metrics ปกติเรียกว่า "ติดจรวด". และ customer list บอกจุด: Anthropic, OpenAI, NVIDIA, Cursor, Cognition, Meta, Cohere, Postman — คือ **lab, model vendor, agent product, และ dev tool ที่ build agent ของตัวเอง ล้วนเลือก Daytona เป็น runtime** แทนที่จะ build เอง

ประเด็นที่ Burazin ย้ำกับ Fortune คือ positioning ของ Daytona ไม่ใช่ sandbox แต่คือ **"agent cloud"** — เขาเทียบตรง ๆ ว่า "Companies are going to manage thousands of digital employees, and each one needs a safe place to fail." Series B นี้จะเอาเงินไป **ขยายจาก sandbox ไปเป็น compute layer เต็ม stack** — เพิ่ม compute auto-scaling, hiring ใน San Francisco, Croatia, Singapore. Pattern transfer ชัด: ถ้า human employee ต้องการ laptop + VPN + IAM + audit log → digital employee ต้องการ VM + network policy + credential vault + action log. Daytona กำลัง bet ว่าตัวมันเป็น "AWS ของ agent"

## ทำไมสำคัญ

Pattern สองสัปดาห์ที่ผ่านมาตรงกันเหลือเกิน — เมื่อ 15 ต.ค. Perplexity เปิด SPACE sandbox แบบ Apache 2.0 พร้อม 3 cloud partner (CoreWeave, Akamai, Crusoe) อ้างว่า sandbox จะกลายเป็น commodity. วันนี้ Daytona ปิด $60M ที่ $1B เพื่อ **สร้าง managed sandbox ที่เสียเงินใช้** และคนที่เข้ามา back คือ CEO ของ Stripe, Shopify, Datadog, Zoom, Perplexity, Mercor. Reading นี้คือ: open-source commodity ก็เรื่องหนึ่ง, แต่ **enterprise ต้อง managed cloud ที่มี SLA ไม่ใช่ repo ให้ fork** และนั่นคือ layer ที่ยังขายได้. Daytona กับ Modal กับ E2B อยู่ในลีกเดียวกัน — "Firecracker-as-a-service ที่ enterprise จ่ายได้" — ตอนนี้ Daytona ขึ้นก่อน

Signal ที่น่าสนใจกว่าคือ **มันเป็นดีลที่ทั้ง CEO ของ "มี agent product" (Perplexity, Mercor) และ CEO ของ "มี SaaS ที่ agent จะกิน" (Shopify, Stripe, Datadog, Zoom) ร่วมเขียนเช็ค** — เป็น hedge ว่าไม่ว่าใครชนะใน agent product layer runtime ชั้นล่างต้องมี. และ Datadog ของ Pomel ลงเงินใน Daytona แสดงว่า observability vendor เริ่มมองว่า agent runtime คือ data source ถัดไปของตัวเอง (Datadog เคย play เดียวกันตอน Kubernetes เป็น default). นี่คือ playbook ของ Snowflake / Datadog ยุคแรก — ไม่ใช่ product play แต่คือ **category creation ที่ cross-sell ไปทุก buyer**

## มุม AI Agent Platform

สำหรับ **Builders**: ถ้าคุณกำลัง build agent product (coding agent, research agent, SDR agent) การ build sandbox เองช้าและเสียเงิน — Daytona + E2B + Modal จะมี SDK ที่พอดีกับ framework (LangGraph, CrewAI, OpenAI Agents SDK, Claude Agent SDK) แล้ว. แปลว่าเวลาที่เคยใช้กับ ops ควรใช้กับ **tool catalog, policy engine, agent-level observability** แทน. สำหรับ **Users / Business** ที่ deploy agent ใน workflow: ถาม vendor ตรง ๆ ว่า "agent รันบน runtime อะไร" — ถ้าตอบว่า "shared Docker" หรือ "serverless function" ให้ follow up ว่า isolation level กับ credential handling. วันนี้ enterprise security ไม่ยอม cut corner ตรงจุดนี้แล้ว. สำหรับ **Ecosystem**: cloud hyperscaler (AWS Bedrock AgentCore, Azure AI Foundry, GCP Vertex) จะเร่งปล่อย managed sandbox ของตัวเอง — competitive squeeze กำลังจะมา. Daytona + Modal + E2B มี **window 12–18 เดือน** ที่จะ lock-in developer mind-share ก่อน hyperscaler bundle sandbox เข้ากับ model + billing

## Sources
- [Daytona hits $1B valuation with $60M Series B for AI agent cloud (Tech.eu)](https://tech.eu/2026/10/20/daytona-hits-1b-valuation-with-60m-series-b-for-ai-agent-cloud)
- [Exclusive: Daytona, a startup building the 'agentic cloud,' valued at $1 billion (Yahoo Finance)](https://uk.finance.yahoo.com/news/exclusive-daytona-startup-building-agentic-120000625.html)
- [Daytona raises $24M Series A to build agent-native compute infrastructure (Tech.eu, Feb 2026)](https://tech.eu/2026/02/06/daytona-raises-24m-series-a-to-build-agent-native-compute-infrastructure/)

---

## Audio script
วันนี้มีข่าวใหญ่ที่คนทำ agent ควรรู้ — Daytona บริษัท sandbox สำหรับ AI agent ปิดรอบ Series B หกสิบล้านดอลลาร์ที่ valuation พันล้าน แปลว่าเป็น unicorn แล้วภายในแปดเดือนจาก Series A ที่ยี่สิบสี่ล้าน. FirstMark เป็น lead แต่ที่น่าสนใจกว่าคือ list ของ angel — Patrick Collison แห่ง Stripe, Tobi Lütke แห่ง Shopify, Aravind Srinivas แห่ง Perplexity, Olivier Pomel แห่ง Datadog, Eric Yuan แห่ง Zoom. ไม่ใช่คนทั่วไป คือ CEO ที่ขาย product ให้ลูกค้าเอง และกำลัง bet ว่า agent runtime คือ infrastructure layer ถัดไป. revenue run rate ของ Daytona โตยี่สิบห้าเท่าใน 8 เดือน ลูกค้ามี Anthropic, OpenAI, NVIDIA, Cursor, Cognition, Meta, Cohere, Postman. CEO บอกว่า "บริษัทกำลังจะต้อง manage digital employee เป็นพัน ๆ ตัว และแต่ละตัวต้องมีที่ให้มันล้มเหลวได้อย่างปลอดภัย" — คือ positioning ว่า Daytona ไม่ใช่ sandbox แต่คือ agent cloud. บทเรียนคือ ถ้าสร้าง agent อยู่ อย่าสร้าง sandbox เอง — layer นี้มี unicorn เสิร์ฟแล้ว เวลาที่เคยใช้กับ ops เอาไปใช้กับ tool catalog, policy, observability จะคุ้มกว่า.
