---
date: 2026-07-25
slug: anthropic-claude-opus-5-half-price
topic: agent-platform-trend
reading_time_min: 4
sources: 5
image_prompt: |
  An editorial isometric illustration on a warm cream background: two
  price tags hanging from a glass laboratory rack, the left one labeled
  "FABLE 5 · $10 / $50" crossed out in red, the right one labeled
  "OPUS 5 · $5 / $25" glowing green. Between them, a benchmark chart
  bar showing three columns "18.7 · 33.7 · 43.3" with the tallest bar
  stamped "OPUS 5 · FRONTIER-BENCH". At the base, a small conveyor
  belt of tiny agent icons (browser, terminal, subagent tree) flowing
  from left to right. Sharp editorial typography, high contrast,
  1:1 aspect, no real human faces.
image: images/26-07-25-0610-01-anthropic-claude-opus-5-half-price.png
---

# Anthropic Opus 5 มาแล้ว — ราคาครึ่งเดียวของ Fable 5, ชนะบน Frontier-Bench + OSWorld, จ่อ default runtime สำหรับ agent builder

## TL;DR
- Anthropic ปล่อย Claude Opus 5 วันศุกร์ 24 ก.ค. — โมเดลตัวที่สี่ในสองเดือน — ราคา **$5/$25 ต่อล้าน token** เท่า Opus 4.8 แต่ **ครึ่งเดียว** ของ Fable 5 ($10/$50)
- Frontier-Bench v0.1: **Opus 5 43.3%** vs Fable 5 33.7% vs Opus 4.8 18.7%; OSWorld 2.0 computer-use ชนะ Fable 5 ที่ ~1/3 ของราคา
- Harvey ตัด token usage เฉลี่ย **26%** ที่ quality เท่า Opus 4.8; Zapier รัน churn-prevention workflow ครบ end-to-end โดยไม่กิน token เพิ่ม
- Claude Code เปลี่ยน default Opus เป็น 5 + ขยาย MCP handling + nested subagent — signal ว่า Anthropic ตั้งใจให้เป็น default runtime สำหรับ agent orchestration

## เกิดอะไรขึ้น
วันศุกร์ที่ 24 กรกฎาคม 2026 Anthropic ประกาศ Claude Opus 5 ตอนเช้า US time — เป็น **โมเดลตัวที่สี่ในสองเดือน** (Sonnet 5 → Haiku 4.5 → Opus 4.8 → Opus 5) ที่ Anthropic ปล่อยตามยุทธศาสตร์ frequent-release. ราคา API ตั้งไว้ที่ **$5 ต่อล้าน input token / $25 ต่อล้าน output token** — เท่ากับ Opus 4.8 ที่ปล่อยเมื่อกลางเดือน แต่ **เพียงครึ่งเดียว** ของ OpenAI Fable 5 ($10/$50) ซึ่งเป็นคู่แข่งโดยตรงในตลาด frontier-tier. Opus 5 กลายเป็น default สำหรับ Claude Max subscriber ทันที และเป็น top-tier option บน Claude Pro.

Benchmark ที่ Anthropic เปิด — **Frontier-Bench v0.1 (agentic + coding + reasoning composite): Opus 5 ทำ 43.3%** เทียบกับ Fable 5 33.7% และ Opus 4.8 18.7%. บน **OSWorld 2.0** (benchmark computer-use ที่ให้ agent คุมเบราว์เซอร์ + desktop app ทำ task จริง) Opus 5 ทำได้เหนือกว่า Fable 5 ที่ราคาประมาณ **1/3**. ด้าน cyber Opus 5 หา vulnerability ได้ 79.4% (เทียบ Mythos 5 ที่ 80%) แต่ working exploit ได้แค่ 4 จาก 13 ของ Mythos 5 — Anthropic เขียนใน model card ว่าเป็น choice ตั้งใจ ให้เก่ง defensive มากกว่า offensive.

Design goal ของ Opus 5 ไม่ใช่ longest-running autonomous task (ยังเป็น Opus 4.8 กับ Claude for Research) แต่เป็น **"daily professional use"** — task ที่ human กับ agent สลับกันคุม, tool call เยอะ, latency ต้องต่ำ, budget ต้องอ่านออก. Anthropic ยังใส่ **effort dial** ที่ให้ dev เลือก reasoning depth ตั้งแต่ minimal ถึง extended — pay-per-quality tradeoff ที่ทำ AI bill "turn-downable" — pattern เดียวกับที่ OpenAI intro ใน o3-mini แต่ตอนนี้ Anthropic implement บน flagship tier.

