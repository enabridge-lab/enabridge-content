---
date: 2026-08-08
slug: omilia-67m-series-b-voice-agent-60m-arr-bank-1m-calls
topic: use-case
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial isometric illustration of a huge glowing customer service
  headset on a pedestal labeled "OMILIA VOICE AI"; behind it, a phone call
  waveform curls into a bank building silhouette tagged "TIER 1 US BANK".
  Three large stat cards float around: "1,000,000 CALLS / DAY", "$60M ARR"
  (with an upward arrow "10x"), and "45ms LATENCY, 25 LOCALES". Below,
  five small brand tiles labeled "CAPITAL ONE", "DISCOVER", "RBC", "TACO
  BELL", "PSEG". Teal + coral palette, grid floor, editorial isometric
  style, 1:1 aspect, no real human faces, text sharp at 200px thumbnail.
image: images/26-08-08-0613-03-omilia-67m-series-b-voice-agent-60m-arr-bank-1m-calls.png
---

# Omilia $67M Series B: voice agent ที่รับสาย 1 ล้าน call/วัน ที่ธนาคาร Tier 1 สหรัฐ, ARR 10x เป็น $60M — voice = production-grade แล้ว

## TL;DR
- **6 ส.ค.** — Omilia (Cyprus, 2003) ปิด **Series B $67M** (€58.1M) นำโดย Expedition Growth Capital — เพื่อเปิดออฟฟิศ US ครั้งแรกครึ่งหลังปี 2026
- **ตัวเลขที่พิสูจน์ scale voice agent** — **live ARR โต 10x จาก Series A** เป็น **$60M+**; **200+ enterprise deployment**; **Tier 1 US bank รับ 1 ล้าน call/วัน**; ลูกค้าอ้างอิง: Capital One, Discover, RBC, Taco Bell, DWP (UK gov), PSEG
- **Product timing** — 8 ก.ค. เพิ่ง launch **Lexis** — generative TTS model native บน Cloud Platform, **latency <45ms** ครอบ 25 locale (ทำ full-duplex conversation แทน turn-based)
- **มุม Agent Platform** — Voice-first vertical agent เข้าโซน "**agent ที่ทำงานได้จริง มีตัวเลข customer + revenue**" ที่ text-based general assistant ยังทำไม่ถึงในระดับ enterprise. ตลาด CCaaS (Cisco, Genesys, NICE, Five9) กำลังถูก reshape

## เกิดอะไรขึ้น

วันพุธที่ 6 สิงหาคม Omilia — บริษัท voice AI ที่ก่อตั้งใน Cyprus ปี 2003 (ให้ค่อย ๆ scale ก่อนคำว่า "AI agent" จะกลาย mainstream) — ปิด **Series B $67M** นำโดย Expedition Growth Capital. Series A เมื่อ 3 ปีที่แล้วปิดที่ระดับ live ARR ~$6M — วันนี้ Omilia รายงาน **live ARR $60M+**, โตประมาณ **10x**. Capital ครั้งนี้จะ fund การเปิด **office US แห่งแรก** ในครึ่งหลังปี 2026 (Boston/NY) + ขยาย engineering + go-to-market team ในภูมิภาค

Product portfolio ของ Omilia = **agentic self-learning CX platform** — voice-first customer service agent ที่รับสายเข้า, จัดการ intent complex (KYC verify, dispute, refund, policy change), transfer ไป human เฉพาะกรณีที่ agent ตัดสินว่าต้อง escalate. 200+ enterprise deployment ครอบ industry ที่ compliance สูง: **banking (Capital One, Discover, RBC), telecom, government (DWP UK), utility (PSEG), retail (Taco Bell)**. Highlight ที่ Rafael Cortés (CEO) วางในการ pitch — **Tier 1 US bank ใช้ Omilia จัดการ 1 ล้าน call/วัน** — ตัวเลขที่ CCaaS incumbent (Cisco, Genesys, Five9, NICE) ต้องหยุดคิด: agent voice ระดับนี้ผ่านการ compliance ของธนาคารระดับสูงสุดในสหรัฐได้จริง

