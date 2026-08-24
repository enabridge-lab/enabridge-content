---
date: 2026-08-25
slug: nuggets-authority-control-plane-agent-identity-saas
topic: openbridge-trend
reading_time_min: 3
sources: 3
image_prompt: |
  A wide editorial isometric illustration of a fortified glass gate at the
  entrance of a modern data center. A small robot agent stands at the gate
  holding a glowing badge that reads "AUTHORITY". A guard console beside
  the gate prints a long paper strip labeled "SIGNED ACTION RECEIPT" that
  scrolls out toward an auditor stamp icon. Two policy banners overhead
  read "SPENDING LIMIT" and "HUMAN APPROVAL". Two compliance seals on the
  wall read "EU AI ACT" and "DORA". Deep navy, teal, and amber palette;
  chunky sans-serif labels readable at 200px thumbnail; 1:1 aspect ratio;
  no real human faces.
image: images/26-08-25-0615-04-nuggets-authority-control-plane-agent-identity-saas.png
---

# Nuggets Authority Control Plane — agent identity layer แยกตัวออกจาก hyperscaler suite

## TL;DR
- Nuggets (identity firm) launch **Authority Control Plane (ACP)** 22 ส.ค. 2026 — enterprise policy layer ที่ตรวจทุก agent action กับ verified identity + delegated authority + policy + runtime context
- ทุก decision ปล่อย **signed Action Receipt** (agent, authority, action, outcome) ที่ auditor verify ได้โดยไม่ต้องเปิด internal log
- Ship มาพร้อม spending threshold, expiration, human-approval hook — designed ตรงกับ obligation ของ **EU AI Act + DORA** ที่ high-risk agent operator ต้องส่งใน 12 เดือนถัดไป

## เกิดอะไรขึ้น
วันที่ 22 ส.ค. 2026 Nuggets — identity infra firm ที่ก่อนหน้านี้เป็นที่รู้จักจาก decentralized identity wallet — ปล่อย Authority Control Plane (ACP) เป็น product line ใหม่ที่ตั้งใจแยกตัวเองออกจาก consumer identity wallet ไปเจาะตลาด enterprise agent governance โดยตรง

ACP นั่ง gate ทุก agent action ตรวจ 4 อย่างต่อ request: (1) **identity** — agent นี้คือใคร verify ผ่าน DID/credential, (2) **delegated authority** — agent นี้ได้รับอนุญาตให้ทำ action ประเภทนี้แทน principal (user/org unit) ไหน, (3) **policy** — action นี้อยู่ในกรอบ policy ของบริษัทหรือเปล่า (spending, data access, tool scope), (4) **runtime context** — เวลา, location, session state, previous action ทุก decision จะปล่อย signed **Action Receipt** ที่ record 4 field (agent, authority, action, outcome) — auditor เอา receipt ไป verify กับ Nuggets ledger ได้เลยโดยไม่ต้องเปิด log ของบริษัทลูกค้าเอง

Feature set ที่ ship มาครบ enterprise governance ทั้งหมด: spending threshold แบบ multi-level (per action, per session, per day), expiration บน authority (agent ทำได้แค่ในหน้าต่างเวลา), human-approval requirement ที่ trigger เมื่อ action เกิน threshold, และ per-authority audit เพื่อให้ compliance team review ได้แบบ audit ratio ปกติ

## ทำไมสำคัญ
เรื่องนี้เป็น signal ว่า "agent identity + authorization" เพิ่งกลายเป็น standalone SaaS category ก่อนหน้านี้ทุกคน treat มันเป็น feature ของ agent platform (AWS AgentCore Identity, Google Workforce Identity Federation, MCP DPoP) แต่ Nuggets เพิ่งประกาศว่า vertical นี้ใหญ่พอที่จะขายเป็น product แยก โดยเจาะจงที่ regulated buyer ที่มี compliance overhead — bank, insurance, healthcare, gov contractor

Timing ตรงกับ regulatory pressure ที่ทะยานเข้ามาช่วง 12 เดือน — **EU AI Act** high-risk system provision ที่ effective ในปี 2027 บังคับให้ agent-driven decision ที่ impact สิทธิพลเมืองต้องมี traceability กลับได้ถึง identity + authority ของ agent ตัวที่ทำ; **DORA** (Digital Operational Resilience Act) ที่มีผลกับ financial entity บังคับ audit trail ระดับ operational-resilience audit นี่คือกลุ่มลูกค้าที่ Nuggets เจาะโดยตรง — ไม่ใช่ startup ที่ทำ chatbot demo แต่คือ enterprise ที่โดน regulator เขียน letter ถามหา evidence

