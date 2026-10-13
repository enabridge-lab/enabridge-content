---
date: 2026-10-13
slug: rein-security-sidecar-agent-runtime
topic: use-case
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial illustration: a translucent "sidecar" pod velcroed to a larger
  pod labeled "AGENT", intercepting a glowing wire that tries to reach a
  vault marked "RESOURCES". Numbers "$25M SERIES A", "$35M TOTAL", "8X ARR",
  "5X CUSTOMERS" stacked on the right in bold editorial type, readable at
  thumbnail size. Dark cybersecurity navy + emergency-red accents, soft
  neon glow on the sidecar, flat isometric style, 1:1 aspect, no real human
  faces. Visual metaphor: a bouncer that lives next to each agent, not on
  the perimeter.
image: images/26-10-14-0615-03-rein-security-sidecar-agent-runtime.png
---

# Rein Security ได้ $25M Series A — sidecar architecture กำลังชนะ gateway บน agent runtime security

## TL;DR
- 8 ต.ค. **Rein Security** ปิด **$25M Series A** co-led โดย **Glilot Capital** + **Sienna Venture Capital** — รวม funding **$35M** ตั้งแต่ ก่อตั้ง 2024
- Product: **sidecar architecture** ที่ติดข้าง process ของ agent — ไม่ใช่ gateway, ไม่ใช่ proxy — ให้ **visibility ทุก line of code + ทุก resource access** พร้อม real-time block
- Customer อ้าง: **Dun & Bradstreet + Lemonade** — "secure thousands of agents" ที่ runtime; revenue โต **8x** นับจาก launch Jan 2026; customer base โต **5x**
- Team: 31 คน; HQ New York + Tel Aviv; CEO **Matan Bar-Efrat** ที่พูดชัดว่า target สองโลก — "secure the agents enterprise สร้างเอง" + "block adversarial agent ที่ attack enterprise"
- Pattern: Baselayer ($35M + "Know Your Agent") + Cyera–Oasis ($1B deal + "AI Trust Layer") + Rein = **agent trust layer กำลัง consolidate เป็น 3 primitive**: identity, runtime, data

## เกิดอะไรขึ้น

8 ต.ค. Rein Security ประกาศ Series A $25M co-led โดย Glilot Capital + Sienna Venture Capital พร้อมผู้ร่วมลงทุน Corner Ventures, Atlacle, RNP Capital Advisors — รวม total funding เป็น $35M. จุดต่างที่ชัดจาก Noma Security, Lasso Security, Prompt Security คือ **patent-pending sidecar architecture** ที่ไม่ sit ที่ gateway/proxy แต่ **ติดข้าง process ของ agent เอง** — มองเห็นทุก line of code ที่ run + ทุก resource ที่ access + สามารถ **block action harm แบบ real-time ก่อน execute**

ตัวเลขที่น่าสนใจ: นับจาก launch Jan 2026 revenue โต **8x** (base ไม่เปิดเผย), customer base โต 5x. Named customer คือ **Dun & Bradstreet** (data broker ที่ build internal agent สำหรับ fraud detection + credit scoring) + **Lemonade** (insurance ที่ build customer-facing agent) — ทั้งคู่อ้างว่าใช้ Rein เพื่อ "secure thousands of agents at runtime." Headcount 31 คน, HQ New York + Tel Aviv (Israeli-American pattern เดียวกับ Cyera + Oasis), CEO Matan Bar-Efrat positioning product เป็น **dual-use**: ปกป้อง agent ของ enterprise + block agent ของผู้ไม่หวังดีที่พยายามโจมตี enterprise

Pattern ที่ชัด: 90 วันผ่านมา (Jul–Oct 2026) มี **3 ดีลสำคัญใน "agent trust layer"** — **Cyera + Oasis** $1B deal (identity ของ non-human + agentic access governance), **Baselayer $35M Series A** (Agentic Identity Suite + "Know Your Agent" KYA ให้ bank verify ว่า agent ตัวไหนขอ API เข้ามา), และ **Rein Security $25M Series A** (runtime guardrail + sidecar). เพิ่ม Cisco buy Astrix (non-human identity) + CrowdStrike buy SGNL + Palo Alto $25B acquisition CyberArk — **ตลาด non-human identity + agent runtime security กำลัง consolidate เร็วกว่าที่ Gartner คาด**

