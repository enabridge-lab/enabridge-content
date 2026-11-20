---
date: 2026-11-14
slug: att-500-workflows-45b-tokens
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a vast telecom operations center
  with glowing racks of servers. In the foreground a massive scoreboard
  reads "500 WORKFLOWS", "45,000,000,000 TOKENS / DAY", "1,000,000 TX /
  MONTH". A single human silhouette stands at a review station marked
  "HUMAN GATE" between the agent swarm and a line labeled "PRODUCTION".
  A banner at the top reads "AT&T · AGENT FOUNDRY · 2026". Soft turquoise
  and warm orange palette, 1:1 aspect, no real human faces, high contrast
  so numbers stay readable at 200px thumbnail size.
image: images/26-11-21-0604-04-att-500-workflows-45b-tokens.png
---

# AT&T พิมพ์ตัวเลขที่ enterprise agent รอมานาน — 500 workflow ใน production, 45 พันล้าน token/วัน, human gate ทุกตัว

## TL;DR
- AT&T ยืนยันที่งาน AWS re:Invent Boston: 500 agentic workflow ใน production, target ทะลุ 1,500 ภายในปี 2027
- Platform handle >1 ล้าน transaction/เดือน และใช้ ~45 พันล้าน AI token/วัน
- Architecture = agent น้อย + business logic แยกส่วน — **ไม่ใช่** หลายพัน specialized agent
- Human review กำกับทุก workflow จนกว่า accuracy จะถึงช่วง high-90% แล้วจึง autonomous
- Exec อ้าง 5x ROI ภายในปีแรกของ production AI investment

## เกิดอะไรขึ้น
วันที่ 14 พฤศจิกายน Luke Corbin ผู้บริหารจาก AT&T Business ขึ้นเวทีที่งาน AWS Boston ยืนยันตัวเลขที่วงการ enterprise AI พยายามหาทั้งปี — **500 agentic workflow ที่อยู่ใน production จริง** รัน business process ของ AT&T, target คือ **1,500 workflow ภายในปี 2027** หรือประมาณ 3x ภายใน 13 เดือน

ตัวเลขที่น่าสนใจกว่านั้นคือ volume — platform handle มากกว่า **1 ล้าน transaction ต่อเดือน** และบริโภค **45 พันล้าน AI token ต่อวัน** 45B tokens/day = ~1,350 พันล้าน token/เดือน = scale ที่เทียบได้กับ OpenAI หรือ Anthropic ขั้นต้นของ customer tier enterprise ที่ใหญ่ที่สุด ตัวเลขนี้ไม่ใช่ pilot — เป็น production infrastructure spending ระดับ hyperscaler consumer

**Architecture** ที่ Corbin อธิบายเป็นสิ่งที่ counterintuitive — AT&T **ไม่** build หลายพัน specialized agent (แบบที่ IBM + Microsoft Imagine Enterprise pitching) แต่กลับ maintain agent **จำนวนน้อย** ที่ execute workflow ผ่าน **business logic ที่จัดการแบบ centralized** — คล้าย microservice pattern ที่ agent เป็น compute layer แต่ business rule อยู่ใน config layer แยกต่างหาก การ architect แบบนี้ทำให้ debugging ง่ายกว่า scale ง่ายกว่า และปรับ compliance ง่ายกว่าตอน audit

**Human-in-the-loop policy** ก็สำคัญ — AT&T ไม่ปล่อย agent ให้ autonomous ตั้งแต่ day one ทุก workflow เริ่มด้วย human review gate human จะดู output agent ทุกครั้งจนกว่า accuracy จะถึงช่วง mid-to-high 90% (บริษัทไม่เปิดสูตรวัด) แล้วค่อย graduate ขึ้นเป็น autonomous แปลว่า 500 workflow ที่ Corbin อ้างว่าอยู่ใน production ไม่ใช่ทั้งหมดที่ autonomous — บางส่วนยังมี human gate อยู่

สุดท้าย Corbin อ้างว่า AI investment ของ AT&T ให้ **5x ROI ภายในปีแรก** โดยไม่เปิดเผยตัวเลข cost saved หรือ revenue gained ที่ specific

## ทำไมสำคัญ
สัปดาห์นี้มีสองข่าว enterprise agent ที่ส่งสัญญาณคนละทิศ — **IBM + Microsoft Imagine Enterprise** (ประกาศ 10 พฤศจิกายน) seeding platform ด้วย 6,000 prebuilt agent ส่วน **AT&T** ยืนยันว่าตัวเองสร้าง 500 workflow ที่ custom ของตัวเอง ด้วย agent จำนวน น้อยมาก ทั้งสอง camp เถียงกันเรื่อง **"agent-as-catalog" vs "agent-as-compute"**

Camp IBM/Microsoft เชื่อว่า agent = SKU จำนวนมาก enterprise ซื้อ catalog + customize Camp AT&T เชื่อว่า agent = compute primitive จำนวนน้อย + logic แยกส่วน enterprise build workflow เองเพราะเข้าใจ domain ดีกว่า vendor ใด ๆ แต่ละ model ถูก case ต่างกัน — AT&T มี internal engineering team ขนาดใหญ่กับ domain ที่เฉพาะ (telecom, network ops, billing) ส่วนบริษัทเล็กกว่าที่ไม่มี engineering bandwidth การซื้อ prebuilt catalog อาจ reasonable

อีกส่วนที่สำคัญคือ **governance template** — การที่ AT&T ยอมเปิด human gate ก่อน autonomous เป็นสิ่งที่ enterprise CIO ควรเขียนเป็น mandatory pattern ไม่ใช่ optional ปี 2027 ที่หลาย vendor กำลัง pitch "autonomous agent from day one" (Claude Duet, ChatGPT Dots, Agentforce) จะเริ่มเห็น enterprise กลับไป mandate human-in-the-loop มากขึ้นหลัง incident แรกที่ blow up

