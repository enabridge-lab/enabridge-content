---
date: 2026-05-04
slug: parallel-web-systems-100m-agent-infra
topic: agentic-ai
sources: 4
reading_time_min: 4
image_prompt: Editorial illustration of a glowing parallel web of interconnected nodes branching off a familiar globe, with autonomous robotic arms reaching through API portals to fetch data from floating webpages, minimal flat geometric shapes, muted indigo and amber palette, dramatic backlight, no text no logos no faces
image: images/26-05-04-0608-03-parallel-web-systems-100m-agent-infra.png
---

# Parag Agrawal กลับมาแล้ว — Parallel Web ระดม $100M ที่ $2B สร้าง "เว็บคู่ขนาน" ให้ AI agent ใช้แทนคน

## TL;DR
- 28–29 เม.ย. — Parallel Web Systems ของ Parag Agrawal (อดีต CEO Twitter) ปิด Series B $100M led by Sequoia ที่ valuation $2B — เพียง 5 เดือนหลัง Series A $100M ที่ $740M รวม total funding $230M ในเวลาไม่ถึง 18 เดือน
- product คือ **search/research API ที่ออกแบบมาให้ AI agent ใช้แทน Google** — มี 100,000+ developers ลงทะเบียน, customer flagship: Clay, Harvey, Notion, Opendoor — pricing per query สูงกว่า Google API หลายเท่า แต่ result ออกมาในรูป structured data ที่ agent กิน feed เข้า workflow ต่อได้ทันที ไม่ต้อง parse HTML
- thesis ของ Agrawal: web ปัจจุบันออกแบบให้คนอ่าน — robots.txt, anti-bot, paywall, JS rendering — agent ที่จะ scale ต้องการ web layer ใหม่ที่ออกแบบให้ machine consume ตั้งแต่ต้น Sequoia note ระบุว่า "queries from agents จะเกิน queries from humans ภายใน 2027"

## เกิดอะไรขึ้น

วันที่ 29 เมษายน Parallel Web Systems ประกาศปิด Series B ขนาด $100 ล้านที่ valuation $2 พันล้าน นำโดย Sequoia Capital พร้อม Kleiner Perkins, Index Ventures, Khosla Ventures, First Round Capital, Spark Capital และ Terrain Capital ลงทุนตาม รอบนี้เกิดขึ้น **เพียง 5 เดือนหลัง Series A** ที่ก็ขนาด $100M เท่ากันแต่ valuation $740M — Sequoia + Kleiner + Index ตัดสินใจ tripling valuation ในห้าเดือนเพื่อเข้ารอบใหม่ก่อนที่ Microsoft + Google จะเข้ามาขัด ตามที่ TechCrunch รายงาน

CEO Parag Agrawal คือ Twitter CEO คนเก่าที่ Elon Musk ไล่ออกในปี 2022 หลังเทคโอเวอร์ — Agrawal เก็บตัวเงียบ ๆ สองปี ก่อนกลับมา launch Parallel ในต้นปี 2024 thesis ของบริษัทเรียบง่ายแต่ยิ่งใหญ่: **web ปัจจุบันออกแบบมาเพื่อมนุษย์อ่าน** — รูปแบบ HTML, JavaScript rendering, anti-bot mechanism, paywall, captcha, dynamic loading — ทุกอย่างเป็น obstacle สำหรับ AI agent ที่ต้องการ fetch information แบบ programmatic ผลคือ agent vendor ทุกรายตั้งแต่ Anthropic Computer Use ไปถึง OpenAI Operator ต้อง deploy headless browser cluster ขนาดใหญ่ ๆ เพื่อ render page เหมือนที่ user ใช้ — สิ้นเปลือง compute มหาศาลและ slow มาก

Parallel แก้ปัญหานี้โดยสร้าง **"shadow web"** — index ของเว็บที่ pre-fetched, pre-rendered, pre-structured ให้อยู่ในรูป markdown + structured JSON ที่ agent กินได้ทันที พร้อม API ที่รับ query แบบ natural language แทน keyword — แล้ว return ผลพร้อม citation, confidence score และ structured fact extraction ลูกค้าเช่น Clay (B2B prospecting agent) ใช้ Parallel แทน Google + scraping cluster ของตัวเอง — ลด infrastructure cost 60% และ latency จาก 12 วินาทีต่อ research task เหลือ 2.4 วินาที Harvey (legal AI) ใช้ Parallel ค้นกฎหมาย case law แบบ specialized vertical (Parallel มี vertical index แยกสำหรับ legal, finance, healthcare, e-commerce) Notion ใช้ Parallel เป็น backend ของ "Q&A agent" ใหม่ในช่วง beta