สิ่งที่ Rein ทำได้ที่คู่แข่งทำยาก: **ไม่ต้องเปลี่ยน architecture ของ agent**. ลูกค้าที่ใช้ LangGraph, Claude Agent SDK, OpenAI AgentKit, Microsoft Copilot Studio ทุกเจ้า deploy sidecar ตัวเดียว — compared กับ gateway approach (Lasso, Prompt Security) ที่ต้อง route traffic ผ่าน proxy ซึ่ง (1) break streaming (2) break tool use timing (3) require ownership ของ auth flow. Sidecar ไม่มี 3 ปัญหานี้ — ซึ่งเป็น **adoption lever ที่สำคัญกว่า feature set**

## ทำไมสำคัญ

**Agent security กำลังย้ายจาก "model safety" (prompt injection detection) ไปสู่ "runtime containment"** (block ก่อน resource ถูก access). เมื่อ 12 เดือนที่แล้ว ตลาด agent security ขายของด้วย keyword "jailbreak prevention" + "prompt injection filter". วันนี้ enterprise จ่ายเงินให้ **(1) agent ของเราห้ามเขียน file นี้** (2) agent ของเราห้ามเรียก external API นี้ (3) agent ของ supplier เรียก internal API ของเราได้ไหม. นี่คือการเปลี่ยน **threat model** ที่ Gartner อยู่ตามไม่ทัน

Point of view: pattern ที่เห็น — **sidecar กำลังชนะ gateway บน agent runtime** ด้วยเหตุผลเดียวกับที่ **service mesh (Istio, Linkerd) ชนะ API gateway บน microservice** เมื่อ 7 ปีก่อน. Gateway เป็น centralized bottleneck + ownership ของ auth flow; sidecar เป็น decentralized + ติดกับ workload. agent ที่ complex (multi-step tool use, long-running task) ไม่สามารถ fit model request/response ของ gateway ได้. ภายใน 24 เดือน, **"service mesh for agents"** จะเป็น product category ของตัวเอง — Rein + sidecar vendor อีก 3-4 ค่ายจะเหลือ 2 ค่าย

ที่น่าสังเกต: Dun & Bradstreet เป็น **data broker ที่ขายข้อมูล credit score ให้ bank** — ถ้า agent ของ D&B hallucinate = ลูกค้า bank ที่สมัครสินเชื่อโดนปฏิเสธโดยไม่มี audit trail = fine จาก regulator. การที่ D&B ยอมเปิดเผย Rein deployment ชี้ว่า **(1) compliance-sensitive vertical กำลัง require runtime guardrail**, **(2) sidecar architecture ผ่าน SOC 2 + model risk management ของธุรกิจ regulated**. ซึ่งคือ moat ที่ gateway-based competitor สร้างยาก

Compare funding timeline: Rein $8M seed (ก่อน Jan 2026) → launch → 8x revenue + 5x customer ภายใน 9 เดือน → $25M Series A = **capital efficiency ที่สูงกว่า agent framework vendor** (LangChain, LlamaIndex ที่ใช้เงินมากกว่าแต่ ARR ต่ำกว่า). Signal ชัดว่า **investor กำลังเทไปที่ "picks and shovels" ของ agent มากกว่า agent application เอง**

## มุม AI Agent Platform

**Builders:** ถ้าคุณสร้าง agent application / vertical agent — ภายใน 12 เดือน enterprise จะ require ให้ agent ของคุณ **integrate กับ runtime guardrail vendor อย่างน้อย 1 ค่าย**. ไม่ build in support ตั้งแต่ day 1 = หลุด RFP ที่ regulated industry. Rein + Lasso + Prompt Security + Noma เริ่มออก **certification program** สำหรับ agent framework — คาดปี 2027 จะมี standard สำหรับ "agent security integration tier" คล้าย SOC 2 Type II

**Users / business:** CISO ที่ยัง approve agent deployment แบบ case-by-case — ต้องมี **runtime guardrail primitive** ภายใน Q1 2027. 2 คำถามที่สำคัญ: **(1) sidecar vs gateway deployment model** (เลือก sidecar สำหรับ complex multi-step, gateway สำหรับ simple RAG), **(2) support ของ framework ที่ใช้อยู่** (LangGraph? Claude Agent SDK? Copilot Studio?). อย่าซื้อ gateway ที่ไม่ support framework ของทีม — จะทำให้ engineering ต้องเปลี่ยน architecture agent

