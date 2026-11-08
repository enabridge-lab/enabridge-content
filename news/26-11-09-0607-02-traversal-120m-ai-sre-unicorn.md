---
date: 2026-11-03
slug: traversal-120m-ai-sre-unicorn
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a dark data-center floor at night
  during an incident. A giant red alert banner says "INCIDENT: PAYMENTS
  DOWN". A small cube labeled "TRAVERSAL WORKER" walks a glowing trail
  across racks, lighting up logs, traces and dashboards. A huge price tag
  reads "$120M SERIES B" with a smaller stat panel: "$1B VALUATION" and
  "2.5x PRIOR ROUND". A clock on the wall shows "18 MIN" vs "5 HOURS".
  Deep navy and warm amber palette, 1:1 aspect, no real human faces
  (silhouettes OK), high contrast so numbers stay readable at 200px.
image: images/26-11-09-0607-02-traversal-120m-ai-sre-unicorn.png
---

# Traversal แตะ unicorn ที่ $120M — agent สำหรับ on-call SRE กลายเป็นหมวดที่ VC เททั้งทัพ

## TL;DR
- 3 พฤศจิกายน Traversal ประกาศ Series B $120M ที่ valuation $1B — Kleiner Perkins, Redpoint, Khosla co-lead; Sequoia + Battery ร่วม
- Product: **long-running agents สำหรับ site reliability engineering** — Traversal Workers เริ่มสืบสวนทันทีเมื่อ alert fire; Traversal MCP ป้อน production intelligence กลับไป coding agent เพื่อให้เขียนโค้ดที่ resilient กว่า
- รอบนี้ใหญ่ 2.5x ของ seed+Series A รอบเดียวกัน ($48M มิย 2025) — Amex Ventures ลงทุน strategic เมื่อ มีค 2026 นำหน้า
- ORCA-bench benchmark (Cornell Tech + Columbia) ที่ Traversal co-publish: frontier agent 5 ตัวทำได้สูงสุด **25.3% บน medium task, 10.0% บน hard task** — ชี้ว่า general-purpose agent ยังไม่พอ ต้อง vertical

## เกิดอะไรขึ้น
วันที่ 3 พฤศจิกายน Traversal startup นิวยอร์กที่สร้าง AI SRE agent ประกาศปิด Series B $120M ที่ $1B valuation — Kleiner Perkins, Redpoint, และ Khosla Ventures co-lead ส่วน Sequoia Capital และ Battery Ventures ร่วมด้วย เงินจะไปที่ R&D, engineering และ go-to-market ไม่ได้บอกจำนวน seat หรือ ARR แต่ก่อนรอบนี้ Traversal เคยปิด seed + Series A รวมที่ $48M เมื่อมิถุนายน 2025 และมี strategic investment จาก Amex Ventures ในมีนาคม 2026 — รอบใหม่ใหญ่ประมาณ 2.5 เท่าของรอบก่อน

Product core คือ 2 ชิ้นที่ทำงานคู่กัน หนึ่ง — **Traversal Workers** เป็น long-running agent ที่ "subscribe" กับ alerting system เมื่อ incident หรือ alert fire มันเริ่ม investigate ทันที ไล่ logs, traces, metrics, deployment history, และ code change เพื่อหา root cause ไม่ใช่แค่ summarize alert เหมือน tool เก่า ๆ — ทำงานต่อเนื่องเป็นชั่วโมงถ้าจำเป็น สอง — **Traversal MCP** เป็น Model Context Protocol server ที่ป้อน production intelligence (error pattern จริง, recent incident, service dependency graph) กลับไปยัง coding agent อย่าง Claude Code หรือ Cursor เพื่อให้คนเขียนโค้ดได้ตัดสินใจบน context ที่รู้ว่า production เป็นยังไงจริง

ข้อมูลที่น่าสนใจคือ **ORCA-bench** — benchmark ที่ Traversal co-publish กับ Cornell Tech และ Columbia ประกอบด้วย 1,079 tasks ที่ agent ต้องหา root cause ของ incident จริง ผลที่ paper รายงาน: frontier agent 5 ตัวที่ทดสอบทำได้ accuracy สูงสุด 25.3% บน medium task และ 10.0% บน hard task — เป็น signal ที่ Traversal ใช้ขาย GTM ว่า general coding agent ยังไม่พอ ต้องมี vertical agent ที่เข้าใจ ops จริง

## ทำไมสำคัญ
Round นี้บอก 3 เรื่อง หนึ่ง — AI SRE กลายเป็น category ที่ VC tier 1 เข้าทั้งทัพแล้ว ก่อนหน้านี้ตลาด "agent that fixes software failures" ยังรวม Cleric, Resolve.ai, Parity, Rootly AI ฯลฯ ใช้ term ต่าง ๆ กัน ตอนนี้ Traversal ที่ $1B valuation กลายเป็น anchor — valuation ระดับนี้ทำให้ competitor ต้องเร่ง ตอบ: ยังเป็น early innings — คิดดูว่า Datadog ที่ครอง observability มี market cap หลาย 10B — ถ้า agentic layer กินตลาด "คนที่ interpret alert" ได้จริง ขนาดตลาดก็ใหญ่ตาม

