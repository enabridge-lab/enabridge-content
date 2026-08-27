---
date: 2026-08-27
slug: google-a2a-linux-foundation-agentic-ai-standards
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial isometric illustration of two glowing protocol pillars — one labeled
  "A2A" (Google-blue) and one labeled "MCP" (Anthropic-orange) — being placed
  together on a single marble pedestal stamped "AGENTIC AI FOUNDATION". Around
  the pedestal, a ring of small neutral cloud icons (AWS, Microsoft, Google,
  Anthropic, OpenAI, Bloomberg, Cloudflare) forms a circle of stewards. Three
  large numbers float on floating panels: "250+ MEMBERS", "2 PROTOCOLS", "1
  NEUTRAL HOME". Deep navy background with gold rim lighting. 1:1 aspect. No
  real human faces (silhouette only). High contrast so text reads in 200px
  thumbnail.
image: images/26-08-27-0614-01-google-a2a-linux-foundation-agentic-ai-standards.png
---

# Google บริจาค A2A ให้ Linux Foundation — Agentic AI Foundation กลายเป็น "neutral home" ของ MCP + A2A, 250+ สมาชิก

## TL;DR
- **20 ส.ค. 2026** Google ประกาศโอน **A2A (Agent-to-Agent)** protocol ให้ **Agentic AI Foundation (AAIF)** ที่ Linux Foundation ดูแล — A2A มาอยู่บ้านเดียวกับ **Model Context Protocol (MCP)** ที่ Anthropic บริจาคก่อนหน้านี้
- AAIF เพิ่งเปิดตัว ธ.ค. 2025 ด้วยสมาชิก < 40 ราย — วันนี้ **มี 250+ สมาชิก** ครอบ AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI, Shopify — ครบทั้ง hyperscaler และ frontier lab
- **แบ่งงานชัด:** MCP = agent ↔ tools/data, A2A = agent ↔ agent (discovery, delegation, result exchange) — สอง protocol คู่กันปิด stack "how agents talk to everything"
- Signal: agent economy เข้าเฟส **standard consolidation** — vendor แต่ละรายเลิกดัน protocol เจ้าเดียว, ยอมย้ายไป neutral body เพื่อให้ enterprise procurement ยอมเซ็น. คล้ายที่ Kubernetes ย้ายจาก Google → CNCF ปี 2015 ก่อน enterprise adoption ระเบิด

## เกิดอะไรขึ้น

20 ส.ค. 2026 Google Cloud ประกาศบริจาค A2A specification, SDKs และ developer tooling ทั้งชุด ให้ **Agentic AI Foundation (AAIF)** — Linux Foundation project ที่เพิ่งตั้งเมื่อ ธ.ค. 2025. A2A คือ open protocol ที่ Google เปิดตัวรอบ Cloud Next เม.ย. 2025 เพื่อ standardize วิธีที่ agent จาก vendor ต่างกันจะ **discover** กัน, **delegate** งานให้กัน, และ **exchange** ผลลัพธ์ข้าม framework/model boundary

การย้ายบ้านครั้งนี้ทำให้ AAIF กลายเป็นเจ้าของ **สอง protocol หลัก** ของ agentic AI ecosystem: **MCP** (Anthropic บริจาคปลาย 2025) สำหรับ agent ↔ tool/data connections, และ **A2A** สำหรับ agent ↔ agent communication. รวม MCP Apps (production ตั้งแต่กลางปี), Agent Handoff Protocol (DeepJudge บริจาค ส.ค.) — AAIF คือ **de facto standards body** ของ agent layer แล้ว

AAIF โตเร็วมาก: จาก **<40 สมาชิก** ตอนเปิด ธ.ค. 2025 → **250+ วันนี้**. รายชื่อครอบ hyperscaler ครบทุกเจ้า (AWS, Microsoft, Google), frontier lab (OpenAI, Anthropic, Cohere), enterprise/fintech (Bloomberg, Block, Shopify), edge/security (Cloudflare). สมาชิก TSC (Technical Steering Committee) ยังไม่ประกาศครบ แต่ Axios รายงานว่า Google จะรักษาที่นั่ง maintainer หลัก 12-18 เดือน ก่อน hand-off ให้ community มากขึ้นเรื่อย ๆ

**Timing น่าสนใจ:** A2A ย้ายบ้านสองสัปดาห์หลัง Google เปิด Gemini Enterprise for Financial Services + Legal (25 ส.ค.) — signal ว่า Google เปลี่ยน bet จาก "own protocol → own platform" เป็น "give away protocol → win via platform + distribution". เกมเดียวกับ Meta ที่ open-source Llama เพื่อ commoditize model layer, ให้ตัวเองเน้น distribution + custom stack

