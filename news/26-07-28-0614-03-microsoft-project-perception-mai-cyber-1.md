---
date: 2026-07-28
slug: microsoft-project-perception-mai-cyber-1
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: |
  Three squads of small robotic agents on a dark grid — one squad labeled
  "RED" hunting through code, one labeled "BLUE" investigating a glowing
  breach, one labeled "GREEN" patching walls; a large scoreboard overhead
  reads "96% CyberGym / 50% COST". Editorial isometric illustration,
  crimson-cobalt-emerald palette on charcoal background, bold labels,
  numbers rendered large enough to read at 200px. 1:1 aspect, no real human
  faces.
image: images/26-07-28-0614-03-microsoft-project-perception-mai-cyber-1.png
---

# Microsoft ปล่อย Project Perception + MAI-Cyber-1-Flash — agent สาม squad ล่า-สืบ-ปะเข้าแทน SOC team, ตี CyberGym 96% ราคาครึ่งหนึ่งของ Anthropic

## TL;DR
- Microsoft launch **Project Perception** (agentic security platform) + **MAI-Cyber-1-Flash** (first in-house cybersecurity LLM) ที่ event เล็ก ๆ ใน SF เมื่อวันจันทร์ 27 ก.ค.
- **MAI-Cyber-1-Flash** ทำ **96% บน CyberGym** — สูงกว่า Anthropic Mythos **12 คะแนน**, top score ของ leaderboard ที่มี code-search flavor สูง
- **Project Perception** = 3 squad ของ agent ที่ทำงานพร้อมกัน: **red** (ล่าช่องโหว่), **blue** (สืบ + triage risk), **green** (ปิด + hardening)
- **Cost claim:** MAI-Cyber-1-Flash + MDASH stack "50% cost ของ leading model" — pricing pressure ตรงต่อ Anthropic + OpenAI ที่ครองตลาด security automation ตอนนี้
- Public preview **3 ส.ค.** — Microsoft ตั้ง benchmark price ก่อนคู่แข่งจะขยับ

## เกิดอะไรขึ้น

