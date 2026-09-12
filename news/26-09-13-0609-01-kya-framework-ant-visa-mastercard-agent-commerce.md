---
date: 2026-09-13
slug: kya-framework-ant-visa-mastercard-agent-commerce
topic: openbridge-trend
reading_time_min: 5
sources: 5
image_prompt: |
  A editorial illustration of three massive vault doors labeled "VISA",
  "MASTERCARD", and "ANT" fusing into one shared portal in the center
  stamped "KYA — KNOW YOUR AGENT"; a stream of tiny robot silhouettes
  carrying shopping bags walks through the portal from left to right;
  three stacked numbers above read "$3–5T BY 2030", "$100B FRAUD",
  "3 PROTOCOLS → 1". Editorial isometric style, deep indigo background
  with gold accents, strong rim light, high-contrast readable at 200px
  thumbnail, 1:1 aspect, no real human faces.
image: images/26-09-13-0609-01-kya-framework-ant-visa-mastercard-agent-commerce.png
---

# Visa + Mastercard + Ant International เปิด "Know-Your-Agent" (KYA) — 3 protocol คู่แข่งยอมมาโต๊ะเดียว, agentic commerce เข้าเฟส standardized

## TL;DR
- Ant International, Visa, Mastercard ประกาศเมื่อ **9–10 ก.ย.** ว่าจะ align 3 protocol ที่แต่ละค่ายมีของตัวเอง — Visa **Trusted Agent Protocol**, Mastercard **Verifiable Intent**, Ant **Agentic Mobile Protocol** — ให้ interoperable ผ่าน framework ใหม่ชื่อ **Know-Your-Agent (KYA)**
- Target market: agent จะ orchestrate consumer commerce **$3–5 trillion ทั่วโลกภายในปี 2030** (Ant/Visa cite); PYMNTS Intelligence ระบุว่า **~90% ของ enterprise** ยอมรับว่า bot management เป็น "major challenge" — outdated identity ทำให้เสียหาย **~$100B ต่อปี**จาก fraud / false decline
- ยังเป็น "principles alignment" ไม่ใช่ spec เดียวที่ merge — แต่ signal ชัดว่า 3 network ยักษ์ ยอมรับว่าตลาดจะไม่ทนกับ agent identity ที่ห้าง/wallet/protocol แต่ละค่ายเช็คแยกกัน
- นี่คือ moment เดียวกับที่ 3DS 1.0 (2001) รวม issuer + acquirer + wallet เข้า flow เดียว — **KYA อาจเป็น "3DS ของ agent"**

## เกิดอะไรขึ้น

วันพุธ–พฤหัส **9–10 กันยายน** — Ant International, Visa, Mastercard ปล่อย joint statement ว่าจะ collaborate บน "Know-Your-Agent interoperability framework". สิ่งที่ประกาศชัดใน press release คือ 3 network ยอมรับว่าแต่ละคนมี protocol ของตัวเอง — Visa **Trusted Agent Protocol** (ประกาศต้นปี), Mastercard **Verifiable Intent** (Q2 2026), Ant **Agentic Mobile Protocol** (Alipay/Ant flywheel เอเชีย) — และตกลงจะ **"work toward common principles"** ให้ card network + digital wallet + agent platform + marketplace รู้จัก agent เดียวกันข้ามระบบได้

Jiang-Ming Yang, Chief Innovation Officer ของ Ant International, ให้ quote ที่ควรเน้น: "We look forward to expanding collaboration as the industry draws on richer signals". คำสำคัญคือ "richer signals" — แปลว่า KYA ไม่ใช่แค่ ID ของ agent (เจ้าของใคร, model อะไร, spec version ไหน) แต่รวมถึง **behavior signal** ที่ network ทั้งสามมีอยู่แล้ว: transaction pattern, device fingerprint, biometric baseline, spend velocity, geographic anomaly ทั้ง 3 network ใช้ราคาแพงในการดูแลอยู่แล้ว 

ตัวเลขที่ 3 network ยกมาสนับสนุนคือ **$3–5 ล้านล้านดอลลาร์** ของ consumer commerce ที่ agent จะ orchestrate ภายในปี 2030 (ตัวเลข Bain / McKinsey ที่ Ant cite), **~90% ของ enterprise** ที่ตอบ PYMNTS Intelligence ว่า bot management เป็น "major challenge", และ **~$100 พันล้าน**ต่อปีที่ธุรกิจสูญเสียจาก outdated identity control (fraud + false decline + lost customer combined). เป้าคือ **ลด integration cost + duplicate verification** ที่ตอนนี้ merchant + wallet + agent developer ต้อง onboard แยกกับแต่ละ network

ยังเป็นเพียง **principles alignment** — ไม่ใช่ merged specification เดียว ไม่ใช่ open standard body — แต่การที่ Visa (US card rail), Mastercard (US card rail), และ Ant (Alipay รายใหญ่จีน) มายืนบนเวทีเดียวกันในเรื่อง agent identity คือ moment ที่ไม่เคยเกิดในระดับ payment protocol อื่นเลย ตั้งแต่ 3-D Secure (2001, EMVCo consortium) และ EMV chip (1996). Roadmap ที่ทั้ง 3 hint คือ H1 2027 จะมี pilot deployment กับ marketplace ยักษ์ (Amazon, Alibaba, Shopify ถูก mention เป็น candidate)

