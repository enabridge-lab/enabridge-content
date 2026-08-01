---
date: 2026-08-01
slug: groundcover-100m-series-c-observability-ai-agents
topic: agentic-ai
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial isometric composition. Center: a translucent glass control-room
  console labeled "OBSERVABILITY FOR ENGINEERS + AGENTS", filled with pulsing
  waveform panels — one panel labeled "AGENT TRACE", one "TOOL CALL", one
  "TOKEN COST". Around the console, small silhouetted engineer figures on one
  side and small robotic agent silhouettes on the other, both feeding data
  streams into the console. In the top corner: a bold neon ribbon
  "$100M SERIES C — 250 CUSTOMERS — 3x ARR". Bottom corner: a small "BYOC"
  vault icon (bring your own cloud). Muted indigo + electric-cyan palette,
  dramatic chiaroscuro, flat editorial style, 1:1 aspect, no real human
  faces (silhouettes only), text must render sharply at 200px thumbnail.
image: images/26-08-01-0610-04-groundcover-100m-series-c-observability-ai-agents.png
---

# Groundcover ระดม $100M ทำ observability สำหรับ "engineers + agents" — Datadog ยุค agent-native กำลังฟอร์มตัว, One Peak lead

## TL;DR
- **29 ก.ค.** — Groundcover ปิด **$100M Series C** นำโดย **One Peak**, ร่วม Morgan Stanley Expansion Capital + existing Zeev/Angular/Heavybit/Jibe; total funding แตะ **$160M**
- Metrics: **3x ARR ปีที่แล้ว, 2x workforce, 250+ paying customers ตั้งแต่ early-stage ถึง Fortune 5**, ปิด multiple 7-figure contract ปีที่แล้ว
- Platform: **full-stack observability for engineers & agents** — deploy inside customer cloud (BYOC), visibility ครบ application + infrastructure + AI workload โดยไม่มี operational overhead
- Signal: **Datadog + New Relic pattern ยุค agent-native กำลังเกิด** — observability category ที่ AI workload trace + agent action + cost + eval — เป็น sub-category ใหม่ที่ VC มองเป็น "next $10B category"

## เกิดอะไรขึ้น

วันที่ 29 กรกฎาคม Groundcover ประกาศ **$100M Series C** — round ใหญ่สุดใน observability category สำหรับปี 2026, นำโดย **One Peak** (growth-stage fund ยุโรปที่มี track record ใน enterprise software), พร้อม Morgan Stanley Expansion Capital + existing investors (Zeev Ventures, Angular Ventures, Heavybit, Jibe). Total funding แตะ **$160M**. Growth metric ที่ share ใน announcement: **ARR โต 3x ปีที่แล้ว, workforce เพิ่ม 2x, 250+ paying customer** ตั้งแต่ early-stage startup ถึง **Fortune 5 enterprise**, ปิด **multiple 7-figure contract** ปีที่แล้ว. CEO Shahar Azulay + CTO Yechezkel Rabinovich (ex-cyber; founded ปี 2022) position บริษัทเป็น **"observability platform built for the AI era"**

Platform architecture ที่ทำให้ Groundcover แตกต่างจาก Datadog / New Relic / Grafana: **BYOC (Bring Your Own Cloud) — Groundcover deploy sensor + collector inside customer's cloud premises**, ไม่ส่ง data ออกไปยัง vendor SaaS. เหตุผลที่ enterprise regulated (bank, healthcare, government) สนใจ: **compliance + data residency + cost predictability** (ไม่จ่ายตาม volume-based Datadog pricing model ที่กำลังทำลาย FinOps team ใน AI era). Technical stack: eBPF-based observability agent ที่รันบน node level, capture network flow + application performance + LLM API traffic + agent tool call — **all-in-one deployment**. เดิม Groundcover คือ Kubernetes observability play; 12 เดือนที่ผ่านมา pivot มา cover **AI + agent workload** เต็มตัว

Announcement มี line ที่ตั้งใจให้ industry ฟัง: **"observability for engineers & agents"** — ไม่ใช่แค่ observability สำหรับ human operator ที่ตรวจ log แล้ว. Position: agent ที่รันใน production ต้อง **self-observe** (query metrics ของตัวเอง, adjust behavior), และ human operator ต้อง **observe agent** (audit tool call, replay trace, verify cost per outcome). Datadog's LLM Observability product (launch ปีที่แล้ว) กับ New Relic's AI Monitoring ยัง focus **LLM API level** (prompt in, response out, token count). Groundcover pushing **agent level** — trace หลาย turn, correlate tool call กับ business outcome, cost attribution ต่อ agent-user-action

## ทำไมสำคัญ

