---
date: 2026-10-31
slug: deepseek-harness-mit-plugin-agent-runtime
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a modular workbench with a glowing
  core cube stamped "DSH" surrounded by snap-in blocks labeled "MODELS",
  "TOOLS", "SKILLS", "SESSIONS", "SANDBOXES", "STORAGE", "AGENT LOOP",
  "UI". Each block is a slot that any color plug can fit. On the floor
  a bright badge reads "MIT LICENSE", and a side banner lists
  "~207K GITHUB STARS" (with a small "unverified" asterisk). In the
  background, two shadowy walled gardens are labeled "CLAUDE AGENT SDK"
  and "OPENAI AGENTS API" with a bold arrow pointing from them to the
  workbench. Deep teal and crimson palette with gold highlights,
  1:1 aspect, strong contrast for 200px thumbnails, no real human faces.
image: images/26-11-03-0605-05-deepseek-harness-mit-plugin-agent-runtime.png
---

# DeepSeek Harness MIT: open-source agent runtime ที่ "ทุกอย่างคือ plugin" ท้าทาย Claude Agent SDK กับ OpenAI Agents API

## TL;DR
- DeepSeek เปิด **DSH (DeepSeek Harness) v0.1** ภายใต้ MIT เมื่อ 13 ส.ค. 2026, update ต่อเนื่องถึง v0.2.1-rc.1 คู่กับ **V4.1 Flash-1017** (open weights MIT) ที่ปล่อย 17 ต.ค.
- Design rule: **"ทุก component เป็น Plugin"** — model, tool, skill, session, sandbox, storage, agent loop, orchestration, UI ทั้งหมด swap ได้
- Build บน **Cordis meta-framework** (DeepSeek's internal plugin orchestrator); run ด้วย `npx @deepseek-ai/dsh web` → เปิด UI ที่ localhost:3080
- **Secondary report** อ้างว่า repo ทะลุ ~207K GitHub star ภายใน 2 สัปดาห์ (ยังไม่ verified จาก GitHub ตรง — ตีความระวัง). ตัว README เตือนตรง ๆ ว่ามี breaking change แน่ ไม่แนะนำ production

## เกิดอะไรขึ้น

DeepSeek บริษัท AI จีน (ที่เขย่าตลาดด้วย V3 open-weight ปลายปี 2024 แล้ว R1/V4 ตามมา) ปล่อย **DeepSeek Harness v0.1 (dsh)** ภายใต้ MIT license วันที่ 13 ส.ค. 2026 — คู่กับการขึ้นราคา V4-Pro API ในวันเดียวกัน. ตั้งแต่นั้น release ต่อเนื่อง: v0.1.5 คู่กับ V4.1 Flash-0910, v0.2.1-rc.1 คู่กับ **V4.1 Flash-1017** (open weights MIT ปล่อยวันที่ 17 ต.ค. 2026)

**Design rule ที่โดดที่สุด**: ทุก component ของ harness คือ **Plugin** ที่ swap ได้. README ของ dsh ระบุชัดว่า "practically every component can be replaced: models, tools, skills, sessions, sandboxes, storage, agent loops, orchestration and user interfaces." Harness build บน **Cordis meta-framework** — plugin orchestrator ของ DeepSeek เองที่ expose dependency injection + lifecycle hook เป็น primary interface

เปรียบเทียบ:
- **Claude Agent SDK** = framework ของ Anthropic ที่ Claude Code build บน, ตัดสินใจ opinion หลายอย่างให้คุณ (session, memory, tool call style)
- **OpenAI Agents API** (ตัว API primitive + Agents SDK TypeScript/Python) = framework แบบ hosted, OpenAI คุม runtime + sandbox + computer use
- **LangGraph / CrewAI / AutoGen** = Python frameworks ที่ opinion-heavy
- **DSH** = **ยอมเปิดทุกชั้นให้ swap** — model เป็น local Llama ก็ได้, UI เปลี่ยนได้, sandbox เปลี่ยนได้

การใช้งาน: `npx @deepseek-ai/dsh web` เปิด local web UI ที่ port 3080, หรือ clone แล้ว run `pnpm`. README เตือนตรง ๆ ว่า **"THERE WILL BE COMPATIBILITY-BREAKING CHANGES"** — session format ไม่ guarantee stability. วาง position เป็น "experiment, don't ship to prod"

ตัวเลขที่ควร skeptical: Secondary source อ้างว่า repo ขึ้น **~207,000 GitHub star ใน 2 สัปดาห์**. เราไม่ยืนยันกับ GitHub ตรง — ถ้าจริงจะเป็น traction ระดับ Ollama / LangChain early days. ถ้าปลอม ก็เป็น signal ว่า DeepSeek จ้าง farm. ควรเช็ค `github.com/deepseek-ai/dsh` ตรงก่อนอ้าง number นี้

Context ที่สำคัญ: DeepSeek ทำ **V4.1 Flash** เป็นโมเดลเล็กที่ open weights MIT, specializing ใน code + agent task. การ pair โมเดลกับ harness ภายใต้ license เดียวกัน = **ชุด stack เต็มที่ enterprise จีน + ประเทศที่ sanction USD จะเลือก** โดยไม่ต้องผ่าน API ของ OpenAI หรือ Anthropic ที่ GCC/Russia/Iran/บางส่วนของจีนเองไม่สามารถใช้ได้

## ทำไมสำคัญ

**ปี 2026 เป็นปีที่ agent runtime ตัดสิน market share** — Anthropic ครอบ Fortune 500 ผ่าน Claude Agent SDK + MCP (Cresta, Vercel, Honeycomb, Replit, Workato, Dayforce ที่เราเพิ่งเขียน), OpenAI ครอง developer ผ่าน Agents API + Codex + AgentKit (ที่เพิ่ง sunset ย้ายไป code-first). ทั้งสองเป็น **closed runtime** ที่ depend บน hosted API

DSH เสนอ **third option**: open-source runtime + open-weights model + swappable everything. เป็น thesis เดียวกับที่ Mozilla + Linux ตีชนะ IE + Windows เมื่อ 20 ปีก่อน — ใช้เวลา แต่กัดกร่อน moat ของ closed vendor ได้. สำหรับ **sovereign AI** (ประเทศไทย, UAE, ซาอุ, สิงคโปร์, อินโดนีเซียที่กำลัง build national AI stack), DSH + V4.1 Flash + Qwen3 + ThaiLLM เป็น reference stack ที่ไม่ต้องขออนุญาต US

ที่น่า skeptical: **"ทุกอย่างคือ plugin" คือ promise ที่ยากทำจริง**. CrewAI กับ AutoGen ก็เคย claim same thing, สุดท้ายต้อง opinionated เพราะ user ไม่อยากเขียน config เป็นร้อยบรรทัด. DSH ใน v0.1/0.2 ยัง pre-prod โดยนัย — README ยอมรับเอง. ถ้า Cordis orchestration layer ไม่เสถียร, DSH จะไม่สามารถ scale เกิน hobby/experiment ไปได้

Angle ที่ builder ไม่ค่อยพูด: **DSH เปิดช่องให้ Claude Code ของ Anthropic + Codex ของ OpenAI "ลอก" pattern ดี ๆ มาฟรี** โดยไม่มีค่า license. ถ้า DSH คิดวิธี resume-session ที่ดีกว่า, Claude Code + Codex จะ copy ภายใน 2 release. **Open-source agent runtime ไม่จำเป็นต้องชนะ** — แค่กดดัน closed vendor ให้ค่าย feature ด้วยกัน

## มุม AI Agent Platform

สำหรับ **builders** ที่ขาย commercial agent SDK (LangChain, CrewAI, Agency ตัวเล็ก ๆ): **DSH ตีลาน low-end ของคุณ**. ลูกค้าที่ build hobby/internal tool มี option free + MIT + maintained-by-DeepSeek. คุณต้องขยับขึ้น enterprise support, compliance badge, hosted managed runtime — ไม่งั้นสูญ seat free tier หมด

สำหรับ **users / business**: ถ้าคุณเป็นทีมเล็กที่กำลัง build internal agent ให้พนักงาน (เช่น legal firm ไทยที่ต้องประมวลสัญญา, บัญชีที่ต้องจัด invoice), **DSH + V4.1 Flash + Ollama รัน on-prem ได้ภายใน 1-2 สัปดาห์** โดยไม่มีค่า license. ข้อแลก: ต้อง DevOps resource เองเต็ม + รับ breaking change ของ v0.x pre-release. สำหรับ task non-critical + data sensitive, trade-off น่าสนใจ

สำหรับ **ecosystem**: ตีคู่กับ Qwen3-Coder + Mistral + Llama 4 open-weights, สัญญาณชัดว่า **"open-source agent stack" กำลังเป็น alternative stable** ไม่ใช่แค่ research artifact อีกต่อไป. ภายใน 12 เดือน, enterprise RFP จะเริ่มถาม "เราใช้ open-source runtime ตัวไหนได้บ้าง, exit cost จาก Anthropic/OpenAI เท่าไหร่" — ซึ่งเป็น leverage ที่ procurement ไม่เคยมี

## Sources
- [DeepSeek Harness v0.1 enters developer preview with open-source code (Cryptobriefing)](https://cryptobriefing.com/deepseek-harness-open-source-developer-preview/)
- [DeepSeek open-sources coding-agent harness before V4-Pro API price hike (Runtime Wire)](https://runtimewire.com/article/deepseek-open-sources-agent-harness-v4-pro-api-price-hike)
- [Where DeepSeek Harness Stands Right Now (dev.to deep-dive)](https://dev.to/diflowrin/deepseek-harness-plugin-first-agent-runtime-2djh)
- [DeepSeek V4.1 Flash Gets Coding Gains + Cheaper Agent Tasks (ProPakistani)](https://propakistani.pk/?p=1101294)

---

## Audio script
สัปดาห์นี้ขอปิดด้วยเรื่องของ DeepSeek บริษัท AI จีนที่เขย่าตลาดด้วย V3 กับ R1 ก่อนหน้านี้ครับ DeepSeek เปิด DeepSeek Harness หรือ dsh ภายใต้ MIT license เมื่อวันที่ 13 สิงหาคม แล้ว update ต่อเนื่องถึง v0.2.1 rc 1 คู่กับ V4.1 Flash 1017 ที่ปล่อย open weights MIT เมื่อ 17 ตุลาคม design rule ที่โดดที่สุดคือทุก component ของ harness เป็น plugin ที่ swap ได้ ทั้ง model tool skill session sandbox storage agent loop orchestration และ UI โดย build บน Cordis meta framework ของ DeepSeek เอง เปรียบเทียบกับ Claude Agent SDK ของ Anthropic ที่ตัดสินใจ opinion หลายอย่างให้คุณ และ OpenAI Agents API ที่ hosted คุม runtime ให้ ส่วน dsh ยอมเปิดทุกชั้นให้ swap ตั้งแต่ model เป็น local Llama ไปจนถึง UI ที่เปลี่ยนได้ ใช้งานผ่าน npx deepseek ai dsh web เปิด local web UI ที่ port 3080 README เตือนตรง ๆ ว่าจะมี breaking change แน่ไม่แนะนำ production ส่วนตัวเลข 207,000 GitHub star ใน 2 สัปดาห์ที่ secondary source อ้างยังไม่ verified ควรเช็ค GitHub ตรงก่อนอ้าง takeaway ที่ชอบ ปี 2026 เป็นปีที่ agent runtime ตัดสิน market share Anthropic ครอบ Fortune 500 ผ่าน Claude Agent SDK กับ MCP OpenAI ครอง developer ผ่าน Agents API ทั้งสองเป็น closed runtime dsh เสนอ third option open source runtime กับ open weights model ทุกอย่าง swappable เป็น thesis เดียวกับ Mozilla กับ Linux ที่ตีชนะ IE กับ Windows เมื่อ 20 ปีก่อน ใช้เวลาแต่กัดกร่อน moat ของ closed vendor ได้ สำหรับ sovereign AI เช่นไทย UAE ซาอุ สิงคโปร์ อินโดนีเซียที่กำลัง build national stack dsh plus V4.1 Flash plus Qwen3 plus ThaiLLM เป็น reference stack ที่ไม่ต้องขออนุญาต US angle ที่ builder ไม่ค่อยพูด dsh เปิดช่องให้ Claude Code กับ Codex ลอก pattern ดี ๆ มาฟรีโดยไม่มีค่า license ถ้า dsh คิดวิธี resume session ที่ดีกว่า Claude Code กับ Codex จะ copy ภายใน 2 release open source agent runtime ไม่จำเป็นต้องชนะ แค่กดดัน closed vendor ให้ค่าย feature ด้วยกัน