## ทำไมสำคัญ

Pattern ที่เห็นชัดคือ **payment rail incumbent เข้ามา "own" agent identity layer ก่อนที่ browser / OS / LLM vendor จะทำ**. ถ้าปล่อยไว้อีก 12 เดือน OpenAI (Agents API เพิ่งเปิด public beta 10 ก.ย. — ดูคลิปถัดไป), Anthropic (Computer Use + MCP), Google (ADK + Agent Space), Apple/Google ในระดับ OS จะ define ว่า agent identity คืออะไร แล้ว payment network จะต้อง comply. การเคลื่อนไหวรอบนี้แปลว่า Visa/Mastercard/Ant อยาก define ก่อน — และให้ LLM vendor + browser adapter ตาม

signal ที่คมกว่านั้นคือ **Ant International อยู่บนเวทีเดียวกับ Visa/Mastercard**. ปกติ Ant + Alipay อยู่คนละ regulatory sphere กับ US card network — การที่ Ant ยอม open protocol ให้ interoperate เท่ากับยอม concession ว่าตลาด Chinese/APAC agent commerce จะไม่ closed ecosystem — และในทางกลับกัน Visa/Mastercard ยอมรับว่าโดยไม่มี Ant (ที่ครอบ ~1.2B active user ใน Alipay + shop + wallet globally) จะไม่มี "global" agent standard. นี่คือ trade-off ที่ทั้ง 2 ฝั่งเห็น TAM ใหญ่กว่าจึงยอมยืนร่วมกัน

เทียบกับ moment ประวัติศาสตร์: **3-D Secure 1.0** (2001) ที่ Visa initiate ก่อน แล้ว Mastercard/JCB/AmEx ตามเข้าใน EMVCo — ทำให้ e-commerce online payment ได้ authentication framework เดียว ราคา fraud loss ลดจาก ~0.30% ของ transaction เหลือ ~0.05% ในเวลา 5 ปี. KYA ในบริบท agentic commerce มีศักยภาพเป็น "3DS 2.0 for agent" — ถ้าทำสำเร็จ **agent จะ transact ข้าม platform ได้โดยไม่ต้อง re-onboard ทุกครั้ง**. ถ้าล้ม จะกลายเป็นแค่ RFC บนกระดาษเหมือน Web Payments API 2015 ที่ไม่มี network ยอม default

## มุม AI Agent Platform

**สำหรับ Builders** ที่กำลังสร้าง agent framework / commerce agent / autonomous shopper: (1) เริ่ม **evaluate KYA spec** ทันที่มัน publish (Q4 2026 – Q1 2027 คาด) — implementation cost ยิ่งเข้าเร็วยิ่งต่ำ; (2) architect agent identity layer ให้ **pluggable** — อย่า hardcode Visa TAP หรือ Mastercard VI ตัวเดียว เพราะ KYA จะ mandate multi-protocol dispatcher; (3) จับตา **agent-signed credential** pattern — LangChain / CrewAI / OpenAI Agents API ยังไม่มี native attestation layer, KYA อาจ force มาตรฐาน x509-style agent cert ที่ทุก framework ต้อง sign transaction ด้วย

**สำหรับ Users / Business** ที่กำลัง deploy agent ใน commerce workflow: (1) ถ้ามี merchant account อยู่แล้ว, ถามผู้ให้บริการ payment ว่ามี KYA roadmap ไหม — Stripe, Adyen, Fiserv, Worldpay คาดว่าจะทยอยประกาศ within 30–60 วัน; (2) ระวัง **false decline rate spike** ตอนช่วง transition (agent traffic ที่ทำโดย legitimate customer แต่ยัง unverified) — เตรียม fallback path ให้ human intervention รับได้; (3) SME/startup Thai ที่ใช้ Alipay+/GrabPay/PromptPay agentic checkout — Ant มี direct pipeline เข้ามาก่อน US network ในภูมิภาค คุยกับ acquirer + wallet partner ตั้งแต่ Q4 2026

**สำหรับ Ecosystem** (vendor / cloud / protocol): identity provider (Okta, Auth0, Ping, Cloudflare Zero Trust) จะโดน pressure ให้ integrate เป็น "KYA-compliant issuer" — ถ้าไม่ทำก็โดน bypass; W3C Verifiable Credentials + DID community น่าจะโดน invite เข้าเป็น neutral standard body (Ant hint ถึง "richer signals" คือคำใบ้); **Thailand PDPC + BOT** ที่กำลังพิจารณา agent guideline ควรใช้ KYA เป็น baseline reference — Bangladesh Bank + BSP Philippines + MAS Singapore ก็จะทำแบบนั้น เพราะไม่มีใครอยากเป็นประเทศเดียวที่ agent onboard cost สูงกว่าเพื่อน

