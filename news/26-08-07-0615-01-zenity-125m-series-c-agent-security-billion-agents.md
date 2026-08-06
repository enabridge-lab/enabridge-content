---
date: 2026-08-07
slug: zenity-125m-series-c-agent-security-billion-agents
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  A monumental digital vault labeled "1 BILLION AI AGENTS" glowing amber
  behind massive stacked bills; three glowing metric plates hover in front
  reading "$125M SERIES C", "$185M TOTAL RAISED", "3x REVENUE, 2 YRS IN A
  ROW". Editorial isometric illustration, warm gold and midnight navy
  palette, thin blue circuit lines wiring the plates to Fortune 500 logo
  silhouettes in the background. 1:1 aspect, high contrast so numbers read
  in a 200px thumbnail. No real human faces.
image: images/26-08-07-0615-01-zenity-125m-series-c-agent-security-billion-agents.png
---

# Zenity ระดม $125M เพื่อ "รักษา" ยุค 1 พันล้าน AI Agent — Norwest นำ, SoftBank + Hitachi + LG ร่วม

## TL;DR
- Zenity ปิด Series C $125M นำโดย Norwest — รวมทุนแตะ $185M, tripled revenue สองปีติด, on track ทำอีกรอบปีนี้
- ลูกค้า Fortune 500 / Global 2000 ใช้ Zenity คุม autonomous agent — Gartner จัดเป็น "frontrunner" ใน AI agent governance เมื่อ เม.ย. 2026
- Deal นี้เกิดในสัปดาห์เดียวกับ Black Hat 2026 ที่ทุก vendor แข่งกัน launch security capability สำหรับ agent — agent security คือ category ใหม่ที่ทั้ง VC และ enterprise ยอมรับแล้ว

## เกิดอะไรขึ้น
วันที่ 3 สิงหาคม 2026 Zenity ประกาศ Series C มูลค่า $125 ล้าน นำโดย Norwest Venture Partners มี Qumra Capital, SoftBank Vision Fund 2, Hitachi Ventures และ LG Technology Ventures เข้าร่วมเป็น new investors ขณะที่ Vertex Ventures, Third Point Ventures, DTCP และ Intel Capital ยังคงลงเพิ่ม รวม total funding เท่ากับ ~$185M

Zenity อยู่ในตลาดที่แทบไม่มีคู่แข่งเมื่อสองปีก่อน — AI agent security & governance ที่ออกแบบเฉพาะสำหรับ autonomous agents ไม่ใช่ human user. บริษัทมีพนักงาน 230+ คน R&D อยู่ Tel Aviv, go-to-market อยู่ New York, และเป็นลูกค้า Fortune 500 / Global 2000 หลายราย. เม.ย. 2026 Gartner จัด Zenity เป็น frontrunner ใน category "AI agent governance" ชี้ว่า architecture ของบริษัทเป็น "agentic-centric" กับ intent-aware detection ที่ competitor ทำไม่ได้

ตัวเลข growth ที่บริษัทแชร์กับ investor: tripled revenue ในแต่ละปีของสองปีที่ผ่านมา และ on track จะ triple อีกรอบปีนี้ — pattern แบบนี้เป็นสาเหตุที่ SoftBank Vision Fund 2 (ซึ่งปีนี้ค่อนข้าง picky หลัง portfolio ที่แพงในปี 2021-2022) ยอมเข้ามา. ที่น่าสังเกตกว่าคือ Hitachi และ LG — สอง strategic investor สาย hardware/industrial ที่เข้า deal นี้เพราะกำลัง deploy agents ในโรงงาน supply chain และ consumer product ของตัวเอง

## ทำไมสำคัญ
ตำแหน่งของ Zenity ในตลาดตอนนี้ — และ investor ที่ตามมา — คือ signal ว่า "agent security" ได้แยกตัวจาก "AI security" หรือ "GenAI content moderation" ที่เป็น pitch ของปี 2023-2024 อย่างสิ้นเชิง. Zenity ไม่ได้ขาย prompt filter, ไม่ได้ขาย output classifier — ขายระบบ observability + policy enforcement ที่ตามดู agent ตั้งแต่ moment มัน request tool, สร้าง sub-agent, เข้าใช้ OAuth grant, จนถึงส่ง data ไป external service. เมื่อองค์กรมี 50+ agents run ต่อวัน ทุก agent มี identity + permission + audit trail ของตัวเอง — pattern นี้เป็น IAM ยุคใหม่ที่ Okta / Entra ID ตามไม่ทัน

