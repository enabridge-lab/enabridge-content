---
date: 2026-08-31
slug: claudeforce-salesforce-anthropic-37-skills
topic: openbridge-trend
reading_time_min: 5
sources: 4
image_prompt: |
  Editorial isometric illustration of two giant translucent buildings labeled
  "SALESFORCE" and "CLAUDE" merging into a single glass tower with a bold
  neon sign on top reading "CLAUDEFORCE". Streams of small numbered cards
  labeled "37 SKILLS" flow between the two buildings on illuminated bridges.
  Below, a subtle banner reads: "CRM INSIDE CLAUDE". Muted blue + orange
  palette, high contrast so the tower name and 37-SKILLS cards read clearly
  at 200px thumbnail. Magazine editorial style. 1:1 aspect ratio. No real
  human faces, silhouette figures walking between towers OK.
image: images/26-08-31-0618-02-claudeforce-salesforce-anthropic-37-skills.png
---

# Claudeforce — Salesforce ยัด CRM ทั้งก้อนเข้า Claude, 37 sales skills, Benioff บอก "you won't need our app"

## TL;DR
- **Salesforce + Anthropic** ประกาศ **Claudeforce** (26 ส.ค.) — ปิด strategic partnership ที่ทำ 2 ทิศทาง: Claude กลายเป็น default reasoning ใน Agentforce + Salesforce ทั้งก้อนเข้าไปอยู่ใน Claude
- **Salesforce in Claude Plugin:** 37 prebuilt sales skills — seller ทำ pipeline update, deal review, meeting prep ผ่าน Claude ได้โดย **ไม่ต้องเปิด Salesforce** เลย
- **Claude in Salesforce:** default model ของ Atlas Reasoning Engine, Agentforce Vibes, Agentforce Coworker — deploy ผ่าน Amazon Bedrock ภายใน Salesforce Trust Boundary
- **Benioff** ออกมาตอบ "SaaSpocalypse" concern ที่นักลงทุนจี้มาหลายไตรมาส — ครั้งแรกที่ SaaS ยักษ์ยอมรับว่า agent จะ subsume UI ของตัวเอง

## เกิดอะไรขึ้น

วันที่ 26 ส.ค. Salesforce ประกาศ **Claudeforce** — expanded partnership กับ Anthropic ที่ทำใน 2 ทิศทางพร้อมกัน. Marc Benioff ประกาศพร้อม Dario Amodei — เป็นการตอบ SaaSpocalypse concern ตรง ๆ ที่นักลงทุนกดดันมาตั้งแต่ Q4 ปีที่แล้ว: agent จะ eat SaaS หรือไม่?

**ทิศแรก — Salesforce in Claude:** เปิด **Plugin ใน Claude** ที่มี **37 prebuilt sales skills** — meeting preparation, deal health review, pipeline analysis, opportunity update, forecast query, activity log. Seller สามารถพูดใน Claude ว่า "ให้ prep call กับ Acme Corp พรุ่งนี้เช้า" — Claude query Salesforce API, ดึง contact history + open opportunity + last email + support ticket, สรุปพร้อม suggested talking point + risks — ทำใน Claude UI ทั้งหมด **โดย seller ไม่ต้องเปิด Salesforce app**. นี่คือประโยคที่ทำให้ VentureBeat พาดหัวว่า "you won't need its app again"

**ทิศสอง — Claude in Salesforce:** Claude กลายเป็น **default reasoning model** ของ:
- **Atlas Reasoning Engine** (Agentforce brain)
- **Agentforce Vibes** (marketing/content agent)
- **Agentforce Coworker** (general-purpose employee agent)
- Available ใน **Agent Builder** ให้ builder เลือก

Deploy ผ่าน **Amazon Bedrock** ภายใน **Salesforce Trust Boundary** — สำคัญเพราะ regulated customer (financial services, healthcare, government) สามารถใช้ Claude ได้โดย data ไม่ออก compliance perimeter ของ Salesforce

Partnership ระดับนี้ระหว่าง 2 บริษัทที่มี valuation รวม > $500B — เกิดหลังจากที่ Salesforce เคยพยายาม build reasoning model ของตัวเอง (Einstein GPT, Atlas) แล้วเจอ reality ว่า frontier lab ไปเร็วกว่า. Benioff เลือกที่จะ **partner แทน compete** — เป็น strategic bet ที่คล้าย Microsoft-OpenAI ปี 2023

## ทำไมสำคัญ

Claudeforce คือ **first major SaaS-frontier-lab merger** ในระดับ product architecture (ไม่ใช่แค่ API partnership). เทียบกับ competitive landscape:
- **Microsoft-OpenAI** — deep integration แต่ Microsoft เป็น cloud + OS ไม่ใช่ CRM; Copilot ยังต้องเปิด Word/Excel
- **Google-Anthropic** (Cloudflare-Anthropic distribution) — infrastructure play, ไม่ touch application UI
- **Salesforce-Anthropic** — **application UI merger**: Claude UI = Salesforce UI = same experience

Signal ที่ตามมา:
- **ServiceNow, Workday, HubSpot, Zendesk** จะต้องเลือก partner กับ frontier lab ภายใน 6 เดือน — Anthropic เต็มแล้ว, OpenAI จะเป็น target ต่อไป; Google Gemini partnership ก็เป็น option
- **Slack** (owned by Salesforce) กลายเป็น distribution channel ของ Claude — 200M+ paid user ที่ pipe agent เข้า workflow. Slack ในตอนนี้เพิ่งเปิดให้ run full Salesforce CRM motion ภายใน Slack conversation (Aug 26)
- **Agentforce competitive moat** — Salesforce มี unique advantage คือ **data + workflow + business logic + governance** ที่สั่งสมมาตั้งแต่ Force.com era; ที่ agent lab startup ไม่มี. Claudeforce คือ Salesforce เปิดให้ Claude access asset ทั้งหมดนี้ — Claude เก่งขึ้น 10× บน workflow B2B

