---
date: 2026-06-30
slug: openai-gpt-5-6-sol-terra-luna-government-gated
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  A dramatic editorial illustration of three celestial bodies in a dark cosmic
  scene — a massive glowing red sun labeled "SOL" dominates the frame on the
  left, a balanced earth-toned planet labeled "TERRA" sits center, and a small
  crescent moon labeled "LUNA" hovers on the right. A heavy government-style
  red velvet rope barrier with a gold "RESTRICTED — 20 PARTNERS ONLY" sign
  stretches across the foreground blocking access. An OpenAI logo glows faintly
  above. Bold floating headline reads "GPT-5.6 PREVIEW" with stacked pricing
  numbers "$5/$30 · $2.50/$15 · $1/$6" in oversized sans-serif. Cinematic
  lighting, deep navy and crimson palette, ultra-sharp text rendering for 200px
  thumbnail readability, 1:1 aspect ratio, tech-magazine cover style, no real
  human faces.
image: images/26-06-30-1714-01-openai-gpt-5-6-sol-terra-luna-government-gated.png
---

# OpenAI เปิดตัว GPT-5.6 Sol, Terra, Luna — frontier model ใหม่ที่รัฐบาลสหรัฐ "อนุญาตให้" ใช้ก่อนเพียง 20 บริษัท

## TL;DR
- 26 มิ.ย. — OpenAI ปล่อย limited preview ของ **GPT-5.6 Sol** (flagship), **Terra** (balanced), **Luna** (fast/cheap) — ครั้งแรกที่ frontier model release ถูก **gate ด้วย US frontier AI review process** ของรัฐ; เปิดให้ ~20 partner ที่ผ่าน approval เท่านั้น
- Pricing per 1M tokens: **Sol $5/$30**, Terra $2.50/$15, Luna $1/$6 — Sol ขยับขึ้นจาก GPT-5 ราว 60%, Terra ถูกลง 2x จาก GPT-5.5, Luna คือ price floor ใหม่ของ frontier-tier
- Sol อ้าง "agentic improvements ใน coding, biology, cybersecurity" + safety stack แข็งสุดในประวัติ OpenAI — เป็น signal ชัดว่า frontier release ในยุคต่อจากนี้ไม่ใช่ pure product decision อีกแล้ว แต่กลายเป็น **public-private regulatory choreography**

## เกิดอะไรขึ้น

26 มิถุนายน 2026 — OpenAI ประกาศ limited preview ของ **GPT-5.6** ที่ split เป็น 3 tier ครั้งแรก: **Sol** (flagship สำหรับงานยาก), **Terra** (balanced สำหรับ everyday work), **Luna** (fast + affordable). ใน blog post ทางการ OpenAI เรียกมันว่า "next-generation model" และระบุชัดว่า Sol ทำคะแนน agentic benchmark สูงสุดที่ลำดับ — โดยเฉพาะ coding, biological research, cybersecurity reasoning. แต่ที่จริงจัง — ใน sentence แรก ๆ ก็พ่วงเงื่อนไขมา: ทั้งสาม model "ยังไม่ generally available" และทุก partner ที่ได้เข้าถึง preview ต้องผ่าน **US frontier AI review process** ที่ Washington กำหนดเป็น gateway ใหม่

ตัว pricing structure เผยกลยุทธ์ทันที. Sol ราคา $5/$30 ต่อ 1M token (input/output) แพงกว่า GPT-5 ประมาณ 60% — ถือว่า "ขึ้นราคาเงียบ" ใน segment ที่ผู้แข่งขัน (Claude Opus 4.8, Gemini Ultra 3) ก็ขยับขึ้นพร้อมกัน. Terra ราคา $2.50/$15 ถูกลง 2x จาก GPT-5.5 — บีบ Sonnet/Flash/4o เข้ามาที่ middle tier. Luna ราคา $1/$6 คือ price floor ใหม่ของ frontier-grade — ตั้งใจกิน volume workload (search retrieval, classification, draft generation) ที่ฝั่ง Llama/Mistral เคยครอง

