---
date: 2026-10-30
slug: persona-ai-identity-ops-case-review
topic: use-case
reading_time_min: 3
sources: 3
image_prompt: |
  An editorial isometric illustration of a security operations center. A
  central glass desk labeled "PERSONA CASE REVIEW AGENT" is surrounded by
  three stacked panels: "ASSISTANT", "AGENTS", "EXTEND". A pipeline flows
  from an incoming queue of ID cards into the desk; from the desk, three
  outputs route to colored lanes labeled "APPROVE", "ESCALATE", "REJECT".
  Above the desk a bold three-line counter reads "30+ EARLY-ACCESS
  CUSTOMERS", "HUNDREDS OF THOUSANDS OF DECISIONS", "HUMAN APPROVAL ON
  CONSEQUENTIAL CASES". A side panel shows an "MCP SERVER" icon plugged
  into an external agent. Dark teal and lime palette, 1:1 aspect, strong
  contrast for 200px thumbnails, no real human faces.
image:
---

# Persona ปล่อย AI suite สำหรับ identity ops — agent ทำ case review แทน แต่ human ยังเซ็น ‘consequential decision’

## TL;DR
- **Persona** (identity verification platform, $2B valuation รอบ 2025) เปิดตัว **Persona AI** ปลาย ต.ค. 2026 — suite 3 ชั้น: **Persona Assistant** (co-pilot), **Persona Agents** (autonomous case review), **Persona Extend** (MCP server ให้ external agent ของ customer เข้าถึง Persona data)
- Scale จริง: **30+ early-access customer**, **“hundreds of thousands of identity decision”** รัน production แล้ว. ไม่เปิด customer name, ไม่เปิด accuracy rate, ไม่เปิด time-to-decision reduction
- Governance pattern สำคัญ: **human approval ยังอยู่สำหรับ consequential decision**, agent ทำ evidence gathering + policy check + recommendation พร้อม visible reasoning
- Thesis ของ CEO Rick Song: ยุค agentic AI ทำให้ **“who is behind the bot?”** เป็นคำถาม infrastructure — identity verification จะต้องเริ่ม verify agent ไม่ใช่แค่คน

## เกิดอะไรขึ้น

30 ต.ค. 2026 Persona (co-founded + CEO โดย Rick Song, ex-Square) เปิดตัว **Persona AI** — suite ที่ embed AI ลึกลง identity verification stack. 3 ชั้น:

- **Persona Assistant** — co-pilot สำหรับ analyst ของ customer: ตอบคำถามเกี่ยวกับ case, drill-down evidence, suggest next action
- **Persona Agents** (Case Review Agents) — รัน case review autonomous: รวบรวม evidence, เทียบ policy ของ customer, recommend decision (approve/reject/escalate) พร้อม **visible reasoning**. permission ตั้งต่อ agent — agent ทำได้แค่สิ่งที่ customer approve ให้
- **Persona Extend** — MCP server ที่ expose Persona data + workflow ให้ **external agent ของ customer เอง** เรียกใช้ (เช่น customer มี agent compliance ใน Mintive, agent นั้นเรียก Persona Extend ผ่าน MCP ไปขอ verify)

ตัวเลขที่ Persona เปิด: **30+ early-access customer**, **“hundreds of thousands of identity decisions in production”**. ไม่มี accuracy rate, ไม่มี time-reduction number, ไม่เปิด customer name. บริษัทเน้นข้อความว่า **human approval ยังอยู่สำหรับ consequential decision** (เปิดบัญชี high-value, approve wire transfer) agent ทำแค่ evidence + recommendation

ที่น่าสังเกต thesis ของ CEO Rick Song: ใน PYMNTS interview เขา argue ว่า fraud landscape กำลังย้ายจาก “fraudster vs user” → “bot vs identity system”. คำถาม core คือ **“who is behind the bot?”** — Persona วาง Extend เป็น infrastructure สำหรับยุคที่ **AI agent ของบริษัท A ต้องยืนยันตัวตนกับระบบของบริษัท B** (เรื่อง capability ที่ Mintive ก็กำลัง push ในมุม governance ภายใน enterprise)

## ทำไมสำคัญ

ตัวเลข Persona ยังเล็กเทียบ UBS (เรื่อง 01) หรือ Mintive (เรื่องสัปดาห์ก่อน) — แต่สำคัญเพราะ **เลือก shape ของเลเยอร์ identity verification ยุค agent**. ก่อนปี 2026 identity verification = ตรวจ user. จาก Persona AI pattern = **ตรวจทั้ง user และ agent ที่ act แทน user**

