---
date: 2026-10-23
slug: moonshot-kimi-k31-pro-open-weights
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a Chinese open-weight model crate
  labeled "KIMI K3.1 PRO" sitting on a terminal benchmark leaderboard. On top
  of the crate glow three stacked numbers: "65.7% TERMINAL-BENCH 4.0",
  "2.8T / 104B MoE", "1M CONTEXT". Below the crate, a leaderboard shows:
  "CLAUDE OPUS 5.5 — 66.4%", "KIMI K3.1 PRO — 65.7%", "GPT-6 ASTRA — 58.2%".
  A countdown ribbon reads "OPEN WEIGHTS — NOV 4". A small moon icon marks
  the Moonshot logo. Deep navy, amber, and jade palette, strong contrast for
  200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-25-0605-04-moonshot-kimi-k31-pro-open-weights.png
---

# Moonshot ปล่อย Kimi K3.1 Pro — open-weight ที่ตาม Claude Opus 5.5 ห่าง 0.7 แต้ม + 1M context, เปิด weights 4 พ.ย.

## TL;DR
- **23 ต.ค.** Moonshot AI ปล่อย **Kimi K3.1 Pro** — MoE **2.8T total / 104B active parameter**, **1M-token context**, Terminal-Bench 4.0 ที่ **65.7%** (Moonshot report; Artificial Analysis อิสระวัดได้ 67%)
- Benchmark เทียบ: **Claude Opus 5.5 66.4%, Kimi K3.1 Pro 65.7%, GPT-6 Astra 58.2%** บน Terminal-Bench 4.0 (coding benchmark)
- **Open weights สัญญาปล่อย 4 พ.ย.** (ยังไม่ประกาศ license ชัด); ก่อนนั้นใช้ได้ผ่าน **Kimi apps, Kimi Work, Kimi Code, Kimi API**
- Signal: open-weight frontier **ตามหลัง closed Claude แค่ไม่ถึงหนึ่งแต้ม** — Replit → OpenAI switch (ดูข่าว 02) จะเจอ **tier ที่สาม**: self-hosted open ภายในสองไตรมาส

## เกิดอะไรขึ้น

วันพฤหัสที่ **23 ต.ค.** Moonshot AI (บริษัท AI ของจีนที่ Alibaba ลงทุน) ปล่อย **Kimi K3.1 Pro** — generation ใหม่ของ model line ที่เริ่มสร้างแรงกระเพื่อมตั้งแต่ K2 เมื่อต้นปี 2026. architecture เป็น **Mixture-of-Experts** ขนาด **2.8 ล้านล้าน parameter รวม / 104 พันล้าน active ต่อ token**. **context window 1 ล้าน token** ไม่ใช่เรื่องใหม่ (Gemini 2.5 ทำได้ก่อน) แต่สำหรับ open-weight model นี่คือ **largest ที่เคยปล่อย**

benchmark heading คือ **Terminal-Bench 4.0** — ชุด test ที่ประเมิน coding agent บน task ที่ต้องใช้ shell + file system จริง: K3.1 Pro ทำได้ **65.7%** ตาม Moonshot. **Artificial Analysis** (benchmark aggregator อิสระ) วัดได้ **67%** ซึ่งทำให้มันเป็น **"the highest score of any model"** ใน snapshot ของ Artificial Analysis. เทียบ: **Claude Opus 5.5 66.4%, GPT-6 Astra 58.2%, Kimi K3 (รุ่นก่อน) 13%**. gap จาก Kimi K3 → K3.1 Pro คือ **จาก 13% เป็น 65.7% ใน generation เดียว** — pace ที่ไม่มี closed lab ไหนไกล้

ตัว weight **ยังไม่ปล่อย**. Moonshot สัญญาว่าจะ **publish full model weights 4 พ.ย.** พร้อม license ที่ "ยังไม่ประกาศ" (K2 ปล่อยเป็น modified Apache พร้อม usage restriction, น่าจะคล้ายกัน). ก่อนนั้นเข้าใช้ผ่าน **Kimi mobile app, Kimi Work (enterprise), Kimi Code (coding agent), Kimi API** — ซึ่ง pricing report ไม่ชัด แต่ community ชี้ไปที่ **~1/3 ของ Claude Opus 5.5** ต่อ token

