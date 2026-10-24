---
date: 2026-10-24
slug: replit-openai-100m-anthropic-switch
topic: use-case
reading_time_min: 5
sources: 3
image_prompt: |
  An editorial isometric illustration of two glowing tech headquarters facing
  off: a large orange OpenAI tower with its logo on top, pulling a thick cable
  labeled "REPLIT $100M+/YR" out of a smaller purple Anthropic tower. The
  cable is tagged with a bright yellow discount coupon reading "30%+ OFF".
  Below, a scoreboard shows "OPENAI 16% → 52%" on the left and
  "ANTHROPIC 57% → 18%" on the right under a header reading "RIPPLING
  CODING SHARE". Deep navy, orange and purple palette, strong contrast for
  200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-25-0605-02-replit-openai-100m-anthropic-switch.png
---

# Replit ย้ายงบ AI กว่า $100M/ปี จาก Anthropic ไป OpenAI หลัง 30%+ discount — model switching กลายเป็น enterprise reality

## TL;DR
- **23–24 ต.ค.** The Information รายงาน Replit **ย้ายงบ AI ส่วนใหญ่จาก Anthropic ไป OpenAI** ในดีลมูลค่า **เกิน $100M ต่อปี** หลัง OpenAI เสนอส่วนลดเกิน **30%** และ Anthropic ปฏิเสธจะต่อ discount เดิมโดยไม่เพิ่ม commitment
- Rippling (เครื่องมือ HR + payroll) รายงานตัวเลขที่น่าตกใจ: **OpenAI share ใน coding workload** โตจาก **16% ใน พ.ค. → 52% ตอนนี้** ขณะที่ **Anthropic ตกจาก 57% → 18%**
- Amjad Masad CEO Replit พูดที่ TechCrunch Disrupt (16 ต.ค.) ว่า **"not working with Anthropic"** แล้ว เหตุผล: cost + partnership + performance; OpenAI กลายเป็น **default model สำหรับ Replit Agent**
- Signal: **enterprise ที่ build on top ของ foundation model เริ่มสวิทช์ provider แบบจริงจัง** — ไม่ใช่แค่ A/B test. Lock-in ที่ frontier lab คิดว่ามีจริงอาจไม่มี

## เกิดอะไรขึ้น

ก่อนรุ่งเช้าของวันเสาร์ที่ **24 ต.ค.** (ตามเวลาสหรัฐ) The Information ปล่อยรายงานว่า **Replit** platform สำหรับ cloud dev + no-code agent builder ได้ **ย้ายงบ AI ส่วนใหญ่จาก Anthropic ไป OpenAI** ในดีลมูลค่าเกิน **$100 ล้านต่อปี**. OpenAI ให้ discount **เกิน 30%** ซึ่งทำให้ unit economics ของ Replit Agent (ที่ชาร์จ end user ต่อ task) กลับมาบวก. source บอกว่า Anthropic เคยให้ discount Replit อยู่ แต่เลือกไม่ต่อถ้า Replit ไม่เพิ่ม commitment ขนาดใหญ่

Amjad Masad CEO Replit เปิดเผยทิศทางนี้ไว้แล้วตั้งแต่ **TechCrunch Disrupt (16 ต.ค.)** — เขาบอกตรง ๆ ว่า **"Replit is no longer working with Anthropic"** และเหตุผล **"based on both cost, partnership, and performance"**. ตอนนี้ **OpenAI เป็น default model ของ Replit Agent**; user ที่ต้องการ Claude ยัง switch ไปใช้ได้ และ Replit docs ยังขึ้น Claude 7 รุ่น ซึ่งทำให้ source บางสายฝั่ง Anthropic อ้างว่า "ความสัมพันธ์ยังอยู่"

ตัวเลขที่น่ากลัวกว่าดีลเดี่ยวคือ **data ของ Rippling** ที่ The Information quote: ในระบบ Rippling (เครื่องมือ enterprise HR + spend management ที่มีลูกค้าแสน ๆ บริษัท) **OpenAI's share ใน coding workload** โตจาก **16% ใน พ.ค. 2026 → 52% วันนี้** ส่วน **Anthropic ตกจาก 57% → 18%** ภายในระยะเวลาแค่ **~5 เดือน**. นี่ไม่ใช่ dataset ของ Replit คนเดียว — มันคือ aggregate ของบริษัทจำนวนหลักพันที่ใช้ coding assistant

