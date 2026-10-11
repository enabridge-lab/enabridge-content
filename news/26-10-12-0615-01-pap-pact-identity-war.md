---
date: 2026-10-07
slug: 26-10-12-0615-01-pap-pact-identity-war
topic: agentic-ai
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial hero: two massive glass front doors to a storefront labeled
  "YOUR BUSINESS". The left door has a shield stamped "PAP — META × SIERRA",
  the right door has a shield stamped "PACT — DECAGON × INSTINCT". A tiny
  robot courier labeled "AGENT" stands between them holding two OAuth
  key-cards, confused about which door to use. A banner across the top reads
  "WHO DOES THE AGENT REPRESENT?". Isometric vector, cobalt + warm orange
  accents on slate background, 1:1 aspect, no real human faces, text clearly
  readable at 200px thumbnail.
image: images/26-10-12-0615-01-pap-pact-identity-war.png
---

# สองโปรโตคอลใหม่สำหรับ "เอเจนต์เคาะประตูธุรกิจ" — PAP กับ PACT เริ่มสงครามเลเยอร์ identity ก่อนเลเยอร์ payment

## TL;DR
- 6 ต.ค. 2026 **Meta + Sierra** เปิด **Personal Agent Protocol (PAP)** — มาตรฐานเปิดให้ personal agent "sign in" เข้าธุรกิจแบบที่ธุรกิจรู้ว่าคือเอเจนต์ของใคร; **Walmart, Shopify, Stripe, Genesys, Rocket, Instinct** ประกาศเข้าร่วมก่อน spec v0.1 จะออกด้วยซ้ำ
- 1 ต.ค. **Decagon** เปิดคู่แข่ง **PACT (Personal Agent Consent & Trust)** สร้างบน A2A + OAuth 2.0 และ **open-source spec พร้อม** ที่ openpactprotocol.org — คนที่อยู่ใน PAP working group เองก็ไป co-develop PACT ด้วย
- ทั้งสอง protocol **เลือก identity ก่อน payments** — เป็นสัญญาณชัดว่า bottleneck ของ agentic commerce ปี 2027 ไม่ใช่ "เอเจนต์จ่ายเงินยังไง" แต่คือ "ธุรกิจรู้ได้ไงว่าตัวที่กำลังคุยอยู่คือเอเจนต์ของลูกค้า ไม่ใช่ bot ปลอม"

## เกิดอะไรขึ้น

สัปดาห์แรกของเดือนตุลาคม 2026 เป็นสัปดาห์ที่โลก agent protocol เพิ่มสองชั้นใหม่พร้อมกัน — และทั้งคู่เลือก **เลเยอร์ identity** เป็นเลเยอร์แรกที่จะปิดก่อน. วันที่ 6 ต.ค. Meta ร่วมกับ Sierra ประกาศ **Personal Agent Protocol (PAP)** หลังจาก Amazon บล็อก Muse agent ของ Meta ไม่กี่สัปดาห์ก่อน โดยอ้างว่าตัว agent "ไม่ยอมบอกว่าคือใคร". PAP แก้ปัญหานี้แบบตรงเป้า: ให้ personal agent (เช่น ChatGPT, Gemini, Muse) sign-in เข้า storefront ของธุรกิจผ่าน OAuth เดียวกันกับที่ขับเคลื่อน "Sign in with Google"

PAP แบ่งโหมดเข้าธุรกิจเป็นสองระดับ. **Guest mode** — agent ทำงานทั่วไปอย่างเช็กสต็อก, อ่าน return policy, เปิด product spec ได้โดยไม่ต้อง login. **Authenticated mode** — เมื่อเอเจนต์ต้องแตะ account ของลูกค้า (เช็ก order, สั่งซ้ำ, จัดการ subscription) ลูกค้า sign-in ที่หน้าเว็บของธุรกิจเอง ไม่ใช่ในหน้าของ agent, แล้วเลือกให้ scope เป็น read-only หรือ write. หนึ่ง session carry ข้าม website, API, และ channel ของธุรกิจได้. Partners ที่เปิดเผย ณ วันประกาศคือ **Walmart, Shopify, Stripe, Genesys, Rocket, และ Instinct** — ซึ่งน่าสังเกตเพราะ spec v0.1 ยังไม่ออก (Sierra สัญญา "ภายในสิ้นเดือน ต.ค.") และยังไม่มี governing body ประกาศ