**Product timing ที่รับ round นี้** — 8 กรกฎาคม Omilia ship **Lexis**, generative TTS model native ที่ **latency <45ms** ครอบ 25 locale — ตัวเลขที่ทำให้ full-duplex conversation (agent+user พูดทับได้) เป็นไปได้ในระดับ production. เทียบกับ ElevenLabs / OpenAI TTS ที่ latency 200-400ms และไม่ค่อย native กับ ASR + dialog manager — Omilia เดิน vertical integration ทั้ง stack (ASR → NLU → dialog → TTS) ซึ่งเป็น thesis ที่ทำให้ enterprise voice agent ทำงานจริงในโครง SLA <2s ต่อ turn ที่ธนาคารต้องการ

## ทำไมสำคัญ

**Voice agent ผ่านจุดที่ CFO เชื่อได้แล้ว.** ตลอด 3 ปีที่ผ่านมา voice AI มี demo สวยแต่ metric ในองค์กรจริงไม่ค่อยผ่าน: containment rate 20-30% (แปลว่า 70-80% ยังต้อง route ไป human), CSAT drop 5-10 point เทียบกับ human agent. Omilia $60M ARR + 200 deployment + Tier 1 bank ที่ปล่อยให้จัดการ **1 ล้าน call/วัน** = signal ว่า **containment 60-70% + CSAT parity หรือดีกว่า** เป็นไปได้ในระดับ production. อาจไม่ใช่ Anthropic-scale story, แต่เป็น **"quiet compounding vertical agent"** ที่ enterprise ซื้อจริง

**อุตสาหกรรม CCaaS $30B (Cisco, Genesys, NICE, Five9, Talkdesk) กำลังถูก reshape จาก 2 ทิศ**: (1) **voice-native AI vendor** อย่าง Omilia, Sierra (Bret Taylor, $10B valuation reported มีนา 2026), PolyAI, Cresta ที่มาจาก AI-first — build stack ใหม่ทั้งท่อ; (2) **CCaaS incumbent** ที่ retrofit ด้วย GenAI (Genesys Cloud AI, NICE Enlighten, Five9 Genius) — มี distribution ที่ AI-first ยังไม่มี. Omilia $67M round + US expansion = strategy หนึ่ง: **land ที่ enterprise level ก่อน incumbent ปรับตัว**. Sierra เดิน strategy คล้ายกันด้วย founder brand + Bay Area lead investor. Cresta ยึด contact center agent-assist (co-pilot) ก่อนขยับไป full autonomy. **จบเกม** = 2-3 ปีข้างหน้าจะเห็น consolidation — incumbent ซื้อ AI-first (Genesys ซื้อ Cresta? NICE ซื้อ PolyAI?) หรือ AI-first IPO แล้วซื้อ CCaaS แบบ inverse merger

**Signal สำหรับ Thai market**: contact center outsourcer (Datamining, True Contact Center, AIS Contact Center, K-Contact) กำลังถูก enterprise ลูกค้าถามเรื่อง AI voice agent — Omilia ยังไม่มี Thai locale ใน Lexis (25 locale ที่ launch), แต่ **PolyAI / Cresta / homegrown Thai voice AI (Amity Voice, Vulcan, KMUTT Speech Lab spinoff) จะได้ momentum** จากเคสที่ Omilia สร้าง proof point ระดับโลก. Enterprise ที่เคยตอบ "voice AI ยังไม่พร้อม" 2 ปีที่แล้ว จะเริ่มเปิด pilot Q4 2026 - Q1 2027

## มุม AI Agent Platform

