---
date: 2026-08-18
slug: zenity-125m-agent-security
topic: openbridge-trend
reading_time_min: 6
sources: 5
image_prompt: |
  Editorial isometric illustration of a colossal glowing vault door labeled
  "AGENT RUNTIME" hanging above a fractal grid of one billion tiny robot
  silhouettes; three floating stacked numerals dominate the frame:
  "$125M SERIES C", "1B AGENTS", "FORTUNE 50". A single laser tripwire
  cuts across an agent mid-action, halting it before it reaches a red API
  endpoint. Muted indigo, steel, and amber palette; dramatic chiaroscuro
  lighting; crisp editorial typography readable at 200px thumbnail;
  1:1 aspect; no real human faces (silhouettes only), no logos.
image: images/26-08-18-0611-01-zenity-125m-agent-security.png
---

# Zenity ปิด $125M Series C — SoftBank/Hitachi/LG แทงหุ้น "Agent SecOps" ก่อนยุค 1 พันล้าน agent

## TL;DR
- **Zenity** ปิด **$125M Series C** (Norwest นำ) วันที่ 3 ส.ค. — pitch: "secure the era of 1 billion AI agents"; ลิสต์ผู้ลงทุนใหม่คือ **SoftBank Vision Fund 2, Hitachi Ventures, LG Technology Ventures, Qumra Capital** + existing Vertex/DTCP/Intel Capital/Third Point
- Platform ทำ **runtime governance** สำหรับ agent — เห็น intended action ของ agent real time, allow/modify/block ก่อน execute; ต่างจาก AI security รุ่นเดิมที่ focus แค่ model + prompt filter
- Customer มี majority เป็น **Fortune 500/Global 2000** และมี Fortune 50 หลายรายที่ใช้มาตั้งแต่ต้น — เงินก้อนนี้ไปที่ global expansion + product ต่อจาก "prompt security" ไปเป็น "action security"
- Signal: **Agent SecOps** กลายเป็น category แยกจาก AppSec, LLM security, DLP — VC ให้ multiple ระดับ growth-stage cyber (Wiz-tier)

## เกิดอะไรขึ้น

วันที่ 3 ส.ค. Zenity — บริษัท Israeli founded ปี 2021 ที่เริ่มจาก "no-code / low-code security" — announce Series C $125M ที่ Norwest Venture Partners นำ. รอบนี้ดึง strategic backer ระดับ **SoftBank Vision Fund 2, Hitachi Ventures, LG Technology Ventures, และ Qumra Capital** เข้ามาใหม่ พร้อม existing investor รอบก่อน (Vertex, Third Point, DTCP, Intel Capital). Total raised ของบริษัทตอนนี้ทะลุ **$180M+** และ valuation ยังไม่ disclose แต่ Fortune รายงานว่า multiple ใกล้เคียง Wiz Series C ตอน late 2022

Positioning statement ที่ CEO Ben Kliger เขียนใน announcement คือ **"secure the era of 1 billion AI agents"** — reference ตรงถึง prediction ของ Salesforce/Microsoft ปี 2024 ว่า enterprise จะมี agent มากกว่า human worker 1000x ภายใน 2028. Zenity vault ตัวเองในตำแหน่งของ "control plane" ที่ enterprise ต้องมี ก่อน CISO จะยอม approve production rollout

จุดที่ทำให้ Zenity ต่างจาก Robust Intelligence, Prompt Security, HiddenLayer คือ **runtime action governance** — ไม่ใช่ filter prompt หรือ scan model artifact, แต่ตัด hook เข้าไปที่ layer ก่อน tool call จริง. เวลา agent จะ execute action (เช่น "delete row จาก database", "send email ถึง external", "POST ไป API ที่ไม่รู้จัก") Zenity intercept ก่อน แล้ววิเคราะห์ intended action vs policy — allow, modify, block, หรือ log. Behavioral baseline ต่อ agent ต่อ workflow build ขึ้นจาก session ที่ผ่านมา ทำให้ anomaly detection แม่นกว่า rule-based DLP

Customer ที่เปิดเผยตอนนี้เต็มไปด้วย Fortune 50 — Zenity บอกว่า "majority" ของ customer คือ Fortune 500 หรือ Global 2000. ที่น่าสังเกตคือใน announcement press release พูดถึง **Copilot Studio, ServiceNow, Salesforce Agentforce, Google Agentspace, Anthropic Claude Enterprise** ว่าเป็น platform ที่ Zenity มี integration ready — คุมทุก major agent platform ที่ enterprise deploy จริงในปี 2026

## ทำไมสำคัญ

รอบ funding นี้คือ **first big signal** ว่า "Agent SecOps" กลายเป็น category ที่ VC ยอมให้ multiple แบบ tier 1 cyber. เทียบกับปี 2023 ที่ AI security คือ "prompt injection + red team + model watermark" — Zenity ผลักไป layer ลึกกว่า: **runtime action authorization** ซึ่ง map ตรงกับ SASE/ZTNA pattern ของ Zscaler ยุค 2018-2020

Pattern ที่เห็นชัด: **CISO buyer เริ่มเรียกร้อง "same guarantees ที่ human ได้"** — RBAC, audit log, SIEM export, DLP hook — แต่กับ agent workflow ที่ move faster กว่า human 100-1000x. tools ที่ตอบโจทย์ (Zenity, CalypsoAI, Lakera) ตอนนี้ค่อนข้าง niche; แต่ curve การซื้อในปี 2026-2027 น่าจะ mimic curve ของ CASB ปี 2015-2017 — จาก "อยากได้แต่งบไม่ผ่าน" ไปเป็น "compliance บังคับ"

