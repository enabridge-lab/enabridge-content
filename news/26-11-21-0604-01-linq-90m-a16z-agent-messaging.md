---
date: 2026-11-18
slug: linq-90m-a16z-agent-messaging
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a giant glowing smartphone floating in
  the center with iMessage, WhatsApp, and RCS speech bubbles pouring out of it.
  Inside each bubble a tiny AI agent silhouette types and pushes orders onto a
  conveyor belt labeled "DOORDASH CHECKOUT". A large banner across the top
  reads "1,000,000,000 MESSAGES" and a price tag floats to the side: "$90M
  SERIES B". Soft turquoise and warm orange palette, 1:1 aspect, no real human
  faces, high contrast so numbers stay readable at 200px thumbnail size.
image: images/26-11-21-0604-01-linq-90m-a16z-agent-messaging.png
---

# Linq ปิด $90M a16z ย้าย agent ออกจาก chat window ไปอยู่ในข้อความทุกช่องที่คนใช้อยู่แล้ว

## TL;DR
- Linq ปิด Series B $90M นำโดย Andreessen Horowitz — Ben Horowitz นั่งบอร์ด, valuation ~$1B ตามรายงาน Dealroom
- Platform ทำให้ AI agent คุยกับลูกค้าผ่าน iMessage for Business, WhatsApp, RCS ได้โดยตรง — ไม่ต้องมี chat UI ของตัวเอง
- DoorDash deploy แล้ว ให้ลูกค้า discover ร้าน + checkout จบใน thread เดียว, Linq บอกว่าประมวลผ่าน 1 พันล้าน message ไปแล้ว
- กำลังเพิ่ม HD Calling (agent โทรคุยคุณภาพ handset) + physical computing infra ให้ agent ใช้ซอฟต์แวร์แทนคน

## เกิดอะไรขึ้น
วันที่ 18 พฤศจิกายน Linq สตาร์ทอัพซานฟรานซิสโกประกาศ Series B $90M นำโดย Andreessen Horowitz โดย Ben Horowitz จะเข้าไปนั่งเป็นบอร์ดเอง ตัวเลขที่ Dealroom รายงานต่อว่า valuation อยู่ที่ประมาณ $1B — ถ้าตัวเลขนี้จริงแปลว่า Linq ขยับจาก Series A $20M เมื่อเดือนกุมภาพันธ์มาเป็น unicorn ภายใน 9 เดือน ด้วยการขายคอนเซ็ปต์เดียว: "เอา agent ออกจาก chat window"

Core product ของ Linq คือ API layer ที่ให้ developer ทำให้ AI agent ส่งข้อความ ตอบลูกค้า และทำธุรกรรมผ่านช่องทางที่คนเปิดอยู่แล้ว — Apple Messages for Business, WhatsApp, RCS ลูกค้าไม่ต้องโหลดแอป ไม่ต้องสมัคร chatbot ของบริษัท agent ก็ส่งข้อความตามรหัสธุรกิจเข้าไปใน inbox ปกติได้เลย DoorDash เป็นลูกค้า reference case ที่ถูกพูดถึงมากที่สุด — ลูกค้าสามารถ discover ร้าน สร้างออเดอร์ และจ่ายเงินจบใน SMS conversation เดียว ไม่ต้องสลับไปเปิดแอป

Linq อ้างว่าแพลตฟอร์มประมวลผ่าน message ไปแล้วมากกว่า 1 พันล้านข้อความ — ตัวเลข 1 billion เป็น milestone ที่ไม่ว่าจะเป็น messaging infra ใดก็ตามต้องฝ่าไปให้ได้ก่อนจะมี network effect ที่ sustainable ได้ สิ่งที่ประกาศคู่กันในรอบนี้คือ 2 feature ใหม่: **HD Calling** ที่ให้ agent โทรเข้าโทรออกคุณภาพเสียง handset-grade และ **physical computing infrastructure** ที่เปิดให้ agent ใช้ซอฟต์แวร์เดสก์ท็อปแทนคน — เช่น เข้าเว็บ กรอกฟอร์ม upload ไฟล์ ใน sandbox ของ Linq เอง

