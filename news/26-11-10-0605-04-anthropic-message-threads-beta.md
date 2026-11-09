---
date: 2026-11-10
slug: anthropic-message-threads-beta
topic: agentic-ai
reading_time_min: 3
sources: 4
image_prompt: |
  Editorial isometric illustration of a long conversation pipeline shown
  as a glowing thread between two servers; a huge counter reads "35%
  FASTER TTFT" and sub-tiles show "500K-1M TOKENS", "5 MIN THREAD LIFE",
  "NO HIPAA / NO ZDR". A small Claude Code window hovers at the side
  marked "DEFAULT ON". Deep turquoise and warm cream palette, clean
  editorial style, 1:1 aspect, no real human faces (silhouettes OK),
  high contrast so numbers stay readable at 200px thumbnail.
image: images/26-11-10-0605-04-anthropic-message-threads-beta.png
---

# Anthropic เปิด Message Threads beta — cut TTFT 35% สำหรับ long-running agent, default on ใน Claude Code แล้ว

## TL;DR
- Anthropic launch Message Threads เป็น public beta บน Messages API (2 พ.ย.) — agent ส่ง full conversation แค่ครั้งแรก ครั้งถัดไปส่งเฉพาะ message ใหม่ + thread ID
- รายงาน median time-to-first-token ลดลง ~35% สำหรับ request ขนาด 500K-1M tokens — token usage ยังเท่าเดิมเพราะ Claude ยังอ่าน context ทั้งหมดทุก turn
- Default on ใน Claude Code แล้ว — รองรับ native platform + AWS + Microsoft Foundry + Google Cloud — แต่ไม่รองรับ ZDR และ HIPAA

## เกิดอะไรขึ้น
วันที่ 2 พฤศจิกายน Anthropic เปิด Message Threads เป็น public beta บน Messages API — pattern ที่แก้ปัญหา latency ใหญ่สุดของ long-running agent: การส่ง full conversation history ทุก turn Developer เพิ่ม thread parameter ใน Messages API request ครั้งแรกส่ง full conversation เพื่อ start thread ครั้งถัดไปส่งเฉพาะ new message กับ ID ของ previous response — Anthropic จัดการ caching ข้างในเอง

ผลลัพธ์ที่บริษัทรายงาน — request ที่มี context 500,000 ถึง 1 million tokens median time-to-first-token (TTFT) ลดลงประมาณ 35% คนที่ build coding agent, research agent, หรือ multi-step workflow agent ที่ context ยาว ๆ จะรู้สึกชัด Claude ยังอ่าน full conversation ทุก turn — ใช้ token เท่าเดิม — แต่ server-side caching ทำให้ไม่ต้อง re-parse ทั้งหมด

Detail ที่ควรรู้ — thread หมดอายุ 5 นาทีหลัง request สุดท้าย, content เก็บใน memory (ไม่ลง disk), encrypt ด้วย server-managed key, ลบใน 1 ชั่วโมงหลังใช้งานล่าสุด ไม่ compatible กับ zero data retention (ZDR) และไม่ใช่ HIPAA-ready สิ่งที่น่าสนใจคือ feature เปิดใช้ใน Claude Code เป็น default แล้ว — Anthropic ใช้ dog-food product ตัวเองก่อน release ให้ developer ทั่วไป และรองรับผ่าน native Claude Platform, Claude on AWS, Claude in Microsoft Foundry, และ Claude Models on Google Cloud

## ทำไมสำคัญ
35% TTFT reduction บน long context เป็น meaningful improvement — แต่ signal ที่สำคัญกว่าคือ Anthropic กำลัง optimize infra สำหรับ agent workload โดยเฉพาะ ไม่ใช่ chat Message Threads ไม่ค่อย useful ถ้าคุณใช้ API สำหรับ single-turn request (summarization, classification) แต่สำคัญมากถ้า agent ของคุณ run 50-100 turn ใน task เดียว การลด TTFT 35% คือ compound effect — ถ้า agent รัน 100 turn ประหยัดเวลาใช้งานได้หลายนาที

Signal ที่สอง — การไม่รองรับ ZDR และ HIPAA คือ trade-off ที่ตั้งใจ Anthropic เลือกให้ performance ก่อน compliance ซึ่งบอกว่า target user คือ developer ที่สร้าง agent ให้ US consumer หรือ non-regulated enterprise ถ้าคุณอยู่ใน healthcare, finance, government ต้องรอ feature นี้ไปอีกพักหนึ่ง หรือใช้ pattern อื่น