ย้อนกลับไปต้นปี 2026, Anthropic domain เรื่อง coding agent แทบไม่มีคู่แข่ง — Claude Sonnet 4/5 เป็น default ของ Cursor, Replit, GitHub Copilot (option) และ internal tool หลาย ๆ บริษัท. การ turnaround ขนาดนี้ใน 5 เดือนสะท้อนสาม factor พร้อมกัน: (1) **GPT-6 Astra และ coding model ของ OpenAI ดีขึ้นจริง** (65–70% range บน SWE-Bench Verified), (2) **ราคา OpenAI ลงเร็วกว่า** — Replit ได้ 30%+, Rippling spec ก็น่าจะใกล้เคียง, (3) **Anthropic เลือก discipline เรื่อง pricing** — ไม่ยอม race to the bottom เพื่อ retain volume. CEO Dario Amodei เคยพูดว่า unit margin สำคัญกว่า market share ในช่วง IPO prep (Anthropic จะ IPO กลาง พ.ย. ตามรายงาน Reuters)

## ทำไมสำคัญ

จุดที่หนึ่ง — **lock-in ของ foundation model layer ไม่แข็งอย่างที่ frontier lab เคยคาด**. ตอนที่ Replit, Cursor, GitHub ประกาศ default model เมื่อปีก่อน, VC วิเคราะห์ว่า "whoever ชนะ coding, ชนะ long-term" เพราะ workflow, prompt library, muscle memory ของ dev จะ lock. ความจริงคือ **model abstraction layer** (ของ Replit, Cursor, LangChain, OpenRouter) ทำให้ **การสลับ model ใช้เวลาเป็นสัปดาห์ไม่ใช่เดือน** พอ pricing เอื้อ. ซึ่งแปลว่า **leverage ของ foundation model lab vs. application layer คนลด**

จุดที่สอง — **enterprise AI budget เริ่ม behave เหมือน cloud compute**. Rippling data (OpenAI 16%→52% / Anthropic 57%→18%) คือ pattern เดียวกับที่เราเห็นตอน AWS→GCP migration เมื่อ 2018-20: pricing + performance movement ทริกเกอร์ migration ครึ่งทางภายในสองไตรมาส. ถ้า pattern นี้ยืน Anthropic อาจเสีย coding workload share เป็นหลัก 10 point ภายในสิ้นปี — ซึ่งใน IPO prep หมายถึง revenue mix shift ที่ underwriter ต้อง re-model

จุดที่สาม — **compound effect กับ open-weight**. Kimi K3.1 Pro (ปล่อย 23 ต.ค., open weights 4 พ.ย.) ชี้ว่า 65% บน Terminal-Bench 4.0 ทำได้ด้วย open model. ภายใน 2027 **enterprise จะมีสาม tier**: frontier closed (Claude/GPT), discount frontier (เช่น Kimi, Qwen, Mistral Large 3), และ self-hosted open. Replit ครั้งหน้าอาจไม่ย้ายไป OpenAI — อาจย้ายไป open-weight ของตัวเอง

## มุม AI Agent Platform

สำหรับ **Builders**: ถ้า build agent platform หรือ coding assistant **อย่า hardcode model vendor**. abstraction layer (ของ LiteLLM, Portkey, OpenRouter, LangChain) จะกลายเป็น non-negotiable infrastructure — ไม่ใช่เพราะ developer อยากทดลอง แต่เพราะ **CFO จะเริ่มขอ model-switching flexibility เป็น hard requirement** ของ procurement contract. agent framework ที่ลึกผูกกับ API ของ provider เดียวจะเสียเปรียบ

