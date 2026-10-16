---
date: 2026-10-17
slug: microsoft-copilot-studio-agent-accounts
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A glowing corporate badge card labeled "AGENT ACCOUNT" sliding into a
  Microsoft-blue reader on a modern office floor; next to it, three
  stacked numbers float: "ENTRA ID", "SHARED MEMORY", "TRIGGERED BY EMAIL".
  In the background, a translucent robot teammate reads a Teams message
  while a clock behind it shows no human prompt — the agent starts work on
  its own. Editorial isometric illustration, cobalt and amber palette, high
  contrast for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-17-0614-01-microsoft-copilot-studio-agent-accounts.png
---

# Microsoft Copilot Studio ให้ agent มี account ของตัวเอง — เสียงสะท้อนตรงจาก ServiceNow Passport

## TL;DR
- 15 ต.ค. Microsoft เปิด preview **Copilot Studio agent accounts** ใน Frontier program — agent แต่ละตัวได้ **Entra ID** ของตัวเอง, มี **shared business-process memory**, และรัน **triggers** (email, schedule, external signal) โดยไม่ต้องรอ prompt
- ตามหลัง ServiceNow AI Passport (14 ต.ค.) **24 ชั่วโมง** — hyperscaler สองรายใหญ่สุด convert agent ให้มี identity + runtime trigger ในสัปดาห์เดียวกัน
- Memory ยัง **ไม่มี opt-out** ใน preview — ข้อมูลที่ user ส่งเข้า agent ถูก summarize แล้วตอบ user คนอื่นได้; เอกสาร Learn ของ Microsoft เขียนว่า "private" แต่ preview เขียนว่า "shared" — คือ gap ที่ enterprise security team จะกดเบรก

## เกิดอะไรขึ้น

วันพฤหัสที่ 15 ต.ค. Microsoft ประกาศผ่าน Copilot blog ว่า Copilot Studio ได้สามอย่างใหม่พร้อมกันใน Frontier early-access: **agent accounts** ที่เป็น Entra ID ของ agent, **shared memory** ที่เก็บ context ของ business process ข้ามหลาย conversation, และ **triggers** ที่ให้ agent เริ่มทำงานเองเมื่อมี external signal (email ถึง mailbox เฉพาะ, scheduled time, webhook) โดยไม่ต้องมี user พิมพ์อะไรเลย — Microsoft เรียกมันตรง ๆ ว่า "digital teammates ที่ delegate business process ได้"

Agent account เป็น shift ที่สำคัญ — ก่อนหน้านี้ agent ทำงานใน Copilot ภายใต้ identity ของ user ที่ invoke มัน (คล้าย service principal แบบ shared) ตอนนี้ agent ได้ identity ของตัวเอง audit log แยกได้ ตั้ง conditional access ได้ License ก็ถูก model แยกต่างหาก — WindowsForum report ว่า Microsoft กำลัง price มันแบบ seat ของ agent ไม่ใช่ seat ของ user เท่ากับ Copilot Studio กลายเป็น platform ที่ขาย "agent headcount" ให้องค์กรจริง ๆ

ส่วน shared memory เป็น feature ที่ควรจับตามากที่สุด — agent จำสิ่งที่ user A บอกไว้แล้วใช้ context นั้นตอบ user B ใน team เดียวกัน Microsoft positioning ว่าเป็น "institutional memory ของ team" แต่ preview เขียนไว้ชัดว่า **ไม่มี opt-out** ซึ่งเอกสาร Learn เก่า (~74 วัน) ที่พูดถึง memory ของ GitHub Copilot เขียนว่า "private" ตรงนี้คือ gap ของ product ที่ enterprise security team จะต้องกดเบรก และ Microsoft เองก็ต้อง clarify ก่อน GA

Triggers เป็นชิ้นที่ใกล้ ServiceNow AI Passport ที่สุด — เพราะทันทีที่ agent รันเองได้โดยไม่ต้องมี human prompt ปัญหา governance (ใคร accountable? scope แค่ไหน?) ก็กลายเป็น runtime concern ไม่ใช่ design-time Microsoft แก้ด้วย agent account + Entra conditional access ส่วน ServiceNow แก้ด้วย signed passport — ต่าง approach คน answer คำถามเดียวกัน

## ทำไมสำคัญ

ที่น่าสังเกตคือ **timing** — ServiceNow AI Passport ประกาศ 14 ต.ค., Microsoft Copilot Studio agent accounts ประกาศ 15 ต.ค. วันต่อวัน พร้อม pattern เดียวกัน: identity ของ agent + trigger ที่ไม่ต้อง user prompt + accountable owner สองยักษ์ enterprise platform ที่ไม่ใช่ framework vendor ลงมาเล่น "agent OS" layer ภายใน 24 ชั่วโมงกัน — pattern นี้ตรงกับ brief เมื่อวาน (ServiceNow): control plane ของ agent กำลังกลายเป็น product line

