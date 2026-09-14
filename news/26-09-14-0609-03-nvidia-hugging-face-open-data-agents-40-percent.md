---
date: 2026-09-14
slug: nvidia-hugging-face-open-data-agents-40-percent
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A crisp editorial illustration of a giant open crate labeled "OPEN DATA FOR
  AGENTS" spilling out glowing lines of code paths and task trajectories, each
  branching like tree roots. Three large numbers stack above the crate:
  "50,000+ TASK TRAJECTORIES", "40% BENCHMARK LIFT", "SWE + ROBOTICS". A small
  green NVIDIA logo and a yellow Hugging Face emoji sit at opposite corners.
  Deep charcoal background with lime accents, editorial isometric style, sharp
  typography sized for 200 pixel thumbnail, 1:1 aspect, no real human faces.
image: images/26-09-14-0609-03-nvidia-hugging-face-open-data-agents-40-percent.png
---

# NVIDIA + Hugging Face เปิด Open Data for Agents — 50,000 task trajectories, benchmark +40%

## TL;DR
- 13 กันยา NVIDIA + Hugging Face release **Open Data for Agents** — curated dataset ของ agent task trajectories สำหรับ post-training และ RL
- ประกอบด้วยชุดใหญ่ ๆ เช่น **Open-SWE-Traces** (200k+ software engineering trajectories) และ **robotics trajectories 500K+** พร้อม 15TB multimodal data
- Benchmark performance ของ agent ที่ fine-tune บน dataset นี้ +40% เทียบ baseline — dataset gap เคยเป็น bottleneck ใหญ่ของ agent quality

## เกิดอะไรขึ้น

NVIDIA กับ Hugging Face ปล่อย Open Data for Agents ในสัปดาห์ที่ NVIDIA ยังอยู่กลาง process ซื้อ Hugging Face ($13B, ประกาศ 2 กันยา, ปิด H1 2027). Dataset ชุดนี้ประกอบด้วยหลายชิ้นใหญ่: **Open-SWE-Traces** 200k+ agent trajectories ที่เก็บผ่าน SWE-agent + OpenHands framework — เห็น agent ที่พยายามแก้ code จริง มี tool call, มี error, มี retry, มี success/failure signal ครบ. **NVIDIA GR00T dataset** 500K+ robotics trajectories, 57M grasps, 15TB multimodal — สำหรับ vision-language-action model.

จุดที่ต้องดู ไม่ใช่ตัวเลข dataset size แต่คือ shift ของ training paradigm. หนึ่งปีที่ผ่านมา frontier lab พูดถึง "RL on agent trajectories" เยอะมาก แต่ dataset ที่เปิดจริงยังน้อย — ส่วนใหญ่เป็น proprietary. Anthropic, OpenAI, Google ต่างเก็บ trajectory data ของตัวเอง (จาก Claude Code, GitHub Copilot, Gemini CLI) แล้ว fine-tune วนไปเรื่อย. Startup / open source lab ทำแบบเดียวกันไม่ได้เพราะ no scale. Open Data for Agents คือ NVIDIA ยัด scale เข้าไปในตลาดโดยตรง.

## ทำไมสำคัญ

Agent quality gap ระหว่าง frontier lab กับ open source ในช่วงหลังไม่ได้อยู่ที่ model architecture — Qwen, DeepSeek, Kimi ตามทันหมด. อยู่ที่ trajectory data — signal ว่า agent ควรทำอะไรเมื่อเจอ error 500 จาก API, ควร retry อย่างไร, ควรเรียก tool ไหนถัดไป. Trajectory ที่ดีคือ ทฤษฎีคุณค่าใน RL loop สำหรับ agent — pattern matching อย่างเดียวไม่พอ, ต้องมี state-action-reward tuple จริง.

Signal สำคัญ: NVIDIA ตำแหน่งตัวเองไม่ใช่แค่ chip vendor. Chip → CUDA → framework → model → **data**. NVIDIA เดินขึ้น stack ครบทุกชั้น. การเปิด data เป็น open weights + open training corpus ยัง reinforce mission ที่ Jensen พูดในทุก keynote — "make every developer an AI developer". สำหรับ open source ecosystem: Meta AI, Mistral, Together, Fireworks จะเห็น benefit ทันทีจาก dataset ที่ curated แล้ว.

