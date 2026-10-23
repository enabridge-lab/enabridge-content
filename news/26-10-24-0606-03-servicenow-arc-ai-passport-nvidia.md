---
date: 2026-10-21
slug: servicenow-arc-ai-passport-nvidia
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a glowing fortified citadel labeled
  "SUPER INTELLIGENCE CONTROL TOWER" at the center. A translucent AI agent avatar
  named "ARC" stands at a checkpoint presenting a hologram passport stamped
  "AI PASSPORT". Three concentric rings surround the citadel, each labeled:
  "SOFTWARE — OPENSHELL", "FIRMWARE — BLUEFIELD DPU", "SILICON — NVIDIA". A
  small banner above reads "INCLUDED AT NO EXTRA COST — EMPLOYEEWORKS". Deep
  navy, ServiceNow green and NVIDIA green palette, strong contrast for 200px
  thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-24-0606-03-servicenow-arc-ai-passport-nvidia.png
---

# ServiceNow ส่ง Arc + AI Passport GA — governance agent ลงลึกถึงชิป NVIDIA BlueField

## TL;DR
- **21 ต.ค.** ที่งาน NVIDIA GTC Berlin, ServiceNow ประกาศ **Arc** GA (general availability) — personal enterprise agent ที่รันบน Mac วันนี้, Windows ตามใน "ภายในไม่กี่สัปดาห์", รวมใน EmployeeWorks Foundation/Advanced/Prime SKU **ไม่คิดเงินเพิ่ม**
- Arc governance โดย **Super Intelligence Control Tower** (ชั้น policy) + **NVIDIA OpenShell** (ชั้น runtime enforcement) — Control Tower monitor behavior, vet access, ตรวจ prompt injection, วัด performance
- **AI Passport** = credential system สำหรับ agent ที่ NVIDIA **BlueField DPU** อ่านได้ — เลเยอร์ hardware root of trust ของ agent identity. **Caveat:** sources ไม่ตรงกันว่า BlueField enforcement live แล้วหรือยังเป็น future release — software OpenShell enforcement ชัดว่า shipping
- Signal: ServiceNow ไม่ขาย "AI feature" เป็น add-on อีกต่อไป — bundle ลง base platform ทั้งหมด = **bet ว่า "agent runtime" ต้องเป็น stack layer ไม่ใช่ product skus**

## เกิดอะไรขึ้น

วันพุธที่ **21 ต.ค.** ที่งาน **NVIDIA GTC Berlin**, ServiceNow ประกาศ **general availability** ของ **Arc** — personal enterprise agent ที่ ServiceNow เปิดตัวไว้ตอน Dreamforce เป็น preview เมื่อ ก.ย. 2026, ตอนนี้ ship เป็น GA บน macOS (Windows ตามภายในไม่กี่สัปดาห์). ที่น่าสังเกตคือ Arc **ไม่มี premium pricing** — รวมอยู่ในทุก SKU ของ **EmployeeWorks** (Foundation, Advanced, Prime) ที่ customer เดิมมีอยู่แล้ว ไม่คิดเงินเพิ่ม

Arc ทำงานผ่าน 3 เลเยอร์:

**เลเยอร์ 1 — Agent execution:** Arc รับ goal จากผู้ใช้ → **plan** วิธีทำ → **execute** ข้ามระบบ enterprise (ServiceNow, Salesforce, SAP, Oracle, etc. ผ่าน MCP) → **self-check** ผลงาน → ปรับ. ถ้า integration ที่ต้องใช้ยังไม่มี, Arc **build on the fly** แล้วรัน integration นั้นภายใน **NVIDIA OpenShell** boundary

**เลเยอร์ 2 — Policy (software):** **Super Intelligence Control Tower** — ชั้น policy ของ ServiceNow ที่ CIO ตั้ง rule ว่า agent ตัวไหนทำอะไรได้บ้าง. **NVIDIA OpenShell** รับ rule นั้นมา enforce ที่ runtime, monitor action, vet access permission, ตรวจ prompt injection, วัด performance. ซึ่ง sources ยืนยันว่า live แล้วตอนนี้

