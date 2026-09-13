---
date: 2026-09-14
slug: salesforce-long-horizon-runtime-hunter-weeks
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A sleek editorial illustration of a business timeline stretched from Monday to
  Friday across weeks, with a glowing agent icon labeled "HUNTER" moving through
  it, opening and closing tasks along the way. Below, three stacked panels read
  "PLAN", "REMEMBER", "RESUME" in bold sans-serif. A silhouetted seller in the
  background hands over a folder titled "PIPELINE" while a Salesforce cloud logo
  glows softly in the corner. Editorial isometric style, deep navy background
  with amber highlights, 1:1 aspect, no real human faces.
image: images/26-09-14-0609-01-salesforce-long-horizon-runtime-hunter-weeks.png
---

# Salesforce เปิด long-horizon runtime — agent ที่ทำงานเป็นสัปดาห์ ไม่ใช่แค่ chat

## TL;DR
- Salesforce ประกาศ Agentforce portfolio ใหม่ 11 กันยา — เจ็ด agent มีชื่อจริง (Casey, Paige, Carter, Hunter, Marshall, Piper, Fin) แต่ประเด็นจริงคือ **long-horizon runtime** ที่ให้ agent ทำงานได้ข้ามวัน ข้ามสัปดาห์
- **Multi-Agent Orchestration GA** พร้อมกัน — routing งานข้าม agent ให้ทำงานเป็นทีมเดียว
- Hunter (outbound sales agent) เป็น agent ตัวแรกที่รันบน runtime ใหม่ — pilot ตอนนี้, GA พฤศจิกา

## เกิดอะไรขึ้น

Salesforce ใช้เวที Agentforce บอกตลาดว่ายุค "agent = chat interface ที่พูดตอบกลับได้" จบแล้ว. บริษัทเปิด **long-horizon runtime** — runtime ที่ออกแบบมาสำหรับ agent ที่ต้องทำงานต่อเนื่องเป็นวัน เป็นสัปดาห์ เป็นเดือน โดยจำได้ว่าครั้งที่แล้วทำอะไรไว้ วางแผนระยะยาวได้ กลับมาทำงานต่อจากที่ค้างได้เอง. Runtime นี้มีสามชิ้นหลัก: memory, durable execution, และ dynamic steering — สามคำที่ก่อนหน้านี้อยู่ในบทความ engineering blog ของ startup ตัวเล็ก ๆ ตอนนี้กลายเป็น product SKU ของ CRM รายใหญ่.

Hunter คือ proof ว่ามันใช้จริงได้ — outbound sales agent ที่ทำงานตาม pipeline ตั้งแต่ค้น account, จัด outreach cadence, ตามผลลัพธ์, และประสาน handoff กับ seller ที่เป็นคน. ปกติงานพวกนี้ SDR ทำเป็นสัปดาห์ ๆ เพราะต้องรอ prospect ตอบ ต้องรอ deal cycle เดิน. เดิม agent สู้ไม่ได้เพราะ chat session หมด context ทุกครั้ง. Runtime ใหม่ให้ agent พก plan + memory ติดตัวข้ามครั้ง.

พร้อมกัน Salesforce ประกาศ **Multi-Agent Orchestration GA** — layer ที่ทำหน้าที่ route งานข้าม agent ให้ทำงานเป็นทีมประสานงาน. ตัวอย่าง: Hunter ค้นเจอ lead → ส่งต่อให้ Casey (service) เตรียม context → ส่งกลับให้ seller คน. AI Skills in Coworker (pilot) และ Agent Optimizer จะ GA ตุลาคม.

## ทำไมสำคัญ

หนึ่งปีที่ผ่านมาทุกคนพูดว่า "agent จะเปลี่ยนธุรกิจ" แต่ 80% ของ enterprise apps ที่ฝัง agent แล้ว มีแค่ 31% ที่จริง ๆ deploy production. ช่องว่างระหว่าง embedding กับ operating คือเรื่อง runtime — agent ที่ทำงานได้ 5 นาทีแล้วลืม ไม่ใช่ agent ที่ธุรกิจกล้า trust ให้ทำ pipeline sales จริง. Salesforce ประกาศครั้งนี้คือการยอมรับ officially ว่า chat runtime ไม่พอ — long-running orchestration ต้องเป็น first-class primitive.

