---
date: 2026-10-17
slug: kakao-kanana-space-messenger-agent
topic: use-case
reading_time_min: 3
sources: 3
image_prompt: |
  A giant yellow chat bubble floating above Seoul skyline, labeled "KAKAO
  TALK → AGENT INTERFACE"; inside the bubble three stacked numbers glow:
  "10M MAU TARGET", "DEC 2026 BETA", "H1 2027 PUBLIC". A translucent robot
  concierge inside the bubble hands a shopping bag and a train ticket to a
  silhouette figure while a payment prompt labeled "APPROVE?" waits for
  confirmation. Editorial isometric style, yellow and slate palette, high
  contrast for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-17-0614-04-kakao-kanana-space-messenger-agent.png
---

# Kakao Kanana Space: เมื่อ messenger กลายเป็น primary interface ของ agent — 10M MAU target

## TL;DR
- ที่งาน **if(kakao) 26** Kakao เปิดตัว **Kanana Space** — assistant ที่เปลี่ยน **KakaoTalk** จาก messaging app เป็น agent interface ที่คุม message, schedule, shopping ภายใน chatroom
- **Closed beta ธ.ค. 2026**, public ผ่าน KakaoTalk ตั้งเป้า **H1 2027** — payment + outgoing message ต้องมี final approval จาก user
- **Target: 10 ล้าน MAU** ของ KakaoTalk AI services ภายในสิ้นปี — เป้าหมายระยะยาวแซง ChatGPT ใน South Korea ภายใน 2029

## เกิดอะไรขึ้น

เมื่อ 13 ต.ค. ที่งาน if(kakao) 26 Kakao Corp (operator ของ KakaoTalk — messenger ที่ 95% ของคน South Korea ใช้) ประกาศ **Kanana Space** — assistant ที่ merge voice + text + conversational context ให้ user ทำ task จบในกรอบของ chatroom ไม่ต้อง switch app Kanana เป็น series บน-device assistant ของ Kakao ที่เริ่ม iOS beta ต้นปี 2026 — Kanana Space คือการ **ยกระดับจาก assistant เดี่ยว ๆ** เป็น interface ของ ecosystem agent ทั้งหมด

Flow ที่ Kakao demo: user พิมพ์ใน chat "ขอ gift card Starbucks 20,000 won ให้แม่" Kanana ทำ 3 ขั้น — ค้นหา SKU, ตัดเงินจาก KakaoPay (**ต้องรอ user confirm**), ส่ง gift card เข้า chatroom ของแม่โดยอัตโนมัติ ทั้งหมดเกิดใน chat window เดียว ไม่ต้องเปิด Kakao Shopping หรือ KakaoPay แยก Kakao positioning นี้เป็น "agent-first commerce" — payment + outgoing message **ต้องมี final approval** เพื่อลด risk แต่ discovery + search + context ทำ background ได้ตลอด

Kakao ยัง tie-in กับ **Coupang Eats** ตั้งแต่ ส.ค. — food delivery เป็น vertical แรกที่ test agent-first commerce ภายใน KakaoTalk — user order + pay ไม่ต้องเปิด app Coupang Eats แยก และ Kakao ประกาศ **AI for All** consortium ภายใต้ LG U+ ที่จะปล่อย general-purpose chatbot + public agent + specialized agent (public service, health, elderly care) โดย beta เดือน ต.ค., official release ธ.ค.

**Target ที่ ambitious ที่สุด** — Kakao บอกจะเกิน **10 ล้าน MAU** ของ AI services ภายในสิ้นปี 2026 (รายงานอื่น conservative กว่าที่ 5 ล้าน) และตั้งเป้า **แซง ChatGPT ใน South Korea** ภายในปี 2029

## ทำไมสำคัญ

สิ่งที่ Kakao กำลัง test คือ hypothesis ที่ western platform ไม่กล้าเสี่ยง — **messenger เป็น primary interface ของ agent** ไม่ใช่ IDE, browser, standalone app WeChat ของ Tencent มี pattern นี้มาตั้งแต่ 2017 (mini-program + payment ภายใน chat) และพิสูจน์ว่าทำงานในตลาด Chinese 1 พันล้าน user ตอนนี้ Kakao กำลัง replicate ใน South Korea 50 ล้าน population แต่ด้วย agent native จากวันแรก ไม่ใช่ mini-program ที่เป็น embedded web

ที่น่าสนใจคือ **constraint design** — Kakao บังคับ payment + outgoing message ให้ผ่าน user approval ซึ่งคือ response ต่อ fail mode ที่ WeChat เคยเจอ (fraud, spam, phishing ใน mini-program) และต่างจาก US agent framework ที่ส่วนใหญ่ assume full autonomy ก่อน แล้วค่อยเพิ่ม guard rail — Kakao start ด้วย guard rail ก่อน

