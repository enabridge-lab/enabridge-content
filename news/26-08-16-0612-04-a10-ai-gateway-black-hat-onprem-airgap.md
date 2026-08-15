---
date: 2026-08-16
slug: a10-ai-gateway-black-hat-onprem-airgap
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a hardened bunker/data-center cross-
  section; inside sits a control tower routing colored streams of agent
  traffic labeled "OPENAI", "CLAUDE", "GEMINI", "SELF-HOSTED" to different
  model bays; three giant floating numbers dominate the scene, stacked:
  "AIR-GAPPED", "$-PER-REQUEST", "1 CONTROL PLANE"; A10 Networks wordmark on
  the bunker wall; a small "BLACK HAT USA 2026" sign at the entrance. High
  contrast, thick outlines readable at 200px thumbnail, 1:1 aspect, no real
  human faces, editorial magazine style.
image: images/26-08-16-0612-04-a10-ai-gateway-black-hat-onprem-airgap.png
---

# A10 Networks เปิดตัว AI Gateway ที่ Black Hat — on-prem/air-gapped control plane, per-request cost tracking; ตลาด AI Gateway กลายเป็น category ในหนึ่งสัปดาห์

## TL;DR
- **13 ส.ค. 2026** — A10 Networks เปิดตัว **A10 AI Gateway (GA)** ที่ Black Hat USA 2026 — control plane เดียวสำหรับ route + govern agent, app, LLM ทั่วองค์กร
- Feature ต่างจาก hyperscaler gateway: **deploy on-prem, private cloud, หรือ air-gapped ทั้งหมด** — เหมาะกับ regulated industry (defense, finance, healthcare, government) ที่ไม่ให้ traffic ออก DC
- **Per-request cost tracking เป็นดอลลาร์**, token budget limit ต่อ team/model, rate limit per key/team, และ route ตาม task complexity — match request กับ model ที่ถูก cost ที่สุด
- Bundle กับ **TrojAI** (A10 acquire, AI security posture) และ **ThreatX** — ตอบโจทย์ CISO ที่เห็น AI Gateway เป็น category ใหม่ที่ต้อง own ใน network layer (คู่ line กับ Azure APIM AI Gateway ที่ launch ไปสัปดาห์เดียวกัน)

## เกิดอะไรขึ้น
วันที่ 13 สิงหาคม 2026 ที่ Black Hat USA 2026 ใน Las Vegas, A10 Networks (NYSE: ATEN) — เดิมเป็น application delivery + DDoS defense vendor — ปล่อย **A10 AI Gateway** เข้า general availability พร้อม positioning ว่าเป็น *"intelligent control plane for all AI operations"* คือ **1 plane สำหรับ route, govern, cost-track ทุก AI traffic** ที่ผ่านองค์กร ทั้ง third-party API (OpenAI, Anthropic, Gemini) และ self-hosted model

Feature ที่ define positioning ต่างจาก hyperscaler gateway (Azure APIM AI Gateway, AWS AgentCore Gateway, Cloudflare AI Gateway) = **deployment posture**: A10 ship เป็น **software หรือ hardware appliance** ที่รันใน customer environment 100% — **on-prem, private cloud, air-gapped** — ไม่มี call-home, ไม่มี telemetry ไป A10 cloud เท่ากับ regulated industry (US DoD, financial services, healthcare, EU government) ที่ห้าม data plane ออก DC สามารถ deploy AI Gateway ได้โดยไม่ผ่าน hyperscaler ตัวไหน

Feature ที่ CISO จะ note: (1) **route ตาม task complexity** — request ที่ classify เป็น "summarize" ไปที่ small model ($), "complex reasoning" ไปที่ Claude Opus 4 ($$$) — ลด cost per request 40-70% ตาม A10 case study เอง; (2) **per-request cost tracking เป็นดอลลาร์** (ไม่ใช่แค่ token) — สำคัญเพราะ CFO ที่ approve AI budget ต้อง forecast รายเดือน; (3) **token budget limit per model + team**, rate limit per key/team — ตัด rogue agent ที่ burn budget ก่อนถึง limit; (4) **access policy sync กับ Entra/Okta/AD** — user group ที่ query PII data ต้อง route ผ่าน model ที่ certify แล้ว

