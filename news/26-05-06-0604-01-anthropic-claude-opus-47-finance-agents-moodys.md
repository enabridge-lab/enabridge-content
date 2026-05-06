---
date: 2026-05-06
slug: 26-05-06-0604-01-anthropic-claude-opus-47-finance-agents-moodys
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: A bold cream-colored Anthropic squiggle logo sits at the center of a dark navy editorial scene, its lines splitting into ten parallel beams of warm orange light that fan outward into ten silhouetted skyscrapers shaped like Wall Street towers. A muted teal Microsoft 365 hex tile and a coral Moody's "M" badge orbit the squiggle as small connected nodes, with subtle ledger-grid lines arcing between them. A bold sans-serif headline "OPUS 4.7" floats in the upper-left in cream, with the number "64.37%" in coral on the lower-right. Editorial illustration, flat geometric shapes with subtle gradients, slate blue + coral + cream palette on deep navy, dramatic side-lighting from the squiggle outward, 1:1 aspect.
image: images/26-05-06-0604-01-anthropic-claude-opus-47-finance-agents-moodys.png
---

# Anthropic ships the JV's product on Day 2 — Claude Opus 4.7 + 10 banking agents + Moody's MCP + Microsoft 365

## TL;DR
- หนึ่งวันหลังประกาศ JV $1.5B กับ Blackstone/H&F/Goldman, Anthropic เปิด **Claude Opus 4.7** + library 10 finance agents + Moody's MCP app (600M companies) + Microsoft 365 native — ใน briefing ปิดที่ NY ที่ Jamie Dimon มาเอง
- **Vals AI Finance Agent benchmark: Opus 4.7 = 64.37%** ขึ้นนำอุตสาหกรรม — เป็นครั้งแรกที่ frontier model ออกมาพร้อม benchmark วงในของ buy-side
- Pattern: Anthropic ใช้ JV เป็น distribution + pricing layer แต่ ship "product surface" ออกตรง — ไม่รอ services arm สร้างเอง

## เกิดอะไรขึ้น

วันที่ 4 พฤษภาคม Anthropic ประกาศ JV $1.5B กับ Blackstone, Hellman & Friedman, Goldman Sachs เพื่อทำ enterprise AI services firm — สื่ออ่านว่าเป็น "shot at consulting industry" วันต่อมา 5 พฤษภาคม ที่ briefing ปิดในนิวยอร์ก Anthropic เปิดสิ่งที่ JV จะขาย: **Claude Opus 4.7** model ใหม่ + library ของ pre-built finance agent ราว 10 ตัว + Moody's native app + integration ลึกใน Microsoft 365 — ทั้งหมดในวันเดียว

Opus 4.7 เปิดมาพร้อม **score 64.37% บน Vals AI Finance Agent benchmark** ซึ่งเป็น benchmark ใหม่ที่ buy-side firm ใช้ทดสอบ agent บน workflow ของ asset manager จริง — credit memo, earnings analysis, pitchbook generation, KYC, month-end close — ตัวเลขนี้สูงกว่ารุ่นที่ Anthropic ออกครั้งก่อนระดับ ~10pp และนำหน้า GPT-5.5 บน task เดียวกัน Anthropic ระบุชัดว่า model นี้ "tuned สำหรับ financial work" ไม่ใช่ frontier general — สัญญาณว่าค่ายเริ่ม fork model spec ตาม vertical

ประเด็นใหญ่กว่า model คือ **distribution layer สามชั้นที่ Anthropic ปลดล็อกพร้อมกัน**: (1) **Microsoft 365 native** — Claude finance agent ทำงานใน Excel, Outlook, Teams โดยไม่ต้อง switch app, ลูกค้า enterprise จะเห็น Claude เป็น tab ใน Office ribbon โดยตรง (2) **Moody's Agentic Solutions MCP app** — Moody's เอา dataset 600 ล้านบริษัท + credit/compliance workflow มาเปิดเป็น native MCP app ใน Claude — agent ของ Anthropic เรียก Moody's primary data ได้โดยไม่ต้อง integration project แยก (3) **FIS deployment ที่ BMO + Amalgamated Bank** สำหรับ AML investigator agent (ดูใน brief #2)

สิ่งที่ทำให้ทั้งหมดดูจัดวางมา: **Jamie Dimon ของ JPMorgan** ปรากฏในงานแล้วให้ endorsement ว่า Claude เป็น "the most capable financial AI we've tested" — แม้ JPM ไม่ใช่ founding partner ของ JV แต่การออกหน้าครั้งนี้ทำให้ Anthropic จับ G-SIB ใหญ่สุดของอเมริกาเป็น reference customer ได้ก่อนคู่แข่ง

## ทำไมสำคัญ

