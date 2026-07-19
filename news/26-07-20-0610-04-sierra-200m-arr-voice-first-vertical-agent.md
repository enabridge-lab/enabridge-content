---
date: 2026-07-20
slug: sierra-200m-arr-voice-first-vertical-agent
topic: use-case
reading_time_min: 3
sources: 3
image_prompt: |
  An editorial illustration showing a stylized customer service floor split
  in two — the left half is a shrinking traditional call center with empty
  desks and a sign "TEXT · LEGACY", the right half is a glowing wave-based
  voice interface with sound waves rippling outward and a big number
  "$200M ARR" floating above it, labeled "SIERRA · VOICE-FIRST". At the top
  a ribbon reads "40% OF FORTUNE 50". The Sierra glyph mark (simple mountain
  silhouette) sits in the top-right. Editorial isometric style, warm sunset
  gradient, high contrast, 1:1 aspect, no real human faces.
image: images/26-07-20-0610-04-sierra-200m-arr-voice-first-vertical-agent.png
---

# Sierra ทะลุ $200M ARR — voice agent แซง text, ปิดดีล 40% ของ Fortune 50

## TL;DR
- Sierra AI แตะ $200M ARR ในเดือน พ.ค. 2026 จาก $130M ปลายปี 2025 และ $26M ปลายปี 2024 — 7x โตในปีเดียว
- Voice agent overtake text แล้ว ในฐานะ primary interaction channel — คาด power "หลายร้อยล้าน call" ในปีนี้
- Post-money valuation $15.8B, ให้บริการ 40%+ ของ Fortune 50, "billions of customer interactions" — case study ที่ vertical agent เอาชนะ horizontal SaaS ได้แบบชัดที่สุดใน CX

## เกิดอะไรขึ้น
Sierra บริษัท customer experience agent ที่ก่อตั้งโดย Bret Taylor (อดีต co-CEO Salesforce, เพิ่งเป็น board chair OpenAI) กับ Clay Bavor (อดีต Google VP) เผยตัวเลขล่าสุดเมื่อสัปดาห์ที่แล้ว: **$200M ARR ตอนพฤษภาคม 2026** — โต 7 เท่าใน 12 เดือน. ต้นปี 2024 อยู่ที่ $26M, ปลาย 2025 ที่ $130M, และเพิ่งเพิ่มอีก $100M ARR ในสองไตรมาสหลังสุด. Sierra รับเงิน Series E $950M เมื่อ พ.ค. นำโดย GV กับ Tiger Global, มี Benchmark, Sequoia, Greenoaks ร่วม — ปิดที่ post-money valuation $15.8B.

ที่น่าสนใจกว่า ARR คือการ shift channel: **voice agent ของ Sierra แซง text แล้ว** ในการเป็น primary interaction channel ตั้งแต่ ต.ค. 2025, ตอนนี้กำลัง power หลายร้อยล้าน AI call ในปี 2025 และแนวโน้มจะขึ้นเป็น billion ใน 2026. ลูกค้ารวมถึง Sonos, WeightWatchers, ADT, SoFi, Ramp, Casper — และเพิ่งประกาศเข้า 40%+ ของ Fortune 50. เม็ดเงินระดม Series E จะถูก allocate ไปที่ Agent OS (การ deploy agent ให้ non-technical team ใช้ได้), AI-driven agent improvement (agent ปรับตัวจาก feedback อัตโนมัติ), และขยายเข้า sales + engagement workflow — ไม่ใช่แค่ customer support อีกต่อไป.

Bret Taylor พูดใน interview สัปดาห์นี้: "Seat-based SaaS คือ pricing model ของยุคที่ software เป็น tool ให้คน — เมื่อ agent ทำงานเอง, การ charge ตาม seat ไม่ make sense อีก. เรา charge ตาม outcome — ticket resolved, call completed, refund processed." Sierra pricing เป็น per-completed-conversation range $0.50-$5 ขึ้นกับ complexity.

## ทำไมสำคัญ
$200M ARR จาก $26M ใน 18 เดือนเป็นเลขที่บอกอะไรหลายอย่าง — แต่ที่สำคัญที่สุดคือ **outcome pricing ทำงานจริงในระดับ enterprise**. หลายสิบปีที่ SaaS ขายเป็น per-seat มี unwritten assumption: value = seat count = productivity. Agent economy break assumption นี้: value = work completed = business outcome. Sierra pricing 50 cent - 5 dollar ต่อ conversation ที่ปิดจบ — ลูกค้ารู้ ROI ทันที ไม่ต้องพิสูจน์ผ่าน "seat utilization survey".

Signal ที่สอง — voice overtake text — น่าจับตากว่าตัวเลข ARR. เมื่อ 3 ปีก่อน, "voice AI" คือ IVR ที่พูดตอบไม่ค่อยตรง. ตอนนี้ voice agent ของ Sierra + คู่แข่ง (PolyAI, Retell, Vapi, ElevenLabs Conversational, Rime) latency ต่ำกว่า 300ms, interruption handling ดีกว่ามนุษย์ที่เพิ่งเข้างาน, และรองรับ 15+ ภาษาแบบ real-time. Cars24 อินเดีย (เคยเป็น case study ในสัปดาห์ก่อน) ปิดกว่า 1M นาที voice call ต่อวันด้วย OpenAI Realtime. Voice จะกลายเป็น default channel ของ agent ก่อน text ใน vertical ที่ user มือใหญ่มัก drop-off ที่ typing form — sales, healthcare intake, insurance FNOL, field service dispatch.