ที่ลึกกว่าราคาคือ **trust architecture**. OpenAI launch Sol พร้อม "safety stack ที่แข็งสุดในประวัติบริษัท" — ระบุชัดว่ามี strengthened protections สำหรับ high-risk activity, sensitive cyber requests, repeated misuse. ตัว review process ของรัฐบาลก็ไม่ใช่แค่ checkbox — เป็นการ vet ระดับลูกค้าต่อลูกค้า. 20 partner ที่ผ่าน includes ผู้เล่นใน defense, biosecurity research, critical infrastructure — Axios รายงานว่า list ใกล้กับ list ของ Anthropic Mythos 5 ที่ Commerce Department เพิ่งปลดล็อก export restriction บางส่วนเมื่อ 27 มิ.ย.

ภาพรวมของ 72 ชั่วโมงที่ผ่านมา — **frontier AI ในสหรัฐกลายเป็น dual-track**. Track หนึ่งคือ commercial release (GA models, public API) ที่ลูกค้าทั่วไปใช้ได้. Track สองคือ **frontier preview ที่รัฐ vet ก่อน** — Sol, Mythos 5, อาจรวม Gemini Vertex ต่อไป. ความหมายคือ enterprise ที่ต้องการ leading edge ต้องจัดที่ยืนใน track สอง — และนั่นเปลี่ยน sales motion ของทั้งวงการ

## ทำไมสำคัญ

**Tiering ที่ OpenAI ทำกับ Sol/Terra/Luna คือ first explicit acknowledgment ว่า frontier release จากนี้ไม่ใช่ "ของใหม่ใหญ่หนึ่งตัว" แต่เป็น product line** — ส่งสัญญาณตรง ๆ ว่าโลกที่เคยมี GPT-4 แล้วทุกคนใช้เหมือนกันหมดจบแล้ว. ทุก enterprise procurement ต่อจากนี้ต้องตอบคำถาม **"ใช้ tier ไหน สำหรับ workload ไหน"** ก่อน Vendor — Sol สำหรับ regulator-facing high-stakes work, Terra สำหรับ daily ops, Luna สำหรับ high-volume retrieval/classification. Anthropic ก็ขยับชั้นนี้ด้วย Opus 4.8 + Haiku 4.5 + Mythos — ความเหมือนเกินจะเป็นบังเอิญ

อีกชั้นที่สำคัญกว่า — **government gating กลายเป็น product feature**. การที่ OpenAI ปล่อย Sol ผ่าน Washington-approved partner list ก่อน GA หมายถึงสิ่งที่หลายคนพูดมานานหลายเดือนว่า "AI export control" จะเข้ามา — เข้ามาแล้ว และมาในรูปร่าง preview gate มากกว่ารูป ban. ดีต่อ OpenAI เพราะแบ่งแยก customer tier ได้ก่อนคู่แข่ง, เปิด channel ใหม่ของ trust-building กับรัฐ, ลด liability พลาด — แต่ความเสี่ยงคือ open-source/sovereign AI ขบวนการ (Mistral, Llama 5, DeepSeek) จะใช้เป็น narrative ว่า US labs กำลังกลายเป็น "regulated utility" และ EU/China จะใช้ moat นี้รุกตลาดที่ Washington vet ไม่ทัน

Pattern ที่เห็นชัด — **vendor-government coupling**. ขณะที่ Anthropic ฟ้อง DOD อยู่ในศาล (ยังไม่จบ) เรื่อง Mythos limits, OpenAI เลือก path opposite — เข้าทำงานในกลไก review process. แต่ละ lab กำลังเล่นเกม regulatory ที่ต่างกัน. ผู้ชนะระยะกลางคือ lab ที่ navigate dual track ได้แม่นที่สุด: ปล่อย commercial GA เร็ว + แทรก preview channel กับ regulator ได้ลึก. SpaceX-Cursor $60B deal ที่เพิ่งปิดสองสัปดาห์ก่อน (ลูกค้า enterprise 70% Fortune 1000, $2.6B enterprise ARR) ก็จะเข้าระบบนี้เช่นกัน — Sol/Terra/Luna จะเป็น default model ของ Cursor SpaceX แน่นอน

## มุม OpenBridge

