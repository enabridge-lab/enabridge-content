---
date: 2026-08-08
slug: databricks-unity-ai-gateway-ga-quadrillion-tokens
topic: openbridge-trend
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial isometric illustration of a massive stone gateway arch labeled
  "UNITY AI GATEWAY" bridging two sides — on the left a cluster of AI
  agents, MCP servers (labeled "MCP"), and skill icons; on the right a row
  of model boxes labeled "OPENAI", "ANTHROPIC", "GEMINI", "MISTRAL",
  "LLAMA". Every packet passing through the arch flashes a small "GOVERN"
  stamp. A giant scoreboard above the arch reads "1 QUADRILLION TOKENS /
  YEAR" in bold, with three enterprise logos represented as generic
  building silhouettes tagged "RIVIAN", "ASANA", "EDMUNDS". Orange +
  slate palette (Databricks accent), grid floor, editorial isometric
  style, 1:1 aspect, no real human faces, text sharp at 200px thumbnail.
image: images/26-08-08-0613-02-databricks-unity-ai-gateway-ga-quadrillion-tokens.png
---

# Databricks Unity AI Gateway GA: ควบคุม model + MCP + agent จาก catalog เดียว, 1 quadrillion token/ปี, Rivian/Asana/Edmunds เดิน production

## TL;DR
- **4 ส.ค.** — Databricks ประกาศ **Unity AI Gateway GA** — unified control plane ที่ govern **model, MCP server, agent, skill, tool** ผ่าน Unity Catalog เดียวกับที่ govern table + volume (RBAC + policy + lineage)
- **ตัวเลขก่อน GA** — **1+ quadrillion tokens** (10^15) ผ่าน gateway ใน 12 เดือน; **thousands of enterprise customers** (highlight: **Rivian, Asana, Edmunds**)
- **ครอบคลุม MCP** — govern MCP server เหมือน database resource: allowlist, spending cap, audit log ต่อ agent identity → CISO + FinOps มี single pane of glass
- **มุม Agent Platform** — Databricks กำลัง lock **"agent runtime governance"** ที่ layer data (ใกล้ workload) ไม่ใช่ที่ layer network (Cloudflare) หรือ endpoint (AWS Bedrock AgentCore) — คู่แข่งจริงคือ **Snowflake Cortex AI Gateway** (Black Hat, 5 ส.ค.) กับ **Google Gemini Enterprise Agent Platform**

## เกิดอะไรขึ้น

วันจันทร์ที่ 4 สิงหาคม Databricks ประกาศ **Unity AI Gateway** เข้า **General Availability** — extension ของ Unity Catalog ที่ปกติ govern data (table, volume, model artifact) ขยายไป govern **runtime interaction ระหว่าง agent, model, MCP server, skill, tool**. หน้าที่ 4 อย่าง: (1) **route** AI traffic ข้าม provider (OpenAI, Anthropic, Google, open-weight) ผ่าน connector เดียว, (2) **control** ว่าทีมไหน / user ไหนใช้ service อะไรได้บ้าง (RBAC เหมือน table permission), (3) **govern MCP server** — allowlist, cost cap, audit ต่อ agent, (4) **monitor** — spend, latency, lineage, usage tag แบบเดียวกันกับ data query. ทั้งหมดใน UI + API + Terraform ที่ engineer + IT + finance ใช้ร่วมได้

Databricks เปิดตัวเลข gateway ที่ทำ traffic ก่อน GA: **1+ quadrillion tokens/ปี** (10^15 หรือ 1,000 ล้านล้าน) — เทียบ scale กับ OpenAI ที่รายงาน 15 พันล้าน token/นาที (~7.9 quadrillion/ปี ถ้ายิงตลอด). Customer ที่ vendor highlight: **Rivian** (EV → software update / agent-assisted service), **Asana** (SaaS ที่ embed agent), **Edmunds** (auto marketplace ที่ใช้ agent สำหรับ inventory + pricing). Enterprise gateway ที่ vendor อื่นเปิดในระดับใกล้กัน — Cloudflare AI Gateway, AWS Bedrock AgentCore, Google Apigee-based MCP gateway — ยังไม่มีใครประกาศตัวเลข token throughput ระดับนี้อย่างเป็นทางการ

**Timing ที่กด GA สัปดาห์นี้ = การประกาศ MCP 2026-07-28 spec** ที่ทำให้ MCP กลายเป็น stateless protocol + Extensions framework — เหมาะกับ enterprise runtime แบบ Unity AI Gateway. **MCP มี 400M+ monthly SDK download** (4x YoY, Anthropic รายงาน) → เป็น standard พอที่ enterprise IT ยอมรับ. Databricks pitch = ถ้า agent + MCP + tool คือ "compute + storage + network ยุคใหม่" → Unity Catalog คือ **IAM + policy + observability** ที่ mapping ตรง 1:1 กับสิ่งที่ enterprise คุ้นเคยจาก Snowflake governance / AWS IAM / Azure RBAC — ไม่ต้อง build governance ใหม่จาก scratch

