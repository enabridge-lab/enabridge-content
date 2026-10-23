---
date: 2026-10-22
slug: aaif-four-projects-agent-skills
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of four glowing modular containers being
  lifted by cranes onto a central platform stamped "AGENTIC AI FOUNDATION — LINUX
  FOUNDATION". Each container has a logo-shaped stencil and a label: "ANTHROPIC —
  AGENT SKILLS", "OPENAI — OPEN RESPONSES", "HUGGING FACE — OPENENV",
  "ALIBABA — OPENSANDBOX". Three stacked numbers float above the platform:
  "10 PROJECTS", "1M PUBLISHED SKILLS", "280M INSTALLS". A banner below reads
  "AGNTCON — OCT 22, 2026". Deep navy and Linux Foundation blue palette, strong
  contrast for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-24-0606-05-aaif-four-projects-agent-skills.png
---

# Agentic AI Foundation รับ 4 โปรเจกต์ใหม่ — Anthropic Agent Skills (1M skills, 280M installs), OpenAI Open Responses, HF OpenEnv, Alibaba OpenSandbox

## TL;DR
- **22 ต.ค.** ที่งาน AGNTCon ซานโฮเซ, Linux Foundation's **Agentic AI Foundation (AAIF)** รับ 4 โปรเจกต์ใหม่จาก Anthropic, OpenAI, Hugging Face, Alibaba — total roster ตอนนี้ **10 projects** (จาก 3 ตอนเปิดตัว ธ.ค. 2025)
- **Anthropic — Agent Skills:** standard ที่ grow มาจาก Claude skills, Anthropic claim **~1 ล้าน skill published, ~280 ล้าน installs**. AAIF รับ name, logo, GitHub org, agentskills.io
- **OpenAI — Open Responses:** spec ของ interoperable LLM interface based on OpenAI Responses API — จาก proprietary API → vendor-neutral spec
- **Hugging Face — OpenEnv:** containerized service สำหรับ reinforcement learning environment ที่ใช้ train agent
- **Alibaba — OpenSandbox:** sandbox runtime ที่ AI lab ใช้ simulate production environment
- Signal: **agent protocol/skill/sandbox layer กำลัง consolidate ภายใต้ neutral governance** — คู่ขนานกับ MCP ที่ Anthropic donate ไปก่อนหน้า. The Register วิจารณ์ว่า "vendor-affiliated tech moving to friendly, funded foundation" — ยังต้องรอดูว่า governance จะ enable cross-company adoption จริงหรือเป็น PR ของ vendor

## เกิดอะไรขึ้น

วันพฤหัสที่ **22 ต.ค.** ที่งาน **AGNTCon** ซานโฮเซ, Linux Foundation's **Agentic AI Foundation (AAIF)** ประกาศรับ 4 โปรเจกต์ใหม่ ซึ่งเป็น batch ที่ใหญ่ที่สุดตั้งแต่ AAIF ก่อตั้งเมื่อ ธ.ค. 2025. ก่อนหน้านี้ AAIF มี 3 โปรเจกต์หลัก — **MCP (Model Context Protocol)** จาก Anthropic, **Agent2Agent (A2A)** จาก Google, และ **Goose** agent framework จาก Block. รอบนี้ขยายเป็น 10 โปรเจกต์

**Anthropic — Agent Skills:** standard ที่ Anthropic สร้างจาก Claude skills — เป็น protocol สำหรับ **package + distribute + install "skill"** ให้ agent (เช่น skill สำหรับ reading PDF, สำหรับ running SQL, สำหรับ generating slides). Anthropic อ้างว่าตั้งแต่ Claude Skills launch (เม.ย. 2025) มี **~1 ล้าน skill published** และ **~280 ล้าน installs** รวมทั้ง skill ที่ Anthropic ship เอง + skill ที่ community สร้าง. AAIF รับ brand (ชื่อ Agent Skills), logo, GitHub organization, และ domain **agentskills.io**. ตีความ: Anthropic เปิดให้ ecosystem เข้า contribute ภายใต้ governance กลาง ไม่ bind กับ Claude

