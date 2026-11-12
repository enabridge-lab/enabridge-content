---
date: 2026-11-13
slug: rox-100m-revenue-agent-salesforce
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  A dramatic editorial scene of a giant corporate boardroom — on one wall a
  massive glowing wordmark "ROX" with a cheeky agent-robot silhouette,
  pointing at a cracked Salesforce-cloud-shaped icon tipped onto its side.
  Floating above: "$100M SERIES B" and "$1.3B VALUATION". Three small logo
  chips on a shelf labeled "PUMA", "GROQ", "RAMP" as customer badges. A
  scoreboard in the corner reads "SALES REP = NEXT SEAT". Editorial
  cinematic style, deep navy with hot coral accents, 1:1 aspect, high
  contrast large numbers readable at 200px, no real human faces.
image: images/26-11-13-0604-02-rox-100m-revenue-agent-salesforce.png
---

# Rox $100M ชน Salesforce ที่ hallway ของ CRM — แต่คำถามจริงคือใครจ่าย renewal

## TL;DR
- Rox ปิด Series B $100M valuation $1.3B นำโดย General Catalyst + March Capital — Sequoia และ GV ลงเพิ่ม
- Puma, Groq, Ramp อยู่ในรายชื่อลูกค้า — แต่ Rox ไม่เปิด active user หรือ revenue
- Positioning ชัด — "AI revenue agent" ที่ identify, generate pipeline, manage deal, expand account แทน rep แทนที่จะเป็น CRM record

## เกิดอะไรขึ้น
วันที่ 11 พฤศจิกายน Rox ประกาศ Series B $100M ที่ valuation $1.3B — General Catalyst กลับมา lead อีกรอบคู่กับ March Capital, Sequoia และ GV ลงเพิ่ม, Prosperity7 เข้าเป็น new investor Rox ตั้งในปี 2024 ชูธงว่าเป็น "AI revenue agent" สำหรับ Global 2000 — สิ่งที่น่าสนใจคือ pitch ไม่ใช่ "CRM ที่มี AI" แต่เป็น "agent ที่ทำงานแทน rep ตั้งแต่ prospect research จนถึง account expansion"

ลูกค้าที่เปิดเผยคือ Puma (retail/footwear), Groq (semiconductors), และ Ramp (fintech) — ทั้งสามเป็น reference ที่ target ต่างกันชัด: brand ที่ขาย B2B2C, infra provider ที่ขาย enterprise technical, และ fintech ที่ขาย finance team ทั่วประเทศ Rox อ้างว่าโปรดักต์ของตัว crosses the boundary ของ outbound + inbound + account-based + renewal workflow ได้ด้วย agent เดียว

มุมที่ตลาดโฟกัสคือ positioning เทียบ Salesforce — General Catalyst บอกผ่าน Reuters ว่ารอบ Series A ปี 2024 มีทีม sales มากกว่า 35 ทีมใน public beta การที่ GC double down ใน Series B แบบ returning lead แปลว่า retention metric ภายในดีพอให้เชื่อว่า agent-native CRM เป็นหมวดใหม่จริง ไม่ใช่ feature ที่ Salesforce เพิ่ม Agentforce เข้าไปแล้วจบ

## ทำไมสำคัญ
เมื่อ Salesforce ประกาศ Agentforce Coworker 185,000 users เมื่อสัปดาห์ก่อน (ดู brief 26-11-06-0605-01) ตลาดคิดว่า incumbent ปิดช่องแล้ว แต่ Rox $100M ที่ valuation $1.3B ชี้ว่า investor ยังเชื่อว่ามีช่องให้ startup — เพราะคำถามพื้นฐานยังไม่มีคำตอบว่า agent ที่ bolt-on CRM เดิม (Agentforce บน Salesforce Core) จะดีกว่าหรือแย่กว่า agent-native stack ที่ไม่มี legacy schema ของ Account/Opportunity/Lead แปะอยู่

ประวัติศาสตร์ SaaS บอกว่า — เมื่อเทคโนโลยี foundation เปลี่ยน (cloud → mobile → AI) โปรดักต์ที่ชนะมัก native built ไม่ใช่ bolted-on กระนั้น Salesforce มี distribution + relationship + data gravity มหาศาล การแข่งไม่ใช่เรื่อง "ใคร agent เก่งกว่ากัน" แต่เป็น "CFO ของ Fortune 500 จะกล้าแทนที่ system of record ที่ทำงานมา 15 ปีไหม" ซึ่งคำตอบตามประวัติคือ ไม่ จนกว่าจะเจ็บจัด

Caveat จริง ๆ คือ Rox ยังไม่เปิด active user, revenue, หรือ churn — Puma/Groq/Ramp เป็นชื่อ logo แต่ไม่รู้ว่าใช้ Rox เป็น primary หรือ pilot การ raise ที่ valuation 13x ของ revenue ที่ไม่เปิดเผยมี political risk สูง ถ้า Q1 2027 ยังไม่โชว์ ARR + customer count ชัด investor จะเริ่มถาม tough question เรื่อง unit economics

