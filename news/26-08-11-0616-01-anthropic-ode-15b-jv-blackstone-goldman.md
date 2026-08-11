---
date: 2026-08-10
slug: anthropic-ode-15b-jv-blackstone-goldman
topic: use-case
reading_time_min: 4
sources: 3
image_prompt: |
  A grand marble bank lobby with a small "Ode" plaque above the entrance;
  three stacked deal cards on the counter read "$1.5B RAISED", "100 ENGINEERS",
  "BANKS · HOSPITALS · MANUFACTURERS". Behind the counter, an oversized Anthropic
  A logo glows next to Blackstone and Goldman Sachs monograms. Editorial isometric
  style, deep navy and gold palette, 1:1 aspect, no real human faces.
image: images/26-08-11-0616-01-anthropic-ode-15b-jv-blackstone-goldman.png
---

# Anthropic เปิด "Ode" — JV $1.5B กับ Blackstone/Goldman ส่งวิศวกร 100 คนฝัง Claude ในแบงก์กับโรงพยาบาล

## TL;DR
- Anthropic + Blackstone + Hellman & Friedman ลงคนละ ~$300M, Goldman Sachs +$150M รวม $1.5B ตั้ง "Ode with Anthropic" — บริษัทลูก services ที่ส่งวิศวกร AI 100 คนไปฝังในลูกค้า mid-market
- Target: community banks, regional health systems, mid-sized manufacturers — segment ที่อยากใช้ Claude แต่ไม่มีทีม engineering ของตัวเอง
- ต่อยอดจากการซื้อ Fractional AI เดือน May, CEO/CTO เดิมของ Fractional (Chris Taylor, Eddie Siegel) รัน Ode ต่อ

## เกิดอะไรขึ้น
วันเสาร์ที่ 8 สิงหาคม Anthropic ประกาศ Ode with Anthropic — joint venture $1.5B ที่ต่างจากดีลปกติของ frontier lab ตรงที่มันไม่ใช่การขาย API หรือขาย seat license แต่เป็นการ**ตั้งบริษัท services ขึ้นมาเอง** เพื่อเข้าไปทำโปรเจกต์ให้ลูกค้าถึงในออฟฟิศ Anthropic, Blackstone, และ Hellman & Friedman แต่ละเจ้าลงเงินราว $300M เป็น anchor พร้อม Goldman Sachs อีก ~$150M — เหลืออีก ~$450M มาจาก General Atlantic, Apollo, GIC, และ Sequoia

โครงสร้างของ Ode ตรงไปตรงมา: มีวิศวกร 100 คน (ส่วนใหญ่มาจาก Fractional AI ที่ Anthropic ซื้อเดือน May) รับงานเข้าไปฝังกับลูกค้าแบบ SWAT team ทำโปรเจกต์ agent ที่ specific — จาก loan underwriting ใน community bank ไปถึง discharge planning ใน regional hospital ไปถึง production scheduling ใน mid-sized factory Chris Taylor ที่เคยเป็น CEO ของ Fractional ขึ้นเป็น CEO ของ Ode, Eddie Siegel เป็น CTO

Segment ที่ Ode ล็อกไว้ก็คือ segment ที่ทั้ง Accenture, McKinsey Digital, Deloitte, และ EY ปล่อยผ่านมานาน — องค์กรที่ใหญ่พอมีเงินจ่าย consulting ($5M+/ปี) แต่ไม่ใหญ่พอที่จะจ้าง Big Four ที่คิดค่า partner rate $2,000/ชั่วโมงได้จริง Ode เอา Claude เข้าไปพร้อมทีมวิศวกร แล้วเก็บค่าโปรเจกต์แบบ outcome-based — ต่างจาก consultancy เดิมที่คิด time-and-materials

## ทำไมสำคัญ
ดีลนี้เป็น**ครั้งแรก**ที่ frontier lab เดินเข้ามาแข่งใน services layer เอง — ไม่ใช่ผ่าน partner ecosystem แบบ Google/AWS ที่ปล่อยให้ Accenture, TCS, Infosys รับงาน implementation ต่อ Anthropic ตัดสินใจว่าถ้าจะเจาะ mid-market ที่ไม่มี in-house engineering ต้องส่งคนของตัวเองไปทำ ไม่งั้น Claude จะจบแค่ chatbot experiment แล้วถูก churn ใน 6 เดือน

Signal ที่ตามมาชัด: Blackstone ($1T AUM) กับ Hellman & Friedman ($90B AUM) ไม่ใช่ VC — พวกเขาเป็น PE firm ที่ portfolio company หลายพันแห่ง**คือ mid-market บริษัทที่ Ode จะไปขาย** ดีลนี้จึงเป็น distribution moat ในตัวมันเอง — Ode มีลูกค้าปลาย warm ให้เข้าถึงทันที ไม่ต้อง cold outbound แข่งกับ Salesforce/ServiceNow ที่มี salesforce หลายหมื่นคนอยู่ตลาดเดียวกัน

