---
date: 2026-09-30
slug: rsa-agent-id-identity-governance-mcp
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a bank vault door with a giant
  fingerprint scanner labeled "AGENT ID". Inside the vault, a swarm of
  small robot silhouettes each wear ID badges reading "DISCOVER",
  "SECURE", "GOVERN". A human hand at a terminal presses a red button
  labeled "APPROVE HIGH-RISK ACTION". A ticker at the top reads
  "SHADOW AGENTS: 0" in bright green. Cinematic teal-and-gold palette,
  bold text rendering for 200px thumbnails, no real human faces,
  1:1 aspect. Style of a Bloomberg magazine cover.
image: images/26-10-01-0616-02-rsa-agent-id-identity-governance-mcp.png
---

# RSA เปิดตัว "Agent ID" — เอา identity infrastructure ที่คุ้นกับ enterprise มายัดเข้า MCP server กับ AI agent ทั้งกอง

## TL;DR
- 29 ก.ย. ที่ The AI Conference ใน San Francisco — RSA ประกาศ **Agent ID** platform ที่แบ่ง 3 module: **Discover, Secure, Govern** — target ตรงที่ financial services, government, critical infrastructure
- **Discover** ค้น AI agent + MCP server ทั้งที่ known กับ shadow ผ่าน identity/cloud/endpoint/gateway data source; **Secure** enforce policy ผ่าน AI/MCP Gateway — บังคับ **named human operator** approve action สำคัญเช่น wire transfer, PII access, classified data
- **Discover + Secure GA 16 พ.ย. 2026**, Govern (lifecycle) H1 2027 — เปิดฉาก category ใหม่ของ agent identity สำหรับ regulated industries

## เกิดอะไรขึ้น
ที่ The AI Conference — งานที่ Fei-Fei Li ประกาศดีล AMD ในสัปดาห์เดียวกัน — RSA ก็ส่งของแรงตัวเอง: **Agent ID**, product ตัวแรกที่บริษัท identity ตัวเก่าเข้าแล้ว pivot มา address ตรง ๆ กับ AI agent + MCP server. RSA ไม่ใช่ startup — พวกเขาเป็นคนที่ผลิต SecurID token ให้ธนาคารกับหน่วยงานรัฐบาล 30+ ปี. Play นี้คือเอา primitives ที่ regulated organization ยอมรับอยู่แล้ว (SSO, MFA, RBAC, audit trail) มาห่อรอบ agent ใหม่

Platform แบ่ง 3 module. **Discover** ทำงานเหมือน asset inventory: สแกน identity source, cloud provider, endpoint, network gateway เพื่อค้น agent กับ MCP server ที่ทีมต่าง ๆ สร้างเอง — รวม shadow agent ที่ dev แอบ deploy ไว้. **Secure** วางตัวเป็น AI/MCP Gateway ระหว่าง agent กับ system: ทุก call ผ่าน policy check + สำหรับ high-risk action (wire transfer, classified data access, PII access, account modification) บังคับให้มี **named authenticated human** เป็นคน approve. **Govern** จัดการ lifecycle — provision, rotate credential, decommission

Timeline ชัด: **Discover + Secure GA 16 พ.ย. 2026**, Govern **H1 2027**. Target ตรงที่ financial services, government agency, critical infrastructure — sector ที่ต้อง demonstrate "ownership of an AI agent, the systems it can access, and the human who authorized its high-impact actions" ใน compliance report

News นี้ตามหลัง Docusign MCP GA เมื่อวานพอดี — pattern ชัดเจนว่า **MCP กำลังกลายเป็น protocol พื้นฐานที่ enterprise vendor ต้อง address**. ต่างกันที่ Docusign เปิดเป็น **application server** ให้ agent เข้ามาเรียก, RSA เปิดเป็น **identity layer** ที่ agent ทั้งกอง (Claude, ChatGPT, Gemini, in-house) ต้องผ่านก่อนจะทำอะไรก็ตาม

## ทำไมสำคัญ
Signal ที่ 1 คือ **agentic identity เป็น category ใหม่ที่ชัดแล้ว** — ไม่ใช่ extension ของ IAM หรือ CIEM. RSA เป็น incumbent เจ้าแรกที่พูดเรื่องนี้ตรง ๆ แทนที่จะเรียก marketing slide เดิม. Okta, Ping, CyberArk มี 60–90 วันประกาศตัว agent identity ของตัวเอง — ไม่งั้นเสีย mindshare ในหมวดที่ RSA เพิ่งเปิดฉาก. คู่แข่งฝั่ง startup — Astrix, P0 Security, Andesite — จะต้องเลือกจะ pivot ให้ focus แคบลง หรือขายให้ incumbent ก่อน

Signal ที่ 2 คือ **regulated industry ตัดสินใจเดินก่อน**. Gartner คาดว่า 40% ของ agent project จะถูกยกเลิกภายใน 2027 เพราะปัญหา governance — และ Chief Risk Officer ของธนาคารกับหน่วยงานรัฐบาลอ่านสถิตินี้แล้ว. RSA ไม่ได้ target consumer หรือ mid-market — เขา target ธนาคาร รัฐบาล utility. คนที่ต้อง provide **auditable identity chain** สำหรับทุก action ที่ agent ทำแทนมนุษย์. Sector นี้ประกอบด้วย 20–30% ของ IT budget ของทั้งโลก

