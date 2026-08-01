---
date: 2026-08-02
slug: dynatrace-autonomous-sre-cloud-agent-builder-ga
topic: openbridge-trend
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial isometric composition of a night-time NOC (network operations
  center) with three glowing panels. Left panel labeled "AUTONOMOUS SRE" shows
  an agent silhouette merging two alert bubbles into one investigation.
  Middle panel labeled "CLOUD SRE" shows three cloud icons (AWS, Azure, GCP)
  connected by a single glowing loop with the tag "ONE AUDIT TRAIL". Right
  panel labeled "AGENT BUILDER" shows a no-code drag interface with the badge
  "NO CODE · AUG GA". Above them a headline stack: "FROM INSIGHT TO ACTION"
  and a subline "AWS / AZURE / GCP INTEGRATED". Deep Dynatrace-lime + charcoal
  palette, chiaroscuro editorial style, 1:1 aspect, no real human faces, text
  must render sharply at 200px thumbnail.
image: images/26-08-02-0610-03-dynatrace-autonomous-sre-cloud-agent-builder-ga.png
---

# Dynatrace เปิด Autonomous SRE + Cloud SRE + Agent Builder — observability vendor แรกที่ take corrective action ข้าม AWS/Azure/GCP ด้วย audit trail เดียว

## TL;DR
- **27 ก.ค.** — Dynatrace เปิดของใหม่สาม product ใน Dynatrace Intelligence platform: **Autonomous SRE Agent** (merge investigation autonomously), **Cloud SRE Agent** (coordinate remediation ข้าม AWS/Azure/GCP), **Agent Builder** (no-code custom agent)
- **Cloud SRE Agent + Enhanced Dynatrace Assist = GA today** สำหรับ DPS customer. **Autonomous SRE + Agent Builder = GA สิงหาคม**
- ประกาศพร้อม tagline "moving from insight to action" — observability vendor แรกที่ยอมให้ agent take action ข้าม cloud provider แล้วเขียน **single auditable record**
- Signal: **observability layer กำลัง collapse เป็น autonomous ops platform** — Dynatrace, Datadog, New Relic กำลัง reset สงคราม; winner = ใครที่ enterprise trust ให้ agent take action ก่อน

## เกิดอะไรขึ้น

วันจันทร์ที่ 27 กรกฎาคม (วันเดียวกับที่ Microsoft ปล่อย Project Perception) Dynatrace ประกาศ "autonomous operations for enterprise AI" — ประกอบด้วย 3 agent product ที่ collapse observability + incident response + remediation เข้าเป็น workflow เดียว. **Autonomous SRE Agent** ทำงานเมื่อ Davis AI detect problem ใหม่ — agent ตัดสินใจว่าเป็นส่วนหนึ่งของ investigation เก่าหรือใหม่, ถ้าใช่ merge เข้า auto พร้อม enrich context (ไม่มี on-call รับ 3 page แยกสำหรับ symptom ของ root cause เดียวกันอีก). **Cloud SRE Agent** เป็นตัว coordinator — integrate กับ agent AI ของ AWS (Amazon Q Ops), Azure (Copilot for Cloud), GCP (Gemini Cloud Assist) แล้ว centralize findings เข้ามาที่ Dynatrace ให้เป็น **single auditable record** สำหรับ SRE + compliance team

**Agent Builder** เป็น no-code interface ที่ให้ enterprise สร้าง custom agent ต่อ workflow ตัวเอง — เช่น "ถ้า checkout latency > p99 SLA เกิน 5 นาที, run this playbook, notify Slack ทีม payments, ถ้า confidence > 0.85 auto rollback deployment". Enhanced Dynatrace Assist — natural-language investigation ที่รวม ChatOps style + agentic tool use — เปิดให้ SaaS DPS customer ทั้งหมด (Dynatrace Platform Subscription tier)

Rick McConnell (Dynatrace CEO) พูดกับ New Stack ว่าจุด hardest ที่ agentic ops ต้อง solve = **trust boundary ระหว่าง detect กับ act**. "Everybody wants AIOps that take action — nobody wants an agent that rollback production without audit trail". Approach ของ Dynatrace = ทุก action ต้องผ่าน **explicit approval level** (Level 1 = auto, Level 2 = human-in-loop 30s window, Level 3 = require explicit approval) กำหนดต่อ playbook. Cloud SRE Agent + Enhanced Dynatrace Assist = **GA today** for DPS SaaS customer. Autonomous SRE Agent + Agent Builder = **GA August 2026** (คาดกลางเดือน). ราคายังไม่เปิด แต่ analyst หลายคนคาดจะเป็น per-agent + per-action pricing tier บน DPS existing subscription

