---
date: 2026-10-19
slug: opsin-21m-ai-agent-security
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  Editorial isometric illustration of a glowing control tower overlooking
  a sprawling industrial park where small AI agent silhouettes wander
  between buildings labeled "COPILOT", "CLAUDE", "GEMINI", "CHATGPT".
  Three giant numbers hover beside the tower: "93% UNRESTRICTED",
  "1 IN 200 HUMAN APPROVAL", "$21M". A banner on the tower reads "OPSIN
  RISK GRAPH". Deep cobalt and warm amber palette, high contrast for
  200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-19-0604-02-opsin-21m-ai-agent-security.png
---

# Opsin ปิด $21M คุม agent sprawl — 93% ของ tool ที่ agent connect อยู่ "ไม่มี gate" ให้ human approve เลย

## TL;DR
- 15 ต.ค. **Opsin** (San Jose, AI agent security) ปิดรอบ **$21M** นำโดย **SYN Ventures + Race Capital** — ไม่เปิด valuation, ไม่บอก round stage ชัด (บริษัทเคย raise seed $7M ปี 2025)
- Product: **Risk Graph** ที่ join agent identity + intended purpose + permission + observed activity. Action: restrict, quarantine, หรือ notify owner. Visibility: Copilot, Claude, ChatGPT Enterprise, Gemini + tool อนุมัติอื่น ๆ
- Data ที่ Opsin เอง publish: **93%** ของ tool ที่ connect กับ agent มี "unrestricted access" ต่อ system ที่คุยด้วย — คือเข้าได้ทุกตัวโดยไม่มี gate. **1 ใน 200** action เท่านั้นที่ require human approval ก่อนรัน
- Customer confirm: Culligan, Barry-Wehmiller, Wellstar Health System, **UiPath** — ~20 enterprise. UiPath น่าสนใจที่สุดเพราะเป็น vendor agent runtime เองแต่ยัง outsource security ให้ Opsin
- Signal: AI agent security กลายเป็น **category ที่เงินไหลเข้าชัดเจน** — Reco raise $55M ก.ย., Opsin $21M ต.ค., ตามหลัง Anthropic + CrowdStrike ที่ build in-house

## เกิดอะไรขึ้น

วันพุธที่ 15 ต.ค. **Opsin** ประกาศปิดรอบ **$21 ล้าน** นำโดย SYN Ventures + Race Capital. บริษัท positioning ตัวเองเป็น "AI governance and security startup" ที่ให้ security team เห็น agent ที่ run อยู่ทั่วองค์กร — ครอบคลุม Microsoft Copilot, Claude, ChatGPT Enterprise, Gemini, และ tool อื่น ๆ ที่ IT อนุมัติ. ก่อนหน้านี้ Opsin raise seed $7M ปี 2025, ส่วนรอบนี้ company ไม่เปิดเผย valuation และ round stage อย่างเป็นทางการ — tracker บางเจ้าถึงกับ note ว่า announcement ไม่ระบุ round stage ด้วยซ้ำ

Product core คือ **Risk Graph** — graph database ที่ join 4 dimension: **identity ของ agent, intended purpose, permission grants, และ observed activity**. เมื่อ agent ทำสิ่งที่ไม่ตรงกับ purpose ที่ประกาศไว้ (เช่น procurement agent ที่ dedicate ไปจัดการ supplier แต่กลับไปอ่าน HR database), ระบบ trigger response ได้ 3 ชั้น: (1) **restrict** — block action นั้น, (2) **quarantine** — ตัด agent จาก system ทั้งหมดจนกว่า human จะ review, (3) **notify owner** — ส่งไปที่ security team หรือ agent owner. คิดง่าย ๆ คือ CASB (Cloud Access Security Broker) แต่ layer ของ agent ไม่ใช่ของ app