**สำหรับ builders:** ถ้า build voice AI vertical (financial services, healthcare, telco, retail) — **latency + full-duplex + locale coverage คือ moat จริง**. Omilia ใช้เวลา 20+ ปี integrate ASR/NLU/TTS ที่ latency <45ms ครอบ 25 locale = ไม่ใช่สิ่งที่ startup 6 เดือน replicate ได้แม้จะมี Anthropic + OpenAI API. Path ที่เป็นจริงสำหรับ AI voice startup ใหม่: (a) **specialize ที่ narrow vertical** (dental office, veterinary clinic, small law firm) ที่ Omilia/Sierra ยังไม่ down-market ถึง; (b) **build on top of foundation** (ElevenLabs TTS + OpenAI Realtime API + Vapi/Retell orchestrator) + ขาย distribution + workflow; (c) **specialize locale** ที่ big vendor ยัง underserved (Thai, Vietnamese, Bahasa, Filipino). ห้าม compete โดยตรงกับ Omilia บน English + banking

**สำหรับ users/business:** Contact center leader — **ถ้ายัง defer AI voice pilot เกิน Q1 2027 = ตกกลุ่มที่ compete cost/service ไม่ได้**. Checklist ที่ CX head + ops ต้องเช็ค: (1) **containment rate benchmark** — vendor คนไหน commit >60% ในภาษาที่คุณต้องการ? (2) **latency SLA** — <500ms ต่อ turn สำหรับ conversational, <2s สำหรับ complex? (3) **compliance layer** — audit log format compatible กับ regulator (BOT, TDRA, กสทช.)? (4) **integration cost** — connect กับ CRM (Salesforce, Zendesk, MS Dynamics) + core banking / policy admin กี่เดือน? (5) **escalation policy** — เมื่อ agent ตัดสินว่าต้อง handoff, ใครรับ + context transfer สมบูรณ์ไหม? Thai bank ที่ pilot ตอนนี้ (KBTG, SCB 10X, TMBThanachart) ควร evaluate **PolyAI (English-native, Thai roadmap)** vs. **Amity Voice / KMUTT-derived** (Thai-native) ในความเร็วต่างกัน — non-Thai vendor เร็วในการ deploy, Thai-native แม่นในการเข้าใจสำเนียงและ context

**สำหรับ ecosystem:** **Winner:** vertical voice AI ที่ deployed จริง (Omilia, Sierra, PolyAI, Cresta), TTS foundation ที่รองรับ enterprise SLA (Lexis, ElevenLabs Enterprise, Cartesia), CCaaS incumbent ที่ retrofit เร็วพอ (Genesys). **Loser:** CCaaS ที่ยัง sell "AI-ready" แต่ไม่ commit metric, human BPO ที่ไม่มี augmentation layer. **Enabridge angle:** ตำแหน่งที่ Thai integrator ควรเล่นคือ **"voice agent implementation partner"** — ช่วย Thai enterprise (bank, insurance, telco, utility) evaluate + integrate voice AI vendor + design escalation + measure containment KPI ใน 90 วัน. เป็น service line ที่ margin สูง (project-based + retainer), timing เหมาะ (proof point ระดับโลก Omilia + Sierra สร้างแล้ว, Thai buyer เริ่มเปิดเงิน), และ **Enabridge ที่ manage integration หลาย backend ได้จะได้เปรียบ SI ทั่วไป**

