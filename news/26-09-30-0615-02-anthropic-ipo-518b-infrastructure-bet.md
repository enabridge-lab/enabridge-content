---
date: 2026-09-29
slug: anthropic-ipo-518b-infrastructure-bet
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a giant open ledger book on a marble
  pedestal labeled "S-1 PROSPECTUS". Three towering columns rise from the
  page: "$518B COMPUTE", "$42B LOSS 2025", "$4.6B REVENUE 12x". A tiny warning
  banner at the top reads "EXISTENTIAL RISK". Cloud provider logos (AWS,
  Google Cloud) sit in the background as smaller pillars. Muted navy and
  gold palette, sharp contrast for 200px thumbnails, bold text rendering,
  no real human faces, 1:1 aspect. Style of a Bloomberg Businessweek cover.
image: images/26-09-30-0615-02-anthropic-ipo-518b-infrastructure-bet.png
---

# Anthropic ยื่น IPO leak แล้ว — จองใช้ cloud $518B, ขาดทุน $42B, เตือน AI อาจ "จบมนุษยชาติ" ในเอกสาร

## TL;DR
- Reuters ได้ prospectus IPO ของ Anthropic — จองใช้ compute + infrastructure รวม $518B, ขาดทุน $42B ในปี 2025, revenue โต 12 เท่าเป็น $4.6B
- Anthropic เขียนคำเตือน "existential risk to humanity" ในเอกสารทางการต่อ SEC — ครั้งแรกในประวัติศาสตร์ที่บริษัท frontier lab พูดในเอกสาร IPO
- Valuation ที่คุยกันคือ **$2 ล้านล้านดอลลาร์** — สูงกว่า OpenAI ตอนนี้ และเป็นสัญญาณของยุค frontier-lab-as-utility

## เกิดอะไรขึ้น
Reuters ปล่อยรายละเอียดของ IPO prospectus ของ Anthropic ในวันที่ 28-29 กันยายน. ตัวเลขที่หลุดออกมาชนตากันหมด: จองใช้ cloud + infrastructure รวม **518 พันล้านดอลลาร์** ในหลายปีข้างหน้ากับพาร์ทเนอร์ 6 เจ้าซึ่งประกอบด้วย Google, Amazon, Microsoft, Broadcom และรายอื่น. Revenue ปี 2025 โต 12 เท่าเป็น $4.6 พันล้าน. Operating loss เกิน $8 พันล้าน — ยังไม่รวม writedown ของ liability ที่ผูกกับ round ก่อน ๆ ซึ่งดัน net loss ทั้งปีไปเป็น $42 พันล้าน. ค่าใช้จ่ายด้าน compute อย่างเดียวปีที่แล้ว $7.33 พันล้าน — เพิ่มขึ้น 3 เท่าจากปี 2024 และคิดเป็นครึ่งของ operating expenses ทั้งหมด $12.65 พันล้าน.

ใน risk section ของ prospectus Anthropic เขียนไว้ตรง ๆ ว่า AI ของตัวเองอาจก่อ "existential risk to humanity" — นี่เป็นครั้งแรกที่ frontier lab เขียนคำเตือนแบบนี้ในเอกสารทางการต่อ SEC. สื่อทุกเจ้าตั้งแต่ Fortune, TechCrunch, Gizmodo หยิบประโยคนี้เป็นพาดหัว. Anthropic บอกด้วยว่า Amazon กับ Google ที่ลงทุนไปแล้วเป็นซัพพลายเออร์ cloud หลัก และบริษัทเซ็นสัญญา compute เพิ่มกับ SpaceX (Starlink data centers) กับ provider เล็กหลายรายเพื่อ lock capacity สำหรับ model รุ่นต่อ ๆ ไป.

