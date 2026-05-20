---
date: 2026-05-11
slug: 26-05-11-0606-01-uber-claude-code-34b-ai-budget-burn
topic: use-case
reading_time_min: 4
sources: 5
image_prompt: |
  A massive corporate budget envelope marked "UBER 2026 AI BUDGET — $3.4B" being
  rapidly consumed by stylized flames shaped like terminal cursors and code
  brackets, with a glowing Anthropic Claude Code logo at the center. Calendar
  pages reading "JAN→APR" flutter away in the fire. In the foreground, a wall
  chart shows a steep usage curve labeled "84% engineers agentic, 11% PRs by AI"
  with bold numbers. Composition: editorial business-magazine illustration,
  slightly satirical, cinematic dramatic lighting, deep navy and ember-orange
  palette, high contrast for thumbnail readability, 1:1 aspect, no human faces.
image: images/26-05-11-0606-01-uber-claude-code-34b-ai-budget-burn.png
---

# Uber เผางบ AI ทั้งปี 2026 ใน 4 เดือน — Claude Code กลายเป็น cost center ใหม่ที่เลิกใช้ไม่ได้

## TL;DR
- Uber CTO Praveen Neppalli Naga ยอมรับว่าใช้งบ AI 2026 ทั้งก้อนหมดภายในเดือนเมษายน — annual R&D spend $3.4B รวมอยู่ในเฟรมงานนั้น; Claude Code adoption พุ่งจาก 32% ของ developer เดือน ธ.ค. 2025 เป็น 84% ในเดือน มี.ค. 2026
- ตัวเลข productivity: ~11% ของ PR ทุกตัวที่ Uber ตอนนี้เปิดโดย AI agent, ~11% ของ live backend code update เขียนโดย AI system รวมถึง ride-matching, dynamic pricing, bug fix — ต้นทุนต่อ engineer $500–$2,000/เดือน
- CTO บอก "back to the drawing board" บน budgeting — token-based pricing ของ Claude Code (ไม่ใช่ flat per-seat) ทำให้ cost scale แบบ non-linear ตาม parallel agent run และ workflow complexity

## เกิดอะไรขึ้น

ในรอบสัปดาห์ที่ Hacker News front-page วาง story นี้ค้างไว้สามวัน, **Uber กลายเป็น public proof point แรกของยุค "agentic coding ราคาแพงเกินจะตั้งงบ"** — Praveen Neppalli Naga, CTO ของ Uber, ออกมาพูดเปิด ๆ ว่า budget AI ปี 2026 ของบริษัทถูกใช้หมดภายในสี่เดือน ตัวเลขรายงานที่ Yahoo/Finance หยิบมาคือ Uber spend $3.4B กับ R&D และ AI ในส่วนนี้ใหญ่พอจะเป็น line item ตัวที่บริหารระดับบอร์ดต้องตอบคำถามนักลงทุน

ตัว driver หลักคือ Claude Code ของ Anthropic — adoption rate ที่ Uber เริ่มที่ 32% ของ developer ในเดือน ธ.ค. 2025, ขึ้นเป็น 63% ในเดือน ก.พ., แล้ว 84% ในเดือน มี.ค. 2026 ตามข้อมูลที่ Uber engineering share — และที่สำคัญกว่าคือ output: ตอนนี้ ~11% ของ pull request ทุกตัวที่ merge เข้า codebase ของ Uber ถูกเปิดโดย AI agent, และ ~11% ของ live backend code update รวมถึง algorithm ของ ride-matching, dynamic pricing engine, และ bug fix mass-scale มาจาก agent ทำงานเอง engineer แต่ละคนรายงาน API cost ต่อเดือนระหว่าง $500–$2,000 — เลขที่กระจายตาม project ใหญ่ ที่มี parallel agent หลายตัวรัน continuous integration

ที่ทำให้ story นี้คม คือ **economic model ของ Claude Code ไม่ใช่ per-seat แบบ Copilot/Cursor original — มันคือ token-based pricing** ที่ Anthropic ปรับมาตั้งแต่ปลายปีก่อน เมื่อ engineer 84% เริ่ม run agent หลายตัวพร้อมกัน (sub-agent + Outcomes + Multi-Agent Orchestration ที่ Anthropic เพิ่งเปิด public beta สัปดาห์ก่อนที่ Code w/ Claude 2026) cost scale **non-linear** ตาม parallel concurrency × token consumption × reasoning depth — Cursor adoption ที่ Uber plateau ขณะที่ Claude Code โต 2.6x ใน 3 เดือน บอกอย่างชัดเจนว่า budget overrun ไม่ใช่เพราะ tool fail แต่เพราะ tool ดีจน engineer หยุดใช้ไม่ได้

