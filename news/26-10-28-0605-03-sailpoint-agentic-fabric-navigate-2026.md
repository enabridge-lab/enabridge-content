---
date: 2026-10-28
slug: sailpoint-agentic-fabric-navigate-2026
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  An editorial isometric illustration of a vast grid of thousands of tiny robot
  silhouettes standing in cubicles — each one wearing a glowing identity badge
  on its chest. Above the grid, a tall watchtower searchlight sweeps across
  them, revealing color-coded badges: green for sanctioned, red for shadow
  agents, yellow for over-privileged. Three stacked numbers hang in the sky:
  "79% RUN AGENTS", "2% HAVE IDENTITY TOOLS", "ZERO STANDING PRIVILEGE". A
  ribbon arches over the tower reading "AGENTIC FABRIC". Deep slate background
  with amber alert highlights, strong contrast for 200px thumbnails, 1:1 aspect,
  no real human faces (robot silhouettes OK).
image: images/26-10-28-0605-03-sailpoint-agentic-fabric-navigate-2026.png
---

# SailPoint Navigate 2026 — identity-first governance ของ "non-human workforce" เริ่ม GA

## TL;DR
- **6 ต.ค.** ที่ Austin, SailPoint ประกาศ **Agentic Fabric** ที่ Navigate 2026 — layer ที่ discover + govern AI agent, MCP server, agent credential ผ่าน endpoint/browser sensor + SIEM/XDR + vault scanning
- **Horizons Report:** **79% ของ enterprise** รัน AI agent **ใน production แล้ว** แต่ **มีแค่ 2%** ที่ deploy identity security tool ที่ purpose-built สำหรับ agent — gap ที่ CISO รู้แต่ยังไม่มี vendor ตอบ
- SailPoint ปล่อย product ชั้น new: **Autonomous Agents สามประเภท** (enforce policy, adjust privilege, protect system), **A-ISPM** (Autonomous Identity Security Posture Mgmt), **JIT conditional provisioning** กับ **zero-standing-privilege** ครอบ human + service account + agent
- Signal: agent governance กำลังจาก theoretical ไป operational — layer ที่ IT security ต้องมี before enterprise agent fleet จะ 10× ปี 2027

## เกิดอะไรขึ้น

วันอังคารที่ **6 ต.ค.** ที่ Austin, SailPoint เปิดงาน Navigate 2026 ด้วย keynote ที่ CEO Mark McClain ยืน next to Horizons Report หน้าใหญ่สะดุด — **79% ของ enterprise** respondent รัน AI agent **in production** แล้ว แต่ **มีเพียง 2%** ที่ deploy identity security tool ที่ **purpose-built** สำหรับ agent. gap นี้คือสิ่งที่ SailPoint ตั้งใจจะเติม — product line ใหม่ชื่อ **Agentic Fabric**

Agentic Fabric ประกอบ 4 ชั้น: (1) **Discovery** — scan endpoint, browser extension, SIEM/XDR log, vault, CI/CD pipeline เพื่อหา agent + MCP server + credential ที่คน spawn โดย IT ไม่รู้; (2) **Autonomous Agents สามประเภท** — enforcement agent (apply policy real-time), privilege-adjustment agent (shrink/expand access ตาม context), protection agent (ตัด session เมื่อ anomaly); (3) **A-ISPM** — Autonomous Identity Security Posture Management ที่ใช้ live identity context ใน SailPoint Atlas หา exposure + remediate ทันที; (4) **Conditional JIT** — just-in-time provisioning ที่ default **zero standing privilege** ครอบ human + service account + agent identity ในชั้นเดียว

ที่น่าสนใจคือ **การ frame agent เป็น identity class ใหม่** — ไม่ใช่ user, ไม่ใช่ service account แต่คือ **"non-human worker"** ที่ต้อง onboard, assign role, manage lifecycle, offboard. McClain ให้ quote กับ SiliconANGLE ว่า "we need real-time decisions about whether an agent is doing what's expected" — statement ที่สะท้อนว่า identity vendor ยอมรับ **IGA (Identity Governance Administration) framework เดิมใช้ไม่ได้กับ agent** ที่ action เปลี่ยนทุก prompt

SailPoint ยังประกาศคู่: **kill switch สำหรับ rogue agent** (ตัด credential ของ agent ตัวเดียวโดยไม่กระทบ parent service), **IdentityIQ 9.0** สำหรับ on-prem customer พร้อม automated upgrade tool (customer base จำนวนมากที่ยัง on-prem สำหรับ regulatory reason — financial services, defense). bundle นี้ขัดกับ pattern ของ Microsoft Entra Agent ID (GA 1 พ.ค.) และ WSO2 Agent Manager (GA 16 ก.ย.) ที่ cloud-only — SailPoint ชัดว่าจะเป็น **"identity for agent ที่ enterprise ยังเลือก on-prem ได้"**

