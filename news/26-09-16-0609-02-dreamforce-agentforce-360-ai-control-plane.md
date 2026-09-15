---
date: 2026-09-15
slug: dreamforce-agentforce-360-ai-control-plane
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  A cinematic wide shot of the Dreamforce main stage bathed in electric blue
  light, a giant screen behind the podium showing a control panel labeled
  "AGENTFORCE 360 — AI CONTROL PLANE" with seven pill buttons in a row
  reading "CASEY", "PAIGE", "CARTER", "HUNTER", "MARSHALL", "PIPER", "FIN".
  Below the screen a smaller banner reads "TRUST BOUNDARY + CLAUDEFORCE".
  In front of the stage stand silhouetted attendees with badges reading
  "SEP 15 2026". Editorial poster style, deep navy background with cyan and
  amber highlights, 1:1 aspect, no real human faces.
image: images/26-09-16-0609-02-dreamforce-agentforce-360-ai-control-plane.png
---

# Dreamforce Day 1 — Salesforce เปิด Agentforce 360 + AI Control Plane และ ยึดเกม enterprise agent ด้วย 7 ตัวจริง

## TL;DR
- Dreamforce 2026 keynote 15 ก.ย. — Salesforce เปิด **Agentforce 360** พร้อม **AI Control Plane** สำหรับ identity, policy enforcement, และ lifecycle management ของ agent
- 7 named agent (Casey, Paige, Carter, Hunter, Marshall, Piper, Fin) 6 ตัว GA แล้ว — Hunter (outbound sales) อยู่ pilot ใช้ long-horizon runtime ที่พันธะกิจต่อเนื่องได้เป็นสัปดาห์/เดือน, GA พฤศจิกา
- Marc Benioff + Dario Amodei ขึ้น keynote คู่กัน; **Claudeforce** (Claude ใน Salesforce Trust Boundary ผ่าน Bedrock) — beta เปิดกันยา, ยิงชุด plugin 37 sales skills

## เกิดอะไรขึ้น

Dreamforce 2026 ที่ San Francisco เปิด keynote วันจันทร์ 15 กันยายน โดย Marc Benioff ไม่ได้ปล่อย product ใหม่แบบเดียว — ปล่อย **สถาปัตยกรรมทั้งชุด**. Agentforce 360 คือ platform สำหรับ build autonomous agent ที่รันงานใน Customer 360, ทุกตัวรันบน Atlas Reasoning Engine พร้อม guardrails ที่ลูกค้าตั้งได้เอง. เหนือขึ้นไปคือ **AI Control Plane** — ชั้น identity, policy enforcement, lifecycle management สำหรับ agent (คล้าย IAM แต่สำหรับ agent + tool, ไม่ใช่ human user).

Salesforce เปิดตัว 7 named agent เมื่อ 11 กันยายน แต่วันจันทร์นี้เอามาโชว์เต็ม — Casey (service), Paige (HR/IT support), Carter (commerce), Hunter (outbound sales), Marshall (supply chain), Piper (inbound pipeline), Fin (customer experience). 6 ตัว GA แล้ว, Hunter อยู่ pilot เพราะเป็นตัวแรกที่ใช้ **long-horizon runtime** — พันธะกิจต่อเนื่องได้เป็นสัปดาห์/เดือน แทนที่จะจบใน single chat session; GA พฤศจิกายน. เดิมพันของ Salesforce คือ agent จะไม่ใช่ chatbot แต่เป็น "coworker" ที่มีชื่อ, มีตำแหน่ง, มี memory ข้ามเดือน.

Highlight ของ keynote คือช่วงที่ **Dario Amodei ขึ้นเวทีร่วมกับ Benioff**. สองคนย้ำเรื่อง Claudeforce — partnership ที่ประกาศตั้งแต่ 26 สิงหา — ให้ Claude รันภายใน Salesforce Trust Boundary ผ่าน Amazon Bedrock (สำหรับ regulated industry ที่ห้าม data ออกนอก perimeter), บวก "Salesforce in Claude" plugin ที่แพ็ค 37 sales skill (pipeline update, revenue context reasoning, governed action). Beta เปิดกันยา, พร้อมชุด skill เพิ่มปลายปี.

## ทำไมสำคัญ

Salesforce กำลังพยายามยึด layer ที่ยังไม่มีใครยึดชัดเจน — **agent control plane**. ทุกคนพูดเรื่อง agent framework (LangGraph, CrewAI, AutoGen), agent runtime (Bedrock AgentCore, OpenAI Agents), agent protocol (MCP, ACP, A2A). แต่ **agent identity + policy + lifecycle** ยังไม่มีใครทำเป็น productized layer สำหรับ enterprise. ถ้า Salesforce ทำได้ในความเป็น de facto ก่อนคนอื่น พวกเขาจะขยับจาก CRM vendor เป็น **agent OS ของ enterprise** — และมี lock-in ที่ยากกว่าเดิมมาก.

Signal อีกชั้นคือ Hunter's long-horizon runtime — pattern ที่ทุกคนพยายามทำ (OpenAI's Agents API + Codex harness, Anthropic's Claude memory + connectors) แต่ Salesforce มีข้อได้เปรียบว่ามี data + workflow context ครบใน CRM อยู่แล้ว. Agent ที่ทำงาน weeks/months โดยไม่หลงทาง ต้องรู้ว่าใครเป็นลูกค้า, ใครติดต่อล่าสุด, ปิด deal ระดับไหน — ทั้งหมดนี้อยู่ใน Salesforce ทำเอง. ถ้า Hunter GA พฤศจิกาแล้วปิด deal ได้จริง จะกลายเป็น proof point ที่ startup vertical AI ต้องรีบตอบ.

