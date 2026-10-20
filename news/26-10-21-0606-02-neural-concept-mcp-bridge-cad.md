---
date: 2026-10-21
slug: neural-concept-mcp-bridge-cad
topic: agentic-ai
reading_time_min: 4
sources: 2
image_prompt: |
  An editorial isometric illustration of an industrial design studio where a
  wheel rim sits inside a CAD workspace split into "BEFORE" and "AFTER" halves.
  Beside the rim three stacked numbers glow: "3 MIN vs 1 DAY", "WEEKS → HOURS",
  "70+ OEMs". Thin ribbon bridges arc from the rim toward five labeled gates
  reading "CATIA", "NX", "ANSA", "HYPERMESH", "ABAQUS". A badge in the corner
  reads "MCP BRIDGE". Cobalt and amber palette, strong contrast for 200px
  thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-21-0606-02-neural-concept-mcp-bridge-cad.png
---

# Neural Concept ปล่อย MCP Bridge — MCP ข้ามจาก SaaS เข้าซอฟต์แวร์วิศวกรรมเครื่องกลครั้งแรก Traton เป็น case study

## TL;DR
- 19 ต.ค. Neural Concept (Lausanne, Series C $100M ธ.ค. 2025 นำโดย Goldman Sachs) ปล่อย **MCP Bridge** — Model Context Protocol server ที่ให้ AI agent ขับ CAD / simulation software ตัวจริงของ enterprise
- Connectors รุ่นแรกครอบ **CATIA, NX** (design), **ANSA, HyperMesh** (prep), **Abaqus** (simulation) — ไม่ใช่ reference impl แต่ขาย production customer
- **Traton SE** (Volkswagen Group — truck/bus): engineer เขียน geometry cleanup ของ wheel rim จาก 1 วัน → 3 นาที, การ setup simulation draft จากสัปดาห์ → ชั่วโมง
- CEO Pierre Baqué: "For the first time, the software that shapes every physical product can be operated by AI at enterprise scale" — Neural Concept มีลูกค้า 70+ OEM (Bosch, GE, Subaru, OPMobility)

## เกิดอะไรขึ้น

วันอาทิตย์ 19 ต.ค. Neural Concept ปล่อย **MCP Bridge** — ซึ่งเป็น Model Context Protocol server ตัวแรกที่ทำหน้าที่เป็น bridge ระหว่าง AI agent (Claude, GPT, Gemini class) กับ **commercial engineering software ที่ enterprise ใช้งานจริง**. ตามรายงานของ EEJournal, connector set แรกครอบคลุม 5 เครื่องมือหลักของ aerospace / automotive / industrial design: Dassault Systèmes **CATIA** กับ Siemens **NX** สำหรับ design, BETA CAE **ANSA** กับ Altair **HyperMesh** สำหรับ model preparation, และ Dassault **Abaqus** สำหรับ finite element simulation. ไม่ใช่ research prototype — Neural Concept เป็นบริษัทที่เพิ่งปิด Series C $100M เมื่อธันวาคมปีก่อน นำโดย Goldman Sachs Growth Equity, และ 70+ OEMs เป็นลูกค้าอยู่แล้ว (Bosch, Siemens, GE, Subaru, OPMobility)

Customer story ที่น่าดึงดูดคือ Traton SE — บริษัท heavy truck ของกลุ่ม Volkswagen (ยอดขาย €45B ปี 2025). Ciro Alosa, electromagnetic design engineer ของ Traton, บอก SiliconAngle ว่า agent ที่ขับผ่าน MCP Bridge ลด time-to-cleanup ของ wheel rim จาก **1 วัน เหลือ 3 นาที**. ที่สำคัญกว่านั้น time-to-script ของ validated simulation จาก research paper ลดเหลือ **"สอง-สามวัน"** จากที่เคยเป็นสัปดาห์. CEO Pierre Baqué quote เลยว่า "For the first time, the software that shapes every physical product can be operated by AI at enterprise scale" — คือ claim ว่า CAD / CAE ไม่ใช่ ivory tower ของ CAD specialist อีกต่อไป agent จะกลายเป็นชั้นแรกที่ engineer ใช้งาน

Technical reading: CAD/CAE software (CATIA, NX, Abaqus) เป็น **GUI-first product ที่ไม่มี REST API สวย ๆ** — ส่วนใหญ่ขับผ่าน scripting language proprietary (Python API ของ CATIA เรียก CAA, ของ Abaqus เรียก Abaqus Python, ของ NX เรียก NXOpen) ที่ docs ไม่ครบ, syntax drift ตามรุ่น, และ sandbox ยาก. การ wrap ให้ agent ใช้ได้ผ่าน MCP คือ **non-trivial system engineering** ไม่ใช่แค่ generate scripts — ต้อง handle license token, version drift, undo state, ability ที่ engineer ยังรับผิดชอบ output สุดท้าย. Neural Concept มี advantage คือ 70 OEM customer base + Series C เงิน $100M ที่ให้ build infrastructure ชั้นนี้ได้

## ทำไมสำคัญ

MCP เริ่มจาก Anthropic เมื่อ 1 ปีก่อน และ landing area แรกคือ developer tool (GitHub, Linear, Slack, Supabase, PostgreSQL) — คือ ecosystem ที่ API สะอาด, docs ชัด, และคน CTO ของ 2-3 คนที่ตัดสินใจ adopt. การที่ MCP ข้ามเข้ามาถึง **CAD / CAE ซึ่งเป็น software 30-ปีที่ engineer เครื่องกลใช้** คือ signal สำคัญว่า protocol นี้ไม่ใช่ "fad ของ chat vendor" แต่กำลังกลายเป็น **universal tool-use spec** ที่ vertical SaaS ทุกเจ้าต้อง adopt. ถัดจาก CAD จะเป็น PLM (Teamcenter, Windchill), EDA (Cadence, Synopsys), medical imaging (Agfa, GE Healthcare), legal (Clio, Thomson Reuters) — ทุก category ที่ software เก่า + GUI heavy + revenue stream มั่นคง