ประเด็นที่สาม — **40% ของ Fortune 50** เป็น penetration rate ที่ SaaS category ทั่วไปใช้เวลา 8-10 ปีสร้าง (Salesforce, ServiceNow, Workday). Sierra ทำใน 3 ปี. นี่คือ signal ว่า vertical agent ที่โฟกัส workflow เดียวลึก (CX) เอาชนะ horizontal platform ที่พยายามทำทุกอย่างได้ในตลาด enterprise ที่ decision maker เจ็บด้วย เรื่องเดิม ๆ ทุกวัน — call ล้น, agent turnover, CSAT ต่ำ, cost per contact สูง.

## มุม AI Agent Platform
สำหรับ **builders** ที่กำลังสร้าง vertical agent: model ธุรกิจของ Sierra ควรเป็น reference — sell outcome (per-resolution / per-completion), integrate ลึกในระบบลูกค้า (Salesforce, Zendesk, telephony, warehouse), และ optimize latency + accuracy ใน narrow workflow แทนที่จะโชว์ generality. Voice-first เป็น differentiator แข็ง — ถ้า vertical ของคุณ (healthcare, financial services, field service, hospitality) mostly voice-driven, สร้าง voice-native ตั้งแต่ต้นดีกว่าติด voice on top text agent ทีหลัง.

สำหรับ **users / business** ที่จะ deploy agent สาย CX: ประเมิน vendor 3 มิติ — (1) outcome pricing มีจริงไหม หรือ dressed-up seat pricing, (2) voice + text + web + mobile รวมกันเป็น experience เดียวไหม, (3) มี "Agent OS" ให้ CX team ตัวเองปรับ prompt/policy ได้ หรือต้องส่ง ticket ให้ vendor แก้. สำหรับ **ecosystem**: incumbent CX platform (Salesforce Service Cloud, ServiceNow CSM, Zendesk, Freshdesk) มีเวลาไม่มาก — Agentforce กับ ServiceNow AI Agents พยายามอยู่ แต่ยังขาย seat + implementation service เป็นหลัก. Bret Taylor รู้ playbook ของ Salesforce ดี — เขากำลังโจมตี business model เดิมของบริษัทเก่าตัวเอง.

## Sources
- [Sierra revenue, valuation & funding (Sacra)](https://sacra.com/c/sierra/)
- [TechCrunch: Sierra raises $950M as the race to own enterprise AI gets serious](https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/)
- [Sierra Revenue 2026: $200M ARR, $15.8B Valuation (Getlatka)](https://getlatka.com/companies/sierra)

---

## Audio script
ข่าวจาก Sierra ครับ บริษัท customer experience agent ของ Bret Taylor อดีต co-CEO Salesforce เผยตัวเลขล่าสุด แตะ 200 ล้านดอลลาร์ ARR ในเดือนพฤษภาคม โตจาก 26 ล้านปลายปี 2024 130 ล้านปลายปี 2025 มาที่ 200 ล้านตอนกลางปีนี้ 7 เท่าใน 12 เดือน post-money valuation อยู่ที่ 15.8 พันล้านดอลลาร์ จากการระดม Series E 950 ล้านเมื่อพฤษภา ลูกค้าครอบคลุม 40 เปอร์เซ็นต์ของ Fortune 50 มี Sonos, WeightWatchers, ADT, SoFi, Ramp, Casper ที่น่าสนใจกว่า ARR คือ voice agent ของ Sierra แซง text แล้วในการเป็น primary channel ตั้งแต่ตุลาปีที่แล้ว กำลัง power หลายร้อยล้าน call ต่อปี ทำไมสำคัญ ผมมองว่านี่คือหลักฐานว่า outcome pricing ทำงานจริงในระดับ enterprise Sierra charge 50 เซนต์ ถึง 5 ดอลลาร์ ต่อ conversation ที่ปิดจบ ลูกค้ารู้ ROI ทันที ไม่ต้องพิสูจน์ผ่าน seat utilization survey Bret Taylor บอกตรงๆ ว่า seat based pricing คือ model ของยุคที่ software เป็น tool ให้คน เมื่อ agent ทำงานเอง ต้อง charge ตาม outcome signal ที่สองคือ voice overtake text 3 ปีก่อน voice AI คือ IVR ตอบไม่ค่อยตรง ตอนนี้ latency ต่ำกว่า 300 มิลลิวินาที รองรับ 15 ภาษา real time voice จะกลายเป็น default channel ก่อน text ใน vertical ที่ user drop off ที่ typing form sales healthcare insurance field service ประเด็นที่สาม 40 เปอร์เซ็นต์ของ Fortune 50 เป็น penetration rate ที่ Salesforce ใช้เวลา 8-10 ปีสร้าง Sierra ทำใน 3 ปี นี่คือ signal ว่า vertical agent ที่โฟกัส workflow เดียวลึกๆ ชนะ horizontal platform ในตลาดที่ decision maker เจ็บด้วยเรื่องเดิมๆ ทุกวัน Bret Taylor รู้ playbook ของ Salesforce ดีมาก เขากำลังโจมตี business model ของบริษัทเก่าตัวเองครับ
