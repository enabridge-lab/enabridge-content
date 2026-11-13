---
date: 2026-11-14
slug: decagon-missions-long-horizon
topic: use-case
reading_time_min: 3
sources: 3
image_prompt: |
  An editorial isometric illustration of a horizontal timeline that stretches
  across the frame, labeled "MISSION" with waypoints at "DAY 1", "DAY 3",
  "DAY 7". A single glowing agent avatar carries a package of context from
  left to right past the waypoints. Below the timeline, four brand cards
  stack in a row: "CHIME — 70% CONTAINMENT", "DUOLINGO — 80% DEFLECTION",
  "HERTZ — PROACTIVE OUTBOUND", "DEUTSCHE TELEKOM". Above, a banner reads
  "DECAGON MISSIONS — LONG HORIZON". Editorial style, soft violet and warm
  coral palette, high contrast so numbers stay readable at 200px, 1:1
  aspect, no real human faces.
image: images/26-11-14-0605-04-decagon-missions-long-horizon.png
---

# Decagon เปิด Missions — customer service agent ขยับจาก Q&A ไปทำงานข้ามหลายวัน

## TL;DR
- 12 พฤศจิกายน Decagon เปิด "Missions" — agent ที่ทำ long-horizon task ข้ามหลาย conversation หลาย system หลายคน ต่อเนื่องเป็นวันหรือสัปดาห์
- Named customers: Chime (70% chat/voice resolution, operating cost ลด >60%, voice agent รับสาย >1M calls/เดือน), Duolingo (80% deflection), Hertz (outbound proactive), Deutsche Telekom
- 100+ enterprise ลูกค้าใหม่ปี 2025, valuation $4.5B หลัง Series D $250M ม.ค. 2026 — signal ว่า customer-service agent moves beyond chat

## เกิดอะไรขึ้น
วันที่ 12 พฤศจิกายน Decagon ซึ่งเป็น customer service agent startup ที่ลูกค้าหนักอยู่ในกลุ่ม consumer ประกาศ Missions — product feature ใหม่ที่ขยับ paradigm จาก "ตอบคำถามเดี่ยว ๆ" ไปเป็น "agent รับผิดชอบผลลัพธ์ที่ใช้เวลาหลายวันหรือสัปดาห์" Missions coordinate agent ข้าม system ภายใน, monitor status update, และ engage คนในหลายขั้นตอนตามจำเป็น

ตัวอย่าง use case ที่ Decagon ยก — ลูกค้าธนาคารร้องเรียน fraud charge ที่ต้องรอ investigation 7-14 วัน ปกติ chat agent ตอบได้แค่ "เราจะติดต่อกลับภายใน 7 วัน" แล้วจบ session Missions จะจัดการเอง: ส่งต่อ case ให้ investigator, ติดตาม status จาก backend, update ลูกค้าเป็นระยะ, แจ้ง resolution, และเก็บ feedback — ทั้งหมดในฐานะ agent เดียวที่ "เป็นเจ้าของ mission"

Named customer ที่ Decagon ประกาศคู่กับ Missions เป็นกลุ่มที่ highlight pattern นี้ชัด — Chime (digital bank) รายงานว่า voice + chat agent containment rate อยู่ที่ 70% operating cost ของ contact center ลดลงมากกว่า 60% voice agent รับสายมากกว่า 1 ล้าน call ต่อเดือน Duolingo ซึ่งเป็น language learning รายงาน deflection rate ประมาณ 80% Hertz ใช้ Decagon ทำ outbound proactive — ตรวจ pattern ที่ลูกค้าจะโทรเข้าเรื่องรถเช่า (เช่น flight delayed) แล้วโทรหาลูกค้าก่อน Deutsche Telekom อยู่ใน customer list แต่ไม่ breakdown metric

บริษัทบอกด้วยว่าปี 2025 รับลูกค้าใหม่มากกว่า 100 enterprise รอบล่าสุด Series D $250M ที่ valuation $4.5B ปิดในเดือนมกราคม Decagon ไม่เปิดเผย ARR แต่ตัวเลข customer count + valuation บอกว่าอยู่ในกลุ่ม top 3 pure-play customer-service agent startup

## ทำไมสำคัญ
สัญญาณที่ Missions ส่งไปถึงตลาดชัดเจน — customer service agent ที่แค่ตอบ FAQ แล้ว transfer ให้คนไม่พอแล้ว ลูกค้าใหญ่ต้องการ agent ที่ "take ownership of outcome" ซึ่งเป็น shift ที่ลึกกว่า chatbot deflection rate การ measure ที่ถูกต้องสำหรับ Missions ไม่ใช่ containment rate แต่เป็น case resolution time, customer satisfaction หลังจบ case, และ cost per resolved issue (ไม่ใช่ per message)

เทียบกับ player อื่น — Sierra มี similar play โดย Bret Taylor focus ที่ complex workflow, Ada ไปทาง automation platform-style, Intercom Fin focus ที่ scale ของ SMB ขณะที่ Decagon โฟกัสที่ consumer enterprise high-volume (bank, telco, EdTech, travel) ที่ต้องรับมือ issue type ซับซ้อนและ compliance Missions เป็น product move ที่ shift Decagon จาก "deflection engine" ไปเป็น "customer operations layer" ซึ่งเป็น position ที่ CFO คิดเป็น cost center replacement ไม่ใช่ marketing tool

