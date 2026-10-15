---
date: 2026-10-16
slug: nous-research-hermes-enterprise
topic: use-case
reading_time_min: 3
sources: 3
image_prompt: |
  A towering open-source stone monolith carved with the word "HERMES",
  cracked open to reveal a glowing enterprise server rack inside. Three
  giant floating numbers around it read: "22.7M DOWNLOADS", "$36M ARR",
  "$1.5B VALUATION". A line of corporate briefcases queue up at a payment
  kiosk marked "HERMES FOR BUSINESSES". Editorial isometric style,
  oxidized copper and electric cyan palette, 1:1 aspect, no real human
  faces.
image: images/26-10-16-0615-03-nous-research-hermes-enterprise.png
---

# Nous Research: open-source agent ที่โตถึง $36M ARR แล้วเพิ่งเริ่มเก็บเงิน

## TL;DR
- **$90M Series B** ที่ valuation **$1.5B** นำโดย Robot Ventures — Nvidia, M12, Samsung, USV, Y Combinator, Menlo ร่วมด้วย
- **Hermes Agent** (MIT license, เปิดกุมภา 26) โดนดาวน์โหลด **22.7 ล้านครั้ง** แล้ว — WSJ รายงาน ARR **~$36M** กลางเดือน ก.ย. บริษัทคาด **>$100M** สิ้นปี
- เม็ดเงินก้อนนี้ใช้ build **Hermes for Businesses** — hosted commercial version ที่ยังยืนอยู่บน MIT core เดิม

## เกิดอะไรขึ้น

Wall Street Journal เปิดเผยว่า Nous Research ที่เริ่มจากเป็น community รอบ open-weight model เมื่อปี 2024 ตอนนี้ปิด Series B ที่ $90 ล้าน ด้วย valuation $1.5 พันล้าน จุดที่น่าทึ่งไม่ใช่ตัวเลข funding — แต่คือ **traction trajectory** ของ Hermes Agent ซึ่งเป็น open-source agent framework ที่บริษัทปล่อยภายใต้ MIT license เมื่อกุมภาพันธ์ปีนี้ ใน 8 เดือนทำยอดดาวน์โหลด 22.7 ล้านครั้ง — เป็นอัตราที่เทียบได้กับ Ollama หรือ LangChain ในช่วง peak

ที่สำคัญกว่า adoption คือ **revenue conversion**: Nous เพิ่งเริ่มขาย commercial hosted version ไม่กี่เดือน แต่ WSJ อ้างว่า ARR run rate แตะ $36M ไปแล้วเมื่อ mid-September และ Dillon Rolnick (CEO) เขียนในหมายเหตุรอบ funding ว่าคาดว่าจะทะลุ $100M ก่อนสิ้นปี — ซึ่งถ้าเป็นจริง การ convert จาก open-source adoption เป็น enterprise revenue ที่ 3x ในหนึ่งไตรมาสเป็นตัวเลขที่ veteran VC หลายคนยืนยันว่าหา pattern แบบนี้ได้ยากมาก

Round นี้ลงนามโดย Robot Ventures เป็น lead แต่ Nous เองไม่ประกาศว่า confirm ตัวนี้ — มี Nvidia, Microsoft M12, Samsung, Union Square Ventures, Y Combinator และ Menlo Ventures ร่วมลง รวม cumulative funding ประมาณ $158M

## ทำไมสำคัญ

เส้นทาง "open-source core + hosted commercial" ของ Nous Research กำลังทำซ้ำ playbook ที่ MongoDB, Confluent, Databricks ใช้ชนะใน data infrastructure ยุคก่อน แต่ที่สำคัญคือ **อัตราการ convert เร็วกว่ามาก** — MongoDB ใช้เวลา 4-5 ปีจาก open release ถึง $100M ARR, Nous กำลังจะทำใน 10 เดือน

ปัจจัยที่ทำให้ pattern นี้เร็วขึ้นคือสองเรื่อง หนึ่ง: enterprise ยุคนี้พร้อมจ่ายเงินสำหรับ hosted ของ open-source project ที่ developer ของตัวเองใช้อยู่แล้ว (เพราะไม่อยาก host เอง — compliance กับ GPU cost แพง) สอง: agent workload โดยธรรมชาติต้องเก็บ state ยาวและเชื่อม tool หลายตัว ทำให้ "hosted" คุ้มกว่า "self-deploy" มาก ส่วน Hermes ที่ได้ MIT license ก็กลายเป็น Trojan horse ที่ลงไปในองค์กรก่อน แล้วค่อย upsell

