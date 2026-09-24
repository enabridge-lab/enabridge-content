---
date: 2026-09-25
slug: 26-09-25-0615-02-amazon-seller-central-claude-bedrock
topic: use-case
sources: 4
reading_time_min: 4
image_prompt: |
  An oversized Amazon warehouse aisle at night, shelves receding into the vanishing
  point. A translucent glowing robotic assistant (silhouette only, no face) reaches
  through Seller Central dashboard windows to reprice a product; three neon numbers
  hover above the scene: "90% SELLERS ALREADY USE AI", "24/7 AUTOMATION",
  "12 MONTHS FREE". A small Claude logo and Amazon Bedrock badge float beside the
  robot. Editorial isometric cinematic style, deep navy plus Amazon-orange accent,
  1:1 aspect, no real human faces.
image: images/26-09-25-0615-02-amazon-seller-central-claude-bedrock.png
---

# Amazon เปิด Seller Central APIs ให้ Claude/Quick เรียก — first-party marketplace ยักษ์ยอมรับต่อสาธารณะว่า 90% ของ seller ใช้ AI นอกอยู่แล้ว

## TL;DR
- **23 ก.ย. ที่ Amazon Accelerate** — Amazon เปิด beta ให้ external AI agent (Anthropic Claude + Amazon Quick) เรียก Seller Central APIs โดยตรง — inventory, pricing, listings, analytics — ผ่าน Bedrock (Nova + Claude)
- Amazon **ยอมรับต่อสาธารณะ**: ~90% ของ seller ใช้ external AI tool อยู่แล้วเพื่อรัน operations = เปิด API ตามหลัง behavior; แถม free Quick Plus subscription **12 เดือน** ถึง 31 ธ.ค. 2026 ให้ทุก account
- **Signal:** persistent memory ของ seller (pricing pattern, inventory cycle, growth goal) **ตามข้าม tools** (Seller Central ↔ Quick ↔ Claude) = pattern architecture ใหม่ที่ context/memory เป็น shared layer ไม่ใช่ per-app

## เกิดอะไรขึ้น

23 กันยายน 2026 ที่ Amazon Accelerate — งาน annual conference สำหรับ seller — Amazon ประกาศเปิด **Seller Central APIs ให้ external AI agent เรียกโดยตรง** พร้อม launch US beta ของ **Selling Partner plugin** ที่ทำงานผ่าน Anthropic Claude และ Amazon Quick assistant. อยู่บน Bedrock ที่ combine **Amazon Nova + Claude models** และ Amazon ยืนยันว่า data ของ seller **ไม่ออกจาก infrastructure ของ Amazon**

สิ่งที่ seller ทำได้จากพลิกเกินคือชุดใหญ่: จัดการ **inventory, ปรับราคาแบบ dynamic, สร้าง/แก้ listing, ดู analytics, automate routine 24/7** — โดยไม่ต้องเปิด Seller Central UI. Amazon ใส่ carrot ให้ **ทุก primary account holder = ได้ Quick Plus subscription ฟรี 12 เดือน จนถึง 31 ธ.ค. 2026** = ~$100+ value ต่อ account (พันล้าน dollar exposure ถ้าคำนวณตาม active seller base ~2M)

ที่สำคัญกว่าตัว API คือ **persistent memory**: Seller Assistant จำ pattern การตั้งราคา, inventory cycle, growth goal ของแต่ละ seller และ **memory ตามข้าม tool** (Seller Central UI ↔ Amazon Quick ↔ Anthropic Claude). ยิ่งไปกว่านั้น Amazon เผยตัวเลขที่หลายคนมองข้าม: **ประมาณ 90% ของ seller ใช้ external AI tool อยู่แล้ว** เพื่อจัดการธุรกิจ — Amazon เปิด API ก็ **ตามหลังพฤติกรรม** ไม่ได้นำ

## ทำไมสำคัญ

ประเด็นแรกที่คนพลาด: Amazon **เก็บ storefront ปิดต่อไป** (ผู้ซื้อยัง shop ผ่าน amazon.com UI เดิม) แต่**เปิด backend ทั้งชุดให้ agent เข้ามาบริหาร**. API Evangelist บันทึกว่า pattern นี้ = "closed frontend, open backend" คือ playbook ใหม่ของ marketplace ยักษ์ในยุค agent — control experience ของลูกค้าปลายทาง แต่ delegate business operation ของ seller ให้ agent ทำ. เหตุผลก็คือ marketplace ต้องการ seller performance สูงขึ้น (ราคาเหมาะสม, inventory ตรง, listing quality) แต่ไม่อยาก risk experience บนหน้าลูกค้า

