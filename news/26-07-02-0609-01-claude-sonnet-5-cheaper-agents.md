---
date: 2026-06-30
slug: claude-sonnet-5-cheaper-agents
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial hero illustration for a tech-magazine cover. A giant scale
  balance: on the left, a small glowing "Sonnet 5" orb with a tiny price
  tag stacked "$2 IN · $10 OUT"; on the right, a much larger "Opus 4.8"
  orb barely tipping the beam. Behind, a dark control-room wall with
  four vertical benchmark bars labeled "SWE 63.2", "TERMINAL 80.4",
  "OSWORLD 81.2", "BROWSECOMP 84.7" — bold amber numbers over deep
  navy. Bottom ribbon reads "1M CONTEXT · AGENTIC BY DEFAULT". Small
  Anthropic logo lower-right. Cinematic isometric editorial style,
  ultra-sharp text rendering for 200px thumbnail readability, 1:1
  aspect ratio, no real human faces.
image: images/26-07-02-0609-01-claude-sonnet-5-cheaper-agents.png
---

# Claude Sonnet 5 — Anthropic ปล่อย "Opus-class agent" ราคาถูกลง 5 เท่า, ล้ม unit economics ของทั้ง agent market

## TL;DR
- 30 มิ.ย. — Anthropic ปล่อย **Claude Sonnet 5** (`claude-sonnet-5`) กลายเป็น default ทันทีใน claude.ai + Claude Code + Bedrock + Vertex AI. Promo pricing **$2/$10 per Mtok** ถึง 31 ส.ค. (std $3/$15) — เทียบ Opus 4.8 ที่ $15/$75, ประหยัด **~5–7.5x**
- Benchmark: SWE-bench Pro **63.2%**, Terminal-Bench 2.1 **80.4%**, OSWorld-Verified **81.2%**, BrowseComp **84.7%** — Sonnet 5 = Opus-class ที่ราคา Sonnet. GDPval-AA Elo 1,618 แซง Opus 4.8 (1,615) ในงาน knowledge-work
- 1M context + selectable reasoning effort (low / medium / high / max / x-high) — ทำให้ agent builder tune cost-per-task ได้แบบ SKU. ทุก platform ที่ pricing agentic workflow "ต่อ run" จะเจอ margin compression ทันที

## เกิดอะไรขึ้น

30 มิถุนายน 2026 — Anthropic ปล่อย Claude Sonnet 5 พร้อมประกาศเปลี่ยน default model ของ claude.ai ทันทีสำหรับผู้ใช้ Free/Pro และตั้งเป็น default ใหม่ของ Claude Code. TechCrunch พาดหัวตรง ๆ ว่า **"cheaper way to run agents"** — สะท้อนธีมหลักของ launch นี้: Anthropic ไม่ได้ขาย model ที่ smarter กว่าเดิม แต่ขายให้ **agent unit economics พลิกดีขึ้น**

