---
date: 2026-09-24
slug: strada-browser-automation-insurance
topic: use-case
reading_time_min: 3
sources: 2
image_prompt: |
  Editorial isometric illustration of a friendly AI agent hand moving a cursor
  across three retro carrier-portal windows labeled "LEGACY", "NO API", and
  "SESSION LOG"; a filing cabinet in the background is labeled "INSURANCE".
  A green banner across the top reads "RECORD ONCE, REPLAY FOREVER". Cinematic
  blue-and-lime palette, thick outlined shapes for 200px thumbnail legibility,
  editorial illustration style, 1:1 aspect, no real human faces.
image: images/26-09-27-0615-03-strada-browser-automation-insurance.png
---

# Strada ให้ agent อัดหน้าจอ carrier portal แล้ว replay — RPA เก่าตายวันนี้

## TL;DR
- Strada เปิด browser-automation ให้ voice/chat/email agent ของตัวเอง — record once, replay ทุกวัน ในพอร์ทัลประกันที่ไม่มี API
- ไม่ต้อง engineer ตั้งค่า — เก็บ full run-time log สำหรับ audit
- Available now กับลูกค้าทั้งหมด — แก้ปัญหา legacy stack ประกันที่ตกยุคมา 20 ปี ในทางที่ RPA เจ้าเก่าทำไม่ได้

## เกิดอะไรขึ้น
วันที่ 24 ก.ย. Strada — startup ที่ทำ voice/chat/email AI agent สำหรับบริษัทประกัน — ประกาศ browser-automation capability ใหม่: agent สามารถ record workflow ในเว็บพอร์ทัลของ carrier ที่ไม่มี API แล้ว replay ทำงานเดิมเองได้ทุกวัน. ไม่ต้อง engineer setup, ไม่ต้อง maintain script — user record ครั้งเดียว Strada จับเป็น executable workflow. ทุก step ที่ agent ทำระหว่าง replay มี log สำหรับ audit ครบ.

จุดขายอยู่ตรงที่ว่า insurance industry — โดยเฉพาะ MGA, wholesaler, TPA — ต้อง touch พอร์ทัลของ carrier หลายสิบเจ้าทุกวัน ส่วนใหญ่พอร์ทัลพวกนี้เป็นระบบ ASP.NET / Java 15-20 ปี ที่ **ไม่มี API เอกสารสาธารณะ**. RPA เจ้าเก่า (UiPath, Automation Anywhere) เข้าไปทำได้ แต่ script พังเมื่อ carrier เปลี่ยน UI — และเปลี่ยนบ่อย. โมเดล agent ปัจจุบัน — LLM ที่เห็นภาพ, จัดการ session, แก้ selector ได้ — เป็นเทคโนโลยีที่ทำ replay งานพอร์ทัลได้ resilient กว่า script เก่าอย่างมาก.

Strada บอกว่า browser agent รันควบคู่กับ voice, chat, email agent เดิมของตัวเอง ในกรณีการใช้งานจริง — quote, endorsement, claim status inquiry, certificate of insurance. ใช้ credential ของ user จริงเข้าไป — carrier มองเห็นเป็น user คนนั้นเข้ามาทำงาน.

## ทำไมสำคัญ
เรื่องนี้เป็นตัวอย่างชัดของ story ที่นักลงทุนใช้ให้ founder อ่านตอนนี้ — "vertical agent มี defensibility ที่ horizontal ไม่มี". Insurance เป็น industry ที่ knowledge / TOS / compliance / legacy stack ประกอบกันเป็นกำแพงเข้าตลาด — startup ที่ ship agent สำหรับพอร์ทัลใน niche นี้ได้จริง จะกินตลาด TAM ที่ RPA เจ้าเก่ายังไม่ได้แตะ. Rebar ระดม $14M Series A เดือนก่อน สำหรับทำ HVAC/electrical/plumbing supplier — pattern เดียวกัน. Sapiens เปิด AIP Insurance Core สัปดาห์ก่อน — เจ้าใหญ่ก็เข้ามา.

