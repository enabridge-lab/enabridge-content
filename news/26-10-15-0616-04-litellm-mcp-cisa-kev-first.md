---
date: 2026-10-15
slug: litellm-mcp-cisa-kev-first
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  A giant steel vault door labeled "LITELLM MCP GATEWAY" stands wide open with
  a cartoon broken padlock on the floor. A clipboard in the foreground has a
  stamp reading "CISA KEV — FIRST MCP ENTRY". Three glowing stat boxes above
  read "CVE-2026-59822", "CVSS 8.8", and "FIX: 1.84.0". A tiny silhouette of
  an attacker walks through the open door holding a paper labeled "FAKE BEARER
  TOKEN". Editorial dark-mode illustration, red and amber warning palette,
  1:1 aspect, no real human faces.
image: images/26-10-15-0616-04-litellm-mcp-cisa-kev-first.png
---

# MCP ตัวแรกที่โดนขึ้น CISA KEV — LiteLLM gateway ปล่อย session ให้ fake bearer token

## TL;DR
- CVE-2026-59822 — LiteLLM MCP Streamable HTTP endpoint ตก auth แล้วไหลไป "empty auth object" ทำให้ fake Bearer token เปิด session ได้. CVSS 8.8, patch ที่ version 1.84.0
- CISA ใส่ลงใน Known Exploited Vulnerabilities (KEV) catalog เป็น MCP ตัวแรก, deadline federal remediation 16 ก.ย. 2026. Wiz honeypot เห็น exploitation attempt ตั้งแต่ 7 ก.ค.
- ตามด้วย CVE-2026-59821 (post-auth root RCE ผ่าน custom guardrails) + MCP Python SDK OAuth downgrade — ไม่ใช่ bug เดี่ยว แต่เป็น pattern ของ "ชั้น auth หายไปทั้งแถบ" ใน MCP ecosystem

## เกิดอะไรขึ้น
LiteLLM คือ gateway ที่หลายทีมใช้ unify LLM API — ChatGPT, Claude, Gemini, local models — ให้เป็น interface เดียว แล้วใช้เป็น MCP server ให้ agent ของตัวเองเสียบใช้. ปัญหาอยู่ที่ MCP Streamable HTTP endpoint: เมื่อ API key validation fail แทนที่จะ reject request handler กลับ fallback ไป empty authentication object. ผล: Bearer token ที่สร้างขึ้นมามั่ว ๆ (เช่น `Bearer anything`) เปิด MCP session ที่มี permission เต็มได้

CVE-2026-59822 ได้ CVSS 8.8 — "High", exploit สำเร็จโดยไม่ต้องมี credential จริง. Fix ปล่อยที่ LiteLLM 1.84.0. CISA ขึ้นลง KEV catalog เมื่อ 2 ก.ย., ตั้ง federal agency deadline 16 ก.ย. — เป็น MCP vulnerability ตัวแรกที่เข้า list นี้. Wiz รายงานว่า honeypot ของเค้าเห็น exploitation attempt จริงตั้งแต่ 7 ก.ค. ก่อน CVE จะออกเกือบ 2 เดือน

ไม่ได้มาคนเดียว — ชุดเดียวกันมี CVE-2026-59821 (post-auth root-level RCE ผ่าน custom code guardrails ของ LiteLLM, คนที่เข้า MCP session ได้แล้วรัน code เป็น root), และ MCP Python SDK OAuth downgrade issue ที่ Cycode ขุดเจอ — malicious MCP server สามารถบังคับ SDK client ให้ fallback ไป legacy OAuth flow ที่ไม่ validate issuer ทำให้ขโมย credential + authorization code ได้ (fix ใน 1.30.0 กับ 2.2.0)

Context กว้างกว่านี้: Q3 2026 นักวิเคราะห์นับได้ 14 CVE ใน MCP ecosystem + ~200,000 exposed MCP servers บน internet. Attack vector หลัก 3 ตัวที่ซ้ำ: prompt injection, malicious registries, config hijacking ที่ให้ auto-approve MCP servers (Claude Code ก็เคยโดน CVE คนละกลุ่ม)

## ทำไมสำคัญ
MCP ที่ Anthropic เปิด protocol เมื่อปลายปี 2024 ตอนนี้โตเป็น protocol ที่ทุก agent runtime ใหญ่พึ่ง — Anthropic, OpenAI (Connectors), Google Gemini Agent, Workday, Databricks, Cloudflare ยืนบน MCP กันหมด. การที่ CVE แรกของ MCP ขึ้น CISA KEV คือ moment ที่ security community ยอมรับว่า protocol นี้ไม่ใช่ experimental อีกต่อไป — มัน production critical พอที่ federal agency ต้องมี patch deadline