signal ที่ตามมา: expect ทุก enterprise agent platform (Microsoft Copilot, ServiceNow AI Agents, IBM watsonx Orchestrate, SAP Joule) ต้อง reposition ตัวเองรอบ concept "long-horizon" ในไตรมาสถัดไป. คำว่า "durable execution" ที่ Temporal / Restate / Inngest ใช้มาสอง-สามปี ตอนนี้กลายเป็นคำที่ CRM sales rep ก็ต้องพูดได้.

## มุม AI Agent Platform

**Builders** — ใครกำลังสร้าง agent framework: ถ้ายังไม่มี memory layer + durable execution primitives ต้องรีบทำ. Salesforce เพิ่งตั้ง benchmark ว่า long-horizon = ต้องมี. Framework อย่าง LangGraph, Mastra, Google ADK ที่มี stateful graph aiready รับได้ก่อน. **Users / business** ที่กำลัง deploy agent — checklist ใหม่: agent ที่ซื้อวันนี้ต้องทำงานได้ข้ามครั้ง ข้ามสัปดาห์ ไม่งั้นได้แค่ chatbot ที่แพงกว่าเดิม. **Ecosystem** — vendor observability (LangSmith, Braintrust, Arize) ต้องขยาย trace model ให้ handle sessions ที่ยาวเป็นสัปดาห์. Storage, memory vendors (Zep, mem0, Redis, Pinecone) มี wind ในหลังทันที.

สำหรับทีมไทยที่กำลังจะ pilot AI agent ในธุรกิจ — คำถามที่ต้องถาม vendor ก่อนเซ็นสัญญาปีนี้: "agent คุณจำได้ไหมว่าอาทิตย์ที่แล้วคุยกับลูกค้าคนนี้เรื่องอะไร?"

## Sources
- [Salesforce Debuts Job-Ready Agentforce Agents and Long-Horizon Runtime](https://www.unite.ai/salesforce-debuts-job-ready-agentforce-agents-and-long-horizon-runtime/)
- [Salesforce Expands Agentforce With a New Portfolio of AI Agents Built for High-Value Work](https://www.salesforce.com/news/stories/agentforce-job-ready-ai-agents/)
- [Salesforce agents gain a runtime that pursues goals over weeks, not chats](https://ppc.land/salesforce-agents-gain-a-runtime-that-pursues-goals-over-weeks-not-chats/)

---

## Audio script
วันนี้มีข่าวใหญ่จาก Salesforce ที่เพิ่งเปิด Agentforce portfolio ใหม่ พร้อม AI agent เจ็ดตัวที่มีชื่อจริง แต่ประเด็นสำคัญไม่ใช่ชื่อ agent ครับ ประเด็นคือ Salesforce เปิดตัว long-horizon runtime — runtime ที่ให้ agent ทำงานต่อเนื่องเป็นวัน เป็นสัปดาห์ ไม่ใช่แค่ในหนึ่ง chat session ปกติ. Runtime ตัวใหม่นี้มี memory มี durable execution และ dynamic steering — สามชิ้นที่ทำให้ agent เก็บ plan ระยะยาว จำได้ว่าครั้งก่อนคุยกับลูกค้าเรื่องอะไร แล้วกลับมาทำงานต่อได้เอง. Hunter agent สำหรับ outbound sales เป็นตัวแรกที่รันบน runtime นี้ ตอนนี้อยู่ pilot จะ GA พฤศจิกายน. พร้อมกัน multi-agent orchestration ก็ GA แล้วครับ — routing งานข้าม agent ให้ทำงานเป็นทีมเดียวได้. ทำไมสำคัญ? เพราะปีที่ผ่านมา 80% ของ enterprise app ฝัง agent แล้ว แต่แค่ 31% ที่ deploy production จริง ช่องว่างนี้คือเรื่อง runtime นี่แหละครับ. Chat session สั้น ๆ ไม่พอสำหรับ workflow ธุรกิจจริง. คำที่ทีม engineer ใช้กันมานาน เช่น durable execution กำลังจะกลายเป็นคำที่ CRM sales ก็ต้องพูดได้. สำหรับ builder ที่กำลังสร้าง agent — memory และ durable execution ต้องเป็น first-class ไม่ใช่ optional. สำหรับ business ที่กำลังจะ pilot agent — คำถามใหม่ที่ต้องถาม vendor คือ agent คุณจำได้ไหมว่าอาทิตย์ที่แล้วทำอะไรไว้.