## ทำไมสำคัญ

**Governance คือ blocker หลักของ agent ในองค์กร enterprise ปี 2026.** พ้น pilot ที่ engineer สร้างเอง 1-2 agent, พอต้อง scale ไป 50-100 agent + MCP server หลากหลาย → CISO ถามคำเดียว: **"ใครเห็น data อะไร, ใช้ token เท่าไร, log audit ไปที่ไหน?"** ถ้าตอบไม่ได้, deployment ค้าง. Unity AI Gateway resolve คำถามนั้นด้วย model เดียวกับที่ Databricks ใช้ solve data governance เมื่อ 5 ปีก่อน (Unity Catalog vs. Hive Metastore) — **govern ที่ layer resource, ไม่ใช่ layer network** — ทำให้ policy portable ข้าม cloud + provider

**Battle 3 ทางกำลังชัด**: (1) **Data-plane gateway** (Databricks Unity, Snowflake Cortex Gateway ที่เพิ่ง preview เมื่อ 5 ส.ค. ที่ Black Hat, Palantir AIP) — govern ที่ใกล้ workload; (2) **Network-plane gateway** (Cloudflare AI Gateway + Wallets, AWS Bedrock AgentCore Gateway) — govern ที่ edge; (3) **Endpoint-plane** (Anthropic Claude apps gateway, OpenAI Enterprise governance) — govern ที่ model provider. Enterprise ระดับ Fortune 500 มักจะ **run ทั้ง 3 layer พร้อมกัน** — เพราะ compliance ต้องซ้อน — แต่ **layer ไหนเป็น source of truth ของ policy** จะกำหนดตำแหน่งของ vendor ในการเจรจา 3 ปีข้างหน้า. Databricks ได้เปรียบเรื่อง data lineage ที่ enterprise คุ้นแล้ว; Cloudflare ได้เปรียบเรื่อง edge coverage; hyperscaler ได้เปรียบเรื่อง compute lock-in

**Signal สำหรับ startup gateway/observability** (Portkey, Helicone, Traceloop, LangFuse, Braintrust): พื้นที่ observability + eval ยังโตได้ แต่ **pure gateway** ที่ไม่ผูกกับ catalog governance จะโดน Databricks + Snowflake + Cloudflare squeeze. Path เดียวคือ **specialize เป็น layer สูงกว่า** (agent quality analytics, cost attribution ต่อ business outcome, PII redaction เชิง vertical) หรือ **integrate ไปเป็น partner** ใน Unity Catalog / Snowflake Cortex marketplace ก่อนตำแหน่งจะเต็ม

## มุม AI Agent Platform

**สำหรับ builders:** ถ้า agent framework ของคุณยัง connect model ผ่าน API key hardcode + no policy layer — **integrate Unity Catalog SDK / Snowflake Cortex Gateway / Cloudflare AI Gateway เป็น deploy target** ก่อนสิ้นปี. Enterprise ที่ evaluate framework ปี 2027 จะถามคำถามแรกไม่ใช่ "หน่วยความจำ agent ใช้อะไร" แต่จะเป็น **"agent ของคุณ integrate กับ Unity Catalog / Snowflake Cortex / Cloudflare Gateway ได้ไหม"** — เพราะ CISO ต้อง sign off ก่อนจ่ายเงิน. LangChain, Mastra, Cloudflare Agents SDK, Claude Agent SDK ที่ integrate อยู่แล้วจะได้เปรียบ; framework ที่ยัง lock-in ที่ own runtime จะโดนตัดออกจาก procurement short list

**สำหรับ users/business:** Enterprise ที่ deploy agent — **CISO + head of AI + FinOps ต้องเลือก governance layer หลักภายใน Q4 2026** ก่อนจำนวน agent ทะลุ 10 ตัว. Framework เลือก: (a) ใช้ Databricks/Snowflake อยู่แล้ว → ธรรมชาติจะไป Unity AI Gateway / Cortex Gateway; (b) multi-cloud + Cloudflare heavy → ไป Cloudflare AI Gateway + Wallets; (c) AWS-native → AgentCore Gateway; (d) Google-native → Gemini Enterprise Agent Platform. คำถามที่ต้องตอบ: (1) policy ของเรา **portable** ข้าม provider หรือ lock-in? (2) audit log format compatible กับ SIEM (Splunk, Datadog, Sentinel) เดิมไหม? (3) cost attribution ทำถึงระดับ business unit / cost center หรือแค่ team? (4) มี **kill switch** สำหรับ agent เดี่ยว ๆ ที่พังจริงไหม? สำหรับ **Thai enterprise ระดับ K-Bank / SCB / PTT / AIS** ที่ใช้ Databricks / Snowflake อยู่แล้ว — Unity AI Gateway หรือ Snowflake Cortex Gateway จะเป็น path ที่ต้าน friction น้อยที่สุด (Enabridge team ที่มี Databricks + Snowflake certification ให้ prioritize skill นี้)

