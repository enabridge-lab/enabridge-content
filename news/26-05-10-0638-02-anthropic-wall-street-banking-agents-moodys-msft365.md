---
date: 2026-05-10
slug: anthropic-wall-street-banking-agents-moodys-msft365
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: A hero illustration of the Anthropic Claude logo and the JPMorgan Chase emblem facing each other across a marble Wall Street trading floor, connected by ten glowing data streams labeled with finance icons (KYC, ledger, pitchbook, earnings). Above them, in massive bold condensed sans-serif white text overlaid on the dark navy ceiling: "10 AGENTS · $30B ARR". A small Microsoft Excel logo and a Moody's logo sit on a desk in the foreground, glowing as data flows through them. Editorial cover-art composition, dramatic spotlight, dark navy and gold palette with high contrast, magazine cover style, 1:1 aspect, no real human faces (silhouette of two executives walking on stage in deep background allowed).
image: images/26-05-10-0638-02-anthropic-wall-street-banking-agents-moodys-msft365.png
---

# Anthropic เปิด 10 banking agent + Microsoft 365 + Moody's data — Dario กับ Jamie Dimon ขึ้นเวทีร่วมก่อน IPO ฤดูใบไม้ร่วง

## TL;DR
- 5 พ.ค. 2026 ที่งาน "Briefing: Financial Services" (NYC, invite-only) Anthropic เปิด **10 pre-built agent template** สำหรับ research/operations/finance งาน — pitch builder, earnings reviewer, financial model builder, GL reconciler, month-end closer, statement auditor, KYC screener ฯลฯ — พร้อม **Claude Opus 4.7** ที่ tune สำหรับ financial work
- Plug Microsoft 365 ตรง (Excel/PowerPoint/Word add-in, Outlook ตามมา) — context carry across apps automatic; **Moody's integration** ใส่ credit rating + 600M+ company data เข้า workflow ตรง
- Dario Amodei กับ Jamie Dimon ขึ้นเวทีร่วมครั้งแรก — Claude อยู่ production ที่ **JPMorgan Chase / Goldman Sachs / Citi / AIG / Visa**; run-rate revenue Anthropic **$30B** (จาก $9B ปลาย 2025)
- Move นี้ก่อน IPO Anthropic ฤดูใบไม้ร่วง 2026 — vertical-specific deployment + bank logo บน slide = signal ว่า agentic AI ผ่าน "experimentation" ไป "infrastructure ของ financial services" แล้ว

## เกิดอะไรขึ้น

วันที่ 5 พ.ค. 2026 ที่ Manhattan Anthropic เปิด event invite-only ชื่อ "Briefing: Financial Services" สำหรับ executive ของ bank โลก — และจัด keynote ที่ห้ามคิดมาก่อนว่าจะเกิด: **Dario Amodei กับ Jamie Dimon ขึ้นเวทีร่วมเป็นครั้งแรก** Dimon ถ้ามองในประวัติเป็น CEO bank ที่ skeptical AI hype มากที่สุดคนหนึ่ง; การมายืนข้าง Anthropic บอก signal ตรงว่า phase ของ "ลอง POC" ของ Wall Street จบไปแล้ว

ของที่ปล่อย: **10 agent template สร้าง pre-built** สำหรับงานที่ analyst กับ ops staff ของ investment bank ใช้เวลาเยอะที่สุด — ฝั่ง research มี pitch builder ที่ generate comps + draft pitchbook, meeting prep tool, earnings reviewer ที่อ่าน transcript flag model update ที่ต้องแก้, financial model builder; ฝั่ง operations มี general ledger reconciler, month-end closer, financial statement auditor และ KYC screener ที่ assemble entity file + package escalation ให้ทีม compliance ทุก template build บน **Claude Opus 4.7** model ใหม่ที่ Anthropic claim ว่า capable ที่สุดสำหรับ financial work

