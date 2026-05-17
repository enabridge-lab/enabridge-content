---
date: 2026-05-11
slug: uber-3-4b-claude-code-budget-burned-four-months
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: A hero illustration of a burning stack of dollar bills inside a glass server rack, with neon code streams flowing out of the flames. Beside it a giant chart shows an exponential curve breaking through a ceiling labeled "2026 BUDGET". An Uber logo silhouette floats at top-right; a digital countdown reads "4 MONTHS". In massive condensed white sans-serif headline reads "$3.4B BURNED" with subline "70% of code = AI". Editorial dark charcoal and electric green palette, high contrast, magazine-cover composition, 1:1 aspect, no real human faces. Style The Information / Stratechery dramatic financial-news cover with cinematic depth and hot lighting.
image: images/26-05-12-0609-04-uber-3-4b-claude-code-budget-burned-four-months.png
---

# Uber เผางบ AI ทั้งปี 2026 ภายใน 4 เดือน — Claude Code ดัน 70% ของ code, $500-2,000 ต่อ engineer ต่อเดือน, "back to the drawing board"

## TL;DR
- CTO ของ Uber **Praveen Neppalli Naga** ออกมายอมรับว่าใน 4 เดือนแรกของ 2026 Uber **ใช้งบ AI ของทั้งปี $3.4B หมด** — Claude Code + Cursor adoption ระเบิดเกินที่ finance ทุกระดับเคย model: monthly API cost ต่อ engineer แตะ **$500-$2,000**, **95% ของ engineer ใช้ AI ทุกเดือน**, **70% ของ code ที่ commit มาจาก AI**
- **Minions** internal background coding agent ของ Uber (built on Claude) ตอนนี้ produce **~1,800 code change ต่อสัปดาห์ — zero human authoring** (engineer review/approve ตามปกติ); จาก <1% ของ code change ไป **8% ของ all code change** ในไม่กี่เดือน
- **Root cause** ไม่ใช่ราคา Claude Code ต่อ token แต่เป็น **organizational gap** ระหว่างทีมที่ขับ adoption (engineering) กับทีมที่ manage spend (finance/procurement) — pattern ที่ Goldman/Morgan Stanley/Disney/JPMorgan จะเจอเหมือนกันใน Q3-Q4

## เกิดอะไรขึ้น

ในระยะ 2 สัปดาห์ที่ผ่านมา **Praveen Neppalli Naga** (CTO Uber) ออก thread ใน X แล้วให้ interview กับ The Information ยอมรับว่า Uber **burn งบ AI ทั้งปี 2026 ของบริษัท ($3.4B) หมดในเดือนเมษายน** — เพียง 4 เดือนหลัง roll out Claude Code ให้ engineering team ในเดือนธันวาคม 2025 ตัวเลขรายละเอียดที่เปิดเผย: **monthly API cost per engineer** อยู่ที่ **$500-$2,000** (median ~$1,100), adoption rate **95% ของ engineer ใช้ AI ทุกเดือน** (เทียบ 60% เมื่อ ม.ค. 2026), **70% ของ committed code originated from AI** (เทียบ <10% สิ้นปี 2025)

ตัว engine ที่ทำให้ตัวเลขกระโดดคือ **Minions** — internal background coding agent ที่ Uber build บน Claude (run ผ่าน Anthropic API + Uber MCP gateway) Minions produce **~1,800 code change ต่อสัปดาห์** ที่เป็น **fully autonomous authoring** (zero human typing — engineer review + merge เท่านั้น) เพิ่มจาก <1% ของ all code change ที่ Uber merge เป็น **8% ภายใน 3 ไตรมาส** — number ที่ Praveen เรียก "real reset moment for engineering" engineer ของ Uber 95% engage AI tool ทุกเดือนรวมทั้ง Claude Code, Cursor, GitHub Copilot และ Uber MCP gateway ที่ power no-code agent builder + Minions

