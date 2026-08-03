---
date: 2026-08-03
slug: visa-lianlian-loopxpay-b2b-agentic-payment-greater-china
topic: use-case
reading_time_min: 4
sources: 7
image_prompt: |
  Editorial isometric composition of a warehouse dock in Hong Kong at
  dawn. A cargo pallet is being loaded next to a large glowing card
  reader; on the card reader a hologram badge reads "TRUSTED AGENT —
  LOOPXPAY". A dotted line connects a supplier warehouse across the
  water to the reader, tagged "FIRST LIVE B2B AGENTIC TXN". Above, a
  clean stat block shows "GREATER CHINA · 24 JUL 2026" and a Visa-blue
  banner "VISA AGENTIC DIRECTORY REGISTERED". Deep dawn-blue + Visa
  royal-blue palette, chiaroscuro editorial style, 1:1 aspect, no real
  human faces (silhouettes ok), text sharp at 200px thumbnail.
image: images/26-08-03-0612-03-visa-lianlian-loopxpay-b2b-agentic-payment-greater-china.png
---

# Visa + Lianlian LoopXPay = B2B agentic payment ตัวแรกที่ live ใน Greater China — Trusted Agent Protocol เริ่มมีของจริง

## TL;DR
- **24 ก.ค.** — Visa และ Lianlian DigiTech (Hong Kong) ประกาศ **first live B2B agentic transaction ใน Greater China** — Lianlian's **LoopXPay agent** identify supplier, compare options, place order, execute payment ใน single workflow
- LoopXPay ลงทะเบียนใน **Visa Agentic Directory** — enterprise + merchant identify verified AI agent ผ่าน **Visa Trusted Agent Protocol** (TAP) ที่ Visa เปิดต้นปี 2026
- Guardrail: agent ทำงานภายใต้ **pre-defined spending controls + approval parameters** ที่บริษัทตั้งไว้ล่วงหน้า — ไม่ใช่ blank check
- Signal: **B2B payment กำลังเป็น first vertical ที่ agent เข้าถึง money movement** — SMB (ไม่มี procurement team) ได้ประโยชน์ทันที; Visa เดิมพันบทบาท identity + trust layer แทน card rail ในยุค agent economy

## เกิดอะไรขึ้น

วันที่ 24 กรกฎาคม Visa และ Lianlian DigiTech (บริษัท payment fintech ฮ่องกงที่ IPO บน HKEx เมื่อปี 2024 มี market cap ~$18B) ประกาศ press release ร่วม — **completed the first live B2B agentic transaction ใน Greater China market**. Transaction เกิดจาก Lianlian's proprietary agent ชื่อ **LoopXPay**: agent รับ input จาก procurement team ว่าต้องการ product sample จาก supplier, ระบุ 3 supplier candidate, เปรียบเทียบ specification + pricing + delivery, place order กับผู้ที่ scoring สูงสุด, executed cross-border payment ผ่าน Visa network ทั้งหมดใน single workflow ที่ complete ใน <5 นาที (spec เดิมของ manual procurement = 2-4 ชั่วโมง)

Trust architecture ที่ Visa vault คือ **Visa Trusted Agent Protocol (TAP)** ที่เปิด March 2026 คู่กับ **Visa Agentic Directory** — registry ที่ verified AI agent ต้องมี credential + capability declaration + spending scope + business identity ก่อน merchant network ยอม accept transaction. LoopXPay เป็น **first agent ใน APAC ที่ผ่าน TAP verification** — ต่อจาก U.S. registered agents (Perplexity Comet Purchase, OpenAI Operator Wallet, Anthropic Claude Purchase Extension) ที่ live มาตั้งแต่ Q2. Lianlian บอก Caixin ว่า "TAP verification ใช้เวลา 6-8 สัปดาห์ audit — Visa ตรวจ agent code path + prompt injection defense + spending guardrail + human-in-loop escalation policy — เทียบกับ merchant onboarding ปกติที่ 3 สัปดาห์"

Business context ที่ทำให้ transaction นี้สำคัญ: **SMB pain point ที่ LoopXPay solve คือ procurement bandwidth**. Visa press release อ้าง data ว่า SMB ในภูมิภาค Greater China (HK + Macau + Taiwan + mainland tier-1) ใช้เวลาเฉลี่ย **17 ชั่วโมง/สัปดาห์** ทำ sourcing + supplier vetting + payment — ตัวเลขที่ agent สามารถกลืนได้ 70-80%. Lianlian claim ว่า pilot 6 สัปดาห์กับ 40 SMB customer = **มูลค่ารวมการซื้อ $3.2M**, **average time saved 12 ชม./สัปดาห์/บริษัท**. Agent จะ generally available ให้ SMB Greater China ในเดือน **กันยายน 2026**, pricing subscription $200-800/เดือน ตาม transaction volume band

