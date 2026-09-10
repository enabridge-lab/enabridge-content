---
date: 2026-09-10
slug: air-security-50m-agent-firewall-sequoia-greenoaks
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial isometric illustration of a giant translucent firewall grid
  labeled "AIR" glowing blue and white; behind it a swarm of small robot
  agents queue in a line, each holding a signed permit stamped "SKILL
  VERIFIED"; a lone red robot with a suspicious paper is bounced back by a
  brick wall. Three headline chips float on the side: "$50M SEED",
  "SEQUOIA + GREENOAKS", "6 MONTHS OLD". Steel-blue and coral accent
  palette, cinematic rim lighting, bold high-contrast typography for
  200px thumbnail, 1:1 aspect, no real human faces.
image: images/26-09-10-0610-03-air-security-50m-agent-firewall-sequoia-greenoaks.png
---

# AIR Security ออกจาก stealth ด้วย $50M — สอง ex-military Israeli founder + Sequoia + Greenoaks + Wiz + Cognition insider ทั้งกลุ่ม เดิมพันว่า "firewall สำหรับ agent" จะเป็น category ที่ใหญ่พอ ๆ กับ Palo Alto ใน 5 ปี

## TL;DR
- **AIR Security** ออกจาก stealth วันที่ 1 ก.ย. 2026 ด้วย **$50M seed** — round แรก $10M นำโดย **Sequoia**, round สอง $40M นำโดย **Greenoaks**, ปิดห่างกันแค่ไม่กี่สัปดาห์
- **Product**: **inline firewall for AI agents** — vet skills/MCP servers/tools ที่ agent ใช้ก่อน allow, block malicious action, และ enforce policy ใน supply chain ของ agent
- **Team**: founder Yair Saban + Niv Hoffman เจอกันใน military เกือบ 10 ปีที่แล้ว, บริษัทก่อตั้ง **ก.พ. 2026** (6 เดือน!), 40 คนใน Israel, กำลังตั้ง AI behavior research lab
- **Angel roster**: Zach Frankel (President, Cognition), Yinon Costica (Co-founder, Wiz), Anne Neuberger, Ofir Ehrlich (Eon), Varun Anand (Clay) — cross-pollination ระหว่าง cyber, agent, และ enterprise infra
- Signal: agent security กลายเป็น **investable category ในสายตา top-tier fund** — เทียบ pattern ที่ Wiz, Snyk, Vercel ปูทางไว้

## เกิดอะไรขึ้น

**AIR Security** ประกาศออกจาก stealth วันที่ 1 กันยายน 2026 ด้วย seed round ที่แปลกกว่าปกติ — **$50 ล้าน แบ่งเป็น 2 tranche ปิดห่างกันไม่กี่สัปดาห์**. tranche แรก $10M นำโดย **Sequoia Capital**, tranche สอง $40M นำโดย **Greenoaks**. Swish Ventures และ Netz ร่วมด้วย. บริษัท **ก่อตั้งเดือน ก.พ. 2026** — จาก founding ถึง $50M ใช้เวลา 6 เดือน, pace ที่เทียบได้กับตอน Wiz raise Series A รอบแรก

Founder คู่: **Yair Saban** (CEO) และ **Niv Hoffman** — ทั้งสองมี background จาก Israeli military cyber unit, เจอกันเกือบ 10 ปีที่แล้ว. Company ตอนนี้มี **40 คนใน Israel** และกำลัง build **AI behavior research lab** ที่ focus ที่ **การเข้าใจว่า agent ตัดสินใจอย่างไร ในสถานการณ์ที่ผู้โจมตี inject prompt / manipulate tool response / poison memory**. ต่างจาก security lab ทั่วไปที่ focus ที่ code exploitation, lab นี้ focus ที่ **behavioral security** — agent จะ "หลง" ยังไง, และจะออกแบบ guardrail ยังไง

