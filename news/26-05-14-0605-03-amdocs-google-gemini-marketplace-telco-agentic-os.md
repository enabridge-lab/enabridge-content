---
date: 2026-05-13
slug: amdocs-google-gemini-marketplace-telco-agentic-os
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: A glowing telecom control room with massive video walls showing a global network map, while in the foreground a bold storefront-style facade reads "GEMINI ENTERPRISE AGENT MARKETPLACE" in tall typography. On a center shelf the Amdocs "aOS" logo glows next to the Google Gemini logo, with floating agent cards labeled "CARE", "ORDER", "BILLING" arranged like products. Telco towers and 5G signal arcs frame the composition, no human faces visible. Cool tech-blue and signal-orange palette, isometric editorial illustration, high contrast for thumbnail readability, 1:1.
image: images/26-05-14-0605-03-amdocs-google-gemini-marketplace-telco-agentic-os.png
---

# Amdocs ลง Google Gemini Marketplace — vertical agentic OS เริ่ม ship เป็นสินค้า

## TL;DR
- Amdocs (13 พ.ค.) เปิดตัว Telco Agents for Customer Experience บน Google Gemini Enterprise Agent Marketplace — agent สำเร็จรูปสำหรับ communications service providers (CSPs)
- Stack: Amdocs aOS (telco agentic OS) + Cognitive Core + Gemini Enterprise; ครอบ care, service request, issue resolution, order orchestration; coordinate ข้าม BSS/OSS เดิม
- Signal: vertical agent ขยับจาก "build your own" → "buy off the shelf in marketplace". Telecom เป็นเคสแรก แต่ pattern จะลามถึง healthcare, banking, retail ภายในไตรมาส

## เกิดอะไรขึ้น

วันที่ 13 พ.ค. Amdocs ประกาศว่า "Amdocs Telco Agents for Customer Experience" available บน Google Gemini Enterprise Agent Marketplace แล้ว — เป็นหนึ่งใน wave ของ partner-built agents ที่ Google เริ่มเปิดให้ enterprise customer ของ Gemini Enterprise มา shop ตรง ๆ หลังประกาศ marketplace นี้ที่ Google Cloud Next 2026

Architecture ที่ Amdocs โชว์มี layer ชัด ใต้สุดคือ aOS — agentic operating system สำหรับ telco ที่ Amdocs build มาเอง ทำ orchestration ข้าม BSS/OSS เดิม (Amdocs install อยู่ใน CSP ใหญ่กว่า 80% ของโลกอยู่แล้ว). ตรงกลางคือ Cognitive Core — reasoning + governance layer ที่รู้ telco semantics เช่น service catalog, charging, dispute logic. ชั้นบนใช้ Gemini Enterprise เป็น model + planner. ผลลัพธ์ที่ user-facing คือ agent ที่จัดการ care interaction, service request, issue resolution, order orchestration ได้แบบ end-to-end โดยไม่ต้อง human escalate

Amdocs ยังไม่ปล่อยตัวเลข deployment ของรอบนี้ (Q3 2026 earnings guidance ที่ออกพร้อมกันบอกว่า AI/agentic revenue เริ่ม material แต่ไม่ break out) — แต่ pipeline ที่ระบุคือ Tier-1 CSP ใน North America + Europe, อ้างอิงประวัติ Amdocs ที่ run customer experience platform ของ AT&T, Vodafone, T-Mobile

## ทำไมสำคัญ

Story นี้ตัวเล็กในเชิง headline แต่ signal ใหญ่ในเชิง market structure. ปี 2024–25 enterprise คิดว่าจะต้อง "build" agent ของตัวเองด้วย LangChain/CrewAI/AutoGen. ปี 2026 marketplace model ของ Google Gemini Enterprise (และ Salesforce AppExchange Agent edition, AWS Bedrock Agents Marketplace ที่กำลังตามมา) เปลี่ยน default จาก build เป็น buy + customize — เหมือนตอน Salesforce AppExchange เปลี่ยน CRM economy ในยุค 2008–2012

