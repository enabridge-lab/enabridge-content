---
date: 2026-08-26
slug: cognition-devin-40b-valuation-1b-arr
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial isometric illustration of a rocket labeled "DEVIN" launching off a
  laptop keyboard, trailing glowing dollar sign contrails; three floating
  panels stamped with big numbers: "$40B", "$1B ARR", "3 MONTHS". A ghostly
  wireframe silhouette of a developer figure watching from below. Muted deep
  indigo, hot magenta, and neon lime accent palette. Dramatic backlight, 1:1
  aspect. No real human faces (silhouette only). High contrast so text reads
  clearly at 200px thumbnail.
image: images/26-08-26-0617-03-cognition-devin-40b-valuation-1b-arr.png
---

# Cognition คุย $40B valuation แค่สามเดือนหลัง $26B — Devin ทำ $1B ARR, coding agent เป็น category ที่ราคาไม่ยั้ง

## TL;DR
- **12 ส.ค. 2026** Bloomberg + TechCrunch รายงาน **Cognition** (เจ้าของ **Devin**) กำลังคุยรอบ funding ใหม่ที่จะได้ **valuation ≥ $40B** — ขึ้นจาก $26B รอบ May 2026 (สามเดือนที่แล้ว) และ ~$10B ปีที่แล้ว
- Trigger: **ARR แตะ ~$1B** (annualized run rate) ในเดือน ส.ค. — จาก $492M ที่ Scott Wu CEO confirm ตอน May round → doubling ใน 3 เดือน
- Customer list ที่ disclose: **Mercedes-Benz, NASA, Goldman Sachs** ใช้ Devin เป็น autonomous coding agent (ไม่ใช่ copilot suggestion — Devin อ่าน codebase, draft plan, write code, run test, fix bug เองส่วนใหญ่)
- Signal: **coding agent เป็น category ที่ hyperscale เร็วที่สุด**: Anthropic Claude Code ($2.5B ARR), Cognition Devin (~$1B ARR), Cursor ($500M+ ARR reported), OpenAI Codex (3M weekly active dev). รวมแล้ว coding agent อาจโดน $10B+ ARR ทั้ง category ในไตรมาสนี้ — เร็วกว่า category อื่นทุก vertical

## เกิดอะไรขึ้น

**Cognition** (San Francisco, founded 2023 โดย Scott Wu, Steven Hao, Walden Yan) กำลัง open talks กับ investor รอบ funding ใหม่ที่ **valuation ≥ $40 billion** ตาม Bloomberg report ที่ TechCrunch, PYMNTS, และ Dealroom ยืนยัน. รอบก่อนหน้าที่ปิดเมื่อ May 2026 = **$1B ที่ $26B valuation** — และตอนนั้น Wu confirm กับ TechCrunch ว่า ARR อยู่ที่ **$492M**. Bloomberg source ปัจจุบัน say ARR "approaching $1 billion" — doubling ใน ~3 เดือน

ตัวเลขนี้ใหญ่มากเพราะ **Cognition ขายแค่ product เดียว: Devin** — autonomous coding agent ที่ launch ในเดือน มี.ค. 2024 ในฐานะ "world's first AI software engineer" ที่แตกต่างจาก GitHub Copilot / Cursor / Windsurf ตรงที่ Devin **ไม่ใช่ suggestion tool** — เป็น agent ที่รับ task (JIRA ticket, GitHub issue, Slack message) แล้ว **plan → clone repo → edit → run test → PR** เองได้ทั้ง cycle. Developer เห็น log ผ่าน UI ที่คล้าย VS Code + terminal + browser combined, แทรกแซงตอนไหนก็ได้แต่ default คือ agent ทำงานเอง