Sonnet 5 ทำคะแนน SWE-bench Pro ที่ 63.2% (Opus 4.8 อยู่ที่ 69.2%) แต่ที่น่าตกใจกว่าคือ Terminal-Bench 2.1 พุ่งไป 80.4% จาก 67.0% ของ Sonnet 4.6 — improvement 13 จุดใน 4 เดือน. คะแนน computer-use OSWorld-Verified อยู่ที่ 81.2% และ agentic search BrowseComp ที่ 84.7% ทั้งสองตัวใกล้เคียงกับ Opus 4.8. ที่ครอส line ที่สุดคือ GDPval-AA v2 (Anthropic's knowledge-work benchmark) — Sonnet 5 ทำ Elo 1,618 แซง Opus 4.8 ที่ 1,615 ไปเล็กน้อย. คือ Sonnet เล็ก ๆ ที่ **แซง Opus ในบางงานจริง**

Sonnet 5 มี native 1M-token context, และเพิ่ม knob ใหม่ **selectable reasoning effort** ห้าระดับ (low / medium / high / max / x-high). API ให้ developer เลือก effort ต่อ call — effort ต่ำจ่ายน้อยแต่คิดตื้น, effort สูงจ่ายมากแต่ deep. หมายถึง agent orchestrator สามารถ tune cost-quality tradeoff แบบ per-step ได้ — task routing แบบเก่า "Haiku for cheap, Opus for hard" ตอนนี้ยุบเหลือ Sonnet 5 ตัวเดียวคุมทั้ง spectrum

Detail สำคัญที่ builder หลายเจ้ายังไม่ทัน digest — **Sonnet 5 ใช้ tokenizer ใหม่** ที่ทำให้ input เดียวกันแปลงเป็น token **~1.0-1.35x** เมื่อเทียบ Sonnet 4.6. คือ effective price ของ Sonnet 5 ไม่ใช่ $2/$10 เสมอไป — ในเอกสาร-หนัก workflow อาจกลายเป็น ~$2.7/$13.5 effective. TechCrunch และ Caylent ต่างชี้ว่า benchmark cost projection แบบเก่า (สมมติ 1:1 token ratio) จะ under-estimate cost ของ agent ที่รัน production

## ทำไมสำคัญ

**Sonnet 5 ไม่ได้เปลี่ยน frontier — เปลี่ยน "middle tier" ของ agent stack**. ในรอบ 6 เดือนที่ผ่านมา pattern ของ Anthropic ชัด: Opus ยกระดับ ceiling (4.8 ก.ค. → 4.7 [1M] มิ.ย.), Sonnet ยกระดับ **cost/quality frontier**. คนที่จะโดนกระทบหนักคือ agent platform ที่ pricing แบบ **per-run subscription** (Sierra, Decagon, Cognigy, Kore.ai) — ถ้า unit cost ของ Claude ลด 5 เท่า, gross margin ของแพลตฟอร์มพวกนี้ขยายทันที (ดีต่อพวกเขา) แต่ **ราคาที่ขายลูกค้าก็มี pressure ลง** เพราะลูกค้า benchmark กับ Anthropic API โดยตรงได้

เทียบกับ OpenAI GPT-5.6 Sol/Terra/Luna ที่ preview 26 มิ.ย. — Sonnet 5 มา 4 วันหลังและตอบโจทย์คนละ segment. Sol เจาะ frontier reasoning, Terra ที่ราคาสมเหตุสมผล, Luna ที่ราคาถูกสุด. Sonnet 5 อยู่ระหว่าง Terra กับ Sol ในด้านคุณภาพแต่ **ราคาถูกกว่า Terra ~40%** (Terra pricing = ~$3.5/$14 mtok in early leak). เกมนี้กลายเป็น price war ที่ agent builder ได้ประโยชน์: ทุก 4-6 เดือนจะมี model ใหม่ที่ทำให้ agent เดิมประหยัดลง 30-50% ยิ่งเปิดโอกาสให้ startup รุ่นใหม่กระโดดเข้ามาโดยไม่ต้องระดมทุนก้อนโต

Signal ที่ 2 — **selectable reasoning effort** เป็น product move ที่ deeper กว่าที่ดู. Anthropic กำลัง productize compute budget ให้กลายเป็น first-class API parameter. คู่แข่งจะต้อง match: OpenAI มี reasoning_effort อยู่แล้วใน o-series, Google มี thinking_budget ใน Gemini 3. ในอีก 12 เดือน จะเกิด standard interoperable **effort spec** ข้าม provider (คล้าย OpenAPI spec ของ tool call) ซึ่ง MCP อาจ absorb เข้าไปด้วย — คือ agent orchestrator จะ route ระหว่าง provider โดย effort budget เป็นตัวแปรร่วม

## มุม AI Agent Platform

**Builders** — ถ้าคุณเป็น agent framework (LangGraph, LlamaIndex, Dust, Vercel AI SDK, OpenBridge, Sierra, Sema4) ให้ **default new agent template ไป Sonnet 5 + medium effort** ภายในสัปดาห์นี้. ที่สำคัญกว่านั้น — เพิ่ม `reasoning_effort` เข้า config schema ของคุณด้วย เพราะไม่งั้นลูกค้าไม่มีทาง tune. ถ้าคุณเป็น per-run pricing platform, model change ต้อง propagate เข้า pricing calculator ภายใน 48 ชั่วโมง (Snowflake / Databricks / Vercel เจอบทเรียนนี้จาก Claude 3.5 → 3.7 ที่ pricing ล้าสมัย 2 อาทิตย์ ลูกค้าโวย). Watch tokenizer — ถ้า tool call ของคุณ marshal JSON เยอะ ๆ token inflation อาจสูงเกิน 1.2x

**Users / business** — enterprise ที่ deploy agent ผ่าน Anthropic โดยตรง (Bank, insurer, healthcare payer) ได้ **free 5-7x cost reduction** ทันทีโดยไม่ต้องแก้ prompt — แค่เปลี่ยน model name. ถ้ามี budget เหลือควรใช้เพื่อ scale coverage ของ agent (ทำงานตลอด 24/7 ทุก channel) หรือย้าย task ที่เดิมส่งไป human ให้ agent handle เพิ่ม. ประเด็นสำคัญที่หลายคนจะพลาด — **reasoning effort = knob สำหรับ compliance**. ในงานที่ต้อง auditable (loan approval, medical claim), เขียน policy ว่า "high effort mandatory" ทำให้ audit trail แจ้งเตือนได้ว่า decision ผ่าน deep reasoning จริง ๆ

**Ecosystem** — Google Vertex AI + Amazon Bedrock day-one available สะท้อนว่า hyperscaler channel เป็น neutral ground ที่ทั้ง Anthropic + OpenAI + Google เอง compete. Distribution moat ของ Anthropic ตอนนี้อยู่ที่ 3 ชั้น: (1) Foundry (Microsoft), (2) Bedrock + Vertex (AWS + Google), (3) SI channel (PwC + Globant + คุยกับ Wipro). ที่หายไปคือ **on-prem / air-gapped** — ตลาด defense / regulated European ยังไม่มี story ชัดจาก Anthropic เทียบกับ OpenAI ที่จับ Dell/Codex on-premises แล้ว

## Sources
- [Introducing Claude Sonnet 5 — Anthropic](https://www.anthropic.com/news/claude-sonnet-5)
- [Anthropic launches Claude Sonnet 5 as a cheaper way to run agents — TechCrunch](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)
- [Anthropic Claude Sonnet 5 vs Sonnet 4.6 vs Opus 4.8: Agentic Coding Benchmarks — MarkTechPost](https://www.marktechpost.com/2026/06/30/anthropic-claude-sonnet-5-vs-sonnet-4-6-vs-opus-4-8-agentic-coding-benchmarks-api-pricing-and-cost-performance-tradeoffs-compared/)
- [Claude Sonnet 5 Launch Analysis: What Changed, What Matters — Caylent](https://caylent.com/blog/claude-sonnet-5-launch-analysis-what-changed-what-matters-and-what-to-validate)
- [Claude Sonnet 5 Benchmarks Explained — Vellum](https://www.vellum.ai/blog/claude-sonnet-5-benchmarks-explained)

---

## Audio script

วันที่สามสิบมิถุนายน Anthropic ปล่อย Claude Sonnet 5 กลายเป็น default ของ claude.ai และ Claude Code ทันที. TechCrunch พาดหัวว่านี่คือทางที่ถูกกว่าในการรัน agent — โปรโมชั่นสองดอลลาร์ต่อล้าน token ขาเข้า สิบดอลลาร์ต่อล้าน token ขาออก ถึงสิ้นเดือนสิงหาคม เทียบ Opus 4.8 ที่สิบห้ากับเจ็ดสิบห้า ประหยัดห้าถึงเจ็ดเท่า.

Benchmark น่าตกใจ — Terminal-Bench 2.1 พุ่งจากหกสิบเจ็ดของ Sonnet 4.6 ไปแปดสิบสี่ในสี่เดือน. GDPval knowledge work Elo หนึ่งพันหกร้อยสิบแปด แซง Opus 4.8 ไปเล็กน้อย. หมายถึง Sonnet เล็ก ๆ แซง Opus ในบางงานจริง แล้วราคาถูกลงเกือบสิบเท่า.

จุดที่เปลี่ยนเกมคือ selectable reasoning effort ห้าระดับ ตั้งแต่ low ถึง extra high. Developer เลือก effort ต่อ call ได้. Task routing แบบเก่า Haiku ราคาถูกกับ Opus ยาก ๆ ตอนนี้ยุบรวมใน Sonnet 5 ตัวเดียว. Detail ที่หลายคนจะพลาด — Sonnet 5 ใช้ tokenizer ใหม่ ที่ทำให้ input เดิมกลายเป็น token หนึ่งถึงหนึ่งจุดสามห้าเท่า. Effective price จริงจึงสูงกว่าที่โฆษณาราว 20-35% ในงานเอกสารหนัก.

สำหรับ agent platform ที่ pricing แบบ per-run — Sierra, Decagon, Cognigy — margin ขยายทันที แต่ราคาที่ขายลูกค้าจะมี pressure ลงเพราะลูกค้า benchmark กับ API ตรงได้. Enterprise ที่ deploy ผ่าน Anthropic ตรง ได้ cost reduction ห้าถึงเจ็ดเท่าฟรี แค่เปลี่ยนชื่อ model. ที่ควรใช้ budget ที่เหลือ ไม่ใช่ save เก็บ แต่เอาไปขยาย coverage ให้ agent วิ่งครบทุก channel หรือย้าย task ที่ human handle อยู่ให้ agent รับต่อ. Reasoning effort ยังเป็น knob สำหรับ compliance ที่ยังไม่มีใครพูดถึง — ในงาน audit-critical เขียน policy บังคับ high effort แล้ว log ไว้ ก็เป็น evidence ที่ regulator ยอมรับได้.