**เลเยอร์ 3 — Hardware root of trust (ยังก่ำกึ่งว่า live):** **AI Passport** — credential ที่ ServiceNow ออกให้ agent, **NVIDIA BlueField DPU** และ **OpenShell** อ่านได้เพื่อ validate permission ที่ silicon layer. ตรงนี้ sources ไม่ตรงกัน — **Investing.com** รายงานว่า BlueField enforcement เป็น "shipping"; **Shashi.co + StockTitan** รายงานว่า hardware enforcement ยังเป็น "future release", software-level OpenShell enforcement เท่านั้นที่ยืนยันว่า live. ตีความอย่าง conservative: AI Passport **spec + API** live, BlueField **hardware enforcement** ยัง roadmap

ลูกค้า early adopter: ServiceNow ยกตัวอย่าง deployment internal + 2-3 customer ที่ยังไม่เปิดชื่อ — ไม่มีตัวเลข deployment จริง, ROI, หรือ incident reduction ให้ reference. ตรงนี้ยัง "บริษัทอ้าง"

## ทำไมสำคัญ

สองสัญญาณที่ต้องจับ

**หนึ่ง — ServiceNow bundle Arc ลง base SKU** = **anti-add-on pricing**. ก่อนหน้านี้ Salesforce ขาย Agentforce เป็น premium (+$2 per conversation), Microsoft ขาย Copilot เป็น $30/user/month. ServiceNow เลือกคนละทาง — bundle ลง Foundation SKU ที่ลูกค้ามีอยู่แล้ว ด้วย narrative **"agent คือ platform feature ไม่ใช่ product"**. ตีความสองแบบ: (a) ServiceNow เชื่อมั่นว่า agent จะ drive revenue ผ่าน usage expansion (ต้องซื้อ ServiceNow module เพิ่ม) ไม่ใช่ per-seat upsell, (b) competitive pressure จาก Oracle/Microsoft บังคับให้ต้อง bundle เพื่อป้องกัน churn ไม่ว่าแบบไหน, **enterprise AI pricing เริ่มเข้าสู่ race-to-zero สำหรับ agent runtime เอง** — เงินจะไปอยู่ที่ **domain context + workflow data** ไม่ใช่ "agent builder"

**สอง — AI Passport + BlueField = agent identity ลงไปที่ silicon**. ตอนนี้ identity ของ agent ยัง fragment มาก — AWS มี AgentCore identity, Oracle มี credential store, Microsoft มี agent accounts (Copilot Studio), Salesforce มี connected app. ไม่มี **cross-vendor standard**. ServiceNow + NVIDIA bet ว่า **ถ้า hardware DPU บังคับ identity verification ที่ silicon-rooted**, มันจะกลายเป็น default (เพราะ NVIDIA ครองตลาด enterprise AI silicon). ตรงนี้ชนกับ **AWS Graviton + Trainium** และ **Google Titanium IPU** (ที่ Google ACE เมื่อ 22 ต.ค. ใช้เป็น root of trust สำหรับ microVM-per-agent). สงคราม silicon ของ agent compute เริ่มแล้วบนเลเยอร์ที่ ลูกค้ามองไม่เห็น

## มุม AI Agent Platform

