---
date: 2026-09-15
slug: google-antigravity-claude-opus-5-engineers
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A dramatic editorial illustration of a fortress labeled "GOOGLE" with its main
  drawbridge lowered, revealing a glowing purple orb marked "CLAUDE OPUS 5"
  rolling inside past a signpost reading "ANTIGRAVITY IDE". Above the fortress
  wall a smaller banner reads "GEMINI = PRIMARY", contrasted with a bigger neon
  sign "OPUS 5 = FOR EVERY ENGINEER". In the foreground a silhouette in a
  hoodie carries a laptop marked "COMMIT PR". Editorial isometric style, deep
  navy and google-red palette with amber highlights, 1:1 aspect, no real human
  faces.
image: images/26-09-16-0609-01-google-antigravity-claude-opus-5-engineers.png
---

# Google เปิดประตูให้ engineer ทุกคนใช้ Claude Opus 5 ผ่าน Antigravity — เส้นระหว่าง frontier lab เริ่มเบลอ

## TL;DR
- Business Insider รายงาน 15 ก.ย. — Google เปลี่ยน internal policy ให้ engineer **ทุกคน** เข้าถึง Claude Opus 5 ผ่าน Antigravity (agent-first IDE ที่ Google ต่อยอดจากทีม Windsurf ที่ซื้อมา $2.4B)
- ก่อนหน้านี้ Claude เข้าถึงได้เฉพาะทีม DeepMind กับ high-priority projects เท่านั้น; engineer ทั่วไปโดนบังคับใช้ Gemini
- Google ยังยืนยัน "Gemini remains our primary and foundational model" — แต่การเปิด Opus 5 ให้ทุกคนเป็น signal ว่า internal developer productivity กำลังชนะ narrative "eat our own dog food"

## เกิดอะไรขึ้น

Hugh Langley จาก Business Insider แตกข่าววันที่ 15 กันยายน — Google ปรับ policy ภายในให้ engineer ทุกคนเข้าถึง **Claude Opus 5** ผ่าน Antigravity ได้ทันที. Antigravity คือ agent-first IDE ที่ Google ปล่อยเมื่อ 4 เดือนที่แล้ว หลังจากซื้อทีม Windsurf มาที่ราคา $2.4 พันล้านเมื่อพฤศจิกายน 2025 — ตัว IDE ไม่ได้ทำ autocomplete แบบ Copilot ตัวเก่า แต่รัน plan + execute + verify loop เพื่อจบงานเป็น task ("implement this API endpoint with tests" แล้วมันรันจนเสร็จ).

ก่อนหน้านี้ Claude ใน Google ถูกล็อกไว้แค่บางทีมของ DeepMind กับ high-priority projects. Engineer ส่วนใหญ่ต้องใช้ Gemini เท่านั้น — ซึ่งเป็นสัญลักษณ์สำคัญ เพราะ Google เคยยึดหลัก "eat our own dog food" อย่างเคร่งครัด. โฆษก Google ยืนยันกับ Business Insider ว่า "Gemini remains our primary and foundational model for internal development" พร้อมกับเปิด quota Opus 5 ให้ทุกคนใช้ตาม limit

ที่น่าสนใจกว่านั้นคือ context — engineer ภายในหลายคนบ่นมานานว่า Gemini ทำงาน coding ไม่เทียบเท่า Claude โดยเฉพาะ multi-step refactoring และการเข้าใจ codebase ขนาดใหญ่. การเปิดให้ทุกคนใช้ Opus 5 คือการยอมรับกลาย ๆ ว่า Anthropic ยังนำในสายนี้อยู่ — และการยึดหลักปิดกั้นเครื่องมือคู่แข่งกำลังกินเวลา engineer ต่อวันของ Google เอง.

## ทำไมสำคัญ

หนึ่งปีก่อน frontier lab แต่ละที่ต่างจับมือฝั่งตัวเองอย่างชัดเจน — OpenAI มี Copilot/GitHub, Google มี Gemini + AI Studio, Anthropic เสิร์ฟผ่าน AWS Bedrock. เรื่อง engineer Google ใช้ Claude ในงานจริงคือการยอมรับต่อสาธารณะว่า **ยุคของ pure single-vendor coding stack จบแล้ว** — ต่อไปทุก IDE จะ multi-model และเลือก model ตาม task ไม่ใช่ตาม vendor. Anthropic ได้ validation ครั้งใหญ่ที่สุดจากคู่แข่งตัวเอง.

Signal อีกชั้นคือ Antigravity เอง — Google กำลังเดิมพันว่า UX ของ coding agent ต้องเป็น IDE ที่ plan + execute + verify ครบใน loop เดียว ไม่ใช่ chat box + autocomplete. ถ้ามอง pattern แล้ว: Cursor + Windsurf + Antigravity + Cline + Claude Code — ทุกตัวมุ่งไปทางเดียวกันคือ agent เป็นชั้น orchestrator ทับ IDE ไม่ใช่ปลั๊กอินใน IDE เดิม. ตัว model กลายเป็น commodity ที่สลับได้ทันที; IDE + workflow กลายเป็น moat.