ที่ Microsoft ทำต่าง ServiceNow คือ Microsoft **มี Entra และ Microsoft 365 identity graph อยู่แล้ว** — ไม่ต้อง bootstrap identity provider จากศูนย์ Entra กลายเป็น identity provider ของ agent ตั้งแต่วันแรก ซึ่งเป็น strategic moat ที่ ServiceNow ไม่มี เช่นเดียวกัน Microsoft ไม่ต้องสร้าง tool catalog ใหม่ — Microsoft Graph API + 300+ connector ของ Power Platform เป็น catalog อยู่แล้ว

สิ่งที่ไม่พูดถึงคือ **cost** — Microsoft ยังไม่ public ราคาของ agent account แต่ WindowsForum อ้างว่า licensing จะคล้าย per-seat สำหรับ agent หมายความว่าถ้า org deploy agent 100 ตัวจริง ค่า license ก็จะเป็น order-of-magnitude ของ Microsoft 365 E5 ซึ่งจะเป็น benchmark ที่ competitor ต้อง price around

## มุม AI Agent Platform

สำหรับ **builder** ที่กำลังสร้าง agent framework แบบ open-source (CrewAI, LangGraph, PydanticAI) นี่เป็นสัญญาณชัดว่า Microsoft กำลัง compete ไม่ใช่ที่ model หรือ orchestration แต่ที่ **identity + licensing** — ตรงที่ open-source แตะยาก ถ้าลูกค้า enterprise ต้องการ Entra audit log ก็ยากที่จะไปใช้ framework อื่น vendor อื่นต้องเลือกว่าจะ interop กับ Entra ตั้งแต่ day one หรือยอมเสีย enterprise segment

สำหรับ **business ที่ deploy agent** การเลือกระหว่าง Microsoft Copilot Studio กับ ServiceNow AI Passport กำลังกลายเป็น architectural decision — ไม่ใช่แค่ซื้อ feature แต่คือเลือก identity provider ของ agent fleet ว่าจะอยู่ที่ไหน และ Microsoft มี advantage ตรงที่ Entra อยู่ในมืออยู่แล้ว; สำหรับ **ecosystem** — เริ่มเห็น shape ของ "agent IAM" market ที่ Microsoft, ServiceNow, Okta (ยังเงียบ) จะชนกันในปี 2027

## Sources
- [Delegate shared business processes to agents that are more persistent and proactive — Microsoft](https://www.microsoft.com/en-us/copilot/blog/copilot-studio/delegate-shared-business-processes-to-agents-that-are-more-persistent-and-proactive-with-microsoft-copilot-studio/)
- [Microsoft Copilot Studio Agent Accounts Preview: Entra IDs, Shared Memory, Triggers and Licensing — WindowsForum](https://windowsforum.com/news/microsoft-copilot-studio-agent-accounts-preview-entra-ids-shared-memory-triggers-and-licensing.448622/)
- [New in Frontier: Delegate Business Processes to Copilot Studio Agents — futurework.blog](https://futurework.blog/2026/10/16/new-in-frontier-delegate-business-processes-to-copilot-studio-agents/)

---

## Audio script
เมื่อวานเราคุยเรื่อง ServiceNow AI Passport ว่า agent ทุกตัวต้องมี signed identity กับ runtime kill-switch วันนี้ 15 ตุลาคม Microsoft ขยับตามแบบวันต่อวัน เปิด preview Copilot Studio agent accounts ใน Frontier early-access program ให้ agent แต่ละตัวมี Entra ID ของตัวเอง มี shared business-process memory และมี triggers ที่ให้ agent เริ่มทำงานเองโดยไม่ต้องรอ user prompt ไม่ว่าจะเป็น email ที่เข้า mailbox เฉพาะ หรือ scheduled time หรือ external webhook

ประเด็นสำคัญคือ Microsoft ไม่ต้อง bootstrap identity provider จากศูนย์เหมือน ServiceNow เพราะมี Entra และ Microsoft Graph อยู่แล้ว แปลว่า Entra กำลังจะกลายเป็น identity provider ของ agent ตั้งแต่วันแรก Audit log แยกได้ conditional access ตั้งได้ licensing ก็มีแนวโน้มว่าจะคิดเป็น seat ของ agent ไม่ใช่ seat ของ user เหมือนเดิม

เรื่องที่ enterprise security team จะต้องจับตาคือ shared memory เพราะ preview เขียนไว้ว่าไม่มี opt-out แต่เอกสาร Learn ของ Microsoft ที่พูดถึง memory ของ GitHub Copilot เขียนว่า private นี่เป็น gap ของ product ที่ Microsoft ต้อง clarify ก่อน GA

ภาพรวมที่สำคัญคือ ServiceNow 14 ตุลาคม Microsoft 15 ตุลาคม สองยักษ์ enterprise platform ที่ไม่ใช่ framework vendor ลงมา claim agent OS layer ภายใน 24 ชั่วโมงกัน pattern เดียวกันเลย คือ identity ของ agent plus runtime trigger plus accountable owner คำถามคือใครในวงการ framework open-source อย่าง LangGraph หรือ CrewAI จะยอม interop กับ Entra ตั้งแต่ day one หรือยอมเสีย enterprise segment ไปเลย
