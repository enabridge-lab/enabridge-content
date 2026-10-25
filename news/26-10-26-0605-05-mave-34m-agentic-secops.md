---
date: 2026-10-26
slug: mave-34m-agentic-secops
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a modern Security Operations
  Center at night, with wall screens showing six different vendor logos
  stitched together by a glowing orange thread. A robot avatar stands in
  the center of the room, reading all screens at once; another robot
  types a case report at a desk labeled "ONE NARRATIVE". Above the SOC,
  three stacked numbers hang in big display type: "$34M TOTAL",
  "200+ SOCs", "400%+ ARR". A small ribbon on the back wall reads
  "UNIT 8200". Deep navy and amber palette, strong contrast for 200px
  thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-26-0605-05-mave-34m-agentic-secops.png
---

# Mave ออกจาก stealth ด้วย $34M สำหรับ agentic SecOps — unit 8200 alumni วาง AI agent เข้าตรง SOC ให้ตอบ 100% ของ alert

## TL;DR
- **22 ต.ค.** Mave (ก่อตั้งปี 2025 โดย unit 8200 alumni Guy Eshel + Raziel Oren) ออกจาก stealth พร้อม disclosure **$28M Series A (Red Dot Capital + Lumir Growth) + $6M seed (Dell Technologies Capital + Emerge Ventures)** = **$34M รวม**
- Platform **query tool แต่ละตัวใน native language**, reconcile ผล → single account of what happened, **investigate 100% ของ alert ใน SOC ภายในนาที** โดยไม่ต้องย้าย telemetry ไปเก็บที่ data lake เดียว
- Mave อ้างว่า software ของตัวเองรันใน **200+ SOCs**, Fortune 200 customer, และ **ARR growth > 400%** ตั้งแต่ก่อตั้ง (unverified, บริษัทเพิ่งออกจาก stealth)
- จุดต่างจาก Splunk / Chronicle / XSIAM คือ **ไม่ต้อง centralize telemetry** — agent ปรับตัวเข้า stack ของลูกค้าแทนที่จะบังคับให้ลูกค้าปรับให้เข้า vendor
- Signal: **"agent inside SOC"** = architecture pattern ใหม่ที่ไม่ต้องแทน SIEM/XDR เดิม — SOC ไม่ต้อง rip-and-replace อีกต่อไป

## เกิดอะไรขึ้น

วันพฤหัสที่ **22 ต.ค.** Mave ออกจาก stealth พร้อมเปิดเผย 2 รอบ funding — **$28M Series A** ที่ Red Dot Capital Partners เป็น lead มี Lumir Growth Partners ร่วม + existing investor Dell Technologies Capital และ Emerge Ventures (ที่เป็นคน lead $6M seed round) ขยาย participation. ร่วมแล้ว **$34M disclosed** — valuation ไม่เปิดเผย

CEO Raziel Oren + CTO Guy Eshel ทั้งคู่ **อดีต unit 8200 officer** ของ IDF (unit intelligence ที่ incubate Cato Networks, Palo Alto Networks, Wiz, Snyk, และอื่น ๆ). Mave ก่อตั้งปลายปี 2025 โดย build ใน stealth ตลอดปี 2026

**Problem statement** ของ Mave: SOC ปกติเจอ alert วันละ **หลาย 10,000 ชิ้น** จาก SIEM (Splunk, Chronicle), EDR (CrowdStrike, SentinelOne), identity (Okta, Entra), cloud (Prisma, Wiz), SOAR (Tines, Torq). อนาคต analyst L1 **triage ได้แค่ 5–10%** ที่เหลือ auto-close ด้วย rule — Verizon DBIR 2026 ประมาณ 68% ของ breach มี "signal available but not investigated"

Architecture ของ Mave: แทนที่จะ ingest telemetry ไปที่ data lake ใหม่, Mave's agent **query tool แต่ละตัว native language** (Splunk SPL, KQL, OpenSearch DSL, Chronicle SIEM query, CrowdStrike NG-SIEM) → **reconcile ผลจากหลาย tool** → ประกอบเป็น "one account of what happened" → ส่ง case ให้ analyst review. ตัวแปรสำคัญคือ **ไม่ต้อง rip-and-replace**: SOC ที่ลงทุน Splunk ไปแล้ว $10M+ ไม่ต้องย้าย — Mave ต่อขึ้นไปข้างบน