Bundle strategy: A10 acquire **TrojAI** ต้นปี 2026 เพื่อได้ AI security posture (model risk assessment, red-team framework) และ **ThreatX** (WAF + API security) — เท่ากับ A10 pitch enterprise buyer ว่า *"เราคือ AI Gateway + WAF + AI security ใน stack เดียว"* ต่างจาก hyperscaler ที่ต้อง bundle 4-5 SKU

## ทำไมสำคัญ
เรื่องนี้เป็น **confirmation ว่า AI Gateway กลายเป็น category** — 4-5 vendor ประกาศ product line ในเดือนเดียว: **AWS AgentCore Gateway** (มิ.ย.), **Cloudflare Kitesurf** (ส.ค. 11), **Azure APIM AI Gateway tier** (ส.ค.), **A10 AI Gateway** (ส.ค. 13), และ **F5, Kong, WSO2** ตาม roadmap Q4 — ไม่มี category ไหนใน infra ที่ vendor ประกาศ product พร้อมกันขนาดนี้ตั้งแต่ *service mesh* ปี 2018

Pattern ที่น่าจับตา 2 อย่าง: หนึ่ง — **AI Gateway = category ที่ hyperscaler + network vendor + security vendor ต่างเข้ามาจากคนละ angle** และแต่ละ angle จะเจอลูกค้าคนละกลุ่ม hyperscaler ได้ startup + cloud-native enterprise, network vendor (A10, F5, Cisco) ได้ regulated + on-prem, security vendor (Palo Alto, Zscaler) ได้ zero-trust deployment — ตลาดใหญ่พอที่จะรองรับหลายเจ้า แต่ **customer ต้องเลือก 1 gateway เท่านั้น** เพราะ 2 gateway = 2 policy layer = incident response nightmare

สอง — **positioning "on-prem + air-gapped" ของ A10** ตอบคำถามที่ hyperscaler ยัง gap: US DoD JWCC contract, EU sovereign cloud, และ China/UAE ที่ต้อง data residency 100% — segment นี้ประเมิน TAM ราว **$3-5B/ปี** (จาก A10 filings) เทียบกับ hyperscaler AI Gateway ที่ target public cloud (~$8-12B) — total AI Gateway market ปี 2027 น่าจะ break $15B

Signal ต่อจากนี้: Q4 2026 คาดว่า **Cisco จะประกาศ AI Defense platform** ที่รวม gateway + observability ผ่าน acquisition รอบใหม่ (rumor: Robust Intelligence extension), และ **Palo Alto Networks** จะปล่อย AI Runtime Security ที่ integrate กับ existing Prisma Cloud — ทำให้ enterprise มี 6-8 vendor ให้เลือกภายในสิ้นปี ซึ่งจะ trigger RFP war ที่กด margin ลง 20-30% ในไตรมาส 1 2027

## มุม AI Agent Platform
**Builders** ที่สร้าง MCP server หรือ agent tool: ต้องรองรับ **deployment ใน customer VPC / on-prem** ไม่ใช่แค่ SaaS ที่ callback ไป vendor cloud — enterprise ที่เลือก A10 gateway จะบังคับให้ทุก tool integration รันใน trust boundary ของตัวเอง SaaS-only MCP tool ที่ต้อง call ออก internet จะถูกตัดออกจาก procurement round

**Users / business** ที่ deploy agent ใน regulated industry: **AI Gateway = compliance requirement** ไม่ใช่ optional infrastructure อีกต่อไป ตาม EU AI Act 2 ส.ค. + upcoming US federal AI executive order + China GB standard — CISO ที่ไม่มี AI Gateway ในสถาปัตยกรรม = fail audit ทันที คำแนะนำ practical: ถ้าธุรกิจของคุณ regulated → เริ่ม RFP AI Gateway ในไตรมาสนี้ ประเมิน on-prem vs cloud gateway ตาม data residency requirement — และ **plan budget $500K-$2M/ปี** สำหรับ enterprise-scale deployment (100-500 developer + agent workload)

