---
date: 2026-07-19
slug: kimi-k3-chip-48h-autonomous-agentic
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  A 4mm-square glowing microchip sits alone on a dark studio pedestal, backlit
  in cool cyan; three bold editorial headlines float above it in slab-serif:
  "48 HOURS", "NO CADENCE. NO SYNOPSYS.", "8,700 TOKENS/S". A tiny Kimi K3
  wordmark etched into the die surface. Isometric composition, deep navy and
  amber palette, sharp typography readable at 200px thumbnail, 1:1 aspect,
  no real human faces.
image: images/26-07-19-0609-01-kimi-k3-chip-48h-autonomous-agentic.png
---

# Kimi K3 ออกแบบชิปของตัวเองใน 48 ชั่วโมง — และ EDA duopoly หายไป $15.8B ในหนึ่งวัน

## TL;DR
- Moonshot AI ปล่อย **Kimi K3** — open-weight MoE 2.8 ล้านล้าน parameter — พร้อม demo ว่า model ออกแบบชิปทำงานได้จริงใน **single 48-hour autonomous run** โดยใช้เครื่องมือ open-source ล้วน
- ชิปขนาด **4 mm²** ที่ 100 MHz, throughput > **8,700 tokens/s** ใน simulation, ทำ RTL → tape-out simulation ไม่แตะ Cadence หรือ Synopsys เลย
- Cadence + Synopsys ราคาหุ้นตก ~9% วันเดียว รวม **market cap หาย $15.8B** — Synopsys คนเดียวหาย $6.3B
- Full weights ออก **27 กรกฎาคม 2026**; benchmark AA-Briefcase (agentic) K3 ได้อันดับ 2 (1,527), ตามหลังแค่ Claude Fable 5 Max และ GPT-5.6 Sol Max

## เกิดอะไรขึ้น
กลางสัปดาห์ที่ผ่านมา Moonshot AI ปล่อย Kimi K3 — model open-weight ตัวใหญ่ที่สุดในโลกด้วยพารามิเตอร์ 2.8 ล้านล้าน architecture แบบ Mixture-of-Experts พร้อม Kimi Delta Attention และ context window 1 ล้าน token. แต่สิ่งที่ทำให้ Wall Street ตกใจไม่ใช่ตัวเลข benchmark — เป็น demo ที่แนบมา: K3 ถูกปล่อยให้ทำงานเดี่ยว 48 ชั่วโมง และตอนออกมา มันสร้าง **ชิปที่ทำงานได้จริง** ตัวหนึ่ง — chip ที่ออกแบบมาเพื่อรัน nano-version ของตัวเองบน architecture เดียวกัน

ตัวชิปเป็น 4 mm² บน Nangate 45nm Open Cell Library ปิด timing ที่ 100 MHz มี 1.46M standard cells, SRAM 0.277 MB และ INT4 MAC array พร้อม fused dequantization. K3 อ่าน spec, ตัดสินใจ architecture, เขียน RTL, รัน synthesis, place & route, ทำ verification loop, iterate จนผ่าน — ทุกอย่างในหน้าต่างเดียว 48 ชั่วโมงโดยใช้ **open-source EDA ล้วน**. ไม่มี Cadence Innovus, ไม่มี Synopsys Design Compiler, ไม่มี Mentor Calibre

ปฏิกิริยาของตลาดคมชัด: วันศุกร์ Cadence และ Synopsys ราคาลง ~9% รวมกันสูญ **market cap $15.8B** — Synopsys คนเดียวหายไป $6.3B. BNP Paribas ออก note ว่า "buy the dip" ทันที เพราะ 45nm node ที่ K3 ทำนั้นล้าหลังกว่า frontier (3nm, 2nm) หลาย generation และ tool proprietary ที่ Cadence กับ Synopsys เป็นเจ้าของยังฝังลึกในสายพาน AI accelerator ระดับสูง. แต่ก็เห็นชัดว่า market ไม่ได้ pricing "รอ 10 ปี" ให้เกิด — pricing "รอเดือน" หรือ "รอไตรมาส"

## ทำไมสำคัญ
เรื่องนี้เป็น proof point ของ **long-horizon agentic capability** ที่แข็งแรงที่สุดตั้งแต่มีคำว่า agent. งาน chip design ต้องรักษา context หลายชั้น ตัดสินใจซ้อน ๆ ที่พึ่งกัน iterate เมื่อ verification fail แล้วย้อนไปแก้ RTL ต้นทาง — 48 ชั่วโมงของงานที่ต้องเข้าใจ toolchain, semiconductor physics, และ verification methodology พร้อมกัน. เดิมทีคนตั้งคำถามว่า agent จะทำงาน "หลายวัน" ได้ไหมโดยไม่เพี้ยน; K3 ตอบไปเรียบร้อยว่าได้

Signal ที่ควรอ่านจากตลาด: analyst pricing ว่า **software moat ของ EDA อาจไม่ป้องกัน 45nm-tier ได้แล้ว**. Node นี้ครอบคลุมชิป industrial IoT, microcontroller, MEMS controller — ตลาดที่คนส่วนใหญ่มองข้าม แต่รวมกันปีละหลายหมื่นล้านดอลลาร์. ถ้า open-source EDA + agentic model กลายเป็นสูตรทำ ASIC ราคา $50K ที่เคย $500K การกระจายการออกแบบชิปจะเปลี่ยนไปเหมือน 3D printing เปลี่ยน prototyping — ไม่ใช่ทั้งอุตสาหกรรม แต่ตัดหางออกจำนวนมาก