Devin เจอ backlash หนักตอน launch (คนวิจารณ์ว่า demo cherry-picked, benchmark manipulated) — แต่ปีต่อมา ARR growth บอกว่า enterprise ที่ pay $500/month/dev + enterprise tier ที่ 10-50x นั้น = **ผลลัพธ์ productivity จริง**. Customer ที่ Cognition disclose:
- **Goldman Sachs** — Devin ทำงานเป็น "additional developer" ในทีม engineering, มี Goldman badge, log กิจกรรมเข้า audit trail เดียวกับ human dev
- **Mercedes-Benz** — ใช้ Devin ทำ code migration งานใหญ่ (legacy Java → cloud-native)
- **NASA** — deploy ในทีม flight software (ยังไม่ระบุ mission)

รอบใหม่ที่คุยอยู่ (lead investor ยังไม่เปิด — rumor คือ mix ของ hedge fund + growth crossover investor เพราะ VC ตัวใหญ่รอบก่อนใส่แล้ว) คาด close **ภายในไตรมาสนี้** ก่อน Cognition จะทำ **Windsurf integration** GA (Cognition ซื้อ Windsurf IDE ที่ Google ปล่อยออกจาก reverse acquisition ในกลางปี — deal นี้เพิ่ม developer surface อีก 200-300k). Bloomberg คาดว่ารอบ $40B valuation จะ raise **$500M-$1B fresh capital** เพื่อ hire + compute + acquisition ต่อไป

## ทำไมสำคัญ

Coding agent = **category ที่ economics ดีที่สุดใน agent stack ปัจจุบัน**. เพราะ (1) **ROI คำนวณตรง** — enterprise dev salary $200-400k/year full-cost; agent ที่ทำงานได้เท่า junior/mid dev หนึ่งคนที่ราคา $6-12k/year subscription = 20-50x arbitrage; (2) **outcome measurable** — PR merged, test passing, bug fixed = countable event ที่ CFO อ่านเข้าใจ; (3) **friction to try ต่ำ** — dev อยากลองเอง, ไม่ต้องผ่าน CIO approval หลายเดือน. เทียบกับ agent category อื่น (customer service, legal, sales) ที่ต้องพิสูจน์ CSAT/regulatory/compliance นานกว่า

**Landscape ตอนนี้:**
- **Anthropic Claude Code** — ~$2.5B ARR (ตัวเลขจาก Anthropic filing ตอน Google $40B deal ปลาย เม.ย. — ดู brief 25 เม.ย.)
- **Cognition Devin** — ~$1B ARR ปัจจุบัน (double ในไตรมาสเดียว)
- **Cursor** (Anysphere) — reported $500M+ ARR ปลายปี 2025, คาด $1B ปี 2026 (ยังไม่ update ตัวเลขปัจจุบัน)
- **GitHub Copilot** — ยังใหญ่สุดใน category แต่ Microsoft ไม่ break out ตัวเลข; คาด $2B+ ARR
- **OpenAI Codex** — 3M weekly active dev; Cognizant + CGI enterprise deal เม.ย. 2026; revenue น่าจะแตะ $1B+ ARR ถ้ารวม direct + enterprise partner channels
- **Google Antigravity + Gemini Enterprise coding** — เพิ่งเปิดตัว 24 ส.ค. (ดู brief วันเดียวกัน), ยังไม่มี ARR

รวมแล้ว coding agent category **น่าจะโดน $10B+ ARR รวมภายในไตรมาสนี้** — เร็วกว่า customer service agent (Sierra, Decagon, Ada) ที่รวมกันน่าจะยังอยู่ ~$1-2B; เร็วกว่า voice agent (Sierra, HappyRobot, Vapi) ที่รวมกัน ~$500M-$1B. **Coding = tip of the spear ของ agent monetization**

Signal อีกด้าน: **Cognition $40B ที่ ~$1B ARR = revenue multiple ~40x** — ระดับที่ปกติสงวนไว้ให้ hyperscale software (Salesforce, Snowflake ตอนช่วง IPO) หรือ frontier lab (Anthropic, OpenAI). Investor ยอมจ่าย multiple นี้เพราะเชื่อ 3 สมมติฐาน: (1) Devin ARR จะโตอีก 5-10x ใน 12 เดือน; (2) Cognition จะขยายจาก coding agent → generic engineering agent (data engineering, infra, security) → หาก true = TAM 10x ขึ้น; (3) code = training data ที่ high-value สำหรับ recursive self-improvement — agent ที่ code เก่งขึ้นเรื่อย ๆ เพราะเรียนจาก own PR feedback

