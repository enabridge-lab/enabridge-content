---
date: 2026-10-27
slug: daytona-60m-agent-cloud
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a futuristic data-center cross-section
  with glowing sandbox cubes popping into existence on a conveyor, each stamped
  "60ms". A big neon ribbon above reads "AGENT CLOUD". Three floating numbers
  on the right: "$60M SERIES B", "$1B VALUATION", "25x REVENUE". Blue and
  magenta neon on dark navy background, crisp line work, 1:1 aspect, no real
  human faces.
image: images/26-10-27-0607-02-daytona-60m-agent-cloud.png
---

# Daytona ยูนิคอร์นที่สาม — Agent cloud ที่ provision sandbox ใน 60ms + รายได้โต 25 เท่าตั้งแต่ต้นปี

## TL;DR
- Daytona ปิด Series B $60M ที่ valuation $1B นำโดย FirstMark — ยูนิคอร์นที่ 3 ของโครเอเชีย (ตาม Infobip, Rimac)
- ลูกค้าของ Daytona คือ Anthropic, OpenAI, Nvidia, Cursor, Cognition, Meta, Cohere — ใช้ sandbox เป็น runtime สำหรับ agent ที่ต้อง run code และใช้เครื่องมือ
- Revenue run rate โต 25x ระหว่างมกราคม-กันยายน; sandbox เปิดใหม่ใน 60 millisecond ด้วย pre-loaded snapshots

## เกิดอะไรขึ้น
วันที่ 20 ตุลาคม Daytona ประกาศ Series B $60M (€56M) ที่ valuation $1B นำโดย FirstMark. Ivan Burazin ซีอีโอ ซึ่งย้ายจาก Croatia มาสร้างบริษัทที่ New York บอกว่ารายได้บริษัทโต 25 เท่าจากมกราคมถึงกันยายน และประมาณ $50M จากรอบนี้มาจาก existing investor — signal ว่า insider เชื่อแรง. Total funding ของบริษัทตอนนี้แตะ ~$91M.

