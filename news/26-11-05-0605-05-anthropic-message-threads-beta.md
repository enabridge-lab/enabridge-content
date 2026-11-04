---
date: 2026-11-02
slug: anthropic-message-threads-beta
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a sleek data-center corridor with
  two queues leading into "ANTHROPIC MESSAGES API". Queue A is piled high
  with thick paper rolls labeled "800 KB FULL HISTORY" every turn. Queue B
  holds a single small envelope labeled "1.8 KB NEW MESSAGE + THREAD ID"
  with a glowing fast lane. A big status board above reads
  "MESSAGE THREADS BETA", "-35% MEDIAN TTFT @ 500K-1M TOKENS", "5-MIN TTL".
  Deep indigo and amber palette, 1:1 aspect, high contrast for 200px
  thumbnails, no real human faces.
image: images/26-11-05-0605-05-anthropic-message-threads-beta.png
---

# Anthropic ปล่อย Message Threads beta — ตัดภาระ agent ส่ง conversation ซ้ำทุกเทิร์น แต่ token cost เท่าเดิม

## TL;DR
- 2 พ.ย. 2026 Anthropic ปล่อย **Message Threads** public beta บน Messages API — เปิดด้วย header `message-threads-2026-08-12` + field `thread`
- Agent ส่ง conversation เต็ม **ครั้งเดียว** — รอบถัดไปส่งแค่ **new message + previous response ID** — Anthropic reconstruct state ฝั่ง server
- **TTFT ลด ~35% ใน request ขนาด 500k–1M token** — Claude Code เปิด default แล้ว, เพิ่ม on AWS Bedrock + Azure Foundry + Google Cloud Vertex ด้วย
- **Token usage ไม่ลด** — Claude ยัง read conversation เต็มทุก turn ใน model execution; ประหยัดแค่ network + input processing
- **TTL 5 นาที** — thread encrypted in memory, ไม่ลงดิสก์, ไม่เข้า zero data retention / HIPAA — production client ต้องเก็บ canonical history เอง
- สิ่งที่ยังไม่ชัด: GA date, roadmap ของ long-lived session (> 5 นาที), rate limit ของ thread concurrent

## เกิดอะไรขึ้น

2 พ.ย. 2026 Anthropic ปล่อย **Message Threads** เข้า public beta บน Messages API. ก่อนหน้านี้ feature นี้อยู่ใน closed beta กับ Claude Code และ selected enterprise ไม่กี่ราย (ตั้งแต่ ส.ค. — เห็นได้จาก header date 2026-08-12). ตอนนี้เปิดให้ developer ทุกคนใช้ได้ด้วย beta header ง่ายๆ: `anthropic-beta: message-threads-2026-08-12` + ส่ง field `thread: { id: ..., previous_response_id: ... }` ไปใน request

Mechanic: agent loop ปกติต้องส่ง array `messages` ทั้งหมดใน request ทุก turn — รวม system prompt + user + assistant turns + tool results + new input. ที่ Anthropic ประเมิน request size agent ขนาดกลางอยู่ที่ **~800 KB ต่อ request**. ด้วย Message Threads, developer ส่ง conversation เต็ม **ครั้งเดียว** (ครั้งแรกของ thread) — turn ถัดไปส่งแค่ **new message + thread ID + previous response ID**. **Anthropic เก็บ state** ของ thread ฝั่ง server (encrypted in memory, ไม่ persist to disk) และ reconstruct full conversation ให้ model ตอน inference

Impact: **median TTFT (time-to-first-token) ลดลง ~35%** สำหรับ request ขนาด 500k–1M token — ซึ่งเป็นขนาดปกติของ coding agent, research agent, long-running workflow. **Claude Code เปิด default** แล้วสำหรับ user ส่วนใหญ่. **Available บน native Claude Platform + AWS Bedrock + Azure AI Foundry + Google Cloud Vertex** — multi-cloud ครบ

