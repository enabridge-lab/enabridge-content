---
date: 2026-11-04
slug: palo-alto-clutch-500m-non-human-identity
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a giant translucent gate labeled
  "NON-HUMAN IDENTITY" with silhouettes of robot agents queuing to pass.
  A security scanner reads keys and tokens floating over each agent's head
  (labeled "API KEY", "SERVICE ACCOUNT", "AGENT TOKEN"). A massive price
  tag hovers above: "$500M". Smaller sign reads "CYBERARK $25B · HUMANS",
  with an arrow pointing to the scanner: "CLUTCH · MACHINES + AGENTS".
  Editorial style, cool slate-blue and warm amber palette, 1:1 aspect, no
  real human faces, high contrast for 200px thumbnail.
image: images/26-11-06-0605-04-palo-alto-clutch-500m-non-human-identity.png
---

# Palo Alto จ่อ $500M ซื้อ Clutch — non-human identity กลายเป็นตลาดจริง หลัง CyberArk $25B ปูทาง

## TL;DR
- Palo Alto Networks รายงานกำลังเจรจาซื้อ Clutch Security ที่ประมาณ $500M — ยังไม่ signed แต่ The Information รายงาน Nov 4
- Clutch ตั้งปี 2023 ที่ Israel จัดการ credential ของ non-human identity (API key, service account, agent token) — ระดมมากกว่า $20M จาก Lightspeed, SignalFire
- ตามหลังดีล CyberArk $25B ที่ Palo Alto ปิดก่อนหน้า — strategic คือ "มนุษย์ที่ CyberArk, เครื่องและ agent ที่ Clutch"

## เกิดอะไรขึ้น
วันที่ 4 พฤศจิกายน The Information รายงานว่า Palo Alto Networks กำลังเจรจาซื้อ Clutch Security ที่ประมาณ 500 ล้านเหรียญ — ดีลยังไม่ signed Palo Alto ไม่ comment ตามนโยบายเรื่อง rumor Clutch ก็ไม่ตอบ request for comment ถ้าปิดจริงนี่จะเป็นการ acquisition ที่ 5 ของ Palo Alto ในปี 2026

Clutch เป็น startup Israel ที่ตั้งปี 2023 โดย Ofir Har-Chen (อดีต Cybereason) ทำ platform สำหรับจัดการ non-human identity (NHI) — ครอบคลุม API key, service account, token, machine credential, และ ที่สำคัญคือ credential ที่ AI agent ใช้เพื่อ access ระบบ Platform ของ Clutch ทำได้ 4 อย่างหลัก คือ discovery (หา credential ที่ไหน), governance (จัดการ permission), protection (vault + rotation), และ detection (anomaly ใน usage) — ระดมเงินมากกว่า $20M จาก Lightspeed, SignalFire, และ Merlin Ventures

Strategic positioning น่าสนใจ — Palo Alto เพิ่งปิดดีล CyberArk ที่ $25 พันล้านเมื่อต้นปีซึ่งโฟกัส human privileged access (admin password, PAM) Clutch ที่โฟกัส machine และ agent identity ไม่ overlap กับ CyberArk โดยตรง — เป็น complementary ที่ Palo Alto ต้องการเพื่อขายความเป็น "identity vendor ที่ครอบจักรวาล" ให้ enterprise buyer

สิ่งที่ตลาดคิดอยู่ตอนนี้ — nhi ไม่ใช่ตลาดใหม่ แต่ปริมาณ non-human identity ใน enterprise เพิ่มขึ้น 10-50 เท่าในช่วง 2 ปีที่ผ่านมา เพราะ AI agent แต่ละตัวต้องมี credential เพื่อเรียก API, database, SaaS tool — enterprise ขนาดใหญ่มี NHI หลักแสนถึงล้าน credential ต่อ human identity 1 คน จำนวนแบบนี้ไม่มีทางจัดการด้วย process เดิม

## ทำไมสำคัญ
ถ้าดีลนี้ปิดราคานี้ Clutch จะ exit ที่ ~25x revenue คาดการณ์ (ปี 2025 revenue ยังไม่ถึง 20M ตาม trade press) — เป็น premium multiple ที่สะท้อนว่า Palo Alto มองว่า NHI + agent identity เป็น strategic category ไม่ใช่ feature ที่ซื้อแยกได้ ทีนี้ตลาด NHI มี ผู้แข่งขันหลายราย — Astrix, Oasis Security, Entro Security, Natoma — ทุกรายจะถูก revalue ขึ้น

Pattern ที่สะท้อนเรื่องนี้คือ identity-as-core-security — ปี 2010 security = network, ปี 2015 = endpoint, ปี 2020 = cloud, ปี 2025-2026 กำลังเป็น identity โดยเฉพาะ non-human ที่ปริมาณระเบิดขึ้นเพราะ agent ถ้า theory นี้ถูก Microsoft Entra, Okta, Ping จะต้องตอบกลับ — รอดูว่าใครจะซื้อ Astrix หรือ Oasis เป็นรายถัดไป

