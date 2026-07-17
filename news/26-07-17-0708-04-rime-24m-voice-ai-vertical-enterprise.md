---
date: 2026-07-15
slug: rime-24m-voice-ai-vertical-enterprise
topic: use-case
reading_time_min: 3
sources: 4
image_prompt: |
  A moody editorial illustration of a soundproof recording booth glowing
  in the corner of a corporate skyline. A tape reel labeled "STUDIO DATA"
  spins in the center; sound waves flow out toward four building
  silhouettes labeled "MAYO CLINIC", "DIALPAD", "UPSTART", "ASURION".
  Three stacked block-letter numbers dominate the top: "$24M SERIES A",
  "35 PEOPLE", "STUDIO-TRAINED VOICE". Editorial magazine style, warm
  amber palette, 1:1 aspect, readable at 200px thumbnail, no real human
  faces (silhouettes only).
image: images/26-07-17-0708-04-rime-24m-voice-ai-vertical-enterprise.png
---

# Rime ปิด $24M Series A — voice AI ที่เทรนจาก studio ของตัวเอง กลายเป็นสูตรที่ยักษ์เข้าไม่ถึง

## TL;DR
- **15 กรกฎาคม 2026** — Rime ปิด Series A $24M นำโดย M13 Ventures, ตามด้วย Twilio Ventures, Corazon Capital, และ Unusual Ventures — เพื่อขยาย voice AI ที่ handle enterprise call
- ต่างจากคู่แข่ง — Rime **บันทึกเสียง conversational data เองใน studio ที่ San Francisco** ไม่ scrape เสียงจาก web
- Customer จริงระดับ Mayo Clinic, Dialpad, Upstart, Asurion — ทีม 35 คน, จะขยายให้ hire model + partnership

## เกิดอะไรขึ้น

Rime — voice AI startup จาก San Francisco ที่ก่อตั้งปี 2022 โดย Lily Clifford (ex-Stanford PhD), Brooke Larson (ex-Amazon Alexa), และ Ares Geovanos — เพิ่งปิด Series A $24 ล้านเมื่อวันที่ 15 กรกฎาคม. M13 Ventures นำรอบ, Twilio Ventures ตามเข้ามาเป็น strategic (บอกใบ้ว่าจะ integrate กับ Twilio voice), Corazon Capital และ existing backer Unusual Ventures ปิดขอบ. Morgan Blumberg จาก M13 นั่งเข้าบอร์ด และบริษัทเพิ่งดึง Rafael Valle — เดิมทำ audio understanding ที่ Meta Superintelligence Labs และ Nvidia — มาเป็น Chief Scientist

จุดที่ Rime ต่างจากคู่แข่ง voice AI (ElevenLabs, Cartesia, Deepgram) คือ **data supply chain**. คู่แข่งส่วนใหญ่ train บน voice data ที่ scrape จาก podcast, YouTube, และ audiobook — ซึ่งเป็นเสียง monologue ไม่ใช่ conversation จริง. Rime สร้าง recording studio ของตัวเองใน San Francisco แล้ว hire voice actor ให้เล่น scenario ของ customer service call — คำถาม, การขัดจังหวะ, การเปลี่ยนอารมณ์, silence, filler word ("um", "let me think") — ทั้งหมดที่ทำให้ agent ฟังเป็นธรรมชาติจริง

customer list ที่ Rime เปิด — **Mayo Clinic, Dialpad, Upstart, Asurion** — คลุมทั้ง healthcare, telco, fintech, insurance/warranty. ทั้งสี่คือ enterprise ที่ regulatory strict กับ voice quality (misheard word ในสายประกันเสียได้ทั้ง case). ทีม 35 คน จะขยายด้าน model development, engineering, และ partnership โดยเฉพาะ

## ทำไมสำคัญ

pattern ที่ Rime พิสูจน์คือ **data moat > model architecture** ในยุคที่ base model เก่ง ๆ commodity แล้ว. ElevenLabs มี compute เยอะกว่า Rime หลาย order of magnitude แต่ถ้า training data คุณคือ audiobook คนอ่านคนเดียว agent จะสะดุดตอนเจอ live customer ที่ขัดจังหวะกลางประโยค. Rime แลกเวลาสร้าง studio 4 ปี ให้ได้ conversational data ที่ scraper คู่แข่งเข้าไม่ถึง

signal ที่ตามมาคือ vertical voice AI จะเริ่ม fragmentation — healthcare voice, financial voice, retail voice จะเป็น product แยกกัน เพราะ compliance และ vocabulary ต่างกันมาก. คู่แข่งใหญ่ที่ปรับตัวไม่ทันจะเสีย enterprise deal ให้ specialist. Cartesia กับ ElevenLabs Enterprise ที่พยายามคุม end-to-end ต้องเลือกระหว่างสร้าง studio ตาม Rime หรือ acquire คนที่มี proprietary data set — ทั้งสองทางแพงและช้า