**Observability category กำลัง fork ที่ agent boundary**. 2010-2020 = APM (Application Performance Monitoring) — Datadog, New Relic, Dynatrace ครอง. 2020-2025 = Observability 2.0 — OpenTelemetry standard + high-cardinality data + eBPF (Groundcover, Chronosphere, Honeycomb). 2026 = **Agent Observability** — new dimension ที่ trace ไม่ใช่แค่ HTTP request แต่ **agent reasoning chain + tool call sequence + LLM API call + cost per outcome + eval result**. Groundcover's $100M round + growth metric = **first proof point of investable market**. คาดว่า Datadog + New Relic + Splunk จะ **acquire หรือ deep partner** กับ pure-play agent observability startup ภายใน 12-18 เดือน (Splunk เพิ่ง acquire Onum ที่ทำ AI data pipeline เดือน มิ.ย.)

**BYOC = category-defining architectural choice**. ปัจจุบัน Datadog ทำ enterprise observability ที่ **ส่ง log + metric + trace ทั้งหมด ไป Datadog SaaS** — จุด friction ใหญ่กับ regulated industry ที่มี **data residency requirement** + **cost predictability requirement** ที่ Datadog volume pricing ทำให้ predict ยาก. Groundcover BYOC = **data ไม่ออก customer premises, cost = flat platform license**. เทียบง่าย ๆ กับ Snowflake vs. on-prem data warehouse ยุค 2018 — โมเดล cloud-hosted ชนะแล้ว 8 ปี แต่ observability กำลังกลับมา **hybrid/BYOC ที่ regulated enterprise พร้อมจ่าย 20-30% premium**. Signal: Databricks, Confluent, MongoDB ที่มี BYOC option = growing 40%+; Datadog ที่ 100% SaaS = growing 20% (Q2 earnings 2 สัปดาห์ก่อน)

