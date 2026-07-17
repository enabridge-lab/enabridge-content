---
date: 2026-07-18
slug: cars24-openai-voice-agents-india-1m-minutes
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a bustling India used-car
  dealership at dusk with a silhouetted headset icon glowing over a
  rooftop antenna. Big stacked numerals dominate the sky:
  "1,000,000 MINUTES / MONTH", "12% LOST LEADS RECOVERED",
  "600 EMPLOYEES ON CHATGPT". A stylized car outline and a phone
  handset shape connect via curving voice-wave lines. Warm amber and
  deep navy palette, brand-neutral logos, no real human faces,
  1:1 aspect, readable at 200px thumbnail.
image: images/26-07-18-0609-03-cars24-openai-voice-agents-india-1m-minutes.png
---

# Cars24 handles 1 ล้านนาที/เดือน — ตัวอย่าง voice agent ใน emerging market

## TL;DR
- Cars24 (ผู้ค้ารถมือสองรายใหญ่สุดในอินเดีย, IPO-bound) เผยว่า OpenAI voice + chat agent จัดการบทสนทนาลูกค้า **>1 ล้านนาที/เดือน**
- Agent recover **12% ของ lost lead** ที่ตกไปในช่องระหว่าง test drive กับ purchase
- ChatGPT Enterprise + Codex deploy กับ ~600 พนักงาน, DAU ที่ **85–90%** — เกือบทุกคนใช้ทุกวัน
- OpenAI publish case study อย่างเป็นทางการ 16 ก.ค. — เป็น emerging-market use case ที่มีตัวเลขจริงมากที่สุดในรอบปี

## เกิดอะไรขึ้น
เมื่อ 16 กรกฎาคม OpenAI publish case study Cars24 บน openai.com/index/cars24 — โฟกัสไปที่การที่ Cars24 ใช้ Realtime API + Chat Completions ประกอบ AI voice/chat agent ที่คุยกับลูกค้าตั้งแต่ initial inquiry, budget qualification, test-drive booking, financing intake, ไปจนถึง post-purchase support. ตัวเลขที่ Cars24 เปิดคือ >1 ล้านนาที conversation ต่อเดือน — ไม่ใช่นาที idle แต่คือนาทีที่ agent คุยกับลูกค้าจริงในแต่ละขั้นของ funnel

กลไก recover 12% lost lead น่าสนใจ: ก่อนหน้านี้ลูกค้าจำนวนมากดูรถ, จองทดลองขับ, แล้วก็ไม่มา — Cars24 ต้องส่ง sales rep มนุษย์โทรตาม, ค่าใช้จ่ายต่อ contact สูง, coverage ไม่พอ. AI agent โทรตาม 24 ชั่วโมงในทุกภาษาอินเดีย, ยืนยันนัด, offer alternative car ถ้า preference เปลี่ยน. ผลลัพธ์ 12% ของลูกค้าที่จะสูญเสียตามระบบเดิม กลับเข้า funnel ได้

อีกด้านที่น่าจะสำคัญกว่ากับทีมไทย: internal deploy. ChatGPT Enterprise + Codex ให้พนักงาน central org ~600 คน — ครอบคลุม engineering, finance, legal, marketing, operations. DAU 85–90% แปลว่า tool ไม่ได้ถูกซื้อมาแล้ววางเฉย. Cars24 report ว่า Codex ช่วยทีมวิศวกร build workflow กับ automate recurring task ได้เร็วขึ้นมาก. Cars24 ยังประกาศ AI Lab ที่ commit $20M investment ให้ AI startup — จับ ecosystem อินเดีย

Autoguideindia รายงานเสริมว่า Cars24 ประมวล **1.1 ล้านล้าน AI token ในไตรมาสเดียว** — จำนวนที่ enterprise B2C ในเอเชียยังไม่มีใครแตะ

## ทำไมสำคัญ
เกือบทุก case study voice AI ที่ enterprise เอามาโชว์ในปี 2025 เป็นของ US company หรือ European B2B — Klarna, Air India Express, T-Mobile. Cars24 เป็นตัวอย่างของ **emerging-market B2C** ที่มีตัวเลข deployment ระดับ production จริง ๆ. Volume 1 ล้านนาที/เดือน + recover 12% lost lead + 1.1T token/ไตรมาส แปลว่า unit economics ของ voice agent ในตลาดที่ค่าจ้าง sales rep ต่ำกว่า US มาก — ก็ยังคุ้ม

สิ่งที่ Cars24 ทำถูกและควรลอกคือ scope ที่แคบและวัดผลได้: agent ไม่ได้มา replace มนุษย์ทุกจุด, แค่จับ funnel gap ที่มนุษย์ทำไม่ทัน — โทรตามหลัง test-drive miss, qualify budget ตอน off-hours, offer alternative car. 12% recover เป็นตัวเลขที่ CFO อ่านแล้วเข้าใจได้ทันที ไม่ต้องแปล