## ทำไมสำคัญ

ประเด็นที่หนึ่ง — **79% / 2% gap คือตัวเลขที่ CISO ของทุก Fortune 1000 จะชี้ให้ CEO ดู**. 79% รัน agent แต่ 2% มี tool ที่ govern — เท่ากับ **77% ของ enterprise มี non-human worker fleet แต่ไม่มีระบบ HR + security**. นี่คือ "shadow IT problem" ของ 2017-2020 ที่ scale ×100 — ก่อนหน้า shadow IT คือ "SaaS tool ที่ marketing ซื้อโดย IT ไม่รู้", ตอนนี้คือ **"agent ที่ engineer spawn + ไปเรียก API + ไปจ่ายเงิน + ไป sign document โดยไม่มี audit"**. ตลาด identity governance ที่ Gartner estimate $8B 2025 น่าจะ **double ภายใน 2027** และ SailPoint + Okta + Microsoft + CyberArk จะ fight for share

ประเด็นที่สอง — **IGA framework เดิมหมดอายุ**. Identity governance ปัจจุบัน assume ว่า identity = ตัวตนคงที่ (จะกี่ roles ก็แล้วแต่, pattern การ access เสถียร). Agent คือ identity ที่ **behavior random ตาม prompt**, scope ที่ขอ **ขยาย/หดได้ทุก task**, และ **spawn child agent ตัวเองได้**. จึงต้องมี framework ใหม่: **lifecycle = per-task ไม่ใช่ per-year**, **privilege = conditional ไม่ใช่ permanent**, **audit = trace of decision ไม่ใช่ snapshot of role**. SailPoint วางหมากตั้งแต่ **A-ISPM = ISPM for agent** ซึ่ง Microsoft ยังไม่พูดชัด, Okta ไม่มี equivalent, CyberArk focused on secret อย่างเดียว

ประเด็นที่สาม — **เกิด "non-human HR" category ใหม่**. ถ้า agent คือ worker จริง, enterprise ต้องมี **อัตรากำลัง agent รายไตรมาส**, **performance review** (เท่าไหร่ task สำเร็จ, SLA, cost per task), **termination process** (kill switch คือ step 1). ตลาด HR tech มี Workday, Rippling, BambooHR ที่ serve human — ชั้น "agent HR" ที่ serve non-human มีคน think about แต่ไม่มีใคร productize ครบ. SailPoint ยืน **identity + lifecycle + privilege** ซึ่งคือ 60% ของ non-human HR stack — เหลือ **performance eval + cost allocation + termination orchestration** เป็นช่องว่างสำหรับ startup

## มุม AI Agent Platform

สำหรับ **Builders** (framework/agent companies): ถ้าสร้าง agent framework ยังไม่มี **native identity binding** (เช่น integrate SailPoint, Entra Agent ID, WSO2 Agent Manager, Okta Agent SDK) จะ **ขาย enterprise ไม่ได้** หลังปีนี้. gap: framework ยอดนิยม (CrewAI, LangGraph, Pydantic AI) ยัง optional สำหรับ identity — ส่วนใหญ่ assume developer จะ wire เอง. โอกาส: framework ที่ย้ายไป **"identity-first by default"** ก่อนคนอื่น claim — ขณะที่ **Claude Agent SDK + OpenAI Agents SDK** น่าจะ bundle ของ parent (Anthropic, OpenAI) แต่ open-source framework ยังเปิดช่อง

สำหรับ **Users / Business**: enterprise ที่มี agent 50+ ตัวใน production **ควร deploy agent-identity-governance ไม่ช้ากว่าสิ้นปี** — เริ่มด้วย discovery (หา agent + MCP server ที่ shadow spawn), ตามด้วย inventory + role mapping, สุดท้ายเท่ยม zero-standing-privilege rollout. ไทย enterprise ที่เริ่ม pilot (ธนาคาร, telco, บริษัท insurance ขนาดใหญ่) ส่วนมากอยู่ขั้น "agent 1-5 ตัว, developer spawn เอง" — ขั้นนี้ยังพอ manage ด้วย manual audit; ขั้น 50+ ตัวต้อง tool. ไทย ETDA + สดช. ที่ร่าง AI Governance Act ควร reference identity-first framework เป็นมาตรฐาน

