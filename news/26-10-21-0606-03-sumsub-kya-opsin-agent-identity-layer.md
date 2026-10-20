---
date: 2026-10-21
slug: sumsub-kya-opsin-agent-identity-layer
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a security checkpoint built like an
  airport gate. On the left, five labeled briefcases: "AGENT-01",
  "AGENT-02", "AGENT-03", "AGENT-04", "AGENT-05" line up at a scanner labeled
  "KYA GATE". Each briefcase emits a PII sticker that a filter above the gate
  catches. Beside the gate three stacked numbers glow: "65% HAD BREACH",
  "93% FULL ACCESS", "1 in 200 NEED HUMAN". Two badges in the corner read
  "SUMSUB $0 raised today" and "OPSIN $21M SYN+RACE". Cobalt and amber
  palette, strong contrast for 200px thumbnails, 1:1 aspect, no real
  human faces.
image: images/26-10-21-0606-03-sumsub-kya-opsin-agent-identity-layer.png
---

# วันเดียว 2 บริษัทเปิดชั้น "Know Your Agent" — Sumsub ปล่อย KYA Module, Opsin ปิด $21M; identity layer ของ agent กลายเป็น category จริง

## TL;DR
- 20 ต.ค. **Sumsub** (ชื่อเดิมใน KYC ของ fintech ไทย — เคยทำ identity verification ให้ Bitkub, Line BK, Robinhood ไทย) ปล่อย **KYA (Know Your Agent) Module for MCP** — proxy ที่สอดอยู่ระหว่าง agent กับ data store ของบริษัท strip PII ออกก่อน agent เห็น + liveness check ของคนอนุมัติเมื่อ agent action เกิน threshold
- วันเดียวกัน **Opsin** (San Jose) ปิดรอบ **$21M นำโดย SYN Ventures + Race Capital** เพื่อขยาย platform ที่ตามรอย agent ที่พนักงานสร้างใน Copilot / Claude / ChatGPT Enterprise — ลูกค้าแล้ว 20 เจ้า (Culligan, Barry-Wehmiller, Wellstar, UiPath)
- **65% ของ organization เคยมี agent security incident** ใน 12 เดือนที่ผ่าน (Sumsub cited research). **93% ของ misaligned agents มี full unrestricted access** ต่อ system ตัวเอง และ **มีแค่ 1 ใน 200 agent ที่ต้องให้มนุษย์อนุมัติก่อน action** (Opsin stat)
- ทั้งคู่ bet ว่า **agent identity + policy layer** จะกลายเป็น regulated category เหมือน IAM / DLP — ไม่ใช่ feature ของ agent platform แต่คือ product แยก ที่ security team ซื้อ

## เกิดอะไรขึ้น

วันอังคาร 20 ต.ค. — วันเดียวกัน 2 บริษัทประกาศ product + funding ที่ชี้ไปทิศเดียวกัน:

**Sumsub** ที่คนไทย fintech รู้จักดี (identity verification สำหรับ Bitkub, Line BK, StashAway) ประกาศปล่อย **KYA (Know Your Agent) Module สำหรับ Model Context Protocol**. KYA ไม่ใช่ feature wrap — มันเป็น **proxy layer ที่ enterprise ติดระหว่าง AI agent (Claude / ChatGPT / in-house) กับ data store ของบริษัท**. ทุก request ที่ agent ยิง KYA จะ inspect ก่อน, strip PII + sensitive field ออก, แล้วค่อยส่ง sanitized version ให้ agent. ที่น่าสนใจกว่านั้น: ถ้า agent **action เกิน threshold** (เช่น อนุมัติ invoice เกิน $X, access record จำนวนเกิน Y) KYA เรียก **liveness check แบบ real-time** — คือ ping คนที่ควรอนุมัติ, ถ่ายรูป, verify. Rule engine configurable ตาม sensitivity + action type + department. Audit log ครบ ตัวโมดูลเปิดบน Amazon Bedrock AgentCore Gateway ก่อน ตามด้วย MCP gateway อื่น

**Opsin** เป็นเรื่องเดียวกันแต่คนละมุม — Opsin ไม่ได้ proxy traffic แต่ **map ตัว agent → identity → permission → activity** ให้ security team ของ enterprise. Dashboard ของ Opsin แสดงให้เห็นว่าพนักงาน A สร้าง agent 12 ตัวใน Microsoft Copilot, แต่ละตัว access อะไร, call tool อะไร, พฤติกรรม anomalous ตรงไหน. CEO James Pham (จาก Abnormal Security) ขาย product ตรง: **"93% ของ misaligned agent-connected tools มี full unrestricted access ไปยัง system ของตัวเอง และมีแค่ 1 ใน 200 action ที่ต้องการมนุษย์อนุมัติ"** — stat ที่ CISO ฟังแล้วเขียนเช็คเลย. SYN Ventures + Race Capital นำรอบ, 20 enterprise customer แล้ว (Culligan, Barry-Wehmiller, Wellstar Health, UiPath)

Timing coincidence ไม่ใช่ coincidence — Sumsub cite research ของตัวเองว่า **65% ของ organization มี agent security incident อย่างน้อย 1 ครั้งใน 12 เดือนที่ผ่าน และ sensitive data exposure เป็น root cause อันดับ 1**. 2 บริษัท 2 approach ต่างกัน (inline proxy vs. observability + policy) แต่ทั้งคู่กำลัง bet ว่า **"Know Your Agent"** จะเป็น regulated category เหมือน Know Your Customer ที่ Sumsub, Jumio, Onfido เป็น $B business

## ทำไมสำคัญ

