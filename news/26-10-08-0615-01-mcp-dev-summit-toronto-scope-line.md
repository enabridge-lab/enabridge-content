---
date: 2026-10-07
slug: 26-10-08-0615-01-mcp-dev-summit-toronto-scope-line
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial hero: a vast transparent cathedral of protocol layers rising into
  a dawn sky, with a single central column labeled "MCP" glowing warm amber.
  Around it, four grey satellite pillars drift at a distance, each with a
  stenciled label: "IDENTITY", "OBSERVABILITY", "GOVERNANCE", "A2A". A thin
  rope line between the center column and the satellites is tagged "SCOPE
  LINE — HOLD". Four small lantern silhouettes stand on the amber column,
  each with a stamped flag: "ANTHROPIC", "AWS", "MICROSOFT", "OPENAI". A
  banner near the base reads "AAIF · TORONTO · OCT 5–6". Isometric editorial
  illustration, high-contrast cool navy and warm amber, 1:1 aspect, no real
  human faces.
image: images/26-10-08-0615-01-mcp-dev-summit-toronto-scope-line.png
---

# MCP Dev Summit Toronto — ผู้ดูแลโปรโตคอลลาก "scope line" กลางห้อง: identity, governance, observability ไม่ใช่ของเรา

## TL;DR
- **MCP Dev Summit Toronto (5–6 ต.ค. 2026)** จัดโดย Linux Foundation + Agentic AI Foundation (AAIF) เป็นงาน MCP ครั้งใหญ่ที่สุดที่เคยมี — 70 speakers, 6 tracks, 50+ sessions
- ผู้ดูแลหลักจาก **Anthropic, AWS, Microsoft, OpenAI** ยืนยันตรงกันว่า MCP จะ **ไม่** ขยายไป identity, observability, governance — "ของพวกนั้นเป็นงานของ layer อื่น"
- Signal: ecosystem ยอมรับว่า "the open agent stack" จะเป็น stack ของหลาย protocol — ไม่ใช่ one-protocol-to-rule-them-all

## เกิดอะไรขึ้น

วันจันทร์-อังคารที่ผ่านมา University of Toronto เป็นเจ้าภาพของสิ่งที่ **Forkast** เรียกว่า "the first major in-person gathering of the MCP community" — **MCP Dev Summit Toronto 2026** จัดภายใต้ Linux Foundation ร่วมกับ **Agentic AI Foundation (AAIF)** ซึ่งเพิ่งโผล่มาเป็น host ของโปรโตคอลเมื่อไม่กี่เดือนก่อน. 70 คนพูด, 6 tracks ไล่ตั้งแต่ agent architecture → infrastructure → security → production operations. ครั้งแรกที่คนทั้ง ecosystem — vendor, framework author, enterprise architect — มานั่งห้องเดียวกันแบบจับต้องได้

ประโยคสำคัญที่สุดของงานไม่ใช่ feature ใหม่ แต่คือสิ่งที่ **จะไม่** อยู่ใน MCP. ตามรายงานของ The Stack ("The protocol proliferation problem") ผู้ดูแลหลัก — ตัวแทนจาก **Anthropic** (เจ้าของ MCP เดิม), **AWS, Microsoft, OpenAI** — ยืนยันแนว scope ที่เคยลากไว้ตั้งแต่งาน MCP Dev Summit NA ที่ New York เมื่อ April: MCP เชื่อม AI application กับ data source / tool. จบ. "Observability, identity, governance — those problems belong to other projects and other standards." 

ผลคือ **ecosystem รอบๆ MCP** ขยายทันที. The Stack รายงานว่า **AGNTCY** — Linux Foundation project ที่ Cisco เริ่มไว้ — ตั้งตัวเองเป็น discovery / identity layer; **Agent2Agent (A2A) protocol** รับงาน inter-agent communication; **MCP Gateway pattern** กลายเป็นที่นั่งใหม่ของ token brokering, policy enforcement, audit log — ไม่ได้อยู่ใน MCP core. ที่ Toronto มี session หนึ่งโดยนัยสรุปว่า "each layer works, but the integration between them does not" — เป็นปัญหา coordination ที่ยังไม่มี winner ชัด

Context น่ากลัว: อาทิตย์เดียวกัน **OX Security** รายงานว่า 15,465 public MCP servers ไม่มี governance layer เลย (ดู brief ถัดไป) — scope line ที่ maintainer ลากไว้ที่ Toronto จึงไม่ใช่เรื่อง philosophy เฉยๆ แต่คือ **เส้นที่กำลังเป็น attack surface ของจริง** ถ้าไม่มี layer อื่นมาปิด

## ทำไมสำคัญ

Pattern ที่สำคัญคือ MCP ยอมรับว่าตัวเอง **"ไม่ใช่ platform แต่เป็น protocol"** — เหมือน HTTP ไม่ใช่ web, เหมือน TCP ไม่ใช่ internet. การยืนยัน scope แคบๆ ของ maintainer มีข้อดีสองชั้น: หนึ่ง, สเป็กจะเสถียร deprecation policy 12 เดือนที่เพิ่งประกาศไปใช้จริงได้; สอง, ecosystem รู้ว่าต้องไปสร้างอะไรเสริม — ไม่ต้องรอ Anthropic สร้าง "Enterprise MCP"