แต่ Decagon ชิงออกตัวก่อน 5 วัน. เมื่อ 1 ต.ค. ที่ event **Decagon Dialogues 2026** บริษัทเปิด **PACT (Personal Agent Consent & Trust Protocol)** พร้อม **Personal Agent Gateway** — และ 6 ต.ค. ก็ open-source ทั้ง spec และ reference implementation ที่ openpactprotocol.org สร้างคู่กับ Instinct. จุดต่างที่สำคัญ: PACT ไม่ได้สร้างใหม่หมด แต่ build บน **A2A (Agent2Agent)** สำหรับ discovery และใช้ **OAuth 2.0 device authorization flow** สำหรับ delegated consent. ธุรกิจประกาศ Agent Card ของตัวเอง ลงรายการ scope เช่น `orders:read` หรือ `orders:cancel`, แล้วให้เอเจนต์ "แสดงบัตร" ตอนขอทำแต่ละอย่าง

Point ที่สับสนที่สุด — **Instinct อยู่ทั้งสองค่าย**. Instinct เป็น partner ที่ Meta/Sierra ลิสต์ใน PAP announcement และ Decagon ลิสต์เป็น co-developer ของ PACT. ซึ่งอาจตีความได้สองแบบ: (ก) Instinct เตรียมสะพานระหว่างสองโปรโตคอลและเดิมพันกับทั้งคู่ หรือ (ข) ยังไม่มีใครรู้แน่ว่าเกมนี้จะจบที่โปรโตคอลเดียว เลยไม่กล้าเลือกข้าง. ขณะเดียวกัน Forkast ตีข่าว 10 ต.ค. ว่า **PAP v0.1 ยังไม่ shipped, A2A Agent Registry ยังไม่มี formal spec, และ Google Gemini Agent ยังไม่ถึง GA** — สามเสาแห่ง roadmap ตุลาคม 2026 พลาด deadline ทั้งหมด

ที่ชัดเจนที่สุดคือ **ทั้ง PAP และ PACT เลือกตัด payments ออกจาก v1 อย่างจงใจ**. ปีที่แล้ว agentic commerce ทั้งตลาดโฟกัสที่ "เอเจนต์จ่ายเงินยังไง" (Stripe Agentic Checkout, Visa Intelligent Commerce, Mastercard Agent Pay). ปีนี้ pivot แล้ว — ก่อนจะคุยเรื่องเงินได้ ต้องแก้เรื่อง "ธุรกิจรู้ได้ไงว่าใครคุยอยู่"

## ทำไมสำคัญ

**Identity-first คือการยอมรับ reality ของ attack surface.** ตั้งแต่ Amazon บล็อก Muse ไปจนถึง Walmart ล็อก scraping ของ ChatGPT และ Reddit ต่อสู้กับ bots มาเกือบปี, patterns ชัดว่า **ธุรกิจไม่ไว้ใจ traffic จาก agent ที่ไม่ identify ตัวเอง**. วิธีก่อนหน้าคือ user agent string + CAPTCHA + rate limit — ซึ่งเลเยอร์พวกนี้ไม่พอรับคลื่น agentic traffic ที่คาดว่าจะมี 150K+ agent ต่อ Fortune 500 ภายใน 2028 (Gartner forecast ที่อ้างใน Google Gemini Agent launch สัปดาห์ที่แล้ว). PAP + PACT เสนอ identity primitive แทน: "เอเจนต์ตัวนี้แทนลูกค้าชื่อ X, มี scope เท่านี้, business validate กลับที่ IdP ของตัวเองได้"

