---
date: 2026-08-22
slug: zenity-125m-security-1-billion-agents-governance
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  An editorial illustration of a vast digital citadel with glowing gates.
  Behind the gates, endless rows of tiny robotic AI agents queue for
  inspection — each pausing at a checkpoint where a shield-shaped guardian
  scans their intent. Three headline numbers glowing overhead:
  "1 BILLION AGENTS", "$125M SERIES C", "3X REVENUE (2 YRS)". A subtle
  Fortune 500 crest and a Gartner "LEADER" ribbon sit at the base.
  Editorial isometric style, midnight and emerald palette, dramatic
  lighting. 1:1 aspect, no real human faces.
image: images/26-08-22-0609-03-zenity-125m-security-1-billion-agents-governance.png
---

# Zenity ปิด $125M — "1 billion agents" thesis กลายเป็น governance thesis, revenue โต 3 เท่า 2 ปีติด, SoftBank/Fortune 500 ใช้จริง

## TL;DR
- Zenity ปิด Series C $125M เมื่อ 3 ส.ค. — Norwest นำ, new investor Qumra/Hitachi Ventures/SoftBank Vision Fund 2/LG Technology Ventures, existing Vertex/DTCP/Third Point/Intel Capital ร่วม
- Revenue โต 3 เท่า 2 ปีติดต่อกัน, Fortune 500 + Global 2000 ใช้ (รวม SoftBank Corp), Gartner ตั้งเป็น leader ใน agent governance
- Positioning ใหม่: "secure the era of 1 billion AI agents" — deterministic intent inspection ก่อน action, ไม่ใช่ prompt/log analysis หลัง incident

## เกิดอะไรขึ้น

Zenity — startup อิสราเอลที่ทำ security/governance platform สำหรับ agentic AI — ปิด Series C $125M เมื่อ 3 ส.ค. รอบนำโดย Norwest, พร้อม new investor Qumra Capital, Hitachi Ventures, SoftBank Vision Fund 2, LG Technology Ventures ร่วม existing investor Vertex Ventures, DTCP, Third Point Ventures, Intel Capital. บริษัทเลือก tagline สำหรับรอบนี้ว่า "raises $125 million to secure the era of 1 billion AI agents" — คำที่พาดหัวชี้ตรงว่า thesis ของบริษัทและนักลงทุนคือ agent จะระเบิดจำนวนแบบ exponential

ตัวเลข business ที่บริษัทเปิดออกมา: revenue โต 3 เท่าใน 2 ปีติดต่อกัน — ในอุตสาหกรรม security ที่ growth rate ปกติ 50-80% สำหรับ startup ระดับนี้ 300% x 2 ปี = 9x คือ signal ที่ VC ยอมจ่าย valuation premium. ลูกค้าปัจจุบันรวม Fortune 500 และ Global 2000 หลายเจ้า — SoftBank Corp เป็น reference ที่บริษัทเปิดชื่อได้. Gartner ตั้ง Zenity เป็น leader ใน agent governance category ใน report เมษายน 2026 — เร็วมากสำหรับ category ที่ Gartner เพิ่งสร้าง

Technical differentiator ที่ Zenity เน้น: platform ทำ deterministic intent inspection ก่อน action — เข้าใจว่า agent ตั้งใจทำอะไร แล้วตัดสินใจ allow/modify/block ก่อน tool call จะเกิดขึ้น. แนวคิดนี้ต่างจาก prompt firewall (Lakera, Rebuff) ที่ inspect input, และต่างจาก log-based detection (Datadog LLM Observability, Traceloop) ที่ตามล่าหา anomaly หลัง incident. Zenity เน้น "block before it happens" — pattern เดียวกับ RASP (Runtime Application Self-Protection) ในโลก AppSec เก่า

## ทำไมสำคัญ

รอบนี้และ HappyRobot ปิดในสัปดาห์เดียวกัน (ส.ค. 3-4) ไม่บังเอิญ — สะท้อน 2 มุมของ agent economy ที่เกิดพร้อมกัน: **สร้าง agent** (HappyRobot ทำ voice agent สำหรับ logistics, 1.2B unicorn) และ **ควบคุม agent** (Zenity 125M เพื่อ deterministic governance). ทุกครั้งที่ agent 1 ตัวถูก deploy ในระบบ enterprise, มันสร้างงานให้ security team ที่ต้อง audit permissions, tool binding, data access — เร็วกว่าที่ทีมจะรับได้