## มุม OpenBridge

**Direct implication ต่อ Thai enterprise:** ถ้า Goldman Sachs, Mercedes-Benz, NASA ใช้ Devin เป็น developer จริงในทีม engineering — Thai enterprise ที่ยังใช้ dev outsource (KBank, SCG, PTT, CP Group, True) มี **arbitrage window ใหญ่มาก**. dev outsource Thai/India ที่ราคา $30-80k/year fully loaded คน = agent tier $6-24k/year subscription แทน 1-2 คน = savings 4-8x + ทำงาน 24/7 + ไม่มี attrition. ตลาดนี้ปิดตัวเองภายใน 12-18 เดือน (agent จะกิน share ของ human outsource) — Thai vendor ที่ยังไม่ pivot จะเจอ margin compression

**Direct implication ต่อ OpenBridge product roadmap:** ไม่ควร try build coding agent เอง (แข่งกับ Anthropic + Cognition + Cursor = สู้ไม่ได้). แต่ควร **integrate coding agent เป็น first-class citizen ในหน้าตา orchestration** — เช่น customer พูดกับ OpenBridge orchestrator ว่า "แก้ bug ในระบบ inventory ให้หน่อย" → orchestrator route ไป Devin/Claude Code/Cursor พร้อม context (JIRA, spec, past PR) → รับ PR กลับมา → deploy pipeline. **OpenBridge เป็น glue layer ที่ enterprise Thai** ใช้ให้ coding agent + business agent + integration agent ทำงานประสานกันในภาษาไทย + ตาม compliance ไทย

**Strategic signal:** **agent category ที่มี clear ROI + measurable outcome จะ hyperscale เร็ว** — coding เป็น proof; ถัดไป: legal (contract review), finance (audit + reconciliation), procurement (RFP + vendor management). OpenBridge ควร prioritize vertical agent เหล่านี้เข้าที่ platform โดยเลือก 2-3 vertical ที่ Thai enterprise มี pain ชัด และ ROI 5-10x คำนวณได้ตรง — ไม่ควรเลือก vertical hype (marketing, HR generic) ที่ ROI ยาก measure. คำถามที่ต้องตอบใน 30 วันข้างหน้า: **OpenBridge จะ pick vertical ไหนก่อน?** (แนะนำ: finance/audit reconciliation กับ SME manufacturing — pain ชัด, budget มี, competitor น้อย)

