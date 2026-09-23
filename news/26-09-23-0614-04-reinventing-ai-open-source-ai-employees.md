---
date: 2026-09-19
slug: reinventing-ai-open-source-ai-employees
topic: agentic-ai
sources: 3
reading_time_min: 4
image_prompt: |
  A cozy editorial isometric render of a tidy home office at dawn where
  eight glowing translucent robot silhouettes sit at eight desks, each
  labeled with a job placard: "GTM ENGINEER", "SEO/AEO", "WEB DEV",
  "SOCIAL MEDIA", "AD MANAGER", "SALES", "CUSTOMER SATISFACTION", "CHIEF
  OF STAFF". Above them a neon marquee reads "8 OPEN SOURCE AI EMPLOYEES
  — MIT LICENSE — 59 ROUTINES". A big glowing shield tile reads "RUNS ON
  YOUR MACHINE"; a smaller strip reads "11 HARNESSES: CLAUDE CODE •
  OPENCLAW • HERMES • CODEX • ANTIGRAVITY..." A GitHub-cat mascot smiles
  in the corner. Warm SME-founder palette (amber + teal), editorial
  isometric style, 1:1 aspect, big contrasty labels for 200px thumbnail,
  no real human faces.
image: images/26-09-23-0614-04-reinventing-ai-open-source-ai-employees.png
---

# Reinventing.AI ปล่อย 8 open-source AI Employees บน MIT — รันบนเครื่องตัวเองผ่าน 11 agent harness; 59 scheduled routines สำหรับ SMB

## TL;DR
- 19 ก.ย. — Reinventing.AI เปิด repo `github.com/markfulton/ai-employees` บน **MIT license** พร้อม **8 scheduled business roles + 59 routines** — role รวม GTM Engineer, SEO/AEO, Web Dev, Social Media, Ad Manager, Sales, Customer Satisfaction, **Chief of Staff**
- **แต่ละ AI Employee = folder ของ plain files** (role description, operating contract, schedule, routine scripts) ที่ agent harness รัน **บนเครื่องเจ้าของเอง** — ไม่มี SaaS, ไม่มี subscription, ไม่มี "sign up และให้เราถือ data". เจ้าของ **own the files**, own outputs, own credentials
- Compatible กับ **11 agent harness**: **Claude Code, OpenClaw, Hermes, OpenCode, Grok Bot, Codex, Antigravity, Muse, Pi, Cline, Qwen Code, DeepSeek** บน Windows / macOS / Linux. Security guarantee: ไม่มี routine ไหนสร้าง account, กรอก password, ผ่าน captcha, หรือเขียน credential ลงไฟล์

## เกิดอะไรขึ้น

19 ก.ย. Reinventing.AI (บริษัทที่ CEO Mark Fulton ก่อน exit จาก **Bombora** ปี 2024) ปล่อย open-source repository ที่ประกอบด้วย 8 "AI Employee" package. Framing ทางการ: "employees that live on your machine, not on someone else's server". Repo public บน GitHub, MIT license, **commercial use รวมอยู่แล้ว**, no membership required

**8 roles ที่ ship พร้อมกัน:**
1. **GTM Engineer** — automate go-to-market experiment, list enrichment, outreach sequence
2. **SEO/AEO Employee** — SEO เดิม + AEO (Answer Engine Optimization = optimize for LLM answer)
3. **Web Dev Employee** — landing page, A/B test, deploy pipeline
4. **Social Media Employee** — content calendar, cross-post, engagement monitor
5. **Ad Manager Employee** — budget allocation, creative rotation, performance report
6. **Sales Employee** — pipeline nurture, meeting prep, follow-up
7. **Customer Satisfaction Employee** — ticket triage, sentiment monitor, escalation
8. **Chief of Staff** — cross-role coordination, weekly summary, exec brief

**Architecture ที่ต่าง (และเป็น pattern ใหม่):** แต่ละ AI Employee = **folder ของ plain files** ไม่ใช่ container image / SaaS deploy — ประกอบด้วย (1) **role description** (Markdown), (2) **operating contract** (สิ่งที่ทำได้/ไม่ทำได้ + escalation rule), (3) **schedule** (cron-style, "daily 9am send email digest"), (4) **routines** (scripts). Agent harness (Claude Code, Codex, Cline อื่น ๆ) load folder เข้า, execute routine ตาม schedule, output ไปที่ที่ owner กำหนด. **Owner เป็นคน own ทุกอย่าง** — files, output, credential

