---
date: 2026-08-07
slug: black-hat-2026-agent-security-acalvio-zero-networks-deception
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  A dark cybersecurity war room; a giant holographic MCP server labeled
  "DECOY" glows red-orange in the center, ringed by translucent honeypot
  cubes labeled "HONEY SKILL", "HONEY TOKEN", "FAKE RAG". Above it hover
  two big signs: "LEAST AGENCY" (blue) and "DECEPTION GUARDRAILS" (amber).
  Small silhouettes of hooded attacker figures walk into the ring, unaware.
  Editorial illustration, deep navy + amber + red palette, thin white
  circuit lines. 1:1 aspect. Sign text must render large enough to read at
  200px. No real human faces.
image: images/26-08-07-0615-02-black-hat-2026-agent-security-acalvio-zero-networks-deception.png
---

# Black Hat 2026: Agent Security กลายเป็น theme หลัก — decoy MCP, honey skill, least-agency enforcement เต็มพื้น

## TL;DR
- Black Hat USA 2026 (สัปดาห์นี้ที่ Las Vegas) — vendor สายไซเบอร์แทบทุกเจ้ายิง launch capability ใหม่ที่ target agent เฉพาะ
- Acalvio Deception Guardrails ฝัง decoy MCP server, honey skill, fake RAG เพื่อจับ agent ที่ถูก compromise ก่อนถึง production
- Zero Networks Least Agency Enforcement คุมสิ่งที่ agent เข้าถึงและกระทำได้ — approval-in-the-loop กลายเป็น default posture
- ข้อความชัดเจน: prompt filter + output classifier เดิม "ไม่พอ" — agent ต้องการ security layer เฉพาะที่คิดใหม่ตั้งแต่ threat model

## เกิดอะไรขึ้น
สัปดาห์นี้ Las Vegas เจ้าภาพ Black Hat USA 2026 และแทบทุก vendor สาย cybersecurity ที่มี presence ที่งาน — Acalvio, Zero Networks, Astelia, Menlo Security, Cyera, Sweet Security, ESET, Reco, Palo Alto Networks, CrowdStrike, Snowflake — ออกความสามารถใหม่ที่ตั้งเป้าเฉพาะ AI agents. SecurityWeek สรุปเป็น "Part 1 / Part 2 / Part 3" ของ vendor announcements และ agents เป็น theme ที่ปรากฏใน majority ของ pitches

Acalvio Technologies ประกาศ Deception Guardrails เมื่อ 30 กรกฎาคม 2026 เป็น preemptive defense สำหรับ agentic AI. patent-pending นี้ฝัง deceptive assets ตั้งแต่ระดับ tool: honey skills (skill หลอกที่ agent มองว่าเป็น real capability), decoy MCP servers, decoy RAG sources และ honey agents. เมื่อ agent ที่ถูก compromised (จาก prompt injection หรือ credential leak) ลอง call decoy — ระบบจับได้ + feed fabricated data ให้ attacker พลอย alert SOC ทันที. Ram Varadarajan ของ Acalvio บอก vmblog ว่า traditional guardrails ทำได้แค่ filter input/output "แต่ไม่รู้ว่า agent ทำอะไรหลัง compromise" — Deception Guardrails ปิดช่องนี้

Zero Networks launch Least Agency Enforcement ที่งานเดียวกัน — คุมว่า AI agent ทำอะไรได้บ้าง, เมื่อไหร่ต้องขอ human approval, และ scope ของแต่ละ session. ชื่อ "Least Agency" เป็นเรียกเลียน "Least Privilege" ของ IAM ยุค 2000s แต่หมายถึงตัดสิทธิ์การกระทำแทนการเข้าถึงข้อมูล. Astelia ประกาศ agentic AI capability สำหรับ exposure management platform — automate reachability analysis + remediation ตลอด vulnerability lifecycle. ESET ออก AI Behavioral Monitoring ที่ตามดู autonomous agent ที่พยายามเข้าถึง resource ที่ไม่ควรหรือ run unsafe action

Reco จะ present สอง session ที่ Black Hat + DEF CON 34 เรื่อง security debt ที่เกิดขึ้นเงียบ ๆ เมื่อ agent inherit permission, ใช้ OAuth grant, trigger action ผ่าน SaaS ของ enterprise — theme เดียวกับ Zenity แต่ framed ผ่าน SaaS attack surface

## ทำไมสำคัญ
มี pattern ที่ต้องมอง 2 ชั้น. ชั้นแรก — vendor sweep ครั้งนี้เป็นสิ่งที่ AWS re:Invent ปี 2024 หรือ RSA ปี 2025 ยังทำไม่ได้: category "AI agent security" มี submarket ชัดเจนพอที่ vendor จะ segment ตัวเองได้ (deception, agency control, exposure mgmt, behavior monitoring, identity governance, code security). ปีที่แล้ว pitch ทุกคนเหมือนกันหมด — "prompt injection defense" — ปีนี้แยกกันเป็นหมวดเหมือน endpoint security ยุค 2015

