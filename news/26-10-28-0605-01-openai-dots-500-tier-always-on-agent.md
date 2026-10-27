---
date: 2026-10-28
slug: openai-dots-500-tier-always-on-agent
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  An editorial isometric illustration of a glowing orange "Dot" orb floating above
  a city of enterprise office buildings at night, trailing a long golden light
  tail of past tasks. In the foreground a price tag ribbon reads "$500 / MONTH"
  in massive display type, with two smaller tags beneath: "$200 PRO" and
  "$100 PRO". A small shelf of three stacked numbers hangs on the left:
  "20M WAU", "+35% QTD", "FIRST CONSUMER PREMIUM TIER". Deep navy sky with
  amber-orange highlights, Kodak-film grading, strong contrast for 200px
  thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-28-0605-01-openai-dots-500-tier-always-on-agent.png
---

# OpenAI Dots เปิดราคา $500/เดือน — consumer AI product ตัวแรกที่กล้าตั้งราคาระดับนี้

## TL;DR
- **OpenAI Dots** คือ always-on agent ที่รันในคลาวด์ VM ของตัวเอง เก็บงานข้าม conversation ได้ ปัจจุบันเปิดเฉพาะคน paying — **Pro 100 ($100/เดือน) / Pro 200 ($200) / Pro 500 ($500)** แต่ละชั้นได้ "a dot" รวมอยู่ด้วย ชั้น $500 เพิ่ม headroom สูงสุด + Astra Ultra
- **Rollout:** US + 4,000+ ประเทศแต่ **ไม่รวม UK, EEA, Switzerland** รอ regulatory clearance; Enterprise/Edu/Healthcare เป็น custom-priced กับ Dots **off by default**
- **ตัวเลขรอบล่าสุด (Aug 19):** OpenAI รายงาน coding + agent features ชน **20M weekly active users**, enterprise run rate **+50% ไตรมาสถึงวันนั้น**, overall revenue run rate **+35% QTD**
- Signal: นี่คือครั้งแรกที่ consumer AI product กล้าตั้ง **$500/เดือน floor** และเป็น **first real price tag for autonomous AI** — "SaaS seat ของ non-human worker" กำลังก่อตัวเป็น category จริง

## เกิดอะไรขึ้น

Bloomberg Tax (bgov) ยืนยันว่า OpenAI เปิด **Dots เป็นผลิตภัณฑ์ always-on agent** พร้อม pricing tier ใหม่ **$500/month** ซึ่งเป็น floor ที่ consumer AI product ไม่เคยกล้าแตะมาก่อน. โครงสร้าง tier เป็น: Pro 100 ($100), Pro 200 ($200), Pro 500 ($500) — ทุกชั้นได้ dot หนึ่งตัว, ชั้นสูงกว่าแค่เพิ่ม usage headroom และปลดล็อก Astra Ultra สำหรับ Pro 500. ไม่มี free tier สำหรับ Dots เลย

Dots ทำงานใน dedicated cloud VM ของตัวเอง — "keep working between conversations" คือ core promise. คน call หรือ message dot ผ่าน ChatGPT desktop/web/mobile หรือผ่าน **Slack + Microsoft Teams**; texting อยู่ใน roadmap. ความต่างจาก OpenAI Agents API (ที่ public beta เมื่อ Sep 10) คือ Dots เป็น **productized agent สำหรับ end-user** ไม่ใช่ developer primitive — ชั้นที่คล้าย ChatGPT แต่ "เดินงานต่อหลังปิดหน้าจอ"

Regional carve-out น่าสังเกต: UK, EEA, Switzerland ถูกตัดจาก initial rollout. ปัจจัยที่ตลาด infer คือ **EU AI Act Article 5 + GPAI obligations** ที่ require pre-deployment risk assessment สำหรับ autonomous agent class — OpenAI เลือก wait until regulatory clarity. สำหรับ enterprise, Dots เป็น **custom-priced + off by default** ซึ่งบ่งว่า liability model สำหรับ agent ที่เดินงานอิสระในองค์กรยังไม่ nail

ที่น่าสนใจกว่า pricing คือ scaling signal: ที่ investor meeting **14 ส.ค.** OpenAI รายงาน enterprise revenue **ชน consumer เป็นครั้งแรก** — enterprise run rate **>$40B annualized**, business customer **+32% ใน ก.ค.** เดือนเดียว, agent features **20M WAU** (Aug 19), overall run rate **+35% QTD**, enterprise **+50% QTD**. ChatGPT for Work **+40% seat ใน 2 เดือน** ชน 7M. ตัวเลขทั้งหมดก่อน Dots launch — แปลว่า Dots ยัง upside ไม่ reflect

