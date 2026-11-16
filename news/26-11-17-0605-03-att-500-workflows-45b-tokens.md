---
date: 2026-11-16
slug: att-500-workflows-45b-tokens
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a telco network operations center,
  with a giant transparent floor-to-ceiling data stream wall at center
  flowing blue packets upward. Three stacked number panels dominate the
  foreground: "500 WORKFLOWS", "45B TOKENS / DAY", "3x BY 2027".
  Side rack labeled "BUSINESS AGENT FOUNDRY" sits on the left. A
  silhouette operator at a console labeled "HUMAN IN LOOP" bottom-right.
  AT&T-style blue halo lighting, clean editorial style, soft turquoise and
  deep navy palette, 1:1 aspect, no real human faces (silhouettes OK),
  high contrast so the numbers read at 200px.
image: images/26-11-17-0605-03-att-500-workflows-45b-tokens.png
---

# AT&T พิมพ์ตัวเลข agentic ของจริง — 500 workflow ใน production, 45 พันล้าน token/วัน, 5x ROI ภายในปีเดียว

## TL;DR
- AT&T ยืนยันผ่าน VP AI Luke Corbin ว่ามี workflow agentic ใกล้ 500 ตัวใน production — รัน 45B token ต่อวัน, 1M+ transaction ต่อเดือน, เป้าทำให้โต 3 เท่าในปี 2027
- Platform ชื่อ Business Agent Foundry — human-in-loop ทุก workflow จนกว่า accuracy จะแตะ mid-to-high 90% range
- AT&T อ้าง ROI ประมาณ 5 เท่าภายในปีแรกจาก production AI investment — ตัวเลข self-reported ยังไม่มี third party verify

## เกิดอะไรขึ้น
บทสัมภาษณ์ Luke Corbin, VP AI at AT&T ที่ Mobile World Congress sideline + งาน Investor Day ย่อย ๆ ช่วง 10–14 พ.ย. ชี้ตัวเลขที่เป็น milestone ของ enterprise agentic AI — เกือบ 500 workflow อยู่ใน production, platform Business Agent Foundry ประมวล token 45 พันล้านตัวต่อวัน และทำ transaction ธุรกิจมากกว่า 1 ล้าน transaction ต่อเดือน Corbin ยืนยันว่าเป้าหมายปีหน้าคือ triple ตัวเลข workflow ให้แตะ 1,500

ตัวเลข 45B token/วัน สำคัญเพราะ frame scale ที่ compare กับ consumer LLM ได้ — OpenAI เคยบอกว่า ChatGPT consumer ประมวล token ~100B/วัน แปลว่า AT&T ตัวเดียวใช้ token เกือบครึ่งของ ChatGPT ทั้ง consumer base ซึ่ง highlight สองประเด็น: หนึ่ง enterprise workload ใหญ่ขึ้น substantially จากปี 2024–25 สอง — AI gateway ของ AT&T ที่ route ไปหลาย model (open-source + proprietary) เริ่มมี throughput ที่ไม่น้อยไปกว่า hyperscaler consumer service

ด้าน governance Business Agent Foundry ใช้ pattern human-in-loop เป็น default — ทุก workflow เริ่มที่มี human review 100% ของ output จนกว่า accuracy จะยืนที่ mid-to-high 90% range ภายใน acceptable risk profile ถึงจะ graduate ไปเป็น full autonomous นี่คือ playbook ที่ Anthropic, DeepMind และ enterprise safety team หลายคนแนะนำมาตลอด — AT&T เป็นหนึ่งใน telco แรก ๆ ที่ document อย่างเปิดเผย

## ทำไมสำคัญ
ก่อนหน้านี้ตลาด enterprise agentic AI อ่านสัญญาณจาก case study ที่ "ตัวเลขดูน่าทึ่งแต่ scale ยังเล็ก" — เช่น Natera ที่ cut response time จาก 17 ชั่วโมงเหลือ 8 นาที หรือ UBS ที่ deploy 12,700 agent ตัวเลข AT&T แตกต่าง เพราะมันรวมสองสิ่ง: scope (500 workflow) + volume (45B token / 1M transaction) — แสดงทั้ง breadth และ throughput ซึ่งเป็นสัญญาณ production-maturity ที่สูงกว่า pilot

ข้อสังเกตที่สำคัญคือ "AT&T ไม่ได้ใช้ agent framework ของ hyperscaler ตัวใดตัวหนึ่ง" — Business Agent Foundry เป็น in-house platform ที่ orchestrate multiple model (รวม open-source) ผ่าน AI gateway ชี้ให้เห็นว่า enterprise ขนาด F100 เริ่มไม่ bet-the-farm กับ single vendor อีกต่อไป — multi-model, model-router, observability layer เป็น standard สำหรับ company ที่ serious กับ AI spend 9 digits ต่อปี Signal นี้ไม่ดีสำหรับ pure-play agent platform (Salesforce Agentforce, ServiceNow Now Assist) ถ้าใหญ่สุดมอง DIY เป็น default

