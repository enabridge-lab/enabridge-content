---
date: 2026-07-31
slug: microsoft-visual-studio-copilot-sdk-agent-runtime-consolidation
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  Editorial isometric illustration of three separate developer workstations — labeled "VISUAL STUDIO",
  "VS CODE", "COPILOT CLI" — merging their glowing streams into a single central pillar labeled
  "COPILOT SDK RUNTIME". Below, small icons of an agent node with tool ports (dotnet, azure, csharp,
  git). Rich indigo, warm amber highlights, flat editorial style, dramatic chiaroscuro. 1:1 aspect.
  Text labels must render sharply at 200px thumbnail. No real human faces.
image: images/26-07-31-0611-02-microsoft-visual-studio-copilot-sdk-agent-runtime-consolidation.png
---

# Microsoft ย้าย Visual Studio agent ไป GitHub Copilot SDK — จุดเริ่ม agent runtime consolidation ระดับ vendor

## TL;DR
- **30 ก.ค.** — GitHub Copilot in Visual Studio July update เปิด **Agent (Preview) ตัวใหม่ที่ build บน Copilot SDK เดียวกับที่ powers GitHub Copilot CLI** — Microsoft consolidate agent runtime ข้าม 3 dev surface ที่เคย fork กัน (Visual Studio, VS Code, CLI)
- มาพร้อม **built-in .NET + Azure skill** (dotnet-trace-collect, dotnet-pinvoke, csharp-scripts, azure-validate, azure-upgrade), **organization-level custom instructions** ที่ push preference จาก org owner ลงทุก repo, และ **Copilot Actions > Review Selection** สำหรับ inline code review
- Positioning: **Agent framework diversity ตายที่ layer runtime** — VC-funded framework startup จะ compete ยากขึ้นเมื่อ Microsoft/Anthropic/OpenAI ต่างมี SDK ของตัวเองที่ integrate ลึกกับ IDE + CLI + cloud
- ต่อยอด pattern เดียวกับ Anthropic Claude Code SDK ที่ powers Claude Code CLI + Claude Desktop; OpenAI Agents SDK ที่ powers ChatGPT Enterprise + Codex — **3 vendor lock runtime layer สำเร็จภายในปี 2026**

## เกิดอะไรขึ้น

วันที่ 30 ก.ค. GitHub Copilot in Visual Studio ปล่อย July update ที่ตัว headline คือ **Agent (Preview) ตัวใหม่ที่ build บน Copilot SDK ตัวเดียวกับที่ powers GitHub Copilot CLI**. ในแง่ product คือ tab ใหม่ใน agent picker; ในแง่ architecture คือ **Microsoft เพิ่งย้าย AI layer ทั้งหมดของ Visual Studio ให้ run บน SDK เดียวกับที่ VS Code + CLI ใช้** — เลิก maintain 3 agent stack แยกที่ fork กันมาปีที่ผ่านมา. Blog post ของ Visual Studio team (28 ก.ค.) บอกตรง ๆ ว่า "future capabilities land in sync with VS Code and the Copilot CLI rather than on a separate development track"

สิ่งที่ผู้ใช้เห็นทันที: **shorter, easier-to-scan responses; less back-and-forth**. Agent ใหม่ได้ prompt architecture + tool orchestration ที่ team GitHub tune จนนิ่งบน CLI + VS Code; VS user ที่เดิม feel เหมือน "agent ตอบยาว วนซ้ำ" จะได้ profile เดียวกับที่ CLI + VS Code ให้ทันที. Built-in skill ที่ตามมา — dotnet-trace-collect, dotnet-pinvoke, csharp-scripts (author โดย .NET team), azure-validate, azure-upgrade (author โดย Azure team) — เป็น **first-party tool ที่ enterprise .NET shop รอมานาน**. Skill พวกนี้ disabled by default (user เลือกเปิดเอง), ปรากฏใน tool picker เมื่อ workload ที่เกี่ยวข้อง install อยู่ — pattern ที่ Anthropic MCP + OpenAI plugin ใช้เหมือนกัน

Feature ชั้นสอง (ที่ enterprise buyer จะเห็นค่า): **organization-level custom instructions** ให้ org owner set Copilot preference กลาง (coding style, response format, prohibited pattern) ที่ push ลงทุก repo — คนไม่ต้อง config per-developer อีกต่อไป. บวกกับ **Copilot Actions > Review Selection** ที่เลือก code block แล้ว invoke inline review powered by GitHub's code review system — ตัว review agent ตัวเดียวกันที่ทำงานใน PR bot บน github.com, ตอนนี้ available inline ใน IDE. Git branch context, C++ build tools discovery (opt-in), aggregate credit usage ใน status menu — ทุกอย่างชี้ไปทาง **converged experience across dev surfaces**

