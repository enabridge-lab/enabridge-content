---
date: 2026-11-01
slug: anthropic-self-eval-watermark-eu-ai-act
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a Claude-logo robot speaking into
  a mirror; the reflection holds up a glowing JSON card reading
  "verdict: safe · 10 tokens". Behind the mirror a second robot stamps
  invisible watermark lines on a scroll labeled "MYTHOS 5, OPUS 4.7,
  OPUS 4.6, SONNET 4.6". Below a calendar page highlights
  "DEC 2 · EU AI ACT". Three stacked numbers glow:
  "78% CATCH @ 1% FP", "16% → 96% RECALL BY MODEL SIZE",
  "WATERMARK LIVE NOV 3". Cream, warm orange and ink-black palette,
  high contrast for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-11-02-0605-05-anthropic-self-eval-watermark-eu-ai-act.png
---

# Anthropic เปิดเลเยอร์ "self-evaluation" + watermark 4 รุ่นก่อน EU AI Act 2 ธ.ค. — governance primitive ย้ายเข้า model

## TL;DR
- Anthropic เปิดใน blog ว่า **newer Claude models มี hidden self-evaluation layer** ที่ output JSON ~10 token ต่อ response ตั้งแต่ **มิ.ย. 2026**
- บน **Claude Fable 5**: ที่ **1% false-positive**, self-eval catch **78% ของ violation** ที่ heavy classifier flag
- Recall scale ตาม model size: **~16% บนรุ่นเล็กสุด → ~96% บนรุ่นใหญ่สุด** — bigger model = better own-judge
- Verdict feed **offline monitoring** ไม่ block real-time response (ยัง)
- **3 พ.ย.**: Text watermark ขยายไป **Mythos 5, Opus 4.7, Opus 4.6, Sonnet 4.6** — ก่อน EU AI Act deadline **2 ธ.ค. 2026**

## เกิดอะไรขึ้น

Anthropic ประกาศผ่าน blog post + X announcement (รายงานผ่านสื่อ 凤凰网科技 1 พ.ย.) ว่า newer Claude models (Fable 5, Opus 4.7, Sonnet 4.6, Mythos 5) **มี hidden "self-evaluation" layer** ที่รันหลัง response ถูก generate แล้ว. layer นี้ไม่ใช่ RLHF ใน training time — เป็น **post-response review** ที่ model ตอบ **~10-token JSON verdict** เกี่ยวกับ response ของตัวเอง ("safe", "violation": [tag]). Anthropic ยืนยันว่า layer นี้ **"running since June 2026"** โดยที่ user ไม่รู้

ตัวเลข performance ที่ Anthropic release:
- **Claude Fable 5**: ที่ **false-positive rate 1%**, self-eval **catch 78% ของ violation ที่ heavy classifier flag**. "Heavy classifier" คือ constitutional classifier ที่ Anthropic ใช้ offline — ซึ่ง compute หนักกว่า self-eval หลาย order ของขนาด
- **Recall scaling** กับ model size: รุ่นเล็กสุด **~16% recall**, รุ่นใหญ่สุด **~96% recall**. แปลว่า bigger model = better own-judge — คล้ายกับ paper research เรื่อง LLM-as-judge แต่คราวนี้เป็น **self-as-judge** scale validate ด้วย production traffic จริง

การใช้งาน: verdict ส่งเข้า **offline monitoring pipeline** ไม่ใช่ real-time guardrail. Anthropic เขียนตรงว่า **"does not block response in real time"** — น่าจะเพื่อประหยัด latency และ compute. ถ้าทำ real-time ต้องเพิ่ม 10 token/response ไปที่ TPS ของทุก inference. ที่น่าสนใจคือ **ไม่ chain เข้า Claude Agent SDK** — คือ layer อยู่บน API gateway ไม่ใช่ layer ของ developer. ลูกค้า API ไม่ได้ control verdict นี้

วันที่ **3 พ.ย. 2026**: Anthropic ขยาย **text watermarking** จากเดิมที่ Fable 5 ตัวเดียว → ครอบ **Mythos 5, Opus 4.7, Opus 4.6, Sonnet 4.6**. Watermark คือ pattern สถิติที่ถูกฝัง token distribution ซึ่ง detector ของ Anthropic สามารถระบุได้ว่า text generate มาจาก Claude. Timeline นี้ **1 เดือนก่อน EU AI Act deadline 2 ธ.ค. 2026** ที่ required general-purpose AI model ต้องมี "machine-readable mark" บน output

## ทำไมสำคัญ

ประเด็นแรก: **Anthropic เป็นเจ้าแรกที่ ship self-evaluation ที่ production scale + release ตัวเลข**. ก่อนหน้านี้มี research จาก OpenAI (constitutional AI, process supervision), DeepMind (self-critique) แต่ยังไม่มีใครประกาศว่า **run on live traffic 5 เดือน + ตัวเลข catch rate 78%**. ตัวเลขนี้สำคัญเพราะเป็น **first ground-truth benchmark** สำหรับ community: ถ้า self-eval 78% recall แล้ว เราไปต่อได้ว่า ensemble ของ self-eval + heavy classifier ควร catch กี่เปอร์เซ็นต์ของ violation

ประเด็นสอง: **recall ที่ scale ตาม model size คือทิศทางของ safety primitive ปี 2027**. ถ้า bigger model = better self-judge แปลว่า safety ไม่ต้องเป็น external classifier อีกต่อไป — model ตัวเองก็เป็น judge ได้ บน assumption ว่า compute budget จะโต. OpenAI, Google, Meta จะ follow pattern นี้. แต่สิ่งที่ **น่ากังวล**: self-judge มีปัญหา circular — model ที่ cheat training ก็ cheat self-eval ได้. Anthropic ไม่ release methodology ว่าแก้ปัญหานี้ยังไง

