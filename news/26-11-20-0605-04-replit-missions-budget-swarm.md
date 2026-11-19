---
date: 2026-11-17
slug: replit-missions-budget-swarm
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a dashboard with a glowing meter
  labeled "BUDGET: $1,000" filling halfway; around it hover 32 small agent
  icons working in a swarm, each with a tiny status dot. A giant metric panel
  beside it reads "2 DAYS / $3,000" in huge type with a smaller banner
  "32 AGENTS, 5X TRACES". Clean editorial style, bright violet and electric
  cyan palette, 1:1 aspect, no real human faces, high contrast so numbers
  stay readable at 200px.
image: images/26-11-20-0605-04-replit-missions-budget-swarm.png
---

# Replit ปล่อย Missions — "งบ" คือ primitive ใหม่ของ agent UX ที่ platform อื่นยังไม่มี

## TL;DR
- Replit เปิด Missions วันที่ 17 พฤศจิกายน — multi-agent swarm (สูงสุด 32 agents) ทำงานภายใน spending cap ที่ user กำหนดก่อนเริ่ม
- Replit บอกว่าใช้ Missions สร้าง DataCat (platform monitoring ภายในของตัวเอง) เสร็จภายใน 2 วันด้วยงบ $3,000 และอ้างว่า beat Claude Code ที่ 5x บน trace benchmark
- Approval gate บังคับ sign-off ก่อน agent ทำ action ที่กระทบลูกค้า — ติด prospect, ส่ง proposal, แก้ sales material, commit product spec

## เกิดอะไรขึ้น
วันที่ 17 พฤศจิกายน Replit เปิดตัว Missions ซึ่งเป็น product ใหม่ที่พยายามเปลี่ยน UX ของ agentic coding จาก "สั่ง agent ทำทีละ step" เป็น "ตั้ง goal + ตั้งงบ แล้วปล่อย swarm ไปจัดการ" ตัวอย่างใน launch post คือ user ตั้ง spending cap $1,000 สั่งให้สร้าง sales outreach system ให้ Missions ทำการ plan build test iterate ภายใน budget นั้น ถ้าจะต้อง exceed ต้องขอ approval ก่อน

Mechanic ที่ Replit เน้นมีสองส่วน (1) spending limit — user ตั้ง cap ก่อน mission เริ่ม Mission pause ทันทีเมื่อ reach limit และ user ต้อง approve increase (2) action approval — Mission ไม่ทำ action ที่กระทบคนนอกจนกว่า user จะ sign-off ตัวอย่างใน launch post คือ ติด prospect ไม่ได้ ส่ง proposal ไม่ได้ แก้ sales material ไม่ได้ commit product spec ไม่ได้ จนกว่าจะอนุมัติ Replit อ้างใช้ swarm สูงสุด 32 agents ต่อ mission ที่ work concurrent แล้ว coordinate กันผ่าน shared state

Evidence หลัก — Replit บอกว่าใช้ Missions สร้าง DataCat ซึ่งเป็น app monitoring platform ของตัวเอง ภายใน 2 วันด้วย budget $3,000 FourWeekMBA อ้าง benchmark ภายในของ Replit ที่ว่า Missions beat Claude Code 5x บน trace benchmark (metric ที่ measure execution path quality) ซึ่งเป็น vendor claim ต้องระวัง แต่ถ้าแค่ cost-to-ship ที่ $3K สำหรับ internal tool ที่ production-grade เป็น number ที่ enterprise startup หลายรายพยายามทำแล้วไม่ถึง

## ทำไมสำคัญ
สิ่งที่ Replit กำลัง pitch ไม่ใช่ model ที่เก่งกว่า แต่เป็น primitive ใหม่ของ agent UX — budget as first-class citizen ปีที่ผ่านมา agent platform ทั้งหมด (Cursor, Windsurf, Cognition Devin, Claude Code) focus ที่ "agent ทำงานเก่งแค่ไหน" ไม่ค่อยมีใคร pitch "agent ทำงานเก่งแค่ไหน under budget constraint X" การ pricing agent ตาม token หรือ action ปล่อยให้ cost unpredictable — Replit แก้ด้วย budget-first UX

Finding DataCat ($3K/2 days) เป็น proof point ที่ smart — Replit เอา internal tool ที่คน evaluate ได้จริงมาพูด ไม่ใช่ demo abstract คุณอ่าน launch post แล้วคิดว่าใช้ Mission สร้าง SaaS prototype รอบนี้ได้ด้วย budget pattern เดียวกัน ซึ่งเป็น framing ที่ distinct จาก Claude Code (ที่ขาย developer productivity) และ Devin (ที่ขาย autonomy ที่สมบูรณ์แบบกว่าที่ delivery จริง)

