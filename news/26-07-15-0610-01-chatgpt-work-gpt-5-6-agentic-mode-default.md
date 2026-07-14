---
date: 2026-07-15
slug: chatgpt-work-gpt-5-6-agentic-mode-default
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial isometric hero illustration of a giant desk at night with a
  glowing rectangular slate labeled "CHATGPT WORK" in the center;
  autonomously running arms deliver stacked finished deliverables labeled
  "SLIDES", "SHEETS", "DOCS", "WEB APP" onto out-trays. In the background
  three glowing model tiles float above the desk labeled "SOL", "TERRA",
  "LUNA" connected by thin wires to a small router-box labeled "PLAN MODE
  APPROVAL". A ticking wall clock in the top corner reads "HOURS, NOT
  MINUTES". Bold text readable at 200px thumbnail, high-contrast cinematic
  teal-amber palette, 1:1 aspect, no real human faces.
image: images/26-07-15-0610-01-chatgpt-work-gpt-5-6-agentic-mode-default.png
---

# OpenAI ship ChatGPT Work + GPT-5.6 สาม tier — agentic mode หยุดเป็น feature เริ่มเป็น default surface ของ knowledge work

## TL;DR
- 9 ก.ค. OpenAI ship **ChatGPT Work** — agentic mode ใน ChatGPT ที่ **รันเป็นชั่วโมง** ข้าม apps/files/workflows คืนงานเป็นไฟล์ SLIDES/SHEETS/DOCS/WEB APP ที่ finished ไม่ใช่ draft
- ปล่อย **GPT-5.6 สาม tier** พร้อมกัน: **Sol** frontier ($5/$30 per M tokens), **Terra** mid ($2.50/$15), **Luna** budget ($1/$6); plus **Multi-agent Responses API beta** ที่ root agent spawn subagents (`/root/researcher`, `/root/reviewer/tester`) แบบ hierarchical
- Enterprise ได้ **spend controls ใน Admin Console** + workspace defaults + group limits + request-for-credits flow — pricing โยง Codex usage structure token-based (ไม่ใช่ seat/flat) = **agent economics เข้ามาแทน SaaS economics ใน consumer product ที่มีผู้ใช้ 900M+**

## เกิดอะไรขึ้น
พฤหัสฯ 9 ก.ค. OpenAI ปล่อยของสามชิ้นในวันเดียว — GPT-5.6 model family, ChatGPT Work agentic mode, และ Multi-agent Responses API beta — เหมือน bundling ที่จงใจให้เห็นว่า agent ไม่ใช่ product ข้าง ๆ อีกต่อไป มันคือ default surface ของ ChatGPT ปีนี้. Bloomberg รายงานว่า launch นี้เดิมถูก administration ขอให้ hold late-June ให้ trusted partners ทดสอบก่อน หลังจาก Commerce Department's Center for AI Standards and Innovation ทำ safety testing เสร็จจึงเปิดสาธารณะ — timing signal ว่า agentic autonomy ระดับนี้ตอนนี้ผ่านการ review ระดับรัฐบาลก่อนออก

**ChatGPT Work** คือ agent ที่ "gathers context across your apps, breaks a goal into steps, and returns finished sheets, slides, docs, and web apps". มี Codex technology built in รันบน GPT-5.6 มี **Plan mode** ให้ user approve step-by-step plan ก่อนเริ่ม, มี **configurable check-ins** ตอนกลางทาง, และ **action approvals** สำหรับ operation ที่ irreversible. OpenAI พูดตรง ๆ ว่า "designed for longer, more involved work than a typical chat request, so usage works differently" — เลิก assume ว่า 1 prompt = 1 response, เริ่ม assume ว่า 1 goal = ชั่วโมงของ autonomous work

**GPT-5.6** ปล่อยเป็นสาม tier แทน single flagship: Sol เป็น frontier reasoning ($5 input / $30 output per M tokens), Terra เป็น "~5.5-level intelligence at half the cost" ($2.50/$15), Luna เป็น small fast ($1/$6). Plus **Ultra mode** ใหม่ที่มี Max reasoning level + heavier sub-agent use. โครงสร้าง three-tier นี้ mirror Anthropic (Opus/Sonnet/Haiku), Google (Ultra/Pro/Flash), SpaceXAI (Grok Sol/Terra/Luna? — จริง ๆ Grok 4.5 คือ single-tier) — **tier ecosystem = new normal** เพราะ workload ในองค์กรจริง ๆ ไม่ homogeneous, ต้อง route ตาม task profile

