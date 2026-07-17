---
date: 2026-07-15
slug: oak-60m-seed-ai-native-identity-operating-system
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  A giant editorial cutaway of an "Identity Operating System" control room:
  three columns of glowing badges labeled "HUMAN", "MACHINE", "AI AGENT"
  flowing into one unified plane. Above, block-letter numbers stack:
  "$60M SEED", "50 PEOPLE", "GA". An oak-tree silhouette holds up the plane
  like a load-bearing beam. Editorial isometric style, high contrast,
  1:1 aspect, readable at 200px thumbnail, no real human faces.
image: images/26-07-17-0708-01-oak-60m-seed-ai-native-identity-operating-system.png
---

# Oak เปิดตัว $60M seed — สร้าง Identity Operating System สำหรับยุคที่ agent มีจำนวนมากกว่าคน

## TL;DR
- **15 กรกฎาคม 2026** — Oak ออกจาก stealth ด้วย seed round $60M ที่ co-led โดย Accel, Greylock, CRV เพื่อสร้าง "Identity Operating System" ที่จัดการ human + machine + AI agent identity บน control plane เดียว
- ผู้ก่อตั้ง Shai Morag (serial founder ที่ขาย Ermetic ให้ Tenable ปี 2023) กับ Tal Marom เดินทีม 50 คนใน stealth และผลิตภัณฑ์ **generally available แล้ว**
- Signal ชัดเจน — VC ระดับ tier-1 จ่าย seed ขนาด Series A เพื่อ bet ว่า identity infrastructure ของยุค agent จะเป็น layer แยกจาก IAM แบบเก่า ไม่ใช่ feature ของ Okta / CyberArk

## เกิดอะไรขึ้น

Oak — สตาร์ทอัพ identity ที่อยู่ใน stealth มาเกือบสองปี — เปิดตัววันที่ 15 กรกฎาคมพร้อม $60 ล้านในรอบ seed. Accel, Greylock Partners, และ CRV เป็น co-lead — สามกอง VC ที่แทบไม่เคยยอมแชร์ lead ในรอบเดียวกัน หมายความว่า deal นี้แข่งกันจริงและ syndicate ต้องกดค่า check ลงเพื่อให้ทุกฝ่ายได้ที่นั่ง. Hetz Ventures, AlphaDrive Ventures, และ strategic angels ตามเข้ามาปิดขอบ

ผู้ก่อตั้ง Shai Morag คือคนที่ปลุกปั้น Ermetic — CIEM platform ที่ Tenable ซื้อไปในปี 2023 ราว $265 ล้าน. คู่หูใหม่คือ Tal Marom, อดีต engineering leader ที่ทำงานร่วมกับ Morag มาก่อน. ทั้งสองเก็บทีมเงียบ ๆ 50 คน ระหว่าง stealth และเดินขาย product เข้า enterprise ไปเรียบร้อยแล้ว — press release ระบุตรงว่า Oak **generally available** ในวันเปิดตัว ไม่ใช่ waitlist หรือ private beta

Thesis ของ Oak คือ legacy identity governance (Sailpoint, Saviynt, Okta Governance) ถูกออกแบบมาจากยุคที่ identity หมายถึง "พนักงาน login กับระบบ SaaS สิบตัว". พอ AI agent เริ่ม provisioned ในระดับพันตัวต่อ enterprise — แต่ละ agent มี API key, มี OAuth scope, มี ephemeral credential, มี tool permission ที่เปลี่ยนทุกวัน — ระบบเก่าไม่มี data model ที่รับไหว. Oak เขียน control plane ใหม่ที่ treat human / machine / agent identity เป็น first-class citizen ประเภทเดียวกัน แล้วสร้าง connector ใหม่ในหลักชั่วโมง (เทียบกับหลายเดือนของ legacy)

## ทำไมสำคัญ

seed size $60M เป็นสัญญาณตลาดที่เก่ง — ปีปกติ seed round ใหญ่ที่สุดในโลก security อยู่ที่ 15–25 ล้าน. การที่ Accel/Greylock/CRV ยอมจ่ายระดับนี้ก่อน revenue milestone ใด ๆ แปลว่า diligence ของทั้งสามกองเห็นตรงกัน: identity ของยุค agent จะเป็น re-platform cycle ครั้งใหม่ ไม่ใช่ upgrade path ของ Okta

pattern ที่เห็นเชื่อมกับหลายเรื่องในสองเดือนที่ผ่านมา — Arcade เปิด Agent Gateway ให้ agent ถือ credential แทน user, MCP 2026-07-28 spec เตรียมเปิดตัว OAuth 2.1 + ID-JAG (Identity Assertion JWT Authorization Grant) เป็น standard, Cisco push personal agent architecture บน on-prem. ทุกจุดชี้ไปที่ปัญหาเดียวกัน: **agent proliferation ทำให้ identity เป็น bottleneck เหมือน network เคยเป็นในยุค cloud early days**. Oak positioned ตัวเองให้เป็น "OS" ของ layer นี้ — ท่าเดียวกับที่ Okta ทำกับ SaaS ในปี 2011

