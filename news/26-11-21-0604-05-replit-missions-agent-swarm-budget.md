---
date: 2026-11-17
slug: replit-missions-agent-swarm-budget
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a glowing mission control room with
  a giant central dial labeled "BUDGET: $3,000" ticking down. Around it, five
  tiny agent silhouettes fetch files, write code, and stamp approval gates
  labeled "CONTACT PROSPECT", "SEND PROPOSAL", "PRODUCT COMMIT". A banner
  across the top reads "REPLIT MISSIONS" with a subhead "AGENT SWARMS · BUDGET
  GATED · HUMAN APPROVAL". Soft turquoise and warm orange palette, 1:1 aspect,
  no real human faces, high contrast so numbers stay readable at 200px
  thumbnail size.
image: images/26-11-21-0604-05-replit-missions-agent-swarm-budget.png
---

# Replit Missions เปิดให้ delegate งานให้ swarm ของ agent — ผูกด้วย budget cap + approval gate รายขั้น

## TL;DR
- Replit เปิดตัว Missions 17 พฤศจิกายน — product ใหม่ที่ให้ user delegate ทั้ง project ให้ swarm ของ agent (ไม่ใช่งานทีละ task)
- Budget cap set ก่อนเริ่ม, agent หยุดทันทีเมื่อถึงเพดาน + ต้อง human approve ก่อนจะเพิ่มเพดาน
- "Mission Agreement" กำหนด success criteria + action ที่ต้อง human sign-off (เช่น contact prospect, ส่ง proposal, commit product)
- Replit เอง demo: build internal product monitoring platform ใน 2 วันด้วย $3,000 budget
- ยังไม่เปิดราคา Missions เป็น line item, plan access ยังเป็น gated beta

## เกิดอะไรขึ้น
วันที่ 17 พฤศจิกายน Replit เปิดตัว **Missions** — ขั้นต่อยอดจาก Agent ของ Replit ที่เป็น single-agent coding assistant Missions เปลี่ยน UX จาก "คุยทีละข้อความ" เป็น "**ส่งโปรเจกต์หนึ่ง task ไปทั้งก้อน**" user กำหนด goal, budget, และ approval gate → swarm ของ agent (หลายตัวทำงานขนาน) run ไปจนกว่าจะเสร็จหรือ hit cap

สิ่งที่ Replit เน้นหนักที่สุดคือ **spending gate** — ก่อนเริ่ม mission ทุกครั้ง user ต้องตั้ง budget limit ไว้เป็น hard cap Replit check spend ทุก step — เมื่อถึง cap แล้ว agent หยุดใช้ paid service ทันที (model API call, cloud compute, SaaS tool) ถ้า budget หมดก่อนงานเสร็จ mission ค้างไว้ ไม่มีการ auto-charge เพิ่ม การขอเพิ่มเพดานต้อง human approve ก่อน ไม่ใช่ agent เรียกได้เอง

**Mission Agreement** คือ structure ที่ Replit ให้ user define ก่อนเริ่ม: success criteria, actions ที่ agent ต้อง human approve ก่อนทำ (เช่น contact prospect, ส่ง proposal, แก้ sales material, commit product), และ spending cap pattern นี้ต่างจาก Claude Code หรือ Cursor ที่ agent อาจ run shell command ได้ตลอดเวลาโดยไม่มี structured approval

เป็น proof of own eating, Replit ใช้ Missions เองสร้าง internal product monitoring tool ตัวหนึ่ง ใน 2 วันด้วย budget $3,000 แหล่งข่าวต่างกันเรียกชื่อ product ว่า "Radar" หรือ "DataCat" — ไม่ชัดว่าคืออันเดียวกันหรือ 2 ตัว Replit อ้างว่า Missions win trace benchmark ที่ build แข่ง Claude Code ด้วย 5x — แต่ไม่มี benchmark rule ที่ public ให้ verify

**ไม่เปิดราคา** — Missions ยังอยู่ใน gated beta Replit ยังไม่บอกว่าจะ bundle เข้า plan ไหน และไม่บอกว่า parallel agent จำนวนเท่าไหร่ต่อ plan

## ทำไมสำคัญ
ตลาด agentic coding ปี 2026 มีผู้เล่นเยอะ — Claude Code, Cursor Composer, Google Antigravity, GitHub Copilot Agent HQ, OpenAI Codex — แต่ทุกค่ายโฟกัสที่ **single-agent, continuous conversation** Replit เข้าจากข้างตรงกันข้าม — **batch delegation + budget-first UX**

Thesis หลังนี้คือ: developer ไม่ได้อยากคุย chat 10 ชั่วโมงเพื่อให้ agent build product — เขาอยาก fire-and-forget งานไปทั้งก้อน แล้วกลับมาดูผลตอนตื่น แต่ fire-and-forget ที่ไม่มี budget cap = recipe disaster — agent หลงทาง รัน model call เรื่อย ๆ จน bill ทะลุหมื่นดอลลาร์ก่อนที่ user จะรู้ทัน Replit จึงเลือกเริ่มจาก **constraint-first** แทน capability-first — Budget, approval gate, Mission Agreement ก่อนที่จะคุยเรื่อง agent ตัวไหนเก่งแค่ไหน

Pattern นี้ตรงกับ pain point ที่ enterprise CIO รายงานมาทั้งปี — ไม่กลัวว่า agent จะไม่เก่ง กลัวว่า agent จะ **ไม่ stop** ปี 2025-2026 มี incident report หลายกรณีที่ agent spin-loop รัน inference เองจน cloud bill พุ่ง 10-100x ของประมาณการเดิม Mission Agreement ของ Replit = structured abstraction ที่ตอบปัญหานี้โดยตรง