**Multi-agent ใน Responses API (beta)** ทำให้ root agent spawn subagents แบบ concurrent ผ่าน hierarchical path — เช่น `/root ├── /root/researcher ├── /root/reviewer └── /root/reviewer/tester`. OpenAI provides "hosted orchestration actions and instructions" — พูดง่าย ๆ คือ orchestration primitive ที่เดิมต้องเขียนเองใน LangGraph/CrewAI ตอนนี้ built into API. Feature นี้ available "with all GPT-5.6 models" — สัญญาณว่า multi-agent จะเป็น table stakes ของ frontier API ทุกเจ้าใน Q3

Enterprise angle จำเป็นต้องอ่านเงื่อนไข: **ไม่มี per-task price / credit rate / hard limit ประกาศตอน launch** — Work ตาม Codex usage structure ที่เพิ่งย้ายไป **token-based ตั้งแต่ 6 ก.ค.** ทำให้ budget/prioritization กลายเป็น engineering + finance issue พร้อมกัน. Admin Console มี spend controls: workspace defaults, group limits, individual overrides, request-for-credits review flow — สร้างมาสำหรับ CFO ที่กลัวว่าพนักงานคนไหนจะ "รัน Work ทิ้งค้างคืน" แล้วบิลไม่จบ

## ทำไมสำคัญ
Pattern ที่ Enabridge tracking หลายเดือน — **agentic mode หยุดเป็น separate product เริ่มเป็น default execution model** — เพิ่งได้ largest datapoint ในตลาด consumer LLM. ChatGPT Weekly Active Users อยู่ที่ ~900M+, ChatGPT Enterprise มี paying customer เกือบล้าน seat — OpenAI ไม่ได้ launch agent สำหรับกลุ่ม early adopter, launch ให้ทั้ง base ที่มีอยู่. เทียบกับ Anthropic Claude Cowork, Google Workspace Studio, Microsoft Copilot Agent, Salesforce Agentforce — สี่ค่ายพูดเรื่องเดียวกันในสี่ product surface, แต่ ChatGPT Work มี distribution ใหญ่ที่สุด

Signal สำหรับ builder ecosystem: **API-level multi-agent = commoditize orchestration framework**. LangGraph, CrewAI, AutoGen, Semantic Kernel, Claude Agent SDK ทั้งหมด monetize / differentiate ที่ orchestration primitive (handoff, checkpoint, human-in-loop, state graph). ถ้า OpenAI Responses API มี hierarchical spawn built-in + Google ADK v1.0 stable + Microsoft Agent Framework Magentic-One stable = orchestration layer โดน "collapsed into the API" แบบเดียวกับที่ RAG framework โดน collapsed เข้า Assistants API เมื่อปีที่แล้ว. Framework ที่จะรอดต้องขึ้นไปหา governance layer, evaluation layer, หรือ vertical agent layer แทน

ที่น่าจับตาระยะกลางคือ **pricing psychology transition**. Consumer เพิ่งเรียนรู้ว่า Plus $20/เดือน = unlimited-ish; ตอนนี้ Work ปล่อย token-based ที่ Codex-style hard cap. เดือน ก.ค. นี้จะเป็นเดือนแรกที่ ChatGPT user เจอ "you've hit your Work limit — request more credits" — reaction จะบอกว่า mass market พร้อมรับ agent economics แค่ไหน. ถ้าเงียบ (พร้อมจ่าย per outcome) = ทั้งตลาด SaaS ต้อง revise pricing sheet ในหกเดือน. ถ้า backlash (revolt against usage-based) = agent product แพงจะยัง niche

## มุม AI Agent Platform
สำหรับ **builders**: ถ้าเป็น orchestration framework — พิจารณา move up-stack. LangChain/CrewAI/AutoGen ยังคงมี market ใน hybrid/on-prem/regulated แต่ commodity API multi-agent จะกิน default use case. Builder ที่ทำ agent runtime (Bespoke Labs training environments, Braintrust eval, Arize observability, LangSmith trace) ได้ tailwind — เพราะทุกคนต้อง test/observe agent ที่ตอนนี้ deploy ง่ายขึ้น. Builder ที่ทำ vertical agent (legal, medical, finance, ops) ต้องแข่งกับ ChatGPT Work + connectors ของ user เอง — moat ต้องอยู่ที่ workflow expertise + integration depth ไม่ใช่ prompt

