---
date: 2026-10-19
slug: cognizant-google-gemini-frontier
topic: use-case
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial illustration of a modern enterprise office floor viewed in cross-section,
  with four stacked bands: top band labeled "18,000 ASSOCIATES" (small silhouettes
  packed in rows), second band labeled "55,000 TRAINED", third labeled "100K BY 2026",
  bottom labeled "200K GOAL". A giant Gemini-style gradient diamond anchors the right
  side, with lines flowing from each band into the diamond. A Cognizant blue ribbon
  wraps the lower edge. Clean editorial infographic style, blue and sunrise orange
  palette, strong contrast for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-22-0605-03-cognizant-google-gemini-frontier.png
---

# Cognizant ตั้ง Gemini Frontier Capability Group 18,000 คน — services firm ขยับจาก SI ไปเป็น "agent operator"

## TL;DR
- **19 ต.ค.** Cognizant ประกาศขยาย partnership กับ Google Cloud, ตั้ง **Gemini Frontier Capability Group** รวม **18,000+ associate** ที่โฟกัสขาย + deploy Gemini agent solution ให้ enterprise client
- Scale targets ที่ Cognizant โฆษณา: **55,000 associate** ผ่าน "Build with Gemini" workshop แล้ว, **100,000 ลงปี 2026**, เป้า **200,000 คน** รวม
- ต่อยอดจาก Oct 2025 ที่เคย commit strategic investment ใน Gemini Enterprise + Feb 2026 ที่เปิด **Gemini Enterprise Center of Excellence** + Agent Development Lifecycle (ADLC) framework
- Signal: services firm ขนาดใหญ่ (Accenture, TCS, Infosys, Wipro, Deloitte, Cognizant) กำลัง **re-skill labor pool เป็น "agent operator"** — ตลาด service revenue ย้ายจาก IT integration ไป agent lifecycle management

## เกิดอะไรขึ้น

วันจันทร์ที่ **19 ต.ค.** Cognizant ประกาศ expansion ของ Google Cloud partnership — ตั้ง **Gemini Frontier Capability Group** ที่ Cognizant เรียกว่า "แกนกลางของการ operationalize agentic AI ให้ enterprise scale". กลุ่มนี้มี **มากกว่า 18,000 associate** (ขณะ Cognizant มีพนักงานประมาณ 350,000 คนทั่วโลก) ที่จะทำงานเฉพาะ Gemini solution — ตั้งแต่ pre-sales, agent design, deployment, run, และ post-deployment optimization. โครงสร้างสามชั้นหลัก: **sales/consulting layer** (ช่วยลูกค้า map use case), **agent engineering layer** (ใช้ Google ADK + Vertex AI Agent Builder สร้างและ fine-tune agent), และ **operations layer** (monitor, retrain, scale)

ตัวเลขที่ Cognizant โฆษณาเพื่อแสดง pipeline ของ talent: **55,000 associate** ผ่าน workshop "Build with Gemini" แล้ว (เริ่มตั้งแต่ ม.ค. 2026), เป้าหมาย **100,000** ลงปลายปี 2026, และ **"long-term goal"** 200,000 คน — คือเกือบ 60% ของพนักงานทั้งบริษัท. CEO Ravi Kumar S. ให้ comment ว่า partnership expansion นี้คือ "เร่งการ shift จาก engagement แบบ project-based ไปเป็น outcome-based service ที่ scale ด้วย agent". ตัวเลข workshop นี้มาจาก Cognizant ล้วน ไม่มี third-party ตรวจ จึงอยู่ในหมวด "บริษัทอ้าง"

Partnership นี้ไม่ใช่ของใหม่ — มี 3 phase ชัดเจน: **ต.ค. 2025** Cognizant ประกาศ strategic investment ใน Gemini Enterprise + Neuro AI + Agent Foundry; **ก.พ. 2026** เปิด **Gemini Enterprise Center of Excellence** + commit framework ที่เรียกว่า **Agent Development Lifecycle (ADLC)**; รอบ **ต.ค. 2026** นี้คือ phase 3 — scale labor pool. Market reaction: Cognizant stock บวกเล็กน้อย 1.4% ในวันประกาศ, Google Cloud ไม่ comment ตัวเลข revenue

## ทำไมสำคัญ

Pattern ที่สำคัญคือ **services firm กำลัง re-skill labor pool เป็น "agent operator"** — ไม่ใช่แค่ขาย GenAI consulting. Accenture ประกาศ 80,000 Agent Builder ไปแล้วเดือน ก.ค., TCS กำลัง train 100,000 คนบน Microsoft Copilot Studio, Infosys ตั้ง Topaz Agent Hub, Deloitte มี Zora AI. **ทั้ง 6 บริษัทกำลังขยับไปที่ตลาดเดียวกัน**: การเป็น "run" partner ของ agent fleet ใน enterprise. ธุรกิจ IT services เดิมที่ขายคน-ชั่วโมง เขียน code + integration กำลังเปลี่ยนเป็นขาย **agent lifecycle management** ที่ metric คือ outcome (claim processed, lead converted, ticket resolved) ไม่ใช่ staff hour