Microsoft เลือกวันจันทร์ (27 ก.ค.) เปิดตัวสองผลิตภัณฑ์ที่เชื่อมกัน — **MAI-Cyber-1-Flash** (LLM specialized cybersecurity ตัวแรกของบริษัท) และ **Project Perception** (agentic security platform) — ที่ event ไม่ใหญ่ใน SF ที่นักข่าว TechCrunch, VentureBeat, Axios, GeekWire, The Register เข้าร่วม. Timing ที่เลือกน่าสนใจ: 1 สัปดาห์ก่อน public preview วันที่ 3 ส.ค., และ 24 ชั่วโมงก่อน MCP 2026-07-28 spec ล็อก (brief #01)

**MAI-Cyber-1-Flash** built บน MAI-Thinking-1 base ที่ Microsoft ปล่อยเมื่อ Q2, fine-tune ด้วย security data ที่ Microsoft สะสมมาจาก Defender, Sentinel, GitHub Advanced Security. Number ที่ leadership ใช้ pitch คือ CyberGym benchmark — leaderboard ของ security-focused code understanding — ที่ MAI-Cyber-1-Flash ทำ **96%** เทียบกับ Anthropic Mythos (top competitor ก่อนหน้า) ที่ **84%**. Delta 12 คะแนน บน benchmark ที่ saturate ยาก = signal จริง

แต่ product hero คือ **Project Perception**. Architecture: agent 3 squad ทำงาน coordinated แบบ human SOC team

- **Red team agents** — ล่า vulnerability + attack path ต่อเนื่อง (offensive posture)
- **Blue team agents** — รับ alert, ทำ triage + investigation
- **Green team agents** — ปิด vulnerability, patch, harden config

3 squad นี้แชร์ shared memory ผ่าน **MDASH** (Microsoft Distributed Agent Security Hub) — internal orchestration layer ที่ทำหน้าที่ agent-to-agent protocol + policy enforcement. Pitch เชิง cost: MAI-Cyber-1-Flash + MDASH combo ให้ "world-class security performance ที่ **50% cost** ของ leading model และ Microsoft's previous best offering"

Public preview เปิด **3 ส.ค.** — 1 สัปดาห์จากวันนี้. GA target ยังไม่ประกาศ แต่ Microsoft signal ว่าจะพร้อมก่อน Ignite (พ.ย. 2026)

## ทำไมสำคัญ

Microsoft ทำ 3 อย่างพร้อมกันด้วย launch นี้: (1) **claim ตำแหน่ง benchmark leader** ใน security-specific LLM — พื้นที่ที่ Anthropic + OpenAI ยังไม่ verticalize; (2) **ตัด price 50%** ในตลาดที่ SOC operation ใช้เงิน 6-7 หลักต่อเดือน — pressure ที่ ไม่มีใคร match ได้ทันในไตรมาสนี้; (3) **package agent orchestration เป็น product** ไม่ใช่แค่ SDK — ทำให้ CISO ซื้อได้เลยแทนที่จะต้อง build

Pattern ที่เห็นชัด: **hyperscaler เริ่ม vertical fine-tune LLM ของตัวเอง** ในโดเมนที่ทำเงินแล้ว. Microsoft = security (มี Defender + Sentinel เป็น distribution). AWS = coding (มี CodeWhisperer). Google = ads / search. ระบบนี้เคยเกิดกับ AWS ปี 2015-2017 ตอนย้ายจาก generic compute → managed service ต่อ vertical — และผู้ชนะยุคนั้นคือคนที่ควบคุม distribution + data

**Signal ต่อ Anthropic + OpenAI:** ทั้งคู่จะเจอปัญหา distribution ใน enterprise security. Anthropic Mythos ที่ตี 84% บน CyberGym เป็น general-purpose model ที่ผู้ใช้ต้อง wrap เอง — Microsoft ขายเป็น turnkey ที่มี Defender integration พร้อมใช้. CISO ที่อยู่ Azure/M365 ecosystem จะเลือก path ที่มี support + SLA + audit log integrate อยู่แล้ว. Anthropic ต้องออก enterprise partnership กับ SIEM vendor (Splunk, Elastic, IBM QRadar) ภายใน 90 วัน ไม่งั้นเสียตลาดนี้

จุดที่ under-appreciated คือ **red team agent as product**. Legal + ethical ยังกลาง ๆ — "agent ที่ล่า vulnerability ต่อเนื่อง" คือสิ่งที่ pen-test team คน ทำ + จ่าย $500-2000/hr. ถ้า Microsoft ทำให้ได้ที่ marginal cost ใกล้ 0 = อาชีพ offensive security consulting โดน commoditize ในระดับที่ Bloomberg terminal commoditize research junior ปี 2000. Regulator (SEC, EU AI Act, NIST) ยังไม่มี framework สำหรับ agent-driven red team — เป็น regulatory gray zone ที่ Microsoft เข้าเป็นเจ้าแรก

## มุม AI Agent Platform

**Builders:** Architecture pattern "red / blue / green squad" คือ template ที่ agent orchestrator ต้องเรียนรู้. คนที่ build agent สำหรับ vertical อื่น (finance audit, legal review, medical diagnosis) จะ steal pattern นี้ภายในสัปดาห์ — separation of concern ตาม role + shared memory ผ่าน orchestration hub. ใครที่ยัง build agent เดี่ยว monolith ต้อง re-architect. MDASH คือ blueprint ของ agent-to-agent protocol ระดับ enterprise — จับตาว่า Microsoft จะ open ต่อ industry หรือ keep proprietary

**Users / business:** สำหรับ CISO Thai — ถ้าใช้ Azure/M365 อยู่ = evaluation ของ Project Perception ต้องอยู่ใน Q3 roadmap; MAI-Cyber-1-Flash pricing 50% ต่ำกว่า incumbent = business case ผ่านเอง. สำหรับ SOC operation ที่ยัง in-house หรือ MSSP tier 2 — เตรียม defend ต่อ questions จาก CFO ใน 60 วัน ("ถ้า Microsoft ทำได้ 50% cheaper ทำไมเรายังจ้าง MSSP")

**Ecosystem:** สำหรับ Enabridge — **อย่า compete บน generic agent platform**. Verticalize ทันที: agent สำหรับ Thai regulatory compliance (Bank of Thailand, SEC), agent สำหรับ Thai fraud pattern (call center scam, PromptPay abuse), agent สำหรับ Thai financial statement audit. Microsoft ไม่ speak Thai regulator; นั่นคือ moat. Pattern architecture (red / blue / green) copy ได้ แต่ domain expertise + Thai data ต้อง build local

## Sources
- [Microsoft launches its first cybersecurity model, plus a new agentic cybersecurity system — TechCrunch](https://techcrunch.com/2026/07/27/microsoft-launches-its-first-cyber-model-and-a-new-agentic-cybersecurity-system/)
- [Microsoft launches AI cybersecurity model, agentic defense platform to cut enterprise security costs — VentureBeat](https://venturebeat.com/security/microsoft-launches-ai-cybersecurity-model-agentic-defense-platform-to-cut-enterprise-security-costs)
- [Microsoft Project Perception launches AI agents, specialized model for cybersecurity — Axios](https://www.axios.com/2026/07/27/microsoft-unveils-new-cyber-model-agentic-security-tools-to-fight-hackers)
- [Microsoft escalates the AI security race with 'Project Perception' — GeekWire](https://www.geekwire.com/2026/microsoft-escalates-the-ai-cybersecurity-race-with-project-perception-and-a-new-in-house-model/)
- [Microsoft's solution to AI security: more AI and more acronyms — The Register](https://www.theregister.com/security/2026/07/27/microsofts-solution-to-ai-security-more-ai-and-more-acronyms/5279140)

---

## Audio script
Microsoft เปิดตัว 2 ผลิตภัณฑ์ที่เชื่อมกันเมื่อวันจันทร์ที่ 27 กรกฎาคม. MAI-Cyber-1-Flash เป็น LLM specialized cybersecurity ตัวแรกของบริษัท และ Project Perception เป็น agentic security platform. ที่ event ไม่ใหญ่ใน SF.

MAI-Cyber-1-Flash ทำ 96 เปอร์เซ็นต์บน CyberGym benchmark สูงกว่า Anthropic Mythos 12 คะแนน. Fine-tune ด้วย security data ที่ Microsoft สะสมมาจาก Defender, Sentinel, GitHub Advanced Security. เป็น top score ของ leaderboard ที่ saturate ยาก.

Project Perception หัวใจคือ agent 3 squad ทำงาน coordinated เหมือน human SOC team. Red team agent ล่า vulnerability ต่อเนื่อง. Blue team agent รับ alert ทำ triage. Green team agent ปิด vulnerability harden config. 3 squad แชร์ memory ผ่าน MDASH ซึ่งเป็น internal orchestration layer.

Pitch เชิง cost คือ Combo นี้ให้ world-class security performance ที่ 50 เปอร์เซ็นต์ของ leading model. Public preview วันที่ 3 สิงหาคม. GA ก่อน Ignite เดือนพฤศจิกายน.

Signal ต่อ Anthropic กับ OpenAI. ทั้งคู่จะเจอปัญหา distribution ใน enterprise security. Mythos ที่ 84 เปอร์เซ็นต์เป็น general-purpose model ที่ผู้ใช้ต้อง wrap เอง. Microsoft ขายเป็น turnkey มี Defender integration พร้อม. CISO ที่อยู่ Azure ecosystem จะเลือก path ที่มี SLA + audit log integrate อยู่แล้ว.

จุดที่ under-appreciated คือ red team agent as product. Pen-test manual จ่าย 500 ถึง 2000 ดอลลาร์ต่อชั่วโมง. ถ้า Microsoft ทำได้ที่ marginal cost ใกล้ 0. อาชีพ offensive security consulting โดน commoditize ในระดับที่ Bloomberg terminal commoditize research junior ปี 2000.

สำหรับ Enabridge. อย่า compete บน generic agent platform. Verticalize ทันที. Agent สำหรับ Thai regulatory Bank of Thailand SEC. Agent สำหรับ Thai fraud pattern call center scam PromptPay abuse. Microsoft ไม่ speak Thai regulator. นั่นคือ moat.