12 เดือนที่ผ่านมา enterprise กลัว "model hallucination" กับ "data leakage" ที่ model layer. 6 เดือนที่ผ่านมา focus ย้ายไปที่ **sandbox / runtime isolation** (SPACE ของ Perplexity, OpenShell ของ NVIDIA, Daytona). วันนี้ layer ที่สว่างคือ **identity + policy** — คือจุดที่ "agent คือใคร, acting on behalf of ใคร, มี permission ทำอะไร, และกำลังทำอะไรอยู่". Pattern ที่ CISO ตั้งคำถามกับ vendor agent วันนี้คือ:
1. Agent มี identity แยกจาก user ไหม (ไม่ใช่ใช้ API key ของ user)
2. Permission scope เท่ากับ user หรือ scope down
3. Action log ตรวจสอบย้อนหลังได้ไหม
4. ถ้า agent compromise จะ revoke access ยังไง

Sumsub + Opsin + Microsoft Entra Agent ID + ServiceNow Passport (ที่เปิดเดือนก่อน) + Okta's "Workforce Identity for AI" (ที่เพิ่งประกาศ roadmap) — ล้วน converge มาจุดเดียวกัน: **agent identity ต้องเป็น first-class citizen ของ IAM** ไม่ใช่ shared credential pool. ประวัติศาสตร์ของ IAM บอกว่า category นี้ไม่ consolidate เร็ว (Okta + Microsoft + Ping ยังแชร์ตลาดกัน 10+ ปี) — แต่ winner ชัดคือคนที่ onboard enterprise ก่อน 2027

ส่วน Sumsub ที่ pivot จาก KYC (consumer identity) ไปเป็น KYA (agent identity) — คือ playbook ที่ clever. Sumsub มี infrastructure liveness check + document verification + fraud scoring อยู่แล้ว. การ apply tech stack เดียวกันกับ agent instead of human คือ marginal cost ต่ำ margin สูง. ถ้าคำกล่าวที่ว่า "AI agent คือ digital employee" จริง → KYC compliance ของ digital employee ควร auto ไหลไปที่ KYC vendor เดิม (Sumsub, Jumio, Onfido) ไม่ใช่ startup ใหม่

## มุม AI Agent Platform

สำหรับ **Builders** ที่สร้าง agent framework / app: **agent identity ต้องไม่ reuse user token** — ให้ allocate principal แยก, scope permission ชัด, และ emit audit event ตาม standard (SOC2, ISO 27001, SOX friendly). ถ้า framework ของคุณ (LangGraph, CrewAI, Agno, Pydantic AI, Mastra) ยังใช้ "whatever token the user has" คือ **เตรียมเจอ enterprise block** ที่ security review. สำหรับ **Users / Business** ที่ deploy agent ใน workflow: ก่อนเปิดใช้ agent ใน production ขอให้ security team ตอบ 4 คำถามด้านบน. และ Sumsub + Opsin + Microsoft Entra Agent ID + Harmonic + Lasso Security ล้วนขาย product ที่คลุม 4 คำถามนี้ — vendor eval ไม่ต้อง build เอง. สำหรับ **Ecosystem**: AWS, Microsoft, Google (hyperscaler), Okta, CyberArk, Ping (IAM incumbent), และ Palo Alto, CrowdStrike, Wiz (security) ล้วน likely แข่ง + partner กับ Sumsub/Opsin — M&A activity ชั้นนี้ปี 2027 น่าจะคึกคัก

## Sources
- [Sumsub tightens grip on what AI agents can access (Fintech.Global)](https://fintech.global/2026/10/20/sumsub-tightens-grip-on-what-ai-agents-can-access/)
- [Opsin Raises $21 Million Led By SYN Ventures And Race Capital For AI Agent Security (Pulse 2.0)](https://pulse2.com/opsin-raises-21-million-led-by-syn-ventures-and-race-capital-for-ai-agent-security/)
- [Opsin raises $21M to track what AI agents can reach and do (Runtime Wire)](https://runtimewire.com/article/opsin-21-million-ai-agent-security)

---

## Audio script
วันนี้มีสองข่าวที่ชี้ไปทิศเดียวกัน — Sumsub บริษัท KYC ที่คนไทย fintech รู้จักเพราะทำ identity verification ให้ Bitkub, Line BK, StashAway ประกาศปล่อย KYA Module คือ Know Your Agent — proxy ที่สอดอยู่ระหว่าง AI agent กับ data store ของบริษัท strip PII ออกก่อน agent เห็น และถ้า agent approve invoice เกิน threshold จะเรียก liveness check ของคนอนุมัติแบบ real time. วันเดียวกัน Opsin ที่ San Jose ปิดรอบยี่สิบเอ็ดล้านดอลลาร์ นำโดย SYN Ventures กับ Race Capital เพื่อขยาย platform ที่ตามรอย agent ที่พนักงานสร้างใน Copilot, Claude, ChatGPT Enterprise. Stat ที่ CISO ได้ยินแล้วเขียนเช็คคือ 93% ของ misaligned agent มี full access ไปยัง system ตัวเอง และมีแค่ 1 ใน 200 action ที่ต้องการมนุษย์อนุมัติ. และ Sumsub cite research ว่า 65% ของ organization เคยมี agent security incident ใน 12 เดือนที่ผ่าน. บทเรียนคือ Know Your Agent กำลังจะเป็น category เหมือน Know Your Customer ที่ Sumsub, Jumio, Onfido เป็น business พันล้าน. ถ้าสร้าง agent อยู่อย่า reuse user token — scope แยก permission ให้ชัดและ emit audit event. ถ้าใช้ agent ใน business ก่อน deploy ให้ security team ตอบว่า agent มี identity แยกจาก user ไหม scope อะไร revoke ยังไง.