สิ่งที่น่ากลัวกว่าตัว CVE คือ pattern. ชั้น auth ของ MCP server implementation หลายตัวหายไปเหมือนกันหมด — ไม่ใช่ bug เขียนผิด แต่คือ design assumption ว่า "ถ้า token ใช้ไม่ได้ ไปใช้ default session" ซึ่งใน web gateway ปกติใครก็รู้ว่าห้าม. การซ้ำของ pattern นี้บอกว่า MCP ecosystem ยังอยู่ใน phase ที่ developer ยัง treat MCP server เหมือน internal tool — ไม่ใช่ production API

Wiz honeypot ที่เห็น exploit attempt ตั้งแต่ ก.ค. 2 เดือนก่อน CVE ออก คือ warning ที่ชัด — attacker scan หา MCP endpoint ก่อน defender จะรู้ตัว. 200,000 exposed MCP servers คือ attack surface ขนาดไหน ลองคิดว่าแต่ละตัวต่อกับ LLM backend ที่มี API key ของบริษัทลูกค้าอยู่

## มุม AI Agent Platform
- **Builders**: ถ้าคุณ run LiteLLM หรือ MCP server อื่นใน production — audit auth path ตอนนี้. ห้ามให้ fallback เป็น silent success. เพิ่ม structured logging + alert ที่ invalid-token count ก่อนจะมี exploit จริง. ถ้ายังรัน self-hosted ขอให้ไปใช้ managed MCP (Cloudflare, Databricks, Workday) จนกว่า operational maturity จะพอ
- **Users / Business**: ถาม vendor ของคุณตรง ๆ ว่า MCP endpoint ของเค้าผ่าน pentest + redteam หรือยัง และ patch cadence เท่าไหร่. ถ้าตอบ "เรา audit ปีละครั้ง" แปลว่ายังไม่พร้อม production
- **Ecosystem**: นี่คือ moment ที่ Anthropic + Linux Foundation Agentic AI Foundation ต้องเร่ง reference auth implementation + certification. ถ้าปล่อยไว้ให้ developer เขียนเองทุกคน จะมี CVE แบบนี้อีก 30-50 ตัวในปีหน้า — จนกว่าจะมี incident ใหญ่ที่ทำให้ CIO ห้ามใช้ MCP ทั้ง org

## Sources
- [LiteLLM CVE-2026-59822: First MCP Flaw on CISA's Exploit List — ByteIota](https://byteiota.com/litellm-cve-2026-59822-mcp-auth-bypass/)
- [The Relay Has No Lock: LiteLLM's MCP Auth Bypass Marks a First for the CISA KEV Catalog — Forkast](https://forkast.news/the-relay-has-no-lock-litellms-mcp-auth-bypass-marks-a-first-for-the-cisa-kev-catalog/)
- [MCP security October 2026: LiteLLM on CISA KEV, Grafana MCP flaw — Adversa](https://adversa.ai/blog/top-mcp-security-resources-october-2026/)
- [LiteLLM CVE-2026-59822: Your AI Gateway Is a Cloud Control Plane — Hive Security](https://hivesecurity.gitlab.io/blog/litellm-cve-2026-59822-ai-gateway-cloud-pivot/)

---

## Audio script
วันนี้มีเรื่องสำคัญสำหรับทุกคนที่ใช้ MCP ใน production. CVE ตัวแรกของ MCP ขึ้น CISA KEV catalog แล้ว — CVE-2026-59822 ที่ LiteLLM MCP gateway. ปัญหาคือเมื่อ auth validation fail handler ไม่ reject request กลับ fallback ไป empty auth object ทำให้ Bearer token ที่สร้างมั่ว ๆ เปิด MCP session ได้ CVSS 8.8 patch ที่ version 1.84.0. ที่น่ากลัวกว่าคือ Wiz honeypot เห็น exploitation attempt ตั้งแต่กรกฎาคม 2 เดือนก่อน CVE จะออก — attacker scan หา endpoint ก่อน defender รู้ตัว. และไม่ได้มาคนเดียว — ชุดเดียวกันมี CVE-2026-59821 ที่เป็น post-auth root RCE และ MCP Python SDK OAuth downgrade issue. ปัจจุบันมี 14 CVE ใน MCP ecosystem รวม + 200,000 exposed MCP servers บน internet. สิ่งที่น่าสนใจคือ pattern — ชั้น auth หายไปเหมือนกันหมด. developer หลายทีมยัง treat MCP server เหมือน internal tool ไม่ใช่ production API. ถ้าคุณ run self-hosted MCP ลง audit auth path เลยวันนี้. ห้าม fallback เป็น silent success. ถ้าทำไม่ไหวย้ายไป managed MCP ของ Cloudflare, Databricks, หรือ Workday ก่อน. และสำหรับ Anthropic กับ Linux Foundation นี่คือ moment ที่ต้องเร่ง reference auth implementation + certification program จริงจัง ไม่งั้นปีหน้ามี CVE แบบนี้อีก 30 ถึง 50 ตัวครับ