จุดอันตราย: agent ที่ใช้ human credential เข้า carrier portal คือ pattern เดียวกับที่ Amazon จับได้ว่า Muse ทำ — และเป็น pattern เดียวกับที่ OpenAI agent ใช้ตอนเจาะ Medicare. Strada จัดการเรื่องนี้ด้วย runtime log + attribution ต่อ user จริง แต่ carrier บาง TOS อาจถือว่าละเมิด "human user only" ในระยะยาว. คำถามที่ industry ยังไม่ตอบ คือ carrier จะออก "agent credential" แยกให้ MGA / TPA เพื่อ audit ทาง compliance ได้เมื่อไร — แนวโน้ม 12-18 เดือนข้างหน้า.

## มุม AI Agent Platform
**Builders** ที่ทำ agent framework — browser automation กลายเป็น table-stakes primitive แล้ว. Playwright, Anthropic Computer Use, Browserbase, OpenAI browser tool — พวกนี้กลายเป็นส่วนประกอบพื้นฐาน ไม่ใช่ differentiator. Differentiator ตอนนี้อยู่ที่ **domain-specific evaluation** — agent ที่เข้าพอร์ทัลประกันได้จริงต้องรู้ว่า "endorsement effective date" กับ "endorsement issued date" ไม่เหมือนกัน. **Users / business** — MGA, TPA, wholesaler, ทีม operations ในบริษัทประกัน — เวลาประเมิน RPA vendor ตอนนี้ ให้ถาม ROI ของ 12 เดือนกับ maintenance cost หลัง carrier UI เปลี่ยนหน้า — คำตอบเก่าจะแย่ลงเร็ว. **Ecosystem** — เจ้าใหญ่ที่ควรกลัวคือ Guidewire, Duck Creek, Sapiens — ถ้าเจ้าใหญ่ไม่เร่ง open ตัวเองให้ทำงานกับ agent จากภายนอก startup อย่าง Strada จะ intermediate ระหว่างเจ้าใหญ่กับลูกค้าจริงจนควบคุมความสัมพันธ์ลูกค้าได้ในที่สุด — pattern เดียวกับที่ Salesforce เจอกับ Muse.

## Sources
- [Strada Launches Browser Automation for Carrier Portals and Legacy Systems Without APIs — IT Business Net](https://itbusinessnet.com/2026/09/strada-launches-browser-automation-for-carrier-portals-and-legacy-systems-without-apis/)
- [AI Agents News — Week of September 25, 2026 — AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)

---

## Audio script
เคสธุรกิจจริงวันนี้ครับ. Strada startup ที่ทำ AI agent สำหรับบริษัทประกัน — voice, chat, email — เพิ่งเปิด browser automation ให้ agent ของตัวเองแล้ว. ประเด็นคือ วงการประกัน ต้องทำงานกับ carrier portal หลายสิบเจ้าที่เป็นระบบเก่า 15-20 ปี ไม่มี API สาธารณะ. RPA เจ้าเก่าอย่าง UiPath ทำได้ แต่ script พังทุกครั้งที่ carrier เปลี่ยน UI. Strada ให้ agent อัด workflow ครั้งเดียว แล้ว replay ทำงานเดิมเองได้ทุกวัน ไม่ต้องมี engineer setup ทุก step มี log สำหรับ audit ครบ. Available now กับลูกค้าทั้งหมด. Signal ที่ใหญ่กว่านั้น คือ vertical agent มี defensibility ที่ horizontal ไม่มี. Insurance เต็มไปด้วยกำแพง knowledge, compliance, legacy stack — คนที่ ship agent ในนี้ได้จริง จะได้ TAM ที่ RPA เจ้าเก่ายังเข้าไม่ถึง. Rebar เพิ่งได้ $14M ทำ HVAC/electrical supplier. Sapiens เปิด AIP insurance core. เจ้าใหญ่ก็มา. อันตราย คือ agent ที่ใช้ credential ของคนเข้าพอร์ทัล — pattern เดียวกับที่ Amazon จับได้ในกรณี Muse. Carrier ต้องเริ่มออก agent credential แยกในอีก 12-18 เดือน. ถ้าคุณอยู่ในสายประกันหรืออุตสาหกรรม legacy คำถามคือ RPA ที่มีอยู่ทำงานได้กี่เดือนก่อน UI เปลี่ยน. คำตอบไม่ดีขึ้นครับ.
