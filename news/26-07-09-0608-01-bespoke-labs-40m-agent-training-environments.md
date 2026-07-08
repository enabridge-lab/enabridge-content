---
date: 2026-07-09
slug: 26-07-09-0608-01-bespoke-labs-40m-agent-training-environments
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A cinematic hero of a glowing enterprise "digital twin" city under a glass
  dome: miniature skyscrapers labeled "SLACK", "TICKETS", "MICROSERVICES",
  "LOGS", "EMAIL" glowing in cyan; robotic silhouettes wander streets learning
  the map; a large title plate above reads "TRAINING ENVIRONMENTS = NEW MOAT"
  and beside it "$40M SERIES A · BESPOKE LABS". Editorial isometric render,
  high-contrast, 1:1 aspect, no real human faces (silhouettes only).
image: images/26-07-09-0608-01-bespoke-labs-40m-agent-training-environments.png
---

# Bespoke Labs ปิด $40M Series A — วางเดิมพันว่า "moat ต่อไปของ agent ไม่ใช่โมเดล แต่คือสนามฝึก"

## TL;DR
- **Bespoke Labs** ปิด **$40M Series A** (นำโดย Wing VC, ร่วม Mayfield/The House Fund/8VC + angels จาก Anthropic, OpenAI, Meta) วันจันทร์ 6 ก.ค. — บริษัทสร้าง **environment ที่เลียนแบบบริษัทจริง** (codebase ใหญ่, microservices, Slack, tickets, logs, email) สำหรับให้ agent ฝึก long-horizon workflow
- อ้างอิง **METR benchmark**: task ที่ agent ทำสำเร็จ reliably โตขึ้น 2 เท่าทุก **7 เดือน** — แต่ปัญหาคือ agent ทำงานสั้นๆ ได้เก่ง, พอ 2-3 วันเริ่มพัง; Bespoke แก้ตรงจุดนี้ด้วยการปั๊ม synthetic enterprise เต็มรูปแบบให้ agent ตะลอนฝึก
- ผู้ก่อตั้ง Mahesh Sathiamoorthy + Alex Dimakis เป็นทีมเบื้องหลัง **Terminal-Bench** และ **OpenThoughts** (dataset ดาวน์โหลด 500k+ ใช้ที่ Thinking Machines Lab, Meta, Amazon) — ไม่ใช่ startup ธรรมดา, เป็น research lab ที่ระบบนิเวศ frontier lab พึ่งพา benchmark ของเขาอยู่แล้ว

## เกิดอะไรขึ้น

วันจันทร์ที่ 6 กรกฎาคม 2026 Bespoke Labs — research lab ตั้งใน SF ปี 2024 — ประกาศปิด **$40M** ในรอบที่รวม Series A นำโดย **Wing Venture Capital** และ seed ที่ปิดโดย **8VC** ทั้งสองรอบ. รายชื่อ angel สั้น ๆ แต่หนัก: Jeff Dean (Google DeepMind), Tristan Handy (dbt Labs CEO), Spiros Xanthos (Resolve AI CEO), Dheeraj Pandey (DevRev CEO), บวก angels จาก Anthropic, OpenAI, Meta

สิ่งที่ Bespoke ทำไม่ใช่ agent — **แต่เป็นสนามฝึก agent**. บริษัทออกแบบ **environment** ที่จำลองบริษัทจริงทั้งใบ: repo หลายแสนบรรทัด, microservices ที่ผูกกัน 30-40 ตัว, ticket ใน Jira, email ใน Outlook, logs ที่ pipe ผ่าน Datadog-แบบ, conversations ใน Slack. agent ที่วางลงในนี้จะเจอ "งานจริงเลียนแบบ" — pull request ที่ break test เพราะ dependency chain, incident ที่ต้อง trace ผ่าน 5 service, requirement ใน spec ที่ engineer 3 คนตีความไม่เหมือนกัน — สิ่งที่ synthetic benchmark เก่า ๆ ทำไม่ได้

