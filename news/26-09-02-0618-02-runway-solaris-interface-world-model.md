---
date: 2026-09-02
slug: runway-solaris-interface-world-model
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  A cinematic split composition: on the left a wireframe of a
  traditional coded UI with rigid rectangles and code lines "div, css, js";
  on the right a fluid, painterly interface that morphs mid-frame — a
  cursor mid-click leaves a glowing trail as buttons and panels
  materialize into being like a video frame being generated. A big label
  above reads "NO CODE. JUST FRAMES." A subtitle underneath: "GEN-4.5 + LLM".
  Editorial magazine style, futuristic teal and magenta palette, ultra-high
  contrast for legibility at 200px thumbnail. No real human faces,
  silhouette OK. 1:1 aspect.
image: images/26-09-02-0618-02-runway-solaris-interface-world-model.png
---

# Runway Solaris — "Interface World Model" ที่ generate UI ทีละ frame แบบ real-time, ทำลาย paradigm coded interface

## TL;DR
- **Runway** ประกาศ **31 ส.ค. 2026** เปิด **Solaris** — model แรกในตระกูล **"Interface World Models"** — generate software UI ทีละ frame real-time ไม่ใช้ code
- **Architecture**: Gen-4.5 video model + LLM ที่อ่าน click/drag แล้ว prompt frame ถัดไป
- **Status**: early-access research — ยังไม่มี public API, ยังไม่มี pricing, รับ request ผ่าน form
- **Signal**: ถ้า scale ได้ — เปลี่ยน software จาก **written thing** เป็น **generated stream** เหมือน video

## เกิดอะไรขึ้น

Runway — บริษัท video generation ที่คนรู้จักจาก Gen-3 / Gen-4 — ประกาศ **31 สิงหาคม 2026** ปล่อย **Solaris**. Solaris ไม่ใช่ video model, ไม่ใช่ code generator, ไม่ใช่ chatbot. มันคือสิ่งใหม่ที่ Runway เรียก **"Interface World Model"** — model ที่ **generate UI ของ software ทีละ frame** real-time ตอนที่คุณคลิก ลาก กด keyboard

Architecture ที่ประกาศ: Gen-4.5 video foundation model + LLM layer. LLM อ่าน input event (click ตำแหน่งไหน, drag ทิศไหน, กด key อะไร), decide ว่า UI ควรตอบสนองยังไง, แล้ว prompt Gen-4.5 ให้ synthesize frame ถัดไป. ไม่มี HTML, ไม่มี CSS, ไม่มี React, ไม่มี state manager — ทุก pixel เกิดจาก model predict. Runway โชว์ demo: user คลิกปุ่มที่ไม่มีอยู่ในหน้าจอก่อนหน้า → Solaris generate popup, animation, form ให้ทันที เหมือน software ที่ "จินตนาการเอง"

**แต่ยังไม่ shipped**. Runway บอกชัด: Solaris เป็น **early-access research project** — ไม่มี GA, ไม่มี API, ไม่มี open weight, ไม่มี pricing. เก็บ request ผ่าน waitlist form + "working with key partners to launch publicly." The Decoder รายงานว่าตอน demo ยังมี artifact เยอะ (icon เพี้ยน, text ไม่ consistent, layout กระตุก) แบบเดียวกับ video model ยุคแรก

Runway founder Cristóbal Valenzuela เขียนใน blog ว่าเป้าหมาย long-term คือ **"software ที่ generate ได้เหมือน video"** — 10-15 ปีข้างหน้า UI จะไม่ใช่ artifact ที่ dev เขียน แต่เป็น artifact ที่ model synthesize on-demand ตาม intent ของ user แต่ละคน

## ทำไมสำคัญ

Solaris ยัง janky แค่ไหน POV ของ Runway ก็ *เปิดคำถามใหม่* ที่ agent industry ต้องตอบ:

**ถ้า UI ไม่ใช่ code — agent จะ interact กับมันยังไง?** ตอนนี้ browser agent (Claude in Chrome, Operator, Comet, Hatch) พึ่ง DOM structure — HTML, ARIA label, click coord — เพื่อรู้ว่าจะ interact กับปุ่มไหน. ถ้า UI ถูก generate ทีละ frame ไม่มี DOM = agent ต้อง see-and-act เหมือน human ใช้ vision model. **Anthropic computer use + OpenAI Operator** ที่ใช้ screenshot-based grounding เตรียมพร้อมกว่า text-based agent แน่นอน

**Vibe coding vs vibe software.** Vibe coding (Cursor, Windsurf, Claude Code) generate **code** ที่ compile เป็น software. Solaris generate **software** โดยไม่ผ่านชั้น code. ถ้า approach นี้ scale — market ของ code-gen tool จะ compress อย่างรวดเร็ว. แต่ที่จริง 2 approach นี้อาจ complementary — Solaris สำหรับ prototype + throwaway UI (report, dashboard ครั้งเดียว), code-gen สำหรับ persistent product

