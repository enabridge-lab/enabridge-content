---
date: 2026-08-05
slug: eu-ai-act-gpai-enforcement-live
topic: agentic-ai
reading_time_min: 4
sources: 6
image_prompt: |
  Editorial isometric illustration of a heavy stone gate marked "EU AI ACT — ART. 51-56"
  swinging open on Aug 2, 2026. Beyond the gate: a checkpoint counter where robot
  agents queue for identity scanning; overhead sign reads "GPAI — DOCUMENTATION,
  EVALUATION, RISK MITIGATION". A large yellow warning banner on the left wall reads
  "FINES: €15M OR 3% OF WORLDWIDE TURNOVER". On the right, a small backdoor labeled
  "1,800 UNAUTHENTICATED MCP SERVERS" is being sealed with a red padlock stamped
  "COMPLIANCE HAZARD". EU flag stars form the arch above. Editorial navy + gold
  palette, chiaroscuro style, 1:1 aspect, no real human faces, text sharp at 200px.
image: images/26-08-05-0614-02-eu-ai-act-gpai-enforcement-live.png
---

# EU AI Act GPAI enforcement live 2 ส.ค. — regulatory floor สำหรับ AI Agent ทั้งโลก, €15M/3% turnover fine, และเหตุผลที่ MCP identity gap กลายเป็น fine-able exposure

## TL;DR
- **2 ส.ค.** — European Commission (ผ่าน European AI Office) **มีอำนาจเต็มในการ investigate + enforce** EU AI Act ต่อ **GPAI (general-purpose AI models)** provider + prohibited AI practices. อำนาจครอบคลุม: request documentation, conduct evaluations, request corrective/risk mitigation measures, market restriction, recall/withdrawal, **fines สูงสุด €15M หรือ 3% ของ worldwide annual turnover** (แล้วแต่จำนวนไหนสูงกว่า)
- **Timeline gap ที่เพิ่ง close** — GPAI obligations มีผลตั้งแต่ 2 ส.ค. 2025 แต่ **enforcement power เพิ่งเปิดใช้ได้ 2 ส.ค. 2026** = 12 เดือน grace period จบวันนี้; provider ของ GPAI ที่ release ก่อน 2 ส.ค. 2025 ต้อง compliant ก่อน 2 ส.ค. 2027
- **Signal ที่กระทบ agent deployment ทั่วโลก** — ทุก enterprise ที่ deploy agent ที่ใช้ GPAI (OpenAI, Anthropic, Google, xAI, Mistral, DeepSeek, Cohere, Meta) ใน EU market ต้องมี audit trail + risk mitigation + documentation ทันที; **>1,800 MCP server ที่ยังไม่มี authentication บน public internet** (Iden research) = fine-able exposure ในทันที
- **Winners = agent governance infrastructure** — Snowflake Cortex AI Gateway + Hush Security ($30M Series A 28 ก.ค.) + Aembit/1Password/SailPoint/Saviynt + Cognizant Frontier Certified compliance workforce + Palantir AIP audit layer. **Losers**: startup ที่ยัง ship agent ไม่มี OTel trace + identity scoping + kill switch — ต้อง retrofit ก่อน enterprise ยอมเซ็น contract

## เกิดอะไรขึ้น

วันเสาร์ 2 สิงหาคม 2026 European Commission ประกาศว่า **European AI Office มีอำนาจเต็มในการ investigate + enforce EU AI Act ต่อ GPAI (general-purpose AI models) provider** — เป็น "enforcement phase" ที่ Wilson Sonsini เรียกว่า start of the real regulatory era. อำนาจของ Commission ครอบคลุม: (1) request documentation + information จาก GPAI provider ทุกราย, (2) conduct evaluations (Commission เข้าถึง model ได้เพื่อ test), (3) request corrective measures, (4) risk mitigation + market restriction, (5) recall/withdrawal จาก EU market, (6) **fines สูงสุด €15M หรือ 3% ของ worldwide annual turnover** แล้วแต่จำนวนไหนสูงกว่า. Prohibited AI practices (social scoring, manipulative techniques, real-time biometric surveillance ใน public space) ก็เข้ามาอยู่ใน enforcement scope วันเดียวกัน.

