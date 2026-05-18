---
date: 2026-05-16
slug: anthropic-claude-agent-credits-openclaw-meter
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: A vintage gas-station style meter labeled "CLAUDE AGENT CREDITS" with three illuminated dial tiers showing "$20 PRO", "$100 MAX 5x", "$200 MAX 20x" in bold cyberpunk typography. Behind it, a glowing Anthropic logo and an OpenClaw-style claw silhouette reaching toward the meter. A floating date stamp reads "JUNE 15, 2026". Composition: centered hero shot, dark navy background with electric orange accents for contrast. Style: editorial illustration, retro-futuristic, high contrast for thumbnail legibility, no human faces.
image: images/26-05-16-0604-02-anthropic-claude-agent-credits-openclaw-meter.png
---

# Anthropic ใส่ meter ให้ Claude agents — เปิด OpenClaw กลับมาแลก credit แยกชั้น $20/$100/$200

## TL;DR
- เริ่ม **15 มิ.ย. 2026** — Anthropic แยก programmatic Claude usage ออกจาก chat subscription, ใช้ monthly credit ที่ API-style rate
- Tier: **Pro $20 / Max 5x $100 / Max 20x $200** ต่อเดือน ใช้กับ Agent SDK, GitHub Actions, third-party harness เช่น OpenClaw
- กลับลำหลังจาก 4 เม.ย. ที่บล็อก OpenClaw และ 135K+ instances ทั้งหมด — ครั้งนี้เปิดกลับแต่จ่ายตามจริง

## เกิดอะไรขึ้น

วันที่ 14 พ.ค. Anthropic ประกาศโครงสร้างใหม่ของ Claude subscription ที่จะเริ่มมีผล 15 มิ.ย. — **programmatic usage จะถูกแยกออกจาก flat-rate chat subscription** แล้วใช้ระบบ credit รายเดือนแยกต่างหาก คิดเรทแบบ API. ตัวเลขที่ Anthropic ระบุ: Pro ($20/เดือน) ได้ credit ใช้ programmatic $20, Max 5x ($100) ได้ $100, Max 20x ($200) ได้ $200 — หลัก ๆ คือ "credit เท่ากับราคา subscription". เกินจาก credit นี้ต้องเติม pay-as-you-go.

เรื่องนี้คือ **U-turn** จากท่าเดิมเมื่อต้นเดือน เม.ย. — 4 เม.ย. Anthropic ตัดสิทธิ์ Pro/Max subscribers ทั้งหมดในการใช้ subscription กับ third-party agent harness เช่น **OpenClaw** เพราะ Anthropic พบว่า third-party tool ส่วนใหญ่ unoptimized — ปล่อย agent loop ไม่จำกัด ทำให้ token cost บานปลาย. ตัวเลขที่ Anthropic เปิดเผยตอนนั้น: **135,000+ OpenClaw instances** รันอยู่บน Claude subscription — Anthropic คำนวณว่ามัน subsidize usage ที่ไม่ได้ price ไว้ และไม่ sustainable. ครั้งนี้ Anthropic เปลี่ยนใจ — เปิดกลับมา แต่ทุกอย่างที่ไม่ใช่ chat interface ของ Anthropic เองต้องวิ่งผ่าน credit meter.

จังหวะที่ออกข่าวก็เด่นชัด — วันเดียวกับที่ OpenAI ปล่อย **Codex บน ChatGPT mobile app** ฟรีทุก tier และ Axios ตีหัวข้อว่า "Anthropic tightens Claude limits as OpenAI courts agent users". Anthropic กำลังเลือก margin มากกว่า volume — ในขณะที่ OpenAI กำลังเลือก distribution มากกว่า unit economics. นี่คือสองท่าธุรกิจที่ต่างกันชัด.

## ทำไมสำคัญ

สัญญาณใหญ่: **flat-rate subscription model สำหรับ agentic compute ตายแล้ว**. ตอน chat-only ผู้ใช้คนหนึ่งใช้ token ต่อเดือนคำนวณได้ — แต่ agent คือ loop ที่ใช้ token ได้ไม่จำกัด, การจะ price แบบ all-you-can-eat ทำให้ผู้ขาย model ขาดทุนทันทีกับ power user. คาดได้เลยว่า OpenAI, Google, xAI จะเดินตามภายในไตรมาสนี้ — ไม่ทางใดก็ทางหนึ่ง. Cursor และ Windsurf ที่ขาย "unlimited Claude" บน flat $20/month ต้อง renegotiate กับ Anthropic หรือไม่ก็เปลี่ยน pricing เอง.