Caveat — 32 agents swarm fancy มาก แต่คำถามคือ coordination cost เท่าไหร่ ที่ scale นี้ shared state มักกลายเป็น bottleneck และ context pollution (agent A เขียนสิ่งที่ agent B ยกเลิกแล้ว) ก็เพิ่มขึ้นมาก Replit ไม่เปิดเผย architecture ของ coordination layer ที่ detail Spiritt (คู่แข่งที่ขาย agent swarm คล้ายกัน) เขียน comparison page ชี้ว่า pricing ของ Missions ยังไม่ชัดเจนว่าใครได้สิทธิ์ใช้ และ swarm size limit จะปรับตาม plan ไหน

## มุม AI Agent Platform
Builders — ถ้าคุณ build agent product ลองคิดว่า pricing primitive ของคุณคืออะไร per-seat (Agentforce), per-action (Flex Credit), per-token (model provider), per-budget (Replit Missions) ใครที่ให้ CFO predict คอสต์ได้ง่ายที่สุด จะชนะ enterprise deal rounds ใน Q1 2027 เน้นว่า budget-first UX สร้างง่ายกว่าที่คิด — แค่ meter cumulative spend แล้ว pause เมื่อ reach limit ค่า engineering lift อยู่ที่ UX ของ approval loop ไม่ใช่ metering เอง

Users/business — development team ไทยที่ evaluate "agent IDE" สำหรับ build internal tool ควร ask vendor ว่ามี budget cap ไหมแบบ hard-stop ไม่ใช่แค่ warning ต่างจาก Claude Code และ Cursor ที่ยังเป็น usage-based แบบไม่มี ceiling Replit เป็นเจ้าแรกที่ pitch controlled spending ที่ชัดเจน สำหรับ Enabridge หรือบริษัทที่ pilot agent development นี่คือ pattern ที่ควรเอาไปใช้ตอน sign contract เขียน clause ให้ชัดว่าถ้าเกิน cap ต้องมี human approval

Ecosystem — Anthropic กับ OpenAI ที่ขาย model ต่อ token ไม่น่าจะชอบ framing นี้ เพราะ "budget cap" บังคับให้ orchestrator (Replit) ต้องคุม cost ซึ่งทำให้ orchestrator มี leverage ต่อ model vendor เพิ่มขึ้น ถ้า pattern นี้ scale เราน่าจะเห็น model provider เริ่ม expose cost-aware API endpoint ที่ let orchestrator ตัดสินใจ "model นี้คุ้มกับ task นี้ไหม" ภายใน Q2 2027

## Sources
- [Introducing Replit Missions (Replit Blog)](https://replit.com/blog/introducing-replit-missions)
- [Replit's agent swarms built an app monitoring platform in 2 days on a $3K budget (The New Stack)](https://thenewstack.io/replit-missions-agent-swarms/)
- [Replit Says Missions Beat a Claude Code Build 5x on Traces (FourWeekMBA)](https://fourweekmba.com/ai-replit-says-missions-beat-a-claude-code-build-5x-on-traces/)
- [Replit launches Missions, an agent swarm that works to a budget (Cocoloop)](https://news.cocoloop.cn/en/2026/11/replit-missions-agent-swarm/)

---

## Audio script
Replit เปิดตัว Missions เมื่อวันที่ 17 พฤศจิกายน เป็น product ที่พยายามเปลี่ยน UX ของ agentic coding user ตั้ง goal แล้วตั้ง spending cap ก่อนเริ่ม จากนั้น swarm ที่มี agent สูงสุด 32 ตัว ทำงาน concurrent plan build test iterate ภายในงบนั้น ถ้าจะ exceed ต้องขอ approval ก่อน และก่อนทำ action ที่กระทบลูกค้า เช่น ส่ง proposal หรือติดต่อ prospect agent ต้องรอ sign-off เสมอ

Replit อ้างว่าใช้ Missions สร้าง DataCat แพลตฟอร์ม monitoring ของตัวเองภายใน 2 วันด้วยงบสามพันเหรียญ และบอกว่า beat Claude Code ที่ 5 เท่าบน trace benchmark ซึ่งเป็น internal metric ยังต้องรอ third-party verify

สิ่งที่น่าสนใจกว่าคือ Replit กำลัง pitch primitive ใหม่ของ agent UX — budget as first-class citizen ปีที่ผ่านมาทุก vendor focus ที่ agent ทำงานเก่งแค่ไหน แต่ไม่ค่อยมีใครให้ CFO predict cost ได้ ถ้าคุณกำลัง build agent product ลองถามตัวเองว่า pricing primitive ของเราคืออะไร per-seat, per-action, per-token หรือ per-budget ใครที่ CFO predict cost ได้ง่ายที่สุดจะชนะ deal ใหญ่ใน Q1 ปีหน้าครับ