Praveen อธิบาย root cause ของ budget overrun ไม่ใช่ "Claude Code แพง" — **monthly cost per engineer $500-$2,000 ยัง justifiable** ถ้าเทียบกับ salary $250-500k/ปี + productivity gain การ overrun เกิดจาก **organizational gap**: ทีม engineering ที่ขับ adoption (และเก็บ KPI productivity ของตัวเอง) ไม่ communicate กับทีม finance/procurement ที่ manage spend ทำให้ ramp-up ของ usage exponential ไม่มี control loop Uber ranking engineer ใน internal leaderboard ตาม AI tool usage ด้วย ซึ่ง create incentive ใช้เยอะ — ตอนนี้ Uber "back to the drawing board" หา structure ที่ balance — Praveen บอกว่าจะ negotiate enterprise pricing tier กับ Anthropic / Cursor และ build internal **token budget governance** ให้ทีม

## ทำไมสำคัญ

เรื่องของ Uber คือ **first major case study ของ "consumption-based AI cost ที่ scale แบบ uncontrolled"** ในเชิง production — ไม่ใช่ SaaS subscription ที่ predictable, ไม่ใช่ data warehouse ที่ slope ขึ้นช้า, แต่เป็น cost curve ที่ proportional กับ **engineer productivity gain** ตรงๆ ปัญหาคือ productivity gain ที่ engineer สัมผัสได้คือ "code มากขึ้น แก้ bug ไว" — ไม่ใช่ "AI cost ที่ company จ่ายต่อ commit" — และ Uber ไม่มี telemetry ที่ map cost ตรงกับ value ในระดับ engineer/task

Signal สำหรับ market: **Q3-Q4 2026 จะเห็น CFO panic หลายราย** Goldman Sachs (deploy Claude วงกว้าง), JPMorgan, Disney (ที่ AI integration เต็มสตูดิโอ), Microsoft (internal use of GitHub Copilot), Netflix (ตัวที่ Anthropic Multi-Agent Orchestration case study) — ทุก firm จะหา budget overrun เดียวกัน เพราะ pattern ของ rollout ดูเหมือน Uber: engineering ทดลอง ขยายตามที่ engineer "อยากใช้" ไม่มี governance พอ vendor side: Anthropic + OpenAI จะเปิด enterprise pricing tier ที่มี **token budget controls + alerting + dashboard** เป็น product feature default — และ market FinOps สำหรับ AI (เดิม cloud cost FinOps tool เช่น CloudHealth, Vantage) จะเปิด segment ใหม่ "AI FinOps"

อีก angle ที่ปลายตา: ตัว Minions เอง — internal coding agent ที่ produce 1,800 change/week zero authoring — เป็น **proof point ที่ดังที่สุดเรื่อง autonomous agent ใน production engineering** ที่ public อยู่ตอนนี้ Anthropic Dreaming/Outcomes/Multi-Agent (ที่ออกเมื่อ 6 พ.ค.) เป็น primitive ของ platform; แต่ Minions แสดงว่า workflow autonomous ที่ run โดยลูกค้าเอง (Uber) บน Claude raw API ก็ทำงานได้ที่ scale 1,800/wk เพียง 6 เดือนหลัง launch — เป็น blueprint ให้ทุก enterprise engineering team อยาก copy ใน 2026-2027 ความหิวของตลาดต่อ pattern นี้คือสิ่งที่ขับ Anthropic API revenue + ขับ Uber bill ระเบิด

## มุม OpenBridge

OpenBridge ต้องดูสองด้านพร้อมกัน: (1) **threat** — เพราะ Uber พิสูจน์ว่า bottleneck ที่ enterprise วันนี้ไม่ใช่ "AI fast enough" แต่เป็น "cost governance" และ enterprise พร้อมที่จะลงทุน FinOps tool ก่อน expand integration ใหม่ ทำให้ sales cycle ของ OpenBridge อาจ slow ใน Q3-Q4 ถ้า buyer เปลี่ยน priority; (2) **opportunity** — Uber Minions + MCP gateway pattern แสดงว่าทุก enterprise engineering team จะอยาก build "Minions ของบ้านตัวเอง" ใน 12 เดือน — ต้องการ MCP gateway + connector + audit trail ที่ทำงานกับ Claude / GPT / Gemini หลายตัวพร้อมกัน

