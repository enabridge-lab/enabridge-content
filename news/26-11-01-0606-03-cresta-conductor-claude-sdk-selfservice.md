---
date: 2026-10-29
slug: cresta-conductor-claude-sdk-selfservice
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a telecom-style control center.
  A central glass console labeled "CRESTA CONDUCTOR" sits in the middle.
  Three glowing pipelines flow from a developer silhouette with a laptop
  labeled "GIT + CI/CD" into the console, and three outputs stream to call-
  center desks marked "ALASKA AIRLINES", "COX", "INTUIT". Above the console
  a bold three-line counter reads "1 WEEK TO PROD", "5× FASTER DEPLOY",
  "$10M+ ATENTO DEAL". A side panel shows five badges stacked:
  "SOC 2", "ISO 27001", "PCI DSS", "HIPAA", "ISO 42001". Deep indigo and
  neon-cyan palette, 1:1 aspect, strong contrast for 200px thumbnails,
  no real human faces.
image:
---

# Cresta เปิด Conductor ให้ developer self-service — Claude Agent SDK + 1 สัปดาห์เข้า prod + 5 compliance badge

## TL;DR
- **Cresta** (CX AI company, backed by a16z + Sequoia + Greylock) ประกาศวันที่ 29 ต.ค. ว่า **Conductor** — agent builder ที่สร้างบน Claude Agent SDK — เปิดให้ enterprise developer **self-service** ไม่ต้องรอ Cresta professional service team
- ตัวเลขที่บริษัทเปิด: **1 week จาก first requirement → production, 5× faster deployment** (ไม่เปิด baseline), **eight-figure multi-year deal กับ Atento** signed พ.ค. 2026 เพื่อ embed Conductor ทั่ว Americas
- Compliance set: **SOC 2 Type II, ISO 27001, PCI DSS, HIPAA, ISO 42001** — ISO 42001 ตัวสุดท้ายคือ AI management system standard ที่เพิ่งเริ่มใช้ ปี 2024 — Cresta เป็นหนึ่งใน vendor แรกที่คุย
- Signal: CX vertical กำลัง **re-platform บน Claude Agent SDK** — บวกกับ Honeycomb, Replit, Vercel ที่เลือก Claude Agent SDK ปีนี้ Anthropic กำลังชนะศึก “agent runtime มาตรฐาน”

## เกิดอะไรขึ้น

Cresta — บริษัท AI สำหรับ contact center ที่มี customer ชื่อดัง Alaska Airlines, Cox Communications, Intuit — ประกาศวันที่ 29 ต.ค. 2026 ว่า **Conductor** เปิด self-service สำหรับ enterprise developer. Conductor สร้างบน **Claude Agent SDK** โดยตรง: developer เขียน Python code เอง, deploy ผ่าน CLI, ใช้ existing Git + CI/CD pipeline, แล้ว Cresta provide infra layer (A/B test, routing, rollback, access management, usage visibility, cost tracking)

ที่ควรสังเกต 3 จุด:

**หนึ่ง** — Conductor **ไม่ใช่ low-code builder อย่าง AgentForce / Microsoft Copilot Studio** — เป็น **code-first platform** ที่ให้ developer เขียน Python แล้ว import ความสามารถ CX ของ Cresta (routing, agent assist, QA). pattern นี้คล้าย **Vercel for CX agents** มากกว่า Salesforce for CX

**สอง** — บริษัท quote **1 week จาก requirement → production, 5× faster deployment**. ไม่เปิด baseline (เทียบกับ in-house build? เทียบกับ competitor? เทียบกับเวอร์ชันเก่าของตัวเอง?) — ลด credibility บ้างแต่ยัง directional. Atento partner signed **multi-year, eight-figure deal** พ.ค. 2026 embed Conductor ข้าม Americas ยืนยันว่าตัวเลขไม่ว่างเปล่าทั้งหมด

**สาม** — compliance set ที่ Cresta เปิดคือ **SOC 2 Type II + ISO 27001 + PCI DSS + HIPAA + ISO 42001**. ตัวสุดท้ายสำคัญ: **ISO 42001** คือมาตรฐาน Artificial Intelligence Management System ที่ ISO ปล่อยปี 2024 — vendor ส่วนใหญ่ยังไม่คุย. Cresta ถือเป็นหนึ่งใน CX vendor แรกที่ claim ISO 42001 — จะกลายเป็น table-stakes ของ RFP ปี 2027 เมื่อ EU AI Act เริ่ม bind ตัวจริง

## ทำไมสำคัญ

CX เป็น vertical ที่สมบูรณ์ที่สุดสำหรับ agentic deployment: workflow มี pattern ชัด (triage, lookup, resolve, escalate), ROI วัดง่าย (handle time, CSAT, first-call resolution), compliance friction สูง (PCI, HIPAA, GDPR). นั่นทำให้ CX เป็นสนามแข่งที่ **vendor ชนะใหม่ได้ ถ้ามีเลเยอร์ที่สูงกว่า script-based bot** — และ Cresta บอกชัดว่า **เลเยอร์นั้นคือ agent + developer SDK + compliance envelope**

