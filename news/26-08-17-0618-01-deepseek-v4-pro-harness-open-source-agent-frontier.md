---
date: 2026-08-17
slug: deepseek-v4-pro-harness-open-source-agent-frontier
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial isometric illustration of a giant open-source treasure chest labeled
  "DeepSeek Harness v0.1" spilling out toolbelts, wrenches, and blueprints onto
  a table; a red dragon-shaped datacenter looms behind it. Three stacked giant
  numbers dominate the composition: "1.6T PARAMS", "1M CONTEXT", "MIT LICENSE".
  Small "OpenAI Responses API compatible" stamp bottom-right. Silhouettes of
  Western frontier-lab towers in the far background dwarfed by the dragon.
  Editorial magazine style, thick outlines, high contrast readable at 200px
  thumbnail, 1:1 aspect, no real human faces.
image: images/26-08-17-0618-01-deepseek-v4-pro-harness-open-source-agent-frontier.png
---

# DeepSeek V4 Pro 0813 GA + open-source ตัว agent harness — โมเดล frontier ตัวแรกที่มาพร้อม runtime ให้ใช้ฟรี, กำลังจะพลิกเกม agent stack ทั้งวงการ

## TL;DR
- **13 ส.ค. 2026** — DeepSeek ปล่อย **V4-Pro GA (build 0813)** พร้อม **open-source `DeepSeek Harness v0.1`** ภายใต้ MIT license — โมเดล frontier ตัวแรกที่ ship agent runtime ให้ใช้ฟรีคู่กับ weights
- **1.6T total params / 49B active per token, 1M context, 384k output** ต่อ request — scored **53 บน Artificial Analysis Intelligence Index** (median open-weights = 27), tuned สำหรับ agent tool-use workflow
- API เข้ากันได้กับ **OpenAI Responses API format** และ **Codex integration** built-in — swap DeepSeek แทน GPT ใน harness เดิมได้ทันที
- **Price hike Aug 16 (วันนี้)** — output token $0.87 → $3.96/M ที่ peak (4.5×) — แต่ยังถูกกว่า Fable 5 ($50/M) 12–13 เท่า
- Signal: จีน open-source ไม่ใช่แค่ให้ weights แล้ว — ให้ **ทั้ง stack agent runtime** เพื่อดัน adoption

## เกิดอะไรขึ้น
วันพฤหัสฯ 13 สิงหาคม 2026 DeepSeek ปล่อย **V4-Pro-0813** ออกจากสถานะ preview เข้าสู่ **General Availability** พร้อมกันสามช่องทาง — app, web, และ API ตัวเลขบน paper spec ทำให้ทั้งวงการต้องอ่านซ้ำ: **Mixture-of-Experts 1.6 trillion parameters** โดย active per token แค่ 49B (efficient inference ratio 3%), รองรับ **1M token context** และ generate ได้สูงสุด **384,000 output tokens** ในหนึ่ง request — เพียงพอสำหรับ agent loop ที่ต้อง reasoning หลายสิบ step ต่อเนื่องโดยไม่ต้อง restart context

ที่ทำให้ทั้ง OSS community stop-scroll ไม่ใช่ตัวโมเดล — แต่คือประกาศคู่กันว่า **DeepSeek ปล่อย `DeepSeek Harness v0.1`** เป็น **open-source agent runtime framework** บน GitHub ภายใต้ **MIT license** เป็นครั้งแรกที่ frontier lab ตัวใหญ่ ship "โมเดล + runtime" มาด้วยกัน แทนที่จะปล่อย weight แล้วให้ community เขียน harness เอง (แบบ Llama, Mistral, Qwen ที่ผ่านมา) — ผลคือ dev ที่อยากลอง agent workflow ไม่ต้องเริ่มจากศูนย์ หรือดัด LangChain/CrewAI ให้เข้ากับ tool-calling convention ของ DeepSeek อีกต่อไป

DeepSeek ทำต่อไปอีกขั้น: API endpoint ของ V4-Pro **compatible กับ OpenAI Responses API format ทันที out-of-the-box** และ **built-in Codex integration** — สำหรับ dev ทุกคนที่ built agent บน OpenAI SDK แล้วอยากลอง DeepSeek แค่เปลี่ยน base_url + API key เดิม compile ผ่าน ไม่ต้อง refactor tool schema, streaming logic, หรือ retry pattern — friction เท่ากับศูนย์