ประเด็นที่น่า probe: ขณะที่ 18,000 คนฟังดูเยอะ, **ความ productive ของ agent operator ยังพิสูจน์ไม่ได้ว่า scale ดีกว่า developer เดิม**. ตัวเลข 55,000 workshop graduate ก็เป็น **training throughput** ไม่ใช่ **production deployment throughput**. McKinsey report เดือน ก.ย. ยัง flag ว่าในฟังก์ชัน business ใด ๆ ก็ตาม มีแค่ **ไม่เกิน 10% ของบริษัท** ที่ scale agent ได้จริงใน production. ถ้า Cognizant จะ scale ได้ตามเป้าต้อง solve **unit economics ของ agent operator** ให้แสดงให้ลูกค้าเห็นว่า agent 10 ตัว + 1 คน manage ถูกกว่า developer 10 คน — ซึ่งยัง data ไม่พอ

ข้อสังเกตเพิ่ม: Google Cloud ได้ประโยชน์หนักกว่า Cognizant ในรอบนี้. 18,000 คนที่ขาย Gemini เป็นหลัก คือ **sales force extended** ที่ Google ไม่ต้องจ้างเอง. ขณะ Cognizant lock-in กับ Gemini stack ที่ถ้า Google เปลี่ยน pricing หรือ terms เมื่อไหร่ ธุรกิจของ Cognizant จะกระทบตรง. Services firm อื่น ๆ ที่ยัง multi-cloud จะดูข้อตกลงนี้แล้วตัดสินใจว่าจะ hedge หรือ commit

## มุม AI Agent Platform

สำหรับ **Builders** ของ agent framework: ตลาด enterprise channel ของ Cognizant/Accenture/TCS คือ **ประตูหลักเข้า Fortune 500**. ถ้า framework คุณไม่ ship **training curriculum + certification program + partner enablement kit** ที่ service firm สามารถ roll ให้พนักงาน 100,000 คนได้ จะ pass channel นี้ไม่ได้. สำหรับ **Users / Business** ที่กำลัง evaluate agent solution: การเลือก SI partner สำคัญเท่า ๆ กับการเลือก framework — ถาม Cognizant/Accenture/TCS ว่า **client ที่ scale deployment ได้มีกี่ราย**, ไม่ใช่ workshop graduate กี่คน. ถ้าตอบไม่ได้ หรือยังมี pilot เป็นหลัก ให้ wait หรือ hire direct. สำหรับ **Ecosystem**: SI firm 6 เจ้ากำลังชนกัน แต่ **cross-cloud agent operator** (คนที่ build + run agent ได้บนทั้ง Google, AWS, Microsoft, OpenAI) ยังหายาก. ตลาด **talent arbitrage** ของคนที่ cert ครบ 3 stack จะมี premium สูง

## Sources
- [Cognizant Expands Strategic Partnership with Google Cloud to Operationalize Agentic AI at Enterprise Scale (Nasdaq)](https://www.nasdaq.com/press-release/cognizant-expands-strategic-partnership-google-cloud-operationalize-agentic-ai)
- [Google and Cognizant expand AI partnership, eye Gemini rollout to 200,000 workers (Crypto Briefing)](https://cryptobriefing.com/?p=397883)
- [Cognizant Creates Gemini Group Under Expanded Google Cloud Partnership (Morningstar)](https://www.morningstar.com/news/dow-jones/202610195273/cognizant-creates-gemini-group-under-expanded-google-cloud-partnership)

---

## Audio script
วันจันทร์ที่ 19 ตุลาคม Cognizant ประกาศขยาย partnership กับ Google Cloud ตั้งกลุ่มใหม่ชื่อ Gemini Frontier Capability Group ที่มีพนักงาน 18,000 คนทำงานเฉพาะ Gemini agent solution ให้ลูกค้า enterprise. Cognizant โฆษณาเพิ่มว่ามีพนักงาน 55,000 คนผ่าน workshop Build with Gemini แล้ว ตั้งเป้าถึง 100,000 ปลายปี 2026 และระยะยาวที่ 200,000 คน. ตัวเลขพวกนี้ยังเป็นที่บริษัทอ้าง — ไม่มี third-party ตรวจ. Pattern สำคัญคือ services firm ขนาดใหญ่ทั้ง Accenture, TCS, Infosys, Deloitte, Wipro, Cognizant กำลัง re-skill พนักงานเป็น agent operator พร้อมกัน. ตลาด IT services เดิมที่ขายคน-ชั่วโมงเขียน code กำลังเปลี่ยนเป็นขาย agent lifecycle management ที่ metric คือ outcome ไม่ใช่ staff hour. จุดที่ต้อง probe คือ Cognizant 18,000 คน + 55,000 คน trained ยังเป็น training throughput ไม่ใช่ production deployment จริง. McKinsey ก็ยัง flag ว่าในฟังก์ชันธุรกิจใด ๆ มีแค่ไม่เกิน 10% ของบริษัทที่ scale agent ได้จริง. และที่ sudah สังเกตคือ Google Cloud ได้ประโยชน์หนักกว่า Cognizant ในดีลนี้ — 18,000 คนที่ขาย Gemini คือ sales force extended ที่ Google ไม่ต้องจ้างเอง
