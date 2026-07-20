---
date: 2026-07-21
slug: gemini-enterprise-agent-identity-openai-billing-bifurcation
topic: agent-platform-trend
reading_time_min: 4
sources: 5
image_prompt: |
  A split editorial illustration: on the left half, a Google-blue vault door
  with a glowing circular seal labeled "AGENT IDENTITY — X.509 CERTIFICATE",
  bank-safe deep and heavy. On the right half, an OpenAI-black tollbooth arm
  lowered across a highway, digital meter above it counting "5 → 25 CREDITS
  PER RUN". Between them a signpost reads "TWO GOVERNANCE MODELS". Editorial
  isometric style, sharp typography, high contrast, cream background,
  1:1 aspect, no real human faces.
image: images/26-07-21-0610-01-gemini-enterprise-agent-identity-openai-billing-bifurcation.png
---

# Gemini Enterprise ล็อค identity ระดับ protocol, OpenAI เปิดมิเตอร์คิดเงิน — governance ของ agent แยกเป็นสองรูปแบบ

## TL;DR
- 19 ก.ค. TechTimes ตีเป็น cover story: Google Gemini Enterprise Agent Platform บังคับ cryptographic agent identity (X.509 cert ต่อ agent) ที่ชั้น protocol, ขณะที่คู่แข่งยัง govern ที่ dashboard tier
- OpenAI Workspace Agents billing เปิดใช้จริง 6 ก.ค. — ทุก agent run กิน 5-25 credit บน GPT-5.5 + per-seat fee เดิม; free preview จบแล้วสำหรับ Business/Enterprise/Edu/Teachers
- ตลาด agent governance กำลังแยกสองแนว: **identity-at-protocol** (Google) กับ **usage-at-billing-meter** (OpenAI) — enterprise ต้องเลือกก่อน MCP 2026-07-28 ship ในสัปดาห์หน้าจะซับ pattern นี้ต่อ

## เกิดอะไรขึ้น
วันที่ 19 กรกฎาคม 2026, TechTimes ปล่อยบทวิเคราะห์ที่ก้าวไปไกลกว่า press release เดิม — วางตำแหน่ง Gemini Enterprise Agent Platform ของ Google ให้เป็น "governance leader" ของกลุ่ม hyperscaler เพราะเรื่องเดียว: Google บังคับ agent identity ที่ชั้น protocol ไม่ใช่ที่ dashboard. เอกสาร Google Cloud อธิบายชัดว่า Agent Identity assign X.509 certificate ให้ agent ทุกตัวแบบ unique — token ที่ agent ถือถูก cryptographically bound กับ cert นั้น, ทุก API call / file access / DB query ถูก sign + log + trace ได้เหมือน Entra ID ของพนักงานคน. ไม่มี shared service account, ไม่มี long-lived key ที่ dev สร้างเอง.

Agent Gateway ทำหน้าที่ air traffic control — agent ตัวหนึ่งเรียก model หลายตัวสำหรับ sub-task ต่างกันได้ แต่ยัง keep identity + policy + audit trail ให้เป็นก้อนเดียว. Infosecurity Magazine ที่รายงานฟีเจอร์นี้ตั้งแต่เดือนก่อน เพิ่งจับ pattern ได้ในสัปดาห์นี้ว่า Google กำลังใช้ security architecture นี้เป็นดาบเจาะตลาด regulated (banking, healthcare, government) ที่ CISO ปฏิเสธ agent platform อื่นเพราะไม่มี trust boundary ต่ำกว่าชั้น application.

ในขณะเดียวกัน — และนี่คือส่วนที่ TechTimes เอามาชนกันในบทเดียว — OpenAI เปลี่ยน Workspace Agents ให้เข้าโหมด billing เต็มตัวตั้งแต่ 6 กรกฎาคม. ทุก agent run ใน ChatGPT Business/Enterprise/Edu/Teachers เดี๋ยวนี้ใช้ workspace credits, metered เป็น input / cached input / output tokens สามสาย. Run ปกติบน GPT-5.5 กิน 5-25 credit ต่อครั้ง — คิด on top per-seat subscription ที่ทีมจ่ายอยู่แล้ว. Free preview เดิมประกาศจบ 6 พฤษภาคม แล้วเลื่อนออกไปสองรอบ, ตอนนี้จบจริง. Runs ที่เรียกจากนอก ChatGPT (เช่น agent ตอบใน Slack channel) ยัง free preview อยู่ — เป็น ceasefire ชั่วคราวก่อนขยายมิเตอร์ต่อ.

## ทำไมสำคัญ
สองข่าวนี้ต้องอ่านคู่กัน เพราะมันบอก **enterprise agent governance market กำลังแยกเป็นสอง architecture มาตรฐาน** ที่ CISO / CIO จะต้องเลือกภายในปีนี้. Google เดิมพันว่า enterprise ที่มีความเสี่ยงจริง (FS, healthcare, gov, defense) จะจ่ายเพิ่มเพื่อ identity-at-protocol — เพราะ audit committee, regulator, และ EU AI Act compliance ทั้งหมดต้องการหลักฐานว่าใครทำอะไรเมื่อไหร่ ไม่ใช่แค่ dashboard สรุปรายเดือน. OpenAI เดิมพันตรงกันข้าม — ให้ governance เป็นเรื่อง commercial (credit budget, spend alert, per-workspace quota) แล้วปล่อยให้ identity อยู่ที่ application layer (OAuth, SSO, per-user session). สองแนวไม่ผิด แต่ compatible กันน้อยกว่าที่คิด: agent ที่ audit ได้ระดับ cryptographic ไม่ merge เข้ากับ agent ที่ metered เป็น bucket ของ credit ได้ทั้งดุ้น.