ตัวสินค้าของ Daytona เรียบง่ายในเชิง framing: "sandbox for AI agents" — environment แยก (isolated) ที่ agent run code, เรียก tool, และทำงานยาว ๆ ได้โดยไม่กระทบระบบหลัก. จุดที่ทำให้ Daytona ต่างคือ pre-loaded snapshot ที่ทำให้ provision sandbox ใหม่ใช้เวลาแค่ 60 milliseconds — เร็วพอที่ agent ที่ parallelize งาน (เช่น Cognition's Devin) จะเปิด sandbox ได้แบบ on-demand ทุก task ย่อย โดยไม่สะดุด.

Customer list ที่ Daytona เปิดเผยคือรายการที่ทำให้ VC ยิ้ม: Anthropic, OpenAI, Nvidia, Cursor, Cognition, Meta, Cohere. ใช้ Daytona เป็น infrastructure สำหรับ train และทดสอบ model + agent. ที่น่าสังเกตคือลูกค้าเหล่านี้ส่วนใหญ่ก็มี cloud infrastructure เป็นของตัวเองอยู่แล้ว แต่ยังยอมจ่ายให้ Daytona — บอกว่า general-purpose cloud ไม่ตอบโจทย์ agent workload.

## ทำไมสำคัญ
Agent workload แตกต่างจาก SaaS workload ที่เราเคยรู้จักในสองแกนที่สำคัญ: (1) จำนวน sandbox เยอะมาก เพราะ agent หนึ่งงานอาจเปิด 50-100 sandbox parallel สำหรับ tool call ย่อย (2) อายุสั้นมาก — บาง sandbox อยู่แค่ไม่กี่วินาที. AWS Lambda ทำได้ แต่ cold start 300-1000ms และคิดเงินแบบ pricing model ที่ไม่ลงตัวกับ pattern นี้. Daytona มองเห็นช่องว่างและสร้าง primitive ใหม่ที่เรียกว่า "agent-native compute".

Pattern เดียวกันกับที่ Snowflake แยกออกจาก general warehouse เพื่อ serve BI workload โดยเฉพาะ, และ Vercel แยกออกจาก generic hosting เพื่อ serve frontend workflow. ตอนนี้ Daytona กำลังทำ bet ที่ว่า agent runtime เป็น category แยกที่ hyperscaler จะไม่ชนะ — เพราะ hyperscaler ตั้ง pricing และ UX มาจาก legacy workload. 25x revenue growth ใน 9 เดือนบอกว่าตลาดเริ่มเชื่อ.

## มุม AI Agent Platform
สำหรับ **builders**: ถ้าคุณกำลังสร้าง agent ที่ต้อง execute code (web scraping, data analysis, software engineering) การไปใช้ Lambda / Cloud Run / Fly.io มี friction ที่คุณจะเจอตั้งแต่ user 100 คน — Daytona ชี้ว่ามี vocabulary ใหม่ที่ควรเริ่มเรียน: snapshot, warm sandbox, parallelized tool call. สำหรับ **users** ไม่ต้องเลือกเอง แต่ควรรู้ว่า agent platform ที่ production-ready ภายในปี 2027 จะต้องใช้ compute layer แบบนี้. สำหรับ **ecosystem**: มีคำถามใหญ่ว่า AWS, Azure, GCP จะ build/buy หรือปล่อยให้ Daytona (และ competitor อย่าง E2B, Modal) เติบโตเป็น independent layer — เพราะถ้า agent native compute เป็น $10B category จริง จะไม่มี hyperscaler ไหนปล่อย.

## Sources
- [Daytona Raises $60M Series B at $1B for AI-Agent CPU Cloud, 25x Revenue Jump Since January (AI Weekly)](https://aiweekly.co/alerts/daytona-raises-60m-series-b-at-1b-for-ai-agent-cpu-cloud-25x-revenue-jump-since)
- [Daytona hits $1B valuation with $60M Series B for AI agent cloud (Tech.eu)](https://tech.eu/2026/10/20/daytona-hits-1b-valuation-with-60m-series-b-for-ai-agent-cloud/)
- [Daytona Series B — Croatia's Third Unicorn (The Recursive)](https://therecursive.com/daytona-series-b-valuation-croatias-third-unicorn)
- [Daytona raises $60M Series B (Dealroom)](https://dealroom.co/news/164304-daytona-raises-60m-series-b-at-1b-valuation-to-build-the-agentic-cloud/)

---

## Audio script
ข่าวที่สองวันนี้เรื่อง Daytona บริษัทจากโครเอเชียที่เพิ่งเป็นยูนิคอร์นลำดับที่สามของประเทศ จากการปิดรอบ Series B 60 ล้านดอลลาร์ที่ valuation พันล้าน. สินค้าที่ Daytona ทำคือ sandbox สำหรับ AI agent คือ environment แยกที่ agent เอาไว้ run code เอาไว้เรียก tool โดยไม่กระทบระบบหลัก. จุดที่ Daytona ชนะคู่แข่งคือเปิด sandbox ใหม่ได้ในเวลาแค่ 60 มิลลิวินาที เร็วกว่า AWS Lambda หลายเท่า เพราะใช้วิธี pre-load snapshot เอาไว้ก่อน. ลูกค้าของ Daytona ตอนนี้คือ Anthropic, OpenAI, Nvidia, Cursor, Cognition, Meta, Cohere ซึ่งใช้ sandbox เป็น runtime สำหรับ train และทดสอบ model. ซีอีโอบอกว่ารายได้บริษัทโต 25 เท่าตั้งแต่มกราคม. เรื่องนี้สำคัญเพราะมันบอกว่า agent มี workload แปลกใหม่ที่ hyperscaler เดิมอาจจะ serve ไม่ดีพอ ถ้าคุณสร้าง agent ที่ parallelize งานหลาย task ย่อย คุณต้องเริ่มคุ้นกับ vocabulary ใหม่ของ agent-native compute
