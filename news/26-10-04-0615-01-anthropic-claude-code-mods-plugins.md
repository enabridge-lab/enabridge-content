---
date: 2026-10-04
slug: anthropic-claude-code-mods-plugins
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a glowing Anthropic Claude Code terminal
  prompt being wrapped by three stacked TypeScript brackets labeled "PROMPT",
  "TOOL" and "UI". A chain of middleware onions floats behind, each layer
  stamped "MOD". Below sits a bold version tag "v2.1.287" and a warning
  shield reading "NO SANDBOX". Cinematic deep-indigo and electric-orange
  palette, bold text rendering for 200px thumbnails, no real human faces,
  1:1 aspect. Style of a Wired magazine cover story.
image: images/26-10-04-0615-01-anthropic-claude-code-mods-plugins.png
---

# Anthropic เปิด "Mods" ให้ Claude Code — TypeScript middleware ที่ hook เข้า agent ภายใน, ไม่มี sandbox

## TL;DR
- 1 ต.ค. Anthropic ปล่อย **mods** สำหรับ Claude Code — TypeScript function เล็ก ๆ ที่ hook event ภายใน, rewrite prompt, block/retry tool call, redact secret, แทน UI ได้; ติดตั้งผ่าน `/plugin`
- ต้องใช้ **Claude Code v2.1.287** ขึ้นไป; mods เดินเป็น middleware chain แบบ onion ตาม registration order
- **ไม่มี sandbox** — mod รันด้วย privilege เท่ากับ Claude Code เอง; Team/Enterprise plan ใช้ managed settings จำกัดได้

## เกิดอะไรขึ้น
วันที่ 1 ตุลาคม Anthropic เปิดตัว **Claude Code Mods** — TypeScript function เล็ก ๆ ที่ hook เข้า event ภายในของ agent แล้วเปลี่ยนพฤติกรรม. mod หนึ่งตัวสามารถ rewrite prompt ก่อนถึง model, block หรือ retry tool call, approve/deny permission request, redact secret ออกจาก tool output ก่อน Claude อ่าน, หรือแม้แต่แทนที่ UI element. วิธี ship คือห่อ mod ไว้ใน plugin แล้ว install ด้วย `/plugin` ทั้งใน CLI และ desktop app — ต้องเป็น Claude Code เวอร์ชัน **2.1.287** ขึ้นไป.

ตัวอย่างที่ Anthropic ปล่อยมาเองน่าสนใจ: **TokenWeather** meter บอก context ที่ใช้, **Blast Radius** sample ที่เตือนก่อนรันคำสั่งอันตราย, และ **Replay Theater** ที่ให้ดู session ย้อนหลัง. ที่สำคัญคือ feature ของ Claude Code เองหลายอย่าง — รวมถึง `/diff` และ `AGENTS.md` support — ตอนนี้ถูก implement เป็น mod แล้ว. Anthropic เลยกำลังบอกว่า mod ไม่ใช่ extension layer แต่คือ core ของ agent ที่ถูก expose ให้ developer เขียนทับได้.

ที่ควรกังวลคือ **ไม่มี sandbox**. mod เป็นโค้ดที่รันด้วย privilege เท่ากับ Claude Code เอง — อ่านเขียนไฟล์ได้, start process ได้, call network ได้. โครงสร้าง execution เป็น onion-style middleware chain เรียงตาม registration order ซึ่งแปลว่า mod ตัวที่โหลดก่อนจะ wrap mod ตัวที่โหลดหลัง และถ้า mod ไม่ friendly ตัวหนึ่งเข้ามาในสายโซ่ ก็ควบคุม mod ตัวอื่นได้. Anthropic ใส่ built-in security mod ที่จำกัด user-installed mod สำหรับ Team/Enterprise plan และเครื่องที่มี managed settings ไว้ให้ แต่ย้ำว่า "security bar ของ mod เท่ากับโปรแกรม local ทั่วไป" — คุณต้อง audit code ก่อน install.

## ทำไมสำคัญ
Mods เป็น **tacit admission** ว่า coding agent framework ที่ตลาดต้องการมีสองชั้น — core agent kernel ที่ vendor ดูแล และ user-space ที่ enterprise/developer เขียนเอง. ที่ผ่านมา Claude Code และ Cursor พยายามรวมสองชั้นนี้เป็น black box ที่ configure ด้วย prompt + settings file. แต่พอ user เริ่มขอ "block tool call ที่ touch production", "redact token อัตโนมัติ", "retry เมื่อ model ตอบ hallucination" — tier settings ตอบไม่ได้. Mods ยอมให้ user เขียน TypeScript hook ที่ run ก่อนและหลังทุก event — ชัดเจนกว่า "customize prompt" ที่ Cursor ให้.