Caveat ที่ควรจำ: "40% benchmark lift" ที่รายงาน เป็นตัวเลขบนชุด benchmark ที่ NVIDIA เลือกเอง. ต้องรอ third-party (Princeton SWE-bench team, LMSYS) verify ว่ามัน generalize.

## มุม AI Agent Platform

**Builders** — startup ที่ทำ agent เฉพาะทาง (coding, browser, sales, ops) ตอนนี้มี base dataset ให้ post-train เอง โดยไม่ต้องพึ่ง OpenAI/Anthropic API เท่านั้น. อุตสาหกรรม "vertical fine-tune agent" (RunLLM, Cognition, Cursor) ได้เครื่องมือใหม่. **Users / business** — องค์กรใหญ่ที่ต้องการ agent ที่ deploy on-prem หรือ private cloud มี option ที่ไม่ต้องพึ่ง frontier lab. Bank, healthcare, defense ที่จำกัด data egress ได้ upside โดยตรง. **Ecosystem** — LangGraph, LlamaIndex, Mastra, Google ADK จะเริ่ม ship "recipe" ที่ integrate dataset นี้เข้า workflow ของ user. เห็น trend "framework + open dataset + open weights = production agent" ชัดขึ้น.

สำหรับทีมไทย — บริษัทที่คิดว่า AI agent = ต้องซื้อ Claude/GPT API เท่านั้น พลาด option ใหม่. Open weight agent ที่ fine-tune บน task-specific trajectory data + host เอง อยู่ในระยะเอื้อมของทีม engineer 5-10 คน. Cost economics ต่างจากปีก่อนมาก.

## Sources
- [Data for Agents | Hugging Face Blog](https://huggingface.co/blog/nvidia/open-data-for-agents)
- [nvidia/Open-SWE-Traces · Datasets at Hugging Face](https://huggingface.co/datasets/nvidia/Open-SWE-Traces)
- [NVIDIA Unveils New Open Models, Data and Tools to Advance AI Across Every Industry](https://blogs.nvidia.com/blog/open-models-data-tools-accelerate-ai/)

---

## Audio script
วันนี้มีอีกข่าวใหญ่จาก NVIDIA และ Hugging Face — เพิ่งเปิด Open Data for Agents ชุด curated dataset สำหรับ post-training และ RL ให้ AI agent ทำงานได้ดีขึ้น. ประกอบด้วย Open-SWE-Traces 200,000 กว่า trajectory ของ agent ที่พยายามแก้ code ผ่าน SWE-agent และ OpenHands framework — เห็น agent เจอ error retry สำเร็จหรือไม่สำเร็จ ครบทุก step. รวมถึง robotics dataset 500,000 trajectory กับข้อมูล multimodal อีก 15 TB สำหรับ vision-language-action model. Benchmark ที่ NVIDIA รายงานบอกว่า agent ที่ fine-tune บน dataset นี้ perform ดีขึ้น 40% เทียบ baseline. ทำไมสำคัญ? ปีที่ผ่านมา agent quality gap ระหว่าง frontier lab กับ open source ไม่ได้อยู่ที่ model architecture แล้ว — Qwen DeepSeek Kimi ตามทันหมด — อยู่ที่ trajectory data. Frontier lab เก็บ signal ของตัวเองจาก Claude Code Copilot Gemini CLI แล้ว fine-tune วนไปเรื่อย ทำให้ open source ตามไม่ทัน. Open Data for Agents คือ NVIDIA ยัด scale เข้าไปในตลาดโดยตรง. สำหรับ builder — startup ที่ทำ agent เฉพาะทางมี base dataset ให้ post-train เอง. สำหรับธุรกิจในไทย — คนที่คิดว่า AI agent ต้องซื้อ API เท่านั้น พลาด option ใหม่ครับ. Open weight agent ที่ fine-tune บน trajectory data แล้ว host เอง อยู่ในระยะเอื้อมของทีมเล็ก ๆ 5 ถึง 10 คน. Economics เปลี่ยนไปจากปีที่แล้วเยอะ.
