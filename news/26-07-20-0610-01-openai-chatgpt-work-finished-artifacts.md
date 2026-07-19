---
date: 2026-07-20
slug: openai-chatgpt-work-finished-artifacts
topic: agentic-ai
reading_time_min: 3
sources: 4
image_prompt: |
  A minimalist editorial illustration of an office desk cut in half by a glowing
  diagonal line. On the left: a person's silhouette typing scattered sticky notes
  labeled "IDEAS", "DRAFTS", "NOTES". On the right: a stack of finished documents
  emerging autonomously — a titled Word doc, a spreadsheet with numbers, a slide
  deck labeled "Q3 REPORT". A large three-word phrase floats above: "FROM NOTES
  TO WORK". The OpenAI black spiral logo sits in the top-left corner. Editorial
  isometric style, sharp typography, high contrast, cream background, 1:1 aspect,
  no real human faces.
image: images/26-07-20-0610-01-openai-chatgpt-work-finished-artifacts.png
---

# ChatGPT Work: OpenAI ปิด gap ระหว่าง "AI ตอบคำถาม" กับ "AI ทำงานให้เสร็จ"

## TL;DR
- OpenAI ปล่อย ChatGPT Work + desktop app update ตัวใหม่ 18 ก.ค. — agent ที่ทำงานยาวข้าม app ได้ (doc, sheet, deck, Sites) โดย powered ด้วย GPT-5.6
- GPT-5.6 มาเป็นครอบครัว 3 ตัว: Sol ($5/$30 per M tokens), Terra ($2.50/$15), Luna ($1/$6) — Sol เป็น workhorse สำหรับ coding + agentic workflow
- Signal ที่ใหญ่กว่า pricing: ChatGPT ย้ายจาก "ตอบคำถาม" ไปสู่ "ส่งงานสำเร็จรูป" — เป็นการเปลี่ยน UX contract ของ AI product platform ทั้งหมด

## เกิดอะไรขึ้น
วันที่ 18 กรกฎาคม 2026, OpenAI ปล่อย desktop app experience update สำหรับ ChatGPT Business ที่ทำให้ user สลับระหว่าง Chat และ Work ได้ในหน้าเดียว, ค้น conversation + Projects เก่าได้ง่ายขึ้น, และ continue งาน Work ข้าม web / mobile / desktop บน macOS และ Windows. Update นี้เป็น rollout ต่อจากการเปิดตัว ChatGPT Work และครอบครัว GPT-5.6 เมื่อ 9 กรกฎาคม.

ChatGPT Work คือ agent สำหรับงานยาวและซับซ้อน — ไม่ใช่แค่ตอบคำถาม แต่ค้น context จาก app ที่เชื่อมต่อ, ดึงไฟล์, และสร้าง output จริง: Word document, spreadsheet, presentation, report, กระทั่ง Sites. Powered ด้วย GPT-5.6 Sol (top tier), Terra (balanced), หรือ Luna (cheap) — Sol ถูกวางเป็น "workhorse" สำหรับ complex reasoning, coding, agentic workflow. OpenAI positioning เจาะจงว่า Sol เป็น "best coding model yet" และ "strongest cybersecurity model yet".

Pricing ก็มีความหมาย: Sol ที่ $5 input / $30 output per million tokens เทียบกับ Claude Opus 4.8 ($5/$25) ใกล้เคียง, แต่ Terra ($2.50/$15) ตัดราคาลงไปเกือบครึ่ง, และ Luna ($1/$6) เข้าโซน commodity — ในสัปดาห์เดียวกัน xAI ก็ปล่อย Grok 4.5 ที่ $2/$6 มายัน. ราคา output token flagship-class ตอนนี้อยู่ที่ $4-6 range เทียบกับ $25-50 ของ legacy flagship เมื่อปีที่แล้ว.

## ทำไมสำคัญ
ประเด็นใหญ่ไม่ใช่ pricing — ที่สำคัญกว่าคือ **UX contract ของ AI product ย้ายเสาแล้ว**. ตั้งแต่ ChatGPT เปิดตัวปลายปี 2022, contract คือ "user ถาม, AI ตอบ" — output เป็น text ที่ user ต้อง copy-paste แล้วเอาไปทำงานต่อ. ChatGPT Work เขียน contract ใหม่: "user บอกงาน, AI ส่งของ" — output เป็น artifact ที่ user เปิดใน Word / Excel / PowerPoint ได้เลย. นี่คือความเปลี่ยนแปลงเดียวกับที่ Sierra AI เจอในฝั่ง customer support — จาก "seat" (คนใช้ software) ไปสู่ "outcome" (งานที่เสร็จ).