เทียบกับ Cadence AuraStack ที่เพิ่งประกาศเมื่อสัปดาห์ก่อน (Enabridge สรุปไปเมื่อ 26-07-18) — Cadence กำลังพยายามฝัง agent เข้าใน stack ของตัวเองเพื่อป้องกันตำแหน่ง. K3 บอกว่า agent ที่นั่งอยู่ **นอก** stack กำลังจะโค่นชั้นล่างของมันได้เอง. ใครที่ยังคิดว่าจีนตามหลัง frontier ห่างเป็นปี ๆ ต้องรีบคำนวณใหม่ — Axios พาดหัวว่า "China just erased America's AI lead"

## มุม AI Agent Platform
**Builders** ที่กำลังสร้าง agent framework หรือ orchestration layer เห็นชัดเลยว่ามาตรฐาน "how long can an agent run coherently" ขยับจากหน่วยชั่วโมงเป็นหน่วยวัน — retry, checkpointing, memory compaction ต้องออกแบบใหม่. **Users / business** ในสาย hardware, EDA, semiconductor consulting ต้องรีบเก็บ data point นี้เข้า strategic review — ไม่ใช่เพื่อ replace แต่เพื่อทำความเข้าใจว่า commodity layer ของตัวเองอยู่ตรงไหน. **Ecosystem** — open-source EDA (OpenROAD, Yosys, ORFS) จะได้ traction ใหม่ทันที; cloud vendor ที่รัน MoE ขนาด 2.8T (AWS, Azure, Alibaba, Tencent) ได้ workload spec ใหม่ที่ต้อง optimize; Anthropic, OpenAI, Google จะต้องตอบว่า long-horizon agentic demo ของตัวเองอยู่ไหน — เพราะ narrative "closed frontier ยัง lead" เริ่มไม่ผูกกับ evidence

## Sources
- [Kimi K3 Tech Blog: Open Frontier Intelligence](https://www.kimi.com/blog/kimi-k3)
- [Kimi K3 Built A Chip In Just 48 Hours (wccftech)](https://wccftech.com/kimi-k3-built-a-chip-in-48-hours-over-8700-tokens-s-as-china-delivers-2-8-trillion-ai-model/)
- [Cadence & Synopsys slide as Kimi K3 designs chip in 48h (Yahoo/Investing)](https://finance.yahoo.com/technology/ai/articles/cadence-synopsys-slide-kimi-k3-162824133.html)
- [Synopsys loses $6.3 billion following Kimi K3 chip-design demonstration](https://ts2.tech/en/synopsys-nasdaqsnps-loses-6-3-billion-following-kimi-k3-chip-design-demonstration/)
- [China just erased America's AI lead (Axios)](https://www.axios.com/2026/07/17/china-ai-kimi-k3-open-source-anthropic-opus)

---

## Audio script
สัปดาห์นี้ Moonshot AI จากจีนปล่อย Kimi K3 model open-weight ตัวใหญ่ที่สุดในโลก 2.8 ล้านล้าน parameter สถาปัตยกรรม Mixture-of-Experts พร้อม context window ล้าน token. แต่สิ่งที่ทำให้ Wall Street สะดุ้งไม่ใช่ตัวเลข parameter หรือ benchmark. เป็น demo ที่แนบมา — K3 ถูกปล่อยให้ทำงานคนเดียว 48 ชั่วโมง แล้วออกมาพร้อมชิปที่ทำงานได้จริง ชิปสี่ตารางมิลลิเมตร ทำงานที่ 100 เมกะเฮิรตซ์ throughput เกิน 8,700 token ต่อวินาที ในงานคือรัน nano version ของตัวเอง. สิ่งสำคัญคือ K3 ทำทั้งกระบวนการตั้งแต่ RTL ไปจนถึง tape-out simulation โดยใช้เครื่องมือ open-source ล้วน ไม่แตะ Cadence, ไม่แตะ Synopsys เลยแม้แต่ขั้นตอนเดียว. ผลคือ Cadence กับ Synopsys ราคาหุ้นตกประมาณ 9% ในวันเดียว รวมกันหาย market cap 15,800 ล้านดอลลาร์. นี่คือ proof point ของ long-horizon agentic capability ที่แข็งแรงที่สุดตั้งแต่วงการมี agent — งานที่ต้อง maintain context หลายชั้น ตัดสินใจซ้อน iterate เมื่อ verify fail — agent ทำได้ต่อเนื่องสองวันโดยไม่เพี้ยน. Analyst เตือนว่า node 45 นาโนที่ K3 ทำอยู่ยังห่างจาก frontier ที่ 3 กับ 2 นาโนหลาย generation — แต่ตลาด IoT กับ microcontroller ที่ใช้ node นี้รวมปีละหลายหมื่นล้าน; ถ้า ASIC ราคาลดจาก 500,000 เหลือ 50,000 ดอลลาร์ การกระจายอำนาจการออกแบบชิปจะเปลี่ยนไปเลย. Full weights ของ K3 ปล่อย 27 กรกฎาคมนี้ — คนที่รอ open-frontier model พร้อม agent capability ระดับ long-horizon เตรียมตัวรับได้เลย
