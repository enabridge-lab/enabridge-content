---
date: 2026-11-10
slug: bay-ai-50m-agent-security
topic: use-case
reading_time_min: 4
sources: 2
image_prompt: |
  Editorial isometric illustration of a futuristic lighthouse projecting a
  scanning beam across a harbor of laptops and cloud servers. The beam reads
  "VET EACH ACTION BEFORE IT RUNS". In the water, three ships labeled
  "MICRON", "WIX", "PELOTON" sail safely past a rejected pirate ship tagged
  "RISKY AGENT ACTION — BLOCKED". A floating banner reads "$50M — FALSE
  POSITIVES UNDER 1%". Navy, warm teal, and amber accent palette; clean
  vector style; crisp typography readable at 200px thumbnail. 1:1 aspect, no
  real human faces.
image: images/26-11-11-0604-03-bay-ai-50m-agent-security.png
---

# Bay AI เปิดตัวพร้อม $50M — ตรวจทุก action ของ agent ก่อนรันจริง, Fortune 100 ขยาย autonomous agent 3 เท่าใน 30 วัน

## TL;DR
- Bay AI (Tel Aviv) เปิดตัววันที่ 10 พ.ย. ด้วย **$50M** — Battery Ventures นำ $37M Series A, YL Ventures + Striker VP นำ $13M seed, มี Wiz CEO Assaf Rappaport ร่วมลงด้วย
- Launch customer ได้แก่ **Micron Technology, Wix.com, ClickUp, Peloton** และ Fortune 100 ลูกค้ารายงานว่า**ใช้ autonomous agent เพิ่มสามเท่าภายใน 30 วัน**หลัง deploy Bay
- Install ผ่าน MDM/EDR ที่มีอยู่แล้ว **ไม่ถึง 5 นาที** — false positive rate รายงานที่**ต่ำกว่า 1%**

## เกิดอะไรขึ้น
Yuval Zacharia (CEO), Aner Morag (CPO) และ Boris Danilovich (VP R&D) — สามอดีต Unit 8200 — เปิดตัว Bay AI พร้อมกันกับ $50M ครอบคลุม seed + Series A. ผลิตภัณฑ์คือ security layer สำหรับ AI agent ที่รันบน laptop พนักงาน, cloud workload และ SaaS app ภายใต้ policy เดียวกันทั้งหมด

สถาปัตยกรรมมีสามชิ้น: **Wave** เป็น scanner inventory agent + extension + local model บนเครื่อง; **Bay Enforcer** เป็น static binary ที่ hook เข้าระบบ แล้วรับ proposed action ของ agent มา evaluate ด้วย context ของ session ทั้งก้อน — ตอบ verdict ภายใน millisecond, action ที่เสี่ยงไม่ถูกรันเลย ผู้ใช้อาจถูกถามให้ approve เป็นขั้น ๆ; **Lighthouse** draft policy เฉพาะทีมจาก activity 30 วันหลัง แล้วให้ทดสอบ policy ใหม่ย้อนกับข้อมูลเดือนก่อน

สิ่งที่น่าสนใจคือ scale ของลูกค้า — ภายในเก้าเดือนก่อนเปิดตัว Bay signed ลูกค้า enterprise หลายสิบราย รวมถึง Micron, Wix, ClickUp, Peloton. และ claim ที่ specific มากคือ "Fortune 100 customers tripled their use of autonomous agents in just under 30 days" หลัง deploy — แปลว่าปัญหาที่ Bay แก้ไม่ใช่แค่ security แต่คือ **confidence to let agents actually run**. ส่วน revenue ยังไม่เปิดเผย

## ทำไมสำคัญ
ประเด็นสำคัญไม่ใช่ว่าตลาด agent security เกิดขึ้นแล้ว — Lasso, Lakera, HiddenLayer, Noma มีกันก่อนหน้านี้ — แต่คือ **thesis ที่ Bay ใช้ขาย**: ถ้า enterprise อยากให้ agent มี autonomy จริง (ไม่ใช่แค่ chatbot ที่สรุปข้อมูล) องค์กรต้องมี runtime enforcement ที่ตัดสินใจทีละ action — ไม่ใช่แค่ filter input/output ของ model

ข้อมูลที่ส่งสัญญาณแรงคือตัวเลข "tripled autonomous agent use within 30 days". ถ้าเชื่อ claim นี้ แปลว่าใน enterprise ที่ Bay เข้าไป deploy agent ที่ "sit idle" ไว้ก่อนด้วยกลัวความเสี่ยง — ถูกปลดล็อคให้รันจริง. Agent platform ที่ deploy แล้วไม่มีใครกล้าใช้คือ asset ตายซาก — layer แบบ Bay ทำให้มัน generate value ได้ ซึ่งแปลว่า agent security คือ **enabler ของ agent ROI** ไม่ใช่แค่ cost center

