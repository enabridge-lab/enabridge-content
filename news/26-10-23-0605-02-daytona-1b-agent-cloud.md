---
date: 2026-10-20
slug: daytona-1b-agent-cloud
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a floating cloud platform shaped like a
  modular workshop; inside, dozens of tiny glowing sandbox cubes line up, each
  cube labeled by OS — "LINUX", "WINDOWS", "MACOS", "GPU". A tiny agent silhouette
  works alone inside each cube. Above the platform three stacked numbers glow:
  "$1B VALUATION", "25x REVENUE", "$60M SERIES B". A ribbon labeled "AGENT
  EXECUTION CLOUD" curls underneath the platform. Deep teal and warm orange
  palette, high contrast for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-23-0605-02-daytona-1b-agent-cloud.png
---

# Daytona แตะ $1B — "agent execution cloud" ที่ hyperscaler ไม่อยากทำ, Patrick Collison กับ Tobi Lütke ลงเงินด้วย

## TL;DR
- **20 ต.ค.** Daytona ประกาศ **Series B $60 ล้าน** นำโดย **FirstMark**, มูลค่าบริษัท **$1,000 ล้าน** — รวมทุนที่ระดมได้ทั้งหมด $91 ล้าน. บริษัทวาง positioning เป็น **"Agent Execution Cloud"** คือ cloud ที่ออกแบบมาเฉพาะสำหรับรัน AI agent, ไม่ใช่ containerize แอป
- **Investor mix บอกเรื่อง**: Qualcomm Ventures, Samsung Next, Okta Ventures เข้าร่วม + **Patrick Collison (Stripe) กับ Tobi Lütke (Shopify)** เป็น angel. Fortune รายงานว่า **~$50 ล้านมาจาก existing investor** — มี conviction สูงต่อ thesis
- **Product**: sandbox รัน Linux, Windows, macOS, GPU workload บน platform เดียว. ลูกค้าที่อ้าง (unverified): Anthropic, OpenAI, Meta, Cohere
- **Growth**: บริษัทบอก **revenue run rate โต 25 เท่า ตั้งแต่มกราคม** จาก base ที่ไม่เปิดเผย. Pivot จาก open-source dev environment manager (ก่อตั้ง 2023) → agent infra ปลายปี 2025
- **Context**: มา 2 วันก่อน Google Agent Compute Engine ที่ให้ microVM-per-agent เหมือนกัน — Daytona กำลัง bet ว่าตลาดต้องการ **"Switzerland ของ agent runtime"** ที่ cross-cloud, ไม่ bind เข้า hyperscaler ใครคนเดียว

## เกิดอะไรขึ้น

วันจันทร์ที่ **20 ต.ค.** Fortune, TechCrunch และ pulse2 รายงานการระดมทุนรอบ Series B ของ **Daytona** — บริษัทจากซานฟรานซิสโกที่เรียกตัวเองว่า **"Agent Execution Cloud"**. รอบนี้ $60 ล้าน, มูลค่าบริษัทแตะ **$1,000 ล้าน** (unicorn status), นำโดย **FirstMark**. Investor list น่าสนใจเพราะมันผสม strategic + angel + repeat: **Qualcomm Ventures** (ชิป edge), **Samsung Next** (consumer device), **Okta Ventures** (identity) ร่วม round, บวก angel ระดับ **Patrick Collison (Stripe)** กับ **Tobi Lütke (Shopify)** — Fortune ชี้ว่า **ประมาณ $50 ล้านมาจาก existing investor** ที่ follow-on. การที่ existing investor กินส่วนใหญ่ของรอบที่ valuation 10 หลัก = conviction signal ที่หนักกว่า new-money markup