## ทำไมสำคัญ

Pattern ที่กำลังตกผลึกคือ **agent economy ต้อง neutral standards ถึงจะ scale**. หนึ่งปีที่แล้วทุก vendor พยายามดัน protocol เจ้าเดียว — OpenAI มี Assistants API + tool spec, Google มี A2A + Agent Development Kit, Microsoft มี AutoGen + Semantic Kernel — และเจอ friction เดียวกัน: **enterprise procurement ไม่ยอมเซ็นสัญญายาวกับ protocol ที่ owner คนเดียว** เพราะกลัว lock-in. ที่ Amazon Chime ตายก็เพราะเรื่องนี้; ที่ Slack ชนะ HipChat ก็เพราะ open ecosystem approach; ที่ Kubernetes ชนะ Docker Swarm ก็เพราะย้ายไป CNCF. Google รู้ patten นี้ดีจากประสบการณ์ Kubernetes → CNCF ปี 2015

**จุดกดดัน OpenAI:** OpenAI เป็นสมาชิก AAIF แต่ยังไม่ได้บริจาค protocol เจ้าไหน — Agents SDK, ChatKit, Function Calling ยังเป็น proprietary. ถ้า AAIF ประกาศ standard สำหรับ agent runtime หรือ tool schema ในอีก 3-6 เดือน แล้ว OpenAI ไม่ align — enterprise deal จะเริ่มเปรียบเทียบว่า "vendor นี้ compliant กับ AAIF baseline ไหม" คล้าย SOC 2. คำถามคือ OpenAI จะบริจาค Assistants API spec หรือดัน alternative? สัปดาห์ก่อน Sam Altman ให้สัมภาษณ์ The Verge บอก "protocols will consolidate — we welcome that" — signal เบา ๆ ว่าเตรียมยอม

**Anthropic ได้เปรียบเชิงกลยุทธ์:** MCP + A2A รวมกันแล้ว, ทั้งสอง protocol ถูก design โดย team ที่เข้าใจ enterprise deployment (MCP มาจาก Anthropic research + real deployments, A2A มาจาก Google Cloud enterprise team). Anthropic ที่ push MCP ก่อนใครในตลาด — Claude รองรับ MCP ตั้งแต่ปลาย 2024, Files API + Skills API + Computer Use เพิ่งขึ้น GA เมื่อ 19 ส.ค. — build platform ที่ **native compatible** กับ AAIF standards ทั้งชุด. คู่แข่งที่ล่าช้าปรับ tooling จะเสียเปรียบ deal enterprise procurement

## มุม AI Agent Platform

**Builders:** ถ้าคุณสร้าง agent framework, orchestration platform, หรือ agent tool — **เริ่ม audit compatibility กับ AAIF standards วันนี้**. Baseline expectation กำลังจะกลายเป็น: (1) รองรับ MCP client + server, (2) รองรับ A2A discovery + delegation, (3) publish agent card ตาม A2A spec, (4) join AAIF ในระดับ Silver membership ($10K-$50K/year) เพื่อ carry trust signal ให้ enterprise sale. ที่ยังใช้ proprietary protocol จะเจอ objection คำแรกใน RFP: "does this comply with AAIF?" — pattern เดียวกับ CNCF conformance badge ในโลก Kubernetes

**Users / business:** สำหรับ enterprise ที่จะ deploy multi-agent workflow — เขียน RFP ให้ **require AAIF compliance** (MCP + A2A) เป็น mandatory, และ **ห้าม proprietary protocol** เป็น dealbreaker. ประโยชน์: portability ระหว่าง vendor (ย้าย agent จาก Google → AWS → self-hosted โดยไม่ rewrite), fallback strategy ถ้า vendor เจอปัญหา (agent fail → route ไป backup agent อีก vendor ผ่าน A2A discovery), และ compliance audit ที่ง่ายกว่า (audit protocol layer ครั้งเดียวใช้กับทุก agent). Thai SMB / OpenBridge customer ที่ประเมิน platform ตอนนี้ ควรเช็ค AAIF membership + certification เป็น criteria แรก ๆ