Valuation ในตลาด pre-IPO perp คุยกันที่ระดับ **$2 ล้านล้านดอลลาร์** — สูงกว่า OpenAI ที่กำลังรอ IPO ในเวลาเดียวกัน. CoinDesk รายงานว่า perp trader "แทบไม่กระพริบตา" ตอนเห็น $518B commitment. Prospectus ยังบอกด้วยว่า Anthropic เชื่อว่า AI จะเปลี่ยน global economy "profoundly than industrialization, electricity and the internet" — วลีนี้อาจไปอยู่ใน pitch deck ของ VC ทุกเจ้าใน 6 เดือนข้างหน้า.

## ทำไมสำคัญ
$518 พันล้าน commitment ทำให้ Anthropic กลายเป็น **compute utility** มากกว่า software company. เทียบดู — Klarna ทั้งบริษัทประกาศว่าประหยัด $60M จาก AI, JPMorgan รัน 450+ agent case ต่อวันในราคาต้นทุนอาจต่ำกว่า Anthropic ใช้ค่าน้ำมันเครื่องบินเจ็ตของพนักงานปีหนึ่ง. อัตราส่วน compute-to-revenue ที่ Anthropic บอกไว้ (7.33B compute ต่อ 4.6B revenue) ยังลบอยู่ในระดับที่บริษัท SaaS ทั่วไปจะถูกไล่จากตลาด แต่ค่านิยม $2T สะท้อนว่านักลงทุนกำลังเดิมพันเรื่อง **capacity ownership** ไม่ใช่ P&L: ใครควบคุม compute pool ใหญ่ที่สุดในทศวรรษหน้า ควบคุมความสามารถของ agent ทั้งอุตสาหกรรม.

การเขียน "existential risk" ในเอกสาร SEC เป็น play ที่ฉลาดมาก 3 ชั้น. (1) ป้องกันการฟ้อง — ถ้าเกิดอะไรร้ายแรงในอนาคต Anthropic บอกได้ว่าเตือนแล้ว. (2) กีดกันคู่แข่ง — บริษัทใดที่จะ IPO ตามหลังต้องเขียนคำเตือนเหมือนกัน ไม่งั้นดูขาด self-awareness. (3) สร้าง narrative moat — เราเป็น "AI lab ที่ห่วงเรื่อง safety จริง" ซึ่งดึงลูกค้าประเภท enterprise regulated (bank, insurance, healthcare) ที่ต้องอ้าง due diligence ให้ compliance ของตัวเอง. Pattern เดียวกับที่ Anthropic เปิด Life Sciences Verification Program สัปดาห์ก่อน — วางตัวเป็น "grown-up frontier lab" ที่ตรงข้ามกับ OpenAI ที่เพิ่งเจอเคส Medicare Australia.

Signal สำหรับตลาด: **ยุคที่ startup AI จะแข่งด้วย product feature จบไปแล้ว**. ต่อไปเป็นยุคของ contract capacity. ใครไม่มีสัญญา multi-year กับ hyperscaler อย่างน้อยระดับ 8-9 digit ต่อปีจะไม่มีทางเทรน frontier model รอบต่อไปได้. mid-tier lab (Mistral, Cohere, xAI ในระดับหนึ่ง) จะต้องเลือกระหว่างการเป็น "national champion" ที่รับ funding จากรัฐ หรือถูก absorb เข้าสู่ hyperscaler ตัวใดตัวหนึ่ง.

