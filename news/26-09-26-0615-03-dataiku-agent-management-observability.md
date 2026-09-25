---
date: 2026-09-25
slug: dataiku-agent-management-observability
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  A dramatic editorial isometric enterprise control tower at night, a large
  central radar screen labeled "AGENT INVENTORY". Around it, eight docking
  bays each carrying a stylized logo silhouette: AWS Bedrock, Databricks,
  Google Vertex, Microsoft Copilot Studio, Azure Foundry, Salesforce
  Agentforce, Snowflake Cortex, Dataiku. Small agent-drones fly between
  bays, each tagged with a colored risk band (green, yellow, red). Foreground
  KPI card reads "LESS THAN 1 IN 5 ORGS HAVE A COMPLETE AGENT INVENTORY".
  Editorial isometric style, brand-neutral except logo silhouettes, 1:1
  aspect, big contrasty text sized to read at 200px thumbnail, no real
  human faces.
image: images/26-09-26-0615-03-dataiku-agent-management-observability.png
---

# Dataiku launch Agent Management — ตัว inventory + observability สำหรับ agent ที่รันข้าม 8 platform, จับ agent sprawl ที่ enterprise เพิ่งเริ่มมองเห็น

## TL;DR
- **24 ก.ย. — ที่งาน Dataiku Succeed** — Dataiku ประกาศ **Agent Management** เป็น **standalone product** ที่ find + measure + tier ทุก AI agent ที่ enterprise รัน ข้าม platform ทั้งหมด. GA ตุลาคม 2026. Pricing per-instance annual + metered per-agent monitoring
- Support 8 platform หลัก: **AWS Bedrock, Databricks Agents, Google Vertex, Microsoft Copilot Studio, Azure AI Foundry, Salesforce Agentforce, Snowflake Cortex, Dataiku เอง** + **OpenTelemetry** สำหรับ custom platform. เป็น cross-platform inventory ตัวแรกที่ครอบทุกเจ้าใหญ่พร้อมกัน
- ตัวเลขจาก IBM "AI in Motion" ที่ Dataiku quote: **fewer than 1 in 5 enterprise มี complete inventory ของ AI system ที่ตัวเองรัน** — และ Dataiku วางตัวเองเป็น "Agent DLP + FinOps + Governance" ใน layer ที่ยังไม่มี dominant vendor. Fits pattern เดียวกับ AIR ($50M seed, ก.ย. 1) และ Respan Span-1 — **agent observability กำลังกลายเป็น category**

## เกิดอะไรขึ้น

**24 กันยา 2026** ที่ **Dataiku Succeed** (annual conference ของ Dataiku ที่ NYC) — Dataiku ประกาศ **Agent Management** เป็น standalone product line ที่แยกจาก core Dataiku DSS platform. Product ไม่ได้ build agent ให้; **มัน find agent ที่ tenant enterprise มีอยู่แล้ว** ในระบบทั้งหมด — โดยเชื่อมกับ management API ของ 8 platform หลัก + OpenTelemetry สำหรับ custom deployment

Core capabilities มี 3 layer: **(1) Inventory** — auto-discover agent ทุกตัวที่รันใน AWS Bedrock, Databricks Agents, Google Vertex, Microsoft Copilot Studio, Azure AI Foundry, Salesforce Agentforce, Snowflake Cortex, Dataiku เอง. Cross-reference กับ IAM + procurement records เพื่อ flag orphan agent (ไม่มี owner). **(2) Performance monitoring** — tracked ทั้ง technical metrics (latency, error rate, token cost, tool-call failure) + business KPI (task completion, revenue impact, user satisfaction) — layer นี้ต่างจาก APM ทั่วไปเพราะมี LLM eval ในตัว. **(3) Risk tiering** — score agent ตาม data access scope, action reversibility, exposure ต่อ external input, compliance zone (HIPAA, GDPR, SOC2). Agent risk-tier สูง = trigger review workflow อัตโนมัติ

Pricing model: **per-instance annual license** (ราคายังไม่ public แต่ analyst estimate $50k–500k ต่อปีขึ้นกับ enterprise size) + **metered per-agent monitoring** — ยิ่ง agent เยอะยิ่งจ่าย. GA เดือน **ตุลาคม 2026**. Dataiku CTO บอกว่า design เข้ามาตอบ **"disconnect between how fast agents are being created and how organizations observe them"** — ตัวเลข IBM "AI in Motion" research (Q2 2026) ที่ Dataiku quote บอก **น้อยกว่า 1 ใน 5 enterprise มี complete, current inventory ของ AI system ตัวเอง**