Pattern นี้ตรงกับที่ Anthropic เพิ่งทำ (2 ก.ค.) — เปิด spend alert ที่ 75%/90%, per-user dashboard, SCIM filter — แต่ Anthropic ยังไม่ถึงชั้น cryptographic identity. Salesforce Agentforce ($1.2B ARR) กับ Microsoft Copilot Studio อยู่ตรงกลาง — มี identity ผูก Entra/Google Workspace แต่ยังไม่ถึงระดับ per-agent cert. เมื่อ MCP 2026-07-28 spec ship อีก 7 วัน (28 ก.ค.) — spec ที่มี Enterprise-Managed Authorisation extension เข้า stable + OAuth 2.1/OIDC alignment — pressure ทั้ง architecture จะเพิ่มขึ้นอีกชั้น. คนที่ commit ผิดข้างในไตรมาสนี้ จะต้อง re-architect ในไตรมาสหน้า.

## มุม AI Agent Platform
สำหรับ **builders** ที่กำลังสร้าง framework หรือ orchestration layer: การเลือก integration pattern สำคัญมาก — ถ้า agent ของคุณ deploy บน Google Cloud, ต้อง support X.509 cert-bound token ตั้งแต่ SDK ชั้นล่าง, ไม่ใช่ wrap รอบ generic bearer token. ถ้า deploy บน OpenAI, ต้อง instrument credit budget + spend alert เป็น first-class primitive. Framework ที่ไม่ abstract สองแบบนี้ให้เป็น cross-platform API จะกลายเป็น "Vercel-only" หรือ "Bedrock-only" — จำกัดตลาดตัวเอง.

สำหรับ **users / business**: ถ้าคุณอยู่ในอุตสาหกรรม regulated (finance, healthcare, insurance, government contractor) — cryptographic agent identity จะกลายเป็น non-negotiable ในการ audit ปี 2027. เริ่มถาม vendor ตอนนี้ว่า "agent ของคุณมี unique cert ต่อ instance ไหม? การเรียก tool ถูก sign + log ระดับ protocol ไหม?" ถ้าคำตอบเป็น "SSO + dashboard" — เตรียมงบสำหรับ replatform. ถ้าคุณอยู่ในอุตสาหกรรม less-regulated (marketing, sales, dev tooling, SMB CX) — credit-based agent จะให้ economic transparency ดีกว่า และควร instrument cost per resolved task เป็น North Star metric ทันที. สำหรับ **ecosystem**: identity provider (Okta, Ping, Duo) จะโดนบังคับเข้ามาเล่นในตลาดนี้ในไตรมาสหน้า — Okta Agent Identity Kit เป็น product ที่เดาได้ก่อนสิ้นปี.

## Sources
- [Gemini Enterprise Agent Platform Leads Enterprise AI Governance as OpenAI Starts Billing for Agents — TechTimes (19 Jul)](https://www.techtimes.com/articles/320956/20260719/gemini-enterprise-agent-platform-leads-enterprise-ai-governance-openai-starts-billing-agents.htm)
- [Agent Identity overview — Google Cloud docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview)
- [Google Introduces Unique AI Agent Identities in New Gemini Enterprise — Infosecurity Magazine](https://www.infosecurity-magazine.com/news/google-ai-agent-identities-gemini/)
- [OpenAI Workspace Agent Billing Went Live Monday — TechTimes (8 Jul)](https://www.techtimes.com/articles/319932/20260708/openai-workspace-agent-billing-went-live-monday-token-math-every-team-needs-now.htm)
- [The 2026-07-28 MCP Specification Release Candidate — MCP Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)

---

## Audio script
วันนี้เรามีสองข่าวใหญ่ที่ต้องอ่านคู่กันครับ ทั้งคู่บอกว่า enterprise agent governance กำลังแยกเป็นสอง architecture หลัก TechTimes 19 กรกฎาคมยกให้ Gemini Enterprise Agent Platform ของ Google เป็น governance leader ของ hyperscaler เพราะ Google บังคับ cryptographic agent identity ที่ชั้น protocol agent ทุกตัวมี X.509 certificate ของตัวเอง token ที่ถือถูก sign กับ cert นั้น ทุก API call ทุก file access ทุก database query ถูก log กลับไปหา identity ได้ ไม่มี shared service account ไม่มี long-lived key ที่ dev สร้างเอง ในขณะเดียวกัน OpenAI ก็เพิ่งเปิดมิเตอร์ Workspace Agents billing เต็มตัวเมื่อ 6 กรกฎาคม ทุก agent run กิน 5 ถึง 25 credit บน GPT-5.5 คิดทับ subscription per seat ที่ทีมจ่ายอยู่แล้ว free preview ที่ยืดมาสองรอบจบจริง ทำไมสำคัญครับ เพราะ Google เดิมพันว่า enterprise ในสาย FS healthcare government defense จะจ่ายเพิ่มเพื่อ identity ระดับ cryptographic เพื่อรองรับ audit เพื่อรองรับ EU AI Act OpenAI เดิมพันตรงข้ามว่า governance ควรเป็นเรื่อง commercial แค่ตั้ง credit budget ตั้ง spend alert แล้วปล่อย identity อยู่ที่ application layer สอง architecture นี้ compatible กันน้อยกว่าที่คิด ถ้า MCP spec 2026-07-28 ship อีก 7 วันตามกำหนด pressure ทั้งสองแนวจะเพิ่ม สำหรับ builder ต้อง abstract สองแบบให้เป็น cross-platform API สำหรับ user ในอุตสาหกรรม regulated ให้เริ่มถาม vendor ว่ามี unique cert ต่อ agent instance ไหมครับ ถ้าคำตอบเป็นแค่ SSO plus dashboard ก็เตรียมงบ replatform ในปี 2027 ได้เลย