Caveat หลัก — ดีลยังไม่ signed The Information แค่รายงานเจรจา บางทีจบด้วย price ต่างหรือ fall through ได้ Palo Alto's stock ลงวันเดียวกับ Fortinet ที่ sell-off หลัง earnings ถ้า Palo Alto Q1 FY27 earnings 18 พย ออกมาไม่ดี พวกเขาอาจจะชะลอดีล — การ fund 5 ดีลในปีเดียวต้อง justify กับ nvestor

## มุม AI Agent Platform
Builders — ถ้าคุณสร้าง agent framework คำถาม "credential ของ agent เก็บยังไง rotate ยังไง" จะกลายเป็น hygiene requirement ใน 6-12 เดือน เหมือน TLS ที่ครั้งหนึ่งเคยเป็น premium แต่ตอนนี้ default — plan ล่วงหน้าว่าจะ integrate กับ NHI vendor ไหน หรือ build vault layer ของตัวเอง ไม่ใช่ปล่อย hardcoded token ใน config

Users/business — ถ้าคุณ deploy agent หลายตัวใน production ปัญหา credential sprawl ของคุณใหญ่ขึ้นเร็วมาก — ลองนับว่ามีเท่าไหร่ก่อน buy platform แล้วตั้งว่าจะต้องการ discovery ที่ auto ก่อน governance Enabridge ที่สร้าง agent platform ให้ลูกค้า ควร include NHI management as default — ไม่ใช่ feature add-on

Ecosystem — ภายในปี 2027 คาดว่า identity vendor ใหญ่ทุกรายต้อง มี NHI/agent story — Okta ที่เพิ่งเปิด "Agent Identity" เมื่อ Q3 จะต้องประกาศ acquisition ตามถ้าไม่ใช่ organic growth ที่พิสูจน์แล้ว — Microsoft Entra ที่เริ่ม preview "Workload Identity Federation for Agents" เมื่อ Ignite ปี 2025 จะต้อง GA ภายในปีนี้ตลาด NHI กำลังเข้า land-grab phase

## Sources
- [Palo Alto Networks in talks to buy Clutch Security for $500m (Globes)](https://en.globes.co.il/en/article-palo-alto-networks-in-talks-to-buy-clutch-security-for-500m-1001562156)
- [Palo Alto in Talks to Buy AI-Agent Startup Clutch for $500M (AI Weekly)](https://aiweekly.co/alerts/palo-alto-in-talks-to-buy-ai-agent-startup-clutch-for-500m)
- [Palo Alto Networks Isn't Done Shopping (Benzinga)](https://www.benzinga.com/m-a/26/11/62908280/palo-alto-networks-isnt-done-shopping-500-million-ai-security-deal-could-be-next)
- [Palo Alto Networks Weighs $500M Purchase of AI Credential Startup Clutch (BigGo)](https://finance.biggo.com/news/48f4d52c-30c2-42d0-a4b6-93aae9cf7154)

---

## Audio script
The Information รายงานเมื่อวันที่ 4 พฤศจิกายนว่า Palo Alto Networks กำลังเจรจาซื้อ Clutch Security ที่ประมาณห้าร้อยล้านเหรียญ ดีลยังไม่ signed Palo Alto ไม่ comment ตามนโยบาย Clutch เป็น startup Israel ตั้งปี 2023 ทำ platform จัดการ non-human identity ครอบคลุม API key, service account, token, และที่สำคัญคือ credential ที่ AI agent ใช้ Platform ทำได้สี่อย่างคือ discovery ว่า credential อยู่ไหน governance ว่าใครมี permission อะไร protection ด้วย vault และ rotation และ detection ของ anomaly ระดมเงินมามากกว่า 20 ล้านจาก Lightspeed และ SignalFire ที่น่าสนใจคือ Palo Alto เพิ่งปิดดีล CyberArk ที่ 25 พันล้านซึ่งโฟกัส human privileged access ส่วน Clutch โฟกัสเครื่องและ agent — เป็น complementary ที่ Palo Alto ต้องการขายเป็น identity vendor ครบวงจร pattern ที่ชัดเจนคือ ปริมาณ non-human identity ใน enterprise เพิ่ม 10 ถึง 50 เท่าในสองปีที่ผ่านมา เพราะทุก agent ต้องมี credential สำหรับคนที่สร้าง agent framework คำถาม credential เก็บยังไง rotate ยังไง จะกลายเป็น hygiene requirement ใน 6 ถึง 12 เดือน เหมือน TLS ที่เคยเป็น premium แต่ตอนนี้เป็น default สำหรับ business ที่ deploy agent หลายตัว ลองนับก่อนว่า credential sprawl ของตัวเองใหญ่แค่ไหน แล้วเลือก platform ที่ discovery อัตโนมัติก่อน governance