การที่ CrowdStrike เพิ่งซื้อ Fiddler AI กับ Dreadnode ไปในราคาประมาณ $495M ไม่กี่วันก่อน และ Palo Alto Networks ก็เข้าคุย Clutch Security ที่ประมาณ $500M — ตลาด agent security consolidation เริ่มแล้ว. Bay ที่เพิ่งออกมา Fresh จะโดนแรงกดดันเลือกระหว่างสร้าง independent brand หรือ exit เร็ว

## มุม AI Agent Platform
- **Builders**: ถ้าออกแบบ agent framework ที่มี tool-use / computer-use หนัก ๆ ต้องคิดถึง integration กับ enforcement layer แบบนี้ — API ที่ให้ framework ส่ง proposed action ไป pre-check ได้ก่อนรัน จะกลายเป็น requirement ของ enterprise sale. ตอนนี้ยังเป็นโอกาส differentiate ตัวเอง
- **Users / business**: ตัวเลข "tripled agent use in 30 days" คือ pattern ที่เห็นได้ชัด — เหตุผลใหญ่ที่ agent pilot ไม่ scale คือ security + governance ไม่พร้อม. ก่อน deploy agent ใหม่ รีวิว control plane ให้พร้อมก่อน. ตัวเลือก: Bay, Lasso, Lakera, HiddenLayer, Noma — เลือกให้ตรงกับ stack ที่มี
- **Ecosystem**: Battery Ventures, YL Ventures, และ Wiz CEO ลงพร้อมกันบอกว่าตลาดนี้ highly backed. Legacy EDR vendor (CrowdStrike, SentinelOne, Palo Alto) จะต้องทำตัวเลือก — ซื้อ, สร้าง, หรือ partner. Hyperscaler (AWS, Azure, Google) จะต้องตัดสินใจว่าจะ bundle runtime security เข้าไปใน agent platform ของตัวเองหรือเปิดให้ third party

## Sources
- [AI security startup Bay launches with $50M to vet agent actions before they run (SiliconANGLE, 10 พ.ย. 2026)](https://siliconangle.com/2026/11/10/ai-security-startup-bay-launches-with-50m-to-vet-agent-actions-before-they-run/)
- [AI Agents News Brief: November 8, 2026 (AI Agents Directory)](https://aiagentsdirectory.com/news/ai-agents-news-brief-november-8-2026)

---

## Audio script
Bay AI สตาร์ทอัพความมั่นคงจาก Tel Aviv เปิดตัวพร้อมกันกับเงินห้าสิบล้านดอลลาร์. Battery Ventures นำสามสิบเจ็ดล้านใน Series A บวก seed อีกสิบสามล้านจาก YL Ventures กับ Striker ซึ่งมี CEO ของ Wiz ร่วมลงด้วย. ผู้ก่อตั้งสามคนเคยอยู่หน่วยไซเบอร์แปดสองศูนย์ของกองทัพอิสราเอล. ผลิตภัณฑ์ติดตั้งบนเครื่องพนักงานกับ cloud กับ SaaS ผ่าน MDM หรือ EDR ที่มีอยู่แล้ว ใช้เวลาไม่ถึงห้านาที. วิธีทำงานคือ Bay Enforcer จะ hook เข้าระบบ แล้วตรวจทุก action ที่ agent ขอรันก่อน — verdict ภายในมิลลิวินาที, false positive rate ต่ำกว่าหนึ่งเปอร์เซ็นต์. Lighthouse สร้าง policy ให้เฉพาะทีม จาก activity ของเดือนก่อน. ลูกค้าเริ่มต้นได้แก่ Micron, Wix, ClickUp, Peloton. ตัวเลขที่น่าสนใจที่สุด — ลูกค้า Fortune 100 ที่ใช้ Bay รายงานว่าขยายการใช้ autonomous agent เพิ่มสามเท่าภายในสามสิบวัน. ข้อความคือ security layer ไม่ใช่ cost center — มันคือ enabler ของ agent ROI เพราะปลดล็อคให้องค์กรกล้าให้ agent รันจริง. ตลาดนี้กำลังหวานเพราะเพิ่งมีดีล CrowdStrike ซื้อ Fiddler และ Palo Alto คุย Clutch. ถ้ากำลัง deploy agent ใน workflow ควรรีวิว control plane ก่อน scale
