---
date: 2026-10-20
slug: microsoft-copilot-studio-hooks-guardrails
topic: agentic-ai
reading_time_min: 2
sources: 3
image_prompt: |
  Editorial isometric illustration of a factory conveyor belt carrying
  an "AGENT TOOL CALL" package. Above the belt a vertical glowing gate
  stamped "HOOK" blocks the package mid-air. Side panels on the gate
  list three triggers in bold text: "ON SESSION START", "ON TOOL BEFORE",
  "ON TOOL AFTER". Behind, a sign on a wall reads "COPILOT STUDIO
  PREVIEW". Deep purple-navy background, warm orange accents on the
  gate, high-contrast type readable at 200px thumbnail. 1:1 aspect,
  no real human faces.
image: images/26-10-20-0607-04-microsoft-copilot-studio-hooks-guardrails.png
---

# Microsoft เปิด Hooks ใน Copilot Studio — agent workflow มี "ปุ่ม pause" ก่อนเรียก tool

## TL;DR
- Microsoft เปิด **Hooks** ใน Copilot Studio เป็น public preview (ช่วง 7–12 ต.ค. 2026) — workflow เล็ก ๆ ที่ fire ตาม event ของ agent: session start, before tool call, after tool call
- Hook สามารถ inspect / modify / block tool call ก่อนรัน — เป็น primitive สำหรับ policy enforcement + approval gate ที่ agent framework ส่วนใหญ่ยังไม่มี built-in
- Preview นี้ยังจำกัดเฉพาะ agent ที่สร้างบน GitHub Copilot harness — เป็นสัญญาณว่า Microsoft กำลัง unify agent runtime ของ GitHub และ Copilot Studio

## เกิดอะไรขึ้น
ช่วงต้น-กลาง ต.ค. 2026 Microsoft Copilot Studio เริ่มเปิด **Hooks** เป็น public preview — primitive ใหม่สำหรับสร้าง workflow ที่ fire ตาม event ของ agent. event ที่ supported ตอนนี้มี: **on session start** (ก่อน agent เริ่มงาน), **on tool before** (ก่อน agent เรียก tool), **on tool after** (หลัง agent ได้ผล). Hook เป็น workflow ที่เขียนด้วย Copilot Studio เอง — สามารถ inspect payload ของ tool call, modify มัน, หรือ block ไม่ให้รันเลยก็ได้. Blog ของ Copilot Studio CAT team วันที่ 12 ตุลาคม 2026 ยืนยัน preview นี้บน copilotstudio.preview.microsoft.com. BraivIQ editorial ระบุว่า Jason Moore, VP of Product สำหรับ Copilot Studio ประกาศเรื่องนี้วันที่ 7 ตุลาคม — ซึ่ง conflict กับวันของ CAT blog เล็กน้อย — อาจเป็น announcement กับ follow-up post

ที่ควรรู้คือ preview นี้ยังจำกัดเฉพาะ agent ที่สร้างบน **GitHub Copilot harness** เท่านั้น — ไม่ใช่ agent ทุกตัวใน Copilot Studio. นี่คือสัญญาณชัดว่า Microsoft กำลัง unify agent runtime ของ GitHub Copilot และ Copilot Studio ให้เป็น stack เดียวกัน — ดีกว่าแยก 2 ค่ายใน Microsoft ที่ลูกค้า confuse กันตลอด

Microsoft เองย้ำใน documentation ว่า Hook **ไม่ควรเป็น safeguard เดียว** สำหรับ business-critical rule — เป็น defense-in-depth ไม่ใช่ ultimate gate

## ทำไมสำคัญ
Hooks เป็น primitive ที่ agent framework ชั้น open-source (LangGraph, AutoGen, CrewAI) มีมาก่อนในชื่ออื่น — "middleware", "callback", "interceptor" — แต่การที่ Microsoft เปิดเป็น first-class citizen ใน Copilot Studio กับ GUI ที่ non-developer ลาก-วางได้ เป็นการ "productize" primitive นี้ให้ enterprise ใช้งานจริง. ที่น่าสังเกตคือ hooks มาพร้อม Managed Runtime และ Apps ใน Copilot Studio update รอบนี้ — รวมกันเป็น "agent control + runtime + hosting" ที่ enterprise ซื้อเป็น bundle แบบไม่ต้องประกอบเอง