Pattern ใหญ่ที่กำลังชัด: **enterprise AI stack ปี 2027 มี 3 เลเยอร์ identity**:
1. **User identity** (Okta, Auth0, Microsoft Entra, Persona verify) — ของจริง, มีมา 10 ปี
2. **Agent identity** (Mintive, Rein, Google Agent Garden) — เลเยอร์ใหม่, ใครเป็นเจ้าของ agent, agent มีสิทธิ์เท่าไหร่
3. **Agent-to-service verification** (Persona Extend, OpenAI OAuth for Agents, A2A protocol) — เลเยอร์ที่ยังเพิ่งเริ่ม — เมื่อ agent ของบริษัท A เรียก API บริษัท B ยืนยันยังไงว่า agent นั้น legit

Persona กำลังหยิบตำแหน่ง **เลเยอร์ 3** ก่อนที่คนอื่นจะเห็น — pattern เดียวกับ Stripe หยิบตำแหน่ง payment layer ก่อน 2015

จุดอ่อน: **ไม่มี accuracy number** คือเสียง alarm ให้ CISO. agent ที่ recommend เปิดบัญชี/approve wire ต้องมี false-positive / false-negative rate ที่พิสูจน์ — ไม่งั้นค่ายอมรับไม่ได้ ตราบใดที่ Persona ยังไม่เปิดตัวเลข, 30 early-access customer คงรวมถึง fintech ที่ test ใน non-critical path เท่านั้น

## มุม AI Agent Platform

**Builders** ที่ทำ agent framework / orchestration: Persona Extend คือ pattern ที่ framework ของคุณจะต้อง consume — MCP server สำหรับ identity verification. ปีหน้า customer จะถามว่า “agent ที่คุณสร้างให้ฉัน verify กับ Persona/Jumio/Onfido ยังไง” ถ้าตอบไม่ได้ framework ของคุณไม่ enterprise-ready

**Users / business** โดยเฉพาะ fintech / healthcare / crypto / marketplaces: **agent of your customer may try to call your API**. ถ้าระบบคุณยัง authenticate แค่ user password + 2FA, pattern นี้จะ break ภายใน 12-18 เดือน. ควรเริ่มออกแบบ **agent credential flow** (OAuth for agents, delegated token, verifiable credential) ตั้งแต่ตอนนี้

**Ecosystem**: Rick Song วาง Persona เป็น **identity primitive ของยุค agent** — ทาง Okta มี Auth for GenAI, Microsoft Entra มี Agent ID, Google มี Agent Garden identity. 4-5 ค่ายกำลังเดิมพันเลเยอร์เดียวกัน. ชนะที่ต้องมี **(1) coverage ของ regulated geography** (Persona แข็ง US + UK/EU), **(2) MCP interop** (เพิ่งเริ่ม), **(3) distribution ใน major platform** (Microsoft น่าจะชนะ default enterprise, Okta ชนะ developer-first). Persona เสี่ยงอยู่ตรงไม่มี distribution hub — ชนะได้ถ้า product ดีกว่าชัดเจน หรือถูก Stripe/Visa/Mastercard ซื้อ

## Sources
- [Daily AI Agent News — October 30, 2026 — Persona AI section (AI Agent Store)](https://aiagentstore.ai/ai-agent-news/daily/2026-10-30)
- [Persona AI product page](https://withpersona.com/product/ai)
- [Bots Overtake Fraudsters as Digital Identity’s Main Threat, Says Persona CEO (PYMNTS)](https://www.pymnts.com/?p=2739152)

---

## Audio script
Persona บริษัท identity verification ที่ valuation ล่าสุด 2 พันล้านเหรียญ เปิดตัว Persona AI เมื่อ 30 ตุลาคม สาม layer คือ Persona Assistant Persona Agents และ Persona Extend ตัว Agents ทำ case review อัตโนมัติ รวบรวม evidence เทียบ policy ของ customer แล้ว recommend decision พร้อม visible reasoning แต่ human ยังต้อง approve consequential decision ส่วน Extend เป็น MCP server ที่ expose Persona data ให้ agent ของ customer เอง เรียกใช้ ตัวเลขที่เปิด 30 กว่า early access customer หลายแสน identity decision ใน production บริษัทไม่เปิด customer name ไม่เปิด accuracy rate ไม่เปิดตัว time reduction thesis ของ Rick Song ซีอีโอ บอกว่าโลก agent ทำให้คำถาม who is behind the bot กลายเป็นคำถาม infrastructure identity verification จะต้องเริ่ม verify agent ไม่ใช่แค่คน pattern ใหญ่ที่กำลังชัดคือ enterprise AI stack ปี 2027 จะมี 3 เลเยอร์ identity หนึ่ง user identity สอง agent identity สาม agent to service verification ที่ Persona กำลังเล่น ถ้าคุณทำ fintech healthcare crypto marketplace agent ของ customer อาจเริ่มเรียก API คุณ ถ้าระบบยัง authenticate แค่ password 2FA ภายใน 12 ถึง 18 เดือน จะ break ควรออกแบบ agent credential flow ตั้งแต่ตอนนี้ครับ
