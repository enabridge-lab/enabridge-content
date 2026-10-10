---
date: 2026-10-10
slug: 26-10-11-0614
topic: agentic-ai
reading_time_min: 3
sources: 4
image_prompt: |
  Editorial isometric illustration of a glass vault labeled "CKG CONTRACT KNOWLEDGE GRAPH"
  with glowing nodes and edges inside connecting clauses, deals, and signatures. Outside the
  vault, a small navy-blue Ironclad robot-agent reads a floating contract. Giant stacked
  labels in the sky: "AGENT + GRAPH", "DATA STAYS INSIDE", "LEGAL + PROCUREMENT + SALES".
  Deep ink background, electric blue and gold accents, high contrast for 200px thumbnail.
  1:1 aspect ratio, no real human faces.
image: images/26-10-11-0614-03-ironclad-contract-knowledge-graph.png
---

# Ironclad ยิง Agent + Contract Knowledge Graph — vertical agent รุ่นใหม่มา pattern เดียวกัน "domain graph + agent + data stay inside"

## TL;DR
- 8 ต.ค. 2026 — Ironclad (SF, contract lifecycle management) เปิด **Ironclad Agent** + **Contract Knowledge Graph (CKG)** ใน press release ทางการ
- ตัว agent วิ่งงาน legal / procurement / sales ด้วยภาษาธรรมชาติ โดย CKG เป็น layer graph ของ clauses + relationships + obligations + ประวัติการเจรจาที่ป้อน context ให้
- **ข้อมูลสัญญาคงอยู่ใน environment ของลูกค้า** — pitch ตรงจุด enterprise ที่กลัว leak ให้ foundation model, ยัง**ไม่มี third party verify ประสิทธิภาพ**

## เกิดอะไรขึ้น
Ironclad เป็นเจ้า CLM (contract lifecycle management) ที่ Workday + Y Combinator หนุนมานาน valuation รอบล่าสุด ~$3.2B วันพุธ 8 ต.ค. ประกาศเปิดสองสินค้าพร้อมกัน

สินค้าแรกคือ **Ironclad Agent** — ที่เดียวที่ทีม legal / procurement / sales ใช้ภาษาธรรมชาติสั่งงาน: "ค้นหาสัญญา NDA ทั้งหมดที่หมดอายุใน Q1 ที่มี termination clause เขียนว่าแจ้งล่วงหน้า 60 วันขึ้นไป" หรือ "เริ่ม redline draft ที่ได้จาก counterparty นี้ตาม playbook ปกติของเรา" agent วิ่งผ่าน Ironclad workflow เอง ไม่ต้องสร้างคำสั่งผ่าน UI step by step

สินค้าที่สองคือ **Contract Knowledge Graph (CKG)** — layer ใหม่ที่ป้อน context ให้ agent CKG โยง **clauses, relationships, obligations, และประวัติการเจรจา** ของทุกสัญญาในบริษัทลงใน graph เดียว agent query graph นี้แล้วเอาผลลัพธ์ไปตัดสินใจ ไม่ใช่ RAG แบบปกติที่ chunk + embed + retrieve

Jason Boehmig CEO ย้ำว่า **CKG อยู่ใน environment ของลูกค้า** — foundation model เห็นผลลัพธ์ query แต่ไม่ได้ absorb ข้อมูลสัญญาเข้า training data นี่คือ pitch ตรงจุด enterprise legal team ที่เป็น **gatekeeper** ไม่ยอมให้ข้อมูลสัญญารั่วไหลไปยัง OpenAI/Anthropic/Google

Customer quote ในแถลงการณ์มาจาก Associate General Counsel ของ **ANDMORE** พูดถึงเวลาที่ประหยัดในการ review สัญญา — แต่**ไม่มีตัวเลข %** ไม่มี third party case study ยังเป็น vendor-driven claim

## ทำไมสำคัญ
Ironclad เป็นเจ้าที่สามในสัปดาห์เดียวที่ประกาศ **domain graph + agent** pattern — ก่อนหน้านี้ Atlassian ประกาศ **Teamwork Graph** คู่ **AMP (Agentic Multiplayer Protocol)**, Salesforce เปิด **Agentforce** คู่ **Data Cloud graph** pattern เริ่มชัดขึ้นเรื่อย ๆ: **"generic RAG หมดอายุใน vertical SaaS — ต้องมี knowledge graph เฉพาะ domain ที่ agent query"**

เหตุผลง่าย ๆ — RAG ปกติดีสำหรับ document retrieval แต่สัญญามีความสัมพันธ์หลายชั้น: master agreement โยง SOW, amendment โยง original, termination clause โยง notice period จาก section อื่น Chunk + embed ไม่รักษาความสัมพันธ์เหล่านี้ graph รักษาได้