ที่ Moonshot เน้นในการ release คือ **cyber capability**: K3.1 Pro ถูก **prune ความสามารถ hacking ลงมาที่ ~81%** (จาก baseline ~100% ที่ K3) — ที่ผิดปกติเพราะ Moonshot เป็นหนึ่งใน lab แรก ๆ ที่พูดเปิดว่า **ตัดฟีเจอร์โดยเจตนา** ก่อนปล่อย

## ทำไมสำคัญ

จุดที่หนึ่ง — **open-weight ไล่กวด closed frontier ภายใน 0.7 แต้ม**. เมื่อปี 2024 ช่องว่าง open-weight best (Llama 405B) กับ closed frontier best (Claude 3.5 Opus) อยู่ที่ **15–20 point** บน SWE-Bench. ภายใน 24 เดือน gap หดลงเหลือ **~1 point** บน Terminal-Bench 4.0. ถ้า trend ต่อ, **Q2 2027 open-weight จะเท่าหรือเกิน closed frontier** — ซึ่งเปลี่ยน business model ของ Anthropic/OpenAI อย่างสิ้นเชิง

จุดที่สอง — **จีน produce open-weight frontier เร็วกว่าสหรัฐ**. Kimi (Moonshot), Qwen 3.5 (Alibaba), DeepSeek V4, Hunyuan Turbo (Tencent) — ทั้งหมดนี้ open-weight และ performance อยู่ใน tier เดียวกับ Claude/GPT. US open-weight (Llama 4 ของ Meta, Grok Open ของ xAI) ยังตามหลัง 2–3 generation. US regulator คุม export compute ไปจีน แต่**ไม่ได้คุม open-weight ที่จีนปล่อยออกมา** — ซึ่งจะ reshuffle leverage ของ US frontier lab ใน procurement ของประเทศอื่น

จุดที่สาม — **pattern ของ Replit → OpenAI switch (ดูข่าว 02) จะทำซ้ำกับ open-weight**. ภายในสองไตรมาสคาด: บริษัทที่ **spend $10M+/ปี กับ foundation model** จะเริ่ม evaluate **self-hosted Kimi K3.1 Pro / Qwen 3.5** เทียบ closed frontier. ถ้า perform within 2–3 points และ compute cost ลด 60–70% enterprise CFO จะกด switch. Portkey, Not Diamond, OpenRouter — ที่เป็น "router" layer ตามข่าว 02 — จะเริ่ม route มา self-hosted automatically

## มุม AI Agent Platform

สำหรับ **Builders** (ของ agent framework/coding assistant): **อย่าสมมติว่า closed frontier คือ default long-term**. Framework ที่ build on top ของ API ของ Anthropic/OpenAI โดยไม่คิด Kimi/Qwen/DeepSeek เป็น substitute จะเสียเปรียบใน procurement. **เริ่ม plan model router + benchmark harness ที่ compare open vs closed ของตัวเองวันนี้** — ไม่ใช่ตอนที่ customer ขอ

สำหรับ **Users / Business**: ถ้า cost of AI กินงบ R&D หรือ margin > 2–3% — **เริ่ม pilot self-hosted open weight**. ตัวเลือกตอนนี้ไม่น้อย: Nous Hermes ($90M Series B 7 ต.ค.), Kimi K3.1 Pro (4 พ.ย.), Qwen 3.5. GPU ที่ host ต้องการใช้ **H200/B200/MI400** — cost อยู่ที่ **$2–5/hour per GPU** ใน hyperscaler, สำหรับ 70% utilization = $12–30K/เดือนต่อ 8-GPU node ซึ่งน้อยกว่า token spend ของบริษัทที่ 1,000+ heavy user

