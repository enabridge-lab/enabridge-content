---
date: 2026-11-04
slug: adobe-cx-coworker-multi-platform
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a central glass console labeled
  "ADOBE CX ENTERPRISE COWORKER" from which five bright cables radiate out
  to five labeled server towers: "ANTHROPIC", "OPENAI", "GOOGLE",
  "MICROSOFT", "DATABRICKS". Behind them three dim pending towers read
  "AWS", "IBM", "SNOWFLAKE" with status lights marked "SOON". A ticker tape
  above reads "MARKETING AGENT DISTRIBUTES EVERYWHERE 2026-11-04".
  Deep red and midnight blue palette with crisp silver highlights, 1:1
  aspect, high contrast for 200px thumbnails, no real human faces.
image: images/26-11-05-0605-02-adobe-cx-coworker-multi-platform.png
---

# Adobe ส่ง CX Coworker ไปทุก LLM platform — pattern ใหม่ของ app vendor คือ “distribute agent หนีการโดน disrupt”

## TL;DR
- 4 พ.ย. 2026 Adobe ประกาศ **CX Enterprise Coworker** รันอยู่ใน platform ของ **Anthropic, Databricks, Google, Microsoft, OpenAI** แล้ว — **AWS, IBM, Snowflake ตามคิว**
- Marketing Agent ของ Adobe จะปรากฏใน Claude Enterprise, ChatGPT Enterprise, Gemini Enterprise, Microsoft 365 Copilot, IBM watsonx Orchestrate และ Amazon Quick
- Adobe เปิดตัว Coworker ครั้งแรก Adobe Summit เม.ย. 2026, GA 10 มิ.ย. 2026 — รอบนี้คือ step 2: **จากเปิดในบ้านตัวเอง → ไปอยู่ใน chat ของทุก LLM vendor**
- Pattern ใหม่: SaaS vendor ที่โดน AI กดราคา (Adobe หุ้น -30% YTD 2026) **แจก agent ของตัวเองไปทุก surface** — distribute ไม่ใช่ปกป้อง
- สิ่งที่ยังไม่เปิด: ไม่มี pricing model, ไม่เปิด token economics, ไม่ชัดว่า Adobe เก็บ data flow back มาเทรน model เองหรือไม่

## เกิดอะไรขึ้น

4 พ.ย. Adobe ประกาศผ่าน press release ว่า **CX Enterprise Coworker** — AI agent ที่ Adobe แนะนำครั้งแรกใน Adobe Summit เดือน เม.ย. และ GA เมื่อ 10 มิ.ย. — ตอนนี้รันอยู่ใน platform ของ **Anthropic (Claude Enterprise), Databricks, Google (Gemini Enterprise), Microsoft (365 Copilot), OpenAI (ChatGPT Enterprise)** เป็นระลอกแรก. **AWS (Amazon Quick), IBM (watsonx Orchestrate), Snowflake** จะตามคิวในไตรมาสหน้า

Coworker ทำหน้าที่เป็น **project manager ของ marketing workflow** — รับ brief, แตก task ให้ sub-agent (บางตัวเป็น Adobe tool เดิมอย่าง Firefly / Analytics / Journey Optimizer, บางตัวเป็น third-party), สรุป KPI, แจ้งเตือน content approval. ใน Claude Enterprise ผู้ใช้จะเรียก Coworker ผ่าน `@Adobe` ตามปกติ — Anthropic เป็น runtime, Adobe เป็น skill layer

มุมธุรกิจ: Adobe เลือก timing นี้ไม่บังเอิญ — **หุ้น ADBE ลง ~30% YTD 2026** ท่ามกลางความกังวลว่า Firefly แข่งกับ DALL-E / Nano Banana ไม่ไหว, และ Figma + Canva + AI-native startup กัดส่วนแบ่ง. Shantanu Narayen CEO ยืนยันบน earnings call Q3 ว่ากลยุทธ์ต่อไปคือ **“make Adobe where the workflow runs, not where the tool opens”** — แปลว่า Adobe ยอมรับว่า user ไม่จำเป็นต้องเข้า Adobe app เลย ตราบใดที่ Adobe agent ยังอยู่ใน loop

