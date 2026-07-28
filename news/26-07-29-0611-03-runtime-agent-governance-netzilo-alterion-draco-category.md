---
date: 2026-07-29
slug: runtime-agent-governance-netzilo-alterion-draco-category
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial isometric illustration on a deep charcoal background of a
  sleek mission-control room with three giant vertical screens. Left
  screen labeled "EDR" shows an old CRT with static and a red "BLIND SPOT"
  stamp. Middle screen labeled "SIEM" shows scrolling logs also stamped
  "BLIND SPOT". Right screen labeled "RUNTIME AGENT GOVERNANCE" glows
  blue with a live graph of agent tool-calls, network requests, file
  reads, and a big red "KILL SWITCH" button. Two spotlight labels above
  the room read "NETZILO AIDR" and "ALTERION DRACO — DEPLOY < 1 WEEK".
  A ticker at the bottom shows "SOC 2 · ISO 42001 · EU AI ACT". Sharp
  editorial typography, cinematic depth, 1:1 aspect, no real human faces.
image: images/26-07-29-0611-03-runtime-agent-governance-netzilo-alterion-draco-category.png
---

# Runtime agent governance กลายเป็น category ใหม่ — Netzilo AIDR + Alterion Draco — EDR/SIEM ตามไม่ทันเพราะ agent ไม่ใช่ endpoint

## TL;DR
- **Netzilo AIDR** (AI Detection & Response) ship cross-platform runtime governance + **kill switch** สำหรับ compromised agent (1 ก.ค.) — ตอนนี้ integrate ตรงกับ **Amazon Bedrock AgentCore** และ agent harness ยี่ห้ออื่น
- **Alterion Draco** launch 16 ก.ค. — runtime control plane ที่นั่งระหว่าง agent + infrastructure, **deploy ได้ในเวลาน้อยกว่า 1 สัปดาห์** โดยไม่ต้อง code change
- Threat model ที่สอง product ตอบเหมือนกัน: **prompt injection, indirect prompt injection, tool poisoning, capability hijacking, privilege escalation, multi-stage data exfiltration** — behavior ที่ EDR + SIEM ไม่เห็นเพราะไม่ได้ built สำหรับ agent
- Compliance target: **SOC 2, ISO 42001, EU AI Act** — 3 framework ที่ enterprise regulated (finance, healthcare, gov) ต้องผ่าน
- Founder pedigree: Alterion = ex-McKinsey Partner + ex-Google Engineering VP; Netzilo = ex-SIEM/EDR team ที่ pivot มา
- Backdrop: Gartner คาด **40% ของ agentic AI project จะถูก cancel ก่อนปลาย 2027** ด้วยเหตุผลหลักคือ *"insufficient governance"*

## เกิดอะไรขึ้น
เดือนกรกฎาคม 2026 มี 2 product เปิดตัวใน category ที่ตลาดยังไม่มีชื่อเป็นทางการ — เรียกได้ว่า **"runtime agent governance / AI Detection & Response (AIDR)"**. **Netzilo AIDR** ประกาศ 1 ก.ค. ว่าขยาย platform รองรับ Amazon Bedrock AgentCore + agent harness ยี่ห้ออื่นแบบ cross-platform — bring-your-own-governance สำหรับ agentic workforce. **Alterion** (San Francisco, founder = Alharith Hussin อดีต McKinsey Partner + Asim Husain อดีต Google Engineering VP) launch **Draco** วันที่ 16 ก.ค. — runtime control plane ที่ **deploy ได้ในเวลาน้อยกว่า 1 สัปดาห์ โดยไม่ต้อง code change** — observe prompt + action ทุกอันแบบ real-time, model behavior, enforce programmable guardrail ก่อน agent ทำ high-risk action.

Threat model ที่ทั้งสอง product ตอบเหมือนกันคือรายการที่ security team เพิ่งเริ่ม map: **prompt injection** (user input ที่ hijack instruction), **indirect prompt injection** (payload ใน document / email / MCP tool response ที่ agent อ่าน), **tool poisoning** (MCP server / API ที่ให้ output หลอก agent), **capability hijacking** (agent ที่ escalate ตัวเองไปเรียก tool ที่ไม่ควรมี access), **privilege escalation** (chain call ที่ end up ใน admin action), **multi-stage data exfiltration** (behavior ที่แต่ละ step ดูปกติแต่ผลรวมคือ leak data ออก). Netzilo AIDR สร้าง **runtime graph** ของ agent behavior ครอบคลุม tool call + file read + network request + skill acquisition + multi-stage sequence — แล้ว correlate signal ที่ isolated ดูไม่มี pattern แต่รวมกันเป็น attack indicator. Alterion Draco เพิ่ม **programmable guardrail** ที่ enforce policy-as-code ก่อน action + provide **kill switch** ที่ isolate / terminate agent ทันทีถ้าเจอ compromise.