สอง — Strategic investor pattern มี signal ของตัวเอง Amex Ventures ลง Traversal ในมีนาคม 2026 — แปลว่า American Express ใช้เองใน SRE stack ของตัวเอง และคิดว่าโมเดลนี้จะกลายเป็น infrastructure มาตรฐาน strategic ลงทุนไม่ใช่เพื่อ return แต่เพื่อให้ company ตัวเองเข้าถึง roadmap ก่อน แนวคิดนี้เริ่มเห็นใน Capital One Ventures (Sentra), JP Morgan (Firmly), Mastercard (Firmly), Samsung NEXT — bank + bank-adjacent + commerce tier 1 เริ่มไล่ซื้อ seat ใน agent infrastructure ก่อน

สาม — ORCA-bench ตัวเลขที่ paper publish (25.3% medium / 10% hard) เป็นทั้ง marketing และ scientific statement มัน frame ให้ CTO เห็นว่า general-purpose agent ไม่ใช่คำตอบ — ต้องมี vertical agent ที่ train บน ops data จริง pattern เดียวกันเราเริ่มเห็นใน legal agent (Harvey), coding agent (Factory, Cognition, Cursor), และ security agent (Dreadnode, Mintive) — vertical beats horizontal ในระยะ 12 เดือนข้างหน้า

## มุม AI Agent Platform
**Builders** — Traversal MCP ชี้ pattern ที่ coding agent ecosystem จะเดินตาม: production intelligence ป้อน MCP → coding agent ใช้ context ตัดสินใจเขียนโค้ด เส้นระหว่าง "agent ที่ monitor" กับ "agent ที่ write code" กำลังหายไป ใครสร้าง agent platform ควรคิดว่า MCP export ของ production system (error log, incident history, dependency graph) คือ product surface ไม่ใช่ internal tool

**Users / business** — ถ้าคุณมีทีม SRE / on-call engineer 20+ คน Traversal, Cleric, Resolve.ai กำลังเป็น default ที่ CIO ไทยต้อง evaluate ภายในปี 2027 ROI argument ง่าย: 1 on-call night shift ของ senior engineer ~$1-2k, incident ปีละ 100+ ครั้ง, mean time to resolution ลดจาก 5 ชม. เหลือ 35 นาที = saved ~$100-200k/year ต่อ 10 engineer. Pricing ยังไม่เปิดชัด แต่ anchor ที่คุ้ม

**Ecosystem** — Datadog, New Relic, PagerDuty ต้องตัดสินใจเร็ว — build in-house agent (Datadog Bits), buy startup, หรือยอมเป็น data source ของ agent platform อื่น ประวัติศาสตร์ monitoring บอกว่า incumbents มักช้าเพราะต้องไม่ cannibalize existing product และ Traversal + co ก็ไม่ปล่อยให้ช้าได้

## Sources
- [Traversal raises $120M at a $1B valuation to fix what AI code breaks (TNW)](https://thenextweb.com/news/traversal-120m-series-b-1b-valuation-ai-sre)
- [Goodwin Advises Traversal on $120 Million Series B](https://www.goodwinlaw.com/en/news-and-events/news/2026/11/announcements-technology-goodwin-advises-traversal-120-million-series-b)
- [Traversal raises $120M to automate incident response (Dealroom)](https://dealroom.co/news/169321-traversal-raises-120m-at-1b-valuation-to-automate-incident-response/)
- [Traversal: AI SRE Platform Receives Strategic Investment From Amex Ventures (Pulse2)](https://pulse2.com/traversal-ai-site-reliability-engineering-platform-receives-strategic-investment-from-amex-ventures)

---

## Audio script
Traversal startup ที่สร้าง AI agent สำหรับ site reliability engineering ปิด Series B 120 ล้านเหรียญที่ valuation 1 พันล้านเหรียญ นำโดย Kleiner Perkins, Redpoint, และ Khosla ร่วมกับ Sequoia และ Battery รอบนี้ใหญ่ประมาณ 2.5 เท่าของรอบก่อน ก่อนหน้านี้ Amex Ventures เคยลงทุน strategic ในเดือนมีนาคม Product ของ Traversal ประกอบด้วย 2 ชิ้น หนึ่งคือ Traversal Workers ที่เป็น long-running agent ซึ่ง subscribe กับ alert system เมื่อ incident เกิดก็เริ่ม investigate ทันที ไล่ logs, traces, deployment history เพื่อหา root cause สองคือ Traversal MCP ที่ป้อน production intelligence กลับไปยัง coding agent เช่น Claude Code หรือ Cursor เพื่อให้ engineer เขียนโค้ดบน context ที่รู้ว่า production เป็นอย่างไรจริง ตัวเลขที่น่าสนใจคือ ORCA-bench ที่ Traversal co-publish กับ Cornell Tech และ Columbia — frontier agent 5 ตัวทำได้สูงสุดแค่ 25% บน medium task และ 10% บน hard task ชี้ว่า general coding agent ยังไม่พอ ต้องมี vertical agent สำหรับ ops โดยเฉพาะ สำหรับ builder signal ชัดเจนว่า MCP ของ production system กำลังกลายเป็น product surface ไม่ใช่ internal tool สำหรับ CIO ไทยที่มีทีม on-call engineer 20+ คน Traversal กับคู่แข่งเป็น default ที่ต้อง evaluate ภายในปี 2027 ROI argument คำนวนง่าย — 1 night shift senior engineer 1-2 พันเหรียญ ลด mean time to resolution จาก 5 ชั่วโมงเหลือ 35 นาที คุ้มในระยะเวลาไม่ถึงปี