การที่ round ปิดในสัปดาห์เดียวกับที่ Acalvio launch Deception Guardrails, Zero Networks launch Least Agency Enforcement, Palo Alto Networks กำลัง roll out Idira (จาก CyberArk acquisition), และ CrowdStrike ประกาศ Agents of Chaos $100K challenge — ไม่ใช่บังเอิญ. Black Hat USA 2026 คือ moment ที่ตลาด collectively ยอมรับว่า agent เป็น attack surface ใหม่ที่ vendor เดิมไม่ครอบคลุม. Zenity ได้ mindshare + war chest ก่อน category กลายเป็น commoditized

## มุม AI Agent Platform
สำหรับ **builders** ที่ทำ agent framework / orchestration — ต้อง design assumption ใหม่: policy enforcement เป็น hard requirement ไม่ใช่ optional feature. Agent ที่ไม่มี identity, ไม่มี audit trail, ไม่มี intent classifier จะไม่ผ่าน procurement ที่ Fortune 500. ถ้ายังยกให้ user config เอง = ตกรอบ. สำหรับ **enterprises** ที่เพิ่งเริ่ม deploy agent — ถ้ายัง treat agent security เหมือน endpoint security หรือ API security = under-invest. Attack surface ของ agent คือ tools + credentials + inference behavior ที่เปลี่ยนตาม prompt ทุกครั้ง; ต้อง budget วางหมวด "agent governance" แยกในปีงบ 2027. สำหรับ **ecosystem** — ทั้ง CSP (AWS/Azure/GCP), IAM incumbents (Okta/Entra), และ CNAPP vendors (Wiz/Palo Alto) จะต้องเลือก: build เอง, ซื้อ Zenity/Reco/Astelia คู่แข่ง, หรือ partner. คำถามที่ค้างคือ Zenity จะ exit ยังไง — IPO ที่ valuation $2-3B ในปี 2027, หรือถูก Palo Alto / CrowdStrike acquire ที่ราคาสูงกว่า Adaptive Shield ($300M) หลายเท่า

## Sources
- [Zenity Raises $125 Million to Secure the Era of 1 Billion AI Agents](https://zenity.io/company-overview/newsroom/company-news/zenity-raises-125-million-to-secure-the-era-of-1-billion-ai-agents)
- [SoftBank, Hitachi, LG back Zenity's $125 million round to police AI agents — Fortune](https://fortune.com/2026/08/03/softbank-hitachi-lg-back-zenitys-125-million-round-to-police-ai-agents/)
- [Zenity Raises $125M Series C to Expand AI Agent Security Platform — AIwire](https://www.hpcwire.com/aiwire/2026/08/04/zenity-raises-125m-series-c-to-expand-ai-agent-security-platform/)
- [Zenity lands $125m as AI agent security race heats up — Fintech Global](https://fintech.global/2026/08/04/zenity-lands-125m-as-ai-agent-security-race-heats-up/)

---

## Audio script
วันนี้มี funding round ที่ผมว่าคนทำ AI Agent ต้องอ่าน. Zenity ปิด Series C หนึ่งร้อยยี่สิบห้าล้านเหรียญ นำโดย Norwest, ดึง SoftBank Vision Fund สอง, Hitachi Ventures และ LG Technology Ventures เข้ามาใหม่. รวม total funding ตอนนี้ประมาณหนึ่งร้อยแปดสิบห้าล้าน. Zenity ขายอะไร — ระบบ security กับ governance ที่ออกแบบมาเฉพาะสำหรับ AI Agent ไม่ใช่ user มนุษย์. ตอนนี้ลูกค้าเป็น Fortune 500 กับ Global 2000, พนักงานสองร้อยสามสิบคน, revenue triple สองปีติด. เมษายน ที่ผ่านมา Gartner จัดให้เป็น frontrunner ใน AI Agent governance. ที่น่าสังเกตคือ deal นี้ปิดในสัปดาห์เดียวกับ Black Hat USA สองพันยี่สิบหก ที่ vendor ทุกเจ้าแข่งกัน launch capability สำหรับ agent security — Acalvio ออก Deception Guardrails, Zero Networks ออก Least Agency Enforcement, CrowdStrike ประกาศ Red Team challenge หนึ่งแสนเหรียญ. Signal ชัดเจนคือ agent security ได้แยกเป็น category ใหม่แล้ว ไม่ใช่ subset ของ AI security ทั่วไปอีกต่อไป. องค์กรที่กำลัง deploy agent ต้อง budget แยก agent governance ในปี 2027 ไม่งั้นตกรอบตอน procurement.