นี่คือ moment ที่ frontier lab **ตัดสินใจขายเป็น product มากกว่า model API** อย่างชัดเจน — และเลือกตลาดแรกคือ financial services ซึ่งเป็น vertical ที่ regulated หนัก, willingness-to-pay สูง, workflow ซับซ้อน, และ data gravity อยู่กับ proprietary vendor (Moody's, Bloomberg, FIS, Refinitiv) ไม่ใช่ open web ตำแหน่งของ Anthropic เลยไม่ใช่แค่ "Claude API + คู่มือ" แต่เป็น "Claude as the operating layer สำหรับ analyst desk" ที่มี MCP เป็น primitive เชื่อมต่อ data vendor — คู่ที่จะเจ็บที่สุดไม่ใช่ OpenAI แต่เป็น **Bloomberg Terminal** ($30k/seat/year) และ **FactSet/Refinitiv** ที่ขาย data บวก thin workflow มา 30 ปี

เทียบกับ OpenAI ที่ counter ด้วย PwC partnership (brief #3) ความแตกต่างชัด — OpenAI เลือกขายผ่าน **services delivery partner** ที่มี relationship CFO อยู่แล้ว, Anthropic เลือกขายผ่าน **vertical software stack** (Moody's, FIS, Microsoft 365) ที่มี data + workflow primitives อยู่แล้ว — strategy ของ Anthropic ทำให้ unit economics ดีกว่า (ไม่ต้องแบ่งกับ services firm) แต่ scale ช้ากว่า เพราะต้องรอ partner ship integration เอง

Signal สำคัญที่สุดคือ **vertical model fork** — Opus 4.7 ที่ tune มาเฉพาะ finance ทำให้ benchmark ใหม่ระดับ 64.37% เปิดทาง Anthropic ออก "Opus for Healthcare", "Opus for Legal", "Opus for Manufacturing" ในไตรมาสถัดไปได้ทันที pattern เดียวกับ Sierra ที่ออก vertical agent — แต่ทำที่ระดับ model spec แทน application layer

## มุม OpenBridge

**ข้อสำคัญที่สุดสำหรับ OpenBridge: MCP กลายเป็น distribution layer แทน "API integration" รุ่นเก่า** — Moody's เอา 600M company dataset มา ship เป็น MCP app ภายใน 6 เดือนหลัง spec เปิด เพราะ effort ต่ำกว่า build connector ของ tool เฉพาะ ถ้า OpenBridge ยังคิด integration เป็น "REST + OAuth + retry policy" — กำลังจะตกขบวน รอบ procurement หน้า ลูกค้าจะถามว่า "MCP app ของคุณอยู่ที่ไหน" ไม่ใช่ "API doc อยู่ที่ไหน"

Action ตรง: (1) **publish OpenBridge MCP server** ที่ expose data primitive (workflow run, audit log, integration metadata) เป็น MCP tool — agent ของลูกค้าเรียกได้โดยไม่ต้อง custom integration project (2) **partnership scout ระดับ vertical** — เลือก data/SaaS player 1 รายต่อ vertical ที่ OpenBridge อยากเข้า (เช่น healthcare = Epic/Veeva, finance = MSCI/S&P) แล้วเสนอ co-build MCP app ก่อนคู่แข่งจอง slot (3) **positioning ใหม่** — แทนที่จะ pitch "integration platform" ลอง pitch "MCP application gateway สำหรับ enterprise" — Claude/GPT จะ orchestrate, OpenBridge จะ expose tool + governance

## Sources
- [Anthropic deepens push into Wall Street with new AI agents (Fortune)](https://fortune.com/2026/05/05/anthropic-wall-street-financial-services-agents-jamie-dimon/)
- [Anthropic ships ten financial-services agents and pulls Opus 4.7 (TNW)](https://thenextweb.com/news/anthropic-financial-services-agents-claude-opus-4-7-fis)
- [Agents for financial services and insurance (Anthropic)](https://www.anthropic.com/news/finance-agents)
- [Moody's brings credit and compliance workflows directly into Claude (Moody's)](https://www.moodys.com/web/en/us/media-relations/press-releases/moodys-brings-credit-and-compliance-workflows-directly-into-anthropics-claude.html)
- [Anthropic Targets Financial Services Space With New AI Agents (PYMNTS)](https://www.pymnts.com/news/artificial-intelligence/2026/anthropic-targets-financial-services-space-with-new-ai-agents/)

---

## Audio script
วันที่ห้าพฤษภาคมเป็นวันที่ Anthropic ทำสิ่งที่ครั้งแรกในประวัติศาสตร์อุตสาหกรรม. หนึ่งวันหลังประกาศ joint venture หนึ่งจุดห้าพันล้านเหรียญกับ Blackstone และ Goldman. เขา ship ทุกอย่างที่ JV จะขายภายในยี่สิบสี่ชั่วโมง. โมเดลใหม่ Claude Opus 4.7 ที่ tune มาเฉพาะ finance ออกมาด้วย benchmark หกสิบสี่จุดสามเจ็ดเปอร์เซ็นต์บน Vals AI ขึ้นนำอุตสาหกรรม. พร้อมกัน library ของ agent สำเร็จรูปสิบตัวสำหรับงาน analyst. ครอบ credit memo, KYC, pitchbook, month-end close ครบ. และที่หนักกว่านั้น Moody's เอา dataset หกร้อยล้านบริษัทมา ship เป็น MCP application native ใน Claude. แปลว่า agent เรียก Moody's primary data ได้ตรงไม่ต้อง integration project. Microsoft 365 ก็ embed เข้าไปใน Excel, Outlook, Teams. Jamie Dimon ของ JPMorgan ขึ้นเวที endorsement ว่าเป็น financial AI ที่ดีที่สุดที่เขาเคยเทสต์. มุมที่น่าสนใจคือ Anthropic เลือก strategy ต่างจาก OpenAI ที่ขายผ่าน services partner แบบ PwC. Anthropic ขายผ่าน vertical software stack คือ Moody's, FIS, Microsoft. pattern ที่ทุกค่ายเห็นพ้องกันคือ MCP กลายเป็น distribution layer ใหม่. ใครยัง integration แบบเดิม REST plus OAuth กำลังตกขบวน. ลูกค้ารอบหน้าจะถามว่า MCP app อยู่ไหน ไม่ใช่ API doc อยู่ไหน.
