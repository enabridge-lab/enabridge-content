---
date: 2026-11-06
slug: walmart-agent-gateway-mcp-retail
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a bright Walmart-style store at
  night, lit from inside. A glowing arch above the entrance labeled
  "AGENT GATEWAY" lets small cube-shaped shopping agents walk in single
  file, each carrying an ID card marked "AGENT PROFILE". A sign above
  the arch reads "SPEAKS MCP". Behind a closed metal door next to it,
  a crossed-out Amazon-style arrow says "BLOCKED". A smaller stat tile
  reads "SPARKY + MCP" with another "NO CARD CAPTURE". Warm electric
  blue and sunny yellow palette, 1:1 aspect, no real human faces
  (silhouettes OK), high contrast so text stays readable at 200px.
image: images/26-11-09-0607-05-walmart-agent-gateway-mcp-retail.png
---

# Walmart เปิดประตูให้ AI agent — Agent Profiles, Gateway, และ MCP ทำให้ retail ที่ใหญ่ที่สุดในอเมริกาเป็น agent-friendly ตัวแรก

## TL;DR
- 21 ต.ค. Walmart ประกาศ 3 ชิ้น: **Agent Profiles** (ลูกค้าตั้ง agent ของตัวเองให้ซื้อแทน), **Walmart Agent Gateway** (route agent ผ่าน Sparky, Walmart AI assistant), และ **agent-specific terms of use** — rollout เริ่มพฤศจิกายน
- Gateway ใช้ **Model Context Protocol (MCP)** — protocol ที่ Anthropic open-source ปี 2024 เพื่อ connect AI assistant กับ data system
- Rules ที่ชัดเจน: agent ห้าม override intent, ห้ามเปลี่ยน payment method, ห้ามเก็บ card data ของลูกค้า — non-compliant agent ถูก block
- Context: **ตรงกันข้ามกับ Amazon** ที่เริ่ม block third-party agent ไม่ให้ซื้อแทนลูกค้า — Walmart เลือกเส้นทางเปิด
- Walmart มี integration conversational commerce กับ ChatGPT, Gemini, Meta Muse อยู่แล้ว

## เกิดอะไรขึ้น
21 ตุลาคม 2026 Walmart ประกาศ 3 ชิ้นที่รวมกันเป็นการเปิดบ้านให้ AI shopping agent ครั้งแรกใน retail ระดับใหญ่ของอเมริกา — และ rollout customer-facing เริ่มพฤศจิกายน ชิ้นแรกคือ **Agent Profiles** ให้ลูกค้าตั้ง "agent ของตัวเอง" ที่ซื้อของแทนบน Walmart.com และ Sam's Club เช่น ตั้ง spending cap, พื้นที่ delivery, preference อะไรเทียบได้/ไม่ได้ ชิ้นที่สองคือ **Walmart Agent Gateway** ซึ่งเป็น technical layer ที่ route request จาก external agent (ChatGPT, Comet, Gemini, Muse ฯลฯ) ผ่าน **Sparky** — AI assistant ของ Walmart เอง — ก่อนไปถึง catalog และ checkout

สิ่งที่น่าสนใจทาง technical คือ gateway ใช้ **Model Context Protocol (MCP)** เป็น standard ขับ ตั้งแต่ Anthropic open-source MCP เดือนพฤศจิกายน 2024 protocol นี้ค่อย ๆ กลายเป็น default ของ agent integration — ตอนนี้ MCP ถูก adopt โดย Anthropic, OpenAI (ChatGPT Apps), Google (Gemini CLI), GitHub (Copilot), และ Microsoft (Copilot Studio) และตอนนี้ Walmart agent gateway อย่างเป็นทางการ — เป็น proof ว่า MCP ไม่ใช่ dev protocol แต่เป็น commerce protocol จริง ๆ แล้ว

ชิ้นที่สามคือ **agent-specific terms of use** — agent ห้าม override user intent (ซื้อของที่ไม่ได้อยากได้), ห้ามเปลี่ยน payment method, และห้ามรับ card data ของลูกค้า — ซึ่งเป็น privacy + fraud protection สำคัญ non-compliant agent จะ ถูก block ที่ gateway ส่วน Walmart มี integration อยู่แล้วกับ ChatGPT, Gemini, และ Meta Muse — Agent Profile + Gateway ยืนยันและทำให้ relationship เหล่านี้เป็น programmatic

Context ที่สำคัญ: Walmart เดินเส้นตรงข้ามกับ **Amazon** — Amazon เริ่ม block third-party agent (Comet, Perplexity shopping) ที่พยายามซื้อของแทนลูกค้า และฟ้อง Perplexity (infamous Perplexity-Amazon case) — แต่ Ninth Circuit vacate preliminary injunction เดือน ส.ค. 2026 Walmart เลือก opposite move: ไม่เถียงกับ agent ecosystem แต่ building infrastructure เพื่อให้ agent เข้ามาแบบ governed

## ทำไมสำคัญ
สามเรื่อง หนึ่ง — **MCP กลายเป็น commerce protocol จริง ๆ** ตอนนี้ไม่ใช่แค่ dev tool ที่ Claude ใช้ connect database Walmart เป็น Fortune #1 retailer (revenue $650B+) ยอม commit MCP ใน customer-facing gateway บอกว่า MCP ได้ reach critical mass เป็น standard — Shopify, Target, Costco, Carrefour จะ follow เพราะไม่อยากถูก Amazon lock out แต่ก็ไม่อยากสร้าง gateway เอง

