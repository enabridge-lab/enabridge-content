---
date: 2026-09-14
slug: deadbugz-mcp-metadata-poisoning-supply-chain
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A high-contrast illustration of a black beetle silhouette perched on
  three glowing bug counters in a row — the third counter flips red and
  bursts open, revealing hidden metadata text scrolling out: "HUNT SSH
  KEYS", "AWS TOKENS", "K8S CONFIG". Beside it, a warning card labeled
  "MCP SERVER" with a stamp "CALL 3". Below, a small ledger reads
  "23 PULL REQUESTS / 74 MINUTES". A single red skull hovers behind a
  cracked shield labeled "TRUST". Editorial noir style, deep charcoal
  and blood-red palette, 1:1 aspect, no real human faces.
image: images/26-09-15-0609-04-deadbugz-mcp-metadata-poisoning-supply-chain.png
---

# Deadbugz — MCP supply-chain campaign ที่รอ 3 tool call แล้วค่อยพิษ

## TL;DR
- Pillar Security + Adversa เปิดข้อมูล campaign ชื่อ **Deadbugz** — malicious MCP server ที่ยัดผ่าน PR สาธารณะเข้า repo คนอื่น
- Attack pattern: ให้ **2 tool ไม่มีพิษ (text formatting/summarization)** ก่อน — พอเรียกครบ **3 tool call** metadata ที่ agent อ่านจะ rewrite เป็นคำสั่งไปหา SSH key, AWS creds, shell history, Kubernetes config
- Delivery: บัญชี GitHub `zellkernel` ยิง **23 PR ใน 74 นาที** (9:52 PM – 11:07 PM UTC, 10 ส.ค. 2026) เข้า project AI/MCP/dev-tool ที่ไม่เกี่ยวกัน

## เกิดอะไรขึ้น

ทีม security หลายเจ้า (Pillar, Adversa, Cloud Security Alliance) รวบรวมและตั้งชื่อ campaign **Deadbugz** — malicious MCP server ที่ออกแบบมาเพื่อ **evade code review โดยเฉพาะ**. ผู้โจมตีสร้าง MCP server ที่ประกอบด้วย tool 2 ตัวธรรมดาไม่มีพิษ (text formatting, summarization) — reviewer ที่ดู PR ใหม่จะไม่เจออะไรผิด, static analysis จะไม่ trigger, LLM code review จะบอกว่า "safe". แต่ payload จริงถูก **runtime-gate** — server จะเก็บ counter ว่า client เรียก tool มาแล้วกี่ครั้ง; ถ้าถึง **3 crawl** จริง ๆ metadata ที่ server ส่งกลับ (คำอธิบายของ tool + hint ที่ agent อ่าน) จะ rewrite เป็นคำสั่งบอก agent ให้ไปค้น SSH key, AWS credential, shell history, และ Kubernetes config พร้อมซ่อนไม่ให้ user เห็น.

Delivery ทำผ่าน GitHub account เดียวชื่อ `zellkernel` — บัญชียิง **23 PR ใน 74 นาที** ระหว่าง 21:52 – 23:07 UTC วันที่ 10 สิงหา ไปยัง project AI/MCP/dev tool ที่ไม่เกี่ยวกัน. รูปแบบ PR ทุกฉบับดูปกติ (add integration, add example) แต่ยัด dependency ไปที่ MCP server ที่โจมตีเป็นเจ้าของ. ถ้า maintainer merge, ทุก user ที่ install package + configure agent ผูก MCP นี้ = ตกเป็นเหยื่อในทันทีที่ agent เรียก tool ครบ 3 ครั้ง.

ประเด็นที่นักวิจัย security ชี้ทุกเจ้า — **นี่ไม่ใช่ code vulnerability แบบเดิม**. Code ของ server "สะอาด" ทุก line ที่คน/machine อ่านได้ ประเด็นอยู่ที่ **metadata poisoning ผ่าน MCP protocol contract** — ตัว protocol ที่ agent เชื่อ tool description เพื่อ decide ว่าจะเรียก tool ไหน = surface area ใหม่ที่ก่อนหน้านี้ไม่มีในโลก software supply chain.

## ทำไมสำคัญ

MCP กลายเป็น de-facto standard สำหรับ agent เรียก tool ในหกเดือนที่ผ่านมา — Anthropic, OpenAI, Google, Microsoft ปล่อย support หมด. แต่ security assumption ของ MCP ตอน design (แค่เดือน พ.ย. 2024) คือ tool developer เป็นคนที่ user "รู้จัก". สมมติฐานนี้ตาย ณ วันที่ MCP server registry สาธารณะเปิด และ marketplace-style install กลายเป็น flow ปกติ.

Signal ตามมา — expect ทุก enterprise ที่ deploy agent ใน production ต้อง **whitelist MCP server** + **run tool description ผ่าน sanitization layer** ก่อน hand ให้ model, ไม่ใช่ trust ตรง. Startup security ที่ทำ MCP scanning (Pillar, Adversa, Prompt Security, Lakera, Protect AI) มี wind; framework ที่ยังไม่มี "MCP allowlist" primitive — LangGraph, Mastra, Google ADK, OpenAI Agents API — ต้อง add ในไตรมาสถัดไป. คำว่า "MCP audit" กำลังจะเข้า SOC 2 / ISO 42001 baseline requirement ในปี 2027.