**Security model ที่โปรโมท:** ทุก sending, publishing, spending action **เกิดขึ้นบน channel ที่ owner release ให้ under conditions**, หรือใน session ของ owner, หรือผ่าน permission layer ของ harness. **Zero credential storage** — ไม่มี routine ไหนสร้าง account, กรอก password, ผ่าน captcha, หรือเขียน credential ลงไฟล์. ทุก API key คนใช้ inject ผ่าน harness's own secrets manager. Security posture นี้ตอบ objection หลักของ SMB owner (compliance + credential leakage) — เพราะไม่มี server ปลายทางที่จะโดน breach

**11 agent harness ที่ compatible:** Claude Code (Anthropic), Codex (OpenAI), Grok Bot (xAI), Cline (VS Code extension), Qwen Code (Alibaba), DeepSeek (open weight), OpenClaw, Hermes, OpenCode, Antigravity (Google), Muse (Meta), Pi. รายการนี้เยอะเพราะ Reinventing.AI ตั้งใจไม่ผูกกับ vendor เดียว — เจ้าของเลือก harness ตาม preference / cost / performance ของแต่ละ workload

## ทำไมสำคัญ

Move นี้เป็นครั้งแรกที่ **"AI Employee" ทั้ง package ถูก package แบบ open source + on-device** ที่ SMB สามารถ deploy ได้จริงในเสียงเดียว (git clone → schedule รัน → done). Framework เดิม (n8n workflows, Zapier agents, Make.com scenarios) ยัง require SaaS backend; **open source AI agent framework** เดิม (LangGraph, CrewAI) ยัง require developer ประกอบเอง. Reinventing.AI package สอง trend เข้าด้วยกัน = **turn-key + open + on-device**

**Pattern ที่กำลังยึด "self-hosted agent movement":** ตามหลัง Ollama (self-host LLM), Continue.dev (self-host coding agent), LibreChat (self-host ChatGPT clone). Movement นี้ growth เพราะ 3 ปัจจัย: (1) **API cost ลด 40-50% ในวันเดียว** (Opus 5.5 + GPT-6 Sol เมื่อวาน) = self-host economics แข่งได้; (2) **data privacy** — SMB owner ไม่อยากส่ง customer data ไป third-party; (3) **AI-native workflow** — routine ที่คนเขียนขึ้นเองไม่ต้องรอ vendor feature roadmap. ตลาด SMB (US มี ~33M, TH มี ~3M) เป็น long tail ที่ Salesforce Agentforce ($540M ARR, 18,500 enterprise customer) แทรกไม่ได้เพราะ pricing สูงเกิน

**Chief of Staff role น่าสนใจสุด** — เป็น **meta-agent** ที่ coordinate 7 role อื่น, produce weekly exec brief. เป็น pattern ที่ enterprise agent framework (LangGraph supervisor, CrewAI hierarchical) ทำได้แล้ว แต่ที่ user level ยังไม่มี package ที่ deploy ได้เลย. **ถ้า Chief of Staff pattern ได้ผล, SMB owner คนเดียวจริง ๆ อาจ manage ธุรกิจได้ที่ scale เดิมของทีม 5-10 คน** — mid-market disruption

จุดต้องจับตา: **quality ของ routine ที่ ship เริ่มต้น**. Repo ปล่อยใหม่, community contribution ยังไม่ได้ทดสอบยาว, ทีมที่ deploy ต้อง audit routine เอง. ถ้า Q4 มี real testimonial จาก SMB ที่วัด time saved / revenue lift ได้จริง, adoption จะเร่งขึ้น. Watch: fork count, star count, PR count ใน 90 วันข้างหน้า

## มุม AI Agent Platform

สำหรับ **builders** — repo นี้เป็น **reference implementation** สำหรับใครที่ทำ agent framework: **role/contract/schedule/routine เป็น pattern ที่ portable ข้าม harness** (11 ตัว ณ ตอนนี้). Startup ที่ทำ agent framework ไทยควรออกแบบให้ **compatible กับ pattern นี้** — vendor lock-in ตายอีก 12 เดือน, portability = distribution. ถ้าทำ Vertical AI Employee (เช่น "Thai HR Compliance Employee", "SET Filing Employee") ก็ **package แบบเดียวกัน** distribute บน GitHub = ตัดคน middleman

