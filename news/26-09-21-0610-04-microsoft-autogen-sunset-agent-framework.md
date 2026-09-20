---
date: 2026-09-21
slug: microsoft-autogen-sunset-agent-framework
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: |
  A weathered wooden signpost at a highway fork. Left arrow reads "AUTOGEN"
  and is faded with a small sign underneath saying "MAINTENANCE MODE". Right
  arrow reads "AGENT FRAMEWORK 1.0" glowing bright with a Microsoft-style
  tile grid. In the distance behind the right arrow, a bright horizon; in
  the distance behind the left arrow, a foggy road. Editorial ink-and-wash
  style with cool blue palette, high contrast so the two labels read clearly
  at 200px thumbnail size. 1:1 aspect, no real human faces.
image: images/26-09-21-0610-04-microsoft-autogen-sunset-agent-framework.png
---

# Microsoft AutoGen เข้าสู่ maintenance mode — 54,000 dev ต้องเลือกทางใหม่

## TL;DR
- Microsoft ประกาศ AutoGen เข้า maintenance mode — bug fix + security patch เท่านั้น ไม่มี new feature
- Microsoft Agent Framework 1.0 (Python + .NET, GA เม.ย. 2026) กลายเป็น primary path — เป็นการ merge AutoGen + Semantic Kernel
- ประมาณ 54,000 developer ที่ build บน AutoGen ต้อง migrate — ผลกระทบ ripple ผ่าน CrewAI, LangGraph, และ agent framework ecosystem ทั้งหมด

## เกิดอะไรขึ้น
สัปดาห์นี้ Microsoft ยืนยัน publicly ว่า AutoGen — one of the pioneering multi-agent frameworks ที่ Microsoft Research ปล่อยเมื่อ ปี 2023 — เข้าสู่ maintenance mode อย่างเป็นทางการ. Community management จะยังคงอยู่ (bug fix + security patch), แต่ new feature development ทั้งหมดจะย้ายไปที่ Microsoft Agent Framework ซึ่ง GA ที่ v1.0 เมื่อ 2 เมษายน 2026. Framework ใหม่นี้คือการ merge codebase ของ AutoGen (multi-agent orchestration) กับ Semantic Kernel (enterprise-grade SDK ของ Microsoft) เข้าเป็นตัวเดียว — เป็นการ resolve ความ fragment ที่ community ของ Microsoft เจอมา 2 ปี.

ตัวเลขที่ทำให้เหตุการณ์นี้หนัก: AutoGen มี GitHub star กว่า 30,000 และ developer ประมาณ 54,000 คนที่ผลิตงานบนมัน — ทั้ง academic paper, startup ที่ build agent product บน AutoGen โดยตรง, และ enterprise POC ที่ทำในปี 2024-2025. Migration path มี official guide, แต่ต้องเขียน orchestration logic ใหม่เกือบทั้งหมดเพราะ API surface ต่างจากเดิม. งานที่ dependency ลึกกับ AutoGen (custom agent, GroupChat manager, function calling wrapper) ต้อง refactor เป็น Agent Framework primitives.

News flow ที่กระตุ้น awareness ใหม่ในสัปดาห์นี้คือ combination ของ (1) VentureBeat feature วันที่ 19 ก.ย. เรื่อง "Microsoft retires AutoGen and debuts Agent Framework," (2) GitLab 19.4 add per-agent governance controls (คนเริ่มพูดถึง framework selection อีกครั้ง), และ (3) forge/localization tooling ecosystem ปรับตัวตาม Agent Framework primitives — signal ชัดว่า Microsoft ecosystem ทั้ง stack กำลัง converge.

## ทำไมสำคัญ
AutoGen sunset เป็น first-ever "sunset moment" ของ major agent framework — เป็น proof point ว่า agent framework ecosystem เริ่มเข้าสู่ consolidation phase. LangGraph, CrewAI, Semantic Kernel — และ vendor framework อีกหลายเจ้า — ต้องคิดว่าเดินไปแบบไหน. คำถามที่ enterprise architect ต้องตอบไม่ใช่ "framework ไหนดีที่สุด" อีกต่อไป, แต่เป็น "framework ไหนจะยังอยู่ในปี 2028."

Signal ที่ตามมา: (1) แนวโน้ม winner-take-most ใน agent framework จะเร่งขึ้น — vendor framework (Microsoft Agent Framework, OpenAI Agents SDK, Google Vertex AI Agent Builder) จะครองพื้นที่มากขึ้น, open-source framework ที่ไม่มี vendor backing (เช่น pure-community fork) จะยากที่จะยั่งยืน, (2) enterprise ที่ standardize บน AutoGen ต้อง audit migration cost วันนี้ — ยิ่งช้ายิ่งเสี่ยง technical debt, (3) LangChain / LangGraph ecosystem จะได้ประโยชน์ระยะสั้น (developer หนีจาก AutoGen จะไป LangGraph หรือ CrewAI ก่อน), แต่ระยะยาว vendor framework จะครอง.