signal ต่อไปคือ Okta / CyberArk / Sailpoint ต้อง respond ยังไง. Okta มี "Agent Identity" ที่ยัง feature-level, CyberArk เพิ่งซื้อ Zilla ปีก่อนแต่ยังเป็น governance overlay, Sailpoint post-IPO ยังไม่ทำ AI-native repositioning. ถ้า Oak ปิด Series A ภายในหกเดือนที่ valuation 500M+ (ซึ่งดูมีความเป็นไปได้สูงจาก unit economics ของ security seed rounds) คู่แข่ง incumbent จะเริ่ม acquire เพื่อไม่ให้ตกขบวน

## มุม AI Agent Platform

**Builders** ที่กำลังสร้าง agent framework — อย่ารอให้ identity เป็น afterthought. ทุก agent ควร provisioned พร้อม identity เฉพาะตัว ไม่ใช่ share credential กับ orchestrator หรือ user session. Oak's bet คือ SDK ที่ให้ agent runtime ยิง identity API ทันทีตอน spawn ซึ่งเป็น pattern ที่ open framework (LangChain, CrewAI, Agno) น่าจะ adopt ในอีก 6 เดือน. **Users / business** ที่ deploy agent ใน production — เริ่มถามคำถามที่ Okta ตอบไม่ได้: agent A เข้าถึง Snowflake table ไหนบ้าง, ถ้า agent ถูก compromise revoke access ได้ในกี่วินาที, มี audit trail level ของ tool call มั้ย. ถ้าคำตอบคือ "ยัง" นั่นคือ security gap ที่ CISO จะเริ่มเจอใน red team รอบหน้า. **Ecosystem** — Sailpoint / Saviynt / Okta / CyberArk ต้องเลือกระหว่าง (a) รีบ acquire startup แบบ Oak, (b) rewrite platform เอง (ยากเพราะ tech debt), หรือ (c) ปล่อยให้ new stack ครองยุคใหม่แล้ววิ่งไล่. Enabridge ที่ integrate agent บน enterprise workflow ต้องเช็คว่า identity layer ที่ client ใช้อยู่รับ agent-scale credential ไหวไหม — ไม่งั้น deployment จะติดตอน compliance review

## Sources
- [Backed by $60M in funding, Oak steps out of stealth to fix the identity mess that AI agents are making worse — TechCrunch](https://techcrunch.com/2026/07/15/backed-by-60m-in-funding-oak-steps-out-of-stealth-to-fix-the-identity-mess-that-ai-agents-are-making-worse/)
- [Oak Raises $60M in Seed Funding to Build the AI-Native Identity Operating System — PR Newswire](https://www.prnewswire.com/news-releases/oak-raises-60m-in-seed-funding-to-build-the-ai-native-identity-operating-system-302826349.html)
- [Oak exits stealth with $60M to rewire IAM for AI agents — AI Weekly](https://aiweekly.co/alerts/oak-exits-stealth-with-60m-to-rewire-iam-for-ai-agents)
- [Oak emerges from stealth with $60M to build identity platform — MSSP Alert](https://www.msspalert.com/brief/oak-emerges-from-stealth-with-60m-to-build-identity-platform)

---

## Audio script
สวัสดีครับ วันนี้ 17 กรกฎาคม 2026 มีข่าว security ที่คนสร้าง AI agent ทุกคนควรฟัง. Oak สตาร์ทอัพจาก Israel เพิ่งออกจาก stealth เมื่อวันที่ 15 พร้อมเงิน seed 60 ล้านเหรียญ ที่ co-lead พร้อมกันสามกอง คือ Accel, Greylock, และ CRV. ปกติ seed round ในโลก security ใหญ่ที่สุดอยู่ที่ 15 ถึง 25 ล้านนะครับ 60 ล้านตัวนี้ถือว่า outlier ชัดเจน. ผู้ก่อตั้งคือ Shai Morag ที่เคยขาย Ermetic ให้ Tenable ในราคาราว 265 ล้าน กับคู่หู Tal Marom. Thesis ของเขาคือ identity governance แบบเดิมที่เราคุ้นเคย เช่น Okta, Sailpoint, CyberArk ถูกออกแบบมาจากสมัยที่ identity หมายถึงพนักงานล็อกอินเข้า SaaS สิบตัว. แต่พอเรา deploy agent เป็นพันตัวต่อ enterprise แต่ละตัวถือ API key ถือ OAuth scope ที่เปลี่ยนทุกวัน ระบบเก่ารับไม่ไหว. Oak เลยเขียน control plane ใหม่ที่มอง human, machine, และ AI agent เป็น identity ประเภทเดียวกัน. สำคัญคือ product generally available แล้ว ไม่ใช่ demo. Signal ที่สื่อคือ VC ระดับ tier one เห็นตรงกันว่า identity สำหรับยุค agent จะเป็น re-platform cycle ไม่ใช่แค่ feature เสริมของ Okta. คนที่ deploy agent ใน production ควรถามตัวเองว่า agent ของคุณเข้าถึงระบบไหนได้บ้าง revoke ได้ในกี่วินาที audit trail ครบไหม ถ้าคำตอบยัง คือ security gap ที่จะโดน CISO ถามในอีกไม่กี่เดือนครับ