**Cost economics ยังไม่ผ่าน.** Video frame generation กิน GPU มหาศาล — 24 fps × 1080p × session หนึ่งชั่วโมง = compute cost ที่แพงกว่า render React หน้าเดิม 1000-10,000 เท่า. Solaris จะเป็น consumer product ได้ต่อเมื่อ inference cost ลง 100-1000 เท่า (ที่ DeepSeek V4 + Cerebras + Groq กำลังไล่). ในระหว่างนี้ Solaris จะอยู่ในโหมด demo / research — ยังไม่ใช่ threat กับ codebase ใครในปี 2026-2027

**Precedent.** Runway ใช้ playbook เดียวกับ Gen-1: launch เป็น research → 12 เดือน จน quality พอใช้ → 24 เดือน จน production-ready. ถ้าใช้ timeline เดียวกัน — Solaris production-grade จะเป็น **ปลาย 2028 - ต้น 2029**

## มุม AI Agent Platform

**Builders**: 2 implication ที่ต้องคิด. (1) ถ้า agent framework ของคุณพึ่ง DOM-parsing / text-selectors ล้วน — เตรียม **vision-based grounding** เป็น first-class citizen ตั้งแต่ตอนนี้. Anthropic computer_toolset_20260801 + OpenAI Operator SDK เดินหน้าเรื่องนี้ไปก่อนหน้าเยอะ. (2) เริ่มคิดเรื่อง **"agent-to-agent UI"** — ถ้า Solaris generate UI ตาม intent, agent อีกตัวจะ negotiate intent กับ Solaris ยังไงโดยไม่ผ่าน screen? MCP + A2A protocol อาจต้องเพิ่ม intent-schema layer

**Users / businesses**: บริษัทที่ทำ enterprise app ยังปลอดภัย 3-5 ปี — Solaris ไม่ replace ERP / CRM / accounting ในเร็ววัน. แต่ **frontend team ที่ทำ marketing microsite, campaign landing, one-off dashboard** จะเจอ competition จาก Solaris-style tool ใน 12-18 เดือน. เริ่ม pivot เข้า **design system + component library** ที่ agent (ทั้ง Solaris-style และ Vercel v0 / Claude artifact-style) consume ได้เป็น service

**Ecosystem**: OpenAI, Google, Anthropic ยังไม่มี "Interface World Model" — ทุกเจ้า focus ที่ code-gen + agent action. ถ้า Solaris พิสูจน์ว่า approach ใช้งานได้จริง — Google (Gemini + Veo) กับ OpenAI (Sora + GPT-5.6) มี asset ทำได้ทันที. Runway มี window แคบ — 12-18 เดือนก่อน hyperscaler ตามทัน

## Sources
- [Runway News: Introducing Solaris (Runway)](https://runway.com/news/research/introducing-solaris)
- [Runway's Solaris is an AI system that generates software interfaces in real time (The Decoder)](https://the-decoder.com/runways-solaris-is-an-ai-system-that-generates-software-interfaces-in-real-time/)
- [Runway's Solaris previews the no-code internet (The Rundown AI)](https://www.therundown.ai/articles/runway-solaris-previews-the-no-code-internet)
- [Runway Solaris: AI-Generated Interfaces, Frame by Frame (Neuron Daily)](https://www.theneurondaily.com/p/runway-solaris-treats-software-like-video)

---

## Audio script
เรื่องที่สองน่าสนใจมาก. Runway บริษัท video generation ประกาศเมื่อวันที่ 31 สิงหาคม เปิด Solaris — model แรกในตระกูลที่เขาตั้งชื่อว่า Interface World Model. Solaris ไม่เขียน code, ไม่ compile React, ไม่มี HTML — มัน generate UI ของ software ทีละ frame เหมือน video ตอนที่คุณคลิก ลาก กดปุ่ม. Architecture คือ Gen-4.5 video model บวก LLM ที่อ่าน input แล้ว prompt frame ถัดไปให้ synthesize ทันที. Runway โชว์ demo ว่า user คลิกปุ่มที่ไม่มีอยู่ในหน้าจอก่อนหน้า Solaris ก็ generate popup ให้ทันทีเหมือน software จินตนาการเอง. ยังเป็น early access research ไม่มี API ไม่มี pricing ยัง janky อยู่ แต่ POV ของ Runway เปิดคำถามใหม่ให้ agent industry — ถ้า UI ไม่ใช่ code แล้ว agent จะ interact ยังไง? Browser agent ที่พึ่ง DOM แบบ Comet Operator Hatch เจอปัญหาแน่ — vision based grounding อย่าง Anthropic computer use และ OpenAI Operator เตรียมพร้อมกว่า. Cost ยังแพงกว่า render UI ปกติ 1000 ถึง 10000 เท่า ยังไม่ใช่ threat กับใครเร็วนี้ แต่ถ้า Runway ใช้ timeline เดียวกับ Gen-1 — production ready ปลาย 2028 ต้น 2029. สำหรับ team frontend ที่ทำ landing page campaign หรือ dashboard ครั้งเดียว เตรียม pivot เข้า design system ที่ agent consume ได้ตั้งแต่ตอนนี้ครับ
