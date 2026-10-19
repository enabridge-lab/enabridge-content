---
date: 2026-10-20
slug: google-gemini-enterprise-agent-platform-spiffe
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: |
  Editorial isometric diagram of a secure data center hallway. In the
  foreground three agent "capsules" stand side by side, each stamped
  with a label: "AGENT-1", "AGENT-2", "AGENT-3". A thick vertical pillar
  behind them is labeled "AGENT GATEWAY" in bold capitals, with glowing
  conduits running out to two side signs reading "MCP" and "A2A". A
  prominent key-shaped badge in the center says "SPIFFE ID". Deep blue
  background, warm green accents, high-contrast typography readable at
  200px thumbnail. 1:1 aspect, no real human faces.
image: images/26-10-20-0607-03-google-gemini-enterprise-agent-platform-spiffe.png
---

# Google ให้ agent มี "ID แบบมีลายเซ็น" และ gateway กลาง — Gemini Enterprise Agent Platform พยายามเป็น control plane ของ agent

## TL;DR
- Google เปลี่ยนชื่อ Vertex AI Agent Builder เป็น **Gemini Enterprise Agent Platform** และ roll out ของสำคัญ 3 ชิ้น: **Agent Identity** (SPIFFE ID แบบ cryptographic ต่อ agent), **Agent Gateway** (control plane กลางสำหรับ MCP + A2A), และ sandboxed Workspaces
- SPIFFE ID หมายความว่า agent แต่ละตัวมี identity แบบที่ Zero Trust ของ workload จับได้ — เท่ากับ agent "เข้า IAM" ได้แบบ workload ปกติ ไม่ใช่ API key เงา ๆ
- Agent Gateway รองรับ mTLS + MCP + A2A — Google วาง pos ให้ตัวเองเป็น control plane มาตรฐานของ agent ไม่ว่า underlying agent จะมาจาก Google หรือค่ายไหน

## เกิดอะไรขึ้น
Google ค่อย ๆ ประกาศเปลี่ยนชื่อ Vertex AI Agent Builder เป็น **Gemini Enterprise Agent Platform** ตั้งแต่ Cloud Next 2026 และตอนนี้ feature set เริ่มชัดขึ้นเรื่อย ๆ. หัวใจที่น่าจับตาที่สุดคือ **Agent Identity** — Google ให้ agent ทุกตัวมี **SPIFFE ID** (Secure Production Identity Framework For Everyone — มาตรฐานของ CNCF ที่ workload ใน Kubernetes ใช้มาหลายปี) เป็น cryptographic signature ของ agent. identity นี้ใช้ทำ authentication, access control, และ audit — agent ที่ทำงานในระบบจะมี ID แบบที่ IAM, SIEM, และ workload policy engine จับได้แบบเดียวกับ workload ปกติ ไม่ใช่ "service account แฝง" ที่ใช้ API key ถาวร

ชิ้นที่สองคือ **Agent Gateway** — Google วางให้เป็น control point เดียวสำหรับ connectivity และ policy ของ agent. ทุก call ที่ agent ยิงออกไป ไม่ว่าจะเป็น agent-to-agent (A2A protocol ของ Google เอง) หรือ agent-to-tool (ผ่าน MCP ของ Anthropic) จะวิ่งผ่าน gateway ซึ่งทำ mTLS + enforce access policy + log ทุก call. ตามเอกสารของ Google, gateway รองรับ MCP security และ A2A ในตัว — ซึ่งคือการที่ Google ยอม "เปิดบ้าน" ให้ protocol ของคู่แข่ง (Anthropic) ผ่านเข้ามาได้ เพื่อแลกกับการเป็น control plane

ชิ้นที่สามคือ sandboxed environment สำหรับรัน code ที่ agent generate — Google เรียก "Workspaces" ใน launch post และบางเอกสารเรียก "Agent Sandbox" — เป็น environment สำหรับ bash command + file management ที่แยกจาก core system. Features บางส่วน (A2A บน runtime) ยังอยู่ใน Preview / Pre-GA ตามรายงานของ third-party evaluation

## ทำไมสำคัญ
ปัญหาที่ enterprise ไม่พูดดัง ๆ ตอนนี้คือ: agent ที่ build ด้วย framework ค่ายใดก็ตาม ใช้ API key หรือ service account ที่ยาวอายุ ไม่ใช่ workload identity — เท่ากับ agent ไม่ "เข้า IAM" ของบริษัท, อยู่นอก SIEM, และ audit ยาก. การที่ Google หยิบ SPIFFE มาใช้เป็นสัญญาณว่า agent governance กำลังเลียน patterns ที่ Zero Trust / workload identity ของ cloud-native ใช้มา 7-8 ปี — ซึ่งเป็นสิ่งที่ CIO และ CISO ของ enterprise ขนาดใหญ่ "เข้าใจแล้ว" โดยไม่ต้องเรียนใหม่

