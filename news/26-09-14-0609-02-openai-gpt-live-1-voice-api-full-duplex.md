---
date: 2026-09-14
slug: openai-gpt-live-1-voice-api-full-duplex
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A vibrant editorial illustration of a voice waveform crossing itself in real
  time, with two microphones facing each other. Three bold price tags float
  above: "$0.05 / MIN", "0.798 SEC LATENCY", "86.2% TAU3". Below sits a small
  call center silhouette with headsets glowing amber. OpenAI logomark visible in
  the corner. Editorial isometric style, dark teal background with bright coral
  accents, sharp legible numerals sized for a 200 pixel thumbnail, 1:1 aspect,
  no real human faces.
image: images/26-09-14-0609-02-openai-gpt-live-1-voice-api-full-duplex.png
---

# OpenAI เปิด GPT-Live-1 API ที่ $0.05 ต่อนาที — voice agent economics เปลี่ยนอีกครั้ง

## TL;DR
- GPT-Live-1 เข้า API ที่ราคา **$0.05 ต่อนาที** — full-duplex ฟังกับพูดพร้อมกัน โมเดลเดียวกับ ChatGPT Voice
- Latency ลดจาก 1.63 วิ (GPT-Realtime-2) เหลือ **0.798 วิ** — ครึ่งหนึ่ง; Tau3 benchmark กระโดดจาก 45.7% เป็น **86.2%** เกือบสองเท่า
- Voice-AI ตอนนี้กินไป 19% ของ inbound contact-center volume (จาก 6% ในปี 2024). Cost per resolution ~$1.18 vs $7.40 ของคน

## เกิดอะไรขึ้น

OpenAI ปล่อย GPT-Live-1 เข้า API เมื่อ 10 กันยา — โมเดล full-duplex ตัวเดียวกับที่รัน ChatGPT Voice. คำว่า full-duplex ในโลก voice AI แปลว่ามันฟังกับพูดพร้อมกัน ไม่ใช่รอ user พูดจบแล้วค่อยเริ่มตอบ. ก่อนหน้านี้ pipeline voice agent ส่วนใหญ่คือ STT → LLM → TTS สาม hop ที่ latency สะสม 1.5-2 วินาที; hop เหล่านั้นทำให้ conversation รู้สึก "รอ" — ผู้ใช้ชั่งใจว่าจะแทรกดีไหม, ระบบไม่รู้ว่ายังพูดต่อดีไหม.

ตัวเลขที่ OpenAI ประกาศ: response latency จาก 1.63 วินาที (GPT-Realtime-2) ลงเหลือ 0.798 วินาที. Tau3 benchmark (evaluate voice agent capability) กระโดดจาก 45.7% เป็น 86.2% — เกือบสองเท่า. ในโลก voice ต่างของ 300 มิลลิ กับ 800 มิลลิ คือความต่างของ "natural" กับ "annoying" — ตัวเลข 0.798 ยังไม่ถึง natural แต่ก็ไม่ใช่ annoying แล้ว. ราคา $0.05/นาทีสำหรับ voice layer เดี่ยว — ถ้าเทียบว่า human agent ค่าใช้จ่ายต่อนาทีคุยลูกค้าอยู่ในหลักหลายบาท-สิบบาท. Cost differential ยังชัดมาก.

## ทำไมสำคัญ

Voice agent เคยเป็น "cool demo แต่ deploy ยาก" — เพราะ latency, hallucination, และ interruption handling ทั้งสามเรื่องพร้อมกัน. หนึ่งปีที่ผ่านมา containment rate ของ voice AI deployment ที่ดี ๆ ขึ้นไปแตะ 50% แล้ว ในธุรกิจ hospitality, travel, financial services. 78% ของ top 50 bank โลกมี voice agent production อย่างน้อยหนึ่ง use case. AI resolution ราคาต่อ call เฉลี่ย $0.62; voice-AI $1.18; human agent $7.40. ในธุรกิจที่ contact center เป็น cost center หลัก ตัวเลขนี้เท่ากับ inevitable transition.

