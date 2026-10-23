---
date: 2026-10-21
slug: walmart-agent-gateway-mcp
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration contrasting two retailers: on the left,
  a locked blue warehouse labeled "AMAZON" with a glowing red "NO AGENTS" shield
  blocking a line of small robot shoppers; on the right, a glowing yellow Walmart
  storefront with an open glass gateway stamped "MCP GATEWAY" letting the same
  robot shoppers walk in through a turnstile marked "APPROVED AGENTS". Three
  stacked numbers float above: "AGENT PROFILES", "SPENDING LIMITS", "NO CARD
  DETAILS". Deep navy, Walmart yellow and Amazon orange palette, strong contrast
  for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-24-0606-01-walmart-agent-gateway-mcp.png
---

# Walmart เปิด Agent Gateway (MCP) ให้ AI agent ซื้อของแทนลูกค้า — Amazon ปิด, Walmart เลือกเปิด

## TL;DR
- **21 ต.ค.** CEO Walmart John Furner ประกาศ **Agent Gateway** ที่งาน Masters of Scale Summit — เป็น **MCP server** ให้ "approved" AI agent search inventory + buy แทนลูกค้าทั้งใน Walmart และ Sam's Club
- **Agent Profiles** จะ launch ใน ~1 เดือน — ลูกค้าตั้ง spending limit ให้ auto-approve (เหมือน authorized user ของบัตรเครดิต) หรือ require approval ทุก transaction. **Agent ไม่ได้ card details**, เปลี่ยน payment method ไม่ได้
- Beta จำกัดเฉพาะ **companies + developers** ผ่าน Walmart Developer Portal; ไม่มี public date — contrast ชัดกับ **Amazon ที่ block third-party agent** จาก amazon.com
- Signal: retailer รายใหญ่ **ตัดสินใจคนละขั้วเกี่ยวกับ agent commerce** — Walmart bet ว่า agent-ready = traffic growth, Amazon bet ว่า agent = margin leak + attribution loss

## เกิดอะไรขึ้น

วันพุธที่ **21 ต.ค.** ที่ Masters of Scale Summit ที่ซานฟรานซิสโก, **John Furner** CEO Walmart US ประกาศ **Walmart Agent Gateway** — บริการ **MCP (Model Context Protocol)** server อย่างเป็นทางการที่ใช้ open standard ของ Anthropic ให้ AI agent (ของ OEM หรือ custom) ติดต่อ Walmart แบบ programmatic แทนที่จะต้อง "คลิกเว็บ" เหมือนมนุษย์. agent ยิง query ไปที่ gateway ขอ product, stock, checkout โดยตรง — ตัด front-end web scraping ทิ้ง

gateway ครอบคลุมทั้ง **Walmart.com** และ **Sam's Club**. ตัว gateway มีสามส่วน: (1) **Agent Gateway API** สำหรับ search/buy, (2) **Agent Profiles** ที่ลูกค้าตั้ง rule — "auto-approve ถ้า order ต่ำกว่า $X" หรือ "ต้อง approve ทุกครั้ง", (3) **ชุด 7 Agent Terms** ที่ developer ยอมรับก่อนเข้าใช้ — รวมถึง "no payment card details to agent", "cannot change payment method", และ **non-compliant agent จะถูก block อัตโนมัติ**

Agent Profiles ยังไม่ launch — Walmart บอก "ภายในประมาณ 1 เดือน". ตอนนี้ gateway เป็น beta จำกัดเฉพาะ **companies + developers** ที่ apply ผ่าน Walmart Developer Portal. ไม่มี public rollout date สำหรับผู้บริโภคทั่วไป. ตัวเลข deployment จริงยังไม่เปิด — Walmart ไม่ยืนยันว่า agent partner รายไหนบ้าง, จำนวน request ที่คาด, หรือ cut ของ commission (ถ้ามี). ที่ชัดคือ gateway ชี้ไป MCP เป็น protocol standard — ไม่สร้าง proprietary API

## ทำไมสำคัญ

จุดที่ต้องจับคือ **contrast กับ Amazon**. ตั้งแต่กลางปี 2026 Amazon ได้ block agent จาก OpenAI, Perplexity, Anthropic และรายอื่นจาก amazon.com — ตีความว่า agent = "traffic ที่หนีจาก Prime ecosystem + ทำให้ ad surface หด + ลูกค้าไม่เห็น recommendation ของ Amazon เอง". Walmart อ่านเกมคนละมุม — agent = **demand channel ใหม่ที่ Amazon ปิด แต่ Walmart เปิด**. ถ้า agent commerce โตเท่าที่ VC คาด (Gartner ประเมิน 20% ของ online transaction จะผ่าน agent ภายใน 2028), Walmart ชนะ traffic ที่ Amazon ไม่ยอมรับ

