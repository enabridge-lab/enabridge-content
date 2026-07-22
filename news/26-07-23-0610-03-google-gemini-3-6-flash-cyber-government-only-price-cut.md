---
date: 2026-07-23
slug: google-gemini-3-6-flash-cyber-government-only-price-cut
topic: agent-platform-trend
reading_time_min: 4
sources: 5
image_prompt: |
  A split editorial isometric illustration on a warm off-white background:
  on the left, three price tags stacked — the top tag reads "3.5 FLASH:
  $9.00/M OUT" with a red X, the middle "3.6 FLASH: $7.50/M OUT · -17%
  TOKENS", the bottom "3.5 FLASH-LITE: HIGH-THROUGHPUT". On the right, a
  vault door stamped "3.5 FLASH CYBER" with the label "GOVERNMENT &
  TRUSTED PARTNERS ONLY" and a shield icon. Above both sides a banner
  reads "NO 3.5 PRO — AGAIN". Sharp editorial typography, high contrast,
  1:1 aspect, no real human faces.
image: images/26-07-23-0610-03-google-gemini-3-6-flash-cyber-government-only-price-cut.png
---

# Google ปล่อย Gemini 3.6 Flash + Cyber variant (government-only) — ตัดราคา output 17%, แต่ยังไม่มี 3.5 Pro (ครั้งที่สาม)

## TL;DR
- 21 ก.ค. Google ปล่อย Gemini 3 model ใหม่ในวันเดียว — **3.6 Flash** (mainstream, $7.50/M output ลดจาก $9), **3.5 Flash-Lite** (high-throughput ราคาถูกสุดใน class), **3.5 Flash Cyber** (security-tuned เฉพาะ government + trusted partner)
- Gemini 3.6 Flash ใช้ **output token น้อยลง 17%** เทียบ 3.5 Flash + knowledge cutoff ขยับ Jan 2025 → Mar 2026 + DeepSWE 37% → 49% + OSWorld-Verified 78.4% → 83.0%
- **Gemini 3.5 Pro (flagship) เลื่อน launch เป็นครั้งที่สาม** — ตลาดเริ่มเทียบกับ GPT-5.6 (Luna/Terra/Sol, พ.ค.) และ Claude Sonnet 5 (ก.ค.) ที่ ship ตรงเวลา
- **Flash Cyber** เป็น government-only pilot สำหรับ finding + fixing cybersecurity vulnerability — เดียวกับ trend Anthropic Mythos 5 (100+ trusted US org, 26 มิ.ย.) และ White House voluntary framework ที่จะประกาศก่อน 1 ส.ค.
- Signal: **frontier tier แข่ง cost + speed มากกว่า capability**; specialized-for-government variant กลายเป็น new SKU tier

## เกิดอะไรขึ้น
วันที่ 21 กรกฎาคม Google ปล่อย Gemini model ใหม่พร้อมกัน 3 ตัว — Gemini 3.6 Flash, Gemini 3.5 Flash-Lite, และ Gemini 3.5 Flash Cyber. TechCrunch, 9to5Google, gcn.com, และ Google blog รายงานตรงกัน. รุ่น flagship **Gemini 3.5 Pro** — ที่ทุกฝ่ายรอมาสองไตรมาส — **ไม่ได้ ship อีกครั้ง**, เลื่อนเป็นครั้งที่สามในรอบ 8 เดือน. TechCrunch ตั้งข้อสังเกตว่าโครงสร้างประกาศ (three sub-flagship ในวันเดียว, ไม่มี Pro) ดูเหมือน Google กำลัง buy time เพื่อ finetune Pro ให้แข่งกับ GPT-5.6 Sol ได้.

**Gemini 3.6 Flash** เป็นตัวที่สำคัญที่สุดสำหรับ enterprise agent workload — output pricing ลดจาก $9.00 เหลือ $7.50 ต่อ million token (input คงที่ $1.50), และใช้ output token น้อยลง 17% เทียบ 3.5 Flash (แปลว่า effective cost per task ลดประมาณ 30% เมื่อรวม pricing cut + token efficiency). Knowledge cutoff ขยับจาก January 2025 เป็น March 2026 — สำคัญมากสำหรับ agent ที่ต้องรู้ event ล่าสุด (เช่น regulation update, product launch). Performance improvement ที่ต้องอ่าน: DeepSWE coding benchmark 37% → 49% (+12 point), OSWorld-Verified (computer use / browser agent) 78.4% → 83.0% (+4.6 point). Available บน GitHub Copilot ทันที (GitHub blog post วันเดียวกัน).