**OpenAI — Open Responses:** OpenAI Responses API เป็น interface ที่ OpenAI เปิดใน ก.พ. 2026 — ส่วน extension ของ Chat Completions ที่รองรับ async + background execution + agent-oriented primitive. การ donate ให้ AAIF เท่ากับประกาศว่า **spec นี้จะมีหลาย implementation** ไม่ใช่แค่ OpenAI (Anthropic, Google, DeepSeek น่าจะ ship compatible endpoint ตามใน 2027). นี่คือการแข่ง "LLM interface standard" รอบที่สองหลัง OpenAI Chat Completions ที่ครองตลาด de facto มา 3 ปี

**Hugging Face — OpenEnv:** containerized service ที่ให้ dev สร้าง reinforcement learning environment สำหรับ training agent. ก่อนหน้านี้ RL environment แต่ละทีมสร้างเอง — มี Gymnasium (ของ Farama) เป็น standard ที่กว้างแต่ไม่ enterprise-ready. OpenEnv เพิ่ม container, versioning, และ shared registry

**Alibaba — OpenSandbox:** sandbox runtime ที่ AI lab (เช่น Qwen team) ใช้ **simulate production infrastructure** ตอน train model — มี tool, API, database ภายใน sandbox ที่ agent interact ได้. คู่แข่งคือ **Daytona** (ที่ปิด Series B $60M ที่ $1B valuation สัปดาห์ก่อน) และ Replit — แต่ OpenSandbox เป็น open-source

## ทำไมสำคัญ

สองสัญญาณที่สำคัญกว่าเนื้อหา

**หนึ่ง — "ของขวัญฟรี" จาก vendor ไปที่ foundation = การเปลี่ยนขั้วของอำนาจ**. Anthropic ยอมปล่อย Agent Skills brand (ซึ่งเป็นหนึ่งใน moat ที่ชัดที่สุดของ Claude ecosystem) ให้ foundation = ตีความว่า Anthropic bet ว่า **"ยิ่ง Agent Skills เป็น standard, Claude ยิ่งชนะ"** — เพราะ skill ที่ community สร้างบน Claude ยังรันบน Claude ได้ดีที่สุด. OpenAI เลือก Open Responses ด้วย logic เดียวกัน — ถ้า spec ชนะ, OpenAI มี head start เป็น reference implementation. ตีความอีกมุม (The Register): "friendly, funded foundation" — AAIF ยัง **governance โดย donor** เยอะ, ยังไม่มี enforcement กลางที่ independent

**สอง — layer stack ของ agent กำลัง consolidate เร็วมาก**. ปีที่แล้ว AAIF มี 3 project ตอนก่อตั้ง, ตอนนี้ 10, คาดว่าจะเป็น 20+ ภายใน Q2 2027. layer ที่ cover: protocol (MCP, A2A), skill (Agent Skills), interface (Open Responses), training environment (OpenEnv), execution sandbox (OpenSandbox), framework (Goose). ที่ยัง **missing จาก AAIF**: identity (ServiceNow AI Passport, 1Password for Agents), governance control plane (ServiceNow Super Intelligence Control Tower, Opsin), payment (Mastercard Agent Pay, Visa Intelligent Commerce). น่าจับตาว่า vendor ของ layer เหล่านี้จะ donate ไหม

Pattern ที่ enterprise ควรจับ: **standard ของ agent layer ชี้ไปที่ "ยิ่ง open ยิ่งเร็ว"** — เพราะ enterprise CIO เลือก vendor ที่ compatible กับ open spec มากกว่า proprietary. ภายใน 2027 ความต่างระหว่าง AWS/Google/Microsoft/Oracle agent platform จะเหลือแค่ **compute, data gravity, และ workflow integration** — ไม่ใช่ที่ "ใครมี skill พิเศษ"

## มุม AI Agent Platform