Caveat สำคัญ — ทุกตัวเลขมาจาก AT&T เอง, ไม่มี auditor ภายนอก, "workflow" ไม่ได้ define ชัดเจน — 1 workflow = 1 task? หรือ 1 department? หรือ 1 integration point? เป็นคำถามเปิด นักวิเคราะห์ ซึ่งรวมถึงบทความใน The New Stack และ Byteiota ชี้ว่าตัวเลข 500 workflow "nearly" อาจรวม workflow ที่ยัง human-gated ทั้งหมด — ถ้าแยกเฉพาะที่ autonomous ตัวเลขอาจเหลือครึ่งหรือน้อยกว่า

## มุม AI Agent Platform
**Builders** — architecture pattern "few agents + centralized business logic" ของ AT&T เป็น blueprint ที่คุ้มคัดลอก หลายทีมที่ build agent platform ปัจจุบันตกหลุม **agent explosion** — สร้าง specialized agent หลายสิบตัวแล้วจัดการไม่ไหว pattern ที่ work ใน scale คือ **few, powerful, orchestrated** agent + rules engine ที่แยก deployable จาก agent code

**Users/business** — ถ้าคุณกำลัง pitch agent project ให้ CFO ตัวเลขที่ควรเน้นไม่ใช่ "AI จะทำอะไรได้" แต่คือ **governance posture** + **ROI timeline** AT&T อ้าง 5x ROI ปีแรก = ตั้งความคาดหวังที่ realistic (ไม่ใช่ 50x ที่ vendor pitch) และ **human gate until accuracy >90%** เป็น risk-management stance ที่ CFO เข้าใจง่าย Enabridge ที่ build agent platform ให้ลูกค้าไทยควรมี template "graduate from human-in-the-loop" เป็น built-in process ไม่ใช่ feature addon

**Ecosystem** — ตัวเลข 45B tokens/day จาก AT&T ตัวเดียว ≈ workload ของ AWS/Azure/GCP ชั้น top-tier ของ inference load ทั้งปี 2024 ที่ hyperscaler report ซึ่งแปลว่า **compute capacity สำหรับ agent** จะเป็น bottleneck จริงของปี 2027 ไม่ใช่ model quality — ถ้า AT&T หนึ่งรายใช้ขนาดนี้ Fortune 500 อีก 499 บริษัทที่ตามมาจะเจอ **GPU scarcity + inference price inflation** แน่ cloud provider ที่ secure capacity ล่วงหน้าจะชนะ

## Sources
- [AT&T uses agentic AI to reinvent business processes from the ground up (SiliconANGLE)](https://siliconangle.com/2026/11/14/att-uses-agentic-ai-to-reinvent-business-processes-from-the-ground-up/)
- [AT&T Keeps Human Review on Nearly 500 AI Workflows (Beri.net)](https://www.beri.net/article/att-500-agentic-workflows-business-agent-foundry-human-oversight-high-90s-accuracy-threshold-45-billion-tokens-ai-gateway-open-models)
- [AT&T: 500 AI Agent Workflows, 45 Billion Tokens Per Day (Byteiota)](https://byteiota.com/att-agentic-workflows-45-billion-tokens/)
- [AT&T Plans to Triple Production Agentic Workflows in 2027 (TokenPost)](https://www.tokenpost.com/news/business/57497)

---

## Audio script
AT&T เพิ่งพิมพ์ตัวเลขที่ตลาด enterprise agent รอมาทั้งปี ที่งาน AWS Boston วันที่ 14 พฤศจิกายน Luke Corbin ผู้บริหาร AT&T Business ยืนยันว่าบริษัทมี agentic workflow ห้าร้อย workflow อยู่ใน production รัน business process ของบริษัทจริง ตั้ง target ว่าจะทะลุหนึ่งพันห้าร้อย workflow ภายในปี 2027 หรือสามเท่าภายในสิบสามเดือน platform handle มากกว่าหนึ่งล้าน transaction ต่อเดือน และบริโภค AI token สี่สิบห้าพันล้าน token ต่อวัน ซึ่งเป็น scale ที่เทียบได้กับลูกค้าชั้น top tier ของ hyperscaler ตัวเลขนี้ไม่ใช่ pilot แต่เป็น production infrastructure spending ระดับใหญ่ สิ่งที่น่าสนใจคือ architecture ที่ counterintuitive AT&T ไม่ build specialized agent หลายพันตัวแบบที่ IBM Microsoft Imagine Enterprise pitch แต่ maintain agent จำนวนน้อย ที่ execute workflow ผ่าน business logic ที่จัดการแบบ centralized คล้าย microservice pattern ที่ agent เป็น compute layer แต่ business rule อยู่ใน config layer แยกต่างหาก ทำให้ debug ง่าย scale ง่าย audit ง่าย อีกจุดสำคัญคือ human-in-the-loop policy ทุก workflow เริ่มด้วย human review gate human ดู output agent ทุกครั้งจนกว่า accuracy จะถึง mid-to-high 90 เปอร์เซ็นต์ แล้วค่อยปล่อย autonomous สำหรับ builder blueprint นี้คุ้มคัดลอก few powerful orchestrated agent บวก rules engine แยก deployable สำหรับ CFO ตัวเลข 5x ROI ปีแรกเป็นความคาดหวังที่ realistic human gate until ninety percent accuracy เป็น risk management stance ที่เข้าใจง่าย caveat คือทุกตัวเลขมาจากบริษัทเอง workflow ยังไม่ define ชัด อาจรวม workflow ที่ยัง human gated ทั้งหมด