ความหมายในวงกว้างคือ **approval gate + policy enforcement กำลังเป็น table stakes** ของ agent platform. Google ทำผ่าน Agent Gateway, Microsoft ทำผ่าน Hooks + Managed Runtime, Workday ทำผ่าน Agent Harness guardrails. ค่ายไหนไม่มี primitive นี้ภายใน 6 เดือน จะไม่ผ่าน procurement ของ enterprise. Open-source framework ต้องตอบว่าจะ bundle policy engine เข้ามายังไง — ไม่งั้นต้องยอมเป็น "runtime ล่าง" ที่ platform ค่ายใหญ่ wrap ไว้

## มุม AI Agent Platform
สำหรับ **Builders** — ถ้าใช้ LangGraph หรือ AutoGen อยู่แล้ว เริ่มคิดว่า hook/middleware ของตัวเอง compatible กับ pattern ของ Copilot Studio ยังไง (on session start / on tool before / on tool after) เพราะ pattern นี้น่าจะเป็น de-facto. สำหรับ **Users / business** ที่ใช้ Microsoft 365 — ถ้ากำลัง pilot agent ควรเริ่มออกแบบ hook เป็น approval gate สำหรับ action ที่กระทบ external system (ส่งเงิน, แก้ customer record, ส่งอีเมลภายนอก) — น้ำหนักของ internal audit จะได้ไม่หนัก. สำหรับ **Ecosystem** — GitHub Copilot harness กำลังกลายเป็น runtime พื้นฐานของทั้ง Microsoft agent portfolio — เป็นสัญญาณว่า acquisition GitHub จ่าย dividend ให้ Microsoft ชัดในชั้น infrastructure. แต่ค่ายที่ bet บน Copilot Studio UI (low-code) จะต้องรอฟีเจอร์แบบนี้นานกว่าคน dev หน่อย

## Sources
- [Hooks in Copilot Studio: Give Your Agent More Than Instructions (Microsoft Copilot Studio CAT Blog)](https://microsoft.github.io/mcscatblog/posts/hooks-in-copilot-studio/)
- [Copilot Studio Adds Apps, Hooks, and Foundry IQ (Zeniteq)](https://www.zeniteq.com/copilot-studio-adds-apps-hooks-and-foundry-iq-rtgymd)
- [Workflow Automation With Hard Stops: Agent Hooks (BraivIQ)](https://www.braiviq.com/blog/workflow-automation-agent-hooks-approval-gates)

---

## Audio script
Microsoft เปิดฟีเจอร์ชื่อ Hooks ใน Copilot Studio เป็น public preview สัปดาห์ที่แล้ว. Hook เป็น workflow เล็ก ๆ ที่ fire ตาม event ของ agent — มีสาม event หลัก. หนึ่ง on session start — รันก่อน agent เริ่มงาน. สอง on tool before — รันก่อน agent เรียก tool. สาม on tool after — รันหลัง agent ได้ผล. Hook สามารถ inspect call, แก้มัน, หรือ block ไม่ให้รันเลยก็ได้ — เป็น approval gate แบบ built-in. ที่น่าสังเกตคือ preview นี้ยังจำกัดเฉพาะ agent ที่สร้างบน GitHub Copilot harness ซึ่งเป็นสัญญาณชัดว่า Microsoft กำลังรวม runtime ของ GitHub Copilot กับ Copilot Studio ให้เป็น stack เดียว. ความหมายในวงกว้างคือ approval gate กำลังเป็น table stakes ของ agent platform. Google มี Agent Gateway, Workday มี Agent Harness, Microsoft มี Hooks — ค่ายไหนไม่มี primitive แบบนี้ภายในหกเดือนจะไม่ผ่าน procurement ของ enterprise. สำหรับคนที่ใช้ Microsoft 365 แล้วกำลัง pilot agent — เริ่มออกแบบ hook เป็น approval gate สำหรับ action ที่กระทบ external system เช่น ส่งเงิน แก้ customer record ส่งอีเมล — audit จะได้ไม่หนัก. และ Microsoft เองย้ำว่า hook ไม่ควรเป็น safeguard เดียวสำหรับ business-critical rule