Caveat — "Replit beat Claude Code 5x on traces" เป็น marketing claim ที่ไม่มี benchmark แบบ reproducible, ควร wait for third-party test ก่อนเชื่อ ตัว pricing ยัง opaque ซึ่งทำให้ enterprise procurement ยากที่จะ budget ล่วงหน้า และ "approval gate ทุกครั้ง" อาจทำให้ velocity ช้าเกินไปสำหรับ task บางประเภทที่ไม่ต้องการ safeguard ขนาดนั้น

## มุม AI Agent Platform
**Builders** — ถ้าคุณกำลังสร้าง agent platform ที่ให้ user delegate งาน การเพิ่ม **budget primitive** เป็น first-class concept ใน API/UX ตั้งแต่ day one เป็นเรื่องที่คุ้มลงทุน จะช่วยลด incident ต้นทุน + ทำให้ CFO อยากเซ็น PO ง่ายขึ้น ที่ Replit ทำคือ hard cap + approval ถ้าจะทะลุเพดาน — ไม่ใช่ rate limit ที่ silently throttle

**Users/business** — Mission Agreement เป็น template ที่ enterprise procurement ควรลอก ก่อน onboard agent ลง production ให้ define: 1) agent มี budget cap เท่าไหร่/วัน-เดือน 2) action ไหนต้อง human approve 3) success criteria ที่ agent วัดผลตัวเองได้ Enabridge ที่ build agent platform ให้ลูกค้าไทย ถ้ายังไม่มี budget-cap primitive ให้ลูกค้าตั้งก่อน deploy — คุ้มทำเป็น priority ก่อน feature อื่น

**Ecosystem** — ความ pressure ต่อ Cursor + Claude Code + Antigravity ตอนนี้ไม่ใช่ model benchmark แต่คือ **ปัจจัยการควบคุม** Cursor + Claude Code ยังขาด structured budget primitive — ใช้ได้ไม่จำกัดในขอบของ subscription แต่ไม่มี per-mission cap ที่ user บังคับ Enterprise plan ของทั้งคู่ต้องตาม Mission Agreement ภายใน 6-12 เดือน หรือจะเสีย large procurement deal ให้ Replit และ agent orchestrator อื่นที่มี governance ครบกว่า

## Sources
- [Replit's agent swarms built an app monitoring platform in 2 days on a $3K budget (The New Stack)](https://thenewstack.io/replit-missions-agent-swarms/)
- [Replit Missions Lets Teams Set Budgets for AI Agent Swarms (Technobezz)](https://www.technobezz.com/news/replit-missions-budgets-ai-agent-swarms)
- [Replit launches Missions, an agent swarm that works to a budget (Cocoloop)](https://news.cocoloop.cn/en/2026/11/replit-missions-agent-swarm/)
- [Replit Says Missions Beat a Claude Code Build 5x on Traces (FourWeekMBA)](https://fourweekmba.com/ai-replit-says-missions-beat-a-claude-code-build-5x-on-traces/)

---

## Audio script
Replit เปิดตัว Missions วันที่ 17 พฤศจิกายน เป็น product ใหม่ที่เปลี่ยน UX ของ agent coding จาก คุยทีละข้อความ เป็น ส่งโปรเจกต์ไปทั้งก้อน user กำหนด goal, budget, และ approval gate แล้ว swarm ของ agent หลายตัวทำงานขนาน run ไปจนเสร็จหรือ hit cap สิ่งที่ Replit เน้นหนักที่สุดคือ spending gate ก่อนเริ่ม mission ทุกครั้ง user ต้องตั้ง budget limit เป็น hard cap Replit check spend ทุก step เมื่อถึง cap agent หยุดทันที ไม่มี auto charge เพิ่ม การขอเพิ่มเพดานต้อง human approve ก่อน Mission Agreement คือ structure ที่ user define ก่อนเริ่ม success criteria action ที่ agent ต้อง human approve เช่น contact prospect ส่ง proposal commit product pattern นี้ต่างจาก Claude Code หรือ Cursor ที่ agent run shell command ได้ตลอดเวลาโดยไม่มี structured approval Replit ใช้ Missions เองสร้าง internal product monitoring tool ใน 2 วัน ด้วย budget สามพันดอลลาร์ และอ้างว่าชนะ Claude Code ที่ trace benchmark ห้าเท่า แต่ยังไม่มี benchmark แบบ reproducible ให้ verify ยังไม่เปิดราคา Missions เป็น line item Thesis ของ Replit คือ developer อยาก fire and forget ไปทั้งก้อนแล้วกลับมาดูผลตอนตื่น แต่ fire and forget ที่ไม่มี budget cap คือ recipe disaster ปี 2025 ถึง 2026 มี incident ที่ agent spin loop run inference จน cloud bill พุ่งสิบถึงร้อยเท่า Mission Agreement แก้ปัญหานี้โดยตรง สำหรับ builder การเพิ่ม budget primitive เป็น first class ใน API ตั้งแต่ day one คุ้มลงทุน สำหรับ enterprise procurement ลอก Mission Agreement เป็น template ก่อน onboard agent สำหรับ Cursor Claude Code Antigravity pressure ตอนนี้ไม่ใช่ benchmark แต่คือ governance primitive ต้องมีภายในหกถึงสิบสองเดือน ไม่งั้นเสีย enterprise deal ให้ Replit