Daytona เริ่มในปี 2023 เป็น **open-source dev environment manager** — ของประเภทที่คู่แข่ง GitHub Codespaces หรือ Gitpod. ปลายปี 2025 บริษัท pivot ไปที่ agent infrastructure เต็มตัว. ตอนนี้ core product คือ **sandbox-as-a-service** ที่รัน Linux, Windows, macOS, และ GPU workload **บน platform เดียว** — agent 1 ตัวเรียก sandbox 1 ตัว, มี computer+browser+storage ของตัวเอง. บริษัทอ้าง **revenue run rate โต 25 เท่า ตั้งแต่มกราคม 2026** (base ไม่เปิดเผย — ต้องระวังการตีความ, เพราะ 25x จาก $100K ARR ≠ 25x จาก $1M). รายชื่อลูกค้าที่อ้างใน blog post ของบริษัท: **Anthropic, OpenAI** (ไม่ verified จาก third party); coverage อื่นระบุ **Meta, Cohere** ด้วย

Timing ของรอบนี้สะกิดใจมาก: มาสองวันก่อน **Google Agent Compute Engine** (22 ต.ค.) ที่ให้ microVM-per-agent บน Google Cloud. AWS **Bedrock AgentCore** ก็มีของประเภทเดียวกัน. hyperscaler สองเจ้าใหญ่สุดกำลังทำสิ่งที่ Daytona ทำอยู่ — คำถามคือ **Daytona มี thesis อะไรที่จะไม่โดนบด**

## ทำไมสำคัญ

Thesis ของ Daytona ที่น่าจะทำให้ FirstMark กด $60M คือ **"neutrality คือ moat"**. Hyperscaler แต่ละเจ้าจะพยายามล็อก agent runtime เข้า identity + registry + governance stack ของตัวเอง (Google เพิ่งขยาย Agent Gateway/Registry/Identity ไปที่ ACE/Cloud Run/GKE เมื่อวาน) — บริษัทที่สร้าง agent ที่ **ต้องรันบน cloud หลายเจ้า** (เพราะลูกค้าของเขาใช้ cloud ต่างกัน, หรือเพราะ cost arbitrage, หรือเพราะ compliance ของแต่ละ region) จะอยากมี **execution layer ที่ไม่ bind เข้าใครคนเดียว**. Daytona bet ว่าตลาดจะต้องการ "Switzerland ของ agent runtime" ขนาดใหญ่พอให้มี unicorn อยู่ได้ — เหมือน Vercel/Netlify ที่อยู่ได้ท่ามกลาง AWS/GCP/Azure

ส่วน investor mix เอง — Qualcomm (edge/mobile silicon), Samsung Next (consumer device), Okta (identity) — ชี้ว่า Daytona กำลังวาง roadmap ที่ไม่ใช่แค่ "data center sandbox" แต่ **ขยายไป edge + consumer device + enterprise identity**. ถ้า agent ต้องรันบน device ของลูกค้าในอนาคต (เช่น agent บน smartphone ที่จับข้อมูลเฉพาะเครื่อง), **Qualcomm + Samsung** คือ gateway ไปที่นั่น. ถ้า agent ต้องแลก identity ข้าม enterprise, **Okta** คือ identity plane. การเลือก investor แบบนี้ **ไม่ใช่ random** — มันเป็น signal ว่า Daytona วาง bet ว่า agent runtime จะไม่อยู่ใน data center อย่างเดียว

ที่ต้องระวัง: **25x growth** จาก base ไม่เปิดเผย คือตัวเลขที่ต้องขีดเส้นใต้ — ไม่ใช่ลวงโฆษณา แต่ unknown base. และ **lock-in** ของ hyperscaler agent runtime (Google Agent Substrate กับ AWS AgentCore) ที่ปล่อยออกมาเดือนนี้ จะทดสอบ thesis "neutrality ชนะ" ของ Daytona ภายใน 12-18 เดือน

## มุม AI Agent Platform