GPT-Live-1 ที่ราคา $0.05/นาที + latency 0.798 วิ ไม่ใช่ incremental. มันคือ moment ที่ voice agent ผ่านจาก "pilot ที่ประหยัดคน" เป็น "default channel ที่ต้องอธิบายว่าทำไมยังใช้คน". Signal ต่อจากนี้: expect voice AI market ($2.4B ในปี 2024) มุ่งเป้า $47.5B ปี 2034 (CAGR 34.8%). OpenAI ตั้ง price floor ใหม่ที่ competitor ต้องตาม — ElevenLabs, Vapi, Retell, LiveKit ต้อง reposition.

## มุม AI Agent Platform

**Builders** — Voice agent framework ที่พึ่ง pipeline STT+LLM+TTS ต้อง rethink architecture. Native full-duplex model กลายเป็น baseline. Toolset integration (function calling ระหว่างที่ผู้ใช้ยังพูด) เป็นความสามารถที่ต้อง support. **Users / business** — call center, sales BDR, appointment booking, service desk — ROI calc ใหม่ที่ต้องทำ. Voice agent ที่ช้ากว่า 1 วิเริ่มดูล้าสมัย. **Ecosystem** — telephony provider (Twilio, Vonage, Plivo) ต้อง expose realtime audio pipe ที่รองรับ streaming duplex; observability tool ต้อง handle audio traces, ไม่ใช่แค่ text.

สำหรับทีมไทย — contact center outsourcing เป็น industry ใหญ่ (BPO/CX outsourcing มีมูลค่าหลายพันล้านบาท). ปีนี้-ปีหน้าจะเห็นการ compete บน "AI-first voice" ไม่ใช่ "AI-assisted human". ธุรกิจที่ deploy voice AI เอง (retail, hospitality, healthcare) จะเห็น cost per interaction ลงหลายเท่า — แต่ต้องระวัง compliance เรื่อง PDPA และ voice consent.

## Sources
- [GPT-Live-1 arrives in the API at $0.05 a minute, OpenAI's voice model](https://pasqualepillitteri.it/en/news/15720/openai-gpt-live-1-api-voice)
- [How we built a realtime system for responsive voice AI in six months | OpenAI](https://openai.com/index/continuous-voice-interaction-with-gpt-live/)
- [OpenAI Details GPT-Live's Architecture for Continuous Stateful Voice Interaction | InfoQ](https://www.infoq.com/news/2026/09/openai-gpt-live/)

---

## Audio script
มีข่าวใหญ่จาก OpenAI ครับ เพิ่งเปิด GPT-Live-1 เข้า API ที่ราคา 5 เซ็นต์ต่อนาที — โมเดล full-duplex ตัวเดียวกับที่รัน ChatGPT Voice. Full-duplex คือมันฟังกับพูดพร้อมกัน ไม่ต้องรอ user พูดจบ. ก่อนหน้านี้ pipeline voice agent เป็น STT LLM TTS สามชั้น latency รวมกัน 1.5 ถึง 2 วินาที ทำให้บทสนทนาไม่ลื่น. GPT-Live-1 ตัดชั้นเหล่านั้นทิ้ง — latency เหลือ 0.798 วินาที ครึ่งหนึ่งของรุ่นก่อน; benchmark Tau3 กระโดดจาก 45% เป็น 86% เกือบสองเท่า. ทำไมสำคัญ? ปีที่ผ่านมา voice agent เริ่มติดในธุรกิจจริง — 78% ของ top 50 bank โลก deploy production voice agent แล้ว; voice-AI กินไป 19% ของ inbound contact center volume จากที่เคยแค่ 6% ในปี 2024. ราคาต่อ call: AI 62 เซ็นต์ voice-AI 1.18 ดอลลาร์ ส่วน human agent 7.40 ดอลลาร์. GPT-Live-1 ที่ 5 เซ็นต์ต่อนาที + latency 0.798 วิ ไม่ใช่ improvement เล็ก มันคือจุดที่ voice agent ผ่านจาก pilot เป็น default. สำหรับ builder — framework ที่ยัง STT+LLM+TTS ต้อง rethink; native duplex เป็น baseline. สำหรับธุรกิจในไทย — contact center outsourcing และ retail, hospitality ต้อง revisit ROI calc ใหม่ทั้งหมดครับ.