## ทำไมสำคัญ
ปี 2026 ตลาด agentic AI พิสูจน์แล้วว่า chat UI แยกต่างหากไม่ใช่ default — Salesforce Agentforce ไปอยู่ใน Microsoft Teams, Anthropic ปล่อย Claude Duet ออกจาก chat.anthropic.com, ChatGPT Dots ของ OpenAI ก็โฟกัสที่การเข้าไปในชีวิตประจำวันผ่านโทรศัพท์และ connector Linq เลือกคนละทางกับทั้งหมด — แทนที่จะสู้เพื่อ chat surface ของตัวเอง หรือฝัง agent ใน productivity suite กลับไปโฟกัสที่ "อาวุธ default" ที่คนทำธุรกิจใช้คุยกับลูกค้ามาตั้งแต่ก่อน AI: SMS/MMS, WhatsApp, iMessage

แนวคิดนี้สำคัญเพราะมันตอบคำถาม go-to-market ของ agent ที่ยากที่สุด — จะให้ user คุยกับ agent ได้ยังไงโดยไม่ต้อง educate หรือติดตั้งอะไร ถ้าคนฟิลิปปินส์คุยกับร้านอาหารผ่าน WhatsApp อยู่แล้วทุกวัน การเอา agent ไปอยู่ใน WhatsApp conversation ก็ไม่ต้องสอนอะไรใหม่ ต่างจากการ pitch ให้เขาโหลด ChatGPT หรือ Claude app หรือสมัคร agent portal เว็บไซต์ลูกค้า นี่คือ distribution thesis เดียวกับที่ Agentforce ขึ้น 21x ใน 3 เดือนหลังไปอยู่ใน Teams — แต่ขยายไปถึง consumer

Caveat: Linq ไม่ได้ confirm valuation $1B เอง ตัวเลขนี้มาจาก Dealroom เท่านั้น และ "1 billion messages" เป็นตัวเลข aggregate ไม่มี breakdown ว่าเป็น customer-initiated หรือ agent-initiated สัดส่วนเท่าไหร่ ไม่มีตัวเลข revenue หรือ paid customer count ที่เปิดเผย ยิ่งไปกว่านั้น การเอา agent ไป text คนผ่าน SMS/WhatsApp เป็นดาบสองคม — ถ้า brand ใช้ agent spam หนัก ๆ regulatory backlash จะมาเร็ว โดยเฉพาะในสหรัฐที่ TCPA ค่าปรับต่อข้อความสูงมาก

## มุม AI Agent Platform
**Builders** — ถ้าคุณกำลังสร้าง agent ที่ต้องคุยกับ end user และยังไม่ได้คิดเรื่อง messaging distribution layer ให้ถอยกลับไปคิดใหม่ Linq round นี้บอกชัดว่า "ที่ agent ไปเจอ user" กลายเป็น unbundled stack แยกจาก "ที่ agent ถูกสร้าง" — เหมือนที่ Twilio เคยทำกับ communication API ยุคก่อน AI ความต่างคือ: ตอนนี้ agent ไม่ใช่แค่ส่งโน้ต OTP แต่ทำธุรกรรมเองได้ด้วย ดังนั้น compliance + fallback-to-human + rate-limit layer จะสำคัญกว่า raw API throughput

**Users/business** — สำหรับธุรกิจไทยที่ WhatsApp/LINE/Facebook Messenger คือช่องทางคุยลูกค้าหลัก Linq ยังไม่เปิด LINE แต่ pattern ที่ compan นี้ validate ได้คือ: agent ใน messaging surface ที่มีอยู่แล้ว > agent ใน app ของบริษัท Enabridge ที่สร้าง agent platform ให้ลูกค้าในไทยควรดูว่า channel integration กับ LINE Business Platform + WhatsApp Business API อยู่ตรงไหนในสถาปัตยกรรมของตัวเอง ถ้ายังไม่มี first-class — เสี่ยงที่ Linq (หรือ copycat ไทย) จะเข้ามากิน layer นี้ก่อน