## ทำไมสำคัญ

ประเด็นที่หนึ่ง — **$500/เดือนคือ price-anchor ใหม่ของ consumer AI**. ก่อนหน้านี้ consumer AI product ติดเพดาน $200 (ChatGPT Pro, Perplexity Max). Dots เป็นผลิตภัณฑ์แรกที่ consumer-facing กล้าตั้งราคาเท่า **Salesforce เซียลหนึ่ง** หรือ **Microsoft 365 E5 ×3** — สะท้อนว่า OpenAI มั่นใจว่า "autonomous agent worker" คือ category แยกจาก "AI assistant" ที่ consumer เคยจ่าย. ถ้า CAC payback สมเหตุผล, Anthropic, Google, Meta จะตามเร็ว; ถ้า churn สูง, consumer AI ถูก reset floor กลับไป $200

ประเด็นที่สอง — **Enterprise overtaking consumer คือ structural shift**. เดิม VC มอง OpenAI เป็น consumer story (ChatGPT 800M+ WAU). ตอนนี้ enterprise revenue > consumer, enterprise +50% QTD, consumer run rate กลับโตช้ากว่า — valuation framework ของ OpenAI กลายเป็น **enterprise SaaS multiple** (10-15× revenue) ไม่ใช่ consumer internet (25-30× DAU). ที่ **$5OpenB OpenAI ARR เป้า 2027**, enterprise share น่าจะ 60%+ — mix shift นี้คือข่าวใหญ่กว่า product launch

ประเด็นที่สาม — **The Information: Replit → OpenAI $100M+/ปี deal** (ที่ brief รอบที่แล้วรายงาน) + **20M agent WAU + 50% enterprise QTD growth** ต่อกันเป็น picture เดียว: OpenAI กำลัง convert agent momentum เป็น **long-dated enterprise commit** โดยใช้ discount เป็นเครื่องมือ. Anthropic ที่เพิ่งปล่อย Claude Duet (21 ต.ค.) + sandbox-runtime (24 ต.ค.) + Chat/Cowork GA (23 ต.ค.) กำลัง catch up แต่ scale gap น่าจะโตขึ้นก่อน IPO กลาง พ.ย.

## มุม AI Agent Platform

สำหรับ **Builders** (framework/agent companies): **$500 floor เปิดโอกาสให้ agent startup ตั้งราคาสูงกว่า "SaaS seat $20-50" ได้ครั้งแรก**. ถ้า Dots validate ว่า consumer จ่าย $500 สำหรับ always-on agent, agent-native tool ที่ส่งผลงาน "ชัดต่อสัปดาห์" (recruiter agent, analyst agent, lawyer agent) จะมี pricing power ตั้ง $300-600/user — ตัว floor ขยับขึ้นให้ทั้ง category. framework (LangChain, CrewAI, Vercel AI SDK) ที่ host managed agent runtime ก็มี pricing room เพิ่ม

สำหรับ **Users / Business**: การตัดสินใจซื้อ Dots เท่ากับ hire **non-human worker ที่ไม่มี 90-day review** — enterprise procurement ต้องมี **playbook ใหม่** สำหรับ (1) การ assign work ที่ "agent sign document / send email / make payment" ได้ (Anthropic Duet ขอ approval, Dots ไม่ชัด), (2) การ audit agent activity ย้อนหลัง (connects กับ SailPoint Agentic Fabric + Microsoft Entra Agent ID), (3) การกำหนด "agent spending cap" ก่อน rollout — Google Universal Gemini for Work (ข่าว 04) มี hard cap per project ซึ่ง OpenAI Dots **ยังไม่มี enterprise-grade equivalent**

สำหรับ **Ecosystem**: EU regulatory carve-out ของ Dots คือ signal ว่า **agent product กำลัง bifurcate เป็น US tier กับ EU tier** โดยกฎหมาย. ตลาด APAC (Japan, Korea, Singapore, Thailand) ที่มี AI Act lite หรือ voluntary code จะกลายเป็น **testing ground จริง** สำหรับ agent-first product — ไทยที่ ETDA + สดช. กำลังร่าง AI Governance Act (คาด 2027) จะเป็น jurisdiction ที่ agent product อย่าง Dots เข้าได้ก่อน EU หลายเดือน; ethical use case + enterprise pilot ควร start now

