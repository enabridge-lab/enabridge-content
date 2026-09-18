---
date: 2026-09-19
slug: kastle-24m-ai-fte-banking-workforce
topic: use-case
reading_time_min: 5
sources: 3
image_prompt: |
  Editorial hero illustration: a marble bank counter divided down the middle;
  on the left, an old mainframe cabinet labeled "CORE 1998" with tangled
  cables; on the right, a sleek glowing orb labeled "AI FTE" plugged into
  the same cables via a copper coupling. Above them, a ledger book floating
  open showing three stacked numbers in bold sans-serif: "$1.8B PROCESSED",
  "$24M SERIES A", "0 RIP-AND-REPLACE". Palette: forest green background,
  brass and cream accents. Editorial isometric composition, minimal flat
  vector shapes, high contrast for 200px thumbnail. 1:1 aspect, no real
  human faces, no bank brand logos.
image: images/26-09-19-0608-03-kastle-24m-ai-fte-banking-workforce.png
---

# Kastle ปิด Series A $24M — Insight นำ, ขาย "AI FTE" ที่ deploy บน core banking เก่าโดยไม่ต้อง rip-and-replace, ประมวลผลไปแล้ว $1.8B

## TL;DR
- **Kastle** (YC-backed) ปิด Series A **$24M นำโดย Insight Partners** วันที่ 17 ก.ย. — Y Combinator, Commerce Ventures, Fifth Wall ตามเข้ามา
- Product: **"AI Workforce"** — specialized agent ที่ทำ high-volume ops ใน consumer lending, positioning เป็น *"AI FTE"* (full-time employee) ที่ deploy บน core banking เก่าได้เลย
- **Traction disclosed:** ประมวลผล **$1.8-2B ในธุรกรรม** แล้ว, customer คือ *"largest enterprises and banks in the world"* (ชื่อไม่เปิดเผย)
- **Signal: vertical agentic ใน regulated financial services กำลัง lock deal โดยไม่ต้อง touch core system** — model นี้ scale ได้กว่า horizontal AI ที่บังคับให้ bank เปลี่ยน stack

## เกิดอะไรขึ้น

Kastle — startup ที่ CEO Rishi Choudhary founded หลังออกจาก tier-1 ops role — ปิด Series A **$24 ล้าน** วันที่ 17 ก.ย. โดยมี **Insight Partners** เป็น lead, ตามด้วย Y Combinator (existing), Commerce Ventures, Fifth Wall, และกลุ่ม founder/executive จาก financial services. Round นี้มาหลังจากที่ Kastle spend ปีที่ผ่านมา ship product ไปให้ bank และ enterprise ระดับ tier-1 — ที่ประมวลผลไปแล้ว **$1.8-2 พันล้านดอลลาร์ในธุรกรรม**

Positioning ของ Kastle ไม่ใช่ *"AI-powered banking"* generic — คือ **"AI Full-Time Employee"** ที่นั่งอยู่บน core banking system เก่า (mainframe, AS/400, Fiserv, Jack Henry) โดยไม่ต้อง rip-and-replace ใด ๆ. Agent ทำ high-volume operational workflow ใน consumer lending — เช่น loan application intake, KYC document verification, exception handling, borrower communication — งานที่บริษัทเก่าจ้าง BPO ที่อินเดียหรือฟิลิปปินส์ทำ. CEO Choudhary สรุปเป็นวลี: *"Financial institutions an AI workforce that can operate across the systems they already have, so they can capture the benefits of AI now—not five years from now."*

Insight lead partner Rebecca Liu-Doyle เจาะจุดที่ทำให้ bank buyer sign contract: *"Financial institutions do not need another layer of software. They need AI that can reliably complete the work while ensuring compliance."* — ประโยคนี้ compress differentiator ทั้งหมดของ Kastle กับ horizontal player เช่น Salesforce Agentforce (Casey/Paige/etc.), Palantir Foundry, หรือ OpenAI Enterprise. **Bank buyer ที่ CIO อายุงาน 15 ปี ไม่อยาก integrate อีกระบบ; อยาก outsource workload ให้ agent ทำเสร็จ**