สำหรับ **users / business** — **SMB owner ควรลอง clone repo แล้ว deploy 1 role ทดสอบ**. Sales หรือ Social Media เริ่มง่ายสุด. ทดสอบ 2 สัปดาห์แล้ววัด: hours saved, output quality, credential safety. ถ้าได้ผล scale ไป 3-4 role. **Enterprise IT** ไม่ควร ignore trend นี้ — employee ในบริษัทอาจ deploy AI Employee บนเครื่องตัวเอง = shadow AI Employee ที่ IT ไม่รู้. เขียน policy ให้ชัดเจนก่อน Q1 2027

สำหรับ **ecosystem** — **Anthropic (Claude Code), OpenAI (Codex), Google (Antigravity)** = winner ทางอ้อม เพราะ harness ของพวกเขาถูก list เป็น compatible; **Google Antigravity ที่ Wikipedia เพิ่งเปิด article** ก็ได้ visibility เพิ่มขึ้น. **n8n, Zapier, Make** = feel pressure — pattern "open + on-device + on your files" อ่อนแอโมเดล SaaS workflow ของพวกเขา. **Salesforce Agentforce, ServiceNow Now Assist** = ยังไม่กระทบเพราะ target enterprise, แต่ movement นี้จะกลืน low-end enterprise ใน 24-36 เดือน. **Cursor + Windsurf + Devin** = ไม่กระทบ (target developer, ไม่ใช่ business role)

## Sources
- [Reinventing.AI Releases Eight Open Source AI Employees on GitHub Under MIT License — EIN Presswire](https://www.einnews.com/pr_news/941970685/reinventing-ai-releases-eight-open-source-ai-employees-on-github-under-mit-license)
- [ai-employees repository — GitHub (markfulton/ai-employees)](https://github.com/markfulton/ai-employees)
- [Reinventing.AI Releases Eight Open Source AI Employees on GitHub Under MIT License — Middletown Life](https://lifestyle.middletownlifemagazine.com/story/697437/reinventing-ai-releases-eight-open-source-ai-employees-on-github-under-mit-license/)

---

## Audio script
เมื่อ 19 กันยา บริษัท Reinventing.AI ปล่อย 8 AI Employee packages แบบ open source บน GitHub ภายใต้ MIT license — commercial use ฟรี. 8 roles ประกอบด้วย GTM Engineer, SEO/AEO, Web Dev, Social Media, Ad Manager, Sales, Customer Satisfaction, และ Chief of Staff — total 59 scheduled routines. Architecture ที่ต่างคือแต่ละ AI Employee เป็น folder ของ plain files — role description, operating contract, schedule, routine scripts — ไม่ใช่ container image หรือ SaaS deploy. เจ้าของ own ทั้ง files, output, และ credential. Compatible กับ 11 agent harness — Claude Code, Codex, Grok Bot, Cline, DeepSeek, Antigravity, Muse, Pi และอื่น ๆ. Security model — ไม่มี routine ไหนสร้าง account, กรอก password, ผ่าน captcha, หรือเขียน credential ลง file. Signal สำคัญ — เป็นครั้งแรกที่ AI Employee ทั้ง package ถูก package แบบ open source + on-device ที่ SMB deploy ได้จริงในเสียงเดียว. Pattern นี้ตามหลัง Ollama, Continue.dev, LibreChat = "self-hosted agent movement" ที่ growth เพราะ API cost ลด 40-50% เมื่อวาน + data privacy + AI-native workflow. Role ที่น่าสนใจสุดคือ Chief of Staff เพราะเป็น meta-agent ที่ coordinate 7 role อื่น produce weekly exec brief — ถ้า pattern นี้ได้ผล, SMB owner คนเดียวอาจ manage ธุรกิจได้ที่ scale เดิมของทีม 5-10 คน. สำหรับ builder ไทยที่ทำ agent framework ควรออกแบบให้ compatible กับ pattern folder + role + schedule + routine นี้ — vendor lock-in ตายอีก 12 เดือน, portability = distribution. สำหรับ SMB owner ไทยลอง clone repo deploy 1 role ก่อน วัด hours saved 2 สัปดาห์ ถ้าได้ผลค่อย scale.