ชั้นที่สอง — ทุก launch สะท้อน threat model ที่บริษัท assume ตรงกัน: (1) agents ในองค์กรมี privilege มากกว่าที่ควร, (2) การ compromise เกิดจาก tool call ที่ผิด context, (3) traditional defense (WAF, EDR, IAM) ไม่เห็น agent identity, (4) การ audit ย้อนหลังไม่พอ — ต้อง detect + respond runtime. Acalvio ใช้ deception, Zero Networks ใช้ approval gate, Palo Alto ใช้ identity (Idira) — ตอบคำถามเดียวกันด้วย posture ที่ต่างกัน

การที่ CrowdStrike ประกาศ AI Unlocked: Agents of Chaos $100K challenge ในสัปดาห์เดียวกัน (ดู brief #3 ของรอบนี้) — เป็นการ acknowledge ว่า vendor community ยังไม่มี playbook เพื่อ train defender. ต้องสร้าง gamified environment ให้คน hack agent จริง ๆ ก่อนถึงจะเข้าใจ attack pattern

## มุม AI Agent Platform
สำหรับ **builders** — ถ้ายังเก็บ agent behavior ใน log อย่างเดียว, ยังไม่มี tool-level identity หรือ intent classification, ยังไม่ integrate กับ deception layer — จะขายเข้า regulated industry ไม่ได้ในปี 2027. Design MCP server / tool registry ต้องเผื่อ decoy path เพราะ security team จะขอ. สำหรับ **enterprises** ที่ deploy agent อยู่แล้ว — ต้องทบทวน "agent inventory" (agent ไหน run อะไร ใช้ tool อะไร, ใครเป็น owner) เป็นอันดับแรก ก่อนซื้อ tool ใหม่. Least agency policy ควร default deny แล้วเปิดเฉพาะ scope. สำหรับ **ecosystem** — คำถามคือ platform layer (Anthropic, OpenAI, Google) จะ ship native agency controls เอง หรือ leave to third-party. Anthropic เพิ่งประกาศ inference hooks in beta สำหรับ Enterprise (ดู brief #4) — เป็นสัญญาณว่า frontier lab เริ่มลงมาแข่งกับ pure-play security vendor

## Sources
- [Black Hat USA 2026 – Summary of Vendor Announcements (Part 1) — SecurityWeek](https://www.securityweek.com/black-hat-usa-2026-summary-of-vendor-announcements-part-1/)
- [Acalvio Unveils Deception Guardrails to Secure AI Agents — PR Newswire](https://www.prnewswire.com/news-releases/acalvio-unveils-deception-guardrails-to-secure-ai-agents-302838574.html)
- [The top new cybersecurity products at Black Hat USA 2026 — CSO Online](https://csoonline.com/article/4204921/the-top-cybersecurity-product-announcements-from-black-hat-2026.html)
- [Reco Experts to Present at Black Hat USA and DEF CON 34 on AI Agent Security Exposure](https://www.manilatimes.net/2026/08/03/tmt-newswire/globenewswire/reco-experts-to-present-at-black-hat-usa-and-def-con-34-on-ai-agent-security-exposure/2397160)

---

## Audio script
Black Hat USA สองพันยี่สิบหก ที่ Las Vegas สัปดาห์นี้ กลายเป็น event ที่ theme ชัดที่สุดในรอบหลายปี — AI Agent Security. Vendor สาย cyber แทบทุกเจ้าออก capability ใหม่ที่ target เฉพาะ agent. Acalvio ออก Deception Guardrails ที่ฝัง decoy MCP server, honey skill, และ decoy RAG เพื่อจับ agent ที่ถูก compromise ก่อนจะถึง production system. Zero Networks ออก Least Agency Enforcement ที่คุมว่า agent ทำอะไรได้ ต้องขอ human approval เมื่อไหร่ — เรียก "least agency" เลียน least privilege ยุค IAM. Astelia ออก reachability + remediation automation, ESET ออก AI Behavioral Monitoring, Reco จะ present เรื่อง OAuth grant กับ SaaS attack surface ที่ DEF CON. Pattern ที่เห็นคือ prompt filter กับ output classifier แบบเดิมไม่พอแล้ว. Category AI Agent Security แยกเป็น submarket ชัดเจน — deception, agency control, exposure management, behavior monitoring, identity governance. ถ้าคุณเป็น builder ที่ทำ agent framework ต้อง design tool-level identity + intent classification ตั้งแต่ต้น. ถ้าคุณเป็น enterprise ที่ deploy agent อยู่ต้องทบทวน agent inventory ก่อนซื้อ tool ใหม่. Frontier lab เริ่มลงมาแข่งด้วย — Anthropic เพิ่งเปิด inference hooks in beta สำหรับ Claude Enterprise ในสัปดาห์เดียวกัน.