Caveats สำคัญ:
1. **Token usage ไม่เปลี่ยน** — Claude ยัง read conversation ทั้งหมดทุก turn ตอน execute model, ดังนั้น **cost per request ยังเท่าเดิม**. ประหยัด network + input processing time เท่านั้น
2. **TTL 5 นาที** — thread หายหลัง 5 นาทีที่ไม่มี request เข้ามา. สำหรับ long-running autonomous agent (เช่น overnight research), developer ต้อง refresh / reconstruct — หรือหา pattern อื่น
3. **ไม่ eligible สำหรับ zero data retention (ZDR) และ HIPAA setups** — enterprise ที่ต้องการ compliance level นี้ **ไม่สามารถใช้** Message Threads. เป็นข้อจำกัดที่หนัก — financial, healthcare, government use case ยังต้องใช้ pattern เดิม
4. **Production fail recovery** — เนื่องจาก Anthropic ไม่ persist ให้, ถ้า thread หาย developer ต้อง resend full history. Production client ยังต้องเก็บ canonical history ของตัวเอง

ส่วน header date **2026-08-12** น่าสนใจ — Anthropic ใช้ date-based beta header เหมือน API versioning. ถ้าเห็นประวัติศาสตร์ (prompt caching, PDF, tool use), feature ปกติอยู่ beta 3–6 เดือนก่อน GA. **คาด Message Threads GA ใน Q1 2027**

## ทำไมสำคัญ

Message Threads คือ **การยอมรับว่า agent loop ปกติไม่ efficient** — การส่ง conversation 800 KB ทุก turn คือ waste ของ bandwidth + input processing time. Anthropic เลือก **state ฝั่ง server** แก้ — คล้ายกับ OpenAI **Responses API** ที่เปิดเมื่อ มี.ค. 2026 (ทำ hierarchy ของ response ID กับ previous_response_id คล้ายๆ กัน). **Divergence ของ 2 เจ้า**: OpenAI คงรูปแบบ response chain; Anthropic เลือก **named thread + beta flag ชัด** — แบบ Anthropic เรียก easier to reason about แต่ require explicit opt-in

Pattern สำคัญสำหรับ developer experience: **Claude Code เปิด default** แปลว่า Anthropic เห็น telemetry ของตัวเองแล้วมั่นใจ — coding agent ของ Claude Code เอง benefit จาก TTFT 35% เพียงพอที่ Anthropic ยอม ship default. บ่งบอกว่า **คนที่สร้าง agent จริงจะเห็น latency win คุ้มค่า** — ปัญหาเดียวคือ 5-min TTL + ZDR limit

Impact ต่อ market: **OpenAI Responses API, Google Vertex, Azure AI — มีคู่แข่ง spec แล้ว**. Message Threads ของ Anthropic เป็น **middle ground** — ไม่ full stateful (OpenAI Assistants API มี thread แบบ long-lived + persist to disk + search semantics) แต่ **ไม่ stateless แบบ Messages เดิม**. เลือกตรงนี้สะท้อน POV ของ Anthropic: **อย่าทำ server เก็บ state ยาว**, ให้ developer เก็บเอง, เซิร์ฟเวอร์ optimize แค่ latency window สั้น. POV นี้ดี defense ต่อ data retention concern แต่ limit use case

ประเด็นที่ ecosystem ต้องจับตา: **LangGraph, Vercel AI SDK, Mastra, Inngest** จะต้อง detect Message Threads header แล้ว route request ให้ถูก — framework ที่ยังส่ง full history ทุก turn จะ **silent waste** latency. คาด LangGraph / Vercel ship native support ภายใน 2 สัปดาห์ (Vercel มักเร็วสุด). **Observability vendor** (Braintrust, Arize, Humanloop, Langfuse) ต้อง handle trace ของ thread — ปัจจุบัน trace ปกติเน้น full message history, พอ thread มาต้อง stitch จาก thread ID

## มุม AI Agent Platform

