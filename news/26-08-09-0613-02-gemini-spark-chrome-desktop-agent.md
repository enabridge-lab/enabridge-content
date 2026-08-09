---
date: 2026-08-08
slug: gemini-spark-chrome-desktop-agent
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: |
  A giant Chrome browser window opens like a doorway on a desktop; a small
  glowing "Gemini Spark" comet flies through it into a stack of logged-in
  tabs — Gmail, Booking, a bank. Behind the comet, saved-password key icons
  and cookie chips float. Bold caption on top reads "YOUR CHROME, THEIR
  AGENT" and "160+ COUNTRIES". Editorial isometric illustration, cool blue
  and warm amber palette, high contrast so text reads at 200px thumbnail,
  1:1 aspect, no real human faces.
image: images/26-08-09-0613-02-gemini-spark-chrome-desktop-agent.png
---

# Gemini Spark ยึด Chrome desktop ของคุณ — Google เปลี่ยนเกม browser agent

## TL;DR
- Google ปล่อย Gemini Spark ใช้ Chrome desktop จริงของ user แทน remote browser ของ Google — เข้าถึง session ที่ login อยู่แล้ว, saved password, cookies
- Rollout เริ่ม 3 สิงหาคม ที่ US สำหรับ AI Pro subscriber, ตอนนี้เปิดในกว่า 160 ประเทศ
- Google ยืนยัน payment และ sensitive action ต้อง human approve — แต่ prompt injection ยังเป็นความเสี่ยงที่ทีม security ทั่วโลกจับตา

## เกิดอะไรขึ้น
Google ประกาศเมื่อสัปดาห์ก่อนว่า Gemini Spark — always-on agent ที่รัน 24/7 บน cloud VM สำหรับ AI Ultra subscriber — ตอนนี้ทำงานบน Chrome desktop จริงของ user ได้แล้ว. ก่อนหน้านี้ Spark เปิด browser แยกใน cloud ของ Google, ผลลัพธ์คือทำงานพวก "จองอพาร์ตเมนต์" หรือ "search flight" ไม่ค่อยดี เพราะไม่มี session ที่ user login ไว้. Rollout เริ่ม 3 สิงหาคม ในสหรัฐฯ ตามด้วย 160+ ประเทศสำหรับ AI Pro subscriber ในสัปดาห์เดียวกัน.

โดย default Spark ขอ permission ก่อนเข้าถึง saved password และ logged-in session. Google ยกตัวอย่าง use case: schedule apartment viewing สำหรับ property ที่ user save ไว้, research flight option แล้ว start booking process จนถึงหน้า checkout — แต่ payment และ action sensitive อื่น ๆ ต้อง human validate. เบื้องหลัง Spark รันบน Gemini 3.5 และ orchestrate ผ่าน Antigravity — agent harness ที่ Google เปิดตัวที่ I/O 2026 เป็น platform สำหรับ build agentic software.

การ shift จาก remote browser ไป local Chrome เป็น pivot ทางสถาปัตยกรรมที่สำคัญกว่าที่ blog post ของ Google บอก. เมื่อ agent รันบน browser ของ user มันสืบทอด trust ทั้งหมดของ user — cookies, tokens, MFA session, saved credit card. นั่นคือทำไม OpenAI Operator ตัวแรก ๆ ที่รัน remote browser ต้องให้ user login ใหม่ทุก site และประสบการณ์แย่ ในขณะที่ Anthropic's Computer Use เริ่มจาก sandbox VM แต่ก็ผลักไปทาง local หลังจากที่ user เจอ friction เดียวกัน.

## ทำไมสำคัญ
Google กำลังทำสิ่งที่ Microsoft อยากทำมานาน — ใช้ browser ที่มี market share 65%+ เป็น distribution channel ของ agent. Chrome มี 3 พันล้าน user ทั่วโลก, และตอนนี้ทุกคนที่มี AI Pro subscription (ราคา $20/เดือน) ได้ agent ที่รู้จัก workflow ของตัวเองมาแล้ว. Comparable move ที่ Perplexity ทำผ่าน Comet browser หรือ Arc's DIA เกิดที่ scale ที่คนละระดับ.