## มุม AI Agent Platform

**Builders** ที่กำลัง build agent framework — เพิ่ม primitive สอง: (1) **MCP server allowlist + signed manifest** — ไม่ให้ agent ต่อ MCP ที่ไม่ได้ approve; (2) **tool description sanitization** — ตัด instruction-looking pattern ออกจาก metadata ก่อน hand ให้ model. **Users / business** ที่ deploy agent — วันนี้ ถ้า agent ของคุณต่อ MCP server ที่ install จาก marketplace / community registry คุณมี exposure. Audit ทันที: list MCP endpoints ที่ agent ต่ออยู่, ตรวจว่ามาจาก vendor ที่รู้จัก, และ ถ้าเรียก tool มาจาก MCP นั้น 3 ครั้งขึ้นไปมี anomalous behavior หรือไม่. **Ecosystem** — MCP registry (npmjs-style สำหรับ MCP) ต้องมี trust score + code signing; Anthropic ที่เป็นเจ้าของ protocol ต้อง issue spec update สำหรับ metadata integrity check.

สำหรับทีมไทยที่กำลัง POC agent เชื่อม MCP ในธนาคาร/ประกัน/hospital — **หยุด install MCP server จาก npm/GitHub โดยตรง**; ให้ security team review manifest + build เอง หรือใช้เฉพาะจาก enterprise-grade vendor (Anthropic first-party, OpenAI, Microsoft, Cloudflare). Cost ที่โดน SSH key + cloud creds leak ในหนึ่ง incident จะสูงกว่า cost ที่ประหยัดจาก community MCP เกินสิบเท่าเสมอ.

## Sources
- [Deadbugz: Currently Active MCP Supply-Chain Campaign — Pillar Security](https://www.pillar.security/blog/deadbugz-currently-active-mcp-supply-chain-campaign)
- [MCP security September 2026: Deadbugz + 3 server CVEs — Adversa AI](https://adversa.ai/blog/top-mcp-security-resources-september-2026/)
- [Deadbugz shows how MCP metadata poisoning evades AI agent trust](https://nhimg.org/articles/deadbugz-shows-how-mcp-metadata-poisoning-evades-ai-agent-trust/)

---

## Audio script
สัปดาห์นี้ทีม security หลายเจ้ารวมข้อมูลและตั้งชื่อ campaign ว่า Deadbugz ครับ — malicious MCP server ที่ออกแบบมาเพื่อหลบ code review โดยเฉพาะ. ผู้โจมตีสร้าง MCP server ที่ประกอบด้วย tool 2 ตัวธรรมดาไม่มีพิษ text formatting กับ summarization. Reviewer ดู PR ใหม่จะไม่เจออะไรผิด static analysis ไม่ trigger LLM review บอกว่าปลอดภัย. แต่ payload จริงถูก runtime-gate — server เก็บ counter ว่า client เรียก tool มาแล้วกี่ครั้ง พอถึง 3 ครั้ง metadata ที่ server ส่งกลับ ตัว tool description ที่ agent อ่านเพื่อ decide จะ rewrite เป็นคำสั่งไปค้น SSH key AWS credential shell history และ Kubernetes config พร้อมซ่อนไม่ให้ user เห็น. Delivery ทำผ่าน GitHub account ชื่อ zellkernel ยิง 23 PR ใน 74 นาทีเข้า project AI MCP dev tool ที่ไม่เกี่ยวกัน. ประเด็นที่นักวิจัยทุกเจ้าชี้เหมือนกัน นี่ไม่ใช่ code vulnerability แบบเดิม code ของ server สะอาดทุกบรรทัดที่คนหรือ machine อ่านได้ ประเด็นอยู่ที่ metadata poisoning ผ่าน MCP protocol contract ตัว protocol ที่ agent เชื่อ tool description เพื่อ decide เรียก tool ไหน = surface area ใหม่ที่ก่อนหน้านี้ไม่มีในโลก supply chain. Signal ตามมา ทุก enterprise ที่ deploy agent ต้อง whitelist MCP server กับรัน tool description ผ่าน sanitization layer ก่อน hand ให้ model. MCP audit จะเป็น baseline requirement ใน SOC 2 กับ ISO 42001 ในปี 2027. สำหรับทีมไทย โดยเฉพาะสาย bank ประกัน hospital ที่กำลัง POC agent เชื่อม MCP — หยุด install MCP server จาก npm หรือ GitHub โดยตรง ให้ security team review manifest แล้ว build เอง หรือใช้เฉพาะจาก enterprise-grade vendor. cost ที่โดน credential leak หนึ่งครั้ง สูงกว่า cost ที่ประหยัดจาก community MCP เกินสิบเท่าเสมอ