Adobe ยังไม่เปิด **billing model** — คาดว่าจะเป็น hybrid ระหว่าง Adobe Experience Cloud seat license + usage-based ฝั่ง LLM platform. **Data flow** เป็นประเด็นเงียบๆ — Coworker ที่รันใน Claude Enterprise เข้าถึง client marketing data ของ brand (campaigns, analytics, journey) — Anthropic / OpenAI / Google จะ access data นั้นแค่ไหน, retain ได้ไหม, ยังไม่มีคำตอบเป็นทางการ

## ทำไมสำคัญ

จุดสำคัญคือ **กลยุทธ์ของ SaaS incumbent ภายใต้แรงกด AI**. Salesforce เลือกสู้ด้วย Agentforce (รัน agent ของตัวเองบน Agentforce 3.0), ServiceNow เลือก Now Assist + MCP marketplace (ข่าวจากรอบ 10-31 ของเรา), **Adobe เลือกที่จะกระจาย agent ออกไปแทนที่จะดึง user กลับเข้ามา**. ท่านี้สวนกับ playbook ปกติ — ปกติ SaaS vendor สร้าง “ป้อม” — AI ยุคนี้ตั้งข้อสมมติว่า user จะทำงานใน LLM ไม่ใช่ใน app

ทำไม Adobe กล้า distribute? เพราะเห็นว่า **ถ้าไม่ไป user จะไม่มา** — Menlo Ventures (รอบนี้เรื่อง 01) เพิ่งบอกว่า 80% ของ token ตกอยู่กับ agent, 69% ของ deployment spend ไปที่ Anthropic/OpenAI/Google. ถ้า CMO ของ brand ใหญ่เปิด Claude Enterprise เป็น default workspace, การวาง Adobe agent ไว้ที่นั่นคือ distribution strategy ที่ลง surface ของ competitor model. การไม่ทำแปลว่าเหลือ user เฉพาะคนที่เปิด Adobe Experience Cloud โดยตรง — จำนวนลดลงทุกปี

Pattern อีกข้อที่ต้องจับตา: **multi-agent reseller pattern** — Adobe ไม่ใช่คนเดียวที่กระจาย. Workday มี agent ใน Copilot แล้ว, ServiceNow มีใน ChatGPT Enterprise, Snowflake มี Cortex agent ใน Teams. ปี 2027 จะเห็น **marketplace of enterprise agents บน LLM platform** คล้ายกับ App Store บน iPhone — ต่างกันที่ **แต่ละ agent รันข้ามหลาย platform ไม่ exclusive**. ประเด็นเป็น commercial — ใครเก็บส่วนแบ่ง, ใคร attribute conversion, ใคร own GTM

สิ่งที่ยัง skeptical ได้: Adobe ไม่เปิด **early traction number** — ไม่มี active user, ไม่มี task volume, ไม่มี time saved metric. Adobe เลือก announce ก่อนที่จะมี proof point — ท่าที่ตลาดเข้าใจว่าเป็น defensive posture ไม่ใช่ product-led growth

## มุม AI Agent Platform

สำหรับ **builders** ที่สร้าง agent framework / marketplace / registry (MCP registry, OpenAI AgentKit แม้จะกำลัง wind down, ServiceNow MCP marketplace, Hugging Face Spaces): การที่ enterprise software ชั้นนำยอม distribute agent ข้ามหลาย LLM surface พร้อมกัน แปลว่า **agent registry layer จะเป็น battlefield สำคัญปี 2027**. MCP แบบ open standard มี tailwind — **vendor neutral + multi-host** ตรงกับความต้องการของ Adobe/Workday/ServiceNow ที่ไม่อยาก lock ตัวเองไว้กับ runtime เดียว

