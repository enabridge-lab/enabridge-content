---
date: 2026-05-08
slug: anthropic-spacex-colossus-300mw-orbital-compute
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: A bold editorial illustration in deep navy and warm cream — at center, a stylized Anthropic spiral logo in cream glows with light, while a SpaceX rocket silhouette in slate gray launches diagonally from lower-left through the frame leaving a coral exhaust trail. Above the rocket trail, four NVIDIA GPU board icons in flat-vector style are arranged in a row labeled "220K GPUs". A bright coral headline "MEMPHIS → ORBIT" arches over the top, with "300 MW" rendered very large in cream sans-serif on the lower-right. Subtle Earth-curvature line at the bottom hints at orbital ambition. Editorial flat-vector style, dramatic spotlight, slate navy + cream + coral + electric teal palette, no human figures, logos crisp for 200px thumbnail readability, 1:1 aspect ratio.
image: images/26-05-08-0927-02-anthropic-spacex-colossus-300mw-orbital-compute.png
---

# Anthropic เซ็นดีล SpaceX กิน Colossus 1 ทั้ง data center — 300MW + 220K GPU + เปิดทาง compute ในวงโคจร

## TL;DR
- 6 พ.ค. 2026 Anthropic ประกาศดีลใช้ compute ทั้งหมดของ Colossus 1 ที่ Memphis ของ SpaceX — 300+ MW + 220,000+ Nvidia GPU available ภายใน 1 เดือน financial term ไม่เปิดเผย
- Anthropic + SpaceX ระบุ "expressed interest" จะร่วมพัฒนา orbital AI compute หลาย gigawatt ในอวกาศ — เป็น declared statement แรกของ frontier lab ที่ commit ถึง space-based AI infra
- ดีลนี้พ่วงมากับการขยาย Claude Code limit + จับคู่กับดีล Anthropic-Google TPU $200B และ Anthropic-Blackstone-Goldman venture $1.5B — รวมเป็น signal ว่า Anthropic ขยับจาก "compute-starved underdog" เป็น "multi-cloud + multi-orbit lab"

## เกิดอะไรขึ้น

วันที่ 6 พ.ค. 2026 Anthropic ประกาศดีลที่หลายคนไม่คาดถึงเลย — ใช้ compute ทั้งหมดของ Colossus 1 data center ที่ Memphis ของ SpaceX (ใต้ holding xAI/SpaceX) ภายใน 1 เดือน Anthropic จะมี 300+ megawatt ของ capacity บวก 220,000+ Nvidia GPU พร้อมให้ Claude วิ่งจริง ตัวเลขที่ใหญ่กว่าการขยาย AWS Trainium ของปีที่แล้วทั้งปี Colossus 1 อยู่ใน Boxtown, Memphis — โรงงาน Electrolux เก่าที่ Musk ใช้สร้าง "world's largest AI supercomputer" ในปี 2024 เพื่อ train Grok ของ xAI ตอนนี้ Anthropic ที่เป็นคู่แข่งหลักของ xAI กลับเข้ามากินที่นั่งทั้งโต๊ะ

จุดที่ไม่มีใครคาดถึงคือ ใน press release ของทั้งสองฝั่ง พูดถึง "exploratory partnership" ที่ Anthropic + SpaceX จะร่วมพัฒนา orbital compute capacity หลาย gigawatt ในวงโคจร ซึ่งเป็น declared statement แรกของ frontier lab ที่ commit ถึง space-based AI infrastructure อย่างจริงจัง — Bezos กับ Project Kuiper เคย hint แต่ไม่เคย sign ดีลแบบนี้ ส่วน Microsoft กับ Google ยังตอบสนใจระดับ R&D เท่านั้น แปลว่า: ใน 5 ปีข้างหน้า ถ้าโลกจะมี data center ในอวกาศ Anthropic เป็นชื่อแรกที่จะเล่น

ขนาดของดีล financial ไม่เปิดเผย แต่ scale บอกตัวเอง — 220K Nvidia GPU ที่ราคา ~$30K/GPU = $6.6B ของ hardware capex ที่ SpaceX ลงทุนไปแล้ว Anthropic เซ็น lease/usage contract ที่ระยะเวลายังไม่ระบุ พ่วงประกาศวันเดียวกันว่า Claude Code limit ของ Pro และ Max จะขยาย "อย่างมีนัยสำคัญ" — แปลว่า Anthropic compute-starved อยู่จริง ก่อนที่ดีลนี้จะปิด เห็นได้จากการ throttle Claude Sonnet/Opus หลายรอบในไตรมาสที่ผ่านมา