**Product**: inline firewall + supply-chain vetter. Position คือ **"agent ทำอะไรได้บ้าง" ต้อง gate ผ่าน policy engine ก่อน, และ "agent จะใช้ tool / skill / MCP server อะไร" ต้อง pre-vet supply chain ก่อน install**. เหมือน npm audit + Wiz + Cloudflare WAF รวมกันแต่ specific ให้ agent. ตัวอย่าง use case ที่ AIR pitch:
- Enterprise deploy coding agent (Devin, Claude Code, Codex) → AIR vet MCP server ที่ agent จะเรียก ก่อน commit ให้ agent runtime
- Enterprise deploy customer-service agent → AIR intercept HTTP call ที่ agent ทำ, check ว่าไม่ leak PII, ไม่ยิงไป endpoint ที่ blacklist
- Enterprise deploy multi-agent workflow → AIR log + audit ทุก inter-agent handoff เพื่อ forensics ตอน incident

**Angel investor list** อ่านเหมือน insider dinner party: **Zach Frankel (President, Cognition — บริษัทที่ทำ Devin)**, **Yinon Costica (Co-founder, Wiz — บริษัท cloud security ที่ Google ซื้อ $32B)**, **Anne Neuberger (อดีต Deputy National Security Advisor for Cyber, White House)**, **Ofir Ehrlich (Co-founder, Eon)**, **Varun Anand (Co-founder, Clay)**, และผู้ก่อตั้ง cyber startup อีกหลายราย. คน 3 คนแรกให้ signal ที่ต่างกัน: Frankel signal ว่า **agent developer ต้องการเครื่องมือนี้ใน stack ของตัวเอง**, Costica signal ว่า **security architecture pattern ของ cloud security 15 ปีจะย้ายไป agent security**, Neuberger signal ว่า **US government + regulator เริ่มคิดถึง agent security เป็น national issue**

## ทำไมสำคัญ

**Round นี้ยืนยัน thesis ที่ Sequoia / Greenoaks / Andreessen พูดกันในสัปดาห์ที่ผ่านมา: agent security เป็น category ใหม่ที่ underserved และตลาดพร้อม pay**. เทียบขนาด — Palo Alto Networks (network firewall) $110B market cap, CrowdStrike (endpoint security) $85B, Wiz (cloud security) sold $32B. **agent firewall category** ตอนนี้ยังไม่มี incumbent, และ ownership window เปิดตอนนี้ก่อนที่ hyperscaler จะ bundle เข้า runtime ของตัวเอง. AIR + คู่แข่งอย่าง **Prompt Security, HiddenLayer, CalypsoAI, Robust Intelligence** กำลัง sprint เพื่อ claim category name

Pattern ที่ต้องจับตา: **agent security ที่ ship จริง จะเป็น 3 layer** — (1) **model-level** (ป้องกัน prompt injection, jailbreak) ที่ Anthropic / OpenAI ทำใน model training; (2) **runtime-level** (memory isolation, sandbox VM, capability system) ที่ AgentCore, Muse Secure VM, Cloudflare Workers ทำ; (3) **inline firewall + supply-chain layer** ที่ AIR pitch อยู่. Layer 3 คือ **checkpoint ระหว่าง agent กับ external world** — เทียบ WAF ที่นั่งระหว่าง web app กับ internet. ยังไม่มี dominant vendor, และ enterprise ที่ deploy agent จริงจังกำลังจะต้องซื้อ

Deep signal: **timing ที่ Sequoia และ Greenoaks ยอม lead 2 tranche ต่อกันในบริษัทอายุ 6 เดือน**. VC top-tier ปกติจะ compete lead round เดียว. การยอม co-invest tranche-based (แทนที่จะรวมเป็น Series A $50M เดียว) แปลว่า **valuation ปรับขึ้นระหว่าง 2 tranche** — บ่งชี้ว่า traction / pipeline growth ใน 30-60 วันตัวเลขน่าตื่นเต้นพอที่ Greenoaks ยอมจ่าย mark-up ทันที. เป็น signal ว่า enterprise pipeline สำหรับ agent security **ไม่ได้ทฤษฎี** — มี buyer signing เดือนละหลายเจ้าแล้ว

## มุม AI Agent Platform