ประเด็นสาม: **Timeline watermark + EU AI Act คือ compliance play ที่ชัด**. EU AI Act Article 50(2) require GP AI output ต้องมี machine-readable mark ให้ detect ว่า synthetic. Anthropic ขยาย watermark ก่อน **1 เดือน** = ให้ developer + enterprise ทดสอบ detector pipeline ก่อน. OpenAI ประกาศ watermark feature ไปแล้วแต่รายละเอียด rollout ยังไม่ชัดเท่า. Google มี SynthID แต่ focus Gemini vision/audio มากกว่า text. **Anthropic เลือก compete ที่ compliance** — ซึ่งคือ moat ที่ enterprise regulated (banking, insurance, government) จะเลือก

## มุม AI Agent Platform

สำหรับ **builders**: self-eval layer **ไม่ให้ developer เข้าถึง verdict** คือจุดที่ต้องเตือนตัวเอง. ถ้าคุณ build agent บน Claude API คุณ **ไม่สามารถ read verdict ของ self-eval** ได้ — มันคือ internal signal ของ Anthropic. ถ้าต้องการ custom guardrail (ex. domain-specific policy) ยังต้อง chain classifier ของตัวเอง (Prompt Security, Lakera, custom). อย่าสมมติว่า Claude self-eval ครอบ workflow ของคุณ — มันครอบ **Anthropic policy** ไม่ใช่ **business policy**

สำหรับ **business users**: **ตัวเลข 78% catch @ 1% FP คือ reference** ที่ควรใช้ตั้ง SLA กับ vendor อื่น. ถ้า vendor claim guardrail 99% catch — ถามว่า FP rate เท่าไหร่. ถ้า 10% FP ก็ไม่น่ากลัว; ถ้า 0.1% FP ก็ไม่น่าเชื่อ. Anthropic ตั้ง bar ที่ 1% FP / 78% catch — ใช้เป็น benchmark แทนที่จะเชื่อ marketing. สำหรับทีม compliance ที่ต้อง deploy agent บน banking/health/legal: **ask vendor ว่า watermark detector ของเขา ready รึยังก่อน EU AI Act 2 ธ.ค.** — ถ้ายังไม่พร้อม เสี่ยง non-compliance

สำหรับ **ecosystem**: การที่ Anthropic ship self-eval + watermark ก่อน OpenAI/Google ประกาศ production number คือ **soft advantage ใน regulated market**. ปี 2027 bank, insurance, pharma, defence ที่ต้อง audit AI output จะเลือก vendor ที่มี compliance primitive built-in. **Microsoft (Azure OpenAI) + Google Cloud** ต้องเร่ง — ไม่งั้นลูกค้า Fortune 500 ที่ renew contract 2027 จะ bias ไปทาง Anthropic. **AWS Bedrock** (ซึ่ง host Claude) ได้ประโยชน์ทางอ้อม

## Sources
- [Anthropic on X — self-evaluation layer disclosure](https://x.com/AnthropicAI)
- [AI Daily Digest November 1, 2026 — Claude self-evaluation + watermark (DEV)](https://dev.to/hiroki-ii-ai/ai-daily-digest-november-1-2026-google-folds-jules-into-antigravity-claude-ultra-drops-the-3e5e)
- [Anthropic Removes Five-Hour Limit for Verified Ultra (CryptoBriefing — pricing context)](https://cryptobriefing.com/anthropic-removes-five-hour-limit-ultra/)

---

## Audio script
ข่าวสุดท้ายของรอบนี้สำคัญสำหรับทีม compliance และ team ที่ build agent บน Claude Anthropic ประกาศผ่าน blog และ X ว่า newer Claude models มี hidden self-evaluation layer ที่รันหลัง response ถูก generate แล้ว layer นี้ output JSON ประมาณสิบ token ต่อ response บอก verdict ว่า response นั้น safe หรือ violation Anthropic ยืนยันว่าใช้บน production traffic จริงตั้งแต่มิถุนายน 2026 โดย user ไม่รู้ ตัวเลขที่ release บน Claude Fable 5 ที่ false-positive rate 1 เปอร์เซ็นต์ self-eval catch 78 เปอร์เซ็นต์ของ violation ที่ heavy constitutional classifier flag recall scale ตาม model size รุ่นเล็กสุด 16 เปอร์เซ็นต์ รุ่นใหญ่สุด 96 เปอร์เซ็นต์ แปลว่า bigger model better own judge คล้าย LLM-as-judge research แต่ครั้งนี้คือ self-as-judge validate ด้วย production traffic จริง สิ่งที่ developer ต้องรู้ verdict ไม่ให้ developer access มันคือ internal signal ของ Anthropic ไม่ chain เข้า Claude Agent SDK ถ้าคุณต้องการ custom guardrail ยังต้อง chain classifier ของตัวเอง อีกข่าวที่สำคัญ 3 พฤศจิกายน Anthropic ขยาย text watermarking ไปที่ Mythos 5 Opus 4.7 Opus 4.6 Sonnet 4.6 ก่อน EU AI Act deadline 2 ธันวาคม ประมาณ 1 เดือน EU require ว่า general purpose AI output ต้องมี machine readable mark Anthropic เลือก compete ที่ compliance ซึ่งคือ moat ที่ enterprise regulated banking insurance government จะเลือก สำหรับทีม compliance ไทยที่ต้อง deploy agent บน banking หรือ healthcare ให้ ask vendor ว่า watermark detector ของเขา ready ไหมก่อน EU AI Act ถ้าไม่พร้อมเสี่ยง non-compliance ครับ