ตัวเลข security incident สนับสนุน thesis นี้: 88% ของ organization รายงาน confirmed/suspected AI agent incident ในปีที่ผ่านมา (สูงถึง 92.7% ใน healthcare), แต่มีแค่ 24% มี dedicated AI security team. Cisco State of AI Security 2026 บอกว่ามีแค่ 29% ของ organization รู้สึกพร้อม secure agentic AI. Endor Labs analyze 2,614 MCP implementation พบ 82% ใช้ file operation ที่เสี่ยง path traversal, 67% ใช้ API ที่เสี่ยง code injection. Vulnerable MCP Project track >50 known vulnerability, 13 critical

ที่น่าสังเกตคือ SoftBank Vision Fund 2 กลับมาลงทุน — SoftBank Corp เอง (บริษัทลูก) เป็นลูกค้าอยู่แล้ว. Pattern "investor-customer alignment" นี้เห็นบ่อยในกลุ่ม Vision Fund — Zenity ได้ทั้ง capital + distribution ผ่านทั้ง portfolio company ของ Vision Fund และ enterprise footprint ของ SoftBank Group

## มุม AI Agent Platform

**Builders** ที่สร้าง agent framework: ถ้ายังใช้ approach "let the LLM decide, trust the tool call" จะเจอ pushback หนักจาก enterprise security team ตั้งแต่ 2027 ต้นไป — ต้องมี intent-inspection hook ที่ policy engine (Zenity, Aporia, Lakera, Prompt Security) plug เข้าได้. **Businesses** ที่ deploy agent: security-first จะกลายเป็น table stakes ของ RFP — vendor ที่ตอบไม่ได้ว่า "how do you block an agent from taking an unintended action" จะเสียเปรียบทันที. ทางเลือก practical: (1) ใช้ agent gateway อย่าง Zenity/Cequence เป็น chokepoint, (2) requirement ให้ vendor sign SOC 2 + AI-specific attestation. **Ecosystem**: Palo Alto Networks, CrowdStrike, Wiz มี window แคบ ๆ ในการซื้อ Zenity ก่อน valuation ทะลุ $2B — ปกติ security incumbent จะเข้ามาซื้อ startup ที่โต 300% เมื่อเข้าใกล้ $200M ARR. คาดว่า Q4 2026 หรือ Q1 2027 จะได้เห็นดีล M&A ในเซกเมนต์ agent security

## Sources
- [Zenity Raises $125 Million to Secure the Era of 1 Billion AI Agents (Zenity Newsroom)](https://zenity.io/company-overview/newsroom/company-news/zenity-raises-125-million-to-secure-the-era-of-1-billion-ai-agents)
- [Israeli startup Zenity bags $125M in funding to build the security layer for AI agents (SiliconANGLE)](https://siliconangle.com/2026/08/03/israeli-startup-zenity-bags-125m-funding-build-security-layer-ai-agents/)
- [Zenity secures $125m Series C funding for AI agent governance (Yahoo Finance)](https://finance.yahoo.com/technology/ai/articles/zenity-secures-125m-series-c-111131196.html)
- [Zenity raises $125m to secure AI agents, not models (TNW)](https://thenextweb.com/news/zenity-125m-series-c-ai-agent-security)
- [MCP Security Statistics 2026: CVEs, Vulnerabilities & Breach Data (Practical DevSecOps)](https://www.practical-devsecops.com/mcp-security-statistics-2026-report/)

---

## Audio script
Zenity บริษัท security อิสราเอลปิดรอบ Series C 125 ล้านเหรียญ นำโดย Norwest, SoftBank Vision Fund 2 ลง, Hitachi และ LG ลงด้วย. Tagline ของรอบตรงประเด็นมาก: "secure the era of 1 billion AI agents" — พูดตรง ๆ ว่า thesis คือ agent จะระเบิดเป็นพันล้านตัวใน 2-3 ปี. Revenue โต 3 เท่า 2 ปีติดต่อกัน — เท่ากับ 9 เท่ารวม, ระดับที่ VC ยอมจ่าย premium. Fortune 500 หลายเจ้าใช้แล้ว SoftBank Corp เป็น reference. Technical differentiator: deterministic intent inspection ก่อน action — เข้าใจว่า agent จะทำอะไร แล้วบล็อกก่อนเกิด. ต่างจาก prompt firewall ที่ inspect input และต่างจาก log analysis ที่ตาม anomaly หลัง incident. เหตุที่ตลาดนี้ร้อน: 88% ของ organization รายงาน agent incident ในปีที่ผ่านมา แต่มีแค่ 24% มีทีม security dedicated. สำหรับ builder ที่สร้าง framework — ถ้ายังใช้ approach "let LLM decide, trust tool call" จะเจอ pushback หนักจากปีหน้า, ต้องมี intent-inspection hook ที่ policy engine plug เข้าได้. สำหรับ business — security-first จะกลายเป็น table stakes ของ RFP vendor ที่ตอบไม่ได้ว่า block agent action ยังไงจะเสียเปรียบทันที.