CTO ตอบนักวิเคราะห์แบบ Naga-style honest — "back to the drawing board" บนการตั้งงบ AI; แต่ Uber ไม่ได้บอกว่าจะตัด — แค่จะออกแบบ budgeting model ใหม่ ที่รับ realities ว่า productivity gain น่าจะคุ้มราคา **ถ้า** marginal output ของ agent run แต่ละครั้งสร้าง enterprise value มากกว่า marginal cost ของ token (ที่ Anthropic ปรับขึ้นได้ทุกไตรมาส)

## ทำไมสำคัญ

นี่คือ **first public crack ใน narrative ของ agentic coding ROI** — ตลอด 18 เดือนที่ผ่านมา story หลักของ Claude Code/Cursor/Devin คือ "engineer productivity 2-10x, cost-saving ไม่มีลิมิต" ตอนนี้ Uber ที่เป็น engineering org ใหญ่ที่สุดของ B2C tech (~4,500 software engineer) ออกมาพิสูจน์ว่า **lifecycle cost ของ agentic workflow ไม่ใช่ predictable line item** — มัน scale ตามการใช้ ไม่ใช่ตามจำนวน seat. การที่ token-based pricing ของ Anthropic + Anthropic ปรับ pricing แบบ midmarket SaaS (5-10% ทุกไตรมาส) แปลว่า CFO ของบริษัท Fortune 500 ตอนนี้มี new line item ที่ผันแปรเหมือน cloud compute ใน 2014 ก่อนยุคของ FinOps

Pattern ที่จะเห็นในไตรมาส 2-3: **FinOps for AI tooling** จะกลายเป็นคำใหม่ — เริ่มจาก dashboard ที่ engineering org ใช้ track per-developer per-project token consumption, ตามด้วย policy engine ที่ throttle parallel agent ของ junior engineer, แล้ว pricing strategy เก็บค่า "extra agent run" จาก business owner ที่ feature request. Tools เช่น Sourcegraph Cody, Coder Workspaces, JetBrains AI ที่เคยขายแค่ subscription จะเริ่มจัด tier "budget cap + chargeback" — ของที่ AWS Bedrock มี IAM/budget guardrail แต่ Claude Code/Cursor ใน developer laptop ยังไม่มี

Signal ที่สอง: **agentic workflow productivity gain มัก undersell โดย vendor** — Uber report 11% ของ PR by AI ที่ฟัง compact แต่ใน scope ของบริษัทระดับนั้นคือ value creation หลายร้อยล้าน/ปี (และนี่คือก่อน multi-agent orchestration เปิด GA). ที่ Claude Code ทำให้ engineer ส่วนใหญ่ "หยุดไม่ได้" สะท้อนว่า productivity threshold ของ frontier agent ผ่านจุดที่ engineer มอง switching cost ของการเลิกใช้สูงเกินไป — Anthropic ตอนนี้มี **lock-in ที่ไม่ใช่ data lock-in แต่เป็น cognitive lock-in** ที่ราคาตั้งตามใจได้

## มุม OpenBridge

Story นี้บอก OpenBridge สามอย่างตรง ๆ:

(1) **Connector layer ใน OpenBridge ต้องคิด FinOps จาก day 1** — agent ที่เรียก MCP connector ของ OpenBridge ใช้ API call จริงทุก action; ถ้า downstream agent loop หรือ retry หรือ multi-step orchestration, cost ที่ end-customer แบกอาจ explode คล้าย Uber. OpenBridge ควร emit **per-action usage metric** (token equivalent, cost estimate, throughput) ติด response payload เพื่อให้ agent platform ที่ใช้ connector ของเรา (Sierra, Decagon, custom Claude Code workflows) chargeback กลับ business owner ได้ — feature นี้คือ moat: connector ใหม่จะลอกได้ แต่ chargeback-ready connector จะกลายเป็น category-defining (เหมือน CloudWatch billing tag ใน AWS).

