---
date: 2026-08-03
slug: aws-bedrock-agents-classic-shutdown-agentcore-mcp-2026
topic: openbridge-trend
reading_time_min: 4
sources: 6
image_prompt: |
  Editorial isometric composition of an AWS-orange server rack labeled
  "BEDROCK AGENTS CLASSIC" with an "EVICTION NOTICE" tag hanging from
  it, lights dim. Behind it, a taller sleek rack labeled "AGENTCORE"
  glows bright with a modular grid of green pods labeled "GATEWAY",
  "MEMORY", "RUNTIME", "OBSERVABILITY", "IDENTITY". A stat banner reads
  "NEW CUSTOMERS CLOSED 30 JUL 2026" and a badge shows
  "MCP 2026-07-28 NATIVE". Deep navy + AWS orange + green accents,
  chiaroscuro editorial style, 1:1 aspect, no real human faces, text
  crisp at 200px thumbnail.
image: images/26-08-03-0612-02-aws-bedrock-agents-classic-shutdown-agentcore-mcp-2026.png
---

# AWS ทิ้ง Bedrock Agents Classic 30 ก.ค. — บังคับ enterprise ทั้งตลาดเดิน AgentCore + MCP 2026-07-28 ก่อน re:Invent

## TL;DR
- **30 ก.ค.** — AWS ประกาศ **Bedrock Agents Classic (launched พ.ย. 2023) ปิด new-customer signup**, ย้ายเข้า maintenance mode; model catalog freeze ที่ snapshot 30 ก.ค.; existing workload ยังรันได้แต่ AWS "strongly recommend migration ไป AgentCore"
- แทนที่ด้วย **Amazon Bedrock AgentCore** — modular platform ที่แยก Runtime / Gateway / Memory / Identity / Observability เป็น service ต่างหาก, GA ตุลาคม 2025 ในภูมิภาค us-east-1 + us-west-2, ขยาย 4 region เพิ่มมิถุนายน 2026
- **AgentCore Gateway = ประกาศ native support MCP 2026-07-28 spec** (blog post 29 ก.ค.) — ทำให้ AWS ผลักเข้าสู่ position "managed MCP router" ตัวแรกใน hyperscaler
- Timing สำคัญ: **AWS re:Invent อยู่ 30 พ.ย. – 4 ธ.ค.** — enterprise ที่ยังใช้ Bedrock Agents Classic มี 4 เดือน migrate ก่อนถูก question ทาง financial pressure จาก AWS TAM

## เกิดอะไรขึ้น

30 กรกฎาคม AWS อัปเดต Bedrock Agents documentation ให้กลายเป็น **Amazon Bedrock Agents Classic — maintenance mode**. Effective ทันที: **ไม่รับ new customer**, model catalog ถูก freeze (ทั้ง Anthropic Claude 4.7/5, GPT-5.4/5.6, Nova, Llama 4 — snapshot ณ 30 ก.ค.), existing workload ยังรันได้แต่ AWS "strongly recommend migration ไป AgentCore ภายในไตรมาส 4". Existing IaC template (CloudFormation, CDK, Terraform) ที่ create agent ใหม่จะ work ต่อสำหรับ allowlisted account เท่านั้น. ไม่มี hard deadline ประกาศให้ existing customer แต่ TAM (Technical Account Manager) เริ่ม outreach direct ให้ enterprise scope migration plan.

AgentCore ที่จะรับช่วง เป็น **modular platform** ต่างจาก Agents Classic ที่เป็น monolith. แยก 5 service: **Runtime** (agent execution + sandboxing), **Gateway** (tool routing + MCP proxy), **Memory** (short + long-term recall), **Identity** (IAM-integrated auth + delegated permission), **Observability** (traces + audit + policy control). GA ตั้งแต่ ตุลาคม 2025 ใน us-east-1 + us-west-2; มิถุนายน 2026 ขยาย us-east-2, eu-west-1, ap-southeast-1, ap-northeast-1 (Singapore + Tokyo — สำคัญกับ Thai enterprise). **AWS ML Blog วันที่ 29 ก.ค. (หนึ่งวันหลัง MCP spec)** ประกาศ AgentCore Gateway = **native MCP 2026-07-28 support** — enterprise เอา MCP server registered ใน Gateway ได้ทันที, มี built-in IAM + throttling + audit + WAF, bill per request

