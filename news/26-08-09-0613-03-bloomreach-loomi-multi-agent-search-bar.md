---
date: 2026-08-08
slug: bloomreach-loomi-multi-agent-search-bar
topic: use-case
reading_time_min: 3
sources: 3
image_prompt: |
  A single glowing search bar in the center of a minimalist e-commerce page,
  splitting into three colorful pipelines below it: one to a product grid, one
  to a chat-shopping guide, one to an order-support ticket. Big text overlays
  read "1,400+ BRANDS" and "AMERICAN EAGLE • PANDORA • SONEPAR" and "ONE
  ENTRY POINT". Editorial isometric, warm coral and deep teal palette, high
  contrast for 200px thumbnail readability, 1:1 aspect, no real human faces.
image: images/26-08-09-0613-03-bloomreach-loomi-multi-agent-search-bar.png
---

# Bloomreach เปลี่ยน search bar เป็น "หน้าประตูเดียว" — American Eagle, Pandora ใช้จริงแล้ว

## TL;DR
- Bloomreach ปล่อย "Ask Me Anything" ใน Loomi conversational agent วันที่ 5 สิงหาคม — search bar เดียวรับได้ทั้ง keyword, conversational shopping question, customer service
- ใช้จริงแล้วโดยแบรนด์ในกลุ่ม 1,400+ customer ของ Bloomreach — American Eagle, Sonepar, Pandora นำร่อง
- Signal ของ pattern ใหม่: multi-agent orchestration ที่ shopper ไม่ต้องรู้ว่ากำลังคุยกับ agent ไหน

## เกิดอะไรขึ้น
Bloomreach — vendor ecommerce personalization ที่มี customer 1,400+ ราย — เปิดตัว "Ask Me Anything" experience วันที่ 5 สิงหาคม โดยใช้ agentic personalization platform Loomi เป็น orchestration layer ที่รับ input จาก search bar เดียว. Shopper พิมพ์ keyword ปกติ, ถาม shopping question ยาว ๆ, หรือกดถามเรื่อง order/return — ทั้งหมดเข้ามาที่ search bar เดียวกัน แล้ว Loomi routes ไปยัง agent ที่เหมาะ.

Architecture ที่ Bloomreach โชว์คือ Loomi conversational agent ทำหน้าที่ recognize intent แล้วส่งต่อ: keyword search → merchandising engine เดิม (fast lookup), shopping question เชิงสำรวจ → generative agent, order/return question → integrations กับ customer service agent ของ third-party. หน้าตาสำหรับ shopper ยังเป็น search bar เดิม แต่ backend เป็น multi-agent system ที่ทำงานประสานกัน. American Eagle, Sonepar (industrial distributor), Pandora อยู่ใน early rollout batch.

การตัดสินใจนี้ตอบโจทย์เดียวกับที่ Amazon, Walmart, และ Shopify เผชิญมาปีที่ผ่านมา: shopper ตอนนี้อยาก search แบบ conversational เหมือน ChatGPT แต่ยังต้องการ speed ของ keyword search แบบเดิมสำหรับ product ที่รู้ว่าอยากได้. Solution ของ Bloomreach คือไม่ต้องเลือก — ให้ agent เป็นคน route ให้ transparent สำหรับ shopper.

## ทำไมสำคัญ
นี่คือ example ที่ชัดของ pattern ที่หลายคนพูดถึงว่า "multi-agent orchestration" แต่ยังไม่มี production case ชัด ๆ. Loomi ไม่ใช่ single LLM ตอบทุกอย่าง — เป็น router ที่รู้จัก tool ของแต่ละ downstream agent แล้วเลือกใช้ ให้ latency เร็วเมื่อจำเป็น (keyword lookup) และ quality สูงเมื่อ user ต้องการคำแนะนำ (generative agent). Pattern นี้เดียวกับที่ Anthropic โชว์ใน "orchestrator-worker" design pattern และ Google ใน Agent Development Kit — แต่ Bloomreach ทำใน production กับแบรนด์ scale จริงแล้ว.

