---
date: 2026-10-26
slug: forever-security-agentsmd-downloads
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  An editorial isometric illustration of a laptop with a glowing Downloads
  folder open on the desk. Inside the folder sits a single sinister document
  tagged "AGENTS.md" in bold red type, with faint tendrils of code reaching
  up toward a robot avatar at the keyboard. Above the laptop, three stacked
  numbers hang in big display type: "90%+ CODEX HIJACK", "1,300 CLAUDE
  SESSIONS", "NOTHING TO PATCH". A small ribbon on the corner of the folder
  reads "~/Downloads". Deep navy and alarm red palette, strong contrast for
  200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-26-0605-01-forever-security-agentsmd-downloads.png
---

# AGENTS.md ใน Downloads folder hijack Codex + Claude Code — Forever Security บอก "ไม่มีอะไรให้ patch"

## TL;DR
- **22–25 ต.ค.** Forever Security รายงานการโจมตีจริงที่ coding agent บนเครื่องลูกค้ากำลังจะ install npm package malicious `function-color` — สาเหตุคือไฟล์ **AGENTS.md** ใน `~/Downloads` ที่กลายเป็น working directory ของ agent
- **Codex โดน 90%+** ของการทดสอบ, **Claude Code** ตามด้วย CLAUDE.md variant ที่หันทราฟฟิก API ของ agent ไปที่ attacker server (1 รายงานถึงขั้น OAuth token hijack ของ account) — Weizman นับ Claude Code session จาก folder นั้น **1,300+ ครั้ง**
- **Delivery:** หน้าเว็บแค่หน้าเดียวโยน `AGENTS.md` เข้า Downloads ของ Chrome/Edge/Firefox ได้โดยไม่ต้องถาม (Brave ถาม); Downloads เป็น working dir เริ่มต้นเมื่อ developer launch agent ที่โฟลเดอร์นั้น
- **Vendor response:** Forever ยืนยัน *"nothing here for OpenAI or Anthropic to patch — an agent that follows AGENTS.md in its folder is doing exactly what it was built to do"* — ปัญหาคือ by-design behaviour ของ instruction-file loading
- Signal: **AGENTS.md กลายเป็น prompt injection surface อันดับหนึ่งของ coding agent** — เพราะทั้ง Codex, Claude Code, Cursor, และ VS Code Chat ล้วน auto-load ไฟล์นี้โดย default

## เกิดอะไรขึ้น

วันพุธที่ **22 ต.ค.** Forever Security — บริษัท monitoring ด้าน agent security — ตรวจเจอว่า coding agent บนเครื่องลูกค้ารายหนึ่ง (ยังไม่เผยชื่อ) **กำลังจะติดตั้ง npm package ชื่อ `function-color`** ซึ่งเป็น malware ที่รู้จักแล้วใน npm registry. ตัว agent รันคำสั่งเพราะมี AGENTS.md ในโฟลเดอร์งาน แต่ **AGENTS.md ตัวนั้นไม่ได้อยู่ใน repo ของลูกค้า** — มันอยู่ใน `~/Downloads` ซึ่งเป็น working directory ที่ developer คนนั้นใช้ launch agent

จุดที่ทำให้เรื่องนี้แปลกจาก prompt injection ปกติคือ **delivery vector**: Forever ยืนยันว่าเพียงเปิด web page หนึ่ง (payload อยู่หลัง link ธรรมดา) **Chrome / Edge / Firefox จะ save file ไปที่ `~/Downloads` โดยไม่ถาม** — เพราะ default download behaviour คือไม่ prompt. Brave เป็นข้อยกเว้นเดียวที่ขออนุญาตก่อน save. นั่นแปลว่า developer ที่เปิดดูเว็บแล้ว switch กลับไปรัน coding agent ที่โฟลเดอร์ Downloads **ไม่จำเป็นต้องรู้ตัวเลยว่ามีไฟล์แปลกถูก drop** — agent ก็ load ไฟล์เป็น instruction ทันที

Forever ทดสอบ reconstructed attack กับ Codex ด้วย payload ไม่อันตราย (แค่สั่งเปิด Calculator app) — **success rate เกิน 90%**. กับ Claude Code ที่ hardened กว่า Forever ต้องเปลี่ยนวิธี: ใช้ CLAUDE.md ที่ redirect API traffic ของ agent ไปที่ server ของตัวเอง, บาง version ของการ report ระบุว่าถึงขั้น **leak OAuth token แล้ว hijack account** ด้วยคำสั่งเดียวใน markdown. researcher Gal Weizman รายงานว่า Claude Code **launch session จาก folder นั้นไปแล้ว 1,300+ ครั้ง** ก่อนที่จะมีใครรู้ตัว