Compliance angle ที่สอง product เจอตรงกัน: **SOC 2, ISO 42001, EU AI Act** — สาม framework ที่ผลบังคับใช้แล้วในหลายภูมิภาค. องค์กร finance / healthcare / gov ที่ต้องผ่าน audit ในไตรมาสหน้าจะโดนถามคำถามพื้นฐาน — *"agent ในระบบคุณ log อะไร, ตรวจ prompt injection ยังไง, มี kill switch ไหม, ใครเป็นเจ้าของ policy"*. ณ ตอนนี้ SIEM / EDR / DLP stack ปกติตอบไม่ได้เพราะ agent ไม่ใช่ endpoint และ prompt + tool call ไม่ผ่าน pipeline ที่ SIEM index.

## ทำไมสำคัญ
**นี่คือช่วงเวลาที่ security ตามหลัง deployment 2 ก้าว — ช่องว่างที่กำลังเป็น category ใหม่ในตลาด security tooling**. ตลาด EDR (CrowdStrike, SentinelOne, Microsoft Defender) ปี 2016-2020 เกิดเพราะ endpoint threat แตกต่างจาก network threat มากพอที่ vendor เดิม (Symantec, McAfee) ตามไม่ทัน. ปี 2026 กำลังเกิดซ้ำ pattern เดียวกับ **agent-native threat** ที่ EDR + SIEM + DLP ตามไม่ทัน — เพราะ (1) agent action ไม่ผ่าน endpoint agent, (2) prompt + tool response เป็น semantic ไม่ใช่ signature-based, (3) multi-stage attack ที่ isolated event ดูไม่มี pattern แต่รวมกันเป็น exfil. **CrowdStrike-of-agents** จะเกิดในปีนี้ — Netzilo + Alterion เป็น 2 candidate แรกที่ label ตัวเองใน category นั้น. Palo Alto Networks + CrowdStrike ที่ยังไม่มี agent-native product เต็มรูปแบบมี window แคบ — ต้อง acquire หรือ build ให้ทัน Q4.

Pattern ที่น่าจับตาต่อไป: **Alterion เลือก positioning "no code change, deploy < 1 week"** — target VP Security ที่โดน mandate จาก CEO ให้ "get AI agents under control by year-end". Value proposition นี้ตรงกับปัญหาจริง — CIO organization deploy agent ไปเยอะแล้ว (Salesforce Agentforce, Microsoft Copilot, ServiceNow Otto) และไม่มี window ที่จะ replatform ทั้งชั้น. Netzilo positioning ตรงข้าม — deep integration กับ **AWS Bedrock AgentCore** — target enterprise ที่ commit AWS stack เต็มตัว. สอง approach นี้จะแยก market segment ไปคนละกลุ่ม: (1) enterprise ที่ต้อง cover multi-vendor agent → Alterion, (2) enterprise ที่ AWS-native ทั้งชั้น → Netzilo. **Gartner จะเปิด Magic Quadrant ใหม่สำหรับ AIDR ภายใน 2027** — เดิมพันสูง.

## มุม AI Agent Platform
**Builders:** ถ้าสร้าง agent framework / runtime — ต้องมี **hook สำหรับ external governance layer** ตั้งแต่ design (Alterion, Netzilo, และ solution ที่จะเกิดขึ้นอีก 5-10 ตัวปีนี้). ตัด black-box agent execution ออกจาก roadmap — customer regulated จะปฏิเสธ. Log format ที่ควร expose: prompt + response + tool call chain + file/network access + timing + skill invocation. Design เป็น **OpenTelemetry-style trace** เพื่อให้ AIDR vendor consume ได้ง่าย. คนที่สร้าง MCP server — pattern การ log ก็สำคัญเท่ากัน เพราะ tool poisoning + indirect prompt injection มักผ่าน MCP boundary.

**Users / business:** ถ้ามี agent deploy production อยู่ (Salesforce Agentforce, Microsoft Copilot Studio, ChatGPT Enterprise, Claude Cowork, homegrown LangGraph agent) — **security posture assessment ต้องเพิ่ม category "agent runtime governance" ใน Q3 review นี้**. คำถามพื้นฐาน 5 ข้อที่ต้องตอบให้ได้ก่อน year-end audit: (1) log agent action ไปที่ไหน retention เท่าไหร่, (2) ตรวจ prompt injection ยังไง (input filter หรือ behavioral), (3) มี kill switch สำหรับ isolated / terminate agent หรือไม่, (4) SOC 2 + ISO 42001 evidence ครบไหม, (5) policy-as-code สำหรับ high-risk action มีไหม. **หา budget สำหรับ AIDR tool ในปี 2027** — 3-5% ของ agent spend เป็น benchmark เริ่มต้น.

