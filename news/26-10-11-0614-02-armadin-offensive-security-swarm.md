---
date: 2026-10-10
slug: 26-10-11-0614
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial isometric illustration of a crimson-black control room with a floating orb labeled
  "ARMADIN" at the center, releasing a swarm of small, menacing red drone-agents that spiral
  outward toward a corporate server tower. Giant stacked labels in the sky: "+$255.5M SERIES B",
  "$2.5B VALUATION", "OFFENSIVE AGENT SWARM". Deep charcoal background, red and amber accents,
  high contrast for 200px thumbnail. 1:1 aspect ratio, no real human faces.
image: images/26-10-11-0614-02-armadin-offensive-security-swarm.png
---

# Kevin Mandia ปิด $255M ที่ $2.5B — a16z กับ Accel เท dime ลงฝั่ง "agent รุก" ไม่ใช่ "agent รับ"

## TL;DR
- 1 ต.ค. 2026 — **Armadin** ของ Kevin Mandia (ผู้ก่อตั้ง Mandiant) ปิด Series B **$255.5M ที่ valuation >$2.5B** — รอบใหญ่สุดในหมวด agent-security ปีนี้
- a16z + Accel นำร่วม, Bain Capital Ventures + Redpoint เข้าใหม่, คืนทัพรวม Google Ventures / Kleiner Perkins / Menlo / In-Q-Tel — รวม funding ~$445M
- สินค้าคือ **swarm ของ AI agent บุกเข้าระบบลูกค้าเอง** หา hole ก่อนอาชญากรจะหา — "autonomous red team as a service"; ลูกค้า Fortune 500 + รัฐบาล, ยอด ARR และจำนวนไม่เปิดเผย

## เกิดอะไรขึ้น
วันพุธที่ 1 ต.ค. **Armadin** ประกาศปิด Series B **$255.5M** ที่ valuation มากกว่า **$2.5B** — รอบใหญ่สุดในกลุ่ม agentic-security ตั้งแต่ต้นปี **Kevin Mandia** CEO (ผู้ก่อตั้ง Mandiant ที่ Google ซื้อปี 2022 ด้วยราคา $5.4B) นำบริษัทร่วมกับทีมที่ส่วนใหญ่มาจาก Mandiant/FireEye เดิม

**a16z + Accel นำร่วม** พร้อม Bain Capital Ventures และ Redpoint เข้าใหม่ นักลงทุนเดิมคืนทัพรวม **Google Ventures / Kleiner Perkins / Menlo Ventures / Ballistic Ventures / In-Q-Tel / 8VC** — รายสุดท้ายคือ VC arm ของหน่วยข่าวกรองสหรัฐ ซึ่งเป็น**ตัวบอก** ว่าลูกค้าเป้าหมายเริ่มไกลกว่า enterprise ไปทาง defense/intel ด้วย รวม funding ของ Armadin ตั้งแต่ก่อตั้ง (เพิ่งออกจาก stealth มีนาคม 2026) ตอนนี้ประมาณ **$445M**

ตัวสินค้าคือสิ่งที่ Mandia เรียกว่า **"effective autonomous security"** — swarm ของ AI agent หลายตัวประสานกันบุกเข้าระบบของลูกค้าเอง หา vulnerability + misconfiguration ก่อนอาชญากรจะเจอ ต่างจาก pentest ทั่วไปตรงที่รันต่อเนื่อง 24/7 ไม่ใช่ engagement 2 สัปดาห์แล้วจบ และต่างจาก **"blue team agent"** (SOC/SIEM augmentation ที่ Netskope, Dropzone, Prophet Security ขาย) ตรงที่ **Armadin เป็นฝ่ายรุก** — จำลองพฤติกรรม attacker จริง ไม่ใช่คัดกรอง alert

Mandia บอก Reuters ว่าบริษัทมีลูกค้า Fortune 500 และรัฐบาลใน production แล้ว แต่ **ไม่เปิดเผย ARR, จำนวนลูกค้า หรือชื่อ** — ซึ่งเป็นสัญญาณให้ระวังเล็กน้อย เพราะในหมวด cyber ตัวเลขเหล่านี้ปกติเป็น trust signal

## ทำไมสำคัญ
ตลาด cybersecurity ปี 2026 เริ่มแยกเลเยอร์ชัดขึ้น — ฝั่ง **detection + response** (CrowdStrike, SentinelOne, Palo Alto Cortex) กำลัง commoditize ด้วย AI copilot ส่วนฝั่ง **offensive / attack simulation** กลับกลายเป็นหมวดใหม่ที่ VC เท dime หนัก Armadin, HackerOne, Pentera, Horizon3 ล้วน raise ใหญ่ปีนี้ แต่ Armadin ได้ valuation และทีมที่น่ากลัวสุด เพราะ Mandia อยู่ที่ **intersection** ของสาม network — detection vendor, incident response, intel community

Mandia เองพูดชัดในหลาย fireside chat ว่า **"ถ้าคุณคิดจะใช้ AI defender, คุณต้องสมมติว่า attacker ของคุณมี AI ก่อนแล้ว"** — thesis นี้ขายได้ไหม? คำตอบคือ **ขายกับ CISO ที่มี budget จริง** — Fortune 500 + หน่วยข่าวกรองเป็นลูกค้าเริ่มต้นที่ unit economics ยอมรับได้ แต่สำหรับ mid-market หรือ SMB ที่ไม่มี blue team อยู่แล้ว การเอา autonomous red team เข้ามา**เสี่ยงกว่าได้** — เจอ hole แล้วไม่มีคนปิด

