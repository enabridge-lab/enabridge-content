---
date: 2026-09-30
slug: intelligence-explosion-paper-anthropic-openai
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a colossal stone staircase spiraling
  upward into a storm cloud, each step labeled with a rising percentage:
  "1%", "26%", "80%". At the top, a giant hourglass leaks glowing sand
  labeled "TIME LEFT". At the bottom, 22 tiny silhouetted figures in a
  circle raising torches. A red banner reads "INTELLIGENCE EXPLOSION —
  22 SCIENTISTS WARN". Cinematic teal-and-crimson palette, dramatic
  chiaroscuro, sharp contrast for 200px thumbnails, bold text rendering,
  no real human faces, 1:1 aspect. Style of a Wired cover story.
image: images/26-10-01-0616-01-intelligence-explosion-paper-anthropic-openai.png
---

# 22 นักวิจัย AI แถวหน้าเซ็นชื่อร่วม — เตือน "intelligence explosion" อาจเริ่มปี 2028 พร้อมตัวเลขจริงจาก Anthropic ที่ AI เขียนโค้ดแทนมนุษย์แล้ว 80%

## TL;DR
- 22 คนรวม Hinton, Bengio, Jakub Pachocki (OpenAI CSO), Jack Clark (Anthropic co-founder), Eric Horvitz (Microsoft), Dawn Song (Berkeley) ปล่อย paper ผ่าน Cambridge Programme on AI Science & Policy — เตือนว่า agent ที่ทำวิจัย AI ต่อได้ อาจ trigger **intelligence explosion**
- ตัวเลขที่ทำให้ paper น่ากลัวกว่าคำเตือนก่อนหน้า: **AI approved code ใน Anthropic 80%** (พ.ค. 2026, จาก single digit ต้นปี 2025); **R&D task ที่ทำโดย light supervision 1%→26%** ในช่วง มี.ค.–ส.ค. 2026
- Paper ปิดด้วยประโยค: **"Once an intelligence explosion begins, the window for action may close"** — สัญญาณเรียกร้องนโยบายจากคนในบริษัทที่กำลังสร้างมันเอง

## เกิดอะไรขึ้น
สัปดาห์ก่อน DevDay ของ OpenAI, Cambridge Programme on AI Science & Policy ปล่อย working paper ชื่อ "Preparing for the Intelligence Explosion" — ที่แปลกกว่าคือ list ของ author. มี Geoffrey Hinton กับ Yoshua Bengio ก็ไม่แปลก แต่ signature ที่มา with **Jakub Pachocki** (Chief Scientist ของ OpenAI), **Jack Clark** (co-founder ของ Anthropic), **Eric Horvitz** (Microsoft Chief Scientific Officer), และ **Dawn Song** จาก UC Berkeley — คนที่ทำงานอยู่ในบริษัทที่กำลัง scale frontier lab อยู่ตอนนี้

Paper วางเคสว่า agent ที่ทำ AI research อัตโนมัติกำลัง approach threshold ใหม่: ไม่ใช่แค่ทำ coding task หรือ copy-paste literature review — แต่กำลังจะทำ **months-long AI research project** โดยไม่ต้องมีมนุษย์เข้าไปแทรก. Extrapolation จากข้อมูลปัจจุบัน (ที่มาจากรายงาน METR + internal metrics ของ lab) ชี้ว่าเหตุการณ์นี้อาจเกิดขึ้น **ก่อน mid-2028** — ไม่ใช่ 2035 ตามที่ Kurzweil เคยพูด

ตัวเลขที่เป็นเนื้อของ paper: **AI-approved code ที่ Anthropic โต จาก single digit (ต้นปี 2025) เป็น 80% (พ.ค. 2026)** — 80% ของ commit ที่ push เข้า main ผ่านการรีวิวโดย Claude เอง. **Share ของ R&D task ที่ทำโดย AI แบบ light supervision** โต **1%→26%** ในช่วง **มี.ค.–ส.ค. 2026** — 5 เดือน. ถ้ากราฟยังชันแบบเดียวกัน 40% ต้นปี 2027 และ >70% กลางปี 2027 คือฐานที่ paper คำนวณ

Recommendation ของ paper ไม่ใช่ moratorium (ต่างจากคำร้อง 2023) — แต่เรียกร้องให้รัฐบาลตั้ง monitoring infrastructure, forced disclosure ของ automated research capability, และ **circuit breaker mechanism** ที่ lab ต้องมี. Paper ปิดด้วยประโยคที่ chill: "Once an intelligence explosion begins, the window for action may close."

## ทำไมสำคัญ
Paper นี้ต่างจาก open letter ปี 2023 ตรงที่ **มันมีตัวเลขจริงจากภายใน** — และตัวเลขนั้นมาจาก signatory เอง (Anthropic co-founder เอา metric จาก Anthropic มาแปะ). ที่ผ่านมา discourse เรื่อง AI safety ถูกวิจารณ์ว่าเป็น "theoretical scenario" — paper นี้เปลี่ยน conversation เพราะ 80% กับ 26% ไม่ใช่ prediction, มันคือ current state

