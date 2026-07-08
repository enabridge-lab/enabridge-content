---
date: 2026-07-09
slug: 26-07-09-0608-02-openai-gpt56-ultra-mode-subagents-runtime
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A cinematic tech-editorial illustration: a central glowing orb labeled "SOL"
  splits into rays that reach smaller labeled orbs "TERRA" and "LUNA"; from Sol
  descend three cascading translucent copies labeled "SUB-AGENT 1",
  "SUB-AGENT 2", "SUB-AGENT 3" arranged like a fanned staircase; a big number
  plate on the right reads "91.9%" with subtitle "TERMINAL-BENCH 2.1"; small
  chips underneath show "$2.50/M IN", "$15/M OUT" for Terra. Editorial dark
  neon style, 1:1 aspect, high contrast for 200px thumbnail, no real human faces.
image: images/26-07-09-0608-02-openai-gpt56-ultra-mode-subagents-runtime.png
---

# OpenAI GPT-5.6 Ultra Mode ยก sub-agent จาก app layer → **runtime layer** — และเปลี่ยน economics ของ agentic default

## TL;DR
- OpenAI preview **GPT-5.6 Sol / Terra / Luna** (26 มิ.ย.); ประกาศ **Sol บน Cerebras 750 tok/s** และ preview partner 20 องค์กร (7 ก.ค.) — Sol Ultra ทำ **91.9% Terminal-Bench 2.1** ด้วยการ **spawn sub-agent เอง** ไม่ใช่ scale compute เฉย ๆ
- **Terra** ($2.50 in / $15 out per M tokens) วางตำแหน่งเป็น "agentic everyday", **Luna** ($1 in / $6 out) เป็น router/fast tier — matrix pricing บอกชัดว่า OpenAI ตั้งใจให้ agent runtime แตกงานลง Luna, escalate เฉพาะ hard reasoning ไป Sol
- **Sub-agent orchestration ย้ายจาก application layer** (LangGraph, CrewAI, สำหรับ dev พันด้วยมือ) **ลงมา runtime layer** ที่ OpenAI จัดการเอง — Terminal-Bench 2.1 91.9% ไม่ใช่แค่คะแนน, มันคือ**คำประกาศว่า framework ที่แข่ง sub-agent orchestration ต้องพิสูจน์ตัวเองใหม่**

## เกิดอะไรขึ้น

OpenAI ตัดสินใจ split GPT-5.6 เป็น **3 model 3 tier** เหมือน Google Gemini + Anthropic (Opus/Sonnet/Haiku) — **Sol** (frontier reasoning + long-horizon agent), **Terra** ($2.50 in / $15 out ต่อ M token, ~GPT-5.5-level ที่ครึ่งราคา), **Luna** ($1 in / $6 out, small + fast). Preview เปิด 26 มิ.ย. 2026 ให้กลุ่ม preview partner ~20 องค์กร หลังจากส่ง release plan ให้รัฐบาลสหรัฐฯ ล่วงหน้าตาม voluntary AI safety framework

สิ่งที่เด่นสุดไม่ใช่โมเดล แต่คือ **Ultra Mode** — โหมดใหม่ที่ **spawn sub-agent** จาก parent เอง, run ขนานกัน, sync กลับ, แล้วให้ parent สรุป. Sol Ultra reach **91.9% บน Terminal-Bench 2.1** (ก้าวจาก Sonnet 5 ที่ ~85% และ Opus 4.8 ที่ ~87%). ที่สำคัญคือ **METR เตือน** ในรายงานคู่กันว่า Ultra mode ยกระดับ agentic risk เพราะ parent สามารถ delegate task ที่ safety filter คน ๆ เดียวจับไม่ได้ — OpenAI ตอบด้วยการเปิด preview จำกัด 20 องค์กร และรายงานให้ US AISI ตรวจก่อน general release