จุด pricing ของ Parallel น่าสนใจ — per-query สูงกว่า Google Custom Search API ราว 8–15x แต่ revenue ของบริษัทโตเร็วมาก SiliconANGLE รายงานว่า run-rate ทะลุ $40M ARR ภายใน 14 เดือนแรกและคาดว่าจะแตะ $100M สิ้นปี 2026 reason ที่ลูกค้ายอมจ่าย: cost-per-resolved-task ของ agent ที่ใช้ Parallel ต่ำกว่าคู่แข่งราว 3x เพราะ agent ไม่ต้อง iterate หลายรอบเพื่อ parse + verify Sequoia note ว่า **"infrastructure layer ของ agent economy"** กำลังจะมีมูลค่ามากกว่า model layer เอง ภายใน 5 ปีนี้

อีกจุดหนึ่งที่ Agrawal เน้นกับนักข่าว: Parallel กำลัง launch **"Agent Browser"** ในไตรมาส 3 — runtime ที่ run inside agent ของลูกค้า โดยมี optimized rendering pipeline และ session memory ที่ persist ข้าม query — pitch โดยตรงให้ Anthropic Computer Use, OpenAI Operator, และ Google Mariner ที่ตอนนี้ทุกรายใช้ Chromium baseline ที่หนักและช้า

## ทำไมสำคัญ

Parallel Web Systems คือ signal ว่า **agent economy เริ่มมี infrastructure layer ของตัวเองที่แยกจาก consumer web** — pattern ที่ Sequoia เปรียบกับ AWS ที่แยก enterprise infra จาก consumer hosting ในยุค 2006 ปัจจุบันทุก agent ที่ดี ๆ ต้องการ 4 อย่างที่ web เดิมทำได้ไม่ดี: (1) structured data ที่ agent parse ได้ตรง (2) low-latency programmatic access (3) per-vertical specialization (legal, medical, finance) (4) authentication/payment rail ที่ไม่ใช่ captcha — Parallel เดิน 3/4 อย่างนี้แล้วและกำลังจะแตะอย่างที่ 4

เทียบกับ player อื่น Brave Search API + Tavily + Perplexity API ก็พยายามทำ space เดียวกัน แต่ Parallel ได้ moat ที่หา replicate ยาก: (1) ลูกค้า top-tier agent vendor (Clay, Harvey, Notion) บอก usecase ตรง (2) team engineering อดีต Twitter search ที่รู้จัก scale issue ของ web index ระดับ trillion-document (3) cap table ที่มี Sequoia + Kleiner + Index ที่ portfolio company เกือบทุกรายเป็น prospect — Parag Agrawal เคยเป็น CTO ของ Twitter ที่ดูแล search infra เพราะฉะนั้นเขามี domain knowledge แบบ deep ที่ founder ทั่วไปไม่มี

ข้อ caveat: **Cloudflare** เพิ่ง launch "Code Mode" สำหรับ agent ในวันที่ 1 พ.ค. (ที่เราเคย brief ไป) ซึ่งมี edge compute layer ที่ host ใน data center ใกล้ลูกค้า — ถ้า Cloudflare ตัดสินใจ extend ไปยัง search/research service ของตัวเองก็จะเป็นคู่แข่งที่หินมาก ส่วนถ้า Microsoft หรือ Google decide ว่า agent infrastructure คือ strategic priority และยอมขาย search/index API ราคา loss-leader Parallel จะเจอ pressure pricing หนัก — แต่ทั้งสามรายข้างต้นมี conflict of interest กับ Bing/Google search consumer business ที่ยังเป็น cash cow อยู่

## มุม OpenBridge