แต่ข้อเสียคือตอนนี้ enterprise CIO ที่จะ deploy MCP agent ต้องประกอบ **5 protocol stack** เอง: MCP (tool access) + A2A (agent-to-agent) + OAuth/OIDC (identity) + OpenTelemetry (observability) + policy engine (OPA / Cedar สำหรับ governance). แต่ละชั้นมี vendor คนละเจ้า compatibility matrix ยาวเป็นหน้าๆ. นี่คือเหตุผลที่ **MCP Gateway** กำลังเป็นหมวดใหม่ที่น่าสนใจที่สุดใน agent infrastructure — ใครรวม 5 ชั้นให้เป็น appliance เดียว ใครชนะ

เทียบกับ **OpenAI AgentKit** (DevDay 2025 — ChatKit + Connector Registry + Agent Builder) หรือ **Microsoft Agent 365** ที่พยายามปิดทุก layer ใน one platform — model-first players เลือกเดินทาง "closed stack เบ็ดเสร็จ"; MCP ecosystem เลือก open stack ที่ compose กัน. ปี 2027 จะเห็นว่าตลาด enterprise ชอบแบบไหนมากกว่า

## มุม AI Agent Platform

**Builders:** ถ้ากำลังสร้าง agent framework / orchestration product ต้องตัดสินใจอย่างชัดเจนว่าจะ **"MCP-native + bring your own identity/governance"** หรือ **"vertically integrated agent runtime"** — ครึ่งๆ กลางๆ แพ้ทั้งสองทาง. Vendor ที่สร้าง MCP Gateway (Pomerium, Boundary, custom Kong plugins) + policy engine wrapper จะเป็น critical path. **Users / business** ที่กำลัง pilot agent ควรวาด protocol diagram ก่อน POC — ถ้าไม่มี identity + audit layer ชัด POC จะไปไม่ถึง production. **Ecosystem:** AAIF ภายใต้ Linux Foundation จะเป็น neutral ground ที่ Anthropic / OpenAI / Google / Microsoft เจอกันได้ — เป็นสถานที่เดียวในตอนนี้ที่ทั้งสี่ยอมส่งคนไปนั่ง. ใครไม่มีเก้าอี้ที่ AAIF อาจตก roadmap ของ enterprise agent stack

## Sources
- [The protocol proliferation problem: Making sense of the open agent stack - The Stack](https://www.thestack.technology/the-protocol-proliferation-problem-making-sense-of-the-open-agent-stack/)
- [MCP Dev Summit Toronto Opens Today — The Protocol Stack Seeks Its Missing Coordination Layer - Forkast](https://forkast.news/mcp-dev-summit-toronto-opens-today-the-protocol-stack-seeks-its-missing-coordination-layer)
- [MCP Dev Summit Toronto - Linux Foundation Events](https://events.linuxfoundation.org/mcp-dev-summit-toronto/)
- [MCP Dev Summit 2026: AAIF Sets A Clear Direction With Disciplined Guardrails - Futurum Group](https://futurumgroup.com/insights/mcp-dev-summit-2026-aaif-sets-a-clear-direction-with-disciplined-guardrails/)

---

## Audio script
วันจันทร์กับอังคารที่ Toronto มี MCP Dev Summit ครั้งใหญ่ที่สุดเท่าที่เคยจัดมา. Linux Foundation กับ Agentic AI Foundation เป็นเจ้าภาพ, 70 คนขึ้นเวที, 6 tracks ไล่ตั้งแต่ architecture จนถึง production operations. แต่ข่าวสำคัญไม่ใช่ feature ใหม่. maintainer จาก Anthropic AWS Microsoft OpenAI ยืนยันตรงกันในห้องว่า MCP จะไม่ขยายไปทำ identity ไม่ทำ observability ไม่ทำ governance. ของพวกนั้นเป็นงานของ layer อื่น. ประโยคนี้ลาก scope line ให้ ecosystem รู้ว่าต้องไปสร้างอะไรเสริม. ตอนนี้ AGNTCY ของ Cisco ตั้งตัวเป็น discovery และ identity layer. A2A protocol รับงาน agent to agent. MCP Gateway กลายเป็นหมวดใหม่ที่น่าสนใจที่สุด ใครรวม 5 ชั้นเป็น appliance เดียวใครชนะ. ความหมายต่อ builder คือต้องเลือกชัด จะเดิน MCP native แล้ว bring your own identity หรือเดิน vertically integrated แบบ OpenAI AgentKit กับ Microsoft Agent 365. ครึ่งๆ กลางๆ แพ้ทั้งสองทาง. ความหมายต่อ enterprise CIO คือก่อน pilot ต้องวาด protocol diagram ก่อน ถ้าไม่มี identity กับ audit layer POC จะไปไม่ถึง production. AAIF ภายใต้ Linux Foundation ตอนนี้เป็นที่เดียวที่ Anthropic OpenAI Google Microsoft ยอมส่งคนมานั่งร่วมกัน ใครไม่มีเก้าอี้ที่โต๊ะนี้อาจตก roadmap enterprise agent ปี 2027