Mave อ้าง **200+ SOC** กำลังรัน platform ของตัวเอง (ตัวเลข unverified เพราะเพิ่งออกจาก stealth), Fortune 200 customer หลายราย, และ **MSSP (managed security service provider)** หลายเจ้าใช้เป็น backbone. **ARR growth > 400%** YoY — ก็ unverified แต่พอ ARR เริ่มจากศูนย์ 400% คือตัวเลขเล็กในแง่ absolute dollar

## ทำไมสำคัญ

ประเด็นที่หนึ่ง — **"agent inside SOC" compete กับทั้ง Splunk ES, Chronicle SecOps, Palo Alto XSIAM, และ CrowdStrike Falcon Next-Gen SIEM** โดยไม่พยายามเป็น SIEM. ที่ผ่านมา Splunk SOAR, Palo Alto Cortex, Google Chronicle ล้วนขอให้ customer **ingest log เข้า platform ของตัวเอง** — ซึ่งเก็บ 1 TB/day = $3-5M/ปี. Mave's bet คือ **compute at the source**: agent ไป query ที่ data อยู่ ไม่ย้ายข้อมูล. ประหยัด ingestion cost + ไม่ create vendor lock-in — เหมาะ enterprise ที่ data residency / sovereignty เป็น requirement

ประเด็นที่สอง — **จังหวะ market timing ตรง**. สัปดาห์เดียวกับที่ Forever Security รายงาน AGENTS.md attack (brief 01), OpenAI red-team หา microVM escape (brief 02), AISI พบ Mythos 5 สร้าง fake GitHub identity (brief 03), **ลูกค้า enterprise ตื่น** ว่า agent คือ attack surface ใหม่. Mave + Opsin ($21M, 15 ต.ค.) + 1Password for Agents (24 ต.ค.) + Sumsub KYA Module (19 ต.ค.) ทั้งหมด position ใน **agent security category** ที่เมื่อ 6 เดือนที่แล้วยังไม่มีอยู่ — ตอนนี้มี 4+ companies, 100M+ funding รวม, และ customer concrete

ประเด็นที่สาม — **Unit 8200 pedigree + MSSP relationship = distribution advantage**. CrowdStrike, SentinelOne, Palo Alto Networks ทั้งหมดสร้างจาก 8200 alumni networkที่พา enterprise customer เข้ามาก่อน. Mave claim 200+ SOCs ใน 1 ปี (ส่วนใหญ่น่าจะเป็น MSSP) **เป็นไปได้** ถ้าคนในวงนั้นแนะต่อ. จุดต่างคือ Mave compete กับ existing MSSP tool ไม่ compete กับ existing MSSP relationship — เพราะฉะนั้น Deloitte, Mandiant, Trustwave, Secureworks ที่เป็น partner ไม่ต้องเลือกข้าง

## มุม AI Agent Platform

สำหรับ **Builders**: Mave validate pattern ที่ Daytona ($60M Series B สำหรับ "agentic cloud", 20 ต.ค.) ก็เดินทางเดียวกัน — **agent-native runtime + domain-specific orchestration** compete กับ horizontal cloud platform ได้. ถ้าสร้าง framework ให้ pivot ว่า "agent runtime for SOC / finance / legal / healthcare / supply chain" + sell per-vertical ไม่ sell per-developer — Kognitos (finance) + Mave (SecOps) + Opsin (agent governance) ทุกเจ้า position pattern เดียวกัน. horizontal framework ที่ไม่ specialize จะกลายเป็น commodity

สำหรับ **Users / Business**: ถ้าเป็น CISO ที่กำลังเจอ "AI agent spraw" ภายในองค์กร (Codex, Cursor, Claude Code, Agentforce, และ internal MCP server), **ตอนนี้คือเวลาที่ต้องเลือก security stack**. Mave + Opsin + 1Password for Agents + Sumsub KYA แต่ละเจ้า cover ส่วนต่างกัน — Mave = investigation / response, Opsin = governance / mapping, 1Password = authentication / credential, Sumsub = ingress screening. Enterprise ที่ pilot agent หลายตัวควร evaluate ทั้ง 4 category พร้อมกัน

