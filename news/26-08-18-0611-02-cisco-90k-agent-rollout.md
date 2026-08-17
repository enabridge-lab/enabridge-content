---
date: 2026-08-18
slug: cisco-90k-agent-rollout
topic: use-case
reading_time_min: 5
sources: 5
image_prompt: |
  Editorial isometric cutaway of a giant office tower with 90,000 tiny
  desk silhouettes glowing softly, each with a small floating agent orb
  hovering above it; a hyperscale on-premises data center wing juts out
  of the base, cables threading up through every floor. Foreground:
  three huge stacked numerals — "90,000 EMPLOYEES", "$9B FY26 GUIDE",
  "ON-PREM ROUTED". Deep navy, brushed steel, and warm amber accents;
  dramatic chiaroscuro; crisp editorial typography readable at 200px
  thumbnail; 1:1 aspect; silhouettes only, no real human faces, no logos.
image: images/26-08-18-0611-02-cisco-90k-agent-rollout.png
---

# Cisco แจก AI agent ให้พนักงานทั้ง 90,000 คน — เดินสูตร on-prem + model routing เพื่อ cost + trust

## TL;DR
- **Cisco** เริ่ม rollout AI agent **personalized ต่อพนักงาน** ให้ครบทั้ง **90,000 employees** จากปลาย ก.ค. (fiscal 2027 kickoff) — เป็น enterprise-wide rollout ที่ใหญ่ที่สุดในรอบ AI era ของ US large-cap
- Agent ทำ **model routing** ต่อ task — task ง่ายส่งไป cheap model, task ยากส่งไป frontier — ไม่ default frontier ทุก call เพื่อคุม cost
- Infrastructure **on-premises เป็นหลัก** — Cisco บอกว่าให้ control cost + data security ได้ดีกว่า cloud managed
- Context: Cisco บันทึก AI-related orders **$2B ใน FY25**, ปรับ **FY26 guidance ขึ้นเป็น $9B** — 4.5x YoY, hyperscaler driven; internal rollout นี้คือ "eat our own dog food" pitch
- Timing น่าคิด: rollout **มาพร้อม layoff รอบใหม่เดือนเดียวกัน** — trust experiment ของทั้ง industry

## เกิดอะไรขึ้น

Cisco announce ตั้งแต่ 1 ก.ค. (Fortune, People Matters) ว่าจะเริ่ม deploy AI agent **personalized ต่อพนักงาน** ให้ทั้ง 90,000 คน โดยเริ่มจากวันแรกของ fiscal 2027 (28 ก.ค.). ณ วันที่ 15 ส.ค. rollout เดินหน้าใน production เต็มระดับ — ทำให้ Cisco เป็น US large-cap enterprise แรกที่ hit "100% employee AI agent coverage" นับ headcount

Architecture ที่ CFO Mark Patterson เปิดเผยใน Fortune interview คือ **cost-first routing**: agent ของพนักงานแต่ละคนไม่ได้ต่อ frontier model เป็น default; ระบบวิเคราะห์ task ก่อนแล้ว route ไป model tier ที่เหมาะ — task ง่าย (email summarize, meeting note) ส่งไป small model on-prem, task ซับซ้อน (financial analysis, code refactor) ส่งไป Claude/GPT/Gemini frontier tier. Pattern นี้เทียบตรงกับ **NVIDIA Nemotron 3.5 Lightning + NeMo Switchyard** ที่ NVIDIA launch วันที่ 11 ส.ค. — ทิศทาง "routing เป็น table stakes" ตกผลึกในเดือนเดียวกัน

จุดที่ต่างจาก Klarna, JPMorgan, Moderna ที่ประกาศ AI transformation ก่อนหน้า: **on-premises infra เป็นหลัก**. Cisco ใช้ compute ของตัวเอง (จาก Splunk acquisition + internal GPU deployment) เพื่อคุม cost per query + audit trail. Cisco บอกว่านี่คือ moat: บริษัทที่ไม่มี infra จะจ่าย per-token bill ที่ scale ไม่ predictable — ตัวเลข rough คือ cost per employee per year สำหรับ full agent access อยู่ที่ **$4,000-6,000** ถ้าใช้ cloud managed vs **$1,200-1,800** ถ้า on-prem routed