Pattern การใช้ ChatGPT Enterprise + Codex ภายในองค์กร 600 คน DAU 85–90% ก็เป็น benchmark ที่หลายบริษัทไทยควรตั้งเป้า. องค์กรส่วนใหญ่ที่ซื้อ ChatGPT Enterprise พบ DAU 20–40% หลัง 6 เดือน — Cars24 ทำ 85–90% เพราะ workflow บังคับใช้จริง ไม่ใช่แค่ optional tool

## มุม AI Agent Platform
**Builder** — voice agent stack ของ Cars24 (Realtime API + Chat Completions + integration กับ CRM ของตัวเอง) แสดงให้เห็นว่าไม่จำเป็นต้องมี "voice agent platform" ระดับ Retell / Vapi ก็สร้าง production system ได้ ถ้าทีม engineering ในบ้านแข็งพอ. สำหรับ Enabridge / builder ในไทย — ช่องทางที่น่าสน คือ vertical wrapper (used-car, real estate, insurance, telecom) ที่ package "voice agent stack + local telephony + CRM integration + Thai-specific voice tuning" เป็น product เดียว. **Users / business** — ถ้าองค์กรมี call center ขนาดใหญ่, ไม่ใช่คำถามว่า "จะทำไหม" อีกแล้ว, แต่คือ "เริ่มจาก funnel gap ไหน" — เลือกจุดที่ agent human hand-off ชัด ๆ ก่อน (missed call, follow-up, qualification). **Ecosystem** — OpenAI push case study แบบนี้บ่อยขึ้นในไตรมาสหลัง แปลว่า sales motion ของ OpenAI Enterprise กำลังชนกับ Anthropic โดยตรงในตลาด APAC — ทีมที่เลือก vendor อยู่ต้องดูให้ดีว่า pricing model ของแต่ละเจ้าจะทน scale 1T+ token/ไตรมาสได้หรือเปล่า

## Sources
- [How Cars24 scales conversations and builds faster with OpenAI](https://openai.com/index/cars24/)
- [Cars24 Supercharges Sales with OpenAI (StartupHub.ai)](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/cars24-supercharges-sales-with-openai)
- [Cars24 triples AI usage, Processes 1.1 trillion AI tokens in a quarter (Autoguideindia)](https://www.autoguideindia.com/reports/cars24-1-1-trillion-ai-tokens-q1-fy27-consumer-ai-transformation/)
- [IPO-Bound Cars24 Commits $20 Million to Launch AI Labs](https://startupfox.in/article/cars24-launches-ai-labs-20-million-investment-startups)

---

## Audio script
วันที่ 16 กรกฎาคม OpenAI เผย case study ของ Cars24 — ผู้ค้ารถมือสองรายใหญ่สุดของอินเดียที่กำลังจะ IPO. ตัวเลขที่น่าสนใจคือ voice + chat agent ของ Cars24 จัดการบทสนทนาลูกค้าเกิน 1 ล้านนาทีต่อเดือน. ไม่ใช่นาที idle นะ แต่คือนาทีที่ agent คุยกับลูกค้าจริงทุกขั้นของ funnel ตั้งแต่ inquiry, ทดลองขับ, financing, ไปถึง post-purchase. กลไกที่น่าลอกคือการที่ agent โทรตามลูกค้าที่ miss test-drive appointment — recover ได้ 12% ของ lost lead ที่จะสูญไปในระบบเดิม. อีกด้านคือ internal deploy — ChatGPT Enterprise กับ Codex ให้พนักงานประมาณ 600 คน DAU 85–90% — เกือบทุกคนใช้ทุกวัน. เทียบกับ enterprise ทั่วไปที่ DAU หลัง 6 เดือนอยู่แค่ 20 ถึง 40 เปอร์เซ็นต์. Cars24 ยังประมวล token 1.1 ล้านล้านในไตรมาสเดียว — ระดับที่ enterprise B2C ในเอเชียยังไม่มีใครแตะ. บทเรียนสำหรับทีมไทยชัดมาก: อย่ามอง voice agent เป็นการ replace มนุษย์ทุกจุด, ให้เลือก funnel gap ที่มนุษย์ทำไม่ทัน — missed call, follow-up, budget qualification — วัดผลเป็นตัวเลข lost lead recovery ที่ CFO อ่านแล้วเข้าใจได้ทันที. สำหรับ builder — vertical wrapper ที่ package voice agent + telephony ไทย + CRM integration ยังเป็นช่องว่างที่ยังไม่มีใครยึด