Feature ที่ AgentCore มี Classic ไม่มี: **multi-agent orchestration** (agents share memory + delegate task via A2A protocol), **AgentCore Policy** (fine-grained governance rule ที่ GA ใน March 2026), **Quality Evaluations** (built-in eval harness), **Session as first-class resource** (session ID, replay, snapshot), **Fully Managed Knowledge Bases** (RAG pipeline ที่ ship ก.ค. — คู่กับ Web Search on AgentCore). Werner Vogels (AWS CTO) โพสต์ X ในวันประกาศ: "Classic did its job — got 40k+ customers to production. AgentCore is the next 4 million."

## ทำไมสำคัญ

**AWS ประกาศตายของ agent 1.0 architecture** — model + tool + prompt ที่ pack เป็น monolith. Bedrock Agents Classic (nov 2023) เป็น response แรกของ AWS ต่อ ChatGPT tool-use, สร้างขึ้นก่อน MCP + A2A + AgentCore pattern จะเกิด. Architecture นั้นดี pilot ไม่ดี scale — enterprise บ่นเรื่อง cold start, session persistence, multi-agent coordination, cross-account permission มาตลอดปี 2025. **Deprecation ไม่ใช่ surprise แต่ timing คือ signal** — AWS เลือก ประกาศหลังจาก MCP 2026-07-28 spec ปล่อย 2 วัน = ต้องการวาดภาพ AgentCore = "MCP-native platform" ที่ Bedrock Agents ไม่มีทางเป็น

**Hyperscaler เดิน move เดียวกันหมด**. Microsoft Azure AI Foundry ปิด Prompt Flow legacy ใน มิถุนายน, ผลักไป Agent Service + Copilot Studio unified stack. Google Cloud ทิ้ง Vertex AI Studio Legacy ใน เมษายน, ทุกอย่างไปที่ Gemini Enterprise Agent Platform. **ตอนนี้ AWS ตาม** — cycle เดียวกันของทุกคน: agent 1.0 (2023-2024 monolith) → agent 2.0 (2025-2026 modular + MCP + A2A). Pattern นี้ทำให้ enterprise **ไม่สามารถอ้างว่า "รอดูก่อน"ได้อีก** — ทุกคลาวด์บังคับ upgrade ในไตรมาสเดียวกัน

**AgentCore Gateway = MCP router ตัวแรกที่ hyperscaler ship**. เมื่อ MCP spec ใหม่ทำให้ MCP server รันบน serverless ได้ทันที, ผู้ต้องมี **router / policy / audit layer** ตรงกลาง คือ enterprise ที่ deploy หลายร้อย MCP server — AWS เห็นก่อนว่า AgentCore Gateway จะกลายเป็น API Gateway equivalent ของยุค agent. Bill per request, มี WAF integration, integrate CloudWatch + IAM + Secrets Manager. **Azure API Management + Google Cloud API Gateway จะตามใน 4-8 สัปดาห์** — และเมื่อทั้งสามมี "managed MCP router" service, category นี้จะเกิดเป็น line-item budget ใหม่ใน enterprise cloud contract

## มุม AI Agent Platform

**สำหรับ builders:** ถ้า agent build บน Bedrock Agents Classic — **migration ไป AgentCore เป็นงาน mandatory ก่อน re:Invent** (30 พ.ย.). AWS ปล่อย migration toolkit + reference architecture; แนะนำเริ่มด้วย non-critical workload (internal Q&A, log summarization) เพื่อ validate เอา main revenue-generating agent ตามหลัง. Focus 3 gap ที่ Classic → AgentCore differ ชัด: (1) tool ต้อง register ผ่าน Gateway (MCP-based) ไม่ใช่ inline schema เดิม, (2) memory ต้อง explicit ผ่าน AgentCore Memory (short + long-term separate), (3) session state ต้อง treat เป็น managed resource — snapshot + replay + delete มี audit trail