Action ตรง: (1) **เปิด "OpenBridge for Internal Agents" product** — MCP gateway + connector + per-agent token budget + per-team cost dashboard ที่ enterprise engineering team deploy ในบ้าน ที่มี Uber-style governance built-in; (2) **partnership กับ Vantage / CloudZero / Finout** สำหรับ AI FinOps integration — OpenBridge ส่ง usage telemetry ตรง dashboard ของ FinOps tool ที่ CFO อ่านอยู่แล้ว; (3) **case study sales asset** — เขียน whitepaper "How to Avoid Uber's $3.4B Mistake" สำหรับ buyer enterprise engineering ที่กำลัง deploy internal coding agent — ใช้ pattern ของ Uber เป็น cautionary tale ไม่ใช่ blueprint แล้ว pitch OpenBridge MCP gateway เป็น governance layer; (4) **ดู Thai bank/telco/conglomerate** ที่กำลัง roll out Claude/GPT enterprise (SCBX, AIS, PTT, ThaiBev) — ทุกองค์กรจะมี Uber moment ภายใน 12-18 เดือน OpenBridge เข้าก่อน CFO panic = win deal ก่อน RFP

Pattern ใหญ่: **ตลาด FinOps สำหรับ AI agent คือ category ใหม่ที่ Uber ปูทาง** OpenBridge ต้องเป็น **"infrastructure ที่ engineer love + finance trust"** — ไม่เลือกข้างใดข้างหนึ่ง ในขณะที่ pure-play AI FinOps startup จะเข้ามาแย่ง space นี้ภายใน 6 เดือน

## Sources
- [Praveen Neppalli on X: "Agentic software engineering adoption is on fire at @Uber"](https://x.com/praveenTweets/status/2033627282418655711)
- [Uber Spends Full 2026 AI Budget in 4 Months — Briefs.co](https://www.briefs.co/news/uber-torches-entire-2026-ai-budget-on-claude-code-in-four-months/)
- [Uber CTO Shows How Claude Code Can Blow Up AI Budgets — The Information](https://www.theinformation.com/newsletters/applied-ai/uber-cto-shows-claude-code-can-blow-ai-budgets)
- [Uber's Anthropic AI Push Hits A Wall — CTO Says Budget Struggles Despite $3.4B Spend — Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/ubers-anthropic-ai-push-hits-223109852.html)
- [How Uber uses AI for development: inside look — Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development)

---

## Audio script
ข่าวที่จะถูกพูดถึงนานคือ Uber CTO ออกมายอมรับว่าใน 4 เดือนแรกของ 2026 บริษัทใช้งบ AI ทั้งปี 3.4 พันล้านดอลลาร์หมด Claude Code กับ Cursor adoption ระเบิดเกินที่ finance เคย model ตัวเลขรายละเอียด monthly API cost ต่อ engineer แตะ 500 ถึง 2 พันดอลลาร์ 95% ของ engineer ใช้ AI ทุกเดือน 70% ของ code ที่ commit มาจาก AI Minions internal coding agent ของ Uber build บน Claude ตอนนี้ produce 1800 code change ต่อสัปดาห์ engineer ไม่ได้พิมพ์เลย review approve อย่างเดียว จาก น้อยกว่า 1% ของ code change ของบริษัท ไป 8% ในไม่กี่เดือน CTO Praveen Neppalli Naga บอกว่า root cause ไม่ใช่ราคา Claude แพง แต่เป็น organizational gap ระหว่างทีม engineering ที่ขับ adoption กับทีม finance ที่ manage spend Uber ranking engineer ใน leaderboard ตาม AI tool usage ด้วย create incentive ใช้เยอะ Q3 Q4 จะเห็น Goldman JPMorgan Disney Netflix Microsoft เจอ pattern เดียวกัน vendor side Anthropic OpenAI จะเปิด enterprise pricing tier ที่มี token budget controls dashboard เป็น default feature ตลาด FinOps สำหรับ AI agent กลายเป็น category ใหม่ สำหรับ OpenBridge ต้องเปิด product MCP gateway plus per-agent token budget plus per-team cost dashboard ที่ enterprise engineering team deploy ในบ้านได้ มี Uber-style governance built-in และ partner กับ Vantage Finout สำหรับ AI FinOps integration buyer SEA SCBX AIS PTT ThaiBev จะมี Uber moment ภายใน 12 ถึง 18 เดือน เข้าก่อน CFO panic ชนะก่อน RFP ครับ