สำหรับ **Users / Business**: ถ้า deploy coding agent ภายใน (เช่น Cursor Enterprise, GitHub Copilot Enterprise, Replit Teams, Devin) **เริ่มเจรจา pricing กับ vendor โดยอ้าง benchmark multi-vendor**. ตอนนี้ Replit แสดงให้เห็นว่า discount 30%+ ที่ scale $100M เป็นไปได้ — บริษัทที่ spend $5–10M/ปีก็น่าจะได้ 15–20%. ที่สำคัญกว่า: **ให้ internal team พยายามสร้าง evaluation ของตัวเองเพื่อตัดสินว่า model ไหน perform ดีกว่าสำหรับ codebase ของบริษัท** — ไม่ใช่พึ่ง public benchmark

สำหรับ **Ecosystem**: Anthropic IPO (กลาง พ.ย.) จะ reprice ที่ valuation ลดลง หรือ delay. OpenAI ชนะ coding segment ชั่วคราว แต่ margin จะลดลงเพราะ discount model ที่ให้. **ผู้ชนะที่แท้จริงอาจเป็น model router + inference platform** (เช่น Portkey, Not Diamond, OpenRouter) ที่กินค่า orchestration + optimization

## Sources
- [Replit Shifts $100M+ AI Spend to OpenAI After 30% Price Cut (AI Weekly, citing The Information)](https://aiweekly.co/alerts/replit-shifts-100m-ai-spend-to-openai-after-30-price-cut)
- [Techmeme: Replit moved most AI spend from Anthropic to OpenAI (The Information)](https://www.techmeme.com/261024/p8)
- [Replit is no longer working with Anthropic, CEO says (Daily.dev / TechCrunch Disrupt)](https://daily.dev/posts/replit-is-no-longer-working-with-anthropic-ceo-says-dwx4lw3uu)

---

## Audio script
วันเสาร์ 24 ตุลาคมเช้า The Information รายงานว่า Replit platform สำหรับ cloud dev และ no-code agent ย้ายงบ AI ส่วนใหญ่จาก Anthropic ไป OpenAI เป็นดีลมูลค่าเกิน 100 ล้านดอลลาร์ต่อปี. OpenAI ให้ discount เกิน 30 เปอร์เซ็นต์ ซึ่งทำให้ unit economics ของ Replit Agent กลับมาบวก. Anthropic เคยให้ discount Replit อยู่แต่เลือกไม่ต่อถ้าไม่เพิ่ม commitment ขนาดใหญ่. Amjad Masad ซีอีโอ Replit บอกที่ TechCrunch Disrupt เมื่อ 16 ตุลาว่า Replit not working with Anthropic อีกต่อไป เหตุผลเพราะ cost partnership และ performance. ตอนนี้ OpenAI คือ default ของ Replit Agent. ตัวเลขที่น่ากลัวกว่าดีลเดี่ยวคือข้อมูลจาก Rippling ที่ The Information quote — OpenAI share ใน coding workload โตจาก 16 เปอร์เซ็นต์ในเดือนพฤษภาคมเป็น 52 เปอร์เซ็นต์วันนี้ Anthropic ตกจาก 57 เป็น 18 ใน 5 เดือน. ตีความได้สามประเด็น หนึ่ง lock-in ของ foundation model ไม่แข็งอย่างที่ VC เคยคาด model abstraction layer อย่าง LiteLLM Portkey OpenRouter ทำให้สวิทช์ model ใช้เวลาแค่สัปดาห์. สอง enterprise AI budget behave เหมือน cloud compute 2018 to 2020 ตอน AWS to GCP — ราคากับ performance ทริกเกอร์ migration ครึ่งทางใน 2 ไตรมาส. สาม Kimi K3.1 Pro ที่ปล่อยวันเดียวกันเตือนว่า open weight gen next จะมา enterprise จะมีสาม tier คือ frontier closed, discount frontier, และ self hosted open. สำหรับคน build agent platform อย่า hardcode model vendor abstraction layer คือ non negotiable. CFO จะขอ model switching flexibility เป็น hard requirement ของ procurement ภายในปีหน้า. และผู้ชนะที่แท้จริงอาจเป็น model router และ inference platform ไม่ใช่ foundation lab ไหนเลย
