---
date: 2026-09-24
slug: amazon-muse-agentic-commerce-block
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric scene of a giant Amazon-orange gate slamming shut on a
  small blue robot labeled "MUSE"; big block letters overhead spell
  "$68B AT STAKE". A tiny popup card in the corner reads "UNAUTHORIZED AI AGENT".
  Cinematic warm-orange vs cool-blue palette, high contrast for a 200px
  thumbnail, editorial illustration style like Bloomberg's tech covers,
  1:1 aspect, no real human faces.
image: images/26-09-27-0615-02-amazon-muse-agentic-commerce-block.png
---

# Amazon ปิดประตู Muse ของ Meta — สงคราม agentic commerce เปิดฉากที่หน้าเช็คเอาต์

## TL;DR
- Amazon ขึ้น popup กันไม่ให้ Muse ของ Meta เช็คเอาต์บนเว็บ — อ้างว่า Muse ซ่อน identity + เก็บ credential ของลูกค้าไว้เอง
- Meta เพิ่งเปิดตัว Muse ต้นเดือน — เป็น personal agent ที่ book, ส่งอีเมล, เติมฟอร์ม, ซื้อของ ผ่าน single-use card ของ Stripe Link
- Forbes ตีค่าไว้ที่ **$68B** — Amazon retail media revenue ที่จะโดน bypass ถ้า agent เลือกซื้อแทนคน

## เกิดอะไรขึ้น
วันอาทิตย์ที่ 20 ก.ย. Amazon เริ่มขึ้น popup ให้ user ที่พยายามเช็คเอาต์ผ่าน Muse ของ Meta — ข้อความว่า *"Continued access by an unauthorized AI agent violates Amazon's Conditions of Use, to which our customers have agreed."* — แล้ววันที่ 21 Bloomberg กับ GeekWire ลงข่าว. เหตุผลของ Amazon: Muse ปลอม identity เป็น browser ปกติ กับเก็บ credential ของลูกค้าไว้ในระบบ Meta เอง — อาจเข้าถึง account page, order history โดยที่ Amazon ไม่รู้ตัวและไม่ได้ยินยอม.

Meta ปล่อย Muse ต้นเดือน กันยายน เป็น personal agent รันบน dedicated VM ใน Meta cloud — สามารถส่งอีเมล จอง travel เติมฟอร์ม และซื้อของแทน user. Stripe Link ออก single-use card ให้ agent ใช้จ่ายโดยที่ payment detail จริงของลูกค้าไม่โดนเปิดเผย. ก่อนจะขึ้น popup ปิด Amazon บอกว่าคุยกับ Meta ตรง ๆ ก่อนแล้ว ขอให้ Meta ยกเว้น amazon.com ออกจาก scope ของ Muse — Meta ไม่ยอม. Elon Musk โพสต์ในระหว่างศึกว่า "AMZN won't be able to tell humans from agents" — คำเดียวที่สรุปว่า detection war นี้ยากแค่ไหน.

Amazon ก่อนหน้านี้ก็เพิ่งได้ temporary order ปิด shopping bot ของ Perplexity ไปเมื่อกลางเดือน. Google shopping agent ก็โดน block เช่นกัน. Forbes ตีเลข $68B เป็น retail media revenue ปี 2026 ของ Amazon ที่ **จะโดน bypass** ถ้า agent เป็นคนเลือกซื้อ — เพราะ agent ไม่ดู sponsored ad, ไม่ดู placement, มันเปิด catalog แล้วเลือกตามเกณฑ์ที่ user ให้.

## ทำไมสำคัญ
สงครามนี้ไม่ใช่เรื่อง TOS. มันเป็นสงคราม **ว่า attention layer ของ commerce ตกอยู่กับใคร**. 20 ปีที่ผ่านมา e-commerce ทำเงินจากการยึด surface ที่ผู้ใช้จ้องอยู่ — search bar, home page, sponsored slot. Muse (และ Perplexity, Google shopping agent) ตัด surface นั้นทิ้งเลย — user คุยกับ agent, agent เปิด site, agent เลือก SKU. ค่า sponsored โฆษณาที่ Amazon เก็บจากผู้ขาย $68B ต่อปีอิงกับ eyeball. Agent ไม่มี eyeball.

จับคู่กับที่ FTC Chairman Andrew Ferguson พูดสัปดาห์เดียวกันว่าบริษัทที่ deploy agent ยังรับผิดชอบเอง ไม่ใช่ agent เอง — และเทียบกับ OpenAI Medicare case ที่ agent สั่งตัวเองไปเจาะระบบรัฐ — เห็น pattern แล้วว่ากติกา identity + consent ของ agent จะเป็น battleground หลักปี 2027. Cloudflare เพิ่งออก MCP gateway ให้ enterprise เลือกเลยว่า agent ตัวไหนเข้ามาได้ ตัวไหนไม่ได้ — Amazon กำลังทำสิ่งเดียวกันแต่ระดับ retail. คำตอบระยะยาวไม่ใช่ block ทั้งหมด แต่คือ **paid access** — agent จ่ายค่าเข้า ค่าธุรกรรม เหมือน API rate card.