ที่น่าจับตาคือ context — Anthropic เพิ่ง close ดีล Google TPU $200B (29 เม.ย.), เปิด venture firm กับ Blackstone + Goldman Sachs $1.5B (4 พ.ค.), และตอนนี้ลงดีล SpaceX อีก ทั้งหมดในระยะ 10 วัน ผู้บริหาร Anthropic ที่เคย narrative ตัวเองเป็น "small lab" ตอนนี้กำลังกำกับ infrastructure portfolio ที่กว้างกว่า OpenAI ที่พึ่ง Azure อย่างเดียว — และไม่ใช่ฝั่ง consumer ที่ Anthropic แข่ง แต่เป็น enterprise + agent stack ที่ต้องการ inference burst ใหญ่ ๆ

## ทำไมสำคัญ

ที่ดีลนี้ใหญ่ที่สุดคือ Musk ยอมขาย Colossus 1 ให้คู่แข่งของ xAI อย่างเปิดเผย — สอง interpretation: หนึ่ง xAI กำลัง build Colossus 2 ที่ใหญ่กว่า (rumor ว่าใน Tennessee อีกแห่ง 1 GW+) จึงไม่ต้องการ Colossus 1 อีก สอง SpaceX/xAI ต้องการ cash flow ทันทีเพื่อ fund อย่างอื่น (Starship V3, Neuralink scale, หรือ Twitter/X) สำหรับ industry ภาพรวมคือ frontier lab ทุกค่ายตอนนี้ต้อง "rent compute from competitors" เพราะไม่มีใครสร้างได้ทันความต้องการตัวเอง — pattern เดียวกับ Netflix รัน บน AWS ของ Amazon ในยุค 2010 ที่ Amazon เปิดตัว Prime Video เป็นคู่แข่งโดยตรง

ที่น่าสนใจคือ orbital compute angle — ในวงโคจรไม่มีปัญหา cooling (vacuum + radiator), ใช้ solar 24/7 (ไม่ต้องจ่าย power utility), และ latency ของ training (vs inference) ไม่สำคัญ ถ้า SpaceX deploy data center ใน LEO ขนาด 1 GW ในปี 2030–2032 เกมเปลี่ยน: power grid bottleneck ที่ทุก hyperscaler เจอใน Virginia, Phoenix, Texas จะหายไปทันที Anthropic ที่ commit เป็นรายแรก = first-mover ใน orbital frontier ราคาที่ตีตอนนี้คือ "Anthropic จะมี compute ที่ scale ถูกกว่า peer ในอีก 5 ปี" — กระทบ valuation ระดับ trillion-dollar

อีกประเด็น: Anthropic ตอนนี้มี compute ใน 4 ค่ายขนานกัน — Amazon Trainium, Google TPU, Microsoft Azure (เก่า), และ SpaceX/Nvidia GPU; ไม่ vendor lock เลย ซึ่งทำให้ Claude routing optimization (ส่ง workload ไปยัง substrate ที่ถูกที่สุด) เป็น core competency ที่ OpenAI (Azure exclusive) ทำไม่ได้ pattern นี้คือคืน "AI = compute arbitrage" ที่ Stratechery เขียนถึงตั้งแต่ 2023 — ใครจัดการ compute portfolio ดีกว่า ชนะ

## มุม OpenBridge

ไม่ direct เกี่ยว แต่ adjacent insight สำคัญ: (1) **ดีล multi-cloud ของ Anthropic = ลูกค้า OpenBridge จะมี Claude แบบ regional + sovereign more options** ปลายปีนี้ ลูกค้า Thai enterprise ที่ pick Claude เพราะ data residency จะมีทางเลือกใน Singapore (Google TPU), AWS Asia (Trainium), และอาจ Memphis (GPU) — OpenBridge connector ที่ route AI call ตาม customer policy (ไม่ใช่ fixed endpoint) จะเป็น feature ที่ขาย B2B Thai ได้ตรง ๆ (2) **300MW + 220K GPU = Anthropic enterprise tier จะมี throughput ที่ใหญ่ขึ้น** Claude API ที่ rate limit ลูกค้า OpenBridge เจอใน Q1–Q2 จะเริ่ม unblock — แปลว่า workflow ที่เคย split เป็น batch จะรัน real-time ได้ pricing ของ OpenBridge tier ที่ pass-through Anthropic ควร refresh ในเดือน มิ.ย. (3) **orbital compute = อย่ารีบ FOMO** กว่าจะ commercial production คือ 2030+ แต่ในเอกสาร investor ของ OpenBridge ที่ pitch "AI infra-agnostic integration layer" สามารถใส่ slide ว่า "no matter where compute lives — ground, cloud, orbit — connector ของเราเชื่อมที่ data ลูกค้าอยู่" เป็นภาพ futuristic ที่ ฺBOI/VC ชอบ