(2) **Pricing model OpenBridge ควรเลือกระหว่าง flat per-connector vs token-based per-call ตั้งแต่วันแรก** — Uber/Anthropic เป็น cautionary tale ว่า token-based pricing ดีต่อ vendor แต่ aggressive ต่อ buyer, และ buyer ก็เริ่มต่อต้าน (FinOps committee, procurement gate). ถ้าเลือก hybrid (flat baseline + variable usage cap) OpenBridge จะวางขายให้ enterprise IT ง่ายกว่า — เพราะ procurement ของ JPMorgan/SCBX ไม่ approve line item ที่ "ไม่รู้ปลายปีจะแพงเท่าไหร่"

(3) **"AI cost observability" เป็น product extension ที่อาจ build ได้** — สมมติว่า OpenBridge ขายเป็น **AI cost ledger สำหรับ enterprise agent stack**: รับ webhook จาก Claude Code/Cursor/Devin, รวมกับ token usage จาก OpenAI/Anthropic API, แล้ว map กลับเข้า engineer/team/feature ผ่าน connector ของเรา (Jira, Linear, GitHub). Adjacent product ที่ใช้ traction ของ core connector + ตอบโจทย์ pain point ที่ CFO ทุกบริษัท Fortune 500 จะมีภายในไตรมาส Q3 2026

## Sources
- [Uber torches 2026 AI budget on Claude Code in four months (briefs.co)](https://www.briefs.co/news/uber-torches-entire-2026-ai-budget-on-claude-code-in-four-months/)
- [Uber Burned Its Entire 2026 AI Budget in Four Months (Medium)](https://medium.com/@sebuzdugan/how-uber-burned-its-entire-2026-ai-budget-in-just-four-months-8328741760de)
- [Uber's Anthropic AI Push Hits A Wall — CTO Says Budget Struggles Despite $3.4B Spend (Yahoo Finance)](https://finance.yahoo.com/sectors/technology/articles/ubers-anthropic-ai-push-hits-223109852.html)
- [Hacker News discussion](https://news.ycombinator.com/item?id=47976415)
- [Why Uber has Already Burned Through its AI Budget (AI Magazine)](https://aimagazine.com/news/why-uber-has-already-burned-through-its-ai-budget)

---

## Audio script
เรื่องนี้น่าจะเป็น story ที่จุกใจ CFO ทุกบริษัท Fortune 500 — Uber เพิ่งยอมรับว่าใช้งบ AI ปี 2026 ทั้งก้อนหมดภายในเดือนเมษายน ภายในแค่สี่เดือน. ตัวเลขที่ออกมาเข้าใจง่ายคือ engineer ของ Uber 84 เปอร์เซ็นต์ใช้ Claude Code ของ Anthropic ทุกวัน เพิ่มจากแค่ 32 เปอร์เซ็นต์ตอนปลายปีที่แล้ว และตอนนี้ pull request 11 เปอร์เซ็นต์ของทั้งบริษัทถูกเปิดโดย agent — รวมถึง algorithm ของ ride-matching, dynamic pricing, bug fix ใหญ่ ๆ. CTO Praveen Neppalli Naga บอกตรงๆว่า "back to the drawing board" บน budgeting — เพราะ Claude Code ใช้ pricing แบบ token-based ไม่ใช่ per-seat แบบ Copilot ดั้งเดิม. แต่ละ engineer ใช้ API cost ระหว่าง 500 ถึง 2,000 ดอลลาร์ต่อเดือน. ที่น่าสนใจคือ Uber ไม่ได้บอกว่าจะตัด — แค่จะหาวิธี budgeting ใหม่ เพราะ tool มันดีจน engineer หยุดใช้ไม่ได้. นี่คือ first public crack ใน narrative agentic coding ROI ที่ vendor ขายมาตลอด 18 เดือน — productivity จริง แต่ cost จะ scale ไม่จบ. คาดว่าไตรมาสหน้าจะเริ่มเห็น FinOps for AI tooling เป็นคำ buzzword ใหม่ — dashboard track token per engineer, policy throttle agent run, chargeback model. สำหรับ OpenBridge หมายความว่า connector ต้องคิด FinOps จากวันแรก, emit per-action cost metric ใน payload, เลือก pricing model ที่ procurement enterprise approve ได้ ไม่ใช่ pure token-based. และอาจเปิด product สอง — AI cost ledger สำหรับ enterprise agent stack — ที่ตอบโจทย์ pain point ที่ CFO ทุกแห่งจะเจอภายใน Q3 ปีนี้
