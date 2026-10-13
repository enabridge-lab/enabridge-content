---
date: 2026-10-13
slug: dataiku-cross-platform-agent-management
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial illustration: a transparent clipboard labeled "AGENT INVENTORY"
  floats above a crowded skyline of mismatched vendor towers — "BEDROCK",
  "VERTEX", "COPILOT STUDIO", "AGENTFORCE", "CORTEX", "FOUNDRY" — all
  getting scanned by a single hovering drone with the word "AGNOSTIC"
  printed on its wing. Large readable text "LESS THAN 1 IN 5" and "FULL
  INVENTORY" at thumbnail size. Dataiku teal + enterprise charcoal on
  deep navy background, flat isometric style, 1:1 aspect, no real human
  faces. Visual metaphor: the sprawl is here, and someone is finally
  counting.
image: images/26-10-14-0615-05-dataiku-cross-platform-agent-management.png
---

# Dataiku ปล่อย Agent Management GA — cross-platform agent inventory ชน single-vendor monitoring ของ hyperscaler

## TL;DR
- 24 ก.ย. **Dataiku** เปิด **Agent Management** ที่งาน Dataiku Succeed; ประกาศ **GA ตุลาคม 2026**. บาง source บอก product page lists ตุลาคม, press release เดิม bluff ว่ากันยายน — timing เลื่อนไปอยู่ใน window นี้
- Integrations: **AWS Bedrock, Databricks, Google Vertex, Copilot Studio, Azure Foundry, Agentforce, Snowflake Cortex, OpenTelemetry** สำหรับ custom runtime
- Map **tool + model + risk + certification + evidence trail** ของแต่ละ agent — "schedule test rerun" สำหรับ high-risk agent เป็น feature ที่ hyperscaler built-in ยังไม่มี
- IBM research ที่ Dataiku อ้าง: **น้อยกว่า 1 ใน 5 ของ organization มี complete inventory ของ AI system ปัจจุบัน** — gap ที่ Dataiku พยายามปิด
- Positioning: single-vendor monitoring ของ AWS Bedrock, Google Vertex, DigitalOcean Agent Learning = **"favor own agent"**; Dataiku positioning เป็น "**agnostic by design**"

## เกิดอะไรขึ้น

24 ก.ย. ที่งาน Dataiku Succeed, Florian Douetteau (CEO) เปิดตัว Agent Management เป็น standalone product ตัวแรกของ Dataiku ที่ **ไม่ require Dataiku DSS deployment**. จุดต่างจาก hyperscaler monitoring (AWS Bedrock Observability, Google Vertex Agent Garden Dashboard, Azure AI Studio Agent Monitor) คือ **cross-platform by design** — Dataiku ไม่ขาย model, ไม่ขาย compute, ไม่ขาย backbone platform → neutral position ที่ hyperscaler ไม่สามารถ claim ได้

Integration list ที่ประกาศ: AWS Bedrock, Databricks, Google Vertex, Microsoft Copilot Studio, Azure AI Foundry, Salesforce Agentforce, Snowflake Cortex Agents, บวก OpenTelemetry สำหรับ custom runtime ที่ enterprise build เอง. Agent Management จะทำ 4 อย่างสำคัญ: (1) **inventory** — รายการ agent ทุกตัวที่ run อยู่ cross platform, (2) **tool + model mapping** — track ว่าแต่ละ agent เรียก tool อะไร + ใช้ backbone model อะไร, (3) **risk classification** — classify agent ตาม impact ของ action + sensitivity ของ resource access, (4) **evidence trail** — เก็บ certification status + known risk + schedule test rerun สำหรับ high-risk agent

Positioning ของ Dataiku ตรง — Clement Stenac (CTO) บอก TechCrunch ว่า "monitoring ของ hyperscaler favor own agent" โดยยกตัวอย่าง: AWS Bedrock Observability บันทึก performance ของ Bedrock agent ได้ดี แต่ **ไม่เห็น agent ที่รันบน Google Vertex หรือ Azure Foundry**. Enterprise ที่ซื้อ 3 cloud + 2 SaaS = agent sprawl ที่ไม่มี single pane of glass. Dataiku อ้าง IBM research ว่า **น้อยกว่า 1 ใน 5 organization มี complete inventory ของ AI system ปัจจุบัน** — ซึ่งคือ compliance gap ที่ regulator เริ่มถาม