**Builders**: ถ้าคุณสร้าง agent framework, เตรียม **integration point สำหรับ external firewall/policy engine**. LangChain ควรเปิด `callback_manager` ที่ third-party WAF hook ได้, CrewAI ควรมี `Guardrail(url=...)` primitive ที่ delegate policy ไปยัง AIR / competitor. คนที่ **ไม่ ship security integration** จะเสีย enterprise deal ที่ CISO ต้องเห็น firewall report. สำหรับ MCP server developer, **submit ไป AIR + คู่แข่ง supply-chain registry ก่อน list บน Bazaar / Anthropic MCP registry** — enterprise agent จะ block install ถ้า MCP ไม่ผ่าน supply-chain vet เร็ว ๆ นี้

**Users / Business**: ถ้าคุณเป็น enterprise ที่ deploy agent (production หรือ pilot), **agent firewall กำลังกลายเป็น line item ใน security budget ปี 2027**. ก่อน RFP procurement ควรมี requirement 3 อย่าง: (1) **inline mediation** ที่ block agent call ก่อน execute (ไม่ใช่ post-hoc log); (2) **supply-chain vet** ที่ approve MCP server / tool / skill ก่อน agent มี access; (3) **behavioral anomaly detection** ที่ catch prompt injection แบบ novel. ราคา category นี้จะเริ่มจาก $50-200K/year สำหรับ mid-market, $500K-2M สำหรับ Fortune 500 — เป็น budget ที่ต้องเริ่ม negotiate ก่อน CISO approve agent production deployment

**Ecosystem**: ผู้ชนะ: (1) **security startup ที่ ship agent-specific product เร็ว** — AIR, Prompt Security, HiddenLayer, CalypsoAI, Robust Intelligence; (2) **security consultant** ที่จะขาย "agent security assessment" service ให้ enterprise ก่อน production — Deloitte, Mandiant, Coalfire; (3) **compliance auditor** ที่จะออก certification ใหม่ (SOC 2 for Agents, ISO for Agent Ops). ผู้แพ้ระยะสั้น: **security vendor เก่าที่ยัง reposition ช้า** — เช่น network security ที่ยัง frame ตัวเองเป็น firewall for traffic, ไม่ใช่ firewall for agent decision. ผู้แพ้ระยะยาว: **hyperscaler ที่ยอมให้ third party ครอง firewall layer** — AWS, Azure, GCP น่าจะ acquire หรือ build parallel product ใน 12-18 เดือน. สำหรับ Thailand: **cybersecurity consulting firm** ที่เตรียม agent security offering ก่อนคู่แข่ง สามารถ position ตัวเองเป็น "trusted advisor for agent deployment" ให้ enterprise ที่กำลัง evaluate — window นี้เปิดตอนนี้ ก่อน 12 เดือนข้างหน้าจะแน่นด้วย MSP incumbent