สำหรับ Anthropic การได้ engineer 30,000+ คนของ Google ใช้ Opus 5 ทุกวัน หมายถึง feedback loop จากคนที่ demanding ที่สุดในโลก — เอามาใช้เทรน Opus รุ่นต่อไปได้ยาว. สำหรับ Google การยอมเปิดคือการยอมรับว่า **productivity ของทีม engineering ตัวเองสำคัญกว่า vendor loyalty** — ท่าทีที่บริษัทไทยหลายแห่งยังคิดไม่ถึง

## มุม AI Agent Platform

**Builders** ที่กำลังสร้าง coding agent — ดู pattern ของ Antigravity: plan + execute + verify loop, ไม่ใช่ single-turn autocomplete. Model ต้องเปลี่ยนได้ทันที (Gemini, Claude, GPT), ไม่ใช่ล็อกไว้ที่ตัวเดียว. IDE / orchestrator layer คือที่ที่ product moat จะเกิด ไม่ใช่ตัว model. **Users / business** โดยเฉพาะทีม engineering ไทย — ถ้ายังบังคับให้ dev ทีมใช้ Copilot อย่างเดียว หรือให้ใช้ Cursor แต่ล็อก model ให้ใช้ GPT-4 อย่างเดียว ต้องคิดใหม่: engineer productivity หายไปเยอะกว่าค่า license หลายเท่า. Google เดิมพัน $2.4B เพื่อได้ Windsurf แล้วยังเปิดให้ engineer เลือก model ได้เอง — บริษัทอื่นที่งบน้อยกว่าจะเถียงยากขึ้น. **Ecosystem** — Bedrock ได้ประโยชน์เต็ม ๆ (Anthropic ให้ Google เข้าถึง Opus 5 ผ่านช่องทางไหนก็ไม่ชัด แต่ Bedrock เป็น pipe หลัก), Cursor/Windsurf-alike ตลาดจะเปิดกว้าง, และ Gemini ในสายเดียวกันจะโดนกดดันหนักขึ้นให้ปิดช่องว่างกับ Opus 5.

สำหรับตลาดไทย — ทีม dev ในบริษัทใหญ่ (SCB TechX, KBTG, Central Tech) ที่ยังยึด single-vendor coding tool ควรอ่าน move นี้ให้ดี. คำถามที่ต้องถามคือ "เรามี agent-first IDE ให้ทีมใช้แล้วหรือยัง" ไม่ใช่ "ใช้ Copilot ตัวไหนดี".

## Sources
- [Google gives all of its engineers Claude Opus 5 access via Antigravity (Techmeme roundup, Business Insider)](https://www.techmeme.com/260915/p5)
- [Google Antigravity + Claude Is the Hybrid AI Dev Setup Nobody Expected](https://medium.com/@karthikmulugu/google-antigravity-claude-is-the-hybrid-ai-dev-setup-nobody-expected-e19f505b0a24)
- [Google breaks internal precedent, opens Anthropic's Claude model to all engineers](https://finance.biggo.com/news/2aa7c4bf-ad9a-4e3b-8ed8-3c2862e9ecb6)

---

## Audio script
วันนี้มีข่าวใหญ่จาก Google ที่เปลี่ยน internal policy ให้ engineer ทุกคนเข้าถึง Claude Opus 5 ผ่าน Antigravity ได้ทันทีครับ. Antigravity เป็น agent-first IDE ที่ Google ต่อยอดจากทีม Windsurf ที่ซื้อมาที่ราคาสองพันสี่ร้อยล้านเหรียญ เมื่อพฤศจิกายน 2025. ก่อนหน้านี้ Claude ใน Google เปิดให้เฉพาะทีม DeepMind กับ high-priority projects เท่านั้น. engineer ทั่วไปโดนบังคับใช้ Gemini อย่างเดียว. โฆษก Google ยังยืนยันว่า Gemini remains the primary model for internal development แต่การเปิด Opus 5 ให้ทุกคนใช้ตาม quota เป็น signal สำคัญมากว่า Google ยอมรับว่า Anthropic ยังนำในสาย coding อยู่ และการยึดหลักปิดกั้นเครื่องมือคู่แข่งกำลังกินเวลา engineer ต่อวันของบริษัทเอง. Signal ที่ควรอ่านคือ ยุคของ single-vendor coding stack จบแล้วครับ. ต่อไปทุก IDE จะ multi-model และเลือก model ตาม task ไม่ใช่ตาม vendor. Antigravity ไม่ใช่ autocomplete แบบ Copilot ตัวเก่า แต่รัน plan execute verify loop เพื่อจบงานเป็น task ทั้งชิ้น. สำหรับ builder ที่กำลังทำ coding agent — model ต้องสลับได้ทันที, IDE กับ orchestrator layer คือที่ที่ moat จะเกิด ไม่ใช่ตัว model. สำหรับทีม engineering ไทยในบริษัทใหญ่อย่าง SCB TechX KBTG Central Tech ที่ยังบังคับให้ dev ใช้ tool ตัวเดียว ต้องคิดใหม่ครับ. Google เดิมพันสองพันสี่ร้อยล้านเหรียญเพื่อได้ Windsurf แล้วยังเปิดให้ engineer เลือก model ได้เอง บริษัทอื่นที่งบน้อยกว่าจะเถียงยากขึ้น. คำถามใหม่ที่ต้องถามคือ เรามี agent-first IDE ให้ทีมใช้แล้วหรือยัง ไม่ใช่ ใช้ Copilot ตัวไหนดี