Early customer benchmark ที่ Anthropic quote — Harvey (legal AI) ตัด **average token usage 26%** ที่ quality เท่า Opus 4.8 (มีความหมายว่า enterprise ที่ใช้ Opus อยู่แล้วจะเห็น bill ลดลง 26% ทันทีที่ switch); Zapier รัน churn-prevention workflow ครบ end-to-end (research → draft outreach → schedule → follow up) **โดยไม่กิน token เพิ่ม** จาก Opus 4.8. GitHub, Notion, Perplexity — ทั้งหมด default agent tier ไป Opus 5 ในสัปดาห์เดียวกัน. Claude Code CLI ก็ update วันเดียวกัน — Opus 5 เป็น default Opus, MCP handling รองรับ 2026-07-28 spec RC (ดู brief #3), และ nested subagent (subagent เรียก subagent เรียก subagent) เปิดใช้งานทั่ว.

## ทำไมสำคัญ
**Anthropic กำลังบีบ gap ระหว่าง frontier กับ mainstream** — ราคาครึ่งเดียวของ Fable 5 บน model ที่ชนะบน composite benchmark ที่ Anthropic เลือกมา ไม่ใช่ marketing move — เป็น pricing pressure โดยตรงต่อ OpenAI GPT-5.6 tier ที่กำลัง gate feature ตาม price band ($10/$50 สำหรับ Fable 5, $25/$125 สำหรับ Fable 5 Pro). Enterprise buyer ที่กำลัง sign contract Q3 ต้องกลับมาถามคำถามใหม่: ทำไมต้องจ่าย premium tier ตลอด production traffic ในเมื่อ Opus 5 ทำได้เท่าหรือดีกว่าใน 90% ของ workload? Salesforce Agentforce, Sierra, Cognigy, Vertex Agent Builder — ทุก platform ต้องเปิด switch ให้ enterprise เลือก Opus 5 default ในไตรมาสนี้ ไม่งั้นจะเสีย workload ให้คู่แข่งที่เร็วกว่า.

Pattern ที่ crystallize คือ **frequent-release cadence + aggressive pricing = compounding market share**. Anthropic ปล่อย 4 model ใน 2 เดือน — velocity ที่ OpenAI ไม่ match ในไตรมาสนี้ (GPT-5.5 ปลาย ก.ค., GPT-5.6 คาด ก.ย.). ทุก release ทำให้ Claude Max/Pro subscription ดึงดูดขึ้น, และทุก benchmark win Anthropic เอาไปอ้างใน sales cycle. เทียบกับ 12 เดือนที่แล้ว Anthropic ครองแค่ coding niche — วันนี้ครอบทั้ง code + agent runtime + enterprise governance. Google Gemini 3.6 กับ Alibaba Qwen 3.8-Max ยังตามหลังใน US enterprise deal cycle.

Sub-signal สำคัญ: **effort dial + nested subagent + MCP 2026-07-28 support** — สามอย่างนี้รวมกันแปลว่า Anthropic ตั้งใจให้ Claude Code เป็น **default runtime สำหรับ agent orchestration** ไม่ใช่แค่ chat interface. Dev ที่กำลังตัดสินใจระหว่าง LangGraph + framework glue vs. Claude Code + native MCP ตอนนี้เริ่มเจอ trade-off ที่ tilts ไปทาง native — เพราะ subagent tree, tool call caching, และ error recovery ถูก tune กับ Opus 5 โดยตรง.

## มุม AI Agent Platform
สำหรับ **builders** ที่กำลังสร้าง production agent — Opus 5 ทำให้ always-on computer-use และ long-tool-chain workflow **economically viable ที่ 1/3 ของราคาเดิม**. ถ้าเคยไม่กล้าให้ agent run 30-minute autonomous task เพราะ token bill พุ่ง ตอนนี้เปิดได้ทั้งวัน. คำถาม architecture ที่ต้อง revisit ทันที: (1) เปลี่ยน default LLM ใน framework จาก Sonnet 5 → Opus 5 คุ้มไหม (คำตอบ: คุ้ม ถ้า workload มี computer-use หรือ multi-turn tool call), (2) merge Fable 5 tier กับ Opus 5 tier เป็น single-model deployment ได้ไหม (ประหยัด operational complexity + billing overhead), (3) migrate ไป Claude Code CLI + MCP native แทน framework glue คุ้มไหม.

สำหรับ **enterprise users** — เจรจา contract renewal ทันที. Salesforce Agentforce, ServiceNow AI Agent, Google Vertex Agent Builder — ทุกเจ้าใช้ Anthropic เป็น sub-provider ใน model routing layer. Opus 5 พร้อมใช้ผ่าน AWS Bedrock + Azure AI Foundry + Vertex ในวันเดียวกัน. ขอ **price adjustment clause** ที่ทำให้เมื่อ underlying model ราคาลด, contract ก็ลดตาม (ไม่ใช่ vendor เก็บ margin ไว้เอง). ถ้า vendor ปฏิเสธ = เป็น signal ว่า vendor กำลัง extract rent จาก LLM price arbitrage.

สำหรับ **ecosystem** — pressure ต่อ standalone framework (LangGraph, CrewAI, Autogen, LlamaIndex) เพิ่มขึ้น เพราะ Claude Code + nested subagent + MCP native ทำ orchestration ระดับ production ได้แบบ zero framework overhead. Differentiation ของ framework ต้อง shift ไป (1) **cross-vendor portability** (workflow เดียวกันรันได้บน Claude/GPT/Gemini), (2) **domain-specific abstraction** (RAG pipeline, evaluation harness, agent memory), (3) **enterprise governance** (audit log, policy enforcement, PII redaction). ถ้ายังขาย "wrapper รอบ tool call" คน default Claude Code แทน.

## Sources
- [Anthropic launches Claude Opus 5 (Yahoo Tech)](https://tech.yahoo.com/ai/claude/articles/anthropic-launches-claude-opus-5-172317294.html)
- [Anthropic unveils more cost-efficient model for everyday tasks (Bloomberg)](https://www.bloomberg.com/news/articles/2026-07-24/anthropic-unveils-more-cost-efficient-model-for-everyday-tasks)
- [Anthropic Claude Opus 5 launch benchmarks (TNW)](https://thenextweb.com/news/anthropic-claude-opus-5-launch-frontier-bench-coding)
- [Claude Opus 5 launch benchmarks price recap (Tech-ish)](https://tech-ish.com/2026/07/24/claude-opus-5-launch-benchmarks-price/)
- [Anthropic Claude Opus 5 pricing strategy (Quartz)](https://qz.com/anthropic-claude-opus-5-fable-5-price-072426)

---

## Audio script
สวัสดีครับ วันนี้ Anthropic เปิดตัว Claude Opus 5 — โมเดลตัวที่สี่ในสองเดือน. จุดที่น่าตกใจคือราคา — ห้าดอลลาร์ต่อล้าน input token, ยี่สิบห้าต่อล้าน output — เท่ากับ Opus 4.8 แต่เพียงครึ่งเดียวของ Fable 5 ของ OpenAI. Benchmark ที่ชื่อ Frontier-Bench Opus 5 ทำได้สี่สิบสามเปอร์เซ็นต์, ชนะ Fable 5 ที่สามสิบสามเปอร์เซ็นต์, และทิ้ง Opus 4.8 ที่สิบแปดเปอร์เซ็นต์แบบขาดลอย. บน OSWorld ที่ทดสอบ computer-use Opus 5 ก็ชนะที่ราคาแค่หนึ่งในสามของ Fable 5. Harvey เจ้าของ legal AI platform บอกว่า switch แล้วประหยัด token เฉลี่ยยี่สิบหกเปอร์เซ็นต์ที่คุณภาพเท่าเดิม. Zapier รัน churn-prevention workflow ได้ครบทั้งกระบวนการโดยไม่กิน budget เพิ่ม. Anthropic ยังเปิด effort dial ให้ dev เลือก reasoning depth ได้ — pay per quality trade-off ที่ทำให้ AI bill turn downable. Claude Code CLI ก็ update ตาม — default Opus เปลี่ยนเป็น 5, MCP handling รองรับ spec ใหม่ 2026-07-28, และ nested subagent เปิดใช้งานทั่ว. สิ่งนี้แปลว่า Anthropic ตั้งใจให้ Claude Code เป็น default runtime สำหรับ agent orchestration ไม่ใช่แค่ chat interface. สำหรับ builder ที่กำลัง review architecture ไตรมาสนี้ คำถามหลักคือ — จะเปลี่ยน default LLM เป็น Opus 5, จะ migrate ไป Claude Code แทน framework glue, และจะเจรจา price adjustment clause กับ vendor ที่ใช้ Anthropic sub-provider หรือเปล่า. แนะนำให้เริ่มทดสอบวันนี้ครับ.