## Sources
- [AI coding startup Cognition reportedly already in talks to raise at $40B valuation (TechCrunch)](https://techcrunch.com/2026/08/12/ai-coding-startup-cognition-reportedly-already-in-talks-to-raise-at-40b-valuation/)
- [Cognition eyes $40B valuation months after reaching $26B (Dealroom)](https://app.dealroom.co/news/note/cognition-eyes-40b-valuation-months-after-26b-raise)
- [Cognition AI Eyes $40 Billion Valuation From New Funding (PYMNTS)](https://www.pymnts.com/news/artificial-intelligence/2026/cognition-ai-eyes-40-billion-valuation-from-new-funding/)
- [AI Coding Startup Cognition Reportedly in Talks for New Funding Round at $40B Valuation (The AI Insider)](https://theaiinsider.tech/2026/08/13/ai-coding-startup-cognition-reportedly-in-talks-for-new-funding-round-at-40b-valuation/)
- [Codex (AI agent) — Wikipedia (background on autonomous coding agent category)](https://en.wikipedia.org/wiki/Codex_(AI_agent))

---

## Audio script
Cognition เจ้าของ Devin กำลัง open talks รอบ funding ใหม่ที่ valuation อย่างน้อย สี่หมื่นล้านเหรียญ. ขึ้นจาก สองหมื่นหกพันล้าน รอบ May 2026 แค่สามเดือนก่อน. Trigger คือ ARR แตะ หนึ่งพันล้าน annualized. จาก สี่ร้อยเก้าสิบสองล้าน ที่ CEO Scott Wu confirm ตอน May round. doubling ใน สามเดือน.

Customer list ที่ Cognition disclose. Goldman Sachs. Mercedes-Benz. NASA. Goldman ให้ Devin ทำงานเป็น additional developer ในทีม engineering. มี Goldman badge. log กิจกรรมเข้า audit trail เดียวกับ human. Mercedes-Benz ใช้ Devin ทำ code migration งานใหญ่ legacy Java เป็น cloud native. NASA deploy ในทีม flight software.

Devin แตกต่างจาก GitHub Copilot Cursor Windsurf. ไม่ใช่ suggestion tool. เป็น agent ที่รับ task JIRA ticket GitHub issue. plan. clone repo. edit. run test. PR. เองทั้ง cycle. developer เห็น log แทรกแซงตอนไหนก็ได้ แต่ default คือ agent ทำงานเอง.

Landscape ตอนนี้. Anthropic Claude Code สองพันห้าร้อยล้าน ARR. Cognition Devin หนึ่งพันล้าน. Cursor ห้าร้อยล้านบวก. GitHub Copilot ประมาณสองพันล้าน. OpenAI Codex สามล้าน weekly active dev. รวมแล้ว coding agent category น่าจะโดน หนึ่งหมื่นล้าน ARR รวมภายในไตรมาสนี้. เร็วกว่า customer service agent เร็วกว่า voice agent. coding เป็น tip of the spear ของ agent monetization.

ทำไมสำคัญ. Coding agent economics ดีที่สุดใน agent stack. ROI คำนวณตรง. dev salary สองแสน สี่แสน per year. agent ที่ทำงานเท่า junior mid dev ราคา หกพัน หนึ่งหมื่นสองพัน per year. arbitrage ยี่สิบถึงห้าสิบเท่า. outcome measurable. PR merged. test passing. bug fixed. CFO อ่านเข้าใจ. friction to try ต่ำ. dev อยากลองเอง ไม่ต้องผ่าน CIO.

Cognition สี่หมื่นล้านที่ หนึ่งพันล้าน ARR. revenue multiple สี่สิบเท่า. investor ยอมจ่ายเพราะเชื่อ. หนึ่ง Devin ARR โตอีก ห้าถึงสิบเท่าในสิบสองเดือน. สอง Cognition ขยายจาก coding เป็น generic engineering agent. data engineering. infra. security. TAM สิบเท่าขึ้น. สาม code เป็น training data high value สำหรับ recursive self improvement. agent ที่ code เก่งขึ้นเรื่อย ๆ.

สำหรับ OpenBridge. Thai enterprise ที่ยังใช้ dev outsource KBank SCG PTT CP True. มี arbitrage window ใหญ่. dev outsource ราคาสามหมื่น แปดหมื่น per year. agent tier หกพันถึงสองหมื่นสี่พัน. savings สี่ถึงแปดเท่า. ทำงาน ยี่สิบสี่ ชั่วโมง. ไม่มี attrition. ตลาดนี้ปิดตัวเองใน สิบสองถึงสิบแปด เดือน.

OpenBridge ไม่ควร build coding agent เอง แข่ง Anthropic Cognition Cursor สู้ไม่ได้. ควร integrate coding agent เป็น first class citizen ในหน้าตา orchestration. customer พูดว่า แก้ bug ในระบบ inventory. orchestrator route ไป Devin Claude Code Cursor พร้อม context. รับ PR กลับ. deploy pipeline. OpenBridge เป็น glue layer.

signal สุดท้าย. agent category ที่มี clear ROI measurable outcome จะ hyperscale เร็ว. coding เป็น proof. ถัดไป legal contract review. finance audit reconciliation. procurement RFP. OpenBridge เลือก vertical ที่ pain ชัด ROI 5 ถึง 10 เท่าคำนวณได้ตรง. finance audit reconciliation กับ SME manufacturing แนะนำก่อน