จุดที่นักลงทุนจับตา:
- **Take rate**: ใครเก็บเงิน user seller คนไหน? ผู้ใช้ที่ pay Claude subscription ($200/mo) + Salesforce seat ($150-300/mo) จะเห็น value stack แบบไหน? Benioff ยังไม่ตอบชัด
- **Model lock-in vs choice**: ถ้า user prefer GPT-5 หรือ Gemini 3 บน Agentforce — Salesforce ยัง open หรือไม่? Agent Builder ยังบอก "select model" — แสดงว่ายัง multi-model
- **Data sovereignty**: Amazon Bedrock inside Salesforce Trust Boundary = ดี แต่ Anthropic ยัง see prompt/completion log หรือไม่? เอกสาร legal ยังไม่ publish

## มุม AI Agent Platform

**Builders** ที่ build vertical agent (industry-specific: manufacturing, legal, healthcare): Claudeforce เปิดโมเดลใหม่ — **agent ที่ live inside another company's context** (Claude ที่มี Salesforce context) กลายเป็น pattern ที่ทุก B2B SaaS จะเลียนแบบ. Path forward: (1) build Plugin/skill สำหรับ Claude / GPT desktop ที่ inject context ของ vertical เข้า general-purpose agent; (2) หรือ inverse — inject Claude/GPT reasoning เข้า vertical UI

**Users / businesses** ที่ใช้ Salesforce (85% ของ Fortune 500): ต้องเริ่ม **evaluate seller workflow ใหม่** — ถ้า seller ใช้ Claude เป็น primary UI แล้ว Salesforce เป็น backend, training + change management เปลี่ยนหมด. HR + IT ต้องเตรียม governance policy ก่อน rollout — เพราะ Claude prompt เก็บไว้ที่ไหน, ใครดูได้, log audit ยังไง

**Ecosystem — SaaS ทั้งชั้น application layer:**
- **Winners**: Salesforce (ยึด seat + data), Anthropic (ยึด reasoning + user), Slack (ยึด surface), AWS (ยึด compute)
- **Losers**: standalone AI CRM (Attio, Copper, monday CRM), pipeline-only tool (Salesloft, Outreach), sales intel tool ที่ไม่ integrate deep (Gong, Chorus จะโดนกดดัน)
- **Uncertain**: HubSpot — SMB dominant, ยังไม่ประกาศ frontier lab partner ใหญ่; ต้องขยับใน 90 วัน

**Enabridge angle**: Claudeforce = template สำหรับ **agent integration layer** ที่ Enabridge สามารถ position ในตลาดไทย/SEA ที่ Salesforce ไม่ hard-lock. ตลาด mid-market SEA ที่ใช้ Odoo, Zoho, Bitrix, HubSpot Starter — ไม่มี "Claudeforce equivalent" — โอกาสสร้าง **"AgentLayer for SEA SaaS"** ที่ inject Claude/local LLM reasoning เข้าใน CRM ที่ enterprise ไทยใช้จริง

## Sources
- [Salesforce and Anthropic Announce Claudeforce (Salesforce Investor)](https://investor.salesforce.com/news/news-details/2026/Salesforce-and-Anthropic-Announce-Claudeforce-The-1-AI-Meets-the-1-AI-CRM/default.aspx)
- [Salesforce just put its entire CRM inside Claude (VentureBeat)](https://venturebeat.com/orchestration/salesforce-just-put-its-entire-crm-inside-claude-and-says-youll-never-need-its-app-again)
- [Salesforce, Anthropic expand partnership as Benioff responds to 'SaaSpocalypse' (CNBC)](https://www.cnbc.com/2026/08/26/salesforce-anthropic-partnership-claudeforce.html)
- [Claudeforce Explained: What Salesforce + Anthropic Actually Ship (Apex Hours)](https://www.apexhours.com/claudeforce-explained-what-salesforce-anthropic-actually-ship/)

---

## Audio script
ข่าวใหญ่ครับ วันที่ 26 สิงหาคมที่ผ่านมา Salesforce ประกาศ partnership ครั้งใหญ่กับ Anthropic ชื่อว่า Claudeforce. Deal นี้ทำสองทิศทางพร้อมกัน — ทิศแรก Salesforce เอา CRM ทั้งก้อน 37 sales skill เข้าไปอยู่ใน Claude ผ่าน plugin ใหม่ แปลว่า seller ตั้งแต่วันนี้สามารถทำ pipeline update ทำ deal review ทำ meeting prep ใน Claude ได้โดยไม่ต้องเปิด Salesforce app เลย. ทิศสอง Claude กลายเป็น default reasoning model ของ Agentforce ทั้ง Atlas Reasoning Engine ทั้ง Agentforce Vibes ทั้ง Agentforce Coworker — deploy ผ่าน Amazon Bedrock ภายใน Salesforce Trust Boundary. Marc Benioff ออกมาตอบ SaaSpocalypse concern ที่นักลงทุนจี้มาหลายไตรมาสว่า Salesforce ยอมรับแล้วว่า agent จะ subsume UI ของตัวเอง จึงเลือกจับมือกับ frontier lab แทนสู้กัน. Signal ต่อไปคือ ServiceNow, Workday, HubSpot ต้องเลือก partner ภายในหกเดือน. สำหรับ Enabridge — Claudeforce ยึด enterprise Fortune 500. โอกาสของเราคือ mid-market SEA ที่ใช้ Odoo, Zoho, HubSpot Starter — สร้าง AgentLayer ที่ inject reasoning เข้า CRM ที่ SME ไทยใช้จริงครับ