Pattern ที่กว้างกว่า: **MCP กลายเป็น "store door" ของอินเทอร์เน็ต**. Walmart ไม่สร้าง REST API ใหม่, ไม่สร้าง GraphQL ของตัวเอง — เลือก MCP ของ Anthropic (ตอนนี้อยู่ใต้ Linux Foundation's Agentic AI Foundation) เป็น default. นี่คือครั้งแรกที่ retailer ระดับ Fortune 1 **commit MCP เป็น commerce protocol** ไม่ใช่แค่ internal tool integration. ถ้า Target, Costco, Best Buy ตาม, MCP จะกลายเป็น **de facto standard ของ agent commerce** เหมือนที่ HTTPS คือ default ของ web commerce

สัญญาณต่อไปที่ต้องดู: **(1)** Amazon จะเปลี่ยนท่าทีไหมถ้า Walmart ได้ transaction volume จากเส้นทาง agent, **(2)** Walmart จะ monetize gateway ยังไง — commission per agent-transaction, developer fee, หรือเป็น loss leader เพื่อแย่ง market share จาก Amazon, **(3)** payment network (Visa, Mastercard, Stripe) จะปรับตัวยังไงกับ "agent-initiated transaction" — ซึ่ง Mastercard Agent Pay (เม.ย. 2026) และ Visa Intelligent Commerce ได้เริ่ม lay groundwork แล้ว

## มุม AI Agent Platform

สำหรับ **Builders** (ของ agent framework และ consumer AI apps): ถ้า agent คุณไม่พูด MCP ที่ compatible กับ Walmart Agent Gateway spec, คุณพลาด channel ของ retailer ที่ใหญ่ที่สุดในสหรัฐ. ที่สำคัญกว่าคือเลเยอร์ **agent identity** — Walmart จะ verify agent ผ่าน Developer Portal ก่อนอนุมัติ ซึ่งหมายความว่า agent ที่ไม่มี **verifiable identity + policy compliance history** จะเข้าไม่ได้ นี่คือเหตุผลว่าทำไม **1Password for Agents** (เปิดตัววันถัดมา) และ **ServiceNow AI Passport** กลายเป็น primitive สำคัญเลเยอร์หนึ่งแยกต่างหากจาก agent runtime เอง. สำหรับ **Users / Business** (เจ้าของแบรนด์ที่ขายผ่าน Walmart Marketplace): เตรียม product data + inventory feed ให้ agent อ่านได้ ไม่ใช่แค่ให้มนุษย์อ่าน — attribute เช่น size, material, compatibility ต้อง machine-structured, ถ้าไม่ agent จะ skip. สำหรับ **Ecosystem**: Walmart รอบนี้บอก e-commerce platform (Shopify, BigCommerce, Adobe Commerce) ให้เร่ง ship native MCP endpoint — ไม่ใช่แค่ "AI SEO plugin" ที่คุยกับ agent ผ่าน web scraping. Shopify ที่มี **Patrick Collison** + **Tobi Lütke** เป็น angel ใน Daytona (รอบ Series B $1B เมื่อสัปดาห์ก่อน) น่าจะเป็นรายแรกที่ขยับ

## Sources
- [Walmart opens an MCP gateway for AI shopping agents (DEV Community)](https://dev.to/mikefluff/walmart-opens-an-mcp-gateway-for-ai-shopping-agents-1eno)
- [Walmart Debuts Agent Gateway MCP Server and Agent Profiles for Approved AI Shoppers (AI Weekly)](https://aiweekly.co/alerts/walmart-debuts-agent-gateway-mcp-server-and-agent-profiles-for-approved-ai)
- [While Amazon blocks AI agents, Walmart rolls out the welcome mat (daily.dev)](https://daily.dev/posts/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat-v11efhkr1)

---

## Audio script
วันพุธที่ 21 ตุลาคม John Furner ซีอีโอ Walmart US ประกาศ Agent Gateway ที่งาน Masters of Scale Summit ซานฟรานซิสโก — เป็น MCP server ของ Walmart ที่เปิดให้ AI agent ที่ approved แล้ว ค้น inventory และซื้อของแทนลูกค้าทั้งใน Walmart และ Sam's Club. ตัว gateway มีสามส่วน หนึ่งคือ API สำหรับ search และ buy สองคือ Agent Profiles ที่ลูกค้าจะตั้ง spending limit ให้ agent ซื้อแบบ auto-approve หรือต้อง approve ทุก transaction. สามคือชุด 7 Agent Terms ที่ developer ต้องยอมรับก่อนเข้าใช้ รวมถึงกฎว่า agent ไม่ได้ card details และเปลี่ยน payment method ไม่ได้. agent ที่ไม่ compliant จะโดน block อัตโนมัติ. ที่น่าสนใจที่สุดคือ Walmart เลือกคนละขั้วกับ Amazon — Amazon block agent จาก amazon.com ตั้งแต่กลางปี เพราะมอง agent เป็น traffic หนีจาก Prime ecosystem. Walmart มอง agent เป็น demand channel ใหม่ที่ Amazon ไม่ยอมรับ ถ้า agent commerce โตเท่าที่ Gartner คาด 20% ของ online transaction จะผ่าน agent ภายใน 2028, Walmart ชนะ. ที่สำคัญกว่าคือ Walmart เลือก MCP ของ Anthropic เป็น protocol — ไม่ build REST API ของตัวเอง นี่คือครั้งแรกที่ retailer ระดับ Fortune 1 commit MCP เป็น commerce protocol. ถ้า Target, Costco, Best Buy ตาม MCP จะกลายเป็น de facto standard ของ agent commerce เหมือนที่ HTTPS คือ default ของ web commerce. สำหรับ builder — ถ้า agent คุณไม่พูด MCP, พลาด channel ของ retailer รายใหญ่ที่สุดในสหรัฐ และ agent identity กลายเป็น primitive แยกเลเยอร์ที่ Walmart, 1Password, ServiceNow เริ่มสร้างพร้อมกัน
