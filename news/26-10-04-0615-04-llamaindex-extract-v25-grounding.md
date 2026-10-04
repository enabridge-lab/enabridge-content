---
date: 2026-10-04
slug: llamaindex-extract-v25-grounding
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: |
  Editorial isometric illustration of a stack of enterprise documents being
  scanned by a glowing agent harness labeled "EXTRACT v2.5"; a prominent
  benchmark meter arcs across the top from a dim bar "46.8" to a bright bar
  "80.6" stamped "GROUNDING". A side panel reads "F1 87.1 to 93.9". Dashed
  bounding boxes highlight correct fields on the documents. Cinematic
  forest-green and warm-amber palette, bold text rendering for 200px
  thumbnails, no real human faces, 1:1 aspect. Editorial Wired-style cover.
image: images/26-10-04-0615-04-llamaindex-extract-v25-grounding.png
---

# LlamaIndex ปล่อย Extract v2.5 — grounding score กระโดด 46.8 → 80.6, schema extraction agent ชั้นใหม่

## TL;DR
- 1 ต.ค. LlamaIndex เปิด **Extract v2.5** — schema-based document extraction agent generation ใหม่, ไม่มีค่า per-page เพิ่ม
- **ExtractBench grounding** กระโดด: Agentic tier **46.8 → 80.6**, Agentic Plus **46.4 → 82.2** — เกือบ 2 เท่า
- **Value F1** ขึ้นทุก tier: Cost Effective 87.1 → 93.9, Agentic 89.8 → 95.8, Agentic Plus 95.1 → 96.4

## เกิดอะไรขึ้น
LlamaIndex ปล่อย **Extract v2.5** วันที่ 1 ตุลาคม — generation ใหม่ของ schema-based document extraction agent ที่บริษัทวาง positioning เป็น "RAG infrastructure สำหรับ enterprise document". ตัวเลขที่ทำให้คนในวงการต้องสะดุดคือ **grounding score บน ExtractBench** — เป็น benchmark ที่วัดว่า agent สามารถ cite กลับไปที่ bounding box ที่ถูกต้องของต้นฉบับได้มั้ย ไม่ใช่แค่ตอบถูก. Agentic tier กระโดดจาก **46.8 → 80.6** และ Agentic Plus จาก **46.4 → 82.2** — เพิ่มเกือบเท่าตัว.

Value F1 ซึ่งวัด accuracy ของค่าที่ extract ออกมาก็ขึ้นทุก tier: Cost Effective **87.1 → 93.9**, Agentic **89.8 → 95.8**, Agentic Plus **95.1 → 96.4**. ที่สำคัญคือ **ไม่มีค่า per-page เพิ่ม** — LlamaIndex ขึ้น quality โดยไม่ขึ้นราคา.

เบื้องหลังเทคนิค LlamaIndex บอกว่า v2.5 รันบน **agent harness ใหม่** ที่ออกแบบมาเฉพาะสำหรับ document extraction, ได้แรงบันดาลใจมาจาก coding agent รุ่นหลัง, และ tune รอบ ๆ model เพื่อจัดการ failure mode ของ vision + reasoning + verification. agent สามารถ cross-reference context จากหลายหน้าของเอกสาร และ ground value ใน source ที่ชัดเจน. นี่คือ pattern ที่เราเริ่มเห็นในตลาด extraction — vendor ทุกเจ้าหันมาเขียน harness แบบ coding agent (plan → execute → verify loop) แทน single-shot prompt ที่ใช้มา 2 ปี.

## ทำไมสำคัญ
Grounding ที่เพิ่มเท่าตัวแปลว่า **enterprise ใช้ Extract ได้ใน compliance workflow จริง**. ก่อนหน้านี้ที่ grounding ~46 ลูกค้าใน financial services, legal, healthcare ต้องมีคนรีวิวทุก extraction เพราะ bounding box อาจชี้ผิด — เท่ากับ "ลด manual work ครึ่งหนึ่ง" ไม่ใช่ "ยกเลิก manual review". ที่ **80+** compliance team สามารถเริ่ม sample audit แทน full review ซึ่งเป็น switch ของ ROI ทั้งหมด. บวกกับที่ **F1 ขึ้นแต่ราคาไม่ขึ้น** คือ pattern เดียวกับ frontier model layer — competition บีบให้ quality เพิ่มโดยไม่ขึ้นราคา และ winner คือ end user.