## Sources
- [PYMNTS — Visa and Mastercard Team With Ant on Know Your Agent Framework](https://www.pymnts.com/cybersecurity/2026/visa-mastercard-team-with-ant-know-your-agent-framework)
- [Unite.AI — Ant International, Visa, Mastercard Align on AI Agent Verification Rules](https://www.unite.ai/ant-international-visa-mastercard-align-on-ai-agent-verification-rules/)
- [Forkast — Ant International, Visa, and Mastercard Agree on Agent Identity Standard. Now Comes the Hard Part](https://forkast.news/ant-international-visa-and-mastercard-agree-on-agent-identity-standard-now-comes-the-hard-part/)
- [Electronic Payments International — Ant, Mastercard and Visa collaborate on KYA to scale agentic commerce](https://www.electronicpaymentsinternational.com/news/ant-mastercard-visa-kya-agentic-commerce/)
- [Investing News Network — Ant International, Mastercard and Visa Initiate Collaboration on Know-Your-Agent Interoperability](https://investingnews.com/ant-international-mastercard-and-visa-initiate-collaboration-on-know-your-agent-interoperability-to-scale-agentic-commerce/)

---

## Audio script
วันพุธและพฤหัส เก้าถึงสิบกันยายน. Ant International Visa Mastercard ประกาศร่วมกันว่าจะสร้าง framework ชื่อ Know Your Agent หรือ KYA เพื่อให้ AI agent ที่ไปซื้อของแทนคน onboard และยืนยันตัวตนได้ข้าม network. Visa มี Trusted Agent Protocol ของตัวเอง. Mastercard มี Verifiable Intent. Ant มี Agentic Mobile Protocol. สามค่ายจะ align มา common principle เดียวกัน.

ตัวเลขที่ทั้งสามยกมาน่าสนใจ. Agent จะ orchestrate consumer commerce สามถึงห้าล้านล้านเหรียญทั่วโลกภายในปี 2030. เก้าสิบเปอร์เซ็นต์ของ enterprise บอกว่า bot management เป็น major challenge. หนึ่งแสนล้านเหรียญต่อปี เสียหายจาก outdated identity control ทั้ง fraud และ false decline.

Jiang Ming Yang Chief Innovation Officer ของ Ant ให้คำที่ควรจับ. richer signals. แปลว่า KYA ไม่ใช่แค่บอกว่า agent ตัวนี้ใคร ของ vendor ไหน แต่จะรวม behavior signal ที่ network ทั้งสามมีอยู่แล้ว. transaction pattern. device fingerprint. spend velocity. geographic anomaly. รวมเข้าเป็นสัญญาณ trust แบบ real time.

ยังเป็น principles alignment ไม่ใช่ merged spec เดียว. ยังไม่มี timeline ปิด. แต่การที่ Visa Mastercard Ant มายืนบนเวทีเดียวกันในเรื่อง identity ยังไม่เคยเกิดขึ้นเลยตั้งแต่สาม D Secure ปี 2001. ตอนนั้น Visa เริ่มก่อน แล้ว Mastercard JCB AmEx ตามเข้า EMVCo. e-commerce online payment ได้ authentication framework เดียว. fraud loss ลดจากศูนย์จุดสามเปอร์เซ็นต์เหลือศูนย์จุดศูนย์ห้าในห้าปี. KYA ในบริบท agent มีศักยภาพเป็น 3DS 2.0 for agent.

pattern ที่ต้องอ่านคือ payment rail incumbent เข้ามา own agent identity ก่อนที่ browser LLM vendor หรือ OS จะทำ. ถ้าปล่อยอีก 12 เดือน OpenAI Anthropic Google Apple จะ define agent identity แล้ว payment network จะต้อง comply. Visa Mastercard Ant อยาก define ก่อน.

signal ที่คมกว่าคือ Ant อยู่บนเวทีเดียวกับ US card network. ปกติ Ant Alipay อยู่คนละ sphere กับ Visa Mastercard. การที่ Ant ยอม open protocol เท่ากับยอมรับว่าตลาด Chinese APAC agent commerce จะไม่ closed. และในทางกลับกัน Visa Mastercard ยอมรับว่าถ้าไม่มี Ant ที่ครอบหนึ่งจุดสองพันล้าน active user ก็ไม่มี global standard.

สำหรับผู้สนใจตลาดไทยและ APAC. Ant มี direct pipeline เข้ามาก่อน US network. Alipay+ GrabPay PromptPay agentic checkout จะมาก่อน. SME ไทยที่ใช้ payment provider เหล่านี้ควรถาม roadmap ตั้งแต่ Q4 2026. Stripe Adyen Fiserv Worldpay คาดว่าจะประกาศ KYA support ใน 30-60 วัน.

builder ที่กำลังสร้าง agent commerce framework ต้อง architect identity layer แบบ pluggable. อย่า hardcode protocol ของ network เดียว. เพราะ KYA จะ mandate multi protocol dispatcher. และจับตา agent signed credential pattern ที่ทุก framework จะต้อง sign transaction ด้วย.