Signal ทางการค้าคือ Bloomreach ผลักเรื่องนี้เป็น differentiator ต่อ Salesforce Commerce, Adobe Commerce, และ Shopify. Search bar เป็น real estate ที่มี intent สูงสุดในทุก ecommerce site — ใครควบคุมได้แปลว่าเป็น entry point ของทุก conversion. Bloomreach โชว์ว่า upgrade layer นี้ให้เป็น multi-agent ไม่ต้อง rebuild หน้าเว็บ ไม่ต้อง retrain team merchandising, ไม่ต้องเลือกระหว่าง speed กับ intelligence. เรื่อง revenue impact ยังไม่มี figure ที่ third party ยืนยัน — Bloomreach ยังไม่เปิดเผยตัวเลข lift จาก AMA experience เมื่อเทียบกับ baseline.

## มุม AI Agent Platform
สำหรับ **builders** ที่ทำ vertical agent (customer service, product recommendation, order management): moment ที่ต้องคิดว่าจะเสียบเข้า orchestrator ของ vendor อย่าง Bloomreach ได้ยังไง — เพราะ shopper จะไม่กด "chat with Zendesk" อีกต่อไป แต่พิมพ์ที่ search bar ของแบรนด์. API contract ต้อง clean, latency ต้องต่ำ, และ tool description ต้องละเอียดพอให้ router agent เลือกใช้ถูก. สำหรับ **users / business**: ecommerce brand ที่ยังใช้ search + chat + customer service เป็น silo แยก จะเจอ competitor ที่รวมทุกอย่างเข้า entry point เดียว — pilot ตัวเองว่า multi-agent router pattern นี้เพิ่ม conversion หรือลด support ticket ได้จริงไหม. สำหรับ **ecosystem**: pattern "orchestrator + specialized agents" กำลัง mature จาก demo ไป production — vendor commerce platform อื่น ๆ (Salesforce Agentforce, Adobe AEP, Shopify) จะต้อง ship คล้าย ๆ กันในไตรมาสหน้า.

## Sources
- [Bloomreach Launches Multi-Agent "Ask Me Anything" Capability Powered by Loomi | BusinessWire](https://www.businesswire.com/news/home/20260805530145/en/Bloomreach-Launches-Multi-Agent-Ask-Me-Anything-Capability-Powered-by-Loomi-Transforming-the-Search-Bar-Into-a-Single-Entry-Point-for-Shoppers)
- [Bloomreach Unveils Ask Me Anything AI Shopping Experience | Martechvibe](https://martechvibe.com/article/bloomreach-unveils-ask-me-anything-ai-shopping-experience/)
- [Bloomreach Launches Ask Me Anything Capability | DestinationCRM](https://www.destinationcrm.com/Articles/CRM-News/CRM-Across-the-Wire/Bloomreach-Launches-Ask-Me-Anything-Capability-176024.aspx)

---

## Audio script
เรื่องต่อไปเป็น business use case ที่น่าสนใจ. Bloomreach เป็น vendor ecommerce ที่มี customer พันสี่ร้อยแบรนด์ ปล่อยฟีเจอร์ใหม่ชื่อ Ask Me Anything เมื่อวันที่ห้าสิงหา. เรื่องคือแทนที่จะมี search bar สำหรับหาสินค้า chat bot สำหรับถาม แล้วก็ contact us ปุ่มสำหรับปัญหา order — ตอนนี้รวมเข้า search bar เดียวเลย. คุณพิมพ์ keyword หา product ก็ได้ ถามแบบยาว ๆ ว่าอยากได้เสื้อสไตล์ไหนก็ได้ หรือถามว่า order เมื่อวานถึงไหนแล้วก็ได้. เบื้องหลังคือ agent ที่ชื่อ Loomi ทำหน้าที่ route intent ไปยัง agent ที่เหมาะ — keyword ไป search engine เดิม, คำถามยาวไป generative agent, เรื่อง order ไป customer service agent. American Eagle Pandora Sonepar เริ่มใช้แล้ว. ทำไมสำคัญ? เพราะนี่คือ multi-agent orchestration ที่หลายคนพูดกันมาปีนึง แต่ยังไม่มี case production ชัด ๆ. Bloomreach ทำจริงแล้วในแบรนด์ scale ระดับหลายพัน. Signal ที่ต้องจับตาคือ search bar เป็น real estate ที่มี intent สูงสุด — ใคร control ได้ควบคุม entry point ของทุก conversion. Salesforce Adobe Shopify น่าจะปล่อยของคล้าย ๆ กันในไตรมาสหน้า. คู่แข่งใครยัง silo search กับ chat กับ support แยกอยู่ต้อง rethink ครับ.