เทียบกับ **ChatGPT Work** และ **Microsoft Autopilot** ที่กำลัง ship ในช่วงเดียวกัน — ทั้งสองวาง positioning เป็น "digital teammate" ที่ configure ไม่ได้ลึกเท่า; Anthropic เลือกคนละทางคือเปิด API ภายในให้ developer. นี่ตอกย้ำ pattern ที่เห็นมาตลอด Q3 2026 — **frontier model แข่งราคาที่ model layer, differentiate ที่ developer surface**. Argon vs GPT-6.1 Sol pricing match แล้ว, Mods เป็น non-price moat ที่ Anthropic ลงทุนก่อน.

## มุม AI Agent Platform
สำหรับ **Builders** ที่สร้าง agent framework หรือ IDE extension: Mods เป็น template ที่น่าเลียน — expose middleware chain + typed event bus ให้ user ของคุณเขียน hook ด้วยภาษาที่พวกเขาใช้อยู่แล้ว. ถ้า framework ของคุณบังคับ YAML config หรือ prompt template ล้วน ๆ อยู่ ให้คิดใหม่ภายใน 60 วัน — standard ใหม่กำลังจะเลื่อนเป็น "เขียน TypeScript/Python function". สำหรับ **Users** ที่ deploy coding agent ใน team: ถึงเวลาตั้ง governance policy ก่อนที่ dev จะเริ่ม install mod จาก public registry; marketplace ของ mod จะเกิดในไม่กี่สัปดาห์ และ supply-chain risk จะตามมา — เพราะไม่มี sandbox. สำหรับ **Ecosystem**: expect ให้ Cursor, Windsurf, Zed, Aider ปล่อย equivalent plugin API ภายใน 90 วัน; ส่วน security vendor อย่าง Snyk/Semgrep/Socket จะมี product ใหม่สำหรับ "scan AI agent plugin" ก่อนสิ้นปี.

## Sources
- [Anthropic Launches Claude Code Mods, TypeScript Agent Hooks](https://aiweekly.co/alerts/anthropic-launches-claude-code-mods-typescript-agent-hooks)
- [Claude Code Adds "Mods" That Let Developers Change Its Internal Processing and Interface](https://xenospectrum.com/en/claude-code-mods-controls/)
- [Claude Code Mods Are Not Sandboxed](https://fourweekmba.com/ai-claude-code-mods-extensibility-control/)
- [Claude Code mods land in 2.1.287 with deep access, no sandbox](https://www.sourcetrail.com/mods/claude-code-mods-land-in-2-1-287-with-deep-access-and-no-sandbox/)

---

## Audio script
วันที่ 1 ตุลาคม Anthropic ปล่อย Mods ให้ Claude Code — เป็น TypeScript function เล็ก ๆ ที่ hook เข้า event ภายในของ agent แล้วเปลี่ยนพฤติกรรมได้ตั้งแต่ rewrite prompt ก่อนถึง model, block หรือ retry tool call, redact secret ก่อน Claude อ่าน, ไปจนถึงแทน UI. ติดตั้งผ่าน slash plugin บน CLI และ desktop app ต้องเป็น Claude Code เวอร์ชัน 2.1.287 ขึ้นไป. ที่น่าสนใจคือ feature ของ Claude Code เองหลายอย่าง เช่น slash diff และ AGENTS.md support ตอนนี้ถูก implement เป็น mod แล้ว เลยกลายเป็นว่า mod ไม่ใช่ extension layer แต่คือ core ที่ expose ให้ developer เขียนทับได้. ข้อควรระวังคือ mod ไม่มี sandbox รันด้วย privilege เท่าโปรแกรม local ทั่วไป เขียนเป็น middleware chain แบบ onion ที่ตัวโหลดก่อน wrap ตัวโหลดหลัง — ถ้า mod ไม่ friendly เข้ามาในสายโซ่ก็ควบคุม mod ตัวอื่นได้. Signal สำคัญคือ frontier model แข่งราคาแล้ว ตอนนี้ differentiator ของ Anthropic คือ developer surface. ถ้าคุณเป็นทีมที่ใช้ Claude Code ให้ตั้ง governance policy ก่อนที่ dev จะเริ่ม install mod จาก public registry เพราะ marketplace กำลังจะเกิดในไม่กี่สัปดาห์และ supply chain risk จะตามมาแน่.
