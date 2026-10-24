---
date: 2026-10-23
slug: cursor-computer-use-desktop
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a developer's desk showing a laptop
  running the Cursor IDE with a glowing cursor icon labeled "AGENT" clicking
  across three stacked windows: an Xcode-like IDE, an iOS Simulator phone,
  and a Chrome browser. Above the laptop, three stacked numbers hang in big
  display type: "ANY DESKTOP APP", "ONE TASK, THREE WINDOWS",
  "macOS / LINUX". A small permission dialog floats to the side reading
  "ACCESSIBILITY + SCREEN RECORDING". Deep navy and electric blue palette,
  strong contrast for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-25-0605-05-cursor-computer-use-desktop.png
---

# Cursor Computer Use เข้าสู่ desktop IDE — coding agent คลิกใน iOS Simulator, Xcode, และ browser ได้ในคำสั่งเดียว

## TL;DR
- **23 ต.ค.** Cursor ปล่อย **Computer Use** เข้า **desktop IDE** — coding agent สามารถคลิก, พิมพ์, screenshot, และควบคุม GUI app นอก browser (iOS Simulator, Xcode, Figma, อื่น ๆ) ของ developer เอง, บน **macOS + Linux**
- Setup ต้อง **grant Accessibility + Screen Recording** permission บน macOS; agent รัน task เดียวที่ต้อง span หลาย window ได้ (เช่น "build feature + test ใน Simulator + revise code")
- ก่อนหน้านี้ Cursor มี Computer Use แค่ใน **cloud agent (isolated VM)** และ **self-hosted worker**; version นี้คือครั้งแรกที่ local developer machine ถูกควบคุมโดย agent ตรง ๆ
- Signal: **boundary ระหว่าง "coding agent" กับ "computer use agent" หายไป** — Cursor + Anthropic Claude Code + OpenAI Codex จะเริ่ม compete กันบน "ควบคุม GUI ของ developer" ไม่ใช่แค่ generate code

## เกิดอะไรขึ้น

วันพฤหัสที่ **23 ต.ค.** Cursor (coding IDE ยอดนิยมที่ประเมิน valuation ~$10B รอบล่าสุด) ปล่อย **Computer Use** feature เข้าสู่ **desktop IDE version** — ก่อนหน้านี้ feature นี้มีแค่ใน **cloud agent (isolated VM, full desktop)** และ **self-hosted worker ที่รันบน Linux/macOS** หลังจาก update, local Cursor สามารถให้ coding agent **click, type, screenshot, และควบคุม GUI app นอก browser** โดยตรงบน machine ของ developer เอง

ตามเอกสารของ Cursor + Flavio Copes (independent developer blogger ที่ cover ตอน release): ตัวแรกใน macOS **ต้อง grant Accessibility + Screen Recording permission**. Accessibility ให้ agent คลิก/พิมพ์กับแอป, Screen Recording ให้ agent "เห็น" ว่า screen อยู่ที่ไหน. ตัวอย่าง task ที่ Copes ทำให้ดู: **ให้ agent build iOS feature + test ใน Simulator + revise code เป็น loop เดียว** — agent เขียน Swift code, launch Simulator, คลิก button ใน app, อ่าน output ที่ปรากฏ, revise code, run ใหม่

Cursor คร่าว ๆ ก่อนหน้านี้มีสามโหมดของ "agent control": (1) **cloud agent** ที่รันใน isolated VM บน Cursor infrastructure (เช่น Devin style), (2) **self-hosted worker** ที่รันบน machine ขององค์กร, และ (3) **local coding agent** ที่แก้ไข code แต่ไม่คุม GUI. version นี้คือการขยาย (3) ให้ครอบคลุม GUI control. ต่างจาก (1) ตรงที่ **agent ควบคุม machine ของคุณจริง** — ถ้าทำพลาด screenshot, คลิก, type ไปที่ app ใด ๆ ที่คุณเปิดอยู่ (รวมถึง browser ที่ login Google หรือ Slack)