## ทำไมสำคัญ

**Observability vendor แรกที่ยอมให้ agent take corrective action ข้าม cloud provider — เดิมพันหลัง**. Datadog เปิด Bits AI Autonomous SRE เมื่อพฤษภาคม แต่ยังจำกัดที่ "recommend action + generate runbook draft" — ไม่ take action เอง. Splunk (Cisco) มี AIOps Agent ที่รัน remediation แต่ scope แค่ Cisco stack เอง. New Relic เพิ่งประกาศ NRQL Agent แต่ยัง preview เท่านั้น. Dynatrace **cross-cloud + agent take action + audit trail** = configuration ที่ enterprise ยอมรับได้ก่อนเพราะมี explicit approval level ที่ CISO map เข้ากับ change management policy ที่มีอยู่แล้ว

**"Insight to action" tagline = observability industry มี identity crisis กำลังจบ**. เดิม observability = dashboard + alert; วันนี้ = **autonomous ops platform**. เหตุผลใต้ก้อนนี้: **agent workload ใน production ทำให้ MTTD/MTTR เดิมล้าสมัย** — agent ทำ decision millisecond, ทำ tool call พันครั้งต่อ minute, ถ้า human ต้อง triage ทุก anomaly = fail. Enterprise ที่ deploy agent จริง (Klarna, JPMorgan, Morgan Stanley, Novartis) กำลังบอก vendor observability ว่า **"เราต้องการ agent ที่ triage agent ให้เรา"**. Dynatrace ตอบก่อน; Datadog + New Relic จะตามใน 4-6 สัปดาห์

**Cross-cloud audit trail = enterprise buying criterion #1 สำหรับ 2027**. Cloud SRE Agent มีสิ่งที่ hyperscaler-native ไม่มี — **vendor-neutral consolidation ของ action history**. Amazon Q Ops รู้ AWS, Azure Copilot รู้ Azure, Gemini Cloud Assist รู้ GCP. แต่ enterprise 60% run **multi-cloud production** — ต้องมี layer ที่ตอบ auditor ได้ว่า "6 agent จาก 3 cloud provider ตัดสินใจ rollback deployment เพราะเหตุผลนี้" ใน single timeline. นี่คือ **defensible moat ของ observability vendor** ที่ hyperscaler จะไม่ challenge (เพราะเป็น neutrality play — AWS จะไม่ audit Azure agent). Dynatrace + Datadog + Grafana Cloud = **new SIEM สำหรับ agent era**

## มุม AI Agent Platform

**สำหรับ builders:** ถ้ากำลังสร้าง agent framework ที่ deploy production — **Agent Builder จาก Dynatrace + Portkey + Databricks Mosaic Gateway = stack ที่ enterprise buyer พร้อมซื้อ**. โอกาส: build agent action / tool ที่ **register ผ่าน Dynatrace Agent Builder registry** (คาดเปิด marketplace ปลายปี, ตามที่ Rick McConnell ใบ้). ถ้ากำลังสร้าง observability framework ต่อ agent เอง — ต้อง think ว่า **agent trace + audit + approval level = OpenTelemetry extension** ที่กำลังจะ standardize (SIG-Agent working group เพิ่งเริ่ม). ทำ MCP server exposing action-with-approval ให้ Dynatrace Agent Builder consume ได้เลย

**สำหรับ users/business:** SRE + platform team ต้อง **audit ตอนนี้ว่า MTTD/MTTR ใน agent workload มีตัวเลขจริงไหม** — ส่วนใหญ่ไม่มี. Enterprise ที่ยัง run Datadog/Splunk เฉย ๆ — เตรียม **RFP amendment ให้เพิ่ม "agent action + cross-cloud audit trail" เป็น requirement** ใน renewal cycle 2027. Cost model จะเปลี่ยนจาก **per-host + per-log-GB → per-agent + per-action + per-audit-record** ใน 12-18 เดือน — CFO ต้องเข้าใจ. Thai bank / telco ที่ยัง run Nagios + Zabbix + Grafana OSS = **falling 3 generation behind** — agent-native observability คือ table stakes สำหรับ Basel III / TB110 audit ต่อไป

