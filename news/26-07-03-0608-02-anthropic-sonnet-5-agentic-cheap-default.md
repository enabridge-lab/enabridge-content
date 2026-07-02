---
date: 2026-06-30
slug: anthropic-sonnet-5-agentic-cheap-default
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration: a giant price tag hanging in the foreground reads
  "$2 IN · $10 OUT", casting a shadow over a mid-ground robot silhouette
  running a browser and terminal window. Behind, a leaderboard flat-screen
  shows five stacked benchmark bars — "SWE-BENCH PRO 63%", "OSWORLD 81%",
  "BROWSECOMP 85%", "TERMINAL-BENCH 80%", "GDPVAL 1618". A small Claude
  Sonnet 5 wordmark and Anthropic logo sit at lower-right. Bold overlay
  headline: "SONNET 5 — DEFAULT FOR EVERYONE". Cinematic isometric
  tech-magazine style, deep navy and neon-orange palette, ultra-sharp text
  for 200px thumbnail readability, 1:1 aspect ratio, no real human faces.
image: images/26-07-03-0608-02-anthropic-sonnet-5-agentic-cheap-default.png
---

# Anthropic ปล่อย Claude Sonnet 5 — "most agentic Sonnet ever" ราคาถูกกว่า Opus 5 เท่า, ตั้ง default ให้ทุก user

## TL;DR
- 30 มิ.ย. — Anthropic เปิดตัว **Claude Sonnet 5**, model ที่บริษัทเรียกว่า "most agentic Sonnet ever built" — 63.2% บน **SWE-bench Pro**, 84.7% บน **BrowseComp**, **80.4% บน Terminal-Bench 2.1** ที่ *แซง Opus 4.8* — และตั้งเป็น **default model** ให้ทุก Free/Pro user บน claude.ai ตั้งแต่วันแรก
- ราคา intro **$2 in / $10 out ต่อล้าน token** ถึง 31 ส.ค. (จะขึ้นเป็น $3/$15 ก.ย.) — ถูกกว่า Opus 4.8 **5 เท่า** ที่ performance ใกล้ ๆ กันในหลาย agent benchmark
- POV — นี่คือช่วงที่ **"agent-grade intelligence" กลายเป็น commodity** ในราคา mid-tier: การรัน agent 24/7 บน production ที่เมื่อ 6 เดือนก่อนต้อง Opus, วันนี้ Sonnet 5 ทำได้ที่ 1/5 ของราคา → เศรษฐศาสตร์ของ agent เปลี่ยน

## เกิดอะไรขึ้น

30 มิถุนายน 2026 — Anthropic ประกาศ Claude Sonnet 5 ผ่าน blog อย่างเป็นทางการ พร้อมข้อความเปิดว่า "It can make plans, use tools like browsers and terminals, and run autonomously at a level that, just a few months ago, required larger and more expensive models". แปลว่า Anthropic ไม่ pitch ตรงว่า "smart กว่า" — pitch ที่ **"autonomous กว่า ที่ราคาถูกกว่า"**

Benchmark ที่ Anthropic เลือกโชว์ก็บอกทิศทางชัด — **SWE-bench Pro** (real coding agent tasks) 63.2%, **OSWorld-Verified** (computer use) 81.2%, **BrowseComp** (agentic web search) 84.7%, **Terminal-Bench 2.1** 80.4% ที่แซง Opus 4.8 ที่ 74.6%, และ **GDPval-AA v2** 1,618 Elo ที่แซง Opus 4.8 ที่ 1,615. คือ benchmark ทั้งหมดที่วัดคือ **agent-in-action** ไม่ใช่ MMLU / GSM8K แบบสมัยก่อน. Message ที่ส่งไปหา dev คือ — ไม่ต้องเลือกระหว่าง smart กับถูก, Sonnet 5 กินทั้งสองอย่าง

