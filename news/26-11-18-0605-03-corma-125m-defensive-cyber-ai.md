---
date: 2026-11-18
slug: corma-125m-defensive-cyber-ai
topic: use-case
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a dark cyber defense war room with
  a translucent dome shielding a server rack. Inside the dome, robot agents
  patrol shoulder-to-shoulder with silhouetted human analysts. Above the
  scene, three big stacked numbers glow: "$125M SERIES A",
  "$1B VALUATION", "90 DAYS". A side panel reads "DEFENSIVE AI AGENTS" and
  a small plaque on the wall shows "UNIT 8200 x DEEPMIND". Clean editorial
  style, deep indigo and neon cyan palette, high contrast so numbers stay
  readable at 200px thumbnail, 1:1 aspect, no real human faces
  (silhouettes OK).
image: images/26-11-18-0605-03-corma-125m-defensive-cyber-ai.png
---

# Corma ขึ้น unicorn ใน 90 วัน — NEA นำ $125M อัด AI agent ฝั่ง defense เข้า SOC แทน analyst

## TL;DR
- Corma สตาร์ตอัปอิสราเอลปิด Series A $125M นำโดย NEA (Sequoia + Khosla + Coatue ลงต่อ) ที่ valuation $1B — รวมเงิน $185M ใน 90 วัน หลังออกจาก stealth เดือน ส.ค.
- เทรน foundation model ของตัวเอง สำหรับ cyber defense แล้ว deploy เป็น AI workforce ทำงานร่วมกับ SOC analyst — ไม่ใช่ copilot แต่เป็น agent ที่รัน playbook จริง
- Team ผสม Google/DeepMind researcher กับ Unit 8200 — บริษัทอ้าง cost งาน security ลดเกิน 90% (ยังไม่มี third party verify)

## เกิดอะไรขึ้น
วันที่ 16 พฤศจิกายน Corma — สตาร์ตอัปอิสราเอลที่ยังไม่มีใครรู้จักเมื่อสิงหาคม — ประกาศ Series A $125M ที่ valuation $1B ทำให้เป็น unicorn ใน 90 วันหลังออกจาก stealth รอบนี้นำโดย NEA โดย Sequoia, Khosla Ventures กับ Coatue ที่ลงใน seed $60M รอบก่อน ก็ตามเข้าเพิ่มทั้งหมด รวม funding $185M แล้ว สิ่งที่ Corma ขายไม่ใช่ copilot ไม่ใช่ SIEM ตัวใหม่ — คือ foundation model ที่ตัวเองเทรน specifically สำหรับ cyber defense แล้ว deploy ออกมาเป็น AI workforce ทำงานร่วมใน SOC (Security Operations Center) ของลูกค้า

Team ของ Corma ผสม researcher จาก Google กับ DeepMind เข้ากับ cyber operator จาก Unit 8200 ของกองทัพอิสราเอล — ซึ่งเป็น combo ที่ VC ยุคนี้พร้อมจ่าย premium อย่างชัดเจน Agent ของ Corma ไม่ได้แค่ flag alert แต่สืบ root cause, correlate กับ threat intel, เขียน remediation playbook แล้วรัน action ใน EDR/firewall/identity system เอง โดย analyst human เป็นคน supervise เฉพาะ case ที่ agent uncertainty สูง บริษัทอ้างว่า security task cost ลดลงกว่า 90% (ตัวเลขนี้เป็นของบริษัท ไม่มี third party audit)

ที่น่าสังเกตคือ positioning ชัดว่า "defensive" ไม่ใช่ "red team" — ในขณะที่สตาร์ตอัปอื่นอย่าง Dreadnode (ที่ CrowdStrike ซื้อไปเมื่อสองสัปดาห์ก่อน) เล่นฝั่ง offense กับ simulation Corma ตั้งใจวางตัวเองเป็น partner ของ SOC incumbent ไม่ใช่ตัวแทน

## ทำไมสำคัญ
Cyber defense กำลังจะเป็น vertical ที่ "agent-first" เป็นค่า default ไม่ใช่ feature เสริม — เพราะเหตุผลสามข้อ หนึ่ง ปริมาณ alert ที่ SOC ต้องรับต่อวันโตเร็วกว่าที่ hire analyst ได้ สอง attacker ฝั่งตรงข้ามใช้ agent generate payload ไว้แล้ว ต้องมี speed matching จากฝั่ง defense สาม cost ของ SOC analyst ที่ qualified ทะลุ $200K/ปีในสหรัฐ ทำให้ math ของการเอา agent มารัน playbook ซ้ำ ๆ คุ้มเร็วมาก Corma เข้ามาในจังหวะที่ตลาดพร้อมจ่าย