สิ่งที่ต้องระวังคือตัวเลข $36M ARR และ projection $100M มาจาก WSJ ที่ cite แหล่งไม่ระบุ ไม่ใช่ Nous confirm โดยตรง และ Spanish-language source บางเจ้าให้เลข Series B ที่ $75M ไม่ใช่ $90M — pattern นี้คือ WSJ ใช้ late-round rumor ที่ยัง settle ไม่เสร็จ

## มุม AI Agent Platform

สำหรับ **builder** ที่กำลังเริ่ม project agent framework — model business ของ Nous คือ reference ที่ควรดู: ปล่อย core เป็น open-source permissive license (MIT ไม่ใช่ AGPL), build hosted platform เบา ๆ ที่ opinionated ตอบ compliance + observability + managed-GPU, แล้วให้ community ขยาย ecosystem ให้

สำหรับ **business ที่ deploy agent** — ให้พิจารณาว่า Hermes อยู่ใน shortlist หรือยัง การที่ Nvidia, Microsoft, Samsung ร่วมลงหมายความว่าจะมี integration ที่ smooth กับ CUDA stack, Azure, และ Samsung ecosystem ในอีก 6-12 เดือน

สำหรับ **ecosystem** นี่คือสัญญาณชัดว่า open-source agent framework ไม่ใช่ "ไม่มี business model" อีกต่อไป — Nous ทำให้เห็นว่า adoption 22M+ convert เป็น revenue ได้จริง ซึ่งจะทำให้ incumbent proprietary platform (Salesforce Agentforce, ServiceNow Now Assist, Microsoft Copilot Studio) ต้องทบทวนว่าจะ compete กับ "free + hosted" model ยังไง

## Sources
- [Nous Research raises $90m at $1.5b valuation for open source AI](https://dealroom.co/news/160592-nous-research-raises-90m-at-1-5b-valuation-for-open-source-ai/)
- [Nous Research Raises $90 Million to Build Business AI Agents](https://mezha.net/eng/?p=3729422)
- [Nous Research closes Series B of US$75M and brings Hermes to companies](https://ecosistemastartup.com/nous-research-cierra-serie-b-de-us75m-y-lleva-hermes-a-empresas/)

---

## Audio script
Wall Street Journal รายงานสัปดาห์นี้ว่า Nous Research ปิด Series B ที่ 90 ล้านดอลลาร์ ด้วย valuation 1.5 พันล้านดอลลาร์ นำโดย Robot Ventures มี Nvidia Microsoft Samsung และ Y Combinator ร่วมด้วย ที่น่าทึ่งไม่ใช่ตัวเลข funding แต่คือเรื่องของ Hermes Agent ที่เปิดภายใต้ MIT license เมื่อกุมภาพันธ์ปีนี้ 8 เดือนทำยอดดาวน์โหลดไปแล้ว 22.7 ล้านครั้ง และ ARR แตะ 36 ล้านดอลลาร์กลางเดือน ก.ย. บริษัทคาดว่าจะทะลุ 100 ล้านก่อนสิ้นปี

สิ่งที่น่าสนใจคือ Nous กำลังทำซ้ำ playbook ของ MongoDB และ Databricks ที่ปล่อย core เป็น open-source แล้วขาย hosted commercial แต่เร็วกว่ามาก MongoDB ใช้เวลา 4 ถึง 5 ปีจาก open release ถึง 100 ล้าน ARR Nous กำลังจะทำใน 10 เดือน

ที่เร็วเพราะสองอย่าง หนึ่ง enterprise ยุคนี้พร้อมจ่ายเงินให้ hosted version ของ open-source ที่ developer ตัวเองใช้อยู่แล้ว เพราะ host เองแพง สอง agent workload ต้องเก็บ state ยาวและเชื่อม tool เยอะ ทำให้ hosted คุ้มกว่า self-deploy มาก สำหรับทีมที่กำลังสร้าง agent framework ให้ดู model ของ Nous เป็น reference ปล่อย core เป็น MIT แล้ว build hosted ที่ opinionated รอบ compliance observability และ managed GPU สำหรับ business ที่กำลังเลือก agent platform Hermes ควรอยู่ใน shortlist เพราะ Nvidia Microsoft Samsung อยู่ในรอบนี้ แปลว่า integration กับ stack ของเขาจะมาเร็ว