## ทำไมสำคัญ

**Agent observability กำลังกลายเป็น category ที่มีตัวเลข**. เดือน ก.ย. 2026 เห็น pattern ชัด: **AIR ปิด seed $50M (Sep 1)** — vet agent skills + block malicious ones. **Respan** — trace + eval + gateway ที่ประมวลผล 2T token/เดือน. **Dataiku Agent Management (Sep 24)** — enterprise inventory ครอบ 8 platform. **Salesforce Agentforce Command Center** (จาก Dreamforce 15 ก.ย.). **Google ADK Agent Registry** (จาก Cloud Next 26 ก.ย.). ทั้งหมดพูดเรื่องเดียวกัน — "เรามี agent เยอะเกินไปแล้ว, ไม่รู้ว่ามัน running อะไรบ้าง, ไม่รู้ว่ามัน cost เท่าไหร่, ไม่รู้ว่ามันทำ compliant หรือไม่"

Pattern historical ที่ควรเทียบ: **DevOps → observability**. ปี 2013–2015 Datadog + New Relic + Splunk แข่งกันครอง APM layer หลังจาก microservices explode. ปี 2019–2021 ChatOps + Kubernetes observability (Sysdig, Grafana) เป็น wave 2. ปี 2023–2025 LLM observability wave 3 (Langfuse, Arize, LangSmith, Braintrust). **Agent observability = wave 4** — ต่างจาก LLM observability เพราะ agent = LLM + tool + memory + workflow + long-running state; observability ต้อง surface **causality chain** ไม่ใช่แค่ log. **Dataiku bet** = enterprise-first, cross-platform, governance-heavy. **AIR bet** = security-first, skill vetting. **Respan bet** = developer-first, eval + trace loop. ทั้งสามอยู่ใน category เดียวกันแต่คนละ persona

จุดที่ต้องจับตา: **cross-platform vs single-platform tension**. Dataiku bet ว่า enterprise ต้องการ observability ที่ **agnostic** จาก platform — เพราะ enterprise จริงมี agent ในหลาย cloud + หลาย vendor. แต่ hyperscaler (AWS, Google, MS) กำลัง push observability ใน stack ตัวเอง (Bedrock AgentCore Observability, Vertex Agent Monitoring, Azure AI Foundry Governance). **Enterprise CIO ต้อง trade-off**: use hyperscaler tool ที่ deeper integration แต่ locked-in, vs cross-platform tool ที่ shallow แต่ portable. Historical precedent: Datadog ชนะ AWS CloudWatch มาแล้ว because cross-platform + better UX = ทำ premium. Dataiku วางตัวเองใน spot เดียวกัน — แต่ก็มี risk เจอ Databricks (คู่แข่งตรง) หรือ Snowflake ที่ enterprise ใช้ analytics ตัวเดียวกัน ทำเองในตัว

## มุม AI Agent Platform

สำหรับ **builders** ที่ทำ agent framework หรือ startup agent observability — **positioning ต้อง sharp ทันที**. Landscape ณ 25 ก.ย.: AIR = security angle ($50M เร็ว), Respan = developer eval angle (2T token/เดือน), Dataiku = enterprise governance angle (pricing per-instance + metered), LangSmith/Braintrust = LLM eval ที่ขยายมาเป็น agent, Arize = ML observability incumbent ที่มี agent module. **Position ที่ยังว่าง**: **agent FinOps** (cost attribution + budget alerts + optimization suggestion), **agent testing/CI-CD** (integration test framework สำหรับ agent workflow), **agent contract compliance** (SLA + retry logic + fallback routing). ทีมที่ทำ pure-play "agent monitoring" ธรรมดา — Dataiku กินหมด

สำหรับ **users / business** ที่รัน agent >5 ตัวใน production — **Q4 2026 = deadline ที่ ควร have proper inventory + observability**. Dataiku pricing (per-instance + metered) น่าจะเจ็บ ~$100–500k/year สำหรับ Fortune 500 — เทียบกับ cost ของ compliance violation หรือ agent-caused breach (Spain data protection case ที่ Plugin4Shell disclosure quote = **fine potential €10M+ under GDPR**) แล้ว ROI ชัดเจน. **แนะนำ**: audit ก่อนซื้อ — spreadsheet inventory agent + platform + owner + data scope, ประเมิน gap, แล้วเลือก tool (Dataiku ถ้า multi-platform, hyperscaler-native ถ้า single-cloud). ทีมเล็กที่มี 1–3 agent ยังไม่ต้อง — ใช้ platform-native ก่อน

