---
date: 2026-09-17
slug: agntcon-mcpcon-europe-linux-foundation-governance
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A wide editorial illustration of the RAI Amsterdam convention hall exterior
  with a large banner reading "AGNTCON + MCPCON EUROPE 2026". Above it, three
  logos in equal size — "ANTHROPIC", "BLOCK", "OPENAI" — connected by glowing
  lines to a central pillar labeled "AAIF / LINUX FOUNDATION". At the entrance
  a big neon sign reads "99 SPEAKERS / 20 SPONSORS / MCPA CERT". In the
  foreground three silhouettes with lanyards enter through revolving doors.
  Editorial isometric style, deep blue and Linux-penguin-black palette with
  amber highlights, 1:1 aspect, no real human faces.
image: images/26-09-18-0609-03-agntcon-mcpcon-europe-linux-foundation-governance.png
---

# AGNTCon + MCPCon Europe เปิดที่ Amsterdam วันนี้ — MCP ย้ายจาก Anthropic ไป Linux Foundation จบ, protocol governance เริ่มเป็นทางการ

## TL;DR
- วันนี้ (17-18 ก.ย.) **AGNTCon + MCPCon Europe 2026** เปิดที่ RAI Amsterdam — งาน open-source AI agent ที่ Linux Foundation จัด, มีโปรแกรม MCP track โดยเฉพาะ + panel closing เรื่อง MCP challenges/opportunities
- **99 speakers, 20 sponsors** — keynote โดย David Soria Parra (co-creator MCP, Anthropic), Angie Jones (VP, Agentic AI Foundation), Mazin Gilbert (Executive Director, AAIF)
- เปิดตัว **Model Context Protocol Associate (MCPA) certification** — เป็น cert ทางการตัวแรกของ agent protocol; ecosystem MCP ตอนนี้มี **17,000+ server** ใน registry

## เกิดอะไรขึ้น

เช้าวันนี้ที่ RAI Amsterdam งาน **AGNTCon + MCPCon Europe 2026** เริ่มเปิด — เป็นงาน 2 วัน (17-18 ก.ย.) จัดโดย **Linux Foundation** ครั้งแรกที่รวม 2 category ไว้ด้วยกัน: agent architecture/framework/infrastructure และ Model Context Protocol. งานมี **99 speakers + 20 sponsors** — panel closing เรื่อง "MCP Challenges & Opportunities" มี speaker จาก **GitHub, Hugging Face, Agentic AI Foundation, Arcade**

Keynote list เป็น line-up ที่เล่า governance story ของ MCP ตรง ๆ: **David Soria Parra** (co-creator MCP จาก Anthropic — คน design protocol เดิม); **Angie Jones** (VP, Agentic AI Foundation — องค์กร governance ที่ Anthropic donate MCP ให้เมื่อเดือนสิงหา); **Mazin Gilbert** (Executive Director, AAIF — คนคุม roadmap protocol หลังจากนี้). สาม role นี้อยู่ในสาม organization ที่ต่างกัน: **protocol origin (Anthropic) → foundation (Linux Foundation/AAIF) → community (developer)** — เป็น governance triangle มาตรฐานของ open standard ที่ประสบความสำเร็จ (เทียบกับ Kubernetes/CNCF, React/Meta→OpenJS, K8s conformance)

จุดที่ signal ชัดที่สุดคือ **MCP Associate (MCPA) certification** — cert ทางการตัวแรกของ agent protocol. หลักสูตร cover: MCP server implementation, security best practice, tool design pattern, client integration, ecosystem interop. Exam pool เปิดตอนงาน. เมื่อ protocol มี cert = **มี job market มี hiring signal มี resume line** — เป็น indicator ที่ค่อนข้าง unambiguous ว่า Linux Foundation กำลัง treat MCP เป็น long-term standard ระดับ Kubernetes

ประวัติศาสตร์ย่อ ๆ ของ MCP governance transition: **พ.ย. 2024 Anthropic เปิด MCP spec แรก → เม.ย. 2025 มี server ecosystem ~1,000 → ม.ค. 2026 MCP ecosystem แตะ 17,000 server → ส.ค. 2026 Anthropic donate MCP ให้ Agentic AI Foundation (AAIF) directed fund under Linux Foundation, ร่วมก่อตั้งกับ Block + OpenAI → ก.ย. 2026 AGNTCon + MCPCon Europe formal debut + MCPA cert launch**. หลังจากวันนี้ **Anthropic ไม่ใช่ owner ของ protocol แล้ว** — เป็น contributor รายใหญ่แต่ไม่ใช่ decision maker คนเดียวอีก

## ทำไมสำคัญ

Pattern ที่ทำซ้ำมาแล้วในประวัติศาสตร์ software: **origin company donate protocol/tool ให้ neutral foundation ตอนที่ ecosystem โตพอจนบริษัทเดียวคุมไม่ได้แล้ว**. Google ทำกับ Kubernetes (CNCF, 2015), Facebook ทำกับ React (OpenJS, 2022 หลัง trademark drama), IBM ทำกับ OpenShift Kubernetes stack. Anthropic ทำกับ MCP ปีนี้ **เร็วผิดปกติ** — protocol อายุแค่ 22 เดือน — แต่ก็เข้าใจได้ เมื่อ OpenAI/Google/Microsoft ยอม adopt แล้ว governance ต้อง neutral ไม่งั้น trust ไม่มา