สำหรับ Harvey + Robin AI + Spellbook (คู่แข่งใน legal AI) — pattern นี้บังคับให้ต้องตอบด้วย graph layer ของตัวเองภายใน 6-12 เดือน หรือยอมแพ้ตลาด enterprise CLM

## มุม AI Agent Platform
**Builders** ที่สร้าง vertical agent (legal, healthcare, finance, insurance) ควร**หยุดสร้าง chat UI บน RAG generic** แล้วเริ่มสร้าง domain knowledge graph ตั้งแต่ day 1 — ขั้นต่ำคือ ontology ที่ชัดเจน + edge relationships + temporal versioning; ถ้าทีมเล็กไม่มี resource ใช้ Neo4j หรือ ArangoDB เป็น base, อย่าสร้างบน vector store อย่างเดียว

**Users / business** — ทีม legal / procurement / finance ไทยที่ใช้ CLM / ERP / contract management ควรถามเวนเดอร์: "คุณมี knowledge graph ของ domain เราไหม? ข้อมูลเราถูก absorb เข้า training data หรือเปล่า?" ถ้าเวนเดอร์ตอบไม่ชัดเจน แปลว่า technical architecture ยัง RAG-era อยู่ ไม่พร้อม agent-era ปีหน้า

**Ecosystem** — pattern นี้สร้าง **moat ใหม่** ให้ incumbent SaaS: ข้อมูล 10 ปีของลูกค้า + ontology ที่ตัวเองเท่านั้นเข้าใจ = graph ที่ build-from-scratch ไม่ได้ Startup ที่พยายามแย่งตลาดจาก Ironclad / DocuSign / Workday ด้วย AI อย่างเดียว ขายยากขึ้น ต้องมี graph ของตัวเอง + ลูกค้าให้สัมภาษณ์แล้วใช้ pattern "import ข้อมูลเก่าของ incumbent เข้า graph เรา" ไม่งั้นแพ้ switching cost

## Sources
- [Ironclad Launches New AI Agents Grounded in Commercial Context — PR Newswire](https://www.prnewswire.com/news-releases/ironclad-launches-new-ai-agents-grounded-in-commercial-context-helping-teams-negotiate-better-and-capture-more-value-from-every-deal-302900338.html)
- [Ironclad Launches New AI Agents Grounded in Commercial Context — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/ironclad-launches-ai-agents-grounded-130000530.html)
- [Ironclad Agent Overview — Ironclad Support](https://support.ironcladapp.com/hc/en-us/articles/42346411035799-Ironclad-Agent-Overview)
- [Ironclad Launches New AI Agents — SalesTechStar](https://salestechstar.com/sales-marketing/ironclad-launches-new-ai-agents-grounded-in-commercial-context-helping-teams-negotiate-better-and-capture-more-value-from-every-deal/)

---

## Audio script
ข่าวที่สามครับ Ironclad เจ้า contract lifecycle management ที่หลายคนรู้จัก เปิด Ironclad Agent คู่กับ Contract Knowledge Graph หรือ CKG วันที่ 8 ตุลาคม ตัว agent วิ่งงาน legal procurement sales ด้วยภาษาธรรมชาติ สั่งงานเช่น ค้นหาสัญญา NDA ทั้งหมดที่หมดอายุไตรมาสหนึ่ง หรือ เริ่มดราฟท์ redline ตาม playbook ปกติ แล้ว agent วิ่ง workflow ของ Ironclad เอง ไม่ต้องกด UI step by step

สิ่งที่น่าสนใจคือ CKG — layer ใหม่ที่โยง clauses relationships obligations และประวัติการเจรจาของทุกสัญญาลงใน graph เดียว agent query graph นี้แทน RAG แบบปกติที่ chunk แล้ว embed แล้ว retrieve — เพราะสัญญามีความสัมพันธ์หลายชั้น master agreement โยง SOW amendment โยง original ซึ่ง RAG ปกติรักษาไม่ได้ ที่สำคัญคือ CKG อยู่ใน environment ของลูกค้า foundation model ไม่ absorb ข้อมูลสัญญาเข้า training data pitch ตรงจุด enterprise legal team ที่กลัวข้อมูลรั่ว

นี่เป็นเจ้าที่สามในสัปดาห์เดียวที่ประกาศ domain graph คู่กับ agent หลัง Atlassian กับ Salesforce pattern เริ่มชัดขึ้น generic RAG หมดอายุใน vertical SaaS ต้องมี knowledge graph เฉพาะ domain สำหรับ builders ที่สร้าง vertical agent ไทยไม่ว่าจะ legal healthcare finance หรือ insurance ควรหยุดสร้าง chat UI บน RAG generic แล้วเริ่มสร้าง domain knowledge graph ตั้งแต่ day 1 เพราะ pattern นี้สร้าง moat ใหม่ให้ incumbent SaaS ที่ยากจะโดนแย่งตลาดด้วย AI อย่างเดียวครับ