Financial context ที่ต้องใส่ไว้: Cisco รายงาน AI-related orders ที่ **$2B ใน FY25** และปรับ **FY26 guidance ขึ้นเป็น $9B** — เกือบ 5x growth. driver หลักคือ hyperscaler ที่ซื้อ Silicon One + optics + Splunk observability; แต่ narrative ที่ Cisco ต้องขาย wall street คือ **"เรา sell เพราะเราใช้"** — internal rollout 90K จึงเป็น marketing asset ระดับ Chuck Robbins CEO keynote

Timing ที่หลาย analyst หยิบขึ้นมาพูดคือ rollout **มาพร้อม layoff รอบใหม่** (ประมาณ 4,000 ตำแหน่งเดือน ก.ค.) — UC Today เขียนว่านี่จะกลายเป็น "biggest trust test" ของ enterprise AI ปีนี้: employee จะเชื่อไหมว่า agent มาช่วยไม่ใช่มาแทน

## ทำไมสำคัญ

Rollout นี้ตอบ questions ที่ CFO/CIO ทุกคนถามกัน: **cost per employee ต่อปีเท่าไหร่? ROI จริงเท่าไหร่? on-prem ประหยัดจริงไหม?** Cisco เผยตัวเลขจริงที่ vendor ส่วนใหญ่ไม่กล้าเปิด — ทำให้กลายเป็น **reference architecture ที่ CIO ของ Fortune 1000 จะลอกภายใน 12 เดือน**

Pattern ที่เห็น: **enterprise ที่ own compute (Cisco, IBM, Oracle, Dell) มี positioning ที่ software-only competitor ทำไม่ได้** — pitch "your data ไม่ออกจาก perimeter" + "cost ไม่ผูกกับ token pricing volatility". นั่นแปลว่า **cycle การซื้อของ Cisco/Dell/HPE ในปี 2027 น่าจะโตกว่า public cloud IaaS ครั้งแรกในรอบ 8 ปี** — ไม่ใช่เพราะ cloud แพ้, แต่เพราะ agent workload มี profile ที่ต่าง (predictable, always-on, latency-sensitive)

จุดที่ต้องระวังคือ **layoff timing paradox**: ถ้า Cisco ประกาศ productivity gain ในไตรมาสหน้า พร้อมกับ layoff รอบใหม่ = narrative "AI แทนคน" ที่ทั้ง media และ union จับได้แน่. ตรงข้าม ถ้า Cisco ยัน "agent ช่วย ไม่แทน" แต่ productivity ไม่เพิ่ม = shareholders questions. mediating narrative ที่ smart คือ "agent + reskill program" — Cisco จับคู่ rollout กับ upskilling budget ไว้แล้ว, แต่ execution จะ define

Cross-reference ที่น่าสังเกต: อาทิตย์เดียวกัน **EY** ยัง run agentic audit rollout กับ 130,000 auditor (จาก brief 26-04-19-2312), **Anthropic Cowork** เผยว่า **90%+ ของ session ไม่ใช่ coding** (ก.ค.-ส.ค. 2026 data), และ **NVIDIA Nemotron 3.5 Lightning** ออกแบบเพื่อ always-on agent. Pattern converge ชัด: **agent = utility ที่ทุกคนมี**, ไม่ใช่ tool ที่ tech worker ใช้

## มุม AI Agent Platform

**Builders / framework maker:** ถ้าไม่มี **model routing** ที่ transparent + configurable + observable = framework ล้าสมัยใน 6 เดือน. คนที่ยัง lock ไปที่ single provider (Cursor lock ไป Anthropic, Copilot lock ไป OpenAI) มีความเสี่ยงถูก enterprise ถามว่า "route ได้ไหม" แล้วตอบไม่ได้ = สูญ deal. NeMo Switchyard, LiteLLM, Portkey กำลังกลายเป็น table stakes