แต่ก่อนที่ dev community จะฉลอง — วันนี้ **16 ส.ค. 16:00 UTC** DeepSeek ขึ้นราคา API ทั้ง family: V4-Pro output tokens จาก $0.87/M rate flat → **$3.96/M ที่ peak hours** = ขึ้น **4.5 เท่า**; อีกหลาย tier ขึ้น 50–1,100% ตาม token type. เหตุผลชัดคือ **agent workload = token consumption สูงมาก** (400M SDK download/เดือน ของ MCP บอก volume) — DeepSeek พยายาม harvest revenue ก่อน commoditize รอบต่อไป ซึ่ง Anthropic Fable 5 อยู่ที่ $50/M output ก็ยังแพงกว่า V4-Pro peak 12–13 เท่า — ยังมี headroom อีกเยอะ

## ทำไมสำคัญ
เรื่องนี้เปลี่ยน **agent stack default** เร็วขึ้น 2–3 quarter จีนหลุดพ้นภาพ "open-weight = intelligence ต่ำ" ตั้งแต่ V4 Flash (score 50) แล้ว V4-Pro 0813 (score 53) วางตัวชนกับ mid-tier frontier ของ Anthropic/OpenAI ได้ในหลาย benchmark และการ ship harness มาด้วย = signal ว่า DeepSeek ต้องการเป็น **default agent runtime สำหรับ dev ที่อยากคุมต้นทุน** ไม่ใช่แค่ raw model provider

Pattern สำคัญ 3 อย่างที่ทีม product ต้องดู: หนึ่ง — **"Model + harness bundle" กำลังจะเป็น new default** เพราะ frontier lab ทุกเจ้ารู้แล้วว่า latency ต่อ agent turn = user experience — ปล่อยแค่ weight แล้วปล่อยให้ community ต่อไม่พอ; รอ Anthropic กับ Google ปล่อย equivalent ภายใน Q4. สอง — **OpenAI Responses API กำลังกลายเป็น de-facto interface standard** ไม่ใช่ Chat Completions อีกต่อไป — DeepSeek pick side ชัด, Google Gemini ทำ compat layer แล้ว, Mistral รอเวอร์ชั่นถัดไป. สาม — **agent-tuned model** จะแซง general-purpose model ในตลาด mid-tier ภายในสิ้นปี — ตลาดจะ split เป็น "agentic tier" vs "chat tier" ต่างกันชัดเจน

Signal ที่จับตาต่อ: Anthropic Fable 5.1 (คาด Q4) น่าจะปล่อย Claude Skills SDK ให้ community + ship agent harness ที่ compatible กับ MCP 2026-07-28 spec; OpenAI Codex ที่เพิ่ง GA จะขยับเป็น universal harness เชื่อมกับ Presence platform; และคาดว่า Llama 5 (Meta, ต.ค.) จะตอบด้วย open-source harness ของตัวเองเพื่อไม่เสีย developer mindshare

## มุม AI Agent Platform
**Builders** ที่สร้าง framework: cost/benefit ของการ **fork DeepSeek Harness** vs. keep building บน LangGraph/CrewAI/AutoGen ต้อง reevaluate ทันที — MIT license = ใช้ commercial ได้เต็มที่ + code base มาจาก team ที่เข้าใจ model behavior ลึกที่สุด (เพราะ train เอง). Framework maker ที่จับ multi-provider abstraction (LiteLLM, Vercel AI SDK) ได้ประโยชน์เพราะ DeepSeek ตัดปัญหา schema mismatch ทันที; framework ที่พึ่ง lock-in บน OpenAI/Anthropic tool schema ต้องเร่ง port

**Users / business** ที่ deploy agent ใน workflow: **token budget อยู่ที่ประเด็นสำคัญ** ตอนนี้ — cost หลัง price hike ยังต่ำกว่า Claude/GPT 5–10× แต่คำถามคือ **quality-adjusted cost per successful task** ไม่ใช่ raw token — ต้อง benchmark บน workload ตัวเอง (multi-step reasoning, tool call correctness, hallucination rate) ก่อน migrate. บริษัทที่รัน agent volume สูง (call center, coding automation, batch analysis) จะเป็นกลุ่มแรกที่ POC — enterprise ที่พึ่ง compliance/data residency ต้องดู hosted option (Baseten, Fireworks, Together จะรีบ pick up)