Mahesh Sathiamoorthy ผู้ร่วมก่อตั้ง (มาจาก Google Research + Databricks) พูดว่าปัญหาหลักของ agent ตอนนี้ไม่ใช่ IQ, แต่คือ **stamina** — "agent เขียน code, ตอบคำถาม, ปิด ticket สั้น ๆ ได้ดี, แต่พอต้อง operate autonomously ต่อเนื่อง 3-4 ชั่วโมงเริ่มหลง". อ้างอิง benchmark **METR** ที่ Bespoke ช่วยพัฒนา (พร้อม **Terminal-Bench** ของทีมเอง), **task length ที่ agent ทำเสร็จ reliably** โตประมาณ **2 เท่าทุก 7 เดือน** — แต่ trend line นั้นจะฝ่าเพดาน "ทำงานหลายวันโดยไม่พัง" ต้องมี **training environment** ที่ agent ได้เห็นความยุ่งของบริษัทจริง

Wing VC ที่นำรอบนี้ signal ชัดว่า thesis คือ **"เกม data ของ AI ยุค 2020-2024 = internet scraping จบแล้ว, เกม data ยุค agent = การ synthesize บริษัท"**. Alex Dimakis (UT Austin ML professor, ผู้ร่วมก่อตั้ง) บอก TechCrunch ว่าลูกค้ากลุ่มแรกคือ **frontier lab ที่ต้องการ post-training environment** ก่อน ship agent model รุ่นต่อไป, ไม่ใช่ enterprise ที่จะเอาไป deploy — Bespoke เป็น **infrastructure vendor สำหรับผู้ทำ model** ไม่ใช่ตลาด end-user โดยตรง

## ทำไมสำคัญ

Pattern ที่เห็นชัดขึ้นเรื่อย ๆ ตั้งแต่ **GPT-5.6 Ultra mode** เปิดตัวสัปดาห์ก่อน (Sol reach 91.9% บน Terminal-Bench 2.1 ด้วยการ spawn sub-agent), และ **Claude Sonnet 5** ที่ Anthropic pitch ตัวเองว่า "agentic default" — **frontier lab แข่งกันไม่ใช่ที่ชิ้น model แต่ที่ agent stamina + tool use**. คำถามคือ stamina มาจากไหน? คำตอบง่าย ๆ คือ RLHF/RLVR บน **long-horizon task ในสภาพจริง** — และสภาพจริงนั้นก็คือสิ่งที่ Bespoke สร้าง

เทียบกับ **Patronus AI** ($50M เมื่อ 25 มิ.ย.) ที่สร้าง "digital worlds เพื่อ stress-test agent", **ScaleAI/xAI** ที่มี team RL environment ในบ้าน, และ **METR** ที่ทำ measurement — Bespoke อยู่ตรงกลาง: research-first, benchmark-first, ทีมที่ frontier lab เชื่อว่า "ไม่ cheating benchmark เพราะเราเป็นคนเขียน benchmark". นี่คือ moat จริง — Wing VC ไม่ได้เดิมพัน "product ที่ขาย", แต่เดิมพัน **trust ที่ frontier lab มีต่อทีมนี้** เพราะ Terminal-Bench / OpenThoughts คือของที่ Meta/Amazon/Thinking Machines Lab download ไปใช้จริง

Signal ต่อจากนี้: **การ evaluate agent จะเลิกใช้ prompt-based benchmark ไปสู่ "รันใน enterprise-สังเคราะห์ 48 ชั่วโมงแล้วนับ outcome"** — และ vendor ที่ควบคุมสภาพจำลองนั้นได้จะมีอำนาจเหมือน MLPerf ในยุค pretraining. Bespoke, Patronus, และ **Terminal-Bench-alternative** (ต้องดูว่าใครจะออก) จะกลายเป็น "AV-TEST/AV-Comparatives ของ agent world"

## มุม AI Agent Platform

**Builders** ที่สร้าง agent framework — ถ้าคุณ ship agent runtime ที่ไม่มีข้อมูลว่ามัน perform อย่างไรใน **long-horizon** (Bespoke Terminal-Bench + Patronus digital world + METR task length), คุณจะขายให้ CIO ไม่ได้ในครึ่งหลัง 2026 เพราะ RFP รอบใหม่จะขอ **third-party evaluated agent metric**. ถ้าเป็น startup framework/orchestrator (LangGraph, CrewAI, AutoGen alternative) ต้อง cache environment integration ตั้งแต่วันนี้ — ผูกกับ Bespoke API ให้ agent ที่ build ด้วย framework ของคุณ test-run ได้ก่อน deploy

