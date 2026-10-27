---
date: 2026-10-28
slug: vercel-drives-ga-ship-2026
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a black Vercel-triangle data vault floating
  above a sandbox stage. From the vault, three glowing drives slide into three
  separate sandbox pods containing tiny agent silhouettes at work — each pod labeled
  with a mounted drive icon that remains lit even after the pod closes. Big display
  numbers hang in the sky: "1 TiB DEFAULT", "16 TiB MAX", "FORKABLE". A ribbon
  across the top reads "DRIVES — GA" and another at the base reads
  "SHIP 2026". Monochrome black-and-white with electric cyan highlights, strong
  contrast for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-28-0605-02-vercel-drives-ga-ship-2026.png
---

# Vercel Drives GA — persistent storage ของ agent sandbox เริ่มเป็น primitive มาตรฐาน

## TL;DR
- **15 ต.ค.** ที่ Ship 2026 San Francisco, Vercel ประกาศ **Drives GA** — persistent storage layer ที่ mount เข้า Vercel Sandbox แล้วอยู่หลัง sandbox stop; default **1 TiB** บนทุก plan (Hobby 1 GiB), scale ถึง **16 TiB**
- **Forking also GA:** fork drive คัดลอก state ตอนนั้น ใช้ run experiment parallel ได้ แต่ไม่ merge กลับ parent — pattern ใหม่สำหรับ **"agent branching"** แทน workspace cloning
- **Vercel Daemons เข้า public beta** — continuously-running background worker (ก่อนหน้าเป็น ephemeral function); **Enterprise-Managed Authorization** ผ่าน Vercel Connect public beta ด้วย
- **Context:** Vercel ประกาศว่า **Meta Superintelligence Labs** รัน Vercel; enterprise token use บน AI Gateway **โต 4× ใน 3 เดือน**
- Signal: agent primitive layer กำลัง bifurcate — Anthropic ลง sandbox-runtime (OS-level, ไม่มี container), Vercel ลง managed persistent sandbox + daemon + gateway — คนละ abstraction แต่ rhyme กัน

## เกิดอะไรขึ้น

วันพุธที่ **15 ต.ค.** ที่ Ship 2026 ณ San Francisco, Vercel ประกาศ **Drives เข้า GA** พร้อม **Forking GA** และ **Daemons public beta**. Drives คือ "persistent storage ที่ outlive sandbox run" — คุณ mount drive หนึ่งก้อนเข้า Vercel Sandbox, agent เขียน code, cache, model weight, document ลงไป, sandbox terminate — drive ยังอยู่, mount ใหม่เมื่อไหร่ก็เริ่มทำงานต่อได้. ก่อนหน้านี้ Sandbox ของ Vercel เป็น ephemeral: agent run แล้ว state หายทันที, pattern ที่คน CrewAI/LangGraph complaint ว่าทำ long-running workflow ไม่ได้

ตัวเลข spec: default **1 TiB** ต่อ drive สำหรับทุก paid plan (Hobby ได้ 1 GiB), expandable ถึง **16 TiB**. Fork คัดลอก state ปัจจุบันของ drive เป็น child drive — ใช้ run parallel experiment ได้แต่ **ไม่ merge back**. Pattern เทียบกับ git branch แต่ไม่มี merge — เหมาะกับ "agent explores multiple paths แล้วเก็บแค่ที่ดีที่สุด" workflow ที่ **Cognition Devin, OpenAI Codex, Replit Agent** ทำกันอยู่แล้วแต่ต้อง roll ของตัวเอง

**Vercel Daemons** ที่เข้า public beta เป็น shift สำคัญกว่า storage: จาก serverless function ที่ "boot-run-die" ไปเป็น **long-running background worker** ที่ listen event + รัน loop ของตัวเอง. Pattern ที่ Vercel เคย relentlessly ปฏิเสธ (CTO Guillermo Rauch เคยยืนยันว่า Vercel ไม่ทำ long-running compute). ตอนนี้ภาษา marketing เปลี่ยนเป็น "continuously running background workers" — ยอมรับว่า agent workflow ต้องการ compute pattern ที่ serverless ตอบไม่ครบ