Market context สำคัญ: **Reducto, Unstructured.io, Mistral OCR** ทั้งหมดกำลัง compete ใน document extraction space และทุกเจ้ามี benchmark ของตัวเอง. LlamaIndex เลือกเผชิญหน้าโดย publish **ExtractBench** เป็น third-party benchmark ที่ reproducible — move นี้บีบคู่แข่งต้องตอบด้วย number เท่านั้น. ถ้า Reducto หรือ Mistral ตอบไม่ได้ภายใน 60 วัน, LlamaIndex จะยึด "default choice" ของ enterprise RAG infra ไปอีก 2-3 quarter.

## มุม AI Agent Platform
สำหรับ **Builders** ที่สร้าง RAG pipeline หรือ document AI product: ถ้า extraction layer ของคุณยังเป็น single-shot LLM call ให้ migrate ไป agent harness ตอนนี้ — Extract v2.5 แสดงให้เห็นว่า harness approach ชนะ single-shot ประมาณ 30+ point ใน grounding. สำหรับ **Users / business** ใน finance/legal/healthcare: Extract v2.5 เปลี่ยน economics ของ compliance document workflow — pilot ภายในเดือนนี้แล้ววัด audit sample rate ก่อน/หลัง. สำหรับ **Ecosystem**: Reducto, Mistral OCR, Unstructured.io ต้องปล่อย benchmark ตอบภายใน Q4; Databricks + Snowflake จะเริ่มสร้าง native integration กับ Extract เพื่อขาย data cloud + RAG รวมกัน; และ harness-first pattern จะกระจายจาก coding → extraction → ไปถึง search และ data engineering ภายใน 2 quarter.

## Sources
- [LlamaIndex Launches Extract V2.5 With Accuracy and Grounding Gains (Unite.AI)](https://www.unite.ai/llamaindex-launches-extract-v2-5-with-accuracy-and-grounding-gains/)
- [Introducing Extract v2.5 (LlamaIndex Blog)](https://www.llamaindex.ai/blog/introducing-extract-v2-5)
- [ExtractBench: The Most Comprehensive Extraction Benchmark (LlamaIndex)](https://www.llamaindex.ai/blog/introducing-extractbench)

---

## Audio script
วันที่ 1 ตุลาคม LlamaIndex ปล่อย Extract v2.5 — generation ใหม่ของ schema-based document extraction agent. ตัวเลขที่น่าสะดุดคือ grounding score บน ExtractBench — benchmark ที่วัดว่า agent cite กลับไปที่ bounding box ของต้นฉบับได้มั้ย. Agentic tier กระโดดจาก 46.8 ไป 80.6 และ Agentic Plus จาก 46.4 ไป 82.2 เกือบ 2 เท่า. Value F1 ก็ขึ้นทุก tier Cost Effective 87.1 ไป 93.9, Agentic 89.8 ไป 95.8, Agentic Plus 95.1 ไป 96.4 โดย per-page pricing ไม่ขึ้น. เบื้องหลัง LlamaIndex บอกว่า v2.5 รันบน agent harness ใหม่ที่ออกแบบมาเฉพาะ document extraction ได้แรงบันดาลใจจาก coding agent รุ่นหลัง ใช้ plan execute verify loop แทน single-shot prompt. ประเด็นสำคัญคือ grounding ที่เพิ่มเท่าตัวทำให้ compliance team ใน finance legal healthcare เปลี่ยนจาก full manual review เป็น sample audit ได้ — เปลี่ยน ROI ทั้งหมด. ถ้าคุณสร้าง RAG pipeline หรือ document AI และยังเป็น single-shot LLM call ให้ migrate ไป agent harness ตอนนี้ pattern นี้ชนะ single-shot กว่า 30 point ใน grounding ชัดเจน.