Cross-reference: อาทิตย์เดียวกัน **Atlassian Rovo prompt injection** ยัง unpatched มาแล้ว 2 เดือน (PromptArmor disclose 23 พ.ค., ยังไม่มี fix ณ 5 ส.ค.) และ **Anthropic ยังไม่ยอมแก้ MCP design flaw ที่ protocol level**. ทั้งสอง pattern ตอกย้ำว่า **vendor-side fix ไม่ทัน** — enterprise ต้อง third-party control plane เพื่อ ownership + speed of response. นั่นแปลว่า Zenity ไม่ได้ขายแค่ "nice to have"; มันขาย "insurance policy สำหรับ risk ที่ vendor ไม่รับ"

จุด weak คือ **incumbents ที่ยังไม่ตอบ**: Microsoft Purview, Cisco AI Defense, Palo Alto Prisma AIRS ทั้งหมดยัง early ในเรื่อง runtime agent action. ถ้า Microsoft ตัดสินใจ bundle "Purview Agent Guardrails" ฟรีกับ Copilot Enterprise ใน Q4 = Zenity ต้องเร่ง moat ให้ deep ทันที ก่อนกลายเป็น feature ของ platform

## มุม AI Agent Platform

**Builders / framework maker:** ทุก framework (LangChain, LlamaIndex, DSPy, Bee) ต้องเริ่ม design "policy hook" ที่ inject-able ระหว่าง reasoning และ tool call — ไม่ใช่แค่ callback สำหรับ observability, แต่เป็น **synchronous authorization decision**. คนที่ ship SDK รอบใหม่โดยไม่มี hook นี้ = ถูก mark เป็น "unusable for enterprise" ภายใน 12 เดือน

**Users / business deployer:** ถ้าตอนนี้ deploy agent เข้า production โดยไม่มี runtime governance = risk profile เดียวกับ deploy web app โดยไม่มี WAF ในปี 2010. อย่ารอ audit finding — ตั้ง budget line item "Agent SecOps" ใน 2027 budget cycle ทันที; Zenity, CalypsoAI, Lakera ควรเข้า evaluation shortlist. สำหรับ Thai enterprise / SET100: cost start ราว $30-50/agent/month, break-even เมื่อ agent จำนวน >20 ตัว

**Ecosystem:** SoftBank Vision Fund 2 + Hitachi Ventures + LG Technology Ventures เข้าพร้อมกัน = **APAC distribution play**. คาดว่า Zenity จะเปิด Tokyo/Seoul/Singapore office ภายใน Q1 2027; Thai market จะเข้าผ่าน Singapore hub. Local partner opportunity สำหรับ integrator ที่มี Fortune 500 Thai unit (SCB Tech X, KBTG, PTT Digital) — pitch ให้ Zenity รอบ H1 2027

## Sources
- [Zenity Raises $125 Million to Secure the Era of 1 Billion AI Agents (BusinessWire)](https://www.businesswire.com/news/home/20260803963850/en/Zenity-Raises-$125-Million-to-Secure-the-Era-of-1-Billion-AI-Agents)
- [SoftBank, Hitachi, LG back Zenity's $125 million Norwest-led round to police AI agents (Fortune)](https://fortune.com/2026/08/03/softbank-hitachi-lg-back-zenitys-125-million-round-to-police-ai-agents/)
- [Zenity Raises $125 Million Series C to Strengthen AI Agent Security and Governance (Cybersecurity News)](https://cybersecuritynews.com/zenity-ai-agent-security/)
- [Zenity Closes $125M to Secure the Era of 1 Billion AI Agents (The AI Insider)](https://theaiinsider.tech/2026/08/11/zenity-closes-125m-to-secure-the-era-of-1-billion-ai-agents/)
- [Zenity Raises $125M Series C to Expand AI Agent Security Platform (AIwire/HPCwire)](https://www.hpcwire.com/aiwire/2026/08/04/zenity-raises-125m-series-c-to-expand-ai-agent-security-platform/)

---

## Audio script
เช้าวันอังคารที่ 18 สิงหาคม เรื่องแรกที่น่าจับตา — Zenity บริษัทอิสราเอลด้าน AI agent security เพิ่งปิด Series C ที่ 125 ล้านดอลลาร์ นำโดย Norwest มี SoftBank Vision Fund 2, Hitachi Ventures, LG Technology Ventures เข้ามาใหม่. Zenity วาง positioning ตัวเองว่า "secure the era of 1 billion AI agents" อ้างตัวเลขที่ Salesforce กับ Microsoft เคยพูดว่า enterprise จะมี agent มากกว่าคน 1000 เท่าภายในปี 2028. ที่น่าสนใจคือ Zenity ไม่ได้แค่กรอง prompt เหมือน AI security ยุคก่อน แต่มัน intercept ที่ layer ระหว่าง reasoning กับ tool call — ก่อน agent จะ execute action จริง ระบบจะดูก่อนว่า allow, modify, block, หรือ log. customer ตอนนี้เต็มไปด้วย Fortune 500 กับ Fortune 50 หลายเจ้า. signal ใหญ่ที่สุดของข่าวนี้คือ Agent SecOps กลายเป็น category ใหม่ระดับ tier 1 cyber แล้ว — VC ยอมจ่าย multiple แบบ Wiz Series C ปี 2022. สำหรับทีมที่กำลัง deploy agent เข้า production ตอนนี้ ถ้ายังไม่มี runtime governance = risk profile เดียวกับ deploy web app โดยไม่มี WAF ในปี 2010. ตั้ง budget line item Agent SecOps ใน 2027 planning cycle ทันที.
