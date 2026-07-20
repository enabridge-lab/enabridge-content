---
date: 2026-07-20
slug: aws-bedrock-agentcore-5x-runtime-web-search
topic: agent-platform-trend
reading_time_min: 3
sources: 3
image_prompt: |
  An editorial illustration of a colossal orange AWS Bedrock server rack
  scaling upward like a skyscraper, with a large glowing dial mounted on
  its front reading "5,000 SESSIONS" (previously "1,000" crossed out). Small
  agent icons stream in from all sides through pipes labeled "200 TPS".
  On the roof: a floating search magnifier icon with a padlock over it,
  labeled "WEB SEARCH · ZERO DATA EGRESS". Bottom banner reads "AGENTCORE
  RUNTIME · JULY 2026". Editorial isometric style, deep navy background,
  orange accent lighting, high contrast, 1:1 aspect, no real human faces.
image: images/26-07-20-0610-03-aws-bedrock-agentcore-5x-runtime-web-search.png
---

# AWS AgentCore เพิ่ม runtime quota 5x + Web Search ในบ้าน: enterprise agent เริ่มเลิกกลัวเรื่อง scale

## TL;DR
- AWS Bedrock AgentCore ยก runtime service quota ขึ้น 5x — active session per account จาก 1,000 → 5,000 (us-east-1, us-west-2), invoke TPS จาก 25 → 200 per agent
- เพิ่ม managed Web Search tool ที่ให้ agent ค้น web โดยไม่มี data egress ออกจาก AWS environment — ตอบโจทย์ compliance ของ FS + healthcare
- Signal: ปีนี้ enterprise agent เริ่มเข้าโหมด production scale จริง ไม่ใช่ pilot อีกแล้ว — AWS ต้องยก quota เพราะลูกค้าชน ceiling

## เกิดอะไรขึ้น
สัปดาห์นี้ AWS ปล่อย release note ชุดใหญ่สำหรับ Amazon Bedrock AgentCore — ตัว managed runtime สำหรับ deploy agent ที่ AWS re:Invent 2025 เพิ่งเปิดตัว. Update ที่สำคัญที่สุดคือ **service quota เพิ่มขึ้น 5x**: active session workload per account จาก 1,000 เป็น **5,000** ใน us-east-1 และ us-west-2 (จาก 500 เป็น 2,500 ใน region อื่น). InvokeAgentRuntime API rate จาก 25 TPS เพิ่มเป็น **200 TPS per agent per account**. New session creation rate สำหรับ container deployment จาก 100 TPM เป็น **400 TPM per endpoint**.

Feature ใหม่อีกตัวที่เพิ่งเปิดคือ **managed Web Search tool** — agent สามารถค้น web แบบ real-time เพื่อ ground response กับข้อมูลปัจจุบัน โดย data residency ยังอยู่ใน AWS environment ที่ลูกค้าคุม, มี zero data egress. AWS ใช้ proprietary web index + structured knowledge graph ของตัวเอง แทนที่จะเรียก Bing / Google ผ่าน API. รวมถึง ActiveSessionCount CloudWatch metric ที่ publish per minute per service type — ให้ ops team ตั้ง alarm เวลา traffic spike และเข้าใจ session quota consumption แบบ real-time.

Feature Web Search นี้ตอบโจทย์ที่ enterprise ในสาย financial services + healthcare + government บ่นมานาน — ทีมจะ deploy agent ต้องใช้ web grounding แต่ compliance ห้าม data ออกนอก AWS boundary. ก่อนหน้านี้เลือกได้แค่ (1) fine-tune knowledge เก็บใน model, (2) ต่อ third-party search API แล้วเสี่ยง audit, (3) ทำ RAG กับ static crawl เอง. AWS ยัดรวมทั้ง search infrastructure + index + governance ไว้ในตัว.

## ทำไมสำคัญ
Quota bump 5x เป็น demand signal ที่ตรงเป้าที่สุดในตลาด agent ปีนี้ — AWS ไม่ยก quota เพราะพักผ่อน, ยกเพราะลูกค้าชน. 6 เดือนก่อน ceiling 1,000 sessions ต่อ account ก็พอสำหรับ pilot ทั่วไป — วันนี้เป็น bottleneck. Andy Jassy พูดในการประชุมนักลงทุน Q1 2026 ว่า "Bedrock ARR crossed multiple billion" และ agentic workload กำลังเป็นตัวขับหลัก — quota bump รอบนี้บอกว่าตัวเลขนั้นจริง.

เทียบ pattern กับคู่แข่ง: Google Gemini Enterprise Agent Platform (เพิ่งเปลี่ยนชื่อจาก Vertex AI Agent Builder) ก็ update runtime ให้รองรับ long-running operation ยาว 7 วัน, sub-second cold start, provisioning น้อยกว่า 1 นาที. Microsoft Copilot Studio + Azure AI Foundry, Salesforce Agentforce 360 (ARR แตะ $1.2B), OpenAI Agent Platform ก็เร่งขยาย runtime ทั้งหมด. คำถามที่ CTO ต้องถามตัวเองไม่ใช่ "agent runtime ควรใช้ของใคร" แต่เป็น "agent runtime ควรใช้ **กี่ตัว**" เพราะ workload แต่ละอย่างเริ่ม fit กับ runtime ต่างกัน — coding agent อยู่บน Anthropic managed, business workflow อยู่บน AgentCore, sales agent อยู่บน Agentforce.