**Ecosystem**: คนได้ประโยชน์ = **appliance/hardware vendor** ที่จะเห็น hardware refresh cycle เร็วขึ้น (A10 + F5 + Cisco จะ boost revenue จาก AI Gateway SKU 20-40% Q4); **security consultant + system integrator** (Deloitte, Accenture, Wipro) ที่จะได้ implementation project ระดับ $200K-$1M ต่อ deployment คนเสีย = **iPaaS vendor** ที่ไม่มี AI Gateway story (MuleSoft, Boomi ยัง silent) และ **DIY approach** ที่ enterprise พยายาม build บน LiteLLM + OPA + custom — จะพบว่า TCO สูงกว่า commercial gateway หลังปีแรก

## Sources
- [A10 Networks Launches A10 AI Gateway, an Intelligent Control Plane for All AI Operations (Yahoo Finance)](https://ca.finance.yahoo.com/news/a10-networks-launches-a10-ai-130000537.html)
- [A10 Networks introduces AI Gateway to secure and manage enterprise AI (Help Net Security)](https://www.helpnetsecurity.com/2026/08/13/a10-networks-introduces-ai-gateway-to-secure-and-manage-enterprise-ai/)
- [A10 Networks Launches Intelligent Control Plane for All AI Operations (Security MEA)](https://securitymea.com/2026/08/13/a10-networks-launches-intelligent-control-plane-for-all-ai-operations/)
- [A10 Networks Launches AI Gateway for Governance (StockTitan)](https://www.stocktitan.net/news/ATEN/a10-networks-launches-a10-ai-gateway-an-intelligent-control-plane-9ie4bgymo9pf.html)

---

## Audio script
วันที่ 13 สิงหาคมที่ Black Hat USA 2026 Las Vegas A10 Networks ปล่อย A10 AI Gateway เข้า general availability positioning เป็น intelligent control plane เดียวสำหรับ route govern cost track ทุก AI traffic ที่ผ่านองค์กร ทั้ง third-party API และ self-hosted model จุดที่ต่างจาก hyperscaler gateway คือ deployment posture ship เป็น software หรือ hardware appliance ที่รันใน customer environment 100 เปอร์เซ็นต์ on-prem private cloud หรือ air-gapped ไม่มี call home ไม่มี telemetry ไป vendor cloud

feature ที่ CISO จะสนใจ คือ route ตาม task complexity request ง่ายไป small model request ยากไป Claude Opus 4 ลด cost 40 ถึง 70 เปอร์เซ็นต์ per-request cost tracking เป็นดอลลาร์ไม่ใช่แค่ token token budget per team model access policy sync กับ Entra Okta AD และ bundle กับ TrojAI ที่ A10 acquire ต้นปี พร้อม ThreatX เป็น AI Gateway บวก WAF บวก AI security ใน stack เดียว ต่างจาก hyperscaler ที่ต้อง bundle 4 ถึง 5 SKU

ทำไมสำคัญ นี่คือ confirmation ว่า AI Gateway กลายเป็น category — 4 ถึง 5 vendor ประกาศ product line ในเดือนเดียว AWS AgentCore Gateway Cloudflare Kitesurf Azure APIM AI Gateway และ A10 ตอนนี้ ไม่มี infra category ไหนที่ vendor ประกาศพร้อมกันขนาดนี้ตั้งแต่ service mesh ปี 2018 hyperscaler ได้ startup กับ cloud-native network vendor อย่าง A10 F5 Cisco ได้ regulated กับ on-prem segment ที่ target ต่างกัน

สำหรับ builder ที่สร้าง MCP server ต้องรองรับ deployment ใน customer VPC on-prem ไม่ใช่แค่ SaaS ที่ callback ไป vendor cloud SaaS-only MCP tool ที่ต้อง call ออก internet จะถูกตัดจาก procurement round สำหรับ business ใน regulated industry AI Gateway ไม่ใช่ optional อีกต่อไป CISO ที่ไม่มีในสถาปัตยกรรม fail audit ทันที ควรเริ่ม RFP ในไตรมาสนี้ plan budget 500 พันถึง 2 ล้านดอลลาร์ต่อปีสำหรับ enterprise scale deployment ครับ