## มุม AI Agent Platform
**Builders** ที่พึ่ง Claude — ราคา token ของ Anthropic ในอีก 2-3 ปีข้างหน้าจะไม่ลดง่าย ๆ ถึงจะ scale เท่าไร เพราะบริษัทมีภาระ commitment ที่ต้อง amortize. ถ้าคุณสร้าง agent ที่ margin บาง — เริ่มเจรจาเงื่อนไข volume discount ล่วงหน้า และมี fallback ไปโมเดล open-source หรือ Gemini เตรียมไว้. **Users/Business** ที่กำลังเลือก vendor สำหรับ enterprise agent — คำเตือน "existential risk" ในเอกสาร SEC คือของขวัญ. คุณเอาไปยื่นให้ risk committee ของบริษัทได้เลย: "vendor นี้บอกเองว่ามีความเสี่ยง เรามี governance stack มา cover ยัง?" — บังคับให้ทีม procurement คุยเรื่อง audit trail + kill switch จริงจัง. **Ecosystem** — AWS กับ Google เป็นทั้งซัพพลายเออร์ + นักลงทุนของ Anthropic คู่แข่งเบอร์สอง ก็เป็นทั้งคู่ของ OpenAI. hyperscaler จะกลายเป็น "kingmaker" ของ frontier lab ทั้งหมด — และวันหนึ่งจะบีบกำไรของ lab ให้แคบลงเรื่อย ๆ เพราะ AWS/GCP ของตัวเองก็ขาย agent product แข่งอยู่. เกม vertical integration กำลังจะเริ่มร้อนขึ้น.

## Sources
- [Anthropic's IPO prospectus shows sweeping AI vision, surging costs — Reuters via Yahoo](https://finance.yahoo.com/technology/ai/articles/exclusive-anthropics-ipo-prospectus-shows-231722972.html)
- [Anthropic warns investors of AI's 'existential risk to humanity' in IPO filing — CNBC](https://www.cnbc.com/2026/09/29/anthropic-warns-ai-existential-risks-ipo-filing-reuters.html)
- [Anthropic IPO Plans Show $518 Billion in Projected Spending — PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/anthropic-ipo-plans-show-518-billion-in-projected-spending/)
- [Anthropic's leaked IPO prospectus details steep losses, rapid growth, and a fear that AI could end humanity — Fortune](https://fortune.com/2026/09/29/anthropic-leaked-ipo-prospectus-losses-growth-ai-end-humanity/)

---

## Audio script
มาต่อกับข่าวใหญ่ตัวที่สองครับ. Reuters ได้เอกสาร IPO prospectus ของ Anthropic ตัวเลขที่หลุดออกมาชนตากันหมดครับ. Anthropic จองใช้ cloud กับ compute infrastructure รวม 518 พันล้านดอลลาร์ในหลายปีข้างหน้า กับพาร์ทเนอร์ 6 เจ้ารวม Google, Amazon, Microsoft, Broadcom. Revenue ปี 2025 โต 12 เท่าเป็น 4.6 พันล้าน แต่ขาดทุน operating เกิน 8 พันล้าน. Net loss ทั้งปี 42 พันล้าน. Valuation ที่คุยใน pre-IPO market ระดับ 2 ล้านล้านดอลลาร์ สูงกว่า OpenAI ที่กำลังรอ IPO เหมือนกัน. ประเด็นที่สื่อทุกเจ้าจับคือใน risk section ของ prospectus Anthropic เขียนตรง ๆ ว่า AI ของตัวเองอาจก่อ existential risk to humanity เป็นครั้งแรกที่ frontier lab เขียนแบบนี้ในเอกสาร SEC. Impact ต่อวงการ agentic ครับ. หนึ่ง ราคา token ของ Claude ในอีก 2-3 ปีจะไม่ลดง่ายเพราะภาระ commitment. ถ้าคุณสร้าง agent margin บาง เริ่มเจรจา volume discount กับเตรียม fallback ไปโมเดลอื่น. สอง คำเตือน existential risk ในเอกสารทางการเป็นของขวัญให้ risk committee ในองค์กร ยื่นให้ vendor คุยเรื่อง audit trail กับ kill switch จริงจัง. สาม hyperscaler ทั้ง AWS Google เป็นทั้งซัพพลายเออร์และคู่แข่งของ Anthropic. เกม vertical integration กำลังร้อนขึ้น. คำ verdict สั้นครับ ยุคที่ startup AI แข่งด้วย feature จบแล้ว ต่อไปเป็นยุคของ contract capacity. ใครไม่มีสัญญา multi-year กับ hyperscaler จะเทรนโมเดลรอบต่อไปไม่ได้ครับ.