**Enterprise-Managed Authorization via Vercel Connect** ที่เข้า beta คือ enterprise ที่เอา Vercel ไป self-host หลัง corporate IdP (Okta, Entra, Ping) จะได้ fine-grained access control ต่อ sandbox + drive + daemon — layer ที่ enterprise ปัจจุบันต้อง workaround ผ่าน VPN + bespoke proxy. Vercel ประกาศคู่ไปด้วยว่า **Meta Superintelligence Labs ใช้ Vercel** — รีเฟอเรนซ์ชื่อใหญ่ที่สุดที่ Vercel ให้ public, และ enterprise AI Gateway token use **โต 4× ใน 3 เดือน**

## ทำไมสำคัญ

ประเด็นที่หนึ่ง — **agent primitive stack กำลัง layer จริง**. ย้อนไป 6 เดือน Vercel = frontend host + serverless function. ตอนนี้ Vercel = **frontend + sandbox + persistent storage + daemon + model gateway + auth** — เกือบครบ stack สำหรับ build agent production. ที่สำคัญคือ **Drives คือ primitive มาตรฐาน** ที่ developer ไม่ต้องสร้างเอง — ชั้นนี้ก่อนหน้าทำผ่าน S3 + Lambda + EFS หรือ Modal + Replicate — ตอนนี้ Vercel bundle ให้ ลด time-to-production ของ agent app จากเดือนเป็นสัปดาห์

ประเด็นที่สอง — **"agent branching" via drive fork คือ pattern ใหม่ที่ยังไม่เป็น vocabulary มาตรฐาน**. ถ้า Devin + Codex + Replit ต้อง roll ของตัวเอง, Vercel bundling ชั้นนี้ลง primitive เท่ากับ **commoditize pattern**. framework (LangGraph, CrewAI) ที่จะ relevant ต่อไปต้อง treat "fork + measure + merge หรือ discard" เป็น first-class citizen — ไม่ใช่ท่าพิเศษ. โอกาส: eval framework ที่วัด quality ของ fork แต่ละสาย — ตลาดนี้ยังไม่มี leader

ประเด็นที่สาม — **Vercel vs Anthropic sandbox-runtime pattern แตกต่างทาง topology**. Anthropic (ข่าว 25 ต.ค.) ลง **OS-level sandbox** (Seatbelt + bubblewrap) ไม่ต้องมี container, agent รันบน developer machine; Vercel ลง **managed sandbox + persistent drive** cloud-side. สองโมเดลตอบคนละ workload: Anthropic เหมาะกับ **local-first agent + MCP server** ที่ไม่ต้องแชร์ state; Vercel เหมาะกับ **long-running + multi-user + enterprise audit**. การเลือก stack จะเริ่ม commit workload shape จริง — ไม่ใช่ "framework แบบไหนก็ได้" อีกต่อไป

## มุม AI Agent Platform

สำหรับ **Builders**: ถ้า agent product ใช้ Vercel อยู่แล้ว, migrate workload ที่ long-running (research assistant, code reviewer, scraping agent) จาก serverless function ไป Daemon + Drive คือ no-brainer — ลด cost cold-start + ไม่ต้อง rehydrate state. Pattern สำคัญ: **drive fork แทน workspace clone** สำหรับ parallel experiment, เก็บแค่ chosen path + delete fork อื่น ลด storage bill. framework ที่เน้น "deterministic replay" (LangGraph) ควร integrate drive-fork concept ก่อน framework อื่น claim

สำหรับ **Users / Business**: enterprise ที่ pilot agent บน Vercel มาแล้ว 2026 Q2-Q3 ตอนนี้มี path ชัดเจน — **enterprise managed auth + drive + daemon** เป็น stack ครบที่ให้ IT เซ็น approval ได้. ที่เคยค้างคือ "ไม่มี persistent state + ไม่มี long-running + auth แค่ project level" — ชั้นเหล่านี้ปิดลงใน 1 release. สำหรับ CTO ที่กำลังเลือก deploy agent production platform, Vercel ขยับจาก "frontend of agent product" ไป "end-to-end agent platform" — competitor กลับกลายเป็น Modal + Replicate + Val Town ไม่ใช่ Netlify + Cloudflare Pages