สำหรับ **Ecosystem**: Hugging Face, Replicate, Together, Groq, Cerebras — ที่ host open-weight model — จะเจอ demand surge ตั้งแต่ 4 พ.ย. ที่ K3.1 Pro ปล่อย weight. Nvidia (ตั้งแต่ GTC Berlin 21 ต.ค. ที่ปล่อย Nemotron 3.5 Super VL 120B) ขับเคลื่อน open-weight infrastructure อย่างชัดเจน. ส่วน Anthropic/OpenAI ต้อง **ชัดใจว่า value proposition long-term คือ "frontier capability + safety primitive"** (ดูข่าว 03 sandbox-runtime) ไม่ใช่ "token margin"

## Sources
- [Moonshot AI Releases Kimi K3.1 Pro: 2.8T/104B MoE (MarkTechPost)](https://www.marktechpost.com/2026/10/23/moonshot-ai-kimi-k3-1-pro-open-weight-model/)
- [Kimi K3.1 Pro launches at 4th on Intelligence Index (Artificial Analysis)](https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks)
- [Moonshot releases Kimi K3.1 Pro and says it cut its hacking skills (The Next Web)](https://thenextweb.com/news/moonshot-kimi-k3-1-pro-open-weight-cyber)

---

## Audio script
วันพฤหัส 23 ตุลาคม Moonshot AI บริษัท AI ของจีนที่ Alibaba ลงทุน ปล่อย Kimi K3.1 Pro architecture แบบ Mixture of Experts ขนาด 2.8 ล้านล้าน parameter รวม 104 พันล้าน active ต่อ token มี context window 1 ล้าน token ซึ่งเป็น largest ที่ open weight ไหนเคยปล่อย. บนชุด test Terminal Bench 4.0 Moonshot report ได้ 65.7 เปอร์เซ็นต์ Artificial Analysis วัดอิสระได้ 67 เปอร์เซ็นต์ซึ่งทำให้เป็นคะแนนสูงที่สุดใน snapshot. เทียบคู่แข่ง Claude Opus 5.5 ได้ 66.4 GPT 6 Astra 58.2 รุ่นก่อน Kimi K3 แค่ 13 — gap generation เดียวจาก 13 เป็น 65.7 pace ที่ไม่มี closed lab ไหนไกล้. Weight ยังไม่ปล่อยแต่ Moonshot สัญญาว่าจะ publish full weights 4 พฤศจิกายน. ก่อนนั้นใช้ผ่าน Kimi apps, Kimi Work, Kimi Code, Kimi API ที่ community ชี้ว่าราคาราวหนึ่งในสามของ Claude Opus. ที่ Moonshot เน้นในการ release คือการ prune ความสามารถ hacking ลงมาที่ประมาณ 81 เปอร์เซ็นต์จาก baseline ของ K3 — ผิดปกติเพราะพูดเปิดว่าตัดฟีเจอร์โดยเจตนา. ความสำคัญสามประเด็น หนึ่ง open weight ไล่กวด closed frontier ภายใน 0.7 แต้ม จาก gap 15 ถึง 20 point เมื่อปี 2024. ถ้า trend ต่อ Q2 2027 open weight จะเท่าหรือเกิน closed frontier. สอง จีน produce open weight frontier เร็วกว่าสหรัฐอย่างชัดเจน — Kimi Qwen DeepSeek Hunyuan ทั้งหมด open weight ขณะ Llama 4 กับ Grok Open ของสหรัฐตามหลัง 2 ถึง 3 generation. สาม pattern ของ Replit ไป OpenAI จะทำซ้ำกับ open weight — บริษัทที่ spend เกิน 10 ล้านดอลลาร์ต่อปี กับ foundation model จะเริ่ม evaluate self hosted ภายในสองไตรมาส. สำหรับคน build agent framework อย่าสมมติว่า closed frontier คือ default long term เริ่ม plan model router และ benchmark harness ที่ compare open vs closed วันนี้. สำหรับ enterprise ที่ cost of AI กินงบ R&D หรือ margin เกิน 2 ถึง 3 เปอร์เซ็นต์ เริ่ม pilot self hosted — ตัวเลือกมีทั้ง Nous Hermes, Kimi K3.1 Pro, Qwen 3.5. และ Anthropic กับ OpenAI ต้องชัดใจว่า value proposition long term คือ frontier capability บวก safety primitive ไม่ใช่ token margin
