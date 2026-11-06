---
date: 2026-11-05
slug: salesforce-agentforce-coworker-21x
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a bright corporate office floor with
  three desk pods wrapped around a large glowing cube marked "AGENTFORCE".
  A giant graph line at the back wall shoots up 21x, labeled "3 MONTHS",
  while a huge banner reads "185,000 USERS" and a small price tag hangs:
  "$50 / USER / MONTH". A Microsoft Teams-style window hovers beside one pod
  showing an AI teammate replying in chat. Clean editorial style, soft
  turquoise and warm orange palette, 1:1 aspect, no real human faces
  (silhouettes OK), high contrast so numbers stay readable at 200px.
image: images/26-11-06-0605-01-salesforce-agentforce-coworker-21x.png
---

# Salesforce พิมพ์ตัวเลขที่ enterprise agent รอมาทั้งปี — 185,000 คน, โต 21 เท่าใน 3 เดือน, $50/user/เดือน

## TL;DR
- Agentforce Coworker มี active users 185,000 คน โตขึ้น 21x ในเวลา 3 เดือน ทำให้ Salesforce เป็นรายแรกที่ยืนยัน scale จริงของ "agent-as-seat" ในตลาด enterprise
- เพิ่ม flat pricing $50/user/เดือน + รองรับ Microsoft Teams, Microsoft 365, Google Workspace — เปลี่ยนจาก per-action เป็น per-seat ชัดเจน
- Adecco Group เป็น early reference account — Salesforce เริ่มแปลง adoption number เป็น case study เพื่อปิด land-and-expand cycle

## เกิดอะไรขึ้น
วันที่ 5 พฤศจิกายน Salesforce ออกข่าว 2 บรรทัดที่หนักกว่าที่มันดู — ตัวเลข Agentforce Coworker โต 21 เท่าใน 3 เดือน active users เกิน 185,000 คน แปลว่าช่วงต้นเดือนสิงหาคมตัวเลขยังอยู่ประมาณไม่ถึง 10,000 — ซึ่งสำหรับโปรดักต์ enterprise ที่ขายผ่าน account executive ไม่ใช่ PLG ถือว่าเป็น curve ที่ไม่ค่อยเห็นในวงการ

สิ่งที่น่าสนใจกว่าตัวเลข user คือ pricing move — $50/user/month flat เพิ่มขึ้นเป็นทางเลือก ควบคู่ไปกับ consumption-based pricing เดิมที่คิดเป็น Flex Credits ต่อ action การย้ายไป per-seat แปลว่า Salesforce เชื่อว่า agent ใช้บ่อยพอจน CFO ต้องการเลขที่ predict ได้ ไม่ใช่เลขที่ผูกกับ usage spike รายวัน Analyst บางคนชี้ว่า $50 ที่ CFO จ่าย = ประมาณ 500 actions ของ Flex Credit ดังนั้น flat-rate คุ้มเมื่อ Coworker ทำงานเกิน ~17 action/วัน

Expansion อีกส่วนคือ channel — Agentforce Coworker เข้า Microsoft Teams ภายในเดือนนี้ เชื่อมกับ Microsoft 365 และ Google Workspace Salesforce บอกว่านี่คือ "agent surface" ที่พนักงานเปิดอยู่แล้ว ไม่ต้องให้พวกเขาไปที่ Salesforce app Adecco Group ซึ่งเป็น global staffing company ถูกยกเป็น early customer ที่ scale การใช้งานข้าม business unit — เป็นตัวอย่างที่ Salesforce จะเอาไปขายต่อ

## ทำไมสำคัญ
ตัวเลข 185,000 users ของ enterprise agent ที่ยืนยันโดยบริษัทมหาชน (ไม่ใช่ private startup pitch) เป็น signal ที่ตลาดรอมาทั้งปี — จนถึงตอนนี้ agentic adoption เล่าเป็น "pilot" กับ "POC" เป็นส่วนใหญ่ การย้ายจาก pilot ไป production ที่มี user count 6 หลักเป็นการพิสูจน์ว่า work-handoff model มันเวิร์คในระดับ org ไม่ใช่แค่ demo

Pricing move ก็บอกอะไรหลายอย่าง — $50/user เป็นราคาที่คุ้นเคยสำหรับ SaaS buyer (เทียบ Office 365 E3, Zoom, Google Workspace Business Plus) การ anchor ที่นี่ Salesforce กำลังบอกว่า agent = SaaS seat รุ่นใหม่ ไม่ใช่ infrastructure cost center ที่ต้อง FinOps มาจัดการ ถ้า model นี้เวิร์ค จะกดดันคู่แข่ง — Microsoft Copilot ($30), ServiceNow Now Assist (bundle), Workday Illuminate — ต้องเลือกว่าจะ race to bottom หรือจะไปโฟกัส vertical ที่ต่าง