**Timeline gap ที่ปิดวันนี้ = สาเหตุที่ตลาดยังไม่ปรับตัวเต็มที่**. GPAI obligations เอง (transparency requirement, technical documentation, EU copyright, systemic risk assessment ที่ >10^25 FLOPs) มีผลตั้งแต่ **2 ส.ค. 2025** — แต่ Commission ไม่มี enforcement power เต็มจนกว่าจะครบ 12 เดือน "grace period". วันนี้ (2 ส.ค. 2026) grace period จบ. GPAI provider ที่ release ก่อน 2 ส.ค. 2025 (ChatGPT/GPT-4/Claude 3/Gemini 1.5 series) ยังมี extra 12 เดือน — ต้อง compliant ก่อน 2 ส.ค. 2027. GPAI ที่ release **หลัง** 2 ส.ค. 2025 (GPT-5, Claude 4.x/Opus 4.7, Gemini 2/3, Grok 3-4, Llama 4, Mistral Large 2, DeepSeek V3-V4, Qwen 3) = **compliant ตั้งแต่วันนี้**.

Help Net Security รายงานว่า Commission จะ prioritize "systemic risk" GPAI ก่อน — model ที่ compute >10^25 FLOPs หรือ deploy ใน critical sector. Beam.ai + Compliance Hub ระบุว่า enforcement pattern จะเริ่ม compliance audit **ภายใน 60-90 วัน** จาก enforcement date — เท่ากับ Commission จะทวงเอกสารรอบแรกช่วง ต.ค.-พ.ย. 2026. GPAI Code of Practice ที่ EC เผยแพร่ ก.ค. 2025 = playbook practical — provider ที่ sign Code จะได้ regulatory sandbox + reduced compliance overhead. Anthropic, Google, Microsoft, Mistral sign แล้ว; **OpenAI ยังไม่ sign** — จะเป็น first target ของ enforcement scrutiny

**สิ่งที่กระทบ agent deployment โดยตรง** = EU AI Act ตีความ "agent" ที่ deploy GPAI = subject to Article 51-56 obligations (transparency, documentation, incident reporting) + potentially high-risk classification ตาม Annex III (ถ้า agent ทำงานใน HR, credit scoring, critical infrastructure, education, law enforcement, migration, justice — 8 sector). Provider ที่ deploy agent workflow ที่ hit high-risk criteria ต้องมี: risk management system, data governance, technical documentation, human oversight, transparency, accuracy/robustness/cybersecurity, conformity assessment. **>1,800 MCP server ที่ยังไม่มี authentication บน public internet** (Iden research ต้น 2026) — ถ้า enterprise EU deploy agent ที่ call MCP server เหล่านี้ = potential fine เพราะไม่มี audit trail + identity control + risk mitigation

## ทำไมสำคัญ

**EU AI Act enforcement live = end of "move fast + break things" agent era** — 12 เดือนที่ผ่านมา startup + enterprise ทั่วโลก ship agent ที่ compose GPAI + MCP + custom tool โดยไม่ต้องคิดเรื่อง audit trail จริงจัง. **วันนี้ทุก agent ที่ touch EU market มี €15M/3% turnover fine exposure**. สำหรับ US big tech (Google $348B rev → 3% = $10.4B fine cap; Microsoft $270B → 3% = $8.1B; Amazon $637B → 3% = $19.1B; Meta $164B → 3% = $4.9B) fine ที่ €15M เล็กมาก — แต่ **market restriction + recall order** เป็น existential threat. Commission มี track record ของ Digital Services Act enforcement (Meta fine €200M Apr 2025, Apple €500M) — บอกว่าจะใช้อำนาจจริง

**Pattern การ compliance จะไล่ตาม GDPR playbook** — GDPR ประกาศ 2016, enforcement start 25 May 2018, first major fine (British Airways £183M) ก.ค. 2019 = **14 เดือน**. AI Act enforcement start 2 ส.ค. 2026 → คาดการณ์ first major GPAI fine **Q4 2027**. ในระหว่างนั้น enterprise + startup ต้อง (1) audit ทุก GPAI ที่ใช้ ว่า sign Code of Practice หรือไม่, (2) map data flow ที่ agent touch, (3) implement human oversight + kill switch + incident reporting, (4) certify agent workflow ที่ hit Annex III high-risk category