สำหรับ **users / business**: ถ้าเป็น brand ที่ใช้ Adobe Experience Cloud อยู่แล้ว การมี Coworker ปรากฎใน Claude / ChatGPT / Gemini / Copilot แปลว่า **ไม่ต้องเทรนทีมใหม่ให้เปิด Adobe tool อีก** — CMO ที่อยู่ใน ChatGPT Enterprise อยู่แล้วเรียก @Adobe ได้เลย. CFO ต้อง audit **data egress policy** — data marketing จะไหลผ่าน Anthropic / OpenAI / Google ยังไง, retention policy ของแต่ละ platform ต่างกัน, PII / brand asset ต้องเช็ค DPA ก่อน enable

สำหรับ **ecosystem**: Anthropic ได้ประโยชน์ที่สุด — Claude Enterprise ถูก enterprise brand brand เลือกเป็น runtime มากขึ้น (SAP ก็เลือกไปเมื่อ Sapphire เม.ย.). OpenAI ได้ consumer / general / coding, แต่ **Anthropic กำลัง win enterprise contract ของ tier 1**. Google ได้ Workspace user ที่ bundle อยู่แล้ว แต่ convert ไป Gemini Enterprise ยังต้องสู้. Microsoft ได้ installed base ของ Office — 365 Copilot คือ default — แต่ประเด็นคือ **ใครเร็วที่สุดที่จะ onboard Adobe/Workday/ServiceNow agent ให้เรียบ** — ปัจจุบัน Adobe ชื่อ Anthropic ขึ้นก่อน Microsoft / OpenAI สองชื่อในบางช่องทาง — เป็น signal ของการตลาด

## Sources
- [Adobe News — Adobe Integrates CX Enterprise Coworker Into AI Platforms From OpenAI, Google, Microsoft](https://www.marketscreener.com/news/adobe-integrates-cx-enterprise-coworker-into-ai-platforms-from-openai-google-microsoft-ce785fdfdc8bf227)
- [Futurum Group — Adobe Brings CX Enterprise Coworker into Third-Party AI Platforms](https://futurumgroup.com/insights/adobe-brings-cx-enterprise-coworker-into-third-party-ai-platforms/)
- [Adobe — General Availability of CX Enterprise Coworker (June 2026 announcement)](https://news.adobe.com/news/2026/06/adobe-announces-general-availability-of-cx-enterprise-coworker)

---

## Audio script
4 พฤศจิกายน Adobe ประกาศว่า CX Enterprise Coworker — agent ที่ Adobe เปิดตัวเมื่อ Summit เดือนเมษา และ GA เมื่อ มิถุนา ตอนนี้วิ่งอยู่ใน Claude Enterprise ChatGPT Enterprise Gemini Enterprise Microsoft 365 Copilot และ Databricks แล้ว ส่วน AWS IBM Snowflake จะตามเร็วๆนี้. ท่านี้สำคัญ เพราะ Adobe เป็น SaaS incumbent ที่หุ้นลง 30 เปอร์เซ็นต์ปีนี้ กลัวโดน AI กดราคา — แทนที่จะปกป้องผู้ใช้ให้ลงมาใน Adobe app Adobe เลือกส่ง agent ของตัวเองไปอยู่ทุก surface ที่ user เปิด pattern นี้สวนกับ playbook SaaS เดิม. Salesforce เลือกรัน Agentforce ของตัวเอง ServiceNow เลือก MCP marketplace Adobe เลือกกระจาย — คนที่ชนะเร็วที่สุด คือ Anthropic เพราะ Claude Enterprise ถูก Adobe ชื่อขึ้นก่อน และเดือนก่อน SAP ก็เลือก Claude เป็น reasoning layer ของ Autonomous Enterprise. ปี 2027 จะเกิด marketplace ของ enterprise agent ข้ามหลาย LLM ประเด็นคือใครเก็บ revenue ใคร own customer. Takeaway สำหรับ CMO ไทย ถ้าใช้ Adobe Experience Cloud อยู่แล้ว ไม่ต้องย้าย tool แต่ต้อง audit data egress และ DPA กับ LLM provider ที่จะเข้าถึง campaign data ของเรา ก่อนเปิด Coworker ในงาน real