ที่น่าสนใจคือ Cresta เลือก **Claude Agent SDK** แทนที่จะสร้าง runtime เอง หรือใช้ LangGraph / Agents SDK. Anthropic ปีนี้สะสม big-name adopter เร็ว: **Honeycomb** (observability), **Replit** (dev), **Vercel** (platform), **Cresta** (CX). pattern คือ company ที่มี vertical expertise + ไม่อยากสร้าง agent harness เองจาก scratch เลือก Claude Agent SDK เพราะ **tool use + context management + sandbox** มาพร้อม

เทียบกับ OpenAI AgentKit ที่ประกาศ wind-down (30 พ.ย. 2026 บริษัท ขอให้ย้ายไป Agents SDK) ความต่างน่าสังเกต: OpenAI vendor-ize Agent Builder แบบ visual → ไม่มี pull-through. Anthropic vendor-ize SDK → developer adopt เพราะ code-first. ปีหน้า **สงคราม agent runtime มาตรฐาน** น่าจะเห็น Claude Agent SDK vs Agents SDK ชนกันตรงๆ, LangGraph เป็น framework ที่ครอบด้านบน

สำหรับ CX สายไทย/SEA: **Atento ที่ Cresta เลือกเป็น flagship partner คือ outsource call center ใหญ่ที่สุดใน LatAm** และมีสาขาใน Philippines + Thailand. ปีหน้า Thailand BPO (TrueMoney contact center, SCB CX) น่าจะเริ่มเห็น Cresta-powered agent ที่ตอบลูกค้าภาษาไทย

## มุม AI Agent Platform

**Builders**: ถ้าคุณสร้าง agent framework ของตัวเอง (CrewAI, Agno, PydanticAI) การแข่งขันเปลี่ยนจาก “ใครมี abstraction สวย” → “ใครคู่ Claude Agent SDK / Agents SDK ได้ดีที่สุด”. Cresta เลือก wrap, ไม่ competing — เพราะ wrap ให้ customer เรียก Claude โดยตรงเมื่อ Cresta ไม่ให้ประโยชน์, และ layer Cresta UI/compliance/routing ด้านบน. นี่คือ **layer wrapper strategy** ที่ Vercel ใช้กับ Next.js

**Users / business**: ถ้าคุณ run contact center / support team, คำถามใหม่คือ “Cresta vs Sierra vs Siena vs in-house”. 1 week-to-prod ทำให้ build vs buy เอียงไปทาง buy ชัดขึ้น — แต่ **vendor lock-in บน Cresta + Claude Agent SDK** จะเป็นค่าใช้จ่ายที่ CTO ต้องชั่งใจ

**Ecosystem**: ISO 42001 กำลังเป็น compliance primitive ใหม่ — vendor ที่ยังไม่ได้ cert จะต้องรีบ. บริษัทไทยที่ใช้ Microsoft Azure / Google Cloud / AWS จะได้ ISO 42001 ผ่าน hyperscaler ไม่ต้องทำเอง — แต่ถ้า deploy agent บน startup vendor ต้องตรวจเอง

## Sources
- [Cresta Opens Agent Platform to Developer Self-Service (CMSWire)](https://www.cmswire.com/contact-center/cresta-opens-agent-platform-to-developer-selfservice)
- [How Cresta turned CX expertise into an agent builder on the Claude Agent SDK (Anthropic)](https://claude.com/blog/how-cresta-turned-cx-expertise-into-an-agent-builder-on-the-claude-agent-sdk)
- [Daily AI Agent News — October 30, 2026 (AI Agent Store)](https://aiagentstore.ai/ai-agent-news/daily/2026-10-30)

---

## Audio script
Cresta ประกาศวันที่ 29 ตุลาคมว่า Conductor ซึ่งเป็น agent builder ที่สร้างบน Claude Agent SDK เปิดให้ enterprise developer self service ไม่ต้องรอ professional service team ของ Cresta แล้ว นั่นหมายความว่า developer เขียน Python เอง deploy ผ่าน CLI ใช้ Git และ CI CD เดิม แล้ว Cresta provide infra layer คือ A B test routing rollback access management cost tracking บริษัท quote ว่าใช้เวลา 1 สัปดาห์จาก requirement แรกไป production เร็วกว่าเดิม 5 เท่า ยืนยันด้วย deal 8 หลักกับ Atento ที่เป็น BPO ใหญ่ที่สุดใน LatAm และมีสาขาที่ไทย compliance ของ Cresta ครบ SOC 2 ISO 27001 PCI DSS HIPAA และที่น่าสังเกต ISO 42001 ซึ่งเป็นมาตรฐาน AI management system ของ ISO ที่พึ่งปล่อยปี 2024 vendor ส่วนใหญ่ยังไม่คุย Cresta เป็นหนึ่งใน CX vendor แรกที่ claim จะกลายเป็น table stakes ของ RFP ปีหน้าเมื่อ EU AI Act bind ตัวจริง ที่น่าสนใจที่สุด Cresta เลือก Claude Agent SDK แทนที่จะสร้าง runtime เอง — ปีนี้ Anthropic สะสม big name adopter เร็ว Honeycomb Replit Vercel Cresta pattern คือบริษัทที่มี vertical expertise ไม่อยากสร้าง agent harness เองจาก scratch เลือก Claude Agent SDK เพราะ tool use context management sandbox มาพร้อม ปีหน้าสงคราม agent runtime มาตรฐานน่าจะเห็น Claude Agent SDK vs OpenAI Agents SDK ชนกันตรงๆ ครับ