**Agent observability = pre-condition ของ FinOps ยุค agent**. Cost story ที่เพิ่ง break ใน 30 ก.ค. — OpenAI cut Luna 80% (Enabridge cover เรื่อง #2 วันนี้) — ทำให้ **per-turn cost swing 80%** จาก decision routing ระดับ prompt. Enterprise ที่ไม่มี agent-level cost attribution จะ **overpay 3-5x** ในไตรมาสข้างหน้า. Groundcover's positioning: **cost per outcome, not cost per token** — trace ไปถึงระดับ "agent user action A ใช้ $0.42, action B ใช้ $12.30, action B fail 70%" → business decision layer มี data พอ optimize. Datadog LLM Observability ปัจจุบันยังไม่มี "cost per outcome" layer

## มุม AI Agent Platform

**สำหรับ builders (agent framework/runtime):** ต้อง **treat observability instrumentation เป็น first-class primitive ตั้งแต่ v1** — ไม่ใช่ optional module ที่ทิ้งให้ ops team integrate เอง. OpenTelemetry semantic convention สำหรับ agent workload — "gen_ai.request", "gen_ai.tool_call", "gen_ai.agent_decision" — เข้า draft ใน OTel 1.30 (Q3 release). Framework ที่ **export OTel-compliant span พร้อม agent semantic** = drop-in กับ Groundcover + Datadog + New Relic. ที่ยัง proprietary logging = obsolete ภายใน Q4. Anthropic Claude Code SDK, GitHub Copilot SDK, LangGraph — ทุกตัวจะ ship OTel emission ก่อน re:Invent (พ.ย.)

**สำหรับ users/business:** ก่อน scale agent deployment ไป production, **audit ว่า observability layer พร้อมหรือยัง**. คำถามต่อ platform vendor: (1) *"trace ระดับ agent turn + tool call + LLM call ได้ไหม?"*, (2) *"cost attribution ต่อ agent-user-action มีไหม?"*, (3) *"ตอนเกิด incident, replay + counterfactual (ถ้า agent เลือก tool อื่น จะเกิดอะไร) ได้ไหม?"*, (4) *"BYOC option มีไหม? data ต้องอยู่ใน VPC ของเรา?"* — สำหรับ regulated industry (bank, insurance ที่ Enabridge บทวิเคราะห์ frequent), คำตอบ "ไม่มี BYOC" = ไม่ผ่าน CISO. Thai SET50 ที่ deploy agent ใน production workflow (SCB, KBank digital, Bualuang Securities, PTT digital) จะเห็น RFP round Q4 ที่ **agent observability = mandatory section** — Datadog + Groundcover + New Relic จะแข่งกัน

**สำหรับ ecosystem:** **สาม startup category ที่ VC จะ deploy ใน 6 เดือนข้างหน้า** ตาม Groundcover thesis: (1) **agent evaluation platform** (Braintrust, LangSmith, Arize AI Phoenix — measure agent output quality over time), (2) **agent cost governance** (still greenfield — startup ที่ให้ CFO/FinOps team budget cap + alert + optimization ระดับ agent-user-action), (3) **agent forensics** (Chronosphere, Groundcover ที่ขยายจาก observability → post-incident investigation). Loser: legacy APM ที่ยัง treat AI workload เป็น "just another HTTP call" — enterprise buyer จะ replace ภายใน 18-24 เดือน

## Sources
- [groundcover Raises $100 Million Series C To Scale AI-Era Observability Platform — Pulse 2.0](https://pulse2.com/groundcover-raises-100-million-series-c-to-scale-ai-era-observability-platform/)
- [groundcover Raises $100 Million Series C to Scale AI-Era Observability Platform — Unite.AI](https://www.unite.ai/groundcover-raises-100-million-series-c-to-scale-ai-era-observability-platform/)
- [Groundcover raises $100M as observability pivots from monitoring to AI infrastructure — Network World](https://www.networkworld.com/article/4204009/groundcover-raises-100m-as-observability-pivots-from-monitoring-to-ai-infrastructure.html)
- [groundcover Raises $100 Million Series C to Create the Observability Platform Built for the AI Era — BusinessWire](https://www.businesswire.com/news/home/20260729686071/en/groundcover-Raises-$100-Million-Series-C-to-Create-the-Observability-Platform-Built-for-the-AI-Era)
- [groundcover raises $100M to build observability for the AI era — TNW](https://thenextweb.com/news/groundcover-raises-100m-to-build-observability-for-the-ai-era)
- [groundcover Raises $100M Series C to Create the Observability Platform Built for the AI Era — BigDATAwire](https://www.hpcwire.com/bigdatawire/this-just-in/groundcover-raises-100m-series-c-to-create-the-observability-platform-built-for-the-ai-era/)

---

## Audio script
วันนี้เช้าที่ Enabridge อยากให้ทุกคนเห็น sub category ใหม่ที่เกิดในตลาด agent stack. วันที่ 29 กรกฎาคม Groundcover ปิด Series C 100 ล้านเหรียญ นำโดย One Peak ร่วม Morgan Stanley Expansion Capital. Total funding แตะ 160 ล้าน. Metrics ARR โต 3 เท่าปีที่แล้ว workforce 2 เท่า customer 250 รายตั้งแต่ early stage ถึง Fortune 5 ปิด multiple 7 figure contract.

Groundcover position ตัวเองเป็น observability สำหรับ engineers กับ agents. Architecture ที่ทำให้แตกต่างจาก Datadog New Relic Grafana คือ BYOC. Bring your own cloud. Deploy sensor กับ collector inside customer premises ไม่ส่ง data ออก. เหตุผลที่ regulated enterprise สนใจ compliance กับ data residency กับ cost predictability. Datadog volume pricing กำลังทำลาย FinOps team ใน AI era.

Signal ที่อยากให้เห็น. Observability category กำลัง fork ที่ agent boundary. 2010-2020 คือ APM ยุค Datadog New Relic Dynatrace. 2020-2025 คือ Observability 2.0 ยุค OpenTelemetry กับ eBPF. 2026 คือ Agent Observability ยุคใหม่ ที่ trace ไม่ใช่แค่ HTTP request แต่ agent reasoning chain กับ tool call กับ LLM API call กับ cost per outcome. Groundcover 100 ล้านคือ first proof point of investable market.

BYOC คือ category defining choice. Datadog ส่ง log ทั้งหมดไป SaaS. friction ใหญ่กับ regulated industry ที่มี data residency กับ cost predictability. Groundcover BYOC data ไม่ออก customer premises cost flat platform license. เทียบกับ Snowflake vs on prem data warehouse ยุค 2018 แต่ observability กำลังกลับมา hybrid ที่ regulated enterprise พร้อมจ่าย premium.

สำหรับ enterprise ไทย SET50. ก่อน scale agent deployment ต้อง audit observability layer พร้อมหรือยัง. คำถามต่อ platform vendor 4 ข้อ. Trace ระดับ agent turn กับ tool call กับ LLM call ได้ไหม. Cost attribution ต่อ agent user action มีไหม. Replay กับ counterfactual ได้ไหม. BYOC option มีไหม data ต้องอยู่ใน VPC ของเรา. Regulated industry คำตอบไม่มี BYOC = ไม่ผ่าน CISO.

สำหรับ builders. Treat observability instrumentation เป็น first class primitive ตั้งแต่ v1. OpenTelemetry semantic convention สำหรับ agent workload เข้า draft ใน OTel 1.30 Q3 release. Framework ที่ export OTel compliant span พร้อม agent semantic drop in กับ Groundcover Datadog New Relic. Framework ที่ยัง proprietary logging obsolete ภายใน Q4. คุยกันวันหน้าครับ.