Date discrepancy ที่ควรระวัง: Press release เดิมบอก GA กันยายน, product page บอก GA ตุลาคม — Forkast ยืนยันว่า buyer ควร verify timing ตรงกับ Dataiku ก่อน commit RFP. ตัวเลข pricing ยังไม่เปิด; Dataiku ไม่ปล่อย free tier แต่มี **pilot program** สำหรับ enterprise ที่มี multi-platform agent sprawl อยู่แล้ว

## ทำไมสำคัญ

Pattern ที่ชัด: **Agent governance กำลังแตกออกเป็น 3 layer** — (1) **runtime security** (Rein, Lasso, Prompt Security), (2) **identity trust** (Baselayer, Cyera-Oasis), (3) **inventory + lifecycle management** (Dataiku Agent Management, Collibra AI Governance, Credo AI). ค่ายที่ชนะใน layer 3 ต้อง own **integration surface กว้างที่สุด** + **neutral** ต่อ model vendor. Hyperscaler ที่ขาย model + compute ไม่สามารถ claim neutrality ได้ — จึงเป็น gap ที่ independent vendor อย่าง Dataiku ชนะได้

Point of view: Dataiku กำลังเดินทาง pivot ที่สำคัญ — จาก **"ML platform ที่ compete กับ Databricks + Snowflake"** (เส้นทางเดิมที่โดนกิน margin) ไปสู่ **"governance + inventory layer ที่ sit บน Databricks + Snowflake"** (เส้นทางใหม่ที่ Databricks + Snowflake ไม่สามารถทำได้เอง เพราะ conflict of interest). ถ้า pivot สำเร็จ, Dataiku valuation ($3.7B ล่าสุด) จะ re-rate ขึ้น — เพราะ **governance market มี pricing power สูงกว่า ML platform** (compare Collibra + Credo AI growth rate ปี 2026)

ที่น่าสังเกต: **Hyperscaler ที่ลงมาแข่ง** = AWS Bedrock Agent Governance, Google Agent Policy Manager, Azure AI Governance ทุกตัว **ประกาศแล้ว** แต่ยัง single-vendor. ภายใน 18 เดือน hyperscaler จะ expand ไป cross-cloud (เหมือนที่ AWS CloudTrail รองรับ GCP log) — แต่ enterprise customer จะไม่ trust: "monitoring ของ AWS จะ hide weakness ของ Bedrock agent" คือข้อสมมติที่ CIO อายุ 25+ ปีคิดโดย default. Dataiku ชนะที่ **ความไว้ใจ** มากกว่า feature set

Compare กับ DigitalOcean Agent Learning (เมื่อวาน): DO = **vertical integration ภายใน platform เดียว**, Dataiku = **horizontal governance across platform**. ทั้งคู่ไม่ competing — ทั้งคู่ชี้ pattern เดียวกัน: **agent sprawl เป็น enterprise reality แล้ว, และ 2 primitive ที่ enterprise ต้องการเพิ่มคือ "self-improve loop" กับ "cross-platform inventory"**. Vendor ที่ provide 1 ใน 2 จะมีตลาด

## มุม AI Agent Platform

**Builders:** ถ้าคุณสร้าง agent platform / framework — **expose observability + metadata ผ่าน OpenTelemetry หรือ standard protocol** คือ table stake. Framework ที่ไม่ expose metadata (ยังเก็บ log ใน proprietary format) จะ losing enterprise deal เพราะ CISO ขอ Dataiku-compatible agent ซึ่ง require OTel export

**Users / business:** CDO/CISO ที่มี agent รันบน 2+ platform (ตัวอย่าง: AWS Bedrock สำหรับ RAG + Microsoft Copilot Studio สำหรับ productivity + Snowflake Cortex สำหรับ analytics) — Dataiku Agent Management เป็น **first step ก่อน regulator ถาม**. Thai bank + insurance ที่ BOT เริ่มถาม "มี agent กี่ตัวใน production" ภายใน Q1 2027 — ไม่มี inventory = ตอบไม่ได้. ตัวเลือก: Dataiku, Collibra AI Governance, Credo AI — Dataiku ชนะที่ integration breadth, Collibra ชนะที่ existing data catalog relationship, Credo AI ชนะที่ risk assessment depth