การมี Amodei ขึ้นเวทีเป็น signal ต่อ enterprise buyer ว่า Salesforce ไม่ได้ยึด single model — Anthropic (ผ่าน Bedrock), OpenAI, และ Gemini ต่อได้หมด. คนที่จะเสียคือ startup agent orchestration ที่ขาย "agent-with-your-data" — ตอนนี้ Salesforce ทำเอง.

## มุม AI Agent Platform

**Builders** ที่กำลังสร้าง agent runtime / orchestration — ดู pattern ของ AI Control Plane: agent identity, policy enforcement, lifecycle management เป็น layer ที่แยกจาก reasoning และ tool call. ใครที่ยังไม่คิดเรื่องนี้ยังอยู่ prototype phase; enterprise คำถามแรกคือ "agent นี้ทำอะไรได้บ้าง ใครอนุมัติ ถ้าทำเสียหายใครรับผิด". **Users / business** โดยเฉพาะทีม sales/service ไทยที่ใช้ Salesforce อยู่แล้ว — 6 named agent GA แล้วต่อได้กับ Customer 360 ที่มีอยู่. คำถามที่ต้องเตรียมคือ "workflow ไหนของทีมเราให้ agent รันได้เต็ม end-to-end" และ "policy บังคับตรงไหน (approval threshold, data access, audit)". **Ecosystem** — startup vertical CRM agent (Rippling AI, Attio, Regie.ai) โดนกดดันหนัก เพราะ Salesforce ยึด control plane + named agent + long-horizon runtime พร้อมกัน. Anthropic ได้ distribution enterprise มหาศาลผ่าน Claudeforce; OpenAI + Google ต้องเร่งหา partner CRM ระดับเดียวกัน (HubSpot? Zendesk? Microsoft Dynamics?).

สำหรับตลาดไทย — บริษัทที่ใช้ Salesforce Enterprise/Unlimited ควรเรียก Salesforce AE มาคุยเรื่อง Agentforce 360 pricing + Trust Boundary + Claudeforce ให้ครบก่อนต่อสัญญาปีหน้า. ถ้ายังใช้ HubSpot/Zoho — คำถามคือ vendor ของคุณจะเปิด control plane ที่เทียบเคียงได้เมื่อไหร่.

## Sources
- [Salesforce Debuts Job-Ready Agentforce Agents and Long-Horizon Runtime](https://www.unite.ai/salesforce-debuts-job-ready-agentforce-agents-and-long-horizon-runtime/)
- [Dreamforce 2026 day one live: Marc Benioff keynote and more](https://www.techradar.com/pro/live/dreamforce-2026-live-were-in-san-francisco-for-salesforces-big-ai-event)
- [Salesforce and Anthropic Announce Claudeforce](https://www.salesforce.com/news/press-releases/2026/08/26/salesforce-and-anthropic-announce-claudeforce/)

---

## Audio script
วันนี้เป็นวันแรกของ Dreamforce 2026 ที่ San Francisco และ Salesforce ปล่อยของหนักมากครับ. Marc Benioff เปิดงานด้วย Agentforce 360 พร้อม AI Control Plane ซึ่งเป็นชั้น identity policy enforcement และ lifecycle management สำหรับ agent — คล้าย IAM แต่สำหรับ agent และ tool ไม่ใช่ user คน. ตัว 7 named agent Casey Paige Carter Hunter Marshall Piper Fin — 6 ตัว GA แล้ว. Hunter คือ outbound sales agent ที่อยู่ pilot เพราะเป็นตัวแรกที่ใช้ long-horizon runtime พันธะกิจต่อเนื่องได้เป็นสัปดาห์เดือน แทนที่จะจบใน single chat session — GA พฤศจิกา. Highlight คือช่วงที่ Dario Amodei ขึ้นเวทีคู่กับ Benioff ย้ำเรื่อง Claudeforce partnership ที่ประกาศตั้งแต่สิงหา ให้ Claude รันภายใน Salesforce Trust Boundary ผ่าน Amazon Bedrock สำหรับ regulated industry ที่ห้าม data ออกนอก perimeter. บวก Salesforce in Claude plugin ที่แพ็ค 37 sales skill — beta เปิดกันยา. Signal ที่ต้องอ่านคือ Salesforce กำลังยึด layer ที่ยังไม่มีใครยึดชัดเจน — agent control plane. ทุกคนพูดเรื่อง agent framework agent runtime agent protocol แต่ agent identity policy lifecycle ยังไม่มีใครทำเป็น productized layer สำหรับ enterprise. ถ้า Salesforce ทำได้ในความเป็น de facto ก่อนคนอื่น พวกเขาจะขยับจาก CRM vendor เป็น agent OS ของ enterprise. สำหรับ builder ที่กำลังทำ agent runtime — AI Control Plane เป็น layer ที่แยกจาก reasoning และ tool call ต้องออกแบบตั้งแต่วันแรก. สำหรับทีมไทยที่ใช้ Salesforce Enterprise อยู่แล้ว ควรเรียก AE มาคุยเรื่อง Agentforce 360 pricing และ Trust Boundary ก่อนต่อสัญญาปีหน้าครับ