Comparison กับ US — Google Gemini Agent / OpenAI Operator / Anthropic Claude Platform ทั้งหมดยัง assume agent รันใน browser หรือ app ของตัวเอง ไม่ได้ชน messenger platform ตรง ๆ Meta WhatsApp Business API มี agent ของ merchant ได้ แต่ไม่ใช่ **personal assistant layer** ของ user Kakao กำลัง test ว่าถ้า agent อยู่ใน messenger จริง conversion rate จะสูงกว่าหรือเปล่า — คำตอบของ Kakana Space คือ data point ที่ Google, Meta, Microsoft จะดูอย่างใกล้ชิด

## มุม AI Agent Platform

สำหรับ **builder** ที่กำลังสร้าง agent สำหรับ consumer — ถ้า hypothesis ของ Kakao ถูกต้อง (messenger = agent interface) distribution strategy ต้อง pivot ไม่ใช่ล้ว app standalone แต่ reach ผ่าน messenger ที่มีอยู่แล้ว LINE ใน SEA (Thailand/Taiwan/Japan) จะเป็นคู่เปรียบที่ชัดที่สุดสำหรับทีม Thai — ถ้า Kanana Space ประสบความสำเร็จ LINE น่าจะเปิด agent API ที่คล้ายกันภายใน H1 2027

สำหรับ **business ที่ deploy agent สำหรับ consumer-facing commerce** — คำถามใหม่คือ "ลงทุน in-house agent หรือ integrate เข้ากับ messenger ที่ user ใช้อยู่แล้ว" ถ้า user ไม่ต้องการ switch app นี่คือ friction ที่ e-commerce brand ไม่ควรเพิ่ม — เลยอาจเป็นเหตุผลให้ enterprise brand ย้าย point-of-sale agent เข้า LINE/Kakao/WhatsApp Business

สำหรับ **ecosystem** — Kakao เป็น case study แรกใน Asia ที่ productize messenger-as-agent-interface ที่ scale ถ้า adoption จริง (10M MAU) ภายใน Q1 2027 vendor อื่น (LINE, Rakuten, Grab) จะ copy pattern เร็ว — ขณะที่ US ยัง stuck อยู่ที่ "ไหนคือ ที่อยู่ของ agent?"

## Sources
- [Kakao unveils Kanana Space as KakaoTalk expands into AI interface — Korea Times](https://www.koreatimes.co.kr/business/tech-science/20261013/kakao-unveils-kanana-space-as-kakaotalk-expands-into-ai-interface)
- [South Korea's Kakao Turns KakaoTalk Into an AI Agent Platform — BigGo Finance](https://finance.biggo.com/news/41149b60-52de-4770-91ca-ef9e52b39bd0)
- [Kakao Launches ChatGPT Chatbot for KakaoTalk Chatrooms — kakaocorp.com](https://www.kakaocorp.com/page/detail/12107)

---

## Audio script
Kakao Corp ที่ operate KakaoTalk messenger ที่ 95 เปอร์เซ็นต์ของคน South Korea ใช้ ประกาศ Kanana Space เมื่อ 13 ตุลาคมที่งาน if kakao 26 ว่าจะเปลี่ยน KakaoTalk จาก messaging app เป็น primary interface ของ agent คุม message schedule shopping payment ภายใน chatroom เดียว ไม่ต้อง switch app

Closed beta เริ่ม ธันวาคม 2026 เปิด public ผ่าน KakaoTalk ครึ่งแรกปี 2027 Target คือ 10 ล้าน MAU ของ AI services ภายในสิ้นปี และระยะยาวตั้งเป้าแซง ChatGPT ใน South Korea ภายใน 2029

จุดสำคัญคือ constraint design — Kakao บังคับให้ payment และ outgoing message ต้องมี final approval จาก user ก่อน ซึ่งเป็น response ตรงต่อ fail mode ที่ WeChat เคยเจอใน mini program เรื่อง fraud spam phishing และต่างจาก US agent framework ที่ assume full autonomy ก่อนแล้วค่อยเพิ่ม guard rail Kakao เริ่มด้วย guard rail ก่อน

Pattern นี้สำคัญสำหรับทีมในไทยที่ build consumer agent เพราะ LINE ที่ dominant ใน SEA น่าจะเปิด agent API ที่คล้ายกันภายในครึ่งแรกปี 2027 ถ้า Kanana Space ประสบความสำเร็จ แปลว่า brand ที่กำลังสร้าง consumer agent ควรวาง roadmap ว่าจะอยู่ใน messenger ของ user ไม่ใช่สร้าง app standalone แยกออกไป เพราะ friction ของการ switch app จะทำให้ conversion ตก