สำหรับ **Builders** (agent runtime, agent IDE, framework): ถ้า agent คุณจะไป enterprise คุณต้อง **compatible กับ 3 identity standards คู่ขนาน**: AI Passport (ServiceNow/NVIDIA), AgentCore identity (AWS/Bedrock), และ Titanium IPU (Google ACE). ยังไม่มี unified spec และคาดว่าจะไม่มีในปี 2027 — ดังนั้น **identity adapter** เป็นเลเยอร์ที่ตลาดต้องการ. สำหรับ **Users / Business** (CIO ที่ใช้ ServiceNow stack อยู่แล้ว): ไม่ต้องสร้าง agent runtime เอง — Arc GA แปลว่าทีม IT ของคุณได้ agent builder ฟรีที่ bundle กับ EmployeeWorks SKU ที่คุณจ่ายอยู่แล้ว. คำถามไม่ใช่ "ต้องซื้อ agent platform ไหม" แต่คือ **"ควรใช้ Arc เป็น default แล้วเพิ่ม Copilot/Agentforce บน workflow เฉพาะ หรือกลับกัน"**. สำหรับ **Ecosystem**: ความสัมพันธ์ ServiceNow-NVIDIA ลึกขึ้นชัด — ปีที่แล้ว ServiceNow lead investor ใน Writer, ปีนี้ ServiceNow + NVIDIA แชร์ roadmap silicon-level. คู่แข่ง (Workday, Oracle HCM, SAP SuccessFactors) ที่ไม่มี silicon partner จะเสียเปรียบในการขาย **"governance-ready agent"** ให้ enterprise ที่ regulated — เพราะไม่มี hardware-rooted answer

## Sources
- [ServiceNow delivers industry-first personal enterprise agent and policy enforcement with NVIDIA (ServiceNow Newsroom)](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-delivers-industry-first-personal-enterprise-agent-and-policy-enforcement-with-NVIDIA-extending-AI-governance-across-software-and-silicon/)
- [ServiceNow Ships Arc and Extends Agent Governance Toward Silicon (Shashi)](https://www.shashi.co/2026/10/servicenow-ships-arc-and-extends-agent.html)
- [ServiceNow launches Arc AI agent with NVIDIA security features (Investing.com)](https://www.investing.com/news/company-news/servicenow-launches-arc-ai-agent-with-nvidia-security-features-93CH-4962645)

---

## Audio script
วันพุธที่ 21 ตุลาคม ที่งาน NVIDIA GTC Berlin ServiceNow ประกาศ Arc GA — personal enterprise agent ที่รันบน Mac แล้ววันนี้ Windows ตามภายในไม่กี่สัปดาห์ รวมในทุก SKU ของ EmployeeWorks ไม่คิดเงินเพิ่ม Arc ทำงานผ่านสามเลเยอร์ หนึ่งคือ agent execution ที่รับ goal แล้ว plan execute self-check ปรับ ถ้า integration ยังไม่มี Arc build on the fly รันในขอบเขตของ NVIDIA OpenShell. สองคือ Super Intelligence Control Tower ที่ CIO ตั้ง rule ว่า agent ทำอะไรได้บ้าง และ OpenShell รับ rule นั้นมา enforce ที่ runtime monitor action vet permission ตรวจ prompt injection วัด performance. สามคือ AI Passport credential ที่ ServiceNow ออกให้ agent และ NVIDIA BlueField DPU อ่านได้เพื่อ validate ที่ silicon layer ตรงนี้ sources ยังไม่ตรงกัน Investing บอกว่า live แล้ว Shashi กับ StockTitan บอกยัง roadmap ตีความแบบ conservative คือ spec live แต่ hardware enforcement ยังไม่. สองสัญญาณสำคัญคือ ServiceNow bundle Arc ลง base SKU ไม่คิดเงินเพิ่ม = narrative ว่า agent เป็น platform feature ไม่ใช่ product แปลว่า pricing ของ agent runtime กำลัง race to zero เงินจะไปอยู่ที่ domain context กับ workflow data ไม่ใช่ที่ agent builder. และสองคือ AI Passport กับ BlueField ดัน identity ของ agent ลงไปที่ silicon ชนกับ AWS AgentCore และ Google Titanium IPU — สงคราม silicon ของ agent compute เริ่มแล้วบนเลเยอร์ที่ลูกค้ามองไม่เห็น. สำหรับ builder ต้อง compatible กับ 3 identity standards พร้อมกัน และ identity adapter เป็นช่องตลาดที่ยังว่าง สำหรับ CIO ที่ใช้ ServiceNow อยู่แล้วคำถามไม่ใช่ซื้อ agent platform ไหมแต่คือใช้ Arc เป็น default แล้วเพิ่ม Copilot กับ Agentforce บน workflow เฉพาะหรือกลับกัน