สำหรับ **ecosystem** — **Dataiku launch นี้เป็นชัยชนะทางอ้อมของ OpenTelemetry standard**. เพราะ Dataiku เลือก OTel เป็น extensibility layer สำหรับ custom platform = enterprise ที่ built custom agent runtime เอง (Cognition Devin, LangGraph deployment, in-house harness) จะต้อง emit OTel traces ตาม convention เพื่อ integrate. **OTel + MCP + A2A** กำลังกลายเป็น **three-legged stool ของ agent interoperability** — tool discovery (MCP), inter-agent communication (A2A), observability (OTel). Vendor ที่ bet ทั้งสามมาตรฐาน (Google, Microsoft, Dataiku, Databricks) = ecosystem play; vendor ที่ push proprietary standard (บาง frontier lab) = walled garden ที่จะเจอ pressure

## Sources
- [Dataiku Launches Agent Management — Dataiku press release](https://www.dataiku.com/company/news/dataiku-agent-management-general-availability)
- [Dataiku debuts cross-platform Agent Management, expands Cobuild building agent — SiliconANGLE](https://siliconangle.com/2026/09/24/dataiku-debuts-cross-platform-agent-management-expands-cobuild-building-agent/)
- [Dataiku Unveils Agent Management to Track Enterprise AI Agents Across Platforms — BigDATAwire](https://www.hpcwire.com/bigdatawire/this-just-in/dataiku-unveils-agent-management-to-track-enterprise-ai-agents-across-platforms/)
- [Dataiku Agent Management: Track Your AI Agents Now — byteiota](https://byteiota.com/dataiku-agent-management-enterprise-ai/)
- [Dataiku Launches AI Agent Management Product Supporting Other Platforms — DigitalToday](https://www.digitaltoday.co.kr/en/view/107408/dataiku-launches-ai-agent-management-product-supports-other-platforms)

---

## Audio script
วันที่ 24 กันยา 2026 ที่งาน Dataiku Succeed ประจำปี ที่ New York — Dataiku ประกาศ product ใหม่ชื่อ Agent Management เป็น standalone product แยกจาก core Dataiku DSS. Product ไม่ได้สร้าง agent ให้ แต่มัน find agent ที่ enterprise มีอยู่แล้วในระบบทั้งหมด โดยเชื่อม API กับ 8 platform หลัก — AWS Bedrock, Databricks Agents, Google Vertex, Microsoft Copilot Studio, Azure AI Foundry, Salesforce Agentforce, Snowflake Cortex และ Dataiku เอง — plus OpenTelemetry สำหรับ custom platform. มี 3 layer หลักคือ Inventory Performance และ Risk tiering. Score agent ตาม data access scope, action reversibility, exposure ต่อ external input และ compliance zone. Pricing per-instance annual + metered per-agent monitoring. GA เดือนตุลาคม. เหตุผลที่ launch — Dataiku CTO quote ตัวเลข IBM AI in Motion research ว่า น้อยกว่า 1 ใน 5 enterprise มี complete inventory ของ AI system ที่ตัวเองรัน. Pattern ที่จับได้เดือน กันยา 2026 — AIR ปิด seed 50 ล้าน วันที่ 1, Respan trace ประมวลผล 2 ล้านล้าน token ต่อเดือน, Salesforce Agentforce Command Center และ Google ADK Agent Registry ล่าสุด. Category agent observability เพิ่งเกิดชัด ๆ ใน 30 วันนี้. Historical parallel ที่ควรเทียบคือ DevOps observability wave 1 ที่ Datadog เอาชนะ CloudWatch เพราะ cross-platform + UX ดีกว่า. Dataiku วางตัวเองใน spot เดียวกันสำหรับ agent — cross-platform, governance-heavy, enterprise-first. สำหรับ builder ที่ทำ agent framework — ถ้าจะเข้า observability category ตอนนี้ pure play monitoring หายไปแล้ว. Position ที่ยังว่างคือ agent FinOps, agent testing CI CD, agent contract compliance. สำหรับ enterprise ไทยที่รัน agent เกิน 5 ตัวใน production — Q4 นี้ควร have proper inventory เพราะ cost ของ compliance violation หรือ agent breach ตาม GDPR อยู่ระดับ 10 ล้านยูโร plus. audit ก่อนซื้อ tool — spreadsheet inventory ก่อน แล้วค่อยเลือก vendor ทีหลัง.