สำหรับ **Ecosystem**: Vercel ประกาศ Meta Superintelligence Labs เป็น reference ไม่ใช่เรื่องเล็ก — บอกว่า frontier lab ที่ scale ที่สุดในโลกยัง rely บน managed platform แทน rolled-own. สำหรับคนทำ model layer (ร่วม Hugging Face, Modal, Fal, Replicate, Together) นี้คือสัญญาณว่า **"we'll build our own agent runtime" คือ false economy สำหรับทีมเล็กกว่า 100 คน** — เก่งที่สุดในโลกยังเลือก Vercel

## Sources
- [Introducing Vercel Drives — persistent storage for agents (Vercel blog)](https://vercel.com/blog/introducing-vercel-drives-persistent-storage-for-agents)
- [Vercel Ship 2026 recap (Vercel blog)](https://vercel.com/blog/vercel-ship-2026-recap.md)
- [Meta Superintelligence Labs runs on Vercel, Vercel says (fourweekmba)](https://fourweekmba.com/ai-meta-superintelligence-labs-runs-on-vercel-vercel-says/)
- [Vercel Drives guide (Vercel docs)](https://vercel.com/kb/guide/vercel-drives)

---

## Audio script
วันพุธที่ 15 ตุลาคมที่ Ship 2026 ซานฟรานซิสโก Vercel ประกาศ Drives เข้า GA — persistent storage layer ที่ mount เข้า Vercel Sandbox แล้วอยู่หลัง sandbox stop ค่า default 1 TiB บนทุก plan ขยายได้ถึง 16 TiB. ก่อนหน้านี้ Sandbox ของ Vercel เป็น ephemeral — agent run เสร็จ state หายทันที — pattern ที่คน CrewAI กับ LangGraph complaint มานาน ว่าทำ long-running workflow ไม่ได้. Drives แก้ได้แล้ว. ที่น่าสนใจคือ Forking ก็เข้า GA — fork คัดลอก state ปัจจุบันของ drive เป็น child ใช้ run parallel experiment ได้ แต่ไม่ merge กลับ parent — เป็น pattern ใหม่สำหรับ agent branching ที่ Devin กับ Codex กับ Replit Agent roll ของตัวเองก่อนหน้านี้. Vercel Daemons ก็เข้า public beta — long-running background worker ชั้นที่ Vercel เคย relentlessly ปฏิเสธ ตอนนี้ยอมรับว่า agent workflow ต้องการ compute pattern ที่ serverless ตอบไม่ครบ. Enterprise-Managed Authorization ผ่าน Vercel Connect เข้า beta พร้อมกัน — enterprise ที่ self-host หลัง Okta หรือ Entra จะได้ fine-grained access control ต่อ sandbox drive daemon. Vercel ประกาศคู่ว่า Meta Superintelligence Labs ใช้ Vercel และ enterprise AI Gateway token use โต 4 เท่าใน 3 เดือน. ประเด็นต่อจากนี้มีสาม หนึ่ง agent primitive stack กำลัง layer จริง — 6 เดือนก่อน Vercel เป็นแค่ frontend host ตอนนี้เกือบครบ stack สำหรับ build agent production ลด time to production จากเดือนเป็นสัปดาห์. สอง agent branching ด้วย drive fork คือ pattern ใหม่ที่ยังไม่เป็น vocabulary มาตรฐาน ถ้า Vercel bundle ชั้นนี้ลง primitive เท่ากับ commoditize — eval framework ที่วัด quality ของ fork แต่ละสายคือตลาดใหม่ที่ยังไม่มี leader. สาม Vercel กับ Anthropic sandbox-runtime pattern ต่างทาง topology — Anthropic OS-level sandbox บน machine ของ developer, Vercel managed cloud sandbox — สองโมเดลตอบคนละ workload การเลือก stack เริ่ม commit workload shape จริง. สำหรับ builder migrate long-running workload จาก function ไป Daemon ลด cost cold-start + ไม่ต้อง rehydrate state สำหรับ enterprise CTO Vercel ขยับจาก frontend of agent product ไป end to end agent platform cornerstone คู่แข่งกลายเป็น Modal กับ Replicate ไม่ใช่ Netlify อีกต่อไป