อีกมุม: นี่เป็นการยอมรับว่า **third-party agent ecosystem แข็งแกร่งพอที่ Anthropic จะไม่กล้าตัดทิ้ง** — 135K OpenClaw instances คือกลุ่มผู้ใช้ที่ committed มาก. ถ้า Anthropic ตัดออกถาวร ผู้ใช้ก็จะย้ายไป Codex / Cursor / Devin ทันที. ดังนั้นโมเดลที่ออกมาคือ "เปิด แต่จ่ายเอง" — Anthropic ยอมขาย token เพิ่มแม้จะรู้ว่ามัน margin ต่ำกว่า chat. ที่ต้องจับตา: API rate สำหรับ Opus 4.7 / Sonnet 4.6 ในโหมด agentic ยังแพงกว่า GPT-5 mini หลายเท่า — ถ้า OpenAI ตัดราคา API agent ลง Anthropic จะอยู่ในสภาพยากทันที.

## มุม OpenBridge

ตรงประเด็น OpenBridge มาก — **ลูกค้า enterprise ที่รัน agent บนหลาย model จะต้องการ cost orchestration layer** ที่บอกว่างานนี้ส่งไป Claude ดี งานนี้ส่งไป GPT ดี และต้อง budget cap ได้รายเดือน. ระบบ credit ใหม่ของ Anthropic ทำให้ cost visibility สำคัญขึ้น — ลูกค้าจะตื่นกลางคืนเพราะ agent run loop กิน credit หมดเดือน. OpenBridge สามารถ position ตัวเองเป็น **"agent FinOps layer"** ที่ route + cap + observe ค่า model spend.

ระดับ tactical: ถ้า OpenBridge ใช้ Claude อยู่ในผลิตภัณฑ์ — ต้อง audit ว่า workload เป็น chat (subscription OK) หรือ programmatic (จะกระทบหลัง 15 มิ.ย.). ถ้าเป็น agent loop ในชื่อลูกค้า ต้อง migrate ไป API หรือ Claude Agent SDK credit ภายในเดือนนี้ ไม่งั้น production จะดับ.

## Sources
- [Anthropic puts Claude agents on a meter across its subscriptions — InfoWorld](https://www.infoworld.com/article/4171274/anthropic-puts-claude-agents-on-a-meter-across-its-subscriptions.html)
- [Anthropic reinstates OpenClaw and third-party agent usage on Claude subscriptions — VentureBeat](https://venturebeat.com/technology/anthropic-reinstates-openclaw-and-third-party-agent-usage-on-claude-subscriptions-with-a-catch)
- [Anthropic tightens Claude limits as OpenAI courts agent users — Axios](https://www.axios.com/2026/05/14/anthropic-claude-price-openai-tokens)
- [Anthropic Splits Claude Subscriptions: What Changes for Indie Hackers on June 15 — DevToolPicks](https://devtoolpicks.com/blog/anthropic-splits-claude-subscriptions-agent-sdk-credit-june-2026)

---

## Audio script
ข่าวที่สอง — Anthropic ปรับโครงสร้าง pricing ของ Claude ใหญ่มาก เริ่ม 15 มิถุนายน. ใครที่รัน Claude ใน agent loop ไม่ว่าจะผ่าน OpenClaw, Agent SDK, หรือ GitHub Actions — จะถูกแยกออกจาก chat subscription แล้วต้องใช้ credit รายเดือนแยก คิดเรทแบบ API. Tier ก็ตรงไปตรงมา: Pro ได้ credit ยี่สิบดอลลาร์, Max 5x ได้หนึ่งร้อย, Max 20x ได้สองร้อย — เกินกว่านี้จ่าย pay-as-you-go. นี่คือการกลับลำจากตอนต้นเดือนเมษายนที่ Anthropic ตัด OpenClaw ทิ้งทั้งหมด ทั้งที่มี instances รันอยู่หนึ่งแสนสามหมื่นห้าพันตัว Anthropic ค้นพบว่า third-party harness ส่วนใหญ่ปล่อย loop ไม่จำกัด ทำให้ subsidize usage ที่ไม่ได้ price ไว้. สัญญาณใหญ่คือ flat-rate subscription สำหรับ agentic compute ตายแล้ว — agent loop ใช้ token ได้ไม่จำกัด การ price แบบ unlimited ทำให้ผู้ขายโมเดลขาดทุน. คาดว่า OpenAI Google และ xAI จะตามมาภายในไตรมาสนี้. มุม OpenBridge: ลูกค้า enterprise ที่รัน agent บนหลายโมเดลจะต้องการ cost orchestration layer บอกว่างานไหนส่งไปไหน และ cap budget รายเดือนได้ เราอาจ position เป็น agent FinOps layer ระดับ tactical ถ้าใช้ Claude ในผลิตภัณฑ์ต้อง audit workload ว่าเป็น chat หรือ programmatic ถ้าเป็น agent loop ในชื่อลูกค้าต้อง migrate ภายในเดือนนี้ไม่งั้น production จะดับวันที่สิบห้ามิถุนายน.