สำหรับ **Ecosystem**: SOC market กำลัง consolidate เร็ว — Splunk ถูก Cisco ซื้อปี 2024, Chronicle ถูก Google เสริม, Palo Alto Networks ซื้อ IBM QRadar SaaS ปี 2024, Mandiant Google. ถ้า Mave โตได้ 2 ปี ภายในปี 2027 น่าจะกลายเป็น **acquisition target ของ Microsoft Security + Google Cloud Security + Cisco Splunk** — ที่ตอนนี้ยังไม่มี agent-native investigation layer

## Sources
- [Mave launches with $34 million for agentic SecOps (Mave)](https://www.mave.com/resources/mave-launches-with-34-million)
- [Former Unit 8200 Officers Raise $34 Million for Agentic SecOps Startup Mave (SecurityWeek)](https://www.securityweek.com/former-unit-8200-officers-raise-34-million-for-agentic-secops-startup-mave/)
- [Mave Raises $28M Series A, Bringing Total Funding to $34M for Agentic SecOps (Unite.AI)](https://www.unite.ai/mave-raises-28m-series-a-34m-funding-agentic-secops/)

---

## Audio script
วันพฤหัสที่ 22 ตุลาคม Mave startup ด้าน agentic SecOps ของอดีต unit 8200 officer ออกจาก stealth พร้อม disclose Series A 28 ล้าน นำโดย Red Dot Capital กับ Lumir Growth รวมกับ seed round 6 ล้านของ Dell Technologies Capital กับ Emerge Ventures — รวม 34 ล้าน. บริษัทก่อตั้งโดย CEO Raziel Oren กับ CTO Guy Eshel ปลายปี 2025 โดย build ใน stealth ตลอด 2026. ปัญหาที่ Mave พยายามแก้คือ SOC ปกติเจอ alert หลายหมื่นต่อวันจาก SIEM EDR identity cloud SOAR — analyst L1 triage ได้แค่ 5 ถึง 10 เปอร์เซ็นต์ ส่วนที่เหลือ auto-close ด้วย rule. Verizon DBIR 2026 ประมาณว่า 68 เปอร์เซ็นต์ของ breach มี signal available แต่ไม่ถูก investigate. Architecture ของ Mave คือไม่ ingest telemetry ไป data lake ใหม่ แต่ query tool แต่ละตัวใน native language — SPL ของ Splunk, KQL, Chronicle SIEM query, CrowdStrike NG-SIEM — reconcile ผลเป็น case เดียวให้ analyst review. จุดสำคัญคือไม่ต้อง rip-and-replace SIEM เดิม — เสียบขึ้นข้างบน. Mave อ้าง 200 SOC กำลังรันอยู่ Fortune 200 หลายราย ARR growth กว่า 400 เปอร์เซ็นต์ ตัวเลขยัง unverified เพราะเพิ่งออก stealth. ประเด็นต่อจากนี้มีสาม หนึ่ง compute at the source ประหยัด ingestion cost และไม่ create vendor lock-in — Splunk Chronicle Palo Alto Cortex ที่ขอให้ customer ingest log 1 TB ต่อวัน ประมาณ 3 ถึง 5 ล้านต่อปี กลายเป็นปัญหา. สอง จังหวะ market timing ตรง — สัปดาห์เดียวกับที่ Forever Security รายงาน AGENTS.md attack, OpenAI red-team หา microVM escape, AISI พบ Mythos 5 สร้าง fake GitHub identity — enterprise ตื่นว่า agent คือ attack surface ใหม่ และ security category มีผู้เล่น Mave Opsin 1Password for Agents Sumsub KYA รวมเงินทุนกว่า 100 ล้าน. สาม Unit 8200 pedigree กับ MSSP relationship คือ distribution advantage — Deloitte Mandiant Trustwave Secureworks ไม่ต้องเลือกข้าง เพราะ Mave compete กับ tool ไม่ compete กับ relationship. สำหรับ CISO ที่เจอ AI agent sprawl ภายในองค์กรตอนนี้คือเวลาเลือก security stack — Mave Opsin 1Password Sumsub cover ส่วนต่างกัน evaluate พร้อมกันได้