Pattern ที่ zoom out เห็น: **3 frontier vendor ปิดเกม runtime layer สำเร็จภายในปี 2026**. Anthropic Claude Code SDK powers Claude Code CLI + Claude Desktop + Bedrock (May 2026 GA); OpenAI Agents SDK powers ChatGPT Enterprise Workspace + Codex CLI + Custom GPT (June 2026); Microsoft/GitHub Copilot SDK powers Visual Studio + VS Code + Copilot CLI (July 2026). **3 vendor ต่าง lock 3 developer surface + IDE + cloud dev stack ของตัวเอง** — และไม่มีใครยอม share runtime กับใคร

## ทำไมสำคัญ

**Agent framework diversity ตายที่ layer runtime**. ปี 2025-2026 เห็น open framework โผล่รัว — LangChain, LlamaIndex, CrewAI, Autogen, Pydantic AI, Mastra, Vercel AI SDK — ทั้งหมด compete ที่ layer abstraction + developer ergonomics. แต่ทุก framework ต้อง run บน runtime ของใครสักคน (Anthropic, OpenAI, Microsoft, หรือ open source เช่น vLLM/Ollama). **Runtime layer ที่ vendor ควบคุมได้** = observability, cost tracking, safety filter, tool orchestration, memory. Framework ที่ **wrap** runtime ได้ประโยชน์น้อยลงเรื่อย ๆ เมื่อ runtime เจ้าของ features เยอะขึ้น. LangChain adopt Anthropic MCP รอ MCP 2026-07-28 spec — เพราะรู้ว่าถ้าไม่ทำก็ตกจาก enterprise deal

**Enterprise buyer's calculus เปลี่ยน**. เมื่อก่อน CIO ถาม "IDE ไหนที่ dev เราชอบ?" (VS vs VS Code vs JetBrains vs Cursor). ตอนนี้ CIO ถาม **"agent runtime ไหนที่ enterprise เราจะ lock in สำหรับ 3-5 ปีข้างหน้า?"** — เพราะ runtime = subscription line item + observability data + security posture ที่ integrate กับ SIEM. Microsoft consolidate 3 dev surface บน SDK เดียว = **buying decision ย้ายจาก IDE (per-seat) ไป runtime (per-token + per-seat)**. GitHub Copilot Enterprise's rev/user grew 45% Q2/Q1 2026 (Q2 earnings) เพราะ pricing เริ่มรวม agent + IDE + review เป็น bundle เดียว — ราคาสูงกว่าเดิม แต่ CIO อธิบาย ROI ง่ายกว่า

**Signal ที่ต้องตาม 6-12 เดือน:** (1) *JetBrains ตอบยังไง?* — JetBrains AI ยังใช้ multiple backend (Claude, Gemini, OpenAI); ถ้าไม่มี "runtime ของตัวเอง" ก็เสี่ยงกลาย front-end ของ vendor. อาจ deep partner กับ Anthropic หรือ acquire startup runtime; (2) *Cursor, Windsurf, Zed จะ pivot ยังไง?* — VC-funded IDE ที่ compete บน UX เริ่ม squeeze เมื่อ runtime vendor ปิด IDE ของตัวเองด้วย; (3) *Vercel AI SDK, Mastra, Pydantic AI จะ position ตัวเองยังไง?* — framework ต้อง prove ว่า **cross-runtime abstraction** ให้ value พอที่ enterprise จ่าย. เดิม Vercel AI SDK differentiate ด้วย streaming + framework-agnostic — ต้อง double down บน cost tracker + observability ให้เร็ว

## มุม AI Agent Platform

**สำหรับ builders (framework/SI ในไทย):** ถ้ากำลังสร้าง product ที่ wrap Copilot/Claude/OpenAI runtime, ต้องตัดสินใจ 3 เดือนนี้ — (1) **stick กับ 1 vendor deep** (specialize บน MCP + Anthropic ecosystem, หรือ Copilot SDK + .NET/Azure ecosystem, หรือ OpenAI Agents SDK + Azure OpenAI), (2) **build cross-runtime abstraction ที่ prove value เกิน wrapper** (cost tracker, prompt cache manager, multi-runtime routing), (3) **pivot ขึ้นชั้น application** (vertical agent app ที่ hide runtime choice จาก user). ทางที่ตายเร็วสุดปี 2027 คือ **generic agent framework wrapper** ที่ไม่ specialize อะไร