**สำหรับ users/business:** Enterprise ที่ใช้ Bedrock Agents Classic (คาด 15-25K account จาก 40K+ ที่ AWS อ้าง reached production) — **budget owner ต้องเรียก TAM คุย migration timeline ภายในสิงหาคม**. Cost implication: AgentCore charging model (per-runtime-second + per-gateway-request + per-memory-op) ต่างจาก Classic (per-invocation) — บาง workload ถูกลง 30-50%, บาง workload แพงขึ้น 20-40% ขึ้นกับ pattern. **สำหรับ Thai enterprise**: AgentCore เพิ่งเข้า ap-southeast-1 (Singapore) มิถุนายน — SI ที่ pilot Bedrock Agents Classic ปีที่แล้ว (Bluebik, G-Able, MFEC, ACI) ต้อง re-scope proposal ทันที; SET50 ที่รอ ap-southeast-7 (Bangkok region เปิด Q1 2026) มี option deploy production ในประเทศ

**สำหรับ ecosystem:** Winners — **LangChain, LlamaIndex, CrewAI, Mastra** (agent framework ที่ position ตัวเองเป็น cloud-agnostic — enterprise ที่กลัว vendor lock จะเลือกใช้เพื่อ build once deploy anywhere), **Portkey, LiteLLM, Databricks Mosaic AI Gateway** (MCP-native routing gateway ที่ AgentCore Gateway ไม่ครอบ), **Cloudflare Workers + Vercel** (serverless MCP hosting ที่ต่างจาก AWS-native). Losers — **framework ที่ tight couple กับ Bedrock Agents Classic API** (Semantic Kernel Bedrock adapter, some Chainlit integrations), **CDK/CloudFormation templates ที่ community เขียนใน 2024** — deprecated ทันที. Anthropic + OpenAI ยัง neutral: Claude + GPT ยังเป็น top-2 model บน AgentCore

## Sources
- [Amazon Bedrock Agents Classic maintenance mode — AWS Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html)
- [How AgentCore Gateway supports the MCP 2026-07-28 spec — AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/how-agentcore-gateway-supports-the-mcp-2026-07-28-spec/)
- [AWS Just Killed Bedrock Agents — ServerGurus](https://servergurus.com/blog/aws-bedrock-agentcore-2026)
- [My Robot Accountant Got an Eviction Notice — DEV Community](https://dev.to/aws-builders/my-robot-accountant-got-an-eviction-notice-so-we-moved-migrating-from-bedrock-agents-classic-to-4bjo)
- [Amazon Bedrock AgentCore now available in four additional AWS Regions — AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-four-additional-regions/)
- [AWS Bedrock AgentCore Makes the Agent Session a Cloud Resource — RohitAI](https://rohitai.com/blog/aws-bedrock-agentcore-managed-agent-stack)

---

## Audio script
วันที่ 30 กรกฎาคม AWS ประกาศปิด Bedrock Agents Classic สำหรับลูกค้าใหม่. เป็น service agent ตัวแรกของ AWS ตั้งแต่พฤศจิกายน 2023. Model catalog ถูก freeze, workload เดิมยังรันได้ แต่ AWS strongly recommend migrate ไป AgentCore ก่อนไตรมาส 4.

AgentCore ต่างจาก Classic ที่เคยเป็น monolith — แยกเป็น 5 service คือ Runtime, Gateway, Memory, Identity, Observability. เพิ่งประกาศเมื่อวานว่า Gateway จะ native support MCP spec 2026-07-28 ที่เพิ่งออกวันที่ 28 กรกฎาคม. หมายความว่า AWS วาดตัวเองเป็น managed MCP router ตัวแรกใน hyperscaler.

Signal ใหญ่กว่า — hyperscaler ทุกเจ้าทำ move เดียวกันหมด. Microsoft ปิด Prompt Flow legacy เดือนมิถุนายน. Google ทิ้ง Vertex AI Studio Legacy เมษายน. AWS ตามวันนี้. Enterprise ไม่มีทางเลือกอีก — agent 1.0 architecture ตายในไตรมาสเดียวกัน. Timing สำคัญ — re:Invent อยู่ 30 พฤศจิกายนถึง 4 ธันวาคม. Enterprise ที่ยังใช้ Bedrock Agents Classic มี 4 เดือน migrate ก่อนถูก financial pressure จาก TAM. สำหรับ Thai enterprise ที่ deploy production บน ap-southeast-1 Singapore — SI ต้อง re-scope proposal ทันที เพราะ AgentCore charging model ต่างจาก Classic; บาง workload ถูกลง 30-50% บาง workload แพงขึ้น 20-40%.
