---
date: 2026-09-25
slug: 26-09-25-0615-03-ema-ai-employees-77m-wipro
topic: use-case
sources: 4
reading_time_min: 4
image_prompt: |
  A giant open-plan enterprise office at dawn seen from above, hundreds of desks
  arranged in concentric rings around a central glowing translucent "AI EMPLOYEE"
  hologram silhouette. Three neon numbers rise vertically like columns of light:
  "240K WIPRO EMPLOYEES", "65 COUNTRIES", "2.9M QUERIES/YR". A small "$77M SERIES B"
  banner is stamped in the top-right corner. Editorial isometric cinematic style,
  cool teal plus warm amber accents, 1:1 aspect, no real human faces (silhouettes ok).
image: images/26-09-25-0615-03-ema-ai-employees-77m-wipro.png
---

# Ema ระดม $77M Series B — Wipro deploy AI Employee ถึง 240,000 คน ใน 65 ประเทศ; valuation ขึ้น 4x

## TL;DR
- **23 ก.ย. — Ema ระดม Series B $77M** — นำโดย **Creaegis** — Accel, S32, Prosus follow-on ทุกราย = **total capital ถึง $140M**, valuation ขึ้น **>4x** จากรอบก่อน
- **Wipro deployment มี hard number**: **240,000 associates ใน 65 ประเทศ, 100+ workflows, ~2.9M queries/ปี** — ไม่ใช่ pilot เล็ก ๆ แต่เป็น production ที่ครอบทั้ง HR/IT/Finance
- **Signal:** "AI Employee" thesis เปลี่ยนจาก marketing ไปเป็น deployment scale จริงในองค์กร Fortune Global 500; วางฐานให้ Salesforce Coworker + Reinventing.AI Open Source Employees (เมื่อวันจันทร์) มี playbook อ้างอิง

## เกิดอะไรขึ้น

23 กันยายน 2026 — Ema (ex-Google/Uber founders, launched 2023) ประกาศ **Series B $77M** นำโดย **Creaegis** พร้อม follow-on จาก Accel, S32, Prosus (existing backers ทุกราย add ขึ้น). Total capital raised = **$140M**, valuation ขึ้น **>4x** จากรอบก่อน (yourstory + fintech.global). CEO Surojit Chatterjee (ex-Coinbase CPO) พูดชัดว่ารอบนี้เข้ามาไม่ใช่เพื่อ product validation — validation มีแล้ว — แต่เพื่อ scale GTM + hire senior sales/CS leaders

Deployment ที่ Ema เปิดเผยในการประกาศ = **Wipro**: ระบบ Employee Assistant ที่รันบน Ema **รองรับ 240,000 associates ใน 65 ประเทศ**, ครอบ **100+ workflows** และ **handle ~2.9M queries ต่อปี**. Ema เรียก mode นี้ว่า "AI Employees" — คือ agent ที่มี persona, มี role (HR support, IT service, Finance query), มี tool access (Workday, ServiceNow, SAP), และ **รันในระดับ enterprise ทั้งองค์กร** ไม่ใช่ per-team pilot

Founder Surojit ยังเปิดเผยตัวเลข aggregate ทั้ง portfolio: customer ของ Ema รวมกัน handle **millions of interactions ต่อปี** ใน HR + IT + Finance; ARR ไม่ประกาศ แต่ Creaegis (fund ที่มาจาก Barings + Siddharth Parekh + focus Series B/growth-stage India+SEA) จะไม่ใส่ $77M ถ้า ARR ไม่ถึง **$15-25M** ที่ growth 3-4x YoY (compare ratio ตลาด SaaS series B ทั่วไป)

## ทำไมสำคัญ

หกเดือนก่อนตลาดยังถกกันว่า "AI Employee" คือ hype หรือ product category จริง. คำตอบมาเป็น hard number: **240K employees ใน 65 ประเทศ 100+ workflows** = deployment ระดับ enterprise ทั้ง organizational chart — ไม่มี consulting engagement ไหนที่จ่ายค่า workflow automation แบบเก่าให้ scale แบบนี้ได้ในราคาที่คุ้ม (traditional RPA + BPO deal สำหรับ 240K seat headcount = $50-100M/year run rate)

