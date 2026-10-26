---
date: 2026-10-27
slug: opsin-21m-agent-governance
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of an air-traffic-control tower
  overlooking a runway of translucent AI agent silhouettes; a glowing radar
  dish on top sweeps the field. A control board inside the tower shows three
  big stacked labels: "93% UNRESTRICTED", "1 IN 200 APPROVALS", "$21M RAISE".
  Deep purple and lime accent palette, crisp line work, 1:1 aspect, no real
  human faces.
image: images/26-10-27-0607-05-opsin-21m-agent-governance.png
---

# Opsin $21M + "93% ของ agent tool ไม่มี access control" — agent sprawl กลายเป็น enterprise crisis

## TL;DR
- Opsin ปิด $21M นำโดย SYN Ventures + Race Capital เมื่อ 15 ตุลาคม — build "agent control plane" ที่ monitor agent บน Copilot, Claude, ChatGPT Enterprise, Gemini
- Customers ~20 ราย รวม Culligan, Barry-Wehmiller, Wellstar Health System, UiPath
- สถิติที่ Opsin เปิดเผย: 93% ของ tool ที่ต่อกับ agent มี access แบบไม่จำกัด; มีเพียง 1 ใน 200 agent ที่ต้องการ human approval ก่อน action (ตัวเลขจากบริษัท ยังไม่มี third party ยืนยัน)

## เกิดอะไรขึ้น
15 ตุลาคม Opsin สตาร์ทอัพจาก San Jose ประกาศ Series A $21M นำโดย SYN Ventures และ Race Capital. Opsin เป็น platform ที่ให้ security team มองเห็น "flock" ของ agent ที่ build บน Microsoft Copilot, Claude, ChatGPT Enterprise และ Gemini — เชื่อม purpose ของ agent, permission ที่มี, data ที่เข้าถึง และ activity log ไว้ที่เดียว. ถ้า agent ไหน misbehave Opsin สามารถ quarantine, block action หรือแจ้งเจ้าของให้ remediate ได้.

ลูกค้าชุดเปิด 20 ราย ประกอบด้วยชื่อที่ชัดเจนในธุรกิจ regulated: Culligan (water treatment), Barry-Wehmiller (manufacturing), Wellstar Health System (healthcare), และ UiPath (automation). CEO James Pham พร้อม co-founder Jeremy Mailen และ Oz Wasserman พูดเรื่อง "agent sprawl" — ปัญหาที่พนักงานในองค์กรสร้าง agent เองโดยที่ IT ไม่รู้ และ agent เหล่านั้นมี access ที่ไม่ได้ scope.

ตัวเลขที่ Opsin เอามา pitch (ยังไม่ยืนยันจาก third party): จาก analysis ของ customer agent activity, **93% ของ tool ที่ agent ต่อ มี access แบบ unrestricted** — คือเข้าถึงทุกส่วนของระบบที่ตัวเอง interact. และ **มีเพียง 1 ใน 200 agent** ที่ต้อง human approval ก่อนทำ action. ถ้าตัวเลขจริง เป็น severe over-privilege ในระดับที่น่ากังวล.

## ทำไมสำคัญ
Opsin เป็นหลักฐานชัดอีกชิ้นว่า "agent governance" กลายเป็น category ที่ VC เริ่มใส่เงินจริงจัง. ในเดือนตุลาคมเดือนเดียว เรานับได้: Opsin $21M, Mave Security $34M (Israel, cross-vendor security operations), + Microsoft ขยาย Project Perception เอง + Nevis $70M (financial advisor agents + governance). รวมกัน ~$150M+ หมุนเข้าหมวดนี้ในเดือนเดียว.

Pattern ที่เห็นคล้ายคลึง SIEM ยุคกลาง-2010 — ก่อนที่ Splunk จะเป็น $4B business เรามี agent สร้าง log กระจาย ไม่มี central visibility. ตอนนี้ชื่อ product อาจต่าง (SOAR, agent observability, agent control plane) แต่ pattern คือ "central pane of glass ที่ตามเก็บทุกสิ่งที่ identity หนึ่ง ๆ ทำ". ที่ต่างคือ: agent สามารถสร้างได้ด้วย prompt, จำนวนตัวจึงโต exponential กว่า user, และ action ที่ agent ทำมี impact ใหญ่กว่า log event (ตัดสินใจ, จ่ายเงิน, แก้ data).

