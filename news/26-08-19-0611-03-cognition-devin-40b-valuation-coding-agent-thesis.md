---
date: 2026-08-19
slug: cognition-devin-40b-valuation-coding-agent-thesis
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a rocket labeled "DEVIN" launching
  from a coding workshop; the rocket's exhaust trail is made of tiny PR
  merge icons and green checkmarks; three big floating numbers stacked
  centre: "$40B VALUATION", "$492M → $1B ARR", "+50% MoM"; small enterprise
  logos as passengers in the rocket's window: a bank vault ("GOLDMAN"),
  a car silhouette ("MERCEDES"), a government building; a Cognition
  wordmark on the rocket fin. Editorial magazine style, thick outlines,
  high contrast, readable at 200px thumbnail, 1:1 aspect, no real human
  faces.
image: images/26-08-19-0611-03-cognition-devin-40b-valuation-coding-agent-thesis.png
---

# Cognition คุยรอบใหม่ที่ $40B — 3 เดือนหลัง $26B, ARR ทะลุ $492M โต 50% ต่อเดือน 6 เดือนติด, Goldman/Mercedes เป็นลูกค้าจริง — coding agent thesis เข้าโหมด repricing

## TL;DR
- **12 ส.ค. 2026** — Bloomberg + TechCrunch รายงาน Cognition (บริษัทแม่ของ Devin + Windsurf) คุย funding round ใหม่ที่ **valuation อย่างน้อย $40B**
- **3 เดือนก่อน** เพิ่งปิดรอบ **$1B ที่ $26B valuation** — round ใหม่ตั้งเป้า **+54% ในหนึ่งไตรมาส**
- **Revenue signal ที่ทำให้ deal เกิด:** ARR **$492M** ณ รอบก่อน, ตั้งเป้าแตะ **$1B ARR**, และ enterprise Devin usage โต **50% ต่อเดือน 6 เดือนติด**
- Customer จริง: **Goldman Sachs, Mercedes-Benz, several US government agencies** — ไม่ใช่ startup portfolio อีกแล้ว

## เกิดอะไรขึ้น
วันที่ 12 สิงหาคม 2026 Bloomberg ตี exclusive ว่า **Cognition อยู่ในช่วง early talks กับ investor** สำหรับ funding round ใหม่ที่ valuation อย่างน้อย $40 พันล้านดอลลาร์ — TechCrunch ยืนยันตามในไม่กี่ชั่วโมง พร้อม detail เพิ่ม. ที่น่าสังเกตคือ **รอบก่อน ($1B ที่ $26B) เพิ่งปิดเมื่อ พ.ค.** — 3 เดือนก่อนหน้านี้เอง — ทำให้ Cognition กลายเป็นบริษัทที่ raise 2 รอบใน 90 วันด้วย valuation ที่เพิ่ม 54%

CEO **Scott Wu** บอก TechCrunch หลังรอบ $26B ว่าบริษัทมี **ARR ~$492M** ณ ตอนนั้น พร้อมยืนยันว่า **enterprise usage ของ Devin โต 50% ต่อเดือน ต่อเนื่อง 6 เดือน** — ถ้าตัวเลขนี้ต่อเนื่อง run rate ปัจจุบันควรใกล้ **$1B ARR** ซึ่งเป็น anchor ที่ investor รอบใหม่กำลังใช้เพื่อ justify $40B (คิดเป็น ~40x forward ARR — high แต่ไม่ crazy ในสาย vertical software ที่โต 50% MoM). Customer list ที่บริษัท reference คือ Goldman Sachs, Mercedes-Benz และหน่วยงานรัฐบาลสหรัฐ — คนละ tier กับ startup portfolio ที่ coding agent สาย early ใช้เป็น anchor customer

Product stack ปัจจุบันของ Cognition มี 4 surface: **Devin Desktop** (editor, เดิมชื่อ Windsurf ก่อน rebrand ก.ค.), **Devin Cloud** (autonomous agent), **Devin CLI**, และ **Devin Review**. Cascade agent เดิมของ Windsurf ถูก retire 1 ก.ค. แทนด้วย **Devin Local** — บริษัทรวม product family เป็นแบรนด์เดียวเรียบร้อยภายใน 8 เดือนหลังซื้อ Windsurf

## ทำไมสำคัญ
Signal ที่สำคัญที่สุดไม่ใช่ตัวเลข $40B — **แต่คือความเร็วของ repricing** — 90 วันสำหรับ 54% valuation jump ที่ไม่ใช่ AI hype phase แรก (Cognition มี paying enterprise revenue จริง). เทียบกับ **Cursor** ที่ SpaceX ปิดดีลซื้อ $60B เมื่อ มิ.ย. บน ARR $500M+, ตลาดกำลัง price **coding agent runtime = $30-40 per dollar of ARR** ซึ่งเทียบเท่า Snowflake รอบ IPO ปี 2020