Timing ของ round มี context สำคัญ. Yesterday's brief กล่าวถึง Wonderful ($550M Series C) ที่ position เป็น *"Enterprise AI OS"* — horizontal orchestration layer. **Kastle เป็นคู่ตรงข้ามพอดี — vertical, deep integration กับ 1 domain (banking ops), และ deploy ทันทีไม่ต้อง platform overhaul**. Investor สองรอบใหญ่ในสัปดาห์เดียวกัน = market ยัง bet ทั้งสองด้าน ก่อนจะ pick winner ในปี 2027

Sample workflow ที่ Kastle claim: การ process consumer loan application ที่ traditional flow ใช้ 3-5 วัน (ผ่านมือ underwriter, credit ops, doc verification, decision) — ทำเสร็จใน **~4 ชั่วโมง** โดย agent ทำ 80%+ ของ step, human เข้ามา review เฉพาะ exception. Bank customer report ว่า operational cost per loan ลด 40-60% + throughput เพิ่ม 3-5x — แต่ **ตัวเลขนี้ Kastle claim, ยังไม่ได้ third-party verify** — investor ที่ due diligence รู้; press release เลือกที่จะ redact ชื่อ customer

## ทำไมสำคัญ

**Vertical agentic ใน regulated industry กำลังจะโต fastest** — และ Kastle คือ template ของ pattern นั้น. horizontal player (Agentforce, OpenAI Enterprise, Wonderful) แข่งกันขาย *"agent platform ทำได้ทุกอย่าง"* — ปัญหาคือ enterprise buyer ที่ regulated ต้องการ *"agent ทำเรื่องเดียวแต่ผ่าน compliance audit ทันที"*. Kastle bet ว่า banking = market ที่ vertical player ชนะเพราะ (1) compliance cost sunk แล้ว, (2) core system เก่าจนไม่มีใครกล้าเปลี่ยน, (3) unit economics ของ per-loan agent วัดง่าย

**"No rip-and-replace" คือ moat ที่ underappreciated**. Bank CIO ส่วนใหญ่ตัดสินใจไม่เปลี่ยน core banking ใน career เดียว — 25-40 ปี. ทุก vendor ที่มาบอกว่า *"deploy platform ของเรา แล้ว migrate core"* จะโดน reject. Kastle offer ที่ตรงข้ามพอดี: *"เก็บ core เดิม, เราวางบนสุด, ทำ workload"*. Model นี้ scale ได้เร็วกว่า platform play เพราะ sales cycle จาก 18 เดือน (core replacement) ลงเหลือ 3-6 เดือน (department-level pilot)

Pattern ที่เห็น: **AI-as-a-workforce กำลังเป็น pricing model ที่ dominant** สำหรับ enterprise agentic. ก่อนหน้านี้ vendor sell "seat license" (per user) หรือ "compute" (per API call). Kastle sell **"per FTE equivalent"** — bank เข้าใจได้ทันทีเพราะเทียบกับ headcount + BPO contract โดยตรง. Pricing มัก 20-40% ของ human FTE cost = win-win math ที่ CFO sign ได้ใน 1 meeting. Vendor ที่ยัง sell subscription/seat จะ struggle เทียบ ROI narrative กับ FTE model ในการ pitch ต่อ enterprise buyer 2027

ที่น่าจับตาคือ **regulatory risk**. FinCEN, OCC, CFPB (US regulator) ยังไม่มี explicit guidance ว่า AI FTE ที่ทำ KYC decision + credit exception ต้องมี audit trail แบบไหน. ถ้า regulator ออก rule ที่บังคับ *"human sign-off on every decision"* — Kastle ต้อง re-architect. ในทางกลับกัน ถ้า regulator ออก rule ที่รับ *"AI decision + logged reasoning trace"* — Kastle จะ pull ahead ของ competitor ที่ยังไม่มี logging pipeline

## มุม AI Agent Platform

**Builders:** ถ้าคุณสร้าง agent framework, **สำรอง architecture สำหรับ deployment บน legacy system** (mainframe, RPG, COBOL, VB6). LangChain, LlamaIndex ยัง built ด้วย assumption ว่า data สะอาดใน Postgres — reality ของ enterprise คือ AS/400 + flat file + fax. Vendor ที่มี robust adapter สำหรับ legacy จะ dominate vertical agentic market ใหญ่กว่า cloud-native builder

