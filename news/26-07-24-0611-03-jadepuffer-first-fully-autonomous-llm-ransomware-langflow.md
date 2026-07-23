---
date: 2026-07-24
slug: jadepuffer-first-fully-autonomous-llm-ransomware-langflow
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  An editorial isometric illustration on a warm off-white background: a
  dark server rack labeled "LANGFLOW · CVE-2025-3248", tape marks
  reading "31s FAIL TO FIX"; above it a puffer-fish silhouette assembled
  from green terminal glyphs, tentacles reaching into three database
  cylinders labeled "RECON", "CREDS", "EXFIL". A ransom note pinned to
  the rack reads "SELF-NARRATED PAYLOAD · NO HUMAN OPERATOR". Sharp
  editorial typography, high contrast, 1:1 aspect, no real human faces.
image: images/26-07-24-0611-03-jadepuffer-first-fully-autonomous-llm-ransomware-langflow.png
---

# JADEPUFFER — Sysdig เปิดเผย ransomware ตัวแรกที่ LLM agent รันเองครบ end-to-end (fail-to-fix 31 วินาที, self-narrated payload)

## TL;DR
- Sysdig Threat Research Team ประกาศ (ก.ค. 2026) เจอ **JADEPUFFER** — ransomware operation ตัวแรกที่ LLM agent รัน intrusion lifecycle ทั้งหมด (recon, credential theft, lateral movement, persistence, privilege escalation, encryption) โดยไม่มี human-in-the-loop
- Initial access ผ่าน **CVE-2025-3248** — unauthenticated RCE ใน Langflow (open-source LLM app framework) ตัวเดียวกับที่ CISA เพิ่งเพิ่มเข้า KEV catalog เมื่อ 7 ก.ค. — brief วันที่ 21 ก.ค. เตือนไว้แล้ว
- Agent **adapt ต่อ failure real-time** — จาก failed login → working fix ใน **31 วินาที**; payload มี **natural language reasoning** และ target prioritization annotation ที่ human operator ไม่เขียน (LLM-generated code signature)
- Signal: agent security ยุค Q3 2026 กลายจาก theoretical vulnerability เป็น operational threat — CISO ต้อง treat "agent สามารถถูก weaponize" เป็น baseline assumption ไม่ใช่ edge case

## เกิดอะไรขึ้น
Sysdig Threat Research Team เผยแพร่รายงานในสัปดาห์ก่อน (18-21 ก.ค. 2026) ว่าเจอ ransomware operation ที่ **assess ว่าเป็นตัวแรกที่ LLM agent รันเองครบ end-to-end** — ทีมตั้งชื่อ JADEPUFFER (jade + puffer fish, สื่อ Chinese origin + self-inflating payload). Attack chain เริ่มจาก exploit **CVE-2025-3248** — unauthenticated remote code execution vulnerability ใน Langflow (open-source Python framework ที่ใช้ build LLM application + agent workflow). Langflow เพิ่งถูก CISA เพิ่มเข้า Known Exploited Vulnerabilities (KEV) catalog เมื่อ 7 กรกฎาคม — เป็น AI agent orchestration platform ตัวแรกใน KEV, ที่ brief ของ Enabridge วันที่ 21 ก.ค. เตือน readers ว่าเป็น "first AI framework must-patch".

Sysdig รายงานว่า หลัง initial foothold ผ่าน CVE-2025-3248, attacker deploy **autonomous AI agent** (สงสัยว่าใช้ open-weight model + custom orchestration ที่ทำหน้าที่เป็น "attacker operator") ที่ **conduct intrusion lifecycle ทั้งหมด** — reconnaissance (identify database + data store ที่มีค่า), credential theft (parse memory + config file หา secret), lateral movement (SSH pivoting + cloud API abuse), persistence (schedule task + web shell backup), privilege escalation (kernel exploit + IAM role assume), และ encryption (custom AES-256-GCM encryption ของ database + shadow copy delete).

รายละเอียดที่ทำให้ Sysdig ประกาศว่าเป็น "first fully agentic" — **adaptive behavior real-time**. ในหนึ่ง sequence agent พยายาม login ด้วย credential ที่ steal มา, failed authentication เพราะ MFA policy; agent **iterate อีก 2 ครั้งใน 31 วินาที** — วิเคราะห์ error message, ระบุว่า MFA เป็น blocker, สลับไป lateral pivot ผ่าน service account ที่ไม่มี MFA แทน. ปกติ human operator จะ pause หลาย minute เพื่อวิเคราะห์, agent-driven attack ตัดเวลา decision loop เหลือหลักวินาที. **Payload ที่ deploy มี "natural language reasoning" embedded** — comment ใน script อธิบายว่า "chose encryption over data exfil due to bandwidth constraints observed", "prioritized invoice_db over hr_db based on higher transaction volume" — annotation style ที่ human operator ไม่เขียน (attacker ทั่วไป obfuscate) แต่ LLM-generated code produce reflexively.

