---
date: 2026-09-06
slug: anthropic-fable-51-cache-cost-75-percent-agent-economics
topic: agentic-ai
reading_time_min: 5
sources: 3
image_prompt: |
  A dramatic price tag scene: an oversized "$1.00" tag on the left, slashed through
  with a red X, an oversized "$0.25" tag on the right glowing gold, arrow between
  them labeled "-75% CACHE READ". Behind: a stack of glowing books labeled
  "1M TOKENS CONTEXT" and a spinning gear labeled "AGENTIC LOOP". Anthropic
  wordmark faintly visible on the right tag. Editorial isometric style, deep
  charcoal background, gold and crimson accents for high thumbnail contrast,
  1:1 aspect, no real human faces.
image: images/26-09-06-0609-02-anthropic-fable-51-cache-cost-75-percent-agent-economics.png
---

# Anthropic ตัดราคา Fable 5.1 cache read 75% เหลือ $0.25/M token — agent workload หนัก ๆ ประหยัดจริงถึง 45%, unit economics เปลี่ยนโครงสร้าง

## TL;DR
- Anthropic ปล่อย **Claude Fable 5.1 + Mythos 5.1** เมื่อ 1 ก.ย. 2026 — pricing shift ที่สำคัญที่สุดคือ **cache read ลดจาก $1.00 → $0.25 per million tokens (75% cut)**, base I/O อยู่ที่ $10/$50 per million tokens เท่าเดิม
- Context window 1M tokens, output cap 128K tokens per response; Anthropic ประมาณว่า typical workload ประหยัด ~25%, agentic workload ที่ใช้ cache หนัก ประหยัด **~45%**
- Signal: **agent unit economics เปลี่ยนโครงสร้าง** — คนที่ออกแบบ agent loop รอบยาว ๆ (multi-turn, tool-heavy, long-context) จะได้ประโยชน์เต็ม; middleware ที่ inject context ซ้ำ ๆ ต้อง redesign; MCP server ที่ pipe large context เข้าทุก turn จะกลายเป็น cost driver ที่มองเห็น

## เกิดอะไรขึ้น

Anthropic ปล่อย Claude Fable 5.1 และ Mythos 5.1 เมื่อ 1 ก.ย. 2026 — เป็น incremental release บน Fable 5/Mythos 5 platform เดิม. Headline feature ที่ทุก builder จับตาคือ **cache read pricing ที่ลดจาก $1.00 ต่อ 1 ล้าน token เหลือ $0.25** — cut 75% ในคราวเดียว, ซึ่งเป็นการปรับที่ใหญ่ที่สุดใน pricing history ของ Anthropic. Base input ยังอยู่ที่ $10/M, base output $50/M — ราคาเท่าเดิมกับ Fable 5 pubished tier — และ context window ยัง 1M tokens, output cap 128K per response.

Model ตัวเองก็ upgrade — benchmark ใหม่ที่ Anthropic ปล่อยระบุว่า Fable 5.1 ทำ Terminal-Bench-Science 52.6% (SOTA), improved reasoning + tool-use consistency, และ Mythos 5.1 ยังคงเป็น restricted-access variant สำหรับ vetted cybersecurity + life sciences organizations ที่ต้องการ capability ที่ปกติถูก safeguard บล็อก. แต่สิ่งที่จะเปลี่ยน landscape ของ agent builder จริง ๆ ไม่ใช่ benchmark — เป็น pricing.

Anthropic ประมาณว่าผลกระทบสุทธิต่อ typical workload อยู่ที่ประมาณ **25% ถูกลง** แต่ workload ที่ heavily agentic — พวกที่ input มาจาก cache เป็นส่วนใหญ่ (long system prompt, MCP tool schemas, retrieved documents, conversation history) — จะประหยัดได้ถึง **45%**. VentureBeat และ Latent Space รายงานตรงกันว่ามี trade-off ซ่อนอยู่ — output tokens อาจโตขึ้น ~70% ต่อ response (เพราะ Fable 5.1 verbose มากขึ้นในบาง reasoning task) และ **prompt cache API เปลี่ยน 3 pattern** ที่ developer เคยพึ่งพา — พวกที่ hardcode cache breakpoint ไว้แบบเดิมต้อง refactor.

## ทำไมสำคัญ

Pattern ที่ควรอ่านออกคือ Anthropic กำลัง **subsidize agentic workload อย่างชัดเจน** — ไม่ใช่ price war ทั่วไป. คิดง่าย ๆ: agent loop ตัวเดียวที่ทำงาน 30 turn, มี system prompt 20K token + tool schema 15K + retrieval context 40K + conversation history โตขึ้นเรื่อย ๆ — ทุก turn ที่ 2 เป็นต้นไป input 95% มาจาก cache. ก่อนหน้านี้ที่ $1/M คุณจ่าย ~$0.075 ต่อ turn แค่ cache read; ตอนนี้เหลือ ~$0.019 — 4 เท่า cheaper. ในสเกล enterprise ที่มี agent รัน 10,000 loop ต่อวัน ตัวเลขนี้แปลว่า **cost per agent-day ลดจาก ~$750 → ~$190 ในคำนวณ compute อย่างเดียว** — ยังไม่นับ output tokens.

ผลข้างเคียงที่สำคัญ: **middleware layer ที่ inject context ซ้ำโดยไม่ใช้ cache** จะกลายเป็น cost driver ที่ visible ทันที. ก่อนหน้านี้ทีม engineering อาจ tolerate abstraction ที่ inefficient เพราะ marginal cost หลบอยู่หลัง input pricing; ตอนนี้ที่ cache read ถูกกว่า input read **40 เท่า** (0.25 vs 10), การไม่ hit cache = burning money. ทีมที่ใช้ LangChain / LlamaIndex / crewAI จะต้อง audit context pipeline อย่างเข้มงวด — abstraction ที่รบกวน caching (dynamic system prompt injection, tool description shuffle) จะโดน pressure เปลี่ยนหรือถูก bypass ตรง.