**Ecosystem:** **4 ตัวเล่นใน agent governance market** กำลัง pre-consolidation — Dataiku (ex-ML pivot), Collibra (data catalog pivot), Credo AI (greenfield AI governance), IBM watsonx.governance (incumbent enterprise). ภายใน 18 เดือนจะเหลือ 2 brand ใหญ่ หนึ่ง independent + หนึ่ง hyperscaler-aligned. **Hyperscaler ของตัวเอง** จะ cover 70% ของ single-cloud customer; cross-cloud customer จะต้อง independent

## Sources
- [Dataiku Ships Standalone Agent Governance (Forkast)](https://forkast.news/dataiku-ships-standalone-agent-governance-with-a-bet-that-cross-platform-beats-native/)
- [Dataiku Launches Agent Management (AgileBrandGuide)](https://agilebrandguide.com/dataiku-launches-agent-management-to-track-and-manage-performance-of-ai-agents-built-and-running-on-leading-platforms/)
- [Dataiku: Solving AI Sprawl and Risk with Agent Management (AI Magazine)](https://aimagazine.com/news/dataiku-solving-ai-sprawl-and-risk-with-agent-management)
- [Dataiku Agent Management reveals unmonitored AI agents (Help Net Security)](https://www.helpnetsecurity.com/?p=385726)
- [Dataiku launches cross-platform AI agent management tool (IT Brief UK)](https://itbrief.co.uk/story/dataiku-launches-cross-platform-ai-agent-management-tool)

---

## Audio script
Dataiku ปล่อย Agent Management ที่งาน Dataiku Succeed วันที่ 24 กันยายน แล้วประกาศ GA ตุลาคม 2026 เป็น standalone product ตัวแรกของ Dataiku ที่ไม่ต้อง deploy Dataiku DSS คู่กัน จุดต่างสำคัญคือ cross platform by design integrate กับ AWS Bedrock Databricks Google Vertex Microsoft Copilot Studio Azure Foundry Salesforce Agentforce Snowflake Cortex Agents บวก OpenTelemetry สำหรับ custom runtime ทำ 4 อย่างหลักคือ inventory ของ agent ทุกตัว cross platform map tool กับ model ของแต่ละ agent classify risk ตาม impact ของ action และเก็บ evidence trail กับ scheduled test rerun สำหรับ agent risk สูง CTO ของ Dataiku บอก TechCrunch ชัดว่า monitoring ของ hyperscaler favor own agent AWS Bedrock Observability บันทึก performance ของ Bedrock agent ได้ดีแต่ไม่เห็น agent ที่รันบน Google Vertex หรือ Azure Foundry Dataiku อ้าง IBM research ว่าน้อยกว่า 1 ใน 5 organization มี complete inventory ของ AI system ปัจจุบัน Pattern ที่ชัดคือ agent governance กำลังแตกเป็นสาม layer runtime security identity trust และ inventory lifecycle management ค่ายที่ชนะต้อง own integration surface กว้างที่สุดและ neutral ต่อ model vendor hyperscaler ที่ขาย model กับ compute ไม่สามารถ claim neutrality ได้ สำหรับ CDO ไทยที่มี agent รันบนสอง platform ขึ้นไป Dataiku Agent Management คือ first step ก่อน regulator ถาม Bank of Thailand กับสำนักงาน กลต เริ่มถามว่ามี agent กี่ตัวใน production ภายในไตรมาสหนึ่งปี 2027 ถ้าตอบไม่ได้คือ compliance gap ที่ต้องเติมด่วน ภายใน 18 เดือนตลาด agent governance จะเหลือสองค่ายใหญ่ หนึ่ง independent หนึ่ง hyperscaler aligned builder ที่สร้าง agent framework ต้อง expose observability metadata ผ่าน OpenTelemetry หรือ standard protocol เป็น table stake ไม่งั้นหลุด enterprise deal เพราะ CISO ขอ Dataiku compatible agent