Agent Gateway เป็นเดิมพันที่น่าสนใจ. Google ยอมเปิดให้ MCP (ของ Anthropic) และ A2A (ของตัวเอง) ผ่าน gateway เดียวกัน — เท่ากับ Google ประกาศว่า "เราไม่สน protocol สงคราม เราขาย control plane". ถ้า enterprise ตัดสินใจว่า control plane คือ Google Gateway แล้ว agent runtime ของค่ายไหนก็ connect ผ่าน gateway นี้ — ไม่ว่า agent จะ build ด้วย LangGraph, Agents SDK, หรือ Claude — รายได้ consumption ก็ตกที่ Google. นี่คือ playbook เดียวกับที่ Cloudflare ใช้กับ L7 traffic และ Google กำลัง replicate ที่ชั้น agent

Caveat: Agent Gateway ยังเป็น Google product อยู่ — มี vendor lock-in. SPIFFE ID อย่างเดียวพกไปใช้ที่อื่นได้เพราะเป็น open standard แต่ Gateway ไม่ใช่

## มุม AI Agent Platform
สำหรับ **Builders** — ถ้า target customer เป็น enterprise ที่ใช้ GCP ควรเริ่ม support Agent Identity + Agent Gateway เป็น integration ชั้นแรก. การใช้ SPIFFE ID ไม่ใช่ Google-specific — เพราะเป็น CNCF standard — แต่ Google จะเป็นค่ายแรกที่ enterprise จะได้ลองใน scale จริง. สำหรับ **Users / business** — ถ้าอยู่ใน GCP ecosystem เริ่มถามว่า agent ที่ pilot อยู่มี identity แบบ workload หรือเปล่า, log วิ่งไปที่ SIEM หรือเปล่า, policy ของ gateway ตรงกับ data policy เดิมของบริษัทไหม. สำหรับ **Ecosystem** — Anthropic ได้ประโยชน์ทางอ้อม เพราะ MCP ของตัวเองได้รับการรับรองโดย Gateway ของ Google — เท่ากับ MCP เป็น de-facto protocol มากขึ้น. แต่ Anthropic ก็เสีย positioning ชั้น "ใครคือ control plane" เพราะคนที่ขาย control plane คือ Google. Microsoft Copilot Studio ต้องเร่งทำ gateway ของตัวเองเทียบ ไม่งั้นลูกค้า hybrid cloud จะไหลไปใช้ของ Google

## Sources
- [Introducing Gemini Enterprise Agent Platform (Google Cloud Blog)](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform)
- [Google Introduces Unique AI Agent Identities in New Gemini Enterprise (Infosecurity Magazine)](https://www.infosecurity-magazine.com/news/google-ai-agent-identities-gemini/)
- [Agent Gateway overview (Google Cloud Documentation)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)

---

## Audio script
Google เพิ่งโชว์ของจริงเรื่องการควบคุม agent ในระดับ enterprise. เขาเปลี่ยนชื่อ Vertex AI Agent Builder เป็น Gemini Enterprise Agent Platform แล้วปล่อยของสำคัญสามชิ้น. ชิ้นแรกชื่อ Agent Identity — agent ทุกตัวจะได้ ID แบบ cryptographic ที่เรียกว่า SPIFFE ID. ชื่อฟังดูเทคนิค แต่ความหมายคือ agent "เข้า IAM ของบริษัท" ได้เหมือน workload ปกติ — ไม่ใช่ API key ถาวรแฝง ๆ อีกต่อไป. ชิ้นที่สองคือ Agent Gateway — control plane กลางที่ทุก call ของ agent วิ่งผ่าน จะเป็นการเรียก MCP ของ Anthropic หรือ A2A ของ Google เองก็ได้ gateway ทำ mTLS, enforce policy, log ครบ. ชิ้นที่สามคือ sandboxed environment สำหรับรัน code ที่ agent generate แยกจาก core system. ที่น่าสนใจที่สุดคือ Google ยอมเปิดให้ MCP ของ Anthropic ผ่านเข้ามาได้ — เพราะเขาเลือกไม่สู้ที่ protocol แต่สู้ที่ control plane. สำหรับคนที่ทำ agent — ควรเริ่มคุย SPIFFE ID ตั้งแต่ตอนนี้ เพราะมันเป็น CNCF standard ไม่ใช่ Google เฉพาะตัว. สำหรับ CIO — ถ้าใช้ GCP ควรถามทีมว่า agent ที่ pilot อยู่ identity เป็น workload หรือยัง log เข้า SIEM หรือยัง ไม่งั้นหลัง pilot ไปแล้วจะปิดช่องยาก