7 ก.ค. Cerebras ประกาศคู่กันว่า **GPT-5.6 Sol จะรันบน Wafer-Scale Engine** ที่ **สูงสุด 750 token/วินาที** เมื่อ available. Sonnet 5 ตอนนี้อยู่ประมาณ 130-160 tok/s ผ่าน Anthropic direct; Groq/Sambanova ทำ Llama/Qwen ได้ ~500-800 tok/s. สิ่งนี้เปลี่ยน economics ของ agentic loop: ถ้า Sol run ที่ 750 tok/s พร้อม Ultra mode, sub-agent 5 ตัวรัน parallel = throughput เทียบเท่า agent 5 คนตอบสอบพร้อมกัน — และ Cerebras billing แบบ per-token ยัง scale ได้

Pricing matrix บอกอะไร: Terra $2.50/$15 = agent tier ที่ตั้งใจให้เป็น default runtime. Luna $1/$6 = router/fast tier สำหรับ tool call, formatting, RAG retrieval. Sol $5/$30 = reasoning + long-horizon ที่ Ultra Mode spawn sub-agent จาก Sol เอง (แต่ sub-agent ตัวลูกจะ default ไป Terra หรือ Luna ตามที่ parent เลือก). โครงสร้าง 3 tier ที่คุยกันได้ในรัน**เดียว** = **agent runtime แบบ multi-model native ที่ dev ไม่ต้อง orchestrate เอง**

## ทำไมสำคัญ

**Sub-agent orchestration ย้ายชั้น**: จากที่ dev ต้องใช้ LangGraph / CrewAI / AutoGen / OpenAI Agents SDK ในการ define graph สนามรบสัปดาห์ที่แล้ว = Anthropic Sub-Agent + Sonnet 5, สัปดาห์นี้ = OpenAI Sol Ultra Mode. **runtime layer คือชั้นใหม่ที่ frontier lab แข่ง** — ที่ผ่านมา orchestration แข่งกันที่ SDK/framework layer, แต่ตอนนี้ frontier lab บอกว่า "**ให้เรา spawn sub-agent ให้เอง คุณเรียก endpoint เดียว**"

Pattern ที่เห็นในรอบ 30 วัน — **Anthropic Claude Sub-Agent (มิ.ย.)**, **OpenAI Ultra Mode sub-agent (26 มิ.ย.)**, **Google Gemini Enterprise Agent Platform ที่มี A2A native** — คือ frontier lab **eat orchestration middleware** ทั้ง 3 เจ้า. **LangChain valuation** ก่อน funding รอบล่าสุด $1.25B — คำถามคือ moat orchestration middleware อยู่ตรงไหนถ้า runtime layer ทำเองได้ 91.9% แล้ว? คำตอบน่าจะเหลือแค่ **multi-vendor abstraction** (agent ที่ต้องข้าม Anthropic + OpenAI + Google) + **enterprise governance layer** — ทั้งสองอย่างเป็น **niche ไม่ใช่ mass market แล้ว**

Signal ราคา — Terra $2.50/$15 vs Sonnet 5 $3/$15 (default price) = OpenAI ยอมกิน margin เพื่อชนะ tier กลาง. Luna $1/$6 vs Haiku 4.5 $1/$5 = ใกล้เคียง แต่ Luna น่าจะ trade quality สูงกว่า Haiku ในบาง benchmark. **agent developer จะย้ายไป OpenAI ในไตรมาสข้างหน้าถ้า Ultra mode reliability ตามที่ preview บอก** — เพราะประหยัด engineering effort ของ orchestration งาน 3-6 เดือน = ROI ชัดกว่า loyalty ต่อ vendor

## มุม AI Agent Platform

**Builders** — ถ้าคุณ build orchestration framework (LangChain, Windmill, CrewAI, AutoGen), moat ต้องย้ายเร็ว: (1) **multi-vendor routing** ที่ frontier lab ทำเองไม่ได้, (2) **governance/observability** (Langfuse, Helicone, Braintrust) ที่ runtime layer ไม่แตะ, (3) **domain-specific** sub-agent library (legal, medical, finance) ที่ general Ultra mode ยังตอบไม่แม่น. ถ้า pitch ยัง "we abstract sub-agent orchestration" — deck นั้น outdated ภายใน 90 วัน

