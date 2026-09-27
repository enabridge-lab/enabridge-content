---
date: 2026-09-26
slug: claude-code-48k-files-windows-junction
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a Windows folder tree being deleted at
  breakneck speed, with three glowing red numbers stacked on the right:
  "48,000 FILES", "103 SECONDS", "0 GIT HISTORY". A tiny robot with a broom
  sweeps files into a bin while a warning banner overhead reads
  "JUNCTION FOLLOWED". Cinematic navy-and-crimson palette, sharp contrast for
  200px thumbnails, no real human faces, 1:1 aspect. Editorial illustration in
  the style of a Bloomberg cybersecurity cover.
image: images/26-09-28-0616-01-claude-code-48k-files-windows-junction.png
---

# Claude Code ลบไฟล์โปรเจ็คต์ 48,000 ไฟล์ใน 103 วินาที — บทเรียนราคาแพงเรื่อง sandbox บน Windows

## TL;DR
- Developer เปิด task "#873" ให้ Claude Code rebuild mirror — agent เขียน Python script ลบ mirror เก่า แล้วเดินทะลุ Windows directory junction เข้าไปลบไฟล์จริง 48,218 ไฟล์ พร้อมยับ Git object store ใน 103 วินาที
- Root cause คือ `os.walk()` ที่ปิด `followlinks` แต่ไม่ detect junction ของ Windows — agent มองเห็น 614 junction เป็น folder ธรรมดา
- Case study สด ๆ ที่ทุก platform ต้องเอาไป retro: "permission ให้ทำงาน" ไม่ใช่ "permission ให้เขียน implementation ที่ไม่ปลอดภัย"

## เกิดอะไรขึ้น
คืนวันที่ 25 กันยายน ตามเวลา ET ระหว่าง 22:10:31 ถึง 22:12:14 น. Reddit user โพสต์รายงานที่ต่อมาถูกจับตาโดย TechRadar, Cybersecurity News, และ Android Headlines — Claude Code agent ทำงาน task "#873" ที่ให้ rebuild mirror ของ project tree บน Windows แล้ว agent ค้นพบว่า `build_mirror.py` ตัวเดิมไม่สามารถ refresh mirror in-place ได้ เลย **เขียน Python script ใหม่ของตัวเอง** เพื่อลบ mirror เก่าที่อยู่ใน temporary location ก่อน จะได้ create fresh copy.

Mirror ที่จะลบมี 7,332 ไฟล์ปกติ + 614 Windows directory junction ที่ point กลับเข้าไปใน "Dashboard tree" ที่เป็น production project. Script ใช้ `os.walk()` โดยตั้ง `followlinks=False` — เพื่อป้องกันเดินตาม symlink — แต่บน Windows `followlinks` ไม่ครอบคลุม directory junction. Agent เลยเดินทะลุ junction เข้าไปทั้ง 614 ทาง แล้วลบไฟล์ในโปรเจ็คต์จริงทั้งหมด รวมถึง `.git/objects/` ทำให้ history recover ไม่ได้ด้วย.

รายงานเปิดเผยตัวเลขชัด — 48,218 ไฟล์ ถูกลบภายใน 103 วินาที เมื่อคำนวณเป็นอัตราคือ ~468 ไฟล์/วินาที ที่ agent ยิงคำสั่งลบต่อเนื่องไปทั้งคืน ผ่าน tool permission ที่ user เคยกดยอมรับให้ในตอนต้น task. หลังจบ agent ตอบกลับด้วยข้อความ "I broke something" แล้วก็ apologize — ในขณะที่ทั้ง repo หายไปเรียบร้อยแล้ว. ข่าวนี้กลายเป็น top story ของ Hacker News วันที่ 26 ก.ย. ก่อนจะไหลไปยังหน้าข่าว mainstream ภายใน 24 ชั่วโมง.

## ทำไมสำคัญ
Story นี้ต่างจาก "AI จะครองโลก" clickbait ตรงที่ **root cause เป็น engineering bug ที่จับต้องได้** — Windows junction กับ Python stdlib. คน dev ทุกคนที่เขียน mirror script บน Windows เคยเจอ edge case นี้ แต่ agent เดินไปเจอตอนที่ human ไม่ได้ review แต่ละบรรทัดของ implementation. นี่คือ shape ของ agentic failure ที่ต่างจาก classic bug — agent ได้ **authority ให้ทำงานให้จบ** ไม่ใช่ authority ให้เขียน solution ใด solution หนึ่ง — แต่ผลลัพธ์ถูกเทียบกับ solution ที่มัน "เลือก" เขียนเอง โดยไม่มี checkpoint.

Coincidence ที่ทำให้ story นี้ยิ่งดัง คือมันตกลงมาในช่วงที่ OpenAI ก็เพิ่งยอมรับเคส Medicare Australia ไม่กี่วันก่อน — pattern เดียวกัน: agent ตัดสินใจ scope-of-action ต่างจากที่ user คาดหวัง แล้วเดินไปถึงระบบที่ไม่ควรแตะ. รอบสัปดาห์นี้เลยกลายเป็นจุดที่คำถาม "how do you contain agent blast radius" ถูกยกระดับจาก panel discussion เป็น requirement เชิงเทคนิคที่ platform vendor ต้องตอบ.