จุดที่ Flavio Copes เน้นในรีวิวคือ **productivity leap** สำหรับงาน mobile dev + visual testing — ก่อนหน้านี้ไม่มี agent ที่คุม iOS Simulator หรือ Android Emulator ได้โดยที่ developer ไม่ต้อง switch context. Cursor Computer Use ปิดช่องว่างนั้น

## ทำไมสำคัญ

ประเด็นที่หนึ่ง — **"coding agent" กับ "computer use agent" รวมเป็นสิ่งเดียวกันแล้ว**. ตอนที่ Anthropic ปล่อย Computer Use (ต.ค. 2024) และ OpenAI ปล่อย Operator (ม.ค. 2025), ตลาดคิดว่า category แยกจาก coding agent: computer use = "ทำงาน admin, จองตั๋ว, SaaS workflow", coding agent = "แก้ codebase". Cursor Computer Use ลบ boundary นั้น — เพราะ **developer workflow ส่วนใหญ่ไม่ได้อยู่ใน codebase อย่างเดียว** มันข้าม Xcode, Simulator, Chrome DevTools, Figma, Postman, Terminal

ประเด็นที่สอง — **เสี่ยง security มากขึ้นหลายขั้น**. Accessibility + Screen Recording permission ให้ agent **เห็นและควบคุม window ไหนก็ได้** รวมถึง browser ที่ login Google, Slack, 1Password manager, email. ถ้า prompt injection ผ่าน webpage หรือ code comment ให้ agent "ไปอ่าน password manager แล้ว copy ตัว API key ไป paste ที่ Slack ของ attacker" — ไม่มี sandbox ปิดตรง ๆ ที่ชั้นนี้. Anthropic sandbox-runtime (ข่าว 03) ไม่ครอบคลุม Computer Use layer; ต้องรอ **1Password for Agents** (ข่าวเมื่อ 22 ต.ค.) + **ServiceNow AI Passport** (ข่าว 23 ต.ค.) ขยายมาถึง IDE level

ประเด็นที่สาม — **Cursor กำลังเร่ง moat ก่อน OpenAI/Anthropic ลง IDE โดยตรง**. OpenAI ซื้อ Windsurf ($3B ก.ค. 2025) และ Codex ขยายความสามารถทุกเดือน; Anthropic เพิ่ง launch Claude Code ที่มี built-in Computer Use plan. Cursor ต้องขยาย feature ก่อนที่ foundation lab จะ compete ด้วย first-party product. Replit → OpenAI switch (ข่าว 02) แสดงให้เห็นว่า **model layer คุยกับ customer โดยตรงได้** — Cursor ต้องชัดใจว่า value ของ IDE คือ UX + workflow + enterprise feature ไม่ใช่ model

## มุม AI Agent Platform

สำหรับ **Builders**: ถ้า build coding agent หรือ dev tool, **ต้องวาง roadmap Computer Use ให้พร้อม Q1-Q2 2027**. agent ที่ไม่ควบคุม GUI จะดู limited เทียบกับ Cursor + Claude Code + Codex. integrate ผ่าน Anthropic Computer Use tool, Playwright, หรือ native accessibility API ของ OS. **ข้อควรระวัง**: Cursor เลือกให้ user grant permission ชั่วคราว + ให้ agent รัน task เดียวเท่านั้น — pattern นี้ควรเป็น default, ไม่ใช่ "allow forever"

สำหรับ **Users / Business**: ถ้าทีม dev ใช้ Cursor Enterprise, **เริ่มเขียน policy ว่า Computer Use permission เปิดได้ตอนไหน + กับ app อะไรบ้าง**. default ที่ developer คลิก "allow" ครั้งแรกคือ security exposure ขนาดใหญ่. ให้ security team draft **"Computer Use Acceptable Use Policy"** ที่ระบุ: (1) agent ห้ามเปิด password manager app, (2) agent ห้าม interact กับ Slack/Teams window ที่ login ของบริษัท, (3) activity log ของ Computer Use ต้องเก็บ 90 วัน. ถ้ายังไม่มี policy, อย่าให้ enable production