สิ่งที่ทำให้ Forever ตั้งหลังชนฝา: *"There is nothing here for OpenAI or Anthropic to patch. An agent that follows the AGENTS.md in its folder is doing exactly what it was built to do."* — vulnerability ไม่ใช่ bug แต่เป็น **feature contract** ของ coding agent ทั้ง industry: AGENTS.md ใน working dir = ground truth instructions

## ทำไมสำคัญ

ประเด็นที่หนึ่ง — **AGENTS.md กลายเป็น prompt injection surface อันดับหนึ่งของ coding agent ทั้งหมด**. เริ่มจาก OpenAI's AGENTS.md spec ที่ปัจจุบัน Linux Foundation host ภายใต้ AAIF (ประกาศ 22 ก.ค.) ทำให้ Codex, Cursor, Claude Code, Antigravity, VS Code Chat, Zed และ 70+ platform load ไฟล์เดียวกัน. Prompt Security (ธ.ค. 25) + NVIDIA AI Red Team (ก.ค. 26) + Mirage Security (ส.ค. 26) ทั้งหมดเตือนประเด็นเดียวกันมา 10 เดือน — แต่คราวนี้ Forever พิสูจน์ว่า **"attacker ไม่ต้องแตะ repo"** ก็ pwn agent ได้ แค่ควบคุม working directory ของ developer (ซึ่ง Downloads = default สำหรับคนทั่วไปที่ clone repo ล่าสุด)

ประเด็นที่สอง — **"nothing to patch" คือ framing ที่น่ากลัวที่สุด**. เมื่อ security research พบ CVE ปกติ vendor patch แก้ภายในสัปดาห์. แต่คราวนี้ Forever ยืนยันว่าถ้า Codex / Claude Code เลิก load AGENTS.md จาก working dir, feature ที่ developer พึ่งพาที่สุดจะพัง. ทางเลือกเหลือสาม: (1) sandbox agent ให้ไม่สามารถ run npm/pip/apt command โดย default (แพง, UX แย่), (2) ใช้ Anthropic's sandbox-runtime (ปล่อย open-source 24 ต.ค. ตามที่ brief เมื่อวานรายงาน) — จะต่อสายช่วยเรื่องนี้ตรง, (3) **ให้ IDE / shell** warn developer ก่อนรัน agent ที่ working dir ที่ไม่ใช่ repo. ข้อ 3 ต้อง convention ของ industry — ยังไม่มีใครทำ

ประเด็นที่สาม — **ปรากฏการณ์นี้บอกชัดว่า agent security ไม่ใช่ "nice to have" แล้ว แต่เป็น shipping blocker**. Mave เพิ่งปล่อย $34M (22 ต.ค.) เพื่อทำ agentic SecOps ตั้งแต่ day 1, Opsin $21M (15 ต.ค.) เน้นการ map ว่า agent ตัวไหนทำอะไรได้บ้าง, 1Password for Agents (brief 24 ต.ค.) ลาก trust layer เข้ามาคั่น, Sumsub KYA Module for MCP (19 ต.ค.) screen agent request ก่อนถึง MCP server. ตลาดคาดการณ์ **agent security category** กำลังโตเร็วกว่า agent framework

## มุม AI Agent Platform

สำหรับ **Builders** (framework / orchestration / coding agent): ต้องยอมรับว่า **working directory เป็น trust boundary**. design decision ที่น่าทำคือ (1) auto-detect ว่า folder มี `.git` + remote ที่ developer เชื่อถือหรือไม่ ก่อนจะ load AGENTS.md, (2) hash + sign AGENTS.md เป็น convention — ไฟล์ที่ไม่มี signature trusted developer ไม่ควรถูก load เป็น instruction (ขอ user confirm แทน), (3) **isolate network + filesystem** โดย default ด้วย sandbox-runtime (Anthropic เพิ่งเปิด open-source) — agent ยังทำงานได้ แต่ไม่สามารถ reach outbound network โดยไม่ขอ. Cursor + Claude Code ที่กำลังเร่ง Computer Use (ตามที่ brief 25 ต.ค. รายงาน) ยิ่งต้องแยก working dir ให้ชัด

สำหรับ **Users / Business**: ถ้าใช้ Codex / Claude Code / Cursor ภายในองค์กร ให้ออก policy ชัดว่า (1) ห้าม launch coding agent ที่ `~/Downloads`, `~/Desktop`, หรือ `/tmp`, (2) force clean checkout ของ repo ที่ hash-verified ก่อน agent run, (3) deploy EDR / endpoint tool ที่ detect `AGENTS.md` / `CLAUDE.md` ที่ไม่ได้มาจาก git. Enterprise security team ที่ตอนนี้ยังมอง "coding agent = developer tool" ต้อง pivot: **coding agent = unprivileged user ที่พกใบลาราชการ** — ต้องมี audit trail ทุก action และ network outbound ต้องผ่าน proxy