**Users/business** ที่ pilot agent ในไทย — **CIO/CTO ต้องประเมิน Ultra Mode ในไตรมาสหน้าทันที**. ถ้า workflow ที่คุณ deploy ใช้ LangGraph + Claude 4.5 + sub-agent 3-5 ตัวที่ tune มา 6 เดือน, บาง workflow อาจ replace ด้วย Sol Ultra endpoint เดียวได้ที่ราคาต่ำกว่า และ latency ต่ำกว่า (โดยเฉพาะบน Cerebras). **ทดสอบก่อน sign contract 1-year** ที่กำลังจะต่อ. **Ecosystem**: hyperscaler ที่ host frontier model (Azure AI Foundry สำหรับ OpenAI, Bedrock สำหรับ Anthropic, Vertex สำหรับ Google) จะแข่งกัน expose Ultra Mode / Sub-Agent API แบบ region-aware + private VPC ก่อน Q4 — ระวัง lock-in ผ่าน **agent tier ที่ portable ยาก**

## Sources
- [Previewing GPT-5.6 Sol: a next-generation model (OpenAI)](https://openai.com/index/previewing-gpt-5-6-sol/)
- [GPT-5.6 Release Nears: Ultra Mode Spawns Subagents, Terra Cuts Cost, METR Flags Risk (TechTimes)](https://www.techtimes.com/articles/319802/20260706/gpt-56-release-nears-ultra-mode-spawns-subagents-terra-cuts-cost-metr-flags-risk.htm)
- [OpenAI unveils GPT-5.6 Sol, Terra and Luna models — but only accessible to limited preview partners for now (VentureBeat)](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now)

---

## Audio script
เพื่อน ๆ ครับ ข่าวที่สองเช้านี้ต้องพูดถึง OpenAI ที่เปิดตัว GPT-5.6 เป็นสามรุ่น — Sol เป็น flagship, Terra เป็นตัวกลางราคาครึ่งเดียว, และ Luna เป็นตัวเล็กเร็วราคาถูก. สิ่งที่น่าสนใจไม่ใช่ตัวโมเดลอย่างเดียวนะครับ แต่คือฟีเจอร์ใหม่ที่ชื่อ Ultra Mode ที่ Sol สามารถ spawn sub-agent ออกมาเองในระหว่างรัน — parent สั่งงาน sub-agent ตัวลูกทำเสร็จส่งคืน parent สรุป Terminal-Bench 2.1 ที่เป็น benchmark วัด agentic ability ยากที่สุด Sol Ultra ทำได้ 91.9% ก้าวจาก Sonnet 5 ที่ประมาณ 85% วันที่ 7 กรกฎา Cerebras ประกาศเพิ่มว่า Sol จะรันบน wafer-scale engine ที่เร็วสุด 750 token ต่อวินาที ประเด็นสำคัญที่ builders ต้องคิดคือ orchestration ของ sub-agent ที่เคยเป็นชั้น application ทำด้วย LangGraph CrewAI AutoGen ตอนนี้ frontier lab กำลัง eat ชั้นนี้ลงไปเป็น runtime — คุณเรียก endpoint เดียว Ultra จัดการ sub-agent ให้เอง. framework ที่ pitch ตัวเองว่าช่วย orchestrate sub-agent อย่างเดียวจะกลายเป็น commodity ใน 90 วัน moat ต้องย้ายไปที่ multi-vendor routing observability governance หรือ domain-specific sub-agent library. สำหรับคนที่ deploy agent ในไทยตอนนี้ ถ้าคุณเซ็นสัญญา 1 ปีกับ vendor orchestration ที่ tune มา 6 เดือน ทดสอบ Sol Ultra ก่อนต่อสัญญาครั้งหน้านะครับ อาจประหยัดได้เยอะและตอบง่ายกว่า
