---
date: 2026-08-10
slug: corma-60m-sequoia-defensive-cybersecurity-ai-lab
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  A modern SOC control room seen from above; on the wall three large numeric
  cards read "94% RESPONSE TIME CUT", "15X COVERAGE", "6 WEEKS IN PROD". A
  logo plate labeled "CORMA" sits above a Sequoia monogram and a small
  "FORTUNE 100/500" tag. Editorial isometric style, deep navy and neon
  green palette, 1:1 aspect, no real human faces (silhouette OK).
image: images/26-08-12-0617-02-corma-60m-sequoia-defensive-cybersecurity-ai-lab.png
---

# Corma ระดมทุน $60M seed จาก Sequoia — เปิดตัวเป็น "first frontier defensive cybersecurity AI lab" ด้วย agent ที่ลดเวลาตอบสนอง 94%

## TL;DR
- Corma (Tel Aviv/SF, founded 2025) ระดม $60M seed lead โดย Sequoia Capital ร่วมกับ Khosla Ventures และ Coatue เมื่อ 10 ส.ค. — ประกาศตัวเป็น "first frontier AI lab for defensive cybersecurity"
- Deploy model แรกเมื่อ 6 สัปดาห์ก่อนกับลูกค้า Fortune 100/500 ในสาขา healthcare, financial services, energy, critical infrastructure, retail — ผลรายงาน: **ลด threat-response time ลง 94%+, ขยาย coverage 15 เท่า** ข้าม security function
- POV เดียวกับ OpenAI Daybreak ที่เพิ่งประกาศวันเดียวกัน: defense จะเป็น agent-shaped market แต่ Corma เดิน specialist path — build foundation model เฉพาะทาง แทนที่จะ tier-off จาก general-purpose

## เกิดอะไรขึ้น
Corma เปิดตัวสู่ตลาดพร้อม $60M seed round ที่แปลกในหลายมิติ — round size ระดับ Series A แต่เรียก seed, lead โดย Sequoia (ซึ่งไม่ค่อยเข้า seed อีกแล้ว), และ founder position บริษัทว่าเป็น "lab" ไม่ใช่ "startup" ตั้งใจ signal ตำแหน่งเทียบ Anthropic/OpenAI — แต่ vertical เดียวคือ defensive cyber ทีมมาจาก Israeli cyber ecosystem (unit 8200-adjacent) + AI research background พร้อม co-founder ที่เคยอยู่ทั้ง Palo Alto Networks กับ DeepMind ตามที่ Fortune รายงาน

Product ของ Corma คือ **foundation model ที่ trained เฉพาะทาง defensive security** — ไม่ใช่ wrapper บน GPT/Claude — พร้อม agent runtime ที่ทำงานข้าม security tool ของลูกค้าตั้งแต่ SIEM, EDR, ticketing, IAM, และ CMDB โดย carry out task ตั้งแต่ triage → investigate → contain → remediate แบบ end-to-end Corma อ้างว่า model ของเขาเข้าใจ security context ที่ general-purpose model plaintext ไม่มี — เช่น log format ของ CrowdStrike Falcon, alert schema ของ Splunk ES, และ playbook grammar ของ SOAR

Metric ที่บริษัทเปิดหลัง deploy 6 สัปดาห์กับ Fortune 100/500 ในหลาย vertical (healthcare/financial/energy/critical infra/retail): **response time ลด 94%+**, **coverage ขยาย 15x** ข้าม security function, และเจอ multi-stage attack campaign ที่ human-led team จะพลาด — ตัวเลขที่หนัก แต่ Corma ระบุว่ามาจาก customer report ของเขาเอง ไม่ใช่ audit ของ third party