**Ecosystem**: คนได้ประโยชน์ (1) **inference broker/router** (OpenRouter, Portkey, Groq) — DeepSeek พร้อม deploy บน non-DeepSeek infra ทันทีเพราะ weight open, (2) **Codex-compatible tool marketplace** — third-party tool provider ที่ conform Responses API format ได้ instant reach ผ่าน DeepSeek user base, (3) **China cloud provider** (Alibaba, Baidu, Huawei) ที่ host DeepSeek — ได้ enterprise workflow บ้าน western ที่หวัง cost ต่ำ. คนเสีย = **Anthropic/OpenAI margin structure** ต้อง defend premium ด้วย "quality moat" ให้จริง ไม่ใช่แค่ marketing และ **agent framework startup ที่โฟกัส OpenAI-only** จะโดน commoditize ไว

## Sources
- [DeepSeek Launches V4 Pro Model with Open Agent Tools and Higher API Rates (AllBlogThings)](https://www.allblogthings.com/2026/08/deepseek-launches-v4-pro-model-with-open-agent-tools-and-higher-api-rates.html)
- [DeepSeek ships improved V4 Pro, open-sources its agent software, and raises API prices (The Decoder)](https://the-decoder.com/deepseek-launches-an-improved-v4-pro-model-raises-api-prices-and-makes-its-agent-software-open-source/)
- [DeepSeek-V4-Pro GA Release (DeepSeek API Docs)](https://api-docs.deepseek.com/news/news260813/)
- [DeepSeek V4 Pro Leaves Preview With Agent Gains (Technology.org)](https://www.technology.org/2026/08/14/deepseek-v4-pro-official-release-agent-benchmarks/)
- [DeepSeek V4 Pro 0813 (max) — Intelligence, Performance & Price Analysis (Artificial Analysis)](https://artificialanalysis.ai/models/deepseek-v4-pro)

---

## Audio script
วันที่ 13 สิงหาคม DeepSeek ปล่อย V4-Pro 0813 ออก general availability พร้อมเรื่องที่ทำให้ทั้งวงการ open-source ต้องหยุดอ่านซ้ำ — เขา open-source ตัว agent runtime ของตัวเองชื่อ DeepSeek Harness v0.1 บน GitHub ภายใต้ MIT license ครั้งแรกที่ frontier lab ตัวใหญ่ ship ทั้งโมเดลและ agent framework มาด้วยกัน ไม่ใช่แค่ปล่อย weight แล้วให้ community เขียน harness เองแบบ Llama หรือ Mistral

ตัวเลขที่ทำให้ต้องจริงจัง 1.6 trillion parameter mixture of experts, active per token แค่ 49 billion, context 1 million token, generate output ได้สูงสุด 384,000 token ต่อ request คะแนน Artificial Analysis Intelligence Index อยู่ที่ 53 สูงกว่าค่ากลาง open-weights กว่าเท่าตัว และที่ tempting สำหรับ dev คือ API compatible กับ OpenAI Responses API format ทันที swap DeepSeek แทน GPT ในโค้ดเดิมได้เลย ไม่ต้อง refactor

แต่วันนี้ 16 สิงหาคม 16:00 UTC ราคา API ขึ้นทันที output token จาก 87 เซ็นต์ต่อล้าน เป็น 3.96 ดอลลาร์ต่อล้านช่วง peak เพิ่ม 4.5 เท่า แม้กระนั้นก็ยังถูกกว่า Anthropic Fable 5 ที่ 50 ดอลลาร์ต่อล้าน ประมาณ 12 เท่า สัญญาณคือ DeepSeek พยายามเก็บ revenue จาก agent workload ที่ token consumption สูง ก่อนที่รอบ commoditize ครั้งต่อไปจะมา

ทำไมสำคัญ pattern ที่ 3 อย่าง หนึ่ง model บวก harness bundle กำลังจะเป็น default ใหม่ รอ Anthropic กับ Google ตอบภายในไตรมาส 4 สอง OpenAI Responses API กำลังกลายเป็น interface standard ของวงการ ไม่ใช่ Chat Completions อีกต่อไป สาม โมเดล agent-tuned จะแซง general-purpose ในตลาด mid-tier ตลาดจะแยกเป็น agentic tier กับ chat tier ชัดเจน

สำหรับ builder ที่สร้าง framework ต้องคิดจริงจังว่าจะ fork DeepSeek Harness หรืออยู่กับ LangGraph CrewAI ต่อ MIT license ใช้ commercial ได้เต็ม และ codebase มาจาก team ที่เข้าใจ behavior ของโมเดลลึกที่สุด สำหรับ business ที่ deploy agent ต้อง benchmark quality-adjusted cost per successful task ไม่ใช่ราคาต่อ token ก่อน migrate ครับ
