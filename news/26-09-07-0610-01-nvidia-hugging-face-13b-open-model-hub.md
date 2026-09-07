---
date: 2026-09-07
slug: 26-09-07-0610-01-nvidia-hugging-face-13b-open-model-hub
topic: openbridge-trend
reading_time_min: 5
sources: 5
image_prompt: |
  A colossal green Nvidia hand gently cradling a small yellow-smiling Hugging Face
  emoji-icon that sits atop a glowing open book of AI models. Around them float
  translucent "$12.9B" price-tag and floating labels "18M developers", "3M models",
  "500K datasets". Editorial isometric illustration, warm rim light, moody teal-and-
  amber palette, deep composition depth, 1:1 aspect. Text elements crisp and legible
  at 200px thumbnail. No real human faces.
image: images/26-09-07-0610-01-nvidia-hugging-face-13b-open-model-hub.png
---

# Nvidia จ่าย $12.9B ซื้อ Hugging Face — chip company กลายเป็นเจ้าของ open-model hub ที่ agents ทุกตัวเดินผ่าน

## TL;DR
- Nvidia ประกาศ 3 ก.ย. — deal $12.9B (cash + equity retention $1B), Hugging Face จะยังเป็น open platform, ปิดดีลครึ่งแรก 2027
- Hugging Face = 18M developers, 3M models, 500K datasets, 1M apps, 200K companies ใช้ platform → กลายเป็น "distribution layer" ของ open-source AI ที่ agent ทุกตัวดึงโมเดลผ่าน
- signal: Nvidia ไม่ได้ซื้อบริษัท ซื้อ **choke point ของ open-source AI supply chain** — ตอนที่ closed API พ่ายแพ้เรื่อง cost, HF คือทางเลือกที่ทุกคนไป

## เกิดอะไรขึ้น
3 กันยายน 2026 — Nvidia กด SEC filing แจ้งเซ็น definitive agreement ซื้อ Hugging Face มูลค่าประมาณ $12.9B: cash $11.9B ให้ผู้ถือหุ้น + equity retention program $1B สำหรับพนักงาน HF ที่จะย้ายเข้า Nvidia. ปิดดีลครึ่งแรกปี 2027 หลังผ่าน regulator. Jensen Huang ยืนยันบน CNBC ว่า Clément Delangue (CEO HF) เป็นคนติดต่อ Nvidia เอง "หลายสัปดาห์" ก่อนดีลออก — ไม่ใช่ Nvidia hunt ลงมา.

ตัวเลข Hugging Face ที่ Nvidia ได้ pull ไปในดีลนี้ใหญ่กว่าที่คนส่วนใหญ่รับรู้: **18 ล้าน developers/researchers/creators active, 3 ล้านโมเดล share บน platform, 500,000 datasets, 1 ล้าน applications, 200,000 บริษัทใช้เพื่อ discover + deploy AI**. ที่สำคัญกว่านั้น — Hugging Face คือคนสร้าง `transformers` library ที่ทุก LLM framework บนโลกใช้ต่อ, `datasets` library, `accelerate`, `PEFT`, `TGI` (Text Generation Inference server), และ MCP servers อีกจำนวนมากที่ agent developer เอามาต่อกับ open-weight models.

Jensen framing เรื่องนี้ว่า "Hugging Face is the operating system of open-source AI." เขาย้ำว่า HF จะยังเป็น neutral open platform รองรับทุก accelerator (รวม TPU, Trainium, Groq, Cerebras) เพราะถ้าปิดจะทำลาย network effect. แต่ตลาดตีความอีกทิศ: **AMD, Intel, Google, AWS ตอนนี้ต้องพึ่ง open-model distribution layer ที่ competitor ตัวเอกเป็นเจ้าของ**.

ปฏิกิริยา 48 ชั่วโมงแรกน่าสนใจ — ราคาหุ้น Nvidia บวก 1.4% ตอนประกาศ (ตลาดชอบ), Databricks CEO Ali Ghodsi twitter ว่า "the open ecosystem needs an independent hub" (แปลว่า concern), OpenRouter (routing layer) เห็น traffic เพิ่ม 12% วันประกาศ (คนเผื่อทาง). ที่เงียบผิดปกติคือ Meta และ Mistral — สองผู้ปล่อย open-weight ใหญ่สุด — ยังไม่มี statement ออกมา 3 วันหลังดีล.

## ทำไมสำคัญ
Deal นี้ไม่ใช่แค่ AI M&A ปกติ — เป็น **strategic control ของ AI supply chain layer** ที่ agent economy พึ่งทั้งหมด. เมื่อ enterprise ปฏิเสธ closed API เพราะ pricing / privacy / latency แล้วหันไป open-weight (Llama, Qwen, Mistral, DeepSeek) — เกือบทุกทีมโหลดผ่าน HF Hub. Nvidia รู้ว่า agentic AI ทำให้ **model calls ต่อ workflow ทวีคูณ 10-50 เท่า** ของ chatbot ยุคแรก — และคนไม่ยอมจ่าย API rate ต่อ token ทั้งหมด. HF Hub คือทางออกของ enterprise ที่ Nvidia ต้อง lock เข้าตัวเอง.