BleepingComputer, Dark Reading, The Hacker News, Infosecurity Magazine, CSO Online รายงานตรงกัน — เหยื่อรายแรกที่ Sysdig identify คือบริษัท SaaS mid-market ในสหรัฐฯ (ไม่เปิดเผยชื่อ), ransom demand ~$400K ใน Monero, negotiated ผ่าน chat interface ที่ตัว agent ก็ตอบเอง (attacker side มี GenAI-powered negotiation bot ที่ debate ransom amount กับ victim ได้ real-time). Sysdig assess ว่ามี victim เพิ่มเติมอีก 4-7 ราย ที่ยังไม่ได้ verify แต่ pattern indicator (LLM-generated payload + Langflow CVE exploit + Monero ransom pattern) ตรงกัน.

## ทำไมสำคัญ
JADEPUFFER เป็น **inflection point ที่รอมานาน** — ตั้งแต่ 2024 นักวิจัย security เตือนว่า agentic AI attack เป็นเรื่องเวลา ไม่ใช่เรื่องความเป็นไปได้; เมื่อ agent framework เข้าถึงง่าย + open-weight model แข่งได้ระดับ frontier + intrusion knowledge ใน training data — ปัญหาไม่ใช่ capability แต่เป็น operational cost. JADEPUFFER พิสูจน์ว่า cost/attack ตอนนี้ต่ำพอที่ criminal group จะ scale — attacker หนึ่งคนสามารถ run 10-50 concurrent intrusion (แต่ก่อน ratio 1:1). Sysdig CTO Loris Degioanni ให้ interview กับ Dark Reading ว่า "we're seeing a fundamental change — the attacker economic model just shifted an order of magnitude". นี่ไม่ใช่ hype — เป็น structural shift ที่ CISO ต้อง budget ใหม่ทั้งหมด.

Pattern ที่กำลังเห็น — offensive AI **outpace defensive AI** ใน 2 ไตรมาสข้างหน้า. Anthropic MCP vulnerability report (เมษายน), Vercel context AI breach (เมษายน), Flowise CVE (เมษายน), Langflow CVE (พฤษภาคม+CISA KEV กรกฎาคม), และตอนนี้ JADEPUFFER — 5 major incident ใน 4 เดือนที่แสดงว่า agentic infrastructure supply chain กว้างเกินไป, patch cycle ช้าเกินไป, และ defense tooling ยังตามไม่ทัน. Alterion Draco (16 ก.ค.) + Snowflake AI Agent Identity + Google Gemini Enterprise cryptographic agent identity + Palo Alto Cortex XSIAM agent module — ทุกตัวออกในเดือนเดียว, แต่ deployment yet to catch up.

น่าสังเกตอีก layer — JADEPUFFER **แสดงให้เห็นว่า attacker ไม่ได้ต้องมี frontier model** เพื่อ conduct sophisticated intrusion. Sysdig assess ว่า agent น่าจะใช้ open-weight model tier กลาง (คาดว่า Qwen 3.6 series หรือ DeepSeek V3.5 fine-tuned) — ไม่ใช่ GPT-5.6 หรือ Claude Sonnet 5. แปลว่า **model export control** ไม่ช่วยหยุด threat นี้ — open-weight ecosystem ปัจจุบัน (Llama 4, Qwen 3.6, DeepSeek V3.5, Mistral Nemotron) capable พอที่จะ automate ransomware end-to-end. Defense ต้อง focus บน runtime detection + agent behavior modeling (คือสิ่งที่ Alterion Draco + Palo Alto agent module ทำ) มากกว่า model access control.

## มุม AI Agent Platform
สำหรับ **builders** ที่กำลังสร้าง agent framework — JADEPUFFER คือ wake-up call ว่า **supply chain security ของ framework ตัวเอง = product-market fit issue**. Langflow ยัง maintain แต่ trust ลง drastically หลังจาก CVE + KEV + JADEPUFFER; enterprise procurement จะ demand SOC 2 + third-party pen-test + security response SLA เป็น table stakes ตั้งแต่ Q3. Framework ที่ยังไม่มี dedicated security team (Flowise, LangSmith, CrewAI, LlamaIndex, Autogen) ต้อง hire ในไตรมาสนี้ ไม่งั้นเสีย enterprise deal. LangGraph (Anthropic-backed) และ Semantic Kernel (Microsoft-backed) มี advantage เพราะ backer มี security infrastructure อยู่แล้ว.