ในระดับ strategic: Anthropic ส่งสัญญาณว่า **agentic use case = strategic priority** และพร้อมยอมเสียมาร์จินระยะสั้นเพื่อ lock ใน long context loop ที่ competitor tap ไม่ได้ง่าย. OpenAI GPT-6 Astra ที่ปล่อย 3 ก.ย. มี context 512K + response cache ที่ราคาสูงกว่า, Gemini 3.8 Flash เน้น latency ราคาถูกแต่ context 200K. ถ้าคุณสร้าง agent ที่ต้องเก็บ state ยาว ๆ, tool call เยอะ, RAG หนัก — Fable 5.1 กลายเป็น default choice ในทาง economics โดย skew ที่ชัดกว่าไตรมาสก่อนมาก.

## มุม AI Agent Platform

**Builders** — audit agent architecture วันนี้ตอบ 3 คำถาม: (1) system prompt คุณ static หรือ dynamic — ถ้า dynamic เพราะ personalization ให้ dedupe แล้ว cache ส่วน common; (2) MCP tool schemas มี stable ordering ไหม (order เปลี่ยน = cache miss); (3) conversation history rotation strategy คุณ preserve prefix เพื่อ cache hit ต่อเนื่องได้แค่ไหน. คน rebuild pipeline ให้ cache-friendly ในเดือน ก.ย. นี้จะเห็น cost drop 40% ทันที.

**Users / Business** — CFO / CTO ที่กำลัง commit agent budget 2027 — revise assumption ใหม่. เดิม 1 agent seat = $X/month based on average token cost; ตอนนี้ที่ Fable 5.1 pricing seat-based agent pricing (แบบ xAI Grok Bot $120-300/seat ที่ประกาศเมื่อวานซืน) จะมี margin room เพิ่ม 25-45% — คาดว่าจะเห็น vendor ลดราคา seat หรือเพิ่ม tool budget ให้ user ในไตรมาสหน้า.

**Ecosystem** — สำหรับ OpenAI + Google: pressure ตัดราคา cache read มาก่อนสิ้นปี — GPT-5 mini กับ Gemini 2.5 flash ที่ราคา cache read $0.075-0.15/M อยู่แล้วยัง OK แต่ frontier tier (GPT-6 Astra, Gemini 3.8 Pro) จะโดน ราคา cache สูง $0.60-1.20/M. สำหรับ inference infrastructure vendor (Baseten, Fireworks, Together): pricing arbitrage window ระหว่าง Anthropic direct vs deployed variant แคบลง — value shift ไปที่ latency, region, compliance แทน.

## Sources
- [Anthropic's Claude Fable 5.1 and Mythos 5.1 arrive with a 75% cost reduction for Fable cache reads (VentureBeat)](https://venturebeat.com/technology/anthropics-claude-fable-5-1-and-mythos-5-1-arrive-with-a-75-cost-reduction-for-fable-cache-reads)
- [Anthropic Releases Claude Fable 5.1 and Claude Mythos 5.1: 52.6% on Terminal-Bench-Science and 75% Cheaper Cache Reads (MarkTechPost)](https://www.marktechpost.com/2026/09/01/anthropic-releases-claude-fable-5-1-and-claude-mythos-5-1-52-6-on-terminal-bench-science-and-75-cheaper-cache-reads/)
- [Anthropic Cuts Fable 5.1 Cache Reads 75% to $0.25/M — and Breaks Three Prompt Patterns Developers Rely On (AI Unfiltered)](https://www.arturmarkus.com/anthropic-cuts-fable-5-1-cache-reads-75-to-0-25-m-and-breaks-three-prompt-patterns-developers-rely-on/)

---

## Audio script
Anthropic เพิ่งปล่อย Claude Fable 5.1 กับ Mythos 5.1 อาทิตย์นี้ headline ที่ agent builder ทุกคนต้องอ่าน ราคา cache read ลดจากดอลลาร์ต่อล้าน token เหลือ 25 cent ตัดไป 75% ในคราวเดียว base input output ยังเท่าเดิม context ยัง 1 ล้าน token ผลกระทบสุทธิ workload ทั่วไปประหยัด 25% แต่ workload ที่ agentic หนัก long system prompt tool schema เยอะ retrieval context ใหญ่ conversation history ยาว จะประหยัดถึง 45% เพราะทุก turn ที่ 2 เป็นต้นไป input 95% มาจาก cache

ในสเกลจริง agent loop รัน 10,000 ครั้งต่อวัน ต้นทุน compute ลดจาก 750 ดอลลาร์เหลือ 190 ดอลลาร์ต่อวัน middleware ที่ inject context ซ้ำโดยไม่ hit cache จะกลายเป็น cost driver ที่มองเห็นทันที เพราะตอนนี้ cache read ถูกกว่า input read 40 เท่า LangChain LlamaIndex crewAI ต้อง audit pipeline ใหม่ builder ที่ rebuild ให้ cache friendly ในเดือนนี้จะเห็น cost drop 40% ทันที ในระดับ strategic Anthropic ส่งสัญญาณชัดว่า agentic use case คือ priority ยอมเสียมาร์จินสั้นๆ เพื่อ lock in long context loop ที่ OpenAI Astra กับ Gemini 3.8 tap ไม่ได้ง่าย คาดว่า OpenAI กับ Google จะตัดราคา cache tier ตามภายในสิ้นปี ครับ