สอง — **สองเกม strategic** กำลังชนกันชัด: Amazon "walled garden" vs Walmart "governed open" คำถามคือ model ไหน win Amazon มี leverage มากกว่าในระยะสั้นเพราะเป็น largest online retailer ลูกค้าต้อง "กลับ" มาซื้อจาก Amazon ส่วน Walmart มี leverage ระยะยาวในฐาน physical store + grocery + pickup ที่ agent ไม่สามารถ bypass ได้ Walmart bet ว่าเมื่อ agent ecosystem โต Walmart ที่ "agent-friendly" จะได้ share จาก Amazon เพราะ agent ตัวใหม่เลือก Walmart first

สาม — **Framework agent policy** ที่ Walmart ปล่อย (ห้าม override intent / ห้ามเปลี่ยน payment / ห้ามเก็บ card) จะกลายเป็น template ของ retailer อื่น เพราะ regulator สหรัฐ (FTC) และสหภาพยุโรป (European Commission) จะต้องมีแนวทางภายใน 2027 ว่า agent ที่ซื้อของแทนคน under terms อะไร ถ้า Walmart ปล่อย template ก่อน regulator ตัว template นั้นจะ set anchor

## มุม AI Agent Platform
**Builders** — ถ้าคุณสร้าง agent ที่ซื้อของแทนลูกค้า (ChatGPT shopping, Perplexity, Gemini shopping, หรือ startup ของตัวเอง) MCP compliance + Walmart Agent Profile integration กลายเป็น table stakes ทันที — ลูกค้าอยากซื้อของจาก Walmart เป็นปกติ และถ้าคุณไม่ comply กับ agent gateway ลูกค้าก็จะเลือก agent ที่ comply รองรับ Walmart ไปใช้แทน

**Users / business** — Retailer ไทย (Central, CP, Big C, Makro) ควรเริ่มคิดเรื่อง agent-friendly infrastructure แล้ว ไม่ใช่รอให้ ChatGPT shopping เปิดในไทยก่อน timeline อย่างเร็วคือ 2027-28 preparation ทำได้ 3 step: (1) MCP server ของ product catalog, (2) policy ว่า agent ซื้อ/คืน/promo ได้แค่ไหน, (3) measurement framework ว่า sales จาก agent นับยังไง (เทียบ sales จาก organic search / affiliate) Walmart playbook เป็น reference ที่ใช้ได้

**Ecosystem** — Shopify อยู่ในตำแหน่งน่าสนใจ — Shopify Store Builder + Shopify Agents สามารถ ship MCP + Agent Gateway เป็น default สำหรับ merchants 2M+ ของตัวเองได้ภายใน 12 เดือน ถ้าเดินเกมเก่งก็กลายเป็น default agent surface ของ e-commerce นอก Amazon-Walmart duopoly การแข่งขันนี้ compress ให้ Shopify ต้องเลือกฝั่ง (agent-friendly default เร็ว) ไม่ใช่กลาง ๆ

## Sources
- [While Amazon blocks AI agents, Walmart rolls out the welcome mat (TechCrunch)](https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/)
- [Walmart sets the rules for AI shopping agents (Actu IA)](https://www.actuia.com/en/news/walmart-sets-the-rules-for-ai-shopping-agents/)
- [Walmart's agentic commerce vision: Practical, personalized, immersive (Constellation Research)](https://www.constellationr.com/blog-news/insights/walmarts-agentic-commerce-vision-practical-personalized-immersive-and-less)
- [Inside Walmart's AI Playbook: Stores, Sparky, and the Rise of Agentic Commerce (Wing VC)](https://www.wing.vc/content/inside-walmarts-ai-playbook-stores-sparky-and-the-rise-of-agentic-commerce)

---

## Audio script
Walmart ประกาศเมื่อวันที่ 21 ตุลาคม เปิดบ้านให้ AI shopping agent มาซื้อของแทนลูกค้าบน Walmart.com และ Sam's Club โดย rollout customer-facing เริ่มพฤศจิกายน ประกอบด้วย 3 ชิ้น หนึ่งคือ Agent Profiles ที่ให้ลูกค้าตั้ง agent ของตัวเองพร้อม spending cap และ preference สองคือ Walmart Agent Gateway ซึ่งเป็น technical layer ที่ route request จาก agent ภายนอก เช่น ChatGPT, Comet, Gemini, Meta Muse ผ่าน Sparky AI assistant ของ Walmart ก่อนถึง catalog และ checkout และสามคือ terms of use เฉพาะ agent ที่ห้าม override intent ลูกค้า ห้ามเปลี่ยน payment method และห้ามเก็บ card data สิ่งที่ technically สำคัญคือ Agent Gateway ใช้ Model Context Protocol หรือ MCP ซึ่ง Anthropic open-source ปี 2024 การที่ Walmart ที่เป็น Fortune #1 retailer commit MCP ใน customer-facing gateway เป็น proof ว่า MCP ไม่ใช่แค่ dev tool แต่เป็น commerce protocol จริง Walmart เดินทางตรงข้ามกับ Amazon ที่ block third-party agent และฟ้อง Perplexity เมื่อปี 2025 bet ของ Walmart คือ เมื่อ agent ecosystem โต retailer ที่ agent-friendly จะได้ share จาก Amazon เพราะ agent ตัวใหม่เลือก Walmart first สำหรับ retailer ไทยอย่าง Central, CP, Big C, Makro ควรเริ่มคิดเรื่อง MCP server ของ product catalog, policy ว่า agent ซื้อได้แค่ไหน และ measurement framework ว่า sales จาก agent นับอย่างไร timeline ที่ ChatGPT shopping จะเปิดในไทยคือ 2027-28 — Walmart playbook เป็น reference ที่ใช้ได้
