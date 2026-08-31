---
date: 2026-09-01
slug: 26-09-01-0614-01-mckinsey-state-ai-agentic-coding-eats-saas
topic: openbridge-trend
reading_time_min: 5
sources: 3
image_prompt: |
  A tall SaaS invoice on a glass desk being sliced diagonally by a glowing
  bright green "AGENT BUILD" beam; three stacked headline numbers dominate the
  frame — "32% SKIP BUY", "27% → 40% SCALE", "41% TECH". A silhouetted CFO
  figure walks away from the invoice. Editorial isometric style, high contrast
  navy background with mint accents, crisp sans-serif numbers readable in 200px
  thumbnail, 1:1 aspect, no real human faces.
image: images/26-09-01-0614-01-mckinsey-state-ai-agentic-coding-eats-saas.png
---

# McKinsey State of AI 2026 — 32% เอนเทอร์ไพรส์ยกเลิกซื้อซอฟต์แวร์เพราะ agentic coding, agent scaling 27→40% ในหนึ่งปี

## TL;DR
- McKinsey สำรวจ 1,719 ผู้บริหารทั่วโลก: **32% ตัดสินใจไม่ซื้อ software product/feature เพราะ build เองด้วย agentic coding tool ได้** — sector เทคโนโลยีสูงถึง **41%**
- Enterprise ($1B+ revenue) ที่ scale agent ใน 1+ function โต **27% → 40% ในหนึ่งปี**, บริษัทเล็กแบน 22%
- Chui (McKinsey QuantumBlack): ROI สอดคล้อง historical adoption curve — 37% รายงาน "some EBIT impact" (flat vs 2025), แต่ high performer แค่ 6%

## เกิดอะไรขึ้น

25 ส.ค. McKinsey ปล่อย **State of AI 2026** ที่รวมข้อมูลจาก 1,719 executive ทั่วโลก. ตัวเลขที่ทำให้ SaaS CFO ทั้งอุตสาหกรรมต้องอ่านซ้ำคือ **32% ของ respondent ตัดสินใจไม่ซื้อ software product หรือ feature ในปีที่ผ่านมา เพราะทีมภายในใช้ agentic coding tool build เองได้เร็วพอ** — ตัวเลขเทค sector โผล่ที่ **41%** อ่านตรงตัวคือ **4 ใน 10 tech company ยกเลิกไปแล้ว 1+ software vendor**.

คู่กันคือตัวเลข scaling ของ enterprise ตัวจริง: บริษัทรายได้ **$1B+ ที่ scale agent อย่างน้อย 1 function** โตจาก **27% (2025) → 40% (2026)** ในเวลาแค่ 12 เดือน; บริษัทเล็กกลับ **flat ที่ 22%** — ช่องว่างระหว่าง large vs SMB adoption กว้างขึ้น (18 pp) ไม่ใช่แคบลง. Michael Chui, senior fellow ที่ QuantumBlack, บอก The Register ว่า "Some ROI is already being achieved, and we expect more over time. It's a journey, not a destination" พร้อมยอมรับว่า timeline **สะท้อน adoption curve ของเทคโนโลยีอื่นในอดีต** — ไม่ใช่ hype cycle แต่เดิน slope ตามปกติ.

รายงานเสริมด้วย reality check: **37% รายงาน "at least some EBIT impact" จาก AI** — flat จากปี 2025, **แค่ 6% qualify เป็น "high performers"** (5%+ EBIT + significant impact rating), **80% ของ individual user รายงาน personal productivity ดีขึ้น** แต่ **20% ชี้ว่า operating cost ของ AI เป็นตัวเบรกการขยาย**. อีกด้านหนึ่ง **53% ของ leader ยังเชื่อว่า AI เป็น "support tool" ในอีก 1-2 ปี**, มีแค่ **25% ที่คิดว่า agentic AI จะทำงาน autonomous เคียงข้าง employee** — เป็น narrative ที่แตกจาก vendor-side hype อย่างชัดเจน.

## ทำไมสำคัญ

ตัวเลข 32% skip-software-purchase คือ **first hard data ว่า agentic coding เริ่มกิน SaaS TAM จริง** — ไม่ใช่ theoretical risk. ที่น่ากลัวกว่าคือ **41% ใน tech sector** — sector ที่ตัวเองสร้าง SaaS มาขายคนอื่น ตอนนี้เลือก build เองเพราะ Claude Code / Cursor / Devin / Codex ทำให้ marginal cost ของการ build feature ตกลงมาระดับ "ทำเองภายในสัปดาห์ vs subscription $50-500/seat/mo x หลายร้อย seat". Pattern นี้ replicate scenario ที่ Salesforce เจอกับ Notion + LangChain + a bunch of AI tools ที่ mid-market ใช้ build lightweight CRM แทนการซื้อ enterprise seat.

ที่ต้อง pair คือ scaling gap 27→40% ของ enterprise vs SMB flat: **large enterprise มี capacity to scale agent** (engineering team + platform + governance) ในขณะที่ SMB ไม่มี — ซึ่งแปลว่า SMB จะเป็น **buyer ของ managed agent platform ที่ turnkey กว่า** ไม่ใช่ builder. Pattern นี้ตรงข้ามกับสมมติฐาน early-2025 ว่า SMB จะ leapfrog enterprise ด้วย no-code agent — ในความเป็นจริง governance + integration + reliability requirement มัน bar สูงพอที่ small team ไม่มี bandwidth ทำเอง จึงต้อง outsource ไปที่ platform vendor. ข้อสังเกตนี้ผสมกับ AccuKnox AgentZ (เมื่อวาน) + Aziron ของ Aziro (28 ส.ค.) + Salesforce Agentforce ที่ scale ตรง — เห็น shape ของ market ชัดขึ้น: **enterprise build + operate เอง, SMB ซื้อ managed platform**.