เลเยอร์ลึกกว่านั้น: **Neural Concept positioning ตัวเองเป็น "application layer for industrial agent"** ไม่ใช่ CAD vendor replacement. เขาไม่ได้สร้าง CAD ใหม่ — เขาสร้าง layer ที่ agent คุยกับ CAD ของ Dassault, Siemens, Altair ที่ enterprise จ่ายเงินซื้ออยู่แล้ว. Business model นี้แตกต่างจาก SaaS ยุคก่อน — SaaS vendor พยายามแทนที่ incumbent software, แต่ MCP vendor ยุคใหม่ **enabling** incumbent ให้ขาย expansion seat (เพราะ engineer คนหนึ่งผ่าน agent คลิก compute 100x มากกว่าเดิม). Dassault, Siemens, Altair ไม่ควร scared — ควร co-sell กับ Neural Concept

Signal ที่ Enabridge ควรจำ: **"MCP connector สำหรับ software แพง ๆ ที่ไม่มี API"** อาจเป็น startup opportunity ขนาดใหญ่ที่สุดของ ecosystem — เพราะ barrier (deep domain knowledge + customer trust + license partnership) สูงพอที่จะกัน copycat แต่ market (300+ enterprise software vendor ทั่วโลก) ใหญ่พอที่จะมี 10+ unicorn ชั้นนี้

## มุม AI Agent Platform

สำหรับ **Builders** ที่สร้าง agent framework / orchestration: ถ้าคุณ focus เฉพาะ developer tool integration (GitHub, Slack, DB) — vertical opportunity กว้างกว่ามาก. CAD, EDA, PLM, legal doc management, medical imaging ล้วนเป็นตลาดที่ enterprise จ่ายปีละหมื่น-ล้านดอลลาร์/seat และยังไม่มี MCP connector. การเขียน MCP server สำหรับ Abaqus + proving ROI ใน 2 Fortune 500 คือ VC pitch ชัด. สำหรับ **Users / Business** ที่ใช้ CAD/CAE/PLM: ถาม vendor ของคุณ (Dassault, Siemens, Altair, PTC, Autodesk) ว่ามีแผน MCP / agent integration ไหม — ถ้ายัง ให้ eval Neural Concept หรือ copycat ที่กำลังจะเกิด. Engineer หนึ่งคนที่ขับ agent ผ่าน CAD = productivity 10-50x ที่ Traton ยืนยันแล้ว. สำหรับ **Ecosystem**: Dassault, Siemens, Altair, PTC มี 2 ทาง — build MCP ของตัวเอง (slow), หรือ partner กับ Neural Concept + copycat (fast แต่เสีย data layer control). ประวัติศาสตร์ของ SaaS บอกว่า category creator (Neural Concept ในกรณีนี้) จะชนะ seat-level ก่อน incumbent ตื่น

## Sources
- [Neural Concept launches MCP to help AI agents operate commercial CAD tools (SiliconANGLE)](https://siliconangle.com/2026/10/19/neural-concept-launches-mcp-to-help-ai-agents-operate-commercial-cad-tools/)
- [Neural Concept Launches MCP Bridge, Augmenting AI Agents to Operate Industrial Engineering Software (EEJournal)](https://www.eejournal.com/industry_news/neural-concept-launches-mcp-bridge-augmenting-ai-agents-to-operate-industrial-engineering-software/)

---

## Audio script
วันนี้มีข่าวที่คน build agent ควรรู้ — Neural Concept บริษัทจาก Lausanne ที่เพิ่งปิด Series C ร้อยล้านดอลลาร์เมื่อธันวาคมปีก่อน นำโดย Goldman Sachs ประกาศปล่อย MCP Bridge — เป็น Model Context Protocol server ตัวแรกที่ให้ AI agent ขับซอฟต์แวร์ CAD กับ simulation ตัวจริงของ enterprise. Connector รุ่นแรกครอบคลุม CATIA, NX สำหรับ design, ANSA, HyperMesh สำหรับ prep model, และ Abaqus สำหรับ simulation. ลูกค้าแรกคือ Traton บริษัท heavy truck ของกลุ่ม Volkswagen — engineer ของเขาบอกว่าทำ geometry cleanup ของ wheel rim ลดจากหนึ่งวันเหลือสามนาที, การ setup simulation draft จากสัปดาห์เหลือชั่วโมง, และเขียน script simulation จาก research paper ลดเหลือสองสามวัน. ที่สำคัญกว่าตัวเลขคือ signal ว่า MCP กำลังข้ามจาก developer tool ไปถึง enterprise software เก่า 30 ปี. ถัดจาก CAD จะเป็น PLM, EDA, medical imaging, legal doc. ถ้าใครสร้าง agent framework อยู่ MCP connector สำหรับซอฟต์แวร์แพง ๆ ที่ไม่มี API สวย ๆ คือ opportunity ขนาด unicorn เพราะ barrier สูงแต่ตลาดใหญ่. ถ้าใช้ CAD อยู่ให้ถาม vendor ตัวเองว่าแผน MCP เป็นยังไง.