เทียบกับสัปดาห์เดียวก่อนที่ Reinventing.AI ปล่อย open-source AI Employees 8 role บน MIT license (24 ก.ย.) — Ema เป็นฝั่งตรงข้าม: **closed-source, enterprise-grade, deployment-first** เข้ามาโค้ดใหญ่ ๆ. ทั้งสองแนวจะอยู่ด้วยกัน — open-source สำหรับ SMB self-hosted, Ema สำหรับ Fortune 500 ที่ต้องการ compliance + SLA + governance. Signal คือ **category "AI Employee" ผ่านช่วง "จะรอดหรือไม่" แล้ว**; ปีหน้าเราจะเริ่มเห็น pricing per-AI-employee-seat เข้ามาแทน pricing per-user

การเลือก Creaegis เป็น lead น่าสนใจ — fund นี้ตั้งใจ India+SEA + growth stage — signal ว่า Ema กำลัง double down ตลาดเอเชียใต้ + เอเชียตะวันออกเฉียงใต้ ที่ HR/IT/Finance workflow มี volume สูงและ labor arbitrage อยู่ใกล้จุดพลิก (Filipino/Indian shared service center ที่รัน HR/IT ให้ Global 2000 เดิม)

## มุม AI Agent Platform

**Builders** — AI Employee ไม่ได้ต้องการ new framework แต่ต้องการ **role modeling + org-chart-aware permission + audit trail** ที่ enterprise IT ยอมรับ; framework layer (LangGraph, CrewAI, Anthropic SDK) เป็น commodity, **role/policy layer คือ moat**. **Users/business** ในไทย — company ที่ใช้ Wipro/Accenture/Cognizant เป็น shared service สำหรับ HR/IT ต้อง reopen contract; ROI ของ Ema-class deployment ไม่ชัดว่าจะแทน BPO ทั้งชุด แต่ **shrink deal size ลง 30-50%** เป็นสถานการณ์ที่ realistic ใน 12-18 เดือน. **Ecosystem** — Wipro เอง (customer ของ Ema) กำลัง cannibalize service ตัวเอง = signal ว่า IT services เอาต์ซอร์สแบบเก่าจะเปลี่ยนโครง; Enabridge platform ที่ position เป็น "agent orchestration + governance" มี window เข้าคุยกับกลุ่มนี้แน่นอน

## Sources

- [Ema raises $77M in funding to deploy AI employees across enterprise HR, IT and finance departments — SiliconANGLE](https://siliconangle.com/2026/09/23/ema-raises-77m-in-funding-to-deploy-ai-employees-across-enterprise-hr-it-and-finance-departments/)
- [Ema Raises $77M Series B to Scale AI Employees — Ema blog](https://www.ema.ai/blog/funding-announcement/ema-raises-series-b)
- [Ema secures $77m Series B to scale AI Employees — Fintech Global](https://fintech.global/2026/09/23/ema-secures-77m-series-b-to-scale-ai-employees/)
- [Enterprise AI startup Ema raises $77M in Series B round led by Creaegis — YourStory](https://yourstory.com/2026/09/enterprise-ai-startup-ema-raises-series-b-round-led-by-creaegis)

---

## Audio script

Ema ปิด Series B 77 ล้าน US ประกาศ 23 กันยา นำโดย Creaegis จาก Barings ส่วน existing backer Accel S32 Prosus follow on ทุกราย total capital ตอนนี้ 140 ล้าน valuation ขึ้นมากกว่า 4 เท่าจากรอบก่อน สิ่งที่ทำให้รอบนี้พิเศษไม่ใช่ตัวเลขระดมทุน แต่คือ deployment ที่ Ema เปิดเผยพร้อมกัน Wipro บริษัท IT services ยักษ์ของอินเดีย ใช้ Ema สร้าง Employee Assistant ที่รองรับ 240 000 associates ใน 65 ประเทศ ครอบ 100 workflows handle 2 900 000 queries ต่อปี ไม่ใช่ pilot แต่คือ production ทั้ง organizational chart หกเดือนก่อนตลาดยังถกกันว่า AI Employee เป็น hype หรือ category จริง ตัวเลขนี้ปิดคำถามนั้น สำหรับทีมไทยที่ใช้ Wipro Accenture หรือ Cognizant เป็น shared service สำหรับ HR IT เตรียม reopen contract ได้เลย ROI ของ Ema class deployment ไม่ชัดว่าจะแทน BPO ทั้งชุด แต่ shrink deal size ลง 30 ถึง 50 เปอร์เซ็นต์ในหนึ่งปีครึ่งเป็น scenario ที่ realistic Wipro cannibalize service ตัวเองด้วย signal ชัดว่า IT services outsource แบบเก่าจะเปลี่ยนโครง Enabridge ที่ position เป็น agent orchestration กับ governance มี window เข้าคุยกับกลุ่มนี้แน่นอน