จุดสำคัญคือ **AAIF ไม่ใช่แค่ MCP** — foundation รับ agent protocol อื่นเข้ามา (A2A ก็อยู่ใน orbit), agent registry standard, security policy standard. **Linux Foundation กำลังสร้าง Kubernetes-equivalent สำหรับ agent stack**. เมื่อ 5 ปีก่อน CNCF landscape มี 1,200+ tool; วันนี้ AAIF landscape เริ่มโตแบบเดียวกัน. คำถามคือ **ใครจะเป็น "Docker" ของ agent world** — tool ที่ commoditized โดย foundation หลังจากผู้เล่นเดิมสร้าง traction ไปแล้ว. Bet: ไม่ใช่ MCP (protocol เอง commoditized ยาก) แต่คือ **runtime layer** (Anthropic Claude Managed Agents, OpenAI Agents API, Microsoft Agent Framework) — สนามนี้จะโดน commoditize ใน 24 เดือน

MCPA cert เป็น signal อีกชั้น: **ตลาด hiring MCP dev เริ่มเป็นทางการ**. LinkedIn "MCP engineer" openings ใน US โต 340% YoY (จาก Q3 2025 → Q3 2026, per LinkedIn Talent Insights). เมื่อมี cert **rate card ของ MCP consultant จะเริ่ม tier** — cert holder charge premium ได้; agency ที่ hire MCPA-certified staff จะ market ต่างขึ้น

## มุม AI Agent Platform

สำหรับ **builders**: neutral governance = ปลอดภัยกว่าในการ bet เทคโนโลยี. เดิม build บน MCP มี risk "Anthropic เปลี่ยน spec แบบ breaking change หรือ commercialize" — ตอนนี้ Foundation คุม, breaking change ต้อง proposal process. **โอกาสสำหรับ builder ไทย**: MCPA cert เป็นสอบ online ได้ทั่วโลก — freelancer/consultant ที่เข้ารอบแรกจะมี resume differentiator ในตลาด SEA ที่ยังไม่มีคน cert หลาย

สำหรับ **users/business**: enterprise procurement team ที่เคย push back "AI vendor lock-in" มี answer ให้แล้ว — MCP + AAIF governance = protocol ไม่ผูก vendor. CTO ที่ pitch board ว่า "เราต่อ MCP กับ 5 model provider" มี regulatory + audit story ที่แข็งขึ้น. **Thailand-specific**: กบข./ธนาคารแห่งประเทศไทย/หน่วยงานที่ต้อง audit เทคโนโลยี — เอกสาร reference สำหรับ MCP governance เพิ่งเป็นทางการ

สำหรับ **ecosystem**: consulting firm, system integrator, cloud vendor — MCPA cert สร้าง staffing signal ใหม่. Accenture/Deloitte/PwC จะเริ่ม require MCPA ใน job spec ภายใน 6 เดือน. Startup vendor ที่ไม่ contribute back ให้ AAIF จะเสีย credibility กับ enterprise buyer. **Standard governance = commoditize บาง layer, ปลด lock-in อีก layer** — winner คือ integrator + runtime provider ที่มี differentiation อื่นนอกจาก protocol

## Sources
- [AGNTCon + MCPCon Europe Schedule & Directory](https://agntconmcpconeu26.sched.com/)
- [AGNTCon + MCPCon Europe — Linux Foundation Events](https://events.linuxfoundation.org/agntcon-mcpcon-europe/program/schedule/)
- [AGNTCon + MCPCon Europe 2026: Everything You Need to Know — AI Expert Magazine](https://www.aiexpertmagazine.com/agntcon-mcpcon-europe-2026-everything-you-need-to-know/)

---

## Audio script
วันนี้ที่ Amsterdam งาน AGNTCon plus MCPCon Europe 2026 เปิดแล้ว. งาน 2 วัน 17 กับ 18 กันยา, Linux Foundation จัด, 99 speaker, 20 sponsor. Keynote line up สำคัญมาก: David Soria Parra ผู้ co-create MCP จาก Anthropic; Angie Jones VP ของ Agentic AI Foundation; Mazin Gilbert Executive Director ของ AAIF. สาม role นี้เล่า story ของ MCP governance transition — จาก protocol ของ Anthropic คนเดียว → foundation ที่ Anthropic, Block, OpenAI ร่วมก่อตั้งภายใต้ Linux Foundation. ของใหม่วันนี้คือ Model Context Protocol Associate หรือ MCPA — cert ทางการตัวแรกของ agent protocol. เมื่อ protocol มี cert = มี job market, มี rate card, มี hiring signal. Pattern เดียวกับ Kubernetes เมื่อ 10 ปีที่แล้ว. Anthropic เพิ่งเปิด MCP เดือนพฤศจิกา 2024 — วันนี้ยังไม่ครบ 2 ปีก็ handover governance แล้ว. เร็วผิดปกติ แต่เข้าใจได้ เมื่อ OpenAI Google Microsoft adopt เข้ามาแล้ว trust ต้อง neutral. คำถามระยะยาวคือ ใครจะเป็น Docker ของ agent world — protocol เอง commoditize ยาก แต่ runtime layer จะโดน commoditize ใน 24 เดือนแน่. สำหรับ builder ไทย โอกาสคือ MCPA cert สอบ online ได้ทั่วโลก — คนเข้ารอบแรกจะได้ resume differentiator ในตลาด SEA. สำหรับองค์กรที่เคยกลัว vendor lock-in — MCP plus AAIF governance = answer procurement ที่ audit ได้จริงแล้ว.