## Sources
- [OpenAI Unveils Always-On AI Agent Dots, New $500 Paid Tier (Bloomberg)](https://news.bloombergtax.com/private-equity/openai-unveils-always-on-ai-agent-dots-new-500-paid-tier)
- [OpenAI Dots pricing — plan by plan (eesel.ai)](https://www.eesel.ai/blog/openai-dots-pricing)
- [OpenAI tells investors enterprise revenue overtook ChatGPT consumer business (unite.ai)](https://www.unite.ai/openai-tells-investors-enterprise-revenue-has-overtaken-its-chatgpt-consumer-business/)
- [OpenAI's $500 agent play — the first real price tag for autonomous AI (Forkast)](https://forkast.news/openais-500-agent-play-1-2b-users-4000-apps-and-the-first-real-price-tag-for-autonomous-ai/)

---

## Audio script
OpenAI เปิดตัว Dots ซึ่งเป็น always-on agent ที่รันในคลาวด์ VM ของตัวเอง เก็บงานข้าม conversation ได้ — ที่น่าสนใจคือ pricing structure: Pro 100 ที่ 100 ดอลลาร์ต่อเดือน, Pro 200 ที่ 200, และ Pro 500 ที่ 500 ดอลลาร์ต่อเดือน ทุก tier ได้ dot หนึ่งตัว ชั้น 500 เพิ่ม headroom สูงสุด บวก Astra Ultra. 500 ดอลลาร์ต่อเดือนคือ floor ที่ consumer AI product ไม่เคยกล้าแตะมาก่อน — ก่อนหน้านี้เพดาน consumer อยู่ที่ 200. Rollout ไป US กับ 4,000 กว่าประเทศ ยกเว้น UK, EEA, Switzerland ที่รอ regulatory clearance ภายใต้ EU AI Act. Enterprise, Edu, Healthcare เป็น custom-priced กับ Dots off by default. ตัวเลขที่หนุน pricing นี้คือ scale: OpenAI รายงานเมื่อ 14 สิงหาคมว่า enterprise revenue overtake consumer เป็นครั้งแรก, enterprise run rate เกิน 40 พันล้านดอลลาร์ annualized, business customer โต 32 เปอร์เซ็นต์ในกรกฎาคมเดือนเดียว, agent features ชน 20 ล้าน weekly active user บน Aug 19, overall revenue run rate +35 เปอร์เซ็นต์ QTD, enterprise +50 เปอร์เซ็นต์. ประเด็นต่อจากนี้มีสาม หนึ่ง 500 ดอลลาร์ต่อเดือนคือ price anchor ใหม่ ถ้า validate ได้ Anthropic กับ Google จะตามเร็ว เปิดทางให้ agent-native tool ตั้งราคาสูงกว่า SaaS seat 20-50 ดอลลาร์ได้ครั้งแรก. สอง enterprise overtaking consumer เป็น structural shift — valuation ของ OpenAI กลายเป็น enterprise SaaS multiple ไม่ใช่ consumer internet อีกต่อไป ที่ 500 พันล้านดอลลาร์ ARR เป้า 2027 enterprise share น่าจะเกิน 60 เปอร์เซ็นต์. สาม Dots + Replit deal 100 ล้านต่อปี + agent WAU 20 ล้าน ต่อกันเป็น picture เดียวว่า OpenAI convert agent momentum เป็น long-dated enterprise commitment โดยใช้ discount เป็นเครื่องมือ Anthropic กำลัง catch up ด้วย Claude Duet กับ sandbox-runtime แต่ scale gap น่าจะโตขึ้นก่อน IPO กลางพฤศจิกายน. สำหรับทีมที่ซื้อ Dots มา deploy ควร note ว่ามันคือ hire non-human worker ที่ไม่มี 90-day review ต้องมี playbook การ assign งาน การ audit และการตั้ง spending cap ซึ่ง Dots enterprise edition ยังไม่มี equivalent กับ Google Universal Gemini for Work ที่ hard cap per project ได้ — ตลาด APAC รวมไทยที่มี AI Act lite จะเป็น testing ground จริงก่อน EU อีกหลายเดือน