## ทำไมสำคัญ
Corma กับ [OpenAI Daybreak](https://dataconomy.com/2026/08/11/openai-expands-daybreak-with-new-gpt-5-6-cyber-model/) ประกาศห่างกัน 24 ชั่วโมง — เรื่องบังเอิญที่บอก consensus ของ market ในเวลาเดียวกันว่า **AI-vs-AI cyberwar เริ่มจริง** และการที่ human-led SOC จะทันกับ AI-powered attacker เป็นเรื่องยาก signal ที่นักลงทุนอ่านคือ: defensive cyber ไม่ใช่ analytics dashboard อีกต่อไป มันคือ workload ที่ agent ต้อง execute — และตลาดพร้อมจ่ายเงินระดับ frontier lab เพื่อ solution ที่ตัวเองไม่ต้อง staff SOC 24/7

จุดต่างที่ interesting: Corma เดิน **vertical foundation model path** — คล้าย pattern ที่ [Physical Intelligence](https://www.physicalintelligence.company) ทำกับ robotics หรือ [Latent Labs](https://www.latentlabs.com) ทำกับ biology — ไม่ใช่ fine-tune บน general model แต่ pre-train ใหม่บน security data corpus นี่คือ bet ว่า security domain "different enough" ที่ general model ตามไม่ทันแม้จะ tier-off แบบ OpenAI ทำ — ถ้า Corma ถูก market ก็จะเห็น vertical foundation lab เกิดในหลาย domain อีกภายในปี 2027

จังหวะที่น่าจับ: **Sequoia lead + Khosla + Coatue** ใน seed = signal ที่ tier-1 fund พร้อมจ่าย premium สำหรับ founding-stage lab ที่มี technical credibility Sequoia เพิ่งลงใน [Anthropic Ode $1.5B](https://www.anthropic.com/news/introducing-ode) เมื่อไม่กี่วันก่อน — แสดงว่า thesis เดียวกันคือ enterprise + AI agent จะเป็น distribution game ไม่ใช่ technology game

## มุม AI Agent Platform
สำหรับ **builders** ที่ทำ security agent framework: Corma เป็น signal ว่า vertical foundation model จะเข้ามาแข่งกับ agent orchestration layer ที่ build บน frontier model — ถ้า model ของ vertical lab เข้าใจ security context ดีกว่าจริง framework บน GPT/Claude ต้องมี moat อื่นเช่น integration depth หรือ workflow accuracy เพื่ออยู่รอด สำหรับ **users/business** ที่ deploy agent: ตัวเลข 94% response time reduction เป็น benchmark ที่ CISO จะเอาไปเทียบตอน RFP — ถ้า vendor ไหนยังพูดเป็น percentage ของ "alert triaged" หรือ "false positive reduced" อย่างเดียว จะเสียเปรียบ Corma ที่พูดเป็น time-to-contain

สำหรับ **ecosystem/vendor**: CrowdStrike ($90B+ market cap), Palo Alto ($100B+), SentinelOne, Rapid7, และ managed SOC providers เจอ competitor ที่มี model layer + agent runtime + Fortune 500 customer proof ในรอบเดียว pricing model ของ managed SOC ที่คิดต่อ endpoint หรือ per-analyst-hour จะโดนกดทันทีถ้า Corma pricing เป็น outcome-based (per-incident-resolved) — pattern เดียวกับที่ Anthropic Ode ใช้กับ Big Four consulting

## Sources
- [Exclusive: Corma raises $60 million from Sequoia — Fortune](https://fortune.com/2026/08/10/exclusive-corma-raises-60-million-from-sequoia-for-ai-trained-to-defend-against-cyberattacks/)
- [Corma, the First Frontier Defensive Cybersecurity AI Lab, Raises $60M — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/corma-first-frontier-defensive-cybersecurity-130000308.html)
- [Corma raised $60M from Sequoia to build the defensive AI that cybersecurity is missing — The Next Web](https://thenextweb.com/news/corma-60m-seed-sequoia-defensive-cybersecurity-ai)
- [Corma raises $60M to build defensive cybersecurity AI — Tech Startups](https://techstartups.com/2026/08/10/corma-raises-60m-to-build-defensive-cybersecurity-ai-as-ai-powered-attacks-surge/)

---

## Audio script
เมื่อวานนี้ 10 สิงหาคม startup ชื่อ Corma เปิดตัวพร้อม $60 ล้าน seed round lead โดย Sequoia Capital ร่วมกับ Khosla กับ Coatue — ตำแหน่งบริษัทตัวเองว่าเป็น first frontier AI lab for defensive cybersecurity ตั้งอยู่ที่ Tel Aviv กับ San Francisco ก่อตั้งปีที่แล้ว ทีมมาจาก Israeli cyber ecosystem ผสมกับ AI research background สิ่งที่ Corma ทำต่างจาก security vendor เจ้าเดิมคือเขา build foundation model เฉพาะทาง defensive security ไม่ใช่ wrapper บน GPT หรือ Claude แล้วรัน agent runtime ทำงานข้าม security tool ของลูกค้าตั้งแต่ SIEM, EDR, ticketing จนถึง remediation ตัวเลขที่เขาเปิดหลัง deploy 6 สัปดาห์กับ Fortune 100/500 ใน healthcare, financial services, energy, critical infra, retail คือลด response time 94% ขยาย coverage 15 เท่า และเจอ multi-stage attack ที่ทีมคนตามไม่ทัน ที่บังเอิญคือ Corma กับ OpenAI Daybreak ประกาศห่างกันแค่วันเดียว — signal ว่า market เห็นตรงกันว่า AI-vs-AI cyberwar เริ่มแล้ว defensive cyber ไม่ใช่ dashboard SaaS แต่เป็น agent workload สำหรับคนทำ AI Agent Platform นี่คือสัญญาณว่า vertical foundation model จะแข่งกับ agent framework บน frontier model และ CrowdStrike Palo Alto SentinelOne ต้องอ่าน RFP ปีนี้ให้ดีเพราะ Corma มาพร้อม model บวก agent บวก Fortune 500 proof ในรอบเดียวครับ