**สำหรับ users/business:** ถ้ากำลัง evaluate dev tool + agent stack — check ว่า vendor consolidate agent runtime แล้วหรือยัง. Microsoft/GitHub บวก Anthropic บวก OpenAI มี clear roadmap. Vendor ที่ยัง fork runtime ตาม product line = TCO สูง, feature parity ช้า, security posture ยาก audit. **RFP Q4 2026 ควรมี clause: "vendor agent runtime consolidation roadmap in next 18 months"** — ถ้าตอบไม่ได้, sign contract แค่ 12 เดือน อย่า 36

**สำหรับ ecosystem (Thai IT services + reseller):** window เปิดสำหรับ **certified Copilot SDK integrator** (คล้าย Salesforce integrator ปี 2018-2020). G-Able, Bluebik, ACI, Netka, MFEC — ที่ position "Copilot SDK-native + .NET migration + Azure Foundry integration" จะ close deal ที่ K-Bank, SCB, PTT, CPALL, AIS ได้เร็วกว่า integrator ที่ยังขาย "multi-vendor AI advisory". Anthropic partnership (Cognizant EMEA style — brief 29 ก.ค.) กับ Microsoft's Copilot SDK consolidation = **2 wave ที่ SI ต้องเลือก specialize ก่อน Q1 2027**

## Sources
- [GitHub Copilot in Visual Studio — July update (July 30, 2026)](https://github.blog/changelog/2026-07-30-github-copilot-in-visual-studio-july-update/)
- [Visual Studio July Update — Meet the New Agent, Powered by the GitHub Copilot SDK — Visual Studio Blog](https://devblogs.microsoft.com/visualstudio/visual-studio-july-update-meet-the-new-agent-powered-by-copilot-sdk/)
- [Visual Studio July Update Brings Copilot Agent and Built-In Skills — Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/07/30/visual-studio-july-update-brings-copilot-agent-and-built-in-skills.aspx)
- [Visual Studio 2026 July Update: Agent Skills and Copilot Billing Fix — byteiota](https://byteiota.com/visual-studio-2026-july-update-agent-skills-and-copilot-billing-fix/)

---

## Audio script
ข่าวที่ dev ทุกคนที่ใช้ Visual Studio ต้องรู้เช้านี้. GitHub Copilot in Visual Studio ปล่อย July update วันที่ 30. Feature หลักคือ Agent Preview ตัวใหม่ที่ build บน Copilot SDK ตัวเดียวกับที่ powers Copilot CLI. แปลว่า Microsoft ย้าย AI layer ของ Visual Studio ทั้งหมดให้ run บน SDK เดียวกับ VS Code กับ CLI. ตัดการ maintain agent stack แยก 3 ตัวที่ fork กันมาปีที่ผ่านมา.

Feature ที่ตามมา. Built-in .NET กับ Azure skill ที่ team Microsoft author เอง. dotnet-trace-collect, dotnet-pinvoke, csharp-scripts, azure-validate, azure-upgrade. Organization-level custom instructions ให้ org owner set Copilot preference กลางแล้ว push ลงทุก repo. Copilot Actions Review Selection ให้เลือก code แล้ว invoke inline review.

Zoom out ให้เห็น pattern. 3 vendor ปิดเกม agent runtime สำเร็จภายในปี 2026. Anthropic Claude Code SDK powers Claude Code กับ Claude Desktop กับ Bedrock. OpenAI Agents SDK powers ChatGPT Enterprise กับ Codex CLI. Microsoft GitHub Copilot SDK powers Visual Studio VS Code CLI. 3 vendor lock 3 developer surface ของตัวเอง.

Implication ใหญ่. Agent framework diversity ตายที่ layer runtime. LangChain LlamaIndex CrewAI Autogen ที่ wrap runtime จะ compete ยากขึ้นเมื่อ runtime เจ้าของ features เยอะขึ้น. Enterprise buyer เปลี่ยน calculus. เดิมถาม IDE ไหนที่ dev ชอบ. ตอนนี้ถาม agent runtime ไหนที่จะ lock in 3 ถึง 5 ปี. เพราะ runtime เท่ากับ subscription plus observability plus security posture.

สำหรับ builders. ต้องตัดสินใจ 3 เดือนนี้. Stick หนึ่ง vendor deep. หรือ build cross-runtime abstraction ที่ prove value เกิน wrapper. หรือ pivot ขึ้นชั้น vertical application. Generic framework wrapper ที่ไม่ specialize อะไร ตายเร็วสุด.

สำหรับ SI ไทย. G-Able Bluebik ACI Netka MFEC. Window เปิดให้ position certified Copilot SDK integrator plus .NET migration plus Azure Foundry. คู่กับ Anthropic partnership แบบ Cognizant EMEA. 2 wave ที่ต้องเลือก specialize ก่อน Q1 2027. คุยกันวันหน้าครับ.