Signal ที่ 2 คือ **political shift**: การที่ Chief Scientist ของ OpenAI (Pachocki) กับ Anthropic co-founder (Clark) เซ็นชื่อพร้อมกัน = สัญญาณว่า internal culture ของ lab กำลังแตกออกจาก marketing story ของ CEO ทั้งสองข้าง. Altman + Amodei ยัง push accelerationist narrative — แต่ Chief Scientist และ co-founder เริ่มพูดต่างออก. คล้ายเหตุการณ์ Ilya Sutskever ปี 2024

Signal ที่ 3 คือ **timing**: paper ออกก่อน DevDay 1 วัน + ก่อน Anthropic IPO prospectus leak 2 วัน. Coincidence หรือไม่ — แต่ผลลัพธ์คือ regulator ทั่วโลก (EU AI Act phase 2, UK AISI, US AI Safety Institute) จะยกตัวเลข 80% ในการเจรจากับ lab ในไตรมาส Q4 นี้

## มุม AI Agent Platform
**Builders** — ถ้าคุณสร้าง agent framework, ตัวเลข 26%→70% ใน 12 เดือนของ R&D automation หมายความว่า **framework ที่คุณเขียนเองอาจถูก AI-generated framework แซง** ในรอบต่อไป. Bet ที่ปลอดภัยกว่าคือทำ orchestration layer / observability / safety runtime — layer ที่ AI ยังไม่แตะได้ง่าย ๆ. **Users / business** ที่ deploy agent ในองค์กร: paper เป็น **material ให้ risk committee ใหม่** — เมื่อ Anthropic co-founder เซ็นเอกสารว่า "existential risk" ไม่ใช่ hypothetical, ทุก vendor RFP ตั้งแต่ Q4 นี้จะโดนถามคำถาม safety จริงจัง ไม่ใช่ checkbox. **Ecosystem** — Microsoft Chief Scientist (Horvitz) เซ็นชื่อ = Microsoft ในฐานะ investor ของ OpenAI + partner ของ Anthropic กำลังส่งสัญญาณ dual-hedge. Cloud provider ที่ยังไม่มี "AI safety tier" ในสัญญา enterprise (compute quota, kill switch, monitoring) จะโดนบีบให้ประกาศภายใน 6 เดือน

## Sources
- [Hinton, Bengio and AI lab scientists warn of an intelligence explosion — The Next Web](https://thenextweb.com/news/intelligence-explosion-paper-hinton-bengio-pachocki-clark)
- ["Window for action may close" if AI begins improving itself, AI pioneers warn — Axios](https://www.axios.com/2026/09/28/ai-pioneers-intelligence-explosion)
- [Anthropic, OpenAI and the Intelligence Explosion Paper — FourWeekMBA](https://fourweekmba.com/ai-anthropic-openai-intelligence-explosion-working-paper/)
- [Intelligence Explosion Paper: What 22 AI Leaders Warn — CellCog](https://cellcog.ai/blog/intelligence-explosion-paper/)

---

## Audio script
ข่าวใหญ่วันนี้ครับ. เมื่อวันจันทร์ที่ผ่านมา Cambridge Programme on AI Science and Policy ปล่อย paper ชื่อ Preparing for the Intelligence Explosion. ที่ทำให้ paper นี้ต่างจาก open letter อื่น ๆ คือ 22 ชื่อที่เซ็นร่วม. มี Geoffrey Hinton กับ Yoshua Bengio ตามคาด แต่ที่ไม่คาดคือ Jakub Pachocki หัวหน้านักวิทยาศาสตร์ของ OpenAI และ Jack Clark ผู้ร่วมก่อตั้ง Anthropic เซ็นชื่อด้วย. คนที่ทำงานอยู่ในบริษัทที่กำลังสร้างสิ่งที่เขาเตือน. Paper วางตัวเลขจริงบนโต๊ะ. หนึ่ง โค้ดที่ Anthropic push เข้า main ในเดือน พ.ค. 2026 ผ่านการรีวิวโดย Claude เอง 80 เปอร์เซ็นต์ ต้นปี 2025 ตัวเลขนี้อยู่แค่หลักหน่วย. สอง งานวิจัย R&D ที่ทำโดย AI แบบ light supervision จาก 1 เปอร์เซ็นต์ ในเดือน มี.ค. เป็น 26 เปอร์เซ็นต์ ในเดือน ส.ค. — 5 เดือน. ถ้ากราฟยังชัน paper บอกว่า months-long AI research project จะทำอัตโนมัติเต็มตัวก่อน mid-2028. เขาปิด paper ด้วยประโยค Once an intelligence explosion begins, the window for action may close. Impact ต่อ AI Agent Platform สำคัญมาก. ถ้าคุณสร้าง framework agent เอง คำเตือนคือ framework ของคุณอาจถูก AI-generated framework แซงในรอบต่อไป ต้องขยับไปทำ orchestration observability กับ safety runtime แทน. ถ้าคุณเป็น business ที่ deploy agent ในองค์กร paper นี้เป็นของขวัญให้ risk committee ยื่นให้ vendor คุยเรื่อง governance จริงจัง ไม่ใช่ checkbox. และสัญญาณที่คมที่สุด — Chief Scientist ของ OpenAI กับ co-founder ของ Anthropic เริ่มพูดต่างจาก CEO ของตัวเอง เหมือน Ilya Sutskever เมื่อปี 2024 ครับ.