**ราคา intro $2 in / $10 out** ทำให้เศรษฐศาสตร์ของ agent เปลี่ยนไปแบบตรง ๆ. Agent ที่ run 24/7 (background monitoring, data pipeline observability, coding review bot) เมื่อก่อนต้อง balance ระหว่าง Sonnet 4.6 ที่ถูกแต่ dumb กับ Opus 4.8 ที่ smart แต่แพง. ตัวอย่างเช่น agent ที่ทำ 100M input + 20M output token ต่อวัน — บน Opus 4.8 อยู่ที่ ~$1,900/day, บน Sonnet 5 intro price เหลือ $400/day. ต่อปี savings ~$550K ต่อ agent 1 ตัว

ที่เด่นสุดคือการ **ตั้งเป็น default** ให้ Free และ Pro user ทันทีในวัน launch — ปกติ Anthropic จะปล่อยให้ทดลองก่อนแล้วค่อย set default. รอบนี้ผลักเข้าไปเลย signal ว่ามั่นใจใน performance regression น้อย และอยากได้ agent traffic เข้ามาให้ไว. Fable 5 (Anthropic's smallest model) ก็กลับมา global ในวันเดียวกัน — ครบทั้ง 3 tier

## ทำไมสำคัญ

**Agent economics เปลี่ยนจาก "แพงเกินไปสำหรับ production" เป็น "ถูกพอที่จะ run continuous"**. รอบ 12 เดือนที่ผ่านมา คำถามที่ platform team ในบริษัทใหญ่ ๆ ถามคือ "จะเอา agent ไป run production ได้จริงตอนไหน?" — คำตอบทางเทคนิคคือ "ได้แล้ว", แต่คำตอบทางการเงินคือ "ยังไม่ค่อยคุ้ม". Sonnet 5 ที่ราคา 20% ของ Opus 4.8 บน performance 90-95% ของ Opus บน agent task เปลี่ยน equation นี้แบบ overnight. **payback period ของ agent project ลดลง 3-5 เท่า**

Pattern ที่เห็นในตลาดคือ **model tier compression** — ช่องว่างระหว่าง frontier กับ mid-tier แคบลงเรื่อย ๆ. Sonnet 5 vs Opus 4.8 ตอนนี้ต่างกันแค่ 6 คะแนน SWE-bench Pro, และแซงในบางเรื่อง (Terminal-Bench, GDPval). เทียบกับ 12 เดือนก่อน — Sonnet 3.5 vs Opus 3.5 ห่างกัน 15-20 คะแนน. Pattern เดียวกันเห็นในค่าย OpenAI (GPT-5.5 vs 5.6-mini) และ Google (Gemini 3 Pro vs Flash). สิ่งที่ implication คือ — **premium tier กำลังกลายเป็น "edge case optimizer"** ไม่ใช่ default choice อีกต่อไป

Timing ก็เป็นชั้นเชิงเชิงกลยุทธ์ — Sonnet 5 มาก่อน OpenAI GPT-5.6-workspace ที่ประกาศไปสัปดาห์ก่อน 2 วัน, และก่อน Google I/O agent update ปลายเดือน ก.ค. คือ Anthropic **claim price/performance leadership ในช่วงที่ Fortune 500 กำลังตัด budget FY27** (ต้นเดือน ก.ค. คือช่วง forecasting rush). CIO ที่กำลังเลือก vendor สำหรับ agent workload ปีหน้า เห็นตัวเลขนี้ + ราคา $2/$10 แล้วต้องกลับไปคำนวณใหม่

## มุม AI Agent Platform

**Builders** ที่สร้าง agent framework — ถึงเวลา re-benchmark default model choice. ถ้า framework ของคุณ default เป็น GPT-4o หรือ Claude Sonnet 4.6 ตอนนี้, ควร run eval บน Sonnet 5 ให้เห็นตัวเลข quality/cost curve ใหม่ ภายในสัปดาห์นี้. คนที่ทำ observability / cost tracking (Helicone, Langfuse, Braintrust, PromptLayer) จะเห็น traffic pattern shift ชัดในเดือน ก.ค. — คำนวณ savings recommendation ให้ user ให้ทัน. Framework ที่ hard-code Opus ใน high-quality workflow (Cline, Aider, Roo Code, Cursor Composer) ควรตั้ง Sonnet 5 เป็น "recommended default" แล้วให้ Opus เป็น escalation

**Users / business** ที่ pilot agent อยู่ในขั้น POC — นี่คือช่วงที่ CFO อนุมัติ scale-up ได้ง่ายที่สุดใน 18 เดือนที่ผ่านมา. เอา cost/token ของ Sonnet 5 ไปทำ 12-month projection + payback analysis, ตัวเลขจะ ชวนกว่ารอบก่อนมาก. ธุรกิจไทยที่ผัน pilot ค้างเพราะ TCO ไม่ผ่าน — call center automation, contract review, sales research — วันนี้ตัวเลขเปิดกลับมาน่ารันใหม่. คำเตือน: intro pricing $2/$10 หายหลัง 31 ส.ค., ถ้าจะ commit long-term contract ให้เจรจา rate lock ก่อน

## Sources
- [Introducing Claude Sonnet 5 — Anthropic](https://www.anthropic.com/news/claude-sonnet-5)
- [Anthropic launches Claude Sonnet 5 as a cheaper way to run agents — TechCrunch](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)
- [Anthropic Claude Sonnet 5 vs Sonnet 4.6 vs Opus 4.8: Agentic Coding Benchmarks — MarkTechPost](https://www.marktechpost.com/2026/06/30/anthropic-claude-sonnet-5-vs-sonnet-4-6-vs-opus-4-8-agentic-coding-benchmarks-api-pricing-and-cost-performance-tradeoffs-compared/)
- [Claude Sonnet 5: Benchmarks, Pricing & How It Compares — Codersera](https://codersera.com/blog/claude-sonnet-5-launch-guide-2026/)
- [Claude Sonnet 5: Features, Benchmarks, and Pricing — DataCamp](https://www.datacamp.com/blog/claude-sonnet-5)

---

## Audio script

วันที่สามสิบมิถุนายน Anthropic ปล่อย Claude Sonnet 5 ที่บริษัทเรียกว่า most agentic Sonnet ever built. ตัวเลข benchmark ที่โชว์ทั้งหมดเป็น agent-in-action — SWE-bench Pro หกสิบสามจุดสอง OSWorld แปดสิบเอ็ด BrowseComp แปดสิบสี่ Terminal-Bench แปดสิบจุดสี่ ที่จริง ๆ แซง Opus 4.8 ในสองเรื่อง.

จุดเปลี่ยนจริง ๆ อยู่ที่ราคา — intro pricing สองดอลลาร์ต่อล้าน token อินพุต สิบดอลลาร์ต่อล้าน token เอาต์พุต ถึงสิ้นสิงหาคม. ถูกกว่า Opus 4.8 ห้าเท่าที่ performance ใกล้กันมาก. Agent ที่รัน continuous ยี่สิบสี่ชั่วโมง ที่เมื่อก่อนต้อง Opus 4.8 เพราะต้องการ quality — วันนี้ Sonnet 5 ทำได้ที่ 1 ใน 5 ของราคา. Agent ที่กิน 100M input 20M output ต่อวัน savings หลักล้านต่อปี.

Pattern ที่เห็นในตลาดคือ model tier compression — ช่องว่างระหว่าง frontier tier กับ mid tier แคบลงเรื่อย ๆ. Sonnet 5 vs Opus 4.8 ตอนนี้ต่างกันแค่หกคะแนน SWE-bench เมื่อ 12 เดือนก่อนต่างกันสิบห้าถึงยี่สิบคะแนน. Pattern เดียวกันในค่าย OpenAI กับ Google. Premium tier กำลังกลายเป็น edge case ไม่ใช่ default อีกแล้ว.

สำหรับทีมที่สร้าง agent framework — re-benchmark ให้ทัน. ถ้ายัง default เป็น GPT-4o หรือ Sonnet 4.6, ต้อง run eval บน Sonnet 5 ให้เห็นตัวเลข quality cost curve ใหม่ ภายในสัปดาห์นี้. ฝั่ง business ที่ pilot agent ค้างเพราะ TCO ไม่ผ่าน — วันนี้ตัวเลขเปิดกลับมาน่ารันใหม่ทั้งหมด. คำเตือนเดียวคือ intro pricing หายหลังสิงหาคม ถ้า commit long-term contract ให้เจรจา rate lock ให้ทัน.