สำหรับ **Ecosystem**: AAIF ที่ host MCP + AGENTS.md ตอนนี้ต้องขยับ **spec change proposal** ให้ AGENTS.md มี signature / source URL ที่ verifiable (ไม่ใช่แค่ markdown ไฟล์เปล่า). ไม่งั้น Fortune 500 CISO ที่กำลัง pilot coding agent ปลายปี 2026 จะชะลอ roll-out ทั้ง stack

## Sources
- [AI coding agents hijacked using AGENTS.md file in Downloads folder (BleepingComputer)](https://www.bleepingcomputer.com/news/security/ai-coding-agents-hijacked-using-agentsmd-file-in-downloads-folder/)
- [A web page can plant AGENTS.md in your Downloads folder: Codex obeyed it in over 90% of attempts (DEV)](https://dev.to/piekwerk/a-web-page-can-plant-agentsmd-in-your-downloads-folder-codex-obeyed-it-in-over-90-of-attempts-342h)
- [Forever Security traced an AI agent's attempted malware install to Downloads (RuntimeWire)](https://runtimewire.com/article/forever-security-ai-agent-downloads-folder-instructions)
- [Mitigating Indirect AGENTS.md Injection Attacks in Agentic Environments (NVIDIA AI Red Team)](https://developer.nvidia.com/blog/mitigating-indirect-agents-md-injection-attacks-in-agentic-environments/)

---

## Audio script
วันที่ 25 ตุลาคม Forever Security บริษัทที่ทำ security monitoring สำหรับ AI agent รายงานการโจมตีที่น่าจะเปลี่ยนวิธีคิดเรื่อง coding agent ทั้งหมด. ทีมเจอว่า coding agent บนเครื่องลูกค้ากำลังจะติดตั้ง npm package ที่เป็น malware ชื่อ function-color. สาเหตุไม่ได้มาจาก repo ที่ลูกค้าทำงานอยู่ แต่มาจากไฟล์ชื่อ AGENTS.md ในโฟลเดอร์ Downloads ซึ่งกลายเป็น working directory ของ agent. วิธี deliver ไฟล์คือเว็บเพจเดียว เพราะ Chrome Edge Firefox จะเซฟไฟล์ไป Downloads โดยไม่ถาม — Brave เป็นข้อยกเว้นที่ขออนุญาตก่อน. Forever ทดสอบ reconstruct attack กับ Codex ได้ success rate เกิน 90 เปอร์เซ็นต์ ส่วน Claude Code ต้องเปลี่ยนเป็น CLAUDE.md ที่ redirect traffic ของ agent ไป server attacker ซึ่งบาง version ของ report ระบุถึงขั้น hijack OAuth token ได้. researcher รายงานว่า Claude Code launch session จากโฟลเดอร์นั้นไปแล้ว 1,300 ครั้ง ก่อนจะมีใครรู้. จุดที่ Forever ย้ำคือไม่มีอะไรให้ OpenAI กับ Anthropic patch — เพราะ agent ทำสิ่งที่มันถูก design ให้ทำพอดี load AGENTS.md จาก working dir. ประเด็นต่อจากนี้มีสาม หนึ่ง AGENTS.md ตอนนี้คือ prompt injection surface อันดับหนึ่งของ coding agent ทั้ง industry — 70+ platform ที่ integrate ตั้งแต่ Codex Cursor Antigravity VS Code Chat ล้วน load ไฟล์เดียวกัน. สอง framing nothing to patch น่ากลัวที่สุด — ทางเลือกเหลือสาม sandbox agent, deploy sandbox-runtime ของ Anthropic ที่เปิด open-source เมื่อ 24 ตุลาคม, หรือให้ IDE เตือน developer ก่อน launch ที่ working dir ที่ไม่ใช่ repo. สาม agent security กลายเป็น shipping blocker — ตลาดเริ่มสะท้อนด้วย Mave 34M Opsin 21M 1Password for Agents และ Sumsub KYA Module ที่ประกาศในเดือนเดียวกัน. สำหรับ enterprise ถ้าใช้ Codex Claude Code Cursor ควรออก policy ห้าม launch agent ที่ Downloads Desktop หรือ tmp และ force clean checkout พร้อม audit trail ก่อน agent รัน