จังหวะน่าสนใจ: OpenAI มี ChatGPT Enterprise + สตูดิโอ agent, Google มี Gemini Enterprise + Google Cloud Professional Services, Microsoft มี Azure + Copilot + accenture Alliance — Anthropic ไม่มีขาซ้ายและขวานี้ Ode จึงเป็นการ**สร้าง GTM ที่ Google/Microsoft ไม่มี** เพราะพวกเขาเป็น cloud provider ที่แข่งกับ SI partner ตัวเองไม่ได้ Anthropic ไม่มี cloud ไม่มี partner conflict — เดินเข้าไปทำเองได้เต็มตัว

## มุม AI Agent Platform
สำหรับ **builders** ที่กำลังทำ agent framework/orchestration: Ode คือ signal ว่าปีนี้ตลาดจะแยกเป็นสองชั้นชัดขึ้น — chinook OSS/self-serve tools สำหรับ developer และ managed white-glove services สำหรับ business ที่ยอมจ่าย $2M+ ต่อโปรเจกต์เพื่อไม่ต้องคิด Framework ไหนไม่มี "top-of-funnel" ผ่าน services partner จะโตช้าลง สำหรับ **users/business** ที่ deploy agent: Ode เปิดช่องให้ mid-market เข้าถึง Claude ไม่ต้องผ่าน consulting กลางระหว่าง ($400-500/hour) — คาดว่า pricing model ของ Ode จะเป็น outcome-based ($X ต่อ loan approved, $Y ต่อ discharge processed) ซึ่งจะกดดันให้ Big Four ต้องปรับ pricing structure ตาม

สำหรับ **ecosystem/vendor**: Accenture, TCS, IBM Consulting, Deloitte AI & Data ตอนนี้มี frontier competitor ที่มาพร้อม model + วิศวกร + capital $1.5B — และไม่ต้องขายชั่วโมง Salesforce/ServiceNow ก็ควรจับตา เพราะ Ode ไม่ได้ขาย platform แต่ขาย agent-that-works-day-1 ซึ่งอาจ bypass การซื้อ Agentforce หรือ Now Assist ไปเลยในลูกค้า mid-market ที่ Claude ทำงานให้แล้ว

## Sources
- [Anthropic Launches "Ode With Anthropic" — $1.5B JV With Blackstone and H&F](https://aitoolsrecap.com/Blog/anthropic-ode-with-anthropic-jv-blackstone-2026)
- [Anthropic, Blackstone launch $1.5B Ode enterprise services firm](https://aiweekly.co/alerts/anthropic-blackstone-launch-15b-ode-enterprise-services-firm)
- [Anthropic's $1.5B Enterprise JV: 6 Things You Need to Know](https://www.mindstudio.ai/blog/anthropic-1-5b-enterprise-jv-blackstone-goldman-sachs)

---

## Audio script
Anthropic เพิ่งประกาศดีลที่แปลกมากครับ ตั้งบริษัทลูกชื่อ Ode with Anthropic ระดมทุน 1.5 พันล้านเหรียญ ร่วมกับ Blackstone Hellman & Friedman และ Goldman Sachs สิ่งที่แปลกคือมันไม่ใช่ product launch แต่เป็น services company — ส่งวิศวกร 100 คนเข้าไปฝังในลูกค้าเลย target คือ community bank โรงพยาบาลระดับภูมิภาค กับโรงงานขนาดกลาง ซึ่งเป็น segment ที่มีเงินจ่าย consulting แต่ไม่ใหญ่พอจะดึง Big Four มาทำ ทำไมมันสำคัญ Anthropic ตัดสินใจว่าถ้าจะให้ Claude ไปอยู่ในธุรกิจจริง ไม่ใช่แค่ chatbot ต้องส่งคนของตัวเองไปทำ ที่น่าสนใจไปกว่านั้นคือ Blackstone มี portfolio company หลายพันแห่งที่เป็น mid-market — แปลว่า Ode มีลูกค้า warm รอเข้าอยู่แล้ว ไม่ต้อง cold outbound แข่งกับ Salesforce สำหรับคนที่ทำ AI Agent Platform นี่คือสัญญาณว่าตลาดจะแยกเป็นสองชั้นชัดขึ้น — DIY tools สำหรับ dev กับ managed services สำหรับ business และ Accenture Deloitte IBM Consulting ตอนนี้มีคู่แข่งที่มาพร้อม model วิศวกร แล้วก็ทุน 1.5 พันล้านครับ