ของอีกชิ้นที่ดึงคนซื้อมาก: Claude integrate ตรงเข้า Microsoft 365 ผ่าน add-in สำหรับ Excel / PowerPoint / Word (Outlook ตามมา) — สร้าง model ใน Excel แล้วเปิด PowerPoint ทำ deck ต่อ context ตามไปเอง ไม่ต้อง re-explain งาน อีก partnership ที่หนัก: **Moody's** เปิด proprietary credit rating + data ของ 600M+ บริษัทเข้า Claude direct — workflow ของ analyst ขอ rating + supporting data ภายในประโยคเดียว ไม่ต้อง switch แอป

หลัง briefing Anthropic เปิดเผยว่า Claude อยู่ production ที่ **JPMorgan Chase, Goldman Sachs, Citi, AIG, Visa** และอีกหลายเจ้า รายงานอีกข่าว: **Anthropic run-rate revenue แตะ $30B แล้ว** จาก ~$9B ปลายปี 2025 — โต ~3.3x ใน 5 เดือน Move ทั้งหมดนี้ก่อน IPO ที่คาดว่าจะเกิดฤดูใบไม้ร่วง 2026

## ทำไมสำคัญ

Pattern ที่ชัดที่สุดคือ Anthropic เลือก **vertical depth ก่อน horizontal breadth** ขณะที่ OpenAI ยัง broaden Frontier Workspace เป็น productivity tool ทุก vertical Anthropic ใช้กลยุทธ์ Salesforce ปี 2002 — เลือกหนึ่ง vertical (financial services) build template เฉพาะ + partnership ข้อมูล (Moody's) + จับมือ logo ใหญ่ที่สุด (JPMorgan) + ขึ้นเวทีคู่ CEO เป็น proof-of-trust สำหรับ buyer ฝั่งระมัดระวัง การมี 10 template + Microsoft 365 integration + bank data = ลูกค้าซื้อเป็น "financial AI suite" ไม่ใช่ "model API" — ซึ่งกำหนด pricing ที่ unit ของ workflow ไม่ใช่ token

ตัวเลข $30B run-rate revenue (จาก $9B ใน 5 เดือน) เป็นอัตราการโตที่ enterprise SaaS ไม่เคยเห็นในประวัติศาสตร์ Stripe + Snowflake รวมกันยังไม่เคยทำ — และยังต้องระวังว่าตัวเลข run-rate Anthropic อาจ inflate จาก prepaid commitment ของ enterprise buyer (pattern เดียวกับ snowflake unused capacity ปี 2022) แต่แม้จะ adjust สัดส่วน 30-40% ก็ยังเป็น category สูง JPMorgan-Anthropic alliance + Moody's data integration บอกตรงว่า **financial services เป็น vertical แรกที่ AI agentic จะ "win first" แบบ end-to-end** — และผลกระทบ second-order ตรงต่อ Bloomberg, FactSet, S&P Global ที่ขายข้อมูลแบบ legacy seat license

อีก signal ที่ underrated: timing IPO อาจเป็นเหตุผลตรงที่ทำเรื่องนี้ตอนนี้ — bank deployment + Microsoft 365 integration + Moody's = three checkpoint ที่ S-1 จะใช้ฉาย "enterprise revenue ที่ deep + sticky" ไม่ใช่ "consumer ChatGPT-style top of funnel" ทุก institutional investor อ่าน S-1 จะคุ้มค่ามากกว่าตัวเลข run-rate อย่างเดียว

## มุม OpenBridge

Vertical-first strategy ของ Anthropic เป็น playbook ที่ OpenBridge ควร mimic — เลือก **1-2 vertical Thai/SEA enterprise** (banking + insurance น่าจะเป็น natural choice เพราะข้อมูลปริมาณมาก + workflow มี pattern ชัด) แล้ว build connector pack + sample agent template เฉพาะ vertical นั้น แทนการขาย "MCP server ทั่วไป" Move นี้ทำให้ deal cycle สั้นลงเพราะ buyer เห็น artifact พร้อมใช้ ไม่ใช่ infrastructure

อีกประเด็น: Microsoft 365 + Moody's integration บอกว่า **agent platform ชนะที่ "context flow ระหว่าง app"** ไม่ใช่ที่ feature ของ app เดียว สำหรับ OpenBridge นี่คือ thesis core — เราอยู่ที่ junction ของ enterprise SaaS multi-source การที่ Anthropic spend ทรัพยากรขนาดนี้ build add-in เข้า Excel/Word/PowerPoint บอกตรงว่า "context carry across apps" คือ moat ที่ใหญ่จริง OpenBridge ควร **emit "context handoff metadata"** ที่ agent ใช้ swap context across SaaS app ของลูกค้าได้โดยอัตโนมัติ; ลูกค้า ServiceNow + Salesforce + Workday + SAP ทุก seat ของไทยมี pattern เดียวกัน

ส่วนเรื่อง Moody's-style data partnership ตรงๆ — OpenBridge ควรไปคุย local data provider (SET, set-data, Wisesight, SCBX/KBank/SCB credit data, NSO) ถ้ามี exclusive integration กับ source ใดส่วนใดที่ unique ใน SEA agent platform ของ frontier vendor ต้องผ่าน OpenBridge เพื่อแตะ data นั้น = pricing power ที่ generic MCP server ไม่มี

## Sources
- [Anthropic deepens push into Wall Street with new AI agents, full Microsoft 365 integration, Moody's data partnership — Fortune](https://fortune.com/2026/05/05/anthropic-wall-street-financial-services-agents-jamie-dimon/)
- [Anthropic deepens its ties to Wall Street with new partnerships, tools — Axios](https://www.axios.com/2026/05/05/anthropic-wall-street-dimon-amodei)
- [Anthropic Unveils AI Agents to Field Financial Services Tasks — Bloomberg](https://www.bloomberg.com/news/articles/2026-05-05/anthropic-unveils-ai-agents-to-field-financial-services-tasks)
- [Anthropic rolls out financial services agents as arms race with OpenAI heats up — InvestmentNews](https://www.investmentnews.com/fintech/anthropic-rolls-out-financial-services-agents-as-arms-race-with-openai-heats-up/266445)
- [Agents for financial services — Anthropic](https://www.anthropic.com/news/finance-agents)

---

## Audio script
สวัสดีครับ Yoh ที่ New York วันที่ 5 พฤษภา Anthropic จัด event ให้ executive bank โลก และจัด keynote ที่ Dario Amodei กับ Jamie Dimon ขึ้นเวทีร่วมเป็นครั้งแรก สิ่งที่ปล่อย คือ 10 pre-built agent template สำหรับงาน financial — pitch builder, earnings reviewer, GL reconciler, KYC screener — รัน บน Claude Opus 4.7 ที่ tune มาเฉพาะงาน finance พร้อม integrate ตรงเข้า Microsoft Excel PowerPoint Word — context carry across app อัตโนมัติ และ partner กับ Moody's เปิดข้อมูล credit rating + 600 ล้านบริษัทเข้า workflow ตรง Claude อยู่ production ที่ JPMorgan, Goldman Sachs, Citi, AIG, Visa และ run-rate revenue ของ Anthropic แตะ 30 พันล้านดอลลาร์ จาก 9 พันล้านปลายปีที่แล้ว โต 3.3 เท่าใน 5 เดือน pattern ชัดคือ Anthropic เลือก vertical depth ก่อน horizontal breadth — playbook Salesforce ปี 2002 + ทำก่อน IPO ฤดูใบไม้ร่วง สำหรับ OpenBridge insight คือเราต้องเลือก vertical Thai/SEA หนึ่ง-สอง แล้วสร้าง connector + agent template เฉพาะ vertical แทนการขาย MCP server ทั่วไป และคุยกับ data provider ท้องถิ่นเพื่อทำ Moody's-style exclusive integration ครับ
