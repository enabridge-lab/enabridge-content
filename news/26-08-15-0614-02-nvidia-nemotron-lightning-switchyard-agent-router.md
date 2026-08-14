---
date: 2026-08-15
slug: nvidia-nemotron-lightning-switchyard-agent-router
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  Editorial isometric illustration of a giant train switchyard from above,
  but the trains are glowing model tokens routed between three tracks
  labeled "OPUS 4.8", "NEMOTRON LIGHTNING 30B", "GPT-5". A brass cost meter
  in the foreground reads "COST 100% → 33%" with a green downward arrow. An
  NVIDIA logo pennant top right. Editorial magazine style, thick outlines,
  high contrast, 1:1 aspect, no real human faces, readable at 200px
  thumbnail.
image: images/26-08-15-0614-02-nvidia-nemotron-lightning-switchyard-agent-router.png
---

# NVIDIA เปิด NeMo Switchyard เป็น open source — router ที่กด cost agent เหลือ 1 ใน 3, Cognition/Ramp/Boomi deploy แล้ว

## TL;DR
- NVIDIA ปล่อย **Nemotron 3.5 Lightning** (30B MoE, active แค่ 3B params, เร็ว **4x** เทียบ dense 30B) พร้อม **NeMo Switchyard** — open source model router สำหรับ agent workload บน GitHub
- Switchyard **cuts task cost เหลือ ~1 ใน 3** เทียบรัน Opus 4.8 อย่างเดียว โดย route แต่ละ step ไป model ที่ถูกที่สุดที่ทำได้
- Deploy จริงแล้ว: **Cognition -28% cost, Ramp -58% cost + -33% runtime, Boomi 100% domain-routing accuracy** — เป็น commodity layer ที่ทำให้ vendor lock-in บน frontier model เริ่มไม่คุ้ม

## เกิดอะไรขึ้น
วันที่ 11 สิงหาคม 2026 NVIDIA ปล่อย 2 asset พร้อมกันที่จะเปลี่ยน economic ของ agent stack: **Nemotron 3.5 Lightning** และ **NeMo Switchyard** — ตัวหนึ่งเป็น model, อีกตัวเป็น router ที่ open source เต็มตัวบน GitHub

Nemotron 3.5 Lightning คือ mixture-of-experts model 30B parameters ที่ **active แค่ 3B params ต่อ inference step** — architecture นี้ทำให้ output speed เร็วขึ้น 4 เท่าเทียบ dense 30B รุ่นเดียวกัน NVIDIA ตั้ง target ชัดว่านี่คือ model สำหรับ **execution layer ของ long-running agent** ไม่ใช่ frontier reasoning — คือ workload ที่ต้อง run หลายพัน step ซ้ำ ๆ ที่ต้อง latency ต่ำและ cost ต่ำมาก

แต่ตัวจริงที่ทำให้ทุกคนตื่นคือ **NeMo Switchyard** — open source library ที่ route แต่ละ step ของ agent workflow ไป model ที่เหมาะที่สุด (จาก provider ใดก็ได้ — Anthropic, OpenAI, Google, Nemotron, self-hosted OSS) โดย **preserving OpenAI + Anthropic API compatibility** = developer ไม่ต้อง rewrite application ตัวเลข benchmark ของ NVIDIA เอง — **cuts task cost เหลือ ~33% ของการรัน Claude Opus 4.8 อย่างเดียว** โดยที่ task success rate ยังเทียบเท่า

Real-world deployment ที่ NVIDIA เปิดเผยเป็นสิ่งที่ทำให้ story นี้ไม่ใช่แค่ benchmark: **Cognition** (บริษัทเจ้าของ Devin + Windsurf) **cut cost 28%** ในการรัน Devin agent, **Ramp** (spend management SaaS) **cut cost 58% + runtime 33%** ในการรัน finance workflow agent, และ **Boomi** (integration platform) hit **100% domain-routing accuracy** สำหรับ agent workflow ในโดเมนธุรกิจของตัวเอง — ทั้ง 3 บริษัทเป็น flagship agent customer ที่ vendor frontier ทุกเจ้าอยากได้

## ทำไมสำคัญ
Switchyard เป็นสัญญาณว่า **agent inference economics กำลังจะกลายเป็น commodity** — จุดที่ industry ได้ผ่านมาแล้วในทุก wave (compute → cloud → CDN → search) ที่ margin ย้ายจาก provider ไป orchestrator เมื่อลูกค้ามีทางเลือกที่ swap ได้ realtime ตอนนี้ agent builder ไม่ต้องเลือกระหว่าง Anthropic หรือ OpenAI ตอน design time อีกต่อไป — เขียน 1 ครั้ง แล้ว router ตัดสินใจตอน runtime ว่า step นี้ให้ใครทำ

Pattern น่าสนใจ 2 อย่าง: หนึ่ง — **NVIDIA เข้าเกม routing** ไม่ใช่แค่ขาย GPU แสดงว่าเขาเห็นว่า agent orchestration layer จะกลายเป็น value capture ใหม่ที่ไม่ใช่ hardware ล้วน สอง — **open source แบบเต็มตัวบน GitHub** เป็นการวาง Switchyard เป็น de facto standard ตัดหน้า proprietary router (LiteLLM, OpenRouter, Portkey, Vercel AI Gateway) ทำให้ vendor เหล่านี้ต้อง reprice หรือ pivot ไป enterprise features (audit, PII redaction, cost allocation)