สิ่งที่ Corma จะต้องพิสูจน์คือ — การเทรน foundation model เองคุ้มกับ cost หรือเปล่า เทียบกับคู่แข่งที่ fine-tune บน Claude หรือ GPT-5 แล้วเสริม RAG จาก threat intel ข้อดีของ model ตัวเอง คือ latency ต่ำ control ได้เต็ม และ compliance กับ CISO ที่ไม่อยาก leak data ออกไปที่ public API แต่ cost การเทรนสูง และ frontier model เองพัฒนาเร็วมาก Corma ต้องพิสูจน์ว่า vertical model ของตัวเองยัง compound ได้เร็วพอ

## มุม AI Agent Platform
สำหรับ **Builders** — pattern ของ Corma (vertical foundation model + AI workforce + human-in-the-loop เฉพาะที่ uncertain) เป็น blueprint ที่ vertical อื่นจะลอก ถ้าคุณกำลังสร้าง agent ใน domain ที่ data เฉพาะทาง (medical, legal, industrial safety) การถือ model ตัวเองไม่ใช่ overhead แต่กลายเป็น moat คำถามที่ต้องตอบตัวเองได้คือ data proprietary ที่คุณมี พอสำหรับเทรน model ที่ beat frontier model ในงานเฉพาะได้ไหม

สำหรับ **Users / business** — CISO ที่กำลังคุย POC กับ cyber agent vendor ตอนนี้ ต้องถามให้ชัดว่า foundation layer ของเขาอยู่ที่ไหน ถ้าเป็น frontier model ล้วน security guarantee ขึ้นกับ roadmap ของ OpenAI หรือ Anthropic ถ้าเป็น vertical model ของ vendor control ได้มากกว่า แต่ต้องประเมินว่า vendor มี data moat จริงหรือเปล่า Corma ชนะเพราะ team Unit 8200 มี data กับ playbook ที่คนทั่วไปเข้าไม่ถึง — คนอื่นที่ไม่มี advantage แบบนี้อาจไม่ควรเดิน path เดียวกัน

## Sources
- [Cyber startup Corma goes from stealth to unicorn in just three months with $125 million Series A — Calcalist Tech](https://www.calcalistech.com/ctechnews/article/bjiqapu0me)
- [Corma Reaches $1 Billion Valuation Through AI Cybersecurity — Jerusalem Post](https://www.jpost.com/business-and-innovation/tech-and-start-ups/article-915220)
- [Corma Raises $125M at $1B Valuation for Cyber Defense AI — Isra-tech](https://www.isra-tech.net/corma-raises-125-million-at-1-billion-valuation-for-defensive-cybersecurity-ai/)
- [Corma Series A: $125M at a $1B Valuation, Led by NEA — SCommerce](https://www.scommerce.com/corma-series-a/)

---

## Audio script
ข่าวจากอิสราเอล บริษัทชื่อ Corma เพิ่งปิด Series A หนึ่งร้อยยี่สิบห้าล้านดอลลาร์ ที่ valuation หนึ่งพันล้าน นำโดย NEA โดยที่ Sequoia, Khosla, Coatue ที่ลง seed ตอนสิงหาคม ก็ลงต่อทั้งหมด บริษัทนี้ขึ้น unicorn ในเวลาเก้าสิบวันหลังออกจาก stealth เท่านั้น สิ่งที่ Corma ทำไม่ใช่ copilot ไม่ใช่ SIEM แต่เป็น foundation model ที่เทรนเองสำหรับ cyber defense แล้ว deploy เป็น AI workforce ทำงานใน SOC ของลูกค้าร่วมกับ analyst

team ผสม researcher จาก Google กับ DeepMind เข้ากับ operator จาก Unit 8200 ของกองทัพอิสราเอล ทำให้ได้ premium จาก VC agent ของ Corma ไม่ได้แค่แจ้งเตือน แต่สืบ root cause เขียน playbook แล้วรัน action ใน EDR กับ firewall เอง โดยคนเข้ามา supervise เฉพาะเคสที่ไม่แน่ใจ บริษัทอ้างว่า cost งาน security ลดเกินเก้าสิบเปอร์เซ็นต์ ซึ่งยังต้องรอ third party ยืนยัน สัญญาณสำหรับ builders ใน vertical อื่นคือ การถือ foundation model ของตัวเองเริ่มเป็น moat ไม่ใช่ overhead แต่คุณต้องมี proprietary data ที่ beat frontier ในงานเฉพาะได้จริง สำหรับ CISO ต้องเริ่มถาม vendor ว่า foundation layer เขาอยู่ที่ไหน