Data ที่ Opsin เอง publish จาก customer base ของตัวเองคือ **จุดที่หลายคน miss**: จาก enterprise ที่ scan แล้ว **93% ของ tool ที่ agent connect อยู่มี "full, unrestricted access"** ต่อระบบปลายทาง — คือ API key หรือ OAuth token ที่ scope เต็ม ไม่มี least-privilege. และที่หนักกว่าคือ **1 ใน 200 action** เท่านั้นที่ configure ให้ require human approval ก่อนรัน. แปลเป็นภาษาคน: 199 ใน 200 action ที่ agent ทำใน production ของ enterprise เหล่านี้ **ไม่มี human in the loop เลย**

Customer list ที่ยืนยันคือ Culligan (water treatment), Barry-Wehmiller (industrial manufacturing), Wellstar Health System (healthcare), และ **UiPath**. ตัวสุดท้ายน่าสนใจที่สุด — UiPath เป็น automation vendor ที่มี agent runtime ของตัวเอง แต่ยังเลือก outsource agent security layer ให้ Opsin ดู นี่คือ confirmation ที่หนักแน่นมากว่า **agent security ไม่ใช่ feature ของ runtime** — มันคือ layer แยกที่ต้องมี vendor-agnostic view

## ทำไมสำคัญ

$21M ไม่ใช่ Series B $200M แบบ Arena, แต่ pattern ที่ชัดคือ **AI agent security กลายเป็น category แยกที่เงินไหลเข้าแล้ว** — Reco ปิด $55M ก.ย. (AI agent security), Opsin $21M ต.ค., Anthropic + CrowdStrike build in-house. จุดสำคัญไม่ใช่ขนาด round แต่คือ **สิ่งที่ Opsin เลือก publish** — 93% ของ tool connect ไม่มี gate, 1 ใน 200 ต้อง human approve. นี่คือ data point ที่ **CISO เอาไปใช้ขอ budget ได้ทันที** — ซึ่งหมายความว่า Opsin กำลัง create category เองในตัว

Pattern ที่กำลัง emerg ตามข่าว Oct 17-18 คือ **"agent sprawl is the new shadow IT"** — enterprise ปล่อยให้ dev + business user ลาก Copilot/Claude/ChatGPT เข้ามาเอง, แต่ไม่มีใครจัดการว่า agent เหล่านี้ connect อะไรบ้าง, มีสิทธิ์อะไร. เทียบกับ shadow IT ยุค 2015 ที่ Okta + Zscaler + Netskope โตมาจากตรงนี้ — Opsin + Reco กำลังจะเป็นชั้นเดียวกันของ agent decade. และสาเหตุที่ layer นี้แยกออกจาก runtime คือ enterprise ไม่ lock-in single agent vendor — ต้อง governance ที่ vendor-neutral

สิ่งที่ควร note: UiPath เป็น customer. UiPath มี agent runtime เอง, มี RPA เป็น decade แล้ว, แต่ยังต้องซื้อ Opsin — คือ confirmation ว่า **runtime vendor ไม่ควร trust ตัวเองในเรื่อง audit**. CISO ที่ชาญฉลาดจะไม่ยอมให้ Copilot ใช้ Microsoft Purview audit ตัว Copilot เอง — มัน incentive-aligned ผิดด้าน. นี่คือ moat ที่ Opsin มี: vendor-neutral position

## มุม AI Agent Platform

สำหรับ **Builders** (framework + agent runtime): หยุด build audit log + permission UI ของตัวเอง — เพราะ CISO ของ enterprise จะ bypass ไปใช้ Opsin / Reco / Datadog agent monitoring อยู่ดี. ที่ควร invest คือ **telemetry export surface** — webhook, SIEM integration, policy-as-code API — ให้ security vendor connect ได้ง่าย. และ **assume** ว่า agent ของคุณจะโดน quarantine เป็นปกติ — build graceful degradation เมื่อ connection ถูกตัดกลางคัน