Ironic angle: MCP (Model Context Protocol) ที่ Anthropic ปล่อยและ donate ให้ AAIF เมื่อ ธ.ค. 2025 กลายเป็น "neutral ground" ที่ framework ทั้งหมดต้อง compatible กับ. คนแพ้จริงๆ ในเกมนี้ไม่ใช่ AutoGen หรือ Semantic Kernel — แต่คือ agent framework ที่ไม่ได้ align กับ MCP standard.

## มุม AI Agent Platform
สำหรับ **builders**: ถ้าคุณสร้าง agent product บน AutoGen, timeline การ migrate ควรจะเสร็จก่อน Q2 2027 — หลังจากนั้น bug ใหม่จะยาก support เพราะ Microsoft ไม่ commit new fix นอกจาก security. ถ้าคุณเลือก framework ใหม่ตอนนี้, criteria ที่ควรใช้: (1) vendor backing ระยะยาว, (2) MCP compatibility, (3) governance primitive built-in (identity, policy, observability). Agent Framework 1.0 ผ่านทั้ง 3 ข้อ, LangGraph ผ่าน 2 (ยัง experimental กับ governance), CrewAI ผ่าน 1 (community-driven).

สำหรับ **users / business**: framework selection ตอนนี้เป็น strategic decision ระดับ CTO ไม่ใช่ tech lead อีกต่อไป. Wrong bet จะเสีย 6-12 เดือนของ engineering time ในปีข้างหน้า. Enterprise ที่ยังอยู่ในระยะ pilot ควร evaluate 2-3 framework parallel ก่อน commit — cost ของการทำ POC ต่ำกว่า cost ของการ migrate ทีหลังมาก.

สำหรับ **ecosystem**: consolidation phase หมายความว่า agent framework จะกลายเป็น commodity — differentiator ที่แท้จริงจะย้ายไปที่ (1) MCP tool ecosystem (ใครมี integration เยอะกว่า), (2) agent identity + governance layer, (3) vertical agent template. Startup ที่สร้าง framework ทั่วไปโดยไม่มี differentiator ชัด จะเจอ headwind. คนที่สร้าง MCP tools, agent testing/eval, agent observability — ยังมี opportunity ใหญ่.

## Sources
- [Microsoft retires AutoGen and debuts Agent Framework to unify and govern enterprise AI agents (VentureBeat)](https://venturebeat.com/orchestration/microsoft-retires-autogen-and-debuts-agent-framework-to-unify-and-govern)
- [Microsoft AutoGen: The Pioneering Multi-Agent Framework Now in Maintenance Mode (Starlog)](https://starlog.is/articles/ai-agents/microsoft-autogen/)
- [Microsoft Agent Framework: The production-ready convergence of AutoGen and Semantic Kernel](https://cloudsummit.eu/blog/microsoft-agent-framework-production-ready-convergence-autogen-semantic-kernel)

---

## Audio script
Microsoft ยืนยันสัปดาห์นี้ว่า AutoGen — multi-agent framework ที่ปล่อยตั้งแต่ปี 2023 และมี dev ใช้ประมาณ 54,000 คน — เข้าสู่ maintenance mode อย่างเป็นทางการ. new feature ทั้งหมดจะย้ายไป Microsoft Agent Framework version 1.0 ที่ GA ตั้งแต่ต้นเดือนเมษายน. Framework ใหม่คือการ merge AutoGen กับ Semantic Kernel เข้ามาเป็นตัวเดียว. เหตุการณ์นี้เป็น sunset moment แรกของ major agent framework — signal ว่า ecosystem กำลังเข้าสู่ consolidation phase. คำถามของ enterprise ตอนนี้ไม่ใช่ framework ไหนดีที่สุด แต่คือ framework ไหนจะยังอยู่ในปี 2028. Winner จะเป็น vendor framework ที่มี MCP compatibility และ governance built-in. Microsoft Agent Framework, OpenAI Agents SDK, Google Vertex AI Agent Builder อยู่ในกลุ่มนี้. LangGraph กับ CrewAI ได้ประโยชน์ระยะสั้นจาก developer ที่หนีจาก AutoGen แต่ต้องดูระยะยาว. สำหรับธุรกิจที่ pilot agent อยู่ ต้องประเมิน 2-3 framework parallel ก่อน commit เพราะการเลือกผิดตอนนี้ต้องใช้ 6-12 เดือน engineering ในการแก้ทีหลัง. คนที่ได้ประโยชน์จริงๆ ในภาพใหญ่คือคนที่สร้าง MCP tool, agent evaluation, agent observability — ตรงนั้นยังมี opportunity ใหญ่.