Parallel เป็น case study ตรงของ pattern "agent infrastructure" ที่ OpenBridge ควรจับตา 3 มุม: (1) ถ้า OpenBridge มี workflow ที่ require ดึง data จาก web/external API ให้พิจารณา integrate Parallel หรือคู่แข่ง (Tavily, Brave) เป็น **sub-component** ใน pipeline — แทนที่ลูกค้าจะ build scraping infra เอง เราจัดเตรียมเป็น managed service ในไม่กี่เดือน Parallel น่าจะมี Thai-language vertical index ออกมาแล้ว (2) thesis ของ Agrawal ว่า "agent ต้องการ data layer ที่ออกแบบเพื่อ machine ตั้งแต่ต้น" สามารถ apply กับ B2B integration ได้ตรง — connector ของ OpenBridge ปัจจุบันที่ ออกแบบให้ human map field manually กำลังจะเป็น obsolete agent ของลูกค้าจะคาดหวังว่าเราให้ semantic schema + auto-mapping พร้อม

(3) จุดที่ urgent ที่สุด: OpenBridge ควรเริ่ม monitor pricing model ของ agent infrastructure layer ทั้งหมด (Parallel, Browserbase, E2B, Modal) เพราะ pricing ที่ลูกค้าของเราจ่ายให้ "ข้อมูลและ runtime" ของ agent กำลังจะกินสัดส่วนของ AI budget มากกว่า model API call เอง ภายในปี 2027 ตามที่ Sequoia note และ a16z รายงาน — ถ้า OpenBridge ยังคิด pricing เป็น "API call ต่อเดือน" จะ undercharge อย่างหนัก

## Sources
- [Parallel Web Systems hits $2B valuation five months after its last big raise](https://techcrunch.com/2026/04/29/parallel-web-systems-hits-2b-valuation-five-months-after-its-last-big-raise/)
- [Sequoia Capital leads Parallel's $100M raise at $2B valuation to build the web infrastructure for AI agents](https://techfundingnews.com/parag-agrawal-parallel-100m-series-b-sequoia-ai-agents/)
- [Parag Agrawal's startup raises $100M to build a parallel web for AI agents](https://siliconangle.com/2026/04/28/parag-agrawals-startup-raises-100m-build-parallel-web-ai-agents/)
- [Parallel Web Systems: Infrastructure for intelligence on the web](https://parallel.ai/blog/series-b)

---

## Audio script
ข่าวที่สาม — Parag Agrawal อดีต CEO Twitter ที่ Elon Musk ไล่ออกในปี 2022 กลับมาแล้วในฐานะ founder ของ Parallel Web Systems บริษัทเพิ่งปิด Series B หนึ่งร้อยล้านดอลลาร์ ที่ valuation สองพันล้าน นำโดย Sequoia — เพียงห้าเดือนหลัง Series A ที่ valuation เจ็ดร้อยสี่สิบล้าน ขึ้นเกือบสามเท่าในห้าเดือน

product ของ Parallel คือ search API ที่ออกแบบให้ AI agent ใช้แทนคน thesis คือ — web ปัจจุบันออกแบบมาเพื่อให้คนอ่าน HTML, JavaScript, captcha, paywall ทุกอย่างเป็นอุปสรรคสำหรับ agent ที่ต้องการ fetch ข้อมูลแบบ programmatic Parallel เลยสร้าง shadow web ของตัวเอง — index เว็บที่ pre-rendered, pre-structured ให้อยู่ในรูป markdown + JSON ที่ agent กินได้ทันที

ลูกค้าใหญ่ ๆ มี Clay, Harvey, Notion, Opendoor — Clay ใช้ Parallel แทน Google + scraping ของตัวเอง ลด infra cost หกสิบเปอร์เซ็นต์ latency จากสิบสองวินาทีเหลือสองจุดสี่วินาที pricing per-query สูงกว่า Google API แปดถึงสิบห้าเท่า แต่ลูกค้ายอมจ่ายเพราะ cost-per-resolved-task ของ agent ต่ำกว่าคู่แข่งสามเท่า run-rate ARR สี่สิบล้านในสิบสี่เดือนแรก

จุดสำคัญคือ Sequoia note ว่า infrastructure layer ของ agent economy จะมีมูลค่ามากกว่า model layer ภายในห้าปี — agent ไม่ใช่แค่ใช้ Claude หรือ GPT เท่านั้น ยังต้องการ web access, runtime, browser, payment rail ที่ออกแบบเพื่อ machine

OpenBridge ควรคิดเรื่องเดียวกัน — connector ของเราที่ออกแบบให้ human map field manually กำลังจะ obsolete agent ของลูกค้าจะคาดหวัง semantic schema + auto-mapping พร้อม pricing ของเราด้วย — ถ้ายังคิดเป็น API call ต่อเดือนจะ undercharge ในอีกสองปี