Thesis ของ Opsin ลึกกว่าตัวสินค้า: ถ้าแต่ละแผนกสร้าง agent ของตัวเองได้ "ด้วย prompt" โดยไม่ผ่าน IT, บริษัทจะมี agent ภายในปี 2027 มากกว่าจำนวนพนักงาน. ถ้าตัวเลข "1 ใน 200 ต้อง approval" ถูกต้อง, นั่นคือ 199 ตัวที่ act autonomous โดยที่ไม่มีใครดู. ซึ่งคือตลาดของ Opsin.

## มุม AI Agent Platform
สำหรับ **builders**: ถ้าคุณสร้าง agent framework หรือ orchestration layer ให้ enterprise ควรออกแบบ metadata layer ของ agent (purpose, scope, approval requirement) เป็น first-class citizen — ไม่ใช่ feature ที่ bolt on หลัง. Opsin อ่าน metadata เหล่านี้; ถ้า framework ของคุณไม่ emit, ลูกค้าใหม่ของ Opsin จะไม่ใช้ framework คุณ.

สำหรับ **users / business**: Opsin, Microsoft Entra Agent ID, และ Mave Security กำลังตั้ง playbook สำหรับ "agent policy" ที่คล้าย "data loss prevention" ของยุค 2015 — เริ่ม pilot กับ agent 10-20 ตัวในแผนก คู่กับ security team ก่อนที่ agent sprawl จะกลายเป็น 500+. สำหรับ ecosystem: มีคำถามว่า Microsoft Entra Agent ID จะ absorb category นี้ (bundle มากับ M365) หรือจะมี neutral layer เหมือน Okta ที่อยู่เหนือทุก vendor — การ positioning ของ Opsin (cross-vendor) เป็น hedge ว่า market จะไม่ consolidate รอบ Microsoft เท่านั้น.

## Sources
- [Opsin Raises $21M Led By SYN Ventures And Race Capital For AI Agent Security (Pulse 2.0)](https://pulse2.com/opsin-raises-21-million-led-by-syn-ventures-and-race-capital-for-ai-agent-security/)
- [Opsin raises $21m as AI agents outpace legacy security (FinTech Global)](https://fintech.global/?p=260790)
- [Opsin Raises $21M Led by SYN Ventures and Race Capital to Expand AI Agent Security Platform (citybiz)](https://www.citybiz.co/?p=919256)
- [Opsin raises $21M to rein in rogue enterprise AI agents (Dealroom)](https://dealroom.co/news/162933-opsin-raises-21m-to-rein-in-rogue-enterprise-ai-agents/)

---

## Audio script
ข่าวที่ห้าและสุดท้ายวันนี้เรื่อง Opsin สตาร์ทอัพจาก San Jose ที่เพิ่งปิด Series A 21 ล้านดอลลาร์ นำโดย SYN Ventures กับ Race Capital. Opsin สร้าง control plane สำหรับ AI agent ที่ enterprise สร้างบน Copilot, Claude, ChatGPT Enterprise และ Gemini. ลูกค้ายี่สิบรายแรกของเขารวม Culligan, Barry-Wehmiller, Wellstar Health System และ UiPath. ตัวเลขที่น่าสนใจที่ Opsin เปิดเผยจาก analysis ของลูกค้าคือ 93% ของเครื่องมือที่ agent ต่ออยู่ มี access แบบไม่จำกัด และมีเพียง 1 ใน 200 agent ที่ต้อง human approval ก่อนทำ action. ตัวเลขนี้ถ้าจริง หมายความว่าในองค์กรใหญ่หนึ่งแห่งอาจจะมี agent หลายร้อยตัวที่กำลัง act autonomous โดยไม่มีใครคุม. เรื่องนี้สำคัญเพราะเดือนตุลาคมเดือนเดียว หมวด agent governance รับเงินมากกว่า 150 ล้านดอลลาร์ จาก Opsin, Mave Security และ Microsoft เอง — pattern เดียวกับที่ SIEM เคยโตเมื่อสิบปีก่อน ตลาดกำลังตื่นว่า agent sprawl คือ enterprise risk ที่จับต้องได้