Caveat — ตัวเลข 185,000 เป็น "users who used Coworker" ไม่ใช่ paid seats และไม่มี breakdown ระหว่าง free trial, bundled license, และ paid conversion นักวิเคราะห์บางคนใน Compare the Cloud ชี้ว่า adoption number ≠ productivity gain ถ้าอยากรู้ว่า agent สร้างมูลค่าจริงไหม ต้องรอ Q4 earnings ที่ Salesforce ต้อง guide revenue อิมแพ็กแบบชัด

## มุม AI Agent Platform
Builders — Salesforce กำลังบอกว่า distribution > model quality — ไม่ว่าคุณจะมี agent ที่ smart แค่ไหน ถ้าไม่อยู่ใน surface ที่ user เปิดอยู่แล้ว (Teams, Gmail, Slack) คุณต้อง compete กับ incumbents ที่ embed เข้าไปได้ง่ายกว่า นี่ reinforce thesis ว่า agent platform play ที่ชนะจะเป็น horizontal integration layer ที่ cross SaaS silos ไม่ใช่ standalone chat UI

Users/business — ถ้าคุณคิดจะซื้อ agent seat per-user ตอนนี้มี market anchor แล้ว — $30 (Copilot) ถึง $50 (Agentforce) คือช่วงที่จะกลายเป็น default ปี 2027 buyer ควรตั้งคำถามคือ agent ทำงานเกิน $50 มูลค่าต่อเดือนไหม ไม่ใช่เชื่อ sales deck ของ vendor Enabridge ที่สร้าง agent platform ให้ลูกค้าไทย ควร benchmark pricing ตัวเองกับ anchor นี้ — ยิ่ง embed ใน workflow ที่พนักงานใช้แล้ว ยิ่งง่ายที่จะจัดการ renewal

Ecosystem — Microsoft ต้องคิดหนัก — การที่ Agentforce ไปอยู่ใน Teams แปลว่า Salesforce กำลังใช้ surface ของ Microsoft แข่งกับ Copilot ในบ้าน Microsoft เอง ประวัติศาสตร์เคยเกิดกับ Slack vs Teams ที่ Microsoft ตัดสินใจไม่อนุญาตบาง integration รอดู Microsoft จะปล่อยให้ Agentforce นั่งข้าง Copilot ใน Teams นานแค่ไหน

## Sources
- [Salesforce's Agentforce Coworker Usage Soars 21x in Three Months](https://www.salesforce.com/ap/news/press-releases/2026/11/05/sg-salesforces-agentforce-coworker-usage-soars-21x-in-three-months-as-enterprises-delegate-real-work-to-ai/)
- [Can Salesforce Win the AI Front Door Inside Teams? (CX Today)](https://cxtoday.com/can-salesforce-win-the-ai-front-door-inside-teams)
- [Salesforce says Agentforce Coworker usage is up 21x in three months (Compare the Cloud)](https://www.comparethecloud.net/news/salesforce-says-agentforce-coworker-usage-is-up-21x-in-three-months-and-sets-a-50-per-user-price)
- [Salesforce's $50 Coworker Seat Costs as Much as 500 Actions (FourWeekMBA)](https://fourweekmba.com/ai-salesforces-50-coworker-seat-costs-as-much-as-500-actions/)

---

## Audio script
ข่าว Salesforce ที่ออกเมื่อวันที่ 5 พฤศจิกายนเป็นตัวเลขที่ตลาด enterprise agent รอมาทั้งปี Agentforce Coworker ซึ่งเป็น AI teammate ของ Salesforce มี active users 185,000 คน โตขึ้น 21 เท่าในเวลาแค่สามเดือน แปลว่าต้นเดือนสิงหาคมตัวเลขยังอยู่ประมาณไม่ถึงหมื่น นี่เป็น curve ที่ไม่ค่อยเห็นในโปรดักต์ enterprise ที่ขายผ่าน sales rep ไม่ใช่ product-led growth Salesforce เพิ่มทางเลือก pricing ใหม่ที่ 50 เหรียญต่อ user ต่อเดือน flat rate แทนที่จะคิด per action แบบเดิม การ anchor ราคาแบบนี้บอกว่า Salesforce เชื่อว่า agent จะกลายเป็น SaaS seat รุ่นใหม่ ไม่ใช่ infrastructure cost ที่ต้องมี FinOps ดูแล และ Agentforce จะเข้าไปอยู่ใน Microsoft Teams, Microsoft 365, และ Google Workspace ซึ่งเป็น surface ที่พนักงานเปิดอยู่แล้ว สำหรับคนที่สร้าง agent platform signal นี้ชัดเจน distribution สำคัญกว่า model quality agent ที่อยู่ใน Teams จะชนะ agent ที่อยู่ในแอพของตัวเอง สำหรับ CFO ที่กำลังคิดจะซื้อ agent ตอนนี้มี market anchor แล้ว 30 เหรียญถึง 50 เหรียญต่อ user ต่อเดือน จะกลายเป็น default ปี 2027 แต่ caveat คือตัวเลข 185,000 เป็น user ที่ใช้งาน ไม่ใช่ paid seat และไม่มี breakdown ชัด รอดู Q4 earnings ว่า Salesforce จะ guide revenue impact อย่างไร