**สำหรับ agent governance vendor = tailwind ทันที**. Snowflake Cortex AI Gateway (28 ก.ค.) + Hush Security $30M Series A (28 ก.ค.) + Aembit + 1Password + SailPoint + Saviynt = ecosystem ที่ enterprise เอาไป check compliance box. Palantir AIP + ServiceNow AI Control Tower + Cisco Cloud Control ก็ position ตัวเองเป็น "AI Act ready by default". **SI channel (Cognizant, Deloitte, Accenture, PwC)** ที่ certify workforce = ได้ regulatory tailwind — enterprise ที่ต้อง audit + document ในเวลาจำกัด จะจ้าง SI ก่อน hire in-house

**Second-order effect ต่อ MCP protocol** — MCP 2026-07-28 spec (stateless core, mandatory OAuth/OIDC, versioned extensions, private network tunnels) ที่ Anthropic ship เมื่อ ก.ค. **จะเป็น de facto standard สำหรับ EU deployment** เพราะ built-in authentication + audit. MCP server ที่ยัง run บน spec เก่า (no auth) จะ deprecate เร็วขึ้น — 1,800+ server ที่ Iden พบต้อง migrate ก่อน enterprise ยอมใช้. **MCP registry + gateway (Snowflake Cortex, AWS AgentCore Gateway, Google Managed Agents MCP)** = compliance layer ที่ enterprise force ให้ทุก agent traffic ผ่าน

## มุม AI Agent Platform

**สำหรับ builders:** ถ้า agent ของคุณ touch EU market หรือ EU citizen data — **ทำ 3 อย่างภายใน 30 วัน**: (1) audit ทุก GPAI dependency (ChatGPT, Claude, Gemini, Grok, Mistral, DeepSeek) — sign Code of Practice หรือไม่, systemic risk classification, technical documentation; (2) implement audit trail (OTel span ต่อ tool call, user action log, decision provenance) + human oversight checkpoint; (3) MCP server + tool integration ต้องผ่าน gateway (Snowflake Cortex, AgentCore Gateway, Foundry) หรือมี built-in OAuth/OIDC. **Kill switch = mandatory** — Commission ระบุชัดว่า "ability to shut down + rollback" เป็น required capability. Startup ที่ pitch agent ไม่มี audit + kill switch จะ lose EU enterprise deal ตั้งแต่ Q4 2026

**สำหรับ users/business:** Enterprise ที่ deploy agent ใน EU (หรือ serve EU customer) — **launch AI Act compliance audit ภายในสัปดาห์นี้**. Priority: (1) inventory ทุก agent + GPAI ที่ใช้ + tool/MCP endpoint, (2) map ต่อ Annex III high-risk category (HR/credit/education/critical infra/justice/migration) — agent ที่ hit ต้อง conformity assessment เต็มรูปแบบ, (3) documentation + incident response plan, (4) DPO + Legal review contract กับ GPAI provider (data processing agreement, EU representative). **Thai enterprise ที่ export หรือมี EU subsidiary** (PTT Global Chemical EU, CP Group ผ่าน Charoen Pokphand EU, Central Retail Selfridges Group, Thai Union Foods, MFEC EU office, SCB EU branch) — trigger compliance program ทันที; ถ้ายังไม่มี ให้ hire SI (Cognizant + Deloitte + PwC มี EU compliance practice) ก่อน Q4