**Builder**: ถ้าคุณสร้าง agent framework หรือ orchestration product, Daytona เป็น runtime option ที่ **ไม่ bind คุณเข้า hyperscaler ใครคนเดียว** — มีค่าถ้าลูกค้าคุณต้อง deploy cross-cloud. API surface ของ Daytona ตอนนี้ยังไม่ใหญ่เท่า Google Agent Substrate หรือ AgentCore — เป็นข้อเสียชั่วคราว, แต่เป็น trade-off กับ portability

**User / business**: compliance team ที่กลัว cloud lock-in จะเริ่มมอง "agent runtime layer ที่ portable" เป็นส่วนหนึ่งของ risk mitigation — เหมือนที่หลายบริษัทเลือก Kubernetes แทน hyperscaler-specific serverless เมื่อสิบปีที่แล้ว. การเลือก Daytona vs ACE/AgentCore จะเริ่มเป็นคำถาม architecture ที่ CTO ต้องตอบ ไม่ใช่แค่ dev tool preference

**Ecosystem**: unicorn-level funding ของ agent infra category เพิ่งขึ้นเป็น **4+ รายในไตรมาสเดียว** (Daytona, Town, Arena, Nous Research). pattern ชัด: VC เชื่อว่า agent stack ไม่ใช่ feature ของ cloud ใหญ่, มี category ของตัวเองพอสร้าง unicorn ได้. ที่ควรจับตา: **Cloudflare + Fly.io + Replit** จะ pivot เข้า agent runtime positioning ภายในปีนี้แน่

## Sources
- [Fortune: Daytona valued at $1 billion in latest funding round](https://fortune.com/2026/10/20/daytona-startup-building-the-agentic-cloud-valued-at-1-billion-in-latest-funding-round/)
- [Daytona Blog: Daytona Raises $60M Series B to Build the Agent Cloud](https://www.daytona.io/dotfiles/daytona-raises-60m-series-b-to-build-the-agent-cloud)
- [Pulse 2.0: Daytona Raises $60 Million Series B At $1 Billion Valuation](https://pulse2.com/daytona-raises-60-million-series-b-at-1-billion-valuation-to-build-agent-cloud-infrastructure/)

---

## Audio script
วันจันทร์ Daytona บริษัทจากซานฟรานซิสโกประกาศ Series B 60 ล้านเหรียญ มูลค่าบริษัท 1 พันล้าน นำโดย FirstMark บริษัทเรียกตัวเองว่า Agent Execution Cloud คือ cloud ที่ออกแบบมาเฉพาะสำหรับรัน AI agent ไม่ใช่ containerize แอปทั่วไป sandbox ของมันรัน Linux Windows macOS กับ GPU workload บน platform เดียว ลูกค้าที่อ้างแบบ unverified คือ Anthropic OpenAI Meta Cohere บริษัทบอกว่า revenue run rate โต 25 เท่าตั้งแต่มกราคม จากฐานที่ไม่เปิดเผย investor list น่าสนใจเพราะมี Qualcomm Samsung Next Okta บวก Patrick Collison จาก Stripe กับ Tobi Lütke จาก Shopify เป็น angel Fortune ระบุว่า 50 ล้านมาจาก existing investor ที่ follow-on ตีความได้ว่า conviction signal หนักกว่า new money markup ที่น่าสนใจคือ timing — มาก่อน Google Agent Compute Engine 2 วัน AWS ก็มี Bedrock AgentCore อยู่แล้ว คำถามคือ Daytona มี thesis อะไรที่ไม่โดนบด คำตอบน่าจะเป็น "neutrality คือ moat" บริษัทที่ build agent ที่ต้องรันบน cloud หลายเจ้าจะอยากมี execution layer ที่ไม่ bind เข้าใครคนเดียว เหมือน Vercel Netlify ที่อยู่ได้ท่ามกลาง AWS GCP Azure investor mix ที่มี Qualcomm Samsung Okta ยังชี้ว่า Daytona วางเพลงให้ agent runtime ขยายไป edge consumer device identity ไม่ได้อยู่แค่ data center ครับ