สำหรับ **Ecosystem**: การแยก **cloud-only identity governance (Entra, WSO2)** vs **cloud + on-prem (SailPoint)** จะกลายเป็น differentiator จริงสำหรับ **financial services, defense, healthcare, government** — sector ที่ regulatory บังคับ data residency. SailPoint เลือกวางตรงนี้ขัดกับทิศ Microsoft/Okta — strategy ที่จะ pay-off ถ้า agent adoption ใน regulated sector โตเร็ว

## Sources
- [SailPoint Unlocks a Secure Agentic Era with Autonomous Identity Security (SailPoint press release)](https://www.sailpoint.com/press-releases/sailpoint-unlocks-a-secure-agentic-era-with-autonomous-identity-security)
- [SailPoint Bets on Identity to Govern AI Agents at Navigate 2026 (Futurum Group)](https://futurumgroup.com/?p=96537)
- [Identity security, AI agents — 15 insights from Navigate 2026 (SiliconANGLE)](https://siliconangle.com/2026/10/09/identity-security-ai-agents-15-insights-from-navigate-2026-sailpointnavigate/)
- [AI, Secured — Executive highlights from SailPoint Navigate 2026 (SailPoint community)](https://community.sailpoint.com/events/ai-secured-executive-highlights-and-product-innovations-from-sailpoint-navigate-2026)

---

## Audio script
วันอังคารที่ 6 ตุลาคมที่ Austin, SailPoint เปิดงาน Navigate 2026 ด้วย keynote ที่ CEO Mark McClain ยืนข้าง Horizons Report หน้าใหญ่ — 79 เปอร์เซ็นต์ของ enterprise รัน AI agent ใน production แล้ว แต่มีแค่ 2 เปอร์เซ็นต์ที่ deploy identity security tool ที่ purpose-built สำหรับ agent. gap นี้คือสิ่งที่ SailPoint ตั้งใจจะเติม ด้วย product line ใหม่ชื่อ Agentic Fabric ซึ่งมี 4 ชั้น: discovery ที่ scan endpoint browser SIEM XDR vault pipeline หา agent กับ MCP server กับ credential ที่คน spawn โดย IT ไม่รู้, autonomous agent 3 ประเภท — enforce policy, adjust privilege, protect system, A-ISPM หรือ Autonomous Identity Security Posture Management ที่ใช้ live context หา exposure และ remediate ทันที, และ conditional JIT provisioning ที่ default zero standing privilege ครอบ human service account กับ agent identity ในชั้นเดียว. SailPoint ยังมี kill switch สำหรับ rogue agent และ IdentityIQ 9.0 สำหรับ on-prem customer. ประเด็นต่อจากนี้มีสาม หนึ่ง 79 ต่อ 2 เปอร์เซ็นต์ gap คือตัวเลขที่ CISO ทุก Fortune 1000 จะชี้ให้ CEO ดู — 77 เปอร์เซ็นต์ของ enterprise มี non-human worker fleet แต่ไม่มีระบบ HR กับ security — shadow IT ที่ scale 100 เท่าของ 2017-2020. สอง IGA framework เดิมหมดอายุ — identity governance ปัจจุบัน assume identity เป็นตัวตนคงที่ แต่ agent คือ identity ที่ behavior random ตาม prompt scope ขยายและหดได้ทุก task spawn child ตัวเองได้ — ต้องมี framework ใหม่ที่ lifecycle per task, privilege conditional, audit เป็น trace of decision ไม่ใช่ snapshot of role. SailPoint วางหมาก A-ISPM ก่อน Microsoft Okta CyberArk. สาม เกิด non human HR category ใหม่ — enterprise ต้องมีอัตรากำลัง agent รายไตรมาส performance review termination process — SailPoint ยืน identity กับ lifecycle 60 เปอร์เซ็นต์ของ stack เหลือ performance eval กับ cost allocation กับ termination orchestration เป็นช่องสำหรับ startup. สำหรับ builder ที่สร้าง framework ยังไม่มี native identity binding ขาย enterprise ไม่ได้หลังปีนี้ — framework ที่ย้ายไป identity first by default จะชนะก่อน. สำหรับ enterprise ที่มี agent เกิน 50 ตัว ควร deploy agent identity governance ไม่ช้ากว่าสิ้นปี เริ่มด้วย discovery ตามด้วย inventory และ zero standing privilege. ไทย ETDA กับ สดช. ที่ร่าง AI Governance Act ควร reference identity first framework เป็นมาตรฐาน