**Users / business ที่ deploy agent** — ในไทย SCB/AIS/ปตท./retail/insurer ที่ pilot agent มา 6-12 เดือน คำถามที่ตอบยากที่สุดเวลา present ต่อ CEO คือ **"agent นี้ทำงานเสถียรกี่ % ตลอด 8 ชั่วโมง"**. รอบต่อไปเวลา sign vendor, ขอ **evaluation report จาก third-party environment** (Bespoke, Patronus, หรือของ vendor เอง) — ถ้าตอบไม่ได้แสดงว่า vendor นั้นไม่มี data บอกว่า agent ตัวเอง stamina เท่าไร, คุณกำลังเป็น human evaluator ให้เขาโดยไม่รู้ตัว. **Ecosystem**: hyperscaler (AWS Bedrock, Azure AI Foundry, Google Vertex) จะแข่งกันเปิด "agent evaluation as a service" ใน 2 ไตรมาสข้างหน้า — คนที่ integrate Bespoke/Patronus environment ก่อนจะได้ enterprise trust

## Sources
- [Bespoke Labs Announces $40M to Build the Environments That Train Reliable Agents (BusinessWire)](https://www.businesswire.com/news/home/20260706827813/en/Bespoke-Labs-Announces-$40M-to-Build-the-Environments-That-Train-Reliable-Agents)
- [Bespoke Labs raises $40M for AI agent training worlds (Axios Pro)](https://www.axios.com/pro/enterprise-software-deals/2026/07/06/bespoke-labs-training-ai-agents)
- [Bespoke Labs Announces $40M to Build the Environments That Train Reliable Agents (AIwire)](https://www.hpcwire.com/aiwire/2026/07/07/bespoke-labs-announces-40m-to-build-the-environments-that-train-reliable-agents/)

---

## Audio script
เพื่อน ๆ ครับ เช้านี้มีข่าวจากซานฟรานที่น่าคิดมากคือ Bespoke Labs ปิด Series A สี่สิบล้านดอลลาร์ นำโดย Wing VC — แต่สิ่งที่พวกเขาทำไม่ใช่ AI agent นะครับ แต่คือ สนามฝึก agent เขาสร้าง environment ที่จำลองบริษัทจริงเต็มใบ — codebase หลายแสนบรรทัด microservices สามสี่สิบตัว Slack tickets email logs — ทุกอย่างที่ agent ต้องเจอในบริษัทจริง แล้วให้ agent วิ่งเข้าไปฝึก long-horizon workflow ที่ทำต่อเนื่องเป็นชั่วโมงเป็นวัน จุดสำคัญคือทีมนี้ไม่ใช่ startup ธรรมดา — เป็นคนที่สร้าง Terminal-Bench และ OpenThoughts dataset ที่ Meta Amazon Thinking Machines Lab ดาวน์โหลดใช้จริง frontier lab เชื่อทีมนี้เพราะเขาเป็นคนเขียน benchmark เอง signal สำคัญคือ เกม data ยุค 2020 ถึง 2024 คือการ scrape internet เกม data ยุค agent จากนี้ไปคือการ synthesize บริษัท และ Bespoke Patronus METR คือกลุ่มที่จะกลายเป็น MLPerf ของ agent world สำหรับคนที่ deploy agent ในไทย — SCB AIS ปตท retailer insurer ที่ pilot agent มาแล้ว 6 เดือนหนึ่งปี คำถามที่ตอบยากที่สุดเวลาไปเสนอ CEO คือ agent นี้ทำงานเสถียรกี่เปอร์เซ็นต์ตลอด 8 ชั่วโมง รอบต่อไปเวลาเซ็น vendor ขอ evaluation report จาก third-party environment ให้ได้ ถ้าตอบไม่ได้แสดงว่า vendor เขายังไม่รู้จัก agent ตัวเองด้วยซ้ำครับ