**Gemini 3.5 Flash-Lite** เป็น cost-optimized SKU สำหรับ high-throughput workload — retail search, product catalog embedding, low-value automation. ราคายังไม่เปิดเผยเต็ม แต่ Google บอกจะเป็น "most cost-effective in class" — ต่ำกว่า Gemini 3.5 Flash-Lite เดิม + ต่ำกว่า GPT-5.6 Luna + ต่ำกว่า Claude Haiku 5. คู่แข่งหลักที่ถูกล็อกเป้าคือ Anthropic Claude Haiku 5 ที่ commanding retail + support automation ตลาดล่าง.

**Gemini 3.5 Flash Cyber** เป็น SKU ที่แปลกใหม่ที่สุด — fine-tuned สำหรับหาและซ่อม cybersecurity vulnerability, **available เฉพาะ government + trusted partners** ผ่าน limited access pilot program. Pattern ตรงกับ Anthropic Mythos 5 ที่ re-authorize ให้ 100+ trusted US org + federal agency (26 มิ.ย.), และ OpenAI GPT-5.6 Sol preview ที่ให้ government-approved partner (พ.ค.). สามฝ่ายทั้ง Anthropic + OpenAI + Google ตอบสนอง Trump Executive Order 2 มิ.ย. ("Promoting Advanced AI Innovation and Security") ที่ให้ federal agency 30 วัน pre-release review บน "covered frontier models" — voluntary framework ที่ White House จะประกาศก่อน **1 สิงหาคม** (deadline 60 วันจาก EO).

## ทำไมสำคัญ
Pattern สำคัญที่ต้อง track — **frontier model tier แข่ง cost + speed มากกว่า capability**. Google 3.6 Flash ตัดราคา output 17%, Anthropic Sonnet 5 ตัดราคา 25% ตอน launch (ก.ค.), OpenAI GPT-5.6 Terra ตั้ง price ที่ $2/M input ต่ำกว่าที่ตลาดคาด. capability ยัง marginal improvement — DeepSWE +12 point ดูเหมือนก้าวใหญ่ แต่ตลาด enterprise agent มอง cost per successful task + tokens per action มากกว่า benchmark. Anthropic Claude Sonnet 5 ยังนำ agent-specific benchmark (SWE-bench Verified, τ-Bench, MMLU-Pro Reasoning), Google กำลังไล่ด้วย pricing.

**Gemini 3.5 Pro ที่เลื่อนครั้งที่สาม** เป็น signal ที่ contradictory — Google อ้างว่าจะ ship "in coming months" แต่ตลาดเริ่มไม่เชื่อ. TechCrunch ตั้งคำถามว่า Google กำลังมี structural problem หรือแค่ delay ธรรมดา. เทียบกับ OpenAI ที่ ship GPT-5.6 family (Luna/Terra/Sol) พร้อมกัน 3 ตัวใน พ.ค. และ Anthropic ที่ ship Claude Sonnet 5 + Claude Haiku 5 พร้อมกันใน ก.ค. — Google ดูเหมือนพลาด flagship cycle ล่าสุด. Enterprise ที่ evaluate multi-model stack ในไตรมาสนี้จะ default GPT-5.6 Sol + Claude Opus 4.8 + Gemini 3.6 Flash — Gemini Pro slot จะยังเป็น "TBD" อีก 1-2 ไตรมาส.

**Cyber SKU + government-only** เป็น trend structural — frontier lab กำลัง unbundle "public frontier model" กับ "government-approved frontier model" เป็นสอง SKU class. เดือนสิงหาคม White House voluntary framework จะ formalize เรื่องนี้เป็น process — enterprise ที่ทำงานกับ federal agency, defense contractor, critical infrastructure จะต้อง choose "government-approved variant" ในไตรมาสหน้า. ราคา + latency + capability ของ government variant มักต่างจาก public version — vendor procurement team ต้องเตรียม dual-track evaluation.

## มุม AI Agent Platform
สำหรับ **builders** ที่สร้าง agent framework / product — three-fold action item: (1) upgrade default cheap-tier model จาก Gemini 3.5 Flash เป็น 3.6 Flash ทันที (effective cost drop 30% + fresher knowledge + better computer use), (2) architect model routing ให้ swap ระหว่าง Gemini 3.6 Flash / GPT-5.6 Luna / Claude Haiku 5 per task ตาม cost-per-successful-task metric ไม่ใช่ per-token, (3) ถ้า target government + defense + critical infrastructure customer, เริ่มขอ access "government-only" SKU (Anthropic Mythos 5, Google Flash Cyber, OpenAI Sol government preview) วันนี้ — waitlist ยาว.