Feature นี้เทียบกับคู่แข่งยังไง — OpenAI มี prompt caching มานาน แต่ semantics ต่าง (caching เป็น opt-in per prefix) Google Vertex มี context caching ที่ต้อง explicit มากกว่า Anthropic เลือกให้ thread เป็น first-class concept ที่ง่ายกว่า cache management — developer ไม่ต้องคิดเรื่อง prefix invalidation ทำให้ pattern นี้ win developer ที่ไม่มี infra team

## มุม AI Agent Platform
Builders — ถ้าคุณสร้าง agent framework (LangGraph, CrewAI, AutoGen, เป็นต้น) ที่ใช้ Claude ควร wrap Message Threads เข้าใน abstraction ของตัวเองก่อนที่ developer จะไปเขียน thread handling เอง การที่ Anthropic ใส่ feature นี้เป็น default ใน Claude Code เป็น signal ว่า long-running agent คือ workload ที่กำลัง scale ไว framework ที่ไม่ update pattern นี้จะ lag ด้าน latency

Users/business — business ที่ deploy agent บน Claude API ให้ถามทีม engineering ว่า migrate ไป Message Threads แล้วหรือยัง ถ้าใช่ จะเห็น user experience ดีขึ้นทันทีสำหรับ workflow ที่ context ใหญ่ ถ้าไม่ใช่ นั่นคือ low-hanging improvement ที่ควร prioritize Enabridge ที่ host agent บน Claude ให้ลูกค้า ควร communicate improvement นี้เป็น "silent win" — ลูกค้าไม่ต้องเปลี่ยน code แต่ experience ดีขึ้น

Ecosystem — ไม่รองรับ ZDR และ HIPAA คือ gap ที่ competitor จะ attack ถ้าคุณขาย agent ให้ healthcare หรือ regulated industry OpenAI กับ Google จะใช้ประเด็นนี้ pitch ว่า platform ของเขา enterprise-ready กว่า Anthropic คงต้องตามด้วย compliant version ภายใน 6 เดือน ไม่งั้นเสีย share ใน vertical ที่ regulate หนัก

## Sources
- [Make long-running agents faster with message threads (Claude Docs)](https://claude.com/resources/articles/message-threads)
- [Anthropic Launches Message Threads Beta for Long-Running Agents (Unite.AI)](https://www.unite.ai/anthropic-launches-message-threads-beta-for-long-running-agents/)
- [Anthropic's message threads let Claude agents skip resending chats (The Next Web)](https://thenextweb.com/news/anthropic-message-threads-beta-claude-api-agents)
- [Anthropic launches message threads for Claude, cuts time-to-first-token ~35% (NewsBytes)](https://www.newsbytesapp.com/news/science/anthropic-launches-message-threads-for-claude-cuts-time-to-first-token-roughly-35/tldr)

---

## Audio script
Anthropic เปิด Message Threads เป็น public beta บน Messages API เมื่อวันที่ 2 พฤศจิกายน แก้ปัญหา latency ใหญ่สุดของ long-running agent คือการส่ง full conversation history ทุก turn Developer เพิ่ม thread parameter ครั้งแรกส่ง full conversation ครั้งถัดไปส่งเฉพาะ new message กับ ID ของ previous response ผลที่บริษัทรายงาน median time to first token ลดลงประมาณ 35 เปอร์เซ็นต์ สำหรับ request ที่มี context 500,000 ถึง 1 ล้าน tokens Claude ยังอ่าน full conversation ทุก turn ใช้ token เท่าเดิม แต่ server-side caching ทำให้ไม่ต้อง re-parse ทั้งหมด detail ที่ควรรู้ thread หมดอายุ 5 นาทีหลัง request สุดท้าย content เก็บใน memory ไม่ลง disk ไม่ compatible กับ zero data retention และไม่ใช่ HIPAA ready feature เปิดเป็น default ใน Claude Code แล้ว รองรับผ่าน native platform plus AWS plus Microsoft Foundry plus Google Cloud 35 เปอร์เซ็นต์ TTFT ลดลงฟังดูเป็น incremental แต่ถ้า agent รัน 100 turn ใน task เดียว compound เป็นหลายนาที signal ที่สำคัญกว่าคือ Anthropic กำลัง optimize infra สำหรับ agent workload ไม่ใช่ chat สำหรับคนสร้าง agent framework ควร wrap Message Threads เข้าใน abstraction ตัวเองก่อน developer เขียน thread handling เอง ถ้า business ของคุณ deploy agent บน Claude API ให้ถามทีม engineering ว่า migrate ไป Message Threads แล้วหรือยัง ถ้ายัง นั่นคือ low-hanging improvement