Signal ที่สำคัญคือ Google เลือก risk profile นี้อย่างมี strategy. ให้ agent เข้าถึง saved password และ logged-in session แปลว่า prompt injection กลายเป็น attack surface ระดับ enterprise — malicious website บอก agent ให้โอนเงิน, ส่ง email, หรือ leak data. Google เพิ่ม safeguard สำหรับ prompt injection และบังคับ human-in-the-loop สำหรับ payment. Anthropic เพิ่งเผยแพร่ research เดือนที่แล้วว่า computer-use agent ยังโดน hijack ได้ 20%+ ในสถานการณ์ที่ทดสอบ — Google เดินหน้า ship อยู่ดี. นี่คือคำตอบว่า agent race ตอนนี้ไม่ใช่แค่ capability แต่เป็นเรื่อง distribution และ trust ที่ existing product เอามาแลก.

## มุม AI Agent Platform
สำหรับ **builders** ที่ทำ browser agent (Browserbase, Anchor, Nova Act ของ Amazon): moat เดิมของการ maintain browser infra ในระดับ scale เริ่มถูก challenge เพราะ Chrome ของ user ฟรี. โอกาสจะกลายเป็น layer ของ orchestration + memory + eval แทน raw browser execution. สำหรับ **enterprise ที่ deploy agent**: ทีม security ต้องประเมินใหม่ — Chrome enterprise policy เพียงพอไหมสำหรับ Gemini Spark? MDM tool ต้อง detect/block ไหม? นี่จะเป็นเรื่องเดียวกับที่เคยเถียงกันเรื่อง shadow IT ยุค SaaS — พอ agent เข้าถึง SaaS ทุก tool ที่ user login แล้ว governance layer ต้องเลื่อนขึ้นไปที่ browser + identity provider. สำหรับ **ecosystem**: Chrome extension marketplace จะกลายเป็น distribution channel ของ agent tool คล้าย App Store — และ Google จะได้ทั้ง OS layer (Chrome) และ agent layer (Gemini) ในคราวเดียว.

## Sources
- [Google's Gemini Spark Expands to More Countries and Adds New Chrome Features | Thurrott](https://www.thurrott.com/a-i/339900/googles-gemini-spark-agent-expands-to-more-countries-and-adds-new-chrome-features)
- [Gemini Spark can now use Chrome to auto browse | 9to5Google](https://9to5google.com/2026/07/30/gemini-spark-chrome-auto-browse/)
- [Google's Gemini Spark Takes Control of Chrome to Automate Web Tasks | BigGo Finance](https://finance.biggo.com/news/01999bcd-5e70-4cf8-a34f-f62bab2150b8)

---

## Audio script
เรื่องต่อไปเป็นเรื่องที่จะเปลี่ยนการใช้ browser ของทุกคน. Google ปล่อย Gemini Spark ที่ตอนนี้ไม่ใช้ browser ใน cloud อีกต่อไป — แต่เข้ามาขับ Chrome desktop ของคุณโดยตรง. หมายความว่ามัน login เข้า Gmail Booking bank ธนาคาร ทุกที่ที่คุณเคย login ไว้ได้เลย รวมถึง saved password. Rollout เริ่มวันที่สามสิงหาที่อเมริกา ตอนนี้เปิดในกว่าหนึ่งร้อยหกสิบประเทศแล้ว สำหรับ AI Pro subscriber. use case ที่ Google โชว์คือให้ agent ไปนัดดูอพาร์ตเมนต์ที่คุณ save ไว้ หรือหา flight แล้วเข้าไปเริ่ม booking — แต่ตอน payment ต้องกดยืนยันเอง. เหตุผลที่สำคัญคือนี่คือ moment ที่ Google เอา Chrome ซึ่งมีคนใช้สามพันล้านคนเป็น distribution channel ของ agent — Perplexity Arc หรือ browser agent อื่น distribution ห่างชั้นเลย. แต่ประเด็นที่ต้องระวังคือ prompt injection. เมื่อ agent เข้าถึง cookie password ของคุณได้ทั้งหมด เว็บที่มี malicious payload อาจสั่ง agent ให้โอนเงินหรือ leak data ได้. Anthropic วิจัยเดือนที่แล้วเจอว่า agent ยังถูก hijack ได้ยี่สิบเปอร์เซ็นต์ในสถานการณ์ทดสอบ. Google ยังเดินหน้า ship — นี่แปลว่า agent race ตอนนี้แข่งกันที่ distribution และ trust ไม่ใช่ capability อย่างเดียวแล้วครับ.