สำหรับ **builders** ที่ build agent ด้วย Claude: enable `anthropic-beta: message-threads-2026-08-12` ตอนนี้ได้ทันทีถ้า use case ไม่ require ZDR. Agent coding, research, customer support, data analysis — benefit หนักสุด. Workflow ที่ตัว agent รัน < 5 นาที/turn (ส่วนใหญ่) ใช้ได้เลย. **อย่าลืมเก็บ canonical history ของตัวเอง** — ถ้า 5-min window หมด, fallback ไป resend full จะ smooth. Framework เจ้าใหญ่จะ ship native support เร็ว — ถ้ารอได้, รอดีกว่า custom implement

สำหรับ **users / business** ที่ใช้ Claude Code: ไม่ต้องทำอะไร — Claude Code เปิด default แล้ว, TTFT ควรลงเห็นชัด (coding agent ขนาด 500k token context ซึ่งพบปกติใน repo ใหญ่). ถ้าใช้ Claude Enterprise ใน Cowork, feature นี้ควร available ด้วย — ติดต่อ CS. สำหรับ regulated industry (banking, healthcare, FSI) — **อย่าเพิ่ง enable ใน production** ถ้ายังต้อง ZDR / HIPAA. รอ Anthropic ประกาศ compliant variant (คาด Q2 2027)

สำหรับ **ecosystem**: **OpenAI vs Anthropic ตีกันเรื่อง state management primitive** น่าสนใจ — OpenAI รัน Responses API + Assistants API (2 แบบ), Anthropic รัน Messages + Message Threads. **Standard ไม่มี** — จะไม่มีในระยะเวลาที่คาดได้. MCP (Model Context Protocol) ไม่ cover ส่วนนี้, OpenAI Agents SDK vs Claude Agent SDK ก็ expose API ต่างกัน. **Framework layer** (LangGraph, Vercel AI SDK) จะเป็น abstraction ที่ developer ต้องเลือก. 2027 developer community จะเห็น **migration tax ของการเปลี่ยน LLM vendor** สูงขึ้น ไม่ใช่ลด — contrast กับ marketing “provider agnostic” ที่ทุก framework ขาย

## Sources
- [Anthropic — Make long-running agents faster with message threads](https://claude.com/resources/articles/message-threads)
- [The Next Web — Anthropic's message threads let Claude agents skip resending chats](https://thenextweb.com/news/anthropic-message-threads-beta-claude-api-agents)
- [AlphaSignal — Message Threads Cut Agent Request Size from 800 KB to 1.8 KB](https://alphasignal.ai/news/anthropic-s-message-threads-cut-agent-request-size-from-800-kb-to-1-8-kb)

---

## Audio script
2 พฤศจิกายน Anthropic ปล่อย Message Threads ขึ้น public beta บน Messages API. กลไกคือ แทนที่ agent จะส่ง conversation เต็ม 800 กิโลไบต์ทุก turn เราส่งเต็มครั้งเดียว รอบต่อไปส่งแค่ new message กับ thread ID เท่านั้น ประมาณ 1.8 กิโลไบต์ ที่เซิร์ฟเวอร์ Anthropic เก็บ state ไว้ encrypted in memory 5 นาที ผลที่ได้ TTFT ลด 35 เปอร์เซ็นต์ สำหรับ request ขนาด 500 K ถึง 1M token Claude Code เปิด default แล้ว available ทั้ง native Claude Bedrock Azure Foundry และ Vertex. Caveats สำคัญ สาม ข้อ. หนึ่ง token usage ไม่เปลี่ยน ประหยัดแค่ network และ input processing. สอง TTL แค่ 5 นาที agent ที่รันยาวต้อง reconstruct เอง. สาม ไม่ compatible กับ zero data retention และ HIPAA — regulated industry รอ compliant variant ต้นปี 2027. ภาพใหญ่ OpenAI มี Responses API อยู่แล้ว Anthropic เลือก path แตก ต่าง — Framework layer แต่ละเจ้าต้อง detect header แล้ว route request ให้ถูก Vercel AI SDK LangGraph น่าจะ ship เร็วสุด. Takeaway สำหรับ builder enable วันนี้ได้ทันทีถ้า use case ไม่ต้อง ZDR coding agent research customer support benefit หนักสุด เก็บ canonical history ของตัวเองไว้เสมอ กัน thread หมดอายุ