**สำหรับ ecosystem:** Winner — **compliance/governance vendor** (Snowflake Cortex, Hush, Aembit, 1Password, SailPoint, Saviynt, Palantir AIP, ServiceNow Control Tower, Cisco Cloud Control), **enterprise SI ที่มี AI Act practice** (Cognizant Frontier Certified, Deloitte AI Institute, PwC AI Lab, EY Fabric), **MCP gateway** (Snowflake, AWS AgentCore, Google Managed Agents, Cloudflare Agents). Loser — **model provider ที่ไม่ sign Code of Practice** (OpenAI จะเผชิญ scrutiny แรกก่อน; xAI ก็ยังไม่ sign) — enterprise EU จะเลี่ยง OpenAI/xAI direct integration แล้วผ่าน hyperscaler (Azure OpenAI, AWS Bedrock) ที่มี compliance wrapper. **Enabridge angle**: Thai SI ที่ position เป็น "AI Act compliance-first architect" (audit agent workflow + document ตาม Annex III + implement kill switch/OTel/OAuth) จะ open door เข้า EU-linked Thai enterprise + ASEAN multinational subsidiary. **Package deal**: audit ($50-100K) + implementation ($150-300K) + ongoing DPO service ($20K/เดือน) = TAM ที่ Thai SI แข่งกับ Big 4 ได้เพราะ price point เหมาะ mid-market

## Sources
- [EU AI Act Enforcement Phase Begins — Wilson Sonsini](https://www.wsgr.com/en/insights/eu-ai-act-enforcement-phase-begins.html)
- [EU begins enforcing AI Act, putting AI models under the microscope — Help Net Security](https://www.helpnetsecurity.com/2026/08/04/eu-ai-act-enforcement-ai-models/)
- [EU AI Act 2026: GPAI Enforcement & 3% Fines Begin — Beam.ai](https://beam.ai/agentic-insights/eu-ai-act-enforcement-august-2-2026-gpai-fines)
- [EU AI Act GPAI Enforcement Goes Live August 2, 2026 — ComplianceHub.Wiki](https://compliancehub.wiki/eu-ai-act-gpai-enforcement-august-2026-readiness/)
- [Enforcement of Chapter V under the EU AI Act — artificialintelligenceact.eu](https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/)
- [European Commission Issues Guidelines for Providers of General-Purpose AI Models — WilmerHale](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250724-european-commission-issues-guidelines-for-providers-of-general-purpose-ai-models)

---

## Audio script
วันเสาร์ 2 สิงหาคม European Commission ประกาศว่า European AI Office มีอำนาจเต็มในการ investigate และ enforce EU AI Act ต่อ GPAI provider. อำนาจครอบคลุม request documentation, conduct evaluations, corrective measures, market restriction, recall จาก EU market. Fine สูงสุด 15 ล้านยูโร หรือ 3% ของ worldwide annual turnover แล้วแต่จำนวนไหนสูงกว่า. GPAI obligations เอง มีผลตั้งแต่สิงหาคมปีที่แล้ว แต่ enforcement power เพิ่งเปิดใช้วันนี้ — grace period 12 เดือนจบแล้ว.

Signal ที่กระทบ agent deployment ทั่วโลก — ทุก enterprise ที่ deploy agent ที่ใช้ GPAI ใน EU market ต้องมี audit trail risk mitigation และ documentation ทันที. มากกว่า 1,800 MCP server บน public internet ที่ยังไม่มี authentication = fine-able exposure ในทันที. Commission จะ prioritize systemic risk GPAI ก่อน — คาดการณ์ first major fine ราว Q4 2027 ตาม GDPR pattern.

Winner — agent governance infrastructure ทั้ง Snowflake Cortex AI Gateway, Hush Security ที่เพิ่ง raise 30 ล้านดอลลาร์ Series A, Aembit, 1Password, SailPoint, Saviynt. Palantir AIP กับ ServiceNow AI Control Tower position เป็น AI Act ready by default. SI channel ที่ certify workforce จะได้ regulatory tailwind. Loser — model provider ที่ไม่ sign Code of Practice โดยเฉพาะ OpenAI กับ xAI จะเผชิญ scrutiny แรกก่อน. สำหรับ Enabridge — Thai SI ที่ position เป็น AI Act compliance-first architect audit agent workflow และ implement kill switch OTel OAuth จะเปิดประตูเข้า EU-linked Thai enterprise. Package deal audit บวก implementation บวก DPO service = TAM ที่ Thai SI แข่งกับ Big 4 ได้ในราคาที่เหมาะ mid-market.