Caveat — ตัวเลข 70% containment, 80% deflection, 1M calls/month เป็นที่ Decagon และ Chime ร่วมกันประกาศ ไม่มี third-party audit และ "containment" ไม่ตรงกับ "resolution" (ลูกค้าอาจจะโทรกลับทีหลัง) นักวิเคราะห์ที่ตรวจ metric แบบนี้ซ้ำ ชี้ว่า deflection rate บริษัท self-report มักสูงกว่า actual repeat-contact-adjusted rate 15-25% แต่สำหรับคนที่กำลังเลือก vendor ตัวเลข 70% กับ 80% ก็ยังเหนือ incumbent BPO ที่ปกติอยู่ 20-30%

## มุม AI Agent Platform
Builders — ถ้ากำลังสร้าง customer-service agent ให้คิดว่า "multi-session memory + long-horizon coordination" เป็น table stake ไม่ใช่ feature premium architecture ที่ต้อง support — persistent agent state ข้าม conversation, integration กับ backend ของลูกค้า (ticketing, CRM, product DB), และ status polling ที่ไม่ใช่ user-initiated ทั้งหมดต้อง design ตั้งแต่แรก สำหรับทีมที่ยังทำ FAQ chatbot — เตรียมเปลี่ยน architecture หรือจะโดนแทนที่

Users/business — สำหรับ enterprise ที่คิดจะ deploy customer-service agent ควร re-scope project จาก "ลด ticket" เป็น "เป็นเจ้าของ outcome บาง category" — ลูกค้าไทยกลุ่ม telco, retail bank, insurance, airline, e-commerce ที่ Enabridge ดูแลควรจัด workshop เพื่อ map case lifecycle ของแต่ละ issue type ปัจจุบัน แล้วเลือก category ที่ยาวที่สุด (fraud dispute, claim, refund, loyalty issue) เป็น pilot ของ long-horizon agent แทน FAQ KPI ที่ตั้งควรเป็น "case resolution time" ไม่ใช่ "message volume"

Ecosystem — Zendesk, Salesforce Service Cloud, Freshworks เจอ existential question — เมื่อ agent เป็นเจ้าของ case ตั้งแต่ต้นจบ ticketing system ที่ออกแบบสำหรับ human agent จะมี value อะไร คำตอบระยะสั้นคือ — ticketing อาจเหลือเป็น backend system of record แต่ customer-facing UX ถูก agent กินไป ทั้งสามบริษัทต้อง build native agent ของตัวเอง หรือ acquire — Zendesk ซื้อ Ultimate.ai ไปปีก่อน แต่ยังไม่เห็น Missions-style product รอดู Service Cloud response

## Sources
- [Decagon Launches Missions for Long-Running AI Customer Workflows (Unite.AI)](https://www.unite.ai/decagon-launches-missions-for-long-running-ai-customer-workflows/)
- [Decagon: How AI Service Agents Firm Hit US$4.5bn Valuation (AI Magazine)](https://aimagazine.com/news/decagon-how-ai-service-agents-firm-hit-us-4-5bn-valuation)
- [Decagon Review (2026): AI Support for Notion, Duolingo (The AI Agent Index)](https://theaiagentindex.com/agents/decagon)

---

## Audio script
วันที่ 12 พฤศจิกายน Decagon ซึ่งเป็น customer service agent startup ประกาศ Missions ซึ่งเป็น feature ใหม่ที่ขยับ paradigm จากตอบคำถามเดี่ยว ๆ ไปเป็น agent ที่รับผิดชอบผลลัพธ์ข้ามหลายวันหรือสัปดาห์ Missions coordinate agent ข้าม system, monitor status update และ engage คนในหลายขั้นตอนตามจำเป็น ตัวอย่างคือลูกค้าธนาคารร้องเรียน fraud charge ที่ต้องรอ investigation 7 ถึง 14 วัน ปกติ chat agent ตอบได้แค่เราจะติดต่อกลับภายใน 7 วันแล้วจบ session Missions จะจัดการเอง ส่งต่อ case ให้ investigator ติดตาม status จาก backend update ลูกค้าเป็นระยะ แจ้ง resolution และเก็บ feedback ทั้งหมดในฐานะ agent เดียวที่เป็นเจ้าของ mission Named customer ประกอบด้วย Chime ที่ containment rate 70 เปอร์เซ็นต์ operating cost ลด 60 เปอร์เซ็นต์ voice agent รับสายมากกว่าหนึ่งล้านสายต่อเดือน Duolingo ที่ deflection 80 เปอร์เซ็นต์ Hertz ที่ใช้ทำ outbound proactive และ Deutsche Telekom สัญญาณชัดเจนว่าตลาดต้องการ agent ที่ take ownership of outcome ไม่ใช่แค่ตอบ FAQ แล้ว transfer ให้คน สำหรับ enterprise ที่คิดจะ deploy customer-service agent ควร re-scope project จากลด ticket เป็นเป็นเจ้าของ outcome บาง category ลูกค้าไทยกลุ่ม telco retail bank ประกัน airline e-commerce ควรจัด workshop map case lifecycle ของแต่ละ issue type แล้วเลือก category ที่ยาวที่สุด เช่น fraud dispute, claim, refund เป็น pilot ของ long-horizon agent แทน FAQ