**Ecosystem:** Google ยอมเสีย proprietary control ของ A2A เพื่อเร่ง adoption + ผูก enterprise ให้อยู่กับ Google Cloud (ที่เป็น reference implementation). Anthropic ได้ leverage ว่า MCP-native platform ของตัวเองพร้อมสำหรับ standard rollout. AWS + Microsoft ต้อง align — Microsoft น่าจะบริจาค Semantic Kernel abstraction บางส่วน, AWS น่าจะ open ส่วนของ Bedrock AgentCore. Alibaba/ByteDance/Tencent ไม่ใช่สมาชิก AAIF วันนี้ — จุดที่ต้องดูคือ **Chinese cloud จะสร้าง alternative standards body หรือ join AAIF?** ถ้าแยก → geopolitical split ของ agent standards ทันที คล้าย 5G

## Sources
- [Google Cloud donates A2A to Linux Foundation (Google Developers Blog)](https://developers.googleblog.com/en/google-cloud-donates-a2a-to-linux-foundation/)
- [Google's A2A protocol gets a new home (Axios)](https://www.axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards)
- [Google's A2A Protocol Joins AAIF, Consolidating the Agent Economy's Protocol Layer Under One Roof (Yahoo Tech)](https://tech.yahoo.com/ai/gemini/articles/google-a2a-protocol-joins-aaif-020554895.html)
- [Google transfers A2A to the Agentic AI Foundation (Techzine Global)](https://www.techzine.eu/news/devops/143659/google-transfers-a2a-to-the-agentic-ai-foundation/)
- [MCP Is Growing Up (Agentic AI Foundation)](https://aaif.io/blog/mcp-is-growing-up)

---

## Audio script
วันพุธยี่สิบเจ็ดสิงหา. Google บริจาค A2A protocol ให้ Agentic AI Foundation. Linux Foundation project ที่เพิ่งตั้งเมื่อธันวา สองพันยี่สิบห้า. A2A มาอยู่บ้านเดียวกับ MCP ที่ Anthropic บริจาคก่อนหน้านี้.

Agentic AI Foundation เพิ่งเปิดตัวเก้าเดือนก่อน. เริ่มด้วยสมาชิกน้อยกว่าสี่สิบราย. วันนี้มีสองร้อยห้าสิบสมาชิกแล้ว. ครอบ AWS Anthropic Google Microsoft OpenAI Bloomberg Block Cloudflare Shopify. ครบทั้ง hyperscaler และ frontier lab.

แบ่งงานสองโปรโตคอลชัดเจน. MCP standardize วิธีที่ agent เชื่อมต่อกับ tools และ data source. A2A standardize วิธีที่ agent คุยกับ agent ตัวอื่น. discovery. delegation. result exchange. ข้าม framework ข้าม vendor.

Pattern ที่ตกผลึกคือ agent economy ต้อง neutral standards ถึงจะ scale. หนึ่งปีก่อน ทุก vendor พยายามดัน protocol เจ้าเดียว. เจอ friction เดียวกัน. enterprise procurement ไม่ยอมเซ็นสัญญายาวกับ protocol ที่ owner คนเดียว. กลัว lock in. คล้าย Kubernetes ที่ Google ย้ายไป CNCF ปี สองพันสิบห้า. ก่อน enterprise adoption ระเบิด.

จุดกดดัน OpenAI. OpenAI เป็นสมาชิก AAIF แต่ยังไม่บริจาค protocol เจ้าไหน. Assistants API ChatKit Function Calling ยัง proprietary. ถ้า AAIF ประกาศ standard สำหรับ agent runtime อีกสามถึงหกเดือน แล้ว OpenAI ไม่ align. enterprise deal จะเริ่มถามว่า vendor นี้ compliant กับ AAIF baseline ไหม. คล้าย SOC 2.

Anthropic ได้เปรียบเชิงกลยุทธ์. MCP กับ A2A รวมกันแล้ว. platform ของ Anthropic native compatible ตั้งแต่ต้น. คู่แข่งที่ล่าช้าปรับ tooling จะเสียเปรียบ.

สำหรับ builders. เริ่ม audit compatibility กับ AAIF standards วันนี้. รองรับ MCP client server. รองรับ A2A discovery delegation. publish agent card. join AAIF Silver membership. carry trust signal ให้ enterprise sale.

สำหรับ enterprise. เขียน RFP require AAIF compliance เป็น mandatory. proprietary protocol เป็น dealbreaker. Thai SMB และ OpenBridge customer ที่ประเมิน platform ตอนนี้ ควรเช็ค AAIF membership เป็น criteria แรก.

สำหรับ ecosystem. Alibaba ByteDance Tencent ไม่ใช่สมาชิก AAIF วันนี้. จุดที่ต้องดูคือ Chinese cloud จะสร้าง alternative standards body หรือ join AAIF. ถ้าแยก. geopolitical split ของ agent standards ทันที. คล้าย 5G