ที่ Amdocs ทำได้ดีคือเดิน vertical ลึก ไม่ใช่ horizontal ตื้น. agent ของ Amdocs รู้จัก concept อย่าง "B2B contract uplift", "MVNO wholesale rate", "5G slice activation" — knowledge ที่ horizontal player (ServiceNow, Salesforce) ต้องใช้เวลานานกว่ามาก. นี่คือ pattern ที่จะลามถึง healthcare (Epic + Anthropic จะออก clinical agent), banking (FIS, Fiserv กำลัง pilot), insurance (Guidewire, Duck Creek). ใครเป็นเจ้าของ vertical OS เดิม + ออก agent ทับบนเอง → เจ้านั้นชิงได้

อีกอย่างที่น่าสังเกต — Amdocs ไม่ได้ลงทุน foundation model เอง แต่ใช้ Gemini ผ่าน marketplace deal. นี่คือ economics ที่ enterprise software vendor เก่าทุกเจ้ารู้ดี: ปล่อยให้ hyperscaler แข่ง compute, ตัวเองเก็บ business logic + customer relationship. POV: vertical SaaS ที่ "agent-wrap" ของเดิมจะกินก่อน horizontal AI startup จะตั้งหลัก — เพราะ distribution + domain knowledge ต่อรองไม่ได้

## มุม OpenBridge

Amdocs aOS เป็น mini-OpenBridge สำหรับ telco — orchestrate ข้าม BSS/OSS, ให้ semantic layer, แล้วเปิดให้ agent มา consume ผ่าน marketplace. นี่คือ playbook ที่ OpenBridge อาจ pick: เลือก vertical 1–2 ตัวที่ integration เป็นจุดปวดมาก (เช่น retail commerce, SME finance ops) แล้วทำ semantic layer + agent ที่ ship ใน marketplace ของ hyperscaler ใหญ่

อีก angle — เมื่อ telco operator customer ของ Amdocs เริ่ม run agent เหล่านี้จริง พวกเขาจะมี traffic ที่ "ออก" จาก aOS ไปจิก CRM (Salesforce), data warehouse (Snowflake), billing system อื่น. ตรงนั้นคือพื้นที่ที่ integration platform horizontal อย่าง OpenBridge ยังเล่นได้ — เพราะ Amdocs cover เฉพาะ telco boundary. การ position ที่ชัดคือ "เราคือ glue ระหว่าง vertical agent ของคุณกับ rest of stack" — ไม่ใช่ "เราคือ agent platform" ซึ่งกำลังจะ commoditized

## Sources
- [Amdocs Announces Availability of Telco Agents for Customer Experience in Google's Gemini Enterprise Agent Marketplace — Yahoo Finance](https://finance.yahoo.com/news/amdocs-announces-availability-telco-agents-202000772.html)
- [Partner-built agents available in Gemini Enterprise — Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/partner-built-agents-available-in-gemini-enterprise)
- [Amdocs Telco AI agents join Google Gemini marketplace — Stock Titan / DOX news](https://www.stocktitan.net/news/DOX/amdocs-announces-availability-of-telco-agents-for-customer-4jla35biv276.html)

---

## Audio script
ข่าวเล็กแต่ signal ใหญ่. Amdocs เมื่อวานประกาศว่า Telco Agents ของตัวเอง available บน Google Gemini Enterprise Agent Marketplace แล้ว — agent สำเร็จรูปที่ communications service provider ซื้อตรงจาก marketplace แล้ว plug เข้า BSS OSS เดิมได้เลย. Stack มีสามชั้น — aOS เป็น agentic operating system ของ Amdocs สำหรับ telco, Cognitive Core เป็น reasoning layer ที่รู้ telco semantic เช่น service catalog charging dispute, ชั้นบนใช้ Gemini เป็น model. ทำไมเรื่องนี้สำคัญ — ปี 2024 25 enterprise คิดว่าต้อง build agent ของตัวเองด้วย LangChain. ปี 2026 marketplace model เปลี่ยน default จาก build เป็น buy plus customize. นี่คือ moment เดียวกับที่ Salesforce AppExchange เปลี่ยน CRM economy เมื่อสิบกว่าปีก่อน. vertical SaaS ที่ wrap ของเดิมเป็น agent จะกินก่อน horizontal AI startup เพราะ distribution กับ domain knowledge ต่อรองไม่ได้. มุม OpenBridge คือ position ตัวเป็น glue ระหว่าง vertical agent กับ rest of stack ไม่ใช่ agent platform เพราะตรงนั้นกำลัง commoditized.