**การแยก two-protocol competition ตั้งแต่ day 1 คือ bad news สำหรับทุกคน.** ประวัติศาสตร์เตือน: WAP vs i-mode, SSL vs TLS, OpenID vs SAML — การมีสอง spec ขัดกันตั้งแต่แรกยืดเวลา adoption ออกไป 3–5 ปีเสมอ. ครั้งนี้ **PACT ชนะเกม spec speed** (open-source แล้ว) แต่ **PAP ชนะเกม distribution** (Walmart + Shopify + Stripe = coverage ครึ่งหนึ่งของ US retail checkout). วิธีจบที่น่าจะเป็นที่สุดคือ convergence — ทั้งคู่สร้างบน OAuth เหมือนกัน, PACT build บน A2A, PAP build บน MCP + OpenAPI, อาจรวม sublayer ของกันและกันในที่สุด. แต่ระหว่างทางคือ 12-18 เดือนที่ builder ต้อง support ทั้งคู่

**Payments-last คือ reversal ของ playbook ที่เรารู้จัก.** Visa, Mastercard, Stripe ทุ่มลง agentic payment infrastructure ตลอดปี 2025–26 โดยสมมติว่า "เอเจนต์จ่ายเงินได้แล้วค่อยคุยเรื่องอื่น". สัปดาห์นี้บอกตรงกันข้าม: **merchant ไม่เปิดกระเป๋าสตางค์ให้ agent ที่ไม่ identify ตัวเอง** — เลเยอร์ identity ต้องมาก่อน. ซึ่งก็หมายความว่า Stripe (ที่อยู่ใน PAP partner list) น่าจะใช้ PAP เป็น "sign-in gate" ก่อน agentic checkout — payment สวมเลเยอร์ identity ของ PAP แทนที่จะเดินทางคู่ขนาน

## มุม AI Agent Platform

**Builders:** คนทำ agent framework ต้องตอบคำถามใหม่ — "agent ของคุณ sign-in อย่างไร ให้ธุรกิจตรวจสอบได้?". LangChain, Mastra, CrewAI, Vercel AI SDK ต้อง ship PAP + PACT adapter ก่อนสิ้นปี ไม่งั้นผลิตภัณฑ์ที่สร้างบนเฟรมเวิร์กนั้นจะเจอ 403 ที่ merchant ไปทีละราย. ส่วน builder ที่สร้าง **personal agent product** โดยตรง (เช่น ChatGPT, Gemini, Claude, Muse, Perplexity) จะเจอ pressure หนักที่สุด — ไม่สามารถเล่น "incognito browsing" ได้อีกต่อไป, ต้องตัดสินใจว่าจะ ship native PAP + PACT หรือเจอ enterprise merchant ตัดไฟ

**Users / business:** CIO ของ retail, hospitality, SaaS, และ consumer finance ที่โดน scraping-traffic กัดต้นทุน server มาตลอดปี มี path ชัดขึ้น — ติด Agent Card, publish OAuth endpoint, ลง scope definition, แล้ว agent traffic กลายจาก "DDoS ที่หน้า bot ปลอม" เป็น "customer segment ใหม่". **Ecosystem:** OAuth provider (Auth0, Okta, Microsoft Entra, Google Identity) เป็น quiet winner — delegated authorization คือสิ่งที่พวกเขาขายอยู่แล้ว. Hyperscaler agent runtime (Google Gemini Agent, Microsoft Agent 365, AWS Bedrock) ต้อง embed support ให้ลูกค้าของตัวเองไว้ใจพาเอเจนต์ไปเคาะประตูธุรกิจอื่น. ส่วนทีมที่สร้าง vertical agent app ในไทย (banking agent, insurance agent, telco agent) ควรเริ่มคุยกับ security team วันนี้ว่าจะ expose Agent Card format ไหน — เพราะเลเยอร์นี้คือสิ่งที่ปิด gap ระหว่าง "agent demo สวย" กับ "agent production ที่ลูกค้าต่างจังหวัดเสียบใช้งานจริง"