## ทำไมสำคัญ

**นี่คือครั้งแรกที่ agent economy มี "identity + trust layer" ที่ merchant ยอมรับ** — เป็น problem ที่หลายคนพูดถึงตั้งแต่ Claude 3.5 sonnet computer use เมื่อ Oct 2024 แต่ไม่มีใครมี solution ที่ merchant network ยอม. Visa TAP + Agentic Directory คือ answer โดย **infrastructure ที่มีอยู่แล้ว** (Visa network + 130M merchant + 4.3B card holders) — ไม่ใช่ crypto, ไม่ใช่ new rail, แค่ verification layer เพิ่ม. Mastercard Agent Pay (ประกาศ เม.ย. 2026) ก็ทำ pattern คล้ายกัน; Stripe Agent Toolkit ที่เข้า beta พฤษภาคม focus AI-native merchant. **B2B agentic payment กำลังกลายเป็น 3-horse race — Visa TAP / Mastercard Agent Pay / Stripe** ก่อนสิ้นปี ทั้งสามจะ live production; card network เดิมได้ role ใหม่ = identity broker แทนแค่ transaction router

**Greater China ก่อน US ในเรื่องนี้ = signal ของ regulatory environment**. Hong Kong Monetary Authority + China CAC (Cyberspace Administration) ปล่อย tiered agent authorization framework เมื่อ 15 ก.ค. — LoopXPay จัดตัวเองเข้า **Tier 2 (user-authorized decision)** โดยตั้ง pre-approved spending ceiling ต่อ transaction + daily volume; Tier 3 (autonomous decision) ยังต้อง filing กับ CAC ก่อน. **สภาพแวดล้อม regulate ก่อน ทำให้ enterprise ยอม pilot เร็วกว่า US** — Sarbanes-Oxley + procurement policy ของ Fortune 500 ยัง gray-area เรื่อง agent authority. Result: Asia จะ lead เรื่อง B2B agentic payment production case study ใน 6-12 เดือน; US จะ catch up ผ่าน regulated financial services (JPM, BofA, Amex) ที่มี compliance team รับได้

**SMB angle คือที่ VC จะเดิมพันหนักในไตรมาสถัดไป**. LoopXPay ไม่ได้ target enterprise (มี ERP + procurement team อยู่แล้ว) — target **SMB ที่ founder + 3-5 คนทำทุกอย่าง**. Time saving 12 ชม./สัปดาห์/บริษัท x 40 บริษัท pilot = 480 ชม. = ~ $20K value at $40/hr; ที่ subscription $500/เดือน = **10x ROI ทันที**. เมื่อ math นี้เป็น true และ Visa TAP verification เปิดทาง — **สตาร์ทอัพ vertical B2B agentic payment ในทุก region จะเกิดในไตรมาส 3-4** (Latin America, Southeast Asia, Middle East). Enabridge angle: **market opportunity ที่ Thai fintech (2C2P, Omise, LightNet) ควร partner กับ SI ทันที** ก่อน foreign player เข้าตลาด

## มุม AI Agent Platform

**สำหรับ builders:** ถ้ากำลัง build agent ที่มี payment/purchase capability — **priority #1 คือ register กับ card network agent directory**. Visa TAP + Mastercard Agent Directory + Stripe Agent Toolkit — audit process 4-8 สัปดาห์แต่ต้องมีถ้าจะ execute real transaction. **Design pattern สำคัญ**: separation of concerns ระหว่าง discovery/comparison agent (LLM-driven, creative) กับ execution agent (deterministic, policy-bound, verified). LoopXPay ทำ pattern นี้ชัด — LLM ตัดสินใจว่าจะซื้ออะไร, deterministic module executed payment ด้วย credential ที่ user pre-authorized. **Prompt injection defense = table stakes** — Visa audit reject 40% ของ agent ที่ apply ในรอบแรก (Lianlian ผ่าน round 2)

**สำหรับ users/business:** SMB Thailand + SEA ที่ต้องการ leverage agent สำหรับ procurement — **watching space นี้อีก 3-6 เดือน**. LoopXPay จะ expand ไป Southeast Asia Q4 2026 (Lianlian มี license ใน HK + Singapore); alternative ที่ควร evaluate: **Ramp Bill Pay Agent** (US-based, coming to APAC Q1 2027), **Airwallex Agent** (Australia-founded, HK HQ, มี Thailand license). Enterprise ที่มี procurement team อยู่แล้ว — pilot LoopXPay หรือ equivalent ใน **long-tail vendor category** (office supplies, cloud subscription, IT hardware) ที่ manual overhead สูง แต่ per-transaction value ต่ำ; ROI เห็นใน 60-90 วัน