Pattern ที่ควรจดคือ **coding agent เริ่ม bifurcate ชัดเจน**: (1) **IDE-first** (Cursor สาย consumer-y, dev เลือกเอง) vs (2) **cloud-first autonomous** (Devin Cloud, ที่ enterprise procurement ซื้อจากบนลงล่าง). $40B raise ตอกว่า model #2 กำลังชนะในโลก enterprise เพราะ (a) delegated work model ที่ OpenAI Enterprise Signal ยืนยัน (ดู brief #2), (b) VPC deployment + dedicated support ที่ enterprise ต้องการ, (c) audit trail + PR review workflow ที่ compliance ทีมยอมรับได้

**Risk ที่ยังอยู่:** Cognition เผาเงินหนัก (คาด burn rate ~$50-70M/เดือน จาก inference + engineering + GTM), และ **Claude Code + Codex** ที่มาจาก vendor ที่เป็นเจ้าของ model ตัวเองมีความได้เปรียบต้นทุน 40-60% ต่อ token. Cognition ต้อง prove ว่าตัวเองสร้าง product moat (memory, planning, tool orchestration) ที่ premium นี้คุ้มพอ — และรอบ $40B แปลว่าต้อง grow เป็น multi-billion ARR ภายใน 24-36 เดือนถึงจะ justify

## มุม AI Agent Platform
สำหรับ **Builders** ที่สร้าง framework/orchestration ให้ coding agent: Cognition กำลัง set benchmark ที่ **runtime + agent + IDE ต้อง integrate สนิท** — ใครที่ยัง sell แค่ SDK/library ต้อง reposition เป็น application เต็มตัวหรือ deepen embed กับ IDE distributor. **Amp, Aider, Continue** — 4 ปีข้างหน้าจะยากขึ้น

สำหรับ **Users / business** ที่ deploy Devin: pricing ที่ Cognition set (~$500 seat/เดือน + variable execution) แปลว่า ROI ต้องมาจากงานที่ agent ทำ **end-to-end ไม่ใช่ pair programming**. หา metric "PR merged by Devin ต่อสัปดาห์" หรือ "engineer-days saved on migration" — ถ้าตัวเลขไม่ pass 3-5x กลับ subscription cost ภายใน 3 เดือน แปลว่ายัง deploy ผิด (workflow, permission, tool integration ยังไม่พร้อม). สำหรับ **ecosystem** — cloud vendor ต้อง commit ว่า Devin runtime จะเป็น first-class citizen บน platform ตัวเองไหม (AWS Bedrock Agents, Azure AI Foundry) หรือปล่อยให้ Cognition กลายเป็น layer อิสระที่กิน margin

## Sources
- [AI Startup Cognition in New Funding Talks at $40 Billion Value — Bloomberg](https://www.bloomberg.com/news/articles/2026-08-12/ai-startup-cognition-in-new-funding-talks-at-40-billion-value)
- [AI coding startup Cognition reportedly already in talks to raise at $40B valuation — TechCrunch](https://techcrunch.com/2026/08/12/ai-coding-startup-cognition-reportedly-already-in-talks-to-raise-at-40b-valuation/)
- [Cognition Eyes $40 Billion Valuation in Fresh Funding Talks — Benzinga](https://www.benzinga.com/markets/private-markets/26/08/61157025/cognition-eyes-40-billion-valuation-in-fresh-funding-talks)
- [Cognition Seeks Funding at $40B as Devin Revenue Target Reaches $1B — Mezha](https://mezha.net/eng/bukvy/a24cb53d_cognition_seeks_funding/)

---

## Audio script
วันที่ 12 สิงหาคม Bloomberg และ TechCrunch รายงานว่า Cognition บริษัทแม่ของ Devin และ Windsurf กำลังคุย funding round ใหม่ที่ valuation อย่างน้อย 40 พันล้านดอลลาร์. เรื่องน่าตกใจคือรอบก่อนหน้าเพิ่งปิด 1 พันล้านที่ 26 พันล้าน valuation เมื่อพฤษภาคม 90 วันที่แล้วเท่านั้น — repricing 54% ในหนึ่งไตรมาส. เลขที่ทำให้ deal เกิดคือ ARR 492 ล้านที่รอบก่อน และ enterprise Devin usage โต 50% ต่อเดือนต่อเนื่อง 6 เดือน ถ้าตัวเลขนี้ต่อเนื่อง ARR ปัจจุบันควรใกล้ 1 พันล้าน. Customer list ก็ไม่ธรรมดา Goldman Sachs, Mercedes-Benz, และหน่วยงานรัฐบาลสหรัฐหลายแห่ง คนละ tier กับ startup portfolio ปกติ. Pattern ที่เกิดชัดคือ coding agent bifurcate เป็น 2 สาย — IDE-first แบบ Cursor ที่ SpaceX ซื้อไป 60 พันล้าน กับ cloud-first autonomous แบบ Devin Cloud ที่ enterprise procurement ซื้อจากบนลงล่าง — 40 พันล้านของ Cognition ตอกย้ำว่า model ที่ 2 กำลังชนะในโลก enterprise. คำถามที่เหลือคือ Cognition จะสร้าง moat ต่อ Claude Code และ Codex ได้ทันไหม เพราะ vendor ที่เป็นเจ้าของ model เองมีต้นทุน token ต่ำกว่า 40-60%.