## Sources
- [TechCrunch — AIR raises $50M to help companies vet the skills and add-ons AI agents use](https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/)
- [SecurityWeek — AI Agent Firewall Startup AIR Security Emerges From Stealth With $50 Million](https://www.securityweek.com/ai-agent-firewall-startup-air-security-emerges-from-stealth-with-50-million/)
- [Calcalistech — Six-month-old AIR Security raises $50 million to build a firewall for AI agents](https://www.calcalistech.com/ctechnews/article/r13apdnugg)
- [Dealroom — Air raises $50M seed to build a firewall for AI agents](https://dealroom.co/news/148163-air-raises-50m-seed-to-build-a-firewall-for-ai-agents/)
- [The Globe and Mail (AccessWire) — AIR Emerges from Stealth With $50M to Build a Firewall for Agents](https://www.theglobeandmail.com/investing/markets/markets-news/ACCESS%20Newswire/4380070/air-emerges-from-stealth-with-50m-to-build-a-firewall-for-agents/)

---

## Audio script
AIR Security ประกาศออกจาก stealth วันที่ 1 กันยายน. seed round ที่แปลกกว่าปกติ. 50 ล้านเหรียญ. แบ่งเป็น 2 tranche ปิดห่างกันไม่กี่สัปดาห์. tranche แรก 10 ล้าน นำโดย Sequoia Capital. tranche สอง 40 ล้าน นำโดย Greenoaks. บริษัทก่อตั้งเดือนกุมภาพันธ์ 2026. จาก founding ถึง 50 ล้านใช้เวลา 6 เดือน. pace ที่เทียบได้กับตอน Wiz raise Series A รอบแรก.

Founder คู่. Yair Saban CEO และ Niv Hoffman. ทั้งสองมี background จาก Israeli military cyber unit. เจอกันเกือบ 10 ปีที่แล้ว. company มี 40 คนใน Israel. กำลัง build AI behavior research lab ที่ focus ที่การเข้าใจว่า agent ตัดสินใจอย่างไร เมื่อผู้โจมตี inject prompt manipulate tool response poison memory.

Product. inline firewall บวก supply chain vetter. position คือ agent ทำอะไรได้บ้าง ต้อง gate ผ่าน policy engine ก่อน. และ agent จะใช้ tool skill MCP server อะไร ต้อง pre vet supply chain ก่อน install. เหมือน npm audit บวก Wiz บวก Cloudflare WAF รวมกัน แต่ specific ให้ agent.

Angel investor list อ่านเหมือน insider dinner party. Zach Frankel President Cognition บริษัทที่ทำ Devin. Yinon Costica Co founder Wiz บริษัท cloud security ที่ Google ซื้อ 32 พันล้าน. Anne Neuberger อดีต Deputy National Security Advisor for Cyber ที่ White House. Ofir Ehrlich Eon. Varun Anand Clay. Frankel signal ว่า agent developer ต้องการเครื่องมือนี้ใน stack. Costica signal ว่า architecture pattern ของ cloud security 15 ปีจะย้ายไป agent security. Neuberger signal ว่า US government regulator เริ่มคิดถึง agent security เป็น national issue.

Signal ใหญ่. Round นี้ยืนยัน thesis ที่ VC top tier พูดกัน. agent security เป็น category ใหม่ที่ underserved และตลาดพร้อม pay. เทียบขนาด. Palo Alto Networks 110 พันล้าน. CrowdStrike 85 พันล้าน. Wiz sold 32 พันล้าน. agent firewall category ยังไม่มี incumbent. ownership window เปิดตอนนี้ก่อน hyperscaler จะ bundle เข้า runtime.

Pattern. agent security ที่ ship จริงจะเป็น 3 layer. model level ป้องกัน prompt injection jailbreak ที่ Anthropic OpenAI ทำใน training. runtime level memory isolation sandbox VM ที่ AgentCore Muse Secure VM ทำ. inline firewall supply chain layer ที่ AIR pitch. Layer 3 คือ checkpoint ระหว่าง agent กับ external world. เทียบ WAF ที่นั่งระหว่าง web app กับ internet.

Timing ที่ Sequoia และ Greenoaks ยอม lead 2 tranche ต่อกัน ใน 30 ถึง 60 วัน แปลว่า traction pipeline growth น่าตื่นเต้นพอที่ Greenoaks ยอมจ่าย mark up ทันที. enterprise pipeline สำหรับ agent security ไม่ได้ทฤษฎี. มี buyer signing เดือนละหลายเจ้าแล้ว.

สำหรับ builder เตรียม integration point สำหรับ external firewall policy engine. LangChain ควรเปิด callback manager. CrewAI ควรมี Guardrail primitive. คนที่ไม่ ship security integration จะเสีย enterprise deal.

สำหรับ enterprise agent firewall กำลังกลายเป็น line item ใน security budget ปี 2027. ราคาเริ่ม 50 ถึง 200K ต่อปีสำหรับ mid market. 500K ถึง 2M สำหรับ Fortune 500. ต้องเริ่ม negotiate ก่อน CISO approve production.

ผู้ชนะ. security startup ที่ ship agent specific เร็ว. security consultant. compliance auditor ที่ออก certification ใหม่. ผู้แพ้. security vendor เก่าที่ reposition ช้า. hyperscaler ที่ยอมให้ third party ครอง firewall layer อาจ acquire ใน 12 ถึง 18 เดือน. Thailand cybersecurity consulting ที่เตรียม agent security offering ก่อนคู่แข่ง position ตัวเองเป็น trusted advisor.