**สำหรับ ecosystem:** Winners — **Visa + Mastercard + Stripe** ได้ new revenue stream (verification fee + transaction network fee) โดย infrastructure เดิม; **Lianlian + Airwallex + Nium** (cross-border payment fintech) ได้ competitive moat จาก TAP registration ที่ยากกว่า newcomer จะ replicate; **enterprise procurement software** (Coupa, SAP Ariba, Ivalua) จะเจอ SMB market disruption จากล่าง. Losers — **manual procurement outsourcing service** (upto $50B market globally), **B2B marketplace ที่ position ตัวเองเป็น "human-verified supplier network"** (Alibaba B2B, Made-in-China, Global Sources) — ต้องปรับ product ให้ agent-friendly ภายในไตรมาส 4. **Cryptocurrency payment rail** (USDC, PYUSD, stablecoin) เสีย seat เพราะ card network ยอมรับ agent ก่อน crypto จะขึ้น mainstream B2B

## Sources
- [Visa and Lianlian Advance Trusted B2B Agentic Commerce Through LoopXPay's First Live B2B Agentic Transaction — PR Newswire](https://www.prnewswire.com/apac/news-releases/visa-and-lianlian-advance-trusted-b2b-agentic-commerce-through-loopxpays-first-live-b2b-agentic-transaction-302833916.html)
- [Visa and Lianlian complete Greater China's first live agentic B2B payment — Electronic Payments International](https://www.electronicpaymentsinternational.com/news/visa-lianlian-greater-china-first-live-agentic-b2b-payment/)
- [Visa, HK's Lianlian Complete Live B2B Purchase Using AI Agent — Crowdfund Insider](https://www.crowdfundinsider.com/2026/07/293670-visa-hks-lianlian-complete-live-b2b-purchase-using-ai-agent/)
- [Visa, LianLian Automate Cross-Border B2B Payment With AI Agent — Caixin Global](https://www.caixinglobal.com/2026-07-27/visa-lianlian-automate-cross-border-b2b-payment-with-ai-agent-102468413.html)
- [Visa and Lianlian Take Agentic AI Into B2B Payments — finews.asia](https://www.finews.asia/finance/45008-visa-lianlian-agentic-ai-b2b-payments)
- [Visa and Lianlian complete first live B2B agentic transaction with AI-powered LoopXPay agent — Dealroom.co](https://app.dealroom.co/news/feed/visa-and-lianlian-complete-first-live-b2b-agentic-transaction-with-ai-powered-loopxpay-agent)
- [Visa, Lianlian complete first B2B AI agent payment — IBS Intelligence](https://ibsintelligence.com/ibsi-news/visa-lianlian-complete-first-b2b-ai-agent-payment/)

---

## Audio script
วันที่ 24 กรกฎาคม Visa และ Lianlian DigiTech บริษัทเพย์เมนต์ฟินเทคฮ่องกง ประกาศเสร็จสมบูรณ์ B2B agentic transaction ตัวแรกใน Greater China. Agent ชื่อ LoopXPay ระบุซัพพลายเออร์ เปรียบเทียบ ordered แล้วจ่ายเงินผ่าน Visa network ในเวิร์กโฟลว์เดียว. ทั้งหมดใช้เวลาไม่ถึง 5 นาที เทียบกับ manual procurement ที่ต้องใช้ 2 ถึง 4 ชั่วโมง.

หัวใจของ deal คือ Visa Trusted Agent Protocol และ Visa Agentic Directory ที่ Visa เปิดเมื่อมีนาคม. Agent ที่จะ execute transaction ต้องผ่าน audit 6 ถึง 8 สัปดาห์ Visa ตรวจ prompt injection defense, spending guardrail, human-in-loop policy. LoopXPay เป็น agent แรกใน APAC ที่ผ่าน. เทียบกับ US ที่มี Perplexity Comet Purchase, OpenAI Operator Wallet, Anthropic Claude Purchase Extension live มาตั้งแต่ไตรมาส 2.

Signal ที่สำคัญที่สุดคือ 3 เรื่อง. หนึ่ง — card network เดิมได้ role ใหม่เป็น identity broker แทนแค่ transaction router. Visa Mastercard Stripe จะเป็น 3-horse race เรื่อง B2B agent payment ก่อนสิ้นปี. สอง — Asia ก่อน US เพราะ regulate ก่อน CAC Hong Kong Monetary Authority ปล่อย tiered agent framework แล้ว. Sarbanes-Oxley ยัง gray area เรื่องนี้. สาม — SMB market ที่จะเกิด vertical B2B agentic payment startup ในไตรมาสหน้าทุก region. สำหรับ Enabridge — Thai fintech อย่าง 2C2P Omise LightNet ควร partner กับ SI ทันที ก่อน foreign player อย่าง LoopXPay หรือ Airwallex เข้าตลาดไทยไตรมาส 4.