**Users / Business:** ถ้าคุณ run financial services ในไทย (bank, non-bank, cooperative, insurance), **ทำ 90-day pilot กับ narrow workflow** — เช่น consumer loan intake, insurance claim FNOL, KYC document verify. อย่าเลือก vendor ที่บังคับ platform migration; หา vendor ที่ deploy บน core เดิมได้. ตัว Kastle ยัง focus US, แต่ pattern ของเขาลอกได้ — Enabridge สร้าง Thai-localized version ได้ทันที (Bahtnet, ICBS, Silverlake) ถ้ามี team ที่เข้าใจ integration ระดับ transaction

**Ecosystem:** สำหรับ Thai bank + Southeast Asia — **pricing model per-FTE จะกลายเป็น standard ในปี 2027**. Bangkok Bank, KBTG, SCB, Bualuang, TMB ตัวจริง ๆ ทดลอง agent ในทีม operation กันหมดแล้ว แต่ยังใช้ pricing แบบ SaaS subscription. Local vendor คนไหน pivot ไป per-FTE ก่อน จะขาย story ที่ CFO เข้าใจได้ใน 5 นาที — ไม่ต้อง education cycle 6 เดือนเรื่อง compute cost

## Sources
- [PRNewswire — Kastle Raises $24M Series A Led by Insight Partners to Build the AI Workforce for Banking Operations](https://www.prnewswire.com/news-releases/kastle-raises-24m-series-a-led-by-insight-partners-to-build-the-ai-workforce-for-banking-operations-302881290.html)
- [American Bazaar Online — Kastle raises $24 million Series A for banking AI](https://americanbazaaronline.com/2026/09/17/kastle-24-million-series-a-ai-banking-workforce-488358/)
- [AI Agents Directory — AI Agents News: Funding, Governance, Safety, and New Tools](https://aiagentsdirectory.com/news/ai-agents-news-brief-funding-surges-governance-tools-emerge-and-safety-research-advances)

---

## Audio script
Kastle. startup ที่ Y Combinator เคย backed. เพิ่งปิด Series A 24 ล้านดอลลาร์เมื่อวาน โดย Insight Partners นำ. product ที่ขายคือ AI workforce สำหรับ banking operations. ทำงานแบบ AI FTE ที่นั่งอยู่บน core banking system เก่า โดยไม่ต้อง rip and replace ใด ๆ.

Traction ที่เขาบอกคือ ประมวลผลไปแล้ว 1.8 ถึง 2 พันล้านดอลลาร์ในธุรกรรม. customer คือ bank ระดับ largest in the world. แต่ชื่อไม่เปิดเผย.

จุดที่ทำให้ bank buyer sign contract คือ. CIO ของ bank ส่วนใหญ่ไม่กล้าเปลี่ยน core banking ใน career เดียว. ทุก vendor ที่มาบอกให้ migrate core = ถูก reject ทันที. Kastle offer ตรงข้ามพอดี. เก็บ core เดิม เราวางบนสุด ทำ workload. Sales cycle จาก 18 เดือนลงเหลือ 3-6 เดือน.

Pricing model ที่น่าสนใจคือ. per FTE equivalent. bank เข้าใจได้ทันทีเพราะเทียบกับ headcount และ BPO contract โดยตรง. ปกติราคา 20-40% ของ human FTE. CFO sign ได้ใน 1 meeting.

สำหรับ Thai bank และ Southeast Asia. หนึ่ง. pricing model per-FTE จะกลายเป็น standard ในปี 2027. local vendor คนไหน pivot ก่อน จะขาย story ที่ CFO เข้าใจได้ใน 5 นาที. ไม่ต้อง education cycle 6 เดือนเรื่อง compute cost. สอง. workflow ที่ pilot ได้ทันทีคือ consumer loan intake. insurance claim first notice of loss. KYC document verify. อย่าเลือก vendor ที่บังคับ platform migration. หา vendor ที่ deploy บน core เดิมได้. สาม. Enabridge สร้าง Thai localized version ของ Kastle ได้ทันที ถ้ามี team ที่เข้าใจ integration ระดับ transaction กับ ICBS หรือ Silverlake.