**Users / business deployer:** ทำ **cost baseline per task class** ก่อน rollout — categorize task เป็น tier (สรุป email = $0.001, generate report = $0.05, analyze financial = $0.50) แล้ว route ตาม tier ไม่ใช่ default frontier ทุก call. ROI ของ full-frontier vs tiered-routing ต่างกัน 3-10x. สำหรับ Thai enterprise ที่จ่ายเงิน USD สำหรับ token — cost saving นี้ทวีคูณด้วย FX volatility

**Ecosystem:** **on-prem revival** — Dell, HPE, IBM, Lenovo, Supermicro ทั้งหมดได้ประโยชน์. ธุรกิจไทยที่ขาย private GPU cluster (Kirz, True IDC, Amun.tech, NTPC) มี window 12-18 เดือนที่ enterprise buyer จะเปรียบเทียบ cloud vs on-prem serious ครั้งแรก — sale motion ต้องเปลี่ยนจาก "colocation" ไป "AI-ready GPU floor" พร้อม TCO calculator สำหรับ agent workload

## Sources
- [Cisco is rolling out AI agents to every single one of its 90,000 employees (Fortune)](https://fortune.com/2026/07/01/cisco-cfo-ai-agents-finance-employees-mark-patterson/)
- [Cisco to roll out AI agents to all 90,000 employees from August 2026 (HR Katha)](https://www.hrkatha.com/news/cisco-to-roll-out-ai-agents-to-all-90000-employees-from-august-2026/)
- [Every one of Cisco's 90,000 employees now has an AI agent — CFO explains the cost (People Matters)](https://www.peoplematters.in/amp/news/ai-and-emerging-tech/every-one-of-ciscos-90000-employees-now-has-an-ai-agent-its-cfo-explains-the-cost-50638)
- [Cisco's 90,000-Employee AI Agent Rollout Could Become Enterprise AI's Biggest Trust Test (UC Today)](https://www.uctoday.com/employee-engagement-recognition/ciscos-90000-employee-ai-agent-rollout-could-become-enterprise-ais-biggest-trust-test/)
- [Cisco's AI Agent Rollout Lands the Same Month as Layoffs (CXM)](https://cxm.world/employee-experience/cisco-ai-agent-rollout-layoffs-employee-trust/)

---

## Audio script
เรื่องที่สองของเช้าวันอังคาร — Cisco เริ่ม rollout AI agent ให้พนักงานทั้ง 90,000 คน. เป็น enterprise-wide rollout ที่ใหญ่ที่สุดในรอบ AI era ของ US large-cap. จุดที่น่าสนใจสองอย่าง หนึ่ง — agent ของพนักงานแต่ละคนไม่ได้ต่อ frontier model เป็น default; ระบบ route task ไป model tier ที่เหมาะสม task ง่ายส่งไป small model, task ยากส่งไป Claude หรือ GPT frontier — ทำให้ cost per employee อยู่ที่ประมาณ 1,500 ดอลลาร์ต่อปี แทนที่จะเป็น 5,000 ถ้า default frontier ทุก call. สอง — Cisco run ส่วนใหญ่ on-premises ไม่ใช่ cloud managed เพราะคุม cost กับ data security ได้ดีกว่า. financial context ที่ต้องรู้คือ Cisco รายงาน AI-related orders 2 พันล้านดอลลาร์ใน FY25 ปรับ FY26 guidance ขึ้นเป็น 9 พันล้าน 4.5 เท่า — internal rollout 90K นี้คือ marketing asset ระดับ Chuck Robbins keynote. signal ที่ใหญ่กว่าคือ pattern การ routing กับ on-prem revival กำลังกลับมา — Dell HPE IBM Lenovo ได้ประโยชน์เต็ม ๆ. ที่ต้องระวังคือ timing paradox — rollout มาพร้อม layoff รอบใหม่เดือนเดียวกัน narrative "AI แทนคน" กำลังจะขึ้น หน้าหนึ่งของ WSJ ใน 60 วัน.