Direct implication สำหรับ OpenBridge: **product positioning ต้อง assume tiered frontier เป็น default**. การออกแบบ connector / orchestration layer ของ OpenBridge ต้อง routing ระหว่าง Sol-class, Terra-class, Luna-class workloads ได้ทันที — และต้องคำนวณ TCO ของลูกค้าผ่าน routing rule ที่ตั้งเอง. ใครออก feature นี้ก่อน (LangChain, LlamaIndex, Vercel AI SDK, Cloudflare AI Gateway) ได้ moat 6-12 เดือน — OpenBridge ที่อยู่ในชั้น integration backbone มี window สั้นก่อนตลาดบีบ

อ้อมแต่สำคัญ — **government gate เปลี่ยน enterprise sales cycle ของ Thai bank/insurance**. KBank, SCB, BAY ที่อยากใช้ Sol-class frontier ต่อจากนี้ต้องผ่าน partner ที่ได้รับ US gov approval หรือ wait GA. นี่คือ window ให้ OpenBridge build **"sovereign routing layer"** — ลูกค้า Thai ใช้ Sol สำหรับ workload non-sensitive, ใช้ Sonnet/Gemini สำหรับ regulated data ใน region, ใช้ open-source สำหรับ on-prem. Product narrative ใหม่: "OpenBridge = vendor-neutral router ที่ไม่ต้องเลือก US lab เดียว"

## Sources
- [Previewing GPT-5.6 Sol: a next-generation model — OpenAI](https://openai.com/index/previewing-gpt-5-6-sol/)
- [OpenAI Launches GPT-5.6 Sol, Terra, and Luna in Limited Preview — MacRumors](https://www.macrumors.com/2026/06/26/openai-gpt-5-6-sol/)
- [OpenAI releases powerful new GPT-5.6 model under restrictions — Axios](https://www.axios.com/2026/06/26/openai-gpt-sol-terra-luna-trump)
- [OpenAI unveils GPT-5.6 Sol, Terra and Luna — VentureBeat](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov)
- [OpenAI GPT-5.6 Sol/Terra/Luna restricted to trusted partners — Latent Space](https://www.latent.space/p/ainews-openai-gpt-56-sol-terra-luna)

---

## Audio script

วันที่ยี่สิบหกมิถุนายน OpenAI ปล่อย GPT-5.6 ออกมาเป็นสามเวอร์ชั่นพร้อมกัน Sol, Terra, Luna. Sol คือ flagship — ทำงานยากที่สุด, agentic ดีที่สุด, แพงที่สุด ห้าดอลล่าร์ต่อล้าน input และสามสิบดอลล่าร์ต่อล้าน output. Terra คือเวอร์ชั่นกลาง — ราคาถูกลงสองเท่าจาก GPT-5.5. Luna คือเล็กที่สุด เร็วและถูกที่สุด ดอลล่าร์เดียวต่อล้าน input.

แต่เรื่องไม่ได้จบที่ราคา. ครั้งนี้พิเศษ — เพราะรัฐบาลสหรัฐกำหนดให้ Sol, Terra, Luna ผ่าน frontier AI review process ก่อน. แปลว่ามีแค่ประมาณยี่สิบบริษัทที่ได้ใช้ก่อน. ลูกค้าทั่วไปต้องรอ GA ในอีกหลายสัปดาห์. นี่เป็นครั้งแรกที่ frontier model release จากค่ายอเมริกาผ่าน gate ของรัฐแบบเปิดเผย.

ภาพที่เห็นคือ frontier AI ในสหรัฐกำลังกลายเป็น dual-track. Track หนึ่งคือ commercial release ที่ทุกคนใช้ได้. Track สองคือ preview ที่รัฐ vet partner ที่ได้เข้าถึงก่อน. Anthropic ก็มี Mythos 5 ที่ Commerce Department เพิ่งปลดล็อก export ban บางส่วน. Pattern เดียวกัน.

สำหรับทีม OpenBridge — สาม tier นี้เปลี่ยน design ของ integration layer ทั้งหมด. ต่อจากนี้ connector ต้อง route workload ระหว่าง Sol-class, Terra-class, Luna-class ได้อัตโนมัติ. ใครออกก่อนได้ moat สั้น ๆ ก่อนตลาดบีบ.