สำหรับ **Users / Business**: ถ้าใน org มี Copilot/Claude/ChatGPT Enterprise รัน production อยู่, คำถามแรกที่ CISO ควรถามคือ "**agent ของเรา connect ไปที่ไหนบ้าง?**" — ถ้าตอบไม่ได้ภายใน 10 นาที หรือหา dashboard ไม่เจอ, security posture ยังไม่พร้อม scale. 93% ไม่มี gate เป็น industry average ของ Opsin's customer — ถ้าของคุณต่ำกว่านี้ก็ยังถือว่าเสี่ยง, ไม่ใช่ปลอดภัย. และสิ่งที่ควรปรับก่อนซื้อ vendor คือ **least-privilege scope ของ token** ที่ connect agent — API key full-access ไม่ควรออกให้ agent ที่ purpose แคบ

สำหรับ **Ecosystem**: Opsin + Reco + ตัวที่จะตามมาคือ "shovel seller" layer ของ agent era — เหมือน Snowflake vs. cloud provider. VC ที่เร่งถาม "เราควรลงเงินใน agent framework ตัวไหน" กำลังโฟกัสผิดจุด — layer ที่ moat กว้างกว่าคือ security + evaluation + observability ของ agent. 2027 น่าจะเห็น Series B $100M+ ของผู้เล่น agent security รอบใหม่ และ CrowdStrike / Palo Alto ซื้อตัวเล็ก consolidate category

## Sources
- [Opsin Raises $21M Led By SYN Ventures And Race Capital For AI Agent Security (Pulse2)](https://pulse2.com/opsin-raises-21-million-led-by-syn-ventures-and-race-capital-for-ai-agent-security/)
- [Opsin raises $21M to rein in rogue enterprise AI agents (Dealroom)](https://dealroom.co/news/162933-opsin-raises-21m-to-rein-in-rogue-enterprise-ai-agents/)
- [Opsin Raises $21M to Keep AI Agents on Task and Out of Trouble (Yahoo Finance)](https://finance.yahoo.com/technology/ai/articles/opsin-raises-21m-keep-ai-133000746.html)

---

## Audio script
วันพุธที่ 15 ตุลา Opsin ที่ซานโฮเซ่ ปิดรอบ 21 ล้านดอลลาร์ นำโดย SYN Ventures กับ Race Capital — ไม่เปิด valuation ไม่บอก round stage. Product คือ Risk Graph ที่ join 4 มิติ identity ของ agent purpose ที่ประกาศไว้ permission grants กับ observed activity. ถ้า agent ทำผิด purpose ระบบตัดสินได้สามชั้น restrict quarantine หรือ notify owner. ครอบคลุม Copilot Claude ChatGPT Enterprise Gemini กับ tool อื่น ๆ ที่ IT อนุมัติ. จุดที่ Opsin publish แล้วทำให้คนที่คุม security ตกใจคือ 93% ของ tool ที่ agent connect อยู่มี unrestricted access เข้าได้ทุกตัวโดยไม่มี gate และ 1 ใน 200 action เท่านั้นที่ require human approval ก่อนรัน แปลเป็นภาษาคนคือ 199 ใน 200 action ที่ agent ทำใน production enterprise ไม่มีมนุษย์ขั้น. Customer confirm 20 เจ้ารวม Culligan Barry-Wehmiller Wellstar กับ UiPath. UiPath น่าสังเกตมากที่สุดเพราะเป็น vendor automation ที่มี agent runtime เองแต่ยัง outsource security layer ให้ Opsin — confirm ว่า agent security ไม่ใช่ feature ของ runtime มันคือ layer แยกที่ต้อง vendor-neutral. Pattern ที่ emerg คือ agent sprawl กลายเป็น shadow IT รุ่นใหม่ Reco $55M ก.ย. Opsin $21M ต.ค. ตามหลัง Anthropic กับ CrowdStrike ที่ build in-house. ข้อเสนอสำหรับทีมที่ใช้ Copilot หรือ Claude ใน production คำถามแรกที่ CISO ควรถามคือ agent ของเรา connect ไปที่ไหนบ้าง ถ้าตอบไม่ได้ภายใน 10 นาที security ยังไม่พร้อม scale.