จุดที่น่าจับตาที่สุดคือ Web Search tool — ประเด็นคือ hyperscaler กำลังเปลี่ยน default assumption ของ agent ทุกตัว: agent ต้องมี fresh web knowledge เข้าถึงได้แบบ compliance-safe. ถ้า AWS wrapping Bing / Perplexity / SerpAPI แบบมี governance, agent enterprise จะเลิกใช้ third-party search API. ตลาด search-for-agent (Perplexity, You.com, Exa, Tavily, Serper) จะโดน commoditize เร็ว.

## มุม AI Agent Platform
สำหรับ **builders**: ถ้า framework ของคุณ (LangGraph, CrewAI, Semantic Kernel, custom) ยังไม่มี adapter ที่รอง native runtime ของ hyperscaler (AgentCore, Gemini Enterprise, Copilot Studio), เริ่มทำวันนี้ — enterprise procurement จะเลือก runtime ที่มี VPC / IAM / compliance ในตัว มากกว่า framework ที่ต้อง self-host. Framework จะกลายเป็น "developer experience layer" อยู่บน managed runtime แทน. บวกกับ MCP spec 2026-07-28 ที่จะ ship stateless ในสัปดาห์หน้า, runtime จะเป็นชั้นที่ compete ด้วย ops + governance ไม่ใช่ทันได้อีก.

สำหรับ **users / business**: quota 5x คือ signal ให้เริ่มวางแผน production-scale agent จริงจัง ไม่ใช่ pilot อีก. คำถามที่ต้องตอบตอนออกแบบ deployment คือ concurrency profile (peak sessions, TPS burst), region strategy (residency + quota per region), และ observability contract (ActiveSessionCount alarm, error budget, rollback). สำหรับ **ecosystem**: hyperscaler ทั้ง 3 กำลัง absorb ทั้ง search, memory (Google Memory Bank), voice (Sierra Voice), file I/O, sandbox execution เข้ามาในตัว — vendor พวก vector DB, ephemeral compute, search API ต้องหา wedge ใหม่ที่ hyperscaler ไม่ทำ (specialized vertical index, on-prem, edge, cross-cloud federation).

## Sources
- [AWS: Release notes for Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html)
- [InfoWorld: AWS raises AgentCore runtime quotas by up to 5x](https://www.infoworld.com/article/4192220/aws-raises-agentcore-runtime-quotas-by-up-to-5x-to-help-enterprises-scale-ai-agents.html)
- [AWS: New in Amazon Bedrock AgentCore — broader knowledge and continuous learning](https://aws.amazon.com/blogs/machine-learning/new-in-amazon-bedrock-agentcore-build-agents-with-broader-knowledge-and-continuous-learning/)

---

## Audio script
ข่าวจาก AWS ที่ทีม platform ควรฟังครับ สัปดาห์นี้ AWS Bedrock AgentCore ปล่อย release note ชุดใหญ่ ตัวสำคัญที่สุดคือ service quota เพิ่มขึ้น 5 เท่า active session ต่อ account จาก 1,000 เป็น 5,000 ใน us-east-1 กับ us-west-2 InvokeAgent API rate จาก 25 TPS เป็น 200 TPS ต่อ agent New session creation rate จาก 100 TPM เป็น 400 TPM ต่อ endpoint ทำไมสำคัญ AWS ไม่ยก quota เพราะสนุก ยกเพราะลูกค้าชน ceiling เมื่อ 6 เดือนก่อน 1,000 sessions พอสำหรับ pilot ทั่วไป วันนี้กลายเป็น bottleneck นี่คือ demand signal ที่ตรงเป้าที่สุดในตลาด agent ปีนี้ Feature ใหม่อีกตัวคือ managed Web Search tool ที่ให้ agent ค้น web โดย data residency อยู่ใน AWS ไม่มี egress ออกนอก boundary AWS ใช้ proprietary web index กับ knowledge graph ของตัวเอง แทนที่จะเรียก Bing หรือ Google ผ่าน API เรื่องนี้ตอบโจทย์ financial services กับ healthcare ที่ compliance ห้ามข้อมูลออกนอก AWS ประเด็นคือ hyperscaler กำลังเปลี่ยน default assumption ของ agent ทุกตัว ตลาด search for agent อย่าง Perplexity, Exa, Tavily จะโดน commoditize เร็ว บวกกับ Google Gemini Enterprise Agent Platform ที่รองรับ long running ops 7 วัน sub second cold start Microsoft Copilot Studio Salesforce Agentforce ก็เร่งเหมือนกัน คำถามที่ CTO ต้องถามไม่ใช่ agent runtime ควรใช้ของใคร แต่เป็น ควรใช้กี่ตัว เพราะ workload แต่ละอย่างเริ่ม fit runtime ต่างกัน สำหรับคนสร้าง framework ถ้ายังไม่มี adapter รอง native runtime hyperscaler เริ่มทำวันนี้ครับ enterprise จะเลือก runtime ที่มี VPC IAM compliance ในตัว มากกว่า framework ที่ต้อง self host framework จะกลายเป็น developer experience layer อยู่บน managed runtime แทน