ที่จะ watch: ถ้า Claude Code limit ขยายจริงตามที่ Anthropic บอก dev/agent ที่ใช้ OpenBridge ผ่าน Claude Code MCP integration จะเข้มข้นขึ้น — log usage spike ใน Q2 จะเป็น early indicator ของว่า dealflow Claude-driven ของเราโตหรือไม่

## Sources
- [Anthropic taps SpaceX AI data center to expand Claude capacity | Invezz](https://invezz.com/ca/news/2026/05/06/anthropic-taps-spacex-ai-data-center-to-expand-claude-capacity/)
- [Anthropic to use all of SpaceX-xAI's Colossus 1 data center compute | DCD](https://www.datacenterdynamics.com/en/news/anthropic-to-use-all-of-spacex-xais-colossus-1-data-center-compute/)
- [Anthropic, SpaceX announce compute deal that includes space development | CNBC](https://www.cnbc.com/2026/05/06/anthropic-spacex-data-center-capacity.html)
- [New Compute Partnership with Anthropic | xAI](https://x.ai/news/anthropic-compute-partnership)

---

## Audio script
สวัสดีครับโย วันนี้เรื่องที่ไม่มีใครคาดถึงเลย Anthropic ประกาศเมื่อ 6 พ.ค. ว่าจะใช้ compute ทั้งหมดของ Colossus 1 data center ที่ Memphis ของ SpaceX 300 megawatt บวก 220 พัน Nvidia GPU พร้อมใน 1 เดือน Colossus 1 เคยเป็นโรงงาน Electrolux เก่าที่ Musk สร้าง world largest AI supercomputer ปี 2024 เพื่อ train Grok ของ xAI ตอนนี้ Anthropic ที่เป็นคู่แข่งโดยตรงของ xAI กลับเข้ามากินที่ทั้งโต๊ะ

จุดที่น่าทึ่งคือใน press release ทั้งสองฝั่ง พูดถึง exploratory partnership ที่จะร่วมพัฒนา orbital compute หลาย gigawatt ในวงโคจร เป็น declared statement แรกของ frontier lab ที่ commit ถึง space based AI infrastructure แบบจริงจัง Bezos กับ Project Kuiper เคย hint แต่ไม่เคย sign ดีลแบบนี้ Microsoft กับ Google ยังอยู่ระดับ R&D เท่านั้น

financial term ไม่เปิด แต่ scale บอกตัวเอง 220 พัน Nvidia GPU ราคา 30K ต่อตัว คือ 6.6 พันล้านดอลลาร์ของ capex ที่ SpaceX ลงไปแล้ว Anthropic เซ็น lease usage contract เข้ามาใช้ พร้อมประกาศว่า Claude Code limit จะขยายอย่างมีนัยสำคัญ แปลว่า Anthropic compute starved อยู่จริง ก่อนที่ดีลนี้จะปิด เห็นได้จากการ throttle Claude Sonnet Opus หลายรอบใน Q1 Q2

ที่น่าจับตาคือ Anthropic เพิ่ง close ดีล Google TPU 200 พันล้าน เปิด venture firm กับ Blackstone Goldman 1.5 พันล้าน และตอนนี้ดีล SpaceX อีกหนึ่ง ทั้งหมดในระยะ 10 วัน Anthropic ที่เคย narrative ว่าเป็น small lab ตอนนี้กำกับ infrastructure portfolio ที่กว้างกว่า OpenAI ที่พึ่ง Azure อย่างเดียว ตอนนี้มี compute ใน 4 ค่ายขนานกัน Amazon Trainium Google TPU Microsoft Azure SpaceX Nvidia GPU compute arbitrage กลายเป็น core competency

มุม OpenBridge ไม่ direct เกี่ยว แต่สาม insight หนึ่ง multi cloud ของ Anthropic แปลว่าลูกค้า Thai enterprise ที่ pick Claude เพราะ data residency จะมีทางเลือกมากขึ้น OpenBridge connector ที่ route AI call ตาม customer policy ขาย B2B Thai ได้ตรง สอง throughput ที่เพิ่ม Claude API rate limit ที่เคยเจอใน Q1 Q2 จะ unblock pricing tier ของเรา refresh เดือน มิ.ย. สาม orbital compute อย่ารีบ FOMO แต่ในเอกสาร investor ใส่ slide ว่า no matter where compute lives ground cloud orbit connector เราเชื่อมที่ data ลูกค้าอยู่ ภาพ futuristic ที่ VC ชอบครับ