## Sources
- [Sierra and Meta's Personal Agent Protocol Gives Commerce a Common Front Door — Yahoo Tech](https://tech.yahoo.com/ai/meta-ai/articles/sierra-meta-personal-agent-protocol-024451270.html)
- [Meta and Sierra's Personal Agent Protocol Starts With Login, Not Payments — Datafloq](https://datafloq.com/meta-and-sierras-personal-agent-protocol-starts-with-login-not-payments/)
- [Meta's Personal Agent Protocol Signs Walmart Before It Has a Spec — Beri.net](https://www.beri.net/article/meta-sierra-personal-agent-protocol-oauth-guest-read-write-access-vs-ucp-acp-trusted-agent-protocol-retail-banks)
- [Introducing the Personal Agent Consent & Trust Protocol (PACT) — Decagon](https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact)
- [Decagon Personal Agent Gateway explained: detection, scopes and PACT — eesel.ai](https://www.eesel.ai/blog/decagon-personal-agent-gateway)
- [Three Agent Specs Promised for October Remain Unshipped — Forkast](https://forkast.news/three-agent-specs-promised-for-october-remain-unshipped-the-vendor-extensions-filling-the-vacuum-are-fragmenting-the-stack/)

---

## Audio script
สัปดาห์แรกของเดือนตุลาคมปีนี้มีสองโปรโตคอลใหม่สำหรับเอเจนต์เคาะประตูธุรกิจ โผล่พร้อมกัน. วันที่ 1 ตุลาคม Decagon เปิด PACT ที่ event ของตัวเอง ย่อมาจาก Personal Agent Consent and Trust. วันที่ 6 ตุลาคม Meta และ Sierra เปิด Personal Agent Protocol หรือ PAP. ทั้งคู่สร้างบน OAuth เหมือน Sign in with Google. ทั้งคู่ตั้งใจตัด payments ออกจาก version แรก. ทั้งคู่เลือกเลเยอร์ identity เป็นเลเยอร์แรกที่จะปิด. จุดที่น่าสังเกตคือ merchant ยอม commit ก่อน spec จะออก. Walmart Shopify Stripe Genesys Rocket Instinct เซ็นเข้า PAP ก่อน spec v0.1 จะ ship ด้วยซ้ำ. ขณะที่ PACT open-source spec พร้อม reference implementation ไปแล้วที่ openpactprotocol.org. จุดสับสนที่สุดคือ Instinct อยู่ทั้งสองค่าย. ส่วน Google Gemini Agent GA, PAP v0.1, และ A2A Agent Registry formal spec — สามเสาแห่ง roadmap ตุลาคมพลาด deadline ทั้งหมด ตามการตีข่าวของ Forkast. เรื่องนี้สำคัญเพราะมันบอกว่า bottleneck ของ agentic commerce ปี 2027 ไม่ใช่ เอเจนต์จ่ายเงินยังไง. แต่คือ ธุรกิจรู้ได้ไงว่าตัวที่กำลังคุยอยู่คือเอเจนต์ของลูกค้า ไม่ใช่ bot ปลอม. Amazon บล็อก Muse ของ Meta เพราะเหตุผลเดียวกัน. ตั้งแต่ Walmart ล็อก scraping ของ ChatGPT ถึง Reddit สู้ bots — pattern ชัดว่าธุรกิจไม่ไว้ใจ traffic จาก agent ที่ไม่ identify ตัวเอง. การมีสอง spec แข่งกันตั้งแต่ day 1 คือ bad news สำหรับทุกคน. ประวัติศาสตร์เตือนว่า WAP กับ i-mode, OpenID กับ SAML — สอง spec ขัดกันตั้งแต่แรกยืด adoption 3 ถึง 5 ปี. CIO retail hospitality SaaS ไทยควรเริ่มคุยกับ security team ตอนนี้ ว่าจะ expose Agent Card format ไหน เพราะเลเยอร์นี้คือสิ่งที่ปิด gap ระหว่าง agent demo สวย กับ agent production ที่ใช้งานจริง