สำหรับผู้ใช้ Claude Code เอง — Anthropic ต้อง balance ความเก่งกับ safety. Product ตัวนี้แหล่งรายได้กำลังโตเร็ว (Anthropic รายงานว่า Claude Code ทะลุ $500M ARR ในกลางปี) แต่ incident แบบนี้ทำให้ enterprise buyer ที่กำลัง sign contract ระดับ 8-figure ถามคำถามใหม่: "Show me your recovery playbook when agent breaks something big." คำตอบ "we ask user to grant permission" ไม่พอ.

## มุม AI Agent Platform
**Builders** ที่ทำ coding agent — เรื่องนี้เป็น mandatory retro. ต้อง (1) sandboxing ที่จริงจัง ไม่ใช่แค่ approve/deny prompt, (2) preview mode ที่ให้ agent "ทำแล้วบอก diff" ก่อนคอมมิต — pattern ที่ Cursor Agent เริ่มทำ พร้อม `--dry-run` flag ที่ agent เข้าใจ, (3) blast radius limiter ที่ตัดเมื่อจำนวนไฟล์ที่จะเปลี่ยนต่อ command เกิน threshold. **Users / business** ที่ให้ agent เข้าถึง production repo — จนกว่าตัวเลขเหล่านี้จะเป็น default ในผลิตภัณฑ์ ให้ทำ 3 อย่าง: (1) run agent ใน git worktree ที่แยก, (2) เปิด backup snapshot ทุก 15 นาที ระหว่าง agent session, (3) ให้ agent มี write access เฉพาะ scope-directory ไม่ใช่ entire repo. **Ecosystem** — Warp, Cursor, Windsurf, Devin, Copilot ต่างมี kill-switch pattern ที่ต่างกัน. คนที่ solve Windows junction + macOS resource fork + Linux bind mount edge case แบบสมบูรณ์แล้ว expose เป็น standard sandboxing layer จะมี moat จริง — เพราะ safety ใน agentic coding เป็น cost ที่ทุก customer จ่ายอยู่แล้ว แค่ยังไม่มี vendor ที่ productize ให้ได้.

## Sources
- [Claude Code Agent Allegedly Deletes 48,000 Files in 103 Seconds — Cybersecurity News](https://cybersecuritynews.com/claude-code-agent-file-deletion/)
- ['I broke something': A Claude Code AI agent deleted 48,000 files — TechRadar](https://www.techradar.com/pro/security/i-broke-something-a-claude-code-ai-agent-deleted-48-000-files-in-just-over-100-seconds-then-apologized-for-doing-so)
- [A Claude Code Rampage Allegedly Wiped Out 48,000 Project Files — Android Headlines](https://www.androidheadlines.com/2026/09/claude-code-ai-agent-deletes-48000-files-in-103-seconds.html)
- [Claude Code File Deletion: 48,000 Files, Essential Warning — Progressive Robot](https://www.progressiverobot.com/2026/09/26/claude-code-file-deletion-48000-files-103-seconds/)

---

## Audio script
ข่าวสะเทือนวงการ coding agent วันนี้ครับ. คืนวันที่ 25 กันยายนตามเวลาอเมริกา Claude Code ของ Anthropic ลบไฟล์ในโปรเจ็คต์ของ developer คนหนึ่งไป 48,218 ไฟล์ในเวลา 103 วินาที พร้อมยับ Git history ด้วย. เรื่องคือ developer สั่งให้ agent rebuild mirror ของโปรเจ็คต์ agent เจอว่า script เดิมไม่ทำงาน เลยเขียน Python script ใหม่เพื่อลบ mirror เก่าก่อน — แต่ agent ใช้ os.walk แบบไม่ follow symlink ซึ่งบน Windows ไม่ครอบคลุม directory junction. Mirror เก่ามี junction 614 อันชี้กลับไปโปรเจ็คต์จริง agent ก็เลยเดินทะลุลบทั้งหมด แล้วมาบอกทีหลังว่า I broke something. เรื่องนี้ต่างจาก AI clickbait ตรงที่ root cause จับต้องได้ เป็น engineering bug ธรรมดา แค่ agent ได้ authority ให้ทำงานให้จบ ไม่ใช่ authority ให้เขียน implementation ไหนก็ได้. ในเมื่อ OpenAI ก็มีเคส Medicare ที่ agent ไป touch ระบบรัฐเมื่อสัปดาห์ก่อน pattern ชัดว่าคำถาม how do you contain agent blast radius เลิกเป็น panel discussion แล้ว. ถ้าคุณกำลังให้ agent เข้าถึง production repo ให้รัน agent ใน git worktree แยก เปิด snapshot ทุก 15 นาที และ scope write access เฉพาะ folder ที่จำเป็น. Vendor ที่ solve sandboxing edge case แบบสมบูรณ์ก่อน จะมี moat จริงในตลาดนี้ครับ.