**Ecosystem:** ตลาด non-human identity + agent runtime security กำลังเดินทาง consolidation เร็ว — **24 เดือนข้างหน้าจะเหลือ 5 brand ใหญ่**: (1) Cyera (identity + data) หลัง Oasis acquisition, (2) Baselayer (identity verification สำหรับ financial), (3) CyberArk (ภายใต้ Palo Alto, enterprise-wide), (4) Rein / Lasso (runtime guardrail — น่าจะ merge ค่ายใดค่ายหนึ่ง), (5) Prompt Security / Noma (gateway-based, จะโดนกิน). Hyperscaler ของตัวเอง (AWS Bedrock Guardrails, Azure AI Content Safety, Google Model Armor) ยัง — ยังไม่พอสำหรับ regulated enterprise

## Sources
- [Rein Security lands $25m as AI agents outrun security (FinTech Global)](https://fintech.global/2026/10/09/rein-security-lands-25m-as-ai-agents-outrun-security/)
- [Rein Security Raises $25 Million (Disaster Recovery Journal)](https://drj.com/industry_news/rein-security-raises-25-million-to-secure-the-ai-agents-enterprises-build-and-stop-the-ones-that-attack-them/)
- [Rein Security raises $25M to secure enterprise AI agents (Dealroom)](https://dealroom.co/news/160871-rein-security-raises-25m-to-secure-enterprise-ai-agents/)
- [Rein Security Raises $25M (Morningstar / PR Newswire)](https://www.morningstar.com/news/pr-newswire/20261008ph66266/rein-security-raises-25-million-to-secure-the-ai-agents-enterprises-build-and-stop-the-ones-that-attack-them)
- [Rein Security Raises $25M Series A to Secure AI Agents (Automate.bworldtools / CTech)](https://automate.bworldtools.com/Articles/2026-10-11_Rein_Security_Raises_25M_Series_A_to_Secure_AI_Agents_r0t.html)
- [Rein Security Raises $25M Series A (The SaaS News)](https://www.thesaasnews.com/news/rein-security-raises-25m-series-a/)

---

## Audio script
วันที่ 8 ตุลาคม Rein Security ปิด Series A ที่ 25 ล้านเหรียญ co-lead โดย Glilot Capital กับ Sienna Venture Capital รวม total funding เป็น 35 ล้านเหรียญ จุดต่างจาก Lasso Prompt Security Noma คือ patent pending sidecar architecture ที่ไม่ sit ที่ gateway หรือ proxy แต่ติดข้าง process ของ agent เอง มองเห็นทุก line of code ที่รัน ทุก resource ที่ถูก access แล้ว block action ที่ไม่ปลอดภัยก่อน execute ตัวเลขที่น่าสนใจ นับจาก launch มกราคม 2026 revenue โต 8 เท่า customer base โต 5 เท่า Dun and Bradstreet กับ Lemonade เป็น named customer อ้างว่าใช้ Rein ปกป้อง agent หลักพันตัว pattern ที่ชัด 90 วันผ่านมา มี 3 ดีลสำคัญในชั้น agent trust layer Cyera ซื้อ Oasis หนึ่งพันล้าน Baselayer Series A 35 ล้าน Rein 25 ล้าน รวมกับ Cisco ซื้อ Astrix Palo Alto ซื้อ CyberArk 25 พันล้าน ตลาด non human identity กับ agent runtime security กำลัง consolidate เร็วกว่า Gartner คาด sidecar กำลังชนะ gateway ด้วยเหตุผลเดียวกับที่ service mesh ชนะ API gateway บน microservice 7 ปีก่อน gateway เป็น bottleneck + ownership ของ auth flow sidecar decentralized ติดกับ workload สำหรับ CISO ไทยที่ยัง approve agent deployment case by case ต้องมี runtime guardrail primitive ภายในไตรมาสหนึ่ง 2027 เลือก sidecar สำหรับ multi step complex gateway สำหรับ simple RAG ที่สำคัญ check support ของ framework ที่ใช้อยู่ก่อนซื้อ สำหรับ builder ที่สร้าง vertical agent ภายใน 12 เดือน enterprise จะ require integrate กับ runtime guardrail vendor อย่างน้อยหนึ่งค่าย ไม่ build in day one จะหลุด RFP ที่ regulated industry ทันที