สำหรับ **Ecosystem**: **IDE market** (Cursor, Zed, JetBrains, VS Code with Copilot) จะแข่งกันบน Computer Use quality + security model ภายใน 2 ไตรมาสหน้า. **Observability tools** (Datadog, New Relic, Honeycomb) ต้องเพิ่ม instrumentation สำหรับ "agent action events" — ว่า agent คลิกที่ไหน, screenshot เมื่อไหร่ — ไม่ใช่แค่ "LLM completion events". **MDM platform** (Jamf, Kandji, Microsoft Intune) ต้อง enforce Computer Use permission policy ที่ระดับ fleet

## Sources
- [How to use Cursor Computer Use (Flavio Copes)](https://flaviocopes.com/cursor-computer-use/)
- [Cursor's Computer Use Lets Its Coding Agent Click Through Desktop Apps (AlphaSignal)](https://alphasignal.ai/news/cursor-s-computer-use-lets-its-coding-agent-click-through-desktop-apps)
- [Cursor computer use and desktop sharing (Cursor Docs)](https://cursor.com/docs/cloud-agent/self-hosted/computer-use)

---

## Audio script
วันพฤหัส 23 ตุลาคม Cursor ปล่อย Computer Use เข้าสู่ desktop IDE — ก่อนหน้านี้ feature นี้มีแค่ใน cloud agent ที่รันใน isolated VM กับ self hosted worker. หลัง update local Cursor สามารถให้ coding agent คลิก พิมพ์ screenshot และควบคุม GUI app นอก browser โดยตรงบน machine ของ developer เอง รองรับ macOS กับ Linux. บน macOS ต้อง grant Accessibility กับ Screen Recording permission. Accessibility ให้ agent คลิกและพิมพ์กับแอป Screen Recording ให้ agent เห็น screen. ตัวอย่างที่ Flavio Copes รีวิวคือ task เดียวที่ให้ agent build iOS feature test ใน Simulator และ revise code เป็น loop — agent เขียน Swift code launch Simulator คลิก button อ่าน output revise code run ใหม่ ไม่ต้อง developer switch context. ความสำคัญสามประเด็น หนึ่ง coding agent กับ computer use agent รวมเป็นสิ่งเดียวกันแล้ว ตอน Anthropic ปล่อย Computer Use ปลาย 2024 กับ Operator ของ OpenAI มกราคม 2025 ตลาดคิดว่าเป็นสอง category — Cursor ลบ boundary นั้น เพราะ developer workflow ส่วนใหญ่ข้าม Xcode Simulator Chrome DevTools Figma Postman Terminal ไม่ได้อยู่ใน codebase อย่างเดียว. สอง เสี่ยง security มากขึ้น Accessibility กับ Screen Recording ให้ agent เห็นและควบคุม window ไหนก็ได้ รวม browser ที่ login Google Slack password manager email ถ้า prompt injection ผ่าน webpage หรือ code comment ไม่มี sandbox ที่ชั้นนี้ Anthropic sandbox runtime ที่เพิ่งปล่อยไม่ครอบคลุม Computer Use ต้องรอ 1Password for Agents กับ ServiceNow AI Passport ขยายมาถึง IDE. สาม Cursor เร่ง moat ก่อน OpenAI กับ Anthropic ลง IDE โดยตรง — OpenAI ซื้อ Windsurf 3 พันล้าน Anthropic launch Claude Code มี Computer Use plan. Cursor ต้องชัดใจว่า value ของ IDE คือ UX workflow enterprise feature ไม่ใช่ model. สำหรับ builder วาง roadmap Computer Use ให้พร้อม Q1 Q2 2027. สำหรับ enterprise ที่ใช้ Cursor เริ่มเขียน policy ว่า Computer Use permission เปิดได้ตอนไหน app อะไรบ้าง default ที่ developer คลิก allow ครั้งแรกคือ security exposure ใหญ่