Signal ที่ 3 คือ **MCP กลายเป็น attack surface ที่ต้อง secure**. RSA เรียกมันตรง ๆ — MCP Gateway. Anthropic เปิด MCP เป็น open protocol เมื่อปีก่อน, ตอนนี้ทุก vendor (Docusign, RSA, NVIDIA OpenShell) กำลังสร้าง infrastructure รอบ MCP. MCP เป็น protocol เดียว, แต่ layer ที่รอบมันจะ fragment เร็วมาก — เหมือน HTTP กับ Cloudflare/Fastly/AWS WAF ตอนต้นยุค 2010s

## มุม AI Agent Platform
**Builders** — ถ้าคุณสร้าง agent framework, expect ว่า enterprise buyer ตั้งแต่ Q1 2027 จะถามว่า framework ของคุณ **compatible กับ RSA Agent Gateway มั้ย** — เหมือนที่เคยถามว่า SSO integration มี SAML/OIDC support มั้ย. Framework ที่ยังไม่ระบุ auth mechanism ต่อ tool call ของ agent (LangChain, CrewAI) มี 6 เดือนก่อน enterprise buyer มองเป็น "not production-ready". **Users / business** — RSA Agent ID เป็น **defensive purchase** ที่ Chief Risk Officer + General Counsel จะดัน เข้ามาถูก IT ก่อนที่ innovation team จะรู้ตัว. ถ้าคุณ deploy agent อยู่ตอนนี้ ให้เตรียม **agent inventory** — list ทุกตัวที่ทีมทำเอง, มี owner ใคร, connect กับ system อะไร — ก่อนที่ audit จะถาม. **Ecosystem** — Hyperscaler ทุกเจ้าจะต้องเลือก: build agent identity เอง (AWS IAM extension, Azure Entra Agent, Google Cloud IAM) หรือ integrate กับ RSA/Okta. Microsoft น่าจะ build เอง (Entra), AWS น่าจะเป็น hybrid, Google ยังไม่ชัด — Q4 นี้ทุกเจ้าต้องประกาศ position

## Sources
- [RSA Launches Agent ID Platform to Secure AI Agents and MCP Servers — CyberSecurityNews](https://cybersecuritynews.com/rsa-agent-id/)
- [RSA Security Extends Identity Management Reach to AI Agents — Security Boulevard](https://securityboulevard.com/2026/09/rsa-security-extends-identity-management-reach-to-ai-agents/)
- [RSA Agent ID Secures AI Agents and MCP Servers With Identity-Based Access Controls — GBHackers](https://gbhackers.com/rsa-agent-id-secures-ai-agents-and-mcp-servers/)
- [Alarm sounds on agentic governance as rapid deployment creates security gaps — Biometric Update](https://www.biometricupdate.com/202609/alarm-sounds-on-agentic-governance-as-rapid-deployment-creates-security-gaps)

---

## Audio script
ข่าวที่สองครับ. RSA — บริษัทที่ทำ SecurID token ให้ธนาคารมา 30 ปี — เมื่อวันอังคารประกาศ Agent ID ที่ The AI Conference ใน San Francisco. Product นี้เป็น identity platform สำหรับ AI agent กับ MCP server โดยเฉพาะ ตัวแรกจาก incumbent ใหญ่ที่พูดเรื่องนี้ตรง ๆ. แบ่งเป็น 3 module. Discover ทำหน้าที่ inventory — สแกน identity source cloud endpoint gateway เพื่อค้น agent กับ MCP server ทั้งที่ known และ shadow ที่ dev แอบ deploy. Secure วางตัวเป็น gateway ระหว่าง agent กับ system ทุก call ผ่าน policy check และสำหรับ action สำคัญเช่น wire transfer หรือ PII access บังคับให้มีคนจริงชื่อจริงเป็นคน approve. Govern จัดการ lifecycle. Discover กับ Secure GA 16 พ.ย. 2026 Govern ครึ่งปีแรก 2027. Target ตรงคือ financial services government critical infrastructure sector ที่ต้อง demonstrate ownership ของ agent กับ human ที่ authorize action ในเอกสาร compliance. Impact สำคัญ 3 อย่างครับ. หนึ่ง Agentic identity กลายเป็น category ใหม่ที่ชัดเจน Okta Ping CyberArk มี 60-90 วันประกาศตัวเอง. สอง regulated industry เดินก่อน — Chief Risk Officer ของธนาคารกับหน่วยงานรัฐบาลอ่านสถิติ Gartner ที่บอกว่า 40 เปอร์เซ็นต์ของ agent project จะถูกยกเลิกภายใน 2027 เพราะ governance. สาม MCP กลายเป็น attack surface — ทุก vendor จะสร้าง infrastructure รอบมัน เหมือน HTTP กับ Cloudflare Fastly ตอนต้น 2010s. สำหรับ builder ถ้าคุณสร้าง framework agent ต้องมี auth mechanism ต่อ tool call ให้ชัด ไม่งั้นถูกมองว่า not production-ready ใน 6 เดือน. สำหรับ business ถ้าคุณ deploy agent อยู่ตอนนี้ เตรียม agent inventory ก่อน audit จะถาม ครับ.