ประเด็นที่สอง: **Amazon เลือก Anthropic Claude** เป็น partner เปิดตัว = Anthropic นั่ง delivery layer ของ marketplace ที่ทำ GMV >$700B ต่อปี (2025 numbers). Combine กับที่ Salesforce เปิด Claudeforce สัปดาห์เดียวก่อนหน้า = Anthropic วิ่งสะสม "distribution surface" ที่ OpenAI ยังไม่มี — surface ของ enterprise workflow จริงที่ agent เรียกได้

ประเด็นที่สาม (ที่ปฏิวัติที่สุด): **persistent memory ข้าม tool**. เดิม memory ของ AI ผูกกับแอปเดียว — ChatGPT รู้จักคุณใน ChatGPT, Claude รู้จักคุณใน Claude. Amazon Seller Assistant memory **ตามคุณข้าม product boundary** = pattern architecture ใหม่ที่ context เป็น shared plane, ไม่ใช่ locked-in feature ของแต่ละ vendor. ในระยะยาว = user จะเลือก agent ที่ **ให้ portable memory** เหนือ vendor lock-in

## มุม AI Agent Platform

**Builders** ที่กำลังสร้าง marketplace/e-commerce agent — Seller Central APIs เปิดให้ MCP-style tool call = แข่งกับ Claude/Quick ตรง ๆ ได้ (ถึงแม้ Amazon จะเปิดเฉพาะ 2 partner ก่อน). **Users/business** ที่ขายบน Amazon (SEA seller ที่ยิงไปตลาด US): 12 เดือน Quick Plus ฟรี = เริ่ม pilot 24/7 automation ทันที; workflow เดิมที่จ้าง VA (Filipina/Indian) ทำ inventory + pricing = โดน pressure ทันที. **Ecosystem** — Anthropic ยึด distribution ของ e-commerce marketplace ยักษ์; Shopify/eBay/Etsy ที่ยังไม่มี answer = ต้อง respond ใน 6 เดือน หรือ seller migrate ไปฝั่งที่ agent-native แล้ว

## Sources

- [Amazon opens its seller tools to outside AI agents, starting with Anthropic's Claude — GeekWire](https://www.geekwire.com/2026/amazon-opens-its-seller-tools-to-outside-ai-agents-starting-with-anthropics-claude/)
- [Amazon Opens Seller Tools to Outside AI Agents, Starts With Claude on Bedrock at Accelerate — AI Weekly](https://aiweekly.co/alerts/amazon-opens-seller-tools-to-outside-ai-agents-starts-with-claude-on-bedrock-at)
- [Amazon Brings Seller Assistant to Claude and Amazon Quick — Unite.AI](https://www.unite.ai/amazon-brings-seller-assistant-to-claude-and-amazon-quick/)
- [Amazon Opened Seller Central To Agents, And Kept The Storefront Closed — API Evangelist](https://apievangelist.com/2026/09/24/amazon-opened-seller-central-to-agents-and-kept-the-storefront-closed/)

---

## Audio script

Amazon เพิ่งประกาศเมื่อ 23 กันยา ที่งาน Amazon Accelerate ว่าเปิด Seller Central APIs ให้ external AI agent เรียกได้ตรง ๆ เริ่มจาก Anthropic Claude กับ Amazon Quick เอง ทำงานผ่าน Bedrock ที่ combine Amazon Nova กับ Claude. Seller สามารถให้ agent จัดการ inventory ปรับราคา สร้าง listing ดู analytics แบบ 24 7 โดยไม่ต้องเปิดหน้า Seller Central อีก แถม Amazon แจก Quick Plus ฟรี 12 เดือน ให้ทุก primary account ถึงสิ้นปี ตัวเลขที่น่าสนใจสุดจาก Amazon เองคือ ประมาณ 90 เปอร์เซ็นต์ของ seller ใช้ external AI tool อยู่แล้ว Amazon เปิด API ก็คือตามหลังพฤติกรรม สิ่งที่ปฏิวัติที่สุดคือ persistent memory ที่ตามผู้ใช้ข้าม tool ตั้งแต่ Seller Central Amazon Quick จนถึง Claude memory จำ pattern การตั้งราคา inventory cycle growth goal ของแต่ละ seller pattern นี้ใหม่หมด เพราะ memory เคยผูกกับแอปเดียวเสมอ ในระยะยาวจะเห็น user เลือก agent ที่ให้ portable memory มากกว่าที่ยึด vendor lock in ในมุม Enabridge นี่คือ signal ให้ marketplace ยักษ์อื่น Shopify eBay Etsy ต้อง respond ใน 6 เดือน ไม่งั้น seller ย้ายไปฝั่งที่ agent native แล้ว
