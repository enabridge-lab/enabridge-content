---
date: 2026-10-17
slug: cisco-webex-agentic-framework
topic: openbridge-trend
reading_time_min: 3
sources: 3
image_prompt: |
  A translucent robot teammate sitting at a conference table joining a
  Webex meeting through a floating glass screen; three stacked numbers glow
  above the table: "SPACES", "MEETINGS", "CALLS". Behind the robot a
  dashboard labeled "DIALOG LAYER — CUSTOMER CONTEXT" shows a timeline that
  survives across sessions. Editorial isometric illustration, deep navy and
  teal palette, high contrast for 200px thumbnails, 1:1 aspect, no real
  human faces.
image: images/26-10-17-0614-03-cisco-webex-agentic-framework.png
---

# Cisco Webex ให้ agent "เดินเข้ามานั่งใน meeting" — collab platform กลายเป็น agent runtime

## TL;DR
- 7 ต.ค. (WebexOne 2026) Cisco เปิด **agentic framework** ให้ agent เข้าร่วม **spaces, meetings, calls** ได้เหมือน teammate — มี **Dialog layer** เก็บ customer context ข้าม interaction
- Agent สามารถ **invite** ได้โดย employee + ทำ task ข้าม calendar / document / third-party app ภายใต้ **human oversight + audit trail**
- RoomOS 27 มี **Director Agent** auto-adjust camera + **Workspace Advisor** build 3D twin ของห้องประชุม — Cisco ยืมโมเดล "agent-as-attendee" จาก Zoom AI Companion แต่เพิ่ม framework ให้ dev build เอง

## เกิดอะไรขึ้น

ที่ WebexOne 2026 ต้นเดือน Cisco ประกาศ framework agentic ของ Webex — ไม่ใช่ feature เดี่ยว ๆ อย่าง notetaker หรือ polling (ซึ่งเปิดมาตั้งแต่ WebexOne 2025) แต่คือ platform ที่ให้ **agent เป็น attendee** ของ meeting, space, call ได้ Employee สามารถ invite agent ด้วยชื่อ (เช่น @research-agent) agent เข้ามาด้วย identity ของตัวเองพร้อม audit log ทำงานข้าม calendar + Jira + Salesforce + third-party app แล้วตอบกลับใน thread เดียวกัน

**Dialog layer** คือตัวแปรสำคัญ — ก่อนหน้านี้ customer service agent (CX) ของ Webex Contact Center จำ context ของ customer ได้แค่ภายใน session Dialog layer เก็บ context ข้าม interaction หมายความว่า agent ที่คุยกับ customer เรื่อง refund วันจันทร์ จำได้วันพุธเวลา customer โทรกลับเรื่อง delivery และยกบริบทมาเพื่อ cross-sell / de-escalate Cisco positioning มันเป็น "agent memory ของ CX" ซึ่งตรงกับที่ Microsoft ประกาศเมื่อวาน (shared business-process memory) แต่ specialized สำหรับ customer-facing

Side announcement ที่ไม่ควรข้ามคือ **RoomOS 27** พร้อม **Director Agent** ที่ auto-adjust camera framing ของห้องประชุม (ตามคนพูด) และ **Workspace Advisor** ที่ build 3D digital twin ของห้องแล้วแนะนำ layout + hardware optimization ก็เป็น physical AI อีกจุดที่ Cisco เริ่มเล่น

TechRepublic ตั้งข้อสังเกตว่า feature หลายอันยัง "forthcoming" — Cisco ประกาศ framework แต่ availability + integration + access control ยังต้องรอ Q1 2027 ซึ่งเป็น pattern ที่ Cisco ทำบ่อย (ประกาศเร็ว ship ช้า)

## ทำไมสำคัญ

ตั้งแต่ WebexOne 2025 Cisco ปล่อย meeting agent มาหลายตัว (notetaker, polling, scheduler, AI receptionist) แต่ยังเป็น point feature ปี 2026 นี้ Cisco ขยับไป **platform** คือเปลี่ยนจาก "Cisco ขาย agent ให้คุณใช้" เป็น "คุณ build agent มาเองก็ได้ Cisco เป็น runtime" ซึ่ง align กับ playbook ของ Microsoft Copilot Studio (horizontal agent OS) แต่ specialized ที่ collaboration surface