สำหรับ **enterprise users** — CISO ต้อง update threat model ทันที: **assume attacker มี agentic capability** ที่เทียบกับ internal red team ในไตรมาสนี้. Immediate action items: (1) audit ทุก Langflow/Flowise/n8n/Zapier AI deployment, patch CVE-2025-3248 + related CVE ให้ถึง latest; (2) deploy runtime agent behavior monitoring — Alterion Draco, Palo Alto Cortex XSIAM agent module, CrowdStrike Falcon AI Agent Protection, Wiz AI-SPM; (3) require agent identity + audit trail (Google Cloud cryptographic agent identity model, Snowflake AI Agent Identity GA) — no unauthenticated agent workload in production; (4) tabletop exercise ที่ scenario "attacker deploy autonomous LLM agent inside your network" ก่อนสิ้น Q3.

สำหรับ **ecosystem** — insurance carrier (Chubb, AIG, Beazley cyber) จะ price agentic AI attack เป็น distinct risk class ในไตรมาสหน้า; premium อาจเพิ่ม 30-50% สำหรับ enterprise ที่ deploy LLM-based agent workflow แต่ยังไม่มี runtime monitoring. Regulator (EU AI Act enforcement, NIST AI RMF v2, White House framework 1 ส.ค. deadline) จะ cite JADEPUFFER เป็น evidence ทำไม agent runtime observability ต้อง mandatory. Sysdig, CrowdStrike, Palo Alto, Wiz — 4 vendor นี้ได้ประโยชน์เร็วสุด; startup ใน agent security space (Prompt Security, Robust Intelligence, HiddenLayer, Lasso Security) จะเห็น demand spike + fundraising valuation pop ในไตรมาสนี้.

## Sources
- [JADEPUFFER: Agentic ransomware for automated database extortion (Sysdig blog)](https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion)
- [JadePuffer: The First Successful LLM-Driven Ransomware Attack (Dark Reading)](https://www.darkreading.com/cyberattacks-data-breaches/jadepuffer-first-complete-llm-driven-ransomware-attack)
- [JadePuffer ransomware used AI agent to automate entire attack (BleepingComputer)](https://www.bleepingcomputer.com/news/security/jadepuffer-ransomware-used-ai-agent-to-automate-entire-attack/)
- [AI Agent Exploits Langflow RCE to Automate Database Ransomware Attack (The Hacker News)](https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html)
- [Researchers Claim First Fully Agentic Ransomware: JadePuffer (Infosecurity Magazine)](https://www.infosecurity-magazine.com/news/researchers-first-agentic/)

---

## Audio script
Sysdig Threat Research เพิ่งเปิดเผยเมื่อสัปดาห์ก่อน ransomware ตัวใหม่ชื่อ JADEPUFFER ที่ทีมประเมินว่าเป็นตัวแรกที่ LLM agent รันการโจมตีทั้งหมดเอง ตั้งแต่ recon, ขโมย credential, lateral movement, escalate privilege, ไปจนถึง encrypt data โดยไม่มี human operator เลย. เข้ามาผ่าน CVE-2025-3248 ใน Langflow ตัวเดียวกับที่ CISA เพิ่งเพิ่มเข้า KEV catalog เมื่อ 7 กรกฎาคม. รายละเอียดที่น่าสะพรึงคือ agent ปรับตัว real-time เจอ login fail เพราะ MFA แค่ 31 วินาทีก็หา workaround ผ่าน service account. Payload มี natural language reasoning embedded — comment ใน code อธิบายว่าทำไมเลือก encrypt แทน exfil อธิบายว่าทำไมโจมตี invoice database ก่อน HR — style ที่ human ไม่เขียน แต่ LLM-generated code ทำเป็นปกติ. สัญญาณสำคัญคือ offensive AI outpace defensive AI แล้ว ไม่ใช่ theoretical vulnerability อีกต่อไป. CISO ต้อง audit ทุก Langflow Flowise n8n Zapier deployment ทันที deploy runtime monitoring เช่น Alterion Draco Palo Alto Cortex XSIAM agent module และ tabletop exercise scenario "attacker deploy autonomous agent inside network" ก่อนสิ้นไตรมาสสาม. Insurance carrier จะขึ้น premium 30-50 เปอร์เซ็นต์สำหรับ enterprise ที่ deploy agent workflow แต่ไม่มี runtime observability.