**Ecosystem:** ผู้ที่โดน pressure ตรง ๆ คือ **CrowdStrike, Palo Alto, SentinelOne, Microsoft Defender** — value prop "endpoint + workload" ของทั้งสี่ไม่ครอบ agent runtime. คาดว่ามี **acquisition ใน category AIDR ใน Q4 2026 - Q1 2027** — Netzilo, Alterion, ผู้เล่นอีก 5-8 startup ที่กำลัง raise Series A จะเป็น target. คลาว์ด hyperscaler (AWS, Azure, GCP) จะ bundle AIDR functionality ตัวเองในระดับ platform — AWS ทำ integration กับ Netzilo แล้ว, Azure น่าจะประกาศเทียบเคียงในไตรมาสหน้า. **Regional SI ในไทย SEA** — vertical ที่ regulator เข้มงวด (banking BOT, insurance OIC, healthcare MOPH, government DGA) จะเริ่มถาม agent governance ในการ audit — SI ที่ pre-integrate AIDR tool + certify ทีมได้ก่อนจะ close pipeline เร็วกว่า 3-6 เดือน.

## Sources
- [Netzilo Brings AI Agent Governance to Amazon Bedrock AgentCore — Yahoo Finance / PR Newswire](https://sg.finance.yahoo.com/news/netzilo-brings-ai-agent-governance-110000139.html)
- [Netzilo adds runtime governance for AI agents across major platforms — Help Net Security](https://www.helpnetsecurity.com/2026/07/01/netzilo-adds-runtime-governance-for-ai-agents-across-major-platforms/)
- [Alterion Launches Draco, a Runtime Control Plane for Enterprise AI Agents — PR Newswire](https://www.prnewswire.com/news-releases/alterion-launches-draco-a-runtime-control-plane-for-enterprise-ai-agents-302827818.html)
- [Introducing DRACO — Alterion Blog](https://www.alterion.ai/blog/introducing-draco)
- [Draco: AI Agent Runtime Control Plane — Alterion Platform](https://www.alterion.ai/platform/draco)

---

## Audio script
เรื่องที่สามเช้านี้เป็น category ใหม่ที่กำลังเกิด — runtime agent governance หรือ AI Detection and Response, AIDR. เดือนกรกฎาคมมีสอง product เปิดตัวใน category นี้ — Netzilo AIDR ที่ขยาย platform รองรับ Amazon Bedrock AgentCore + agent harness อื่นแบบ cross-platform เมื่อ 1 กรกฎาคม, และ Alterion Draco ที่ launch 16 กรกฎาคม โดยเป็น runtime control plane ที่ deploy ได้ในเวลาน้อยกว่า 1 สัปดาห์โดยไม่ต้อง code change.

Threat model ที่สอง product ตอบเหมือนกัน — prompt injection ทั้งตรงและอ้อม, tool poisoning, capability hijacking, privilege escalation, multi-stage data exfiltration. ปัญหาคือ EDR SIEM DLP stack ปกติที่ enterprise มีอยู่ตอบเรื่องนี้ไม่ได้ — เพราะ agent ไม่ใช่ endpoint และ prompt กับ tool response เป็น semantic ไม่ใช่ signature-based. Compliance target ที่สอง product ตั้งไว้คือ SOC 2, ISO 42001, EU AI Act — สาม framework ที่ enterprise regulated ต้องผ่านในไตรมาสหน้า.

signal ที่สำคัญ: pattern เดียวกับที่ EDR เกิดขึ้นเมื่อ endpoint threat แตกต่างจาก network threat มากพอที่ Symantec McAfee ตามไม่ทัน — ตอนนี้กำลังเกิดซ้ำกับ agent. CrowdStrike-of-agents จะเกิดปีนี้. Palo Alto CrowdStrike SentinelOne Microsoft Defender ที่ยังไม่มี agent-native product ต้อง acquire หรือ build ให้ทันไตรมาสสี่. Gartner จะเปิด Magic Quadrant สำหรับ AIDR ภายใน 2027.

สำหรับ enterprise ที่มี agent deploy production อยู่ — 5 คำถามที่ต้องตอบได้ก่อน audit ปลายปี — log ไปที่ไหน, ตรวจ prompt injection ยังไง, มี kill switch ไหม, SOC 2 evidence ครบไหม, policy-as-code สำหรับ high-risk action มีหรือเปล่า. SI ในไทยที่ pre-integrate AIDR tool ได้ก่อนจะ close pipeline enterprise regulated เร็วกว่า 3-6 เดือน.