Pattern ที่น่าจับตาคือ **collaboration platform เริ่ม compete กับ agent framework ที่ layer ของ "ที่อยู่ของ agent"** — ก่อนหน้านี้ agent รันใน sandbox ของ cloud (OpenAI Platform, Anthropic Platform) ตอนนี้ agent เริ่มรันในที่ที่ work เกิดขึ้นจริง (Webex, Teams, Slack) ซึ่งเปลี่ยนเกม distribution — ลูกค้าไม่ต้องเลือก IDE แปลก ๆ มา invoke agent แต่ invoke จาก conversation ที่มีอยู่แล้ว

ที่ Cisco ยัง weak กว่า Microsoft คือ identity + licensing — Microsoft มี Entra, Cisco มี Duo (ซื้อปี 2018) แต่ Duo น้ำหนักน้อยกว่า Entra ใน enterprise identity graph และ licensing ของ Cisco ยังไม่ชัดว่าจะ price agent-as-attendee แบบ seat หรือแบบ task

## มุม AI Agent Platform

สำหรับ **builder** ที่ขาย agent framework (CrewAI, LangGraph, LlamaIndex) — Cisco Webex framework หมายถึงมี distribution channel ใหม่: agent ของคุณสามารถถูก invite เข้า Webex meeting ได้โดยตรง ถ้า framework ของคุณ expose metadata ที่ Dialog layer อ่านเข้าใจ แปลว่า integration layer กับ collaboration platform กลายเป็น strategic — ไม่ใช่แค่กับ cloud orchestration

สำหรับ **business ที่ deploy agent** — ถ้า team ของคุณใช้ Webex อยู่แล้ว การ invite agent เป็น attendee ของ meeting คือ shortcut adoption ที่ไม่ต้อง train พนักงานใหม่ แต่ต้องระวัง audit trail ของ agent action ให้แยกจาก audit ของ meeting content

สำหรับ **ecosystem** — Cisco ไม่ใช่คนแรกที่ทำ (Zoom AI Companion มาก่อน + Slack มี AgentForce ของ Salesforce) แต่ Cisco เป็นคนแรกที่ productize ว่าเป็น **framework** ให้ dev build agent attendee เองได้ ไม่ใช่แค่ใช้ agent ของ Cisco — Zoom, Microsoft Teams, Slack ต้องตอบคำถามเดียวกันภายใน 6 เดือน

## Sources
- [Cisco Announces Webex AI Agents for Meetings and Customer Service — TechRepublic](https://www.techrepublic.com/article/news-cisco-webex-ai-agents-meetings-customer-service/)
- [Cisco goes all-in on agents - and it could mean big changes in your workplace — TechRadar](https://www.techradar.com/pro/cisco-goes-all-in-on-agents-and-it-could-mean-big-changes-in-your-workplace)
- [Cisco unveils framework to transform workforce collaboration with AI agents — Digiday](https://digiday.com/media/cisco-unveils-framework-to-transform-workforce-collaboration-with-ai-agents/)

---

## Audio script
ที่งาน WebexOne 2026 Cisco เปิด framework agentic ของ Webex ให้ agent เข้าร่วม spaces meetings calls ได้เหมือน teammate ลง log ว่าใครทำอะไร มี audit trail และข้อสำคัญคือมี Dialog layer ที่เก็บ customer context ข้าม interaction หมายความว่า customer service agent ที่คุยเรื่อง refund วันจันทร์ จำได้วันพุธเวลา customer โทรกลับเรื่อง delivery พร้อมบริบททั้งหมด

Pattern ที่น่าสนใจคือ collaboration platform เริ่ม compete กับ agent framework ที่ layer ของที่อยู่ของ agent ก่อนหน้านี้ agent รันใน sandbox ของ cloud ตอนนี้ agent รันในที่ที่ work เกิดขึ้นจริง ไม่ว่าจะเป็น Webex Teams หรือ Slack ซึ่งเปลี่ยนเกม distribution ลูกค้าไม่ต้องเลือก IDE แปลก ๆ มา invoke agent แต่ invoke จาก conversation ที่มีอยู่แล้ว

จุดอ่อนของ Cisco คือ identity และ licensing Microsoft มี Entra ที่หนัก Cisco มี Duo ที่น้ำหนักน้อยกว่า และ Cisco ยังไม่ประกาศว่า price agent as attendee แบบ seat หรือแบบ task สำหรับทีมที่กำลังสร้าง agent framework ถ้า Webex expose metadata ให้ Dialog layer อ่านเข้าใจ แปลว่า integration layer กับ collaboration platform กลายเป็น strategic หลัก ไม่ใช่แค่กับ cloud orchestration อย่างเดียวอีกต่อไป