**Ecosystem** — Twilio, Bandwidth, Sinch ต้องตื่น Linq ก็คือ Twilio generation 2 ที่ build-on-top-of messaging infrastructure ของพวกเขา ถ้า agent messaging เป็น category ใหม่จริง incumbents จะเลือกเอง — จะ compete (เปิด native agent API), partner (เชียร์ให้ Linq run บนตัวเอง), หรือ acquire ก่อนจะช้าเกิน a16z ลงเงินก้อนนี้พร้อม Ben Horowitz เอง = สัญญาณว่า a16z คิดว่า category นี้ใหญ่

## Sources
- [Linq Raises $90 Million in New Funding Led by Andreessen Horowitz (PRNewswire)](https://www.prnewswire.com/news-releases/linq-raises-90-million-in-new-funding-led-by-andreessen-horowitz-to-build-the-infrastructure-platform-for-ai-agents-302944728.html)
- [Linq raises $90M to put AI agents inside your text threads (Dealroom)](https://dealroom.co/news/174117-linq-raises-90m-to-put-ai-agents-inside-your-text-threads/)
- [Linq Raises $90 Million Series B Led by a16z (i10x)](https://i10x.ai/news/linq-raises-90-million-series-b-a16z-ai-agents-messaging)
- [Linq Raises $90M to Move AI Agents Beyond Chat Windows (Emergent)](https://emergent.sh/news/linq-raises-90m-move-ai-agents-beyond-chat)

---

## Audio script
ข่าวที่สำคัญที่สุดของสัปดาห์นี้ในวงการ agent infrastructure คือ Linq สตาร์ทอัพซานฟรานซิสโกปิด Series B เก้าสิบล้านดอลลาร์ นำโดย Andreessen Horowitz โดย Ben Horowitz จะเข้าไปนั่งเป็นบอร์ดเอง รายงานจาก Dealroom บอกว่า valuation อยู่ที่ประมาณพันล้านดอลลาร์ ขึ้นมาจาก Series A ยี่สิบล้านเมื่อเดือนกุมภาพันธ์ สิ่งที่ Linq ขายคือการเอา AI agent ออกจาก chat window ไปอยู่ในแอพส่งข้อความที่คนใช้อยู่แล้วทุกวัน Apple Messages for Business, WhatsApp, RCS ลูกค้าไม่ต้องโหลดแอพ ไม่ต้องสมัคร chatbot ของบริษัท agent ก็ส่งข้อความตรงเข้า inbox ปกติได้เลย DoorDash เป็นลูกค้าตัวอย่างที่ให้ลูกค้าสั่งอาหารและจ่ายเงินจบใน SMS conversation เดียว บริษัทอ้างว่าประมวลผ่านข้อความไปแล้วมากกว่าหนึ่งพันล้านข้อความ Thesis เบื้องหลัง deal นี้คือ distribution สำคัญกว่า model quality agent ที่อยู่ใน surface ที่คนใช้อยู่แล้วจะชนะ agent ที่อยู่ในแอพของตัวเอง สำหรับ builder ที่สร้าง agent platform ถ้าคุณยังไม่มี messaging distribution layer เป็น first-class ให้รีบคิดใหม่ สำหรับธุรกิจไทยที่ LINE WhatsApp Facebook Messenger เป็นช่องหลัก คำถามคือ platform ของคุณเชื่อม channel ที่ user ใช้อยู่แล้วได้ลึกแค่ไหน Twilio กับ Sinch ก็ต้องตื่น เพราะ Linq ก็คือ Twilio generation 2 ที่ build on top of infrastructure เดิม caveat คือ valuation พันล้านยังไม่ confirm จากบริษัทเอง และการ text ลูกค้าด้วย agent เป็นดาบสองคม ถ้าใช้เยอะไปเจอ regulatory backlash แน่