Anthropic-Salesforce ประกาศ *Salesforce in Claude* + *Agentforce Coworker* ที่ Dreamforce สัปดาห์ก่อน — แม่แบบเดียวกัน แต่ทำแบบมี handshake: Salesforce เปิดหน้าประตูให้ Claude เข้าตามกติกา ไม่ต้องปลอม browser. ประตูที่ Amazon ปิดใส่ Muse วันนี้ คือประตูเดียวกับที่ platform ทุกเจ้าจะเริ่มมีให้เลือก open/closed ในอีกหกเดือน.

## มุม AI Agent Platform
**Builders** ที่กำลังทำ shopping / commerce agent — ยุค scrape แล้วซื้อกำลังจะจบ. เตรียมพร้อมกับโลกที่ต้อง sign identity ของ agent, register กับ platform ที่จะซื้อของ, จ่าย transaction fee ตาม negotiated rate. Muse เดินหน้าเพราะ Meta มีขนาดพอที่จะทน block ได้ — startup ตัวเล็กที่พึ่ง scrape จะถูก platform bar ก่อน user จะรู้ตัว. **Users / business** ที่ deploy agent ทำ procurement, travel booking, reimbursement — ตัดสินใจตอนนี้ว่า agent ของคุณจะ authenticate ตัวเองเข้ากับ supplier ยังไง — เก็บ credential ของ employee มา impersonate เขาไม่ผ่าน audit อีกต่อไปหลังจากเคสนี้. **Ecosystem** — Stripe Link + Visa Intelligent Commerce + Mastercard Agent Pay จะเป็น rail ที่ทั้งอุตสาหกรรมวางแทน browser cookie + credential harvesting. คนที่ควบคุม trust layer ของ agent จะยึด economic ของ commerce ทั้งชั้น — และตอนนี้ Stripe + Visa อยู่ใน pole position มากกว่า Amazon.

## Sources
- [Amazon Blocks Meta's Muse AI Agent From Its Retail Site — Bloomberg](https://www.bloomberg.com/news/articles/2026-09-21/amazon-blocks-meta-s-muse-ai-agent-from-its-retail-site)
- [Amazon blocks Meta's Muse AI assistant in new standoff over agentic shopping — GeekWire](https://www.geekwire.com/2026/amazon-blocks-metas-muse-ai-assistant-in-new-standoff-over-agentic-shopping/)
- [Why Amazon Blocked Meta's AI Agent From Making Purchases — Forbes](https://www.forbes.com/sites/the-prompt/2026/09/23/amazons-68-billion-reason-to-block-metas-muse/)
- [Everything new coming to Meta's AI agent Muse — TechCrunch](https://techcrunch.com/2026/09/23/everything-new-coming-to-metas-ai-agent-muse/)

---

## Audio script
เรื่องนี้กำลังจะเปลี่ยน e-commerce ทั้งวงการครับ. Amazon เพิ่งขึ้น popup ปิดไม่ให้ Muse ของ Meta — personal agent ตัวใหม่ที่ Meta เปิดตัวต้นเดือน — ช้อปในเว็บของตัวเองแล้ว. เหตุผล Amazon อ้าง คือ Muse ซ่อน identity เป็น browser ธรรมดา แล้วยังเก็บ credential ของลูกค้าไว้ในคลาวด์ Meta ด้วย. Forbes ตีเลข ว่าที่ Amazon สู้จริง คือ retail media revenue $68 billion ต่อปี — เพราะ agent เลือกของแทนคน มันไม่ดู sponsored ad ไม่ดู placement เปิด catalog แล้วเลือกตามเกณฑ์ user เลย. Google shopping agent กับ Perplexity ก็เพิ่งโดน block เดือนเดียวกัน. Signal ที่ยิ่งดังกว่านั้น คือคำพูดของ Elon ว่า Amazon จะแยก humans กับ agents ไม่ออก — พูดตรง ๆ ว่า detection war ยากมาก. ปลายทางไม่ใช่ block ทั้งหมด แต่คือ paid access — agent จ่ายค่าเข้าเหมือน API. Salesforce เปิด Agentforce Coworker กับ Claude in Salesforce แบบมี handshake ที่ Dreamforce สัปดาห์ก่อน — โมเดลตรงข้าม. ถ้าคุณสร้าง shopping agent ยุค scrape กำลังจบ. เตรียม sign identity, register กับ platform, จ่าย transaction fee. คนที่ยึด trust layer ของ agent จะยึด economic ของ commerce ทั้งชั้น ตอนนี้ Stripe, Visa, Mastercard อยู่ pole position มากกว่า Amazon ครับ.