ประเด็น trust ก็ยังเปิด Armadin ไม่ประกาศ ARR, ไม่มีชื่อลูกค้า, คุณสมบัติ "autonomous" กี่ % จริง ยังไม่มี third party verify — เอกสาร pitch VC ที่สื่อ leak มาระบุว่า guardrail กับการขอ approval ก่อน exploit จริงเป็น "configurable" ซึ่งเป็นคำที่กว้างจนไม่รู้ว่าดีหรือไม่ดี

## มุม AI Agent Platform
**Builders** ที่สร้าง agent framework ควรรู้ว่า **offensive use case** กำลังเป็น segment ที่ VC จ่ายแพง — tool calling pattern, exploitation chain, lateral movement เป็น control flow ที่ complex กว่า chat agent มาก; ถ้า framework ของคุณไม่รองรับ long-horizon planning + sandboxed execution environment ตั้งแต่ day 1 segment นี้ปิดประตู

**Users / business** — CISO ไทยที่กำลังพิจารณาซื้อ attack-simulation agent ต้องถามคำถามที่ง่ายแต่สำคัญ: "ใครรับผิดชอบถ้า agent exploit production system จริงแล้วทำ downtime?" ถ้าสัญญาเขียน disclaimer ให้ลูกค้าทั้งหมด แสดงว่าเวนเดอร์ยังไม่พร้อม production deployment ที่แท้จริง

**Ecosystem** — การที่ **In-Q-Tel** (VC ของ CIA) ลงเงิน บอกว่า agentic cybersecurity กำลังเข้าสู่ **dual-use territory** — ลูกค้าของเวนเดอร์เหล่านี้จะมีทั้ง enterprise กับหน่วยงานรัฐผสมกัน ซึ่งเปลี่ยนทั้ง export control, data residency และ ethical framework; สำหรับ Thailand ที่กำลังสร้าง National Cybersecurity Agency และกฎ data sovereignty ประเด็นที่ต้องเริ่มคิดคือ "AI red team as a service" ที่สั่งซื้อจากเวนเดอร์ต่างชาติ ต้องมี **sovereign tier** หรือ on-prem option แค่ไหน ไม่งั้นจะเจอ regulatory risk ปีหน้า

## Sources
- [Armadin's $255.5M Series B Signals the Largest Agent Security Round — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/armadin-255-5m-series-b-141312980.html)
- [Kevin Mandia's Armadin Raises $255 Million at $2.5 Billion Valuation — SecurityWeek](https://www.securityweek.com/kevin-mandias-armadin-raises-255-million-at-2-5-billion-valuation/)
- [Armadin Series B Raises $255.5 Million, but Autonomous Security Still Faces a Trust Test — Remio](https://www.remio.ai/post/armadin-series-b-raises-255-5-million-but-autonomous-security-still-faces-a-trus)
- [Armadin Raises $255.5 Million Series B — PR Newswire](https://www.prnewswire.com/news-releases/armadin-raises-255-5-million-series-b-to-scale-effective-autonomous-security-302895278.html)
- [Armadin raises $255.5M at a $2.5B-plus valuation for its AI attack platform — Runtime Wire](https://runtimewire.com/article/armadin-series-b-255-million-valuation)

---

## Audio script
ข่าวที่สองวันนี้ครับ สายข่าวความปลอดภัยไซเบอร์ — Armadin บริษัทของ Kevin Mandia ผู้ก่อตั้ง Mandiant ที่ Google ซื้อไปปี 2022 ปิด Series B 255 point 5 ล้านดอลลาร์ ที่ valuation มากกว่า 2 point 5 billion นำโดย a16z กับ Accel มี Bain Capital Ventures กับ Redpoint เข้าใหม่ และคืนทัพรวม Google Ventures, Kleiner Perkins, และ In-Q-Tel ซึ่งเป็น VC ของ CIA ครับ

สินค้าของ Armadin ไม่ใช่ security copilot แบบที่เราคุ้นเคย แต่คือ swarm ของ AI agent ที่บุกเข้าระบบของลูกค้าเองเพื่อหาช่องโหว่ก่อนอาชญากรจะเจอ — autonomous red team as a service ที่รัน 24 ชั่วโมง 7 วันไม่หยุด ต่างจากการจ้าง pentest ปกติที่เป็น engagement 2 สัปดาห์แล้วจบ Mandia บอกว่าถ้าคุณคิดจะใช้ AI defender คุณต้องสมมติว่า attacker ของคุณมี AI ก่อนคุณแล้ว — thesis นี้ขายได้กับ Fortune 500 กับหน่วยข่าวกรอง แต่สำหรับ mid-market หรือ SMB ที่ไม่มี blue team อยู่แล้วการเอา autonomous red team เข้ามาอาจเสี่ยงกว่าได้ เจอรูแล้วไม่มีคนปิด

ประเด็นที่น่าสนใจคือ Armadin ไม่เปิดเผย ARR ไม่มีชื่อลูกค้า และ guardrail กับการขอ approval ก่อน exploit จริงยังเป็น configurable ซึ่งเป็นคำที่กว้างจนไม่รู้ว่าดีหรือไม่ดี สำหรับ CISO ไทยที่กำลังพิจารณาซื้อ attack-simulation agent คำถามที่ต้องถามคือ ใครรับผิดชอบถ้า agent exploit production system จริงแล้วทำ downtime และสำหรับหน่วยงานรัฐไทยที่กำลังสร้าง data sovereignty regulation การที่ VC ของ CIA ลงทุนในหมวดนี้ชี้ว่า agentic cybersecurity กำลังเข้าสู่ dual-use territory ที่ regulatory risk ต้องเริ่มคิดตั้งแต่ตอนนี้ครับ