Pattern ที่เห็นทั่วอุตสาหกรรม: Sierra ประกาศ $200M ARR ต้นปีนี้ ที่ valuation $15.8B, ตอนนี้ voice agent overtake text แล้ว, ให้บริการ 40%+ ของ Fortune 50 — ทั้งหมดขายเป็น "งานที่เสร็จ" ไม่ใช่ "seat". Vertical agent เช่น Harvey (legal), Hippocratic (healthcare), EvenUp (personal injury) ทำแบบเดียวกัน. ChatGPT Work คือ OpenAI move เข้าสู่ horizontal outcome — ทำงาน office ใน Microsoft 365 / Google Workspace แทนที่จะเป็น seat product.

## มุม AI Agent Platform
สำหรับ **builders** ที่กำลังสร้าง agent framework หรือ orchestration layer: UX contract "artifact-in-artifact-out" จะกลายเป็น baseline expectation. ถ้า agent ของคุณยังส่ง markdown ตอบกลับใน chat, คุณจะแพ้ agent ที่ส่ง .xlsx / .pptx / .docx ผ่าน connector ตรง. Runtime ต้องรองรับ long-running task (นาที-ชั่วโมง) และ file I/O ผ่าน MCP หรือ SDK สำเร็จรูป — AWS Bedrock AgentCore ขยาย runtime session quota เป็น 5,000 sessions/account และ Google Gemini Enterprise Agent Platform ให้ 7-day long-running ops ก็เพราะเห็น pattern เดียวกัน.

สำหรับ **users / business**: seat-based procurement ของ SaaS จะเริ่มไม่ fit — ถ้า Legal ใช้ Harvey ทำงานให้เสร็จ, Finance ใช้ ChatGPT Work ปิดรายงาน, CX ใช้ Sierra จบ ticket — สิ่งที่ CFO จะต้อง track คือ "งานที่เสร็จต่อ dollar" ไม่ใช่ "license per head". Vendor lock-in ย้ายจาก data ไป workflow — ตัว agent เข้าถึงระบบ SAP / Salesforce / Google Drive ผ่าน MCP ก็จะกลายเป็น critical infrastructure ยาก swap. สำหรับ **ecosystem**: MCP spec 2026-07-28 ที่กำลังจะ ship (RC ประกาศเมื่อวันก่อน) จะยิ่งเร่ง pattern นี้เพราะ authorization กับ tool discovery จะ standardize.

## Sources
- [OpenAI: Introducing ChatGPT agent (context)](https://openai.com/index/introducing-chatgpt-agent/)
- [OpenAI launches GPT-5.6 family](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [GPT-5.6 Wikipedia entry](https://en.wikipedia.org/wiki/GPT-5.6)
- [OpenAI Release Notes July 2026](https://releasebot.io/updates/openai)

---

## Audio script
วันนี้เรามีข่าวใหญ่จาก OpenAI ครับ 18 กรกฎาที่ผ่านมา เขาปล่อย desktop app update สำหรับ ChatGPT Business ที่ทำให้ user สลับ Chat กับ Work ได้ในหน้าเดียว ต่อยอดจากการเปิดตัว ChatGPT Work และครอบครัว GPT-5.6 เมื่อ 9 กรกฎา สิ่งที่น่าสนใจคือ ChatGPT Work ไม่ใช่แค่ chatbot ตอบคำถามอีกแล้ว มันเป็น agent ที่ค้น context จาก app ที่เชื่อม ดึงไฟล์ แล้วส่งงานสำเร็จรูปกลับมา ทั้ง Word document ทั้ง spreadsheet ทั้ง presentation ทั้ง report ทั้ง Sites ตัวเลขที่ต้องรู้ครับ GPT-5.6 มาเป็นสามตัว Sol เป็น flagship ราคา 5 ดอลลาร์ input 30 ดอลลาร์ output ต่อล้าน token, Terra ราคาครึ่งเดียว, Luna ราคา 1 กับ 6 ดอลลาร์ Sol ถูกวางเป็น workhorse สำหรับ coding และ agentic workflow ทำไมสำคัญ ผมมองว่าเป็นการเปลี่ยน UX contract ของ AI product เลยครับ จากเดิม user ถาม AI ตอบ ตอนนี้กลายเป็น user บอกงาน AI ส่งของ pattern เดียวกับ Sierra ที่ ARR ทะลุ 200 ล้าน หรือ Harvey ในฝั่ง legal ทั้งหมดขายเป็น outcome ไม่ใช่ seat สำหรับคนสร้าง agent framework ต้องเริ่มคิดว่า runtime รองรับ long-running task ยังไง file I/O ผ่าน MCP ยังไง เพราะ artifact-in artifact-out จะกลายเป็น baseline คิดดูครับว่าถ้า Legal ใช้ Harvey Finance ใช้ ChatGPT Work CX ใช้ Sierra สิ่งที่ CFO track จะเปลี่ยนจาก license per head ไปเป็นงานที่เสร็จต่อ dollar ครับ