เทียบกับดีลที่คล้ายกัน: Microsoft ซื้อ GitHub 2018 ($7.5B) แล้วใช้เป็นฐาน Copilot ecosystem. ตอนนั้นคนกลัวว่า Microsoft จะทำลาย GitHub — แต่ผ่านไป 7 ปี GitHub โต 3× และกลายเป็น distribution layer ของ AI coding. Nvidia + HF น่าจะเดิน pattern คล้ายกัน แต่เดิมพันสูงกว่า 2× เพราะ open-model layer สำคัญต่อ agent economy กว่า code hosting ต่อ coding tools ยุค 2018.

Second-order effect: **Google (TPU) และ AWS (Trainium) ต้องรีบสร้าง / ซื้อ neutral model hub ของตัวเอง** ภายใน 12 เดือน — ไม่งั้นทุก enterprise AI workflow ที่ลง HF จะ default ไป Nvidia stack. Google เคยลอง Kaggle + Vertex AI Model Garden แต่ community share ยังห่างชั้น HF สิบเท่า. AWS มี SageMaker JumpStart — ยิ่งห่าง. ปีหน้าคาดจะเห็น Google offer ซื้อ Replicate หรือ Modal, และ AWS อาจ offer Together.ai หรือ Fireworks.

## มุม AI Agent Platform
สำหรับ **builders** — ทีมสร้าง agent framework (LangChain, CrewAI, LlamaIndex, Vercel AI SDK) ที่ default download model ผ่าน HF Hub ต้องเริ่มคิด abstraction layer เผื่อวันที่ HF ให้ preferential treatment กับ CUDA models. Multi-hub routing (HF + Replicate + Modal + Fireworks) จะเป็น table stakes ภายใน Q2 2027.

สำหรับ **users / business** — ทีมที่ deploy agent บน open-weight (เช่น Llama 4, Qwen 3, Mistral Large 3) ควร audit dependency ตอนนี้: กี่ % ของ agent workflow ที่ต้อง pull weight/tokenizer/dataset จาก HF? มี fallback registry หรือยัง? ถ้าใช้ HF Inference Endpoints เป็น production — เตรียม migration playbook เผื่อ Nvidia ปรับ pricing / SLA หลังปิดดีล.

สำหรับ **ecosystem** — MCP server marketplace บน HF Hub (มีประมาณ 400+ ตอนนี้) เป็น jewel ที่ Nvidia ได้ฟรี. ถ้า Nvidia integrate MCP hub เข้า NIM / NeMo Agent Toolkit จะกลายเป็น **default agent runtime stack ของ enterprise** ที่ยากจะ compete. Anthropic (เจ้าของ protocol MCP) อาจต้องเร่งเปิด MCP registry official ของตัวเองภายใน 6 เดือน เพื่อไม่ให้ HF/Nvidia กลายเป็น sole distributor. Startup ไทยที่กำลังคิดสร้าง agent framework บน open-weight — เริ่มออกแบบ dependency injection ให้ swap hub ได้ตั้งแต่วันนี้.

## Sources
- [Nvidia Confirms $13 Billion Acquisition of Open-Weight AI Platform Hugging Face — Yahoo Finance](https://finance.yahoo.com/markets/article/nvidia-confirms-13-billion-acquisition-of-open-weight-ai-platform-hugging-face-141058641.html)
- [NVIDIA to Acquire Hugging Face — NVIDIA Blog](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/)
- [Hugging Face approached Nvidia's Huang weeks ahead of $12.9B acquisition — CNBC](https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html)
- [Nvidia Is Acquiring Hugging Face For Almost $13 Billion — Forbes](https://www.forbes.com/sites/zacharyfolk/2026/09/03/nvidia-is-acquiring-hugging-face-for-almost-13-billion/)
- [Nvidia 8-K SEC filing 2026-09-02](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000078/nvda-20260902.htm)

---

## Audio script
ข่าวใหญ่สุดของสัปดาห์นี้คือ Nvidia จ่าย 12.9 พันล้านดอลลาร์ซื้อ Hugging Face ครับ. Hugging Face ที่เราคุ้นชื่อว่าเป็นเว็บโหลดโมเดล open source มีคน active 18 ล้าน developer, มีโมเดลแชร์บนแพลตฟอร์มถึง 3 ล้านตัว, และ 200,000 บริษัทใช้มัน deploy AI. Jensen Huang บอกว่า Hugging Face จะยังเป็น open platform ที่รองรับทุก chip แต่ตลาดตีความอีกทาง — AMD, Google, AWS ตอนนี้ต้องพึ่ง distribution layer ที่ competitor ตัวเก่งเป็นเจ้าของ. เดิมพันจริง ๆ ของดีลนี้คือ agent economy — เพราะ agent เรียก model 10 ถึง 50 เท่าของ chatbot รุ่นแรก และ enterprise ปฏิเสธ closed API แล้วหันไป open weight ผ่าน Hugging Face Hub. Nvidia ไม่ได้ซื้อบริษัท เขาซื้อ choke point ของ AI supply chain. ทีมที่สร้าง agent บน open weight ควร audit dependency ตอนนี้ เพราะภายใน 6-12 เดือนอาจต้องมี multi-hub routing เป็น table stakes. คนที่ต้องเร่งตอบโต้คือ Anthropic — เจ้าของ protocol MCP — ต้องเปิด MCP registry ของตัวเองเร็ว ไม่งั้น Hugging Face plus Nvidia จะกลายเป็น default agent runtime ของ enterprise ทั้งอุตสาหกรรม. ปิดดีลกลางปีหน้า แต่ ripple effect เริ่มแล้ววันนี้ครับ.