Signal ต่อจากนี้: Auth0 (Okta), Ping Identity, ForgeRock, Microsoft Entra จะออก agent-native product ในไม่กี่ quarter — ตลาด identity ที่นิ่งมา 5 ปีเพราะ SSO/MFA อิ่มตัว กำลังกลับมาเปิดโดย agent economy สร้าง new principal type ที่ต้อง verify ต่างจาก human

## มุม AI Agent Platform
สำหรับ **builders** ที่ทำ agent framework/runtime: ยัง treat identity เป็น "wrap OAuth ในตัว agent" ไม่พออีกต่อไป enterprise buyer 12 เดือนถัดไปจะถามหา (1) agent DID / verifiable credential, (2) delegated authority chain ที่ตรวจได้, (3) signed receipt ต่อ action ไม่ใช่แค่ log line ที่ replay ได้ pattern integration ต้องรองรับ policy engine ภายนอก — Nuggets, OPA, Cedar — ไม่ใช่ embed policy ใน framework ตัวเอง

สำหรับ **users/business** ที่ deploy agent ใน workflow: ถ้าอยู่ในอุตสาหกรรมที่ regulator เขียน letter ได้ (bank, insurance, healthcare, listed company) เริ่ม audit trail spec ของ agent ตั้งแต่ pilot อย่ารอจน DORA/EU AI Act deadline ถึงค่อยไปสร้าง retroactive สำหรับ Enabridge ในฐานะ AI Agent Platform โจทย์ใหม่คือ "authority delegation ที่ควบคุมได้" — ลูกค้า Thai SME ที่ deploy agent ใน finance/insurance workflow ต้องเห็น evidence ทำได้ก่อน

สำหรับ **ecosystem** (identity provider, IAM, compliance vendor): agent economy กำลังสร้าง TAM ใหม่ที่ human identity market ไม่มี — agent 100k ตัวใน enterprise (Databricks Agent Bricks number จากสัปดาห์ก่อน) แต่ละตัวต้องมี identity, authority, audit trail Nuggets เลือกช่องเล็กแต่ deep (regulated + EU-first) ผู้เล่นใหญ่ (Okta, Ping) จะขยับตามเร็ว เพราะ existing enterprise contract เอื้อ upsell — ใครที่ tie deep กับ MCP DPoP + A2A protocol ได้ก่อนจะกลายเป็น default

## Sources
- [Nuggets Launches Authority Control Plane for Autonomous AI Agents — The Fintech Times (Aug 22, 2026)](https://thefintechtimes.com/nuggets-launches-authority-control-plane-for-autonomous-ai-agents/)
- [Nuggets launches authority platform for governing enterprise AI agents — Biometric Update](https://www.biometricupdate.com/202607/nuggets-launches-authority-platform-for-governing-enterprise-ai-agents)
- [Enterprise AI Governance Framework — Nuggets Labs](https://www.nuggets.life/docs/nuggets-labs/enterprise-ai-governance-framework)

---

## Audio script
วันนี้ Nuggets ซึ่งเป็น identity infra firm ปล่อย Authority Control Plane เป็น product ใหม่ ที่ตั้งใจแยกตัวเองออกไปเจาะตลาด enterprise agent governance โดยตรง

ตัว platform นั่ง gate ทุก agent action ตรวจ 4 อย่างต่อ request identity ของ agent, delegated authority, policy ของบริษัท, และ runtime context ทุก decision ปล่อย signed Action Receipt ที่ record ครบ 4 field agent authority action outcome ซึ่ง auditor เอาไป verify กับ Nuggets ledger ได้โดยไม่ต้องเปิด internal log ของบริษัทลูกค้า

Feature ครบชุด enterprise governance spending threshold multi-level expiration บน authority human approval hook เมื่อเกิน threshold Timing ตรงกับ regulatory pressure ทั้ง EU AI Act ที่ effective ปี 2027 กับ DORA สำหรับ financial entity ที่มีผลใน 12 เดือนถัดไป

signal สำหรับคนทำ agent platform คือ ตลาด identity ที่นิ่งมา 5 ปีกำลังกลับมาเปิด เพราะ agent เป็น principal type ใหม่ที่ต้อง verify ต่างจาก human สำหรับลูกค้า Thai SME ในอุตสาหกรรม regulated อย่าง finance หรือ insurance ต้องเริ่ม audit trail spec ตั้งแต่ pilot ไม่ใช่รอจน deadline compliance ถึงค่อยสร้างครับ