สำหรับ **Builders**: ติดตาม AAIF spec อย่างใกล้ชิด — ภายใน Q2 2027 ถ้า agent runtime คุณไม่พูด Agent Skills + Open Responses + MCP + A2A คุณพลาด enterprise channel ทั้งหมด. สำคัญกว่าคือ **contribute spec** ด้วย — ให้ voice ของคุณอยู่ใน governance ไม่ใช่แค่ consumer. สำหรับ **Users / Business**: AAIF roster = **vendor-neutral purchasing checklist** — ก่อนซื้อ agent platform ให้ถามว่า "support MCP, Agent Skills, Open Responses, A2A ไหม". ถ้า vendor ตอบไม่ครบ, lock-in risk สูง. สำหรับ **Ecosystem**: layer ที่ AAIF ยังว่าง (identity, payment, observability) คือ **greenfield market** — startup ที่ ship ก่อนและ donate spec ให้ AAIF ภายใน 2027 จะได้ brand ของ "default standard" ก่อน incumbent. 1Password, Opsin, Mastercard, Visa มีโอกาสมอง AAIF เป็น strategic distribution channel ไม่ใช่แค่ open-source community

## Sources
- [Agentic AI Foundation adds four more open-source AI tools (SiliconANGLE)](https://siliconangle.com/2026/10/22/agentic-ai-foundation-adds-four-more-open-source-ai-tools/)
- [Agentic AI Foundation Announces Four New Projects: Agent Skills, Open Responses, OpenEnv, and OpenSandbox (Linux Foundation Press)](https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox)
- [Vendor-affiliated AI agent tech gets adopted by friendly, funded foundation (The Register)](https://www.theregister.com/ai-and-ml/2026/10/23/vendor-affiliated-ai-agent-tech-gets-adopted-by-friendly-funded-foundation/5304912)

---

## Audio script
วันพฤหัสที่ 22 ตุลาคม ที่งาน AGNTCon ซานโฮเซ Agentic AI Foundation ของ Linux Foundation รับ 4 โปรเจกต์ใหม่ รวมเป็น 10 โปรเจกต์แล้ว จาก 3 ตอนเปิดตัวเมื่อ ธันวาคม 2025. โปรเจกต์แรก Anthropic donate Agent Skills ซึ่งเป็น standard ที่ grow มาจาก Claude skills Anthropic อ้างว่ามี 1 ล้าน skill published และ 280 ล้าน installs AAIF รับทั้ง brand logo GitHub org และ domain agentskills.io. โปรเจกต์ที่สอง OpenAI donate Open Responses spec ของ LLM interface ที่ขยายจาก Chat Completions รองรับ async และ background execution — ก่อนหน้านี้ Chat Completions เป็น de facto มา 3 ปี Open Responses จะเป็นรอบที่สอง. โปรเจกต์ที่สาม Hugging Face donate OpenEnv สำหรับสร้าง reinforcement learning environment ตอน train agent. โปรเจกต์ที่สี่ Alibaba donate OpenSandbox runtime ที่ Qwen team ใช้ simulate production infrastructure ตอน train model คู่แข่งคือ Daytona กับ Replit แต่ OpenSandbox เป็น open-source. สองสัญญาณที่สำคัญกว่าเนื้อหาคือ Anthropic ยอมปล่อย Agent Skills brand ที่เป็น moat ของ Claude ecosystem = bet ว่า ยิ่งเป็น standard ยิ่งชนะ เพราะ skill ที่ community สร้างยังรันบน Claude ได้ดีที่สุด OpenAI logic เดียวกัน. สองคือ layer stack ของ agent consolidate เร็วมาก ปีที่แล้ว 3 โปรเจกต์ ตอนนี้ 10 น่าจะ 20 ภายใน Q2 2027 ภายในปี 2027 ความต่างระหว่าง AWS Google Microsoft Oracle จะเหลือแค่ compute data gravity กับ workflow integration — ไม่ใช่ที่ใครมี skill พิเศษ. สำหรับ builder ติดตาม spec AAIF ให้ครบ ถ้า agent คุณไม่พูด Agent Skills Open Responses MCP A2A ภายใน Q2 2027 คุณพลาด enterprise channel. สำหรับ CIO ก่อนซื้อ agent platform ให้ถาม support สี่ตัวนี้ครบไหม ถ้าไม่ครบ lock-in risk สูง สำหรับ ecosystem layer ที่ AAIF ยังว่าง identity payment observability คือ greenfield market ที่ startup ที่ donate spec ให้ AAIF ก่อนจะได้ brand default standard