สำหรับ **users / business** — ถ้าคุณเป็น CIO ที่ evaluate frontier model stack ตอนนี้, default configuration ที่ balanced สำหรับ Q3 2026 คือ: **top-tier reasoning** Claude Opus 4.8 หรือ GPT-5.6 Sol; **agent workhorse** Claude Sonnet 5 หรือ GPT-5.6 Terra; **cost-optimized** Gemini 3.6 Flash หรือ Claude Haiku 5; **specialized cybersecurity** Gemini 3.5 Flash Cyber (ถ้ามี government partnership) หรือ Anthropic Mythos 5. อย่า commit single-vendor stack — hyperscaler เดิมพันหลายทาง, enterprise ต้องเดิมพันหลายทางเหมือนกัน. สำหรับ **ecosystem** — model provider ที่ไม่มี government SKU (xAI Grok, Mistral, Cohere, AI21) จะเสียเปรียบใน federal + defense procurement ไตรมาสหน้า; router product (OpenRouter, Portkey, Kong AI Gateway, LiteLLM) จะได้ประโยชน์เพราะ enterprise ต้อง multi-model routing.

## Sources
- [Google launches Gemini 3.6 Flash and a cybersecurity model with 17% fewer output tokens — GCN (21 Jul)](https://gcn.com/google-launches-gemini-flash-cybersecurity-model/19924/)
- [Google releases three new Gemini models — but no 3.5 Pro — TechCrunch (21 Jul)](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)
- [Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber — Google Blog (21 Jul)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)
- [Google launches Gemini 3.6 Flash and 3.5 Flash-Lite, teases Gemini 4 — 9to5Google (21 Jul)](https://9to5google.com/2026/07/21/gemini-3-6-flash-launch/)
- [Gemini 3.6 Flash is now available in GitHub Copilot — GitHub Changelog (21 Jul)](https://github.blog/changelog/2026-07-21-gemini-3-6-flash-is-now-available-in-github-copilot/)

---

## Audio script
วันนี้ 21 กรกฎาคม Google ปล่อย Gemini model ใหม่ 3 ตัวพร้อมกัน 3.6 Flash 3.5 Flash-Lite และ 3.5 Flash Cyber Flagship Gemini 3.5 Pro ที่ทุกฝ่ายรอมาสองไตรมาสไม่ได้ ship อีกครั้ง เลื่อนเป็นครั้งที่สามใน 8 เดือน 3.6 Flash เป็นตัวสำคัญสุดสำหรับ enterprise agent workload ราคา output ลดจาก 9 ดอลลาร์เหลือ 7.50 ดอลลาร์ต่อ million token ใช้ output token น้อยลง 17 เปอร์เซ็นต์ effective cost per task ลดประมาณ 30 เปอร์เซ็นต์ Knowledge cutoff ขยับจาก มกราคม 2025 เป็นมีนาคม 2026 DeepSWE coding benchmark 37 ขึ้น 49 OSWorld-Verified computer use 78.4 ขึ้น 83 available บน GitHub Copilot ทันที Flash-Lite เป็น cost-optimized SKU สำหรับ high-throughput workload retail search product catalog embedding ล็อกเป้า Anthropic Claude Haiku 5 ที่ commanding retail automation ตลาดล่าง Flash Cyber เป็น SKU แปลกใหม่สุด fine-tuned สำหรับหาและซ่อม cybersecurity vulnerability available เฉพาะ government กับ trusted partner ผ่าน limited pilot Pattern เดียวกับ Anthropic Mythos 5 กับ OpenAI GPT-5.6 Sol government preview สามฝ่ายตอบสนอง Trump Executive Order 2 มิถุนายน ที่ให้ federal agency 30 วัน pre-release review บน covered frontier model voluntary framework จะประกาศก่อน 1 สิงหาคม ทำไมสำคัญครับ Pattern สำคัญคือ frontier model tier แข่ง cost กับ speed มากกว่า capability capability ยัง marginal improvement ตลาด enterprise agent มอง cost per successful task มากกว่า benchmark Gemini 3.5 Pro ที่เลื่อนครั้งที่สามเป็น signal contradictory Google อ้างจะ ship in coming months แต่ตลาดเริ่มไม่เชื่อ enterprise ที่ evaluate multi-model stack ในไตรมาสนี้จะ default GPT-5.6 Sol + Claude Opus 4.8 + Gemini 3.6 Flash Cyber SKU + government-only เป็น trend structural frontier lab กำลัง unbundle public frontier model กับ government-approved frontier model เป็นสอง SKU class enterprise ที่ทำงานกับ federal agency defense contractor critical infrastructure ต้อง choose government variant ในไตรมาสหน้า สำหรับ builder อัพเกรด default cheap-tier model เป็น 3.6 Flash วันนี้ architect model routing ให้ swap ระหว่าง Gemini 3.6 Flash GPT-5.6 Luna Claude Haiku 5 per task สำหรับ CIO อย่า commit single-vendor stack hyperscaler เดิมพันหลายทาง enterprise ต้องเดิมพันหลายทางเหมือนกันครับ