**สำหรับ ecosystem:** **Winner:** Databricks + Snowflake (governance moat แข็งขึ้น), MCP protocol (ยิ่งเป็น standard = ยิ่ง gateway ยึด control ได้), enterprise SI ที่ implement governance stack. **Loser ระยะกลาง:** pure LLM gateway startup ที่ไม่ผูกกับ data catalog, agent framework ที่ไม่มี governance integration. **Neutral:** hyperscaler ที่มี gateway ของตัวเอง (AWS/Google/Azure) — จะยังชนะใน account ที่ single-cloud, แต่จะ lose ใน multi-cloud / data-heavy account ที่ Databricks/Snowflake อยู่แล้ว. **Enabridge angle:** ถ้าลูกค้า Enabridge ใช้ Databricks/Snowflake อยู่แล้ว, การเสนอ **Unity AI Gateway (หรือ Cortex Gateway) implementation** เป็น service line ใหม่ที่ upsell ต่อจาก data governance เดิมได้ทันที — ไม่ต้อง sell platform ใหม่, sell การใช้ platform ที่ CFO อนุมัติแล้วให้ครอบ agent-era

## Sources
- [Unity AI Gateway is Generally Available — Databricks Blog](https://www.databricks.com/blog/unity-ai-gateway-generally-available)
- [Databricks Unity AI Gateway Hits GA — StartupHub](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/databricks-unity-ai-gateway-hits-ga)
- [Unity AI Gateway: Multi-AI governance and cost control — Databricks](https://www.databricks.com/product/artificial-intelligence/unity-ai-gateway)
- [Databricks August 2026 release notes](https://docs.databricks.com/aws/en/release-notes/product/2026/august)
- [AI governance at Data + AI Summit 2026: Unity AI Gateway — Databricks Blog](https://www.databricks.com/blog/ai-governance-data-ai-summit-2026-whats-new-unity-ai-gateway)

---

## Audio script
วันจันทร์ที่ 4 สิงหาคม Databricks ประกาศ Unity AI Gateway เข้า General Availability. เป็น extension ของ Unity Catalog ที่ปกติ govern data table volume model artifact ขยายไป govern runtime interaction ระหว่าง agent model MCP server skill tool. ทำ 4 อย่าง route AI traffic ข้าม provider control ว่าทีมไหนใช้ service อะไรได้ govern MCP server allowlist และ cost cap monitor spend latency lineage. ตัวเลขก่อน GA คือ 1 quadrillion token ต่อปี หรือ 1000 ล้านล้าน token thousands ของ enterprise customer โดยเน้น Rivian Asana Edmunds.

Timing ที่กด GA สัปดาห์นี้เพราะ MCP 2026 07 28 spec ทำให้ MCP เป็น stateless protocol เหมาะกับ enterprise runtime. MCP มี 400 ล้าน monthly SDK download 4 เท่า year over year. Databricks pitch คือถ้า agent MCP tool เป็น compute storage network ยุคใหม่ Unity Catalog คือ IAM policy observability ที่ mapping ตรง 1 ต่อ 1 กับที่ enterprise คุ้นเคย ไม่ต้อง build governance ใหม่.

Governance คือ blocker หลักของ agent ในองค์กร enterprise ปี 2026. พ้น pilot ที่ engineer สร้าง 1 2 agent พอ scale ไป 50 ถึง 100 agent CISO ถามคำเดียวว่าใครเห็น data อะไรใช้ token เท่าไร log audit ไปที่ไหน ตอบไม่ได้ deployment ค้าง.

Battle 3 ทางกำลังชัด data plane gateway อย่าง Databricks Unity Snowflake Cortex Palantir AIP govern ใกล้ workload. Network plane อย่าง Cloudflare AI Gateway AWS Bedrock AgentCore govern ที่ edge. Endpoint plane อย่าง Anthropic Claude apps gateway OpenAI Enterprise. Enterprise ระดับ Fortune 500 จะ run ทั้ง 3 layer พร้อมกัน แต่ layer ไหนเป็น source of truth ของ policy จะกำหนดตำแหน่งของ vendor ในการเจรจา 3 ปีข้างหน้า.

สำหรับ Thai enterprise K Bank SCB PTT AIS ที่ใช้ Databricks หรือ Snowflake อยู่แล้ว Unity AI Gateway หรือ Cortex Gateway จะเป็น path ที่ต้าน friction น้อยที่สุด. สำหรับ Enabridge ลูกค้าที่ใช้ Databricks หรือ Snowflake อยู่แล้ว การเสนอ Unity AI Gateway implementation เป็น service line ใหม่ upsell ต่อจาก data governance เดิมได้ทันที ไม่ต้อง sell platform ใหม่ sell การใช้ platform ที่ CFO อนุมัติแล้วให้ครอบ agent era.