## มุม AI Agent Platform

**สำหรับ builders ของ agent platform:** ผู้ที่ target enterprise ($1B+ revenue) ต้อง **ขาย operating layer** (governance, observability, cost budget, credential vault) มากกว่าขาย "framework" — เพราะ enterprise เหล่านี้ build agent เองอยู่แล้ว, ที่ pain point ที่จ่ายเงินคือการ scale จาก 5 agent → 50 agent ในลักษณะที่ security signs off. ผู้ที่ target SMB ต้อง **turnkey vertical app** ที่ time-to-value < 30 วัน, ยอมรับ trade-off ของ flexibility เพื่อ speed + reliability. ผู้ที่ยัง target "middle" (mid-market $100M-1B) จะโดนบีบสองด้าน. **สำหรับ businesses ที่จะ deploy agent:** ก่อนต่อสัญญา SaaS ปีถัดไป ทำ build-vs-buy audit ทุก vendor $10K+/yr — คำถามใหม่คือ "feature นี้ agent build ได้ใน 2 สัปดาห์มั้ย" ไม่ใช่ "vendor นี้ดีที่สุดในตลาดมั้ย". **สำหรับ ecosystem:** SaaS pure-play vendor ที่ไม่มี agent hook (คือขาย workflow feature ที่ Claude/GPT build ได้ตรง ๆ) จะเจอ renewal drag ในไตรมาสถัด ๆ ไป; vendor ที่ position ตัวเองเป็น **infrastructure ที่ agent เรียกใช้** (data layer, identity, payment rail, observability) กลับได้ประโยชน์เพราะ agent build เองก็ยังต้องเรียกของเหล่านั้น.

Enabridge ตรงกลาง: มีทั้ง SEA enterprise (BBL, KBank, SCB, PTT scale) ที่กำลัง scale agent 5→13+, และ SEA SMB (retail chain, distributor, insurance broker) ที่ต้อง turnkey. ทางเดินคือ **สอง product line**: (1) **AgentOS สำหรับ enterprise** — governance-first, on-prem/BYO-compute option, integrate เข้า banking core / SAP; (2) **AgentPack สำหรับ SMB** — vertical template (Thai retail POS, restaurant, freight forwarder, insurance renewal) ที่ deploy < 30 วัน, ราคา per-outcome. Cross-sell คือ agent skill / connector library ที่ share ระหว่างสอง tier ผ่าน registry เดียวกัน.

## Sources
- [McKinsey says enterprise AI is finally 'on the road to ROI' — The Register](https://www.theregister.com/ai-and-ml/2026/08/25/mckinsey-says-enterprise-ai-is-finally-on-the-road-to-roi/5292388)
- [Nearly 32% of organizations decide to build in-house software using AI coding agents over purchases: McKinsey — India Gazette](https://www.indiagazette.com/news/279274436/nearly-32-of-organizations-decide-to-build-in-house-software-using-ai-coding-agents-over-purchases-mckinsey)
- [State of AI trust in 2026: Shifting to the agentic era — McKinsey](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/tech-forward/state-of-ai-trust-in-2026-shifting-to-the-agentic-era)

---

## Audio script
McKinsey เพิ่งปล่อย State of AI 2026 มีตัวเลขที่ต้องตกใจ 32 percent ของบริษัทที่สำรวจ 1,719 องค์กรทั่วโลก ตัดสินใจไม่ซื้อ software product หรือ feature ในปีที่ผ่านมา เพราะทีมภายในใช้ agentic coding tool build เองได้เร็วพอ ยิ่งถ้าดูเฉพาะ tech sector ตัวเลขพุ่งไป 41 percent แปลว่า 4 ใน 10 tech company ยกเลิกไปแล้ว 1 vendor ขึ้นไป ตัวเลขที่สองที่ต้องจำคือ enterprise รายได้ 1 billion dollar ขึ้นไป ที่ scale agent ใน 1 function เป็นอย่างน้อย โตจาก 27 เป็น 40 percent ในหนึ่งปี ขณะที่บริษัทเล็ก flat ที่ 22 percent ช่องว่างกว้างขึ้น 18 percentage point ในปีเดียว signal ที่ Enabridge ต้องอ่านคือ agentic coding เริ่มกิน SaaS TAM จริง ไม่ใช่ theoretical เพราะฉะนั้นถ้าเราขาย platform ต้องแบ่งเป็น 2 tier ชัดเจน enterprise ขาย operating layer governance observability cost budget เพราะเขา build agent เองอยู่แล้ว SMB ขาย turnkey vertical app time-to-value ต่ำกว่า 30 วัน ก่อนต่อสัญญา SaaS ปีหน้า ทุกบริษัทควรทำ build-vs-buy audit ทุก vendor 10,000 dollar ต่อปีขึ้นไป คำถามเปลี่ยนไปแล้วจาก vendor นี้ดีที่สุดมั้ย เป็น feature นี้ agent build ได้ใน 2 สัปดาห์มั้ย