Signal ที่ต้องดู: **frontier lab จะตอบยังไง** — Anthropic ที่เพิ่งขึ้นราคา Sonnet 5 เป็น $3/M output token 31 ส.ค. จะเริ่มเจอ pressure จาก builder ที่ route ไป Nemotron Lightning สำหรับ step ที่ไม่ต้อง reasoning หนัก และ OpenAI ที่เตรียม IPO จะต้อง justify ทำไม customer ยังต้องล็อคกับ platform ตัวเดียว signal ถัดไปจะเห็นภายใน 6 เดือน — เมื่อ Switchyard usage stats แสดงว่า agent step ที่ทำงานจริงบน frontier model เหลือแค่ 20-30% ของ total workload

## มุม AI Agent Platform
**Builders** ที่สร้าง agent: ต้องลอง Switchyard ในสัปดาห์นี้ — API compatible กับ OpenAI/Anthropic แปลว่า swap แค่ base_url + api_key ก็ทดสอบได้ ถ้า cost cut 30-50% ก็มีเรื่อง P&L เข้า Q4 planning ทันที และถ้า framework ของคุณยังผูก hardcode กับ Anthropic/OpenAI SDK = ควร wrap ผ่าน router pattern ก่อน customer ถามเอง

**Users / business** ที่ deploy agent: ถ้า agent workflow ของคุณอยู่บน Claude/GPT-5 อย่างเดียวและมี **inference bill > $50K/เดือน** = Switchyard คือ ROI ในหน่วยสัปดาห์ ไม่ใช่เดือน คู่กับ observability tool (LangSmith, Arize) เพื่อวัดว่า routing decision กระทบ output quality แค่ไหน — โดยเฉพาะ regulated industry (finance, healthcare) ที่ audit trail สำคัญกว่า cost saving

**Ecosystem**: คนที่ได้ประโยชน์ = **open-source model vendor** (DeepSeek, Qwen, Mistral, Nemotron itself), **cloud provider ที่ host OSS** (Together, Fireworks, Modal, Replicate, Baseten), **observability layer** ที่ต้อง track cross-model behavior คนที่เสีย = router startup ที่เก็บเงิน (LiteLLM, OpenRouter จะต้อง pivot ไป enterprise features), **frontier lab** ที่ต้องขายด้วย feature ไม่ใช่ lock-in อีกต่อไป

## Sources
- [NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard (NVIDIA Blog)](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/)
- [Nvidia releases Nemotron 3.5 Lightning and NeMo Switchyard (SiliconANGLE)](https://siliconangle.com/2026/08/11/nvidia-releases-nemotron-3-5-lightning-nemo-switchyard-give-enterprise-ai-capability-options/)
- [NVIDIA-NeMo/Switchyard on GitHub](https://github.com/NVIDIA-NeMo/Switchyard)
- [Nvidia's Switchyard cuts AI agent costs (VentureBeat)](https://venturebeat.com/orchestration/nvidias-switchyard-router-reshuffles-ai-models-mid-task-cutting-task-costs-to-a-third-in-its-own-tests)

---

## Audio script
เมื่อวันที่ 11 สิงหาคม NVIDIA ปล่อย 2 asset พร้อมกันที่จะเปลี่ยน economic ของ agent stack ตัวแรกคือ Nemotron 3.5 Lightning เป็น mixture-of-experts model 30 billion parameters ที่ active แค่ 3 billion ต่อ inference step ทำให้เร็วขึ้น 4 เท่าเทียบ dense model รุ่นเดียวกัน ตั้ง target สำหรับ execution layer ของ long-running agent ไม่ใช่ frontier reasoning

ตัวจริงที่ทำให้ทุกคนตื่นคือ NeMo Switchyard เป็น open source library บน GitHub ที่ route แต่ละ step ของ agent workflow ไป model ที่เหมาะที่สุดจาก provider ใดก็ได้ ไม่ว่าจะเป็น Anthropic, OpenAI, Google หรือ Nemotron โดย preserve API compatibility ทำให้ developer ไม่ต้อง rewrite application ตัวเลข benchmark ของ NVIDIA เอง cut task cost เหลือประมาณ 1 ใน 3 ของการรัน Claude Opus 4.8 อย่างเดียว

Real-world deployment ที่ NVIDIA เปิดเผยคือ Cognition ที่รัน Devin agent cut cost 28 เปอร์เซ็นต์ Ramp cut cost 58 เปอร์เซ็นต์และ runtime 33 เปอร์เซ็นต์ในการรัน finance workflow และ Boomi hit 100 เปอร์เซ็นต์ domain routing accuracy

ทำไมสำคัญ Switchyard เป็นสัญญาณว่า agent inference economics กำลังจะเป็น commodity เหมือนที่เคยเกิดกับ compute cloud CDN และ search value capture จะย้ายจาก provider ไป orchestrator ตอนนี้ agent builder ไม่ต้องเลือกระหว่าง Anthropic หรือ OpenAI ตอน design time อีกต่อไป เขียน 1 ครั้งแล้ว router ตัดสินใจตอน runtime ว่า step นี้ใครทำ

สำหรับ builder ต้องลอง Switchyard สัปดาห์นี้ swap แค่ base URL กับ API key ก็ทดสอบได้ สำหรับ business ที่มี inference bill เกิน 5 หมื่นดอลลาร์ต่อเดือน นี่คือ ROI ในหน่วยสัปดาห์ไม่ใช่เดือนครับ