pattern คู่ขนานน่าสังเกต — voice AI startup ที่ปิดรอบใหญ่ครึ่งปีที่ผ่านมา (Cartesia, Sesame, PolyAI) ทั้งหมด positioning ตัวเองรอบ enterprise contact center ไม่ใช่ consumer. Rime lock strategy เดียวกันแต่มี **data-side moat** ที่ยากลอกเลียน. valuation ของรอบไม่เปิดเผย แต่ Series A $24M กับทีม 35 คนน่าจะ imply post-money ราว $150–200M — ยังมี room ให้ scale ก่อนต้องปิดรอบใหม่

## มุม AI Agent Platform

**Builders** ที่ทำ voice agent — ถ้าคุณ train บน public voice dataset เท่านั้น output ของคุณจะฟังเหมือน narration ไม่ใช่ conversation. หา conversational data ที่จริง (บันทึกเอง หรือ license จาก contact center) เป็นการลงทุน core ไม่ใช่ nice-to-have. **Users / business** — เมื่อ agent เริ่ม handle inbound call ที่จริงจัง เช่น booking, refund, appointment, ตัว voice quality กลายเป็น brand risk. องค์กรควรมี benchmark ว่า voice agent ที่ใช้ pass ทดสอบ regulatory (recorded evidence, PCI-DSS, HIPAA) หรือไม่ — ไม่ใช่แค่ evaluation เชิง latency กับ WER. **Ecosystem** — Twilio ที่ลง strategic ใน Rime บอกใบ้ว่า Twilio Voice จะเริ่ม bundle Rime เป็น default voice model สำหรับ programmable voice — เป็นสัญญาณ distribution ระดับ AWS Marketplace ที่ startup อื่นได้ยาก. สำหรับ Enabridge ที่ทำ agent ในบริบทไทย — voice AI ในภาษาไทยยังห่างจาก English 12–18 เดือน; ถ้าจะ deploy voice agent ควร partner กับผู้ให้บริการที่มี Thai conversational studio data เอง มากกว่ารอ frontier lab support

## Sources
- [Rime picks up $24M Series A to help enterprises field customer calls — TechCrunch](https://techcrunch.com/2026/07/15/rime-picks-up-24m-series-a-to-help-enterprises-field-customer-calls/)
- [Rime Lands $24M Series A to Scale Voice AI — CMSWire](https://www.cmswire.com/customer-experience/rime-lands-24m-series-a-to-scale-voice-ai/)
- [Rime Raises $24M in Series A Funding — FinSMEs](https://www.finsmes.com/2026/07/rime-raises-24m-in-series-a-funding.html)
- [Voice AI Startup Rime Closes $24M Series A Led by M13 — JustAI News](https://justainews.com/applications/voice-and-speech-recognition/voice-ai-startup-rime-closes-24m-series-a-led-by-m13/)

---

## Audio script
เรื่องสุดท้ายวันนี้ครับ Rime สตาร์ทอัพ voice AI จาก San Francisco เพิ่งปิด Series A 24 ล้านเหรียญเมื่อวันที่ 15 กรกฎาคม. M13 นำรอบ ตามด้วย Twilio Ventures ที่ลงมาแบบ strategic. จุดที่น่าสนใจไม่ใช่ตัวเงิน แต่เป็น data supply chain ครับ. คู่แข่ง voice AI ส่วนใหญ่ ElevenLabs Cartesia Deepgram train โมเดลบนเสียงที่ scrape จาก podcast กับ audiobook ซึ่งเป็น monologue คนอ่านคนเดียว. Rime สร้าง studio recording เองที่ San Francisco เลย hire voice actor มาเล่น scenario ของ customer service call ทั้งการขัดจังหวะ การถามซ้ำ silence filler word อย่าง um กับ let me think ที่ทำให้ agent ฟังเป็นธรรมชาติจริง. Customer ปัจจุบันคือ Mayo Clinic, Dialpad, Upstart, Asurion ทั้งหมดคือ enterprise ที่ regulatory strict มาก. Pattern ที่ Rime พิสูจน์คือในยุคที่ base model กลายเป็น commodity data moat ต่างหากที่เป็นสนามรบ. ถ้าคุณสร้าง voice agent อยู่ อย่า train บน public dataset อย่างเดียว หา conversational data ที่จริงจากการบันทึกเองหรือ license มาจาก contact center เป็นการลงทุนแกน ไม่ใช่ nice-to-have. สำหรับ Enabridge ที่ทำในบริบทไทย voice AI ภาษาไทยยังห่าง English 12 ถึง 18 เดือน ถ้าจะ deploy จริงควร partner กับผู้ให้บริการที่มี Thai conversational studio data เอง ดีกว่ารอ frontier lab จาก US เข้ามาซัพพอร์ตครับ