Caveat — ตัวเลข 5x ROI self-reported ไม่มี third party audit นักวิเคราะห์ที่ Beri.net เตือนว่า definition ของ "workflow" ที่ AT&T ใช้ไม่ชัดเจน (เป็น business process ทั้ง end-to-end หรือเป็น individual automation task?) และ accuracy threshold "mid-to-high 90%" ไม่มี benchmark ที่เปิดเผย ก่อนจะเอาตัวเลขนี้เป็น case study อ้างอิงใน pitch deck อื่น ๆ ควรระวัง — telco มีหลาย workflow (customer service chat, bill reconciliation) ที่ error cost ต่ำ ต่างจาก medical / financial trading ที่ bar สูงกว่ามาก

## มุม AI Agent Platform
Builders — tool chain ที่ AT&T ใช้ชี้ว่า AI gateway + model router + observability (ไม่ใช่ agent framework) เป็น infrastructure ที่ enterprise ขนาดใหญ่ควร invest ก่อน Builders ที่คิดสร้าง agent product สำหรับ F500 ควร assume ว่าลูกค้ามี gateway แล้วและไม่ต้องการ vendor lock — API-first + OpenAI-compatible + MCP-compatible เป็นคุณสมบัติที่ไม่ใช่ nice-to-have อีกต่อไป Pattern "human-in-loop until accuracy stabilizes" ก็เป็น UX ที่ควร build ให้ default — ไม่ใช่ feature premium

Users/business — ถ้า AT&T ทำได้ 500 workflow ต่อปี องค์กรขนาดกลาง (1,000–5,000 คน) ควรตั้งเป้า production agent ที่ 30–50 workflow ภายใน 18 เดือนเป็นอย่างน้อย คำถามที่ต้องตอบก่อน scale คือ (1) มี AI gateway ที่ observable + fine-grained access control ไหม, (2) มี workflow owner ที่ accountable (ไม่ใช่ IT เฉย ๆ) ไหม, (3) มี KPI เชื่อม accuracy ของ agent กับ business outcome โดยตรงไหม Enabridge ลูกค้าไทยส่วนใหญ่ยังอยู่ phase 1 — การ scaffolding gateway + model-router เป็น foundational work ที่ไม่ควรข้าม

Ecosystem — ข่าวนี้คือ bull case ของ open-source + multi-model — ถ้า F100 ที่ใหญ่สุดเลือก DIY ด้วย open-source + proprietary mix จะดึง gravity ไปที่ observability layer (DataDog LLM obs, Humanloop, LangSmith), gateway (Portkey, Helicone, Kong AI Gateway) และ eval tools (Braintrust, Patronus) มากกว่า agent framework pure-play Bay, Kindo ที่ระดมเงินช่วงนี้เกี่ยวข้องตรง — security + governance layer เป็น segment ที่ F500 ขนาดใหญ่กำลังจ่ายจริง

## Sources
- [AT&T Runs ~500 Agentic AI Workflows Processing 45B Tokens a Day (AI Weekly)](https://aiweekly.co/alerts/att-runs-500-agentic-ai-workflows-processing-45b-tokens-a-day-targets-3x-by-2027)
- [AT&T Keeps Human Review on Nearly 500 AI Workflows (Beri.net)](https://www.beri.net/article/att-500-agentic-workflows-business-agent-foundry-human-oversight-high-90s-accuracy-threshold-45-billion-tokens-ai-gateway-open-models)
- [AT&T uses agentic AI to reinvent business processes (Physical AI News)](https://physicalainews.com/att-uses-agentic-ai-to-reinvent-business-processes-from-the-ground-up/)
- [AT&T Plans to Triple Production Agentic Workflows in 2027 (TokenPost)](https://www.tokenpost.com/news/business/57497)

---

## Audio script
AT&T เพิ่งพิมพ์ตัวเลข agentic AI ที่หายากมากในตลาดจริง Luke Corbin รองประธานฝ่าย AI ของ AT&T ยืนยันว่ามี workflow agentic เกือบ 500 ตัวอยู่ใน production — platform ภายในชื่อ Business Agent Foundry ประมวล token 45 พันล้านตัวต่อวัน ทำ transaction ธุรกิจมากกว่า 1 ล้านรายการต่อเดือน และเป้าหมายคือทำให้ตัวเลขนี้โต 3 เท่าในปี 2027

ตัวเลข 45 พันล้าน token ต่อวันสำคัญมาก เพราะมันใกล้ครึ่งหนึ่งของ ChatGPT ทั้ง consumer base นั่นหมายความว่า enterprise workload เริ่มใหญ่พอ ๆ กับ consumer scale และ AI gateway ของ AT&T ที่ route ไปหลาย model ทั้ง open-source และ proprietary กลายเป็น infrastructure ที่มี throughput ไม่น้อยไปกว่า hyperscaler

สิ่งที่น่าสนใจคือ AT&T ไม่ได้ใช้ agent framework ของ hyperscaler ตัวใดตัวหนึ่ง Business Agent Foundry เป็น in-house platform ที่ orchestrate หลาย model ผ่าน AI gateway บวก observability layer บวก human-in-loop ทุก workflow จนกว่า accuracy จะยืนที่ mid-to-high 90% range สำหรับ Enabridge และคนที่สร้าง agent platform บทเรียนตรงนี้ชัด — การลงทุน gateway กับ observability ต้องมาก่อน agent framework และ pattern "human-in-loop until stable" ต้องเป็น default ไม่ใช่ feature พิเศษครับ