## มุม AI Agent Platform
Builders — สิ่งที่ Rox พิสูจน์คือ "agent ที่ทำงาน end-to-end ของ function ใดฟังก์ชันหนึ่ง" ได้ valuation สูงกว่า "copilot ที่ช่วยทำงานบางส่วน" การ pitch ของ Rox ไม่ใช่ "AI ช่วย rep ของคุณ" แต่เป็น "agent ทำงานแทน rep" ความแตกต่างที่เล็กในคำ แต่ใหญ่ใน business model — agent-as-labor pricing (ที่คิดตามผลงาน) จะกินตลาด seat-based pricing ในระยะยาว ถ้า execution ของ agent-native player เอาชนะ incumbent ที่เพิ่ม AI layer ได้จริง

Users/business — ถ้าทีมของคุณกำลัง evaluate CRM/sales tech ใหม่ปี 2027 ให้ต้อง compare agent-native (Rox, Clay, 11x, Nooks) กับ incumbent-plus-AI (Salesforce Agentforce, HubSpot, Microsoft Dynamics Copilot) ไม่ใช่แค่ demo feature แต่ถาม metric เดียว — "agent ทำ action ได้กี่ step โดยไม่ต้อง human intervene และเมื่อ intervene มันเกิดเพราะเหตุผลอะไร" ตัวเลขนี้คือ proxy ของ agent autonomy จริง

Ecosystem — Salesforce, HubSpot, Microsoft ต้องเลือกยากในปี 2027 — ขายต่อ seat ของ coworker agent (predictable revenue) หรือ shift ไป outcome-based pricing (เสี่ยงกับ existing margin) ถ้า agent-native player เช่น Rox พิสูจน์ outcome-based ได้จริง incumbent ที่ไม่ปรับจะติดใน innovator's dilemma classic สำหรับ Enabridge และคนไทยที่ขาย agent — เคส Rox ชี้ว่า "agent ตัวหนึ่งที่ทำงานของ function ทั้งฟังก์ชัน" ขายได้แพงกว่า assistant 10 ตัว

## Sources
- [Rox Raises $100M Series B at $1.3B Valuation to Advance AI Research (Unite.AI)](https://www.unite.ai/rox-raises-100m-series-b-at-1-3b-valuation-to-advance-ai-research/)
- [Rox raises $100M at $1.3B valuation to take on Salesforce (Crypto Briefing)](https://cryptobriefing.com/rox-raises-100m-ai-sales-salesforce/)
- [Sequoia-backed Rox raises $100M at $1.3B valuation (TechFundingNews)](https://techfundingnews.com/sequoia-backed-rox-raises-100m-at-1-3b-valuation-can-ai-agents-unseat-salesforce-in-sales/)
- [Rox Raises $100 Million As Investors Bet AI Agents Can Outsell Salesforce's CRM (Ventureburn)](https://ventureburn.com/rox-raises-100-million-ai-agents-outsell-salesforce-crm/)

---

## Audio script
Rox ปิด Series B 100 ล้านเหรียญที่ valuation 1.3 พันล้านเหรียญเมื่อวันที่ 11 พฤศจิกายน General Catalyst กลับมา lead อีกรอบคู่กับ March Capital, Sequoia และ GV ลงเพิ่ม, Prosperity7 เข้าเป็น investor ใหม่ Rox positioning ตัวเองไม่ใช่ CRM ที่มี AI แต่เป็น AI revenue agent ที่ทำงานตั้งแต่ prospect research จนถึง account expansion แทน sales rep ลูกค้าที่เปิดคือ Puma, Groq, และ Ramp เป็น reference ที่ target ต่างกันชัด เมื่อ Salesforce ประกาศ Agentforce Coworker 185,000 users เมื่อสัปดาห์ก่อน ตลาดคิดว่า incumbent ปิดช่องแล้ว แต่ Rox 100 ล้านที่ 1.3 พันล้านชี้ว่า investor ยังเชื่อว่ามีช่องให้ startup เพราะคำถามพื้นฐานยังไม่มีคำตอบ agent ที่ bolt-on CRM เดิมจะดีหรือแย่กว่า agent-native stack ประวัติศาสตร์ SaaS บอกว่าเมื่อ foundation technology เปลี่ยน โปรดักต์ที่ชนะมักเป็น native built ไม่ใช่ bolted-on สิ่งที่ Rox พิสูจน์คือ agent ที่ทำงาน end-to-end ของ function ใดฟังก์ชันหนึ่งได้ valuation สูงกว่า copilot ที่ช่วยทำงานบางส่วน agent-as-labor pricing ที่คิดตามผลงานจะกินตลาด seat-based ในระยะยาว สำหรับคนที่ขาย agent ในไทย เคส Rox ชี้ว่า agent ตัวหนึ่งที่ทำงานของ function ทั้งฟังก์ชันขายได้แพงกว่า assistant 10 ตัว แต่ caveat คือ Rox ยังไม่เปิด active user หรือ revenue ถ้า Q1 2027 ยังไม่โชว์ตัวเลขชัด investor จะเริ่มถาม tough question เรื่อง unit economics