สำหรับ **users/business** ที่ evaluate agent product: ก่อนซื้อ seat license ของ agent vendor ปีนี้ ให้ถามว่า (1) ต้นทุน per task expected เท่าไร (มี benchmark vs ChatGPT Work / Claude Cowork / Foundry Agent Service), (2) ถ้าพนักงานใช้ ChatGPT Work workflow เดียวกันได้ผลใกล้เคียง vendor สร้าง value อะไรเพิ่ม, (3) มี Plan mode / approval workflow / audit log เทียบ OpenAI+Anthropic หรือไม่. Thai enterprise ที่มี ChatGPT Enterprise deploy แล้ว: Q3 นี้ควร pilot Work กับ finance/HR/marketing team แล้ววัด output vs current tool — น่าจะ collapse subscription ซ้ำซ้อนได้ 2-3 tool

สำหรับ **ecosystem**: hyperscaler ที่ขาย agent runtime (Azure Foundry Agent Service, Vertex AI Agent Builder, Bedrock Agents) เจอ pressure สองด้าน — OpenAI จับ consumer + prosumer + SMB ตรง, model provider จับ frontier API. Hyperscaler ต้อง double-down ที่ enterprise governance + private compute + framework-agnostic (Foundry รองรับ LangChain/CrewAI/custom เพราะเข้าใจ point นี้). Governance vendor (Devenex, Datadog LLM Observability, Portkey, Kong AI Gateway) เข้า critical infrastructure category — enterprise ที่ let พนักงาน run agent 8 ชม./task ต้อง centralize policy + spend + audit ก่อน CFO panic

## Sources
- [OpenAI Launches ChatGPT Work Agent to Handle Complex Tasks — Bloomberg](https://www.bloomberg.com/news/articles/2026-07-09/openai-unveils-chatgpt-work-agent-to-field-tasks-for-hours)
- [ChatGPT Work: OpenAI's Agent That Ships Finished Work — Digital Applied](https://www.digitalapplied.com/blog/chatgpt-work-openai-agent-launch-2026)
- [OpenAI Launches ChatGPT Agent That Executes Complex Workflows — PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/openai-launches-chatgpt-agent-that-executes-complex-workflows/)
- [Multi-agent | OpenAI API (Responses API guide)](https://developers.openai.com/api/docs/guides/responses-multi-agent)
- [July 2026 AI Releases: OpenAI, Anthropic, Google DeepMind, Meta AI — ThursdAI](https://thursdai.news/releases/2026-07)

---

## Audio script
9 กรกฎาคม OpenAI ปล่อยของสามชิ้นในวันเดียว GPT 5.6 สาม tier ChatGPT Work agentic mode และ Multi-agent Responses API beta ChatGPT Work คือ agent ที่รันเป็นชั่วโมง มัน gather context จากทุก app ที่ user ต่อไว้ ทำเป็น plan ให้ approve แล้วส่งมอบงานเป็นไฟล์ finished ทั้ง slides sheets docs หรือ web app ไม่ใช่ draft ที่ต้องแก้ต่อ. Bloomberg บอกว่า launch นี้ถูก administration ขอ hold ให้ Center for AI Standards and Innovation ทำ safety testing เสร็จก่อน timing บอกว่า autonomy ระดับนี้ผ่าน review ระดับรัฐบาลแล้ว. GPT 5.6 ปล่อยเป็น Sol frontier ห้าดอลลาร์ต่อล้าน token Terra mid tier สองห้าสิบดอลลาร์ Luna budget หนึ่งดอลลาร์ — tier ecosystem กลายเป็น new normal เพราะ workload จริงไม่ homogeneous. Multi-agent ใน Responses API ทำให้ root agent spawn subagents แบบ hierarchical concurrent orchestration ที่เมื่อก่อนต้องเขียนใน LangGraph หรือ CrewAI ตอนนี้ built in ใน API — framework ที่ monetize orchestration primitive ต้อง move up stack ไป governance eval หรือ vertical agent. สำคัญที่สุดคือ Work ตาม Codex pricing structure token based ไม่มี flat cap — เดือน กรกฎาคมนี้จะเป็นเดือนแรกที่ ChatGPT user เจอ hit your Work limit request more credits reaction จะบอกว่า mass market พร้อมรับ agent economics แค่ไหน. Thai enterprise ที่มี ChatGPT Enterprise แล้ว Q3 ควร pilot Work กับ finance HR marketing เทียบ output กับ tool เดิม น่าจะ collapse subscription ซ้ำซ้อนได้ 2-3 tool