## Sources
- [Omilia raises $67M to scale its customer support platform — TechCrunch](https://techcrunch.com/2026/08/06/omilia-raises-67m-to-scale-its-customer-support-platform/)
- [Omilia Secures $67M in Series B Funding — Business Wire](https://www.businesswire.com/news/home/20260806641060/en/Omilia-Secures-%2467-Million-in-Series-B-Funding-to-Accelerate-Global-Expansion-of-Its-Agentic-Self-Learning-CX-Platform-for-Large-Enterprises)
- [Omilia Secures $67M Series B to Expand U.S. Voice AI — CMSWire](https://www.cmswire.com/customer-experience/omilia-raises-67m-series-b-for-voice-ai-push/)
- [Cyprus-based Omilia secures €58.1M in Series B — EU-Startups](https://www.eu-startups.com/2026/08/cyprus-based-enterprise-agentic-cx-company-omilia-secures-e58-1-million-in-series-b-funding)
- [Omilia Raises $67M Series B to Expand Enterprise Agentic AI Platform — citybiz](https://www.citybiz.co/article/885138/omilia-raises-67-million-series-b-to-expand-enterprise-agentic-ai-platform/)
- [Voice-First CX Platform Omilia Raises $67M Series B — WOWTALE](https://en.wowtale.net/2026/08/07/234637/)

---

## Audio script
วันพุธที่ 6 สิงหาคม Omilia บริษัท voice AI จาก Cyprus ก่อตั้งปี 2003 ปิด Series B 67 ล้านดอลลาร์ นำโดย Expedition Growth Capital. เงินก้อนนี้ใช้เปิดออฟฟิศแรกในสหรัฐครึ่งหลังปี 2026. ตัวเลขที่พิสูจน์ scale คือ live ARR โต 10 เท่าจาก Series A เป็น 60 ล้านดอลลาร์ 200 enterprise deployment ลูกค้ามี Capital One Discover RBC Taco Bell DWP ของรัฐบาล UK และ PSEG. Highlight ใหญ่คือ Tier 1 US bank ใช้ Omilia จัดการ 1 ล้าน call ต่อวัน.

Product timing ที่รับ round นี้ 8 กรกฎาคม Omilia ship Lexis generative TTS model latency ต่ำกว่า 45 มิลลิวินาที ครอบ 25 locale ทำให้ full duplex conversation เป็นไปได้ในระดับ production. เทียบกับ ElevenLabs หรือ OpenAI TTS ที่ latency 200 ถึง 400 มิลลิวินาที Omilia เดิน vertical integration ทั้ง stack ASR NLU dialog TTS ซึ่งเป็น thesis ที่ทำให้ enterprise voice agent ผ่าน SLA ต่ำกว่า 2 วินาทีต่อ turn ที่ธนาคารต้องการ.

Signal ใหญ่คือ voice agent ผ่านจุดที่ CFO เชื่อได้แล้ว 3 ปีก่อน voice AI มี demo สวยแต่ containment rate 20 ถึง 30 เปอร์เซ็นต์ CSAT drop 5 ถึง 10 point. วันนี้ Omilia 60 ล้าน ARR 200 deployment Tier 1 bank ปล่อยให้จัดการ 1 ล้าน call ต่อวัน หมายความว่า containment 60 ถึง 70 เปอร์เซ็นต์ CSAT parity หรือดีกว่าเป็นไปได้ในระดับ production.

CCaaS 30 พันล้านดอลลาร์ ตลาด Cisco Genesys NICE Five9 Talkdesk กำลังถูก reshape จาก voice native AI vendor Omilia Sierra PolyAI Cresta และ CCaaS incumbent ที่ retrofit ด้วย GenAI. 2 ถึง 3 ปีข้างหน้าจะเห็น consolidation.

สำหรับ Thai market Omilia ยังไม่มี Thai locale แต่ PolyAI Cresta หรือ Amity Voice Vulcan KMUTT Speech Lab spinoff จะได้ momentum. Enterprise ที่เคยตอบว่า voice AI ยังไม่พร้อม 2 ปีก่อน จะเริ่มเปิด pilot Q4 2026 ถึง Q1 2027. สำหรับ Enabridge ตำแหน่งที่ Thai integrator ควรเล่นคือ voice agent implementation partner ช่วย Thai bank insurance telco utility evaluate integrate voice AI vendor design escalation policy measure containment KPI ใน 90 วัน. เป็น service line ที่ margin สูง timing เหมาะ proof point Omilia และ Sierra สร้างแล้ว.