**สำหรับ ecosystem:** losers ชัด — **legacy AIOps startup** (BigPanda, Moogsoft ตอนนี้ IBM, PagerDuty AIOps) ที่ยังอยู่ recommend-only + no cross-cloud action. Winners: (1) Dynatrace (ก้าวก่อน 4-6 สัปดาห์), (2) Datadog (จะ ship autonomous action ในสิงหาคม-กันยายน), (3) **MCP + OpenTelemetry SIG-Agent** ที่กำลัง standardize agent trace format, (4) hyperscaler ที่ยอม expose action API ให้ 3rd-party (AWS Q Ops แล้ว, Azure Copilot for Cloud beta). Enabridge angle: ถ้า pitch Thai bank/insurance เรื่อง agent deployment — Dynatrace autonomous ops + cross-cloud audit + Level 1/2/3 approval = reference architecture ที่ CISO + Head of SRE ยอมรับได้; ต่างจาก 6 เดือนที่แล้วที่ต้อง handwave เรื่อง "AI Ops"

## Sources
- [Dynatrace Brings Autonomous Operations to Enterprise AI, Moving from Insight to Action — Dynatrace Press Release](https://www.dynatrace.com/news/press-release/autonomous-operations-enterprise-ai/)
- [Dynatrace's new agents can reveal the single hardest part of AI operations — The New Stack](https://thenewstack.io/dynatrace-autonomous-sre-agents/)
- [Dynatrace Introduces Domain Specific Agents — Dynatrace Press Release](https://www.dynatrace.com/news/press-release/dynatrace-introduces-domain-specific-agents/)
- [Dynatrace Adds New Autonomous Agents and No-Code Tools — Channel Post MEA](https://channelpostmea.com/2026/07/29/dynatrace-adds-new-autonomous-agents-and-no-code-tools-to-intelligence-platform/)
- [Dynatrace Intelligence automates incident triage and remediation with AI agents — Help Net Security](https://www.helpnetsecurity.com/2026/07/27/dynatrace-intelligence/)
- [Dynatrace Brings Autonomous Operations to Enterprise AI — Yahoo Finance / BigDATAwire](https://www.hpcwire.com/bigdatawire/this-just-in/dynatrace-brings-autonomous-operations-to-enterprise-ai-moving-from-insight-to-action/)

---

## Audio script
27 กรกฎาคม Dynatrace เปิดของใหม่สามตัวใน Dynatrace Intelligence platform. Autonomous SRE Agent, Cloud SRE Agent, และ Agent Builder. Cloud SRE ออนไลน์ทันที, สองตัวที่เหลือ GA สิงหาคม.

ที่ทำให้ package นี้สำคัญ — Dynatrace เป็น observability vendor แรกที่ยอมให้ agent take corrective action ข้าม AWS, Azure, GCP แล้วเขียน single audit trail เดียว. Datadog ยังแค่ recommend, ไม่ take action. Splunk take action ได้แต่ scope แค่ Cisco stack. Dynatrace มี approval level ตั้งไว้ 3 ระดับ — Level 1 auto, Level 2 human-in-loop 30 วินาที, Level 3 explicit approval — เพื่อให้ CISO map เข้า change management policy ที่มีอยู่แล้ว.

Signal ที่สำคัญ — observability industry กำลัง collapse เป็น autonomous ops platform. เหตุผล — agent ทำ tool call พันครั้งต่อ minute, ถ้ารอ human triage ทุก anomaly = fail. Enterprise ที่ deploy agent จริงอย่าง Klarna, JPMorgan, Morgan Stanley กำลังบอก vendor ว่า "เราต้องการ agent ที่ triage agent ให้เรา". Dynatrace ตอบก่อน. Datadog กับ New Relic จะตามใน 4 ถึง 6 สัปดาห์. สำหรับ Thai bank ที่ยัง run Nagios กับ Zabbix — falling 3 generation behind. Agent-native observability คือ table stakes สำหรับ Basel III audit ต่อไป.
